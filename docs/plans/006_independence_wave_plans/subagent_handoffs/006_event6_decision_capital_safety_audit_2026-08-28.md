# Event 006 decision capital-scope safety audit — 2026-08-28

## Disposition

This was a read-only audit, and no gameplay, localisation, existing documentation, or asset file was changed.

No additional bounded patch meets the strict semantics-preserving bar for the current tree.

The existing `has_independence_wave_current_capital_controlled_by_root` helper in `common\scripted_triggers\006_independence_wave_triggers.txt:199-205` is the correct fail-closed primitive for an absent or zero-state Event 006 shell.

The dormant Banat/AXX, Epirus/BBX, and Thrace/BAX decision sections in `common\decisions\006_independence_wave_balkan_decisions.txt:1-234`, `:477-710`, and `:941-1170` contain zero raw current-capital control predicates and 23 helper references per section.

## Evidence and engine semantics

The required repository instructions and the `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents` skills were reviewed before the audit.

The relevant offline references were `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md:253,257-264,314-315` and `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:81-105,337-340,451-463`.

The vanilla documentation precedents were `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:1612-1617,5336-5343,5381-5385` and the vanilla `common\decisions\AFG.txt:107-111` `any_owned_state` control pattern.

The wiki explicitly marks `capital_scope` as a country-to-state scope that can produce an invalid event target when no capital exists, while `any_owned_state` is a country-to-state iterator and `is_capital`/`is_controlled_by` are state triggers.

The decision documentation makes `visible` and `available` continuously evaluated for visible decisions, while mission `activation` is the daily appearance gate and `cancel_trigger` ends an active mission.

## Severity-sorted findings

### High — prior dormant-shell error class is covered

The AXX/BBX/BAX pre-release decision surfaces are now fail-closed through `has_independence_wave_current_capital_controlled_by_root`.

The generic provisional-phase gate is also helper-backed at `common\scripted_triggers\006_independence_wave_triggers.txt:210`.

The package predicates used by the remaining package decision categories include `is_independence_wave_active_country = yes`, and the generic provisional/recognized phase predicates include the same active-country gate at `common\scripted_triggers\006_independence_wave_decision_triggers.txt:14-30`.

### Medium — raw controls remain on live runtime surfaces by design

The central decision registry retains raw current-capital predicates only at `common\decisions\006_independence_wave_decisions.txt:45,98,151,215,272,491,543,582` for DM-01 through DM-05, DM-10, and the treasury-backed public-works action.

The consolidated Balkan registry retains raw controls only in the active BOS, MAC, MNT, TRA, and KOS sections at `:257-471`, `:742-935`, `:1195-1427`, `:1456-1649`, and `:1673-1854`; the AXX, BBX, and BAX sections are excluded by the zero-count check above.

Other active package decision registries retain their existing live controls in these bounded file regions: `006_independence_wave_bashkiria_mari_decisions.txt:30-1104` (46), `006_independence_wave_far_eastern_decisions.txt:38-592` (23), `006_independence_wave_form01_02_04_decisions.txt:32-51` (2), `006_independence_wave_form48_decisions.txt:25-334` (7), `006_independence_wave_formable_decisions.txt:31-311` (9), `006_independence_wave_frontier_decisions.txt:34-1163` (48), `006_independence_wave_iberian_decisions.txt:21-393` (42), `006_independence_wave_karelia_crimea_decisions.txt:21-466` (34), `006_independence_wave_mediterranean_decisions.txt:27-371` (25), `006_independence_wave_pacific_decisions.txt:27-552` (35), `006_independence_wave_rhineland_bavaria_saar_decisions.txt:26-873` (70), `006_independence_wave_scotland_wales_decisions.txt:20-416` (36), `006_independence_wave_siberian_decisions.txt:46-3931` (169), `006_independence_wave_transcaucasus_decisions.txt:28-253` (24), `006_independence_wave_wallonia_frisia_decisions.txt:32-634` (42), and `006_independence_wave_western_decisions.txt:30-861` (62).

These raw decision controls are inside post-release package categories or active/provisional phase decisions and are paired with the existing cancellation, route, project, and cleanup logic.

The scan found 805 raw positive/negative current-capital control occurrences across the Event 006 decision/trigger/event surfaces, including the one multiline achievement proof; the count is not a recommendation to mechanically replace every occurrence.

Replacing every raw control with the helper would be a broader behavioral change, because the helper intentionally restricts the test to a capital state still owned by `ROOT`, while a valid live country's raw `capital_scope` can continue to describe its capital through occupation or an ownership transition.

### Medium — two shared helper predicates are review-only residuals

`common\scripted_triggers\006_independence_wave_decision_triggers.txt:380` uses raw current-capital control inside `can_pay_independence_wave_provisional_capital_cost`, which is called by `independence_wave_refresh_country_state` only inside its active-country branch at `common\scripted_effects\006_independence_wave_effects.txt:182-193`.

`common\scripted_triggers\006_independence_wave_decision_triggers.txt:401` uses raw current-capital control inside `has_independence_wave_safe_reserve_surplus`; its sole decision consumer is DM-41 at `common\decisions\006_independence_wave_decisions.txt:2253-2258`, whose visible gate is recognized-or-later and therefore active-country gated.

