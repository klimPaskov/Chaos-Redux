# IW-052 Buryatia package-core implementation handoff

Status: package-local implementation complete for review, with admission intentionally fail-closed.

Date: 2026-08-15.

Owner: country-package subagent.

## Guidance consulted

The repository AGENTS.md, chaos-redux-subagents, chaos-redux-events, chaos-redux-focus-trees, chaos-redux-decisions-missions, and chaos-redux-event-assets skills were read before implementation.

The required offline Paradox wiki core pages and the relevant vanilla documentation for script constants, events, decisions, ideas, AI strategy, focuses, localisation, scopes, triggers, effects, modifiers, and on actions were consulted.

Vanilla BYA tag, country, history, characters, localisation, flags, state 564, and Event 005 precedent files were inspected read-only.

## Scope and ownership boundary

This tranche implements only the BYA-owned Event 006 constants, triggers, effects, ideas, AI strategy, decisions, decision category, localisation, and five guarded callbacks in the shared Event 006 focus framework.

The central adapter, attestation, preflight, scenario, deterministic Join, Event 005, vanilla BYA files, map files, flags, portraits, and workbook were not changed.

The package remains unadmitted until the parent-owned identity and rights flag is supplied.

## Changed source files

- common/script_constants/006_independence_wave_buryatia_constants.txt
- common/scripted_triggers/006_independence_wave_buryatia_package_triggers.txt
- common/scripted_effects/006_independence_wave_buryatia_package_effects.txt
- common/ideas/006_independence_wave_buryatia_ideas.txt
- common/ai_strategy/006_independence_wave_buryatia.txt
- common/decisions/006_independence_wave_buryatia_decisions.txt
- common/decisions/categories/006_independence_wave_buryatia_categories.txt
- localisation/english/006_independence_wave_buryatia_l_english.yml
- common/national_focus/006_independence_wave_focus.txt

The localisation file is UTF-8 with BOM.

## Admission, identity, and origin gates

is_independence_wave_buryatia_package requires original_tag = BYA, an active Event 006 country, the exact package ID independence_wave_package_id.iw_052, and the parent-owned independence_wave_iw_052_identity_rights_cleared country flag.

The same package predicate rejects soviet_collapse_active_origin and liberation_origin.soviet_collapse.

has_independence_wave_bya_command_roster requires the parent-owned rights flag plus the two installed vanilla BYA character tokens BYA_seymon_ignatyev and BYA_bidia_dandaron.

No BYA_yakov_bykin token, Erbanov token, Event 005 institutional leader, generic portrait, or new character was introduced.

can_initialize_independence_wave_iw_052_package requires the exact region constant independence_wave_region.volga_urals_siberia_far_east, regional depth, mountain_or_frontier archetype, setup anchor/former-host event targets, state 564 ownership and control, state 564 capital, and the guarded vanilla roster.

independence_wave_bya_checkpoint_vanilla_roster is called only from the exact setup path and writes independence_wave_bya_roster_checkpoint only after the rights and two-character checks pass.

No package-local source sets or clears the parent-owned rights flag.

## Exact map and force binding

The runtime and prepared setup predicates bind BYA to state 564 and capital state 564.

The region-05 reservation remains the parent-owned RG-564 reservation for state 564 and was not edited.

The package consumes the existing p52 force mapping as independence_wave_force_profile.mounted_mobile with independence_wave_force_package_military_tradition.p52 equal to 68.

The package setup applies exactly the documented p52 reinforcement path: integrate_militias, regional_guards, secure_depots, terrain_units, and professional_officers.

Navy and air inheritance remain disabled by the prepared setup gate.

No ownership, controller, core, state, province, port, railway, supply, resource, or building data was written.

## Package mechanics

The package defines the Buryat frontier pressure, duration, cost, politics, seven package ideas, four guarded AI strategies, the frontier compact decision category, the timed founding mission, ten package projects, route installation, lifecycle refresh, former-host settlement, network settlement, failure penalties, and cleanup.

The five shared focus callbacks are:

- independence_wave_bya_focus_convene_frontier_council
- independence_wave_bya_focus_secure_baikal_communities
- independence_wave_bya_focus_integrate_frontier_guards
- independence_wave_bya_focus_settle_former_host_ledgers
- independence_wave_bya_focus_open_baikal_mongolia_corridor

Each callback is defined in the BYA effects file before its shared-focus call site and is gated by is_independence_wave_buryatia_package.

The shared focus additions are limited to the five BYA if callbacks at the founding-administration, state-inventory, first-oath, former-host-policy, and fellow-new-states focus rewards.

The package emits no set_cosmetic_tag, drop_cosmetic_tag, set_portraits, or portrait override effect.

Cleanup restores the installed vanilla BYA political baseline with democratic 50, communism 0, neutrality 50, and fascism 0 popularity.

## Vanilla and Event 005 separation

The source review confirmed vanilla BYA = countries/Buryatia.txt, vanilla history capital state 564, and vanilla opening character IDs BYA_seymon_ignatyev and BYA_bidia_dandaron.

The package does not edit C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/BYA.txt, history/countries/BYA - Buryatia.txt, vanilla flags, or vanilla portraits.

Event 005's Baikal Relay Council institution and GFX_portrait_BYA_baikal_relay_council remain untouched and are not used as Event 006 identity evidence.

The separate Erbanov portrait and source-placeholder work remains parent-owned and unresolved.

## Mandatory MCP receipts

All receipts below were produced in workspace mod_chaos_redux_ea3b2d67c2c0.

Map inspection for state 564 returned MAP_INSPECTED and artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4902683e5c8a5a6235567b40e16736601b3beac7d37766d7347648c86ef758bc/2f4b270b71f0d1753132e9f167a5892ce7e33027ab159af85927de011bc5046f/map-inspect.5dbdbe866ef44b19.json.

