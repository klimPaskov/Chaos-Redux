# Inactive and protected interface review for Handoff 2

The three historical camp choices are obsolete definitions replaced by the genuinely new national administration mechanic, and the research choice is contained in an explicitly protected restoration.
Keep those four choices without restoring their old parent windows.
Keep the Disease Board's three historical layouts inactive under owner plan A12.
The parent removed its residual presentation opener, and the focused source recheck confirms no interface open hook remains.
The parent owns all renders.
This worker changed only this handoff, performed no GUI MCP calls, launched no game, read no logs, and made no commit or push.

## Authority and scope

Read `AGENTS.md`, `docs/plans/handoffs_2026-10-13/00_common_rules.md`, `02_interface_restores_left_undecided.md`, `docs/plans/chaos_redux_restore_plan_2026-10-12.md`, and the relevant rows and evidence of `docs/plans/interface_restore_audit_2026-10-13.md`.
Handoff 2 supersedes the older audit's unclear-choice retention rule.
Old acceptance labels alone are not used as keep grounds.
Owner A12 explicitly rejects the Board, B12 explicitly requests technology consolidation while preserving the upper chemical tree, and Handoff 2 item 3 explicitly protects `cd2f068437` and `30ac00fb03`.
No gameplay balance, AI, event-chain, portrait, 3D, catalog or live-engine completion claim is made by this bounded visibility/history review.

Initial source snapshot HEAD was `d9ee328c87fa46af6af6693086e2b6094ebfa31e`.
Working file hashes below identify the reviewed bytes independently of concurrent commits.

## Choice dispositions

| Choice | Action | Concrete basis and exact historical source |
| --- | --- | --- |
| `776c6848818c5a266ce10df4767741b4b5861e2a` | Keep current administration, do not restore obsolete camp pages | Parent `bdb917e93981e229d4ea946be425bec98a0ac874:interface/camp_repression_ledger.gui`, lines 65–80, has the old Overview/State Pools/Sites/Country/Discovery navigation and Refresh, with overview at 83 and old State Pools at 109. Those controls and corresponding consumers no longer exist in engine-loaded GUI sources. The new administration policies, funded-work slots, crisis and finite records did not have an earlier window in this parent. Root identifier reuse does not preserve its old content. |
| `9bf6beab9a32cfc5ab32e6925c88acdcf02f6ba5` | Keep current administration, do not restore obsolete rail/cards | Parent `9e7a29142336bf7118e25c29814cd0711d49a131:interface/camp_repression_ledger.gui`, lines 66–70, has old vertical tab consumers, overview at 83, State Pools at 102 and Discovery at 156. Neither this sidebar nor the commit's later horizontal rail/cards survives. Restoring them would reintroduce the retired manual command family over the new administration consumer. |
| `57a17719791bb96e1a7aa498850917ea4dde890b` | Keep current administration, do not restore obsolete alignment/seals | Parent `5ed9e92e7300c986f63ef5ae27586aefa02cb3b7:interface/camp_repression_ledger.gui`, lines 66–70, has rail x=18/190/362/534/706 at y=102, reach card x=0 at 87 and evidence seal at 179. All those named rail/card/seal consumers are absent from current interface and scripted-GUI files. Current native administration uses its own new controls. This disposition does not approve the historical recentering or seal substitution. |
| `35bc07594338d04ec12eb87f9b32fceef91649c5` | Keep inactive Board, preserve rejection | Parent `c8445c8138c277d6418229d1ad1425b4aac39d29` contains the pre-compaction Board in `interface/biowarfare_disease_containment.gui` and its matching scripted GUI. Owner A12 explicitly rejected this entire workflow, implemented by protected `3deac2d4da401de6e47c04f3170a409833ddffa4`. Restoring an earlier active Board would contradict that specific owner request. |
| `023bf29dc400b7ac5c9a7a79cba00ecbc0040991` | Keep inactive Board, preserve rejection | Parent `f2e6d8eb0facff509bc34edf7e2284a8b806db42` has the earlier summaries and named disease tabs in the same GUI/scripted-GUI pair. A12 overrides this historical presentation choice. Do not resurrect its old tab/data bindings while the rejected Board remains detached. |
| `23c6e94c114385fc22121746539816159da55f6c` | Keep inactive Board, preserve rejection | Parent `96d613885d3f3b9abbff8f369c42397a58f0c6de` has the earlier selector/filter/header view in the same pair. Protected A12 disables both consumers regardless of flags or state. No Board geometry restoration is needed. Residual opener removal is a separate presentation cleanup described below. |
| `073f76002294ebb69017b1b53eef62c6f88958de` | Keep protected research restoration | Parent `d49f7d74d5f063c6dbb20a4b250a90c11f83bcb1:interface/countrytechtreeview.gui` has the literal template defaults `lol boat`, `lol boat guns`, `bang bang klik`, `Happy-Go-Lucky-Tank`, `Where is the name?`, and `category:`. The change replaces 31 scalar text defaults without geometry or behavior changes. Do not infer a demonstrated visible bug from engine-populated fallback fields. The decisive keep reason is exact preservation of the protected entire-file `30ac00fb03` restoration, including the same 31 ordered defaults already present in protected `cd2f068437`. |

