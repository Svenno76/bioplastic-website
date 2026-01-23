# News Articles Refactoring Plan

## Summary Statistics

**Total 2025-12 Articles Needing Refactoring:** 16 files (includes duplicates with capitalized filenames)
**Total Remaining 2026-01 Articles:** 16 files (not yet refactored)
**Total 2025-11 Articles:** 2 files (minor changes needed)

**Already Refactored (2026-01):**
- 2026-01-02-technip-energies* 
- 2026-01-03-technip-energies*
- 2026-01-12-solena-materials*
- 2026-01-13-boss*
- 2026-01-14-radicle*
- 2026-01-16-beam*
- 2026-01-16-primient*
- 2026-01-19-borealis*
- 2026-01-19-teysha*
- 2026-01-19-vioneo*
- 2026-01-20-avantium*
- 2026-01-20-zhongke*
- 2026-01-21-braskem*

---

## 2025-12 ARTICLES (16 files needing refactoring)

### 2025-12-01 | Ecopha Biotech and Terra Sol Win Energy & Renewables Award

**File:** `2025-12-01-ecopha-biotech-and-terra-sol-win-energy-renewables-award-at-the-2025-innovation-aus-award-for-breakthrough-pha-technology.md`

**Current Front Matter:**
```yaml
title: "Ecopha Biotech and Terra Sol Win Energy & Renewables Award at the 2025 Innovation Aus award for Breakthrough PHA Technology"
date: 2025-12-01
draft: false
summary: "Ecopha Biotech and design partner Terra Sol Studio secured the 2025 InnovationAus Energy & Renewable"
tags: ['Ecopha Biotech and Terra Sol Studio', 'product-launch', 'innovation', 'product']
category: "Product Launch"
company: "Ecopha Biotech and Terra Sol Studio"
source: "News Hub"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Product Launch" (correct)
- **Tags:** 
  - REMOVE: 'product-launch', 'innovation', 'product' (generic)
  - KEEP: ['Ecopha Biotech', 'Terra Sol Studio']
  - NEW: Keep only company names
- **Company Field:** 
  - CHANGE FROM: `"Ecopha Biotech and Terra Sol Studio"` (string)
  - CHANGE TO: `["Ecopha Biotech", "Terra Sol Studio"]` (array)
- **Add:** company_type field if applicable

---

### 2025-12-02 | Scientists Develop New Plastics That Break Down Safely

**File:** `2025-12-02-scientists-develop-new-plastics-that-break-down-safely-instead-of-polluting.md`

**Current Front Matter:**
```yaml
title: "Scientists Develop New Plastics That Break Down Safely Instead of Polluting"
date: 2025-12-02
draft: false
summary: "Rutgers University scientists have engineered novel plastics that naturally degrade under everyday c"
tags: ['Rutgers University', 'product-launch', 'innovation', 'product']
category: "Product Launch"
company: "Rutgers University"
company_type: "University"
source: "Rutgers University"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Product Launch" (correct)
- **Tags:** 
  - REMOVE: 'product-launch', 'innovation', 'product' (generic)
  - KEEP: ['Rutgers University']
- **Company Field:** 
  - CHANGE FROM: `"Rutgers University"` (string)
  - CHANGE TO: `["Rutgers University"]` (array)
- **Company Type:** ✓ KEEP "University"

---

### 2025-12-03 | Breaking the Plastic Wave 2025 Global Report

**File:** `2025-12-03-breaking-the-plastic-wave-2025-global-report-warns-of-doubling-pollution-without-urgent-action.md`

**Current Front Matter:**
```yaml
title: "Breaking the Plastic Wave 2025: Global Report Warns of Doubling Pollution Without Urgent Action"
date: 2025-12-03
draft: false
summary: "New landmark report from The Pew Charitable Trusts reveals plastic pollution could more than double "
tags: ['The Pew Charitable Trusts', 'regulatory-&-policy']
category: "Regulatory & Policy"
company: "The Pew Charitable Trusts"
source: "The Pew Charitable Trusts"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Regulatory & Policy" (correct - this is a policy report)
- **Tags:** 
  - REMOVE: 'regulatory-&-policy' (generic, matches category)
  - KEEP: ['The Pew Charitable Trusts']
- **Company Field:** 
  - CHANGE FROM: `"The Pew Charitable Trusts"` (string)
  - CHANGE TO: `["The Pew Charitable Trusts"]` (array)

---

### 2025-12-03 | EUBP presents the Results of the 2025 Market Data Report

**File:** `2025-12-03-eubp-presents-the-results-of-the-2025-market-data-report.md`

**Current Front Matter:**
```yaml
title: "EUBP presents the Results of the 2025 Market Data Report"
date: 2025-12-03
draft: false
summary: "European Bioplastics' 2025 Market Data Report projects a doubling of global biobased plastics produc"
tags: ['European Bioplastics (EUBP)', 'market-analysis']
category: "Market Analysis"
company: "European Bioplastics (EUBP)"
company_type: "Testing/Certification Company"
source: "European Bioplastics"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Market Analysis" (correct)
- **Tags:** 
  - REMOVE: 'market-analysis' (generic, matches category)
  - KEEP: ['European Bioplastics']
