# Event 014 Decision and Mission Final Audit v4

Date: 2026-08-24

Owner: `event014_decision_audit_v4`

Scope: Event 014 Cannibalism decision categories, decisions, missions, costs, tooltips, timers, AI target gates, cleanup, exploit prevention, unit recruitment, population consumption, spread/convergence/terminal route locks, and decision-owned scripted-GUI evidence.

## Outcome

The six requested five-resource cost contracts are now four-type contracts in the shared worktree, and their payment triggers, payment helpers, constants, and icon-first localisation agree.

This pass also repaired four player-facing affordability tooltip gaps for the joint suppression, convergence interdiction, Island Host landing, and aftermath institutional recovery decisions.

No Prison Host, direct pre-reveal Hannibal decision or scripted-GUI leak, duplicate canonical consumption request, free recruitment path, free Larder yield from an unusable state, or short recovery bypass was found in the audited source.

Fresh decision-owned GUI evidence and current post-patch probability evidence remain blocked by the installed MCP service, so this handoff does not claim visual fidelity or a probability comparison.

## Changed files owned by this pass

- `common/decisions/014_cannibalism_decisions.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_decision_final_audit_v4.md`

The decision and localisation files also contain concurrent Event 014 changes from other agents. Only the four availability wrappers and four requirement localisation keys listed below were authored by this pass. The concurrent six-cost constant, trigger, payment, and cost-localisation hunks were preserved and audited in place.

## Identifiers changed by this pass

Decision availability wrappers:

- `cannibalism_joint_suppression_operation`
- `cannibalism_interdict_likely_convergence_host`
- `cannibalism_land_against_island_host`
- `cannibalism_rebuild_feeding_state_institutions`

Localisation keys:

- `cannibalism_joint_suppression_requirements_tt`
- `cannibalism_convergence_interdiction_requirements_tt`
- `cannibalism_island_landing_requirements_tt`
- `cannibalism_aftermath_institution_requirements_tt`

## Before and after behavior

Before this pass, the four decisions exposed a raw scripted affordability trigger directly in `available`, which gave a disabled button no named reason beyond the generic engine state.

After this pass, each decision wraps the same unchanged affordability trigger in `custom_trigger_tooltip` and retains the existing `custom_cost_trigger`, target trigger, target-root route gate, effect tooltip, effect helper, cooldown, and AI weight.

The new requirement strings use the same resource texticons as the cost rows, so they do not add a fifth spendable type or spell resource labels in place of icons.

The six requested cost contracts were already changed by a concurrent worktree tranche when this pass began; no cost hunk was reverted or duplicated.

| Contract | Spendable types after the concurrent fix | Gameplay/payment alignment | Cost localisation |
| --- | --- | --- | --- |
| `cannibalism_logistics_cost_land` | manpower, support equipment, motorized equipment, trains | `cannibalism_can_pay_logistics_cost` and `cannibalism_pay_logistics_cost` use those four types for a land theater; command power is a zero compatibility slot | icon-first dynamic row at `localisation/english/014_cannibalism_l_english.yml:50` |
| `cannibalism_logistics_cost_island` | manpower, support equipment, motorized equipment, convoys | the same logistics helper switches the fourth transport to convoys for an island theater; command power is a zero compatibility slot | icon-first dynamic row at `localisation/english/014_cannibalism_l_english.yml:51` |
| `cannibalism_joint_suppression_cost_text` | manpower, Command Power, infantry equipment, support equipment | `cannibalism_can_pay_joint_suppression_cost` and `cannibalism_execute_joint_suppression` use the four non-zero fields; trucks are zero in the shared helper | icon-first row at `localisation/english/014_cannibalism_l_english.yml:1443` |
| `cannibalism_convergence_interdiction_cost_text` | manpower, Command Power, infantry equipment, support equipment | `cannibalism_can_pay_convergence_interdiction_cost` and `cannibalism_execute_convergence_interdiction` use the four non-zero fields; trucks are zero in the shared helper | icon-first row at `localisation/english/014_cannibalism_l_english.yml:1448` |
| `cannibalism_island_landing_cost_text` | manpower, infantry equipment, support equipment, convoys | `cannibalism_can_pay_island_landing_cost` and `cannibalism_execute_island_host_landing` use the four non-zero fields; command power is a zero compatibility slot | icon-first row at `localisation/english/014_cannibalism_l_english.yml:1457` |
| `cannibalism_aftermath_institution_cost_text` | manpower, Command Power, support equipment, trains | `cannibalism_can_pay_aftermath_institution_cost` and `cannibalism_complete_aftermath_institutional_recovery` use the four non-zero fields; trucks are a zero compatibility slot | icon-first row at `localisation/english/014_cannibalism_l_english.yml:1470` |

