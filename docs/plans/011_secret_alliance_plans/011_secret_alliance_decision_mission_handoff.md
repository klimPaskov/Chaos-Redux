# Event 011 Secret Alliance Decision and Mission Handoff

This handoff designs the decision and mission layer for Event 011 Secret Alliance. It is direction-only planning. Working labels below are not final localisation and should not be pasted into player-facing text.

## Implementation Surface

Recommended event-owned files:

- `common/decisions/011_secret_alliance_decisions.txt`
- `common/decisions/categories/011_secret_alliance_categories.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/on_actions/011_secret_alliance_on_actions.txt`
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- Event integration in the eventual Event 011 event script and Event Logs plumbing

Do not place ordinary Event 011 categories in shared legacy decision files. Use the event-owned category and decision files unless a verified engine limitation appears.

Vanilla precedents to mirror:

- `common/decisions/_documentation.md` for targeted decision performance and `target_root_trigger`.
- `common/decisions/WTT_border_conflicts.txt` for activated targeted warnings, state flags, border-war state pairing, border-war escalation, timeout cleanup, and no state transfer.
- `common/decisions/AST.txt` for target arrays, activated missions, and per-target mission cleanup.
- `common/on_actions/*` `on_war_relation_added` precedent for catching any new war relation without a whole-world daily pulse.

## Core Play Loop

The anti-player pact begins hidden and should not become a normal visible faction until the reveal phase. It starts with three founding countries, gains members through Event 011 evolution logic, and acts against the player through pressure, sabotage, diplomatic isolation, and border incidents.

At Evolution II, the player receives a decision category that lets them respond without fully seeing every secret. The category should let the player:

- Build evidence and identify members.
- Protect industry, depots, rail lines, and border states.
- Negotiate with known or suspected members.
- Expose the pact at a cost.
- Prepare for likely war.
- Start limited border conflicts only against pact members that border the player.

At Evolution III, the pact becomes visible as a public faction or faction-like bloc. The same category shifts into public crisis management, war preparation, coalition diplomacy, and final attempts to split members before open war.

If any pact member enters war against the player, the pact reveals immediately and every valid pact member joins the war on the pact side.

## Category Lifecycle

Proposed category id:

- `secret_alliance_countermeasures_category`

### Hidden Setup Phase

Visibility:

- Not visible to the player before Evolution II.
- Hidden event effects may track pact members, pressure, and invitations.
- No player decisions should reveal the pact early unless another accepted Event 011 plan explicitly gives a pre-Evolution II discovery route.

State:

- Global or event-owned arrays track founding and invited pact members.
- Player country stores only suspicion flags and intercepted clue counts.
- Pact members should not be in a visible faction unless Evolution III or war reveal has fired.

### Evolution II Phase

Visibility:

- Category visible to the player if Event 011 is active, Evolution II is enabled and recorded, the player exists, and the pact has at least one valid living member.
- Category should remain visible when empty because the header carries visible values and current phase explanation.

Playable role:

- The player has enough information to act, but not enough to know every member.
- Known-member actions target only members the player has identified or that have exposed themselves through border activity.
- Suspected-member actions are broad domestic or diplomatic missions that can discover new members.

Visible values:

- Suspicion or Public Awareness, shown as a percentage or stage.
- Evidence, shown as integer progress toward exposure thresholds.
- Pact Pressure, shown as low, rising, severe, or equivalent staged wording.
- War Readiness, shown as a percent or stage.
- Industrial Security, shown as a percent or stage.
- Active Operations, shown as current active missions over cap.
- Known Members, shown as a count and dynamic list when any are known.
- Border Risk, shown only when a known pact member borders the player.

The category description should use scripted localisation to show a compact value line and separate tooltip breakdowns. Do not expose raw triggers or raw arrays.

### Evolution III Phase

Visibility:

- Category remains visible if Event 011 is active and the pact is public, the pact has valid members, or the pact war aftermath is unresolved.

Playable role:

- The player no longer investigates a rumour. They manage public crisis, diplomacy, mobilization, and active war risk.
- Unknown member discovery decisions close unless a late hidden member system exists.
- Stronger exposure actions convert into coalition diplomacy and sanction actions.
- Border-war actions become rarer and riskier because formal war is close.

Visible values:

