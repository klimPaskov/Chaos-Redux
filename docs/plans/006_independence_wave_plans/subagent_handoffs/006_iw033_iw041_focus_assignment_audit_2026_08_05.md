# IW-033 / IW-041 focus assignment contract audit

Date: 2026-08-05  
Scope: Event 006 Karelia (IW-033 / KAR) and Crimean Tatar State (IW-041 / CRI) focus assignment, shared-tree coverage, route registration, AI/icon/localisation evidence, and dispatch/final-validation wiring.  
Mode: Read-only audit. No gameplay files were changed.

## Pre-promotion owner-patch snapshot (2026-08-05)

The status and verdict sections through `Changed files` below preserve the audit state before the parent promoted the IW-033/IW-041 content-attestation rows. The post-promotion note at the end is the current decision and supersedes the earlier HOLD wording.

The IW-033/IW-041 owner patch changes decision, mission, effect, trigger, cleanup, and package localisation surfaces only; it does not add or remove focus nodes or alter the shared assignment contract. The refreshed `hoi4.focus_inspect` receipt is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3cc9cf18a882cd1ed11f0720ba6deb8e576e605baef6f0ce1297efc6ae2ccecf/c749d590445bae156e1b135759eb46abd1202dc47d2d2d415af25ccc73f1d88c/focus-inspect.291f8225bd3c4b3c.json`; the shared tree remains 184 focuses and 193 connectors with no Event 006 crossings or node intersections, one intentional long connector, four linear-detour warnings, and unrelated vanilla continuous-focus icon diagnostics. The runtime content-attestation gate and the queued Level 2 country-specific-focus decision remain open.

## Pre-promotion verdict (historical)

The assignment contract is source-complete for the accepted one-tree architecture: both packages are admitted only from the vanilla `generic_focus` carrier, assign `full_framework`, and load the single `independence_wave_focus_tree` through the shared assignment effect. The assignment code does not claim an additive overlay for KAR or CRI and does not replace a meaningful vanilla tree. The shared tree exposes the required government, former-host, regional ambition, signature, network/league, power-struggle, economy, and force-archetype surfaces, and the package adapters register the package-specific state before final validation.

Runtime admission is currently HOLD, not PASS. The package dispatcher lists IW-033 and IW-041 as adapters, but its content-attestation registry does not list either package. The preflight and scenario-preflight triggers require that attestation, so no normal release or scenario path can promote these packages until the independent package/focus/decision/localisation/AI/asset audits are promoted. This is an intentional fail-closed barrier, not a focus-tree overwrite defect.

There is also a content-depth mismatch that the assignment contract alone cannot resolve. The candidate registry and focus spec classify KAR and CRI as Level 2 and require one country-specific focus group. No KAR/CRI/IW-033/IW-041 focus IDs or blocks exist in the national-focus files; the packages currently receive the shared generic routes plus package effects, ideas, decisions, and AI. The existing generic-tree closure handoff explicitly closes broad focus expansion and rejects bespoke trees. This audit therefore queues the gap for a parent scope decision rather than weakening the one-tree assignment contract or adding gameplay here.

## Evidence reviewed

Required repository guidance and references were read before audit: `AGENTS.md`; `.agents/skills/chaos-redux-focus-trees/SKILL.md`; `.agents/skills/chaos-redux-events/SKILL.md`; `.agents/skills/chaos-redux-decisions-missions/SKILL.md`; `.agents/skills/chaos-redux-event-assets/SKILL.md`; `.agents/skills/chaos-redux-improvement-loop/SKILL.md`; `.agents/skills/chaos-redux-subagents/SKILL.md`; the offline Paradox wiki core pages and National Focus modding page; and the vanilla focus/effects/triggers documentation.

Primary source files:

- `common/scripted_effects/006_independence_wave_focus_effects.txt:29-85` owns full versus additive assignment. Full mode sets `independence_wave_full_focus_framework`, sets the generic-tree assignment flag, calls `load_focus_tree = { tree = independence_wave_focus_tree keep_completed = no }`, and marks the layout dirty. Additive mode is carrier-gated and fail-closed.
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-83` defines the generic-focus contract. The full path requires the assignment flag, full-framework flag, and `has_focus_tree = independence_wave_focus_tree`; the additive path only admits the explicitly reviewed ICE and IW-023 carriers.
- `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt:448-485` and `:489-538` initialize IW-033 and IW-041. Both require the original `generic_focus` carrier, set the full-framework input, load the shared tree, enable all four government and all four former-host routes, register the package power struggle, ambition, signature, and league surfaces, load the force mapping, and publish package AI flags.
- `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt:8-123` proves exact package identity, anchor state, region/depth/archetype, former-host protection, and command-roster conditions. `:213-317` proves the prepared setup contract, including the full focus assignment, all route flags, power-struggle type, ambition/league registration, force mapping, package tradition, and package AI profile.
- `common/national_focus/006_independence_wave_focus.txt:34-94` defines the single `independence_wave_focus_tree` and imports shared roots. The route blocks begin at `:910` (government), `:1408` (former-host), `:1578` (ambition/signature), and `:1655` (network/league). The source contains no KAR/CRI-specific focus block.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-68` dispatches setup and final validation and applies the common final barrier requiring the generic focus contract and generic AI profile. `:72-89` dispatches cleanup, which reaches the shared focus-runtime reset.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:88-123` defines the content-attestation registry and preflight. IW-033/IW-041 are absent from the `OR` list at `:89-113`, while preflight requires the trigger at `:119-123`. Scenario preflight also requires it at `:257-265`. Exact candidate identity checks for IW-033/IW-041 are present at `:244-253`.
- `common/ai_strategy/006_independence_wave_karelia_crimea.txt:19-89` supplies package-level survival, production, construction, and former-host restraint profiles for KAR and CRI. `common/ai_strategy/006_independence_wave_generic.txt:35-105` supplies the shared recovery/consolidation profiles.
- `docs/events/006_independence_wave/karelia_crimea_packages.md` is the package contract for anchors, archetypes, route families, ideas/decisions, former-host protection, dynamic forces, and final ledgers.
- `docs/specs/006_independence_wave/spec_part_4_focus_tree_architecture.md` and `spec_part_5_country_packages_and_regional_overlays.md` define the accepted one-tree architecture and Level 2 country-specific-focus expectation.
- `docs/plans/006_independence_wave_plans/006_generic_focus_contract_closure_handoff_2026_08_02.md` records the prior closure decision: no bespoke tree and no broad generic route expansion without a new accepted design.

