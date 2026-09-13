# Event 006 IW-095 Dahomey package tranche handoff (2026-09-03)

## Scope and disposition

This tranche audits IW-095 Dahomey (`DAH`) only, including the installed-state rebind, package-local preparation, central admission surfaces, Event 012 origin separation, identity and asset gates, and supported Event 006 consumers.

Disposition: **blocked; no gameplay promotion and no gameplay edits were made**. The package-local preparation is not an admitted Event 006 package because accepted identity, flag, portrait, central-admission, and current runtime evidence are incomplete. The safest bounded action is to preserve the existing fail-closed package and resolve the blockers below in order.

## Decision

Do not set `independence_wave_package_content_ready` for `DAH`, do not add `DAH` to the central adapter or content-attestation registries, and do not add a DAH shell, leader, flag, portrait, map binding, fallback, or Event 006 Join path in this tranche.

The installed runtime anchor is state `776` (Dahomey), not research-only baseline state `556` (Bamako). State `776` is currently owned by `FRA` before release and must remain the only executable anchor unless a later accepted source resolution explicitly changes it. The reservation group is `RG-NIGERIA-COARSE`, which permits at most one automatic package in the coarse group and requires the host protected-state check.

## Evidence reviewed

- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, IW-095 row: `DAH`, automatic only when a unique current state exists, baseline `556`, current source rebind to be rechecked, grounded male leader or authentic provisional institution required, source-correct symbol required, and no automatic medieval reconstruction.
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`, `RG-NIGERIA-COARSE`: baseline `556|558`, current installed rebind required, host protected state first, maximum one automatic package.
- `docs/specs/006_independence_wave_specs/research/006_sensitive_identity_research_rules.md` and `006_sensitive_package_resolution.md`: people, institutions, 1930s public name, communities, territory, government, compact anchor, and source/rights separation are mandatory; missing grounded identity is fail-closed.
- `docs/specs/006_independence_wave_specs/quality/research_acceptance_checklist.md` and `research_validation_report.md`: targeted research checks pass, but current map rebind, gameplay, runtime, AI, focus, decisions, GUI, and final visual checks remain open.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, especially the IW-095 entry and Event 006 boundary: package-local preparation is present at state `776`, while DAH shell, identity/rights, neutral flag/emblem, portraits, central adapter/publisher/preflight/Join, typed probability, and repaired MCP manifest remain absent or unresolved; state `556` is research-only.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, IW-095 row: current compact anchor `776`, former host `FRA`, baseline `556`, `rebound_to_current_split`, and `776=FRA` pre-release.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw095_package_audit_2026-08-26.md`, `006_iw095_dahomey_package_local_implementation_2026-08-27.md`, and `006_event6_iw095_source_research_2026-09-01.md`: prior audits agree that the package is local/prepared only, not centrally admitted; the opening flag and grounded leadership routes remain unresolved.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw095_portrait_gate_2026-09-01.md`: no approved portrait consumer, source placeholder, runtime DDS, or independent identity/rights review exists.
- Vanilla references: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\country_tags\00_countries.txt` registers `DAH = "countries/Dahomey.txt"`; vanilla `common/countries/Dahomey.txt` supplies only African graphical culture and a color; `history/countries/DAH - Dahomey.txt` has generic 1936 setup and no named leader; `history/states/776-Dahomey.txt` has owner `FRA`, core `DAH`, and capital province `10919`.
- Existing Event 012 use: `common/scripted_effects/012_africa_effects.txt` assigns the Dahomey host playbook to `DAH` and state `776`; `common/scripted_triggers/012_africa_proof_triggers.txt` contains the Dahomey host/action rows. This requires an explicit origin-safe separation before Event 006 admission.

## Country package coverage checklist

