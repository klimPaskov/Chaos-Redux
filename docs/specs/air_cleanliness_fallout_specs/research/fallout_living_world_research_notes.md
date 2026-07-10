# Fallout Living World Research Notes

## Purpose

These notes support the event and climate design in this planning pass. They are design grounding, not a literal simulation contract. Final tuning must be checked against gameplay, local Hearts of Iron IV engine behavior, and the accepted Chaos Redux balance model.

## Nuclear winter, light loss, and food systems

Primary source:

- Xia, Robock, Scherrer, Harrison, Bodirsky, Weindl, Jägermeyr, Bardeen, Toon, and Heneghan, *Global food insecurity and famine from reduced crop, marine fishery and livestock production due to climate disruption from nuclear war soot injection*, Nature Food 3, 586 to 596, 2022.
- Source: https://www.nature.com/articles/s43016-022-00573-0

Relevant findings:

- Stratospheric soot would reduce light, temperature, precipitation, crop production, and marine productivity.
- The modeled climate effects last about a decade and peak during the first few years.
- Across the modeled cases, maximum average temperature reduction over crop regions ranges from about 1.5 degrees Celsius to 14.8 degrees Celsius.
- The temperature reduction peaks within roughly one to two years and can persist for more than ten years.
- High northern latitudes suffer the strongest percentage losses in crop production.
- Marine food production declines less than land crops, but cannot replace the lost calories.
- Alternative food, cold-tolerant crops, greenhouses, waste reduction, and feed conversion can help, but rapid large-scale conversion is difficult.
- Export restrictions and transport disruption can make import-dependent regions suffer even where local climate cooling is smaller.

Design translations:

- Winter phase severity should be strongest in Years 1 and 2, then recover slowly.
- Every region should become visibly colder, dimmer, or ecologically disrupted, but the visible form should differ by biome.
- Snow cover is appropriate for boreal, continental, highland, and some temperate classes.
- Tropical and arid classes should use cold rain, frost at elevation, dead vegetation, dust, ash, reduced sunlight, failed monsoons, and unusual cold nights. Do not apply a universal snow texture.
- Food events need several mechanisms. Crop failure, seed conversion, livestock slaughter, fishing pressure, trade closure, cold storage loss, greenhouse construction, fungal food, and ration politics should not collapse into one generic famine chain.
- Southern Hemisphere and maritime refuge states can have relative advantages without becoming safe havens. Refugee pressure, shipping loss, fertilizer loss, fuel loss, and political conflict remain major constraints.
- Recovery should not return the world to normal after one successful harvest. The climate, food, and political memory layers continue into Year 10.

## Shelter and decontamination

Primary public-health source:

- United States Centers for Disease Control and Prevention, Radiation Emergencies safety guidance.
- Source: https://www.cdc.gov/radiation-emergencies/safety/index.html

Relevant guidance:

- The core immediate action is to get inside, stay inside, and remain informed.
- Interior rooms and basements provide more protection than exterior walls and roofs.
- Remaining inside for at least the first day can materially reduce exposure while radioactive material weakens.
- Removing outer clothing and washing can remove a large share of external contamination.

Design translations:

- Ash-week orientation must care about shelter depth, interior space, filter stock, water, crowding, fire, structural damage, and communication.
- Shelter decisions should have timing. Opening doors early, admitting late arrivals, sending rescue teams, moving patients, or changing ventilation should alter casualties and future legitimacy.
- Decontamination needs clothing, water, heat, privacy, staff, and waste handling. A single national modifier is too abstract.
- Shelter law becomes a founding political issue. Who was admitted, who was turned away, and who controlled the filters should create years of grievance and institutional memory.
- Fallout effects should decay differently from the long soot-driven climate crisis. Local radiation, surface access, and climate winter are related but separate systems.

## Electromagnetic disruption and communications

Primary official source:

- United States Radiation Emergency Medical Management, Electromagnetic Pulse Following a Nuclear Detonation.
- Source: https://remm.hhs.gov/EMP.htm

Relevant guidance:

- EMP itself is treated as an infrastructure and equipment problem, not a direct health effect.
- Communications, grid controls, hospital equipment, fuel systems, water controls, and electronic vehicles can be disrupted.
- Equipment brought from unaffected areas may work if the supporting infrastructure remains functional.
- Damage to towers, repeaters, lines, and power can matter as much as device damage.
- Response planning must assume that ordinary communications may be unavailable.

Design translations:

- EMP events should damage or disable communication, power, medicine, fuel, water, and logistics capacity through infrastructure dependencies.
- An intact radio, generator, or vehicle is useful only when the network around it still works.
- Communication restoration should proceed from local runners and field radios to relay chains, regional frequencies, and interregional contact.
- False broadcasts, duplicated call signs, dead transmitters, automated stations, and disputed distress signals create event material with real effects.
- EMP must not be presented as a mysterious direct killer. Deaths come from blast, fire, radiation, failed medical equipment, lost water, cold, transport collapse, and delayed rescue.

## Emergency institutions and preparedness

Primary institutional source:

- International Atomic Energy Agency, Emergency Preparedness and Response.
- Source: https://www.iaea.org/topics/emergency-preparedness-and-response-epr

Relevant principles:

- Effective response depends on maintained arrangements, capabilities, standards, tools, trained personnel, and coordination.
- Preparedness and response operate at local, national, and international levels.
- Deliberate acts, accidents, negligence, and cascading infrastructure failures require different information and response paths.

Design translations:

- Pre-collapse preparation must matter. Shelters, trained staff, spare filters, stored seed, hard-copy plans, local drills, and redundant communication should change opening events.
- A surviving government name does not guarantee capacity. Institutions need staff, records, authority, tools, and routes.
- Regional coordination should emerge through actual capabilities, such as laboratories, weather stations, rail dispatch, hospital networks, and water testing.
- Successor legitimacy should come from repeated delivery of food, heat, security, justice, and information, not from one ideology event.

## Radiation genetics and mutant-fiction boundary

Primary review source:

- National Research Council, *Health Risks from Exposure to Low Levels of Ionizing Radiation: BEIR VII Phase 2*, Chapter 4, 2006.
- Source: https://www.nationalacademies.org/read/11340/chapter/6

Relevant findings:

- Ionizing radiation can induce genetic damage in experimental systems.
- The report notes no statistically demonstrable adverse heritable genetic effects attributable to the radiation exposures of the atomic-bomb survivor populations examined.
- It also states that evidence for radiation-induced germ-cell mutations causing genetic disease in humans is absent.

Design translations:

- Radiation sickness, cancers, burns, cataracts, infertility pressure, pregnancy risk, and contaminated environments can be grounded in real hazards.
- Rapid human transformation into stable new species is not a scientific prediction.
- Mutant countries, altered peoples, inherited extreme traits, and nonhuman societies are explicitly fictional Chaos Redux content.
- Their triggers should include high-chaos fiction, experimental programs, biological contamination, supernatural causes, or scripted scenario logic where appropriate.
- Player-facing text must not claim that ordinary radiation predictably creates fantasy mutants.
- Fictional altered societies should have culture, law, health, diplomacy, family, and internal politics. They should not exist only as hostile monsters.

## Research limits

The cited climate paper models a set of soot-injection scenarios. It does not predict one exact outcome for every possible Chaos Redux source event.

The planning package therefore uses:

- phase bands instead of one literal temperature value
- regional visual classes instead of universal snow
- resource and infrastructure variables instead of deterministic national death totals
- several Fallout causes with different memories and local damage
- gameplay tuning that remains subject to local testing

A 2025 agriculture paper was identified during research, but the primary publisher page could not be opened in this environment. Its reported figures were not used as the sole basis for any hard tuning rule.

## Historical and regional research still required during implementation

Before final localisation and country-specific event writing, implementation should run focused research for:

- region-specific staple crops and cold-sensitive food systems
- period transport, power, water, hospital, mine, port, and rail institutions
- local winter, monsoon, drought, flood, highland, and maritime patterns
- historically plausible civil-defense, emergency-government, religious, labor, military, and municipal institutions
- local naming, symbolism, clothing, architecture, and material culture for assets
- real leaders and real historical symbols where a successor route uses them

This work must avoid stereotypes and should distinguish sourced history from alternate-history invention.
