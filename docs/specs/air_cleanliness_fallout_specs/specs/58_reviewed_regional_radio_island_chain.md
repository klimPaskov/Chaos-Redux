# Reviewed regional Fallout chain: Radio Island Chain

Status: accepted implementation tranche, dormant until the Fallout scheduler activation and delivery contracts are proven.

This ordinary regional incident belongs to the Oceania and Remote Islands runtime region. It is not a super-event and it does not reuse zombie identifiers, files, assets, audio, sprites, or paths.

## Identity and ownership

- Candidate and human opening: `600`
- Hidden AI opening: `601`
- Human delayed result: `602`
- Hidden AI delayed result: `603`
- Human callback: `604`
- Hidden AI callback: `605`
- Authenticated cleanup: `606`
- Scheduler transaction key: `710057`
- Route identity: `7157`
- Route upper bound: `7158`
- Event Log history: `9163`
- Runtime region: `fallout_region.oceania_remote_islands`
- Primary family: `fallout_event_primary_family.regional_and_biome`
- Cooldown family: `fallout_event_cooldown_family.broadcast`
- Event class: `fallout_event_class.routine_incident`
- Preferred phase: `fallout_event_phase.first_winter_year`
- Secondary phase: `fallout_event_phase.consolidation`
- Visible budget cost: `2`

The candidate is appended by the ordinary Fallout candidate registry. It never sets either scheduler activation flag and it contributes no release-floor credit while the scheduler remains dormant.

## Regional premise

Cold seas, damaged ports, and long distances have broken the old island broadcast network into isolated local stations. One surviving coastal state has a native radio or radar installation, enough power to keep a transmitter warm, and a population that can staff it. The country must decide whether the signal belongs to everyone, to the armed command, to a paid service, or to a federation of islands.

The text names island weather, harbor approaches, fishing grounds, quarantine notices, and radio-watch families. It does not claim that a real institution survived and it does not create a bilateral partner in this tranche.

## Admission and deterministic target

Country admission requires a current Fallout identity, resource row, generation receipt, ordinary-event eligibility, the exact Oceania and Remote Islands region, the first-winter-year phase or later, and at least one affordable branch. The country must have at least 18 Power, 12 Fuel, 10 Recognition, and 24 Cohesion.

The state selector scans native owned and controlled states and admits only a produced current-generation Air Winter row with surviving population, at least 12 Supply Access, at least 8 Reclamation, exposure below 72, disease pressure below 68, a coastal receipt, at least one non-damaged radar station or air base level, and at least one non-damaged infrastructure level. The lowest eligible native state id is the sole frozen host. No capital fallback, historical island enumeration, or multi-state transaction is used.

## Four authored branches

1. Public relay service spends Power 6, Fuel 4, Filters 3, and Recognition 3. Success improves signal reach, Recognition, and Cohesion. Partial success leaves a local schedule. Failure creates an island silence memory and increases exposure.
2. Maritime defense net spends Power 5, Fuel 6, Command Power 10, and War Support is checked on the native 0 to 1 scale. Success improves warning reach and military coordination. Partial success keeps the net local. Failure damages one radio or radar installation when one remains and reduces Cohesion.
3. Harbor subscription spends Fuel 4, Scrap 3, Recognition 2, and requires Power 18. Success improves route access and a durable service ledger. Partial success creates a narrow paid route. Failure raises smuggling pressure without changing diplomacy.
4. Island federation spends Food 5, Power 4, Recognition 5, and requires Cohesion 40. Success creates a named island council memory and improves Recognition and Cohesion. Partial success creates a provisional council. Failure records a federation dispute and increases dependency.

Every branch has a truthful cost trigger and a non-zero failure path. The human and hidden-AI lanes use the same branch payment, frozen inputs, grade, delayed result, callback, Event Log, and cleanup effects.

## Deterministic grading and timing

The result is issued 35 days after the opening. A ten-component integer score uses equal weights and a divisor of 100. Components are Power, Fuel, Filters, Cohesion, Recognition, the averaged relay, contact, and intelligence signal ledger, Reclamation, host-state Supply Access, inverse Exposure, and inverse Disease. The score is clamped to 0 through 100 and is never rerolled.

Branch thresholds are public in the dedicated constants. Each branch has separate success and partial thresholds so failure and partial results remain reachable. The callback is issued 240 days after the result and reauthenticates the generation, owner, controller, host state, branch, result, and callback ticket before changing durable ledgers.

Callback outcomes establish one of four durable country memories: public island relay, maritime warning net, harbor subscription service, or provisional island federation. Cleanup clears only transaction state and preserves route identity, branch, result, callback, and memory flags.

## AI, Event Log, and integration

The hidden AI branch chooses a valid affordable branch deterministically. Public-relay weight rises with Recognition and Cohesion. Maritime-defense weight rises with War Support and Fuel. Harbor-subscription weight rises with Power and Scrap. Island-federation weight rises with Cohesion and Food. Low signal quality or high smuggling pressure reduces the relevant branch without forcing an invalid choice.

History `9163` records the opening branch, success, partial, failure, callback, and cancellation payloads. The country is the primary actor and the authenticated host state is the secondary actor. Localisation uses concrete island and harbor language and avoids process or implementation wording.

## Deliberate exclusions

This tranche adds no partner country, reciprocal air access, trade-route subsystem, naval equipment, focus tree, decision, mission, country package, formable, scripted GUI, recurring scheduler, super-event, or animation. Those remain queued until their engine contracts are separately reviewed.

The exact all-valid-province thermonuclear manual sweep remains dormant because native enumeration, callback load, and runtime acceptance are not proven. The accepted 90 to 95 percent prestrike population contract remains unchanged.
