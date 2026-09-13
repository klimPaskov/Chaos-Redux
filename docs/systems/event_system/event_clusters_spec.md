# Chaos Redux Event Cluster System Contract

## Unresolved cross-document claims

The source contract remains subject to the acceptance boundary below.
Its completed checklist items are retained source-implementation claims, not independently verified completion or acceptance of every design detail.

- In the captured working-tree documents, this file's catalogue gives Negative Economy Chaos level 2, while the catalogue in [event_clusters.md](event_clusters.md) gives level 1.
- The common Severe-member floor is T3, while the runtime reference describes Acid Rain participation from Gathering Storm, T1, onward.
The documents do not explain the acceptance basis and scope of that exception together.
- The general pacing rule describes one minor update for repeatable clusters, while the Natural Disasters record describes a Major update when the prepared queue contains Acid Rain.
- The worked small-cluster example starts with two eligible logical rows but subsequently describes a trigger, a required row, and optional rows.
The optional-decay example continues that setup with another optional row.
- The High-severity support example says no other row is base-eligible while also describing an eligible trigger.

These scenario definitions and special cases require owner reconciliation before they can serve as matching probability-audit fixtures.
The original formulas, values, tables, and examples remain unchanged.
See the [shared documentation review](../../plans/repo_cleanup/subagent_handoffs/2026-09-05_shared_events_documentation.md) for exact scope and evidence limits.

## Contract status and scope

This file retains the source contract candidate for the Dynamic Severity-Aware Cluster Overhaul.

The repository evidence named for this pass does not include an attributable user decision or parent acceptance for each exact formula, membership, and scenario claim. The prior documentation handoff describes the overhaul as user-approved but does not preserve the decision text. The explicit approval available in [2026-09-05_documentation_batch01.md](../../plans/repo_cleanup/subagent_handoffs/2026-09-05_documentation_batch01.md) authorizes full-reading documentation batches and does not accept cluster behavior.

The contract is therefore retained for parent review, while implementation-facing files and historical handoffs remain evidence of what was described or implemented.

Event clusters are a catalogue and dispatch layer above ordinary Chaos Redux random-event selection.

The cluster layer may narrow ordinary event eligibility, but it never replaces the event system's fireability contract.

This contract covers automatic selection, normal manual firing, manual cluster forcing, member eligibility, severity, activation and participation chance, queue state, history, pacing, Event Logs, Settings, catalog presentation, and acceptance evidence.

The Events sheet records every distinct cluster ID for an event and does not store a scalar member severity.

The current fixed catalogue and 75-row membership matrix are reproduced in [event_clusters.md](event_clusters.md).

They retain the supplied v2 catalogue and memberships except where explicit later direction revised the repeated Wars and Natural Disasters slots.

The fixed catalogue uses cluster IDs 1 through 18.

The memberless Random Stuff runtime cluster is retained at ID 19 outside the fixed catalogue rows.

Catalogue Chaos levels map to zero-based internal unlock tiers, with level 1 to tier 0, level 2 to tier 1, level 3 to tier 2, and level 4 to tier 3.

Catalogue types map `Minor Fire-Once` to runtime `one_time` and `Minor Repeatable` to runtime `repeatable`.

Required status and declared minimum-tier values remain runtime architecture metadata, while the supplied membership matrix is authoritative only for event slot and member severity.

## 1. Ordinary event-system authority

Ordinary event-system eligibility is authoritative for every automatic trigger, manual trigger, required row, optional row, and delayed member dispatch.

Cluster logic can only narrow that eligibility.

The ordinary event system remains responsible for event toggles, normal trigger and target requirements, Event Chaos level, fire-once or repeatable state, stored weight and cap state, force context, and every event-specific fireability condition.

Required status means 100 percent participation after the row is eligible.

Required status never bypasses event fireability.

An ineligible required row is not forced to fire, and its history snapshot carries N/A with the canonical invalidation reason.

When the selected trigger event is rejected by the ordinary event system, the cluster does not roll.

The rejected selection continues through ordinary standalone handling, which may reject it again under the same event-system rules.

