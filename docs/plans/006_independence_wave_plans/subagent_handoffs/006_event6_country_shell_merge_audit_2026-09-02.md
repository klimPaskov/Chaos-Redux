# Event 006 country-shell consolidation audit

Date: 2026-09-02.

Status: source changes made and ready for parent review; no staging or commit performed.

## Scope

The consolidation is limited to Event 006 country-definition shells, the Event 006 country-tag registry, the required complete vanilla-compatible country-colors replacement, and this handoff.

No country history, gameplay, localization, assets, flags, central admission, or unrelated files were edited.

## References consulted

The offline `paradox_wiki/Country creation - Hearts of Iron 4 Wiki.md` confirms that multiple tags may reference the same `common/countries/` file and that `common/countries/colors.txt` overrides a tag's country-definition color.

The required offline core pages were consulted in parallel: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

Installed vanilla country-definition precedents were inspected under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/countries/`, including representative culture/color files, and the installed `common/countries/colors.txt` was preserved as the replacement base.

The installed documentation directory contains no country-definition/colors schema, so the country-creation snapshot and vanilla source files supplied the relevant syntax.

## Changed source files

Added one shared shell for each exact culture pair:

- `common/countries/006_independence_wave_shared_african.txt` — `african_gfx` / `african_2d`.
- `common/countries/006_independence_wave_shared_asian.txt` — `asian_gfx` / `asian_2d`.
- `common/countries/006_independence_wave_shared_commonwealth.txt` — `commonwealth_gfx` / `commonwealth_2d`.
- `common/countries/006_independence_wave_shared_eastern_european.txt` — `eastern_european_gfx` / `eastern_european_2d`.
- `common/countries/006_independence_wave_shared_middle_eastern.txt` — `middle_eastern_gfx` / `middle_eastern_2d`.
- `common/countries/006_independence_wave_shared_southamerican.txt` — `southamerican_gfx` / `southamerican_2d`.
- `common/countries/006_independence_wave_shared_western_european.txt` — `western_european_gfx` / `western_european_2d`.

Updated `common/country_tags/006_independence_wave_countries.txt` so all 85 researched tags point to their shared shell while the 17 unresolved tags retain the inert reservation path and every identity comment remains unchanged.

Added `common/countries/colors.txt` as the exact installed vanilla file followed by 85 Event 006 `color = rgb` overrides. The overrides contain no `color_ui`, matching the prior shells' behavior.

Removed the 85 superseded per-tag shells, one for each researched tag: ACX, AFX, AGX, AJX, AKX, ARX, ASX, ATX, AXX, BAX, BBX, BFX, BHX, BJX, BKX, BWX, CIX, CJX, CKX, CLX, COX, CPX, CQX, CUX, CVX, CWX, CXX, CYX, DAX, DBX, DFX, DHX, DKX, DLX, DOX, DPX, DSX, DUX, DVX, DYX, DZX, EBX, EEX, EHX, ELX, EMX, EQX, ERX, ESX, EUX, EWX, FAX, FBX, FDX, FLX, FNX, FOX, FSX, FUX, FVX, FXX, GBX, GCX, GIX, GMX, GRX, GTX, GYX, GZX, HAX, HBX, HCX, HDX, HEX, HFX, HGX, HKX, HPX, HSX, HUX, HYX, HZX, IAX, IBX, and ICX.

The inert `common/countries/006_independence_wave_unresearched_reservations.txt` was retained unchanged.

## Parity evidence

An in-memory PowerShell audit compared the pre-change files from `git show HEAD` with the current source; no helper script was written.

The audit result was:

```
PASS tags=102 researched=85 pairs=7 shells_before=86 shells_after=8 individual_shell_bytes_before=53156 shared_shell_bytes_after=8674 vanilla_prefix_bytes=21236 colors_bytes=24950
```

The audit proved all 102 tag entries remain present, all tag comment/identity suffixes are byte-equivalent, all 85 researched tags retain their original `graphical_culture` and `graphical_culture_2d`, and every former shell RGB triplet appears exactly once in the appended color overrides.

The installed vanilla colors file is 21,236 bytes with SHA-256 `346e1ac0d82b929fca9e4917a60a689685948a83a9066ccc4e2ea257afa275a9`; the first 21,236 bytes of the mod replacement are byte-identical.

The resulting Event 006 shell count is 8 (seven shared researched shells plus the inert reservation), down from 86, for a reduction of 78 files.

The 85 researched per-tag shells occupied 53,156 bytes; the seven shared shells occupy 8,674 bytes, saving 44,482 shell bytes.

Including the retained inert shell and the required 24,950-byte complete colors replacement, the tracked Event 006 country-definition/color surface is 53,839 bytes before versus 34,307 bytes after, a net reduction of 19,532 bytes.

## Remaining risks and maintenance

The vanilla `common/countries/colors.txt` is a whole-file replacement in HOI4, so a future vanilla patch that changes that file requires refreshing the preserved prefix and rerunning the parity audit.

Historical Event 006 handoffs and plans still contain non-runtime references to the removed per-tag shell paths; those documentation references were outside this bounded source task and remain for a later documentation reconciliation.

The runtime/script search found no non-documentation references to the removed shell paths.

No fallback, placeholder, or gameplay simplification was used.
