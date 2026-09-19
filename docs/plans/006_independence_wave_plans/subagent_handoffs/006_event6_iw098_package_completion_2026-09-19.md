# Event 006 IW-098 Sokoto package completion audit — 2026-09-19

## Disposition

Status: HOLD with no gameplay source patch.

The IW-098 package remains adapter-only and admission remains fail-closed.

The audit found no narrow, unambiguously safe package-local fix that can be applied without inventing identity, rights, portraits, flags, FORM-25 identity, central admission, or probability targets.

Only this handoff was added by this audit; no country, map, event, focus, decision, AI, asset, or central-admission source file was changed.

## Scope and authority

This audit covers only IW-098/SOK (Sokoto), the accepted Event 006 package specifications, the current source, and the current installed-map rebinding evidence.

The accepted registry row is IW-098, resolved tag `SOK`, registered-tag reuse, automatic pool when not living, baseline anchor state `558`, and reservation group `RG-NIGERIA-COARSE` in `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`.

The accepted anchor and reservation sources are `docs/specs/006_independence_wave_specs/matrices/006_state_anchor_and_reservation_groups.csv` and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.

The latest relevant audit evidence was read from `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_country_package_closure_audit_2026-08-26.md`, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_package_readiness_audit_2026_08_02.md`, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_completion_gap_audit_2026-09-19.md`, and the 2026-09-13 route-cost and portrait-asset handoffs.

## Country-package coverage checklist

| Surface | Finding | Evidence and disposition |
| --- | --- | --- |
| Tag and registry | Structurally wired as `SOK`/IW-098 | Candidate registry, package loader, fixed-origin triggers, and scenario dispatch agree; no tag patch. |
| Current anchor | Current map anchor is state `902`, while accepted matrix baseline is `558` | The installed-map binding explicitly records `baseline=558`, `current=902`, `rebound_to_current_split`; do not rewrite the matrix or source anchor. |
| Reservation group | `RG-NIGERIA-COARSE` is wired | State `902` also appears in the IW-100 collision row, with IW-098 recorded as the winner and cardinality one; central capacity still blocks admission. |
| Former host | Former host is captured and checked | Source uses the fixed-origin former-host event target and requires a living, non-subject, non-capitulated host with a capital. |
| Identity/date | Post-cutover Sultan path exists; pre-cutover path is absent | Existing vanilla `SOK_siddiq_abubakar` is accepted only after `1938.06.17`; the accepted research requires Hasan dan Mu’azu Ahmadu before that date, but no grounded/source-cleared Hasan implementation is present. |
| Rights and portrait consumers | Dikko and Bello consumers are wired, but provenance and rights remain unresolved | Existing runtime DDS files are technically valid and exact consumer paths exist; unresolved identity/source/rights evidence keeps admission closed. |
| Flag and symbol | No Event 006 exact-period SOK flag family is present | Vanilla country color is not a substitute for the accepted period flag/symbol requirement; no asset was invented. |
| Event 012 separation | Preserved | Event 012 owns the SOK sovereign character and focus-tree lifecycle; Event 006 owns only its two SOK corps-command consumers. |
| Setup and forces | Adapter-local setup is complete but gated | Setup configures politics, values, ideas, decisions, focus, shared force mapping, mounted-mobile doctrine/force state, and p98 tradition only after attestation and leadership gates. |
| Focus | Shared IW focus framework is source-wired and MCP-inspected/rendered | No SOK-specific source defect was found; one unrelated vanilla continuous-focus localisation diagnostic and one long-connector warning remain in the shared tree. |
| Decisions | SOK decision surface and localisation are present | No safe local decision patch was identified; route-cost changes require the missing probability/audit authority and accepted balance target. |
| AI | Five IW-098 strategy identifiers are present | No weights were changed because the mandatory named probability-auditor route is not exposed and no accepted balance target authorises a new weight. |
| Localisation | SOK parties, leaders, decisions, focuses, and event strings are present | No missing package-local key requiring a safe patch was found. |
| FORM-25 | Generic `sahel_confederation` profile is loaded | No IW-098-specific WFX/SFX tag, member, territory, consent, flag, or identity adapter exists; this is a broader formable/central integration blocker. |

## Map and state setup