## Camp replacement evidence

`3098ed9d2bc3d6b0eab5008c5bcd9e6d2b086422` replaces the old manual GUI with the national administration interface.
Its parent is `2e44610483208a74831ea9242c2faaa9389cf6ca`.
The parent GUI has 114 unique named elements and no `camp_admin` policy, funded-work, location-registry or finite-history consumers.
The new committed GUI introduces `camp_admin_tab_administration`, `camp_admin_tab_locations`, and `camp_admin_tab_records` at lines 13/16/19, policy pickers at 35/37/39, separate economy/institution panels at 40/46, location list at 66 and finite history list at 88.
The same commit replaces the old 550-line scripted-GUI consumer with the administration dispatcher and new dynamic lists.

Comparing each of the three exact historical parent GUIs with current source leaves only four meaningful shared names: `repression_ledger_category_window`, `repression_ledger_category_open_button`, `repression_ledger_window`, and `camp_gui_close_window`.
The old pages, cards, seals, pool/site selectors, tabs and Refresh are absent across current `interface/` and `common/scripted_guis/`, rather than surviving as a separately accessible legacy window.
This supports the genuinely new mechanic exception, not a generic accepted-redesign exception.
It does not classify later cosmetic changes to the new administration window.

Current `interface/camp_repression_ledger.gui` uses the new tabs at lines 19/23/27, administration panel at 33, policy controls at 53/55/57, funded-work panels at 58/66, locations at 94/98 and records/history at 141/169.
Current `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`, lines 3–21, connects the reused category/root names to `camp_admin_refresh_interface`, three `camp_admin_view` values and picker cleanup.
Its final dynamic lists populate the new location/history rows from `camp_admin_gui_states` and `camp_admin_history_ids`.
The active inbound entry is `common/decisions/categories/genocide_crisis_categories.txt:16`, `scripted_gui = camp_repression_ledger_category_scripted_gui`.
The category checks eligibility and visible camp actions at lines 9–14.

The mechanic source `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/accepted_implementation.md`, lines 14–16 and 23–25, independently names automatic priority/mandate/spending, separate economic/institutional slots and the three new views.
Its line 10 records the September 6 implementation acceptance, but the keep decision rests on the actual new consumers and absence of the old window, not that status label alone.

## Disease Board entry visibility and remaining hooks

