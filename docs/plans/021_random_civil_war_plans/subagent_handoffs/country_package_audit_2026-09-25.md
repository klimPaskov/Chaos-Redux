# Event 021 Country Package Audit Handoff — 2026-09-25

Disposition: HOLD / PARTIAL. This is a source-backed country-package audit, not a completion certificate. No HOI4 process was launched. No gameplay, asset, or pre-existing documentation file was edited. This handoff is the only intended write from this audit; nothing was staged or committed.

## Scope and source-of-truth note

The audit is limited to the 32 Event 006 identities currently admitted by Event 021, their package setup and runtime consumers, the Event 021 parent/actor adapter, package map anchors, identity uniqueness, origin isolation, and abort/terminal cleanup.

The requested Event 021 matrix path, docs/specs/021_random_civil_war_specs/021_random_civil_war_country_package_matrix.md, currently defines actor-family contracts and gates but does not enumerate 32 package rows. The executable 32-row crosswalk comes from common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:15-47, paired carrier mapping at :59-90, and common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt:8 onward. I reconciled those rows to docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv and docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv. Treat the absent 021 identity table as a documentation/source-of-truth gap, not as evidence that the 32-row set is unknown.

The Event 021 source specification requires a complete human Event 006 package, distinct Event 021 origin, preserved package identity/content, viable host remnant, and no Event 006 firing/evolution/weight/cap or league mutation (Part 7, plus the country matrix). Event 006 Part 5 and Part 7 define the shared generic focus framework, package-specific setup, leader, politics, force, AI, asset, and readiness obligations. Event 006 remains HOLD / PARTIAL in its current source-of-truth map.

## Coverage checklist

- Exact scope count: 32 package IDs, 32 unique carrier tags, 32 unique current primary anchor IDs; the strict Event 006 allocator and country-API audits pass.
- Human/fail-closed gate: Event 021 candidates require a normal human host; package actors and completed adapters also pass the shared actual-nonhuman exclusion. No admitted carrier is an actual nonhuman identity in the current crosswalk.
- Tag and character uniqueness: no duplicate carrier IDs or current anchor collisions in the admitted crosswalk. The read-only character scan found zero duplicate top-level mod character IDs and zero collisions with installed Vanilla character IDs; this does not prove live roster ownership for every route.
- Package completeness: the Event 021 proof requires Event 006 package setup, command roster, force mapping and application, a full framework or additive focus assignment, the generic focus contract, the generic AI profile, valid anchor/former-host targets, a current-generation force package, and a package-specific prepared predicate.
- Focus, decisions and AI: the shared Event 006 tree/overlay and package-owned content are source-wired behind the Event 021 package/player-surface gate. Weighted AI behavior is not accepted by this audit; the required specialist pass has not returned.
- Event 006 origin isolation: source path uses package-only preparation and Event 021 receipts. The strict Event 006 active-origin classifier, normal activation/commit, history, network/league registration, released-package history, and evolution delivery are not called by the Event 021 adapter path.
- Force, reinforcement and technology: source proof includes current-generation force setup; Event 006 force effects inherit host technology and then apply the package force profile. No per-package technology tree was found. Equipment, manpower, production, supply and reinforcement behavior remain unverified in a campaign.
- Formables: the package content is present behind family/route readiness, but FORM-07, FORM-08 and FORM-48 remain fail-closed or unavailable; details appear below.
- Map/capital safety: one primary-anchor path does not fail closed on a current host capital or protected/reserved state. Its abort path restores ownership/controller but has no explicit capital restoration. These are actionable source-level risks, not demonstrated live failures.
- Cleanup: the earlier generation-reset omission is repaired in current source; the separate capital-restoration question and live rollback/relaunch proof remain open.
- Weighted logic: unresolved pending specialist output. No substitute source-only probability conclusion is claimed.

## Exact 32-row crosswalk and row exceptions

Names, carrier tags and primary anchors below are from the current candidate registry and current installed-map binding crosswalk, reconciled to the Event 021 adapter. The flag notes are copied from the specialized 2026-09-25 flag handoff and are not a second visual review. A missing direct Vanilla basename is reported as a runtime lookup uncertainty; engine fallback is not assumed. “No additional row issue found” is limited to this source audit and does not certify the package in-game.