## Assignment and overwrite matrix

| Package | Admission/setup gate | Assignment | Owning tree | Additive carrier | Overwrite risk |
| --- | --- | --- | --- | --- | --- |
| IW-033 / KAR | `can_initialize_independence_wave_iw_033_package` plus `has_focus_tree = generic_focus` (`006_independence_wave_karelia_crimea_package_effects.txt:452`) | `independence_wave_focus_assignment.full_framework` (`:460-461`) | `independence_wave_focus_tree` | None; additive helper only permits ICE or IW-023 (`006_independence_wave_focus_triggers.txt:70-82`) | Low. The source starts from the vanilla generic carrier and the shared assignment effect owns the loaded tree. |
| IW-041 / CRI | `can_initialize_independence_wave_iw_041_package` plus `has_focus_tree = generic_focus` (`:493`) | `independence_wave_focus_assignment.full_framework` (`:513-514`) | `independence_wave_focus_tree` | None | Low, for the same reason. |

The shared assignment effect clears opposite ownership flags before publishing the selected mode (`006_independence_wave_focus_effects.txt:43-53`) and the generic contract trigger refuses to report a full assignment unless the engine reports the expected tree (`006_independence_wave_focus_triggers.txt:55-67`). This is the required fail-closed behavior for duplicate-tree and meaningful-vanilla-tree safety.

## Route coverage

