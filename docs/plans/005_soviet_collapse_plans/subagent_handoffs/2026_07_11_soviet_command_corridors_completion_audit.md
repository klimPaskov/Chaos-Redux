# Event 005 Command and Corridors Completion Audit

**Date:** 2026-07-11
**Mode:** final read-only decision/mission completion audit
**Audited surface:** the implemented Command and Corridors tranche, including the Soviet mission board and refill lifecycle, live corridor geography, compromise resolution, release-cause propagation, selected-target desks, terminal actions, UWR/KMB hooks, AI gates, costs, and referenced decision assets.
**Verdict:** **PASS for the bounded Command and Corridors tranche.** No remaining P1/P2 gameplay, decision, mission, targeting, cost, AI, or asset blocker was found in the final shared tree. This is not a full Event 005 completion claim; the later tranches and the separately queued focus/country-package backlog remain outside this audit.

This audit did not edit gameplay files and did not create a commit. It created only this handoff.

## Required references consulted

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- Offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding
- Vanilla `common/decisions/_documentation.md`
- Vanilla `documentation/effects_documentation.md`
- Vanilla `documentation/triggers_documentation.md`
- Vanilla `documentation/script_concept_documentation.md`
- Vanilla `common/script_constants/documentation.md`
- Vanilla `common/on_actions/_documentation.md`
- Vanilla AST and WTT targeted-decision/mission precedents
- The accepted improvement addendum and all four implementation/audit handoffs in this Event 005 plan folder
- The final bounded localisation audit, `2026_07_11_soviet_localisation_audit.md`

## Historical blocker disposition

The earlier read-only audits correctly rejected the first implementation state. The final tree corrects every historical blocker:

| Historical blocker | Final disposition |
|---|---|
| Corridor missions used only a broad country-level geography gate | Corrected. Every corridor mission has a project-specific rail, depot, border, or logistics predicate in `available`, its inverse in `cancel_trigger`, and refill-only `cancel_effect`. |
| Corridor activation could bypass the mission-specific geography | Corrected during this final audit. All 42 activation sites now carry the same project predicate as their mission body. |
| Invalid corridor pointers could survive when no replacement existed | Corrected. Candidate selection clears the old state flag and variable before attempting a replacement. |
| Crisis priority bands were non-monotonic and posture-insensitive | Corrected. Crisis bands are monotonic and posture flags apply centralized offsets before priority scoring. |
| Opening missions were filled before the player chose a posture | Corrected. Event `chaosx.nr5.2` applies the option and then calls the existing opening-objective fill from `after`. |
| Neighbor release reactions read cause flags from the wrong scope | Corrected. The released actor is saved and read through an event target inside neighbor iteration. |
| Sponsor-interest flags had no live consumer | Corrected. All 17 preterminal foreign actions and the terminal aid action consume sponsor interest in AI weighting. |
| Release causes were recorded after pressure/setup consequences | Corrected. `soviet_collapse_apply_breakaway_setup_package` records the cause before the release package and Soviet pressure consumers run. |
| UWR contamination and KMB treaty/concession hooks were inert | Corrected. All three hooks have live callsites and feed the shared crisis values while the Soviet crisis is active. |
| KMB superiority was undefined and KMB costs were duplicated literals | Corrected. One reusable valid/superior neighbor trigger serves decisions and AI; all six KMB costs use script constants. |
| Compromise AI omitted PP budgeting, war state, time, or the live corridor | Corrected. PP hints use the payment constants, all three decisions respond to war and board age, and the corridor compromise requires a live selected corridor. |
| Selected-target visibility could bypass action-specific permission gates | Corrected. Selection controls human row display only; every action still requires its own target and payment triggers. |
| Hiding/reopening target desks could reset cooldowns | Corrected. Normal select/hide paths no longer activate or remove targeted decisions. Explicit resolution and terminal cleanup own removal. |
| Target cleanup was asymmetric across annexation, reintegration, reconquest, and terminal transition | Corrected. Shared reset/cleanup helpers cover both Moscow and the exact sponsoring country before target state is cleared. |
| Union Unmade left the preterminal desk without bounded actions | Corrected. Preterminal actions close and one Moscow reclamation action plus one foreign wartime-aid action remain available through the same target arrays. |
| Exact displayed fuel/equipment reserves failed strict `>` affordability gates | Corrected. Centralized fixed-point/integer sentinel constants make the exact displayed reserve sufficient. |
| Broad zero-callsite target-removal helpers remained as misleading dead code | Corrected during final integration. Only the live `_for_prev` resolution/terminal removal helpers remain. |

No historical blocker remains open.

## Mission-board proof

### Complete and exclusive classification

The live decision file defines 118 unique Soviet missions. The three family triggers classify the same set exactly once:

- Chain of Command: 37
- Corridors and Depots: 21
- Republic Settlement: 60

