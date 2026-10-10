# Event 091 technical architecture

## Authority and status

This is the accepted technical planning handoff for The Great Revolution. Native feasibility and implementation acceptance remain separate proof gates.
The current user brief fixes the event's premise, proportional opening, Event 001 inheritance, Stalin and Trotsky treatment, one public global Momentum value, one public joiner Influence value, and The Red World conditions.
The parent accepted the complete Project Source reading gate before this draft began.
The latest supplied documentation supplies the technical contracts.
Read-only repository evidence at commit `a3ef485c5da7e2337122eca04ac65c175050f251` identifies historical implementation and migration work at that revision.
It does not override the current brief or prove native execution.

No gameplay has been implemented and no HOI4 MCP result has been collected.
Exact proposed helper and field names in these drafts are contracts for implementation review, not claims that those definitions already exist.
Engine-facing details remain subject to installed documentation, vanilla precedent, targeted source inspection, and the validation map in `feasibility_and_mcp_map.md`.

## One crisis with two lifecycle owners

Event 001 remains the owner of organizing, popularity pressure, agitation levels, local rebels, rituals, whispers, containment, and ordinary political remnants.
Event 091 receives an immutable handoff of that history and becomes the owner of Lenin, the worldwide opening, the central fighting country, the nonhuman host, alignment, Influence, Momentum, finite survival anchors, terminal transition, and defeat aftermath.

The shared `communism_spread` global flag was verified in the pinned planning source.
Event 091 must read it rather than invent an equivalent flag.
The verified historic unlock is `communism_spread_world_revolution_unlocked`, with the stage flag `communism_global_evolution_world_revolution_whispers`.
The pinned Event 001 defeat helper cleared those historic markers and reset Event 091's weight to zero. Inspect the current owner before applying a repair.
That behavior conflicts with the current brief and must be changed in the Event 001 owner before the replacement Event 091 is enabled.
Containment may clear the active spread state and make the major event ineligible while its historic unlock and accumulated weight remain intact.

The final connected crisis beat is the separate firing of Major Event 091. Actual Event 001 Evolution 3 entry, active or pre-fire, supplies its historical prerequisite. Baseline firing and the Chaos threshold alone do not.
It receives its own major history row and actor.
There is no additional Event 001 evolution history row for the same firing.
Later Momentum stages, army development, leader transformations, and apotheosis are baseline Event 091 progression.

## Recommended opening allocation

### Independent nominations followed by a physical union

The recommended solution preserves each country's exact source pool and independently calculated proportional target.
Each country nominates its own states after guaranteed inherited bases are counted.
The opening then unions those nominations into one physical claim per state.
A country's nominated share and its actual affected ownership or control are recorded separately.

This is the closest match to the user's proportional rule when countries own and control overlapping territory.
Changing the pool into exclusive owner-only or controller-only states would change the rule.
A constrained matching algorithm could underfill a country's quota when another country reserves the shared states first.
Independent nomination avoids that shortfall and avoids a country-order advantage.

The physical union can affect a country beyond its own nomination count.
For example, country A owns ten states and has ten percent communist support.
Country B occupies two of those states and has one hundred percent support.
A nominates one state and B nominates both occupied states.
Their union can affect two or three A-owned states.
A's own proportional nomination remains one.
The additional affected states are recorded as occupation-overlap effects caused by B's nomination.
They are never presented as a second popularity roll, erased from A's history, or used to spawn the same forces twice.

This distinction is an explicit interpretation required by overlapping ownership and control.
No method can simultaneously preserve every overlapping exact target, guarantee all established bases, impose one physical state claim, and guarantee that every country's final map loss exactly equals its independent target in every campaign configuration.
The specification should state this interpretation prominently.

### Pool and nomination definitions

For each ordinary participant country, freeze one deduplicated pool containing its eligible owned or controlled states plus eligible rebel-held states with exact Event 001 host lineage.
Owned and controlled memberships may both exist for a state, but a state appears once within each country's pool.
Special actors are excluded from ordinary ideological nomination.
Valid Event 001 rebels participate through their owner-specific inheritance contract and do not become an additional ordinary-country popularity roll.

