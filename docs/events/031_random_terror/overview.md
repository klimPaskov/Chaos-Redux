# Event 31 Random Terror

## Identity and pacing

Random Terror is Event `31`, enters through `chaosx.nr31.1`, remains a Minor Repeatable event at Chaos level `1`, and records one pacing event even though one bounded global wave can affect several eligible countries and exact states.

The hidden entry event calls `random_terror_run_global_wave`, refreshes the global ledgers, schedules eligible evolution or world-end work, and sends local report callbacks without allowing those callbacks to increment pacing again.

The accepted evolution names are Organized Cells, Transnational Terror Network, Territorial Insurgency, The Jihadist International, and The Final Jihad.

Global Jihad remains a scenario owned by Event 31, and The False Revelation remains the terminal world-end branch.

The accepted proposal for `SCN-014` collided with Fallout, and `SCN-015` is occupied by Missile Age.
Global Jihad uses triggerable-scenario slot `SCN-016` and its separate world-end registry uses slot 15.
Internal Fracture is not registered because its member package has not been accepted.

## State model

Every affected government maintains Terror Pressure, Response Legitimacy, incident count, response history, and mission locks.

Every affected state maintains activity, pressure, incident memory, exact civilian-loss accounting, cooldown state, territorial readiness, and action or mission commitments.

Later evolutions add Network Reach, International Unity, territorial-control values, actor authority, external supply, strategic victories, and hidden apocalyptic readiness without changing the identity-neutral baseline targeting rules.

Religion, ethnicity, nationality, refugee status, and ordinary ideology never increase baseline target or recruitment weight.

Evolution IV alone opens the wholly fictional jihadist branch, and its content includes opposition from Muslim governments, communities, clerics, soldiers, civic organizations, and fictional religious authorities.

The final entity is presented as an unexplained presence whose followers make a divine claim.
The game never confirms that it is Allah or any divine being.

## Outcomes and containment

The accepted baseline covers containment, continued spread, coups, civil war, state partition, territorial takeover, negotiated surrender, territorial actor formation, and defeat.
The current source contains those outcome families, with the unresolved unit, mission and transaction findings listed below.

Disabled evolutions leave the ordinary incident, containment, state-response, surrender, and defeat paths available.

The terminal transaction requires the normal Chaos and territorial-readiness gates even when Maximum Global Jihad activates The Final Jihad.

The actual terminal role requires the final profile, a country final-actor receipt and the active terminal transaction.
Ordinary JMX is a human Final Jihad command with ordinary ideas and three research slots.
Its symbolic Final Command Council precedes the entity, which is recruited without a leadership role and promoted only through the gated transaction.
The terminal marker supplies five slots and records the host's prior count for exact cleanup restoration.
The counteroffensive commits denial from its three-contribution quorum and terminal losses, allowing the objective to be established before the final-defeat predicate requires it.
Member consent, merger accounting, faction handling and the full aftermath retain open validation and implementation findings.

## Decisions, missions, and exact states

The system uses the compact government-response, actor-command, and False Revelation decision categories defined in `common/decisions/categories/031_random_terror_categories.txt`.

Government and actor actions use standard state-targeted decision presentation, concrete variable-backed costs, exact state flags, target locks, outcome helpers, AI weights, and cleanup hooks.

No Event 31-specific scripted GUI exists.

Global Jihad is registered in the shared `chaosx_scenarios_window` list with all five deployment types, all four intensities, dynamic descriptions and impact warnings, fail-closed launch status, and the Event 31 preflight transaction. Maximum enables The Final Jihad but only schedules The False Revelation through the ordinary `1000+` Chaos, readiness, unity, territorial-control, crisis-state, strategic-victory, and viable-actor gates.

## Territorial actors

Eight predeclared carrier tags provide bounded territorial-country capacity without dynamic tags, custom units, Event 19 providers, 3D models, custom unit sounds, or bespoke counters.

The carrier framework declares capitals, fictional leaders and councils, existing infantry templates, basic technology, manpower and equipment setup, focus loading and diplomatic or cleanup helpers.
The complete accepted country package requires dynamic safe capitals, resource-grounded forces, compatible donor research, functional economy, reinforcement, diplomacy, AI and playable cleanup.
The current capacity/force audit identifies gaps in those requirements and does not approve the eight declarations as complete packages.

