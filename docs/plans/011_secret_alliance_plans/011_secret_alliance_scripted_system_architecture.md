# Event 011 Secret Alliance - Scripted System Architecture Handoff

Status: superseded historical design handoff. No gameplay, localisation, GUI, GFX, binary, or spreadsheet files were changed by this document.

Use `subagent_handoffs/scripted_system_architecture_pass.md` for the accepted implementation architecture and engine-compatible gameplay commit `407b9a05`, atop balance freeze `1c87d923`, for current behavior. Earlier strict reports remain historical scoped evidence. The holistic completion audit owns the current verdict. This early handoff predates the full source specification, and its statement that Event 011 has no manual scenario is superseded by implemented SCN-009 Coalition Unmasked.

## Scope

Event 011 creates a hidden Anti-[player country] Pact. Three random countries secretly coordinate against the player while remaining publicly unaffiliated. They sabotage, conspire, recruit more members, and reveal as a faction when a pact member enters war with the player. Evolution I adds minor members, Evolution II allows one major and unlocks player counter-decisions, and Evolution III moves the pact toward reveal or near-war and may add another major.

There is no world-end branch, manual scenario, or event cluster requirement in the current brief.

## References Consulted

- Repository instructions: `AGENTS.md`.
- Skills: `chaos-redux-event-planning`, `chaos-redux-events`, `hoi4-decisions-missions`, `hoi4-mtth`, `chaos-redux-subagents`.
- Offline Paradox wiki pages: Data structures, Triggers, Effects, Scopes, Decision modding, Event modding, Modifiers, Localisation, On actions, Idea modding, AI modding.
- Vanilla documentation: script concepts, script constants, effects, triggers.
- Vanilla precedents:
  - `common/decisions/BEL.txt`: `create_faction_from_template` and faction invitation flow.
  - `common/decisions/BALTIC.txt`: faction creation with country loops.
  - `common/decisions/AST.txt`: scoped loops, targeted decision activation, saved event targets.
  - `common/factions/templates/`: faction template structure.
- Chaos Redux precedents:
  - Shared dynamic helper documentation and existing event-owned target-array patterns for candidate selection, saved event targets, invalid target cleanup, and target arrays.
  - `common/scripted_effects/chaosx_dynamic_effects.md`.
  - `common/scripted_triggers/chaosx_dynamic_triggers.md`.
  - `common/mtth/chaosx_mtth_variables.txt`.

Frame animation was not used because the current architecture does not require animated UI state.

## Core Architecture

Use one active Event 011 pact instance targeting one player country. The hidden pact must not create a faction until reveal. Before reveal, durable state should live in global arrays, global event targets, country flags, and central variables. After reveal, vanilla faction membership becomes the visible representation, but Event 011 state should still remain available for event logs, decisions, cleanup, and AI handling.

The player country should be represented by a global event target saved at setup. The pact leader should also be represented by a global event target so delayed pulses, decisions, and reveal effects can resolve the same leader without relying on brittle variable or tag reconstruction. Regular event targets should be used inside short chains for current member, current recruit, and selected decision target.

Recommended persistent state:

- `event_target:secret_alliance_target_player`: global event target pointing at the player target.
- `event_target:secret_alliance_leader`: global event target pointing at the current pact leader.
- `global.secret_alliance_members`: all active members.
- `global.secret_alliance_founders`: original three founders.
- `global.secret_alliance_minor_members`: current minor members.
- `global.secret_alliance_major_members`: current major members.
- `global.secret_alliance_revealed_members`: members successfully moved into the revealed faction and war.
- `global.secret_alliance_invalid_members`: recently pruned or blocked countries.
- `global.secret_alliance_counter_targets`: compact player decision target array.

Recommended country flags:

- On members: `secret_alliance_member`, `secret_alliance_founder`, `secret_alliance_minor_member`, `secret_alliance_major_member`, `secret_alliance_hidden`, `secret_alliance_revealed`, `secret_alliance_leader`.
- On target player: `secret_alliance_target`, `secret_alliance_under_sabotage`, `secret_alliance_countermeasures_unlocked`, `secret_alliance_exposed_network`.
- Temporary or cooldown flags: `secret_alliance_recently_considered`, `secret_alliance_selected_counter_target`, `secret_alliance_recently_sabotaged`, `secret_alliance_invalidated`.