- **Company Field:** 
  - CHANGE FROM: `"European Bioplastics (EUBP)"` 
  - CHANGE TO: `["European Bioplastics"]` (array, remove acronym from array)
- **Company Type:** ✓ KEEP "Testing/Certification Company"

---

### 2025-12-04 | ALPLA and NTCP Pilot Solvent-Based Process

**File:** `2025-12-04-alpla-and-ntcp-pilot-solvent-based-process-for-food-safe-recycled-hdpe.md`

**Current Front Matter:**
```yaml
title: "ALPLA and NTCP Pilot Solvent-Based Process for Food-Safe Recycled HDPE"
date: 2025-12-04
draft: false
summary: "ALPLA and NTCP are piloting a solvent-based process in the Netherlands to produce food-safe recycled"
tags: ['ALPLA and NTCP (National Test Centre Circular Plastics)', 'plant-announcements']
category: "Plant Announcements"
company: "ALPLA and NTCP (National Test Centre Circular Plastics)"
source: "ALPLA"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "Plant Announcements" (plural)
  - CHANGE TO: "Plant Announcement" (singular)
- **Tags:** 
  - REMOVE: 'plant-announcements' (generic, matches category)
  - KEEP: ['ALPLA', 'NTCP']
- **Company Field:** 
  - CHANGE FROM: `"ALPLA and NTCP (National Test Centre Circular Plastics)"` (string with description)
  - CHANGE TO: `["ALPLA", "NTCP"]` (array, clean names)

---

### 2025-12-04 | CARBIOS and Wankai seal major deal

**File:** `2025-12-04-carbios-and-wankai-seal-major-deal-to-launch-asias-first-large-scale-pet-biorecycling-plant.md`

**Current Front Matter:**
```yaml
title: "CARBIOS and Wankai seal major deal to launch Asia's first large-scale PET biorecycling plant"
date: 2025-12-04
draft: false
summary: "CARBIOS and Wankai New Materials have finalized a landmark agreement to establish a joint venture fo"
tags: ['CARBIOS and Wankai New Materials', 'plant-announcements']
category: "Plant Announcements"
company: "CARBIOS and Wankai New Materials"
source: "CARBIOS Newsroom"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "Plant Announcements" (plural)
  - CHANGE TO: "Plant Announcement" (singular)
- **Tags:** 
  - REMOVE: 'plant-announcements' (generic)
  - KEEP: ['CARBIOS', 'Wankai']
- **Company Field:** 
  - CHANGE FROM: `"CARBIOS and Wankai New Materials"` 
  - CHANGE TO: `["CARBIOS", "Wankai New Materials"]` (array)

---

### 2025-12-05 | Innovative Start-Ups Honored at ISC3 Innovation Challenge

**File:** `2025-12-05-innovative-start-ups-honored-at-the-isc3-innovation-challenge-2025-power2polymers-from-germany-wins-top-prize.md`

**Current Front Matter:**
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

**Refactoring Plan:**
- **Category:** ✓ KEEP "Investment & Funding" (award/recognition, could be Product Launch or Investment & Funding - funding context makes this correct)
- **Tags:** 
  - REMOVE: 'investment-&-funding', 'investment', 'funding' (generic)
  - KEEP: ['Power2Polymers']
- **Company Field:** 
  - CHANGE FROM: `"Power2Polymers"` 
  - CHANGE TO: `["Power2Polymers"]` (array)
- **Company Type:** ✓ KEEP "Technology Company"

---

### 2025-12-09 | TotalEnergies Corbion Highlights PLA Innovations

**File:** `2025-12-09-totalenergies-corbion-highlights-pla-innovations-and-chemical-recycling-at-chinese-conference.md`

