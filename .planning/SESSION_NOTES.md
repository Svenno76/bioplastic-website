# Session Notes - Design System Planning

**Date:** 2026-03-24
**Status:** Starting Fresh (Reset to GitHub main)

## What Was Attempted
Phases 3-5 design implementation using Tailwind CSS + Material Design 3 colors:
- Phase 3: News/Articles Pages
- Phase 4: News Article Details
- Phase 5: Company Profiles

**Issue:** Tailwind CSS classes not applying properly. Material Design colors defined in `tailwind.config.js` but grid layouts, colors, and Material Symbols icons not rendering correctly.

**Decision:** User requested complete reset to GitHub clean state and proper planning before proceeding.

## What User Wants to Do

**Goal:** Redesign bioplastics website with "Editorial Conservatory" aesthetic (premium, intentional design)

**Design System:**
- Material Design 3 color palette (primary: #134238, surfaces with tones)
- Typography: Manrope (headlines) + Inter (body)
- No 1px borders - use tonal color shifts instead
- Glassmorphism, asymmetric grids, proper spacing

**Current State:**
- ✅ Phase 1-2: Typography + Homepage done (header with glassmorphism)
- ❌ Phases 3-5: Reverted (styling issues with Tailwind)
- ⏳ Phases 6-8: Not started (Glossary, Footer, Global Refinements)

## Critical Issues Found
1. **Tailwind CSS not compiling properly** - custom colors not in output CSS
2. **Material Symbols icons** - showing as emoji instead of icon font
3. **Grid layouts** - Tailwind `grid` classes not working
4. **Design system mismatch** - Moved too fast without verifying technical foundation

## Next Session Plan

**Before implementing:**
1. ✅ Verify Tailwind CSS build pipeline works
   - Check `assets/css/tailwind.css` imports
   - Verify `tailwind.config.js` colors in compiled CSS
   - Test Material Symbols font loading

2. ✅ Document design system properly
   - Color palette with usage
   - Component specs (buttons, cards, etc.)
   - Layout patterns
   - Typography scale

3. ✅ Make tech decision:
   - Option A: Use Tailwind (fix build issues first)
   - Option B: Revert to inline styles (faster, guaranteed to work)
   - Option C: Hybrid approach (inline + minimal Tailwind)

4. ✅ Plan implementation strategy:
   - Phase-by-phase approach with incremental testing
   - Build verification after each phase
   - Visual QA before commit

## Files to Check Next Session
- `hugo.toml` - base configuration
- `assets/css/tailwind.css` - Tailwind imports/config
- `tailwind.config.js` - color definitions
- `static/css/custom.css` - legacy styles (may conflict)
- `layouts/` - template structure

## Key Decision Points
- **Should we use Tailwind or inline styles?** Need to verify Tailwind works first
- **How aggressively modernize the design?** Take it slower, test incrementally
- **Which pages first?** Prioritize based on traffic/importance

## Success Criteria
- Design matches "Editorial Conservatory" aesthetic
- All pages render correctly (desktop + mobile)
- No console errors
- Material Design 3 colors applied consistently
- Proper typography hierarchy throughout
