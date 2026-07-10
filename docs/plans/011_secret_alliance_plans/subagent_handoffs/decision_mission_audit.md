# Event 011 Secret Alliance decision and mission implementation audit

## Verdict

**Incomplete and not ready for a completion claim.**

The current implementation has a broad nominal identifier surface. It contains 67 decision or mission entries and the expected family counts are recognizable. The central player loop is not yet faithful to the accepted specification. Most objectives are passive meter or flag checks, four declared active-cap families never change their counters, dynamic affordability checks do not match click-time deductions, Evidence has no corroborating classes, the three-card suspect UI does not exist, and no Event 011 English localisation exists.

The hostile-war reveal hook has a sound foundation. It checks both directions of `on_war_relation_added`, excludes a limited border conflict because it waits for a normal war relation, guards reveal re-entry, and calls the common reveal transaction. That transaction still cannot prove the hard all-valid-members rule because current validity permits third-party subjects and incompatible faction leaders, faction joining is not post-validated, and delayed or fractured members skipped by a planned offensive receive no later resolution.

Severity summary:

| Severity | Count |
| --- | ---: |
| Critical | 2 |
| High | 8 |
| Medium | 4 |

No gameplay, localisation, asset, spreadsheet, or GUI file was edited by this audit.

## Sources and method

The audit read the complete Event 011 source package, including all five specification parts, all matrices, prompts, research notes, and handoffs. It also read `AGENTS.md`, `hoi4-decisions-missions`, and `chaos-redux-events`.

Required engine references included:

- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- the other required offline core pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, ideas, and AI
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/_documentation.md`
- official trigger, effect, script-constant, and script-concept documentation
- vanilla `common/decisions/JAP.txt`, especially the border-incident and border-conflict chain around lines 3540 to 3683
- vanilla `common/decisions/AST.txt`, including activated mission and cancellation patterns
- vanilla `common/decisions/FIN.txt`, including dynamic variable-backed custom-cost triggers

Important engine semantics applied in this audit:

- `activate_mission` ignores normal activation conditions and cannot activate an already active mission.
- A non-selectable mission auto-completes when its `available` block becomes true.
- `remove_mission` removes a mission without running complete or timeout effects.
- Decision `visible` and `available` are interface-frequency checks. Target filtering belongs in daily `target_root_trigger` and `target_trigger` when possible.
- A custom cost displays and blocks but does not deduct anything. Its trigger, displayed text, and manual deduction must describe the same price.
- Vanilla border conflict decisions use named state pairs, state highlighting, and `divisions_in_border_state` before starting the conflict.

## Nominal matrix coverage

The table distinguishes identifier presence from playable fidelity.

| Matrix family | Current identifiers | Status | Audit result |
| --- | ---: | --- | --- |
| Category lifecycle | 2 categories | Partial | Both categories exist, but Foreign Interference remains open after reveal and the required compact mechanic UI is absent. |
| Investigation decisions | 8 | Partial | All working roles have an entry. Seven merely activate generic missions and one resolves an immediate generic roll. Several decision-to-mission mappings do not match their subject. |
| Counterintelligence missions | 7 | Partial | All seven have timeout bands and mechanical full, partial, and failure branches. Their completion requirements are passive flags or meters rather than named actionable objectives. |
| Protection projects | 8 | Partial | All eight labels exist. They are instant permanent Preparedness gains with the same idea and no maintained burden, regional target, expiry, or working active cap. |
| Diplomatic probes | 7 | Partial | All seven exist. Selected-suspect handling is stale-prone, concessions are mostly generic, and the AI cannot independently choose a target. |
| Deception and offensive actions | 8 | Partial | All eight exist. The active-offensive cap is inert, several are immediate generic rolls, and Evidence classes do not constrain repeated use. |
| Border conflict family | 5 actions plus 1 mission | Incomplete | The conflict can start for free, requires no divisions in the selected border states, does not highlight or name its state pair, bypasses its active cap, and has no withdraw or negotiation choice. |
| Public exposure | 5 | Partial | All five exist. A later recruitment can erase the gameplay meaning of an earlier false accusation. Public proof is a scalar threshold rather than corroborated evidence. |
| Evolution III emergency | 7 plus countdown | Partial | All seven actions and the countdown exist. The emergency cap is inert and the actions can be taken together for a large one-day permanent Preparedness jump. |
| Revealed-war actions | 7 | Partial | All seven exist. Public members are not rebuilt into a valid target selector, so several actions can be inaccessible or point at a stale pre-reveal suspect. |
| Full, partial, failure memory | 7 missions and some generic rolls | Partial | Outcome bands and counters exist. Evidence classes, per-route memory, and later adaptation are absent. |
| Suspect confidence and false leads | Scalar confidence | Incomplete | Bands and false leads exist, but the three-card cap, clue-class corroboration, immutable innocence memory, invalid-target cleanup, and reveal-time public member list do not. |
| AI equivalence | `ai_will_do` on most buttons | Incomplete | Normal targets are hard-blocked to `is_ai = no`, selector AI has weight zero, and no AI target-selection helper bypasses the human selector. |
| Cleanup and cancellation | Common cleanup effect | Partial | Missions are removed and many flags clear. A live border war is not cancelled, selected suspects are not pruned when invalid, one flag name is mismatched, and faction or subject changes have no immediate hook. |
| Localisation and tooltips | Script references only | Missing | No Event 011 localisation file or key definition exists under `localisation/`. |

## Findings

### DM-01 Critical: the complete player-facing localisation and mechanic UI surface is absent

Evidence:

- `localisation/` contains zero matches for `secret_alliance` or `chaosx.nr11`.
- `localisation/english/011_secret_alliance_l_english.yml` does not exist.
- `common/scripted_guis/011_secret_alliance_scripted_gui.txt` does not exist.
- `interface/011_secret_alliance.gui` does not exist.
- Neither category in `common/decisions/categories/011_secret_alliance_categories.txt:9-23` has `scripted_gui =`.
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt` defines phase, Evidence, Preparedness, suspect, confidence, and incident helpers, but no category, GUI, or localisation string calls them.
- The decision file references 67 decision or mission IDs, 22 custom-cost roots, and 74 custom effect tooltips. The event file references 72 event keys. The scripted localisation file routes 32 output keys. A conservative minimum of 397 unique Event 011 localisation definitions is required before adding all GUI, faction, scenario, achievement, and super-event strings. None are currently defined in `localisation/`.

