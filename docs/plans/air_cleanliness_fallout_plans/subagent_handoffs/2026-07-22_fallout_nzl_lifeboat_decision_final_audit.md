# Fallout NZL Lifeboat decision final audit

Date: 2026-07-22

Scope: the dormant NZL Lifeboat category, its 18 decisions and missions, direct cost localisation, focus reveal receipts, and directly consumed NZL helpers.

Status: narrow lifecycle, target-safety, and cost-clarity patch complete. The package remains dormant and no activation caller was added.

## Changed files

- `common/decisions/categories/fallout_nzl_lifeboat_categories.txt`
  - `fallout_nzl_lifeboat_category` now uses the static `original_tag = NZL` allowed gate and retains the current-package visible gate.
- `common/decisions/fallout_nzl_lifeboat_decisions.txt`
  - Added package-current activation gates to all seven selectable missions.
  - Added missing state or live-requirement checks to six custom-cost triggers.
  - `fallout_nzl_rebuild_partner_relief_port` cancels if the exact partner becomes hostile during the project.
- `localisation/english/fallout_nzl_lifeboat_l_english.yml`
  - Corrected the dairy convoy and partner-port cost displays to use the registered motorized and support-equipment text icons.

## Before and after behavior

The category previously used `fallout_nzl_lifeboat_package_is_current` inside `allowed`. Decision `allowed` is checked only at startup or reload, while this package is deliberately dormant at startup. A valid later activation would therefore leave the category permanently unavailable. The category now has a static NZL ownership gate and remains hidden until the exact current-generation package receipt is valid.

The seven mission activations previously depended only on focus or transaction flags. They now also require `fallout_nzl_lifeboat_package_is_current`, so stale flags cannot activate a mission after the package fails closed.

The partner-port project now cancels instead of granting a naval base to a relief partner that enters a war with NZL before project completion. Its existing cancellation cleanup still clears the global port target and the external-project lock.

The breakwater, Auckland, milk-rail, weather-chain, rescue-passage, and forced-settlement cost displays now turn blocked when their actual state, food, or exact-pirate gate is unmet. The two modified cost groups show equipment icons rather than plain localisation names.

## Changed identifiers and localisation keys

Category:

- `fallout_nzl_lifeboat_category`

Mission activation gates:

- `fallout_nzl_wellington_breakwater_works`
- `fallout_nzl_auckland_storm_port_works`
- `fallout_nzl_milk_rail_assignments`
- `fallout_nzl_port_militia_training_mission`
- `fallout_nzl_convoy_volunteer_corps_mission`
- `fallout_nzl_refugee_fleet_admission`
- `fallout_nzl_offer_rescue_passage`

Cost and target-safety decisions:

- `fallout_nzl_wellington_breakwater_works`
- `fallout_nzl_auckland_storm_port_works`
- `fallout_nzl_milk_rail_assignments`
- `fallout_nzl_weather_station_chain`
- `fallout_nzl_offer_rescue_passage`
- `fallout_nzl_anti_piracy_bearing`
- `fallout_nzl_rebuild_partner_relief_port`

Localisation keys:

- `fallout_nzl_cost_dairy_relief_convoy`
- `fallout_nzl_cost_dairy_relief_convoy_blocked`
- `fallout_nzl_cost_dairy_relief_convoy_tooltip`
- `fallout_nzl_cost_partner_relief_port`
- `fallout_nzl_cost_partner_relief_port_blocked`
- `fallout_nzl_cost_partner_relief_port_tooltip`

## Issue list

1. Critical, fixed. The category had a runtime activation trigger in its one-time `allowed` block. A dormant package could never reveal the category when a future approved caller activates it.
2. Medium, fixed. Seven selectable missions could activate from stale unlock flags because mission activation lacked the generation-bound package trigger.
3. Medium, fixed. A partner-port rebuild could finish after the target became an enemy, granting it a naval base.
4. Medium, fixed. Six custom-cost displays could remain normal while an actual map, value, or exact-target requirement blocked the action. Two cost groups also did not use the project icon-first convention.
5. Medium, remaining. Cost strings reproduce the present script-constant values as literal localisation numbers. A future constants retune needs a paired localisation review or a bounded scripted-localisation cost system. This audit does not introduce that broader presentation system.
6. External blocker. Fallout standard-release blockers still prevent an activation caller. This patch must not and does not bypass the allocator, assignment, conflict-disposition, or scheduler receipts.

## Category lifecycle notes

