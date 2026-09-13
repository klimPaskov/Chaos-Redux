# Equipment from Heavens: Delivery Manifest

## Manifest construction

Every delivery is assembled from a curated registry of safe physical stockpile items. The registry is divided by equipment family, technology band, variant rules, quantity role, DLC or designer compatibility, and evolution eligibility.

The manifest generator follows this order:

1. Select delivery magnitude.
2. Select the active evolution pool.
3. Select one anchor family.
4. Select supporting families.
5. Select at least one strategically awkward family when the active pool permits it.
6. Select safe equipment tokens or stable variants for each family.
7. Calculate quantities from magnitude, evolution, and global conflict conditions.
8. Roll nuclear and special-equipment slots when their evolutions are active.
9. Validate the whole manifest before any grant.
10. Save the snapshot and apply the stockpile grant once.

A failed family or token validation rerolls that slot inside a similar value band. It never reduces the package because the recipient is small or technologically backward.

## Anchor, support, and mismatch roles

The anchor family carries roughly half to two thirds of the package's military value. It gives each firing a recognizable identity such as an infantry arsenal, armored park, artillery reserve, air fleet, motor pool, or logistics mountain.

Supporting families make the anchor usable or create a second strategic direction. An armor-heavy package may include trucks, support equipment, anti-air, and trains. An air-heavy package may include fuel-handling equipment only when represented by real stockpile items, trucks, anti-air, and support equipment.

The mismatch role prevents the generator from becoming an optimization tool. It should select something valid but poorly matched to the recipient's geography, force structure, or current war. Examples include amphibious equipment for a landlocked country, naval bombers for a country with few airbases, thousands of trains for an island state, anti-tank guns during a colonial war, or more tanks than the recipient can fuel.

Mismatch logic must not examine recipient capacity to reduce the reward. It only helps choose one awkward family after the package scale is fixed.

## Family count

Suggested starting bands are:

| Active stage | Distinct conventional families | Mismatch families | Advanced or special slots |
| --- | ---: | ---: | ---: |
| Baseline | 4 to 8 | 1 to 2 | 0 |
| Evolution I | 7 to 12 | 1 to 3 | 0 |
| Evolution II | 8 to 14 | 1 to 3 | 0 to 1 nuclear slot |
| Evolution III | 8 to 14 | 1 to 3 | 0 to 1 nuclear slot and 0 to 3 special slots |

A family count is not a pile of near-identical variants. Several rifle models can appear inside one infantry-equipment family. The manifest summary should report the family once and list notable variants in its tooltip.

## Magnitude distribution

Use these as starting weights for probability review:

| Active stage | Enormous | Colossal | Impossible |
| --- | ---: | ---: | ---: |
| Baseline | 60 | 30 | 10 |
| Evolution I | 50 | 35 | 15 |
| Evolution II | 40 | 40 | 20 |
| Evolution III | 35 | 40 | 25 |

The final implementation can tune these values after probability inspection, but it must preserve the ordering. Later evolutions cannot make smaller packages more common.

## Quantity model

Quantity depends on the selected family, magnitude, evolution, and bounded global conditions. It never reads recipient factories, manpower, army size, stockpile shortage, ideology, subject status, or major status.

Useful global factors include current year, number of active major wars, current Chaos tier, and whether the world is already using late-game equipment. These factors can increase scale modestly. They cannot turn an Enormous package into a small aid shipment.

The generator should produce clean rounded quantities. The main bands below are design anchors, not a substitute for engine and balance validation.

