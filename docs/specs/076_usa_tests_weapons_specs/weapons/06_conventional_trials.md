# 06 · Conventional trials

## Common damage calibration

Each profile acts on current real targets in its selected state. The casualty bands below are proposed game-balance values expressed in basis points of the state's current civilian population. One basis point is 0.01 percent. They are not historical casualty estimates or real-world weapon performance. The exact helper contract and native damage units must be verified before implementation.

A selected point within a band depends on the disclosed intensity and the state target's exposure class. Snapshot the band at acceptance. At impact, apply it to the actual surviving population and clamp only to the technical limits of the population owner. Do not impose a special low cap for weak minors.

| Family | Baseline civilian-loss band | Physical emphasis | Normal experience |
| --- | --- | --- | --- |
| Artillery shells | 25 to 75 basis points | Infrastructure, forts, nearby military or industrial targets | Army |
| Heavy artillery | 50 to 150 | Strongpoints, supply facilities and concentrated structures | Army |
| Tactical air bombardment | 50 to 150 | Air bases, military factories, anti-air and transport | Air |
| Strategic bombing | 100 to 300 | Civilian and military industry, infrastructure and rail targets | Air |
| Incendiary bombing | 100 to 250 | Industrial and inhabited districts, supported fire aftermath | Air |
| Prototype rockets | 50 to 200 | Impact installations, transport and a larger miss footprint when supported | Air |
| Mature conventional missiles | 100 to 300 | Owner-selected impact area and actual installations | Air or delivery-owner branch |
| Tank and anti-tank trials | 5 to 25 | Land targets, forts, military facilities and supported deployed units | Army |
| Aircraft weapons | 10 to 50 | Air bases, military facilities and valid local targets | Air |
| Experimental explosives | 50 to 150 | A concentrated structural target with actual destruction | Army or owning project |
| Naval guns | 25 to 100 | Coastal forts, ports and exposed coastal installations | Navy |
| Torpedoes | 5 to 25 where a populated coastal area is affected | Verified naval target, port or coastal owner variant | Navy |

For illustration, 100 basis points applied to a state containing two million civilians requests 20,000 civilian losses. If only 12,000 people can actually be removed under the technical contract, every downstream total uses 12,000. A test on an empty military target may still have military effects, but it does not invent civilian casualties to meet a flavor sentence.

## Structural damage levels

Use three physical profiles. A contained trial damages one or two relevant existing installations by a substantial amount. A bombardment profile damages several relevant installations and can remove one existing building level outright where the provider supports destruction. A heavy profile damages the relevant complex widely and can remove multiple levels. Counts are structural design values, not requirements to turn every test into a state-wide wipe.

Repairable damage must use the actual building-damage route. Permanent loss must reduce actual built levels through a supported effect. If a building is absent, do not create it simply to destroy it. Select another present relevant target or report that component as zero.

Each profile records the building type, before state, applied damage and actual lost levels. Railways, supply hubs, naval bases and provincial forts require their own correct scope. A generic `damage_building` call cannot be represented as destruction of all transport links in a state.

## Artillery and heavy artillery

Ordinary artillery trials concentrate fire on a selected land range that includes useful targets. Their American result concerns shell performance, fire-support practice, artillery manufacture or the current artillery technology. Heavy artillery shifts the useful target toward fortified positions and transport or industrial structures.

Evolution I introduces prolonged bombardment as a larger variant. It schedules several physical pulses within one accepted experiment. All pulses share the job but have distinct receipt keys. The announced maximum intensity and target area remain fixed. The analysis reward is paid once after the last pulse, not once per shelling day.

Military effects require units to be physically present within the resolved area. Absent units cannot suffer losses through a national reserve deduction. Player movement before impact may save a formation, while buildings and civilians remaining inside the range still receive the full profile.

## Air bombardment and incendiaries

Tactical trials prioritize military installations and transport supporting them. Strategic trials emphasize actual industrial capacity and associated routes. Aircraft-gun and bomb-development variants use their own current equipment and research categories instead of granting every possible air bonus at once.

Incendiary trials may pass a fire request to an existing fire or disaster owner only through a neutral adapter that supports caused fires. Event 076 retains responsibility. It must not fire the Natural Disasters random event or borrow an unrelated private disaster state machine. Without a supported fire adapter, implement the specified direct incendiary damage and mark the continuing-fire variant unavailable. Do not claim a spreading fire from a static state modifier.

A real native bombing route can feed shared strategic-bombing casualty detection. That creates an accounting collision risk. The integration must either consume the owner's existing receipt or exclude that same strike from the generic detection pass. An extra Event 076 population transaction is not allowed for a loss already applied by native or shared bombing logic.

## Rockets and missiles

Prototype rockets enter only with a real research or experimental provider. Mature missile launches use the missile owner's stock, custody, target and launch contract. A successful delivery-system experiment rewards rockets, guidance, delivery research or the associated doctrine.

A guidance-failure variant is available only when the delivery owner can resolve an actual alternate impact and report its casualties. The owner must preserve the accepted test's allowed footprint or treat an impact outside it as an accident with separate condemnation. The event does not invent another independent missile accident engine.

An experimental launch that fails before any physical test produces no successful-test package. Where a real owner reports useful partial test data, a bounded partial-development outcome can be recorded as such. It cannot be counted as a successful impact for achievements or the nuclear super-event.

## Armor, anti-armor and explosives

Armor and anti-armor families distinguish the tested tank gun, armor system and anti-tank weapon. They target compatible installations or deployed formations and reward the corresponding branch. Reliability improvements must use a supported equipment or design route. An unsupported global reliability modifier is not acceptable shorthand.

Explosive trials focus on an actual structural target. Destruction of a fort, damaged factory district or supply installation gives the test a different military purpose from indiscriminate air bombardment. The provider's American result follows the actual project or land-weapons field.

## Naval weapons

Naval guns can conduct an offshore bombardment of a valid coastal state through a supported provider. Torpedo trials require a separate valid naval-target or coastal-installation contract. Do not sink ships that happen to belong to the victim but are on the other side of the world.

A ship loss must identify the affected naval unit through the owning effect's actual result. Equipment loss and crew casualties remain separate accounting fields. Port destruction, reduced naval-base levels and repairable port damage are distinct outcomes and must be recorded accurately.

Naval rewards concern Navy Experience, torpedo or gun research, relevant naval doctrine, or verified same-family production development. They do not become Army Experience simply because the victim's damaged state is on land.
