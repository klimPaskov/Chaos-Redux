# Event 006 Improvement Addendum: Post Focus and Formation Tranche

Status: open implementation plan.

Closure recommendation: do not close Event 006 yet. The first focus and formation tranche establishes the release origin, provisional tree, route locks, congress scaffolding, and a first Formation Ledger path. It does not yet satisfy the source-spec promise for package depth, route-specific formations, aftermath management, GUI value, visual state, catalog alignment, achievements, or final audit gates.

Prior addendum check: no earlier `006_independence_wave_improvement_addendum_*` file is present in `docs/plans/006_independence_wave_plans/`. The existing gate, foundation handoff, and audit handoffs remain active context rather than unresolved competing addenda.

## Accepted Closure Criteria Already Met

These points should be preserved and treated as accepted foundations, not redesigned:

- Event 006 has a distinct runtime origin through `chaosx_release_origin_independence_wave` and should remain separate from Event 005 Soviet Collapse systems.
- The release wave fires immediately from `events/006_independence_wave.txt`; dossiers, decisions, ledger work, and GUI surfaces manage aftermath rather than delaying release.
- The current resolver avoids releasing a candidate whose core covers the host capital and checks a host-state floor before each release. The next pass should harden this into a capital-preferred reserved-state solver, not replace the instant-release model.
- Released countries load `common/national_focus/006_independence_wave_focus.txt` through `independence_wave_load_liberation_focus_tree`, giving Event 006 a provisional focus surface.
- The provisional focus tree already has four route locks: observer charter, officer mandate, national directory, and sponsored cabinet. New route content should attach to these identities instead of creating a second opening tree.
- `common/decisions/006_independence_wave_decisions.txt` includes initial aftermath, committee survival, New States Congress, and Formation Ledger categories.
- Regional compact formation exists as a first Formation Ledger path, with `independence_wave_prepare_regional_compact`, `independence_wave_proclaim_regional_compact`, and `independence_wave_integrate_compact_ministries`.
- Basic constants, ideas, scripted triggers, localisation, and docs exist for the current tranche.

## Unresolved Expansion Items

The first tranche is intentionally incomplete. The next implementation should focus on these concrete depth additions before any closure handoff:

- The package ladder is still ordinary-dominated. Higher chaos release pools for dormant tags, city states, protectorates, historical-return tags, local-polity packages, strange packages, and hidden formables remain unwired.
- Regional compact formation is still a light proof of concept. It needs real member proof, route-gated political checks, post-formation risk, and event log integration before it can carry the "First League" super-event or related achievements.
- The national directory/border branch currently prepares claim ambition but does not have a playable Border Commission decision family.
- Historical-return and local-polity route content is mostly represented by reveal clues rather than country packages, bespoke focuses, decisions, flags, assets, and AI behavior.
- Dossier Board, Patron Ledger, and Formation Ledger remain decision-category scaffolds. Full scripted GUI should wait until stable variables and target lists exist, but the next pass should register the data model and animated asset needs.
- No package-specific formation decisions exist for Volga Bulgaria/Old Great Bulgaria, Assyria, Mapuche, Buganda/Asante, free ports, railway polities, or strange packages.
- Super-events, audio, achievements, catalog rows, event details, and asset manifests are not implementation-ready for completion claims.
- The current focus tree lacks revolutionary, dedicated anti-patron, crisis, free city/free port, railway sovereignty, and strange-state modules identified by the source specs and focus audit.

## Addendum Scope

Implement the next tranche as a bounded "package and ledger hardening" pass. It should make a small set of package families real, strengthen the existing regional compact, and give the border route an actual decision loop. Do not attempt the full Event 006 end-state in one patch.

The implementation should touch these gameplay surfaces when accepted by the parent:

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/decisions/categories/006_independence_wave_categories.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `common/ideas/006_independence_wave_ideas.txt`
- `events/006_independence_wave.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `interface/006_independence_wave*.gfx` if new sprites are registered
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/` after the plan is accepted and promoted
- catalog, event-detail, achievement, super-event, and asset docs only when implementation facts exist

Do not patch Event 005 files for this tranche. Shared tags such as Old Great Bulgaria may be referenced only through Event 006 origin checks and separate Event 006 content.

## Expansion 1: Resolver and Package Registry Hardening