Let `N_i` be that country's frozen pool size, and let `p_i` be its current communist popularity normalized to a fraction between zero and one.
Calculate `x_i = N_i × p_i`.
The whole part is guaranteed and a one-time Bernoulli draw with probability equal to the fractional remainder determines whether one additional state is nominated.
Thus `T_i = floor(x_i) + rounding_draw_i`.
There is no fixed state minimum, maximum, or popularity-to-state lookup table.

Let `G_i` be the valid inherited states in that country's pool.
All of them are nominated first.
Select `max(0, T_i - size(G_i))` additional states without replacement from the remaining local pool.
The country's nomination count is `max(T_i, size(G_i))`.
When inherited history exceeds the proportional target, preserve it and add no popularity-based states.

Additional selection uses frozen weights and a local selected-set context.
Adjacency to that country's existing and newly nominated bases can improve coherence.
Another country's earlier processing must not alter these weights.
The union is constructed only after every local nomination is sealed.
All random results are stored before the first territorial mutation and are never rerolled after a callback, repeated event, save reload, or late alignment choice.

### Guaranteed inheritance with incomplete older data

Verified current state markers include `communist_controlled_state`, `communist_control_level_1`, `communist_control_level_2`, and `communist_control_level_3`.
The repository's rebel-creation paths clear those state markers after transferring territory, retaining regular chain targets but no inspected durable exact host and level receipt.
Future Event 001 rebel creation must preserve exact host, state, level, episode, and troop provenance before clearing live containment state.

An older rebel's observed territory, formations, leaders, and stockpiles remain real inputs even when its original level was erased.
Such a state receives `legacy level unknown` in the internal inheritance receipt.
It must not be silently treated as Level 3, removed from the map, or replaced by a popularity reroll.
The least-assumption quality package is allowed only for additional opening muster on that unknown receipt.
Existing assets are preserved at their observed quality.
Ambiguous original-host identity is an explicit unresolved source-data condition, not permission to fabricate a political history.

### Sovereign origin

Choose an origin from the highest available valid Event 001 class in the required order.
It is one state with one immutable identity, even when several countries have pool membership there.
Level 3, Level 2, Level 1, and valid rebel-origin states normally already belong to the guaranteed inherited union.
Within the highest valid class, use Part 3's strictly positive origin weights, stable state-identity order and saved weighted draws.
Retain attempted identities and failure reasons for the specified failover rather than choosing the first candidate or introducing a second ranking policy.

If no inherited origin exists, prefer a nominated populated industrial state in the country with the strongest current communist pressure among valid selected origins.
Every origin comes from the exact inherited and nominated physical union.
Do not add a forced origin state, impose a minimum nomination, or reroll a zero result.
If that union has no viable sovereign origin, reject the proposal before actual Event 091 firing.
Consume no fire-once history, opening Chaos, asset payment, or super-event announcement, retain the accumulated weight, and remove the candidate only for that selection cycle.
Retain the rejected proposal's random draws and reservation identity until a meaningful relevant world-state change authorizes review.
Reopening UI, repeated callbacks, or save reload cannot fish for another draw.
This parent-accepted policy preserves proportional arithmetic and makes a rare selected proposal fail feasibility instead of creating a successfully fired event without Lenin.

Lenin's origin is sovereign World Revolution territory even when its former owner or controller joins.
The direct switch opportunity belongs only to the human country whose physical opening territory contains that origin.
Use frozen controller identity as the accepted meaning of physical territory for the default switch offer in an occupation, with legal-owner disclosure in the report.
Switching is optional and does not undo the uprising for a player who stays.

## Atomic snapshot and late political choices

The opening has an atomic planning boundary before it has an atomic mutation boundary.
One guarded synchronous proposal effect freezes country eligibility, ordinary-world ideology average, country pools, population and military inputs, state owner and controller, Event 001 lineage, local levels, and ruling ideology for the accepted transaction.
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
A current Stalin-led Soviet Union refuses immediately when alignment commits.
A current Trotsky-led Soviet Union joins immediately as an autonomous partner at that same committing boundary.
These fixed routes do not wait for a modal popup.
Snapshot leadership provides narrative history and AI context, while the current active leader controls the committed result.
An ordinary pending request rechecks current leadership so an old popup cannot obtain a stale Trotsky join or evade a current Stalin refusal.

