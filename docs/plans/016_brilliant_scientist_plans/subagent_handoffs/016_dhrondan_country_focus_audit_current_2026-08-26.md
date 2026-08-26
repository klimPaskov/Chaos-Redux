# Event 016 current D’Rhondan country and focus-package audit

> Status correction: the earlier five-marker finding in this handoff is superseded by the 2026-08-26 route-consumer and survival-marker repairs. Current source consumers are listed below; the remaining gap is weighted/runtime evidence, not an unconsumed flag.

> Later shared MCP receipt correction: `016_current_mcp_audit_2026-08-26.md` records successful current DHR focus inspection/rendering and partial Alien Infantry technology inspection/rendering after the timeout-only attempts described in this handoff. The timeout records remain accurate for this audit's calls, while full comparison and live acceptance remain open.

Date: 2026-08-26.

Owner: `/root/dhr_country_focus_audit_current`.

Status: audit complete, documentation-only. No gameplay source was patched and no Git commit was created. The current package is structurally aligned with the accepted D’Rhondan addendum, but dynamic state-transfer proof and the named route-AI probability pass remain blocked by the installed validation surface.

## Scope and required references

The audited country and focus surfaces are `common\country_tags\016_dhrondan_country.txt`, `common\countries\Empire of D'Rhonda DHR.txt`, `history\countries\DHR - Empire of D'Rhonda.txt`, `history\units\016_dhrondan_dormant.txt`, `common\national_focus\016_dhrondan_focus_tree.txt`, `common\characters\016_dhrondan_characters.txt`, `common\country_leader\016_dhrondan_traits.txt`, `common\ideas\016_dhrondan_focus_ideas.txt`, `common\ai_strategy\016_dhrondan_country_strategies.txt`, `common\ai_strategy_plans\016_dhrondan_focus_ai.txt`, the DHR scripted effects and triggers, DHR decisions and events, DHR localisation, DHR GFX registrations, and DHR flags and portraits.

The accepted design was checked against `docs\specs\016_brilliant_scientist_specs\specs\016_alien_infantry_and_dhronda_addendum.md`, `docs\events\016_brilliant_scientist\systems\016_dhrondan_focus_tree.md`, `docs\events\016_brilliant_scientist\systems\dhrondan_country.md`, `docs\specs\016_brilliant_scientist_specs\matrices\016_focus_tree_architecture.md`, `docs\specs\016_brilliant_scientist_specs\matrices\016_country_package_matrix.md`, `docs\specs\016_brilliant_scientist_specs\matrices\016_route_coverage.md`, and `docs\plans\016_brilliant_scientist_plans\016_source_of_truth_map.md`.

