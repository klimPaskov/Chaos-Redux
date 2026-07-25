# Event 013 Natural Disasters implementation-depth addendum

> Disposition, 2026-07-10: implemented and folded into the live Event 013 package. The gaps and blockers below describe the pre-closure snapshot. Current evidence and residual validation boundaries are recorded in `013_implementation_validation_notes.md`; this addendum is retained as the accepted improvement-loop design record. The earlier B-001 wording that required the warning action to choose the fine follow-up route is superseded by `013_full_improvement_loop_2026-07-11.md`, which explicitly requires preparation to mitigate an independently resolved hazard and records warning-route independence as an acceptance case.

> Historical snapshot: the incomplete state and blocker tables below describe the pre-closure audit only. They remain useful as improvement-loop provenance but must not be read as current missing implementation. Use `013_event_completion_final_audit.md` and `013_implementation_validation_notes.md` for current status.

Status at snapshot: implementation planning only
Date: 2026-07-10
Implementation state at snapshot: incomplete
Scope owner: main Event 013 implementation agent

This addendum audits the accepted Event 013 source pack against the live implementation and converts the remaining depth gaps into bounded implementation tranches. It does not authorize a new disaster family, another event family, a focus tree, a country package, a generic global disaster agency, a terminal world-end branch, or a second large UI system.

The controlling design sources remain the accepted files under `docs/specs/013_natural_disasters_specs/`. In particular:

- Parts 1-5 control the core system, reusable engine, families, aftermath, evolutions, cluster, and scenario behavior.
- Part 6 controls accepted presentation, achievement, and super-event roles.
- Part 7 controls AI, balance, and acceptance behavior.
- Part 8 controls the 25 family mini-specs.
- Part 9 controls the abnormal path GUI and its static/animated sprite contract.
- Part 10 controls aftermath decision and mission depth.
- `matrices/013_disaster_call_contract.md` controls the caller contract.
- `implementation_readiness/013_acceptance_gate_matrix.md` and `013_validation_scenario_matrix.md` control completion proof.
- `docs/super_events/013_natural_disasters_super_event_research_addendum.md` supersedes the earlier four-route disposition wherever the two documents conflict; the accepted package contains six super-event roles.

Working architecture notes and old subagent handoffs are evidence of intent or prior state, not proof that the live implementation satisfies the accepted sources.

## Audit verdict

Event 013 has a substantial working backbone, but it is not source-pack complete. The strongest implemented surfaces should be preserved: the public wrapper, persistent delayed queues, future-dated jobs, 25 family ids and profiles, Deaths integration, regional spread, aftermath phases, foreign relief, cluster/scenario calls, ten achievement registrations and runtime trackers, six super-event script slots, and the Evolution III/manual-abnormal GUI gate.

The blocking depth gaps are concentrated rather than architectural:

| Area | Live strength | Completion blocker |
| --- | --- | --- |
| History ownership | One call-level history write is structurally separated from delayed jobs. | Needs trace proof for normal, cluster, scenario, external, and follow-up paths before completion. |
| Caller API | Wrapper, target modes, family, severity, sequence, news/report/aftermath/chain policies, and several scales exist. | No family-group call, no weaponized-caller cost proof, no supply scale, the recovery scale is persisted but unused, and several enums/bounds are not rejected. |
| Family profiles | All 25 ids have unique lethality, building priorities, reports/news text, warning entry, and default chain. | Only 25 of 75 accepted warning directions exist; targeting, state modifiers, cards, AI choices, and follow-up routes remain materially generic. |
| Evolutions | The accepted sequence ranges and Evolution II regional spread exist; abnormal families are non-terminal. | Evolution I promotes broad calls to severe rather than widening activity with only slight severity pressure. Target suitability is still mostly random. |
| Aftermath | Rescue, stabilization, reconstruction, chain prevention, relief, full/partial/failure outcomes, and resilience exist. | Active caps are fixed, aftermath policy variants are not behaviorally distinct, recovery scale is dead, repeated impacts cannot merge/supersede, and owner/control changes can strand state work. |
| Reports/news | Twenty-five family event routes and family-specific text exist; affected-country delivery is delayed. | The event script references 14 report and 24 news sprite basenames, but `interface/013_natural_disasters.gfx` registers none of them. |
| Abnormal GUI | Correctly gated to abnormal cards and uses eight real animated/static pairs. | It sorts active cards by urgency rather than showing sequence arrival order or predicted path. Eight required static GUI sprites are missing. |
| Super-events | Six slots, researched text, audio ids, tracks, once-only flags, and same-sequence suppression exist. | Two of six final DDS images are absent, and the delayed-tsunami gate does not prove a separated multi-coast chain. |
| Achievements | Ten accepted ids, localisation, and substantial sequence-bound runtime hooks exist. | All 30 accepted icon files are absent and every route still needs end-to-end scenario proof, especially operational-route and death-threshold disqualifiers. |
| Documentation/catalog | Specs, plans, workbook rows, manifests, and a mechanic document exist. | Several handoffs are stale and the mechanic document currently claims absent sprites, complete path order, and complete API behavior. Workbook statuses correctly remain incomplete. |

