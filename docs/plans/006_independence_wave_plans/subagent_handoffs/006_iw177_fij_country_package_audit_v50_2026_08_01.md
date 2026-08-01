# IW-177 Fiji country-package audit v50

Date: 2026-08-01

Scope: FIJ/IW-177 only. This audit covers the current country package against the accepted Event 006 complete-package contract, including identity, setup, map safety, politics, forces, ideas, visible values, AI, diplomacy, host survival, regional ambition, focus and decision wiring, FORM-39 readiness, cleanup, existing-tree preservation, and dispatch gates. It does not implement FORM-39 admission, alter any asset-research file, edit another country package, or weaken a source or portrait gate.

## Result

FIJ is a broad, internally connected gameplay tranche with a safe compact map binding and a coherent founding-congress package, but it remains runtime-closed by design. The current FIJ package is not content-attested and must not be admitted until the Sukuna source/date decision, the researched PNG/WPG member packages, MFX identity review, collision/readiness proofs, and the remaining static/runtime evidence are accepted.

One bounded correctness patch was made in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`. The IW-177 setup effect no longer writes `independence_wave_fij_melanesian_route_adapter_complete`; the flag is left unset, and any future writer must be readiness-owned after all named FORM-39 gates pass. FIJ cleanup still clears the flag. The parent-owned `prepare_fsm`/`prepare_fij` hidden-event recruitment edits in the same file were preserved and are not part of this patch.

## Country-package coverage checklist

| Surface | Status | Evidence and exact risk |
| --- | --- | --- |
| Tag and package identity | PASS, runtime closed | Registered vanilla `FIJ` is bound to `constant:independence_wave_package_id.iw_177 = 177`; `is_independence_wave_fij_package` requires original tag FIJ, active-country status, and IW-177. |
| Compact anchor and reservation | PASS | IW-177 reserves only state `636` in `RG-PACIFIC-ISLANDS`; the region-13 loader and reservation effect use FIJ/636 exactly. FIJ, SAM, and FSM share this group, so only one automatic package may be selected from the group. |
| Host and map survival | PASS with live proof open | `can_initialize_independence_wave_iw_177_package` requires state 636 owned and controlled by FIJ, a living non-FIJ former host, and capital state 636. The protected English host state/capital contract is revalidated through the shared host pointer. No extended territory or map rewrite is added. |
| Politics and parties | PASS at source | Setup sets democratic rule and elections, applies FIJ constants `44/12/34/10` for democratic/communist/neutrality/fascist popularity, installs four localized party names, and promotes the centrism Sukuna leader. |
| Leader and portrait | CONDITIONAL / blocker | `FIJ_independence_wave_founding_congress_chair` is a male country leader localized as Ratu Sir Lala Sukuna and wired to `GFX_portrait_FIJ_independence_wave_founding_congress_chair`. The sourced National Archives of Fiji image is a bounded visual/provenance PASS, but its archive date is only circa 1940s against the 1936-centered baseline. It must remain user-gated and must not be described as a 1936 photograph. |
| Flags and advisors | PASS for current scope | Vanilla FIJ normal/medium/small ideology flags are reused. No new historical flag is invented. No advisor, operative, commander, high-command, dossier, small portrait, or opposite-gender leader/name pool is claimed by IW-177. |
| Focus framework | PASS for current framework | FIJ is allowed to initialize only from vanilla `generic_focus`; setup assigns `independence_wave_focus_assignment.full_framework`, loads `independence_wave_focus_tree`, and cleanup restores `generic_focus`. The shared tree imports the FIJ roots/capstone and the six connected branch focuses. The guard prevents replacing a meaningful pre-existing country tree. |
| Decisions and mission | PASS at source | `independence_wave_fij_founding_congress_category` contains the 250-day `independence_wave_fij_hold_constituent_congress_together` mission and six staged, costed, timed decisions: convene congress, register communal veto, open labor/shipping board, settle colonial accounts, charter coastal guard, and ratify island compact. Cancel, timeout, capital-loss, and failure effects are present. |
| Ideas and visible values | PASS at source | `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact` form a lifecycle. Setup exposes congress pressure, communal authority, shipping access, colonial accounts, and defense readiness through centralized FIJ constants and category localisation. |
| Forces and starting baseline | PASS with runtime gate | Mapping row `IW-177` uses `coastal_maritime`, force level `53`, tradition `p177`, reinforcement mask `659`, navy-only inheritance, and no air inheritance. The dynamic loader runs only with the Pacific command structure and command-roster readiness. Vanilla FIJ remains the small baseline: infantry weapons 1, 20 convoys, no OOB, infrastructure 2, naval base 1, and no unsupported large army. |
| Technology and industry | INCOMPLETE TOOLING / bounded baseline | No bespoke FIJ technology tree or industrial windfall is claimed. The installed MCP exposes no Technology Tree Viewer, so prerequisite and unlock rendering remains unresolved. Vanilla FIJ technology/industry/supply values are preserved and the package AI emphasizes infrastructure, dockyard, fuel, infantry/support, and convoys. |
| AI and playability | PASS at source with risks | `independence_wave_fij_coastal_congress_survival`, `independence_wave_fij_founding_restraint`, and `independence_wave_fij_host_threat` cover survival, restraint, and severe-host-threat states. Shared focus/decision AI weights exist, but no bespoke FIJ focus-order script exists; generic full-framework ordering and one-state island vulnerability remain balance risks. |
| Diplomacy and host settlement | PASS at source | Shared host negotiation, guarded-frontier, association, reclamation, ambition, and league routes are explicitly installed. The `independence_wave_fij_settle_colonial_accounts` project intentionally has no capital-control requirement because it is a former-host diplomatic settlement; it still requires a living host and cancels if the host disappears. |
| Regional ambition and formable | FORM-39 implemented, readiness closed | FIJ selects `melanesian_federation`. The FORM-39 adapter now has exact FIJ/PNG/WPG members, anchors `636/523/669`, consent ledger, MFX identity dispatch, autonomous-member cleanup, staged integration, and paid projects. FIJ eligibility and readiness still require `independence_wave_fij_melanesian_route_adapter_complete`, the three member research flags, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, and `independence_wave_form39_identity_review_complete`. These readiness inputs remain intentionally unset. |
| Cleanup and rollback | PASS at source | `independence_wave_cleanup_iw_177_fiji` removes the FIJ mission, six decisions, three ideas, five ledger variables, lifecycle and route flags, formable selection, focus tree, and Sukuna leader, and clears the FORM-39 adapter flag. The shared FORM-48 cleanup guard now covers only HBX/IW-184, HAW/IW-173, and FSM/IW-179; FIJ is not sent through the wrong federation cleanup. |
| Runtime dispatch and attestation | BLOCKED by design | IW-177 has an adapter/preflight branch and exact FIJ scenario branch, but `has_independence_wave_runtime_package_content_attestation_for_execution_id` intentionally omits 177. Scenario/preflight content gating therefore blocks FIJ before execution. |

## File-surface checklist

Current FIJ package gameplay and contract surfaces are present in:

- `common/script_constants/006_independence_wave_pacific_constants.txt` for FIJ politics, ledger, mission, and AI tuning.
- `common/ideas/006_independence_wave_pacific_ideas.txt` for the three FIJ lifecycle ideas.
- `common/decisions/categories/006_independence_wave_pacific_categories.txt` and `common/decisions/006_independence_wave_pacific_decisions.txt` for the founding-congress category, mission, six decisions, costs, timing, cancellation, and failure effects.
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` for FIJ identity, leadership, map, host, command, setup, lifecycle, force, AI, focus, and completion checks.
- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` for FIJ setup, politics, ledger initialization, focus assignment, force dispatch, final validation, cleanup, and the bounded route-flag correction.
- `common/national_focus/006_independence_wave_pacific_focus.txt` and `common/national_focus/006_independence_wave_focus.txt` for the six FIJ shared focuses and full-framework imports.
- `common/scripted_effects/006_independence_wave_focus_effects.txt` for the full-framework assignment and generic-tree preservation contract.
- `common/characters/006_independence_wave_pacific_characters.txt`, `interface/006_independence_wave_pacific_portraits.gfx`, and `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds` for the male Sukuna leader consumer.
- `localisation/english/006_independence_wave_pacific_l_english.yml` for parties, leader, ideas, category, mission, decisions, focuses, and tooltips.
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt` and `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt` for IW-177 planning, state 636, and reservation-group binding.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` for adapter/preflight, content-attestation, and scenario gates.
- `common/scripted_triggers/006_independence_wave_form39_triggers.txt`, `common/scripted_effects/006_independence_wave_form39_effects.txt`, and the shared formable registry files for the named Melanesian adapter and readiness contract.
- Vanilla references `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/FIJ - Fiji.txt`, `history/states/636-Fiji.txt`, `common/country_tags/00_countries.txt`, `common/countries/Fiji.txt`, and vanilla FIJ localisation/flag files.

## Missing or stale surfaces

- Canonical content attestation intentionally omits `constant:independence_wave_package_id.iw_177`; no dispatch change is authorized in this audit.
- FORM-39 readiness inputs remain writerless or review-closed: `independence_wave_fij_melanesian_member_research_complete`, `independence_wave_png_melanesian_member_research_complete`, `independence_wave_wpg_melanesian_member_research_complete`, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, and `independence_wave_form39_identity_review_complete`.
- IW-178 PNG and IW-157 WPG do not yet have accepted complete country packages or research-flag writers, so the exact three-member route cannot execute.
- MFX is staged as a candidate identity but remains `needs_user_review`; its readiness and collision gates must not be inferred from an asset file or a stale report.
- Older FIJ handoffs describe FORM-39 as registry-only or say the setup trigger requires the route-adapter flag. Current source supersedes those statements: the FORM-39 gameplay adapter is implemented, while FIJ setup does not write the readiness flag and `has_prepared_independence_wave_iw_177_package_setup` keeps package setup separate from formable readiness.
- No installed Technology Tree Viewer is available. This is an unresolved inspection limitation, not technology completion evidence.

## Map and state setup issues

State `636` is the sole compact FIJ anchor with vanilla provinces `4286/7302/12159`, one victory point, infrastructure 2, naval base 1, local supply 0, and 180,000 manpower. It is owned by ENG in vanilla history, cores FIJ, and is capital state 636. The package requires the released country to own/control it while the former host retains its protected remnant and capital state 126. The reservation group prevents automatic FIJ/SAM/FSM co-admission. No map write, extended territory, railway, port, resource, or supply rewrite is needed or authorized.

The shared Event 005/Event 006 origin and reservation guards remain the controlling collision barrier. FIJ has no country-specific bypass. Live host survival, final state control, and allocator transaction evidence remain unperformed.

## Politics, leader, portrait, flag, advisor, and party issues

The FIJ political contract is internally coherent: democratic provisional authority, four localized parties, centrism Sukuna chair, and the 44/12/34/10 starting distribution. The portrait consumer is male-only and has no advisor or small derivative. The DDS exists at 156x210 with 131,168 bytes and matches the GFX basename. The source chain is National Archives of Fiji / Wikimedia Commons `PD-Fiji`, but the archive's circa-1940s date is the controlling 1936-baseline blocker. No generated substitute, opposite-gender pairing, invented historical flag, or unreviewed advisor asset was introduced.

Vanilla FIJ ideology flag triplets are reused for all four ideologies. FORM-39 MFX identity and flat flag review are separate readiness gates and must remain closed until independently accepted.

## Focus, decision, idea, and asset issues

The six FIJ focus identifiers are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus`. Their prerequisites, bypass flags, capital/host/stability gates, reward effects, icons, AI weights, and localisation are present.