**Current Front Matter:**
```yaml
title: "TotalEnergies Corbion Highlights PLA Innovations and Chemical Recycling at Chinese Conference"
date: 2025-12-09
draft: false
summary: "TotalEnergies Corbion showcased its Luminy® PLA innovations"
tags: ['TotalEnergies Corbion', 'market-analysis']
category: "Market Analysis"
company: "TotalEnergies Corbion"
company_type: "Bioplastic Producer"
source: "TotalEnergies Corbion Newsroom"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Market Analysis" (conference presentation about products/market)
- **Tags:** 
  - REMOVE: 'market-analysis' (generic)
  - KEEP: ['TotalEnergies Corbion']
- **Company Field:** 
  - CHANGE FROM: `"TotalEnergies Corbion"` 
  - CHANGE TO: `["TotalEnergies Corbion"]` (array - JV, keep as single entity)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2025-12-11 | Concordia University Expands Sustainable Biomanufacturing Capacity

**File:** `2025-12-11-concordia-university-expands-sustainable-biomanufacturing-capacity-with-5m-investment.md`

**Current Front Matter:**
```yaml
title: "Concordia University Expands Sustainable Biomanufacturing Capacity with $5M Investment"
date: 2025-12-11
draft: false
summary: "Concordia University has significantly upgraded its Genome Foundry and Bioprocessing facilities with"
tags: ['Concordia University', 'investment-&-funding', 'investment', 'funding']
category: "Investment & Funding"
company: "Concordia University"
company_type: "University"
source: "Concordia University News"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Investment & Funding" (correct - $5M investment announcement)
- **Tags:** 
  - REMOVE: 'investment-&-funding', 'investment', 'funding' (generic)
  - KEEP: ['Concordia University']
- **Company Field:** 
  - CHANGE FROM: `"Concordia University"` 
  - CHANGE TO: `["Concordia University"]` (array)
- **Company Type:** ✓ KEEP "University"

---

### 2025-12-19 | UPM unlocks new bio-based markets as Leuna biorefinery

**File:** `2025-12-19-upm-unlocks-new-bio-based-markets-as-leuna-biorefinery-produ.md`

**Current Front Matter:**
```yaml
title: "UPM unlocks new bio-based markets as Leuna biorefinery produces its first commercial product"
date: 2025-12-19
draft: false
summary: "UPM has officially launched commercial production at its Leuna biorefinery, marking a transformative step in replacing fossil-based raw materials with renewable, wood-based biochemicals."
tags: ['UPM', 'innovation', 'sustainability']
category: "News"
company: "UPM"
company_type: "Bioplastic Producer"
source: "UPM"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Plant Announcement" (commercial production launch at facility)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['UPM']
- **Company Field:** 
  - CHANGE FROM: `"UPM"` 
  - CHANGE TO: `["UPM"]` (array)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2025-12-25 | RIKEN Scientists Develop Saltwater-Safe

**File:** `2025-12-25-riken-scientists-develop-saltwater-safe.md`

**Current Front Matter:**
```yaml
title: "RIKEN Scientists Develop Saltwater-Safe"
date: 2025-12-25
draft: false
summary: "Researchers at RIKEN's Center for Emergent Matter Science (CEMS)"
tags: ['RIKEN Center for Emergent Matter Science (CEMS)', 'product-launch', 'innovation', 'product']
category: "Product Launch"
company: "RIKEN Center for Emergent Matter Science (CEMS)"
company_type: "University"
source: "RIKEN"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Product Launch" (correct - new material)
- **Tags:** 
  - REMOVE: 'product-launch', 'innovation', 'product' (generic)
  - KEEP/CHANGE: ['RIKEN'] (simplify from full center name)
- **Company Field:** 
  - CHANGE FROM: `"RIKEN Center for Emergent Matter Science (CEMS)"` 
  - CHANGE TO: `["RIKEN"]` (array, use main org name)
- **Company Type:** ✓ KEEP "University"

---

### 2025-12-31 | Loliware partners with Entec

**File:** `2025-12-31-loliware-partners-with-entec.md`

**Current Front Matter:**
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

**Refactoring Plan:**
- **Category:** ✓ KEEP "Partnerships" (correct)
- **Tags:** 
  - REMOVE: 'partnerships', 'collaboration', 'partnership' (generic, duplicative)
  - KEEP: ['Loliware', 'Entec'] (both partner companies)
- **Company Field:** 
  - CHANGE FROM: `"Loliware"` 
  - CHANGE TO: `["Loliware", "Entec"]` (array - both partners)
- **Add:** company_type field if needed

---

### 2025-12-31 | Notpla produced 15M single-use plastic alternatives

**File:** `2025-12-31-notpla-produced-15m-single-use-plastic-alternatives.md`

