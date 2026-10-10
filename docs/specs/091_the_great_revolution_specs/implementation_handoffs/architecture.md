# Event 091 technical architecture

## Authority and status

This is the accepted technical planning handoff for The Great Revolution.
Native feasibility and implementation acceptance remain separate proof gates.
The user brief fixes the premise, the proportional opening, Event 001 inheritance, the Stalin and Trotsky rules, the two public values and the Red World conditions.
Read-only repository evidence at commit `a3ef485c5da7e2337122eca04ac65c175050f251` identifies historical implementation and migration work at that revision and does not override the brief or prove native execution.
No gameplay has been implemented.
Helper and field names in this handoff are contracts for implementation review, not claims that those definitions exist.
Engine-facing details remain subject to installed documentation, vanilla precedent and the validation map in `feasibility_and_mcp_map.md`.

This handoff owns ownership, ordering and transaction boundaries.
The design chapters own the rules themselves: the opening allocation in [Part 3](../design/091_the_great_revolution_spec_part_3_opening_and_territory.md), Influence and sovereignty in [Part 5](../design/091_the_great_revolution_spec_part_5_influence_momentum_and_powers.md) and [Part 8](../design/091_the_great_revolution_spec_part_8_decisions_missions_and_ai.md), and the Red World, finite network and defeat in [Part 9](../design/091_the_great_revolution_spec_part_9_war_expansion_and_endings.md).

## One crisis with two lifecycle owners

Event 001 remains the owner of organizing, popularity pressure, agitation levels, local rebels, rituals, whispers, containment, and ordinary political remnants.
Event 091 receives an immutable handoff of that history and becomes the owner of Lenin, the worldwide opening, the central fighting country, the nonhuman host, alignment, Influence, Momentum, finite survival anchors, terminal transition, and defeat aftermath.

The shared `communism_spread` global flag was verified in the pinned planning source.
Event 091 must read it rather than invent an equivalent flag.
The verified historic unlock is `communism_spread_world_revolution_unlocked`, with the stage flag `communism_global_evolution_world_revolution_whispers`.
The pinned Event 001 defeat helper cleared those historic markers and reset Event 091's weight to zero.
Inspect the current owner before applying a repair.
That behavior conflicts with the brief and must be changed in the Event 001 owner before the replacement Event 091 is enabled.
Containment may clear the active spread state and make the major event ineligible while its historic unlock and accumulated weight remain intact.

The final connected crisis beat is the separate firing of Major Event 091.
Actual Event 001 Evolution 3 entry, active or pre-fire, supplies its historical prerequisite, and baseline firing or the Chaos threshold alone do not.
It receives its own major history row and actor, with no additional Event 001 evolution row for the same firing.
Later Momentum stages, army development, leader transformations, and apotheosis are baseline Event 091 progression.

## Opening transaction ownership

Pool, quota, weighted selection, origin precedence, overlap and rejected-proposal rules are defined in Part 3.
Three technical points belong here.

First, the physical union can affect a country beyond its own nomination count.
No method can simultaneously preserve every overlapping exact target, guarantee all established bases, impose one physical state claim, and make every country's final loss equal its independent target.
The specification states the independent-nomination interpretation prominently, and a country's nominated share and its actual affected ownership or control are recorded separately.
Excess caused by another country's nomination is an occupation-overlap receipt, never a second popularity roll, and never a second force grant.

Second, older data is incomplete.
Verified current state markers include `communist_controlled_state`, `communist_control_level_1`, `communist_control_level_2`, and `communist_control_level_3`.
The repository's rebel-creation paths clear those markers after transferring territory and retain no inspected durable exact host and level receipt.
Future Event 001 rebel creation must preserve exact host, state, level, episode and troop provenance before clearing live containment state.
An older rebel's observed territory, formations, leaders and stockpiles remain real inputs even when the original level was erased.
Such a state receives `legacy level unknown` in the inheritance receipt, is never silently treated as Level 3, removed from the map or replaced by a popularity reroll, and receives only the least-assumption quality package for additional opening muster.
Ambiguous original-host identity is an explicit unresolved source-data condition, not permission to fabricate a political history.

Third, the origin switch.
Lenin's origin is sovereign World Revolution territory even when its former owner or controller joins.
The direct switch opportunity belongs only to the human country whose physical opening territory contains that origin, using frozen controller identity as the meaning of physical territory in an occupation, with legal-owner disclosure in the report.
Switching is optional and does not undo the uprising for a player who stays.

## Atomic snapshot and late political choices

