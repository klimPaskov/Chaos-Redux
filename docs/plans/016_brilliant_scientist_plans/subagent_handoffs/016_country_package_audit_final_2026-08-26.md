# Event 016 D’Rhondan country-package final audit

Date: 2026-08-26.

Owner: `/root/event016_country_audit_final`.

Status: evidence-only read-only handoff. No gameplay source, asset, localisation, map, technology, event, or AI file was edited in this audit, and no Git commit was created. The static DHR package is substantially aligned with the accepted Event 016 addendum, but this report does not claim live acceptance, engine acceptance of the revolt transaction, or whole-event completion.

## Scope and references

The review covered the fixed DHR tag, country definition and history, dormant OOB, characters and leader traits, cosmetics, ideas, focus tree and focus helpers, country/contact decisions and categories, country/contact events, scripted effects and triggers, AI strategy and focus plans, shared Alien Infantry API, Event 019 provider 508, CXT hooks, technology/unit/equipment declarations, localisation, GFX registrations, portraits, flags, manifests, and the DHR country documentation.

The accepted Event 016 source set reviewed was `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_1_core.md`, `.../spec_part_2_host_directorate_and_decisions.md`, `.../spec_part_3_project_portfolio.md`, `.../spec_part_4_evolutions_and_event_chain.md`, `.../spec_part_5_kruger_state_country_package.md`, `.../spec_part_6_kruger_state_focus_tree.md`, `.../spec_part_7_world_reactions_and_ai.md`, `.../spec_part_8_super_events_world_end_and_aftermath.md`, `.../spec_part_9_assets_animation_and_localisation.md`, `.../spec_part_10_achievements_and_completion.md`, and `.../spec_016_alien_infantry_and_dhronda_addendum.md`, together with `acceptance/016_acceptance_criteria.md`, `016_balance_and_exploit_review.md`, `016_parent_depth_and_anti_bloat_review.md`, `package_manifest.md`, the country/focus/AI/decision/event/asset matrices, and `README.md`.

The country-system references were `docs/events/016_brilliant_scientist/systems/dhrondan_country.md` and `016_dhrondan_focus_tree.md`. Prior evidence reviewed included `016_dhrondan_country_audit_2026-08-25.md`, `016_dhrondan_country_focus_audit_current_2026-08-26.md`, `016_dhr_route_consumers_2026-08-26.md`, `016_alien_dhrondan_current_completion_audit_2026-08-26.md`, `016_alien_api_audit_current_2026-08-26.md`, `016_alien_dhrondan_country_scoped_registry_2026-08-26.md`, `016_alien_landing_state_registry_2026-08-26.md`, `016_final_focus_audit_2026-08-26.md`, `016_final_decision_audit_2026-08-26.md`, and `016_final_event_completion_audit_2026-08-26.md`.

`AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, and `.agents/skills/chaos-redux-comfyui/SKILL.md` were read. The required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, country creation, faction, state, character, national focuses, equipment, divisions, technology, map, and GFX were consulted. Vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, especially `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, `loc_formatter_documentation.md`, and `loc_objects_documentation.md`, plus vanilla country/history/focus/AI/technology precedents, was consulted.

The repository was inspected at current `HEAD 659895db2` and the requested history through `18f7c7d67` (`docs: attest directorate gui and localize dhrondan outcomes`). The latter commit is documentation/asset/localisation oriented for this audit; no DHR gameplay edit was made by this pass.

## Executive result

The DHR package has one fixed tag registration, one country definition, one dormant history/OOB, one 12-character roster, three route leaders, five civilian advisors, one high-command figure, three commanders, three route cosmetics, eleven lifecycle ideas, an exactly 88-focus tree, route-specific AI plans and force strategies, and the shared provider-508 Alien Infantry contract. Static source checks found no duplicate DHR tag, KRG tag, DHR country definition, DHR focus ID, public D’Rhondan template, or second `release = DHR` caller.

The accepted source behavior is present for fixed-tag formation, three regimes, state transfer, core/claim handling, host-military conservation, landing-only alien cohorts, focus loading, decision consumers, CXT registration, and Event 019 provider 508. Dynamic state/controller/capital/enclave behavior, API materialisation with the inactive sub-unit boundary, current technology projection, current event projection, route-AI probabilities, and user live acceptance remain unproved.

