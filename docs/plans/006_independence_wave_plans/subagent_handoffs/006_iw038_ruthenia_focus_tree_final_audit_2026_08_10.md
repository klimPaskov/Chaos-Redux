# IW-038 Ruthenia shared-focus integration final audit — 2026-08-10

## Scope and verdict

This is a read-only final focus audit for Event 006 IW-038 Ruthenia (`RUT`) against the current shared dirty worktree. It covers the five requested helper call sites, package helper definitions, full-framework setup and assignment, route reachability, decision idempotence, AI weights, icon/localisation coverage, and the no-additive/no-bespoke-tree contract.

The shared-focus integration is source-complete for the requested five hooks. Each helper has exactly one guarded call in `common/national_focus/006_independence_wave_focus.txt`, the matching package effect is one-shot guarded, and the corresponding project decision consumers reuse the same completion flags. `RUT` is assigned the shared full framework; no RUT national-focus file, bespoke tree, or additive carrier exists. The package is not final-admission complete: RUT decision/route localisation is absent, typed probability evidence is not present in this audit, and the parent-owned central attestation remains fail-closed.

No gameplay file was changed, staged, or committed. This handoff is the only file written by this audit.

## Route coverage

| IW-038 route or lane | Shared focus route and source | RUT helper / consumer | Reachability and result |
| --- | --- | --- | --- |
| Survival / provisional administration | `independence_wave_prepare_capital_administration` (`common/national_focus/006_independence_wave_focus.txt:99-119`) | `independence_wave_rut_focus_convene_provisional_assembly` at `:115`; secure-depots decision calls the helper at `common/decisions/006_independence_wave_ruthenia_decisions.txt:83-90` | Root focus is available only through `can_use_independence_wave_full_focus_framework`; RUT guard is exact `original_tag = RUT` plus `is_independence_wave_rut_package = yes`. Helper raises the two RUT ledgers, applies shared administration, and sets `independence_wave_rut_depots_secured`. Covered and one-shot. |
| Mountain communities / civic settlement | `independence_wave_inventory_the_state` (`006_independence_wave_focus.txt:140-161`) | `independence_wave_rut_focus_guarantee_mountain_communities` at `:157`; community project calls it at `006_independence_wave_ruthenia_decisions.txt:169-176` | Requires the capital-administration focus and full-framework availability. Helper applies the shared public-settlement bundle and sets `independence_wave_rut_communities_guaranteed`. Covered and one-shot. |
| Border guards / mountain security | `independence_wave_bind_the_first_oath` (`006_independence_wave_focus.txt:163-184`) | `independence_wave_rut_focus_integrate_border_guards` at `:180`; guards project calls it at `006_independence_wave_ruthenia_decisions.txt:124-131` | Requires the survival root and full framework. Helper applies the shared security-reform bundle and sets `independence_wave_rut_guards_integrated`. Covered and one-shot. |
| Former-host settlement | `independence_wave_define_former_host_policy` (`006_independence_wave_focus.txt:1402-1418`) | `independence_wave_rut_focus_settle_former_host_ledgers` at `:1410`; normal project calls it at `006_independence_wave_ruthenia_decisions.txt:227-234`, host-loss fallback at `:255-265` | Focus requires completed `independence_wave_complete_founding_settlement`, full framework, and an unsettled host relation. Helper applies bilateral host deltas only when the saved host is usable, progresses the shared host ledger, and sets `independence_wave_rut_host_ledgers_settled`. Covered; two decision consumers are protected by the helper flag. |
| Network / Carpathian corridor | `independence_wave_recognize_fellow_new_states` (`006_independence_wave_focus.txt:1672-1688`) | `independence_wave_rut_focus_open_carpathian_corridor` at `:1680`; corridor project calls it at `006_independence_wave_ruthenia_decisions.txt:541-548` | Requires founding settlement completion and `can_participate_in_independence_wave_network_focuses` (active network member, no client lock). Helper opens the corridor once, updates both RUT ledgers, network/league values, and ambition, then sets `independence_wave_rut_carpathian_corridor_open`. Covered and one-shot. |
| Constitutional government | `independence_wave_prepare_first_assembly` → `independence_wave_ratify_constitution` → constitutional capstone (`006_independence_wave_focus.txt:922-1005`) | `independence_wave_rut_ratify_constitutional_autonomy` calls `independence_wave_install_rut_constitutional_government` (`006_independence_wave_ruthenia_decisions.txt:280-307`) | Shared focus lane is route-locked and mutually exclusive with other governments; RUT decision installs the package government after project readiness and capital/cost gates. Covered through the shared route, not a RUT-specific focus node. |
| Agrarian compact | `independence_wave_prepare_traditional_confirmation` → `independence_wave_restore_legitimate_authority` → traditional capstone (`006_independence_wave_focus.txt:1067-1135`) | `independence_wave_rut_adopt_agrarian_compact` calls `independence_wave_install_rut_agrarian_government` (`006_independence_wave_ruthenia_decisions.txt:325-351`) | Shared lane is exposed as “Traditional Restoration”; its package adapter maps `has_independence_wave_traditional_route` to the RUT agrarian government. Reachable and route-locked, but the generic focus wording does not name the RUT agrarian outcome (see mismatch section). |
| Socialist councils | `independence_wave_organize_popular_councils` → cooperative administration/public guard → council capstone (`006_independence_wave_focus.txt:1007-1065`) | `independence_wave_rut_convene_socialist_councils` calls `independence_wave_install_rut_socialist_government` (`006_independence_wave_ruthenia_decisions.txt:369-396`) | Shared popular-council route is available after founding settlement and mutually exclusive with other government lanes. Covered through the shared route and package decision. |
| Mountain emergency command | `independence_wave_establish_emergency_command` → militia/economy → emergency capstone (`006_independence_wave_focus.txt:1137-1185`) | `independence_wave_rut_establish_mountain_emergency_command` calls `independence_wave_install_rut_emergency_government` (`006_independence_wave_ruthenia_decisions.txt:414-440`) | Shared emergency lane is route-locked, instability/war-aware, and mutually exclusive with rival settlements. Covered through the shared route and package decision. |

