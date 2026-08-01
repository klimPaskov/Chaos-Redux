# IW-177 Fiji and FORM-39 package closure audit v88

Date: 2026-08-01

Scope: FIJ/IW-177 and the FORM-39 Melanesian Federation adapter boundary only.

Disposition: **source-connected but runtime closed; one narrow cleanup patch applied.**

This audit compares the current package against `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, the Event 006 resume packet, the accepted IW-177 and FORM-39 handoffs, the offline Paradox wiki pages, and the installed vanilla country/state/documentation precedents. It does not admit IW-177, write a research flag, accept Sukuna's date, accept the MFX identity, create PNG/WPG packages, or change the allocator and dispatch allowlists.

## Country-package coverage checklist

| Surface | Status | Current evidence and risk |
| --- | --- | --- |
| Tag and package identity | PASS at source, runtime closed | Vanilla `FIJ` is mapped to `countries/Fiji.txt`; `is_independence_wave_fij_package` requires original tag `FIJ`, an active Event 006 country, and `constant:independence_wave_package_id.iw_177`. No new gameplay country tag is created. |
| Reservation and anchor | PASS at source | IW-177 loads reservation group `RG-PACIFIC-ISLANDS`, region `southeast_east_asia_oceania`, depth `regional`, archetype `port_or_island`, registered-tag mode, and sole anchor state `636` in `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:294-305`; planning and reservation are guarded by state/tag/group availability in `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt:176-184` and `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:764-772`. FIJ, SAM, and FSM share the reservation group, so simultaneous automatic admission is blocked by design. |
| Map and host safety | PASS at source, live proof open | `can_initialize_independence_wave_iw_177_package` requires state `636` owned and controlled by FIJ, capital state `636`, a living non-FIJ former host, and the expected protected host pointer. No FIJ map rewrite, extra state, railway, resource, port, or supply mutation exists. Live host survival and allocator transaction evidence remain unperformed. |
| Politics and party setup | PASS at source | `independence_wave_initialize_fij_politics` installs democratic provisional authority, elections, FIJ party names, and the centralized popularity split `44/12/34/10` for democratic/communism/neutrality/fascist politics in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:111-128` and `common/script_constants/006_independence_wave_pacific_constants.txt:42-49`. |
| Leader and portrait | CONDITIONAL blocker | `FIJ_independence_wave_founding_congress_chair` is explicitly `gender = male`, uses `GFX_portrait_FIJ_independence_wave_founding_congress_chair`, and promotes centrism. The current runtime DDS is the National Archives of Fiji identity source for Ratu Sir Lala Sukuna, but the retained source metadata says circa 1940s against a 1936-centered baseline. Pt. Vishnu Deo has a 1929 public-domain source but a 1936 office-state gap and halftone limitations, so it remains user-review evidence rather than a silent replacement. |
| Flags and advisors | PASS for current FIJ scope, FORM-39 pending | Vanilla FIJ normal/medium/small ideology flags are reused and no historical flag is invented. IW-177 has no advisor, operative, commander, high-command, dossier, small portrait, or opposite-gender name/portrait pool. MFX normal/medium/small TGAs exist, but the identity package is `needs_user_review` and its readiness flags remain unset. |
| Focus framework | PASS at source, live layout open | IW-177 initializes only from `generic_focus`, assigns `independence_wave_focus_assignment.full_framework`, and loads `independence_wave_focus_tree`; cleanup returns to generic focus. The six FIJ focus identifiers are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus`. The shared tree and focus ownership are present, but the Event 006 focus layout still has the source-map blockers and no live focus-render proof was run. |
| Decisions and mission | PASS at source | `independence_wave_fij_founding_congress_category` exposes the 250-day `independence_wave_fij_hold_constituent_congress_together` mission and six staged decisions: convene congress, register communal veto, open labor/shipping board, settle colonial accounts, charter coastal guard, and ratify island compact. The decisions have centralized costs, timed removal, capital/host cancellation, timeout, and project-failure effects in `common/decisions/006_independence_wave_pacific_decisions.txt:442-554`. The former-host account intentionally omits a capital-control requirement while retaining a living-host cancellation gate. |
| Ideas and visible ledgers | PASS at source | `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact` form the FIJ lifecycle. Setup exposes congress pressure, communal authority, shipping access, colonial accounts, and defense readiness through centralized constants and category localisation. |
| Forces and starting baseline | PASS at source, runtime gate open | The IW-177 force row is profile `5` (`coastal_maritime`), force level `53`, tradition `p177 = 53`, reinforcement mask `659`, inheritance mask `1` (navy only), and research sensitivity `0` in `common/script_constants/006_independence_wave_force_package_constants.txt:254,468,682,896,1110`. Dynamic force application is guarded by Pacific command structure and `independence_wave_command_roster_ready`. Vanilla FIJ remains a small baseline with infantry weapons 1, 20 convoys, no OOB, infrastructure 2, naval base 1, and no unsupported large army. |
| Technology, industry, supply, production | BOUNDED BASELINE / TOOLING LIMIT | No bespoke FIJ technology tree or industrial windfall is claimed. Vanilla FIJ technology, production, state infrastructure, port, local-supply, and convoy values are preserved. The installed package exposes no Technology Tree Viewer, so prerequisite and unlock rendering remains unresolved rather than being treated as complete. |
| AI and playability | PASS at source with balance risk | `common/ai_strategy/006_independence_wave_pacific.txt:95-120` provides FIJ coastal-congress survival, founding restraint, and severe-host-threat strategies. Centralized priorities cover army, infantry/support, convoys, fuel, infrastructure, dockyard, and coastal defense. Generic full-framework focus ordering and one-state island vulnerability remain unproved balance risks. |
| Diplomacy and former-host settlement | PASS at source | The package installs host negotiation, guarded-frontier, association, reclamation, ambition, and league route surfaces. FIJ's colonial-account project uses a live former-host requirement and deliberately remains a bilateral diplomatic settlement without a capital-control gate. |
| FORM-39 route selection | IMPLEMENTED, FAIL-CLOSED | FIJ selects `constant:independence_wave_formable_family.melanesian_federation` and registers the named route surface. The adapter uses exact members FIJ/IW-177/636, PNG/IW-178/523, and WPG/IW-157/669, three minimum members/consents/anchors, negotiated federation, frozen ledgers, autonomous membership, anchor-only integration, projects, and rollback. It cannot pass readiness while its named research/reservation/identity inputs remain unset. |
| Cleanup and rollback | PATCHED, source pass | `independence_wave_cleanup_iw_177_fiji` removes FIJ mission/decisions, ideas, ledgers, lifecycle flags, formable selection, route exclusions, focus ownership, and Sukuna, and clears the FIJ route adapter flag. `independence_wave_form39_cleanup_runtime` now also clears the runtime-only `independence_wave_form39_readiness_attested` receipt, matching the other reviewed formable cleanup paths. |
| Dispatch and attestation | BLOCKED by design | IW-177 appears in the generic adapter and exact FIJ scenario branches, but `has_independence_wave_runtime_package_content_attestation_for_execution_id` intentionally omits `iw_177`; normal and scenario preflight therefore cannot execute it. No dispatch promotion is authorized. |

## File-surface checklist

| Surface | File(s) | Key identifiers or evidence |
| --- | --- | --- |
| Country identity and setup | `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`, `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` | `is_independence_wave_fij_package`, `can_initialize_independence_wave_iw_177_package`, `has_prepared_independence_wave_iw_177_package`, `independence_wave_setup_iw_177_fiji`, `independence_wave_cleanup_iw_177_fiji`. |
| Package planner and map binding | `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt`, `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt` | `independence_wave_load_package_iw_177`, `independence_wave_reserve_package_iw_177`, `can_plan_independence_wave_package_iw_177`, state `636`, `RG-PACIFIC-ISLANDS`. |
| Politics and tuning | `common/script_constants/006_independence_wave_pacific_constants.txt`, `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` | FIJ politics `44/12/34/10`, pressure start/stable values `31/62`, five FIJ ledgers, mission duration `250`, AI tuning. |
| Leader and portrait | `common/characters/006_independence_wave_pacific_characters.txt`, `interface/006_independence_wave_pacific_portraits.gfx`, `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds`, `events/006_independence_wave.txt` | `FIJ_independence_wave_founding_congress_chair`, male metadata, GFX consumer, synchronous hidden recruitment event `chaosx.nr6.350`. |
| Focus ownership | `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/006_independence_wave_pacific_focus.txt`, `common/scripted_effects/006_independence_wave_focus_effects.txt` | `independence_wave_focus_tree`, full-framework assignment, six FIJ focus IDs, generic-tree preservation and cleanup. |
| Decisions and ideas | `common/decisions/categories/006_independence_wave_pacific_categories.txt`, `common/decisions/006_independence_wave_pacific_decisions.txt`, `common/ideas/006_independence_wave_pacific_ideas.txt` | Founding-congress category, mission, six decisions, three FIJ ideas, cost/cancel/timeout/failure paths. |
| Force and AI | `common/script_constants/006_independence_wave_force_package_constants.txt`, `common/scripted_effects/006_independence_wave_force_effects.txt`, `common/ai_strategy/006_independence_wave_pacific.txt` | IW-177 profile/tradition/reinforcement/inheritance row, dynamic-force gate, FIJ survival/restraint/host-threat strategies. |
| Localisation and assets | `localisation/english/006_independence_wave_pacific_l_english.yml`, `localisation/english/006_independence_wave_formable_registry_l_english.yml`, vanilla FIJ flag triplets, MFX TGAs, `docs/assets/006_independence_wave/form39_melanesian_federation_identity_2026_07_27/` | FIJ party/leader/idea/decision/focus strings, MFX candidate manifest and review status, no missing FIJ visual consumer identified. |
| FORM-39 adapter | `common/scripted_triggers/006_independence_wave_form39_triggers.txt`, `common/scripted_effects/006_independence_wave_form39_effects.txt`, `common/decisions/categories/006_independence_wave_form39_categories.txt`, `common/decisions/006_independence_wave_form39_decisions.txt`, `common/ideas/006_independence_wave_form39_ideas.txt` | Exact member/anchor gates, readiness attestation, MFX identity, autonomous relations, integration, projects, dissolution, rollback, cleanup. |
| Shared formable registry and dispatch | `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`, `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`, `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | Family profile `melanesian_federation`, minimums `3/3/3`, generic commit allowlist, family-readiness reset, IW-177 adapter/preflight/content-attestation branches. |
| Source authority and research | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, `docs/events/006_independence_wave/form39_melanesian_federation.md`, prior IW-177 and FORM-39 handoffs | Event 006 remains HOLD/PARTIAL; IW-177 is outside attestation; MFX is `needs_user_review`; PNG/WPG and Sukuna source/date evidence are not admitted. |

