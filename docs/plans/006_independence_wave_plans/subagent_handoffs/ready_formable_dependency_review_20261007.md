# Ready-formable dependency review — 2026-10-07

Disposition: bounded read-only audit completed; the reviewed source has protocol defects requiring owner correction before a consistent source commit.
General MCP delays do not block delivery of this report.
No gameplay, localisation, GUI, asset, Git, or index changes were made.
This Markdown report is the only authored file.

## Scope and acceptance

Reviewed FORM-17/32/36/37 against D30/D31/D33 in `docs/plans/006_independence_wave_plans/agent_decisions_2026-10-04.md:779-834,868-884`, Part 6's sovereignty contract in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md:78-87`, and the named `ready_formable_contracts_20261006.md` handoff.
The parent expressly owns final source correction, related-hunk selection, review and commit.
The parent's latest message reports seven legal/failed/replay callback cases with passing success flags, a resolved signature-helper inventory, and review of the four-family shared-registry diff.
Those are parent-reported results; this audit does not recast them as independently observed engine tests.

The engine-loaded paths are `common/decisions/` and `common/script_constants/`, rather than the abbreviated `decisions/` and `constants/` paths in the initial prompt.
The review covers the ready-formable files, four-family shared registry/readiness/identity branches, ATJ/IAX signature entry and achievement dependencies, institutions, invitation receipts, and puzzle/category/cosmetic dependencies.
It does not choose AI weights, change balance, audit unrelated focus routes, or claim visual or live-engine acceptance.
No opinion-modifier definition matching `ready_formable` was found, and these adapters use access and guarantee effects rather than a new opinion modifier.

## Critical protocol findings

### F1 — Eight unresolved member-selector calls in the shared registry

`common/scripted_effects/006_independence_wave_formable_registry_effects.txt:2356,2360,2364,2368,2647,2651,2655,2659` calls `is_independence_wave_ready_formable_member_for_root`.
The definition at `common/scripted_triggers/006_independence_wave_ready_formable_contracts_triggers.txt:235-258` is `has_independence_wave_ready_formable_member_for_root`.
A definition/reference inventory over all current scripted-effect and scripted-trigger files found no definition for the called spelling.
The eight unresolved references are the invitation issuance and member-ledger branches for these four families.
The same inventory found no other unresolved literal Event 006 helper calls in the eleven audited files, including the signature effect and trigger modules.
This agrees with the parent's signature-module inventory while identifying a separate shared-registry defect.

Owner action: align those eight call sites with the existing helper.
Do not introduce an alias or widen member eligibility as a substitute.
The MCP command checker returned `SCRIPT_COMMAND_UNRESOLVED` for the called spelling; that result alone cannot resolve custom helpers, so the source inventory supplies the missing-definition evidence.

### F2 — Identity application invalidates the immediately following integration proof

Each identity adapter sets its family global `identity_in_use` flag before setting `independence_wave_formable_identity_committed`: ready effects `:584-642`.
The generic commit then calls the integration adapter: registry effects `:3048-3058`.
Each integration adapter requires `has_independence_wave_ready_formable_runtime_commit_proof`: ready effects `:699-769`.

That proof still calls `has_valid_independence_wave_formable_founding_proposal`, which calls `is_valid_independence_wave_formable_founding_carrier`.
The four founding-carrier branches require identity clearance: registry triggers `:1127-1150,1347-1356`.
Identity clearance explicitly requires the same global lock to be absent: ready triggers `:434-440`.
Consequently the carrier rejects its own identity lock after a successful identity mutation.

There is a second rejection path: runtime proof calls commit readiness; registry triggers `:1548-1563` calls `has_independence_wave_formable_identity_compatibility_gate`.
Its owner definition is `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:414-424`.
For these non-IW043/IW058 signature families it delegates to `has_independence_wave_selected_formable_identity_available`, whose four branches also require absent locks: form01/02/04 triggers `:128-142`.
Correcting only the founding-carrier branch therefore leaves another rejection.

Source case: declare the correct member/roster prerequisites true, evaluate each family before its lock, then apply that adapter's global lock and evaluate again.
All four parsed-source cases changed from true to false.
The generic success branch requires both committed flags; integration cannot set its flag under this state and the transaction enters the failure/rollback path at registry effects `:3060-3064,3111`.
This is a source-order defect, independent of the timed-project callback tests.