## Preserve these implementation decisions

The closure pass should extend the current system rather than replace it.

1. Keep `chaosx.nr13.1` as the Event 013 root and keep the event repeatable and non-terminal.
2. Keep `call_natural_disaster` as the only public gameplay entry point. External systems must not duplicate Deaths, damage, report, aftermath, or chain logic.
3. Keep delayed work in persistent affected-country queues with exact state payloads and distinct future dates.
4. Keep one Event 013 history row at the logical call level. Warning, impact, report, news, follow-up, reassessment, and recovery jobs remain silent subwork.
5. Keep the 25 accepted family ids. Expand their profiles and branches; do not add substitute families.
6. Keep Event 046 inert, Event 051 separate with heat overlap exclusion, and Event 099 inert unless a later explicit decision accepts the narrow dust bridge.
7. Keep the existing Natural Disasters cluster as five logical Event 013 members and keep Disaster Barrage as one non-terminal reusable-API call.
8. Keep normal disasters in the decision category. The custom map remains limited to Evolution III abnormal paths and manual Maximum Barrage cards.
9. Keep the six accepted researched super-event roles and the ten accepted achievement routes. Do not add weaker substitutes.

## B-001: close all 25 family mini-specs

This is the largest accepted content blocker. The live decision file contains exactly one warning decision per family. Part 8 specifies three directions per family, so 50 warning directions are absent. Every current warning adds the same preparation-score unit, while its family profile then feeds common death/building reduction. That gives useful baseline behavior, but not the three different preparation tradeoffs promised by the mini-spec.

The table below is a closure index, not replacement design. Retain the live warning and implement the two missing accepted directions. The live-default column records current behavior; the final column is the accepted route set that must become context-selectable.

