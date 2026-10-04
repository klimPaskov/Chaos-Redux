# Event 014 actual raid-target evidence

## Source capture

The exact current Event 014 source bytes are copied under `current_source_snapshot/` and indexed by `current_source_snapshot/source_snapshot_manifest.json`.

The source capture uses the parent label `14f045+GenGuard`; its recorded Git head at capture was `35c5916539b485ee0971060afa5619e79e82b708`.

The decision, effects, triggers, constants, and English localisation byte hashes match the 2026-10-03 Larder probability baseline manifest; all eight captured Event 014 source paths were clean in `git status` at capture.

The source copies are evidence files under this proposal's `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-04_actual_raid_target_owner_proposal/evidence/` directory, not runtime source edits.

All source citations in this handoff refer to that captured pre-owner-patch snapshot.

At the final read-only status check, Git head was `72046dd78ee414f4310eec050cd4cedfc4368aff`; the shared worktree showed modifications to `common/scripted_effects/014_cannibalism_effects.txt`, `common/scripted_triggers/014_cannibalism_triggers.txt`, `common/script_constants/014_cannibalism_constants.txt`, and `localisation/english/014_cannibalism_l_english.yml`, while `common/decisions/014_cannibalism_decisions.txt` remained clean.

Those modified paths match the source owner's stated write set; this subagent did not inspect their in-progress contents and does not claim they match this proposal.

Parent acceptance basis: the 2026-10-04 parent message accepts the existing March state-target strike with unchanged preparation modifier, costs, duration, cooldown, and recoveries as full-field fidelity, and selects `0.50` damage units in the existing fixed-point Warlord decision constants group.

Source ownership remains with `01a10386` for Event 014 effects, triggers, constants, and localisation through its patch and commit; this handoff owns only the accepted design proposal and evidence.

Application remains queued until the current-source AI baseline and target fixtures are captured and recorded.

The parent reports that data worker `01a103a4-2c1c...` finished the proposed reader hooks; the accepted raid receipt contract stores stable state, action kind, result, date, `ROOT` generation, and the controller's current country generation when it is an Event 014 actor.

The data receipt must use the committed state target, not the earlier view-only selected-state proposal; no province target is selected by the native state-target decision.

## Accepted spec and current GUI/API evidence

`docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_6_decisions_missions_and_gui.md:438` accepts a selected raid or infiltration target; lines 470-477 name the raid-action family; line 599 requires a raid-target card in the Warlord command window.

The parent-designated current gap is `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_final_current_completion_audit.md:67-81`, E014-FINAL-03; it records the missing card and says the old audit did not allege missing raid gameplay.

`docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_gui_required_fields_data_api.md:132-138` records that the March operation has no target and proposes a view-only selection; the current user instruction rejects a controlled-state view selection as the raid target.

`docs/plans/014_cannibalism_plans/2026-10-04_gui_data_implementation/evidence/owner_api_proposal.md:2-7` records parent acceptance for the data-owner contract, keeps the AI baseline frozen, and assigns actual targeted raid work to the parent.

The current window is `cannibalism_warlord_command_window`, bound by `cannibalism_warlord_command_scripted_gui`; `interface/014_cannibalism_frontline_hunger.gui:132-153` contains its background, meters, and capacity row but no raid-target card, while `common/scripted_guis/014_cannibalism_scripted_gui.txt:157-183` contains its visibility and value bindings.

The existing background glyph is `GFX_cannibalism_warlord_command_background`, wired at `interface/014_cannibalism_frontline_hunger.gui:137` and defined in `interface/014_cannibalism.gfx:541`.

The getter `GetCannibalismUiRaidTarget` and the localisation card key are proposals in the Data API handoff, not current source definitions.

## Current source and decision inspection

`hoi4.source_lookup` returned the exact current definition `cannibalism_march_raid_supply_depot` in `mod:common/decisions/014_cannibalism_decisions.txt:2569-2588`, source revision `ee16f1dacebf49d427b40f03c2885f015fed64a3675ce97783734888823d1b08`, with `overridden = false`.

