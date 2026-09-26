# Read-Only Focus-Tree Audit Handoff: IW-040/KUB

**Date:** 2026-09-26. **Scope:** bounded audit of the implemented IW-040/KUB five-focus group against accepted Part 4/Part 5 and its 2026-09-26 addendum. **Disposition:** source route logic matches the accepted group; one unregistered focus-search filter needs review; imported-node layout proof and route-aware AI comparison remain blocked or unresolved.

This audit is read-only for gameplay and localisation. This handoff is the only file written. No tests were added or run, and HOI4 was not launched.

## Acceptance and design boundary

Part 4 records the accepted IW-040/KUB five-focus group and its explicit source acceptance basis in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md:695-707`. Part 5 records the package coverage and unresolved imported-node layout and AI evidence in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md:80`. The controlling detail is `docs/plans/006_independence_wave_plans/006_event6_reg04_kuban_focus_group_improvement_addendum_2026-09-26.md:15-65`.

The user explicitly selected root-level `shared_focus` definitions imported into the full Event 006 tree and accepted imported-node MCP layout evidence as blocked. No direct-focus duplicate is proposed or needed. Broad tree redesign, new route families, and unrelated KUB package systems were outside this audit.

## Files inspected

- `common/national_focus/006_independence_wave_focus.txt`
- `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt`
- `common/scripted_effects/006_independence_wave_kuban_package_effects.txt`
- `common/scripted_effects/006_independence_wave_focus_effects.txt`
- `common/decisions/006_independence_wave_frontier_decisions.txt`
- `common/script_constants/006_independence_wave_constants_registry.txt`
- `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`
- `localisation/english/006_independence_wave_focus_l_english.yml`
- `localisation/english/006_independence_wave_frontier_l_english.yml`
- `interface/006_independence_wave.gfx`
- `docs/events/006_independence_wave/kuban_package.md`
- Accepted Part 4 and Part 5 files and the KUB improvement addendum listed above.
- `AGENTS.md`; `.agents/skills/chaos-redux-focus-trees/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; and the relevant event, decision, and event-asset skills.
- Offline Paradox wiki pages for National focus modding, Effects, Triggers, Scopes, Localisation, Data structures, Modifiers, On actions, Event modding, Decision modding, Idea modding, AI modding, and AI focuses.
- Installed vanilla `common/focus_inlay_windows/documentation.md` and the shared-focus precedent in vanilla `common/national_focus/austro_hungarian_releasable_shared.txt` and `austria.txt`. The installed `documentation` directory contains no dedicated national-focus Markdown reference; the focus documentation found in another vanilla folder covers focus inlay windows.

## Route coverage

| Accepted route | Source evidence | Audit result |
|---|---|---|
| `independence_wave_kub_record_stanitsa_petitions` opens after `independence_wave_prepare_capital_administration`; 5 units; Civic Concord +5. | `006_independence_wave_focus.txt:5038-5063`; reward initializes both deltas and uses the clamped helper. | Present; root does not call the generic depot/provisional-assembly callback. |
| `independence_wave_kub_reconcile_grain_and_rail_registers` follows the root; 5 units; Mounted Readiness +5. | `006_independence_wave_focus.txt:5065-5087`. | Present; distinct logistics/admin reward, no generic depot receipt or construction reward. |
| Hearing branch `independence_wave_kub_hear_non_host_petitions` follows reconciliation; 7 units; Civic +10, Mounted Readiness -5; matching paid-project companion +5 Civic once. | `006_independence_wave_focus.txt:5091-5122`; companion helper at `006_independence_wave_kuban_package_effects.txt:361-373`. | Present; reciprocal exclusion with the service branch; reward and companion remain branch-specific. |
| Service branch `independence_wave_kub_audit_mounted_service_roll` follows reconciliation; 7 units; Civic -5, Mounted Readiness +10; matching paid-project companion +5 Mounted Readiness once. | `006_independence_wave_focus.txt:5126-5156`; companion helper at `006_independence_wave_kuban_package_effects.txt:375-387`. | Present; reciprocal exclusion with the hearing branch; no unit spawn or generic guard-integration callback is granted by the focus. |
| `independence_wave_kub_publish_land_and_service_docket` follows either selected branch through one explicit OR prerequisite; 7 units; +5 to both ledgers. Availability also requires that same branch and its matching paid-only project receipt. | `006_independence_wave_focus.txt:5161-5198`. | Present; neither generic callback flag can satisfy the docket. The focus does not claim former-host settlement, claims, cores, network entry, or FORM-08 consent, matching the accepted non-promises. |

The five IDs each have one root-level `shared_focus` definition and one import, at `006_independence_wave_focus.txt:90-94` and `5038, 5065, 5091, 5126, 5161`. All five imports are inside `focus_tree = { id = independence_wave_focus_tree }` at lines 37-94. The bounded search of `common/national_focus/` found no direct-focus duplicate or import into another tree.

Selected KUB path cost is 5/5/7/7 = 24 units or 168 nominal days, after the existing 5-unit/35-day capital-administration focus. This arithmetic does not establish the 600-day mission's feasibility or project affordability.

## Package, origin, setup, framework, and anchor gates

`can_use_independence_wave_kub_reg04_focus_group` at `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt:45-52` requires an active Event 006 country, exact KUB package identity and IW-040 package id, complete package setup, the full-focus-framework gate, the generic focus contract, and state 234 owned and controlled by ROOT and marked as the capital. `is_independence_wave_active_country` requires the active-origin flag and Event 006 liberation-origin value and rejects an ended origin (`006_independence_wave_triggers.txt:9-14`). The package predicate requires `original_tag = KUB`, active package content, and the IW-040 id (`006_independence_wave_kuban_package_triggers.txt:11-15`).

The complete-setup trigger additionally checks prepared setup, both package/setup-complete flags, origin activation readiness, aligned registries, current-country membership in the active and network arrays, and network membership (`006_independence_wave_kuban_package_triggers.txt:234-244`). The full-framework and generic-focus contract require the active package content plus full-framework ownership and the assigned `independence_wave_focus_tree` contract (`006_independence_wave_focus_triggers.txt:32-68`). Every node gates `allow_branch`, `available`, and its focus reward with the KUB group trigger; new capture, transition, and companion helpers also recheck their appropriate KUB/full-tree conditions.

Prerequisite semantics are correct: each branch has the common reconciliation prerequisite, the two branch exclusions are reciprocal, and the docket's OR prerequisite is separate from its AND-of-branch-and-matching-receipt availability gate. The imported shared-focus design is consistent with the offline wiki and vanilla shared-focus precedent.

## Ledger, receipt, companion, and lifecycle audit

`independence_wave_kuban_pressure` defines bounds 0-100, starting values 34/41, stability threshold 60, minor gain 5, standard gain 10, and minor loss -5 (`common/script_constants/006_independence_wave_constants_registry.txt:6335-6352`). Each focus reward sets both temporary deltas, uses zero for the unchanged ledger, and calls `independence_wave_change_kub_compact_values`; that helper applies and clamps both variables, refreshes the compact/fragmented idea, and refreshes country state (`common/scripted_effects/006_independence_wave_kuban_package_effects.txt:32-67`). The matching companion helpers also initialize both deltas and clamp through the same helper.

The transition tooltip captures both pre-reward values, refreshes the lifecycle after the reward, and shows `independence_wave_kub_compact_stability_reached_tt` only when the compact is now stable and the two ledgers were not both already at threshold (`006_independence_wave_kuban_package_effects.txt:70-99`). The localized tooltip exists at `localisation/english/006_independence_wave_focus_l_english.yml:570`. Source arithmetic recorded in the accepted addendum leaves the focus-only route short of both 60-point thresholds; the group alone does not resolve the mission.

The docket checks only `independence_wave_kub_community_compacts_project_paid` after the hearing branch or `independence_wave_kub_border_guards_project_paid` after the service branch (`006_independence_wave_focus.txt:5170-5187`). The two receipts are written in their successful `remove_effect` handlers after the existing package callback (`common/decisions/006_independence_wave_frontier_decisions.txt:734-758, 800-824`). Their `cancel_effect` handlers apply failure effects and do not set a paid receipt (`:766-771, 832-838`). Generic flags such as `independence_wave_kub_communities_guaranteed` and `independence_wave_kub_guards_integrated` are not used as docket receipts.

Both orderings are idempotent. If the branch focus completes first, its caller finds no paid receipt and the helper does nothing; successful project expiry then requires that exact focus completed and the award marker absent before invoking the same helper. If the paid project completes first, the later branch focus sees its matching receipt and awards once. The helper itself rechecks the full group gate, matching payment flag, and absence of its award marker, setting the marker before applying the delta (`006_independence_wave_kuban_package_effects.txt:361-387`; decision call sites at `:737-757, 803-823`).

Setup clears both paid receipts before initialization and invokes full-framework assignment (`006_independence_wave_kuban_package_effects.txt:421-459`). Package cleanup clears both paid receipts and package lifecycle flags (`:507-593`). Companion markers are cleared with the full focus-history reset in `independence_wave_assign_focus_framework`, which uses `load_focus_tree = { tree = independence_wave_focus_tree keep_completed = no }` (`common/scripted_effects/006_independence_wave_focus_effects.txt:55-75`). This matches the accepted distinction: payment receipts follow package setup/cleanup; companion markers follow focus history.

## Missing or simplified content

No accepted focus ID, branch, prerequisite, paid-receipt condition, ledger delta, companion, transition tooltip, or reused focus icon is absent from the bounded five-node route. The branch is not a fake fork: it trades between different ledgers and requires different paid projects. The small ledger rewards are connected to the package's visible stability mechanic rather than repeated generic political-power or factory rewards.

The docket intentionally does not settle the former-host relationship or grant claims, cores, network admission, or formable consent. Those absences are specified in the accepted addendum and are not omissions in this tranche. The source-level group also does not by itself achieve both stable ledgers or resolve the founding mission; that limitation is documented and remains a campaign-balance question.

## Icon coverage

| Focus ID | Icon ID | Registration and backing DDS | Source result | MCP visibility |
|---|---|---|---|---|
| `independence_wave_kub_record_stanitsa_petitions` | `GFX_goal_independence_wave_founding_administration` | `interface/006_independence_wave.gfx:3`; `gfx/interface/goals/006_independence_wave/goal_independence_wave_founding_administration.dds` exists. | Registered; unique within group. | Blocked because imported nodes are omitted. |
| `independence_wave_kub_reconcile_grain_and_rail_registers` | `GFX_goal_independence_wave_infrastructure_authority` | `interface/006_independence_wave.gfx:19`; `gfx/interface/goals/006_independence_wave/goal_independence_wave_infrastructure_authority.dds` exists. | Registered; unique within group. | Blocked because imported nodes are omitted. |
| `independence_wave_kub_hear_non_host_petitions` | `GFX_goal_independence_wave_popular_councils` | `interface/006_independence_wave.gfx:7`; `gfx/interface/goals/006_independence_wave/goal_independence_wave_popular_councils.dds` exists. | Registered; unique within group. | Blocked because imported nodes are omitted. |
| `independence_wave_kub_audit_mounted_service_roll` | `GFX_goal_independence_wave_army_integration` | `interface/006_independence_wave.gfx:17`; `gfx/interface/goals/006_independence_wave/goal_independence_wave_army_integration.dds` exists. | Registered; unique within group. | Blocked because imported nodes are omitted. |
| `independence_wave_kub_publish_land_and_service_docket` | `GFX_goal_independence_wave_former_host_settlement` | `interface/006_independence_wave.gfx:21`; `gfx/interface/goals/006_independence_wave/goal_independence_wave_former_host_settlement.dds` exists. | Registered; unique within group. | Blocked because imported nodes are omitted. |

No focus icon is missing or repeated within this group. The sprite registrations and DDS paths are also listed in `docs/events/006_independence_wave/kuban_package.md:23-27`. The audit checked registration and file existence, not the artwork's visual quality or in-tree visibility.

## Localisation and reward mismatches

All five focus title, description, and reward-tooltip keys are present, as are the two companion tooltips, the docket's positive and blocked paid-gate tooltips, and the conditional stability tooltip (`localisation/english/006_independence_wave_focus_l_english.yml:551-570`). The two paid-receipt effect tooltips are present in `localisation/english/006_independence_wave_frontier_l_english.yml:210-211`. The displayed reward names and clamp-aware “can rise/fall by up to” wording match the actual ledger changes. No mechanical reward/localisation mismatch was found.

| Priority | Key | Difference from accepted addendum | Effect |
|---|---|---|---|
| Low | `independence_wave_kub_record_stanitsa_petitions_desc` (`focus_l_english.yml:552`) | Localisation says “Host communities”; the accepted route text says “Host villages.” | Meaning remains aligned with the +5 Civic Concord reward; exact copy has drifted. |
| Low | `independence_wave_kub_hear_non_host_petitions_desc` (`focus_l_english.yml:558`) | Localisation says “land and service record”; accepted text says “service and land record.” | Meaning and +10/-5 tradeoff remain aligned; wording order has drifted. |

The docket description matches the addendum's current “lists rights under review, mounted-service obligations, and claims still requiring talks with the former host” wording. Localisation key coverage was checked; UTF-8 BOM/encoding was not independently verified.

## AI behavior gaps

No `ai_will_do` block appears in the five KUB focus definitions, and no `focus_factors` or `ai_national_focuses` entry for these IDs was found in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`. The existing KUB strategy profile covers mounted survival production/building and former-host restraint (`:1696-1722`), not ledger-sensitive choice between the petition and service branches. The paired paid decisions are gated by mission resolution, affordability, and serialization, but their AI scores are not tied to the selected KUB focus branch (`common/decisions/006_independence_wave_frontier_decisions.txt:713-776, 778-838`). Thus the accepted route preference remains unverified and may permit a project choice that does not match the eventual focus branch; the docket itself still fails closed on mismatched branch/receipt pairs.

