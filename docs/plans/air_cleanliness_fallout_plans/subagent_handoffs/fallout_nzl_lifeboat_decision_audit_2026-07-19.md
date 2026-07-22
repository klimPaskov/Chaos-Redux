# Fallout NZL Lifeboat decisions: audit and narrow patch handoff

## Scope and outcome

Owner: decision and mission audit subagent.

Changed files:

- `common/decisions/fallout_nzl_lifeboat_decisions.txt`
- `localisation/english/fallout_nzl_lifeboat_l_english.yml`

The category file was inspected but needs no edit: its `allowed` and `visible`
conditions already fail closed on `fallout_nzl_lifeboat_package_is_current`.

The patch consumes all four previously orphaned focus unlock flags and corrects
the lifecycle gate on every ordinary existing decision. The dormant package is
still not activated by this patch.

## Changed decision identifiers and behavior

| Identifier | Route and target | Cost and lifecycle | Result and bounds |
| --- | --- | --- | --- |
| `fallout_nzl_mobilize_home_guard_state` | Home Guard Rolls; only controlled states 284, 1079, 723, 1080, and 1081 | 120 infantry equipment, 350 manpower, 10 Army XP; 70 days; only one in flight | One bunker and +4 Sea-Lane Security. Each state records the current generation, so it cannot be mobilized twice in that generation. Loss of the package or state cancels it, clears the in-flight lock, and loses 4 Parliament Trust. |
| `fallout_nzl_dispatch_dairy_relief_convoy` | Dairy Relief Fleet; hidden after the Two-Island Supply Ring | 5 convoys and 30 trucks; 70 days; 90-day cooldown | +7 Food Security and +4 Parliament Trust. Every use consumes transport capacity; no unit, equipment, or value loop exists. Package loss cancels it with -4 Parliament Trust. |
| `fallout_nzl_rebuild_partner_relief_port` | Humanitarian route and Relief Ports Without Annexation; exact current relief partner | 10 convoys and 70 support equipment; 105 days | One partner per generation receives 35 support equipment plus a receipt. NZL gains +4 Sea-Lane Security and +4 Parliament Trust. It cancels if the package or exact partner receipt becomes invalid, with no refund and -4 Trust. No claim, core, country transfer, or generic target search is used. |
| `fallout_nzl_guarantee_relief_partner` | Humanitarian route and Relief Ports Without Annexation; exact current unguaranteed relief partner | 5 convoys and 12 Command Power; immediate | Grants NZL's guarantee, records the target and current generation on NZL, and writes the reciprocal partner receipt. The central reset must revoke this relation in NZL scope; see Cleanup handoff. |
| `fallout_nzl_revoke_raider_access` | Isolation route and Demand Quiet Seas; exact current pirate aggressor | 12 Command Power; immediate | Removes military access and docking rights in both directions only for the stored aggressor, then gives +4 Sea-Lane Security and -4 Parliament Trust. The action is one use per package through its reset-managed flag. |
| `fallout_nzl_quiet_seas_patrol` | Isolation route and Demand Quiet Seas; exact current pirate war after access is revoked | 5 convoys and 12 Navy XP; 70 days; 90-day cooldown | +7 Sea-Lane Security. It cancels on package loss, an invalid pirate war, or settlement and cannot create war goals, units, equipment, cores, or repeatable free rewards. |

All new cost localisation IDs have base, `_blocked`, and `_tooltip` variants.

## Lifecycle correction for existing actions

`activation` is mission-only. These five ordinary decisions were using it and
could therefore survive their intended focus route gates:

- `fallout_nzl_fishery_quota_compact`
- `fallout_nzl_weather_station_chain`
- `fallout_nzl_arm_rescue_cutters_action`
- `fallout_nzl_last_berth_closure`
- `fallout_nzl_anti_piracy_bearing`

They now use package-bound `visible` blocks. Package-invalid cancellation was
also added to the four timed ordinary actions. `fallout_nzl_weather_station_chain`
also cancels if Auckland is lost. `fallout_nzl_offer_rescue_passage` now has an
explicit package-invalid cancellation branch in addition to its exact external
transaction check.

Mission surfaces remain mission surfaces and retain `activation`:
`fallout_nzl_wellington_breakwater_works`,
`fallout_nzl_auckland_storm_port_works`,
`fallout_nzl_milk_rail_assignments`,
`fallout_nzl_port_militia_training_mission`,
`fallout_nzl_convoy_volunteer_corps_mission`,
`fallout_nzl_refugee_fleet_admission`, and
`fallout_nzl_offer_rescue_passage`.

## Issue list, sorted by severity

1. **Critical, fixed:** five normal decisions used mission-only `activation`.
   Their route condition was not a correct live visibility gate.