The family intersections are empty and their union equals all 118 definitions. Mission identifiers remain the original set (`001–089`, `091–108`, `111`, `119–128`); none were renumbered or replaced.

The family definitions are in `common/scripted_triggers/005_soviet_collapse_triggers.txt` under:

- `has_active_soviet_collapse_chain_of_command_objective`
- `has_active_soviet_collapse_corridors_and_depots_objective`
- `has_active_soviet_collapse_republic_settlement_objective`

### Existing scheduler retained

The implementation reuses one mission board and one capped refill lifecycle:

- one `soviet_collapse_activate_priority_operational_objectives`
- one `soviet_collapse_queue_objective_refill`
- one `soviet_collapse_set_objective_refill_monthly_cap`
- one `soviet_collapse_process_objective_refill`
- one `soviet_collapse_activate_opening_objectives`
- one refill event, `chaosx.nr5.128`

No second release scheduler, objective board, or recurring all-country on-action was introduced.

### Live corridor geography

The 21 corridor missions are:

- Rail: `005, 034, 053, 056, 063, 094, 099`
- Depot: `017, 038, 043, 062, 068, 069, 106, 127`
- Border: `047, 091, 098`
- Logistics: `006, 046, 061`

All 21 mission bodies have exactly one matching project predicate in `available`, the matching inverse in `cancel_trigger`, and `soviet_collapse_queue_objective_refill = yes` in `cancel_effect`. Cancellation removes an invalid project without recording ordinary mission success or failure.

The project predicates are centralized in `common/scripted_triggers/005_soviet_collapse_triggers.txt`:

- `has_soviet_collapse_selected_corridor_rail_project`
- `has_soviet_collapse_selected_corridor_depot_project`
- `has_soviet_collapse_selected_corridor_border_project`
- `has_soviet_collapse_selected_corridor_logistics_project`

The final activation invariant is also exact. Each corridor mission has two activation sites—one priority-prefill site and one remaining-slot site—for 42 total. All 42 carry the mission's matching project predicate:

| Project gate | Activation sites |
|---|---:|
| Rail | 14 |
| Depot | 16 |
| Border | 6 |
| Logistics | 6 |
| Broad-only, missing, or wrong | 0 |

This final correction matters because official vanilla documentation states that `activate_mission` ignores normal mission trigger conditions. The scheduler therefore now suppresses an incompatible project before activation rather than relying only on later cancellation.

### Compromise integrity

The three compromise resolvers cover 37/37, 21/21, and 60/60 family members. Every branch:

1. checks a family-specific resolution guard,
2. marks one active mission done,
3. removes that mission,
4. applies one compromise outcome,
5. queues the existing refill once.

Vanilla documents that `remove_mission` runs neither completion nor timeout effects, so compromise cannot also register the mission's ordinary decisive success or failure. Payment is likewise single-source: the decision calls one payment helper and does not add a duplicate ordinary cost.

Configured costs and exact gates remain coherent:

- Chain compromise: 15 Command Power, gate 14.99
- Corridor compromise: 35 Political Power, gate 34.99
- Settlement compromise: 50 Political Power, gate 49.99

The two political-power compromises use `ai_hint_pp_cost` from the same constants as their payment helpers. All three AI blocks account for war, priority/pressure, active-family existence, and the supported objective-activation grace signal. Current HOI4 documentation exposes no exact remaining-mission-time trigger, so the explicitly documented board-age signal is the available time input; this is not an unreported completion assumption.

## Release-cause and successor integration

`soviet_collapse_apply_breakaway_setup_package` records one dominant release cause before applying the release package and current Soviet pressure consequences. The four mutually exclusive causes affect:

- the released country's opening component package,
- Moscow's next prioritized family,
- sponsor interest,
- neighboring successor reactions,
- cause-aware AI strategy.

Cause flags do not occur in release eligibility, candidate selection, MTTH, timing, or scheduler logic. They therefore respond to a release without forcing or accelerating one.

Neighbor processing saves the released country as `soviet_collapse_release_actor` before entering neighbor scope and reads the cause from that event target. All 17 preterminal foreign intervention actions contain one sponsor-interest AI consumer.

## Selected-target lifecycle proof

The 17 preterminal foreign actions each contain:

- one matching action-specific `can_target_*` trigger,
- one matching action-specific `can_pay_*` trigger in `available`,
- the same payment trigger in `custom_cost_trigger`,
- active-phase gates in both row visibility and root targeting,
- one sponsor-interest AI modifier.

Selected-target references are confined to selection and human row-display helpers. They do not appear in the underlying action target, route, League, acceptance, dependency, or payment gates. AI continues to evaluate the full eligible dynamic target array.

Lifecycle mutation is now bounded:

