# 14 · Persistence and owner contracts

## Give every experiment its own identity

A wave is a parent record. Each experiment is a child record with an immutable generation and sequence. A physical sub-pulse, reward delivery and continuing owner effect each has a distinct receipt identity linked to that experiment. The runtime representation may use fixed slots and compiled scripted branches if that is what the installed engine supports. Do not assume arbitrary persistent objects or runtime reflection exist.

The 24 live slots are a scheduling bound, not an authorization to reuse a live record. Reusing a closed slot increments its generation. Every delayed event, decision target, mission callback and owner return must validate that generation before acting. A callback from an old occupant becomes a no-op even if the slot now contains a different country.

| Record | Required information |
| --- | --- |
| Wave | Unique sequence, commissioning USA identity, creation time, effective evolution profile, selected job identities, counted-as-fired receipt |
| Job | Slot and generation, wave, original actor and recipient identities, state, family, concrete provider, provider revision, frozen test and reward profiles |
| Schedule | Stage, demand deadline, preparation end, commitment state, impact or pulse due dates, analysis deadline |
| Authorization | Acceptance or refusal receipt, legal-war preconditions, prototype permission, reserved and spent resources |
| Physical result | Requested and applied civilian loss, military route, building and supply mutations, owner instance IDs, verified or unresolved status |
| Delivery | Technical result, reward headroom check, selected benefit, granted receipt, pending earned claim |
| History | Repetition counters, last actual impact dates, unique family and continent successes, victim damage objectives, cumulative exact losses |

These are required data meanings. They are not claims that variables with these exact labels already exist. Inspect native scope and serialization limits before assigning the actual storage layout.

## Freeze agreements and recheck physical reality

Freeze the accepted target country, state, weapon family, selected variant, severity and reward scale. Re-evaluate whether the country exists, the state is still a valid authorized location, the required owner is enabled, and resources or reserved permissions remain valid. Measure population, buildings and units at the actual impact.

A recheck cannot quietly replace an accepted artillery trial with a nuclear test or move the target to a new government. Invalidity cancels an uncommitted job or follows the existing committed-provider cancellation contract. It does not produce damage in an unrelated state or a free reward.

A target becoming a major after acceptance does not alone erase its already agreed test. A change of owner or legal recipient is different and requires a valid authorization contract. USA becoming a subject, losing the ability to declare the threatened war, or disappearing requires revalidation of open demands.

## A mutation is not safely repeatable

Write the unique mutation-issued marker before applying an irreversible effect. Capture the actual result immediately through the owner transaction. A retry with a completed receipt returns the existing result. A retry with an issued marker but missing proof enters an unresolved state and does not apply the effect again.

The engine does not provide a general database transaction merely because these records are called receipts. The implementation must prove that the selected same-effect mutation and observation order survives the game's event and save semantics. Where it cannot prove recovery from an ambiguous issue, quarantine the job for diagnosis. Never guess a successful result or risk duplicate deaths through a blind retry.

Reports may be rebuilt from completed receipts. Physical losses, declarations of war, equipment debits and reward grants may not be replayed to rebuild presentation. The shared history logger records the wave once and receives separate follow-up entries where supported.

## Scope discipline

The actor is USA for this event, regardless of which country received the shared random-event dispatch. The victim, impact state and responsible provider must travel through explicit verified scope contracts. Do not infer them from an arbitrary stack of FROM scopes after several delayed events.

The read portion of the offline event reference notes that delayed events for a nonexistent country can remain pending until the country reappears. Consequently, a release or civil-war change must not resurrect an old unvalidated ultimatum or impact. Generation guards and current identity checks are required at the earliest authoritative callback.

A reward earned by the original USA is not transferred automatically to any country that later occupies its states. If that country disappears, preserve the claim under the original identity according to the existing country's lifecycle contract. Do not assume a later released tag is always the same eligible recipient. The current repository must settle the valid inheritance behavior explicitly.

## Shared owner boundaries

| Owner | Required call or capability | Event 076 must not do |
| --- | --- | --- |
| Exact civilian loss | Documented `apply_exact_state_civilian_population_loss` and its observed result | Apply another state loss after an owner already did so |
| Shared Deaths | Existing registration and attribution, disabled-setting behavior | Guess a reason ID, double-register, or force-enable the ledger |
| Unit damage | Verified local target selection, actual damage and military accounting route | Debit unrelated reserves and describe destroyed deployed units |
| Building damage | Existing dynamic helper where valid, native removal and provincial adapters | Treat infrastructure damage as proof of railway damage |
| Nuclear | Restricted prototype authority, actual strike, fallout and project development | Add reusable free warheads or duplicate nuclear-use accounting |
| Chemical and biological | Existing valid tests, contamination, outbreaks and pulse receipts | Duplicate spread, exposure, disease or containment logic |
| Condemnation | Incident submission and evidence supplements | Maintain a competing sanction ladder |
| Research and production | Family-specific useful benefit and stacking semantics | Grant a capped or nonexistent bonus as a meaningful reward |
| Decisions and missions | Actual costs, map objectives, inclusive affordability | Charge twice or finish an objective merely because its timer expired |

When a documented dynamic stockpile helper negates a temporary quantity in place, initialize that temporary value before every call. Do not reuse a mutated negative value for the next test, which could accidentally grant equipment. Isolate provider scratch variables from job history.

## Continuing owner instances

After a completed biological analysis, an outbreak remains a disease-owned instance with the experiment's causal identifier. The event retains a compact mapping from that instance to actor, victim, originating state and wave. Each later loss pulse has an owner sequence or equivalent unique key.

Tail attribution must survive ownership changes and program closure. It must not require keeping every original UI field, mission and temporary event target alive. Preserve enough exact cumulative data for country reports, the shared ledger and achievements, while using bounded owner-supported receipt retention.

Do not promise permanent unbounded per-person or per-pulse storage. Establish the retention and compaction contract with the current owner. Aggregate only after deduplication and after no outstanding callback can reuse an old identity. A compacted receipt must still prevent a replay from adding the same loss again.

## Cancellation and migration

Before commitment, a valid player cancellation releases unspent reservations, removes that demand and its pending impact, and records no successful test. It does not refund resources already consumed by an owner. After commitment, show whether the owner can actually abort. A button cannot promise a recall that the provider cannot perform.

New provider revisions affect new jobs. Existing accepted jobs keep a supported revision or undergo explicit migration. A removed handler cannot be replaced with a different weapon family without renewed authorization. A migration must not reissue completed damage or regrant already received rewards.

Legacy `USA_testing_denied` does not grant permanent immunity. The new system does not preserve the old reversal in which the victim was made the aggressor. Existing wars are not automatically ended or reversed during save migration. Retain their real game state and begin applying new event behavior only through validated new jobs.

## Missing capabilities are implementation gates

The inspected documentation establishes a useful exact-loss interface, but the corresponding full current implementation was not audited here. Local unit damage, railway and supply mutations, restricted pre-technology nuclear tests, exact long-tail attribution, research headroom and slot serialization all need current repository and installed-game verification.

Preserve the mandatory design when one of these is absent. Build the correct owner adapter or record the blocked requirement. Do not mark the whole event complete after reducing it to a conventional building penalty, a disease modifier or an immediate generic experience reward.
