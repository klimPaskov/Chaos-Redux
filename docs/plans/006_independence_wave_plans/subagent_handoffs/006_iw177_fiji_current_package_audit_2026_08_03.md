# Event 006 IW-177 FIJ current country-package audit handoff (2026-08-03)

## Outcome

The current IW-177 Fiji package is internally coherent at source level, and this audit found no narrow country-package defect that can be repaired without changing an accepted admission contract.

No gameplay, map, tag, localisation, asset, readiness, attestation, or fallback patch was made.

FIJ remains a fail-closed package candidate because the planner still has a legacy content-ready gate, the central runtime content-attestation list excludes `iw_177`, the strongest Sukuna source is circa 1940s against the 1936 baseline, and the named FORM-39 FIJ/PNG/WPG research, consent, X-tag, flag, identity, and route inputs remain unresolved.

## Authority and scope

The audit used the current `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, the Event 006 resume and completion packets, the accepted IW-177 and FORM-39 handoffs, current FIJ package source, the accepted registry and installed-map binding rows, the installed vanilla FIJ country and state files, the offline Paradox wiki pages required by `AGENTS.md`, and relevant vanilla HOI4 documentation.

No obsolete pasted flag-log material was used.

## Country-package coverage checklist

- **Tag and registration: PASS at source.** `original_tag = FIJ`, package id `constant:independence_wave_package_id.iw_177`, anchor state `636`, and reservation group `RG-PACIFIC-ISLANDS` agree in the package loader and triggers. The accepted registry row resolves to the registered vanilla tag `FIJ`; the `GUX` value in the legacy `provisional_new_tag` column is not selected by the current binding.

- **Country and state baseline: PASS at source.** The package deliberately reuses vanilla FIJ and does not create duplicate country history or a mod state file.

- **Politics and party setup: PASS at source.** Setup applies the baseline laws, democratic elections, popularity constants `44/12/34/10`, four FIJ party-name pairs, centrism leadership, provisional authority, and five FIJ ledger variables.

- **Leader and roster: CONDITIONAL.** `FIJ_independence_wave_founding_congress_chair` is recruited by the hidden origin-roster event, is male, and is promoted as the ruling centrism country leader. The one-person leader has no opposite-gender name-pool or metadata pairing.

- **Focus framework: PASS at source; live rendering open.** Setup only replaces vanilla `generic_focus`, assigns the full shared `independence_wave_focus_tree`, imports the FIJ roots, and excludes additive overlay behavior.

- **Decisions and mission: PASS at source.** The founding-congress mission and six staged decisions have visibility, costs, timers, cancellation, timeout, host-loss, effect, and cleanup paths.

- **Ideas and ledgers: PASS at source.** The three FIJ lifecycle ideas are mutually refreshed, and congress pressure, communal authority, shipping access, colonial accounts, and defense readiness are initialized and clamped.

- **Force package: PASS at source; live materialisation open.** The p177 mapping is `coastal_maritime`, tradition `53`, reinforcement mask `659`, navy-only inheritance mask `1`, and research sensitivity `0`. Mask `659` decodes to five pathways: integrate militias, regional guards, volunteer corridors, terrain units, and professional officers.

- **AI: PASS at source; balance open.** The three FIJ strategies cover coastal congress survival, founding restraint, and severe-host-threat response with documented vanilla building and equipment identifiers.

- **Cleanup: PASS at source.** FIJ cleanup removes its mission, six decisions, three ideas, ledger variables, route and lifecycle flags, formable selection, shared focus ownership, and the Event 006 leader. It does not fabricate external FORM-39 research receipts.

## File surface checklist

- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` defines `is_independence_wave_fij_package`, FIJ leadership and congress-state predicates, `can_initialize_independence_wave_iw_177_package`, `has_prepared_independence_wave_iw_177_package`, and `has_complete_independence_wave_iw_177_package_setup`.

- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` defines FIJ leadership and politics preparation, ledger and lifecycle effects, six focus adapters, `independence_wave_setup_iw_177_fiji`, Pacific dispatch/final validation, and `independence_wave_cleanup_iw_177_fiji`.

- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt` and `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt` define IW-177 loading, weighting, planning, reservation, state `636`, and `RG-PACIFIC-ISLANDS` ownership.

- `common/national_focus/006_independence_wave_pacific_focus.txt` defines six FIJ focus ids, and `common/national_focus/006_independence_wave_focus.txt` imports the FIJ roots into the shared full framework.

- `common/decisions/categories/006_independence_wave_pacific_categories.txt` defines `independence_wave_fij_founding_congress_category`; `common/decisions/006_independence_wave_pacific_decisions.txt` defines mission `independence_wave_fij_hold_constituent_congress_together` and six FIJ decisions.