| Surface | Status | Evidence and exact identifiers |
|---|---|---|
| Tag registration and consistency | Partial | Vanilla carrier `DAH` exists; no Event 006 DAH entry in `common/country_tags/006_independence_wave_countries.txt`; package-local selectors use `original_tag = DAH`. |
| Current state anchor and host | Partial | Executable anchor is `776`; research baseline `556` is non-executable; current `776=FRA` and the protected-remnant/host runtime receipt is still open. |
| Reservation and admission | Blocked | `RG-NIGERIA-COARSE` is present in package-region registries, but the central admission gate has no IW-095 adapter, attestation, publisher, preflight, or Join receipt. |
| Government, identity, and rights | Blocked | Package-local setup is gated by `independence_wave_iw_095_identity_rights_cleared`; no accepted identity route or rights attestation clears it. |
| Flag and emblem | Blocked | No approved opening 1936 flag route or rights record; vanilla modern/1959 designs and French tricolor are not acceptable substitutes. |
| Leader and portrait | Blocked | Casimir d'Almeida is a research-only candidate with role/spelling/rights/consumer unresolved; the Abomey source is an institutional court reference, not an approved leader portrait. |
| Parties and localization | Partial | DAH package-local party, route, category, mission, project, and idea keys exist in `localisation/english/006_independence_wave_l_english.yml`; central admitted-country coverage is absent. |
| Focus tree | Blocked | Shared tree exists, but `common/national_focus/006_independence_wave_focus.txt` has no `IW095`/`DAH` package callback or admitted tree assignment. |
| Decisions and missions | Partial/blocked | Package-local IW-095 category, mission, and projects exist, but visibility and activation require setup, rights, and force gates that are not centrally reachable. |
| Ideas and lifecycle | Partial/blocked | DAH ideas exist in `common/ideas/006_independence_wave_ideas_registry.txt`; carrier/setup lifecycle is package-local and unadmitted. |
| Forces and economics | Partial/blocked | Dynamic package helper and P95 territorial-defense mappings exist; vanilla DAH has only generic setup and no promoted Event 006 force/industry receipt. |
| AI and probability | Blocked | DAH strategy factors exist in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, but no typed probability audit/compare artifact exists. |
| Event and origin safety | Blocked | `chaosx.nr6.1` remains generic; Event 012 already owns DAH host logic, and no Event 006 DAH origin-safe adapter/cleanup path is admitted. |
| Formable and regional ambition | Missing | No DAH/Form-24 formable family is registered; the package-local prepared gate explicitly requires `independence_wave_formable_family_registered` to remain false. |

## File surface checklist

| Surface | Current file(s) | Finding |
|---|---|---|
| Country tags/shell | `common/country_tags/006_independence_wave_countries.txt`; `common/countries/006_independence_wave_shared_african.txt` | `DAH` is absent from the Event 006 tag list and shared African shell. This is deliberate carrier protection until identity and admission are accepted. |
| Country history | Vanilla `history/countries/DAH - Dahomey.txt`; package effects under `common/scripted_effects/006_independence_wave_first_footprint_package_effects.txt` | No mod DAH history or admitted Event 006 setup exists; vanilla setup remains generic. |
| State/map | Vanilla `history/states/776-Dahomey.txt`; `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` | State `776` is the only current execution anchor; `556` must not be executed. Fresh map/runtime inspection is unavailable, so topology, supply, railway, port, and host-protection claims remain unvalidated. |
| Politics/parties | Vanilla DAH history; `localisation/english/006_independence_wave_l_english.yml`; first-footprint effects | Package-local politics and party names are gated; no accepted government/identity route or central publisher exists. |
| Leaders/characters/portraits | Vanilla `common/characters/DAH.txt`; no mod DAH character/GFX consumer | Vanilla DAH has generic advisors and no named package leader; no approved source portrait, character role, portrait GFX, or runtime DDS exists. |
| Flags/emblems | Vanilla `gfx/flags/DAH_*.tga`; source research handoffs | Technical vanilla flags are not accepted as the Event 006 opening identity; source motif route and rights are unresolved. |
| Focus | `common/national_focus/006_independence_wave_focus.txt` | Generic tree has no IW-095/DAH callback. Package-local route hooks do not establish central tree reachability. |
| Decisions/missions | `common/decisions/categories/006_independence_wave_categories.txt`; `common/decisions/006_independence_wave_decisions.txt` | IW-095 category and projects are local and fail closed on setup/rights/force/capital. |
| Ideas | `common/ideas/006_independence_wave_ideas_registry.txt` | DAH compact, council, customs, market, civic guard, emergency, land, and trade ideas exist but cannot be reached by an admitted runtime package. |
| AI | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` | Survival, restraint, settled compact, and emergency strategy rows exist; probability evidence is missing. |
| Event/admission | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`; `common/scripted_effects/006_independence_wave_effects.txt` | Central adapter, attestation, setup dispatch, final validation, and Join lists do not include IW-095. |
| Event 012 separation | `common/scripted_effects/012_africa_effects.txt`; `common/scripted_triggers/012_africa_proof_triggers.txt` | Existing DAH host playbook at state `776` creates a concrete origin/cleanup collision risk. |
| Formable | No dedicated DAH/Form-24 source under `common/formable_nations/` or equivalent | Formable family and scope checks are absent. |
| GUI | Shared Event 006 status UI only; no DAH-owned GUI | Prior dated GUI evidence reports `GUI_TAB_STATE_CONFLICT`; current GUI MCP inspection is unavailable. No DAH-specific GUI should be added in this tranche. |

