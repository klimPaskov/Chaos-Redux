# Fallout scheduler post-commit documentation reconciliation handoff

Status: reconciled, incomplete, and dormant

This documentation-only pass reconciles the parent blocker ledger after commit
`de0b45fd3e88`. It updates only `BLOCKERS_AND_DECISIONS.md` and this handoff.
It does not claim scheduler activation, event completion, runtime acceptance,
or completion of the Fallout living-world goal.

## Files changed

- `docs/plans/air_cleanliness_fallout_plans/BLOCKERS_AND_DECISIONS.md`
  - Updated B9 to describe the accepted numerical scheduler substrate as
    implemented behind unset activation gates.
  - Restored the release blockers for atomic major-arc and relationship
    reservation, 25-point relationship relevance, active-siege receipts,
    pair-memory compaction, reviewed candidate production, content callers,
    host authority, runtime proof, and reserved suffixes.
  - Updated B12 to record the fifteen defined dormant Ash-week blocks, six
    dedicated report sprites, missing eight blocks, incomplete matrix and
    candidate package, missing caller, missing logs and details, and the zero
    release-floor count.
- `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/fallout_scheduler_post_commit_doc_reconciliation_2026-07-18.md`

No gameplay, localisation, GUI, asset, spreadsheet, specification, or source
event file was edited by this pass.

## Source-of-truth map

| Authority | Current role | Disposition |
|---|---|---|
| `FALLOUT_EVENT_SCHEDULER_PROOF.md` | Current scheduler implementation and activation-boundary evidence | Current authority after `de0b45fd3e88` |
| `FALLOUT_EVENT_SCHEDULER_NUMERICAL_CONTRACT_PROPOSAL.md` | Accepted cadence, scoring, fatigue, pressure, queue, tie, and hidden-AI contract | Promoted into source specs and dormant implementation |
| `README_IMPLEMENTATION_STATUS.md` | Current cross-system status and release floor | Current high-level ledger |
| `FALLOUT_ASH_WEEK_ORIENTATION_CONTRACT_PROPOSAL.md` | Accepted five-component design, 23 reserved roles, gates, assets, and acceptance rules | Accepted source design, implementation remains partial |
| `FALLOUT_ORIENTATION_LIVE_LEDGER_TRANSACTION_PROOF.md` | Current schema-3 live-ledger and state-result boundary | Current proof, with repair and caller blockers |
| `FALLOUT_ORIENTATION_RESOURCE_PILOT_EVENT_PROOF.md` | Dormant events `70` through `73` and resource pilot limits | Current partial implementation proof |
| `FALLOUT_ORIENTATION_GOVERNMENT_PILOT_EVENT_PROOF.md` | Dormant events `74` through `77` and government pilot limits | Current partial implementation proof |
| `FALLOUT_ORIENTATION_CLOSURE_EVENT_PROOF.md` | Dormant events `82` through `84` and authenticated cleanup limits | Current partial implementation proof |
| `events/fallout_world_end_events.txt` | Source evidence for defined event ids | Defines `62` through `65`, `70` through `77`, and `82` through `84`. It does not define `66` through `69` or `78` through `81` |
| `BLOCKERS_AND_DECISIONS.md` | Parent-facing blocker and decision ledger | Reconciled in this pass |

## Plan and handoff disposition

| Document or tranche | Disposition | Reason |
|---|---|---|
| `FALLOUT_EVENT_SCHEDULER_NUMERICAL_CONTRACT_PROPOSAL.md` | Promoted and implemented dormant | User approval is recorded on 2026-07-18. The values are implemented behind the two unset activation flags and earn no event credit |
| `FALLOUT_EVENT_SCHEDULER_PROOF.md` | Current evidence | Records deterministic review lanes, receipts, caps, fail-closed gates, and the absence of content callers |
| `FALLOUT_ASH_WEEK_ORIENTATION_CONTRACT_PROPOSAL.md` | Accepted and queued in part | The complete contract remains authoritative. Fifteen blocks have dormant implementation evidence, while eight blocks and the required gates remain unresolved |
| `FALLOUT_ORIENTATION_RESOURCE_PILOT_EVENT_PROOF.md` | Implemented dormant pilot | Events `70` through `73` exist with no caller, no logs, no details, no package receipt setter, and no release credit |
| `FALLOUT_ORIENTATION_GOVERNMENT_PILOT_EVENT_PROOF.md` | Implemented dormant pilot | Events `74` through `77` exist with no caller, no approval setter, no logs, no details, and no release credit |
| `FALLOUT_ORIENTATION_CLOSURE_EVENT_PROOF.md` | Implemented dormant closure package | Events `82` through `84` exist with authenticated cleanup and no caller, logs, details, or release credit |
| `fallout_scheduler_numerical_contract_implementation_2026-07-18.md` | Retained as supporting handoff | Its implementation evidence remains useful. The current scheduler proof and this handoff supersede its old summary of the parent blocker ledger |
| `fallout_ash_week_unaccepted_proposal_reconciliation_2026-07-18.md` | Historical approval record, status claims superseded | Its approval history remains valid. Its old claim that no orientation event or asset exists is superseded by the pilot and asset proofs |
| `fallout_orientation_pilot_audit_2026-07-18.md` | Historical partial audit, count claims superseded | Its caller, matrix, candidate, log, detail, and runtime blockers remain relevant. Later pilot proofs supersede its old `4 of 23` implementation count |
| `fallout_orientation_transaction_substrate_2026-07-18.md` | Historical substrate handoff, event surface claims superseded | It remains evidence for the transaction substrate. Later pilot proofs supersede its old statement that events `66` through `84` are all absent |