`AGENTS.md`, `.agents\skills\chaos-redux-subagents\SKILL.md`, `.agents\skills\chaos-redux-events\SKILL.md`, and `.agents\skills\chaos-redux-focus-trees\SKILL.md` were read before the audit. The offline Paradox wiki core pages, national-focus, country-creation, AI, event, idea, decision, effect, trigger, localisation, scope, map, division, equipment, and technology pages were consulted. Vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\` was consulted for effects, triggers, script concepts, constants, dynamic values, and localisation, and vanilla `common\national_focus\germany.txt`, AI strategy plans, AI strategy documentation, and AI template documentation were used as syntax precedents.

## Country package coverage checklist

| Surface | Result | Evidence and exact identifiers |
| --- | --- | --- |
| Fixed tag registration | Resolved | `DHR = "countries/Empire of D'Rhonda DHR.txt"` at `common\country_tags\016_dhrondan_country.txt:8`; the country definition exists and no duplicate `DHR` registration was found. |
| Dormant setup | Resolved statically | `history\countries\DHR - Empire of D'Rhonda.txt:8-14` uses `capital = 1`, `oob = "016_dhrondan_dormant"`, zero research slots, zero stability, zero war support, neutrality, and 100 neutrality popularity. `history\units\016_dhrondan_dormant.txt:8` contains an empty `units = {}` block. |
| Idempotent release and rejoin | Source-aligned, runtime unproven | `dhrondan_start_revolt`, `dhrondan_release_and_transfer_landing_states`, `dhrondan_initialize_country_runtime`, global transaction/formation/force flags, and existing-DHR branches are present in `common\scripted_effects\016_dhrondan_country_effects.txt:1-505`. A fresh cross-provider engine scenario was not available. |
| Territory, cores, enclaves, and capital | Source-aligned, runtime unproven | `dhrondan_transfer_current_landing_state` preserves the host core, transfers host-owned states, uses `set_state_owner_to = DHR` for occupied host-owned states, and claims third-party-owned marked states at `common\scripted_effects\016_dhrondan_country_effects.txt:81-123`. The first viable marked passable state becomes the first-release capital. |
| Focus loading | Resolved by prior MCP evidence | `load_focus_tree = { tree = dhrondan_focus_tree keep_completed = yes }` at `common\scripted_effects\016_dhrondan_country_effects.txt:276-278`; prior successful `hoi4.focus_inspect` resolved the tree. |
| Politics and regime identity | Resolved statically | Provisional Vael, Imperial Vael, Synod Sera, and Covenant Ilyr installation effects exist at `common\scripted_effects\016_dhrondan_country_effects.txt:212-302`, with mutually exclusive route flags and cosmetic tags. |
| Advisors and commanders | Resolved statically | `common\characters\016_dhrondan_characters.txt` has three route leaders, five `political_advisor` characters, one `high_command` character, and three `corps_commander` characters. This satisfies the accepted “six advisors/high-command plus three commanders” roster. |
| Flags and portraits | Resolved | Four DHR flag families exist in base, medium, and small forms. The portrait handoff records twelve full fictional native-ImageGen portraits and nine role cards, and `interface\016_dhrondan_portraits.gfx` resolves all 21 portrait sprites and texture paths. |

## Focus-tree and file-surface checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Exact tree size | Resolved | `common\national_focus\016_dhrondan_focus_tree.txt` contains exactly 88 focus blocks. Section counts are survival 8, Imperial 8, Synod 8, Covenant 8, laboratory 10, army/predictive 12, orbital/air/naval 8, diplomacy/intelligence 8, expansion/world order 12, and crisis/late game 6. Politics therefore totals 24. |
| Duplicate and missing focus IDs | Resolved statically | All 88 `DHR_*` focus IDs are unique. The four strategy plans reference 63 unique focus IDs and all 63 resolve to the focus tree. |
| Route exclusions and navigation | Resolved | The three roots at `common\national_focus\016_dhrondan_focus_tree.txt:185-193`, `298-306`, and `411-419` each require `DHR_convene_the_two_world_throne` and mutually exclude the other two roots. Ten shortcuts at lines 41-50 target existing focus IDs. |
| Prerequisite topology | Resolved by prior MCP evidence and source review | Multiple prerequisite blocks are used for intended AND capstones, while one block with several focus entries is used for intended OR convergence at `DHR_define_the_two_worlds_question` and `DHR_begin_postwar_integration`. The prior valid MCP inspect returned 102 connectors with no crossings, node intersections, or long connectors. |
| Search filters and icons | Resolved | Fourteen distinct search-filter tokens are used, all observed in vanilla. All 88 focus icons have matching base and `_shine` sprite names in `interface\016_dhrondan_focus_icons.gfx`; 99 unique referenced texture paths, including lifecycle ideas, resolve to files. |
| Focus localisation | Resolved | All 88 title keys and all 88 `_desc` keys exist in `localisation\english\016_dhrondan_focus_l_english.yml`. The 11 lifecycle idea title/description pairs and seven custom focus-effect tooltips are also present. |
| Focus effect references | Resolved statically | The tree calls nine unique `dhrondan_focus_*` effects, and all nine are defined in `common\scripted_effects\016_dhrondan_focus_effects.txt`. A wider DHR scripted-call scan found no unresolved candidate effect or trigger names after excluding decision/category identifiers. |
| Lifecycle spirits | Resolved statically | Political, predictive, and off-world helpers clear their family before adding the next stage at `common\scripted_effects\016_dhrondan_focus_effects.txt:12-119`, enforcing the maximum three simultaneous focus-created spirits. |
| Paid landing boundary | Resolved in source | `DHR_feed_the_landing_reserve` calls `dhrondan_focus_prepare_landing_cohort`, which enables the landing network and stores the shared 2,000-laser cost without creating a unit or granting equipment. No direct `create_unit`, `add_equipment_to_stockpile`, alien training, claim, core, or transfer effect occurs in the focus tree. |

