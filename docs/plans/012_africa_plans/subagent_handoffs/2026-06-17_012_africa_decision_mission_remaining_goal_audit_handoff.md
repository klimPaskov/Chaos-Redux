# Event 012 Africa Decision/Mission Remaining Goal Audit Handoff

Date: 2026-06-17
Agent role: Chaos Redux decision and mission subagent

## Scope

Audited Event 012 Africa decisions and missions for the remaining active-gameplay requirements: varied non-PP costs, map objectives, active caps, target selection, cleanup, dynamic localisation, AI equivalents, and exploit protection.

Required references consulted before editing:

- `AGENTS.md`
- `hoi4-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`
- Offline wiki snapshot: Decision modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Idea modding, AI modding
- Vanilla docs/examples: `~/projects/Hearts of Iron IV/common/decisions/_documentation.md`, `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`, and vanilla `ETH.txt`, `foreign_influence.txt`, African Union category examples

No web was used. No focus, country package, asset, achievement, spreadsheet, or super-event files were edited.

## Files Changed

- `common/decisions/012_africa_decisions.txt`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_decision_mission_remaining_goal_audit_handoff.md`

## Changed IDs

Decision:

- `africa_press_scramble_treaty_settlement`

Localisation referenced but not changed:

- `africa_press_scramble_treaty_settlement_cost_tt`
- `africa_press_scramble_treaty_settlement_cost_tt_blocked`
- `africa_press_scramble_treaty_settlement_cost_tt_tooltip`

## Patch Behavior

Before:

- `africa_press_scramble_treaty_settlement` put its convoy, support-equipment, manpower, and command-power gates inside `available`, while also using `custom_cost_text`.
- The visible custom cost line could not reliably switch through the intended custom cost trigger path, even though matching base, blocked, and tooltip localisation existed.

After:

- The same non-PP resource gates are now inside `custom_cost_trigger`.
- The decision still targets registered outside holders, still consumes the same resources in `complete_effect`, still marks the holder settled, and still refreshes the external-holder pool.
- The blocked and satisfied cost text now follows HOI4 custom cost structure.

## Issue List Sorted By Severity

High:

- Broad `state_target = africa` presentation remains a design gap. Current state-target families are active and resource-gated, but several can still expose a large map/list at once: liberation objectives, paper-claim surveys, living cores, integration rail belts, return settlements, habitat seats, state-holder warnings, and some Bestiary state operations. This needs a selected-region or active-target-cap pass, not a silent local patch.
- The decision file still mixes regular `cost = constant:...` with `custom_cost_trigger/custom_cost_text` across many decisions. Existing localisation often includes PP in the custom text while the script also uses regular PP cost. Because vanilla documentation warns that custom costs do not replace real resource subtraction and should not be mixed casually with regular cost, this needs a parent-owned cost-model decision across the whole Event 012 surface.

Medium:

- Several post-unification sponsor and proof decisions have strong resource costs and route locks, but are still mostly single-click certification actions rather than missions with failure states. The sponsor readiness mission is real; the later continent-charter and external-proof actions are gated proofs without their own timed risk.
- Some Bestiary actor operations are one-time and resource-gated, but reward the target with equipment, manpower, construction, or units immediately. One-time flags prevent obvious loops, but these are still reward-heavy action buttons rather than multi-step local operations with failure/disaster consequences.
- Liberation objectives are no longer passive and have retry cleanup, but the target trigger still allows broad loyal Charter or rear-area controlled states. This is better than a PP store, but weaker than named front corridors.
- AI weights exist for almost every decision, but many remain flat `normal/preferred/strong` route weights. They do not yet score current equipment surplus, local war pressure, target strategic value, or crisis severity in detail.

Low:

- Category and GUI value localisation is mostly current and dynamic, including Covenant Pressure, Aid Corridor status, Archive Seal status, Omen Review, Sponsor readiness, dossier names, and selected Bestiary package names. Remaining text issues are mostly depth/readability rather than missing keys.
- True timed mission durations are varied and file-scoped. They are not mirrored into script constants, but the file-scoped constants are appropriate for `days_mission_timeout` compatibility.

## Decision Category Lifecycle Notes

- `africa_continental_congress_category` is the main visible value and GUI entry category after `africa_decision_layer_visible`.
- `africa_charter_league_diplomacy_category` handles Charter invitations, aid, aid corridors, member confidence, votes, court cases, and integration docketing. It has one-active-target caps for confidence/corridor missions through global event targets and active flags.
- `africa_liberation_war_office_category` contains operation prep, columns, rail offices, front objectives, Scramble case refresh, treaty settlements, and the Scramble treaty mission. The patched settlement cost now follows custom-cost UI behavior.
- `africa_regional_integration_category` remains the main broad state-target area. It uses state flags and counters for paper cores, living cores, and rail regions, but still needs selected-region presentation.
- `africa_diaspora_return_category` now exists and has varied convoy, support equipment, manpower, officer-school, and state-settlement actions.
- `africa_authority_atlas_category` has selected-dossier survey, office, guard, settlement, direct Archive seal, and archive guard missions with per-selected-dossier helpers.
- `africa_high_chaos_category` has package unlocks, habitat seats, omen review, warnings, actor binding, actor package actions, and containment mission. Lifecycle is one-time flag heavy and mostly protected from repeat loops.
- `africa_continent_sponsor_category` has a real sponsor readiness mission, then later sponsor/proof/certification actions.
- `africa_rsa_civil_war_emergency_category` is route-gated by the active RSA civil war flag. The previous RSA patch already closed the repeated mine-port and negotiator loops.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_member_confidence_mission` | Africa unifier | Charter League Diplomacy | One aided Charter-side country | Target remains alive, uncapitulated, in the Charter relationship, and finishes war | 120 days | Cohesion and Regional Trust | Colonial Alarm up, Cohesion down | Low; active target flag and event target are cleared |
| `africa_aid_corridor_mission` | Africa unifier | Charter League Diplomacy | One aided Charter-side war target | Target survives, remains linked to Charter, and finishes war | 150 days | Cohesion and Regional Trust | Colonial Alarm up, Cohesion down | Low; one active corridor cap and target cleanup exist |
| `africa_liberation_front_deadline_mission` | Africa unifier | Liberation War Office | Broad African front states | Border columns, rail belt, required secured front states, active war | 180 days | Momentum and Cohesion | Alarm up, Cohesion down | Low exploit risk after cleanup; medium target-breadth risk |
| `africa_scramble_treaty_deadline_mission` | Africa unifier | Liberation War Office | Registered outside holders | All holders settled and capital controlled | 240 days | Legitimacy, Cohesion, Alarm relief | Alarm up, Cohesion down | Low; holder flags and pool refresh exist |
| `africa_regional_integration_deadline_mission` | Africa unifier | Regional Integration | Continental integration counters | Living cores, regional authorities, rail regions | 300 days | Trust, Authority, burden relief | Trust down, burden/alarm up | Low duplicate risk; medium abstraction risk |
| `africa_selected_dossier_survey_mission` | Africa unifier | Authority Atlas | Selected old-seat dossier | Selected dossier seat remains controlled/protected | 120 days | Opens/surveys dossier and starts archive guard work | Restoration Debt and Local Sovereignty pressure | Low; selected survey active flag clears |
| `africa_direct_archive_seal_mission` | Africa unifier | Authority Atlas | Direct Archive seal proof | Legitimacy, old-seat legitimacy, restoration debt thresholds | 120 days | Authority and old-seat legitimacy | Counterfeit crisis, alarm/debt rise | Low; active/success/failure flags clear |
| `africa_archive_guard_deadline_mission` | Africa unifier | Authority Atlas | Dossier guard network | Dossier work ready and required secured seats | 180 days | Archive Mandate and old-seat legitimacy | Restoration debt and local sovereignty pressure | Low; archive guard context helper clears |
| `africa_omen_reliability_review_mission` | Africa unifier | High-Chaos Reports | Bestiary omen review | Habitat trust above gate; alarm and volatility below caps | 120 days | Omen reliability verified | Alarm, volatility, covenant pressure rise | Low; active/success/failure flags clear |
| `africa_bestiary_containment_deadline_mission` | Africa unifier | High-Chaos Reports | Bestiary network | Habitat terms, omen reliability, habitat seats/actions/bound actor | 420 days | Trust, nonhuman sovereignty, volatility relief | Alarm, volatility, Cohesion damage | Low duplicate risk; medium broad-system abstraction |
| `africa_continent_sponsor_readiness_mission` | Africa unifier | Continent Sponsor | Africa-wide sponsor readiness | Register, World Root mandate, dossiers, packages, authorities, living cores | 180 days | Sponsor ready and super-event surface | Alarm and restoration debt | Low; active/success/failure flags clear |
| `africa_rsa_pretoria_deadline_mission` | RSA continental side | RSA Civil-War Emergency | Transvaal/Cape/Natal belt | Mine-port belt, negotiators, settlement, continental victory, Allied peace, state control | 120 days | Momentum and legitimacy | Momentum/war support down, alarm up | Low after prior RSA loop patch |

