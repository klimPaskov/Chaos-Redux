# IW-012 DM-01 force-tier repair

Date: 2026-07-28.

## Scope and disposition

The IW-012 decision audit found that the shared `independence_wave_secure_provisional_capital` mission could cancel every fragile release: `divisions_in_state size > 3` requires four divisions, while the fragile force tier intentionally caps the opening force at one to three divisions. The repair keeps DM-01 for every released country, but makes its guard force-tier aware. Fragile releases require two divisions (`size > 1`); viable, armed, and high-chaos releases retain the established four-division requirement. The thresholds remain centralized in `common/script_constants/006_independence_wave_decision_constants.txt`.

The shared `has_independence_wave_active_founding_mission` trigger now includes the bespoke IW-012 harbour crisis, preventing generic founding projects from starting beside that local survival deadline. The local harbour mission remains a separate owner of its five ledgers and failure consequences; DM-01 still records its own capital-garrison outcome rather than treating ledger stabilization as a free success.

## Validation evidence

- The decision now delegates its under-garrison cancellation branch to `independence_wave_secure_provisional_capital_garrison_satisfied`.
- The trigger branches on `independence_wave_force_level`, with a standard fallback when the level is absent, and reuses the existing `capital_scope`/`divisions_in_state` precedent.
- Static braces/depth checks pass for the modified decision, trigger, and constants files.
- No political-power store, free-unit loop, new tag, history rewrite, portrait, flag, advisor icon, or focus-tree replacement was introduced.

## Remaining boundaries

Live mission activation, force materialization, timing, save/load, and AI choice evidence remain parent-owned runtime checks. The global Event 006 status remains `HOLD / PARTIAL`.
