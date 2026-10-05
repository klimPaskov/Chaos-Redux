# Event 015 Country, Idea, Achievement, and Asset Audit — 2026-10-05

## Authority and disposition

This handoff records the resumed country, idea, achievement, and asset review assigned on 2026-10-05, including the parent-authorized narrow political-state guard and two achievement call-boundary fixes.

The requested path did not exist at the start of this review, so this file is the new durable handoff.

Disposition: the identity teardown and achievement-helper corrections below are implemented; the surviving 50-idea removal-cost patch is verified; the parent-owned generic-tree return is present in the shared source; the approved-light-tree restriction is a design deviation the parent will surface; fresh source-lineage revalidation remains unresolved because the former asset workspace and row-level crosswalk are absent.

No country tag, state, party, leader definition, focus definition, localisation key, formable, map, production line, or asset file was changed by this subagent.

## Country-package coverage checklist

| Surface | Coverage | Evidence and current status |
| --- | --- | --- |
| Country tag registration, country definition, history, names, parties, flags, diplomacy, and setup | Not audited in this bounded resume | Event 015 transforms the existing recipient tag; no tag or country setup file was touched. |
| State ownership, controllers, cores, claims, capital, supply, rail, ports, resources, buildings, and victory points | Not audited | No map or state file changed, so no map MCP route was in scope. |
| Release, spawn, annexation, subject, civil-war, and cosmetic-tag cleanup | Partial, identity teardown only | Existing teardown still removes only Event 015's eight leadership roles and drops a cosmetic tag only when it is one of the five Event 015 identities. Other release and annexation logic remains with its owner. |
| Leaders, portraits, advisors, parties, ruling ideology, and elections | Partial, teardown ownership path | Current ruling leadership is checked before Event 015 retires its synthetic leaders; politics restore only when an Event 015 leader or the saved original leader is still ruling. The four institutional leader images use institutional names and are shared by four founder/successor pairs. |
| Focus-tree assignment, replacement, route reachability, and safe-state return | Focus return checked; MCP blocked | The parent added a generic-origin receipt and a guarded return path. Approved-light origins remain excluded until a literal return mapping exists. Focus inspect and render timed out. |
| Idea definitions, lifecycle, icons, and route play | Source lifecycle and runtime icon wiring checked | All 50 defined ideas appear in add and remove lifecycle blocks; each has `removal_cost = -1`; 12 referenced idea sprites resolve. No idea modifier was changed. |
| Decisions, missions, tooltips, and option effects | Only the two achievement call paths checked | Decision content remains owned by the decision agent. That owner confirmed its standalone renunciation action has no later peaceful-case recorder consuming the transient output. |
| Achievements | Need, Not Greed evidence path checked; all icon triplets checked | `utopia_manifesto_need_not_greed` requires the peaceful-case proof and obsolete-case-renunciation flag. Its 14 achievement definitions have 42 matching runtime and GFX states. |
| Starting army, navy, air force, templates, equipment, technology, research, industry, fuel, and supply | Not audited | No military, technology, industry, or supply setup was in the assigned file surface. |
| AI strategy, focus weights, diplomacy weights, and playability | No weights changed | The parent-owned approved-light eligibility restriction changes the random-event candidate pool; the active probability auditor should include it in the same-scenario postpatch comparison. |
| Localisation coverage | No keys changed or renamed | Other localisation is owned by the text agent. No new player-facing requirement or identity string was added here. |
| Asset paths, registrations, hashes, and provenance | Runtime coverage checked; source lineage partly unresolved | Current runtime assets and registrations are present. Historical asset handoffs preserve aggregate provenance and review results, but their cited source workspace and requirement-to-runtime crosswalk are no longer present. |

## Changed behavior and identifiers

Before this patch, `utopia_manifesto_teardown_identity_package` retired Event 015 leaders and unconditionally restored the saved party, leader, and election state. That could replace the party, leader, and election settings of another package that had installed a foreign successor while Event 015 was active.

`utopia_manifesto_snapshot_identity_political_ownership` now records a temporary country flag, `utopia_manifesto_identity_politics_owned_at_teardown`, only when the current ruling leader is one of Event 015's eight synthetic leaders or is the saved original character and still the active country leader. Teardown restores the saved politics only when that snapshot is present, then clears it.