The zero compatibility fields remain because the shared payment helpers still accept a fixed set of temporary variables; they are set to zero, are not affordability-gated, and are not displayed.

## Severity-sorted issue list

### Blocker: decision-owned GUI MCP evidence is unavailable

The required `hoi4.gui_inspect` route was attempted for the five Event 014 windows `cannibalism_early_header_window`, `cannibalism_network_window`, `cannibalism_warlord_command_window`, `cannibalism_revealed_command_window`, and `cannibalism_wendigo_command_window`.

The correctly shaped early-window request with `scenario = { id = event014_decision_gui_audit_v4 }` returned `ARTIFACT_STORAGE_LIMIT` with `artifactCount = 0` and the message `Artifact batch cannot fit after reclaiming expired artifacts`.

The five-window inspect batch did not complete, and the correct `hoi4.gui_render` call for the early window timed out after 180 seconds with `timed out awaiting tools/call after 180s`.

No GUI source was changed in this pass, so `hoi4.gui_rewrite` was not appropriate.

The compact GUI source still exposes the intended early values, network state, Warlord Larder/Frenzy/Alignment/capacity, revealed Larder/Network/loyalty/terminal progress, and Wendigo anchors/countdown/capacity/terminal status, but a fresh visual fidelity claim is blocked.

### Blocker: named probability-auditor and current probability refresh are unavailable

The required named `chaosx_ai_probability_auditor` route was not exposed as a callable tool in this runtime.

The direct `hoi4.probability_inspect` decision adapter previously returned 95 candidates with `poolComplete = false`, zero available scenario candidates, 32 required inputs, and no unresolved diagnostics at artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a96791ee01aeda97abe575041d783d754beb67e74fd8809509500/9d8828873c26b9a83e1be6df65856969f29e39154c7824a97d08232faab24cca/probability-inspect-7094c91933c5.json`.

The mission adapter discovery artifact at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11ef6a639f8a19c52dc8a40f69dab8ceea46de458205862ee62aa61cc7b313e5/17af84c5755570c12276824553b662fa463b4ac7e408a5de81973ce14fa6dbd3/probability-inspect-7094c91933c5.json` reported no mission candidates and suggested the decision adapter.

Post-tooltip decision refresh attempts timed out after 180 seconds with the same MCP service timeout.

No AI weight or probability-bearing modifier was changed in this pass, so no probability compare is claimed.

### Medium: visible decision density needs runtime confirmation and likely phasing

The source category blocks contain more than six child decisions in several phases even though route flags and target filters reduce the live set.

The containment category contains 13 baseline decisions plus five maintained-objective entries, the Warlord command category contains 15 entries, the Wendigo command category contains 12 entries, the unified War Machine category contains 14 entries, the unified Larder category contains nine entries, and the unified global-campaign category contains eight entries.

The achievement tracker contains 18 permanently unavailable read-only entries and is not an operational action surface.

The category visibility and phase flags are coherent, but the blocked GUI render prevents proving that every scenario keeps visible primary actions at six or fewer.

Recommended owner fix: phase or hide low-frequency actions in the dense containment, Warlord, Wendigo, Larder, War Machine, and global-campaign categories, then rerun the five-window GUI matrix before completion.