Automatic cluster activation is therefore a conversion of an already valid automatic selection, not a second event picker.

Manual cluster forcing may bypass cluster-specific gates such as the cluster unlock tier, cluster cooldown, cluster enable state, and the automatic activation roll.

Manual cluster forcing cannot fire a trigger or member that the equivalent event-system force context rejects.

Manual cluster forcing does not borrow automatic fatigue or previous-participation memory, and it does not write automatic-roll memory.

## 2. Event Chaos Levels and member severity

Event Chaos Levels remain an independent event property with the existing six tiers and existing assignments.

The normal event-system check for an event Chaos Level occurs before a cluster can activate that event automatically.

Member severity supplies a separate cluster-member floor.

The severity floor mapping is:

| Member severity | Severity floor | Existing tier name |
| --- | --- | --- |
| Low | T0 | Calm World |
| Medium | T1 | Gathering Storm |
| High | T2 | Rising Chaos |
| Severe | T3 | Chaos Tier |

The effective member minimum is the greater of the severity floor and the declared member minimum.

In formula form:

    effective_member_min = max(severity_floor, declared_member_min)

The effective member minimum is an additional cluster constraint and does not replace the event's own Event Chaos Level.

A cluster-only floor or escalation-support failure uses a cluster-specific row status while retaining no event-system failure reason, so it cannot be mistaken for failure of the event's independent Chaos Level.

High and Severe non-trigger members require at least one other base-eligible member.

The trigger row is exempt from that support requirement.

A cluster with only one configured member is exempt from that support requirement.

Eligibility uses two passes to avoid circular support.

Pass one evaluates the trigger and every configured logical row against the ordinary event-system contract and the effective member minimum without applying the High or Severe support requirement.

Pass two applies the support requirement to High and Severe non-trigger rows using the pass-one base-eligible set.

The logical row count used by activation chance is the count of rows that remain eligible after the two-pass evaluation.

The severity corrections are:

| Event | Cluster role | Correct member severity |
| --- | --- | --- |
| Fury | Two logical members in Wars | Medium and High |
| Tensions Rising | Member in Diplomacy | Medium |
| Black Plague | Required member in Diseases | Severe |

## 3. Activation chance

Activation chance is rolled only for an eligible automatic trigger that belongs to an eligible cluster.

The activation tier bases are:

| Current tier | Player-facing tier | Base |
| --- | --- | ---: |
| T0 | Calm World | 5 |
| T1 | Gathering Storm | 10 |
| T2 | Rising Chaos | 15 |
| T3 | Chaos Tier | 25 |
| T4 | Totalen Chaos | 35 |
| T5 | World Collapse | 50 |

The trigger severity factors are:

| Trigger severity | Factor |
| --- | ---: |
| Low | 1.35 |
| Medium | 1.15 |
| High | 0.85 |
| Severe | 0.65 |

The eligible logical-count factors are:

| Eligible logical rows | Factor |
| --- | ---: |
| 1 | 1.40 |
| 2 | 1.30 |
| 3 | 1.20 |
| 4 | 1.10 |
| 5 or more | 1.00 |

Fatigue uses a score clamped to 0 through 4.

The fatigue factor is 0.90^score.

The previous optional-participation factor is:

| Previous optional participation ratio | Factor |
| --- | ---: |
| 25 percent or less | 1.40 |
| More than 25 percent through 50 percent | 1.30 |
| More than 50 percent through 75 percent | 1.15 |
| More than 75 percent | 1.00 |
| Zero optional denominator | Neutral factor 1.00 |

The previous ratio excludes the trigger and all required rows.

The previous ratio uses actually dispatched eligible optional rows from the last completed automatic batch.

The ratio denominator is the number of optional rows considered eligible in that batch.

When that denominator is zero, the previous-participation factor is neutral.

The activation formula is:

    activation_chance = clamp(round(base × trigger_severity_factor × eligible_count_factor × fatigue_factor × previous_participation_factor), 1, 90)

