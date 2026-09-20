# 070 Cookie Click: runtime and integration contracts

## Ownership and identifiers

The root catalog identity is Event 070 and its planned root event is `chaosx.nr70.1`.
Internal callbacks, flavor events, warnings and revolt events are members of that same event-owned system.
They are not separate picker events or cluster members.

Use a stable instance identifier, an explicit owner country and a separate resulting Empire identity.
Do not infer the owner from whichever country happened to open a GUI or receive a news report.
The final tag, scenario registry ID, super-event IDs and exact file-level runtime names require an inventory before assignment.
A planning token is never passed to the engine as a real tag.

ROOT and inherited event scopes retain their actual engine meaning.
Use explicit saved targets and scope-safe helper parameters.
Do not pretend that entering a country scope changes ROOT.
Do not use an event recipient as both an observer and an authoritative owner without checking which role it actually has.

## Lifecycle

| State | Entry | Allowed work | Exit |
| --- | --- | --- | --- |
| Uncreated | No active instance | Normal picker eligibility or explicit manual setup | Pet initialization or manual Empire preflight |
| Living weak | First pet initialization below maturity | Clicks, rewards, hunger, bounded self-feeding and possible starvation death | Permanent maturity, weak death or removal of owner |
| Living mature | Maturity threshold crossed or evolved opening | Clicks, rewards, hunger, preparation and warning | Recovery remains in this state, or revolt preflight |
| Revolt warning | Eligible persistent severe hunger and warning interval | Feeding rescue and permitted preparation | Cancellation, failed eligibility or completed danger interval |
| Revolt preflight | A permitted successful danger draw or direct scenario launch | Validate every mutation dependency and calculate snapshot | Commit or return to unresolved pet state without partial setup |
| Cookie Empire | Country successfully committed | Economy, wars, units, tree, subjects and possible world-end entry | Defeat, owner destruction or The Final Bite |
| Final Bite active | Ordinary or manual world-end commit | Global aggression and final campaign | Defeat or settled terminal result |
| Ended | Weak death, defeat or other resolved lifecycle | Limited durable history and valid aftermath | A separate explicitly launched manual instance only |

Weak death and successful country creation are irreversible for that instance.
A recovered warning returns to a mature pet.
It does not restore an early-removal opportunity.
A failed preflight never counts as a successful uprising.

## Saved data contract

| Data group | Saved fields | Ownership and use |
| --- | --- | --- |
| Identity | Instance ID, original host, current pet owner, Empire tag, manual flag, active lifecycle, setup stage | One authoritative system owner |
| Daily feeding | Cycle serial, start and end time, frozen target, accepted clicks, paid milestone mask, full reward status | Pet owner, checked for every accepted click |
| Growth | Human lifetime clicks, completed full cycles, consecutive full cycles, reward-value history, earned Level thresholds | Permanent instance progression |
| Appetite | Current evolution, maturity flag, hunger cycles, severe cycles, zero-click cycles, last bite time | Pet phase only |
| Warning | Armed state, remaining warning interval, eligible rolls, recovery marker, pending commit ID | Only one warning per instance |
| Reward track | Frozen eligible family choices, exact quantities, saved alternatives, entitlement IDs, actual paid value | Paid once and never re-rolled on reload |
| Consumption | Actual debit history, source family, completed-batch IDs, per-state irreversible history | Shared with uprising strength where relevant |
| Empire | Food reserve, frozen daily demand, policy, governing method, birth Level, growth score, first-settlement history, current Level, army and expansion snapshot | Replaces pet feeding data as active logic |
| Operations | Owner, target, saved inputs, committed quantities, completion state, deadline, partial-result ledger | Per active program with explicit limits |
| World | Registered Cookie threat source, milestone flags, valid neighbor set, global-war queue, Cookie-domain members | Bounded event-owned indices |
| Presentation | Current semantic face, level band, evolution band, acknowledged warnings | No cosmetic frame index affects gameplay |
| Eligibility | Manual setup history, suspension history, achievement disqualifiers | Persistent campaign accounting |

