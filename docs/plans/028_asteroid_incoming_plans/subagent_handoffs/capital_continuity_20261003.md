# Event 028 capital continuity handoff

Disposition: implemented in bounded source with parent wrapper integration complete, while native/probability acceptance remains unresolved.
Parent integration: both legacy wrapper bodies now invoke the supplied helpers before physical destruction.
The parent re-ran all seventeen source cases successfully and aligned the board preflight with a distinct fully controlled backup while retaining eligible contested centers.
The source-only planned-fragment follow-up and its validation are included below.
Acceptance basis: the explicit parent assignment authorizes the complete Event 028 spec, specifically Part 2 capital continuity and Part 10 original-target achievement and capital/annexation acceptance.
The parent retains final integration, completion, and commit ownership.

## Owned changes

- `common\scripted_effects\028_asteroid_incoming_capital_effects.txt` adds four event-owned helpers documented below.
- `common\scripted_effects\028_asteroid_incoming_effects.txt` removes the generic owner/controller capital-count increment and its temporary input, then calls the exact-recipient aggregator inside the existing deduplicated state aggregation.
- This handoff documents the helper contracts, tuning, source scenarios, migration, reference revisions, and blocked evidence.

No runtime effects, triggers, events, settings, UI, asset, workbook, AI weight, cost, country identity, leader, focus, radiation, or map file is edited by this worker.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or modified.
These helpers belong to Event 028 and are documented here rather than added to the shared dynamic-effect registry.
The existing `chaosx_dynamic_effects.txt` and corresponding Markdown registry were inspected before design.

## Helper map

| Helper | Scope and inputs | Outputs and defaults | Side effects and call sites |
| --- | --- | --- | --- |
| `asteroid_incoming_score_backup_capital_candidate` | State within the selector's `every_owned_state`. PREV is the moving country. Regular `asteroid_incoming_backup_capital_country` and locked-state targets required. | Unscoped temporary `asteroid_incoming_backup_capital_score`, initialized to the existing base score. No caller-supplied numeric defaults. | Temporary arithmetic only. Called by `asteroid_incoming_select_surviving_capital`. |
| `asteroid_incoming_select_surviving_capital` | Existing country, exact locked-state target, completed main-footprint arrays and matching state ring/transaction records. | Clears and selects global `asteroid_incoming_backup_capital_state`. It remains absent if no candidate qualifies. | Saves a regular country target, computes temporary ranks, selects one deterministic candidate. Called by the relocator and the parent-owned legacy selector wrapper. |
| `asteroid_incoming_relocate_current_capital` | Any scope, invoked after footprint planning and before main-state destruction. Requires locked-state target and active transaction identity supplied by the parent flow. | Existing global capital-country and backup targets, relocation-complete or relocation-failed flags, successful exact-recipient state receipt. No current capital at the locked coordinate produces a zero receipt and no complete/failed flag. | One transaction-local country scan, one native `set_capital` for the exact current country, existing country relocation flag, original-target-only replacement pointer. Parent-owned legacy relocation wrapper must call it. |
| `asteroid_incoming_aggregate_capital_relocation` | State inside `asteroid_incoming_aggregate_current_state` before its aggregation-complete marker. Positive receipt, exact recipient pointer, and matching relocation transaction required. | Adds the observed move count to `asteroid_incoming_country_capital_relocated_count` of the recorded existing country only. Absent or stale receipt adds nothing. | Does not add a population/building receipt or increment either country's affected-state count. Its direct call site is integrated in `028_asteroid_incoming_effects.txt`. |

The selector's local capital-candidate predicate rejects the locked center, foreign territory, foreign occupation, partially controlled contested states, empty states, impassable states, wasteland, existing main craters, and historical or processed fragment sites.
It retains the shared meaningful-settlement predicate while distinguishing a fragment flag set during current planning from an already processed site.
A flagged fragment center qualifies only when its state-planned flag, unprocessed status, current transaction ID, exact fragment-center profile, and current fragment-site array membership all match.
Core eligibility is a strict first preference, matching Part 2's requirement to use non-core territory only when no valid controlled core remains.
Within that core class, the preference is outside the main footprint, then surviving Ring 3, Ring 2, and Ring 1.
The score and final internal state-pointer ID tie break apply within a core/safety class.
No valid first candidate is rejected merely because its score is zero or negative.
The internal state pointer ID is documented as distinct from the displayed/history state ID and may be negative.
Determinism is independent of source iterator ordering for the same registered state objects, while pointer stability across engine reload remains native evidence pending.

The scorer preserves the accepted population, VP, industry, infrastructure, railway, supply, core bonus, and enemy-neighbor penalty values.
It adds the existing neighbor-connectivity score when another usable owned and controlled non-center state is directly adjacent, implementing the specified connection preference.
That adjacency is a local preference, not proof of a complete surviving transport path or arbitrary frontline distance.
An enemy-controlled neighboring state retains the existing frontline penalty.
No extra global state/path scan or periodic hook is added.

## Constants and tuning

| Existing constant | Value | Use |
| --- | --- | --- |
| `asteroid_incoming_runtime.target_score_base` | 100 | Candidate score starts here. |
| `target_score_capital` | 40 | Existing core bonus, retained beneath the strict core preference. |
| `target_score_population_large` / `target_score_population_medium` | 30 / 15 | Population above the existing 100k / 25k thresholds. |
| `target_score_victory_point` | 25 | At least one positive-VP province, using the existing bunker-level existence idiom. |
| `target_score_industry` | 15 | Civilian industry above the existing zero floor. |
| `target_score_infrastructure` / `target_score_rail` | 10 / 10 | Infrastructure and railway. The old infrastructure term used the identically valued rail constant. |
| `target_score_supply` | 15 | Supply node. |
| `target_score_neighbor` | 10 | Direct connection to usable remaining owned and controlled territory. |
| `target_score_frontline_penalty` | -30 | Adjacent controller at war with the moving country. |
| `maximum_footprint_ring`, `zero`, `one` | 3, 0, 1 | Safety ranks and count arithmetic. Outside-footprint rank is maximum ring plus one. |

All constants above are reused from `common\script_constants\028_asteroid_incoming_constants.txt` without changing that file.
The file-local `@asteroid_capital_vp_any_bunker_level = -1` mirrors the existing VP-presence test's literal parsing requirement, with no VP magnitude or fortification requirement.
No shared tuning constant or new numeric balance target is introduced.
Main-footprint members lacking a matching current transaction and a valid positive ring record are rejected, rather than assumed safe.
The main footprint is a required caller input and must already have been planned.
When a stronger fragment profile replaces a main-ring record, the existing recorded strongest-profile ring is used conservatively for that member's safety rank.
Current planned and unprocessed fragment centers can serve as capital territory because their existing 50 percent population-loss profile preserves the state.
The shared impact-target predicate remains unchanged and continues to exclude fragment sites for target construction.

## Identity, event targets, and cleanup

`global.asteroid_incoming_target_was_capital` remains the immutable lock-time snapshot for presentation and original-target achievement eligibility.
It no longer decides whether a country needs physical relocation.
The relocator first compares each existing country's documented `capital` pointer to the exact locked state, then checks its actual `capital_scope` for that same state.
This guards entry into `capital_scope` for countries with no matching capital.
The move uses `remember_old_capital = no`, so the destroyed center is not retained as a return capital.
After native `set_capital`, another exact `capital_scope` check confirms the selected backup before any successful receipt is written.

On success, the main state records these persistent values:

| Field | Contract |
| --- | --- |
| `asteroid_incoming_state_capital_relocated` | Observed move count, one after confirmed movement and zero before success. This is the existing aggregation count input rather than a new boolean mechanic. |
| `asteroid_incoming_state_capital_relocation_country` | Exact country pointer captured from PREV while entering the locked state from the moving country. |
| `asteroid_incoming_state_capital_relocation_transaction_id` | Transaction identity, checked by both repeat-call and accounting guards. |

The recipient pointer is intentionally retained with the physical receipt rather than replaced by later OWNER or CONTROLLER lookup.
The state aggregation's existing `asteroid_incoming_state_country_aggregated` marker prevents repeat counting.
A repeat relocation call with a positive same-transaction receipt preserves that receipt and all successful outputs.
Before an unsuccessful or fresh attempt, only the locked state's relocation receipt and existing capital-related global targets/status flags are reset.
The original selected-country pointer, original-target flag, locked coordinate, and lock-time snapshot are never overwritten.

`asteroid_incoming_backup_capital_country` is a regular effect-chain target and clears automatically when that chain ends.
`asteroid_incoming_backup_capital_state` is the existing global selector output and remains covered by the existing transaction cleanup.
`asteroid_incoming_capital_country` identifies the actual current capital country, including an annexer, and is cleared before a fresh relocation attempt.
`asteroid_incoming_replacement_capital_state` is set only when that actual mover is the exact original target, the locked capital snapshot is positive, and original-target annexation has not been recorded.
An annexer can retain the existing generic relocation country flag for reporting, but receives no original-target flag, replacement pointer, or achievement completion flag from these helpers.
An original target that has already moved its capital after lock is left alone unless it again has its actual capital at the locked coordinate at resolution.
The existing original-target-annexed tracking remains parent-owned.

The capital-only aggregator works for the recorded existing recipient even if ownership/control changes have separated it from both physical-loss recipients.
It deliberately changes only that recipient's capital count, leaving report-row creation and physical-loss attribution to the existing parent flow.
Whether such an exceptional non-holder also needs a dedicated report row is a parent presentation question, not an invented gameplay change here.

## Parent migration and remaining work

The parent integrated these legacy wrappers in `028_asteroid_incoming_runtime_effects.txt`:

```txt
asteroid_incoming_select_backup_capital = {
	asteroid_incoming_select_surviving_capital = yes
}

asteroid_incoming_relocate_destroyed_capital = {
	asteroid_incoming_relocate_current_capital = yes
}
```

Keep `asteroid_incoming_process_footprint`'s relocation call before preparedness aftermath and destruction.
The worker did not edit either wrapper or that caller.
The appendix independently verifies both integrated wrapper bodies and their caller order.
The accounting helper already has its direct call site inside the existing state deduplication guard.
No universal owner/controller capital-count fallback remains.

Part 2's contested-state avoidance adds a full-control requirement at relocation.
The parent-owned country viability and exact main-center preflight now require a distinct fully controlled backup while allowing an otherwise valid contested center.
This worker inspected that source and did not modify the parent-owned trigger or runtime files.

