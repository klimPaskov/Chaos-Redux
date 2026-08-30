# Event 006 next safe package patch audit: IW-013/NAV

Date: 2026-08-30.

Owner: Chaos Redux country-package audit worker.

Scope: Event 006 Independence Wave package-local and admitted-country surfaces for IW-013 Basque Country using the current source-of-truth map, resume packet, candidate registry, installed binding, package manifest, event/focus sources, and vanilla HOI4 references.

## Verdict

No gameplay, localisation, asset, map, admission, attestation, fallback, or pre-event-visibility patch is safe in this tranche.

Exactly one concrete audit finding is recorded: IW-013 has a state-anchor authority conflict between its baseline candidate/research rows and its accepted installed/runtime binding.

The runtime package source already follows the accepted installed binding by using state 792, so changing the package source to state 172 would be an identity and reservation redesign rather than a typo fix.

The package remains fail-closed at central attestation/admission gates and is not promoted by this audit.

## Single finding: IW-013 anchor authority conflict

| Surface | Evidence | Current value |
| --- | --- | --- |
| Candidate registry | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:14` | Baseline state 172, described as the compact Basque anchor, reservation group `RG-172`. |
| Research resolution | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:14` | Repeats baseline state 172 and `RG-172`. |
| Installed binding | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:14` | `fixed_anchor_compact` state 792 (`País Vasco`), optional extensions `172|806`, installed cores `792|172|806`, baseline traceability retained as 172. |
| Current source-of-truth override | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:531` | Explicitly states that NAV uses installed-map compact País Vasco anchor 792, with 172 and 806 retained only as optional extension objectives. |
| Runtime package trigger | `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:33-50` | Requires package metadata, anchor target state 792, state 792 as capital, and the vanilla NAV leader. |
| Runtime package setup | `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:153-194` | Prepares IW-013 around state 792 and validates `792 = { is_capital = yes }`. |
| Reservation registry | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:586-595` | Reserves 792 as the anchor and 172/806 as optional extensions under `rg_172`. |
| FORM-07 registry | `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:826-828`; `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:34-38` | Uses 792 as the installed compact Basque anchor; 172/806 remain optional. |
| Shared constant | `common/script_constants/006_independence_wave_constants_registry.txt:3877-3879` | `basque_anchor_state = 792`. |

Vanilla evidence makes the distinction material rather than cosmetic.

`C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\NAV - Navarra.txt` sets `capital = 792`.

Vanilla state history identifies state 792 as Basque Country with Bilbao, steel, a civilian factory, an arms factory, naval base, and air base, while state 172 is Navarre and state 806 is French Basque Country.

The installed binding therefore matches the vanilla NAV capital and the current package/formable design, while the registry/research 172 value is a stale or unresolved baseline reference that must be reconciled by the design authority.

### Why this is not a safe local source patch

Changing `792` to `172` in package gameplay would change NAV's accepted capital, host-remnant behavior, reservation semantics, FORM-07 qualification, compact-versus-extension ordering, and state-transfer/release outcomes.

Changing only the candidate and research rows would alter design-authority records outside this country-package ownership and would leave the package binding, constants, triggers, effects, and formable registry contradictory.

The safe action is one parent-owned atomic authority reconciliation across the candidate row, research row, installed binding, source-of-truth map/resume packet, and any dependent documentation, followed by the normal package and event gates.

## Country-package coverage checklist

| Surface | Audit result | Evidence and disposition |
| --- | --- | --- |
| Tag registration and carrier | Covered; no patch | IW-013 intentionally reuses vanilla `NAV`; `common/country_tags/006_independence_wave_countries.txt` does not create a replacement tag. Dispatch recognizes `iw_013` and NAV, while central attestation remains fail-closed. |
| States, ownership, cores, capital, and map | Covered; no patch | Runtime compact anchor is 792 with optional 172/806; vanilla NAV capital is 792. Read-only map inspect/render for states 172, 792, and 806 completed successfully. No map rewrite was attempted. |
| Host and release safety | Covered; no patch | Installed binding records SPR as the surviving host for the compact set and FRA/SPR ownership evidence for the three states; vanilla SPR capital is 41 and FRA capital is 16. No transfer or release behavior was changed. |
| Politics, parties, laws, and ideas | Covered; no patch | IW-013 setup in `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:428-470` normalizes the intended democratic package state, party names, popularity, ideas, cosmetic identity, route framework, and lifecycle. No missing package-local identifier was evidenced. |
| Leaders, characters, and portraits | Covered; no patch | Vanilla NAV leader Ramón Ormazábal Tife remains the package leader; `NAV_independence_wave_jose_antonio_aguirre` is an additive corps commander in `common/characters/006_independence_wave_characters_registry.txt:249-262` and recruitment registry lines 188-191. Existing DDS/GFX wiring is stable. The current portrait audit records `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` rights status; no portrait or leader invention is authorized here. |
| Flags and cosmetic names | Covered; no patch | Existing NAV cosmetic route names and flag-family wiring are present; alternate-history flag provenance/rights remains an admission gate. No flag asset or localisation change is justified by the anchor conflict. |
| Focus tree | Covered; no patch | Shared `independence_wave_focus_tree` inspection/render passed with 184 focuses, 195 connectors, zero layout diagnostics; only an unrelated vanilla localisation warning was reported. No package-local focus defect was established. |
| Decisions, ideas, and event-owned assets | Covered; no patch | IW-013 regional decisions, ideas, event entry, and package assets are wired through the existing regional registries. No package-owned GUI or new event visual asset is in scope, so no shared UI or asset change was made. |
| Military, technology, industry, supply, and production | Covered; no patch | IW-013 uses the existing force mapping and p13 starting-force route; state 792's vanilla industrial/naval facilities support the accepted compact anchor. No custom technology surface is owned by IW-013. Technology inspection/render was blocked by `SCAN_BYTE_LIMIT`, and the installed package exposes no Technology Tree Viewer. |
| AI and playability | Covered with limitation; no patch | Existing package AI strategy and preparation weight are wired. Read-only probability source inspection found zero adapter-backed candidates; the required `chaosx_ai_probability_auditor` route is unavailable in this environment, so no quantitative AI/probability claim or weight patch was made. |

## File-surface checklist

The inspected package surfaces are `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`, `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`, `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`, `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`, `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`, `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt`, `common/script_constants/006_independence_wave_constants_registry.txt`, `common/characters/006_independence_wave_characters_registry.txt`, `history/general/006_independence_wave_character_recruitment_registry.txt`, `localisation/english/006_independence_wave_iberian_l_english.yml`, `interface/006_independence_wave_portraits_registry.gfx`, and `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds`.

No stale package-local tag, focus, decision, idea, localisation, portrait path, flag path, leader id, or formable id was found that could be corrected independently of the 172-versus-792 authority decision.

No gameplay or matching localisation/asset file was changed in this handoff.

## MCP evidence and limitations

- Map inspect: `MAP_INSPECTED`, status `ok`, states 172/792/806 selected, revision `b7b2aed87ddd4e30ac1e8856eaec1edd5ec05acadd0d0c3b928a798b9ae06c16`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9235fe08cad5c7628d569786c28537dda6193e84056273b820b2126f1571178/ad452f28671cf2507d0b5da7b0fec75811841b6cd9562b24a44086ea0fd8429b/map-inspect.b7b2aed87ddd4e30.json`.
- Map render: `MAP_RENDERED`, status `ok`, owner layer with coastlines, ports, victory points, resources, state buildings, supply nodes, and railways; validation passed; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ad1da38e5d6e5aaf4fc6f4c86817a2e5e5a064029f78c1a5b993fe0f0fa60e1/46f411cd3c97e5e69ae80ae22471a667aa82225ebc2d1c32203aee9d74a1aa3c/map-owner.png`.
- Focus inspect/render: `FOCUS_INSPECTED` and `FOCUS_RENDERED`, status `ok`, 184 focuses and 195 connectors, zero layout diagnostics; inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21005c148e3896ec6794954a7b3330cbbe53b882413308a49c5ed9c21299d9a6/e68ddc7a032294af2eda5ec74ae368e4c74af3e25df848e3ee105457cc4d6154/focus-inspect.8d8b7b758947f6db.json`.
- Event inspect/render: focused `hoi4_event_inspect` returned exact MCP `INTERNAL_ERROR Unexpected internal error`; read-only event render returned `EVENT_RENDERED_PARTIAL` with helper/lifecycle analysis deferred, 4 blocking diagnostics in a graph containing broad unresolved vanilla/deferred nodes; no scoped IW-013 source error was identified. This is a tool limitation, not a basis for a gameplay patch.
- Probability: `PROBABILITY_SOURCE_INSPECTED`, status `ok`, source `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, zero candidates/available candidates; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4059741f2f9e4e4a9545d68b8a7df565b55a680cc5f52bfd22e1a7f0e5dce30a/3d0080d84d9f9d1bf82190db8867d25c28708200d84ff58ff4faf99a1f6328de/probability-inspect-c9a81863c89a.json`. The mandatory custom `chaosx_ai_probability_auditor` route is not callable here, so no sweep or compare was claimed.
- Technology inspect/render: both returned exact MCP `SCAN_BYTE_LIMIT` (“Scan exceeds configured byte limit”). No Technology Tree Viewer is installed, so technology evidence remains unresolved and no technology patch was attempted.

