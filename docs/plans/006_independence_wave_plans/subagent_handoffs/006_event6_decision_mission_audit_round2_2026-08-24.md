# Event 006 decision and mission audit round 2

Date: 2026-08-24.

Owner: `/root/event6_decision_audit_round2`.

Parent: `/root`.

Status: read-only audit complete; no gameplay source was changed. The earlier FORM-08 cost mismatch and DM-01 disclosure findings are closed by current source handoffs. The highest-impact bounded next tranche is the FORM-03 package cost/icon and lifecycle presentation tranche, subject to asset/UI ownership for the missing League Reserve texticon and scenario-backed visible-action proof.

## Authority and scope

The requested `docs/specs/006_independence_wave_specs/003_decision_mission_gui_contract.md` is absent. This round used `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`, `docs/specs/006_independence_wave_specs/prompts/independence_wave_decision_mission_prompt.md`, `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`, `docs/specs/006_independence_wave_specs/matrices/006_wave_tuning_model.csv`, `docs/specs/006_independence_wave_specs/matrices/006_idea_lifecycle_matrix.csv`, `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, and the current Event 006 handoffs.

The required offline Paradox wiki pages were consulted: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`, and `Interface modding - Hearts of Iron 4 Wiki.md`.

The required vanilla documentation was consulted: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `script_collection_input.md`. Vanilla decision files were checked for `custom_cost_trigger`/`custom_cost_text`, `civilian_factory_use`, and selectable-mission precedents.

The audit covered Event 006 decision and mission categories, lifecycle gates, costs, requirement/tooltips, AI weights, route and target safety, cleanup, cooldown and duplicate risks, the shared Statehood Ledger GUI, and the formable state-puzzle GUI.

## Severity-sorted findings

### P1: FORM-03 League Reserve is a real consumed ledger value without a compliant texticon

`independence_wave_form03_request_development_compact_technical_mission` at `common/decisions/006_independence_wave_form03_decisions.txt:506-548` genuinely commits `global.independence_wave_league_shared_reserve` by `constant:independence_wave_form03_league.technical_mission_reserve_cost` and reserves a civilian factory through `modifier = { civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT }`.

Its gate at `common/scripted_triggers/006_independence_wave_form03_triggers.txt:431-443` requires post-charter progression, League membership, Development Compact route, shared reserve at least `technical_mission_minimum_reserve`, the administration-light material bundle, and no committed or completed mission.

Its payment and refund lifecycle at `common/scripted_effects/006_independence_wave_form03_effects.txt:848-888` subtracts 20 reserve at commitment, clears the commitment and returns 10 on cancellation, and clears the commitment while marking completion on success.

The cost keys at `localisation/english/006_independence_wave_form03_l_english.yml:206-208` show icon-first command power, manpower, and civilian-factory values, but spell out `League Reserve` with no corresponding texticon. No valid Event 006 League Reserve texticon exists in the current interface/GFX sources; the older `GFX_focus_soviet_collapse_league_reserve_table` is a focus icon, not a texticon, and must not be reused as a resource icon.

This is not an over-four-group finding if the factory commitment is counted as the fourth group: command power, manpower, civilian-factory commitment, and League Reserve. It is an icon-compliance and semantic-disclosure failure, not permission to hide the reserve charge in prose.

Recommended next action: register a dedicated League Reserve texticon through the accepted asset/UI route, then replace the literal in `independence_wave_form03_compact_technical_mission_cost` and `_blocked` while keeping the dynamic reserve amount and cancellation/refund wording. If the owner instead chooses a non-consumed ledger requirement presentation, the trigger/effect and cost contract must be changed together; do not silently move this charge into a description.

### P1: FORM-03 category has 23 structural child actions and lacks scenario-backed visible-action proof