Public values remain Cookie Fullness and Cookie Level.
The daily click count and target remain next to the Fullness bar.
The lifetime-click number can appear in its prescribed tooltip.
The other stored fields are implementation state, not extra player-facing meters.
Do not expose an entire debug data table in the normal interface.

## Accepted-click transaction

The following is logical pseudocode.
It is not claimed to be valid HOI4 script.

```text
receive click intent for displayed owner and cycle
validate human control, active living state and authoritative owner
reject stale cycle, ended instance, locked transformation or already full target
increment accepted daily and lifetime clicks by exactly one
derive the new displayed Fullness from the frozen target
record growth and permanent maturity transitions
grant any newly crossed milestone entitlement once
if the 75-percent milestone is reached, cancel a pending warning immediately
if the full target is reached, lock further clicks for this cycle
update only this window's semantic state
emit the supported local visual and sound reaction
```

A client animation is not evidence that the authoritative click was accepted.
In multiplayer, the accepted count and reward ownership must pass through the engine's supported synchronized action path.
A packet retry or repeated GUI callback must not pay a milestone twice.
Verify the actual available GUI action and synchronization behavior in the installed game.

Every physical accepted click can have immediate local feedback.
Expensive gameplay effects, stockpile scans, reward-family selection and global logging must not run on every click.
They run at initialization, relevant state changes or milestones.
Per-click counter mutation is still real gameplay work and must be measured.

## Cycle and bite scheduling

Use one owner-aligned 24-hour cycle.
At a cycle boundary, finish accepted intents belonging to the old cycle under a deterministic server order.
Commit any newly completed milestone before classifying that cycle's hunger.
Evaluate the completed cycle's fullness, then early death, warning and revolt conditions.
A completed death or revolt cancels pet self-feeding.
Next initialize the new cycle, frozen target and saved reward track if the pet remains active.

The cycle's self-feeding bite is scheduled at its first owner-local quarter review after the daily hunger classification.
There is at most one completed mechanically significant bite in a cycle.
A first accepted click can postpone that pending bite until the next quarter review.
At each such review, at least five percentage points of new feeding progress extends the hold.
Reaching 75 percent suspends the bite for the rest of the cycle.
A stalled player eventually reaches a review where the due bite can resolve.

Hunger, severe-cycle history and zero-click history are classified from the completed cycle even when the bite was postponed.
Therefore a token-click pattern cannot indefinitely evade the revolt history.
Unused bite budgets do not accumulate into an unlimited delayed punishment.
A cookie can remain angry without receiving a retroactive sequence of ten missed debits at once.

The first initialization cycle receives the grace described in part 01.
A reward track or target is never partially replaced during a cycle.
An evolution activated during the cycle affects its face and warning information immediately where appropriate, but new target and consumption-pool permissions start on the next cycle.

## Reward mutation order

Save the entitlement's attempt state before calling the award helper.
Revalidate the selected reward and its documented alternative.
Apply only a supported actual award.
Record the actual quantity and value, then mark the entitlement completed.
A repair callback consults this record before doing any work.

The available engine is not assumed to support an atomic database transaction.
Design script ordering and completion flags around the actual save and callback behavior.
Test saves at each staged boundary.
Where the engine cannot expose an exact intermediate mutation receipt, use a narrow idempotent award design and test it rather than claiming database-level guarantees.

Batching at 25, 50, 75 and 100 percent gives four ordinary award checkpoints.
One click crossing a rounded milestone is sufficient.
The number of checks does not depend on whether a player clicks slowly or at an unusually high rate.
The final reward is never paid merely because the cycle ended.

## Helper boundaries

The supplied helper documentation is the starting contract.
Read current implementations before reuse.

`calculate_economy_scaled_factory_grant` calculates a count.
The caller still owns valid-state selection, slot checks and application.
It is not a promise that factories have already appeared.

The equipment stockpile helpers use documented temporary inputs and return actual debits.
Reset every caller-owned input before use and read actual outputs afterward.
Do not allow parameters from a previous cookie bite to leak into the next owner's operation.

`union_compatible_researched_technologies_from_donor` is an additive compatible-technology helper.
Use it only when a country setup explicitly requires that donor behavior.
It is not the ordinary daily research reward and is not permission to hand out every available technology.

