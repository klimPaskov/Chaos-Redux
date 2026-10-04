# Event 012 recovery localisation and ordinary decision audit

Disposition: unresolved parent wording fixes and partial MCP/native presentation evidence.
This is a read-only source audit of the parent?s current working tree, with the sole authorized write being this handoff.
No gameplay, localisation, spreadsheet, export, or skill source was changed, no Git command ran, and Hearts of Iron IV was not launched.
The user?s assignment treats the original recovery design as accepted and requires full Gods implementation without simplifications.
This report does not independently accept new design or certify the full Gods goal complete.

## Scope and source result

Reviewed all six recovery decision rows, recovery effects/triggers/constants, epoch-binding effects/triggers, the recovery English file and four display getters, the private host-description getter and pending member priority, existing category visibility, moved ordinary description leaves, and the two milestone 12209 English keys and their selector bindings.
Read AGENTS.md and the events, decisions-missions, and subagents skills, including the event writing rules and the linked scripted-GUI content/action budget only.
Read the original-host recovery design and helper handoff as context, distinguishing their earlier proposals and evidence limits from current source.
Gameplay and probability acceptance remain with the separately assigned auditors.
No focus tree, map, technology, new GUI, art, meter, or country surface was audited or added.
Shared world-log layout remains outside this bounded audit, its two recovery leaves and source selectors are inside scope.

All six decision IDs have matching English title and description leaves:

| Decision ID | Decision source line | English title/description lines |
| --- | --- | --- |
| gods_of_africa_restore_original_mandate | 7 | 2?3 |
| gods_of_africa_invite_original_mandate_member | 28 | 4?5 |
| gods_of_africa_finish_original_mandate | 62 | 6?7 |
| gods_of_africa_resume_original_mandate | 80 | 8?9 |
| gods_of_africa_approve_original_mandate | 100 | 10?11 |
| gods_of_africa_decline_original_mandate | 130 | 12?13 |

Decision source: `common/decisions/012_africa_gods_recovery_decisions.txt`.
English lines throughout this report refer to `localisation/english/012_africa_gods_recovery_l_english.yml` unless specified otherwise.

## Findings and exact parent replacements

### F1: grammatical/style repair, English line 20

`gods_of_africa_recovery_start_effect_tt` starts its final sentence with lowercase `authority`.
Its first two sentences also repeat the action and invitation function already visible in the row and description.
Replace the complete value with:

`Reconvene the congress and invite current members to support renewed tribute authority. Tribute remains suspended until ratification and consolidation are complete.`

This repairs the sentence start, removes redundant wording, and keeps the distinction between congress and activated authority.

### F2: incomplete eligible-member requirement, English line 15

`gods_of_africa_recovery_start_requirement_tt` says the minimum must be current Charter members, but `gods_of_africa_recovery_member_is_eligible` accepts chartered, autonomous-federal, and integrated-region relationships at recovery-trigger lines 81?103.
The same tooltip calls the first proof completed, while its source capability permits either succeeded or recovered proof at `common/scripted_triggers/012_africa_triggers.txt:754?759`.
The sentence is overloaded and uses implementation-flavoured `committed continental host`.
Replace with:

`Africa's surviving original government leads the continental union, is not capitulated, owns and controls its capital, and has satisfied its first proof. Its tribute mandate remains unsettled, and at least [Root.GetGodsOfAfricaRecoveryMinimumApprovals] current Charter, autonomous-federal, or integrated members are eligible to support its renewal.`

Do not substitute a crown-legitimacy requirement, include a successor, or imply that an annexed original government can qualify after release.
The exact exclusion predicates belong to current source, not a list of private receipts in the tooltip.

### F3: ratification blocked text omits physical and first-proof gates, English line 17

`gods_of_africa_recovery_finish_requirement_tt` explains capital and quorum but omits the explicit noncapitulation and first-proof conditions used by `gods_of_africa_recovery_can_finish` through `gods_of_africa_authority_owner_has_physical_return` at trigger lines 28?35 and 259?264.
A visible congress row can therefore be blocked for a world-state requirement its tooltip does not explain.
Replace with:

`The surviving original government is not capitulated, owns and controls its capital, and has satisfied its first proof. At least [Root.GetGodsOfAfricaRecoveryMinimumApprovals] eligible members must approve, with more than half of all current eligible members in favour. Current approvals: [Root.GetGodsOfAfricaRecoveryApprovedCount] of [Root.GetGodsOfAfricaRecoveryEligibleCount].`

