# Event 012 Gods Recovery AI and Probability Audit

Audit date: 2026-10-04.

Status: The read-only source audit is complete for the six recovery decisions and the newly widened resume action. Engine-level ranking, exact AI selection behavior, and balance conclusions remain unresolved because the connected analyzer had no eligible scenario candidates and the actual cross-category candidate pools were incomplete.

The report preserves the parent’s accepted full Gods goal, no-simplifications requirement, and recommended original-host congress design. The parent-supplied baseline is that the six recovery rows were absent at commit 3669cba8d; Git was explicitly prohibited, so that commit claim was not independently verified.

No gameplay, AI, event, decision, scripted effect, scripted trigger, localisation, or other source file was edited. No Git command or HOI4 launch was used. This handoff is the only file written by this audit.

## Audited surfaces and source identity

The six weighted rows are gods_of_africa_restore_original_mandate, gods_of_africa_invite_original_mandate_member, gods_of_africa_finish_original_mandate, gods_of_africa_resume_original_mandate, gods_of_africa_approve_original_mandate, and gods_of_africa_decline_original_mandate in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/decisions/012_africa_gods_recovery_decisions.txt.

The authoritative AI and quorum values are in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/script_constants/012_africa_gods_recovery_constants.txt.

Recovery row gates and the current due-clock helpers are in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/012_africa_gods_recovery_triggers.txt.

Recovery start, member invitation and answer, mandate commit, and due-clock repair effects are in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/012_africa_gods_recovery_effects.txt.

Competing legacy weighted decisions are defined in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/decisions/012_africa_gods_decisions.txt. Their categories are declared in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/decisions/categories/012_africa_gods_categories.txt.

The existing wake events are defined in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/events/012_africa_gods_of_africa.txt.

The accepted Gods requirements and defeat/re-legitimation boundary are in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/specs/012_africa_is_one_gods_of_africa_specs/specs/012_gods_of_africa_full_spec.md:1-110 and 1070-1085. The parent’s accepted congress design and scenario material are in C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/012_africa_plans/subagent_handoffs/012_africa_gods_original_host_recovery_design_2026-10-03.md.

The source changed while the audit was running. The pre-widening working-tree decision file had physical SHA-256 7A24177DFAA4275DCEDBB8F4132C70C0154C2DF90F1768C4FB788756B4E9E36E and MCP sourceHash a816bc23166c199afe2f09f6769707a8f1433dbd716da16725d08c8ceb457c35 at sourceRevision 7fefd5ea61aee7d21333d85d87ae0369aa12d5cef36a83ab56949dd86626441e.

An intermediate source snapshot had physical decision-file SHA-256 D0F462A26B2A6378D649C75A0B8DAF0A0762D2208FFFE0B13EF1B71DC657F752, MCP sourceHash 2eba2417192f7b143a2a0adb7b3cde6259e4a4dc4b40a77f81adb9ad768da24d, and sourceRevision 97bc0f0aa6529da289881d534f6394ecefc7d3f22c2a0690b35094b8708f2275. A later source lookup showed the widened resume visibility gate; the final local read confirms that gate remains in place.

The last observed decision file has physical SHA-256 CB6C0965F03B25E2D3E7A4D653EDEE380C1FE70C0E1791766914643124E6CFD1, MCP sourceHash 6dc8a4461e2cfa8d31457be216df36f52512093b81f25817cb661c544c3a6392, and weighted-source revision 6967ccf321b52ac10c0df76bc1d1e928efc06b3be7eeff0623cc960a451ff078.

The current resume-gate source lookup returned revision 669a9ad00120f961896461aba9dcc8fff61f7ed2611a7d0578a3718284e7089d and a complete definition for gods_of_africa_recovery_can_resume at lines 310-321. The exact resume decision definition was returned at lines 80-96 in source lookup revision ae19cd1aefa3f04847edcf5f1a094311fe87c08542c15f5e5c353106e95b924b; the decision file’s final physical hash is unchanged from that lookup.

Final physical source hashes at the last local read:

| Source | SHA-256 |
| --- | --- |
| common/decisions/012_africa_gods_recovery_decisions.txt | CB6C0965F03B25E2D3E7A4D653EDEE380C1FE70C0E1791766914643124E6CFD1 |
| common/script_constants/012_africa_gods_recovery_constants.txt | 4FB023940CE5CB8695F849A01C9F65696E2B5F7B48AD5AA129877FA797A424CF |
| common/scripted_effects/012_africa_gods_recovery_effects.txt | 55932CB10E1A6CB021CAA4B8C4D4B385755C0AF18677624403B4CA1F0A29ED12 |
| common/scripted_triggers/012_africa_gods_recovery_triggers.txt | 3664AB41FA1BFC62ECA631C5E1618CFA94E3E3DDA7568D0C749C816E5E34369C |
| common/decisions/012_africa_gods_decisions.txt | 6D6FB4A7EFC3750CE15A4925FFEEB4B42A38B689A9EC345F045FD78944ECF0F0 |
| common/decisions/categories/012_africa_gods_categories.txt | 88272D874647CEFF2596CA8C840226E6AC91E41A012DC800214A28C32AA9F581 |
| events/012_africa_gods_of_africa.txt | 9130D9A956EC6AE17E03BD787BE5D0177CD4021C07FEA80D94F7072B5915DF53 |

The constants file centralizes start_finish = 10, invite_resume = 5, approve = 10, decline = 1, unstable_accept_factor = 0.25, unstable_decline_factor = 4, and stability_threshold = 0.35. The separate quorum constants are minimum_approvals = 2 and majority_multiplier = 2. The six decision rows refer to these constants; their AI tuning values are not hardcoded in the decision bodies.

The shared values are intentional cross-phase reuse. No contradictory or unbounded expression was found in the six rows.

## Score traces and gating

| Decision | Actor scope | Source-defined AI score | Source gate and score classification |
| --- | --- | --- | --- |
| gods_of_africa_restore_original_mandate | Host ROOT | Base 10 through start_finish; no row-specific modifier | Visible for the current original-host recovery opportunity. Available only with current original-owner identity, revoked/loss state, physical return, first-proof condition, and at least two currently eligible members. Score-only source trace. |
| gods_of_africa_invite_original_mandate_member | Host ROOT, member FROM | Base 5 through invite_resume; no row-specific modifier | Targeted over africa_relationship_countries. The member must be currently eligible and have no current recovery receipt. Score applies per matching target entry, so the live target count affects the candidate pool. Score-only source trace. |
| gods_of_africa_finish_original_mandate | Host ROOT | Base 10 through start_finish; no row-specific modifier | Visible for a current recovery congress. Available only with physical return, at least two current approvals, and a strict current-member majority. A failed quorum can leave the row visible but unavailable; MCP did not prove how the engine filters that row from AI selection. |
| gods_of_africa_resume_original_mandate | Host ROOT | Base 5 through invite_resume; unchanged in the parent update | Visible and available through gods_of_africa_recovery_can_resume. The gate is the OR of current due activation, owner, or registry wake receipts, followed by a one-repair-per-day guard. |
| gods_of_africa_approve_original_mandate | Member ROOT | Base 10; factor 0.25 when has_stability is strictly below 0.35 | Requires a current host-bound member request and excludes an active demand, negotiation, or reconciliation response phase. The current member answer effect clears the opposite answer before adding the selected vote. |
| gods_of_africa_decline_original_mandate | Member ROOT | Base 1; factor 4 when has_stability is strictly below 0.35 | Uses the same current-request gate as approval. The current effect removes the member from approval arrays when declining. |

The source therefore defines opposing low-stability factors for approval and decline. This is a source-level indication that low stability is intended to reverse the base preference; it is not an MCP-confirmed score ranking. The analyzer returned no eligible rows for the low-stability fixture, so I do not claim transformed numeric scores or a verified rank reversal.

The host and member decisions use different actor scopes and categories. Their weights must not be summed or normalized together. The offline AI modding wiki describes most ai_will_do surfaces as score races with the highest generated score selected, while the Chaos Redux decision skill requires reporting these decision values as willingness scores rather than click probabilities. Event-option ai_chance proportional sampling and event MTTH timing distributions are not involved in these six rows.