**Current Front Matter:**
```yaml
title: "Notpla produced 15M single-use plastic alternatives"
date: 2025-12-31
draft: false
summary: "Notpla produced 15 million single-use plastic alternatives in 2025, advancing seaweed biopolymer applications."
tags: ['Notpla', 'financial-results', 'earnings', 'financial']
category: "Financial Results"
company: "Notpla"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Financial Results" (correct - production/sales metric)
- **Tags:** 
  - REMOVE: 'financial-results', 'earnings', 'financial' (generic)
  - KEEP: ['Notpla']
- **Company Field:** 
  - CHANGE FROM: `"Notpla"` 
  - CHANGE TO: `["Notpla"]` (array)
- **Add:** company_type field if needed

---

### 2025-12-31 | Sway partners with Atlantic Packaging

**File:** `2025-12-31-sway-partners-with-atlantic-packaging.md`

**Current Front Matter:**
```yaml
title: "Sway partners with Atlantic Packaging"
date: 2025-12-31
draft: false
summary: "Sway partnered with Atlantic Packaging for biopolymer packaging initiatives."
tags: ['Sway', 'partnerships', 'collaboration', 'partnership']
category: "Partnerships"
company: "Sway"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Partnerships" (correct)
- **Tags:** 
  - REMOVE: 'partnerships', 'collaboration', 'partnership' (generic)
  - KEEP: ['Sway', 'Atlantic Packaging'] (both partners)
- **Company Field:** 
  - CHANGE FROM: `"Sway"` 
  - CHANGE TO: `["Sway", "Atlantic Packaging"]` (array - both partners)
- **Add:** company_type field

---

### 2025-12-31 | Uluu raises $10.5 million in funding

**File:** `2025-12-31-uluu-raises-105-million-in-funding.md`

**Current Front Matter:**
```yaml
title: "Uluu raises $10.5 million in funding"
date: 2025-12-31
draft: false
summary: "Uluu raised $10.5 million to expand seaweed biopolymer production and development."
tags: ['Uluu', 'investment-&-funding', 'investment', 'funding']
category: "Investment & Funding"
company: "Uluu"
company_type: "Bioplastic Producer"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Investment & Funding" (correct)
- **Tags:** 
  - REMOVE: 'investment-&-funding', 'investment', 'funding' (generic)
  - KEEP: ['Uluu']
- **Company Field:** 
  - CHANGE FROM: `"Uluu"` 
  - CHANGE TO: `["Uluu"]` (array)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2025-12-31 | Zerocircle raises $2.3 million

**File:** `2025-12-31-zerocircle-raises-23-million.md`

**Current Front Matter:**
```yaml
title: "Zerocircle raises $2.3 million"
date: 2025-12-31
draft: false
summary: "Zerocircle raised $2.3 million for biopolymer technology advancements."
tags: ['Zerocircle', 'investment-&-funding', 'investment', 'funding']
category: "Investment & Funding"
company: "Zerocircle"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Investment & Funding" (correct)
- **Tags:** 
  - REMOVE: 'investment-&-funding', 'investment', 'funding' (generic)
  - KEEP: ['Zerocircle']
- **Company Field:** 
  - CHANGE FROM: `"Zerocircle"` 
  - CHANGE TO: `["Zerocircle"]` (array)
- **Add:** company_type field

---

## 2026-01 REMAINING ARTICLES (16 files needing refactoring)

### 2026-01-05 | AI Tool Released to Predict Bioplastic Biodegradability

**File:** `2026-01-05-ai-tool-released-to-predict-bioplastic-biodegradability.md`

**Current Front Matter:**
```yaml
title: "AI Tool Released to Predict Bioplastic Biodegradability"
date: 2026-01-05
draft: false
summary: "The ANIPH Project has launched a pioneering AI-driven predictive tool..."
tags: ['ANIPH Project', 'innovation', 'sustainability']
category: "News"
company: "ANIPH Project"
company_type: "Bioplastic Producer"
source: "Aniph.eu"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Product Launch" (new AI tool)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['ANIPH Project']
- **Company Field:** 
  - CHANGE FROM: `"ANIPH Project"` 
  - CHANGE TO: `["ANIPH Project"]` (array)
- **Company Type:** RECONSIDER - This is a project/initiative, not a producer. May need adjustment based on content

---

### 2026-01-05 | Ingevity Sells CTO Refinery for $110M

**File:** `2026-01-05-ingevity-sells-cto-refinery-for--110m-in-high-value-strategi.md`

**Current Front Matter:**
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

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "M&A" (asset sale/divestment)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['Ingevity']
- **Company Field:** 
  - CHANGE FROM: `"Ingevity"` 
  - CHANGE TO: `["Ingevity"]` (array)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2026-01-06 | AIMPLAS Launches 2026 Training Program

**File:** `2026-01-06-aimplas-launches-2026-training-program-with-bioplastics-focus.md`

**Current Front Matter:**
```yaml
title: "AIMPLAS Launches 2026 Training Program with Bioplastics Focus"
date: 2026-01-06
draft: false
summary: "AIMPLAS launches extensive 2026 training program..."
tags: ['AIMPLAS', 'product-launch', 'innovation', 'product']
category: "Product Launch"
company: "AIMPLAS"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "Product Launch" (not quite right)
  - CHANGE TO: "Market Analysis" (could also be "News" - training program announcement is more informational than a product launch)
