# Event 011 Secret Alliance Decision/Mission Audit Handoff

Audit scope:
- `common/decisions/011_secret_alliance_decisions.txt`
- `localisation/english/011_secret_alliance_l_english.yml`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`

Required reading completed:
- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages: Decision modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Idea modding, AI modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`
- Vanilla decision precedents in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions`
- Event 011 specs and matrices under `docs/specs/011_secret_alliance_specs/`

## Patch Summary

Changed files:
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `localisation/english/011_secret_alliance_l_english.yml`
- `docs/plans/011_secret_alliance_plans/subagent_handoffs/2026-07-01_event011_decision_mission_audit_handoff.md`

Changed identifiers:
- `secret_alliance_interrogate_couriers_effect`
- `secret_alliance_can_open_counter_pact_category`
- `secret_alliance_counter_pact_category_desc`
- All 21 `custom_cost_text` localisation groups used by `011_secret_alliance_decisions.txt`, with `_blocked` and `_tooltip` variants added.

Before behavior:
- `secret_alliance_interrogate_couriers` required command authority and support equipment, but `secret_alliance_interrogate_couriers_effect` only spent command power.
- `secret_alliance_can_open_counter_pact_category` remained true after `secret_alliance_revealed`, so the `visible_when_empty = yes` category could remain visible after reveal with no usable covert decisions.
- The category description was static and did not show the required evidence, preparedness, suspicion, known links, or pact pressure values.
- Custom costs had base localisation only. Blocked custom costs and hover cost tooltips could fall through to missing localisation.

After behavior:
- `secret_alliance_interrogate_couriers_effect` calls `secret_alliance_pay_security_medium = yes`, matching the availability trigger and support-equipment cost.
- `secret_alliance_can_open_counter_pact_category` now returns false after `secret_alliance_revealed`, closing the covert category when the compact is public.
- `secret_alliance_counter_pact_category_desc` displays suspicion, evidence, preparedness, counter-network, known links, and pact pressure without listing hidden member names or total hidden membership.
- Every custom cost key used by the decision file has base, blocked, and tooltip localisation.

## Issue List

### High: Spec missions are mostly implemented as repeatable instant decisions

Affected ids:
- `secret_alliance_guard_rail_offices`
- `secret_alliance_secure_industrial_districts`
- `secret_alliance_harden_ports_and_cables`
- `secret_alliance_frontier_watch`
- `secret_alliance_secure_capital_command`
- `secret_alliance_build_reserve_depots`

Spec expectation:
- Evolution II should include missions for rail offices, industrial districts, ports/cables, suspected frontiers, and capital/command lines with deadlines, success, failure, and map or unit requirements.

Current behavior:
- These are clickable decisions with cooldowns and instant value gains. They spend varied resources, but do not require holding named states, supplied divisions in target regions, port control, rail control, or success/timeout resolution.

Recommended fix:
- Convert the security/readiness subset into actual `days_mission_timeout` missions or paired start-decision plus mission objectives. Use named state groups or custom trigger tooltips for rail, industrial, port, capital, and exposed border objectives.

### High: Final crisis window has duplicate enforcement and an auto-complete pattern

Affected ids:
- `secret_alliance_final_crisis_mission`
- `secret_alliance_force_public_crisis`
- `secret_alliance_final_crisis_window`
- event `chaosx.nr11.60`

Current behavior:
- Public crisis schedules hidden event `chaosx.nr11.60` after `final_crisis_days`.
- A visible mission `secret_alliance_final_crisis_mission` also has `days_mission_timeout = final_crisis_days`.
- The mission is non-selectable. If its `available` block is already true, it can complete immediately and call `secret_alliance_attempt_public_dissolution`.
- The scheduled event still exists, though its reveal helper is guarded by resolved/revealed checks.

Recommended fix:
- Keep one lifecycle owner. Either use the visible mission as the sole timer or keep the hidden event and make the visible mission clearly informational. If the player should choose a final attempt, make it a selectable mission or a separate decision with cost and failure handling.

### High: Second major joining is too broad for Evolution III pressure

Affected ids:
- `secret_alliance_force_public_crisis`
- `secret_alliance_select_second_major`
- `secret_alliance_second_major_candidate`

Spec expectation:
- The second major should be less likely if the target exposed members, split one away, or has strong faction backing. It should be more likely if the target ignored investigations and has low preparedness.

Current behavior:
- `secret_alliance_force_public_crisis` always calls `secret_alliance_select_second_major`.
- `secret_alliance_select_second_major` picks any `secret_alliance_second_major_candidate` with no evidence, preparedness, target isolation, exposed-patron, split-member, or faction-backing modifiers.

Recommended fix:
- Add a route-aware second-major trigger or weighted selection helper. Gate the second major behind pact strength, target isolation, low preparedness, or high chaos, and block or sharply reduce it after strong exposure and split outcomes.

### Medium: Border and route gates do not prove real border readiness

Affected ids:
- `secret_alliance_has_exposed_neighbor`
- `secret_alliance_frontier_watch`
- `secret_alliance_border_search`
- `secret_alliance_close_crossings`
- `secret_alliance_challenge_patrols`
- `secret_alliance_limited_border_war`
- `secret_alliance_invite_border_inspectors`
- `secret_alliance_prepare_exposed_border_mission`

Current behavior:
- The shared gate checks for an exposed member with `any_neighbor_country = { tag = ROOT }`.
- Costs include army-size checks and support equipment, but not supplied divisions in border states, controlled border states, or supply feasibility.
- Strategic passage and shared sea-zone routes from the spec are not represented.

Recommended fix:
- Add a scripted trigger for an exposed land-border pressure state group, with custom tooltip naming the relevant border region. If sea passage is supported, add a separate naval/port route gate rather than using the land-neighbor decision family.

### Medium: AI equivalents exist but are too generic

Affected ids:
- Decision `ai_will_do` blocks in `011_secret_alliance_decisions.txt`
- `secret_alliance_target_ai_equivalent_pulse`

Current behavior:
- Decision weights mostly test values like evidence, preparedness, cohesion, stage, and faction membership.
- AI target equivalent pulse grants evidence, preparedness, exposure, or network directly without paying costs, checking border validity, supply, faction support, war risk, stability fragility, or strength ratio.

Recommended fix:
- Add contextual AI gates for stability, war state, target strength, exposed-neighbor supply, faction backing, active war count, and resource affordability. Keep the pulse as a fallback only if AI cannot use the decision surface.

### Medium: Diplomacy and split operations are not target-specific enough

Affected ids:
- `secret_alliance_private_demarche`
- `secret_alliance_offer_off_ramp`
- `secret_alliance_court_rival`
- `secret_alliance_protect_defector`
- `secret_alliance_pressure_random_exposed_member`
- `secret_alliance_attempt_member_defection`

Current behavior:
- The decisions operate on random exposed members through helper effects.
- No per-target decision row, selected target, relations, ideology, fear of patron, border status, or target strength is considered.

Recommended fix:
- Add a selected-target or targeted-decision layer for exposed members, or at least split member pools by minor/neighbor/patron-associate. Use commitment, ideology, relations, patron presence, and target strength in defection and pressure outcomes.

### Low: Cost design is varied but still partially abstract

Patched:
- Cost display and blocked/tooltip keys were added.
- One underpayment in `secret_alliance_interrogate_couriers_effect` was fixed.

Remaining examples:
- `secret_alliance_harden_ports_and_cables` uses the generic security-medium cost instead of convoys, naval XP, coastal divisions, or port control.
- `secret_alliance_secure_capital_command` is command-power only, not a capital-region defense objective.
- `secret_alliance_close_crossings` and `secret_alliance_challenge_patrols` are command-power-only costs despite representing border control actions.

Recommended fix:
- Add more concrete route costs where the action is logistical, naval, or territorial. Use custom trigger tooltips when the requirements exceed three lines.

## Decision Category Lifecycle Notes

Owner: target country with `secret_alliance_target` flag.

Opening:
- Opens through `secret_alliance_can_open_counter_pact_category`, which allows the category during Evolution II, high suspicion, high evidence, or after `secret_alliance_counter_pact_open`.
- Evolution II calls `secret_alliance_open_counter_pact_category`.

Public crisis:
- `secret_alliance_can_publicly_confront` unlocks public confrontation decisions during public crisis or full dossier conditions.
- `secret_alliance_force_public_crisis` sets `secret_alliance_public_crisis`, activates the war countdown, and schedules hidden crisis resolution.

Reveal and cleanup:
- Patched so `secret_alliance_can_open_counter_pact_category` returns false after `secret_alliance_revealed`.
- `secret_alliance_reveal_compact` removes `secret_alliance_counter_pact_bureau` and adds `secret_alliance_public_war_command`.
- No wartime replacement decision category exists in this audit scope. If the design wants post-reveal wartime subversion, it still needs separate decisions.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `secret_alliance_build_counter_network_mission` | Target | Counter-Pact Desk | National | `secret_alliance_counter_network >= counter_network_strong` | 120 days | Sets done flag, gains evidence and preparedness | Gains suspicion, raises pact cohesion | Medium. It is a passive meter mission, but it at least has distinct success/failure. |
| `secret_alliance_prepare_exposed_border_mission` | Target | Counter-Pact Desk | Exposed neighbor border, abstract | Has exposed neighbor and `preparedness >= preparedness_border_ready` | 150 days | Sets done and prepared-border flags, gains network | Gains suspicion and forces public crisis | High. It duplicates frontier decisions and does not verify supplied divisions or border states. |
| `secret_alliance_final_crisis_mission` | Target | Counter-Pact Desk | National/public crisis | Public crisis active and either preemptive-strike cost is payable or full dossier plus high preparedness | 120 days | Attempts public dissolution | Reveals compact from public crisis | High. It overlaps hidden event `chaosx.nr11.60` scheduled by `secret_alliance_force_public_crisis`. |

Spec-mapped mission gaps:
- Rail offices, industrial districts, ports/cables, frontier watch, and capital command are decisions, not missions.
- No mission currently names a region or checks unit placement in specific states.
- No mission currently verifies supply status.

## Cost And Requirement Clarity Notes

Patched:
- The category header now shows the required mechanic values.
- The base custom cost lines are concise.
- All custom costs now have `_blocked` and `_tooltip` localisation.

Remaining gaps:
- Cost text is still descriptive rather than icon-first with exact numeric amounts. This is acceptable for a quick patch, but the next pass should use dynamic values or short icon-first summaries where possible.
- Several costs do not match the spec palette for their action type, especially ports/cables, capital command, and border crossing decisions.
- Requirements involving places are mostly abstract. Add custom trigger tooltips for named rail, industrial, port, capital, and border regions.

## AI Validity And Route-Lock Notes

Pass:
- Important decisions have `ai_will_do`.
- Most decision visibility gates respect `secret_alliance_can_open_counter_pact_category` and hide before the counter-pact phase.
- Public confrontation is gated by `secret_alliance_can_publicly_confront`.

Gaps:
- AI weights are contextual but shallow. They do not test supply, strength ratio, domestic fragility, active wars, exposed-neighbor feasibility, or faction backing.
- AI target pulse grants progress directly and can bypass the costs the human pays.
- Second major selection ignores the target's successful counterplay.

Route-lock and leak notes:
- No explicit hidden member list is exposed in the decision category after the patch.
- Public confrontation can unlock from full evidence before Evolution III, which matches the spec's high-evidence alternate path.
- Covert category now closes after reveal, preventing an empty visible category leak.

## Localisation And Tooltip Gaps

Patched:
- `secret_alliance_counter_pact_category_desc` now displays state values.
- All custom cost keys have blocked and tooltip variants.

Remaining:
- Success and failure tooltips for missions are present, but they are broad and do not name concrete map requirements.
- Decision effect tooltips generally state value movement, but they do not describe partial success, false lead, or heavy-handed outcomes where those are intended by spec.
- Some text still describes abstract values like "preparedness" and "cohesion" directly. That may be acceptable for mechanic UI, but event prose should keep in-world framing.

## Cleanup And Exploit Risk Notes

Pass:
- Runtime cleanup clears major flags, member flags, event targets, arrays, and ideas.
- `secret_alliance_reveal_compact` and `secret_alliance_resolve_without_war` guard against repeated reveal/resolution.
- `secret_alliance_recently_pressured` has a timed flag duration through `set_country_flag` in the helper.

Risks:
- Repeatable decisions can farm evidence/preparedness/network through cooldown loops. Costs exist, but the lack of mission caps or pressure backlash makes repeated farming likely.
- Public dossier and demand decisions can force public crisis repeatedly until reveal or resolution unless their cooldown and flags are enough in live play.
- `secret_alliance_final_crisis_mission` and hidden event `chaosx.nr11.60` duplicate the final timeout owner.
- No active mission cap exists.

## Concrete Recommended Fixes

1. Convert the security mission family into timed missions:
   - `secret_alliance_guard_rail_offices`
   - `secret_alliance_secure_industrial_districts`
   - `secret_alliance_harden_ports_and_cables`
   - `secret_alliance_frontier_watch`
   - `secret_alliance_secure_capital_command`

2. Add named region/state-group scripted triggers and tooltips:
   - Rail offices/junction states
   - Industrial districts
   - Port and cable stations
   - Capital command region
   - Exposed member border states

3. Rework final crisis ownership:
   - Choose visible mission or hidden event as the single timeout owner.
   - If player agency is required, make the final attempt a decision or selectable mission with cost.

4. Add contextual second-major gating:
   - Lower or block second-major entry after exposed members, defection, high preparedness, or strong faction backing.
   - Raise it when target ignored the pact, has low preparedness, and pact cohesion is high.

5. Improve target-specific diplomacy:
   - Use targeted decisions or a selected exposed member pattern.
   - Make demarche/off-ramp/rival/defector actions use commitment, ideology, relations, border exposure, and patron fear.

6. Strengthen AI equivalents:
   - Keep the pulse as backup, but prefer AI use of real decisions where valid.
   - Add AI blockers for weak stability, bad border supply, ongoing losing wars, lack of resources, and suicidal preemptive strikes.

## Validation

Meaningful validation run:
- Verified localisation remains UTF-8 with BOM after patch: `EF BB BF`.
- Parsed all `custom_cost_text` references in `common/decisions/011_secret_alliance_decisions.txt`; all 21 unique custom cost key groups now have base, `_blocked`, and `_tooltip` localisation.
- Confirmed `secret_alliance_interrogate_couriers_effect` now calls `secret_alliance_pay_security_medium = yes`.
- Confirmed `secret_alliance_can_open_counter_pact_category` now blocks on `secret_alliance_revealed`.

Skipped validation:
- No in-game validation was run.
- No broad event-chain or on-action validation was run because the audit scope was limited to decisions, related localisation, and directly needed helpers.
- No commit was created, per the audit instruction.

## Remaining Risk

The patched decision surface is safer and clearer, but Event 011's decision implementation still falls short of the full Part 3 spec because several intended missions are still instant decisions, map requirements are abstract, AI equivalents are broad, and the final crisis window needs one lifecycle owner.