- Pact Cohesion becomes visible after reveal.
- Public Awareness changes into Public Proof or International Recognition.
- War Readiness, Industrial Security, and Active Operations remain visible.
- Known Members should become Pact Members once public reveal fires.

### War Phase

Visibility:

- Category remains visible while the player is at war with at least one pact member, unless Event 011 cleanup has ended the pact.

Playable role:

- Remove peacetime negotiation actions.
- Keep industrial protection, counterintelligence cleanup, propaganda, and war preparation missions.
- Add war-limited actions that weaken pact cohesion, encourage exits, protect rear areas, and record achievement hooks.

### Aftermath Phase

Visibility:

- Hide the category after the pact is dissolved, all members are invalid, the player is defeated, or the event chain marks Event 011 complete.
- If aftermath content is implemented later, use a separate small aftermath category or a narrow phase in this category. Do not leave war missions active after peace.

Cleanup:

- Remove active targeted decisions.
- Remove active missions.
- Clear selected target variables and target flags.
- Clear border-war state flags.
- Clear global event targets if any are used.
- Clear per-target cooldown flags only when the event ends, not when a single decision times out.

## Dynamic Tuning Values

Use `common/script_constants/011_secret_alliance_constants.txt` for tuning. Do not scatter magic numbers across decisions, events, and scripted effects.

Recommended constant groups:

- `secret_alliance_phase_thresholds`: evidence thresholds, awareness thresholds, pact pressure thresholds, reveal thresholds.
- `secret_alliance_active_caps`: base cap, major bonus, wartime bonus, Evolution III bonus, AI cap modifier.
- `secret_alliance_duration_bands`: short, standard, long, emergency, border_incident, negotiation.
- `secret_alliance_cost_bases`: equipment, support equipment, trucks, trains, convoys, fuel, XP, command power, civilian factory burden, stability risk, war support risk.
- `secret_alliance_cost_scaling`: industry scale, manpower scale, pact pressure scale, known member scale, prior success discount, prior failure surcharge.
- `secret_alliance_ai_weights`: defensive posture, exposure route, negotiation route, border risk, war readiness, industry protection, low stability blocker, low stockpile blocker.
- `secret_alliance_border_wars`: cooldown, minimum duration, combat width, escalation delay, cancellation timeout, province count, win pressure change, loss pressure change.

Duration handling:

- Use file-scoped `@` constants for `days_mission_timeout` where script constants or variable tokens are unsafe.
- For dynamic duration adjustment, activate the mission with a safe base timeout and then use `add_days_mission_timeout` through a scripted effect when campaign state should lengthen or shorten it.
- If a mission family needs very different durations, prefer separate mission variants selected by phase and difficulty rather than one mission with unsupported dynamic timeout syntax.

Cost calculation:

- Use scripted effects to calculate temporary cost variables before completion or activation.
- Use scripted triggers plus custom tooltips to show missing equipment, trains, convoys, fuel, XP, factory burden, or required state control.
- Political power can appear only on diplomatic paperwork actions and should never be the sole cost of a major action.
- Command power costs must stay conservative and never exceed 60.

## State and Variable Model

Global or event scope:

- `global.secret_alliance_members`: array of current pact members.
- `global.secret_alliance_founders`: array of original three members.
- `global.secret_alliance_public`: flag after Evolution III or war reveal.
- `global.secret_alliance_revealed_by_war`: flag when war forced the reveal.
- `global.secret_alliance_pressure`: aggregate pressure against the player.
- `global.secret_alliance_cohesion`: pact cohesion after public reveal.

Player country:

- `secret_alliance_evidence`
- `secret_alliance_public_awareness`
- `secret_alliance_war_readiness`
- `secret_alliance_industrial_security`
- `secret_alliance_negotiation_leverage`
- `secret_alliance_active_operations`
- `secret_alliance_selected_target_id`
- `secret_alliance_border_operation_count`
- `secret_alliance_exposure_success_count`
- `secret_alliance_negotiation_success_count`

Target country:

- `secret_alliance_member` country flag.
- `secret_alliance_founder` country flag.
- `secret_alliance_known_to_player` targeted or country flag.
- `secret_alliance_split_from_pact` flag.
- `secret_alliance_recently_targeted_by_player` timed flag.
- `secret_alliance_border_cooldown_against_player` timed flag.
- `secret_alliance_negotiation_cooldown_against_player` timed flag.

