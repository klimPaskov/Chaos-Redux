# Camps: gameplay gates, window redesign and decision trim, 10 October 2026

Disposition: implemented.
Acceptance basis: the user's 10 October brief, items 3.3 (camp and genocide paths open on gameplay conditions, dates only steer AI timing) and 4.2 (redesign the Camps and Repression window, remove its debug look), plus the coordinator's task to trim the camp decisions.
No game was launched; live behaviour, AI timing and save persistence remain user-validated.

## 1. Date gates replaced by gameplay conditions

New country triggers in `common/scripted_triggers/camp_administration_country_triggers.txt`: `camp_admin_ger_war_of_conquest`, `camp_admin_jap_china_war`, `camp_admin_country_major_war`, `camp_admin_country_postwar_reckoning` and `camp_admin_census_campaign_age_over`.

| Path | Before | Now |
| --- | --- | --- |
| Auschwitz site (Kraków setup and decision) | after 1943-05-29 | Nazi Germany fighting a war of conquest, German authority over state 88, a mandate harsher than custody, a development spending ceiling |
| Auschwitz program and Mengele chain gate (`camp_admin_country_mengele_site_gate`, renamed from `..._historical_gate`) | after 1943-05-29 | operating state-88 site under German authority |
| Radical mandate, killing campaign | after 1941-06-21 | war of conquest with an operating site (Germany); China war (Japan); escalation order (Soviet Union) |
| Occupation campaign (`camp_occ_authority_has_campaign`) | after 1937-07-06 / 1941-06-21 | opens through war and mandate (`camp_occ_campaign_can_open`), then persists through flag `camp_occ_campaign_opened` |
| Western, northern and southern origins | per-country calendar list | campaign older than 240 days and German rule over the state older than 45 days (`camp_occ_timing`); Denmark shielded while its own government stands undefeated and at peace with Germany; eastern origins strike as soon as the campaign opens |
| Danish rescue | from 1943-10-01 | once a registered Danish origin is no longer deferred |
| Hungarian order | 15 May to 9 July 1944 | 57 to 113 days after German domination of Hungary during an open campaign (`camp_occ_partner_dominated`) |
| Slovak, Croatian, Bulgarian and Vichy orders | calendar windows | day windows measured from the campaign opening (`camp_occ_partner_table`), same shares |
| Łódź clearance | August to September 1944 | ordered when enemy forces close on state 87 while Auschwitz is a killing destination; lasts 54 days |
| Manual Auschwitz transfer | after 1943-05-29 | Mengele program and campaign prerequisites only |
| WVHA program | after 1942-02-28 | completed Inspectorate program and war |
| Soviet wartime industry / engineer release | 1941-06-21 / 1944-01-01 | war with a major / completed design bureaux plus review |
| Japanese transport, army review, Pingfang | 1937 / 1939 dates | China war; review authorization; Pingfang site flags |
| Archives (all three majors) | fixed postwar dates | at peace or capitulated after reform |
| Census stock steps | calendar steps | war or world tension, then the German campaign age (`camp_admin_census_campaign_days`) |
| British, Raj, US, French, Vichy and Italian civil authorities | calendar windows | war with a major, British subject at war, Spanish Republic fallen (`nationalist_victory`) and France unbeaten, government type; US claims open at peace after authority ends |
| Vichy collaboration records | after 1942-07-01 | Germany's campaign has opened |

Dates remain only as AI timing: German radical mandate (`OR = { has_war_with = SOV date > 1941.6.21 }`), AI Auschwitz setup (`date > 1940.4.26` or war with the Soviet Union) and the civil review AI weights.
Player text that named dates was rewritten: the Kraków requirements, radical mandate tooltip, manual-transfer source tooltip and US claims blocker.

## 2. Window redesign

Reference: `.tmp/camp_repression_ui_2026-10-10/src/camp_admin_reference.png` (gptimage, kept out of LFS), selected by the parent under the 4.2 authorization.

