# News Articles Refactoring Guide

This directory contains comprehensive documentation for refactoring all remaining news articles in the bioplastics website to follow a standardized structure.

## Quick Reference

**Status:** 34 files need refactoring across 2025-11, 2025-12, and 2026-01

**Priority:**
1. **TIER 1:** 2025-12 articles (16 files) - includes duplicate file cleanup
2. **TIER 2:** 2026-01 remaining articles (16 files) - includes date corrections
3. **TIER 3:** 2025-11 articles (2 files) - minor changes

**Already Completed:** 13 articles in 2026-01 (dated 2026-01-02 through 2026-01-21)

## Documentation Files

### 1. **REFACTORING_PLAN.md** (1079 lines)
Complete detailed refactoring plan for each individual file including:
- Current front matter for each file
- Specific changes needed (category, tags, company field, etc.)
- Before/after comparisons
- Organized by date range (2025-12, 2026-01, etc.)

**Use this for:** Making detailed edits to individual files

### 2. **FILES_BY_CATEGORY.md**
Organized reference showing:
- Files grouped by priority tier
- Files organized by target category
- Duplicate files to delete
- Date corrections needed
- Category changes required
- Refactoring checklist

**Use this for:** Quick reference, tracking progress, understanding overall structure

### 3. **REFACTORING_EXAMPLES.md**
Six real-world before/after examples showing:
- Simple single-company partnership
- Multi-company partnership with descriptions
- Investment announcement
- Category change required
- Date and category corrections
- Complex M&A transaction

Includes transformation patterns and automated script template.

**Use this for:** Understanding how to make changes correctly, training reference

## Quick Start - What to Do

### For Each Article:

1. **Remove generic tags:** Delete these if present:
   - 'innovation', 'sustainability', 'product', 'product-launch'
   - 'investment', 'funding', 'investment-&-funding'
   - 'partnerships', 'collaboration', 'partnership'
   - 'plant-announcement', 'plant-announcements'
   - 'market-analysis', 'financial-results', 'earnings', 'financial'

2. **Keep only company names as tags:** 
   - Include all companies mentioned (important for partnerships/M&A)

3. **Convert company field to array:**
   ```yaml
   # Before:
   company: "Company Name"
   
   # After:
   company: ["Company Name"]
   ```

4. **Update category if needed:**
   Choose from: Certifications, Financial Results, Investment & Funding, M&A, Market Analysis, Partnerships, Plant Announcement, Product Launch, Regulatory & Policy

5. **Fix "Plant Announcements" → "Plant Announcement"** (singular)

6. **Add company_type field** if missing

### Duplicate File Cleanup:

Delete all capitalized versions, keep lowercase versions:
- Delete: `2025-12-01-Ecopha_Biotech_and_Terra_Sol_Win_Energy...md`
- Keep: `2025-12-01-ecopha-biotech-and-terra-sol-win-energy...md`

### Date Corrections (2026-01):

Four files have incorrect dates that need fixing:
1. `2026-01-06-basf-debuts...`: 2025-03-04 → 2026-01-06
2. `2026-01-06-covationbio...`: 2025-04-14 → 2026-01-06
3. `2026-01-06-fkur...`: 2010-01-06 → 2026-01-06
4. `2026-01-06-totalenergies-corbion...`: 2026-03-27 → 2026-01-06

## Standard Categories

All articles must use ONE of these categories:

- **Certifications** - New certifications, compliance achievements
- **Financial Results** - Quarterly earnings, sales reports, production metrics
- **Investment & Funding** - Funding rounds, grants, investments
- **M&A** - Mergers, acquisitions, divestitures, stake purchases
- **Market Analysis** - Reports, market studies, conference presentations
- **Partnerships** - Joint ventures, collaborations, strategic alliances
- **Plant Announcement** - Facility openings, expansions, commissioning (singular!)
- **Product Launch** - New products, materials, technologies, research breakthroughs
- **Regulatory & Policy** - Regulations, policy changes, compliance announcements

## Common Company Types

When adding company_type field, use:
- "Bioplastic Producer"
- "Technology Company"
- "University"
- "Research Institution"
- "Industry Association"
- "Testing/Certification Company"
- "Consulting Firm"
- "Investment Firm"

## File Statistics

| Task | Count |
|------|-------|
| Delete duplicate capitalized versions | ~13-15 files |
| Fix date errors | 4 files |
| Change "Plant Announcements" to "Plant Announcement" | 2 files |
| Change "News" to appropriate category | 11 files |
| Convert company strings to arrays | 34 files |
| Remove generic tags | 34 files |
| Add/verify company_type field | ~20 files |
| **Total unique files to refactor** | **34 files** |
| **Total operations** | **100+ edits** |

## Next Steps

1. Review REFACTORING_PLAN.md for detailed file-by-file changes
2. Consult FILES_BY_CATEGORY.md for quick lookup by date/category
3. Reference REFACTORING_EXAMPLES.md for how to make changes
4. Start with 2025-12 articles (TIER 1)
5. Progress to 2026-01 remaining articles (TIER 2)
6. Finish with 2025-11 articles (TIER 3)
7. Delete duplicate capitalized filenames

## Key Rules

✓ ALWAYS convert company field to array format
✓ ALWAYS remove generic tags
✓ ALWAYS keep company name tags
✓ ALWAYS use singular "Plant Announcement" (not plural)
✓ ALWAYS pick specific category (never leave as "News")
✓ ALWAYS add company_type when missing
✓ DO NOT remove important company information - just reformat it

✗ DON'T keep generic tags like 'innovation' or 'sustainability'
✗ DON'T use "News" as category
✗ DON'T use "Plant Announcements" (plural)
✗ DON'T keep company fields as strings instead of arrays
✗ DON'T delete files without having backup/verification

---

**Last Updated:** 2026-01-22
**Total Files to Refactor:** 34
**Progress:** 13 of 47 articles completed (28%)
