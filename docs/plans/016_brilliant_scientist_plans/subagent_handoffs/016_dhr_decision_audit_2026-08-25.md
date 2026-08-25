# Event 016 D’Rhondan and Portal decision/mission audit

Date: 2026-08-25

Owner: dhr_decision_audit

Scope: Alien Infantry landing, D’Rhondan contact and country decisions, Kruger and Mengele expedition missions, rebellion pulse mission, native Portal Warfare raids, D’Rhondan decision categories, and the Kruger Directorate decision-category scripted GUI/header surface.

Authority: AGENTS.md; .agents/skills/chaos-redux-decisions-missions/SKILL.md; .agents/skills/chaos-redux-events/SKILL.md; .agents/skills/chaos-redux-subagents/SKILL.md; the accepted Alien Infantry/D’Rhondan addendum and acceptance scenarios; offline Paradox wiki pages; installed vanilla documentation and precedents.

## Disposition

The audited decision and mission surfaces have no newly found P0 or P1 gameplay defect.

One narrow P2 localisation defect was fixed in localisation/english/016_dhrondan_contact_l_english.yml:29.

No decision, mission, raid, trigger, effect, category, scripted-GUI, or interface source was changed.

The remaining items are bounded audit risks and MCP evidence blockers, not silent substitutions for gameplay validation.

## Changes applied

dhrondan_rebellion_pulse_mission_desc previously described the 10% branch as “six or seven arrivals with Chaos 600–799,” which did not match the source gate because the base tier applies at six or more arrivals with Pact Strain at least 30 and Chaos at least 600 whenever the higher tier is inactive.

The tooltip now states the active base gate, the 20% alternatives, and the 40% high tier, including higher-tier precedence.

Before: “Six or seven arrivals with Chaos 600–799.”

After: “At least six arrivals, Pact Strain 30+, and Chaos 600+ when neither higher tier applies.”

The localisation file remains UTF-8 with BOM, verified as EF BB BF.

## Severity-sorted findings

### P2 fixed: rebellion pulse tooltip did not describe the actual low tier

Sources: common/scripted_triggers/016_dhrondan_contact_triggers.txt:141-196; common/scripted_effects/016_dhrondan_contact_effects.txt:345-367; localisation/english/016_dhrondan_contact_l_english.yml:29.

The gate requires the pact, at least six arrivals, Pact Strain at least 30, Chaos at least 600, and no world end.

The resolver selects 40% first, then 20%, then the 10% base weight, so the revised text explicitly says when the base tier applies.

### P2 remaining: Portal raid persistent beachhead and extraction flags have no bounded cleanup consumer in this surface

Sources: common/scripted_effects/016_brilliant_scientist_raid_effects.txt:53-105,270-340.

brilliant_scientist_portal_beachhead_active, brilliant_scientist_portal_raid_breach_recorded, brilliant_scientist_portal_raid_targeted, brilliant_scientist_portal_facility_extracted, and brilliant_scientist_portal_factory_extracted are persistent history/state markers in the current effects, but this audit found no expiry or containment consumer that clears the state markers.

This is not an immediate duplication exploit because successful and critical raid outcomes use destroy_unit = yes and the extraction resolver transfers only one building per call.

Recommendation: the owner of the later portal-beachhead/containment lifecycle should define an explicit clear or terminal-state policy before adding more raid aftermath content.

No broad cleanup system was added here.

### P2 remaining: native Portal Raider requirement has a minimum but no maximum

Sources: common/raids/016_brilliant_scientist_portal_raids.txt:141-147,373-379 and common/units/016_brilliant_scientist_project_forces.txt.

Both raid types require portal_raider = { min = 6 }, while the locked Quantum Transit Raiders template contains exactly six battalions.

The accepted design uses the locked six-battalion template, but a different formation with more than six qualifying battalions may pass the native minimum if the engine permits it.

Recommendation: confirm the native raid engine’s formation-size contract in a live save or add an explicit bounded-template check through the owning raid design.