The current installed-map binding intentionally maps IW-098/SOK to state `902` (`Sokoto`) even though the accepted candidate matrix baseline is state `558`.

Vanilla `history/states/902-Sokoto.txt` defines owner `ENG`, cores `NGA` and `SOK`, Victory Point province `1891` with value `1`, and the expected Sokoto province list; the package binding records `ENG=126` as the former-host country and the current anchor as a rebound to the current split.

`common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` loads IW-098 with package id `iw_098`, region `RG-NIGERIA-COARSE`, current anchor `902`, and former-host ownership by `ENG`.

`common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt` uses `state=902` for the IW-098 fixed anchor, ownership proof, anchor proof, and capital survival proof.

The reservation registry also lists state `902` for IW-100; the collision record in `docs/plans/006_independence_wave_plans/` gives IW-098 the winner slot under cardinality one. This is evidence for capacity handling, not permission to rewrite either accepted baseline or central admission.

No `hoi4.map_rewrite` operation was attempted, so no map rollback or recovery action is required.

## Identity, date, rights, flag, and portrait consumers

The accepted Sokoto research dossier identifies Hasan dan Mu’azu Ahmadu as the pre-17 June 1938 Sultan and Siddiq Abubakar III as the post-cutover Sultan; it also explicitly rejects treating Ahmadu Bello as Sultan.

`common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt` implements `independence_wave_prepare_iw098_date_appropriate_leadership` only for the post-cutover `SOK_siddiq_abubakar` path and requires Event 012 safety, post-cutover state, and the existing vanilla character.

`common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt` implements `has_independence_wave_iw098_date_appropriate_leadership` with the same post-cutover restriction and no pre-cutover Hasan branch.

Adding a Hasan character, source, name, portrait, or date branch would exceed this bounded audit and would violate the no-invented-identity and no-unapproved-rights constraints.

`common/characters/006_independence_wave_characters_registry.txt` registers `SOK_muhammad_dikko` and `SOK_bello_rabah` as male corps commanders, and `history/general/006_independence_wave_character_recruitment_registry.txt` recruits them only for `SOK`.

Their runtime portrait consumers are `GFX_portrait_SOK_muhammad_dikko` and `GFX_portrait_SOK_bello_rabah` in `interface/006_independence_wave_small_assets.gfx`, pointing to `gfx/leaders/006_independence_wave/portrait_SOK_muhammad_dikko.dds` and `gfx/leaders/006_independence_wave/portrait_SOK_bello_rabah.dds`.

The asset audit reports valid 70-DDS outputs at 156x210 with hashes `84feaacc0f2e83c3f7380bb39d5a0849f30825de0e36a5c30ede82d346c676f4` (Dikko) and `c6a26906005d0f2a840156490609bab2c8500aacf5d9175135c6a7a464e17864` (Bello), but it does not establish grounded identity, source provenance, or rights clearance.

The Event 012 character `africa_priority_sokoto_sovereign` remains the only SOK sovereign consumer owned by Event 012, with its own portrait `GFX_portrait_012_africa_priority_sokoto_sovereign`.

No Event 006 SOK flag family or accepted exact-period flag/symbol source was found; vanilla colour data is not an admissible replacement.

No SOK advisor package was found in the bounded source surface, and no advisor was invented.

## Setup, politics, ideas, focus, decisions, and AI

`independence_wave_setup_iw098_sokoto` clears stale setup state, requires the prepared scope, fixed-anchor ownership, runtime content attestation, SOK anchor proof, former-host capital survival, and Event 012 safety, then applies the Sultan path, baseline laws, politics, values, ideas, decisions, focus configuration, command roster, and shared force mapping.

The setup validator requires the SOK package values, focus signature, command roster, force mapping, mounted-mobile package result, p98 tradition result, and anchor/host proofs before setting package completion.

`independence_wave_validate_iw098_package` is fail-closed on package setup, Sultan selection, full focus framework/signature/formable configuration, runtime attestation, date-appropriate leadership, command roster, force mapping, p98/mounted-mobile setup, anchor proof, host survival, Event 012 safety, and the accepted SOK idea result.

