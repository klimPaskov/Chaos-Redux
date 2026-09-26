# IW-040/KUB focus group and mission gate implementation handoff

**Disposition:** implemented as a bounded IW-040 source tranche; Event 006 remains **HOLD / PARTIAL**.

**Acceptance basis:** the user authorized the active Event 006 rework with “i approve everything” and supplied the explicit objective requiring highlighted packages to receive country-specific focus content. The parent accepted the five-focus KUB design and the narrow mission/government reachability repair in Part 4. The user's separate choice retains root-level shared-focus imports and records imported-node layout evidence as blocked.

## Implemented source

The full Event 006 tree imports `independence_wave_kub_record_stanitsa_petitions`, `independence_wave_kub_reconcile_grain_and_rail_registers`, `independence_wave_kub_hear_non_host_petitions`, `independence_wave_kub_audit_mounted_service_roll`, and `independence_wave_kub_publish_land_and_service_docket`. The hearing and service-roll branches are mutually exclusive, and the docket requires the selected branch plus its matching paid-project receipt.

Every KUB node and reward helper requires the active Event 006 origin, exact IW-040/KUB package, complete setup, full-tree and generic focus contracts, and owned, controlled, capital state 234. Ledger changes use the existing clamped helper and central constants. The new tooltips describe bounded gains and conditional compact stabilization.

`independence_wave_kub_community_compacts_project_paid` and `independence_wave_kub_border_guards_project_paid` are published only by the successful project `remove_effect`s, after their existing guarded package callbacks. Their decision visibility no longer depends on the shared callback flags, so a prior generic focus reward cannot hide an unpaid project. Cancellation and timeout do not publish either receipt. The matching +5 companion works in both focus-first and project-first order and is guarded by its award flag.

The government-choice decisions use `is_independence_wave_kub_government_choice_open` before founding resolution and serialize through `has_independence_wave_kub_active_government_project`. Vanilla `triggers_documentation.md` defines `has_decision` as an active selected decision. The 600-day mission still requires stable ledgers, a government, and owned and controlled state 234; every other package project remains gated on successful mission resolution. Existing decision costs, durations, route outcomes, cancellation effects, and failure behavior were preserved.

## Files changed

- `common/national_focus/006_independence_wave_focus.txt`
- `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_kuban_package_effects.txt`
- `common/scripted_effects/006_independence_wave_focus_effects.txt`
- `common/decisions/006_independence_wave_frontier_decisions.txt`
- `localisation/english/006_independence_wave_focus_l_english.yml`
- `localisation/english/006_independence_wave_frontier_l_english.yml`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `docs/events/006_independence_wave/kuban_package.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`
- `docs/plans/006_independence_wave_plans/006_event6_reg04_kuban_focus_group_improvement_addendum_2026-09-26.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw040_kuban_focus_tree_audit_2026-09-26.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw040_kuban_decision_mission_audit_2026-09-26.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw040_kuban_decision_ai_probability_audit_2026-09-26.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw040_kuban_localisation_audit_2026-09-26.md`

The read-only localisation audit found all 22 scoped keys present exactly once, with no missing callers or duplicates, and confirmed both English files retain UTF-8 BOMs. Parent follow-up clarifies that both paid projects satisfy the matching route requirement for the Land and Service Docket, shortens the companion text, specifies the former-host claim, and replaces the semicolon join in the branch effect lines. The loss tooltips currently display `minor_gain` as the positive magnitude of `minor_loss`; the two values are +5 and -5 in the current shared KUB pressure ladder. If they are tuned separately in the future, update this presentation with the actual loss magnitude.

The focus-tree audit handoff confirms the five-node route and reward gates, and identified two filter tags and two description strings for parent follow-up. The parent replaced the unregistered `FOCUS_FILTER_LOGISTICS` with `FOCUS_FILTER_INDUSTRY`, removed the irrelevant `FOCUS_FILTER_WAR_SUPPORT` from the service-roll focus in favor of supported `FOCUS_FILTER_MANPOWER`, and aligned the two focus descriptions with the accepted addendum. The route-aware AI and imported-node visual evidence remain unresolved or blocked as recorded below.

The decision/mission audit confirmed the source-level cycle repair and both receipt orders, and identified three shared cost labels with four values inline. Parent follow-up reduced `independence_wave_cost_security_standard`, `independence_wave_cost_security_major`, and the KUB strategic cost label to three inline values while retaining all paid resources and factory commitment in their full tooltips. No affordability condition, cost amount, payment effect, or duration changed. Native decision-row wrapping is still unverified.

