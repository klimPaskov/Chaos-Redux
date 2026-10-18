# 113 The Partition: Tasks and shared systems

Event 101 Tasks can turn an active partition into a timed commitment to another country's survival or to a durable settlement.
The objective attaches to a real crisis that already exists.
Its result follows the actual campaign outcome and the accepted deadline.

The accessible repository review did not establish an implemented Tasks 101 API or Event 113 runtime.
The interface below is therefore a complete proposed dependency contract, not a claim that these helpers already exist.
The implementation must resolve the current owner before adding or changing shared behavior.

## Two Task families

### Task D: Defend a threatened country

The Task may be offered to the target itself or to an eligible outside protector while the crisis is still in diplomacy or actual war.
The target must remain a living eligible minor and the full-prevention result must still be uncertain.
A completed withdrawal, already completed defense, or fully ratified handover does not create a new easy attachment opportunity.

The proposed deadline is 180 days at baseline, 240 days in Partition Fever, and 360 days in Grand Partitions, measured from Task acceptance.
The offered date and required result are fixed and visible at acceptance.
A later active evolution changes the difficulty of the crisis but does not silently extend the Task.
The Task owner can decline to offer a deadline that is implausible for the current phase.

Success requires the bound target to achieve full prevention by diplomacy or defense before the deadline.
The target must retain all opening owned territory, remain independent, control its capital and threatened states, and have no outstanding partition award or relevant aggression.
Mere existence at the deadline, one victorious battle, or one capitulated claimant is insufficient.

The target's own Task requires that real outcome.
An outside protector additionally needs a qualifying contribution to the same crisis made after Task acceptance and before resolution.
Its current-country identity must match the accepted actor, and it cannot be an active claimant against the target.

| Protector contribution route | Required facts | Limits on credit |
| --- | --- | --- |
| Material protection | Both the full arms package and full transport package actually delivered, with valid matched donor and recipient receipts | Each package credited once, returned or circular supplies do not create a second contribution |
| Guarantee backed by aid | A new native guarantee actually established and maintained through resolution, plus one full actual arms or transport package | A preexisting guarantee or a repeated request alone earns no new contribution |
| Sustained defensive intervention | Actual legal entry into the target's defense and continued participation for at least 30 days before resolution | An issued goal, preparation, or promise is insufficient |
| Early intervention in a short war | Actual legal entry within five days of the first verified crisis attack, continued participation until the relevant aggression ends | Available only when the entire relevant war lasted less than 30 days, preventing a last-moment nominal entry |

These are observable commitment routes, not a claim of exact battle causation or a generic named-war contribution score.
Ordinary volunteers and lend-lease may help the target in play, but they count toward this Task only if a separately verified current owner can attribute the required actual contribution to the same crisis without false credit.
The default acceptance contract uses the four routes in the table.

The Task completes from a verified full-prevention outcome and a qualifying contribution where required.
Its success is immediate at that proven result.
The event's separate 45-day containment observation governs its direct Chaos reduction and does not delay Task D unless the Task offer explicitly includes that extra requirement.
The UI must show this distinction.

### Task S: Secure a durable settlement

This Task may be offered to the target, an invited mediator, or a claimant genuinely willing to moderate the proposal.
It is offered while material terms are still unsettled, before the final required ratification.
The proposed deadline is 180 days at baseline, 240 days in Partition Fever, and 360 days in Grand Partitions.

Success requires a completed nonextinguishing settlement or a binding no-transfer withdrawal outcome that leaves the target independent, followed by 45 days of compliance within the accepted deadline.
All promised awards and due material commitments must actually be completed.
The target must meet the appropriate remnant conditions.
Relevant aggression must have ended through actual withdrawal or native peace.

A complete partition, a nominal remnant below the accepted floor, a partial handover, or a signed agreement still being fought over does not satisfy this Task.
The actor's own contribution must fit its role.

| Actor | Required contribution before resolution |
| --- | --- |
| Target | Submit or accept the actual valid settlement and maintain its obligations through the follow-through period, bearing the real territorial sacrifice where applicable |
| Mediator | Lead a target-invited proposal that removes at least one state from the first valid published demand, changes a complete offer into a viable limited offer, or secures a binding no-transfer withdrawal |
| Moderating claimant | Permanently forgo at least one valid state from its first published demand, representing at least 25% of its originally demanded population or industry, or withdraw its entire original demand |

For a claimant with zero demanded industry, only the population test applies.
Its first published demand is the baseline for sacrifice.
It cannot enlarge an offer after taking the Task and then claim credit for withdrawing that artificial addition.
A state promised to somebody else never counts as this claimant's sacrifice.

The target's formal acceptance can be sufficient as its contribution because the agreement itself has a real territorial or political cost and must hold for 45 days.
It does not earn success by signing alone.
An outside mediator must have the specific material improvement or withdrawal result recorded, rather than appear in the final report after others resolved the crisis.
Its credited proposal must materially improve the then-current offer after attachment as well as satisfy the immutable first-demand comparison.
Repeating a concession completed before its participation gives no contribution credit.

## Success, failure, and neutral cancellation

The Tasks owner evaluates the current bound outcome at the deadline before applying timeout.
A result already valid by that deadline is eligible for success even if a notification is delivered later.
A result that becomes valid afterward does not retroactively turn a failed timed objective into success.
For a 45-day settlement follow-through, the accepted conditions must have completed that full period by the deadline.

