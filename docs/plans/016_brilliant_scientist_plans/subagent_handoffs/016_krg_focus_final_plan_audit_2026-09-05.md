# Event 016 KRG focus final-plan audit

Date: 2026-09-05.

Scope: bounded read-only audit of the KRG focus package against the accepted closure contract.

Status: no KRG gameplay, AI, localisation, icon, effect, trigger, constants, or idea file was changed, no focus was added or removed, and nothing was staged or committed.

## High-priority fixes first

No confirmed P1 source defect was found after the static route, reward, ownership, prerequisite, bypass, mutual-exclusion, icon, localisation, and AI-plan pass.

The main unresolved decision is the AI plan pre-start guard. All 19 plans use `allowed = { NOT = { original_tag = DJX } }` at `common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt:22,55,87,113,129,174,196,218,235,255,292,308,330,354,372,398,447,499,543`, while the accepted architecture document describes a KRG-ownership `allowed` guard. The current file header explicitly states that Event 016 may transform any valid non-DJX host and that the continuously evaluated `enable` block owns the runtime KRG guard. This is an acceptance discrepancy, not a confirmed runtime defect, so it was not patched without an owner decision and a before/after probability comparison.

Do not split `KRG_sustainable_project_capacity` into four AND prerequisites. Its single prerequisite block at `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1040` is an intentional OR over the four mutually exclusive supply focuses, with a separate OR in `available`.

## Route coverage table

| Focus ids | Source range | Coverage finding |
| --- | --- | --- |
| `KRG_audit_inherited_portfolio` through `KRG_complete_the_founding_audit` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:36-265` | Opening formation, origin survival, inherited portfolio, facilities, supply, and founding audit are present; setup and paid downstream consumers are wired. |
| `KRG_define_the_states_purpose` through `KRG_the_project_synthesis` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:294-787` | Directorate, human republic, clone, machine, temporal, xenobiological, and synthesis identity routes are present with route locks and causal project/identity checks. |
| `KRG_stabilize_the_laboratory_economy` through `KRG_sustainable_project_capacity` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:817-1034` | Economy, power, rail, portfolio, prototype, and four supply doctrines are present; supply choices are pairwise exclusive and project-facing. |
| `KRG_restore_the_ordinary_chain_of_command` through `KRG_a_council_of_project_commanders` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1064-1200` | Conventional security, officers, engineers, counterintelligence, airspace, general staff, and project-council consequences are present. |
| `KRG_audit_the_growth_halls` through `KRG_the_replicated_host` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1225-1348` | Cloning route has facility, nutrient, identity-law, cadre, drift, and replicated-state gates; deployment history and physical reserve/hatchery checks are delegated to canonical project triggers. |
| `KRG_wake_the_assembly_lines` through `KRG_an_army_of_machines` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1376-1501` | Robotics route has power, repair, command, rogue-node, and machine-state consequences; deployment and power/assembly checks are causal. |
| `KRG_open_the_restoration_ledger` through `KRG_the_dinosaur_host` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1529-1652` | Paleogenetics route has reserves, handlers, pens, escape, and dinosaur-state consequences; deployment requires history, sites-ready, reserve, and hatchery state. |
| `KRG_open_the_designed_organism_dossier` through `KRG_the_engineered_legion` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1679-1806` | Xenobiology route has vats, exact control, containment, red-team, and engineered-legion consequences; deployment requires history, exact control, sites-ready, vat, and control-center state. |
| `KRG_recover_the_transit_logs` through `KRG_the_strategic_transit_corps` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1834-1934` | Portal route has terminal audit, rings, depot, breach, and paid recruitment/insertion consequences. |
| `KRG_authenticate_the_temporal_ledger` through `KRG_the_continuity_guard` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:1962-2090` | Temporal route has evidence, anchor, synchronization, paid warning/stabilization operations, debt gate, and continuity-guard consequences; wartime warning readiness is enforced by `brilliant_scientist_kruger_focus_warning_operation_is_ready` at `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt:325-337`. |
| `KRG_build_an_independent_reactor_grid` through `KRG_authorize_agents_of_last_resort` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2118-2249` | High-energy, alien-arms, biological containment, and last-resort routes have delivery, interface, quarantine, and crisis consequences with facility and project-history gates. |
| `KRG_a_state_without_friends` through `KRG_build_the_submission_network` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2276-2367` | Diplomacy and intelligence branches provide foreign bureau, former-host, commonwealth, and submission outcomes with pairwise route locks. |
| `KRG_secure_the_laboratory_corridors` through `KRG_the_continental_laboratory_network` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2392-2478` | Expansion and integration branches require military reach, valid targets, compliance/time, recovered facilities, and supplied continental network. |
| `KRG_evolution_four_sovereign_science` through `KRG_commit_to_the_strategic_singularity` | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt:2503-2578` | Evolution IV requires identity plus project capstone history; Laboratory World and Strategic Singularity are pairwise mutually exclusive terminal commitments with distinct causal effects. |

## Missing or simplified content

No missing focus ID, route family, focus AI block, direct focus reward consumer, concrete project gate, or terminal commitment was confirmed.

