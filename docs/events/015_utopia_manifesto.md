# Event 015: Utopian Manifesto

## Overview

`utopia_manifesto` replaces the old Event 015 world-tension event. It is a Minor Fire-Once event that selects an eligible minor or eligible player country, blocks majors and strong industrial states, and reports `N/A` in the event log when no valid target exists.

AI targets are forced to accept. Human targets can accept or reject. Acceptance loads `utopia_manifesto_tree` only for the accepting country, opens the Utopian Ledger, applies the opening ideas, and unlocks ledger-driven decisions. Rejection removes the route cleanly and keeps the country on its existing path.

## Targeting

Target eligibility is defined in `common/scripted_triggers/015_utopia_manifesto_triggers.txt`.

- Valid targets must use normal civilian systems, must not be major powers, must not be nonhuman or special chaos countries, must not be capitulated, and must not already be in another event-owned focus-tree route. Countries already marked by a Chaos route are rejected through the shared `is_special_chaos_country` and `is_actual_nonhuman_country` gates.
- Strong states are blocked by total factories, military factories, naval factories, controlled states, and division count.
- Player countries are eligible if they pass the same safety gates.
- AI countries are additionally screened so subject-at-war and player-enemy cases do not force the route into unsafe wars.
- The event log uses the hard-valid target check for `N/A`, while automatic firing uses the stricter dispatchable-target check so valid player/minor availability is visible without spending the timer on unsafe AI contexts.

Event selection and event-log `N/A` behavior are wired through `chaosx_logic_effects.txt`, `chaosx_settings_effects.txt`, and `chaosx_events_log_effects.txt`.

## Ledger

The Utopian Ledger is visible through `utopia_manifesto_ledger_category` and the scripted GUI `utopia_manifesto_ledger_scripted_gui`.

Ledger values:

- Need
- Consent
- Surplus
- Overreach
- Vocation Balance
- Foreign Suspicion

The six core values are stored as country variables, clamped through shared constants, mirrored into display variables, and refreshed whenever ledger effects run. `League Confidence` is an auxiliary ledger readout used only for Friend, aid, League, and late public-identity behavior. They drive:

- decision availability and AI weight
- focus route availability
- Needful Land claims and integrations
- Friend recognition, League aid, League identity, and League achievement behavior
- Marked Bounds branch visibility
- late outcomes and achievements

The ledger GUI also shows route, geography, pressure state, active storehouse/integration project counts, League Confidence, friend count, and League member count. Scripted GUI buttons refresh the ledger, collect petitions, audit storehouses, and start a renunciation vote when their route, cooldown, and cost gates are met.

## Focus Tree

The accepting country receives `common/national_focus/015_utopia_manifesto_focus_tree.txt`.

Implemented branches:

- Opening trunk: manuscript, translation, census, reading halls, first store, useful arts, Need measurement, and boundary question.
- Living Humanism: councils, six-hour country, care tables, consent assemblies, mercy registers, renunciation, and living commonwealth.
- Common Store State: grain, measures, trains, surplus, auditors, crisis rations, and store-state maturity.
- Guild Commonwealth: guild congress, apprenticeships, trade law, workshops, engineers, patents, and charter.
- Island Discipline: harbors, convoys, sea roads, ring councils, shore engineers, couriers, and island compact for coastal countries; inland rail rings, Ring Watch units, guarded depots, and rail-spine engineers for landlocked countries.
- Economy and storehouse spine: local bread boards, granaries, rail/cart routes, reserve, foreign aid, and store network.
- Vocation branch: labor registers, workshop children, rotation, colleges, healers, and all useful arts.
- Military branch: just-cause review, household guard, storehouse engineers, drill, no-bloody-glory, reinforcement paths, and guarding the ledger.
- Diplomacy branch: Need-not-conquest, neighbors, arbitration, storehouses abroad, friends, League of Need, aid corridors, observers, and no secret empire.
- Needful Land and integration: proof, arbitration, settlement charters, marked districts, postwar registers, local storehouses, household councils, common administration, integration, compliance before core, and commission.
- Geography adaptation: coastal routes, landlocked caravan stores, subject ledger, tiny country deep ledger, and adapted commonwealth.
- Hidden Marked Bounds: revealed only when Need, Overreach, or chaos pressure justifies it; includes idle-soil survey, hard maps, boundary posts, guarded settlement, necessary-war table, wardens, bounds state, and no idle acre.
- Late proclamation outcomes: Paper Utopia, New Utopia, Necessary Commonwealth, Marked Bounds State, Proclaim the Common Store, and The Manifesto Survives.

