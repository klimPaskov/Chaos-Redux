# Event 012 survivor settlement audit, 2026-10-03

## Concrete findings

**S1: successful direct enrollment is not guaranteed to enter the only final-settlement traversal.**
`common\scripted_triggers\012_africa_gods_triggers.txt:122–131` refuses candidate insertion when `gods_of_africa_candidate_count` reaches 640.
The separate enrollment predicate at `175–188` checks live roster capacity, not candidate membership or successful candidate insertion.
`common\scripted_effects\012_africa_gods_effects.txt:377–393` attempts candidate insertion and then independently calls registration when that enrollment predicate passes.
Registration at `310–361` creates genuine history/generation/origin/owner proof and live membership without proving candidate-array membership.

The concrete conditional source scenario is a committed active host with completed census, candidate count 640, live participant count below 640, and an eligible major/player outside both arrays.
Candidate insertion fails, enrollment succeeds, and the actor has a genuine initialized ledger outside `gods_of_africa_candidate_registry`.
Final settlement at effects `3450–3474` traverses only that candidate array.
It omits the actor even if still live, and also omits it after subsequent archival because archival does not repair candidate insertion.
Host cleanup empties the live array and resets its counters without evaluating this omitted actor or issuing its receipt.
This is an actual permissive source path, not an assertion that a supplied campaign already reached the cap.
No runtime evidence establishes the maximum possible population of ordinary, dynamic, recreated, or copied country objects.
The previous count of defined tags is not proof that this source path is unreachable.

Parent action: establish durable final-pass coverage for every successful genuine enrollment, including the insertion-cap boundary, and verify that archival retains that coverage.
Do not resolve the accepted all-survivor requirement by silently dropping an enrolled actor, inventing a world scan, or presenting the 640 cap as a proven engine population limit.
The exact bounded storage/capacity repair remains parent-owned.

**S2: direct reward invocation can consume its one-use receipt for an invalid standing.**
`gods_of_africa_grant_settlement_reward`, effects `3037–3104`, requires a standing variable at `3043`, but does not call the available four-value validator.
Given otherwise valid history, committed host/outcome flags, no reward receipt, and a standing outside favored/respected/distrusted/enemy, it sets `gods_of_africa_settlement_reward_granted` at `3047`.
None of its grant branches then matches, so the one-use receipt is consumed without a valid settlement grant policy.
Missing standing is rejected, but present malformed standing is not.
The normal current grader always writes one of the four enums, so this is a direct-helper malformed-input gap rather than a claim of an observed ordinary-path failure.
Direct guards are explicitly in scope, and the accepted architecture's reward preflight requires a final enum at design `312`.
The finalizer and receipt already use `gods_of_africa_final_settlement_value_is_valid`.
Parent action: require the same valid-standing proof before any reward-receipt mutation, then confirm invalid standing leaves that receipt absent.
No reward amount, threshold, or balance target needs to be chosen by this audit.

## Scope, acceptance, and disposition

This is a bounded read-only survivor-coverage and accounting audit against `012_africa_gods_survivor_victor_design_2026-10-03.md` and the parent's explicit accepted all-surviving-participant contract.
The recommendation to use historical proof, one exact inherited generation/origin, frozen receipt host, and separate acknowledgement is parent-accepted within that scope.
The design handoff and pertinent full-spec settlement passages were read.
The new `2abe5b406` participant/ROOT skill rule was read and applied, with host-owner ROOT retained in the existing targeted decision and explicit participant targets used for transfers.
Only this new handoff was written.
No gameplay, other docs, skills, assets, workbook, Git index, commit, or HOI4 launch was changed or performed by the auditor.
Mobile and L1–L3 were not re-audited.