## Missing or stale package surfaces

The named FORM-39 admission inputs are intentionally not written by gameplay setup: `independence_wave_fij_melanesian_route_adapter_complete`, `independence_wave_fij_melanesian_member_research_complete`, `independence_wave_png_melanesian_member_research_complete`, `independence_wave_wpg_melanesian_member_research_complete`, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, and `independence_wave_form39_identity_review_complete` remain unset or review-closed. A targeted `set_country_flag` scan found no writer for the route, member-research, X-tag, flat-flag, or identity-review inputs; the FIJ route flag is only required by FORM-39 triggers and cleared by FIJ cleanup.

`independence_wave_form39_register_readiness` is the only source writer for `independence_wave_form39_readiness_attested`, and it is reachable only after all named inputs and the exact member package contract pass. The cleanup patch makes this runtime receipt idempotently removable after dissolution, rollback, or origin cleanup without clearing the external research and identity evidence flags.

IW-178 PNG and IW-157 WPG remain outside the accepted package set, so the exact three-member route has no accepted research writers, community/district package proof, or runtime force/host evidence. Do not replace them with generic Papua or pan-Melanesian substitutes.

The MFX cosmetic colors and normal/medium/small TGAs exist, but the asset manifest and graphics handoff remain `needs_user_review`; their presence is not a runtime fallback or identity approval. The current MFX collision handoff also requires a fresh installed-mod audit if the external mod set changes.