## Cost And Requirement Clarity Notes

- Event 012 is no longer a passive PP store. The audited surface uses infantry equipment, support equipment, convoys, trains, manpower, command power, army XP, state control, target countries, one-active mission flags, dossier variables, and map targets.
- The patched Scramble settlement now uses custom cost trigger semantics for its non-PP resources.
- All `custom_cost_text` ids currently referenced by `common/decisions/012_africa_decisions.txt` have base, `_blocked`, and `_tooltip` localisation entries in `localisation/english/012_african_union_l_english.yml`.
- Remaining uncertainty: the regular PP `cost = constant:...` plus custom cost pattern is widespread. I did not rewrite it because doing so safely requires deciding whether every custom-cost decision should subtract PP manually, use `ai_hint_pp_cost`, or keep the current pattern based on verified engine behavior.

## AI Validity And Route-Lock Notes

- Targeted country decisions generally use target arrays plus route/flag checks: Charter candidates/members/protected members, external colonial holders, and high-chaos actor tags.
- State-target decisions use scripted triggers that require African states, control/ownership, integration flags, high-chaos seat constants, or external-holder state conditions.
- Dead-target risk appears low for country targets because default targeted decisions do not target non-existing countries and the relevant `target_trigger` blocks often include `exists = yes` or exact tag/high-chaos flags.
- Route locks are present for Charter mandate, General Staff, courts, liberation offices, integrated regions, Authority Atlas, Bestiary, sponsor office, RSA branch, and World Is One proof gates.
- Remaining AI gap is quality, not basic validity: AI weights need deeper modifiers for current resource position, active wars, overextension, target strength, and crisis pressure.