No plan was rejected. The unresolved work remains queued because the accepted
caller and activation gates require reviewed data and implementation surfaces.

## Contradictions resolved

- B9 no longer says that fatigue mutation, decay, scoring, queue limits, or
  deterministic review are absent. They are implemented behind dormant gates.
- B9 no longer says that candidate selection itself is absent. The numerical
  selector exists, while reviewed candidate production, content callers, and
  event definitions remain absent for the ordinary living-world scheduler.
- B9 now states the hard caps of three major arcs, eight delayed rows, and six
  bilateral rows per participant.
- B12 no longer says that no orientation event, localisation, or asset exists.
  It records the fifteen defined dormant blocks and six dedicated report
  sprites while preserving the missing caller, missing matrix coverage,
  missing candidate package, missing logs, missing details, and zero count.
- B9 explicitly retains the 25-point human-owned war or mission relevance
  blocker, the active-siege receipt blocker, the atomic major-arc and
  relationship reservation blocker, and the pair-memory compaction blocker.

## Contradictions still open

- The accepted orientation contract opens with approval-time language saying
  that no implementation exists. Later pilot proofs record partial
  implementation. The contract is treated as historical approval boundary,
  while the pilot proofs and B12 are the current implementation ledger.
- Six report-event assets are delivered and registered, but the character or
  institution candidate package and complete asset coverage remain absent.
- The dispatcher contains reserved routes for `66` through `69` and `78`
  through `81`, while the corresponding event definitions remain absent.
- Historical handoffs still contain old no-event or old count wording. They
  are not active implementation instructions and are listed above as
  superseded status evidence.

## Remaining unresolved blockers

- `fallout_event_scheduler_activation_approved` and
  `fallout_event_scheduler_active` have no setter.
- Suffixes `100` through `126` remain undefined typed reservations and are
  uncounted. The living-world release floor remains `0 of 660`.
- No Hearts of Iron IV runtime or save, multiplayer, popup, callback, or
  engine persistence proof exists.
- Literal lobby-host authority remains unproven. The project coordinator is
  deterministic but is not a documented lobby-host predicate.
- Major-arc and relationship candidates remain fail-closed until reviewed
  rows freeze complete atomic class and reciprocal reservation payloads.
- The accepted 25-point human-owned war or mission relevance case remains
  fail-closed because no typed relationship receipt exists.
- Active-siege recurrence remains fail-closed because no typed current-siege
  producer receipt exists.
- Pair-family memory is not an atomic reciprocal reservation and does not yet
  have deterministic expiry compaction.
- No reviewed candidate producer or ordinary living-world content caller
  exists. Hidden AI result callers and content-owned cleanup callers are also
  absent.
- Ash-week orientation coverage remains incomplete. Eight of 23 event blocks,
  96 of 108 matrix cells, capital repair, resource package installation,
  government-row approval, character or institution registry installation,
  candidate assets, the orientation caller, event-log rows, event-detail rows,
  and final audits remain unresolved.

## Stale prompt and duplicate-document check

- No prompt file was named by the parent or found in the named authority set.
- The prior approval handoff and pilot audit remain useful historical records,
  but their old status claims must not be used to plan duplicate event or asset
  work.
- No duplicate current source specification was created or modified.

## Recommended parent decisions

1. Keep both activation flags unset and keep every reserved scheduler suffix
   outside release-floor accounting.
2. Treat `FALLOUT_EVENT_SCHEDULER_PROOF.md` and the current README as the
   scheduler status authority, with this reconciled B9 as the blocker index.
3. Treat the three pilot proofs and current event source as evidence of
   partial Ash-week implementation, not as approval to wire a caller.
4. Resolve the remaining matrix, candidate registry, capital repair,
   package-install, event-log, event-detail, and audit surfaces before any
   orientation caller or scheduler activation review.
5. Keep literal host authority and runtime observation as explicit blockers.

## Validation performed

- Compared the updated B9 and B12 text with the current scheduler proof,
  numerical contract, README, orientation contract, live-ledger proof, three
  pilot proofs, closure proof, and the current event source.
- Confirmed the current event source defines fifteen orientation blocks and no
  event definitions in scheduler suffixes `100` through `126`.
- Confirmed the current proof set records six dedicated report sprites, no
  orientation caller, no scheduler activation setter, no event-log rows, no
  event-detail rows, and a living-world count of `0 of 660`.
- Confirmed no changed handoff text uses an em dash or semicolon.
- No HOI4 executable was run. No MCP lint pass was claimed. No workbook or
  runtime validation was in scope for this documentation-only reconciliation.

## Parent follow-up

The parent should review the two changed documentation files, then continue
from the unresolved gates above. No gameplay completion claim is supported by
this handoff.
