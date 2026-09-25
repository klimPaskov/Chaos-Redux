# Event 006 League lifecycle audit — 2026-09-25

## Disposition

This is the requested bounded, read-only audit of the League and charter lifecycle across all 14 accepted scenario cases. Source crosswalk is complete for the named cases. The overall Event 006 status remains **HOLD / PARTIAL** because typed probability evidence is incomplete, the event-graph MCP results are partial, the GUI artifacts could not be visually inspected in this session, and live runtime evidence is intentionally user-owned.

No new transition, array-alignment, generation-ownership, caller-reachability, cost-count, cleanup, or exploit defect was found in the current source crosswalk. The accepted DM45 CongressFailed retry is reachable in current source and follows the standard cooldown and growth-since-failure gate. The current working-tree DM-53 gate uses actual League phase or membership receipts and no longer accepts route eligibility alone.

This audit made no gameplay, localization, AI, cost, availability, GUI, or scenario-model edits and made no commit. The only file created by this audit is this handoff. The shared checkout already had unrelated dirty files, including the focus source and the formable-registry trigger noted below; neither was changed or staged by this audit.

## Scope, acceptance basis, and source identity

Accepted behavior was taken from the user-authorized Event 006 scope, including the accepted specs, matrices, diagrams, research rules, and the P2 League section of the next-safe-tranche addendum. The reviewed design surfaces were spec part 3, spec part 6, diagram 006_league_state_machine.md, matrix 006_decision_mission_map.csv, the specified P2 addendum section, and current Event 006 authority documents.

The source surfaces were the requested League trigger, effect, decision, shared-decision, focus-callback, and support-event files, plus the formable-registry trigger/effect, decision helpers, rival-bloc/evolution effects, scripted GUI/interface, relevant localization, and generation-array guards needed to verify DM-53 and the lifecycle consumers.

The source snapshot was initially pinned at HEAD cbb163549744d72de4147413bb7a7c04dc0993ed. Before handoff finalization, HEAD advanced to 98790f5c50c78a05c42ec70cd19b7b541499729d through an unrelated Event 021 popup-description commit; the audited Event 006 source hashes below remained unchanged. The following hashes identify the working-tree source reviewed; they are not claims that the files are committed at that revision.

| Reviewed working-tree source | SHA-256 |
|---|---|
| common/scripted_triggers/006_independence_wave_triggers.txt | 3EE2B9BCC82D39A43578FE069E9AF1623AE0F3209003DBE61A089D950D552B13 |
| common/scripted_effects/006_independence_wave_effects.txt | C8C5538E80821D2101F60FAA2F90B63B465FA4AC71C71EB072DB7364A79E7546 |
| common/decisions/006_independence_wave_decisions.txt | B79340367E73F07343874F5505CBAF36D4EB71677558E35938AD1A04EB9524EB |
| common/decisions/006_independence_wave_shared_decisions.txt | 4D065BDE1AEF2744C987A1E46F089E5398FD36C02993A1B35E7DC57F75B92D7D |
| common/national_focus/006_independence_wave_focus.txt | 62FF7CEDBCFC4523E43C9085A14A5DE66FCF9CC84E047AD2DEAA52C501D8274D |
| events/006_independence_wave_support_events.txt | F8DB738666DC14003DC3240DD027DA3DDD8EC3F67EE85465B9C8F580B4265021 |
| common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt | 2643796F68B9E83E318024465E6FF453C942A02C1AD57CEF32F04A5C75220AF0 |

At inspection time, Git reported the national-focus source and formable-registry trigger as modified in the shared working tree. The focus diff was the existing former-host icon substitution. The formable-registry trigger diff replaces the route-availability branch in the League reveal gate with the regional-conference and charter-vote receipts shown below. This audit did not create, alter, stage, or commit either change.

## Findings sorted by severity

### P2 — Evidence gap: typed AI and probability analysis is incomplete

