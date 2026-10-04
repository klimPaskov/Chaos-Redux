# Event 23 assembly registry lifecycle audit retry

Disposition: the bounded source audit is complete, but the required probability and decision scenario MCP evidence is incomplete. Do not treat this as engine, save and reload, or live campaign acceptance.

Audit date: 2026-10-03.

Repository: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.

## Scope and acceptance basis

The user authorized a read-only audit and one written handoff at this path. No gameplay, localisation, asset, workbook, or Git files were changed. No commit or staging operation was performed.

The accepted assembly rule is recorded in docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_6_soviet_collapse_integration.md:24-35. The existing Assemble Device Batch action selects one registered storage depot owned and controlled by SOV, with infrastructure above zero and at least one actual civilian or military factory. Missing, dismantled, technically denied, or Event 5 snapshot-pending sites are invalid.

The existing atomic technology and reactor requirements, costs, production amount, mission duration, and AI weights remain in force. Site loss cancels the existing mission without rerouting, granting a batch, or transferring technical or command access. No new action, mission, GUI, facility, technology, unit, delivery platform, or cost type is within scope.

The Part 10 Soviet Collapse acceptance case requires the snapshot before transfer and conservation after transfer at docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_spec_part_10_achievements_acceptance_and_closure.md:380-397. The bounded decision prompt sets the limits of six primary actions, three active missions, and four spendable cost types at docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_decision_mission_prompt.md:40-62 and docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_coding_prompt.md:85-87.

The user separately directed that transit and dismantlement ROOT/PREV closure repairs remain parent-owned. This audit did not duplicate that work.

## Findings sorted by severity

### P1

No source-confirmed P1 assembly failure was found in the inspected decision, trigger, effect, callback, or localisation path.

### P2

1. Assembly receipt closure drops the country pointer even when the state mirror does not match. In common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:1681-1697, the state mirror is closed only when its active flag and batch nonce match the SOV nonce. The country-side closed nonce is then written and the state pointer, ID, nonce, and global display target are cleared outside that match branch. If the state mirror is absent or carries a different nonce, its active flag and state nonce can remain orphaned while SOV records the nonce as closed and loses its cleanup pointer. The normal completion and cancellation path has matching registration fields, so this is a mismatch or corrupted receipt risk rather than a normal-path failure. Recommended local fix: preserve or explicitly dispute the country receipt unless the exact state pointer, stored state ID, and active nonce close together; do not silently clear the only pointer to an unmatched active state mirror.

2. The six-action budget is met by unique phase-gated decision definitions, but the actual visible row count is unresolved. The six definitions found in common/decisions/023_sov_nuclear_bombs_decisions.txt are sov_nuclear_bombs_operational_command at line 74, sov_nuclear_bombs_expand_fissile_production at line 274, sov_nuclear_bombs_assemble_device_batch at line 292, sov_nuclear_bombs_prepare_delivery_crews at line 317, sov_nuclear_bombs_conduct_command_exercise at line 331, and sov_nuclear_bombs_install_stronger_authentication at line 345. Both operational command and assembly use state targeting, so each eligible state may produce a separate decision entry. The opening helper registers the capital and up to two random owned controlled storage states in common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:129-151. Actual qualifying targets, concurrent target clones, and the full phase row count were not returned by MCP. Do not treat six decision IDs as proof of six or fewer visible decision rows.

3. The mandatory AI probability audit is unresolved. The first chaosx_ai_probability_auditor reported that its probability tools were unavailable to that child model, so it returned source traces only and no scores. A parent-side probability_inspect request without an explicit workspace then timed out after 600 seconds. A fresh auditor verified that inspect, evaluate, sweep, compare, and render schemas were exposed, then launched decision and mission probability_inspect calls with the confirmed workspace ID and explicit source path. Both calls remained unanswered for about five and a half minutes before the auditor terminated its orchestration call, without a service error or result. Evaluation, sweep, and rendering were not run. No source change was made, so probability_compare is not applicable and no balance target was changed.

4. The visible cost count is three, but the actual debit helper is outside the user-authorized file list. The decision and English cost localisation show political power, support equipment, and manpower. The exact definitions of sov_nuclear_bombs_can_pay_security_cost and sov_nuclear_bombs_pay_security_cost do not appear in any of the named source files, so display-to-debit parity cannot be asserted from this audit.

### P3

5. The four-row category header identifies operational devices, Readiness, Integrity, and Status in localisation/english/023_soviet_nukes_l_english.yml:95-96. The Status row combines posture and public knowledge as an unlabeled pair. The underlying terms are localised, but the header does not tell the player which of the two values is posture and which is knowledge. Keep the four-item limit and label both values in the existing row.

