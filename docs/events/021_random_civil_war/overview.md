# Event 021 Random Civil War

This document is the canonical implementation summary for Event 021 Random Civil War.

The catalog status is `Needs Testing`. The rework implementation phase is marked complete for test entry, while acceptance certification remains incomplete.
The current-source findings and repairs in `docs/plans/021_random_civil_war_plans/active_repair_ledger_2026-09-02.md` supersede earlier certification and source-completeness statements below.
Historical MCP and asset results apply only to their recorded source revisions and files, not to the complete current runtime.

The late source repairs and their unresolved evidence boundary are recorded in `docs/plans/021_random_civil_war_plans/subagent_handoffs/late_source_repairs_2026-09-06.md`.
The improvement-loop dispositions are recorded in `docs/plans/021_random_civil_war_plans/improvement_loop_disposition_2026-09-06.md`.
The test-release decision is recorded in `docs/plans/021_random_civil_war_plans/subagent_handoffs/test_release_gate_2026-09-13.md`.

## Identity and scope

Event 021 is a Minor Repeatable event with chaos level 1, the root `chaosx.nr21.1`, and the stable event id `21`.

The automatic event and The Fracture Cascade are enabled for the `Needs Testing` phase after the one-time runtime initializer seeds `random_civil_war_rework_ready`. Event 021 is included in `event_log_event_is_reworked_default_enabled`, so new settings initialization does not place it in the default-disabled rework queue. This test release does not certify the final acceptance gates.

The target pool is fail-closed, so an empty or invalid target pool renders `N/A`, records a skip reason, and contributes no live automatic weight.

Event 021 is a normal event-system package and does not add a custom GUI, animated asset, super-event, 3D model, or whole-world daily, weekly, or monthly loop.

The package uses the normal Event Log, Event Details, Settings, decision, mission, on-action, and scenario surfaces already shared by Chaos Redux.

The parent transaction is in `common/scripted_effects/021_random_civil_war_parent_effects.txt` and the reusable state layer is in `common/scripted_effects/021_random_civil_war_effects.txt`.

## State model

Each eligible country receives hidden Fracture Pressure and visible State Authority values through `event021_initialize_country_state` and `event021_refresh_country_state`.

Fracture Pressure uses the centralized thresholds `exposed_threshold`, `fractured_threshold`, and `critical_threshold` in `common/script_constants/021_random_civil_war_constants.txt`.

State Authority uses the visible Cohesive, Contested, Failing, and Collapse bands from the same constants file and the `event021_GetAuthorityBand` scripted localisation.

Pressure rises from weak stability, military disloyalty, territorial loss, low state capacity, nearby conflict, prior Event 021 memory, and active war.

Pressure falls through relief, settlements, reconstruction, and other explicit administrative actions.

Authority changes through capital control, supply and depot access, administration, negotiation, repression, foreign intervention, settlement, and victory or defeat.

The state refresh publishes the current pressure band, authority band, summary, phase, target name, and N/A fallback used by the decision category and Event Details.

## Targeting and opening transaction

The bounded scheduler is entered from the existing Chaos global-host pulse through `event021_parent_global_scheduler_pulse`.

The scheduler registers only a bounded sample of normal human countries, reviews the persistent registered array, and launches a bounded critical queue.

Broad registration, due-country openings, Critical queue admission, and Critical launches require active Evolution III. Earlier stages use the host pulse only to maintain countries already registered by an explicit live crisis, and disabling Global Fracture empties the Critical queue.

Each country carries its own due date, pressure memory, recurrence memory, and generation information, so review work does not require an unrestricted world scan.

The target transaction follows route preparation, target weighting, archetype selection, severity selection, reservation, connected-state planning, force planning, validation, and commit.

The core target layer reserves the country and every planned state before ownership, control, or actor mutations occur.

The reservation is shared with the Wars cluster through `random_civil_war_cluster_target_reserved` and remains idempotent when the cluster has already reserved the target.

The plan must preserve a projected post-transfer capital outside the reserved state set and a connected controlled productive state, except for same-tag contests that transfer no territory.

It must also contain a connected state set, enough organized support, a valid route, and a capacity slot before it can commit.

Failure rolls the transaction back, clears temporary plan state, records a skip reason, and does not create an actor or partial war.