No scenario-specific typed decision or mission score output, evaluated weights, same-scenario comparison, or effective selection probability was returned for the 14 League cases. The read-only probability route was delegated to chaosx_ai_probability_auditor; its only completed result was a candidate-pool inspection of event chaosx.nr6.363. A follow-up requesting the League scenario set remained pending after two bounded waits.

The .363 inspection identifies two options, rights-charter and secretariat-compromise, with a complete local candidate pool, zero required inputs, and zero unresolved inputs. It does not evaluate either option’s effective weight, run a named scenario, render probabilities, or compare revisions. Its source revision is 48b034dabac40da0b4e8522b736e49f65e5b556bb4fad6598bc91e048b49b8dc and its source hash is 4d7ed5adb1d7c26803d1771ba98d4a3c9149fb2e2661d3ff0e770edbcf613437. Candidate-pool inspection is not a balance result.

The DM45 retry source still uses the centralized high AI base and the retry gate described below. The historical retry handoff’s partial comparison and its 17 unresolved inputs were not treated as fresh evidence or as a quantitative conclusion in this audit.

**Required follow-up:** obtain typed, named-scenario decision and mission analysis through chaosx_ai_probability_auditor, including DM45 retry-ready and retry-unready branches, DM46 route choices, DM47 leadership challenges, DM60 expulsion, DM62 mandate, and relevant League event options. If a later authorized change touches any score or gate that changes the weighted candidate set, compare the same named scenarios before and after. Until that evidence exists, report no quantitative AI balance conclusion.

### P3 — Status display leaves network standing’s meaning unclear

The shared status GUI displays a raw network-standing number beside the League phase. Its surrounding text says invitations, aid, arbitration, and congress votes affect standing, but the rendered display does not expose a scale, band, threshold marker, consequence, or response. Source references are common/scripted_guis/006_independence_wave_scripted_gui.txt and localisation/english/006_independence_wave_gui_l_english.yml, including the network status line and its explanation.

This is a player-facing clarity gap, not evidence that the underlying value is invalid. A future authorized UI/text pass should expose the accepted range or a named band and show the relevant threshold or player response. That work is outside this read-only audit.

### P3 — GUI visual review is not signed off

The shared status-window inspection/render reported 63 GUI_VISIBLE_OVERLAP findings. The artifact was not visually opened in this session, so the findings remain unclassified and no clipping, spacing, click-region, or renderer-only conclusion is claimed. The Formables window’s scenario inspection and render completed without blockers, but its render artifact was likewise not visually opened. Exact artifacts and limits are listed under MCP evidence.

This is an evidence limitation rather than a confirmed layout defect. The production render remains the required in-game visual reference; no GUI edit was requested or made here.

### DM-53 source behavior — prior route-only mismatch does not reproduce in the current working tree

The accepted Part 6 rule says a regional caucus, charter, or member vote opens formable discovery. In the current working tree, common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:804-823 implements the League-state branch as an OR of:

- global independence_wave_regional_conferences_opened;
- global independence_wave_charter_vote_open;
- country independence_wave_league_member; or
- country independence_wave_formable_league_reveal_ready.

The branch does not accept independence_wave_league_route_available. The exact existing working-tree diff removes that route flag and adds the first two global receipts. The route flag is eligibility: package initialization can set it before any League conference, and the focus charter prerequisite uses it before the focus completion opens the conference. Therefore its removal from this reveal gate preserves the lifecycle distinction required by Part 6.

The two phase receipts are written by the corresponding state transitions: independence_wave_open_regional_conference sets the regional-conference receipt at common/scripted_effects/006_independence_wave_effects.txt:2636-2645, and independence_wave_open_charter_vote sets the charter-vote receipt at lines 2694-2703. The charter-vote marker is cleared by the League phase-flag cleanup when that phase ends. League membership is registered on proclamation and remains the post-formation receipt. The explicit country reveal-ready flag is accepted by the gate, but static search found only the trigger reference and a cleanup clear at common/scripted_effects/006_independence_wave_formable_registry_effects.txt:2762; no literal setter was found in current .txt source. The three other receipt paths are present.