The source intentionally uses category-seed flags for paleogenetics at `KRG_open_the_restoration_ledger:1544`, xenobiology at `KRG_open_the_designed_organism_dossier:1694`, and biological quarantine at `KRG_make_containment_the_first_doctrine:2239`. These are existing category/child-decision entry points, not empty replacement branches, and remain a P2 readability risk only.

Diplomatic, integration, and terminal tails are shorter than the full architecture ledger by design and still expose concrete consumers; adding nodes would violate the exact-100 closure.

The visible lifecycle remains capped at three focus-created spirit carriers in `common/ideas/016_brilliant_scientist_focus_ideas.txt`; hidden administration, portfolio, and scientific-population mirrors retain modifiers. A raw idea-object count can therefore read as six, but only three are visible and the hidden mirrors are one per slot.

The focus-owned effects file explicitly forbids focus-created stages, agents, forces, and units at `common/scripted_effects/016_brilliant_scientist_focus_effects.txt:4-6`. Static source review found no direct focus `create_unit`, equipment stockpile, factory, political-power, stability, or war-support reward calls; route effects set flags and call existing paid/project consumers.

## Icon coverage

| Surface | Result |
| --- | --- |
| Focus icon references | 100 unique `GFX_goal_KRG_*` references, one per focus in `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt`. |
| GFX registrations | 200 mentions in `interface/016_brilliant_scientist_kruger_state_focus.gfx`, representing 100 normal and 100 `_shine` sprites. |
| DDS textures | 100 `goal_KRG_*.dds` files under `gfx/interface/goals/016_brilliant_scientist_kruger_state_focus`. |
| Prior decoded raster | The retained 2026-09-02 raster pass decoded the complete tree successfully; no KRG icon warning was reported. The fresh 2026-09-05 raster request timed out, recorded below. |

## Localisation and reward mismatch list

`localisation/english/016_brilliant_scientist_focus_l_english.yml` contains 100 focus title keys, 100 description keys, and 100 effect-tooltip keys with a UTF-8 BOM. No missing KRG localisation key or focus-name/reward contradiction was confirmed.

Every focus has one `custom_effect_tooltip` reward surface, and route-specific completion effects set consumer flags or invoke existing focus helpers rather than repeating generic modifier ladders.

## AI behavior gaps

`common/ai_strategy_plans/016_brilliant_scientist_kruger_state_plans.txt` contains 19 plans, 19 `allowed` blocks, 19 `enable` blocks, 19 `abort` blocks, and 19 ordered `ai_national_focuses` blocks covering all 100 focus IDs. Every plan's continuously evaluated `enable` block includes `brilliant_scientist_is_kruger_sovereign_country = yes`; project plans also gate their route's operational/history prerequisites, and terminal plans zero the opposite terminal focus.

The three origin plans use the same four supply-focus factor surface at lines `34-40`, `67-74`, and `98-104`. This is a static differentiation risk, not a proven dominance or starvation result; no weight patch was made because no accepted target or before/after comparison exists.

The `allowed` guard discrepancy is unresolved as described above. The current header's any-valid-host transformation rationale may be intentional, but it differs from the architecture document's KRG-only wording.

War-state behavior is enforced through focus availability helpers rather than plan-level `has_war` clauses. In particular, temporal warning focus availability requires `has_war = yes`, while continental integration availability requires `NOT = { has_war = yes }` through `brilliant_scientist_kruger_focus_overextension_is_clear` at `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt:431-436`.

## MCP and probability evidence

Fresh focus MCP calls were attempted against workspace `mod_chaos_redux_ea3b2d67c2c0`, tree `brilliant_scientist_kruger_state_focus_tree`, and the bound focus source.

- `hoi4.focus_inspect` with national mode and the bound relative path timed out twice with `tool call error: tool call failed for hoi4_agent_tools/hoi4.focus_inspect; Caused by: timed out awaiting tools/call after 180s`.
- `hoi4.focus_render` with national mode and the bound relative path timed out with `tool call error: tool call failed for hoi4_agent_tools/hoi4.focus_render; Caused by: timed out awaiting tools/call after 180s`.
- `hoi4.focus_raster` at review scale 1 timed out with `tool call error: tool call failed for hoi4_agent_tools/hoi4.focus_raster; Caused by: timed out awaiting tools/call after 180s`.
- No `hoi4.focus_compare` route was exposed by the installed tool inventory, so no compare call could be made.

