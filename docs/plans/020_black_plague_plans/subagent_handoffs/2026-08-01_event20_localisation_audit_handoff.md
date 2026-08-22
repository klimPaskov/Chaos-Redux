# Event 020 localisation audit handoff

## Scope and result

This audit covered the Event 020 English localisation files, the shared Event Details, event-log, world-end, triggerable-scenario, mapmode, debug, and super-event scripted-localisation surfaces, and the current Rat Nation and Rat King decision and focus consumers. No new country tag or 3D model was introduced. The package still uses exactly `RTA` and `RTX`.

The only narrow player-facing localisation defect found was a triggerable-scenario description that disclosed a hidden terminal route by saying that the final apocalypse remained locked. The description now describes the escalating plague in-world without exposing the future route or its lock state.

## Changed files and keys

- `localisation/english/chaosx_gui_l_english.yml`: `chaosx.scenarios.black_plague.desc`.
- Before: `A contagious Black Plague erupts across multiple continents. A Rat Nation rises among the infected while the Rat King gathers a separate royal basin. Evolutions I through IV are forced. The final apocalypse remains locked.`
- After: `A contagious Black Plague erupts across multiple continents. A Rat Nation rises among the infected while the Rat King gathers a separate royal basin. The outbreak advances through an escalating chain of plague evolutions.`

The existing Event Details world-end keys `chaosx.events_log.world_end.black_plague.title` and `chaosx.events_log.world_end.black_plague.details` were already present in the working tree and were not changed by this audit.

## Audit findings

### Missing keys

No Event 020-specific localisation key is missing. The complete source-reference scan found only `GFX_super_event_085_rat_king_coronation` and `GFX_super_event_086_rat_king_takeover` as apparent misses. These are intentional sprite names, not localisation keys, and both are defined in `interface/020_black_plague_super_events.gfx`.

All 192 `name`, `desc`, `custom_cost_text`, `custom_effect_tooltip`, and `custom_trigger_tooltip` references in the Event 020 decision files resolve. All 23 Rat Nation and 38 Rat King focus title and description pairs resolve. The two remaining focus IDs without a matching pair are the tree roots `black_plague_rat_focus_tree` and `black_plague_rat_king_focus_tree`, which do not require player-facing focus text.

### Duplicate keys

No duplicate key exists in the Event 020 localisation files or in the shared Event 020 surfaces checked here. A repository-wide scan still sees unrelated pre-existing Event 012 `africa_world_*` duplicates in `localisation/english/012_africa_world_order_l_english.yml` and `localisation/english/012_africa_world_union_war_l_english.yml`; they are outside this scope and were not changed.

### Scripted-localisation issues

No unresolved Event 020 scripted-localisation selector remains. The Event Details and event-log scan resolves all 25 Event 020 world-end/evolution references, the scenario scan resolves all 12 SCN-012 references, and the mapmode scan resolves all 31 Black Plague references. The nine `GetBlackPlague...` methods used by response and mapmode text are all defined in `common/scripted_localisation/`.

The two GFX tokens listed under missing-key findings are correctly routed through the super-event sprite selector and should not be added to localisation.

### Dynamic-text opportunities

Population-scaled support equipment, motorized equipment, fuel, Medical Reserve, manpower, trains, convoys, stability, command power, response burden, and durations already use scoped variables or constants in the current Event 020 text. The prior generic `black_plague_shared_action_cost` text is no longer consumed by the shared decisions.

The shared-response cost rows in `localisation/english/020_black_plague_response_l_english.yml` still spell civilian-factory counts as literal `1`, `2`, or `3` while the corresponding decisions use direct `civilian_factory_use` values. This is readable today but could be centralized through shared constants and dynamic localisation if the response-cost system is tuned later.

### Cross-surface mismatch notes

- `common/decisions/categories/020_black_plague_rat_categories.txt` and `common/decisions/020_black_plague_rat_decisions.txt` both define `black_plague_rat_brood_category` and `black_plague_rat_king_court_category`. This is duplicate gameplay registration, not duplicate localisation, and should be resolved by the decision owner.
- `black_plague_rat_harden_the_immune_blood` is available only when `black_plague_rat_disease_immune` is absent, while both Rat and Rat King initialisers set that flag immediately. The localisation promises a permanent immunity action, but the current source makes the button unreachable. This needs a gameplay decision, not a wording-only patch.
- `docs/systems/air_cleanliness/air_contamination_mechanic.md` still says that SCN-012 has no live public row, while `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`, `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`, `localisation/english/chaosx_gui_l_english.yml`, and `docs/systems/event_system/triggerable_scenarios.md` show the live SCN-012 adapter. The older `2026-07-24_part9_scn012_adapter_handoff.md` and `2026-07-29_event20_core_readiness_report.md` also describe pre-implementation or pre-registry states and should be treated as historical until documentation is reconciled.
- The live world-end registry, Event Details selectors, and `chaosx.events_log.world_end.black_plague.*` keys are present. Older readiness text claiming that the public Black Plague terminal row is absent is stale rather than a current localisation gap.

### Encoding

Every checked Event 020 or shared localisation file is UTF-8 with BOM. The touched `chaosx_gui_l_english.yml` retained its BOM after the patch. Git's LF-to-CRLF warning is a line-ending normalization notice, not an encoding failure.

## Validation

The focused Python audit scanned all Event 020 localisation files and the shared Event Details, event-log, scenario, mapmode, and super-event surfaces for BOMs, duplicate keys, missing localisation references, and unresolved custom methods. It reported zero Event 020 duplicate keys, zero missing localisation keys, and zero unresolved `GetBlackPlague...` methods after treating the two intentional GFX names as sprite references. Decision and focus key scans were also run as described above.

No Hearts of Iron IV executable was launched. Live gameplay and GUI consumer validation remain parent/user-owned.

## Unresolved wording decisions

The scenario impact rows still mention that Evolutions I through IV are forced because those rows describe the selected scenario's visible setup. The hidden terminal-lock sentence was removed from the general description. If the parent wants the scenario UI to avoid all explicit evolution numbering, that is a separate wording choice rather than a missing-key defect.

## Recommended parent actions

Keep the patched scenario description. Route the immune-blood availability mismatch and duplicate decision-category registration to the decision owner. Consider a later dynamic factory-count localisation pass if shared response costs become tunable. Reconcile the stale SCN-012 and world-end statements in the historical docs. No further Event 020 localisation patch is required for key coverage or scripted-localisation loading.

Handoff path: `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_localisation_audit_handoff.md`.
