# Event 35 condition-scaled duration architecture sidecar

## Status and authority

Disposition: `implemented` for this bounded read-only audit and its handoff, with final parent integration and native lifecycle evidence `unresolved`.
The parent explicitly assigned this sidecar on 2026-10-07 while implementing condition-scaled project duration.
The accepted task inputs are a structural baseline of 133 days, five bounded condition components, frozen accepted work, certification beginning at total work minus 42 days, a separate 42-day protection treatment, and a native selected-center mission synchronized to stored due day plus grace.
No gameplay, tests, localisation, assets, spreadsheet, or Git writes were authorized.
Only this handoff was written.
Probability work remains with auditor `01a116fe-db3a-7630-829a-e6976b133e79` and was not repeated.
No design change, fallback, or simplification was implemented.
This is not an Event 35 completion claim or a final audit of the parent's still-changing patch.

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

## Reading and inspected source

Read AGENTS.md and the complete events, decisions-missions, and subagents skills.
Read the spec index, part 3, relevant acceptance and inheritance sections of parts 11 and 8, part 4, and the complete state lifecycle map for this bounded surface.
Part 3 line 147 explicitly requires state damage, Severity, infrastructure, war state, and earlier failures to scale Regional Works duration.
Part 11 D-01 lines 384-387 requires small-economy costs and project duration to scale correctly.
Part 4's transfer and cleanup contracts require state work and receipts to survive legitimate transfer without duplicating rewards.
The parent retains full-package spec coverage and acceptance reconciliation.

Inspected existing `chaosx_dynamic_effects.txt` and its matching Markdown before assessing the new owner helper.
The existing generic date conversion helpers operate on encoded `global.date` values and are not appropriate for this subsystem's `global.num_days` deadlines.
Keep required work, due-day differences, and native timeout deltas in days.
No central router or shared wrapper is warranted.

Inspected the main project authorizer, processor, transfer/adoption, stage/treatment helpers, cleanup, decision effects, selected-state triggers, mission definition, receiver event, and event-owned control callback.
The duration helper appeared during the audit and was read directly and through narrow live source lookup.
At the last inspection, authorizer output storage and the frozen required-work/certification fields were wired, and terminal cleanup cleared both new fields.
Mission binding and timer changes had not yet appeared in the inspected decision effects and triggers.
Treat those as parent work in progress rather than an alleged final omission.

## Helper and field map

| Helper or field | Scope and inputs | Output and side effects | Call sites or consumers |
| --- | --- | --- | --- |
| `great_depression_quote_center_project_duration` | STATE with the paying crisis country as ROOT, current center registration, caller-owned `great_depression_duration_quote_type` and preinitialized `great_depression_duration_quote_days` | Temporary quote only, zero on failed preconditions, protection interval or bounded structural quote | Authorizer and state-targeted tooltip wrapper |
| `great_depression_prepare_center_duration_tooltip` | COUNTRY in a state-targeted decision, FROM is the exact state, caller supplies quote type | Writes country tooltip cache `great_depression_tt_project_days` from positive quote | Parent-owned state action tooltip call sites |
| `great_depression_center_project_required_work_days` | STATE accepted authorization | Persistent frozen required work | Project completion and processor thresholds |
| `great_depression_center_project_certification_start_work_days` | STATE accepted authorization | Persistent `max(required work - 42, 0)` | Processor certification transition |
| `great_depression_center_project_due_day` | STATE accepted authorization | Persistent nominal completion day, shifted by accepted interruption | Existing country ledger mirror and proposed mission timer sync |
| Existing project ledger writer | STATE with exact registration and ROOT country | Mirrors stage, start, due, and pause dates into existing aligned country arrays | Authorization and stage changes |
| Proposed narrow mission bind/sync helpers | COUNTRY owning the native mission, exact stored state/episode/authorization | Frozen mission identity, native signed timeout delta, receipt-gated resolution | Initial mission activation, accepted authorization binding, pause/resume repair, completion/cancellation/timeout |

No extra duration arrays are required if state fields remain authoritative and all mission consumers enter the exact stored site.
If the parent adds mirrors, every append, reuse, clear, and retirement path must maintain their alignment.
The existing ledger contains due-day mirrors already.

## Constants and bounded calculation

The observed `great_depression_project_duration` category uses a first-entry fixed-point schema.

| Component | Observed tuning | Bound |
| --- | --- | --- |
| Structural baseline | Existing `center_project_total_days = 133` | Positive minimum |
| Native damaged infrastructure and factories | 7 days per damaged level, combined cap 6 | 0-42 days |
| Severity above 40 | 0.5 day per point, cap 60 points | 0-30 days |
| Poor infrastructure | Reference 5, 4 days per missing level | 0-20 days |
| War | 14 days | 0 or 14 days |
| Current-episode project failures | 7 days per failure, cap 3 | 0-21 days |
| Accepted total | Integer-rounded after final clamp | 133-245 days |
| Certification interval | Existing 42 days | Starts at accepted total minus 42 |
| Protection treatment | Existing 42 days | Separate from structural work |
| Mission grace | 7 days | Added to the stored project due day |

The unbounded sum of capped components reaches 260 days, so the final 245-day cap intentionally saturates the most adverse combination.
That cap is explicit tuning, not a missing factor.
The helper clamps each damage getter before addition and clamps the combined damage again, which bounds intermediate arithmetic without altering historical failure counts.
The failure counter is read-only in the quote and resets at accepted episode entry in the current main effect.
War and Severity are read from ROOT rather than the state's current owner, so the quote remains tied to the proven payer.
The intended ROOT contract must remain explicit at every call site.

Independent arithmetic spot checks of the observed formula gave clean conditions 133 days with certification at 91, damage 3/Severity 80/infrastructure 2/war/two failures 214 days with certification at 172, and capped adverse inputs 245 days with certification at 203.
Half a damaged level plus Severity 41, otherwise clean, gave 137 days with certification at 95.
These are formula checks, not actual-source execution or native observations.
The native getter documentation establishes the tokens but does not by itself establish every runtime fractional damage value or rounding boundary.

## Scope audit