Protected `3deac2d4da401de6e47c04f3170a409833ddffa4` replaces both top-level visible bodies with `always = no` and removes the category attachment.
That result survives in current `common/scripted_guis/biowarfare_disease_containment_scripted_gui.txt:16` and `:35`.
`common/decisions/categories/biowarfare_disease_containment_categories.txt:3–8` contains no `scripted_gui` attachment.
The only exact window references are the inert definitions at `interface/biowarfare_disease_containment.gui:20/:33` and their own disabled bindings at scripted-GUI lines 14/32.
There is no other engine-loaded interface/category opener to those windows.

The initial review found these residual opener declarations, which the parent subsequently removed as recorded in the final recheck below:

| File / block | Residual hook | Status |
| --- | --- | --- |
| `interface/biowarfare_disease_containment.gui:29`, header window | `buttonType` named `disease_containment_board_open`, with `disease_containment.gui.open` and `.open.tt` | Hidden by disabled parent, but still an opener declaration. |
| `common/scripted_guis/biowarfare_disease_containment_scripted_gui.txt:18–20`, header effects | `disease_containment_board_open_click = { disease_containment_board_open = yes }` | Sole caller of the open effect, inside the disabled header. |
| Same file, lines 22–24, header triggers | `disease_containment_board_open_click_enabled` | Residual opener enablement binding. |
| `common/scripted_effects/biowarfare_disease_containment_effects.txt:416–429` | `disease_containment_board_open`, sets `disease_containment_board_open` at 419 and adds `THIS` to `global.disease_containment_board_open_countries` at 422 | Gameplay helper has no other call. Preserve under this presentation-only task. |

Source-wide exact call/setter scanning covered `common/`, `interface/`, `events/`, and `history/`.
No active inbound call to the open helper was found.
Existing refresh callbacks remain in `events/020_black_death.txt:109`, `common/scripted_effects/020_black_plague_effects.txt:1847`, and `020_black_plague_scenario_effects.txt:732/:794`.
They call refresh-open helpers, which only rebuild already-open state or close it, never set the open flag.
Their presence cannot overcome top-level `always = no`.
This audit makes no gameplay repair recommendation for them.

## Disease Board inert asset and localisation checks

All 35 localisation keys consumed by the reviewed Board/header GUI resolve exactly once across `localisation/english/*.yml`.
All 73 `disease_containment` prefix keys in that English inventory are unique.
Definitions remain in `localisation/english/biowarfare_disease_containment_l_english.yml`.
No missing or duplicate Board key was found.

All seven consumed sprite names have one effective definition and each referenced DDS was fully decoded with Pillow.
`GFX_tiled_window` has one mod override and one vanilla precedent, not duplicate mod definitions.
No pointer stub, missing texture or decoder failure was found.

