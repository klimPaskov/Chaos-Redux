# IW-004 Brittany readiness re-audit — 2026-07-22

## Scope and disposition

This is a fresh country-package audit of the accepted Event 006 IW-004 Brittany package (`BRI`) after the sourced portrait replacement. It covers the registry and research binding, tag/origin admission, state reservation and host survival, package setup and cleanup, force mapping, politics, leaders, focus and decision surfaces, AI, localisation, flags and portrait provenance. It does not modify gameplay files, the runtime attestation, the registry, or any protected asset.

**Disposition: remain fail-closed for runtime admission.** The BRI package is internally consistent and static-admission ready, but the current execution gate is intentionally closed: `has_independence_wave_runtime_package_content_attestation_for_execution_id = { always = no }` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`. This handoff recommends that the parent keep IW-004 out of runtime execution until the parent-owned compile-time content attestation is deliberately restored with this audit as evidence. No package defect requires a local patch.

## Country-package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Accepted identity/binding | PASS | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` (`IW-004`, `BRI`, Level 2, `reuse_registered_tag`); `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` (BRI, `automatic_pool_ready_if_not_living`, state 14, `RG-14`). |
| Tag and origin gate | PASS | `common/scripted_triggers/006_independence_wave_brittany_package_triggers.txt` (`is_independence_wave_bri_package`, `can_initialize_independence_wave_iw_004_package`, `has_prepared_independence_wave_iw_004_package_setup`); dispatch adapter matches package id 4. |
| Anchor/host/Event 005 collision | PASS | BRI resolves to state 14; the allocator and runtime capacity triggers require the state-14 anchor, host survival, Event 005 opening-core exclusion, and `RG-14`. Current installed state 14 is FRA-owned and state 16 remains the protected FRA capital. |
| History and map coherence | PASS | Vanilla `history/countries/BRI - Brittany.txt` starts at capital 14; vanilla `history/states/14-Brittany.txt` is a coastal/port state with Breton and French cores, dockyards and naval facilities. No mod-side duplicate BRI country/history/tag/flag override was found. |
| Starting setup and lifecycle | PASS | `common/scripted_effects/006_independence_wave_brittany_package_effects.txt` prepares roster, laws, politics, lifecycle ideas, full focus framework, route gates, formable family, force mapping and AI profile; `has_prepared...` checks the complete package receipt. |
| Forces/technology/industry/supply | PASS | `common/scripted_effects/006_independence_wave_force_package_effects.txt`, `006_independence_wave_force_effects.txt`, `006_independence_wave_force_package_constants.txt`, and `006_force_package_mapping.csv` agree on p4 `coastal_maritime`, tradition 58, coastal infantry/sailors/local guards, navy inheritance, no air inheritance, and five required pathways. |
| Politics/ideas/advisors | PASS | BRI baseline laws and 45/20/30/5 starting popularity are set in the package effect; two lifecycle ideas and five route ideas are defined in `common/ideas/006_independence_wave_brittany_ideas.txt`; advisor roster uses existing vanilla BRI characters only. |
| Focus tree | PASS | BRI has five package-specific nodes in `common/national_focus/006_independence_wave_focus.txt`, loaded through the shared framework with package prerequisites, icons, AI weights, localisation and network/formable gates. |
| Decisions/mission | PASS | `common/decisions/006_independence_wave_brittany_decisions.txt` contains one 480-day mission and fourteen package decisions with package/host/capital gates, costs, AI weights, timeout/cancel effects and cleanup. |
| AI/diplomacy/host behavior | PASS | `common/ai_strategy/006_independence_wave_brittany.txt` covers survival, host threat, route priorities and founding/settled restraint; host/relationship cleanup is wired through shared Event 006 effects. |
| Cleanup | PASS | `independence_wave_cleanup_iw_004_brittany` removes the BRI mission, all fourteen decisions, package ideas, route/lifecycle flags and variables; shared origin cleanup clears force/focus/league/network state. |
| Localisation | PASS | `localisation/english/006_independence_wave_brittany_l_english.yml` is UTF-8 BOM and covers both leaders, descriptions, parties, category, mission, all BRI decisions, ideas, focus nodes and tooltips; shared cost strings are in `006_independence_wave_decisions_l_english.yml`. |
| Flags and portraits | PASS | Vanilla BRI identity flags remain the only active BRI flag surface. The two BRI Event 006 runtime sprites point to the replacement DDS files below; no BRI `_small`, advisor, dossier or miniature consumer exists. |
| Runtime admission | HOLD | Deliberately empty runtime content attestation keeps all Event 006 execution fail-closed. This is the only current blocker and is not changed by this handoff. |

