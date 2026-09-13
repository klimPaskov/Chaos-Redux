# Event 066 Abundance Design Decision Log

## 1. Dynamic coverage uses owner providers

### Decision

Event 66 consumes an extensible provider registry.
Core, DLC, country-specific, event, crisis, and Chaos Redux systems publish the semantic values they own.

### Reason

HOI4 script cannot be assumed to reflect safely over every raw variable, mechanic, database object, or DLC value.
Owner registration gives the event full extensibility while preserving lifecycle, display, AI, and accounting rules.

### Rejected alternative

A large central switch inside Event 66 would remain a hardcoded pool and would require direct edits whenever another mechanic is added.

## 2. Semantic values are different from raw variables

### Decision

Only player-meaningful quantities, stocks, capacities, pressures, stages, and balances can become candidates.

### Reason

Sequence IDs, proof fields, hidden flags, array indexes, debug counters, and temporary calculations have no coherent abundance meaning.
Showing them would leak implementation and risk corrupting state.

### Rejected alternative

Treating every numeric field as eligible would create false universality and unusable choices.

## 3. Owner callbacks perform every mutation

### Decision

Event 66 selects values and submits abundance requests.
The owning system applies the result and returns a receipt.

### Reason

Deaths, population, contamination, condemnation, famine, migration, occupation, stockpiles, balance-of-power systems, and event crises already have source accounting and cleanup contracts.

### Rejected alternative

Directly setting foreign variables would skip transitions, double count shared systems, and make later owner changes unsafe.

## 4. The player sees four standard event options

### Decision

Use one normal event popup with four dynamic option shells.

### Reason

The player makes one quick choice.
A separate mechanic window would add layout, resolution, click-region, and maintenance risk without improving the decision.

### Rejected alternative

A dedicated scripted GUI would turn a compact incident into a permanent interface and require a large event UI implementation for little gain.

## 5. The event has no persistent public meter

### Decision

All complex pool and transaction state remains hidden.
The player sees candidate names, current public state, broad result, target, risk, and persistence.

### Reason

The event does not ask the player to manage an ongoing Event 66 resource.
Provider systems already expose their own values where needed.

### Rejected alternative

A new Abundance meter would duplicate owner mechanics and exceed the information needed for one choice.

## 6. Harm affects weighting and AI, not baseline eligibility

### Decision

Harmful values remain in the pool.
Evolution I and Evolution III can increase their generation weight.
AI can penalize or prefer them after generation.

### Reason

The accepted concept explicitly allows abundance to be disastrous.
Filtering harmful values would remove the event's defining risk.

### Rejected alternative

A safe-only pool would collapse Event 66 into a broad reward event.

## 7. Pair and triple cards have no authored packages

### Decision

Each atomic value is drawn independently from the full current pool.
Only duplicates and hard storage conflicts are rerolled.

### Reason

The accepted concept requires unrelated combinations and complete randomness.

### Rejected alternative

Synergy bundles, ideology packages, country packages, and favored pairs would become a hidden predetermined catalog.

## 8. Stale bundle items can fail partially

### Decision

Each selected atomic item revalidates and applies separately.
Valid items remain applied when another item becomes invalid.

### Reason

A human can leave a popup open while the country changes.
Universal rollback is unsafe across unrelated owners.

### Rejected alternative

Rerolling failed items after selection would change the choice the player made.
Rolling back successful items would require every owner to support perfect reversal.

## 9. Pending human choices block later Event 66 generation for that country

### Decision

A country holding an unresolved Event 66 popup is skipped by a later wave.

### Reason

The four stored card slots must not be overwritten.
The event is repeatable and human popups can remain open indefinitely.

### Rejected alternative

Auto-selecting or discarding the old choice would remove player agency.

## 10. Cluster duplicate slots coalesce

### Decision

Low, Medium, and High Event 66 member hits in one Sudden Abundance firing produce one world wave.
The highest severity and bounded slot count shape that wave.

### Reason

Three waves would create twelve choices per country, repeated global scans, several cap changes, and history spam.

### Rejected alternative

Treating the three rows as cloned events would multiply pacing and break the cluster's single-transaction rule.

## 11. Direct Event 66 Chaos is one-time

### Decision

The first global manifestation adds `+5` Chaos once.
Later waves, evolution activation, bundle cardinality, and cluster coalescing add no automatic direct Chaos.

### Reason

The first worldwide anomaly is a concrete systemic shock.
Repeated effects already feed owner and shared Chaos sources when they cause deaths, contamination, war, ideology change, or other consequences.

### Rejected alternative

Adding Chaos on every country choice or every atomic value would create severe repeat farming and duplicate source accounting.

## 12. Three achievements test the actual mechanic

### Decision

The achievement set covers harmful recovery, broad provider-family use, and sustained triple abundance.

### Reason

Achievements based only on the event firing or one obvious click would be trivial.
Provider receipts support meaningful conditions and save-safe tracking.

## 13. Asset scope stays focused

### Decision

Plan one report event image and three achievement icon families.

### Reason

The event needs a strong popup identity and achievement coverage.
The standard event surface already provides all required interaction.

### Rejected alternative

Extra decision icons, UI panels, portraits, animation, flags, and 3D assets would have no live consumer.

## 14. The authoritative workbook remains the only catalog edit source

### Decision

Record the old Event 66 row conflict and provide a spreadsheet worker prompt.
Do not edit the supplied CSV snapshots.

### Reason

The project rules identify the XLSX workbook as authoritative and the CSV files as generated exports.
The workbook was not supplied in this task.
