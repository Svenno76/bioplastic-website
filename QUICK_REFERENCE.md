# Quick Reference - Article Refactoring Lookup

## For Each Article You Refactor - Use This Checklist

```
Article: [FILENAME]
Date: [YYYY-MM-DD]

✓ TAG REVIEW
  □ Removed 'innovation'? Y/N
  □ Removed 'sustainability'? Y/N
  □ Removed 'product-launch'? Y/N
  □ Removed 'investment-&-funding'? Y/N
  □ Removed 'partnerships'/'collaboration'? Y/N
  □ Removed 'plant-announcement(s)'? Y/N
  □ Removed 'market-analysis'? Y/N
  □ Removed 'financial-results'? Y/N
  □ Kept company names? Y/N
  □ For partnerships/M&A - both companies in tags? Y/N

✓ COMPANY FIELD
  □ Changed from string to array? Y/N
  □ Format: ["Company1", "Company2"]? Y/N
  □ Clean names (no descriptions)? Y/N

✓ CATEGORY
  □ Is it one of approved list? Y/N
  □ Is it singular "Plant Announcement" (not plural)? Y/N
  □ Not using "News"? Y/N

✓ COMPANY TYPE
  □ Field present? Y/N
  □ Value is appropriate? Y/N

✓ DATE
  □ Correct date (YYYY-MM-DD format)? Y/N
  □ No obvious typos (e.g., 2010, 2026-03-27)? Y/N
```

---

## Articles by Date and Status

### TIER 1: 2025-12 (16 files)

| Article | Category | Status | Changes |
|---------|----------|--------|---------|
| 2025-12-01 Ecopha Biotech | Product Launch | ✓ OK | Tags, company array |
| 2025-12-02 Scientists Develop | Product Launch | ✓ OK | Tags, company array |
| 2025-12-03 Breaking Plastic Wave | Regulatory & Policy | ✓ OK | Tags, company array |
| 2025-12-03 EUBP presents | Market Analysis | ✓ OK | Tags, company array |
| 2025-12-04 ALPLA NTCP | Plant Announcement | ⚠ FIX | Category (plural→singular), tags, company array |
| 2025-12-04 CARBIOS Wankai | Plant Announcement | ⚠ FIX | Category (plural→singular), tags, company array |
| 2025-12-05 Innovative Startups | Investment & Funding | ✓ OK | Tags, company array |
| 2025-12-09 TotalEnergies Corbion | Market Analysis | ✓ OK | Tags, company array |
| 2025-12-11 Concordia University | Investment & Funding | ✓ OK | Tags, company array |
| 2025-12-19 UPM Leuna | Plant Announcement | ⚠ FIX | Category (News→Plant Announcement), tags, company array |
| 2025-12-25 RIKEN Saltwater | Product Launch | ✓ OK | Tags, company array |
| 2025-12-31 Loliware Entec | Partnerships | ✓ OK | Tags, company array, add Entec |
| 2025-12-31 Notpla 15M | Financial Results | ✓ OK | Tags, company array |
| 2025-12-31 Sway Atlantic | Partnerships | ✓ OK | Tags, company array, add Atlantic |
| 2025-12-31 Uluu $10.5M | Investment & Funding | ✓ OK | Tags, company array |
| 2025-12-31 Zerocircle $2.3M | Investment & Funding | ✓ OK | Tags, company array |

**Duplicates to DELETE (2025-12):**
- Ecopha_Biotech_and_Terra_Sol...
- Scientists_Develop_New_Plastics...
- Breaking the Plastic Wave 2025.md
- EUBP_presents_the_Results...
- ALPLA_and_NTCP...
- CARBIOS_and_Wankai...
- Innovative_Start_Ups...
- Lubrizol_Unveils...
- TotalEnergies_Corbion...
- Concordia_University...
- Grandpuits__A_Zero_Crude...
- RIKEN_Scientists...
- AIMPLAS_to_Speed_Up...

---

### TIER 2: 2026-01 Remaining (16 files)

| Article | Current | Target | Status | Changes |
|---------|---------|--------|--------|---------|
| 2026-01-05 AI Tool | News | Product Launch | ⚠ FIX | Date?, category, tags, array |
| 2026-01-05 Ingevity Sells | News | M&A | ⚠ FIX | Category, tags, array |
| 2026-01-06 AIMPLAS Training | Product Launch | Product Launch | ✓ OK | Tags, array (or→Market Analysis?) |
| 2026-01-06 BASF Polyethersulfone | Product Launch | Product Launch | ⚠ FIX | **DATE: 2025-03-04→2026-01-06**, tags, array |
| 2026-01-06 CovationBio PTMEG | Product Launch | Product Launch | ⚠ FIX | **DATE: 2025-04-14→2026-01-06**, tags, array |
| 2026-01-06 FKuR Texas | Plant Announcement | Plant Announcement | ⚠ FIX | **DATE: 2010-01-06→2026-01-06**, tags, array |
| 2026-01-06 TotalEnergies Benvic | Partnerships | Partnerships | ⚠ FIX | **DATE: 2026-03-27→2026-01-06**, tags, array, add Benvic |
| 2026-01-07 Aduro $20M | News | Investment & Funding | ⚠ FIX | Category, tags, array |
| 2026-01-07 BASF Steam Cracker | News | Plant Announcement | ⚠ FIX | Category, tags, array |
| 2026-01-08 MTU Biorefinery | News | Plant Announcement | ⚠ FIX | Category, tags, array, update company_type |
| 2026-01-08 Natur-Tec Sales | News | Financial Results | ⚠ FIX | Category, tags, array |
| 2026-01-08 SABIC Divests | News | M&A | ⚠ FIX | Category, tags, array |
| 2026-01-09 Orinko Omikron | News | M&A | ⚠ FIX | Category, tags, array, add Omikron |
| 2026-01-12 AIMPLAS Biovalsa | News | Product Launch | ⚠ FIX | Category, tags, array |
| 2026-01-14 Japanese Researchers | News | Product Launch | ⚠ FIX | Category, tags, array, update company_type |
| 2026-01-15 L'Oréal Startups | News | Investment & Funding | ⚠ FIX | Category, tags, array, update company_type |