One additional classification ambiguity is recorded rather than patched: `common/scripted_triggers/chaosx_dynamic_triggers.txt:16-48` does not list DHR in `is_special_chaos_country`, and `:51-69` does not list DHR in `is_actual_nonhuman_country`. The accepted DHR addendum describes an alien country but does not explicitly prescribe either shared classifier. This requires an owner/spec decision because adding a classifier entry would change shared systems; it is not silently inferred here.

## Country-package coverage checklist

| Surface | Evidence | Result |
| --- | --- | --- |
| Fixed tag and country path | `common/country_tags/016_dhrondan_country.txt:8` maps `DHR` to `countries/Empire of D'Rhonda DHR.txt`; the target file exists. | Resolved statically. |
| Dormant setup | `history/countries/DHR - Empire of D'Rhonda.txt:8-30` uses bootstrap `capital = 1`, empty `oob = "016_dhrondan_dormant"`, neutral 100 popularity, and all twelve stable character IDs; `history/units/016_dhrondan_dormant.txt:8` has an empty `units = {}` block. | Source-aligned; bootstrap-capital and no-OOB behavior remain engine-unverified. |
| Fixed-tag initialization and rejoin | `dhrondan_start_revolt`, `dhrondan_release_and_transfer_landing_states`, `dhrondan_initialize_country_runtime`, global transaction/formation/force receipts, and existing-DHR branches are in `common/scripted_effects/016_dhrondan_country_effects.txt:18-505`. | Source-aligned; runtime/idempotence matrix unproved. |
| Three regimes | `DHR_IMPERIAL`, `DHR_SYNOD`, and `DHR_COVENANT` are installed by route helpers at `common/scripted_effects/016_dhrondan_country_effects.txt:212-266`; the three focus roots are mutually exclusive. | Resolved statically. |
| Leaders/advisors/commanders | `common/characters/016_dhrondan_characters.txt:26-223` defines three leaders, five `political_advisor` characters, one `high_command` character, and three `corps_commander` characters; all twelve are recruited by history. | Resolved statically. |
| Portraits and gender/name pairing | `interface/016_dhrondan_portraits.gfx` resolves the twelve full portraits and role-card textures under `gfx/leaders/DHR/` and `gfx/interface/ideas/016_dhrondan/`; the portrait handoff records fictional native-ImageGen lineage and processing. Names are fixed alien names and no opposite-gender random pool or female metadata mismatch was found. | Resolved for the accepted fixed roster; random-name-pool interpretation remains a design question. |
| Flags and cosmetics | Base and `DHR_IMPERIAL`, `DHR_SYNOD`, `DHR_COVENANT` flags have normal/medium/small DDS ladders and are registered by the DHR GFX files. | Resolved statically; live presentation unproved. |
| Territory, cores, claims, capital | `dhrondan_transfer_current_landing_state` adds DHR and host cores, uses `transfer_state_to = DHR` for host-controlled states, `set_state_owner_to = DHR` for occupied host-owned states, and claims marked states not owned by DHR at `common/scripted_effects/016_dhrondan_country_effects.txt:84-128`. | Source-aligned; map/state transaction evidence remains blocked. |
| Disconnected enclaves | `dhrondan_prepare_initial_enclave_components`, `dhrondan_flood_fill_initial_enclave_component`, and `dhrondan_deploy_next_initial_enclave_cohort` flood-fill DHR-owned, DHR-controlled, passable marked components outside the home area and add one paid cohort per uncovered component. | Source-aligned; native adjacency/controller execution unproved. |
| Revolt conservation | `dhrondan_conserve_revolt_military_assets` deletes surviving `D’Rhondan Landing Cohort` divisions with `disband = no` and sends all host `alien_laser_weapon_equipment_1` to DHR. | Source-aligned; materialisation/deletion/stockpile conservation unproved in live runtime. |
| Alien template restriction | `alien_infantry` is `active = no` with zero manpower; the shared API creates the locked ten-battalion `D’Rhondan Landing Cohort` with `force_allow_recruiting = no`; DHR sets `dhrondan_alien_infantry_training_forbidden`. | Source-aligned; the inactive-subunit/API construction boundary is engine-unverified. |
| Focus wiring | `dhrondan_focus_tree` loads through `load_focus_tree = { tree = dhrondan_focus_tree keep_completed = yes }` at `common/scripted_effects/016_dhrondan_country_effects.txt:276-278`; 88 focus IDs, route roots, shortcuts, effects, triggers, icons, and localisation resolve statically. | Resolved by prior successful MCP/source evidence. |
| Decisions/events | Country and contact decisions/categories, events `.40-.52`, state legality rechecks, compact delivery cleanup, and route-marker consumers are present. | Source-aligned; current event projection is partial/unavailable. |
| CXT hooks | `common/on_actions/016_alien_infantry_cxt_on_actions.txt:8-27` uses one bounded `random_country` startup registration and tag-scoped `on_daily_CXT` repair/synchronisation, matching `docs/testing/chaosx_test_country.md`. | Resolved statically; live CXT setup unproved. |
| Duplicate Kruger/DHR/formation | `rg` found one `KRG` tag registration, one `DHR` tag registration, one DHR country file, one DHR `release` caller, one focus tree, and one API-owned landing template. | No duplicate found statically. |
| Shared classification | DHR is absent from both shared classifier OR blocks; KRG uses `brilliant_scientist_is_kruger_sovereign_country` as intended. | Open interpretation/blocker; requires design owner decision, not a source-only patch. |