Owner action: preserve the pre-mutation uniqueness check, and use a generation/family/transaction-owned proof after identity mutation that recognizes the current carrier's own reservation.
Keep other carriers excluded.
Review both rejection paths rather than relaxing a global gate indiscriminately.

### F3 — Carrier-driven cleanup removes reciprocal relations against ROOT instead of the member

Carrier rollback calls `independence_wave_ready_formable_cleanup_autonomous_members`, which scopes into each recorded member and calls `...cleanup_autonomous_member`: ready effects `:824-825,858-880`.
ROOT remains the original carrier along this call path.
The member helper enters the stored cleanup-carrier target, then removes relations with `country = ROOT`: `:903-909`.
Those commands address carrier-to-carrier relations, rather than the recorded carrier-to-member access and guarantee.
The member's reciprocal receipt flags are subsequently cleared at `:918-921`, losing the remaining cleanup ownership evidence.

Member-to-carrier removals at `:895-901` address the stored carrier correctly.
A direct member-owned cleanup invocation also has a different ROOT context, so testing that entry alone does not cover carrier rollback or carrier origin cleanup.

Owner action: capture the actual member scope before entering the carrier and use that pointer for both reciprocal removals.
Retain generation-bound ownership checks and preserve relations that predate the contract.
This finding is a source scope/endpoint trace, not an observed native diplomatic mutation.

### F4 — The generic consent evaluator's temporary output lacks caller-owned storage

Registry effects `:2666` calls `independence_wave_formable_evaluate_candidate_consent`, then reads its temporary output at `:2676` and appends it at `:2689`.
The evaluator first creates `independence_wave_formable_candidate_consent` inside its own frame at `:2488`.
The builder does not initialize that output before the call.
The only later initialization in this builder is the existing Balkan special case at `:2672`; it does not protect the four ready-formable families.

Actual-source call-frame cases used accepted and withheld human receipts, with and without caller-owned output storage.
Without preinitialization, the evaluator internally computed the proper symbolic consent value but the conservative return model discarded the newly created scalar.
With caller preinitialization, its modifications survived return.
The documented lifetime contract requires the latter pattern.
This is a generic dependency defect exposed by the new readiness/commit callers, rather than a missing output from the meta identity dispatcher.

Owner action: initialize the scalar in the ledger builder before each evaluator call; any outer consumer of a forwarded temporary output must likewise own its storage.
Do not reset an existing cursor or unrelated helper input.
The ledger arrays/counts/readiness receipts returned to the new wrappers are normal country state, so they do not need temporary-output forwarding.
The new integration helper's counters are consumed inside that helper, and integration success is published through a country flag.
The signature CXT daily caller initializes `chaosx_test_country_extension_registration_added` before calling its wrapper, and the wrapper initializes it before calling the generic registration helper: CXT on-actions `:26-31`, signature effects `:19-25`.
That output chain is correctly owned; startup does not read the output after return.

### F5 — A removed/replaced cosmetic tag prevents release of owned identity state

Ready effects `:826-853` gates each carrier rollback block on both its carrier receipt and the expected current cosmetic tag.
If an external identity change has already dropped/replaced NCX/IDX/MRX/MSX, the block skips clearing the global identity lock, carrier receipt, and charter/restoration receipts.
The unconditional tail only clears integration completion/count.
Runtime cleanup reaches this helper whenever a carrier receipt remains, but does not repair the skipped block: `:929-949`.

Parsed-source cases for ATJ/MRX and IAX/MSX confirmed that an intact cosmetic releases the lock and restores the recorded live institution.
With another current cosmetic, the lock and carrier receipt remain, and the old institution is not restored.
The other two families have the same guarded structure.

Owner action: release owned reservation/charter receipts even when the expected cosmetic is absent.
Only drop a cosmetic when the contract still owns that particular cosmetic.
Keep the live-framework restoration gate so an ended package cannot resurrect its institutions.

### F6 — CXT readiness repair calls carrier-root helpers with ROOT still CXT

Signature effects `:28-98` runs a `for_each_scope_loop` over the active-country registry from the CXT extension and calls `independence_wave_focus_register_formable_family` in selected ATJ/IAX country scopes at `:70,94`.
The registration wrapper at `common/scripted_effects/006_independence_wave_focus_effects.txt:287-291` delegates to the selected-family readiness dispatcher and the new readiness adapter.
That adapter calls country/anchor roster helpers and the generic ledger builder which interpret ROOT as the proposing carrier.