DM-53 itself is independence_wave_discover_regional_identity at common/decisions/006_independence_wave_decisions.txt:3712-3745. Its visibility calls the selected-family discovery trigger; completion permanently marks the selected family discovered, creates its member/anchor ledger, and applies country-value deltas. Thus the reveal gate controls a consequential one-time action, not merely a label. Current commit-readiness, undiscovered, selection, and transaction-lock gates remain in force.

The reviewed profile constants assign revealed_by_league_state to 11 family profiles; the shared discovery decision explicitly excludes FORM-05, mediterranean_island_league. The 10 active DM-53 family consumers are Celtic Cooperation State, Adriatic Federation, Danubian Confederation, Baltic Federation, East African Federation, Southern African Confederation, Indian Ocean League State, Maritime Federation, Polynesian League State, and Caribbean Federation.

**Expected versus actual:** the accepted design requires an actual conference, charter, or member receipt, or an explicit reveal receipt. Current working-tree source meets that condition. The earlier route-eligibility concern from the focus audit is therefore closed for this source snapshot; this auditor did not patch it. No direct focus prerequisite is required by the accepted lane map.

**Safe future boundary:** if the parent later revises this gate, keep the trigger scoped to those causal receipts and use a lifecycle-owned setter/clearer for any new explicit receipt. Do not substitute route eligibility. Re-run DM-53 visibility and AI scenario analysis through the probability auditor if the candidate set changes. The current source needs no new patch from this audit.

## League lifecycle crosswalk: all 14 named cases

These are source-path findings. They do not claim that a named scenario was executed in HOI4 or that the corresponding state persisted through save/load.