## Current resume row and RCV-LIVE-DUE-REPAIR

The current decision source uses gods_of_africa_recovery_can_resume in both visible and available. This closes the visibility mismatch seen in an earlier local read during the parent’s concurrent update and exposes the same existing row for a valid due activation, owner, or registry receipt.

gods_of_africa_activation_wake_is_due requires current epoch permission, consolidation pending, the actual activation-clock scheduled flag, the current due-day variable reached, and a current recovery mandate when the recovery epoch applies.

gods_of_africa_owner_wake_is_due and gods_of_africa_registry_wake_is_due each require current epoch permission, active Gods state, committed activation, their own scheduled flag, their own due-day variable, and current date greater than or equal to that due day.

gods_of_africa_recovery_can_resume additionally requires ROOT to be the host and limits repair to one invocation per day through gods_of_africa_last_clock_repair_day.

gods_of_africa_resume_original_host_recovery selects the matching stored clock kind and due day, then calls gods_of_africa_schedule_current_clock. The scheduler checks current permission and exact due-day identity and queues only the existing chaosx.nr12.600, chaosx.nr12.606, or chaosx.nr12.607 event with at least a one-day delay. The repair effect does not change the due date, authority epoch, or epoch permission.

If activation, owner, and registry are all due at once, the effect’s if/else-if order selects activation first, then owner, then registry. One decision repairs only one receipt per day; the other due receipts must remain eligible for later repair. This is bounded source behavior, but its actual AI selection and delay under a full host decision pool were not resolved.

The requested RCV-LIVE-DUE-REPAIR scenario is included in the current seven-scenario evaluator. Its campaign state was left empty rather than fabricating typed scopes or permission overrides. The source predicates exclude wrong permission, early date, and inactive-host owner/registry cases; the MCP scenario did not independently prove those branches.

## Scenario results and completeness

The current scenario set id is RCV-EVENT012-RECOVERY-AUDIT-2026-10-04-v2 and its scenario hash is 96139b903dce07f640472c9416d1812757ea2bd88def9847f1958801887433a5. All seven required scenario ids were passed to the final evaluator. The state object was empty for each scenario except RCV-MEMBER-LOW-STABILITY, which used stability = 0.34 as one representative value from the parent-declared below-0.35 band.

The live probability fixture contract required scenarioSet to be an object with a set id and each scenario to provide a state record. No actor, typed scope, controls, event-target, or candidate-override data was supplied.

| Scenario id | Declared test | Candidate-pool and external-factor completeness | Source trace and result classification |
| --- | --- | --- | --- |
| RCV-ORIGINAL-RETURN-PEACE | Current original committed host, origin identity matches, loss epoch revoked, capital controlled, Evolution I and first proof active, no terminal or successor state | Incomplete. No native ROOT country id, current africa_host target, flags, origin/generation/loss variables, capital controller, or first-proof fixture was supplied. | Bounded source logic only: recovery start is gated on those facts. MCP returned the row as never eligible under the empty fixture. Overall result unresolved. |
| RCV-CONGRESS-2OF3 | Three eligible current members, two approvals, stable and cooperative | Incomplete. No host identity, three actual member scopes, relationship array, invitation receipts, current approval flags, or arrays were bound. | Bounded source logic only: the quorum checks minimum approvals and 2 × approvals greater than eligible count. No exact engine or selection result. Overall result unresolved. |
| RCV-INVALID-2OF4 | Four eligible members, two approvals, quorum must fail | Incomplete for the same host/member-array reasons. | Bounded source logic only: the strict-majority predicate rejects a half vote. Finish retains a positive base score while unavailable; the analyzer did not verify native AI filtering. Overall result unresolved. |
| RCV-MEMBER-LOW-STABILITY | Current invited member under 0.35 stability | Incomplete. Stability 0.34 was supplied, but no member actor, current request, host target, or category candidate pool was supplied. | Score-only source trace for base/factor expressions. MCP excluded both rows and returned no ranking. Rank reversal and churn remain unresolved. |
| RCV-DUE-CONSENT-RESTORED | Expired 180-day consolidation, current epoch 2, pending state, current scheduled activation receipt, restored quorum | Incomplete. No current date/global day, due day, activation receipt, epoch variables, member arrays, or host identity were supplied. | Bounded due and mandate predicates only. MCP returned resume as never eligible in the empty fixture. Overall result unresolved. |
| RCV-STALE-PERMISSION | Expired hint with wrong epoch, successor, or different origin | Incomplete. No actual owner identity, successor state, permission variables, receipt flags, or date were supplied. | Bounded rejection through current identity/epoch/permission predicates. No MCP branch proof. Overall result unresolved. |
| RCV-LIVE-DUE-REPAIR | Competing due owner/registry receipt; wrong-permission, early, and inactive cases excluded | Incomplete. No native host actor, owner/registry scheduled flag, due-day variable, current date, active/committed flags, permission fields, or last-repair day were supplied. | Bounded current due-repair path, one row, one repair per day, with activation-before-owner-before-registry branch order. MCP returned resume as never eligible in the empty fixture. Overall result unresolved. |