| Sprite / exact definition | Resolved texture | Dimensions | SHA-256 |
| --- | --- | --- | --- |
| `GFX_black_plague_crisis_seal_static`, `interface/020_black_plague_rat_identity.gfx:78` | `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_static.dds` | 64×64 | `1ac112d10e013b7e077910ab6aaacda871eaa9ad8eebb0f54e479c9e82e6c933` |
| `GFX_black_plague_crisis_seal_animated`, same registry at 83 | `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_sheet.dds` | 512×64, 8 frames declared | `c477abdc6f09078bc1f1e1a82b7f12c486a0d964367c485f8d210fa34c2f2d5a` |
| `GFX_chaosx_button_123x34`, `interface/chaosx.gfx:92` | `gfx/interface/chaosx_button_123x34.dds` | 123×36 | `57212d055703ceb8d82bdd916370c500df602e124ffc75c09575b14f9055e9f7` |
| `GFX_decision_bio_expand_biosecurity_capacity`, `interface/biological_countermeasures.gfx:38` | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_expand_biosecurity_capacity.dds` | 32×32 | `5d94bdc612f412447d67e03968d3177f814b5e624e254515527f2bd357e700a1` |
| `GFX_decision_bio_expand_medical_capacity`, same registry at 34 | `gfx/interface/decisions/biowarfare/countermeasures/decision_bio_expand_medical_capacity.dds` | 32×32 | `1a10e89e0be110834d7d73ce89cfc732d75b6e064c54f6cf5a650076dc2a326e` |
| `GFX_tiled_window`, `interface/countrytechtreeview.gfx:253` | Installed vanilla `gfx/interface/tiles/tiled_window.dds` | 192×192 | `b3a4c47d11ca655e69cfafa257300d9fbd51f395652e63152ad7d2ba24f5ba6b` |
| `GFX_tiled_window_transparent`, installed vanilla `interface/core.gfx:148` | Installed vanilla `gfx/interface/tiles/tiled_window_transparent.dds` | 95×95 | `f25207c86dd9afa64d97da8863598eda5fb4790d90a54ae1457ddfd9b5949cc9` |

These source and decoder checks found no load defect in the audited inert Board localisation or sprite dependencies.
They are not an engine-load test and do not establish visual acceptance or rendered state coverage.

## Protected research evidence

Current entire `interface/countrytechtreeview.gui` is byte-identical to `30ac00fb0300f664ba17aed3b2af3d911690bbf3:interface/countrytechtreeview.gui`.
Its SHA-256 is `094d6d55f011298a94c72d7be7a97698e1b62dc45d9d289c3240022ef74ba56b` and Git blob is `0199b1a1aa326e5b3abbafd6b8edc379591a9ca8`.
Protected `cd2f06843749af324c799df8bf55e376ba6d2c2f` is byte-identical to the restored `4337957b1f` GUI, SHA-256 `32e87c79055f991d560b609e88ae9bb62e127ad86f314ef970af2361346ccf2e`.
Current source differs from that earlier restore through the subsequent protected B12 consolidation and root-binding corrections, so a whole-file equality claim against both protected commits would be false.
All 31 template default assignments are preserved exactly as an ordered stream between `cd2f068437` and current source.
Current examples are `Research Bonus` at 4837, `Technology` at 4882, `Unnamed Battalion` at 6636 and `Category` at 7026.
The historical copyedit is classified as a protected existing restore, not a proven fallback-label bugfix.

## Source provenance and verification limits

| Reviewed file | SHA-256 |
| --- | --- |
| Current `interface/camp_repression_ledger.gui` | `6592c4f020f46ba7446f72f6d01ddb7d42be91149c610adf880662acd9f49326` |
| Current camp scripted GUI | `0f8652433d1cfaae82692db74e5a2b51ddb1986f365f7bcde5c66efc4ab3cd22` |
| Camp parent of `776c6848818c` | `a7e0f61973ef0f708e20fa33311220ae783bf0e680312fc1c507b6c076803c68` |
| Camp parent of `9bf6beab9a32` | `2368ec4c169459e933d837b4feb9a55553bf5f54996422ddbc1c936e80259be8` |
| Camp parent of `57a17719791b` | `cffd0c296db06762af92c554e2d6dc28419361b1c7d72201a1368e658752dbbc` |
| Camp replacement `3098ed9d2bc3` GUI | `3b6a0bcbee508fc624723acf2d7855e0937679042e28e94aa0a9ca32011c0f98` |
| Initial current Disease GUI | `bc25a820aa74f89add8aad42c41858eab66bfee3e12a7f6a47f792459e826efe` |
| Initial current Disease scripted GUI | `ba47826bf69b56f84dfa56a0b3deb962721b3ed06b1e2a9bb11f30b452989515` |
| Current Disease category | `37324ac7a931c8620f90bf9cd04295f4a249ced7aad966245efc703628fa5f52` |
| Disease GUI parent of `35bc07594338` | `bbaf561276ecf96a5affd96b32d3e4cc1baccd4b46435cd3937ae343c6ec441f` |
| Disease GUI parent of `023bf29dc400` | `6471b3cbf7139f79157748eed359b621dec16393c91a39651274a394af88c391` |
| Disease GUI parent of `23c6e94c1143` | `0b2535873e31c30f15d3a7ea695b7ce02ba1cbe80ade15a80bbe1c6edb1292f5` |
| Current Disease English localisation | `2a045de2adcec7c7edbf4ad49a0feb2660d89b25cd0e27d6d9d3a418b4bb5500` |
| Current `interface/020_black_plague_rat_identity.gfx` | `20aa9681c39bf83e0b0bab72ae0aa54d7fca1a952ab332b5a70bdf04e4ef7b66` |
| Current `interface/biological_countermeasures.gfx` | `febac90c065a9eeff6f94f192038af26e09ff6ebd852f5495a4763f353a4fe48` |

Reused the owner's reference coverage and reread the pertinent local sections without reopening unchanged MCP checks.
Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`, lines 1–80, SHA-256 `43ce647fc5fde27488855b060b5463c790e5e356149fceb010d36b960b40f838`, documents named-window attachment, decision-category attachment, visibility and button effect/trigger binding.
Offline `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, lines 369–386, SHA-256 `b74afc86be4e5dbb3b0fc600820d73a8340f7dc1821fc5ef02c9ee1f028c0b1c`, documents anchor-relative positioning.
Installed `interface/sov_paranoia_system_scripted_gui.gui`, lines 1–75, was reread as the native separated sprite/text precedent.
No new MCP failure or retry was incurred.
No weighted pass is needed for this read-only UI history and visibility scope.

All seven historical-choice dispositions are resolved for the parent table.
The initial handoff requested removal of the three residual presentation opener declarations.
That patch and its focused recheck are complete.
The older main audit's unresolved-choice wording and the owner plan's A-INTERFACE line are stale under Handoff 2 and remain parent-owned updates.
Renders and broader restoration completion are outside this worker's ownership.
No simplification was introduced by this audit.
Skills read and applied: `chaos-redux-scripted-gui`, `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, and `chaos-redux-event-assets`.
No skill was created or updated.

