# Technical state and integration handoff

## 1. Authority and evidence boundary

This document defines the accepted planning contracts for implementation.
Parts 01 through 04 own the tournament, preparation, match and evolution rules.
Part 05 owns presentation requirements, Part 06 owns AI and probability fixtures, and Parts 09 and 11 own implementation routing and completion evidence.
This document introduces no final player-facing copy or gameplay code.

The archived planning record says its supplied-source reading gate passed before that design session. This describes the imported intake, not a new acceptance decision or present source/tool inventory.
The integrated rules use 15-day camps, ten-day final settlement and one major enhanced course of up to 15 effective points in one attribute per wrestler per edition.
Part 12 records source authority and review history.

Part 12 records the archived inspected-source evidence.
Relevant entries are R02 for classifiers, R03 for offline GUI documentation, R05 for clone ownership and reservation order, R06 for universal costs, R07 for alien ownership and R08 for offline data structures.
Those references do not establish installed-game syntax, native bracket behavior, synchronized RNG or multiplayer execution. The archived session reported no HOI4 MCP route, installed-documentation pass or live multiplayer validation; that dated limitation is not a present-tense capability claim and does not make optional verification a completion gate.

## 2. Owners and proposed source surfaces

Use the event-owned stem `108_wrestling_tournament` and helper prefix `wrestling_` after identifier collision checks.
The canonical new entry is `chaosx.nr108.1`.
Original catalog ID 113 is reconciliation metadata, not a second runtime event identity.
Part 12 records the limited negative repository inventory evidence and the coding environment must recheck before creating files.

| Surface | Proposed owning path or system | Responsibility |
| --- | --- | --- |
| Opening and country receivers | `events/108_wrestling_tournament.txt` | Entry, notifications, safe response events and bounded scheduler delivery |
| Edition, tree and transaction logic | `common/scripted_effects/108_wrestling_tournament_effects.txt` | Authoritative mutations, construction, match commits, settlement and cleanup |
| Pure admission and action predicates | `common/scripted_triggers/108_wrestling_tournament_triggers.txt` | Eligibility, authority, preflight, validity and exact receipt matching |
| Tuning and enumerations | `common/script_constants/108_wrestling_tournament_constants.txt` | Schema-first categories for phases, statuses, days, budgets, caps and probability tables |
| AI scores and timing | Event-owned MTTH file under `common/mtth/` | Part 06's willingness and evolution timing, with exact native forms verified |
| Decisions and categories | Event-owned decision and category files | Payment, native factory reservations, camps, cases and response actions |
| Bounded lifecycle callbacks | `common/on_actions/108_wrestling_tournament_on_actions.txt` | Verified annexation, authority, host and scheduler repair seams |
| Sporting recognition | Event-owned ideas, modifiers and opinion files | One recognition tier, bounded consequences and explicit expiry |
| Dedicated bracket | `wrestling_tournament_window` and `wrestling_tournament_scripted_gui` | Read-only projections, navigation and calls into authorized actions |
| Shared event system | Existing registration, logic, event-log and settings owners | Repeatable selection, pre-fire guard, name/actor maps, history and evolution logging |
| Career and identity documentation | Event-owned helper reference and canonical event doc | Types, helper API, snapshot mapping, lifecycle, assets and implementation limits |

These are proposed ownership paths, not declarations that files or callable APIs already exist.
Event-specific logic stays in its owner files.
Do not add a neutral helper to `chaosx_dynamic_effects.txt` simply because one tournament needs it.
A genuinely cross-system helper requires existing-call-site review and paired shared documentation.
Shared event log, Event Details, settings and registries remain parent-owned rather than delegated to the event UI worker.

## 3. Record types and storage contract

Store authoritative edition records globally so losing a host or sponsoring country cannot erase a bracket.
Separate personal career identity, edition entry, current sponsoring authority and historical affiliation.
Use positive monotonic IDs and an explicit zero/invalid sentinel from a documented enumeration.
Do not recycle a retired person's ID or treat an array index as a contestant identity.

