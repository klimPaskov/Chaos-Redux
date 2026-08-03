# Event 006 IW-023 TRA independent source admission audit

Date: 2026-08-03

Package: `IW-023`

Country: `TRA` (vanilla Transylvania)

Audit mode: source-only package admission review; no gameplay, map, asset, or attestation edits.

Status: **HOLD**.

Source-local result: **PASS for the current replacement contract**.

Admission result: **HOLD because the outer runtime-content attestation and FORM-08 minimum proof are not complete**.

## Authority and evidence boundary

The accepted country contract is `docs/systems/006_independence_wave_transylvania_package.md`.

The current event authority is `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_completion_evidence_v106_2026_08_03.md`.

The superseded additive-package audit and the obsolete pasted flag-log were not used as current evidence.

The current replacement contract preserves vanilla TRA identity/history and the `austro_hungarian_releasable_focus` carrier while using a reviewed additive Event 006 overlay; it does not require a new TRA country tag, a new bespoke tree definition, or a replacement Maniu portrait.

Offline Paradox Wiki references consulted before source review include Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, Division modding, Equipment modding, Technology modding, State modding, Character modding, Portrait modding, and Map modding under `paradox_wiki/`.

Vanilla documentation consulted includes `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.

Vanilla precedents inspected were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/TRA - Transylvania.txt`, `common/characters/TRA.txt`, and `common/national_focus/austro_hungarian_releasable_shared.txt`.

## Country package coverage checklist