| Surface | Shared implementation | KAR / CRI registration | Audit result |
| --- | --- | --- | --- |
| Full generic survival and administration | Shared tree root and imported roots in `006_independence_wave_focus.txt:34-94`; 184 direct focus nodes in the engine tree | Both adapters assign full framework | Covered. |
| Government | Four `allow_branch` lanes and mutually exclusive commits in `006_independence_wave_focus.txt:910-1253`; route triggers in `006_independence_wave_focus_triggers.txt:127-238` | Both adapters enable constitutional, popular-council, traditional, and emergency-military availability (`006_independence_wave_karelia_crimea_package_effects.txt:462-465` and `:515-518`) | Covered; route locks are package-published and the four commits are mutually exclusive. |
| Former host | Four host routes in `006_independence_wave_focus.txt:1408-1575`; host trigger gates in `006_independence_wave_focus_triggers.txt:252-290` | Both adapters enable negotiation, guarded-frontier, association, and reclamation (`:466-469` and `:519-522`) | Covered. |
| Power struggle | Shared focus registration and route-aware effects | KAR uses `civilians_vs_army` (`006_independence_wave_karelia_crimea_package_effects.txt:470-471`); CRI uses `municipal_commission_vs_industrial_security` (`:523-524`) | Covered and package-distinct. |
| Regional ambition | `independence_wave_focus_open_regional_ambition` (`006_independence_wave_focus_effects.txt:635-663`) chooses the Eastern Europe/western Russia borderland family; focus triggers at `006_independence_wave_focus_triggers.txt:292-318` | Both adapters register ambition family (`006_independence_wave_karelia_crimea_package_effects.txt:472` and `:525`) | Covered at shared/regional level; no package-specific focus IDs. |
| Signature/formable | Shared signature module and formable gates in `006_independence_wave_focus.txt:1578-1652`; triggers at `006_independence_wave_focus_triggers.txt:320-334` | Both adapters register signature (`:473` and `:526`) | Covered as a registered shared module; package-specific formable dependency still belongs to the separate package attestation. |
| Network / league | Shared route and member/phase/consent focus blocks from `006_independence_wave_focus.txt:1655`; triggers at `006_independence_wave_focus_triggers.txt:336-349` | Both adapters allow league route (`:474` and `:527`) | Covered at shared level; final package admission is still blocked by missing attestation. |
| Economy and military archetype | Shared adapter effects map archetype to economy and force programs in `006_independence_wave_focus_effects.txt:504-633` | KAR maps mountain/frontier and p33; CRI maps mounted/mobile and p41 (`006_independence_wave_karelia_crimea_package_triggers.txt:240-243` and `:293-296`) | Covered; package effects/ideas provide the differentiating state. |

## Missing or simplified content