Persistent arrays use zero-based indices and supported numeric or token values under the offline contract in R08.
Every aligned record family has identical append, update and retirement operations across its arrays.
Its count equals its ID-array length.
Do not infer native object IDs through arithmetic on typed country or state pointers.

| Record | Minimum durable fields | Owner and consumers |
| --- | --- | --- |
| Identity | Wrestler ID, name token, source mode, portrait/version token, origin identity, authored availability, human/nonhuman classification and external provenance if any | Career owner writes, selection, match and history read |
| Career | Six attributes, dated form/record evidence, appearances, contested results, title standing, rival references, injuries, suspensions, retirement, last adjustment date and receipt | Career/outcome helpers write once, seeding and selection read |
| Applicant | Edition ID, country actor/authority generation, offered/reserved candidate IDs, nominated wrestler, admission result/reason, journey and arrival proof, historical display identity | Entry owner writes, lock builder reads |
| Entry | Stable entry ID, locked wrestler, seed inputs/evidence, original seed, leaf position, frozen affiliation, Readiness, Strain, preparation, assistance, safety and current lifecycle status | Preparation, lock and outcome owners write, GUI/AI read allowed fields |
| Edition | ID, ruleset version, phase, published dates, registered and locked counts/tree sizes, delay ledger, next work cursor, scheduler generation, champion standing, payout/placement receipts, archival settlement date | Edition owner writes, every scoped consumer validates ID and version |
| Match | ID, stage/round, two fixed feeders, outgoing destination, original/revised date, pair-freeze date, frozen pair/tactics, attempt references, current official verdict/version, output entrant or vacancy | Match owner writes, bracket, successor and inquiries read |
| Attempt | Match/attempt IDs, permitted inputs, validity revision, probabilities/weights, RNG receipt, selected outcome branch, method, actual attrition, injury and report receipts | Resolver writes, audit and case owner read with disclosure gates |
| Case/network | IDs, affected entries/attempts, true incident, allegation, evidence, public status, conduct finding, pending actor responses, delay use and sanction/amendment receipts | Case owner writes, public views read only disclosed fields |
| Command/payment | Request ID, actor and authority, edition/entry/action/target/version, accepted quote vector, actual paid vector, reservations, phase, compensation and completion receipts | Action/payment owners write, recovery reads exact matching record |
| Archive | Original seed line and complete qualifiers/main tree, immutable attempts, amendment chain, one current standing, historical names/flags/portraits and award disposition | Settlement freezes operational references, history projection reads |

An archive must retain all qualifier entrants and results.
Paging selects a bounded edition view and does not prune accepted countries, old identities or inconvenient sanctions.
Operational arrays for a new edition begin clean with new IDs, while career and archive IDs remain resolvable.
Normal cleanup retires temporary envelopes, not durable history.

## 4. Historical identity is independent of live ROOT

Freeze the edition's name, portrait version and historical national affiliation through an explicit display-identity registry.
The country snapshot includes stable country identity, relevant cosmetic/ideology version, historical name token and static flag asset version.
A live country pointer remains useful for current authority and payment but cannot supply frozen historical text or flags.
R08 establishes no arbitrary runtime string array storage.

Every supported campaign display identity must have a verified token-to-localisation and token-to-flag consumer.
Dynamic names outside that registry need a proved capture mechanism or an explicit snapshot blocker.
Do not substitute a mutable GetName call, present regime flag, unrelated portrait or anonymous replacement and claim compliance.
Retain original portrait identity in the archive even if a later approved asset improves the current profile.

ROOT remains the native callback's original scope through nested country and state blocks.
For country notifications it is the actual event recipient, while a targeted decision uses the documented acting-country and target contract.
A wrestler ID, historical affiliation or deleted sponsor is never a legal substitute for live country ROOT.
Capture explicit current actor, subject, host and payer pointers before nested work.
Revalidate COUNTRY objects with documented country predicates and STATE objects with documented state identity/validity predicates.
Variable-scope existence alone does not validate either.

