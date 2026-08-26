# Event 006 IW-177 Fiji package closure handoff

Date: 2026-08-26.

Scope: FIJ/IW-177 only.

## Admissibility verdict

**FAIL-CLOSED / not admissible.**

No gameplay patch is safe or authorized from this audit.

IW-177 is internally wired as a dormant FIJ adapter, but it is not content-attested and cannot enter normal or scenario execution until the sourced leader/date gate and the complete FORM-39 Melanesian Federation contract are accepted.

Adding IW-177 to the central content-attestation trigger would bypass unresolved evidence and was not done.

No country, state, tag, leader, party, focus, decision, idea, AI, localization, GFX, DDS, formable, Join, capacity, dispatch, scenario, or map file was changed.

## Country-package coverage checklist

| Surface | Status | Evidence and exact risk |
| --- | --- | --- |
| Candidate and identity | PASS as dormant adapter | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:178` binds IW-177 to Fiji, registered tag `FIJ`, anchor `636`, and `RG-PACIFIC-ISLANDS`; `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:32` requires original tag FIJ, active-country state, and package id IW-177. |
| Research authority | HOLD | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:178` requires a release-date-safe sourced male leader or authentic institution and explicitly blocks the package when that evidence is unavailable. |
| State and host collision | PASS at source, live proof open | Vanilla state `636` is Fiji's capital, owner ENG, FIJ core, small-island state, infrastructure 2, naval base 1, one victory point, and provinces `4286 7302 12159`; package setup requires FIJ to own and control 636 as capital while retaining a living non-FIJ former host. |
| Reservation group | PASS at source | `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:103` places IW-177 with IW-175/IW-176/IW-179 in `RG-PACIFIC-ISLANDS`; only one automatic package may consume the shared coarse anchor in a wave. |
| Politics and parties | PASS at source | `independence_wave_initialize_fij_politics` sets democratic elections and FIJ party names with centralized popularity values `44/12/34/10` in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:112`; all four party/localization pairs exist. |
| Leader identity and date safety | BLOCKED | `FIJ_independence_wave_founding_congress_chair` is male and uses a centrism country-leader role in `common/characters/006_independence_wave_characters_registry.txt:1093`; the visible Sukuna source is explicitly circa 1940s against the 1936-centered opening, while the 1929 Vishnu Deo alternate has unresolved role, halftone, and attribution limits. |
| Portrait consumer | PROVISIONAL / blocked | `interface/006_independence_wave_small_assets.gfx:97-98` maps `GFX_portrait_FIJ_independence_wave_founding_congress_chair` to the existing 156x210 DDS, but `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/source_manifest.json:6,14,34,122,158,160` remains `needs_user_review` and `provisional_pending_source_date_and_package_admission`; the exact-consumer audit found no safe alternate consumer. |
| Flags | PASS for carrier, no new flag authorized | Vanilla FIJ normal, medium, and small ideology triplets are reused; no historical or invented FIJ flag was added. |
| Advisors and command roster | PASS for current scope | No FIJ advisor, operative, high-command, commander, dossier, small portrait, or opposite-gender leader/name-pool consumer is requested; no substitute was invented. |
| Focus framework | PASS as dormant source | `common/national_focus/006_independence_wave_focus.txt:57-59,4153-4245` imports the FIJ roots and defines six connected FIJ focuses under `independence_wave_focus_tree`; setup and cleanup use the full-framework assignment only for the vanilla generic tree. |
| Decisions and mission | PASS as dormant source | `common/decisions/006_independence_wave_pacific_decisions.txt:445-553` defines the founding-congress category, 250-day mission, and six costed timed decisions with activation, cancellation, timeout, and failure paths. |
| Ideas and visible values | PASS as dormant source | `common/ideas/006_independence_wave_ideas_registry.txt:3555-3583` defines `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact`; the lifecycle effect transitions and removes them. |
| Forces and starting baseline | PASS with runtime gate | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:178` maps IW-177 to `coastal_maritime`, force level 53, local infantry/coastal guards, and no air inheritance; the dynamic force loader requires Pacific command and roster readiness. Vanilla FIJ remains basic infantry weapons 1, 20 convoys, no OOB, infrastructure 2, naval base 1, and no unsupported windfall. |
| Technology and industry | BOUNDED BASELINE / TOOLING HOLD | No bespoke FIJ technology tree is claimed; the installed package exposes no Technology Tree Viewer, so prerequisite and unlock rendering remain unresolved. |
| AI and playability | SOURCE PASS / PROBABILITY HOLD | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:2414-2440` defines survival, founding-restraint, and severe-host-threat profiles; live behavior and the required probability comparison remain unverified. |
| Patron, network, and league | PASS as dormant source | IW-177 setup enables the shared host routes, ambition family, league route, and aligned network arrays, but none can execute before package attestation and host checks. |
| Cleanup and rollback | PASS at source | `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:1017-1055` clears the FIJ mission, six decisions, three ideas, ledgers, lifecycle/setup/AI flags, selected family, route-adapter receipt, and temporary leader. |
| Central admission | BLOCKED by design | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` lists IW-177 in the runtime adapter, but `:159-202` omits IW-177 from content attestation. The exact FIJ preflight branch remains at `:320-323`. |