6. The assembly decision and mission call the result a batch without showing its expected quantity. The quantity is computed from existing production constants and reactor count in common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:2163-2172. The decision and mission text at localisation/english/023_soviet_nukes_l_english.yml:226-227 and 341-342 do not state that quantity. The cancellation text also explains that work stops at the selected site but does not state that the upfront security costs remain spent. Consider a concise dynamic amount and sunk-cost clarification inside the current decision or mission localisation if the parent accepts those text changes.

## Assembly lifecycle and receipt trace

The decision is SOV-only through sov_nuclear_bombs_event_actor_is_valid. It is visible in production phase when production capacity exists, no other project is active, and the assembly cooldown is absent. Its target is any SOV-owned state and the target trigger requires sov_nuclear_bombs_event_state_is_valid_assembly_site. Availability rechecks production capacity, atomic_research, nukes, no active project, site validity, and security cost affordability. The complete effect repeats the relevant gates, saves the selected state as sov_nuclear_bombs_assembly_selection, starts production, and pays only after the production mission active flag is present. Evidence: decisions file lines 292-312 and triggers file lines 650-672.

The base storage predicate requires a registered site, SOV control, no missing or dismantled state, no pending Event 5 snapshot, no technical denial, and infrastructure above zero. The assembly predicate adds SOV ownership and at least one arms factory or industrial complex. The active receipt trigger checks the persistent state pointer, state ID, active state flag, state nonce, and an existing SOV owner pointer.

The start effect increments the ledger transaction sequence, stores the exact state pointer and ID on SOV, saves the SOV owner and nonce on the state, sets the active batch marker, records SOV institutional access, and creates the global display target. Evidence: common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:1650-1674.

The existing mission is sov_nuclear_bombs_device_assembly_mission. It is visible and activated only while the production mission flag is set, is non-selectable, has impossible availability, and uses the existing production duration constant. Its cancel trigger checks invalid SOV actor, invalid exact site, or lost production capacity. Its timeout and completion both call sov_nuclear_bombs_complete_production_mission, while its cancel effect calls sov_nuclear_bombs_cancel_production_mission. Evidence: decisions file lines 1199-1215 and the Vanilla decision modding page lines 469-478.

The success helper clears the active mission flag before its success gate, then requires the registered actor, valid exact site and nonce, production capacity, both technologies, and a positive pending amount before registering devices. The registration effect adds the native stockpile and matching ledger buckets, marks sov_nuclear_bombs_production_transaction_recorded, clears the pending amount, and refreshes reconciliation. The outer completion helper then applies the existing success state and closes the receipt. Evidence: event effects lines 1918-1953 and runtime effects lines 269-292.

The cancellation helper clears the active flag and pending amount, closes the receipt, records cancellation, returns the phase, and applies the configured rejection Integrity adjustment. It does not grant a batch or issue a cost refund. A successful run sets the existing assembly cooldown. The exact in-scope grant call is from the completion helper. The transaction-recorded flag is set but does not itself appear in the grant helper's guard. The normal replay path is protected by the cleared mission flag, cleared amount, and closed active receipt. A direct re-entry that recreated a positive amount under an active receipt would require further indexed caller review, which the timed-out source lookup did not provide.

On state control change, the Event 23 callback first tries the pending Event 5 reconciler, then invokes the exact-state control reconciliation for registered or assembly states. The assembly registry helper marks a lost site contested and cancels the SOV assembly mission only when the active site ID matches that exact state. Evidence: common/on_actions/023_sov_nuclear_bombs_on_actions.txt:39-55 and common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:2096-2104.

On SOV annexation, the actor cleanup closes the assembly receipt before clearing the production mission flag and other SOV-only project state. This path creates no production batch. Evidence: common/on_actions/023_sov_nuclear_bombs_on_actions.txt:71-86 and common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:3033-3090.

## Event 5 before and after snapshot order

The Event 23 helper order is internally consistent in the named runtime file. sov_nuclear_bombs_begin_event5_state_transfer finishes an older pending receipt, increments the snapshot generation, and snapshots the exact state before transfer. The snapshot records the state owner and controller, relevant site buckets, Event 23 context, and bounded registry fields before setting the pending and transfer-in-progress markers. Evidence: common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:2171-2184 and 2662-2721.

The assembly registry pre-snapshot records the facility role, active batch flag, owner pointer, active state nonce, SOV state pointer, SOV state ID, and SOV nonce. The post-snapshot records the same active fields plus the closed nonce and contested state. Evidence: runtime effects lines 2516-2585 and 2587-2620.