Reward tuning is intentionally forceful. Ordinary focus rewards use large ledger swings, equipment bundles, manpower, XP, trains, convoys, trucks, and state construction so a successful minor becomes visibly stronger. Negative routes are also forceful: failed stores, confused vocation, foreign ridicule, Paper Utopia, Marked Bounds, and hardline proclamations carry large economic, diplomatic, resistance, or Suspicion costs. Late outcome focuses call scripted capstone packages that give absurd state-building rewards while preserving route identity and, for hardline paths, equally visible Overreach, Suspicion, threat, and resistance pressure.

## Decisions and Missions

Decision code lives in `common/decisions/015_utopia_manifesto_decisions.txt`.

Concrete costs and objectives include:

- census: Command Power and support equipment
- storehouse projects: support equipment, trains, convoys, timed state project
- apprenticeships: support equipment
- urgent service: manpower and stability
- rural rotation: trains, support equipment, timed mission
- household guard: infantry equipment, manpower, Army XP
- sea-road guard: convoys, support equipment, timed mission
- storehouse engineers: support equipment, motorized equipment, Army XP
- just-cause review: war support
- arbitration: trains, Command Power, stability, timed objective, no claim unless the arbitration mission resolves successfully, and settlement outcomes for compensation, guarantee-backed charters, or refusal
- Marked Bounds claim: stability, route risk, timed survey objective, and no claim unless the marked district survey resolves successfully
- boundary wardens: infantry equipment, Army XP
- common administration: infantry equipment, support equipment, manpower, timed state integration project
- local households: support equipment, compliance gain, resistance reduction
- foreign aid and League corridors: convoys, trains, support equipment, timed mission
- renunciation vote: stability and timed vote

The system does not create political-power stores.

## Needful Land and Integration

Needful Land is designed around proof and administration, not instant coring.

- Claims require Need proof, safe targets, arbitration or Marked Bounds pressure, and AI safety gates.
- Boundary arbitration and Marked Bounds district surveys start timed missions first; they add claims only after the target and state still satisfy the objective checks.
- Boundary arbitration stores the target country/state in per-country arrays, then resolves into a compensated settlement, a guarantee-backed settlement charter, or public refusal. Compensation spends Surplus, guarantee charters create a real guarantee from the manifesto country to the target, and refusal adds no claim while high Suspicion or hardline pressure can draw an outside major guarantee for the target.
- Claims use state flags and do not grant free cores.
- Integration projects require state control, equipment, manpower, project capacity, compliance, local storehouses, household councils, and local administration.
- Local stores and household councils are hard preparation requirements for Common Administration, not only accelerators. Common administration improves compliance and reduces resistance after that local setup. Forced-settlement risks raise resistance, Overreach, and Foreign Suspicion instead of becoming free administration.
- Route-specific risks are tracked through Overreach, Foreign Suspicion, forced-settlement flags, and Marked Bounds disqualifiers.

## Units

Dynamic unit-family helpers live in `common/scripted_effects/015_utopia_manifesto_effects.txt`.

- Household Guard spawns limited infantry-based defensive units scaled by war status and controlled-state count.
- Storehouse Engineers spawn limited support/engineering formations scaled by Surplus and state count.
- Craft Militias support the Guild and workshop branches with capped light defensive batches.
- Harbor Watch units support coastal and island discipline branches with capped coastal-defense batches.
- Ring Watch units support the landlocked Island Discipline interpretation with capped rail-ring and depot-defense batches.
- Surveyor Columns support Needful Land and Marked Bounds state work with capped occupation-support batches that raise Overreach.
- League Cadres turn Friend and League-member progress into capped defensive reinforcements.
- Batch caps and maximum-per-call values are centralized in `common/script_constants/015_utopia_manifesto_constants.txt`.

