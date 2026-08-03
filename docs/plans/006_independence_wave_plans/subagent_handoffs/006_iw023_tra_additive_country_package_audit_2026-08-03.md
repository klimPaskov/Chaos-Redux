# IW-023 Transylvania additive country-package audit

Date: 2026-08-03

Status: HOLD for parent review; this is a static package audit and does not claim runtime completion.

## Scope and evidence

This audit covers Event 006 candidate IW-023 (Transylvania) using the existing vanilla `TRA` tag as an additive package carrier.

The audit preserves vanilla TRA history, characters, flags, cosmetic names, Yugoslav release logic, and Austro-Hungarian focus compatibility as externally referenced content rather than treating TRA as a new country.

The audit read the repository package registry, research resolution, map bindings, reservation group, force mapping, focus and decision contracts, current IW-023 scaffold, offline Paradox wiki pages, required vanilla documentation, vanilla TRA files, vanilla TRA focus consumers, and the installed country-tag collision scan.

No gameplay file or vanilla file was edited by this subagent.

## Country-package coverage checklist

- PASS — Identity and tag policy: IW-023 resolves to registered vanilla `TRA`, with `reuse_registered_tag` and `automatic_pool_ready_if_not_living` in `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` and `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`.
- PASS — Country registration: vanilla `00_countries.txt:208` maps `TRA` to `countries/Transylvania.txt`; `AWX` is not a valid replacement and is not present in the Event 006 registry arrays.
- PASS — Vanilla country identity: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/countries/Transylvania.txt` contains only the eastern-European graphical cultures and vanilla color, so the additive package does not need to replace the country definition.
- PASS — Vanilla history preservation: `history/countries/TRA - Transylvania.txt` retains capital state `84`, three research slots, vanilla technologies, democratic politics, Iuliu Maniu, popularity, and all twenty recruited vanilla characters; it has no vanilla OOB or starting production that should be copied or overwritten.
- PARTIAL — Map and release setup: current package bindings select compact states `84|76` with anchor `84` and protect host `ROM` state `46`; static ownership and controller evidence is present, but an Event 006 release has not been run and transfer, capital, cores, supply, and host-survival behavior remain unverified at runtime.
- PARTIAL — Politics and leadership: vanilla `Iuliu Maniu` is a sourced period leader and the setup trigger checks him with `has_country_leader = { ruling_only = yes name = "Iuliu Maniu" }`; the package adds route-party names and council decisions but does not provide a separate sourced council or institutional leader roster.
- PASS — Portrait and flag coverage: vanilla TRA portraits and `TRA.tga`, `TRA_communism.tga`, `TRA_fascism.tga`, `TRA_neutrality.tga`, and Szekely Land variants exist in the game install; the mod has no `gfx/flags/TRA*` override, so base assets remain available, subject to origin-specific cosmetic-tag checks.
- PARTIAL — Advisors and characters: all vanilla TRA characters remain gated by `original_tag = TRA`, but the package has no new sourced historical character or portrait evidence and must not invent one for a crisis route.
- BLOCKED — Focus contract: the additive carrier predicate now recognizes TRA and `austro_hungarian_releasable_focus`, but the copied carrier file adds eight Event 006 shared focuses unconditionally to every Austro-Hungarian releasable tag and has no TRA-specific focus group or branch gate; this does not yet prove the Level 2 country-specific focus requirement or a reviewed TRA carrier contract.
- PASS — Ideas surface: `common/ideas/006_independence_wave_transylvania_ideas.txt` defines seven TRA-scoped ideas and the matching English localisation exists, but the package cannot be admitted until origin/readiness and formable registration pass.
- PASS — Decision surface: category `independence_wave_tra_danube_council_category` and twelve TRA decision/mission identifiers are defined in `common/decisions/categories/006_independence_wave_transylvania_categories.txt` and `common/decisions/006_independence_wave_transylvania_decisions.txt`, with matching localisation and AI strategy references; no runtime execution is claimed.
- PARTIAL — Forces and technology: the force mapping specifies `mountain_frontier`, mountain infantry and defecting regulars, with engineers, reconnaissance, and artillery first, while vanilla TRA technologies remain in history; there is no vanilla OOB, and the dynamic grant/reinforcement path has only static trigger evidence.
- PARTIAL — Industry and supply: the additive setup uses startup effects rather than changing vanilla history, but no runtime evidence confirms equipment, manpower, trains, fuel, reinforcement, supply, or regional infrastructure after release.
- BLOCKED — Formable/ambition surface: the Danubian Confederation family profile exists in the generic formable registry, but no IW-023 effect selects family id `8`, sets the selected-family variable, or calls `independence_wave_focus_register_formable_family`; the setup trigger also currently requires `NOT = { has_country_flag = independence_wave_formable_family_registered }`, so registration order must be designed explicitly.
- BLOCKED — Origin/readiness admission: the planner still calls legacy `is_independence_wave_candidate_tag_available`, which requires the absent `independence_wave_package_content_ready` flag; the exact TRA wrapper exists but is not used by the planner.
- PARTIAL — AI and playability: `common/ai_strategy/006_independence_wave_transylvania.txt` contains four TRA-scoped strategies for frontier survival, host restraint, settled frontier, and emergency commission, but strategy activation, focus selection, force production, diplomacy, and survival remain untested in-game.
- PASS — Localisation coverage: the current package localisation covers route parties, seven ideas, the category, all twelve decisions, and effect tooltips; vanilla country names, adjectives, party names, leaders, and cosmetic names remain supplied by the game files.
- PARTIAL — Cleanup: the cleanup effect removes the first hold-border object with `remove_mission` and the remaining eleven with `remove_decision`; the first object is mission-shaped (`activation` and `days_mission_timeout`) and should be reviewed against the engine contract rather than changed blindly.

## File-surface checklist

- Registry and resolution: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row `IW-023`; `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` row `IW-023`.
- Map contract: `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` row `IW-023`; `docs/plans/006_independence_wave_plans/006_current_map_reservation_groups.csv` row `RG-DANUBE-BORDERLAND`.
- Force contract: `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` row `IW-023`, profile `mountain_frontier`.
- Static registry code: `common/collections/chaosx_country_collections.txt`, `common/script_constants/006_independence_wave_country_registry_constants.txt`, and `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt` all treat TRA as a registered reuse tag.
- Planner and loader: `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` contains `can_plan_independence_wave_package_iw_023`; `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt` contains the IW-023 loader, weight, reservation, anchor, and compact-territory effects.
- Dispatch: `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` calls the TRA setup, finalisation, and cleanup effects; `common/scripted_effects/006_independence_wave_scenario_effects.txt` includes IW-023 in scenario ranking.
- TRA package helpers: `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt` and `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt` contain the exact tag, setup, runtime, route, AI, force, and cleanup contracts.
- Focus carrier: `common/scripted_triggers/006_independence_wave_focus_triggers.txt` recognizes `independence_wave_iw_023_lifecycle_initialized` plus `has_focus_tree = austro_hungarian_releasable_focus`; `common/scripted_effects/006_independence_wave_focus_effects.txt` attaches the generic additive overlay.
- Carrier source: `common/national_focus/austro_hungarian_releasable_shared.txt` preserves the 56 vanilla focus nodes and adds eight `shared_focus` entries named `independence_wave_overlay_take_stock_of_independence`, `independence_wave_overlay_secure_state_services`, `independence_wave_overlay_integrate_release_forces`, `independence_wave_overlay_open_foreign_desk`, `independence_wave_overlay_address_former_host`, `independence_wave_overlay_join_network`, `independence_wave_overlay_open_regional_ambition`, and `independence_wave_overlay_mature_independence`.
- Shared overlay source: `common/national_focus/006_independence_wave_focus.txt` contains the eight generic overlay focuses but no `TRA`-specific focus IDs or country-specific focus group.
- Ideas, decisions, AI, and localisation: `common/ideas/006_independence_wave_transylvania_ideas.txt`, `common/decisions/categories/006_independence_wave_transylvania_categories.txt`, `common/decisions/006_independence_wave_transylvania_decisions.txt`, `common/ai_strategy/006_independence_wave_transylvania.txt`, and `localisation/english/006_independence_wave_transylvania_l_english.yml`.
- Roster checkpoint: `events/006_independence_wave.txt:203` defines `chaosx.nr6.350`, but it has no TRA branch.
- Vanilla identity surfaces: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt`, `common/countries/Transylvania.txt`, `history/countries/TRA - Transylvania.txt`, `common/characters/TRA.txt`, `common/national_focus/generic.txt`, and `common/national_focus/austro_hungarian_releasable_shared.txt`.