| ID | Package / carrier | Primary anchor | Per-row exception or review note |
| --- | --- | ---: | --- |
| IW-001 | Scotland / SCO | 121 | Current split binding is expanded; adapter anchor remains 121. Vanilla SCO.tga is absent; other direct ideology variants exist. |
| IW-002 | Wales / WLS | 122 | Vanilla WLS.tga is absent; other direct ideology variants exist. |
| IW-004 | Brittany / BRI | 14 | Vanilla BRI_democratic.tga is absent. |
| IW-006 | Wallonia / AFX | 34 | Mod ideology aliases are under the existing user-review/provenance gate; no new asset or fallback is authorized. |
| IW-007 | Frisia / AGX | 36 | Mod ideology aliases remain under the existing user-review/provenance gate. |
| IW-008 | Rhineland / RHI | 51 | Shares reservation group RG-RHINE-SAAR with IW-010; strict allocator confirms pair capacity 2. Vanilla RHI.tga is absent. |
| IW-009 | Bavaria / BAY | 52 | Candidate compact group is broader than the adapter’s single primary anchor. Vanilla BAY.tga is absent. |
| IW-010 | Saar / AJX | 42 | Shares RG-RHINE-SAAR with IW-008; strict allocator confirms pair capacity 2. Mod ideology aliases remain under the existing review gate. |
| IW-012 | Icelandic emergency republic / ICE | 100 | The inherited ICE_personal_union cosmetic lookup has no base or ideology flag files, including the selected democratic basename; neither setup path explicitly drops/sets that cosmetic tag. Engine fallback is unknown. Vanilla ICE_democratic.tga is also absent. The vanilla single-state host is excluded by Event 021’s greater-than-one controlled-state gate, but this does not resolve other-host or future-map use. |
| IW-014 | Catalonia / CAT | 165 | Vanilla CAT_democratic.tga and CAT_neutrality.tga are absent. FORM-07 identity/formable access remains blocked. |
| IW-017 | Corsica / COR | 1 | Vanilla COR_neutrality.tga is absent. |
| IW-018 | Sardinia / ARX | 114 | Existing portrait wiring maps ARX_gavino_piras to Vittorio Vernè’s portrait; the portrait handoff leaves this identity mismatch for review. Generated-flag output rights are also unresolved. |
| IW-019 | Sicily / ASX | 115 | Existing flag-source obligations and generated-output rights remain separate unresolved asset records. |
| IW-023 | Transylvania / TRA | 84 | Vanilla TRA_democratic.tga is absent; the HUN_EMPIRE democratic variant used by the gated FORM-08 route is also absent. FORM-08 remains unavailable. |
| IW-024 | Banat / AXX | 82 | Current binding is expanded; optional state 764 overlaps the excluded IW-025 optional extension, not this primary anchor. The prior source PNG/manifest handoff is absent from the current tree; preserve its existing runtime TGA and do not infer provenance. FORM-08 remains unavailable. |
| IW-026 | Macedonia / MAC | 106 | Current binding is expanded. Vanilla MAC.tga is absent. |
| IW-027 | Thrace / BAX | 184 | Existing flag provenance/source package remains under user review. |
| IW-028 | Epirus / BBX | 185 | Existing source attribution/date/licence and BLX source package remain under user review. |
| IW-029 | Bosnia / BOS | 104 | Current binding is expanded. Vanilla BOS.tga is absent. |
| IW-030 | Montenegro / MNT | 105 | Vanilla MNT_democratic.tga is absent. |
| IW-031 | Kosovo / KOS | 802 | This is a new current-state binding relative to the candidate matrix’s blank baseline anchor; the current country-API audit reports IW-031-crosswalk=pass. Keep state 802 as the current binding. |
| IW-033 | Karelia / KAR | 146 | Current binding is expanded. Vanilla KAR.tga is absent. |
| IW-038 | Ruthenia / RUT | 73 | The direct RUT ideology variants for communism, democracy, fascism and neutrality are absent; do not assert fallback. |
| IW-040 | Kuban Cossack Host / KUB | 234 | Vanilla KUB_democratic.tga is absent. The portrait handoff reports the declared Ivanis large portrait texture absent from the installed DLC tree. |
| IW-041 | Crimean Tatar state / CRI | 137 | Vanilla CRI.tga is absent. |
| IW-044 | Tatarstan / TAT | 249 | Vanilla TAT.tga is absent. |
| IW-045 | Bashkiria / BSK | 651 | Vanilla BSK.tga is absent; existing route/provenance status remains under the specialized flag handoff’s review boundary. |
| IW-070 | Armenia / ARM | 230 | Vanilla ARM_democratic.tga and the inspected Transcaucasus-unified formable basename are absent; no fallback is assumed. |
| IW-071 | Georgia / GEO | 231 | Vanilla GEO_neutrality.tga and the inspected Transcaucasus-unified formable basename are absent; no fallback is assumed. |
| IW-072 | Azerbaijan / AZR | 229 | Vanilla AZR.tga and the inspected Transcaucasus-unified formable basename are absent; no fallback is assumed. |
| IW-173 | Hawaii / HAW | 629 | Current binding is expanded. Vanilla HAW_democratic.tga is absent. Portrait runtime pixels match an archived ImageGen repaint candidate for Samuel Wilder King and require user review. FORM-48 is unreachable while IW-179/FSM remains fail-closed. |
| IW-184 | California / HBX | 378 | Portrait runtime pixels match an archived ImageGen repaint candidate for William D. Stephens and require user review. FORM-48 is unreachable while IW-179/FSM remains fail-closed. |

