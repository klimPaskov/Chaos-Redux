# Dynamic Value Space

## The practical meaning of full dynamic coverage

Event 66 must not contain a central handpicked list of favored values.
Its core logic reads a registry populated by the systems that own those values.
A new Chaos Redux mechanic joins Abundance by publishing an adapter through the shared Event 66 contract.
The event generator does not need to be redesigned when that happens.

HOI4 script should not be treated as if it can inspect every arbitrary variable, modifier, DLC database, or event ledger automatically.
A raw reflection claim would create false coverage and unsafe writes.
The complete design therefore uses owner registration and a coverage audit.
Every owner is responsible for exposing every player-meaningful value that can safely become abundant.
Event 66 is responsible for consuming those providers without knowing their internal storage.

## Provider responsibilities

Each provider represents one semantic value or one dynamic family of semantic values.
It supplies enough information for Event 66 to decide whether the candidate exists, display it, weight it, store it, apply it, and verify the result.

A provider declares:

- a stable provider identity and schema version
- the owning system or event family
- a short display name and a full tooltip name
- an icon or texticon when a valid existing one is available
- the country conditions under which the value exists
- any DLC, ideology, tag, route, technology, law, event, or stage gate
- how the current value or stage is read
- how an abundance request is applied
- the shape of the value, such as accumulator, bounded gauge, stockpile, capacity, stage, state-distributed value, or owner-custom value
- whether high values are beneficial, harmful, mixed, contextual, or unknown
- its rarity and strangeness classifications
- a deduplication family and any hard storage conflicts
- its base generation weight
- AI evaluation facts that do not expose secret outcomes
- a result receipt and a persistence check when achievements or audits need one

The provider may generate several candidates when it owns a dynamic family.
An equipment provider can publish concrete equipment types that are valid for the country.
An ideology provider can publish relevant popularity values.
A state-resource provider can publish resource categories while choosing the state internally.
A country-specific system can publish several independent currencies or pressures.

## Provider callbacks

The contract has six conceptual operations.
Exact script structure belongs to implementation, but every provider must satisfy the same behavior.

### Registration

The owner publishes its stable provider identity and metadata.
Registration is idempotent.
A provider can remain registered while returning no candidates for countries that do not use its mechanic.

### Enumeration

The owner inspects the current country and publishes zero or more valid candidate records.
Enumeration must be read-only.
It must not activate an event, create a crisis, spend a resource, or count the owning event as fired.

### Presentation

The owner supplies spoiler-safe display text, current-state text, broad direction, and any reliable risk label.
A provider whose only possible label would expose a secret mechanic stays unavailable until that mechanic is publicly revealed.

### Application

The owner receives a stored candidate identity, the Event 66 sequence, the strength profile, and any stored target data.
It performs the abundance operation through the same lifecycle rules used by its own mechanic.

### AI evaluation

The owner reports immediate utility, waste risk, danger, urgency, strategic fit, and uncertainty in a normalized form.
This information is used after the four cards exist.
It never changes which values were generated for that AI country.

### Receipt

The owner returns success, partial success, rejection reason, applied magnitude or stage, harm class, persistence state, and any owner transaction identity.
The receipt prevents double application and supports debugging, achievements, and completion audits.

## Required provider families

The following matrix defines coverage obligations without turning the entries into a closed pool.

| Family | Expected examples | Eligibility rule | Abundance direction |
| --- | --- | --- | --- |
| Political and administrative resources | Political Power, government currencies, parliamentary support | The country owns and can change the value | Increase the named quantity |
| Military command resources | Command Power, Army Experience, Navy Experience, Air Experience | The mechanic and command system are active | Fill or grant through practical upper range |
| Social and political gauges | Stability, War Support, ideology support, legitimacy | The gauge exists and is publicly meaningful | Move toward the high end of the named gauge |
| Population and mobilization | manpower, reserves, mobilization pools, country-owned population currencies | The owner can change it without corrupting population accounting | Apply owner-defined enormous reserve or saturation |
| Fuel and stored materiel | fuel, convoys, trains, equipment, special stockpiles | A concrete stock exists and the token is valid | Fill capacity or grant a country-scaled surplus |
| Industry and construction capacity | factory-linked resources, building capacity, country-specific industrial funds | The country owns the mechanic and a safe grant exists | Expand through provider-defined saturation |
| Trade and market values | international-market CIC or other market balances | Required DLC and market access exist | Increase the market value through its owner API |
| Intelligence values | agency currencies, network capacity, operation resources | Required DLC and agency state exist | Increase the named capacity or stock |
| Autonomy and occupation values | autonomy progress, compliance, resistance, occupation-linked pressures | A valid subject or occupied-state relationship exists | Increase the named value, even when harmful |
| Country-specific mechanics | congress support, balance-of-power values, unique national currencies | The exact mechanic belongs to the country now | Apply through the country mechanic owner |
| Chaos Redux event mechanics | event currencies, pressures, capacities, project values | The owner event or system has exposed the mechanic | Increase through the owner lifecycle |
| Active crisis values | panic, famine pressure, contamination contribution, condemnation, other crisis values | The crisis exists or the owner explicitly permits activation | Increase the publicly named quantity |
| State-distributed values | resource deposits, local support, regional pressure, state capacity | The provider can resolve valid owned or controlled states | Distribute excess through an owner-defined target rule |
| Shared global systems | world ledgers with country-attributable contributions | The owner exposes a country-scoped contribution operation | Increase the country's contribution, not a raw global total |