The accepted plan does not authorize numeric focus, decision, timing, or random weights. The required read-only `chaosx_ai_probability_auditor` returned `PROBABILITY_SOURCE_INSPECTED` for `common/national_focus/006_independence_wave_focus.txt`, revision `e4267fdccbb5caf9aea80aec2474dcfae9602346b731a1ae420b2cb9a1cb9640`, source hash `4c4d2a35e6897758371f2332c04835794838e71e60ae5f558492c485f633d283`, with 184 candidates, 0 available candidates, 17 required inputs, `poolComplete=false`, and no candidate examples. The zero available count came from inspection without campaign state and does not establish that no KUB focus is available. [Probability inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b62b658ec7d25ed6fddcf8f71642c0f0ef3b77b67da4894b04360747f70868/15732a04974d8219066c42e0919697da179887b14cd223d1f808f59642cd2d18/probability-inspect-4c4d2a35e689.json).

The artifact read failed with `MCP error -32603: Artifact provenance manifest is unavailable`, so the required-input names could not be recovered. An evaluation probe using empty scenario set `iw040-kub-no-campaign-fixture-provided` was rejected with `Too small: expected array to have >=1 items at scenarioSet.scenarios`. A sweep probe with the same empty set and no invented paths was rejected with that error plus `Too small: expected array to have >=1 items at sweep.paths`. Neither probe produced an analysis artifact. No valid campaign scenario IDs, traces, rankings, selection probabilities, timing results, or comparison artifacts exist. Compare was not run because there is no source patch or complete typed baseline; the current file was not self-compared. The candidate pool and external factors remain incomplete, so ranking, starvation, dominance, and route preference remain unresolved.