- **Tags:** 
  - REMOVE: 'product-launch', 'innovation', 'product' (generic)
  - KEEP: ['AIMPLAS']
- **Company Field:** 
  - CHANGE FROM: `"AIMPLAS"` 
  - CHANGE TO: `["AIMPLAS"]` (array)
- **Add:** company_type field

---

### 2026-01-06 | BASF debuts world's first biomass-balanced polyethersulfone

**File:** `2026-01-06-basf-debuts-worlds-first-biomass-balanced-polyethersulfone.md`

**Current Front Matter:**
```yaml
title: "BASF debuts world's first biomass-balanced polyethersulfone"
date: 2025-03-04  # NOTE: Wrong date!
draft: false
summary: "BASF debuted the world's first biomass-balanced polyethersulfone biopolymer."
tags: ['BASF', 'product-launch', 'innovation', 'product']
category: "Product Launch"
company: "BASF"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **DATE ERROR:** Fix date from "2025-03-04" to "2026-01-06"
- **Category:** ✓ KEEP "Product Launch" (correct - new product)
- **Tags:** 
  - REMOVE: 'product-launch', 'innovation', 'product' (generic)
  - KEEP: ['BASF']
- **Company Field:** 
  - CHANGE FROM: `"BASF"` 
  - CHANGE TO: `["BASF"]` (array)
- **Add:** company_type field

---

### 2026-01-06 | CovationBio unveils bio-based PTMEG alternative

**File:** `2026-01-06-covationbio-unveils-bio-based-ptmeg-alternative.md`

**Current Front Matter:**
```yaml
title: "CovationBio unveils bio-based PTMEG alternative"
date: 2025-04-14  # NOTE: Wrong date!
draft: false
summary: "CovationBio unveiled bio-based alternative to PTMEG at Chinaplas 2025."
tags: ['CovationBio', 'product-launch', 'innovation', 'product']
category: "Product Launch"
company: "CovationBio"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **DATE ERROR:** Fix date from "2025-04-14" to "2026-01-06"
- **Category:** ✓ KEEP "Product Launch" (correct - new product)
- **Tags:** 
  - REMOVE: 'product-launch', 'innovation', 'product' (generic)
  - KEEP: ['CovationBio']
- **Company Field:** 
  - CHANGE FROM: `"CovationBio"` 
  - CHANGE TO: `["CovationBio"]` (array)
- **Add:** company_type field

---

### 2026-01-06 | FKuR Launches Bioplastic Development in Texas

**File:** `2026-01-06-fkur-launches-bioplastic-development-in-texas.md`

