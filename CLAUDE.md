# CLAUDE.md — Bioplastics Portal

> **Agent:** Hermes (Nous Research)  
> **Last updated:** 2026-06-27  
> **Purpose:** Project conventions, structure, and verification for bioplasticsportal.com

## Project Overview

Hugo static site for bioplastics industry news, company profiles, and educational content. Deployed to Netlify.

- **Tech:** Hugo v0.123+ / Ananke theme
- **Repo:** `/home/pi/bioplastic-website` (GitHub: svenno76/bioplastic-website)
- **Live:** https://bioplasticsportal.com
- **Deploy:** Auto on git push → Netlify

## Verification

Canonical test command:

```bash
cd /home/pi/bioplastic-website && make verify
```

This runs 3 targets:
1. `verify-build` — Hugo build + output existence
2. `verify-news-filter` — News filter JS functions present
3. `verify-no-stale` — Confirms no old dropdown/legacy filter code

**Do NOT check for:** `dropdown selects`, `filterPosts()`, `filterNews()`, `unified filter bar` — these were intentionally removed (Sven prefers compact button groups).

## Common Commands

| Task | Command |
|------|---------|
| Dev server | `hugo server` |
| Production build | `hugo --gc --minify` |
| Full verification | `make verify` |
| Git deploy | `git add -A && git commit -m "..." && git push` |

## Codebase Structure

```
content/          — Markdown content (news, companies, blog, glossary)
  news/           — YYYY-MM-DD-slug.md
  companies/      — slug.md
  blog/           — YYYY-MM-DD-slug.md
  glossary/       — slug.md
layouts/          — Hugo templates (.html)
  partials/       — Reusable partials (header, footer, auto-link)
  news/           — News list + single templates
  companies/      — Company single template
static/           — Assets (CSS, images)
  css/            — custom.css, homepage.css
  images/         — logos/, blog/, news/
themes/ananke/    — Base theme (git submodule)
public/           — Generated output (git-ignored)
```

## Front Matter Reference

**News article** (`content/news/YYYY-MM-DD-slug.md`):
```yaml
---
title: "Article Title"
date: 2026-06-27
draft: false
summary: "Brief summary"
tags: ["Company", "tag1"]
category: "Product Launch"
company: ["Company Name"]    # Always array, even for single company
source: "Source Name"
featured_image: "/images/news/slug-1024.jpg"
sitemap:
  priority: 0.7
---
```

**Company profile** (`content/companies/slug.md`):
```yaml
---
title: "Company Name"
headquarters: "City, Country"
founded: "1997"
website: "https://example.com"
primary_materials: "PBAT, ecoflex"
market_segments: "Packaging, agriculture"
overview: "Brief description"
sitemap:
  priority: 0.8
---
```

**Blog post** (`content/blog/YYYY-MM-DD-slug.md`):
```yaml
---
title: "Article Title"
date: 2026-06-27
draft: false
categories: ["Guide", "Materials"]
tags: ["PLA", "Bio-based"]
summary: "Brief description"
featured_image: "/images/blog/slug-hero.jpg"
image_type: "photo"
---
```

## Critical Conventions

### File Editing
- **NEVER** use `write_file` or `execute_code` for HTML/templates — they mangle `=` signs
- **ALWAYS** use terminal heredoc for files containing `=` (Hugo templates, HTML, CSS)
- Use `patch` for targeted edits in markdown/content files

### Company Field Handling
News articles use TWO formats for `company`: string (`"BASF"`) and array (`["BASF"]`). **Always use `reflect.IsSlice` before iterating.**

### Auto-Linking
- Partial: `layouts/partials/auto-link-content.html`
- Applied to: news content, company primary_materials, market_segments, content
- Regex uses `\b` word boundaries (single backslash in file)
- Strip existing `<a>` tags BEFORE applying auto-link (prevents nested links)
- **Do NOT use inline `<picture>`/`<img>` in Markdown** — use `featured_image` frontmatter

### Image Sourcing
- **Unsplash** works reliably for blog/news hero images
- **Wikimedia Commons** page URLs often return HTML stubs — use `upload.wikimedia.org` direct links
- Always verify with `file` command after download
- OpenAI image generation hits billing limits — use Unsplash as fallback

### Hugo Gotchas (v0.123)
1. `.Kind` for taxonomy term pages is `"term"`, not `"taxonomy"`
2. `[sitemap.priority]` map NOT supported — use per-page frontmatter
3. `replaceRE` can't handle arrays — `delimit` first
4. `delimit` on a string outputs ASCII codes — always `reflect.IsSlice` first
5. `.bak` files in `layouts/` break Hugo builds — store backups in `/tmp/`
6. Goldmark `unsafe = true` needed for inline HTML in Markdown

## User Preferences

- **Language:** German preferred, English for code/technical
- **Communication:** Direct, no nicknames, structured progress tracking
- **Quality:** Perfectionist — clean code, thorough verification, no shortcuts
- **Images:** Keep original text 1:1 when illustrating — only add images, never rewrite
- **Filtering:** Compact button groups, NOT dropdowns
- **Feedback style:** Wants options with tradeoffs (A/B/C), not single prescriptive answers

## Active Tasks

See `CLASSIFICATION_REVIEW_TODO.md` for company classification audit status.

## References

- `references/news-filtering.md` — Client-side filter implementation
- `references/manual-article-publish.md` — Full article publishing workflow
- `references/newsletter-workflow.md` — Newsletter template, quality checks, cron
- `references/auto-link-regex-debugging.md` — Regex escaping pitfalls
- `references/image-optimization.md` — Sizing, lazy loading, logo detection
- `references/supabase-schema.md` — DB schema, column types, constraints
- `references/batch-script-output-format.md` — How to interpret batch log stats