| Bounded surface | Status | Source finding and acceptance limit |
| --- | --- | --- |
| Existing enrolled live, capitulated, minor, or converted census actors | Source coverage confirmed | Historical predicate omits live/major/capitulation/special-country gates |
| Every successfully enrolled actor | Partial | S1 prevents an unconditional all-survivor completion claim |
| Current-history and exact inherited-lineage proof | Source-present | Exact comparisons and optional owner check, with missing inherited-origin migration limit below |
| Four-way grading, commit guard and snapshots | Source-present | Existing threshold/order preserved, regrading closes on committed outcome |
| Reward resource accounting and direct call guard | Partial | Matched native debit policy and one-use flag, but S2 malformed enum gap |
| Finalization and live participant flag removal | Source-present for processed actors | Historical/direct guard and no new membership or enrollment manufactured |
| `.608`, frozen host proof, acknowledgement and replay | Source-present | Acknowledgement changes only pending presentation, with native target/object lifetime unconfirmed |
| Manual settlement action | Source-present owner-wide dispatch | Existing host targeted decision invokes the final pass, with three English strings aligned |
| Required MCP/engine evidence | Unconfirmed | No validated current artifact or native scenario claimed |

Disposition: accepted survivor architecture is implemented in substantial source form, with S1–S2 outstanding at this snapshot and required MCP/native acceptance unconfirmed.
The survivor tranche is not source-complete while those findings remain.
Bilateral victor renewal is explicitly accepted and queued by the parent for the next tranche.
Broader final grading ratios, streaks, campaign support, reward scaling, and victor/militia work remain separately queued and are not claimed implemented by this review.
No plan is promoted, rejected, silently disposed, or replaced by a simplification here.

## Historical proof and registry boundaries

`common\scripted_triggers\012_africa_gods_settlement_triggers.txt:5–37` requires an existing country, a valid committed current host, exclusion of the host itself, initialized history or a history-count variable, and stored participant generation.
If `gods_of_africa_history_owner_id` is present, it must equal `THIS.id`.
The current-generation branch uses equality, allowing an absent legacy origin but rejecting a present incompatible origin.
The inherited branch requires present participant origin, exact equality to the transferred old generation, equality to inherited origin, and equality to current host origin.
There is no broad less-than-generation ancestry gate.
There is no new participant flag, re-enrollment, major-rank requirement, or non-capitulated requirement in this predicate.
An initialized zero-count ledger therefore qualifies on the same provenance terms as one with conduct entries.
Unenrolled candidates, nonexistent actors, wrong owner IDs, wrong generations, and incompatible origins fail.

Origin and owner are stamped only inside genuine registration at core effects `334–341`, and existing values are retained rather than rebound.
`common\scripted_effects\012_africa_host_transfer_effects.txt:68–71` stages the old host's exact origin and generation.
Successor commit at `1138–1140` sets the staged origin and increments the staged old generation.
The two new restore lines at `468–469` copy the exact old generation and origin from global staging into the successor's inherited-history proof.
Candidate array/count/census restore remains the existing bounded transaction at `467–481`, with staging at `115–120,737–740`.
This is a one-generation source contract and does not prove engine country-object copying or slot lifetime.

**Explicit migration limit:** an already archived historical ledger without an origin stamp cannot pass the strict inherited branch after succession.
It can still pass the documented legacy current-generation branch while generation matches.
No absent inherited origin was inferred or written at settlement to manufacture ancestry.
Coverage of such unstamped inherited records is unresolved unless the parent can supply or derive authorized provenance through an existing genuine owner transaction.
This is an intentional fail-closed proof boundary, not acceptance that the all-survivor migration obligation has disappeared.

## Grading, finalization, and accounting traces

`gods_of_africa_commit_final_settlement`, core effects `3450–3474`, requires the existing active-host proof and either settled Scramble phase or continental completion flag.
It commits the host endpoint before traversing candidates, closes ordinary response authority through that flag, processes history, records the milestone, and calls system cleanup.
The history helper requires only the committed host rather than live participant authority.
`gods_of_africa_commit_participant_settlement`, new effects `5–18`, saves a regular `gods_of_africa_settlement_host` in host scope, grades, rewards, finalizes, marks pending receipt, and fires `.608` for the current participant scope.

The grader at core effects `3008–3031` has its own `settlement_can_commit` guard, snapshots settling generation/origin, participant history generation, host Strength and doctrine, then writes enemy/favored/respected/distrusted and commits outcome.
Snapshots occur before the owner's final cleanup sets global Strength to zero at `3497`.
The three standing predicates at core triggers `910–956` use settlement history proof and durable permanent opt-out.
An opted-out actor therefore grades Enemy even when host-loss cleanup removed live defiance.
The existing threshold, doctrine and outcome order are retained.
Full-spec grading depth is separately queued, not proven by these retained classifiers.

