# Event 021 Random Civil War completion requirement audit

Date: 2026-09-06

Auditor: `chaosx_event_completion_auditor`

Mode: read-only completion audit

Overall disposition: **INCOMPLETE AND RELEASE-BLOCKED**

The current implementation is a substantial source implementation with a complete Event 021-owned static asset package, normal decision and mission definitions, cluster and scenario registration, six achievement definitions, extensive lifecycle helpers, and current nonfinal catalog rows.

It does not meet the accepted Event 021 completion standard because the release gate remains closed, the Event 006 player-facing package is still explicitly unavailable to Event 021-origin actors, accepted weighted severity is implemented as a deterministic ladder, Evolution II is not propagated to crises opened after activation, several presentation events and both news events have no caller, reused Event 006 assets and portraits remain uncertified, required probability and event MCP evidence is incomplete, and all user-owned live-game, save/reload, lifecycle, and performance gates remain open.

No gameplay file was edited during this audit.

## Classification

- **Proven**: current source, asset, documentation, or generated artifact directly demonstrates the requirement within the stated limit.
- **Incomplete**: the accepted requirement is absent, contradicted, stale, or only partly implemented in current files.
- **Weak/indirect**: relevant source exists, but the required engine, scenario, lifecycle, comparison, or consumer evidence does not.
- **Blocked**: a required external route, user-owned validation gate, missing dependency, or unresolved input prevents completion evidence.

## Governing evidence reviewed

- `AGENTS.md`.
- Every file under `docs/specs/021_random_civil_war_specs/`, including the ten-part source specification and its objective, integration, evolution, settlement, asset, validation, and acceptance requirements.
- The Event 006 specification set under `docs/specs/006_independence_wave_specs/`, its current status and package contract, and current Event 006 implementation surfaces relevant to Event 021 reuse.
- Current Event 021 events, scripted effects, scripted triggers, constants, decisions, decision categories, AI strategies, on-actions, achievements, localisation, scripted localisation, GFX definitions, event-log and event-details integration, scenario and cluster registration, documentation, plans, asset manifests, validation records, and catalog workbook/exports.
- Required offline wiki references: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`.
- Installed vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation`, including event, effect, trigger, on-action, scripting-concept, localisation, modifier, and AI documentation relevant to civil-war creation, event targets, war/annex callbacks, decisions, missions, variables, and script constants.
- Vanilla source precedents for event dispatch, civil-war effects, decisions/missions, AI weighting, on-actions, and war/annex lifecycle behavior.

The wiki and vanilla documentation establish syntax and engine contracts; they do not prove that the current Event 021 runtime paths execute correctly.

## Original objective requirement audit