A country scope entered from the CXT-owned loop does not rebase ROOT to ATJ/IAX.
The connection checks therefore compare members to CXT, and registry candidate checks read CXT's profile family rather than ATJ/IAX's.
This repair path does not satisfy the normal country-owned registration contract.
The outer selected-family/no-consent gates do not change ROOT.
Normal route decisions and signature entry executed with ROOT equal to the acting country are separate entry paths.

Owner action: provide the readiness path with an explicit carrier scope/contract, or invoke a correctly scoped deferred registration entry.
Preserve the existing debug extension's bounded registry and player-triggered application boundary.
No runtime behavior or AI design change is proposed here.

## Invitation, sovereignty, and restoration evidence

The normal invitation path writes carrier, carrier generation, member generation, family and sequence before delivery.
Delivery rejects a second pending/shown popup, consumes the delivery flag before presentation, and verifies the carrier pointer and live proposal: ready effects `:118-150`, ready triggers `:578-604`.
Event `chaosx.nr6.8617` has refusal first, an explicit thirteen-day timeout, and acceptance guarded both for initial option visibility and at effect execution: events `:16-44`, ready effects `:153-167`.
Refusal clears accepted/declared flags through the generic withholding helper at registry effects `:2462-2479`.
A stale sequence/generation while the original popup receipt remains unchanged fails the reply predicate at ready triggers `:563-576`.
None of these paths authorizes territory transfer or subject creation.

There remains an unresolved stale-popup replacement case.
An old event callback carries no immutable sequence/family/generation argument; both options and `after` read or clear the country's current popup storage.
Proposal cleanup clears that storage through registry effects `:690-712`; a later invitation can populate it again.
If the old native popup can still resolve after a newer popup receipt is installed, its acceptance helper will validate the newer receipt and can accept the newer invitation; its refusal or `after` can also alter/clear the newer receipt.
The callback never compares the original event's FROM or a per-event immutable request receipt.
The source cannot distinguish those two callbacks.
Native coexistence/closure of these popups was not established, so this is an unresolved lifecycle case, not a claimed observed exploit.
The parent should cover old-popup response after proposal withdrawal and replacement, including a changed carrier, before claiming no stale consent.

Membership gates retain exact original tag, package ID, stored anchor, owned/controlled capital, active Event 006 origin and aligned registry membership.
The ledger builder additionally compares the candidate to the aligned registry generation.
FDX's 440/986 alternatives are retained; FORM-32 requires four entries.
FORM-36 requires ports at 1050/673/1052.
The new member installer changes only matching institutions and receipt-owned access/guarantees.
It does not call annexation, subject creation, state transfer, core grants, origin ending, focus loading, or unit mutation.
The generic dispatcher has unrelated absorption helpers, but the four ready-formable adapters do not call them.

Institution restoration was tested from the actual parsed install/restore bodies under explicit package/live-framework facts:
28 cases cover each of ATJ's four and IAX's three governance choices as carrier/member, both live and ended; repeated installation was checked in each case.
Eight further cases cover absent and ambiguous governance choices for both roles and packages.
All 36 cases passed their bounded assertions: live restoration returned the recorded L2/L3 idea, ended frameworks restored none, repeated installation changed nothing, absent/ambiguous choices granted no substitute, and an unrelated sentinel idea remained untouched.
The restore helpers clear replacement receipts after attempting restoration: ready effects `:412-504`.
These models do not execute package cleanup, diplomacy, map ownership, native callbacks or engine idea-slot limits.

Package cleanup precedes decision/formable cleanup during generation reset and origin end: core effects `:468-476,3133-3137`.
The restoration outer gate checks `is_independence_wave_regional_framework_live`, whose definition requires current generation, framework setup receipt and a non-ended origin: regional triggers `:217-222`.
That ordering protects the departing package while allowing a still-live sovereign member to restore its recorded institution.
The ATJ/IAX charter stage-2 achievement predicates explicitly depend on postformation carrier proof, both completed stages and the stage-2 charter: signature triggers `:321-345`.

## Consistent commit tree

This is a source dependency/hunk map for the parent, not a statement about the Git index or which files are already committed.
No Git command or index inspection was performed.
Stage only the related owned content and listed four-family hunks; do not stage whole shared files merely because they appear here.
Resolve F1–F6 in their owning source before calling the commit consistent.