Recommended variables:

- Global: `secret_alliance_phase`, `secret_alliance_member_count`, `secret_alliance_minor_count`, `secret_alliance_major_count`, `secret_alliance_exposure`, `secret_alliance_cohesion`, `secret_alliance_sabotage_pressure`, `secret_alliance_reveal_pressure`, `secret_alliance_pulse_sequence`.
- Target player: `secret_alliance_counterintelligence`, `secret_alliance_border_watch`, `secret_alliance_diplomatic_alarm`, `secret_alliance_discovered_members`.
- Member country: `secret_alliance_commitment`, `secret_alliance_risk`, `secret_alliance_sabotage_value`, `secret_alliance_recruit_weight`.

Use flags for binary state. Use variables only for quantities that scale, decay, or feed MTTH and AI weights.

## Candidate Selection Strategy

Setup should run from `chaosx.nr11.1` in player target scope. It should save the target player, build a candidate pool once, choose three founders, mark them, and schedule the first hidden pulse. A one-time setup scan across countries is acceptable; recurring daily, weekly, or monthly world scans are not.

Baseline founder candidates should:

- Exist and be normal playable countries.
- Not be the player target.
- Not be at war with the player target.
- Preferably not be in any faction. For the first implementation, durable members should be required to be out of factions to avoid accidentally dragging unrelated factions into reveal.
- Not be subjects, governments in exile, capitulated, or special chaos/nonstandard countries.
- Not already have Event 011 membership or invalidation flags.
- Have enough independent diplomatic agency to plausibly conspire.

Candidate weighting should prefer countries that are more narratively plausible as an Anti-[player country] pact:

- Existing rivalry, claims, border friction, low opinion, or hostile ideology.
- Strategic proximity to the player target.
- Countries threatened by player expansion, high world tension, or recent player wars.
- Countries outside the player's faction and outside factions friendly to the player.

Use a weighted-array pattern: add candidates multiple times to a temporary pool according to scripted trigger bands, then use `random_scope_in_array`. Keep candidate pool setup in scripted effects and keep criteria in scripted triggers.

If future design wants countries already in factions, represent them as `secret_alliance_associate` contacts rather than pact members. Associates can sabotage or leak intel, but should not be added to the revealed faction unless they first become eligible. This avoids a hidden pact reveal unintentionally involving a third-party faction.

## Major And Minor Rules

Initial founders should be minors unless the event spec later explicitly allows a major founder. This makes the "secret alliance" grow into a major threat through evolutions rather than starting as an instant great-power bloc.

Recommended membership caps:

- Setup: exactly 3 founders, minors only.
- Evolution I: add minors only.
- Evolution II: allow up to 1 major and unlock player counter-decisions.
- Evolution III: allow up to 2 total majors and push reveal or near-war pressure.

The implementation should use a helper trigger for current major cap rather than duplicating phase checks. The major cap should be driven by script constants, not literal numbers embedded in recruitment effects.

## Hidden And Revealed States

Hidden state:

- No faction exists yet.
- Members are tracked by arrays, flags, and event targets.
- Sabotage and conspiracy happen through delayed country events, hidden effects, timed ideas, target variables, and player-facing suspicion/counterintelligence decisions.
- The pact may have a leader for coordination, but the leader should not visibly create a faction.

Revealed state:

- The leader creates a visible faction from a template.
- Valid members join the faction.
- Valid members join the war against the player target.
- Event 011 switches to revealed flags and updates event logs, decision availability, and any evolution state.
- Hidden-only sabotage and recruitment decisions stop or transform into open-war mechanics.

Use `secret_alliance_phase` for broad state:

- `0`: inactive or setup not complete.
- `1`: hidden pact active.
- `2`: exposed or near-reveal state.
- `3`: revealed faction and war state.
- `4`: cleanup or completed state.

## Reveal Trigger Strategy

Primary reveal hook:

- Use the narrow `on_war_relation_added` on-action. If ROOT or FROM is the target player and the other side is a valid pact member, call the Event 011 reveal effect.

Additional reveal paths:

- Player counter-decision success exposes the pact.
- Evolution III escalation event forces reveal or near-war.
- Reveal pressure reaches a tuned threshold during an event-owned hidden pulse.
- A member is already in a new war with the target when a delayed pulse validates member state.

Do not implement `on_daily`, `on_weekly`, or `on_monthly` world iteration for this system without explicit user permission. If a future implementation thinks a recurring world scan is required, it should stop and request permission first. Prefer event-owned delayed pulses from the target player or pact leader.

## Faction Creation Strategy

Use `create_faction_from_template`, not raw `create_faction`. The official documentation marks `create_faction` as deprecated, and vanilla has clear faction-template precedents.

Future implementation should add a faction template file, likely:

- `common/factions/templates/011_secret_alliance_faction_templates.txt`
- Template id: `faction_template_secret_alliance_pact`
- Icon: `GFX_faction_logo_secret_alliance`
- Name key: `SECRET_ALLIANCE_PACT_NAME`

Leader choice at reveal:

- Prefer `event_target:secret_alliance_leader` if still valid, independent, not in a faction, and not at war in a way that blocks faction creation.
- Otherwise pick the strongest valid founder.
- Otherwise pick the strongest valid current member.
- If no valid leader exists, do not silently use a static fallback. The pact should dissolve or the implementation should report a design blocker depending on the final event spec.

Reveal flow:

- Refresh and prune member arrays.
- Resolve or reassign leader.
- Set leader rule if needed: `can_create_factions = yes`.
- Create the faction from template.
- Add valid members to the leader's faction.
- Join valid members to the existing war against the player target.

For war entry, mirror vanilla `add_to_war` patterns after confirming the exact syntax in current vanilla docs and examples. The intended behavior is that members join the same war against the player, not that each member creates a separate war unless reveal is intentionally starting a new war from outside an existing conflict.

If reveal is caused by exposure rather than an existing war, the final design must decide whether the pact declares war immediately or enters a near-war state with a timed ultimatum. Evolution III currently supports either reveal or near-war, so the implementation should keep those as separate effects.

## Decision Category And Target Selectors

Evolution II should unlock player counter-decisions. Use the selected-target pattern from `hoi4-decisions-missions`:

- One player selector decision chooses a suspected country from `global.secret_alliance_counter_targets`.
- Selection marks a single country with `secret_alliance_selected_counter_target` or stores a regular event target inside the activation chain.
- Follow-up targeted decisions act only on the selected target.
- AI countries should not use the human selector. AI should evaluate valid target arrays directly with equivalent scripted effects.

Recommended player decision families:

- Investigate embassy traffic: raises exposure and may discover a member.
- Pressure neutral government: lowers member commitment or blocks recruitment.
- Raid front companies: reduces sabotage pressure, risks diplomatic alarm.
- Fortify suspected border: improves defensive readiness against a selected member.
- Counter-sabotage industry: reduces ongoing damage on the player target.
- Expose pact member: forces a member into public reveal or removes it from the hidden network.
- Demand public guarantees: pressures non-members and associates, with escalation risk.

Costs should not be only political power. Use varied costs and tradeoffs:

- Command power with a cap appropriate for the player stage.
- Stability or war support strain.
- Support equipment, infantry equipment, trucks, trains, convoys, or fuel where appropriate.
- Intel-like exposure and counterintelligence variables for pacing.

Decision targets:

- `target_array = global.secret_alliance_counter_targets`.
- `target_root_trigger` should confirm the player is the target and counter-decisions are unlocked.
- `target_trigger` should confirm the target country is a valid member, suspected member, or associated country depending on the decision.
- Use `activate_targeted_decision` where bounded activation is clearer than permanently visible broad target lists.

## AI Action Equivalents

AI pact members should use scripted effects equivalent to player-visible decisions:

- Sabotage industry or logistics.
- Support recruitment.
- Raise or lower reveal pressure.
- Coordinate with the pact leader.
- Prepare border or war plans once exposure is high.
- Invite a major when the current evolution permits it.

