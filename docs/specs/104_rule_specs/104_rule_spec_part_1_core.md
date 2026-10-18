# Event 104: Rule

## The campaign experience

One of the campaign's actual game rules changes while the world is already running.
The player receives a report naming the rule, its previous setting, and its new setting.
The change applies to the shared world immediately and survives the report, subsequent events, and saving and loading.
The player continues the same campaign with different permissions, restrictions, or behaviour in the systems governed by that rule.

The first few firings should be easy to follow.
One diplomatic assumption changes, then another campaign system changes later.
The player learns the consequences through the ordinary diplomatic, political, military, and country interfaces where those rules operate.
At higher Chaos, several rules can change in one firing and previously altered rules can be revised again.
The resulting campaign should acquire its own recognisable, accidental rule set.

The player does not select the rule, choose the destination setting, pay to veto the result, or receive a compensating bonus.
Their agency comes from changing their campaign strategy after a real rule changes.
A restrictive result can close an approach they were using.
A permissive result can create a useful opening for them, their allies, or their enemies.
Both are legitimate outcomes.

## Event identity

| Field | Specification |
| --- | --- |
| Event ID | 104 |
| Event name | Rule |
| Type | Minor Repeatable |
| Requested catalog status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Randomizations |
| Cluster role | Medium member |
| Primary entry convention | `chaosx.nr104.1` |
| Companion concept | Event 105, Random Idea |

The user explicitly accepted uploaded planning IDs 104 Rule and companion 105 Random Idea on 10 October 2026.
The current workbook retains its old numbering, with migration accepted and queued for later authorized catalog work.
The user released legacy Rule 107 for Lootboxes 107 on 10 October 2026. Rule keeps planning ID 104, and legacy Random Idea 110 remains held.
The proposed numerical tuning and expanded behaviour in this package are design decisions made under the request to produce full specifications.
They are ready for review and implementation planning.
They are not claims that this event already exists or has passed engine validation.

## What counts as a rule change

A Rule outcome changes the option of an existing, identified game rule in the native game-rule state.
The relevant native reader must report the selected option after the change.
At least one current campaign consumer must then behave differently because of that option.
The changed option must remain effective after save and reload and must have the same authoritative value for all multiplayer participants.

The package does not certify a native runtime writer.
That is a blocking implementation question, described in `104_rule_native_feasibility.md`.
An event-owned variable, a national spirit, a country permission override, a forced diplomatic action, or an edited save does not satisfy this definition by itself.
Those mechanisms cannot be presented as a completed implementation of the requested native rule change.

The distinction matters because a rule can exist in the setup menu without being useful during a running campaign.
A setting that only changed the initial map has already done its work.
A setting that is still read when countries request a diplomatic action can have a continuing purpose.
Every admitted rule needs evidence for its own consumer and destination options.
The presence of a rule name or a reader alone is insufficient.

## Default, current setting, and campaign start

The **default setting** is the canonical default option in the effective rule definition loaded by the current game and mod combination.
The **current setting** is the option actually active immediately before this firing commits its change.
The **campaign-start setting** is whatever the player selected when starting the campaign.
These are separate facts.

Every destination must differ from both the canonical default and the current setting.
This requirement applies to every evolution, including Rule Revisions and No Stable Rulebook.
A player-selected non-default setting may therefore change to a different non-default setting if the rule is otherwise eligible.
The event cannot assume that an untouched rule is currently at its default.

When a rule has only a default and one non-default option, changing it to that sole alternative exhausts its Event 104 destinations.
Evolution II does not create another valid option.
The rule becomes selectable again only if its actual current state later changes in a way that restores a valid non-default destination.
Rules with two or more distinct non-default options provide the long-term revision potential required by the later evolutions.

## Baseline firing