| Surface | Evidence and identifiers | Result |
| --- | --- | --- |
| Tag and registry | Vanilla `TRA` remains the package tag. `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt:8-12` requires `original_tag = TRA` and package id `iw_023`. | PASS locally; no mod tag redefinition found. |
| Candidate planner | `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt:9-19` requires an open plan, an unused package/reservation group, `is_independence_wave_exact_package_iw_023_tag_available`, and state `84` anchor availability. | PASS locally; no planner execution receipt. |
| Origin and host | `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt:14-41` binds exact TRA/state-84 origin availability, anchor ownership/control, former-host pointer, and protected former-host state. | PASS locally; no live transfer or save/load receipt. |
| Map and state binding | `docs/plans/006_independence_wave_plans/006_current_installed_map_package_bindings.csv:24` binds `TRA`, anchor `84` Transylvania, compact state `76` North Transylvania, former host `ROM`, protected state `46`, and reservation group `RG-DANUBE-BORDERLAND`. | PASS locally; no map write was necessary. |
| Vanilla history and roster | Vanilla history retains capital `84`, democratic starting setup, and `Iuliu Maniu`. `events/006_independence_wave.txt:166-186` sets `independence_wave_tra_vanilla_roster_checkpoint` only when the ruling Maniu roster is present. | PASS locally; no runtime roster receipt. |
| Politics and parties | `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:138-246` exposes constitutional, workers, traditional, emergency, and patron-client routes with route-specific politics, popularity, party names, ideas, and ledger deltas. | PASS locally; route balance is not runtime-attested. |
| Visible ledgers and lifecycle | `independence_wave_tra_frontier_cohesion` and `independence_wave_tra_federal_legitimacy` are initialized at `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:252-263`, clamped and refreshed at `:40-56`, and drive `tra_divided_border_authority` versus `tra_danube_settlement` at `:22-36`. | PASS locally; no live ledger progression receipt. |
| Focus ownership | `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:270-272` assigns `additive_overlay`. `common/scripted_triggers/006_independence_wave_focus_triggers.txt:41-82` permits the carrier only when the TRA lifecycle and `austro_hungarian_releasable_focus` are present. | PASS locally; additive carrier is intentional and does not replace the vanilla tree. |
| Focus dispatch validation | `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:308-316` requires `has_independence_wave_generic_focus_contract`; no blind TRA `load_focus_tree` call was found. | PASS locally; no live focus selection receipt. |
| Mission and decisions | `common/decisions/categories/006_independence_wave_transylvania_categories.txt:7-9` defines `independence_wave_tra_danube_council_category`; `common/decisions/006_independence_wave_transylvania_decisions.txt:13-222` contains one timed mission and eleven authored decisions with costs, cancellation/timeout, and AI blocks. | PASS locally; no live completion receipt. |
| Ideas and cleanup | `common/ideas/006_independence_wave_transylvania_ideas.txt:29-106` defines the seven TRA ideas. Cleanup at `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:326-355` removes the mission, eleven decisions, ideas, ledgers, lifecycle, route, roster, and AI state. | PASS locally; no save/load cleanup receipt. |
| Forces and military identity | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:24` maps TRA to `mountain_frontier`, tradition `68`, mountain infantry/defecting regulars, five named reinforcement paths, and no navy/air inheritance. Setup loads and applies it at `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:289-290`. | PASS locally; no runtime unit, equipment, supply, or survival receipt. |
| Technology, industry, supply, production | Setup adds `civilian_economy`, `export_focus`, and `volunteer_only` only when missing at `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:259-261`; no TRA OOB, factory-history, technology, production-line, train, fuel, or railway rewrite is present. | No source defect; runtime economy/supply behavior remains unverified. |
| AI and playability | `common/ai_strategy/006_independence_wave_transylvania.txt:21-68` defines frontier survival, former-host restraint, settled-frontier, and emergency-commission profiles. `common/ai_strategy/006_independence_wave_form08.txt:17-51` covers post-formation behavior. | PASS locally; no seeded AI survival or war receipt. |
| Portraits, flags, advisors | Vanilla `Iuliu Maniu` portrait and TRA flag identity are preserved. No fictional TRA portrait, advisor art, or opposite-gender name/portrait pairing is introduced. FORM-08 reuses existing `HUN_EMPIRE` cosmetic identity. | PASS locally; no visual runtime proof. |
| Localisation and icons | `localisation/english/006_independence_wave_transylvania_l_english.yml:13-62` covers TRA ideas, category, actions, tooltips, route names, and player-facing text. Existing Event 006 decision/focus sprites are reused. | PASS locally; no in-game render receipt. |
| FORM-08 contract | `common/scripted_effects/006_independence_wave_form08_effects.txt:11-40` is scoped to active TRA anchor `84` and HUN identity reuse. `common/scripted_triggers/006_independence_wave_form08_triggers.txt:85-119` requires three members, three consents, and three anchors before mutation. | Source gate is correctly fail-closed; required independent proof is absent. |
| Event 005 separation | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:96-101` rejects `soviet_collapse_active_origin`, `liberation_origin.soviet_collapse`, and an already-active Event 006 origin before package preflight. | PASS locally; no cross-origin runtime receipt. |
| Runtime attestation | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:73-90` attests fourteen package IDs and does not include `iw_023`, although `iw_023` remains in the adapter list at `:10-36`. | **BLOCKING HOLD.** Parent-owned promotion is required after accepted admission evidence. |

## File surface checklist

The reviewed package surface is complete for the current contract:

- `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt` covers exact tag, planner-origin, runtime-ready, roster, prepared-setup, final-validation, and cleanup guards.
- `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt` covers setup, ledgers, five government routes, former-host and Network effects, force loading, AI registration, final validation, and cleanup.
- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` and `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt` cover the automatic TRA planner adapter.
- `events/006_independence_wave.txt` covers the hidden `chaosx.nr6.350` Maniu roster checkpoint.
- `common/national_focus/austro_hungarian_releasable_shared.txt` and `common/national_focus/006_independence_wave_focus.txt` cover the vanilla carrier and reviewed additive overlays.
- `common/decisions/categories/006_independence_wave_transylvania_categories.txt` and `common/decisions/006_independence_wave_transylvania_decisions.txt` cover the visible decision/mission surface.
- `common/ideas/006_independence_wave_transylvania_ideas.txt` covers the seven package ideas and lifecycle names.
- `common/ai_strategy/006_independence_wave_transylvania.txt` and `common/ai_strategy/006_independence_wave_form08.txt` cover pre- and post-formation AI profiles.
- `common/scripted_effects/006_independence_wave_form08_effects.txt` and `common/scripted_triggers/006_independence_wave_form08_triggers.txt` cover FORM-08 registration, mutation gates, rollback, and cleanup.
- `localisation/english/006_independence_wave_transylvania_l_english.yml` covers the package's player-facing text.
- `docs/plans/006_independence_wave_plans/006_candidate_country_registry.csv`, `research/006_package_research_resolution.csv`, `006_current_installed_map_package_bindings.csv`, and `006_force_package_mapping.csv` provide the registry, research, map, and force receipts.

No missing TRA gameplay surface was found in the inspected source. No stale TRA-specific file was used to justify promotion. The only stale evidence boundary is the separately excluded obsolete flag-log.

## Map and state setup issues

No source-level map or state defect was found. State `84` is the fixed compact anchor, state `76` is the optional compact extension, and former-host `ROM` retains protected state `46` under the current binding.