The exact-ID `hoi4.decision_inspect` request used scenario `E014_MARCH_RAID_PAID_BASELINE_2026_10_04`, actor `CBA`, date `1936.1.1`, the March-host/action flags, Larder `35`, and command power `10`.

That result was `DECISION_ANALYZED_PARTIAL`, `complete = false`, source revision `ee16f1dacebf49d427b40f03c2885f015fed64a3675ce97783734888823d1b08`, report hash `12c84a7f4675a118855809aae808d0a9005787f06f697d987db711d336f523a1`, 7,949 indexed decisions, and 218 unresolved definitions; the inline index was bounded to 64 of 6,578 source paths.

Its report artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7659dc155bd18e9c4c8fa7659fb96b905fa795a614a2a554086c10b64894eb52/01996367bbe55fd5d8715174321e59782c6d343531ea28ae6efbf5f8e1ec2f8c/decision-12c84a7f4675a118855809aa.json`.

No broader decision-inspection retry was made after the required exact-ID request returned a partial result.

The decision source calls only `cannibalism_begin_march_supply_raid_operation`; it has no `state_target`, `target_trigger`, target pointer, or target receipt.

`common/scripted_effects/014_cannibalism_effects.txt:17109-17120` rechecks payment, computes the existing route bonus, pays the existing cost, applies `cannibalism_march_supply_raid_operation` to the acting country, and applies route-based recovery.

`common/dynamic_modifiers/014_cannibalism_dynamic_modifiers.txt:105-110` shows that modifier is a country operation buff; it does not damage a target state.

The operation cost is Larder `35`, command power `10` with a `> 9.99` gate, 30 base days, and the unchanged `long_reenable_days` value of 30 in `common/script_constants/014_cannibalism_constants.txt:1614-1616,1666-1669`.

Its present AI expression is base `constant:cannibalism_decision_ai.high` with `constant:cannibalism_decision_ai.urgent_factor` when `has_war = yes`.

## Existing real target audit

`cannibalism_infiltrate_ritual_cell` is a paid `state_target = yes` decision at `common/decisions/014_cannibalism_decisions.txt:915-939`; its root gate is `cannibalism_containment_decisions_visible` during Evolution I, and its target is a `ROOT`-controlled state with an active cell, node identity, and no infiltration cooldown in `common/scripted_triggers/014_cannibalism_triggers.txt:983-992`.

That transaction increases the target node's strength and raises investigation evidence and cell strength in `common/scripted_effects/014_cannibalism_effects.txt:7531-7560`; it is a genuine infiltration target, but it belongs to the ordinary containment phase and does not identify a hostile supply target for the Warlord command window.

The unified enemy-front-collapse decision has a real country target in `common/decisions/014_cannibalism_decisions.txt:1876-1892`, but it is a CBL campaign operation and cannot identify a state supply depot.

The Wendigo terminal hunt is a real paid country target with target lock, an explicit 120-day mission, and success/failure cleanup in `common/decisions/014_cannibalism_decisions.txt:2797-2862`, `common/scripted_effects/014_cannibalism_effects.txt:6418-6453,6503-6568`; it belongs to the post-reveal Wendigo command route.

The continental and naval hunt actions are non-targeted country operations; convoy harvest processes existing receipts; `cannibalism_record_warlord_major_victory_harvest` records a capitulated country once after victory and is not a paid target selection (`common/decisions/014_cannibalism_decisions.txt:1862-1921`; `common/scripted_effects/014_cannibalism_effects.txt:17047-17072,15064-15170`).

The Warlord state-targeted recruitment decision `cannibalism_raise_bone_guard` provides the closest same-owner map selector pattern in `common/decisions/014_cannibalism_decisions.txt:2297-2322`; its purpose is recruitment, so its state must not be presented as a raid target.

## Offline wiki and installed-game references

Offline `Decision modding` targeted-decision example, path `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 550-575, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, documents target roots, target triggers, and `FROM` use.

Offline `Decision modding` state-target section, same path and revision, lines 576-595, documents `state_target = yes`, per-state `FROM` scope, the `on_map_mode` values, and the broad state-pool performance cost.