## Map, state, and host setup

- Compact territory is state `84` Transylvania plus state `76` Northern Transylvania, with state `84` as the fixed anchor and capital candidate.
- Both compact states are currently Romanian-owned and Romanian-controlled and carry vanilla TRA cores; state `84` has steel and coal, while state `76` has the larger manpower pool and multiple victory points.
- Optional extension states are `82` Banat, `83` Crisana, and `764` West Banat; they must remain claims, diplomacy, plebiscite, or integration surfaces until an explicit extension path wins them.
- Host protection is recorded as `ROM` state `46`; the package must not transfer or core the protected host state and must leave the host capital untouched.
- Reservation group `RG-DANUBE-BORDERLAND` covers states `45|76|82|84|764|802` and members `IW-023|IW-024|IW-025|IW-031|IW-032`; the group permits at most one package from the group per coarse state and marks IW-032 disabled.
- Vanilla `YUG_autonomous_transylvania` in `common/national_focus/yugoslavia.txt:1467-1480` can also release TRA, core states `82|83|84|76`, and optionally use state `764`; Event 006 must use its own origin marker and must not treat a Yugoslav release as an IW-023 release.
- No event-specific map rewrite was audited or applied; railway, supply hub, port, building, resource, and controller transfer behavior require parent-owned dry-run/review/apply/post-validation if map edits become necessary.

