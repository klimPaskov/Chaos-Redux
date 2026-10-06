# Event 028 recovery decisions and crater actions audit

Audit date: 2026-10-06.

Disposition: source audit complete with unresolved acceptance and runtime items below.

Repository: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

This was a read-only gameplay audit. The only file written by this subagent is this handoff. Root applied gameplay and localisation edits to the shared working tree while the audit was in progress. Those edits are identified as parent-owned and are not attributed to this audit.

## Scope and evidence

Read AGENTS.md, .agents\skills\chaos-redux-decisions-missions\SKILL.md, .agents\skills\chaos-redux-events\SKILL.md, and .agents\skills\chaos-redux-subagents\SKILL.md.

Read the Event 028 takeover history at C:\Users\klimp\Videos\chaos_redux_trailer\records\cx\phase2_history\028.md and spec parts 6, 7, and 10 under docs\specs\028_asteroid_incoming_specs.

Reviewed current recovery decisions, scripted triggers, recovery and crater effects, mission constants, crater and recovery dynamic modifiers, on_actions, event callbacks, scripted localisation, achievement completion, and cost localisation.

The connected hoi4.reference_context request for the decision surface returned no result after about 62 seconds and was terminated. No artifact, revision, or citation was returned. Pertinent local references were read directly: offline Decision modding at paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:308-331, 339-355, and 467-478; installed decision documentation at C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:12-45; installed effects documentation at C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:1153-1172; installed trigger documentation at C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:1531-1544; offline Effects at paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:344-346 and 3351-3353; offline Scopes at paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md:748-771; and offline Data structures at paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:1174-1183.

The narrow hoi4.decision_inspect request for asteroid_incoming_stabilize_damaged_zone_mission used scenario stabilize_single_named_state, actor GER, date 1936.1.1, and no repository-wide query or refresh flag. It returned no result after about 62 seconds and was terminated. No artifact, revision, or scenario result is claimed. No retry was made.

No scripted GUI is owned by this category, so no GUI inspect or render was applicable. No game or desktop was launched. The parent’s probability auditor owns the required AI-weight analysis. Its scenario-specific result was not available in this handoff, so this audit makes no numeric probability or balance claim.

## Severity-ranked findings

### High: network completion skips damaged states that had no pre-impact rail link

The takeover acceptance in phase2_history\028.md requires a rail connection from the current capital to every damaged non-crater state the country controls, as well as its largest surviving industrial state. The current asteroid_incoming_network_damaged_states_are_linked trigger exempts every controlled affected state that lacks asteroid_incoming_preimpact_rail_linked at common\scripted_triggers\028_asteroid_incoming_triggers.txt:1372-1382. The country can complete the national network mission while a controlled damaged state remains disconnected.

Recommended fix: align the trigger with the accepted objective by requiring the current-capital route for every controlled affected non-crater state. If the parent intends to exempt islands or states without a pre-impact route, record that as a parent-approved design adjustment and update the accepted handoff rather than claiming the current acceptance is met.

### High: the outer-ring objective differs from its takeover acceptance

The takeover acceptance says the outer-ring mission must clear Outer Shock Zone and Light Fragment Damage across the controlled affected set and reduce Ring 2 burden below a constant threshold. The current trigger at common\scripted_triggers\028_asteroid_incoming_triggers.txt:1422-1463 clears those two timed modifiers but then tests that each controlled main_ring_two state has reached the mission share of pre-impact infrastructure, civilian factories, and military factories. There is no Ring 2 burden threshold check.

Recommended fix: implement the accepted Ring 2 burden threshold, or record a parent-accepted substitution that the 60 percent infrastructure and factory recovery requirement is the intended objective. The current source is a distinct objective, though it may be more demanding in some states.

### Medium: network, outer-ring, and regional objective membership changes with current control

Network and outer-ring checks iterate the country’s currently controlled states. Regional capacity is recalculated monthly over the damaged states the country controls at that review. The mission contracts do not freeze a full incident member set or cancel when a non-anchor member leaves control. Losing a badly damaged member can therefore change the objective and regional denominator while the mission continues if its named anchor and, for the network mission, hub remain controlled.