The source documents and implements `chaosx.nr35.8` as the affected-country maintenance receiver.
Its immediate effect refreshes mission capacity and then calls the country pulse, which processes transfers before projects.
Along that chain ROOT is the affected country and entering a registered STATE pointer leaves ROOT unchanged.
Thus the duration quote's ROOT reads and the current project processor's ROOT checks are coherent along this receiver path.
Targeted decision effects enter FROM with the acting country retained as ROOT, so the quote tooltip wrapper has the intended country/state relationship.
The control callback only records loss history and does not directly invoke the audited project authorizer, adoption, or processor.
Its ROOT is the new controller, so it must not become a direct project-owner caller without a new explicit scope contract.

Adoption runs in the selected STATE with the successor as ROOT and rewrites `center_episode_id` and live `project_episode_id` to the successor's active episode.
It does not rewrite project work, due date, authorization ID, or the new duration fields.
That preserves frozen accepted work without re-quoting against the successor's Severity, war, or failure history.
Historical transfer and completion receipts remain separate from the adopted live episode.

Cleanup enters a registered STATE from the country and compares `center_episode_id` with `PREV.great_depression_active_episode_id`.
That PREV read correctly identifies the calling cleanup owner without assuming that ROOT was rebound by a nested country scope.
Episode IDs are allocated from the global sequence, so successful adoption into a different active episode protects the state from subsequent old-owner cleanup.

## Concrete findings for the parent

### F1. Bind the native mission to exact authorization, not mutable selection

The baseline mission-capacity helper at `035_great_depression_decision_effects.txt:64-73` binds only state and episode after a native mission is already active.
It takes the then-current `great_depression_selected_center_state`.
If selection changes between native activation and the next receiver refresh, the mission can bind the wrong site.
The baseline completion trigger at `035_great_depression_decision_surface_triggers.txt:2266-2276` accepts a reopened state and a historical completed receipt without matching the completed authorization.
The authorizer keeps historical completion IDs, so a later paid project can coexist with an older completion receipt.
These source facts make the exact binding requirement material.

Freeze `(state pointer, active episode ID, authorization ID)` in the country when the matching project authorization becomes the mission contract.
If native activation deliberately precedes any paid authorization, freeze the site/episode immediately and treat authorization as explicitly unbound until the next accepted project on that same site.
Do not make ordinary refresh rebind an established receipt to the currently selected site or to a later authorization.
Successful resolution must match `project_completed_authorization_id` and the current live project authorization with the bound mission authorization, and also verify current registration, ownership/control, and episode.
The context predicate must allow the exact completed receipt after the unspent-authorization predicate becomes false.
Otherwise the native cancellation path can cancel a legitimately finished project before success.

### F2. Existing-row adoption has a confirmed cap/index defect

The baseline adoption guard requires `center_count < center_registry_cap` before checking whether the state already occurs in the successor's array.
A returning site already occupying a row is therefore rejected at a full registry even though no append is needed.
Below the cap, adoption assigns `center_registry_index = ROOT.center_count` before the conditional append.
When the site already exists in that country's array, the append is skipped but the index still points to the next free slot rather than its existing row.
The following stage-ledger write, and later duration-related stage/due mirrors, can write the wrong row or create an unmatched array slot.
This affects regained centers and repeated transfers.

For an existing row, reuse its discovered exact index without applying an append-cap gate or incrementing count.
For a genuinely new row, retain the current cap and aligned append contract.
This is a narrow lifecycle repair, not a request to increase the project or center cap.

### F3. Source cleanup can erase a transfer awaiting adoption

The cleanup guard protects an already adopted successor record because its episode has changed.
Before adoption, however, the transferred state still carries the source episode.
Source recovery or retirement then clears its center, transfer flags, work, due date, and the newly added duration fields through `great_depression_clear_registered_center_runtime`.
An open transfer contract and a valid physical successor are not excluded by that guard.
This destroys the retained local burden and partial work before the explicit successor can adopt it.
Part 4 requires those state receipts to move with the state.
Preserve or explicitly retire that transfer-owned state under the existing ownership contract rather than treating source-country episode cleanup as sufficient authority to delete it.
No new global scan is needed.

### F4. A paused project can outlive its unextended native mission

The current processor shifts `project_due_day` by the entire pause interval only when work resumes.
The pause failure threshold is 28 days and observed mission grace is 7 days.
Example: nominal due day 133, pause begins day 130, and ownership returns day 145.
The retained project can validly resume and shift its due day to 148, but a mission still synchronized to the old due day plus grace reaches day 140 first.
If current context allows the mission to remain active while paused, that native timeout can create a failure before the valid resumption.
If authority loss instead cancels the mission immediately, cancellation must preserve the state work and accepted threshold and allow only a new successor/regain mission contract to bind it.
Keep these alternatives explicit under the existing contract.
For a mission intentionally retained through pauses, its effective stored deadline must account for the current pause before timeout, without adding the same pause twice on resume.

### F5. Receipt-gate callbacks before publishing failure, relief, or payment

The baseline completion, timeout, and cancellation helpers write mission flags and call generic outcome helpers before clearing their state/episode fields.
They have no exact receipt guard inside the callback body.
Native cancellation or timeout can arrive after transfer, cleanup, a replacement project, or an owner repair pass.
The native mission and any owner recovery path must share the same active-contract guard and consume that contract once before irreversible outcome writes.
Clear state, episode, authorization, deadline cache, and private active receipt together on every terminal mission path and in `cancel_all_missions`.
Authority-loss cancellation should not increment project failure history or apply success relief.
Removing the native mission skips its completion/timeout effects according to the documented native lifecycle, so independent removal must be paired with private receipt cleanup.

The existing mission's `available` also requires the center-reopen payment after the state project has already completed, and its generic completion helper pays that cost.
An inability to pay can therefore let a mission expire after successful work.
This is an existing objective/payment coupling for parent review, not permission for this sidecar to change costs or route design.

### F6. Tooltip forecasts and accepted work sample Severity at different points

The pure tooltip quote reads current Severity.
Regional Works calls `great_depression_commit_country_action` with `strong_relief` before authorizing the center project, so the authorizer's fresh quote reads the already reduced Severity.
Above the floor and below the caps, a five-point relief changes the raw duration by 2.5 days before integer rounding.
For the arithmetic example with Severity 80, the current-condition forecast is 214 days while the otherwise identical post-action Severity 75 quote is 211.5 before rounding.
This is a forecast/acceptance coherence issue to review in final call sites, not proof of a native tooltip display defect.
If the UI promises exact accepted duration, compute the forecast and authorization from the same intended pre- or post-action conditions without changing the accepted relief effect.

