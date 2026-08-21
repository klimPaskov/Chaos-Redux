# Shared Event Chaos Levels Localisation Audit

## Scope

Audited only:

- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`

The audit checked the normal-event Chaos-level display and gate wording for the Events catalogue, Event Details, and Settings trigger controls. No gameplay, GUI, documentation outside this handoff, or spreadsheet source was edited.

## Reviewed terminology proposal

The audit proposed changing:

- `localisation/english/chaosx_gui_l_english.yml`

Changed key:

- `chaosx.event_chaos.requires.5`

Current and final: `Requires Totalen Chaos (Chaos level 5)`.

Proposed but rejected: `Requires Total Chaos (Chaos level 5)`.

Parent review retained the user's explicit tier name and the shared Event Log wording. No dynamic tokens or formatting codes were removed.

## Findings

### Missing keys

None found for the feature selectors or GUI consumers. The six exact-level filter keys, six colored numeric keys, five named locked-requirement keys, requirement-met key, and catalogue level label all resolve in `chaosx_gui_l_english.yml`.

### Duplicate keys

None found among the feature keys in the owned GUI localisation file or across `localisation/english/*.yml`.

### Scripted localisation issues

No selector-order defect found. Each colored level selector tests levels 1 through 5 before its level-6 fallback. Each requirement selector tests the met state first where that surface needs it, then named locked tiers, with the fallback last.

The Events row selectors consistently index `global.events_log_events_view_chaos_level_entries` with `events_log_history_index`. The Event Details selectors consistently index `global.events_log_open_event_detail_chaos_level_entries` with `events_log_open_event_detail_index`. Direct source tracing confirms the producer effects append these values to arrays aligned with their corresponding event rows.

### Dynamic text opportunities

No additional dynamic text is needed for this bounded feature. The numeric `Chaos lvl:` display is sourced from the row's required-level array, and the requirement text uses the existing named tier keys. Replacing those names with the current live tier selector would be incorrect because the tooltip must name the required tier, not the player's current tier.

### Cross-surface mismatches

The audit proposed changing level 5 from `Totalen Chaos` to `Total Chaos`. Parent review rejected that proposal because the user's required six-level list explicitly names `Totalen Chaos`, and the shared Event Log tier localisation uses the same name. The final feature text therefore retains `Totalen Chaos`.

The remaining surfaces agree on the contract:

- Event 9 resolves to internal tier 1, displayed as Chaos level 2 and named Gathering Storm.
- Other registered normal events default to internal tier 0, displayed as Chaos level 1.
- Locked catalogue rows receive a negative display weight and therefore show `N/A` through `chaosx.events_log.events.weight.locked`.
- Locked catalogue rows also show the named `Requires ... (Chaos level N)` label.
- Event Details shows exact colored numeric `Chaos lvl:` text.
- Settings and Event Details trigger tooltips show the requirement status and state that Force Trigger Mode bypasses it.

### File encoding

`localisation/english/chaosx_gui_l_english.yml` retains its UTF-8 BOM (`EF BB BF`) after the patch. The two files under `common/scripted_localisation/` are Clausewitz script sources rather than localisation YAML and retain their existing encoding.

### Prose quality

- Vagueness: none remains in the feature text. Locked requirements name both the tier and numeric level.
- Bloat: the requirement and bypass wording is short enough for tooltips.
- Obvious explanation: the tooltip does not repeat the button label beyond the necessary action line and gate status.
- Repetition: the repeated requirement strings are shared localisation keys consumed by all three surfaces.
- Overcomplication: none found.
- Parent-reviewed terminology: retained the user-specified `Totalen Chaos` wording. No em dashes, semicolon sentences, staged contrasts, prompt fragments, or implementation-history prose occur in the feature text.

### Sourced quotations

No sourced or attributed quotation appears on any inspected feature surface. No quotation text was changed.

## Validation

Meaningful source checks completed:

- Traced the Event 9 requirement from `initialize_event_chaos_level_registry` and `get_event_required_chaos_level` through the Settings variable, Events catalogue parallel arrays, and Event Details parallel arrays.
- Verified that list and detail availability triggers compare the same required tier against the matching Chaos Meter minimum.
- Verified that both Settings and Event Details click gates explicitly accept `force_trigger_mode_enabled` as a bypass.
- Verified that negative catalogue weights resolve to `§RN/A§!`.
- Checked feature localisation key coverage and cross-file duplicates.
- Verified the GUI localisation file's BOM after editing.

## MCP blocker

Required read-only MCP inspection was attempted and is unresolved because the installed server did not return evidence:

- `hoi4.gui_inspect` for `events_log_events_content_window` with an Event 9 locked scenario timed out after 180 seconds.
- A combined inspection attempt covering `chaosx_settings_window`, `events_log_events_content_window`, and `events_log_event_details_window` also remained pending and was terminated after repeated waits.
- `hoi4.event_inspect` lint for selector `{ kind: event, eventId: chaosx.nr9.1 }`, with helper expansion disabled and bounded depth/nodes/edges, timed out after 180 seconds.
- `hoi4.gui_render` for `events_log_event_details_window` was started for locked and long-text states at 1920x1080, then terminated without output when the parent requested immediate conclusion.

No artifact URI was produced. Source review is not presented as equivalent rendered or engine evidence. Overflow and final visual placement therefore remain unverified by MCP in this audit.

## Remaining risks and skipped validation

- MCP could not verify rendered text overflow, click-region agreement, or evaluated runtime localisation for the three linked GUI windows.
- The Event 9 event-chain graph could not be retained or inspected through MCP because of the timeout.
- No in-game validation was performed, as live consumer validation belongs to the user.

No unresolved wording decision remains. No mechanic gap or improvement-loop plan was required.
