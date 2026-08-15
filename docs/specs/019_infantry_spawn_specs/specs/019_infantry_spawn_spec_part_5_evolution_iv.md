# Event 19 Infantry Spawn
## Part 5: Evolution IV and the Chaos unit registry

## Evolution IV: Anomalous Muster

### Identity change

Evolution IV lets the Event 19 formation system draw from registered Chaos unit families. The event stops treating every formation as an ordinary military anomaly and begins handling units whose existence depends on supernatural, biological, material, or future Chaos Redux systems.

The evolution must remain dynamic. Event 19 should not contain a permanent handwritten list that future agents must update every time a new Chaos unit enters the mod. Instead, Chaos unit families opt into a reusable registry that records whether the family can be trained, spawned, used in random templates, or create a derivative revolt country.

The registry is an explicit safety boundary. Future units do not enter Event 19 merely because they exist. A developer adds one registry entry when the unit family is ready. Event 19 then reads that entry automatically.

## Entry conditions

Evolution IV becomes possible when several of these conditions exist:

- global chaos reaches a very high evolution range
- Evolution III requests have been used extensively
- anomalous unit systems already exist in the campaign
- one or more parent Chaos events have revealed compatible unit families
- claimant crises have normalized military formations outside ordinary state authority
- countries have repeatedly preserved technology-locked or impossible formations

The evolution can also be forced by the triggerable scenario’s anomalous type. A forced scenario entry is tightly scoped and does not mark unrelated parent events as fired.

## Active-event evolution

A country with an active Evolution III crisis gains:

- the Anomalous Registry area in the Muster Board
- family eligibility display
- trainable versus spawn-only rules
- family-specific sustainment and containment actions
- Anomalous Saturation
- derivative revolt risk
- the possibility that a future random draw uses one or more registered families

Existing ordinary random lots remain ordinary. They do not transform into zombies, ghosts, golems, or other units without a specific event or decision.

## Pre-fire evolved opening

A country entering Event 19 for the first time under Evolution IV receives the Muster Board and registry but does not automatically gain every available Chaos unit.

The starting package depends on:

- which registered families are globally or locally eligible
- whether the family's parent event has revealed the unit, if the registry requires that condition
- country ideology and special-country identity
- local terrain and industry
- current war state
- Muster Control and Army Congestion
- scenario overrides

The first anomalous formation is a one-time country-level reception incident.
The registry selects one currently eligible complete provider row, then freezes
its index, family identity, provider identity, visual profile, and a monotonic
transaction nonce before dispatch. The selected host-scene profile and provider
package cannot be replaced by a same-tick eligibility change. Delayed execution
requires those exact values, a positive nonce, the same aligned row, and contract
version 4, but does not rerun current provider eligibility after the promise is
issued. Partial, mismatched, or out-of-range frozen evidence fails visibly and
never substitutes another family.

The visible incident offers guarded cantonment, a negotiated command compact,
and refusal. Either acceptance creates exactly one provider package through the
existing snapshot, materialize, prove, and rollback transaction; it consumes no
ordinary provider price, request overhead, cooldown, or request counter.
Cantonment increases control and relieves anomalous pressure. Negotiation grants
more immediate military value while conceding control and accepting pressure.
Refusal creates no family formation and pays political and command costs for a
stronger containment position.

Outcome flags and Event Log history are written only after the selected effects
prove. A proved rollback produces a visible failed-reception consequence; an
unproved rollback locks and quarantines the management surface. If no provider
is eligible on entry, the country retains one pending state and retries only on
its country-local Event 19 pulse. A normal active Evolution IV transition, a
scenario actor, or a derivative country never receives or consumes this
pre-fire incident.

## Chaos unit family registry

### Registry purpose

The registry provides one source of truth for Event 19 compatibility. It can also support future systems that need to know whether a unit is trainable, spawn-only, derivative-capable, or isolated from its parent event. The live provider contract is version 4.

The event-agnostic Chaos family contract should remain a shared, documented
scripted system. This implementation uses exactly one dedicated Event 19
registry code file for the ordinary table and the three baseline zombie, ghost,
and golem bindings. The installed mutated zombie, elephant, Africa strange,
additional ghost, cave, rat, and CBRN families register through owner-side
adapters in their existing integration surfaces. Registry constants and
triggers belong in the existing Event 19 constants and trigger files, and
startup calls belong in existing parent on-actions. A future family keeps its
complete registration and provider callbacks in its own existing integration
surface. Do not create family-specific or additional Event 19 registry files.