Installed `common/decisions/_documentation.md`, lines 1-46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, documents that `target_root_trigger` is root-country scope and `target_trigger` is evaluated for each target state/country.

Installed `documentation/effects_documentation.md`, `damage_building`, lines 3374-3416, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, supports `damage_building` in STATE scope.

Offline `Effects - Hearts of Iron 4 Wiki.md`, Buildings, lines 1752-1792, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, describes damage to a named building in a state and the damage amount.

Installed `documentation/triggers_documentation.md`, `any_neighbor_state`, lines 1497-1505 and `has_war_with`, lines 5051-5059, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, confirms STATE neighbor scope and COUNTRY war relation.

Vanilla `common/decisions/BALTIC.txt:131-170` provides a state-targeted decision with a target trigger; vanilla `common/scripted_effects/ITA_scripted_effects.txt:3204-3208` checks `supply_node > 0` before damaging a `supply_node`.

The vanilla example's `damage = 1.5` is structural precedent only and is not a proposed Chaos Redux balance value.

Installed `common/buildings/00_buildings.txt:98-116` defines `supply_node` as a province building, sets `province_max = 1`, and sets `damage_factor = 0.1`; the entry does not define `value`.

Offline `Building modding - Hearts of Iron 4 Wiki.md`, Additional arguments, lines 111-134, revision `1e5fb5410a26af12b5b791b193f8f602c4ef8a3614ed897ae4c67084477f7bfc`, says `value` determines base health and multiplies by building level, but does not establish a default when the building entry omits `value`.

Therefore `0.50` is reported as a damage amount in building damage units, not as 50 percent of supply-node health; `damage_factor = 0.1` is a separate incoming air/land damage modifier.

Installed `documentation/triggers_documentation.md`, `building_count_trigger`, lines 1830-1840, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, supports STATE scope and lists `supply_node` as a countable building.

Installed `documentation/triggers_documentation.md`, `non_damaged_building_level`, lines 6554-6569, describes the state-scoped `building` and `level` check; the narrow live `reference_read` returned `REFERENCE_SECTION_UNKNOWN`, so this exact section was read directly from the installed documentation file.

The proposed target predicate combines `supply_node > 0`, `building_count_trigger = { supply_node < 2 }`, and `non_damaged_building_level = { building = supply_node level = 1 }` so a state target has one supply node and that sole node can still take damage.

Installed `damage_building` documentation lines 3374-3416 says that when a province building is addressed through a state, the effect searches the state's provinces and uses the first matching building; the unique-node target predicate removes that ambiguity without inventing a province picker.

The receipt stores the exact selected state, kind, result, date, `ROOT` generation, and the controller's current country generation when it is an Event 014 actor; no province pointer is selected or claimed.

Target fixtures required before source application are no eligible hub, one unique healthy supply node, a multiple-hub state, a fully damaged sole hub, a recycled Event 014 controller, and the current Larder/command-power boundaries.

The offline state-target decision documentation and bounded vanilla decision search exposed no province-target decision pattern; this proposal keeps the accepted native state-target surface and does not guess or score a province.

## Probability baseline

The read-only `chaosx_ai_probability_auditor` audited only `cannibalism_march_raid_supply_depot` and confirmed decision source SHA-256 `AD356DB7875965262A049BCDC858499193EE5C2163DC1C736AA066C063D279D3`, matching the captured source.

Scenarios `event014_march_raid_supply_depot_peace_costs_satisfied` and `event014_march_raid_supply_depot_war_costs_satisfied` return eligible raw AI scores `60` and `150` respectively; the existing war modifier is `2.50`.

The auditor's Larder sweep tested `34` as unaffordable and `35` as affordable with command power `10`; the existing command gate is `> 9.99` and the re-enable value is 30 days.

The results are exact score-only outputs, not normalized probabilities; both inspect outputs report `poolComplete = false`, the supplied pool is empty, and actual campaign state and external AI strategy factors were not supplied.

Inspect source revision was `f909093237b7b9060ac5ec5b94b6a6645f6cbdf849fd807dbeebd44159defb89`; evaluate/sweep source revision was `9110eb2fcb2ab5f3babda07f6350668322a150425c45d610ef40f7ee4d9af9fc`.