The strict majority remains more than half, not half, and the minimum remains dynamic.
Optional small prose repair for `gods_of_africa_finish_original_mandate_desc` at line 7:

`Ratification requires support from more than half of all current eligible members and at least [Root.GetGodsOfAfricaRecoveryMinimumApprovals] approvals. Current approvals: [Root.GetGodsOfAfricaRecoveryApprovedCount] of [Root.GetGodsOfAfricaRecoveryEligibleCount]. Ratification begins [Root.GetGodsOfAfricaRecoveryConsolidationDays] days of consolidation.`

This removes the noun stack `support renewed authority through a strict majority` without changing policy.

### F4: member blocked tooltip omits negotiation, English line 19

`gods_of_africa_recovery_member_requirement_tt` mentions tribute response and reconciliation but does not explicitly identify the negotiation gate.
`gods_of_africa_recovery_member_request_is_current` at trigger lines 182?196 excludes demand-active, negotiation-open, and reconciliation-pending separately.
Replace with:

`Our invitation concerns the surviving original government's current mandate. We remain an eligible cooperative member at peace with Africa and have no tribute response, negotiation, or reconciliation to resolve.`

This retains current identity and world-state meaning without exposing generation, epoch, or request-field names.

### F5: log title ambiguously suggests activation, English line 34

`africa.event_log.gods.original_host_recovery.title` reads `Africa's continental mandate restored`.
Milestone 12209 is recorded during ratification, before consolidation and final activation, in `common/scripted_effects/012_africa_gods_recovery_effects.txt:287?350`.
The detail correctly says tribute authority awaits consolidation and continued consent, but the title should state the same stage explicitly.
Replace title with:

`Africa's restored mandate ratified`

Retain the current detail at line 35 verbatim:

`Current continental members have renewed the surviving African unifier's mandate. Tribute authority awaits consolidation and continued consent. Countries exempt after defeating Africa retain their exemption until they request and receive separate recognition.`

The title and detail selectors are `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:10604?10609` and `:6758?6763`.
The constant is `common/script_constants/012_africa_event_log_constants.txt:70`, `gods_original_host_recovery = 12209`.
No log layout or history-ledger redesign is recommended.

### F6: generic resume description contains avoidable abstraction, English line 9

`gods_of_africa_resume_original_mandate_desc` says `retain the authority appropriate to its present compact`, which gives little concrete information.
Its current scope correctly covers due activation, owner, and registry obligations at trigger lines 278?321 and effect lines 410 onward.
Do not narrow the row back to consolidation or claim it ratifies a mandate, resets a completion date, or activates tribute immediately.
Recommended replacement:

`Resume the current compact's due obligations once Africa is not capitulated, owns and controls its capital, and has satisfied its first proof. A restored mandate must retain enough current member support for consolidation to conclude.`

Keep `gods_of_africa_recovery_resume_requirement_tt` at line 18 unchanged: `The current mandate is valid and a continental obligation is due.`
Keep `gods_of_africa_recovery_resume_effect_tt` at line 23 unchanged: `Resume the current compact's due obligations. Its authority and existing completion dates remain in force.`
These are intentionally generic world-state descriptions and do not expose scheduler flags, raw day IDs, or private event IDs.
Title capitalisation at line 8 can remain as supplied, it is not a gameplay defect.

## Coverage, scripted localisation, and dynamic text

Missing-key list: none found for the six titles, six descriptions, their five requirement keys and six effect keys, three recovery category leaves, four numeric display leaves, four getter names, two log leaves, or moved ordinary host/member description leaves.
Duplicate-key list: none found for the recovery English keys when checked against all current top-level English localisation files.
Wrong-namespace list: none found in this bounded set.
The target invitation title/description/tooltips use `[From.GetName]`, corresponding to member FROM and chooser host ROOT in the native targeted row.
Member response/category text uses `[africa_host.GetName]`, with no `event_target:` prefix inside localisation.
The member request validator checks that the stored actual object exists and equals the authoritative global host before this branch is displayed.
No scalar epoch or loss sequence is treated as a display scope.

