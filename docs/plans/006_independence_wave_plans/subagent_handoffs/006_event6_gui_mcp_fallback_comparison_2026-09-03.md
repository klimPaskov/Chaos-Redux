# Event 006 GUI MCP fallback comparison

Audit date: 2026-09-03. Scope: the Event 006 `independence_wave_status_window` animated status sprites and their static siblings, with an exact Event 012 GUI comparison to distinguish source defects from adapter diagnostics.

## Result

No source or asset change is justified. Event 006 retains four standard `frameAnimatedSpriteType` definitions paired with separately registered 64x64 static sibling sprites and mutually exclusive scripted-GUI visibility. The current HOI4 MCP adapter emits `GUI_ANIMATION_STATIC_FALLBACK_MISSING` for those four animated definitions, but the same diagnostic is emitted for Event 012's explicitly paired animated/static families. The warning is therefore an adapter association limitation, not evidence of a missing runtime texture or unsupported source relation.

## Event 006 evidence

- `hoi4.gui_inspect` on `independence_wave_status_window` with scenario `independence_wave_status_default` returned `GUI_INSPECTED`, status `ok`, complete source coverage, 48 inspected elements, zero missing or unresolved elements, and four fallback warnings at `interface/006_independence_wave.gfx:67,70,73,76`.
- The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a283367a7a27c7c147492a4605d45b40610b1b5530d1c67c688e5bf3251b7225/8be905380f32d6ff3e0671924ed8e7789d6f6072af2deed3c69591ec8d4cb934/gui-inspect.a92f0af359f5fdac.json`.
- `hoi4.gui_render` covered normal, active, and warning states at 1920x1080 and 1366x768. The source graph and truncation checks passed; the generated fixture raised `GUI_TAB_STATE_CONFLICT` because it marks every tab visible despite mutually exclusive source triggers. The render also repeats the four fallback warnings.
- The render comparison reported zero changed pixels in the offline representation. No live game, save/load, or blendframe playback claim is made.
- Event 006 source definitions remain in `interface/006_independence_wave.gfx` and `interface/006_independence_wave.gui`. No unsupported `fallback`, `static_sprite`, or duplicate alias key was added because the offline wiki and installed vanilla precedents do not define such a field for `frameAnimatedSpriteType`.

## Event 012 control comparison

- `hoi4.gui_inspect` on `africa_charter_window` with scenario `africa_charter_default` returned the same `GUI_ANIMATION_STATIC_FALLBACK_MISSING` diagnostic for three animated families that already have explicit static sibling sprites and GUI visibility pairing.
- The control artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b890ba7c18118cea1cee479fcb520c8f334b59920e002a6f834282f4de62cfe/0a434319a7f979b011f4fb6c7f578b366c2cae394004c47295217beac357bb58/gui-inspect.e1eaf761884e9e74.json`.
- This cross-event reproduction shows that the adapter does not infer sibling relationships from the project-owned `frameAnimatedSpriteType` and GUI visibility pattern. It does not show that Event 006 lacks a fallback texture.

## Validation and ownership

The semantic source matrix passes five mutually exclusive tab contracts, recognition/dependency/league/formable frame counts of 5/3/4/4, cleanup of all four frame variables plus the animation flag, and four static/animated sibling pairs. The Event 006 allocator still passes with the pre-event crisis surface retired and the exact 3/4/5/7/10 ladder.

The Event 006 GUI worker was stopped after its MCP turn stalled; it made no source or asset edit. The parent reviewed the source and both MCP artifacts. No GFX fallback patch, replacement artwork, generic alias, or runtime wiring change was made.

Remaining GUI acceptance is dynamic-state and live click/playback proof, not a known texture-path defect. Event 006 remains `HOLD / PARTIAL` for the broader package because portrait, flag, emblem, rights, admission, audio, reachability, and other documented gates remain unresolved.