The actor focus tree is `random_terror_actor_focus_tree` in `common/national_focus/031_random_terror_focus.txt`.

Its 114 focuses cover opening survival, Shadow Council, War Directorate, Ideological Secretariat, captured economy, armed movement, network and diplomacy, expansion, crisis, Jihadist International, Final Jihad, and False Revelation routes.

## Visual assets and wiring

The authoritative visual audit is `docs/plans/031_random_terror_plans/031_random_terror_visual_asset_audit.md`.

Base sprites are registered in `interface/031_random_terror.gfx` and the 114 focus shine sprites are registered in `interface/031_random_terror_shine.gfx`.

Focus icons live under `gfx/interface/goals/031_random_terror/` and use `GFX_goal_random_terror_*` plus exact `_shine` counterparts.

Idea icons live under `gfx/interface/ideas/031_random_terror/` and use `GFX_idea_random_terror_*`.

Decision and mission icons and the three category pictures live under `gfx/interface/decisions/031_random_terror/` and use `GFX_decision_random_terror_*`, `GFX_decision_mission_random_terror_*`, and the three consumed `GFX_decision_category_031_random_terror_*` sprites.

Six news pictures and sixteen accepted report pictures live under `gfx/event_pictures/031_random_terror/`.

`GetRandomTerrorIncidentReportPicture` selects baseline report art from the incident type preserved by the global wave, while evolution, diplomacy, terminal, and defeat events use fixed report consumers.

Portraits live under `gfx/leaders/031_random_terror/`.

The ten-frame entity sheet lives at `gfx/interface/animated/031_random_terror/false_revelation_entity_sheet.dds`, is registered as `GFX_Portrait_Random_Terror_Entity_Animated`, and is consumed by Evolution V in the shared Event Details portrait selector.

The explicit static fallback is `GFX_Portrait_Random_Terror_Entity_Static_Fallback`, consumed by the final actor character.

Four large two-frame faction emblems and four miniature emblems live under `gfx/interface/emblems/031_random_terror/` and are consumed by the regional coordination, network confederation, Jihadist International, and Final Command faction transactions.

Thirty-seven fictional cosmetic identities provide 111 normal, medium, and small TGA files under the standard `gfx/flags/` roots, alongside 24 base flag files for the eight carrier tags.

Deterministic ordinary, transnational, and jihadist cycles expose all active identities over carrier generations, while cleanup assigns all eight dormant identities and the terminal actor uses the unique final identity.

Achievement states live directly under the engine-facing `gfx/achievements/` root as twelve colored, twelve grey, and twelve not-eligible DDS files whose basenames match their achievement IDs.

## Achievement coverage

The single root registry in `common/achievements/chaos_redux_achievements.txt` exposes the twelve accepted Event 031 IDs below.

| Achievement ID | Persistent proof flag | Visibility | Runtime icon aliases |
| --- | --- | --- | --- |
| `031_no_second_blast` | `random_terror_achievement_no_second_blast` | Visible | `GFX_achievement_031_no_second_blast[_grey|_not_eligible]` |
| `031_the_long_watch` | `random_terror_achievement_the_long_watch` | Visible | `GFX_achievement_031_the_long_watch[_grey|_not_eligible]` |
| `031_the_city_still_stands` | `random_terror_achievement_the_city_still_stands` | Visible | `GFX_achievement_031_the_city_still_stands[_grey|_not_eligible]` |
| `031_cut_every_route` | `random_terror_achievement_cut_every_route` | Visible | `GFX_achievement_031_cut_every_route[_grey|_not_eligible]` |
| `031_the_false_claim_rejected` | `random_terror_achievement_false_claim_rejected` | Visible | `GFX_achievement_031_the_false_claim_rejected[_grey|_not_eligible]` |
| `031_no_collective_punishment` | `random_terror_achievement_no_collective_punishment` | Visible | `GFX_achievement_031_no_collective_punishment[_grey|_not_eligible]` |
| `031_enemy_of_my_enemy` | `random_terror_achievement_enemy_of_my_enemy` | Visible | `GFX_achievement_031_enemy_of_my_enemy[_grey|_not_eligible]` |
| `031_fracture_from_within` | `random_terror_achievement_fracture_from_within` | Hidden | `GFX_achievement_031_fracture_from_within[_grey|_not_eligible]` |
| `031_maximum_survivor` | `random_terror_achievement_maximum_survivor` | Visible | `GFX_achievement_031_maximum_survivor[_grey|_not_eligible]` |
| `031_false_revelation_denied` | `random_terror_achievement_false_revelation_denied` | Hidden | `GFX_achievement_031_false_revelation_denied[_grey|_not_eligible]` |
| `031_victims_before_victory` | `random_terror_achievement_victims_before_victory` | Visible | `GFX_achievement_031_victims_before_victory[_grey|_not_eligible]` |
| `031_war_without_a_capital` | `random_terror_achievement_war_without_a_capital` | Hidden | `GFX_achievement_031_war_without_a_capital[_grey|_not_eligible]` |