The eight checked Event 015 leader ids are `utopia_manifesto_household_assembly`, `utopia_manifesto_commonwealth_council`, `utopia_manifesto_council_of_callings`, `utopia_manifesto_rotating_congress`, `utopia_manifesto_board_of_measure`, `utopia_manifesto_college_of_measure`, `utopia_manifesto_stewardship_council`, and `utopia_manifesto_directorate_of_service`.

This preserves full repeal for a baseline, unformed, or Practical Commonwealth country when its saved original leader is still active, while leaving a foreign successor's current politics intact.

The peaceful-case achievement helper now rejects method `renunciation` before evaluating either negotiated methods or the domestic-substitution branch. This prevents a still-live domestic-review flag from letting an obsolete case count as peaceful.

The `.54.a` obsolete-renunciation event option and `utopia_manifesto_close_obsolete_case_after_treaty_refusal` now initialize caller-owned `utopia_manifesto_achievement_case_target_input` to zero and `utopia_manifesto_achievement_case_method_input` to `unset` before calling the renunciation recorder. The nested helper's `renunciation` override therefore survives until `utopia_manifesto_record_achievement_peaceful_case_resolution` consumes it.

The normal `utopia_manifesto_case_target_id` remains available during both recorder calls and is cleared later by the central active-case cleanup. It is copied to the persistent peaceful-target array before that cleanup. The array rejects a target id that has already been counted, so repeating or reusing a stale target cannot increase the distinct-target count.

Domestic substitution still requires both `utopia_manifesto_case_closed_for_domestic_alternative` and `utopia_manifesto_domestic_alternative_found`. The recorder clears the case-closed receipt after processing; the domestic-review resolver clears its live result before recomputing it.

The separate decision action `decision_utopia_renounce_need_case` calls the obsolete-renunciation recorder but does not call the peaceful-case recorder afterward. Its decision owner confirmed there is no nested cleanup or recorder that consumes those temporary values, so no preinitialization was added there.

The surviving idea patch adds `removal_cost = -1` to all 50 Event 015 idea definitions. This disables manual removal while scripted lifecycle effects can continue to replace and remove ideas. The current idea file diff adds 50 lines and changes no modifiers.

| Idea family | Exact idea ids |
| --- | --- |
| Found Manifesto | `utopia_manifesto_found_manifesto`, `utopia_manifesto_found_manifesto_mitigated`, `utopia_manifesto_found_manifesto_failure` |
| Unmeasured Country | `utopia_manifesto_unmeasured_country`, `utopia_manifesto_unmeasured_country_mitigated`, `utopia_manifesto_unmeasured_country_final`, `utopia_manifesto_unmeasured_country_failure` |
| Inherited Order | `utopia_manifesto_inherited_order`, `utopia_manifesto_inherited_order_mitigated`, `utopia_manifesto_household_land_trusts`, `utopia_manifesto_common_ownership`, `utopia_manifesto_measured_tenure`, `utopia_manifesto_state_allotment`, `utopia_manifesto_mixed_property_order`, `utopia_manifesto_inherited_order_failure` |
| Charter of Households | `utopia_manifesto_charter_of_households`, `utopia_manifesto_charter_of_households_mitigated`, `utopia_manifesto_charter_of_households_failure`, `utopia_manifesto_charter_of_households_final` |
| Common Table | `utopia_manifesto_common_table`, `utopia_manifesto_common_table_mitigated`, `utopia_manifesto_common_table_failure`, `utopia_manifesto_common_table_final` |
| Perfect Measure | `utopia_manifesto_perfect_measure`, `utopia_manifesto_perfect_measure_mitigated`, `utopia_manifesto_perfect_measure_failure`, `utopia_manifesto_perfect_measure_final` |
| Closed Island | `utopia_manifesto_closed_island_idea`, `utopia_manifesto_closed_island_mitigated`, `utopia_manifesto_closed_island_failure`, `utopia_manifesto_closed_island_final` |
| Practical Commonwealth | `utopia_manifesto_practical_commonwealth_idea`, `utopia_manifesto_practical_commonwealth_mitigated`, `utopia_manifesto_practical_commonwealth_failure`, `utopia_manifesto_practical_commonwealth_final` |
| Common Store Network | `utopia_manifesto_common_store_network`, `utopia_manifesto_common_store_network_mitigated`, `utopia_manifesto_common_store_network_failure`, `utopia_manifesto_common_store_network_final` |
| Garden District Network | `utopia_manifesto_garden_district_network`, `utopia_manifesto_garden_district_network_mitigated`, `utopia_manifesto_garden_district_network_failure`, `utopia_manifesto_garden_district_network_final` |
| Auxiliary Dependency | `utopia_manifesto_auxiliary_dependency`, `utopia_manifesto_auxiliary_dependency_mitigated`, `utopia_manifesto_auxiliary_dependency_failure` |
| Stewardship Burden | `utopia_manifesto_stewardship_burden`, `utopia_manifesto_stewardship_burden_mitigated`, `utopia_manifesto_stewardship_burden_failure`, `utopia_manifesto_stewardship_burden_final` |