The six decision identifiers are `independence_wave_fij_convene_constituent_congress`, `independence_wave_fij_register_communal_veto`, `independence_wave_fij_open_labor_shipping_board`, `independence_wave_fij_settle_colonial_accounts`, `independence_wave_fij_charter_coastal_guard`, and `independence_wave_fij_ratify_island_compact`. The founding mission is `independence_wave_fij_hold_constituent_congress_together`. The decision audit records the former-host settlement's deliberate diplomatic-capital exception; no change was made without design direction.

The three ideas are `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact`. Shared icon coverage is present; no new FIJ icon asset was required. The 56-key FIJ localisation crosswalk used in this audit found no missing keys, and the file retains UTF-8 BOM encoding.

## Starting military, technology, industry, supply, and production issues

The accepted mapping is `IW-177 -> coastal_maritime`, force level 53, tradition 53 (`p177`), reinforcement mask 659, navy-only inheritance, and no air inheritance. The force loader is guarded by `has_country_flag = independence_wave_command_roster_ready` and `has_independence_wave_pacific_command_structure = yes`, preventing an incomplete package from receiving a free formation. Vanilla FIJ's one infantry-weapons level, 20 convoys, no OOB, infrastructure 2, and naval base 1 remain the baseline. The current source does not claim bespoke FIJ research, air, armor, broad industry, or a technology-tree pass.