### Medium: two early mission timeout minima are below the skill duration band

`cannibalism_restore_supply_corridor_mission` has a minimum timeout of 63 days because its minimum 21-day hold is followed by a 42-day buffer.

`cannibalism_rotate_compromised_formations_mission` has a minimum timeout of 49 days because its minimum 14-day hold is followed by a 35-day buffer.

The missions retain dynamic hold requirements, success, partial, failure, and cleanup behavior, and the shorter values may be an intentional emergency-response cadence, but the decisions-and-missions skill recommends at least 90 days for an easy maintained mission.

Recommended owner fix: raise `logistics_timeout_buffer_days` from 42 to 69 and `rotation_timeout_buffer_days` from 35 to 76 if the 90-day floor is accepted, then run the required same-scenario AI probability compare.

No duration constant was changed here because this is a balance-bearing timing decision rather than a syntax or lifecycle defect.

### Medium: broader legacy cost rows remain over budget outside the six requested contracts

The six requested rows now meet the four-type budget, but the wider Event 014 localisation still contains legacy rows that spell out resource names and/or expose more than four simultaneous spendable types.

Examples include `cannibalism_unified_mobile_consumption_cost_text` with seven displayed values, `cannibalism_unified_counterwar_conversion_cost_text` with five, `cannibalism_unified_counterwar_operation_cost_text` with five, `cannibalism_unified_silent_anchorage_cost_text` with five, and `cannibalism_wendigo_press_terminal_hunt_cost_text` with five.

These rows are outside the six local contracts requested for this tranche and were not silently reduced.

Recommended owner fix: audit each remaining gameplay-changing decision and scripted-GUI action, consolidate real payment contracts to four spendable types, and replace literal resource labels with the registered texticons in the same gameplay change.

### Low: terminal Wendigo hunt duration remains a local magic number

`cannibalism_wendigo_terminal_hunt_mission` uses `@CANNIBALISM_WENDIGO_TERMINAL_HUNT_MISSION_DAYS = 120` in `common/decisions/014_cannibalism_decisions.txt:2440` rather than the shared Event 014 timing constants.

The 120-day value is in the medium mission band and has no observed behavior defect, but it should be centralized if the decision timing constants are next edited.

### Low: other raw affordability triggers still lack named custom tooltips

The four targeted cost contracts now have named requirement tooltips, and logistics already had one, but other paid decisions still expose direct `available = { scripted_cost_trigger = yes }` blocks.

Remaining examples include Island Host blockade and rescue, aftermath identification and memorial, ritual-economy actions, several Warlord actions, and several Wendigo actions.

Recommended owner fix: add concise custom requirement tooltips in a separate bounded localisation tranche rather than concatenating more prose into cost rows.

## Decision-category lifecycle notes

- `cannibalism_containment_category` opens only for active ordinary countries with `cannibalism_containment_decisions_open` and closes at world end; its early scripted GUI reports Field Hunger, Command Integrity, Cult Cohesion, primary theater, and active mission.
- `cannibalism_network_alerts_category` opens only when a real inbound route has a screenable state and uses the compact early header; humane screening and route sealing are separate response choices.
- `cannibalism_international_response_category` opens for Evolution II active countries or registered reconstruction participants and excludes Event 014 countries as actors; target triggers reject dead, capitulated, invalid, or already revealed routes as appropriate.
- `cannibalism_reconstruction_category` opens only for a registered reconstruction participant before world end; state-target decisions require the matching recovery phase and controller.
- `cannibalism_warlord_command_category` opens for a living Warlord with its command flag or for a reveal-gated inherited recruitment route; target decisions require controlled states, route flags, origin knowledge, caps, equipment, Larder, and population.
- `cannibalism_unified_command_category`, `cannibalism_unified_larder_category`, `cannibalism_unified_war_machine_category`, and `cannibalism_unified_global_campaign_category` are individually gated by unified route flags and stage capacity, preventing all operational rows from appearing at once in intended progression.
- `cannibalism_unified_world_end_category` opens only during final mobilization or after the ordinary terminal world-end flag; the terminal decisions are not a pre-reveal advertisement.
- `cannibalism_wendigo_command_category` opens only for the revealed transformed Hannibal country during pre-lock; `cannibalism_wendigo_counterwar_category` opens for valid external responders or a terminal-hunt defender.
- `cannibalism_achievement_tracker_category` is a read-only 18-entry presentation category with no gameplay effect, cost, cooldown, or AI behavior.