## Late Identities

Late route identity keeps the original country tag but can apply cosmetic names and flags through the repo's standard cosmetic-tag path.

- `utopia_new_utopia` applies the `utopia_new_utopia` cosmetic tag after the peaceful New Utopia proclamation.
- `utopia_necessary_commonwealth` applies the `utopia_necessary_commonwealth` cosmetic tag for the harder survival route.
- `utopia_marked_bounds_state` applies the `utopia_marked_bounds_state` cosmetic tag for the hardline final route.
- A successful League with enough members and League Confidence can apply the `utopia_league_of_need` cosmetic tag before later proclamations override it.
- All four cosmetic tags have generated base flags plus `democratic`, `communism`, `fascism`, and `neutrality` flag variants in normal, medium, and small flag folders so existing ideology-specific country flags are not retained.

## Super-Events

The regional proclamation uses five route-specific display slots with one deliberately shared, Event 015-exclusive audio cue:

- `96`: Consent of Households
- `97`: The Common Table
- `98`: Guardians of Measure
- `99`: The Closed Island
- `100`: The Joke Understood
- playback audio ID `57`: **Utopia Has Neighbors**

All five slots use the verified closing wish-over-hope sentence from Thomas More's *Utopia*, in Gilbert Burnet's 1684 translation. The exact wording, edition chain, primary-text links, and public-domain reasoning are recorded in `docs/super_events/015_utopia_manifesto_super_event_text_research.md`.

Audio ID `57` uses Johannes Brahms's *Symphony No. 3 in F major, Op. 90*, III. *Poco allegretto*, performed by the Musopen Symphony Orchestra. The specific recording is CC0 1.0 Universal. The source file, frozen Commons metadata and licence pages, exact checksums, edit record, final OGG/WAV paths, and uniqueness audit are recorded in `docs/super_events/015_utopia_manifesto_super_event_audio_research.md`. `music/chaosx_music_track_list.html` carries the active catalogue row.

The text and audio package is final and wired. The visual package is not complete: `interface/015_utopia_manifesto_super_event.gfx` registers five route-specific DDS paths for slots `96`-`100`, but those files do not yet exist. The two installed legacy super-event images are traceable generated assets from the superseded two-image presentation and are not fallbacks for the five current sprites.

## Assets

Runtime sprite registry: `interface/015_utopia_manifesto.gfx`

Asset package: `docs/assets/015_utopia_manifesto/`

Required icon and art families:

- one installed, provenance-traced opening report picture
- one installed, provenance-traced boundary-crisis news picture
- five route-specific super-event images, currently blocked at prompt-only status
- two installed, provenance-traced legacy super-event images that are not selected by current slots
- focus icons for every `GFX_goal_utopia_*`
- decision and category icons for every Event 015 decision surface
- idea icons for every Event 015 national spirit
- 12 achievement icons with grey and not-eligible variants
- cosmetic flags for New Utopia, Necessary Commonwealth, League of Need, and Marked Bounds State, including ideology-specific runtime variants
- Utopian Ledger background/header/warning panels
- animated GUI pieces with static fallbacks, live Ledger visibility triggers, and imagegen source-frame documentation

Focus, decision, decision-category, idea, achievement, cosmetic flag, and Ledger runtime GUI packages were generated through imagegen-backed asset subagents, then processed into final DDS/TGA runtime assets with manifests and contact sheets under `docs/assets/015_utopia_manifesto/`. The same manifest contains the non-icon event-art source ledger and the exact five-file super-event image blocker. Event 015 cannot claim a complete super-event image package until each current route sprite has a generated master, processed preview, final DDS, manifest row, and checksum evidence.

## Future Plans

- Add optional scripted GUI tabs for detailed ledger history, active integration projects, and League members.
- Add more state-specific text for Needful Land projects when region/culture data makes the local wording more precise.
- Add additional League behavior for multi-country cooperative wars if a later feature turns the lightweight member/confidence network into a broader diplomatic system.
- Add more route-specific AI personality tuning after observing live balance across very small minors, coastal minors, landlocked minors, and subjects.