- `common/ideas/006_independence_wave_pacific_ideas.txt` defines `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact`.

- `common/characters/006_independence_wave_pacific_characters.txt`, `history/general/006_independence_wave_character_recruitment.txt`, and `interface/006_independence_wave_pacific_portraits.gfx` define the FIJ leader and its portrait consumer.

- `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds` is the provisional runtime consumer. Its validated SHA-256 is `31fea5eb5c7c4b6f34ec138ed6a3168a7c6c39755a992bd6abf0296c5838d2c6`, with exact `156x210` 32-bit DDS dimensions.

- `common/ai_strategy/006_independence_wave_pacific.txt` defines the three FIJ AI blocks, and `common/script_constants/006_independence_wave_pacific_constants.txt` plus `common/script_constants/006_independence_wave_force_package_constants.txt` provide the package tuning and p177 mapping.

- `common/scripted_triggers/006_independence_wave_form39_triggers.txt` and `common/scripted_effects/006_independence_wave_form39_effects.txt` own the exact FORM-39 FIJ member, research, consent, identity, mutation, and cleanup contract.

- `localisation/english/006_independence_wave_pacific_l_english.yml` contains the FIJ parties, leader, category, mission, six decisions, six focuses, three ideas, and tooltips. A targeted check found all 27 direct FIJ player-facing keys present.

## Missing or stale country-package surfaces

The planner function `can_plan_independence_wave_package_iw_177` still calls `is_independence_wave_candidate_tag_available`, which requires the absent `independence_wave_package_content_ready` flag. No FIJ source grants that publishable flag, so the automatic planner remains closed. This is consistent with the current fail-closed contract and requires parent-owned admission work rather than a FIJ setup shortcut.

The package dispatch adapter and scenario branch are present, but the central `has_independence_wave_runtime_package_content_attestation_for_execution_id` OR block does not contain `iw_177`. Runtime and scenario preflight therefore stop before mutation.

The installed HOI4 agent package exposes no Technology Tree Viewer, so technology-tree rendering and comparison remain an unresolved tooling limitation.

## Map and state setup issues

Vanilla `history/countries/FIJ - Fiji.txt` sets capital `636`, infantry weapons level `1`, twenty convoys, democratic 1936 politics, and no static OOB.

Vanilla `history/states/636-Fiji.txt` remains owner `ENG` with FIJ core, `small_island`, manpower `180000`, infrastructure `2`, province `4286` naval base `1`, victory point `4286`, provinces `4286/7302/12159`, and local supply `0.0`.

The loader, initializer, prepared-setup trigger, map binding, and reservation group all agree on state `636`; preparation additionally requires FIJ ownership/control and a living non-FIJ former host that retains its protected state. Static map safety is therefore a source pass.

Live allocator reservation, host survival, state transfer, supply flow, and save/load persistence were not run because this agent must not launch HOI4 and no live evidence was supplied.

## Politics, leader, portrait, flag, advisor, and party issues

`independence_wave_initialize_fij_politics` applies democratic `44`, communist `12`, neutrality `34`, and fascist `10` popularity, four party-name pairs, elections, and centrism leadership.

The strongest sourced identity is Ratu Sir Lala Sukuna, but the source is catalogued circa the 1940s while the Event 006 baseline is 1936. The 1929 Vishnu Deo candidate is anonymous in the source evidence and was not a founding-congress council member in 1936, so it cannot silently replace Sukuna. This remains a source/date/role blocker.

The portrait GFX basename and DDS consumer resolve, but the texture remains provisional and is not admission evidence.

The mod has no FIJ flag override; vanilla `FIJ_democratic`, `FIJ_neutrality`, `FIJ_fascism`, and `FIJ_communism` normal, medium, and small triplets are present. No FIJ advisor, operative, high-command, commander, small-portrait, or custom name-pool asset is required by the current package.

## Focus, decision, idea, and asset issues

