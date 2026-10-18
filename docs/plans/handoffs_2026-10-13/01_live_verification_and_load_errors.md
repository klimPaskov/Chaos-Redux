# Handoff 1: live verification and remaining load errors

Read `00_common_rules.md` in this folder first.

## Why

Two rounds of restores and fixes were committed from source review only. Nothing was run in the game, and the interface renderer stalled for every job. The previous load-error job skipped its Linux loop. This handoff proves the work in the real game and finishes the load errors.

## Tasks

1. **Clean load (plan item C1).** On the isolated Linux game: launch with Chaos Redux, read the fresh `error.log` and `text.log`, fix every mod-caused error and every localisation collision at the source, relaunch, and repeat until none remain. Known leftovers from `chaos_redux_load_camps_repair_2026-10-13.md`: five missing flags with no historical original, the `UPPER_LEFT` and `Ven` diagnostics, and the missing Matignon DDS. Missing art goes to handoff 4's list (`icons_needing_new_art_2026-10-13.md`); do not invent it. Also read the owner's Windows logs read-only at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/logs/` for errors the Linux run does not show.
2. **Start a 1936 game and check each restored or fixed surface.** Take a screenshot of each into `.tmp/live_verification_2026-10-13/` and note pass or fail in `docs/plans/live_verification_2026-10-13.md`:
   - Welcome window text; main-screen about text; Chaos Redux help text.
   - Event log: history rows show only event names; flag hover names the country the click pans to; clusters view without the "show" control and subheaders; cluster details with a working checkbox per member and no overlapping "fires automatically" text.
   - Settings: auto event logs under Miscellaneous; super-event volume arrows have a tooltip; crisis pressure is off by default and worded for all events.
   - Chaos Meter window: history alignment, condemnation description, deaths entry spacing.
   - World-end scenario details view positioning; Launch Scenario button centred.
   - Technology folders: chemical (upper part unchanged from commit `cd2f068437`, consolidated lower part without overlaps) and biological (no disconnected cards).
   - Scientists: all present with their levels and traits; the Inhumane trait icon is the original.
   - Chemical release abilities usable by an army leader.
   - Biowarfare: the restored decision flow, a fast policy change, a raid started without friction, responses visible on the map.
   - Migration window picture inside its box; migration and famine decisions appear only under real pressure and cost fuel or convoys, never political power.
   - Camps window: every button works with no error line.
   - UI fractures: none at Calm World, growing and redder per tier, never over main buttons (set the Chaos Meter tier through the settings to step through them).
   - Starting state: breakthroughs for Japan, United Kingdom, United States, Soviet Union (bio) and Germany, United Kingdom, France (chemical); Germany has tabun; Japan starts unrestricted.
3. **Super events.** Fire the zombie outbreak super event and two others: correct original audio, original text, original layout.
4. **`e chaosx_test`.** Run it and confirm every unit family spawns at its assembly site without errors.
5. **Random terror event (C5) and performance (C4).** Fire the random terror chain and follow it to its end. Run the game at speed 5 for two in-game years with events firing and record whether it slows down; if it does, profile with the ranked list in `performance_audit_2026-10-13.md` and fix further.
6. Fix every failure you find, by restoring from history where an earlier version was right. Re-check after each fix.

## Deliverable

`docs/plans/live_verification_2026-10-13.md` with the pass/fail table, screenshots, fixes and commits. A clean-load statement is allowed only if the final launch's `error.log` has no mod-caused line.

## Interface screenshots handed from Handoff 2

The exact historical interface restores are implemented; the current audit is `docs/plans/interface_restore_audit_2026-10-13.md`.
The post-restore MCP render of `utopia_manifesto_ledger_container` timed out after 600 seconds and returned no artifact.
Source geometry and dependencies were reviewed instead; these screenshots are the requested visual follow-up, not a prerequisite for delivering Handoff 2's source changes.
Use the isolated Linux game under this handoff's rules and keep screenshots under `.tmp/live_verification_2026-10-13/`.
Capture 1920×1080 at UI scale 1 and 1366×768 at scale 1 where supported, using the actual normal entry points and coherent live states.

| Window / source | States and specific visual check |
| --- | --- |
| `chaosx_settings_window` — `interface/chaosx.gui` | Earlier side-by-side timer and manual controls; advanced and Miscellaneous scrolling; Fallout disable preference; volume-arrow tooltips; auto logs remain in Miscellaneous; new system-settings opener stays accessible below legacy content. |
| `events_log_popup_window`, `events_log_event_details_window`, `events_log_cluster_details_window` — `interface/chaosx_events_log_popup.gui` | Original event footer and actor flag/frame; catalogue/history actor hover matches click; Cluster Details three metadata lines, 41px member rows and each B2 checkbox; populated/empty/history cases and long member names; no Show/subheaders. |
| `chaos_meter_popup_window` — `interface/chaosx_chaos_meter_popup.gui` | Status original body plus live meter after scrolling; original Air overview and bottom toggle; source-record list/details overlay after scrolling; protected history, condemnation and deaths spacing. |
| `secret_alliance_counter_network_container` — `interface/011_secret_alliance.gui` | Hidden/revealed/selected/empty incident states; restored 720×360 cards and objectives; long objective text; warning and animation preference. Verify actual category placement because source width exceeds the 502px native-grid precedent. |
| `africa_charter_window` — `interface/012_africa_charter.gui` | Animation preference on/off; League complete/incomplete and Authority thresholds; historical ring position clears the toggle in every frame by alpha measurement; verify secondary text contrast over the ring and the native font label. |
| `cannibalism_early_header_window`, `cannibalism_network_window` — `interface/014_cannibalism_frontline_hunger.gui` | Early command, all five network pages, selected/empty/crowded dossiers and the two animation modes. |
| `cannibalism_warlord_command_window` — same file | Overview/States; old controlled-state and consumed-population summary, original capacity and new footer tabs; long values remain readable. |
| `cannibalism_revealed_command_window` — same file | Overview/Loyalty/Targets; old continental target card and seal; new tabs in left-side free space; empty/populated records; both animation modes. |
| `cannibalism_wendigo_command_window` — same file | Overview/Anchors; Winter Victories and original pulse; new footer tabs; inspect the historical decorative pulse/terminal-layer intersection when both qualifiers hold. |
| `utopia_manifesto_ledger_container` — `interface/015_utopia_manifesto_ledger.gui` | All four pages, four restored native summary scrollbars, warning, route emblems, recent balance animation and readiness seal. This was the failed MCP render target. |
| `kruger_directorate_container` — `interface/016_brilliant_scientist_directorate.gui` | Expanded/collapsed, five tabs, Refresh, animation preference, warning/project/facility/foreign/sovereignty/singularity cases; new middle portfolio scroller below the old two columns. Verify 700×500 category placement against the native-grid width. |
| `resources_found_field_window` — `interface/018_resources_found.gui` | Active/closed/selected/exhausted fields; original identity/status/metric positions and all five scaled hitboxes; long identity/resource strings and inherited dense status strip. |
| `black_plague_response_category_window` — `interface/020_black_plague_response.gui` | Historical 470×272 picture/checkbox progress, Medical Reserve and International Response; zero, unorganized and organized capacity states, preserving their guards. |
| `acid_rain_world_window`, `acid_rain_category_inlay` — `interface/033_acid_rain.gui` | Regional/global/aftermath, separate phase clocks and national contamination, ratio/marker/completion states, compact global deaths, breakup tooltip and long status strip. |
| Event 005 focus art — two restored registries | Representative old and later focuses (e.g. AAX old/new pair), base/shine states and UWR/KMB; old 1,012 mappings and later 718 mappings are documented in the crosswalk. |
| Event 012 fictional leader portraits | Pan, Gorilla Kingdom, The Green, Living Rivers, Stoneborn and Ancient Hosts; verify the six original DDS consumers, retaining the separate RSA portrait. |
| Restored category/idea/report art — Events 016/025/028/031, Famine/Migration and Independence Wave | Verify original same-role art, retained genuinely new discovery/evolution/famine-only content, restored per-category icons and protected original Migration picture. |
| Disease Containment Board | It must remain absent: category detached, header/board always invisible and no opener button/click hook. Inert strings and sprites passed source/decode dependency checks. |

Record screenshots, actual visible defects and any fixes in this handoff's existing live-verification report.
Do not recreate a Windows test session for these checks.
