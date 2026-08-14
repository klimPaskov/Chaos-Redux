# IW-150 ATJ compatibility adapter handoff

Date: 2026-08-14

## Disposition

Implemented a bounded, package-local, source-backed preservation boundary for IW-150. ATJ remains dormant, high-chaos-only, and fail-closed. The adapter does not admit IW-150 to Event 006 and does not claim that the unresolved 1936 identity or symbol gates are complete.

The adapter is inert unless a living registered ATJ carrier has the active Event 006 origin, the exact IW-150 package id, the current ATJ anchor, and a future source-backed institutional-selection marker. The normal vanilla Indonesian release and character-transfer route remains owned by vanilla sources.

## Files changed

| File | Identifiers | Scope and side effects |
| --- | --- | --- |
| `common/scripted_triggers/006_independence_wave_iw150_atj_compatibility_triggers.txt` | `is_independence_wave_iw_150_atj_compatibility_context`, `has_independence_wave_iw_150_atj_anchor_surface`, `has_independence_wave_iw_150_atj_character_surface`, `has_independence_wave_iw_150_atj_core_surface`, `has_independence_wave_iw_150_atj_releasable_surface`, `has_independence_wave_iw_150_atj_compatibility_contract` | Country-scope read-only predicates. The strict contract requires `original_tag = ATJ`, active Event 006 origin, `liberation_origin = independence_wave`, package id `iw_150`, the future `independence_wave_iw_150_institution_selected` marker, ownership and control of current state 1050, capital state 1050, the ATJ core, `INS_alauddin_syah`, and Indonesia's `INS_releasables` entry for ATJ. |
| `common/scripted_effects/006_independence_wave_iw150_atj_compatibility_effects.txt` | `independence_wave_iw_150_atj_compatibility_clear_institution_selection`, `independence_wave_cleanup_iw_150_atj_compatibility` | Country-scope cleanup wrappers. They only clear the future selection marker after the complete strict contract passes. They never set the marker and never mutate origin state, package identity, ownership, cores, characters, assets, or the Indonesian transfer route. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw150_atj_compatibility_adapter_2026_08_14.md` | This handoff | Records the source boundary, engine evidence, unresolved identity gates, and follow-up limits. |

No central adapter, content attestation, preflight, dispatcher, Join, event, decision, focus, force, AI, flag, portrait, localisation, workbook, country-history, or vanilla file was changed.

## Country package coverage checklist

| Surface | Status | Evidence or limitation |
| --- | --- | --- |
| Registered tag and country definition | PASS for preservation | Installed vanilla `common/country_tags/00_countries.txt` registers `ATJ = "countries/Atjeh.txt"`. Installed `common/countries/Atjeh.txt` remains the vanilla definition. No Chaos Redux tag or country definition was added. |
| Research state and current anchor | PASS for bounded adapter | Research state 672 is a coarse Sumatra anchor only. The current installed map binding rebinds IW-150 to state 1050, `Atjeh`, with Banda Aceh victory point 13398. Runtime predicates intentionally use state 1050 and do not treat state 672 as a live Aceh state. |
| State owner, controller, core, capital, port, victory point, and supply | PASS for source witness, no write | Vanilla `history/states/1050-Ajteh.txt` has `owner = INS`, `add_core_of = ATJ`, port building at province 13398, and victory point 13398. The adapter checks only the released ATJ ownership and control of state 1050, its capital, and the ATJ core. No map rewrite was made. |
| Country history and leader | PASS for preservation | Vanilla `history/countries/ATJ - Atjeh.txt` uses capital 1050 and `recruit_character = INS_alauddin_syah`. The adapter observes `has_character = INS_alauddin_syah` and never recruits or removes it. |
| Indonesian releasable and transfer route | PASS for preservation | Vanilla `history/countries/INS - Indonesia.txt` contains `add_to_array = { INS_releasables = ATJ }`. Vanilla `common/scripted_effects/INS_scripted_effects.txt` owns `indonesia_transfer_ATJ`. The adapter only checks array membership and never calls, replaces, or duplicates the transfer effect. |
| Politics, party, leader identity, advisors, and council | BLOCKED for package admission | The accepted 1936 opening is a coalition of uleebalang, ulama, merchants, veterans, schools, ports, and district notables. No source-cleared institutional leader consumer has been admitted. This adapter does not invent one. |
| Portraits and portrait-specific wiring | BLOCKED and out of scope | No portrait asset or runtime consumer was added. Any future character portrait remains subject to the portrait-worker route. |
| Flags, symbols, and cosmetic identity | BLOCKED and fail-closed | The neutral 1936 coalition symbol remains on HOLD. The Sultanate reconstruction is route-owned and conditional, while PUSA material is date-gated to 1939 or later. No asset or runtime basename was added. |
| Focus tree | Shared tree only, no ATJ route | The shared `independence_wave_focus_tree` has no ATJ-specific route or assignment in this tranche. The focus inspect and render reported existing workspace diagnostics, including 14 blocking diagnostics, that are unrelated to these new files. |
| Decisions, missions, ideas, and package lifecycle | NOT IMPLEMENTED | IW-150 has no package setup, final validation, cleanup, force receipt, ideas, decisions, or mission surface in the current source. This handoff does not create those systems. |
| Starting military, technology, industry, supply, and production | NOT IMPLEMENTED | Vanilla ATJ history remains the only starting setup. No IW-150 balance or production patch was made. The installed Technology Tree Viewer route remains an unresolved project limitation for a package-specific tech review. |
| AI and probability | UNCHANGED | No AI weight, strategy factor, MTTH, random selection, or weighted target was edited. The mandatory probability compare route is therefore not applicable to this source-only preservation patch. |

## Event 006 origin and living-tag guards

`is_independence_wave_iw_150_atj_compatibility_context` requires all of the following:

- `exists = yes` and `original_tag = ATJ`.
- `is_independence_wave_active_country = yes`.
- `independence_wave_active_origin` and no `independence_wave_origin_ended` flag.
- `liberation_origin = independence_wave`.
- `independence_wave_package_id = iw_150`.
- The future package-local institution-selection marker.

The helper therefore cannot match dormant ATJ, an ordinary vanilla release, a different Event 006 package, a different origin system, or an ended Event 006 origin. The cleanup wrappers are contract-gated and idempotent. No caller was added, so ordinary vanilla gameplay remains unchanged.

## Engine evidence

- Read-only `hoi4.map_inspect` queried state IDs 672 and 1050 and province 13398 in workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `MAP_INSPECTED` and inspected two states plus the requested province. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a86e7d7d60b46ca7f63c1818ddcabe00bea4c27dddf57b5ee868c4da8c8ffec/e2668787cc3de7868ff8dcca978dcdc125c46b866f5e488918933ff7baf80c7b/map-inspect.24bebf72ae84437c.json`.
- Read-only `hoi4.map_render` produced the state-layer render with coastlines, ports, victory points, buildings, supply nodes, and railways. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1267c78960792f34acb0720cc9b464e991bd196f66545c1f070a9758160f0471/35f79eea9be0f532121dcf6281883e05e50a683095d12000fb7e7b09fc9dc5ce/map-state.png`.
- The map inspection aggregate validation is false because unrelated workspace `map/buildings.txt` locator and floating-harbor diagnostics exceeded the diagnostic ceiling. The selected ATJ state and province were not rewritten. No map blocker is introduced by this adapter.
- Read-only `hoi4.event_inspect` traced `chaosx.nr6.1` with downstream depth 3 and returned `EVENT_INSPECTED_PARTIAL`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f0a4f9f056ba935608a6d6368fc6cd93e3da3fe067a369ea0a16b433732de0dc/6a3f1083f059c0eacf2f4daee7fabea9a504f15887965321cc98edce8cd1d32b/event-trace-741883f50501.json`.
- Read-only `hoi4.event_render` produced the Event 006 overview and returned `EVENT_RENDERED_PARTIAL`. The overview render had no blocking diagnostics, but the workspace-wide event graph remains partial. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7def116a59f2895e74ca36ea05346922337000b2180569ff89b3fe12d768bf90/2c93dd3682ffa88d27b2754368d085bacbab50413c3dfdd4b8f47a71406d07a8/event-overview-741883f50501.png`.
- Read-only `hoi4.focus_inspect` and `hoi4.focus_render` reviewed the shared `independence_wave_focus_tree`. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a97b38692089d1f94065c97a0796597cd98e43c8b0593c07705fbb023d4b525/c5e76edae9b0a78a03b56366e0c8bc776868766d0c193519a4e4fccd1a7a3af7/focus-inspect.5bb17398adee2259.json`. Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b95abe18cc1f9ee16a845c3a40adbc706efcebdcc77887c7afef6ca02d62c36a/f56fae85bd94de3d84ad9d80df0f4ed7f41d7486808bf90fda2180f90f7d9d95/independence_wave_focus_tree.focus.json`.
- Read-only `hoi4.tech_inspect` returned `TECH_INSPECTED_PARTIAL`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3cfffcec59e6ef3ac6cc59c16ab3b66eaa9a19f63c95f5e7cdb89eb3b7e67b3a/4887ece220fc01e31917b7fda7592d88594c39fc48cdf94c5f673c6c8d2da1c6/technology-scan-ed5e591a4dcb.json`. A separate installed Technology Tree Viewer acceptance route is not available, so package-specific technology acceptance remains unresolved.

