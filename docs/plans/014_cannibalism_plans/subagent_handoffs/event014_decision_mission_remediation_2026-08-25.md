# Event 014 decision and mission remediation handoff

Date: 2026-08-25.

Owner: Event 014 decisions and missions.

## Scope and status

This patch owns Event 014 decision categories, decisions, maintained Unified mission activation, narrow Event 014 triggers and timing constants, and the Event 014 cost localisation surface.

Shared event logs, Event Details, settings, super-event GUI, model assets, focus layout, country packages, and the dedicated GUI layout were not changed.

The source-level phase matrix is implemented for the Unified, Warlord, and Wendigo command surfaces where the existing route flags prove mutually exclusive phases.

The 18-row achievement tracker remains permanently non-interactive, and the two-row network alert category remains an intentional alert surface.

## Changed files and identifiers

- `common/decisions/014_cannibalism_decisions.txt`: phase-gated Unified War Machine, Unified Global Campaign, Warlord, and Wendigo actions; route-aware Unified two-slot availability tooltips on every player-started Unified mission family action.
- `common/decisions/categories/014_cannibalism_categories.txt`: `visible_when_empty = no` for ordinary, Warlord, Wendigo, and Unified categories; tracker and network-alert exceptions remain `yes`.
- `common/scripted_triggers/014_cannibalism_triggers.txt`: `cannibalism_unified_player_mission_slots_available`, four family continuation triggers, larder route-current triggers, Unified War Machine and Global Campaign phase triggers, Warlord phase triggers, and Wendigo phase triggers.
- `common/script_constants/014_cannibalism_constants.txt`: existing `cannibalism_decision_timing.logistics_minimum_days` and `rotation_minimum_days` floors raised to 90 days.
- `localisation/english/014_cannibalism_l_english.yml`: Event 014 Larder, consumed state-population, victory-receipt, convoy-hunt-receipt, and enemy-loss-receipt texticons inserted into the exact cost strings without changing ledger labels or numeric values.

## Visibility and density matrix

The mission row is excluded from primary-action counts because it is a status objective rather than a player-started action.

| Surface and phase | Visible primary actions | Result |
| --- | ---: | --- |
| Unified command | Four command actions; one Unified command mission row | Within six |
| Unified Larder | Four shared setup actions plus exactly one current consumption method | Five |
| Unified War Machine foundation | Air-program foundation only before recruitment flags open | One |
| Unified War Machine recruitment | Legion create/surge, three origin specialists, and Bone Guard | Six |
| Unified War Machine operations | Continental, enemy-front, naval, convoy receipt, silent anchorage, and air operations | Six |
| Unified Global Campaign cell | One cell action | One |
| Unified Global Campaign campaign | Campaign, terror, border, and postwar actions | Four |
| Unified Global Campaign counterwar | Coalition hub and pressure-conversion actions | Two |
| Unified world-end | Two terminal consumption actions | Two |
| Warlord baseline | State consumption, Scavenger, Feast, Origin Specialist, Bone Guard, and emergency reinforcement | Six |
| Warlord network | Network Cadre, foreign seed, intensification, one origin operation, and emergency reinforcement | Five |
| Warlord endgame | Abandon, align, synchronized attack, one origin operation, and emergency reinforcement | Five |
| Wendigo setup | Three anchor actions, pack training, enemy receipt muster, and inherited cell | Six |
| Wendigo countdown | Three anchor actions, frozen corridor, one countdown adjustment, and terminal-hunt launch | Six |
| Wendigo terminal | Terminal-hunt press only | One |
| Achievement tracker | Eighteen read-only rows with `always = no` availability | Intentional non-interactive exception |
| Network alerts | Two route-response actions | Intentional two-row alert surface |

Containment and international categories retain their established route and target triggers rather than receiving speculative broad phase rewrites.

The decision MCP route is not exposed in this runtime, so exact engine-expanded target-array row counts for those categories cannot be proven from an authoritative scenario evaluator; this residual is recorded instead of hiding gameplay actions by guesswork.

## Unified mission cap