| Condition | Task D | Task S |
| --- | --- | --- |
| Full prevention before deadline, actor contribution valid | Success | Success only if its settlement and 45-day compliance requirements also hold |
| Durable limited settlement before deadline | Failure to prevent partition entirely | Success if role contribution and remnant conditions hold |
| Target remains alive but fighting continues at deadline | Failure | Failure |
| Partial handover or agreement not yet durable at deadline | Failure | Failure |
| Target loses all owned territory or becomes a subject | Failure, regardless of which country caused the actual loss | Failure |
| Target becomes a major while the objective is still active | Neutral cancellation | Neutral cancellation |
| A still-independent target's suspended crisis closes because an unrelated war prevents lawful resumption | Neutral cancellation if the Task actor did not initiate that unrelated war, otherwise failure for abandoning a viable objective | The same |
| Target identity becomes technically ambiguous after a transformation | Neutral cancellation until the owner can prove continuity, with no reward from the old identity | The same |
| Actor ceases to exist or abandons the required actor identity | Failure under the Tasks owner's campaign identity rule | The same |
| An invalid attachment is rejected before acceptance | No Task created | No Task created |
| Duplicate terminal message or save reload | Existing result retained, no second payment | The same |

An unrelated annexation is a real failure to preserve the country, even though it does not count as an Event 113 complete partition.
Neutral cancellation is reserved for an invalid objective or authority, such as major immunity or an unresolvable identity transition.
It is not a way to conceal a real military or sovereignty loss.

The event publishes the actual outcome once.
Tasks owns the reward, failure consequence, deadline, and one-time consumption of that outcome.
Reward values use the current Tasks balance owner rather than an invented second reward table inside Event 113.
Baseline, evolved, and Grand objectives carry proposed ordinary, hard, and extreme difficulty bands for that owner to evaluate against actual risk.

## Attachment and observation contract

The integration needs the following information, expressed here as semantic fields rather than registered helper names.

| Field group | Required content |
| --- | --- |
| Identity | Event 113, immutable batch, crisis, attachment and actor identities, target identity generation |
| Accepted objective | D or S, actor role, opening form, accepted date, absolute deadline, exact success and contribution rules |
| Territorial baseline | Opening owned states, union of valid threatened states, first published claimant demand where relevant, current proposal version |
| Commitments | Approved provider, commitment kind, actual delivery or native relationship evidence, applicable due date |
| Progress | Current phase, pending obligations, first valid outcome date, compliance start and any breach date |
| Terminal result | Proven outcome, actual state ownership and sovereignty facts, success or failure eligibility, precise cancellation reason |
| Consumption | One fresh result sequence, recipient acknowledgment, reward or failure already consumed flag |

A proposal revision can change the crisis's terms without changing which country Task D promises to preserve.
Task S continues only if its objective remains achievable under the newly displayed valid terms.
It never silently turns into an objective to erase the target.
An attached Task retains its original opening-territory and sacrifice baselines so that revised proposals cannot make it artificially easy.

Each actor can have at most one active Partition Task.
The Tasks owner may attach different actors to the same crisis when their roles are valid.
Each has its own contribution and reward receipt.
The event outcome is shared evidence, not a global reward flag that every late observer can consume.

An absent Tasks subscriber does not create a deferred reward entitlement.
A subscriber that accepted while the crisis was active can consume its terminal record after the active crisis row is cleaned up.
The retained record is bounded to the needed outcome and acknowledgments.
It is not a second unlimited campaign history database.

## Shared event and catalog integration

The shared event dispatcher prepares the actual actor bundle before the generic opening log is written.
The wave uses the repeatable event handler once and the Diplomacy cluster's existing pacing rules.
Individual target announcements, later outcomes, protection responses, and evolution reports use their appropriate history paths without repeating global event pacing.

The design requests a High-severity member of the Diplomacy cluster for Event 113.
The current supplied catalog snapshots place The Partition at original ID 123 and place a different event at 113.
Before any implementation changes the authoritative workbook or runtime registration, the current workbook must be hydrated and the identity mapping reconciled explicitly.
The original ID is provenance, not a second runtime dispatch alias.
Existing unrelated event data must survive that reconciliation.

The authoritative XLSX is the editable catalog source.
The supplied CSV snapshots remain evidence and exported views.
An implementation updates the workbook through its owner and regenerates the CSV exports with the project's exporter.
This planning task does not change those sources or claim an implemented status.

## Shared crisis capacity and costs

The target selector uses the documented shared limit of three applicable local crises per country.
The implementation must locate the actual capacity reservation and release contracts and demonstrate exact reuse.
The event's separate three-commitment claimant/protector limit must not masquerade as that shared owner.
A target's capacity reservation lasts through its unresolved crisis, including its continuing war observation, and releases once on closure.

The universal-cost framework owns quotation, supported resource adaptation, actual paid components, and refund receipts.
Event 113 owns the action's purpose, actor, target, proposal, eligibility, consumed or refundable character, and outcome.
The implementation must prove each required resource path and actual donor-to-recipient conservation before enabling material transfers.

## Other campaign systems

Existing claims, cores, factions, guarantees, focuses, leaders, armies, occupation, state buildings, and native country identities remain the campaign's source of truth.
The event adds its own temporary plans, negotiations, and documented outcomes around those facts.
It does not rewrite meaningful country content as a consequence of merely entering a crisis.

The shared human-crisis-pressure owner supplies its documented pressure factors where the accepted context applies.
The shared civilian, famine, migration, Deaths, and Condemnation systems act on their own actual conditions and evidence.
A land transfer alone supplies neither a casualty report nor a physical migration transaction.
An ordinary partition attempt does not register an existential world-threat source.

Disabling this event in the shared random-event setting prevents new firings according to that owner's current semantics.
Existing crises continue their accepted deadlines, obligations, outcome observation, and safe cleanup after new firings are disabled.
Disabling selection is neither a border reversal nor an end to an existing native war.
If the current shared setting also requires immediate retirement of active event machinery, that implementation conflict must be reported before wiring the setting rather than silently replacing this continuation rule.