`independence_wave_form03_low_countries_category` in `common/decisions/006_independence_wave_form03_decisions.txt:14-823` contains these 23 child IDs: `independence_wave_form03_authorize_core_delegation`, `independence_wave_form03_withhold_core_delegation`, `independence_wave_form03_belgium_authorize_founding_delegation`, `independence_wave_form03_belgium_withhold_founding_delegation`, `independence_wave_form03_join_as_autonomous_member`, `independence_wave_form03_convene_language_convention`, `independence_wave_form03_open_multilingual_service_examinations`, `independence_wave_form03_publish_member_language_codes`, `independence_wave_form03_establish_federal_language_appeals`, `independence_wave_form03_extend_protected_local_services`, `independence_wave_form03_reconnect_sambre_meuse_corridor`, `independence_wave_form03_coordinate_frisian_waterway_standards`, `independence_wave_form03_standardize_rail_and_customs_manifests`, `independence_wave_form03_request_development_compact_technical_mission`, `independence_wave_form03_invite_sovereign_corridor_partners`, `independence_wave_form03_ratify_confederal_charter`, `independence_wave_form03_resubmit_confederal_charter`, `independence_wave_form03_reopen_charter_talks`, `independence_wave_form03_repair_language_settlement`, `independence_wave_form03_repair_industrial_compact`, `independence_wave_form03_implement_member_language_guarantees`, `independence_wave_form03_fund_associate_corridor_share`, and `independence_wave_form03_withdraw_from_autonomous_membership`.

The category registration at `common/decisions/categories/006_independence_wave_categories.txt:165-183` is correctly gated to post-charter, sovereign-associate, pending-invitation, or autonomous-member states and attaches the existing `independence_wave_formable_state_puzzle_scripted_gui`. Child visibility is further phased by language, works, corridor, ratification, compromise, and member flags. This count is structural, not proof that 23 actions are simultaneously visible.

The package still needs scenario evidence proving the accepted maximum of six visible primary actions and the active-mission count in each phase. Do not add another warehouse category or tab solely to hide the actions. The bounded fix should phase existing actions by current language/works/ratification/member state, preserve the shared GUI entry point, and document the maximum visible set for founding invitation, post-charter drafting, works, compromise, ratification, and sovereign-associate states.

### P2: Shared Event 006 category density remains unresolved outside FORM-03

A current structural scan of `common/decisions/006_*.txt` found 87 category roots, 785 direct child action blocks, 56 categories above six children, 37 above ten, and a maximum of 26. The largest roots include `independence_wave_iw058_council_of_communities_category` at 26, `independence_wave_form03_low_countries_category` at 23, `independence_wave_karelia_crimea_category` at 22, and `independence_wave_form05_charter_category` at 16.

Route gates, one-shot flags, active-project locks, and local serialization may reduce simultaneous display. No complete scenario proof was available, so structural counts must not be treated as simultaneous runtime visibility. A broader category rewrite is out of scope for this handoff.

### P2: Raw category value rows remain cognitively dense

The Event 006 category descriptions still expose raw stability, war-support, cohesion, reserve, confidence, host, patron, network, phase, and threshold values. The Statehood Ledger status surface is intended to present five primary values plus former-host, patron, network, phase, and active-mission summaries, but ordinary categories remain text-heavy and their values do not consistently state cause, threshold, consequence, and next response on one compact surface.

This is a presentation backlog, not a safe source-only patch without completed GUI evidence. Meter/state-frame or threshold-marker work belongs in the existing GUI surface and must follow the mandatory GUI inspect/render/rewrite workflow if accepted.

### P2: DM-01 automatic mission disclosure is source-applied but live tooltip evidence remains blocked

`independence_wave_secure_provisional_capital` at `common/decisions/006_independence_wave_decisions.txt:19-82` remains intentionally `activation = { always = no }` and `available = { always = no }`, with the material commitment reserved by `independence_wave_start_provisional_capital_mission` before activation. Its `custom_cost_text = independence_wave_cost_provisional_capital` is now a dynamic disclosure keyed to force tier and capital supply.

`common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:69-200` selects fragile, viable, major, supplied, and isolated bundles, and `localisation/english/006_independence_wave_decisions_l_english.yml:115-131` uses the correct infantry, support, train, and motorized texticons. The automatic mission still has a 30-to-75-day central timer, capital/garrison cancellation, one-time activation, and explicit failure/relocation effects.