| Required case | Current source path and caller | Source disposition |
|---|---|---|
| LEAGUE_3_LIVING_FAIL_CLOSED | can_independence_wave_open_regional_conference and can_independence_wave_form_league require the centralized minimum-living-origins threshold of four. DM45’s preparation path and the focus callback both enter through the conference/formability gates. | Three living origins cannot open formation. Source gate is fail-closed; runtime scenario not executed. |
| LEAGUE_4_LIVING_3_WILLING | Formation separately checks living-origin and founder thresholds, cohesion/common-cause requirements, completed preparation, a shared strategic problem, aligned founder arrays, active network membership, and patron/client restrictions. | Four living origins with three willing founders is permitted only when every remaining accepted threshold passes. The fourth living country need not itself be willing. Runtime not executed. |
| LEAGUE_CONGRESS_FAILURE | DM45 timeout records failure and snapshots active-origin and network-member counts, sets the standard centralized cooldown, and enters CongressFailed. Its retry activation calls can_independence_wave_retry_congress, which requires the cooldown to be clear and either active-origin or network-member growth since the snapshot. Completion calls independence_wave_reopen_regional_conferences, then synchronously re-registers the founder, completes preparation, and opens CharterVote. | Retry caller is reachable in current source. RegionalConferences is an intermediate transition during the completed retry effect rather than a lingering selectable phase. AI source remains a centralized high base. Typed retry probability evidence is absent. |
| LEAGUE_FIVE_PILLARS_ADOPTED | DM46 adopts the next missing pillar in its fixed sequence, with cooldown and the accepted shared proposal/leader constraints. When all five exist, the chosen proposal maps to the formal League route and proclamation path. | Five pillars are source-reachable and ordered. Runtime sequencing and weighted selection were not exercised. |
| LEAGUE_EACH_ROUTE | The five focus proposal callbacks write distinct route proposals: defensive congress, development compact, sovereign equality, armed liberation, and radical revisionist. DM46 maps the selected proposal and accepted pillar state into a valid route; route-specific charter flags then gate downstream mechanics. | All five routes have source callers and mapping. AI route probabilities remain unresolved; route reachability is not quantitative balance evidence. |
| LEAGUE_LEADERSHIP_CHALLENGE | DM47 is a selectable mission for an active regional power that is a charter-compliant member, clears the standing gate, and is in Formal or Durable League. Success replaces the leader pointer; timeout records a loss and applies the authored standing/cohesion/confidence losses. | Per-country win/loss flags prevent repeat completion by the same claimant. Source does not prove that only one qualified country can have a challenge active at once; concurrent ballots and timer resolution remain runtime/evaluator questions. |
| LEAGUE_MEMBER_EXPULSION | DM60 requires expulsion authority, a valid selected member, and a recorded factual charter ground; it stores the target while the vote runs. The accepted success/failure helpers update membership/rival-contract state and clear the stored target. DM61 records a sponsored-coup ground only after a real civil-war action. | Target and grounds are source-bound, and the timed vote has success, failure/cancel, cooldown, and cleanup paths. Runtime target persistence and overlapping-vote behavior are unproven. |
| LEAGUE_WAR_MANDATE | DM62 is restricted to a charter-compliant member under the defensive route and mutual-defense charter. It targets a valid external country, writes a target-specific timed authorization and metadata, and clears the active target. The war-relation on-action consumes only the exact attacker/defender authorization; unauthorized external war records expulsion evidence, while internal civil wars are excluded. | Exact target and route locks are present. Authorization is time-limited and target-bound; expiry, save/load, and the on-action sequence were not run live. |
| LEAGUE_FAILED_RESCUE | DM44 requires a valid active member target at war, compliant membership, mutual-defense charter, and the accepted reserve equipment. Success returns reserved infantry/support equipment to the member, grants a guarantee, and clears the target. Peaceful cancellation refunds and improves League standing; abandonment/client-route failure records the failed-rescue latch and applies losses. | The failed-rescue witness feeds the crisis gate and is cleared through lifecycle cleanup. Target/refund/failure paths are source-present; no timer was executed. |
| LEAGUE_CRISIS_REFORM | The crisis-entry helper is restricted to Formal/Durable and an accepted crisis cause, including fracture, failed rescue, member war, patron capture, or pending rival activation. Reform moves to Reformed League; normalization returns to Formal and refreshes the accepted clock/flags. | Source transition and decision caller are present. Player sequencing and crisis availability were not executed. |
| LEAGUE_CRISIS_SPLIT | The split helper accepts League Crisis or an allowed pending rival activation from Formal, Durable, or Reformed. Rival-bloc effects initialize generation-aware rival arrays, register members, and enter the rival phase. | Split route is source-wired from crisis/expulsion/rival activation. Simultaneous member migration and cleanup remain runtime-unproven. |
| LEAGUE_RIVAL_REUNIFICATION | The reunification decision invokes the League helper, transfers valid rival members through generation-aware registration, returns to Formal, and dissolves/clears the rival contract. | Source caller and transfer effects exist. Cross-array migration and persistence have not been run live. |
| LEAGUE_DURABLE | The durability trigger requires the timed mission receipt, Formal League, the minimum member count, and the cohesion threshold. The completion helper rechecks registries, moves to Durable, refreshes member ideas, publishes the durable outcome, and evaluates the next danger milestone. | The accepted mission/transition path is source-present. Timer completion, publication delivery, and subsequent danger interaction remain untested. |
| LEAGUE_GENERATION_CLEANUP | Founder, member, network, active-origin, patron, and historical records carry aligned generation/country metadata. Alignment triggers compare each parallel array length. Reconciliation removes stale/dead/mismatched rows; unregister/dissolve/restart clear current-generation members, leader pointers, transaction targets, flags, and variables while retaining historical receipts where specified. | No new static array-alignment or generation-owner defect was found. MCP workspace lifecycle analysis is partial; tag reuse, save/load, and array mutation were not runtime-tested. |

## Decision category and focus lifecycle

The state sequence is Informal Network → Regional Conferences → Congress Preparation → Charter Vote → Consultative League → Formal League → Durable League, with CongressFailed retrying through the accepted growth/cooldown gate and League Crisis branching to reform, split, dissolution, or rival reunification.

