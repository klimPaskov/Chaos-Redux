# Event 025 catalog changes pending

These changes belong in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, sheet `Events`, row 26 (ID `25`, Alien technology in Antarctica).
They are staged here because the workbook and its CSV exports are owned by the catalog worker in the shared tree.
After applying them to the workbook, run `python .tools/export_event_catalog_csv.py` from the mod root.

| Cell | Column | Current value | New value | Source of the wording |
| --- | --- | --- | --- | --- |
| `C26` | Details | A race for alien technology in Antarctica can unlock advanced jet research for the country that secures the site. | Impossible readings beneath the Antarctic ice draw governments into a race across six field sectors. Each expedition keeps a private record of its route, camp, survey evidence and fragments, while five independent hazards can change the race. One expedition secures the primary alien-derived result; every other expedition keeps only what it verified. | Premise paragraph of `chaosx_nr25_event_details_unfired` (and the other three Event Details states) |
| `D26` | Evo I | (empty) | The buried transmitter answers field instruments in a patient, non-human pattern, and it grows louder week by week. Strong pulses can burn out radios, drain a camp, injure field crews, scramble survey records or show rivals where an expedition works; shielded instruments and distant listening posts blunt them. The signal adds danger to the race without removing the possibility of recovery. | `chaosx.nr25.evolution.active_signal.body` (Active Signal) |
| `E26` | Evo II | (empty) | Movement has been observed beyond the wreck's outer shell. It may be a mechanism, a biological response, or an echo in the snow, but the field teams must account for it while the recovery race continues. | `chaosx.nr25.evolution.something_survived.body` (Something Survived) |
| `F26` | Evo III | (empty) | Armed patrols and emergency claims are joining the expedition flags. The local crisis can still be contained through rescue, interception, or a demilitarised compact without forcing a global war. | `chaosx.nr25.evolution.militarised_antarctica.body` (Militarised Antarctica) |
| `G26` | Evo IV | (empty) | The alien-derived wreck is shedding hot fragments into six distinct sectors. Each field is evidence and hazard at once, and careful recovery can preserve the primary race. | `chaosx.nr25.evolution.wreck_breaking_apart.body` (The Wreck Is Breaking Apart) |
| `H26` | Evo V | (empty) | The recovered system is beginning to anticipate its operators. Dependence remains measurable and recoverable, but each custody decision changes the relationship between human judgment and the alien-derived interface. | `chaosx.nr25.evolution.technology_changes_users.body` (The Technology Changes Its Users) |
| `M26` | Status | To Be Reworked | Needs Testing | Event 25 is in the default-enable allowlist after the 2026-10-04 completion pass; live validation is still required. |

`Event Name` (`Alien technology in Antarctica`), `World-End Scenario` (none), `Type` (`Major`), `Chaos level` (`1`) and `Cluster ID` (none) need no change.
The evolution order follows the Evolutions log tiers one to five (agent decision D13).
The fourteen Event 025 achievements have no catalog column; they are registered in `common/achievements/chaos_redux_achievements.txt` (agent decision D9).

Disposition: `accepted and queued`, accepted under the user's grant of full implementation authority to this workstream; queued because the workbook is outside this owner's write scope.