The auditor found no explicit `ai_will_do` on the five focus definitions and no target-specific `focus_factors` or ordered-focus entries in `common`. The offline wiki describes the omitted-block default score as 1, but that is documentation-based context, not an MCP score trace or a recommended weight. No numeric weights are added or recommended. Route-aware AI comparison remains unresolved.

## Focus MCP evidence and limits

This audit ran `hoi4.focus_inspect` and `hoi4.focus_render` on `common/national_focus/006_independence_wave_focus.txt` for `independence_wave_focus_tree`.

The fresh inspector returned `FOCUS_INSPECTED`, revision `3b1cb81a4b87c30e7f75d06fa896dbd1d4e421760029f306a132306c3085ff3c`, 184 direct focus nodes, 196 connectors, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, zero crossings, zero node intersections, zero too-close pairs, and one long connector. [Fresh focus inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12b6c0d8adba50b73ddd5c68b6d6f33bd4065a4b6606b8bbae54d999c0d7c602/99268935fd4ab67465f41895ae514c446939756f19bd4a1d0a323964f76cc42d/focus-inspect.3b1cb81a4b87c30e.json). The task-supplied post-change receipt revision `abfac347f793f1880cb1020e579a3a96cfb86842fb22b986f1cd2d566ec8c4ea` reports the same direct counts and layout hash; [supplied receipt artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8cd2f83c97661cc511887e0e5e068a6146cf4c6b8a2acf454dd3794b64caf60/ade344ec3aa14ca4469bb42c8776f1a4fdfa5ff3b6f2279366fc93d441d761f7/focus-inspect.abfac347f793f188.json).