The focus callbacks in common/national_focus/006_independence_wave_focus.txt open the conference, complete preparation, mark congress readiness, and set each of the five route proposals. DM45 owns the founding-contribution timer and performs the congress transitions. DM46 owns the five-pillar charter decision and route proclamation. DM47 is the leadership challenge. Crisis, durability, rescue, expulsion, mandate, reunification, and cleanup callers are in the specified decisions/effects/on-action/rival-bloc files. The current callback source was checked for League lines; its unrelated pre-existing icon diff was left untouched.

Congress and League decision rows are state, charter, member, route, target, and cooldown gated. The League decision file marks only DM45 and DM47 as selectable_mission=yes. Other time-bounded rows, including rescue, expulsion, and mandate, are ordinary timed decisions and are not counted as additional selectable missions. Source does not show more than three simultaneous selectable missions or prove more than six primary rows visible at once. Exact player-visible candidate counts depend on country, phase, route, target state, and the live UI; they were not established by static definitions.

The first successful proclamation calls the one-time news acknowledgement helper and sets its receipt before firing event chaosx.nr6.35. That event is a single-option acknowledgement. It is not replayed by upgrade, reform, or reunification. Event chaosx.nr6.363 is a distinct League evolution incident with rights-charter and secretariat-compromise outcomes; it is not DM45’s formal CharterVote. Its shared evolution dispatch resolves the selected outcome and clears pending state.

## Mission quality notes

| Action | Owner, category, and scope | Requirement and duration | Success / failure / cancellation / duplicate control |
|---|---|---|---|
| DM45 Founding Congress | Active Event 006 network member; League decision category; no geographic target. | Congress unlock and accepted League phase, strategic cost, strategic mission timeout. Retry additionally needs CongressFailed, cooldown expiry, and active-origin or network-member growth since failure snapshots. | Success reopens RegionalConferences if retrying, then completes preparation and CharterVote. Timeout records failure snapshots/cooldown and League losses. Country-level complete/failed flags prevent repeat; the changed-growth gate controls later retries. |
| DM47 Leadership Challenge | Active regional power and compliant League member; League category; no geographic target. | Formal or Durable League, standing threshold, strategic cost, standard mission duration. | Success transfers leader; timeout records claimant loss and applies League/standing losses. Per-claimant win/loss flags prevent repeated attempts. A global one-ballot lock was not established from source; simultaneous challengers need typed scenario/runtime review. |
| DM44 Rescue Threatened Member | Compliant member as decision owner; League category; state-targeted to an active member capital currently at war. | Mutual-defense charter, valid active League member target, short decision timer, diplomatic-light cost plus infantry/support equipment reserve. | Success returns the reserve to target, guarantees it, improves League values, and clears target. Peace cancellation refunds reserve; abandonment/client lock records failed rescue and losses. Exact target and cleanup paths are present. |
| DM60 Charter Expulsion Vote | Charter-expulsion authority; League category; state-targeted to the exact selected member. | Recorded factual expulsion ground and strategic cost; duration and re-enable cooldown use the centralized charter-expulsion-vote constants. | Success resolves the member case and clears target; failure/cancel applies authored failure and cleanup. Target validity is rechecked. Duplicate risk from parallel ballots is not settled by static source alone. |
| DM62 Charter War Mandate | Compliant defensive-route member; League category; state-targeted to one valid external country. | Defensive route and mutual-defense charter; diplomatic-standard cost; rapid decision duration and standard cooldown. Successful completion writes the exact target authorization with the centralized timed-flag duration. | Matching war declaration consumes the mandate through the on-action; other external wars record a factual breach. Target pointer is cleared on completion/cancel and event cleanup. Authorization is bounded by target and expiry. |

The durability timed objective is a shared League mission rather than a selectable decision row. Its accepted duration, minimum-member/cohesion gates, completion receipt, and failure/cancel cleanup are source-centralized; no mission timer was advanced in runtime.

## Cost, requirement, localization, and AI review

No reviewed decision or gameplay-changing League GUI action exceeds four distinct consumed resource types. Cost count treats the civilian-factory modifier as a reserved commitment, not a consumed resource.

