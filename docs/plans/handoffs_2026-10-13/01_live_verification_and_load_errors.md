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
| resources_found_field_window — `interface/018_resources_found.gui` | Active/closed/selected/exhausted fields; original identity/status/metric positions and all five scaled hitboxes; long identity/resource strings and inherited dense status strip. |
| `black_plague_response_category_window` — `interface/020_black_plague_response.gui` | Historical 470×272 picture/checkbox progress, Medical Reserve and International Response; zero, unorganized and organized capacity states, preserving their guards. |
| `acid_rain_world_window`, `acid_rain_category_inlay` — `interface/033_acid_rain.gui` | Regional/global/aftermath, separate phase clocks and national contamination, ratio/marker/completion states, compact global deaths, breakup tooltip and long status strip. |
| Event 005 focus art — two restored registries | Representative old and later focuses (e.g. AAX old/new pair), base/shine states and UWR/KMB; old 1,012 mappings and later 718 mappings are documented in the crosswalk. |
| Event 012 fictional leader portraits | Pan, Gorilla Kingdom, The Green, Living Rivers, Stoneborn and Ancient Hosts; verify the six original DDS consumers, retaining the separate RSA portrait. |
| Restored category/idea/report art — Events 016/025/028/031, Famine/Migration and Independence Wave | Verify original same-role art, retained genuinely new discovery/evolution/famine-only content, restored per-category icons and protected original Migration picture. |
| Disease Containment Board | It must remain absent: category detached, header/board always invisible and no opener button/click hook. Inert strings and sprites passed source/decode dependency checks. |

Record screenshots, actual visible defects and any fixes in this handoff's existing live-verification report.
Do not recreate a Windows test session for these checks.