## File-surface checklist

The candidate and research authority is in `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, and `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`.

The FIJ package trigger contract is in `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:32,247,437,528`.

The FIJ setup, dispatch, lifecycle, force, and cleanup contract is in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:803-862,1017-1073`.

The region-13 package loader, allocation weight, and reservation publisher are in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:3268,3504,3738`.

The central adapter, attestation, normal preflight, and scenario preflight are in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63,159-202,320-323,529-532`.

The shared allocation, host-loss capacity, and frozen-plan reservation logic is in `common/scripted_effects/006_independence_wave_package_planner_effects.txt:61-170,267-318,393-435,478-701`.

The shared Join conversion and fixed attested candidate probe are in `common/scripted_effects/006_independence_wave_join_effects.txt:119-244,353-418`.

The scenario ranking publisher is in `common/scripted_effects/006_independence_wave_scenario_effects.txt:256`.

The character, portrait, localization, focus, decisions, ideas, AI, and force surfaces are `common/characters/006_independence_wave_characters_registry.txt:1093-1107`, `interface/006_independence_wave_small_assets.gfx:97-99`, `localisation/english/006_independence_wave_pacific_l_english.yml:246-305`, `common/national_focus/006_independence_wave_focus.txt:53-59,4153-4247`, `common/decisions/006_independence_wave_pacific_decisions.txt:445-553`, `common/ideas/006_independence_wave_ideas_registry.txt:3555-3583`, and `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:2414-2440`.

The separate FORM-39 contract is in `common/scripted_triggers/006_independence_wave_form39_triggers.txt`, `common/scripted_effects/006_independence_wave_form39_effects.txt`, `common/countries/006_independence_wave_formable_cosmetics.txt`, `localisation/english/006_independence_wave_formable_registry_l_english.yml`, and `docs/events/006_independence_wave/form39_melanesian_federation.md`.

## Missing or stale country-package surfaces

No stale FIJ gameplay consumer, localization key, focus id, decision id, idea id, GFX key, or runtime DDS path was found in the bounded source review.

The central Join probe at `common/scripted_effects/006_independence_wave_join_effects.txt:213-244` intentionally ends its fixed candidate order at the currently attested IW-184 branch and does not include unattested IW-177 or IW-179.

This is not a current defect because `independence_wave_join_try_package` and the planner both require the central content-attestation predicate before reservation.

When FIJ eventually clears every admission gate, the parent must add IW-177 to the Join candidate sequence in the same reviewed promotion change; doing so now would violate the source-of-truth comment that the sequence is attestation-ordered.

The package's current FORM-39 admission inputs remain unset or review-closed: `independence_wave_fij_melanesian_route_adapter_complete`, `independence_wave_fij_melanesian_member_research_complete`, `independence_wave_png_melanesian_member_research_complete`, `independence_wave_wpg_melanesian_member_research_complete`, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, and `independence_wave_form39_identity_review_complete`.

A current common-source writer scan found no setter for those seven inputs.

Only `independence_wave_form39_register_readiness` sets the runtime receipt `independence_wave_form39_readiness_attested` after all gates pass, and cleanup clears that receipt.

## Map, state, and host setup

The installed vanilla `history/states/636-Fiji.txt` defines state 636 as a small island with 180,000 manpower, owner ENG, FIJ core, infrastructure 2, naval base 1 at province 4286, one victory point at 4286, local supplies 0, and provinces 4286, 7302, and 12159.

The installed vanilla `history/countries/FIJ - Fiji.txt` defines capital 636, infantry weapons level 1, 20 convoys, democratic rule, elections, and the baseline popularity values 50/6/38/6 before IW-177 setup applies its package values.