## File surface and identifier checklist

The package references are complete and consistent across these owned gameplay surfaces:

- `common/scripted_triggers/006_independence_wave_brittany_package_triggers.txt`: package/origin/anchor/host gates, command and advisor roster, lifecycle/route/formable/force receipts, complete-package gate.
- `common/scripted_effects/006_independence_wave_brittany_package_effects.txt`: BRI roster and portrait assignment, baseline laws and politics, lifecycle/route setup, IW-004 setup/final-validation/cleanup adapters.
- `common/ideas/006_independence_wave_brittany_ideas.txt` and `common/script_constants/006_independence_wave_brittany_constants.txt`: lifecycle and route ideas plus central BRI tuning.
- `common/decisions/categories/006_independence_wave_brittany_categories.txt` and `common/decisions/006_independence_wave_brittany_decisions.txt`: BRI category, mission and fourteen decisions.
- `common/national_focus/006_independence_wave_focus.txt`: `independence_wave_bri_charter_ports_fisheries_focus`, `independence_wave_bri_establish_breton_gallo_services_focus`, `independence_wave_bri_integrate_sailors_guards_focus`, `independence_wave_bri_settle_french_accounts_focus`, `independence_wave_bri_convene_celtic_delegation_focus`.
- `common/ai_strategy/006_independence_wave_brittany.txt`: BRI survival, host-threat, route-policy and restraint strategies.
- `localisation/english/006_independence_wave_brittany_l_english.yml`: `BRI_independence_wave_civic_delegate` = Régis de l'Estourbeillon and `BRI_independence_wave_coastal_commandant` = Henri-Léon Devin, with all package player-facing strings.
- `interface/006_independence_wave_brittany_portraits.gfx`: `GFX_portrait_BRI_independence_wave_civic_commission` and `GFX_portrait_BRI_independence_wave_coastal_commandant`.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`: BRI setup, final-validation and cleanup dispatch are present in all three passes.
- `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt` and `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt`: BRI is an explicit FORM-01 eligible member/carrier with state-14 anchor protection.
- `common/scripted_effects/006_independence_wave_force_package_effects.txt`, `common/scripted_effects/006_independence_wave_force_effects.txt`, and `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv`: package id 4 and p4 mapping receipts agree.

## Map, state, host, and collision findings

- State 14 (`Brittany`) is the accepted fixed compact anchor and is a legal coastal port state. The BRI setup trigger requires that the setup anchor event target resolves to state 14 and that BRI owns and controls it.
- The installed vanilla state history has `owner = FRA`, capital state 16 is outside the compact package, and the package binding explicitly requires FRA to retain that capital. The current installed map scan found 75 FRA-owned states; no over-broad “take all host states” behavior is present in the BRI package.
- `RG-14` is unique/max-one, and the allocator checks the state reservation and host protected-state rules before selecting IW-004. The task-specific allocator check passed (`python -B .tools/audit_event6_allocator.py`: 149 publishers, 126 automatic/high-chaos selectable packages, all automatic counts and scenario/order checks passed).
- Event 005 collision guards reject Soviet/Event 005 opening-core anchors and hosts. BRI/state 14/FRA do not match those protected sets; the IW-004 capacity path also checks host survival and RG-14.
- No mod-side `BRI` tag, country definition, country history, state-history override, or flag override was found. Vanilla BRI registration and identity flags remain the source of truth.

## Leaders, portraits, sources, and asset consumers

Both one-person leaders are grounded real male figures, use male metadata, and are assigned through existing BRI character tokens; no random-name pool, female metadata, institutional-body naming, or generated-person substitute remains.

1. Civic delegate: Régis-Marie-Joseph de l'Estourbeillon (1858–1946), Breton regionalist leader and former Morbihan deputy. Source and rights evidence are in `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/manifest.md` and the v3 visual audit. Runtime DDS: `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`, 156×210, 131168 bytes, SHA-256 `583F821ED7F8B78A89321DBB7E1E7B7CAD7E30829DFA5DD14B6F255E42E27DC0`.
2. Coastal commandant: Henri-Léon Devin, French naval officer trained at École navale Brest in 1930, suitable for the 1936 joint coastal command role. Source, rights and ownership evidence are in `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/manifest.md`, `sourced_portrait_refinishes_2026_07_22/manifest.md`, and `006_devin_revision02_visual_audit_2026_07_22.md`. Runtime DDS: `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds`, 156×210, 131168 bytes, SHA-256 `0806F9560139EA1DBC30FF4385B16E829560D85BCDDD15A91A294B28D39802FB`.

The current runtime consumers are exactly the two sprite entries in `interface/006_independence_wave_brittany_portraits.gfx` and the two portrait assignments in `independence_wave_prepare_bri_roster_and_portraits`. A scoped search found no active BRI Event 006 advisor, dossier, commander miniature, `_small`, or extra portrait consumer. The source manifests report no active vanilla/current identity owner for either sourced figure. The protected prior Event 006 assets were unchanged:

- `portrait_BAY_rupprecht_of_bavaria.dds` — SHA-256 `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`.
- `portrait_RHI_josef_friedrich_matthes.dds` — SHA-256 `AA61CC3A12FB6670B690C7685FEB9383383CE58599C9E6D6E7C14F20FAB3BCE2`.

Older historical handoffs still mention the superseded fictional BRI portraits and `_small` paths, but those are documentation records only; no active runtime consumer or asset is present. They are outside this bounded ownership and were not rewritten.

## Politics, force package, focus, decisions, AI, and cleanup

- Politics initializes civilian economy, export focus and volunteer-only laws, then democratic elections with 45/20/30/5 popularity and distinct constitutional, traditional, labour, emergency and patron routes. Route ideas and transitions are BRI-specific and have a playable compact-stabilization path.
- The p4 force mapping supplies coastal infantry/sailors/local guards, engineers/coastal recon first, later artillery/logistics/signals, navy inheritance, no air inheritance, and five required preparation pathways. Dynamic force receipts and technology/slot inheritance are checked by the package-prepared trigger.
- The five BRI focus nodes are all localized, iconized, AI-weighted and gated by the shared framework. The final Celtic delegation focus requires network membership and links to the existing FORM-01 flow.
- The 480-day settlement mission and fourteen decisions cover language institutions, ports, sailors, French ledgers, flotilla/reserve tradeoffs, five government routes, durable independence and Celtic integration. Trigger tooltips/effect descriptions are present.
- AI strategies prioritize survival industry, equipment, support, coastal defense and host-threat response, with negative founding/settled restraint until the relevant threat or regional conditions justify escalation. Vanilla precedent confirms the negative `avoid_starting_wars` usage.
- BRI cleanup removes all package-local decisions, mission, ideas, route/lifecycle flags and variables. Shared origin termination additionally clears force mapping, focus runtime, league/network records and other Event 006 transient state.

## Runtime gate and recommendation

The current runtime attestation remains intentionally empty:

```text
common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt
has_independence_wave_runtime_package_content_attestation_for_execution_id = {
	always = no
}
```

The BRI package therefore cannot enter runtime execution even though its package-local setup and final-validation adapters are complete. This is a deliberate parent/registry admission gate, not a Brittany package defect. Recommendation: **remain fail-closed** until the parent restores an exact compile-time attestation entry after reviewing this handoff and the current portrait manifests. Do not add an IW-004 attestation from this subagent.

## Changes and validation

- Gameplay files changed: none.
- Runtime attestation changed: none.
- Assets changed: none.
- Handoff added: this file only.
- Meaningful checks: exact package/dispatch and cleanup surfaces reviewed; vanilla BRI/state-14/state-16 binding checked; allocator audit passed; both BRI runtime DDS hashes and dimensions matched the latest refinish manifest; BAY/RHI protected hashes matched; localization BOM and package key coverage checked; scoped runtime search found no prohibited BRI Event 006 assets/consumers.
- Skipped: in-game/runtime execution and map-write validation, because the runtime gate is intentionally closed and this subagent does not own the parent attestation or map scope. No logs were required or used.

## Remaining risks / blockers

1. Parent-owned runtime content attestation is empty, so IW-004 remains fail-closed despite a passing package audit.
2. Historical handoffs contain superseded portrait/_small wording; they do not affect runtime but may need a later documentation-curation pass.
3. A live-game run after parent admission is still needed to exercise actual release/host survival and dynamic force materialization; this audit establishes static readiness only.