## Validation

- Read-only source review completed against the required offline wiki pages and installed vanilla documentation for country tags, country and state history, country and state scopes, `original_tag`, `has_character`, `is_core_of`, `is_in_array`, `capital_scope`, scripted effects, and country flags.
- The two new Clausewitz files have balanced braces, tab-indented script blocks, no unsupported `<=` or `>=` operators, and no unary variable negation.
- `python .tools/audit_event6_allocator.py` passed after the patch. The audit still reports IW-150 as non-admitted because this tranche does not add package admission or central registration.
- No live game launch, save/load test, map rewrite, event rewrite, focus rewrite, probability patch, or technology patch was performed.

## Remaining blockers and follow-up

- IW-150 still needs a source-cleared 1936 institutional and leader consumer.
- The neutral 1936 coalition flag or symbol remains unresolved. The traditional or Sultanate reconstruction may be used only on an explicitly owned later route, and PUSA names and symbols remain date-gated to 1939 or later.
- The complete IW-150 setup, final-validation, lifecycle cleanup, force, idea, decision, mission, focus, AI, localisation, portrait, flag, and asset surfaces remain unimplemented.
- A future owner may set `independence_wave_iw_150_institution_selected` only after those identity and source gates are accepted. Any future route must keep vanilla `indonesia_transfer_ATJ` as the owner of the normal Indonesian character transfer behavior.

No simplification was hidden. This is a preservation adapter only, not package admission or package completion.
