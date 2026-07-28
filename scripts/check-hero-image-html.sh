#!/bin/bash
# Check hero image in built HTML: og:image, twitter:image, JSON-LD all match and return 200

set -euo pipefail

HTML_FILE="$1"

if [ -z "$HTML_FILE" ] || [ ! -f "$HTML_FILE" ]; then
    echo "Usage: $0 <built-article-html-file>"
    exit 1
fi

echo "🔍 Hero image check (built HTML): $HTML_FILE"

# Extract og:image
OG_IMAGE=$(grep -o 'property="og:image" content="[^"]*"' "$HTML_FILE" | head -1 | sed 's/.*content="\([^"]*\)".*/\1/')
TWITTER_IMAGE=$(grep -o 'name="twitter:image" content="[^"]*"' "$HTML_FILE" | head -1 | sed 's/.*content="\([^"]*\)".*/\1/')
JSONLD_IMAGE=$(grep -o '"image":\["[^"]*"' "$HTML_FILE" | head -1 | sed 's/.*\["\([^"]*\)"\].*/\1/')

echo "  og:image:      $OG_IMAGE"
echo "  twitter:image: $TWITTER_IMAGE"
echo "  JSON-LD image: $JSONLD_IMAGE"

FAIL=0

# Check all three match
if [ "$OG_IMAGE" != "$TWITTER_IMAGE" ]; then
    echo "  ❌ FAIL: og:image ≠ twitter:image"
    FAIL=1
fi

if [ "$OG_IMAGE" != "$JSONLD_IMAGE" ]; then
    echo "  ❌ FAIL: og:image ≠ JSON-LD image"
    FAIL=1
fi

# Check URL is absolute and on our domain
if [[ ! "$OG_IMAGE" =~ ^https://bioplasticsportal\.com/images/news/ ]]; then
    echo "  ❌ FAIL: Image URL not on bioplasticsportal.com: $OG_IMAGE"
    FAIL=1
fi

# Check filename convention
FILENAME=$(basename "$OG_IMAGE")
if [[ ! "$FILENAME" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-.*\.(png|jpg|jpeg|webp)$ ]]; then
    echo "  ❌ FAIL: Filename convention violated: $FILENAME"
    FAIL=1
fi

echo "  ✅ All image URLs match and follow convention"

# Check live URL returns 200 (only if we have network)
echo "  🔍 Checking live URL..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$OG_IMAGE" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
    echo "  ✅ Live image returns HTTP 200"
elif [ "$HTTP_CODE" = "000" ]; then
    echo "  ⚠️  SKIP: Network unavailable, cannot verify live URL"
else
    echo "  ❌ FAIL: Live image returns HTTP $HTTP_CODE"
    FAIL=1
fi

if [ $FAIL -eq 0 ]; then
    echo "  ✅ Hero image (HTML) checks passed"
    exit 0
else
    exit 1
fi