| Requirement | Classification | Current evidence and limit |
|---|---|---|
| Event identity is ID 21 with entry `chaosx.nr21.1`, Minor Repeatable, Chaos tier 1, and Wars cluster Medium severity. | **Proven** | The entry namespace and root are defined in `events/021_random_civil_war.txt:1-20`. Event catalog row 21 in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` records Minor Repeatable and Chaos tier 1. `common/scripted_effects/chaosx_event_cluster_effects.txt:1345-1351` registers Event 021 in Wars with Medium severity, and `common/script_constants/event_cluster_constants.txt:128-130` reserves the related Wars rows. |
| The event remains unavailable until the rework is complete. | **Proven** | `common/scripted_effects/021_random_civil_war_parent_effects.txt:37` clears `random_civil_war_rework_ready`; no current source sets it. Gate consumers remain in the parent effects and Event 021 triggers. This proves the safety hold, not feature completion. |
| The completed event can auto-fire for eligible Calm World countries. | **Blocked** | The release gate prevents normal auto-fire. The current catalog status is `Needs Testing`, and no user-owned live opening is recorded. |
| Entry validation produces either a valid target opening or the no-target branch. | **Weak/indirect** | Target-pool, validation, and no-target source exist, and `chaosx.nr21.17` is defined in `events/021_random_civil_war.txt`. The release gate and missing current lifecycle render prevent engine proof. |
| Hidden Fracture Pressure and visible State Authority drive the crisis. | **Weak/indirect** | Constants, variables, ideas, scripted effects, scripted localisation, and decision costs are present across `common/script_constants/021_random_civil_war_constants.txt`, `common/ideas/021_random_civil_war_ideas.txt`, and the Event 021 effect and localisation files. Continuous runtime updates, minimum-authority tracking, successor transfer, and UI truth remain live-game gates. |
| Six distinct routes exist: ideological, legal/constitutional, regional, Event 006 full package, command breakdown, and same-tag split. | **Weak/indirect** | Route selection, role setup, flags, localisation, and archetype-specific effects exist in the Event 021 trigger/effect family. Event 006 reuse is incomplete as described below, and route-by-route runtime outcomes are not certified. |
| Automatic archetype selection is weighted and auditable. | **Weak/indirect** | `common/scripted_effects/021_random_civil_war_parent_effects.txt:1070-1077` contains a weighted `random_list` for archetype selection. A complete current named-scenario probability certificate was not produced. |
| Automatic severity uses the accepted weighted pressure-and-viability model. | **Incomplete** | `common/scripted_effects/021_random_civil_war_effects.txt:541-570` implements a sequential deterministic Limited-to-Critical ladder, with one-state and all-island forcing. `event021_parent_select_severity` only invokes that ladder. This conflicts with the accepted weighted-severity plan and with older probability claims. `docs/plans/021_random_civil_war_plans/active_repair_ledger_2026-09-02.md:50-51` records the discrepancy. |
| One-state countries and invalid higher-severity geometries safely collapse to Limited. | **Proven in source** | The deterministic selector forces one-state and all-island cases to Limited in `common/scripted_effects/021_random_civil_war_effects.txt:541-570`. Engine execution remains part of the blocked live matrix. |
| Territory is connected, supplied, capital-aware, and leaves viable remnants. | **Weak/indirect** | State-selection and opening helpers exist in the Event 021 effect family and use bounded candidate arrays and viability checks. No current engine state-flow artifact or user live evidence proves connectivity, supply access, capital treatment, or remnant viability across the required cases. |
| Land forces, stockpiles, navy, and air are scaled dynamically for each route and severity. | **Weak/indirect** | Dynamic allocation helpers and tuning constants exist. No route-by-route engine fixture or live balance record proves complete transfer, valid unit placement, naval/air behavior, or absence of destructive edge cases. |
| The normal decisions interface supplies 3-5 actions per phase and 1-3 missions with bounded resources and useful AI. | **Proven in source; runtime weak** | `common/decisions/021_random_civil_war_decisions.txt` defines twenty-one actions/missions, including three timed missions at lines 710, 753, and 790, and each surface has `ai_will_do`. `common/decisions/categories/021_random_civil_war_categories.txt` uses the normal decisions interface. Availability, target selection, timeout effects, cancellation, exploit resistance, and cleanup have no final decision-mission runtime audit or user evidence. |
| Event 006 reuse supplies a complete admitted country package without starting Event 006 or incrementing its global lifecycle. | **Incomplete** | The 32-package Event 021 adapter allowlist and package capture/release maps exist in `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt` and `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt`. Internal package identity is recognized by `is_independence_wave_package_content_active` in `common/scripted_triggers/006_independence_wave_triggers.txt:38-53`. However, player-facing focus and decision surfaces still require strict Event 006 origin through `is_independence_wave_event6_local_content_active` at lines 29-36. The focus tree uses that strict gate at `common/national_focus/006_independence_wave_focus.txt:40-45`, and many aggregate decisions and category registrations use it or the stricter player-surface predicate. Current comments at `common/scripted_triggers/006_independence_wave_triggers.txt:56-67` explicitly say Event 021 adapter receipts never publish Event 006 categories, missions, costs, queues, or history. This directly contradicts the Event 021 objective. |
| Event 006 reuse is origin-neutral, idempotent, and does not create Event 006 events, evolution, league, or count side effects. | **Weak/indirect** | Dedicated Event 021 receipt flags and internal setup predicates exist and explicitly avoid `independence_wave_active_origin`. Source intent supports side-effect isolation. Idempotence and absence of all global side effects are not engine-certified, and the player-facing package is withheld rather than fully adapted. |
| The Event 006 reused package preserves its focus tree, decisions, formables, AI, characters, units, ideas, flags, and package assets. | **Incomplete / blocked** | The current strict player-facing origin gates prevent the promised tree and decision surface for Event 021 actors. `docs/assets/021_random_civil_war/validation/reused_event006_asset_audit_2026-09-02.md` and `event006_reused_asset_crosswalk_2026-09-02.md` leave every reused family pending or blocked, identify ten admitted packages without a current mod portrait row, forty-six Event 006 portrait rows with review-pending/source-placeholder uncertainty, orphan rows, and incomplete flag/formable/provenance evidence. |
| Evolution I supports multiple independent active and prefire fronts with lower-weight major-country participation and independent resolution. | **Weak/indirect** | Multi-front arrays, caps, secondary opening helpers, resolution records, and reduced-major tuning exist. Current probability certification, independent multi-front settlement, successor continuity, and the required medium/major live scenarios are absent. |
| Evolution II supplies exposure, support, relief, sponsorship, mediation, and strange incidents to active and future crises. | **Incomplete** | The decision surfaces and supporting effects exist. `event021_parent_propagate_exposure` and `event021_parent_roll_strange_incident` are called only inside `event021_parent_apply_evolution_ii` in `common/scripted_effects/021_random_civil_war_parent_effects.txt:5266-5267`. No caller applies the overlay when a new crisis opens after Evolution II is already active. The strange-incident roll is therefore activation-time only, and its cooldown does not establish the accepted ongoing rare-incident model. |
| Evolution III creates nonterminal global bands, bounded queues, caps, scheduling, and nesting without stealing human control. | **Weak/indirect** | Global scheduler, queue, cap, same-day guard, host recovery, and nesting source exists. `docs/plans/021_random_civil_war_plans/active_repair_ledger_2026-09-02.md` records the source repairs but leaves queue liveness, cursor progression, fairness, cap behavior, nested-human independence, and performance unproven. |
| Wars cluster integration coordinates Events 004, 007, and 021 with reservations, collision prevention, and skip reasons. | **Proven in source; runtime weak** | Cluster registration and constants exist. Event 021 records bounded skip classes for missing actors/targets, role collisions, occupied tags, reservations, caps, generation, and stale state in `common/scripted_effects/021_random_civil_war_parent_effects.txt`. Cross-event collision, cooldown, and fairness scenarios remain unrun. |
| Manual scenario SCN-018 supports four crisis types, four intensities, and Maximum on all eligible normal human countries. | **Proven in source; execution blocked** | `common/script_constants/chaosx_triggerable_scenarios_constants.txt:32` assigns Event 021 to scenario 18. Event 021 constants define four types and intensities, and `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` contains selection, cycling, and dispatch. The 2026-09-06 ticket-count ordering repair is recorded in `docs/plans/021_random_civil_war_plans/subagent_handoffs/scenario_ticket_count_ordering_repair_2026-09-06.md`. The release gate blocks execution and no observed Low/Maximum count evidence exists. |
| Shared individual-crisis target pressure is honored for weighted and fixed-target entry. | **Incomplete / blocked** | Weighted candidate adjustment exists through `adjust_individual_crisis_candidate_ticket_weight`. `apply_individual_crisis_fixed_target_event_pressure` remains undeclared and unconsumed; both the active ledger and the 2026-09-06 scenario repair identify the missing fixed-target contract. Candidate weighting is not an equivalent replacement. |
| Settlements cover government victory, opposition victory, independence, autonomy, coalition, partition, merger, obligations, reconstruction, and recurrence. | **Weak/indirect** | Settlement selectors, treaty effects, reconstruction decisions, obligation arrays, and partition/merger-related effects exist across the parent, settlement, treaty, and decision files. Complete multi-signatory obligations, second-crisis ordering, every outcome's distinct territorial/legal effect, successor adoption, and terminal cleanup are not engine- or live-certified. |
| Ordinary successor promotion preserves unresolved fronts, wars, history, treaty signatories, and legitimate achievement state. | **Incomplete / blocked** | Pre-annex ordering and history transfer were repaired in `common/scripted_effects/021_random_civil_war_parent_effects.txt:3824-3830` and `3869-3878`, with natural victory callbacks in `common/on_actions/021_random_civil_war_cxt_on_actions.txt:47-64`. The helper comments and active ledger correctly state that source pointer transfer does not itself mutate or prove remaining wars. Complete predecessor enemy-roster capture, surviving-war rebinding, signatory succession, and natural annex lifecycle proof remain absent. |
| Cleanup is idempotent, releases reservations and generations, preserves durable recurrence/achievement history, and resets per-crisis state. | **Weak/indirect** | Cleanup, rollback, generation release, command reset, and durable-history exceptions exist. Full cleanup across no-target, failed preflight, every settlement, annexation, recurrence, scenario, and multiple-front routes is not certified. Prior settlement type, obligations, successor state, and second-crisis ordering remain open. |
| Six route-specific achievements are registered, localized, and wired with three icon states each. | **Proven in source and static assets** | Six entries exist in `common/achievements/chaos_redux_achievements.txt:713-808`, localisation exists in `localisation/english/021_random_civil_war_l_english.yml:334-365`, and the eighteen runtime sprite states are registered in the Event 021 GFX files. Award truth under actual lifecycle transitions is still a live-game gate. |
| Entry, route, evolution, settlement, and no-target events are actually reachable from the chain. | **Incomplete** | Current call-site search finds calls for `.1`, `.2`, `.3`, `.7`, `.8`, `.9`, and `.17`. No current call site was found for country events `.4`, `.5`, `.6`, or hidden callback events `.10-.16`, nor for `chaosx.news.211` or `.212`. This leaves exposure, settlement, global-fracture, both news presentations, and several callback event definitions dead or stale even where equivalent effects are called directly. |
| Event log, event details, evolution records, names, and localisation remain synchronized. | **Weak/indirect** | Event-log append and snapshot source, event-details selectors, evolution records, scripted localisation, and English localisation are present. Dead presentation events, current MCP helper limits, and no live consumer evidence prevent full proof. The localisation audit also records dead Event 021 scenario-name helper selectors even though shared scenario selectors resolve the visible strings. |
| Static Event 021-owned report, decision, evolution, scenario, and achievement art is processed, wired, and documented. | **Proven for owned files; consumer review blocked** | `docs/assets/021_random_civil_war/manifest.md` records forty owned texture consumers with original, processed, DDS, and comparison evidence. Contact sheets and DDS round-trip reviews show a coherent static package. The manifest discloses native-alpha failures and bounded Pillow edge-repair fallback for achievement states. User in-game crop, scaling, and final consumer review remain open. |
| Reused Event 006 assets and portraits are complete, provenance-safe, and final. | **Blocked** | `docs/assets/021_random_civil_war/validation/reused_event006_asset_audit_2026-09-02.md` explicitly remains incomplete. `reused_rhi_bay_portraits_2026-09-02.md` leaves all six reviewed portrait rows blocked or provisional. Grounded generated repaints cannot count as final portraits under the current portrait policy; required `chaosx_portrait_creator` final handoffs and user-supplied grounded replacements are absent. |
| No dedicated scripted GUI, super-event, 3D unit, animation, or unit-audio package is required. | **Proven** | The accepted design uses the normal decisions UI and static art only. No event-owned scripted GUI, super-event, custom 3D unit, skeletal animation, or unit sound-design package is introduced, so their specialist completion gates are not in scope. |
| Documentation and authoritative workbook/export rows match the nonfinal implementation state. | **Weak/indirect** | The XLSX Event 021 row, Wars cluster row, and SCN-018 row are current and explicitly `Needs Testing` or `Partially Available`. The three CSV exports are newer than the workbook and scenario values align. The Events CSV has a trailing blank field and the Clusters CSV omits the workbook `Status` column, so export-schema parity is imperfect. More importantly, `docs/plans/021_random_civil_war_plans/active_repair_ledger_2026-09-02.md:46-47` says Event 021-origin Event 006 local surfaces were opened, while current source explicitly closes them; older source-complete and weighted-severity claims are stale. |
| A completion report may promote the event and open the release gate. | **Blocked** | The current source, catalog, active ledger, acceptance evidence, asset audit, MCP results, probability evidence, and missing user gates all prohibit a completion or promotion claim. |

## Completion status by surface

| Surface | Status | Disposition |
|---|---|---|
| Core event identity and safety hold | **Proven** | Correct ID, category, tier, cluster severity, and intentionally closed release gate. |
| Opening target and route framework | **Weak/indirect** | Extensive source exists; runtime state flow and final weighted target evidence do not. |
| Severity | **Incomplete** | Deterministic ladder conflicts with accepted weighted design and stale historical probability claims. |
| Territory and military split | **Weak/indirect** | Source helpers exist; required geographic, balance, and transfer scenarios are absent. |
| Decisions and missions | **Weak/indirect** | Definitions and AI scores exist; runtime transitions, timeouts, cleanup, and exploit checks are not certified. |
| Event 006 adapter | **Incomplete** | Internal setup exists, but the promised player-facing Event 006 package is deliberately gated off for Event 021 origins. |
| Evolution I | **Weak/indirect** | Multi-front source exists; probability, independence, and settlement behavior are not certified. |
| Evolution II | **Incomplete** | Existing crises receive one activation pass; future crises and ongoing strange incidents lack a caller. |
| Evolution III | **Weak/indirect** | Bounded scheduler source exists; liveness, fairness, nesting, and performance are unproven. |
| Cluster and scenario | **Weak/indirect** | Registration and builders exist; release gate and absent live fixtures block execution proof. |
| Settlement, successor, recurrence, cleanup | **Weak/indirect / blocked** | Significant source repairs exist; remaining-war continuity, signatory succession, second-crisis ordering, and complete cleanup remain open. |
| Event presentations | **Incomplete** | Several event and news definitions have no call sites. |
| Achievements | **Proven in source and static wiring** | Six exact definitions and three-state icon packages exist; runtime awards remain unproven. |
| Event 021-owned assets | **Proven with disclosed fallback** | Forty active owned consumers are documented and visually reviewed; user consumer approval remains open. |
| Reused Event 006 assets and portraits | **Blocked** | Crosswalk, provenance, final portraits, and consumer evidence are incomplete. |
| Documentation and workbook | **Weak/indirect** | Nonfinal rows are current, but plan/source contradictions and CSV schema drift remain. |
| Event MCP evidence | **Blocked / partial** | Current inspections are partial; current renders and comparison did not complete. |
| Probability evidence | **Blocked / partial** | Historical partial audits exist; no complete current named-scenario certificate covers every weighted surface. |
| User live-game, save/reload, and performance gates | **Blocked** | No user evidence exists, and the release gate prevents the intended full matrix. |

## MCP evidence and exact limits

### Event inspection

- A current `hoi4.event_inspect` downstream trace was run for `chaosx.nr21.1` and a separate current trace was run for `chaosx.nr6.1` using the event selector, helper expansion, and bounded depth.
- Both returned `EVENT_INSPECTED_PARTIAL` at source revision `d845f43c9709` and graph hash `c23d0d5…`.
- The workspace projection reported 9,740 events, 15,167 options, zero expanded helpers in the returned graph, 8,731 unresolved references, 2,199 issues, and one blocking diagnostic.
- `validation.passed` was false because the service deferred large-workspace helper projections and lifecycle passes.
- These artifacts prove that the server indexed the current source and produced bounded traces; they do not prove helper state flow, lifecycle completion, event reachability, or engine execution.

### Event rendering

- Current root renders for Event 021 and Event 006 were requested with `hoi4.event_render`; both exceeded the 180-second tool limit and produced no current artifact.
- A later pair of narrower cached option renders for `chaosx.nr21.3` and `chaosx.nr6.1` was still running when the user directed immediate finalization, so it was terminated rather than keeping the audit open.
- Historical Event 021 partial render artifacts in the acceptance ledger remain weak/indirect evidence because they predate the current revision and render graph structure rather than the in-game event card.

### Event comparison

- `hoi4.event_compare` was requested from cached revision `23d07f38466bd55877a4f79f36a99c34bb9b7f0790f582a264bb307cc60e4646` to current revision `d845f43c9709…`, with refresh enabled and render disabled.
- The call exceeded the 180-second tool limit and produced no comparison artifact.
- Earlier comparisons also failed because the required baseline revision was not cached.
- Source diff and source review are not substituted for the missing mandatory comparison evidence.

## Probability evidence and weighted surfaces

The required `chaosx_ai_probability_auditor` route was started for the current Event 021 audit with no inherited context.

The worker remained running at the user's finalization deadline and returned no handoff.

It was closed rather than delaying this report, so this audit does not claim that its source review substitutes for the mandatory probability workflow.

Current weighted or score-bearing surfaces requiring a complete current certificate include:

- automatic target tickets and the shared individual-crisis load curve;
- archetype weights;
- the accepted but currently deterministic severity model;
- Evolution I major-country participation and front selection;
- sampled evolution timing;
- sponsor, relief, mediation, and neighboring response scores;
- strange-incident `random_list` weights;
- settlement AI and recurrence decisions;
- global scheduler and queue selection;
- Wars cluster candidate selection and collision behavior;
- SCN-018 Low, Medium, High, and Maximum target selection;
- all Event 021 decision and mission `ai_will_do` blocks;
- Event 006 package AI that is expected to be reachable from an Event 021-origin package.

Historical probability handoffs document partial source inspections, several adapter failures, unresolved inputs, a sponsor resource-guard comparison, and some scenario-specific outputs.

They do not form one complete current same-scenario baseline/post-change certificate, and older weighted-severity outputs no longer describe the deterministic current source.

## Accepted-plan disposition

| Plan or requirement | Disposition on 2026-09-06 | Evidence |
|---|---|---|
| Keep Event 021 unavailable until release gates close. | **Implemented** | The release-ready flag is cleared and never set. |
| Six-route civil-war framework and normal decision interface. | **Implemented in source; validation queued** | Current event, effect, trigger, decision, category, localisation, and AI files. |
| Full admitted Event 006 package reuse under Event 021 origin. | **Accepted but incomplete** | Internal package setup exists; current player-facing predicates explicitly exclude Event 021-origin actors. |
| Weighted automatic severity. | **Unresolved / not implemented** | Current deterministic ladder conflicts with the accepted improvement addendum; the active ledger records the discrepancy without a disposition that changes the spec. |
| Shared fixed-target individual-crisis pressure helper. | **Blocked** | No defined input/output/caller contract and no implementation. |
| Scenario ticket-count ordering repair dated 2026-09-06. | **Implemented in source; evidence queued** | `subagent_handoffs/scenario_ticket_count_ordering_repair_2026-09-06.md`; no MCP probability or live scenario certificate. |
| Ordinary successor ordering and history transfer repairs. | **Implemented in source; lifecycle blocked** | Current parent effects and on-action ordering; no remaining-war or signatory-succession proof. |
| Event 021-owned forty-texture static asset package. | **Implemented and source-reviewed** | Current manifest, validation records, GFX, and decoded DDS evidence. |
| Event 006 reused visual/provenance package. | **Blocked** | Current reused-asset audit and portrait crosswalk remain incomplete. |
| Broad new GUI, super-event, focus-tree, 3D, animation, or audio expansion. | **Rejected/out of scope** | The accepted design uses existing Event 006 content, normal decisions UI, and static Event 021 art. |
| September 1 source-complete claims and conflicting August 31 resume claims. | **Superseded** | `active_repair_ledger_2026-09-02.md:3-6` explicitly supersedes them, and current source reveals additional contradictions. |
| Completion promotion and release-gate opening. | **Blocked** | No current plan or handoff satisfies the remaining implementation, asset, MCP, probability, or user gates. |

## Simplifications, placeholders, fallbacks, and stale evidence

- Event 021-origin Event 006 actors receive internal package setup receipts but are deliberately denied the package's player-facing focus and decision surfaces.
- Automatic severity is deterministic rather than the accepted weighted selection.
- Evolution II propagation is activation-time only; later openings and ongoing strange-incident review are missing.
- Event country presentations `.4`, `.5`, and `.6`, hidden callbacks `.10-.16`, and news events `.211` and `.212` have no current call sites.
- The shared fixed-target individual-crisis pressure helper is absent.
- Reused Event 006 assets, flags, formables, portraits, provenance, and consumer evidence are incomplete.
- Six reviewed RHI/BAY portrait rows remain provisional or blocked, and grounded generated repaints do not satisfy the required final portrait workflow.
- Event 021-owned achievement alpha repairs used a documented Pillow border-connected cleanup after native-alpha generation failed; the fallback is disclosed and visually reviewed rather than hidden.
- Fifteen legacy Event 021 DDS files remain documented as unregistered historical orphans and are not counted among the forty active owned consumers.
- Historical weighted-severity probability results, source-complete statements, and the active ledger statement that Event 006 local surfaces were opened are stale against current source.
- Historical event renders and comparisons do not certify the current source revision.

## Meaningful validation completed

- Compared all Event 021 source-spec acceptance families against current identifiers and call sites.
- Confirmed the closed release gate and absence of a setter.
- Enumerated current Event 021 event definitions and external call sites, exposing dead presentation and callback definitions.
- Traced Evolution II exposure and incident callers and confirmed they occur only at Evolution II activation.
- Compared current Event 006 package-content, local-content, and player-surface predicates with focus-tree, aggregate decision, and category consumers.
- Confirmed six achievement definitions, localisation blocks, and three-state GFX registrations.
- Confirmed Event 021 cluster constants and registration, SCN-018 constants and dispatch, four scenario types, and four intensity bands.
- Reviewed current owned-asset manifest and validation evidence and the incomplete reused Event 006 asset and portrait audits.
- Read the authoritative XLSX rows for Event 021, Wars, and SCN-018 and compared them with the generated CSV values and schemas.
- Used the mandatory read-only event inspect, render, and compare routes and retained their partial results and exact blockers.

## Missing validation

- Complete current helper-expanded Event 021 and Event 006 event renders.
- Current changed-revision event comparison artifact.
- Complete probability inspect/evaluate/sweep/simulate/sequence/compare evidence for every named scenario and weighted surface.
- Final decision/mission runtime audit covering visibility, availability, cost, targets, AI purchases, timeouts, cancellation, and cleanup.
- Engine fixtures for territory connectivity, supply, capitals, remnants, force division, stockpiles, navy, and air.
- Engine fixtures for multi-front independent resolution, late Evolution II openings, Evolution III queue liveness, cap behavior, nested human control, and nonhuman cleanup.
- Multi-signatory settlement and obligation fixtures, ordinary successor remaining-war continuity, signatory succession, and second-crisis recurrence ordering.
- Cluster collision and fairness fixtures involving Events 004, 007, and 021.
- SCN-018 observed target counts for Low, Medium, High, and Maximum.
- User-owned live event-card, decisions, assets, localisation, achievement, save/reload, and performance evidence.

## User-owned live-game and performance gates

These gates are **blocked**, not failed, because no user evidence was supplied and agents do not run Hearts of Iron IV.

- Stable minor automatic opening.
- Unstable minor automatic opening.
- One-state country fallback.
- Subject and invalid-target handling.
- Medium and major Evolution I front behavior.
- Event 006-origin package usability under Event 021.
- Evolution II border, support, sponsor, mediation, relief, and strange-incident behavior, including crises opened after activation.
- Evolution III stable and critical global bands, queue liveness, nesting, and human-control preservation.
- Wars cluster reservation, collision, skip, and cooldown behavior.
- SCN-018 Low and Maximum counts, plus Medium and High sanity.
- Every settlement route, successor continuation, recurrence, cleanup, and save/reload ordering.
- Achievement award and disqualification truth.
- Event-card crops, decision icons, evolution icons, scenario icons, news images, achievement states, and reused Event 006 consumers.
- Performance under Maximum intensity and Evolution III global scheduling.

## Remaining blockers and recommended next actions

1. Resolve the accepted Event 006 reuse contract: either implement origin-neutral player-facing focus, decision, formable, AI, and package consumers for Event 021 actors, or obtain and record an explicit spec change that narrows reuse.
2. Resolve severity design: implement and certify the accepted weighted model or record an explicit accepted spec disposition for the deterministic ladder, then replace stale probability claims.
3. Add the missing late-opening Evolution II propagation and bounded ongoing strange-incident review, or disposition those accepted requirements explicitly.
4. Wire or remove/disposition dead Event 021 presentation and news events so the documented event chain matches actual reachability.
5. Define and implement the shared fixed-target individual-crisis pressure contract before accepting fixed-target and scenario paths.
6. Finish ordinary successor remaining-war and signatory succession behavior, multi-signatory obligations, recurrence reset, and terminal cleanup before promoting settlement completion.
7. Complete the Event 006 reused asset and portrait crosswalk, including required `chaosx_portrait_creator` handoffs and user-supplied grounded final portraits.
8. Run one current `chaosx_ai_probability_auditor` pass over every named Event 021 scenario and all weighted AI surfaces, with same-scenario comparisons wherever source changed.
9. Obtain current successful `hoi4.event_render` artifacts for both Event 021 and Event 006 and a valid changed-revision `hoi4.event_compare`; preserve exact server blockers if the routes remain unavailable.
10. Reconcile `active_repair_ledger_2026-09-02.md`, the acceptance evidence, source-of-truth map, resume packet, asset status, and workbook/export schema with current source before any promotion.
11. Keep `random_civil_war_rework_ready` closed until the implementation, asset, MCP, probability, and user-owned live/performance gates above are all disposed with evidence.

## Final auditor disposition

Event 021 is **not complete**.

Finished work is concentrated in source scaffolding, owned static assets, achievements, catalog registration, and many lifecycle helpers.

Partial work includes target and route selection, territory and force construction, decisions and missions, Evolutions I and III, cluster/scenario behavior, settlements, recurrence, cleanup, event log/details, AI, and documentation.

Blocked work includes complete Event 006 package reuse, reused assets and portraits, fixed-target crisis pressure, successor war/signatory continuity, current event MCP render/compare evidence, complete probability certification, and every user-owned live-game/save/performance gate.

Design-gap work includes the unresolved deterministic-versus-weighted severity conflict and the mismatch between the accepted Event 006 full-package objective and the current deliberate player-surface exclusion.