Purpose: make the release system capable of selecting more than ordinary releasables while preserving instant release and host survival.

Add package-family constants or documented enum values for:

- `ordinary`
- `dormant`
- `game_rule`
- `protectorate`
- `city`
- `railway`
- `historical_return`
- `local_polity`
- `strange`

If existing numeric values are renumbered, migrate every scripted trigger, effect, decision, localisation condition, and doc reference in the same patch. Prefer explicit named script constants where supported.

Required helper design:

- `independence_wave_score_candidate_package_type`: assigns a candidate package family and score from chaos tier, candidate status, state pattern, host conditions, and route unlocks.
- `can_independence_wave_candidate_enter_dormant_pool`: blocks tags without viable state support, avoids Event 005 origin routes, and requires higher chaos than ordinary releases.
- `can_independence_wave_candidate_enter_city_pool`: checks that the candidate can plausibly operate as a city/free-port polity without erasing the host capital.
- `can_independence_wave_candidate_enter_railway_pool`: checks rail or junction relevance before using railway sovereignty content.
- `can_independence_wave_candidate_enter_protectorate_pool`: checks patron influence or observer/sponsored route conditions.
- `can_independence_wave_candidate_enter_historical_pool`: checks historical-return reveal flags and package-specific state groups.
- `can_independence_wave_candidate_enter_local_polity_pool`: checks local-polity reveal flags and package-specific state groups.
- `can_independence_wave_candidate_enter_strange_pool`: locks impossible states to high chaos and explicit strange-route unlocks.
- `independence_wave_reserve_host_survival_state`: records the host state that must never be released in the current wave, preferring the capital and falling back only to a controlled non-capital if the capital cannot be protected by the candidate scan.
- `independence_wave_apply_candidate_shrink_or_skip`: removes protected states from a candidate release if the engine surface supports it; otherwise skips that candidate. Do not use a silent fallback. If shrink behavior cannot be implemented cleanly, the parent should stop and decide between skip-only release selection or a more detailed state-transfer solver.
- `independence_wave_clear_pending_candidate_state`: clears temporary variables, event targets, and candidate flags after each scan.

Event targets are acceptable when the effect chain needs stable host or candidate scopes. Use regular event targets for short chains. Use global event targets only when persistence beyond the chain is required, and clear them in the same system.

Do not add `on_daily`, `on_weekly`, or other whole-world polling for this package registry. The resolver should run from the Event 006 event/effect chain and explicit decisions.

## Expansion 2: Make the Regional Compact a Real Formation

Purpose: turn the existing Formation Ledger path into a real political project with member proof, risks, AI behavior, and later super-event eligibility.

Current identifiers to keep:

- `independence_wave_prepare_regional_compact`
- `independence_wave_proclaim_regional_compact`
- `independence_wave_integrate_compact_ministries`
- `independence_wave_formation_ledger_category`
- `independence_wave_new_states_congress_category`
- `can_independence_wave_proclaim_regional_compact`

Add formation state:

- `independence_wave_compact_founder`
- `independence_wave_compact_member`
- `independence_wave_compact_member_count`
- `independence_wave_compact_charter_open`
- `independence_wave_compact_charter_failed`
- `chaosx_formation_origin_independence_wave`
- `chaosx_independence_wave_formable_family = regional`

Strengthen `can_independence_wave_proclaim_regional_compact` so the decision requires:

- the actor is an Event 006 release
- Formation Ledger has been revealed
- compact petition has been prepared
- at least three living Event 006 releases can qualify as members
- member candidates are independent or not under a major protector
- member candidates are not actively at war with each other
- the founder has enough coalition cohesion, legitimacy, or observer backing
- the compact has not already failed
- no Event 005 Soviet Collapse origin tag is counted

Add decisions or missions:

- `independence_wave_invite_compact_delegate`: targeted decision against eligible Event 006 releases; adds member support or refusal cooldown.
- `independence_wave_draft_anti_puppet_clause`: observer/civic route decision that blocks major-patron capture but costs political power and legitimacy.
- `independence_wave_compact_charter_window`: timed mission after enough delegates support the compact; failure reduces cohesion and locks a retry cooldown.
- `independence_wave_arbitrate_member_dispute`: targeted decision to repair a member conflict before proclamation.
- `independence_wave_recognize_compact_secretariat`: post-formation decision that stabilizes the compact but requires continued member independence.