`fallout_nzl_lifeboat_category` is NZL-only at startup and visible only when `fallout_nzl_lifeboat_package_is_current` passes. It may render empty so the four bounded values remain legible. Focus completion flags reveal actions in phases. The central `fallout_nzl_reset_package_runtime` effect clears category unlock flags, active-project flags, reciprocal guarantees, global event targets, value variables, and generation receipts on package reset.

There is no decision-owned scripted GUI. GUI inspection and rendering are not applicable.

## Mission quality notes

| Mission | Owner and category | Region and requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| `fallout_nzl_wellington_breakwater_works` | NZL, Lifeboat Ledger | Wellington 284, convoys, trucks | 70 days | Naval base and Harbor Capacity | Package or state loss, trust loss | One-shot completion flag |
| `fallout_nzl_auckland_storm_port_works` | NZL, Lifeboat Ledger | Auckland 1079, support equipment, manpower | 105 days | Naval base, dockyard, Harbor Capacity | Package or state loss, harbor loss | One-shot completion flag |
| `fallout_nzl_milk_rail_assignments` | NZL, Lifeboat Ledger | South Island 723, trucks, trains | 70 days | Food Security gain | Package or state loss, spoiled stores | One-shot completion flag |
| `fallout_nzl_port_militia_training_mission` | NZL, Lifeboat Ledger | National port militia, rifles, manpower, Army XP | 70 days | Army XP and Sea-Lane Security | Package loss marks major failure | One-shot completion flag |
| `fallout_nzl_convoy_volunteer_corps_mission` | NZL, Lifeboat Ledger | Auckland 1079, support equipment, convoys, manpower | 105 days | One guarded escort formation | Package or state loss marks major failure | Explicit formation receipt and one-shot mission |
| `fallout_nzl_refugee_fleet_admission` | NZL, Lifeboat Ledger | Harbor and Food above Strained | 70 days | Manpower and Parliament Trust | Package loss clears external lock and marks failure | One-shot completion flag |
| `fallout_nzl_offer_rescue_passage` | NZL, Lifeboat Ledger | Exact current external transaction, convoys, Food above Stable | 105 days | Relief-partner receipt and Parliament Trust | Package or transaction loss clears transaction and marks failure | One-shot completion flag |

All seven missions are selectable objectives with costs, duration, successful timeout effects, cancellation cleanup, and no passive checklist completion. Their durations use the shared 70 and 105 day bands.

## Ordinary decision quality notes

| Decision | Reveal and requirement | Lifecycle and result | Exploit and target result |
| --- | --- | --- | --- |
| `fallout_nzl_fishery_quota_compact` | Dairy route, manpower, Sea-Lane Security above Critical | 35 days, 90 day cooldown, Food gain for Sea-Lane loss | Repeatable but resource and security bounded |
| `fallout_nzl_weather_station_chain` | Radio-weather route, Auckland 1079, Command Power | 35 days, 90 day cooldown, temporary weather receipt and Sea-Lane gain | No stack because the warning duration and cooldown match |
| `fallout_nzl_arm_rescue_cutters_action` | Rescue-cutter focus, convoys, Navy XP | 70 day one-shot, Harbor loss then major Sea-Lane gain | No unit or stockpile reward |
| `fallout_nzl_last_berth_closure` | Isolation route, trust above Critical, Political Power | 35 day one-shot, immediate trust loss then food and Sea-Lane gains | Route-lock effect is recorded for achievements |
| `fallout_nzl_anti_piracy_bearing` | Current recorded pirate war and 65 percent surrender threshold | Immediate one-shot Command Power action, white peace and settlement receipt | Cannot select an unrelated or dead country |
| `fallout_nzl_mobilize_home_guard_state` | Home Guard focus, one exact controlled package state, rifles, manpower, Army XP | 70 days, one active state project, bunker and Sea-Lane gain | Per-state generation receipt prevents bunker repetition |
| `fallout_nzl_dispatch_dairy_relief_convoy` | Dairy fleet, convoys, trucks, Harbor above Critical | 70 day one-shot, Food and Trust gains | Transport is consumed and no resource is returned |
| `fallout_nzl_rebuild_partner_relief_port` | Humanitarian postwar focus, exact coastal relief partner, convoys, support equipment, trust | 105 days, one external project, target naval base and receipts | One partner receipt per generation and new hostility cancellation |
| `fallout_nzl_guarantee_relief_partner` | Humanitarian postwar focus, one exact unguaranteed relief partner | Immediate one-partner guarantee, reciprocal receipt | Annexation and package reset clear the guarantee state |
| `fallout_nzl_revoke_raider_access` | Isolation quiet-seas focus, exact recorded aggressor, Command Power, trust | Immediate one-use access revocation in both directions | Cannot affect a generic target or repeat after the receipt flag |
| `fallout_nzl_quiet_seas_patrol` | Isolation quiet-seas focus, access revoked, current pirate war, convoys, Navy XP | 70 day one-shot, Sea-Lane gain or cancellation trust loss | Current-war and settlement checks close the action |