Impact:

The decision and mission layer is not readable or reviewable in game. Costs, blocked states, objective names, success, partial success, failure, suspect confidence, Evidence, Preparedness, and the faction identity have no final visible text. The supplied meter, card, and warning sprites are registered only as sprites and do not form a mechanic window.

Exact patch:

1. Add `localisation/english/011_secret_alliance_l_english.yml` with UTF-8 BOM and cover every current ID, `_desc`, custom tooltip, and all three custom-cost variants: base, `_blocked`, and `_tooltip`.
2. Add `common/scripted_guis/011_secret_alliance_scripted_gui.txt` and `interface/011_secret_alliance.gui` with two meters, exactly three suspect cards, recent incident, active mission count, confidence, selected target, and Evolution III War Pressure.
3. Attach the GUI to the appropriate category with `scripted_gui = <event_owned_gui_id>`.
4. Use `[GetSecretAlliancePhase]`, `[GetSecretAllianceEvidenceBand]`, `[GetSecretAlliancePreparednessBand]`, `[GetSecretAllianceSelectedSuspectName]`, `[GetSecretAllianceSelectedConfidenceBand]`, and `[GetSecretAllianceRecentOperation]` in real category or GUI text.
5. Add named `custom_trigger_tooltip` blocks for all hidden requirements. Current `hidden_trigger` blocks suppress the very information the player needs.
6. Make every custom-cost string icon-first and display the exact stored dynamic variables as integers.

### DM-02 Critical: the reveal transaction does not guarantee the all-valid-members contract

Evidence:

- `secret_alliance_handle_war_relation_added` at `common/scripted_effects/011_secret_alliance_effects.txt:3208-3231` correctly detects either side of a normal target-member war and calls the shared reveal.
- `secret_alliance_is_valid_member` at `common/scripted_triggers/011_secret_alliance_triggers.txt:62-72` does not exclude a third-party subject, a civil-war-invalid actor, or a country that became the leader of an incompatible faction after recruitment.
- `secret_alliance_prepare_current_member_for_faction` at `common/scripted_effects/011_secret_alliance_effects.txt:2164-2172` removes only non-leader faction members. An existing faction leader remains in its faction.
- `secret_alliance_select_reveal_leader` at `common/scripted_effects/011_secret_alliance_effects.txt:2043-2087` randomly selects among eligible sponsors or founders. It does not select the strongest actor in the specified order.
- `secret_alliance_create_public_faction` at `common/scripted_effects/011_secret_alliance_effects.txt:2174-2197` does not verify that the leader actually created the faction or that every snapshot member successfully joined it.
- `secret_alliance_start_planned_coalition_war` at `common/scripted_effects/011_secret_alliance_effects.txt:2361-2411` skips delayed and fractured members. Only turned members are recorded as fracture exits. `constant:secret_alliance_reveal_conversion.delayed_call_days` at `common/script_constants/011_secret_alliance_constants.txt:440` is unused, so delayed and fractured members can remain in the faction and at peace with the target indefinitely.

