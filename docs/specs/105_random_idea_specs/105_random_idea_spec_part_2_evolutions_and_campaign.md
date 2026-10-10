# 105 Random Idea: evolutions and campaign behavior

## Evolution ladder

Each firing uses the highest enabled stage supported by the Chaos value captured at the start of that firing.
The stage sets a total requested draw count for each country.
The event does not add the earlier stages' counts together.

| Chaos at firing | Stage | Requested ideas per country |
| --- | --- | --- |
| 0–199 | Baseline | Exactly 1 |
| 200–399 | Evolution I: Double Draw | Exactly 2 |
| 400–599 | Evolution II: Three of a Kind | Exactly 3 |
| 600–799 | Evolution III: Idea Collision | Uniformly 4, 5, or 6 |
| 800+ | Evolution IV: Idea Storm | A variable bundle using current Chaos and the country's existing Event 105 burden |

The exact one, two, and three counts preserve the user brief.
The four-through-six range and the Storm tuning below are concrete design decisions made for this specification under the requested expansion.
Every count remains subject to genuine fresh-pool exhaustion and the selected definitions' normal behavior.

Player-facing Chaos level 1 means the starting level, corresponding to the engine framework's zero-based initial tier.
It does not postpone the baseline until 200 Chaos.
The inspected repository explicitly distinguishes these one-based display levels from its zero-based stored tier IDs.
The supporting source is recorded in the technical handoff.

## Evolution I: Double Draw

At 200 Chaos or above, each recipient draws two identities independently from its own fresh pool, without repeating an identity within the bundle.
The second result is not selected to complement or oppose the first.
Both results can be beneficial, both harmful, both inert in that country, or unrelated in every ordinary sense.

The two direct identities are different whenever at least two eligible identities remain available to dispatch.
Native replacement can leave fewer than two new retained ideas.
This is reported as a consequence of the ideas' own behavior and does not trigger a third compensating draw.

## Evolution II: Three of a Kind

At 400 Chaos or above, each recipient requests three distinct direct identities.
The evolution's supplied name does not introduce three matching families, three copies of one spirit, a shared category, or a bonus for a themed set.
Military, economic, political, scientific, hidden, and highly specific national ideas stay in one flat eligible universe.

The result can create a recognizable combination by chance.
The event does not recognize that combination as a new recipe or award a separate synergy modifier.
Any synergy comes from the normal effects already defined in the loaded game.

## Evolution III: Idea Collision

At 600 Chaos or above, each country first rolls its own count from four, five, and six, with equal probability for each count.
It then makes that many fresh identity selections using the ordinary uniform draw rules.
One country's count does not affect another's count.

This stage increases uncertainty in both quantity and composition.
A powerful spirit does not reduce the number of later draws, and a penalty does not earn an extra draw.
Existing Event 105 burden does not reduce this stage's count, preserving a clear progression from the user's fixed lower stages.

## Evolution IV: Idea Storm

At 800 Chaos or above, the event gives lightly burdened countries a large variable bundle.
The count grows in hundred-point Chaos steps and decreases as the recipient already carries more directly drawn Event 105 identities.
This adjustment changes quantity only.
It never changes which eligible national ideas may be selected.

Define the firing inputs as follows.

| Symbol | Meaning |
| --- | --- |
| C | Global Chaos captured before this firing produces any effects |
| B | The number of distinct previously dispatched Event 105 identities that this recipient currently holds, captured before any country receives this firing's grants |
| S | The nominal Storm intensity before burden adjustment |
| T | The burden-adjusted center of the count range |
| K | This country's requested number of direct draws |

The accepted tuning is:

S = 8 + floor((min(C, 1600) − 800) / 100)

T = max(5, ceil(24 × S / (24 + B)))

K is a uniform whole-number draw from T − 1 through min(16, T + 2), including both endpoints.

These equations are used only for the 800+ stage.
The 1600 ceiling limits further growth in one firing's intensity.
The 16 limit applies to one requested bundle, not to a country's total ideas or the size of the loaded pool.
The constant 24 makes the burden adjustment gradual enough to preserve meaningful differences between lightly and heavily affected countries.

| Existing burden B | 800 Chaos | 1000 Chaos | 1200 Chaos | 1600+ Chaos |
| --- | --- | --- | --- | --- |
| 0 | 7–10 | 9–12 | 11–14 | 15–16 |
| 6 | 6–9 | 7–10 | 9–12 | 12–15 |
| 12 | 5–8 | 6–9 | 7–10 | 10–13 |
| 24 | 4–7 | 4–7 | 5–8 | 7–10 |
| 48 | 4–7 | 4–7 | 4–7 | 5–8 |
| 96 | 4–7 | 4–7 | 4–7 | 4–7 |