Concurrent crises keep durable host-to-actor and actor-to-host country pointers. Settlement, successor, Event 006 finalization, and cleanup rebuild their short-lived global transaction targets from those pointers before acting, so one theater cannot consume the most recently launched theater's host or actor.

The parent never blindly divides half of a country’s army, equipment, or territory.

Opening force, navy, air, manpower, stockpile, and front shares are computed from centralized severity and route tuning plus a bounded scan of the selected connected states. Local divisions, population support, depots, arsenals, ports, airfields, actor identity, live national air and naval assets, equipment availability, and an external war all modify the allocation before its viability clamps.

Air and naval shares are zero unless the selected region controls the matching base, the parent has live assets, and the actor identity can use them. Event 006 actors retain their package-owned force profile instead of receiving a second generic split.

Vanilla `start_civil_war` receives the computed opening size and ratios, so its stockpile and force allocation remains tied to the same measured transaction instead of a second unconditional grant.

Regional, command, and Event 006 evidence receipts keep source-specific actor, package, and region identity. A receipt with a referenced actor clears when that scope ceases to exist, while settlement completion creates a finite settlement receipt that expires through the same refresh contract.

Decision actions then spend real command power, political power, manpower, experience, infantry equipment, trucks, trains, and convoys through bounded effects.

## Routes and severity

The route registry supports ideological uprisings, rival legal governments, regional secessions, command schisms, complete Event 006 independence actors, and same-tag contests.

Ideological and legal routes use the existing country institutions and do not create a duplicate country identity.

Regional routes require more than one controlled state and a connected grievance or anchor.

Command routes require more than one division and a valid military loyalty or arsenal path.

Event 006 routes are accepted only when one of the 32 content-attested human packages can pass the existing package registry, anchor, carrier, and final-validation gates.

Same-tag routes cover unsafe one-state and all-island countries without releasing a duplicate tag.

The route adapter records the selected archetype and route evidence before the parent commits.

Stable countries resolve to Limited, exposed countries resolve to Serious, and weak, exhausted, occupied, divided, poorly administered, or critically pressured countries can resolve to Severe or Critical crises after the required evolution or scenario gate. The current source uses a deterministic pressure-and-viability ladder; the full named probability matrix and any future weighted severity replacement remain uncertified.

The target weight is centralized in `random_civil_war_target_weight` and includes pressure, failing or collapsed authority, exposure, route validity, stage, and severity evidence.

The final opening severity is centralized in `random_civil_war_severity` and `event021_parent_tuning` rather than hardcoded in the event root.

## Front and region registry

The opening state plan is connected and bounded by `maximum_multifront_states` and the active theater capacity.

Each committed theater registers a stable Event 021 theater receipt, original host, anchor state, opposing actor, current phase, and generation.

Each front registers a stable front id, actor pair, state reference, front goal, priority, and resolution receipt in the shared arrays.

Before the opening engine call, Event 021 also creates an aligned bounded front-plan receipt with row identity, actor role, anchor and capital, connected-state membership, relationship, route or package provenance, objective, force envelope, and settlement lifecycle status. The normal row order is host remnant, primary claimant, optional ordinary secondary, and optional Event 006 secondary, with a maximum of four rows.

Registration and priority binding consume the matching plan row by front id. Optional starters mark their row rejected when a frozen receipt cannot materialise, and settlement review does not report all internal fronts resolved while a plan row remains pending. Rollback and final cleanup clear the complete plan ledger.

The Event 006-owned `independence_wave_initialize_event021_adapter_registry` and `independence_wave_capture_event021_adapter_actor` effects publish the complete package allowlist and matching carrier identity consumed by Event 021.

Event 021 reads the selected package's validated anchor and carrier from that contract and hands the complete package to the generic Event 006 setup dispatcher.

Evolution I enables viable secondary fronts, independence fronts, additional command authorities, and reduced-weight targeting of major countries. After an ordinary opening, one complete dormant Event 006 package may consume a distinct noncapital anchor and enter as an additional independence front when the host remnant and all front, theater, and belligerent caps remain valid.

Ordinary secondary fronts require a connected state candidate, active opposition, a distinct unreserved evidence-backed route, available capacity, and the explicit Evolution I gate. The package-owned additional front uses the Event 006 registry and adapter instead of manufacturing an ordinary archetype, and is registered only after its war with the host is proved.