- Strategic palette actions such as DM45, DM47, and DM60 consume command power, stability, and one transport alternative (convoys or trains), for three distinct spendable types. Their civilian-factory-use modifier is a separate reservation.
- Standard diplomatic palette actions consume command power and one transport alternative, for two spendable types. DM62 also carries a separate civilian-factory reservation.
- DM53 uses command power and manpower, for two spendable types, plus a separate factory-use reservation.
- DM44 uses command power, one transport alternative, infantry equipment, and support equipment, for four consumed types maximum.
- DM61’s material coup action uses manpower, army experience, infantry equipment, and support equipment, for four consumed types.
- DM41’s safe reserve helper spends only the first eligible surplus channel in priority order: infantry equipment, trains, convoys, then fuel. It does not consume all four.

Reviewed cost localizations use the corresponding texticons for spendable resources; no literal resource-name substitution or hidden fifth consumed type was found. The cost strings place the factory reservation icon close to consumed-cost icons, so player-facing tooltip separation between “spent” and “held” was not confirmed in the GUI. The source modifier shows the factory is reserved, not consumed.

DM53’s description communicates the formable-discovery choice briefly. DM45, DM44, DM60, and DM62 have outcome, target, or threshold descriptions and custom trigger/effect tooltips for blocked/active states. No League-specific wall of repeated requirement prose or cost over four spendable types was found in the reviewed source/localization.

Source route validity is guarded by active Event 006 status, living-country/member checks, founder/member-array reconciliation, client/patron restrictions, charter route and mutual-defense flags, exact selected targets, and explicit internal-war exclusions. AI blocks are present for the League decisions and mandate/expulsion actions. These are source-validity observations only: without typed scenario weights, no relative route preference, mission-selection likelihood, event-option probability, or quantitative balance conclusion is available.

## Cleanup, receipts, exploits, and downstream consumers

League member/founder/active-origin parallel arrays have explicit alignment triggers and generation columns. The audited unregister, reconciliation, dissolution, restart, expulsion, reunification, and event-end paths clear current-generation pointers/flags and active decision targets. The mandate on-action binds authorization to the exact attacker/defender pair and consumes it; a stale mandate cannot authorize a different target under the inspected source path.

No obvious free-equipment loop, repeated guarantee loop, repeatable congress-reward loop, war-goal spam path, member/core spam path, stale generation pointer, or unbounded timed authorization was found in this bounded League review. This is a static source finding, not a runtime exploit test. Preserve the accepted distinction between history receipts and active-generation flags when later cleanup is changed.

Downstream consumers include DM53 formable discovery and its permanent member/anchor ledger, League route/charter decisions, the first-congress news acknowledgement, .363 evolution dispatch, durability publication/ideas, achievement clocks and disqualifiers, expulsion grounds, the war-relation on-action, crisis gates, rival-bloc registry, and generation cleanup. Any later lifecycle gate or receipt change should cross-check those consumers and the accepted matrices before implementation.

## Evidence inventory and limits

### Source evidence

The source crosswalk above comes from the current working-tree files and cited line locations. Current source hashes and repository HEAD are recorded above. Source inspection does not prove event-engine scope resolution, modifier timing, mission coexistence, saved-state persistence, or player-visible decision enumeration.

### Structural MCP evidence

The broad event scan completed as a partial workspace graph. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59c4b8a1a9d5a6af567820ad5a128b78aaef47714cb4eb3e4188f0965b99a9ce/ec37dddfcec9308bbcef7188a0897599aadf454d9583fa60db59061f2a4f5a11/event-scan-cc097d15c00f.json. MCP revision cc097d15c00f15159a92e4fc4de590cfe2b67224170be81d9d17e55e0c16c587; graph included 9,824 events, 15,175 options, 7,764 terminals, zero helpers, and 8,858 unresolved references. Validation was false because large-workspace projection/lifecycle passes were deferred. This is not complete caller or League-state evidence.

