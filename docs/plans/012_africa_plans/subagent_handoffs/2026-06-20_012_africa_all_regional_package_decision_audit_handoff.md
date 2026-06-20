# Event 012 All Regional Package Decision Audit Handoff

Date: 2026-06-20
Scope: audit-only handoff for the all-ten regional authority package action tranche. No gameplay files were edited and no commit was made.

## Summary

No blocking gameplay or syntax issue remains in the ten-action regional authority package tranche. All ten package actions exist, are targeted decisions under the Charter diplomacy category, require the active runtime unifier and `africa_regional_authorities_open`, target the intended regional authority tag, require `can_africa_target_regional_package_action_for_root`, require the matching companion authority-tree capstone flag, are one-time through target flags, spend concrete resources through `custom_cost_trigger` plus scripted effects, transfer material/forces/buildings to the target, move visible Africa values, increment `africa_regional_package_action_count`, and fire visible local reports `chaosx.nr12.55` through `chaosx.nr12.64`.

Two non-blocking parent fixes are recommended:

1. Add `_tooltip` localisation keys for the ten `africa_regional_package_*_cost_tt` custom costs.
2. Consider adding an `available` revalidation block to each package decision so target validity is checked every tick, not only by daily `target_trigger`.

## Files Inspected

- `AGENTS.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- Vanilla decision precedents in `~/projects/Hearts of Iron IV/common/decisions/SOV.txt`, `PHI.txt`, `_generic_decisions.txt`, and `AST.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/script_constants/012_africa_constants.txt`
- `common/national_focus/012_africa_focus.txt`
- `common/national_focus/012_africa_authority_focus.txt`
- `events/012_african_union.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`

## Pass/Fail Findings

### Pass: decision and target lifecycle

- All ten decision ids are present in `common/decisions/012_africa_decisions.txt`: WAC at lines 776-818, SAH 820-864, IOC 866-909, MAG 911-954, NHR 956-998, EAC 1000-1043, GLK 1045-1087, CBC 1089-1132, ZSC 1134-1177, and SLC 1179-1222.
- Each decision has `target_array = global.africa_charter_member_countries`, `target_root_trigger` with `is_africa_runtime_unifier = yes` and `has_country_flag = africa_regional_authorities_open`, and a tag-specific `target_trigger`.
- Each `target_trigger` requires the matching tag and one-time target flag, plus `can_africa_target_regional_package_action_for_root = yes`: WAC lines 791-795, SAH 835-839, IOC 881-885, MAG 926-930, NHR 971-975, EAC 1015-1019, GLK 1060-1064, CBC 1104-1108, ZSC 1149-1153, and SLC 1194-1198.
- `can_africa_target_regional_package_action_for_root` requires the target to exist, be a regional authority subject, have mandate success, not be former/resistant, not have capitulated, not be at war with root, and control its capital in `common/scripted_triggers/012_africa_triggers.txt` lines 428-437.
- The matching authority focus capstone flags are set in `common/national_focus/012_africa_authority_focus.txt`: WAC lines 425-450, SAH 454-480, MAG 484-512, NHR 517-542, EAC 547-575, GLK 580-601, CBC 606-631, ZSC 636-659, SLC 664-689, and IOC 694-723.

### Pass: costs and effects are concrete

- The package costs use political power plus concrete resource gates in `custom_cost_trigger`, not flat PP-only purchases. Constants are centralised in `common/script_constants/012_africa_constants.txt` lines 752-757 and 897-904.
- The complete effects spend resources and transfer rewards through helper effects in `common/scripted_effects/012_africa_effects.txt`: WAC lines 1606-1630, SAH 1632-1657, IOC 1659-1684, MAG 1686-1712, NHR 1714-1736, EAC 1738-1764, GLK 1766-1786, CBC 1788-1815, ZSC 1817-1843, and SLC 1845-1870.
- Each helper increments `africa_regional_package_action_count`, sets `africa_has_regional_package_action`, adjusts visible Africa values, calls `africa_clamp_core_values`, and fires its report event.

### Pass: counter goal alignment

- The required package-action goal is `regional_package_actions = 10` in `common/script_constants/012_africa_constants.txt` lines 1220-1230.
- The global display target is initialised from that constant at `common/scripted_effects/012_africa_effects.txt` line 5901.
- The unifier package counter starts at `0` in `common/scripted_effects/012_africa_effects.txt` line 1141 and is incremented once by each of the ten helper effects.
- The Charter diplomacy header exposes `africa_regional_package_action_count` against `global.africa_mission_required_regional_package_actions` in `localisation/english/012_african_union_l_english.yml` line 657.

### Pass: reports and event target usage

- `events/012_african_union.txt` defines all ten local report events: `chaosx.nr12.55` lines 718-729, `.56` 731-742, `.57` 744-755, `.58` 757-768, `.59` 770-781, `.60` 783-794, `.61` 796-807, `.62` 809-820, `.63` 822-833, and `.64` 835-846.
- The helper effects save regular event target `africa_regional_package_target` before firing the report, for example WAC at `common/scripted_effects/012_africa_effects.txt` lines 1614-1629 and the same pattern through SLC lines 1852-1869.
- The report localisation reads `[africa_regional_package_target.GetName]` in `localisation/english/012_african_union_l_english.yml` lines 107-136. This matches HOI4 regular event-target localisation behavior: no `event_target:` prefix is used in localisation.

### Pass: one-time and cleanup behavior

- The ten one-time target flags are set in the corresponding helper effects at `common/scripted_effects/012_africa_effects.txt` lines 1616, 1644, 1670, 1697, 1722, 1749, 1774, 1799, 1828, and 1854.
- The same flags are cleared by the broader runtime cleanup/reset helper at `common/scripted_effects/012_africa_effects.txt` lines 958-967 and 1004-1013. This is appropriate for runtime reset cleanup and does not create repeat-click risk during normal play because target triggers block already-used targets.

### Pass: AI route-lock validity

- Every package action has an `ai_will_do` block at `common/decisions/012_africa_decisions.txt` lines 813-817, 859-863, 904-908, 949-953, 993-997, 1038-1042, 1082-1086, 1127-1131, 1172-1176, and 1217-1221.
- Direct searches found the AI-weight flags in current Event 012 surfaces rather than dead flags: examples include `africa_liberation_war_office_open`, `africa_authority_atlas_open`, `africa_integration_temperature_board_open`, dossier lane flags, route flags, origin profile flags, `africa_continent_sponsor_ready`, and `africa_rsa_civil_war_active`.
- Target validity is handled by the tag-specific target trigger plus `can_africa_target_regional_package_action_for_root`, so AI cannot normally select dead, capitulated, former/resistant, hostile, or capital-lost targets after the target list refreshes.

### Medium: target validity is daily-only, not repeated in `available`

- The ten package decisions have `target_trigger` blocks but no `available` blocks in `common/decisions/012_africa_decisions.txt` lines 776-1222.
- Offline wiki decision documentation says `target_trigger` is checked daily, while `available` is checked every tick and can also read `FROM` for targeted decisions. This means a target that capitulates, enters war with root, loses capital control, or otherwise stops matching `can_africa_target_regional_package_action_for_root` can remain clickable until the next daily target refresh if the player acts in that short window.
- Recommended parent fix: add an `available = { FROM = { ... } }` block to each decision repeating its tag, package trigger, capstone, one-time flag, and `can_africa_target_regional_package_action_for_root` checks. This is a safety revalidation, not a redesign.

### Low: custom cost hover tooltip keys are missing

- The ten package custom cost keys have base and `_blocked` localisation in `localisation/english/012_african_union_l_english.yml` lines 1021-1067.
- Direct search found zero matching `_tooltip` keys for `africa_regional_package_wac_cost_tt_tooltip`, `..._sah_...`, `..._ioc_...`, `..._mag_...`, `..._nhr_...`, `..._eac_...`, `..._glk_...`, `..._cbc_...`, `..._zsc_...`, and `..._slc_...`.
- Offline wiki decision documentation says `custom_cost_text = <key>` uses `<key>_tooltip` when hovering over the cost. Existing nearby Event 012 custom costs do provide `_tooltip` keys, for example lines 940, 946, 994, 1000, 1006, and 1014.
- Recommended parent fix: add concise hover text for all ten regional package cost keys.

### Low/watch: archetype gate versus base-equipment spend is intentional-looking but worth parent confirmation

- SAH gates `motorized_equipment` at `common/decisions/012_africa_decisions.txt` line 849 and spends `motorized_equipment_1` in `common/scripted_effects/012_africa_effects.txt` line 1640.
- MAG and EAC gate `train_equipment` at `common/decisions/012_africa_decisions.txt` lines 940 and 1029 and spend `train_equipment_1` in `common/scripted_effects/012_africa_effects.txt` lines 1694 and 1746.
- Vanilla has precedents for both archetype gates and archetype/type stockpile effects, including `SOV.txt` lines 11035 and 11059-11061, `PHI.txt` lines 2368-2376 and 2398-2406, and `_generic_decisions.txt` lines 273-295. Existing Event 012 uses the same gate/spend pattern outside this tranche.
- I do not consider this a blocker. Parent may still prefer matching the effect `type` to the gated archetype for broader variant compatibility.

## Decision Category Lifecycle Notes

- Owner: active Event 012 unifier.
- Category: `africa_charter_league_diplomacy_category`.
- Visibility: category visible while the Event 012 decision layer is visible; package actions additionally require runtime unifier and `africa_regional_authorities_open`.
- Target lifecycle: targets come from `global.africa_charter_member_countries`, are filtered to the matching tag and successful regional authority mandate/capstone state, and are removed by one-time target flags after completion.
- Runtime cleanup: one-time package flags are covered by the broader Event 012 runtime cleanup/reset helper.
- No separate cooldown exploit was found: each action has `days_re_enable = constant:africa_decision_days.regional_authority_mandate`, but the one-time target flag is the real repeat blocker.

## Mission Quality Notes

These ten tranche items are clickable package actions, not timed missions. They do not need success/failure mission branches because their gameplay is an immediate post-mandate support package gated by successful regional authority work and companion-tree capstone completion.

| Action | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_convene_wac_port_congress` | Unifier | Charter diplomacy | WAC | WAC subject, mandate success, Port Union capstone, capital control, one-time flag clear | `days_re_enable = regional_authority_mandate` | Support/convoys/infrastructure, values, report `.55` | None; click gated | Low |
| `africa_open_sah_caravan_columns` | Unifier | Charter diplomacy | SAH | SAH subject, mandate success, Oasis Routes capstone, capital control, one-time flag clear | Same | Manpower/rifles/trucks/guard, values, report `.56` | None; click gated | Low |
| `africa_secure_ioc_sea_lanes` | Unifier | Charter diplomacy | IOC | IOC subject, mandate success, Monsoon Passages capstone, capital control, one-time flag clear | Same | Support/convoys/dockyard, values, report `.57` | None; click gated | Low |
| `africa_reopen_mag_harbor_dockets` | Unifier | Charter diplomacy | MAG | MAG subject, mandate success, Harbor Compact capstone, capital control, one-time flag clear | Same | Convoys/trains/dockyard, values, report `.58` | None; click gated | Low |
| `africa_chart_nhr_highland_warrants` | Unifier | Charter diplomacy | NHR | NHR subject, mandate success, Highland Survey capstone, capital control, one-time flag clear | Same | Support/infrastructure, values, report `.59` | None; click gated | Low |
| `africa_lock_eac_railway_timetable` | Unifier | Charter diplomacy | EAC | EAC subject, mandate success, Railway Board capstone, capital control, one-time flag clear | Same | Support/trains/infrastructure, values, report `.60` | None; click gated | Low |
| `africa_muster_glk_lake_guards` | Unifier | Charter diplomacy | GLK | GLK subject, mandate success, Lake Muster capstone, capital control, one-time flag clear | Same | Manpower/rifles/guard, values, report `.61` | None; click gated | Low |
| `africa_arm_cbc_river_quartermasters` | Unifier | Charter diplomacy | CBC | CBC subject, mandate success, River Quartermasters capstone, capital control, one-time flag clear | Same | Manpower/support/convoys/infrastructure, values, report `.62` | None; click gated | Low |
| `africa_open_zsc_stone_city_yards` | Unifier | Charter diplomacy | ZSC | ZSC subject, mandate success, Stone-City Yards capstone, capital control, one-time flag clear | Same | Support/rifles/civ factory, values, report `.63` | None; click gated | Low |
| `africa_secure_slc_mine_port_belt` | Unifier | Charter diplomacy | SLC | SLC subject, mandate success, Mine-Port Liberation capstone, capital control, one-time flag clear | Same | Manpower/rifles/guard/mil factory, values, report `.64` | None; click gated | Low |

