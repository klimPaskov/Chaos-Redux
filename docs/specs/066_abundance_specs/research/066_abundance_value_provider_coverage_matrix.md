# Event 066 Value Provider Coverage Matrix

## Purpose

This matrix is an implementation audit scaffold.
It describes provider families that must be inspected and gives the expected ownership model.
It does not define a closed Event 66 pool.
Repository inspection can add more rows.

| Coverage family | Candidate scope | Common shape | Owner expectation | Key validity questions | Required audit result |
| --- | --- | --- | --- | --- | --- |
| Political Power and shared political currencies | country | accumulator | core provider or country-mechanic owner | Can the value be read and granted safely, does it have a practical UI ceiling | direct provider or documented exclusion |
| Command Power | country | bounded accumulator | core military provider | Is command system valid for the country, what happens at cap | fill and overflow policy |
| Army Experience | country | bounded accumulator | core military provider | Current cap, DLC interactions, overflow behavior | direct provider |
| Navy Experience | country | bounded accumulator | core military provider | Navy relevance is not an eligibility filter, but engine access must exist | direct provider |
| Air Experience | country | bounded accumulator | core military provider | Air-force absence cannot create an invalid write | direct provider |
| Stability | country | bounded gauge | core society provider | Correct public direction and cap | direct provider |
| War Support | country | bounded gauge | core society provider | Correct public direction and cap | direct provider |
| Ideology popularity and party support | country and ideology token | bounded dynamic family | politics owner | Which ideologies are valid, how hidden ideologies are handled | family provider or reasoned exclusion |
| manpower and reserve pools | country | accumulator | core population or owner-specific manpower provider | Population consistency, engine-safe ceiling, nonhuman treatment | direct or routed provider |
| Fuel | country | bounded stock | core logistics provider | Capacity, current crisis state, persistence at cap | direct provider |
| Convoys | country | stockpile | equipment or logistics family | Concrete token and safe grant | family provider |
| Trains | country | stockpile | equipment or logistics family | DLC or mechanic availability, concrete token | family provider |
| Ordinary equipment | country and concrete equipment token | dynamic stockpile family | equipment registry provider | Researched or usable token, archetype validity, mutual exclusions | dynamic family provider |
| Chaos Redux special equipment | country and owner token | dynamic stockpile family | equipment owner provider | Owner unlock, public identity, CXT and consumer state | owner provider |
| Nuclear stock and missile-like stock | country | stockpile or charge pool | weapon owner | Technology, ownership, condemnation and source behavior | owner provider or blocked reason |
| Civilian, military, and naval industrial capacity | country or states | capacity or state-distributed | industry provider | Safe building placement, state caps, overlap with fixed events | provider with bounded distribution |
| Infrastructure, rail, supply, air, radar, fort, and other building capacity | states | state-distributed | building-family owner | Exact target rules, valid levels, map performance | family provider or exclusion by surface |
| Natural resources | owned states and resource token | state-distributed dynamic family | resource provider | Resource token, target state, DLC resources, map balance | family provider |
| International market balances | country | accumulator or capacity | market owner | DLC present, market access, country actually uses mechanic | DLC provider |
| Military Industrial Organization values | country and organization | stage, fund, or capacity | MIO owner | DLC present, MIO exists, public value semantics | DLC dynamic family or reasoned exclusion |
| Intelligence agency values | country | capacity or accumulator | intelligence owner | DLC present, agency exists, safe direct value | DLC provider |
| Operative and network resources | country, target, or network | capacity or stage | intelligence owner | Target validity, hidden information, safe display | provider or hidden exclusion |
| Autonomy progress | subject relationship | bounded gauge | autonomy owner | Country is subject, direction means more autonomy, relationship survives | relationship provider |
| Compliance | occupied state or aggregate | bounded state value | occupation owner | Valid controlled state, public target, application breadth | state family provider |
| Resistance | occupied state or aggregate | bounded harmful state value | occupation owner | Valid target, harmful direction, owner lifecycle | state family provider |
| Balance of power | country and balance identity | bounded gauge | country package owner | Active balance, correct side and public label | owner provider |
| Congress, parliament, faction, and council support | country and mechanic identity | bounded gauge or accumulator | country package owner | Active institution, public label, route state | owner provider |
| Country-specific economic currencies | country | accumulator | country package owner | Active route and stable semantic meaning | owner provider |
| Country-specific military readiness or command values | country | gauge or stage | country package owner | Public meaning, route validity, cap | owner provider |
| Event-owned project resources | country and project | accumulator or stage | event owner | Owner event active, no fired-state side effect, safe reveal | owner provider |
| Crisis pressure | country or states | harmful gauge | crisis owner | Active crisis or explicit activation permission, recovery path | owner provider |
| Famine values | country or state system | gauge, stock, or access | famine owner | Food Security, reserves, relief access, no population double count | owner adapter |
| Migration values | country or route system | gauge or capacity | migration owner | Displacement, reception, border policy semantics, no transfer duplication | owner adapter |
| Air Cleanliness contributions | country contribution to global ledger | source contribution | Air Cleanliness owner | Country attribution, source ledger, global total protection | owner adapter only |
| Condemnation values | country responsibility ledger | source contribution or gauge | condemnation owner | Public evidence, hidden evidence, source categories | owner adapter only |
| Death-linked burdens | country or state | owner-defined pressure | Deaths or event owner | Never create duplicate death records, public semantic value needed | owner adapter or exclusion |
| Camp and repression values | country or sites | stage, count, or pressure | repression owner | Public reveal, evidence, protected content, owner lifecycle | owner adapter or hidden exclusion |
| Special Chaos-country values | special country | owner-custom | country or event owner | Country actually uses value, ordinary civilian providers excluded where invalid | owner provider |
| Shared global threat or world-end readiness | global | global aggregate | owning terminal systems | Per-country abundance may be semantically invalid and dangerous to expose | normally excluded unless owner supplies contribution |
| Event sequence, proof, debug, and helper variables | internal | none | owning script | No player-facing semantic meaning | mandatory exclusion |
| Boolean flags, tags, names, and ordinary law identities | internal or categorical | none unless owner defines a quantity | owning system | Can abundance be given a real count, intensity, capacity, or stage | exclusion by default |

## Provider family audit questions

For every discovered value, the implementation audit should answer:

1. What does the value mean to a player?
2. Who owns its storage and lifecycle?
3. Does the current country actually possess the mechanic?
4. Can the value be named without spoilers?
5. Is high the correct semantic abundance direction?
6. Can the owner apply a strong result safely?
7. Does the result need a target, cap, persistence state, or transition sequence?
8. Does another shared system already own deaths, contamination, condemnation, population, or Chaos accounting?
9. Can AI evaluate the value without hidden future knowledge?
10. Can the owner return an idempotent receipt?

## Coverage failure examples

The following do not satisfy dynamic coverage:

- registering ten familiar core values and calling the pool universal
- scanning for numeric variables and treating every match as a candidate
- exposing secret project progress under a raw key
- granting equipment through one generic token that ignores concrete types
- setting global contamination or condemnation directly
- excluding all harmful values to protect AI
- keeping country-specific providers in an Event 66 file instead of the owner package
- omitting a DLC family because the base game has a similar value
- allowing a provider to initialize or fire its owner event during enumeration