| Equipment family | Enormous | Colossal | Impossible |
| --- | ---: | ---: | ---: |
| Infantry equipment | 150,000 to 500,000 | 500,000 to 1,000,000 | 1,000,000 to 2,000,000 |
| Support equipment | 15,000 to 50,000 | 50,000 to 100,000 | 100,000 to 250,000 |
| Artillery | 8,000 to 30,000 | 30,000 to 60,000 | 60,000 to 150,000 |
| Anti-tank | 5,000 to 20,000 | 20,000 to 45,000 | 45,000 to 100,000 |
| Anti-air | 5,000 to 20,000 | 20,000 to 45,000 | 45,000 to 100,000 |
| Rocket artillery | 4,000 to 15,000 | 15,000 to 35,000 | 35,000 to 80,000 |
| Motorized vehicles | 25,000 to 80,000 | 80,000 to 200,000 | 200,000 to 450,000 |
| Mechanized vehicles | 10,000 to 35,000 | 35,000 to 90,000 | 90,000 to 200,000 |
| Tanks and armored vehicles | 2,500 to 10,000 | 10,000 to 25,000 | 25,000 to 60,000 |
| Aircraft | 1,500 to 6,000 | 6,000 to 15,000 | 15,000 to 35,000 |
| Trains | 250 to 1,000 | 1,000 to 3,000 | 3,000 to 8,000 |
| Convoys | 750 to 3,000 | 3,000 to 8,000 | 8,000 to 20,000 |

Evolution I can apply a modest scale increase because more specialized items are included. Evolution II and III can shift more of the package value into expensive high-tier equipment without reducing total strategic value.

## Baseline conventional pool

The baseline pool uses recognizable conventional stockpile items that can exist independently of special events.

Core families include:

- infantry equipment
- support equipment
- towed artillery
- anti-tank guns
- anti-air guns
- rocket artillery where a safe token exists
- trucks
- trains
- convoys
- tanks and armored vehicles
- fighters
- close air support aircraft
- tactical bombers
- strategic bombers
- naval bombers
- transport aircraft where safely grantable

The package can mix domestic, foreign, obsolete, current, and slightly advanced equipment. It does not need to match one national equipment lineage.

Complete warships are outside the ordinary stockpile grant model and should not be promised as crate equipment. Convoys remain valid. If a future engine-backed ship-transfer helper is deliberately added, it should be handled as a separate manifest family with its own physical and ownership rules rather than disguised as stockpile equipment.

## Technology selection at baseline

Baseline should remain mostly recognizable to the recipient while allowing a controlled amount of surprise.

For each family, use the recipient's current research only to identify relative technology level. Do not use it to reduce quantity or remove the family.

Suggested starting distribution:

- 55 percent at a level the recipient already fields or could recognize as current
- 30 percent one meaningful generation ahead
- 10 percent as a foreign peer variant or alternate design
- 5 percent at the highest safe conventional tier available to that family

A recipient with almost no research can therefore receive equipment far ahead of its own production, but the overall baseline package should still look conventional.

Receiving a token does not complete its technology. The recipient can use the physical stockpile when the base game allows captured or foreign equipment use. It cannot manufacture replacements until it obtains the normal production access.

## Variant and designer equipment rules

Modern HOI4 equipment designers can make a bare archetype or chassis unusable as a finished weapon. Event 42 must grant complete usable variants, not empty chassis that only inflate a stockpile number.

The implementation should maintain a stable conventional variant registry for designer families. A variant must have valid modules, legal year and DLC behavior, an equipment icon, a supply and fuel profile, and a fielding consumer. It may be a neutral standardized design created for Event 42 or a safely reusable existing design.

The variant registry needs paths for the active DLC configuration. When a designer DLC is unavailable, the event should use the matching non-designer equipment token. When a selected family has no safe complete variant under the current game setup, reroll that family into another valid family of comparable package value.

Foreign naming can appear in reports, but the stable internal variant must not depend on a country that was annexed or never existed.

## Land equipment composition

Infantry and support anchors should contain enough rifles and support material to equip a very large army. Artillery, anti-tank, and anti-air quantities should be large enough to change division design rather than serve as minor supplements.

Armor anchors should include complete vehicles across one to three roles. The package can mix light, medium, heavy, amphibious, tank destroyer, anti-air, or flame-support designs when the active evolution and installed systems permit them. A large armor delivery should usually include motorized or support material, but it does not need to include fuel or manpower.

Mechanized equipment becomes common in Evolution I. It can appear at baseline in rare advanced packages when a safe variant exists.

## Air equipment composition

Air anchors can grant thousands or tens of thousands of aircraft. The package may include more airframes than the recipient has pilots, fuel, airbases, or trained ground crews.

