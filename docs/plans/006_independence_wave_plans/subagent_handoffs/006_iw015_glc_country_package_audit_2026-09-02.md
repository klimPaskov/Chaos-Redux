# Event 006 IW-015 Galicia country-package audit

Date: 2026-09-02

Scope: bounded post-roster audit of package `iw_015`, carrier `GLC`, installed anchor state `171`, and reservation group `RG-171`.

Verdict: **NO-CHANGE / FAIL-CLOSED**.

Standalone central admission is **not permitted**. No gameplay file, central attestation entry, capacity entry, deterministic Join entry, character, portrait, flag, or formable promotion was changed by this audit.

## Authority and binding

The current authority is `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` together with `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` and the accepted Event 006 country-package specifications.

The 2026-08-30 no-additive-roster repair in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_glc_no_additive_roster_repair_2026-08-30.md` is authoritative for GLC leader ownership.

The binding row in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` is `IW-015, Galicia, GLC, automatic_pool_ready_if_not_living, fixed_anchor_compact, state 171, host SPR, host capital 41, RG-171`.

`docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv` confirms that RG-171 may reserve only the unique anchor while the former host remains protected and retains a state; there is no documented state-171 collision in `006_current_map_state_collisions.csv`.

The current global boundary remains 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows, with IW-015 among the eight adapter-only fail-closed IDs.

## Country-package coverage checklist

