# Asteroid Incoming, Part 3: Impact Damage and Local Aftermath

Status: implemented, except complete network demolition (blocked) and the Event 029, camp and famine reconciliations (not implemented).
Implemented values live in the constants file; the [tuning matrix](028_asteroid_incoming_tuning_matrix.md) lists them beside their design ranges.

## Resolution contract

The impact resolves as one guarded transaction in `chaosx.nr28.4`.
It plans every main and fragment footprint before changing any state, merges overlaps by strongest profile, processes each state once, measures population before and after, registers only actual deaths, registers craters, damages units, computes dust, and only then sends reports and presentation.
Re-entry guards make a duplicate resolver call a no-op, and a miss or fail-closed course never reaches any damage step.

## Damage profiles

Profiles are ordered by severity (`asteroid_incoming_profile`), so a state reached by several footprints keeps the strongest one.

| Profile | Civilian loss | Local state modifier | Character |
| --- | ---: | --- | --- |
| Main centre (Ring 0) | 100% | Permanent main crater | Complete destruction |
| Catastrophic ring (Ring 1) | 50% | Catastrophic Impact Zone, long | Strongest survivable damage, first in emergency work |
| Major ring (Ring 2) | 25% | Major Impact Zone, medium | Repairable regional disaster |
| Outer ring (Ring 3) | 5% | Outer Shock Zone, short | Visible transport and building damage |
| Fragment centre | 50% | Persistent fragment crater plus Fragment Centre Recovery | Survivable crater site |
| Fragment ring 1 | 25% | Heavy Fragment Damage, timed | Heavy local damage |
| Fragment ring 2 | 5% | Light Fragment Damage, short | Light local damage |

A Ring 1 state must stay usable after major investment and never quietly becomes a second wasteland.

## Buildings

Building loss uses three category shares per profile (industry, logistics, strategic), centralized in `asteroid_incoming_building_loss`.
Logistics and exposed strategic buildings take heavier proportional damage than distant industry, because shock and debris hit the transport network first.

- State buildings lose the rounded share of their current levels.
- Ordinary provincial buildings (forts, ports, facilities, camps, dams, canals, landmarks and the other ordinary types registered in `028_asteroid_incoming_province_triggers.txt`) lose the rounded share per province, processed in ascending original-level cohorts so no province is damaged twice.
  This is per-province rounding by accepted decision (G6): four level-one forts under a 22.5 percent profile each keep their level, while a level-four fort loses one.
- Full-loss profiles zero every matching province.
- Losses clamp to existing levels and never add levels through rounding.
- Railways and supply nodes are network objects that ordinary building operations do not safely cover; the ring profiles damage them through native network damage only.

### Main crater network (blocked)

The brief requires the main centre to lose all buildings.
State buildings and ordinary provincial buildings are removed, and the crater's railways and supply nodes are wrecked with no repair and suppressed by the crater modifier (no building slots, minus 100 percent construction speed) and the wasteland category.
Complete railway and supply-node demolition and cancellation of queued construction or special projects are not proven.
README Open question 1 proposes how to settle this.

## Permanent crater profiles

The main crater is a distinct permanent identity, not radioactive fallout, and borrows no radiation text or icon.
It moves to the wasteland category, carries the permanent `asteroid_incoming_main_crater` modifier and flag, keeps its owner and controller, cannot be rebuilt, and supports no ordinary construction.
Units can still cross it under the wasteland rules, without supply or infrastructure.

A fragment centre keeps its surviving half of population and buildings.
It carries the persistent `asteroid_incoming_fragment_crater` marker and a timed Fragment Centre Recovery burden, and becomes a mineral site under Extraordinary Minerals.

Each crater site carries one persistent material profile (Part 5).

## Civilian population and Deaths

For each affected state, the transaction reads the population, applies the profile share once through the exact state population-loss helper, and records the actual applied value under the matching asteroid Deaths reason.
The main crater targets zero remaining population; other profiles round consistently and never report more deaths than the state held.
Removed population leaves no recruitable-manpower credit.

Deaths reasons distinguish the main impact, the three main rings, the fragment centre, the two fragment rings and rescue failure.
Every entry is civilian; military losses come only from unit damage.

## Continuing rescue-period deaths

Immediate losses are followed by a small monthly loss while a state's rescue burden lasts: catastrophic ring and fragment centre for up to six months, major ring for four, fragment ring 1 for three.
The monthly share is a few hundredths of a percent of the surviving population, capped per month and above a protected population floor.
The medical preparedness stance halves it, and medical and debris work end it early.
It stays far below the immediate losses; its purpose is to make the first emergency actions matter.

## Units in the footprint

Accepted decision (basis: user-granted design authority, 2026-10-05 round 3): every army standing in a processed state is struck where it stands, whoever owns it, through one native `damage_units` call with ratio strength and organisation damage chosen by the state's profile (`asteroid_incoming_unit_damage`).
Damage falls from the main centre (75 percent strength, 95 percent organisation) through the rings, fragment profiles are lighter, and ships are struck only in the main centre and catastrophic ring.
No value deletes a unit, so an army caught in the crater survives broken rather than vanishing.

## Country reports

After all state transactions, the event builds one receipt per affected country: civilian deaths, damaged states, worst profile, whether it held the main centre, fragment centres suffered, destroyed industry and logistics levels, capital outcome and current burden.
A country counts as affected when it owned or controlled a processed state at impact.