Each ordinary secondary actor receives the role-specific AI adapter for its reserved route: revolutionary for ideological, constitutional for legal or regional, and command claimant for command fronts.

Front review closes resolved fronts, updates authority and pressure, and prevents a secondary front from settling the host before all required fronts are addressed.

Protected remnants preserve the opening capital or a valid replacement and prevent cleanup from deleting the surviving national core.

## Event 006 adapter boundary

Event 021 can initialize a human Event 006 package even when Independence Wave never fired.

The adapter reuses the existing Event 006 carrier, identity, leaders, flags, focus tree, politics, ideas, forces, reinforcement, formables, decisions, AI, and assets.

Event 006 owns both the 32-package admission registry and package-to-carrier mapping, so Event 021 does not maintain a second package list.

The Event 006 package must pass the complete package predicate before the adapter can commit.

The admitted Transcaucasus package roots accept the Event 021 compatibility receipt only during validated adapter setup or after complete human-package proof. A normal Event 006 origin continues to use its Event 006 origin value.

Event 021 records an Event 021 origin receipt on the reused package.

The adapter does not set the Event 006 fired marker, change Event 006 weight or cap, advance Event 006 evolutions, duplicate a tag or character, create an incomplete or actual nonhuman package, or auto-enroll the actor in Event 006 league systems.

Event 006 human countries remain vulnerable to later Event 021 reviews.

`is_actual_nonhuman_country` is used by the normal human-country predicate to keep actual nonhuman countries immune.

When a primary or additional Event 006 front resolves, Event 021 closes only its temporary side and registry records and preserves the durable Event 006 package, identity, focus, assets, and origin history.

## Evolution records and Global Fracture

The Event 021 evolution records are `Gathering Fronts`, `Regional Exposure`, and `Global Fracture`.

The parent transition wrappers write each record once through the shared Event Log and Event Details evolution registry.

Evolution I adds viable multi-front wars, independence fronts, and reduced-weight major targeting.

Evolution II adds Regional Exposure, neighboring actions, sponsors, stronger sides, separate civilian relief and armed support, and a rare uncertain strange incident.

Civilian relief uses `random_civil_war_civilian_relief_available` and bounded humanitarian effects.

Armed support uses `random_civil_war_neighbor_armed_support` and separate military pressure and authority effects.

The strange incident is local to an exposed active side, rate-limited by a recent-incident flag, and never creates an unbounded actor.

Evolution III is the nonterminal Global Fracture state.

Global Fracture moves countries through Stable, Exposed, Fractured, and Critical pressure bands.

Due-country reviews, the bounded Critical queue, active-theater caps, front caps, nested-crisis checks, successor grace, recurrence memory, and generation caps remain authoritative. Automatic, queue, and manual-scenario targets all fail closed during successor grace; a human Event 006 country becomes eligible again only after grace expires and another valid route exists.

Global Fracture does not set `world_end` and does not turn the scheduler into an unrestricted world iteration.

Disabling an evolution through the shared Event Log settings flags clears its active consumers and threat source while preserving the historical evolution record.

## Decisions and missions

The package uses one normal decision category with one static category picture and the dynamic category text `event021_civil_war_crisis_category_desc`.

The category shows one State Authority value, the current authority band, current phase, target summary, and a concise dynamic crisis description.

The opening view uses Secure the Arsenals, Defend the Capital, and Review Command Loyalty, with Seize an Opposition Depot atomically bound to an owned and controlled opening-front state containing a supply node or military factory.

The multi-front view uses Review Command Loyalty, Integrate Loyal Formations, and Set the Priority Front.

The exposure view separates Open a Relief Corridor from armed Support the Government or Support the Opposition and also provides border monitoring or mediation according to the live target.

Regional Exposure uses a dedicated source-country target for the bounded neighbor pass and clears it when that pass ends; it does not reuse the opening transaction's global host pointer.

Settlement, reconstruction, and Global Fracture prevention actions appear only in their own phases, while obsolete or completed actions disappear.

The decision package therefore exposes three to five phase-appropriate actions and never gives one action more than four resource types of cost.