### Required registry fields

Each family entry needs the following design fields.

| Field | Purpose |
| --- | --- |
| Family key | Stable internal family identifier |
| Source system | Parent event or mechanic that owns the original unit |
| Event 19 eligibility | Whether the family can enter the Infantry Spawn system |
| Availability mode | `trainable`, `spawn_only`, or `trainable_and_spawnable` |
| Allowed unit variants | Exact battalions or templates Event 19 may use |
| Ordinary random-template access | Whether the family can mix with ordinary battalions |
| Family-only lot rule | Whether it must appear in a separate lot |
| Initial equipment or sustainment rule | How the first unit exists and what keeps it operational |
| Reinforcement rule | How more units can be obtained |
| Containment rule | What lowers saturation or revolt risk |
| Derivative profile | Which derivative country package, if any, it can create |
| Parent isolation rule | Flags, tags, counts, triggers, and super-events that Event 19 must not set |
| AI class | How ordinary and derivative AI value the family |
| Visual family | Icons, massed-host identity scene in the fixed portrait slot, flag, report image, and UI motif |
| Cleanup profile and callback | Which cleanup contract applies and how provider-owned public additions are removed before shared teardown |
| Migration note | What happens when the family definition changes in a later mod version |

Contract version 4 makes the parent-isolation rule executable. Parent event
actors carry `chaos_unit_family_parent_actor`. Before derivative creation, the
shared `infantry_spawn_parent_event_identity_is_absent` boundary rejects that
marker together with provider-specific parent tags, original tags, country flags,
stages, counts, evolutions, super-events, and terminal progression. Event 19
clears `infantry_spawn_derivative_provider_parent_isolation_proved` before setup.
The provider sets a positive proof only after every shared and parent-specific
check passes, then calls the shared derivative initializer. Missing proof fails
closed. The provider owns these family-specific checks beside its one registration
entry, so a future family does not require an Event 19 list, map, or registry-file
edit.

The shared initializer owns only the private ledger, isolation boundary, generic
opening burdens, and lifecycle locks. Provider setup owns its public identity,
leadership or council, family ideas, route package or adapted equivalent, and
release report. Event 19 clears
`infantry_spawn_derivative_provider_public_package_proved` before dispatch, and
the provider sets that positive proof only after its complete public surface
succeeds. Future-family public identity must not be implemented as another switch
inside Event 19. A nonhuman derivative with either proof missing cannot classify,
materialize, enter a scenario roster, or unlock.

For defeat and final teardown, Event 19 clears the cleanup proof and dispatches
`chaos_unit_family_provider_[provider]_event19_cleanup_derivative`. The provider
must remove every provider-owned public addition before setting
`infantry_spawn_derivative_provider_cleanup_proved` for the requested phase. Event
19 owns exact tracked-formation proofs, private ledgers, common derivative ideas
and missions, common state markers, common flags and variables, and the remaining
shared cleanup surfaces. Cleanup selects the immutable lifecycle owner by the
actor's exact stored family/provider pair rather than current generation policy,
so a disabled or spawn-forbidden row cannot strand a derivative. Initial-provider
authority is retired only while its provider-leadership receipt remains; claimant
promotion clears that receipt. Provider 501 must also revoke its trainable-family
entry and lock every recorded family-501 template, including templates with no
remaining live divisions. Missing provider proof fails closed and blocks the
shared commit.

### Explicit opt-in and visual profile rule

A future Chaos unit family is excluded until it has an explicit registry entry.

This prevents accidental inclusion of:

- boss units
- unique story units
- one-off super-event actors
- units that depend on parent-event variables
- units whose equipment cannot be represented safely
- units that would trigger an unrelated world-end or country package

The developer adding a new family defines one complete generic provider
registration and its Event 19 callbacks in that family's own integration
surface, adds one startup registration call to the family's existing parent
on-action, and updates its documentation. Event 19's generic query and
generation logic requires no family-list, localisation-map, picture-map, or
registry-file edit. This is one external registration row plus the complete
provider callbacks, including derivative setup and cleanup. It never adds another
Event 19 registry file.