States:

- `secret_alliance_border_incident_active` state flag on paired border states.
- `secret_alliance_depot_security_target` state flag for industrial protection missions.
- `secret_alliance_rail_security_target` state flag for rail and supply missions.

Avoid global event targets for long-lived selected targets unless necessary. If global event targets are used for UI convenience, cleanup must clear them on target invalidation and event end.

## Target Selection and Clutter Control

Use two layers:

1. Main category shows values and broad domestic actions.
2. Targeted actions show only for the selected known member, while AI can still evaluate all valid targets through separate AI-visible decisions or scripted effects.

Human-facing pattern:

- A selector decision lists known valid members.
- Selecting a member sets `secret_alliance_selected_target_id` and a target flag on that member.
- Targeted decisions for negotiation, exposure, border incidents, and diplomatic pressure appear only for the selected target.
- A close target decision clears the selected target.

AI pattern:

- AI bypasses the selector.
- AI-targeted decisions or scripted effects iterate valid targets from arrays with strict validity checks.
- AI never depends on a human-only selected target flag.

Clutter caps:

- Evolution II should show at most two active missions by default.
- Majors can support one additional active mission.
- Evolution III or wartime can support one additional active mission.
- Hard maximum should be four active missions for the human player.
- AI should use a lower cap if low industry, low stockpiles, low stability, or ongoing major war makes new operations unsafe.

Target filters:

- Target country exists.
- Target is a current pact member.
- Target has not capitulated.
- Target is not the player.
- Target is not in the player's faction.
- Target is not a subject of the player.
- Target is not already split from the pact.
- Target route is not closed by disabled evolution logic.
- Target is known to the player unless the decision is explicitly an investigation action.
- Border actions require land adjacency and at least one valid state pair.

## Decision Families

### Counterintelligence

Purpose:

- Convert suspicion into evidence, identify members, reduce pact pressure, and protect against sabotage.

Working decision ids:

- `secret_alliance_expand_counterintelligence_desk`
- `secret_alliance_trace_courier_network`
- `secret_alliance_interrogate_captured_liaisons`
- `secret_alliance_turn_a_pact_contact`

Costs and requirements:

- Army XP or agency-like administrative cost for military liaison work.
- Support equipment for field teams.
- Trucks or trains for courier tracing.
- Stability or war support risk for heavy domestic security work.
- A temporary civilian factory burden for nationwide investigations.

Success:

- Adds evidence.
- May reveal one unknown member.
- Reduces pact pressure or slows invitation progress.
- Improves industrial security if the action uncovers sabotage cells.

Failure:

- Raises pact pressure.
- Adds public anxiety or stability risk.
- Starts a counter-propaganda mission if the pact detects the investigation.

Partial success:

- Adds evidence but also increases public awareness risk.
- Reveals a suspected member without enough proof to expose them publicly.

AI:

- High weight if player AI has high industry and low pact evidence.
- Low or zero weight if stability is dangerously low or equipment stockpile is below the dynamic cost.

### Exposure

Purpose:

- Turn evidence into public proof, reveal members, reduce pact cohesion, and force neutral countries to react.

Working decision ids:

- `secret_alliance_prepare_public_dossier`
- `secret_alliance_invite_neutral_observers`
- `secret_alliance_expose_selected_member`
- `secret_alliance_expose_the_pact_network`

Costs and requirements:

- Evidence threshold.
- Convoys or trains for observer access if overseas or distant.
- Civilian factory burden for press, legal, and diplomatic material.
- Political power may be used in small amounts only for public diplomacy.
- Higher costs if pact pressure is severe or the selected target is a major.

Success:

- Reveals selected member or all known members.
- Lowers pact cohesion after Evolution III.
- Increases neutral sympathy or gives temporary diplomatic defense.
- Counts toward exposure achievements.

Failure:

- Pact pressure rises.
- Target gains a temporary defensive propaganda advantage.
- Some countries treat the player as unreliable, reflected through opinion or temporary diplomacy penalties.

Partial success:

- Public awareness rises and one member becomes known, but the pact cohesion drop is smaller.

Risk:

- Repeated exposure without sufficient evidence should make war more likely. Use a cooldown and evidence cost to prevent spam.

AI:

- AI should prefer exposure if evidence is high, target is not much stronger, and war readiness is adequate.
- AI should avoid exposure when already losing a major war unless pact pressure is near a reveal threshold.

### Negotiation and Splitting

Purpose:

- Pull members away from the pact or delay their participation without making negotiation a flat peace button.

Working decision ids:

- `secret_alliance_open_backchannel_to_selected_member`
- `secret_alliance_offer_verification_terms`
- `secret_alliance_guarantee_a_pact_exit`
- `secret_alliance_buy_out_pact_contracts`
- `secret_alliance_host_security_conference`

Costs and requirements:

- Negotiation leverage.
- Convoys, trains, or fuel if support packages must physically move.
- Civilian factory burden for economic concessions.
- War support loss risk if the public sees concessions as weakness.
- Target cannot be at war with the player.
- Target cannot be the pact leader if a pact-leader concept is added, unless Evolution III has weakened cohesion below a threshold.

Success:

- Target gains `secret_alliance_split_from_pact` or a timed non-participation flag.
- Pact cohesion drops.
- Pact invitation speed slows.
- Target may refuse to join the first pact war for a timed period.

Failure:

- Pact learns the player's negotiation channel.
- Target receives a pressure bonus or becomes harder to split.
- Player loses leverage and may lose public awareness control.

Partial success:

- Target does not leave but receives a participation delay.
- Target reveals another member or reduces pact cohesion slightly.

AI:

- Democracies and non-aligned defensive countries should prefer negotiation before war if threat is moderate.
- Fascist or highly militarized player AI should prefer exposure and war preparation.
- AI must avoid paying concessions to dead, capitulated, subject, or already split targets.

### War Preparation

Purpose:

- Make the player actively prepare for the likely pact war through units, supply, equipment, and time pressure.

Working decision ids:

- `secret_alliance_form_war_room`
- `secret_alliance_stockpile_border_railheads`
- `secret_alliance_disperse_aircraft_and_fuel`
- `secret_alliance_expand_emergency_reserves`
- `secret_alliance_prepare_allied_liaison_routes`

Costs and requirements:

- Infantry equipment and support equipment for reserves.
- Trucks and trains for railhead stockpiles.
- Fuel and air XP for aircraft dispersal.
- Army XP or command power for war room planning.
- Convoys if the player has overseas fronts or known overseas pact members.
- Map requirements for border missions, such as supplied divisions in named or dynamically described border regions.

Success:

- Raises war readiness.
- Adds temporary defense or logistics modifiers.
- Reduces impact of first pact attack.
- Can unlock defensive border missions.

Failure:

- Equipment is consumed without full readiness gain.
- Industrial security can drop if preparation pulls resources away from protection.

AI:

- High weight if any known pact member borders the AI player or pact pressure is severe.
- Lower weight if equipment stockpiles are below the dynamic cost.

### Industrial Protection

Purpose:

- Protect factories, depots, railways, and supply lines from pact sabotage and espionage.

Working decision ids:

- `secret_alliance_harden_military_factories`
- `secret_alliance_guard_rail_and_train_yards`
- `secret_alliance_secure_depot_belt`
- `secret_alliance_screen_war_contracts`

Costs and requirements:

- Support equipment, trucks, trains, and civilian factory burden.
- Local state control for state-targeted protection.
- Industrial regions should be named by scripted localisation or tooltip.

Success:

- Raises industrial security.
- Reduces sabotage event severity.
- Protects mission target states or reduces damage if a sabotage event fires.

Failure:

- Pact pressure rises.
- A targeted state may receive temporary output, rail, or supply penalties.

Partial success:

- Factories are protected but rail security fails, or rail security improves while local public anxiety rises.

AI:

- Prefer if player AI is industrially strong, pact pressure is rising, or recent sabotage flags exist.

### Propaganda and Diplomacy

Purpose:

- Manage public morale, build external support, and deny pact narratives.

Working decision ids:

- `secret_alliance_sponsor_independent_press`
- `secret_alliance_rally_allied_observers`
- `secret_alliance_warn_threatened_neighbors`
- `secret_alliance_publicize_pact_defections`

Costs and requirements:

- Civilian factory burden, convoys for foreign observers, and small political power only where the action is formal diplomacy.
- Evidence or known member count for stronger actions.
- War support or stability risk if the action is inflammatory.