If the actual current capital country has no usable backup at resolution, the helper leaves its capital and the locked coordinate unchanged, sets the existing `asteroid_incoming_capital_relocation_failed` flag, and writes no successful count or replacement pointer.
The late ownership/control-change case is unresolved by the accepted spec's pair-construction exclusion alone.
The engine behavior when the parent subsequently destroys that capital cannot be accepted from source evidence.
The worker adds no territory, release, substitute country, redirected impact, or new atmospheric contingency.
The parent must resolve that edge before claiming end-to-end continuity acceptance.
If an engine state permits multiple existing countries to share the exact same actual capital state, the one-recipient receipt assumption also needs native evidence rather than a guessed country-selection rule.

No assets, icons, sprite tokens, or new localisation are needed for these hidden helpers.
No gameplay or visual fallback was introduced beyond the explicitly authorized surviving-ring capital fallback.
Further mechanics or presentation expansion are outside this repair.

## MCP evidence and unsupported acceptance

During the initial repair this architect client's connected `ALL_TOOLS` inventory exposed zero `mcp__hoi4_agent_tools__` coding routes.
The separately exposed Blender HOI4 routes do not provide event, map, documentation, validation, or weighted-target inspection.
Absent required routes: `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.script_validate`, `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.map_inspect`, `hoi4.probability_inspect`, `hoi4.probability_evaluate`, and `hoi4.probability_compare`.
No live coding-route schema, service-health/version result, helper-expansion route, or native task negotiation was available in this architect client during that initial pass.
The source implementation proceeds under the explicit parent's bounded repair authorization, while these required evidence routes remain blocked.

`list_mcp_resource_templates({server: "hoi4_agent_tools"})` returned the artifact template `hoi4-agent://workspace/{workspaceId}/artifact/{sha256}/{provenanceHash}/{name}` with byte-range metadata version 1.
That establishes resource-template availability only.
No relevant generated native artifact URI was supplied or produced for this repair.
No central MCP router, adapter substitution, or wrapper skill was added.

The read-only `chaosx_ai_probability_auditor` was spawned with isolated context as agent `01a10111-bb68-7bd2-b048-114f73292071`.
It received the immutable before sources, this after source, and the named scenarios below.
Its separate client's inventory exposed `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_compare`, and event inspect/render routes, so exposure is client-specific.
A valid `probability_inspect` of `common/scripted_effects/028_asteroid_incoming_effects.txt` failed with the exact error `timed out awaiting tools/call after 600s`.
The live validator confirmed that inspection requires a source object with an identifier, path, inline Clausewitz source, or virtual patch.
A narrower capital-helper inspection and event inspections produced no result before the auditor was instructed to finalize its blocked evidence report.
The auditor did not run evaluate or compare, because no inspected adapter/candidate findings or supported native scenario fixture were available.
It returned no probability/event artifact URI, analyzer revision, comparison ID, or native scenario hash.
It independently confirmed the after capital-helper and aggregation hashes recorded below and made no edits.
Final specialist disposition: probability findings unresolved, with no exact/bounded probability or balance acceptance.
Neither this worker's source-model results nor any score computed from them constitute native or probability acceptance.
HOI4 was not launched.

Immutable before-runtime source: `docs\plans\028_asteroid_incoming_plans\availability_20261003\before\028_asteroid_incoming_runtime_effects.txt`, SHA256 `3662A248017DE946C19BDA1D395D892CB99A8A435B82F06FCDBCF7C0A90CB980`.
The corresponding before trigger SHA256 is `EFA22ACB10085504B65E1C7DF95E47931E2B980D9A3780312CE0B65F885EC08F` and before constants SHA256 is `1403A2F46D41CB7668393C931C10AFC98091697763ADC8C88B786CC773A8EF7E`.
Those identities were checked against the parent record `availability_20261003\repair.md`.
The source scenario appendix runs directly against those before definitions and the actual after helper ASTs.

## Reference evidence

Reference routes were absent, so all sections below were read directly from local files.
Wiki base is the repository's `paradox_wiki\` offline snapshot, with no Paradox web access.
Installed base is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
Revisions are SHA256 hashes of the exact files read.

| Source relative to its base | Relevant line spans | SHA256 |
| --- | --- | --- |
| Wiki `Data structures - Hearts of Iron 4 Wiki.md` | 102-125 state flag scope/lifetime, 263-327 event-target lifetime and identity, 425-478 pointer and temporary-variable scoping, 1667-1675 internal state IDs | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| Wiki `Scopes - Hearts of Iron 4 Wiki.md` | 31-55 iterator contract, 254-270 PREV/capital/event-target scopes, 329-349 invalid-scope guards | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| Wiki `Effects - Hearts of Iron 4 Wiki.md` | 350-363 target effects, 1038-1043 capital movement and old-capital memory, 4683-4697 scripted-effect calls | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| Wiki `Triggers - Hearts of Iron 4 Wiki.md` | 329-346 AND/OR/NOT semantics, 1148-1158 full control, 1827-1863 state/core/ownership/control/building predicates | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| Wiki `Localisation - Hearts of Iron 4 Wiki.md` | 531-536 variable and event-target namespaces | `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064` |
| Installed `documentation\effects_documentation.md` | 2733-2750 target cleanup, 2773-2780 clear_variable, 3840-3856 every_country, 4076-4090 every_owned_state, 6496-6512 target save, 6655-6667 set_capital, 7820-7840 and 7888-7908 variable assignment | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed `documentation\triggers_documentation.md` | 1497-1504 neighbors, 1612-1641 owned-state and VP province filters, 1830-1839 building counts, 2110-2134 variable comparison, 2708-2715 exists, 3844-3851 target availability, 4827-4842 has_state_flag, 5006-5013 has_variable, 5336-5342 capital predicate, 5390-5396 core, 5585-5592 full control, 5672-5684 array membership, 6079-6086 ownership/control, 7561-7568 exact state | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed `documentation\script_concept_documentation.md` | 216-247 Script Constants | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| Installed `common\script_constants\documentation.md` | Full schema and examples | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| Installed `documentation\dynamic_variables_documentation.md` | 180-181 current-country capital pointer | `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA` |
| Installed `documentation\loc_objects_documentation.md` | 172-178 OriginalCapital versus current Capital localisation scopes | `A5D06DA0B42E615FA0C40D0103D9125ED68A7691778E20C0315ACA7C82822C81` |
| Installed `common\scripted_effects\BUL_scripted_effects.txt` | 890-910 owned-core backup and native dynamic PREV capital target precedent | `F523FD6686F22B618A85F4822FA89A1D5F61781C651B08B3C8C89A3D2D8B8CF8` |

Installed set_capital documentation gives a numeric-state example, while the dynamic state-target form is supported by the offline effect reference and the inspected BUL PREV precedent.
The capital pointer precheck, event-target set_capital call, full-control trigger, internal-pointer tie break, and post-move capital_scope result are still engine acceptance pending.
No unrecognized field is treated as a proven runtime capability.

## Source scenario results

The reproducible appendix passed 23 actual-source cases against the immutable before runtime, the frozen pre-follow-up capital helper, and the patched helper/aggregation definitions.
Fixture SHA256: `A6C550CDFAC7A1C6887EA0A264656312D881DC883BF21244FBAEC578097046A6`.
Pre-follow-up capital-helper SHA256: `E9C0FEBDFD97CF5B5495EF9EC4BCC9333776DFBF33AC605F2BE3450D8245CE85`.
After capital-helper SHA256: `A54F762738B32671B3E7A64F87BCF3470989562C41D031822B5B0716504E2D8B`.
After aggregation-file SHA256: `44A5519E86A8E6FCAAF0C681F84ECC77D365383A7CD4092D3D9CB450FAD08A44`.

| Scenario | After source result | Before source result or regression |
| --- | --- | --- |
| `AST_CAP_NORMAL` | Original target moves to controlled core 1001, original replacement pointer set, count one. | Same backup selected. |
| `AST_CAP_ADJACENT_TWO_STATES` | Ring 1 state 1001 is a valid surviving capital. | No backup, because the whole footprint was excluded. |
| `AST_CAP_RING2_OVER_RING1` | Ring 2 state 1002 wins despite Ring 1's larger development score. | No backup, because both were in the footprint. |
| `AST_CAP_CORE_HIERARCHY` | Ring 1 core 1001 beats developed outside-footprint non-core 1002. | Selected non-core 1002. |
| `AST_CAP_OCCUPIED_BACKUP` | Foreign-controlled developed backup rejected, controlled Ring 2 state 1002 selected. | No backup after footprint exclusion. |
| `AST_CAP_CONTESTED_BACKUP` | Partially controlled developed backup rejected, controlled Ring 2 state 1002 selected. | Selected partially controlled 1001. |
| `AST_CAP_ANNEXER` | Actual current country 102 moves to Ring 1 state 1001. Only country 102 receives count one, and no original-target replacement pointer is set. | No move because the original country no longer existed. |
| `AST_CAP_ANNEXER_NEW_CAPITAL` | Actual annexer capital is relocated despite a zero lock-time capital snapshot. | No move because the snapshot was zero. |
| `AST_CAP_MOVED_AFTER_LOCK` | Current capital 1002 remains unchanged. No relocation count, replacement pointer, or failed flag. | Moved the original country's already-surviving capital to 1001. |
| `AST_CAP_OWNER_CONTROLLER` | Owner/current-capital country 101 gets count one, different controller 102 gets zero. Both retain their existing physical-loss receipt flow. | Could not select the surviving Ring 1 backup. |
| `AST_CAP_NO_BACKUP` | Existing failure flag, zero successful moves, no replacement pointer. Foreign and wasteland alternatives rejected. | Also no backup. Late destruction safety remains unresolved. |
| `AST_CAP_TIE_FORWARD` / `AST_CAP_TIE_REVERSE` | Same internal pointer 1001 wins regardless of fixture iterator order. | Reversed order selected 1002. |
| `AST_CAP_STALE_RING` | Stale transaction's Ring 2 record rejected, matching Ring 1 backup selected. | No surviving-footprint fallback. |
| `AST_CAP_NATIVE_MOVE_REJECTED` | A declared native refusal leaves the capital unchanged and produces no successful receipt or achievement pointer. | Selected pointer existed without native post-move confirmation. This fixture is an assumption, not observed engine refusal. |
| `AST_CAP_FRONTLINE` | Equal-rank state away from the declared enemy-controlled neighbor selected. | Same choice, preserving the existing penalty behavior. |
| `AST_CAP_CONNECTED_SURVIVOR` | Equal-rank state with a usable non-center owned neighbor selected. | Picked isolated tied state 1001. |
| `AST_CAP_PLANNED_FRAGMENT_BACKUP` | Sole outside-main backup accepted with current planning metadata, relocation count one, and unchanged fragment coordinates/count. | Frozen pre-follow-up helper rejected it solely because fragment_site was already flagged. |
| `AST_CAP_EXISTING_FRAGMENT_BACKUP` | Historical fragment site rejected, relocation failure retained. | Same rejection. |
| `AST_CAP_PROCESSED_FRAGMENT_BACKUP` | Processed current fragment center rejected despite otherwise matching planning metadata. | Same rejection. |
| `AST_CAP_STALE_PLANNED_FRAGMENT` | Current-looking planned site with stale transaction ID rejected. | Same rejection. |
| `AST_CAP_UNREGISTERED_PLANNED_FRAGMENT` | Planned site absent from the current fragment-center registry rejected. | Same rejection. |
| `AST_CAP_MAIN_CRATER_PLANNED_FRAGMENT` | Main crater rejected even when fragment planning metadata is present. | Same rejection. |