## Native mission synchronization contract

In the exact mission owner's COUNTRY scope, require a live bound receipt, matching site/episode/authorization, an existing accepted due day, and `has_active_mission`.
Compute `remaining = accepted_project_due_day + mission_grace_days - global.num_days`.
Compute `delta = remaining - days_mission_timeout@great_depression_reopen_depression_center`.
Call `add_days_mission_timeout = { mission = great_depression_reopen_depression_center days = var:<delta> }`.
The difference can shorten or extend the timer and repeated synchronization converges to zero delta.
Use signed subtraction, not unary negation of a variable token.
Resolve an already expired matching contract through the guarded timeout path rather than reviving it with a minimum positive timer.
Synchronize after activation/binding and every accepted due-day shift, including pause repair and adoption when the new country actually owns a matching native mission.
Changing only the country array mirror or stored due day does not resize a native mission.
Do not remove and reactivate a running mission as a timer update.

## Cleanup and migration checklist

1. Keep the quote pure and preserve caller-preinitialized temporary output at every helper boundary.
2. Freeze required work and certification start only on fresh accepted authorization.
3. Replace every fixed structural completion/certification comparison with the accepted state fields.
4. Keep protection treatment separate from structural project progression.
5. Preserve new fields through state stage changes, transfer, adoption, partial work, freight credit, and legitimate resume.
6. Reuse exact existing array rows during adoption and mirror due-day changes only to the proven row.
7. Clear new state fields only at terminal retirement with authority over that live record, preserving an open successor transfer when required.
8. Bind and synchronize native mission state independently of human selection, then consume and clear its receipt on success, failure, and cancellation.
9. Update owner helper Markdown and the generic dynamic-effect registry reference in the parent's change.
10. Reinspect the final parent sources and carry the F1-F6 dispositions into the parent completion report.

No new global event target is necessary.
The existing regular `great_depression_transfer_adoption_state` target is a synchronous adoption alias, while asynchronous mission identity belongs in country-owned persistent pointer/receipt fields.
No manual clearing of a regular event target is needed or supported.

## Reference evidence

All paths below are native Windows paths relative to the repository root or installed game root as indicated.
Reference routes were exposed and their successful responses establish retrieval health for these calls.
Installed docs were treated as primary authority and the offline wiki was read in parallel.

| Source | Read spans | Revision |
| --- | --- | --- |
| Installed `documentation\dynamic_variables_documentation.md` | 238-240 mission getter, 1118-1120 damage getter, 1133-1135 infrastructure getter | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Installed `documentation\effects_documentation.md` | 1051-1065 native mission extension, 6083-6092 mission removal, 6496-6504 regular event targets | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation\script_concept_documentation.md` | 216-222 script constants | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common\script_constants\documentation.md` | 1-34 schema and variable access | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Installed `common\decisions\_documentation.md` | Complete 46-line file, including COUNTRY acting scope and FROM targeted state | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |
| Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263-328 event targets, 435-443 temporary lifetime, 1495 mission getter, 1675-1676 infrastructure/damage getters | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 1917 mission extension variable argument | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 811-872 PREV traversal examples | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Offline `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 465-479 activation, automatic completion, timeout | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |

Installed root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Exact vanilla damage precedent was source-located in `common\occupation_laws\occupation_laws.txt:467-468`, with infrastructure use at 388 and combined factory damage at 467-468.
Source lookup revision for that location was `4549887ee800fd76d18a01ce4f6cac30a9aa4c2f686e187bfda10f7a487f4068`.
These blocks were inspected only as getter/arithmetic precedents and their AI weights were not audited or copied.
Exact vanilla variable mission-extension precedent was source-located in `common\scripted_effects\CHI_scripted_effects.txt:634-649`, with `days = CHI_concessions_small` in country scope and a scoped variable in the JAP branch.
Source lookup revision for that location was `c3e452ea22fdf2070018b838791187b44aec15c7bfdccd3ee500659a2d18e9e3`.
This establishes native variable-input precedent, not execution of the proposed signed synchronization transaction.

## MCP artifacts and unsupported coverage

Workspace ID: `mod_chaos_redux_ea3b2d67c2c0`.
Narrow source lookups found the authorizer, adoption helper, and new duration helper.
Adoption structure revision was `c446d58e37dd2dc676a915ce615040d4ce1b14a4b449a8e0c652d641243a3813`.
Duration helper lookup revision was `166708a374bb3866633533ce87e534d37425116eec3d66c7e31a66ba7055e62b`.
The initial lookup used a near-but-nonexistent `great_depression_authorize_state_project` name and returned zero definitions, then the exact owner identifier was inspected successfully.

Event trace artifact:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/204c79d6209dd759ca825b4a627774d159138ceeb0b2c8314759f30af505cf49/24ef03f66bb005f71eab0ace6a31f641faeccadf02884e2b1d0802d1b5170a3a/event-trace-3c38803347d1.json`.
The trace returned `EVENT_INSPECTED_PARTIAL`, focused mode, zero indexed helper coverage, and the explicit message that whole-workspace helper projections and lifecycle passes were deferred.
It is not project lifecycle proof.
The full trace artifact was retained by URI and was not fully ingested by this sidecar.

Scope render manifest:
`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc8a5ecf7ae4b42b84ffbde1e386245680d5184cde644e9b82f7356169523ba7/fe8064e1d453f54ba807acbde1293ede3a690b15e5e90890491d9e42c07d63a4/event-scope-2c3d335e6086-manifest.json`.
The full 46,675-byte manifest text was read and parsed through its supported resource route.
It reports `complete = false` and an empty `selectedNodeIds` for the exact `chaosx.nr35.1` selector despite including the source file hash.
There is therefore no usable selected Event 35 scope render in this result.
The manifest graph revision is `2c3d335e60864d8c0eaddccd379909409538d05e04c6cad5a4fb28c73a521a18` and its Event 35 source hash is `997692c7f82d4069e240ab255cc4348cfb120927ca180c941dc9438ffc7fedaa`.
No broad service-load retry or external tooling repair was attempted.