The exact three-size paths, route/formable cosmetic consumers, source/rights details and per-portrait statuses are retained in event021_event006_flag_asset_audit_2026-09-25.md/.json and event021_event006_portrait_asset_audit_2026-09-25.md/.json. This audit does not re-grade image quality or assert a missing-suffix fallback.

## File-surface checklist and current source anchors

| Surface | Current evidence | Result / limitation |
| --- | --- | --- |
| Event 021 admitted IDs | common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt:15-48 | Exactly 32 package IDs in the dedicated array. Carrier capture/release branches are at :59-128. |
| Carrier/anchor readiness | common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt:8 onward | Static 32 state/tag branches require host ownership/control, population, infrastructure, and dormant carrier. This trigger does not require the anchor to be non-capital or unreserved/protected. |
| Parent package selection | common/scripted_effects/021_random_civil_war_parent_effects.txt:152-225 | Iterates the ordered complete-package array and accepts the first candidate that passes. It is deterministic first-match, not a random draw among valid Event 006 packages; failure does not continue to the next eligible row. |
| Host admission | common/scripted_triggers/021_random_civil_war_parent_triggers.txt:44-62 | Normal-human host, no terminal/incompatible/active/reserved condition, generation allowed, more than one controlled state, and at least one dormant package. |
| Complete content proof | common/scripted_triggers/021_random_civil_war_parent_triggers.txt:67-145 | Requires setup, command roster, force mapping/application, full or additive focus assignment, generic focus contract, generic AI profile, anchor/former-host targets, current-generation force package, no Event 006 active/network/league membership, and package-specific readiness. Static proof is not an engine materialization test. |
| Event 006 player surface | common/scripted_triggers/006_independence_wave_triggers.txt:21-88 and common/scripted_triggers/021_random_civil_war_triggers.txt:21-33 | A complete normal-human Event 021 package can use Event 006 local content without satisfying the normal active-origin classifier. |
| Event 006 package preparation | common/scripted_effects/006_independence_wave_effects.txt:703-868 and :3731 onward | Shared setup writes package-local values/content. Adapter preparation is explicitly separate from normal activation. |
| Lifecycle separation | common/scripted_effects/006_independence_wave_effects.txt:858-942; common/scripted_effects/021_random_civil_war_parent_effects.txt:3840-3929 | Normal Event 006 activation/commit registers active/network/league and writes history/evolution. Event 021 calls the package-only prepare entry, then writes Event 021 origin receipts; no normal Event 006 activation/commit or chaosx.nr6.1 reference occurs in the inspected Event 021 path. |
| Focus/AI/force validation | common/scripted_triggers/021_random_civil_war_parent_triggers.txt:67-132; common/national_focus/006_independence_wave_focus.txt; common/scripted_effects/006_independence_wave_force_effects.txt | Shared generic Event 006 tree plus reviewed additive carrier overlay is the accepted design; package setup rejects missing focus/AI/force proof. Event 006 force setup inherits former-host technology and applies minimum research slots. No package-specific technology-tree route was found. |
| Formables and decisions | common/decisions/006_independence_wave_decisions.txt and common/scripted_effects/006_independence_wave_formable_registry_effects.txt; docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:1-9 | Package gate permits local Event 006 surfaces; family-specific readiness remains separate. IW-179/FSM is still fail-closed, leaving FORM-48 unreachable to HAW/HBX. FORM-07/FORM-08 also remain non-available/readiness-controlled. |
| Statehood Ledger GUI | common/scripted_guis/006_independence_wave_scripted_gui.txt:10-14 | The shared status GUI is visible only for is_independence_wave_active_country. Event 021 packages deliberately are not active Event 006 origins, so this inherited status window stays hidden even while local focus/decision content is admitted. Event 021 specs do not authorize a new custom GUI; parent must decide whether the surface is intentionally omitted or needs an accepted gate change. |
| Force/production/supply/technology | common/scripted_effects/006_independence_wave_force_effects.txt and package setup dispatch | Source contains dynamic package force profiles and reinforcement routes; this audit does not prove stockpiles, manpower, industry, production, rail, supply or division viability after runtime setup. |
| Event 021 terminal cleanup | common/scripted_effects/021_random_civil_war_parent_effects.txt:7111-7296 | Finalizer preserves the complete Event 006 carrier and origin receipt while closing Event 021 front/mission/idea state. Source wiring exists; terminal execution and save/load are unverified. |

