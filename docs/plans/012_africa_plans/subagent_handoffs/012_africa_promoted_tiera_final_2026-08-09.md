# Event 012 Africa Promoted Tier A Final Handoff — 2026-08-09

## Scope completed

Implemented six additive promoted Tier A high-chaos country packages: Pan (EBX), Gorilla Kingdom (EHX), The Green (DPX), Living Rivers (EEX), Stoneborn (DFX), and Ancient Hosts (DHX). Existing Event 006 tags are reused; no country tag, state, portrait binary, model, or generic fallback was added.

## Deterministic state and map evidence

The final bindings are EBX→900, EHX→768, DPX→298, EEX→548, DFX→460, and DHX→448+661. Map MCP inspected all original candidates. State 900 is Benue (capital 8034, pastoral, ENG/core NGA, coal 2, infrastructure 2); 768 is Rwanda (capital 9962, pastoral, BEL/core RWA, tungsten 3, infrastructure 1); 298 is Liberia (capital 7959, rural, LIB/core LIB, rubber 6, arms factory 1 and industrial complex 1); 548 is Uganda/Great Lakes (capital 12989, rural, ENG/core UGA, rubber 3); 460 is Constantine/Kabylia (capital 12051, FRA/core ALG, infrastructure 2); 448 is Tripoli (capital 1149, ITA/core LBA, naval base 5, VP 10); and 661 is the wasteland Tripolitania extension (no capital/VP). The exact inspected artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f18294f01309cafcabe412ba2e07578a05f1112701dd4da49b665f565f9c9739/62fff6d52100d14b0f9fbb67e2f808c79c02a5e33a29c7a1aa3a0d652f7ebb12/map-inspect.0007c964ddcb2856.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47beb95caf2ad27ab2e62e0ea5ffc37080592b16c116b6d48dbed52979c57411/cd355c39b48ae0e5b3db16a7941d4342e8da55658ea639e617e66f21a384f2a8/map-inspect.c43040f3b71aeba0.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a21f7fe1ae85037e5a6ef112f7680223be69e91a4e7d6a6dea8db05c969eeabe/95dd4216ac75d6eae0cdbedb1305db1f6eade3d80734d98d9d0cc20d1c8dfe5b/map-inspect.f8392b6591b771c7.json`.

Map geometry, state-region membership, networks, and adjacencies passed. The installed map has pre-existing global locator diagnostics (`MAP_BUILDING_POSITION_INVALID` 1323 and `MAP_PORT_ADJACENT_SEA_INVALID` 1331); no map write was made. Earlier Ghana state 274 and shared Uganda state 548 alternatives were rejected to avoid Asante priority overlap and EHX/EEX collision. The state predicates fail closed on owner, controller, capital, and global claim flags.

## Gameplay surfaces

Changed gameplay files are `common/script_constants/012_africa_promoted_tiera_constants.txt`, `common/scripted_triggers/012_africa_promoted_tiera_triggers.txt`, `common/scripted_effects/012_africa_promoted_tiera_effects.txt`, `common/scripted_effects/012_africa_promoted_tiera_settlement_effects.txt`, `common/ideas/012_africa_promoted_tiera_ideas.txt`, `common/decisions/012_africa_promoted_tiera_decisions.txt`, `events/012_africa_promoted_tiera_events.txt`, `common/ai_strategy/012_africa_promoted_tiera.txt`, `common/on_actions/012_africa_promoted_tiera_on_actions.txt`, and `common/countries/012_africa_cosmetic.txt`.

Every package has three distinct politics routes, a package-specific starting/route/mature idea lifecycle, a mechanic progress track, an exact strange-force consumer set, a League acceptance/counter/refusal/rival path, explicit congress/local-consent/autonomy/rival overlap settlement, a cosmetic identity applied only at reveal, package-specific AI, and post-settlement effects. `africa_promoted_tiera_cleanup_on_defeat` drops the cosmetic identity, clears the package ledger and claim flags, and marks containment while preserving the original carrier tag.

The exact eight force wrappers are `africa_strange_force_spawn_pan_sappers`, `africa_strange_force_spawn_oracle_recon`, `africa_strange_force_spawn_gorilla_heavy_infantry`, `africa_strange_force_spawn_forest_giants`, `africa_strange_force_spawn_riverborn`, `africa_strange_force_spawn_disaster_wardens`, `africa_strange_force_spawn_stone_cohorts`, and `africa_strange_force_spawn_plague_carriers`; each decision also requires the global formation-package gate.

## Localisation and assets

`localisation/english/012_africa_promoted_tiera_l_english.yml` is UTF-8 with BOM and has no `:0` keys or leading key indentation. Fictional portrait IDs remain exactly `GFX_portrait_012_africa_fictional_pan`, `GFX_portrait_012_africa_fictional_gorilla_kingdom`, `GFX_portrait_012_africa_fictional_the_green`, `GFX_portrait_012_africa_fictional_living_rivers`, `GFX_portrait_012_africa_fictional_stoneborn`, and `GFX_portrait_012_africa_fictional_ancient_hosts`; no binary was edited. Force decisions use `GFX_decision_012_africa_{pan_sappers,oracle_recon,gorilla_heavy_infantry,forest_giants,riverborn,disaster_wardens,stone_cohorts,plague_carriers}` from the committed strange-force icon package.

## MCP and validation notes

The shared focus tree `africa_priority_member_focus_tree` was inspected and rendered with eight focuses and no structural diagnostics; render artifacts were retained in the parent audit. The bounded Event 012 event graph was inspected/rendered through `chaosx.nr12.1` and `africa_priority_member.1200`; the server returned partial graph artifacts with 14 pre-existing global blocking diagnostics but no source skipped. Probability adapter listing succeeded. A narrow probability inspect on the new AI strategy returned `PROBABILITY_SURFACE_EMPTY`, and a decision-source inspect timed out after 180 seconds; these are recorded blockers for the parent `chaosx_ai_probability_auditor` to rerun as narrow decision IDs and compare scenarios.

## Deferred or owned elsewhere

Portrait binaries, source provenance, 3D models/entities, model animations, audio, and counter binaries remain deferred to their owning workers. The installed Technology Tree Viewer route is unavailable; no new technology definition was added. No simplification was made to the six gameplay identities, state guards, overlap settlement, or force-consumer access.