The table shows requested direct draws before pool exhaustion or native lifecycle effects.
Every integer in a displayed range has equal probability.
For a country with B = 0, the expected requested counts at the four listed Chaos values are 8.5, 10.5, 12.5, and 15.5.
At the minimum Storm range of four through seven, the expected count is 5.5.
These are properties of the specified mathematical model, not measured engine probabilities.

At fixed burden, increasing Chaos never lowers the requested-count distribution.
At fixed Chaos, increasing burden never raises it.
An individual later roll can still be smaller because each firing makes new random selections.
The minimum Storm range of four through seven preserves progression from Collision's four through six even for heavily burdened countries.

The event deliberately permits further accumulation at high burden.
It has no hard total-spirit cap and does not erase old ideas to make room.
Duplicate prevention stops repeated exact identities from becoming a wall of repeated grants, while quantity damping slows growth for heavily affected countries.
The remaining finite pool and each idea's own lifecycle can also reduce retained growth, but the design does not assume they will always do so.

## What burden measures

Keep a historical record of exact identities directly dispatched by Event 105 to a country.
At the next firing, count the intersection of that history with the country's currently held ideas.
An exact identity contributes at most one to B.

| Situation | Contribution to B |
| --- | --- |
| An idea was already owned and was therefore skipped by Event 105 | None from that skipped draw |
| Event 105 directly dispatched an idea and the country still holds it | One |
| Event 105 directly dispatched an idea that has since disappeared | Zero while absent |
| That previously drawn exact identity later returns through another native source | One while present, because it is a currently held identity with prior direct-draw history |
| A selected idea's callback grants a different idea indirectly | No automatic direct-draw credit for the indirect identity |
| A native replacement changes one selected identifier into another | The old identifier stops contributing when absent, and the replacement needs its own direct-draw history to contribute |
| Two identifiers have the same display name or icon | Count separately if both satisfy the rule |
| The idea is hidden or empty but remains held | One |

This is an explicit identity-based burden measure.
It does not claim continuous ownership, exclusive causal attribution, or a measurement of the idea's strength.
Recording every newly observed ownership difference as an Event 105 grant would misattribute native callbacks and other events, so that method is not allowed.

Capture B for every roster member before the first grant anywhere in the firing.
This keeps an earlier country's callbacks from changing a later country's requested bundle size.
Current ownership still changes eligibility between individual draws, since the event should not add a now-held identity.

An inherited or recreated country does not gain invented direct-draw history.
Existing history follows a country only where the native country scope and the project's continuity mapping establish that it is the same country.
The implementation must preserve stable identity through save and registry changes rather than trusting an old dense array index.

## Entry timing and settings

These are evolved openings for an instantaneous repeatable event.
There is no active Event 105 crisis waiting for a delayed evolution roll after its grants finish.
A first firing at 650 Chaos uses Idea Collision immediately, and a first firing at 950 uses Idea Storm immediately.
An earlier firing at 150 does not retroactively issue another idea when Chaos reaches 200 later.

The next legitimate firing uses the current captured Chaos and the highest permitted stage.
If Chaos has fallen, the next firing can use a lower stage.
Previously retained ideas remain unchanged.
Historical evolution records remain history, and they must not turn the previous maximum stage into a permanent quantity override.

If the established settings disable evolutions, use the baseline count.
If the established settings support individual stage control, use the highest enabled stage whose threshold is met.
Do not add a new Event 105 settings panel merely to expose extra combinations of switches.
A settings change or an evolution preview must not dispatch ideas, reset prior receipts, or award Chaos.
Freeze the effective stage before the first native dispatch, so a setting changed by a callback affects a later firing rather than later recipients in the current firing.

The same one-firing contract applies when a legitimate cluster invocation reaches Event 105.
It resolves once for that invocation and then allows the cluster to continue its own member sequence.
It does not run once per cluster viewer, report acknowledgement, participating human, or history refresh.

## Evolution history

The normal event history records every legitimate firing through the existing repeatable-event framework.
The separate evolution history records the first use of each actually dispatched evolution stage at most once per campaign.
A stage is used when at least one technically preflighted native dispatch is issued under that stage during a ready firing, with its observed or unresolved outcome kept honest in the firing record.
A preview, a settings change, an empty fresh pool for every recipient, or a technical failure before any dispatch begins does not mark the stage used.

A first firing at Idea Storm records Evolution IV only.
It does not fabricate earlier Double Draw, Three of a Kind, or Idea Collision occurrences.
If one of those lower stages is actually used in a later lower-Chaos firing, its own first-use record may then appear at that real date.
Repeated use of an already recorded stage receives only the ordinary firing record and its captured stage, without duplicate evolution-history entries.
The four first-use receipts preserve history and have no effect on future count selection or Chaos awards.

## Chaos impact map

The concrete abnormal outcome is the retention of newly assigned national identities across the world.
Use one global contribution settled after the firing's immediate native effects, without multiplying a full event award by the number of recipients.
This keeps a loadout with many countries from receiving an arbitrarily larger Chaos jump solely because it contains more tags.