### Owned ready-formable source

- `common/script_constants/006_ready_formable_contracts_constants.txt`
- `common/ideas/006_independence_wave_ready_formable_contracts_ideas.txt`
- `common/scripted_effects/006_independence_wave_ready_formable_contracts_effects.txt`
- `common/scripted_triggers/006_independence_wave_ready_formable_contracts_triggers.txt`
- `common/scripted_triggers/006_independence_wave_ready_formable_state_puzzle_triggers.txt`
- `common/decisions/006_independence_wave_ready_formable_contracts_decisions.txt`
- `common/decisions/categories/006_independence_wave_ready_formable_contracts_categories.txt`
- `events/006_independence_wave_ready_formable_contracts_events.txt`
- `localisation/english/006_independence_wave_ready_formable_contracts_l_english.yml`

### Shared protocol source — only the relevant four-family hunks and dependency repair

| File | Required related content |
| --- | --- |
| `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt` | Four readiness clears in `...clear_selected_family_readiness` and four dispatch branches in `...register_selected_family_readiness`. |
| `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt` | Four identity-availability branches for NCX/IDX/MRX/MSX and phase-correct ownership proof needed by F2. |
| `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` | Popup cleanup dependency; four invitation selectors and delivery/AI-resolution calls; four ledger selectors; ready-family precommit rebuild; rollback/cleanup integration; the narrow consent-output fix needed by F4. |
| `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` | Four founding-carrier branches; ready invited-member validity; ready-family method/consent allowances; readiness, commit, territory and launch dispatch branches. |
| `common/countries/cosmetic.txt` | Only `NCX`, `IDX`, `MRX`, `MSX` entries, currently beginning at lines 1971/1976/1981/1986. Preserve every unrelated palette entry. |
| `common/scripted_effects/006_independence_wave_signature_modules_effects.txt` | Related ATJ/IAX readiness repair and FORM-36/37 entry calls; keep their source wrapper definitions available. |
| `common/scripted_triggers/006_independence_wave_signature_modules_triggers.txt` | FORM-36/37 selection gates and both postformation charter achievement predicates. |

### Four-family puzzle consumer source — matching hunks only

- `interface/chaosx_formable_state_puzzle_group_independence_wave_formables.gui`: the four overlays and fourteen state pieces; preserve the fifteen earlier overlays.
- `common/scripted_guis/chaosx_formable_state_puzzles.txt`: the same four context/overlay branches, fourteen image properties, and FDX alternative visibility in `independence_wave_formable_state_puzzle_scripted_gui`.
- `interface/chaosx_formable_state_puzzles.gfx`: the twenty-eight qualifying/unresolved sprite definitions for those fourteen pieces.
- `common/scripted_localisation/chaosx_formable_state_puzzles.txt`: corresponding sprite/qualification/count/status getters for the four families.
- `localisation/english/chaosx_formable_state_puzzles_l_english.yml`: the four summaries and fourteen state tooltips.
- `docs/formables/state_puzzles/006_form17_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form32_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form36_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form37_state_puzzle/manifest.json`

The matching geometry references are the `independence_wave_form17_state_puzzle_geometry_artifact.json`, `independence_wave_form32_state_puzzle_geometry_artifact.json`, `independence_wave_form36_state_puzzle_geometry_artifact.json`, and `independence_wave_form37_state_puzzle_geometry_artifact.json` files in those same four directories.
Their referenced DDS pairs under `gfx/interface/formables/state_puzzles/006_formXX_state_puzzle/states/` must already exist in the commit tree or accompany their reviewed asset commit.
Both new categories attach the exact grouped GUI; a standalone category named after a manifest is not a replacement for these real entry points.
The manifest required summary counts are 3/4/3/3 across fourteen candidate pieces, including FDX's two alternatives.

The cosmetic flags have a separate reviewed asset handoff and parent palette/ideology correction.
Ensure the reviewed NCX/IDX/MRX/MSX generic and ideology triplets are available in the resulting tree; this audit does not restage them or infer their index status.
No sovereign country-tag registration is required for these four cosmetic identities.

### Definitions that must remain in the tree