The reward helper retains the existing favored/respected package constants and existing PP branches.
It marks a one-use reward receipt before its transaction branches.
For a supported physical package it saves the actual participant target, enters the explicit host, and uses native `send_equipment` for favored/respected infantry at `3060` and `3084`.
The recipient is not inferred from ROOT.
The same host scope initializes the nominal fuel debit before the existing `remove_fuel_from_stockpile = yes` and reduces the common-defense infantry reserve by the matching infantry amount.
Participant fuel credit remains unchanged at `3065` and `3089`.
Host stock, fuel and reserve preflights remain per recipient, so later recipients may reach the existing PP policy when earlier recipients consume finite resources.
No replacement equipment grant or reward in acknowledgement is added.
Native sender/receiver variant selection, fuel clamping/headroom, and exact retention by capitulated receivers remain unobserved, and paired nominal fuel effects are not claimed as proof of native retained quantity.

Finalization at `3208–3307` has its own historical/committed/valid-standing/host-final proof.
It withdraws owned protection, removes missions and live payment/reconciliation/punishment/offer state, retains durable history/outcome/reward proof, and clears the live participant flag.
It does not add archived actors to a live array or decrement participant membership/count for each historical recipient.
The owner finally clears the live arrays and zeros live counters once at `3480–3508`.
Its priority-offender decrement still depends on the remaining enemy flag, which ordinary archive/cleanup clears, and repeated finalization clears that flag on its first call.
No source observation of cloned stale offender state is asserted.

## Receipt, manual action, and replay scenarios

`.608` at `events\012_africa_gods_of_africa.txt:138–154` calls the dedicated receipt predicate, not the live generation/array predicate.
Receipt proof at new triggers `57–71` requires existing recipient, committed outcome, pending receipt, a valid standing, generation/origin snapshots, and an existing frozen regular host whose final commit and generation/origin match those snapshots through PREV.
The global `africa_host` pointer is not consulted by that receipt predicate.
The regular target is carried into the report event according to the local target-lifetime reference.
Replacing the global pointer alone therefore does not redirect the source receipt proof.
A deleted or changed frozen host fails that proof rather than borrowing a successor's authority.
Actual country-object and queued-event lifetime remain U3-style runtime limits.

Acknowledgement at core effects `3309–3314` clears only `gods_of_africa_settlement_report_pending` after receipt validation.
It does not clear standing, committed outcome, reward receipt, history, membership, or counters.
Replay after acknowledgement fails pending proof and charges nothing.
Duplicate final owner invocation fails the committed/active-host gate.
Duplicate per-participant grading/commit fails the committed-outcome gate, while duplicate reward fails its one-use receipt.
Direct grading/finalization mutations are within their own if/limit blocks, rather than escaping the intended wrapper because of indentation.
S2 remains the direct invalid-standing exception to reward input validation.

The existing targeted decision at `common\decisions\012_africa_gods_decisions.txt:987–1040` has host ROOT and participant FROM.
Its caller enters FROM, then the changed manual helper at core effects `4274–4283` enters `event_target:africa_host` and invokes the owner-wide final pass when continental completion is present.
ROOT remains the decision-taking host, satisfying `africa_is_current_host`'s documented source ROOT check at `common\scripted_triggers\012_africa_triggers.txt:431–440`.
This trace does not assume that merely entering host scope changes ROOT in an unrelated caller context.
The three updated English settlement strings describe the owner-wide action and persistent standing.
An archived actor does not need a new live flag to be processed by that pass.