This matrix must be expanded during implementation when repository inspection finds additional player-meaningful families.
A provider coverage report must explain every excluded family.

## Semantic eligibility

A candidate is applicable only when excess has a coherent meaning.
The following are valid reasons to exclude a raw value:

- it is a temporary calculation or proof field
- it is an index, sequence, checksum, date, or debug value
- it cannot be displayed without revealing hidden content
- it cannot be changed safely through an owner operation
- it is global with no country-attributable contribution
- it is binary and has no count, intensity, capacity, or stage interpretation
- it is already retired or no longer part of gameplay
- it belongs to a mechanic the country does not currently possess
- it depends on a DLC or feature that is not active

Desirability is not a valid exclusion reason.
Being dangerous, self-defeating, contradictory, or strategically foolish does not make a value inapplicable.

## DLC and country-specific mechanics

A DLC provider is dormant when the DLC is absent.
It is also dormant for a country that does not have the relevant mechanic, even when the DLC is installed.
A country-specific provider checks the current mechanic state instead of relying only on the country tag.

A value unlocked by a focus, decision, event, law, balance of power, agency, market, special project, or crisis joins the pool only when the owning system says it exists.
A value removed by route change, crisis resolution, annexation, subject change, or mechanic cleanup stops enumerating immediately.

## Event-owned mechanics

An Event 66 roll does not mark another event as fired.
It does not activate another event merely because that event owns a potential value.
The default rule is that an event-owned provider becomes valid only after its owner mechanic exists.

An owner may explicitly support abundance-driven activation.
That choice must be documented by the owner and must use the owner's normal initialization path.
It cannot be inferred by Event 66.

## Hidden and secret values

The registry may know that a provider exists without exposing it before reveal.
A hidden route, undiscovered project, secret evidence total, or unrevealed crisis cannot appear under its internal name.

The owner has three valid choices:

- keep the provider unavailable until reveal
- expose a public cover name that does not spoil the mechanic
- expose a broader parent value while keeping hidden components internal

A provider cannot print raw flags, variable names, project IDs, secret actor identities, or future evolution labels.

## State-scoped values

State-scoped candidates should represent a value family, not every state-value pair in the world.
The provider resolves an eligible state through its own logic and stores the target only when the card needs to name it.
This prevents large countries from flooding the pool with hundreds of copies of one family.

If the target can change before the player responds, the provider should prefer a stable semantic target rule.
For example, it can promise abundant domestic steel and choose a valid state at application time.
A card should name a specific state only when the owner can preserve or safely revalidate that target.

## Shared global systems

A truly global gauge cannot be written separately by every country as if it were a national resource.
It enters the pool only through an owner-defined country contribution, source, request, or responsibility ledger.

For example, a country may receive abundant contamination contribution, abundant public condemnation attached to its actions, or abundant treaty support if the owner system defines those as country-attributable values.
Event 66 must not set the global total directly or bypass source accounting.

## Registration lifecycle

Providers register through their owning package during normal system setup.
Registration is bounded and idempotent.
Activation and cleanup change provider availability, not the stable identity of the provider.

A provider schema change must preserve saved candidate identities or provide a migration path.
A provider removed from the mod must fail closed when an old save still holds a pending Event 66 card.

## Coverage standard

The event is incomplete until a repository-wide value inventory has been compared with the provider registry.
The audit must cover base game values, active DLC systems, country-specific systems, Chaos Redux mechanics, event-owned pressures and currencies, special stockpiles, retired systems, and hidden implementation state.

Every inventory row needs one disposition:

- registered directly
- covered by a dynamic family provider
- unavailable until a named reveal condition
- excluded with a semantic or engine reason
- blocked because no safe owner operation exists

A small handpicked registry with broad claims does not satisfy this specification.