Scripted-localisation issue list: no broken in-scope getter reference or missing output leaf found.
The four recovery getters at `common/scripted_localisation/012_africa_gods_recovery_scripted_localisation.txt:4?46` initialize unscoped temporary counts or tuning-derived display values and output matching numeric leaves.
`[Root.GetGodsOfAfricaRecoveryApprovedCount]` scopes the getter to the current host object, it does not scope a temporary variable to ROOT.
The output leaves at English lines 26?29 read plain temporary names and do not use `Root.some_temp`.
No macro token, currency, internal epoch, clock selector, raw day ID, or formatting character was added to scripted-localisation source.
Current source does not require a new meta-effect tooltip mechanism for these getters.

`GetGodsOfAfricaHostCategoryDesc` at base scripted-localisation lines 622?628 chooses reopen recovery, then committed pending consolidation, then the ordinary active leaf.
Base English `gods_of_africa_host_category_desc` at line 111 invokes it, and `gods_of_africa_host_category_desc_ordinary` at line 474 retains the prior Strength/doctrine text.
`GetGodsOfAfricaVictorCategoryDesc` at lines 602?607 places pending recovery member text ahead of victor and ordinary Strength/Wrath leaves.
Base English participant wrapper is line 109, with ordinary/victor leaves at lines 457?458.
The recovery branches contain neither Strength/Wrath nor historical strength reads, so the pending branch does not inherit undefined preactivation values from those ordinary leaves.
This is source selection evidence, not a visual or native-evaluation claim.

Dynamic opportunities: the approval numerator, eligible denominator, minimum approvals, target name, current host name, and consolidation duration are already dynamic.
The consolidation leaf at line 32 reports the total duration, currently 180 from `common/script_constants/012_africa_gods_constants.txt:15`, and does not claim it is days remaining.
An elapsed/remaining display could improve progress clarity if the parent wants it, but would need its own initialized, scope-correct getter and due-date validation.
It is not a required new meter, currency, or accepted mechanic in this audit.
Do not replace existing current counts with frozen ratification history.

## Ordinary decision source consistency and assets

All six rows declare `cost = 0`, at decision lines 19, 53, 71, 89, 112, and 142.
Their complete effects contain no resource debit and do not describe a fee or reparations payment.
No custom spendable-cost row is needed for these actions, and no hidden internal currency should be exposed.
Visible availability bodies wrap their actual recovery predicates in `custom_trigger_tooltip`, and effects show custom leaves with implementation under `hidden_effect`.
No visible raw flag-name requirement was found in these six rows.

Source category visibility covers active host, reopen recovery, and current committed pending consolidation at category lines 30?43.
Participant visibility admits a current recovery request at lines 14?27.
Recovery rows are phase-gated: start disappears when congress opens, invite/finish occupy congress, invite and due resume occupy consolidation, and approve/decline expose only the opposite response after an answer.
There are at most two simultaneously visible member response types in this family and at most two recovery host action types per phase.
Native targeted invitation rows may repeat for eligible members, so source phase gating alone does not prove a compact visual list.
Active-phase resume also adds a row alongside existing host actions, the total existing Gods action budget remains the decision/gameplay auditor's integration responsibility.
No dedicated GUI or UI worker is required by this six-row ordinary-category design.

All new decision IDs and description leaves match exactly.
Existing source sprites are `GFX_decision_012_africa_gods_public_pardon` and `GFX_decision_012_africa_gods_escalate_offense` at `interface/012_africa.gfx:69?70`.
Category icon is `GFX_decision_category_012_africa_charter_ledger` at `interface/visual_consistency_repair.gfx:18`, and existing picture is `GFX_decision_cat_picture_012_africa_gods` at `interface/012_africa_event_pictures.gfx:20`.
Their texture files exist in the working tree, this is source wiring evidence only.
No actual icon appearance, native title fit, tooltip wrapping, alignment, clipping, or overflow is certified.

Restoration source binds the same original committed host and loss identity, excludes an actually annexed original owner, and rejects consumed succession through the current recovery predicates.
Physical return requires noncapitulation, ownership/control of capital, and existing first-proof capability.
Fresh quorum requires at least two approvals and strictly more than half of the current eligible pool, with consent rechecked for restored consolidation.
The commit does not change doctrine or clear victor exemption, and the preservation helper protects existing final outcome/report receipts.
No new text should describe frozen predefeat Strength as current authority or erase opt-out/history memory.
The existing bilateral victor wording at base English lines 430?450 correctly describes an offer followed by explicit acceptance and says no reparations.
Global ratification remains separate from that personal agreement and from ordinary costly defiance reconciliation.
The entire cancellation/opt-out closure and native victory ledger are not re-audited here, those are gameplay-auditor responsibilities.

