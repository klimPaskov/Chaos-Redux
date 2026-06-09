# Event 006 Idea Icon Asset Tranche Handoff

Status: implemented and wired. Event 006 remains incomplete.

Scope:
- Created static 64x64 idea icons for all implemented Event 006 ideas.
- Reused generated Event 006 source art from the decision-category icon tranche as the source mode for this static idea-icon family.
- Wired idea sprites in `interface/006_independence_wave_icons.gfx`.
- Replaced generic `picture =` tokens in `common/ideas/006_independence_wave_ideas.txt` with Event 006 picture tokens.
- Did not edit country flags, country files, history files, Event 005 files, localisation, focus trees, decisions, or spreadsheet files.

Changed files and paths:
- `interface/006_independence_wave_icons.gfx`
- `common/ideas/006_independence_wave_ideas.txt`
- `docs/assets/006_independence_wave/idea_icons/`
- `docs/events/006_independence_wave.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_idea_icon_asset_tranche_handoff.md`
- `gfx/interface/ideas/independence_wave/idea_independence_wave_*.dds`

Behavior:
- The provisional committee, civic mandate, officer mandate, national directorate, revolutionary committee, patron cabinet, regional compact preparation, regional compact, Volga old-state memory, Assyrian recognition congress, free-city board, Lukiko charter, Sokoto federation, Guarani land congress, and Charrua assembly spirits now use Event 006-specific idea art.
- Local-polity and historically sensitive package icons remain neutral institutional art rather than claiming real cultural, royal, or religious symbols.

Validation run:
- Brace balance passed for `interface/006_independence_wave_icons.gfx` and `common/ideas/006_independence_wave_ideas.txt`.
- Every new DDS file is 64x64 and ARGB8888.
- Every processed PNG is 64x64 with `srgba` channels and transparent corners.
- Every Event 006 `picture = independence_wave_*` token has a matching `GFX_idea_*` sprite definition.
- `common/ideas/006_independence_wave_ideas.txt` has no remaining generic vanilla picture assignments.
- Touched files contain no unsupported comparison operators.
- `git diff --check` returned clean.
- `git status --short -- gfx/flags common/countries history/countries` returned clean.
- No Event 005 files were edited in this tranche.

Remaining gaps:
- This is a static idea-icon tranche only. It does not complete focus icons, report/news images, animated category art, formation seals, scripted GUI panels, final package portraits, or remaining super-event images.