The six focus ids are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus`.

The six decision ids are `independence_wave_fij_convene_constituent_congress`, `independence_wave_fij_register_communal_veto`, `independence_wave_fij_open_labor_shipping_board`, `independence_wave_fij_settle_colonial_accounts`, `independence_wave_fij_charter_coastal_guard`, and `independence_wave_fij_ratify_island_compact`.

The mission id is `independence_wave_fij_hold_constituent_congress_together`, and the three idea ids are `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact`.

All FIJ focus, decision, mission, idea, category, leader, and tooltip localisation keys are present, and the generic focus and shared icon texture paths resolve statically. Live focus rendering, decision timing, and tooltip display remain open validation items.

## Starting military, technology, industry, supply, and production issues

The dynamic starting-force path is guarded by Pacific command structure, command-roster readiness, current-generation mapping, anchor control, former-host safety, and the p177 mapping. The source contract does not add a large unsupported army or armor package.

The vanilla baseline supplies infantry weapons level `1`, twenty convoys, infrastructure `2`, a naval base at province `4286`, local supply `0.0`, and no FIJ-specific technology, production-line, railway, fuel, or industrial override. No static contradiction was found, but live force materialisation, production, resource flow, fuel, supply capacity, and technology behavior remain unvalidated.

## AI and playability issues

`independence_wave_fij_coastal_congress_survival` enables army, infantry, support, convoy, fuel-silo, infrastructure, and dockyard priorities.

`independence_wave_fij_founding_restraint` avoids starting wars when FIJ has no severe host threat and is not a regional power; `independence_wave_fij_host_threat` raises army and coastal-bunker priorities when severe host threat is present.

The building and equipment identifiers match the installed vanilla AI documentation and script-enum categories. AI focus ordering, one-state island resilience, naval inheritance, threat timing, post-release playability, and balance remain live-validation items.

## Diplomacy, host, ambition, and FORM-39 hooks

FIJ setup enables host negotiation, guarded frontier, association, reclamation, ambition, and league route flags through the shared focus adapters. The colonial-account focus/decision requires a living former host and does not automatically start a war or transfer an unbounded extension.

FIJ selects `constant:independence_wave_formable_family.melanesian_federation`. FORM-39 eligibility requires the FIJ route-adapter and member-research flags, exact PNG/IW-178 state `523` and WPG/IW-157 state `669` member inputs, frozen member and invitation arrays, consent, and exact anchors `636/523/669`.

The following admission inputs remain unset or review-closed: `independence_wave_fij_melanesian_route_adapter_complete`, `independence_wave_fij_melanesian_member_research_complete`, `independence_wave_png_melanesian_member_research_complete`, `independence_wave_wpg_melanesian_member_research_complete`, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, and `independence_wave_form39_identity_review_complete`.

MFX normal, medium, and small flag assets exist under `gfx/flags`, but the current FORM-39 identity manifest remains `needs_user_review`. The installed collision scan reports zero MFX collisions, which is useful safety evidence but does not promote the X-tag, identity, flat-flag, or route gates.

## Dispatcher, attestation, and cleanup

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` includes IW-177 in the runtime adapter and exact FIJ preflight/scenario identity branches, but not in the content-attestation OR list. `common/scripted_effects/006_independence_wave_package_planner_effects.txt` additionally requires that attestation before candidate plan publication.

FIJ cleanup clears its local package state and the route-selection/formable flags, while FORM-39 cleanup only clears runtime receipts. It does not manufacture research, consent, flat-flag, X-tag, or identity evidence, which is correct for the current admission design.

## Changed files and behavior

Changed files: this handoff only.

Before and after gameplay behavior is identical. No tag, state id, leader id, party, focus tree id, localisation key, formable id, asset, allocator row, dispatch entry, attestation entry, or readiness flag changed.

## Validation performed

Static checks covered FIJ tag and anchor consistency, package loader and setup/final-validation/cleanup paths, shared focus ownership, six decision ids, idea lifecycle, leader gender and portrait consumer, vanilla flag triplets, p177 force masks, AI identifiers, FORM-39 anchors and gate names, and cleanup ownership.

The direct FIJ localisation check covered 27 party, leader, category, mission, decision, focus, idea, and tooltip keys with no missing keys.

The portrait DDS was read-only validated as a `156x210` 32-bit DDS with the SHA-256 recorded above.

Vanilla FIJ history/state files, vanilla AI documentation, relevant vanilla script-enum categories, and all mandatory offline Paradox wiki pages were consulted.

## Skipped meaningful validation and remaining risks

Live HOI4 launch, allocator execution, state transfer, former-host survival, dynamic force materialisation, focus rendering, AI timing/balance, save/load rollback, FORM-39 consent execution, and final MFX identity/flag review were skipped because they require parent or player-owned runtime evidence.

Technology-tree rendering and comparison were skipped because the installed package exposes no Technology Tree Viewer.

No simplification or fallback was used. FIJ remains incomplete for admission until the source/date decision, named FORM-39 member research and consent contract, MFX X-tag/flat-flag/identity review, route-adapter writers, central attestation, and parent-owned runtime evidence are resolved.

No plan handoff beyond this audit was written because the remaining work is an admission and research decision rather than a narrow FIJ source repair.