The read-only KUB government-choice AI audit used `decision_ai_will_do` and its mission-adapter fallback, but the required input pool remained incomplete and its constructed 15-scenario evaluation was invalid fixture evidence. The sweep could not bind the KUB ledger variable; no valid same-scenario comparison exists because the MCP workspace has no distinct pre-edit source path. Existing source scores were documented but not treated as probabilities. No numeric AI weights changed; route-aware choice and deadline feasibility remain unresolved. The exact evidence and MCP artifacts are in the linked probability-audit handoff.

## Evidence and limits

Post-change `hoi4.focus_inspect` returned `FOCUS_INSPECTED` at revision `abfac347f793f1880cb1020e579a3a96cfb86842fb22b986f1cd2d566ec8c4ea`, with 184 direct nodes, 196 connectors, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, zero crossings, zero node intersections, zero too-close pairs, and one 10-column long connector. [Inspection artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8cd2f83c97661cc511887e0e5e068a6146cf4c6b8a2acf454dd3794b64caf60/ade344ec3aa14ca4469bb42c8776f1a4fdfa5ff3b6f2279366fc93d441d761f7/focus-inspect.abfac347f793f188.json)

Latest post-localisation `hoi4.focus_inspect` returned `FOCUS_INSPECTED` at revision `666ad1c923955705ba25af5e026053425fb63bc77281e80243116b9d242fdf59`, with the same 184 direct nodes, 196 connectors, zero crossings/intersections, zero too-close pairs, one 10-column connector, and unchanged layout hash; [latest inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2cce08b47836a096a2044f62822772f20ddaaa12168f7c43bdc6eec2a11cc80/d2c51911fcce18c4b3ab4b1e5e350dee469282bdde44ae9e18e909de1d3a32aa/focus-inspect.666ad1c923955705.json). It continues to omit imported root-level shared focuses, so it still cannot establish the KUB group layout or attachment.

After the focus-filter corrections, the final `hoi4.focus_inspect` returned `FOCUS_INSPECTED` at revision `79f302324aed7f2504e252e51cdd1bc9e6b86da510ba41894186258846b5a911`, with 184 direct nodes, 196 connectors, zero crossings/intersections, zero too-close pairs, one existing 10-column connector, and layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`; [final inspect artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e54b79601e46972b1928bd83632f92d6151a4b688e59461b303eb267f9c513d7/9d2f5ae26c5e748cd9d43359bd1677dbb6518160beccad3e1b630c55cc1848c5/focus-inspect.79f302324aed7f25.json). Matching `hoi4.focus_render` returned `FOCUS_RENDERED`; [final HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11ec2175bda4262c6a28c70f299fd7eee6e24f3dc9b4d706a65da261bd3f79bf/a4da20a88c98aad31209924cf838212d8c4e5c755b239f6b76cedf7a33cbe1dd/independence_wave_focus_tree.focus.html) and [final SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/2556a32d442d32d34137fb2b95ac0db2d104c1cc408b44ec9357492152b3321a/independence_wave_focus_tree.focus.svg) share the direct-node-only view. The MCP importer still cannot prove the KUB shared-focus attachment or layout.

Post-change `hoi4.focus_render` returned `FOCUS_RENDERED`; [SVG artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/6881bdaa4bcd2d8d0acba80c794da8ce74f947f9ea1c6539460f8dffc0b5cfb0/independence_wave_focus_tree.focus.svg) and the other render artifacts share the direct-tree-only view. The importer omits root-level shared focuses, so it cannot prove the five KUB imports, selected-route layout, connector geometry, or icon visibility; the user's selected path records that evidence as blocked. The renderer also reported the existing vanilla `continuous_restrict_freedom_desc` localization warning.

The 34/41 starting-ledger arithmetic was reviewed for the five-focus group only. The group alone does not reach 60/60 stability. No complete typed campaign probability comparison, route-aware AI evidence, deadline-feasibility scenario, decision/mission MCP receipt, or live-game result is established by this tranche. The separate Event 006 completion auditor failed with HTTP 401 before returning an audit handoff. The user remains responsible for live-game validation.

No new art or tuning constant was needed; the five registered icons and existing KUB pressure and duration constants were reused. No direct-focus duplicate, new GUI, mission completion reward, government reward, claim, core, or network admission was added.
