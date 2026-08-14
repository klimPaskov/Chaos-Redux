# IW-096 BIA compatibility adapter handoff

Status: package-local preservation scaffold landed; IW-096 remains fail-closed and unadmitted.

Date: 2026-08-14.

Owner: Chaos Redux country-package subagent.

## Scope and source authority

This tranche reviewed the required repository instructions, the Event 006, subagent, and focus-tree skills, the required offline Paradox wiki pages, and the installed HOI4 documentation for triggers, effects, script concepts, and dynamic variables.

Vanilla source review covered `common/country_tags/00_countries.txt`, `common/countries/Biafra.txt`, `history/countries/BIA - Biafra.txt`, `history/states/558-Nigeria.txt`, `history/states/900-Benue.txt`, and `common/characters/BIA.txt` under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

The installed vanilla BIA carrier is registered at `common/country_tags/00_countries.txt:265`, keeps `capital = 900`, cores state 900 in `history/states/900-Benue.txt`, recruits `BIA_akenzua_ii`, and uses the generic national focus tree. State 558 is the broad Nigeria/Lagos baseline with an ENG owner and NGA core; it is not a BIA core in the installed vanilla history.

The IW-096 research row still names state 558 as the public baseline and requires a Benin City location, but the current binding audit marks IW-096 `disabled_no_unique_current_state` and `unbound`. IW-107 is the distinct BIA package that is currently bound to state 900. The adapter therefore preserves both facts: future IW-096 release ownership/capital is exact state 558, while the registered vanilla BIA core witness is exact state 900. It does not assert a false BIA core on state 558.

## Country package coverage checklist

| Surface | Result | Evidence or remaining risk |
| --- | --- | --- |
| Tag registration and identity | PASS | `BIA` is a vanilla registered tag; IW-096 and IW-107 are distinguished only by exact package id plus future identity selector. |
| Event 006 origin and living-tag gate | PASS | The new context requires `original_tag = BIA`, `is_independence_wave_active_country = yes`, `independence_wave_active_origin`, and `liberation_origin = independence_wave`. The active-country trigger also excludes `independence_wave_origin_ended`. |
| State and core setup | PRESERVED/FAIL-CLOSED | Future IW-096 anchor contract is exact state 558 ownership, control, capital, and `independence_wave_anchor_state = 558`; vanilla BIA core 900 is a separate read-only witness. No state, owner, controller, capital, or core is mutated. |
| Vanilla history and leader | PASS | `BIA_akenzua_ii` and state 900 are observed, never recruited, removed, or rewritten. |
| Focus tree | PRESERVED | `has_focus_tree = generic_focus` is a read-only witness; no BIA-specific vanilla focus tree exists. |
| Politics, parties, advisors, military, industry, supply | PRESERVED | Vanilla BIA history remains the owner of starting politics, tech, equipment, and setup. No package-local changes were made. |
| Flags and assets | BLOCKED/UNTOUCHED | No flag files, portraits, icons, localisation, or manifests were changed. The effect only clears a future package-local selector marker after all gates pass. Akenzua II portrait provenance remains a separate unresolved asset gate. |
| AI/probability | NOT IN SCOPE | No AI weight, strategy factor, MTTH, random, or probability-bearing surface was changed. |

## Changed file surface

- `common/scripted_triggers/006_independence_wave_iw096_bia_compatibility_triggers.txt`
  - Added `is_independence_wave_iw_096_bia_compatibility_context`.
  - Added `has_independence_wave_iw_096_bia_release_anchor_surface` for exact post-release state 558 ownership/control/capital.
  - Added `has_independence_wave_iw_096_bia_vanilla_surface` for exact state 900 core, `BIA_akenzua_ii`, and `generic_focus` preservation.
  - Added `has_independence_wave_iw_096_bia_compatibility_contract` combining the gated witnesses.