When the selected trigger event occupies more than one currently eligible logical row in the same cluster, its trigger-specific chance receives:

    multiplicity_factor = 1 + 0.15 × (eligible_matching_rows - 1)

The activation chance is multiplied by that factor and rounded again. Every extra eligible matching row guarantees at least one additional percentage point before the final 1 through 90 percent clamp, so every duplicate strengthens the cluster until the shared activation ceiling is reached.

Only currently eligible matching rows count, and the bonus never creates duplicate event dispatches.

When the selected event belongs to several fixed-member clusters, every cluster in which it owns a configured primary-trigger row evaluates eligibility and calculates and rolls its own final trigger-specific chance independently.

If no roll succeeds, the selected event continues through its ordinary standalone path.

If one roll succeeds, that cluster is selected.

If several rolls succeed, one successful cluster is selected uniformly at random.

Only the selected cluster commits successful activation memory, history, pacing, and cooldown state. A successful but unselected candidate remains unchanged, while a candidate whose valid roll failed receives the ordinary failed-roll fatigue reduction.

The displayed starting chance is the computed automatic activation chance before the activation roll.

An activation chance is never recomputed for a historical row.

Fatigue increases by one after a successful automatic cluster activation.

Fatigue decreases by one after a valid automatic activation roll fails.

Fatigue does not change for a gated attempt, a failed preflight, or a manual cluster force.

A valid failed roll proceeds through ordinary standalone handling for the selected trigger and does not apply cluster pacing or a cluster cooldown update.

## 3.1. Random Stuff special activation contract

Random Stuff is the retained memberless runtime cluster at ID 19, with runtime type `repeatable`, unlock tier 3, and no configured fixed-member rows.

Each successfully dispatched ordinary automatic minor event creates exactly one Random Stuff attempt after ordinary minor pacing has been applied.

The attempt is forbidden in manual event context, cluster-member context, Random Stuff bulk context, major-event handlers, below-tier state, disabled state, cooldown state, and when fewer additional events pass the authoritative event-system evaluator than the current tier's exact batch size: three at tier 3, four at tier 4, or five at the final tier.

The roll uses basis points with integer outcomes 1 through 10,000 and succeeds at or below the final basis-point chance.

| Current tier | Base basis points | Displayed base | Selected batch size |
| --- | ---: | ---: | ---: |
| T3 | 30 | 0.30 percent | 3 |
| T4 | 60 | 0.60 percent | 4 |
| T5 | 85 | 0.85 percent | 5 |

The drought bonus is 0.25 basis points per valid failed attempt and is rounded to whole basis points when the live chance is calculated.

The success factor is 1.00 before the first and second successes, 0.75 when two successes have already occurred, and 0.50 after three or more successes.

The final chance is rounded and has no special one-percent ceiling. It is bounded only by the 10,000-outcome roll scale, which represents the natural 100 percent probability limit.

A valid failed roll increments the drought count.

A successful automatic activation increments success count, resets drought to zero, records its chance and roll, and applies a 240-day cooldown.

Manual activation changes none of those automatic fields and applies no cooldown.

Random Stuff builds its candidate pool from every `global.all_events` entry accepted by `evaluate_random_event_selection_candidate` with the all-events filter, then excludes the minor event that opened the attempt.

Positive selectable weight remains an eligibility condition, but weight magnitude is not a sampling weight.

The sample is uniform without replacement and does not use event type, severity, ordinary selection weight, or fixed cluster membership.

The first selected event receives an immediate authoritative recheck and synchronous dispatch.

Only that successful first dispatch creates history.

Remaining selections enter the shared batch queue and receive another authoritative event-system recheck immediately before delayed dispatch.

Selected rows are guaranteed after eligibility and store role Random Draw, severity Not Used, the event's independent Chaos Level, 100 percent participation, final status, and canonical failure reason.

The opening ordinary minor event supplies the one pacing update for the overall incident.

Random Stuff members suppress their own pacing and recursion, so the bonus batch does not add another aggregate timer or major-weight update.

## 4. Optional member participation

The trigger row is guaranteed and fires first synchronously after ordinary eligibility succeeds.