Multi-front countries can rotate the registered priority-front state, while reconstruction repairs the selected rail-spine infrastructure and prevention reuses the communications, loyalty, and regional-administration actions.

The three disjoint-phase missions are Hold the Capital, Secure the Rail Spine, and Enforce Settlement Terms.

Selecting a mission starts its timed commitment; the timeout resolver then evaluates the stored control, supply, front, or settlement objective and dispatches the distinct success or failure effect in `021_random_civil_war_decision_effects.txt`.

Relief and armed support are separate decisions and separate scripted effects.

## Settlement, reconstruction, and recurrence

Settlement terms include government victory, opposition victory, independence, autonomy, coalition, partition, merger, and evolution outcomes.

The settlement selector is bounded by the surviving actors, front goals, State Authority, and the available legal route. Partition and a hardliner government's non-negotiated military victory are classified as harsh failed settlements, so their recurrence cost is preserved.

Settlement obligations are recorded before temporary war state is removed.

Reconstruction restores administration through a finite due-date sequence instead of an always-running maintenance loop.

Completion applies reconstruction relief, records the settlement and achievement receipts, prepares recurrence memory, and then cleans temporary Event 021 state.

`No State Left Behind` snapshots every original core state at opening rather than only the states transferred to the claimant.

`A Flag of Our Own` requires recognized independence, survival through postwar finalization, and a separate Event 006 milestone: a completed constitutional state, committed formable, open-sovereignty declaration, or treaty-backed recognition.
Postwar survival alone does not satisfy that milestone.
The achievement registry evaluates the milestone from the live Event 006 package, including after Event 021 cleanup.

All six achievement IDs are registered in `common/achievements/chaos_redux_achievements.txt` and consume route-specific predicates in `021_random_civil_war_triggers.txt`.
Scenario and debug/force launch receipts disqualify their countries, while an authority-collapse receipt prevents later recovery from erasing the history required by `Hold the Center`.
These source contracts require lifecycle acceptance evidence before the event can be certified.

Recurrence remembers recent crises, failed settlements, broken settlement obligations, unresolved sponsor dependence, and successor origins. Negotiated government or coalition settlements reduce the score, while successor grace, cooldown, normal-human validity, viability, and the bounded recurrence window remain exact launch gates.

Successor grace protects a newly recognized Event 006 or other successor package from an immediate recursive opening while retaining later vulnerability.

Generation caps and active-theater/front caps prevent nested crises from growing without bound.

## Wars cluster integration

Event 021 is logical row `wars_random_civil_war` with row id 1003 in Cluster 1, Wars, at Medium severity and minimum Chaos tier 1.

Event 004 Random War, Event 007 Fury, and Event 021 use the shared Wars cluster reservation and cooldown path.

Event 021 is not registered in any second cluster. During a Wars transaction, Calm World and Gathering Storm reserve both Event 004 countries away from Event 021. Rising Chaos and higher may reuse Event 004's target only when live external-war evidence and Fractured-or-worse pressure prove an intentional collapse under war strain. A newly created or recently resolved Fury actor remains excluded, and Event 006 package admission continues scanning after occupied tags or invalid anchors instead of duplicating a package.

Event 021 reserves a target before its plan begins, detects an existing reservation, and records collision or skip reasons instead of silently overwriting another war member.

An unavailable Event 021 row reports N/A and zero live weight to the cluster catalogue.

The Wars cluster retains one pacing event and does not give Event 021 a second unrestricted pacing loop.

Manual forcing bypasses cluster-only roll gates but still requires Event 021’s normal fireability, reservation, plan, route, and cleanup checks.

## The Fracture Cascade scenario

The manual scenario is The Fracture Cascade with verified raw id 18 and public catalog id `SCN-018`.

The four types are Political Fracture, Independence Cascade, Command Collapse, and Universal Fragmentation.

The four intensities are Low, Medium, High, and Maximum.

Low, Medium, and High use bounded shares of eligible normal human countries with intensity-specific target tickets, route, and force limits. Low favours minors, Medium is neutral, and High makes majors common; the ladder is centralized in `random_civil_war_scenario_target_weight` before shared crisis-load adjustment.