Success:

- Raises public awareness in a controlled way.
- Improves negotiation leverage.
- Makes neutral countries less likely to join the pact.
- Raises allied willingness to support the player.

Failure:

- Public awareness rises faster than evidence.
- Pact pressure increases through counter-propaganda.

AI:

- Democracies and high-stability countries prefer public diplomacy.
- Low-stability countries avoid propaganda that raises public anxiety unless exposure is nearly complete.

### Border Incidents and Border Wars

Purpose:

- Give the player an active military response only when a pact member borders them, without turning the system into war-goal spam.

Working decision ids:

- `secret_alliance_probe_selected_border_member`
- `secret_alliance_secure_border_corridor`
- `secret_alliance_start_limited_border_operation`
- `secret_alliance_border_clash_time_until_cancelled`
- `secret_alliance_escalate_border_clash`

Availability:

- Evolution II or later.
- Selected target is a known pact member.
- Target borders the player through a valid land border.
- Neither side is already at war with the other.
- Neither side is in the same faction.
- No active border incident flags on the selected state pair.
- Target has no recent border cooldown against the player.
- Player has enough divisions in the attacking border state.
- The target has a controlled neighboring state that is not impassable.

Handling:

- Use a WTT-style flow.
- Pick and store attacker and defender state ids.
- Set state flags on both states.
- Activate warning or escalation missions for both sides if both are playable, with AI-only weights for AI.
- Use `start_border_war` with `change_state_after_war = no` unless a later accepted Event 011 route explicitly adds state transfer stakes.
- On win, loser loses pact pressure, cohesion, readiness, or border confidence depending on side.
- On loss, pact pressure and war risk rise.
- On cancel or timeout, clear state flags, variables, and active targeted decisions.

Escalation:

- Border wars should not directly give normal war goals.
- An escalation decision can raise war likelihood and may trigger the pact reveal if the target chooses formal war.
- If formal war starts, use the war reveal effect and make every valid pact member join.

Costs:

- Command power, army XP, infantry equipment, support equipment, and fuel.
- Higher cost if the border is low supply.
- Higher risk if the player lacks sufficient divisions in border states.

Exploit guard:

- Per-target cooldown.
- Per-state active flag.
- No state transfer by default.
- No repeat farming against capitulated or tiny invalid targets.
- No border action if the target is already at war with the player.

AI:

- AI should use border incidents rarely.
- AI weight should rise if war readiness is high, target is weaker, border supply is adequate, and pact pressure is severe.
- AI weight should be zero if the AI is already losing a major war, has low manpower, lacks equipment, or the target is much stronger.

## Timed Mission Families

Missions should be activated from decisions or event effects, not passively dumped into the category. They should auto-complete or time out with distinct effects.

| Mission working id | Owner | Category | Region or target | Requirement | Duration direction | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `secret_alliance_mission_trace_couriers` | Player | Countermeasures | Domestic rail and border routes, dynamic target list | Spend support equipment and trucks, keep industrial security above a dynamic floor, no active courier mission | Standard, lengthened by low stability and many known members | Evidence gain, chance to reveal member, lower pressure | Pressure gain, public anxiety, investigation cooldown | Low if kept as the only evidence discovery mission |
| `secret_alliance_mission_guard_border_corridors` | Player | Countermeasures | Border states adjacent to known pact members | Place supplied divisions in named border region and maintain train stockpile | Medium, shorter in Evolution III | War readiness gain and border risk drop | Target gets border confidence, pact pressure rises | Medium, avoid duplicating war-room mission |
| `secret_alliance_mission_secure_depot_belt` | Player | Countermeasures | Industrial or supply states selected by helper | Control target states, spend support equipment and trains, maintain supply | Standard | Industrial security gain, sabotage severity reduced | State damage or timed output penalty | Low if state-targeted and tied to sabotage risk |
| `secret_alliance_mission_neutral_observer_tour` | Player | Countermeasures | Selected known member or domestic evidence route | Evidence threshold, convoys or trains, no recent failed exposure | Medium to long | Public awareness becomes controlled proof, target pressure drop | Public awareness rises without proof, target hardens | Low if only exposure route mission |
| `secret_alliance_mission_split_selected_member` | Player | Countermeasures | Selected known member | Negotiation leverage, target valid, target not at war, target not pact leader unless cohesion low | Long, modified by target strength and ideology distance | Target split or delayed participation | Leverage loss, target cooldown, pact pressure gain | Low if only member-splitting mission |
| `secret_alliance_mission_war_room_readiness` | Player | Countermeasures | National | Army XP, command power, equipment stockpile, active operations below cap | Long | War readiness gain and first-strike mitigation | Readiness gain reduced, equipment partly lost | Medium, distinguish from border corridor by making this national planning |
| `secret_alliance_mission_counter_sabotage_surge` | Player | Countermeasures | Industrial states after sabotage or high pressure | Support equipment, civilian factory burden, recent sabotage or severe pressure | Emergency to standard | Industrial security recovery and evidence gain | Another sabotage event or security loss | Low if only visible during sabotage pressure |
| `secret_alliance_mission_border_clash_timer` | Player and selected target if playable | Countermeasures | Paired border states | Active border war exists | Emergency, based on border war constants | Cancels stale border war cleanly or records result | Border war escalates or pact pressure rises | Low if tied to one active border clash |
| `secret_alliance_mission_contain_leak_panic` | Player | Countermeasures | National | Failed exposure or high public awareness without evidence | Easy to standard | Stabilizes awareness and restores leverage | Stability or war support risk, pact propaganda boost | Low if reactive only |

