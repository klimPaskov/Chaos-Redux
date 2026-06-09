# Event 006 Focus Icon Asset Tranche Handoff

## Scope

Created and wired a non-flag Event006 focus icon family for `common/national_focus/006_independence_wave_focus.txt`.

No subagent was spawned for this tranche because the scope was bounded to known files and reused existing Event006 generated source art.

## Files Changed

- `common/national_focus/006_independence_wave_focus.txt`
- `interface/006_independence_wave_icons.gfx`
- `docs/events/006_independence_wave.md`
- `docs/assets/006_independence_wave/focus_icons/manifest.md`
- `docs/assets/006_independence_wave/focus_icons/gfx_handoff.md`
- `docs/assets/006_independence_wave/focus_icons/reuse_ledger.md`
- `docs/assets/006_independence_wave/focus_icons/contact_sheets/focus_icons_contact_sheet.png`
- `docs/assets/006_independence_wave/focus_icons/source_png/goal_independence_wave_*_source.png`
- `docs/assets/006_independence_wave/focus_icons/processed_png/goal_independence_wave_*.png`
- `gfx/interface/goals/independence_wave/goal_independence_wave_*.dds`

## Implementation

- Added 25 `GFX_focus_independence_wave_*` sprite definitions to `interface/006_independence_wave_icons.gfx`.
- Replaced all Event006 focus icon references that used vanilla generic sprites with Event006 focus sprites.
- Created 25 final 94x86 DDS files in `gfx/interface/goals/independence_wave/`.
- Added an asset manifest, GFX handoff, focus-by-focus reuse ledger, and contact sheet.
- Updated the Event006 documentation to treat focus icons as a wired Event006 asset family.

## Validation

- `common/national_focus/006_independence_wave_focus.txt` has 57 `GFX_focus_independence_wave_*` references.
- No `GFX_goal_generic_*`, `GFX_focus_generic_*`, or `GFX_goal_support_communism` references remain in the Event006 focus tree.
- 25 final focus DDS files exist and identify as 94x86.
- Sprite names referenced by the focus tree are registered in `interface/006_independence_wave_icons.gfx`.
- This tranche did not edit `gfx/flags`, `common/countries`, or `history/countries`.

## Remaining Risks

- The icons are branch-level generated-derived sprites, not bespoke art for every individual focus.
- Major-route animated focus or formation seal art remains future asset work and must follow the frame-animation workflow with real source frames.