Post-formation mission behavior:

- Keep `independence_wave_integrate_compact_ministries`, but require ongoing member count and cohesion rather than a passive timer.
- Failure should not delete the country. It should remove compact bonuses, mark the formation as discredited, and open a recovery decision.

AI behavior:

- Civic/observer route actors should prefer anti-puppet clause and arbitration.
- Officer route actors should form compact only when their military strength is not lower than nearby hostile claimants.
- Sponsored cabinet actors should avoid the compact unless patron leverage is low or the patron is not a major.
- National directory actors should prefer border leverage over compact diplomacy unless cohesion is unusually high.

Event log and super-event surface:

- Add or reserve log key `chaosx_event_006_log_first_league` only when a compact is actually proclaimed.
- The `First League` super-event should remain blocked until the compact has at least three independent Event 006 members, an implemented event log entry, sourced art, sourced audio, and a completed super-event handoff.

## Expansion 3: Border Commission Decision Family

Purpose: give the national directory and border-claim branch real gameplay that does not become free coring or host erasure.

Use a decision-category family rather than full scripted GUI for the first pass. Either create `independence_wave_border_commission_category` or keep the family inside an existing Event 006 category if UI clutter is lower. The category must have clear reveal conditions from focus route or package state.

Proposed identifiers:

- `independence_wave_file_border_survey`
- `independence_wave_petition_border_parish`
- `independence_wave_request_league_arbitration`
- `independence_wave_offer_protected_transfer`
- `independence_wave_issue_dossier_ultimatum`
- `independence_wave_freeze_claim_under_observers`
- `independence_wave_border_commission_cooldown`
- `independence_wave_border_dispute_failed`

Mechanical rules:

- Border targets must come from named state groups or package definitions, not generic nearest-state grabs.
- A state reserved for host survival may never be targeted by the initial wave or by a border commission transfer.
- Border Commission outcomes should start with claims, demilitarized pressure, autonomy guarantees, or temporary integration missions. Full cores require later package-specific proof.
- `offer_protected_transfer` should require the target owner to be weak, friendly, or patron-aligned and should cost political power plus legitimacy or patron leverage.
- `issue_dossier_ultimatum` should be available mainly to national directory/officer actors, should carry war-risk or stability-risk, and should have restrained AI weights.
- `request_league_arbitration` should be the civic/observer route answer and should be slower but safer.

Costs:

- Arbitration: political power and coalition cohesion.
- Survey: command power or infantry equipment, plus time.
- Protected transfer: political power, legitimacy, and patron leverage if sponsored.
- Ultimatum: command power, stability risk, and border-dispute cooldown.

AI behavior:

- Do not let AI spam border claims. Use cooldowns and a limited open-dispute count.
- AI civic/observer actors prefer arbitration unless already threatened.
- AI national directory actors use ultimatums only with clear strength advantage and no major protector on the target.
- AI sponsored actors use protected transfer only when the patron is not the target or target protector.

## Expansion 4: Starter Package Overlay Set

Purpose: implement a small, source-aware starter set rather than generic country packages. The parent should pick three historical/local packages plus one structural package for the next tranche.

Each accepted package needs:

- release enablement trigger
- package family assignment
- reveal focus or decision
- formation decision if eligible
- state-group proof
- route locks or route bonuses
- post-formation mission
- AI behavior
- localisation
- asset manifest entries
- event log or catalog hook if it can become a major world event

### Package A: Volga Bulgaria / Old Great Bulgaria as Event 006 Overlay

Working package id: `iw_pkg_volga_bulgaria`.

Existing shared tag risk: repo inspection shows Old Great Bulgaria content already exists outside Event 006. This package is useful precisely because it tests Event 006/Event 005 separation. It must never call Event 005 loaders, missions, formables, or Soviet Collapse origin checks.

Core route:

- reveal flag: `independence_wave_volga_archive_opened`
- package family: `historical_return`
- formation family: `old_name_assembly`
- origin guard: `chaosx_release_origin_independence_wave`

Focus anchors:

- `independence_wave_volga_archive_opened`
- `independence_wave_merchants_of_the_river_road`
- `independence_wave_kama_defensive_line`
- `independence_wave_council_of_the_old_name`
- `independence_wave_modern_volga_republic`
- `independence_wave_steppe_memory_unbound`