No raid source change was made because the available native schema does not expose a proven maximum field in this audit.

### P3 remaining: some D’Rhondan decision blockers are helper triggers without a dedicated reason tooltip

Sources: common/decisions/016_dhrondan_contact_decisions.txt:24-43,54-74,79-99 and common/decisions/016_dhrondan_country_decisions.txt:23-64,79-142,158-165.

Fuel, state-target, and compact-target requirements have custom tooltips, but route and lifecycle helpers also cover character health, obligation, transaction locks, active war, and world-end invalidation without a separate player-facing explanation for every failed branch.

The current decision descriptions explain the normal route, cost, duration, and outcome, and the source does not expose a raw scripted block as authored localisation.

Recommendation: if a GUI capture shows an unhelpful generic blocked row, add concise custom trigger tooltips for the route/lifecycle gates rather than exposing helper trigger bodies.

This remains a recommendation because GUI inspect failed before returning a decision-row state.

### P3 remaining: exact-facility Portal destination gating is conservative

Sources: common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt:72-107 and common/scripted_effects/016_brilliant_scientist_raid_effects.txt:98-263.

For facility extraction, availability requires an actor-controlled destination state with all four special-facility families below one, even when only one family is being transferred.

This prevents invalid reconstruction but can hide a valid raid when a family-specific destination exists beside another special facility.

Recommendation: treat this as a balance/usability decision for the raid owner, not as an unreviewed broadening patch.

### Tooling blocker: no custom probability auditor route is callable in this runtime

ALL_TOOLS contained no chaosx_ai_probability_auditor callable, so the required named auditor could not be spawned or routed.

The direct hoi4_probability_inspect route was used for every weighted source that the installed MCP could index, and the missing custom-auditor capability is recorded here rather than treated as complete balance evidence.

## Decision category and lifecycle notes

alien_infantry_landing_category in common/decisions/categories/016_alien_infantry_landing_category.txt:8-14 is visible only with a positive contact receipt and contains one state-targeted primary action plus its hidden timed mission.

alien_infantry_call_landing in common/decisions/016_alien_infantry_landing_decisions.txt:10-59 revalidates a passable state owned and controlled by the calling country, reserves exactly 2,000 alien_laser_weapon_equipment_1, blocks a second pending landing, and starts the seven-day alien_infantry_landing_mission.

alien_infantry_landing_mission in common/decisions/016_alien_infantry_landing_decisions.txt:61-75 cancels through alien_infantry_cancel_landing_reservation when contact, control, ownership, passability, selected state, or world-end validity is lost, refunding exactly 2,000 once.

Successful timeout delegates to alien_infantry_spawn_landing_cohort in common/scripted_effects/016_alien_infantry_api_effects.txt:298-491, which creates one locked, non-recruitable ten-battalion cohort, marks the state, records Presence and Strain, and applies the 30/24/18/12-day cooldown ladder.

dhrondan_contact_category in common/decisions/categories/016_dhrondan_contact_category.txt:8-19 exposes the craft, pact, and active expedition stages without a separate custom decision window.

dhrondan_contact_status_header in common/decisions/016_dhrondan_contact_decisions.txt:10-15 is a compact unavailable status row, not an action.

The Kruger and Mengele decisions in common/decisions/016_dhrondan_contact_decisions.txt:17-75 each pay 50 political power through the native decision cost, consume 500 fuel in the route-specific begin effect, remove themselves after one day, and start exactly one 180-day route mission.

dhrondan_kruger_expedition_mission and dhrondan_mengele_expedition_mission in common/decisions/016_dhrondan_contact_decisions.txt:102-134 are hidden activated missions with dynamic duration from var:dhrondan_expedition_days.

Their cancellation and timeout paths revalidate the route, call failure cleanup when invalid, and open the audience event only when the route remains valid.

dhrondan_rebellion_pulse_mission in common/decisions/016_dhrondan_contact_decisions.txt:136-144 is a country-scoped 90-day mission with no spendable cost, a single active-mission guard, cancellation below the pact/arrival/Strain/Chaos gate, and a random-list resolver that reactivates only while the gate remains valid.

