# IW-153 POK compatibility preservation audit — 2026-08-14

## Disposition

The committed IW-153 adapter is bounded, source-backed, and correctly dormant.

No gameplay or central source patch is justified by this audit, and the adapter remains `specific_community_variant_only` and `unbound`.

No central adapter, content attestation, normal or scenario preflight, Join candidate, dispatcher, event, history, character, core, releasable, localization, portrait, flag, or route entry was changed.

The newly committed IW-155 BLI adapter is noted only as a parallel package-local pattern; it does not widen IW-153 authority or resolve the Dayak identity and asset gates.

## Accepted identity and restriction

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:236` requires IW-153 to reuse registered `POK`, preserve registered POK history, characters, cores, Indonesian releasable membership, and `indonesia_transfer_POK`, while remaining `specific_community_variant_only` and unbound.
- `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md:59` records the retired `FWX` to registered `POK` migration and the same preservation obligations.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:154` records `POK`, disposition `reuse_registered_tag`, restriction `specific_community_variant_only`, anchor `334`, reservation group `RG-BORNEO-DAYAK`, and the final note to keep the named-community restriction and vanilla preservation gates.
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:69` reserves state 334 only after a named Dayak polity is selected and explicitly rejects a generic substitute.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:154` records IW-153 as `specific_variant_only_unbound`, anchor 334, and `baseline_rejected` because no authoritative current-map binding exists.

## Current adapter source

- `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt:21-29` requires `original_tag = POK`, active Event 006 origin, `liberation_origin = independence_wave`, package id `iw_153`, and the future named-community selector flag `independence_wave_iw_153_named_community_selected`.
- `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt:34-37` provides a read-only witness for `INS_syarif_muhammad_alkadrie` and does not recruit, remove, promote, or re-nationalize the character.
- `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt:43-47` witnesses both installed POK cores, state 334 and state 1022, without adding or removing cores.
- `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt:52-58` witnesses `POK` in the `INS_releasables` array from the `INS` scope without mutating the array.
- `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt:63-69` combines the origin, selector, character, core, releasable, and state-334 capital gates into a strict future named-community contract rather than a generic Dayak route.
- `common/scripted_effects/006_independence_wave_iw153_pok_compatibility_effects.txt:20-34` clears only the reserved named-community selector flag after the complete POK/Event 006/IW-153/selection gate passes.
- `common/scripted_effects/006_independence_wave_iw153_pok_compatibility_effects.txt:40-54` exposes a cleanup wrapper that is inert unless the same exact context is live and never clears origin, package identity, history, cores, characters, releasables, or vanilla transfer behavior.

## Vanilla preservation evidence

- Vanilla `common/country_tags/00_countries.txt:379` registers `POK = "countries/Pontianak.txt"`; no replacement tag or country definition was added.
- Vanilla `history/countries/POK - Pontianak.txt:1-3` keeps capital state 334 and recruits `INS_syarif_muhammad_alkadrie`; no Chaos Redux history override exists.
- Vanilla `history/states/334-Kalimantan Barat.txt:17-18` assigns owner `INS` and `add_core_of = POK`.
- Vanilla `history/states/1022 - Interior Borneo.txt:18-21` assigns owner `INS`, preserves the installed core set, and includes `add_core_of = POK`.
- Vanilla `history/countries/INS - Indonesia.txt:276` places `POK` in `INS_releasables`.
- Vanilla `common/characters/INS.txt:2941-2942` defines `INS_syarif_muhammad_alkadrie`; the adapter only witnesses its presence on the registered POK carrier before any transfer.
- Vanilla `common/scripted_effects/INS_scripted_effects.txt:45-74` defines `indonesia_transfer_POK`; when POK exists it sets the character nationality to INS, removes the despotism country-leader role while retaining the advisor path, and saves the global character target, while the fallback searches other countries when POK does not exist.
- The adapter does not call, override, duplicate, or reverse `indonesia_transfer_POK`; its character predicate is intentionally a pre-transfer source witness.

## Central fail-closed boundary

