# Holy Realm Focus Tree Layout and Infrastructure Patch Handoff

Date: 2026-06-13

Scope: focus-tree-only audit and bounded patch for Event 003 Holy Realm. Gameplay edits were limited to `common/national_focus/003_holy_realm.txt`; this handoff records the patch. No assets, GUI, decisions, scripted effects, or unrelated dirty files were edited.

The workspace already had unrelated dirty files and an unrelated untracked handoff in this folder. They were left untouched.

## Files Changed

- `common/national_focus/003_holy_realm.txt`
- `docs/plans/003_holy_realm_plans/subagent_handoffs/2026-06-13_focus_tree_layout_infrastructure_patch.md`

No localisation files were changed.

## High-Priority Fixes First

| Issue | File and ids | Patch status | Notes |
| --- | --- | --- | --- |
| Lamps/Throne overlap with Storehouses, Unbroken Pass, and Awakened One | `THR_lamps_remain_lit`, `THR_throne_without_body`, descendants | Patched | Lowered the Lamps and Throne route families and their descendants so the row-9 logistics/military/Awakened cluster no longer shares their row. |
| Governance fork too far left | `THR_council_of_abbots`, `THR_name_protector_regent`, `THR_seat_pilgrim_assembly`, first follow-ups | Patched | Shifted the governance fork and related follow-ups right, away from Arhat administration. |
| Empty Seat aftermath misplaced | `THR_final_silence`, `THR_empty_seat`, `THR_witnesses_keep_the_record` | Patched | Empty Seat and Witnesses Keep the Record now sit directly below Final Silence. |
| Four Teaching Seats too far right | `THR_four_teaching_seats` | Patched | Moved left under the teaching branch. |
| Same-row prerequisite links | Multiple route nodes | Patched | Coordinate audit now reports no duplicate coordinates and no prerequisite at the same row or below its child. |
| Read the Pattern should sit below One Becomes Many | `THR_read_pattern_suffering`, `THR_one_becomes_many_focus` | Patched | `THR_read_pattern_suffering` is now below and requires `THR_one_becomes_many_focus`. |
| Infrastructure overstacking past max level 5 | Infrastructure reward focuses | Patched | Direct infrastructure rewards now check the grant size before adding roads: level-1 rewards use `infrastructure < 5`, while level-2 rewards use `infrastructure < 4`. Existing Storehouses compact-member random state already had the level-1 cap. |

## Changed Focus IDs

Layout or prerequisite changes:

- `THR_sit_beneath_prayer_flags`
- `THR_first_quiet`
- `THR_second_quiet`
- `THR_third_quiet`
- `THR_fourth_quiet`
- `THR_council_of_abbots`
- `THR_name_protector_regent`
- `THR_seat_pilgrim_assembly`
- `THR_abbot_examiners`
- `THR_regent_pass_watch`
- `THR_pilgrim_refuge_courts`
- `THR_four_teaching_seats`
- `THR_buddha_mandate`
- `THR_the_awakened_one`
- `THR_return_to_the_seat`
- `THR_show_the_powers`
- `THR_powers_are_not_toys`
- `THR_one_becomes_many_focus`
- `THR_path_through_walls`
- `THR_lotus_bridge_focus`
- `THR_read_pattern_suffering`
- `THR_vanishing_from_sight_focus`
- `THR_seated_in_sky_focus`
- `THR_touch_sun_moon_focus`
- `THR_debate_the_pretender_focus`
- `THR_exile_the_echo`
- `THR_break_false_mandala`
- `THR_absorb_the_shadow`
- `THR_lamps_remain_lit`
- `THR_white_flags_foreign_roads`
- `THR_vow_against_annihilation`
- `THR_throne_without_body`
- `THR_witnesses_gather`
- `THR_extinction_of_defilements_focus`
- `THR_doctrine_last_war`
- `THR_reactors_prayer_wheels`
- `THR_all_roads_end_silence`
- `THR_no_one_leaves_mandala`
- `THR_final_silence`
- `THR_empty_seat`
- `THR_witnesses_keep_the_record`
- `THR_mountain_granaries`
- `THR_snowline_clinics`
- `THR_storehouses_for_world`
- `THR_permit_foreign_pilgrimage`
- `THR_letters_to_war_tired`
- `THR_shelter_exiles`
- `THR_mandala_of_nations`
- `THR_refusal_of_empires`
- `THR_last_human_signature`
- `THR_sermon_without_translation`
- `THR_compassion_of_non_return`
- `THR_ministry_of_release`
- `THR_refuse_final_debate`
- `THR_peace_without_ownership`
- `THR_world_still_burns`
- `THR_second_refuge`
- `THR_lamps_entered_register`
- `THR_seal_roads_from_panic`
- `THR_no_more_peace_delegations`
- `THR_sort_worthy_broken`
- `THR_world_marked_as_wound_focus`