Ordinary responses use the native thirteen-day reply timeout with refusal as the default.
An unanswered request receives no joining consent.
Lenin imposes refusal and war through the declared ultimatum expiry and exact request resolver.
That imposed consequence is distinct from consent to affiliation or annexation.
A duplicate request must not overwrite the pending receipt.
Closed requests cannot apply faction entry, war entry, aid, or state disposition twice.

### Owner and controller rights

Each physical state has one final disposition transaction with separate ownership and control fields.
The final rights are derived from both participants' responses and the sovereign-origin rule.
Implementation must use documented native semantics for changing those rights independently.
An engine effect that necessarily changes both cannot be treated as proof of a split transfer.

| Frozen owner | Frozen controller | Recommended selected-state disposition |
| --- | --- | --- |
| Ordinary joiner | Same joiner | Ownership and control remain local, with an allied revolutionary base |
| Ordinary enemy or refuser | Same enemy or refuser | Ownership and control move to World Revolution |
| Joiner | Hostile occupier | Joiner retains ownership, World Revolution takes hostile occupation control as an allied base |
| Enemy or refuser | Joiner | World Revolution receives ownership, joiner retains local control as an allied base |
| Two different joiners | Two different joiners | Preserve current owner and controller relationships, register one allied base and no duplicate unit grant |
| Two different enemies or refusers | Two different enemies or refusers | World Revolution receives the single physical state, retaining both displacement histories |
| Either participant still pending | Either participant still pending | Apply only already authorized nonpending rights when native semantics permit, otherwise preserve a guarded provisional disposition |
| Valid special actor already controls state | Any ordinary claimant | Preserve special actor exclusion and record an unresolved contested claim unless the exact cross-event capture contract permits mutation |
| Any owner and controller | Sovereign origin | World Revolution receives sovereign ownership and control exactly once |

These policies preserve a joined controller's local administration and a joined owner's retained title wherever that is compatible with one physical state.
Their effects on existing wars, occupation, supplies, and garrisons require native verification.
Do not silently replace split rights with two sequential whole-state transfers.

For an Event 001 rebel, political disposition is owned by its inheritance choice.
Joining, subordinate survival, voluntary absorption, or refusal preserves the observed army and stockpiles through the appropriate real transaction.
A refuser retains its human rebel country and non-origin bases and becomes an enemy. The sovereign-origin exception still applies and can cause real collapse or valid exile if it was the last state.
Its established territory remains guaranteed in the opening history and selection receipt, with disposition `inherited base denied Lenin by rebel refusal`.
Preserving history does not authorize unconditional annexation of that polity.

## Public values and internal bookkeeping

Revolutionary Momentum is the sole public global event value.
It ranges from zero to one hundred, with broad power stages at twenty, forty, sixty, and eighty.
Lenin's Influence is the sole persistent event-specific value that an ordinary joined country actively manages.
It ranges from zero to one hundred, with stages at twenty, forty, sixty, eighty, and complete binding pressure at one hundred. A real sovereignty transaction still determines political status.

State provenance, nomination receipts, force budgets, resource reservations, exact casualties, anchor identity, operation dates, alignment status, and achievement evidence are internal bookkeeping.
They do not become additional currencies or visible meters.
World-rule eligibility is shown as a broad map objective or public threshold requirement when needed.
The player does not manage a separate world-share meter alongside Momentum.

Momentum is refreshed from maintained physical territorial coverage and concrete outcomes.
The initial formula assigns forty-five points to territorial rule, fifteen to unique strategic military outcomes, fifteen to functioning political institutions, ten to active regional commands, ten to living transformation, and five to earned current campaign objectives.
Territorial credit saturates at fifty percent population-weighted world rule, political credit at twenty-five percent of frozen ordinary institutional weight, and transformation credit at one hundred thousand unique living person-equivalents.
Political weight combines equal shares of frozen legally owned population and actual civilian plus military factories, with a single-denominator fallback when needed.
Direct councils, absorbed institutions, and contributing partners use the same unique lineage, so the collective route can earn full political credit through functioning human institutions and real contributions without forced absorption or an external partner.
The exact normalizations and review receipts appear in `state_and_transaction_contracts.md`.
Do not sum overlapping country nominations as territory.
Persistent footprint uses state receipts and current control, while one-time victories, joins, commands, and incorporation premiums have unique outcome receipts.
Losing and regaining a threshold changes current powers without issuing the same one-time reinforcement, Chaos premium, or achievement event again.
The public twenty-point thresholds have no hidden general hysteresis.