Regular event targets carry short-chain scope pointers and can travel into events fired by that chain.
Global event targets require explicit lifetime and stale-target cleanup.
Temporary variables are unscoped and are not a durable frame.
Before each helper, caller-initialize every temporary output consumed after return, including forwarded arrays and trigger/localisation calls.
Freeze inputs and outer indexes in normal private storage before nested helper work that can overwrite aliases.
Public APIs document scope, inputs, caller-owned outputs, defaults, side effects, cleanup and direct call sites.

## 5. Immutable dates and the reserved calendar

At announcement, compute one preparation duration in the normal 70 through 110 day range, in five-day steps, with 90 as the anchor.
Publish and freeze that same duration for every entrant.
Entry closes at announcement plus 20 days.
Lock is entry close plus the frozen preparation duration.
The earliest reserved competition slot is lock plus ten days.
The default fixture therefore has entry close 20, lock 110 and competition opening 120.
Fifteen-day camps never become shorter full-gain camps to fit a changed deadline.

At entry close, let P_registered be the next power of two covering the registered field.
Reserve its complete sequence of round-size slots, separated by five days, and retain the published final date.
At lock, P_locked is the next power of two covering the still-valid field and cannot exceed P_registered.
Align the actual tree's rounds with the trailing slots for the same round sizes.
Unused leading slots are rest, not fake matches or additional training.

For a reserved P_registered of 128, the default round-size slots are 128 at day 120, 64 at 125, 32 at 130, 16 at 135, 8 at 140, 4 at 145 and final at 150.
If P_locked becomes 32, its first expected contest is day 130.
If it becomes 2, its first expected contest is the final at day 150.

Store `competition_open_date`, `expected_first_contest_date` and `first_actual_contest_date` separately.
The observed value is set only when a real contested attempt occurs.
A bye, walkover or unused slot does not manufacture an observed contest.
Expected timing may still encounter actual later vacancies.

Use a single edition exceptional-delay ledger with a ten-day aggregate maximum for venue, inquiry and no-contest delays together.
Each accepted change stores cause, old dates, new dates, affected descendants and fresh delay-consumption receipt.
Preserve at least the five-day round recovery interval.
One same-entrant no-contest retry consumes five days if allowance and safety permit.
Repeated no-contest or unavailable allowance produces a vacant branch.
The final settles ten days after its resolved final date.
Next announcement eligibility begins at least 180 days after actual archival settlement.
Store ordinary day durations separately from encoded dates and use the verified shared conversion contract where required.

## 6. Construction, match and standing transitions

Build one balanced power-of-two tree from the locked field using Part 03's seed-line recursion and full ranking tie-break.
For N above 32, the first log2(P_locked/32) levels are qualifiers.
Keep original seed labels through every upset and qualifying advancement.
Every accepted still-valid entry occupies one leaf, every empty leaf is explicit and every internal node has fixed feeder and successor links.
No survivor reseeding occurs.

Construction may require bounded batches.
Persist build phase, row cursor and completed-substage receipts, validate all aligned arrays and node links, then publish the completed draw once.
A partially constructed tree cannot accept tactics or resolve bouts.
A GUI preview of construction does not mutate it.

| Transition | Required guard and durable result |
| --- | --- |
| Open edition | No active edition, recovery elapsed, valid setup and fresh opening receipt before shared history/type accounting |
| Accept entry | Valid current authority, complete distinct candidate pool, journey proof and unique country/identity reservation |
| Lock | Published deadline reached, closed entry, current eligibility, complete ranking snapshot and tree construction receipt |
| Freeze pair and tactics | Both feeders settled and one day before actual scheduled bout, exact match/edition/version, saved default where no valid response exists |
| Resolve attempt | Frozen pair/tactics, present fitness/safety, permitted assistance validity and unused exact attempt receipt |
| Publish advancement | Fresh committed result mutation, fixed outgoing link and no earlier consumption of that result version |
| Amend before successor freeze | Proven rulebook case, original affected match/opponent, clean valid original opponent and unconsumed amendment receipt |
| Amend after successor freeze | Prospective removal/sanction or direct-final title review, no revival into a frozen successor |
| Settle final | Ten-day settlement reached, official standing resolved or explicitly vacant, title and runner-up recipients validated, unused award/placement receipts |
| Archive | Reservations and active missions settled, original/official history retained, phase terminal and actual archive date recorded |

