# Biowarfare System (Mechanics Guide)

This is a player-facing guide to Chaos Redux biowarfare.

It explains what the system does in gameplay terms: what you unlock, how you deploy it, what spreads, and how to contain it.

## Big Picture

Biowarfare has seven connected pillars:

1. Development and unlocks.
2. Payload production and exact stockpile safety.
3. Delivery by native raids.
4. Incubation, detection, and state contamination.
5. Spread between states and countries.
6. Medical containment and recovery.
7. Evidence, attribution, deaths, and Condemnation.

It is a long-horizon system: strong strategic impact, high political risk, and heavy management demands.

## Development and Unlocks

Bioweapons are unlocked through special project progression.

Each completed project opens practical deployment options for that agent family and increases your strategic leverage, but also raises risk.

Overall weapon strength follows `Tularemia < Anthrax < Plague < Smallpox`.

Tularemia is low severity, Anthrax is moderate, Plague is serious, and only Smallpox belongs to the severe weapon tier.

Agent identity changes the harm that follows a release, not the native chance that a raid reaches its target.

That means:

- safer research paths reduce the chance of your own program backfiring,
- some projects let you prepare domestic medical countermeasures while research is still underway,
- skipping those protections can leave you exposed if accidents or later retaliation reach your own territory.

## Delivery

Deliberate battlefield and strategic deployment uses dedicated native raids.

Ordinary battlefield raids require Pathogen Handling Protocols, full derived protection readiness, a completed agent project, matching payload, and battlefield-use authority. Theater CBRN Headquarters is an advanced Chaos Warfare certification, not a prerequisite for these basic attacks.

Food, water and medical sabotage uses covert native supply-chain raids.

The historical Japan-China campaign uses exact-state Anthrax and Plague raids on its explicit route, and the exceptional doomsday release uses `biological_stockpile_doomsday_raid` under the shared biological raid category.

Those exceptions consume exact payload and enter the same ordinary lifecycle; they do not replace the native raid system for ordinary strategic or battlefield deployment.

In practice:

- native routes reserve or consume the exact matching payload,
- the raid supplies the exact target state and responsible actor,
- the ordinary lifecycle creates incubation before an outbreak becomes active,
- detection, deaths, medical pressure, evidence, attribution, contamination, spread, and Condemnation continue after the initial release.

All four ordinary agents use the same native strategic-raid success, critical, and disaster factors and the same native battlefield-raid success factor.

Aircraft, air defense, intelligence, assignment, headquarters preparation, and other verified operational conditions can change delivery reliability.

The selected agent changes post-release potency, incubation, detection, persistence, spread, treatment, deaths, and medical pressure.

## Contamination Effects

Contaminated states suffer major penalties to local performance.

Typical consequences include:

- weaker local economy and logistics,
- reduced military efficiency,
- growing pressure on stability and war capacity.

Different agents create different contamination profiles.

## Spread

Contamination can spread into neighboring states if not contained.

Spread chance is influenced by broader conditions such as:

- preparedness,
- infrastructure and local capacity,
- social and wartime stress,
- public-health response strength.

Some agents spread faster and are harder to stabilize than others.

## Countermeasures

You are not locked into passive defense.

Available responses include:

- emergency containment decisions,
- medical production programs,
- vaccination-scale mitigation for Smallpox and agent-specific treatment or containment for the other ordinary agents.

A strong response can slow spread, reduce damage, and eventually clear contamination.

National bio-surveillance and Smallpox vaccination use Political Power, CBRN Instruments, Support Equipment, and Medical Capacity committed until their respective programs stand down. Each also needs transport on hand when selected, but the trucks are not consumed by establishing the program. The decision's cost row shows the upfront Political Power and equipment payment; its cost hover explains the Medical Capacity commitment and truck requirement. The current tuned amounts and durations come from `common/script_constants/biological_countermeasure_constants.txt`.

Field hospitals and international medical missions instead consume Political Power, Support Equipment, and trucks while committing Medical Capacity until the deployment ends. They require CBRN Instruments on hand without consuming them. If the target outbreak ends before deployment, the committed medical teams return; spent supplies remain spent.

Quarantine consumes Political Power, Command Power, trucks, and manpower. Support and infantry equipment must be on hand to staff the cordon, but remain in the stockpile. The cordon strains local production and raises resistance while slowing disease.

Sustain Containment requires 15 Medical Capacity available, commits 10, and leaves 5 free; it consumes Political Power, Command Power, and Support Equipment when ordered. Trucks and CBRN Instruments must be on hand but are not consumed at selection. A continuing success or partial success consumes another Support Equipment shipment only if the smaller transport and instrument requirements remain met and 5 Medical Capacity stays uncommitted when the mission ends; otherwise the response fails and its committed medical teams return.

An Anthrax, Plague, or Tularemia treatment course consumes Political Power, Support Equipment, and trucks. The first supported course in a state commits a medical team; later courses in the same state reuse that team. The cost hover tells you whether the selected state needs a new Medical Capacity commitment.

## Stockpile Safety and Accidents

