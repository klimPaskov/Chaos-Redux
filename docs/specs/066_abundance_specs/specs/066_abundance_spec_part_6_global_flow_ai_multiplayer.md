# Global Flow, AI, Multiplayer, and Performance

## One world wave

Event 66 is selected once by the normal event system.
That selection creates one global wave identity and one pacing transaction.
The wave then visits every currently valid country through a bounded one-time world pass.

The event must not create a daily, weekly, or monthly whole-world scan.
Provider registration and owner-system updates can use their normal bounded hooks.
The expensive country-local pool build happens only when an Abundance wave is being prepared.

## Wave lifecycle

### Wave creation

The root event records:

- Event 66 identity
- unique wave sequence
- date
- direct or cluster source
- cluster slot count and highest severity when relevant
- current enabled evolution state
- current Chaos tier
- one-time first-manifestation state

The wave state is fixed before any country cards are generated.
A country cannot receive a different evolution or cluster profile because another player delayed a popup.

### Participant snapshot

The root builds a one-time list of countries that pass the Event 66 participant gate.
Countries created after this snapshot wait for a later firing.
Countries annexed during processing fail closed at their own step.

The same country appears once.
Subjects, majors, minors, player countries, AI countries, ordinary countries, and supported special countries use the same participant standard.

### Country pool build

Each participant queries the registered providers in its own scope.
The country constructs four stored card signatures or records a pool-build failure.
No other country can contribute candidates to that pool.

### Resolution routing

A player-controlled country receives a visible event with its four stored cards.
An AI-controlled country uses a hidden resolver over the same four stored cards.

Player and AI routes call the same card application effect.
The AI route cannot bypass revalidation, owner callbacks, receipts, or partial-failure handling.

### Wave completion

The global history row is recorded once when the wave is launched.
Country receipts can finish later without creating new global Event 66 history rows.
The wave keeps bounded aggregate counters for generated cards, applied items, rejected items, and pool failures.

A global finalization step must not wait forever for a human popup.
Aggregate totals can be updated as countries resolve and exposed only through technical diagnostics.

## Pending choices

A human country with an unresolved Event 66 popup is temporarily invalid for a later Abundance wave.
This prevents a new wave from overwriting its stored card records.
The pending state survives save and load.
It clears when the country chooses, ceases to exist, or a bounded owner cleanup proves the event can no longer resolve.

A skipped pending country is recorded in the later wave diagnostics.
The system must not auto-select an old card merely to clear the state.

## AI choice model

AI generation is random under the same rules as player generation.
AI utility begins only after its four cards are stored.

The AI assigns each card a score from owner-supplied facts and general country context.
It then chooses probabilistically among the four cards.
The highest score should usually win, but uncertainty and random variance should preserve occasional strange decisions.

### Core AI factors

| Factor | Intended effect |
| --- | --- |
| Current shortage or headroom | Increases interest in values the country can use immediately |
| War state | Raises military, manpower, fuel, command, and relevant crisis priorities |
| Strategic plan | Raises values connected to the AI's current production, diplomacy, or route plan |
| Overflow waste | Lowers values that cannot create further effect for this country |
| Harm classification | Applies a risk penalty without removing the card |
| Desperation | Reduces risk aversion when defeat, collapse, or crisis is close |
| Route identity | Allows special governments or Chaos actors to prefer dangerous values |
| Persistence | Raises a value whose abundance will remain useful long enough to matter |
| Uncertainty | Keeps unknown or contextual values near neutral instead of forcing zero |
| Bundle interaction | Sums atomic value judgments and applies only broad conflict or synergy facts supplied by owners |
| Chaos tier | Adds modest tolerance for strange and risky options at higher tiers |
| Random noise | Prevents one static score ordering from deciding every similar case |

AI does not know hidden future event branches.
It evaluates public and owner-approved consequences only.

## Harm and AI

AI countries are allowed to select harmful abundance.
They should not do so at the same rate in every situation.