Distributed survival is a separate network capability that can activate at sixty Momentum and fails below forty after the declared survival interval.
This explicit hysteresis prevents one marginal defeat from alternately creating and destroying the network.
It grants no second public value.
The next public power threshold must still describe the actual current Momentum.

## Influence and sovereignty lifecycle

Critical Influence begins at eighty and starts a proposed 180-day struggle for sovereignty.
Influence can reach one hundred and display the full portrait stage while the 180-day critical struggle remains active.
Automatic binding cannot occur before that critical deadline, even if the numeric value is already one hundred.
Only a separate explicit voluntary-submission receipt permits earlier binding.
An institutional concession that raises Influence to one hundred is not submission consent, and there is no hidden ninety-five cap.
A real subject or accepted equivalent binding transaction is required before the country is treated as ruled.
Critical expiry can cause a specified institutional loss and conditional puppet resolution, but never direct annexation.
If the full binding gate is unmet, the country remains in a severe political crisis and keeps independence actions.

The proposed 120-day annex interval starts only after verified subject creation.
A stored timer or Influence value alone cannot prove puppet status.
On the completion date, independence remains available until annexation's final transaction consumes the exact active receipt.
Queued expiry events must match the current generation and stored date, and repeated delivery must not annex twice.

Independence is always available without an added payment gate for ordinary joiners and subjects.
Preparing an army and removing compromised institutions can cost resources and time.
The decisive breakaway itself leaves the faction, cancels annexation, terminates all future Influence increases, and declares war on Lenin through one guarded transaction.
Existing third-eye institutions and army dependencies remain as problems with recovery routes.
Lowering Influence does not revive an already cancelled annex receipt or restore sovereignty while a country remains a real subject without its own valid independence transaction.

Trotsky's autonomous-partner receipt is permanent for this crisis once his accepted partnership is established.
The Soviet Union joins when its current active leader is Trotsky.
An accepted Trotsky-led country outside the Soviet Union can receive the same protected contract after identity verification.
Immunity covers Influence, compulsory binding directives, forced puppeting, annex countdowns, Red World acceleration, and any equivalent adapter attempting the same result.
Leader replacement, temporary faction exit, or a generic ideological change must not silently revoke that protection.
Separate voluntary political choices or normal military defeat follow their own contracts and cannot masquerade as an Influence annexation.

## Finite distributed survival and defeat

Use one origin anchor and at most one registered regional anchor per inhabited continental-command slot.
The six proposed regional slots are Europe, Asia, Africa, North America, South America, and Oceania.
There are at most seven network anchors.
A transformed leader can be the custodian of an existing regional anchor, but every transformed leader must not create another anchor.
One physical site cannot occupy two anchor slots.

Each slot has immutable identity, state pointer, responsible command, generation, activation receipt, and a lifecycle state.
Capture, destruction, voluntary breakaway, or proven severance closes its current anchor receipt.
Opening callbacks and inherited strongholds cannot create additional slots.
A permanently destroyed command cannot be rebuilt in a different state merely to evade defeat or farm another Chaos reward.
Any accepted restoration of a damaged but undestroyed anchor retains the same identity and consumes a real action, resources, time, and prior receipt.

Capturing one disconnected capital does not automatically defeat a high-Momentum network.
The body, origin, finite surviving commands, actual territorial footprint, bound supporters, and Momentum determine continuity.
When the body and origin are secured and Momentum stays below forty, a ninety-day severance objective begins.
Full defeat requires every remaining registered anchor to be permanently destroyed or individually proven severed.
Low Momentum alone does not erase active supernatural commands.
At high Momentum, surviving anchors keep the crisis active while opponents liberate territory and attack its finite sites.
One body reconstitution is allowed per campaign from a pre-existing surviving anchor after 180 days of valid preparation with a paid finite transformed cohort and real equipment.
It cannot use another manifestation seed, Trotsky, independent allies, a newly invented anchor, or stale authority.
The detailed counterpart missions and receipt rules live in `state_and_transaction_contracts.md`.