Every successful case also checks same-transaction relocation idempotence, unchanged original target and lock snapshot, exact recipient counting, and repeated state-aggregation idempotence.
Fixture state/country numbers are declared internal model pointers, not real map-state IDs or measured game geography.
The first executable run caught an incorrect test expectation that a native refusal would also clear the selected backup pointer.
The test was corrected to distinguish candidate selection from confirmed movement, preserving the helper's diagnostic pointer on failure.
No gameplay patch was required for that test correction.

## Planned fragment timing follow-up

Acceptance basis: the parent's explicit follow-up requests acceptance of the current incident's survivable planned fragment center while retaining exclusion of existing and processed craters.
The assessment is confirmed by actual source, rather than contradicted by prior processing.
In `events\028_asteroid_impact.txt`, `chaosx.nr28.4` plans the main footprint at line 331, chooses fragment sites at 332, and invokes physical footprint processing at 344.
In `028_asteroid_incoming_runtime_effects.txt`, the accepted fragment loop at lines 831-851 sets fragment_site and current transaction identity before calling the fragment planner.
In `028_asteroid_incoming_effects.txt`, the fragment planner at lines 351-361 supplies the fragment-center profile and records the footprint.
The footprint recorder sets the state-planned flag at line 291 and does not apply the transaction.
The runtime footprint processor calls capital relocation at line 1305 before entering the physical-processing loop at 1308-1319.
Captured read-only source revisions for this order proof: event source SHA256 `CCF37B9EF68C3E49E886136677087824F935B1F965044D1093BA320D5E61E129`, runtime source `965BFB52A640B5F271A3967BC35730E7FF960C0D81E4FF7D0F2312F13E655C67`, footprint effects `44A5519E86A8E6FCAAF0C681F84ECC77D365383A7CD4092D3D9CB450FAD08A44`.
The inspected parent trigger and constant revisions are `D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B` and `E81036C0CFFA3D9830B220AA4BA7E311F14165D40599B990D316F77E470FE157` respectively.
The existing fragment-center population-loss constant is `0.50`.
The appendix verifies the actual caller order, integrated wrappers, planning markers, and absence of transaction-applied writes in those planning blocks.

Follow-up files edited: only `common\scripted_effects\028_asteroid_incoming_capital_effects.txt` and this handoff/test appendix.
No helper identifier, constant, score, cleanup output, event target, planned coordinate, fragmentation exclusion, or fragment count was added or changed.
The new predicate is inline inside the existing selector's state limit, so it does not declare a scripted trigger in the scripted-effects folder.
The follow-up frozen before source is retained byte-for-byte as base64 in the executable appendix and verified against its SHA256 before use.
It can be supplied as decoded `inlineClausewitz` if a responsive comparison route becomes available.
The six additional fragment cases compare directly against those frozen pre-follow-up helper definitions and verify unchanged fragment plan metadata.
The first caller-order assertion needed correction because the footprint recorder begins with a temporary assignment before its if block, and the corrected assertion selects the actual if block by key.
No engine source change was required for that validation correction.
The no-capital-backup-disappeared edge remains unresolved as recorded above.

During this follow-up, coding routes became exposed in this architect client.
The required first narrow `hoi4.probability_inspect` call used `source: {path: "common/scripted_effects/028_asteroid_incoming_capital_effects.txt"}` and returned `timed out awaiting tools/call after 600s` with `isError = true`.
No probability adapter, candidate, comparison, or artifact evidence was produced.
The reference context and initial installed has_state_flag search returned successfully.
The revision-bound reference read, follow-up offline Flags search, and corrected exact event trace each subsequently failed with `timed out awaiting tools/call after 600s` and `isError = true`.
No event graph, lifecycle result, or event comparison artifact was returned.
The context bundle omitted Data structures, Effects, Triggers, Scopes, On actions, and Localisation at limit four, so that bundle alone is not claimed as detailed reference coverage.
The narrow installed reference search located `has_state_flag` at `documentation\triggers_documentation.md:4827-4842`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, citation ID `ce0d60de326c56a95cca74af1dc6f4cc669faefaddb9b5bfa28abb2103ec590e`.
Those lines and the offline Data structures flag section at lines 102-125 were also read directly.
The read-only probability specialist was given the follow-up cases, frozen-before identity, and exact inspect timeout for the evidence pass.
The event trace's live validator requires `selector: {kind: "event", eventId: "chaosx.nr28.4"}`.
Initial incomplete selector forms were rejected before analysis, and the corrected bounded trace uses depth three, twenty nodes, twenty-five edges, and no helper expansion.
The focused trace produced no analysis, and no source-only order proof is treated as full helper lifecycle or engine evidence.
The read-only specialist's follow-up disposition is probability comparison blocked and native/event trace unresolved.
Its interim report mentioned the caller-order assertion while correction was still underway, and the successful final appendix run supersedes that source-validation caveat.
The appendix parses actual source, evaluates a deliberately limited effect/trigger/scoping subset, raises on unmodeled evaluated tokens, and models declared ownership, control, capital, and building fixtures.
It does not execute HOI4, simulate the two-day world, prove engine capital behavior, or supply a probability_compare substitute.

## Parent isolated-commit handoff

The bounded capital follow-up is complete in the worker-owned source and ready for the parent's isolated source-repair commit.
After the parent's compaction resume, the worker rechecked the current helper and reran all 23 source scenarios plus the actual caller-order and integrated-wrapper assertions successfully.
The helper still matches after-source SHA256 `A54F762738B32671B3E7A64F87BCF3470989562C41D031822B5B0716504E2D8B`, and the original recipient-only aggregation source still matches `44A5519E86A8E6FCAAF0C681F84ECC77D365383A7CD4092D3D9CB450FAD08A44`.
No worker gameplay edits remain queued, and no parent wrapper or availability file was edited during this final verification.

The follow-up commit surface is the capital helper and this handoff/test appendix.
The earlier capital repair also owns the narrow recipient-only aggregation change in `028_asteroid_incoming_effects.txt` if that change is still awaiting the parent's repair commit.
No design simplifications were introduced.
Native/probability acceptance and the late no-viable-backup edge remain unresolved, so commit readiness does not establish Event 028 completion.
The parent's current MCP retries remain parent-owned evidence and can supersede the historical timeout records above when actual results are available.
Skills used throughout this bounded repair remain `chaos-redux-events` and `chaos-redux-subagents`.

## Reproducible source scenario appendix

From the repository root, run this single Python appendix without creating another repository file:

```powershell
python -c "from pathlib import Path; p=Path('docs/plans/028_asteroid_incoming_plans/subagent_handoffs/capital_continuity_20261003.md'); t=p.read_text(encoding='utf-8'); exec(t.rsplit('<!-- capital-source-model -->',1)[1].split(chr(96)*3+'python')[1].split(chr(96)*3)[0])"
```