## Prose-quality assessment

Vagueness: F6 identifies abstract authority wording and replaces it with concrete physical requirements.
Bloat: F2 splits an overloaded requirement sentence and F3 offers a simpler strict-majority description.
Obvious explanation: F1 merges action-title repetition with the meaningful suspension consequence.
Repetition: F1 removes repeated reconvene/invite explanations, remaining approval and consent repeats serve separate description/requirement/effect consumers and are not automatically deleted.
Overcomplication: F2/F3 replace an implementation-flavoured host label and the ratification noun stack without dropping membership types, quorum, or first proof.
Style-rule repair: F1 fixes the sentence start, F5 resolves stage ambiguity, no em dash or semicolon was found in the assigned recovery English values.
No implementation-history, tuning-history, scheduler-flag, macro-token, or internal-currency prose was found in the assigned recovery values.
No broad base-Gods tone rewrite is proposed.
Sourced quotations: no quotation-bearing surface was found in the assigned recovery passages or moved ordinary category leaves.
No actual sourced quotation was edited or repunctuated.
All replacement strings preserve the existing dynamic tokens and gameplay requirements, except deliberately retaining the correct generic resume requirement/effect unchanged.

## Reference and MCP evidence, limits

Live `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup`, and `decision_inspect` were exposed and called.
The localisation context returned both installed and offline references, with no omitted required source kind.
Offline wiki `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, was read through MCP at lines 531?555 for namespaces and 656?705 for scripted localisation, first-match priority, and temporary output lifetime.
Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\loc_objects_documentation.md`, physical SHA-256 `a5d06da0b42e615fa0c40d0103d9125ed68a7691778e20c0315aca7c82822c81`, was read locally at lines 541?586 for THIS/Root/Prev/From.
Vanilla `common/decisions/ETH.txt` was read locally at lines 651?667 for an available-body custom-trigger-tooltip precedent, physical SHA-256 `a50f6aa755cf6dd619957e8ef73c196fe8a422b261a2805789426f43a373504f`.
An attempted exact source lookup for `ETH_rebuild_the_roads` returned zero definitions and is not claimed as precedent evidence.
No web Paradox page was accessed.

