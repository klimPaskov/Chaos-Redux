# Event 006 IW-012 ICE focus and adapter retry audit

> Reconciled 2026-07-28: the original retry below captured the pre-carrier state. The parent subsequently installed the exact vanilla-path `iceland_tree` snapshot with all twelve Event 006 imports, added the IW-012 attestation, and corrected the AI syntax. The final bounded focus disposition is PASS for source carrier/imports, route prerequisites/exclusions, localization, and icons; live shared-focus rendering, route-aware AI probability, and dynamic former-host targeting remain HOLD. See `006_iw012_ice_package_implementation_2026_07_28.md` for the current parent-owned handoff.

## Scope and verdict

This audit covers the current IW-012 registered-tag adapter for `ICE`, its additive focus assignment, the vanilla `iceland_tree`, route and host hooks, the North Atlantic Compact/FORM-02 registration, localization, and origin-aware AI.

Verdict at the time of this retry: **HOLD.** The detailed findings below are retained as the pre-carrier audit snapshot; they are superseded for current source disposition by the reconciliation note above and the parent implementation handoff.

No new country, focus tree, portrait, flag, advisor icon, or OOB was added.

## Vanilla authority evidence

| Surface | Evidence | Result |
|---|---|---|
| Vanilla tree | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/iceland.txt`, `focus_tree.id = iceland_tree` | Preserved and authoritative. |
| Vanilla focus inspect | `hoi4.focus_inspect` on workspace-relative `common/national_focus/iceland.txt`, `treeId = iceland_tree` | 89 focuses, 89 resolved titles, one `NORDIC_form_joint_alliance` shared import, bounds `x=2..37`, `y=0..9`, 104 connectors, 2 crossings, 0 node intersections, 0 long connectors. |
| Vanilla identity/history | `history/countries/ICE - Iceland.txt`, `common/characters/ICE.txt`, existing ICE flag/cosmetic tag | Not overwritten by the adapter. The AAT history recruits `ICE_sveinn_bjornsson` and `ICE_bjorn_sveinsson_bjornsson`, so the setup roster gate has an existing source. |
| Vanilla inspect limits | The MCP resolver reported 193 blocking diagnostics, including missing/unknown vanilla sprite references in the game source scan. | These are vanilla-source diagnostics and were not patched in the mod. |

The vanilla tree contains no `shared_focus = independence_wave_overlay_take_stock_of_independence` import. A repository search finds that root only in `common/national_focus/006_independence_wave_focus.txt:43` and its definition at `:3151`, not in an ICE owning tree.

## Route coverage

| Required route or hook | Current source | Coverage | Risk |
|---|---|---|---|
| Existing ICE tree preservation | `common/scripted_effects/006_independence_wave_focus_effects.txt:29-56` and `common/scripted_effects/006_independence_wave_ice_package_effects.txt:214-252` | `additive_overlay` sets a flag and variable; no `load_focus_tree` is called. | The assignment records intent but does not attach shared focuses to `iceland_tree`. |
| Constitutional government | Setup calls `independence_wave_focus_allow_constitutional_route` at `006_independence_wave_ice_package_effects.txt:230`; route politics branch at `:148-156` | Runtime route flag, politics, popularity, and existing Sveinn leader promotion are present. | Event 006 constitutional focus IDs are inaccessible until a carrier or decisions-only exception is accepted. |
| Traditional restoration | Setup `:232`; route politics branch `:159-167` | Runtime route flag, neutrality politics, service-compact idea, and existing Sveinn promotion are present. | Same missing focus carrier. |
| Emergency military | Setup `:233`; route politics branch `:170-177`; decision `independence_wave_ice_declare_armed_neutrality` at `common/decisions/006_independence_wave_ice_decisions.txt:217-257` | Coastwatch threshold, security cost, route lock, idea, and existing Bjorn commander promotion are present. | Same missing focus carrier; static focus route is not visible on ICE. |
| Patron client | Setup `:234-235`; route politics branch `:180-194` | Patron route is unlocked, route idea is installed, and existing Sveinn is promoted without creating a new leader. | Patron influence remains shared-system owned; no ICE-specific focus carrier or probability evidence. |
| Former host | Setup enables negotiation, guarded-frontier, association, and reclamation flags at `:237-240`; decision `independence_wave_ice_settle_former_host_charter` at `:178-215` | Living-host requirement, war cancellation, bilateral settlement helper, and diplomatic ledger progress are present. | Generic Event 006 former-host focus branches are not attached to ICE. Host-remnant runtime admission remains parent-owned. |
| Network and league | `independence_wave_focus_allow_league_route` at `:243`; compact decision at `common/decisions/006_independence_wave_ice_decisions.txt:146-175` | Compact support and network standing thresholds are checked, and shared league deltas are applied. | No focus overlay visibility or probability sweep proves AI route selection. |
| FORM-02 North Atlantic Compact | `independence_wave_ice_package_effects.txt:244-246`; trigger checks at `006_independence_wave_ice_package_triggers.txt:48-55,104` | Family is selected and registered through the shared formable registry; compact decision opens discovery. | Central content attestation still excludes IW-012, so formable completion is not admitted. |
| Survival mission and projects | `common/decisions/006_independence_wave_ice_decisions.txt:11-249` | One timed harbour mission plus six costed projects serialize through `has_independence_wave_ice_active_package_project`. | AI choices use mostly generic decision weights; live timing and balance are unproven. |
| Force and military setup | `006_independence_wave_ice_package_effects.txt:247-252`; trigger `006_independence_wave_ice_package_triggers.txt:106-119` | p12 `coastal_maritime`, reinforcement flags, navy inheritance, and roster checks are wired. | Runtime materialization and save/load behavior remain parent-owned. |

The full Event 006 tree itself contains the generic eight-node overlay (`independence_wave_overlay_take_stock_of_independence`, `...secure_state_services`, `...integrate_release_forces`, `...open_foreign_desk`, `...address_former_host`, `...join_network`, `...open_regional_ambition`, `...mature_independence`) at `common/national_focus/006_independence_wave_focus.txt:3151-3270`. Those definitions have route gates, rewards, AI blocks, icons, and localization in the Event tree, but they are not imported by the vanilla ICE tree.

## Missing or simplified content

1. **High priority: additive carrier is missing.** `independence_wave_assign_focus_framework` only sets `independence_wave_additive_focus_overlay` for the additive mode. The offline national-focus rules require a static `shared_focus` import in the owning tree; a country flag cannot inject the root. No safe local patch can add this import to the game-owned `iceland_tree` without replacing or shadowing vanilla authority.

2. **Runtime admission is intentionally fail-closed.** IW-012 appears in the adapter list and exact preflight branch, but `has_independence_wave_runtime_package_content_attestation_for_execution_id` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` does not include package 12. The automatic readiness witness at `common/scripted_triggers/006_independence_wave_triggers.txt:479-486` therefore cannot pass until the parent completes package attestation.