The state-control callback cannot reconcile through an in-progress Event 5 transfer. The explicit finish helper clears that marker, runs the exact-state reconciliation, invokes registry reconciliation, and captures the post-transfer context and registry values after site loss can cancel the assembly mission. Evidence: runtime effects lines 2726-2731 and 2777-2928.

The Part 6 specification requires the snapshot before ownership changes at lines 37-52, and the Part 10 acceptance case requires pre-transfer snapshot and conservation at lines 380-397. The runtime documentation claims 82 direct transfers in 34 Event 5 successor helpers and six release tranche helpers at common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md:109-113. The Event 5 transfer source files were outside the exact gameplay source list for this audit, so caller coverage across every transfer command was not independently checked. The source-level helper order is not save/reload proof.

## Cognitive load and mission quality

The command category header exposes four rows. Operational device count has a clear label. Readiness and Integrity are named numeric values, but the header itself does not show their threshold consequences or player response. The paired Status row should identify posture and public knowledge separately without adding a fifth row.

The six production-phase decision definitions meet the six-ID ceiling. The exact native row count remains unresolved because the two state-targeted actions can produce target-specific entries and no scenario inspection result was returned. The assembly flow itself has one active mission and the project gate prevents another project action while it is active. This does not certify the total Event 23 mission count outside the assembly lifecycle.

| Owner | Category | Region | Requirement | Duration | Success | Failure or cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SOV | sov_nuclear_bombs_command_category | One selected registered industrial storage depot, named dynamically in the mission text | Existing reactor capacity, atomic_research and nukes, valid SOV ownership and control, usable infrastructure, one actual factory, no active project, and an active exact site receipt | Existing constant sov_nuclear_bombs_duration.production_mission, unchanged and not numerically audited because the constants file is outside the named source list | Register the pending production amount once, then close the active receipt | Timeout revalidates the same site and capacity; loss rejects without a batch or reroute. Cancellation clears the amount and receipt and records cancellation | One mission ID and one active SOV project flag. Normal replay is guarded by flag and amount clearing. A stale nonce mismatch can leave a state-side active marker |

The dynamic state name is present in sov_nuclear_bombs_device_assembly_mission_desc at localisation/english/023_soviet_nukes_l_english.yml:341-342. The requirements tooltip and decision text explain the exact depot and no-reroute behavior at lines 182 and 226-227. No wall of text or raw trigger block is exposed in those assembly strings.

## Cost, requirements, AI, localisation, and exploit notes

The displayed security cost uses three distinct spendable types, within the four-type cap: £pol_power, £support_equipment_text_icon, and £manpower_texticon. The blocked string uses the same three icons. The custom cost tooltip is present and there is no literal resource-name fallback. Evidence: localisation lines 165-167. Actual payment helper definitions are outside the exact source allowlist, so the debit count and displayed-value parity remain unresolved.

The assembly requirement text is separate from payment. It names registration, Soviet ownership and control, infrastructure, factory presence, missing and dismantled exclusions, technical restriction, pending Event 5 snapshot, production capacity, and atomic technology gates. No hidden fifth cost is visible in the named decision or localisation files.

The decision score is base 0.80 with a factor of 1.50 only while Readiness is strictly less than 50. The mission score is base 0.80 with no modifier. These are willingness weights, not click probabilities. The assembly decision's visible, target-root, target, availability, cost, and cooldown gates are local and SOV-scoped. Invalid depots are not candidate targets. Lost site or capacity cancels the active mission and does not redirect it.

The specialized auditor named these scenarios, but all results remain unresolved because no probability adapter completed: P23_ASSEMBLY_AI_READINESS_49_VALID_SITE, P23_ASSEMBLY_AI_READINESS_50_VALID_SITE, P23_ASSEMBLY_AI_READINESS_80_VALID_SITE, P23_ASSEMBLY_AI_SITE_LOST, and P23_ASSEMBLY_AI_NO_CAPACITY. The source trace makes the readiness modifier true only at 49. Candidate pool completeness, external AI factors, rankings, dominance, and starvation were not measured. No simulation was run. Probability comparison is inapplicable because this audit made no source change.

No free production or repeatable grant is visible in the normal mission path. The decision pays after mission activation, so a later site loss consumes the existing upfront costs without a refund. The mission copy does not state that the payment remains spent after cancellation. Repeated start and cancel attempts have a real cost and the configured Integrity adjustment, so no free loop was established from the named files.

## MCP and reference evidence

The live parent tool inventory exposed reference_context, reference_search, reference_read, source_lookup, decision_inspect, and the probability routes. The HOI4 artifact resource template was listed for server hoi4_agent_tools, but list_mcp_resources returned no artifacts.