The source handoff `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_dm01_cost_disclosure_2026_08_22.md` and current source map treat this as closed at source level. Live tooltip/GUI observation remains unresolved because the required MCP routes timed out.

### P2: FORM-03 durations and mission lifecycle match the matrix, but AI probability is not closed

The FORM-03 map rows `FORM03-D01` through `FORM03-D18` in `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` match the current action families: language actions use 120/150/180-day bands, state works use 180 days, the Development Compact mission uses 180 days, charter ratification uses 360 days, reopening uses 360 days, industrial repair uses 240 days, and sovereign-member actions use 120/180 days.

The ratification mission `independence_wave_form03_ratify_confederal_charter` at `common/decisions/006_independence_wave_form03_decisions.txt:586-612` is activated once by `common/national_focus/006_independence_wave_focus.txt:2076-2083` after the full gate, runs for `constant:independence_wave_decision_duration.integration` (360 days), resolves success through `independence_wave_form03_resolve_full_ratification`, resolves timeout through `independence_wave_form03_resolve_ratification_timeout`, and cancels on loss of post-charter progression. Its failure/partial outcome logic is explicit in `common/scripted_effects/006_independence_wave_form03_effects.txt:950-1060`.

The source-qualified `hoi4.probability_inspect` call for `common/decisions/006_independence_wave_form03_decisions.txt` with `decision_ai_will_do` returned `INTERNAL_ERROR` with no artifact. The callable tool inventory did not expose a separate `chaosx_ai_probability_auditor` route. Existing probability handoff `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_probability_audit_round_2026_08_24.md` provides partial current Event 006 evidence, but no numeric result transfers to FORM-03. Do not rebalance FORM-03 AI scores until a source-qualified inspect and same-scenario comparison complete.

## Decision category lifecycle notes

- `independence_wave_form03_low_countries_category` is visible for post-charter carriers, sovereign associates, pending founding invitations with exact carrier/route anchors, and valid autonomous-member entry. `visible_when_empty = yes` supports the state-puzzle GUI but can leave an empty header after all child actions are complete.
- Founding invitation actions are mutually exclusive through consent-declared/withheld flags and the formable transaction lock.
- Language actions are serialized by `has_independence_wave_form03_active_language_action` and one-shot completion flags.
- State works are serialized by `has_independence_wave_form03_active_state_works` and exact ownership/control of state 34 or 36.
- Industrial administration actions are serialized by `has_independence_wave_form03_active_industrial_administration`; the technical mission additionally requires League membership, Development Compact route, reserve floor, and commitment guard.
- Ratification is a focus-activated mission after both progress values reach 70, all constitutional statuses resolve, and a federal language scope exists.
- Cleanup removes all carrier decisions and the ratification mission through `independence_wave_form03_remove_post_charter_decisions` at `common/scripted_effects/006_independence_wave_form03_effects.txt:1270-1285`; member decisions are removed from BEL/HOL/LUX at `:1302-1315`.

## Cognitive-load notes

Visible primary actions are structurally above the six-action review threshold in FORM-03 and many other categories, but exact simultaneous visibility is unresolved without complete scenario fixtures.

Active missions are bounded by shared founding/security/diplomatic/league locks and package-specific flags; FORM-03 adds language, state-works, and industrial-administration locks. The ratification mission is activated only after the convergence gate, but no typed scenario proves that no unrelated active mission remains alongside it.

Player-facing values in FORM-03 include Federal Accommodation, Industrial Integration, language model, charter phase, League Cohesion, Common Cause, Shared Reserve, Contribution, and Confidence. The category and descriptions name most values, but only the ratification description explicitly states both 70 thresholds and the consequence of timeout; the technical mission description states the reserve floor and refund but not an iconized ledger row.

Text density is highest in long package descriptions and composite tooltips. Current compact cost strings are icon-first for ordinary resources, but the custom reserve ledger is the one confirmed Event 006 literal spendable label remaining in this package.

