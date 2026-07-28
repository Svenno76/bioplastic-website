#!/bin/bash
# Check tags in article have corresponding glossary entries

set -euo pipefail

ARTICLE_FILE="$1"

if [ -z "$ARTICLE_FILE" ] || [ ! -f "$ARTICLE_FILE" ]; then
    echo "Usage: $0 <article-markdown-file>"
    exit 1
fi

echo "🔍 Tag → Glossary check: $ARTICLE_FILE"

# Extract tags from front matter (YAML array)
TAGS_LINE=$(grep '^tags:' "$ARTICLE_FILE" | head -1)
if [ -z "$TAGS_LINE" ]; then
    echo "  ❌ FAIL: No tags found in front matter"
    exit 1
fi

# Parse YAML array - handles both "tags: [A, B]" and "tags:\n  - A\n  - B"
TAGS=$(echo "$TAGS_LINE" | sed 's/.*tags: *//')

# If multiline format, we'd need different parsing - for now assume inline array
# Remove brackets and quotes, split by comma
TAGS=$(echo "$TAGS" | sed 's/\[//g; s/\]//g; s/"//g; s/,/ /g')

FAIL=0

for TAG in $TAGS; do
    TAG=$(echo "$TAG" | xargs)  # trim
    [ -z "$TAG" ] && continue
    
    # Convert to glossary slug
    SLUG=$(echo "$TAG" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g' | sed 's/--*/-/g' | sed 's/^-//; s/-$//')
    
    GLOSSARY_FILE="content/glossary/$SLUG.md"
    if [ -f "$GLOSSARY_FILE" ]; then
        echo "  ✅ '$TAG' → $GLOSSARY_FILE"
    else
        echo "  ❌ FAIL: '$TAG' → no glossary entry ($GLOSSARY_FILE missing)"
        FAIL=1
    fi
done

if [ $FAIL -eq 0 ]; then
    echo "  ✅ All tags have glossary entries"
    exit 0
else
    echo ""
    echo "  💡 To fix: create missing glossary files in content/glossary/"
    echo ry/"
    exit 1
fi