<!-- capital-source-model -->
```python
from pathlib import Path
import copy
import base64
import hashlib
import json
import runpy

root = Path.cwd()
parse = runpy.run_path(str(root / '.tools/validation/validate_028_availability.py'))['parse_source']
prefix = 'asteroid_incoming_'
before_dir = root / 'docs/plans/028_asteroid_incoming_plans/availability_20261003/before'
helper_path = root / 'common/scripted_effects/028_asteroid_incoming_capital_effects.txt'
aggregation_path = root / 'common/scripted_effects/028_asteroid_incoming_effects.txt'

# Exact pre-follow-up helper bytes, frozen in this handoff before the patch.
before_capital_bytes = base64.b64decode('IyBFdmVudCAwMjggY2FwaXRhbCBjb250aW51aXR5LgojIFNlbGVjdHMgc3Vydml2aW5nIHRlcnJpdG9yeSBhbmQgbW92ZXMgb25seSB0aGUgY291bnRyeSB3aG9zZSBjdXJyZW50IGNhcGl0YWwKIyBpcyB0aGUgZXhhY3QgbG9ja2VkIG1haW4gc3RhdGUsIGJlZm9yZSB0aGUgcGh5c2ljYWwgZGVzdHJ1Y3Rpb24gdHJhbnNhY3Rpb24uCiMgRnVsbCBjb250cmFjdHMsIHR1bmluZywgbWlncmF0aW9uLCBhbmQgdmFsaWRhdGlvbiBsaW1pdHMgYXJlIGRvY3VtZW50ZWQgaW4KIyBkb2NzL3BsYW5zLzAyOF9hc3Rlcm9pZF9pbmNvbWluZ19wbGFucy9zdWJhZ2VudF9oYW5kb2Zmcy9jYXBpdGFsX2NvbnRpbnVpdHlfMjAyNjEwMDMubWQuCiMgTm8gb3JpZ2luYWwtdGFyZ2V0IGlkZW50aXR5LCBsb2NrIHNuYXBzaG90LCBvciBhY2hpZXZlbWVudCByZXN1bHQgaXMgY2hhbmdlZC4KCiMgTGl0ZXJhbCBwcm92aW5jZS1idWlsZGluZyB0aHJlc2hvbGQsIG1hdGNoaW5nIHRoZSBleGlzdGluZyBFdmVudCAwMjggVlAgdGVzdC4KIyBBIGJ1bmtlciBsZXZlbCBhYm92ZSAtMSBpbmNsdWRlcyBhIFZQIHByb3ZpbmNlIHdpdGggbm8gZm9ydGlmaWNhdGlvbi4KQGFzdGVyb2lkX2NhcGl0YWxfdnBfYW55X2J1bmtlcl9sZXZlbCA9IC0xCgojIFNUQVRFIFNDT1BFIGluc2lkZSB0aGUgY2FsbGluZyBjb3VudHJ5J3MgZXZlcnlfb3duZWRfc3RhdGUuCiMgT3V0cHV0OiB1bnNjb3BlZCB0ZW1wb3JhcnkgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfc2NvcmUuCiMgSW5wdXRzOiB0aGUgcmVndWxhciBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9jb3VudHJ5IGV2ZW50IHRhcmdldC4KIyBVc2VzIGV4aXN0aW5nIEV2ZW50IDAyOCBzY29yZSBjb25zdGFudHMsIHdpdGggbm8gcmFuZG9tIHJvbGwgb3Igc3RhdGUgbXV0YXRpb24uCmFzdGVyb2lkX2luY29taW5nX3Njb3JlX2JhY2t1cF9jYXBpdGFsX2NhbmRpZGF0ZSA9IHsKCXNldF90ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zY29yZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUudGFyZ2V0X3Njb3JlX2Jhc2UgfQoJaWYgPSB7IGxpbWl0ID0geyBpc19jb3JlX29mID0gUFJFViB9IGFkZF90b190ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zY29yZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUudGFyZ2V0X3Njb3JlX2NhcGl0YWwgfSB9CglpZiA9IHsgbGltaXQgPSB7IHN0YXRlX3BvcHVsYXRpb25fayA+IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3RhcmdldC5sYXJnZV9wb3B1bGF0aW9uX2sgfSBhZGRfdG9fdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfc2NvcmUgPSBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ19ydW50aW1lLnRhcmdldF9zY29yZV9wb3B1bGF0aW9uX2xhcmdlIH0gfQoJZWxzZV9pZiA9IHsgbGltaXQgPSB7IHN0YXRlX3BvcHVsYXRpb25fayA+IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3RhcmdldC5tZWRpdW1fcG9wdWxhdGlvbl9rIH0gYWRkX3RvX3RlbXBfdmFyaWFibGUgPSB7IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3Njb3JlID0gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfcnVudGltZS50YXJnZXRfc2NvcmVfcG9wdWxhdGlvbl9tZWRpdW0gfSB9CglpZiA9IHsgbGltaXQgPSB7IGFueV9wcm92aW5jZV9idWlsZGluZ19sZXZlbCA9IHsgcHJvdmluY2UgPSB7IGFsbF9wcm92aW5jZXMgPSB5ZXMgbGltaXRfdG9fdmljdG9yeV9wb2ludCA9IHllcyB9IGJ1aWxkaW5nID0gYnVua2VyIGxldmVsID4gQGFzdGVyb2lkX2NhcGl0YWxfdnBfYW55X2J1bmtlcl9sZXZlbCB9IH0gYWRkX3RvX3RlbXBfdmFyaWFibGUgPSB7IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3Njb3JlID0gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfcnVudGltZS50YXJnZXRfc2NvcmVfdmljdG9yeV9wb2ludCB9IH0KCWlmID0geyBsaW1pdCA9IHsgaW5kdXN0cmlhbF9jb21wbGV4ID4gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfdGFyZ2V0Lm1pbmltdW1fYnVpbGRpbmdfbGV2ZWwgfSBhZGRfdG9fdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfc2NvcmUgPSBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ19ydW50aW1lLnRhcmdldF9zY29yZV9pbmR1c3RyeSB9IH0KCWlmID0geyBsaW1pdCA9IHsgaW5mcmFzdHJ1Y3R1cmUgPiBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ190YXJnZXQubWluaW11bV9idWlsZGluZ19sZXZlbCB9IGFkZF90b190ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zY29yZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUudGFyZ2V0X3Njb3JlX2luZnJhc3RydWN0dXJlIH0gfQoJaWYgPSB7IGxpbWl0ID0geyByYWlsX3dheSA+IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3RhcmdldC5taW5pbXVtX2J1aWxkaW5nX2xldmVsIH0gYWRkX3RvX3RlbXBfdmFyaWFibGUgPSB7IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3Njb3JlID0gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfcnVudGltZS50YXJnZXRfc2NvcmVfcmFpbCB9IH0KCWlmID0geyBsaW1pdCA9IHsgc3VwcGx5X25vZGUgPiBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ190YXJnZXQubWluaW11bV9idWlsZGluZ19sZXZlbCB9IGFkZF90b190ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zY29yZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUudGFyZ2V0X3Njb3JlX3N1cHBseSB9IH0KCWlmID0gewoJCWxpbWl0ID0gewoJCQlhbnlfbmVpZ2hib3Jfc3RhdGUgPSB7CgkJCQlhc3Rlcm9pZF9pbmNvbWluZ19zdGF0ZV9pc192YWxpZF90YXJnZXQgPSB5ZXMKCQkJCWlzX293bmVkX2FuZF9jb250cm9sbGVkX2J5ID0gZXZlbnRfdGFyZ2V0OmFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX2NvdW50cnkKCQkJCU5PVCA9IHsgc3RhdGUgPSBldmVudF90YXJnZXQ6YXN0ZXJvaWRfaW5jb21pbmdfbG9ja2VkX3N0YXRlIH0KCQkJfQoJCX0KCQlhZGRfdG9fdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfc2NvcmUgPSBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ19ydW50aW1lLnRhcmdldF9zY29yZV9uZWlnaGJvciB9Cgl9CglpZiA9IHsKCQlsaW1pdCA9IHsKCQkJYW55X25laWdoYm9yX3N0YXRlID0gewoJCQkJQ09OVFJPTExFUiA9IHsKCQkJCQlleGlzdHMgPSB5ZXMKCQkJCQloYXNfd2FyX3dpdGggPSBldmVudF90YXJnZXQ6YXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfY291bnRyeQoJCQkJfQoJCQl9CgkJfQoJCWFkZF90b190ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zY29yZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUudGFyZ2V0X3Njb3JlX2Zyb250bGluZV9wZW5hbHR5IH0KCX0KfQoKIyBDT1VOVFJZIFNDT1BFLiBSZXF1aXJlcyBsb2NrZWRfc3RhdGUgYW5kIHRoZSBjb21wbGV0ZWQgbWFpbi1mb290cHJpbnQgcGxhbi4KIyBPdXRwdXQ6IGdsb2JhbCBiYWNrdXBfY2FwaXRhbF9zdGF0ZSwgYWJzZW50IHdoZW4gbm8gdXNhYmxlIGJhY2t1cCBleGlzdHMuCiMgT3JkZXJlZCBwcmVmZXJlbmNlOiBjb3JlLCBzYWZldHkgKG91dHNpZGUgZm9vdHByaW50ID4gcmluZyAzID4gMiA+IDEpLCBzY29yZSwKIyB0aGVuIGxvd2VzdCBpbnRlcm5hbCBzdGF0ZSBwb2ludGVyIElELiBDb3JlIGFuZCBzYWZldHkgY2Fubm90IGJlIG91dHNjb3JlZC4KIyBPY2N1cGllZCwgY29udGVzdGVkLCBlbXB0eSwgaW1wYXNzYWJsZSwgY3JhdGVyLCBhbmQgd2FzdGVsYW5kIHN0YXRlcyBhcmUgcmVqZWN0ZWQuCmFzdGVyb2lkX2luY29taW5nX3NlbGVjdF9zdXJ2aXZpbmdfY2FwaXRhbCA9IHsKCWNsZWFyX2dsb2JhbF9ldmVudF90YXJnZXQgPSBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zdGF0ZQoJc2F2ZV9ldmVudF90YXJnZXRfYXMgPSBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9jb3VudHJ5CglzZXRfdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfYmVzdF9jb3JlID0gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfcnVudGltZS56ZXJvIH0KCXNldF90ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9iZXN0X3NhZmV0eSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUuemVybyB9CglzZXRfdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfYmVzdF9zY29yZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUuemVybyB9CglzZXRfdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfYmVzdF9pZCA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUuemVybyB9CgkjIEluaXRpYWxpemUgdGhlIHNjb3JlIGluIHRoaXMgY2FsbGVyIGJlZm9yZSB0aGUgc2NvcmluZyBoZWxwZXIgbW9kaWZpZXMgaXQuCglzZXRfdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfc2NvcmUgPSBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ19ydW50aW1lLnplcm8gfQoJaWYgPSB7CgkJbGltaXQgPSB7IGV4aXN0cyA9IHllcyBoYXNfZXZlbnRfdGFyZ2V0ID0gYXN0ZXJvaWRfaW5jb21pbmdfbG9ja2VkX3N0YXRlIH0KCQlldmVyeV9vd25lZF9zdGF0ZSA9IHsKCQkJbGltaXQgPSB7CgkJCQlhc3Rlcm9pZF9pbmNvbWluZ19zdGF0ZV9pc192YWxpZF90YXJnZXQgPSB5ZXMKCQkJCWlzX293bmVkX2FuZF9jb250cm9sbGVkX2J5ID0gUFJFVgoJCQkJaXNfZnVsbHlfY29udHJvbGxlZF9ieSA9IFBSRVYKCQkJCU5PVCA9IHsgc3RhdGUgPSBldmVudF90YXJnZXQ6YXN0ZXJvaWRfaW5jb21pbmdfbG9ja2VkX3N0YXRlIH0KCQkJCSMgQSByaW5nIGNhbmRpZGF0ZSBtdXN0IGhhdmUgdGhpcyB0cmFuc2FjdGlvbidzIGNvbXBsZXRlIHJpbmcgcmVjb3JkLgoJCQkJT1IgPSB7CgkJCQkJTk9UID0geyBpc19pbl9hcnJheSA9IHsgYXJyYXkgPSBnbG9iYWwuYXN0ZXJvaWRfaW5jb21pbmdfbWFpbl9mb290cHJpbnRfc3RhdGVzIHZhbHVlID0gVEhJUyB9IH0KCQkJCQlBTkQgPSB7CgkJCQkJCWNoZWNrX3ZhcmlhYmxlID0geyB2YXIgPSBhc3Rlcm9pZF9pbmNvbWluZ19zdGF0ZV90cmFuc2FjdGlvbl9pZCB2YWx1ZSA9IGdsb2JhbC5hc3Rlcm9pZF9pbmNvbWluZ190cmFuc2FjdGlvbl9pZCBjb21wYXJlID0gZXF1YWxzIH0KCQkJCQkJaGFzX3ZhcmlhYmxlID0gYXN0ZXJvaWRfaW5jb21pbmdfc3RhdGVfcmluZwoJCQkJCQljaGVja192YXJpYWJsZSA9IHsgdmFyID0gYXN0ZXJvaWRfaW5jb21pbmdfc3RhdGVfcmluZyB2YWx1ZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUuemVybyBjb21wYXJlID0gZ3JlYXRlcl90aGFuIH0KCQkJCQkJY2hlY2tfdmFyaWFibGUgPSB7IHZhciA9IGFzdGVyb2lkX2luY29taW5nX3N0YXRlX3JpbmcgdmFsdWUgPSBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ19ydW50aW1lLm1heGltdW1fZm9vdHByaW50X3JpbmcgY29tcGFyZSA9IGxlc3NfdGhhbl9vcl9lcXVhbHMgfQoJCQkJCX0KCQkJCX0KCQkJfQoJCQlzZXRfdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfY29yZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUuemVybyB9CgkJCWlmID0geyBsaW1pdCA9IHsgaXNfY29yZV9vZiA9IFBSRVYgfSBzZXRfdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfY29yZSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUub25lIH0gfQoJCQlzZXRfdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfc2FmZXR5ID0gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfcnVudGltZS5tYXhpbXVtX2Zvb3RwcmludF9yaW5nIH0KCQkJYWRkX3RvX3RlbXBfdmFyaWFibGUgPSB7IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3NhZmV0eSA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUub25lIH0KCQkJaWYgPSB7CgkJCQlsaW1pdCA9IHsKCQkJCQlpc19pbl9hcnJheSA9IHsgYXJyYXkgPSBnbG9iYWwuYXN0ZXJvaWRfaW5jb21pbmdfbWFpbl9mb290cHJpbnRfc3RhdGVzIHZhbHVlID0gVEhJUyB9CgkJCQkJY2hlY2tfdmFyaWFibGUgPSB7IHZhciA9IGFzdGVyb2lkX2luY29taW5nX3N0YXRlX3RyYW5zYWN0aW9uX2lkIHZhbHVlID0gZ2xvYmFsLmFzdGVyb2lkX2luY29taW5nX3RyYW5zYWN0aW9uX2lkIGNvbXBhcmUgPSBlcXVhbHMgfQoJCQkJfQoJCQkJc2V0X3RlbXBfdmFyaWFibGUgPSB7IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3NhZmV0eSA9IGFzdGVyb2lkX2luY29taW5nX3N0YXRlX3JpbmcgfQoJCQl9CgkJCXNldF90ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9pZCA9IGlkIH0KCQkJYXN0ZXJvaWRfaW5jb21pbmdfc2NvcmVfYmFja3VwX2NhcGl0YWxfY2FuZGlkYXRlID0geWVzCgkJCWlmID0gewoJCQkJbGltaXQgPSB7CgkJCQkJT1IgPSB7CgkJCQkJCU5PVCA9IHsgaGFzX2V2ZW50X3RhcmdldCA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3N0YXRlIH0KCQkJCQkJY2hlY2tfdmFyaWFibGUgPSB7IHZhciA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX2NvcmUgdmFsdWUgPSBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9iZXN0X2NvcmUgY29tcGFyZSA9IGdyZWF0ZXJfdGhhbiB9CgkJCQkJCUFORCA9IHsKCQkJCQkJCWNoZWNrX3ZhcmlhYmxlID0geyB2YXIgPSBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9jb3JlIHZhbHVlID0gYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfYmVzdF9jb3JlIGNvbXBhcmUgPSBlcXVhbHMgfQoJCQkJCQkJT1IgPSB7CgkJCQkJCQkJY2hlY2tfdmFyaWFibGUgPSB7IHZhciA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3NhZmV0eSB2YWx1ZSA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX2Jlc3Rfc2FmZXR5IGNvbXBhcmUgPSBncmVhdGVyX3RoYW4gfQoJCQkJCQkJCUFORCA9IHsKCQkJCQkJCQkJY2hlY2tfdmFyaWFibGUgPSB7IHZhciA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3NhZmV0eSB2YWx1ZSA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX2Jlc3Rfc2FmZXR5IGNvbXBhcmUgPSBlcXVhbHMgfQoJCQkJCQkJCQlPUiA9IHsKCQkJCQkJCQkJCWNoZWNrX3ZhcmlhYmxlID0geyB2YXIgPSBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zY29yZSB2YWx1ZSA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX2Jlc3Rfc2NvcmUgY29tcGFyZSA9IGdyZWF0ZXJfdGhhbiB9CgkJCQkJCQkJCQlBTkQgPSB7CgkJCQkJCQkJCQkJY2hlY2tfdmFyaWFibGUgPSB7IHZhciA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3Njb3JlIHZhbHVlID0gYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfYmVzdF9zY29yZSBjb21wYXJlID0gZXF1YWxzIH0KCQkJCQkJCQkJCQljaGVja192YXJpYWJsZSA9IHsgdmFyID0gYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfaWQgdmFsdWUgPSBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9iZXN0X2lkIGNvbXBhcmUgPSBsZXNzX3RoYW4gfQoJCQkJCQkJCQkJfQoJCQkJCQkJCQl9CgkJCQkJCQkJfQoJCQkJCQkJfQoJCQkJCQl9CgkJCQkJfQoJCQkJfQoJCQkJc2F2ZV9nbG9iYWxfZXZlbnRfdGFyZ2V0X2FzID0gYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfc3RhdGUKCQkJCXNldF90ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9iZXN0X2NvcmUgPSBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9jb3JlIH0KCQkJCXNldF90ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9iZXN0X3NhZmV0eSA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3NhZmV0eSB9CgkJCQlzZXRfdGVtcF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfYmVzdF9zY29yZSA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3Njb3JlIH0KCQkJCXNldF90ZW1wX3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9iZXN0X2lkID0gYXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfaWQgfQoJCQl9CgkJfQoJfQp9CgojIEFOWSBTQ09QRS4gQ2FsbGVkIG9uY2UgZnJvbSB0aGUgbWFpbi1pbXBhY3QgdHJhbnNhY3Rpb24gYWZ0ZXIgZm9vdHByaW50CiMgcGxhbm5pbmcgYW5kIGJlZm9yZSBkZXN0cnVjdGlvbi4gQSBzYW1lLXRyYW5zYWN0aW9uIHN1Y2Nlc3NmdWwgcmVjZWlwdCBtYWtlcwojIHJlcGVhdCBjYWxscyBpbmVydC4gQSBmYWlsZWQgYXR0ZW1wdCByZWNvcmRzIHRoZSBleGlzdGluZyBmYWlsdXJlIGZsYWcgb25seS4KIyBUaGUgb25lIGNvdW50cnkgc2NhbiBpcyB0cmFuc2FjdGlvbi1sb2NhbCwgd2l0aCBubyBwZXJpb2RpYyByZWdpc3RyYXRpb24uCmFzdGVyb2lkX2luY29taW5nX3JlbG9jYXRlX2N1cnJlbnRfY2FwaXRhbCA9IHsKCWlmID0gewoJCWxpbWl0ID0gewoJCQloYXNfZXZlbnRfdGFyZ2V0ID0gYXN0ZXJvaWRfaW5jb21pbmdfbG9ja2VkX3N0YXRlCgkJCU5PVCA9IHsKCQkJCWV2ZW50X3RhcmdldDphc3Rlcm9pZF9pbmNvbWluZ19sb2NrZWRfc3RhdGUgPSB7CgkJCQkJY2hlY2tfdmFyaWFibGUgPSB7IHZhciA9IGFzdGVyb2lkX2luY29taW5nX3N0YXRlX2NhcGl0YWxfcmVsb2NhdGVkIHZhbHVlID0gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfcnVudGltZS56ZXJvIGNvbXBhcmUgPSBncmVhdGVyX3RoYW4gfQoJCQkJCWNoZWNrX3ZhcmlhYmxlID0geyB2YXIgPSBhc3Rlcm9pZF9pbmNvbWluZ19zdGF0ZV9jYXBpdGFsX3JlbG9jYXRpb25fdHJhbnNhY3Rpb25faWQgdmFsdWUgPSBnbG9iYWwuYXN0ZXJvaWRfaW5jb21pbmdfdHJhbnNhY3Rpb25faWQgY29tcGFyZSA9IGVxdWFscyB9CgkJCQl9CgkJCX0KCQl9CgkJY2xlYXJfZ2xvYmFsX2V2ZW50X3RhcmdldCA9IGFzdGVyb2lkX2luY29taW5nX2NhcGl0YWxfY291bnRyeQoJCWNsZWFyX2dsb2JhbF9ldmVudF90YXJnZXQgPSBhc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zdGF0ZQoJCWNsZWFyX2dsb2JhbF9ldmVudF90YXJnZXQgPSBhc3Rlcm9pZF9pbmNvbWluZ19yZXBsYWNlbWVudF9jYXBpdGFsX3N0YXRlCgkJY2xyX2dsb2JhbF9mbGFnID0gYXN0ZXJvaWRfaW5jb21pbmdfY2FwaXRhbF9yZWxvY2F0aW9uX2NvbXBsZXRlCgkJY2xyX2dsb2JhbF9mbGFnID0gYXN0ZXJvaWRfaW5jb21pbmdfY2FwaXRhbF9yZWxvY2F0aW9uX2ZhaWxlZAoJCWV2ZW50X3RhcmdldDphc3Rlcm9pZF9pbmNvbWluZ19sb2NrZWRfc3RhdGUgPSB7CgkJCXNldF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfc3RhdGVfY2FwaXRhbF9yZWxvY2F0ZWQgPSBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ19ydW50aW1lLnplcm8gfQoJCQljbGVhcl92YXJpYWJsZSA9IGFzdGVyb2lkX2luY29taW5nX3N0YXRlX2NhcGl0YWxfcmVsb2NhdGlvbl9jb3VudHJ5CgkJCXNldF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfc3RhdGVfY2FwaXRhbF9yZWxvY2F0aW9uX3RyYW5zYWN0aW9uX2lkID0gZ2xvYmFsLmFzdGVyb2lkX2luY29taW5nX3RyYW5zYWN0aW9uX2lkIH0KCQl9CgkJZXZlcnlfY291bnRyeSA9IHsKCQkJIyBDb21wYXJlIHRoZSBkb2N1bWVudGVkIGNhcGl0YWwgcG9pbnRlciBiZWZvcmUgZW50ZXJpbmcgY2FwaXRhbF9zY29wZS4KCQkJIyBUaGlzIGV4Y2x1ZGVzIGNvdW50cmllcyB3aXRoIG5vIGNhcGl0YWwgd2l0aG91dCBhbiBpbnZhbGlkIHNjb3BlIGVudHJ5LgoJCQlsaW1pdCA9IHsKCQkJCWV4aXN0cyA9IHllcwoJCQkJY2hlY2tfdmFyaWFibGUgPSB7IHZhciA9IGNhcGl0YWwgdmFsdWUgPSBldmVudF90YXJnZXQ6YXN0ZXJvaWRfaW5jb21pbmdfbG9ja2VkX3N0YXRlIGNvbXBhcmUgPSBlcXVhbHMgfQoJCQl9CgkJCWlmID0gewoJCQkJbGltaXQgPSB7IGNhcGl0YWxfc2NvcGUgPSB7IHN0YXRlID0gZXZlbnRfdGFyZ2V0OmFzdGVyb2lkX2luY29taW5nX2xvY2tlZF9zdGF0ZSB9IH0KCQkJCXNhdmVfZ2xvYmFsX2V2ZW50X3RhcmdldF9hcyA9IGFzdGVyb2lkX2luY29taW5nX2NhcGl0YWxfY291bnRyeQoJCQkJYXN0ZXJvaWRfaW5jb21pbmdfc2VsZWN0X3N1cnZpdmluZ19jYXBpdGFsID0geWVzCgkJCQlpZiA9IHsKCQkJCQlsaW1pdCA9IHsgaGFzX2V2ZW50X3RhcmdldCA9IGFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3N0YXRlIH0KCQkJCQlzZXRfY2FwaXRhbCA9IHsgc3RhdGUgPSBldmVudF90YXJnZXQ6YXN0ZXJvaWRfaW5jb21pbmdfYmFja3VwX2NhcGl0YWxfc3RhdGUgcmVtZW1iZXJfb2xkX2NhcGl0YWwgPSBubyB9CgkJCQkJaWYgPSB7CgkJCQkJCWxpbWl0ID0geyBjYXBpdGFsX3Njb3BlID0geyBzdGF0ZSA9IGV2ZW50X3RhcmdldDphc3Rlcm9pZF9pbmNvbWluZ19iYWNrdXBfY2FwaXRhbF9zdGF0ZSB9IH0KCQkJCQkJc2V0X2NvdW50cnlfZmxhZyA9IGFzdGVyb2lkX2luY29taW5nX2NhcGl0YWxfcmVsb2NhdGVkCgkJCQkJCXNldF9nbG9iYWxfZmxhZyA9IGFzdGVyb2lkX2luY29taW5nX2NhcGl0YWxfcmVsb2NhdGlvbl9jb21wbGV0ZQoJCQkJCQlldmVudF90YXJnZXQ6YXN0ZXJvaWRfaW5jb21pbmdfbG9ja2VkX3N0YXRlID0gewoJCQkJCQkJc2V0X3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19zdGF0ZV9jYXBpdGFsX3JlbG9jYXRlZCA9IGNvbnN0YW50OmFzdGVyb2lkX2luY29taW5nX3J1bnRpbWUub25lIH0KCQkJCQkJCXNldF92YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfc3RhdGVfY2FwaXRhbF9yZWxvY2F0aW9uX2NvdW50cnkgPSBQUkVWIH0KCQkJCQkJfQoJCQkJCQkjIEFjaGlldmVtZW50IGNvbnRpbnVpdHkgYmVsb25ncyB0byB0aGUgb3JpZ2luYWwgdGFyZ2V0IGFsb25lLgoJCQkJCQlpZiA9IHsKCQkJCQkJCWxpbWl0ID0gewoJCQkJCQkJCWhhc19ldmVudF90YXJnZXQgPSBhc3Rlcm9pZF9pbmNvbWluZ19vcmlnaW5hbF90YXJnZXRfY291bnRyeQoJCQkJCQkJCXRhZyA9IGV2ZW50X3RhcmdldDphc3Rlcm9pZF9pbmNvbWluZ19vcmlnaW5hbF90YXJnZXRfY291bnRyeQoJCQkJCQkJCWNoZWNrX3ZhcmlhYmxlID0geyB2YXIgPSBnbG9iYWwuYXN0ZXJvaWRfaW5jb21pbmdfdGFyZ2V0X3dhc19jYXBpdGFsIHZhbHVlID0gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfcnVudGltZS56ZXJvIGNvbXBhcmUgPSBncmVhdGVyX3RoYW4gfQoJCQkJCQkJCU5PVCA9IHsgaGFzX2dsb2JhbF9mbGFnID0gYXN0ZXJvaWRfaW5jb21pbmdfb3JpZ2luYWxfdGFyZ2V0X2FubmV4ZWQgfQoJCQkJCQkJfQoJCQkJCQkJZXZlbnRfdGFyZ2V0OmFzdGVyb2lkX2luY29taW5nX2JhY2t1cF9jYXBpdGFsX3N0YXRlID0geyBzYXZlX2dsb2JhbF9ldmVudF90YXJnZXRfYXMgPSBhc3Rlcm9pZF9pbmNvbWluZ19yZXBsYWNlbWVudF9jYXBpdGFsX3N0YXRlIH0KCQkJCQkJfQoJCQkJCX0KCQkJCQllbHNlID0geyBzZXRfZ2xvYmFsX2ZsYWcgPSBhc3Rlcm9pZF9pbmNvbWluZ19jYXBpdGFsX3JlbG9jYXRpb25fZmFpbGVkIH0KCQkJCX0KCQkJCWVsc2UgPSB7IHNldF9nbG9iYWxfZmxhZyA9IGFzdGVyb2lkX2luY29taW5nX2NhcGl0YWxfcmVsb2NhdGlvbl9mYWlsZWQgfQoJCQl9CgkJfQoJfQp9CgojIFNUQVRFIFNDT1BFLiBDYWxsZWQgb25seSB3aXRoaW4gdGhlIGRlZHVwbGljYXRlZCBjb3VudHJ5LWFnZ3JlZ2F0aW9uIHBhc3MuCiMgUG9zaXRpdmUgc2FtZS10cmFuc2FjdGlvbiByZWNlaXB0IGFuZCBhbiBleGlzdGluZyByZWNvcmRlZCByZWNpcGllbnQgcmVxdWlyZWQuCiMgQWRkcyB0aGUgb2JzZXJ2ZWQgbW92ZSBjb3VudCB0byB0aGF0IGNvdW50cnkgYWxvbmUsIGluZGVwZW5kZW50bHkgb2YgdGhlCiMgcGh5c2ljYWwtbG9zcyBvd25lci9jb250cm9sbGVyIHJvd3MuIE5vIHBvcHVsYXRpb24vYnVpbGRpbmcgcmVjZWlwdCBpcyBhZGRlZC4KYXN0ZXJvaWRfaW5jb21pbmdfYWdncmVnYXRlX2NhcGl0YWxfcmVsb2NhdGlvbiA9IHsKCWlmID0gewoJCWxpbWl0ID0gewoJCQloYXNfdmFyaWFibGUgPSBhc3Rlcm9pZF9pbmNvbWluZ19zdGF0ZV9jYXBpdGFsX3JlbG9jYXRpb25fY291bnRyeQoJCQljaGVja192YXJpYWJsZSA9IHsgdmFyID0gYXN0ZXJvaWRfaW5jb21pbmdfc3RhdGVfY2FwaXRhbF9yZWxvY2F0ZWQgdmFsdWUgPSBjb25zdGFudDphc3Rlcm9pZF9pbmNvbWluZ19ydW50aW1lLnplcm8gY29tcGFyZSA9IGdyZWF0ZXJfdGhhbiB9CgkJCWNoZWNrX3ZhcmlhYmxlID0geyB2YXIgPSBhc3Rlcm9pZF9pbmNvbWluZ19zdGF0ZV9jYXBpdGFsX3JlbG9jYXRpb25fdHJhbnNhY3Rpb25faWQgdmFsdWUgPSBnbG9iYWwuYXN0ZXJvaWRfaW5jb21pbmdfdHJhbnNhY3Rpb25faWQgY29tcGFyZSA9IGVxdWFscyB9CgkJfQoJCXZhcjphc3Rlcm9pZF9pbmNvbWluZ19zdGF0ZV9jYXBpdGFsX3JlbG9jYXRpb25fY291bnRyeSA9IHsKCQkJaWYgPSB7CgkJCQlsaW1pdCA9IHsgZXhpc3RzID0geWVzIH0KCQkJCWlmID0gewoJCQkJCWxpbWl0ID0geyBOT1QgPSB7IGhhc192YXJpYWJsZSA9IGFzdGVyb2lkX2luY29taW5nX2NvdW50cnlfY2FwaXRhbF9yZWxvY2F0ZWRfY291bnQgfSB9CgkJCQkJc2V0X3ZhcmlhYmxlID0geyBhc3Rlcm9pZF9pbmNvbWluZ19jb3VudHJ5X2NhcGl0YWxfcmVsb2NhdGVkX2NvdW50ID0gY29uc3RhbnQ6YXN0ZXJvaWRfaW5jb21pbmdfcnVudGltZS56ZXJvIH0KCQkJCX0KCQkJCWFkZF90b192YXJpYWJsZSA9IHsgYXN0ZXJvaWRfaW5jb21pbmdfY291bnRyeV9jYXBpdGFsX3JlbG9jYXRlZF9jb3VudCA9IFBSRVYuYXN0ZXJvaWRfaW5jb21pbmdfc3RhdGVfY2FwaXRhbF9yZWxvY2F0ZWQgfQoJCQl9CgkJfQoJfQp9Cg==')
assert hashlib.sha256(before_capital_bytes).hexdigest() == 'e9c0febdfd97cf5b5495ef9ec4bcc9333776dfbf33ac605f2be3450d8245ce85'
class FrozenCapitalSource:
    def read_text(self, encoding): return before_capital_bytes.decode(encoding)

class SourceModel:
    def __init__(self, fixture, before=False, beforeCapital=False):
        self.fixture = copy.deepcopy(fixture)
        self.objects = {o['id']: o for o in self.fixture['objects']}
        self.global_object = {'id': -999, 'kind': 'global', 'vars': dict(self.fixture['globalVars']), 'flags': set(self.fixture.get('globalFlags', []))}
        self.objects[-999] = self.global_object
        self.targets = dict(self.fixture['targets'])
        self.temp = {}
        self.trigger_defs = parse(before_dir / '028_asteroid_incoming_triggers.txt') if before else parse(root / 'common/scripted_triggers/028_asteroid_incoming_triggers.txt')
        self.constants = parse(before_dir / '028_asteroid_incoming_constants.txt') if before else parse(root / 'common/script_constants/028_asteroid_incoming_constants.txt')
        self.effects = parse(FrozenCapitalSource()) if beforeCapital else parse(before_dir / '028_asteroid_incoming_runtime_effects.txt') if before else parse(helper_path)
        self.effects.update(parse(aggregation_path))
        for o in self.objects.values():
            o.setdefault('vars', {})
            o['flags'] = set(o.get('flags', []))
        self.actor = self.fixture['actor']

    def scope(self, key, stack):
        obj = self.objects[stack[-1]]
        if key == 'PREV': return stack[-2]
        if key == 'THIS': return stack[-1]
        if key == 'ROOT': return self.actor
        if key == 'global': return -999
        if key in ('OWNER', 'CONTROLLER'): return obj[key.lower()]
        if key == 'capital_scope': return obj['capital']
        if key.startswith('event_target:'): return self.targets[key.split(':', 1)[1]]
        if key.startswith('var:'): return int(self.value(key[4:], stack))
        raise AssertionError(('unsupported scope', key))

    def value(self, token, stack):
        try: return float(token)
        except ValueError: pass
        if token.startswith('constant:'):
            category, key = token[9:].split('.')
            return float(dict((k, v) for k, _, v in self.constants[category])[key])
        if token.startswith('@'): return float(self.effects[token])
        if '.' in token:
            key, field = token.rsplit('.', 1)
            return self.value(field, stack + [self.scope(key, stack)])
        if token in ('THIS', 'PREV', 'ROOT') or token.startswith('event_target:'):
            return self.scope(token, stack)
        obj = self.objects[stack[-1]]
        if token == 'id': return obj['id']
        if token == 'capital': return obj.get('capital', 0)
        return self.temp.get(token, obj['vars'].get(token, 0))

    def trigger(self, rows, stack):
        def node(key, op, val):
            obj = self.objects[stack[-1]]
            if key in ('AND', 'hidden_trigger'): return self.trigger(val, stack)
            if key == 'OR': return any(node(*r) for r in val)
            if key == 'NOT': return not any(node(*r) for r in val)
            if key in self.trigger_defs:
                return self.trigger(self.trigger_defs[key], stack) == (val == 'yes')
            if key in ('OWNER', 'CONTROLLER', 'PREV', 'capital_scope') or key.startswith(('event_target:', 'var:')):
                return self.trigger(val, stack + [self.scope(key, stack)])
            if key in ('any_owned_state', 'any_neighbor_state'):
                pool = [o for o in self.objects.values() if o.get('kind') == 'state' and (o['owner'] == obj['id'] if key == 'any_owned_state' else o['id'] in obj.get('neighbors', []))]
                return any(self.trigger(val, stack + [o['id']]) for o in pool)
            if key == 'check_variable':
                terms = dict((k, v) for k, _, v in val)
                if 'var' in terms:
                    left, right, compare = self.value(terms['var'], stack), self.value(terms['value'], stack), terms.get('compare', 'greater_than_or_equals')
                else:
                    k, op, v = val[0]
                    left, right, compare = self.value(k, stack), self.value(v, stack), {'=': 'equals', '>': 'greater_than', '<': 'less_than'}[op]
                return {'equals': left == right, 'greater_than': left > right, 'less_than': left < right, 'greater_than_or_equals': left >= right, 'less_than_or_equals': left <= right, 'not_equals': left != right}[compare]
            if key == 'has_variable':
                if '.' in val:
                    target, field = val.rsplit('.', 1)
                    return field in self.objects[self.scope(target, stack)]['vars']
                return val in obj['vars'] or val in self.temp
            if key == 'has_event_target': return val in self.targets
            if key == 'has_global_flag': return val in self.global_object['flags']
            if key in ('has_state_flag', 'has_country_flag'): return val in obj['flags']
            if key == 'exists': return obj.get('exists', True) == (val == 'yes')
            if key == 'scope_exists': return (obj is not None) == (val == 'yes')
            if key == 'impassable': return obj.get('impassable', False) == (val == 'yes')
            if key == 'has_state_category': return obj.get('category', 'town') == val
            if key in ('state', 'tag'): return obj['id'] == self.value(val, stack)
            if key == 'is_capital': return (obj['id'] in [o.get('capital') for o in self.objects.values() if o.get('kind') == 'country' and o.get('exists', True)]) == (val == 'yes')
            if key == 'is_core_of': return int(self.value(val, stack)) in obj.get('cores', [])
            if key == 'is_owned_and_controlled_by': return obj['owner'] == obj['controller'] == int(self.value(val, stack))
            if key == 'is_fully_controlled_by': return obj['controller'] == int(self.value(val, stack)) and obj.get('fullControl', True)
            if key == 'has_war_with': return int(self.value(val, stack)) in obj.get('wars', [])
            if key == 'is_in_array':
                terms = dict((k, v) for k, _, v in val)
                return self.value(terms['value'], stack) in self.value(terms['array'], stack)
            if key == 'any_province_building_level':
                terms = dict((k, v) for k, _, v in val)
                assert terms['building'] == 'bunker' and ('limit_to_victory_point', '=', 'yes') in terms['province']
                _, level_op, level = next(r for r in val if r[0] == 'level')
                assert level_op == '>' and self.value(level, stack) == -1
                return obj.get('vp', False)
            if key in ('state_population_k', 'industrial_complex', 'arms_factory', 'dockyard', 'infrastructure', 'rail_way', 'supply_node', 'air_base', 'naval_base', 'state_strategic_value'):
                left, right = obj.get(key, 0), self.value(val, stack)
                return left > right if op == '>' else left < right if op == '<' else left == right
            raise AssertionError(('unmodeled trigger', key, op, val))
        return all(node(*row) for row in rows)

    def execute(self, name, stack=None):
        self.run(self.effects[name], stack or [self.actor])

    def run(self, rows, stack):
        matched = False
        for key, op, val in rows:
            obj = self.objects[stack[-1]]
            if key in ('if', 'else_if', 'else'):
                if key == 'if': matched = False
                condition = next((b for k, _, b in val if k == 'limit'), [])
                if not matched and self.trigger(condition, stack):
                    self.run([r for r in val if r[0] != 'limit'], stack)
                    matched = True
                continue
            if key in self.effects and isinstance(val, str):
                assert val == 'yes'
                self.execute(key, stack)
            elif key in ('every_owned_state', 'every_country'):
                pool = [o for o in self.objects.values() if o['kind'] == ('country' if key == 'every_country' else 'state') and (key == 'every_country' or o['owner'] == obj['id'])]
                condition = next((b for k, _, b in val if k == 'limit'), [])
                for o in pool:
                    if self.trigger(condition, stack + [o['id']]): self.run([r for r in val if r[0] != 'limit'], stack + [o['id']])
            elif key in ('OWNER', 'CONTROLLER', 'PREV', 'capital_scope') or key.startswith(('event_target:', 'var:')):
                self.run(val, stack + [self.scope(key, stack)])
            elif key in ('set_temp_variable', 'set_variable', 'add_to_temp_variable', 'add_to_variable'):
                field, _, token = val[0]
                target = self.temp if 'temp' in key else obj['vars']
                if '.' in field:
                    scope_key, field = field.rsplit('.', 1)
                    target = self.objects[self.scope(scope_key, stack)]['vars']
                value = self.value(token, stack)
                target[field] = target.get(field, 0) + value if key.startswith('add') else value
            elif key == 'clear_variable': obj['vars'].pop(val, None)
            elif key == 'clear_global_event_target': self.targets.pop(val, None)
            elif key in ('save_event_target_as', 'save_global_event_target_as'): self.targets[val] = obj['id']
            elif key in ('set_global_flag', 'clr_global_flag', 'set_country_flag', 'clr_country_flag', 'set_state_flag'):
                flags = self.global_object['flags'] if 'global' in key else obj['flags']
                flags.discard(val) if key.startswith('clr') else flags.add(val)
            elif key == 'set_capital':
                terms = dict((k, v) for k, _, v in val)
                assert terms.get('remember_old_capital') == 'no'
                if not self.fixture.get('rejectNativeMove', False): obj['capital'] = int(self.value(terms['state'], stack))
            elif key == 'add_to_array':
                terms = dict((k, v) for k, _, v in val)
                name = terms['array'].split('.', 1)[1]
                self.global_object['vars'].setdefault(name, []).append(self.value(terms['value'], stack))
            else: raise AssertionError(('unmodeled effect', key, val))

def country(number, capital=0, **changes):
    return dict(id=number, kind='country', capital=capital, **changes)

def state(number, owner=101, ring=None, core=True, **changes):
    variables = {prefix + 'state_transaction_id': 7}
    if ring is not None: variables[prefix + 'state_ring'] = ring
    return dict(id=number, kind='state', owner=owner, controller=owner, cores=[owner] if core else [], state_population_k=30, infrastructure=2, vars=variables, **changes)

def fixture(states, countries=None, snapshot=1, **changes):
    countries = countries or [country(101, 1000), country(102, 0)]
    return dict(actor=102, objects=countries + states, targets={prefix + 'locked_state': 1000, prefix + 'original_target_country': 101}, globalVars={prefix + 'transaction_id': 7, prefix + 'target_was_capital': snapshot, prefix + 'main_footprint_states': [s['id'] for s in states if prefix + 'state_ring' in s['vars']], prefix + 'affected_country_entries': []}, **changes)

cases = []
def add(name, states, expected, recipient=101, replacement=True, failed=False, **kw):
    cases.append((name, fixture(states, **kw), expected, recipient, replacement, failed))

add('AST_CAP_NORMAL', [state(1000, ring=0), state(1001), state(1002, core=False)], 1001)
add('AST_CAP_ADJACENT_TWO_STATES', [state(1000, ring=0), state(1001, ring=1)], 1001)
add('AST_CAP_RING2_OVER_RING1', [state(1000, ring=0), state(1001, ring=1, vp=True, industrial_complex=10, rail_way=5, supply_node=1), state(1002, ring=2)], 1002)
add('AST_CAP_CORE_HIERARCHY', [state(1000, ring=0), state(1001, ring=1), state(1002, core=False, vp=True, industrial_complex=10, rail_way=5, supply_node=1)], 1001)
s = state(1001, vp=True); s['controller'] = 102
add('AST_CAP_OCCUPIED_BACKUP', [state(1000, ring=0), s, state(1002, ring=2)], 1002)
add('AST_CAP_CONTESTED_BACKUP', [state(1000, ring=0), state(1001, vp=True, fullControl=False), state(1002, ring=2)], 1002)
add('AST_CAP_ANNEXER', [state(1000, owner=102, ring=0), state(1001, owner=102, ring=1)], 1001, recipient=102, replacement=False, countries=[country(101, 1000, exists=False), country(102, 1000)], globalFlags=[prefix + 'original_target_annexed'])
add('AST_CAP_ANNEXER_NEW_CAPITAL', [state(1000, owner=102, ring=0), state(1001, owner=102)], 1001, recipient=102, replacement=False, snapshot=0, countries=[country(101, 0, exists=False), country(102, 1000)])
add('AST_CAP_MOVED_AFTER_LOCK', [state(1000, ring=0), state(1001, vp=True), state(1002)], None, recipient=None, replacement=False, countries=[country(101, 1002), country(102, 0)])
s = state(1000, ring=0); s['controller'] = 102
add('AST_CAP_OWNER_CONTROLLER', [s, state(1001, ring=1)], 1001)
add('AST_CAP_NO_BACKUP', [state(1000, ring=0), state(1001, owner=102), state(1002, category='wasteland')], None, recipient=None, replacement=False, failed=True)
add('AST_CAP_TIE_FORWARD', [state(1000, ring=0), state(1001), state(1002)], 1001)
add('AST_CAP_TIE_REVERSE', [state(1000, ring=0), state(1002), state(1001)], 1001)
add('AST_CAP_STALE_RING', [state(1000, ring=0), state(1001, ring=2), state(1002, ring=1)], 1002)
cases[-1][1]['objects'][3]['vars'][prefix + 'state_transaction_id'] = 6
add('AST_CAP_NATIVE_MOVE_REJECTED', [state(1000, ring=0), state(1001)], 1001, recipient=None, replacement=False, failed=True, rejectNativeMove=True)
add('AST_CAP_FRONTLINE', [state(1000, ring=0), state(1001, neighbors=[2000]), state(1002), state(2000, owner=102)], 1002, countries=[country(101, 1000), country(102, 0, wars=[101])])
add('AST_CAP_CONNECTED_SURVIVOR', [state(1000, ring=0), state(1001), state(1002, neighbors=[1003]), state(1003, core=False)], 1002)

for name, condition in (
    ('AST_CAP_PLANNED_FRAGMENT_BACKUP', 'planned'),
    ('AST_CAP_EXISTING_FRAGMENT_BACKUP', 'historical'),
    ('AST_CAP_PROCESSED_FRAGMENT_BACKUP', 'processed'),
    ('AST_CAP_STALE_PLANNED_FRAGMENT', 'stale'),
    ('AST_CAP_UNREGISTERED_PLANNED_FRAGMENT', 'unregistered'),
    ('AST_CAP_MAIN_CRATER_PLANNED_FRAGMENT', 'main_crater'),
):
    backup = state(1001, ring=0, flags=[prefix + 'fragment_site', prefix + 'state_planned'])
    backup['vars'][prefix + 'state_profile'] = 50
    if condition == 'historical':
        backup['vars'][prefix + 'state_transaction_id'] = 6
        backup['flags'].remove(prefix + 'state_planned')
    if condition == 'processed': backup['flags'].append(prefix + 'state_transaction_applied')
    if condition == 'stale': backup['vars'][prefix + 'state_transaction_id'] = 6
    if condition == 'main_crater': backup['flags'].append(prefix + 'main_crater')
    accepted = condition == 'planned'
    add(name, [state(1000, ring=0), backup, state(2000, owner=102, ring=0)], 1001 if accepted else None, recipient=101 if accepted else None, replacement=accepted, failed=not accepted)
    world = cases[-1][1]
    world['globalVars'][prefix + 'main_footprint_states'] = [1000]
    world['globalVars'][prefix + 'fragment_site_states'] = [2000] if condition == 'unregistered' else [1001, 2000]
    world['globalVars'][prefix + 'fragment_site_count'] = 2

fixture_hash = hashlib.sha256(json.dumps(cases, sort_keys=True).encode()).hexdigest()
for name, world, expected, recipient, replacement, failed in cases:
    after = SourceModel(world)
    after.execute(prefix + 'relocate_current_capital')
    main = after.objects[1000]
    moved = main['vars'].get(prefix + 'state_capital_relocated', 0)
    assert after.targets.get(prefix + 'backup_capital_state') == expected, (name, after.targets, expected)
    assert main['vars'].get(prefix + 'state_capital_relocation_country') == recipient, (name, main['vars'], recipient)
    assert (prefix + 'replacement_capital_state' in after.targets) == replacement, name
    assert (prefix + 'capital_relocation_failed' in after.global_object['flags']) == failed, name
    assert (prefix + 'capital_relocation_complete' in after.global_object['flags']) == bool(moved), name
    assert moved == int(recipient is not None), name
    assert after.targets[prefix + 'original_target_country'] == 101 and after.targets[prefix + 'locked_state'] == 1000, name
    assert after.global_object['vars'][prefix + 'target_was_capital'] == world['globalVars'][prefix + 'target_was_capital'], name
    if name.startswith(('AST_CAP_PLANNED_FRAGMENT', 'AST_CAP_EXISTING_FRAGMENT', 'AST_CAP_PROCESSED_FRAGMENT', 'AST_CAP_STALE_PLANNED_FRAGMENT', 'AST_CAP_UNREGISTERED_PLANNED_FRAGMENT', 'AST_CAP_MAIN_CRATER_PLANNED_FRAGMENT')):
        for key in ('main_footprint_states', 'fragment_site_states', 'fragment_site_count'):
            assert after.global_object['vars'][prefix + key] == world['globalVars'][prefix + key], name
        original_backup = next(o for o in world['objects'] if o['id'] == 1001)
        assert after.objects[1001]['vars'] == original_backup['vars'] and after.objects[1001]['flags'] == set(original_backup['flags']), name
        direct_before = SourceModel(world, beforeCapital=True)
        direct_before.execute(prefix + 'relocate_current_capital')
        assert prefix + 'backup_capital_state' not in direct_before.targets, name
        assert dict((k, v) for k, _, v in after.constants[prefix + 'population_loss'])['fragment_center'] == '0.50', name
    if moved:
        assert after.objects[recipient]['capital'] == expected, name
        before_repeat = copy.deepcopy((after.targets, main['vars'], after.global_object['flags']))
        after.execute(prefix + 'relocate_current_capital')
        assert (after.targets, main['vars'], after.global_object['flags']) == before_repeat, name
    main['flags'].add(prefix + 'state_transaction_applied')
    main['vars'][prefix + 'state_profile'] = 70
    after.execute(prefix + 'aggregate_current_state', [after.actor, 1000])
    first_counts = {i: o['vars'].get(prefix + 'country_capital_relocated_count', 0) for i, o in after.objects.items() if o['kind'] == 'country'}
    after.execute(prefix + 'aggregate_current_state', [after.actor, 1000])
    for i, count in first_counts.items():
        assert count == int(i == recipient) and after.objects[i]['vars'].get(prefix + 'country_capital_relocated_count', 0) == count, (name, first_counts)
    before = SourceModel(world, before=True)
    before.execute(prefix + 'relocate_destroyed_capital')
    print(f'{name}: backup={expected}, recipient={recipient}, replacement={replacement}, failed={failed}, counts={first_counts}, before_backup={before.targets.get(prefix + "backup_capital_state")}')
print(f'{len(cases)} actual-source scenario cases passed. Fixture SHA256: {fixture_hash}')

# Verify the actual caller order and planner-only flag timing independently of
# the capital selection model. These are AST order checks, not an engine run.
runtime = parse(root / 'common/scripted_effects/028_asteroid_incoming_runtime_effects.txt')
effects = parse(aggregation_path)
event_rows = parse(root / 'events/028_asteroid_impact.txt', rows=True)
impact = next(b for k, _, b in event_rows if k == 'country_event' and ('id', '=', 'chaosx.nr28.4') in b)
immediate = dict((k, v) for k, _, v in impact)['immediate']
branch = next(b for k, _, b in immediate if k == 'if' and (prefix + 'choose_fragment_sites', '=', 'yes') in b)
order = [k for k, _, _ in branch]
assert order.index(prefix + 'plan_main_footprint') < order.index(prefix + 'choose_fragment_sites') < order.index(prefix + 'process_footprint')
process_order = [k for k, _, _ in runtime[prefix + 'process_footprint']]
assert process_order.index(prefix + 'relocate_destroyed_capital') < process_order.index('while_loop_effect')
assert runtime[prefix + 'select_backup_capital'] == [(prefix + 'select_surviving_capital', '=', 'yes')]
assert runtime[prefix + 'relocate_destroyed_capital'] == [(prefix + 'relocate_current_capital', '=', 'yes')]
def blocks(rows):
    for k, _, b in rows:
        if isinstance(b, list):
            yield k, b
            yield from blocks(b)
fragment_loop = next(b for k, b in blocks(runtime[prefix + 'choose_fragment_sites']) if k == 'for_each_scope_loop' and ('array', '=', 'global.' + prefix + 'fragment_site_states') in b)
fragment_order = [k for k, _, _ in fragment_loop]
assert ('set_state_flag', '=', prefix + 'fragment_site') in fragment_loop
assert fragment_order.index('set_state_flag') < fragment_order.index(prefix + 'plan_fragment_footprint')
assert ('set_variable', '=', [(prefix + 'state_transaction_id', '=', 'global.' + prefix + 'transaction_id')]) in fragment_loop
assert (prefix + 'record_footprint_profile', '=', 'yes') in effects[prefix + 'plan_fragment_footprint'][0][2]
record_branch = next(b for k, _, b in effects[prefix + 'record_footprint_profile'] if k == 'if')
assert ('set_state_flag', '=', prefix + 'state_planned') in record_branch
for body in (fragment_loop, effects[prefix + 'plan_fragment_footprint'], effects[prefix + 'record_footprint_profile']):
    assert (prefix + 'state_transaction_applied') not in [v for k, b in blocks(body) for x, _, v in b if x == 'set_state_flag']
print('AST_CAP_FRAGMENT_SEQUENCE: actual planner metadata precedes relocation and physical transactions. Parent wrappers are integrated.')
for p in (helper_path, aggregation_path): print(f'{p.name}: SHA256 {hashlib.sha256(p.read_bytes()).hexdigest()}')
print('Source-model evidence only. Native and probability acceptance remain blocked.')
```