Maximum freezes every country that passes the normal-human, topology, route-type, capacity, and opening-state preflight into one confirmation-time pool and visits every frozen row exactly once, while still excluding actual nonhuman countries. The run records preflight-selected, frozen commit-eligible, and preflight-skipped counts separately; it never replaces an unavailable plan after preparation. Countries created by an earlier launch cannot join that same scenario run.

Scenario setup is immediate and uses the same reservation, connected-state, force, actor, front, settlement, and cleanup transaction as ordinary play.

No measured one-frame performance failure exists, so the implementation does not add a delayed seven-day fallback.

Scenario setup marks its origin and disqualifies achievements without changing Event 006 fired state, evolution state, league state, or ordinary automatic weights.

Scenario cleanup clears bypass, target, reservation, front, theater, mission, idea, and temporary registry state even when a setup attempt rolls back.

## Event Log and Event Details

The entry, opening, multi-front, exposure, settlement, reconstruction, Event 006, same-tag, cleanup, evolution, and scenario callback events are rooted in `events/021_random_civil_war.txt`.

Event 021 has an Event Log actor mapping, type/name/stage localisation, payload detail text, and three evolution records in the shared log effects and scripted localisation.

Event Details uses the same current phase, severity, authority, pressure, target, front, and settlement payloads as the decision surface.

Failed openings record a concise skip reason and never produce a false successful history entry.

## CXT extension

The modifier-free hidden carrier `chaosx_cxt_extension_event021_random_civil_war` is registered through one bounded existing-country scope.

`random_civil_war_register_cxt_test_content` and `chaosx_cxt_extension_event021_random_civil_war_apply` are idempotent, and the startup plus `on_daily_CXT` hooks synchronize them without a whole-world recurring loop.

The carrier is consumed by the CXT test setup effect and does not alter normal Event 021 eligibility.

## Assets and localisation

Event 021 uses static art only.

The opening report picture is `gfx/event_pictures/021_random_civil_war/report_event_021_random_civil_war_opening.dds`.

The multi-front and Global Fracture news pictures are `news_event_021_multi_front_war.dds` and `news_event_021_global_fracture.dds` in the same folder.

The category picture and icon, decision sprites, mission sprites, idea sprites, and achievement triplets are registered in `interface/021_random_civil_war.gfx`.

The current GFX file contains 40 unique Event021-owned texture references, and the owned runtime audit resolves and visually inspects all 40. Ordinary country events use the report-event family, while the two news events retain their dedicated news-event pictures. The strict DDS, source-equivalence, consumer, and orphan evidence for those owned textures is recorded in `docs/assets/021_random_civil_war/validation/visual_asset_audit_2026-09-01.md`.

Decision sprites are `decision_021_secure_arsenals`, `decision_021_capital_defense`, `decision_021_loyalty_review`, `decision_021_opposition_depot`, `decision_021_relief_corridor`, `decision_021_emergency_settlement`, and `decision_021_reconstruction`.

Mission sprites are `decision_021_hold_capital_mission`, `decision_021_secure_rail_junctions_mission`, and `mission_021_settlement_terms`.

Idea sprites are `idea_021_fractured_command`, `idea_021_war_torn_administration`, and `idea_021_unsettled_settlement`; the temporary secured-depot idea deliberately reuses the fractured-command picture family.

The six achievement triplets are `hold_the_center`, `no_state_left_behind`, `a_flag_of_our_own`, `war_within_a_war`, `the_terms_hold`, and `fractals_of_sovereignty`, each with normal, grey, and not-eligible sprites.

The current GFX consumer reads the achievement states from root `gfx/achievements/021_random_civil_war_*.dds`; the older interface-achievement path remains only as historical handoff provenance.

All player-facing strings are in `localisation/english/021_random_civil_war_l_english.yml`, including the N/A fallback, category summaries, decisions, missions, event details, evolution records, scenario labels, and achievement text.

The static art handoff records generated event art and DDS round-trip evidence.

The icon handoff records historical inherited ImageGen and Pillow fallback steps used for missing icon states, including the promoted runtime and evidence copies; current runtime/GFX evidence resolves all six achievement triplets and the relief/reconstruction action icons.

Event021-owned presentation adds no character portrait. An Event006 independence route deliberately reuses Event006 portraits, flags, focus art, ideas, formable art, and package assets; that inherited 32-package visual/provenance surface is separately inventoried in `docs/assets/021_random_civil_war/validation/reused_event006_asset_audit_2026-09-02.md` and remains incomplete, with blocked portrait provenance and unproven package-wide runtime reachability.

