# Repo Explorer Handoff

> **Superseded source note (2026-08-15):** The POK anchor-hardening candidate described below was applied by the parent in commit `638fc2ebe`. The current contract in `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt` now requires `owns_state = 334` and `controls_state = 334` alongside the state-334 capital witness. This handoff remains historical exploration evidence; it does not identify a current gameplay gap.

## Scope read

- Parent task: inspect the current Event 006 source after the IW-050 Komi repairs and IW-048 Udmurtia package-local tranche, then identify one safe package-local source gap without widening central admission or inventing identity, flag, portrait, or rights decisions.
- Explicit constraints: read-only exploration, preserve concurrent worktree edits, do not edit gameplay, assets, localisation, spreadsheets, central dispatch, attestation, preflight, or deterministic Join, and write only this dated handoff.
- Files or IDs requested: current Event 006 source-of-truth and resume material, package dispatch and attestation, deterministic Join, the Join event callbacks, and candidate package-owned source surfaces.
- Skills and references read: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, and AI, plus the installed vanilla effects, triggers, and script-concept documentation.

## Primary findings

1. At the time of this read-only exploration, one narrow package-local hardening candidate was identified: the dormant IW-153 POK compatibility contract lacked ownership and control checks for the exact state-334 anchor. The parent subsequently applied that trigger-only repair in commit `638fc2ebe`, so this finding is closed in current source.
2. No source patch was applied by this exploration. The later parent repair changed only the dormant POK trigger contract and did not widen central admission.
3. IW-153 remains `specific_community_variant_only`, unbound, and fail-closed. The candidate hardening does not resolve the named Dayak institution, leader, portrait rights, symbol, host, or package-admission gates.
4. The current source-of-truth authority remains 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows. IW-050 KOM and IW-047 MEL remain absent from central adapter, attestation, preflight, and Join surfaces. The IW-048 UDM package in `451b91991` is package-local and was not duplicated.
5. The central Join order remains the exact 32-ID order recorded in the source-of-truth map. No safe reason was found to add KOM, MEL, UDM, POK, or any other unadmitted package to the central lists.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:5-23` | Current authority counts, deterministic Join order, adapter-only IDs, and explicit KOM/MEL package-local boundary. | The post-IW-045 override records 40 adapters, 32 attestations, 29 groups, 161 unattested rows, and the `3/4/5/7/10` ladder. |
| `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:154` | IW-153 design and binding row. | IW-153 is the Dayak federation, reuses `POK`, is `specific_community_variant_only`, remains unbound until a named Dayak polity is selected, and uses state 334 in `RG-BORNEO-DAYAK`. |
| `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:69` | Reservation and anchor contract. | `RG-BORNEO-DAYAK` names anchor 334 and requires the anchor to be unique with the host-remnant test preserved. |
| `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md:234-236` | Identity-reuse source of truth. | The spec requires IW-153 to reuse POK and preserve POK history, characters, cores, Indonesian releasable membership, and `indonesia_transfer_POK` behavior. |
| `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt:21-28` | Dormant POK/Event 006/package/selector context. | The context requires `original_tag = POK`, active Event 006 origin, `iw_153`, and the future named-community selector. |
| `common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt:43-71` | Historical candidate, now repaired. | The current strict contract checks state-334 ownership, control, capital, POK cores, the vanilla character, and Indonesian releasable membership. |
| `common/scripted_triggers/006_independence_wave_iw155_bli_compatibility_triggers.txt:29-36` | Closest sibling pattern. | The BLI anchor helper requires `owns_state`, `controls_state`, `capital_scope`, and the exact core before the strict contract can pass. |
| `common/scripted_triggers/006_independence_wave_iw167_chm_compatibility_triggers.txt:25-33` | Second sibling precedent. | The CHM anchor helper requires exact anchor ownership, control, capital, and core, with no central admission. |
| `common/scripted_effects/006_independence_wave_iw153_pok_compatibility_effects.txt:20-64` | POK cleanup ownership. | Cleanup only clears the future named-community selector under the current strict context. No effect needs widening for the anchor hardening candidate. |
| `common/scripted_effects/INS_scripted_effects.txt:45-70` (vanilla) | Vanilla transfer owner. | `indonesia_transfer_POK` remains the only owner of the Syarif Muhammad Alkadrie nationality and leader-role transfer. The Event 006 adapter must not duplicate it. |
| `history/countries/POK - Pontianak.txt:1,3` (vanilla) | POK history witness. | POK's vanilla capital is state 334 and its history recruits `INS_syarif_muhammad_alkadrie`. |
| `history/states/334-Kalimantan Barat.txt:17-18` and `history/states/1022 - Interior Borneo.txt:18-21` (vanilla) | Core and owner witnesses. | State 334 is an Indonesian state with a POK core, and state 1022 retains its POK core in the installed vanilla baseline. |
| `history/countries/INS - Indonesia.txt:271-279` (vanilla) | Releasable witness. | `INS_releasables` includes `POK` and the other Indonesian releasable tags. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-61,159-202,207+` | Central dispatch, content attestation, and preflight. | POK, KOM, MEL, and UDM are not present in the central runtime adapter or attestation authority in this scan. |
| `common/scripted_effects/006_independence_wave_join_effects.txt:211-248` | Deterministic Join authority. | The fixed probe order contains the 32 attested IDs only and has no IW-153, IW-047, IW-050, or IW-048 entry. |
| `events/006_independence_wave_join.txt:9-68` and `common/on_actions/006_independence_wave_join_on_actions.txt:10-25` | Join event and narrow callbacks. | The Join offer, accept, decline, failure, and retry chain is source-present, while on-war and state-control callbacks are scoped and do not provide a package-admission route for POK. |