The baseline changes one eligible rule.
Eligibility is evaluated against the current world, the effective rule definitions, enabled content, prior Event 104 ownership, and the available destination options.
The picker first selects a rule with equal probability within the active eligibility stratum, then selects one eligible destination for that rule with equal probability.
The baseline has one fresh-rule stratum, while later evolutions can apply the category and recency priorities defined in Parts 2 and 3.
A rule with six possible destinations does not receive six times the selection chance of a rule with one.

Before Evolution II or IV grants revision permission, a rule successfully changed by Event 104 cannot be selected again.
The event records this ownership only after a verified material change.
A rejected candidate, failed write, or identical readback does not mark a rule as changed.
Later firings therefore accumulate different rules until the fresh pool is exhausted or a revision evolution becomes active.

The current rule is rechecked at the point of application.
If another authoritative system has changed it since eligibility was prepared, the event rebuilds that candidate's valid destinations from the current value.
It never applies a stale selection merely because an earlier tooltip or preparation step expected a different value.

## The report and acknowledgement

A successful firing produces one occurrence report for each relevant human recipient through the ordinary event presentation.
The report explains that campaign rules have changed and shows the actual committed rule transitions.
For each changed rule, it identifies the previous setting, new setting, and the practical class of action or behaviour affected.
The report's acknowledgement performs no additional mutation.
Closing it cannot reroll, delay, accept, refuse, or repeat the result.

The report refers to the immutable result of its own firing.
If a later Rule event changes the same rule before the player reads the earlier report, the earlier report continues to describe the earlier transition.
Ordinary gameplay interfaces show the currently active rules.
The existing event history retains the sequence of earlier outcomes.

No government is presented as the culprit merely because it served as the technical event executor.
Rule is a change in the world's operating conditions.
Country-specific AI rule changes may name the affected country, but that country is the subject of the rule, not an invented author of it.

## Meaningful changes

A destination is meaningful when a supported current consumer has a real, reachable behavioural difference under that destination.
The difference can affect an available action, an action's prerequisites, an AI decision that can still be taken, or another continuing campaign mechanic.
The event does not require the player to be the country affected.
An AI-only change can qualify when that AI country exists and has a genuinely reachable alternative behaviour.

Eligibility uses a documented witness for that difference.
For a diplomatic permission, this is a current actor and target whose applicable rule gate changes while the required non-rule conditions are satisfied.
For an AI route, this is an existing AI country with an uncommitted, reachable branch whose selection actually consumes the setting.
For a continuing construction restriction, this would require a current, legal construction opportunity that the new setting changes and verified behaviour for existing construction.
The rule pool specifies the required witnesses and exclusions.

A label change without a behavioural difference is not a result.
Two options that currently produce the same behaviour for all relevant consumers do not provide a valid transition in that world state.
If a permissive rule remains masked by an independent embargo, ideology restriction, missing target, or completed route, that masked relationship does not count as the witness.
Another unmasked relationship may still make the same rule eligible.

## Persistent ownership and outside changes

Successful Event 104 changes remain active without a duration.
Rule does not periodically restore or reapply them.
The authoritative current value always comes from the real game rule.
The event's persistent records explain what Rule changed and which settings it has used.
Those records do not override newer changes made by another legitimate campaign system.

Disabling future Rule firings leaves already changed rules in force.
Disabling an evolution affects future use of that evolution's capability and does not undo changes already committed.
Falling below a Chaos threshold does not revoke an already unlocked evolution.
The size of a later cascade can still decrease because it reads the current Chaos value.

An externally restored default is not silently converted back to the old Rule result.
The rule remains historically touched by Event 104.
Before revision permission, that historical ownership keeps it out of the fresh pool.
After revision permission, its actual restored state may give it a valid destination again.
External changes do not earn Event 104 achievements, first-change credit, or Chaos awards.

## Repeatable pacing

Rule uses the shared Minor Repeatable firing, recovery, cap, and timer framework.
It does not introduce a second occurrence timer or special player-controlled reroll.
A successful cascade is one Event 104 occurrence regardless of how many rules it changes.
Its occurrence weight and pacing are charged once.
Each changed rule is included in the occurrence's result record.