Required rows are guaranteed after ordinary eligibility succeeds.

Optional rows are evaluated after the trigger and required rows.

Optional ordering uses a Chaos-tier severity bias:

| Current tier | Preserve Low to Severe bands |
| --- | ---: |
| Calm World | 90 percent |
| Gathering Storm | 88 percent |
| Rising Chaos | 86 percent |
| Chaos Tier | 84 percent |
| Totalen Chaos | 82 percent |
| World Collapse | 80 percent |

On the severity-biased path, rows follow Low, Medium, High, then Severe bands and are randomized within each band.

On the remaining path, the system uniformly selects one boundary between adjacent severity bands and swaps the two rows at that boundary. This guarantees one cross-severity inversion whenever at least two optional severity bands are present.

A batch with only one optional severity band has no valid boundary and remains randomized within that band.
Such batches are excluded from the cross-severity inversion denominator.

Participation rolls and their accepted-member decay use this resolved order, and accepted members dispatch in the same order.

The optional-member table is indexed by current Chaos tier and member severity.

| Current tier | Low | Medium | High | Severe |
| --- | ---: | ---: | ---: | ---: |
| Calm World | 70 | 35 | 15 | 5 |
| Gathering Storm | 80 | 40 | 20 | 10 |
| Rising Chaos | 90 | 45 | 25 | 15 |
| Chaos Tier | 95 | 50 | 30 | 20 |
| Totalen Chaos | 99 | 60 | 40 | 25 |
| World Collapse | 100 | 75 | 50 | 30 |

For each eligible optional row, the participation formula is:

    optional_member_chance = clamp(round(table_value × eligible_count_factor × 0.95^(accepted_optional_rows)), 1, 100)

accepted_optional_rows counts optional rows already accepted in the current cluster batch.

The decay exponent increments only after an optional row is accepted.

A rejected optional roll, an ineligible optional row, and a skipped invalidated row do not increment the decay exponent.

Required and trigger rows do not consume optional participation decay.

## 5. Stable rows, batches, and dispatch state

Every configured fixed member row has a stable logical row identity that remains distinct even when several rows use the same event ID.

Opening duplicate rows for Events 4, 6, 7, 9, and 13 have explicit primary trigger rows.

The primary trigger row is the first synchronous row for that activation, while later duplicate staged rows retain their own role, severity, declared minimum, chance, and status.

Every activation receives a batch identity that binds the cluster, trigger row, member rows, history context, and delayed dispatch context.

Queued state preserves the batch, cluster, logical row, trigger, history, and member runtime context needed to recheck and dispatch that exact row.

Delayed dispatch rechecks ordinary event-system fireability immediately before firing.

If a queued row fails that recheck, it is invalidated and recorded as skipped with N/A and the first canonical reason from the ordinary event-system resolver.

Invalidation never substitutes another event, another row, or another batch context.

Overlapping batches remain isolated by batch identity and aligned row context.

One batch cannot borrow a target, actor, event-specific context, history sequence, or staged payload from another batch.

Runtime state is versioned and non-destructive.

Runtime version 2 preserves stable semantic row IDs for pre-existing logical rows and assigns globally unique row IDs to every new logical row.

Cluster ID 3 retains the Diplomacy semantic identity formerly named Diplomatic Panic.

IDs 8 through 12 are semantically reassigned to Intelligence, Scientific Research, Negative Economy, Various Anomalies, and Pacts.

Diseases uses ID 13, and the memberless Random Stuff runtime cluster uses ID 19.

Legacy numeric IDs are migration inputs only and are not additional registered clusters.

The migration remaps persisted cluster-ID fields only when the complete legacy 1–12 registry sequence proves their old semantic meanings. It does not recompute historical member snapshots or replace queued row, batch, target, or event-specific context.

Settings navigation walks the current registry order and wraps between IDs 1 and 19 without visiting unregistered values.

Random Stuff has no fixed row registry.
Its history-only row identity combines the dynamic cluster row namespace with the selected event ID, while the batch and history sequence distinguish repeated selections across activations.