## Cognitive-load notes

The compact scripted-GUI headers are value-focused rather than action warehouses, and the network window is a separate post-Evolution-II view with view controls rather than hidden gameplay buttons.

The early header values have direct tooltips describing cause, threshold, consequence, and response; the Warlord, revealed, and Wendigo headers use matching tooltip rows for Larder, alignment or loyalty, capacity, anchors, countdown, and terminal status.

The category-level source still has dense phase families, especially containment and Warlord command, and the blocked runtime GUI evidence leaves simultaneous visible-action counts unresolved.

Mission rows use dedicated objective tooltips and separate success, partial, failure, and cancellation effects rather than exposing long raw trigger blocks.

The 18 tracker rows are intentionally read-only and should not be counted as primary actions.

## Mission quality matrix

| Mission family and id | Owner/category and target region | Requirement and duration | Success, partial, failure | Duplicate and cleanup risk |
| --- | --- | --- | --- | --- |
| Restore supply corridor: `cannibalism_restore_supply_corridor_mission` | ordinary responder; containment; saved primary theater state | payment plus controlled valid theater, formation, support, truck, and train/convoy reserves; dynamic 63–168 days | maintained supply and formation hold; partial relief or failed corridor changes hunger, integrity, and node strength | one active flag; clear helper removes flag, duration, hold variables, and dynamic burden modifier |
| Rotate compromised formations: `cannibalism_rotate_compromised_formations_mission` | ordinary responder; containment; saved primary theater state | payment plus controlled theater and replacement formation screen; dynamic 49–133 days | maintained screening; partial screening or desertion/cell growth | one active flag; clear helper removes flag, duration, hold variables, division floor, and burden modifier |
| Investigation: `cannibalism_investigation_mission` | ordinary responder; containment; primary state plus node id/generation when present | ration audit, forensics, or ritual action receipts; dynamic 120–210 days | evidence and node suppression; recoverable partial record; failed trail burns and integrity falls | one active and one resolved flag; node identity and generation reject recycled targets; cancellation resolves earned partial progress |
| Hold prison: `cannibalism_hold_prison_mission` | ordinary responder; containment; one random controlled prison/camp state with active node | bounded actor pulse requires garrison plus support and transport reserve; dynamic 120–210 days | continuous hold secures compound; partial staff removal; failed cordon strengthens cell/node | auto-start is guarded by active/resolved flags; target state, node id/generation, hold, duration, and division floor are cleared |
| Reach island: `cannibalism_reach_island_mission` | foreign responder; international response; exact Island Host country and actor generation | reconnaissance, blockade, or landing receipts against a valid Island Host; dynamic 150–270 days | route opened and alignment/war-support result; partial charts/forward position; failed expedition result | one active flag and exact target generation; observer unregister and target variables clear on every outcome |
| Break network: `cannibalism_break_network_mission` | foreign responder; international response; exact active network country and actor generation | repeated valid joint suppression receipts; dynamic 150–240 days | route family breaks and Network Reach falls; partial link damage; failure allows route replacement | one active flag and exact target generation; target identity, progress, goal, duration, and observer clear |
| Stop unification: `cannibalism_stop_unification_mission` | pre-reveal foreign responder; international response; likely convergence Host and actor generation | active convergence, unrevealed target, maintained war pressure, and due-date window; dynamic 60–210 days | warning window fractures; partial delay/damage; failed pressure raises war support and preserves convergence pressure | one active flag and target generation; cancellation resolves success/partial/failure; no Hannibal name is used before reveal |
| Stop transformation: `cannibalism_stop_transformation_mission` | external responder; Wendigo counterwar; revealed Wendigo merge host and actor generation | pre-lock Wendigo host plus identify, assault, logistics, or recruitment-site counterwar receipts; dynamic 120–240 days | anchor chain broken or progress goal reached; partial counterwar result; failed window result | one active flag and target generation; all outcomes clear target, progress, goal, duration, and observer |