dhrondan_sovereignty_category in common/decisions/categories/016_dhrondan_country_categories.txt:8-16 owns four primary decision types in common/decisions/016_dhrondan_country_decisions.txt:10-178.

The reclamation, enclave supply, and integration decisions are state-targeted and revalidate their state at completion.

The Two-World Compact is country-targeted, requires a valid independent partner, persists one offer target, and delegates response cleanup to the existing Event 016 compact chain.

## Cognitive-load notes

The landing category shows one primary action and one active mission at a time.

The contact category presents at most two route actions before a pact, or one status row plus Honor Accord after a pact; envoy missions and the rebellion pulse are active progress rows rather than extra decision buttons.

The sovereignty category has four decision types, below the six-action ceiling, although state-targeted rows can repeat for multiple eligible states and should remain gated by the accepted route phase.

The native Portal Warfare category has two raid types, separating state installations from exact provincial facilities.

The only persistent contact values displayed in the D’Rhondan header are Alien Presence and Pact Strain.

The header description explains that successful landings increase both values and that high arrivals combined with world chaos can produce a rebellion response.

The revised pulse mission text gives the cause, threshold, consequence, and higher-tier precedence for each displayed revolt weight.

Landing cost, expedition cost, duration, cooldown, and state-control response are displayed through concise descriptions and custom tooltips, with requirements kept separate from consumed costs.

No raw wall of dynamic numbers or more than six simultaneous primary actions was found in the audited decision surfaces.

## Mission quality matrix

| Mission | Owner/category | Region/target | Requirement | Duration | Success | Failure/cancel | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alien_infantry_landing_mission | Alien Infantry API / alien_infantry_landing_category | One saved controlled host state | Positive contact, one pending flag, valid state, 2,000 reserve | 7 days | One locked landing cohort, state/history marker, Presence +1, Strain +5, cooldown | Invalid contact/control/state/world end refunds 2,000 and clears the mission | Pending flag and clear-before-refund cleanup make cancellation repeat-safe |
| dhrondan_kruger_expedition_mission | D’Rhondan contact / dhrondan_contact_category | Country-scoped expedition | Current Kruger host, completed craft, canonical active Kruger, no injury/confined/obligation/pact, 50 PP and 500 fuel | 180 days | Valid audience, pact receipt, one-time Directorate return deltas, canonical role restoration | Character/host/world invalidation fails with no pact reward and common cleanup | Shared expedition flag, character obligation, and reward receipts prevent overlap/reaward |
| dhrondan_mengele_expedition_mission | D’Rhondan contact / dhrondan_contact_category | Country-scoped expedition | Valid Mengele route, completed craft, no pact/other expedition, 50 PP and 500 fuel | 180 days | Valid audience and Mengele-only contact receipt | Invalid route/world end fails with no Kruger variable mutation | Separate Mengele route and receipt flags plus shared expedition lock prevent overlap/reaward |
| dhrondan_rebellion_pulse_mission | D’Rhondan contact / dhrondan_contact_category | Country-scoped pact host | Pact, at least 6 arrivals, Strain at least 30, Chaos at least 600, no world end | 90 days | 10/20/40% tiered random-list resolution and one rebellion bridge attempt | Gate loss removes the mission; no revolt reactivates only while eligible | has_active_mission guard and dhrondan_rebellion_triggered stop duplicate pulses |

Portal Warfare surfaces are native raids rather than scripted missions, so preparation, reservation, cancellation, expiry, outcome selection, cooldown, and raid history remain engine-owned.

## Cost and requirement clarity