These two lines are possible future defensive-hardening candidates, but changing them is not required to protect dormant shells in the current lifecycle and is not proven semantics-preserving for all live ownership transitions.

### Low — unrelated live-country and fixed-target uses must remain

The live achievement/focus proof controls at `common\scripted_triggers\006_independence_wave_achievement_triggers.txt:13,283-286` and `common\scripted_triggers\006_independence_wave_focus_triggers.txt:105` are final-state/capstone checks, not dormant package availability gates.

The live package controls at `common\scripted_triggers\006_independence_wave_iw043_iw058_package_triggers.txt:1047,1057`, `006_independence_wave_karelia_crimea_package_triggers.txt:195`, and `006_independence_wave_pacific_package_triggers.txt:177` are inside active package predicates and remain unchanged.

The Event 006 AI modifier at `events\006_independence_wave.txt:396` is a live-country decision-weight check and remains unchanged; no AI weight patch was proposed, so no probability compare was required for this read-only audit.

## Required exclusions

Fixed capital-anchor proofs must remain because they test a named state rather than current-capital control: `common\scripted_triggers\006_independence_wave_form48_triggers.txt:27,35,43,164,180,197,280`, `006_independence_wave_compatibility_triggers.txt:21,59,101,150,208,224,254,285,311,338,365`, and `006_independence_wave_formable_registry_triggers.txt:1583,1593,1602,1721`.

The FORM-08 fixed state proof at `common\scripted_effects\006_independence_wave_formable_registry_effects.txt:1104` also remains unchanged.

Supply-node semantics must remain in `common\scripted_triggers\006_independence_wave_decision_triggers.txt:356-366` and `common\scripted_effects\006_independence_wave_decision_effects.txt:948-956`; these checks decide whether the provisional-capital transport burden uses a supply node, trains, or motorized equipment and are not current-capital control tests.

Current-capital construction effects at `common\decisions\006_independence_wave_decisions.txt:507-513` and `:563-570` must retain their state target because the infrastructure is intentionally built in the current capital.

Scenario patron/belligerent distance selectors at `common\scripted_effects\006_independence_wave_scenario_effects.txt:685-758,983-990` are map-distance selectors, not raw control checks, and were not widened by this audit.

## Lifecycle, cognitive-load, mission, cost, AI, localisation, and cleanup notes

The generic Event 006 categories are active-country/phase gated in `common\decisions\categories\006_independence_wave_categories.txt:51-121`, and package categories use package predicates that include the active-country gate; no dormant shell category or mission was exposed by the remaining controls.

The raw controls are hidden requirement/cancellation predicates rather than new player-facing values, so this audit found no new visible-value significance or text-density issue and made no localisation change.

DM-01 remains an automatically activated, material-committed mission with explicit cancellation and failure handling; DM-02 through DM-10 and package missions retain their existing owner, category, region, duration, success, failure, and cleanup wiring.

No duplicate mission activation, cost-loop, free-equipment, war-goal, core, or cooldown exploit was introduced or found in this narrow scope.

No decision cost count or texticon coverage changed; existing costs remain outside the requested capital-scope repair.

AI target/route validity and package route locks remain unchanged; the retained AI modifier is the only raw Event 006 event-weight use in this audit surface.

## MCP status

The mandatory read-only `hoi4.gui_inspect` for `independence_wave_status_window` succeeded with 48 inspected elements and no blocking source-graph diagnostics.

The corresponding `hoi4.gui_render` succeeded for the requested states and resolutions, but reported an existing fatal `GUI_TAB_STATE_CONFLICT` plus overlap/animation-fallback warnings; this is a status-window GUI issue unrelated to capital-scope safety and no GUI rewrite was authorized.

The shared `chaosx_independence_wave_formable_state_puzzle_window` inspect and render both succeeded; the render validation passed with no overlap or blocking diagnostics.

Primary artifacts were `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/502c8bd886b63b784551f923d7e51e28a97b6e7577a1a9c1063d0783bfcaf1f6/44868f2db5df3bfa24b13e627fac97418bf4393a755413c63b18a78baef45bd6/gui-inspect.8e0f49f2549b575f.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64aa57fc1fb57131d0872c1dc24293786ab9aff8820ec72ffe7efb575aec0124/f6fc51a957540bb5e2ee6d2490246896234ee8932d67e114d9f6b9fbf8d4fa33/independence_wave_status_window-full.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/303ac8e0c2e1d946b96982b4b513dd72976b5de8b76ddcf1497b1fc417de9ddb/cddae6cf73adca4dda2202f2d9b09c84eb5e428f3228b5b59158d0f4292d7ea5/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

No `hoi4.gui_rewrite` was run, and no `chaosx_ai_probability_auditor` route was needed because this tranche proposes no weighted-logic change.

## Validation and handoff

The focused static scan confirmed zero raw current-capital controls in each AXX, BBX, and BAX decision section and 23 helper references in each section.

If any future hardening patch is accepted, rerun the Event 006 allocator, country API/flag, FORM-16, and scenario-matrix checks relevant to the touched files, then repeat the GUI/source MCP evidence and route any AI-weight change through probability inspect/evaluate/compare.

No live game or save validation was run or claimed.

Recommendation to the parent: accept this audit as no-change, retain all listed raw live/fixed/supply uses, and do not mechanically replace the remaining 805 controls without a separate design decision covering ownership-transition semantics.