The six-row source inspection with an explicit six-id candidatePool reported candidates = 6 and poolComplete = true. That is completeness for the six definitions in the recovery file only; it is not completeness for a live HOI4 AI selection race.

An earlier narrow source inspection of gods_of_africa_resume_original_mandate returned candidates = 1, poolComplete = true for that one-row query, and availableCandidates = 0. It used the intermediate sourceHash 2eba2417192f7b143a2a0adb7b3cde6259e4a4dc4b40a77f81adb9ad768da24d and sourceRevision 97bc0f0aa6529da289881d534f6394ecefc7d3f22c2a0690b35094b8708f2275. That discovery result was not a live campaign availability result and predates the final broadened visible gate.

Inspection of the legacy 012_africa_gods_decisions.txt source found 36 adapter candidates, poolComplete = false, and requiredInputPaths = scope.FROM. A bounded local source inventory found 20 weighted host-category rows and 18 weighted participant-category rows in that file. The local inventory and adapter count differ by two; the linked analyzer artifact could not be recovered, so that discrepancy remains unresolved.

The legacy host candidates identified locally are gods_of_africa_choose_reciprocal_covenant, gods_of_africa_choose_sovereign_exaction, gods_of_africa_choose_strategic_ambiguity, gods_of_africa_prioritize_land, gods_of_africa_prioritize_support, gods_of_africa_prioritize_fuel, gods_of_africa_prioritize_manpower, gods_of_africa_prioritize_industry, gods_of_africa_prioritize_transport, gods_of_africa_prioritize_air_defense, gods_of_africa_prioritize_emergency, gods_of_africa_grant_leniency, gods_of_africa_public_pardon, gods_of_africa_protect_partner, gods_of_africa_accept_substitute, gods_of_africa_reject_substitute, gods_of_africa_commit_settlement, gods_of_africa_accept_reconciliation, gods_of_africa_mark_offender, and gods_of_africa_escalate_offense.

The legacy participant candidates identified locally are gods_of_africa_demand_mission, gods_of_africa_reconciliation_mission, gods_of_africa_offer_voluntary_aid, gods_of_africa_comply_demand, gods_of_africa_partial_compliance, gods_of_africa_negotiate_demand, gods_of_africa_substitute_demand, gods_of_africa_substitute_demand_slot_1, gods_of_africa_substitute_demand_slot_2, gods_of_africa_substitute_demand_slot_3, gods_of_africa_return_to_demand, gods_of_africa_refuse_demand, gods_of_africa_permanent_defiance, gods_of_africa_prepare_defensive_defiance, gods_of_africa_harden_stockpiles, gods_of_africa_secure_transport, gods_of_africa_prepare_countermeasures, and gods_of_africa_seek_reconciliation.