| Surface | Spendable cost types | Cost evidence and icon coverage |
| --- | ---: | --- |
| alien_infantry_call_landing | 1 | Exactly 2,000 alien_laser_weapon_equipment_1; custom cost and effect text use the alien laser equipment texticon. |
| Kruger expedition | 2 | Exactly 50 PP through cost plus 500 fuel in the begin effect; localisation uses the political-power and fuel texticons. |
| Mengele expedition | 2 | Same 50 PP plus 500 fuel contract; localisation uses the political-power and fuel texticons. |
| dhrondan_honor_accord | 1 | Exactly 75 PP through cost; localisation uses the political-power texticon. |
| DHR sovereignty decisions | 1 each | Each decision has one political-power cost constant; state ownership, war, infrastructure, claims, and partner checks are non-consumed requirements. |
| Portal state/facility raids | 2 | Native 10 Command Power plus 60 teleportation_equipment; the raid engine owns command/equipment reservation presentation. |

No audited gameplay-changing action exceeds the four-spendable-type ceiling.

No fifth cost is hidden in a confirmation window, scripted effect, or secondary panel in the inspected decision paths.

Non-consumed requirements remain separate from costs, including contact receipts, project completion, character state, target ownership/control, wars, cooldown flags, arrival/Strain/Chaos thresholds, and world-end safety.

## AI validity and route-lock notes

alien_infantry_call_landing has a base AI score plus DHR network, reserve-priority, guarded-descent, and near-space factors, while root and target gates still require equipment and a valid controlled state.

Kruger and Mengele route decisions use the dominant contact AI score, but their begin effects revalidate the route and fuel before fuel debit and mission activation.

The Event .40 AI helper pays the exact 50 PP and 500 fuel contract, prefers Kruger when both route gates are valid, and falls back to Mengele.

Honor Accord uses a low base score with a strain-high factor and remains unavailable without pact, positive Strain, no cooldown, no rebellion, and no world end.

DHR sovereignty decisions use route-sensitive standard, urgent, or preferred weights and revalidate the target state or partner at resolution.

Both Portal raid types zero their AI weight when actor readiness or target validity fails, then apply Kruger, major-target, capital, and facility preferences.

The raid source has two native ai_will_do blocks, but the installed probability adapter reported no weighted candidates for the raid source, so no raid selection probability is asserted.

No invalid dead-country target, impossible border, closed expedition route, or target-state scope mismatch was found in the inspected triggers.

## Localisation and tooltip gaps

The D’Rhondan header localisation is compact and meaningful: dhrondan_contact_status_header shows Presence and Strain, while its description explains their source and rebellion consequence.

Kruger and Mengele descriptions state the 180-day duration, 50 PP and 500 fuel cost, and the route-specific Directorate consequence.

Landing text uses the equipment texticon, explains the seven-day reservation, exact refund condition, successful Presence/Strain changes, and cooldown ladder.

State-targeted DHR country rows and Portal raids use custom target requirement tooltips.

The fixed pulse tooltip is the only localisation edit in this handoff.

The remaining route-helper reason tooltip recommendation is recorded under P3 above and was not patched without a successful decision-row GUI capture.

## Cleanup and exploit-risk notes

Landing cancellation clears the pending flag before refunding, removes the mission, and clears both reservation variables, preventing repeated refund calls.

Landing timeout removes pending mission state before applying ordinary cooldown and records only one successful cohort when materialization succeeds.

Kruger expedition failure restores the canonical character only when the obligation receipt and valid host role state permit it, then clears route flags, audience state, and the duration variable.

Mengele expedition cleanup shares only the generic expedition lifecycle and does not call Kruger Directorate mutation helpers.

Honor Accord clamps Strain at zero and uses a timed 180-day cooldown, preventing negative-Strain farming or immediate repeat use.

The rebellion pulse has no free unit or equipment reward and stops after the rebellion bridge marks the country.

Portal success and critical success destroy the selected formation before reconstructing the fixed six-battalion beachhead, preventing a free formation loop.

The two state-raid extraction calls in the critical outcome are intentional bounded payload calls, matching the accepted plan and prior localisation audit; they can transfer up to two eligible state installations, not duplicate the formation.

Persistent Portal beachhead/extraction flags remain the main cleanup follow-up risk listed above.