## Documentation and validation record

The editable event catalog source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

The required CSV exports are generated from that workbook by `.tools/export_event_catalog_csv.py` and are not hand-edited.

The helper contracts are documented beside the scripted effect and trigger files in `common/scripted_effects/021_random_civil_war_effects.md`, `common/scripted_effects/021_random_civil_war_parent_effects.md`, and `common/scripted_triggers/021_random_civil_war_parent_triggers.md`.

The acceptance matrix is in the Event 021 spec part 10 and covers stable, weak, one-state, subject, multi-front, Event 006, exposure, strange incident, Global Fracture, nested, nonhuman, Wars cluster, scenario, settlement, reload, cleanup, and performance cases.

The latest focused Event MCP lint inspected the `chaosx.nr21.1` chain at revision `3ac0bcfca142cdb797cca8faf293cfa1085b9019421045d9f385374ad094fc2a` with graph hash `18501dff365ddaeb371f8e07696cd36dafd3f74a24012df8ba7714f6df9da62f`; it returned no tool blockers and remains partial because workspace-wide helper and lifecycle projection was deferred.

The current report is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e14534054a61ed92f1ec86daa10adcddc359c2ebf0850767d5329e677a952dc8/926a73748dac5be198da6ad76bb3d1c0d5fe35ebe5091101ea729f9b916bfa13/event-lint-3ac0bcfca142.json`.

The earlier helper-expanded state-flow artifact remains useful pre-trigger-fix lifecycle evidence, but two post-fix refresh attempts returned MCP `INTERNAL_ERROR` without an artifact, so no current helper-expanded certificate is claimed.

The current bounded direct-event overview render has layout hash `3cf23da1fa05f76b7c4361d9fc375759010e2528fb44bd24566df7de8387ecf8`; its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c24a4ffb56f09579d38c6d8754042fe32f408aae2a1a96ab3eb78c4809b81a85/55eab89b2cb18f0406b9445e2ba9d9c5dfdc2c905a45d85a061713fabf2c2b29/event-overview-3ac0bcfca142.json`, with the matching manifest, SVG, and PNG artifacts in the same MCP response.

The current sponsor decision inspection parses the three support and mediation candidates with zero unresolved source inputs at source revision `a6e750bba8366c9665e9863cec65323e0af02bbd39e46ab742f3823d6278eb87`. The broader 18-decision and three-mission inspections remain targeted historical evidence until refreshed against the final checkout.

The current strange-incident evaluation reports 8% incident and 92% no incident with zero unresolved inputs under analysis `probability-6238523a08ebef03f0a38e07` and scenario hash `dfc486d2c35bd1237686439b22e74de17dbed503085b3e52346d81252640e284`. The current archetype, sponsor, and bounded admission receipts are recorded in `docs/events/021_random_civil_war/acceptance_evidence.md`.

A fifth independent audit completed the current six-entry archetype pool, four-entry severity pool, and eligible two-entry strange-incident race. One-hot archetype fixtures selected the sole positive route, equal routes normalized to one sixth each, incomplete Event 006 remained zero, and a fifteen-point sweep found no archetype rank reversal. All six severity fixtures completed individually, and eligible strange incidents remained 8/92 while outer-gated cases remained zero. The decision adapter discovered all 18 score-only candidates but could not resolve their hidden country-state inputs; the worker stopped during the SPN/SET pass and was shut down after an unsuccessful interrupted handoff request. These findings remain supplementary current-revision commentary evidence rather than a durable full-matrix certificate.

The current map inspection at revision `fa76cadf611a1bf937556584a71b1e1e0bbde4b0a9b8364ca86614218e0918be` proves state and strategic-region membership plus adjacency, supply-node, and railway checks; unrelated existing map-position, port, and localisation diagnostics are not attributed to Event 021.

Event compare against an older revision remains unavailable because the prior graph revision is not cached, and no completed compare is claimed.

The full named probability matrix, same-scenario comparisons, and runtime acceptance fixtures remain pending.

The agent does not launch Hearts of Iron IV or claim live-save acceptance evidence; live consumer validation remains with the user.