| Named source scenario | Result and limit |
| --- | --- |
| Live versus archived capitulated enrolled census actor | Same retained history is eligible for the retained grader, with no live/major/capitulation gate introduced |
| Zero-conduct actor later losing major status | Count-variable presence, including zero, proves initialized enrollment rather than no history |
| Unenrolled, absent, self, converted, wrong-owner actor | Unenrolled/absent/self/wrong-owner rejected. A still-existing genuinely enrolled converted actor remains eligible |
| Exact inherited generation and origin | Accepted only on the one staged old-generation lineage. Unrelated older or unstamped-origin ancestry rejected |
| Candidate cap with room in live roster | S1 allows genuine enrollment outside the final census and skips that actor at settlement |
| Duplicate grading/reward/final pass | Committed outcome and reward flags prevent another normal debit or standing rewrite |
| Invalid direct reward standing | S2 consumes reward receipt without a matching valid-standing branch |
| Pointer succession before `.608` acknowledgement | Receipt uses its regular frozen host and snapshots, acknowledgement never edits the new host's registry |
| Several physical rewards exhausting reserve | Native source debit and reserve decrease occur per matching recipient in order, with existing PP policy thereafter. Native execution/caps unconfirmed |

## Validation, evidence limits, and documentation

The new helpers and touched settlement bodies were manually read with exact scope/call-site traces.
A temporary read-only lexical/block parse of both new files and the core effects file established four new trigger definitions, one new effect definition, and enclosing if/limit structure around grading, reward and finalizer mutations.
That parser checked source structure, not installed command semantics or engine execution.
No parser script or scratch file was written, and no source change was made.
No new weighted choice or AI weight was audited here, and the separately owned `chaosx_ai_probability_auditor` retains changed-eligibility evidence before AI/full-goal claims.

The parent owns its source-lookup retries, `.606` pending requests, and receipt validation.
This audit also dispatched narrow read-only `.608` trace/state render/comparison and event reference context/search requests without waiting for slow client receipts.
Bounds were depth 1, one node and one trace edge, with no helper expansion, no HTML and no rendered comparison.
No final current revision, valid event graph/comparison, artifact URI, detailed helper coverage, or engine acceptance from those requests was observed before this handoff.
No prior artifact header was treated as validated content.
Pending or unobserved receipts are not proof of missing server routes or server failure.
No helper-expansion mode, native task, job operation or service-health claim was used without negotiation.
Mandatory MCP evidence remains unconfirmed, and source review is not equivalent evidence.

The parent is creating settlement contract documentation and owns canonical documentation alignment.
The new source has overview comments and live call sites, and the unchanged decision assets are reused.
No asset production, new GUI action, world scan or clock was introduced in this bounded tranche.
Missing all-survivor coverage must remain disclosed in docs until S1 is resolved.
No contract document existence or implemented label is promoted to completion proof by this audit.

## Exact local references read

Installed relative paths below are under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
The hashes identify the complete local file revision, while the cited spans identify what was read.

| Reference | Read spans | SHA-256 |
| --- | --- | --- |
| Installed `documentation\triggers_documentation.md` | 2708–2715 existence, 3352–3359 capitulation, 5672–5684 exact membership | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation\effects_documentation.md` | 4296–4310 scope-array iterator, 6496–6503 regular target save, 6550–6557 native equipment send | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `events\AAT_Finland.txt` | 3722–3735 exact native archetype/amount/target transfer structure | `363c53751ed2fbe113fbed5635940f4494b5c67f3bfa0a3787aa327f6cdfda13` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263–283 target distinction, 303–314 regular lifetime, 1243–1269 loop/PREV and country objects | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 260–263 ROOT/current scope/PREV/FROM | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Offline `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | 145–147 triggered-event and trigger re-evaluation rules | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |

The local `remove_fuel_from_stockpile` body at `common\scripted_effects\chaosx_dynamic_effects.txt:810–813` confirms caller amount negation and native add_fuel, with the new reward caller reinitializing its debit before each use.
No native fuel retention/clamping result is inferred from that helper.

## Reviewed source snapshot and recommended next actions