Adding or migrating batch fields must preserve prior successful history snapshots instead of rewriting them from current state.

## 5.1. Explicit state transitions

An automatic candidate transitions from ordinary-pool selection to ordinary event-system eligibility, then to complete fixed-cluster membership discovery, per-cluster gates, two-pass base eligibility, duplicate-row adjustment, and independent activation rolls.

A trigger rejected by ordinary event-system eligibility exits cluster evaluation before any cluster roll and continues through standalone handling.

A cluster-gated or preflight-failed attempt exits without changing automatic fatigue or previous-participation memory.

A valid failed activation roll transitions to ordinary standalone handling after decreasing fatigue by one and without applying cluster pacing or cooldown.

A single successful candidate, or one uniformly selected candidate when several rolls succeed, transitions to batch preparation, synchronous trigger dispatch, required-row eligibility and guaranteed dispatch, severity-biased optional rolls, delayed fireability rechecks, history snapshot commit, one pacing update, and one cooldown update.

An optional row transitions from base-eligible to accepted or rejected, and only an accepted optional row increments the current-batch decay count.

A queued row that fails its delayed recheck transitions to skipped and invalidated with N/A and its canonical reason.

A manual cluster force transitions from selected cluster to cluster-only gate bypass, equivalent event-system force-context checks, batch preparation, and dispatch without an activation roll or automatic-memory update.

## 6. Pacing, cooldown, and history

A successful cluster activation applies one cluster pacing update and one cluster cooldown update for the complete batch.

The number of member rows that dispatch does not multiply pacing or cooldown updates.

The cluster pacing path counts a repeatable or one-time cluster once for global timer compression and dynamic major-event gain.

A major cluster, when intentionally registered, uses its major pacing path once and resets major-event weights once.

Each dispatched member still applies its own ordinary fired-state, fire-once, repeatable recovery, and event-history behavior through the shared event handlers.

Automatic memory is separate from manual memory.

Manual activation records Manual and no roll for the activation chance and roll fields and does not modify fatigue or previous-participation memory.

Only a successful cluster activation creates a cluster history row.

The successful cluster history row snapshots the activation chance, activation roll, trigger, batch, tier, and actor or context fields that are valid for that activation.

Each member snapshot stores its chance, roll, role, severity, effective minimum, status, and canonical reason.

Guaranteed trigger and required rows store 100 percent and Guaranteed after eligibility succeeds.

Ineligible or invalidated rows store N/A for chance and roll fields and preserve their canonical reason.

Manual rows store Manual and no roll rather than a fabricated percentage.

A successful activation creates its history row before delayed members dispatch, so queued member status, canonical reason, final chance, and roll remain provisional until that batch settles.

After batch settlement, the historical snapshot is immutable and is never recomputed from current Chaos tier, fatigue, member definitions, event weights, or current event-system availability.

Normal member event history is recorded only when that member actually dispatches.

The separate cluster history row records the broad activation and its complete member result snapshot.

## 7. Event selection and manual behavior

Automatic selection first uses the ordinary active event pool.

The selected trigger must pass ordinary event-system eligibility before cluster lookup and activation chance evaluation.

If it belongs to a cluster, the cluster applies its own unlock, cooldown, enable state, two-pass member eligibility, and activation rules.

If the cluster roll fails, the selected trigger continues through ordinary standalone dispatch.

If the cluster activates, the trigger, required rows, and accepted optional rows use the batch dispatch order defined above.

Normal manual event firing continues to use the event-system manual or force context.

Manual cluster forcing starts from the selected cluster, bypasses only cluster-specific gates, and still evaluates every trigger and member through the equivalent event-system force context.

Manual cluster forcing has no activation roll and does not seed or consume automatic activation memory.

An event-system rejection blocks that trigger or member even when cluster-specific gates were bypassed.

## 8. Event Logs, catalog, and Settings contract

The Clusters tab lists the registered cluster catalogue, while History lists only successful cluster activations.

The cluster catalogue and the Settings activation summary use the exact copy Varies by member whenever a single cluster-level chance cannot represent all member rows.

