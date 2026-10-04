# Event 013 abnormal path window: live QA repair handoff

Date: 2026-10-03
Worker: chaosx_event_ui_worker (event-owned scripted GUI)
Disposition: implemented; live consumer validation pending with the user.

## Scope and ownership

Event: 013 Natural Disasters (`natural_disasters`).
Window: `natural_disaster_abnormal_path_window`, scripted GUI `natural_disaster_abnormal_path_gui` (player context), opened from the report event `chaosx.nr13.4` option "Open the path map" through `natural_disaster_open_abnormal_gui` and from the event-details history button through `natural_disaster_open_abnormal_gui_history`.
The window, its scripted GUI, its GUI view builder (`natural_disaster_rebuild_abnormal_gui_view`, `natural_disaster_append_gui_record_from_index`) and its `GetNaturalDisasterGui*` scripted localisation are used only by Event 013, so the surface is event-owned.
No shared event-log, event-details, settings, super-event, or registry surface was edited.

Acceptance basis: the parent's live QA brief of 2026-10-03 lists the six defects below and authorises fixing them inside the owned files, including a local unit correction of the value the window reads.
The scoped correction reference is `docs/plans/013_natural_disasters_plans/references/2026-10-03_path_window_layout_reference.jpg`; it keeps the existing background art, composition, and controls and only re-maps content onto the painted regions.

## Files changed

