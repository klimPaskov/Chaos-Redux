# Event 006 country/package readiness audit — AXX, BAX, BBX

Date: 2026-08-21

Owner: `event006_country_audit`

Status: source audit complete; no scoped gameplay patch is justified; runtime receipt/state evidence is still required for the reported manual `chaosx.nr6.1` no-country outcome.

## Scope and conclusion

This audit covers the Event 006 Banat package `IW024`/`AXX`, Thrace package `IW027`/`BAX`, and Epirus package `IW028`/`BBX`, including country registration, country/history/character setup, package effects and triggers, leaders, ideas, AI strategy, flags, directly paired localisation, and the release/transfer/capital/package transaction consumers.

Shared focus, decision, event-GUI, and unrelated map files were not edited or treated as package defects.

The reported invalid `capital_scope` regression is not present in the three package trigger files: all three package anchor checks use numeric state scopes (`82`, `184`, and `185`) with `is_capital = yes`. The only `capital_scope` found in `events/006_independence_wave.txt` is a live-country decision AI modifier and is not on the dormant package-availability path.

The dormant-shell predicate is guarded by `NOT = { num_of_controlled_states > 0 }` and the absent-tag/existing-shell release transaction is internally coherent. No fail-closed source gate should be weakened and no fallback package should be added.

## Country package coverage checklist

| Package | Tag | Package id | Anchor state | Former host | Optional extension | Result |
| --- | --- | --- | ---: | --- | ---: | --- |
| Banat | `AXX` | `IW024` | 82 | `ROM` | — | Covered; dormant anchor gate and runtime-ready gate agree. |
| Thrace | `BAX` | `IW027` | 184 | `GRE` | — | Covered; dormant anchor gate and runtime-ready gate agree. |
| Epirus | `BBX` | `IW028` | 185 | `GRE` | 805 | Covered; state 805 is an explicitly separate extension allocation. |

All three tags are registered in `common/country_tags/006_independence_wave_countries.txt` and map to existing country definitions in `common/countries/006_independence_wave_AXX.txt`, `006_independence_wave_BAX.txt`, and `006_independence_wave_BBX.txt`.

The country histories `history/countries/AXX - Banat.txt`, `BAX - Thrace.txt`, and `BBX - Epirus.txt` intentionally provide neutral dormant shells rather than starting territory. Startup character recruitment is supplied by `history/general/006_independence_wave_additional_character_recruitment.txt:35-46`, which recruits the fixed-tag identities before runtime release.

## File surface checklist

The audited source surfaces are:

- Registration and country definitions: `common/country_tags/006_independence_wave_countries.txt`; `common/countries/006_independence_wave_AXX.txt`; `common/countries/006_independence_wave_BAX.txt`; `common/countries/006_independence_wave_BBX.txt`.
- History and roster: `history/countries/AXX - Banat.txt`; `history/countries/BAX - Thrace.txt`; `history/countries/BBX - Epirus.txt`; `history/general/006_independence_wave_additional_character_recruitment.txt`; `common/characters/006_independence_wave_banat_characters.txt`; `common/characters/006_independence_wave_thrace_characters.txt`; `common/characters/006_independence_wave_epirus_characters.txt`.
- Package effects: `common/scripted_effects/006_independence_wave_banat_package_effects.txt`; `common/scripted_effects/006_independence_wave_thrace_package_effects.txt`; `common/scripted_effects/006_independence_wave_epirus_package_effects.txt`; `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`; `common/scripted_effects/006_independence_wave_execution_effects.txt`.
- Package triggers and dispatch: `common/scripted_triggers/006_independence_wave_banat_package_triggers.txt`; `common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt`; `common/scripted_triggers/006_independence_wave_epirus_package_triggers.txt`; `common/scripted_triggers/006_independence_wave_package_triggers.txt`; `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
- Ideas, AI, and direct localisation: `common/ideas/006_independence_wave_banat_ideas.txt`; `common/ideas/006_independence_wave_thrace_ideas.txt`; `common/ideas/006_independence_wave_epirus_ideas.txt`; `common/ai_strategy/006_independence_wave_banat.txt`; `common/ai_strategy/006_independence_wave_thrace.txt`; `common/ai_strategy/006_independence_wave_epirus.txt`; `localisation/english/006_independence_wave_countries_l_english.yml`; `localisation/english/006_independence_wave_banat_l_english.yml`; `localisation/english/006_independence_wave_thrace_l_english.yml`; `localisation/english/006_independence_wave_epirus_l_english.yml`.
- Portrait wiring and flags: `interface/006_independence_wave_iw024_banat_portraits.gfx`; `interface/006_independence_wave_iw027_thrace_portraits.gfx`; `interface/006_independence_wave_iw028_epirus_portraits.gfx`; the corresponding `gfx/leaders/006_independence_wave/` DDS files; and the complete Event 006 flag families under `gfx/flags/`.

## Release transaction trace

1. `common/scripted_triggers/006_independence_wave_package_triggers.txt:30-42` defines a dormant shell as absent or existing with zero owned states, zero controlled states, no active origin flag, no prepared-origin flag, and no committed-origin flag. The controlled-state guard is `NOT = { num_of_controlled_states > 0 }`.
2. `candidate_origin_available` additionally requires the reservation marker to be absent or owned by the current transaction, and the shared anchor predicate requires the selected state to have an owner/controller and not be a protected active-origin state.
3. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:353-365` requires the package id, dormant state, and exact package gate before dispatch. Runtime adapters and content attestations include `IW024`, `IW027`, and `IW028`.
4. `common/scripted_effects/006_independence_wave_execution_effects.txt:201-340` validates every target as dormant/current-reserved, package-preflight-ready, and anchored to the expected former host before mutation.
5. `common/scripted_effects/006_independence_wave_execution_effects.txt:348-451` masks historical cores, adds package cores, releases an absent tag with the former host as the release scope, and skips the engine `release` no-op for an existing dormant shell. A living target is rejected; no unapproved fallback is present.
6. `common/scripted_effects/006_independence_wave_execution_effects.txt:453-506` transfers the allocated Event 006 states to the target and verifies both ownership and control after each transfer.
7. `common/scripted_effects/006_independence_wave_execution_effects.txt:530-559` enters the target country scope, assigns the anchor state with `set_capital = { state = event_target:anchor remember_old_capital = no }`, prepares the country, and dispatches package setup.
8. `common/scripted_effects/006_independence_wave_execution_effects.txt:563-620` activates the prepared package, runs final validation, and commits only after the final validation gate passes.
9. `common/scripted_effects/006_independence_wave_execution_effects.txt:681-797` is the standalone transaction path; `:840-923` is the manual transaction wrapper that fires `chaosx.nr6.2` only after a committed receipt.

The package-specific capital guards are deliberately state-scoped. `AXX` requires state 82 to be the target capital and owned/controlled by `AXX`; `BAX` requires state 184; `BBX` requires state 185. No package trigger calls `capital_scope`.

## Map and state setup

The offline vanilla state precedents and the read-only HOI4 MCP state inspection agree on the following anchors:

| State | Vanilla owner | Capital province | Package use | Relevant setup |
| ---: | --- | ---: | --- | --- |
| 82 | `ROM` | 9606 | `AXX` anchor | Aluminium 4; military/industrial setup; VP 3 at province 9606. |
| 184 | `GRE` | 11905 | `BAX` anchor | Chromium 11; arms factory 1; infrastructure 1; VP 1 at province 11905. |
| 185 | `GRE` | 3914 | `BBX` anchor | Chromium 14 and steel 14; naval base at 9805; air base 3; industrial complex 1; VPs at 3914, 10203, and 1205. |
| 805 | `ALB` | 914 | `BBX` optional extension | Infrastructure 1; VP 1 at province 914; allocated separately by package logic. |