Population helpers must distinguish actual civilian loss, recruitable-manpower side effects and death reporting.
Conversion requires a supported non-death transformation path.
Research-progress consumption requires an actual supported progress mutation.
A temporary research-speed penalty is not an equivalent implementation of eaten research progress.

## Country commit

The country-creation worker validates tag availability, territory, capital, laws, technology, templates, equipment, starting troops, AI and diplomatic targets before mutation.
Use the current event and country creation skill's accepted order.
A dormant tag is not treated as a complete country before its valid capital and required initialization exist.

Assign source and destination ownership in a known safe sequence.
Set the planned capital and backup.
Initialize additive technology and country-specific systems without erasing a living country.
Create only paid and budgeted troops in valid controlled locations.
Complete stocks, production, government, characters, tree and AI setup before handing control to the player.

Character creation and recruitment must follow the current source's supported event context.
Do not move unsupported character recruitment into an on-action merely because it is convenient.
The corresponding country package audit must check it against installed vanilla examples.

A staged repair can restore a missing portrait binding, missing setup flag or invalid target cache.
It cannot rerun a completed force grant.
A partial mutation that cannot be repaired safely must be reported as a failure with reproducible evidence.
Do not hide it behind another broad country initialization call.

## Indexing and performance

Maintain a short active-cookie owner list, an Empire list with the singleton restriction, active operation targets, prepared territories, current external neighbors and queued global enemies.
Use event-driven updates for ownership, control, country creation, destruction and border changes when verified hooks exist.
Use a bounded periodic reconciliation only as a safety check.

Normal pet updates do not scan every country, every state or every available technology daily.
Reward and edible registries cache supported candidates and revalidate the selected candidate before use.
Dynamic validity does not mean unlimited repeated global enumeration.

During The Final Bite, process a bounded batch of queued targets per update.
Retired targets are removed.
A terminal campaign performs one confirmation pass and then stops unnecessary war-queue work.
Cosmetic animation updates never invoke world-state scans.

A stress test must include the 20,000-click target, rapid input, maximum visible particles, several concurrent missions, a large Empire, and multiplayer spectators.
An unsupported visual feature cannot be approved solely because its still-image mockup looks plausible.

## Long-campaign numeric precision

Verify the exact supported variable range and precision in the installed game.
A daily ceiling does not stop lifetime clicks from growing over many years.
If a single native variable cannot preserve each click exactly, use a documented bucket-and-carry representation with supported integer-safe parts.
The lifetime tooltip reconstructs the same total.
Do not silently lose accepted clicks because the variable can no longer represent an increment of one.
Test the carry boundary, saved rewards, Level calculation and reload using the actual engine representation.
The included Python model uses arbitrary-precision integers and does not validate native numeric limits.

## Save migration and cleanup

Add a versioned event-owned save schema.
Existing saves with no Cookie state remain untouched.
An older Cookie schema migrates once using documented defaults.
Missing optional visual state is repaired without replaying rewards.

When a pet dies, cancel its future cycles, warning and bite callbacks and retire its GUI state.
When the Empire forms, retire only the pet-phase callbacks.
When the Empire is defeated, retire its economy, global-war and event-owned diplomatic tasks.
Keep durable demographic effects, actual wars, surviving subjects and properly earned permanent assets.

Manual restarts receive a new instance and never reuse an old warning ID.
An old callback checks its instance and exits.
The cleanup audit must prove that no periodic Cookie task continues for an ended instance.

## Implementation evidence

The repository explorer must inspect the current Event 070 identity and any historical remnants before changes.
The event inspector must establish the actual root and callback graph.
The focus, decision, technology, GUI and probability tools must provide their corresponding before-and-after evidence.
A static syntax check alone does not prove the feeding interaction, country setup or world-end campaign works.

Record the installed game version, DLC set and tested mod combination.
Only supported current effects can be promoted from this logical design to runtime source.
An unresolved engine capability remains a named implementation blocker with a reproducer and the intended behavior.
It must not be silently replaced by a smaller feature while the package is marked complete.
