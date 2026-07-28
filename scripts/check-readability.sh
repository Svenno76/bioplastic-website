#!/bin/bash
# Check readability: bullet point density, paragraph length, structure

set -euo pipefail

ARTICLE_FILE="$1"

if [ -z "$ARTICLE_FILE" ] || [ ! -f "$ARTICLE_FILE" ]; then
    echo "Usage: $0 <article-markdown-file>"
    exit 1
fi

echo "🔍 Readability analysis: $ARTICLE_FILE"

# Count bullet points (markdown - or * at start of line, in body only - after front matter)
BODY_START=$(awk '/^---$/{count++} count==2{print NR; exit}' "$ARTICLE_FILE")
if [ -z "$BODY_START" ]; then
    BODY_START=1
fi

BULLET_COUNT=$(tail -n +$((BODY_START + 1)) "$ARTICLE_FILE" | grep -E '^[-*] ' | wc -l)

# Count paragraphs (blank line separated, non-heading, non-bullet, non-code)
PARA_COUNT=$(tail -n +$((BODY_START + 1)) "$ARTICLE_FILE" | awk '
    /^```/ { in_code=!in_code; next }
    in_code { next }
    /^#/ { next }
    /^[-*] / { next }
    /^$/ { if (in_para) { paras++; in_para=0 } next }
    { in_para=1 }
    END { if (in_para) paras++; print paras }
')

# Count headings
H2_COUNT=$(tail -n +$((BODY_START + 1)) "$ARTICLE_FILE" | grep -E '^## ' | wc -l)
H3_COUNT=$(tail -n +$((BODY_START + 1)) "$ARTICLE_FILE" | grep -E '^### ' | wc -l)

# Word count (rough)
WORD_COUNT=$(tail -n +$((BODY_START + 1)) "$ARTICLE_FILE" | wc -w)

echo "  📊 Stats: ${WORD_COUNT} words, ${PARA_COUNT} paragraphs, ${BULLET_COUNT} bullets, ${H2_COUNT} H2, ${H3_COUNT} H3"

# Heuristics
FAIL=0

# Too many bullets relative to paragraphs
if [ "$PARA_COUNT" -gt 0 ]; then
    RATIO=$(( BULLET_COUNT * 100 / PARA_COUNT ))
    if [ "$RATIO" -gt 50 ]; then
        echo "  ⚠️  WARN: Bullet-to-paragraph ratio ${RATIO}% (>50%) — consider converting to prose"
    else
        echo "  ✅ Bullet ratio ${RATIO}% OK"
    fi
fi

# Absolute bullet limit
if [ "$BULLET_COUNT" -gt 10 ]; then
    echo "  ❌ FAIL: ${BULLET_COUNT} bullets (>10) — too many, convert to narrative"
    FAIL=1
elif [ "$BULLET_COUNT" -gt 6 ]; then
    echo "  ⚠️  WARN: ${BULLET_COUNT} bullets (>6) — consider reducing"
fi

# Paragraph length check (very rough - words per paragraph)
if [ "$PARA_COUNT" -gt 0 ] && [ "$WORD_COUNT" -gt 0 ]; then
    AVG_WORDS=$(( WORD_COUNT / PARA_COUNT ))
    if [ "$AVG_WORDS" -gt 120 ]; then
        echo "  ⚠️  WARN: Avg ${AVG_WORDS} words/paragraph (>120) — consider shorter paragraphs"
    else
        echo "  ✅ Avg paragraph length ${AVG_WORDS} words OK"
    fi
fi

# Heading structure
if [ "$H2_COUNT" -eq 0 ] && [ "$WORD_COUNT" -gt 300 ]; then
    echo "  ⚠️  WARN: Long article (${WORD_COUNT} words) with no H2 headings — add section breaks"
fi

# List-heavy sections: check if any H2 section has >3 bullets
# (simplified: just warn if total bullets high)
if [ "$BULLET_COUNT" -gt 8 ]; then
    echo "  ⚠️  WARN: High bullet count suggests list-heavy structure — add narrative transitions"
fi

if [ $FAIL -eq 0 ]; then
    echo "  ✅ Readability checks passed"
    exit 0
else
    exit 1
fi