- `common/script_constants/006_independence_wave_country_registry_constants.txt:66-67` places POK in `registered_reuse_unbound_tags`.
- `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:135-203` includes POK only in generic registered-reuse membership; membership alone is not an activation gate.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` has no `iw_153` runtime adapter entry.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` has no `iw_153` content-attestation entry, so the shared preflight at `:207-214` rejects it before release.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-61` and `:92-121` dispatch only admitted package setup/final-validation/cleanup helpers and have no IW-153 branch.
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:69-80` and `:372-380` show the newly committed IW-155/BLI loader as an admitted regional pattern; no IW-153/POK loader exists, which is correct while POK remains unbound.
- `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt:45-52` is likewise BLI-specific and does not make POK selectable.

## Join boundary

- `common/scripted_triggers/006_independence_wave_join_triggers.txt:9-22` uses a generic source-identity gate that excludes active Event 006 origins and Event 006-owned new tags; it does not itself promote registered-reuse POK content.
- `common/scripted_effects/006_independence_wave_join_effects.txt:128-164` routes Join probing through exact package reservation wrappers, not generic country labels.
- `common/scripted_effects/006_independence_wave_join_effects.txt:213-247` enumerates the exact attested package IDs tried by Join and contains no `iw_153` candidate.
- `common/scripted_effects/006_independence_wave_join_effects.txt:278-343` offers Join only after the attested package probe succeeds; therefore an eligible vanilla POK source cannot turn the unbound IW-153 row into Event 006 content.
- This is a fail-closed boundary, not permission to add POK to Join. A future named-community decision would require a separate accepted central admission change outside this adapter.

## MCP evidence

- Read-only `hoi4.map_inspect` selected state IDs 334 and 1022 in workspace `mod_chaos_redux_ea3b2d67c2c0` and returned `MAP_INSPECTED`; selected-state data reported two inspected states, zero unknown province IDs, and zero missing geometry IDs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dcadf34561ad8f3db91c3022996b33d53f71fb861d73b21c8fab9b3e5fe6fb30/496e17a11df39436cae1fab2b7b68b83bc5964beecd0af42f7f153aa291966fb/map-inspect.a346a330dcdc48c8.json`.
- The map receipt passed state/region membership, bitmap geometry, networks, adjacencies, supply, and railway checks; aggregate validation was false only because unrelated workspace-wide `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics exceeded the result ceiling.
- Read-only `hoi4.event_inspect` focused on the Event 006 root `chaosx.nr6.1` and returned `EVENT_INSPECTED_PARTIAL` with no blocker and no proposed or changed files. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c2210156e2d70884fd2bfdeca75bc5a9d5f0a87f609df6f0df47735e95869a6/3d9ea8a1bede135bb512571d954bd6c6dc5b88135e35cf044966cf8df69bb220/event-scan-741883f50501.json`.
- The event receipt is partial because the large workspace analysis deferred broad helper projections; the dormant POK adapter has no event call site and no event-specific runtime branch to inspect.
- Probability inspection was not applicable because the POK adapter contains no AI weight, MTTH, random-list, score, or probability-bearing helper.

## Validation and blockers

- Static source checks re-confirmed balanced braces, tab-indented script blocks, no unsupported `<=` or `>=`, no unary variable negation, and no prohibited POK mutations such as `add_core_of`, `remove_core_of`, `recruit_character`, `set_nationality`, `add_to_array`, `remove_from_array`, tag changes, OOB loads, or route effects in the adapter files.
- The current POK trigger/effect files and committed adapter handoff were not modified by this audit, and no central list or Join source was changed.
- No live HOI4 run, save/load, or runtime asset validation is claimed.
- Remaining blockers are the named Dayak polity or precise regional institution, exact territory/host contract, sourced period-fit leader or institutional identity, portrait provenance, and attested symbol/flag source; the broad Dayak label and state 334 alone remain insufficient.

## Recommendation

Keep the current adapter and central fail-closed boundaries unchanged.

Do not add POK to runtime dispatch, attestation, preflight, regional selection, Join candidates, or any identity/asset surface until the accepted named-community gates are resolved and a separate parent-approved admission tranche exists.
