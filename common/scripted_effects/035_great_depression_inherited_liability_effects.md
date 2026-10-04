# Event35 inherited-liability consumer helpers

This Event35-owned package implements the accepted bounded receipt consumer tranche.
Its source is [035_great_depression_inherited_liability_effects.txt](035_great_depression_inherited_liability_effects.txt).
The immutable owner contract remains [035_great_depression_region_effects.md](035_great_depression_region_effects.md).
Acceptance is the explicit user's full Event35 package goal and the accepted remaining-work findings in [the completion audit](../../docs/plans/035_great_depression_plans/subagent_handoffs/inherited_consumer_completion_audit_2026-10-03.md).
Source implementation does not establish engine execution or full inheritance completion.
The parent reviews this package and owns all existing-file hooks, upstream producers, balance review and final integration.

## Helper map

All entry helpers execute in COUNTRY THIS, which is the receiver or closing owner even when ROOT is a different country.
State scopes are read only and use PREV to address that receiver.
No helper changes the immutable history, another country, buildings, resources, missions, Severity, Chaos, modifiers, event targets or scheduling.

| Helper | Inputs | Outputs | Side effects and call sites |
| --- | --- | --- | --- |
| `great_depression_check_inherited_liability_ledger` | Existing source and mutable arrays | Country flag `great_depression_inherited_ledger_valid` | Clears/recomputes a shape diagnostic, called by register, rebuild and resolve |
| `great_depression_register_inherited_liability` | Still-valid regional companion call and its just-appended row | Country flag `great_depression_inherited_checkpoint_registered` | Allocates private parallel slots and checkpoints exactly that source row, parent hook immediately after regional append |
| `great_depression_read_inherited_liability_row` | Helper-local `inherited_row`, caller-owned returned temporary storage | Six internal temporary values documented below | Read only, used by rebuild and resolve after ledger validation |
| `great_depression_add_inherited_row_pressure` | Validated eligible unresolved row and its caller-owned visibility/disconnection temps | Adds to three normal country pressure summaries | Rebuild's internal row consumer, no physical stage mutation |
| `great_depression_reset_inherited_liability_summary` | Current country episode | Zero normal summaries and current view episode | Rebuild and matching cleanup |
| `great_depression_rebuild_inherited_liability` | Current active receiver and its stored history/checkpoints | Normal hidden summary outputs | Builds helper-local current view and supplied corridor groups, parent hook in hidden-component rebuild |
| `great_depression_resolve_inherited_liability` | Exact normal resolution inputs and appropriate one-shot authority flags | Country flag `great_depression_inherited_resolution_applied` | Writes one private outcome, consumes resolution inputs/flags on all returns, parent paid completion/disposition/owner-transfer hook |
| `great_depression_freeze_inherited_liability_summary` | Still-active closing episode | Normal `great_depression_inherited_last_*` summary and last-ledger-valid country flag | Rebuilds and freezes before state cleanup, unresolved remains unresolved |
| `great_depression_clear_inherited_liability_runtime` | Exact `great_depression_inherited_cleanup_episode_id` | Cleared cached view on matching episode | No history/checkpoint/outcome removal, consumes cleanup input on every return |

Temporary private row output storage is `inherited_row_ready`, `inherited_row_state`, `inherited_row_owned`, `inherited_row_eligible`, `inherited_row_visible` and `inherited_row_disconnected`.
Rebuild and resolve initialize all six before the nested call.
Private callers must validate the ledger and initialize those outputs before invoking the reader.
The reader validates the integral index and both source/checkpoint bounds before any indexed read, then validates the raw integral state ID against built-in `global.states` before entering a variable state scope.
Invalid private indices return state unavailable and false diagnostic temps without an array-element read.
Public callers consume normal summaries and country flags, so no callee-created temporary output escapes.

## Immutable input and bounded current view