| Family | Retain live warning | Add the two missing warning directions | Live default chain | Accepted follow-up route set |
| --- | --- | --- | --- | --- |
| Earthquake | rail crews | open squares; port-withdrawal watch | aftershock | aftershock, seismic landslide, offshore tsunami, urban fire |
| Flood | move rolling stock | raise embankments; clean-water stores | disease | waterborne disease, refugee pressure, crop loss, dam-failure flash |
| Tropical cyclone | close ports | disperse aircraft; coastal evacuation | supply collapse | storm surge, inland flood, disease, supply collapse |
| Extreme wind | pause exposed trains | anchor aircraft; secure roofs | supply collapse | wildfire spread, rail derailment, transport collapse |
| Tornado outbreak | shelter belt | spotter line; clear airfields | refugee pressure | severe-thunderstorm tail, wildfire line, refugee pressure |
| Thunderstorm | lightning patrol | ground aircraft; drainage crews | wildfire | hailstorm, flash flood, wildfire ignition |
| Hailstorm | cover aircraft | cover depots; food reserve | famine pressure | ration pressure, airfield accident, thunderstorm return |
| Blizzard | fuel corridor | rail snow crews; winter shelter | supply collapse | extreme cold wave, supply collapse, refugee exposure |
| Extreme cold wave | heat shelters | protect water lines; frontline rotation | refugee pressure | blizzard follow-up, shelter disease, supply collapse |
| Extreme heat wave | water points | shift work hours; fire watch | disease | wildfire, drought, unrest |
| Drought | water trains | crop salvage; firebreaks | famine pressure | famine pressure, wildfire, refugee pressure |
| Sandstorm and dust storm | convoy spacing | seal airfields; cover water stores | supply collapse | drought, disease, heat wave only when Event 051 compatibility permits |
| Wildfire | firebreaks | evacuation columns; protect power lines | wildfire | smoke illness, refugee pressure, drought feedback |
| Dry mass movement | slope watch | pass closure; mine evacuation | supply collapse | supply isolation, aftershock damage, resource shutdown |
| Wet mass movement | valley evacuation | bridge watch; channel clearance | disease | flood renewal, disease, supply isolation |
| Volcanic eruption | exclusion zone | observatory watch; ash-airfield closure | lahar | ashfall, lahar, tsunami, famine pressure |
| Ashfall | cover machinery | ground air traffic; cover food and water | famine pressure | respiratory deaths, famine pressure, lahar |
| Lahar | valley sirens | bridge cordon; channel clearance | disease | flood, disease, supply isolation |
| Tsunami | inland corridors | coast-withdrawal alarm; close quays | refugee pressure | disease, refugee pressure, naval disruption, coastal famine |
| Storm surge | sandbag low roads | quay closure; evacuate marsh edge | disease | flood, disease, port-supply collapse |
| Meteor impact | crater evacuation | observatory tracking; fire perimeter | refugee pressure | wildfire, dust veil, tsunami, meteor shower |
| Meteor shower | shelter lights-out | observer net; fire patrols | wildfire | wildfire, transport collapse, meteor impact |
| Whole-earth rupture | global rail stand-down | coastal tide watch; regional triage | tsunami | global aftershocks, delayed tsunami chain, regional landslides, urban fire |
| Massive eruption | food corridors | exclusion ring; air shutdown | lahar | regional ashfall, lahar, tsunami, famine pressure |
| Moving storm corridor | rail reroute | path forecast; layered evacuation | supply collapse | tornado outbreak, flood, wildfire, storm surge |

For every row, the implementation tranche must also close the following Part 8 fields rather than only adding buttons:

- Apply the exact family target-fit direction. Coast restrictions already exist for cyclone, tsunami, and storm surge, but the broader pool still lacks meaningful terrain, population, transport, industry, agriculture, resource, winter, dry, volcanic, and path suitability.
- Persist and display `family_group`, linked states when relevant, impact signature, severity, damage profile, death-driver summary, warning result, chain risk, recovery priority, active modifier, and failure date. The current card exposes family, state, phase, damage summary, recovery need, chain text, and scores, but does not expose an actual warning outcome or exact known-death result.
- Replace severity-only state disruption with family-weighted modifier profiles. Both live dynamic modifiers currently receive the same supply, movement, attrition, repair, and resource fields for every family at a given severity. Family damage flags do not prevent irrelevant penalties; for example, a family with no resource direction can still receive the generic local-resource penalty.
- Turn the route sets above into family-conditioned alternatives rather than one default chain per family. Route choice must use family and valid target context, with severity and recovery state influencing whether the route is escalated or allowed to mature. The warning action must remain an independent mitigation result and must not select or rewrite the resolved hazard; `013_full_improvement_loop_2026-07-11.md` is the controlling disposition for that separation. `political_shock` remains an accepted chain family and should be used only for high-death/failed-recovery conditions, not added to every disaster.
- Give AI the same three warning choices and the same route-aware preparation model as the player. Existing per-warning `ai_will_do` modifiers are useful and should be retained, but one available action cannot express the Part 8 priorities.
- Keep the current distinct report and news text. Complete visible sprite registration and any source-matrix-required family identity; do not create 25 redundant images merely to inflate asset count.

### Warning implementation rules