Decision and mission anchors:

- `independence_wave_convene_volga_archive_assembly`
- `independence_wave_proclaim_volga_bulgar_assembly`
- `independence_wave_integrate_volga_kama_ministries`

Design direction:

- Use Volga/Kama trade, river corridor memory, and archive legitimacy as the modern political frame.
- Do not make it a Soviet Collapse branch.
- Do not give free steppe conquest. Border claims must pass through the Border Commission or package-specific state proof.
- If the package uses the existing OGB tag, every focus, idea, decision, and cosmetic tag must check Event 006 origin before enabling.

Assets:

- `GFX_decision_independence_wave_volga_archive`
- `GFX_focus_independence_wave_volga_trade_road`
- `GFX_idea_independence_wave_volga_old_state_memory`
- animated major-route seal only if this package becomes a route centerpiece

Research basis:

- Current Event 006 research notes identify Volga Bulgaria as a high-chaos historical-return candidate. Final claims, flag use, and art sourcing need a dedicated source pass before implementation.

### Package B: Assyria / Northern Mesopotamian Recognition Congress

Working package id: `iw_pkg_assyria`.

Tag status: uncertain. Implement only after confirming whether a suitable tag exists or after the parent creates a non-generic tag package. Do not fake this through an unrelated vanilla tag.

Core route:

- reveal flag: `independence_wave_assyrian_archive_opened`
- package family: `historical_return`
- formation family: `recognition_congress`

Focus anchors:

- `independence_wave_nineveh_petition_archive`
- `independence_wave_guards_of_the_plain`
- `independence_wave_congress_of_exiles`
- `independence_wave_modern_assyrian_state`
- `independence_wave_imperial_shadow_rejected`
- `independence_wave_imperial_shadow_embraced`

Decision and mission anchors:

- `independence_wave_open_assyrian_archive`
- `independence_wave_form_assyrian_recognition_congress`
- `independence_wave_integrate_nineveh_ministries`

Design direction:

- Center modern recognition, community security, diaspora/exile politics, and minority protection.
- Ancient imperial imagery may appear as contested memory, not as the default conquest route.
- State groups should be source-reviewed around northern Mesopotamia/Nineveh/Khabur/Mosul where the map supports them.

Assets:

- `GFX_decision_independence_wave_nineveh_petition`
- `GFX_focus_independence_wave_congress_of_exiles`
- `GFX_idea_independence_wave_minorities_guarded`

Research basis:

- Event 006 research notes list Assyria/Mesopotamia as a high-chaos candidate. Final implementation needs tag, state, symbol, and leader/source verification.

### Package C: Mapuche Land Congress

Working package id: `iw_pkg_mapuche`.

Core route:

- reveal flag: `independence_wave_mapuche_land_congress_open`
- package family: `local_polity` or `historical_return`, depending on final tag/state support
- formation family: `land_congress`

Focus anchors:

- `independence_wave_mapuche_land_congress`
- `independence_wave_frontier_treaty_archive`
- `independence_wave_community_guard`
- `independence_wave_recognition_without_a_patron`
- `independence_wave_araucania_border_defense`

Decision and mission anchors:

- `independence_wave_convene_mapuche_land_congress`
- `independence_wave_map_communal_lands`
- `independence_wave_ratify_araucania_authority`

Design direction:

- Use treaty memory, community defense, land congress politics, and patron-resistant recognition.
- Avoid a monarchist novelty route as the main line.
- Border content should route through surveys, arbitration, and communal land mapping rather than instant cores.

Assets:

- `GFX_decision_independence_wave_land_congress`
- `GFX_focus_independence_wave_frontier_treaty_archive`
- `GFX_idea_independence_wave_community_guard`

Research basis:

- Event 006 research notes list Mapuche as a local-polity/historical-return candidate. Final state groups, names, symbols, and leaders require source review.

### Package D: Buganda Lukiko / Protectorate Record

Working package id: `iw_pkg_buganda`.

Core route:

- reveal flag: `independence_wave_buganda_lukiko_open`
- package family: `protectorate` or `local_polity`
- formation family: `constitutional_kingdom`

Focus anchors:

- `independence_wave_buganda_lukiko_session`
- `independence_wave_kabaka_question`
- `independence_wave_lake_victoria_couriers`
- `independence_wave_protectorate_records`
- `independence_wave_constitutional_kingdom`