Impact:

The hard hostile-war rule is structurally present but not proven for all current states. Public planned reveals also leave unresolved faction members rather than giving them delayed entry, refusal, or withdrawal.

Exact patch:

1. Extend `secret_alliance_is_valid_member` with `is_subject = no`, civil-war reliability checks, and a verified faction-exit rule. If an existing faction leader cannot be safely moved, remove it from active membership before the reveal snapshot.
2. Split reveal-leader selection into designated sponsor, strongest valid major, strongest valid founder, and hostile-war anchor fallback. Use a score or sorted candidate helper instead of `random_scope_in_array`.
3. After faction creation, verify `event_target:secret_alliance_leader = { is_faction_leader = yes }`. After each join, verify `is_in_faction_with = event_target:secret_alliance_leader`. Remove or explicitly resolve failures before war accession.
4. Preserve the current two-sided war hook and reveal re-entry guard.
5. Add a delayed-call event or activated mission using `delayed_call_days`. It must either join the member to the target war after the delay or mark withdrawal, remove active membership, and increment the fracture-exit count.
6. Keep hostile-war reveal as the exception that ignores delayed or compromised call state and joins every remaining valid member immediately.

### DM-03 High: affordability, displayed costs, and manual deductions do not use one price

Evidence:

- `secret_alliance_refresh_dynamic_costs` at `common/scripted_effects/011_secret_alliance_effects.txt:442-493` can scale a base 15 command power and 120 support equipment to materially larger values.
- `secret_alliance_can_start_investigation` at `common/scripted_triggers/011_secret_alliance_triggers.txt:241-246` still checks command power above 14 and support equipment above 99.
- `secret_alliance_can_start_protection` at lines 248-253 checks the unscaled base values.
- `secret_alliance_can_start_offensive_action` at lines 264-269 never checks support equipment or trains even though `secret_alliance_pay_offensive_cost` deducts both.
- `secret_alliance_can_start_emergency_action` at lines 290-299 never checks fuel even though `secret_alliance_pay_emergency_cost` deducts fuel.
- `secret_alliance_can_start_war_action` at lines 301-306 never checks support equipment even though `secret_alliance_pay_war_cost` deducts it.
- `secret_alliance_trace_courier_route` pays trains without checking trains. `secret_alliance_inspect_military_access_talks` pays convoys without checking convoys.
- Many decisions add static base checks for trains, trucks, convoys, fuel, or manpower while click-time deductions use scaled country variables.
- `secret_alliance_reconstruct_meeting_circuit` at `common/decisions/011_secret_alliance_decisions.txt:166-188` pays the investigation command-power cost and then pays the command-power cost a second time. At maximum current scale this can exceed the skill's 60 command-power ceiling.
- Every custom political-power cost lacks `ai_hint_pp_cost`, so official decision behavior gives the AI no reason to reserve the manually deducted political power.

Impact:

A decision can be shown as affordable and then deduct more equipment, trains, fuel, manpower, XP, or command power than the player owns. The displayed price can disagree with the actual price. AI resource reservation is also incomplete.

Exact patch:

1. Add action-family affordability triggers that compare against the same stored variables used by payment. Use `meta_trigger` for a field that does not accept a variable token.
2. Stop recalculating cost inside `secret_alliance_pay_*`. Refresh the stored price before the category opens and on the narrow event pulse, then use that exact snapshot for both affordability and deduction.
3. Give every action with extra trains, trucks, convoys, fuel, manpower, or service XP its own composite affordability trigger and custom-cost localisation.
4. Remove the second command-power payment from `secret_alliance_reconstruct_meeting_circuit`, or assign a dedicated capped heavy-investigation price.
5. Add the appropriate static `ai_hint_pp_cost` to every decision whose custom cost manually deducts political power.
6. Use the currently unused action scale, repeat scale, air XP, navy XP, and pressure factors or remove them. The matrix calls for action-specific and repeat-sensitive costs, not one country-size multiplier for nearly every family.

### DM-04 High: the seven counterintelligence missions are passive checks, not named objectives

Evidence:

- `secret_alliance_watch_liaison_route` completes when total Evidence is above 45 and a recent-source-loss flag is absent.
- `secret_alliance_seize_compromised_courier` completes from a generic border-routes flag and Preparedness above 25.
- `secret_alliance_turn_recruited_clerk` completes from two prior flags plus Alertness below 50.
- `secret_alliance_protect_defecting_envoy` completes from a prior consultation flag and Stability above 49 percent.
- `secret_alliance_break_safehouse_network` completes from a safehouse flag and Preparedness above 50.
- `secret_alliance_national_manhunt` completes from cabinet protection, command power, and Stability.
- `secret_alliance_control_rumor_channel` completes from a prior public or consultation flag and Stability.
- These blocks are at `common/decisions/011_secret_alliance_decisions.txt:197-294`.
- No mission stores or displays a state, region, port, rail junction, depot, route, supplied division count, local unit requirement, transport commitment, or extraction point.
- `secret_alliance_inspect_military_access_talks` activates `secret_alliance_national_manhunt`, which does not match the decision subject.

