# Event 006 next package admission audit: IW-177 Fiji

Date: 2026-08-03.

Scope: identify the safest next non-overlay Event 006 country package, compare its package evidence with the current admission authority, and patch only a narrow package defect if all required evidence is accepted.

Disposition: **no safe admission and no gameplay patch.** IW-177 Fiji is the strongest next non-overlay candidate by static package completeness, but its source and formable gates are still closed. The content-attestation allowlist remains unchanged.

## Executive verdict

The current authoritative content-attestation set is fourteen packages: IW-001 `SCO`, IW-002 `WLS`, IW-004 `BRI`, IW-006 `AFX`, IW-007 `AGX`, IW-008 `RHI`, IW-009 `BAY`, IW-010 `AJX`, IW-012 `ICE`, IW-017 `COR`, IW-018 `ARX`, IW-019 `ASX`, IW-173 `HAW`, and IW-184 `HBX`.

IW-177 is the recommended next candidate because it reuses vanilla `FIJ`, has one compact anchor, and already has country, politics, leader, focus, decisions, ideas, force, AI, localisation, cleanup, and FORM-39 source surfaces. It cannot be admitted yet because the grounded leader evidence is not accepted for the 1936 baseline and the exact FORM-39 dependency has unresolved named-member, identity, flag, and route inputs.

The current normal and scenario dispatch registries already contain IW-177 as an adapter/preflight candidate, but `has_independence_wave_runtime_package_content_attestation_for_execution_id` intentionally omits `constant:independence_wave_package_id.iw_177`. Adding it would bypass unresolved evidence and is not authorized.

## Candidate comparison

| Candidate | Static package evidence | Blocking admission evidence | Decision |
| --- | --- | --- | --- |
| IW-177 Fiji (`FIJ`) | Vanilla carrier, state `636`, `RG-PACIFIC-ISLANDS`, six package focuses, six decisions, 250-day mission, three lifecycle ideas, dynamic force row, AI, localisation, cleanup, and bounded FORM-39 adapter. | Sukuna source is catalogued circa 1940s against the 1936 baseline; Vishnu Deo is a review-only 1929 alternative with an unresolved 1936 office-role decision; FORM-39 still lacks accepted PNG/WPG research writers, MFX X-tag/identity/flat-flag readiness, and route-adapter inputs. | **Recommended next candidate, still HOLD.** |
| IW-030 Montenegro (`MNT`) | Vanilla carrier, state `105`, `RG-105`, politics, decisions, mission, ideas, AI, force profile, localisation, and a narrow preflight wrapper. | MNT leader identity/rights evidence remains `needs_user_review`; no accepted runtime portrait promotion; vanilla MNT has no `1936` OOB and force materialisation is unperformed. | Do not admit or patch. |
| IW-014 Catalonia (`CAT`) | Vanilla carrier, state `165`, `RG-165`, Lluís Companys, full-framework minimal-tree package, decisions, ideas, AI, localisation, and bounded FORM-07 adapter. | FORM-07 still needs a source-approved Iberian X identity, complete flag package, identity review, and complete NAV/GLC runtime adapters; fresh runtime/focus proof is open. | Do not admit or patch. |

## IW-177 country-package coverage checklist

