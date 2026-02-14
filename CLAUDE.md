# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Hugo static site generator project for a bioplastics information portal. It aggregates news, company profiles, studies, books, and a glossary related to the bioplastics industry. The site is deployed to Netlify.

**Tech Stack:**
- Hugo 0.138.0+ (static site generator)
- Ananke theme (base theme with custom overrides)
- Custom HTML/CSS layouts in `layouts/` directory
- Markdown content in `content/` directory

## Common Commands

### Build and Development
- **Local preview:** `hugo server` - Runs development server at `http://localhost:1313`
- **Production build:** `hugo --gc --minify` - Generates optimized static site in `public/` directory
- **Netlify deployment:** Automatically triggered on git push (configured in `netlify.toml`)

### Content Management
- **Add news article:** Create `.md` file in `content/news/` with front matter: `title`, `date`, `summary`, `tags`, `category`, `company`, `source`
- **Add company profile:** Create `.md` file in `content/companies/` with front matter: `title`, `headquarters`, `founded`, `website`, `products`, `revenue`, `employees`, `ceo`, `overview`
- **Check for draft status:** Posts with `draft: true` in front matter won't be published
- **Add new content section:** Create directory in `content/`, add `_index.md`, and corresponding layout in `layouts/[section]/`

## Codebase Structure

### Key Directories
- **`content/`** - Markdown files for all pages (news, companies, studies, books, glossary, bioplastics guide)
- **`layouts/`** - Hugo template files (`.html`) for rendering different content types
- **`static/`** - Static assets (CSS, images) served as-is
- **`themes/ananke/`** - Base theme (git submodule)
- **`public/`** - Generated static website (git-ignored, recreated on build)
- **`archetypes/`** - Content templates for scaffolding new posts
- **`data/`** - Static data files

### Layout Templates
Hugo template hierarchy automatically applied. Custom overrides in `layouts/`:
- `layouts/partials/site-header.html` - Navigation and header
- `layouts/partials/site-footer.html` - Footer
- `layouts/news/single.html` - Individual news article template (includes regex-based company name linking)
- `layouts/companies/single.html` - Individual company profile template
- `layouts/glossary/list.html` - Glossary list view
- `layouts/bioplastics/list.html` - Bioplastics guide list view
- `layouts/list.html` - Default list template

### Styling
- `static/css/custom.css` - Global custom styles
- `static/css/homepage.css` - Homepage-specific styles
- Inline styles used extensively in layout templates for rapid styling

## Important Patterns

### Front Matter Examples

**News article** (`content/news/YYYY-MM-DD-slug.md`):
```yaml
---
title: "Article Title"
date: 2024-10-25
draft: false
summary: "Brief summary for listing pages"
tags: ['Company', 'tag1', 'tag2']
category: "Product Launch"
company: "Company Name"
source: "Information source"
---
```

**Company profile** (`content/companies/slug.md`):
```yaml
---
title: "Company Name"
headquarters: "City, Country"
founded: "1997"
website: "https://example.com"
products: ["Product1", "Product2"]
revenue: "$500M"
employees: "500+"
ceo: "Name"
overview: "Brief company description"
---
```

### Company Name Linking
News articles automatically link company names mentioned in content. The regex pattern in `layouts/news/single.html` (line 24) handles this. Company names must exactly match the pattern defined in that regex.

### Content Organization
- News articles use date-based filenames (`YYYY-MM-DD-slug.md`)
- News index page lists all articles with tag filtering
- Company profiles are individual pages, referenced in news articles
- Homepage redirects to `/news/` section

## Site Configuration
- **Base URL:** `https://bioplastic.netlify.app`
- **Hugo config:** `hugo.toml` - Contains menu structure, custom CSS includes, and site metadata
- **Theme:** Ananke theme with extensive layout overrides
- **Deployment:** Netlify (configured in `netlify.toml`)

## Git Workflow Notes
- Theme (Ananke) is a git submodule
- News content files are frequently added/updated
- `public/` directory is generated and not committed
- Main branch is used for production deployments

## 📋 ACTIVE TASKS

### Company Classification Audit (In Progress)
**Status:** Phase 2 of 3 Complete
**Files:**
- `CLASSIFICATION_REVIEW_TODO.md` - **📌 START HERE** for pending work
- `COMPANY_CLASSIFICATION_AUDIT.md` - Detailed audit report

**Recent Progress:**
- ✅ Reclassified 18 companies to "Converter" (Batches 1-2, early fix)
- ✅ Reclassified 3 companies to "Compounder" (Batch 3)
- ✅ Verified 10 companies as correctly classified (Batch 4)
- ⏳ **2 companies pending manual review:** Blue Circle Olefins, Asahi Kasei

**Next Step:** Open `CLASSIFICATION_REVIEW_TODO.md` to see high-priority items