The accepted IW-177 reservation binds FIJ to state 636 and `RG-PACIFIC-ISLANDS`.

The runtime initializer requires state 636 to be owned and controlled by FIJ, to remain the capital, and to have a living distinct former host whose protected state relationship is still valid.

No map rewrite, state split, railway edit, supply rewrite, claim expansion, or port/resource mutation is present or authorized.

Live reservation, host-survival, state-control, and save/load evidence remain open because the HOI4 MCP transport was unavailable and live game execution is outside this task.

## Politics, leader, portrait, flags, and parties

The FIJ package uses named party strings `FIJ_independence_wave_democratic_party`, `FIJ_independence_wave_communism_party`, `FIJ_independence_wave_neutrality_party`, and `FIJ_independence_wave_fascism_party` with complete long-name localization.

The country leader is the male `FIJ_independence_wave_founding_congress_chair` with centrism ideology, expiry `1965.1.1.1`, and the existing GFX consumer.

The runtime DDS is present at `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds` with `DDS ` magic, 156x210 dimensions, 131168 bytes, and SHA-256 `31FEA5EB5C7C4B6F34EC138ED6A3168A7C6C39755A992BD6ABF0296C5838D2C6`.

The source manifest marks the Sukuna candidate `needs_user_review` because its National Archives of Fiji image is only dated circa 1940s.

The Vishnu Deo 1929 alternate is period-valid as an image but does not safely support the current founding-congress-chair identity and remains anonymous halftone material requiring independent review.

The exact existing-consumer audit dated 2026-08-21 found no identity-safe wiring for either supplied Sukuna or Deo DDS into the institutional FIJ chair consumer.

No portrait fallback, generated grounded face, RunPod operation, opposite-gender pairing, invented leader, or advisor substitution was used.

The carrier reuses vanilla FIJ flag triplets and has no new flag provenance issue.

## Focus, decisions, ideas, and assets

The six FIJ focuses are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus`.

The shared root imports the convene, open-labor-shipping, and ratify nodes, and the prior focus audit's root-import correction is present.

The decision category `independence_wave_fij_founding_congress_category` contains mission `independence_wave_fij_hold_constituent_congress_together` and six staged decisions with explicit capital/host cancellation and failure behavior.

The ideas `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact` use existing shared icon definitions and are package-allowed.

The FIJ localization file contains the party, leader, idea, category, mission, decision, focus, and tooltip keys at `localisation/english/006_independence_wave_pacific_l_english.yml:246-305` and begins with a UTF-8 BOM.

## Force, technology, industry, supply, and production

The accepted force row is IW-177, `coastal_maritime`, force level 53, with engineers, reconnaissance, coastal signals, and maintenance first, while artillery and logistics require inter-island depots.

Dynamic force materialization requires the Pacific command structure, command roster, force mapping package, and final package setup proof.

No bespoke technology tree, air inheritance, armor, large army, broad industry grant, railway change, or production-line expansion is claimed.

The one-state island baseline remains vulnerable to port loss, fuel scarcity, convoy interdiction, and a small replacement pool; the coastal-guard idea and AI priorities address this at source, but live balance is unproved.

The installed MCP exposes no Technology Tree Viewer, so technology prerequisite and unlock rendering is an unresolved tooling limitation rather than completion evidence.

## AI, probability, patron, network, and league

The source AI profiles are `independence_wave_fij_coastal_congress_survival`, `independence_wave_fij_founding_restraint`, and `independence_wave_fij_host_threat`.

Their source priorities cover build army, infantry/support/convoy production, fuel silos, infrastructure, dockyards, coastal bunkers, and war avoidance under severe host threat.

The mandatory `chaosx_ai_probability_auditor` route could not run because the required HOI4 probability MCP transport was closed; no AI weight was changed and no source-only result is being presented as probability evidence.

The package enables shared patron, host, network, regional ambition, and league route surfaces only after setup, and all remain behind central package and formable gates.

## FORM-39 Melanesian Federation blockers

`common/scripted_triggers/006_independence_wave_form39_triggers.txt:20-49` requires exact FIJ/IW-177 state 636, exact PNG/IW-178 state 523, and exact WPG/IW-157 state 669 package identities and research flags.

`common/scripted_triggers/006_independence_wave_form39_triggers.txt:105-112` requires the FIJ route adapter, X-tag reservation, reviewed flat-flag package, identity review, and researched PNG/WPG member packages before readiness.

The repository has no setter for the FIJ route adapter, FIJ/PNG/WPG research flags, MFX X-tag reservation, MFX flat-flag readiness, or MFX identity-review inputs.

IW-178 PNG and IW-157 WPG remain without accepted named-community/district package evidence, source/portrait decisions, force/host setup, and runtime proof.

MFX cosmetic colors/assets exist, but their identity and collision evidence remain review-closed and do not authorize runtime promotion.

The FORM-39 route must remain fail-closed; do not substitute generic Papua, generic Melanesia, a different person, or an invented flag.

## Central adapter, attestation, dispatch, capacity, Join, and scenario surfaces

IW-177 is present in the generic runtime adapter at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:27`.

