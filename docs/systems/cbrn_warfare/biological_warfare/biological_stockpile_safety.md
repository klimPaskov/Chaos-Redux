# Biological Stockpile Safety

## Purpose and scope

Biological payloads are national equipment stock, while the safety system keeps one internal pointer to an exact owned arsenal state for facility risk, accident location, and hostile capture accounting. Arsenal designation and raid staging are not player actions. Biological deployment and captured-facility recovery use their native raid routes.

This document describes the current source behavior. Source inspection does not establish live-game behavior or balance.

## Arsenal registration and repair

The four biological special projects register their first qualifying exact facility through `facility_state_effects` when the project supplies that state context. Registration stores `bio_stockpile_safety_arsenal_state` on the owning country and `bio_stockpile_safety_arsenal_actor` on the state, then starts `cbrn_bio_safety.1`. The source has no active `bio_designate_national_biological_arsenal` decision or matching localisation. If a scripted project completion supplies no facility state and no previous designation history, this source path does not establish an arsenal pointer or schedule its monitor.

On a due monitor event, `bio_stockpile_safety_reselect_arsenal_if_needed` checks whether a country with prior verified designation history has lost a valid pointer. It clears the old designation and may select one random owned, controlled, eligible state with an operational `biowarfare_facility`. This is a bounded internal repair in the affected country, not a player relocation action. If no candidate exists, the cleared pointer has no monitor due date and the event does not schedule another check through that path. The state selection is random among eligible candidates; the source applies no core-state, infrastructure, outbreak-avoidance, or frontline ranking.

`bio_stockpile_safety_arsenal_pointer_is_valid` requires the state to exist, remain owned and controlled by the recorded country, be eligible for the ordinary pathogen route, and retain a positive facility level. It does not require an operational facility level. A damaged or disabled facility whose total level remains positive can therefore stay the current pointer and contribute to the risk calculation.

## Risk snapshot

`bio_stockpile_safety_refresh_risk_band` samples the four live payload equipment counts, weighted stock for risk, Biosecurity, three safety technologies, applicable designer traits, and the exact facility's total, damaged, and operational levels. It also reads exact-state recent bombing, sabotage, and handling context. The bounded `bio_stockpile_safety_risk_score` is a private 0–100 calculation. Band assignment uses explicit trigger conditions in this order, so a score alone does not select a band.

| Band | Current source gate |
|---|---|
| Critical | Effective safety below 20, extreme weighted stock, any damaged facility level, or explicit exact-state sabotage. |
| Dangerous | Effective safety from 20 to below 40 together with large weighted stock, recent strategic bombing, or operational facility level below one. |
| Controlled | Effective safety at least 70, weighted stock below the high threshold, no damaged facility level, no recent bombing, and no explicit sabotage. |
| Strained | Valid risk context that meets none of the preceding gates. |

The thresholds and incident weights live in `common/script_constants/biological_stockpile_safety_constants.txt`. The score and band variables are internal script state; the inspected localisation and idea definitions do not establish a player-facing stockpile risk display or dedicated risk-band spirit.

## Targeted monitor and ordinary accidents

The project registration schedules one hidden country event after the initial delay. `cbrn_bio_safety.1` checks `bio_stockpile_safety_monitor_due_day`, attempts bounded pointer repair, refreshes a valid arsenal's risk snapshot, and schedules another event at the configured 30-day interval. The repair helper does not queue a second event. A stale event that arrives before its recorded due day does not enter the resolution block. There is no all-country daily, weekly, or monthly stockpile pulse in this subsystem.

With a valid pointer, positive sampled payload stock, no pending accident notification, and no ordinary-accident immunity, the event uses a `random_list` for incident versus no incident. The source-defined incident/no-incident weights are 1/9999 for Controlled, 1/199 for Strained, 4/96 for Dangerous, and 15/85 for Critical. It then selects an available agent from its live count after excluding that agent during its accident cooldown and selects one of five severities: Contained Incident, Laboratory Contamination, Local Outbreak, Major Domestic Outbreak, or International Exposure. The read-only probability audit could not resolve those variable-weight stages into verified overall accident probabilities.

An ordinary accident debits the exact matching national payload stock once and records the agent, severity, date, loss, and evidence against the country and designated state. A contained incident produces no outbreak seed. A non-contained incident enters `bio_lifecycle_dispatch_seed` as a domestic laboratory accident, leaving incubation, detection, contamination, medical load, deaths, evidence, attribution, spread, and cleanup to the shared biological lifecycle. The pending notification flag blocks another accident roll until the incident context is cleared.

Fail-Safe Containment Facilities or the matching designer trait can suppress an ordinary accident only while the exact arsenal has no explicit sabotage and no recent bombing. This immunity trigger does not suppress captured-facility releases, deliberate raids, or doomsday release.

## Captured-facility recovery

`on_state_control_changed` passes its exact changed state to the captured-facility helper. On the first hostile capture of the designated arsenal, that helper moves the original custodian's currently unallocated four-agent national payload counts into the captured state's ledger and records the original custodian and current controller. A targeted state event handles an unresolved facility hazard; original-custodian recapture restores the remaining ledger and rebinds the old pointer only when no replacement pointer exists. The exact transfer and release paths are documented in [Captured Biological Facility Recovery](captured_biological_facility_recovery.md).

The controller resolves the site through `bio_facility_secure_preserve_raid` or `bio_facility_destroy_safely_raid`, both native land raids in the Biological Raids category. The selected formation requires a Biosecurity Assault Detachment, and its assigned leader's consolidated CBRN Medical and Biosecurity Section is checked by a character-scoped success factor. Their target, formation, equipment, success, outcome, and AI gates are in `common/raids/biological_facility_recovery_raids.txt`. A capture-source accidental release enters the shared ordinary lifecycle with the exact state ledger as its debit proof. Native target presentation for an enemy-owned state already controlled by the actor remains a documented engine scenario limit, and no decision fallback is approved.

## AI and asset wiring

The internal arsenal repair has no `ai_will_do` ranking; it randomly selects one eligible state. The two recovery raids have separate `ai_will_do` factors: defensive, democratic, and advanced-containment conditions favor preservation, while unrestricted policy, high state hazard, or weak containment favors destruction. These factors show scripted preference, not verified normalized choice probabilities. Retired player-designation costs and AI tuning have no constant groups; the legacy `selected_state` pointer-source enum remains because captured-facility restoration still accepts an older registered pointer.

There is no active arsenal designation sprite consumer. The recovery raid sprites `GFX_raid_type_icon_bio_facility_secure_preserve` and `GFX_raid_type_icon_bio_facility_destroy_safely` are registered in `interface/chaosx_raids.gfx` and point to the corresponding DDS files under `gfx/interface/raids/stage_7_biological_warfare/`. The shared Biological Raids category and unit marker use their existing `gfx/interface/military_raids/map_icons/` art. The stockpile safety script adds no risk-band sprite or national-spirit icon.

## Validation boundary

Source inspection confirms the named definitions, call sites, and registered raid sprites. Read-only HOI4 MCP event inspection and rendering returned partial source-linked artifacts for the targeted monitor; large-workspace helper and lifecycle projections were deferred. Neither that result nor this document proves live-game raid target presentation, accident odds, AI choice probabilities, or a successful end-to-end capture scenario. The parent owns final integration and the user owns live-game validation.