Recommended fix: freeze the accepted objective members and baseline at mission activation, then cancel or transfer the contract if a required member leaves control. If current-control membership is intended, record that acceptance and test whether losing a member should count as progress.

### Medium: duplicate mission success flags are written but not used to prevent another contract

Success effects write asteroid_incoming_mission_successful, asteroid_incoming_outer_mission_successful, asteroid_incoming_regional_mission_successful, asteroid_incoming_network_reconnected, asteroid_incoming_outer_ring_restored, and asteroid_incoming_regional_economy_complete. The mission start helpers asteroid_incoming_try_start_network_mission, asteroid_incoming_try_start_outer_ring_mission, and asteroid_incoming_try_start_regional_economy_mission gate on an active mission and mission capacity, but do not use the corresponding country completion flags to prevent a redundant contract after an earlier success. Other eligible state projects can start a second network, outer-ring, or regional contract. A later timeout could apply the failure penalty after the country-level objective was already completed.

Recommended fix: guard the matching start helpers with their completed country receipt, unless repeat contracts after successful completion are explicitly intended. Keep the per-state receipts for mission-specific outcomes.

### Medium: current profile markers share the same icon

At the source read, the three surveyed profile modifiers asteroid_incoming_crater_material_dense_metallic, asteroid_incoming_crater_material_fused_silicate, and asteroid_incoming_crater_material_shock_crystal all used GFX_idea_asteroid_incoming_fragment_crater in common\dynamic_modifiers\028_asteroid_incoming_crater_dynamic_modifiers.txt:26-40. The profile names and research fields are distinct in localisation, but the state modifier icons do not distinguish them. Check the profile-icon asset handoff before treating this as closed.

### Cross-owner gap: Event 042 still lacks the asteroid visual guard

common\on_actions\042_equipment_from_heavens_on_actions.txt is tracked and clean at the index blob observed during this audit. Its on_nuke_drop handler at lines 21-25 has no asteroid_incoming_visual_strike_state exclusion. Per parent instruction this remains a cross-owner gap only and was not patched.

## Parent-owned patch reviewed in the shared tree

The final targeted read showed parent edits that close several audit findings at source level. They are not changes by this subagent, are not runtime proof, and remain subject to parent diff review and commit.

The seven recovery target selectors now rank only candidates whose state-stored quote passes the same reserve family used by the decision. The parent correction uses asteroid_incoming_transport_dispersion_selected for the debris prepared quote, matching the decision’s available, custom_cost_trigger, and payment branches. The seven candidate quote predicates use the selected state’s stored quote and compare the deciding country’s stockpile through ROOT.

The new crater priority triggers search the persistent mineral-site array, which is bounded to the main crater and up to six fragment sites. They select one highest-profile owned site and one highest-profile rival site, with lower state ID as the tie-break. Owned actions follow security, survey, and fortification stages. Rival actions follow reconnaissance, route disruption, and offensive preparation. With three dust decisions, the source gates the visible primary rows to at most five.

The disruption and offensive result flags now expire after the same operation duration as their local modifiers. This allows those actions to become available again after the operation expires while preventing renewal during its active period.

The hidden country event chaosx.nr28.12 polls the repair-surcharge flag and refreshes state prices after expiry. The on_state_control_changed handler also requotes an affected state synchronously when its controller changes. These paths address stale stored quotes at source level. A live or decision-inspect scenario did not verify the expiry boundary.

The parent added base, blocked, and tooltip localisation keys for all 16 native custom-cost decisions. The three crater inline costs show at most three values and put the fourth spendable type in the full tooltip. The blocked entries render red values. The inline surcharge marker is now the short text “higher cost,” and the tooltip carries its cause and duration.

The report recommendation getter now uses the affordability predicates and includes a rival-crater branch. The crater report wording identifies the selected family of next actions rather than recommending an unavailable fixed action.