## Localisation And Tooltip Gaps

- No missing custom cost localisation keys were found.
- The main category descriptions and GUI strings expose dynamic values and statuses for Legitimacy, Authority, Cohesion, Trust, Liberation, Alarm, Paper Burden, Covenant, dossier selection, Bestiary case, aid corridor, Archive seal, Omen review, and sponsor readiness.
- Remaining gap: the broad state-target families still rely on generic regional/state wording. Named corridor/local objective text would need a selected-region design pass.

## Cleanup And Exploit-Risk Notes

- Aid corridor and member confidence missions clear their target flags and global event targets on cancel, success, and timeout.
- Liberation front objective progress is cleared on cancel, success, and timeout through `africa_clear_liberation_objective_progress`.
- Authority Atlas and archive guard missions use cleanup helpers for selected-dossier and guard context.
- One-time flags block repeated federal votes, autonomy statutes, court cases, dossier guards, high-chaos package actions, actor tasks, RSA mine-port proof, and RSA negotiator pressure.
- Remaining exploit risk is mostly balance-depth: reward-heavy Bestiary actor actions and broad state-target integration could still feel farmable if the resource costs are not enough in late game.

## Concrete Recommended Fixes

1. Decide the Event 012 custom cost model in `common/decisions/012_africa_decisions.txt`: either keep verified regular PP plus custom costs, or move PP into custom costs with explicit PP subtraction and `ai_hint_pp_cost` where needed.
2. Add selected-region or active-target presentation for broad `state_target = africa` families rather than exposing every eligible state.
3. Upgrade liberation objectives from broad eligible states to named or selected front corridors with rail/port/capital hooks.
4. Convert later cross-continent sponsor/proof actions into timed or target-driven objectives when external continent systems exist.
5. Deepen AI weights around equipment surplus, active war, target strength, alarm/volatility pressure, and route priorities.
6. Add package-specific Bestiary incident/failure chains if the actor operations are meant to match the older package depth.

## Validation Run

- Inspected the patched Scramble settlement block and verified `custom_cost_trigger` now wraps the same convoy, support-equipment, manpower, and command-power gates that the cost text describes.
- Verified every `custom_cost_text` id referenced by `common/decisions/012_africa_decisions.txt` has matching base, `_blocked`, and `_tooltip` localisation entries.
- Checked brace balance for `common/decisions/012_africa_decisions.txt` after the patch.
- Reviewed the actual `has_africa_authority_atlas_registered` trigger after a suspicious output fragment; the file already has valid `var/value/compare` checks for both historical dossier and high-chaos package catalog counters.

## Skipped Meaningful Validation

- No game-load validation was run.
- I did not run a full parser against all Event 012 script files.
- I did not touch scripted GUI costs or focus integration because the requested scope was decisions/missions and the only clear safe patch was in the decision file.

## Simplifications, Omissions, And Blockers

- No broad redesign was attempted.
- The broad custom-cost model, state-target cap, route-aware AI depth, and sponsor/Bestiary mission-depth gaps remain unresolved by design and should be handled by the parent or a dedicated plan pass.
- No fallback implementation was used.