The selected-state MCP records resolve owners and capitals, and the state-layer MCP render validates the offline representation. No map write was performed because the defect report is in country/package release handling and no concrete source map defect was found.

The map inspection also reports unrelated global diagnostics in `mod:map/buildings.txt` (`MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`). They are outside the Event 006 country/package scope and are not evidence that states 82, 184, 185, or 805 are invalid.

## Politics, leaders, portraits, flags, advisors, and parties

The three history shells use neutral politics with neutrality 100, and package setup owns the runtime territory, capital, politics, leaders, forces, ideas, and AI configuration as documented in the country files.

The startup roster is complete for the package leaders: `AXX_independence_wave_banat_presidium`, `BAX_independence_wave_thrace_council`, `BBX_independence_wave_epirus_council`, and `BBX_independence_wave_spyros_spyromilios` are recruited in the additional-character history file and are promoted by the package effects at runtime.

The character definitions use male metadata and male-presenting identity names for the four supplied runtime portraits. No opposite-gender name-pool or female-leader metadata pairing was found. The packages do not require an advisor or high-command identity for the release transaction.

The four runtime portrait DDS files are wired through the three package-specific GFX files and do not point into the durable `docs/assets` archive. The supplied 156x210 DDS inputs remain source-placeholder runtime assets rather than styled finals; the prior portrait handoffs contain provenance/crop evidence and the supplied-runtime hashes. No portrait source patch is justified.

The strict Event 006 flag audit reports all 102 registered tags with complete normal, medium, small, and ideology variants. No flag patch is justified.

Party names, country names, adjectives, leader names, package idea names/descriptions, and all package `set_party_name` tokens have directly paired localisation keys. No localisation patch is justified.

## Focus, decision, idea, and asset surfaces

The package effects and triggers include the expected focus-tree, route/formable, idea, force, AI, and cleanup attestations for `IW024`, `IW027`, and `IW028`. Focus-tree and decision implementation/auditing were intentionally left to the parent because the task explicitly excludes shared focus/decision/event-GUI files.

The three package idea files and their direct localisation are present and match the package effect identifiers, including the starting weakness and route lifecycle ideas. No icon or idea-id mismatch was found in the scoped files.

The installed HOI4 MCP package does not expose a Technology Tree Viewer. No technology-tree patch was attempted, and technology readiness remains a parent/engine validation limitation rather than a reason to weaken the release source gates.

## Starting military, technology, industry, supply, and production

The package effect files contain the expected package-specific starting force, equipment-production, infrastructure, bunker, and supply/industry setup calls, and dispatch reaches the package setup effects only after the exact package gate. The state inspection confirms the selected anchors carry the expected vanilla industrial/resource/naval context.

This audit did not add armies, equipment, factories, technology, supply nodes, railways, ports, or other balance changes. No concrete setup inconsistency was found that would justify such a patch.

## AI and playability

The three package AI strategy files exist, use the correct original-tag guards, and reference package setup/profile flags and strategy names for `AXX`, `BAX`, and `BBX`. They do not introduce a cross-tag reference or an unregistered package id.

The mandatory `hoi4.probability_inspect` pass found no weighted surfaces for Thrace and Epirus (`PROBABILITY_SOURCE_DISCOVERED`, `discoveryReason = no_weighted_surfaces`, zero candidates). The Banat adapter returned an exact MCP `INTERNAL_ERROR: Unexpected internal error`; the Epirus adapter initially returned the same error but succeeded without the adapter with the same no-weighted-surfaces result. Because the AI route is not quantitatively inspectable for Banat, no AI weight or strategy-factor patch or probability comparison was claimed or applied.

## Validation evidence

Static Event 006 checks completed against the current tree:

- `python -B .tools/audit_chaosx_country_tags.py --surface-scan`: 136 protected Event 006/Soviet tags; zero external country-definition collisions; zero external identity-surface collisions; one skipped random-event root.
- `python -B .tools/audit_event6_country_api.py`: 242 broad unique tags; 191 resolved carriers; zero missing; zero duplicates.
- `python -B .tools/audit_event6_flags.py --strict`: 102 registered tags; 102 complete flag families; zero incomplete.
- `python -B .tools/audit_event6_allocator.py`: allocator and package reservations passed, including the current positive target count and protected host-state checks.
- `python -B .tools/audit_event6_scenario_matrix.py`: all 32 SCN-008 cells and 8 edge-case receipts passed.
- `python -B .tools/audit_event6_form16.py`: admitted-carrier, state, consent/refusal, mutation, rollback/cleanup, and readiness checks passed.

Read-only HOI4 MCP evidence:

- Event lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3d419ff19ce207cb0110493bb3a315f8faac09208c62689a54ec136544cefda/736e1313a62b0cbd7e05e5796f4ff09867abb24bb94d746e67e35eeea7a63004/event-lint-bc0062fc8506.json` with zero blocking diagnostics for the requested source projection.
- Event state render: manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d1dec1775fec791c205006bc4b4d1ac0c57d0b74a2d7d50c94cab8a5fdd9c0a1/b8234721ae57a7ab312356790e5098dd2a4dea5a5785b740a3a628b52f36a979/event-state-bc0062fc8506-manifest.json` and corresponding JSON/SVG/PNG artifacts under the same MCP run.
- Map state inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b41eea68e1c61384eb62a4e0159cb53b543c8b56f483ef57031b521c2cd7d400/18ca6c3ff22c0b57a1cb6ca9cc1792b1867cd1ddb896bba1a5e9c998bfe3a095/map-inspect.3665a7b49fd0ffa1.json` for states 82, 184, 185, and 805.
- Map state render: PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1e048305649726acd6ca2586a15c2fcdcd904d4b5c238d1374b8bb5d3294a8d/992ebf478dd9b6bc4cb5ee9738bb53cbb4fab7e86c0561a33eefa4df11fb3fe1/map-state.png` and companion JSON/HTML artifacts under the same MCP run.
- AI probability artifacts: Thrace `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c24c68957861244b12429306ad72f92471e73dfd0648dc881dd07e1a2586ed5f/3bf5c8cd93056606fbd55736d879e96518406f65a5075119836d7219793aa5f5/probability-inspect-a2989b651f3c.json`; Epirus `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6742f6686c2c6f812cb3119858ef8d0a792ca841cfc5d3c709e315a1a8950e9/532f82049315feab8511a234f4aee977386603c8d9809624c594827723cb5637/probability-inspect-3ccff62c6b65.json`; Banat adapter blocker `INTERNAL_ERROR: Unexpected internal error`.

## Changed files and identifiers

No scoped gameplay source file was changed in this audit.

The only file added is this handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_country_package_audit_current_2026_08_21.md`.

Changed tags: none.

Changed state ids: none.

Changed leaders, parties, ideas, focus ids, formable ids, localisation keys, AI strategy factors, flags, and runtime assets: none.

## Remaining blockers and next discriminator

The source audit cannot reproduce the user's manual `chaosx.nr6.1` world state without a terminal receipt or game-state snapshot. The next useful discriminator is the exact terminal receipt from the same invocation, including `global.independence_wave_terminal_receipt_*`, `global.independence_wave_standalone_*` counters/flags, and the per-origin committed/prepared/failed/rollback flags. This separates pre-mutation cancellation, rollback after transfer, and finalization failure without weakening any source gate.

The Event MCP graph is a workspace-wide partial projection with deferred helper/lifecycle nodes but zero blocking diagnostics in the requested source projection. The map MCP reports unrelated global building/port diagnostics. The Banat probability adapter has an MCP internal error. These are evidence limitations, not reasons to alter package logic.

No fallback package, fixed capital scope, cross-tag identity, broad balance change, shared focus/decision/event-GUI change, or map write was introduced.