| Definition owner | Required API/dependency |
| --- | --- |
| `common/scripted_effects/006_independence_wave_focus_effects.txt:287-291` | `independence_wave_focus_register_formable_family` loads the profile and calls the readiness dispatcher; it does not rebase ROOT. |
| `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` | Profile loading, invitation store/reply/freeze/close, ledger builder/recount, identity/integration meta dispatchers, commit and failure paths. |
| `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:414-424` | `has_independence_wave_formable_identity_compatibility_gate`; retain its existing ownership and avoid unrelated IW043/IW058 edits. |
| `common/script_constants/006_independence_wave_constants_registry.txt` | Existing family IDs, member/consent/method tables, costs, durations, symbolic consent values and generation constants. No new duplicate tuning registry is needed. |
| `common/scripted_effects/006_independence_wave_decision_effects.txt:14,135,205,234` | Country deltas and administration/diplomatic/security payment helpers. |
| `common/scripted_triggers/006_independence_wave_decision_triggers.txt:342,356,379` | Matching cost-affordability helpers. |
| `common/scripted_triggers/006_independence_wave_regional_framework_triggers.txt:217-222` | Live-framework generation/setup/origin restoration gate. |
| `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` | Existing admitted-package setup, FDX 440/986 loader and BLC 1012 binding. |
| `common/scripted_effects/006_independence_wave_effects.txt` and `common/scripted_triggers/006_independence_wave_triggers.txt` | Existing origin/generation/cleanup lifecycle and active-package predicates. |
| `common/decisions/006_independence_wave_formable_decisions.txt` | Existing discovery, method/consent, founding-invitation, congress and formation consumers. |
| `common/achievements/chaos_redux_achievements.txt:711-721` | Signature achievement consumers; retain only the related signature achievement entries if those are part of the parent's source plan. |

If the parent commits the signature modules as a complete new package rather than only the related ATJ/IAX hunks, its own source closure also includes `common/ideas/006_independence_wave_signature_modules_ideas.txt`, `common/script_constants/006_independence_wave_signature_modules_constants.txt`, `common/decisions/006_independence_wave_signature_modules_decisions.txt`, `common/opinion_modifiers/006_independence_wave_signature_modules_opinions.txt`, `common/on_actions/006_independence_wave_signature_modules_cxt_on_actions.txt`, `common/national_focus/006_independence_wave_signature_modules_focus.txt`, and `localisation/english/006_independence_wave_signature_modules_l_english.yml`, with its parent-reviewed focus inclusion, setup/cleanup hooks, institutions and asset wiring.
That is an adjacent package dependency list, not authorization to include unrelated shared diffs or a focus-completion claim.

Documentation to retain/reconcile with owner fixes: the named ready-formable contracts handoff, `ready_formable_puzzles_gui_takeover_20261006.md`, the ready-formable flag handoff, `docs/events/006_independence_wave/systems/formable_registry.md`, and the signature-module documentation.
The present contracts handoff's claims of successful generic commit and complete reciprocal cleanup need correction or fresh owner evidence after F1–F6.
No stale handoff is promoted to acceptance by this report.

## MCP checks and reference evidence

Exposed routes were verified from the connected tool metadata.
Two actual extracted country-scope helper bodies returned `SCRIPT_CHECKED`, `valid = true`, zero unresolved findings and no omitted findings:
`...clear_human_invitation_popup` (11 commands) and `has_...connection_to_root` (12 commands).
Their coverage is syntax, command kind and declared scope only; `parametersChecked = false`.
The actual `...cleanup_autonomous_member` body returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, 28 checked commands, eight unresolved findings and three unchecked native argument blocks.
It also omitted twelve supported findings; unresolved dynamic variable/target scopes and the custom restore helper remain outside that checker's coverage.
This is not a cleanup pass or engine execution.

Reference context/search/read succeeded and supplied these sections:

| Reference | Read span | SHA-256/source revision |
| --- | --- | --- |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 435-443, temporary-variable lifetime and unscoped storage | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, read locally | 260-268, ROOT/THIS/PREV and state-owner/capital scopes | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` | 180-191, immediate/after and first-option timeout | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| Installed `documentation/effects_documentation.md` | 7820-7827, set_temp_variable; 3564-3577, diplomatic_relation | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation/script_concept_documentation.md` | 216-222, shared constants and field-support limitation | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common/script_constants/documentation.md` | 1-34, schema and supported-reader contract | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

Installed paths are rooted at `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
Vanilla `common/decisions/formable_nation_decisions.txt:76-87` was read locally for the existing-carrier cosmetic precedent; its coring effects were not adopted.
The reference-context response listed omitted topics, so no complete context-bundle coverage is claimed.
The script checker used installed command-index revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