**Current Front Matter:**
```yaml
title: "FKuR Launches Bioplastic Development in Texas"
date: 2010-01-06  # NOTE: Wrong date!
draft: false
summary: "German bioplastic company FKuR is gearing up operations in Texas to develop and sell innovative biocompound products."
tags: ['FKuR', 'plant-announcement', 'manufacturing', 'capacity']
category: "Plant Announcement"
company: "FKuR"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **DATE ERROR:** Fix date from "2010-01-06" to "2026-01-06"
- **Category:** ✓ KEEP "Plant Announcement" (correct)
- **Tags:** 
  - REMOVE: 'plant-announcement', 'manufacturing', 'capacity' (generic, matches category)
  - KEEP: ['FKuR']
- **Company Field:** 
  - CHANGE FROM: `"FKuR"` 
  - CHANGE TO: `["FKuR"]` (array)
- **Add:** company_type field

---

### 2026-01-06 | TotalEnergies Corbion and Benvic expand low-carbon compounds

**File:** `2026-01-06-totalenergies-corbion-and-benvic-expand-low-carbon-compounds.md`

**Current Front Matter:**
```yaml
title: "TotalEnergies Corbion and Benvic expand low-carbon compounds"
date: 2026-03-27  # NOTE: Wrong date!
draft: false
summary: "TotalEnergies Corbion and Benvic teamed up to expand low-carbon biopolymer compounds for automotive and electronics."
tags: ['TotalEnergies Corbion', 'partnerships', 'collaboration', 'partnership']
category: "Partnerships"
company: "TotalEnergies Corbion"
company_type: "Bioplastic Producer"
source: "Perplexity Rev2"
```

**Refactoring Plan:**
- **DATE ERROR:** Fix date from "2026-03-27" to "2026-01-06"
- **Category:** ✓ KEEP "Partnerships" (correct)
- **Tags:** 
  - REMOVE: 'partnerships', 'collaboration', 'partnership' (generic)
  - KEEP: ['TotalEnergies Corbion', 'Benvic'] (both partner companies)
- **Company Field:** 
  - CHANGE FROM: `"TotalEnergies Corbion"` 
  - CHANGE TO: `["TotalEnergies Corbion", "Benvic"]` (array - both partners)
- **Company Type:** Keep for TotalEnergies Corbion

---

### 2026-01-07 | Aduro Secures $20M for Bioplastic Demonstration Plant

**File:** `2026-01-07-aduro-secures--20m-for-bioplastic-demonstration-plant-constr.md`

**Current Front Matter:**
```yaml
title: "Aduro Secures $20M for Bioplastic Demonstration Plant Construction"
date: 2026-01-07
draft: false
summary: "Aduro Clean Technologies has raised $20 million in funding to accelerate the construction of a demonstration plant..."
tags: ['Aduro Clean Technologies', 'innovation', 'sustainability']
category: "News"
company: "Aduro Clean Technologies"
company_type: "Bioplastic Producer"
source: "SEC Filings / News"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Investment & Funding" (funding announcement)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['Aduro Clean Technologies']
- **Company Field:** 
  - CHANGE FROM: `"Aduro Clean Technologies"` 
  - CHANGE TO: `["Aduro Clean Technologies"]` (array)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2026-01-07 | BASF Commissions Renewable Energy Steam Cracker

**File:** `2026-01-07-basf-commissions-renewable-energy-steam-cracker-in-zhanjiang.md`

**Current Front Matter:**
```yaml
title: "BASF Commissions Renewable Energy Steam Cracker in Zhanjiang"
date: 2026-01-07
draft: false
summary: "BASF has officially commissioned its landmark steam cracker at the Zhanjiang Verbund site..."
tags: ['BASF', 'innovation', 'sustainability']
category: "News"
company: "BASF"
company_type: "Bioplastic Producer"
source: "BASF News"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Plant Announcement" (facility commissioning)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['BASF']
- **Company Field:** 
  - CHANGE FROM: `"BASF"` 
  - CHANGE TO: `["BASF"]` (array)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2026-01-08 | MTU Launches Pilot Green Biorefinery

**File:** `2026-01-08-mtu-launches-pilot-green-biorefinery-at-kerry-campus.md`

**Current Front Matter:**
```yaml
title: "MTU Launches Pilot Green Biorefinery at Kerry Campus"
date: 2026-01-08
draft: false
summary: "Munster Technological University has officially opened a state-of-the-art pilot green biorefinery..."
tags: ['Munster Technological University (MTU)', 'innovation', 'sustainability']
category: "News"
company: "Munster Technological University (MTU)"
company_type: "Bioplastic Producer"
source: "MTU"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Plant Announcement" (facility opening)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['MTU'] or keep full name? (simplify)
- **Company Field:** 
  - CHANGE FROM: `"Munster Technological University (MTU)"` 
  - CHANGE TO: `["Munster Technological University"]` or `["MTU"]` (array, decide on abbreviation)
- **Company Type:** May need adjustment - University, not Bioplastic Producer

---

### 2026-01-08 | Natur-Tec Bioplastics Segment Drives Record Q1 Sales

**File:** `2026-01-08-natur-tec-bioplastics-segment-drives-record-q1-sales.md`