## Final focused opener recheck

On the parent's request, rechecked only the three removed opener declarations, the disabled top-level bindings, the detached category and active inbound callers.
The `disease_containment_board_open` button is absent from `interface/biowarfare_disease_containment.gui`.
The header's `effects` and `triggers` bodies at scripted-GUI lines 18–24 contain no `disease_containment_board_open_click` or `disease_containment_board_open_click_enabled` hook.
Both top-level bindings still have `visible = { always = no }` at lines 16 and 35.
The final `chaosx_disease_containment_category` at category lines 3–9 contains no scripted-GUI attachment.
Its unrelated civilian eligibility guard was not evaluated by this presentation-only recheck.

The exact active-source scan across `common/`, `interface/`, `events/` and `history/` now finds only the uncalled gameplay helper definition at `common/scripted_effects/biowarfare_disease_containment_effects.txt:416` and its internal flag setter at 419.
No active inbound opener call, header open control, open-click hook or category attachment remains.
The inert window definitions and disabled `window_name` bindings remain intentionally preserved.
The initial asset/localisation results were not repeated because no relevant asset, localisation or remaining sprite input changed.

| Final checked source | SHA-256 |
| --- | --- |
| `interface/biowarfare_disease_containment.gui` | `11021ae3ae15bea9149a29a2e2c096e766cca09ec9d16568408b9df72a914868` |
| `common/scripted_guis/biowarfare_disease_containment_scripted_gui.txt` | `602e54a30d472fd90eb0aedbacd74fc61a43c4e33def8796ca0057d6141e74c0` |
| `common/decisions/categories/biowarfare_disease_containment_categories.txt` | `e4bf7ba0a6aa4b43345e7f93c7da81a7b3394e604a7f995d59ae21102382ae1a` |

The current source conclusion is resolved: the rejected Board remains disabled and detached, with no residual interface opener.
No remaining implementation blocker was found within this seven-choice and opener-review scope.
Rendered and live-engine behavior remain outside this worker's evidence.
