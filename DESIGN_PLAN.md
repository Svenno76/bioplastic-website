# Bioplastic Website Design Improvement Plan

**Goal:** Make the website look more professional while staying within the Hugo framework

**Timeline:** Multi-week project, phased approach

---

## Current State Assessment

✅ **Good foundation:**
- Clean blue color scheme
- Basic responsive design
- Card components with hover effects
- Decent footer

⚠️ **Room for improvement:**
- News list is very text-heavy (simple list format)
- Limited visual hierarchy
- No real visual distinction between sections
- Card designs are basic
- Typography could be more sophisticated
- Limited use of whitespace & layout variety

---

## Design Improvement Ideas (Within Hugo)

### 1. **News/Content Cards** (High Impact 🎯)
Instead of a simple text list, display cards with:
- **Featured image** (full-width in card, with proper aspect ratio)
- **Category badge** (colorful tag)
- **Company tags** (linked pills)
- **Date + read time** (subtle metadata)
- **Excerpt with better typography** (larger, more readable)
- **Hover effect**: Slight lift + image zoom effect

*This alone would transform the look from "list" to "content hub"*

### 2. **Hero/Featured Section** (High Impact 🎯)
- Show the **latest/most important article** in a prominent "featured card"
- Large image, title, summary, CTA button
- Maybe a rotating featured article carousel (pure CSS or minimal JS)
- Currently your homepage just redirects to /news/ - we could make it special

### 3. **Improved Navigation**
- **Sticky nav** with backdrop blur (you have this partly)
- **Active state indicator** for current section
- **Search bar** (could be a simple Hugo filter or external)
- **Mobile hamburger** properly implemented

### 4. **Color & Typography Polish**
- Use the **Kimi design's softer palette**: They use `#F6F8F6` (soft cream) with `#111C1A` (dark green tint) instead of harsh blues
- More **sophisticated typography hierarchy**:
  - Large, bold headlines (display font)
  - Clean body text (system fonts are fine)
  - Accent colors for interactions
- Better contrast ratios

### 5. **Company Profiles & Linking**
- Create a **company profile card design** with:
  - Logo/image
  - Key stats (Founded, HQ, Employees)
  - Quick links to their products
  - Auto-linked mentions in news articles (you have this!)

### 6. **Section Dividers & Spacing**
- Use the **Kimi approach**: sections with different background colors/gradients
- Proper whitespace between sections
- Visual "breathing room"

### 7. **Glossary Redesign**
- Alphabet filter buttons (A-Z)
- Definition cards with better styling
- Search functionality

### 8. **Statistics/Insights Section**
- Display site stats: "X news articles, Y companies, Z glossary terms"
- Quick "by the numbers" boxes

---

## Implementation Strategy

### Phase 1: Quick Wins (Current)
**Focus:** Immediate visual improvements
- [ ] Improve news card design (featured images, badges, better spacing)
- [ ] Better typography & colors (color palette update, font hierarchy)
- [ ] Refine header/footer aesthetics (cleaner design, better spacing)

### Phase 2: Company Logos & Images
**Focus:** Visual enhancement with logo-based news images
- [x] Complete companies.xlsx with all companies from news tags (181 total companies)
- [x] Download company logos (56 downloaded, 77.8% success rate)
- [ ] Design news-type icons/badges (Product Launch, Investment, Partnership, etc.)
- [ ] Create image templates combining company logo + news type
- [ ] Generate featured images for all news articles
- [ ] Link generated images to news posts

**News Type Categories to Create Images For:**
- Product Launch
- Investment & Funding
- Plant Announcement
- Partnership
- Market Analysis
- Regulatory & Policy
- Industry Collaboration
- Technology Development
- Merger & Acquisition
- Other announcements

### Phase 3: Polish & Refinement
**Focus:** Additional refinement & animations
- [ ] Featured article section
- [ ] Animations (subtle, using CSS)
- [ ] Better responsive design
- [ ] SEO optimizations

---

## Design Decisions to Make

1. **Color palette** - Keep blue? Switch to softer green/cream? Something else?
2. **Tone** - Modern/playful? Or professional/corporate?
3. **Visual complexity** - Lots of imagery/graphics? Or clean & minimal?
4. **Content density** - Featured articles section? Or focus on the list?
5. **Priority** - What bothers you most about the current design?

---

## Notes & Progress

- Plan created: 2026-02-09
- Status: Planning → Phase 1 Implementation