## File-surface checklist

The audited country surface is complete at the file level across `common/country_tags/016_dhrondan_country.txt`, `common/countries/Empire of D'Rhonda DHR.txt`, `common/countries/016_dhrondan_cosmetics.txt`, `history/countries/DHR - Empire of D'Rhonda.txt`, `history/units/016_dhrondan_dormant.txt`, `common/characters/016_dhrondan_characters.txt`, `common/country_leader/016_dhrondan_traits.txt`, `common/ideas/016_dhrondan_focus_ideas.txt`, `common/national_focus/016_dhrondan_focus_tree.txt`, `common/scripted_effects/016_dhrondan_country_effects.txt`, `common/scripted_effects/016_dhrondan_focus_effects.txt`, `common/scripted_triggers/016_dhrondan_country_triggers.txt`, `common/scripted_triggers/016_dhrondan_focus_triggers.txt`, `common/decisions/016_dhrondan_country_decisions.txt`, `common/decisions/016_dhrondan_contact_decisions.txt`, both DHR decision category files, both DHR event files, `common/ai_strategy/016_dhrondan_country_strategies.txt`, `common/ai_strategy_plans/016_dhrondan_focus_ai.txt`, DHR constants and scripted localisation, DHR English localisation, DHR focus/portrait/asset GFX, and all referenced `gfx/flags`, `gfx/leaders/DHR`, focus-icon, idea-icon, advisor-card, decision-icon, report, and news textures.

The shared dependencies are `common/scripted_effects/016_alien_infantry_api_effects.txt`, `common/scripted_triggers/016_alien_infantry_api_triggers.txt`, `common/units/016_brilliant_scientist_project_forces.txt`, `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`, `common/technologies/016_brilliant_scientist_project_technologies.txt`, `common/technologies/016_brilliant_scientist_project_force_technologies.txt`, `common/on_actions/016_alien_infantry_cxt_on_actions.txt`, `common/script_constants/016_alien_infantry_api_constants.txt`, and Event 019 provider files `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`, `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt`, and `common/script_constants/016_brilliant_scientist_project_force_constants.txt`.

## Territory, revolt transfer, and conservation findings

`dhrondan_capture_revolt_inputs` reads the caller country’s `alien_infantry_landing_state_registry`, captures a first controlled/passable marked state and then a host-owned/passable fallback, counts marked states, and derives the ordinary opening cohort count from `max(5, min(15, marked_states + floor(arrivals / 2)))` through the two-arrivals-per-cohort loop in `common/script_constants/016_dhrondan_country_constants.txt:43-53` and `common/scripted_effects/016_dhrondan_country_effects.txt:18-80`.

The transfer pass adds DHR cores without removing host cores, changes owner and controller together for host-controlled states, changes only owner for a host-owned state held by a third-party occupier, and adds a DHR claim to marked states not owned by DHR. The first viable marked state is assigned as capital on a new release. This matches `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md:42-44` and `docs/events/016_brilliant_scientist/systems/dhrondan_country.md:19-35`.