**Date Corrections Required:**
- 2026-01-06-basf-debuts: 2025-03-04 → 2026-01-06
- 2026-01-06-covationbio: 2025-04-14 → 2026-01-06
- 2026-01-06-fkur: 2010-01-06 → 2026-01-06
- 2026-01-06-totalenergies-corbion: 2026-03-27 → 2026-01-06

---

### TIER 3: 2025-11 (2 files)

| Article | Category | Status | Changes |
|---------|----------|--------|---------|
| 2025-11-05 CJ Biomaterials BIQ | Partnerships | ✓ OK | Tags, array, add BIQ Materials |
| 2025-11-05 Fibre Screw Caps | Product Launch | ✓ OK | Tags, company array |

---

## Category Definitions

**Use these to decide which category applies:**

### Certifications
New certifications achieved, compliance awards, official recognitions

### Financial Results
Quarterly earnings, annual reports, production metrics, sales milestones

### Investment & Funding
Funding rounds (Series A, B, etc.), grants awarded, investor backing, capital raises

### M&A
Mergers, acquisitions, stake purchases (>10%), divestitures, spin-offs

### Market Analysis
Reports published, market studies, conference presentations, industry analysis

### Partnerships
Joint ventures, collaborations, strategic alliances, supply agreements

### Plant Announcement
Facility openings, expansions, groundbreaking, commissioning, location announcements

### Product Launch
New products, materials, technologies, research breakthroughs, innovations

### Regulatory & Policy
Regulations enacted, policy changes, compliance announcements, government actions

---

## Tag Decision Tree

Question: What should go in the tags field?

```
Start: You have an article

Q1: Is this about a company?
   YES → Include company name(s) in tags
   NO  → Tags should still be minimal

Q2: Is this a partnership or M&A?
   YES → Include ALL companies involved in tags
   NO  → Continue

Q3: Does the article mention a generic concept?
   YES → Check if it's in the removal list
         If yes: REMOVE IT
         If no: KEEP IT
   NO  → Continue

Q4: Is there anything left other than company names?
   NO  → You're done (tags = company names only)
   YES → Verify those aren't generic terms
```

---

## Generic Terms to ALWAYS Remove

```
innovation              market-analysis
sustainability          financial-results
product                 earnings
product-launch          financial
investment              regulatory-&-policy
funding                 policy
investment-&-funding
partnerships
collaboration
partnership
plant-announcement
plant-announcements
```

---

## Company Type Suggestions

Based on the article content, choose:

```
Bioplastic Producer          - Makes bioplastics/polymers
Technology Company           - Tech/engineering focused
University                   - Academic institution
Research Institution         - R&D focused (non-university)
Industry Association         - Trade group
Testing/Certification        - Labs, certifiers
Consulting Firm              - Advisory/consulting
Investment Firm              - VC, PE, financial
NGO/Non-profit               - Advocacy, non-profit
Government Agency            - Public sector
```

---

## Examples from Completed Refactoring

### Before
```yaml
tags: ['Braskem', 'product-launch', 'innovation', 'product']
category: "Product Launch"
company: "Braskem"
```

### After
```yaml
tags: ['Braskem']
category: "Product Launch"
company: ["Braskem"]
company_type: "Bioplastic Producer"
```

---

### Before
```yaml
tags: ['Orinko Advanced Plastics', 'innovation', 'sustainability']
category: "News"
company: "Orinko Advanced Plastics"
```

### After
```yaml
tags: ['Orinko Advanced Plastics', 'Omikron']
category: "M&A"
company: ["Orinko Advanced Plastics", "Omikron"]
company_type: "Bioplastic Producer"
```

---

### Before
```yaml
tags: ['CJ Biomaterials', 'partnerships']
category: "Partnerships"
company: "CJ Biomaterials"
```

### After
```yaml
tags: ['CJ Biomaterials', 'BIQ Materials']
category: "Partnerships"
company: ["CJ Biomaterials", "BIQ Materials"]
company_type: "Bioplastic Producer"
```

---

## File Statistics

- Total articles to refactor: **34**
- Total duplicate files to delete: **~13-15**
- Total date corrections: **4**
- Total category changes: **13**
- Total generic tags to remove: **100+**
- Total company fields to convert: **34**

---

## Documentation Files

1. **REFACTORING_README.md** - Master guide
2. **REFACTORING_PLAN.md** - Detailed per-file plan
3. **FILES_BY_CATEGORY.md** - Category organization
4. **REFACTORING_EXAMPLES.md** - Before/after examples
5. **QUICK_REFERENCE.md** - This file!

---

Last Updated: 2026-01-22