Source prefix is `great_depression_inherited_region_`, with suffix `_entries`.
The exact existing 21 columns are `episode_id`, `event34_episode_id`, `state_id`, `role`, `project_profile`, `project_stage`, `protection`, `fragility`, `control`, `damage`, `receipt_id`, `collapse_receipt_id`, `legacy_receipt_id`, `corridor_receipt_id`, `exhaustion`, `result`, `center_index`, `stage`, `live_control`, `civilian_baseline`, `military_baseline`.
All 21 lengths must agree and remain within `constant:great_depression_region_contract.ledger_cap`, currently 256.
An entirely absent source ledger is explicitly empty, with no element reads or loop iterations.
Offline Data structures lines 1069-1076 define the empty default, zero-based indices and `^num` length.
Installed effects documentation lines 6397-6410 define native `resize_array` growth and preallocation before indexed writes.
Those native lines do not independently describe every absent-array read, so the empty-default assertion is wiki-backed and native execution remains unverified.
The consumer never initializes, resizes, clears, appends, updates or repairs those source arrays.

Reverse append order selects one latest current-Event35-episode receipt for each raw state ID.
Receipt numbers are opaque, so numeric receipt order is not used as time.
A newer ignored, forbidden, foreign, incompatible or uncheckpointed row suppresses the older row for that state.
Older Event35 episodes do not contribute.
Different Event34 episodes remain eligible for different states within the same active Event35 episode.
The receiver's latest national Event34 context is not used to erase other valid local receipts.

The current view excludes special or nonhuman receivers, receivers that do not use normal civilian systems, inactive/incoherent episodes, wrong owners, conversion prohibitions and another live center episode.
Temporary loss of control preserves the original owner's liability and adds disconnection evidence.
Permanent ownership change excludes pressure for that former owner even before its explicit transfer-outcome hook.
No foreign state is mutated or charged.
The visible test uses exact current registry membership plus matching live center episode, never the historical center-index column.

Explicit unavailable is -1 and remains unavailable in all source and checkpoint columns.
Unavailable metadata does not prove a completed project, sound fragility, protection, zero exhaustion, intact damage, no secured value or a corridor identity.
The `unknown_fact_count` reports unavailable source fields on eligible latest rows.
The mapped physical stage stored by the accepted companion remains a distinct known registration result.
Its hidden stage projection does not manufacture per-state source project history from the aggregate snapshot.

## Mutable checkpoints and resolution

Private prefix is `great_depression_inherited_liability_`, with suffix `_entries`.
The 14 columns are `episode_id`, `event34_episode_id`, `state_id`, `receipt_id`, `collapse_receipt_id`, `checkpoint_day`, `authorization_id`, `completed_id`, `forbidden`, `outcome`, `resolution_day`, `resolution_authorization_id`, `checkpoint_work_days`, `checkpoint_project_stage`.
Five immutable source-key mirrors bind each mutable slot to the source row and receiving country.
Registration grows only these private arrays, fills unregistered slots with unavailable, and then writes the one proven accepted row.
All private lengths must agree and cannot exceed source history length.
Previously registered checkpoints are never reset by replay.

Register inside `great_depression_apply_inherited_region` immediately after the 21 source append operations, while `great_depression_region_validated` and `great_depression_region_call_*` still exist.
Call it only on the accepted nonduplicate append branch and before `great_depression_clear_region_inputs`.
It captures the source conversion prohibition while that proof is still available.
It also reads the exact state's current authorization serial, historical completed serial, work days and project stage.
Missing serials associated with active or spent work become unavailable, rather than proven no work.
No authorization/completion receipt on an uninitialized state permits the native initial serial baseline zero.
Work days and project stage remain unavailable when absent.

A later paid completion may settle the newest matching row when:

- Source row, Event35 episode, Event34 episode, regional receipt and state identity all match.
- The row is still unresolved, owned, controlled, permitted and compatible with the receiver's center and project episodes.
- Native completed stage and receipt, matching current/completed authorization serial, supported recovery project type and full work duration are present.
- The completed serial exceeds the completed serial captured at checkpoint and is at least the authorization serial captured there.
- The completion date is after checkpoint, or same-day work has increased above an available checkpoint work value.
- That serial is not the spent failed authorization, and the current physical state is reopened or restructured.

Authorization active at checkpoint is deliberately allowed to complete on the same serial.
For example, authorization 5 with historical completed 4 can finish after collapse, while completed 4 cannot settle it.
This preserves part8's funded-work continuation requirement.
Explicitly failed work remains spent under the existing native project contract and needs a valid subsequent authorization.
No helper invalidates funded work itself.
Protection alone is not a permanent liability settlement.