AI target countries should also get counter-action equivalents after Evolution II:

- Internal security sweep.
- Diplomatic pressure on suspected members.
- Border readiness.
- Intelligence exposure.

Use MTTH variables for AI weights and pacing. Keep AI action results in the same scripted effects as player decisions so the AI path does not drift from player mechanics.

Before reveal, overt AI strategies should be modest. Do not make all members openly hostile too early unless exposure is high. After reveal, add stronger AI strategies such as preparing for war, antagonizing the player target, and supporting the pact leader.

## MTTH Plan

Use the `hoi4-mtth` pattern for central pacing and AI weights. Add a future file such as:

- `common/mtth/011_secret_alliance_mtth.txt`

Recommended entries:

- `secret_alliance_recruitment_pulse_days`
- `secret_alliance_sabotage_pulse_days`
- `secret_alliance_exposure_gain`
- `secret_alliance_ai_member_action_weight`
- `secret_alliance_ai_counter_action_weight`
- `secret_alliance_reveal_pressure_days`
- `secret_alliance_major_invite_weight`
- `secret_alliance_member_defection_weight`

Use `set_variable` or `set_temp_variable` with `mtth:<entry>` before applying results. If a destination field rejects variables or constants, use file-scoped constants or a documented meta-effect pattern. Do not silently hardcode timing values.

## Script Constants And Tuning Categories

Use script constants for shared tuning. Future implementation should add:

- `common/script_constants/011_secret_alliance_constants.txt`

Recommended categories:

- `secret_alliance_setup`: founder count, minimum candidate pool, base candidate weights, strict no-faction requirement, setup failure thresholds.
- `secret_alliance_membership`: max total members, Evolution I minor additions, Evolution II major cap, Evolution III major cap, invalid prune threshold.
- `secret_alliance_pressure`: exposure thresholds, sabotage floors and caps, cohesion floors and caps, reveal pressure thresholds.
- `secret_alliance_timing`: setup delay, hidden pulse delay, random pulse window, reveal warning duration, decision cooldowns, mission durations.
- `secret_alliance_ai_weight`: low, medium, high, urgent weights and modifiers for ideology, rivalry, bordering, claims, and player threat.
- `secret_alliance_decision_cost`: command power, equipment, stability, war support, convoy, train, and truck cost bands.

Prefer explicit fixed-point access such as `constant:secret_alliance_membership.evo2_major_cap`. If a script field does not support constants, assign the constant to a variable first or use a local `@` constant with a documentation note explaining the limitation.

## Proposed Helper Map

Scripted triggers, future file `common/scripted_triggers/011_secret_alliance_triggers.txt`:

| Helper | Scope | Inputs | Output | Side effects | Main call sites |
| --- | --- | --- | --- | --- | --- |
| `secret_alliance_target_is_valid` | target player country | none | true if target can own Event 011 | none | entry event, pulses, decisions |
| `secret_alliance_country_base_valid` | candidate country | target via global event target | true if normal independent candidate | none | all selection helpers |
| `is_secret_alliance_founder_candidate` | candidate country | target, constants | true if valid founder | none | setup pool |
| `is_secret_alliance_minor_recruit_candidate` | candidate country | target, phase | true if minor recruit valid | none | Evolution I and hidden pulses |
| `is_secret_alliance_major_recruit_candidate` | candidate country | target, phase, major cap | true if major recruit valid | none | Evolution II and III |
| `is_secret_alliance_valid_member` | member country | target, phase | true if member should remain active | none | refresh, reveal, decisions |
| `is_secret_alliance_reveal_war_pair` | war participant scope | ROOT/FROM from on-action | true if war relation should reveal pact | none | `on_war_relation_added` |
| `secret_alliance_can_reveal` | leader or target context | arrays, member count | true if reveal can create faction | none | reveal events/effects |
| `secret_alliance_counter_target_valid` | target country | player target | true if can be selected by decisions | none | decision target triggers |
| `secret_alliance_selected_counter_target_valid` | target country | player target | true if selected target remains usable | none | decision follow-ups |
| `secret_alliance_has_minimum_members` | global or target context | constants | true if member count above floor | none | cleanup, reveal, pulses |