| Mod-relative source | SHA-256 |
| --- | --- |
| `common\scripted_triggers\012_africa_gods_settlement_triggers.txt` | `f64d2a3f76b6a651c2327e1fa4e3352e873f96d1c544d98deab55f9372982611` |
| `common\scripted_effects\012_africa_gods_settlement_effects.txt` | `0d636486d9a49ac7d6107b95e02cd2d4a5df4334f2b349a8496361b0f2781046` |
| `common\scripted_effects\012_africa_gods_effects.txt` | `3f077ec6a19d75281710456d2923e6238ef288917149d4977c731123abfb8905` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `f62af649782d8d43aece47b0087a6cdd3fad85246a4efb0a8ec603143b2469af` |
| `common\scripted_effects\012_africa_host_transfer_effects.txt` | `6b752c49ea7e65ebf8c6d25f11e7c313b45a36426045325d934cf6379ef74588` |
| `events\012_africa_gods_of_africa.txt` | `3466bce083f962f23c8be09edeb4808d0150cdec8eb33d5448b48864e0e62a65` |
| `localisation\english\012_africa_gods_l_english.yml` | `07d1fb931199dc4d69b8d9361416cbd5e77292df62f46242256847d2ec4d8010` |
| `common\decisions\012_africa_gods_decisions.txt` | `230f9f22136cda7a6625641ef45e4d14666b846457e2c466656824d2b0d3f8b6` |
| `common\scripted_effects\012_africa_world_order_effects.txt` | `6a9b793ddc2f3998394aa9909706bed61859769cc63ad09bdfe815fc228b6e7a` |

