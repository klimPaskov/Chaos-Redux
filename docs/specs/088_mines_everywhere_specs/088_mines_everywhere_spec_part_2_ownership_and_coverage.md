# Event 088: Mines everywhere
## Part 2. Ownership, saturation, and coverage

### The ownership model

A minefield contribution belongs to an individual existing country in an individual naval strategic region. Countries do not share a single Event 088 owner, and the player's country is not used as a proxy for the rest of the world. Countries in a faction retain their own ownership. Opponents can receive separate fields in the same region during the same firing.

For design purposes, let C be the countries eligible to own mines at the moment of the incident, and R be the valid naval strategic regions of the active campaign. Every pair in C × R receives one addition. Country eligibility chooses owners. Region validity chooses geography. The two decisions must remain separate.

The set of recipients is determined before the first contribution is applied. A country receiving its minefield does not acquire authority to change the eligibility of later countries. A region receiving mines does not become the source of a new region selection. The total intended coverage is all pairs from the same firing-time world snapshot.

### Who receives a contribution

The default is every existing country for which the active engine can validly maintain an owned minefield. A country is not excluded because it is weak, neutral, a subject, an AI, a minor, outside naval range, or without a large fleet. Requirements for a normal ship minelaying mission are not automatically requirements for an event effect that directly creates owned mines.

The user permits landlocked countries and invalid mine owners to be excluded. This specification uses the narrowest native-legality rule rather than assuming a coastline is required. A landlocked country that the engine demonstrably supports as a mine owner may participate. A country that cannot validly own a field is excluded under the same rule regardless of who controls it. The implementation must document the verified rule and its exceptions rather than silently treating a naval-base count or a technology as a substitute for ownership validity.

Nonexistent tags and bookkeeping countries are not recipients merely because their definitions are present in the installation. Conversely, a current dynamic country must not be excluded merely because its tag was absent from the original start date. A country in exile or a country that has capitulated requires the same native ownership check, not a blanket historical assumption.

### What 1,000 means

For an ordinary country-region field with a nonnegative existing amount at or below its native cap, the design is:

`new amount = min(native cap, existing amount + 1,000)`

This is an addition constrained by a cap, not a replacement operation. Under the intended ordinary cap of 1,000, an empty field reaches 1,000, a field at 250 reaches 1,000, and a field already at 1,000 remains there. The unused portion of an addition is not redistributed to another owner or region.

| Existing amount for one owner | Active cap | Requested addition | Result under the design |
| --- | --- | --- | --- |
| 0 | 1,000 | 1,000 | 1,000 |
| 250 | 1,000 | 1,000 | 1,000 |
| 995 | 1,000 | 1,000 | 1,000 |
| 1,000 | 1,000 | 1,000 | 1,000 |
| 250 | 750 | 1,000 | 750 |
| 250 | 2,000 | 1,000 | 1,250 |
| 1,500 | 2,000 | 1,000 | 2,000 |

The last three rows define compatibility behavior, not a proposed change to the ordinary cap. A lower cap limits what can be placed. A higher cap does not change the requested addition into a fill-to-cap command. The implementation must not modify a global naval define to force all installations to the intended ordinary value.

A preexisting field above its current cap is an exceptional state. Event 088 must not reduce it to make the arithmetic look normal. A native operation that would clamp such a field downward cannot be used blindly. The release must either demonstrate an additive path that preserves it or identify that configuration as unsupported before altering minefields. Clearing the field and reconstructing a guessed amount is not preservation.

### Several owners in one region

Suppose two opposing countries both have empty fields in a valid sea. Each receives the full requested addition. At the intended cap, each can then own 1,000 mines there. The event has not divided a single 1,000-mine budget between them.

Suppose one country already has 900 mines and another has 100. Each receives a separate addition, subject to its own limit. One country's existing field cannot consume the other country's allowance. A third country's contribution cannot overwrite either field.

These examples concern stored ownership and placement. They do not promise that combat modifiers, ship-hit probability, naval superiority, or movement penalties multiply linearly with the number of owners. Those effects remain native and require version-specific verification. The interface must distinguish a mine count from the combat consequence inferred from it.

### Which regions are included

R contains every region that the effective campaign map and engine identify as a valid naval strategic region for mine placement. This includes coastal approaches, remote oceans, valid enclosed seas, major routes, and valid regions added or redefined by compatible map content.

Geography is never sampled. Region identifiers may be sparse, renamed, reordered, or changed. An arbitrary numerical ceiling, a fixed historical list, repeated random selection, the countries' naval range, and the set of regions beside owned states are all inadequate definitions of complete coverage.

Validity is determined from the active map, including its effective overrides. A land-only strategic region is not mined. A lake or otherwise unusual region is included only if the active engine treats it as a valid naval mine region. A region with identifier zero is not automatically invalid. The implementation needs a real validity rule rather than a convention inferred from typical IDs.

Geographical coverage and naval accessibility are different. A valid sea that a particular country cannot reach still receives that country's contribution if direct ownership there is legal. The event does not need to sail a minelayer to each location. It also does not grant fleet access to make an inaccessible sea reachable.

### The current-map compatibility promise

A compatible map configuration must yield a complete, current region set. A generated registry may be used only when it demonstrably represents the effective map actually loaded by that campaign. A registry built from one map cannot support a claim about all later load orders.

When complete coverage cannot be established, the implementation is not allowed to quietly run a reduced version. Normal dispatch must reject that configuration before the incident is consumed or reported as successful. The missing capability remains a release blocker for that compatibility claim. This preserves the global design instead of disguising a historical-region implementation as dynamic support.

### Clearance and subsequent ownership

Clearance is assessed from the point of view of a country using a route. Removing one hostile owner's field does not necessarily remove another hostile owner's field. A route is clear of relevant hostile mines only when all currently relevant hostile contributions have been dealt with according to the native rules.

This does not require friendly or neutral mines to be erased. Nor does it guarantee permanent safety if diplomacy changes or someone later lays additional mines. It does guarantee that Event 088 itself does not replace mines removed through normal play.

Minefields remain engine-owned after the incident. Annexation, liberation, civil war, faction changes, capitulation, peace, and country disappearance follow verified native handling. Event 088 does not grant replacement fields to successor countries or reassign ownership to a fictional neutral mine administrator. Any behavior that the active engine does not preserve must be documented as a compatibility fact rather than compensated for with an unapproved extra mechanic.