1. Three family warnings are alternatives for the same warning window, not three purchases that stack into automatic safety.
2. Each choice needs a distinct physical cost, protected system, chain effect, AI weight, localisation, and outcome field. Costs should use manpower, equipment, trucks, trains, convoys, fuel, stability, war support, temporary production/supply/air activity, or command attention as the Part 8 row directs.
3. Audit cost localisation against the actual trigger and completion effects. The current shelter wording mentions vehicles and fuel where the effect does not deduct them, while field-team affordability may accept support equipment or trucks even when the cost text implies both.
4. A successful preparation reduces risk; it never erases a serious impact.
5. All tuning belongs in script constants or reusable helpers. Do not copy numeric costs into 75 decisions.

## B-002: finish and harden the caller API

The current public wrapper is the correct integration surface, but the live contract is narrower and more permissive than the accepted one.

### Required contract additions

- Add a family-group selector that resolves only within the requested accepted group while preserving the evolution gate and heat exclusion.
- Add `caller_cost_checked` handling for weaponized external calls. Random Event 013, cluster, and scenario calls do not need a caller cost proof; deity, hostile actor, and equivalent enemy-targeting calls must be rejected without it.
- Add a supply-disruption scale as required by the current implementation brief. Apply it to state disruption, neighboring falloff, and relevant supply-collapse routes rather than treating it as a cosmetic stored value.
- Consume the existing recovery scale in initial recovery burden, phase thresholds, reassessment pressure, and neighbor aftermath falloff.
- Differentiate `none`, `light`, `normal`, `full`, and `emergency` aftermath policies. The live code currently treats them primarily as none versus non-none.
- Preserve the accepted death, building, warning, chain, report, news, and log options.

### Required validation

The wrapper must reject, with a stable rejection reason, rather than silently coerce:

- unknown caller types or caller/event combinations;
- unknown family ids or family groups;
- target modes outside the enum;
- selected country/state/region calls without a valid target;
- selected states that are not valid for the requested ownership/control contract;
- unknown severity, sequence, news, report, aftermath, chain, or log policies;
- exact hit counts outside the accepted per-mode cap;
- negative, zero-where-invalid, or unbounded scale overrides;
- abnormal families without Evolution III access or the explicit manual Maximum bypass;
- a weaponized external target without caller cost proof, cooldown, or target legitimacy;
- Event 013 heat while Event 051 heat is active;
- same-day duplicate or globally cooled abnormal requests.

`report_policy = global` must have defined global behavior. Sending only to the affected owner while forcing news is not equivalent to a global report. Either implement its accepted audience explicitly or rename/redefine the enum in the controlling contract before claiming it.

### API proof cases

The parent implementation should exercise one accepted and one rejected call for every enum, plus these cross-system cases:

1. normal root event, direct Event 013 log ownership;
2. Natural Disasters cluster call, one Event 013 row per logical season;
3. Disaster Barrage scenario call, scenario history ownership and no Event 013 duplicate;
4. external affected-country report with the caller in another country;
5. weaponized enemy call with and without cost proof;
6. selected state under occupation or after ownership/control transfer;
7. Event 051 heat exclusion;
8. Evolution III abnormal request during and after global cooldown;
9. exact-count request at the legal maximum and one above it;
10. family-group request at each evolution stage.

## B-003: replace mostly random targeting with family suitability

The current family eligibility rules materially distinguish only coast-bound families and the Event 051 heat exclusion. Most families otherwise use a random country/state path. This fails the source-pack requirement that dense, industrial, transport, agricultural, dry, winter, volcanic, coastal, and path disasters select plausible targets.

Implement a bounded family suitability layer inside call resolution. It must not use daily/weekly/monthly all-country scans.

- Score only the caller-provided scope and the bounded candidate states considered by the call.
- Use existing state/country facts as proxies: population, capital, industry, infrastructure, rail, supply hub, port, airfield, resources, coast, terrain, climate/season where available, war damage, stability, devastation, and unresolved aftermath.
- Preserve randomness among plausible candidates. Suitability is a weight, not a deterministic best-state selector.
- Keep selected target modes strict. A caller that provides an exact valid state should receive that state rather than an unrelated replacement.
- Keep coast, heat-overlap, abnormal access, and duplicate-state guards.
- Persist enough route metadata for abnormal path prediction; do not reconstruct a future route from the urgency-sorted card list.