The decision reference context returned status OK and workspace ID mod_chaos_redux_ea3b2d67c2c0. It cited installed Vanilla Country Decisions revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019 at C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md, lines 1-46, and offline Decision modding revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 at paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md. The context bundle omitted Effects, Triggers, Scopes, Localisation, and installed effects documentation.

A workspace-scoped broad reference_search timed out after 600 seconds. A narrower search for state_target any_owned_state also timed out after 600 seconds. A revision-bound reference_read for the cited Decision modding page at startLine 465 with maxLines 55 and the confirmed workspace ID timed out after 600 seconds. The corresponding offline wiki and installed documentation sections were read directly from the local files and are cited below.

Two source lookups were attempted. The initial definition-only lookup of sov_nuclear_bombs_register_assembly_site with maxLines 12 and no references timed out after 600 seconds. The explicit-workspace retry for sov_nuclear_bombs_event_active_assembly_site_is_valid with maxLines 12, maxDefinitions 1, and includeReferences false also timed out after 600 seconds. No source_lookup artifact or indexed caller list was returned.

The first decision_inspect call was rejected because it omitted the required scenarios field. A retry with a declared SOV readiness-49 scenario, candidate override labeled as an assumption, and explicit workspace ID timed out after 600 seconds. No decision scenario or target-row artifact was returned.

The first chaosx_ai_probability_auditor attempt reported that its probability functions were unavailable to that child model. A parent-side probability_inspect request without a workspace ID timed out after 600 seconds. The fresh auditor retry used workspace ID mod_chaos_redux_ea3b2d67c2c0 and the required mod-relative source object for separate decision and mission inspect calls. Neither call returned an error or analysis artifact before the auditor terminated the pending orchestration call. No probability analysis ID, scenario hash, comparison ID, rendered artifact, or scenario score is available here.

The repository files remain the primary direct evidence. Offline reference spans read locally were Decision modding lines 345-375, 469-478, 527-535, 576-585, and custom cost/text icon lines 305-332; Scopes lines 811-855; Data structures lines 263-312; Effects lines 357-360; On actions lines 257-263 and 450-455; Localisation lines 221-242; and Triggers lines 638-646. Installed documentation read locally included Country Decisions lines 1-46, effects activate_mission lines 661-668 and event target effects lines 2733 and 6496-6512, plus trigger exists lines 2708-2715 and has_event_target lines 3844-3851. A Vanilla SOV state-targeted decision precedent uses state_target = any_owned_state at common/decisions/SOV.txt:11001-11020.

No GUI MCP evidence was requested because this accepted surface is an ordinary state-targeted decision and mission with no scripted GUI or layout work. No game, save, or logs were used.

## Files, identifiers, validation, and remaining work

Only this handoff file was written. No decision, mission, helper, localisation key, asset, workbook, or Git identifier changed. Before and after behavior are unchanged by this read-only audit.

Inspected source snapshot SHA-256 values:

| File | SHA-256 |
| --- | --- |
| common/decisions/023_sov_nuclear_bombs_decisions.txt | DBDBD0E234CF54F54ED36B6F28236648B67A4E6A95F4DF35C604E4D3ED258DA0 |
| common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt | 90D44CC3BE29BC20971489031B3B94A8417658274A70C69629B0A9A789DC9D1E |
| common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt | C590E8E883D375702500E321E8B81B29EB03E9A88C71E3458673EF25E4FBF2CB |
| common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt | 89BDD16A12D23DBFFEDFE31806CC5E0E7ECF7F909412806C134A20588492A9A3 |
| common/on_actions/023_sov_nuclear_bombs_on_actions.txt | B8B9E20220CE345540C2160B8948D9D21376618DE9AAD0C54D9ED6B4B61DC39E |
| localisation/english/023_soviet_nukes_l_english.yml | 9C5A7C50F63A2E9FED35F10CE695658797AF19EC4E27E98DCC2CEBA8E0E35565 |

Meaningful validation completed was a source crosswalk against the accepted Part 6 and Part 10 criteria, the parent implementation note, the exact assembly decision and mission path, the selected-site predicates, capture and annex callbacks, and the matching player-facing localisation. No game runtime, save and reload, probability score, decision scenario, or target-row rendering validation completed.

The parent should resolve the exact nonce-mismatch closure behavior, verify actual decision row counts under named scenarios, complete the required probability audit through chaosx_ai_probability_auditor, and confirm the Event 5 transfer call-site wrappers through an authorized MCP or parent review route. The actual security debit helper definitions and global external callers were outside the exact source allowlist and remain unaudited.

Skills used: chaos-redux-decisions-missions, chaos-redux-events, and chaos-redux-subagents. No skill was created or modified. No plan handoff was written because the open issues are bounded audits and local clarity or receipt checks.