Infrastructure reward cap changes:

- `THR_mountain_refuge`
- `THR_shelter_border_villages`
- `THR_guard_high_passes`
- `THR_rewrite_civil_register`
- `THR_seal_of_refuge`
- `THR_count_mountain_roads`
- `THR_monastic_labor_vows`
- `THR_mountain_granaries`
- `THR_snowline_clinics`
- `THR_guardians_outer_passes`

`THR_storehouses_for_world` was included in the infrastructure audit; its compact-member infrastructure reward already had `limit = { infrastructure < 5 }`, so no reward cap edit was needed there.

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Opening survival trunk | `THR_mountain_refuge`, `THR_shelter_border_villages`, `THR_guard_high_passes`, `THR_bodhisattva_accepts_seal` | Implemented, reward cap patched | Opening infrastructure still exists but no longer fires against maxed states. |
| Meditation and Dhyana path | `THR_sit_beneath_prayer_flags` through `THR_fourth_quiet` | Implemented, layout patched | Ladder now sits below `THR_first_doctrine_suffering` with parents above children. |
| Governance route family | Council, Protector Regent, Pilgrim Assembly forks and follow-ups | Implemented, layout patched | Fork moved right; mutual exclusions unchanged and still route-defining. |
| Teaching mission path | Envoys, Translation Houses, Bombardment, Many Lamps, Four Teaching Seats | Implemented, layout patched | Four Teaching Seats moved left under the teaching path. |
| Industry and sanctuary logistics | Roads, Workshops, Granaries, Clinics, Storehouses | Implemented, layout/reward cap patched | Snowline Clinics and Storehouses moved to avoid same-row prereqs; direct infrastructure rewards are capped. |
| Guardian military | Vow Keeper Regiments through Unbroken Pass | Implemented | `THR_unbroken_pass` remains at row 9; the overlapping post-Buddha route nodes moved down. |
| Anti-chaos powers | Awakened One, powers branch, Pattern, Touch Sun/Moon | Implemented, layout/prereq patched | `THR_read_pattern_suffering` now follows `THR_one_becomes_many_focus`; capstone no longer shares a row with required parents. |
| Lamps / restraint route | `THR_lamps_remain_lit` and peace descendants | Implemented, layout patched | Route moved down; no route rewards changed. |
| Throne / Final Silence route | `THR_throne_without_body`, Last War, witnesses, reactors, ministry, Final Silence | Implemented, layout patched | Final chain moved down; Empty Seat aftermath aligned under `THR_final_silence`. |
| Expansion / register route | Himalayan and eastern register branches | Implemented, mostly unchanged | Outside reported layout cluster except one pass-guardian infrastructure cap. |
| Hidden Schism branch | Debate, Exile, Break, Absorb | Implemented, layout shifted | Shifted down one row to stay below Awakened One after the Buddhahood branch moved. |

## Missing or Simplified Content

- No broad route redesign was attempted. The tree remains a large implemented route set, but a full design-depth pass could still reduce repeated flat rewards in some late support focuses.
- Several non-anchor support focuses still have no route-specific `ai_will_do`; this patch did not add a broad AI pass.
- Infrastructure localisation was not rewritten. The gameplay effect now applies infrastructure only to eligible states below level 5, which is the intended cap behavior, but some descriptions still summarize the route as granting infrastructure.
- No new focus icons were created or replaced. Asset work was explicitly out of scope.

## Icon Coverage Table

| Icon area | Coverage | Notes |
| --- | --- | --- |
| Custom Holy Realm focus icons | Covered | All eight custom Holy Realm focus icon ids used by this tree are defined in `interface/*.gfx`: `GFX_goal_THR_refuge`, `GFX_goal_THR_bodhisattva`, `GFX_goal_THR_arhat`, `GFX_goal_THR_buddha`, `GFX_goal_THR_diplomacy`, `GFX_goal_THR_mercy`, `GFX_goal_THR_pacification`, `GFX_goal_THR_final`. |
| Vanilla/generic focus icons | Covered by base game assumption | The tree uses many vanilla `GFX_goal_generic_*` and `GFX_focus_*` icons. No local missing custom reference was found. |
| Repeated icon patterns | Remaining risk | Several spiritual/meditation focuses still share `GFX_focus_smiling_buddha`; this is acceptable for a narrow layout patch but remains a visual-variety risk for a future icon pass. |

