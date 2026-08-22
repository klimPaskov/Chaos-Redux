# Event 006 pre-event localisation audit and patch handoff

Date: 2026-08-21

Scope: Event 006 localisation only, including the directly paired Event Details key in `chaosx_gui_l_english.yml`. No gameplay, focus, portrait, asset, GUI-layout, spreadsheet, or unrelated localisation source was changed.

## Outcome

The active Event 006 English localisation no longer describes a visible pre-event liberation crisis, queued wave request, pressure threshold, or cooldown consequence. The retained compatibility history keys now describe only public release records and territorial results. The Pacific strategic-project cost display now shows only its dynamic costs. Event Details now starts from governments that have already taken control and uses the live join thresholds from script constants.

The public report `chaosx.nr6.2` and all five `independence_wave.evolution.*` stages already matched the post-commit and post-active mechanics, so they were not rewritten.

## Files changed

- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `localisation/english/006_independence_wave_super_event_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event006_pre_event_localisation_audit_2026_08_21.md`

## Changed keys

### Decision cost display

- `independence_wave_cost_pacific_island_strategic_tooltip`
- `independence_wave_cost_pacific_island_strategic_blocked`

### Retained compatibility history display

- `independence_wave.history.crisis.title`
- `independence_wave.history.crisis.description`
- `independence_wave.history.crisis.cause.occupation`
- `independence_wave.history.crisis.cause.stability`
- `independence_wave.history.crisis.cause.combined`
- `independence_wave.history.crisis.cause.requester_lost`
- `independence_wave.history.crisis.cause.unknown`
- `independence_wave.history.crisis.outcome.title`
- `independence_wave.history.crisis.outcome.queued`
- `independence_wave.history.crisis.outcome.blocked`
- `independence_wave.history.crisis.outcome.cancelled`
- `independence_wave.history.crisis.outcome.committed`
- `independence_wave.history.crisis.outcome.requester_lost`
- `independence_wave.history.crisis.outcome.unknown`

`independence_wave.history.crisis.outcome.description` was inspected but not changed because its scripted-localisation call remains valid.

### Event Details

- `chaosx.events_log.window.event_details.independence_wave`

## Behavior and display before and after

- Before: the compatibility history display described a host entering a liberation crisis before an ordinary synchronized wave, then exposed queued, blocked, cancelled, pressure, and cooldown states.
- After: the same legacy key family is safe if reached by a stale compatibility reference. It says the public record opens only after governments control territory, and its outcomes report only whether a public release or territorial transfer was recorded.
- Before: the Pacific strategic cost tooltip prefaced the numbers with `More than:` and added the obvious sentence `Completion commits these amounts.`
- After: the tooltip and blocked variant show only the existing dynamic cost values and icons, matching the other Event 006 cost families.
- Before: Event Details opened with abstract route-summary prose and hardcoded `half` and `two` join thresholds.
- After: Event Details starts with governments controlling capitals, ministries, and borders, names their immediate tasks, and reads `independence_wave_join.reduction_percent` and `independence_wave_join.minimum_states_lost` dynamically.

## Audit lists

### Missing keys

None found in the assigned Event 006 localisation set. Every localisation key referenced by the Event 006-specific scripted-localisation files has a definition, and every changed key has exactly one English definition.

### Duplicate keys

None found across `localisation/english/006_independence_wave*.yml`.

### Scripted localisation issues

- No broken scripted-localisation reference was found.
- `common/scripted_localisation/006_independence_wave_crisis_localisation.txt` and the shared Event Log scripted-localisation retain the legacy `independence_wave.history.crisis.*` key family. Gameplay and shared scripted-localisation identifiers were outside this task, so the display text was made safe without renaming those keys or calls.

### Dynamic text opportunities

- Implemented: Event Details now uses `[?constant:independence_wave_join.reduction_percent|0]` and `[?constant:independence_wave_join.minimum_states_lost|0]` instead of hardcoded threshold words.
- No other in-scope dynamic opportunity was needed. The public report already uses frozen presentation counts and scripted regional, armed, host, and network text. Evolution text describes stage effects rather than duplicating tunable values.

### Cross-surface mismatch notes

- Fixed: legacy history text no longer contradicts the hidden `chaosx.nr6.1` entry and post-commit `chaosx.nr6.2` presentation contract.
- Fixed: Event Details now describes the current post-active join mechanic with its live thresholds.
- No mismatch found between the public report, Event Details, or the five evolution descriptions after the patch.
- The historical specs and plans still mention the retired crisis system when documenting its removal or older implementation history. Those are not active player-facing localisation and were not changed.

### File encoding concerns

None. All three edited localisation files retain the UTF-8 BOM.

### Prose-quality issues and repairs