Target-fit values should live in family profiles or reusable scoring helpers so AI, scenario, external-call, and normal Event 013 paths share the same logic.

## B-004: restore the intended evolution curve

The sequence counts and delays are already aligned:

- baseline: 1-3 hits, 5-10 days;
- Evolution I: 3-6 hits, 4-8 days;
- Evolution II: 8-18 hits, 2-5 days;
- Evolution III: abnormal path behavior, non-terminal.

The needed correction is qualitative. The live severity resolver promotes broad Evolution I random and cluster calls from local to severe. Evolution I is meant to widen the family pool and make seasons busier without turning every impact into a major catastrophe.

Closure requirements:

1. Baseline must retain meaningful building damage and visible Deaths-system loss.
2. Evolution I should add variety, more active cards, and modest pressure while retaining a mixed local/severe distribution.
3. Evolution II must be visibly stronger through deaths, neighboring damage, supply disruption, famine, disease, refugee pressure, and recovery strain, not merely more frequent.
4. Evolution III must use abnormal path families, route visibility, severe multi-state damage, researched super-event gates, and no `world_end` behavior.
5. Disaster Barrage Maximum may bypass abnormal cooldown only for that manual call and must not fake a natural Evolution III milestone.

## B-005: make aftermath capacity, policy, and lifecycle real

The existing phase engine is worth retaining, but three accepted behaviors are missing.

### Dynamic active caps

The live system exposes three rescue, two stabilization, and two reconstruction slots regardless of country capacity. Constants already exist for base, weak-country, major-country, and barrage cap adjustments but are not consumed.

Implement a single cap-refresh helper that derives per-country caps from accepted capacity inputs and the active scenario state. Recompute lazily when a card opens or closes, before a slot is reserved, when a phase changes, when foreign relief changes capacity, and when a Maximum Barrage begins or ends. This naturally re-reads current major/weak status without a world scan. Weak countries must still have at least one useful route; major countries should gain capacity without making all simultaneous disasters trivial.

### Policy and recovery burden

- Apply aftermath policy and recovery scale to initial burden and phase thresholds.
- Use family and damaged-system identity to select recovery priorities, rather than giving every family the same score path.
- Preserve full, partial, and failure outcomes. A partial close must not count as full reconstruction for achievements.
- Make foreign relief alter the intended phase/capacity inputs without bypassing physical cost or creating free recovery.

### Lifecycle and target changes

- Decide and implement the accepted supersession rule for a second impact in a state with an open card: merge/refresh the card for the same sequence/family or replace it only when the larger regional aftermath explicitly supersedes it. Do not silently skip all repeated impacts.
- Add narrow cleanup/transfer handling for state owner/controller changes, annexation, capitulation, and invalid targets. Jobs and cards currently remain in the original country-owned queues and can strand missions after a state changes hands.
- Close or transfer the state card, mission slots, abnormal-card membership, report recipient, and achievement ledger together. No daily world scan is allowed.
- Keep explicit cleanup for temporary flags, active modifiers, arrays, and event targets.

## B-006: make the abnormal GUI a path map rather than an urgency list

The map is correctly limited to abnormal cards and already has five live layers with animated/static pairs. Its current card builder sorts up to five owned active cards by urgency. The localisation then calls that ordering a path. This does not prove arrival order, next-hit prediction, or route geography.

Implement a sequence-owned route ledger at scheduling time with:

- sequence id and path type;
- ordered segment index;
- exact scheduled impact date;
- target state and linked state/region;
- segment status: forecast, warning, pending, impacted, chain risk, recovery, closed;
- confidence or known/unknown state where a forecast is intentionally imperfect;
- primary and secondary chain markers.

The GUI should render the selected sequence in chronological segment order. Urgency can still determine which sequence or card is selected first, but it must not overwrite physical route order. When more than five segments exist, show the next five relevant segments and an explicit remaining count; do not omit segments while claiming a complete path.