Retained prior structural artifacts from 2026-09-02 remain useful but are not presented as fresh proof: inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2844a32298eccfe04fa1d21e3a3ffa065b28cc626ffc86f6eae4e5cd0a01a0bf/60f1676b3e2d6b70bc6b852339ebf8b39cadc6dd50299fb0649f90f224c49ae6/focus-inspect.6b89499802012141.json`, render HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d516088b64605a3850f3c4aa434b5abd686095193e25bf76ce27d58c413423d1/a539c3bf3ac085aa36703aeac6395216fcee28a9b30c767f1d6e4573817a5b15/brilliant_scientist_kruger_state_focus_tree.focus.html`, render SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47ce06cd96e1426329b76afeda9aab2f9b7d3a3355239a976ebbf9490f2cb3d9/f67980b751d44b7f89980b0502188ac5cd21a3814d2c75c14a61ec6b7a3bd862/brilliant_scientist_kruger_state_focus_tree.focus.svg`, render JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58486f227fc4a55173a06ccceb2f3e546c528f774971399e1f0bb47edb4a2db7/b422a92ebc9519153dfb8fe18bedab1078aacae02ef125222b4c54d560fdd9a1/brilliant_scientist_kruger_state_focus_tree.focus.json`, and raster `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecc018518cabe95c0543811619f1e950311400a2be3992413999a1a028dba885f/197f6d73605ed8f623af39092bea439757e6ed1e2a8de106a97cda46591c4968/brilliant_scientist_kruger_state_focus_tree.focus.png`. That retained inspect reported 100 focuses, 100 titles, zero diagnostics, zero crossings, zero node intersections, zero long connectors, and layout hash `7a0f5017eea9a6d0a7131d07075d2bd848eeb092f5e870f3dc4bda605ec5ea39`.

Current weighted audit used `hoi4.probability_inspect` with adapter `national_focus_ai_will_do`, source `{ path: "common/national_focus/016_brilliant_scientist_kruger_state_focus.txt" }`, the exact 100 KRG IDs, and workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = true`, `candidates = 100`, `availableCandidates = 0`, `unresolved = 0`, source revision `9d6ab96f571780cbaf57ad5868d10fd333654678d6143c3da54b93f99af66f17`, and source hash `6751d47ca56404bb7e1ce23cf2eb4836f15c96079ba41baabbc68f4b81a69e8c`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7877fedb9d07f0a43b66f2369b09debdf3b8aee1182e368ab385e4e5c02401d1/e1342c5bd701113fc2e1e2e1539bf6d1391b0f0b966a4d93d32283388a333467/probability-inspect-6751d47ca564.json`.

Current weighted evaluation used scenario set `KRG_FINAL_AUDIT_2026_09_05` with one named empty-state scenario `KRG_BASE_EMPTY_2026_09_05` (`state = {}`), the same exact 100-ID pool, and the same focus source. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-98f1b81ed3526fe401263fa3`, candidates `100`, unresolved `1391`, diagnostics `100`, source revision `57bb2b43b482fc4dd6e1bb94547b8222ce1dd6f78f387e78f4e99d3675d563fd`, and scenario hash `fa1b2e7d046754429c2997d5131f2ec761a56282e6507068e1c2cb09b0ac7d44`. The analyzer produced ranking and unresolved SVG/PNG resources but withheld normalized probabilities because the empty state leaves route prerequisites and external factors unresolved. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe794c0346bc29c51b08400d1c58fa4edb9a689869b60ea4c8d0bf18f9d1c4ff/56a1241a2866a439db1fa949cff0a5ca6d4c8ea85a69b87408c1cdb6d871cac4/probability-98f1b81ed3526fe401263fa3.json`.

The current empty-state evaluation marked many route focuses `NEVER_ELIGIBLE` in that fixture, including `KRG_audit_inherited_portfolio`, `KRG_a_general_staff_for_the_state`, `KRG_a_council_of_project_commanders`, `KRG_accept_the_stabilization_window`, `KRG_an_army_of_machines`, `KRG_arm_the_alien_cohorts`, and `KRG_build_the_submission_network`. These are fixture/input incompleteness findings, not dead-route proof.

The custom `chaosx_ai_probability_auditor` route was not exposed as a callable tool in this runtime. No probability compare was run because no AI patch was made, and no sweep was run because no approved numeric scenario dimension was declared.

## Validation and remaining risks

Static checks confirmed exactly 100 unique KRG focus IDs, 100 focus blocks with `icon`, `search_filters`, `cost`, `completion_reward`, and `ai_will_do`, 19 AI plans covering all 100 IDs, no undefined KRG focus references, pairwise mutex declarations for identity/supply/command/diplomatic/terminal choices, 100 localisation title/description/effect keys, 100 icon references, 200 normal/shine registrations, and 100 DDS textures.

Required offline wiki pages, vanilla documentation, and vanilla Italy focus/AI precedents were read before this audit. The vanilla precedent uses `bypass`, `available`, `prerequisite`, `mutually_exclusive`, `completion_reward`, `allowed`, `enable`, `abort`, ordered `ai_national_focuses`, and `focus_factors` in the same structural roles.

No game launch, live campaign, live navigation/search interaction, or current visual raster review could be completed because the focus MCP service timed out. The retained prior raster/inspect artifacts and current static checks cannot substitute for that fresh engine evidence.

Remaining risks for parent review are the AI `allowed`-guard acceptance discrepancy, same-factor origin supply choices, category-seed readability, shorter diplomatic/integration/terminal tails, and the unresolved hidden-versus-visible idea count convention. Broad design expansion remains outside this bounded audit and should use the existing `016_krg_focus_depth_followup_plan_2026-08-05.md` rather than adding focuses here.