The host category exposes additional legacy decisions when the active host is valid. The recovery and consolidation phases have different visibility. Targeted invitation entries multiply by the number of currently eligible, uninvited members. During consolidation, member answers can still change until the current mandate is consumed; the answer effect clears the opposing flag and updates the approval arrays, and quorum is recounted from current eligible members. This avoids double-counting both answers but allows vote churn and can delay activation if live approvals fall below quorum.

The actual candidate pool can therefore vary by host/member actor, targeted FROM member, invitation receipt, active phase, demand flags, current arrays, and due-clock state. No exact normalized selection probability, dominance, or starvation result is supportable from the supplied fixtures.

Dominance, starvation, and selection frequency are unresolved rather than passed. The analyzer did not evaluate the complete active-host decision set. The base-5 resume row may compete with many legacy choices, and invitation candidate multiplicity grows with matching FROM members. These are scenario-review risks, not measured AI behavior.

## AI validity, repetition, and risk findings

All six rows have explicit ai_will_do blocks and use centralized finite constants. No missing weight, unbounded numeric value, or duplicated decision identifier was found in the six-row source review.

start_finish = 10 is shared by restore and finish, but their phase gates separate those actions. invite_resume = 5 is shared by invite and resume; the two actions have different target and due-state gates. Their equal base score does not establish a tie or click probability.

The approve and decline factors are intentionally state-sensitive at a strict less-than 0.35 threshold. The source design implies a conditional rank change, but MCP did not establish it. The evaluator’s six PROBABILITY_OUTCOME_NEVER_ELIGIBLE diagnostics are caused by the supplied fixtures missing the actual actor and state bindings; they are not evidence that the rows are dead in campaign state.

Finish can carry base 10 while its quorum gate is false, and resume carries base 5 while its due gate is false. Both are visible/available-gated rows, but this analyzer run did not verify the engine’s treatment of unavailable decisions. No claim is made that such rows can be selected while unavailable.

The answer actions have no explicit cooldown and fire_only_once is no. A member may switch between approval and decline while the request remains current, including during consolidation. The effect prevents simultaneous vote accumulation, but the AI can potentially oscillate or keep the mandate below quorum. Repetition frequency is unresolved because the decision pool and selection cadence were not supplied.

Invite is a targeted row with one candidate entry per current eligible member without a current receipt. Its finite relationship registry and receipt gate prevent repeated invitations to a member whose receipt is current. The per-target candidate multiplicity was not evaluated against the full actor pool.

The resume row has one repair-per-day state guard, and each successful branch queues one of the existing three wake events with a one-day minimum. No repeated same-day repair or timer reset is present in the reviewed source. Whether base 5 is sufficient to prevent AI delay when many active host decisions compete is unresolved; no new balance target is recommended.

No explicit references to the six recovery identifiers were found in common/ai_strategy or common/ai_focuses during the bounded repository search. This does not prove that no engine-level or external strategy modifier can affect the broader decision-selection process. The six source weights themselves do not scale with Strength, Wrath, or another campaign pressure; broader gameplay snowball behavior was not inferred from this weight audit.

## MCP evidence and artifacts

The connected workspace id is mod_chaos_redux_ea3b2d67c2c0.

The mandatory initial source discovery used hoi4.probability_inspect on common/decisions/012_africa_gods_recovery_decisions.txt. It returned sourceHash a816bc23166c199afe2f09f6769707a8f1433dbd716da16725d08c8ceb457c35, sourceRevision 7fefd5ea61aee7d21333d85d87ae0369aa12d5cef36a83ab56949dd86626441e, six matching identifiers, and an incomplete pool. The artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9822faa26b4649907cdb69dbf291668c0e888d3239358722a2e6648d209f5a30/9995a840e909bc81a47b8ae03e1239f682a3112042a5232251c92cff9c31595d/probability-inspect-a816bc23166c.json.

The first adapter-only probability inspection returned MCP error -32602 because this adapter requires a source. Source-only discovery and the subsequent source-bound inspect succeeded.

