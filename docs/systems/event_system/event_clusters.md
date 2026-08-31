# Event Clusters

## Authority and purpose

Event clusters are a catalogue and dispatch layer above ordinary Chaos Redux random-event selection.

The accepted source contract is [event_clusters_spec.md](event_clusters_spec.md).

This document is the implementation-facing summary for the cluster registry, runtime flow, member rows, Event Logs, Settings, pacing, and history.

A cluster can join related events into one activation, but it cannot replace or weaken ordinary event-system fireability.

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

When this cluster-only minimum or the escalation-support rule blocks a row after the event system accepted it, the row uses a cluster-specific status and leaves the canonical event-system reason empty; the UI must not describe that outcome as failure of the event's independent Chaos Level.

High and Severe non-trigger rows need another base-eligible member.

The trigger row is exempt from that support check.

A sole configured member is exempt from that support check.

Pass one evaluates the trigger and all logical rows against ordinary event-system eligibility and the effective minimum without applying the High or Severe support requirement.

Pass two applies the support requirement to High and Severe non-trigger rows using the pass-one base-eligible set.

The eligible logical count for activation chance is the count that remains after both passes.

The cluster-facing severity corrections are Fury as Medium, Tensions Rising as Low, and Black Plague as Severe.

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

Each eligible cluster calculates and rolls its final chance independently. If several clusters succeed, one successful cluster is selected uniformly; the selected event therefore opens no more than one cluster batch.

Only the selected winner commits success fatigue, history, pacing, and cooldown. Successful candidates that lose arbitration remain unchanged, while genuine failed rolls receive the normal failed-roll fatigue reduction.

### Random Stuff whole-pool activation

Random Stuff is the one registered cluster without configured member rows.

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

Every selected row is guaranteed after eligibility; Random Stuff has no severity floor, escalation-support rule, or optional participation roll.

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

Events 6, 9, and 13 have explicit primary trigger rows for their opening duplicate groups.

Later staged rows retain their own role, severity, declared minimum, chance, and status.

Every activation has a batch identity that binds its cluster, trigger row, member rows, history context, and delayed dispatch context.

Queued records retain the batch, cluster, logical row, trigger, history, and event-specific context needed to recheck and dispatch the exact row.

Delayed dispatch rechecks ordinary event-system fireability immediately before firing.

A row that fails that recheck is skipped and invalidated with N/A and the first canonical event-system reason.

A queued row never substitutes another event, logical row, target, or batch context.

Overlapping batches remain isolated by their batch identity and aligned context.

Runtime state is versioned and non-destructive, so historical snapshots are not rewritten when current definitions or state change.

Random Stuff has no permanent row registry; its selected event IDs receive history-only row identities within the saved batch, and the history sequence keeps repeated selections across different batches distinct.

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

The current registry artifacts define these stable cluster IDs and member patterns.

| Cluster | ID | Member pattern | Scope |
| --- | --- | --- | --- |
| Wars | event_cluster_id.wars | Event 4 Random War with optional Fury support | Sudden wars and armed conflicts that can widen through linked incidents. |
| Liberations | event_cluster_id.liberations | Event 6 opening, escalation, and crisis rows with optional Event 5 Soviet Union Collapse | Independence waves, subject breakaways, imperial ruptures, and secession disorder. |
| Diplomatic Panic | event_cluster_id.diplomatic_panic | Event 8 Tensions Rising with optional Event 17 Random Faction | Pressure spikes, ministry reactions, and relation shocks without direct new war goals. |
| Peace | event_cluster_id.peace | Event 9 opening and follow-up rows | Settlements, ceasefires, exhaustion, negotiations, and de-escalation shocks. |
| Natural Disasters | event_cluster_id.natural_disasters | Event 13 opening and staged seasonal rows | Disaster seasons that grow from local incidents into varied, regional, and abnormal sequences. |
| Formables | event_cluster_id.formables | Event 12 Africa Is One | Negotiated restoration and union projects, including the protection-first Charter League route. |
| Positive Economy | event_cluster_id.economy_positive | Event 18 Resources Found | Beneficial economic shocks with persistent development choices. |
| Diseases | event_cluster_id.diseases | Event 20 Black Plague with optional Event 2 Zombie Outbreak | Severe disease outbreaks with public state conditions, spread, and sustained containment work. |
| Random Stuff | event_cluster_id.random_stuff | No fixed members; 3 to 5 uniformly drawn currently eligible events | Rare whole-pool bonus batches after ordinary minor events from Chaos Tier 3 onward. |

The first logical rows for Events 6, 9, and 13 are primary trigger rows.

The member registry remains authoritative for each row's declared minimum, role, event mapping, and event-specific runtime preparation.

When Event 17 is queued as a Diplomatic Panic member, its event-specific pre-fire helper builds the eligible minor pool and saves its own target country instead of reusing another member's actor.

Natural Disasters rows are logical Event 013 season slots rather than separate event IDs.

Each season slot retains its own stable row ID and event-specific target, evolution, severity, presentation, and scaling context before entering the pending queue, so overlapping batches cannot borrow another slot's disaster context.

Resources Found uses the same pre-fire preparation as ordinary automatic firing to select a valid owner and exact owned or controlled state before dispatch.

The cluster preserves one Positive Economy member while the event-specific discovery and repeat-enrichment paths remain owned by Event 018.

The stable logical row registry is event_cluster_member_row_id.

| Logical row | Stable row ID |
| --- | --- |
| Wars Random War | wars_random_war |
| Wars Fury | wars_fury |
| Liberations Independence opening | liberations_independence_opening |
| Liberations Independence escalation | liberations_independence_escalation |
| Liberations Independence crisis | liberations_independence_crisis |
| Liberations Soviet Collapse | liberations_soviet_collapse |
| Diplomatic Panic Tensions | diplomatic_panic_tensions |
| Diplomatic Panic Faction | diplomatic_panic_faction |
| Peace White Peace opening | peace_white_peace_opening |
| Peace White Peace follow-up | peace_white_peace_followup |
| Natural Disasters opening | natural_disasters_opening |
| Natural Disasters early | natural_disasters_early |
| Natural Disasters varied | natural_disasters_varied |
| Natural Disasters regional | natural_disasters_regional |
| Natural Disasters abnormal | natural_disasters_abnormal |
| Formables Africa | formables_africa |
| Positive Economy Resources | economy_resources |
| Diseases Black Plague | diseases_black_plague |
| Diseases Zombie | diseases_zombie |

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

The HOI4 MCP event route currently returns partial coverage, and the probability inspector discovers no compatible adapter for the scripted-variable Random Stuff pool.

The shared Event Log and Settings GUI routes render successfully, but their synthetic scenarios do not inject a selected Random Stuff runtime state; these pages therefore do not claim full engine or branch-specific visual evidence.

## Future cluster additions

A new cluster must define a stable cluster ID, member rows, role, declared minimum, severity, ordinary event-system eligibility path, runtime context, and history fields.

A new cluster must use the same two-pass support rule, activation formula, trigger-row multiplicity adjustment, multi-cluster one-winner resolution, optional participation table, severity-biased dispatch ordering, delayed recheck, pacing contract, and manual memory isolation.

A new cluster must preserve stable logical row identities when duplicate event IDs represent stages or variants.

A new cluster must document its catalog and Settings presentation without requesting new visual assets unless existing surfaces cannot express the contract.
