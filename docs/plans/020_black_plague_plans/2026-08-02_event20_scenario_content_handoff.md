# Event 020 scenario content handoff

Date: 2026-08-02

## Scope

This tranche adds intensity-aware player-facing text to the existing SCN-012 launch report and reconciles the Event 020 source matrices with the live two-tag runtime. It does not add a country tag, disease category, model, or alternate launch path.

## Runtime changes

- `chaosx.nr20.90` now selects Low, Medium, High, and Maximum launch descriptions from `global.black_plague_scenario_intensity` through the existing `triggerable_scenario_intensity` constants.
- Any unexpected intensity value retains the existing generic report as a guarded fallback.
- The descriptions report the live continent, established-state, internal-RTA-basin, and RTX Royal Basin totals without exposing implementation-history wording.
- A repeat SCN-012 signal now performs an idempotent intensity reconciliation before refreshing the shared disease board: it recounts established states, fills missing internal RTA brood markers, tops up the RTX Royal Basin, and restores the configured RTA/RTX division floors. Temporary candidate arrays, reservation flags, and reconciliation counters are cleared before ordinary pulses resume.
- Repeat reconciliation now validates the stored established-state, brood, Royal Basin, division-floor, and Evolution I-IV postconditions. A degraded save retains the scenario setup-failed status for the UI instead of being reported as a successful repeat.

## Source-of-truth changes

- `catalog_update_draft.md` now records the live workbook rows for Event 020, Diseases cluster `8`, and SCN-012, with `Needs Testing` remaining the user-owned validation status.
- `achievement_matrix.md` now records the live `020_black_plague_*` registry and the two-tag absorbed-brood counter used by `One Crown, Many Tails`.
- `event_chain_map.md` now records the live `.4` neighboring-threat allocation and `.90` SCN-012 report allocation, plus the RTA/RTX replacement for historical multi-tag wording.
- The last legacy `GetBlackDeathContinent`/`global.black_death_continent` surface was retired. The compatibility `chaosx.news.21` description now uses canonical mainland wording, so the weighted single-origin implementation is the only Event 020 origin contract.

## Validation

- Focused `hoi4_event_inspect` lint on `chaosx.nr20.90` returned `status: ok`, no blockers, and zero blocking diagnostics. The adapter still reports its documented workspace-wide helper/lifecycle deferral.
- Static inspection of `common/scripted_effects/020_black_plague_scenario_effects.txt` after the reconciliation change found balanced blocks, no unsupported comparison operators, and a clean scoped diff.
- The reconciliation postcondition trigger and scenario status localisation retain balanced blocks and no unsupported comparison operators; focused Event Inspector lint still reports zero blocking diagnostics.
- Touched scripts and localisation retain balanced blocks, no unsupported comparison operators, and UTF-8 BOM localisation encoding.

## Remaining boundary

Live scenario intensity, save/reload, and user-facing report playback remain user-owned because the repository forbids launching the Hearts of Iron IV executable from this workflow. Rat unit models remain explicitly outside the goal.
