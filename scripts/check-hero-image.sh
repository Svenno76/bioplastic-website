#!/bin/bash
# Check hero image: local file exists, front matter matches, filename convention

set -euo pipefail

ARTICLE_FILE="$1"

if [ -z "$ARTICLE_FILE" ] || [ ! -f "$ARTICLE_FILE" ]; then
    echo "Usage: $0 <article-markdown-file>"
    exit 1
fi

echo "🔍 Hero image check: $ARTICLE_FILE"

# Extract featured_image from front matter
FEATURED_IMAGE=$(grep '^featured_image:' "$ARTICLE_FILE" | sed 's/.*: *"//; s/".*//' | head -1)

if [ -z "$FEATURED_IMAGE" ]; then
    echo "  ❌ FAIL: No featured_image in front matter"
    exit 1
fi

echo "  Front matter: $FEATURED_IMAGE"

# Check filename convention: /images/news/YYYY-MM-DD-slug.png
FILENAME=$(basename "$FEATURED_IMAGE")
if [[ ! "$FILENAME" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}-.*\.(png|jpg|jpeg|webp)$ ]]; then
    echo "  ❌ FAIL: Filename convention violated: $FILENAME (expected YYYY-MM-DD-slug.png)"
    exit 1
fi

# Check local file exists
LOCAL_PATH="static${FEATURED_IMAGE}"
if [ ! -f "$LOCAL_PATH" ]; then
    echo "  ❌ FAIL: Local file not found: $LOCAL_PATH"
    exit 1
fi

echo "  ✅ Local file exists: $LOCAL_PATH"
echo "  ✅ Filename convention OK: $FILENAME"

# Check reuse in last 30 days
echo "  🔍 Checking 30-day reuse..."
REUSE_COUNT=$(find content/news -name "*.md" -mtime -30 -exec grep -l "featured_image.*$FILENAME" {} \; | grep -v "$ARTICLE_FILE" | wc -l)
if [ "$REUSE_COUNT" -gt 0 ]; then
    echo "  ❌ FAIL: Same hero image used in last 30 days ($REUSE_COUNT other articles)"
    find content/news -name "*.md" -mtime -30 -exec grep -l "featured_image.*$FILENAME" {} \; | grep -v "$ARTICLE_FILE"
    exit 1
fi

echo "  ✅ No reuse in last 30 days"

exit 0