Mission quality notes:

- Every mission requires action, resource commitment, target validity, or unit placement.
- Avoid passive missions such as owning a stockpile or waiting above a stability threshold.
- Use partial success where a mission has multiple components, such as evidence gained but public anxiety rising.
- Mission descriptions should name dynamic regions through scripted localisation or refer to a named operational region. Do not expose raw state ids.

## Active Mission Cap

Use a scripted effect such as `secret_alliance_refresh_active_operation_count` before activating missions.

Suggested cap model:

- Base Evolution II human cap: 2.
- Major country bonus: plus 1.
- Evolution III or active war bonus: plus 1.
- Low stability or severe equipment shortage: minus 1 for AI only.
- Absolute cap: 4.

Activation rules:

- If at cap, broad decisions can remain visible but unavailable with a clear custom tooltip.
- Targeted decisions should hide if their target is invalid, but show unavailable if only the cap blocks them.
- AI should not try to start a mission if it is at cap.

## War Reveal and Pact War Join

Use `on_war_relation_added`, not `on_daily` or a whole-world pulse.

Trigger direction:

- If ROOT and FROM are newly at war and either is the player while the other is a current pact member, call the Event 011 war reveal effect.
- If the player is not involved, do nothing unless a later spec gives the pact non-player war behavior.
- If the pact is already public and the join effect has run, do not run it again.

Effect direction:

- Set public reveal flags.
- Record the reveal in Event Logs and evolution history if Evolution III has not already done so.
- Convert all known-member display into public pact-member display.
- Iterate current pact member array.
- Skip dead, capitulated, split, player-subject, player-faction, and already-at-war members.
- Add valid members to the pact side of the war using `add_to_war` with the original pact combatant as the targeted alliance and the player as enemy.
- Apply a short join cooldown flag to prevent double calls during the same on-action cascade.
- Remove peacetime negotiation and border incident decisions.
- Activate war-phase defense and propaganda missions if cap allows.

Uncertainty:

- The final implementation must verify exact ROOT and FROM sides in `on_war_relation_added` against vanilla behavior in context. The plan assumes ROOT and FROM are the two countries that now have a war relation.

## AI Behavior

AI needs route-like posture variables even if this is a player-focused event. The same mechanic can fire for an AI player or observer scenario.

Suggested postures:

- Defensive investigator: prioritizes counterintelligence, industrial protection, and war readiness.
- Public exposer: prioritizes dossier and observer missions when evidence is high.
- Diplomatic splitter: prioritizes negotiation and security conferences.
- Military escalator: prioritizes border readiness and rare border incidents.

Weight factors:

- Pact pressure increases urgency.
- Evidence increases exposure weight.
- War readiness increases border action and exposure weight.
- Low equipment, low manpower, or low stability reduce all costly actions.
- Shared ideology or high opinion with a pact member increases negotiation weight.
- Border adjacency increases border corridor and border incident weight.
- Ongoing major war reduces exposure and border incident weight unless pact pressure is severe.
- Evolution III increases war preparation and coalition diplomacy weight.

