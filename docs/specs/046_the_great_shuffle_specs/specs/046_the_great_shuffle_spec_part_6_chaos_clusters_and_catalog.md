# Event 046: Chaos, clusters, and catalog alignment

## Chaos principle

A successful Great Shuffle is a direct source of Chaos because it permanently rewrites the world's current condition.

The gain represents the rupture itself.

It does not depend on whether one country received a useful result.

A world full of unexpected abundance is still a world whose institutions, armies, and material facts changed without cause.

Evolution activation gives zero Chaos.

Eligibility, pacing, registry setup, selection, and report creation give zero Chaos.

Only committed gameplay change scores.

## One gain per transaction

One successful global transaction creates one Event 46 Chaos history entry.

The event does not add Chaos once per country, state, unit, family, or owner adapter.

The committed families contribute to one disruption score.

That score is compressed into one capability band.

A save and load recovery cannot record the gain twice.

A cluster firing cannot record a second Event 46 gain for the same transaction.

A transaction that commits no family adds zero Chaos.

## Capability bands

The target direct-gain bands are:

| Highest committed domain | Target Chaos gain | Meaning |
| --- | ---: | --- |
| Baseline basic national values | `+1` to `+2` | Governments wake to new political and military reserves |
| Evolution I national stores | `+2` to `+3` | Material balance across the world is visibly overturned |
| Evolution II population, industry, buildings, or resources | `+3` to `+5` | The physical and human map no longer matches remembered reality |
| Evolution III politics, research, production, units, or commanders | `+4` to `+6` | Countries and armed forces function through unfamiliar institutions |
| Evolution IV owner-registered mechanics | `+5` to `+8` | Active crises and power systems lose their established state |
| Evolution V proven structural families | `+6` to `+10` | The playable structure of the world is broadly rewritten |

The bands sit on the shared Chaos scale, where a major war declaration is worth `5` and the first nuclear use `10`.
A repeatable event that rewrites the world each time must not outpace those milestones per firing; the repeatable weight and cap already limit how often it returns.

The lower end applies when only a small legal subset commits.

The upper end requires high family coverage and severe families.

The exact mapping is centralized and validated through named probability and gameplay scenarios.

The implemented ordering must preserve that broader and deeper committed change cannot score less than a narrow lower-tier firing with comparable family coverage.

## Family severity contribution

Every family declares a disruption class for Chaos compression.

Basic stores and ordinary numeric values normally contribute low weight.

State population, industry bundles, law groups, production, unit groups, and important owner values normally contribute medium weight.

Structural relationship families contribute high weight.

An owner adapter cannot declare an extreme weight merely to farm Chaos.

The Event 46 owner audits and approves the class.

The weight affects only the one transaction gain.

It does not affect the random result or report priority.

## First manifestation

The first successful Great Shuffle can add a small one-time manifestation premium inside the normal capability cap.

The premium represents the world's first realization that familiar facts can change at once.

It is recorded in the same Event 46 history entry.

It is never applied again and does not alter later family selection.

## Evolution-enabled consequences

The added Chaos comes from the evolved behavior that actually committed.

Evolution II adds no Chaos until a state, building, or resource family changes the world.

Evolution III adds no Chaos until a politics, research, production, unit, or commander family commits.

Evolution IV adds no Chaos merely because an adapter registered.

Evolution V adds no Chaos merely because the threshold was reached.

This preserves the project rule that evolution state itself is not a Chaos source.

## No direct Event 46 reversal

Event 46 has no containment path and no event-owned negative Chaos result.

The rewrite is permanent.

A favorable result does not restore confidence in reality.

Countries can later reduce Chaos through ordinary peace, liberation, democratic change, air recovery, and other shared sources.

Those later actions remain normal consequences of play.

## Generic source overlap

The transaction suppresses generic sources that would count only because Event 46 used a setter.

A shuffled ruling ideology does not also add the ordinary ideology-change Chaos.

A shuffled population does not create Deaths Chaos.

A structural ownership adapter does not also count the same change as ordinary annexation or liberation unless the adapter explicitly hands the result to that shared source instead of Event 46.

The implementation must choose one source owner for every side effect.

The same consequence cannot appear in both Event 46's direct score and a generic source ledger.

Normal consequences after the transaction are not suppressed.

A war begun later, deaths suffered later, or peace signed later uses the ordinary shared source.

## Randomizations cluster

**Randomizations** is a new event cluster for incidents whose central mechanic deliberately randomizes existing gameplay state.

The cluster is Minor Repeatable, begins at Chaos level 1, and uses the normal cluster pacing contract.

Event 46 is a Medium-severity core member.

The cluster description should focus on permanent, unpredictable reordering of existing conditions.

It should not describe random target selection alone.

An event belongs here when randomization of current state is its playable identity.

An ordinary disaster that happens to choose a random target does not qualify.

### One-member behavior

The cluster must not apply Event 46 twice when Event 46 is its only valid member.

Automatic cluster expansion should require at least two distinct valid member entries or use another non-duplicating rule supported by the shared framework.

Manual cluster forcing can record the cluster with Event 46 as its single fired member, but the member transaction still runs once.

Future Randomizations members can make the ordinary wider-cluster roll meaningful without changing Event 46.

### Registry identity

Randomizations is registered as cluster 14 in the workbook and the live registry, with Event 46 as its Medium member.
Implementation enables that existing row and adds no second membership.

## Other cluster relationships

Event 46 owns only its Randomizations membership.
Domestic Unrest (cluster 16), multi-cluster membership (for example Event 42 in clusters 11, 15, and 18), Event 2 in Diseases, and Event 43's cluster belong to the cluster registry and those events' own packages, and they are already represented in the workbook.
This package makes no requirement on them.

## Event 46 workbook target

The authoritative workbook row for ID `46` must replace **Seismic Archive** with **The Great Shuffle**.

The row must contain:

- Minor Repeatable type
- Chaos level `1`
- Randomizations membership
- Medium member severity for that relationship
- the five actual evolution capabilities
- a player-facing premise aligned with Event Details
- status appropriate to implementation evidence

The status remains **To Be Reworked** while this package is only a specification.

After implementation, the normal status target is **Needs Testing** unless the user explicitly approves another status.

The catalog worker must never assign **Playable** by inference.

## Catalog wording direction

The Event 46 details field should explain that the whole valid world receives new permanent values and that each later firing starts from scratch.

It should mention adaptation and the possibility of severe gains or losses.

It should not list script variables, family ratios, protected arrays, formulas, or raw effect values.

Each evolution field should describe the new domain that becomes vulnerable.

The text should not imply that an evolution is an ordinary escalation stage already active between firings.

The Randomizations cluster field should describe deliberate reordering of existing state.

The final player-facing wording is written during implementation and matched across Event Details, Event Log, localisation, and the workbook.

## Workbook and export rule

Only `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is edited.

After a successful workbook save, implementation runs `python .tools/export_event_catalog_csv.py` from the mod root.

The three CSV files are export-only snapshots.

They must not be edited directly.

The exported Events, Clusters, and Scenarios files must remain structurally valid.