No achievement id, tag, state id, character id, party name, focus id, localisation key, or formable id was added or renamed by this subagent.

## Parent-owned focus-tree return and design deviation

The Event 015 acceptance effect previously loaded `utopia_manifesto_tree` once, while `utopia_manifesto_enter_disable_safe_state` cleared Event 015 state without loading another tree. Installed focus-tree scoring is selected before game start and is not automatically recomputed when `utopia_manifesto_accepted` is cleared, so the safe-state path could leave an existing recipient on the Utopia tree after its route state was removed.

The parent has added `utopia_manifesto_original_tree_generic` capture before the acceptance-time tree load. On safe-state entry, the parent now returns to literal `generic_focus` only when that receipt is present and the active tree is still `utopia_manifesto_tree`, then clears the receipt. The active-tree check preserves a later tree replacement installed by another package.

The parent has also set `utopia_manifesto_candidate_has_approved_light_tree` to a hidden false trigger. The two manual flags `utopia_manifesto_tree_replacement_approved` and `utopia_manifesto_tree_replacement_mature` have no producers in the repository, and the approval flag alone does not identify an exact return tree. This restricts approved-light entrants until a literal capture-and-return mapping exists; it is a design deviation from the specification's repository-approved replaceable-tree allowance, and the parent will surface it rather than silently using generic as a fallback.

That parent-owned restriction is in `common/scripted_triggers/015_utopia_manifesto_triggers.txt`; it is included here as shared-source integration evidence, not attributed to this subagent.

No arbitrary `token:<focus_tree_id>` capture or dynamic `load_focus_tree` effect was added. The offline wiki lists known tokenizable datatypes but does not list focus-tree ids; it says any raw token may be tokenized while warning that this use is rare and arguably buggy. Installed documentation supports generic meta-effect and meta-trigger text generation, but neither it nor vanilla examples verify a focus-tree id token roundtrip.

The current full-repeal specification describes replacing the accepted recipient's tree and says rejection leaves the original tree unchanged; it does not define a return-tree contract for full repeal. The current parent-owned generic return is source-backed; return mappings for non-generic approved-light trees remain unresolved.

## Idea lifecycle, achievement, and asset coverage

`common/scripted_effects/015_utopia_manifesto_country_effects.txt` removes every defined stage in the 12 staged idea families and supplies the corresponding add/replace effects. A static identifier pass found 50/50 definitions with an add path and 50/50 with a remove path.

The 12 picture ids used by the 50 ideas are `utopia_found_manifesto`, `utopia_unmeasured_country`, `utopia_inherited_order`, `utopia_charter_of_households`, `utopia_common_table`, `utopia_perfect_measure`, `utopia_closed_island`, `utopia_practical_commonwealth`, `utopia_common_store_network`, `utopia_garden_district_network`, `utopia_auxiliary_dependency`, and `utopia_stewardship_burden`.

The five cosmetic-tag stems are `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH`, `UTOPIA_MANIFESTO_COUNCIL_UNION`, `UTOPIA_MANIFESTO_PLANNED_UTOPIA`, `UTOPIA_MANIFESTO_CLOSED_ISLAND`, and `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH`; each has an unsuffixed file plus `_communism`, `_democratic`, `_fascism`, and `_neutrality` variants in each size folder.

All 12 idea sprite paths exist under `gfx/interface/ideas/015_utopia_manifesto/`, and `interface/015_utopia_manifesto.gfx` contains the corresponding sprite definitions.