The source now uses the caller-country landing registry, with owner-target scope correction in the shared API, so one provider cannot raise another provider’s DHR count or claims. The transfer semantics and disconnected component flood-fill are not certified by a fresh runtime state matrix. The available country inspection route does not exist, and the current map calls did not complete. The first formation’s use of bootstrap history `capital = 1` is an accepted dormant contract, but engine tolerance and replacement of that capital are also runtime-unverified.

The state-transfer source contains a scope-risk worth preserving for owner review: `dhrondan_capture_revolt_inputs` stores temporary counters before entering nested DHR/state scopes. The existing country documentation says the caller-owned values are captured before ownership changes, but only engine execution can prove those temporary values survive every nested callback as intended. No code change was made.

## Politics, leaders, portraits, flags, parties, ideas, and localisation

The provisional route is neutral and installs Vael IX. Imperial continuity remains neutral/non-aligned with `DHR_IMPERIAL`; the Synod installs Sera Qel with neutrality-mapped technocratic government and `DHR_SYNOD`; the Covenant installs Ilyr Ren with democratic politics, elections enabled, and `DHR_COVENANT`. The route helpers clear conflicting route flags and apply one route identity.

The roster consists of `DHR_emperor_vael_ix`, `DHR_first_calculant_sera_qel`, `DHR_speaker_ilyr_ren`, `DHR_archivist_thaal_ven`, `DHR_logistics_oracle_nym_vor`, `DHR_harmonic_envoy_rae_syl`, `DHR_war_calculant_orr_kesh`, `DHR_genetic_steward_vel_ara`, `DHR_shadow_listener_thel_ior`, `DHR_field_vector_kaal_dren`, `DHR_enclave_guardian_syr_vek`, and `DHR_orbital_liaison_omn_tal`. Advisor `idea_token`, slot, route `allowed`, commander skills/traits, and leader role wiring are present.

The portrait handoff records fictional native-ImageGen provenance, processed 156x210 full portraits, role cards, DDS hashes, GFX registration, and runtime paths. Fixed alien names avoid opposite-gender random-pool pairing. The generic top-level guidance asks for actual-ish gender-matched random pools for fictional one-person leaders, while this accepted DHR roster uses fixed approved names and omits `gender`; changing that would be a design change, not a safe audit patch. Institutional roles are not drawing random names.

The country, adjectives, parties, leaders, advisors, commanders, traits, ideas, focuses, decisions, missions, event/detail strings, cosmetic names, and tooltips were statically found in the DHR localisation files. All four flag ladders, 88 focus icon pairs, eleven lifecycle idea icons, portrait role cards, and DHR event/decision assets resolve to installed files. No runtime reference points into the durable archive.

## Focus, decisions, ideas, and route-specific consumers

`common/national_focus/016_dhrondan_focus_tree.txt` contains exactly 88 unique focuses: eight survival, 24 political, ten laboratory, twelve army/predictive, eight orbital/air/naval, eight diplomacy/intelligence, twelve expansion/world order, and six crisis/late-game focuses. The roots `DHR_vael_ix_takes_the_throne`, `DHR_sera_qel_presents_the_calculus`, and `DHR_ilyr_ren_opens_the_chamber` require `DHR_convene_the_two_world_throne` and mutually exclude one another. Ten shortcuts target existing focus IDs.

The three lifecycle families in `common/ideas/016_dhrondan_focus_ideas.txt` clear before setting the next stage, so focus-created political, predictive, and off-world spirits do not stack beyond three. Focus effects do not directly create divisions, grant Alien Laser Weapons, change cores, transfer states, or train alien infantry.

The five route-support markers are consumed by existing surfaces after the route-consumer tranche: `dhrondan_alien_components_standardized` and `dhrondan_orbital_office_reassembled` feed paid-landing AI, `dhrondan_laboratory_route_complete` feeds enclave-supply gates/weights, `dhrondan_predictive_warfare_perfected` feeds reclamation gates/weights, and `dhrondan_access_map_exchange_ready` gates Covenant compact offers. Opening survival markers similarly feed landing or enclave-support AI. No duplicate decisions were added.