Cluster details expose the member role, member severity, effective member minimum, ordinary event-system availability, and starting chance.

Unique event details show the current trigger-specific activation chance.

Duplicate staged IDs show Varies by row because one event ID can represent several logical member rows.

By Roll is the live automatic-pool-weighted mean of distinct eligible trigger events.

The weighted mean is:

    by_roll = sum(trigger_event_weight × trigger_activation_chance) / sum(trigger_event_weight)

The mean uses only distinct trigger events that are eligible in the current automatic pool and have positive live event-system weight.

Unavailable rows and rows with zero live weight display N/A instead of zero for the roll or activation field.

The cluster sort modes include By Cluster ID, By Type, By Roll, By Unlock Tier, By Member Count, and By Fired.

Sort order remains Ascending or Descending.

Cluster history rows open immutable historical details, while catalogue rows open current details.

The current detail view may show current availability and current starting chance.

The historical detail view shows the saved snapshot and does not recompute it.

Clicking a member row opens the member event's ordinary details without replacing the cluster batch or historical context.

Settings may force a selected cluster through its manual path, but the result remains subject to the event-system force context for every dispatched trigger and member.

No new visual assets are required.

Existing Event Logs and Settings sprites, buttons, checkboxes, fonts, and flag surfaces remain the visual surface.

## 9. Registered cluster families

The v2 catalogue preserves cluster IDs as semantic IDs and defines these fixed cluster rows.

| Cluster ID | Canonical name | Catalogue type | Catalogue Chaos level |
| --- | --- | --- | ---: |
| 1 | Wars | Minor Repeatable | 1 |
| 2 | Liberations | Minor Repeatable | 1 |
| 3 | Diplomacy | Minor Repeatable | 1 |
| 4 | Peace | Minor Repeatable | 1 |
| 5 | Natural Disasters | Minor Repeatable | 1 |
| 6 | Formables | Minor Repeatable | 3 |
| 7 | Positive Economy | Minor Repeatable | 1 |
| 8 | Intelligence | Minor Fire-Once | 1 |
| 9 | Scientific Research | Minor Fire-Once | 2 |
| 10 | Negative Economy | Minor Fire-Once | 2 |
| 11 | Various Anomalies | Minor Fire-Once | 4 |
| 12 | Pacts | Minor Fire-Once | 3 |
| 13 | Diseases | Minor Repeatable | 1 |
| 14 | Randomizations | Minor Repeatable | 1 |
| 15 | Sudden Abundance | Minor Repeatable | 1 |
| 16 | Domestic Unrest | Minor Repeatable | 1 |
| 17 | Alien Invasions | Minor Fire-Once | 1 |
| 18 | Military Preparation | Minor Repeatable | 1 |

The exact catalogue details, member ID lists, member severities, statuses, and all 75 logical membership rows are maintained in [event_clusters.md](event_clusters.md).

The memberless Random Stuff runtime cluster remains at ID 19 and is not part of the 18 fixed catalogue rows.

Cluster IDs 8 through 12 therefore refer to their v2 semantic assignments, Diseases refers to ID 13, and Random Stuff refers to ID 19.

The first logical rows for Events 4, 6, 7, 9, and 13 are the explicit primary trigger rows for their respective duplicate groups.

The member registry remains the authority for each row's declared minimum, role, and current event mapping.

The effective minimum and severity rules in this contract apply to every registered and future row.

## 10. Worked examples

### Low-severity small-cluster activation

Suppose the current tier is T0 Calm World, the selected trigger has Low severity, two logical rows are eligible after the two-pass check, fatigue is zero, and the previous automatic batch had 20 percent optional participation.

The factors are base 5, trigger severity 1.35, eligible count 1.30, fatigue 1.00, and previous participation 1.40.

    round(5 × 1.35 × 1.30 × 1.00 × 1.40) = round(12.285) = 12

The activation chance is 12 percent after the 1 through 90 clamp.

The Low-severity optional row uses the Calm World table value 70.

