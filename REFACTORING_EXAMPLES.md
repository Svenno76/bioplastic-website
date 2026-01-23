# Refactoring Examples - Before and After

## Example 1: Simple Single-Company Partnership (2025-12-31)

### File: `2025-12-31-loliware-partners-with-entec.md`

#### BEFORE:
```yaml
title: "Loliware partners with Entec"
date: 2025-12-31
draft: false
summary: "Loliware partnered with Entec to develop seaweed biopolymer solutions."
tags: ['Loliware', 'partnerships', 'collaboration', 'partnership']
category: "Partnerships"
company: "Loliware"
source: "Perplexity Rev2"
```

#### AFTER:
```yaml
title: "Loliware partners with Entec"
date: 2025-12-31
draft: false
summary: "Loliware partnered with Entec to develop seaweed biopolymer solutions."
tags: ['Loliware', 'Entec']
category: "Partnerships"
company: ["Loliware", "Entec"]
company_type: "Bioplastic Producer"
source: "Perplexity Rev2"
```

**Changes Made:**
1. ✓ Removed generic tags: 'partnerships', 'collaboration', 'partnership'
2. ✓ Added partner company to tags: 'Entec'
3. ✓ Converted company from string to array: ["Loliware", "Entec"]
4. ✓ Added company_type field

---

## Example 2: Two-Company Partnership with Descriptions (2025-12-04)

### File: `2025-12-04-alpla-and-ntcp-pilot-solvent-based-process-for-food-safe-recycled-hdpe.md`

#### BEFORE:
```yaml
title: "ALPLA and NTCP Pilot Solvent-Based Process for Food-Safe Recycled HDPE"
date: 2025-12-04
draft: false
summary: "ALPLA and NTCP are piloting a solvent-based process in the Netherlands..."
tags: ['ALPLA and NTCP (National Test Centre Circular Plastics)', 'plant-announcements']
category: "Plant Announcements"
company: "ALPLA and NTCP (National Test Centre Circular Plastics)"
source: "ALPLA"
```

#### AFTER:
```yaml
title: "ALPLA and NTCP Pilot Solvent-Based Process for Food-Safe Recycled HDPE"
date: 2025-12-04
draft: false
summary: "ALPLA and NTCP are piloting a solvent-based process in the Netherlands..."
tags: ['ALPLA', 'NTCP']
category: "Plant Announcement"
company: ["ALPLA", "NTCP"]
company_type: "Bioplastic Producer"
source: "ALPLA"
```

**Changes Made:**
1. ✓ Removed generic tag: 'plant-announcements'
2. ✓ Simplified company names in tags (removed parenthetical descriptions)
3. ✓ Fixed category from "Plant Announcements" (plural) to "Plant Announcement" (singular)
4. ✓ Converted company from string to array with clean names
5. ✓ Added company_type field

---

## Example 3: Investment Announcement (2025-12-05)

### File: `2025-12-05-innovative-start-ups-honored-at-the-isc3-innovation-challenge-2025-power2polymers-from-germany-wins-top-prize.md`

#### BEFORE:
```yaml
title: "Innovative Start-Ups Honored at the ISC3 Innovation Challenge 2025 – Power2Polymers from Germany wins top prize"
date: 2025-12-05
draft: false
summary: "Power2Polymers"
tags: ['Power2Polymers', 'investment-&-funding', 'investment', 'funding']
category: "Investment & Funding"
company: "Power2Polymers"
company_type: "Technology Company"
source: "Informationsdienst Wissenschaft"
```

#### AFTER:
```yaml
title: "Innovative Start-Ups Honored at the ISC3 Innovation Challenge 2025 – Power2Polymers from Germany wins top prize"
date: 2025-12-05
draft: false
summary: "Power2Polymers"
tags: ['Power2Polymers']
category: "Investment & Funding"
company: ["Power2Polymers"]
company_type: "Technology Company"
source: "Informationsdienst Wissenschaft"
```

**Changes Made:**
1. ✓ Removed generic tags: 'investment-&-funding', 'investment', 'funding'
2. ✓ Kept single company name in tags
3. ✓ Converted company from string to array
4. ✓ Category already correct - no change needed
5. ✓ Company_type already present - no change needed

---

## Example 4: Category Change Required (2026-01-05)

### File: `2026-01-05-ingevity-sells-cto-refinery-for--110m-in-high-value-strategi.md`

#### BEFORE:
```yaml
title: "Ingevity Sells CTO Refinery for $110M in High-Value Strategic Pivot"
date: 2026-01-05
draft: false
summary: "Ingevity has completed the $110 million sale of its Crude Tall Oil refinery..."
tags: ['Ingevity', 'innovation', 'sustainability']
category: "News"
company: "Ingevity"
company_type: "Bioplastic Producer"
source: "BriefGlance"
```

#### AFTER:
```yaml
title: "Ingevity Sells CTO Refinery for $110M in High-Value Strategic Pivot"
date: 2026-01-05
draft: false
summary: "Ingevity has completed the $110 million sale of its Crude Tall Oil refinery..."
tags: ['Ingevity']
category: "M&A"
company: ["Ingevity"]
company_type: "Bioplastic Producer"
source: "BriefGlance"
```

**Changes Made:**
1. ✓ Removed generic tags: 'innovation', 'sustainability'
2. ✓ Kept company name in tags
3. ✓ Changed category from "News" to "M&A" (asset sale is a merger/acquisition event)
4. ✓ Converted company from string to array
5. ✓ Company_type remains correct