No stale country-definition, tag, party, focus, decision, idea, portrait consumer, or localisation key was found in the FIJ scope beyond the intentionally closed gates above. Older handoffs that called FORM-39 registry-only or implied that IW-177 setup wrote the route adapter are superseded by the current source and v50 audit.

## Map and state setup issues

Vanilla `history/states/636-Fiji.txt` defines state `636` as a small island with provinces `4286`, `7302`, and `12159`, one victory point at `4286`, infrastructure `2`, naval base `1`, local supply `0`, owner `ENG`, and core `FIJ`. Vanilla `history/countries/FIJ - Fiji.txt` sets capital `636`, infantry weapons level `1`, twenty convoys, no OOB, democratic politics, 1936 elections, and the vanilla `50/6/38/6` popularity baseline before IW-177 setup applies its package distribution.

The package requires FIJ to own/control `636` and retain it as capital while a living non-FIJ former host remains available through the protected host pointer. The reservation group and exact-anchor gates prevent a second Pacific package from occupying the same planner slot. No state transfer, railway, port, resource, supply, or map rewrite is in scope for this audit.

Unperformed evidence is limited to live allocator reservation, host survival under hostile state changes, final state-control checks, save/load, and in-game package materialization.

## Politics, leader, portrait, flag, advisor, and party issues

