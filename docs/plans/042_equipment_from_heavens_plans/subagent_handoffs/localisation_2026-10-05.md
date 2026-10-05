# Event 042 Localisation Handoff

Disposition: implemented within the parent-authorized localisation scope; parent review and final integration remain pending.

## Files changed

- `localisation/english/042_equipment_from_heavens_l_english.yml`

## Keys and behavior

- Shortened the three primary delivery descriptions and the group, stage, clue, recovery report, and evolution prose. The report body and its scripted substitutions contain no colour codes.
- Shortened report descriptions to concise state-specific prose and removed the appended clue from `chaosx.nr42.report.d` so each report stays focused.
- Updated `chaosx.nr42.1.reports_tt` to set an expectation of recovery-site searches and describe the local road and depot burden without promising another popup or hardcoding a duration. Updated the no-crews tooltip to use “aircrew”.
- Added `chaosx.nr42.summary.d`, `chaosx.nr42.summary.accident_d`, `chaosx.nr42.summary.zone_tt`, and `chaosx.nr42.unavailable.t/.d/.a`. Summary descriptions aggregate `[?efh_report_total|0]` sites and describe cargo in storage and continuing local burdens; accident summary also reports lost pieces and infrastructure damage.
- Updated final report title and option to describe the remaining cargo.
- Removed colour formatting from Event Details history, which is rendered on the light parchment surface.
- Retained former singular-file compatibility entries for `chaosx.nr42.2.*` and `chaosx.news.47.*` in the plural file. The canonical root `.1` keys remain present.

## Validation and remaining integration

- Confirmed the localisation file retains a UTF-8 BOM and each localisation entry is on one physical line.
- Attempted `python .tools/report_colour_audit.py --help` as requested to discover event filtering. The script did not expose help; it ran and returned `total keys with colour: 0`, so no `--event 42` scoped audit was available through that interface.
- Parent must wire `chaosx.nr42.summary.d` to the normal final `.13`, `chaosx.nr42.summary.accident_d` to accident final `.16`, and the unavailable keys to `.18`; `summary.zone_tt` is available for the final summary's burden tooltip.
- Parent must verify the production event files use `.2` as the visible delivery popup, preserve the two-popup cap, and aggregate accident text correctly. No live-game or MCP event-chain review was performed by this localisation-only subagent.