| Surface | Current result | Evidence and blockers |
| --- | --- | --- |
| Candidate, tag, and country shell | Pass for the bounded adapter | IW-015 resolves to the vanilla `GLC` carrier; no mod-owned replacement tag or duplicate country definition is present. Vanilla references are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/countries/Galicia.txt` and `history/countries/GLC - Galicia.txt`. |
| Anchor and state setup | Source pass; runtime unclaimed | Vanilla state `171-Galicia.txt` has owner/core `SPR`, core `GLC`, capital 171, VPs 758 and 6734, infrastructure 3, dockyard 2, arms factory 1, air base 2, and naval base 6. MCP selected-state inspection found no missing or unknown province IDs and no selected-state blocker; workspace-wide map validation remains invalid because unrelated building/port diagnostics were truncated. |
| Host protection and origin separation | Pass in source gates | `can_initialize_independence_wave_iw_015_package` requires event-target anchor ownership/control, a non-GLC former host with `liberation_release_protected_state`, the protected-state ownership relation, capital 171, and both preserved vanilla leaders. The package and Event 012 candidate-origin guards require no stale origin/reservation and reject Event 012 carrier flags. |
| Opening flags and package lifecycle | Pass in source; central gate intentionally closed | The setup effect clears stale setup/override state, initializes the package only after the exact trigger contract, publishes `independence_wave_iw_015_setup_complete` only after prepared setup, and cleanup clears package/lifecycle/readiness/project flags. Normal and scenario preflight still require content attestation, which intentionally omits IW-015. |
| Roster checkpoint and duplicate safety | Pass | `history/general/006_independence_wave_character_recruitment_registry.txt` and `common/characters/006_independence_wave_characters_registry.txt` contain no `GLC_independence_wave_alfonso_daniel_castelao` recruitment or definition. `has_independence_wave_glc_command_roster` proves only vanilla Fuco Gómez and Alfonso Daniel Castelao with `ruling_only = no`; the canonical checkpoint applies the supplied portrait to the existing liberal Castelao once when `independence_wave_glc_portrait_override` is absent. |
| Cleanup and retry determinism | Pass in source | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:598-644` removes the GLC mission, decisions, ideas, ledgers, route/project flags, lifecycle/readiness flags, and restores `GFX_portrait_Alfonso_Daniel_Castelao` before clearing the override flag. |
| Force mapping and starting setup | Source pass | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:16` binds IW-015 to p15 `territorial_defense`, strength 50, territorial infantry/coastal guards, no navy/air inheritance, and an institutional officer commission. Setup loads/applies the mapping only after the preserved roster proof and shared readiness flag. |
| Politics, parties, and ideas | Source pass | The five GLC government installers in `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` set route-specific politics and party names. GLC ideas in `common/ideas/006_independence_wave_ideas_registry.txt` cover the contested council, Atlantic compact, constitutional charter, workers port council, municipal covenant, coastal security command, and protected customs mandate with shared Event 006 icons. |
| Decisions and mission | Source pass; no runtime claim | `common/decisions/006_independence_wave_iberian_decisions.txt:205-397` contains the GLC mission and eleven paid projects with capital-control, project-lock, cancellation, failure, cost, and AI blocks. IDs match `has_independence_wave_glc_active_package_project` and cleanup. |
| Focus framework and callback | Source pass; MCP nonblocking warning | Setup assigns `independence_wave_focus_tree` through the full-framework callback and the GLC project effects call the secure-depots, coastal-guards, council, former-host, and network callbacks. Current MCP focus inspect/render returned 184 focuses and no blocking diagnostics, with one long connector warning and one unrelated vanilla missing-description warning. |
| AI strategy | Source pass; quantitative evidence blocked | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:867-901` contains GLC territorial-survival, host-restraint, settled-port, and emergency-command strategies gated by setup/profile/route flags. The mandatory `chaosx_ai_probability_auditor` is not callable in this runtime, so no quantitative balance or survival claim is made. |
| Localisation and party names | Source pass | `localisation/english/006_independence_wave_iberian_l_english.yml:97-129,146-156,181-195` covers GLC category, mission, decisions, effects, parties, and ideas. No new localization was needed. |
| Flags and cosmetics | Vanilla carrier preserved; Event 006 admission unresolved | No custom GLC flag or cosmetic-tag mutation is present in the package. The accepted opening identity remains the vanilla GLC flag family, but an independent opening-flag/rights receipt is not present in the current authority set. |
| Portrait and GFX | Wiring present; promotion blocked | `interface/006_independence_wave_portraits_registry.gfx:141-152` registers `GFX_portrait_GLC_alfonso_daniel_castelao` at `gfx/leaders/006_independence_wave/portrait_GLC_alfonso_daniel_castelao.dds`. The source comment calls the selected input a `source-placeholder`; the resume packet retains an older `styled_final` runtime label, so provenance/lifecycle terminology and rights acceptance remain unresolved. The supplied-output consumer gate has not authorized relabelling or final promotion. |
| Event 012 collision safety | Pass for source guard; no live claim | The shared candidate-origin trigger rejects Event 012 carrier flags `africa_priority_member_package_active` and `africa_priority_member_focus_tree_loaded`; no GLC/171 Event 012 consumer was found in the bounded search. |
| FORM-07 separation | Separately fail-closed | `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` and `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt` use GLC anchor 171 only inside the exact CAT/NAV/GLC corridor and retain separate identity, consent, territory, and commit gates. No FORM-07 admission is implied by this package audit. |