Two absent feeders propagate vacancy.
One real feeder against an original empty leaf is a bye.
One real feeder against an unavailable opponent or later vacancy has the precise walkover/vacant-branch cause.
None of these uses a bout roll, opponent-quality win or upset credit.
An ordinary completed edition has one champion.
Insufficient, vacant and interrupted editions have explicit status and no fabricated title.

Pair/tactic freeze is distinct from the final permitted numeric input snapshot.
A final live check can withdraw an actually ineligible athlete or remove assistance whose owner dependency genuinely expired before the attempt.
It cannot select a new contestant, accept a late tactic or reroll an already committed numeric attempt.
Persist the validity revision used by the resolver so capability loss is explainable.

## 7. Request, payment and RNG receipts

A command identifies actor/authority generation, request ID, edition, entry or case, action kind, target, expected record version and accepted quote version/vector.
Pure preflight validates those identities, phase, authority, capability, positive amounts and exact pending-payment state.
A presence-only pointer, missing actual-paid field or stale actor does not expose a payable pending quote.
Visibility, enabled state, tooltip, availability, payment and AI use the same authoritative inclusive affordability components.

At execution, recheck the fresh quote.
A changed payable vector requires renewed consent before debit.
Once accepted and paid, later sale or country changes cannot rewrite that receipt.
Funding and treatment store start, due, consumed portion and actual reservations.
Refunds return only the actual refundable paid amount once, never a fresh nominal quote.
All payments use at most four spendable cost types and correct texticons under Part 02.
Factory reservations have one native decision owner and the reviewed R06 adapter.
The bracket does not independently reserve or debit them.

Suggested transaction phases are proposed, authorized, reserved, paid, result prepared, committed, rejected and compensated.
Their native persistence and execution semantics must be verified.
Reset the caller-owned fresh-consumption output before each attempted helper call and set it only on that call's exact successful mutation.
Never clear a durable committed receipt to prepare another attempt.
Already-used status is not proof this call consumed anything.
Duplicate requests return their existing disposition before any new debit, reservation, RNG, career update, advancement or award.
Rejected authority-loss cleanup does not run normal failure or reward effects.

Use simulation-side synchronized RNG only in registered opportunity/attempt transactions.
Selection, hidden incident truth, evidence discovery, bout winner, conditional method and injury pools have distinct stored receipts.
The winner pool draws once per attempt.
Part 03's official-bias path records clean and biased thresholds and one complete three-band pool on a common integer scale.
Its official-dependent branch may select only the narrow/long referee-method pool, never a decisive pin or submission.
The causal branch stays hidden until evidence authorizes disclosure.
Equal thresholds reduce to the ordinary two-outcome winner pool.

Store an exact native roll if a supported primitive exposes it, otherwise retain the synchronized selected branch and exact weight/probability snapshot.
Do not claim a nonexistent raw-roll reader.
The logistic equation is design mathematics.
Native production uses a verified monotonic fixed-point lookup or supported approximation with documented error, complement symmetry and bounds.
No exponential effect is assumed.
The GUI, localisation and AI consideration pass never draw sporting outcomes.

Before winner publication, freeze result inputs and outcome receipt.
After winner publication, method and attrition recovery consume their own pending receipts without replacing the winner.
Save/reload resumes prepared work or acknowledges committed work without another draw.
Source/local tests should model helper output lifetimes, the native loop ceiling and stored-state recovery. Use available save/state diagnostics where useful; do not launch HOI4 or make live save/multiplayer observation a completion gate.

## 8. Cases, awards and changes of authority

A case separates immutable generated truth, allegation, evidence, public status and official finding.
Each actor response has its own request receipt.
One country's approval cannot overwrite another country's pending inquiry.
Irreversible confirmation defaults are consequence-free refusal or ordinary care, with click-time revalidation independent from initial popup availability.
Tactic timeout uses the saved default, initially Balanced.
An allegation alone never awards an advancement or imposes a cheating sanction.