`script_validate` could not validate the mixed country-ROOT/state-THIS helper contract through the attempted snippet forms.
A STATE snippet treated ROOT as STATE and reported `has_war` in the wrong scope, which does not prove the production call is wrong because the receiver/decision supplies a country ROOT.
An explicit ROOT binding was rejected with `SCRIPT_BINDING_RESERVED` because ROOT, THIS, and PREV follow the supplied scope and traversal stack.
A COUNTRY snippet with a declared state event-target wrapper returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, an unresolved event-target scope command, and zero checked inner commands.
Argument blocks and helper predicates remain unsupported analysis, and no validator pass is claimed.
The server's standalone health/version and client task-negotiation evidence was not exposed by this bounded discovery, so helper-expansion jobs or native MCP tasks were not used.
No focus, GUI, technology, or map surface was designed or modified by this sidecar.
No dedicated native mission lifecycle inspection route was discovered, and documentation/source inspection is not equivalent to executed native timer evidence.

## Concurrent source identities and remaining verification

These SHA-256 identities describe the observed files during implementation and are not an immutable whole-workspace snapshot.

| File | SHA-256 |
| --- | --- |
| `common\scripted_effects\035_great_depression_effects.txt` | `e6c7463f829957f4297ada3dc5fea259d4ef9a41d97b65344c2e46b1d59120fc` |
| `common\scripted_effects\035_great_depression_project_duration_effects.txt` | `80e24df973418d3769466483ada5832be2a5dd6921b50e022fa35a8a775aed87` |
| `common\scripted_effects\035_great_depression_decision_effects.txt` | `16b87b44668b9a5d5ed2be3f673f2f9c3a04632126abb165767bf872ea2dc5a4` |
| `common\scripted_triggers\035_great_depression_decision_surface_triggers.txt` | `a59b1034461ed5ed4272aa614f11b134c2be55f760222a4f12ba5c12ddff3e32` |
| `common\script_constants\035_great_depression_constants.txt` | `b551ca8bd8dd5bcf6cc42ae96e605230ec2c7bb48c5c4eaa9509618950466456` |

Meaningful audit performed: caller-owned temporary output review, every structural threshold read in the observed patch, transfer/adoption preservation, exact cleanup-owner comparison, mission site and episode binding, native getter and timer precedents, bounded formula spot checks, and MCP partial-coverage inspection.
Meaningful verification still required on final parent sources: existing-row regain at full and nonfull cap, transfer-before-source-cleanup, wrong-site selection changes, previous authorization completion, stale/duplicate callbacks, pauses crossing the original native deadline, successor ownership, fractional damage/rounding boundaries, and exact native timer convergence.
Gameplay/test writes and Git writes were explicitly forbidden for this sidecar.
No game was launched and no logs were requested.
The parent must review final source and own implementation, helper documentation, tests, probability audit reconciliation, and completion claims.

## Follow-up after the parent's core-duration notification

The parent confirmed the quote, frozen work/certification fields, completion guards, terminal cleanup, and updated manual-transfer fixture were implemented.
Native mission identity/synchronization and tooltip forecasts remain parent-owned work in progress.
No AI coefficient changes were reported or audited by this sidecar.

Reinspection found the processor's new presence and positive-value guard at `035_great_depression_effects.txt:1055-1056`.
This rejects missing or nonpositive required work before any progress or pause processing.
Fresh production authorization initializes the caller-owned quote output and writes both frozen state fields, so ordinary accepted projects have the required record.
Adoption still retains those fields directly on the state, without recomputing the quote for the successor.
Terminal cleanup explicitly clears them at lines 3188-3189 under the matching calling-owner episode.

Executed `python -B .tools/test_event035_center_projects.py` without changing the test file or generating Python bytecode.
All 15 existing tests passed.
The manual active-transfer fixture includes required work and certification cut at test lines 1146-1147, and the suite reads the production duration helper.
The executor preserves temporary helper frames and rejects unknown commands.
Its only declared external effect fixture is the out-of-scope humanitarian pressure submission, which is recorded rather than executed.
Project registration, authorization guards, transfer, adoption, due-day processing, ledger updates, and cleanup execute their production helper bodies.
This remains source execution over native primitive fixtures, not native callback, mission timer, save, or game execution.

Additional in-memory probes used that existing source executor without writing tests or other files:

| Probe | Observed source result |
| --- | --- |
| Fresh accepted project transferred and adopted after 20 days | Frozen required work and certification cut unchanged |
| Successor resumes the adopted project | Both fields unchanged and existing pause reconciliation executes |
| Former owner cleans its old episode after adoption | Both successor state fields preserved |
| Successor cleans its matching episode | Both fields removed |
| Required-work field removed before transfer/adoption | Adoption succeeds and sets the successor's active project flag, but processing does nothing even after 40 more days |
| Certification cut explicitly zero while required work remains valid | Certification stage entered after one work day |
| Source cleanup before successor adoption | Both fields and the open transfer contract removed |

### Additional finding F7: malformed active duration records need an explicit lifecycle outcome

The positive required-work guard prevents free completion, but adoption at lines 1251-1272 does not validate required work or certification metadata before committing the new episode and national active slot.
An active transferred record lacking required work is therefore adopted into a successor slot that the processor can never advance, resume, or fail through its pause branch.
It remains paused and active beyond the ordinary 28-day pause-failure interval.
The preservation probe with a valid production authorization passes, so this is a malformed-record risk rather than a normal quote failure.
Reject incomplete active records before adoption commits the slot, or provide an explicit identity-bound repair/resolution contract that preserves the actual accepted record.
Do not silently synthesize a 133-day duration or re-quote against current conditions.
`due_day - start_day` is not generally proof of accepted work because the due day can already include pauses.

The processor also lacks a presence/coherence guard for the frozen certification cut.
The source executor throws `TypeError` for the absent right-hand-side certification token, so actual missing-field engine behavior is unsupported by that fixture and was not inferred from the failed probe.
A separate explicit-zero probe executes the production branch and confirms premature certification after one work day.
For structural projects, validate the stored cut against the accepted required work and intended 42-day certification interval, or document an explicit deterministic repair under that interval contract.
Keep protection's intentional 42-day treatment separate, since a zero cut can be valid for that short treatment.
No repair or fallback was applied by this sidecar.