## Politics, leaders, portraits, flags, advisors, and parties

- Vanilla TRA begins democratic with `Iuliu Maniu` as the ruling leader, popularity `democratic=33`, `neutrality=33`, and `communism=34`; the history file must remain additive-only.
- The twenty vanilla TRA characters in `common/characters/TRA.txt` are all `original_tag = TRA` scoped and use existing Eastern European portrait assets; no new fictional or opposite-gender name/portrait pairing was introduced by the scaffold.
- Vanilla English localisation provides `TRA`, `TRA_DEF`, `TRA_ADJ`, the three ideology party names, and cosmetic names including `TRA_YUG_subject` and `TRA_AUS_danubian_state`; the mod localisation adds only package-specific route and mechanic keys.
- The package route names cover constitutional federal, traditional, labor, military, and patron/compact directions, but party activation and election behavior are not runtime-proven.
- Vanilla flag variants must remain available for vanilla release routes; an Event 006 flag override must be added only if a reviewed origin-specific identity requires it and must include a source/ownership record.

## Focus, decision, idea, and asset issues

- The current additive carrier preserves the vanilla Austro-Hungarian focus tree structure and adds the eight shared overlay focuses listed above, but because the shared file is loaded for all Austro-Hungarian releasable tags, the TRA contract needs an explicit country gate or a documented reviewed carrier contract.
- No TRA-specific focus group exists in `common/national_focus/006_independence_wave_focus.txt`, so the Level 2 requirement for one country-specific focus group is not met by the current scaffold.
- Read-only focus inspection returned tree `austro_hungarian_releasable_focus`, 56 focuses, layout hash `8e1c44e617e03adc234cb622e850552e6b313e775be0cd3452761fa1f52f98bf`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b4cd62194fdb2ac1a7ff2787f1b38a0e15ea818cdc49090f82375b23b74bd3b/b61eb9a3c745ba184ceca5044972a7ac42795a9b815f78e0d0483b2562a1405c/focus-inspect.fea863022e703a78.json`.
- Focus inspection reported 114 blocking diagnostics because the mod-only resolver could not find many vanilla generic icon references; this is not proof that vanilla game assets fail in-game, but it means the inspection is not clean and the omitted resolver diagnostics must be reviewed before a completion claim.
- Read-only focus rendering returned the same layout hash, dimensions `4176x1048`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9e959ee0bf2b6a3578c3ae1c704b92648646fe4dfb00332ce09684648db67c8/4f6de80aabb8c73ec8f72f6b046c49a81f7eb477add151b29c9bd694c813eb1f/austro_hungarian_releasable_focus.focus.json`, and 70 blocking diagnostics of the same missing-vanilla-icon class.
- The focus diagnostic artifacts are useful evidence of the carrier layout, but they do not replace a source-linked review against vanilla assets or a TRA-specific route proof.
- Seven ideas are defined as `tra_divided_border_authority`, `tra_danube_settlement`, `tra_federal_council_charter`, `tra_workers_and_rail_council`, `tra_border_communes_compact`, `tra_frontier_security_commission`, and `tra_patron_trade_compact`; their English names/descriptions exist and use existing generic Event 006 idea icons.
- The decision category is `independence_wave_tra_danube_council_category` and the twelve package actions are `independence_wave_tra_hold_border_council_together`, `independence_wave_tra_secure_carpathian_depots`, `independence_wave_tra_screen_defecting_regulars`, `independence_wave_tra_convene_multiethnic_assembly`, `independence_wave_tra_settle_former_host_ledgers`, `independence_wave_tra_ratify_federal_charter`, `independence_wave_tra_convene_workers_and_rail_council`, `independence_wave_tra_restore_border_communes`, `independence_wave_tra_establish_frontier_commission`, `independence_wave_tra_accept_patron_compact`, `independence_wave_tra_codify_danube_settlement`, and `independence_wave_tra_open_danube_network`.
- The first action is mission-shaped and is removed with `remove_mission`; the other eleven are removed with `remove_decision`; confirm this mixed cleanup against the decision engine before release.