The one-state island start remains vulnerable to port loss, fuel scarcity, and convoy interdiction. AI priorities and the coastal-guard idea address this at source, but no live balance or save/load evidence was produced.

## AI, diplomacy, regional ambition, and playability issues

The FIJ survival strategy prioritizes army, infantry/support, convoys, fuel, infrastructure, dockyard, and coastal defense. Founding restraint discourages opportunistic wars outside severe host threat or regional-power states. The host-threat strategy raises emergency army and coastal-bunker priorities. Generic full-framework focus ordering remains a future AI-balance risk.

The package exposes host negotiation, guarded frontier, association, reclamation, ambition, and league route flags. FORM-39 is the only selected formable family. The named adapter's exact member/anchor and consent contract is source-present, but its research, X-tag, flag, identity, and content-attestation gates are not satisfied. This keeps the regional ambition playable as a visible but fail-closed route rather than silently forming a federation.

## Patch record

Changed file: `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`.

Changed identifier: `independence_wave_setup_iw_177_fiji` no longer writes `independence_wave_fij_melanesian_route_adapter_complete`. No tag, state, leader, party, focus, decision, localisation, or formable identifier changed.

Before: IW-177 setup set the FORM-39 route-adapter flag while only commenting that FORM-39 readiness remained closed. This could satisfy a carrier/member eligibility prerequisite before the explicit research, consent, MFX, flag, and identity gates were accepted.