One low-severity design risk remains at `common/scripted_effects/016_dhrondan_focus_effects.txt:242-255`, called by `DHR_salvage_the_shuttle_docks` at `common/national_focus/016_dhrondan_focus_tree.txt:841-850`: it selects a random owned controlled coastal state with a free dockyard slot, so a fully landlocked DHR can complete the focus without receiving a dockyard. No accepted inland substitute exists, so no patch was made.

## Military, technology, industry, supply, and production

The dormant OOB is empty by design. DHR receives no normal army, production line, or alien training before formation. On revolt, host landing-template divisions are deleted without refund and the host’s Alien Laser Weapons are transferred to DHR. The shared API then grants the ordinary paid reserve, allocates one cohort per disconnected component where required, and concentrates remaining capped cohorts at the capital.

The `alien_infantry` declaration at `common/units/016_brilliant_scientist_project_forces.txt:303-334` is inactive, zero-human-manpower, two-width, 40-strength, 90-organisation, 0.75 default morale/recovery, 10 reconnaissance, 5 suppression, 0.04 supply, and 200 Alien Laser Weapons per battalion. The API-owned ten-battalion template is locked and non-recruitable, requiring exactly 2,000 weapons per cohort. DHR’s `dhrondan_focus_cannot_train_alien_infantry` gate and `dhrondan_alien_infantry_training_forbidden` flag prevent normal training.

`brilliant_scientist_alien_infantry_tech` enables the laser equipment and `brilliant_scientist_alien_predictive_warfare_tech` depends on it and enables predictive tactics through the hidden project technology files. DHR receives bounded host technology inheritance and research-slot setup; no DHR duplicate equipment family, sub-unit, or provider was found. The API’s deliberate absence of `enable_subunits` preserves the landing-only boundary, but the live engine must prove that template construction succeeds while the sub-unit is inactive.

Focus rewards add bounded factories, infrastructure, research, experience, air/naval support, and production access. They do not create free alien formations. Dynamic stockpile, supply, reinforcement, and actual cohort materialisation remain outside static acceptance.

## AI and playability

`common/ai_strategy/016_dhrondan_country_strategies.txt` provides three route-gated force strategies: Imperial infantry/armor, Synod predictive infantry/armor, and Covenant infantry/mountain/marine preferences. `common/ai_strategy_plans/016_dhrondan_focus_ai.txt` provides an opening plan and mutually exclusive Imperial, Synod, and Covenant plans gated by `original_tag = DHR` and route flags, with focus queues, weights, and abort conditions.

The source plans are internally connected to the 88 focus IDs and decision surfaces. Some cross-lane support focuses remain outside individual route queues while inline focus weights keep them reachable; this is a route-priority quality gap, not a dead route. No AI weight was changed.

The required `chaosx_ai_probability_auditor` capability is not exposed in the callable tool set. A direct `hoi4.probability_inspect` request for the DHR focus/route AI source was accepted after source-shape correction in the prior audit but timed out at the MCP service after 180 seconds; no same-scenario `hoi4.probability_compare` exists. The prior rebellion arithmetic artifact is not evidence for route-AI selection. Therefore no quantitative AI, landing, decision, mission, or rebellion acceptance claim is made.

## Alien Infantry API, CXT, and Event 019 provider 508

The shared public APIs are `alien_infantry_grant_contact`, `alien_infantry_revoke_contact`, `alien_infantry_can_call_landing`, `alien_infantry_spawn_landing_cohort`, and `alien_infantry_reconcile_country`. Receipt IDs remain separate for Kruger pact, Mengele expedition, Event 019 provider 508, DHR sovereignty, and future callers. DHR uses the sovereignty receipt and the shared template rather than a duplicate unit/equipment implementation.

The reservation contract remains exactly 2,000 Alien Laser Weapons for seven days, one pending landing, a 30-day base cooldown, and DHR recovery tiers of 24, 18, and 12 days. Failed/invalid reservations refund the proven debit; successful ordinary landings record state history, Alien Presence, Pact Strain, arrival count, and cooldown after materialisation. Sovereignty bootstrap mode skips ordinary pact-host telemetry and cooldown while preserving the exact per-cohort debit.

Event 019 retains provider/family ID 508. `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:668-720` builds/uses the API-owned locked template and delegates materialisation, commit, rollback, deletion ID, and refund to the shared API. Its sustainment callback is explicitly zero-row, and cleanup revokes only provider-508 receipt 3. No second template or ordinary-manpower/equipment callback was found.