## Politics, leaders, portraits, flags, advisors, and parties

The static history starts DHR as a dormant neutral country with no elected government. The provisional runtime installs Emperor Vael IX and the neutral-mapped Imperial route retains neutrality, while the Synod installs First Calculant Sera Qel with `oligarchism` leader ideology and neutral ruling party, and the Covenant installs Speaker Ilyr Ren with `liberalism`, democratic ruling party, and elections enabled. The role helpers use character scope and omit the optional `character` field inside `add_country_leader_role`; vanilla effect documentation confirms that form is valid in CHARACTER scope.

The exact character IDs are `DHR_emperor_vael_ix`, `DHR_first_calculant_sera_qel`, `DHR_speaker_ilyr_ren`, `DHR_archivist_thaal_ven`, `DHR_logistics_oracle_nym_vor`, `DHR_harmonic_envoy_rae_syl`, `DHR_war_calculant_orr_kesh`, `DHR_genetic_steward_vel_ara`, `DHR_shadow_listener_thel_ior`, `DHR_field_vector_kaal_dren`, `DHR_enclave_guardian_syr_vek`, and `DHR_orbital_liaison_omn_tal`. Route availability is explicit for Rae Syl, Thel Ior, and Orr Kesh; the three commanders are stable corps-command characters. All portrait and role paths resolve, and no opposite-gender portrait/name pairing or female metadata mismatch was found.

The character source uses the parent-approved stable actual-ish fictional names from the portrait handoff. It does not implement a runtime random-name pool. Because the accepted DHR addendum locks these stable route identities and the portrait handoff marks all twelve identities parent-approved, I did not introduce randomization during this audit. If the top-level fictional-portrait requirement is interpreted as mandatory per-setup randomization despite the accepted stable roster, that is a design conflict requiring parent direction rather than a safe local patch.

## Focus, decision, idea, and asset findings

The focus tree has the accepted ten lanes, distinct family icon folders, ten shortcuts, inline AI weights on all 88 nodes, route-specific roots, and the crisis choice/convergence structure. `DHR_perfect_predictive_warfare` uses the accepted custom technology upgrade API for alien predictive warfare, while the rest of the army route uses human signal/cadre and experience/command rewards. The accepted plan explicitly allows landing cooldown tiers, laser-production support, cohesion, tactics, diplomacy, and AI route effects; those accepted effects were not removed or misreported as free alien training.

The existing world-order decision consumers were updated by the prior route-consumer tranche and are present in `common\scripted_triggers\016_dhrondan_country_triggers.txt:120-146` and `common\decisions\016_dhrondan_country_decisions.txt:15-152`. The four active world-order gates now distinguish the decisions-unlocked, claim-contract, and route-complete markers.

The current source consumes the five route-support markers through existing decision surfaces:

- `dhrondan_alien_components_standardized` affects paid landing AI through `dhrondan_focus_has_standardized_components`.
- `dhrondan_laboratory_route_complete` gates and weights enclave supply through `dhrondan_focus_has_laboratory_route`.
- `dhrondan_predictive_warfare_perfected` gates and weights reclamation through `dhrondan_focus_has_predictive_warfare`.
- `dhrondan_orbital_office_reassembled` affects paid landing AI through `dhrondan_focus_has_orbital_office`.
- `dhrondan_access_map_exchange_ready` gates Covenant compact offers through `dhrondan_focus_has_access_map_exchange`.

The four opening survival markers are also consumed by the landing or enclave-support AI. Do not remove these flags or create duplicate decisions merely to consume them.

One low-severity playability risk remains in `common\scripted_effects\016_dhrondan_focus_effects.txt:242-255`, called by `DHR_salvage_the_shuttle_docks` at `common\national_focus\016_dhrondan_focus_tree.txt:841-850`. The helper chooses a random owned, controlled coastal state with a free dockyard slot. A fully landlocked DHR can complete the focus and set `dhrondan_shuttle_docks_salvaged` without receiving a dockyard. No safe fallback is obvious because building a dockyard in an inland state is invalid and the accepted plan does not define a substitute reward, so this remains a design-bound risk rather than a patch.

