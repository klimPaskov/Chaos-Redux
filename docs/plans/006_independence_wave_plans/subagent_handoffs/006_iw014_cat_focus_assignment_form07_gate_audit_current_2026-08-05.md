# IW-014 CAT focus assignment and FORM-07 gate audit

Date: 2026-08-05 (Europe/Kyiv).

Scope: current-source audit after the IW-014 standalone admission edits. This handoff verifies full shared-tree assignment, CAT package-focus reachability, and FORM-07 late-binding safety. It does not change gameplay files, assets, or runtime wiring.

## Verdict

The standalone CAT admission is coherent at source level. CAT receives the full `independence_wave_focus_tree`, its six CAT package focuses have reachable prerequisite paths under the documented CAT package, and the generic formable branch remains fail-closed until the complete family commit-readiness contract passes. No gameplay patch is required.

FORM-07 itself remains unavailable in the current source because its identity contract is deliberately absent and NAV/GLC remain outside content attestation. This is the expected late-binding result, not a CAT admission defect.

## Full shared-tree assignment

| Contract | Current source evidence | Result |
| --- | --- | --- |
| Exact CAT carrier | `common/scripted_triggers/006_independence_wave_package_triggers.txt:114-117` requires the available origin to retain `original_tag = CAT`; `006_independence_wave_triggers.txt:515-522` binds IW-014 to CAT and anchor 165. | Pass |
| Setup identity and package proof | `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:8-35` checks active CAT, IW-014 package id, Mediterranean-Iberia region, regional depth, industrial-breakaway archetype, anchor state 165, former host, and `CAT_lluis_companys`. | Pass |
| Full focus input | `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:308-350` sets `independence_wave_focus_assignment_input = ...full_framework` at line 319 and calls `independence_wave_assign_focus_framework` at line 320. | Pass |
| Engine tree load | `common/scripted_effects/006_independence_wave_focus_effects.txt:33-63` clears opposite ownership flags, sets `independence_wave_full_focus_framework` and `independence_wave_generic_focus_tree_assigned`, then calls `load_focus_tree = { tree = independence_wave_focus_tree }`. | Pass |
| Setup receipt | `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:98-183` requires the full-framework flag, the full-framework assignment value, all CAT route/host/network flags, force mapping, CAT AI, and lifecycle receipts before `has_complete_independence_wave_iw_014_package_setup` can pass. | Pass |
| Final focus barrier | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:33-62` dispatches CAT final validation and rejects a selected package unless `has_independence_wave_generic_focus_contract = yes` and `independence_wave_generic_ai_profile` are present. | Pass |
| Runtime/scenario attestation | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:11-36,93-100,204-206,325-327` includes IW-014 in the adapter allowlist, central content attestation, automatic preflight, and SCN-008 scenario preflight. | Pass |

## CAT package-focus reachability

The shared tree resolves the CAT branch as six `shared_focus` nodes at `common/national_focus/006_independence_wave_focus.txt:3703-3792`. Every node has a title, description, icon, completion tooltip, reward hook, and AI block in current localisation/source. Prerequisite semantics follow the national-focus contract: the two separate prerequisite blocks on `independence_wave_cat_settle_iberian_charter_focus` are AND-gates.

| Focus id | Prerequisites | Additional availability | Reward/helper | Reachability |
| --- | --- | --- | --- | --- |
| `independence_wave_cat_secure_barcelona_port_focus` | `independence_wave_prepare_capital_administration` | `allow_branch` requires CAT package + full framework; available requires CAT package | `independence_wave_cat_focus_secure_port` | Reachable after the shared survival root and CAT setup |
| `independence_wave_cat_integrate_factory_workers_focus` | CAT secure-port focus | CAT package | `independence_wave_cat_focus_integrate_workers` | Reachable after first CAT focus |
| `independence_wave_cat_reconcile_assembly_focus` | `independence_wave_prepare_first_assembly` | CAT package | `independence_wave_cat_focus_reconcile_assembly` | Reachable after founding settlement and assembly preparation; assembly preparation may precede any mutually-exclusive government commitment |
| `independence_wave_cat_settle_iberian_charter_focus` | CAT integrate-workers AND CAT reconcile-assembly | CAT package + `has_independence_wave_living_former_host` | `independence_wave_cat_focus_settle_host` | Reachable on the living-host settlement path after both CAT prerequisites |
| `independence_wave_cat_open_mediterranean_corridor_focus` | CAT Iberian-charter focus | CAT package + `independence_wave_network_member` | `independence_wave_cat_focus_open_mediterranean_network` | Reachable after activation registers CAT in the shared network registry |
| `independence_wave_cat_ratify_catalan_sovereignty_focus` | CAT Mediterranean-corridor focus | CAT package + stable CAT compact + `has_independence_wave_cat_route_government` | `independence_wave_cat_focus_ratify_sovereignty` | Reachable after one CAT route government decision and stable ledgers |