A valid event trace retry used workspace `mod_chaos_redux_ea3b2d67c2c0`, selector `{ kind: event, eventId: chaosx.nr6.8617 }`, depth/node/edge limits 1/1/1, and no helper expansion.
It returned no result within the 55-second client bound after the earlier narrow attempt was abandoned without a result.
Decision inventory retried the single FORM-36 stage-2 decision after its declared-unknown-world inspect did not return.
That inventory, event options render, and fourteen-state lookup-only map inspection returned no result within 50-second client bounds.
A source lookup at ready effects line 614 and GUI inspect of `chaosx_independence_wave_formable_state_puzzle_window` returned no result within 20-second client bounds.
These are client no-result limits, not returned server timeout errors, service-version evidence, or source failures.
Initial schema rejections were corrected and are not counted as validation.
No current event graph, map lookup or GUI artifact was produced by those attempts.
The GUI worker's existing artifact/evidence references remain in its handoff; its visual acceptance is not established by this source audit.
No unverified helper-expansion/job/task route was used.
AI/probability acceptance remains with the probability auditor's separate evidence, including `signature_probability_compare_20261007.md`; this audit did not inspect or choose probabilities.

## Source identity and limits

The eleven audited source files were hashed and rechecked before report writing; none changed during that review interval.
Key snapshot hashes are:

| File | SHA-256 |
| --- | --- |
| Ready effects | `30ec8d3d7b4c4d874b0b691f495c4a1ba933f75f8bfff8f1981838adf8b11ed2` |
| Ready contract triggers | `3af50b17c892b99aec4af1e65d735368ddaf7e8b05aa443e1d716b03dddb6992` |
| Ready puzzle triggers | `bab9116bccd202b7ebcc99509f11e8f2decf93610b954bd7c4dfd8c180bf2858` |
| Shared registry effects | `1ee86b707cfc17c4fedfd202b72bcb261519ca9e7717a3d377f73a056f50d558` |
| Shared registry triggers | `f3d279218cf006ed3ec27f21c545460ea18fb536a4464edd2a56c8996b0c8691` |
| form01/02/04 effects | `f763117bab19532fbe50edc4d2c3aca1bfcf7fc215a901b4599f757e1fd81c90` |
| form01/02/04 triggers | `59dd33477113d0cfa76236bbe24de5597978d08c58d743888d2eca38307a932a` |
| Signature effects | `7a9e8f7f84d6142816715aa998be525a3306ae42077fd5ce8c46c4a46ec6ff76` |
| Signature triggers | `31777494886998ebb77fc5e8a2be410803053155fcfdca88483b25643ee34ac9` |
| Ready decisions | `a5cc2a2759fefcd5636e1ef9a0adefbfef3d9f0cb99484d4db234d4c1f1c25a0` |
| Invitation event | `16954e48d9f3279793c573d93284de1b8de2f63b6837d32bb7f39f280f271294` |

The read-only Python cases parsed actual source blocks and executed only the stated ordered flags/ideas/variable/ROOT subset.
They kept normal country state separate from temporary call-frame state and explicitly discarded scalars first created in a returning helper.
External exact membership, current roster and live-package facts were declared fixture inputs rather than derived engine observations.
No broad source evaluator, source patch, test file, log, save, game session, Git operation, or generated gameplay content was created.

Remaining owner work is correction/review of F1–F6, the stale-popup replacement case, and source/commit reconciliation.
Meaningful validation omitted: full native lifecycle execution, current event/helper graph and GUI/map artifacts, native diplomatic mutation, and probability comparison in this audit.
Their absence does not prevent this report, but limits completion claims about the feature.
No implementation simplification or fallback was introduced.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or updated.

## Follow-up read-only review — signature governance ordering and IAX service receipts

Date: 2026-10-07.
Disposition: bounded source review passed for the five completion call sites, ready-owned governance selector, and four-choice IAX institution lifecycle.
The parent applied all reviewed source changes after signature ownership returned.
This worker edited only this report appendix.
No broad MCP, private regression script, gameplay source, Git/index or live-game operation was used.
The earlier F1–F6 findings and source hashes remain historical evidence; this appendix does not claim to re-audit the entire repaired protocol.

### Current source findings