F2 existing-row cap/index reuse, F3 cleanup of an unadopted transfer, F4 pause/native deadline coherence, and F5 exact mission callback guards remain open for parent review.
The additional source probes substantiate F3 but do not replace the pending native mission synchronization review.
Narrow live source lookup revision for the rechecked processor and adoption structure was `16dac9afe078558c4d1201901df65b3835f84dc28053ff108d06322d2a3988cd`.
The follow-up main effect SHA-256 was `366ea129f3b1a9b53343788382606d580baa853a6c05fcaf978b0beb59d75102`, the unchanged quote helper was `80e24df973418d3769466483ada5832be2a5dd6921b50e022fa35a8a775aed87`, and the tested fixture was `44cc7e6de7a0f5fe44fb537f5df67e6d8af6d27c249ab3d7cfe7fb8a473727b2`.
No broader event inspection, probability run, GUI review, or native task was repeated.

## Follow-up after coherence, native timer, and forecast implementation

The parent requested narrow read-only review of the new coherent-duration triggers, active-work adoption preflight, selected-center timer synchronization, all four identity cleanup paths, and guarded completion/timeout callbacks.
Only this handoff was changed by the sidecar.
No gameplay, test, localisation, asset, spreadsheet, or Git writes occurred, and no AI coefficient audit was repeated.
The timer tranche is **not ready** at this inspected revision because the remaining F1 and F5 gaps below were reproduced through production source.

### Updated dispositions

| Finding | Disposition at this review | Evidence and remaining limit |
| --- | --- | --- |
| F1 exact mission identity | `unresolved`, partial implementation exists | Bound authorization equality protects established contracts, but the success trigger still accepts a historical completion with no bound authorization and site capture can follow a changed selector after activation |
| F2 returning-row cap/index | `unresolved`, full-spec repair remains necessary | Spare-cap guard and unconditional `center_count` index remain at main-effect lines 1263 and 1340, with a small exact repair described below |
| F3 cleanup before adoption | `unresolved`, full-spec lifecycle repair remains necessary | Matching source episode still authorizes clearing an open unadopted transfer at main-effect line 3165 |
| F4 pause/native deadline | `implemented` for the authority-loss cancellation disposition, source evidence only | New mission context requires current ownership/control, so a lost site makes native `cancel_trigger` true and cancellation clears identity without charging or applying mission failure pressure, while state work remains preserved |
| F5 guarded callbacks | `unresolved`, partial implementation exists | Matching completion and duplicate callback suppression pass, but timeout lacks the absolute-expiry predicate and context/sync omit coherent-duration validation |
| F6 forecast/accepted Severity sampling | `implemented` for the inspected Regional Works source path | Actual parsed `complete_effect` forecast matches accepted duration using the mapped immediate delta, with visual/native tooltip execution still outside this evidence |
| F7 malformed adoption/completion | `implemented` for the named adoption, completion, and processor entry points | Shared coherence rejects missing fields, fractional/out-of-range work, and incorrect cuts before active adoption commits a row, episode or national slot |

F7 does not establish that every duration consumer is guarded.
The timer/callback omission is retained under F5 rather than claiming universal malformed-record rejection.

### Validation performed

Reran `python -B .tools/test_event035_center_projects.py`, and all 15 tests passed.
Read and ran `python -B .tools/test_event035_project_duration.py`, and all six tests passed.
Those six tests execute production quote calculations for the five factors, caps, fractional damage, protection, frozen accepted work, exact timer authorization, and the actual parsed Regional Works `complete_effect` forecast.
They are source tests with declared native primitives, not an engine scheduler, AI, save, or native UI test.
They do not cover every callback rejection or initial activation/selection interleaving.

Additional in-memory probes executed the production helper/trigger bodies without writing tests:

- Thirteen coherence cases passed, covering structural bounds 133/245, below/above bounds, fractional required work, wrong certification cuts, protection 42/cut zero, invalid protection records, and each missing mandatory field.
- Missing required work and missing cut both rejected active adoption before successor row count, episode, or active-slot mutation.
- A bound native timer model matched accepted due day plus seven days, replay produced zero delta, a signed negative delta shortened the timer to 17 remaining days, and later selection did not rebind an established site.
- Authorization-mismatch timeout applied no debit or pressure, and cancellation cleared site, episode, authorization, and deadline fields.
- Exact successful completion cleared all four fields, and subsequent complete/timeout callbacks applied no additional debit or pressure.
- At stored expiry, the synchronization helper applied one timeout, removed the native mission, cleared the identity, and rejected duplicate pressure on callback replay.
- A production selector changed between two valid registered centers after native activation and before the first capacity refresh, and that refresh bound the second center.
- An unbound mission success predicate accepted an existing completed receipt.
- The parsed native `timeout_effect` applied pressure while the bound stored deadline was still in the future.
- A bound record missing its certification cut failed duration coherence but remained context-valid, eligible for synchronization, and eligible for timeout pressure.

The first timer probes extended the existing executor only with a COUNTRY mission-time getter and signed native extension primitive in memory.
The parsed callback and expiry probes then used the parent's `DurationRuntime`/`BankRuntime` native deadline model directly.
No production helper was substituted with a fake implementation.
These failures prove the source guards are missing under the declared inputs and do not establish that the native scheduler will spontaneously deliver an early timeout.

### Exact narrow repair locations for the parent

1. In `035_great_depression_decision_surface_triggers.txt:2277`, replace the objective's OR branch at lines 2282-2285 that permits missing mission authorization with mandatory authorization presence, mandatory completed-authorization presence, and exact completed-authorization equality.
The waiting mission context may remain explicitly unbound, but an unbound context must not constitute success proof.
Ensure the bound receipt is captured before the project processor can complete work during the same receiver call.
The current post-processing sync skips completed work because it requires an unspent authorization, so merely removing the permissive success branch can strand a completion whose first synchronization arrived after processing.
Capture identity separately before processing, then synchronize the native timer after accepted due-day changes.

2. At `035_great_depression_decision_effects.txt:64-73`, pair site/episode capture with the authoritative mission activation transaction rather than a later refresh of `great_depression_selected_center_state`.
Once captured, selection changes must leave that receipt intact.
Use a verified native hook or the existing owner's explicit `activate_mission` path, preserving the accepted activation cadence.
This sidecar does not invent an undocumented activation-effect field or authorize a new maintenance scan.