- Vagueness: replaced abstract `prepared institutions, regional identities, and remembered polities` opening language with the concrete seizure of capitals, ministries, and borders.
- Bloat: removed the cost tooltip's explanatory prefix and trailing sentence.
- Obvious explanation: removed `Completion commits these amounts.` because the displayed custom cost already communicates the commitment.
- Repetition: consolidated the Event Details list of unsettled conditions into four immediate state-building tasks.
- Overcomplication: split the Event Details overview from the later voluntary join rule and replaced the legacy crisis sequence with direct public-record wording.
- Style-rule repair: removed player-facing threshold and cooldown implementation language from the compatibility history display. No em dash, semicolon, prompt fragment, tuning note, or implementation-history sentence was introduced.

## Sourced quotation preservation

The quote-bearing super-event surface was inspected. These sourced quotation keys were preserved verbatim:

- `chaosx_super_event.23.q` — Woodrow Wilson, Fourteen Points, Point XIV, 8 January 1918.
- `chaosx_super_event.24.q` — Hosea 8:7, King James Version.

No quote wording, punctuation, attribution, or formatting was changed.

## Dynamic localisation preservation

- Preserved `[GetIndependenceWaveCrisisHistoryCause]` and `[GetIndependenceWaveCrisisResolution]` in the compatibility history display.
- Preserved `[GetIndependenceWaveRivalBlocEventDetails]` and `[GetIndependenceWaveRivalBlocEventDetailsMember]` in Event Details.
- Preserved every dynamic cost constant, numeric format, color code, and icon token in the Pacific strategic cost keys.
- Added the two join-threshold constant tokens listed above.

## Meaningful validation

- Exact stale-string search found no active English localisation occurrence of `The Independence Wave Crisis`, `Open the Independence Wave`, `wave pressure`, `More than:`, `Completion commits these amounts`, `ordinary synchronized wave`, `waiting for the next synchronized wave`, or `pressure and cooldown consequences` after the patch.
- Exact definition checks found one definition for every changed key.
- The assigned `006_independence_wave*.yml` set contains no duplicate localisation key.
- Event 006-specific scripted-localisation key resolution found no missing English definition.
- Source inspection confirmed `chaosx.nr6.1` is hidden, while `chaosx.nr6.2` is the first public report and requires a positive committed presentation count.

## MCP evidence and limitations

- Event trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4cfa6bfde3f4b4632f3f5c16ed5007d893ab2dffffd3675b2edca3d0b97d51bd/53a4e1063a287755beb2c15dd0d7296ed819fab3e443400f994393eea0d37e5c/event-trace-bc0062fc8506.json`.
- Event entries render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00014a46c7206835fe50df3457dd5b805d08ef647db478035cf3ea24a72aff7f/b594507adbb4a990a378bd1d7d16ca72d4a7ef99c572721b3c2fd22034253b36/event-entries-bc0062fc8506.json`.
- Event viewer limitation: both event-id and source-file selectors scanned the workspace but returned `selectedNodes: 0`, so the linked event render cannot be treated as a bounded visual confirmation of `chaosx.nr6.2`. Source inspection remains the evidence for the hidden/public transition.
- Event Log GUI inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f761da33efb9e6e2853134d7b30222b252dbec2c3dff59deba9303baa74f60a8/1db3c25c664eb1a53894f4539eca3be5afa95fcd88e196f2045c88a3135dbea0/gui-inspect.a03229dfafd2db4d.json`.
- Event Log GUI render artifact after the patch: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1640b0a7cad150323820b11a02f8e946451a74bc299a4e8d3ddb49b0a5b05ee/c85e5f0a694a46439f89f636f84699a3a67ed33a87efdf0d11803f82f6ff71b0/events_log_popup_window-full.svg`.
- GUI limitation: the available scenario contract accepted an id but no Event 006 value payload, so the renderer produced the same generic full-window artifact before and after the localisation edit. It did not render the selected Event 006 details paragraph or provide a trustworthy text-overflow comparison. The GUI inspection also reported global truncated diagnostics dominated by unrelated source collisions; none identified this Event 006 key specifically.

## Skipped meaningful validation

- No live HOI4 session was launched; in-game consumer validation belongs to the user.
- No spreadsheet edit or workbook comparison was performed because the parent assigned localisation files only.
- No Technology Tree Viewer check applies; Event 006 technology surfaces were outside scope and the viewer is unavailable in the installed package.

## Unresolved wording decisions and remaining risks

- The internal key and scripted-localisation names still contain `crisis` for compatibility. Their displayed English text is neutral, but removing or renaming the internal compatibility system requires gameplay/shared-script ownership.
- The GUI renderer could not inject the Event 006 selection state, so exact in-window wrapping remains unresolved despite the shorter Event Details prose.
- No missing mechanic or design-depth gap was found, so no separate improvement plan was written.

## Simplifications, omissions, and blockers

No gameplay or localisation fallback was used. The only blocker is the MCP selector/scenario limitation described above; it prevents bounded rendered proof, not the source-level localisation patch.