No new source-critical defect was found in this bounded surface.
The five callers retain their original actor/route/one-time completion gates and initialize `independence_wave_ready_formable_governance_choice` immediately before `independence_wave_ready_formable_apply_signature_governance`.
The enum is caller-owned input storage across that nested call.
No temporary output is read after the ready helper returns.

| Signature completion caller | Enum | Current call site |
| --- | --- | --- |
| `independence_wave_atj_signature_complete_district_terms` | `atj_district` | Signature effects 422-424 |
| `independence_wave_atj_signature_complete_school_board` | `atj_school_board` | Signature effects 435-437 |
| `independence_wave_atj_signature_complete_shared_council` | `atj_shared_council` | Signature effects 448-450 |
| `independence_wave_iax_signature_complete_local_charter` | `iax_local_council` | Signature effects 679-681 |
| `independence_wave_iax_signature_complete_river_charter` | `iax_river_office` | Signature effects 692-694 |

The five enum values are defined under `independence_wave_ready_formable_governance` in `common/script_constants/006_ready_formable_contracts_constants.txt`.
The ready-owned selector is in `common/scripted_effects/006_independence_wave_ready_formable_contracts_effects.txt:77-133`.
It rejects absent inputs, cross-package enum choices and nonmatching ATJ/IW-150 or IAX/IW-161 identities before mutation.
Its carrier branch changes only specific restoration receipts, retaining the generic replaced-institution receipt and the active charter.
Its member branch does the equivalent for the existing compact.
The carrier/member branches do not add a plain governance spirit or grant ledger/resource rewards.
The plain branch removes only that actor package's alternative plain governance ideas, then adds the exact selected institution.

The ownership predicates are `has_independence_wave_ready_formable_owned_carrier_institution` and `...owned_member_institution`, in ready contract triggers 252-296.
They require the installed marker, present stored generation/family, current actor generation, exact package/original tag, generic replacement receipt, matching family and a matching charter/compact idea at base, stage 1 or stage 2.
The selector is actor-owned and does not depend on a carrier being ROOT during a member's later signature completion.
Member installation still uses an explicitly supplied carrier ROOT for its family guard; the subsequent signature callback uses the member as ROOT.

The IAX carrier installer recognizes all four plain sources at ready effects 418-453.
The member installer recognizes them at 544-579.
The legacy three branches exclude service administration, and the service branch excludes the other three sources.
Each branch also retains its installed-marker and existing charter/compact guards.
Service installation sets the generic IW-161 replacement receipt plus the distinct role-specific `replaced_iw161_river_service_administration` receipt.
The live-framework restoration blocks at 616-619 and 665-668 recognize that exact receipt, exclude competing specific receipts, and restore only its recorded source.
Receipt cleanup includes the new service marker at 639 and 688.
No source placeholder or substitute institution is introduced for absent or ambiguous input.

The six institution bodies comprise five signature governance completions plus the separate paid service completion.
The latter remains outside the new selector.
The service preparation predicate still requires the current plain `independence_wave_iax_river_office_terms`, and both start and expiry use that predicate.
A receipt saying the river office is represented inside a charter does not satisfy this plain-idea condition.
The new ordering repair therefore does not open or stack the paid service institution under a charter/compact.

The five completion tooltips were read in signature English localisation at lines 83, 86, 89, 126 and 129.
They describe recording the selected terms under the existing compact/charter.
The river-office tooltip distinguishes that case from an independent office's paid service follow-through.
No new route or AI coefficient change was reviewed or proposed.

### Original 36 cases and eight IAX extension cases

The original 36-case suite was rerun from the current parsed installers/restorers.
It retains ATJ's four and IAX's original three choices, both actor roles, live versus ended framework restoration, repeated installation, and absent/ambiguous-source rejection.
All 36 passed.
The service idea was kept separate as an eight-case extension rather than silently changing the meaning of the prior audit count.

| Extension case | Result |
| --- | --- |
| `IAX_SERVICE_CARRIER_LIVE` | One charter replaces service administration; repeated installation is inert; live cleanup restores service administration and clears its receipt. |
| `IAX_SERVICE_CARRIER_ENDED` | Charter removed; ended framework restores no source institution; service receipt cleared. |
| `IAX_SERVICE_CARRIER_AMBIGUOUS_SOURCE` | Service plus river-office terms installs no charter and changes no receipts. |
| `IAX_SERVICE_CARRIER_CONFLICTING_RECEIPTS` | Service and river-office restoration receipts together restore neither plain choice; receipts are cleared. |
| `IAX_SERVICE_MEMBER_LIVE` | One compact replaces service administration; repeated installation is inert; live cleanup restores service administration and clears its receipt. |
| `IAX_SERVICE_MEMBER_ENDED` | Compact removed; ended framework restores no source institution; service receipt cleared. |
| `IAX_SERVICE_MEMBER_AMBIGUOUS_SOURCE` | Service plus river-office terms installs no compact and changes no receipts. |
| `IAX_SERVICE_MEMBER_CONFLICTING_RECEIPTS` | Service and river-office restoration receipts together restore neither plain choice; receipts are cleared. |