**Current Front Matter:**
```yaml
title: "Natur-Tec Bioplastics Segment Drives Record Q1 Sales"
date: 2026-01-08
draft: false
summary: "Northern Technologies International Corp (NTIC) reported record-breaking first-quarter fiscal 2026 sales..."
tags: ['Northern Technologies International Corp (NTIC)', 'innovation', 'sustainability']
category: "News"
company: "Northern Technologies International Corp (NTIC)"
company_type: "Bioplastic Producer"
source: "Seeking Alpha"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Financial Results" (quarterly sales/earnings announcement)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['Northern Technologies International Corp'] or ['NTIC']? (decide on format)
- **Company Field:** 
  - CHANGE FROM: `"Northern Technologies International Corp (NTIC)"` 
  - CHANGE TO: `["Northern Technologies International Corp"]` (array)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2026-01-08 | SABIC Divests European Plastics Units

**File:** `2026-01-08-sabic-divests-european-plastics-units-to-focus-on-sustainabl.md`

**Current Front Matter:**
```yaml
title: "SABIC Divests European Plastics Units to Focus on Sustainable Portfolio"
date: 2026-01-08
draft: false
summary: "SABIC has announced a strategic divestment of its traditional European plastics units..."
tags: ['SABIC', 'innovation', 'sustainability']
category: "News"
company: "SABIC"
company_type: "Bioplastic Producer"
source: "Eco Plastics in Packaging"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "M&A" (divestment/strategic sale)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['SABIC']
- **Company Field:** 
  - CHANGE FROM: `"SABIC"` 
  - CHANGE TO: `["SABIC"]` (array)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2026-01-09 | Orinko Advanced Plastics Acquires 70% Stake

**File:** `2026-01-09-orinko-advanced-plastics-acquires-70--stake-in-omikron.md`

**Current Front Matter:**
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

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "M&A" (acquisition/stake purchase)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['Orinko Advanced Plastics', 'Omikron'] (both companies involved)
- **Company Field:** 
  - CHANGE FROM: `"Orinko Advanced Plastics"` 
  - CHANGE TO: `["Orinko Advanced Plastics", "Omikron"]` (array - both involved in transaction)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2026-01-12 | AIMPLAS Launches Biovalsa Project

**File:** `2026-01-12-aimplas-launches-biovalsa-project-for-agricultural-waste-bio.md`

**Current Front Matter:**
```yaml
title: "Aimplas Launches Biovalsa Project for Agricultural Waste Bioplastics"
date: 2026-01-12
draft: false
summary: "Aimplas has initiated the Biovalsa project to develop high-performance bioplastics for the packaging industry..."
tags: ['Aimplas', 'innovation', 'sustainability']
category: "News"
company: "Aimplas"
company_type: "Bioplastic Producer"
source: "Packaging Insights"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Product Launch" (new project/product development)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['Aimplas']
- **Company Field:** 
  - CHANGE FROM: `"Aimplas"` 
  - CHANGE TO: `["Aimplas"]` (array)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2026-01-14 | Japanese Researchers Develop Marine-Degradable Cellulose Plastic

**File:** `2026-01-14-japanese-researchers-develop-marine-degradable-cellulose-pla.md`

**Current Front Matter:**
```yaml
title: "Japanese Researchers Develop Marine-Degradable Cellulose Plastic"
date: 2026-01-14
draft: false
summary: "A research team at Japan's RIKEN Center for Emergent Matter Science has successfully developed a high-performance cellulose-based plastic..."
tags: ['RIKEN Center for Emergent Matter Science', 'innovation', 'sustainability']
category: "News"
company: "RIKEN Center for Emergent Matter Science"
company_type: "Bioplastic Producer"
source: "World Bio Market Insights"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Product Launch" (new material development)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['RIKEN'] (simplify from center name)
- **Company Field:** 
  - CHANGE FROM: `"RIKEN Center for Emergent Matter Science"` 
  - CHANGE TO: `["RIKEN"]` (array, use main org)
- **Company Type:** CHANGE from "Bioplastic Producer" to "University"

---

### 2026-01-15 | L'Oréal Backs Bioplastics Startups

**File:** `2026-01-15-l-or-al-backs-bioplastics-startups-via-l-accelerator-program.md`

**Current Front Matter:**
```yaml
title: "L'Oréal Backs Bioplastics Startups via L'AcceleratOR Program"
date: 2026-01-15
draft: false
summary: "L'Oréal has selected 13 innovative startups for its L'AcceleratOR program to advance circularity, climate resilience, and sustainable bioplastic packaging solutions."
tags:
  - L'Oréal
  - innovation
  - sustainability
category: "News"
company: "L'Oréal"
company_type: "Bioplastic Producer"
source: "ESG Today"
```

**Refactoring Plan:**
- **Category:** 
  - CHANGE FROM: "News" (too generic)
  - CHANGE TO: "Investment & Funding" (startup acceleration/investment program)