3. **AI strategy types are not established by the installed vanilla corpus.** `common/ai_strategy/006_independence_wave_ice.txt:33-34,45,57-58` uses `production_convoy_factor`, `trade_opinion_factor`, `diplomatic_influence`, and `improve_relations`; none appears as an `ai_strategy` type in the installed vanilla `common/ai_strategy` files. Treat these lanes as unproven or inert until replaced with supported strategies or backed by engine-specific documentation.

4. **The ICE `prepare_for_war` strategy has no target.** `common/ai_strategy/006_independence_wave_ice.txt:46` omits the `id` required by the vanilla AI strategy examples and the offline AI-modding reference. The former-host target is dynamic, so this needs a deliberate supported replacement rather than a guessed tag.

5. **AI values and route selection are not scenario-proven.** The ICE constants use fractional fixed-point values such as `0.30` and `0.45`, while vanilla AI strategy values are integer weights and analogous Event 006 files use integer priorities. No probability sweep was run for hostile/living hosts, route locks, compact readiness, or the one-state survival case.

6. **No fallback was added.** Setup remains roster-gated and preserves the vanilla leaders; the removed dynamic recruitment calls are not replaced with generated characters or alternate assets.

## Icon coverage

| Surface | Coverage | Evidence |
|---|---|---|
| Vanilla ICE focus icons | 89 source focuses retain their vanilla icon references. | `iceland_tree` remains game-owned; no icon edits were made. MCP's vanilla sprite diagnostics are recorded above. |
| Event 006 generic overlay | 8/8 shared blocks specify existing Event 006 goal icons. | `common/national_focus/006_independence_wave_focus.txt:3151-3270`; icons are defined in the existing Event 006 interface package. |
| ICE decisions | 7/7 decisions specify existing Event 006 decision sprites. | `common/decisions/006_independence_wave_ice_decisions.txt:11,55,87,118,149,181,220`; definitions are in `interface/006_independence_wave.gfx:44-53`. |
| ICE ideas | 5/5 ideas reuse existing Event 006 idea pictures. | `common/ideas/006_independence_wave_ice_ideas.txt:27-76`; no new advisor or focus icon is introduced. |

No icon IDs changed in this retry.

## Localisation and reward mismatch list

- `localisation/english/006_independence_wave_ice_l_english.yml` contains the seven decision/mission names and descriptions, seven effect tooltips, five idea names/descriptions, and the decision category title/description.
- The file begins with UTF-8 BOM bytes `239,187,191`.
- The decision names match their effects: shipping registers, municipal charter, coastwatch, compact negotiation, former-host charter, and armed neutrality each set their corresponding flags/ledgers or route lock.
- No ICE focus-localization mismatch exists because no ICE focus overlay is actually attached. The generic Event 006 overlay keys remain in the full-tree localization file and are not missing in source searches.
- No obvious name-to-reward mismatch or repeated generic placeholder reward was found in the ICE decision/idea surface.