Scripted effects, future file `common/scripted_effects/011_secret_alliance_effects.txt`:

| Helper | Scope | Inputs | Outputs | Side effects | Main call sites |
| --- | --- | --- | --- | --- | --- |
| `secret_alliance_initialize_context` | target player | event target name, constants | saved global target, reset arrays | clears stale Event 011 state | entry event |
| `secret_alliance_build_founder_pool` | target player | target, constants | temp candidate array | may mark short candidate cooldowns | entry event |
| `secret_alliance_select_founders` | target player | candidate pool | founders and member arrays | flags chosen founders and leader | entry event |
| `secret_alliance_add_member_from_current_scope` | candidate country | member type | member arrays updated | flags current scope as member | recruitment, evolutions |
| `secret_alliance_refresh_member_arrays` | target or leader | target, arrays | valid arrays, counts | prunes invalid members and clears stale flags | pulses, reveal, decisions |
| `secret_alliance_schedule_next_pulse` | target or leader | MTTH entry | delayed country event | increments pulse sequence | setup and pulses |
| `secret_alliance_run_hidden_pulse` | leader or target | phase, MTTH weights | sabotage/recruit/exposure results | schedules next pulse if still hidden | delayed events |
| `secret_alliance_try_recruit_member` | leader or target | evolution phase | optional new member | flags and arrays member | hidden pulse, evolution events |
| `secret_alliance_apply_sabotage_packet` | target player | pressure variables | damage, timed ideas, exposure | raises exposure and risk | hidden pulse, AI action |
| `secret_alliance_unlock_counter_decisions` | target player | evolution phase | decision category visible | flag set, target array seeded | Evolution II |
| `secret_alliance_select_counter_target` | target player | selected FROM target | selected target state | clears previous selection | selector decision |
| `secret_alliance_clear_counter_target` | target player | none | no selected target | clears selection flags | decision completion, cleanup |
| `secret_alliance_reveal_pact` | target or leader | reveal reason | revealed phase | calls refresh, faction, war, log effects | war hook, counter success, Evolution III |
| `secret_alliance_create_revealed_faction` | leader | template, name, icon | visible faction | sets can-create-faction rule if required | reveal |
| `secret_alliance_join_members_to_war` | leader | target war context | members join faction and war | prunes failed joins | reveal |
| `secret_alliance_cleanup_all` | target player | reason | clean arrays and targets | clears flags, variables, decisions, global targets | completion, invalid dissolution |

Document any new dynamic effect helper in `common/scripted_effects/chaosx_dynamic_effects.md` only if the helper is generic and reused beyond Event 011. Event-specific helpers should have their own top-of-file overview and matching event documentation instead of bloating the global dynamic helper docs.

## On-Actions And Pulses

Recommended on-actions:

- `on_war_relation_added`: reveal when a member enters war with the player target.
- `on_capitulation`: refresh member validity for relevant countries.
- `on_annex`: refresh or cleanup when a member or target is annexed.
- `on_leave_faction` or faction-related hooks only if final implementation supports associates or post-reveal defection.
- `on_peaceconference_ended`: cleanup if the revealed pact war is over and the event has no remaining state.

Avoid recurring global on-actions. Hidden operations should be delayed country events scheduled from the player target or leader. A pulse should refresh arrays, perform at most one or a small bounded set of member actions, then schedule the next pulse using MTTH pacing.

## Cleanup And Invalid Member Handling

`secret_alliance_refresh_member_arrays` should be a central cleanup helper. It should remove or downgrade a country if it:

- No longer exists.
- Has capitulated or is a government in exile.
- Becomes a subject when independence is required.
- Joins the player faction before reveal.
- Is already in a faction when hidden membership requires factionless members.
- Becomes the player target or is otherwise invalidated by a tag/state transformation.
- Has conflicting Chaos Redux special-system flags that make normal diplomacy inappropriate.

Cleanup should:

- Remove the country from all Event 011 arrays.
- Clear Event 011 member flags.
- Remove or expire Event 011 timed ideas and decision state.
- Clear selected target flags if the country was selected.
- Add the country to invalid/cooldown state if repeated selection would be bad.
- Recompute member, minor, and major counts.

If the leader becomes invalid before reveal, choose a new leader from valid founders first, then from valid current members. If no valid leader exists and the pact is still hidden, dissolve the pact cleanly instead of creating a faction from an arbitrary fallback country. If the target player becomes invalid, run full cleanup.

At final cleanup, clear global event targets:

- `secret_alliance_target_player`
- `secret_alliance_leader`
- any global selected or cached target added during implementation

Regular event targets used only inside a chain do not need manual clearing.

## Migration Plan From Design To Implementation

1. Add Event 011 source spec or merge this architecture into the existing Event 011 spec once created.
2. Add script constants and MTTH entries before gameplay effects so all thresholds and timings are centralized.
3. Implement triggers and effects first, with top-of-file overviews.
4. Implement entry event `chaosx.nr11.1` and hidden delayed pulse events.
5. Implement Evolution I, II, and III call sites using the same add-member and reveal helpers.
6. Add decision category and player counter-decisions after Evolution II state exists.
7. Add AI equivalent effects and AI weights that call the same helper effects.
8. Add faction template, faction icon definition, and localisation in the same implementation change.
9. Add event log, event details, spreadsheet alignment, and documentation after gameplay identifiers are stable.
10. Run targeted audits for event completion, decisions/missions, localisation, and any asset wiring.

## Risks And Unsupported Fields

- Faction creation should use `create_faction_from_template`; raw `create_faction` is deprecated.
- Dynamic faction names through localisation should be tested. If faction name localisation cannot resolve `secret_alliance_target_player`, do not replace it with a static fallback without design approval.
- War joining must preserve the intended war structure. Use vanilla `add_to_war` precedent after confirming current syntax, especially if reveal happens from an existing player-member war.
- Some fields may reject `constant:` or variables, especially duration fields. Use variable assignment, local `@` constants, or meta-effects where required and document the limitation.
- Targeted decisions can become noisy if the target array is too broad. Keep `global.secret_alliance_counter_targets` compact.
- Frequent world scans are a performance risk. Setup scans and rare recruitment pool rebuilds are acceptable; recurring daily, weekly, or monthly world iteration needs explicit user permission.
- Factioned countries are a design hazard before reveal. Keep true members factionless unless the final event spec explicitly accepts the risk and adds associate-state handling.

## Implementation Acceptance Criteria

A future implementation should not be considered complete until:

- `chaosx.nr11.1` saves the target player and selects exactly three valid founders or fails cleanly before visible effects.
- Hidden pact state persists through arrays, flags, variables, and global event targets without creating a faction.
- Evolution I only adds minors.
- Evolution II allows at most one major and unlocks player counter-decisions.
- Evolution III creates near-war or reveal pressure and allows at most two total majors.
- Reveal is triggered by `on_war_relation_added`, a player counter-decision, or a designed Evolution III reveal path.
- Reveal creates a faction from a template, adds all valid members, and joins valid members to the intended war against the player.
- Invalid members are pruned before recruitment, decisions, reveal, and cleanup.
- Player decisions use a selected-target pattern and compact target arrays.
- AI action equivalents use the same scripted effects as player-facing actions.
- Constants and MTTH entries own pacing, counts, costs, and weights.
- No recurring world daily, weekly, or monthly on-action is added without explicit user permission.
- Cleanup clears arrays, country flags, variables, timed ideas, decision state, and global event targets.
- Localisation, event details, event log mappings, docs, faction icon definitions, and any spreadsheet rows are updated in the full implementation.

## Validation Notes For This Handoff

This handoff is read-only architecture. No runtime validation was possible because no gameplay scripts were changed. The design was checked against offline wiki pages, vanilla documentation, vanilla faction and decision examples, and the existing dynamic helper documentation.

No simplifications were used in this document. Open design decisions are explicitly called out above instead of being replaced with fallbacks.
