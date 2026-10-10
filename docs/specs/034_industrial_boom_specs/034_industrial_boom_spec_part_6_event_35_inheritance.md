# Industrial Boom specification, part 6: Event 35 inheritance

Event 35 Great Depression 2.0 is the failure state of Industrial Boom.
Event 34 keeps no depression modifier, severity value, recovery category or state shutdown system of its own.
It freezes its final condition and calls Event 35's public gateway `great_depression_start_or_deepen` for the same country.

Event 35's side of this contract is implemented and documented in [docs/events/035_great_depression.md](../../events/035_great_depression.md) (Reusable crisis API and Event 34 inheritance) and in [the reusable crisis API spec](../035_great_depression_specs/035_great_depression_reusable_crisis_api.md).
This part defines what Event 34 must produce.

## Implemented handoff

The implemented Event 34 side lives in `common/scripted_effects/034_industrial_boom_collapse_handoff_effects.txt` and runs from `chaosx.nr34.3`:

1. `industrial_boom_freeze_collapse_snapshot` copies live owner fields into `industrial_boom_snapshot_*` variables once, allocates the collapse receipt, and freezes one inherited region.
2. The boom idea is removed and `industrial_boom_active` is cleared, so no boom bonus survives into the depression.
3. `industrial_boom_deliver_collapse_snapshot` prepares the request with caller `industrial_boom_collapse`, `consequence_no_pacing`, inherited history, queued report and news, the evolution floor, and the severity and opening-shock profile for the evolution.
4. A rejected delivery retries privately through `chaosx.nr34.4` up to `industrial_boom_handoff.maximum_attempts` times, `retry_days` apart, then records `industrial_boom_collapse_retry_exhausted`.
5. An accepted delivery counts the completed boom, sets the inherited-Overheating pressure (`overheating_pressure_factor` of final Overheating), the Event 35 recent-industrial-expansion target signal for 730 days, and any supplier-contract carryover, then clears the frozen state.

The handoff is a consequence, not a second pacing event, and never rolls the Negative Economy cluster.
If Event 35 is already active, the same call deepens the existing episode in place without a second category or modifier.

What remains pending is the producer side: the snapshot currently records interim defaults because the live boom state of parts 2 to 5 does not exist yet.

## Snapshot fields

Event 34 must fill every field from live state at the moment of collapse.

| Snapshot field | Source in the design | Current value |
| --- | --- | --- |
| `industrial_boom_snapshot_evolution` | Active stage, 0 to 3 (part 5) | Always 0 |
| `industrial_boom_snapshot_final_overheating`, `_peak_overheating` | Overheating at collapse and the highest value this boom | Opening seed (part 2), raised only by supplier contracts |
| `industrial_boom_snapshot_landing_state` | Failed when the landing mission, Prevent the Crash or the Emergency Production Halt failed; prepared when a landing mission was active; otherwise unknown | Constant `landing_state` (prepared) |
| `industrial_boom_snapshot_reserve_units` | 1 when a reserve is held, 0 otherwise | Constant 1 |
| `industrial_boom_snapshot_project_units` | Number of projects at Integrating or Secured | Constant 1 |
| `industrial_boom_snapshot_region_units` | Number of Industrial Regions still controlled | Constant 1 |
| `industrial_boom_snapshot_shock_units` | Severe unabsorbed shocks in the last 180 days | 0 |
| `industrial_boom_snapshot_dangerous_days` | Days spent in Dangerous or Critical | 0 |
| `industrial_boom_snapshot_repeat_history_count` | Completed booms before this one | Counted on accepted delivery |

The landing-state values are Event 35's `great_depression_event34_snapshot_state` (unknown, prepared, failed).
Event 35 turns these fields into starting Severity; Event 34 never computes Severity itself.

## Evolution mapping

| Event 34 stage at collapse | Event 35 floor | Severity profile | Opening shock |
| --- | --- | --- | --- |
| Baseline | Baseline | `inherited_baseline` | `event_34_baseline_collapse` |
| I Speculative Mania | Financial Contagion | `inherited_contagion` | `event_34_speculative_collapse` |
| II The Industrial Miracle | Social Collapse | `inherited_social` | `event_34_miracle_collapse` |
| III Runaway Industrialization | The Second Great Depression | `inherited_worldwide` | `event_34_runaway_collapse` |

The mapping is implemented in `industrial_boom_prepare_collapse_request`.
The inherited stage is a floor: Event 35 keeps a higher stage it already has.

## Regional handoff

Event 35 registers inherited states through `great_depression_register_inherited_region`, keyed by Event 34 episode and region receipt, and turns them into Depression Centers or hidden liabilities.
The implemented freezer sends one primary state and copies optional per-region fields when they exist.
Event 35's plans record multi-region and corridor delivery as blocked on these Event 34 producers.

Event 34 must deliver every controlled Industrial Region as a primary role and every Evolution III spread state as a corridor role, each with its own region receipt, using Event 35's region constants:

| Event 34 state | Event 35 field and value |
| --- | --- |
| Ordinary project, speculative project, Miracle project, spread state | `profile`: ordinary, speculative, miracle, corridor |
| Building or Integrating | `project_stage`: unfinished |
| Secured | `project_stage`: completed |
| Abandoned, or abandoned speculative project | `project_stage`: abandoned, liquidated |
| Protected / protection spent in the last 90 days / never protected | `protection`: protected, failed, none |
| Sound / Fragile Miracle Region / Fragile region under Let It Run | `fragility`: sound, fragile, severe |
| Controlled / occupied / lost | `control`: connected, temporary_loss, transferred (already measured by the freezer) |
| Building damage share | `damage`: intact, damaged, heavy (already measured by the freezer) |

A state the target no longer owns still informs Severity through region and shock units, but receives no modifiers.
Event 35 never recreates a project reward that Event 34 did not secure.

## Edge cases

- **Country deleted before delivery.** The delivery fails closed, retries stop when the country no longer exists, and no ghost depression is created.
- **Natural disaster during handoff.** The disaster keeps its damage and Deaths; Event 34 records only the shock; Event 35 receives the damaged state once.
- **Another economic crisis.** Event 35's own conflict rules decide; Event 34 never runs a parallel depression.

## Acceptance

- The same country receives Event 35 at the mapped floor, once, without counting pacing.
- Starting Severity differs between a boom that crashed with a held reserve and secured projects and one that crashed with none.
- Boom bonuses are gone before Event 35's opening shock applies.
- Event 35 reads only the frozen snapshot, never live Event 34 variables, after delivery.
- An active depression is deepened in place.
- Every controlled region and spread state reaches the Event 35 region ledger with the mapped values.
- A save and reload during retry neither duplicates nor loses the handoff.
