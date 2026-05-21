# Event 005 Soviet Collapse Evolution Track Audit

Audit date: 2026-05-21

This audit checks the final clean merged Part 2 requirement that ordinary Soviet Collapse stages remain baseline progression and that evolution logs are reserved for mutation tracks.

## Source References

- Spec: `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_2_core_threat_evolutions.md`
- Effects: `common/scripted_effects/005_soviet_collapse_effects.txt`
- Triggers: `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- Constants: `common/script_constants/005_soviet_collapse_constants.txt`
- Scripted localisation: `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- Localisation: `localisation/english/chaosx_gui_l_english.yml`, `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Baseline Progression Audit

The spec identifies first declarations, local obedience crisis, Moscow response, negotiations/isolation/force, MTTH republic releases, local league preparation, Free Republics' League formation, deeper authority collapse, Union Unmade, reconquest, settlement, and rump survival as baseline progression.

Current source evidence keeps those surfaces out of the evolution log:

| Baseline surface | Evidence | Result |
| --- | --- | --- |
| Opening and first-wave rupture | `events/005_soviet_collapse.txt`, `soviet_collapse_setup_initial_crisis_values`, `soviet_collapse_activate_opening_objectives` | Normal event and mission progression; no Event 005 evolution recorder call. |
| Moscow response missions | `common/decisions/005_soviet_collapse_decisions.txt` objective missions call pressure helpers and objective activation helpers. | Mission outcomes alter crisis variables and reports, not evolution log entries. |
| Progressive MTTH releases | `common/mtth/005_soviet_collapse_mtth.txt`, release helpers, and report events `chaosx.nr5.130` through `.137`. | MTTH families are report/release content, not evolution log stages. |
| Local leagues | Formation helpers fire news events `chaosx.nr5.30`, `.31`, `.32`, `.35`, and `.36`; faction-goal reports use `chaosx.nr5.41` and `.42`. | League formation and goals use news/report events, not super-events or evolution logs. |
| Union Unmade | `soviet_collapse_maybe_show_union_unmade_super_event` and terminal helpers route through the allowed major super-event. | Terminal baseline collapse is a super-event, not an evolution log stage. |

Direct search evidence: the only Event 005 `record_events_log_evolution_entry` call in the current source is inside `soviet_collapse_record_high_chaos_successor_evolution`. Baseline mission, MTTH release, local league, and Union Unmade helpers do not call the recorder.

## Evolution Recorder Audit

| Requirement | Source evidence | Result |
| --- | --- | --- |
| Event ID is tied to Soviet Collapse | `soviet_collapse_high_chaos_event_log.event_id = 5`; recorder sets `events_log_evolution_event_id` from that constant. | Complete. |
| Evolution type separates the mutation track | `soviet_collapse_high_chaos_event_log.evolution_type = 5`; scripted localisation maps this to `chaosx.events_log.evolution.type.soviet_collapse_high_chaos`. | Complete. |
| Stage is the mutation milestone, not ordinary crisis stage | Stage constants are successor/mutation IDs such as factory states, Kronstadt, Free Territory, Black Banner, Basmachi, Pale Railway, Tunguska, Iron Commissariat, Red Martyrs, dead-state actors, and Northern Revenant Fleet. | Complete. |
| Tier is display-oriented | Recorder sets tier 4 by default and tier 5 when world-collapse chaos is active; no gameplay gate depends on the displayed tier value. | Complete. |
| Disabled evolutions do not spawn or record | Each `soviet_collapse_spawn_*_if_enabled` helper sets event ID/type/stage before checking `is_current_evolution_enabled`; the record helper also checks `can_soviet_collapse_record_high_chaos_evolution_this_tier`, which includes `is_current_evolution_enabled = yes`. | Complete. |
| One Soviet Collapse evolution log per chaos tier | `can_soviet_collapse_record_high_chaos_evolution_this_tier` blocks recording after `soviet_collapse_high_chaos_evolution_tier_4_recorded` or `soviet_collapse_high_chaos_evolution_tier_5_recorded` is set. | Complete for current Event 005 recorder surface. |

## Spec Track Mapping

| Part 2 mutation pattern | Current implementation evidence | Status |
| --- | --- | --- |
| The Pattern of Secession | Localised as an evolution pattern and represented mechanically by progressive release/MTTH copycat pressure, but not currently recorded as its own separate evolution type. | Covered as baseline pressure and detail text; not a separate active recorder. |
| Depots Choose Flags | Depot pressure, depot missions, `soviet_collapse_depots_choose_flags_branch`, and Pale Railway/fuel/ammunition failure paths feed the high-chaos successor system. | Covered. |
| The Old Underground Wakes | Old movement pressure, old-underground ideas/focuses, Green Army, Free Territory/Black Banner, Basmachi, and Old Great Bulgaria successor stages. | Covered. |
| Red Resistance without Moscow | Union Defense Committee, Security Directorate Zone, Red Martyrs, Iron Commissariat, and dead-state socialist successor stages. | Covered. |
| Foreign Liaison Offices | Foreign appetite, recognition progress, liaison reach, sponsor influence, and foreign corridor mission failures feed crisis pressure and high-chaos eligibility. | Covered. |
| The War of Committees | Factory states, Ural Workers Directorate, rail/city committee successor content, and local authority splinters. | Covered. |
| The Flags Return Incorrectly | Old-name and hybrid-authority successors such as Old Great Bulgaria, Idel-Ural, Alash, and unusual high-chaos state forms. | Covered. |
| The Factory States | CFR and MFR stages are explicit stage constants and setup helpers. | Covered. |
| Ancient Claims Return | Old Great Bulgaria, Alash, Basmachi, Idel-Ural, Don/Kuban/host, and Mountain Republic successor paths. | Covered. |
| The Dead Are Citizens | Dead Soldiers' Congress, Iron Commissariat of the Dead, Red Martyrs, and Northern Revenant Fleet stages. | Covered. |
| The Former Union Becomes Many Worlds | High-chaos successor rollup, terminal release, and event-detail mutation text. | Covered. |

## Localisation Cleanup

The generic Soviet Collapse evolution title keys in `localisation/english/chaosx_gui_l_english.yml` no longer describe baseline stages such as the first break, Free Republics' League formation, or war for the Union. They now use mutation-track language aligned with the Part 2 list. The active Event 005 high-chaos display text remains in `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`.

## Remaining Risk

This audit proves current source separation between baseline progression and active evolution recording. It does not close the broader Event 005 goal because other ledger rows remain partial, especially high-chaos package final art, country-package one-row audits, achievement placeholder art, AI behavior, asset reconciliation, and final validation.
