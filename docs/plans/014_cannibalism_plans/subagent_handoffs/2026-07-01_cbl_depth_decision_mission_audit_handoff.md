# Event 014 CBL Decision and Mission Audit Handoff

Date: 2026-07-01
Owner: decision and mission subagent
Scope: Event 014 Cannibalism decisions, missions, CBL costs, AI target validity, icons, localisation, cleanup, and docs listed in the parent prompt.

## Changed Files

- `common/decisions/014_cannibalism_decisions.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/events/014_cannibalism.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_cbl_depth_decision_mission_audit_handoff.md`

## Changed Identifiers

- `cannibalism_cbl_last_table_map_mission`
- `cannibalism_cbl_pact_courier_mission`
- `cannibalism_cbl_has_available_hunting_ground_state`
- `cannibalism_cbl_has_neighbor_target`
- `cannibalism_cbl_can_pay_region_project_cost`
- `cannibalism_cbl_apply_hunting_ground_to_controlled_state`
- `cannibalism_cbl_mark_neighbor_hunting_claim`
- `cannibalism_cbl_region_consumption_project_available_tt`
- `cannibalism_cbl_solitary_border_raid_available_tt`

## Issues By Severity

1. High, patched: `cannibalism_cbl_region_consumption_project` could repeatedly pay out manpower, infantry equipment, network strength, deaths, and project count even when all controlled states were already marked. It now requires an unmarked controlled state and only increments the hunting-ground project count when a fresh state is actually marked.
2. High, patched: `cannibalism_cbl_solitary_border_raid` could select broad non-commune neighbors and create repeat claims or war goals against poor targets. The target trigger and effect now require an adjacent unclaimed state, a living non-commune owner, no current war with ROOT, and vanilla `can_ROOT_get_wargoal_on_THIS`.
3. Medium, patched: `cannibalism_cbl_last_table_map_mission` and `cannibalism_cbl_pact_courier_mission` were success-on-available missions but used `is_good = yes`, which makes nonselectable mission tooltip polarity read as failure-oriented. Both now use `is_good = no`.
4. Low, patched: Last Table map docs and loc drifted from the actual constants and triggers. Docs and loc now state at least four controlled states and at least one hunting-ground project.
5. Low, remaining: The mission blocks still include `visible = { has_country_flag = ... }`. The offline wiki says mission `visible` is ignored; activation, cancel triggers, and cleanup already control lifecycle, so this was left as a broad cleanup item rather than a behavior patch.

## Category Lifecycle Notes

- `cannibalism_frontline_hunger_category` is visible through `cannibalism_response_visible`, which covers active outbreak countries and CBL while excluding `world_end`.
- `visible_when_empty = yes` is acceptable because the category is an event command surface and CBL route decisions appear after focus/flag gates.
- CBL global defeat cleanup clears route flags, active mission flags, ideas, state markers, hunting-ground modifiers, and removes active CBL missions with `remove_mission`.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `cannibalism_cbl_last_table_map_mission` | CBL | `cannibalism_frontline_hunger_category` | CBL controlled states | Active flag, CBL, map projection, at least four controlled states, at least one hunting-ground project, CBL route flag | 120 days | Clears active flag, validates map, adds `cannibalism_last_table_integration`, raises network | Clears active flag, stability and war support loss, deaths and cult node | Low after active flag, cancel, and cleanup paths |
| `cannibalism_cbl_pact_courier_mission` | CBL pact route | `cannibalism_frontline_hunger_category` | Coast or rail projection | Active flag, CBL, map projection | 75 days | Clears active flag, raises network and cult nodes, tries global table record | Clears active flag, stability loss, deaths | Low after active flag, cancel, and cleanup paths |
| Ordinary outbreak missions | Outbreak country | `cannibalism_frontline_hunger_category` | Country supply, controlled states, naval access | Active mission flags, outbreak stage flags, supplied divisions, control, naval access as appropriate | Varied by constants | Success and failure are separate scripted effects | Low; activation flags and cancel effects are present |

## Cost And Requirement Clarity Notes

