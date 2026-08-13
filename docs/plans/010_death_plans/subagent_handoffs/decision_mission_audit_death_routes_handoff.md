# Event 010 Death Route Decision/Mission Audit Handoff

Audit date: 2026-06-15

Supersession note: the current Black Atlas implementation is a transient timed dashboard opened from the decision category. It no longer uses a separate GUI close control or standalone decorative status icons.

Scope audited: Missing Island, containment, Living Compact, wasteland/outpost work, Dark Methods, Black Oath/Herald, Black Apostolate, and Black Atlas decision/GUI surfaces.

Allowed patch files only:

- `common/decisions/010_death_decisions.txt`
- `common/scripted_guis/010_death_black_atlas_scripted_gui.txt`
- `interface/010_death_black_atlas.gui`
- `localisation/english/010_death_l_english.yml`
- `docs/plans/010_death_plans/subagent_handoffs/decision_mission_audit_death_routes_handoff.md`

Read-only support checked:

- `docs/specs/010_death_specs/`
- `docs/plans/010_death_plans/improvement_loop_remaining_routes_addendum.md`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/scripted_effects/010_death_effects.txt`
- offline Paradox wiki decision/scripted GUI pages and core required pages
- vanilla scripted GUI documentation and decision/effect/trigger docs

## Files Changed

- `common/decisions/010_death_decisions.txt`
- `common/scripted_guis/010_death_black_atlas_scripted_gui.txt`
- `interface/010_death_black_atlas.gui`
- `localisation/english/010_death_l_english.yml`
- `docs/plans/010_death_plans/subagent_handoffs/decision_mission_audit_death_routes_handoff.md`

No effects, triggers, constants, assets, spreadsheet, or unrelated files were edited.

## Changed Identifiers

Decisions and mission:

- `death_recognize_death_war`
- `death_call_living_conference`
- `death_join_living_compact`
- `death_compact_war_declaration`
- `death_joint_coastal_patrol_plan`
- `death_authorize_wasteland_entry_gear`
- `death_share_wasteland_entry_gear`
- `death_last_shores_response`
- `death_strengthen_quarantine_line`
- `death_keep_port_lit`
- `death_survey_the_wasteland`
- `death_build_dead_zone_outpost`
- `death_hold_quarantine_line_mission`
- `death_bind_the_unburied`
- `death_whisper_to_zol`
- `death_take_black_oath`
- `death_offer_prison_census`

Scripted GUI and GUI:

- `death_black_atlas_scripted_gui`
- `death_black_atlas_forbidden_values`

Localisation:

- `death_black_atlas_gui_values_right`
- `death_black_atlas_gui_forbidden_values`

## Before And After Behavior

- Before: active Heralds and Black Oath countries could still see or use several normal living-containment decisions, including compact joining/calls, coastal patrol, quarantine, wasteland entry, and Last Shores response.
- After: those living-response decisions require `death_has_no_forbidden_oath = yes`. Herald-specific Black Oath decisions remain visible through the Herald route.

- Before: Living Compact leaders could still start the Black Oath contact and oath decisions.
- After: `death_whisper_to_zol` and `death_take_black_oath` are hidden from `death_living_compact_leader`, preserving the compact leadership lock.

- Before: `death_hold_quarantine_line_mission` lasted 60 days, below the decision-mission skill's normal minimum band for hold-line objectives.
- After: the file-scoped mission duration constant is 90 days, giving a real defensive window without changing helper effects.

- Before: `death_bind_the_unburied` and `death_offer_prison_census` required manpower in cost triggers and text, but the decision/effect path did not explicitly subtract the advertised manpower.
- After: both decision `complete_effect` blocks compute the manpower cost from existing constants, negate through a temp variable, and apply `add_manpower = var:...` before calling the existing route helper.

- Before: `death_offer_prison_census` AI became more willing when name debt was already high.
- After: AI weight is zero above `name_debt_high`, and rises when black favor is below the Apostolate favor threshold.

- Before: the Black Atlas had no close button and always displayed a forbidden-route line in the main values panel.
- After: the Atlas has a close button wired to clear `death_black_atlas_open`, and forbidden-route status is separated into `death_black_atlas_forbidden_values`, visible only after Black Book, Zol contact, Oath, Herald, or Apostolate route state exists.

## Issue List By Severity

### High

1. `death_country_containment_category` does not attach `scripted_gui = death_black_atlas_scripted_gui`.
   - File outside allowed scope: `common/decisions/categories/010_death_categories.txt`.
   - Impact: the Atlas scripted GUI may not render from the decision category even though the decision opens the flag and GUI/scripted GUI files exist.
   - Recommended fix: add the scripted GUI attachment to the category in a parent patch.

2. `death_black_apostolate_available` still requires `death_name_debt` greater than or equal to the Apostolate debt threshold.
   - File outside allowed scope: `common/scripted_triggers/010_death_triggers.txt`.
   - Impact: this conflicts with the addendum direction that Apostolate should require debt below the betrayal threshold or converted through the Last Name chain.
   - Recommended fix: parent should revise the trigger once the Last Name/debt-conversion logic is finalized.

### Medium

3. `death_feed_border_to_death` remains cheap in explicit cost text.
   - Allowed file could only change visible decision gates; the real consequence logic is in effects/constants outside scope.
   - Impact: the decision does consume a state and raises route consequences, but the immediate custom cost is only command power.
   - Recommended fix: add stability/manpower/diplomatic or route-debt cost in constants/effects, then align cost text.

4. Black Atlas route secrecy is improved but not complete.
   - `GetDeathAtlasForbiddenStatus` still lives in scripted localisation outside allowed scope.
   - Impact: the hidden value is no longer shown until route contact, but the dynamic status helper itself still contains the full route labels.
   - Recommended fix: if full secrecy is required, split the scripted localisation into pre-contact and route-contact variants.

5. The quarantine hold mission has no region-specific title.
   - Owner: current country.
   - Category: `death_country_containment_category`.
   - Region: any controlled state with `death_quarantine_line` bordering active wasteland.
   - Requirement: keep at least one quarantined border state active.
   - Duration: 90 days after patch.
   - Success: `death_quarantine_hold_success`.
   - Failure: `death_quarantine_hold_failure`.
   - Duplicate risk: low; it is the only active Death mission found.
   - Remaining gap: the mission is country-level rather than naming the exact state whose line is being held.

### Low

6. Some decision requirement text remains broad.
   - State-targeted decisions use `[FROM.GetName]` in effect tooltips for most target actions, but availability failures still rely on custom cost summaries and hidden triggers.
   - Recommended fix: add custom trigger tooltips in triggers/effects if parent wants exact blocked reasons for every map requirement.

7. No active Spirit of War/Peace decision or GUI surface was found in the scoped files.
   - Residual risk: broader event-name/catalog surfaces were not patched in this task.

## Decision Category Lifecycle Notes

- `death_missing_island_category` remains correctly pre-reveal and report-recipient scoped.
- `death_country_containment_category` now better separates living response from Herald/Black Oath state through decision visibility locks.
- The same category still contains active containment, compact, Dark Methods, Herald, Apostolate, Atlas, and aftermath/outpost actions. The current route locks keep it safer, but a parent cleanup may still want subcategory-level lifecycle helpers.
- Black Atlas lifecycle remains timed flag-opened and defeat-gated. The current dashboard has no separate GUI close control.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `death_hold_quarantine_line_mission` | current country | `death_country_containment_category` | any controlled quarantined border state | maintain a `death_quarantine_line` state bordering active wasteland | 90 days | `death_quarantine_hold_success` | `death_quarantine_hold_failure` when no valid line remains | Low |

No additional Death missions were found in the scoped decision file. The remaining wasteland/outpost work is implemented as state-targeted decisions, consistent with the current Death decision spec's preference for decisions over separate objective cards.

## Cost And Requirement Clarity Notes

- Patched manpower-spend mismatch for `death_bind_the_unburied` and `death_offer_prison_census`.
- Existing custom cost localisation has icon-first base/blocked/tooltip variants for the audited route decisions.
- Black Atlas hidden route text no longer appears in the main always-visible values panel.
- `death_feed_border_to_death` cost remains clearer as a design risk than a syntax issue: it has visible severe consequences, but the explicit custom cost is light.

## AI Validity And Route-Lock Notes

- Patched AI-visible living containment actions so Herald/Black Oath countries do not use normal Compact and containment decision families.
- Patched Black Oath contact/take decisions so the compact leader cannot self-route into Oath from leadership.
- Patched `death_offer_prison_census` AI so high debt blocks rather than encourages more census offerings.
- Remaining route-lock risk: `death_black_oath_visible` is still broad in the trigger file, but the two player-facing oath decisions now add the compact-leader block locally.

## Localisation And Tooltip Gaps

- Added `death_black_atlas_gui_forbidden_values`.
- Updated `death_black_atlas_gui_values_right` to remove the always-visible forbidden line.
- No new player-facing decision names were added.
- No localisation encoding conversion was intentionally performed; the existing file retained its UTF-8 BOM.

## Cleanup And Exploit-Risk Notes

- Atlas display is handled by the timed open flag rather than a separate close control.
- Heralds are locally blocked from living containment decisions audited in this pass.
- Manpower farming risk from advertised-but-unpaid manpower costs is reduced for Bound Unburied and Prison Census.
- Remaining exploit risk: Feed Border's immediate custom cost should be strengthened in constants/effects, outside this patch's allowed scope.
- Remaining cleanup risk: category-level scripted GUI attachment is missing outside allowed scope, so the Atlas open/close patch depends on a parent category edit to become visible.

## Validation Performed

- Checked patched files for brace balance after edits:
  - `common/decisions/010_death_decisions.txt`
  - `common/scripted_guis/010_death_black_atlas_scripted_gui.txt`
  - `interface/010_death_black_atlas.gui`
  - `localisation/english/010_death_l_english.yml`
- Verified GUI element/effect names align:
  - `death_black_atlas_forbidden_values` -> `death_black_atlas_forbidden_values_visible`
- Verified the new Atlas localisation key is referenced and defined.
- Verified no active `Spirit of War` / `Spirit of Peace` strings appear in the scoped decision, scripted GUI, interface, or Death localisation files.

Skipped validation:

- No in-game parser run was performed.
- No category attachment patch was made because `common/decisions/categories/010_death_categories.txt` was outside the user-approved edit list.
- No effects/triggers/constants validation patch was made because those files were read-only for this task.

## Commit Status

No commit was created. The worktree already contains substantial parent/user Event 010 changes, including modified versions of the same files, so committing only this subagent patch without also committing unrelated parent work was not safely separable.

## Skills Used

- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
