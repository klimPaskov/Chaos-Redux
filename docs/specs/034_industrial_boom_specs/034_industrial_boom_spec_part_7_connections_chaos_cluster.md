# Industrial Boom specification, part 7: Connections, Chaos, and cluster role

## Connection rule

Event 34 reads existing world conditions and accepts bounded shock or relief requests from other owners.
The owner of a physical loss applies that loss, Deaths, environmental effects and their Chaos once; Event 34 manages only the industrial strain it causes.
A connection is kept only when it changes a choice the player makes about the boom.

## Shock and relief adapter (pending)

Another owner can submit a request naming the active boom country, the source family, a magnitude band, an optional state, and the owner's proof and receipt.
Unknown sources, invalid states, inactive booms and replayed receipts change nothing.
An accepted request changes Overheating once and, when it names a region, can pause that region's project or spend its protection.
The leading-cause line names the source.
A request and Event 34's own observation of the same damage never both apply the immediate shock; continuing damage can keep the Regional strain driver high until repaired, but repair removes that cause and never refunds the original shock.

## Event 35 Great Depression 2.0 (implemented)

Event 35 is the direct failure relationship (part 6).
Two further links are implemented in Event 35 and Event 34 owner files:

**Boom supply contract.** A country in its own depression with an active Financial Contagion surface can take Offer Boom Supply Contract toward an active boom country.
Event 34's `industrial_boom_receive_depressed_market_demand` accepts it when the supplier passes `industrial_boom_supplier_market_demand_target_is_valid`, then adds `supplier_demand_overheating` to the supplier's Overheating and opens a `supplier_contract_days` contract, marked at risk when Overheating is at or above `supplier_contract_overheat_risk`.
The depressed country gains Severity relief and secured freight.
Event 35 reads the supplier only through the `industrial_boom_supplier_adapter_*` triggers.

**Worldwide depression supplier.** A boom that fires while a worldwide depression episode is active joins it as a supplier through `great_depression_event34_supplier_adapter`.

Design additions on the Event 34 side (pending):

- The contract gives the supplier an output opportunity, a 120-day export-order modifier that raises factory output, as Event 35's API already expects Event 34 to return.
- A contract still active at landing upgrades a rough landing to a controlled one once (part 1).

Together these make the contract a real choice for the supplier: more pressure now in exchange for output and a softer landing.
Whether the supplier may refuse is an open question in the README.

## Natural disasters, Acid Rain and bombing

A confirmed disaster, corrosion or bombing loss in an Industrial Region shocks Overheating in proportion to the region's industrial share, pauses its project, and spends its protection if it had one.
[Acid Rain's state consequence contract](../033_acid_rain_specs/specs/033_acid_rain_consequence_repair_acceptance_2026_10_03.md) is the reference owner: Event 34 protection reduces industrial strain only and never lowers Acid Rain mortality or settles that event's recovery.
A forecast changes priorities without proving damage, so it applies no shock.
War both helps and hurts: equipment demand makes running hot worthwhile, and losing industrial states can crash the boom quickly.

## Trade, fuel and logistics

Fuel, trains, trucks, convoys, ports, infrastructure, embargo and blockade feed the Supply and materials driver (part 2).
Stabilize Supply Chains pays the costs that match the country's real route.
Event 34 creates no embargo or blockade of its own.

## Resources Found and other positive economy events

A resource discovery in or near an Industrial Region lowers the Supply and materials driver through ordinary resource availability.
No positive event resets Overheating, grants a project receipt, or bypasses the legacy budgets of part 4.

## Famine and migration (pending owner seams)

Both systems were reworked on 2026-10-10 and expose narrow owner triggers and receipts rather than raw variables.

- **Famine.** An Industrial Region in an active famine stage pauses its project and adds to the Supply and materials driver, read through a famine-owned state trigger. Famine keeps food, mortality and Deaths. A crash creates no famine by itself.
- **Migration.** A displaced cohort locally integrated in an Industrial Region state, through migration's own Local Integration settlement, lowers the Output intensity driver for that region for 180 days, because the works gain labor. Migration keeps cohorts, reception load and Deaths; Event 34 moves no population.

The migration link gives a booming host a concrete reason to integrate arrivals rather than move them on.
Both links need a migration- or famine-owned trigger before implementation; Event 34 must not read their private ledgers.

## Air contamination, fallout and CBRN

A state under a severe contamination or fallout condition cannot be chosen as an Industrial Region or spread state, and an existing project there pauses.
Air Cleanliness, fallout and CBRN owners keep contamination, Deaths and their Chaos.

## Condemnation

Condemnation has no direct effect.
Its sanctions and trade consequences reach the boom only through the trade conditions above.
Economic success never lowers condemnation.

## Camps and Deaths

Event 34 has no camp connection: forced labor is not a boom management tool, and camp output stays within the camp system.
Event 34 records no Deaths; incident text may mention injuries or casualties without numbers, and no incident moves the Deaths ledger.

## Event 39 Murder Mystery (implemented)

Event 39 reads `industrial_boom_active` and gives a booming country better-equipped investigators.
Event 34 must keep that flag set for the whole active boom.

## Chaos

Industrial Boom adds no Chaos for firing, for any management action, or for an evolution activating.
Chaos comes only from concrete abnormal outcomes, applied once through the shared Chaos Meter helpers in `common/scripted_effects/chaos_meter_effects.txt` (`add_chaos_meter_value` with its history entry, see [the Chaos Meter docs](../../systems/chaos_meter/README.md)) and guarded by an Event 34 source receipt.
Magnitudes are constants in the Event 34 tuning file.

| Source | Direction | Guard |
| --- | --- | --- |
| First Miracle project reaches Secured (Evolution II) | Small gain | Once per boom |
| First spread state integrates (Evolution III) | Small gain | Once per boom |
| Controlled landing of a boom that recorded either gain | Reduction no larger than the recorded gains | Once per boom, closes only its own sources |

Speculative Mania adds no Chaos, because its consequences are ordinary economic ones that Event 35 already covers.
A crash adds no Event 34 Chaos; Event 35 owns the Chaos of the depression.
Event 34 never duplicates Chaos from Deaths, war, annexation, nuclear use, Air contamination, world tension or building damage.

## Cluster role

The authoritative catalog places Event 34 in Positive Economy (cluster 7) as its Low member, alongside Events 18, 26, 29, 55, 57 and 58.
Positive Economy is catalogued but not yet registered in the cluster runtime; that registration belongs to the event system.

When a cluster dispatches Event 34:

- the entry is the same `chaosx.nr34.1` with the same target gate and weighting, so a country with an active boom is never chosen;
- Event 34 reads no cluster context and grants nothing extra for being part of a batch;
- rewards stacked with other Positive Economy members on the same country stay inside Event 34's own legacy budget;
- a later crash into Event 35 never rolls Negative Economy or records a cluster row.

The earlier planning statement that Event 34 stays unclustered is superseded by the catalog assignment.

## Acceptance

- Event 35 is the only direct crisis dependency, and the supplier contract is a real choice with a cost and a gain.
- Disasters and bombing shock the boom once and are not duplicated by an adapter request.
- Maritime and land economies react differently to trade and logistics problems.
- Famine, migration, contamination and Deaths stay with their owners.
- Event-owned Chaos occurs only after a concrete abnormal outcome and reverses only its own recorded source.
- A cluster dispatch behaves exactly like a normal firing.