---

## Example 5: Date and Category Correction (2026-01-06)

### File: `2026-01-06-fkur-launches-bioplastic-development-in-texas.md`

#### BEFORE:
```yaml
title: "FKuR Launches Bioplastic Development in Texas"
date: 2010-01-06
draft: false
summary: "German bioplastic company FKuR is gearing up operations in Texas..."
tags: ['FKuR', 'plant-announcement', 'manufacturing', 'capacity']
category: "Plant Announcement"
company: "FKuR"
source: "Perplexity Rev2"
```

#### AFTER:
```yaml
title: "FKuR Launches Bioplastic Development in Texas"
date: 2026-01-06
draft: false
summary: "German bioplastic company FKuR is gearing up operations in Texas..."
tags: ['FKuR']
category: "Plant Announcement"
company: ["FKuR"]
company_type: "Bioplastic Producer"
source: "Perplexity Rev2"
```

**Changes Made:**
1. ✓ Fixed date from "2010-01-06" to "2026-01-06" (obvious typo)
2. ✓ Removed generic tags: 'plant-announcement', 'manufacturing', 'capacity'
3. ✓ Kept company name in tags
4. ✓ Category already correct (singular "Plant Announcement")
5. ✓ Converted company from string to array
6. ✓ Added company_type field

---

## Example 6: Complex Multi-Company M&A (2026-01-09)

### File: `2026-01-09-orinko-advanced-plastics-acquires-70--stake-in-omikron.md`

#### BEFORE:
```yaml
title: "Orinko Advanced Plastics Acquires 70% Stake in Omikron"
date: 2026-01-09
draft: false
summary: "Orinko Advanced Plastics has strengthened its position in the sustainable materials market by acquiring a 70% controlling stake in Omikron..."
tags: ['Orinko Advanced Plastics', 'innovation', 'sustainability']
category: "News"
company: "Orinko Advanced Plastics"
company_type: "Bioplastic Producer"
source: "Adsale CPRJ"
```

#### AFTER:
```yaml
title: "Orinko Advanced Plastics Acquires 70% Stake in Omikron"
date: 2026-01-09
draft: false
summary: "Orinko Advanced Plastics has strengthened its position in the sustainable materials market by acquiring a 70% controlling stake in Omikron..."
tags: ['Orinko Advanced Plastics', 'Omikron']
category: "M&A"
company: ["Orinko Advanced Plastics", "Omikron"]
company_type: "Bioplastic Producer"
source: "Adsale CPRJ"
```

**Changes Made:**
1. ✓ Removed generic tags: 'innovation', 'sustainability'
2. ✓ Added acquired company to tags: 'Omikron'
3. ✓ Changed category from "News" to "M&A" (acquisition/stake purchase)
4. ✓ Added acquired company to array: ["Orinko Advanced Plastics", "Omikron"]
5. ✓ Company_type already correct

---

## Summary of Transformation Patterns

### Pattern 1: Generic Tag Removal
**Always remove these tags (they match or describe the category):**
- 'innovation', 'sustainability', 'product', 'product-launch'
- 'investment', 'funding', 'investment-&-funding'
- 'partnerships', 'collaboration', 'partnership'
- 'plant-announcement', 'plant-announcements'
- 'market-analysis', 'financial-results', 'earnings', 'financial'
- 'regulatory-&-policy', 'policy'

**Always keep these tags:**
- Company names (exact matches from content)
- For partnerships/M&A: ALL involved company names

### Pattern 2: Company Field Conversion
```yaml
# BEFORE (string format)
company: "Company Name"
company: "Company 1 and Company 2"
company: "Company Name (Description)"

# AFTER (array format)
company: ["Company Name"]
company: ["Company 1", "Company 2"]
company: ["Company Name"]  # Keep clean, move description elsewhere if needed
```

### Pattern 3: Category Standardization
```yaml
# DO NOT USE:
category: "News"              # Too generic - pick specific category
category: "Plant Announcements"  # Plural - should be singular
category: "innovation"        # Lowercase - should be titlecase

# USE INSTEAD (pick appropriate):
category: "Certifications"
category: "Financial Results"
category: "Investment & Funding"
category: "M&A"
category: "Market Analysis"
category: "Partnerships"
category: "Plant Announcement"
category: "Product Launch"
category: "Regulatory & Policy"
```

### Pattern 4: Company Type Field
**Add if missing. Common values:**
- "Bioplastic Producer"
- "Technology Company"
- "University"
- "Research Institution"
- "Industry Association"
- "Testing/Certification Company"
- "Consulting Firm"
- "Investment Firm"

---

## Automated Refactoring Script Template

```bash
#!/bin/bash
# Template for batch refactoring with sed/yq

FILE="$1"

# 1. Fix date (if incorrect)
# yq eval '.date = "2026-01-06"' "$FILE" -i

# 2. Change category
# yq eval '.category = "M&A"' "$FILE" -i

# 3. Update tags (remove generic ones, keep company names)
# yq eval '.tags = ["CompanyName"]' "$FILE" -i

# 4. Convert company to array
# yq eval '.company = ["CompanyName"]' "$FILE" -i

# 5. Add/update company_type
# yq eval '.company_type = "Bioplastic Producer"' "$FILE" -i

echo "Refactored: $FILE"
```

**Note:** Actual refactoring should be done with proper YAML handling to avoid syntax errors.