Resolution inputs are normal variables with prefix `great_depression_inherited_resolution_`: `row`, `episode_id`, `event34_episode_id`, `receipt_id`, `state_id`, `outcome` and, for paid completion, `authorization_id`.
There are no inferred required identity defaults.
Use an immutable history row index, not a visible center index.
Inputs and both authority flags are consumed even on rejection.

| Requested input outcome | Required proof | Stored private outcome |
| --- | --- | --- |
| `constant:great_depression_center_stage.reopened` | Actual qualifying paid project completion and supplied exact completed authorization | Paid resolution 1 |
| `constant:great_depression_center_stage.liquidated` | One-shot country flag `great_depression_inherited_disposition_paid` from the exact successful paid liquidation branch and native liquidated state | Liquidated resolution 2 |
| `constant:great_depression_center_stage.abandoned` | Same paid authority flag from exact successful paid abandonment branch and native abandoned state | Abandoned resolution 3 |
| `constant:great_depression_region_control.transferred` | One-shot country flag `great_depression_inherited_permanent_transfer_proven` from exact permanent owner-change path plus native ownership inequality | Transferred resolution 4 |

Stored unresolved is 0.
These private values are file-local `@` outcome enums, not new coefficients or project serials.
Parent callers use the existing shared input enums above.
Disposal authority must come from the validated payment/ownership transaction for that exact source row.
A retained state flag alone is not payment proof and must never create the authority flag during an ordinary pulse.
Controller loss alone cannot satisfy permanent transfer.
The resolver grants no rewards or salvaged value and does not duplicate capacity.

Example after a proved native paid completion, in the exact owning COUNTRY scope:

```txt
set_variable = { great_depression_inherited_resolution_row = matching_latest_source_row }
set_variable = { great_depression_inherited_resolution_episode_id = great_depression_active_episode_id }
set_variable = { great_depression_inherited_resolution_event34_episode_id = great_depression_inherited_region_event34_episode_id_entries^matching_latest_source_row }
set_variable = { great_depression_inherited_resolution_receipt_id = great_depression_inherited_region_receipt_id_entries^matching_latest_source_row }
set_variable = { great_depression_inherited_resolution_state_id = completed_exact_state_id }
set_variable = { great_depression_inherited_resolution_authorization_id = completed_exact_authorization_id }
set_variable = { great_depression_inherited_resolution_outcome = constant:great_depression_center_stage.reopened }
great_depression_resolve_inherited_liability = yes
```

The parent obtains `matching_latest_source_row` through a bounded source-history scan for the completed exact state and current episode.
The resolver independently rejects superseded rows and mismatched source identities.
Inside the existing STATE completion helper, enter its actual country owner to call this COUNTRY helper and pass state values through PREV.
Trace the native callback binding, since entering a country does not rebind ROOT.

## Existing rates and summary outputs

No tuning constants were added or changed.
The package uses only the existing `great_depression_hidden_component` rates and bounds.

| Contribution | Supplied/current condition | Existing rate |
| --- | --- | --- |
| Credit | Any supplied speculative, unfinished, failed/abandoned work, failed protection or fragile/severe condition | `credit_boom_inheritance`, once per row |
| Industrial source condition | Supplied fragility, failed protection, damage or disconnection, or actual current control loss | `industrial_inherited_region`, once per row |
| Exhaustion demand | Supplied positive exhaustion, including a positive fraction | `demand_distressed_center`, once per row |
| Hidden physical demand | Distressed/idled/shuttered/abandoned or liquidated stored mapped stage | `demand_distressed_center` / `demand_idled_center` / `demand_shuttered_center` / `demand_abandoned_center` |
| Hidden physical industry | One of those supported nonoperating hidden stages | `industrial_center_pressure`, once per row |

Protection/completion with no affirmative adverse source facts adds no extra credit or industrial source pressure.
Visible physical stage pressure contributes zero here because the main helper already counts it.
These are ongoing cause summaries, not a second national aggregate opening shock.
Exhaustion is a presence-sensitive consequence using an existing rate.
There is no unsupported quantity-to-pressure scaling or invented exhaustion unit.

