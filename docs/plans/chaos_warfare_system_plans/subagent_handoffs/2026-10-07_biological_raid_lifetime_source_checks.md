# Biological raid caller-lifetime source checks

Disposition: implemented bounded independent regression, pending parent review.
Acceptance basis: the parent assigned tests for the frozen biological caller-storage repair following the audit, caller map, and patch handoff.
All three named handoffs/maps were read.
The parent owns gameplay, MCP evidence, integration, and the commit.

## Artifacts and final result

The source regression owns these three artifacts:

- `docs/testing/2026-10-07_biological_raid_lifetime_source_tests.js`
- `docs/testing/2026-10-07_biological_raid_lifetime_source_results.json`
- This handoff.

The parent-authorized evidence-portability follow-up also added `docs/testing/2026-10-07_biological_raid_lifetime/.gitattributes` and the five exact frozen source copies under `docs/testing/2026-10-07_biological_raid_lifetime/after/common/scripted_effects/`.
Existing before snapshots, manifests, gameplay, and shared Git attributes were not edited.

Run from the mod root:

```powershell
node docs/testing/2026-10-07_biological_raid_lifetime_source_tests.js
```

The portability-adjusted final run at `2026-10-07T16:43:44.299Z` exited 0 with 150 passing cases and `passed_conservative_bounded_source_model`.
It preserves all 149 original coverage cases and adds one line-ending acceptance/substantive-drift rejection case.
It reproduces 68 baseline value/branch failures and five baseline reset-ownership failures.
The existing Event 026 strict-frame VM and parser were imported unchanged.
No doctrine/HQ test suite, shared VM, gameplay, index, or commit was edited.

The JSON retains hashes, numeric source inputs and returned outputs, scope-specific state/history records, selected fixed draw branches, selector captures, and explicit fixture limits.
Its `callerCoverage` records 16 paired reset/dispatch callers, five raid owners covered here, and eleven untouched other owners.
The eleven are a separate follow-up and are not reported fixed or validated by this tranche.

## Patch preservation

The independent test checks all five raw before/after archive hashes against the insertion manifest.
Removing exactly the manifest's 63 literal declarations at 19 original offsets from the raw after archives reconstructs the raw before bytes and AST exactly.
The counts are battlefield 25, strategic 16, sabotage 19, lifecycle 2, and biological diplomacy caller 1.
Every original statement, random body/weight, target/policy gate, event call, history branch, and floor in those five source files retains its order and text.
The generic diplomacy classifier is preserved, and only its biological caller receives the new output storage.
The byte-exact reconstruction also protects the eleven-consumer inventory's spread helper inside the shared lifecycle file.
It does not establish execution coverage for the other consumers.

The exact frozen revisions remain those in `docs/testing/2026-10-07_biological_raid_lifetime/insertion_manifest.json`, with baseline commit `c0f14281546a4b8f38a07349b752bfbd65e4c55d`.
No new tuning, payment, refund, outcome draw, replay mechanism, state target, or reward floor is introduced by the repair.

### Immutable evidence and Git line endings

The source snapshots contain mixed CRLF/LF, and ordinary Git text conversion would invalidate the frozen byte hashes and insertion offsets on a clean checkout.
The evidence directory's local `.gitattributes` marks only `before/**` and `after/**` as `-text`, preserving those archives byte-for-byte in Git.
The five after copies match the original insertion manifest's frozen after SHA-256 values exactly.
The insertion proof uses those archived raw bytes rather than relying on a working checkout's line-ending policy.

Current gameplay continues to supply every parsed resolver, helper, and lifecycle body executed by the tests.
Its equality check against the frozen after archive permits only CRLF-to-LF conversion.
It does not normalize indentation, ordinary whitespace, comments, tokens, numbers, or statements.
The explicit portability case accepts in-memory LF and CRLF versions of each frozen file and rejects an added substantive Clausewitz declaration.
Substantive current-source drift still fails before functional coverage can be claimed.

Read-only `git check-attr text` confirmed `unset` for all ten raw before/after paths.
For each path, `git hash-object --no-filters` matched `git hash-object --path=<archive>`.
Those checks did not stage the real index, write an object with `-w`, or create a commit.
The result JSON records the evidence attributes path, raw-archive contract, normalized-current contract, and retained coverage counts.

## Meaningful exercised cases