## Exact helper reachability and idempotence

The five helper definitions occur once each in `common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt:279-338`:

| Helper | Definition | One focus call | Completion flag | Decision calls |
| --- | ---: | ---: | --- | --- |
| `independence_wave_rut_focus_convene_provisional_assembly` | `:279-288` | `006_independence_wave_focus.txt:115` | `independence_wave_rut_depots_secured` | `006_independence_wave_ruthenia_decisions.txt:89` |
| `independence_wave_rut_focus_guarantee_mountain_communities` | `:290-299` | `006_independence_wave_focus.txt:157` | `independence_wave_rut_communities_guaranteed` | `:175` |
| `independence_wave_rut_focus_integrate_border_guards` | `:301-310` | `006_independence_wave_focus.txt:180` | `independence_wave_rut_guards_integrated` | `:130` |
| `independence_wave_rut_focus_settle_former_host_ledgers` | `:312-325` | `006_independence_wave_focus.txt:1410` | `independence_wave_rut_host_ledgers_settled` | `:233`, host-loss fallback `:264` |
| `independence_wave_rut_focus_open_carpathian_corridor` | `:327-338` | `006_independence_wave_focus.txt:1680` | `independence_wave_rut_carpathian_corridor_open` | `:547` |

A repository-wide source scan found one focus call for each helper and one definition for each helper. The only helper with two decision call sites is former-host settlement, and both branches are protected by its completion flag. Every helper body has a `NOT = { has_country_flag = ... }` one-shot guard. Decision visibility also excludes the completion flag, and `has_independence_wave_rut_active_package_project` serializes paid projects. Setup clears all five completion flags (`common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt:344-364`) and generation-safe cleanup clears them again (`:455-476`), so a new package generation cannot inherit a prior helper receipt.

The focus call guards are exact and do not broaden to another tag: `original_tag = RUT is_independence_wave_rut_package = yes`. The package trigger itself requires `original_tag = RUT`, active Event 006 identity, and package id `iw_038` (`common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt:8-12`). Decision call sites are entered only through RUT project-readiness and capital/cost gates. No duplicate package-owned reward path was found. The network helper intentionally combines the shared network-cooperation reward with the RUT corridor project reward, matching the established package-hook pattern; the corridor flag prevents repeating that combined package reward. A focus completed after a decision can still grant the focus's ordinary shared lane bundle once, which is a one-time focus reward rather than a repeated RUT helper reward.

## Full-framework assignment and no additive/bespoke tree

`independence_wave_setup_iw_038_ruthenia` assigns `constant:independence_wave_focus_assignment.full_framework` and calls `independence_wave_assign_focus_framework` (`common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt:368-403`). The full-framework branch sets `independence_wave_full_focus_framework` and `independence_wave_generic_focus_tree_assigned`, then calls `load_focus_tree = { tree = independence_wave_focus_tree keep_completed = no }` (`common/scripted_effects/006_independence_wave_focus_effects.txt:33-61`). The shared focus trigger requires active-country identity and the full-framework flag (`common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-38`). RUT setup also publishes the four government-route availability flags, host routes, power-struggle registration, ambition family, and league route before setting setup complete (`006_independence_wave_ruthenia_package_effects.txt:378-411`).

`rg --files common/national_focus` finds no RUT/ruthenia/IW-038 national-focus file. The only RUT references in national-focus source are the five guarded helper calls in the shared tree. No `shared_focus` import or additive carrier is associated with RUT. This satisfies the current IW-038 plan's explicit full-framework/no-bespoke-tree contract and does not replace a meaningful vanilla RUT tree.