With no accepted optional row yet, its participation chance is round(70 × 1.30 × 0.95^0) = 91 percent after the 1 through 100 clamp.

The trigger dispatches first and synchronously, and the required row dispatches next after it passes ordinary fireability.

### Optional decay

In the same batch, if the first optional row was accepted, the accepted optional count becomes one before the next optional row is evaluated.

A Medium-severity optional row at Calm World uses table value 35 and the same two-row count factor of 1.30.

    round(35 × 1.30 × 0.95^1) = round(43.225) = 43

The second row therefore has a 43 percent participation chance.

If the first optional row was rejected or invalidated, the accepted count remains zero and the second row uses round(35 × 1.30) = 46 percent.

### High-severity support

Suppose a High-severity optional row passes the ordinary event-system check and its effective minimum, but no other configured row is base-eligible in pass one.

The row is removed in pass two because it lacks another base-eligible member.

The trigger is still eligible and may continue through an ordinary standalone event path when no cluster activation occurs.

## 11. Acceptance scenarios

1. An eligible automatic trigger reaches cluster evaluation, receives the formula result, and records the activation roll without changing ordinary event eligibility.
2. A trigger rejected by the event system does not roll its cluster and continues through ordinary standalone handling.
3. A required row receives 100 percent and Guaranteed only after ordinary eligibility succeeds.
4. A High or Severe non-trigger row requires another pass-one base-eligible row, while the trigger and a sole configured member remain exempt.
5. A duplicate Event 4, 6, 7, 9, or 13 group identifies one stable primary trigger row and preserves every additional logical row with its own severity and participation roll.
6. Optional rows use the tier and severity table, apply the eligible-count factor, and increment decay only after accepted optional dispatch.
   Their evaluation order preserves severity bands at the tier's 80 through 90 percent bias and otherwise permits cross-severity inversions.
7. A valid failed automatic roll decreases fatigue by one, while a gated attempt, failed preflight, or manual force leaves fatigue unchanged.
8. A successful automatic activation increases fatigue by one, updates pacing and cooldown once, and records the previous-participation source only after the batch completes.
9. A delayed row that becomes invalid is skipped with N/A and its canonical reason without borrowing another batch's context.
10. Overlapping batches retain separate cluster, batch, row, trigger, history, and event-specific contexts.
11. Manual cluster forcing bypasses cluster-only gates but cannot dispatch an event rejected by the equivalent event-system force context.
12. Historical activation and member values remain unchanged when current tier, weights, definitions, availability, or fatigue later change.
13. The catalog and Settings activation copy use Varies by member, duplicate staged event details use Varies by row, and unique event details show the current trigger-specific chance.
14. By Roll uses the live automatic-pool-weighted mean of distinct eligible trigger events and returns N/A for unavailable or zero-weight rows.
15. By Unlock Tier and By Member Count sort the registered cluster catalogue with stable tie handling.
16. Fury has Medium and High logical rows, Tensions Rising is Medium, and Black Plague is Severe in every cluster-facing presentation.
17. Event Chaos Level assignments remain unchanged, the Events sheet lists all distinct cluster IDs, and member severity remains row-specific on cluster sheets.
18. The event-log and Settings surfaces reuse existing assets without a new visual asset requirement.
19. Two or more eligible rows carrying the selected event in one cluster increase that cluster's final trigger-specific chance through the multiplicity factor and shared activation ceiling without dispatching the primary trigger twice.
20. An event mapped to several clusters rolls every eligible cluster independently, activates no more than one, and selects uniformly among simultaneous successes.

## 12. Artifact ownership and external validation

The runtime implementation artifacts are common/script_constants/event_cluster_constants.txt, common/scripted_effects/chaosx_event_cluster_effects.txt, common/scripted_effects/chaosx_events_log_effects.txt, common/scripted_effects/chaosx_logic_effects.txt, common/scripted_effects/chaosx_settings_effects.txt, common/scripted_guis/chaosx_scripted_gui_events_log.txt, common/scripted_localisation/chaosx_scripted_localisation_events_log.txt, common/scripted_localisation/chaosx_scripted_localisation_settings.txt, interface/chaosx_events_log_popup.gui, and localisation/english/chaosx_gui_l_english.yml.