The opening has an atomic planning boundary before it has an atomic mutation boundary.
One guarded synchronous proposal effect freezes country eligibility, the ordinary-world ideology average, country pools, population and military inputs, state owner and controller, Event 001 lineage, local levels, and ruling ideology for the accepted transaction.
Seal every nomination and the physical union, then prove the origin and actor before any successful firing is recorded.
The successful firing commit records the immutable calendar month and revalidates the current active Soviet leader.
A rejected proposal date never becomes the announcement month.
State, army, war, faction, and character changes consume only the successfully preflighted sealed plan.

Territorial callbacks raised during application may observe intermediate native state.
They must not rebuild pools, reroll targets, modify nomination receipts, or issue a second force package.
An opening-generation guard makes those callbacks record bounded deferred refresh work.
The closing step services only the recorded participants and states, then releases the guard.
This does not require a permanent whole-world periodic sweep.

Noncommunist participants become enemies immediately, including countries with zero nominations.
Communist participants receive an alignment request tied to the frozen opening receipt.
Their selected non-origin bases remain under provisional local administration until the request resolves.
The sovereign origin, public army appearance, noncommunist wars, immutable month announcement, and guaranteed baseline aid setup do not wait for those responses.

The political response does not recalculate the opening pool or communist popularity.
At execution it rechecks the recipient, request identity, existence, current authority, current ruling ideology, and the current leader rules.
A current Stalin-led Soviet Union refuses immediately when alignment commits, and a current Trotsky-led Soviet Union joins immediately as an autonomous partner at that same committing boundary.
These fixed routes do not wait for a modal popup.
Snapshot leadership provides narrative history and AI context, while the current active leader controls the committed result.
An ordinary pending request rechecks current leadership so an old popup cannot obtain a stale Trotsky join or evade a current Stalin refusal.
Ordinary responses use the native thirteen-day reply timeout with refusal as the default, and an unanswered request receives no joining consent.
Lenin imposes refusal and war through the declared ultimatum expiry and exact request resolver, which is distinct from consent to affiliation or annexation.
A duplicate request must not overwrite the pending receipt, and closed requests cannot apply faction entry, war entry, aid, or state disposition twice.

### Owner and controller rights

Each physical state has one final disposition transaction with separate ownership and control fields.
The final rights are derived from both participants' responses and the sovereign-origin rule, using the disposition matrix in Part 3.
Implementation must use documented native semantics for changing ownership and control independently.
An engine effect that necessarily changes both cannot be treated as proof of a split transfer, and two sequential whole-state transfers must not silently replace split rights.
The effects of each disposition on existing wars, occupation, supplies and garrisons require native verification.

For an Event 001 rebel, political disposition is owned by its inheritance choice.
Joining, subordinate survival, voluntary absorption, or refusal preserves the observed army and stockpiles through the appropriate real transaction.
A refuser retains its human rebel country and non-origin bases and becomes an enemy.
The sovereign-origin exception still applies and can cause real collapse or valid exile if it was the last state.
Its established territory remains guaranteed in the opening history and selection receipt with disposition `inherited base denied Lenin by rebel refusal`.
Preserving history does not authorize unconditional annexation of that polity.

## Public values and internal bookkeeping

Revolutionary Momentum is the sole public global event value and Lenin's Influence is the sole persistent event-specific value that an ordinary joined country manages.
Their stages, meaning and visible content are defined in Part 5, and the Momentum formula and normalizations are in `state_and_transaction_contracts.md`.
State provenance, nomination receipts, force budgets, resource reservations, exact casualties, anchor identity, operation dates, alignment status, and achievement evidence are internal bookkeeping.
They do not become additional currencies or visible meters.
World-rule eligibility is shown as a broad map objective or public threshold requirement when needed, never as a separate world-share meter beside Momentum.

Do not sum overlapping country nominations as territory.
Persistent footprint uses state receipts and current control, while one-time victories, joins, commands, and incorporation premiums have unique outcome receipts.
Losing and regaining a threshold changes current powers without issuing the same one-time reinforcement, Chaos premium, or achievement event again.
Distributed survival is a separate network capability that activates at sixty Momentum and fails below forty after the declared survival interval.
This explicit hysteresis prevents one marginal defeat from alternately creating and destroying the network, grants no second public value, and leaves the public power bands describing the actual current Momentum.

## Influence and sovereignty lifecycle

The rules are in Parts 5, 8 and 9.
The technical contract adds three requirements.
A real subject or accepted equivalent binding transaction is required before a country is treated as ruled, and a stored timer or Influence value alone cannot prove puppet status.
Queued expiry events must match the current generation and stored date, and repeated delivery must not annex twice.
Lowering Influence does not revive an already cancelled annex receipt or restore sovereignty while a country remains a real subject without its own valid independence transaction.

