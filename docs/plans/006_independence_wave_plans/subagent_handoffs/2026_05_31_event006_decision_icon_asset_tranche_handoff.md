# Event 006 Decision Icon Asset Tranche Handoff

Status: implemented and wired. Event 006 remains incomplete.

Scope:
- Created a reusable static 32x32 decision-icon family for implemented Event 006 decisions.
- Reused generated Event 006 decision-category source art as the source mode for the smaller decision icons.
- Wired decision sprites in `interface/006_independence_wave_icons.gfx`.
- Replaced generic decision icons in `common/decisions/006_independence_wave_decisions.txt` with Event 006-specific icon references.
- Did not edit country flags, country files, history files, Event 005 files, localisation, focus trees, ideas, or spreadsheet files.

Changed files and paths:
- `interface/006_independence_wave_icons.gfx`
- `common/decisions/006_independence_wave_decisions.txt`
- `docs/assets/006_independence_wave/decision_icons/`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_decision_icon_asset_tranche_handoff.md`
- `gfx/interface/decisions/independence_wave/decision_independence_wave_*.dds`

Behavior:
- Host aftermath, committee survival, Patron Ledger, Patronage Recognition, New States Congress, Formation Ledger, Border Commission, and Sealed Dossier decisions now use Event 006-specific decision icons.
- The icons cover talks, autonomy, observers, loyalist arms, garrisons, depots, capital holdout, recognition, congress aid, league charters, border surveys, anti-patron audits, archives, local land councils, railway timetables, patron advisers, occult registry, and quiet-dead census surfaces.

Validation run:
- Brace balance passed for `interface/006_independence_wave_icons.gfx` and `common/decisions/006_independence_wave_decisions.txt`.
- Every new DDS file is 32x32 and ARGB8888.
- Every processed PNG is 32x32 with `srgba` channels and transparent corners.
- Every `GFX_decision_independence_wave_*` decision icon reference has a sprite definition.
- `common/decisions/006_independence_wave_decisions.txt` has no remaining generic vanilla decision-icon assignments.
- Touched files contain no unsupported comparison operators.
- `git diff --check` returned clean.
- `git status --short -- gfx/flags common/countries history/countries` returned clean.
- No Event 005 files were edited in this tranche.

Remaining gaps:
- This is a static decision-icon tranche only. It does not complete focus icons, idea icons, report/news images, animated category art, formation seals, scripted GUI panels, final package portraits, or remaining super-event images.
