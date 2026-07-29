# Event 020 rat system and country package audit

> Superseded by the two-tag correction handoff dated 2026-07-29. This historical audit predates the registered package and the single reusable RTA carrier; its former multi-carrier findings are retained for provenance only, not as current implementation requirements.

## Scope and ownership

This audit covers the rat effects, triggers, constants, MTTH, country registration, history, units, ideas, focus trees, decisions, AI, localisation, assets, and Event 20 callback surfaces required by docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_4_evolutions_and_rat_emergence.md, part_5_rat_nations.md, part_6_rat_king.md, and part_7_world_end_and_aftermath.md.

No gameplay file was patched in this audit. The parent agent is implementing evolution dispatch and logging in a separate common/scripted_effects/020_black_plague_evolution_effects.txt surface, so this handoff deliberately does not rewrite common/scripted_effects/020_black_plague_rat_effects.txt or the shared scheduler.

## Executive result

The rat package is currently an unregistered, unwired draft. common/scripted_effects/020_black_plague_rat_effects.txt contains allocator and transfer stubs, but the referenced tags, country files, unit definitions, ideas, focus trees, decisions, AI strategies, portraits, flags, and localisation do not exist. black_plague_rat_run_runtime_pulse is mentioned in a comment at line 5 but is not defined or called anywhere. The only Event 20 scheduler callback is black_plague_run_scheduled_callback in common/scripted_effects/020_black_plague_effects.txt:1424-1453, which calls the disease pulse and never invokes rat runtime work.

This is incomplete rather than a small missing-key defect. The package cannot spawn a playable Rat Nation or Rat King until the country and unit surfaces below are registered and the parent adds the evolution dispatch.

## Country package coverage checklist