Trotsky's autonomous-partner receipt is permanent for this crisis once his accepted partnership is established.
The Soviet Union joins when its current active leader is Trotsky, and an accepted Trotsky-led country outside the Soviet Union can receive the same protected contract after identity verification.
The protection covers Influence, compulsory binding directives, forced puppeting, annex countdowns, Red World acceleration, and any equivalent adapter attempting the same result.
Leader replacement, temporary faction exit, or a generic ideological change must not silently revoke it.
Separate voluntary political choices or normal military defeat follow their own contracts and cannot masquerade as an Influence annexation.

## Finite network and stateless continuity

The network is one origin anchor and at most one registered regional anchor per continental-command slot, at most seven in all.
Each slot has an immutable identity, state pointer, responsible command, generation, activation receipt and lifecycle state.
Capture, destruction, voluntary breakaway or proven severance closes its current anchor receipt.
One physical site cannot occupy two slots, opening callbacks and inherited strongholds cannot create additional slots, and a transformed leader can be the custodian of an existing anchor without creating another.
Any accepted restoration of a damaged but undestroyed anchor retains the same identity and consumes a real action, resources, time and prior receipt.
The severance, reconstitution and defeat rules are in Part 9, and the counterpart missions and receipt rules are in `state_and_transaction_contracts.md`.

Native capital relocation among already held World Revolution states is the preferred continuity mechanism.
If the country loses every native state while a bound-subject anchor remains, a stateless ledger can retain pending defeat analysis but cannot pretend that the country satisfies the Red World existence gate.
Restoring actual World Revolution sovereignty from that anchor is a distinct contested transfer requiring verified native mechanics and the supporter contract, and Trotsky and independent allies cannot supply such a transfer automatically.
If this continuation is technically unsupported, it is a blocked requested branch, not permission to call a phantom country alive.

Defeat closes the active crisis generation, stops supernatural reinforcement, cancels unconsumed Influence and annex receipts, releases surviving supporters through documented political transitions, clears only this event's world-threat source, and refreshes the shared aggregate.
History, dead people, public responsibility, achievement receipts, original nomination records, and liberated-state provenance remain, ordinary communist politics are not set to zero, and body-capture aftermath cannot reinsert Event 091 into the major pool.

## The Red World terminal boundary

The frozen inhabited-world denominator, the ruled-share rule and the final supporter choice are defined in Part 9.
Technically, the denominator is separate from the arithmetic country mean used by the above-five-percent availability gate, and all baseline inhabited world territory belongs in it, including ordinary territory under special-actor occupation.
The final gate consumes one terminal-generation receipt before the shared `world_end` transaction, public scenario registration, presentation and ordinary-event shutdown.
The shared and branch-specific enable controls are part of the gate.
Pause and snapshot of existing annex deadlines happens once per terminal request generation and cannot be refreshed through UI, leader changes, callbacks or reload.

## Physical people, transformed people, and deaths

Conversion changes a living person's state and military availability.
It does not itself kill them or create a second recruitable person.
Keep living conversion provenance separate from native civilian-population mutation, recruited manpower, military casualties, and Deaths registration.
Only one muster owner may reserve and consume a real manpower or population-backed cohort for a new formation.
Observe the native spawn or transfer before deciding whether another debit is needed.

The First Coming seed and the three later manifestation milestones, 40,000 person-equivalents in total, are finite supernatural exceptions defined in Part 6.
They require immutable one-time campaign receipts and include only the finite tool-and-basic-weapon package.
They grant no tanks, trucks, aircraft, ships, or fuel, and ongoing ammunition and supply follow the normal equipment and supply owners.
All additional growth derives from real formations, real equipment, measured reserve manpower, converted living people, captured depots, allied deliveries, or accepted bounded sources.

Failed conversions and repression can kill people.
Use the shared exact civilian-loss transaction for actual civilian losses and register only observed removal once.
Combat casualties use the shared military path without another manual civilian debit.
Famine, migration, contamination, infection, and Condemnation remain with their existing owners.
The supernatural event receives no exemption from those contracts and creates no duplicate outbreak or population-loss framework.

## Required implementation order

First repair Event 001's retained unlock, weight preservation, and durable rebel lineage.
Then create the snapshot, nomination, union, split-rights, and receipt contracts with read-only scenario evidence.
Audit and activate the existing dormant World Revolution identity, preferably the existing `REV` registry identity after a full installed collision audit.
Replace its static capital, generous OOB, technology, stockpile, and leader setup with the approved dynamic country package.
Activate the sovereign origin before capital-dependent setup and keep optional player transfer as the last country-scoped action.

Only after those invariants hold should the parent wire forces, global wars, alignment, Momentum, Influence, finite commands, focus and decision consumers, public history, and presentation.
Terminal and defeat paths then consume the same receipts and lifecycle inventory.
The old destructive Event 091 entry and monthly Event 093 bridge must be retired before normal selection can reach the replacement.
No implementation may run both opening paths.