Each affected country receives one short plain-text report: `chaosx.nr28.5` when it holds or owns a main-footprint state, otherwise `chaosx.nr28.7`.
The report names the worst-hit state by its profile, gives deaths and the number of damaged states, lists destroyed transport and industrial levels only when there are any, adds the capital sentence only when the government moved or could not move, adds transport losses only for the original target, and ends with the current recovery phase and the most useful recovery order open now.
No zero count prints, and parchment text carries no colour codes.

## Control and ownership edge cases

- When owner and controller differ, losses apply to the state once; the controller receives the operational report and recovery work.
- Deaths attribution follows the shared Deaths contract for the state's civilian country.
- A country that ceases to exist before its report receives none; its totals remain in global history.
- An annexed original target gains no original-target achievement identity for the annexer.

## Local state modifiers and emergencies

| Modifier | Profile | Lifecycle |
| --- | --- | --- |
| Main asteroid crater | Main centre | Permanent |
| Catastrophic Impact Zone | Ring 1 | Long timed |
| Major Impact Zone | Ring 2 | Medium timed |
| Outer Shock Zone | Ring 3 | Short timed |
| Fragment crater marker | Fragment centre | Persistent |
| Fragment Centre Recovery | Fragment centre | Timed |
| Heavy Fragment Damage | Fragment ring 1 | Timed |
| Light Fragment Damage | Fragment ring 2 | Short timed |

A state with an active rescue burden or a catastrophic, major, fragment-centre or heavy-fragment modifier has a live local emergency and joins the emergency list.
A state with only outer-shock or light-fragment damage starts with its emergency resolved.
The monthly recovery pass resolves each listed emergency once its burdens end, so reconstruction opens even where no emergency project was taken.
Recovery decisions shorten these modifiers; the crater markers persist.

## Nuclear separation

The map visual is the only nuclear-adjacent surface, and it is graphics only: two vanilla-cloned explosion entities created by script, with no `launch_nuke`, raid, bomb or nuclear callback ([map presentation](../../events/028_asteroid_incoming/map_presentation.md)).
The transaction creates no nuclear strike record, condemnation, retaliation, fallout, nuclear Chaos ladder entry, nuclear achievement progress, nuclear diplomacy or nuclear Deaths reason.
Dust and Air Cleanliness changes remain an asteroid source in every ledger and tooltip.

## Prior damage

Losses use current population and building levels, so reports state actual losses, and the main crater removes whatever remains.
A compatible natural-disaster modifier already on a state stays; duplicate generic penalties should be consolidated where they overlap.

## Riches Found mine in the footprint

Status: unresolved cross-owner design shared with the [Riches Found package](../029_riches_found_specs/029_riches_found_spec_part_1_core_loop.md); no attributable acceptance found and not implemented on either side.

A registered Event 029 mine can be struck like any other location and never causes a reroll.
Event 029 owns the mine ledger, controller aggregate, concessions, paid projects and evolution aftermath.

- When the main centre becomes a crater, the mine is physically destroyed: Event 029 retires its output and site work and rebuilds the controller's remaining-mine aggregate under its existing diminishing returns and cap.
- The discoverer keeps the original windfall; later capture or release grants no replacement, and no later repair can reopen the mine.
- Destruction is not an evacuation, sealing, reform or completed bargain, gives no Event 029 achievement credit, and cannot pay a Bottomless Account obligation with impact deaths; obligations, settlements and cancellations follow Event 029's terminal policies, refunding only recorded payments.
- Mine casualty effects do not run again for people Event 028 already removed, and already distributed Gold Disease material or national aftermath is not erased.
- Mines in surviving rings and fragment centres keep their identity; Event 029 rechecks works, route and controller before allowing output, and a broken requirement can suspend operation.
  A fragment-crater marker alone does not destroy a mine.
- Neither owner restores shared buildings above their repair baseline or charges the same damage twice.

When Event 029 is absent or disabled, the impact finishes normally, and a later Event 029 refresh must recognize a main crater before restoring mine benefits.

## Camp sites in the footprint (proposed)

Status: proposed by the 2026-10-10 audit, not implemented, needs the camp owner.

The impact already removes concentration camp, extermination camp and gulag buildings in its footprint, but the camp administration ledger is never told.
A registered camp site would then keep detainees who died in the impact, or keep a site that no longer exists.

- Event 028 supplies the state, its profile and the measured civilian loss after the state transaction; it makes no second population change.
- In the main crater, the camp owner retires the site and records its detainees as dead in the impact rather than releasing them.
- In a ring or fragment state, the camp owner reconciles its detainee count against the measured loss, and closes the site through its own terminal seam (`camp_admin_integration_close_site`) only when the building is gone.
- No condemnation or discovery evidence is created by the impact itself.

## Famine request point (proposed)

The famine adapter proposed in Part 1 runs per state inside the transaction, after the measured population loss, for catastrophic-ring, major-ring and fragment-centre states.
It passes the measured deaths as the proven amount and lets the famine owner decide the result.

## Recovery closeout

A country's local recovery ends when all its timed impact-zone burdens have expired or been resolved and no failure window is running.
It then receives one closeout report (`chaosx.nr28.6`), its obsolete emergency actions close, and its national burden or temporary legacy ends; the lasting Regional Economy legacy stays (Part 6).
Closeout never restores the main crater, removes fragment sites, clears global dust or changes crater control.