Hard blockers:

- Target does not exist.
- Target has capitulated.
- Target is not a pact member.
- Target is already split.
- Target is in the player's faction.
- Target is a player subject.
- Evolution is disabled or route is closed.
- Selected border pair is invalid.
- Active mission cap is reached.
- Required equipment or XP is below dynamic cost.

AI should never use a hidden human selector. Give AI separate target scanning or scripted effects with the same validity checks.

## Localisation and Tooltip Direction

No final text is provided here.

Required localisation surfaces:

- Category name and description.
- Phase-specific category description fragments.
- Dynamic value line for visible values.
- Tooltip breakdown for evidence, awareness, pressure, readiness, industrial security, pact cohesion, and active mission cap.
- Decision titles and descriptions.
- Mission titles and descriptions.
- Cost met and blocked cost text.
- Requirement summaries.
- Detailed custom trigger tooltips for long requirements.
- Target invalid text.
- Success, failure, and partial success tooltips.
- Border state pair tooltip that names states or an operational border region.

Writing direction:

- Evolution II text should describe discovered patterns, missing couriers, foreign liaisons, border movements, and domestic vulnerability without naming hidden future outcomes.
- Evolution III text can describe the public pact and its visible members.
- Decision text should make the action concrete, not a reward list.
- Cost text should be icon-first and short.
- Long requirements must be hidden behind custom tooltips and scripted localisation.
- Do not mention achievements in player-facing decision text.

## Cleanup Requirements

General cleanup effect:

- `secret_alliance_cleanup_countermeasures = yes`

Call it when:

- Event 011 ends.
- Pact is dissolved.
- Player capitulates or ceases to be valid.
- Pact member array becomes empty.
- A selected target becomes invalid.
- War reveal phase replaces peacetime phase.
- Border war cancels, times out, or escalates.

Cleanup must:

- Remove active Event 011 missions.
- Remove active targeted decisions.
- Clear selected target variable and target flags.
- Clear per-state border incident flags.
- Clear attacker and defender state variables.
- Clear global event targets if used.
- Clear temporary public reveal flags only if they are not needed by achievements or Event Logs.
- Preserve achievement tracking flags that record completed feats.
- Clear timed cooldowns only on full event cleanup, not on normal target switching.

## Exploit Risks and Guards

High severity:

- War join double-fire through `on_war_relation_added`.
  - Guard with `secret_alliance_war_reveal_processed` and per-war or short timed join flags.

- Border war farming.
  - No state transfer by default, per-target cooldowns, active state flags, no action against capitulated targets, no repeat if already at war.

- Repeated exposure farming.
  - Spend evidence, apply cooldowns, scale cost by previous exposure attempts, and cap benefits by phase.

- Negotiation removing too many members too quickly.
  - Require leverage, target cooldown, cohesion threshold for founders, and one active split mission at a time.

Medium severity:

- Equipment cost bypass through dynamic cost tooltips that do not remove equipment.
  - Completion effect must remove the same resources that the availability trigger checked.

- Mission cap bypass through activated targeted decisions.
  - Every mission activation effect must refresh and check active operation count.

- Stale selected target showing decisions for invalid countries.
  - Cleanup helper must run when the target is dead, capitulated, split, in player faction, or no longer a pact member.

- Public awareness rising without enough response options.
  - Include leak containment and propaganda routes after failed exposure.

Low severity:

- Too much category clutter after Evolution III.
  - Replace investigation decisions with public crisis decisions instead of showing both.

- AI spending scarce trains or convoys during unrelated wars.
  - AI cost blockers and lower cap protect against this.

## Achievement Hooks

Achievement ids are working identifiers only. Final titles and descriptions need separate achievement localisation direction and icon planning.

- `secret_alliance_all_lamps_lit`
  - Reveal every current pact member before Evolution III public reveal.
  - Disqualify if war reveal happens first.
  - Requires evidence and exposure tracking for each member.

- `secret_alliance_clean_break`
  - Split a founding member from the pact without entering war with any pact member first.
  - Disqualify if the player starts a normal war goal against a pact member before split completion.

- `secret_alliance_no_first_shot`
  - Survive until the pact reveals and defeat the pact war without initiating a border escalation to formal war.
  - Requires tracking that player did not escalate a border clash into war.