### Actionable source findings

1. Primary-anchor capital/protected-state gap. The ordinary Event 006 allocator gate in common/scripted_triggers/006_independence_wave_package_triggers.txt:9-17 excludes current reserved and protected states. The Event 021 adapter registry trigger does not reuse that gate. In event021_parent_find_event6_package, common/scripted_effects/021_random_civil_war_parent_effects.txt:190-198, the capital/reserved/front/scenario exclusions are behind an OR whose first branch is true whenever random_civil_war_event6_secondary_search_active is absent. That flag is set for the secondary search, not for the primary path. Thus the primary path can accept an anchor that is the host’s current capital or otherwise protected/reserved. The parent then transfers that state and makes it the Event 006 actor’s capital at :4362-4367. The Event 021 Part 7 host-remnant contract forbids taking the protected remnant. This is source-proven permissiveness, not evidence that a live campaign has hit the case.

2. Abort capital restoration is not explicit. event021_parent_abort_event6_opening and event021_parent_abort_event6_secondary_front return anchor owner/controller to the host and clear package transaction state, but neither contains an explicit host-capital restoration. The same setup sets the carrier capital to the selected anchor. Current generation cleanup does not establish prior host/carrier capital restoration. Treat that as a rollback-safety uncertainty requiring source correction or scenario evidence, not as a proven live corruption.

3. Planned footprint versus materialized footprint requires a map receipt. Event 021 adapter setup initially records anchor territory level and can raise it to compact/extended according to planned state count. The Event 021 Event 006 opening branch has an explicit owner/controller transfer for the selected anchor at :4362-4365. Shared Event 006 setup is documented as country-local reversible preparation at common/scripted_effects/006_independence_wave_effects.txt:690 onward. For an already-existing empty carrier, the inspected Event 021 branch does not explicitly transfer every compact/extended planned state. For an absent carrier, the static release effect may have engine-mediated core-state consequences not established by this source audit. Therefore current source does not prove the actual starting footprint for both carrier-existence paths; verify exact ownership and capital for each path before accepting compact/extended package tiers.

4. Deterministic candidate order is a variety decision. The complete-package array is traversed in static registry order and stops at the first eligible row. When multiple Event 006 packages fit a host, lower-index packages win. No country-package random draw appears in this helper. The required archetype/package probability review may determine whether this is intended; do not describe this path as randomly selecting among valid packages.

5. Package surface gaps are inherited, not new package admissions. FORM-48 remains unreachable until IW-179/FSM is admitted; the current matrix excludes IW-179 and the parent did not authorize expanding the 32. FORM-07 and FORM-08 are separately readiness-controlled/unavailable. The 021 package origin gate does not bypass these formable checks.

6. The shared Statehood Ledger GUI is an Event 006 active-origin-only surface. It is hidden for Event 021-origin packages by design of the lifecycle classifier, although local package decisions and focus content are enabled. The current accepted Event 021 spec excludes a new scripted GUI. Record this as a package-facing feature gap for parent resolution, not as authorization to create a GUI.

## Origin receipts, no Event 006 mutation, rollback and cleanup

event021_parent_prepare_event6_adapter_actor stores the prior Event 021 generation, sets an adapter-only setup window, supplies Event 021 values to shared package setup, and calls independence_wave_prepare_event021_adapter_origin. On package proof, it calls event021_record_event6_origin and event021_apply_event6_origin_adapter, then clears the reversible Event 006 prepared flag.

The origin record uses Event 021-only flags/variables for origin kind, date and generation. is_independence_wave_event021_package_country requires a normal human carrier, package/setup/origin receipts and a package ID, while explicitly excluding independence_wave_active_origin and origin-ended states.