Before successor pair freeze, a lawful result amendment can restore only the actual original clean opponent to the existing branch.
After successor freeze, do not replay it or revive a former loser.
Append amendments while retaining original attempt history and one current official result version.
Direct final fraud can change standing to the original clean finalist during or after settlement.
Broader invalidity without a lawful recipient leaves the title vacant.

Separate edition championship payout, runner-up placement payout, recognition tier and career/title standing receipts.
Settle the initial title award only once after ten days.
The runner-up has an independent placement receipt and cannot inherit champion modifiers by receiving runner-up recognition.
After ratification, title transfer or revocation never pays a second edition PP prize.
Record remaining recognition removal and dated standing amendments without seizing spent resources or promising platform achievement retraction.
Awards are gains and never pass through purchase-discount helpers.

Before lock, loss of sponsoring authority withdraws an entry unless an existing valid exile/host path qualifies.
After lock, an already arrived, living, safe and otherwise valid athlete may continue under frozen historical affiliation when the external owner does not prohibit it.
Use saved/default tactics and ordinary neutral recovery.
The annexer gets no control or diverted national award.
A tag reused by a new actor receives neither old consent nor money.
An unsponsored champion retains their personal title while an invalid national recipient yields a recorded unpaid national-award disposition.
A portrait by itself proves neither the athlete's survival nor a valid external actor.

## 9. Bounded scheduler and future failover proof

Global arrays preserve data but do not execute a future timer.
The edition requires one living delivery recipient, one durable next due date, scheduling generation, pending-work receipt and bounded work cursor.
At each valid dispatch, retire the matching delivery receipt before processing, preserve unresolved work, and save the next generation before queueing one receiver.
Separate scheduled delivery from pending work so an immediate repair cannot create a second later receiver.
Stale generations do no gameplay work.

Choose a current existing valid host or registered participant through a bounded deterministic candidate set.
Maintain its exact actor/authority identity separately from the venue and athlete affiliation.
When that recipient disappears, a verified lifecycle callback must reach an existing country context, invalidate only the departed recipient's generation, preserve due dates and queue the remaining delay on a valid replacement.
The documented annexation winner is the proposed fallback repair context, subject to installed callback and source-chain verification.
An unrelated participant's annexation cannot steal another living scheduler's role.
Tag/authority changes and every actual recipient-retirement path need equivalent proved repair coverage.

Venue relocation, host loss, athlete withdrawal and scheduler failover are separate transactions.
A new venue does not rewrite the bracket or silently consume a second delay allowance.
An annexed athlete sponsor does not itself end an otherwise safe unsponsored career.
If completion becomes impossible, the reachable repair callback records interrupted/vacant closure and settles reservations.
No global daily, weekly or monthly world scan is added.

Process bounded batches below the verified 1,000-iteration ceiling.
Pop selected pending rows before processing and append unresolved rows after the preserved unvisited suffix.
Clear a pending receipt only after acknowledgement.
Full actual-world field and queue sizes require testing, rather than turning the checker range 2 through 512 into an admission cap.

A source guard is insufficient to prove future failover.
Acceptance requires a queued receiver whose country is removed before delivery, a native callback that selects and queues another real recipient, stale old delivery rejection, unchanged elapsed-time due dates and eventual progression or explicit closure.
If the installed game supplies no reachable repair seam for a particular disappearance path, that path remains a scheduler blocker.
Do not silently substitute an unapproved world hook or call the global array itself a timer.

## 10. Shared integration, migration and reader roles

The opening pre-fire helper acquires the active guard before generic history recording.
It supplies a meaningful actor only when one actually exists before that record.
A rejected forced opening uses the shared failure feedback and opens the existing bracket without an extra history row, payment or selection-weight change.
At most one explicit pending manual opening may be coalesced and rechecked after recovery.
Automatic selections create no backlog.
The shared repeatable-event frequency, reduction and recovery system remains authoritative.