| Surface | Status | Evidence and concrete identifiers |
| --- | --- | --- |
| Tag and package identity | Source pass; runtime closed | Vanilla `FIJ` maps to `countries/Fiji.txt`; `is_independence_wave_fij_package` requires original tag `FIJ`, an active Event 006 country, and `constant:independence_wave_package_id.iw_177`. No new gameplay tag is created. |
| Registration and binding | Source pass | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row `IW-177,Fiji,...,FIJ,...,636,Fiji,RG-PACIFIC-ISLANDS`; `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` row `IW-177` binds anchor `636` and former host `ENG`. |
| Map and state setup | Source pass; live proof open | Vanilla `history/states/636-Fiji.txt` is the sole anchor with provinces `4286`, `7302`, `12159`, victory point `4286`, infrastructure `2`, naval base `1`, local supply `0`, owner `ENG`, and core `FIJ`; package setup requires FIJ ownership/control, capital `636`, a living non-FIJ former host, and the protected host pointer. |
| Country history and starting setup | Bounded vanilla baseline | Vanilla `history/countries/FIJ - Fiji.txt` sets capital `636`, infantry weapons level `1`, twenty convoys, democratic politics, 1936 elections, and no OOB; the package does not add a large static army or map rewrite. |
| Politics and parties | Source pass | `independence_wave_initialize_fij_politics` in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` applies democratic authority, elections, four FIJ party names, popularity `44/12/34/10`, and centrism leadership. |
| Leader and portrait | Conditional blocker | `FIJ_independence_wave_founding_congress_chair` in `common/characters/006_independence_wave_pacific_characters.txt` is male, promotes centrism, and consumes `GFX_portrait_FIJ_independence_wave_founding_congress_chair`; the current DDS consumer is provisional because the strongest Sukuna source is dated circa 1940s. |
| Flags | Pass for FIJ; FORM-39 pending | Vanilla FIJ normal, medium, and small ideology flag triplets are reused. No historical FIJ flag is invented. MFX normal/medium/small assets exist, but the MFX identity and flat-flag readiness remains review-closed. |
| Advisors, operatives, commanders, and name pools | Pass for current scope | IW-177 defines no advisor, operative, commander, high-command, dossier, small portrait, or opposite-gender random-name pool. The one-person leader is explicitly male. |
| Focus framework | Source pass; live layout proof open | IW-177 initializes only from vanilla `generic_focus`, assigns `independence_wave_focus_assignment.full_framework`, and loads `independence_wave_focus_tree`; cleanup restores `generic_focus`. The six package focus IDs are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus`. |
| Decisions and mission | Source pass | `independence_wave_fij_founding_congress_category` exposes the 250-day `independence_wave_fij_hold_constituent_congress_together` mission and six staged decisions with central costs, cancellation, timeout, host-loss, and project-failure handling. |
| Ideas and ledgers | Source pass | `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact` form the lifecycle; setup exposes congress pressure, communal authority, shipping access, colonial accounts, and defense readiness. |
| Force and starting military | Source pass; materialisation unperformed | `common/script_constants/006_independence_wave_force_package_constants.txt` records IW-177 profile `5` (`coastal_maritime`), military tradition/force level `53`, reinforcement mask `659`, navy-only inheritance mask `1`, and research sensitivity `0`; `independence_wave_apply_dynamic_starting_force` is guarded by the Pacific command structure and command-roster readiness. |
| Technology, industry, supply, production | Bounded baseline; tooling limitation | Vanilla FIJ preserves infantry weapons `1`, infrastructure `2`, naval base `1`, local supply `0`, twenty convoys, and no industrial windfall. The installed package exposes no Technology Tree Viewer, so technology prerequisite and unlock rendering remains unresolved rather than being claimed complete. |
| AI and playability | Source pass with open balance evidence | `common/ai_strategy/006_independence_wave_pacific.txt` defines `independence_wave_fij_coastal_congress_survival`, `independence_wave_fij_founding_restraint`, and `independence_wave_fij_host_threat`; priorities cover army, infantry/support, convoys, fuel, infrastructure, dockyard, and coastal defense. One-state island resilience, generic-framework ordering, and post-release timing are not live-proven. |
| Diplomacy and former-host behavior | Source pass | FIJ installs host negotiation, guarded-frontier, association, reclamation, ambition, and league surfaces; the colonial-account project requires a living former host and does not transfer territory or start an automatic war. |
| FORM-39 dependency | Implemented but fail-closed | FIJ selects `constant:independence_wave_formable_family.melanesian_federation`; exact members are FIJ/IW-177/state `636`, PNG/IW-178/state `523`, and WPG/IW-157/state `669`. Named route, member research, X-tag, flat-flag, identity-review, consent, and collision inputs remain unset or `needs_user_review`. |
| Cleanup and rollback | Source pass | `independence_wave_cleanup_iw_177_fiji` removes FIJ mission, decisions, ideas, ledgers, flags, route selection, focus ownership, and the Event 006 leader; FORM-39 cleanup clears its runtime receipt without erasing external research or identity evidence. |
| Dispatch and attestation | Correctly blocked | IW-177 is present in `has_independence_wave_runtime_package_adapter_for_execution_id` and the scenario preflight branch, but absent from `has_independence_wave_runtime_package_content_attestation_for_execution_id`; normal and scenario release therefore stop before mutation. |

## File-surface checklist