Parent-owned files observed modified during this audit include common\decisions\028_asteroid_incoming_decisions.txt, common\scripted_triggers\028_asteroid_incoming_triggers.txt, common\scripted_triggers\028_asteroid_incoming_crater_priority_triggers.txt, common\scripted_effects\028_asteroid_incoming_recovery_effects.txt, common\scripted_localisation\028_asteroid_incoming_scripted_localisation.txt, common\on_actions\028_asteroid_incoming_on_actions.txt, events\028_asteroid_impact.txt, and localisation\english\028_asteroid_impact_l_english.yml. Root owns final review, integration, and commit.

## Decision category lifecycle

Event 028 uses one ordinary Asteroid Recovery category. Emergency actions show while at least one controlled affected state has a live emergency burden. Reconstruction actions show only after emergency work is closed. Dust actions show after emergency and reconstruction work are closed. Crater actions may coexist with dust actions by design.

The parent’s current priority gates reduce the combined dust and crater list to three dust actions plus at most one owned-site and one rival-site action. Emergency recovery has four primary action types and reconstruction has three. The active mission limit is two, below the specification’s stated maximum for either phase. The category closes when there is no local recovery, dust, active mission, or crater interest.

## Cognitive-load and player-facing value notes

The current category phase gates keep emergency and reconstruction actions from appearing together. Dust and crater actions can coexist, but the parent’s site and stage selectors bound the visible list. No separate decision GUI or extra category was introduced.

Mission dates and thresholds have clear significance. The date marks when the objective may complete, 60 percent describes the stated pre-impact repair share, and the regional 75 percent ratios are labeled for factories, infrastructure, and railway. The regional description remains long and presents three progress percentages in one text block. Those values have a named measure and a visible 75 percent target, so they are interpretable, though a later readability pass could summarize them more compactly.

Crater profiles have distinct names and research consequences: dense metallic material benefits industry, fused silicate composite benefits synthetic resources, and shock-formed crystal and glass benefits electronics. They do not change armour. The shared icon noted above weakens visual distinction.

The next-step report now avoids recommending an unaffordable recovery or dust project by using candidate reserve checks. Its crater recommendation names the selected action family rather than a specific stage. There is no unsupported raw value dump in the reviewed mission thresholds.

## Mission quality

| Mission | Owner, category, and objective area | Requirement and timeout | Success and failure | Duplicate risk |
|---|---|---|---|---|
| asteroid_incoming_rescue_route_mission | Country that controls the named emergency state, in Asteroid Recovery. One exact affected non-crater state and its pre-impact rail link. | The 150-day timeout has a 45-day grace window, so the earliest completion gate is day 105. It requires the state repair share and, when the state was pre-impact rail-linked, a current link to the capital. | Success repairs the named state further, closes its emergency, records rescue-route success, and grants the temporary recovery legacy. Timeout records a bounded state death entry, reapplies profile damage, restores the national recovery burden, and raises repair prices. Losing the named state cancels without penalty. | The same state closes its emergency after success, so the rescue family normally disappears for it. Success receipts are not checked by the mission start helper. |
| asteroid_incoming_stabilize_damaged_zone_mission | Country that controls the affected emergency states, in Asteroid Recovery. Captures the two highest-scoring eligible states at activation. | The 120-day timeout has a 45-day grace window, so the earliest completion gate is day 75. Each saved state must reach the 60 percent pre-impact logistics target. The second-state helper returns true when no second state was saved, and the tooltip explicitly says no second damaged state needs the work. | Success closes local emergencies on the saved states and records the national stabilization flag. Timeout applies failure consequences to each saved state still under control and to the country. | The optional second-state branch is internally guarded and does not create a guaranteed timeout for a one-state group. |
| asteroid_incoming_reconnect_national_network_mission | Country that controls the named corridor and captured hub, in Asteroid Recovery. Its other damaged states are tested by the current-control set. | The 180-day timeout has a 45-day grace window, so the earliest completion gate is day 135. It checks infrastructure repair, current-capital rail links for states marked pre-impact rail-linked, and the captured industrial hub. | Success closes local emergencies across currently controlled affected states and records the network flag. Timeout applies local and national failure pressure while the anchor remains valid. | The country completion flag is not checked before a later eligible supply-spine project can start another network mission. |
| asteroid_incoming_restore_outer_ring_mission | Country that controls the named industrial state, in Asteroid Recovery. The objective includes current controlled affected states with outer-shock or light-fragment damage and current main-ring-two states. | The 270-day timeout has a 45-day grace window, so the earliest completion gate is day 225. It clears the stated modifiers and checks 60 percent of pre-impact infrastructure, civilian factories, and military factories in main-ring-two states. | Success marks outer-ring restoration and grants recovery legacy. Timeout applies local damage and the national failure burden while the anchor remains valid. | The outer-ring completion receipt is not checked before another eligible project can start a redundant contract. |
| asteroid_incoming_rebuild_regional_economy_mission | Original target country only, in Asteroid Recovery. The capacity pool is the country’s currently controlled surviving affected non-crater states at each monthly review. | The 365-day timeout has a 45-day grace window, so the earliest completion gate is day 320. Factories, infrastructure, and railway are each compared with their own pre-impact totals and a 75 percent share. | Success records regional completion, applies final industrial restoration to the named state, and maintains the legacy after local burdens end. Timeout applies local and national failure pressure while the anchor remains valid. | The completion receipt is not checked before another eligible rehousing project can start another regional contract. The changing member set can also change the threshold after a state transfer. |