## Registry, readiness, and collision findings

- The exact package trigger `is_independence_wave_exact_package_iw_023_tag_available` exists in `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt` and checks Event 006 origin, `original_tag = TRA`, capital state `84`, anchor availability, and a non-TRA owner.
- The planner currently calls `TRA = { is_independence_wave_candidate_tag_available = yes }` in `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt`; that legacy predicate requires `has_country_flag = independence_wave_package_content_ready`, and no source grants that flag for IW-023.
- Replace the planner gate with the exact IW-023 wrapper or provide a separately attested readiness path after all required surfaces are proven; do not add the forbidden readiness shortcut merely to make the planner select TRA.
- `has_prepared_independence_wave_iw_023_package` requires `NOT = { has_country_flag = independence_wave_formable_family_registered }` while the package currently never registers a formable; if registration is added before the final prepared check, the trigger order must be changed deliberately.
- The Danubian Confederation profile is family id `8` in `common/script_constants/006_independence_wave_formable_constants.txt:25` and the registry row is at `:378`; the missing adapter must select the family, load its profile, and call `independence_wave_focus_register_formable_family` at the intended lifecycle point.
- Static `python .tools/audit_chaosx_country_tags.py --surface-scan` reported `Protected Event 006/Soviet tags: 136; external country-definition collisions: 0; external identity-surface collisions: 0; random-event roots skipped: 1`.
- The static audit is an owned-identifier and collision result, not proof that the package is complete; vanilla TRA has many external consumers and must not be redefined.

## Starting military, technology, industry, supply, and production

- Vanilla TRA history supplies three research slots and early infantry, support, mountaineer, fighter, tank, destroyer, cruiser, and submarine technologies according to DLC branches, but no OOB, division template, production line, stockpile, or convoy setup.
- Event 006 force mapping row IW-023 selects profile `mountain_frontier`, mountain infantry and defecting regulars, with engineers, reconnaissance, and artillery prioritized, and explicitly disallows navy and air inheritance.
- The package effect statically wires force-package loading, dynamic starting forces, and five reinforcement flags; the parent must verify actual manpower, equipment, template, reinforcement, fuel, trains, and supply after a real release.
- No history-file factory or equipment grant was added by this audit; Event 006 startup grants must remain in scripted effects so vanilla TRA history and other release routes stay intact.

## AI and playability

- `common/ai_strategy/006_independence_wave_transylvania.txt` defines `independence_wave_tra_frontier_survival`, `independence_wave_tra_host_restraint`, `independence_wave_tra_settled_frontier`, and `independence_wave_tra_emergency_commission` with `original_tag = TRA` and package/setup flag gates.
- The strategies use valid vanilla production and construction priorities and avoid immediate expansion, but no in-game evidence confirms strategy activation, focus selection, border behavior, diplomatic restraint, or survival against the protected host.
- The package should not be marked ready while planner admission, formable registration, focus carrier scope, and dynamic force application remain unresolved, because the AI contract depends on those lifecycle flags.

## Required parent follow-ups

- Change the planner to call `is_independence_wave_exact_package_iw_023_tag_available` or implement a separately documented, fail-closed readiness attestation that does not grant the prohibited generic content-ready flag.
- Add and sequence the Danubian Confederation family selection/registration adapter for family id `8`, resolving the `NOT independence_wave_formable_family_registered` prepared-trigger ordering.
- Decide whether the eight shared overlay focuses are an accepted reviewed TRA carrier contract; otherwise gate the carrier file and add a TRA-specific focus group or route-specific focus contract without replacing the vanilla Austro-Hungarian tree.
- Add a TRA branch to `chaosx.nr6.350` if the roster checkpoint is required for IW-023; otherwise remove the no-op call and document that vanilla Maniu and characters are the complete roster.
- Review `remove_mission` versus `remove_decision` for `independence_wave_tra_hold_border_council_together` and confirm category cleanup on annexation, cancellation, and origin termination.
- Run parent-owned release dry-run, map review/apply/post-validation, event/decision/focus inspection after source-linked vanilla asset resolution, and a real playability check before declaring IW-023 ready.

## Simplifications, omissions, and blockers

- No gameplay patch was made by this subagent.
- No new country, leader, portrait, flag, focus tree, formable suite, map state, OOB, or large balance package was invented.
- IW-023 remains incomplete and must be held because planner admission, formable registration, focus-contract scope, and runtime setup evidence are missing.
- No runtime or in-game completion claim is made, and no fallback country or substitute tag was used.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw023_tra_additive_country_package_audit_2026-08-03.md`.