2. **High, fixed:** `fallout_nzl_home_guard_decision_open`,
   `fallout_nzl_dairy_convoy_decisions_open`,
   `fallout_nzl_postwar_relief_decisions_open`, and
   `fallout_nzl_quiet_seas_decisions_open` had no decision consumer.
3. **High, fixed:** a relief guarantee would otherwise be permanent after
   package invalidation. The patch records one exact partner and generation,
   and the chain architect merged the precise central package-reset teardown.
4. **High, fixed:** the rescue-passage mission cancelled only on its external
   transaction receipt. It now explicitly cancels when the package becomes
   invalid as well.
5. **Medium, remaining:** existing custom-cost strings for the nine older
   custom-cost actions do not have `_blocked` or `_tooltip` variants and are
   prose rather than icon-first cost displays. This audit leaves them intact to
   avoid an unrelated localisation rewrite; the six new actions are complete.
6. **Medium, remaining:** `fallout_nzl_weather_warning_current` is set when
   the weather action ends but has no expiry/consumer in this decision surface.
   It should be audited with the owner of weather-chain effects before it is
   made mechanically meaningful.
7. **Medium, outside decision scope:** the whole NZL pilot remains dormant
   until the allocator and conflict ledger call its existing package activation
   path. No decision patch attempts to bypass that architecture.

## Decision category lifecycle notes

`fallout_nzl_lifeboat_category` is correctly package-gated in both `allowed`
and `visible`, and `visible_when_empty = yes` makes an empty but valid category
inspectable. The six new actions are not category-wide stores: their routes,
targets, costs, timers, receipts, and removal rules bound the actual play.

The Home Guard uses vanilla `state_target = any_controlled_state`, a restricted
state-id `target_trigger`, `FROM` state effects, and map-and-decisions mode.
The partner actions use `target_root_trigger` plus the existing
generation-aware `fallout_nzl_relief_partner_is_current` trigger. Quiet-Seas
effects never select a country: they operate exclusively on
`var:fallout_nzl_pirate_aggressor` after existing exact-current triggers pass.

## Existing mission quality notes

| Mission owner/category | Region and requirement | Duration | Success | Failure and duplicate risk |
| --- | --- | --- | --- | --- |
| Breakwater Works / Lifeboat Ledger | Wellington; convoys and trucks | 70 days | Naval base, +12 Harbor Capacity | State/package loss clears major-repair lock, -7 Trust; one-shot completion flag. |
| Storm-Port Works / Lifeboat Ledger | Auckland; support equipment and manpower | 105 days | Naval base, dockyard, +12 Harbor Capacity | State/package loss clears major-repair lock, -7 Harbor; one-shot completion flag. |
| Milk Rail / Lifeboat Ledger | South Island; trucks and trains | 70 days | +12 Food Security | State/package loss marks the major mission failed and spoils stores; one-shot completion flag. |
| Port Militia Drill / Lifeboat Ledger | Country-wide; rifles, manpower, Army XP | 70 days | Army XP and +7 Sea-Lane Security | Package loss records major failure; no unit creation; one-shot completion flag. |
| Convoy Volunteer Corps / Lifeboat Ledger | Auckland; support equipment, 16 convoys, manpower | 105 days | Exactly one escorted formation | State/package loss marks failure; explicit formation guard plus `fire_only_once` closes the free-unit loop. |
| Refugee Fleet Admission / Lifeboat Ledger | Country-wide; Harbor and Food both above Strained | 70 days | 700 manpower and +12 Trust | Package loss clears external lock and records failure; one-shot completion flag. |
| Rescue Passage / Lifeboat Ledger | Exact current external transaction; 16 convoys and Food above Stable | 105 days | Current partner receipt and +12 Trust | Now cancels on package or transaction invalidation, clears the external lock and transaction; one-shot completion flag. |

The non-mission actions have varied equipment, manpower, Command Power, Navy
XP, Political Power, value, cooldown, and target requirements. The only old
static-cost clarity gap is the nine older localisation entries listed above.

## AI validity and route locks

Every new AI block starts from a modest existing constant and relies on the
same visibility/target rules as the player. No AI can pick a dead partner, an
unrecorded partner, a closed route, a completed relief receipt, or an invalid
pirate target. Critical Food Security raises dairy convoy priority; war raises
Home Guard priority; a current pirate war raises both Quiet-Seas priorities.

The existing `fallout_nzl_lifeboat_ai` plan contains focus strategy only, so
the new decisions carry their own valid `ai_will_do` conditions. No decision
AI uses random country selection.

## Cleanup and exploit-risk handoff