The dates above are the source date gates derived from mission duration minus the 45-day grace constant. They are not evidence that the objective conditions were held continuously for that entire period. Part 6 calls for a required period on the rescue route and supply conditions. If that language means continuous condition tracking rather than a completion gate before timeout, the source needs a timer that resets when the route or supply predicate drops. No decision-inspect or live scenario result confirmed that interpretation.

## Cost and requirement audit

The category has 16 clickable decision types. Counting the ongoing civilian-factory commitment as a spendable cost, all remain at or below four distinct cost types. Every spendable value in the current text uses a texticon. Vanilla localisation confirms £command_power and £civ_factory are engine icons. Requirements such as site control, supplied-garrison proxy, a secure perimeter, or hostile access are separate from payment.

| Decision | Distinct spendable types |
|---|---:|
| Deploy Mobile Hospitals | 4: manpower, support equipment, motorized equipment, civilian factories |
| Open Emergency Rail Corridor | 4: trains, support equipment, fuel, civilian factories |
| Clear Unstable Debris | 4: manpower, support equipment, motorized equipment, civilian factories |
| Distribute Emergency Filters | 4: manpower, support equipment, motorized equipment, civilian factories |
| Rebuild a Supply Spine | 4: trains, support equipment, fuel, civilian factories |
| Restore Outer-Ring Industry | 4: manpower, trains, support equipment, civilian factories |
| Rehouse Displaced Workers | 4: manpower, trains, motorized equipment, civilian factories |
| Harden Factories Against Dust | 3: manpower, support equipment, civilian factories |
| Protect Transport and Reserves | 4: trains, support equipment, fuel, civilian factories |
| Join the Observation Network | 4: convoys, support equipment, fuel, civilian factories |
| Secure the Crater Perimeter | 4: manpower, support equipment, fuel, command power |
| Survey Extraordinary Material | 4: support equipment, fuel, command power, civilian factories |
| Fortify Crater Access | 4: manpower, trains, support equipment, civilian factories |
| Reconnoitre a Crater Site | 2: manpower, support equipment |
| Disrupt Extraction Routes | 3: trains, support equipment, fuel |
| Prepare a Crater Offensive | 3: manpower, support equipment, fuel |

The parent patch now localizes base, blocked, and tooltip forms for the custom-cost keys, renders blocked inline values in red, and keeps inline values to three. The full cost tooltip retains all four permitted types where needed. Quote values are stored per affected state, registered at impact, refreshed monthly while the global recovery update is active, and re-quoted on affected-state control changes. The hidden expiry event refreshes quotes after the failure surcharge ends.

## AI, route locks, cleanup, and exploit risk