## Localisation and Reward Mismatch List

- Focus title/description coverage: no missing `THR_*` focus title or `_desc` keys in `localisation/english/003_the_holy_realm_l_english.yml`.
- Localisation keys changed: none.
- Icon ids changed: none.
- Reward mismatch risk: infrastructure descriptions now implicitly mean eligible non-maxed states. This avoids wasted infrastructure over cap without changing player-facing route names.
- No focus names/descriptions were found that directly contradicted the patched layout or `THR_read_pattern_suffering` route placement.

## AI Behavior Gaps

- Major route anchors have AI weights, including peace, governance, teaching, Final Silence, hidden Schism, and expansion anchors.
- Many support focuses still rely on no explicit `ai_will_do` or broad factors from surrounding route flow. A full route-aware AI pass remains broader than this patch.
- No AI weights were changed. The only gameplay sequencing change is `THR_read_pattern_suffering` requiring `THR_one_becomes_many_focus`.

## Before and After Behavior

Before:

- `THR_lamps_remain_lit` and `THR_throne_without_body` shared row 9 with `THR_storehouses_for_world`, `THR_unbroken_pass`, and `THR_the_awakened_one`.
- `THR_empty_seat` and `THR_witnesses_keep_the_record` sat left of the Final Silence endpoint rather than below it.
- Several focus prerequisites were on the same row as their child, including `THR_sit_beneath_prayer_flags`, `THR_doctrine_last_war`, `THR_touch_sun_moon_focus`, `THR_last_human_signature`, `THR_sermon_without_translation`, `THR_ministry_of_release`, `THR_lamps_entered_register`, and the Snowline/Storehouses logistics chain.
- Direct infrastructure rewards could attempt to add infrastructure to states already at the level 5 cap.

After:

- The reported overlap cluster is separated by moving the Lamps route, Throne route, and their descendants down.
- The governance fork and follow-ups are shifted right.
- `THR_empty_seat` and `THR_witnesses_keep_the_record` sit under `THR_final_silence`.
- `THR_four_teaching_seats` sits left of its old position, under the teaching route.
- `THR_read_pattern_suffering` sits under and requires `THR_one_becomes_many_focus`.
- Coordinate validation reports no duplicate focus coordinates and no same-row/below prerequisite links.
- Every direct infrastructure focus reward is guarded by a cap suited to its grant size: `infrastructure < 5` for level-1 grants and `infrastructure < 4` for level-2 grants. Storehouses compact support already had the level-1 cap in its random controlled state limit.

## Meaningful Validation

Ran task-specific text validation:

- Parsed `common/national_focus/003_holy_realm.txt`: 111 focus blocks plus the tree id; no duplicate focus coordinates.
- Checked focus prerequisites and mutual exclusions inside the tree: no missing focus id references.
- Checked prerequisite layout ordering: no prerequisite is on the same row as or below its child.
- Checked direct infrastructure reward call sites: each direct infrastructure grant is guarded by the appropriate cap for its reward size; Storehouses compact support already had the level-1 cap in its random controlled state limit.
- Checked Holy Realm focus localisation coverage: no missing focus title or description keys in `003_the_holy_realm_l_english.yml`.
- Checked custom Holy Realm icon definitions in `interface/*.gfx`: all custom `GFX_goal_THR_*` icons used by the tree are defined.
- `git diff --check -- common/national_focus/003_holy_realm.txt` returned clean.

Skipped meaningful validation:

- No in-game focus-tree UI load/screenshot validation was run from this environment.
- No decision, GUI, scripted effect, or asset validation was run because those systems were explicitly out of scope.

## Remaining Route Risks

- The patch changes one route gate: `THR_read_pattern_suffering` now requires `THR_one_becomes_many_focus`. This matches the requested placement but makes Pattern sequencing stricter than before.
- The tree still has some repeated generic rewards and repeated generic/vanilla icons. Addressing that fully would be a broader focus-tree variety pass.
- Some late support focuses still have limited or generic AI behavior. A route-aware AI pass remains open.
- The visual result should still be checked in-game because Clausewitz path drawing can look awkward even when coordinates and prerequisite ordering are clean.

Plan handoff path: none written. The remaining risks are broader polish/design depth, not a new required route family.
