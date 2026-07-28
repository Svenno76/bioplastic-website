#!/bin/bash
# Master validation: runs all checks for Creator (pre-commit) or Checker (post-deploy)

set -euo pipefail

MODE="${1:-creator}"  # creator or checker
ARTICLE_FILE="${2:-}"

if [ -z "$ARTICLE_FILE" ] || [ ! -f "$ARTICLE_FILE" ]; then
    echo "Usage: $0 <creator|checker> <article-markdown-file>"
    echo ""
    echo "Modes:"
    echo "  creator  - Pre-commit checks (local files, builds site)"
    echo "  checker  - Post-deploy checks (live URL, no build)"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

echo "═══════════════════════════════════════════"
echo "  BPP Quality Validation — $MODE mode"
echo "  Article: $ARTICLE_FILE"
echo "═══════════════════════════════════════════"

FAIL=0

run_check() {
    local name="$1"
    local script="$2"
    echo ""
    echo "▶ $name"
    if "$script" "$ARTICLE_FILE"; then
        echo "   ✅ $name passed"
    else
        echo "   ❌ $name FAILED"
        FAIL=1
    fi
}

# Creator-specific: readability, hero image, tags, companies
if [ "$MODE" = "creator" ]; then
    run_check "Readability" "$SKILL_DIR/scripts/check-readability.sh"
    run_check "Hero image (local)" "$SKILL_DIR/scripts/check-hero-image.sh"
    run_check "Tags → Glossary" "$SKILL_DIR/scripts/check-tags.sh"
    run_check "Companies → Profiles" "$SKILL_DIR/scripts/check-company.sh"
    
    # Build and verify generated HTML
    echo ""
    echo "▶ Building site for HTML verification..."
    hugo --gc --minify > /dev/null 2>&1
    
    # Extract slug from article filename
    SLUG=$(basename "$ARTICLE_FILE" .md | sed 's/^[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}-//')
    HTML_FILE="public/news/$SLUG/index.html"
    
    if [ -f "$HTML_FILE" ]; then
        run_check "Hero image (built HTML)" "$SKILL_DIR/scripts/check-hero-image-html.sh" "$HTML_FILE"
    else
        echo "   ❌ Built HTML not found: $HTML_FILE"
        FAIL=1
    fi
fi

# Checker-specific: live URL checks (would need URL passed separately)
if [ "$MODE" = "checker" ]; then
    echo "  ⚠️  Checker mode requires live URL — not fully implemented yet"
    # Would use: curl -sL "$LIVE_URL" | run checks on HTML
fi

echo ""
echo "═══════════════════════════════════════════"
if [ $FAIL -eq 0 ]; then
    echo "  ✅ ALL CHECKS PASSED"
    exit 0
else
    echo "  ❌ SOME CHECKS FAILED — DO NOT DEPLOY"
    exit 1
fi