- No scoped Event 014 decision surface uses a political power store. Static scan found no `political_power`, `add_political_power`, or numeric `cost =` in the scoped decision/effect/trigger/constants/localisation/docs set.
- CBL custom cost triggers are display gates only, and the corresponding complete effects manually spend concrete resources:
  - Last Table map: Command Power, Army XP, trains, convoys, fuel.
  - Region project: Command Power, support equipment, stability, war support.
  - Pact courier run: Command Power, train, convoys, fuel.
  - Solitary border raid: Army XP, infantry equipment, fuel.
- Localisation now exposes the fresh-state gate for region projects and the valid unclaimed target gate for solitary raids.

## AI Validity And Route-Lock Notes

- CBL decisions are route-locked by CBL flags: Last Table preparation, controlled region unlock, pact route, and table-for-one route.
- AI weights are present on the new CBL decisions and reuse existing script constants.
- `cannibalism_cbl_has_neighbor_target` now mirrors the actual state-neighbor selection used by the raid effect, which reduces AI attempts against dead, already-at-war, same-faction, subject, or already-claimed targets.

## Localisation And Tooltip Gaps

- Icon coverage exists for all new CBL decision icons in `interface/014_cannibalism.gfx`.
- Localisation coverage exists for all new CBL decision and mission ids.
- The localisation file remains UTF-8 with BOM after edits.
- Remaining low issue: mission `visible` blocks are inert for missions per the offline wiki, but their activation blocks and active flags still provide reveal behavior.

## Cleanup And Exploit-Risk Notes

- Active CBL mission cleanup is present in `cannibalism_cleanup_commune_country_pressure` for both active flags and active mission instances.
- Region project repeat farming was patched with the new unmarked controlled state trigger and effect guard.
- Solitary raid duplicate claim and unsafe target risk was patched with unclaimed adjacent-state and wargoal-valid target filters.
- No broad route redesign or balance rebasing was performed.

## Before And After Behavior

- Before: CBL map and pact courier missions could display incorrect nonselectable mission polarity. After: both success-on-available missions use `is_good = no`.
- Before: region projects could keep adding reward payloads and project count after all controlled states were already marked. After: region projects require an unmarked controlled state, and marking/count increment happen only when one exists.
- Before: solitary border raids could claim repeatedly or generate war goals against unsafe broad neighbor targets. After: the decision and effect require an unclaimed adjacent owner that is a valid wargoal target and not already at war.
- Before: docs and loc described older Last Table and target requirements. After: docs and loc match current constants and patched gates.

## Validation

- Consulted offline Paradox wiki decision, trigger, effect, localisation, data structure, modifier, scope, event, idea, AI, interface, and scripted GUI pages before editing.
- Consulted vanilla documentation for mission activation/removal, active mission trigger, equipment/fuel/manpower/stability/war support/command power effects, script constants, and wargoal target precedent.
- Checked vanilla precedents for custom costs with manual spending and nonselectable mission activation/cancel/timeout patterns.
- Static scan confirmed no political power store or numeric PP decision costs in scoped Event 014 decision, effect, trigger, constants, localisation, or docs files.
- Static scan confirmed new CBL decision and mission ids have decision, icon, localisation, and docs coverage.
- Static scan confirmed CBL active mission flags have activation, cancel, success/failure clearing, and global defeat `remove_mission` cleanup.
- Static scan found no unsupported `<=` or `>=` operators in scoped script files.
- Verified `localisation/english/014_cannibalism_l_english.yml` still has UTF-8 BOM after localisation edits.

## Skipped Validation

- Did not run the HOI4 executable or live parser. This subagent run was limited to repo-static validation and vanilla/offline documentation checks.
- Did not commit because the Event 014 package and related parent worktree files are already dirty and untracked; the parent should review and commit the full completed plan scope.

## Remaining Risks

- Existing mission `visible` blocks are inert for missions; they can be removed in a later cleanup pass if desired, but they are not currently the lifecycle mechanism.
- `days_mission_timeout = constant:...` is used consistently in this Event 014 decision file. I left it unchanged because replacing every mission duration field would be a broader parser-compatibility pass.