Each visible FORM-03 value has a gameplay role, but the next player response is not uniformly clear: Federal Accommodation and Industrial Integration have progress thresholds, while League Contribution/Confidence and Shared Reserve are mostly explained through effects/descriptions rather than a compact meter or threshold marker.

## Mission quality notes

| Mission or action | Owner/category/region | Requirement | Duration | Success | Failure/cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_form03_ratify_confederal_charter` | LCX carrier; `independence_wave_form03_low_countries_category`; Low Countries carrier route | Post-charter progression, both progress values at least 70, all constitutional statuses resolved, federal language scope, no foundational member loss | 360-day integration band | `independence_wave_form03_resolve_full_ratification` sets complete outcome and integration flags | Timeout resolves full/partial/rupture outcome from live values; route loss cancels and resolves timeout | Low: focus activates once, completion/phase flags gate repeat, cleanup removes mission |
| `independence_wave_form03_request_development_compact_technical_mission` | LCX carrier; same category; Low Countries/Development Compact route | Post-charter, League member, Development Compact route, reserve at least 80, administration-light bundle, no active industrial administration or completion flag | 180-day long project band | Reserve commitment plus administration payment, then +10 Industrial Integration, +10 Capacity, and League ledger gains | Route loss cancels; 20 reserve commitment returns 10; cleanup also clears committed reserve | Low: active industrial lock, committed flag, completion flag, and cleanup removal |
| `independence_wave_form03_reconnect_sambre_meuse_corridor` | LCX carrier; same category; Walloon/Sambre-Meuse state-work route | Post-charter, state 34 owned and controlled, major factory/command/train bundle | 180-day long project band | Durable corridor modifier, infrastructure queue, +25 Industrial Integration | Ownership/control loss cancels and applies project-cancellation loss | Low: state-works lock and completion flag |
| `independence_wave_form03_coordinate_frisian_waterway_standards` | LCX carrier; same category; Frisian/northern waterway route | Post-charter, state 36 owned and controlled, factory/command/train/convoy bundle | 180-day long project band | Durable waterway modifier, infrastructure queue, +25 Industrial Integration | Ownership/control loss cancels and applies project-cancellation loss | Low: state-works lock and completion flag |
| `independence_wave_secure_provisional_capital` | Released country; founding category; capital region | Country-scoped material reservation, force-tier garrison, capital control and supply/transport branch | 30-to-75-day founding band | Timeout secures capital and opens administration | Capital/garrison loss cancels, records failure/relocation, and applies ledger losses | Low: activation is closed, reservation flag and `fire_only_once = yes` |

## Cost and requirement clarity

Current active custom-cost scan records zero Event 006 active custom-cost keys above four normalized spendable groups after the FORM-08 and shared palette tranches. This does not mean every package requirement is iconized or that all cost prose is closed.

FORM-08 is now action-specific and source-aligned. `independence_wave_form08_convene_river_congress` and `independence_wave_form08_standardize_rail_authority` use `can_pay_independence_wave_form08_administration_strategic_cost` and `independence_wave_decision_pay_form08_administration_strategic`, displaying stability, command power, transport fallback, and manpower. `independence_wave_form08_arbitrate_minorities` uses the security standard payment and displays manpower, army experience, infantry equipment, and support equipment. Civilian-factory availability is a capacity trigger and is not falsely presented as consumed cost. See `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form08_cost_disclosure_patch_2026-08-24.md`.

FORM-03's technical mission is four groups when factory commitment is counted: command power, manpower, civilian-factory commitment, and League Reserve. The first three use valid texticons; League Reserve does not.

FORM-03 state works correctly use equipment, command power, and factory burden instead of a flat political-power-only exchange. The matrix and source agree on state-specific ownership/control requirements for states 34 and 36.

Requirements and consumed costs are not uniformly separated in prose. The technical mission description explains reserve threshold, commitment, and partial refund, but the compact cost row lacks a visual distinction between the spendable topbar values and the shared ledger value. Any correction must preserve the visible reserve charge and use an approved icon.

## AI validity and route-lock notes

FORM-03 AI weights use central constants such as `independence_wave_decision_ai.low`, `.standard`, `.high`, and `.urgent`, with route/ideology/war modifiers in `common/decisions/006_independence_wave_form03_decisions.txt`. Source review finds no obvious dead-country target in this package: exact BEL/HOL/LUX existence and member flags are checked before sovereign-member actions, and state-work actions require exact ownership/control.

The technical mission is route-locked to `global.independence_wave_league_route = constant:independence_wave_league_route.development_compact`, requires League membership, and cannot repeat after completion. The ratification mission is focus-activated only after the full gate and cannot be manually repeated after completion.

The mandatory weighted audit route is incomplete. The fresh direct MCP call for the FORM-03 decision source returned `INTERNAL_ERROR` with no artifact, and no separate callable `chaosx_ai_probability_auditor` route was present. Existing Event 006 probability evidence remains partial or source-inventory-only for shared decisions, KUB/TAT mission fixtures, strategy factors, and most package pools. No AI patch or balance conclusion is justified.

## Localisation and tooltip gaps

The FORM-03 cost/tooltips are generally compact and icon-first after the current cost-localisation tranches. `independence_wave_form03_compact_technical_mission_cost` and `_blocked` are the exception because `League Reserve` is literal.

The technical mission description at `localisation/english/006_independence_wave_form03_l_english.yml:155` is long but materially useful: it states the -20 commitment, 80 floor, 10 cancellation refund, and factory assignment. It should be retained or shortened only after the cost row has a compliant icon.

The ordinary category descriptions and effect tooltips still expose raw values and repeated threshold prose. The next presentation tranche should use dynamic localisation or the existing GUI to show current band, threshold, consequence, and response rather than adding more paragraphs.

## Cleanup and exploit-risk notes

FORM-03 cleanup is stronger than the earlier audit implied. `independence_wave_form03_cleanup_runtime` calls `independence_wave_form03_cleanup_post_charter_progression`; cleanup sets the in-progress flag, refunds any committed technical reserve once, removes carrier and member decisions, removes the ratification mission, clears variables/flags, and removes state modifiers. Cancellation effects guard against duplicate ledger changes while cleanup is in progress.

The technical mission does not create free units, cores, or repeated equipment. Reserve commitment, partial refund, completion flag, industrial lock, and package cleanup prevent the obvious refund/restart loop. The remaining exploit question is scenario-level repeated lifecycle re-entry after a carrier identity transition; source cleanup clears the active package state, so this requires typed route testing rather than a speculative patch.

Shared Event 006 route/target helpers continue to require living countries, valid ownership/control, route compatibility, and active-origin/package gates. No narrow dead-country, impossible-border, stale-target, or cooldown bypass was proven in this round.

## Mandatory GUI evidence and fidelity limits

The two decision-owned GUI surfaces in scope are `independence_wave_status_window` and `chaosx_independence_wave_formable_state_puzzle_window`. Fresh read-only `hoi4.gui_inspect` calls for `independence_wave_status_window` with scenario `independence_wave_status_default` and for `chaosx_independence_wave_formable_state_puzzle_window` with scenario `E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_24` both timed out awaiting `tools/call` after 180 seconds.

Fresh `hoi4.gui_render` calls for both windows with normal/warning/minimum/maximum/long-text or normal/selected/locked/disabled/completed/long-text states at 1280x720 and 1920x1080 also timed out awaiting `tools/call` after 180 seconds. No `hoi4.gui_rewrite` call was made because no safe GUI patch was selected and the mandatory read-only route did not complete.

Historical partial artifacts remain available in the previous audit handoff: Statehood Ledger inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ff50e75abd1c602d184d5715f78167147c922e2d605a2f28a2558cdcc9a88b3/aafdeaf4bb1e7d4e40833d5f4a12e58841b7958d90bd45ed6770f3747bf056e7/gui-inspect.4810e6db3b628432.json`, Statehood Ledger render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d245b460614d138be4d724b8fbbe4c0c3ae510648ae12c90abf3733e231c13/d338d48ff29e92e22f3f8fa051291bb47280836c5a57b0656e32e5c8ba167b57/independence_wave_status_window-full.svg`, and the formable inspect/render artifacts referenced by `006_event6_decision_audit_round_2026_08_24.md`. They are historical fidelity evidence only and not current acceptance.

## Highest-impact bounded next tranche

Do not patch the current source tree in this round. The narrow tranche with the best impact-to-risk ratio is FORM-03 only:

1. Register and wire one dedicated League Reserve texticon through the accepted asset/UI owner, then update `localisation/english/006_independence_wave_form03_l_english.yml` keys `independence_wave_form03_compact_technical_mission_cost` and `_blocked` and verify the cost row against `common/scripted_triggers/006_independence_wave_form03_triggers.txt:431-443` and `common/scripted_effects/006_independence_wave_form03_effects.txt:848-888`.
2. Build a route-state fixture matrix for `independence_wave_form03_low_countries_category` covering founding invitation, post-charter language, works, industrial Development Compact, sovereign-associate, compromise, and ratification states. Record exact simultaneously visible primary actions and active missions; do not infer from the structural count of 23.
3. If any fixture exceeds six visible primary actions, phase existing child visibility by the already-authored flags and action locks in `common/decisions/006_independence_wave_form03_decisions.txt` and `common/scripted_triggers/006_independence_wave_form03_triggers.txt`. Keep one category and the existing scripted GUI; do not add a warehouse tab.
4. Re-run `hoi4.gui_inspect` and `hoi4.gui_render` for both existing windows, then run source-qualified `hoi4.probability_inspect` and same-scenario comparison for FORM-03 decision/mission weights before any AI or tooltip acceptance claim.

Exact source/localisation surfaces for the tranche are `common/decisions/006_independence_wave_form03_decisions.txt`, `common/decisions/categories/006_independence_wave_categories.txt`, `common/scripted_triggers/006_independence_wave_form03_triggers.txt`, `common/scripted_effects/006_independence_wave_form03_effects.txt`, `localisation/english/006_independence_wave_form03_l_english.yml`, the dedicated League Reserve icon/GFX registration file selected by the asset/UI owner, and the existing GUI files wired by `independence_wave_formable_state_puzzle_scripted_gui`.

Acceptance evidence should include the icon-first cost row, pre/post reserve values, cancellation refund exactly once, no duplicate action after completion, visible-action count per fixture, GUI inspect/render artifacts at 1280x720 and 1920x1080, and probability artifacts with source revision, source hash, scenario hash, and unresolved diagnostics.

## Validation and blockers

`python -B .tools/audit_event6_allocator.py` passed in the current tree and reported 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 32 content attestations, 29 compatible groups, the 3/4/5/7/10 automatic ladder, and the retired pre-event crisis surface.

The current source review confirmed 23 FORM-03 child IDs, 22 `custom_cost_text` references across 14 unique keys, and the single literal spendable label `League Reserve` in the FORM-03 custom cost row.

The FORM-03 probability inspect returned `INTERNAL_ERROR` with no artifact. The two required GUI inspect calls and two required GUI render calls timed out after 180 seconds each. These are route blockers, not evidence that AI or visual layout is valid.

Live Hearts of Iron IV launch, save/load, and gameplay validation were not run because live consumer validation belongs to the user.

No decision, mission, category, scripted effect, scripted trigger, AI, GUI, asset, or localisation source was changed by this round. The only new file is this handoff. Existing concurrent worktree changes were preserved.

Remaining issues are the missing League Reserve texticon, scenario-backed FORM-03 visible-action proof, broad Event 006 category density, raw ordinary-category values, live GUI tooltip evidence, and typed FORM-03 probability evidence. FORM-08 cost disclosure and DM-01 source-level disclosure are not remaining issues; their handoffs are current and should not be reopened without new evidence.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_audit_round2_2026-08-24.md`.