3. In `035_great_depression_project_duration_effects.txt:98-105`, replace the positive required-work-only test with `great_depression_center_project_duration_is_coherent = yes` while retaining exact registration, owner/controller, project episode, and unspent-authorization checks.
Apply the same coherence contract to a bound mission context so malformed work cannot authorize either completion or failure.
Keep a deliberately pre-authorization waiting context distinguishable from a malformed bound contract.

4. In `035_great_depression_decision_effects.txt:2684-2687`, require actual stored expiry before bound-contract timeout pressure.
For a bound authorization, require a deadline and `global.num_days` greater than or equal to that deadline through `check_variable`.
Preserve any intended unbound waiting-mission timeout separately under its own explicit native mission contract rather than treating missing expiry proof as valid bound timeout.
Also retain both terminal outcome exclusions in the successful callback guard, so completion and failure are mutually exclusive even if a repair path has retained fields.
Every consumed success/failure receipt must still clear all four fields once.

5. For F2, change the adoption's country guard around main-effect line 1263 from unconditional spare capacity to `existing exact array row OR spare capacity`.
The existing-row condition in that ROOT country block can use `is_in_array = { array = great_depression_center_state_ids value = PREV }`, where PREV is the adoption state.
Replace the unconditional index assignment at line 1340 with an existing-row lookup before append.
When the exact state already occurs in ROOT's array, find its actual index in that bounded array and assign it to the state.
Otherwise assign the next index from `center_count` and retain the existing aligned append and count increment.
Do not increase the cap or add an unrelated registry.
Test existing-row regain both at full capacity and below capacity, asserting unchanged state-array length, reused index, and aligned stage/due mirrors.

6. F3's repair starts at `great_depression_clear_registered_center_runtime`, main-effect line 3165.
Episode equality alone must not delete a live open transfer whose local work is still owned by the transfer contract.
Preserve that record before clearing the source arrays and retiring the source episode, or settle it through an explicit transfer resolution that keeps the accepted work/receipts with the intended successor.
An indiscriminate exclusion of every historical transfer receipt is insufficient because receipt history survives adoption and later transfers.
The exact open-contract and physical-holder disposition belongs to the parent's full-spec lifecycle repair.
This source ownership issue is outside this sidecar's write authority and is not silently accepted as completion of the overall event.

### Retained Public Works gate and broader scope

The parent explicitly directed that this duration tranche retain `great_depression_center_public_works_target_is_valid` requiring Reopened at decision-surface trigger lines 923-928.
Disposition: `accepted and queued` for the mapped Regional Works eligibility/need and native map-improvement repair, with the acceptance basis being the parent's notification that those surfaces are next work and Public Works is not claimed fully implemented.
The actual forecast test correctly uses a Reopened fixture and does not prove Distressed or Idled centers can launch Public Works directly.
Do not weaken the retained gate inside this read-only duration audit or mark the overall Public Works route complete from the six passing tests.

### Reference and MCP coverage for this review

