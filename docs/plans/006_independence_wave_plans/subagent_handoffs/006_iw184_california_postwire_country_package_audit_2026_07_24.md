# IW-184 California (HBX) post-wire country-package audit

Audit date: 2026-07-24.

Audit scope: fresh country-package review after the William D. Stephens portrait promotion in commit `cc9445620` (`Promote sourced California civic leader`). The review covers the dormant HBX shell, runtime package setup, state and host reservation, politics, leader and portrait ownership, flags, ideas, focuses, decisions, force mapping, technology inheritance, industry, supply, AI, FORM-48, SCN-008, cleanup, localisation, assets, and admission evidence.

## Exact verdict

The IW-184 California country package is `PASS` for static and post-wire country-package coverage. The current runtime portrait, stable character consumer, setup proof, force mapping, focus/decision surfaces, flags, localisation, and cleanup all resolve to the intended HBX package.

The package is still `HOLD / FAIL-CLOSED` for canonical runtime execution because `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:47-57` does not yet list `independence_wave_package_id.iw_184` in `has_independence_wave_runtime_package_content_attestation_for_execution_id`. The HBX adapter and ordinary/scenario dispatch branches are registered, but the content-attestation gate intentionally prevents automatic or SCN-008 execution until the parent admits IW-184.

Recommendation to the parent: promote IW-184 into the canonical content-attestation trigger only after reviewing this handoff, then rerun allocator, Event 005 collision/capacity, ordinary-release, and SCN-008 preflight checks. This audit did not edit that trigger or any gameplay file.

## Country-package coverage checklist

