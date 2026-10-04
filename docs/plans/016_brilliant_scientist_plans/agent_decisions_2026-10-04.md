# Event 016 agent decisions, 2026-10-04

Disposition: accepted and implemented under the full-authority mandate that the user granted for the Event 016 takeover.
Each decision below records the choice, the reason, and the implementation evidence.
Runtime behaviour that only a live session can prove is marked as such.

## D1. Host project board: review selector instead of approval

Decision: the meaningless approval order is removed, and one instant review selector drives the generic board.
The direct family rows already start every stage, so a separate approval only cost Political Power without changing anything.

Selector semantics:

- The review moves to the next family after the current one with a recorded stage, wrapping once through all fifteen families.
- The selected stage and the active, suspended, damaged, replicable, replicated, publishable, and published flags are derived from the aligned ledgers by `brilliant_scientist_refresh_directorate_project_selection`.
- The refresh runs after the selector, after each board order, at the end of `brilliant_scientist_refresh_project_counts`, and at the end of `brilliant_scientist_sync_project_force_runtime_after_ledger_change`, so incident damage, suspension, and dismantling keep the flags current.
- "Not replicated" means the independent stage has not reached the current stage, so a family that advances after replication can be replicated again at its new stage; the replicated-family count still counts each family once.
- "Public or mixed governance" means the public compact, or a secret Directorate answering to a Public Science Council, a University Research Network, or a Cabinet Safety Board.
- "Kruger not openly hostile" means Grievance below the extreme band and government control not lost.

Related corrections:

- The never-cleared native suspend, resume, cancellation, and approval request flags, their command variables, and the replication and publication receipt variables had no consumer and are removed; each order now acts and then refreshes the selection.
- Suspend, cancel, and replicate are unavailable while the reviewed family's own stage order is running, so a pending completion callback cannot resurrect a dismantled or suspended stage.
- A suspended family can no longer begin its next stage: every Deployment, Weaponization, native Prototype integration, and no-DLC Prototype row has a not-suspended requirement. Without it, suspension released capacity that the player could immediately spend advancing the same family.
- Replication completes against its locked stage even if the family advances meanwhile; only a family change, suspension, or host loss cancels it.

AI decision: the review selector is used by the AI. It stops on a programme with affordable replication, permitted publication, a resumable suspension, or active damage, and it is blocked when no programme needs board work.
The existing order weights are kept, with one guard: the AI suspends or cancels only a damaged programme or when government control is compromised or lost.
Before this change the six controls were unreachable, so no live AI behaviour regressed; the guard prevents the revived low weights from dismantling healthy programmes at random.

Evidence: `common/decisions/016_brilliant_scientist_directorate_project_board.txt` (generic block and stage-row guards), `common/scripted_effects/016_brilliant_scientist_effects.txt` (selector and refresh), `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt` (refresh hook), `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt` (idle, payment, publication, and AI triggers), `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt` (selected programme name, stage, and status), and `docs/events/016_brilliant_scientist/systems/directorate.md`.

Reachability trace: replication calls `brilliant_scientist_replicate_project_to_requested_stage`, which raises the independent stage and recounts `brilliant_scientist_independently_replicated_family_count` through `brilliant_scientist_refresh_project_counts`.
Publication sets `brilliant_scientist_directorate_publication_completed`.
Both are the remaining inputs of `brilliant_scientist_achievement_public_method_is_complete` and `brilliant_scientist_achievement_clean_break_is_complete`, and `brilliant_scientist_reconcile_old_host_after_transfer` copies the independent stages into the former host's ledger.

Needs live game: decision-list presentation of the scripted programme names, and AI cycling cadence.

## D2. Portal raid province checks without a province scope

Decision: every `var:<province> = { ... }` scope in the Portal raid and beachhead code is replaced, because HOI4 has no province scope and the raid framework exposes `var:target_province` as an integer.

- The facility raid's native `building = { tags = facility }` target guarantees a facility in the selected province, so the target-validity trigger drops its province block and keeps the state, war, and destination checks.
- Extraction copies the raid province once and pastes it through `meta_trigger` into `any_province_building_level` for each facility family; `remove_building` keeps its documented `province = var:ROOT.target_province` argument.
- The breach state is registered on itself, so the runtime trigger drops the province-to-state test.
- Breach control uses a new STATE-scope trigger, `brilliant_scientist_portal_breach_province_is_controlled_by_root`, which pastes the stored province into a country-scope `controls_province`; the sealing decision's target and cancel triggers and the sealing settlement share it.

Evidence: `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`, `common/decisions/016_brilliant_scientist_portal_containment_decisions.txt`, `docs/events/016_brilliant_scientist/systems/portal_raider_api.md`.
References: installed `common/raids/_documentation.md` (raid instance variables and building target types), `documentation/triggers_documentation.md` (`any_province_building_level`, `controls_province`, `meta_trigger`), `documentation/effects_documentation.md` (`remove_building` province argument), and the offline wiki Triggers page (`controls_province = <id>`).

Needs live game: the native building raid supplying `var:target_province` for a facility target, and the meta-trigger province paste resolving in state scope.
Not changed: the state-target Portal raid still lands in `var:ROOT.target_province`; whether the engine fills that variable for a state target remains a live-game question recorded for the raid owner.