The CAT setup registers all five shared government route flags (`...council`, `...constitutional`, `...traditional`, `...emergency`, `...patron`) at `006_independence_wave_catalonia_package_effects.txt:321-331`; route-government completion remains CAT-decision-owned. The network member flag is written by the shared activation path at `common/scripted_effects/006_independence_wave_effects.txt:794-817,1988-2012`, after package setup succeeds. This preserves the intended order instead of exposing the CAT network focus on a dormant package.

## FORM-07 late-binding gate

The CAT standalone setup intentionally registers only Iberian family metadata. `has_independence_wave_cat_formable_registration` at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:42-47` checks family-selected/profile-loaded receipts but does not assert formable commit readiness. CAT setup calls this registration through `independence_wave_focus_register_formable_family` at `006_independence_wave_catalonia_package_effects.txt:335-337`.

The shared formable focus branch is now correctly protected by `can_open_independence_wave_formable_branch` at `common/scripted_triggers/006_independence_wave_focus_triggers.txt:326-334`, which requires full framework, family registration, regional power phase, and `has_independence_wave_formable_commit_readiness = yes`. The generic discovery trigger independently repeats the commit-readiness requirement at `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:63-78`.

`has_independence_wave_formable_commit_readiness` at `006_independence_wave_formable_registry_triggers.txt:533-600` requires the selected/profile family match, identity compatibility, territory adapter, X-tag reservation, complete flag package, identity adapter, integration adapter, member-policy audit, and the family-specific attestation. The Iberian branch at lines 569-572 additionally requires `independence_wave_form07_readiness_attested`.

FORM-07 cannot currently set that receipt: `common/scripted_triggers/006_independence_wave_form07_triggers.txt:194-208` requires the three identity-contract flags (`independence_wave_form07_identity_attested`, `...x_tag_reserved`, `...flag_package_ready`) before registration; `common/scripted_effects/006_independence_wave_form07_effects.txt:22-34` sets generic readiness only inside that guarded block, and the current source contains no setter for those identity flags. Thus CAT family registration does not leak into formable discovery.

The CAT Mediterranean focus helper adds a second guard at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:288-296`: it always records the CAT corridor/ambition rewards, but sets `independence_wave_unlock_formable_discovery` only when `has_independence_wave_formable_commit_readiness = yes`. This closes the late-binding path even if the CAT package focus is completed before FORM-07 is researched.

## Validation

- Current `hoi4.focus_inspect` artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee8dae46d997650b70501e5dd9e8cfd7cb7a6b0f154eceeba5417e3661c69b0d/d867309b1b2665522cd5662ea38ecd5db359e42e76deee79cb74d53a97bbfc67/focus-inspect.51b6f20b9745702f.json`. It resolves one `independence_wave_focus_tree` with 184 focuses, 193 connectors, zero crossings, zero node intersections, zero too-close pairs, and one intentional long CAT-unrelated military connector warning. The 14 blocking icon diagnostics and one vanilla continuous-focus localisation warning are installed-game sources outside Event 006.
- `python -B .tools/audit_event6_allocator.py` passed with 16 attested packages and 15 compatible reservation groups; IW-014 is included in the current central attestation set.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases; current scenario preflight source includes IW-014 exact CAT availability.
- Targeted current-source scan found all six CAT focus IDs with exact title/description keys, icons, completion rewards, custom tooltip keys, and AI blocks; assignment, attestation, readiness, and CAT-network guards all resolve to existing identifiers.

## Remaining risks and non-goals

- FORM-07 remains fail-closed until a reviewed X-ending identity, flag triplet, territory/member/integration adapters, and NAV/GLC package attestation are accepted. No identity or flag fallback was inferred.
- The audit is source/static only. Live focus visibility, save/load, supply/force inheritance, AI timing, and runtime transaction observation remain user-owned QA and were not claimed.
- Descendant CAT shared-focus nodes rely on the loaded full framework and CAT package predicates rather than repeating the root `allow_branch` condition. The final-validation barrier and CAT setup receipt make that ownership safe in the current path; if a future adapter changes cleanup/order, rerun this audit before promotion.

No gameplay files were changed. This handoff is the only file written by this audit.