| Surface | Exact package identifiers and files | Result |
|---|---|---|
| Tag and shell | `HBX`, `IW-184`; `common/country_tags/006_independence_wave_countries.txt:102`; `common/countries/006_independence_wave_HBX.txt`; `history/countries/HBX - California.txt` | `PASS`; one Event 006 tag registration, dormant graphical shell only, runtime owns setup. |
| Registry and region | `IW-184`, `HBX`, `RG-378`, state `378`; `common/scripted_triggers/006_independence_wave_packages_region_14_triggers.txt:36-43`; `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt:54-67,263-275,421-428` | `PASS` for identity, anchor, package loader, automatic weight, and reservation surfaces; weight remains zero while canonical attestation is absent. |
| Runtime adapter | `has_independence_wave_runtime_package_adapter_for_execution_id`; `is_independence_wave_runtime_package_preflight_ready`; `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-31,62-133` | `PASS` for adapter and exact `IW-184/HBX` identity branch. |
| Canonical content admission | `has_independence_wave_runtime_package_content_attestation_for_execution_id`; same file `:47-57` | `HOLD`; IW-184 is absent by design. |
| Setup proof | `can_initialize_independence_wave_iw_184_package`; `has_prepared_independence_wave_iw_184_package_setup`; `has_complete_independence_wave_iw_184_package_setup`; `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:152-166,197-253,370-380` | `PASS` as a runtime proof chain. |
| Politics and parties | `independence_wave_initialize_hbx_politics`; `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:52-69`; `common/script_constants/006_independence_wave_pacific_constants.txt:38-41`; HBX party keys in `localisation/english/006_independence_wave_pacific_l_english.yml:2-9` | `PASS`; democratic ruling party, elections, 48/18/26/8 popularity split, and four named party surfaces are present. |
| Leader and portrait | `HBX_independence_wave_civic_convention_chair`; `common/characters/006_independence_wave_pacific_characters.txt:15-28`; `interface/006_independence_wave_pacific_portraits.gfx:11-14`; current localisation `...pacific_l_english.yml:11-12` | `PASS`; stable male civilian-large-only consumer now names William D. Stephens. |
| Flags and cosmetic identity | `HBX`, `PFX`; `common/countries/006_independence_wave_formable_cosmetics.txt:33-36`; `gfx/flags/{,medium/,small/}` | `PASS`; 15 HBX and 15 PFX files cover normal, medium, small, and five ideology variants. |
| Ideas and lifecycle | `hbx_divided_federal_arsenals`, `hbx_californian_ports_and_works_board`; `common/ideas/006_independence_wave_pacific_ideas.txt`; `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:149-166` | `PASS`; one crisis idea is always installed and swaps to the mature ports-and-works idea at coastal-command stability `68`. |
| Focus assignment and branch | `independence_wave_focus_tree`; seven HBX shared focuses in `common/national_focus/006_independence_wave_pacific_focus.txt:14-142`; parent focus inspection resolved 176/176 focus titles | `PASS` for HBX scope and wiring. The 14 fixed/relative-layout diagnostics are parent-wide shared-tree debt, not an HBX-specific route defect. |
| Decisions and mission | `independence_wave_hbx_hold_coastal_command_together`; six HBX decisions in `common/decisions/006_independence_wave_pacific_decisions.txt:10-168`; category in `common/decisions/categories/006_independence_wave_pacific_categories.txt:8-11` | `PASS`; costs, ownership, capital-control cancellation, AI weights, and cleanup IDs are present. |
| Force mapping | `regular_defectors`, `p184 = 76`; `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:185`; package constants `p184` profile `3`, reinforcement mask `590`, inheritance mask `3` | `PASS`; mapping decodes to secure depots, convert defectors, factory/rail guards, regional guards, professional officers, and both navy/air inheritance. |
| Starting force and technology | `independence_wave_apply_dynamic_starting_force`; `common/scripted_effects/006_independence_wave_force_effects.txt:286-463,523-551,718-887` | `PASS`; dynamic division/equipment/fuel outputs, researched-profile template, host-technology inheritance, minimum research slots, and bounded air/navy transfer are wired. |
| AI and playability | `common/ai_strategy/006_independence_wave_pacific.txt:9-37`; Pacific constants `...pacific_constants.txt:18-20` | `PASS`; survival production/building priorities, founding restraint, and severe-host-threat escalation are HBX-specific. |
| FORM-48 | `PFX`, `FORM-48`, HBX anchor `378`; `common/scripted_triggers/006_independence_wave_form48_triggers.txt:13-134`; `common/scripted_effects/006_independence_wave_form48_effects.txt` | `PASS` for strict route wiring; runtime remains unreachable until HBX is canonically admitted and the three-member ledger is populated. |
| SCN-008 | `SCN-008`, ranked `IW-184`; `common/scripted_effects/006_independence_wave_scenario_effects.txt:94-157,190-206,1000-1032`; scenario preflight in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:152-217` | `PASS` for registry/preflight wiring; the leading canonical attestation check still rejects HBX. |
| Cleanup | `independence_wave_cleanup_iw_184_california`; `common/scripted_effects/006_independence_wave_pacific_package_effects.txt:631-672,750-765` | `PASS`; six decisions, mission, ideas, setup flags, FORM-48 carrier candidate, focus tree, and HBX chair retirement are cleaned in the exact package scope. |

## File-surface checklist and findings

### Identity, tag, state, and host setup

- `HBX` is registered exactly once for IW-184 in `common/country_tags/006_independence_wave_countries.txt:102`, and `common/countries/006_independence_wave_HBX.txt` contains only graphical cultures and the intended map colour.
- `history/countries/HBX - California.txt` is correctly dormant at game start and recruits the stable civic-convention chair; it does not create unreviewed startup territory, forces, technology, or parties.
- The Event 006 registry and Americas/Caribbean package loader consistently pair `IW-184`, `HBX`, `RG-378`, and state `378`.
- The installed vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/378-California.txt` defines state `378` as USA-owned, metropolis-category California with 5,677,248 manpower, oil `120`, aluminium `8`, infrastructure `3`, two arms factories, six industrial complexes, two dockyards, air base `10`, and naval bases at provinces `1562`, `9671`, `9814`, and `610`.
- The mod has no `history/states` override for state `378` or California, so the package uses the current installed map rather than a stale copied state file.
- `can_initialize_independence_wave_iw_184_package` and `has_prepared_independence_wave_iw_184_package_setup` require the event-target anchor to be state `378`, owned and controlled by HBX, the former host to exist and not equal HBX, the former host's protected state to remain host-owned, and HBX's capital to be state `378`.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:268-299,321-341` transfers only frozen plan states and sets the new country's capital to the frozen anchor before package setup.
- `common/scripted_effects/chaosx_liberation_release_effects.txt:233-421,1341-1455` selects a safe host-remnant state with capital preference, records original capitals, relocates a host capital before ownership mutation, and restores it on pre-mutation failure.
- No state, province, railway, supply-node, port, or host-survival defect was found in the HBX-specific package surfaces.

### Politics, leader, portrait, flag, party, and advisor surfaces

- The runtime sets democratic rule with elections enabled and popularity values democratic `48`, communist `18`, neutrality `26`, and fascist `8` from centralized Pacific constants.
- The four party names are California Civic Convention, Pacific Labor Congress, California State Defense Board, and Open Pacific Sovereignty League, with complete player-facing localisation.
- `HBX_independence_wave_civic_convention_chair` remains the stable character key, has `gender = male`, uses only `civilian.large`, and is promoted with `ideology = centrism`.
- The promoted localisation is `William D. Stephens`, with a description framing his real former-governor and Los Angeles civic-leadership background as an alternate-history emergency-convention role.
- The current package and runtime DDS files are byte-identical, `156x210`, legacy uncompressed DDS, header size `124`, pixel-format size `32`, pixel-format flags `65`, `DDSCAPS_TEXTURE`, and SHA-256 `a158a968a1e67f2f83720d1b9201369542c3aaf7318a8c6332d659d91382cad1`.
- The current promoted portrait manifest and GFX handoff under `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/california_william_stephens_trial_01/` match this current hash and explicitly document the male civilian-large-only surface.
- No HBX advisor, dossier, operative, commander, or `_small` portrait derivative exists or is referenced; this is intentional and matches the character definition.
- The country has complete normal, medium, and small HBX flag ladders with five ideology variants each, and the FORM-48 PFX family has the matching 15-file ladder.
- Two package ideas use the existing shared Event 006 icons `independence_wave_fragmented_command` and `independence_wave_founding_identity`; both GFX textures exist.
- Documentation-only staleness remains in the superseded July 17 fictional-Daniel-Mercer portrait package and its `7cd867...` DDS evidence, and in the pre-promotion independent portrait handoff that still describes the former name. The current runtime source of truth is the July 24 Stephens promotion manifest/GFX handoff and the current `A158A...` DDS hash; this does not affect runtime ownership.

### Focus, decisions, mission, ideas, and assets

- HBX receives the full `independence_wave_focus_tree` framework only after `has_focus_tree = generic_focus`; the exact setup then loads the full tree and rejects an additive overlay.
- The seven HBX focus IDs are `independence_wave_hbx_screen_federal_arsenals_focus`, `independence_wave_hbx_reopen_coastal_supply_bureaus_focus`, `independence_wave_hbx_seat_sacramento_civic_convention_focus`, `independence_wave_hbx_bind_ports_factories_and_guard_focus`, `independence_wave_hbx_settle_federal_asset_ledger_focus`, `independence_wave_hbx_charter_pacific_procurement_board_focus`, and `independence_wave_hbx_convene_pacific_maritime_congress_focus`.
- Their prerequisites form the intended arsenal/supply and civic-convention split, converge at `bind_ports_factories_and_guard`, then split into host settlement and Pacific procurement before the dual-prerequisite maritime-congress capstone.
- All seven focus names, descriptions, tooltips, and seven package-specific DDS icons are present; the icon GFX file defines both base and `_shine` sprite names.
- The parent read-only focus inspection parsed the shared tree with 176 focuses and 176 titles. It reported 14 blocking fixed/relative layout diagnostics in authored shared-tree connectors, but no evidence ties those diagnostics to HBX IDs; no broad tree rewrite was made.
- The HBX decision category is visible only for `is_independence_wave_hbx_package = yes`.
- The founding mission is `independence_wave_hbx_hold_coastal_command_together`; its activation is setup-complete-only, its timeout/cancellation path marks founding success or failure, and its decision surface is intentionally unavailable for direct manual activation.
- The six project decisions are `independence_wave_hbx_screen_federal_arsenals`, `independence_wave_hbx_reopen_coastal_supply_bureaus`, `independence_wave_hbx_seat_sacramento_civic_convention`, `independence_wave_hbx_settle_federal_asset_ledger`, `independence_wave_hbx_charter_pacific_procurement_board`, and `independence_wave_hbx_prepare_pacific_maritime_congress`.
- Each decision has a package gate, capital-control or route-specific availability, a concrete cost trigger and tooltip, a timed completion path, cancellation/failure handling, and a bounded AI weight.
- All six decision keys, descriptions, project tooltips, and the founding-failure tooltip are present in `localisation/english/006_independence_wave_pacific_l_english.yml:52-72`; all seven focus keys and their tooltips are present at `:119-139`.

### Starting military, technology, industry, supply, and production

- The force mapping row at `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:185` assigns California the `regular_defectors` profile, military tradition `76`, regular defectors plus industrial/coastal units, and navy/air support conditioned on base and depot screening.
- The exact dispatch constants encode profile `p184 = 3`, reinforcement mask `p184 = 590`, and inheritance mask `p184 = 3`; mask `590` decodes to regional guards, secure depots, convert defectors, factory/rail guards, and professional officers, while mask `3` enables both navy and air inheritance.
- The dynamic force effect creates a bounded six-infantry-plus-artillery regular-defectors template with artillery and reconnaissance support, calculates divisions and stockpiles from population, factories, infrastructure, ports, supply nodes, host force, chaos, legitimacy, patron, network, territory, and force level, and stamps generation/package provenance on created divisions.
- Technology is inherited from the former host through `inherit_technology`; research slots are raised to the centralized minimum and can reach the industrial slot threshold when the factory gate is met.
- Opening stockpiles are dynamic infantry, support, artillery, train, motorized, convoy, and fuel values. Host land forces and general stockpiles are not blindly copied.
- Approved navy and air transfer is bounded to armed/high-chaos force levels and the encoded inheritance flags, using `5%/10%` ratios from centralized constants; baseline compact release does not receive unrestricted host fleets or aircraft.
- The vanilla California anchor is an unusually large industrial and maritime state, so the package's own design note correctly records snowball and officer-autonomy risk rather than granting extra static factories in HBX history.
- The AI prioritizes army `70`, infantry/support/artillery/train/convoy production, infrastructure `55`, industry `50`, dockyards `60`, and escalates to army `105` plus coastal bunkers `90` only under a severe host threat. Founding restraint avoids starting wars while California is neither a regional power nor under severe host threat.
- No missing starting technology, production-line, supply, or equipment surface was found in the HBX-specific implementation. Runtime force output is intentionally dynamic and depends on the frozen host/map inputs.

### AI, FORM-48, SCN-008, and cleanup

- `common/ai_strategy/006_independence_wave_pacific.txt:9-37` contains three HBX-specific strategies: industrial survival, founding restraint, and severe-host-threat response.
- `common/scripted_triggers/006_independence_wave_form48_triggers.txt:13-134` requires HBX to be the exact `IW-184` carrier at anchor `378`, prevents cosmetic-tag reuse, requires the maritime-congress or high-chaos route, and requires exactly HBX, HAW, and FSM country/anchor/invitation arrays for mutation.
- HBX setup sets `independence_wave_hbx_form48_carrier_candidate`, the Pacific Regional Federation family, and the registry surface, but the FORM-48 path remains unreachable while IW-184 is outside the canonical attestation set. This is the intended fail-closed state, not an implementation fallback.
- SCN-008 ranked registry construction includes `IW-184` at `common/scripted_effects/006_independence_wave_scenario_effects.txt:204`, and the scenario preflight includes the exact `IW-184`/HBX tag branch at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:212-217`.
- SCN-008 intensity behavior is centralized in `common/scripted_effects/006_independence_wave_scenario_effects.txt:94-157`: low means anchor/fragile/calm-world values, medium means compact/viable/rising-chaos values, high means extended/armed/total-chaos values, and maximum means extended/high-chaos/world-collapse values; high and maximum also accelerate ambition, with maximum opening the high-chaos lane and hidden formables.
- SCN-008 type behavior is centralized in `...scenario_effects.txt:1000-1032`: sovereign scatter adds no extra type effect, common congress forms the league/congress, wars of separation starts all former-host wars, universal belligerence applies one of former-host/neighboring-release/nearby-nonleague bounded rules, patron worlds assigns patrons, and great partition advances territory one tier before reservation when unique-anchor and host-remnant proofs allow it.
- The allocator audit passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, automatic counts `3 / 4 / 5 / 7 / 10`, intensity labels low/medium/high/maximum, six scenario types, and the required Event 005-anchor -> Event 006-anchor -> optional territory -> lock order.
- Event 006 cleanup removes the HBX founding mission, all six HBX decisions, both HBX ideas, HBX state/route/carrier/lifecycle flags, the FORM-48 researched flag, and the HBX chair, then restores `generic_focus` if the full Event 006 tree was loaded.