That folder and GFX file also contain 29 additional `idea_utopia_*` DDS/sprite pairs with no consumers found outside their own sprite definitions. The unmatched ids are `idea_utopia_arbitration_tables`, `idea_utopia_civic_wardens`, `idea_utopia_common_administration`, `idea_utopia_common_stores_unproven`, `idea_utopia_compulsory_assignments`, `idea_utopia_empty_stores`, `idea_utopia_feared_doctrine`, `idea_utopia_foreign_laughter`, `idea_utopia_guild_congress`, `idea_utopia_guilds`, `idea_utopia_household_councils`, `idea_utopia_household_guard`, `idea_utopia_island_discipline`, `idea_utopia_league_of_need`, `idea_utopia_living_humanism`, `idea_utopia_marked_bounds`, `idea_utopia_marked_bounds_doctrine`, `idea_utopia_necessary_commonwealth`, `idea_utopia_needful_land`, `idea_utopia_new_utopia`, `idea_utopia_paper_utopia`, `idea_utopia_public_storehouses`, `idea_utopia_store_state`, `idea_utopia_storekeeper_commission`, `idea_utopia_unproven_common_stores`, `idea_utopia_useful_arts`, `idea_utopia_utopian_league`, `idea_utopia_vocation_accord`, and `idea_utopia_vocation_confusion`. The deleted manifest prevents distinguishing obsolete art from an accepted non-idea consumer, so these files and sprite definitions were left in place.

The 14 Event 015 achievements remain defined in `common/achievements/chaos_redux_achievements.txt`; all 42 active, grey, and not-eligible icons exist under `gfx/achievements/` and have matching sprite registrations in `interface/015_utopia_manifesto.gfx`.

The 14 achievement ids are `utopia_manifesto_no_place_but_home`, `utopia_manifesto_need_not_greed`, `utopia_manifesto_every_calling_chosen`, `utopia_manifesto_two_year_table`, `utopia_manifesto_archipelago_of_small_places`, `utopia_manifesto_inland_island`, `utopia_manifesto_gold_for_common_use`, `utopia_manifesto_the_joke_understood`, `utopia_manifesto_consent_of_the_governed`, `utopia_manifesto_the_perfect_measure`, `utopia_manifesto_closed_circle`, `utopia_manifesto_no_foreign_hands`, `utopia_manifesto_the_stores_remain`, and `utopia_manifesto_no_one_in_chains`.

The five active route proclamation slots are `96` through `100` and map to `GFX_super_event_015_consent_of_households`, `GFX_super_event_015_common_table`, `GFX_super_event_015_guardians_of_measure`, `GFX_super_event_015_closed_island`, and `GFX_super_event_015_joke_understood`. All five GFX paths, runtime DDS files, and scripted-localisation slot mappings exist. Two legacy DDS files, `super_event_utopia_marked_bounds.dds` and `super_event_utopia_new_utopia.dds`, are present in the same folder but are not referenced by these active slots.

Four institutional leader DDS files exist under `gfx/leaders/015_utopia_manifesto/`, and sixteen advisor DDS files exist under `gfx/leaders/015_utopia_manifesto/advisors/`. All twenty paths map through `interface/015_utopia_manifesto.gfx` to the character references in `common/characters/015_utopia_manifesto_characters.txt`.

The institutional character ids are `utopia_manifesto_household_assembly`, `utopia_manifesto_commonwealth_council`, `utopia_manifesto_council_of_callings`, `utopia_manifesto_rotating_congress`, `utopia_manifesto_board_of_measure`, `utopia_manifesto_college_of_measure`, `utopia_manifesto_stewardship_council`, and `utopia_manifesto_directorate_of_service`; four people-free institutional portraits serve those eight roles.

These leader names identify governing bodies rather than individual chairpersons, and the character-file overview states that the recipient's original leader remains through the founding debate. No one-person random leader pool or gender pairing was added by this patch. Advisor portrait pixels and gender/name pairing were not re-reviewed because the source contact sheets and portrait manifest are absent from the current workspace; the prior asset handoffs remain historical evidence only.