Decision and mission anchors:

- `independence_wave_convene_lukiko_council`
- `independence_wave_renegotiate_protectorate_record`
- `independence_wave_form_buganda_recognition_state`

Design direction:

- Frame the route around a council/constitutional settlement, protectorate records, lake-region logistics, and the kabaka question.
- Avoid invented real-person portraits or unsourced royal symbolism.
- Sponsored cabinet actors can interact with the protectorate record, but Event 006 should not hand control to a major patron by default.

Assets:

- `GFX_decision_independence_wave_lukiko_council`
- `GFX_focus_independence_wave_lake_victoria_couriers`
- `GFX_idea_independence_wave_protectorate_record`

Research basis:

- Event 006 research notes identify Buganda as a plausible local-polity/protectorate package. Final symbols, leadership, and state groups need source review.

### Package E: Free Port or Railway Sovereignty

Working package id: choose one for the next tranche:

- `iw_pkg_free_port`
- `iw_pkg_railway_sovereignty`

Purpose:

- Connect the current port and railway support focuses to a mid-chaos structural package that is not just another historical return.

Free port anchors:

- `independence_wave_free_port_customs_board`
- `independence_wave_secure_customs_house`
- `independence_wave_harbor_neutrality`
- `independence_wave_proclaim_free_port_compact`

Railway anchors:

- `independence_wave_junction_committee`
- `independence_wave_bridge_guard`
- `independence_wave_timetable_authority`
- `independence_wave_railway_league_of_corridors`

Costs and checks:

- Free port content should use convoys, fuel, trade influence, and port control.
- Railway content should use trains, command power, infrastructure control, and corridor security.
- Neither package should erase a host capital or convert arbitrary inland states into ports/corridors.

Assets:

- `GFX_decision_independence_wave_customs_board`
- `GFX_decision_independence_wave_timetable_authority`
- `GFX_focus_independence_wave_harbor_neutrality`
- `GFX_focus_independence_wave_bridge_guard`

## Expansion 5: Ledger GUI and Asset Data Model

Purpose: prepare meaningful GUI surfaces without building a decorative panel before the data exists.

Next tranche should stay with decision-category ledgers unless the parent implements stable target arrays and helper state first. Full scripted GUI is useful only after it can show live package data, member status, protected host state, open border disputes, and formation eligibility.

Decision-category surfaces:

- `independence_wave_formation_ledger_category`: formation decisions, compact charter, package proclamations.
- `independence_wave_new_states_congress_category`: delegate work, anti-puppet clause, observer recognition.
- `independence_wave_host_aftermath_category`: host survival, ministry continuity, capital-rump story.
- Optional `independence_wave_border_commission_category`: only if border decisions become dense enough to need separation.

Data to expose through dynamic localisation:

- release origin
- package family
- protected host state
- actual release count
- compact member count
- current open border dispute count
- formation family
- patron leverage if sponsored cabinet is active
- whether the package is eligible for an animated major-route state

Sprite registrations to reserve when accepted:

- `GFX_decision_category_independence_wave_dossier`
- `GFX_decision_category_independence_wave_congress`
- `GFX_decision_category_independence_wave_formations`
- `GFX_decision_category_independence_wave_border_commission`
- `GFX_independence_wave_formation_seal`
- `GFX_independence_wave_formation_seal_animated`
- `GFX_independence_wave_congress_charter_seal_animated`
- `GFX_independence_wave_host_rump_candle_animated`

Animated major-state rule:

- Animated sprites are required only for major route states, but when they are used they must be real frame assets with source frames, processed sheet, static fallback, preview, manifest, `.gfx` handoff, and implementation notes. Do not accept static-only replacements for major animated UI states.

Asset handoff requirement:

- Route any animated seal, congress glow, host-rump candle, or package centerpiece through the event asset and frame-animation workflows before implementation.
- Register placeholder-safe sprite names in `.gfx` only after the parent accepts the visual surface. Placeholder art must be replaceable without renaming.

## Expansion 6: Super-Events, Audio, Achievements, and Catalog

Purpose: block premature prestige surfaces while giving the parent exact unlock criteria.

Super-events:

- No base Independence Wave super-event.
- `independence_wave_first_league`: unlock only after a strengthened regional compact has at least three independent Event 006 members, an event log entry, sourced art, sourced audio, and a completed super-event handoff.
- `independence_wave_first_old_name`: unlock only after the first real historical-return or local-polity formation succeeds with package-specific state proof and sourced visual/audio material.
- `independence_wave_the_rump_that_endures`: unlock only after the reserved-state solver can prove a host survived at one state or capital-rump scale without being erased.

Audio:

- Do not implement placeholder audio. The audio handoff must name candidate public-domain or properly sourced tracks, legal/source notes, loop/edit guidance, and mood justification.

Achievements:

- `cr_not_the_collapse`: Event 006 shared-tag origin proof, especially for Old Great Bulgaria/Volga. Must be impossible from Event 005.
- `cr_charter_becomes_state`: proclaim a strengthened regional compact after delegate proof.
- `cr_the_ledger_votes_back`: reverse a failed compact or border dispute through ledger decisions.
- `cr_capital_still_answers`: host survives at the protected capital after an Event 006 wave. Only add after the reserved-state solver is implemented.

Catalog and event details:

- Update catalog rows, event details, and event log text only from implemented facts.
- Do not copy this plan into player-facing wording. Localisation should describe the current world state and choices, not implementation history.

## Research Basis and Required Follow-Up

This addendum relies on the Event 006 source-spec pack, especially the research notes and country-package spec, plus current repo inspection of the implemented first tranche. Historical connections are design anchors, not final source claims.

Before implementation of each package, the parent should verify:

- tag availability or new-tag need
- state IDs and state groups
- naming and cosmetic tags
- symbols, flags, portraits, and icon references
- whether named institutions or leaders are appropriate for the selected year and route
- whether any shared tag has Event 005 content that must be blocked by Event 006 origin checks

Uncertain claims:

- Assyria package state group and tag availability are not confirmed.
- Mapuche state groups and final naming require source review.
- Buganda leadership/symbol handling requires source review to avoid invented real-person content.
- Volga Bulgaria/Old Great Bulgaria is viable as a separation test only if every Event 006 path is origin-guarded from Event 005.

## Audit Gates After Implementation

Run these checks before any completion claim:

- Resolver/helper review by a scripted-system architect or equivalent manual audit, covering event targets, package family constants, reserved host state, and cleanup.
- Focus tree audit after package branches are added, verifying route locks, prerequisites, AI weights, and no dead-end focus paths.
- Decision/mission audit after compact, border, and package formation decisions are added, verifying costs, cooldowns, targeted scopes, dynamic localisation, and AI behavior.
- Country package audit for each accepted starter package, verifying state groups, tags, formation eligibility, post-formation missions, and no generic placeholder packages.
- Localisation audit for every focus, idea, decision, mission, event log, achievement, GUI sprite, and dynamic loc key.
- Asset handoff audit for every registered sprite and every animated major-route state.
- Super-event and audio audit before any super-event is wired.
- Completion audit only after specs, docs, catalog, achievements, assets, and validation scenarios match implemented behavior.

Scenario gates:

- Low-chaos ordinary wave still releases ordinary releasables immediately.
- Host keeps at least one state, preferably capital, through the resolver and through any border-transfer decisions.
- Event 006 Old Great Bulgaria/Volga never loads Event 005 Soviet Collapse content.
- Regional compact cannot form from a single isolated country.
- Border Commission cannot core or transfer the host survival state.
- Package formation decisions verify map control and package proof rather than relying only on focuses.
- No GUI button exists without cost, tooltip, AI behavior if AI-usable, cleanup, and helper logic.
- No achievement can fire from debug state, wrong origin, or Event 005 route.
- No base Event 006 super-event fires for a normal release wave.

## Promotion Guidance

Keep this file in `docs/plans/006_independence_wave_plans/` until the parent accepts the next tranche. If accepted, promote the concrete parts into:

- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md` for starter packages and state-group requirements.
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md` for focus anchors and route locks.
- `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md` for compact, border, formation, AI, cost, and cleanup rules.
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md` for sprite names and animated asset families.
- `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md` only for super-event candidates whose unlock conditions are implemented or explicitly queued.
- `docs/specs/006_independence_wave_specs/006_independence_wave_achievements_prompt.md` for origin-safe achievements.

Do not mark Event 006 complete while this addendum remains accepted but unimplemented.