## Missing or stale country-package surfaces

1. `IW-184` is not present in the canonical runtime content-attestation OR block, so automatic planning and scenario preflight remain zero/blocked even though the package adapter, region loader, ordinary preflight branch, and SCN-008 branch exist.
2. `common/scripted_triggers/006_independence_wave_triggers.txt:584-914` has Event 005 liberation-capacity witness functions for the currently admitted package list but no `independence_wave_liberations_capacity_try_iw_184` branch. The shared transactional allocator still protects host remnant and anchor state, but the parent should review/add the admission-time capacity witness when IW-184 is admitted.
3. The shared focus tree still reports 14 fixed/relative layout diagnostics in the parent focus inspection. No HBX-specific connector was identified, so this audit leaves the parent-wide layout debt untouched.
4. Superseded July 17 Daniel Mercer portrait evidence and the pre-promotion Stephens audit handoff retain historical name/hash text. Current runtime files and the July 24 sourced-portrait manifest/GFX handoff are internally consistent; documentation reconciliation is recommended after admission.

## Files and identifiers inspected

Core gameplay surfaces inspected include `common/country_tags/006_independence_wave_countries.txt`, `common/countries/006_independence_wave_HBX.txt`, `history/countries/HBX - California.txt`, `common/characters/006_independence_wave_pacific_characters.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`, `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`, `common/scripted_effects/006_independence_wave_execution_effects.txt`, `common/scripted_effects/chaosx_liberation_release_effects.txt`, `common/scripted_effects/006_independence_wave_force_effects.txt`, `common/scripted_effects/006_independence_wave_force_package_effects.txt`, `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt`, `common/ideas/006_independence_wave_pacific_ideas.txt`, `common/national_focus/006_independence_wave_pacific_focus.txt`, `common/national_focus/006_independence_wave_focus.txt`, `common/decisions/006_independence_wave_pacific_decisions.txt`, `common/decisions/categories/006_independence_wave_pacific_categories.txt`, `common/ai_strategy/006_independence_wave_pacific.txt`, `common/scripted_triggers/006_independence_wave_form48_triggers.txt`, `common/scripted_effects/006_independence_wave_form48_effects.txt`, `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt`, `common/scripted_triggers/006_independence_wave_packages_region_14_triggers.txt`, `common/scripted_effects/006_independence_wave_scenario_effects.txt`, and `common/scripted_triggers/006_independence_wave_triggers.txt`.