- `interface/013_natural_disasters.gui`
- `common/scripted_guis/013_natural_disasters_scripted_gui.txt`
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
- `localisation/english/013_natural_disasters_l_english.yml` (window keys only; the parent's uncommitted `chaosx.nr13.4.d` edit was left in the working tree and is not part of this commit)
- `common/scripted_effects/013_natural_disasters_effects.txt` (display-date unit correction, GUI urgency conversion, segment position array)
- `common/script_constants/013_natural_disasters_constants.txt` (new `natural_disaster_date` category)
- `docs/plans/013_natural_disasters_plans/references/2026-10-03_path_window_layout_reference.jpg`
- `docs/plans/013_natural_disasters_plans/references/2026-10-03_path_window_before_after.jpg`

`interface/013_natural_disasters.gfx` needed no change; every sprite used already existed.

## Defects, root causes, and fixes

### 1. Header subtitle wrapped below the header band

Root cause: `natural_disaster.gui.header_status` concatenated sequence, segment count, family, severity, next impact, domain, and display mode (about 125 characters) into a 760x40 text box placed at y 53, so line one straddled the plate edge and line two sat on the frame below it.
The title also sat at x 38 over the left vent instead of inside the plate.
Fix: the title, family icon, and status now sit inside the painted header plate (x 148 to 938, y 18 to 62) as one vertically centred row.
The status is one line from `GetNaturalDisasterGuiHeaderSummary`: "Sequence N of M | K segments | domain", or "No abnormal sequence is active".
Family and severity moved to the detail panel subtitle, the impact date to the detail facts and timeline, and the display mode to the motion button label and tooltip.
The longest fixture ("Sequence 12 of 12 | 48 segments | Mediterranean tsunami basin") fits in one line.

### 2. Impact date 1958.10.31 on 2 January 1936

Root cause: date variables count one game hour as 0.00001 (offline wiki, Data structures, Game variables `date`), but `natural_disaster_schedule_date`, `natural_disaster_repeat_schedule_date`, and `natural_disaster_next_reassessment` were built as `global.date + <day count>`.
A two-day delay therefore added 200,000 hours; on HOI4's 365-day calendar that is exactly 1 January 1936 plus 22 years and 303 days, which is 1958.10.31, matching the live screenshot to the day.
Fix: these three display dates now add `days * hours_per_day / hours_per_date_unit` (constants `natural_disaster_date.hours_per_day = 24` and `hours_per_date_unit = 100000`).
None of the three variables is read by gameplay; they feed the window, the aftermath card timing lines, and the GUI urgency sort.
The GUI urgency sort (`natural_disaster_prepare_gui_urgency_score`) now converts the date difference back to days before applying its day horizon.
The decision-card lines `natural_disaster.card_timing.scheduled_impact` and `natural_disaster.card.reassessment` read the same variables and are corrected by the same change.

Parent-owned gameplay finding (not changed, reported precisely): the delayed job queue uses the same unit mistake.
`natural_disaster_enqueue_state_job` sets `natural_disaster_job_desired_due_date = global.date + natural_disaster_job_delay_days`, `natural_disaster_reserve_job_day` shifts conflicts by `+1`, and `natural_disaster_process_due_job` (fired by `chaosx.nr13.2` after `days = natural_disaster_job_effective_delay`) only processes jobs whose due date is `<= global.date`.
With these units a job scheduled N days ahead is due N x 4,166 days later, so when `chaosx.nr13.2` fires no job should qualify, and warnings, impacts, reports, follow-ups, and reassessments queued this way would not execute.
The same unit feeds `natural_disaster_report_due_date` and `natural_disaster_chain_due_date` (shown by the window's Report and Chain milestones), the comparison `natural_disaster_chain_due_date > global.date` in the chain-mission activation, and `natural_disaster_chain_mission_extension`.
The parent should confirm in the live run whether queued impacts arrive; a fix would convert the job delay to date units when building the due date, convert `due - global.date` back to days for `days =`, and shift reservation conflicts by one day in date units.
Until that fix lands, the Report and Chain milestone dates in this window remain wrong by the same factor.
Other events use the same `global.date + days` pattern (for example `event021_settlement_deadline` and `random_civil_war_sponsor_commitment_until` in `common/scripted_effects/021_random_civil_war_decision_effects.txt`); they are outside this task and are listed only as a cross-event risk.

### 3. Detail panel values and overflow

Root causes:
- "Hazard: unclassified hazard": the selected record's `family_group` is only stored once the warning profile resolves, so a forecast record still holds `family_group.random`.
- "Sequence: 1 / 0": the row printed the sequence id and the zero-based `path_segment_index`.
- "State: none confirmed": the row printed `natural_disaster_linked_state`, which is the previous path state, not the selected state.
- Overflow: eleven descriptive rows (about 25 lines) were placed in a 220x286 box that crossed the card frame and ran under the recovery meter.

Fixes:
- New `GetNaturalDisasterGuiSelectedHazardClass` resolves the physical hazard class from the selected family, matching the warning-profile mapping, and names the physical hazard for abnormal families (massive eruption: Volcanic and ash; rupture: Seismic; meteor families: Atmospheric impact; storm corridor: Storm and severe weather).
- The facts frame shows five rows: Hazard, Segment "N of M" (new `natural_disaster_gui_position_entries` array filled by the GUI view builder), Path status, Impact due or Struck date (`GetNaturalDisasterGuiSelectedImpactLine`), and Deaths (`|*1` short format).
- The previous-segment link moved to the facts tooltip as "Arrived from", with "no earlier segment" for the origin.
- Below the frame: Warning, Follow-up, and Relief only; Damage, Disruption, and Recovery need moved to the tooltip of that block; card state, result, and death driver moved to the facts tooltip.
- Recovery shows the phase name ("not started", "Early rescue", and so on); the raw scores moved to its tooltip with an explanation of the burden and the meter sections.
- `natural_disaster_gui_recovery_progress_fill_1_visible` no longer requires the live recovery status, so closed history records light the first section consistently with sections two and three.
Checked with the eruption fixture and the longest-text fixture (storm corridor, "funded rail, road, and convoy preparations protected the first relief routes", "a route has been secured for foreign relief", 1.3M deaths); every row stays inside its region without overlap.

### 4. Title text on the plate edges

Root cause: the two-line title (hoi_20b, 52 px) was drawn at 786,116, partly outside the 44 px state plate drawn at 766,94, and 10 px off its horizontal centre.
Fix: the state plate (warning or impact frame at 0.5 scale) is centred in the panel at 795,98; the state name is a single centred line inside it (box 808,103, 244x30, vertical centre), and family and severity form a centred subtitle under the plate.
MCP `centeredOn` confirms the title is centred on the plate.

### 5. Bottom strip: legend, stray "S", empty swatches

Root causes:
- The stray "S" was the `natural_disaster_gui_milestone_schedule` button label: the button used `scale = 0.42`, the engine drew the sprite scaled but centred the text on the unscaled 48x48 frame, so "S" fell outside the icon.
  The same effect pushed the Previous, Locate, and Next labels to the lower right of their 0.65-scaled buttons.
- The legend's two rows (y 653 and 673) straddled the top border of the painted cell bar, and two legend icons were drawn at 7 px.
- The nine painted swatches carried no data.
Fixes:
- No text-bearing button is scaled any more; buttons use the native 123x34 sprite, and text-free controls use transparent hitboxes over separate labels.
- Milestones are icon plus word label slots ("Warn", "Due", "Hit", "Report", "Chain", "Review") in the lower path canvas with 40x48 hitboxes; the timeline text sits beside them with a yellow label.
- The legend title sits in the tray's upper band and the eight items form one row centred in the cell bar with uniform 18 px icons.
- The swatch strip is a labelled severity scale (Local, Severe, Regional, Catastrophic, Abnormal on swatches 1, 3, 5, 7, 9) with a pin under the selected segment's level and a "Severity" caption with tooltip.

### 6. Segment list, markers, and buttons

- Cards: the 0.83-scaled card frames overlapped the painted slots and the map panel border, and the engine dropped the second line of button text.
  Each card is now a slot container with a centred two-line text box (state name and card state) and a transparent 142x90 hitbox matching the painted slot; the selected card shows an amber accent bar.
- Markers: the number labels were hidden under the status overlays.
  Each marker is a 64x82 container with its status overlay, a number label under the pin, and a transparent 64x64 hitbox on top; the impact pin is centred in the slot.
- Buttons: Previous, Next, Locate, and Aftermath sit in two rows at the bottom of the detail panel; Refresh and the motion toggle (label "Motion: on" or "Motion: off") sit in the lower path canvas, with sequence navigation below them when two or more sequences exist.
  The close button moved to 1044,20 so it no longer overlaps the right vent.
- Window placement: `position = { x = -543 y = -372 }` with `orientation = center` and no `origo`, the vanilla pattern used by `interface/acesview.gui`; the size matches the 1087x744 painted panel.

The path note shortens to "Route: the cards list the first five segments in arrival order. N further segments are reached with Previous and Next." because the old four-line route list duplicated the cards.

## Reference and native mapping

| Region (window px) | Native elements | Content and interaction | Notes |
| --- | --- | --- | --- |
| Header plate 148-938 x 18-62 | `natural_disaster_gui_title`, `..._header_family_*`, `..._header_status`, `..._close` | title, family icon, one-line status with tooltip, close | status tooltip explains sequence, segments, domain |
| Segment column slots 40-182 | `..._card_N_slot` containers with `_selected`, `_text`, hitbox | select segment | selected accent bar |
| Path canvas 230-765 x 94-612 | layer containers, `..._marker_N_slot`, `..._path_queue`, `..._milestone_*_slot`, `..._timeline`, refresh, toggle, sequence buttons | markers select segments; milestones select timeline fact | view controls kept with the map |
| Detail panel 798-1062 x 94-613 | state plate frames, title, subtitle, `..._detail_frame`, facts, details, recovery text, meter, Previous, Next, Locate, Aftermath | selected segment facts and actions | long descriptions in tooltips |
| Legend tray 56-583 x 640-725 | `..._legend*` | static legend | one row in the cell bar |
| Severity strip 638-1044 x 640-725 | `..._severity_caption`, `..._severity_label_*`, `..._severity_marker_*` | selected severity | pin is the non-colour cue |

Justified adaptations: the reference keeps the painted background unchanged, so no new art was requested; the state plate holds one line because two hoi_20b lines cannot fit inside the 44 px frame; the severity scale uses five stops across nine painted swatches.

## Budgets

- Visible mechanic values on the detail panel: segment position, impact date, deaths, plus the recovery phase meter; hazard and path status are descriptors.
- Primary actions: Previous, Next, Locate, Aftermath, Refresh, Motion (six, all navigation or display; no gameplay cost), plus sequence navigation only with two or more sequences.
- No control spends resources, so no cost texticons apply.
- Main text blocks are at most three short labelled statements; long descriptors live in two-to-four-line tooltips.

## State matrix covered by MCP renders

- Warning-scheduled eruption (live QA fixture), card 1 selected, motion on, one milestone, abnormal severity.
- Crowded longest-text fixture: damaged panel, static layers, storm corridor family icon, impact, next-hit, and static warning markers mixed, all six milestones, impact plate, three meter sections, catastrophic severity, sequence navigation visible, motion off, no card selected.
- Dormant history view (empty list): only header, path note, legend, severity labels, Refresh, Motion, and Aftermath remain.
- Global render states: normal, selected, warning, hover, full-list, long-text, maximum-value, empty-list.
- Resolutions: 1920x1080 at UI 1, 1366x768 at UI 1, 2560x1440 at UI 1.25, 1280x720 at UI 1.

## MCP evidence

Artifacts live under `C:\Users\klimp\AppData\Local\hoi4-agent-tools\workspaces\mod_chaos_redux_ea3b2d67c2c0\artifacts\<first two hex>\<sha256>\`.
The combined image is `docs/plans/013_natural_disasters_plans/references/2026-10-03_path_window_before_after.jpg` (live screenshot, baseline render, two final renders).

Before:
- `hoi4.gui_inspect`, scenario `nd013_baseline`, shared revision `c74ac3f28363ebc6645f5cab8429808b3fec864ea66710305e46e55bd9caf1e3`, artifact `9a3001493a8885bcf5e676aecd085a10c36ab88cd6592e27a631fe4e8cca8ae6`.
- `hoi4.gui_render`, scenario `nd013-live-eruption-washington` (live values transcribed from `scn007b_3pop03.png`), source revision `8a5e189bf41a9be1508a8775aa65d3b4c1fa65310b72bf4096884cbdf2315f85`: full `f4f537d2227ccd97a69ce7bcfe45844e6bb4378edeeac042f042e5a6e2f0a1d0`, cropped `e09d9f1f9f70ef75437e2aab2734ebd94f9ef2be9b44f4b532fa3ed1520b4826`, click regions `c8cb8fde0b01dc862f774caf4831e8afa3e0a756813e0eb5a518dd225018eb15`, layout `1dadbe53d3d2ee9c0630ec5dc20803dc82cfb62f0fbb514d03b5c5e42c18df48`.
  The baseline render reproduced the wrapped header, the title/plate misalignment, the detail overflow under the meter, and the dropped card second line seen live; it also placed the old window's top-left at screen centre because it did not apply `origo = center`, which the new explicit centring removes.

Intermediate previews (corrected after review):
- Iteration 1, source revision `f577b642bdef82d4b548e721b8640254abc94ed63d59a4979e3a0844905d091a`, cropped `961beeb80fa67a47b21d61826bf38c09d0304145f519099b61c4b9008d3335df`: route note and timeline read as one line, small severity pin; fixed with labelled timeline keys and a 0.45 pin.
- Crowded iteration, source revision `07d0eb6c0e50ffe6ba8a67e65f6e81c23bfd13421fc4a7539d104f039bd09b5d`, cropped `eed99ddc822492dc69ac7e7c30a734e1d85571f84c1b2453ed3fdf2b95148c4a`: "Impact" and "Report" milestone labels touched; fixed with "Hit".

After:
- Dormant and resolution matrix, source revision `06516c726ed85c9c1b06404561ed52c808d652526cbe82f460cfae38bc474404`: cropped `05207adcb040f3c371617ccc822f8c2cb46c2bc47bc550060c6dcea6f501ba1b`, resolution matrix `80e9e1ee3c6a9225ace3173a3e4f57a5710e993aae3707aa28dd47d4c097ee24`.
- Crowded fixture `nd013-crowded-longest-text`, source revision `92deac686f126cc10cef6749cc92e14807b2a8902a13e4321b1bdef2e57c3173`: cropped `87965d4c69dc8b150b14a342ae993d79e173669c8326609fa43f398d316a1305`, click regions `92567d3e31dc619646a84c6ef58c72508b6c4b38afa09a538fb878bdcb21e7d5`, state matrix `1c07c0798484674f482f6fe02b6ccf8502f1127ab36c141f9b8e75f0cd0416ac`, resolution matrix `ba2a0406023b059c7a7c267b340a8785be4c4a54db5831585b66f835453f678c`.
- Live fixture `nd013-live-eruption-washington-fixed`, source revision `c4ba0c51988cd2051d1e7f53f3f77ade0f6d0ba6d6d31d0f7d71f57e3f630a3f`: cropped `c3d42c851d44b37d5a9d099a73d03b73781f89a68fa865bc7e30eec2503964aa`, click regions `7cbd9a356ec739ffeab0214568be178ed9262143acb705ea59470a4a29dbf38d`, state matrix `37b929a8d2b6ac6c5b7807cd8901861955cc129e87e075b162eb64c241e9203a`.
- Assertion run `nd013-live-eruption-washington-assert`, source revision `90fc4319f409a7d17cad93e44ac0bad831f399f71f77af67994fbf1fe01df0cc`, validation `ac6dc6ee9e0967e1504dc9b0071d8e66264c7c73bc79d9f0f65fef727990a3ca`: visible, hidden, containedBy (title in state plate, facts in detail frame, card text in card hitbox, legend in panel), centeredOn (title on plate, card 1 and card 3 text on their hitboxes), and button-label centring checks all passed.
- `hoi4.gui_inspect` after the change, scenario `nd013-post-change-inspect`, shared revision `90fc4319f409a7d17cad93e44ac0bad831f399f71f77af67994fbf1fe01df0cc`, artifact `b62d7af6d2ca3544309b50cb6b97d9eac097165528f70344baaa771dd968a068`.

Reviewed diagnostics: remaining `GUI_VISIBLE_OVERLAP` entries are labels and icons under their own transparent hitboxes or panels under content; `GUI_ACCIDENTAL_CLIPPING` entries are hidden 0x0 elements or sub-pixel float rounding; `GUI_INCONSISTENT_ALIGNMENT` entries are intentional insets.
Fixture values are declared scenario inputs, not observed campaign state; the renderer shows frame 0 of animated sheets.

## Remaining risks and parent-owned work

- Job-queue date units (section 2): gameplay timing, Report and Chain milestone dates, and chain-mission comparisons need a parent-owned fix and live confirmation.
- Pre-existing asset diagnostics: `GUI_ANIMATION_STATIC_FALLBACK_MISSING` for the animated frame and marker sheets and `GUI_ANIMATION_ANCHOR_DRIFT` for the eruption, meteor, and tsunami sheets come from `interface/013_natural_disasters.gfx` naming and sheet art; they were not introduced here and belong to the frame-animation owner.
- At 1280x720 with UI scale 1 the 744 px window exceeds the screen height by 24 px; only the outer frame edge is affected.
- The engine behaviour that scaled buttons centre text on the unscaled frame is taken from the live screenshot; the new layout no longer depends on it.
- Live verification by the user: header, detail panel, legend, severity scale, card selection accent, marker numbers and hitboxes, tooltips on the facts, details, recovery, header, and severity caption, and the corrected impact and reassessment dates in a new save.

## Simplifications

None in the window scope. The job-queue unit bug is reported, not fixed, by instruction.

## Addendum 2026-10-04: delayed job queue date units

Worker: parent-delegated gameplay fix (Event 013 files only).
Disposition: implemented; live consumer validation pending with the user.
Acceptance basis: the parent's brief of 2026-10-03 to fix the job-queue unit mismatch reported in section 2 above, keep every timing value, and correct the window's Report and Chain milestone dates.
The "Job-queue date units" item under Remaining risks is resolved by this addendum.

### Root cause, confirmed

Date variables count one game hour as 0.00001 (offline wiki `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Game variables section, lines 1458 to 1778, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, `date` row).
`natural_disaster_enqueue_state_job` built `natural_disaster_job_desired_due_date` as `global.date + natural_disaster_job_delay_days`, so a delay of N days stored a due date about N x 11.4 years ahead.
`chaosx.nr13.2` was still delayed by the right number of days, because `due - global.date` returned the raw day count, but `natural_disaster_process_due_job` only accepts jobs with `due <= global.date`, so no job could qualify and warnings, impacts, reports, follow-ups, and reassessments never ran.

Save evidence from `save games/qa_scn007b.hoi4` (plain text, 1936.1.2.16, Operation Postern v1.19.2.0, player USA), read with `.agents/skills/chaos-redux-save-inspection/scripts/save_inspect.py` (`info`, then `flatten` with `--in countries`, `--in states`, and `--in variables`, each with `--match natural_disaster`, and `flatten --in countries/USA --match delayed_event`):
- `variables/events_log_history_date_entries^0 = 607.59371` is the launch date, 1936.1.1.
- USA `natural_disaster_job_due_date_entries` run from 609.59371 to 653.59371 and CAN from 610.59371 to 621.59371: the launch date plus whole numbers, so the first two-day job reads as 1958.10.31, the date seen live.
- USA `delayed_event[3]` is `chaosx.nr13.2` with 0 days and 20 hours left at 1936.1.2.16, so it fires 48 hours after the enqueue; the worker wakes on time and finds nothing due.
- USA `achievement_nd_barrage_expiry_date = 847.59371` (launch plus 240), so the Disaster Barrage deadline check in `chaosx.nr13.3` could never pass either.
- Values such as `camp_occ_origin_ceiling_k = 1.91301` confirm that script variables keep five decimals, so a whole-day offset of 0.00024 is stored exactly.
- State 357 holds `natural_disaster_schedule_date = 623.59371` and `natural_disaster_next_subevent_date = 624.59371`: the same-sequence day reservation had moved the impact one day after the displayed date.

Delayed events count down in whole hours (`hours`, `days`, and `months` fields in each saved `delayed_event`), and the installed `documentation/effects_documentation.md` (`country_event`) adds `hours`, `days`, and `months` together, so a due date built as `global.date` plus N days matches the worker's wake time to the hour.
The encoding is a linear hour count, so month lengths do not enter the conversion.

### Fix

Two Event 013 helpers in `common/scripted_effects/013_natural_disasters_effects.txt`, section "PERSISTENT DELAYED JOB QUEUE", work in place on the temp variable `natural_disaster_date_offset`:
- `natural_disaster_convert_days_to_date_offset` multiplies days by `hours_per_day` and divides by `hours_per_date_unit`.
- `natural_disaster_convert_date_offset_to_days` multiplies a date difference by `hours_per_date_unit`, rounds to whole hours, rounds up to whole days through `whole_day_ceiling_hours` and a modulo, and never returns less than zero, so a worker woken after that many days never runs before the due date.

They are Event 013 helpers rather than shared dynamic effects because their constants live in the Event 013 tuning table; a shared date helper in `chaosx_dynamic_effects.txt` would be the natural follow-up for the other systems listed below.
New constants in `natural_disaster_date`: `whole_day_ceiling_hours = 23` and `job_reservation_step_days = 1`, which replaces the former literal one-step conflict shift.
No timing value changed.

Converted sites:
- `natural_disaster_enqueue_state_job`: the due date is `global.date` plus the converted delay; the `days =` delay of `chaosx.nr13.2` is the reserved due date converted back to days, then clamped to `minimum_job_delay_days` as before.
- `natural_disaster_reserve_job_day`: a same-sequence conflict shifts the due date by one day in date units.
- `natural_disaster_transfer_pending_jobs_for_state`: the new controller's `days =` delay is the remaining date difference converted back to whole days, rounded up.
- `natural_disaster_activate_family_chain_mission`: `natural_disaster_chain_mission_extension` converts `chain_due_date - global.date` to days before subtracting `chain_mission_deadline_offset_days`.
- `natural_disaster_apply_state_disruption`: `natural_disaster_modifier_expiry`, which is stored but not read.
- `natural_disaster_achievement_begin_maximum_barrage`: `achievement_nd_barrage_expiry_date`, which `chaosx.nr13.3` compares with `global.date`.
- `natural_disaster_schedule_warning_and_impact`: after the impact job is reserved, `natural_disaster_schedule_date` (or `natural_disaster_repeat_schedule_date` for a repeat strike) takes the impact job's reserved due date and the abnormal history row is refreshed, so the card, the window, and the impact agree when a reservation moved the impact.
- `natural_disaster_schedule_reassessment_for_state`: `natural_disaster_next_reassessment` is the reassessment job's reserved due date.
- `natural_disaster_configure_scheduled_state` and `natural_disaster_configure_repeated_impact` call the helper instead of repeating the conversion inline.
- `natural_disaster_prepare_gui_urgency_score`: an unused default that added raw days to `global.date` is removed; the live-date branch already converts back to days.

These consumers are unchanged and correct once their inputs are real dates: the `due <= global.date` selection in `natural_disaster_process_due_job`, `natural_disaster_release_job_day`, `natural_disaster_chain_due_date > global.date` in the transfer path, the earliest-due chain refill (`chain_due_sentinel = 100000` stays far above date values near 607 to 650), the report snapshot dates, and every `GetDateStringNoHour` consumer.

Window Report and Chain milestones: `natural_disaster_report_due_date` and `natural_disaster_chain_due_date` copy the reserved job due date, so the history arrays, the GUI view arrays, the milestone tooltips, the timeline lines, and the report follow-up line print real dates without a GUI change.

Localisation: `natural_disaster.gui.timeline.with_reassessment` held a raw line break inside its quoted value, which the game reported as "Invalid key name at line 568"; the two parts are joined with an escaped `\n`.
The parent's uncommitted `chaosx.nr13.4.d` colour-code removal in the same file is kept and committed with it at the parent's request.

### Verification

- Numeric check of the helpers against the save values: an enqueue at 607.59371 with a two-day delay stores 607.59419 (1936.1.3) and converts back to 2 days; the 240-day barrage deadline stores 1936.8.29 instead of a year-4675 date; a transfer 30 hours before the due date waits 2 days, 24 hours before waits 1 day, and an overdue job waits 0 days.
- HOI4 MCP gap: `hoi4.event_inspect` `state_flow` on `natural_disaster_job_due_date_entries` and on `achievement_nd_barrage_expiry_date` returned `ARTIFACT_STORAGE_LIMIT` for workspace `mod_chaos_redux_ea3b2d67c2c0`, so this change has no MCP event evidence; source review and the save inspection do not replace it.

### Same pattern elsewhere (not edited)

A repository scan for `set_variable = { X = global.date }` followed within five lines by `add_to_variable = { X = <day count> }` found the same candidate mistake outside Event 013.
Examples are `event021_settlement_deadline`, `random_civil_war_sponsor_commitment_until`, and `event021_mediation_until` in `common/scripted_effects/021_random_civil_war_decision_effects.txt`, with further sites in `021_random_civil_war_effects.txt`, `021_random_civil_war_parent_effects.txt`, and `021_random_civil_war_evidence_effects.txt`.
Other files with hits belong to Events 006, 014, 018, 019, 020, 027, 029, 031, 032, 033, and 042 and to the famine, migration, humanitarian corridor, and condemnation sanction systems.
A site is harmful only where its value is compared with `global.date`, printed as a date, or turned back into a `days =` delay, so each owner should check the consumers.

### Live retest checklist

- Launch scenario #007 Disaster Barrage at maximum intensity: warnings appear on their warning day, impacts strike on the window's "Impact due" date, and reports arrive within the report delay.
- The path window shows 1936 dates for the Due, Report, Chain, and Review milestones, and the card's scheduled impact matches the day the impact lands.
- A forecast follow-up arrives on its Chain date, and its chain mission ends `chain_mission_deadline_offset_days` before that date.
- Recovery reassessments fire on the Review date.
- A state with a queued job that changes controller still delivers the job to the new controller on or after its due date.
- The timeline tooltip with a reassessment shows two lines, and the line 568 startup error is gone.