- `common/scripted_effects/006_independence_wave_iw096_bia_compatibility_effects.txt`
  - Added `independence_wave_iw_096_bia_compatibility_clear_identity_selection`.
  - Added `independence_wave_cleanup_iw_096_bia_compatibility`.
  - Both effects are dormant and only clear `independence_wave_iw_096_benin_identity_selected` after the full contract passes.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw096_bia_compatibility_adapter_handoff_2026_08_14.md`
  - This durable handoff.

No central adapter, attestation, preflight, dispatch, Join, release list, registry constant, package loader, planner trigger, country history, state history, flag, portrait, localisation, workbook, or unrelated file was changed.

## Before and after behavior

Before this tranche, IW-096 had no package-local compatibility predicates or cleanup wrapper. BIA was shared by IW-096 and IW-107 only in static registry data, with IW-096 correctly fail-closed and no current-map loader.

After this tranche, a future named Benin route can prove the exact BIA/Event 006/IW-096 context, require the future state-558 release anchor, and verify that vanilla BIA core 900, Akenzua II, and generic focus content remain present. No current living BIA country is selected by tag membership, and no IW-107 route can satisfy the contract because `independence_wave_package_id` must equal `iw_096`.

The new adapter does not admit IW-096, add a core, transfer a state, change a capital, set the selector, set Event 006 origin, or alter vanilla BIA data.

## MCP evidence and validation

Read-only HOI4 MCP evidence was collected before reporting the surfaces:

- Map inspect for states 558 and 900 returned `MAP_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c014d7dcb5265d372103e28277d8b3b1957326a356520eadb48f5cf31817a1aa/309f2ef4180d16c6a12e99ad92175fe1c0f93ecce949ce1d30400ae32d58ba75/map-inspect.24bebf72ae84437c.json`.
- Read-only map render of the cores layer with coast, port, victory-point, building, supply, and railway overlays returned `MAP_RENDERED`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac06c21799b7b8f653abf2cad35425c5957f1fa23b5e21cf8dd4b0cafdc13d77/dbb1cfdd925d800008f2231c7d2c859df68ff4c1dafceab8a107ab2f6a1c5e1a/map-cores.png`.
- Event 006 root inspect for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0ee458714b0349c103ef7088bb4a904e81a331079391c1cfa7ebff7ca0ac6d0d/1e0dbdc95a8f9e1a741c340a65fa2b2658aef59b43608fc122c740e4a639bea3/event-lint-741883f50501.json`.
- Event 006 state render returned `EVENT_RENDERED_PARTIAL`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c45b71cf817504e42084be56108796beb71ebe3ba28dd67410832e0b60d3793b/6bc058d503fb05927c365ebff0dedbb2cc0501529e0560bacbbe1101adda922d/event-state-741883f50501.json`.
- Vanilla generic focus inspect/render returned `FOCUS_INSPECTED` and `FOCUS_RENDERED` for `generic_focus`; artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8889e91a86e48f788baf5fe65264e87941b721382a0296b08e1659731b921e4f/362a8a49e25160dd92c54b805889b4031817cea1cb3b3a658683b3533c445d6e/focus-inspect.5bb17398adee2259.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91bc6263fa7eee559506ba09892b304befe7d198ede6629452de81eca398dc6b/1a6a3f14141e9a20ad86bd9167838de3ac1d76c71bffafe850b5024529be5d89/generic_focus.focus.json`.
- Read-only technology traces were attempted for `infantry_weapons`, `tech_support`, `tech_trucks`, and `basic_train`, and a technology render was attempted for `infantry_weapons`. The installed route returned partial artifacts with helper projections deferred and `sourceAccurate = false`; the repository instruction that no complete Technology Tree Viewer proof is currently available remains unresolved. Useful partial render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1158c23323b03035cec6b56a73cb7602d8fa7d479c29caa6c923b1fe4ebd617d/6f48fcfb704fc5679eadc80c1b428353318fd24f012ad4690b05fb6fd2f4fa79/technology-technology-401f6921ad63.json`. No technology was changed.

Static validation after the patch confirmed the two new helper files contain the expected helper identifiers, exact package constant `constant:independence_wave_package_id.iw_096`, original-tag `BIA`, state 558 anchor, state 900 core witness, and no central-file edits. No live game or save validation was run, per repository policy.

## Remaining setup and identity risks

- IW-096 remains incomplete and must not be admitted until a unique current-map Benin City state is available and the central planner/attestation/preflight/Join owners add the exact package intentionally.
- The public baseline state 558 is currently too coarse for Benin City and remains occupied by the vanilla Nigeria state. Do not reinterpret state 558 as a BIA core without a source-backed map rebinding.
- IW-107 currently owns the BIA state-900 package boundary. The shared-carrier mutex and exact package-ID gates must remain unchanged when a future IW-096 route is promoted.
- Akenzua II portrait provenance and final asset acceptance remain unresolved and were intentionally left to the portrait/asset owners.
- The partial MCP Event, focus, and technology analyses defer large helper projections and report unrelated workspace diagnostics; the linked artifacts are evidence, not a clean whole-workspace runtime proof.

No plan handoff was written because this tranche was a bounded package-local adapter implementation. The next implementation owner must use this handoff as the source boundary before changing any central Event 006 admission surface.
