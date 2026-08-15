# Event 006 localisation surface audit

## Patch

- Changed `localisation/english/006_independence_wave_super_event_l_english.yml`.
- Changed key `chaosx_super_event.23.q`.
- Preserved the verified Wilson quotation verbatim and added the accepted documentary date to its displayed attribution: `Woodrow Wilson, Fourteen Points, Point XIV, 8 January 1918`.
- No dynamic localisation or gameplay behavior changed.

## Audit results

- Missing keys: none in the current Event 006 event, decision, mission, focus, GUI, formable, scenario, super-event, or scripted-localisation source references scanned.
- Duplicate keys: none for Event 006 keys across English localisation.
- Scripted localisation issues: no unresolved Event 006 `localization_key` targets and no direct section or icon format characters in Event 006 scripted-localisation source.
- Dynamic text opportunities: the Event Details and catalog mirror should use one canonical premise. Exact automatic wave counts belong in a dedicated dynamic status or tooltip surface if they must remain player-visible.
- Cross-surface mismatch: workbook `Events!C7` includes Join eligibility, a Ruthenia package spotlight, and the `3/4/5/7/10` automatic ladder, while `chaosx.events_log.window.event_details.independence_wave` in `localisation/english/chaosx_gui_l_english.yml` contains the premise, Join eligibility, and dynamic rival-bloc appendices. The workbook was not changed in this audit.
- Encoding concern: all 61 Event 006 localisation files retain UTF-8 BOM. However, 642 key lines across 12 Event 006 files have leading indentation contrary to the repository localisation style rule. This should be normalized in a separate mechanical pass.
- Prose quality: sampled current Join, Kosovo, Ruthenia, evolution, scenario, formable, and super-event prose is concrete and preserves route identity. `independence_wave_status_gui_refresh_tt` and `independence_wave_status_gui_toggle_animation_tt` repeat obvious button actions and should be removed or replaced with useful state information.
- Sourced quotations: Wilson and Hosea excerpts were preserved verbatim. The Wilson attribution now matches the accepted research. The Hosea attribution already matched.

## Validation and blockers

- Verified the patched key still carries the exact quoted excerpt, formatting codes, and accepted attribution.
- Verified the localisation file retains its UTF-8 BOM.
- The focus MCP route returned `ARTIFACT_MANIFEST_INVALID` because its artifact provenance manifest is invalid.
- A valid combined Event 006 event and GUI inspection request did not return within the bounded audit window and was terminated. Current render, overflow, and click-region acceptance therefore remain unresolved.
- No workbook or generated catalog CSV was edited.

## Remaining decisions

- Decide whether Event Details or the workbook is the canonical premise text, then align `Events!C7` and `chaosx.events_log.window.event_details.independence_wave` without placing package inventory or automatic release counts in the Details field.
- Decide whether the two obvious scripted-GUI button tooltips should be removed or given non-obvious behavior information.