The package proof excludes independence_wave_active_origin, independence_wave_network_member and independence_wave_league_member. The Event 021 source path contains no reference to the normal Event 006 root chaosx.nr6.1, activate_prepared_country_origin, commit_prepared_country_origin, register_network_member or register_league_member. This supports the no-fire, no-normal-evolution/history, no automatic network/league enrollment contract at source level. No campaign state dump proves counters/weights/caps in runtime.

Abort behavior now calls event021_parent_cleanup_failed_event6_adapter_actor, which runs independence_wave_reset_current_generation when setup was attempted, restores the actor’s prior Event 021 generation if saved, and clears adapter/package variables before a newly released actor is annexed. Abort also restores the selected anchor’s owner/controller. A pre-existing dormant carrier is preserved. Transaction cleanup clears pending primary/secondary package values and temporary Event 021 event targets. Terminal Event 021 cleanup finalizes the adapter actor without annexing it or calling Event 006 origin-ended cleanup.

Open rollback items are explicit capital restoration, possible footprint mismatch, and engine/save-load execution. No branch-level test proves a failed setup, a failed war declaration after capital change, a successful postwar finalization, or a reload.

## Specialized checks and MCP evidence

Read-only task-specific checks on the current checkout:

- python -B .tools/audit_event6_allocator.py --strict passed: 149 publishers; 126 automatic/high-chaos selectable; 138 SCN-008 ranked; 40 adapters; eight adapter-only fail-closed IDs IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177 and IW-179; 32 attested packages; 29 compatible reservation groups; 20 admitted static standalone witnesses; RHINE-SAAR pair capacity 2.
- python -B .tools/audit_event6_country_api.py passed: 242 unique broad tags; 191 unique resolved carriers; missing=0; duplicates=0; IW-031 crosswalk pass.
- Static character-identifier scan found zero duplicate top-level mod character IDs and zero mod/installed-Vanilla ID collisions. It does not check active human roster uniqueness after runtime transfers.
- The asset status above reuses the exact 2026-09-25 specialized flag and portrait handoffs. This agent did not visually inspect flag or portrait quality.

Read-only HOI4 MCP outcomes:

- Event 021 chaosx.nr21.1 inspect/lint returned EVENT_INSPECTED_PARTIAL with source-linked artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7423d81016dad6671bdca6d842ef1f400643079fe171e0a8122609d10d9505a/b7b3d5097ef9501f3587530cc9bdf322c48cb970592a8874f79dd456efe44ada/event-lint-9c06eb1a7fbd.json. Overview render returned EVENT_RENDERED_PARTIAL; manifest hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8fdbf13b06eaecf7e9e4bff2ae4bcd6d1a1f78a148afc42542496bb0814c416c/e1a5665db2ac650b95ba7fe443a4aa66149cef6f834962ca8e4f07cc60aa0dee/event-overview-f50fb76d44de-manifest.json. Partial global graph/source coverage is not a successful scenario execution.
- Event 006 chaosx.nr6.1 overview render returned EVENT_RENDERED_PARTIAL; manifest hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a45e1ade97d891f59160fbd8917601a687375f749421ce3aac3b7c8f9ecbaecb/23b0df5ef70d39d391b3b53359f90c8cda8ee3a812294969a8397fb5422307f0/event-overview-f50fb76d44de-manifest.json.
- Shared independence_wave_focus_tree inspect/render returned FOCUS_INSPECTED and FOCUS_RENDERED. Inspect JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3c91857287460ad5b4f00ef8f4640f342517177e652c77de350bab577009a25/c56eae50c7ecfddb75f1b400740908268938dff2eb73d9b8231fcf4747302f05/focus-inspect.4a66563cb763fd57.json. Rendered SVG: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/d65c84b3f334d371539f4fe2a5adddf279b489c842cd7e967a6a41c2855bd4f4/independence_wave_focus_tree.focus.svg. One authored ten-column connector is accepted in the current Event 006 source map; a separate warning concerns an unrelated Vanilla continuous-focus localisation. This shared-tree render does not certify every package branch in-game.
- Map inspection of the 32 anchors returned MAP_INSPECTED. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cac49eaeb0db05051d1b0d5bddada586308c0510917b9d100a191a48a74a4181/62a1fbe5502bf510ab22922efe5d374cdd96a7c432b54d2d1f8b32a328cdb4f1/map-inspect.c27b8c751e1c28e1.json. The workspace result truncated 2,654 unrelated/global building-position and port-adjacency diagnostics; no selected-anchor defect could be attributed from the inline result. Correctly typed map render returned Transport closed, so no rendered-map evidence exists.
- The inherited independence_wave_status_window inspection returned GUI_INSPECTED, but the broad and narrowed normal-resolution renders both timed out at 180 seconds. No GUI visual acceptance is claimed.
- Technology inspect and render routes responded, but no package-specific technology tree is assigned; package effects inherit former-host technology. The installed Technology Tree Viewer package check reports standalone_viewer_in_package=false and no viewer UI route. A separate current process/app/command inventory found no HOI4 or Technology Tree Viewer process/command; external viewer installations were not inventoried. Tool exposure is not proof of standalone viewer or service health.
- No independent HOI4 MCP server version/health endpoint or client task-negotiation receipt was available in this session. The domain routes above were read-only and produced the listed results, but this is not a complete service-health verification.
- The required chaosx_ai_probability_auditor was spawned with fork_context=false and the complete 32-row scope. Repeated bounded waits returned timed_out with no report/artifact. Its package-weight, AI-strategy, and scenario evaluation is therefore pending; the existing 2026-09-25 current-source probability handoff is only partial local-pool evidence and does not replace that pass.

