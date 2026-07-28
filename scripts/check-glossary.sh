#!/bin/bash
# Check all tags in article have corresponding glossary entries

set -euo pipefail

ARTICLE_FILE="$1"

if [ -z "$ARTICLE_FILE" ] || [ ! -f "$ARTICLE_FILE" ]; then
    echo "Usage: $0 <article-markdown-file>"
    exit 1
fi

# Extract tags from front matter (between tags: [ and ])
TAGS_LINE=$(grep '^tags:' "$ARTICLE_FILE" | head -1)
if [ -z "$TAGS_LINE" ]; then
    echo "⚠️  No tags found in front matter"
    exit 0
fi

# Parse tags array: tags: ["Tag1", "Tag2"] -> Tag1 Tag2
TAGS=$(echo "$TAGS_LINE" | sed 's/.*tags: *\[//' | sed 's/\].*//' | sed 's/"//g' | sed 's/,/ /g')

MISSING_GLOSSARY=()

for TAG in $TAGS; do
    # Convert tag to glossary slug: lowercase, spaces->hyphens, remove special chars
    SLUG=$(echo "$TAG" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g' | sed 's/--*/-/g' | sed 's/^-//; s/-$//')
    
    # Check if glossary entry exists
    GLOSSARY_FILE="content/glossary/$SLUG.md"
    if [ ! -f "$GLOSSARY_FILE" ]; then
        MISSING_GLOSSARY+=("$TAG -> $SLUG.md")
    fi
done

if [ ${#MISSING_GLOSSARY[@]} -gt 0 ]; then
    echo "❌ FAIL: Missing glossary entries for tags:"
    for M in "${MISSING_GLOSSARY[@]}"; do
        echo "   - $M"
    done
    echo ""
    echo "👉 Action needed: Create glossary entries or request approval for new terms"
    exit 1
else
    echo "✅ All tags have glossary entries"
    exit 0
fi