Normal output prefix is `great_depression_inherited_`.
Outputs are `view_episode_id`, `current_count`, `unresolved_count`, `hidden_count`, `disconnected_count`, `paid_count`, `liquidated_count`, `abandoned_count`, `transferred_count`, `foreign_count`, `excluded_count`, `missing_checkpoint_count`, `unknown_fact_count`, `project_fact_count`, `corridor_group_count`, `corridor_member_count`, `corridor_unresolved_count`, `corridor_paid_count`, `corridor_disposed_count`, `credit_pressure`, `demand_pressure`, `industrial_pressure` and `net_pressure`.
All summaries reset on every rebuild.
The ledger-valid country flag describes shape validity, not native execution or full data coverage.
`missing_checkpoint_count` includes absent checkpoints, bad source linkage, invalid state identity or malformed outcome on latest current-episode rows.
A positive value means incomplete coverage, never proven absence of debt.
Unknown fields are counted as fields, rather than as states.
`project_fact_count` counts current owned eligible rows, resolved or not, that carry at least one supplied project profile, project stage, protection or fragility value.
`transferred_count` counts a retained latest-row transfer disposition under a foreign owner and after regain, without creating live pressure for a foreign state.
Foreign-row pressure is excluded and its transfer evidence remains in private outcomes.

Each positive component is bounded by zero and the existing hidden maximum 5.
The helper's standalone net summary uses the existing -5 to 5 overall bound.
Parent integration adds the three components before the main helper's existing total-net clamp.
Never add both the three components and this net summary.

## Exact parent hooks and migration

The parent integration contract is accepted and queued under the explicit parent instruction dated 2026-10-03.
Registration follows the accepted 21-column append while companion proof remains available.
The national rebuild keeps the flat inherited credit term, because the boom's credit hangover is a national fact, and adds this consumer's credit and demand components on top of it.
The flat inherited industrial term applies while `project_fact_count` is zero and is replaced by this consumer's industrial component once a current row carries a supplied project, protection or fragility fact.
The existing main net clamp is unchanged.
The aggregate national opening formula remains unchanged and the consumer's net summary is not added separately.
Paid completion, paid disposition and permanent owner-change callbacks dispatch in COUNTRY THIS to the newest exact-state row of the current episode after their proof fields are written.
Closure freezes before state cleanup and clears this cache before active episode removal.
No hidden-row UI, hidden-row paid producer or recovery blocker belongs to this integration tranche.

| Existing owner location | Hook and ordering | Remaining ownership |
| --- | --- | --- |
| `great_depression_apply_inherited_region`, accepted new append | `great_depression_register_inherited_liability = yes` immediately after all 21 append operations, before call-input cleanup | Parent edits companion |
| `great_depression_rebuild_hidden_components` | Keep the flat inherited credit addition, rebuild this view after its current inputs reset, add the credit and demand components once, and add the industrial component in place of the flat industrial term only when `project_fact_count` is positive, all before final net calculation | Integrated; preserves aggregate opening and visible stage pressure, and does not add the consumer net summary |
| Existing registered-country pulse `great_depression_weekly_pulse` | Uses the hidden rebuild hook, with no new timer or world scan | Parent retains registered schedule |
| `great_depression_complete_center_project` success | Resolve exact state and latest receipt after final native completed serial/stage/day/work and physical outcome are written, before terminal cleanup | Parent copies exact callback country/state identity |
| `great_depression_abandon_selected_center` / `great_depression_auction_or_reorganize_failed_assets` success | After actual payment and native disposition, supply exact source identity and one-shot paid authority, then resolve | Parent validates paid branch, chooses the native liquidation versus abandonment request explicitly |
| Permanent owner-change reconciliation | When native owner has changed, record former owner's exact latest source row with transfer authority and native owner proof | Parent distinguishes permanent owner change from controller loss |
| `great_depression_freeze_episode_summary` | Freeze inherited summary while active episode and native state proof still exist | Parent aligns canonical episode report |
| Recovery / invalid registered actor cleanup | Supply exact closing episode, clear this cached runtime before active episode is removed, preserve source-linked ledger | Parent final cleanup |