## Existing patterns

The safe local pattern is a package-owned read-only anchor helper followed by a strict package contract. The helper checks the exact package context, state ownership, state control, capital state, and package core. The cleanup effect remains separately gated and idempotent. BLI and CHM are the closest current examples.

The POK adapter already preserves the important vanilla surfaces. It does not write history, cores, characters, flags, tags, releasable arrays, or transfer effects. Its only persistent mutation is clearing the future named-community selector after the complete context gate passes.

The historical source gap was limited to the missing ownership-and-control witness in the POK trigger file. The parent repair closes that local contract gap without requiring a new country, leader, portrait, flag, localisation key, focus route, decision, AI strategy, event, on action, dispatcher entry, attestation entry, preflight branch, scenario entry, or Join entry.

## Vanilla or reference precedents

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` was consulted for country events, random lists, event-target effects, and country-state effects.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` was consulted for scope and state predicates, including ownership, control, cores, and event-target checks.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` was consulted for script constants and scope-safe scripted logic.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, and the required event, decision, idea, AI, localisation, modifier, and on-action pages were read from the offline snapshot.
- No approved reference mod was needed. The existing Chaos Redux BLI and CHM compatibility helpers provide the closer structural precedent.
- The installed package has no Technology Tree Viewer. No technology acceptance claim is made for IW-153 or any candidate package.

## HOI4 MCP evidence

- Existing POK map inspection in `006_iw153_pok_compatibility_adapter_2026_08_14.md` returned `MAP_INSPECTED` for states 334 and 1022 with no selected-state unknown or missing geometry IDs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3cb63d1a0885e0a0cb0c79284f58d7e9cfaa9e85028b6016ff915c6a9a5a976e/b32e41894f24af09de1bb9ae0a2882ccfaa33c2f606bb0c5770c43a81d21f547/map-inspect.9ec611428b475849.json`.
- The same map artifact reports aggregate validation false because unrelated workspace `map/buildings.txt` locator and port diagnostics exceeded the diagnostic ceiling. It does not expose core-membership semantics, so the installed vanilla state-history files remain authoritative for the POK core witness.
- A fresh bounded `hoi4.map_inspect` and `hoi4.map_render` rerun was attempted for the same POK states and owner-layer evidence, but the tool calls did not return within the bounded wait and were terminated. No new render artifact or clean aggregate map claim is made. This is an MCP availability limitation, not evidence for a gameplay patch.
- Current Join event inspection returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, with broad workspace helper/lifecycle projection deferred. Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/309f35ec9f35ccdf591cf4964d7f721c52fa533e3098c5cce9c0c6c1429bdfbc/d1dbbd39cf6203251ef3a5224b6a8863329ccb8209ad4b9390c0153d10d67ffa/event-trace-741883f50501.json`.
- Current Join event render returned `EVENT_RENDERED_PARTIAL` with five selected nodes, 41,149 omitted nodes, and 14 broad blocking diagnostics. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31a3c34afd70064adaf906d27f7f9ed360862d756ee7d083b5e2a0f3e822eb41/d37ff2771007302bac4f8cee6fc55f8983d558945874e909d293dd60246290ed/event-options-741883f50501.json`.
- The POK compatibility files add no event, focus, GUI, technology, or weighted surface, so no probability inspection or focus inspection is required for the proposed trigger-only hardening. Existing KUB and TAT strategy inspections report `no_weighted_surfaces`, while KOM mission inspection reports 11 candidates with 15 required inputs and `poolComplete=false`. Those results do not authorize a balance or AI patch.