- `secret_alliance_iron_curtain_raiser`
  - Win a defensive pact war after completing industrial security and war readiness thresholds.
  - Requires war reveal, readiness threshold, industrial security threshold, and war outcome tracking.

- `secret_alliance_border_sentinel`
  - Win three pact border clashes without losing one and without formal war starting during those clashes.
  - Use `secret_alliance_border_operation_count` and loss disqualifier.

- `secret_alliance_smoke_without_fire`
  - Complete exposure through observers and public proof while keeping public awareness below the panic threshold.
  - Rewards careful exposure route, not spam.

Achievement tracking should be hidden from ordinary decision text. Use achievement UI and documentation for the exact challenge.

## Cost and Requirement Clarity Notes

Implementation must provide:

- One helper to calculate dynamic costs per decision family.
- One helper to print short cost summaries.
- One tooltip per complex decision showing detailed missing requirements.
- State and target names through scripted localisation.
- Active mission cap tooltip that says whether the cap or a target requirement blocks the action.
- Clear blocked text for missing equipment, trains, convoys, fuel, XP, divisions in border states, supplied divisions, evidence, leverage, or industrial security.

Avoid:

- Flat political power exchanges.
- Repeated identical costs across every decision.
- Raw `any_country` or `any_state` trigger text in UI.
- Raw state id lists.
- Final player-facing text in this plan.

## AI Validity and Route-Lock Notes

The implementation should centralize target validity in scripted triggers:

- `is_valid_secret_alliance_member = yes`
- `is_valid_secret_alliance_known_target_for_player = yes`
- `can_secret_alliance_target_be_negotiated_with = yes`
- `can_secret_alliance_target_be_exposed = yes`
- `can_secret_alliance_start_border_operation_against_target = yes`
- `is_secret_alliance_countermeasure_phase_active = yes`
- `is_secret_alliance_war_phase_active = yes`

Every AI decision must use the same validity triggers as the human-facing version. No AI path should act against dead countries, hidden disabled evolutions, closed routes, invalid borders, subjects of the player, or countries that already left the pact.

## Concrete Recommended Fixes for Implementation

1. Create the event-owned category and decision files:
   - `common/decisions/categories/011_secret_alliance_categories.txt`
   - `common/decisions/011_secret_alliance_decisions.txt`

2. Create the tuning file:
   - `common/script_constants/011_secret_alliance_constants.txt`

3. Create helper files:
   - `common/scripted_effects/011_secret_alliance_effects.txt`
   - `common/scripted_triggers/011_secret_alliance_triggers.txt`
   - `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`

4. Add an event-owned on-action hook:
   - `common/on_actions/011_secret_alliance_on_actions.txt`
   - Use `on_war_relation_added` only.
   - Do not add `on_daily`, `on_weekly`, or whole-world pulses.

5. Wire Evolution II to activate or reveal:
   - `secret_alliance_countermeasures_category`
   - Visible value initialization.
   - Known member array initialization for any member already exposed by event logic.

6. Wire Evolution III and war reveal:
   - Public pact state.
   - Pact member display.
   - War join helper.
   - Closure of hidden investigation actions that no longer fit.

7. Implement one mission activation helper:
   - Refresh active operation count.
   - Check cap.
   - Activate mission.
   - Apply dynamic duration adjustment when supported.

8. Implement border-war helper using WTT precedent:
   - Select valid paired states.
   - Set state flags.
   - Activate warning and timeout missions.
   - Start border war.
   - Clear flags and decisions on outcome.

9. Add achievement tracking hooks:
   - Exposure count by member.
   - Founder split.
   - Border clash wins and losses.
   - War reveal source.
   - No-first-shot disqualifier.

## Planning Risks Left for Parent

- No Event 011 source spec exists in the repo at the time of this handoff, so member selection rules, founding countries, invitation rules, and pact leader identity remain undefined.
- The final implementation must verify exact `on_war_relation_added` ROOT and FROM handling in the target game version before wiring the join helper.
- Decision icons, category art, achievement icons, and any animated category presentation are not planned here because the user requested a decision and mission handoff only.
- Focus integration is not planned because no Event 011 focus surface was provided.
- Final localisation is not provided by design. Implementation must write in-world text from the direction above.