The fresh focus render returned `FOCUS_RENDERED` with the same layout hash. Artifacts: [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef1b58529ae71e05e1afccafede1221bfd12998c83fefab2d631251cae96c968/4b6f716546a7a9cc92875b0a41f3addac1e2c54510bdfe95427621c78a6a25d2/independence_wave_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/6b65bb42dcd78cfc2b5d857050a18939f793a6ac21108478ab2446794258f828/independence_wave_focus_tree.focus.svg), [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/626472a6eb9914cd0d7b57deff7d5b9ca88d429672064b6a8a96384c9cb240af/c1d740e78a9bf1564e9c678fa2a4a2467f944326b06849a3518af85762d7257e/independence_wave_focus_tree.focus.json), and [source map](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/daa5c3e1457a46dbb03e9d992babfcb0d1b47942b4ffe0e1bfe3d52d4d04b664/c857a79fb59d493338146802e17ed54346ee5bf6fd5113af878dc322592e97ef/independence_wave_focus_tree.focus.source-map.json).

The task-supplied receipt, this audit's fresh inspect, and the probability auditor's separate inspect revision `666ad1c923955705ba25af5e026053425fb63bc77281e80243116b9d242fdf59` all report 184 direct focuses, 196 connectors, and the same layout hash; their source revisions differ, and the cause is not established here. All omit the imported root-level shared nodes. They therefore do not prove KUB attachment, coordinates, connector geometry, overlap, route layout, or icon visibility. The user-selected shared-focus decision leaves precisely that visual proof blocked; these receipts are not KUB layout acceptance. The fresh direct-tree render's 10-column warning is for `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine` at `006_independence_wave_focus.txt:801-819`, outside the imported-node proof. Its `FOCUS_LOCALISATION_REFERENCE_MISSING` warning is the vanilla `continuous_restrict_freedom_desc`, also unrelated to KUB. The source inventory diagnostic says inline reporting was capped at 64 of 92 paths; linked artifacts are available for the complete inventory.