`cannibalism_unified_player_mission_slots_available` explicitly accepts zero or one active flag among `cannibalism_unified_command_mission_active`, `cannibalism_unified_larder_mission_active`, `cannibalism_unified_war_machine_mission_active`, and `cannibalism_unified_counterwar_mission_active`.

The four family continuation triggers allow an action to continue an already active family while the other slot is occupied, but prevent a third family from starting.

`cannibalism_unified_player_mission_slots_tt` says that only two paid Unified missions may be active and instructs the player to finish or cancel an existing mission before opening a new route.

The cap is attached to command, larder, War Machine, and counterwar player-started actions, including convoy-harvest and terminal-consumption actions, but not the automatic compact or counterplay missions.

Existing `cannibalism_unified_record_*_operation` helpers remain the sole activation call sites, and their complete, partial, failure, cancellation, and all-runtime cleanup helpers clear the same four flags and runtime variables.

## Duration decision

Before this patch the existing timing formulas produced effective minima of 63 days for logistics stabilization (`21 + 42` timeout buffer) and 49 days for formation rotation (`14 + 35` timeout buffer).

These are repeatable stabilization objectives rather than emergency actions, so the decisions skill minimum of roughly 90 days applies.

The existing shared constants now use 90-day floors, producing 132-day and 125-day effective minima without duplicating magic numbers or changing the existing modifiers, buffers, or maxima.

## Costs and localisation

The cost audit found no Event 014 gameplay-changing decision above four distinct consumed resource types after the accepted cost reduction.

The five supplied semantic texticons are used without substitution: `£cannibalism_larder_texticon` for Larder, `£cannibalism_state_population_texticon` for consumed state population, `£cannibalism_victory_receipt_texticon` for battlefield victory receipts, `£cannibalism_convoy_hunt_receipt_texticon` for convoy-hunt receipts, and `£cannibalism_enemy_loss_receipt_texticon` for enemy-loss receipts.

Held equipment and readiness checks remain described as requirements in their existing strings and were not converted into consumed costs.

The localisation file retains its UTF-8 BOM.

## AI, route validity, and cleanup

No AI weight, MTTH, target score, or probability-bearing modifier was changed.

The required pre-change `hoi4.probability_inspect` used the decision adapter against `common/decisions/014_cannibalism_decisions.txt` and reported 95 discovered candidates, zero unresolved inputs, and no weighted patch surface; therefore no `hoi4.probability_compare` was required.

The cap and phase triggers use existing route, target, ownership, category, and mission flags, so AI receives the same availability gating as the player without a speculative weight change.

The existing family active flags, mission cancel triggers, resolution helpers, cooldowns, target identity checks, receipt epoch limits, and global cleanup continue to prevent duplicate rewards, receipt reuse, free-unit loops, and stale mission state.

No `Prison Host` identifier or player-facing animation-control action is present in the scoped Event 014 decision, trigger, category, constant, or localisation files.

## MCP and GUI evidence

No Event 014 dedicated GUI source was patched.

The required prior GUI evidence is recorded in `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_direct_gui_mcp_reaudit_2026-08-24.md` for `cannibalism_early_header_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and `cannibalism_wendigo_command_window`.

That evidence reports truncated diagnostics, missing distinct state artifacts, and the renderer returning 1920x1080 despite isolated 3840x2160 requests; it also records that the renderer ignored requested resolutions and state variants.

The exact decision MCP blocker is that no `hoi4.decision_inspect` or decision-specific MCP route is exposed in the installed tool surface.

No GUI rewrite or visual acceptance claim is made from the renderer artifacts.

## Validation and residuals

Source scans verified that every cap-tooltip family helper is defined and referenced, every non-exception category uses `visible_when_empty = no`, and all five supplied texticon tokens occur in the scoped Event 014 cost localisation.

The source-level phase matrix was reviewed against existing flags and mission definitions, and the localisation BOM was checked after editing.

No live game was launched, and no gameplay or renderer fidelity claim is made.

Residual design-level issues are the unexpanded containment/international target-array density proof, the unavailable decision MCP route, and the prior dedicated-GUI renderer limitations.

No shared GUI or event-log surface was altered.
