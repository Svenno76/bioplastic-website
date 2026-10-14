# Company Profile Structure Standards

**Established:** 2026-10-14
**Scope:** All company profiles (`content/companies/*.md`) on bioplasticsportal.com
**Status:** PILOT — rolled out to Polymer Producer category first; other categories follow after review

## Canonical Structure

Every profile follows the same skeleton: a shared core, a category-specific middle, and a shared closing.

### Common core (all categories)

1. `## Overview` — 2–3 paragraphs. Who the company is, founding/HQ context, bioplastics relevance, significance. **Mandatory, always first.**
2. *(category-specific middle — see table below)*
3. `## Recent Developments` — significant events of the last 2–3 years (investments, expansions, partnerships, pivots). Snapshot only — breaking news goes into news articles, never back-filled here. Use H3 subsections (`### Financial Profile`, `### Commercial Milestones`, `### Future Outlook`) when needed.
4. `## Sources` — numbered list of sources at the end. **Mandatory, always last.**

### Category-specific middle sections

| Category | Sections (in order) |
|---|---|
| Polymer Producer | `## Products and Materials` → `## Production Facilities and Capacity` → `## Market Segments and Applications` → `## Sustainability and Certifications` |
| Compounder | `## Formulation Portfolio` → `## Production Facilities` → `## Target Applications` → `## Sustainability and Certifications` |
| Converter / Packaging | `## Product Lines` → `## Materials Used` → `## Brand Partners and Customers` → `## Sustainability and Certifications` |
| Additive Producer | `## Additive Portfolio` → `## Compatible Biopolymers` → `## Sustainability and Certifications` |
| Biotechnology | `## Technology Platform` → `## Products and Outputs` → `## Partnerships and Licensing` → `## Funding and Investors` |
| Recycling & Recovery | `## Recycling Technology` → `## Facilities and Capacity` → `## Feedstock and Output` → `## Environmental Impact` |
| Technology & Equipment | `## Equipment and Systems` → `## Bioplastics Applications` → `## Global Presence` |
| Academic / Research | `## Research Focus` → `## Notable Results and Spin-offs` → `## Partnerships with Industry` |
| Industry Body / Consulting | `## Services and Activities` → `## Relevance to Bioplastics` |

Omit a middle section if the company has no content for it (e.g. pre-commercial producers have no production facilities yet).

### H3 subsections

Page-specific content that doesn't merit its own H2 becomes an H3 under the nearest canonical section, keeping its original short title. Examples:

- `### Company Background`, `### Joint Venture Structure`, `### Leadership` → under **Overview**
- `### Feedstock Strategy`, `### Manufacturing` → under **Production Facilities**
- `### Industry Position`, `### Partnerships`, `### Geographic Presence`, `### Regional Significance` → under **Market Segments and Applications**
- `### Financial Profile`, `### Future Outlook`, `### Commercial Milestones` → under **Recent Developments**

## Rules

1. **Section count:** 5–8 H2 sections max. Anything beyond folds into H3s.
2. **No `## Conclusion`** — essay-ism. Cut it.
3. **No contact/address/email blocks** — the template info-box already shows the website link.
4. **Heading vocabulary is closed** — use the canonical names above. One-off headings (e.g. "Akron Showcase Facility") become H3s under the nearest canonical section.
5. **Footer lines become front matter:**
   - `*Last updated: February 13, 2026*` → `last_updated: 2026-02-13` in front matter
   - `*Information sourced from …*` → `## Sources` numbered list
6. **Front matter additions (mandatory):**
   - `last_updated: YYYY-MM-DD`
   - `profile_status: complete | stub` — `stub` = does not yet follow canonical structure (expansion backlog)

## Example skeleton (Polymer Producer)

```markdown
---
title: Company X
company_type: "Polymer Producer"
...
last_updated: 2026-10-14
profile_status: complete
---

## Overview
[2–3 paragraphs; optional `### Company Background`]

## Products and Materials
[resins, grades, brands, technology platform]

## Production Facilities and Capacity
[plants, capacity figures, feedstock strategy]

## Market Segments and Applications
[segments; optional `### Industry Position`, `### Partnerships`]

## Sustainability and Certifications
[certifications, LCA data, environmental profile]

## Recent Developments
[last 2–3 years; optional `### Financial Profile`, `### Future Outlook`]

## Sources
1. Company X corporate website — https://www.company-x.com
2. [additional sources]
```