The first narrow `decision_inspect(id=gods_of_africa_resume_original_mandate, mode=inspect)` was rejected because declared scenarios were required.
A single corrected request used `localisation_unbound_resume`, actor ETH, closed flags, and an empty declared state, deliberately not claiming a fulfilled recovery fixture.
It completed without a transport timeout as `DECISION_ANALYZED_PARTIAL`, `complete=false`, one scenario, 218 unresolved definitions, failed decision-coverage validation, revision `3e3991edf998a8dc8b9cbc362b7a58225e6efc51c8e52e662a5bfe07694d7abc`.
Although the query named one decision, the service summary counted 1,972 categories and 7,949 decisions, so its result is not presented as six-row completed coverage.
Detailed linked artifact was not available through a listed MCP resource, `list_mcp_resources(server=hoi4_agent_tools)` returned an empty resource list.
Retain this useful artifact URI for parent retrieval, without inventing its detailed scenario contents:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24c63a00227be7804f8470a36a986f95f232277186656c570efc6702686af06f/8de4ae43e0494e64a082278a09292c224d25188d182f98e65ef448a4708bd185/decision-46b8854dcab80bbd150420df.json`

No native ordinary-decision visual-render route was exposed in the connected tool inventory.
No GUI window was in scope, so no unrelated GUI render or event graph scan was substituted.
Overflow and one-to-one in-game text display remain unverified, source validation is not equivalent visual evidence.
The separately assigned gameplay/probability auditors retain their event/lifecycle and weighted-scenario workflows, this worker did not duplicate expensive graph scans.
No callable HOI4 service-health/version route was found, successful reference responses establish only those routes' responsiveness.
The Blender service health tool is a different service and was not treated as HOI4 health.
No job, helper-expansion, or negotiated task route was used.
Standalone Technology Tree Viewer was separately searched in the connected tool inventory and not exposed, record that as a package gap, distinct from the exposed technology inspect/render/compare routes.
Technology is outside this task and no technology-health or viewer-use claim is made.

## Cross-surface handoff and completion

Spreadsheet/catalog text was not inspected or edited, so no workbook mismatch is asserted.
Pass F5's final title and the retained detail above to `chaosx_spreadsheet_doc_worker` if the catalog mirrors milestone 12209.
Pass all F1?F6 final key values to that worker only for catalog fields that actually mirror these decision/tooltips.
Parent owns applying the proposed localisation fixes, keeping UTF-8 BOM, reviewing final wording and current hashes, and any catalog reconciliation.

File encoding concerns: none found in either inspected English file, both decode as UTF-8 with BOM.
No encoding requirement was incorrectly imposed on script TXT files.
Changed files: only this handoff.
Changed localisation keys: none.
Dynamic localisation added/fixed: none, current four getters were audited and retained.
Behavior/display before and after: no source behavior or display changed by this worker, F1?F6 describe proposed wording only.
No new design-depth gap or mechanic-expansion plan was written.
Unresolved wording decisions: parent acceptance/application of F1?F6 and optional elapsed/remaining progress display.
Skipped meaningful validation: fulfilled native recovery/blocked scenarios, native decision fit and overflow, shared world-log visual layout, full opt-out/history closure, balance, and workbook comparison, because they are unavailable through the exposed visual route or outside this bounded owner assignment.
No gameplay simplification was recommended or used.
The bounded source audit is delivered, the full Gods implementation and presentation acceptance remain incomplete while the listed wording and evidence limits remain unresolved.
Skills used: chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents, and the decisions skill's linked scripted-GUI action-budget guidance.
No skill was created or updated.

## Physical source receipts

These SHA-256 values identify the inspected concurrent parent tree, not a frozen Git revision.
Rehash before applying or reviewing fixes if the parent has continued editing.

| File | SHA-256 |
| --- | --- |
| `common/decisions/012_africa_gods_recovery_decisions.txt` | `cb6c0965f03b25e2d3e7a4d653edee380c1fe70c0e1791766914643124e6cfd1` |
| `localisation/english/012_africa_gods_recovery_l_english.yml` | `15d9907e49a9d5a34ee988bee0198c4fe2e236a3d8c133cdfaa080ce96072df6` |
| `common/scripted_localisation/012_africa_gods_recovery_scripted_localisation.txt` | `5a6539506a819b23e0c9a72bad621781c3bc740c9c3df9245630701f387e20c7` |
| `common/scripted_localisation/012_africa_gods_scripted_localisation.txt` | `9cb1fc4d1f5dcdfba29358b8dd363c6cf9f78286de5fa50cf0478460afcec527` |
| `localisation/english/012_africa_gods_l_english.yml` | `a68d86bd4cac6438e5c2b61053127d2017e613bc5df55563958c79cc48e6d45a` |
| `common/decisions/categories/012_africa_gods_categories.txt` | `88272d874647ceff2596ca8c840226e6ac91e41a012dc800214a28c32aa9f581` |
| `common/scripted_triggers/012_africa_gods_recovery_triggers.txt` | `3664ab41fa1bfc62eca631c5e1618cfa94e3e3dda7568d0c749c816e5e34369c` |
| `common/scripted_triggers/012_africa_gods_epoch_binding_triggers.txt` | `5afb48b7e53e2d1aa2f47fde96742add41f85c7203c94842093bdf674effb67e` |
| `common/scripted_effects/012_africa_gods_recovery_effects.txt` | `55932cb10e1a6cb021caa4b8c4d4b385755c0af18677624403b4ca1f0a29ed12` |
| `common/scripted_effects/012_africa_gods_epoch_binding_effects.txt` | `cf93227cd8c9eb725b31757152984c190c2da49259e8eb12080f142c1a90cb1f` |
| `common/script_constants/012_africa_gods_recovery_constants.txt` | `4fb023940ce5cb8695f849a01c9f65696e2b5f7b48ad5aa129877fa797a424cf` |

## Parent application

The parent applies all six required wording corrections to the owned English recovery file, retaining the generic resume requirement/effect and the milestone detail.
The eligible relationship label uses `autonomous federal` without an invented compound adjective.
The log title identifies ratification before consolidation, and no gameplay predicate, price, phase, icon, or getter changes in this wording pass.
Current dynamic tokens remain unchanged; the original source hashes above retain the pre-application audit frame.