## High-priority follow-up and remaining risks

1. Review `FOCUS_FILTER_LOGISTICS` on `006_independence_wave_focus.txt:5072`. The offline focus page describes custom filters as requiring a matching `GFX_FOCUS_FILTER_*` sprite and localisation key; the base-game filter list does not contain `FOCUS_FILTER_LOGISTICS`, and repository/installed-vanilla searches found no matching sprite or localisation registration. This appears to reinstate an unregistered filter token. Source reference: `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:455-487`; compare the KUB line with `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md:693`, which records earlier REG-03 unregistered-filter cleanup.
2. Review the service branch's `FOCUS_FILTER_WAR_SUPPORT` tag at `006_independence_wave_focus.txt:5134`; this focus changes Civic Concord and Mounted Readiness, not HOI4 war support. `FOCUS_FILTER_MANPOWER` may be thematically intended by the service-roll concept, but neither tag is backed by a direct manpower/war-support effect in this focus.
3. Keep route-aware focus/paid-project AI marked unresolved until the specialist probability route can use complete typed campaign scenarios and return scenario-specific inspect/evaluate/sweep/compare evidence. No numeric weights are recommended.
4. Keep imported-node layout and icon visibility marked blocked until the focus MCP includes root-level shared-focus imports or another accepted evidence route is established. Do not use a direct-focus duplicate as a workaround.
5. Align the two low-priority focus description strings if exact accepted wording is required. Verify localisation encoding in the normal parent review; it was not checked here.

No live campaign, full 600-day mission deadline, whole-tree branch audit, or complete decision/mission balance comparison was performed. Those remain outside this bounded source review or depend on the missing typed probability baseline. The focus source, route gates, matching receipt logic, clamping, idempotence, transition tooltip, key coverage, and sprite registration were reviewed; no gameplay or localisation source was edited.

## Parent integration (2026-09-26)

The parent replaced the new grain-and-rail focus's unregistered `FOCUS_FILTER_LOGISTICS` with the installed vanilla `FOCUS_FILTER_INDUSTRY`, and replaced the service-roll focus's irrelevant `FOCUS_FILTER_WAR_SUPPORT` with `FOCUS_FILTER_MANPOWER`. The offline focus-filter reference documents `FOCUS_FILTER_MANPOWER` as a base filter, and installed vanilla national focuses use it. The parent also aligned the two flagged focus descriptions exactly with the accepted KUB addendum: “Host villages” and “service and land record.”

Route-aware focus and paid-project AI remains unresolved pending complete typed campaign scenarios and scenario-specific probability inspect/evaluate/sweep/compare evidence. Imported-group geometry and visibility remain blocked as MCP evidence under the user's selected shared-focus design.