Impact:

Because a non-selectable mission auto-completes when `available` becomes true, several objectives can complete immediately when activated. The rest ask the player to wait for a generic flag or meter. Full, partial, and failure code exists, but the player has little direct work to perform.

Exact patch:

1. At mission activation, select and persist event-owned objective states or routes. Store the target state IDs and print their names in localisation.
2. Use named and visible requirements:
   - liaison and courier routes should name a capital, port, or border route and require maintained transport or surveillance state
   - courier seizure and safehouse missions should require control plus supplied divisions in the selected state or border pair
   - envoy extraction should name and retain control of an extraction capital or port
   - the national manhunt should protect the target capital region and a specific threatened office or route
   - the rumor mission should require a concrete funding or media-channel action rather than Stability alone
3. Add `highlight_states` for map objectives and clear the saved state pair on completion, cancellation, timeout, or invalidation.
4. Preserve the existing 90 to 180 day durations except for the justified 75-day emergency mission.
5. Keep mission-specific full, partial, and failure helpers, but make their outcomes depend on the actual objective state.
6. Remap `secret_alliance_inspect_military_access_talks` to an access or port mission instead of the national manhunt.

### DM-05 High: active caps are inert and permanent Preparedness can be stacked immediately

Evidence:

- `secret_alliance_active_protections`, `secret_alliance_active_diplomacy`, `secret_alliance_active_offensive`, and `secret_alliance_active_emergency` are initialized and cleared, then only read by cap triggers. No gameplay path increments or decrements them.
- Only investigations and one border mission change their active counters. The complete reference set is visible in `common/scripted_effects/011_secret_alliance_effects.txt:485-491,1224-1405,1894-1898` and `common/scripted_triggers/011_secret_alliance_triggers.txt:241-299`.
- Seven repeatable protection decisions and the one-time continuity project can add 83 total Preparedness in one availability window. Each also grants or preserves the same `secret_alliance_hardened_networks` idea.
- Protection gains do not expire or decay. The idea has no cancellation or timed lifecycle.
- Emergency actions can add another 59 Preparedness in one window because the declared emergency cap of two is never consumed.

Impact:

A resource-rich target can nearly maximize Preparedness in one day. Protection projects are duplicate permanent-value buttons rather than maintained commitments. The active caps displayed by the design do not control play.

Exact patch:

1. Convert protection projects into timed maintained projects or activated missions with start, active, complete, cancel, and expiry helpers.
2. Increment `secret_alliance_active_protections` or `secret_alliance_active_emergency` on activation and decrement it on every terminal path.
3. Give each project a maintained component and expiry behavior. Preparedness should be recalculated from active components or lose the component gain when maintenance ends.
4. Add active state to diplomatic and offensive operations that represent continuing probes. Instant actions should use cooldown and per-clue consumption rather than a meaningless active counter.
5. Prevent a completed project from being repeated unless its prior protection expired or a new incident reopened the relevant surface.
6. Replace the single always-identical hardened idea with staged or component-aware ideas.

### DM-06 High: Evidence is farmable and does not use independent evidence classes

Evidence:

- The accepted model requires communications, financial, diplomatic, military, method, and human evidence with corroboration.
- The current code has only `global.secret_alliance_evidence` and direct additions throughout events, missions, and decisions.
- `secret_alliance_record_full_success` at `common/scripted_effects/011_secret_alliance_effects.txt:1136-1145` always adds 15 Evidence and selects a true-member clue, regardless of the action family.
- Repeatable mission-start decisions have cooldowns but no per-clue consumption or completed-route blocker.
- `secret_alliance_present_coalition_case` needs only scalar Evidence above 80 and the current false-confirmed trigger.
- Confidence can be raised repeatedly without proving independent classes.

Impact:

The player can build a complete public case by repeating one method. Duplicate investigations become Evidence generators, and the public-proof route does not enforce corroboration.

Exact patch:

1. Implement one documented `secret_alliance_add_evidence` helper with inputs for evidence class, quality, actor, and source ID.
2. Track per-class values or immutable class flags plus consumed source IDs.
3. Apply diminishing or zero gain when the same source repeats without a new incident.
4. Add `secret_alliance_has_corroborated_evidence` and require at least two independent classes for Likely, Confirmed, public naming, and the coalition case.
5. Route every event, mission, leak, defector, and investigation through this helper instead of direct Evidence additions.
6. Record full, partial, and failure memory by mission family so pact operation selection can adapt to what succeeded.