The sixteen advisor ids are `utopia_manifesto_interpreter`, `utopia_manifesto_general_provisioner`, `utopia_manifesto_secretary_of_callings`, `utopia_manifesto_surveyor_of_shores`, `utopia_manifesto_civic_engineer`, `utopia_manifesto_keeper_of_stores`, `utopia_manifesto_league_envoy`, `utopia_manifesto_advocate_of_limits`, `utopia_manifesto_public_auditor`, `utopia_manifesto_constitutional_jurist`, `utopia_manifesto_council_organizer`, `utopia_manifesto_social_workshop_planner`, `utopia_manifesto_chief_surveyor`, `utopia_manifesto_standards_engineer`, `utopia_manifesto_steward_of_service`, and `utopia_manifesto_contract_broker`.

The final sound file exists at `sound/015_utopia_manifesto/super_event_57_utopia_has_neighbors.wav`, is registered by `sound/chaosx_sound.asset`, and currently hashes to `05da5a30ba49c6592e5295dd499e9ad3e97279586bb7e7d51228ad236ce58655`, matching the durable Event 015 audio research record.

Current path-and-content manifest digests below are SHA-256 over sorted repo-relative `path|whole-file-sha256` rows. They preserve the exact current runtime family inventory without opening image pixels.

| Runtime family | Current files | Unique whole-file hashes | Path-and-content manifest SHA-256 |
| --- | ---: | ---: | --- |
| Referenced idea icons under `gfx/interface/ideas/015_utopia_manifesto/` | 12 | 12 | `5cdad0328125b0740fdbf0a1b03d32aab42fd3bd22b8e4727d8d0cd90655407f` |
| Achievement triplets under `gfx/achievements/` | 42 | 42 | `bf99702a087a044e0cc38fe58df7f40d0ba1e186a7793ab1fe62d0366a2788ef` |
| Normal route flags under `gfx/flags/` | 25 | 21 | `6e95ebfd7473b1723fa51e57b2088446d5e6879ce1f360a0f221bf56dd56bd16` |
| Medium route flags under `gfx/flags/medium/` | 25 | 21 | `e72cb7f6658ad900c5cb7c5c065b53bc0b53224fb698696be73a781c5d95ddbc` |
| Small route flags under `gfx/flags/small/` | 25 | 21 | `6731a61f35246fbb70bc0a64300a19341bcade0505762be6d77ce3a372f77d46` |
| Institutional leader portraits | 4 | 4 | `40e62847887a301e2c32c8c20675ae1b826f2085f4015d05bfd53102141309cb` |
| Advisor portraits | 16 | 16 | `dfb788dd9c3d9fde5168d30b61aae6d137d110bd52eac54872cbe2ffa64309dd` |
| Active route proclamation images | 5 | 5 | `5ab7354e11fe75dce6b23934d94087a273d155f124d550ab22f639530caae89c` |

All 75 route flags have the required normal `82x52`, medium `41x26`, and small `10x7` dimensions, uncompressed 32-bit TGA image type `2`, eight alpha bits, and bottom-left origin. Each size ladder has 21 unique whole-file hashes; the four expected aliases are the only duplicates.

All 12 idea icons, 42 achievement icons, four institutional portraits, sixteen advisor portraits, and five active route images have valid one-level uncompressed BGRA DDS headers, the expected dimensions, and exact byte lengths.

No runtime reference into `docs/assets/` was found in the scoped idea, achievement, portrait, flag, or super-event registration files.

The historical visual/provenance reviews are in `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/advisor_asset_final_audit_2026_07_18.md` and `asset_completion_final_requirement_reaudit_2026_07_16.md`. They document prior ImageGen source review, decoded-pixel equality, and a prior 24/24 requirement crosswalk, but their source records point into the removed `docs/assets/015_utopia_manifesto/` workspace. That workspace and its `manifest.md`, `gfx_handoff.md`, and `requirement_to_runtime_coverage_2026_07_16.md` are absent; no copy of those row-level records was found. The absence alone is expected cleanup after completed asset work, but the current source-master lineage and row-level crosswalk cannot be reopened for this re-audit.

The prior portraits were not regenerated or replaced. The surviving audits attest to fictional built-in ImageGen sources and prior identity/style review, but no `chaosx_portrait_creator`-owned handoff or current portrait-source manifest is present in this workspace. Portrait production ownership is therefore not independently revalidated here.

