# Event 027 native transaction audit, 2026-10-03

Disposition: source audit implemented, native transaction acceptance blocked by missing observed engine evidence.
Authority is the current bounded parent request, which requires exactly one event mastery step, preserved native bank, and empty-track selection only after local engine evidence.
Only this handoff is changed.
Gameplay, queues, achievements, AI weights, and shared workspace edits remain parent-owned.

## Conclusion and owner actions

The installed documentation establishes point addition and branch assignment, but does not establish a safe exact-level transaction.
The current adapter cannot be called verified merely because its registry initialized.
The owner corrected the documented filter mismatch during this audit.
Separate registry readiness from transaction acceptance and keep unsupported transactions unavailable until their evidence exists.
Do not enable empty-track assignment as a substitute for proving its banking sequence.

1. **Documented syntax defect, resolved by concurrent owner edit:** `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt:17143-17164` is the representative loop.
   At baseline revision `55d96a...`, all 107 `add_mastery` blocks passed `track_index`, while the installed effect schema and offline wiki document `index`.
   Final source review at revision `275a35...` found zero `track_index` fields and 107 documented `index` fields, retaining `folder`, `sub_doctrine`, and track-type filters.
   `set_sub_doctrine.track` is a different field and correctly takes the numeric folder index, so do not rename that field.
   Whether the engine rejects or ignores the undocumented field is unresolved, and no executed parser result is claimed.
2. **Verification gate defect:** `common/scripted_triggers/027_doctrine_research_triggers.txt:4181-4207` equates native verification, empty-track verification, and mastery transaction verification with `doctrine_research_adapter_registry_initialized` and, for one wrapper, a built-in domain identity.
   `common/scripted_effects/027_doctrine_research_effects.txt:24-95` sets registry readiness while building registry arrays, without proving native transactions.
   Keep readiness separate from an evidence-backed adapter capability gate, separately for active mastery and empty-track selection.
   The parent must decide release disposition within the explicit user contract, and must not treat a newly set flag as evidence.
3. **Mutation before proof:** the loop at `exact_mastery_effects.txt:17145-17163` adds one point repeatedly until observed level reaches the expected level or 1,000 iterations expire.
   It neither measures the native bank nor computes the exact next-threshold deficit.
   A delayed readback, wrong filter, rejected gain, or unexpected level jump leaves native mutations possible before success fails.
   The caller at `027_doctrine_research_effects.txt:2436-2471` quarantines ambiguous results, but provides no native mastery rollback.
   Quarantine prevents uncertain replay and does not prove that the failed choice had no gameplay effect.
   Preserve ambiguous receipt evidence, prohibit blind retries, and require native transaction proof before mutation.
4. **Empty adoption is already reachable without the required evidence:** `exact_mastery_effects.txt:19711-19728` assigns a branch, reads its resulting level, and then runs the loop.
   The rebase after assignment is the right intended order for distinguishing native progress from the event step, but the documented API does not guarantee that banked rewards finish resolving before this immediate read.
   `exact_mastery_effects.txt:21625-21647` only rejects the completion edge when the selected track remains empty.
   A nonempty track alone does not positively prove the requested branch was assigned and completed.
   The native-completion result should require exact branch identity and a positive completion check, as well as an evidence-backed assignment capability.
   The parent owns receipt recovery and choice consumption changes.

## Documented semantics and their limits

Paths below use `GAME = C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV` and `REPO = C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
All repository-relative citations resolve under REPO.

| Reference and lines | Established rule | Limit |
| --- | --- | --- |
| `GAME\documentation\effects_documentation.md:1477-1502` | `add_mastery` is country-scoped point addition to all matching tracks. Missing filters pass. `track` means track type, and `index` means zero-based index within the folder. | No direct level setter, exact-deficit operation, gain scaling, bank preservation, or synchronous readback guarantee is described. |
| `GAME\documentation\effects_documentation.md:7774-7802` | `set_sub_doctrine` unlocks and assigns the branch. Default assignment finds the first matching track. Extended `track` selects an index among all folder tracks. | Purchase charging, replacement behavior, bank conversion timing, and rollback are not specified. |
| `GAME\documentation\triggers_documentation.md:4181-4196` | `has_mastery_level` tests reached reward count for a subdoctrine. | No track/folder index or native mastery balance is exposed by this documented trigger. |
| `GAME\documentation\triggers_documentation.md:4163-4178,3526-3538` | `has_mastery` checks at least a point amount on any track of a type. `has_completed_subdoctrine` means ever completed, even after switching. | Neither supplies an exact selected-track bank balance or a current track-qualified completion proof by itself. |
| `GAME\common\doctrines\subdoctrines\_documentation.md:3-5,27-42` | Activation starts automatic rewards. Each reward can override the mastery requirement. | The reward-unlock algorithm is explicitly a TODO in the installed document. |
| `GAME\common\doctrines\tracks\_documentation.md:20-23` | Track `active` gates selection and mastery gain, including banking. | This is not a banking preservation or settlement-order specification. |
| `GAME\common\defines\00_defines.lua:25,4687-4688` | Native loop cap is 1,000. Default mastery per reward is 100.0. | Neither value proves exact transaction behavior. |
| `GAME\history\countries\GER - Germany.txt:753-769` | Vanilla selects native doctrines and branches, then adds fixed mastery amounts filtered by subdoctrine. | This is setup source, not an exact one-step or banked-track test. |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:2508-2542,2577-2585` and `paradox_wiki/Doctrine modding - Hearts of Iron 4 Wiki.md:31-47` | Offline snapshot agrees on filter spelling, assignment indexing, and reward-count terminology. | No banking settlement algorithm is supplied. |