## AI behavior gaps

Vanilla `ICE.txt` and the historical/alternate ICE AI plans remain authoritative. The additive file enables survival, shipping, host-charter, and compact profiles only after IW-012 setup flags. The survival profile has supported army, infantry, support, naval-base, dockyard, and coastal-bunker priorities.

The shipping, diplomacy, compact, and host-war lanes listed above require replacement or documentation of unsupported types. The decision AI blocks mostly use shared generic urgency/high weights, with only host-war and armed-neutrality modifiers adding ICE-specific conditions. There is no focus-order AI evidence because the shared overlay is not attached, and no probability inspection/sweep was run.

## Changed files and identifiers

| File | Change | Focus IDs/localization/icon IDs |
|---|---|---|
| `common/scripted_effects/006_independence_wave_ice_package_effects.txt` | Removed two `recruit_character` calls from `independence_wave_initialize_ice_politics`; setup now relies on the existing roster attested by `has_independence_wave_ice_command_roster`. | No focus IDs, localization keys, or icon IDs changed. |
| `docs/events/006_independence_wave/iw012_ice_package.md` | Corrected the focus-integration paragraph so it no longer claims that an additive flag renders shared focuses on vanilla ICE. | No gameplay identifiers changed. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw012_ice_focus_audit_2026_07_28.md` | This audit handoff. | No gameplay identifiers. |

The removed recruitment calls were a narrow direct fix because repository guidance forbids dynamic `recruit_character` calls in scripted effects/on-actions and the ICE setup trigger already requires both vanilla characters.

## Validation performed

- Read `AGENTS.md`, the required focus, event, decision, asset, improvement-loop, and subagent skills, the offline Paradox wiki pages, and the relevant vanilla HOI4 documentation before auditing.
- Inspected the current ICE package effects/triggers/decisions/ideas/localization/AI and the dispatch/readiness hooks with targeted searches.
- Ran `hoi4.focus_inspect` on vanilla `iceland_tree` and on `independence_wave_focus_tree`; the vanilla inspect evidence is the artifact `focus-inspect.65c651a396eb7488.json` at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/891759fb6bc200577952ad5ebad05e2b1286913acac861eec9c43338a3e792f1/050cb92b90be670ffb82e10976969ca913f6d7a02137e40b9a4078eeafdcc21a/focus-inspect.65c651a396eb7488.json`.
- The current Event 006 tree inspect returned `validation.passed = false` with 14 blocking geometry diagnostics; the linked inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2da1c9a8013347e64aa04166b92de45328082417cf5b04106bfc7f7e848798a7/94c2de4332efb9024d7cac89832c555a1c17e2d02816f69d5ce1f436e20b0403/focus-inspect.e6f29840abd1e761.json`. The coupled geometry is central-tree scope and was not patched for ICE.
- `hoi4.focus_render` reproduced the same blockers and produced the HTML review artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eae89357ab4ad8c4f5e1432372d5838f099a602c4c28fb6eb95b6d431f20d97a/bc9929d19a29b8e090572f2f43b18ba0844b1a2ee7cab4915100385a5377c4ee/independence_wave_focus_tree.focus.html` and SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11c1c32334716d360aed8105602ef180f5f6e359d9b94dbadef434508ac4f5b7/de263d27dc69b7bd6b5937c61e79a4e767bf330c6059a281b8ad8de8fa8e4824/independence_wave_focus_tree.focus.svg`.
- Confirmed no ICE package `recruit_character` calls remain; the only ICE character effects in the adapter are promotions of existing vanilla characters.
- Confirmed localization BOM and existing decision/idea icon definitions.

## Skipped meaningful validation

- `hoi4.focus_rewrite` was skipped because the ICE issue is a missing carrier, not a movable focus node, and no safe patch can edit the game-owned tree without changing authority.
- No game executable, save/load, live allocator, runtime decision timing, or FORM-02 congress was run; those checks are parent-owned and explicitly outside subagent scope.
- No AI probability sweep was run because the current file contains unsupported/unresolved strategy types and no accepted scenario manifest.

## Remaining route risks and handoff

The parent should resolve the additive-carrier versus decisions-only architecture, replace or document the unsupported AI strategies, then add IW-012 to content attestation only after a country-package and focus audit pass. The host-remnant proof, force materialization, formable precedence against vanilla Nordic League, and live save/load cleanup remain unresolved.

No improvement-loop plan was written because the tree is not shallow and no new route family is requested. The implementation handoff remains this file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw012_ice_focus_audit_2026_07_28.md`.

No Git commit was created because the worktree is shared and already dirty; the parent owns review and the related plan commit.