This document and event_clusters.md define the documentation contract for those artifacts.

events_log_window.md, events_log_evolutions_and_clusters.md, event_chaos_levels.md, and dynamic_major_event_weights.md define the linked Event Logs, Chaos Level, selection, and pacing surfaces.

No new visual asset is part of this overhaul.

The 2026-09-05 shared-event curator's read-only `hoi4.probability_inspect` call exposed the `custom_weighted_pool` adapter name and returned `PROBABILITY_SOURCE_INSPECTED` for `common/scripted_effects/chaosx_event_cluster_effects.txt` with `poolComplete=false`, zero candidates, zero unresolved inputs, and `availableAdapters=[]`.

The source revision is `1d86199a66e9a4a08cd1700a3c48898b408e33865ddb07936e2fead6591a86c9`, the source hash is `4a7b9de6b059a75ce473dcb5e69cbcbfc95c5cc666106713cc201ac500d21865`, and the artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1fabbbfcac38825b8b39d3ef539f39c1d9b49c7b5f891e59f580a9cc32837c0f/fde0dd32884edc99b6b3fba386f6a73cc59bbaefaa0099760e305c8479c17fd5/probability-inspect-4a7b9de6b059.json`.

This source-discovery result does not provide candidate evaluation, sweep, seeded simulation, sequence analysis, comparison, or weighted-behavior acceptance.

The required narrow read-only `hoi4_event_inspect` query for `chaosx.nr12.1` was attempted with `mode=scan`, `maxDepth=1`, `maxEdges=20`, and `maxNodes=20`, but the MCP operation stalled before returning a result in that probe. Earlier partial artifacts in package handoffs remain historical evidence and are not re-certified here.

The required narrow read-only `hoi4_gui_inspect` query for `events_log_popup_window` with scenario `event_log_shared_architecture_baseline` was attempted in the same pass but stalled before returning a result. Existing GUI artifacts are retained as historical evidence, while current engine and branch-specific visual acceptance remain unresolved.

Source review, static checks, MCP artifacts, and user-owned live-game validation remain separate evidence classes.

## Completion checklist

- [x] Ordinary event-system eligibility remains authoritative for automatic, required, optional, and delayed dispatch, while manual cluster force matches the existing single-event force context and remains subject to dispatcher rejection.
- [x] Trigger rejection skips cluster rolling and continues ordinary standalone handling.
- [x] Required rows are guaranteed only after eligibility and never bypass fireability.
- [x] Severity floors, declared minimums, two-pass support, trigger exemption, and sole-member exemption are implemented.
- [x] Activation bases, factors, fatigue, previous-participation ratio, rounding, and clamps match this contract.
- [x] Optional table values, accepted-row decay, ordering, and guaranteed dispatch match this contract.
- [x] Stable logical rows, primary duplicate trigger rows, batch state, delayed rechecks, invalidation, overlapping-batch isolation, and versioned history are implemented.
- [x] Successful cluster pacing and cooldown update exactly once, and manual memory remains isolated.
- [x] Successful history snapshots include activation and member fields without recomputation, and delayed invalidation settles chance and roll to N/A sentinels.
- [x] Event Logs and Settings expose the required chance, availability, role, severity, effective minimum, sort, and N/A behavior in source.
- [x] Fury, Tensions Rising, and Black Plague use the corrected cluster-row severities.
- [x] The Events sheet lists every distinct cluster ID and leaves severity to the Clusters and Cluster Memberships sheets.
- [x] No new visual assets are requested or required.
- [x] MCP evidence limits and the absence of accepted engine evidence are recorded.
- [ ] Probability inspect, evaluate, sweeps, seeded simulation, sequence analysis, and before/after comparison produce accepted MCP artifacts.
- [ ] Event inspect, render, and comparison produce accepted MCP artifacts.
- [ ] Event Log catalogue, current detail, automatic history, and manual history pass GUI inspect/render at 1920 by 1080 and 1366 by 768.