Register 108 in the correct repeatable array, name/debug mappings, actor/detail selectors and event-owned runtime hooks together.
Keep catalog ID reconciliation explicit before workbook changes.
The workbook is the editable source and its CSVs are export-only. To Be Reworked is the desired status from the immutable brief, not the current row value: parent import evidence reports Event 108 as Fury / Unavailable with type, chaos and cluster blank and original row 113 as Unavailable. The parent owns later workbook reconciliation and any status approval.
Details describe premise rather than effects.
Baseline rounds are not evolution catalog stages.
Shared evolution context and enable gates precede unlock receipts and logging.
Evolution state and ordinary sporting outcomes give zero direct Chaos.
Part 04's real consequence premiums retain per-case receipts, its edition ceiling and no-double-counting shared harm rules.

Cross-event adapters read actual actor existence, provenance, species, owner operation, permission and revocation semantics.
R05 clone operation and R07 alien contact are narrower evidence than an eligible existing wrestler.
No landing, invasion, materialization, production, technology or laboratory grant is called to populate the tournament.
The Sparta interface remains an explicit future owner dependency under Part 04.

Event 108 is a new persistent general system and must follow the current test-country setup contract in [docs/testing/chaosx_test_country.md](../../testing/chaosx_test_country.md) and the applicable AGENTS.md instructions. That owner defines setup-carrier and registration details. Do not copy those mutable recipes here or add periodic content grants; keep debug fixtures distinct from ordinary tournament entries.

| Consumer | Read permission | Mutation boundary |
| --- | --- | --- |
| Bracket and public archive | Published identities, seeds, dates, routes, official findings and disclosed records | Viewer selection and follow preferences only |
| Participant management | Own entry, accepted quote, known health, own offers and permitted cases | Calls the same action mapper as native decisions |
| Spectator | Public draw/profiles and published cases | No participant control or confidential treatment/tactic access |
| AI owner | Same eligible actions and disclosed opponent information as humans, plus its own private team state | Same transaction and cost owners, no outcome or future-roll reading |
| Part 06 probability auditor | Explicit fixtures, full pools, source revisions, hidden audit receipts as authorized | Read-only evidence, no balance patch or gameplay mutation |
| Parent and systems architect | Complete contract and scope/call-chain evidence | Reviewed gameplay owner changes and final integration |
| Event UI worker | Event-owned bindings, public/authorized projection schema and GUI scenario data | Bounded layout and consumer wiring, no independent payment or match resolver |

Before implementation, reconcile workbook numbering, current source owners and every actual identifier collision.
Do not promote an old placeholder or unrelated Event 113 state into a wrestler record without explicit migration proof.
Version the new edition schema and retain ruleset versions on historical attempts.
A future schema change needs a bounded monotonic migration with receipts, preservation tests and exact handling of active transactions.
Do not rebuild old seeds or history using current balance constants.

## 11. Required handoff and exact open proof targets

The coding handoff returns the helper API map, aligned schemas, callback-to-scope traces, transaction recovery states, native reservation owner, source and constant crosswalk, frozen identity mapping, complete pool manifests and parent-reviewed migration decisions.
Part 11 supplies scenario acceptance rows and Part 09 assigns the canonical audit owners.
The mathematical checker and parent rerun establish the abstract seed and probability properties, including N-1 intact-field bouts, but do not establish native execution.

The design leaves implementation questions around installed effects and trigger syntax, dynamic tokens and historical identity consumers, constant schemas, synchronized RNG and weights, fixed-point error, command recovery, factory reservations/refunds, scheduler recipient repair, actual field capacity and bracket wiring.
The parent must inspect current source owners and use relevant MCP routes only when they are exposed and useful. Follow AGENTS.md's limit of one initial request and at most one corrected or narrower retry, then use direct reference/source inspection and meaningful local checks.
The archived tool inventory exposed no HOI4 MCP routes at that time; it is not a current capability claim. Missing optional MCP, save-inspection, renderer or live multiplayer evidence alone does not block otherwise supported source implementation. Do not launch HOI4 or request or await user live-game validation. State what source/local checks establish and identify any material engine behavior that remains unverified.
