# Choice Generation

## Country-local generation

Every participating country builds its pool from its own current mechanics.
The global firing supplies the sequence identity, current evolution state, and cluster strength profile.
It does not supply a universal list of four values.

The generator asks every registered provider to enumerate candidates for the current country.
Invalid providers return nothing.
Valid candidates enter a temporary country-local pool with display data, weight data, owner identity, deduplication data, harm classification, and application identity.

Generation ends with four stored card records.
The card records remain fixed until the country resolves them.

## Candidate record

A generated candidate record needs enough information to survive display and application without querying a different value later.
It includes:

- provider identity and schema version
- stable candidate sub-identity when the provider is a family
- owner system
- short and full display identities
- stored target identity when a target must stay fixed
- current value or stage snapshot for the tooltip
- abundance shape and strength profile
- harm, rarity, strangeness, and source classifications
- deduplication family and hard conflict tags
- generation weight after allowed randomization factors
- a stable signature used to detect duplicates

The record does not store the final effect as free text.
Application always returns to the owner provider.

## Four card construction

The event always attempts to create four distinct card signatures.
At baseline each card contains one candidate.
Evolution II permits two-candidate cards.
Evolution III permits three-candidate cards.

The number of cards never increases.
Higher evolutions increase how many values can live inside one option.
This keeps the popup readable and preserves the four-choice identity.

## Independent randomness

Each atomic value is drawn from the country's full valid pool under the current weighting rules.
Pair and triple cards are assembled from separate draws.
There are no authored pairs, favored synergies, thematic bundles, ideology packages, or country packages.

The generator may reject a duplicate or hard storage conflict and draw again.
That safety step does not authorize a thematic filter.
Contradictory, unrelated, strange, or strategically awkward values remain valid together.

## Uniqueness hierarchy

The generator follows this order:

1. No card may contain the same candidate twice.
2. No two cards may have the same complete signature.
3. Exact candidates should not repeat across cards while enough alternatives exist.
4. Deduplication families should be spread across cards while enough alternatives exist.
5. When the pool is too small, exact candidates may repeat across different cards, but every card must still differ by at least one candidate.
6. Hard storage conflicts remain forbidden even in a small pool.

A pair containing fuel and manpower is distinct from a pair containing fuel and Stability.
A reversed ordering of the same two values is not a new card.

## Weight construction

Generation weight may use only factors connected to variety, ownership, rarity, current applicability, evolution, and cluster profile.
It must not use the value's strategic usefulness to the country.

Allowed factors include:

- provider base weight
- rarity classification
- strangeness classification
- active crisis or active event relevance
- DLC or country-specific status when an evolution boosts unusual mechanics
- recent appearance dampening
- recent selection dampening
- current evolution weighting
- current cluster strength profile
- provider health and successful enumeration

Forbidden generation factors include:

- whether the country needs the value
- whether the value would win a war
- whether the value is harmful
- whether the AI would choose it
- whether the player is likely to prefer it

Evolution I and Evolution III may explicitly increase harmful weighting because the user defined that escalation.
Outside those evolution rules, harm does not control generation.

## Novelty memory

The event keeps light memory of values recently shown and selected by each country.
Recent values remain eligible, but their weights can fall for a limited number of Event 66 firings.
This memory improves variety without creating a consumable deck.

Novelty memory applies at the candidate level and may also apply at the deduplication-family level.
It should decay by Event 66 appearances or a bounded time period.
It must not require a periodic whole-world scan.

## Cardinality selection

The generator decides the size of each card before drawing its atomic values.
Cardinality is controlled by enabled evolutions and the current cluster profile.

At baseline and during Evolution I, every card is a single.
At Evolution II, singles remain possible and pairs enter the distribution.
At Evolution III, triples become common, pairs remain common, and singles become uncommon but do not disappear.

The exact tuning must be verified through the probability workflow.
The intended ordering is fixed:

- Low cluster profile has the lowest multi-value frequency.
- Standard direct firing sits above Low.
- Medium cluster profile is close to or slightly above Standard.
- High cluster profile has the highest multi-value frequency permitted by the current evolution.
- Evolution III produces more triples than Evolution II can produce pairs under comparable profiles.

No profile may create a pair before Evolution II is enabled.
No profile may create a triple before Evolution III is enabled.

## Small pools

Ordinary countries should receive enough generic provider coverage to build four distinct cards.
Special actors can have narrower pools.

When a country cannot build four distinct signatures, the generator tries these steps in order:

1. Relax deduplication-family diversity while preserving exact candidate diversity.
2. Permit exact candidates to appear on different cards while keeping every complete card distinct.
3. Use different pair or triple combinations when evolutions permit them.
4. Ask family providers for alternate valid sub-candidates.
5. Exclude the country from the current wave if four valid signatures still cannot be built.

The event must not insert invalid values, dummy choices, generic fallback rewards, or hidden no-op tokens merely to reach four cards.
A country excluded for pool failure is recorded in the wave diagnostics.

## Saturated values

A value already at its normal maximum can remain a candidate when the provider defines a meaningful overflow, retention, duration, breadth, or saturation consequence.
If the provider can only perform a guaranteed no-op, it should normally return no candidate for that country.

A rare intentional useless candidate is allowed only when the owner marks that behavior as part of the value's design and the tooltip can describe it honestly.
This exception cannot become a substitute for missing abundance logic.

## Option order

After four cards are built, their positions are randomized.
The first option must not be more beneficial, more common, or more likely to be selected by AI merely because it is first.
AI evaluates card identities, not option index.

## Stored rolls

All four card records are stored before the popup or AI resolver reads them.
The following actions must not reroll them:

- opening or closing another window
- hovering an option
- changing a tooltip
- saving and loading
- pausing or unpausing
- country state changes after generation
- event-log rebuilds

A new roll occurs only through a new Event 66 wave or an explicit bounded recovery from a generation failure before the choices are shown.

## Revalidation at choice time

A selected card is revalidated before application because wars, annexations, routes, crises, and mechanic ownership can change while a human popup is open.
Revalidation checks the same semantic candidate.
It does not replace the card with a new random value.

For a pair or triple, each atomic candidate is revalidated separately.
Valid items apply.
Invalid items return a rejection receipt.
The result can therefore be partial when the country state changed after generation.

A partial application does not silently reroll the failed item.
The post-choice report and diagnostics state how many selected values applied.
Achievements that require a complete pair or triple do not count partial results.

## Provider failure

One broken provider must not break the whole global wave.
Enumeration errors, missing display data, invalid weights, missing owner callbacks, and malformed candidate records remove that provider's candidates from the current country pool and create a bounded diagnostic entry.

Repeated provider faults should disable that provider for the rest of the current wave.
They should not permanently unregister it without an owner migration or repair.

## Statistical acceptance

The implementation must prove that candidate generation is not dominated by a small group of generic values when broad providers are active.
It must also prove that unusual values do not crowd out ordinary values before Evolution I.

The probability audit should measure:

- card cardinality by evolution and cluster profile
- candidate-family frequency
- rare and harmful frequency
- repeat frequency across successive waves
- first-option bias
- small-pool behavior
- large-pool behavior
- provider dominance
- starvation of low-weight families
- duplicate and conflict rejection rates

Exact expected shares are not declared until the complete provider pool is known.
The required ordering and diversity conditions are defined in the probability scenario matrix.