The final six-id recovery-source inspection used hoi4.probability_inspect with decision_ai_will_do and returned sourceHash 6dc8a4461e2cfa8d31457be216df36f52512093b81f25817cb661c544c3a6392, sourceRevision 6967ccf321b52ac10c0df76bc1d1e928efc06b3be7eeff0623cc960a451ff078, candidates = 6, and poolComplete = true for that explicit source list. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a5c237179ea337db476de523a9a9801edc10e93a6a8763a8ddd5b2c19462880/41d1a7e14833faf48c4526bdf5d3c3ef5a9d93f9687caf60c86ea446795ff355/probability-inspect-6dc8a4461e2c.json.

The final legacy-source inspection returned sourceHash 1692058d825b8bf3cd581548b0fc46c1662605ed5799a709f4d2cdca18863b13, sourceRevision ab07578b2803227f158f4031fe55c5454cd47f1147626e5520ae0488e704d914, candidates = 36, poolComplete = false, and requiredInputPaths = scope.FROM. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/582831071db71e4b2f8b73be210baa7c6ec7f2beda997c1fffaf540f7fe04a70/b8606d4a02fd10dd96795dbae4e11bfce11c1d7707848f95b354c565010c9dda/probability-inspect-1692058d825b.json.

The final named-scenario evaluation used hoi4.probability_evaluate with raw_value and the six recovery identifiers across the seven scenarios above. It returned analysisId probability-1c2081cd9aa3d592c3d68b5a, scenarioHash 96139b903dce07f640472c9416d1812757ea2bd88def9847f1958801887433a5, sourceRevision 6967ccf321b52ac10c0df76bc1d1e928efc06b3be7eeff0623cc960a451ff078, candidates = 42, eligibleCandidates = 0, excludedCandidates = 42, and unresolved = 204. All six decisions were reported never eligible across the supplied fixtures.

The final evaluation JSON is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08261df33a37913e930c51ebd921f02a5a290afc3248506357c5e2c756a8aece/38c341bc34cf48420501f02a88722be9c82216cdad36cc17d227b0cf3f540c71/probability-1c2081cd9aa3d592c3d68b5a.json.

The immediate hoi4.probability_render call retained a partial ranking at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/888bffe3770e5d1a2bcd7825707aa79e9fbe79bc04f3b2781230a73aabdbba8c/b47632e00b44a67fd91fdae1629415a8fb0191a6eed0a767ae74c160b575c229/probability-probability-1c2081cd9aa3d592c3d68b5a-ranking.svg and an unresolved view at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a33dc2aecff8747bd2d3bd10530bebe6f08efadd54106c05ddc24ad34712dac/bf045c65655d649408983c183cac058b4635d85ce648fcd00216a06479e96c53/probability-probability-1c2081cd9aa3d592c3d68b5a-unresolved.svg.

The current one-point hoi4.probability_sweep used analysisId probability-ada891f6865c40d74cd95114, scenarioHash c72b7b036b94ea88171a73dd25add7bfcecccc92cb5031c517824de7a2542c18, and sourceRevision 6967ccf321b52ac10c0df76bc1d1e928efc06b3be7eeff0623cc960a451ff078. It covered the numeric stability = 0.34 input but returned only one sweep point, zero eligible candidates, and 78 unresolved items. Its sensitivity artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e911c36226d9cf8ac7235c19dd95a0a2fe1259e8e445c41187976b23229eb4aa/da7f8eed84cee0d3391cadefa7878bc47fc88ea1809b81805684e7794e9668d1/probability-probability-ada891f6865c40d74cd95114-sensitivity.svg.

The corresponding one-point threshold view is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/72bb34a5fd76123669940fd2e31ed94c5c729d6f32abf7211460550ff42c6223/probability-probability-ada891f6865c40d74cd95114-threshold.svg. The unresolved view is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5e192102425508a48ce3c7411fa57f5d7a40eca8abf4431eeaf6490e405ccef/71c362a2eb26ecf3fbf23361fa027e8d7485ddb8de438516aa6da1e00ed1e632/probability-probability-ada891f6865c40d74cd95114-unresolved.svg.