Parent next actions: resolve S1 coverage and S2 direct-reward validation, recheck those exact changed blocks, and retain the strict inherited-origin/country-lifetime and MCP/native limits.
Then record contract documentation and the separate queued bilateral-renewal/full-grading/reward-scaling dispositions before any broader completion claim.
This audit introduces no simplification and reports the two outstanding source gaps explicitly.
Skills applied: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-improvement-loop`, and `chaos-redux-decisions-missions` for the existing manual targeted-action context.
No skill was created or updated.

## Narrow shared-tree update at delivery

**S2 is resolved in source, while S1 remains outstanding.**
This disposition supersedes the earlier S2 outstanding status and reward-input exception, preserving the original finding and snapshot for review history.
During handoff verification, the parent changed core effects, so only the affected reward guard and the S1 enrollment/final-pass blocks were reread.

`gods_of_africa_grant_settlement_reward:3037–3104` now invokes `gods_of_africa_final_settlement_value_is_valid = yes` at line 3043 before setting the one-use reward flag.
The validator admits only the four accepted enums, so an absent or malformed standing cannot consume that flag through this direct helper.
No reward amount or balance target changed in this correction.

`gods_of_africa_participant_can_register:175–188`, registration at `310–361`, direct onboarding at `377–393`, and final pass at `3450–3474` still have the S1 relationship described above.
Successful enrollment is not conditioned on census membership, and the final pass still visits only the candidate census.
No resolution of that coverage counterexample is claimed.

Current core effects SHA-256: `6bba5b42dfdf253476a983924a5a4ab53f99969adfad156c2fc264c3f11a2426`.
The reread core triggers retain SHA-256 `f62af649782d8d43aece47b0087a6cdd3fad85246a4efb0a8ec603143b2469af`.
Final bounded status is partial on survivor traversal coverage, with the direct reward enum guard resolved and required MCP/native/object-lifetime evidence still unconfirmed.
No gameplay, other documentation, skill, index, commit, or engine operation was performed by this update.

## Native-country bound and registration resolution

**S1 is resolved in the revised source, and S2 remains resolved.**
This disposition supersedes the original S1 counterexample, partial traversal status, and recommendation to repair that counterexample.
It does not replace the recorded native/MCP/lifetime or inherited-origin migration limits, and it is not a full Gods or Event 012 completion claim.

The narrow reread confirms these changes:

- `common\scripted_triggers\012_africa_gods_triggers.txt:116–135` requires actual membership in `global.countries` before remembering a candidate, retains deduplication, and compares the host's actual `gods_of_africa_candidate_registry^num` with `global.countries^num`.
- The enrollment predicate at `178–189` requires existing candidate-array membership, rejects duplicate live membership, and compares actual `gods_of_africa_participants^num` with native country cardinality.
- Core registration at `310–363` invokes `gods_of_africa_remember_candidate = yes` before its own enrollment guard. Both direct callers and callbacks therefore establish durable candidate coverage before writing genuine history or live membership.
- Direct onboarding at `379–392` remembers the candidate, then delegates registration without a premature membership precheck. The registration's repeated remember is idempotent through the existing dedup guard.
- Archive at `396–507` and clean-participant at `3107–3201` do not remove candidate rows. The existing final pass at `3449–3473` traverses that durable array, so an actor who was genuinely enrolled and later archived remains within its source traversal.
- Reward at `3036–3103` still invokes `gods_of_africa_final_settlement_value_is_valid` before setting the one-use reward receipt, confirming S2's correction.

The source capacity argument uses the native collection, with no invented numeric physical cap.
Let U be the documented native country array and C the host's unique candidate rows created through the checked insertion or preserved transfer.
Every inserted candidate is an actual U member and deduplication prevents repeated C entries.
For a U member P missing from C, the number of unique C entries is strictly smaller than U's total element count, so the insertion cardinality gate has room under that invariant.
If C reaches U's element count while remaining a unique subset, no U member can be outside C.
Likewise, a candidate absent from the unique live roster has room under the same native bound.
Registration now requires membership after insertion, so even a failed insertion cannot create the original S1 orphaned enrolled ledger.
Candidate count presence remains an existing initialization precondition, but stale scalar count values no longer choose either capacity boundary.
No new array, effect-side world traversal, clock, or blanket discovery pass was added.

The exact references were read directly in this follow-up:

| Native/offline reference | Read rule | SHA-256 |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md:972–976` | `global.countries` is the array of all countries, including nonexistent countries | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:1069–1076` | `arrayname^num` reads total element count and regular arrays persist until explicitly cleared | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| The same offline file at `1111–1118` | Exact `global.countries^num` cardinality expression in the documented resize example | Same revision |

These references support the native collection and count expression actually used.
They do not separately establish engine allocation timing, current-versus-recreated object identity, civil-war inheritance, dynamic-slot ID reuse, or queued-event target lifetime.
The capacity argument is therefore confirmed against the documented collection contract and maintained source invariant, with those native lifetime semantics still unobserved.
No claim is made that the engine has a fixed 640-country physical limit.

The unused `max_participants` constant is absent, and the scoped gameplay search found no remaining reference to that removed key.
Minor documentation follow-up: the timing constants' two comments immediately before `priority_offender_cap` still mention 609 defined tags and revisiting a roster ceiling, which no longer describes the native cardinality bound.
The parent already owns canonical guide/contract/handoff updates and should reconcile those retained comments as part of that documentation pass.
This is a stale comment, not a remaining enrollment/settlement coverage defect.

| Current source revision captured in the narrow reread | SHA-256 |
| --- | --- |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `85cc9eb47dd15888547cc81c064a64812c3ea2b794360c89ee41a54153ee21d8` |
| `common\scripted_effects\012_africa_gods_effects.txt` | `089f8578096a8c7f9d906f50596340b653aebd12a63187547f805ced5477627a` |
| `common\script_constants\012_africa_gods_constants.txt` | `4d334d7aaec415996b2839dc73891febf8a25400b5a46b4c2636d0726e3b7786` |
| `common\scripted_triggers\012_africa_gods_settlement_triggers.txt` | `f56c45b8813807be97f69f72af3ea05e97cbffc7529febd4a19c8856f3dfd4d1` |
| `common\scripted_effects\012_africa_gods_settlement_effects.txt` | `0d636486d9a49ac7d6107b95e02cd2d4a5df4334f2b349a8496361b0f2781046` |
| `common\scripted_effects\012_africa_host_transfer_effects.txt` | `6b752c49ea7e65ebf8c6d25f11e7c313b45a36426045325d934cf6379ef74588` |

The current settlement-history predicate was also reread and now explicitly requires host-origin presence, retaining its previous exact current/inherited comparisons and owner-proof policy.
No new blocker was found in these narrow changes.
The reported S1–S2 source defects are resolved, while parent documentation cleanup, strict inherited-origin migration limits, and native/MCP acceptance remain separately recorded.
Only this audit handoff was appended, with no gameplay, other documentation, skill, index, commit, or HOI4 operation by the auditor.