Let N be the number of valid countries in the captured roster.
For each country, let R be the number of its fresh directly dispatched identities from this firing that are actually held at immediate settlement.
Count an identity once, and cap each country's contribution to the aggregate at ten.
Let A be the sum of these capped retained counts across the roster.

If N is zero or A is zero, Event 105 adds zero Chaos.
Otherwise its contribution is ceil(2 × A / N), with a maximum of 20.
The implementation must use the existing central Chaos-writing helper and source attribution, rather than a second meter.

| Milestone or outcome | Reason for Chaos change | Direction and starting magnitude | Dynamic factors | Repeat guard | Shared-source overlap | Reversal counterpart |
| --- | --- | --- | --- | --- | --- | --- |
| A firing leaves fresh directly drawn ideas in the world | Unrelated national conditions have materially become part of recipient countries | Positive, 1–20 from the aggregate formula | Actual retained identities and actual recipient roster | One settled contribution per firing identity | Pays for the anomalous assignment itself, not subsequent wars, deaths, territorial changes, or the selected idea's separate systems | Native later loss does not refund this historical anomaly |
| The baseline leaves exactly one fresh idea in every roster country | Worldwide initial manifestation | +2, as a consequence of the same formula | For a nonempty roster, +1 when 0 < A ≤ N/2 and +2 when N/2 < A ≤ N, with zero when A = 0 | Same firing guard | No additional baseline bonus | None |
| An evolved firing leaves a larger retained bundle | More unrelated national conditions coexist | Same formula, never an extra evolution award | Actual retained count, capped contribution of ten per country | Same firing guard | Does not stack with a separate stage-activation award | None |
| Pool exhaustion, technical non-dispatch, or only self-removing results leave A = 0 | No retained direct outcome has been established by this meter's observation rule | Zero | None | A zero result is still settled once | Any native callback's separately owned effects remain with their own system | None |
| Evolution eligibility, stage selection, settings change, report viewing, history refresh, or achievement unlock | No new national-idea outcome has occurred | Zero | None | These surfaces cannot call the outcome award | No duplicate general event bonus | None |
| A selected idea later creates a war, death, release, coup, or another system outcome | That consequence has its own normal owner | Zero additional Event 105 award | Existing shared rules apply independently | Event 105 does not monitor or repeat that owner's award | Preserve the existing shared source | Its existing system owns any reversal |

For example, ten valid recipients retaining one idea each produce +2.
Ten recipients retaining three each produce +6.
Ten recipients retaining ten or more each produce the capped +20.
If only one of those ten recipients retains one idea, the contribution is +1.

The meter intentionally uses an observed ownership outcome rather than pretending to observe every transient callback effect.
An idea that replaces itself immediately can therefore consume a valid direct draw while contributing zero to Event 105's retained-identity count.
Save this end-of-firing observation for both the Chaos award and the report's retention labels.
Later native changes do not rewrite the saved report outcome.
This limited observation must remain explicit in diagnostics.
It must not cause a callback retry or a hidden blacklist.

There is no Event 105 negative award for later spirit removal, because the event does not own the native removal and offers no containment action.
Repeated real firings may create new anomaly awards, while the same firing's acknowledgement, reload continuation, or duplicate callback may not award twice.
Diagnostic-only firings must follow the project's existing test-context exclusion for progression and achievements.
A player has no Event 105 action with which to purchase, remove, and redraw ideas for Chaos credit.

## Connection to Event 104: Rule

Random Idea and Rule can coexist through the rules and ideas they normally apply.
One changes the campaign's rules while the other adds unrelated national conditions to each country.
Neither event requires the other, schedules the other, modifies the other's pool, or supplies an extra combined reward.

If Rule changes an engine condition that affects an idea's normal behavior, allow that behavior to operate normally.
Event 105 does not reject the idea because Rule makes the result awkward, ineffective, or surprising.
The selection still requires genuine technical addability as a national idea.

Use the user-specified ID 104 for this design connection.
Do not import the older CSV's conflicting Rule number into the new specification.
The future catalog reconciliation must resolve those records without opportunistic renumbering of unrelated live content.

## Balance and replay character

Two countries with identical burden and Chaos receive the same count distribution, while their existing ownership can give them different fresh candidate sets.
Their resulting strength can differ enormously because quantity does not measure power.
No assertion of equal benefit, equal damage, or safe cross-system behavior belongs in the event's balance claims.

The specified count model has been checked mathematically for its threshold ordering and burden behavior.
Campaign frequency, engine randomness, the effective loaded pool, and native retention still need meaningful implementation evidence with native-execution limits stated honestly.
Use available current references, source calculations, and focused checks without requesting or awaiting user-owned game testing for agent delivery.
Those remaining checks should tune count constants only after preserving the complete pool and the exact lower-stage promises.