### DM-07 High: suspect capacity, selected-target lifecycle, and revealed-member selection are incomplete

Evidence:

- `secret_alliance_register_current_country_as_suspect` at `common/scripted_effects/011_secret_alliance_effects.txt:924-934` appends every new suspect. It has no three-card cap, priority score, replacement rule, or weak-lead dismissal memory.
- `secret_alliance_select_suspect` at `common/decisions/011_secret_alliance_decisions.txt:299-306` creates one targeted selector entry per array element. The array can grow without bound.
- `secret_alliance_has_selected_suspect` at `common/scripted_triggers/011_secret_alliance_triggers.txt:197-204` makes stale targets unusable but does not clear the global event target or remove the invalid array entry.
- No on action handles join-faction, puppet, subject-autonomy, or civil-war changes for immediate suspect and member cleanup.
- Reveal snapshotting at `common/scripted_effects/011_secret_alliance_effects.txt:2088-2162` does not populate a public-member selector. Revealed-war actions still depend on the pre-reveal selected suspect and suspect array.

Impact:

The promised three suspect cards do not exist. The decision list can grow with every false lead. Revealed war actions such as separate terms and member opposition may be unavailable because the selected suspect is innocent, cleared, dead, or not one of the public members.

Exact patch:

1. Add a capped, scored three-entry human suspect view array or fixed GUI card set. Keep the full hidden evaluation pool separate.
2. Add `secret_alliance_refresh_suspect_validity` and call it before display rebuilds, on the event pulse, and from narrow faction, subject, annexation, capitulation, and civil-war hooks.
3. Clear `secret_alliance_selected_suspect` immediately when the target becomes invalid and remove its selector decision.
4. On reveal, build a separate public-member target array from `secret_alliance_reveal_member_snapshot`. Revealed-war decisions must target this array, not the concealed suspect array.
5. Give AI a separate target-scoring helper that evaluates every valid actionable member without touching the human selected card.

### DM-08 High: category phase locks do not transform the interface at reveal

Evidence:

- `secret_alliance_response_category_visible` at `common/scripted_triggers/011_secret_alliance_triggers.txt:177-187` remains true when the pact is revealed.
- Most investigation, protection, diplomacy, deception, border, and public exposure decisions use only that trigger or the selected suspect for visibility.
- Mission cancel triggers correctly cancel concealed missions on reveal, but the old clickable decisions remain visible and can activate those missions again.
- The Coalition Crisis category opens alongside the stale Foreign Interference category.

Impact:

The category does not transform from investigation to public coalition management. It produces obsolete actions, two simultaneous major categories, possible immediate mission cancellation loops, and much more clutter than the phase matrix allows.

Exact patch:

1. Make `secret_alliance_response_category_visible` require `secret_alliance_is_concealed = yes`.
2. Move only still-valid protection or counterintelligence aftermath actions into Coalition Crisis with revealed-specific IDs or visible branches.
3. Hide public exposure after reveal and expose the public-member selector plus revealed-war actions instead.
4. During reveal, explicitly remove active hidden decisions if they were activated by effect and cancel hidden missions before the public category rebuild.

### DM-09 High: the border family does not enforce the mapped cost, objective, cap, or exit choices

Evidence:

- `secret_alliance_begin_limited_border_conflict` at `common/decisions/011_secret_alliance_decisions.txt:622-631` shows a custom cost but calls only `secret_alliance_start_dynamic_border_conflict`. No payment helper runs.
- Starting the conflict does not increment `secret_alliance_active_border`, so another border mission can start while the conflict is active.
- The selected state pair is random. No state name or highlight is shown to the player.
- The action checks only that some valid state pair exists. It does not require any division on that border, supplied units, equipment, manpower, or local commitment.
- `secret_alliance_escalate_or_withdraw_border_conflict` at lines 633-641 always calls escalation. There is no withdraw or negotiate outcome.
- `secret_alliance_secure_contested_crossing` at lines 643-657 checks generic flags and Preparedness instead of the stored state pair.
- Vanilla `common/decisions/JAP.txt:3577-3683` highlights the exact states, checks `divisions_in_border_state`, activates matching warning and timeout decisions, and cleans the state flags.

Impact:

The limited conflict is free, geographically opaque, and can bypass its active cap. The player is not making the mapped choice between escalation, negotiation, and withdrawal.

Exact patch:

1. Persist the selected attacker and defender state IDs for the entire border chain and expose both state names through scripted localisation.
2. Add `highlight_states` and a custom requirement tooltip.
3. Require `divisions_in_border_state`, control of the exact pair, supplied local divisions, and the mapped equipment, manpower, XP, and command-power commitment.
4. Call the exact payment helper before `start_border_war` and increment `secret_alliance_active_border`.
5. Decrement the counter and clear state IDs on win, loss, cancellation, escalation, withdrawal, cleanup, and invalidation.
6. Split escalation, negotiation, and withdrawal into separate decisions with distinct costs and results.
7. Keep the current rule that a border conflict alone does not trigger normal-war reveal.

### DM-10 High: Evidence, Preparedness, and Readiness convert into flat ideas rather than scaled wartime effects

Evidence:

- `secret_alliance_convert_hidden_values_to_war_state` computes four 0 to 100 conversion values at `common/scripted_effects/011_secret_alliance_effects.txt:2199-2242`.
- Every reveal member then receives the same `secret_alliance_coalition_opening_coordination` idea regardless of starting Readiness.
- The target always receives `secret_alliance_known_enemy_plans` and `secret_alliance_hardened_networks`, even when scenario launch starts Evidence and Preparedness at zero.
- The ideas in `common/ideas/011_secret_alliance_ideas.txt:36-75` have fixed modifiers and do not read the computed values.

Impact:

A coalition with 18 Readiness and one with 90 Readiness receive the same opening coordination idea. A target with zero Evidence receives the same known-plans idea as a target with a complete case. Prewar counterplay does not carry into the opening war in the promised dynamic way.

Exact patch:

1. Add staged ideas or dynamic modifiers for low, medium, and high opening coordination, known weaknesses, and target defenses.
2. Apply no known-plans idea at zero or fragmentary Evidence.
3. Apply no hardened-network wartime idea at zero or exposed Preparedness.
4. Select the coalition coordination stage from Readiness after turned-member and false-plan penalties.
5. Make Coalition Resolve affect actual member posture or staged modifiers, not only fracture checks and later decisions.
6. Remove or transform `secret_alliance_compromised_channels` at reveal so the visible idea lifecycle matches the phase transition.

### DM-11 High: AI decision equivalence is not operational

Evidence:

- `secret_alliance_target_is_valid` at `common/scripted_triggers/011_secret_alliance_triggers.txt:9-16` requires `is_ai = no`. Normal setup therefore cannot create an AI-controlled target.
- The human selector decision has `ai_will_do = { base = 0 }` at `common/decisions/011_secret_alliance_decisions.txt:299-306`.
- Suspect-facing AI weights rely on the one global human-selected suspect. There is no AI target-selection helper.
- Most `ai_will_do` blocks do not block expenditure during an existential war or when paying the cost would exhaust critical reserves.
- Custom political-power costs lack `ai_hint_pp_cost`.
- Member AI strategies in `common/ai_strategy/011_secret_alliance.txt` are broad build-army and avoid-war values. They do not implement motive, reach, land, maritime, distant-support, or separate-settlement roles from the AI matrix.

Impact:

The presence of `ai_will_do` does not provide the required AI equivalent. An AI target cannot enter the normal system, cannot select a better suspect, and may spend according to stale or incomplete affordability. Coalition member AI also lacks the mapped theater roles.

Exact patch:

1. Add a supported AI-target path for testing and scenario use, or clearly remove the source-spec AI-target promise through an accepted spec change. Do not leave dead weights.
2. Add `secret_alliance_ai_select_action_target` that scores every valid suspect or public member from confidence, geography, resources, motive compatibility that the AI is allowed to know, and current war state.
3. Let AI call the same validated effect helpers without requiring GUI selection.
4. Add zero-weight blockers for existential war, low Stability, low stockpile reserve, unreachable target, invalid route, and insufficient strategic access.
5. Add `ai_hint_pp_cost` for every manually deducted political-power custom cost.
6. Expand member posture by motive and theater role, with cleanup on exit and settlement.

### DM-12 Medium: false-accusation memory is based on current membership instead of innocence at accusation

Evidence:

- `secret_alliance_apply_false_accusation_consequences` marks `secret_alliance_innocent_accused`, then can recruit the false-lead country into the pact at `common/scripted_effects/011_secret_alliance_effects.txt:1623-1648`.
- `secret_alliance_has_false_confirmed_suspect` at `common/scripted_triggers/011_secret_alliance_triggers.txt:405-410` checks whether a publicly named country is not currently an active member.
- Once the innocent country joins because of the accusation, that trigger becomes false. The same historically false accusation no longer blocks the coalition case.

Impact:

An incorrect public accusation can later be treated as a correct case without new proof because the victim joined after being accused. Achievement disqualification remains, but the gameplay public-proof route forgets the error.

Exact patch:

1. Make `secret_alliance_innocent_accused` an immutable at-time fact until terminal cleanup.
2. Change `secret_alliance_has_false_confirmed_suspect` to check that flag, not current active membership.
3. Require a distinct later investigation and explicit proof event before an accusation victim that subsequently joins can be publicly confirmed as a member.
4. Store an Evidence snapshot for public naming and require new evidence before repeating a public accusation against the same country.

### DM-13 Medium: cancellation and cleanup leave stale state

Evidence:

- `secret_alliance_cleanup_runtime_context` clears the unresolved border-war flag but never calls `cancel_border_war` for a live Event 011 conflict.
- `secret_alliance_stockpiles_disperse` is set at `common/scripted_effects/011_secret_alliance_effects.txt:1585`, but cleanup clears `secret_alliance_stockpiles_dispersed` at line 2952.
- Selected suspect cleanup occurs only at final runtime cleanup or manual clear, not at target invalidation.
- Member and suspect validity changes through faction joining, subject status, or civil war have no immediate on-action hook in `common/on_actions/011_secret_alliance_on_actions.txt`.
- `secret_alliance_compromised_channels` is not removed during reveal conversion and can remain stacked with the public-phase ideas until terminal cleanup.

Impact:

The event can leave a border war running after its state is cleared, retain a misspelled protection flag, keep stale suspect pointers, and carry a concealed-phase idea into public war.

Exact patch:

1. Cancel the active border war before clearing Event 011 border flags and state IDs. Keep callback guards so cancellation cannot double-resolve.
2. Standardize the stockpile flag spelling and migrate or clear both spellings once.
3. Add narrow state-change hooks for faction entry, puppet or subject changes, civil-war invalidation, capitulation, annexation, and release as needed.
4. Clear or rebuild the selected target immediately on invalidation.
5. Transform or remove concealed-phase ideas at reveal, then remove public-phase ideas at settlement.

### DM-14 Medium: decision volume and target checks exceed the specified clutter and performance budget

Evidence:

- The sustained Evolution II category can expose most of 8 investigation entries, 8 protection entries, 7 diplomatic probes, 8 offensive actions, 5 border actions, 5 public actions, active missions, and one selector row per suspect.
- The phase matrix calls for 7 to 11 relevant actions in sustained Evolution II.
- `secret_alliance_select_suspect` uses an uncapped target array and interface-frequency `visible` and `available` checks rather than a three-card GUI.
- Official decision documentation states that decision `visible` and `available` checks run at interface frequency and that targeted prefiltering should use `target_root_trigger` and `target_trigger` where possible.
- Founder and scenario member selection can rescan every country once per added member and build up to 40 duplicate ticket entries per candidate. Maximum scenario composition can repeat this process many times in one launch.

Impact:

The category is a debug-menu-sized list rather than a current-state response system. The uncapped suspect selector increases both clutter and repeated UI evaluation. Selection spikes are not recurring global on actions, but they are unnecessarily expensive.

Exact patch:

1. Gate each family by recent incident, phase, selected card, geography, active cap, and route state so only the current 7 to 11 actions appear.
2. Use the fixed three-card scripted GUI instead of one selector row per hidden suspect.
3. Move root-only conditions into `target_root_trigger` and target validity into `target_trigger` on any remaining targeted decision.
4. Build one scored candidate pool per recruitment or evolution batch, then draw without replacement. Do not rescan the whole world for every added member.
5. Preserve the current positive performance property: there is no forbidden global daily, weekly, or monthly country iteration. The event uses a target-bound 45-day pulse and narrow on-action handlers.

## Threshold audit

The confidence and Evidence band helpers use strict `>` comparisons. At exact configured thresholds, the lower band remains active. Examples include `confidence_possible = 15`, `confidence_plausible = 35`, `confidence_likely = 60`, `confidence_confirmed = 85`, and Evidence thresholds at 45, 65, and 80.

This is lower severity than the findings above, but the patch should use explicit `greater_than_or_equals` at the intended inclusive thresholds in:

- `secret_alliance_selected_suspect_is_possible`
- `secret_alliance_selected_suspect_is_plausible`
- `secret_alliance_selected_suspect_is_likely`
- `secret_alliance_selected_suspect_is_confirmed`
- the corresponding scripted-localisation band selectors
- public dossier and reveal gates where the spec says the threshold itself qualifies

## Duplicate and exploit audit

### Engine duplicate protection

Current mission activation generally checks `NOT = { has_active_mission = ... }`, and `activate_mission` itself refuses an already active mission. A simultaneous duplicate instance of the same mission is therefore not the main risk.

### Remaining duplicate and exploit risks

