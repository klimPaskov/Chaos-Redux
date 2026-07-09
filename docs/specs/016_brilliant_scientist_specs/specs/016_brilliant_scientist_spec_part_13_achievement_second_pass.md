# Event 16 Brilliant Scientist, achievement second pass

Achievement title directions are not final titles. Description directions are not final localisation. This section adds route-specific achievements to the achievement package.

## Second-pass purpose

The core spec covered the core event routes. The second-pass design adds achievements for specific project identities, host restraint, foreign containment, custom GUI mastery, and the final-device race. These achievements should reward difficult play rather than automatic event participation.

## Additional achievement matrix

| Working id | Title direction | Eligible play | Unlock conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| `kruger_public_medicine_without_weapons` | direction for a public medicine and restraint achievement | original host | complete public science, medical acceleration, and peer review path, contain all severe incidents, never approve bioweapon, clone, specimen, or final-device projects | Kruger secedes, any sealed biology weapon path approved | hard | clean laboratory, hospital, and restrained equation motif |
| `kruger_war_office_kept_on_chain` | direction for a military-lab control achievement | host at war | use the military laboratory route, complete at least three military projects, keep Government Leverage high enough to prevent rebellion | surrender authority, failed arrest, Kruger secession | very hard | uniformed guard holding a laboratory key |
| `kruger_audit_every_room` | direction for an inspection mastery achievement | any host | complete audit, staff vetting, chain-of-custody, and prototype inventory before approving any Evolution III sealed project | hidden stockpile discovered after Evolution III, failed audit mission | hard | ledger, key ring, and lab door motif |
| `kruger_no_sealed_city` | direction for a restraint route achievement | any host | reach late Kruger research benefits without ever granting sealed city, private guard, clone, robot, or final-device authority | sealed city memory, private procurement memory | hard | open campus beside guarded gate |
| `kruger_clone_war_won` | direction for clone-route conquest | Kruger country | defeat the former host using clone forces as the main army family and complete the clone lane | robot or specimen lane carries the war through main contribution if tracked | very hard | rows of identical helmets under a lab light |
| `kruger_machine_state_low_manpower` | direction for robot-route mastery | Kruger Machine State | defeat the former host and one major without relying on high manpower losses, complete machine lane | clone manpower route dominates, manpower loss exceeds chosen threshold | very hard | gear and silent soldier silhouette |
| `kruger_specimen_containment_failure` | direction for a specimen route challenge | Kruger Dominion | win a major war with specimen or dinosaur forces and keep at least one escaped-specimen aftermath chain active | world-end fired before victory | hidden extreme | cage door, claw mark, and field map motif |
| `kruger_alien_material_empire` | direction for xenotech route | Kruger Ascendancy | collect alien material, complete xenotech lane, and defeat a country that tried to steal the research | no xenotech memory, theft target never exists | hidden hard | alien metal shard and rifle silhouette |
| `kruger_tomorrow_was_late` | direction for temporal route | Kruger Continuum | use temporal or teleport decisions to win the former-host war within a strict time window after secession | final device fired, ordinary conquest exceeds time window | hidden very hard | broken clock and marching shadow motif |
| `kruger_sabotage_the_equation` | direction for anti-final-device victory | former host or coalition leader | delay or sabotage the final device, then capitulate Kruger before arming completes | final device fires, player used surrender authority | extreme | cracked equation board and special forces icon |
| `kruger_every_country_wanted_him` | direction for foreign attention web | any country involved in foreign reactions | trigger multiple foreign offers, theft attempts, or observer missions and keep Kruger from defecting | Kruger sent away by player at baseline | hard | passport, microscope, and border stamps motif |
| `kruger_defeat_without_panic` | direction for clean containment | former host | defeat or contain sovereign Kruger while preventing mass panic escalation and escaped specimen spread | Mass Panic route triggered by Kruger, specimen aftermath failed | very hard | calm city skyline and sealed laboratory motif |
| `kruger_science_oversight_pact` | direction for aftermath treaty | coalition leader or victor | defeat a global Kruger threat, avoid final device use, and choose treaty sharing or oversight aftermath | quick local defeat, final device fired | hard | treaty folder and laboratory seal motif |
| `kruger_all_facility_memories` | direction for project collector route | host or Kruger | create at least one memory in every major project family and survive until the final confrontation phase | world-end happens before route validation unless achievement is Kruger terminal variant | extreme | ring of project symbols around Kruger portrait |
| `kruger_final_device_stopped_at_the_gate` | direction for last-moment containment | anti-Kruger player | stop Kruger after the final-device race has begun and before the terminal branch fires | final device fires, Kruger never started race | hidden extreme | sealed blast door with equation light |

## Tracking notes

The implementation should track achievement-friendly facts explicitly:

- which route did the host choose at baseline
- which project memory families exist
- whether a memory was created through safe, military, or reckless approval
- whether sealed city, private guard, legal exemption, clone, robot, specimen, xenotech, temporal, or final-device memories exist
- whether Kruger seceded, defected, was contained, was killed, or stayed under the host
- whether the former host defeated Kruger
- which project army families contributed to Kruger’s wars when a reasonable tracking method exists
- whether the final-device race started, was sabotaged, was delayed, was completed, or fired
- whether Mass Panic, escaped specimens, or foreign theft incidents tied to Kruger occurred
- whether the player used stolen prototypes or Kruger-derived foreign decisions

## Achievement icon pass

Each achievement needs a unique 64x64 completed icon. The icon artist should not resize focus or idea icons into achievement icons. Grey and not-eligible variants should follow the achievement workflow after the completed icon exists.

## Priority if implementation is staged

If only some achievements can be implemented in the first coding tranche, prioritize:

1. host restraint achievements
2. Kruger host victory and final-device sabotage achievements
3. one achievement for each major Kruger route that can actually exist in that tranche
4. postwar treaty and global coalition achievements after aftermath systems exist

Do not implement a route achievement before the route has real gameplay, assets, tracking, and AI.