The initial visual profiles are exact owned bindings. Profile 1 belongs only to
family 501 and provider 501, profile 2 only to family 502 and provider 502, and
profile 3 only to family 503 and provider 503. An external future provider must
explicitly register `constant:chaos_unit_family_visual_profile.provider_neutral_army`,
value 999, unless a later supported provider-owned profile exists. Profile 999
uses only the identity-neutral Event 19 army or massed-host presentation and
rejects the family and provider IDs reserved by the three initial bindings. An
unknown positive profile fails registration, and every Event 19 consumer rejects
an unsupported or mismatched runtime row.

### Registry compatibility audit

Every registered family must pass a narrow compatibility review before use.

The review asks:

- Can the unit be created safely outside the parent event?
- Does it need a specific country, idea, technology, resource, or event target?
- Can ordinary countries control it?
- Is it trainable or spawn-only?
- Does disbanding or template conversion create an exploit?
- Does its combat or casualty behavior assume parent flags?
- Would parent event triggers count it by tag, original tag, unit type, or country flag?
- What must be excluded from parent counts?
- Can the family create a weaker derivative state without copying the parent event?
- Which assets and localisation states are required?

No family is marked eligible until these questions have answers.

## Initial registry entries

The baseline bindings and owner-side provider rows are required by the design. Exact installed identifiers and their support boundaries are verified in `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`.

### Base Zombie Family

#### Eligibility

Eligible under Evolution IV.

#### Availability mode

Trainable and spawnable, but only the base zombie unit is allowed.

#### Excluded variants

All stronger zombie variants, mutation lines, evolved zombie templates, boss units, and parent-event special formations remain excluded from training. Installed mutated, demonic, wendigo, and armoured variants may arrive through owner-side provider 511 as spawn-only family lots. They never enter the trainable zombie ledger or parent outbreak package.

#### Training rule

An ordinary country can unlock training of the base zombie unit only after completing a containment and command decision chain.

Training uses family-appropriate costs such as:

- population or manpower burden
- containment capacity
- equipment or facility burden
- Anomalous Saturation
- stability or legitimacy risk

It must not grant the parent Zombie Outbreak recruitment, conversion, league, mutation, or world-end systems.

#### Spawn rule

Random draws can create base zombie lots. These lots should normally be family-only rather than mixed with ordinary battalions unless a future verified compatibility rule allows mixed formations.

#### Parent isolation

Event 19 zombie units and derivative states must not:

- use the parent zombie tag or original tag identity
- set parent outbreak country flags
- enter parent zombie-country counts
- advance parent event stages or evolutions
- unlock parent super-events
- join parent leagues automatically
- satisfy parent world-end conditions
- use advanced zombie variants

### Ghost Family

#### Eligibility

Eligible under Evolution IV.

#### Availability mode

Spawn-only.

#### Training rule

No ordinary training button exists. Ghost divisions are created only through the registry spawn helper, event lots, family incidents, derivative country mechanics, or explicit future systems.

#### Sustainment rule

Ghost formations use a nonstandard persistence or manifestation burden rather than normal production alone. The exact representation must follow the verified ghost unit design.

#### Parent isolation

Event 19 ghost units and derivative states must not:

- use the Death tag or original tag identity
- set the parent Death country flag
- enter parent Death consumed-state, soul, continent, or country counts
- advance parent Death event stages or evolutions
- show parent Death super-events
- inherit the full rapid wasteland system
- satisfy parent world-end conditions

### Golem Family

#### Eligibility

Eligible under Evolution IV once the actual golem unit and parent system are verified.

#### Availability mode

The live provider 503 row is spawn-only.

#### Training rule

No normal training button exists unless the parent golem design later defines a safe trainable base unit and the registry entry is deliberately changed.

#### Sustainment rule

Golems require material, quarry, industry, or binding capacity. Ordinary equipment replacement should not silently reproduce them.

#### Parent isolation

Event 19 golem units and derivative states must not set parent golem event flags, stage counters, super-events, or world-end conditions.

The installed golem identifier is verified locally as `coal_golem`. It remains provider 503, spawn-only, and isolated from the KMB parent package.

## Ordinary country anomalous management

### Family reception incident

The pre-fire Evolution IV opening uses the one-time frozen-row reception
transaction above. Later first contact with another family can use a
family-specific report direction, but it must not reopen or duplicate the
initial provider package.