## Central registries and admission blockers

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` includes IW-015 in the runtime adapter allowlist, but the content-attestation allowlist at `:159-202` omits IW-015 by design.

The exact package preflight at `:384-390` verifies `iw_015` and `(original_tag = GLC OR exists = no)`, while the scenario preflight at `:558-560` still requires exact tag availability and the shared attestation path.

`common/scripted_effects/006_independence_wave_join_effects.txt:236-270` probes the explicitly attested package list; IW-015 is absent, so no deterministic Join offer or Join membership is available for GLC.

The region planner wrapper in `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:142-149` uses the legacy candidate-availability contract for IW-015 and has no exact runtime-ready wrapper parity. This is a maintenance observation, not a proven gameplay defect: the legacy `independence_wave_package_content_ready` flag has no setter in the current source, and the central attestation gate independently blocks IW-015. No patch was made because changing planner parity would alter selection semantics without resolved admission evidence.

The current source-of-truth map also records 51 supplied portrait inputs, 38 exact safe mappings, and 13 unresolved inputs, with GLC Castelao retained among the terminology-conflicted consumers. This does not clear portrait rights, final style, or package admission.

## Meaningful validation and engine evidence

The following task-specific static validators passed against the current shared worktree:

- `python -B .tools/audit_event6_allocator.py` reported 40 adapters, IW-015 in the eight adapter-only set, and 32 attested packages.
- `python -B .tools/audit_event6_country_api.py` reported 242 broad unique tags, 191 resolved carriers, zero missing, and zero duplicates.
- `python -B .tools/audit_event6_flags.py --strict` reported 102 registered Event 006 tags and zero incomplete flag families.
- `python -B .tools/audit_event6_form16.py` passed the independent FORM-16 contract without changing FORM-07.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all SCN-008 scenario cells and edge-case matrix publication checks.

Read-only HOI4 MCP evidence was collected without claiming completion:

- `hoi4_map_inspect` for state 171 returned `MAP_INSPECTED`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8c6c0cedf4d5ccac1bc50af7785ddfaccfbbc6ef8059ba7e1494af7d9a12cab/8037037503cfd17ecd3c5fd4bfafbf7eb8815cdac188f5d67ee53628c35dc1c3/map-inspect.2e1838fc269780fc.json`; selected-state source checks passed, while unrelated workspace diagnostics were truncated.
- `hoi4_event_inspect` for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2aa9127c43eb45b0e5f925e054713b154e77293f4fc528001771cbc7bbf6ffe7/91aa5b9f1456c43dc1d7f3eb1fd24dfb138dee20c960f6531086d4c142486530/event-lint-24c482050767.json`; helper/lifecycle projections were deferred.
- `hoi4_event_render` for `chaosx.nr6.1` returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and a manifest under `.../event-overview-24c482050767-manifest.json`; this is not a runtime or save/load proof.
- `hoi4_focus_inspect` and `hoi4_focus_render` for `independence_wave_focus_tree` returned valid source-linked artifacts with no blocking diagnostics; the current tree has one long connector warning and one unrelated vanilla localization warning.
- `hoi4_tech_inspect` trace for `infantry_weapons` returned `TECH_INSPECTED` but reported 1,424 blocking workspace technology diagnostics; `hoi4_tech_render` returned `TECH_RENDERED` with `sourceAccurate = false` for the same global diagnostic set. The installed package exposes no separate Technology Tree Viewer, so technology evidence remains unresolved and no custom GLC technology is claimed.
- `hoi4_probability_inspect` on `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero discovered candidates, and no quantitative result. The required `chaosx_ai_probability_auditor` tool is unavailable, so the required named scenario pass and `hoi4_probability_compare` receipt cannot be produced.

No live game, save/load, MCP completion, or runtime-consumer claim was made.

## Remaining blockers and next safe action

1. Resolve the GLC Castelao portrait source-placeholder versus older styled-final terminology and rights/final-consumer decision through the portrait owner before changing bytes, labels, or gates.
2. Provide an independent accepted opening-flag identity/rights receipt for vanilla GLC, if the package contract requires one.
3. Run the named GLC package, route, decision, focus, and AI probability scenarios through `chaosx_ai_probability_auditor`, then compare identical scenarios after any parent-owned change.
4. Obtain bounded Event 006 helper/lifecycle MCP evidence and a usable technology-tree route, or retain those explicit limitations.
5. Only after all current portrait, opening-flag, origin-separation, probability, and runtime gates independently clear may the parent consider adding central attestation/capacity/Join; FORM-07 must remain separately fail-closed.

Simplifications and omissions: no gameplay patch, no central promotion, no new roster character, no new portrait, no custom flag, no live game validation, and no quantitative AI claim were made because the required evidence is unresolved.