## Missing or stale country package surfaces

The missing surfaces are central admission, a source-accepted identity and rights record, an approved opening flag/emblem, a portrait-worker-owned grounded identity package, a DAH shell/leader/consumer when those inputs are accepted, a DAH adapter/attestation/publisher/preflight/Join path, Event 012 origin-safe cleanup, shared-tree callback, and current runtime receipts. The package-local constants, triggers, effects, decisions, ideas, localization, and AI rows are not stale by themselves, but they are intentionally unreachable while these gates remain closed.

## Map and state setup issues

`776` is the installed Dahomey state and capital anchor; `556` is Bamako and research-only. Vanilla `776` is `FRA`-owned with `DAH` core and capital province `10919`, and the source-of-truth map records `776=FRA` before release. A promotion patch must prove unique reservation, former-host protected-state ownership, controller/owner timing, capital retention, supply/rail/port coherence, and no collision with Event 012. No map rewrite or fallback is safe without fresh MCP map evidence.

## Politics, leader, portrait, flag, advisor, and party issues

The accepted research set does not yet clear a grounded 1936 leader. Casimir d'Almeida is only a research candidate for a narrow Porto-Novo representative/administrative-council role, with spelling, exact office, portrait consumer, rights, and independent review unresolved. The Abomey material supports an institutional court/council context but does not authorize a fabricated personal leader. The portrait gate explicitly requires `chaosx_portrait_creator` to resolve source provenance, role, crop/path mismatch, placeholder, GFX consumer, and DDS manifest; no generated or opposite-gender substitute is allowed.

No reviewed, redistributable opening flag exists. The Ghézo/Abomey banner is an unresolved route-only motif with museum-rights uncertainty, while vanilla DAH flag variants represent later or generic technical identities and cannot be silently reused. DAH package party localization exists, but party names cannot clear the identity/rights gate on their own. Vanilla advisors are generic and do not satisfy a grounded leader requirement.

## Focus, decision, idea, and asset issues

The package-local focus callbacks and decision/idea content are gated and not centrally reachable. `common/national_focus/006_independence_wave_focus.txt` contains no `IW095` or `DAH` callback. The decision category and projects require `independence_wave_iw_095_identity_rights_cleared`, completed setup/force, and capital `776`. No DAH focus icon, decision icon, neutral flag/emblem, or portrait runtime asset has an accepted manifest. No fallback tree, icon, flag, or portrait may be introduced.

## Starting military, technology, industry, supply, and production issues

Vanilla DAH starts with `infantry_weapons = 1`, ten convoys, generic advisors, and neutral politics; it has no package-specific divisions, templates, stockpile, research-slot, production, industry, railway, or supply receipt. The package-local dynamic force helper is not a live admitted setup. Any future setup patch must use the accepted force mapping and validate state `776` capital/supply/port behavior. Technology Tree Viewer is not installed in the current MCP package, and the technology MCP route was unavailable, so no technology-tree claim is made.