The focus framework is sourced from `common/national_focus/006_independence_wave_focus.txt`; the IW-098 configuration registers constitutional, traditional, emergency, patron, host-negotiation, guarded, association, reclamation, power-struggle, ambition, and league surfaces, plus `sahel_confederation` formable integration.

The decision source `common/decisions/006_independence_wave_iw093_iw098_decisions.txt` contains the IW-098 caravan/wells surface including `independence_wave_iw098_secure_caravan_wells`; its localised surface is present in `localisation/english/006_independence_wave_iw093_iw098_l_english.yml`.

The five package strategy identifiers in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` are `independence_wave_iw098_foundation`, `independence_wave_iw098_host_crisis`, `independence_wave_iw098_sultanic_federal`, `independence_wave_iw098_northern_constitution`, and `independence_wave_iw098_frontier_command`.

No AI strategy factor or probability target was modified because the mandatory `chaosx_ai_probability_auditor` route is not exposed in the current tool surface and no accepted balance target was supplied.

## Event 012 separation and cleanup

`common/characters/012_africa_priority_member_characters.txt` and `history/general/012_africa_priority_member_character_recruitment.txt` own `africa_priority_sokoto_sovereign` for SOK.

`common/scripted_effects/012_africa_priority_member_effects.txt` preserves an existing Event 006 focus surface and otherwise loads the Event 012 focus tree through `africa_priority_member_ensure_focus_tree_loaded`.

IW-098 setup and focus triggers exclude `independence_wave_iw098_event012_focus_tree_replaced`, `africa_priority_member_package_active`, and `africa_priority_member_focus_tree_loaded` states.

`independence_wave_cleanup_iw098_sokoto` retires only the Event 006 Dikko and Bello consumers, clears IW-098 route/formable runtime state and attestation flags, restores the generic focus surface, and calls the Event 012 focus-tree preservation helper without retiring the Event 012 sovereign.

This separation is correct and was not changed.

## Central adapter, attestation, preflight, Join, capacity, and cleanup

`common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt` provides IW-098 setup, final-validation, and cleanup dispatch branches through `independence_wave_dispatch_iw093_iw098_package_setup`, `independence_wave_dispatch_iw093_iw098_package_final_validation`, and `independence_wave_dispatch_iw093_iw098_package_cleanup`.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` has IW-098 fixed-origin and scenario-preflight branches, but the central attestation OR list omits IW-098.

`has_independence_wave_iw098_runtime_content_attestation` checks `independence_wave_iw098_runtime_content_attested`; no current source sets that flag for admission.

`is_independence_wave_runtime_package_preflight_ready` requires an attested package, and `common/scripted_effects/006_independence_wave_join_effects.txt` probes attested packages before Join selection, so the omitted attestation keeps IW-098 fail-closed.

The central allocator audit reports 40 runtime adapters, 32 attested packages, and IW-098 among the eight adapter-only fail-closed IDs; the same audit reports 29 reservation groups and the IW-098/IW-100 state collision.

Adding IW-098 to central attestation, capacity, Join, or admission would be a central integration change and is outside this package-only audit and the parent’s explicit no-central-admission constraint.

## FORM-25 linkage

`can_prepare_independence_wave_form25_from_iw098` is a readiness trigger requiring an active SOK package, a sultanic or northern route, compact/network/security thresholds, and no terminal lock.

`common/scripted_effects/006_independence_wave_formable_registry_effects.txt` loads the generic `independence_wave_formable_family.sahel_confederation` profile, whose registry constants require three members, three consents, and three anchors among other generic profile values.

The current source has no FORM-25-specific WFX/SFX tag, member roster, territory/anchor adapter, consent adapter, exact flag, identity, or route integration for IW-098.

No FORM-25 identity or member was invented and no generic profile was promoted to package admission.

## Required MCP evidence and exact tool blockers

The current exposed HOI4 MCP surface includes read-only focus, event, map, technology, and probability routes, but tool exposure does not establish the missing standalone viewer or named auditor.