- **Tags:** 
  - REMOVE: 'innovation', 'sustainability' (generic)
  - KEEP: ['L'Oréal']
- **Company Field:** 
  - CHANGE FROM: `"L'Oréal"` 
  - CHANGE TO: `["L'Oréal"]` (array)
- **Company Type:** CHANGE from "Bioplastic Producer" to "Consumer Products" or appropriate category

---

## 2025-11 ARTICLES (2 files - minor changes)

### 2025-11-05 | CJ Biomaterials partners with BIQ Materials

**File:** `2025-11-05-cj-biomaterials-partners-with-biq-materials-for-phact-pha-turf-infill.md`

**Current Front Matter:**
```yaml
title: "CJ Biomaterials partners with BIQ Materials for PHACT™ PHA turf infill"
date: 2025-11-05
draft: false
summary: "CJ Biomaterials signed a partnership with BIQ Materials to produce artificial turf infill made with PHACT™ PHA..."
tags: ['CJ Biomaterials', 'partnerships']
category: "Partnerships"
company: "CJ Biomaterials"
company_type: "Bioplastic Producer"
source: "Gemini search"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Partnerships"
- **Tags:** 
  - REMOVE: 'partnerships' (generic, matches category)
  - KEEP: ['CJ Biomaterials', 'BIQ Materials'] (both partners)
- **Company Field:** 
  - CHANGE FROM: `"CJ Biomaterials"` 
  - CHANGE TO: `["CJ Biomaterials", "BIQ Materials"]` (array - both partners)
- **Company Type:** ✓ KEEP "Bioplastic Producer"

---

### 2025-11-05 | Fibre Screw Caps on Track to Be Cost-Competitive

**File:** `2025-11-05-fibre-screw-caps-on-track-to-be-cost-competitive-with-fossil-plastics.md`

**Current Front Matter:**
```yaml
title: "Fibre Screw Caps on Track to Be Cost-Competitive with Fossil Plastics"
date: 2025-11-05
draft: false
summary: "Blue Ocean Closures (BOC) has announced a significant breakthrough"
tags: ['Blue Ocean Closures', 'product-launch', 'innovation', 'product']
category: "Product Launch"
company: "Blue Ocean Closures"
company_type: "Technology Company"
source: "bioplastics MAGAZINE"
```

**Refactoring Plan:**
- **Category:** ✓ KEEP "Product Launch"
- **Tags:** 
  - REMOVE: 'product-launch', 'innovation', 'product' (generic)
  - KEEP: ['Blue Ocean Closures']
- **Company Field:** 
  - CHANGE FROM: `"Blue Ocean Closures"` 
  - CHANGE TO: `["Blue Ocean Closures"]` (array)
- **Company Type:** ✓ KEEP "Technology Company"

---

## SUMMARY TABLE: FILES TO REFACTOR

| Date Range | Count | Status |
|-----------|-------|--------|
| 2025-11 | 2 | Minor changes needed |
| 2025-12 | 16 | Major refactoring needed |
| 2026-01 (remaining) | 16 | Major refactoring needed |
| **TOTAL** | **34** | **Awaiting refactoring** |

### Category Change Summary (2025-12)
- "News" → Appropriate category (Plant Announcement, Product Launch, etc.) - 4 files
- "Plant Announcements" (plural) → "Plant Announcement" (singular) - 2 files
- ✓ No changes needed - 10 files

### Category Change Summary (2026-01 remaining)
- "News" → Appropriate category (Plant Announcement, Product Launch, Investment & Funding, M&A, Financial Results) - 11 files
- ✓ No changes needed - 5 files

### Date Corrections Needed (2026-01)
- 2026-01-06-basf-debuts... (Date: 2025-03-04 → 2026-01-06)
- 2026-01-06-covationbio... (Date: 2025-04-14 → 2026-01-06)
- 2026-01-06-fkur... (Date: 2010-01-06 → 2026-01-06)
- 2026-01-06-totalenergies-corbion... (Date: 2026-03-27 → 2026-01-06)

### Company Field Format Summary
- All company fields need conversion from string to array format
- Partnership articles need both partner companies in the array
- Keep company names clean (remove parenthetical descriptions when moving to array format)

---

## NEXT STEPS

1. **Process 2025-12 articles** (16 files) - highest priority
2. **Process 2026-01 remaining articles** (16 files) - fix dates and refactor
3. **Process 2025-11 articles** (2 files) - quick fixes
4. **Verify all changes** against the standardized category list and tag format
5. **Delete duplicate capitalized versions** of files (e.g., keep lowercase, remove UPPERCASE versions)