A stable ordinary AI usually avoids a clearly harmful card when a strong safe choice exists.
A desperate AI can accept a harmful bundle when its other items offer immediate survival value.
A country route built around corruption, panic, extremism, contamination, or another unusual value can receive owner-specific preferences.
A special Chaos country can interpret values through its own goals.

When all four cards are harmful, the AI still chooses one.
It compares severity, current exposure, reversibility, and strategic damage instead of falling back to a generic reward.

## Pair and triple evaluation

A bundle score begins with the sum of its atomic evaluations.
The AI then applies bounded adjustments for:

- hard owner conflicts that were not visible until revalidation
- overlapping caps or shared storage
- immediate strategic synergy
- combined danger
- partial invalidation risk
- persistence mismatch

The generator never uses these adjustments.
They exist only for the final AI choice.

A card with one excellent value and one harmful value can beat a safe single when the country is desperate.
A triple with three mediocre saturated values can lose to one focused single.

## AI refusal and invalidation

The AI cannot refuse all four cards.
The event premise requires one choice.
If a card becomes completely invalid before AI resolution, it receives no valid score and is removed from the AI option set.
If all four become invalid, the country records a resolution failure and clears the wave safely.

AI must not select by option index, display order, raw provider ID, or hidden implementation weight.

## Multiplayer authority

The authoritative game state creates every wave, country pool, card signature, and option order once.
Clients display stored results.
No client performs an independent random roll for the same country.

Each player country receives its own four cards.
Players do not share one global choice.
A choice made by one country does not alter another country's stored cards.

The event root, repeatable weight reduction, cluster state, first-manifestation Chaos, and global history row execute once under authority.
Country application receipts execute once for each country.

## Tag switching and control changes

Country control can change after generation.
The stored cards remain attached to the country.
The country cannot generate a second set because a human takes control.

The implementation should resolve control at dispatch time where possible.
A country that already entered the AI resolver keeps that AI choice transaction.
A country with a visible pending popup keeps it even if control later changes, until the event engine or cleanup resolves the popup safely.

Achievement tracking belongs to the same continuous player country and cannot be combined through tag switching.

## Save and load

The following must survive save and load:

- wave identity for every pending country
- four card signatures
- option order
- candidate target data
- pending-choice state
- selected-card receipt state
- recent candidate and family memory
- evolution activation state
- first-manifestation Chaos guard
- achievement ledgers

Loading a save cannot regenerate display text from a new random candidate.
The provider may rebuild the same text from the stored identity and current public state.

## Performance design

The provider registry can grow large, so the event should avoid permanent full-pool storage.
Candidate pools are temporary during card generation.
Only the four final cards, needed presentation data, and bounded novelty memory remain on the country.

Dynamic family providers should avoid publishing one candidate for every state when a value family plus an internal target selector expresses the same choice.
They should also avoid publishing invalid equipment tokens, hidden branches, or repeated aliases.

Provider enumeration must be bounded and side-effect free.
A provider that needs a broad internal scan should maintain its own active set through the owner system instead of asking Event 66 to discover it from the whole world.

## Diagnostics

Each wave should expose technical counts for:

- participant countries
- countries skipped because of a pending choice
- countries skipped because four cards could not be built
- registered providers queried
- providers that returned candidates
- provider faults
- candidates considered
- cards generated by cardinality
- AI choices by cardinality
- selected atomic items
- complete and partial applications
- invalidated items
- duplicate and hard-conflict rerolls

These counts belong in debug or completion evidence.
They do not belong in the player-facing popup or Event Details premise text.

## Probability validation

Every weighted surface requires a read-only baseline audit, an owner-applied tuning pass, and a comparison audit over the same named scenarios.
The required scenarios are defined in `research/066_abundance_probability_scenario_matrix.md`.

The audit must distinguish exact results, bounded results, sampled results, score-only evidence, and unresolved behavior.
A probability claim based on an incomplete provider pool is not final evidence.