After: IW-177 setup still selects and registers `melanesian_federation`, but leaves `independence_wave_fij_melanesian_route_adapter_complete` unset. FORM-39 eligibility/readiness remains gated by the dedicated readiness contract; no current setup writer bypasses it. FIJ cleanup continues to clear the flag if a future adapter is installed.

## Validation

- Required offline Paradox wiki pages and the relevant vanilla documentation for country setup, focuses, decisions, effects, triggers, localisation, AI, and state/country history were consulted before this audit.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` completed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.
- A targeted route-flag scan now finds the FIJ adapter flag only in FORM-39 eligibility/readiness/strict-precondition triggers and FIJ cleanup; no IW-177 setup writer remains.
- The FIJ localisation crosswalk found all 56 expected party, leader, idea, category, mission, decision, focus, description, and tooltip keys, with UTF-8 BOM present.
- The runtime portrait DDS header is `156x210` and 131,168 bytes, matching the registered GFX consumer.
- No Hearts of Iron IV executable, save, live consumer, map rewrite, or Technology Tree Viewer was run. Live allocator, focus visibility, AI timing, host survival, force materialization, FORM-39 consent, save/load, and runtime rollback remain unproved.

## Remaining blockers and simplifications

- The circa-1940s Sukuna source date remains a non-negotiable user/package admission decision against the 1936-centered baseline.
- IW-177 remains outside canonical content attestation; no admission or readiness weakening was made.
- FORM-39 cannot execute until IW-157/WPG and IW-178/PNG package research and research flags, MFX X-tag/flat-flag/identity review, collision reservation, and FIJ route readiness are accepted.
- Technology-tree rendering, live runtime, save/load, balance, and allocator transaction evidence remain unperformed.
- No fallback country, placeholder portrait, invented flag, advisor substitute, large army, map extension, or unrelated gameplay change was introduced.

No other FIJ country-package gameplay patch was made. No commit was created because the touched scripted-effects file also contains parent-owned uncommitted hidden-event recruitment changes; the parent should review and commit the aggregate change deliberately.