Read installed trigger documentation for `modulo_temp_variable` at 6442-6454, `subtract_from_temp_variable` at 7624-7630, and `set_temp_variable` at the live returned heading span 7482-7488.
The installed trigger-document revision is `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
The prior offline Data structures trigger/temp-variable and mission references remain applicable and were not replaced by web sources.
MCP snippet validation recognized the native command kinds and STATE scope but returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, and five unchecked argument blocks, so no complete validator pass is claimed.
Its installed-document inventory revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
Narrow live processor source lookup revision was `05e6ade29f7643fef2d6ce05b90835cf4104c5e4c6b23bc5855bd0aafc937a33`, and timer helper lookup revision was `881cd8ba2d5714699eea2db4405ef7a20707ce7ad15e0edfe31d67bb302b4bf6`.
The earlier focused event render/inspection limitations remain unresolved and were not disguised as native timer execution.

Observed SHA-256 identities for this review:

| Source | SHA-256 |
| --- | --- |
| Main effects | `72e7f72aba5ec7dc7abfeeec6a0ac6162d460616cd882a1b794e0659f974301e` |
| Decision effects | `2c21bd81f911cf9a3ca2d0297c7c2b0dc067f03af41937f234fbe7e18faf3b4d` |
| Duration effects | `4fd9c70c1a5be03780c638c2b79b9988094227b3f2162ce01f88eb39e485aeb2` |
| Duration triggers | `18fee0dbbb1921bfd0b10ad29c5875bf29b414fa18122e2e3832603d28871053` |
| Decision-surface triggers | `6a829adea9c72d08b62b2510082fd67253b3633d11ce49f14d402cd6e05d6f8c` |
| Six-case duration suite | `8fdf961fb508daae438523074c761b90e6e8d593017af53c81eb768ad53a3cd6` |
| Fifteen-case center suite | `9c5f1728c83c437b8bad54b0f2be420b289564dffe78ff7f818e43ff0de1e41e` |

Completion boundary: coherence and the inspected Regional Works forecast path have concrete source-test evidence.
Initial mission binding and bound callback eligibility/expiry remain local blockers for this timer tranche.
F2/F3 and the mapped Public Works need/map improvements remain outstanding full-event work.
No simplification or fallback was applied, and only the parent can reconcile the final patch and claim tranche or event completion.

## Follow-up on explicit owner activation and the shared objective cap

The parent replaced automatic Reopen Center activation with `activation = { always = no }` and added `great_depression_process_center_mission` in the existing affected-country receiver before pulse cadence gating.
The authorizer also invokes that owner helper after freezing its project record.
No new world iteration is introduced by these call sites, and the existing country receiver supplies the intended ROOT.
Narrow live lookup revision for the owner helper was `3d5952958fc44ea2591163d7933b457bc2c3e7d0de360655c13c8bdf0b7d30cf`.

The helper calls the old `great_depression_should_activate_reopen_depression_center` gates, including the shared main-objective slot predicate.
That predicate checks native active mission identities directly and rejects every other main objective, rather than trusting a stale counter.
After activation, capacity refresh captures site/episode in the same synchronous owner transaction and synchronization binds paid work.
This closes the previously demonstrated selection-change interval between automatic activation and a later unrelated refresh along the intended owner path.
The helper also cancels an existing mission whose site/authority context is invalid before considering activation, without applying Severity pressure.

Reran the latest duration suite with eight tests and the center suite with fifteen tests, and both passed.
The eight duration tests include owner activation, authority-loss cancellation without failure pressure, and expired resolution with a late duplicate callback applying pressure once.
These remain production-source tests over declared native primitives, not native scheduler execution.

Additional source probes addressed the parent's protection/cap question:

- With each of the nine other main objectives active, a protection authorization did not add Reopen Center or any second main objective.
- With two support objectives active and the main lane empty, structural work added exactly one center mission, producing three active objectives.
- Replaying owner mission processing retained those same three objectives.

Disposition: `implemented` for explicit activation pairing and preservation of the old shared objective cap, with native scheduler timing still unobserved.
The cap result does not establish that every project type is a valid work receipt for the reopening objective.

### Additional finding F8: protection work must not supply a reopening deadline

The supported `great_depression_authorize_center_project` protection branch can run on an Idled selected state.
The new owner activation correctly respects the main-objective cap, but its synchronization helper accepts that protection authorization as the reopening mission's work receipt.
An actual-source probe produced a reopening deadline of 42 treatment days plus seven grace days.
At day 42, project processing completed protection and applied the protected treatment, while `great_depression_reopen_depression_center_objective_is_met` remained false because the center was not reopened.
At day 49, the timeout callback applied failure pressure despite successful protection treatment.

This is a supported-authorizer compatibility issue and does not assert that the ordinary player-facing Protect Center action reaches that authorizer.
The current `great_depression_protect_selected_center` action uses its separate immediate treatment path.
The existing protection source test exercises the authorizer API, so its valid short treatment should remain valid without becoming a short reopening deadline.

Exact narrow repair: in `great_depression_sync_center_project_mission`, add a type exclusion for `constant:great_depression_center_project.protection` alongside its coherent-work gate before capturing mission authorization or copying project due day.
Apply the same exclusion when validating an already bound reopening receipt, so a protection-bound context cannot authorize timeout pressure.
Retain the old mission activation gates, allowing a waiting reopening objective where those gates intend one, but do not bind that waiting objective to short protection work.
Then test that protection's 42-day completion remains unchanged, that another main objective still blocks center activation, and that protection cannot shorten or replace an existing reopening contract's deadline.
Disposition: `unresolved`, narrow timer-tranche repair recommended to the parent.
No gameplay change was made by this sidecar.

### Remaining readiness limits

F1's initial activation/capture interval is resolved on the explicit owner path.
Its separate success-predicate OR branch that permits an absent bound authorization remains in the inspected decision-surface trigger and is not marked resolved.
F5 is partially improved because synchronization now includes duration coherence, but the inspected native timeout callback still checks context and terminal flags without requiring bound deadline expiry or coherent bound work.
Its decision-effect bytes remained unchanged from the earlier reproduced early/malformed callback cases.
The passing expired/late-duplicate test establishes the accepted expiry path, not rejection of early or incoherent callbacks.
Those F1/F5 limits and F8 remain timer-tranche follow-up work.
F2 existing-row cap/index reuse, F3 cleanup-before-adoption, and the mapped Public Works eligibility/map-improvement repair remain outstanding full-spec work as already recorded.
Only the handoff was edited, no AI coefficient work was repeated, and no simplification or fallback was applied.
The reviewed owner-duration effect SHA-256 was `83855653440827049e3666f2087a56e6d598a2586a20e0909f2221baad1c0599`, callback decision effects remained `2c21bd81f911cf9a3ca2d0297c7c2b0dc067f03af41937f234fbe7e18faf3b4d`, and the eight-case duration suite was `11c4059e166cf9c1a1b1596b6d6e4378c22d33a9ffefa65278def6433e2fcb8b`.

## Final bounded review after the remaining timer and transfer repairs

This section supersedes the earlier timer-tranche not-ready assessment for the inspected core helpers and callbacks.
The bounded architecture review passes on source evidence and the tests below.
The finished tranche still awaits the parent's selector patch and the required probability auditor comparison, which were explicitly reserved to the parent and auditor.
The overall Event 35 and Public Works implementation are not declared complete.
Only this handoff was edited by the sidecar, and no gameplay, tests, localisation, assets, spreadsheet, or Git writes were made.

### Evidence from the latest source and executed tests

The duration suite had grown from the parent's announced twelve cases to thirteen when executed.
All thirteen duration tests passed, including the added matching-paid-completion and late-success rejection case.
All fifteen center-project tests also passed.
Commands were `python -B .tools/test_event035_project_duration.py` and `python -B .tools/test_event035_center_projects.py`.
No test source was changed and Python bytecode generation was disabled.

Current objective proof at decision-surface lines 2281-2297 requires a present positive mission authorization, a stored unexpired deadline, and exact completed-authorization equality.
Its context also compares the current live authorization, requires coherent bound duration, and rejects protection work.
Thus both current and completed authorization must identify the same bound receipt.
The prior unbound historical success branch is gone from the objective.

The native timeout helper at decision-effect lines 2683-2699 requires a stored deadline and actual expiry before any pressure, plus valid context and both terminal exclusions.
Successful completion excludes failed as well as completed outcomes.
The source tests demonstrate an inert historical/unbound success, inert early timeout, exactly one expiry pressure, exactly one matching completion debit, and inert late/duplicate completion or timeout.
Completion is only valid before the stored deadline, while timeout becomes valid at that deadline, so their date boundaries do not overlap.

Protection is excluded before mission authorization binding and due-day synchronization.
Explicit activation records a separate waiting deadline from the existing 135-day mission tuning.
The protection test shows no bound reopening authorization, a retained 135-day waiting deadline, no pressure at day 49, and rejection of an artificially protection-bound context.
The intended 42-day treatment remains separate from structural work.

The adoption country preflight now permits an existing exact array member or spare capacity.
The row lookup starts from the actual array length for a genuinely new row and scans the existing bounded array for the exact adoption state when reusing a row.
It assigns the found real index before changing episode identity and writing both stage and project ledger mirrors.
No new append, count increase, cap increase, or duration re-quote occurs for an existing row.
The suite covers row zero at counts two and four.
Additional in-memory probes moved the returning state and all aligned columns to nonzero indexes one and three, seeded a stale index of 99, and executed production adoption.
The helper reused those nonzero indexes correctly, kept row counts two/four, and wrote the due-day mirror to the correct row.

The cleanup exclusion at main-effect lines 3185-3193 requires all of the exact episode, transfer receipt, open transfer contract, matching transfer-source episode, and foreign ownership facts.
The matching open foreign-transfer test preserved all project fields, including frozen required work and certification metadata, while ordinary owned retirement cleared them.
Additional source probes confirmed that a closed contract, absent transfer receipt, wrong transfer-source episode, or ownership returned to the source country does not receive the preservation exception.
Those records retire normally under the calling source episode.
The PREV reads in this state loop identify the cleanup owner correctly.

### Final finding dispositions

| Finding | Current disposition | Concrete evidence |
| --- | --- | --- |
| F1 exact mission identity | `implemented` for the reviewed owner/receipt path | Explicit activation/capture, positive bound authorization, current/completed exact match, unbound historical success rejected |
| F2 returning-row cap/index | `implemented` for adoption, selector patch `accepted and queued` | Existing membership bypasses append-cap gate, exact nonzero indexes reused at counts two/four, no duplicate rows or cap increase |
| F3 cleanup before adoption | `implemented` for the reviewed cleanup contract | Exact open foreign source transfer survives, all four near-miss cleanup probes retire normally |
| F4 pause/native deadline | `implemented` for the established authority-loss cancellation contract | Existing scope-loss test cancels without Severity and retained work survives transfer/resume source paths |
| F5 callback safety | `implemented` for the reviewed callbacks | Deadline expiry and terminal guards, coherent bound context, one completion debit, one expiry pressure, early/late/duplicate rejection |
| F6 forecast sampling | `implemented` for the actual Regional Works duration path | Parsed Reopened-fixture `complete_effect` forecast equals the accepted post-action quote |
| F7 malformed work | `implemented` for reviewed duration consumers | Mandatory fields, integer work, exact cut, and type-specific bounds guard adoption, processing, completion, and bound mission context |
| F8 protection/reopening mismatch | `implemented` | Protection cannot bind a reopening deadline or success, waiting deadline stays 135, day-49 timeout is inert |

### Selector and audit gate retained explicitly

The parent's acceptance basis for queuing the selector change is the explicit instruction to await the AI auditor's baseline acknowledgment before applying it, then obtain the required comparison.
The actual selector still uses its old spare-cap-only transfer branch.
An additional source probe confirmed that this selector admits the returning two-row fixture but rejects the returning four-row fixture, even though direct adoption now correctly accepts and reuses both rows.
This is an acknowledged queued integration step, not an end-to-end full-cap selection pass.
Do not mark F2's player/AI selector surface complete until the owner patch and auditor comparison are reconciled.
No probability work was repeated by this sidecar.

The mapped Public Works eligibility/need and native map improvements remain queued under the parent's earlier explicit scope decision.
The Reopened-only gate was retained, and the passing forecast test does not establish direct Public Works availability in Distressed or Idled centers.

### MCP coverage and validation limits

Used only narrow source lookup for adoption and cleanup, without repeating broad event or probability inspection.
Adoption structure revision was `0e3eb0da6b7506a2391331f23d1013c2475f39560377fdf432f499ae5fb666e1`.
Cleanup source revision was `8ae6541434c0a2a85e07c56e4e42dc12f312745c69364d26e582ba8a3d11fa77`.
The source tests execute production helper, trigger, action, and callback logic with explicit native primitive fixtures.
They do not establish native scheduling, scope-pointer representation in the engine, saves, UI rendering, or in-game execution.
Earlier MCP event-render and argument-validation limitations remain recorded, with no complete native lifecycle validation claim.
No new architecture blocker was found in the requested core hunks.
Parent commit readiness still depends on the queued selector integration and mandatory auditor comparison.
No simplification or fallback was applied.

Observed SHA-256 identities at this final bounded review:

| Source | SHA-256 |
| --- | --- |
| Main effects | `e0c992b2041df8638385119c337040a380d9ce01e7dbaf351ecec2944d047750` |
| Decision effects | `f51d0f777c93f4a2ee22a1796a322bfa2dd7cf5d4e99044d1cbd4b313993af9a` |
| Duration effects | `7445da4c5807a2e565119d34ce5461f648cffc1d9f2d44e0fd5b1638ef771156` |
| Decision-surface triggers | `6c6ab9dfe250812da64f23494332395edaa96a00962f80d59f1a24674f0f6a99` |
| Thirteen-case duration suite | `7f84132d6506d56f9f435f1dc9e7270104a0657c78c250d6348f37c261719266` |
| Fifteen-case center suite | `4977de0be24dbc2d03fcd3d2bc131b5ff8231c8771e7985e302eaaa37f8048b4` |

## Final selector disposition after auditor baseline acknowledgment

F2 selector source disposition is `implemented`: direct inspection confirms the transfer branch now accepts exact existing state-array membership OR spare capacity while retaining ownership, control, open-transfer, and active-crisis gates.
The inspected source SHA-256 is `27bc69fc602b9c553e6a9e95820595bf16d6f5cc251c1588d75311c2e7f201fa`.
Read the six-case selector test and the complete owner helper documentation in `common\scripted_effects\035_great_depression_project_duration_effects.md`, which records purpose, scopes, inputs/outputs, side effects, transfer behavior, and validation limits.
The selector test declares existing-row counts four/two accepted, new-row count four rejected/count two accepted, foreign control rejected, and closed stale transfer rejected.
The parent's fourteen-case test run remains pending on its existing handle `40010` in this sidecar's evidence, and the previously confirmed thirteen duration/fifteen center results are not promoted into a fourteen-case pass.
Native probability disposition remains `unresolved` pending the delegated comparison over the same six XFER scenarios and immutable before/after source bindings, with before identity beginning `6a829ade` and the exact after identity above.
The parent reported that the selector patch followed the AI owner's baseline acknowledgment, but no comparison outcome or AI balance acceptance is claimed here.
No broad MCP, probability rerun, world scan, gameplay/Git write, AI coefficient change, asset work, simplification, or fallback was performed by this sidecar.