The unified operational missions `cannibalism_unified_command_mission`, `cannibalism_unified_larder_mission`, `cannibalism_unified_war_machine_mission`, and `cannibalism_unified_counterwar_mission` are action-receipt missions owned by the unified country, with 120, 150, 150, and 120-day base durations respectively, three-action goals, two-action partial thresholds, and explicit success/partial/failure cleanup.

The Wendigo terminal hunt mission is a 120-day success/failure mission with launch, press, defender cancellation, timeout, and target-lock cleanup, but it has no partial branch.

## Cost and requirement clarity

All six requested cost rows are icon-first and contain four or fewer non-zero spendable types after the concurrent fix.

The four newly wrapped affordability triggers now have one matching localisation key each, and the static scan found exactly one definition for each new key.

Logistics retains its existing `cannibalism_restore_supply_corridor_requirements_tt` wrapper, updated by the concurrent tranche to remove command capacity.

The six payment helpers still initialize shared zero fields for compatibility, but those fields are not gated, spent in a non-zero amount, or displayed.

The wider Event 014 cost surface still needs a separate four-type and icon-first pass, as listed under the severity findings.

## AI validity and route-lock notes

The six cost decisions retain AI weights and target arrays, and their target-root and target triggers reject invalid routes, dead or capitulated actors, already revealed convergence targets, non-blockaded Island Hosts, and reconstruction states outside the eligible recovery stage.

The Warlord, unified, and Wendigo recruitment decision families retain route, cap, state control, population, Larder, equipment, and cooldown gates.

The terminal ordinary route requires the unified country, terminal route flag, all operational packages, no existing world end, scenario enabled, Chaos strictly greater than 1000, Network Reach at least 92, controlled states above 35, consumed population at least 25,000K, and Larder at least 750.

The Wendigo terminal route requires the transformed Hannibal country, locked transformation, no existing world end, and Chaos strictly greater than 1000.

The `cannibalism_unified_world_end_category_is_visible` gate opens only during final mobilization or after the ordinary terminal world-end flag, and the terminal consume route does not expose a pre-reveal public Hannibal action.

No AI weight was changed in this pass, and no probability comparison is claimed because the named auditor route and current probability refresh were unavailable.

## Localisation and tooltip gaps

The four new requirement tooltips use registered texticons for all four spendable types and avoid a fifth hidden cost.

Every inspected six-contract decision has an effect tooltip, and the logistics decision has both requirements and effect tooltips.

Other Event 014 paid decisions still have direct scripted affordability triggers without named custom trigger tooltips, including Island Host blockade/rescue, aftermath identification/memorial, ritual actions, Warlord rows, and Wendigo rows.

No missing new localisation key, duplicate new key, or BOM issue was found; the audited Event 014 English localisation file begins with UTF-8 BOM bytes `239,187,191`.

## Cleanup and exploit-risk notes

`cannibalism_can_consume_current_state` requires the correct controller or consumption actor and rejects unusable Larder states, consumption cooldown, stabilization, liberated emergency, and all `cannibalism_recovery_active` stages.

`cannibalism_state_is_unusable_larder` rejects wasteland, Deaths-consumed states, nuclear fallout, severe chemical or biological contamination, irreversible air contamination, non-human owners outside the Wendigo route, insufficient population, and exhausted action counts.

`cannibalism_prepare_consumption_context` issues a unique request id, and `cannibalism_consume_current_state` rejects duplicate request ids before applying population loss.

Larder, consumed population, Deaths, cooldown, and action counters advance only after the exact state population loss is applied; blocked and duplicate requests do not yield Larder.

