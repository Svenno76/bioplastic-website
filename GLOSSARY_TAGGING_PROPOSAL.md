# Glossary-Based Tagging System Proposal

## Executive Summary

Replace free-form tags on all 303 news articles with a **controlled vocabulary drawn exclusively from glossary terms**. This creates discipline, enables the "last 6 news per glossary term" feature, and establishes bidirectional linking (news↔glossary, companies↔glossary).

---

## Current State Analysis

| Metric | Value |
|--------|-------|
| Glossary terms | 30 |
| News articles | 303 |
| Unique free-form tags | 824 |
| Tag occurrences | 1,216 |
| Tags matching glossary | 18 (2.2%) |
| Articles with ≥1 glossary tag | ~80 |

**Problem**: 97.8% of tags are uncontrolled (company names, generic categories, one-off terms).

---

## Proposed Controlled Vocabulary (50 Terms)

### Core Materials (12) — *Already in glossary*
| Glossary Term | Display Name | News Count (est.) |
|---------------|--------------|-------------------|
| pla | PLA | 21 |
| pha | PHA | 20 |
| pbat | PBAT | 4 |
| pbs | PBS | 3 |
| phb | PHB | 4 |
| bio-pe | Bio-PE | 6 |
| bio-pp | Bio-PP | 2 |
| bio-pet | Bio-PET | 1 |
| bio-pp | Bio-PP | 2 |
| starch-based-bioplastic | Starch-based Bioplastic | 2 |
| cellulose | Cellulose* | 13 |
| fdca | FDCA | 1 |

### Technologies & Processes (10) — *Mostly in glossary, add 4*
| Glossary Term | Display Name | Status | News Count |
|---------------|--------------|--------|------------|
| chemical-recycling | Chemical Recycling | **NEW** | 14 |
| thermochemical-liquefaction | Thermochemical Liquefaction | ✅ | 1 (new) |
| pyrolysis | Pyrolysis* | **NEW** | 3 |
| hydrothermal-liquefaction | Hydrothermal Liquefaction* | **NEW** | 0 |
| depolymerization | Depolymerization* | **NEW** | 2 |
| enzymatic-recycling | Enzymatic Recycling* | **NEW** | 2 |
| fermentation | Fermentation* | **NEW** | 7 |
| mass-balance-approach | Mass Balance | ✅ | 4 |
| life-cycle-assessment | Life Cycle Assessment | ✅ | 0 |
| biorefinery | Biorefinery* | **NEW** | 1 |

### Materials Properties & Standards (7) — *Already in glossary*
| Glossary Term | Display Name | News Count |
|---------------|--------------|------------|
| biodegradable | Biodegradable | 3 |
| compostable | Compostable | 5 |
| composting-infrastructure | Composting Infrastructure | 0 |
| en-13432 | EN 13432 | 0 |
| drop-in-bioplastic | Drop-in Bioplastic | 0 |
| drop-in-replacement | Drop-in Replacement | 0 |
| bio-based-aniline | Bio-based Aniline | 1 |

### Circular Economy & Policy (7) — *Mostly in glossary, add 2*
| Glossary Term | Display Name | Status | News Count |
|---------------|--------------|--------|------------|
| circular-economy | Circular Economy | ✅ | 15 |
| recycled-content | Recycled Content* | **NEW** | 5 (rPET + recycled) |
| ppwr-packaging-waste-regulation | PPWR | ✅ | 2 |
| iscc-plus | ISCC PLUS* | **NEW** | 2 |
| extended-producer-responsibility | EPR* | **NEW** | 1 |
| carbon-footprint | Carbon Footprint* | **NEW** | 3 (CO₂/decarbonisation) |
| biobased-content | Bio-based Content* | **NEW** | 4 |