## MCP evidence and blockers

No callable chaosx_ai_probability_auditor appeared in the installed tool inventory.

hoi4_probability_inspect succeeded for the landing source with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94c734385d1d3ff2aeb4d3b399b4d3f1160058386b6a88f13e3000f000ae9b00/650487d06a2184defc64a566a83e568d1a73fa86905c7a1259b438ba3ef8142f/probability-inspect-ee65b59c5aeb.json; it indexed alien_infantry_call_landing through mission_ai_will_do.

hoi4_probability_inspect succeeded for the DHR country decisions with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d6b6cb71006426ebd5970a550de65ac83987ad858703b6bc0fa9db915dfb7e0/07bb850d62a10ba13a00fa93e62cb504251a785bb457bbcdcbc0c5200c11734c/probability-inspect-293ed1a55ed4.json; it indexed one decision candidate and three mission candidates.

hoi4_probability_inspect succeeded for the contact effect random list with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f45a3bc791b502c621462ff4a8a0b0724d785a0f5fa4d876f3972015e0ed7e7/dea9d71ee1284d5cd31022ee1053baa67a00f3d1980637dfb793d0f49552e614/probability-inspect-4ecd98b765f6.json; it indexed the two revolt/no-revolt entries through random_list.

hoi4_probability_inspect succeeded for the Portal raid source with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7f74f4d0070ec15cb8d64f7f2502e73c739877ef99f163fc92e8afcb2fff7f4/b4df7143e0b7126b39fb8fe723c2922df18504c1181cb210d169ed3e3ffce0d4/probability-inspect-653eee865c1c.json; it returned no_weighted_surfaces and no candidates.

A direct hoi4_probability_evaluate attempt reached input validation with the required scenarioSet shape, then remained unresponsive for more than two minutes and was terminated at the parent’s request.

No weighted source was patched, so an after-change probability compare was not applicable.

hoi4.gui_inspect for kruger_directorate_container with scenario event016_directorate_compact_current returned INTERNAL_ERROR, artifactCount 0, empty filesScanned, and blocker Unexpected internal error.

hoi4.gui_render for the same window and scenario completed with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce/fc87e0ae2873caacf7590dc2ee23aecece6c1647c805c55cb1d2ae038822d265/kruger_directorate_container-full.svg.

The render artifact has SHA-256 efb93e06f3584a666ca7a109061b9b9a929f3bf3b75e7965d96252280e504cce, size 727134 bytes, and a warning that the response was truncated at 32,768 bytes while the payload was 39,762 bytes.

The rendered layout is the current compact 500x360 Directorate panel with a 500x58 collapsed header, open/close controls, portrait, four labelled meters, role/control line, and footer.

No hoi4.gui_rewrite was justified because no GUI source defect was found and the only source change was localisation.

The installed MCP inventory did not expose a standard decision or mission inspector; only probability and GUI routes were available for this surface.

## Validation and skipped validation

Completed task-specific checks include source review against the accepted addendum and acceptance scenarios, vanilla state-targeted decision and native raid precedent review, focused identifier/cost/cleanup searches, probability source inspection, GUI render, and BOM verification of the edited localisation.

The edited diff contains one localisation line and no gameplay source changes.

Skipped meaningful validation: live Hearts of Iron IV playtesting, native raid engine outcome validation, actual state-targeted decision click tests, and full decision-row GUI inspection remain user-owned or blocked by unavailable/failed MCP routes.

No Hearts of Iron IV executable was launched, consistent with repository instructions.

## Remaining risks and handoff

The parent should carry forward the Portal persistent-flag cleanup policy, Portal Raider minimum-only formation requirement, conservative facility destination gate, and MCP probability/GUI blockers.

The one applied fix is ready for parent review at localisation/english/016_dhrondan_contact_l_english.yml:29.

No broad mechanic, new decision system, new scripted GUI, formable suite, or unrelated balance change was introduced.

Plan handoff path: docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhr_decision_audit_2026-08-25.md.