Warlord and unified recruitment consume the exact requested population before paying Larder and creating a zero-start formation, with caps, equipment reserves, route flags, and state recruitment cooldowns applied.

The source contains no `Prison Host` or equivalent fourth origin in the audited decision, trigger, effect, scripted-localisation, scripted-GUI, interface, or Event 014 localisation surfaces.

Liberated recovery registers the state once, advances through 90-day emergency, 180-day identification, 365-day institutional, and 1095-day long-trauma stages, and blocks consumption and recruitment until stabilization, for a 1730-day minimum staged recovery.

Global cleanup removes active Event 014 missions and clears target locks and terminal hunt runtime when the owning route completes; mission-specific clear helpers remove flags, targets, progress, duration, observers, and temporary burden modifiers.

## Meaningful validation run

- Static cost-contract check confirmed all six requested localisation rows contain icon tokens and four spendable rows or fewer.
- Static compatibility check found zero-valued `joint_trucks`, `convergence_trucks`, `landing_command`, `institution_trucks`, and `logistics_command` slots exactly where the shared payment helpers still initialize them.
- Static tooltip coverage check found all four new requirement wrappers and exactly one localisation definition for each new key.
- Static scan found no Prison Host token in the audited Event 014 decisions, triggers, effects, localisation, scripted-localisation, scripted-GUI, or interface files.
- Static pre-reveal scan found only the reveal-gated Hannibal achievement icon in decisions and the reveal-gated Wendigo country predicate in the scripted GUI.
- Static terminal scan confirmed strict `greater_than` comparisons against `constant:cannibalism_evolution_threshold.world_end_chaos` in both terminal completion triggers.
- Static consumption/recovery scan confirmed canonical unusable-state, recovery, duplicate-request, exact-loss, and staged recovery gates.
- `git diff --check` reported no whitespace error on the two gameplay/localisation files touched by this pass.

## Skipped or blocked meaningful validation

- Fresh five-window `hoi4.gui_inspect` did not produce a usable artifact because the service returned `ARTIFACT_STORAGE_LIMIT`; the early-window correct request is the recorded failure evidence.
- Fresh `hoi4.gui_render` timed out after 180 seconds, so no post-patch visual artifact or fidelity comparison is claimed.
- The named `chaosx_ai_probability_auditor` was not callable, the mission adapter produced no candidates, and both current decision refresh attempts timed out after 180 seconds.
- HOI4 was not launched because live gameplay validation belongs to the user.
- No broad legacy cost rewrite or mission-duration rebalance was applied because each would expand beyond the six requested contracts or require parent-owned probability comparison.

## Remaining issues and recommended fixes

1. Rerun the five decision-owned GUI inspect/render matrix when artifact storage and renderer timeouts are cleared, then verify visible action counts and long-text states.
2. Route the unchanged AI surfaces through `chaosx_ai_probability_auditor` and complete the same-scenario compare after any timing or AI-weight patch.
3. Decide whether to raise the two emergency mission timeout minima to the skill's 90-day floor.
4. Perform a separate four-type/icon-first audit for the remaining Event 014 cost rows outside the six requested contracts.
5. Centralize the Wendigo terminal-hunt 120-day constant when its owning timing tranche is next edited.
6. Add concise custom requirement tooltips to the remaining direct affordability triggers in a separate bounded localisation tranche.

## Simplifications, omissions, and blockers

No gameplay fallback or unapproved simplification was used.

The six requested cost changes were verified from concurrent worktree hunks rather than reauthored by this pass.

No broad category redesign, timing rebalance, legacy cost rewrite, GUI rewrite, AI-weight change, or live-game validation was claimed.

The exact GUI artifact-storage failure, GUI render timeout, named probability-auditor absence, mission-adapter empty pool, and current probability refresh timeout are the remaining evidence blockers.

No plan handoff was written because the unresolved items are bounded follow-up fixes rather than a new mechanic design.

## Skills used

- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-subagents`
