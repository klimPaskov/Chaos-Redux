# CBRN commander traits and High Command handoff

Status: HQ and battle service implemented in source; native raid-to-army-leader credit remains blocked by the documented outcome-scope API. Native trait-panel visual proof and parent integration review remain pending; the icon artist completed the tracked orphan DDS removal.

## Scope and evidence

`common/unit_leader/chaosx_traits.txt` defines earned Chemical Operations Commander, Biological Operations Veteran, and Hazard Warfare Veteran in appended earned rows 16 through 18; assignable Protected Assault Expert and Theatre Containment Organizer occupy appended general and field marshal rows.
It no longer overrides vanilla Skilled Staffer or Expert Delegator placement.
Installed vanilla `common/unit_leader/00_traits.txt` ends its army earned and field marshal rows at 15 and its general assignable rows at 14; the retained Sweden Rulebook Commander uses general row 16 and Protected Assault Expert uses general row 17.
The offline Character modding wiki states that `gui_row` is zero-based and that an omitted `gui_column` is chosen from `trait_type`, matching the native army trait definitions; these appended rows do not replace a vanilla row in the same column.
Installed vanilla `interface/traittreewindow_common.gui` defines a 210-by-55 `unit_leader_trait` tile, and `interface/armytraittreewindow.gui` defines the centered `unitleader_trait_tree_window` at 1340-by-778 with a clipped, vertically scrollable `regular_traits` panel at root-relative x294/y110 and size 636-by-640.
At UI scale 1, that panel begins approximately at screen x584/y300 for 1920-by-1080 and x904/y480 for 2560-by-1440; actual tile coordinates and row 18 visibility are engine-generated, not proved by these source values.
`common/scripted_effects/cbrn_commander_progression_effects.txt`, `common/scripted_triggers/cbrn_commander_progression_triggers.txt`, `common/script_constants/cbrn_commander_progression_constants.txt`, and `common/on_actions/cbrn_commander_progression_on_actions.txt` implement and document named-leader receipts.

The `cbrn_hq.2` upkeep event calls `cbrn_commander_record_completed_hq_operation` after each of seven successful upkeep ticks; its helper credits only five qualifying active orders after the final paid tick and after confirming the operation code, active status trait, assigned corps commander, and a fresh completion receipt.
Prepare Chemical Offensive and Theater Protective Posture receive no service credit, and failed upkeep and cancellation do not call the helper.
The receipt flag resets only at a new `cbrn_hq_commit_preparation`, so one completed order credits at most once.
Two chemical receipts earn Chemical Operations Commander, two biological receipts earn Biological Operations Veteran, and both traits earn Hazard Warfare Veteran.
The leader-scoped `on_army_leader_won_combat` callback counts a victory toward Protected Assault Expert only while the general commands a protected CBRN battalion.
The callback does not assert that this battalion fought in the specific battle.

`common/country_leader/cbrn_high_command_traits.txt` defines native Chemical Operations Commander specialist, expert, and genius High Command ranks, with planning speed of 1%, 3%, and 5% respectively.
Their appointment command-cap increases of 10, 20, and 30 and AI factors of 0.42, 0.64, and 0.86 match the corresponding vanilla High Command rank pattern; the parent probability audit must inspect and compare these added weights.
The generic CBRN Operations Director idea and trait are retired in `common/ideas/cbrn_high_command.txt` and the owned trait file; the other three institutional offices remain.
Biological Security Director organisation was reduced to 1% for the approved aggregate cap.
Protected Assault Expert gives 5% less out-of-supply penalty, and Theatre Containment Organizer gives one extra army-group command slot; both avoid conventional attack and defence stacking.