No map write was attempted; therefore no map rollback or recovery evidence applies.

## Focused validation

The following task-specific validators passed on 2026-08-30:

- `python -B .tools/audit_event6_allocator.py`: 149 publishers, 126 automatic/high-chaos selectable, 40 runtime adapters, 32 attested packages, 29 reservation groups, and the expected eight adapter-only fail-closed IDs including IW-013.
- `python -B .tools/audit_event6_country_api.py`: 242 unique broad tags, 191 resolved carriers, zero missing carriers, zero duplicate tags, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict`: 102 registered Event 006 tags and 102 complete flag families.
- `python -B .tools/audit_event6_scenario_matrix.py`: all 32 SCN-008 cells and 8 edge cases passed.

Live HOI4 execution and save testing were not run because repository policy assigns live consumer validation to the user.

## Disposition and parent follow-up

Keep IW-013 source/runtime behavior on state 792 until the parent resolves the baseline-versus-installed authority conflict atomically.

The parent should update the candidate registry, research resolution, installed binding traceability, source-of-truth map, resume packet, and any dependent package documentation in one design-authority change, then rerun the map, package, event, probability, portrait/rights, and admission gates.

Do not change central attestation, admission, fallback, pre-event visibility, reservation-group identity, or package promotion as part of this local audit.

## Simplifications, omissions, and blockers

No gameplay patch was made, so there are no source or localisation simplifications to report.

The unresolved 172-versus-792 conflict is intentionally left for parent design-authority reconciliation.

Existing independent blockers remain unchanged: central attestation/admission is fail-closed for the adapter-only package, the current NAV Aguirre portrait rights status is `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW`, the event MCP inspect route fails internally, the typed probability-auditor route is unavailable, and technology inspection is byte-limited with no Technology Tree Viewer.

These blockers do not justify promoting IW-013 or changing its package identity.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui` for the required audit and ownership rules.
