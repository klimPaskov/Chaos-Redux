# Event 012 survivor settlement implementation — 2026-10-03

Acceptance basis: the user's complete Gods-of-Africa goal, full spec 1083–1105 requiring every surviving participant, and the authorized instruction to choose recommended bounded implementation options without another input round.
The parent accepts the census/history/independent-receipt method in `012_africa_gods_survivor_victor_design_2026-10-03.md`.
Its separate bilateral victor re-legitimation proposal is accepted and queued next, after this coverage repair; full grading and reward scaling remain separately outstanding.
Disposition: implemented and independently reviewed in source, pending the scoped commit and native/MCP acceptance.

## Coverage and implementation

New `common/scripted_triggers/012_africa_gods_settlement_triggers.txt` provides history proof, a one-time endpoint commit gate, four-standing validation, and a receipt predicate independent of live participation.
New `common/scripted_effects/012_africa_gods_settlement_effects.txt` coordinates one participant's grading, reward, finalization, and `.608` receipt under that proof.
Its matching Markdown file documents scope, normal inputs/outputs, defaults, side effects, direct-call guards, lineage, cleanup, usage, assets, and validation limits.

The host's final pass traverses the maintained `gods_of_africa_candidate_registry` and uses the same authoritative settled-phase/continental endpoint.
It includes existing historically enrolled countries after archival, capitulation, loss of major status, or later special/nonhuman conversion.
It excludes vanished objects, never-enrolled census entries, and self-transfers to the current host.
No new world discovery pass or timer is added.

The independent audit found that the previous fixed 640 insertion cap could permit genuine enrollment outside the only final traversal.
The owner replaced that arbitrary boundary with the actual native country-array cardinality, checked against actual deduplicated candidate/live array sizes, and made candidate membership a prerequisite of enrollment.
The registration helper attempts candidate insertion before its guard, including direct callers; the callback delegates to that same transaction.
Both arrays are unique subsets of native `global.countries`, so an absent native object always has a physical slot and successful enrollment cannot fall outside its durable final-pass coverage.
The unused `max_participants` constant is removed; demand budgets and cadence are unchanged.
Installed dynamic variables `974–976` define the array as all countries including nonexistent objects; offline Data structures `1072,1113–1118` defines `array^num` and explicitly demonstrates `global.countries^num`.
The malformed-standing direct-reward issue also found by the audit is closed with the same four-value validator before consuming the reward receipt.
The independent narrow follow-up confirms both S1–S2 source defects resolved against the documented native collection contract and final source snapshots.

Genuine enrollment stamps owner ID and original Event 012 host origin when absent and preserves them on re-entry.
Current-generation proof retains an existing country-local history/generation contract when stamps are absent; a present owner/origin stamp must match.
Successor restoration copies exactly the staged old generation and origin into two normal inherited-history fields alongside its transferred candidate census.
Inherited proof requires the participant's present origin and exact inherited generation; no less-than-generation rule or arbitrary origin rebinding is used.

The existing grading helpers require historical proof, preserve their existing thresholds and priority, and treat durable permanent opt-out as defiance.
Grading records settlement generation, origin, historical generation, Strength, and doctrine before public cleanup.
Grading, reward, and finalization each guard their own direct calls.
The existing reward-granted receipt remains one-use.
Reciprocal infantry equipment now uses native `send_equipment` to the captured recipient, preserving actual donor variants; fuel and common-defence ledger quantities and affordability gates remain unchanged.
Existing political-power alternatives and opinion rewards are retained here rather than presented as newly approved full-spec balance.

Finalization withdraws owned protection, removes missions and transient payment/punishment/review state, remembers permanent opt-out, and clears live participant authority.
It preserves final standing, outcome, reward, and history proofs.
The receipt carries regular `gods_of_africa_settlement_host` and requires its final-commit proof and matching generation/origin, independently of the global host's subsequent replacement.
Acknowledgement clears pending presentation only and never changes an unrelated host's live array or count, durable outcome, reward receipt, or conduct ledger.
The existing explicit terminal helper closes the full owner census when its continental flag is valid; three English strings describe that same behavior.

## Meaningful review cases

The independent audit is `012_africa_gods_survivor_settlement_audit_2026-10-03.md`.
Required cases are a live participant, an archived capitulated survivor, a later-converted historical object, zero-conduct first enrollment, a vanished object, a never-enrolled census candidate, exact inherited origin/generation, wrong owner or origin, and a wrong historical generation.
Replay cases cover duplicate endpoint/grading/reward/finalization calls, repeated `.608` acknowledgement, a new global host pointer, and direct calls before the authoritative endpoint.
Accounting cases preserve the existing Favored/Respected amounts, native donor stock and fuel checks, the common-defence decrement, one-time receipt, and unchanged political-power branches.
These are source/scenario acceptance requirements, not reported native executions.

## Source references and coupled evidence

The architecture handoff retains exact installed/offline paths, line spans, hashes, and the native array/host-transfer precedents read for this method.
Installed `documentation/effects_documentation.md:4296–4310` documents scope-array iteration; `6083–6092` mission removal; `6550–6557` native equipment transfer; regular-target persistence is covered by the saved-event-target sections and parallel offline Data structures sections in the architecture handoff.
Installed effects revision: `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Offline Data structures `1147–1156,1210–1256` revision: `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Native `COG_scripted_effects.txt:197–213` uses the same country-object scope-array pattern.
Current host succession is explicitly one-use in `common/scripted_triggers/012_africa_host_transfer_triggers.txt:4–14` and restores its origin/generation from exact staging in `012_africa_host_transfer_effects.txt:1129–1140`.

The current mobile constant groups depend on committed schema correction `16664b3a4`; the initial source traversal did not validate that engine schema.
The mobile AI handoff records agent-client route absence; the parent separately started a correctly named narrow `gods_of_africa_comply_demand` inspect and claims no numeric result until delivery.
One earlier parent inspection used a wrong decision ID and was cancelled before receiving evidence; it is not a valid AI baseline.
The lifecycle MCP handoff records successful detailed mission removal, narrower event timeouts, and pending source/compare/reference follow-ups.
No full event-graph, native inventory, live presentation, clean error.log, or weighted balance claim follows from those source-only checks.

## Assets, omissions, and outstanding work

`.608` reuses its existing registered `GFX_report_event_012_africa_gods_settlement` image in `interface/012_africa_event_pictures.gfx`.
No new GUI, image, DDS, icon, portrait, model, decision row, currency, or public meter is introduced.
This repair does not simplify historical eligibility to live-demand eligibility.
Native allocation timing, country-object and delayed-event lifetime, and inherited histories without origin proof remain explicit acceptance questions.
The accepted full-history grading factors, capability/contribution reward scaling, victor exemption/renewal, complete AI evidence, and user-owned native acceptance remain outstanding.
The whole Gods goal remains incomplete.