1. **Runtime content attestation is not promoted.** IW-033 and IW-041 are absent from `has_independence_wave_runtime_package_content_attestation_for_execution_id` (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:88-114`). Because normal and scenario preflight require that trigger (`:119-123`, `:257-265`), setup/final-validation code is present but unreachable through an admitted runtime package until the independent audit rows are promoted.

2. **Level 2 country-specific focus group is not independently evidenced.** The candidate registry/spec expects one country-specific group for each Level 2 package, but `rg` found no `kar_`, `cri_`, `kc_`, `iw033`, or `iw041` focus identifiers in `common/national_focus/006_independence_wave*_focus.txt`. The current implementation is therefore a shared-tree package with package-specific decisions, ideas, effects, force mapping, and AI. This is a broader design/depth issue, not an assignment bug. The prior generic-tree closure explicitly forbids inventing a bespoke tree; see the queued plan below.

3. **Adjacent package blockers are repaired in source but promotion remains gated.** The owner-patch reconciliation closes the dated decision/mission and dynamic-cost/ledger-localisation findings. These are not focus-source defects, but the package remains outside content attestation while the Level 2 focus-depth decision, independent promotion, and parent-owned probability/runtime evidence remain open.

4. **MCP reports four Event 006 layout warnings and unrelated vanilla diagnostics.** The Event 006 tree has one intentional long connector and four linear-detour warnings. The overall MCP result is `passed:false` because the repository-wide validation also reports 14 missing icon references in vanilla continuous-focus surfaces; none are Event 006 icon references. No focus rewrite was performed because this audit is read-only and none of the warnings blocks KAR/CRI assignment.

## Icon coverage

| Scope | Evidence | Result |
| --- | --- | --- |
| Shared Event 006 focus tree | Static source scan across all `006_independence_wave*_focus.txt` files found 318 unique focus IDs and 121 unique `icon =` references. | All focus IDs have an icon reference. |
| Sprite registration | Every one of those 121 icon names and matching `_shine` names resolves in `interface/006_independence_wave*.gfx`. | No Event 006 focus icon or shine gap found. |
| KAR / CRI package-specific focus art | No KAR/CRI-specific focus IDs exist; package docs specify reuse of existing decision/icon families. | No separate package focus art is wired or required by current source. |

## Historical pre-owner-patch localisation and reward mismatch list

- Static localisation scan found title and `_desc` keys for all 318 focus IDs and `custom_effect_tooltip` keys for all 318 focus IDs in `localisation/english/006_independence_wave*_l_english.yml`.
- All 318 focus definitions have a completion reward block and an `ai_will_do` block. The shared route effects are not one repeated generic reward: government, former-host, ambition, signature, league, economic, military, and power-struggle branches call distinct scripted helpers and package adapters publish distinct state.
- No focus-specific localisation/reward mismatch was found for KAR or CRI because no package-specific focus IDs are present.
- The package-localisation gaps listed here are pre-owner-patch evidence. The current source contains the four party-name families, all sixteen `_blocked`/`_tooltip` companions, corrected icon markers, and dynamic ledger values; those repairs do not invalidate the shared focus localisation scan or promote content attestation.

## AI behavior gaps

- Source coverage is complete for the shared tree: all 318 focus definitions have `ai_will_do`; government, host, ambition, signature, league, economy, and force lanes contain route/state-aware modifiers.
- KAR and CRI have package-level AI strategy factors in `common/ai_strategy/006_independence_wave_karelia_crimea.txt:19-89`, including survival, construction/production, and former-host restraint. The generic recovery/consolidation profiles are in `common/ai_strategy/006_independence_wave_generic.txt:35-105`.
- No KAR/CRI-specific focus-selection modifiers or focus IDs were found. The AI can choose the shared routes through generic state flags, but package-level strategy factors do not independently prove that KAR and CRI select their intended country-specific route emphasis.
- A focus-selection probability audit was not run because the available probability route did not expose a named Event 006 focus-selection surface. This is an evidence limitation, not a claim that the AI is balanced. A future `chaosx_ai_probability_auditor` pass should use named KAR/CRI scenarios once the package adapter is admitted.

## Required MCP focus evidence

Fresh `hoi4.focus_inspect` succeeded for workspace `mod_chaos_redux_ea3b2d67c2c0`, tree `independence_wave_focus_tree`, mode `national`, relative path `common/national_focus/006_independence_wave_focus.txt`.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3cc9cf18a882cd1ed11f0720ba6deb8e576e605baef6f0ce1297efc6ae2ccecf/c749d590445bae156e1b135759eb46abd1202dc47d2d2d415af25ccc73f1d88c/focus-inspect.291f8225bd3c4b3c.json`
- Engine tree: 184 focuses, 193 connectors, zero crossings, zero node intersections, one long connector, maximum horizontal span 13, bounds x=1..121 and y=0..19, layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.
- Event 006 diagnostics: four `FOCUS_LAYOUT_LINEAR_DETOUR` warnings and one `FOCUS_LAYOUT_LONG_CONNECTOR` warning. The long connector is the known isolated `independence_wave_adopt_military_archetype_program -> independence_wave_preserve_independent_command` span-13 link. The aggregate inspect also reports unrelated vanilla continuous-focus icon diagnostics; no Event 006 crossing, overlap, symmetry, or same-row-spacing diagnostic was reported.

Fresh `hoi4.focus_render` also succeeded with the same layout hash.

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77c1af84241a4da87ed185d5f0a81296f92e1cf7d4d338be09412ce2e88a85d7/305111a844b682ad718a0abd237e307a76ed4eaf1a0957baa469842cc442a8bf/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e/78e4a363d61357a1a23a5b1ff0f0bbb2c5f4c55380d72505c47dafe9e7fa00cb/independence_wave_focus_tree.focus.svg`
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d0a9699de3bed2979acd7edfaec33d0329bb3b929bf39b4713db192ea82735c/e9942b7d5fc23a6c19b31164d02fb5b2de1e7e04f13991eb98b98fddb0a666d5/independence_wave_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/994058086733667d683bc0eb37f46682bc8a4f3985992e9d4036cabe3452fca9/285197d17ebe16a444792d5c5aee01bda59926fb56a6b1f69ba7298d417ab612/independence_wave_focus_tree.focus.source-map.json`
- Layout plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1450dbe6b29df77710baf723eb7a16cdeaf402a901a576a4354a54692e3e0e3d/0832d52e917ee09f899616abf48f50d920a5aece672a4426404ecb602cdec9ab/independence_wave_focus_tree.focus.plan.json`

The MCP aggregate result is `passed:false` only because it includes 14 unrelated vanilla continuous-focus missing-icon diagnostics. Event 006 itself has no missing-icon diagnostic in this run.

## High-priority fixes and decisions

1. Historical pre-promotion action: repair and re-audit the package-owned decision/mission and localisation blockers, then promote IW-033 and IW-041 content-attestation rows. The owner later completed the central promotion; do not bypass the preflight gate.
2. Decide the Level 2 focus-depth mismatch. If the design still requires one country-specific focus group per package, implement a bounded gated shared module under the existing `independence_wave_focus_tree` only after an accepted spec/addendum. Do not create a second tree or overwrite a meaningful vanilla tree. If the accepted one-tree closure supersedes the Level 2 expectation, record an explicit scope waiver in the spec and candidate registry.
3. Run the required probability audit for package AI/focus selection now that the adapter is centrally attested and named scenarios are available; compare the same scenarios before and after any AI change. This remains open because no complete typed KAR/CRI scenario contract or `probability_compare` receipt exists.
4. Treat the five Event 006 layout warnings as optional cleanup. None is an assignment or route-lock blocker; the intentional span-13 connector should remain unless a replacement layout preserves route readability.

## Validation and limits

Meaningful checks completed: source inspection of assignment, package triggers/effects, dispatch and cleanup; vanilla `generic_focus` and KAR/CRI history review; static focus-ID/icon/localisation/reward/AI coverage scans; fresh `hoi4.focus_inspect`; fresh `hoi4.focus_render`; and cross-check against the package contract and prior generic-tree closure handoff.

Skipped: no `hoi4.focus_rewrite` because this is read-only; no game launch or live-save validation per repository policy; no probability compare because a named KAR/CRI focus-selection surface was not exposed; no package-attestation promotion because that belongs to the parent integration and dependent audits.

Remaining route risks are the unpromoted runtime attestation, the Level 2 country-specific-focus expectation, adjacent decision/localisation blockers, and the untested runtime AI selection behavior. The shared source route itself has no observed connector crossing, node overlap, missing Event 006 focus icon, missing focus localisation, or missing focus AI block.

## Queued depth plan

The bounded design decision is recorded in `docs/plans/006_independence_wave_plans/006_iw033_iw041_focus_depth_plan_2026_08_05.md`. It is a documentation-only queue for the parent: no gameplay implementation is authorized by this audit.

## Changed files

Only this handoff and the queued depth-plan document were added. No gameplay, localisation, AI, focus, decision, or asset files were edited.

## Post-promotion audit note (2026-08-05)

The parent scope decision accepts the shared generic-tree contract for IW-033/KAR and IW-041/CRI. The Level 2 country-specific-focus expectation is waived for these two packages; no individual KAR or CRI focus tree, package-specific focus group, or second tree should be added. Their differentiation is intentionally carried by the shared tree's route gates and package adapters, plus the package decisions, ideas, power struggles, regional ambition registration, force mappings, former-host routes, league/signature registration, and package AI strategies.

The content-attestation promotion is now present in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:113-118`: both `constant:independence_wave_package_id.iw_033` and `constant:independence_wave_package_id.iw_041` are listed in `has_independence_wave_runtime_package_content_attestation_for_execution_id`. The same file's preflight barrier at `:125-128` still requires both the exact adapter and that attestation, and the scenario path continues to require the attestation at `:264-271`. Setup and final-validation dispatch remain wired in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-52`, including the Karelia/Crimea adapters at `:30` and `:52`, and the common final barrier at `:53-68` still requires `has_independence_wave_generic_focus_contract` plus `independence_wave_generic_ai_profile`.

Static post-promotion assignment verification remains PASS: `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt:452-461` and `:493-514` still require the vanilla `generic_focus` carrier, set `independence_wave_focus_assignment.full_framework`, and call `independence_wave_assign_focus_framework`; `common/scripted_effects/006_independence_wave_focus_effects.txt:55-61` still loads only `independence_wave_focus_tree`; and `common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-67` still requires the full-framework flag, assignment flag, and engine-reported shared tree. No additive-carrier path is admitted for KAR or CRI.

Fresh post-promotion MCP evidence is unchanged in topology and now records the current source revision. `hoi4.focus_inspect` succeeded with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/118a4049a0f5f5535ce21d6896e8dd572e8c04a60f3d08ce9eba124c1d91aa8e/b8efaa61876551a8b2ffa35c62ecf832a208a5a1b420d57d2d89d4e89e44704e/focus-inspect.32afe15f92bb15e9.json`; it reports 184 focuses, 193 connectors, zero crossings, zero node intersections, one long connector, layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`, and four Event 006 linear-detour warnings. `hoi4.focus_render` succeeded with HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77c1af84241a4da87ed185d5f0a81296f92e1cf7d4d338be09412ce2e88a85d7/fd3a88f69c9ca8759cd2668307b373955550317f0b75f9a8f969620c6c4121ef/independence_wave_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315af84241a4da87ed185d5f0a81296f92e1cf7d4d338be09412ce2e88a85d7/326956327bd9dfdb710652b2c708810638ba69cb9b6cfb86d3a6dd81134cfbca/independence_wave_focus_tree.focus.svg`, and matching layout hash. The aggregate MCP validation remains false only because it includes 14 unrelated vanilla continuous-focus icon diagnostics; no Event 006 focus icon, crossing, or overlap diagnostic is present.

The accepted generic-tree contract and generic-tree breadth are separate judgments. Assignment safety, route registration, icon/localisation coverage, and post-attestation dispatch are PASS. Breadth remains a non-blocking design risk to monitor: the shared tree is intentionally large and generic, and no country-specific focus IDs exist for KAR/CRI. Any future breadth improvement must be a separately accepted shared-tree design change, with a new spec/addendum, route-aware AI evidence, and another inspect/render pass; it is not a reason to reopen the assignment contract or add bespoke trees.

The prior queued depth plan is therefore superseded as a required implementation by the parent decision. Its breadth-risk guardrails remain useful: `docs/plans/006_independence_wave_plans/006_iw033_iw041_focus_depth_plan_2026_08_05.md` is retained as historical decision evidence, not an open blocker.

The later owner-AI reserve-floor tranche is separate from focus assignment: it changes regular decision `ai_will_do` selection for IW-033/IW-041, not the shared focus tree or focus ownership contract. The executable decision predicates are documented in `006_iw033_iw041_owner_ai_reserve_floor_patch_2026_08_05.md`, while focus-selection probability and live package runtime remain unproven.