| Coverage | Source proof |
| --- | --- |
| Four agents, four battlefield outcomes | Actual resolver retains required/consumed payload 50/25/25/10 and weaponization 1.25/1.60/0.95/2.10 after the returning getter. Limited/success/critical result mappings reach the actual stored agent record, accepted history, and humanitarian branch |
| Four agents, six strategic fixed outcomes | Failure selects failed delivery or attacker accident, success selects hidden or detected release, and limited/critical retain their direct outcome. Selected outcomes survive both nested selection and outer resolver return, and history records the exact native reservation amount |
| Four agents, four sabotage outcomes | Nested parameter helpers and their outer adapter retain agent, required payload 10/12/10/8, support 40/50/40/60, consumed amounts, selected result, program fields, and accepted state/actor history |
| 36 sabotage program cases | Readiness 40/60/80 and attribution 0/40/200 use actual program arithmetic and constants, verifying exact weaponization bands and concealment cap |
| Five reset owners | All 35 residual reset fields have surviving caller storage and exact default values after actual reset return. Before source loses ownership for those fields. Numeric zero absence alone is not called a visible failure |
| Failed evidence and visibility | Fresh, matching, and stronger-other-actor leads exercise actual battlefield and sabotage evidence helpers. Resolver-owned match status survives state return. A matching existing evidence lead produces stronger visibility than the before missing-output case |
| Seed acceptance and rejection | Existing cursor 99 survives rejected dispatch. A stale supplied receipt is reset to missing before a rejected repeat, state intensity remains unchanged, and the existing failure-history branch runs |
| Two retaliation return boundaries | Generic country retaliation history persists in both versions. Before biological episode status becomes none after the lost return. Revised episode status and classifier outputs survive generic-to-biological and biological-to-dispatch returns |
| Agent selector and post-store consumers | All four accepted agents reach actual incubation selector entry. Active existing episodes reach the detection hook with the correct selector. The before unowned selector is read as zero after store return |
| Native marker bridges | Actual bridge immediate bodies reject missing/duplicate agent/outcome markers and wrong actor identity. Three valid exact-one controls reach lifecycle dispatch |
| Context rejection | Explicit false native-context fixtures prevent seed dispatch in all three resolvers. These are fixture gate outcomes rather than full controller/policy evaluations |

The actor country, victim country, exact target state, attacker handling state, and friendly state use separate regular-variable maps.
Temporary values remain unscoped, and the imported helper-frame cleanup controls their lifetime.
Native events and outcome markers are supplied as fixed source probes, with no stochastic probability claim.

## Duplicate behavior

The actual lifecycle store body is exercised, including numeric meta record keys.
Repeated accepted battlefield dispatch increases the existing agent intensity and increments its repeated-seed count.
The returned seed status is therefore a caller receipt, not a replay guard.
The actual sabotage existing-episode guard rejects the second same-agent release and preserves the first intensity.
These are source-model results and do not establish whether the engine invokes a native callback twice.
No replay mechanism was added or proposed as part of these tests.

## Model boundaries and unsupported behavior

### High-priority incubation timing question

The `battlefield-resolver-anthrax-2` trace captures `state_event = cbrn_bio_lifecycle.1` with `days = 0`, while the actual incubation getter has returned 5 and the stored due day is 15 from fixture day 10.
This does not derive from omitted route/agent/finalizer fixtures.
The actual source in `biological_lifecycle_effects.txt:660-680` owns all three incubation getter outputs and initializes `bio_incubation_days` to zero before its meta effect.
The expanded text calls `bio_lifecycle_prepare_incubation_delay` at line 672, writes the resulting regular due day, then uses `[BIO_INCUBATION_DAYS]` in the event at line 675.
The meta argument at line 679 refers to `bio_incubation_days`.
Under this harness's eager argument substitution, that argument is captured before the getter executes and remains zero in the event token.
The real getter body at lines 635-658 changes the existing caller-owned output to 5, so this is not another demonstrated unowned getter-output return.
The JSON records both the current getter output and due day alongside the event capture, and adds `highPriorityTimingQuestion` explicitly.
Native meta/localization argument evaluation timing remains unresolved, and incubation timing is not marked passing.
This exact source-order concern needs a separate timing-semantics review and must not be dismissed merely as a model discrepancy.
No implementation change was made or recommended as part of this caller-storage tranche.

The real three resolvers, five release/reset owners, payload/result selectors and validators, failed-evidence bodies, actor-history bodies, lifecycle dispatcher, episode store, sabotage episode guard, and numeric retaliation classifiers run from parsed source.
Native context/policy/controller validity and seed-record validity are explicit fixtures.
Route/agent preparation and finalization outputs are fixed fixtures, so complete potency, intensity, share, evidence, reward-floor arithmetic, and legal gate correctness are not numerically established.
Their original source remains protected by exact byte/AST equality.

Numeric meta templates are substituted only for the supported tested arguments.
Event requests and selectors are captured, not scheduled by HOI4.
Native meta evaluation timing, actual incubation delays, detection results, later lifecycle/protection/death ticks, saved-target persistence, and native reservation collection remain unproved.
Unified deliberate-use history, air contributions, integrated command recovery, humanitarian/UWR hooks, and the condemnation sink are named stub boundaries.
The adapter branches and regular episode/actor records leading to them are exercised separately.

The harness rejects native payment/refund commands rather than performing them.
No equipment, fuel, or CP is debited or refunded.
The native raids skill and installed raid documentation retain essential equipment as the engine-owned payment path.
No source test is treated as proof of native collection, cancellation, refund, or callback cardinality.

Reference paths, line spans, and revisions are in the JSON: offline Data structures 435-443, installed `save_event_target_as` 6496-6504, installed raid documentation 167-184, 245-300, and 547-557, and vanilla land-infiltration callbacks 169-184.
The parent owns MCP inspection and comparison, and no additional MCP/probability call, game launch, or log search was performed here.

No gameplay fallback or simplification was implemented.
Fixture substitutions are explicit validation limits and cannot be promoted into whole-biological-service or live-engine completion.
Skills used: `chaos-redux-events`, `chaos-redux-native-raids`, and `chaos-redux-subagents`.
No skills were changed.
The source test artifacts are frozen for parent rerun and review, and no chemical work was started.