## Starting military, technology, industry, supply, and production

The dormant OOB is intentionally empty. `dhrondan_conserve_revolt_military_assets` deletes the host’s `D’Rhondan Landing Cohort` without refund and sends the host’s laser stockpile to DHR. Initial cohort sizing uses the accepted marked-state plus arrival formula, a 15-cohort ordinary cap, disconnected-component extensions, and the shared alien-infantry API. Every materialized landing remains subject to the shared 2,000 Alien Laser Weapons debit. DHR sets the training-forbidden flag and does not expose ordinary alien recruitment or training.

The runtime inherits only the bounded terrestrial baseline from the pact host, adds research slots up to the accepted starting cap, and uses focus-owned factory/infrastructure/research/experience effects. No direct focus reward creates a division or free equipment. The custom alien predictive-warfare technology dependency is an accepted Event 016 technology API call, not normal alien training. Dynamic stockpile, supply, and cohort behavior remain user-owned runtime acceptance surfaces.

## AI and playability

`common\ai_strategy\016_dhrondan_country_strategies.txt` contains three route-gated force strategies. Imperial prefers infantry/armor ratios, Synod prefers infantry/armor with different proportions, and Covenant prefers infantry/mountaineer/marine ratios. `common\ai_strategy_plans\016_dhrondan_focus_ai.txt` contains one opening plan and distinct Imperial, Synod, and Covenant plans, all gated by `original_tag = DHR` and route flags. Vanilla AI strategy and strategy-plan precedents confirm the `role_ratio`, `abort_when_not_enabled`, `ai_national_focuses`, `focus_factors`, and `weight` forms used here.

The route plans omit some generic support priorities, especially cross-lane laboratory, orbital, diplomacy, and army focuses. The inline focus weights keep these nodes reachable, so this is a queued route-priority quality gap rather than a dead route. No AI weight was changed because the required named `chaosx_ai_probability_auditor` route is not exposed in this runtime and no same-scenario before/after comparison could be produced.

## HOI4 MCP evidence and blockers

The prior current MCP audit retained successful Event `.47` state-flow/lint/render artifacts, including `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94eaa4862016956958bae29a2fba697a0e3f1efd857ff96c4fbb3381c76ccb38/cf509287edc5293ffdfebfa2f78ddcd1972b2ee23764f5d60435b01fa7a2b23b/event-state_flow-f588a2607444.json`, the matching lint artifact under `.../678bfabc6eb84fdbff224e0d7fae1f62e48aee85d4d7780a78e2c8043c716038/5afba29c4a86076360b6e191bb05a6ed5a52ef004fef10ceccdc53cd956ad19b/event-lint-f588a2607444.json`, and the Event `.47` render manifest under `.../bd81c30903ef30ef048a6478c0c9e6795e0e6371e82631f253c3e17581525cda/ca626de89826dfcdd32e35b58609f9f2491151a02727e318add020b45e91049e/event-state-f588a2607444-manifest.json`.

