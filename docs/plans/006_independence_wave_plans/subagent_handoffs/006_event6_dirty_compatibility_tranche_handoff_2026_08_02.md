# Event 006 dirty compatibility tranche handoff

Date: 2026-08-02.

Owner: parent implementation handoff.

Status: **INVENTORIED / REQUIRES TARGETED VALIDATION**.

This handoff records the Event 006 portion of the current working-tree compatibility tranche. It does not claim that the whole tranche is committed, game-compiled, or runtime-verified, and it does not promote any package, formable, asset, or super-event gate.

## Scope

The tranche addresses engine-sensitive source surfaces where shared `script_constants` are not accepted in every field, direct comparison syntax is not accepted in the affected context, or a decision/overlay surface needed its visibility/cleanup contract aligned with the current Event 006 source design.

The changes fall into four classes:

1. File-scoped `@CR_SC_INDEPENDENCE_WAVE_*` mirrors are used in fields that reject `constant:` tokens, while the authoritative shared tuning remains in `common/script_constants/`.
2. Variable comparisons in affected decision and trigger contexts use `check_variable` with explicit comparison modes where the field cannot safely consume the previous expression.
3. Decision and overlay visibility/cleanup blocks are aligned with current package and carrier gates; this does not expand the admitted package set.
4. Player-facing Event 006 localization keys are kept in the same source change as the corresponding decision, event, focus, formable, scenario, and rival-bloc surfaces.

## Changed source surfaces at the inventory point

### Decisions and decision categories

- `common/decisions/006_independence_wave_brittany_decisions.txt`
- `common/decisions/006_independence_wave_catalonia_decisions.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/decisions/006_independence_wave_evolution_incident_decisions.txt`
- `common/decisions/006_independence_wave_form01_02_04_decisions.txt`
- `common/decisions/006_independence_wave_form03_decisions.txt`
- `common/decisions/006_independence_wave_form05_decisions.txt`
- `common/decisions/006_independence_wave_form48_decisions.txt`
- `common/decisions/006_independence_wave_ice_decisions.txt`
- `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`
- `common/decisions/006_independence_wave_iw093_iw098_decisions.txt`
- `common/decisions/006_independence_wave_mediterranean_decisions.txt`
- `common/decisions/006_independence_wave_montenegro_decisions.txt`
- `common/decisions/006_independence_wave_pacific_decisions.txt`
- `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt`
- `common/decisions/006_independence_wave_saar_decisions.txt`
- `common/decisions/006_independence_wave_scotland_wales_decisions.txt`
- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`
- `common/decisions/categories/006_independence_wave_categories.txt`
- `common/decisions/categories/006_independence_wave_form03_categories.txt`
- `common/decisions/categories/006_independence_wave_form05_categories.txt`
- `common/decisions/categories/006_independence_wave_ice_categories.txt`
- `common/decisions/categories/006_independence_wave_pacific_categories.txt`

### Scripted effects

- `common/scripted_effects/006_independence_wave_crisis_effects.txt`
- `common/scripted_effects/006_independence_wave_focus_effects.txt`
- `common/scripted_effects/006_independence_wave_force_effects.txt`
- `common/scripted_effects/006_independence_wave_form03_effects.txt`
- `common/scripted_effects/006_independence_wave_ice_package_effects.txt`
- `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt`
- `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt`
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt`
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`
- `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt`
- `common/scripted_effects/006_independence_wave_saar_package_effects.txt`
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
- `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt`

### Scripted triggers

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt`
- `common/scripted_triggers/006_independence_wave_form05_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw022_dalmatia_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw025_vojvodina_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw035_livonia_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw059_mesopotamia_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw085_cyrenaica_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw101_iw102_iw105_cog_overlays_triggers.txt`
- `common/scripted_triggers/006_independence_wave_iw156_iw196_iw197_iw204_overlays_triggers.txt`
- `common/scripted_triggers/006_independence_wave_rival_bloc_triggers.txt`

### Events

- `events/006_independence_wave.txt`
- `events/006_independence_wave_evolution_incidents.txt`
- `events/006_independence_wave_iw093_iw098.txt`

### Localization consumers

- `localisation/english/006_independence_wave_brittany_l_english.yml`
- `localisation/english/006_independence_wave_evolution_incidents_l_english.yml`
- `localisation/english/006_independence_wave_focus_l_english.yml`
- `localisation/english/006_independence_wave_form01_02_04_l_english.yml`
- `localisation/english/006_independence_wave_form03_l_english.yml`
- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `localisation/english/006_independence_wave_ice_l_english.yml`
- `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
- `localisation/english/006_independence_wave_iw043_iw058_events_l_english.yml`
- `localisation/english/006_independence_wave_iw043_iw058_focus_l_english.yml`
- `localisation/english/006_independence_wave_iw093_iw098_decisions_l_english.yml`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/006_independence_wave_pacific_l_english.yml`
- `localisation/english/006_independence_wave_rival_bloc_l_english.yml`
- `localisation/english/006_independence_wave_scenario_l_english.yml`
- `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`

## Validation performed and still required

The allocator, SCN-008 matrix, GUI semantic matrix, and protected-tag audits pass against the current source, but those checks do not validate every field in this tranche. Before this handoff can be promoted to implementation evidence, run targeted source checks for:

- every file-scoped mirror against its authoritative `common/script_constants/` value;
- each converted `check_variable` comparison and its expected scope/variable name;
- decision cost availability and cleanup after cancellation, expiry, host loss, and failed release;
- overlay visibility for ICE and the fail-closed package triggers;
- event option effects and evolution incident receipts;
- localization key coverage, duplicate keys, UTF-8 BOM, and wording alignment;
- the deleted or renamed vanilla-formable compatibility decision file, if it is part of this tranche, before any restoration or removal is considered.

No live Hearts of Iron IV launch, save/load test, MCP completion claim, or runtime package admission is implied by this inventory.

## Remaining risks

- The current worktree contains unrelated dirty changes from other events; this handoff intentionally enumerates only the Event 006 compatibility surfaces above.
- The exact author and commit boundary of the broad working-tree edits is not established here. Parent ownership must be confirmed with a staged diff before committing them.
- A source-level compatibility repair does not close package identity, territory, flag, leader-rights, formable, AI/balance, capacity, asset, or super-event gates.
- The generic focus assignment remains one shared Event 006 tree with ICE as the sole reviewed additive carrier; no additional carrier is admitted by these edits.

## Disposition

Keep this handoff as an inventory and validation queue. Do not cite it as a completion receipt until the targeted checks above are run and the parent has deliberately staged only the intended Event 006 changes.