The FIJ setup is internally consistent: democratic provisional authority, four localized party names, centrism Sukuna chair, male character metadata, and the centralized `44/12/34/10` distribution. The hidden `chaosx.nr6.350` event recruits the character synchronously before promotion, so setup no longer relies on an earlier asynchronous or duplicate recruitment writer.

The runtime portrait DDS has a `156x210` header and `131168` bytes and matches the registered GFX basename. The current source chain is rights-cleared National Archives of Fiji material via Wikimedia Commons but records circa 1940s, which remains a hard 1936 date gate. Pt. Vishnu Deo's 1929 source is useful research evidence but is not a drop-in replacement because of the 1936 office-state gap and halftone quality. No generated real-person portrait, invented historical flag, opposite-gender portrait/name pairing, advisor substitute, or fictional random name pool was introduced.

Vanilla FIJ normal/medium/small ideology flags remain the country flag surface. MFX uses a fictional generated flat design and has normal/medium/small TGAs staged under `gfx/flags/`, but the parent must not mark the identity-review or flag-package gate from those files alone.

## Focus, decision, idea, and asset issues

The FIJ six-focus route is wired into the full Event 006 framework with explicit prerequisites, bypass flags, capital/host/stability gates, reward effects, shared icon consumers, AI-compatible generic ordering, and localisation. The shared focus tree imports the FIJ convene, shipping, and ratification roots while preserving the existing generic tree guard.

The FIJ founding-congress category has one timed mission and six costed decisions with clear trigger/effect tooltips, timeout, capital-loss, living-host cancellation, and project-failure outcomes. The deliberate exception for `independence_wave_fij_settle_colonial_accounts` is documented in the source and does not bypass its living-host guard.

The three FIJ lifecycle ideas and five visible ledger variables are present and cleaned up. The FORM-39 carrier/autonomous ideas use the existing league membership sprite and remain unreachable until the exact identity/member gates are accepted.

No missing FIJ focus, decision, idea, portrait, flag, or localisation consumer was identified in this tranche. The broader Event 006 focus layout and visual review remain parent-owned blockers.

## Starting military, technology, industry, supply, and production issues

The IW-177 force mapping is `coastal_maritime`, force level `53`, tradition `p177 = 53`, reinforcement mask `659`, navy-only inheritance, and no research-sensitive material. The dynamic force effect collects population, factories, infrastructure, railway, port, supply, host divisions, surrender, patron, and network inputs and runs only after the Pacific command structure and command-roster readiness are present.

Vanilla FIJ starts with infantry weapons level `1`, twenty convoys, no OOB, state infrastructure `2`, naval base `1`, local supply `0`, and 180,000 state manpower. The package does not claim bespoke technology, air inheritance, armor, a large army, or an industrial windfall. The one-state island remains vulnerable to port loss, fuel scarcity, and convoy interdiction, so live balance and force-materialization checks remain open.

The installed MCP exposes no Technology Tree Viewer. This is recorded as an unresolved tooling limitation, not as technology completion evidence.

## AI, diplomacy, regional ambition, and playability issues

The FIJ AI strategies prioritize army, infantry, support, convoys, fuel, infrastructure, dockyards, and coastal defense, and apply a strong founding-war restraint unless a severe host threat or regional-power condition is present. The source is coherent for a small maritime country, but generic full-framework focus ordering, one-state resilience, and post-release AI timing are not live-proven.