`docs/specs/015_utopia_manifesto_specs/matrices/asset_manifest_plan.md:3` still points to the absent asset manifest and GFX handoff, and it records an outdated SHA-256 for the current advisor final-audit handoff. The current `advisor_asset_final_audit_2026_07_18.md` SHA-256 is `e2062f21a09a887d26f11bc0563b969a957c89fa13999acd729f65cee31632b1`, not the matrix's recorded `d2f659ac4e968a9d48ae3f346c1a7d9d5e1cb6b09b67f3be16a789662b583693`.

No image was opened or generated during this review. The old contact-sheet and pixel-roundtrip claims remain historical audit evidence rather than a new visual review.

## Files and identifiers

| File | Change or disposition |
| --- | --- |
| `common/scripted_effects/015_utopia_manifesto_identity_effects.txt` | Added `utopia_manifesto_snapshot_identity_political_ownership`; added the ownership-gated political restore; tightened the peaceful-case method gate so renunciation cannot pass through the domestic branch; retained the existing cosmetic-tag and unique-target safeguards. |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | Added the caller-owned zero/unset temporary initialization immediately before the obsolete-renunciation and peaceful-case helpers in `utopia_manifesto_close_obsolete_case_after_treaty_refusal`. The file also contains separate parent-owned focus-origin and safe-return edits. |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | Parent-owned change hides the approved-light predicate until an exact tree return mapping exists. |
| `events/015_utopia_manifesto.txt` | Added the same target/method temporary initialization immediately before the renunciation and peaceful-case helpers in option `chaosx.nr15.54.a`. |
| `common/ideas/015_utopia_manifesto_ideas.txt` | Surviving in-progress patch reviewed: 50 `removal_cost = -1` rows, no modifier changes. This subagent did not add further idea-file edits during the resume. |
| `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/country_release_audit_2026-10-05.md` | Created this handoff because the requested file was absent. |

Current whole-file SHA-256 values include parent-owned concurrent edits where they share a file: identity effects `30e2ef0768d92dc7c496147ebbe305bced096ac480e0fb1a9d7468c60407b2ed`, ideas `57ef7afc6002ca5e7d774e287a614b13b80e0c435f50722223cfa41d12e270fc`, main effects `3768e3089a82caf5dacfee7f0059b35207546a491deda011884b168cff1c6ee5`, events `55a18a9102a81810291b2b4af55bd1349fa4301b88f1f309889872bd271464a8`, and parent-owned triggers `0f545614ec86dba0f5f587db0f44e0b7a222a250e94430344c6785db893fabda`.

No tag, state, leader, party, focus-tree id, localisation key, formable id, or asset file was added by this subagent. The new country flag is `utopia_manifesto_identity_politics_owned_at_teardown`; the new effect is `utopia_manifesto_snapshot_identity_political_ownership`; the changed achievement proof is `utopia_manifesto_need_not_greed`.

The parent-owned focus-return flag is `utopia_manifesto_original_tree_generic`, and the parent-owned safe-state effect is `utopia_manifesto_enter_disable_safe_state`. These are listed to make the shared-file handoff reviewable, not attributed to this subagent.

## Validation and evidence limits

The local lifecycle pass found 50/50 defined ideas with an add path and 50/50 with a remove path. The current idea diff adds 50 removal-cost lines and no modifier lines.

The current asset-path pass found 12/12 referenced idea icons, 42/42 achievement triplet files and GFX sprites, 75/75 route flags with valid TGA headers, 20/20 portrait paths and GFX/character mappings, and 5/5 active route proclamation slots. DDS metadata checks covered the required dimensions, uncompressed BGRA masks, texture caps, and byte lengths; TGA checks covered image type, bit depth, alpha-bit count, dimensions, and bottom-left origin.

The teardown trace verified the eight Event 015 current-leader checks, the saved-original-character check, the restore guard, and the flag cleanup. Installed `has_country_leader` documentation and the vanilla PRC achievement use the explicit `ruling_only = yes` form; the dynamic original-character check uses character-scope `is_country_leader = yes` and an existing `var:` character-scope pattern.

The case-close trace verified both caller preinitializations occur before the renunciation helper, the renunciation override reaches the peaceful-case recorder, the live normal target id remains present until after the recorder, and the duplicate target array rejects repeated ids. The decision owner separately confirmed its renunciation decision has no downstream recorder consuming the temporary output.

`hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.source_lookup` were exposed but each bounded call timed out after 25 seconds. The exact local wiki and installed-game sections were read directly instead; no MCP source revision was returned.

The targeted `hoi4.event_inspect` request for `chaosx.nr15.1` (`mode=trace`, depth `3`, `25` nodes, `35` edges, no refresh) and the matching neighborhood `hoi4.event_render` request both timed out after 25 seconds. The targeted national focus inspect and render for `utopia_manifesto_tree` also timed out after 25 seconds. No event/focus artifact or comparison was returned; the source review is not treated as engine evidence.

The corrected `hoi4.script_validate` attempt for the country-scope ownership-snapshot effect timed out after 25 seconds. Its initial request had an out-of-range `limit=40` schema error; the corrected request used the exposed maximum `limit=32` and produced no validation result.

No event compare was run because neither inspect nor render returned a graph artifact to compare. No focus compare artifact was available because focus inspect and render returned no result; the focus-tree source file itself was unchanged. No AI weight or strategy factor was changed by this subagent; the parent-owned approved-light candidate-pool restriction must be covered by the active probability auditor's same-scenario postpatch comparison.

No live game was launched. No image was generated or replaced. No workbook, export CSV, or commit was produced.

## Remaining issues, omissions, and owner handoff

The current generic-origin focus return is source-backed, but the specification has no explicit full-repeal tree-return requirement and approved-light origin mappings remain unresolved. The parent-owned `always = no` approved-light gate is a safety restriction and design deviation; the parent should report that reduced eligibility as instructed.

The event and focus MCP evidence gates remain blocked by the exact timeouts above. Source-only inspection is not a substitute for those routes.

The historical asset audits remain useful evidence, but their source manifests, prompt records, and row-level requirement-to-runtime crosswalk are not present in the current workspace. The parent or documentation owner should reconcile the stale asset-plan pointer and decide whether the promoted audit summaries are sufficient for release documentation.

The 29 unconsumed idea sprite/DDS pairs are left in place pending that manifest reconciliation; they have no current idea-picture consumer in the searched script, interface, event, or localisation sources.

Portrait runtime coverage is present, but portrait-worker ownership and current source-master lineage are unresolved. No portrait repair was attempted because the parent expressly reserved portrait replacement and any generation for root coordination.

Map/state setup, military/technology/industry/supply starting setup, focus-route depth/AI, and the separate decision implementation were outside this bounded patch and remain with their assigned owners.

## Local reference evidence

| Rule or precedent | Local source and line span | SHA-256 |
| --- | --- | --- |
| `removal_cost = -1` blocks manual spirit removal | `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md:350-358` | `a6405eb98a02a9de4689b7c0ef80b5a887b6c6c747d3907f68c109ed3fd099ac` |
| Vanilla permanent idea precedent | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ideas/afghanistan.txt:16` | `6552a3a0f024e52b941426e5b02cc2aec3129306139ccf31b6d75f7697cf6d30` |
| Country-scoped ruling leader predicate | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:3640-3652` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Character-scoped current leader predicate | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:5408-5415` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Vanilla `has_country_leader` current-ruler example | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/achievements.txt:1346` | `2b7b3d3a3f1a45707af283b111d541a2caff0b23c53eb748c59f079afc3d429c` |
| Variable character scopes and temporary helper-output lifetime | `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:431-449` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Country tree score selection and lack of automatic refresh | `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:45-68,1137-1140` | `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203` |
| Explicit active-tree switching effect | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:4771-4787` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Active focus-tree identity trigger | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:3954` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| General string-built effect and trigger syntax | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:4833-4850`; `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:6404-6423` | effects `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`; triggers `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Vanilla generic tree id | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/generic.txt:19` | `da7d2ad989fe174a904838d55481bcfd07d652940260466259cb27dd21893768` |
| Vanilla explicit tree transition after a generic-tree check | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/07_nsb_on_actions.txt:561` | `939ea1c0cc25c2ce4390d7dda4a8ac84547978931fae36c09d0fab7d7ec79966` |
| Token-valued variable caution and `GetTokenKey` use | `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:955-985` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |

Skills applied: `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, and `.agents/skills/chaos-redux-focus-trees/SKILL.md`. No skill was created or updated.