No map rewrite was performed because the installed-map binding is already present and the requested audit does not authorize map changes.

Runtime ownership/control transfer, capital retention, railway, port, supply, resistance, and save/load cleanup remain unproven and are admission evidence gaps rather than source defects.

## Politics, leader, portrait, flag, advisor, and party issues

TRA preserves the vanilla ruling leader `Iuliu Maniu`, vanilla character roster, vanilla portrait path, and vanilla TRA flag identity.

The five route identifiers and party-name localisation are wired in the route effects; no advisor or high-command replacement is required by the current contract.

No opposite-gender portrait/name pairing, institutional-body misuse, invented historical leader, or unreviewed flag was introduced.

Runtime ideology, popularity, stability, war support, diplomatic posture, and route selection remain unverified.

## Focus, decision, idea, and asset issues

The package uses the accepted additive carrier model. It preserves `austro_hungarian_releasable_focus` and attaches the reviewed shared overlay through `independence_wave_focus_assignment.additive_overlay`.

The mission and decision category have authored costs, timeout/cancellation behavior, AI blocks, localisation, and cleanup references. The seven TRA ideas and both visible ledger names are present.

No custom TRA focus icon, idea icon, portrait, advisor asset, or flag asset is required beyond reused registered assets. No asset generation or runtime wiring was performed.

No live focus render, decision completion, icon render, portrait display, or cleanup receipt is available for admission.

## Starting military, technology, industry, supply, and production issues

The source mapping is the intended mountain-frontier profile with no navy or air inheritance and no free recurring reinforcement loop. The setup applies the dynamic starting-force mapping and leaves vanilla technologies, factories, production lines, trains, fuel, and supply rules intact except for conditional starting laws.

No source-level OOB, equipment, technology, factory, railway, port, or supply defect was found. Runtime force counts, stockpiles, supply capacity, production, and survival remain untested.

## AI and playability issues

TRA has source-gated frontier survival, former-host restraint, settled-frontier, and emergency-commission strategy profiles, plus FORM-08 post-formation strategies.

No seeded AI focus/decision selection, front behavior, diplomacy behavior, war survival, or save/load test was run. This prevents promotion from source review alone.

## FORM-08 and Event 005 origin boundary

FORM-08 is correctly limited to a live TRA package with anchor `84`, capital `84`, and the existing `HUN_EMPIRE` cosmetic identity. The trigger remains fail-closed until independently frozen evidence proves at least three members, three valid consents, and three anchors.

AXX and MAC remain researched carrier rows, not admitted members. This audit does not infer their membership, consent, anchor, tag, flag, or identity proof.

The Event 005 Soviet Collapse origin is separated by the preflight exclusions in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:96-101`; no cross-origin release or cleanup path was added.

## Validation receipts

The following source-only checks were run on 2026-08-03:

- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reported 136 protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one intentionally skipped random-event root.
- `python -B .tools/audit_event6_flags.py --strict` reported 102 registered Event 006 tags, 102 complete flag families, and zero incomplete flag families.

The validation outputs are static source receipts only. They do not prove planner execution, release, ownership transfer, focus selection, AI survival, visual rendering, live FORM-08 mutation, save/load persistence, or cleanup.

Skipped meaningful validation: no Hearts of Iron IV launch, no live MCP planner/focus/decision session, no map rewrite, no release or transfer test, no seeded AI run, no runtime asset display test, and no save/load test were performed or claimed.

## Missing or stale surfaces and admission blockers

No local TRA source repair is warranted. The package contracts, map binding, vanilla roster checkpoint, additive carrier, decisions, ideas, force mapping, AI, localisation, and cleanup are coherent under the accepted replacement contract.

The immediate admission blocker is the parent-owned compile-time attestation OR-set at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:73-90`; it excludes `iw_023` by design. This audit does not edit that gate.

The second blocker is the independent FORM-08 minimum proof of three members, three consents, and three anchors. AXX and MAC are not promoted by this audit.

No fallback identity, generic replacement tree, invented tag, invented portrait, invented flag, or balance simplification was used.

## Handoff and changed files

Changed files: this handoff only.

No gameplay file, tag, state id, leader id, party id, focus-tree id, localisation key, decision id, idea id, force profile, formable id, map binding, or attestation entry was changed.

Safe next step: parent may perform a separate admission decision after accepting this independent source receipt, then update the attestation set and rerun the complete Event 006 validation suite. That promotion is intentionally outside this audit.