An initial sweep over source constant paths failed with PROBABILITY_SWEEP_RANGE_REQUIRED. A second attempt using stability alternatives [0.34, 0.35, 0.36] failed with the same code because the connected route did not accept that range shape. No further fixture fields were guessed.

The baseline inspection represented the parent-supplied absent-row baseline with an empty inline Clausewitz source. It returned no weighted surfaces, sourceHash 24faa4586103c2750a406d3459eb83e7e63eec41c208d44e51b62272b67ed002, and sourceRevision d4abd70bb1b90c8b1205d6b7f4d8b66884150bbe27c5ab5ddc54f569528ed6d9. Its artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/186e5bc9fcd29a16fdf079b654c27163f55dabef738ef5a21bd1243393af2b1b/9a6fa5b5c56723d16b6c3d7a273f793f8b35db9146c1dc672f7c8c2a5e874f2e/probability-inspect-24faa4586103.json.

hoi4.probability_compare was attempted with that empty baseline, the current recovery decision source, and the same seven scenario ids and state objects. It returned PROBABILITY_SURFACE_EMPTY because the baseline contains no weighted blocks. No comparison id or numeric delta exists. The existing 012_africa_gods_decisions.txt source was not substituted as a false before-snapshot, and the current recovery source was not compared to itself.

The separate renderer initially returned PROBABILITY_ANALYSIS_NOT_CACHED for earlier analysis ids. An immediate render after fresh evaluation succeeded for the final seven-scenario evaluation and the final one-point sweep.

hoi4.decision_inspect returned DECISION_ANALYZED_PARTIAL for the named resume row and seven scenarios, with complete = false, 218 unresolved definitions, and an inline inventory limit of 64 out of 6,579 paths. The report artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16cdada08a5b665e6a8b8f819b23e0074dbbbe22adcd08c9da66842c20193bbd/fa1fc407f71b115a6f8df3d7672dfa09b184616850b1b0c320b420beb8555cfc/decision-1f30cc05fcf28f58fdc34fa7.json. The report did not supply a complete actual candidate set.

The focused Event 012 trace for chaosx.nr12.600 was partial at event revision d0087fea8accc02308dd34698d35ccfa59abc878e1f3543a1d6d6157785a4482. Its trace artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/878e820dc958cc2e3cb933648971ddec8f5d267a123d1345d13a7fbac7e0df82/1768d603d90c9d6fd6e41b8cf36b1fb8734c34f0f8aff2ad313b0c8fc88263e7/event-trace-d0087fea8acc.json.

Focused traces for chaosx.nr12.606 and chaosx.nr12.607 returned partial event revision d397c49bcd704632e8edc807c7fbaf2d801de75dd4f095a9ee52deac8d3673e5, aggregate graphHash a4b6fe766c02615eedc5b5ab0bfcfa4d8edddefaa78bc814b4f14ae2940e9d49, and the same broad unresolved counts. The .606 artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74b073eae7250f6eb33034e500e0261e44ae9556de7ef613bd8147bc7933f6a2/5486d573233f671baa136400029e44fc5d962543691f493958b96336c00909ff/event-trace-d397c49bcd70.json. The .607 artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/895d62de5cf46665da5464cd99c26429b5c2c9b33dee37a208eff785acd2042c/379ece26d98a27b506d8e6f30dae00335e154361e916d4456f7e05a77433faea/event-trace-d397c49bcd70.json.

The event neighborhood render for .600 returned EVENT_RENDERED_PARTIAL at event revision 6b9a6428e7573efc5012d443d97c822ff503dfc95bfa7688d849b8093c88c733 and graphHash 953f84b7e8b2fb596118e7f28ad466f155a09346e53965d72ebc77f93411ad36. It selected two nodes, reported 2,193 diagnostics, 42,995 omitted nodes, 8,983 unresolved nodes, and zero helper projections. The source-linked SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05b6a6f5264adecb1ad5600bb302b6b7c92fd97c1a9693976aaa56916b5d9f67/628523795c42429618e8bdfe2830e75607c5b258a91fdc49366d11ac80708624/event-neighborhood-6b9a6428e757.svg. The PNG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/128dc15ce49cdf9aa7b76d33bde70302895dd99674ff54df71d783e8fb7fcc74/1ed67590ee50609737965431a108ed46f35fb2474ab37c15921a38f96f1bae7d/event-neighborhood-6b9a6428e757.png.