## Cost and Requirement Clarity Notes

- Cost values match the script constants and helper spends: PP 25, command power 8 where present, army XP 5 where present, support equipment 90, convoys 6, trains 2, motorized 35, infantry equipment 160, and manpower 1,200.
- Root requirement text is generic but acceptable: every target tooltip names the matching authority, mandate success, capstone, loyalty, capital control, and one-time condition.
- The only clarity gap is missing `_tooltip` cost hover localisation for the ten package cost keys.

## AI Validity and Route-Lock Notes

- No dead AI-weight flags were found in the package `ai_will_do` blocks.
- The route and focus integration is real: `africa_regional_authorities_open` is set by `AFR_regional_authority_charters` in `common/national_focus/012_africa_focus.txt` lines 247-266, and each capstone flag is set by the matching authority focus.
- AI target safety relies on daily target filtering. Add per-tick `available` revalidation if parent wants same-day invalid-target protection.

## Localisation and Tooltip Gaps

- Decision titles and descriptions exist for all ten package actions in `localisation/english/012_african_union_l_english.yml` lines 711-730.
- Report titles, descriptions, and option text exist for `chaosx.nr12.55` through `.64` in lines 107-136.
- Root, target, cost base, blocked cost, and effect tooltip keys exist in lines 1019-1068.
- Missing: ten cost hover `_tooltip` keys for the `custom_cost_text` entries.