Also expose the shared aftermath fields that are currently absent or only implicit: warning result, known-death result or honest direction, linked states, active modifier, and failure date. Normal disasters must remain fully playable through the decision category without this GUI.

The following required static sprites are absent and must be produced, installed, registered, and manifest-tracked:

- `GFX_013_abnormal_disaster_panel`;
- `GFX_013_abnormal_disaster_panel_damaged`;
- `GFX_013_disaster_card_frame`;
- `GFX_013_map_marker_impact`;
- `GFX_013_map_marker_chain_risk`;
- `GFX_013_foreign_relief_badge`;
- `GFX_013_recovery_progress_frame`;
- `GFX_013_recovery_progress_fill`.

Keep the eight existing real frame-sheet/static pairs. Every animation remains optional at runtime only because its static fallback is real; a missing fallback is a blocker, not permission to use a transform-only substitute.

## B-007: finish visible presentation assets and registrations

The asset copy layer contains much usable art, but gameplay registration and accepted identity coverage are incomplete.

### Blocking registrations

`interface/013_natural_disasters.gfx` currently registers the eight abnormal animation pairs but no `GFX_report_event_nd_*` or `GFX_news_event_nd_*` sprites. The event file references 14 report and 24 news sprite basenames. Register every referenced basename against a valid DDS. Do the same inventory for live decision/category and Event 013 idea sprite names before declaring those surfaces complete.

The abnormal notification sprite `GFX_report_event_nd_regional_aftermath` must also resolve to a registered asset.

### Blocking asset production

- Produce the eight static abnormal-GUI assets listed in B-006.
- Produce and install the two missing accepted super-event DDS images for the first abnormal-age reveal and the delayed multi-coast tsunami chain. Four family-role DDS files already exist.
- Produce all completed, grey, and not-eligible variants for the ten accepted achievement ids: 30 files total. The current folder contains an obsolete eight-id set; none of the accepted final basenames exists.
- Reconcile the decision, category, idea, report, and news coverage against the accepted Part 6 prompts and the Part 8 directions. Reuse existing art where the accepted identity permits it. Missing accepted identities require real source/processed/DDS production and manifest entries; no placeholder or fallback filename is allowed.
- Reconcile DDS formats and alpha handling recorded in `013_asset_audit.md` before final presentation sign-off.

Every produced asset needs source, processed PNG, final DDS, prompt/provenance, dimensions, sprite name, live reference, status, and contact-sheet or visual-review evidence where the asset skill requires it.

## B-008: tighten the six super-event gates

Keep exactly the six accepted roles:

1. first natural abnormal age;
2. whole-earth rupture;
3. massive eruption;
4. meteor shower/skyfall;
5. moving storm corridor;
6. delayed multi-coast tsunami chain.

The first five gating patterns are structurally present. The delayed-tsunami gate is too broad: it can fire from a tsunami-family abnormal sequence with enough planned hits without proving separated coasts or a delayed independent major arrival.

Add explicit sequence state for the tsunami-chain role:

- qualifying geological, volcanic, or ocean-impact origin;
- at least two separated coastal target groups or strategic regions;
- a delayed major arrival distinct from the origin impact;
- accepted severity and sequence-size thresholds;
- the sequence has not already fired a family-role super-event;
- the global role has not already fired.

The gate must read that sequence state, not infer it from total planned hits. Preserve research-gated text/audio, settings-aware playback, once-only flags, and same-sequence suppression. Install the two missing images before claiming all six packages complete.

## B-009: finish achievements through route proof, not registry count

The ten accepted achievements and many runtime hooks now exist. Older handoffs that say no `achievement_nd_*` runtime hooks exist are stale. Completion still requires icon production and scenario proof.

For each route, prove start, progress, success, and every disqualifier against one exact sequence:

| Route | Critical proof |
| --- | --- |
| All Clear, All Accounted For | Every tracked severe-season card fully reconstructs; failed deadline, partial abandonment, or unrelated cards cannot satisfy it. |
| The Tide Stops Here | A qualifying delayed geological tsunami is prevented before arrival, or the route fails on a qualifying major second death spike. |
| The Trains Came Through | All tracked regional transport cards recover while the capital supply route remains operational for the whole attempt. |
| Bread Beneath the Ash | Every major ashfall card closes before famine matures. |
| No World Weather Office | Four normal family groups report to the affected country without the global-announcer policy; news alone must not count. |
| Keep the Runways Lit | The full meteor-shower sequence ends with controlled capital, primary supply route, and required airfield network intact. |
| Brace the Broken Earth | Required rupture cards recover before a major aftershock or delayed tsunami matures. |
| All Sirens at Once | Maximum Barrage remains non-terminal, preserves the capital route and one port/rail corridor, and fully reconstructs the required cards before deadline. |
| Every Cot Accounted For | Severe refugee pressure completes the required shelter/evacuation/route work without death, camp-disease, or border-camp failure. |
| An Atlas Bound in Dust | Full reconstruction records exactly the eight accepted normal-family groups; abnormal families and partial cleanup do not substitute. |

The central 100,000 second-wave threshold, 50,000 refugee threshold, two-airfield requirement, and other live constants are balance choices that now exist. They are not a design blocker, but they remain a balance-validation gate. Validate that each can fail and succeed under plausible accepted scenarios.

Produce the 30 exact achievement icon files and register them under the accepted ids. Do not reuse the obsolete eight-id basenames as invisible substitutes.

## Documentation and source-of-truth repair

Documentation must describe the live state honestly during implementation.

### Current overclaims to correct

`docs/events/013_natural_disasters.md` exists, but several statements currently outrun the code:

- it says the API validates all presentation policies and scaling overrides, while several enums/bounds are not validated and recovery scale is unused;
- it presents all family target priorities as implemented, while most target selection remains random beyond coast/heat gates;
- it says the abnormal path queue names threatened states in order, while the GUI rebuilds an urgency-sorted active-card list;
- it says all six super-event roles have image sprites, while only four final Event 013 super-event DDS files exist;
- it says accepted achievement icon triplets live under `gfx/achievements/`, while none of the 30 accepted files exists;
- it describes report/news, decision/category, idea, and static abnormal GUI registrations as complete, while the corresponding Event 013 sprite definitions are absent.

Correct these claims as each tranche lands. Do not leave the document aspirational while presenting it as implementation documentation.

### Handoff disposition

Create a short source-of-truth/disposition section in the mechanic documentation or the final completion report:

- mark the repo explorer map's no-live-implementation statements superseded;
- mark cluster handoff API gaps resolved where the live wrapper now passes family, severity, sequence, target, news/report, aftermath, chain, and log values;
- update the decision handoff's stale variable names and hooks;
- mark the achievement handoff's no-runtime-hook claim superseded while retaining its icon and route-proof blockers;
- update the asset manifest/GFX handoff to show the eight animation pairs as wired and the static GUI, report/news registrations, two super-event images, and ten achievement triplets as open;
- state that the later six-route super-event research addendum controls over the earlier four-route recommendation.

After implementation facts stabilize, align the Event 013, Cluster 5, and SCN-007 rows in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Their current incomplete/testing statuses are accurate and should not be promoted early.

## Implementation order

The dependencies make the following order safest:

1. **API and targeting correctness:** finish contract validation, cost proof, family groups, supply/recovery scaling, target legitimacy, and suitability scoring.
2. **Family depth:** add the missing 50 warnings, family modifier profiles, route alternatives, card fields, and three-choice AI behavior.
3. **Evolution and aftermath:** correct Evolution I severity behavior, consume capacity caps/policies/scales, implement supersession and ownership/control cleanup.
4. **Path presentation:** persist chronological route metadata and update abnormal GUI/card fields.
5. **Assets and registration:** complete sprite registration, eight static GUI assets, two super-event images, and 30 achievement files, then reconcile manifests.
6. **Super-event and achievement gates:** tighten delayed-tsunami qualification and execute every route/disqualifier scenario.
7. **Integration and balance:** exercise normal, cluster, scenario, external, overlapping, and affected-report paths; tune only through constants.
8. **Documentation/catalog/audits:** repair overclaims, update disposition maps and workbook rows, then run the appropriate Event 013, localisation, decision/mission, and asset completion audits.