Focus inspection of `mod:common/national_focus/006_independence_wave_focus.txt` with tree `independence_wave_focus_tree` returned 184 focuses, 196 connectors, zero node intersections, zero crossings, and one long connector, with one unrelated vanilla continuous-focus localisation diagnostic; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63bc102094c837f7fd5479c7c35201ce45da9bd0712b9053bea77b047bc1063f/185397ddc826fd6273e9c65f44fff959cbaca66a9bb6c37cfb581c69f286bb38/focus-inspect.8427a8872da7fdb5.json`.

Focus rendering succeeded for the same tree with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`; HTML artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdebf536d2d08d79fe87e7b92c0cc3c3df83ebd1812cd8aaaf3b82357db60585/independence_wave_focus_tree.focus.html`; SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/independence_wave_focus_tree.focus.svg`.

Map inspection of state IDs `902` and `558` succeeded and confirmed both are present in the current map workspace; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f75d6acf3905937d662d9b7d70360d3bdc9141e6fc5ce1cfaf1400f6acf31/fa6d18f12ce03f877843a26588be94642f3a69d602d40966d75a344f5f6a3f52/map-inspect.1f1a19ae741180ff.json`.

The map inspection validation was false only because the workspace contains unrelated map-wide building-position and port-adjacency diagnostics; no state-902-specific blocker was returned, and no declarative map write was attempted.

Event inspection of `chaosx.nr006.9801` in `events/006_independence_wave.txt` returned focused partial analysis with zero blocking diagnostics; the large workspace deferred helper/lifecycle projections and reported unresolved global nodes; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/316aeac481dd8ab1a9d9ff929ebe3e700c176d6748d800c753aea1d488ec4509/158dd3c211fdea814eb72dde238d7febd79c082d5fdb9aa65e37506f936f16d1/event-scan-d210fa95a760.json`.

The named `chaosx_ai_probability_auditor` tool is not exposed, so the mandatory probability pass could not be routed through that auditor.

Read-only direct probability inspection was still run as diagnostic evidence for `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, `common/national_focus/006_independence_wave_focus.txt`, and `common/decisions/006_independence_wave_iw093_iw098_decisions.txt`; it found no quantitative strategy-factor surface for the first two and one decision match for the third, but it is not a substitute for the required named-auditor pass.

No standalone Technology Tree Viewer tool was exposed or verified, so the viewer remains a package-validation gap; no SOK technology source was edited.

## Validators run

`python -B .tools/audit_event6_country_api.py` passed with broad `242`, resolved `191`, Soviet `34`, Africa `45`, missing `0`, duplicates `0`, and IW-031 crosswalk pass.

`python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008-ranked packages, 40 runtime adapters, 32 attested packages, and eight adapter-only fail-closed IDs including IW-098.

`python -B .tools/audit_event6_scenario_matrix.py` passed the SCN-008 matrix audit, including its 32 cells and eight edge cases.

No live Hearts of Iron IV session was launched, in accordance with repository instructions.

## No-change result and blockers

Changed files: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw098_package_completion_2026-09-19.md` only.

Changed tags, state IDs, leaders, parties, focus IDs, localisation keys, formable IDs, AI weights, portraits, flags, and central-admission identifiers: none.

Before and after package behavior is unchanged: IW-098 can reach its package-local adapter setup path only when the surrounding gates are satisfied, but central attestation/preflight/Join admission remains fail-closed.

Exact blockers are the missing source-cleared pre-cutover Hasan identity and date branch, unresolved Dikko/Bello identity/provenance/rights evidence, missing accepted SOK Event 006 flag/symbol family, omitted central IW-098 runtime attestation, incomplete central capacity/Join admission, incomplete FORM-25 identity/member/territory/consent/flag integration, unavailable named probability auditor, and unavailable standalone Technology Tree Viewer.

The current Event 012 separation, current state-902 rebound evidence, and package-local setup/final/cleanup guards are safe to retain.

No simplification or unapproved fallback was introduced.

## Admission state and parent follow-up

Admission remains `FAIL-CLOSED` for IW-098/SOK.

Before admission can be reconsidered, the parent must receive accepted source/rights evidence for the date-appropriate leadership and portraits, an accepted exact SOK flag/symbol package, explicit central attestation and capacity/Join integration, and a concrete FORM-25 identity/member/territory/consent/flag adapter; any AI target change must also receive the mandatory named probability-auditor baseline and compare pass.

Parent review should preserve the matrix baseline `558` as historical acceptance evidence while retaining current runtime anchor `902`, and should not add Event 006 ownership for the Event 012 sovereign character.
