# Event 012 Africa Decision/Mission/GUI Hook Audit Handoff

Date: 2026-06-21
Role: Chaos Redux decision and mission audit subagent
Scope: Event 012 Africa decisions, missions, and scripted GUI decision hooks only.

## Changed Files

- `common/scripted_guis/012_africa_scripted_gui.txt`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_decision_mission_gui_hook_audit_handoff.md`

No Event 010 files or `events/070_africa_gods.txt` were edited.

## Patched IDs

- Scripted GUI: `africa_continental_congress_scripted_gui`
- GUI button effect: `africa_gui_sponsor_readiness_button_click`
- Shared helper preserved as cost owner: `africa_start_continent_sponsor_readiness_mission`
- Related decision path audited: `africa_prepare_continent_sponsor_mission`
- Related mission audited: `africa_continent_sponsor_readiness_mission`
- Localisation keys audited but not changed:
  - `africa_gui_sponsor_readiness_button_tt`
  - `africa_prepare_continent_sponsor_mission_cost_tt`
  - `africa_prepare_continent_sponsor_mission_effect_tt`

## Before And After Behavior

Before: the GUI Sponsor button spent `constant:africa_decision.sponsor_mission_cost_spend`, then called `africa_start_continent_sponsor_readiness_mission`, which also spends the same political power cost together with convoys, support equipment, and command power. Human GUI use paid the PP cost twice; the normal decision path paid it once.

After: the GUI Sponsor button calls the shared helper only. GUI and normal decision paths now share one cost owner and spend the same PP, convoy, support equipment, and command power package.

## Severity-Sorted Issue List

| Severity | Finding | Evidence | Status |
| --- | --- | --- | --- |
| High | GUI Sponsor button charged political power twice compared with the normal decision path. | `common/scripted_guis/012_africa_scripted_gui.txt` button effect called `add_political_power` before `africa_start_continent_sponsor_readiness_mission`; the helper already spends PP at `common/scripted_effects/012_africa_effects.txt`. | Patched. |
| High | Event 012 decision completion remains blocked by live scenario and exploit proof, not by missing static decision families. | Prior static matrix and completion follow-up still require live validation for ordinary unifier, fragile unifier, RSA branch, ally under attack, high-chaos, full unification, cross-continent union, and World Is One. | Report only; out of patch scope. |
| Medium | Several high-chaos targeted decisions use raw `target_trigger = { FROM = { ... } }` without a custom target tooltip. | Examples include `africa_issue_bestiary_warning_to_holder`, `africa_issue_bestiary_warning_to_state_holder`, `africa_bind_bestiary_actor_to_charter`, and many Bestiary actor actions. | Report only; broad localisation/tooltip pass recommended. |
| Medium | Continental Congress GUI is functional and has costs, effects, trigger checks, and AI-equivalent decision paths, but still lacks live render/readability proof. | GUI has fixed text cards/buttons and static/animated visibility hooks; prior completion audit still marks live GUI proof as missing. | Report only; requires runtime validation. |
| Low | Mission durations are varied and most mission cleanup exists, but duplicate-risk proof is static only. | Mission families range from 90 to 420 days and generally use success/failure helpers; exploit proof for retries, counters, and selected contexts still needs live or scenario-pressure validation. | Report only. |

## Decision Category Lifecycle Notes

- `africa_continental_congress_category`: visible from `africa_decision_layer_visible`, owns the scripted GUI, displays core values, and exposes the Sponsor GUI hook after route gates.
- `africa_charter_league_diplomacy_category`: target-array driven Charter, aid, authority, and regional package actions. It has active caps for confidence/corridor/mandate missions and same-tick `available` revalidation for the ten regional package decisions.
- `africa_liberation_war_office_category`: uses prep decisions, state-targeted liberation objectives, and a deadline mission; objective cleanup resets secured state progress on cancel/success/failure.
- `africa_regional_integration_category`: state-targeted paper-core survey, living-core conversion, rail-belt operations, and integration temperature review; broader live exploit proof remains needed for core-spam safety.
- `africa_authority_atlas_category`: uses selected dossier context, three case slots, old-seat arbitration, archive guard, direct seal, forgery/museum crisis, and resistance watch contexts. Cleanup helpers are present, but live retry/counter proof remains a blocker.
- `africa_high_chaos_category`: high-chaos package unlocks, warnings, habitat seats, actor/package operations, and containment mission. Route gates exist; tooltip clarity on raw target triggers remains the main static readability gap.
- `africa_continent_sponsor_category`: sponsor readiness mission now has GUI/decision cost parity through shared helper ownership.
- `africa_rsa_civil_war_emergency_category`: objective decisions and Pretoria mission use concrete state objectives and costs; live RSA branch proof remains required.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_origin_mandate_case_mission` | Unifier | Congress | Origin profile | Profile-specific value gates and capital control | 120 | Origin mandate success helper | Origin mandate failure helper | Low |
| `africa_member_confidence_mission` | Unifier | Charter diplomacy | Active member/protected target | Target survives, remains in Charter relation, and ends war | 120 | Cohesion/trust gain and target kept flag | Alarm/cohesion penalty and broken flag | Low |
| `africa_aid_corridor_mission` | Unifier | Charter diplomacy | Active aid target | Target survives and war resolves after corridor commitment | 150 | Cohesion/trust gain | Alarm/cohesion penalty | Low |
| `africa_regional_authority_mandate_mission` | Unifier | Charter diplomacy | Active authority target | Target completes regional mandate checks | 150 | Mandate success profile helper | Mandate failure helper | Low |
| `africa_liberation_front_deadline_mission` | Unifier | Liberation office | African front states | Border columns, rail belt, and required secured front states while at war | 180 | Momentum/authority progress and cleanup | Alarm/cohesion failure and cleanup | Medium; live objective-reset proof still needed |
| `africa_regional_integration_deadline_mission` | Unifier | Regional integration | Paper-core regions | Active integration state/counter requirements | 300 | Integration progress and value gains | Burden/alarm/trust penalties | Medium; core conversion route needs live proof |
| Dossier slot missions | Unifier | Authority Atlas | Selected old-seat dossier | Case-specific site/route/hearing checks | 100-120 | Case success helper | Case failure helper | Medium; three-slot retry proof remains needed |
| `africa_dossier_resistance_watch_mission` | Unifier | Authority Atlas | Stored resistance seat | Mediation/enforcement context and seat control | 150 | Watch completion helper | Watch failure helper | Medium; stored-context proof still live-only |
| `africa_bestiary_containment_deadline_mission` | Unifier | High-chaos | High-chaos actors | Habitat terms, omen reliability, bound actors, habitat seats, and package actions | 420 | Habitat/nonhuman/covenant stabilization | Alarm/volatility/cohesion/covenant pressure | Medium; route-stress proof needed |
| `africa_continent_sponsor_readiness_mission` | Unifier | Continental sponsorship | Post-unification Africa | Africa Is One, register, dossier coverage, authorities, package actions, living cores | 180 | Sponsor ready and super-event | Alarm/debt penalties | Low after GUI cost parity patch |
| `africa_rsa_pretoria_deadline_mission` | RSA continental side | RSA emergency | South Africa | Mine-port belt, negotiators, settlement, victory, Allied peace, objective states | 120 | Momentum/legitimacy gain | Momentum loss, alarm, war support penalty | Medium; live RSA proof required |