Each tranche should be implemented and committed separately. A tranche is not complete if its localisation, AI, assets, docs, or relevant scenario proof are deferred.

## Completion proof matrix

The final implementation report needs evidence for these scenarios. Static structure checks alone are insufficient.

| Scenario | Required observable result |
| --- | --- |
| Baseline ordinary season | 1-3 future-dated impacts, meaningful building/death loss, affected-country report after impact, visible card, no duplicate history row. |
| Evolution I season | 3-6 impacts with wider family mix and card pressure, but a mixed local/severe profile rather than universal severe promotion. |
| Evolution II regional season | 8-18 impacts, neighboring falloff, stronger deaths/supply/recovery pressure, and visible famine/disease/refugee routes where conditions qualify. |
| Evolution III abnormal path | Ordered/predicted segments, route-specific GUI, abnormal damage, static-mode readability, qualifying super-event behavior, no world end. |
| External affected report | A non-owner caller schedules a valid impact and the affected country reliably receives the delayed report. |
| Two overlapping sequences | No same-day jobs within either sequence, no queue payload overwrite, correct report/history ownership, independent completion. |
| Every family | Three warning alternatives, target-fit behavior, family-weighted modifier, exact card identity, AI choice, report/news presentation, and at least two context-selectable chain outcomes where the mini-spec provides them. |
| Cluster 5 | Five logical Event 013 slots use the wrapper and record one Event 013 row per accepted logical member. |
| Disaster Barrage | All five type choices and four intensities map correctly; Maximum is abnormal, recoverable, and non-terminal. |
| Related events | Event 046 remains inert, Event 051 does not stack heat, Event 099 remains a placeholder unless explicitly accepted as a narrow API bridge. |
| Six super-events | Correct sequence role, research-approved presentation, once-only/same-sequence behavior, six valid images, and settings-aware audio. |
| Ten achievements | Each route succeeds once, each disqualifier blocks once, counters remain sequence-bound, and all icon variants display. |
| Ownership/control change | Pending job/card/mission/GUI/achievement state transfers or closes without stranded arrays or modifiers. |

If a runtime value cannot be proven from the existing effects, use narrow temporary debug logging around the exact call/sequence/card values, capture the result, and remove every debug line before completion.

## Explicitly optional or rejected expansion

The following items are not blockers for the accepted Event 013 package:

- activating Event 046;
- giving Event 099 a standalone sandstorm system;
- adding a new family beyond the accepted 25;
- adding a terminal world-end outcome;
- adding super-events beyond the accepted six;
- adding achievements beyond the accepted ten;
- adding focus trees, countries, generic agencies, or another scripted GUI;
- replacing the current queue engine with a more elaborate architecture solely to match an old planning diagram;
- adding memorial or long-term rebuilding flavor from the mechanic document's future-plans section.

The narrow Event 099 dust bridge remains optional and requires an explicit acceptance decision before implementation. No fallback or simplification is proposed in this addendum.

## Definition of complete

Event 013 is complete only when:

- all 25 mini-spec rows have their three warnings, target fit, distinct modifier/card identity, AI behavior, reports/news presentation, and route alternatives;
- the reusable API validates its full accepted contract and consumes every advertised scale;
- all normal, cluster, scenario, and external calls preserve one logical history row and reliable affected-country reports;
- evolution pacing and severity match the accepted curve;
- aftermath capacity, policies, repeated impacts, invalid targets, and ownership/control changes are handled;
- the abnormal GUI shows real ordered/predicted paths and works in static mode;
- all required sprites and final assets are present, registered, and manifest-tracked;
- all six super-events and ten achievements pass their qualifying and disqualifying scenarios;
- related-event separation, cluster/scenario behavior, documentation, manifests, and workbook rows match the live implementation;
- final specialist audits find no unresolved gameplay, decision/mission, localisation, asset, achievement, or event-completion blocker.