The FIJ normal preflight branch is present at `:321-322`, and the exact FIJ scenario branch is present at `:530-531`.

The scenario ranking publisher includes IW-177 at `common/scripted_effects/006_independence_wave_scenario_effects.txt:256`.

The canonical content-attestation trigger at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` omits IW-177, which correctly blocks normal and scenario preflight before country mutation.

The planner loader and reservation publisher bind IW-177 to FIJ and state 636 at `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:3268-3281,3738-3745`.

The planner host-capacity helper subtracts the protected remnant for ordinary plans and allows the explicit zero-host Join path only through the Join conversion flag at `common/scripted_effects/006_independence_wave_package_planner_effects.txt:267-318`.

The Join probe's fixed candidate order is attestation-only at `common/scripted_effects/006_independence_wave_join_effects.txt:213-244`; IW-177 is deliberately absent while unattested.

No central capacity, duplicate-anchor, host-survival, Join cleanup, or scenario identity defect was found that could be safely patched without changing admission authority.

## Validation evidence

The required HOI4 MCP read-only routes were attempted for map state 636 inspection/rendering, `independence_wave_focus_tree` inspection/rendering, Event 006 event inspection/rendering, AI probability inspection, and technology inspection.

Every attempted MCP call returned the exact blocker `tool call failed for hoi4_agent_tools/... — Caused by: Transport closed`.

Because the MCP server was unavailable, no map, focus, event, probability, or technology artifact is claimed as engine evidence, and no map rewrite was attempted.

The following read-only validators completed successfully.

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 40 runtime adapters, 7 adapter-only fail-closed IDs including IW-177, 32 attested packages, and 29 compatible reservation groups.
- `python -B .tools/audit_event6_country_api.py` passed with 242 broad unique tags, 191 resolved unique carriers, 34 Soviet carriers, 45 Africa carriers, zero missing, zero duplicates, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py` passed with 102 registered tags, 102 complete flag families, and zero incomplete families.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and 8 listed edge cases.
- `python -B .tools/audit_event6_form16.py` passed the FORM-16 contract audit.
- `python -B .tools/audit_event6_gui_matrix.py` passed the Statehood Ledger semantic source matrix.

The archived installed-tag audit was also attempted read-only with the repository root supplied and stopped on the unrelated registry mismatch `extra=['BLX']`; this result is not used as FIJ collision evidence.

The BOM, FIJ DDS header, dimensions, byte length, and current hash were checked directly.

No Hearts of Iron IV executable, save, live allocator transaction, live focus/event/AI/formable consumer, RunPod service, map rewrite, or staging/commit operation was performed.

## Changed files

Only this handoff was added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fij_package_closure_2026_08_26.md`.

No tags, state ids, leaders, parties, focus-tree ids, localization keys, formable ids, or gameplay behavior changed.

## Blockers and next owner

The parent or portrait owner must obtain an attributed, rights-reusable, date-safe male Fiji source no later than the 1936 baseline, or record and explicitly approve an era exception with a fresh identity/framing/provenance review.

The formable owner must complete exact IW-178 PNG and IW-157 WPG package research, the FIJ/PNG/WPG route adapter and research flags, MFX X-tag reservation, flat-flag package, identity review, installed collision proof, consent ledger, and final FORM-39 runtime wiring.

After those gates pass, the parent must rerun the unavailable MCP map/focus/event/probability routes, route the AI baseline and compare through `chaosx_ai_probability_auditor`, add IW-177 to the central content attestation and attestation-ordered Join candidate list, and repeat the package and scenario validation.

Until then, keep IW-177 outside content attestation and keep FORM-39 unreachable.

No simplification or fallback was introduced.
