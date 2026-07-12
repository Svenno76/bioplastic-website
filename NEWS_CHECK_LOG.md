# News Check Log

Tracks when each company/feed was last checked for news. Used to prioritize and avoid duplicate coverage.

| Source / Company | Last Checked | Method | New Articles Found | Status | Notes |
|------------------|--------------|--------|-------------------|--------|-------|
| bioplasticsmagazine.com | 2026-07-10 | Automated (nightly) | 2 | ✅ Published | Avantium/ReLeaf, Evonik Purocel |
| Avantium | 2026-07-10 | Company site check | 1 | ✅ Published | ReLeaf/Gepack/Frubaça partnership |
| Evonik | 2026-07-10 | Company site check | 1 | ✅ Published | Purocel launch |
| Covestro | 2026-07-10 | Company site check | 1 | ✅ Published | Bio4PURConti |
| Technip Energies | 2026-07-10 | Company site check | 1 | ✅ Published | Nerea/Alterra/Neste |
| Sulzer | 2026-07-10 | Company site check | 0 | ✅ Checked | No new press releases |
| BASF | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| TotalEnergies Corbion | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| Corbion | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| NatureWorks | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| Braskem | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| Danimer Scientific | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| Novamont | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| Futerro | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| Praj Industries | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| CJ Biomaterials | 2026-07-09 | Company site check | 0 | ✅ Checked | No new press releases |
| Borealis | 2026-07-08 | Company site check | 0 | ✅ Checked | No new press releases |
| LyondellBasell | 2026-07-08 | Company site check | 0 | ✅ Checked | No new press releases |
| Dow | 2026-07-08 | Company site check | 0 | ✅ Checked | No new press releases |
| LanzaTech | 2026-07-08 | Company site check | 0 | ✅ Checked | No new press releases |
| UPM Biochemicals | 2026-07-08 | Company site check | 0 | ✅ Checked | No new press releases |
| Celanese | 2026-07-08 | Company site check | 0 | ✅ Checked | No new press releases |
| Arkema | 2026-07-08 | Company site check | 0 | ✅ Checked | No new press releases |

## Check Frequency Guidelines

| Priority | Companies | Frequency | Method |
|----------|-----------|-----------|--------|
| **Tier 1** (Major producers) | BASF, TotalEnergies, NatureWorks, Braskem, Dow, Covestro, Corbion, Novamont | Weekly | Company site + bioplasticsmagazine |
| **Tier 2** (Emerging/Tech) | Avantium, Praj, UPM, CJ, Danimer, Futerro, LanzaTech, Sulzer | Bi-weekly | Company site |
| **Tier 3** (Regional/Niche) | Others with profiles | Monthly | Company site + bioplasticsmagazine |
| **All** | Via bioplasticsmagazine.com | Daily (automated) | Nightly cron |

## Update Instructions

After each check run:
1. Update "Last Checked" date
2. Record "New Articles Found" count
3. Note any published articles in "Status"
4. Add any companies that need profile updates