- Country and setup: `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` and `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` define `is_independence_wave_fij_package`, `can_initialize_independence_wave_iw_177_package`, `has_prepared_independence_wave_iw_177_package`, `independence_wave_setup_iw_177_fiji`, and `independence_wave_cleanup_iw_177_fiji`.
- Reservation and map: `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt` and `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt` define `independence_wave_load_package_iw_177`, `independence_wave_reserve_package_iw_177`, `can_plan_independence_wave_package_iw_177`, state `636`, and `RG-PACIFIC-ISLANDS`.
- Politics and tuning: `common/script_constants/006_independence_wave_pacific_constants.txt` and `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` define FIJ popularity `44/12/34/10`, pressure start/stable values `31/62`, five ledgers, and mission duration `250`.
- Leader and portrait: `common/characters/006_independence_wave_pacific_characters.txt`, `interface/006_independence_wave_pacific_portraits.gfx`, `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds`, and hidden recruitment event `chaosx.nr6.350` define the male leader consumer. The DDS is a provisional consumer, not accepted evidence for admission.
- Focus: `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/006_independence_wave_pacific_focus.txt`, and `common/scripted_effects/006_independence_wave_focus_effects.txt` define the full-framework assignment and six FIJ focuses.
- Decisions and ideas: `common/decisions/categories/006_independence_wave_pacific_categories.txt`, `common/decisions/006_independence_wave_pacific_decisions.txt`, and `common/ideas/006_independence_wave_pacific_ideas.txt` define the founding category, mission, six decisions, and three lifecycle ideas.
- Force and AI: `common/script_constants/006_independence_wave_force_package_constants.txt`, `common/scripted_effects/006_independence_wave_force_effects.txt`, and `common/ai_strategy/006_independence_wave_pacific.txt` define the IW-177 force row and FIJ AI profiles.
- Localisation and assets: `localisation/english/006_independence_wave_pacific_l_english.yml`, `localisation/english/006_independence_wave_formable_registry_l_english.yml`, the vanilla FIJ flag triplets, and `docs/assets/006_independence_wave/form39_melanesian_federation_identity_2026_07_27/` provide the current player-facing and formable asset surfaces.
- FORM-39: `common/scripted_triggers/006_independence_wave_form39_triggers.txt`, `common/scripted_effects/006_independence_wave_form39_effects.txt`, `common/decisions/categories/006_independence_wave_form39_categories.txt`, `common/decisions/006_independence_wave_form39_decisions.txt`, and `common/ideas/006_independence_wave_form39_ideas.txt` define the exact member, identity, readiness, consent, integration, project, and cleanup contract.
- Dispatch authority: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` defines the adapter, preflight, scenario, and content-attestation branches. The content-attestation OR block is the authoritative admission surface and has no IW-177 entry.

## Missing or stale surfaces

The following inputs are intentionally not written by FIJ setup and therefore cannot be inferred from the presence of package scripts: `independence_wave_fij_melanesian_route_adapter_complete`, `independence_wave_fij_melanesian_member_research_complete`, `independence_wave_png_melanesian_member_research_complete`, `independence_wave_wpg_melanesian_member_research_complete`, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, and `independence_wave_form39_identity_review_complete`.

IW-178 PNG and IW-157 WPG remain research HOLDs with no accepted named-community containment, rights-cleared period leadership or institutional evidence, community-specific symbols, or runtime package proof. Generic Papua, New Guinea, or pan-Melanesian substitutes are not authorized.

The MFX normal, medium, and small TGAs are present, but the identity manifest and graphics handoff remain `needs_user_review`; their presence is not an identity approval or runtime fallback.

The strongest Sukuna source is `docs/assets/006_independence_wave/sources/fij_sukuna/commons_ratu_sir_lala_sukuna.jpg`, whose National Archives of Fiji metadata records circa 1940s. The 1929 Vishnu Deo evidence under `docs/assets/006_independence_wave/sources/fij_vishnu_deo_2026_08_01/` is period-valid but its founding-congress-chair role and independent asset/rights review remain unresolved. It must not silently replace Sukuna.

## Admission proof and validation

No files, tags, states, leaders, parties, focus IDs, decision IDs, idea IDs, localisation keys, formable IDs, allocator rows, dispatch allowlists, or attestation entries were changed in this audit.

Before this handoff, the package gate was source-connected but fail-closed. After this handoff, it is unchanged: IW-177 remains an adapter/preflight candidate and cannot mutate a release or scenario because it is absent from the content-attestation OR block.

Task-specific checks run on 2026-08-03:

- `python -B .tools/audit_event6_allocator.py` passed with `149` publishers, `126` automatic/high-chaos selectable packages, `138` SCN-008 ranked packages, `14` attested packages, `13` compatible reservation groups, and automatic counts `6 / 8 / 10 / 14 / 20` with World Collapse `20`.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all `32` SCN-008 intensity/type cells and `8` edge cases.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` reported `136` protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one skipped random-event root.

The following meaningful evidence remains skipped because it belongs to the parent or player-owned runtime boundary: live allocator reservation, host-survival mutation, force materialisation, focus rendering, AI timing, save/load rollback, FORM-39 consent execution, and Technology Tree Viewer inspection. The installed package currently exposes no Technology Tree Viewer, so that limitation is recorded rather than hidden.

## Remaining blockers and next action

FIJ should remain the next candidate in the admission queue, but no parent gate change is safe until both blocker groups are independently closed: (1) an accepted 1936-compatible grounded FIJ leader source/role decision with final runtime asset review, and (2) accepted FORM-39 PNG/WPG package research, MFX X-tag reservation, flat-flag review, identity review, route-adapter writers, collision recheck, and static/runtime proof.

Once those receipts exist, the parent should rerun the FIJ package audit, the full Event 006 source-of-truth reconciliation, allocator and scenario checks, and the parent-owned runtime transaction review before adding IW-177 to the content-attestation OR block.

## Simplifications, omissions, and blockers

No fallback portrait, invented flag, generic member package, shallow replacement focus tree, new gameplay tag, broad formable change, or unrelated Event 006 patch was introduced. No simplification was approved or used. The package remains incomplete for admission because the unresolved source, formable, and runtime evidence above is required by the existing fail-closed contract.

## Source authority

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_completion_evidence_v102_2026_08_02.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fij_package_audit_v91_2026_08_02.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fij_package_closure_v88_2026_08_01.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fij_sukuna_source_research_v50_2026_08_01.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fij_vishnu_deo_repaint_evidence_v109_2026_08_03.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form39_completion_reconciliation_v17_2026_07_27.md`.
- Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/636-Fiji.txt` and `history/countries/FIJ - Fiji.txt`.