The chain architect has merged these items into the central NZL reset block in
`common/scripted_effects/fallout_nzl_lifeboat_effects.txt`. They must remain in
NZL/ROOT scope:

```txt
clr_country_flag = fallout_nzl_home_guard_mobilization_active
clr_country_flag = fallout_nzl_quiet_seas_access_revoked
if = {
	limit = { has_variable = fallout_nzl_guaranteed_relief_partner }
	diplomatic_relation = {
		country = var:fallout_nzl_guaranteed_relief_partner
		relation = guarantee
		active = no
	}
	var:fallout_nzl_guaranteed_relief_partner = {
		clr_country_flag = fallout_nzl_relief_guarantee_received
		clear_variable = fallout_nzl_relief_guarantee_generation
	}
}
clear_variable = fallout_nzl_guaranteed_relief_partner
clear_variable = fallout_nzl_guaranteed_relief_partner_generation
```

Do not perform a world iteration to clear Home Guard state flags or postwar
relief flags. They are harmlessly stale because their paired generation
variables are required to match the current global generation. The reset
snippet revokes the guarantee from NZL/ROOT; reversing that relation would
address the wrong diplomatic direction.

No new action creates a unit, war goal, core, claim, ownership transfer, or
unbounded equipment reward. The one outbound aid action costs twice the
support equipment it grants, has a full timer, and is one receipt per exact
partner per generation.

## Localisation and asset handoff

Added titles/descriptions for the six decisions and full custom-cost triplets
for `fallout_nzl_cost_home_guard`,
`fallout_nzl_cost_dairy_relief_convoy`,
`fallout_nzl_cost_partner_relief_port`,
`fallout_nzl_cost_relief_guarantee`,
`fallout_nzl_cost_revoke_raider_access`, and
`fallout_nzl_cost_quiet_seas_patrol`. The touched localisation file is UTF-8
with BOM.

The six new decision IDs temporarily reuse reviewed existing GFX so there is
no broken sprite reference:

| New decision | Temporary reviewed sprite | Required final sprite and DDS path |
| --- | --- | --- |
| Home Guard | `GFX_decision_fallout_nzl_port_militia_drill` | `GFX_decision_fallout_nzl_home_guard_mobilization` → `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_home_guard_mobilization.dds` |
| Dairy convoy | `GFX_decision_fallout_nzl_milk_rail_assignments` | `GFX_decision_fallout_nzl_dairy_relief_convoy` → `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_dairy_relief_convoy.dds` |
| Partner relief port | `GFX_decision_fallout_nzl_wellington_breakwater_works` | `GFX_decision_fallout_nzl_partner_relief_port` → `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_partner_relief_port.dds` |
| Relief guarantee | `GFX_decision_fallout_nzl_offer_rescue_passage` | `GFX_decision_fallout_nzl_relief_guarantee` → `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_relief_guarantee.dds` |
| Revoke raider access | `GFX_decision_fallout_nzl_last_berth_closure` | `GFX_decision_fallout_nzl_revoke_raider_access` → `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_revoke_raider_access.dds` |
| Quiet-Seas patrol | `GFX_decision_fallout_nzl_anti_piracy_bearing` | `GFX_decision_fallout_nzl_quiet_seas_patrol` → `gfx/interface/decisions/fallout_world_end_nzl_lifeboat_state/decision_fallout_nzl_quiet_seas_patrol.dds` |

The asset brief did not request these six sprites. Asset production should add
the DDS files, source/processed PNGs, prompt records, contact sheet, manifest,
and `interface/fallout_world_end.gfx` entries. That GFX wiring is parent-owned.

## Validation evidence and limits

- Checked offline decision-modelling guidance, vanilla decision documentation,
  script-constant documentation, and vanilla BRA/AFG state-target and DEN
  guarantee precedents before editing.
- Static scan confirms all four focus unlock flags now have decision consumers;
  every added scripted trigger/effect call exists in the current NZL package;
  all six titles, descriptions, and custom-cost triplets resolve once.
- Static lifecycle scan finds zero `activation` keys on the five converted
  normal decisions; the remaining `activation` keys belong only to selectable
  missions.
- Verified the state target is restricted to the five exact package states and
  partner/aggressor actions use existing generation-aware receipts.
- No HOI4 launch or in-game test was run, per parent instruction. No
  decision-owned scripted GUI was touched, so GUI inspection/rendering was not
  applicable.

## Simplifications, omissions, and blockers

No gameplay simplification was made within the assigned six-decision scope.
The temporary icon reuse is deliberate and documented above. Completion still
depends on asset work producing the six bespoke icons and parent GFX wiring,
plus the broader parent validation of the currently dormant package activation
path. The central guarantee and transient-flag cleanup has been merged.