## Simplifications, omissions, blockers, and fallbacks

The Event 006 independence route is gated on the existing package-complete predicate, so a save with an incomplete Event 006 package skips that route instead of receiving a partial substitute.

The static icon handoff contains historical inherited ImageGen and Pillow fallback records for formerly missing icon states; current runtime/GFX inspection resolves all referenced states, and the records remain an asset-provenance simplification rather than character-portrait placeholders.

No grounded portrait, custom GUI, animation, super-event, or 3D asset was requested or added.

No delayed scenario setup fallback was added because no measured performance failure justified it.

The MCP event graph is selected-event evidence rather than a claim that every unrelated workspace helper has been fully projected. A current focus inspection and render successfully parsed and rendered all 184 Event 006 focuses with zero tree-local diagnostics at revision `55a900cb833aadee310a6c5b0f480af8cf0ea73522de74cef01f334788f351ae`; its sole warning concerns vanilla `continuous_restrict_freedom_desc` and is outside Event 021 ownership.

The post-fix improvement loop is resolved in `docs/plans/021_random_civil_war_plans/post_fix_improvement_loop_closure_addendum_2026-08-31.md`: accepted P0/P1 design work is implemented, broad expansion is reject-ready, and only certification evidence remains queued. Current specialist outcomes and exact MCP blockers are reconciled in `acceptance_evidence.md`.

No live HOI4 run, save-state test, or log inspection is claimed by this repository implementation.

## Current test-entry repair record — 2026-09-19

The bounded convergence repair is implemented in the current test-entry source: due reviews no longer force-open stable, exposed, or fractured countries; Critical claims retain their queue row until the recipient callback resolves them; `chaosx.nr21.18` owns the launch transaction; and queue exits record launched, stabilized, or invalidated outcomes.

The same repair persists the frozen scenario secondary state on the host country and preserves the same-tag safety route for Independence Cascade and Command Collapse on unsafe one-state or all-island targets.

SCN-018 now separates its unique selected set from its commit pass. The host-bound callback `chaosx.nr21.19` freezes every selected country's receipt before `chaosx.nr21.15` begins the first ownership mutation, preserving target-specific ROOT scope and exact plan reservations.

The scenario freezer can retain both an ordinary secondary-front receipt and a complete Event 006 secondary package when the target has room for both. Event 006 and ordinary secondary fronts are then committed as separate planned openings after the primary transaction, with package and state reservations preventing overlap; a large target without a second viable route still remains two-sided rather than receiving a fabricated actor.

The event inspector was refreshed for `chaosx.nr21.1` with zero blocking diagnostics and zero skipped sources. Its large-workspace validation remains partial because helper and lifecycle projections are deferred. Event 021 and SCN-018 remain `Needs Testing`, and live gameplay plus the named probability, lifecycle, inherited-package, and provider-contract gates remain open.

The 2026-09-19 source repair also makes Evolution I ordinary and Event 006 additional-front callers fail closed unless their route, anchor, objective, and package receipts were frozen before the opening mutation. The phase-specific decision and mission mapping is recorded in `docs/events/021_random_civil_war/decision_action_family_crosswalk.md`.
The current focused event lint is revision `95a1779f47fa5ffb9e6a53617f6d50c8772bcafcfd208d63b9083c1df85e2023` with graph hash `a3d547bd1e8ba5bf678828b08775811a0cf220001dd9c871f46e605ae08a40fe`, zero blocking diagnostics, zero skipped sources, and deferred helper/lifecycle validation; its artifact is recorded in `docs/events/021_random_civil_war/acceptance_evidence.md`.

Event 006 reuse is bounded by the current shared HOLD / PARTIAL authority: 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows. Event 021 admits only complete human package rows through the existing registry and skips incomplete packages, including IW-095, without partial-country or nonhuman fallback.

The inherited Event 006 probability and portrait gates remain open. The nested package pool has 126 candidates with one unresolved typed input and no complete manifest, root/support event-option probability calls return `INTERNAL_ERROR`, and all 13 scoped supplied portrait rows remain source-placeholder candidate holds. The exact authorities are the current Event 006 validation refresh, IW-095 package audit, probability audit, and portrait-rights closure handoffs referenced by `acceptance_evidence.md`.