Do not copy vanilla's fixed point grants or experience rewards into Event 027.
No technology helper, experience grant, active replacement, or mastery dump is recommended.

## Helper and lifecycle recommendations

Retain the existing country-scoped entry points `doctrine_research_apply_mastery`, `doctrine_research_apply_empty_track_mastery`, and `doctrine_research_capture_transaction_level`.
Their inputs are the selected domain, Grand Doctrine, track, and subdoctrine IDs, and their outputs are success, observed/post level, and native-completion status.
Native doctrine state is their material side effect, and receipt finalization remains owned by `doctrine_research_confirm_selection`.
No new helper without a direct call site is needed, and the existing generic dynamic-effects files contain no native mastery helper to reuse.

Separate the invariant one-level reward from mastery-point increment tuning.
`common/script_constants/027_doctrine_research_constants.txt:35-39` sets maxima, point increment 1, loop limit 1,000, and scan limit 20.
The point increment is also used as the expected level delta at `exact_mastery_effects.txt:21033-21035` and receipt recovery at `027_doctrine_research_effects.txt:2366-2368`.
Changing point granularity must never change the promised one-level reward.
The adapter scans levels 1 through 20 and defaults to zero, so future unsupported branches need explicit coverage rejection rather than a capped value presented as exact.
The `@` point literal mirrors a global constant, and installed constants documentation only promises support in explicitly supported fields.
The comment claiming a specific engine rejection of `constant:` is not independently established by this audit.

Keep native bank untouched and avoid temporary bank removal or synthetic regrant.
Keep country-owned durable receipt data, with post-assignment native level recorded separately from the pre-assignment state where needed for attribution.
No event target or recurring world scan is needed for this bounded transaction.
Preserve ambiguous evidence until the parent resolves it, rather than clearing or replaying the native mutation.
Migrate the existing verification wrappers in place, retain the owner's corrected filter fields, update matching helper docs, and then review direct callers against the same capability gates.

## What supplied observations would still need to establish

No save or observer-run native transaction evidence was supplied to this auditor, and HOI4 was not launched.
Source and offline MCP analysis cannot establish synchronous reward readback, point scaling or rounding, exact bank retention, free assignment, immediate native Milestone activation, or save-boundary atomicity.
For any later supplied before/after saves, use `chaos-redux-save-inspection` and compare exact country, folder index, selected branch, raw mastery/bank, reward level, XP, remaining choices, and receipt state.
Required cases are active low/middle/final rewards, fractional residual mastery, empty track with zero/partial/multiple-level/completing bank, ambiguous Special Forces track identities, and interrupted receipts with external native progress.
A save pair alone may not identify synchronous intra-block order or distinguish unrelated combat/sharing gains without controlled provenance.
These are acceptance gaps, not requests to launch the game or permission to invent a fallback.

## Evidence and validation

Read current AGENTS.md, the events and subagents skills, and all 16 files in `docs/specs/027_doctrine_research_specs/`.
Relevant contract citations are core part 1 lines 141-158, choice-flow part 2 lines 125-152 and 368-380, and goal prompt line 5.
Inspected installed docs and vanilla source, matched all 107 native point-addition helpers against the documented filter schema, and traced the receipt caller's success, native-completion, and ambiguous branches.
No gameplay tests, probability audit, GUI review, full doctrine-domain audit, or source comparison for an implementation patch is claimed.
No gameplay implementation or design simplification was made.