## Cleanup and Exploit-Risk Notes

- One-time target flags prevent repeat clicks per authority.
- The package counter goal is exactly ten and there are exactly ten incrementing helper effects.
- No free reward loop was found through normal decision visibility.
- Residual exploit/safety risk is limited to daily target refresh: a target can become invalid between target-refresh ticks unless parent adds `available` revalidation.
- Regular event target `africa_regional_package_target` is not global and does not need explicit cleanup.

## Recommended Parent Fixes

1. `localisation/english/012_african_union_l_english.yml`: add `_tooltip` keys for:
   - `africa_regional_package_wac_cost_tt_tooltip`
   - `africa_regional_package_sah_cost_tt_tooltip`
   - `africa_regional_package_ioc_cost_tt_tooltip`
   - `africa_regional_package_mag_cost_tt_tooltip`
   - `africa_regional_package_nhr_cost_tt_tooltip`
   - `africa_regional_package_eac_cost_tt_tooltip`
   - `africa_regional_package_glk_cost_tt_tooltip`
   - `africa_regional_package_cbc_cost_tt_tooltip`
   - `africa_regional_package_zsc_cost_tt_tooltip`
   - `africa_regional_package_slc_cost_tt_tooltip`
2. `common/decisions/012_africa_decisions.txt`: add same-tick `available` revalidation to each package action, repeating the existing target checks inside `FROM = { ... }`.
3. Optional: confirm whether SAH/MAG/EAC should continue spending base `motorized_equipment_1` / `train_equipment_1` while gating on archetypes, or whether parent prefers matching the spend `type` to the gated archetype for broader stockpile compatibility.

## Validation Commands and Results

- `rg` count for the ten package decision ids in `common/decisions/012_africa_decisions.txt`: `10`.
- `rg` count for the ten helper definitions in `common/scripted_effects/012_africa_effects.txt`: `10`.
- `rg` count for report events `chaosx.nr12.55` through `.64` in `events/012_african_union.txt`: `10`.
- `rg` count for report title localisation keys `.55.t` through `.64.t`: `10`.
- `rg` count for matching authority focus capstone flag setters in `common/national_focus/012_africa_authority_focus.txt`: `10`.
- `rg` count for one-time package flag clears in the runtime cleanup window: `10`.
- `rg` count for package cost `_tooltip` localisation keys: `0`; base and `_blocked` cost keys: `20`.
- Static tranche scan found `10` `target_root_trigger` blocks, `10` `target_trigger` blocks, and `0` `available` blocks in the ten package action window.
- `git diff --check --` on the scoped Event 012 files returned no whitespace errors.

## Residual Risk

- This was a static audit only. I did not run HOI4, reload the mod, or validate live UI behavior.
- Parent is actively editing and validating the same files locally; line numbers may shift after this handoff.
- No full Event 012 completion claim is made here.
