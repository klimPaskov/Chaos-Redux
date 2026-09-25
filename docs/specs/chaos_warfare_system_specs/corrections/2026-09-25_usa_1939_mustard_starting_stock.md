# U.S. 1939 mustard starting reserve

Acceptance basis: the user's 2026-09-20 CBRN overhaul requests separate sourced 1936 and 1939 starts and offensive stocks calibrated against operation costs and documented program maturity. This correction is a parent-selected gameplay calibration within that scope, not an archival inventory claim.

The [U.S. defence history](https://www.denix.osd.mil/rcwmprogram/history/) records Edgewood Arsenal's 1937 rehabilitation of its mustard-production line and additional output that year. The history does not define the mod's abstract `mustard_agent_lot_1` unit or prove how much remained in either bookmark. Therefore historical tonnage is not converted into lots, and no starting HOI4 production line is granted.

| Bookmark | U.S. mustard lots | Cylinder at 40 | Projector at 70 | Artillery at 120 | Armored at 80 |
| --- | ---: | ---: | ---: | ---: | ---: |
| January 1936 | 240 | 6 | 3 | 2 | 3 |
| August 1939 | 320 | 8 | 4 | 2 | 4 |

Each raid-equivalent column is `floor(lots / route cost)` considered alone; the same lots cannot fund all columns simultaneously, and the operations also require their other equipment, policy, intelligence, and assigned formation. The 1939 value stays below the next-lowest major mustard reserve, Italy's 360 lots. The 80-lot increment is a deliberately modest gameplay reflection of the documented intervening production, not a claim that 80 lots equal the reported historical output.

`common/script_constants/startup_history_constants.txt` owns both values. `chaosx_startup_grant_usa` selects the 1939 value after 31 December 1938 and makes one existing mustard-stock grant. Other countries' offensive lot values remain unchanged because this bounded research found no defensible country-and-agent conversion or accepted factory-line calibration. The 1939 U.S. phosgene knowledge grant remains separate and supplies no phosgene lots.

Source-level review must verify one grant per bookmark, the date boundary, both constant references, and the raid-equivalent arithmetic. Country inventory in the live engine and the other historical industrial differences remain for later evidence; this correction does not close the full CBRN historical-start requirement.