Baseline scenario hashes are `4cb9e1617f5c556f20a5aa98d39fe5c6078cdd07439a32bdaf2580d8b7ef50c8` and `2b35d95f291835467efa6a8334395e69c05305077b3181e924f4636468d821bf`; no probability comparison was run because no patch exists.

Targeted inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ee7b4b1d587840af08af2de554707c7fe127720b233790bebd509024b43a64f/578a268e290310508d70d951bc85b4d2022008f55c4977c8cbb5c13c44bc2514/probability-inspect-669879e6f1b5.json`.

Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e9da922a81c52e1d5b2beba3390aa8def9986cd3bfbd94596a7e1195d7e907e/627756a9fe8393e17e838fe840907f51d94c5a42735f4401995856b598f083bb/probability-2c9c5e702bc622a02628923d.json`.

Evaluation waterfall: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00ee4325d7edef74d3016f389eb3983e765440e5eb4568785dc3e5c6509c71a4/ce7570adb12c4c291705629550a799c028a0e2b9364d634c364c17bbd567405b/probability-probability-2c9c5e702bc622a02628923d-waterfall.svg`.

Sweep artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae9c407af300c4f778b292aca659a50b58fe46a110080a686e464d0e3e9fcaa1/c61e510ca1ce40c35a90b6ea7cf658518227c726b2d83b9a1827a23c882d7c50/probability-59bd22f9bf5db82a86448c8e.json`.

Sweep sensitivity and threshold artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0e88acab4e6deb9701fd07e3ff824e524772f63d13a91b06f39c2af019c5137/2f46efcc9c5378ac80dc78b5656dd6db009e0164ae9c17035126d9fb9ad36e3c/probability-probability-59bd22f9bf5db82a86448c8e-sensitivity.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/4ac76b22c5f86aa0b16af0c34ee1c29b0a25cde7d981692c0c049b45031366bb/probability-probability-59bd22f9bf5db82a86448c8e-threshold.svg`.

The auditor's completion text did not enumerate the four sweep scenario IDs, so this handoff preserves their scenario hash and artifact instead of inventing names.

A bounded read of the sweep JSON returned `MCP error -32603: Artifact provenance manifest is unavailable`; the parent should retain the scenario fixture from the probability evidence before any owner patch.

## GUI inspection and render

`hoi4.gui_inspect` inspected `cannibalism_warlord_command_window` for scenario `E014_DATA_API_WARLORD_20261003`, status `GUI_INSPECTED`, 17 selected elements, zero skipped sources, shared revision `5c074b8fa873319560ca8db0984b95dd6320b062e0efc3bfb3157f90fd06a1f1`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/581ed9f0c57b2359d1253d889fc12fa2073426eee62fab9c7417462a984b7080/d37e207e1ac7f14a0a02500c308c8c303f4fcad927bdfa8fcb1d2869ce9c9d36/gui-inspect.5c074b8fa8733195.json`.

`hoi4.gui_render` rendered the same named window and scenario at 1920x1080, UI scale 1, normal state; status `GUI_RENDERED`, one state, one resolution, source revision `5a257322039e48f295a47a8ae31a465f1a913870286d5da71f275a95f35b4442`.

Full PNG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7857d36c861a9fde5b8cac9d69b0f0de04fd39b26ae9b4cf528746204a66279d/8fd3514167c1e548527d2433c9160bb42aafcadc12895ef87e3c1dc1fa2b4643/cannibalism_warlord_command_window-full.png`.

The rendered source diagnostics include 16 `GUI_VISIBLE_OVERLAP` findings, unresolved Larder/alignment/capacity values, three missing static animation fallbacks, and missing coverage for unrequested non-normal states.

The PNG could not be read for pixel review: both bounded `read_mcp_resource` requests, `offset=0&length=32768` and `metadata=manifest`, returned `MCP error -32603: Artifact provenance manifest is unavailable`.

No visual defect is dismissed; no pixel-level visual acceptance or click-region review is claimed from the production render, and no render retry was made.