Recovery candidate selection now uses state-specific cost and reserve quotes. The player sees the highest-priority affordable state for each recovery action. This changes candidate pools for weighted decisions, so the parent’s probability auditor must use the same named scenarios for baseline and comparison before a numeric balance claim.

The crater target list is bounded to the mineral-site array. Owned sites require live control and action-specific access requirements. Rival sites require an existing controller at war with the actor. Security requires a garrison proxy, controlled access, and reserves. The accepted local supply proxy is a division in the crater or in a controlled access state connected to the actor’s capital. This is not a live division supply-status reader.

Recovery project callbacks carry a country-owned state reservation. Completion and cancellation check that the callback matches the reserved target. Each mission stores its own target state variables, and its cleanup clears only that mission. Annex cleanup removes all five active recovery missions and project reservations. No live callback scenario was run.

Failure effects are present and scoped to the saved states that remain valid. Civilian deaths use the shared exact-state loss contract with the asteroid_rescue_failure reason, a fraction based on current population, and a constant cap. The state’s profile damage is reapplied for a bounded period, the local emergency reopens, the full national recovery burden returns, and repair prices receive a timed surcharge. Same-state failure processing is limited to once per day. Cancelled missions do not invoke timeout penalties.

The takeover acceptance says each national success receipt should be one-time for its incident and state group. Current success flags are written, but the network, outer-ring, and regional mission start helpers do not read their matching country completion flags. This creates a redundant-contract risk after another eligible project completes. Add a completion guard or record an explicit parent decision that repeat contracts are intended.

The dust lapse checks are present in the four dust-protection outcomes. If dust clears before the 30-day project completes, its effect does not restore protection, its cost is not refunded, and the player-facing tooltip says the project lapses. No status flag is set after lapse.

## Localization and tooltip notes

Blocked requirement text separates reserve, route, access, state, project-slot, and garrison conditions from resource costs. Recovery mission tooltips name the objective states or explain when the second stabilization state is absent. Mission dates and 60 or 75 percent thresholds are visible and labeled.

The Event 028 cost-key contract now has all 16 base, blocked, and tooltip key triples in the current tree. The blocked values are red. State surcharge inline text is the two-word marker “higher cost,” with the cause and duration kept in the tooltip.

The next-step report getter now filters recovery, dust, and crater families by the same affordability and site priority helpers. It provides separate owned-site and rival-site wording. The crater wording describes the next action family rather than naming the exact security, survey, fortification, reconnaissance, disruption, or offensive stage.

## Parent follow-up and validation limits

Current source-level closures from the parent patch are the affordable recovery target ranking, the bounded one-owned and one-rival crater site selectors, the action-stage gates, timed rival-operation result flags, red blocked cost values with full tooltip costs, concise surcharge marking, affected-state price refresh on control transfer, and the hidden surcharge-expiry event. These are source observations only.

Unresolved design or source items are the network route exemption, the outer-ring objective mismatch, dynamic mission-member membership after control changes, redundant mission starts after country-level completion, and the cross-owner Event 042 guard.

Meaningful checks run were a local check of the 16 custom-cost base/blocked/tooltip key triplets, source verification of icon tokens, and the bounded source audit described above. No tests, script validation, live campaign, or rendered decision-list evidence were run. The required native decision inspection and decision reference-context calls returned no result as described above.

Required live checks for the parent or user are: a recovery list with an unaffordable highest-priority state and an affordable lower-ranked state; a one-state and two-state stabilization mission; network repair with a damaged state that lacked a pre-impact rail link; outer-ring completion with all Ring 3 and light-fragment effects ended; a country losing one regional member state during the 75 percent objective; failure death and cost-surcharge expiry before and after a state transfer; project and mission callbacks during state control change or annexation; dust clearing during each of the four protection projects; a multi-site crater category showing no more than five primary rows; security, survey, fortification, recon, disruption, and offensive stages including re-use after the timed operation expires; and the Event 042 nuclear guard after its owner applies the change.

No implementation simplification was introduced by this audit. No broad plan was created. The parent owns the gameplay fixes, probability comparison, final source review, and commit.
