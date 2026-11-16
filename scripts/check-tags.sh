#!/bin/bash
# REQ-01: tags in a news article must exist as glossary entries.
# Usage:
#   scripts/check-tags.sh <article-markdown-file>   check one file
#   scripts/check-tags.sh --all                     check every content/news/*.md (quiet; fails on first offender)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
GLOSSARY_DIR="$REPO_ROOT/content/glossary"

slugify() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g' | sed 's/[^a-z0-9-]//g' | sed 's/--*/-/g' | sed 's/^-//; s/-$//'
}

check_file() {
    local ARTICLE_FILE="$1"
    local FAIL=0

    # Extract tags: inline array "tags: [A, B]" OR multiline "- A" list
    local TAGS=""
    if grep -q '^tags: *\[' "$ARTICLE_FILE"; then
        TAGS=$(grep '^tags: *\[' "$ARTICLE_FILE" | head -1 | sed 's/^tags: *//; s/\[//g; s/\]//g; s/"//g' | tr ',' '\n')
    elif grep -q '^tags:' "$ARTICLE_FILE"; then
        TAGS=$(sed -n '/^tags:/,/^[a-z_]*:/p' "$ARTICLE_FILE" | grep '^- ' | sed 's/^-[ ]*//; s/"//g')
    else
        echo "  ❌ FAIL: no tags found in front matter: $ARTICLE_FILE"
        return 1
    fi

    while IFS= read -r TAG; do
        TAG=$(echo "$TAG" | xargs)
        [ -z "$TAG" ] && continue
        SLUG=$(slugify "$TAG")
        if [ ! -f "$GLOSSARY_DIR/$SLUG.md" ]; then
            echo "  ❌ FAIL: '$TAG' -> no glossary entry ($SLUG) in $ARTICLE_FILE"
            FAIL=1
        fi
    done <<< "$TAGS"

    return $FAIL
}

if [ "${1:-}" = "--all" ]; then
    FAIL=0
    while IFS= read -r f; do
        check_file "$f" || FAIL=1
    done < <(find "$REPO_ROOT/content/news" -name '*.md' ! -name '_index*')
    if [ $FAIL -eq 0 ]; then
        echo "  ✅ all news tags resolve to glossary entries"
        exit 0
    fi
    echo "  💡 Fix: use only glossary terms as tags, or create the missing glossary entry first (spec §8 rule 11 / REQ-01)."
    exit 1
fi

ARTICLE_FILE="${1:-}"
if [ -z "$ARTICLE_FILE" ] || [ ! -f "$ARTICLE_FILE" ]; then
    echo "Usage: $0 <article-markdown-file> | --all"
    exit 1
fi

echo "🔍 Tag → Glossary check: $ARTICLE_FILE"
if check_file "$ARTICLE_FILE"; then
    echo "  ✅ All tags have glossary entries"
    exit 0
fi
echo "  💡 To fix: use only glossary terms as tags, or create the missing glossary file in content/glossary/"
exit 1