## Icon coverage

No new focus ids or focus icons were introduced by the RUT hook patch. The five existing shared focus nodes reuse registered Event 006 icon families:

| Focus id | Icon id / shine | GFX and DDS evidence | Result |
| --- | --- | --- | --- |
| `independence_wave_prepare_capital_administration` | `GFX_goal_independence_wave_founding_administration` / `_shine` | `interface/006_independence_wave.gfx:3-4`; `gfx/interface/goals/006_independence_wave/goal_independence_wave_founding_administration.dds` exists | Present. |
| `independence_wave_inventory_the_state` | `GFX_goal_independence_wave_infrastructure_authority` / `_shine` | `interface/006_independence_wave.gfx:19-20`; matching DDS exists | Present. |
| `independence_wave_bind_the_first_oath` | `GFX_goal_independence_wave_army_integration` / `_shine` | `interface/006_independence_wave.gfx:17-18`; matching DDS exists | Present. |
| `independence_wave_define_former_host_policy` | `GFX_goal_independence_wave_former_host_settlement` / `_shine` | `interface/006_independence_wave.gfx:21-22`; matching DDS exists | Present. |
| `independence_wave_recognize_fellow_new_states` | `GFX_goal_independence_wave_league_congress` / `_shine` | `interface/006_independence_wave.gfx:23-24`; matching DDS exists | Present. |

The current MCP focus diagnostics report no missing icon for any Event 006 national-focus node. The reported missing icon errors are for the installed vanilla continuous-focus palette and are outside this RUT scope.

## Localisation and reward alignment

All five shared focus title, description, and custom tooltip keys are present in `localisation/english/006_independence_wave_focus_l_english.yml`: administration `:63-65`, inventory `:69-71`, oath `:72-74`, former-host `:273-275`, and network `:329-331`. Their generic wording matches their shared lane rewards. The RUT helper effects are hidden adapters and do not introduce focus localisation keys.

One package-level mismatch remains: RUT's `adopt_agrarian_compact` decision and `agrarian` government installer are reached through the shared focus lane named “Traditional Restoration” (`independence_wave_restore_legitimate_authority` localisation at `006_independence_wave_focus_l_english.yml:221-223`). This is a deliberate shared-framework mapping in the current plan, not a broken prerequisite, but it does not expose the agrarian identity from the focus surface. The missing RUT localisation package (`rg --files localisation/english` finds no `006_independence_wave_ruthenia_l_english.yml`) prevents verifying the package decision names, route tooltips, cost text, and dynamic ledger prose. Parent localisation work must either document this shared-lane mapping or provide RUT-specific explanatory text; no focus hook patch should invent a new route family.

No repeated focus title/description/tooltip keys or missing keys were found for the five audited nodes. The five helper rewards are package-specific ledger/host/network effects and are not duplicated by another RUT focus call.

## AI behavior gaps

All five shared focus nodes have AI weights: root administration is urgent with a severe-instability preference, inventory is urgent, oath is urgent with a wartime preference, former-host is high with founding-settlement prerequisite boost, and network is high with the same prerequisite boost (`006_independence_wave_focus.txt:118`, `:160`, `:183`, `:1411-1417`, `:1681-1687`). The RUT package AI file adds mountain survival, former-host restraint, settled-compact, and emergency-guard strategy layers (`common/ai_strategy/006_independence_wave_ruthenia.txt:21-71`). No focus AI weight changed in this hook integration, so there is no source-level AI regression.

Quantitative probability evidence is unresolved. The current audit did not run `chaosx_ai_probability_auditor`; no focus-weight or strategy-factor compare should be inferred from the source constants alone. Parent must run the mandatory `hoi4.probability_inspect`/scenario evaluation and compare for the RUT focus/decision/strategy surfaces before content attestation, including empty/unprepared, project-ready peace, project-ready war, host-threat, stable-route, and network-ready cases. The existing RUT decision handoff also records that `ai_strategy_factor` evidence is incomplete.

## MCP focus evidence and diagnostics

