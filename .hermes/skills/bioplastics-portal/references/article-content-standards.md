# Article Content Standards

**Established:** 2026-07-15 | **Updated:** 2026-09-14

## Narrative Journalism Standard (Non-negotiable)

All blog posts and news articles MUST be written as narrative journalism:

- **Flowing prose with transitions** — "First... Second... Finally..."
- **Weave data into prose** — embed numbers, specs, quotes naturally
- **NO bullet points** in body text
- **NO markdown tables** in body text
- **NO lists** in body text
- **Sources as numbered list only** at article end

## Front Matter Requirements

```yaml
title: "Descriptive Title with Company Names"
date: YYYY-MM-DDTHH:MM:SS+02:00
draft: false
summary: "One-sentence executive summary for news list"
tags: ["PLA", "Chemical Recycling", "Investment"]  # bpp-tagging-taxonomy
category: "Plant Announcement" | "Technology" | "Partnerships" | "Investment & Funding" | "M&A" | "Regulatory & Policy" | "Certifications" | "Market Analysis" | "Technology"
company: ["Company A", "Company B"]  # ALWAYS array, never in tags
source: "Company Name"  # Primary source ONLY
source_url: "https://company.com/press-release-url"
featured_image: "https://images.unsplash.com/...?w=1024&q=80"
sitemap:
  priority: 0.7
```

## Hero Image Requirements

| Requirement | Specification |
|-------------|---------------|
| **Source** | Unsplash only |
| **Dimensions** | Landscape 16:9 (`?w=1024&q=80`) |
| **Content** | Visual metaphors only — industrial equipment, process flows, materials, plant exteriors |
| **Forbidden** | Text/titles in image, generic lab photos, people in suits, "green leaf" clichés |
| **Verification** | Must confirm live on published page: `curl -s URL | grep images.unsplash.com` |

**Critical:** If an Unsplash image returns 404, immediately replace with a working Unsplash URL — Netlify edge cache can serve stale 404s for weeks. Always verify the image URL returns HTTP 200 before committing.

## Company Field

- **ALWAYS array:** `["Company A", "Company B"]`
- **NEVER in tags** — company names auto-link from content
- **Must match Supabase** `companies` table entries (case-insensitive lookup)

## Tags (bpp-tagging-taxonomy)

- Exactly **1 material tag** (PLA, PHA, PBAT, PBS, PCL, Bio-PE, Bio-PET, Bio-PP, Bio-PA, Bio-PC, Bio-PU, Starch Blend, Cellulose, Lignin, etc.)
- Up to **5 optional tags** from controlled vocabulary
- **Max 6 tags total**
- No company names, no free-form tags

## Source Field

- **Primary source ONLY** — company press release, official product page
- **Never aggregators:** bioplasticsmagazine.com, packaginginsights.com, etc.
- Aggregator URL goes in article body as "Reported by..." if needed

## Article Structure

1. **Dateline + Lead** — Who, what, when, significance
2. **Context/Challenge** — Market data, regulatory drivers
3. **Solution/Technology** — Technical details, advantages
4. **Executive Quotes** — 2-3 quotes with names/titles
5. **Resources** — Links to PDFs, product pages, brochures
6. **Company Boilerplates** — 1-2 sentences each
7. **Source Attribution** — Handled automatically by template from frontmatter `source` and `source_url` — **DO NOT include source line in markdown body** (would render as `<h2>` and break styling)

## Duplicate Prevention

- **Slug match:** Check `content/news/` for existing slugs (filename basis)
- **Content match:** Grep for company + key topic/press release in existing articles
- **Supabase check:** Query `news` table for existing URLs with `workflow_status='new'` or `'published'`

## Auto-linking

- Company names in content auto-link to `/companies/slug/` — no manual links needed
- Glossary terms auto-link to `/glossary/term/` — use exact glossary term spelling
EOF