- zero Event 005 `activate_targeted_decision` calls,
- normal select/hide effects contain no primitive targeted-decision activation/removal,
- only the live `_for_prev` resolution/terminal helpers remove targeted decisions,
- annexation and federal reintegration call shared target cleanup,
- reconquest resets desks before clearing the registry,
- terminal transition removes preterminal rows while retaining the registry for terminal wartime actions.

The shared target classes remain covered: base republics, Tajikistan, dynamic non-base republics, high-chaos successors, and terminal wartime targets.

The terminal surface contains bounded gameplay rather than a dead panel:

- Moscow: `soviet_collapse_coordinate_reclamation_front`
- Foreign patrons: `soviet_collapse_sustain_terminal_republic_front`

Both retain their action-specific target and affordability gates.

## Exact resource affordability

The final sentinel audit proves that the displayed amount is sufficient despite strict `>` syntax:

- Terminal reclamation uses 36,000 fuel with a `35999.99` gate and spends `-36000`; it uses 8 trains with a `7` gate and spends `-8`.
- Aid-corridor base/regional/major tiers use 12,000/18,000/26,000 fuel gates of `11999.99`/`17999.99`/`25999.99`.
- The same tiers use 4/6/8 trains and convoys with integer gates of `3`/`5`/`7`.
- Major and regional target classifications are disjoint, so the tiered extra spends produce exact totals rather than stacking ambiguously.

The terminal action reuses these same centralized payment triggers; no display/effect mismatch remains.

## UWR and KMB proof

- UWR saves the contamination actor before neighbor iteration, applies anthrax or plague to the victim state, and immediately records the first-time aftermath marker on that same state. The marker feeds Soviet Republic and Foreign pressure only while the crisis is active.
- KMB's resource-treaty completion calls `soviet_collapse_apply_kmb_treaty_corridor_crisis_hook`.
- KMB's superior-neighbor concession completion calls `soviet_collapse_apply_kmb_concession_crisis_hook` in KMB scope after the target operation succeeds.
- `is_soviet_collapse_kmb_valid_concession_target_from_root` and `is_soviet_collapse_kmb_superior_concession_target_from_root` are shared by target selection and AI.
- All six KMB decisions use the centralized `soviet_collapse_kmb_balance` cost table.
- UWR and KMB route-aware AI strategies are live and consume the corresponding readiness, treaty, concession, contamination, and release-cause signals.

No focus nodes were added as part of this tranche.

## Localisation and asset alignment

The separate final localisation audit reports no unresolved missing key, duplicate key, scripted-localisation collision, encoding fault, or mechanic-to-wording mismatch in the bounded tranche. In particular, all 21 corridor requirement tooltips state their live rail/depot/border/logistics condition, and terminal aid/reclamation text matches current target and resource gates.

The five decision sprites used by this tranche each resolve to one registered `spriteType` in `interface/005_soviet_collapse.gfx`, and every referenced DDS exists:

- `GFX_decision_soviet_collapse_command_goal`
- `GFX_decision_soviet_collapse_rail_goal`
- `GFX_decision_soviet_collapse_cleanup_goal`
- `GFX_decision_cut_rebel_supply_routes`
- `GFX_decision_soviet_collapse_foreign_intelligence`

No new mission icon or unregistered visual identifier was introduced.

## Meaningful validation scenarios

Static scope and lifecycle tracing supports the accepted scenarios:

- A depot-only selected state cannot activate a rail mission; a rail-only state cannot activate a depot mission.
- Destroying or losing the selected project's required geography cancels that mission and queues the existing bounded refill without recording success/failure.
- A stale corridor target is cleared even when no replacement state exists.
- A compromise can remove exactly one active member of its family and cannot run the removed mission's ordinary timeout effect.
- A human selected target does not bypass any action-specific route, dependency, acceptance, war, or resource gate.
- Hiding and reopening a desk does not reset targeted-decision cooldown state.
- Annexation, federal reintegration, reconquest, and terminal transition reset both Moscow and sponsor desks before clearing obsolete target state.
- Exact displayed terminal fuel/train/convoy reserves satisfy the final affordability predicates.
- Release-cause state changes setup/response/AI but cannot enter the release scheduler.

## Simplifications, omissions, and blockers

- No remaining P1/P2 blocker was found in the bounded Command and Corridors tranche.
- No fallback state, parallel mission board, second scheduler, static target exception, new focus node, or recurring world scan was introduced.
- No requested decision/mission, target class, UWR/KMB hook, terminal action, localisation surface, or referenced asset is missing from this tranche.
- The exact mission-countdown value is not exposed by current HOI4 triggers; compromise AI uses the explicitly documented objective-activation grace/board-age signal as its supported time input.
- This remains a bounded tranche pass, not a declaration that the full Event 005 focus, country-package, presentation, asset, or later-mechanic backlog is complete.
