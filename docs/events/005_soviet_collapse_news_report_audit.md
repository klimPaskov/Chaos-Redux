# Event 005 Soviet Collapse News and Report Audit

Audit date: 2026-05-21

This audit maps the final clean merged package's Part 7 news/report requirements to current source evidence. It does not close the full Event 005 goal; it only covers the news/report presentation surface.

## Source Evidence

| Requirement | Current implementation | Source evidence | Status |
| --- | --- | --- | --- |
| Local league formation news | Baltic, Caucasus, Central Asian, Eastern Buffer, and Steppe Federation formations use news events, not super-events. | `chaosx.nr5.30`, `.31`, `.32`, `.35`, `.36`; `soviet_collapse_found_*_league`, `soviet_collapse_found_terminal_*_league`, `moldova_soviet_collapse_alliance_not_union`, and `soviet_collapse_report_steppe_federation_news`. | source_pass |
| Internal republic release news | Internal republic setup fires `chaosx.nr5.95` for Karelia, Komi, Crimea, Tatarstan, Bashkiria, Far Eastern Republic, Yakutia, Buryatia, and Tuva. | `soviet_collapse_apply_breakaway_setup_package` gates `soviet_collapse_internal_republic_news_reported` by internal tags and fires `news_event = { id = chaosx.nr5.95 }`. | source_pass |
| Komi or Karelia sovereignty | Covered by the internal republic news hook plus MTTH release cause reports. | `KAR` and `KOM` appear in the internal republic news tag list and progressive release selector. | source_pass |
| Volga republic formation | Tatarstan and Bashkiria get the internal republic news hook; Idel-Ural has its high-chaos notice event. | `TAT` and `BSK` in `chaosx.nr5.95` hook; `chaosx.nr5_custom.30` for Idel-Ural. | source_pass |
| Far Eastern Republic revival | Progressive Far Eastern Republic receives internal republic news; high-chaos Far Eastern revival has a custom notice event. | `FER` in `chaosx.nr5.95` hook; `chaosx.nr5_custom.16` for the high-chaos Far Eastern package. | source_pass |
| Siberian Regional Authority emergence | High-chaos Siberian authority uses a custom notice event. | `chaosx.nr5_custom.17` and `soviet_collapse_siberian_distance_command_failed` spawn path. | source_pass |
| Republics joining local leagues | Regional invitation now fires a news event before the existing guarantee report. | `soviet_collapse_apply_regional_faction_invite` fires `chaosx.nr5.48` and `chaosx.nr5.38`. | source_pass |
| Local leagues declaring war | Defensive-war call uses a normal report event rather than a super-event. | `soviet_collapse_call_regional_league_defensive_war` fires `chaosx.nr5.43`. | source_pass |
| Major foreign recognition events | Foreign recognition aid now fires public news once per recognized republic. | `soviet_collapse_apply_foreign_recognition_aid` sets `soviet_collapse_foreign_recognition_news_reported` and fires `chaosx.nr5.49`. | source_pass |
| MTTH release warnings | Progressive release cause reports explain why local authority failed before calling the release helper. | `chaosx.nr5.130` through `.137`, selected by `soviet_collapse_fire_progressive_release_event`. | source_pass |
| One-member liaison offices | Single regional republic league-preparation now reports that the office is preparatory, not a league. | `soviet_collapse_maybe_report_single_republic_liaison_office` fires `chaosx.nr5.45` only when a regional member exists without quorum. | source_pass |
| Failed missions and mission outcome reports | Failed objective families fire short crisis report events. | Authority/legal `.10`, command `.11`, rail `.12`, depot `.13`, foreign `.14`, cleanup/backlog `.15`, settlement `.16`. | source_pass |
| Sponsor influence changes | Faction and patron pressure reports cover invitations, coordination, mediation, goal success/failure, war quotas, withdrawal, and foreign recognition. | `chaosx.nr5.38`, `.39`, `.40`, `.41`, `.42`, `.43`, `.44`, `.49`. | source_pass |
| Puppet release aftermath | Terminal subject freeing now fires a report when Soviet republican subjects are cut loose. | `soviet_collapse_terminal_subject_freed_report_pending` is set by terminal `set_autonomy = autonomy_free` branches and consumed by `chaosx.nr5.46`. | source_pass |
| Dynamic starting unit explanations | First breakaway setup now reports the dynamic military package logic once to the Soviet player. | `soviet_collapse_dynamic_unit_report_seen` gates `chaosx.nr5.47` after emergency guard and field-brigade creation. | source_pass |
| Balance-relevant crisis shifts | Mission failures, release causes, league goals, war quotas, sponsor recognition, and terminal subject release are visible through report/news events. | `chaosx.nr5.10` through `.16`, `.38` through `.49`, `.95`, `.130` through `.137`. | source_pass |
| Retired super-event achievement hooks | Achievements no longer depend on retired Free Republics' League or Steppe Federation super-event flags. | `chaosx_ach_former_union_of_everyone_else` now checks `soviet_collapse_free_republics_league_announced`; `chaosx_ach_southern_cascade` now checks `soviet_collapse_steppe_federation_news_fired` plus Basmachi, Turkestan, or Alash endgame flags. | source_pass |

## Super-Event Boundary

No ordinary local league formation, ordinary republic release, internal republic release, recognition event, liaison office, or local-league war call uses a super-event helper. These are handled through news/report events and event-log content. Union Unmade and rare high-chaos transformations remain the super-event surface.

## Remaining Goal Scope

This audit closes the news/report coverage gap at source level only. The full Event 005 goal remains open because other ledger rows still track partial high-chaos package art, individual country-package rows, AI strategy audit breadth, and live-session validation surfaces.