## Cost and requirement clarity

The package avoids a political-power storefront. It uses convoys, trucks, trains, support equipment, rifles, manpower, Army XP, Navy XP, Command Power, temporary civilian-factory use, visible value thresholds, exact state control, and exact partner receipts.

Repeatable actions remain bounded:

- Fishery compact spends Political Power and manpower, reduces Sea-Lane Security, and uses a cooldown.
- Weather chain spends Command Power, has a timed warning, and uses a cooldown.
- Home Guard is one active project at a time and once per listed state per Fallout generation.
- Partner-port relief is once per exact partner per generation.
- Relief guarantee is one live recorded partner.

## AI validity and route-lock notes

All 18 decision or mission `ai_will_do` blocks are gated by the same current-package, focus, route, target, or value conditions that control player visibility and availability. The two country-target actions use `target_root_trigger` plus generation-aware relief-partner receipts. The pirate actions operate only on the stored aggressor and current pirate-war receipt. The Home Guard target list is limited to states 284, 1079, 723, 1080, and 1081.

Focus integration is complete for every unlock flag consumed by this category. Each of the 16 focus reveal flags has one decision or mission consumer. `fallout_nzl_anti_piracy_decision_open` is also refreshed only by the exact pirate-war helper. No action can target a dead, stale, unrelated, route-closed, or already-receipted partner.

## Localisation and tooltip notes

All 18 decision titles and descriptions resolve. All 15 custom-cost keys have base, blocked, and tooltip variants. The localisation file remains UTF-8 with BOM. All 18 decision sprites and the category sprite are registered in `interface/fallout_world_end.gfx`.

## Cleanup and exploit-risk notes

The central reset effect clears every decision unlock and active-project flag used here, removes the recorded guarantee from NZL scope, clears global partner and port targets, and deletes generation-bearing values. Annexation clears an active guarantee receipt. Timed actions have cancellation paths for package invalidation, relevant state loss, transaction invalidation, pirate-war settlement, or the newly added partner hostility case.

No exploit loop was found. The only unit-creating mission is receipt-guarded, costs support equipment, convoys, and manpower, is one-shot, and sets a duplication-detection flag if a second grant is attempted. The package has no repeating free equipment, core, claim, war-goal, factory, or unit action.

## Validation evidence

- Read the required repository guidance, decision and focus skills, offline decision, scope, effect, trigger, localisation, modifier, data-structure, AI, on-action, event, and idea references, plus vanilla decision and script-constant documentation and NZL decision precedents.
- Static package scan found exactly 18 decision or mission identifiers, no missing title or description keys, no missing custom-cost variants, no missing registered decision or category sprites, and no selectable mission activation lacking the current-package gate.
- Searched all `.txt` gameplay files and found no caller for `fallout_nzl_activate_lifeboat_package` outside its own dormant helper definition.
- The read-only map inspection passed for states 284, 723, 1079, 1080, and 1081. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37ce3502c1e75d73230afaaeca460fe552e047c7769e1bfea1ce06a0ab0c5e9a/bd1264737f5d23cbdfd07b47d9406d014b837004caeff9a4c1ba9a589f803323/map-inspect.d10a5ab8359ad723.json`.

## Skipped validation

No HOI4 launch or in-game scenario was run, as instructed. No scripted GUI exists in the decision surface. The broader Fallout release and activation path remains outside this scope.

## Remaining blockers and follow-up

- The package is intentionally dormant. A parent-owned caller may be added only after the standard Fallout release blockers and all required current-generation receipts are proven.
- Treat this handoff as superseding the category-lifecycle conclusion in `fallout_nzl_lifeboat_decision_audit_2026-07-19.md`. The previous conclusion did not account for decision `allowed` being evaluated before a dormant package can be activated.
- No separate plan handoff was needed. The remaining localisation synchronization concern is a bounded future presentation improvement, not a decision-system redesign.
