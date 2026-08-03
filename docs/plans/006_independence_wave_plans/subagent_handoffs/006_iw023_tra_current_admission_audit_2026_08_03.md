# Event 006 IW-023 TRA current admission audit

Date: 2026-08-03

Package: `IW-023`

Country: `TRA` (vanilla Transylvania)

Audit status: **HOLD - source contracts are repaired, but IW-023 is not admitted and runtime content is not attested.**

## Authority and scope

This audit uses `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_completion_evidence_v105_2026_08_03.md` and `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw023_tra_postrepair_audit_2026_08_03.md` as the current authority.

The older additive-package audit and the obsolete flag-log report were not used as current evidence.

Offline Paradox Wiki core pages and the relevant country, focus, decision, idea, AI, state, map, and division pages were consulted before this audit.

Vanilla documentation consulted includes `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, and `documentation/script_concept_documentation.md`.

Vanilla precedents inspected were `history/countries/TRA - Transylvania.txt`, `common/characters/TRA.txt`, and `common/national_focus/austro_hungarian_releasable_shared.txt`.

## Decision and safe-patch boundary

No gameplay patch is warranted.

The current source already contains the repaired planner gate, roster checkpoint, additive focus carrier, carrier-scoped FORM-08 readiness adapter, force mapping, AI profile, decision cleanup, and localisation surfaces.

Adding `IW-023` to the runtime content-attestation OR-set would be an admission change rather than a narrow package repair, and would assert evidence that the current authority explicitly says is absent.

No new tag, AXX/MAC member claim, map rewrite, fallback identity, portrait, flag, focus tree, or balance change was introduced.

## Country package coverage checklist

| Surface | Current evidence | Result / remaining risk |
| --- | --- | --- |
| Tag and registry | Vanilla `TRA` is preserved; no mod tag is redefined. `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt:9-18` calls `is_independence_wave_exact_package_iw_023_tag_available`. | Source-ready; not attested for runtime execution. |
| Planner admission | `can_plan_independence_wave_package_iw_023` requires an open plan, free slot, unused package and reservation group, `TRA` exact-tag availability, and state 84 anchor availability. | Repaired contract passes source review; no planner runtime proof. |
| Map and states | Current binding is anchor state `84` (Transylvania), compact state `76` (North Transylvania), former host `ROM` state `46`, reservation `RG-DANUBE-BORDERLAND`; no event-specific map rewrite is present. | Source/map binding is coherent; transfer, capital, supply, and save/load runtime evidence is absent. |
| Vanilla roster and leader | Vanilla `history/countries/TRA - Transylvania.txt:1,66,72-78` has capital 84, democratic ruling party, and ruling leader `Iuliu Maniu` with `GFX_portrait_Iuliu_Maniu`. `events/006_independence_wave.txt:166-186` records `independence_wave_tra_vanilla_roster_checkpoint` only when that ruling roster is present. | Roster checkpoint is source-correct; no live country setup attestation. |
| Portraits, flags, and identity | The package preserves vanilla TRA portraits and does not add a grounded fictional portrait. FORM-08 reuses existing `HUN_EMPIRE` in `common/countries/cosmetic.txt:98-101`; no new tag or flag package is added. | No portrait/flag pairing defect found; HUN identity remains transaction-gated. |
| Politics and parties | `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:252-299` preserves vanilla history, adds missing starting laws only, initializes ledgers, and exposes five government routes plus four host routes. | Source wiring is present; route balance and political survival are not runtime-tested. |
| Focus carrier | `common/national_focus/austro_hungarian_releasable_shared.txt:1-38` keeps `austro_hungarian_releasable_focus` as the TRA carrier and includes the eight reviewed shared overlay IDs. `common/national_focus/006_independence_wave_focus.txt:3347-3473` gates the overlays with `can_use_independence_wave_additive_focus_overlay`. | Additive carrier scope is source-correct; no rendered or live focus-tree evidence. |
| Focus dispatch contract | TRA setup assigns `additive_overlay` at `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:270-272`; final validation requires `has_independence_wave_generic_focus_contract` at `:308-316`. | No blind generic-tree load found. |
| Decisions and mission | `common/decisions/006_independence_wave_transylvania_decisions.txt:13-222` defines category `independence_wave_tra_danube_council_category`, one timed mission, and eleven decisions with authored costs, cancellation, timeout, and AI behavior. `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:326-355` removes the mission with `remove_mission` and the eleven decisions with `remove_decision`. | Cleanup is syntactically and semantically aligned with vanilla documentation; no runtime cleanup receipt. |
| Ideas and lifecycle | `common/ideas/006_independence_wave_transylvania_ideas.txt:29-106` defines the seven TRA package ideas. `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:10-36` removes and refreshes crisis/stable lifecycle ideas. | Coverage is present; lifecycle timing is not live-tested. |
| Starting forces and reinforcement | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` maps IW-023 to mountain infantry and defecting regulars, profile `mountain_frontier`, tradition score `68`, no navy/air inheritance, and five named reinforcement paths. The setup loads the mapping and applies the dynamic starting force at `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:289-290`. | Source mapping is coherent; no runtime unit count, equipment, supply, or survival receipt. |
| Technology, industry, supply, production | Setup adds `civilian_economy`, `export_focus`, and `volunteer_only` only when missing at `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:259-261`; no OOB/history factory rewrite is used. | Narrow starting setup is present; technology, production, fuel, train, and supply behavior are not runtime-attested. |
| AI and playability | `common/ai_strategy/006_independence_wave_transylvania.txt:21-68` provides TRA frontier survival, former-host restraint, settled-frontier, and emergency-commission strategies gated by package flags. `common/ai_strategy/006_independence_wave_form08.txt:17-51` covers post-formation FORM-08 behavior. | Source AI wiring is present; no seeded survival or focus/decision selection run exists. |
| Localisation and assets | `localisation/english/006_independence_wave_transylvania_l_english.yml:13-29` covers TRA ideas and decision category, with the action and tooltip keys continuing through the file. Existing decision/focus icons are reused. | No missing TRA package surface was found in the inspected localisation; no visual runtime proof. |
| FORM-08 / identity | `common/scripted_effects/006_independence_wave_form08_effects.txt:11-40` registers readiness only for active TRA with anchor 84 owned/controlled and capital 84, then records HUN identity reuse. `common/scripted_triggers/006_independence_wave_form08_triggers.txt:85-119` requires minimum member, consent, and anchor counts before mutation. | Fail-closed as intended, but FORM-08 remains blocked until the frozen minimum three-member/three-consent/three-anchor evidence exists; AXX and MAC are not automatically admitted. |
| Cleanup and rollback | TRA cleanup at `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt:326-355` removes package mission, decisions, ideas, ledgers, lifecycle, roster, AI, and route state; shared generation cleanup owns shared formable/focus/relationship/origin cleanup. FORM-08 has its own identity rollback/cleanup helpers. | Source cleanup coverage is present; no save/load cleanup proof. |
| Runtime content attestation | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:73-90` attests only IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-017, IW-018, IW-019, IW-173, and IW-184. IW-023 is absent. | **Blocking admission defect.** Promotion requires a separate accepted TRA package audit and attestation update. |

## File-surface checklist

Reviewed source surfaces are:

- `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt` for setup, ledger lifecycle, routes, force loading, AI flag, final validation, and cleanup.
- `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt` for exact tag availability, roster, prepared setup, runtime readiness, and cleanup guards.
- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt` for planner admission.
- `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt` for IW-023 load, reservation, and automatic-pool ordering.
- `events/006_independence_wave.txt` for `chaosx.nr6.350` roster checkpoint.
- `common/national_focus/austro_hungarian_releasable_shared.txt` and `common/national_focus/006_independence_wave_focus.txt` for the vanilla carrier and eight shared overlays.
- `common/scripted_effects/006_independence_wave_form08_effects.txt`, `common/scripted_triggers/006_independence_wave_form08_triggers.txt`, and the formable registry helpers for FORM-08 readiness, identity, integration, commit proof, and cleanup.
- `common/decisions/006_independence_wave_transylvania_decisions.txt` and `common/decisions/categories/006_independence_wave_transylvania_categories.txt` for the mission/decision surface.
- `common/ideas/006_independence_wave_transylvania_ideas.txt` for package ideas.
- `common/ai_strategy/006_independence_wave_transylvania.txt` and `common/ai_strategy/006_independence_wave_form08.txt` for AI behavior.
- `localisation/english/006_independence_wave_transylvania_l_english.yml` for TRA player-facing strings.
- `docs/plans/006_independence_wave_plans/006_current_installed_map_package_bindings.csv` and `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` for current map and force evidence.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` for the compile-time runtime-content attestation gate.

## Findings by required audit area

### Map and state setup

No source-level state or map defect was found for the current compact package: anchor `84`, compact `76`, and former-host protection `ROM:46` match the installed binding.

No map write was performed because the current task is an admission audit and the binding is already present.

The remaining risk is runtime ownership/control transfer, capital retention, supply, railway, and release cleanup, none of which can be claimed from static source inspection.

### Politics, leader, portrait, flag, advisor, and party

TRA remains the vanilla country with Iuliu Maniu as the ruling leader and no new fictional or opposite-gender portrait pairing.

The package route effects and party names are localised, and no advisor or high-command replacement is required by the current design.

The remaining risk is runtime ideology/party state after setup and route choices.

### Focus, decision, idea, and asset

The additive carrier preserves the vanilla Austro-Hungarian releasable tree and does not call `load_focus_tree` for TRA.

The mission uses `days_mission_timeout`, and the active-project trigger uses `has_decision`, which matches the documented active-decision trigger while cleanup uses the documented `remove_mission` effect.

All seven package ideas, the TRA decision category, the twelve action keys, and the reviewed reused icons are present in source.

No focus render, live decision completion, or asset-runtime evidence was available.

### Forces, technology, industry, supply, and production

The force mapping is the intended mountain-frontier profile with no navy or air inheritance and with secure-depot, defecting-host, regional-guard, terrain-unit, and professional-officer pathways.

Starting economic laws are narrow and conditional; no unsupported OOB or factory-history edits were found.

Runtime unit creation, equipment stockpiles, technology state, production, fuel, supply, and AI survival remain unverified.

### AI and playability

TRA has package-gated frontier survival and restraint strategies, and FORM-08 has post-formation corridor, charter-restraint, and settled-confederation strategies.

No seeded AI selection, survival, war, supply, or save/load test is available, so the package cannot be promoted on AI claims alone.

## Validation receipts

The following current static checks passed on 2026-08-03:

- `python -B .tools/audit_event6_allocator.py` passed with Event 006 attested count `14` and automatic ladder `6 / 8 / 10 / 14 / 20`.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and 8 edge cases.
- `python -B .tools/audit_event6_flags.py --strict` passed `102/102` complete flag families.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` passed with zero external country-definition or identity-surface collisions.
- Vanilla documentation checks confirm `has_decision` tests an active selected decision, `remove_decision` removes an active decision, `remove_mission` removes a mission without completion/timeout effects, and `load_focus_tree` is the tree replacement effect that TRA intentionally does not use.

Skipped meaningful validation: no Hearts of Iron IV launch, no MCP runtime/render session, no live planner execution, no release/transfer/capital/supply test, no seeded AI survival test, and no save/load cleanup test were available or permitted for this audit.

## Blockers, simplifications, and handoff

The compile-time runtime-content attestation set still excludes `IW-023`; this is the immediate admission blocker.

FORM-08 remains fail-closed until the frozen minimum three members, three consents, and three anchors are independently evidenced; AXX and MAC are not admitted by assumption.

No fallback, simplification, generic replacement tree, invented tag, invented portrait, invented flag, or lower gate was used.

Changed files: this handoff only; no gameplay file, tag, state, leader, party, focus-tree ID, localisation key, force ID, or formable ID was changed.

Next safe step: after an independent TRA package admission review accepts source setup, force, AI, current-map, cleanup, and asset evidence, update the attestation set in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` through the parent-owned admission process and rerun the Event 006 audits.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw023_tra_current_admission_audit_2026_08_03.md`.