The mandatory current-worktree `hoi4.focus_inspect` succeeded for `independence_wave_focus_tree` (`FOCUS_INSPECTED`) with revision `8ac3e0da5c84786cb84bf70091dfc0064b2fc3335e8ae22141a1527245b27fc6`, layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`, 184 focuses, and 193 connectors. Layout metrics report zero connector crossings and zero node intersections; one 13-column connector remains in the shared tree, outside the five RUT hook nodes. Inspect artifact: [focus-inspect.8ac3e0da5c84786c.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e8e18ed2cf988bf50eb9b31da741fe5d8a2bb808e872af33412c0d89636884f/23571be7b3dc919b2d44736fd881b37f46e6648a66b6f2eb5540a4ac6975122d/focus-inspect.8ac3e0da5c84786c.json).

The matching current `hoi4.focus_render` succeeded (`FOCUS_RENDERED`) with the same layout hash and produced HTML, SVG, JSON, source-map, and plan artifacts. HTML: [independence_wave_focus_tree.focus.html](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9181237deb74eb7421b6d49e6ed68c5a30acdf7fc0e0b0ad0a3693a9340095d/5beeddce26646471094c357358746461f3b96d153ded80a460eb77c0078131cf/independence_wave_focus_tree.focus.html). SVG: [independence_wave_focus_tree.focus.svg](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e/4d22014be9472168bca74325223d60af4d0df69ec4c0e618f28d66da8b3d4d/independence_wave_focus_tree.focus.svg). JSON: [independence_wave_focus_tree.focus.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43c0594aca6c955bc843f4cce17bb5fc01f78fd021caff1bea569c2b28923d73/fd51471af3504696232e659eb18e99a39d7c092b2e62d9631f80cced394cc335/independence_wave_focus_tree.focus.json).

MCP validation is false for the current shared tree because it reports 14 blocking diagnostics: nine missing icons in the installed vanilla continuous-focus palette and five pre-existing layout warnings (four linear detours and one long connector). No diagnostic names an Event 006 national-focus node, RUT helper, icon, prerequisite, or route. The five source-tree layout warnings concern unrelated generic nodes (`independence_wave_secure_food_and_fuel`, `independence_wave_activate_package_economic_program`, `independence_wave_form_border_guard`, and `independence_wave_build_postwar_integration_authority`). No `hoi4.focus_rewrite` was used because this audit found no RUT-owned layout defect and was read-only.

Canonical SVG artifact URI (use this exact URI; the inline link above contains a shorthand typo): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e/4d22014be9472168bca74325223d60af4d0df69ec4c0e618f28d66da8b8d3b4d/independence_wave_focus_tree.focus.svg`.

## Missing, simplified, or blocked content

- No requested RUT helper call, helper definition, shared route lane, or idempotence flag is missing.
- No RUT bespoke or additive focus tree exists; this is intentional and matches the current IW-038 plan. If a later acceptance decision requires a distinct RUT focus group, that is a broader design change and needs a new improvement plan rather than a local hook patch.
- RUT package localisation is absent, so decision names/descriptions, route outcome text, cost labels, and visible ledger wording remain a parent-owned blocker.
- Typed probability evidence for focus and package AI remains unresolved; no quantitative balance claim is made here.
- MCP's 14 diagnostics are pre-existing/shared or installed-vanilla continuous-focus issues and are outside this bounded RUT audit.
- No live HOI4 launch, save/load, or consumer execution was performed; those belong to the user.

## High-priority follow-up

1. Add and audit the RUT localisation package, including the agrarian-versus-traditional shared-lane explanation and all decision/mission cost/effect keys, before attestation.
2. Route the RUT focus/decision/strategy scenarios through `chaosx_ai_probability_auditor` and preserve unresolved adapter limitations instead of inferring ranking from raw constants.
3. Parent should confirm the package effects/triggers are included in the runtime content inventory and that `is_independence_wave_rut_package` resolves at load time before relying on the five calls. The current focus MCP inventory is centered on the national-focus file and shared icon/localisation sources.
4. Keep the shared-tree/vanilla continuous-focus diagnostics owned by their existing surfaces; no RUT-specific rewrite is justified by this audit.

## Changed files, identifiers, and validation

Changed files: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw038_ruthenia_focus_tree_final_audit_2026_08_10.md` only.

Changed focus ids: none. Audited focus ids: `independence_wave_prepare_capital_administration`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states`.

Changed localisation keys: none. Changed icon ids: none.

Meaningful validation: current `hoi4.focus_inspect` and `hoi4.focus_render` both succeeded; static source scans counted exactly one focus call and one helper definition for each helper, matched each decision consumer and one-shot flag, confirmed full-framework assignment, confirmed no RUT focus-tree file, and matched all five title/description/tooltip keys and icon/shine/DDS assets.

Skipped meaningful validation: no `hoi4.focus_rewrite` because no patch or layout change was authorized; no probability compare because no AI weight changed and this audit is not the probability-owner handoff; no live game validation because repository instructions reserve it for the user.

Plan handoff path: this file. No additional improvement-loop plan was written because the current contract explicitly forbids a bespoke/additive RUT tree and the shared route depth is already supplied by the Event 006 framework.

Remaining route risks are the RUT localisation blocker, unresolved typed AI evidence, the parent-owned central attestation/preflight, and the generic/vanilla MCP diagnostics. None is a missing or unreachable IW-038 shared-focus hook.