## Likely edit order for the parent

1. Treat the POK anchor-witness finding as closed by parent commit `638fc2ebe`; the current trigger contract is the source of truth.
2. Leave `common/scripted_effects/006_independence_wave_iw153_pok_compatibility_effects.txt` unchanged. Its selector cleanup already calls the strict context and does not need a new mutation.
3. Do not widen central admission, attestation, preflight, scenario, dispatcher, or Join surfaces from this historical hardening.
4. Do not edit central adapter, attestation, normal/scenario preflight, scenario, dispatcher, Join, event, on-action, country history, state history, characters, flags, portraits, localisation, focus, decisions, AI, assets, or workbook files in this tranche.
5. Rerun the bounded map inspect and map render for states 334 and 1022. If the map route remains unavailable, record the exact timeout and retain the existing artifact as bounded evidence only.
6. Run package-local syntax checks and the standard Event 006 allocator, tag, flag, country API, and SCN-008 checks without changing their authority inputs. Because no weighted source changes, do not claim a probability delta.
7. Only after a separate identity, rights, symbol, host, complete package, and typed-probability packet is accepted should a future owner consider any IW-153 caller or central admission. This scan does not authorize that work.

## Validation checks

- Confirm the POK trigger diff contains only the new package-local anchor witness and its strict-contract call.
- Confirm `rg -n "iw_153|POK|owns_state|controls_state|capital_scope|is_core_of" common/scripted_triggers/006_independence_wave_iw153_pok_compatibility_triggers.txt` reports the exact context, anchor, core, and contract identifiers.
- Confirm no new `IW-153`, `iw_153`, or POK entry appears in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` or `common/scripted_effects/006_independence_wave_join_effects.txt`.
- Re-run the state-334/state-1022 map inspect and owner-layer render, preserving selected-state evidence separately from unrelated aggregate map diagnostics.
- Re-run the scoped Event 006 Join inspect and render after any event-source change. No event-source change is expected for this candidate.
- Run `.tools/audit_event6_allocator.py`, `.tools/audit_event6_scenario_matrix.py`, `.tools/audit_event6_flags.py`, and `.tools/audit_event6_country_api.py` only after an owner applies the source repair. These checks must continue to report the same central authority counts and no new admission ID.
- Route any future weighted mission or AI work through `chaosx_ai_probability_auditor`, starting with `hoi4.probability_inspect` and using the same named scenarios for `hoi4.probability_compare`. Do not infer a quantitative result from the incomplete KOM or empty KUB/TAT strategy surfaces.

## Risks and blockers

### Confirmed blockers

- IW-153 has no accepted named Dayak institution or exact community territory beyond the state-334 research anchor. The selector remains future-only and unset.
- IW-153 has unresolved period leader, portrait/source-rights, and symbol/flag gates. No identity or asset decision can be inferred from POK reuse.
- IW-153 remains unbound and absent from central adapter, attestation, normal/scenario preflight, and deterministic Join. The proposed helper must remain dormant.
- The current map rerun did not return within the bounded tool wait, so no fresh map render artifact is available. The prior selected-state map artifact is bounded evidence only and aggregate validation remains false because of unrelated workspace diagnostics.
- The current Event MCP view is partial because workspace-wide helper and lifecycle projections are deferred. It is not live runtime or save/load evidence.
- The detailed probability auditor route is not available in this subagent turn. No weighted source patch or quantitative claim is made.

### Ordinary risks

- A future named-community route may intentionally use a temporary occupation or controlled-remnant sequence. The parent should confirm that the strict package admission contract requires simultaneous ownership and control before applying this hardening.
- The worktree contains extensive unrelated concurrent changes and untracked files, including the already committed UDM package-local tranche. Preserve those changes and review any overlapping diff before applying an owner patch.
- Older Event 006 handoffs retain superseded 14, 20, 27, 31, or 39-package counts. Use the post-IW-045 authority only.

## Recommended next action

The POK anchor ownership/control hardening is already applied and should remain dormant. Keep every central list unchanged.

If that anchor interpretation is not accepted, the correct disposition is no safe Event 006 gameplay patch after the KOM and UDM package-local work. The next work should remain evidence-only package admission research, with identity/rights, symbol, host, complete mechanics, and typed probability gates resolved before any central edit.

This handoff reports a candidate source gap and does not claim gameplay implementation, package admission, Join promotion, live runtime validation, or whole-event completion.
