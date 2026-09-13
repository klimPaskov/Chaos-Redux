# Evolutions and Sudden Abundance Cluster

## Evolution model

Event 66 has no long-lived crisis phase between firings.
Its evolutions change the generator used by later Abundance waves.
When a wave begins, the event checks enabled evolution stages and current Chaos before it builds any country pool.

If the event has never fired and the world already meets one or more thresholds, the first wave can open at the highest enabled eligible stage.
The newly reached stages are recorded in order before card generation.

If Event 66 has fired before, a later wave records any newly eligible enabled stages before using them.
There is no separate evolution popup whose only purpose is to announce a weighting change.
The next normal Event 66 firing is the paced entry point.

Evolution state adds no Chaos.

## Evolution I: Strange Abundance

- Chaos requirement: `200+`

The complete dynamic pool remains available.
No separate strange-value list is created.

Generation weighting shifts toward candidates with one or more of these traits:

- unusual or rare
- country-specific
- DLC-specific
- Chaos Redux owned
- tied to an active event or crisis
- harmful, mixed, or contextually dangerous
- normally absent from ordinary countries

Ordinary values remain eligible and visible.
The evolution should make strange outcomes noticeably more common without making Political Power, experience, manpower, fuel, Stability, War Support, or other common values disappear.

The weighting boost is provider metadata plus current country state.
It is not a hardcoded list inside the evolution.

### Disabled-state behavior

When Evolution I is disabled, generation uses baseline rarity and harm weighting even at high Chaos.
Later bundle evolutions can still function.

## Evolution II: Abundance Comes in Pairs

- Chaos requirement: `400+`

A card can contain two independently drawn values.
Singles remain in the distribution.
Both values come from the country's full valid pool.
They do not need to share an owner, theme, benefit, target, or mechanic.

A pair cannot contain the same candidate twice.
Hard storage conflicts are rerolled.
The generator does not search for synergy and does not avoid contradiction.

The player chooses the pair as one option.
Both atomic values are then revalidated and applied independently.

### Intended frequency

Pairs should be common enough to define the evolution, but a single-value option should still appear in many waves.
Low cluster profile favors singles.
High cluster profile favors pairs.
The exact distribution is tuned only after the full provider pool passes probability inspection.

### Disabled-state behavior

When Evolution II is disabled, pair cards are not generated.
Evolution III can still apply its strange weighting increase, but its multi-value cardinality effect is suppressed unless Evolution II is also enabled.
This prevents a disabled pair stage from being bypassed by triple construction.

## Evolution III: Everything in Excess

- Chaos requirement: `600+`

Cards containing three independently drawn values become common.
Pairs remain available.
Singles become uncommon but remain possible.

Rare, unusual, powerful, harmful, owner-specific, active-crisis, and mechanic-specific candidates receive a further weighting increase.
This remains a weighting change over the same live pool.
It does not create a final-tier catalog of preferred values.

A triple must contain three distinct candidates.
Its three transactions apply independently.
An achievement or complete-result report counts the triple only when all three succeed.

### Intended frequency

At a Standard or Medium profile, triples should become the largest single cardinality group.
At a High profile, triples should dominate while leaving some pairs and rare singles.
At a Low profile, pairs can remain at least as common as triples.

The probability audit must verify these orderings across small and large pools.

### Disabled-state behavior

When Evolution III is disabled, triples are unavailable and its extra strangeness weighting does not apply.
Evolution I and Evolution II continue independently when enabled.

## Evolution enablement and logs

Each evolution uses the shared Event Log evolution controls.
A disabled stage cannot set its recorded flag, change generation weights, raise cardinality, unlock achievement conditions, or appear as active in Event Details.

The event records stages in numerical order when one wave crosses several thresholds.
The evolution actor is global because the generator changes for the world, not for one recipient country.

Event Details should explain each evolution's visible change in plain terms.
It should not print weight multipliers, provider metadata, roll attempts, or exact probability formulas.

## Sudden Abundance cluster role

Event 66 occupies three ordered logical member slots in Sudden Abundance:

- Event 66 Abundance, Low
- Event 66 Abundance, Medium
- Event 66 Abundance, High

The entries use one event identity and one provider system.
They are not three cloned events.

The current cluster export does not yet contain Sudden Abundance.
Cluster ID `9` is the first visible unused numeric ID in the supplied export and is the provisional planning ID.
The authoritative workbook and runtime registry must be checked before it is locked.

Event 64 Border Fortifications is already planned elsewhere as a Medium Sudden Abundance member.
The final cluster membership pass must reconcile that accepted design and any other approved members.

## Cluster strength profiles

### Low slot

The chosen value reaches immediate abundance with the shortest provider-defined persistence and the narrowest state or stock distribution.
At Evolution II and III, the Low slot has the weakest pressure toward pair or triple cards.
It still produces a large visible result.

### Medium slot

The chosen value reaches abundance with normal provider persistence and distribution.
Its bundle frequency is close to the Standard direct profile.

### High slot

The chosen value uses the strongest safe provider persistence, distribution breadth, or stage pressure.
At enabled bundle evolutions, it has the strongest pressure toward pairs and triples.
It cannot unlock a pair or triple before the corresponding evolution.

### Standard direct firing

A normal Event 66 firing outside a cluster uses the Standard profile.
Its magnitude is close to Medium, while its weighting is not treated as a cluster member bonus.

## Duplicate-slot coalescing

A cluster firing can contain more than one Event 66 logical slot.
Those slots must never create several world sweeps or several popups for each country.

All Event 66 slot hits in one cluster transaction coalesce into one Abundance wave.
The coalesced wave uses:

- the highest selected severity as its main strength profile
- the number of selected Event 66 slots as a bounded persistence or bundle-pressure input
- one participant snapshot
- one set of four cards per country
- one Event 66 fired transaction
- one repeatable cap change
- one Event 66 history entry
- one contribution to cluster fired counts

Additional slot hits do not increase the number of options above four.
They do not apply several selected cards.
They do not bypass evolution thresholds.
They do not add extra direct Chaos.

## Cluster history and details

Cluster Details should display all three Event 66 rows with their own severity labels.
A cluster history entry should report one coalesced Abundance member result and retain the slot-hit count in technical details.
It should not list the same global wave as three successful country events.

If the provider system cannot build any valid country cards, the coalesced member is skipped with a clear cluster reason.
If some countries fail pool construction, the member still counts as fired and records participant and exclusion counts.

## Cluster balance expectations

The three logical slots give Sudden Abundance a broad severity footprint.
They must not make Event 66 dominate the cluster simply because one event ID appears three times.
The cluster probability audit should compare the effective chance of an Event 66 wave with every other member after optional participation, selection, and coalescing.

The slot design is accepted only when Low, Medium, and High roles are visible in cluster details, mechanically distinct after selection, and counted as one Event 66 wave when they overlap.