## Exact HOI4 MCP evidence and limitations

The installed callable set exposes `hoi4_focus_inspect`, `hoi4_focus_render`, `hoi4_event_inspect`, `hoi4_event_render`, `hoi4_map_inspect`, `hoi4_map_render`, `hoi4_tech_inspect`, `hoi4_tech_render`, and probability tools, but no dedicated country/state-transfer inspector and no callable `chaosx_ai_probability_auditor` worker route.

Prior successful focus evidence is retained from `016_final_focus_audit_2026-08-26.md`: `FOCUS_INSPECTED`, status `ok`, 88 focuses, 102 connectors, no crossing/node-intersection/long-connector diagnostics, bounds x=2..40 and y=0..22, layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7f094589a3899fd52e6b1d05e13777d76d9783faa3751b3887d7cfcf6d228ee/9c81fe28bc00eb91a4c4039c31272b633591ce197dbe936eb31832b8acf64570/focus-inspect.abe2c73eb5b5af0a.json`.

The matching prior focus render completed with `FOCUS_RENDERED`, 6992x2788, and the same layout hash. Useful artifacts are HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4cd067b810b70afd1e61b36eb95f401182898ce7c96ec72969bdb2fd782b475/d8110b9621d74d9306684aef2e6c7c17bfd42a1f813c4cab5968d0ab99d054fc/dhrondan_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289/2512d737d80473f718e621de3ca8f39173afc86ccfb4cb3ccf19f48197e63223/dhrondan_focus_tree.focus.svg`, and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6213aa6ec9163c99ecaf94059b6385d1c7ea233f350724f58a09ebd4f3dca29/eeddeab9c47478dfc378a4a24471c263cfe162016ba0e58222962514ac5d6b8c/dhrondan_focus_tree.focus.json`.

Prior Event `.47` evidence is partial but useful: `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` state-flow/lint artifacts report zero blocking diagnostics while the adapter scanned vanilla `game:` sources and did not ingest the mod DHR event files. Retained artifacts are state flow `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94eaa4862016956958bae29a2fba697a0e3f1efd857ff96c4fbb3381c76ccb38/cf509287edc5293ffdfebfa2f78ddcd1972b2ee23764f5d60435b01fa7a2b23b/event-state_flow-f588a2607444.json`, lint `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/678bfabc6eb84fdbff224e0d7fae1f62e48aee85d4d7780a78e2c8043c716038/5afba29c4a86076360b6e191bb05a6ed5a52ef004fef10ceccdc53cd956ad19b/event-lint-f588a2607444.json`, and render manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd81c30903ef30ef048a6478c0c9c6795e0e6371e82631f253c3e17581525cda/ca626de89826dfcdd32e35b58609f9f2491151a02727e318add020b45e91049e/event-state-f588a2607444-manifest.json`.

The prior targeted map artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f2154f813f3d5da9ee50018c48f0c2b3bd5a174db50a400d1ca27f94fd182a7/dd579f7183317c4cc091189d040fe844385a4701ca7bbb3091c6bddc2ca93773/map-inspect.1bbbbf9bcba2fc25.json` covers static states 1, 12, and 77 and geometry/network checks. The map workspace also retains unrelated `map/buildings.txt` position and floating-harbor diagnostics. It does not prove a dynamic DHR revolt, marked-state registry, controller retention, capital selection, or enclave flood-fill.

In this final audit, bounded calls to `hoi4_focus_inspect`, `hoi4_focus_render`, `hoi4_event_inspect`, `hoi4_event_render`, `hoi4_map_inspect`, `hoi4_map_render`, `hoi4_tech_inspect`, `hoi4_tech_render`, and `hoi4_probability_inspect` were issued concurrently with a 12-second local bound. All nine returned the local status `bounded_wrapper_timeout` with `milliseconds = 12000` and no MCP payload. This was not treated as a tool success. Prior unbounded service attempts recorded in the current handoffs timed out awaiting `tools/call` after 180 seconds for valid focus, map, probability, event, and technology requests.

The available `hoi4_tech_inspect` lint route previously timed out after 180 seconds for `alien_laser_weapon_equipment_1` and `alien_infantry`; no dedicated Technology Tree Viewer is installed. Technology source review therefore cannot be promoted to engine technology-tree acceptance. No dedicated unit/equipment inspector completed.

The mandatory probability owner pass is likewise blocked: the named `chaosx_ai_probability_auditor` route is absent, the direct DHR route-AI probability call timed out after 180 seconds, and no same-scenario compare exists. The prior completed rebellion arithmetic artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba3f44770f08d71e20b0b4a7b7abf983f797e0bbf5dad4931e953ab67fb1db94/b57ddac0f6d7cbe18b9c527093acd93a10f84146ec886f88ef28da658f17ffa9/probability-inspect-fcd942b6523a.json` is retained only as prior branch evidence, not route-AI acceptance.