`common/unit_leader/024_video_game_in_sweden_traits.txt`, `common/scripted_effects/024_video_game_in_sweden_effects.txt`, `localisation/english/024_hearts_of_iron_l_english.yml`, and `interface/chaosx_traits.gfx` remove Field-Validated Planner, its grant, eligibility checks, sprite, and reward promise.
Rulebook Commander and the rest of the Sweden validation flow remain.
`localisation/english/cbrn_doctrine_l_english.yml` removes only the orphaned generic Director keys.
`localisation/english/cbrn_commander_progression_l_english.yml` supplies the new trait, role, and prerequisite text.
`docs/systems/cbrn_warfare/cbrn_commander_progression.md` describes the mechanic and icon contract; `common/scripted_effects/cbrn_commander_progression_effects.md` documents the new helper interface.

## Sprite contract

`GFX_trait_biological_operations_veteran` uses `gfx/interface/traits/cbrn/trait_biological_operations_veteran.dds`.
`GFX_trait_hazard_warfare_veteran` uses `gfx/interface/traits/cbrn/trait_hazard_warfare_veteran.dds`.
`GFX_trait_protected_assault_expert` uses `gfx/interface/traits/cbrn/trait_protected_assault_expert.dds`.
`GFX_trait_theatre_containment_organizer` uses `gfx/interface/traits/cbrn/trait_theatre_containment_organizer.dds`.
The icon artist has the exact names and paths, and all four DDS paths are present; final binary acceptance is outside this handoff.

## Checks and limits

Vanilla `00_traits.txt` supplies the earned-trait, assignable-trait, advisor-rank, out-of-supply, and army-group-size patterns; vanilla `00_on_actions.txt` identifies the winning army leader as the `on_army_leader_won_combat` scope.
The focused `chaosx.nr24.31` MCP trace and neighbourhood render completed without blockers, but the partial graph does not inspect the Sweden validation helper's full lifecycle.
The narrow `hoi4.gui_inspect` call for `windowName=unitleader_trait_tree_window` with an explicit 1920-by-1080 scenario and disabled generated scenarios timed out after 180 seconds; consequently no 1920-by-1080 or 2560-by-1440 native trait-panel render, scroll-state image, or click-region proof exists.
No native GUI override or layout patch was made; source-only row evidence must not be treated as visual acceptance.
Static source review found no active reference to Field-Validated Planner or the retired Director idea in the edited gameplay, interface, or localisation files.
The retired Field-Validated Planner runtime DDS at `gfx/interface/traits/024_video_game_in_sweden/024_video_game_in_sweden_field_validated_planner.dds` and the retired generic Director DDS at `gfx/interface/ideas/stage_5_chaos_warfare/cbrn_operations_director.dds` were removed after active source-reference checks. Historical snapshots still mention them as audit history; the icon package manifest records the removal.
The decoded Event 24 planner PNG under `docs/assets/024_video_game_in_sweden/notes/decoded_png/final_runtime/` is ignored or untracked historical material.
The installed vanilla `common/raids/_documentation.md` defines `actor_effects` and `victim_effects` as raid-instance scope and `division_effects` as participating-division scope, but lists only `var:actor_country`, `var:victim_country`, `var:target_state`, and `var:target_province` as raid-instance pointers.
The same documentation permits character scope in read-only raid success-chance modifiers; it does not pass that character to an outcome effect.
Vanilla raid outcomes use `division_effects` for `add_divisional_commander_xp`, not for an army-leader trait or a division-to-general scope switch; the installed effect and trigger documentation exposes no such switch.
Consequently native chemical and biological raids do not award these army-leader traits, including on completion, because a country-wide leader search would invent credit for an unproven participant.
No raid preparation, cancellation, failure, or successful outcome currently alters these personal commander-service counters.
The exact historical 1936/1939 starting Chemical Operations Commander grants and starting High Command appointment are owned by the historical roster and parent integration pass.
The parent owns removal of the orphaned `interface/cbrn_doctrine.gfx` sprite and reconciliation of the old Director icon entry in `docs/systems/cbrn_warfare/chaos_warfare_doctrine.md`.
No live game was launched by this subagent.
