# Event 012 achievement rows 1-6 patch handoff (2026-08-10)

## Scope

This tranche tightens the six first Event 012 achievement contracts and adds the authored Archive Disposition operation required by row 5. The former unregistered Event 012 triggerable-scenario route and its forced-scenario recorder were retired; rows 1 and 4 retain no-route structural invariants, while the four-actor nonhuman-rights ledger remains authored separately.

## Changed files and identifiers

| File | Identifiers | Evidence / behavior |
| --- | --- | --- |
| `common/scripted_effects/012_africa_achievement_effects.txt` | `africa_achievement_record_action_start`, `africa_achievement_record_full_action`, `africa_achievement_record_action_outcome`, `africa_achievement_record_last_convoy_war_settlement`, `africa_achievement_record_protection_war_settled` | Row 1 protection receipts require current-generation protected relationships and settled protection wars. Row 2 records the below-20%-remaining convoy candidate and only completes after the authoritative 180-day survival plus peace/victory settlement callback. The generic `break_intervention_coalition` proxy no longer writes row 4 victory evidence. Terminal high-chaos action resolution writes its exact row-3 DQ. |
| `common/scripted_effects/012_africa_achievement_effects.txt` | `africa_achievement_record_scramble_settlement`, `africa_achievement_record_archive_restoration`, `africa_achievement_capture_africa_is_one_snapshot`, `africa_achievement_record_congress_agenda_completed`, `africa_achievement_refresh_congress_member_roster`, `africa_achievement_refresh_survival_windows` | Row 4 positive evidence is written only by the Scramble aftermath/close settlement owners after defensive-war victory and terminal settlement; the settled core snapshot writes the exact partition DQ when a marked African core is foreign-ceded. Row 5 maintains a live exact restored roster and blocks stale-generation/destroyed members. Row 6 records all nine full agenda receipts, captures the exact twelve-plus chair roster, and treats suspension as retention rather than expulsion. |
| `common/scripted_effects/012_africa_achievement_effects.txt` | `africa_achievement_record_archive_disposition_safe`, `africa_achievement_record_archive_disposition_sold`, `africa_achievement_record_archive_disposition_suppressed`, `africa_achievement_pay_archive_safe_disposition`, `africa_achievement_pay_archive_destructive_disposition`, `africa_achievement_clear_archive_disposition_target` | Adds the bounded row-5 archive operation. Public/custodial custody sets a target receipt and preserves evacuation/restoration evidence. Sale and suppression set exact target flags plus `africa_achievement_archive_sold_or_suppressed` and specific global ledger flags. Costs are paid from per-archive host variables; the short-lived selected event target is cleared after execution. |
| `common/scripted_triggers/012_africa_achievement_triggers.txt` | `africa_achievement_archive_disposition_window_is_open`, `africa_achievement_archive_disposition_target_is_valid`, `africa_achievement_can_pay_archive_safe_disposition`, `africa_achievement_can_pay_archive_destructive_disposition`, `africa_achievement_archive_destructive_ai_profile`, rows 1-6 completion triggers | The decision category is open only before `africa_is_one` and only when a current-generation evacuated target exists in maintained `africa_relationship_countries`. Target validity is current-generation, not capitulated, evacuated, and not already disposed. Row 5 rechecks every exact restored roster pointer at achievement time for an independent or autonomous-federal relationship. AI destructive choices are zero outside explicit high-chaos, military/authoritarian, or coercive profiles. |
| `common/script_constants/012_africa_achievement_constants.txt` | `africa_achievement_archive_disposition`, `africa_achievement_archive_disposition_cost`, `africa_achievement_archive_disposition_ai` | Centralizes disposition enum, base/per-archive PP/CP costs, base/per-archive cooldown days, and safe-vs-destructive AI weights. |
| `common/decisions/012_africa_decisions.txt` | `africa_archive_disposition_category`, `africa_archive_publish_custodial_register`, `africa_archive_sell_external_archive`, `africa_archive_suppress_archive_register` | Three mutually exclusive target decisions use `target_array = africa_relationship_countries`, dynamic custom costs, dynamic `days_re_enable`, exact tooltips, and the matching scripted effects. |
| `localisation/english/012_african_union_l_english.yml` | Category, decision names/descriptions, dynamic cost keys, and effect tooltips for the three Archive Disposition decisions | Player-facing text explains the safe route, explicit sale/suppression DQs, dynamic reserves, and the pre-Africa-is-One window. |

`common/on_actions/012_africa_world_order_on_actions.txt` now calls the target-owned convoy/protection settlement writers from both `on_peace` and `on_peaceconference_ended`, covering negotiated independence as well as formal conferences without introducing a recurring world scan.

## Dynamic ledger details

`africa_achievement_initialize_normal_host` initializes safe custody at 20 PP/5 CP/45 days and destructive disposition at 10 PP/3 CP/90 days. Each full current-generation archive evacuation adds 5 PP/1 CP/5 days to the safe route and 3 PP/1 CP/10 days to the destructive route on the maintained host scope. The decision UI displays the host variables and pays them through dynamic temporary spend values; no static `cost` field substitutes for the ledger.

## Validation performed

- Read the required offline Paradox wiki pages and vanilla script/effects/triggers/dynamic-variable documentation before editing.
- Inspected existing Event 012 target-array decisions and vanilla target-decision precedents (`AFG.txt`), and used the existing `africa_relationship_countries` roster pattern.
- Source-level searches verified all new decision IDs, helper IDs, localisation keys, and old generic `break_intervention_coalition` achievement writer removal.
- No HOI4 process was launched.

## Blocker / follow-up

The installed callable tool surface in this session did not expose the required `hoi4.event_inspect`, `hoi4.event_render`, or `hoi4.probability_inspect` routes. Therefore no engine-backed event/decision/probability evidence is claimed here. Parent review should run the Event 012 decision/event inspection and the mandatory probability baseline/compare pass when the MCP routes are available, especially for the dynamic `days_re_enable = var:` fields and AI profile modifiers.

No fallback or proxy was used for the Archive Disposition operation. The Scramble writer remains authoritative-only, and row 5 sale/suppression is an explicit authored decision rather than a derived or fake flag.

## Triggerable-scenario route retirement

The unregistered Event 012 triggerable-scenario route was removed from the shared scenario registry, view rebuilds, selector, launch dispatch, and launch eligibility trigger. The placeholder `chaosx.triggerable_scenarios.11` event and its three GUI localisation keys were retired. Exact files changed for this cleanup are `common/script_constants/chaosx_triggerable_scenarios_constants.txt`, `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`, `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`, `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`, `events/chaosx_triggerable_scenarios.txt`, and `localisation/english/chaosx_gui_l_english.yml`. The former forced-scenario DQ checks and definition were removed; rows 1, 4, 27, and 44 retain documentary structural invariants only because no Event 012 triggerable scenario exists.