MCP tool discovery confirmed reference context/search/read, source lookup, event inspection, and technology inspection routes.
`hoi4.tech_inspect` with `mode = explain`, `technologyId = mobile_infantry`, and `maxNodes = 12` failed with `timed out awaiting tools/call after 600s`.
No doctrine artifact, coverage result, runtime result, or standalone viewer verification was delivered by that call.
The missing doctrine inspection is an exact MCP blocker, and the installed-file audit above is source evidence only.
`hoi4.reference_search(query = add_mastery, limit = 8)` returned `OK` for workspace `mod_chaos_redux_ea3b2d67c2c0`, six citations, zero skipped sections, and no artifact URI.
Its installed-document citation ID is `7ba4d670991af373b74e3d8ebfd56f2a806f8d6b56e068a593e131c3713fff9e`, lines 1477-1504, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Its offline Effects citation ID is `4584c7bc57fd3aabb0696f8dcf57f6dccab3d7584b74527bdd958dbbc11dd204`, lines 2508-2586, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
The returned reference inventory reports installed docs and wiki available, with the separate `script_doc` source kind unavailable.
These are reference lookup results, and the detailed installed and wiki sections were also read directly from their local files.
The later `reference_search(query = set_sub_doctrine, limit = 8)`, `reference_context(surface = technology, limit = 6)`, and `source_lookup(symbol = mobile_infantry)` calls each failed with `timed out awaiting tools/call after 600s`.
`event_inspect(mode = trace, selector = { kind = event, eventId = chaosx.nr27.1 }, maxDepth = 3, maxNodes = 20, maxEdges = 30)` also timed out after 600s, without a graph artifact or coverage result.
Two initial selector-shape validation failures were corrected before that accepted-schema request, and are not event-source diagnostics.
No MCP helper expansion, task negotiation, job control, render, comparison, or live-engine result is claimed.
`reference_read` for the cited offline Effects ID and revision returned `OK`, with lines 2514-2543 read and `nextLine = 2544`.
Its returned body confirms `add_mastery.index` and extended `set_sub_doctrine.track`, and delivers no artifact URI.
The remaining relevant lines were read locally, so that continuation is not claimed as MCP coverage.
All issued MCP calls have final results inspected, with no outstanding call or helper continuation.

### Byte revisions

Git HEAD at audit start: `f48758822b294aeed4c179868e27fddf6abab93d`.
The shared worktree is dirty, so the following SHA-256 byte revisions identify the audited source instead of assuming HEAD contains it.
Concurrent owner changes to receipt finalization were preserved, and the caller citations were refreshed against the later revision listed here.
The parent must recheck citations if concurrent edits change these hashes.
The exact-mastery file's baseline and owner-corrected revisions are both retained below.

| Source | SHA-256 |
| --- | --- |
| `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`, baseline | `55d96a1ee5bfcebf854d248f7ee36c64890eab68bf46acffaf763149992ee177` |
| `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`, owner correction | `275a35f60e063d8e45d394341ef6cf9ed12079f40f80fc374f3743e6e09f42d5` |
| `common/scripted_effects/027_doctrine_research_effects.txt` | `db2ebfae400a4fc56acb1988e9dec548a8a9865fd31d190cf1a5c603ac2c8fa6` |
| `common/scripted_triggers/027_doctrine_research_triggers.txt` | `cfbc55eccd114d3c388cad23d3cc87d8904152b032c325af567be1ce894b23a3` |
| `common/script_constants/027_doctrine_research_constants.txt` | `69f7412d01047d19638b49a215db03847c8d7bade0b68a0dada563f8b0220c1b` |
| `GAME\documentation\effects_documentation.md` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| `GAME\documentation\triggers_documentation.md` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| `GAME\common\doctrines\subdoctrines\_documentation.md` | `81dcc8e9565e16050c269220c7a706ec894bb5b22712ecabfcb598e1fb671df0` |
| `GAME\common\doctrines\tracks\_documentation.md` | `7b34cc7f2ac59fd7cdb2dd6c9fa87d6d683db2d2b71eea176b690bdb6d6b2ec8` |
| `GAME\common\defines\00_defines.lua` | `405a24ce579815443cafe052cff1361e20c712ca8182e3f10ccbf45330dd4be4` |
| `GAME\history\countries\GER - Germany.txt` | `5e903c2b485b48d8bba38adbe0b6fd5cadc868df4a575d526a1ef2dac4ab66d7` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| `paradox_wiki/Doctrine modding - Hearts of Iron 4 Wiki.md` | `125456f6380fac4ebe0b04cfa8c9fab9bbd26d8db54ec08fe697e31a9641c3ee` |
| `docs/specs/027_doctrine_research_specs/027_doctrine_research_spec_part_1_core.md` | `9946de19c50cc35ba2ac4052ed651ebfe921d31826ab7983250f23358910970e` |
| `docs/specs/027_doctrine_research_specs/027_doctrine_research_spec_part_2_choice_flow.md` | `d4d7abeafdf97ee81148feba77ebe3f94e9643ed9f2777ee261e4515574bdbdd` |
| `docs/specs/027_doctrine_research_specs/027_doctrine_research_goal_prompt.md` | `14de56c7b21a1193a6abd436319b96e0da0a05c79f332688bee6a74cce84faf3` |