The .35 downstream trace was partial at depth three. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe809946a87d7a31dceff310913f0693168057509b92e6937656772db281d5dd/dcb748c14ec41d50507b1931ec852df3a22758bcb8605f4e83f34dc141486a2d/event-trace-9c06eb1a7fbd.json. MCP revision 9c06eb1a7fbdd5d852bc36edd919e9ae791129c2917a7a871505c1811c11ced2. It does not provide complete decision callers, League lifecycle flow, or execution receipts. No helper_expansion, persistent jobs, native MCP tasks, or unverified negotiation route was used.

The decision-owned shared status GUI, independence_wave_status_window, was inspected for LEAGUE_CONGRESS_FAILURE-generated-1. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a106800837de764d35af2f07fc9a42dd7c974cd4b9b1958ecb9f3366e9b18947/95b2f35c6e6e6630f08888e01048c6757fc4e05b03b0ad07bc94951d9119c5fc/gui-inspect.707699b00cd168f6.json. Inspection covered 48 elements and a complete source graph; its validation reported 63 GUI_VISIBLE_OVERLAP findings and partial sprite-render warnings. The 1920x1080 render across normal, active, warning, and completed states produced a 27-artifact bundle, with five variants and four states; validation was false on the overlap warnings. Example full PNG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7435869af6e7aa47ae4e44a4115b58b432fbd6cd61d5c1fd6dae807d63a67677/c2247a1d6ee74a52363c454f6a53fd7a2b639e3603706b464df3e8abd9505de0/independence_wave_status_window-full.png.

DM53’s decision-owned Formables window, chaosx_independence_wave_formable_state_puzzle_window, was inspected for LEAGUE_CONGRESS_FAILURE-generated-1. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/648b56c371a8a0f63ecf79cb6b48ab7cd470048841d4674b3bf01368929cda79/5cab7901c3119bac69ec806c8a60ed0d927f766ab996e0d8f89931cd4aa8632a/gui-inspect.089ac95aa2b601bf.json. The graph was complete, 93 elements were scenario-inspected, fidelity counts were 652 modelled, one approximated, 50 ignored, and zero missing/unsupported/unresolved; structural validation passed. Its 1920x1080 scenario render completed with validation passed and artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d202974f6702e6d78f473c71dc4a53874a21ba0aa6996197805f8fa63c769756/81a7f0bfe0a8aa1fb0bfcd9d4567f0ae483ca36b7380aebd0c70984101a5cdce/chaosx_independence_wave_formable_state_puzzle_w-full.svg. One earlier inspect request timed out at 180 seconds; the retry on the congress-failure scenario succeeded.

The image artifacts were not visually opened. The CUA browser rejected the hoi4-agent URI under its security policy, and the documented environment prohibited an indirect browser/CDP workaround. Therefore this handoff does not classify the 63 status-window findings or claim a visual pass for either window. The Formables render passed its structural validator, but this is not a substitute for viewing its production render.

### Typed probability evidence

Only the event .363 candidate-pool inspection described above was returned by the probability auditor. No typed LEAGUE_* scenario evaluation, mission/decision score breakdown, probability render, sequence, sweep, or current same-scenario compare artifact was returned. The 14 scenario matrix in this handoff is a source crosswalk, not typed probability evidence.

### Live runtime evidence

None. HOI4 was not launched. No live mission timers, decision lists, save/load behavior, event acknowledgements, evolution outcomes, mandates, array migration, or scenario execution was claimed. Live validation remains user-owned.

## Remaining blockers and audit completion

1. Obtain the missing typed League decision/mission and route/event probability scenarios before making any AI balance or selection-frequency claim.
2. Review the shared status-window production render and classify its overlap findings; visually review the Formables production render in the supported read-only GUI path.
3. Retain live runtime/save-load validation with the user; this audit did not and must not substitute for that evidence.
4. Keep whole Event 006 at HOLD / PARTIAL until its broader completion requirements are independently satisfied.

No gameplay or localization patch, AI/weight/cost/availability edit, scenario change, GUI edit, plan handoff, or commit was made in this pass. Skills used: chaos-redux-decisions-missions, chaos-redux-subagents, chaos-redux-events, chaos-redux-focus-trees, and chaos-redux-scripted-gui.