The report should show what soldiers and civilians can observe:

- zombies moving under military escort
- ghost formations occupying positions without ordinary camp life
- golems standing near factories, quarries, or rail yards
- future registered units using their own concrete visual signs

The text should not explain hidden parent-event mechanics or call the family a copy of another event.

### Sealed Cantonment

Working role:

- isolates anomalous lots in selected states
- lowers immediate deployment value
- reduces revolt risk
- costs guards, supply, local capacity, or stability

### Family Liaison Office

Working role:

- creates a controlled command channel
- improves readiness and reduces accidental incidents
- raises the family’s institutional permanence

The public country name should never become an administrative office name. This is an internal mechanic only.

### Restricted Deployment Order

Working role:

- limits anomalous divisions to selected fronts, states, or roles
- reduces saturation growth and civilian impact
- lowers strategic flexibility

### Sustain the Formation

Working role:

- pays family-specific resources
- keeps units operational
- raises saturation when used repeatedly

### Purge or Disperse the Lot

Working role:

- attempts to remove an anomalous lot
- has family-specific success and failure behavior
- cannot create free resources

### Authorize Family Recruitment

Working role:

- appears only for a trainable registry entry
- base zombies use this path
- stronger zombie types remain unavailable to training, while the installed provider 511 spawn-only lot can materialize them under its owner gate

### Request an Anomalous Draw

Working role:

- expands the random request pool to registered families
- high cost and saturation increase
- result remains unknown until paid

## Anomalous Saturation

### Components

Anomalous Saturation should be computed from named components rather than move as an unexplained number.

Possible components:

- number of anomalous divisions relative to total army
- number of active families
- family combat activity
- unresolved sustainment debt
- unrestricted deployment
- claimant control
- repeat anomalous requests
- family-specific incidents
- containment and cantonment capacity

The UI should show a readable breakdown.

### Saturation bands

#### Trace

A small number of controlled units. Derivative revolt is unavailable unless a specific claimant event overrides it.

#### Embedded

Anomalous units are a visible military institution. Family decisions and political disputes expand.

#### Dominant

Anomalous formations control important districts or constitute a major share of the army. Derivative revolt becomes a real risk.

#### Breach

The state has lost effective control. A derivative country, claimant takeover, or multi-family crisis can begin.

The exact thresholds should be dynamic and centralized.

## Family-specific risk

Anomalous Saturation is an aggregate. Each family also tracks a local pressure or presence value when needed.

This prevents a country with many well-contained zombie units from automatically producing a ghost derivative state. A derivative revolt requires that family’s own presence, units, and failure conditions.

## Multi-family formations

Ordinary Evolution IV draws can produce more than one anomalous family only when every involved registry entry allows mixed use.

Current registry policy:

- zombies are family-only
- ghosts are family-only
- golems are family-only
- future families choose explicitly

Mixed anomalous formations are reserved for rare high-chaos content and need their own compatibility review. They should not be the routine source of absurdity because Evolution III already provides mixed ordinary battalions.

## Claimant interaction

Claimants can seek control of anomalous units.

Archetype tendencies:

- Field Prophets aggressively seek anomalous draws and liaison authority
- Iron Saints seek family-only hosts and emergency powers
- Quartermaster Sovereigns seek sustainment infrastructure
- Hollow Marshals seek restricted command and derivative takeover opportunities
- Barracks Tribunes prefer trainable base zombies or ordinary troops over spawn-only families unless local conditions change

Assigning anomalous formations to a claimant raises both Claimant Influence and Anomalous Saturation.

A claimant revolt with anomalous units can form a derivative state when the registry profile permits it.

The release router records an anomalous-claimant mode for that union. Its exact
transfer set contains only claimant-loyal rows and exact rows belonging to the
selected family. Claimant identity remains the political cause, while the
provider profile supplies the host identity and derivative family package.

## Derivative revolt trigger

A derivative country can form when all relevant conditions align:

- the family has a derivative profile
- the country has enough family presence or units
- saturation or family pressure is high
- central control is weak or a claimant has high influence
- a coherent territorial base can be built
- no conflicting active terminal transition makes the release unsafe

The revolt should not occur from one accidental unit under otherwise excellent control except through the maximum triggerable scenario.

Natural Evolution IV release has two distinct family-capable modes:

- An anomalous claimant release requires a valid claimant plus a complete
  eligible provider row and transfers the exact union described above.
- A claimant-independent family breach requires no claimant. It requires exact
  claimant-free formations of one eligible registered family, sufficient family
  presence, the centralized pressure and saturation gates, and weak central
  control. It transfers only those family rows and installs the provider's
  commander or council identity.

Both modes freeze the selected row and release mode before actor creation and
use the shared exact recreate, prove, delete transaction. A pre-commit family
failure restores the source and exposes a visible deferred-containment outcome.
For a one-state source, a claimant-independent family breach can use the same
tag only after proving that the country has exactly one controlled state, every
live Event 19 formation belongs to the selected claimant-free family set, and
all private ledgers align. Only then does the provider takeover replace the
ordinary package; it never creates a zero-state actor or a self-war.

## Derivative country strength principle

Derivative countries are intentionally weaker than the parent-event countries associated with the same unit family.

Their diplomacy begins from universal hostility toward ordinary states. They should attack reachable countries aggressively after securing the opening revolt, with the former parent and adjacent weak states as first priorities. This does not require suicidal declarations against unreachable overseas targets.

They begin with:

- the revolting Event 19 units they actually controlled
- limited local equipment and manpower or family sustainment
- a weak or mixed starting idea package
- a narrow shared focus overlay or tree
- aggressive regional AI

They do not begin with:

- parent event global mechanics
- parent stage progress
- parent super-events
- parent world-end eligibility
- parent boss units
- free reinforcement beyond their family profile

Paid reinforcement materialization is atomic. The post-payment snapshot owns
all provisional engine templates and divisions, aligned generation, lot, unit,
obligation, and auxiliary tails, and affected aggregates. Provider failure must
prove exact rollback before any payment refund. An unproved rollback remains
quarantined and unrefunded so a surviving partial formation cannot be obtained
for free.

Their danger comes from surprise, local force concentration, unusual units, and a hostile regional plan.

## Derivative identity isolation

### Tag and origin model

The preferred design is a dynamic civil-war or dynamic-country creation path with event-specific origin flags and species-specific cosmetic identity.

Requirements:

- do not use the parent zombie or Death tag
- do not use a parent original tag identity that parent triggers count
- do not set parent actor flags
- set an Event 19 derivative origin flag
- set a family-specific derivative flag
- record the former parent country and revolt generation through safe event targets or variables
- use distinct cosmetic names and flags

Dynamic country creation and the proved same-tag takeover are the only supported identity paths. Event 19 has no fixed pool of permanent tags and no fixed-tag fallback.

### Shared classification

Every derivative country must be registered through the shared Chaos Redux classification system.

- `is_special_chaos_country`: yes
- `is_actual_nonhuman_country`: yes for zombie, ghost, golem, and future actually nonhuman derivatives

Do not create parallel Event 19 classifiers when the shared triggers can express the category.

### Parent-system exclusions

Parent event triggers must be audited for all identity tests they use:

- tag
- original tag
- country flag
- unit type
- idea
- global count
- state marker
- scripted trigger

A derivative state is excluded from parent progression by explicit origin logic. It can still interact with the parent system through later deliberately designed compatibility events, but isolation remains the mandatory baseline.

## Zombie derivative profile

### Military identity

- base zombie units only
- trainable through a limited family decision
- no advanced mutation or specialist zombie units
- ordinary auxiliary units only when a focus or captured population system explicitly permits them

### Starting weakness

Working idea direction: fragmented command.

This should create real penalties to coordination, reinforcement, planning, supply, or leadership. It is not the full parent zombie fragmentation mechanic unless that mechanic is safely reusable without advancing the parent event.

### Growth

Growth comes from:

- base zombie training
- limited casualty or population conversion at much weaker rates than the parent event, if verified safe
- capturing local stockpiles
- integrating scattered derivative bands
- focus and decision completion

### Limits

- no parent mutation paths
- no parent league or confederation system
- no parent super-events
- no parent global outbreak spread
- no world-end path

## Ghost derivative profile

### Military identity

- spawn-only ghost divisions
- no ordinary training queue
- reinforcement through haunting, manifestation, battlefield loss, or state pressure decisions

### Population and wasteland behavior

The derivative can create slow population decline and slow wasteland development.

The effect must be much weaker than the parent Death system.

