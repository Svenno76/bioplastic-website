#!/bin/bash
# Check companies: every company must have a profile

set -euo pipefail

ARTICLE_FILE="$1"

if [ -z "$ARTICLE_FILE" ] || [ ! -f "$ARTICLE_FILE" ]; then
    echo "Usage: $0 <article-markdown-file>"
    exit 1
fi

echo "🔍 Company/profile check: $ARTICLE_FILE"

# Extract companies from front matter
COMPANIES_LINE=$(grep '^company:' "$ARTICLE_FILE" | head -1)
if [ -z "$COMPANIES_LINE" ]; then
    echo "  ⚠️  No companies found (required)"
    exit 1
fi

# Parse YAML array
COMPANIES=$(echo "$COMPANIES_LINE" | sed 's/.*company: *\[//; s/\].*//; s/"//g')

FAIL=0
for company in $COMPANIES; do
    company=$(echo "$company" | sed 's/^,//; s/,$//' | xargs)
    [ -z "$company" ] && continue
    
    # Convert to slug
    SLUG=$(echo "$company" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g' | sed 's/--*/-/g' | sed 's/^-//; s/-$//')
    
    # Check primary slug and common variants
    FOUND=false
    for VARIANT in "$SLUG" "${SLUG}-international" "${SLUG}-group" "${SLUG}-inc" "${SLUG}international" "${SLUG}group"; do
        if [ -f "content/companies/${VARIANT}.md" ]; then
            echo "  ✅ Company '$company' → content/companies/${VARIANT}.md"
            FOUND=true
            break
        fi
    done
    
    if [ "$FOUND" = false ]; then
        echo "  ❌ FAIL: Company '$company' → no profile found (tried: $SLUG.md, variants)"
        FAIL=1
    fi
done

if [ $FAIL -eq 0 ]; then
    echo "  ✅ All companies have profiles"
    exit 0
else
    echo ""
    echo "  💡 To fix: create missing company profiles in content/companies/"
    exit 1
fi