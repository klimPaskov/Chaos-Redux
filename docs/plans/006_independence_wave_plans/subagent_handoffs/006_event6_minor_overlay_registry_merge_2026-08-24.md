# Event 006 minor overlay registry consolidation — 2026-08-24

## Scope

The six small overlay-only packages IW-005 Flanders, IW-022 Dalmatia, IW-025 Vojvodina, IW-035 Livonia, IW-059 Mesopotamia, and IW-085 Cyrenaica were consolidated to reduce parser-file bloat without changing gameplay ownership or central package admission.

## Changed source

- `common/scripted_triggers/006_independence_wave_minor_overlay_triggers_registry.txt`
- `common/scripted_effects/006_independence_wave_minor_overlay_effects_registry.txt`
- `common/decisions/006_independence_wave_minor_overlay_decisions_registry.txt`
- `docs/events/006_independence_wave/systems/iw005_flanders_overlay.md`
- `docs/plans/decision_category_formable_state_puzzle_plans/repo_inventory.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

The former eighteen package-local trigger/effect/decision files are removed. Each registry keeps a `# SOURCE` section for one original file. Trigger file-scoped constants are declared once at the registry top; all package-local identifiers and executable bodies are preserved.

## Boundary

These are living-carrier adapters, not Event 006 origin packages. The merge does not add tags, alter allocator admission, change reservation groups, introduce a crisis category, or expose any pre-event player-facing surface.

## Validation

- Exact old-to-new body comparisons are required before commit: no missing top-level trigger, effect, category, or decision block.
- Run the six maintained Event 006 validators from the mod root after this consolidation.
- Run a repository search for the removed source filenames and update current-facing docs; dated historical handoffs may retain provenance references.

## Remaining risk

No runtime GUI, live save, or in-game load claim is made by this source-only merge. Any future package admission or live-carrier behavior change remains a separate implementation and validation tranche.