The main inheritance credit and industry blocks are national flat terms, while this consumer is differentiated per-source debt.
Event 34 has no per-region project system, so its real handoff rows carry no project profile, project stage, protection, fragility or exhaustion value; only live control and damage are supplied.
Removing both flat terms would therefore drop about 2 net stress from every real Event 34 handoff, so the parent kept the national credit hangover and made the flat industrial term a stand-in that the exact regional industrial output replaces only when a supplied project fact exists.
The row credit branch fires only on supplied facts, so it adds to the national hangover without counting the same fact twice, and the flat and row industrial terms are never both added.
The consumer's standalone net summary remains diagnostic and is never added on top of the three components.
The aggregate opening formula is unchanged.

For historical rows created before the hook exists, rebuild reports missing checkpoint coverage rather than inventing arrival-time authorization, old work or frozen conversion permission.
Registration requires the authoritative still-live accepted companion call.
Retrospective migration therefore needs authentic retained producer proof, or the parent must carry the exact unsupported checkpoint/prohibition gap.
Do not reset immutable history, replay the public national API, or retroactively treat old completion as a new paid result.
Every helper has executable in-package consumers or an explicit requested parent lifecycle hook.
No central shared router or wrapper skill is introduced.

## Corridor, salvage and resolution limits

Corridor groups use only positive supplied `corridor_receipt_id` plus their exact Event34 episode.
Role/profile alone, physical adjacency and historical flags cannot create a group.
Grouping includes the supplied latest local members and their source-linked outcomes, including foreign members awaiting exact transfer disposition.
Groups and counts are helper-local calculations.
The normal summary counts do not prove a whole corridor registry, restored rails, market access, accepted network breakup or a permanent disconnected scar.

Restoration still requires an authentic complete Event34 member registry, a real mapped paid transport/reconstruction action and actual connection proof for the required members.
Breakup requires the accepted paid disposition transaction and exact surviving network membership.
A disconnected scar needs the existing paid/physical outcome, source receipt and parent-owned scar consumer.
No restoration/breakup/scar flag is manufactured here.

The existing project authorization targets visible registered centers.
A hidden row with no such current registration has no executable paid producer in this package.
Promotion, bounded targeted works/transport/finance resolution, transfer adoption and hidden-row action producers remain parent integration dependencies.
The package adds no recovery-blocking gate, since paid resolution is not currently mapped for every hidden row.

Opaque secured legacy IDs contain no amount, building token, secured output or spent-value payload.
Salvage stays unavailable pending authentic Event34 owner data.
A paid liability outcome does not redeem or mark a legacy as consumed.
Existing Event35 reconstruction rewards remain solely owned by the native project helper.

## Cleanup, targets and future integration

No event target is needed.
Validated state IDs are scoped only synchronously and no persistent pointer is added.
Checkpoints, source links and distinct outcomes remain durable compact history.
The freeze helper preserves unresolved-at-close and unknown/missing coverage counts without declaring success.
Matching runtime cleanup only clears cached summaries and country diagnostics.
A stale closing episode cannot erase the current view.
No current liability flag is derived from the companion's permanent historical hidden/disconnected flags.

There are no new player-managed values, localisation keys, UI windows, sprites, icons or assets.
Parent integration may reuse existing visible action and cause text after final behavior is reviewed.
No humanitarian, environmental, Deaths or Condemnation dependency is added.
The parent hooks are integrated.
Hidden-row paid paths, corridor restoration, breakup and scar, secured-value salvage and multi-region inherited priority are closed for Event 35 as blocked on Event 34, which has no per-region project or corridor system; they would need an authentic Event 34 producer first and must not be invented here.

## Evidence

[Implementation handoff](../../docs/plans/035_great_depression_plans/subagent_handoffs/inherited_liability_consumer_implementation_2026-10-03.md) contains exact changed files, reproducible source-contract scenarios, source hashes, MCP provenance/coverage limits and reference paths/line spans/revisions.
The fixtures exercise actual source with conservative temporary-frame cleanup.
They do not certify native arrays, callback timing, physical connection, transfer/adoption, construction, saves or AI balance.