### Applications & Markets (8) — *All NEW*
| Glossary Term | Display Name | Status | News Count |
|---------------|--------------|--------|------------|
| packaging | Packaging | **NEW** | 20+ |
| automotive | Automotive | **NEW** | 4+ |
| textiles | Textiles | **NEW** | 5+ |
| agriculture-films | Agricultural Films | **NEW** | 4 |
| food-contact | Food Contact | **NEW** | 4+ |
| medical-healthcare | Medical/Healthcare | **NEW** | 3 |
| construction | Construction | **NEW** | 2 |
| consumer-goods | Consumer Goods | **NEW** | 6+ |

### Feedstocks (6) — *Some in glossary, add 3*
| Glossary Term | Display Name | Status | News Count |
|---------------|--------------|--------|------------|
| feedstock | Feedstock | ✅ | 2 |
| sugarcane | Sugarcane* | **NEW** | 2 |
| corn | Corn* | **NEW** | 1 |
| lignocellulosic-biomass | Lignocellulosic Biomass* | **NEW** | 2 |
| used-cooking-oil | Used Cooking Oil* | **NEW** | 1 |
| co2-feedstock | CO₂ Feedstock* | **NEW** | 2 |

---

## Implementation Plan

### Phase 1: Extend Glossary (Create 20 New Terms)
Create missing glossary entries for starred (*) terms above. Each follows existing template.

### Phase 2: Retag All 303 News Articles
- Map each article's current tags → controlled vocabulary
- Each article gets 3-8 glossary tags (no free-form)
- Update front matter: `tags: ["chemical-recycling", "pyrolysis", "circular-economy", ...]`

### Phase 3: Update Glossary Template
Add "Latest News" section showing 6 most recent articles tagged with that term.

### Phase 4: Update News Template
- Display tags as links to `/glossary/{term}/`
- Remove category/company filter buttons (or keep as secondary)

### Phase 5: Auto-link Company Descriptions
Enhance `auto-link-content.html` to link all glossary terms in company content.

---

## Tag Mapping Rules

| Current Tag Pattern | → Controlled Tag(s) |
|---------------------|---------------------|
| Company names (BASF, Braskem, etc.) | **REMOVE** — use `company` field instead |
| 'Innovation', 'Product Launch', 'Investment', 'Partnership', 'M&A' | **REMOVE** — use `category` field instead |
| 'Recycling', 'Advanced Recycling' | → `chemical-recycling` + `mechanical-recycling`* |
| 'Biopolymers', 'Bio-Based Plastics', 'Biopolymer' | → `bioplastics` |
| 'Sustainable Packaging', 'Packaging' | → `packaging` |
| 'China', 'Europe', 'Brazil', etc. | **REMOVE** — not topical |
| 'Fermentation', 'Biomanufacturing' | → `fermentation` |
| 'Carbon Capture', 'CCU', 'Decarbonisation' | → `carbon-footprint` + `co2-feedstock` |
| 'Microplastic', 'Marine Biodegradation' | → `biodegradable` + `compostable` |
| 'PEF', 'FDCA', 'YXY' | → `fdca` + `bio-pet` |

---

## Example: Nerea Article Retagging

**Before**: `["chemical-recycling", "technip-energies", "alterra", "neste", "nerea", "modular-solution", "circular-economy"]`

**After**: `["chemical-recycling", "thermochemical-liquefaction", "circular-economy", "mass-balance-approach", "pyrolysis", "packaging", "drop-in-replacement"]`

---

## Benefits

1. **Discipline**: 50 controlled terms vs 824 free-form
2. **Discovery**: "Latest News" on each glossary page (6 most recent)
3. **SEO**: Structured, consistent tagging
4. **Navigation**: Click tag → glossary → related news → other terms
5. **Company linking**: Auto-link glossary terms in company profiles
6. **Analytics**: Track coverage per topic over time

---

## Approval Request

**Please review and approve:**
1. The 50-term controlled vocabulary (20 new glossary entries needed)
2. Retagging strategy for all 303 articles
3. Template changes for glossary "Latest News" and news tag links

Once approved, I'll execute using the `get-shit-done` skill for systematic implementation.