Aircraft must be complete usable designs. The event should not grant an empty airframe when the aircraft designer is active.

An air package can mix several roles. It may be strategically awkward. A landlocked country can receive naval bombers. A minor with one airbase can receive a major strategic bomber fleet. The event does not create pilots, airbases, fuel, doctrines, or mission access to make the result convenient.

## Logistics equipment composition

Trains, trucks, support equipment, and convoys can form their own anchor package. This outcome should be powerful, especially for a country suffering supply pressure, but the generator must not select it because the country needs logistics.

A logistics package can be comically excessive. Tens of thousands of trucks or several thousand trains are valid. A small island can receive a rail fleet it cannot use. A landlocked country can receive convoys it may later transfer, retain, or use after gaining a coast.

## Manifest archetypes

These are composition roles, not fixed packages.

### The Infantry Continent

The anchor is infantry equipment. Support equipment, artillery, anti-air, trucks, and one awkward air or amphibious family support it. The quantity can equip millions of soldiers, but no manpower is included.

### The Armored Rain

The anchor is complete tanks or mechanized vehicles. Trucks, support equipment, trains, anti-air, and artillery accompany them. Fuel and trained crews remain the recipient's problem.

### The Empty Air Force

The anchor is aircraft. The package can create an air fleet larger than the recipient's entire armed forces. Ground support equipment and trucks may accompany it. Pilots, airfields, fuel, and doctrine do not.

### The Moving Country

The anchor is trucks, trains, or convoys. The package can transform logistics or become absurdly mismatched to geography. Smaller weapon families give it military value beyond transport.

### The Gun Horizon

The anchor is artillery, anti-tank, anti-air, or rocket artillery. Rifles, support equipment, and transport help field it. The recipient can gain firepower that its officer corps has never planned to coordinate.

### The Foreign Warehouse

No single national lineage dominates. The package contains several incompatible foreign equipment families, unusual ammunition ratios, and spare parts that do not match the main vehicles. It remains usable stockpile equipment, but replacement and maintenance are difficult in narrative terms.

## Deliberate non-optimization

The package generator should not use shortage scores, desired templates, AI production plans, current enemies, terrain, coastline, or stockpile deficits to maximize recipient benefit.

The only recipient-sensitive checks are technical validity checks. They answer whether the country and current engine configuration can hold and use the physical token at all. They do not answer whether the token is strategically useful.

A reroll caused by technical invalidity should preserve family value. A reroll caused by inconvenience is forbidden.

## Local distribution burden

Magnitude and family mix shape the landing reports.

- Vehicle-heavy packages create blocked roads, damaged fields, fuel spills, and recovery cranes.
- Artillery-heavy packages fill rail yards and require ammunition cordons.
- Air-heavy packages occupy open land, roads, and improvised strips.
- Logistics-heavy packages overwhelm depots and sidings.
- Nuclear or biological packages create sealed military zones and severe handling reports.
- Special Chaos equipment creates quarantine, missing guards, strange movement, or unexplained power draw only when those details match the verified family.

The local burden does not consume a hidden percentage of the grant. Equipment loss from recovery should happen only through a visible rare accident, and the amount should be small compared with the delivered total.

## Package persistence

The manifest snapshot persists until all landing reports and achievement hooks finish. It must survive save and reload without changing quantities, report states, provenance signature, or special-family identity.

After closure, only compact historical facts need to remain:

- recipient
- firing sequence
- magnitude
- broad family mask
- nuclear receipt flag and amount when present
- special-family token and amount when present
- achievement eligibility facts

Detailed temporary arrays and report targets should be cleaned after the final report.

## Balance intent

The event is allowed to be overpowered. Its balance comes from randomness, repeatable weight decay, lack of recipient optimization, missing manpower and fuel, replacement limits, logistical burden, and the opportunity cost of reorganizing a military around an unplanned arsenal.

Do not shrink quantities until they feel like normal lend lease. Do not compensate by adding severe permanent penalties. The recipient should feel fortunate and overwhelmed.

The event should be capable of changing a war immediately. It should not guarantee that the selected country can convert the arsenal into battlefield strength without further effort.