Native capital relocation among already held World Revolution states is the preferred continuity mechanism.
If the country loses every native state while a bound-subject anchor remains, a stateless ledger can retain pending defeat analysis but cannot pretend that the country satisfies the Red World existence gate.
Restoring actual World Revolution sovereignty from that anchor is a distinct contested transfer requiring verified native mechanics and the supporter contract.
Trotsky and independent allies cannot supply such a transfer automatically.
If this continuation is technically unsupported, it is a blocked requested branch, not permission to call a phantom country alive.

Defeat closes the active crisis generation, stops supernatural reinforcement, cancels unconsumed Influence and annex receipts, releases surviving supporters through documented political transitions, clears only this event's world-threat source, and refreshes the shared aggregate.
History, dead people, public responsibility, achievement receipts, original nomination records, and liberated-state provenance remain.
Ordinary communist politics are not globally set to zero.
Lenin's body-capture aftermath cannot reinsert Event 091 into the major pool.

## The Red World denominator and terminal boundary

Use population-weighted inhabited territory rather than a count of empty or tiny states.
Freeze each valid inhabited state's baseline civilian population at the opening snapshot and sum it once for the world denominator.
This world denominator is separate from the arithmetic country mean used by Event 091's above-five-percent availability gate.
All baseline inhabited world territory belongs in the denominator, including ordinary territory under special-actor occupation when it is part of the inhabited map.
Do not exclude enemies' territory merely because it cannot enter the ordinary opening pool.

The fixed denominator prevents killing civilians, destroying infrastructure, or changing the current census from increasing world rule by shrinking the world being measured.
Migrations and conversions do not move that historical territorial weight.
This is an explicit interpretation of meaningful inhabited-world control, measured using opening population weights.
It must be described in design documentation rather than implied to be a live count of surviving people.

Count a state's weight once when its actual current controller is World Revolution, a real Lenin subject, or a fully bound supporter with a completed binding transaction.
Ownership without control gives no current ruled credit.
Faction membership, assistance, critical Influence at eighty, or an uncommitted numeric one hundred gives no ruled credit.
Independent Trotsky partners and other genuinely autonomous allies do not count.
The recommended binding threshold is complete Influence at one hundred followed by the real subject transaction, with any documented equivalent binding government requiring the same command and sovereignty proof.

The Red World final gate requires strict Chaos greater than one thousand, strict ruled share greater than one half, a real existing World Revolution country and Lenin identity, no incompatible active terminal state, and the shared global and branch-specific enable controls.
Exactly one thousand Chaos and exactly fifty percent fail.
The gate consumes one terminal-generation receipt before the shared `world_end` transaction, public scenario registration, presentation, and ordinary-event shutdown.
The terminal phase accelerates existing finite systems through their owners and offers final political choices.
It does not instantly annex every ally or revoke Trotsky's immunity.
Pause and snapshot existing subject annex deadlines once during the thirteen-day final response so an old expiry cannot absorb a country before its choice.
An ordinary joiner's explicit stay commits real binding immediately and opens a ninety-day terminal annex interval.
An existing subject's explicit stay resumes the shorter of its snapshotted remaining days and ninety days from the response.
Refusal or nonconsenting timeout resolves independence and war.
The one-time pause cannot be refreshed through UI, leader changes, callbacks, or reload, and free independence remains available until the exact annex transaction commits.
Trotsky chooses protected autonomy concord or explicit political break, with no surrender route.

## Physical people, transformed people, and deaths

Conversion changes a living person's state and military availability.
It does not itself kill them or create a second recruitable person.
Keep living conversion provenance separate from native civilian-population mutation, recruited manpower, military casualties, and Deaths registration.
Only one muster owner may reserve and consume a real manpower or population-backed cohort for a new formation.
Observe the native spawn or transfer before deciding whether another debit is needed.

The parent's proposed 10,000-person-equivalent First Coming seed and three later 10,000-person-equivalent manifestation milestones are finite supernatural exceptions.
They require immutable one-time campaign receipts and include only the explicitly finite tool-and-basic-weapon package. They grant no tanks, trucks, aircraft, ships, or fuel. Ongoing ammunition and supply follow the normal equipment and supply owners.
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