FIJ installs host negotiation, guarded-frontier, association, reclamation, ambition, and league route flags and selects only the Melanesian family. FORM-39 uses exact FIJ/PNG/WPG arrays and frozen member/anchor/consent ledgers, never a geographic scan. Autonomous membership preserves member tags and trees; full integration transfers or cores only a specifically authorized named anchor.

The post-formation shipping, civil-service, and plebiscite projects require the carrier, both named autonomous members, command power, strategic reserves, and the appropriate administration/diplomatic/security costs. Timed cancellation clears active project flags when the carrier or bound member compact becomes invalid. No additional project or failure-punishment behavior was invented.

## Dispatch, readiness, cleanup, and patch record

The normal dispatch registry lists IW-177 in `has_independence_wave_runtime_package_adapter_for_execution_id` and the FIJ exact preflight branch, and the scenario registry includes IW-177 in its ranked list and exact-tag branch. The content-attestation registry intentionally omits IW-177, so both normal and scenario preflight remain blocked before any release or country mutation. This is the correct fail-closed state while Sukuna, PNG/WPG, MFX, and static/runtime evidence remain unresolved.

Changed file: `common/scripted_effects/006_independence_wave_form39_effects.txt`.

Changed identifier: `independence_wave_form39_cleanup_runtime` now executes `clr_country_flag = independence_wave_form39_readiness_attested`.

Before: FORM-39 cleanup removed post-formation carrier, integration, project, and ledger state but left the runtime attestation receipt on the country.

After: FORM-39 cleanup removes the runtime attestation receipt as well, matching the existing `independence_wave_formable_clear_selected_family_readiness` behavior and the Form-01/02/03/04/05/07/48 cleanup paths. The external research, X-tag reservation, flat-flag, identity-review, and FIJ route-input flags remain untouched and therefore cannot be falsely admitted or erased by cleanup.

No tag, state, leader, party, focus-tree ID, decision, idea, localisation key, formable identity, allocator row, or dispatch allowlist was changed.

## Validation and skipped evidence

- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` completed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one skipped random-event root.
- A targeted writer scan found no `set_country_flag` writer for the FIJ route adapter, the FIJ/PNG/WPG research inputs, or the FORM-39 X-tag/flag/identity-review inputs; the runtime attestation receipt is set only by `independence_wave_form39_register_readiness` and is now cleared by the FORM-39 cleanup plus the shared readiness reset.
- The FIJ localisation file retains a UTF-8 BOM, and the expected FIJ party, leader, idea, category, mission, decision, focus, description, and tooltip surfaces remain present in the existing crosswalk.
- The registered FIJ leader DDS header is `156x210`, the file magic is `DDS `, and the byte length is `131168`.
- Vanilla FIJ country/state history, country-tag registration, flag conventions, focus baseline, and relevant documentation were read directly from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
- No Hearts of Iron IV executable, save, in-game consumer, map rewrite, Technology Tree Viewer, live allocator transaction, focus-render session, AI timing run, host-survival scenario, force-materialization session, FORM-39 consent path, or save/load rollback test was run.

## Remaining blockers, simplifications, and handoff

- IW-177 remains outside canonical Event 006 content attestation and must not be promoted from this audit.
- Sukuna's strongest rights-cleared portrait source remains circa 1940s, while the pre-1937 Vishnu Deo candidate remains a user-review option with a 1936 role-state gap; no silent portrait substitution is authorized.
- FORM-39 remains blocked on the three named country-package research writers and the MFX X-tag reservation, flat-flag review, identity review, collision recheck, and FIJ route-adapter input.
- IW-178 PNG and IW-157 WPG lack accepted complete package research, named-community/district evidence, source/portrait decisions, force/host setup, and runtime proofs.
- Technology-tree rendering, live runtime, allocator, AI balance, host survival, save/load, and rollback evidence remain open.
- No fallback country, placeholder portrait, invented flag, advisor substitute, large army, map extension, generic Papua substitute, or unrelated gameplay change was made.

The parent agent should review the one-line cleanup patch, preserve the fail-closed route and attestation gates, and commit the patch with this handoff when the aggregate Event 006 worktree is ready.