## AI and playability issues

The IW-095 strategy rows provide survival, restraint, settled-compact, and emergency numeric factors, but the country cannot enter the package lifecycle while identity, central admission, and roster receipts are absent. The mandatory `chaosx_ai_probability_auditor` route and HOI4 probability inspect/evaluate/compare tools were unavailable in this model context, so no baseline, scenario sweep, or before/after balance claim is valid.

## MCP and runtime evidence

Fresh read-only HOI4 MCP evidence was attempted for the supported in-scope surfaces, but the installed route was unavailable to this model context.

| Attempt | Result | Consequence |
|---|---|---|
| `hoi4.event_inspect` with `{ kind: "event", eventId: "chaosx.nr6.1" }`, downstream trace, `refresh=true` | Returned `MCP tool hoi4_agent_tools/hoi4.event_inspect is not available to the model` | No fresh Event 006 trace artifact; the dated 2026-09-02 partial trace in the source-of-truth map is prior evidence only. |
| `hoi4.event_render` for `chaosx.nr6.1` | Returned `MCP tool hoi4_agent_tools/hoi4.event_render is not available to the model` | No fresh event render/compare evidence. |
| `hoi4.focus_inspect`/render, `hoi4.map_inspect`/render, `hoi4.gui_inspect`/render, `hoi4.tech_inspect`/render | Corresponding callable functions were unavailable/undefined | No fresh focus, map, GUI, or technology runtime artifact. |
| `hoi4.probability_inspect`, evaluate, compare | Corresponding callable functions were unavailable/undefined | Mandatory probability audit/compare could not run; no AI balance claim. |
| Technology Tree Viewer | Not exposed by the installed package | Record as unresolved limitation; source review is not engine evidence. |

## Changed files and identifiers

Only this handoff file was added. No gameplay, localization, asset, flag, portrait, tag, state, leader, party, focus-tree, decision, idea, AI, formable, GUI, map, or event source was changed. No new identifier was registered. Nothing was staged or committed.

## Next bounded patch sequence

1. The parent/identity owner must choose one explicit source route: a grounded colonial/provisional government identity, an Abomey institutional/council identity, or a clearly marked alternate-history civic route. Do not silently blend a person, court, territory, and later state identity.
2. Resolve the opening 1936 flag/emblem with an accepted source and redistribution-rights record, exact cosmetic tag/basename, and route-specific provenance. Reject vanilla modern/tricolor substitutes unless the source-of-truth owner explicitly accepts them.
3. Route the selected grounded person or institution to `chaosx_portrait_creator`. Resolve Casimir's exact name/office or institutional naming, source rights, portrait consumer, archive crop/path mismatch, HOI4 placeholder, GFX entry, runtime DDS, and manifest before setting identity rights cleared. Do not generate a fictional substitute for a missing grounded source.
4. After those inputs are accepted, the central owner must add the IW-095 adapter, content attestation, preflight, publisher, and Join receipt, plus an explicit origin-safe guard/cleanup boundary against Event 012's DAH host playbook and state `776` use. Parent roster publication must satisfy `independence_wave_dah_roster_checkpoint`.
5. Add only the bounded DAH shared-focus callback and any accepted Form-24/formable gate, then wire the already-present package-local setup to the central lifecycle. Preserve the `776` rebind and `RG-NIGERIA-COARSE` uniqueness checks.
6. Run fresh static checks and the required Event, focus, map, GUI, technology, and probability MCP inspections. Any AI/weight change requires the probability auditor baseline and same-scenario `hoi4.probability_compare`; then the parent may review final admission.

## Simplifications, omissions, and blockers

No simplification or fallback was used. Identity, flag, emblem, portrait, map binding, leader, formable, central adapter, Join receipt, and gameplay setup were intentionally omitted because the accepted research inputs and current runtime/MCP evidence do not clear them. The package remains incomplete and fail-closed; this handoff is the bounded next patch rather than a promotion claim.