| Risk | Evidence | Required control |
| --- | --- | --- |
| Repeat Evidence farming | Repeatable decision cooldowns reopen the same mission after completion. Full success always adds the same Evidence package. | Consume source IDs and evidence classes. Block or diminish repeats until a new incident. |
| Duplicate protection gameplay | Most protection entries use the same generic payment, the same idea, and a flat 8 to 12 Preparedness gain. | Make each project regional or component-specific with an active lifecycle. |
| Emergency burst | Emergency cap stays zero while one-time buttons can all be clicked. | Increment and decrement the cap through project missions. |
| Border cap bypass | Starting the actual border conflict does not increment the border counter. | Increment on start and decrement on every exit. |
| Public naming repeat | `secret_alliance_name_first_member` can reopen after 90 days without a new-evidence requirement. | Snapshot evidence per suspect and require a later corroborating source. |
| Static conversion exploit | Evidence zero and Evidence one hundred grant the same known-plans idea. | Use tiered or dynamic reveal conversion. |

## Required patch order

1. Implement localisation and the actual compact GUI so the player-facing contract can be reviewed.
2. Fix reveal member validity, faction postconditions, delayed calls, and public member targeting.
3. Make cost snapshots, affordability, displayed cost, manual deduction, and AI hints identical.
4. Implement evidence classes and the capped three-card suspect model.
5. Replace passive mission checks with named state and route objectives.
6. Activate the protection, emergency, offensive, diplomacy, and border caps and remove permanent repeat stacking.
7. Rebuild border conflict costs, units, state highlighting, choices, and cleanup.
8. Add phase locks, AI target selection, motive and theater behavior, and invalidation hooks.
9. Replace flat reveal ideas with tiered or dynamic conversion.
10. Run the validation scenarios below, then request a fresh decision and mission audit.

## Required validation scenarios after patching

| Scenario | Required proof |
| --- | --- |
| Dynamic cost on a large major | Every displayed amount equals the affordability gate and exact deduction. No resource becomes negative. |
| Two active investigations | A third investigation is blocked. Completion, timeout, cancellation, reveal, and cleanup each free exactly one slot. |
| Two active protection projects | A third project is blocked. Expiry removes or recalculates its Preparedness component. |
| Repeated same clue | Repeating one clue class cannot produce a complete dossier or confirmed member. |
| Three suspects plus a fourth lead | Only three cards display. Closing or invalidating one admits the next scored lead and clears the old target. |
| Innocent public accusation | The innocence fact remains even if that country later joins. A coalition case still recognizes the earlier error. |
| Named courier or safehouse mission | The mission displays exact states or route, highlights them, requires real unit, control, supply, or transport action, and resolves full, partial, and failure distinctly. |
| Border conflict | The exact state pair and divisions are required, the full cost is paid, only one border objective is active, and win, loss, cancel, withdraw, negotiate, escalation, and event cleanup all clear state. |
| Border war versus normal war | A limited conflict does not reveal the pact. Escalation to normal war does. |
| Hostile-war reveal | Every post-cleanup valid member joins the public faction and target war exactly once. Turned and delayed flags do not delay this route. |
| Planned reveal with delayed member | The member joins after the configured delay or records a withdrawal. It does not remain an unresolved faction member at peace. |
| Low versus high prewar values | Evidence, Preparedness, and Readiness produce visibly different opening ideas or dynamic modifiers. |
| AI target | AI selects a valid suspect or public member without GUI state, respects resources and current wars, and uses the same validated helpers. |
| Reveal phase transition | Concealed missions cancel, Foreign Interference closes, Coalition Crisis opens, and only public-phase actions remain. |
| Terminal cleanup during border conflict | The border war is cancelled, missions disappear, targets and state IDs clear, and no runtime flag remains. |

## Positive implementation evidence worth preserving

- Event-owned constants, decisions, categories, ideas, triggers, effects, AI, factions, events, and on actions are separated cleanly.
- Decision and mission durations are centralized with safe file-scoped `@` constants.
- The seven investigation missions have explicit timeout, cancel, full, partial, and failure helpers.
- The concealed-to-public reveal uses one guarded transaction rather than separate duplicated reveal effects.
- `on_war_relation_added` is two-sided and avoids a forbidden periodic global country scan.
- Hidden-war reveal calls the same faction and conversion helpers as other reveal routes.
- Runtime cleanup removes active missions with `remove_mission`, then clears counters explicitly, which matches the documented effect semantics.
- The code does not treat a border war as a normal war relation.

## Completion disposition

No accepted matrix family is fully complete in its current player-facing form. The identifier count should not be used as coverage proof. Completion requires the patches and task-specific scenarios above, followed by a fresh audit of the actual final localisation, GUI, decision visibility, dynamic costs, objectives, AI targeting, reveal transaction, and cleanup.