| Reference region | Native implementation |
| --- | --- |
| Title with emblem | `camp_admin_title_icon` (tab-country medallion) and `camp_admin_title` |
| Three tabs with icons | existing tab buttons, centered labels, icons `camp_admin_tab_icon_*`, gold underline marks |
| Three summary cards | containers `camp_admin_card_people/output/deaths`, 48 px icons, label and value; workforce moved into the people tooltip |
| Three policy selectors | existing priority, mandate and spending buttons with title-case labels |
| Two work panels with progress bars | economy and institution panels with eleven-frame meters `camp_admin_economy_meter` / `camp_admin_institution_meter` |
| Two actions | existing national actions; locked variants show the action name in grey |

Locations shows four values (people held, local output, maintenance funded, deaths this month) with icons; workforce, capacity and cumulative site deaths moved into tooltips.
Disabled buttons show the greyed action name instead of "Locked" labels.
Records keeps one cumulative column by cause and frames the history list like the table.
Monthly deaths read in people rather than fractions of a thousand.
Generic reference adaptations: the generated eagle emblem became the existing medallion; dropdown arrows were not added because the selectors open native pickers.

Assets, all in `interface/camp_repression_rework.gfx`, DDS under `gfx/interface/camp_repression/`: `GFX_camp_admin_tab_locations` (32 px), `GFX_camp_admin_icon_people/output/support/deaths` (48 px), `GFX_camp_admin_meter` (300×10, 11 frames), redrawn `GFX_decision_generic_site_inspection` (32 px, transparent), new `GFX_camp_restricted_payload_texticon` texture (20 px gas cylinder, replacing the borrowed doom skull) and redrawn `GFX_idea_sov_republic_fear` (64 px).
Twenty unreferenced ledger sprites and textures were removed, including the ghosted `tab_sites`, `guard_burden`, `rail_burden`, `labor_output`, `evidence_risk`, `reform_pressure` and `population_pressure` from the gfx fix plan group `camp_repression_rework`.
Source PNGs: `.tmp/camp_repression_ui_2026-10-10/` (sheet generated with gptimage, alpha verified).

MCP evidence (hoi4-agent-tools `gui_render`, closedFlags scenarios, 1920×1080, UI scale 1), rendered PNGs in `.tmp/camp_repression_ui_2026-10-10/renders/`: before `cx_admin_before`, `cx_site_before`; after `cx_admin_after`, `cx_site_after`, `cx_records_after`, `cx_crisis_after`, `cx_role_picker_after`.
2560×1440 limitation: the render route ignored the `resolutions` list (output stayed 1920×1080), and a scenario-level resolution was rejected as invalid arguments on both attempts, so the retry limit ended that check.
The window is a fixed 900×540 container centered with `orientation = center` and no resolution-dependent anchors, so at UI scale 1 it draws the same pixels at 2560×1440 with wider margins; this is source review, not a render.

## 3. Decision trim

- Removed `camp_repression_open_ledger` and `camp_repression_close_ledger`: the category's Open button and the window's close button do the same.
- Removed the "Expose/Conceal Network Directives" toggles and their visibility gate on 54 decisions; directives show whenever their own conditions hold.
- `generic_dismantle_detention_network` is AI-only; players close the network from the window's second national action, which runs the same reform. Its name no longer references a missing state scope.
- Japan's two army reviews have distinct names: "Submit Ishii's Unit to Army Review" (Ishii program) and "Put Kwantung Camps under Central Army Review" (institutional review).
- Descriptions over 200 characters on live camp decisions were tightened to state the trade-off.

Remaining bloat, not removed in this pass: about ninety legacy decisions hidden behind `NOT = { has_country_flag = camp_admin_initialized }` (all countries initialize at startup), and four Free French and Belgian crisis choices that need missions only the retired monthly bridge starts.

## Verification

`hoi4.script_validate` returned no findings (partial coverage, argument blocks unchecked) for the edited occupation, partner and country triggers, occupation effects, and generic and colonial decisions.
The occupation and partner source suites under `administration_redesign_2026-09-06/occupation/` still drive the removed calendar dates and were not rerun.