## Prior findings: current, stale, or superseded

The 2026-09-20 handoff event006_country_package_audit_2026-09-20.md remains useful for its 32-row identity crosswalk, separate-origin analysis, and runtime-unverified boundary.

Its claim that primary package selection checks capital and reservation constraints is too broad for current source. Those exclusions sit behind the secondary-search flag; the ordinary primary path bypasses them. Re-audit the current code at event021_parent_find_event6_package before relying on that older statement.

The separate 2026-09-20 event006_adapter_abort_cleanup_2026-09-20.md repair resolves the old source-level omission that failed Event 021 adapter attempts did not reset current-generation Event 006 package state. Current abort helpers call event021_parent_cleanup_failed_event6_adapter_actor, and that helper resets the generation and restores the prior Event 021 generation value when present. The older abort-reset finding is stale/resolved at source level.

The older 2026-09-20 handoff’s statement that all 32 actors’ live materialization/save-reload was unverified remains current. Its broad flag-family completeness statement is superseded for this scoped runtime lookup by the row-specific 2026-09-25 flag audit, especially the unresolved ICE_personal_union lookup. The older probability errors and absence of a completed typed audit remain historical evidence only; the current specialist pass in this task is still pending.

## Uncovered requirements and runtime limits

- No actual game campaign was launched. No package was materialized in a save, no fresh/cold load or reload was run, and no leader, flag, politics, focus, decision, formable, AI, military, industry, supply, reinforcement, capital, diplomacy or settlement consumer was observed in-game.
- Static uniqueness and package-completeness proofs do not show that a character is active in exactly one live country or that setup does not collide with existing campaign roster state.
- No package-by-package localization audit was run. Focus, decision and AI weights were not comprehensively modeled; current weighted verification is pending the delegated specialist.
- No engine fallback was assumed for missing carrier/cosmetic flags. Portrait identity/provenance findings remain with the portrait worker’s handoff; this audit did not inspect portrait quality or gender presentation.
- The focus MCP result is one shared tree, not a 32-country scenario matrix. The GUI renderer timed out. The map renderer transport closed. Event inspect/render results are partial. These are coverage gaps, not source proof of a runtime defect.
- The candidate matrix and binding CSV are source evidence, not proof that each current host owns/controls its anchor in the user's campaign.
- FORM-48, FORM-07 and FORM-08 readiness gaps remain. IW-179/FSM was not added to the Event 021 list.
- No rollback/relaunch or capital restoration receipt exists. The anchor/capital concern needs parent resolution before any claim that all protected-remnant paths are safe.

## Handoff conclusion

The 32-row identity crosswalk, carrier and anchor uniqueness, normal-human gates, package setup proof, separate Event 021 origin, no-normal-Event-006 lifecycle mutation, package generation reset, and terminal cleanup are source-supported. These checks do not constitute completion.

Parent review should first resolve the primary-anchor protected/current-capital gate and the capital/footprint rollback/runtime questions, decide whether the hidden Statehood Ledger GUI and gated formables are acceptable Event 021 package surfaces, and obtain the pending specialist probability handoff. Keep Event 021 at HOLD / PARTIAL until those evidence gaps and the user-owned live validation boundary are carried forward.