Completion predicates live in `common/scripted_triggers/031_random_terror_triggers.txt` and read proof flags produced by `common/scripted_effects/031_random_terror_achievement_effects.txt`.

The existing `on_daily` country pass calls `random_terror_achievement_daily_tick` only for Event 031 affected countries, actors, or initialized ledgers, so historical counters survive ordinary save and reload without adding a second world iteration.

Event 031 thresholds use the existing `random_terror_tuning` script constants, including the 180-day crisis window, pressure gates, legitimacy gates, corridor count, route stage size, movement duration, capital recovery window, and major-loss threshold.

The Network Authority text icon lives under `gfx/texticons/031_random_terror/`.

Two super-event pictures live under `gfx/super_events/031_random_terror/`, are registered in `interface/chaosx_super_events.gfx`, and use a public-domain or licensed WAV package played through the shared settings-aware super-event audio helper.

## Validation surfaces

The current visual inventory contains 444 runtime files and is recorded row by row in `docs/plans/031_random_terror_plans/031_random_terror_visual_asset_inventory.md`.

The complete event remains incomplete.

Nine portrait identities have history recruitment and reachable role consumers, including the gated entity and human Final Command Council.
Thirty-six additional identities have roleless definitions and a durable source archive, with recruitment, selection and recycling still open.
Original per-image prompt records and two current source-to-DDS equality records remain missing.
The capital-defense mission icon uses the reviewed native-alpha edit, with its inherited background-removal procedural gap resolved.
The full achievement audit retains player-identity observation limits, and numerical probability comparison and final subsystem audits remain unresolved.

The bounded multi-country wave repair is implemented in commit `b10e6a30292a51d09104aa1c120ab9843be6db25`, with source and acceptance evidence in `docs/plans/031_random_terror_plans/subagent_handoffs/031_multi_country_wave_scope_repair_20261003.md`.
Candidate-state controller checks use the candidate's PREV scope, owned-and-controlled draws use intrinsic state eligibility, and action targets retain their explicit ROOT contract.
The mapped callers initialize temporary outputs and pool storage, and automatic reservations follow successful incident application.
The one-firing pacing path, raw ticket curve, provider definitions, cap, attempt counts and two-day reservation remain unchanged.
The named wave baseline and comparison handoffs preserve the unchanged 17-case fixture, with 600-second failures and no numerical artifact.
The narrower shared-curve comparison is still unreturned in the handoff, so normalized probabilities, complete provider pools and native execution remain unresolved.
The newer mission audit in `docs/plans/031_random_terror_plans/subagent_handoffs/031_mission_owner_and_progress_contract_20261003.md` identifies cross-country consumption and cleanup of all eight generic mission subjects, owner-local recovery performing global cleanup, and shared-slot activation of the wrong mission family.
Five success predicates lack an independently reachable progress producer, while the hostage slot blocks its only current progress action and its accepted partial outcome is missing.
Mission receiver isolation is implemented in `38fd9b9da337f647f91a804628a24d3216075cb6`, with receiver-keyed subjects, family locks, guarded callbacks and exact-state descriptions.
Restoration reserves its slot before invoking its helper, recovery waits for active missions to resolve, and only successful timed restoration records completed civil authority for the achievement check.
The independent source review found no receiver-isolation defect, while the same-fixture numerical comparison remains blocked by archived-source recognition.
Mission progress and outcome implementation remains incomplete.
Foreign-owned controlled targets, external retake targets and controller-owned hostage/uprising missions remain part of the accepted design.
The decision audit also retains split actor-control values, incomplete click-time affordability and exact-balance handling, missing cost companions, excessive target-row fan-out and actor operations that record receipts without performing the promised unit changes.
The carrier audit identifies undeployed-carrier false-negative gates, occupied-tag reuse, stage-blind capacity counting, Maximum/map preflight gaps, weak geography constraints and unresolved force/research sources.
The mapped accepted contracts remain implementation work under the user's instruction to complete the accepted specs and visual audit.
Audit suggestions and proposed regression fixtures remain recommendations until the parent reviews them, and no gameplay simplification is approved.
Carrier, force, technology, economy, exact-cost, AI and full terminal-atomicity coverage remain open.