| Surface | Status | Evidence and required owner action |
| --- | --- | --- |
| Finite tags | Missing | RTA through RTM and RTX are referenced at common/scripted_effects/020_black_plague_rat_effects.txt:117-209 and :685-709, but no tag definition exists in common/country_tags, mod country files, or history. Register a collision-audited finite pool and a separate Rat King tag before runtime use. |
| Country definitions | Missing | No common/countries/* file defines the rat tags. Add graphical culture, colours, and package identity for all dormant tags. |
| Country history | Missing | No history/countries/* file defines rat history, politics, laws, or zero-slot setup. Dynamic transfer still needs a valid country history row. |
| State setup | Incomplete | black_plague_rat_create_from_state transfers the selected state at common/scripted_effects/020_black_plague_rat_effects.txt:365-417, but no registered destination exists, no basin selection is connected, and no Royal Basin/scenario grace setup exists. Preserve owner/controller, capital, cores, plague phase, and state flags when wiring this. |
| Localised country identity | Missing | No RTA-RTM/RTX country names, adjectives, parties, leader names, unit names, focus names, decision names, or mechanic strings exist in localisation/english. |
| Flags and emblems | Missing | No rat normal/medium/small flag set or Rat King/world-end variant exists under gfx/flags; RAT_UNIFIED in common/countries/cosmetic.txt:228-231 is only an unrelated cosmetic definition. |
| Leader and portrait package | Placeholder | Base countries use "The Brood Voice" with GFX_portrait_europe_generic_land_13 at common/scripted_effects/020_black_plague_rat_effects.txt:329-334. The King uses "The Rat King" and the same generic portrait at :672-677. Replace these with collective archetype portraits for broods and a generated sentient individual portrait with matching name and gender metadata for RTX. |
| Party and politics | Placeholder | black_plague_rat_initialize_country and black_plague_rat_initialize_king_country force neutrality and 100 neutrality popularity at :324-325 and :669-670; no party-name localisation, route politics, elections, or Rat King government selection exists. |
| Advisors and characters | Missing | No rat advisors, high command, commanders, characters, or portrait paths exist. Base brood leaders should remain institutional identities; only the sentient King may use a personal fictional name pool. |
| Shared classifiers | Present | common/scripted_triggers/chaosx_dynamic_triggers.txt:16-74 already classifies black_plague_rat_country and black_plague_rat_king_country as special and actual nonhuman countries. No classifier patch is needed. |
| Cleanup and reuse | Broken | black_plague_rat_cleanup_retired_country at common/scripted_effects/020_black_plague_rat_effects.txt:599-616 removes the country from the array but never clears the matching black_plague_rat_slot_<tag>_in_use flag. A retired slot therefore remains permanently unavailable. |

## File surface checklist

The following files or identifiers are referenced by the draft but absent from the repository:

- RTA through RTM in common/country_tags/chaosx_countries.txt, corresponding common/countries/* definitions, history/countries/* rows, localisation, and flags.
- RTX as the separate Rat King country in common/country_tags/chaosx_countries.txt, country definition, history, localisation, and flags.
- rat_swarm and rat_tunnelers in common/units. The only nearby zero-manpower precedent is the Event 018 cave brood file common/units/018_resources_found_cave_broods.txt, whose sub-units are active = no and are not Rat Nation units.
- black_plague_rat_brood_instinct, black_plague_rat_no_civilian_economy, and black_plague_rat_king_dominion in common/ideas. common/ideas/020_black_death_ideas.txt defines only black_death.
- black_plague_rat_focus_tree and black_plague_rat_king_focus_tree in common/national_focus.
- rat_swarm template-priority and role-ratio strategy identifiers in common/ai_strategy or common/ai_strategy_plans.
- Rat-specific decisions and missions under the shared disease category in common/decisions.
- Rat country and Rat King event-log type, stage title, stage body, and event-detail mappings in common/scripted_localisation/chaosx_scripted_localisation_events_log.txt and localisation/english. Existing Event 20 localisation only labels infestation and the five status names in localisation/english/020_black_plague_response_l_english.yml:9 and localisation/english/biowarfare_disease_containment_l_english.yml:45-50.
- Rat flags, leader portraits, four archetype portraits, King portrait animation/static fallback, focus icons, idea icons, decision icons, and asset manifests under gfx and docs.

The draft has no normal technology file or valid technology identifier for rat countries. The installed HOI4 MCP package exposes no Technology Tree Viewer, so technology-tree inspection remains an unresolved limitation. Use a narrow focus-driven or explicitly documented captured-knowledge route rather than giving rat countries ordinary human research by accident.

## Effects and runtime findings

### Callback and evolution dispatch

- black_plague_rat_initialize_runtime exists only at common/scripted_effects/020_black_plague_rat_effects.txt:14-43; no caller was found.
- black_plague_rat_run_runtime_pulse is only a comment at common/scripted_effects/020_black_plague_rat_effects.txt:4-7; there is no definition or caller.
- black_plague_run_weekly_pulse rebuilds disease state at common/scripted_effects/020_black_plague_effects.txt:1356-1422 but never initializes or pulses the rat arrays.
- black_plague_rat_schedule_next_evolution_check at common/scripted_effects/020_black_plague_rat_effects.txt:53-78 schedules only Evolutions I-IV. It has no Evolution V MTTH branch even though V minimum/maximum constants exist at common/script_constants/020_black_plague_rat_constants.txt:43-44.
- No black_plague_rat_activate_evolution_i, black_plague_rat_activate_evolution_ii, or black_plague_rat_activate_evolution_v effect exists. Only III (:471-495) and IV (:711-718) are present.
- black_plague_rat_activate_evolution_iii sets both black_plague_evolution_iii_active and black_plague_evolution_iii_recorded before or without a log call. black_plague_rat_activate_evolution_iv does the same. Parent dispatch must call a shared record path exactly once per evolution.

### Event log defect

black_plague_rat_record_current_evolution at common/scripted_effects/020_black_plague_rat_effects.txt:105-110 calls record_events_log_evolution_entry only when events_log_evolution_has_actor = 1. This drops no-actor Evolution I rows, while the specification requires a row for every evolution with actor context only when available. Record the row with the default actor value or implement a documented deferred row policy, following the existing no-actor patterns in common/scripted_effects/001_communism_spread_effects.txt:2577-2586 and the shared event-log contract.

### Evolution gate gaps

The triggers in common/scripted_triggers/020_black_plague_rat_triggers.txt do not implement the acceptance conditions in Parts 4 and 7:

- black_plague_rat_evolution_i_is_eligible at :93-115 checks only system start, Chaos 200, three established states, and a ready day. It does not require a meaningful death count, multi-state failure, or major containment failure.
- black_plague_rat_evolution_ii_is_eligible at :117-137 checks only Evolution I active, Chaos 400, and either one established dock state or six established states. It does not require Evolution I recorded/pre-fire permission, multiple countries or regions, or a failed real sea/port route.
- black_plague_rat_evolution_iii_is_eligible at :139-155 uses two unrelated global any_state checks. It does not prove one connected uncontrolled basin, large population loss, local weak containment, or an active emergence pressure for that same basin.
- black_plague_rat_evolution_iv_is_eligible at :157-172 checks Chaos 800, two countries, and any active brood. It does not score a candidate's Coherence, Dominion, Sentience, proto-sentience, absorbed-rival history, deaths, or non-collapse eligibility.
- black_plague_rat_evolution_v_is_eligible at :174-183 checks only Evolution IV active, global King active, and Chaos 1000. It lacks Evolution IV recorded, Rat King territory/death thresholds, absorbed-brood/deep-preparation gates, a valid continent target, and disputed-crown/terminal conflict checks.

### Rat Nation spawning and pulse

- black_plague_rat_select_free_slot at :117-210 hardcodes thirteen tags with no definitions and no repository-wide approved-mod conflict evidence. The local mod, vanilla country surfaces, and workshop country_tags files returned no RTA-RTM/RTX matches, but final registration still needs a complete collision review.
- black_plague_rat_select_spawn_state at :212-232 draws any valid state from the global active-state array. It does not group states into connected basins, enforce basin ownership, or keep all states in one emergence package.
- black_plague_rat_create_from_state at :365-417 transfers a state into a selected static tag and adds a core, but its destination country does not exist. It creates units with start_manpower_factor = 1.00 and start_equipment_factor = 1.00 at :392-398, directly violating the no-human-manpower/no-ordinary-equipment requirement unless replaced by genuinely zero-resource sub-units and a scripted brood ledger.
- black_plague_rat_create_division_template at :264-299 references undefined rat_swarm and rat_tunnelers sub-units. Both templates are locked, but no valid template can load until those unit definitions exist.
- black_plague_rat_process_country_pulse at :529-552 adds a flat pulse gain plus controlled-state gain, then raises one unit. It has no Hunger, Coherence, deaths, food access, focus, occupied-state infection bookkeeping, supply strain, terrain/air counterplay, or state performance degradation.
- The pulse cooldown at :513-526 uses rat_merger_cooldown_days (60) instead of the documented approximately 30-day rat_pulse_days constant at common/script_constants/020_black_plague_rat_constants.txt:85-87.
- black_plague_rat_try_absorb_adjacent_brood at :565-597 immediately transfers every valid adjacent state once a flat mass threshold is reached. It has no sustained adjacency timer, dominance score comparison, weaker-brood resistance, unit transfer, absorption history, or royal-candidate contribution.
- Cleanup at :599-616 deletes templates with disband = no, removes the array entry, and leaves slot flags and possible unit/target state behind. Verify the desired unit disposition and clear all per-tag arrays, event targets, cooldowns, and slot flags before reuse.

### Rat King transfer and identity

- black_plague_rat_select_king_source at :633-650 scores only controlled states times state_share_for_king plus Brood Mass. It does not use Coherence, Dominion, Sentience, proto-sentience, deaths, city/port control, or absorbed-rival history.
- black_plague_rat_initialize_king_country at :652-683 creates no Royal Basin, consolidation grace, route choice, royal spirit lifecycle, royal pulse doctrine, or Crown/Council/Hierophancy focus branches. It reuses the missing base templates and a generic vanilla portrait.
- black_plague_rat_transfer_to_king at :685-709 addresses undefined static tag RTX, then tries to set the capital with state = event_target:black_plague_rat_king_source.capital_scope at :690. The chained capital_scope token has no matching precedent in the repository; save the source capital state as a separate event target before calling set_capital.
- The same transfer marks states black_plague_rat_king_royal_node, retires base countries, and transfers states at :693-705, but it does not transfer units, Brood Mass, Hunger, Coherence, dominance history, focus completion, ideas, slot state, or event-target cleanup. It therefore cannot satisfy full Rat Nation-to-King transfer.

## Politics, leader, portrait, flag, advisor, and party issues

The base leader name "The Brood Voice" is an institutional name and is suitable only as a placeholder until four archetype-specific collective identities are localized. It must not remain paired with a generic human portrait. The Rat King must be an individual sentient fictional sovereign with generated portrait, personal name pool, epithet, and matching gender metadata. No rat leader or advisor character currently exists.

The base and King initializers both set neutrality and 100 neutrality popularity without party names or route state. The King route constants exist at common/script_constants/020_black_plague_rat_constants.txt:126-136, but no route selection effect, mutually exclusive government ideas, route lock, or route localisation exists.

## Focus, decision, idea, and asset issues

The focus-tree loaders at common/scripted_effects/020_black_plague_rat_effects.txt:336 and :679 point to nonexistent IDs. The specification requires a shared 40-50-role Rat Nation tree with four archetype modules and a deep 70-100-role Rat King tree with coronation, government, administration, military, plague, knowledge, population policy, continent, and world-end lanes. No focus file, icon, localisation, AI focus plan, or route validation exists.

The human response category is intentionally gated by black_plague_country_can_direct_response at common/scripted_triggers/020_black_plague_response_triggers.txt:10-24, which requires black_plague_country_is_human_host. Shared anti-rat state actions exist at common/scripted_triggers/020_black_plague_shared_response_triggers.txt:319-332, but they are human-response actions and do not provide Rat Nation territory, brood pulse, merger, route, or King decisions. Add rat actions inside the shared disease category rather than creating a duplicate rat-crisis category unless the parent spec is revised.

The idea identifiers added at common/scripted_effects/020_black_plague_rat_effects.txt:335 and :678 are absent. common/ideas/020_black_death_ideas.txt contains only the human disease idea black_death and cannot satisfy the three-deep Rat Nation or three-deep Rat King spirit lifecycle.

No rat flag, portrait, focus icon, idea icon, decision icon, animated King portrait, static fallback, or manifest exists. Asset work must follow chaos-redux-event-assets and, for animated portraits, chaos-redux-frame-animation; no transform-only still-image loop is acceptable.

## Starting military, technology, industry, supply, and production issues

The only unit templates are "Rat Brood" and "Rat Shock Brood" at common/scripted_effects/020_black_plague_rat_effects.txt:264-293. They reference absent sub-units, have no four-archetype unit mix, and are not connected to a real common/units package. Starting and pulse creation both use ordinary manpower/equipment factors at :393-398 and :518-523.

The country initializers set zero research slots at :323 and :668, but no narrow focus-driven progression or captured-knowledge path is implemented. No production lines, equipment stockpiles, conventional economy, supply/burrow nodes, clean-territory strain, air counterplay, or terrain-specific unit package exists. Do not silently enable human production or recruitment to make the missing templates work.

## AI and playability issues

The only AI references are undefined rat_swarm template-priority and role-ratio IDs at common/scripted_effects/020_black_plague_rat_effects.txt:337-340 and :680-681. There is no archetype-aware AI strategy, no focus plan, no port or city preference, no merger standoff behavior, no Royal Basin grace pause, no Rat King consolidation/continental/world-end phases, and no safeguards against normal diplomacy.

The nonhuman classifier is present, but it is not enough to make a country playable. The AI still needs survival, corridor maintenance, pulse timing, dominance comparison, candidate selection, continent selection, and terminal-focus validity checks. Human control also needs a visible pulse/territory mechanic while manual recruit and deploy remain impossible.

## Constants, MTTH, and parse/runtime hazards

- common/script_constants/020_black_plague_rat_constants.txt:10-14 declares the black_plague_rat_evolution group as integer data, which is appropriate for gates but not for the decimal starting_stability = 0.35 and starting_war_support = 1.00 at :73-74 in the integer black_plague_rat_pool group. Vanilla script-constant documentation requires data = fixed_point for floating-point entries. Split the fixed-point values into a fixed-point group or change the schema with care.
- common/scripted_effects/020_black_plague_rat_effects.txt:525 and :585 pass constant:black_plague_rat_pool.rat_merger_cooldown_days to timed set_country_flag effects. chaos-redux-events/SKILL.md:489-501 documents that timed flag days fields reject constant: and variable tokens; use a mirrored file-scoped @ literal or a supported meta-effect pattern.
- load_focus_tree, add_ideas, add_ai_strategy, division_template, and static tag selectors all reference absent identifiers. These are load/runtime failures once the effects become reachable, not harmless placeholders.
- set_capital with state = event_target:black_plague_rat_spawn_state at :379 has local precedents, but the chained event_target:black_plague_rat_king_source.capital_scope at :690 does not. Save a capital state target explicitly before the King transfer.
- black_plague_rat_initialize_runtime clears evolution flags and arrays only on first generation at :14-38; it does not clear slot-in-use flags. Save/reload and scenario-repeat behavior needs explicit generation-safe slot recovery.

## Map, state, infection, and terminal setup issues

The state trigger black_plague_rat_state_can_spawn at common/scripted_triggers/020_black_plague_rat_triggers.txt:63-69 correctly rejects nonhuman owner/controller and already Rat-Controlled states, but no connected-basin selection or terminal eligible-land set exists. Rat occupation calls black_plague_set_current_state_phase with rat_controlled at common/scripted_effects/020_black_plague_rat_effects.txt:382-385, yet there is no rat-to-rat infection ledger, occupied-state infection follow-up, or cleanup/resurgence implementation.

Evolution V and the terminal route are absent. black_plague_rat_evolution_v_is_eligible has no conquest, deaths, preparation, valid continent, or recorded-stage gate. No target-continent state set, 90-percent eligible-land plus strategic-capital rule, final focus completion check, terminal transfer sequence, defeat cleanup, restoration restriction, or aftermath localisation exists. Do not mark Evolution V active as world end; it must unlock the route and leave the terminal gate to live post-focus checks.

## Acceptance mapping

- Evolutions I-V are not all implemented. Only partial III/IV stubs exist, baseline disease states remain separate, and Event 20 has no rat event-log localisation mapping.
- Finite collision-free tags are not registered. The local/vanilla/workshop country-tag scans found no collisions for RTA-RTM/RTX, but registration, history, cleanup, and reuse are missing.
- Full Rat Nation identity, four archetypes, AI, units, decisions, and assets are missing.
- No-human-manpower/no-ordinary-equipment is violated by the two create_unit payloads and unsupported unit identifiers.
- Brood growth is capped numerically, but lacks the required dynamic sources, limits, Hunger/Coherence, supply, terrain, air, food, and anti-rat counterplay.
- Rat Nation immunity, occupied-state infection, sustained dominance/absorption, unit transfer, and grace-period behavior are missing.
- Rat King is not a separate registered country, has a generic placeholder leader, and lacks Royal Basin, grace, routes, spirits, royal pulse doctrines, deep tree, AI, and full transfer.
- Evolution V and terminal criteria are missing, including continent control, strategic capitals/refuges, final focus, staged terminal conquest, defeat, and aftermath.

## Recommended implementation order and ownership handoff

1. Parent evolution work should add the Event 20 callback invocation, evolution I/II/V activation, stage logging, and V route-unlock semantics in the separate evolution-effects file. Do not duplicate those calls in this country package until the parent chooses one source of truth.
2. Register and collision-audit RTA-RTM and RTX, then add country definitions, history, flags, localisation, and dormant-state cleanup before any static tag selector is reachable.
3. Add dedicated zero-manpower/zero-equipment rat sub-units and locked templates for the four archetypes and King families. Keep all formation creation scripted and pulse-paid.
4. Add ideas, shared and King focus trees, shared-category rat decisions, archetype/route AI plans, and all localisation/icon/portrait manifests.
5. Repair basin selection, infection persistence, growth/meter dynamics, sustained dominance, slot cleanup, Royal Basin grace, and full transfer. Replace timed-flag constants and chained capital scope before parse validation.
6. Add Evolution V target-continent preparation, focus and decision checks, terminal sequence, defeat/restoration/aftermath, event-log detail, super-event hooks, and mapmode/UI progress.
7. Validate with a dry-run scenario covering the minimum basin, catastrophic basin, two adjacent broods, Rat King transfer, Royal Basin grace, King defeat, near-success Evolution V interruption, and terminal 90-percent plus strategic-capital gate. A full game launch was not attempted because the destination tags and unit identifiers are absent.

## Validation performed

- Read the required repository instructions, Event 20 specs Parts 4-7 and matrices, offline Paradox wiki pages, and vanilla HOI4 documentation for effects, triggers, script constants, localisation, focus, decisions, country, unit, and technology syntax.
- Used exact repository searches to verify that black_plague_rat_run_runtime_pulse, rat activation I/II/V effects, RTA-RTM/RTX tag definitions, rat focus trees, rat units, rat ideas, rat AI strategy IDs, rat decisions, and rat localisation are absent.
- Checked RTA-RTM/RTX against the mod and vanilla country surfaces and against workshop country_tags files; no collisions were returned. This is not a substitute for final approved-mod conflict review after registration.
- Compared the rat draft with the existing human response gates, shared classifier, Event 018 zero-manpower unit precedent, and Event 20 scheduler callback. No game parse or live scenario validation was run because the package is not loadable as a complete country system.

## Remaining blockers and uncertainty

The package is not complete and must not be reported as implemented. The parent evolution-dispatch work and the missing country/package surfaces are separate ownership areas. The chained King capital scope is a likely runtime hazard but was not game-parsed here. The absent Technology Tree Viewer leaves technology-tree inspection unresolved; the file-level audit found no rat technology package to inspect.