## Exact remaining blockers and risks

1. Dynamic DHR formation evidence is missing for owner/controller/core preservation, first viable capital, lost-state claims, disconnected enclave flood-fill, existing-DHR rejoin, post-annexation reinitialisation, host-template deletion, and laser-stockpile conservation. The source is aligned, but the dedicated country route is unavailable and current map calls timed out.

2. The inactive `alien_infantry`/`enable_subunits` boundary is unverified by the engine. The CXT fixture explicitly unlocks the test token, while normal DHR/API setup deliberately does not; a successful API template/materialisation scenario is required before this can be closed.

3. Current Event `.47` and Event 019 provider 508 projection is partial or timed out because the adapter did not ingest the mod event files and corrected state-flow requests later timed out at 180 seconds. Source review is not equivalent to event acceptance.

4. DHR route AI, landing AI, decision weights, compact/event weights, and rebellion cadence lack the mandatory named auditor and same-scenario `hoi4.probability_compare` pass. No balance claim is made.

5. The installed package has no Technology Tree Viewer, and `hoi4_tech_inspect` lint timed out. Hidden technology dependency, equipment unlock, predictive tactic, and asset projection remain unresolved engine evidence.

6. Shared classification is ambiguous: DHR is not in `is_special_chaos_country` or `is_actual_nonhuman_country`. The accepted DHR addendum does not state whether the alien country must enter either classifier. Parent/spec owner must decide before any classifier patch.

7. The accepted fictional DHR portrait handoff uses fixed approved alien names and no runtime gender metadata, while generic guidance describes gender-matched random pools for one-person fictional leaders. This is a roster/design interpretation issue, not a safe audit fix.

8. `DHR_salvage_the_shuttle_docks` can complete without a dockyard for fully landlocked DHR. The accepted plan does not define a valid inland substitute, so this remains a low-severity design risk.

9. Alien Infantry V13 locator/effect binding, strict audio-role coverage, positional playback, and parent/user live acceptance remain open in the shared model package. The separate Portal Raider runtime model/entity/action/audio package and active-beachhead lifecycle are also outside this country source audit and block whole-event completion.

10. No live Hearts of Iron IV launch or new-save acceptance was performed or claimed, as required by the task boundary.

## Validation and change record

Meaningful static checks completed were one DHR tag registration, one KRG tag registration, one DHR country file, one DHR release caller, twelve recruited character IDs, three route leaders, five political advisors, one high-command character, three commanders, exactly 88 unique focus IDs, 88 focus icon pairs, eleven lifecycle idea icons, ten shortcut targets, route-marker consumer wiring, shared API/provider-508 references, and installed portrait/flag/GFX texture paths. The prior successful focus MCP topology/render evidence and prior partial Event/map artifacts are listed above.

No gameplay or asset file was changed. The only intended file written by this pass is this handoff: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_country_package_audit_final_2026-08-26.md`.

No simplification or fallback was introduced. This handoff intentionally preserves source-aligned findings as source evidence only, records every unavailable/partial MCP route, and does not claim live acceptance, engine acceptance, or Event 016 completion.

## Parent action requested

Treat the static DHR country package as reviewable but not accepted. When the inspection service is responsive, run a two-provider landing-registry and DHR revolt matrix covering controller change, ownership loss, third-party occupation, duplicate-state registration, disconnected components, existing-DHR rejoin, annexation reinitialisation, host-template deletion, equipment conservation, and capital selection. Run the mandatory named probability auditor and identical-scenario compare for opening, Imperial, Synod, Covenant, wartime, peaceful, route-complete, landing, decision, and rebellion scenarios. Resolve the shared DHR classification and fixed-name interpretation with the design owner before changing source.