The initial 81 KB probability-inspection artifact could not be read: read_mcp_resource returned MCP error -32603, Artifact provenance manifest is unavailable. A byte-range retry returned the same error. It is retained as an unresolved artifact-read blocker; no candidate details were inferred from it.

The connected reference context was workspace mod_chaos_redux_ea3b2d67c2c0, surface decision, with no missing or omitted sources. The installed vanilla Country Decisions documentation was read at C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md:1-46, section revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019. It documents that visible is separate from available, and gives the scopes and cadence for targeted decision checks.

The offline Decision modding wiki’s AI section was read at paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:357-374, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162. The offline AI modding wiki’s MTTH blocks section was read at paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md:26-37, revision 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818. The latter describes score-race behavior for most ai_will_do uses and distinguishes event-option ai_chance sampling.

The explicit search under the installed documentation directory found no ai_will_do or decision-weight section. The installed common/decisions documentation above supplied the relevant vanilla visible/available/target contract.

## Recommended parent follow-up

Keep the current six centralized AI values unchanged until a complete actor-specific candidate pool is available. This audit does not choose new balance targets, and no balance target was changed.

Preserve a real pre-change source snapshot before any later weighted edit. Re-run probability_inspect, evaluate the same seven named scenarios with source-supported ROOT and FROM identities, current host targets, relationship and approval arrays, flags, dates, and scheduled-clock receipts, then compare the preserved before-source with the after-source under the identical scenario set.

Do not treat the six new recovery rows as the complete campaign selection pool. Include relevant legacy host/member decisions and every targeted invitation entry in the per-actor candidate pool. Resolve the analyzer’s 36-candidate legacy inventory against the 38 local category rows before making normalized or dominance claims.

Exercise the current one-day repair under due owner-only, due registry-only, both-due, wrong-permission, early-date, inactive-host, and same-day repeated-click states. Confirm that activation-before-owner-before-registry priority is acceptable and that the AI reaches the resume row while ordinary active host decisions compete. Keep the base AI score unchanged unless a later complete comparison produces evidence for a different target.

Exercise approval followed by decline, decline followed by approval, votes that change during consolidation, and quorum changes after a relationship member enters or leaves the live registry. The current effect prevents double-counting but permits answer changes without a cooldown. If the accepted design requires irrevocable votes, any lock belongs in gods_of_africa_recovery_member_request_is_current in common/scripted_triggers/012_africa_gods_recovery_triggers.txt and gods_of_africa_record_recovery_member_answer in common/scripted_effects/012_africa_gods_recovery_effects.txt; no such change is recommended without that design basis.

## Skipped analyses and remaining uncertainty

No exact or normalized AI choice probabilities are reported. The overall candidate pool, actual ROOT/FROM actors, schedule receipts, and external selection factors were incomplete.

No exact ranking or timing distribution is reported. The named evaluator excluded all 42 decision/scenario rows, and the stability sweep produced one point with no eligible candidates.

No sampled simulation was run because no stochastic input distribution or seed was declared. No probability sequence was run because this is not a complete custom weighted pool with cadence and transitions.

The baseline comparison is unresolved because the explicitly absent-row before-source has no weighted surface. The MCP returned PROBABILITY_SURFACE_EMPTY, so no comparison id or numeric delta is available.

The event inspect/render output remained focused and partial. No helper-expansion, job, or native task route was used because server health/version and task negotiation were not exposed. The broader event lifecycle and scenario branches were not proven by these focused artifacts.

No live-game behavior, decision cadence, cooldown, or AI click sequence was observed. The audit did not launch HOI4, inspect a save, run tests, or use Git.

The scenario and API evidence was read-only. The only authored output is this handoff.

Skills applied: chaos-redux-subagents, chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-event-planning, and chaos-redux-mtth. No skill was created or updated.