One exact owned biowarfare facility is designated as the national arsenal.
Anthrax, Plague, Tularemia, and Smallpox inventories are read from their live equipment stockpiles and combined with Biosecurity, safety technology, facility condition, bombing, sabotage, and recent handling.

The player sees one of four bands: Controlled, Strained, Dangerous, or Critical.
Ordinary incidents range from a contained loss to an internationally exposed major outbreak.
The exact matching equipment is debited once, and every non-contained result enters the shared incubation and outbreak lifecycle in the exact arsenal state.

Biowarfare therefore includes internal risk:

- high-risk research choices can backfire,
- stockpile mismanagement can cause catastrophic domestic consequences,
- emergency release paths are possible but extremely dangerous politically and strategically.

Stockpile accidents are cooldown-gated per payload type.
After an Anthrax, Plague, Tularemia, or Smallpox stockpile accident, that same payload type cannot produce another ordinary accident for 730 days.
Other payload types keep their independent cooldowns.
Fail-Safe Containment Facilities stop ordinary accidents but do not stop sabotage, bombing, capture release, or doomsday release.

See [Biological Stockpile Safety](biological_stockpile_safety.md) for exact designation, risk-band, scheduler, lifecycle, AI, and asset contracts.

## Diplomacy and International Consequences

Biological weapon use carries major diplomatic costs.

Repeated use drives increasing international backlash and can reshape your strategic relationships, especially with ideologically opposed blocs.

The first publicly confirmed Smallpox use by a country fires the global news event `chaosx_bioweapon.207`.
`bio_lifecycle_release_confirmed_condemnation_if_due` and `bio_doomsday_record_current_agent_history` raise it just before they set `used_smallpox_weapon`, so each country announces it once.
The first Smallpox outbreak detected in a country's controlled state fires `chaosx_bioweapon.208` for that controller.
`bio_lifecycle_mark_current_agent_detected` raises it and sets `smallpox_victim`, so each controller receives it once.

## AI Behavior

AI chooses research, production, stockpile safety, countermeasures, and delivery according to country program, doctrine route, war state, retaliation status, medical readiness, likely friendly spread, sanction exposure, and target evidence.

Ordinary profiles avoid biological first use.

Retaliatory, historical Japan-China, high-chaos, radical, and near-defeat routes can become more aggressive only after their explicit gates are satisfied.

Agent-specific route preferences may differ because their strategic effects differ, but AI preference never changes the equal native raid-success factors.

## Player Strategy Notes

- Biowarfare is strongest when paired with a containment plan of your own.
- Raid success is only part of the story; post-strike pressure and spread management matter more.
- Overuse can win short wars but lose long diplomatic positioning.

## Implementation surfaces and remaining validation

Strategic, battlefield and covert supply-chain raids, the Japan-China campaign raids, field testing, stockpile accidents, captured-facility recovery raids, the biological doomsday raid, agent-specific incubation and treatment, evidence, attribution, deaths, contamination, spread and designer integration enter the ordinary biological lifecycle.
Event 016 retains the shared `operative_release` lifecycle route from its native owner; this internal route token does not expose a public intelligence attack.
The [consolidation map](../../../plans/chaos_warfare_system_plans/2026-10-08_native_biological_operation_consolidation.md) records retired interface-specific behavior and retained shared history, evidence and achievements.

Captured facilities are secured or destroyed through native land raids and never through a deployment decision.

The doomsday route remains an explicitly authorized native raid exception whose selected state authenticates the wider batch release.

Package scenario validation, balance recording, and the mapped specialist completion audits remain part of the wider CBRN completion stages and are not claimed by this guide.

## Incubation scheduling API

`bio_lifecycle_schedule_incubation_for_current_agent` in `common/scripted_effects/biological_lifecycle_effects.txt` operates on the exact affected state.
Its input is the caller-owned temporary `bio_active_agent`, identifying one of the four ordinary agents; it has no returned output and invents no default agent.
An incubating record without a scheduled activation marks its schedule, draws its delay once, rounds and clamps it using `bio_lifecycle_schedule`, and stores the exact due day before queuing its activation event.
An absent or already scheduled incubation neither draws again nor overwrites its due day.
Usage after selecting the current agent in the affected state is `bio_lifecycle_schedule_incubation_for_current_agent = yes`.

The private `bio_lifecycle_queue_incubation_event_internal` reads the caller-owned selector and completed `bio_incubation_days` after that calculation.
It has no output, default, additional random draw, receipt mutation or independent eligibility check.
Its only side effect is one `cbrn_bio_lifecycle.<agent>` state event, with the ID and integer delay inserted into a literal native event statement when the helper executes.
It is called only by the guarded scheduler after recording the due day.

Activation requires the matching incubating and scheduled flags and the due day to have arrived.
An accepted callback clears incubation scheduling, marks the agent active, performs existing detection, and schedules the agent's ordinary weekly tick.
An early or repeated callback cannot activate the record a second time.
Per-agent flags and due dates allow several agents to incubate independently in the same state.
No worldwide polling hook is used.

The [timing evidence](../../../plans/chaos_warfare_system_plans/2026-10-07_biological_incubation_timing.md) distinguishes the source-tested delay/guard contract from native queue execution and recovery of stranded schedules, which remain unverified.