## Cost And Requirement Clarity Notes

- The layer is not a political-power store. Most costed decisions use custom costs with equipment, manpower, convoys, trains, command power, XP, selected seat control, target state control, or mechanic values.
- The patched GUI Sponsor hook now matches its tooltip and decision cost path: PP, convoys, support equipment, and command power are all spent exactly once through the helper.
- Many major cost keys have icon-first text and `_tooltip` detail keys. The largest remaining clarity gap is target requirements on raw high-chaos `target_trigger` blocks, not the custom cost text.

## AI Validity And Route-Lock Notes

- AI weights exist on the audited decision families and route-locks are generally present through focus flags, route flags, evolution/high-chaos gates, target tags, and active mission flags.
- The scripted GUI itself remains `ai_enabled = { always = no }`, but every GUI button audited maps to existing decision/helper paths that AI can use through normal decisions or scripted effects.
- Static target validity is strong for regional package actions and sponsor gates. Live validation remains needed for stale target arrays after annexation, capitulation, member exit, and scenario setup.

## Localisation And Tooltip Gaps

- No localisation key was changed by the patch.
- Existing sponsor tooltip remains accurate after the patch because the same cost is still paid once.
- Recommended bounded follow-up: add custom target tooltips for the high-chaos holder/state/actor target triggers so players see named availability reasons instead of raw trigger blocks.

## Cleanup And Exploit-Risk Notes

- The patched Sponsor GUI path no longer creates an asymmetric human-only cost penalty.
- Major cleanup helpers are present for active targets and missions: member confidence, aid corridor, regional mandate, liberation objectives, dossier cases, resistance watches, old-seat arbitration, archive guard, and runtime context cleanup.
- Remaining exploit checks need scenario pressure rather than more static reading: living-core conversion, dossier case retries, resistance watch settlement loops, Bestiary warning/action repetition, sponsor proof repetition, and RSA settlement sequencing.

## Validation

- Confirmed `africa_start_continent_sponsor_readiness_mission` is the only remaining `sponsor_mission_cost_spend` owner after the patch.
- Confirmed both call sites, `africa_prepare_continent_sponsor_mission` and `africa_gui_sponsor_readiness_button_click`, route through the shared helper.
- Reviewed diff scope: only `common/scripted_guis/012_africa_scripted_gui.txt` changed among gameplay files in this audit.

## Skipped Meaningful Validation

- No HOI4 runtime validation was run. The remaining high-confidence blockers require live/manual scenario proof, not static syntax inspection.
- No broad tooltip patch was made for every high-chaos target trigger because that is a larger localisation/target-surface pass outside the small local GUI cost fix.

## Concrete Recommended Fixes

1. Run the Event 012 live scenario validation matrix and record pass/fail evidence for decision/mission surfaces, especially GUI clicks, RSA branch, high-chaos package stress, living-core conversion, sponsor proofs, and World Is One gate sequencing.
2. Add a bounded tooltip pass for high-chaos targeted decisions in `common/decisions/012_africa_decisions.txt`, with matching keys in `localisation/english/012_african_union_l_english.yml`.
3. Validate stale target cleanup after member exit, target annexation, target capitulation, integration completion, and world-end transition.
4. Keep Event 012 spreadsheet/catalog status as not final until scenario and exploit proof exists.

No broad plan handoff was written. The remaining work is validation plus bounded tooltip cleanup, not a new decision system.