Design direction:

- population loss occurs over long intervals
- wasteland pressure requires repeated occupation, high ghost presence, or focus completion
- one state does not become wasteland instantly
- the shared Deaths system records actual population loss when used
- the derivative does not enter parent consumed-state counts

### Limits

- no parent soul economy
- no parent rapid state consumption
- no parent continent or world progression
- no parent Death super-event
- no world-end path

## Golem derivative profile

### Military identity

- spawn-only golem formations
- slow, durable, supply-heavy forces
- weaker combat and replacement than the parent golem country or event actor

### Growth

Growth comes from:

- quarry or resource control
- industrial binding projects
- captured heavy equipment or construction capacity
- family-specific focus and decision progress

### Starting weakness

The country should suffer from:

- extremely slow reinforcement
- limited strategic mobility
- high material demand
- weak diplomacy and administration
- reliance on a small number of powerful units

### Limits

- no parent golem endgame
- no automatic replication through normal manpower
- no parent super-event or stage flags
- no world-end path

## Future derivative profiles

A future family can opt into derivative behavior by naming one of these profile classes or defining a new documented class.

Possible reusable profile classes:

- trainable swarm
- spawn-only apparition
- material construct
- biological host
- machine collective
- singular elite host

A profile defines:

- release conditions
- starting package
- recruitment method
- sustainment
- aggression
- territorial effect
- parent isolation
- provider-owned public package
- provider-owned public cleanup
- focus overlay modules
- assets

Its provider implementation also owns the exact positive parent-isolation and
public-package proofs required by the shared derivative classifier. It owns the
defeat and final cleanup callback for its public additions as well. Profile
metadata without those executable proofs is not sufficient to release or cleanly
retire a derivative.

The Event 19 implementation should be modular enough that future families reuse profile logic rather than copy the entire country package.

## Multi-family breach

A country with several dominant anomalous families can experience a multi-family crisis.

Current outcome:

- the strongest family receives derivative priority
- weaker families remain with the parent, are destroyed, or become contested lots
- rival derivative revolts can occur only at extreme saturation or in the triggerable scenario

The ordinary automatic event should avoid creating three simultaneous microstates in every country. Maximum-chaos multi-revolt behavior belongs to rare conditions and the manual scenario.

## Evolution IV AI for ordinary countries

AI evaluates each family by:

- immediate combat need
- sustainment ability
- supply compatibility
- current claimant influence
- saturation
- ideology and risk tolerance
- parent-event threat status
- enemy composition

AI behavior direction:

- stable professional AI uses one controlled family at most
- desperate wartime AI accepts higher saturation
- high-chaos gambler AI requests anomalous draws
- low-industry AI avoids golem sustainment unless it controls resources
- low-stability AI avoids granting claimant control of anomalous units when possible
- AI stops training base zombies when saturation is near breach unless facing capitulation
- AI never attempts to train spawn-only ghosts or golems

## Evolution IV acceptance criteria

Evolution IV is satisfied when:

- Event 19 reads an explicit Chaos unit family registry
- Event 19 keeps exactly one dedicated registry code file
- a future family joins through one external registration row, its complete provider callbacks, and a startup call without an Event 19 list, map, or file edit
- unregistered future families remain excluded until explicit opt-in
- profiles 1, 2, and 3 remain bound to the exact 501, 502, and 503 family-provider pairs
- an external provider explicitly chooses profile 999 unless a later supported owned profile exists, while unknown positive profiles fail registration and all Event 19 consumers
- base zombies are the only zombie variant made trainable
- ghosts and golems remain registered as spawn-only
- family-specific sustainment and containment exist
- Anomalous Saturation is visible and component-based
- claimant control increases anomalous risk
- derivative countries use distinct origin, identity, flags, and packages
- shared and parent-specific identity checks block parent actors before derivative creation
- every nonhuman derivative has positive parent-isolation and public-package proofs
- provider cleanup removes provider-owned public additions and proves defeat or final cleanup before Event 19 clears private ledgers and common surfaces
- parent Zombie Outbreak, Death, golem, and future event progression remain isolated
- derivative countries are registered in shared special and nonhuman classifiers
- zombie, ghost, and golem derivatives are weaker than parent-event countries
- ghost population and wasteland effects are gradual
- no derivative path becomes a direct world-end scenario