All eight passed.
Each replacement/restoration case also retained an unrelated school/port/PUSA sentinel idea.
Source review confirmed the corresponding exclusions in every one of the four IAX source branches, not just the tested ambiguous pair.

### Ordering and rejection cases

Thirty-five additional actual-source ordering cases passed: each of the five completion helpers in plain mode, carrier mode at base/stage 1/stage 2, and member mode at base/stage 1/stage 2.
Owned mode retained exactly the existing charter/compact and wrote exactly one specific restoration receipt.
Subsequent live restoration returned the chosen signature institution.
Plain mode ended with exactly the selected plain institution.
Repeated completion left the idea and receipt state unchanged.
Normal actor variables and CP/manpower were unchanged by every governance completion.
Conservative helper-frame return cleanup left no newly created enum scalar outside its caller.

Within the IAX river-office ordering cases, the genuine school trust and the completed paid transport/watch preparations were supplied.
Service preparation was available in plain mode and false in every owned charter/compact mode.
This directly covers the accepted no-stacking refinement.

Four selector rejection cases passed: ATJ supplied an IAX choice, IAX supplied an ATJ choice, and each package omitted the temporary choice input.
Ideas and receipts remained unchanged.
These are this reviewer's independent source cases, not a claim that the parent's private regression script was run or that its cases have identical fixtures.

### Evidence limits and current source identities

The in-memory model executes the actual ordered source bodies for flags, normal variables, idea replacement/restoration, enum selection and nested temporary call-frame lifetime.
ROOT is explicit for installation and signature completion.
Module/framework/force eligibility and the presence of live actor state are declared fixtures.
The model's variable-existence predicate recognizes supplied normal and temporary storage.
The installed `has_variable` documentation at triggers_documentation.md:5006-5013 describes variable existence without independently proving every engine temporary-storage behavior.
The earlier offline Data structures:435-443 lifetime citation remains the source basis for caller initialization.
No engine idea-slot, database, flag, country-generation, native callback or cleanup execution is claimed.
No new broad MCP request was made under the parent's explicit bounded-review instruction.
The parent owns its regression implementation and all remaining native evidence.

| Reviewed file | SHA-256 |
| --- | --- |
| `common/scripted_effects/006_independence_wave_ready_formable_contracts_effects.txt` | `b6e0bfb658a27d707ae9c7d250fcbd76af647241411b575ad0db1731c9feed7f` |
| `common/scripted_triggers/006_independence_wave_ready_formable_contracts_triggers.txt` | `c7ca400459457e245e92e3d9610d6761ed150f81ba77df60c52e5ed38594b2a0` |
| `common/script_constants/006_ready_formable_contracts_constants.txt` | `b3ddf841051604a67fc435b131c4b16b7581b1b51c354b8194fb922370ca755f` |
| `common/scripted_effects/006_independence_wave_signature_modules_effects.txt` | `502c72e82bb98a45bac281cbc6e28bb8e57f852f80bc19c713b48f11d9c131a0` |
| `common/scripted_triggers/006_independence_wave_signature_modules_triggers.txt` | `7b9f30995ce5dedaf4d3e5e6219f9c02df7082296e4ee316a20e94ca921c4112` |
| `localisation/english/006_independence_wave_signature_modules_l_english.yml` | `461cbc9f9a3a62f8ea45548692732d35d9827396d9bae997b4f963b42a5f3ddf` |

For the related source commit, retain all six reviewed files together: the new ready-owned effect, both ownership predicates, enum constants, five completion callers, unchanged service gate and their current tooltip/idea localisation.
This dependency note does not authorize staging unrelated shared hunks or claim any index state.
No implementation simplification, gameplay edit or fallback was made by this review.
Skills reused: events, decisions-missions and subagents.
No skill was changed.