The framework inspected at the original planning cutoff gave Repeatable events an initial weight of 1000, monthly recovery of 20, and a cap that halves with successful occurrences.
Those are framework values, not an Event 104 probability guarantee.
The event's actual chance of selection depends on the full active event pool and its state.
The implementation must preserve the current shared behaviour unless an independently accepted framework change supersedes it.

## Empty pools and shortened cascades

An empty eligible pool is a valid campaign condition.
It can result from accumulated changes, a lack of revisable options, absent countries, completed AI branches, or current restrictions that mask every possible effect.
Automatic selection treats Rule as temporarily ineligible.
It does not consume an occurrence, reduce its cap, advance Minor pacing, record a successful event, or grant Chaos.
Normal pool evaluation can make it eligible again when the world changes.

If a multi-rule firing finds fewer compatible, meaningful rules than its requested count, it changes the available rules without repeating a rule within the same batch.
The report gives the actual number changed.
The event does not pad the count with cosmetic, protected, ineffective, or default destinations.

Application is best effort over a bounded selection of distinct rules.
Verified successful changes persist even if another selected rule fails.
A batch with at least one verified change is one successful occurrence.
A batch with zero verified changes is rejected before normal successful-firing accounting.
The implementation must prove that a failed write cannot leave an unobserved native mutation behind.
An ambiguous write stops further mutations, preserves the evidence, and places Rule in the runtime quarantine defined in Part 2.
It is a release blocker rather than a harmless skipped candidate.

## The four evolutions

| Evolution | Chaos requirement | Distinct change |
| --- | ---: | --- |
| I: Another Rule | 200+ | Some firings change a second fresh rule. |
| II: Rule Revisions | 400+ | Previously changed rules can be selected again when another valid non-default option exists. |
| III: Rule Cascade | 600+ | The requested batch expands with current Chaos and remains bounded by compatibility and availability. |
| IV: No Stable Rulebook | 800+ | Larger batches deliberately mix fresh changes with a substantial random share of the revisable altered set. |

The full timing, count, selection, and toggle contracts are in Part 3.
Evolution activation itself changes the event's capabilities and awards zero Chaos.
It does not create an unrequested free Rule firing.
The next successful occurrence uses the newly active capability immediately.

## How the campaign responds

The new setting governs future actions through the actual native rule and its verified consumers.
Rule does not automatically declare wars, dissolve factions, recall volunteers, cancel shipments, redo national focuses, reverse completed treaties, or replay startup scripts merely to make the report dramatic.
Any immediate effect on an existing arrangement must be the verified behaviour of that particular native rule and must be documented before the transition is admitted.

Ongoing diplomatic tasks, partition negotiations, and warlord campaigns must check currently active permissions at meaningful action boundaries.
If their required action becomes illegal, their owning system gives the task a clear blocked, revised, or cancelled outcome according to Part 4.
They cannot retain a stale preview that promises a now-impossible action.

Random Idea remains an independent companion event.
Its country ideas can combine with Rule's global settings, and the ordinary game's actual precedence determines the result.
Neither event rerolls or repairs the other simply because their effects produce an inconvenient combination.

## Completion standard

The implemented contract must support an identifiable actual rule transition, its current gameplay effect, persistence through save and reload, and later firings under the correct accumulated state.
Review the relevant installed references, source, and representative checks to establish support and report the limits of unobserved game behaviour.
The user owns live-game validation, which agents neither request nor await as a delivery gate.
All four evolutions must have meaningful supported behaviours in the base-game configuration as well as supported DLC combinations.
If the native writer or a sufficiently rich base-game rule pool cannot be demonstrated, the full design remains blocked for implementation.
The intended mechanic must stay intact in the specification and the blocker must stay visible in the handoff.