The state-membership, bitmap geometry, network/adjacency, and state-region checks passed for the inspected state.

The aggregate map validation remains false because unrelated global map/buildings.txt diagnostics report MAP_BUILDING_POSITION_INVALID and MAP_PORT_ADJACENT_SEA_INVALID; the MCP reported 1323 and 1331 instances respectively and truncated the global diagnostic list.

Map owner-layer render returned MAP_RENDERED with PNG artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a9b699614e18b16f89981f73bc332c1890dd0f192ef7d835376c3733745c209/cf83892f01ffa0142144bb9094582709c4bd55283100188a7f1f305228132ea0/map-owner.png, JSON artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9af401806a6ae79428e61e41c60d73c1a1583fe72600b9c363c5c4401514d601/da47e46ba611e2647aaf456261bb9a4d44ba109001720665ccdb4e34738d0750/map-owner.json, and HTML artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ec8e5f1b00e01bed20d7aeecf0b6b65e2ba60774cc4af527b3f63cc4b6dafe8/606257192db9722938576002730e372a633dac13fa73b9f0523f29fa7897e1a3/map-owner.html.

Shared focus inspection returned FOCUS_INSPECTED with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1195775176454abaf9d9425198bd113fabcb4232ff3eb4d5d64f22bc811353e8/f5f7db505425118b9f76345147a6ed0f749cc0a99d425fa43a4df8d78bcf1889/focus-inspect.39e449926f71d917.json.

The focus renderer returned FOCUS_RENDERED with HTML artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f73f5fb95e7f196377f3499cfaea352fd42460cf29e4e2b57ec55db429c00c22/5a74ae12b498c364ff5e42e2b2863a0b8ac95214fceea6b15b269c7fc50a60ff/independence_wave_focus_tree.focus.html, SVG artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/5b970ac6f5182f3edad960d93a918bf8c6d3836fe5c78eb0f20214605ed5fcc7/independence_wave_focus_tree.focus.svg, JSON artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1fa22e27d1d75ea6c5cda2b369f2a4efc1dbc3d4088e9158f7f0b0c002d93e85/da973aa2c4b7d964ba2e3538d975f5f6efcc907d2ab7e33d9c3ceeb4bdd35cd2/independence_wave_focus_tree.focus.json, source-map artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22cbd3044e248cafe1100fd1a2e5898ebb2eb2d72c31ae6e3687da8d6a69969e/e09c9c2fb09e09d181c85fcd6e124f78a60b621fe9ba4eb8381ecb20cec0cf48/independence_wave_focus_tree.focus.source-map.json, and plan artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c117b5c1ea4298004da7d67ef664911ba68608f453aac366efd580d4b5c1388b/89307de6aefa1e6b742d18de830db3c527b7f84eb4f70fe5f43f86d2c3e832cb/independence_wave_focus_tree.focus.plan.json.

Focus validation is aggregate-false because the shared workspace retains 14 unrelated missing continuous-focus icon diagnostics, including FOCUS_ICON_REFERENCE_MISSING for Denmark and Ethiopia continuous focuses.

Event inspection of events/006_independence_wave.txt returned EVENT_INSPECTED_PARTIAL with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d46a6456d89e06d74072bdedb8d8fed836f423b365a42aa89ad390af27f133b2/c2e3e6f4aa7b6dd82071976988f943c122b6fc59d8c5a41b01d0d9451f9f3385/event-scan-741883f50501.json.

Event rendering returned EVENT_RENDERED_PARTIAL with overview manifest under artifact/2a75ea96ef83c8c4da6fe0862d8752bf2a7c7d8a71b9bb83bf151a93318dd744 and linked JSON, SVG, PNG, and HTML artifacts.

The event tools reported the large-workspace partial-analysis limitation but no event-specific blocker.

Probability inspection of common/ai_strategy/006_independence_wave_buryatia.txt returned PROBABILITY_SOURCE_DISCOVERED with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e4d37065ed85d85140e31f169fd0474327ca9a26efab7ebce504bf34f652269/3a00add55d2dd30f05320089d1e55c2b975eadd237fb2b52b01336324ef82a21/probability-inspect-9d674af1611f.json.

The AI strategy adapter found no weighted surfaces because the strategy source has no direct candidate weights for that adapter.

Probability inspection of the BYA decisions returned PROBABILITY_SOURCE_DISCOVERED with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2874f03d7fafa6efbf3950e4b21a121618dc7a8c3ca7d32c7e4905657372180/91553236ca5e12fd7afacdb5f2ef6c2598db76b5967ed047062d2d747d74474d/probability-inspect-6ef191e231b0.json.

The decision adapter found no direct decision candidates, suggested mission_ai_will_do, and discovered 11 BYA mission candidates including independence_wave_bya_hold_frontier_council.

The required chaosx_ai_probability_auditor callable was not exposed in the installed tool inventory, so the mandatory auditor-mediated probability compare could not be run.

No true before/after probability compare was claimed because no prepatch BYA source existed and the auditor route was unavailable.

No Technology Tree Viewer is exposed by the installed package; no technology source was changed in this tranche.

## Remaining blockers and review risks

The parent must provide the rights flag and independently accept the sourced identity and portrait evidence before any central admission wiring.

The package has no parent-owned central adapter, attestation, preflight, scenario, or Join entry by design.

The installed map and shared focus diagnostics contain unrelated aggregate failures documented above.

Live game validation was not run because agents do not launch Hearts of Iron IV; the parent/user owns live consumer validation.

No source fallback, generic portrait, Event 005 leader reuse, vanilla file edit, map edit, flag edit, or workbook edit was made.

No staging or commit was performed.