Asset and localisation surfaces inspected include `localisation/english/006_independence_wave_countries_l_english.yml`, `localisation/english/006_independence_wave_pacific_l_english.yml`, `interface/006_independence_wave_pacific_portraits.gfx`, `interface/006_independence_wave_pacific_focus_icons.gfx`, `interface/006_independence_wave.gfx`, `interface/006_independence_wave_form48.gfx`, `gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds`, the July 24 sourced-portrait manifest/GFX handoff, the Pacific focus-icon manifest/GFX handoff, the Pacific FORM-48 asset manifest/GFX handoff, and the complete `HBX`/`PFX` flag ladders.

Research and map surfaces inspected include `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row `IW-184`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` row `IW-184`, `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv` row `RG-378`, `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` row `IW-184`, and the installed vanilla state file `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/378-California.txt`.

No country gameplay file, tag file, state file, focus file, decision file, idea file, AI file, localisation file, GFX file, or asset file was changed by this audit. The only new file is this handoff.

## Meaningful validation and scenarios

- `python .tools/audit_event6_allocator.py` passed with the package, scenario, count, and reservation-order totals recorded above.
- A direct current DDS header/hash check passed for the promoted runtime file and the package final DDS: both are `156x210`, valid legacy uncompressed DDS, and byte-identical at SHA-256 `a158a968a1e67f2f83720d1b9201369542c3aaf7318a8c6332d659d91382cad1`.
- A direct localisation coverage check found all seven HBX focus keys, six HBX decision keys, the HBX mission key, and their player-facing descriptions/tooltips in the UTF-8-with-BOM Pacific localisation file.
- A direct asset inventory found all 15 HBX flag variants, all 15 PFX flag variants, all seven HBX focus textures, the two HBX lifecycle idea textures, and the stable HBX portrait sprite/texture path.
- The installed-tag collision evidence at `docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_24.json` records zero Event 006 tag collisions, zero custom-cosmetic collisions, 102 Event 006 tags, 122 Workshop roots, and four local mod roots. That report was generated before the portrait-only promotion; the promotion did not alter tags, so its collision result remains applicable. A fresh full scan was attempted but exceeded the 124-second command window while traversing all installed Workshop archives and wrote no files.
- The parent-provided read-only focus inspection resolved 176 focus titles from `independence_wave_focus_tree` and identified 14 parent-wide layout diagnostics; no HBX-specific layout failure was attributed.
- No live ordinary release, SCN-008 launch, FORM-48 mutation, rollback, or in-game map execution was run in this subagent turn. Those scenarios remain parent validation after canonical admission.
- The installed package exposes no Technology Tree Viewer, so technology behavior was checked through the documented `inherit_technology` runtime path and vanilla documentation rather than a technology-viewer render.

## Remaining risks and required parent follow-up

- Add IW-184 to the canonical runtime content-attestation OR block only after parent review, then verify ordinary release and SCN-008 preflight become positive for `IW-184/HBX`.
- Recheck the joint Event 005/Event 006 capacity contract because the current Event 005 witness wrapper enumerates only currently admitted IDs and has no IW-184-specific capacity witness.
- Rerun the allocator audit and a dry-run/review/apply/post-validation release transaction with state `378`, a USA host remnant, and a non-capital protected host state after admission.
- Exercise SCN-008 at low, medium, high, and maximum intensity and each of the six type families, confirming that HBX appears only when its exact tag/anchor/host proofs pass and that FORM-48 remains gated by the three-member consent ledger.
- Reconcile superseded Daniel Mercer asset/handoff documentation and the source-of-truth map after the canonical admission decision; do not treat those historical files as current runtime consumers.

## Simplifications, omissions, and blockers

No gameplay simplification, fallback, identity redesign, focus-tree rewrite, asset substitution, or broad balance change was made. The only blocker is the parent-owned canonical attestation decision, plus the explicitly recorded parent-wide focus-layout diagnostics and post-admission runtime scenarios that were outside this read-only country-package audit.