The last successful fresh focus inspect returned `FOCUS_INSPECTED`, 88 focuses, 102 connectors, no crossings/intersections/long connectors, and no DHR-specific diagnostics. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7f094589a3899fd52e6b1d05e13777d76d9783faa3751b3887d7cfcf6d228ee/9c81fe28bc00eb91a4c4039c31272b633591ce197dbe936eb31832b8acf64570/focus-inspect.abe2c73eb5b5af0a.json`. The matching focus render completed at 6992 by 2788 pixels with no DHR-specific blockers; its HTML, SVG, JSON, source-map, and plan artifacts are recorded in `016_final_focus_audit_2026-08-26.md`.

In this audit, valid `hoi4.focus_inspect` requests with bounded spacing parameters timed out awaiting `tools/call` after 180 seconds. A corrected national-mode `hoi4.focus_render` request without the continuous-mode-only `columns` parameter also timed out after 180 seconds. A targeted `hoi4.map_inspect` request for state 1 timed out after 180 seconds. These are current MCP service blockers, not source diagnostics. No callable `hoi4.focus_lint` tool is exposed; focus-inspect diagnostics are the available focus lint substitute. The installed package has no dedicated Technology Tree Viewer, so the technology dependency remains an unresolved validation limitation as required by the parent task.

The mandatory route-AI probability request was sent through `hoi4.probability_inspect` with `adapter = national_focus_ai_will_do` and source path `common\national_focus\016_dhrondan_focus_tree.txt`. The source shape was accepted after path-object correction, but the call timed out awaiting `tools/call` after 180 seconds. The custom `chaosx_ai_probability_auditor` route is absent from the exposed tool set, so no named auditor or same-scenario `hoi4.probability_compare` evidence exists for DHR route weights. Prior branch-arithmetic probability evidence applies to the revolt random branch, not route-AI selection.

The prior targeted map artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1f2154f813f3d5da9ee50018c48f0c2b3bd5a174db50a400d1ca27f94fd182a7/dd579f7183317c4cc091189d040fe844385a4701ca7bbb3091c6bddc2ca93773/map-inspect.1bbbbf9bcba2fc25.json` covers states 1, 12, and 77 and reports static state/geometry/network checks, while the map workspace retains unrelated `map\buildings.txt` position and floating-harbor diagnostics. No map rewrite was attempted.

## Required follow-up and remaining risks

1. Restore a callable `chaosx_ai_probability_auditor` route, then run named opening, wartime Imperial, stable-peace Synod, low-stability Covenant, and route-complete scenarios followed by an identical-scenario `hoi4.probability_compare` pass before tuning route priorities.

2. Run a bounded cross-provider landing-registry matrix covering provider A and provider B, controller change, ownership loss, DHR revolt for each provider, duplicate-state registration, existing-DHR rejoin, and legacy-save behavior. Source ownership is corrected, but this dynamic proof is not available from the current timed-out map/MCP route.

3. Retain the current marker consumers and rerun the named decision/focus probability scenarios when the MCP probability route is responsive. Do not add duplicate decisions for these already-consumed flags.

4. Decide whether stable approved DHR character names satisfy the top-level fictional-portrait random-name requirement. Any runtime randomization would need to preserve the accepted route identities and portrait wiring.

5. Decide whether landlocked DHR should receive a different accepted reward for `DHR_salvage_the_shuttle_docks`; no local fallback was applied.

The incomplete 3D Alien Infantry model/action package and unrelated Portal Raider package remain outside this country/focus surface, but they still block whole-event completion claims.

## Changed files and validation

Changed files: only this handoff, `docs\plans\016_brilliant_scientist_plans\subagent_handoffs\016_dhrondan_country_focus_audit_current_2026-08-26.md`. No country, focus, AI, decision, trigger, effect, idea, localisation, portrait, flag, or map source was changed. No tag, state ID, leader ID, party, focus-tree ID, localisation key, or formable ID was changed.

Meaningful checks completed in the current source: exact 88 focus blocks and section counts; 63 unique AI-plan focus references with zero missing; nine called focus effects with zero missing definitions; 88 focus icons with zero missing base or shine sprites; 99 unique focus/idea texture paths with zero missing files; 88/88 focus title and description keys; ten shortcut targets with zero missing; fourteen search-filter tokens all observed in vanilla; one DHR tag registration; twelve recruited character IDs with zero missing definitions; five political advisors, one high-command character, three commanders, and three route leaders; 21 portrait sprite texture references and 23 DHR asset texture references with zero missing files; and four base/medium/small DHR flag sets.

Skipped meaningful validation: live HOI4 launch and in-game acceptance, which remain user-owned; fresh focus inspect/render/map inspect reruns after MCP timeouts; high-fidelity focus raster because the earlier raster request timed out; the named probability auditor and same-scenario compare because the route is unavailable; the cross-provider registry runtime matrix because no working native map/runtime route exists; and the dedicated Technology Tree Viewer because it is not installed.

No simplification was introduced by this audit. The documented omissions are queued AI/runtime evidence, the landlocked dockyard edge case, the random-name-pool interpretation conflict, and external 3D package blockers.

Handoff path: `docs\plans\016_brilliant_scientist_plans\subagent_handoffs\016_dhrondan_country_focus_audit_current_2026-08-26.md`.
