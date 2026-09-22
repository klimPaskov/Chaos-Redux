# 15. Shared system integration

## Selection, type, and catalog

Preserve Event 79 as Minor Repeatable, Chaos level 1, Diplomacy, Medium member, and To Be Reworked. Medium is member severity. It is not a probability and cannot be copied into a numeric participation field.

The authoritative editable catalog is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Update its Event 79 row and cluster membership through the project workbook workflow, then regenerate export CSVs with `.tools/export_event_catalog_csv.py`. The CSVs supplied with this package's inputs are snapshots. This planning task does not modify the workbook or its exports.

The supplied cluster snapshot does not yet express this full Event 79 rework. The integration owner must update the existing Diplomacy cluster membership without creating a second cluster with a similar name. Align member IDs, roles, probabilities, minimum tiers, and danger metadata in the corresponding runtime arrays. Do not infer a numeric probability from the word Medium.

Event selection reserves target and capacity before recording a successful firing. No valid target or no capacity produces unavailable selection, not a zero-point phantom firing. An accepted root call consumes its normal repeat state once. Preserve the shared scheduler's countdowns, weight recovery, multiplayer mode, and cluster accounting.

## Event Log and Event Details

The opening record identifies the selected target and stage. The takeover record identifies the actual winner. Evolution records identify stage activation, not ordinary project completions. The expanded Event Details page explains the 100 threshold, five positive families, interference, real subject result, and concurrent-target behavior.

Use existing log and settings owners. Relevant shared files include `chaosx_logic_effects.txt`, `chaosx_events_log_effects.txt`, `chaosx_settings_effects.txt`, `chaosx_scripted_gui_events_log.txt`, and `chaosx_events_log_popup.gui`. Verify exact repository paths and current owners before editing.

Evolution logging uses the established context fields, including `events_log_evolution_event_id`, `events_log_evolution_type`, `events_log_evolution_stage`, `events_log_evolution_tier`, `events_log_evolution_actor`, and `events_log_evolution_has_actor`. Check `is_current_evolution_enabled` before recording through `record_events_log_evolution_entry`. The exact current contract must be inspected in the implementation repository.

## Chaos impact map

| Event 79 outcome | Chaos ownership | Event 79 additional delta |
| --- | --- | --- |
| Open or register a race | No destabilizing world change yet | 0 |
| Gain or lose Influence | Private contest progress | 0 |
| Deliver ordinary investment or aid | Normal development | 0 |
| Unlock either evolution or expand capacity | Capability only | 0 |
| Real ruling-ideology change | Existing shared political-change owner | 0 additional |
| Actual successful puppeting | Existing shared subject-change owner, ordinary minor puppet +1 under supplied mechanics | 0 additional |
| Target became a major before puppeting | Existing major-subject owner, +3 under supplied mechanics | 0 additional |
| A separate real war or peace occurs | Existing war or peace owner | 0 additional |
| Race closes because the target becomes human or disappears | Administrative closure | 0 |

Event 79 must not add a second puppet point in its completion event. The positive Chaos consequence is the real subject relationship. A leadership transition contributes only when the shared political-change definition actually recognizes that transition. An adviser appointment alone is not automatically an ideology change.

The design has no event-owned negative Chaos reward for withdrawing a campaign or cancelling an investment. Removing an unfinished Influence race does not reverse an already counted real puppet or war.

## Universal discounted costs

Use the existing universal quote, affordability, payment, component receipt, refund, and settlement contract. Recompute a quote immediately before payment. Record actual paid amounts and refund only those amounts once. A tooltip preview is not a locked price or a receipt.

Physical equipment donations conserve equipment. Their material quantity is not eligible for a payment discount that creates extra recipient weapons. Administrative political costs may use their supported cost family. Factory commitments need a separately verified owner adapter and a stated eligibility policy. Until its exact discount path is proven, factory-days remain undiscounted and visibly identified as such.

Do not alter Black Friday's event lifecycle or its source registry from Event 79. Event 79 is a consumer. Do not create a second incompatible discount formula or infer active discounts from an event title.

## Common data helpers

Use project economic and stockpile helpers only for their documented behavior. A helper that calculates an economy-scaled factory grant does not reserve factories, perform construction, or pay costs. Equipment helpers that mutate a temporary amount in place require reinitialization for each component and each participant.

Every proposed helper in the implementation plan is a contract name until implemented and verified. Do not assume arbitrary named arguments are supported by the Clausewitz scripted-effect system. Use documented temporary inputs and the project's actual invocation patterns.

## Test-country registration

Event 79 needs a package-owned CXT extension that prepares test fixtures without automatically taking over normal countries. Follow the existing modifier-free hidden-idea carrier and `<carrier>_apply` setup contract. Register on startup through the established bounded path and retain the tag-scoped CXT repair hook.

The fixture can expose controlled target selection, seed snapshots, project receipts, staged completions, and multi-race cases. It must clearly mark forced races as test-only. The ordinary user-facing Event 79 root and target selection remain separate.