Detected daily control changes disqualify only the changed country, preserving unrelated player countries' eligibility.

Same-day round trips and swaps between already-human countries remain unresolved because the daily country marker does not identify individual clients.

The Event 31 CXT daily hook registers newly discovered content and marks it pending for manual application.

The compact scenario-list label is `#016`, while the stable Global Jihad catalog identifier is SCN-016.
The existing adjacent `#018` scenario label and SCN-018 identifier are preserved.

Capital-dependent achievement tracking stores each government's exact original state and separately records the capital at Maximum scenario confirmation.

Retaking and restoration proof requires a matching country-owned identity, current control is checked at completion, and repeated loss cannot extend the recovery deadline.

The source repair and validation limits are recorded in `docs/plans/031_random_terror_plans/subagent_handoffs/031_achievement_capital_identity_repair_20261003.md`.

The workbook mirrors Event 31 localisation and contains Global Jihad as SCN-016, with Event 31 classified as `To Be Reworked` and Global Jihad as `Needs Testing`.

No Internal Fracture cluster is registered by this implementation.

The achievement active-state count credits the government owning the counted states, including when the global wave's event root is a different country.

The exact repair and its validation limits are recorded in `docs/plans/031_random_terror_plans/subagent_handoffs/031_achievement_count_scope_repair_20261003.md`.

Measured casualty receipts are implemented in commit `bbb2ba6f90ec75462cb94f7274122c52df4abcb3` under the accepted civilian-loss and achievement contracts.
`random_terror_apply_exact_state_loss` initializes both helper outputs, reads measured applied loss for the major-loss receipt and records that same measured amount rather than the requested loss.
The strict major-loss threshold remains greater than 400 people, with the 0/300/400/450 boundary model and full validation limits recorded in `docs/plans/031_random_terror_plans/subagent_handoffs/031_measured_casualty_receipt_repair_20261003.md`.
The current checkpoint lists eleven bounded repair commits and keeps full Event 31 validation open.

The historical HOI4 focus route resolves one 114-focus tree with 114 titles, zero connector crossings and zero same-row spacing violations.
Its structural render is 8,752 by 3,136.
The post-fix decoded-icon raster route timed out after 180 seconds, so the earlier decoded raster remains icon evidence and does not prove post-fix topology.

The event inspector accepts the Event 31 root and returns a partial artifact without an Event 31-specific blocker.

The installed event renderer accepted an exact namespace selector but expanded into a full-workspace render and did not complete after more than six minutes, so namespace-scoped renderer evidence remains an exact tool-route blocker rather than being replaced by source-only proof.

The historical mandatory GUI inspector and renderer completed for `chaosx_scenarios_window` with Event 31 selected, Random Pattern and Maximum at 1920x1080 and UI scale 1.
The inspector reported no missing fields.
Shared-window overlap and alignment findings remain open.
Current narrowed event/reference requests and terminal-role probability comparisons timed out after 600 seconds, with exact limitations in the MCP ledger and specialist handoffs.

## Future extensions

Optional future work can add more fictional incident compositions or additional non-weighted cosmetic identities only when they receive exact consumers, complete source and rights evidence, and the same native-scale audit.

Optional work must not add real extremist identities or symbols, sacred hostile branding, a dedicated Event 31 GUI, a custom unit, an Event 19 provider, a 3D model, a custom unit sound, or a bespoke counter.
