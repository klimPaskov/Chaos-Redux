# Event Clusters

## Unresolved contract alignment

The [contract candidate](event_clusters_spec.md#unresolved-cross-document-claims) records the differing Negative Economy unlock levels, Acid Rain severity-floor and pacing exceptions, and worked-example inputs that still need reconciliation.
This runtime reference preserves its existing membership and source claims without selecting an approved value or providing a current probability audit.

## Authority and purpose

Event clusters are a catalogue and dispatch layer above ordinary Chaos Redux random-event selection.

The source contract candidate is [event_clusters_spec.md](event_clusters_spec.md), pending the attributable acceptance record described there.

This document is the implementation-facing summary for the cluster registry, runtime flow, member rows, Event Logs, Settings, pacing, and history.

A cluster can join related events into one activation, but it cannot replace or weaken ordinary event-system fireability.

## Catalogue and runtime authority

The fixed catalogue in this document is the v2 catalogue from `C:/Users/klimp/Downloads/chaos_redux_clusters_catalog_updated_v2.csv`.

Historical source note: `C:/Users/klimp/Downloads/chaos_redux_clusters_catalog_updated_v2.csv` was absent at that absolute Downloads path when checked on 2026-09-05. Related current catalog surfaces are `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and the export `docs/spreadsheets/chaos_redux_clusters_catalog.csv`. Those files remain outside this bounded documentation scope, and this note does not assert that either current artifact replaces the historical CSV.

The fixed catalogue contains cluster IDs 1 through 18 exactly as listed in the catalogue table below.

The memberless Random Stuff runtime cluster is retained at ID 19 and is documented separately from the 18-row fixed catalogue.

Catalogue `Chaos level` values map to zero-based internal unlock tiers as follows: level 1 maps to tier 0, level 2 maps to tier 1, level 3 maps to tier 2, and level 4 maps to tier 3.

Catalogue types map as follows: `Minor Fire-Once` is the runtime `one_time` type, and `Minor Repeatable` is the runtime `repeatable` type.

Required status and declared minimum-tier values remain runtime architecture metadata.

The exact membership matrix below is authoritative only for event slot and member severity.

The event-system fireability contract remains authoritative for whether a trigger or member can actually dispatch.

## Ordinary event-system eligibility

The ordinary event-system eligibility contract is authoritative for automatic triggers, normal manual triggers, required rows, optional rows, and delayed member dispatch.

Cluster logic can only narrow that eligibility.

A selected automatic trigger must pass ordinary event-system eligibility before the cluster lookup and activation roll.

If the selected trigger fails ordinary eligibility, the cluster does not roll and the selection continues through ordinary standalone handling.

Required status means 100 percent participation after eligibility and never bypasses event fireability.

Manual cluster forcing may bypass cluster-only gates such as the cluster unlock tier, cluster cooldown, cluster enable state, and the automatic activation roll.

Manual cluster forcing still uses the equivalent event-system force context for the trigger and every member.

An event-system rejection therefore blocks dispatch even when cluster-only gates were bypassed.

## Severity floors and two-pass eligibility

Event Chaos Levels remain independent from cluster member severity.

The severity floor is a separate minimum for cluster participation.

| Member severity | Severity floor | Existing tier name |
| --- | --- | --- |
| Low | T0 | Calm World |
| Medium | T1 | Gathering Storm |
| High | T2 | Rising Chaos |
| Severe | T3 | Chaos Tier |

The effective minimum is:

    effective_member_min = max(severity_floor, declared_member_min)

When this cluster-only minimum or the escalation-support rule blocks a row after the event system accepted it, the row uses a cluster-specific status and leaves the canonical event-system reason empty.
The UI must not describe that outcome as failure of the event's independent Chaos Level.

High and Severe non-trigger rows need another base-eligible member.

The trigger row is exempt from that support check.

A sole configured member is exempt from that support check.

Pass one evaluates the trigger and all logical rows against ordinary event-system eligibility and the effective minimum without applying the High or Severe support requirement.

Pass two applies the support requirement to High and Severe non-trigger rows using the pass-one base-eligible set.

The eligible logical count for activation chance is the count that remains after both passes.

The current catalogue assigns Fury separate Medium and High rows, Tensions Rising Medium severity, and Black Plague Severe severity.

## Activation chance

Activation chance is evaluated only for an eligible automatic trigger and an eligible cluster.

| Current tier | Base |
| --- | ---: |
| T0 Calm World | 5 |
| T1 Gathering Storm | 10 |
| T2 Rising Chaos | 15 |
| T3 Chaos Tier | 25 |
| T4 Totalen Chaos | 35 |
| T5 World Collapse | 50 |

| Trigger severity | Factor |
| --- | ---: |
| Low | 1.35 |
| Medium | 1.15 |
| High | 0.85 |
| Severe | 0.65 |

| Eligible logical rows | Factor |
| --- | ---: |
| 1 | 1.40 |
| 2 | 1.30 |
| 3 | 1.20 |
| 4 | 1.10 |
| 5 or more | 1.00 |

Fatigue is clamped to a score of 0 through 4, and its factor is 0.90 raised to that score.

| Previous optional participation ratio | Factor |
| --- | ---: |
| 25 percent or less | 1.40 |
| More than 25 percent through 50 percent | 1.30 |
| More than 50 percent through 75 percent | 1.15 |
| More than 75 percent | 1.00 |
| Zero optional denominator | 1.00 |

The previous ratio excludes trigger and required rows and uses actually dispatched eligible optional rows from the last completed automatic batch.

The activation formula is:

    activation_chance = clamp(round(base × trigger_severity_factor × eligible_count_factor × fatigue_factor × previous_participation_factor), 1, 90)

Fatigue increases by one after a successful automatic activation.

Fatigue decreases by one after a valid failed automatic activation roll.

Gated attempts, failed preflight, and manual forcing leave fatigue unchanged.

A valid failed roll returns to ordinary standalone handling and does not apply cluster pacing or a cluster cooldown update.

### Duplicate triggers and multiple memberships

Membership discovery scans every registered fixed-member cluster instead of stopping at the first match. Automatic candidacy requires the selected event to own a configured primary-trigger row in that cluster.

Within each candidate cluster, every currently eligible logical row carrying the selected trigger event strengthens that cluster's trigger-specific chance:

    multiplicity_factor = 1 + 0.15 × (eligible_matching_rows - 1)

Every extra eligible matching row guarantees at least one additional percentage point before the ordinary 90 percent activation ceiling. Duplicate rows never dispatch the selected trigger more than once.

Each eligible cluster calculates and rolls its final chance independently. If several clusters succeed, one successful cluster is selected uniformly.
The selected event therefore opens no more than one cluster batch.

Only the selected winner commits success fatigue, history, pacing, and cooldown. Successful candidates that lose arbitration remain unchanged, while genuine failed rolls receive the normal failed-roll fatigue reduction.

### Random Stuff whole-pool activation

Random Stuff is the retained memberless runtime cluster at ID 19 and has no configured fixed-member rows.

It unlocks at Chaos Tier 3 and receives exactly one dynamic automatic attempt after a successfully dispatched ordinary minor event.

Manual event firing, major events, ordinary cluster members, and Random Stuff members do not create attempts.

The automatic roll uses integer basis points on a 1 through 10,000 scale.

| Current tier | Base chance | Batch size |
| --- | ---: | ---: |
| T3 Chaos Tier | 0.30 percent | 3 |
| T4 Totalen Chaos | 0.60 percent | 4 |
| T5 World Collapse | 0.85 percent | 5 |

Every valid failed attempt adds 0.0025 percentage points of drought relief before the live chance is rounded to whole basis points.

The prospective third success multiplies the chance by 0.75, and later successes multiply it by 0.50.

The chance has no special one-percent ceiling. Long dry streaks can carry it above one percent, while the roll scale supplies only the natural 100 percent probability limit.

A successful automatic activation starts a 240-day cooldown and resets the drought count.

Gated attempts, insufficient eligible pools, cooldown checks, disabled state, and first-member runtime failure do not change drought or success memory.

At activation, Random Stuff scans `global.all_events` through the ordinary event-system selection evaluator, including positive current selectable weight, and excludes the minor event that opened the attempt.

It then samples uniformly without replacement from that eligible pool.

Major or minor classification, severity, and the magnitude of a positive selection weight do not influence the uniform draw.

The first selected event is rechecked and dispatched synchronously.

The remaining selected events use the shared delayed batch queue and receive another authoritative event-system recheck before dispatch.

Every selected row is guaranteed after eligibility.
Random Stuff has no severity floor, escalation-support rule, or optional participation roll.

The ordinary minor event that opened the attempt already supplied the batch's single pacing update, so Random Stuff does not apply a second aggregate pacing update.

Manual Random Stuff activation bypasses its tier, disabled state, cooldown, and activation roll, but it still constructs the same strict current eligible pool and never changes automatic drought, success, or cooldown state.

## Optional participation and dispatch order

The trigger is guaranteed and fires first synchronously after eligibility.

Required rows are guaranteed after eligibility and follow in declaration order.

Optional ordering is severity-biased rather than severity-locked.

The system preserves Low, Medium, High, then Severe bands in 90 percent of Calm World batches, 88 percent at Gathering Storm, 86 percent at Rising Chaos, 84 percent at Chaos Tier, 82 percent at Totalen Chaos, and 80 percent at World Collapse.

Within that majority path, rows are randomized inside each severity band.

The remaining batches select one random boundary between adjacent severity bands and invert the two rows at that boundary, allowing Medium, High, or Severe members to be evaluated and dispatched before a lower-severity member.

A batch containing only one optional severity band cannot form a cross-severity inversion and remains randomized within that band.

Participation decay follows the resulting order, so a higher-severity member can receive an earlier optional roll during an inversion batch.

The optional participation table is:

| Current tier | Low | Medium | High | Severe |
| --- | ---: | ---: | ---: | ---: |
| Calm World | 70 | 35 | 15 | 5 |
| Gathering Storm | 80 | 40 | 20 | 10 |
| Rising Chaos | 90 | 45 | 25 | 15 |
| Chaos Tier | 95 | 50 | 30 | 20 |
| Totalen Chaos | 99 | 60 | 40 | 25 |
| World Collapse | 100 | 75 | 50 | 30 |

Each eligible optional row uses:

    optional_member_chance = clamp(round(table_value × eligible_count_factor × 0.95^(accepted_optional_rows)), 1, 100)

The accepted optional count increases only after an optional row is accepted in the current batch.

Ineligible, rejected, or invalidated optional rows do not increase that count.

## Stable rows, batches, and delayed state

Every configured fixed member has a stable logical row identity.

Stable logical rows keep duplicate event IDs distinct.

Events 4, 6, 7, 9, and 13 have explicit primary trigger rows for their opening duplicate groups.

Later staged rows retain their own role, severity, declared minimum, chance, and status.

Every activation has a batch identity that binds its cluster, trigger row, member rows, history context, and delayed dispatch context.

Queued records retain the batch, cluster, logical row, trigger, history, and event-specific context needed to recheck and dispatch the exact row.

Delayed dispatch rechecks ordinary event-system fireability immediately before firing.

A row that fails that recheck is skipped and invalidated with N/A and the first canonical event-system reason.

A queued row never substitutes another event, logical row, target, or batch context.

Overlapping batches remain isolated by their batch identity and aligned context.

### Non-destructive semantic-ID migration

Runtime version 2 preserves stable semantic row IDs for pre-existing logical rows.

Every new logical row receives a globally unique runtime row ID.

The versioned migration remaps only persisted cluster-ID fields after the complete legacy 1–12 registry sequence proves their old meanings. Snapshotted member severity, role, tier, chance, roll, status, batch context, and event-specific queue context remain unchanged.

Cluster ID 3 retains the Diplomacy semantic identity formerly named Diplomatic Panic.

IDs 8 through 12 are semantically reassigned to Intelligence, Scientific Research, Negative Economy, Various Anomalies, and Pacts.

Diseases uses ID 13, and the memberless Random Stuff runtime cluster uses ID 19.

Legacy numeric IDs are migration inputs only and are not additional registered clusters.

Settings navigation follows the registered 1–19 sequence and never exposes unregistered numeric IDs.

Runtime state is versioned and non-destructive, so historical snapshots are not rewritten when current definitions or state change.

Random Stuff has no permanent row registry.
Its selected event IDs receive history-only row identities within the saved batch, and the history sequence keeps repeated selections across different batches distinct.

The automatic transition is ordinary-pool selection, ordinary event-system eligibility, multi-cluster candidate discovery, per-cluster gates and activation rolls, one-winner resolution, batch preparation, synchronous trigger, required rows, severity-biased optional ordering, delayed rechecks, successful history commit, and one pacing/cooldown update.

A rejected trigger exits before cluster rolling and continues through standalone handling.

A gated or preflight-failed attempt leaves automatic memory unchanged, while a valid failed roll decreases fatigue and returns to standalone handling.

An accepted optional row increments the current-batch decay count, while a rejected or invalidated optional row does not.

A manual force bypasses only cluster-only gates, checks the equivalent event-system force context, and dispatches without an activation roll or automatic-memory update.

## Pacing, cooldown, and history

Each successful cluster activation applies one cluster pacing update and one cluster cooldown update for the complete batch.

Member count does not multiply either update.

Repeatable and one-time clusters count once for global timer compression and dynamic major-event gain.

An intentionally registered major cluster uses its major pacing path once and resets major-event weights once.

Each dispatched member still uses its ordinary fired-state, fire-once, repeatable recovery, and event-history behavior.

Only a successful cluster activation creates a cluster history row.

The history row snapshots activation chance, activation roll, trigger, batch, tier, actor, and valid context.

Every member snapshot stores chance, roll, role, severity, effective minimum, status, and canonical reason.

Guaranteed trigger and required rows store 100 percent and Guaranteed after eligibility.

Ineligible or invalidated rows store N/A for chance and roll and retain their canonical reason.

Manual rows store Manual and no roll.

A successful activation creates its history row before delayed members dispatch, so queued member status, canonical reason, final chance, and roll remain provisional until that batch settles.

After batch settlement, historical snapshots never recompute from current Chaos tier, fatigue, member definitions, event weights, or event-system availability.

Automatic fatigue and previous-participation memory exclude manual activations.

## Registered cluster families

The v2 fixed catalogue is reproduced exactly below so that cluster IDs, names, player-facing details, member ID lists, severity lists, types, catalogue Chaos levels, and catalogue statuses can be reviewed together.

| Cluster ID | Cluster Name | Details | Members (ID) | Member Severities | Type | Chaos level | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Wars | Sudden wars and armed conflicts break out between countries, turning local disputes, opportunistic attacks, internal fractures, and alliance betrayals into wider fighting. | 4, 4, 4, 4, 7, 7, 21, 45, 62 | Low, Low, Medium, High, Medium, High, Medium, High, High | Minor Repeatable | 1 | In progress |
| 2 | Liberations | Liberation shocks create independent countries, break subjects and unions apart, and connect newly freed states through wider liberation crises. | 5, 6, 6, 6, 63 | Severe, Low, Medium, High, Medium | Minor Repeatable | 1 | In progress |
| 3 | Diplomacy | International relations destabilize through diplomatic crises, faction pressure, treaties, strategic alignment, aggressive posturing, and intervention. | 8, 17, 36, 59 | Medium, Medium, High, High | Minor Repeatable | 1 | In progress |
| 4 | Peace | Peace shocks reduce or reverse conflict through settlements, ceasefires, demobilization, exhaustion, negotiations, and forced returns toward peacetime. | 9, 9, 9, 9, 61 | Low, Low, Medium, High, High | Minor Repeatable | 1 | In progress |
| 5 | Natural Disasters | Natural and environmental catastrophes strike states or regions through five distinct Natural Disasters slots, followed by optional Acid Rain and Heat Wave crises. A sequence containing Acid Rain commits Major-event pacing once while preserving the cluster history. | 13, 13, 13, 13, 13, 33, 51 | Low, Low, Low, Low, Medium, Severe, High | Minor Repeatable | 1 | In progress |
| 6 | Formables | Countries revive, construct, or transform into major historical, religious, imperial, or alternative political formations. | 3, 12, 38, 48 | High, Severe, High, Medium | Minor Repeatable | 3 | In progress |
| 7 | Positive Economy | Beneficial economic shocks create sudden growth, wealth, industry, infrastructure, construction, cheaper activity, or profitable underground markets. | 18, 26, 29, 34, 55, 57, 58 | Medium, Medium, Medium, Low, Medium, High, Medium | Minor Repeatable | 1 | In progress |
| 8 | Intelligence | Espionage, leaks, investigations, covert information, and intelligence failures expose or manipulate states through hidden information. | 39, 52 | Medium, Low | Minor Fire-Once | 1 | New |
| 9 | Scientific Research | Scientific and technological shocks accelerate, distort, gift, or destroy research progress and the institutions that produce it. | 16, 24, 27, 54, 60 | Severe, High, Medium, Medium, High | Minor Fire-Once | 2 | New |
| 10 | Negative Economy | Economic crises damage production, trade, employment, and industrial capacity. Great Depression 2.0 is the cluster's Low baseline member, while harsher consequences depend on the crisis conditions it develops. | 35, 50 | Low, Medium | Minor Fire-Once | 1 | New |
| 11 | Various Anomalies | Genuinely anomalous events that do not fit a more specific thematic cluster. | 47 | Low | Minor Fire-Once | 4 | New |
| 12 | Pacts | Countries create secret, unusual, or rapidly assembled pacts and alliance arrangements that can reshape later conflicts. | 11 | High | Minor Fire-Once | 3 | New |
| 13 | Diseases | Disease outbreaks and biological crises spread through countries, armies, and populations, creating escalating health and military emergencies. | 2, 20, 41 | Severe, Severe, Low | Minor Repeatable | 1 | New |
| 14 | Randomizations | Core parts of the game state are deliberately randomized, producing large systemic changes rather than a conventional political or economic incident. | 46 | Medium | Minor Repeatable | 1 | New |
| 15 | Sudden Abundance | Countries suddenly receive large quantities of manpower, wealth, equipment, weapons, fleets, structures, or other valuable assets without normal buildup. | 19, 29, 32, 37, 42, 56, 64 | Medium, Medium, Medium, Medium, Low, Medium, Medium | Minor Repeatable | 1 | New |
| 16 | Domestic Unrest | Internal instability produces insurgency, separatism, terrorism, civil conflict, and breakaway movements inside or against existing states. | 1, 6, 21, 31, 63 | Medium, High, Low, Medium, Medium | Minor Repeatable | 1 | New |
| 17 | Alien Invasions | Extraterrestrial or non-human invasion forces directly threaten countries, territory, and the existing international order. | 43 | Severe | Minor Fire-Once | 1 | New |
| 18 | Military Preparation | States rapidly acquire the doctrine, strategic weapons, equipment, fortifications, institutions, and military capacity needed for future conflict. | 22, 27, 32, 42, 56, 64 | High, Medium, Medium, Low, Medium, Medium | Minor Repeatable | 1 | New |

The fixed catalogue table contains 18 rows.

The current membership matrix contains 75 logical rows.

It retains the supplied v2 matrix outside the explicitly revised Wars and Natural Disasters repeated-slot sequences.

| Cluster ID | Cluster Name | Slot | Event ID | Event Name | Severity | Membership Notes |
| --- | --- | ---: | ---: | --- | --- | --- |
| 1 | Wars | 1 | 4 | Random War | Low | Logical slot 1 of 4 in Wars. |
| 1 | Wars | 2 | 4 | Random War | Low | Logical slot 2 of 4 in Wars. |
| 1 | Wars | 3 | 4 | Random War | Medium | Logical slot 3 of 4 in Wars. |
| 1 | Wars | 4 | 4 | Random War | High | Logical slot 4 of 4 in Wars. |
| 1 | Wars | 5 | 7 | Fury | Medium | Logical slot 1 of 2 in Wars. |
| 1 | Wars | 6 | 7 | Fury | High | Logical slot 2 of 2 in Wars. |
| 1 | Wars | 7 | 21 | Random Civil War | Medium | Also Domestic Unrest at Low severity. |
| 1 | Wars | 8 | 45 | Third Balkan War | High |  |
| 1 | Wars | 9 | 62 | Allies Backstab | High |  |
| 2 | Liberations | 1 | 5 | Soviet Union Collapse | Severe |  |
| 2 | Liberations | 2 | 6 | Independence Wave | Low | Logical slot 1 of 3 in Liberations. |
| 2 | Liberations | 3 | 6 | Independence Wave | Medium | Logical slot 2 of 3 in Liberations. |
| 2 | Liberations | 4 | 6 | Independence Wave | High | Logical slot 3 of 3 in Liberations. |
| 2 | Liberations | 5 | 63 | Subjects Break Free | Medium | Also Domestic Unrest at Medium severity. |
| 3 | Diplomacy | 1 | 8 | Tensions Rising | Medium |  |
| 3 | Diplomacy | 2 | 17 | A Faction Comes Calling | Medium |  |
| 3 | Diplomacy | 3 | 36 | Chemical and Biological Weapons Convention | High |  |
| 3 | Diplomacy | 4 | 59 | The Offensive | High | Moved from Wars to Diplomacy. |
| 4 | Peace | 1 | 9 | White Peace | Low | Logical slot 1 of 4 in Peace. |
| 4 | Peace | 2 | 9 | White Peace | Low | Logical slot 2 of 4 in Peace. |
| 4 | Peace | 3 | 9 | White Peace | Medium | Logical slot 3 of 4 in Peace. |
| 4 | Peace | 4 | 9 | White Peace | High | Logical slot 4 of 4 in Peace. |
| 4 | Peace | 5 | 61 | Return to Peacetime | High | Moved from Negative Economy to Peace. |
| 5 | Natural Disasters | 1 | 13 | Natural Disasters | Low | Logical Natural Disasters slot 1 of 5. |
| 5 | Natural Disasters | 2 | 13 | Natural Disasters | Low | Logical Natural Disasters slot 2 of 5. |
| 5 | Natural Disasters | 3 | 13 | Natural Disasters | Low | Logical Natural Disasters slot 3 of 5. |
| 5 | Natural Disasters | 4 | 13 | Natural Disasters | Low | Logical Natural Disasters slot 4 of 5. |
| 5 | Natural Disasters | 5 | 13 | Natural Disasters | Medium | Logical Natural Disasters slot 5 of 5. |
| 5 | Natural Disasters | 6 | 33 | Acid Rain | Severe | Optional Severe member. A prepared queue containing Acid Rain commits Major pacing once. |
| 5 | Natural Disasters | 7 | 51 | Heat Wave | High | Optional High member after Acid Rain. |
| 6 | Formables | 1 | 3 | The Holy Realm | High |  |
| 6 | Formables | 2 | 12 | Africa Is One | Severe |  |
| 6 | Formables | 3 | 38 | Malta Crusaders | High |  |
| 6 | Formables | 4 | 48 | Old Great Bulgaria | Medium |  |
| 7 | Positive Economy | 1 | 18 | Resources Found | Medium |  |
| 7 | Positive Economy | 2 | 26 | Black Friday | Medium |  |
| 7 | Positive Economy | 3 | 29 | Riches Found | Medium | Also Sudden Abundance at Medium severity. |
| 7 | Positive Economy | 4 | 34 | Industrial Boom | Low |  |
| 7 | Positive Economy | 5 | 55 | The Great Infrastructure Project | Medium |  |
| 7 | Positive Economy | 6 | 57 | The Black Market | High |  |
| 7 | Positive Economy | 7 | 58 | Random Buildings | Medium |  |
| 8 | Intelligence | 1 | 39 | Murder Mystery | Medium |  |
| 8 | Intelligence | 2 | 52 | Intel Leaked | Low |  |
| 9 | Scientific Research | 1 | 16 | Brilliant Scientist | Severe |  |
| 9 | Scientific Research | 2 | 24 | Video Game in Sweden | High |  |
| 9 | Scientific Research | 3 | 27 | Doctrine Research | Medium | Also Military Preparation at Medium severity. |
| 9 | Scientific Research | 4 | 54 | Gift from Scientists | Medium |  |
| 9 | Scientific Research | 5 | 60 | Research Failure | High |  |
| 10 | Negative Economy | 1 | 35 | Great Depression 2.0 | Low |  |
| 10 | Negative Economy | 2 | 50 | The Great Embargo | Medium |  |
| 11 | Various Anomalies | 1 | 47 | BOOM | Low |  |
| 12 | Pacts | 1 | 11 | Secret Alliance | High |  |
| 13 | Diseases | 1 | 2 | Zombie Outbreak | Severe |  |
| 13 | Diseases | 2 | 20 | Black Plague | Severe |  |
| 13 | Diseases | 3 | 41 | Disease in Divisions | Low |  |
| 14 | Randomizations | 1 | 46 | The Great Shuffle | Medium |  |
| 15 | Sudden Abundance | 1 | 19 | Soldiers from Nowhere | Medium |  |
| 15 | Sudden Abundance | 2 | 29 | Riches Found | Medium | Also Positive Economy at Medium severity. |
| 15 | Sudden Abundance | 3 | 32 | Missiles | Medium | Also Military Preparation at Medium severity. |
| 15 | Sudden Abundance | 4 | 37 | Mysterious People | Medium |  |
| 15 | Sudden Abundance | 5 | 42 | Equipment from Heavens | Low | Also Military Preparation at Low severity. |
| 15 | Sudden Abundance | 6 | 56 | The Navy | Medium | Also Military Preparation at Medium severity. |
| 15 | Sudden Abundance | 7 | 64 | Border Fortifications | Medium | Also Military Preparation at Medium severity. |
| 16 | Domestic Unrest | 1 | 1 | Communist Insurgency | Medium |  |
| 16 | Domestic Unrest | 2 | 6 | Independence Wave | High | Also three separate Liberations slots. |
| 16 | Domestic Unrest | 3 | 21 | Random Civil War | Low | Also Wars at Medium severity. |
| 16 | Domestic Unrest | 4 | 31 | Random Terror | Medium |  |
| 16 | Domestic Unrest | 5 | 63 | Subjects Break Free | Medium | Also Liberations at Medium severity. |
| 17 | Alien Invasions | 1 | 43 | Monsters from the Deep | Severe |  |
| 18 | Military Preparation | 1 | 22 | Concentration Camps | High |  |
| 18 | Military Preparation | 2 | 27 | Doctrine Research | Medium | Also Scientific Research at Medium severity. |
| 18 | Military Preparation | 3 | 32 | Missiles | Medium | Also Sudden Abundance at Medium severity. |
| 18 | Military Preparation | 4 | 42 | Equipment from Heavens | Low | Also Sudden Abundance at Low severity. |
| 18 | Military Preparation | 5 | 56 | The Navy | Medium | Also Sudden Abundance at Medium severity. |
| 18 | Military Preparation | 6 | 64 | Border Fortifications | Medium | Also Sudden Abundance at Medium severity. |

Repeated Event IDs represent distinct logical slots and are not deduplicated.

When an event belongs to multiple clusters, each cluster rolls independently.

If several cluster rolls succeed, winner selection is uniform across the successful clusters.

The repeated slots remain separate within their cluster and increase that event's trigger-specific chance through the cluster multiplicity rule.

Acid Rain is an optional Severe member from Gathering Storm onward. Its tier-aware participation stays subject to the cluster cap, while a prepared queue containing it reserves Event 33 and commits Major pacing once before member dispatch.
Event 33's shared runtime then suppresses a second Major reset.

### Retained memberless runtime cluster

| Cluster ID | Cluster Name | Fixed members | Runtime status |
| --- | --- | --- | --- |
| 19 | Random Stuff | None | Retained memberless whole-pool runtime cluster. |

Random Stuff has no fixed membership row in the supplied v2 matrix.

The runtime ID 19 entry retains the separate whole-pool activation contract documented above.

### Negative Economy: Great Depression 2.0

Cluster ID `10` is the Negative Economy cluster.

Event 035 Great Depression 2.0 is the Negative Economy slot 1 member with Low severity.

Its runtime role and declared minimum remain architecture metadata rather than membership-catalogue fields.

The cluster dispatch preserves the selected Event 35 country and enters the same fail-closed independent start contract used by standalone firing. Cluster dispatch never rerolls the target, never duplicates an active depression, and never gives contagion, worldwide conversion, Event 34 inheritance, or relapse ownership of normal pacing.

### Wars: Random War, Fury, and Random Civil War

The Wars cluster contains four Event 004 Random War rows at Low, Low, Medium, and High severity, followed by two Event 007 Fury rows at Medium and High severity.

Event 021 Random Civil War follows at Medium severity, with Third Balkan War and Allies Backstab retaining High severity.

The first Random War and Fury rows are their primary trigger rows, so a selected Random War uses Low trigger severity and a selected Fury uses Medium trigger severity for activation.

Their later duplicate rows retain their own severity floors, participation chances, and order scores.

Event 021 also belongs to Domestic Unrest at slot 3 with Low severity.

Those two Event 021 memberships roll independently and remain distinct logical rows.

Event 004, Event 007, and Event 021 reserve a target before opening mutations, treat an existing reservation as a collision, and retain a stable reservation receipt until the member succeeds or rolls back.

The Event 021 target reservation is `random_civil_war_cluster_target_reserved`, and a failed route, missing capital, missing remnant, unavailable package, exhausted capacity, or collision records an explicit skip reason.

When no valid Event 021 target exists, the member presents `N/A` and its live automatic weight is zero.

The Wars cluster continues to use one pacing event and one cluster cooldown, so Event 021’s scheduler does not create an additional unbounded pacing loop.

Manual cluster forcing bypasses cluster-only tier, cooldown, enable, and roll gates but still passes Event 021 route, reservation, plan, capacity, and cleanup checks.

## Event Logs and Settings

The Clusters tab lists the registered catalogue.

History lists only successful cluster activations.

Catalogue and Settings activation summaries use the copy Varies by member when member rows have different computed chances.

Cluster details expose role, severity, effective minimum, ordinary event-system availability, and starting chance for each member row.

Unique event details show the current trigger-specific activation chance.

Duplicate staged IDs show Varies by row because one event ID represents multiple logical rows.

By Roll is the live automatic-pool-weighted mean of distinct eligible trigger events.

    by_roll = sum(trigger_event_weight × trigger_activation_chance) / sum(trigger_event_weight)

The mean uses only distinct trigger events with positive ordinary automatic-pool weight.

Unavailable or zero-weight rows show N/A instead of zero.

Cluster sorting includes By Cluster ID, By Type, By Roll, By Unlock Tier, By Member Count, and By Fired, with Ascending and Descending order.

Catalogue details use current state.

History details use the stored snapshot and never recompute.

Clicking a member row opens its ordinary event details without replacing its cluster context.

Manual Settings triggering follows the manual cluster path and the event-system force context for every trigger and member.

The Settings Event Clusters view lets the player select a cluster ID, inspect its name, type, unlock tier, current tier, activation summary, member count, and status, and manually trigger the selected cluster.

The manual result reports whether the selected cluster fired, was unknown, or failed because runtime setup could not build the required scopes.

Manual forcing bypasses cluster-only tier, cooldown, enable, and activation-roll gates but does not bypass equivalent event-system fireability for any trigger or member.

## Existing UI assets

No new visual assets are required.

The cluster catalogue, details, and Settings surfaces reuse existing Event Logs and Settings sprites, buttons, checkboxes, fonts, and flag surfaces.

## Runtime artifact references

Cluster registration and dispatch are owned by common/script_constants/event_cluster_constants.txt and common/scripted_effects/chaosx_event_cluster_effects.txt.

The event cluster event roots remain in events/chaosx_event_clusters.txt, and shared Settings attachment remains in interface/chaosx.gui.

Random selection, event-system eligibility, timers, and member fired-state handling remain in common/scripted_effects/chaosx_logic_effects.txt and common/scripted_effects/chaosx_settings_effects.txt.

Event-log state and history remain in common/scripted_effects/chaosx_events_log_effects.txt, common/scripted_guis/chaosx_scripted_gui_events_log.txt, interface/chaosx_events_log_popup.gui, and the matching scripted-localisation and GUI-localisation files.

The event-system relationship is documented in event_chaos_levels.md and dynamic_major_event_weights.md.

The Event Logs presentation is documented in events_log_window.md and events_log_evolutions_and_clusters.md.

The 2026-09-05 curator's read-only MCP evidence and its limits are recorded in [event_clusters_spec.md](event_clusters_spec.md#12-artifact-ownership-and-external-validation). The required narrow event and GUI inspections stalled before returning a result in that probe, so this page does not claim current engine or branch-specific visual acceptance.

## Future cluster additions

A new cluster must define a stable cluster ID, member rows, role, declared minimum, severity, ordinary event-system eligibility path, runtime context, and history fields.

A new cluster must use the same two-pass support rule, activation formula, trigger-row multiplicity adjustment, multi-cluster one-winner resolution, optional participation table, severity-biased dispatch ordering, delayed recheck, pacing contract, and manual memory isolation.

A new cluster must preserve stable logical row identities when duplicate event IDs represent stages or variants.

A new cluster must document its catalog and Settings presentation without requesting new visual assets unless existing surfaces cannot express the contract.
