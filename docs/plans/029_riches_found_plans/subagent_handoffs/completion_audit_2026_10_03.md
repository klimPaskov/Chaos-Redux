# Event 029 Riches Found completion and gap audit

Disposition: completed read-only completion audit, Event 029 implementation incomplete.
Acceptance basis: the parent's explicit 2026-10-03 assignment and the user's instruction to implement every accepted requirement in `docs\specs\029_riches_found_specs\` without simplifications, fallbacks, placeholders, or omitted routes.
The parent owns implementation and integration, DecisionAudit owns decisions and cost triggers, and `chaosx_ai_probability_auditor` owns the probability pass.
This auditor changed only this report through `apply_patch`.
No gameplay, localisation, asset, workbook, CSV, index, or commit operation was performed, and HOI4 was not launched.

For current repaired-source status, use the [fresh 18:26 checkpoint](#fresh-source-checkpoint-at-1826).
The following 15:35-15:57 introduction and historical sections describe earlier observations whose repaired findings are explicitly superseded there.

This is an observation of a concurrently changing worktree, principally at 2026-10-03 15:35-15:39 Europe/Kiev.
The final narrow follow-up at 15:53 is recorded below and supersedes the identified account call-site and tool-exposure observations.
The parent's subsequent terminal-verification and cost-localisation update was read and checked at 15:57, with its source-only disposition added below.
Identifiers are authoritative anchors because parent edits move source lines.
The source identities below bind this checkpoint, not a frozen final implementation.
The account helper was added during this audit, so the earlier architecture handoff's statement that no obligation record exists is superseded for source presence, while decision integration and acceptance remain open.
The cost-display selectors were also repaired during this audit, so the decision handoff's strict-display comparison finding is stale for current source.

## Fresh source checkpoint at 18:26

Disposition: verified documentation supersession of the parent's listed source repairs, with Event029 still incomplete.
Acceptance basis: the parent's latest explicit request to add fresh source links and supersede repaired P0 claims through a docs-only update.
This section is the current-status override for the specified repairs.
The earlier 15:35-15:57 requirement table, priorities and hashes remain historical observations and must not be reused as claims that these repaired source contracts are still absent.
Source presence, accepted design and engine/probability evidence remain separate.
No new MCP, probability, viewer, game, workbook, index or commit request was made in this update.
Only this audit document was changed.

| Earlier finding or requirement | Superseding source status | Fresh exact source links and current behavior | Remaining acceptance limit |
| --- | --- | --- | --- |
| Occupation circular predicate | Earlier occupation P0 is superseded | [TRIG:545](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_triggers.txt:545>) reads registration, existing owner/controller and owner/control mismatch without requiring the occupation flag. [CORE:1958](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:1958>) can then initialize the occupation flag/date. | Actual transfer, resistance/compliance/supply economics and occupation choices remain unverified. |
| Partial/quarantined generic closure | Earlier conditional-output obstruction is superseded | [CORE:626](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:626>) derives generic closed only from temporary closure, permanent sealing, collapse or exhaustion. [TRIG:204](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_triggers.txt:204>) retains guarded reduced-output paths for controlled quarantine and partial sealing. | This repairs the blocking flag contract, not every partial-seal/recovery route or output balance. |
| AI mine scope and terminal selection | Earlier AI selected-mine blocker is superseded | [TRIG:171](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_triggers.txt:171>) admits AI controllers independently of the human selection pointer. [TRIG:123](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_triggers.txt:123>) rejects a terminal selected mine, and [CORE:990](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:990>) skips terminal mines when assigning a new pointer. | Bespoke action preferences and the changed multi-mine candidate set still need the specialized probability pass. |
| Canonical payroll robbery | Earlier three-name receipt mismatch is superseded | [INC:568](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_incident_effects.txt:568>) writes riches_found_pay_train_robbery_succeeded and resets the success count/ready/sequence flags. [CORE:1778](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:1778>), [DEC:8667](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/decisions/029_riches_found_decisions.txt:8667>) and [ACH-T:95](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_achievement_triggers.txt:95>) consume that same receipt. | The robbery reset is source-present. Complete route-risk, continuous supply, closure/transfer sequence history and exploit acceptance are not claimed. |
| Death history and Last Shift aliases | The specified historical receipt omissions are superseded | [HARM:53](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_harm_effects.txt:53>) invokes the achievement mass-death recorder from the actual applied-death threshold. [ACH-E:205](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_achievement_effects.txt:205>) and [ACH-T:206](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_achievement_triggers.txt:206>) read the actual demons_agreement and sealed_tunnel_reopened producer names. | Civilian/military classification, distinct cause/evidence treatment, foreign intervention history and the remaining achievement routes stay open. |
| All That Glitters portfolio and cap equality | Earlier fourth-unsafe-mine and strict-cap-window findings are superseded | [ACH-E:257](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_achievement_effects.txt:257>) and [ACH-T:131](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_achievement_triggers.txt:131>) require safe count to equal all controlled registered mines. Both reject totals only above the existing caps, permitting equality. | The source count/window agreement is repaired. Actual registry integrity, historical disqualifiers and sustained 180-day acceptance still require validation. |
| Pressure reward and transfer-resistant cadence | Earlier negative pressure-reward formula is superseded | [CORE:878](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:878>) adds the pressure gain before contribution multiplication. [MAINT:40](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_maintenance_effects.txt:40>) admits operating-mine pressure/collapse growth only after its persistent state review date plus the existing 30-day interval. | Source now expresses positive reward with bounded growth. No measured incentive, cap, timing or transfer-abuse signoff. |
| Gold and supernatural pre-entry exposure | Earlier absent pre-entry producer claim is superseded | [EXPOSURE:11](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_exposure_effects.txt:11>) adds ordinary/high-pressure/commodity/guard/theft Gold exposure before recording, permits managed reduction, and supplies supernatural signs under the III toggle/world-end gates. [MAINT:35](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_maintenance_effects.txt:35>) calls it through the bounded registry. | The source has a pre-entry growth path and persistent date guard. Actual evolution entry, timing, toggles and subsequent Gold movement/containment remain unverified. |
| Repeated deepening and III entry/reveal | Earlier one-use +15 depth P0 is superseded | [DEC:1611](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/decisions/029_riches_found_decisions.txt:1611>) permits bounded repeat projects while operating, below depth cap and without an active project. It applies +15 depth and -20 integrity at completion with actor checks/refund. [CORE:883](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:883>) applies the 0.75 output factor during the project. [TRIG:681](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_triggers.txt:681>) includes the investigated prefire path, and [CORE:2485](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:2485>) produces confirmed/crisis state at III entry. | The missing producer/one-shot obstruction is removed. Natural campaign reachability with competing collapse, repeated-contact pacing and all supernatural response routes are not certified. |
| Account Close containment and obligations | Earlier absent containment/work integration is superseded | [DEC:7876](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/decisions/029_riches_found_decisions.txt:7876>) records a paid native close response and rechecks controller/choice before [ACCOUNT:217](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_account_effects.txt:217>). Extraction/rewards stop, existing evacuation is conditionally preserved, and sealing occurs when access is valid. [ACCOUNT:280](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_account_effects.txt:280>) retains a due unpaid obligation during pending containment and clears it at terminal sealing or successful binding. | Evacuation completion and breach-until-seal outcome execution remain unverified. Immediate sealing uses general terminal cleanup, so conditional preservation at the containment helper is not proof an unfinished evacuation mission completes. |
| Bound Terms upper workings | Earlier absent assisted upper-workings endpoint is superseded | [TRIG:793](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_triggers/029_riches_found_triggers.txt:793>) requires completed assistance, sealing access/security, adequate order and supernatural pressure below 85. [DEC:8031](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/decisions/029_riches_found_decisions.txt:8031>) records and rechecks its paid actor/choice. [ACCOUNT:248](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_account_effects.txt:248>) clears live obligations, sets supernatural pressure to zero, raises integrity to at least 60, caps pressure at 60 and selects partial-sealed supervised operation. | Reduced output uses the current conditional-output contract. Full payment/late callback, breach, actor transfer and achievement acceptance remain open. |
| Resolution receipts and actual resolved classification | Specified missing resolution receipts/classification are superseded | [ACCOUNT:195](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_account_effects.txt:195>) owns actor/response receipts and guarded stale cleanup. [CORE:1229](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:1229>) clears pending payment/resolution state through the existing transfer cleanup. [STAGE:43](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_aggregate_stage_effects.txt:43>) and [STAGE:98](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_aggregate_stage_effects.txt:98>) use account_closure_finalized rather than mere refusal to classify a resolved account. | Exact resources are refunded on stale close/bind responses in the reviewed decision bodies. No native receipt execution or current seven-achievement completion proof. |
| Terminal verification ID and date | Prior source repair reconfirmed | [VERIFY:13](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/events/029_riches_found_verification.txt:13>) remains the only .907 definition in the owned event files. [CORE:2116](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_effects/029_riches_found_effects.txt:2116>) queues the regular state target once after seal, and the narrow controller-change branch retains its due date. [EVENT:376](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/events/029_riches_found.txt:376>) remains .906 evacuation. | No new evolution or asset was introduced. Native delivery and terminal achievement-window results remain unresolved. |
| Account player-facing status and five promises | Earlier absent account prose/status surface is superseded | [ACCOUNT-LOC:10](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/scripted_localisation/029_riches_found_account_localisation.txt:10>) dispatches pending/bound/containing/defaulted/exhausted/live status, named families and deadline bands. [LOC:47](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/localisation/english/029_riches_found_l_english.yml:47>) attaches it to the ordinary category, [LOC:163](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/localisation/english/029_riches_found_l_english.yml:163>) provides those strings, and [DEC-LOC:114](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/localisation/english/029_riches_found_decisions_l_english.yml:114>) describes close/bind/payment consequences. | Reviewed text does not display helper IDs or raw supernatural/dependence pressure. Whole-event key coverage, prose/style, native layout, source-consumer values and live disclosure review are not complete. |

### What remains open after this supersession

The earlier P0 fix-list items 1 and 2 no longer describe missing producer paths or the circular/closed-flag contracts at this checkpoint.
Item 3 is superseded for the canonical payroll receipt, threshold-based actual mass-death hook and specified agreement/reopened-tunnel aliases, while full damage, accountability, intervention and achievement history remains partial.
Item 4 is superseded for account Close/Bind source endpoints, actor-resolution receipts and named promise/status prose, with route execution and the remaining account/achievement acceptance still unresolved.
The AI selected-mine bypass is repaired, but bespoke decision/policy/foreign/crisis priorities are still outstanding.
No numerical ordering, probability, timing, balance or AI campaign result is supplied by this docs update.

Outstanding parent work remains concrete physical costs and commitments, dynamic cost quotes, actual transport/building/repair consumers, baseline phase/mission/concession behavior, Gold movement and sustained containment, remaining historical achievement contracts, Event Log actor/preview/global-pair N/A wiring, authoritative XLSX/catalog alignment, unfinished parent asset acceptance, bespoke AI and final engine/MCP proof.
These remain accepted obligations rather than an invitation to expand the event or substitute an improvement plan.
Their earlier source evidence is retained as historical evidence until their owners record a newer disposition.
The current table does not imply that those unrelated surfaces were re-audited or found unchanged.

The possible native political-power storage boundary of 2,000 remains parent-reported research uncertainty.
No hook behavior, actual clamp/lost grant, 1,000-PP truncation or cap fix is asserted here.
The exact one-time 1,000-PP design is retained, and its actual engine behavior stays an open validation question.
The report introduces no gameplay cap or fallback.

Read-only verification consisted of exact producer/consumer/body reads in the named Event029 files, source ID checks and source identity capture.
The account status surface was checked for its actual category and decision text linkage rather than inferred from helper existence.
The existing .907 source and owned ID uniqueness were reconfirmed.
No passing mechanical count or source hash is substituted for the missing scenario and engine evidence.
Previous MCP partial results, timeouts, client terminations, fixture failures and comparison limits remain intact.
Per parent direction, no new tool-domain requests were initiated to replace them.

### Source identities for this fresh checkpoint

Paths use the report's existing CORE/INC/HARM/MAINT/STAGE/TRIG/DEC/ACH/LOC/VERIFY keys.
EXPOSURE is `common\\scripted_effects\\029_riches_found_exposure_effects.txt`.
ACCOUNT-LOC is `common\\scripted_localisation\\029_riches_found_account_localisation.txt`.
These hashes bind the read-only checkpoint and do not freeze ongoing parent edits.

| Source | SHA-256 |
| --- | --- |
| CORE | `CEFC4912FEF7528FB83A6967FD2CE49997AF633F3E651A69DAA9F7C7B1964451` |
| EXPOSURE | `F63673E1A5FFC7A78A67752BE86F59DE0D1ACCE3307A3EE3D62B67897A5627D2` |
| MAINT | `77141C5F31404B83B37F6E07DF1616022D15D07DAF59A30B1CB0E03026F9C1D0` |
| ACCOUNT | `6118906EC832AB34CF8B1A243CA0BC1ED203E76D5098DDA95BDF233A9992759D` |
| STAGE | `1D549B978469A503E5EFE352A2A82E4A804E33222A1FABA89BB73651366F0A54` |
| INC | `56317B35DB83231099B7229DBF110B5A9A1545F9C12D2606951D8B19DEF71369` |
| HARM | `48D9E50AA13359619C62B3C89EE0A183F6114E4CE68A00DD2B39C6DBB8AA39DB` |
| ACH-E | `64A63320DA1E4A22707C36A3518D0302118372F2F25A5BAC405F88EE4D8D7C09` |
| TRIG | `0584BD7297EAC88FB98F2B4E0B317CE4A410306D86483DB6653562944A6324CD` |
| ACH-T | `E2020F19CF356A8A7710E2730B0FCD22FC7E89EA66A66661D2935A37D5D72614` |
| DEC | `5CB3798D0DD3C76D41E3BE99EB23EDCCD88D62D140127BB0D5AB143578A6E7C3` |
| ACCOUNT-LOC | `F20E94924EDE6142D226904710685D49F1D429C972482876D3E20AF52AF4BC5B` |
| LOC | `FF19645CAC65CD2BBB3C41C5F01012D881DF30021D3CAC2E226BBDDC8837325F` |
| Decision English localisation | `B5E618E6049E298676E6A3A012381DEBC44BB1155150980FD42C3A23D8559CB8` |
| VERIFY | `428B61979A1AEF41489C7E40B8A5CF79979B3DD97731C3880F89E1CC9BD36FFD` |

Skills reused: chaos-redux-events, chaos-redux-decisions-missions and chaos-redux-subagents for source evidence, ownership and disposition boundaries.
No skill, spec acceptance, asset requirement or gameplay design was changed.

## Historical checkpoint sections

The following tables and priorities preserve the earlier source observations.
For the repaired contracts listed above, the fresh checkpoint supersedes their current-status interpretation.

## Verdict by surface

| Surface | Current status | Completion limit |
| --- | --- | --- |
| Canonical root, uniform recipient preparation, one state, 1,000 PP receipt, 64-entry registry | Finished source tranche, validation blocked | Current preparation resets readiness and preserves an idempotent state grant. Suitable-state and opening variability remain partial. No successful final event inspect/render/compare. |
| Event 018 and biological-system separation | Finished source boundary | Event 018 markers are exclusions, with no owned resource/cave/Oth-Kesh/outbreak implementation. This is source evidence only. |
| Controller contribution, diminishing returns, one capped DM, seven presentation ideas, severity priority | Finished source repair, broader economics partial | Maintenance and stage migration are integrated. Occupation economics, partial output, pressure reward, active-state recovery, and meaningful balance proof remain open. |
| Controller transfer and occupation | Partial, blocked route semantics | Bounded hooks exist, but occupation detection cannot initialize itself, and historical achievement/transaction receipts do not fully follow actor changes. |
| Ordinary claims, rush, development, revenue, concession, raid routes | Partial | Definitions exist. Physical construction/capacity, route proof, settlement progression, compatible contract extensions, and several consequence consumers are missing. |
| Decision costs and staged transactions | Partial | Inclusive gate/debit repair and current display repair are source-present. Factory/unit commitments, dynamic quotes, staged ownership receipts, and meaningful scenarios remain incomplete. |
| Exact cost and outcome contracts | Design gaps in the implementation contract | The parent must instantiate accepted factory/unit commitments within four costs, actual route/asset damage, sustained reform, and visible account promises. A flat stockpile recipe, marker flag or generic value delta is not a disposition of these requirements. |
| Action presentation and AI mine selection | Partial | One ordinary category is correct. Phase/evolution/crisis coexistence and AI evaluation of every mine are not established. |
| Missions, closure, collapse, recovery | Partial | Nine mission definitions exist. Recovery, fresh public projects, timed cleanup, safe reopening, and transfer-time completion are not complete. |
| Evolution I and Gilded Sovereignty | Partial | Local entry/authority/dependence/recency gates exist, but sustained reform, restoration recency, and actual enclave consequences are incomplete. |
| Evolution II | Blocked by pre-entry progression | Gold pressure lacks an ordinary path to its entry gate. Movement, sustained containment, and susceptibility recovery are missing. |
| Evolution III and Bottomless Account | Blocked by progression, partial active parent tranche | Deep excavation cannot reach the ordinary entry gate through the current one-use action. Supernatural reveal flags and account decision/obligation integration remain incomplete. |
| Seven achievements | Partial | All seven registry entries and icon aliases exist. Historical disqualifiers, controller-bound verification, every-controlled-mine proof, and route execution remain incomplete. |
| Terminal sealing verification callback | Implemented source repair, engine proof blocked | New unique `.907` callback preserves the seal verification due date, requeues only from narrow controller changes, and retains personal-route invalidation flags. It does not certify either achievement route. |
| History, Details, evolution catalog, availability | Partial | Name/text selectors and state payload exist. Root actor and three preview producers are missing, and target-pair N/A semantics are wrong. |
| Reports and category picture | Finished standalone parent review | Nine reports and one category picture have individual source/PNG/DDS review. This does not establish event consumer behavior or package completion. |
| Mission icons | Finished current visual/file-chain review with provenance limit | Nine individual rows reviewed, independent evacuation candidate accepted and wired. Original prompts for eight inherited mission sources are missing. |
| Other authorized icon families | Partial parent acceptance | Wiring/manifests and inherited binary checks are evidence, with remaining parent review and requirement-row reconciliation still open. |
| Docs and authoritative catalog | Partial and stale | Workbook row contradicts unclustered design and does not mirror current Details wording. Overview contains obsolete or unproved claims. |
| CXT extension | Finished source registration tranche | Carrier, manual application, guarded capital fixture, and no discovery PP are source-present. This fixture is not route or live acceptance evidence. |
| Required MCP and campaign evidence | Blocked | HOI4 routes appeared in the refreshed inventory. This auditor's narrow inspect/render/compare requests returned no result within bounded client waits. Existing focused/timeout/invalid-scenario evidence is retained below, not replaced by source review. |

No whole-event completion or numerical balance signoff is granted.
The accepted absence of a dedicated GUI, focus tree, country/formable package, portraits, flags, animation, custom units, 3D models, unit audio/counters, super-events, and terminal scenario does not create a missing-surface requirement.
Do not route the shared Event Log or Details to `chaosx_event_ui_worker`.

## Evidence key

All paths resolve under `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux` unless marked installed vanilla.

| Key | Exact current source |
| --- | --- |
| CORE | `common\scripted_effects\029_riches_found_effects.txt` |
| INC | `common\scripted_effects\029_riches_found_incident_effects.txt` |
| LATE | `common\scripted_effects\029_riches_found_late_outcome_effects.txt` |
| ACCOUNT | `common\scripted_effects\029_riches_found_account_effects.txt` |
| MAINT | `common\scripted_effects\029_riches_found_maintenance_effects.txt` |
| STAGE | `common\scripted_effects\029_riches_found_aggregate_stage_effects.txt` |
| TRIG | `common\scripted_triggers\029_riches_found_triggers.txt` |
| DEC | `common\decisions\029_riches_found_decisions.txt` |
| COST | `common\scripted_triggers\029_riches_found_cost_triggers.txt` |
| CONST | `common\script_constants\029_riches_found_constants.txt` |
| EVENT | `events\029_riches_found.txt` |
| VERIFY | `events\029_riches_found_verification.txt` |
| ACH-E / ACH-T | `common\scripted_effects\029_riches_found_achievement_effects.txt` / `common\scripted_triggers\029_riches_found_achievement_triggers.txt` |
| HARM | `common\scripted_effects\029_riches_found_harm_effects.txt` |
| LOC / SLOC | `localisation\english\029_riches_found_l_english.yml` / `common\scripted_localisation\029_riches_found_scripted_localisation.txt` |
| LOG / LOGLOC | `common\scripted_effects\chaosx_events_log_effects.txt` / `common\scripted_localisation\chaosx_scripted_localisation_events_log.txt` |

## Acceptance criterion to source and current status

The acceptance file and Parts 1-6, AI scenario file, asset/achievement/decision/coding/goal prompts, catalog alignment, research notes, source review manifest, and README were read as the accepted requirement set.
Historical planning-environment claims establish neither current source inspection nor design approval.

| Accepted criterion or scenario | Concrete source identifier and evidence | Status and exact gap |
| --- | --- | --- |
| Minor Repeatable, uniform ordinary recipient, exactly one new state | `riches_found_prepare_random_event_fire`, CORE:93, adds each eligible country once, uses `random_scope_in_array`, then preferred/broad state branches. `chaosx_logic_effects.txt:294` registers repeatable ID. | Source-present. No recipient weight by size, ideology, player, or mine count. Final pool and engine scenario proof blocked. |
| Exact one-time 1,000 PP and durable mine | `riches_found_commit_discovery`, CORE:164-189, state `riches_found_discovery_grant_paid`, CONST `discovery_political_power = 1000`, `riches_found_bind_history_sequence`. | Source-present. One grant after registration, no transfer grant. Engine cap/loss and repeat firing tests not performed. |
| Empty pool cannot reuse stale preparation | CORE `riches_found_prefire_ready`, `riches_found_save_prefire_state`, `riches_found_expire_discovery_receipt`, EVENT `.899`, root `.1` receipt/target rechecks. | Current source repair present. Shared selection, actor/log, and direct invocation still need matched scenarios. |
| Suitable populated/buildable/access-connected state | TRIG:61-103 and CORE `riches_found_prepare_selected_discovery_country`. | Partial. Broad gate can admit a coastal mainland state solely through `is_coastal`, without population/building-slot/port proof. Preferred versus broad branches are not complete geography/ruin/reserved-site coverage. |
| Dynamic opening and surveyed quality | CORE `riches_found_initialize_mine_record`, lines 257-281, CONST `public_initial_*` and four commodity quality factors. | Simplified implementation. Public starting values are fixed, apart from later option/prefire deltas. No low-stability/core/industry/supply/resistance opening adjustment or separate rare surveyed quality band was found. Commodity type is being used as quality. |
| Event 018 exclusion only, no resources/caves/Oth-Kesh/outbreak | TRIG `riches_found_state_is_excluded_target`, INC/HARM headers and owned helper calls. | Source boundary satisfied. No requirement to add Event 018, outbreak, unit, or 3D content. |
| Bounded transfer with local history preserved | CORE `riches_found_handle_state_control_change`, `riches_found_handle_owner_change`, `riches_found_handle_removed_actor`, owned on-actions. | Source skeleton present. Exact occupation semantics, delayed transactions, release/civil-war/recapture and old-controller cleanup still fail or lack proof. |
| Occupation route and reduced output | TRIG `riches_found_mine_is_occupied` at 538 requires `riches_found_occupation_active`. CORE `riches_found_handle_occupation_change` at 1948 calls that predicate before setting the flag. | Broken first occupation transition. An unflagged conquered mine never initializes occupation, so DEC `occupation_*` phase actions remain hidden. Contribution applies 0.65 for owner/controller mismatch but not core/compliance/resistance/supply factors. |
| One bounded aggregate, diminishing returns, one severity stage | CORE `riches_found_rebuild_controller_aggregate` at 949, STAGE collector/applier, modifier-free seven ideas, `riches_found_controller_aggregate`. | Current tranche implemented at source level. Stage collection occurs outside output arithmetic and terms apply once before caps. Combined runtime/balance and tooltip proof missing. |
| Pressure raises current reward with risk | CORE contribution at 878-882, CONST `pressure_factor_floor = 1.00`, slope `0.003`. | Contradictory incentive. Increasing pressure lowers this factor. A predatory policy multiplier does not implement the accepted pressure-dependent marginal reward. Account reward factor is new and separately conditional. |
| Partial sealing/controlled quarantine preserve reduced output | TRIG `riches_found_mine_provides_controller_output`, CORE `riches_found_reconcile_mine_phase` at 624-638. | Broken conditional output. Presentation sets `riches_found_mine_closed` for quarantine/partial seal, while both `state_can_control_access` and conditional output reject that flag. New reduced-output branches remain unreachable after refresh. |
| Claims policy, survey, register/court success/partial/failure | DEC `survey`, `claim_register`, `claim_freeze`, `recognize_local_claims`, `reserve_deposit`, `claims_court`, mission `secure_rush`; INC claims pool. | Partial. Source choices and incidents exist. Claim-policy compatibility, timed acceptance/refund, and real post-start objectives remain open. |
| Rush local/specialist labor and services change play | DEC `camp_administration`, `license_traders`, `local_labor`, `specialist_labor`, `worker_cooperatives`, `sanitation`; INC rush pool. | Partial. Different value/flag outcomes exist, but capacity commitments and reduced receipt costs are absent, and the uniform source cost bands do not implement dynamic country/state burden. |
| Real transport/settlement/processing/public projects | DEC `rail_spur:1077`, `port_route:1162`, `processing_works:1340`, `housing:1434`, `development_fund:1529`, mission `open_railhead:8440`. | Missing physical implementation. Rail/port completion sets route flags and development. Owned sources contain no `build_railway`, `add_building_construction`, `set_building_level`, or equivalent exact physical project adapter. No named route-state ledger or exact map path proof. |
| Development fund supports later bounded projects | DEC `development_fund`, `stabilization_fund:1968`, `curse_stabilization_diversification:5566`, CORE mission starter. | Partial and potentially stranded. Public-settlement start clears `public_project_complete`. Physical actions require phase development, but fund/revenue results advance beyond it. No preserved future project family for a revenue-phase stabilization/diversification mission was demonstrated. |
| Dividend/local share/central receipts/participation/fund/patronage are lasting tradeoffs | DEC `dividend:1704`, `local_revenue:1794`, `central_revenue:1884`, `stabilization_fund`, `tolerate_patronage:2309`. | Simplified. Mostly one-time public-value/flag changes. Contribution does not read dividend/local share/fund receipt allocation or bounded reserve expenditure. No repair withdrawal or staged diversification benefit was found. |
| Three to five ordinary actions, maximum six, emergencies replace obsolete actions | CORE phase reconciliation, DEC visible predicates, TRIG policy concession menu. | Partial. Physical phase can expose six primary actions in a coastal deep mine with a port route, no rail, high development, reinforcement unfinished, no housing/processing/fund/deepening. No full phase 3-5 or combined crisis/evolution scenario proof. Security markers can jump straight to phase 6 and monotonically strand unfinished physical/revenue content. |
| Human selected mine, AI evaluates every valid mine independently | TRIG `riches_found_state_is_active_selected_or_only_mine:170`, DEC `select_mine:8298`. | Missing AI bypass. All action target predicates require the country selection pointer, including AI. The selector has a nonzero AI weight. There is no close/return selection action, and old `selected_target` flags are not cleared by selecting another mine. |
| Bounded player choice of plausible foreign partner | INC `riches_found_prepare_scored_foreign_partner:301`, TRIG `riches_found_foreign_target_is_valid:571`. | Maritime eligibility repaired. Still one cached deterministic highest-score partner, without an ordinary selected-foreign-actor choice list. Hostile-at-peace neighbors/faction members remain eligible and the score floor is positive. Missing strategic commodity/rival/exclusive-conflict/access-interest coverage remains with ProbabilityAudit. |
| Compatible limited contracts, one exclusive, disclosure/renewal/end/transfer | CORE `begin_contract`, `extend_limited_contract`, `review_contract`, `renew_contract`, `expire_contract`, DEC contract family. | Partial. Exclusive guard and lifecycle clocks repaired. Signing sets concession/offtake flags that advance phase 6, while new/amending `offtake`, `trade_access_infrastructure`, and auction actions require phase 5. Compatible extensions become inaccessible. Disclosure is offered after a live concession, not before award. |
| Nationalization/buyout and sponsor reactions | DEC `nationalize_with_compensation:3029`, `nationalize_without_compensation:3128`, `buyout:3223`, INC foreign/contract pools. | Partial. Value/contract changes exist. No compensation claim transaction/settlement consumer, sponsor acceptance branch, or actual sanction/intervention behavior demonstrated. `riches_found_nationalized_without_compensation` is read for sanctions but has no Event029 producer. |
| Distinct security with supplied units and commitments | DEC police/guards/cordon/workers/pay/truce/disarm, TRIG `state_has_supplied_force:341`. | Partial. Presence predicate is route capacity plus divisions in mine state, not verified unit supply or route-state continuity. No actual unit reservation and several cost substitutions recorded by DecisionAudit. |
| Concrete raid target changes the corresponding asset | INC `select_raid_actor`, `select_raid_target`, `apply_raid_consequence:534`. | Targets exist but consequences are largely common order/development deltas. Transport damage flags do not invalidate route predicates, repair lacks a named asset restoration ledger, and private/foreign actors do not receive verified accountability/response state. |
| No successful pay robbery during achievement sequence | INC:568 writes `riches_found_pay_robbery_succeeded`; CORE progress and DEC mission read `riches_found_raid_robbery_succeeded`; ACH-T reads `riches_found_pay_train_robbery_succeeded`. | Broken receipt contract. Neither consumed robbery flag is produced, and the actual produced flag has no owned gameplay reader. No sequence reset on that real robbery, temporary closure, or transfer was found. |
| Temporary closure lowers pressure through time, meaningful reopening | CORE `begin_temporary_closure:2015`, `closure_review_date`, `complete_recovery:2151`, MAINT. | Missing timed closure lifecycle. Helper adds pressure +8 and stores an unread review date. The decision adds a separate immediate pressure reduction, but no recurring closure reduction/maintenance-decay/worker-support lifecycle. Recovery review and collapse recovery dates also lack enforcing readers. |
| Partial sealing reduces deep risk | CORE `begin_partial_seal:2035`, CONST `partial_seal_integrity_loss = -25`, TRIG III gate integrity below 40. | Wrong-direction safety term. Sealing reduces integrity, moving toward the supernatural low-integrity gate. The decision's separate depth/pressure reductions do not establish the required durable safer upper-working state. |
| Minor/severe/catastrophic collapse, recover or terminal destruction | INC collapse pool:588, CORE `collapse_mine`, `refresh_active_mission_progress`, DEC `restore_shaft:8763`. | Partial. Catastrophic random outcome sets collapsed/severe flags but no terminal destruction, exact building damage, or exhaustion endpoint. Restoration rejects `severe_collapse`, with no clearing recovery route. Regular repair does not call `begin_recovery`/`complete_recovery` to reopen. |
| All mission outcomes are distinct, fresh, nonduplicating and controller-safe | CORE mission helpers, DEC nine mission blocks at 8336 onward. | Source success/partial/failure branches and country slot cap exist. Seventeen staged paid transactions remain unguarded by the coordinated ownership/refund contract. Railhead can complete from timed route flags/capacity, public settlement can be stranded, and exact native timer synchronization/continuity is unproved. |
| Last Shift and Close Account verification survives terminal maintenance stopping | CORE `permanently_seal_mine:2071-2111`, `handle_state_control_change:2239-2251`, VERIFY `.907:13-33`. | Source repair present. Seal first refreshes timers, queues one callback under a pending flag for the larger verification interval, and transfer reuses the same due date with remaining delay floored to one day. Callback clears pending before rechecking state and current-controller achievement windows. No native callback delivery, continuous-window, or achievement-unlock proof. |
| Exactly three evolutions at 600/800/1000, individually enabled, real records | CONST type 29/stages 1-3/tiers 3-5, TRIG enabled/gates, EVENT `.901-.905`, CORE `record_evolution_entry`. | Correct source identities and no fourth/fifth logging. Lifecycle and progression coverage incomplete. Delays are computed once and clamped 45-240, without proof of sustained gates or effective starvation under management. |
| Gold Disease can enter after ordinary exposure | CORE initial Gold pressure 0, prefire adds 15. TRIG II gate requires 60. Positive Gold incident deltas occur only in INC Gold pool already gated by recorded evolution. | Source reachability blocker. No ordinary pre-entry growth to 60 was found. High pressure/theft/private guards alone cannot bootstrap the accepted entry route. |
| Gold movement and sustained containment/recovery | DEC `gold_*`, INC Gold pool:632, STAGE active Gold predicate. | Missing destination-linked worker/shipment/guard/sponsor movement and temporary destination effects. No multi-step completed-containment receipt, active-state clearing or lasting susceptibility lifecycle. Closure still permits active-mine incident review. |
| Demons can enter after repeated deepening/contact | CORE initial depth 0, DEC `drive_deeper` adds 15 once and hides when `deep_excavation_authorized`; TRIG III requires depth 60. | Source reachability blocker. No other positive owned depth producer reaches the requirement. Prefire adds supernatural pressure but no required depth. Safety, violence, and policy thresholds cannot substitute for the missing path. |
| Supernatural reveal and response eligibility | DEC agreement requires `riches_found_supernatural_confirmed`, evacuation/sealing reads `supernatural_crisis`, other actions read signs/occult network. | Unhandled gates. No Event029 producer of confirmed/signs/crisis was found. Recorded evolution is a different flag. Agreement is inaccessible even if III is forced into existence. |
| Gilded local dominance, actual dependence, recent successful reform | TRIG Gilded gate:704, LATE receipt/authority/date helpers, CORE aggregate and public-settlement success. | Parent metric tranche present. Receipt temporary lifetime/getter timing and sampled continuity remain unproved. Gilded restoration achievement hook does not publish the new successful-reform date. STAGE treats diversification start as reformed despite no sustained success. |
| Full Gilded responses and meaningful authority/transfer aftermath | DEC revoke/buy/share/board/violent/let-govern at 7327-7851, CORE Gilded entry. | Partial. Responses set flags/value deltas. No explicit national law/labor/diplomacy constraint, authority access control, foreign protection/intervention endpoint, or retained old-country dependence aftermath was demonstrated. |
| Bottomless agreement and repeat-after-contact entry | TRIG account gate:718, new ACCOUNT `accept_account_terms`, DEC agreement/controlled exploitation, LATE post-contact depth difference. | Parent now wired acceptance in both decision outcomes. Post-contact difference producer now exists. The ordinary positive depth path remains one-use and cannot demonstrate repeated excavation after contact. Revealed-contact and sustained-dependence path acceptance remains open. |
| One live obligation, five payment families, rewards/breach/transfer/closure | ACCOUNT helpers/constant groups/payable triggers, MAINT service call, CORE late entry and output factor, DEC material/authority/predatory family outcomes. | At 15:53, all three payment actions call fulfillment, with controller/choice/pending-obligation rechecks. Authority branches between authority and trust, predatory branches between industrial loss and human harm. This supersedes the earlier absent-call finding. Full record/quote/refund/closure/breach/transfer/UI evidence still needs a fresh integration audit and same-scenario validation. |
| No unrelated-death payment or unlimited human harm | HARM finite `predatory_prosperity` receipt, ACCOUNT family structure, TRIG high-chaos human gate. | Source isolation preserved, but no completed matching acceptance/payment path. Do not certify a no-farming route from isolated helper presence. |
| Exact classified deaths and public-responsibility evidence | HARM `apply_harm_record`, collapse/raid/Gold/supernatural wrappers. | Exact civilian-loss API and some once/sequence guards exist. All causes use `resource_field_incident`, no distinct Event029 reason or military classification. All positive harm is attributed publicly to controller, without the requested evidence/actor distinction. Nonfatal coverup/blocked inspection/record destruction have no full Condemnation consumer. |
| Meaningful Chaos outcomes and no duplicate death source | INC/CORE/HARM and owner constants. | Missing explicit accepted claim-war/major-raid/managed-settlement/bargain milestone and reversal integration. Existing shared deaths/Condemnation must remain separate from any owner premium. No numeric balance claim. |
| History actor, correct state, three preview rows | LOG default actor initializes 0, with no Event029 branch; shared handlers call recorder before `.1`; CORE has no actor override. LOG:790 binds state payload, but preview rebuild has no Event029 row producer. | Missing actor/flag and all three catalog-preview producers. Existing LOGLOC titles/bodies/icons do not create preview rows. Actual evolution history recorder is separate and source-present. |
| Details N/A for global country/state availability | LOGLOC:366-372 tests the UI country's `riches_found_is_eligible_discovery_country`. Shared `evaluate_event_pool_candidate_unavailability` has no Event029 branch. | Wrong target-pair surface. An ineligible viewer can see N/A despite another valid recipient, and an empty world pool does not invalidate canonical Event029 live weight before preparation. Missing history state falls back to generic description rather than a demonstrated pair-status contract. |
| Authoritative catalog mirrors Details, no clusters, approved status | XLSX `Events!A30:M30`, ID29, Type Minor Repeatable, Chaos level1, Cluster ID `7, 15`, Status `Needs Testing`. LOC Details/evolution bodies. | Stale/contradictory. Cluster must be blank under accepted design. Details prose differs from LOC:115 and the row advertises N/A as proven. Workbook status/readiness and export reconciliation need owner disposition. CSVs were not used as authority or edited. |

## Achievement-specific historical gaps

Registry evidence: `common\achievements\chaos_redux_achievements.txt:4300-4377` contains all seven IDs.
Tracking and icon registration prove source presence, not completion of the seven campaigns.

| Achievement | Existing exact predicate/receipt | Remaining failure or validation gap |
| --- | --- | --- |
| `029_public_fortune` | ACH-T `public_fortune_route`, ACH-E public two-year window, original discoverer, mature/public-project/exclusive/curse checks | Public projects have the progression gap above. Harm publishes `mass_death_occurred` but does not call the achievement mass-death recorder. Continuous values are sampled, and duplicate-safe is initialized rather than proved by reconciliation. |
| `029_claim_jumper` | ACH-T transfer route, ACH-E one-year deadline, CORE transfer history | Deadline and settlement/repair flags are state-held without a verification-controller binding/reset on B-to-C transfer. A later controller can inherit an earlier controller's timer and recovery action. Existing completed-action history is not proof the new holder performed it. |
| `029_the_pay_train_runs` | Per-instance counting guard, three successes, route/presence predicate | Three mismatched robbery flag names, no real sequence invalidation at robbery/transfer/temporary closure, and no continuously supplied named route proof. |
| `029_all_that_glitters` | Bounded safe-mine count, cap variables, 180-day window | It checks at least three safe mines rather than equality between safe count and every controlled registered/operating mine. A fourth unhealthy mine can escape the count proof. Forbidden-evolution/invalidated country flags lack owned producers. Window uses strict-below-cap while final predicate permits equality. |
| `029_no_man_owns_the_mountain` | Gilded history/reform/legitimacy/open-mine window | Foreign military intervention has only unused owner marking hooks, not an actual detection/response path. Non-destructive access restoration and actor-bound hold are not fully represented. Gilded share/let-govern and restoration need accepted end-state distinction. |
| `029_close_the_account` | Account history, closure-controller, low-death or evacuation, final seal/bound closure, stability/date | Normal account entry and typed payments are incomplete. Breach-imminent reader is not produced by the new breach dispatcher. Closure must end supernatural rewards/obligations, with catastrophic/default history carried into permanent disqualification. |
| `029_the_last_shift` | Dedicated evacuation/assistance/seal, controller and invalidation receipts | Reveal/evacuation gates lack producers. Reopening incident sets `sealed_tunnel_reopened`, but disqualifier reads `demons_reopened_after_seal`. `demons_make_agreement` reader differs from actual `demons_agreement` writer. Positive supernatural state and post-seal verification are not fully closed. |

The mass-death and foreign-intervention hook wrappers are not invoked by the reviewed harm/raid/foreign transaction paths.
No amount of icon, registry, or final-state coverage can substitute for these historical receipts.

## Prioritized owner fix list

1. **P0, evolution reachability:** provide the accepted ordinary pre-entry exposure and repeated/deep-excavation paths for Gold Disease and Demons.
   Preserve paced local entry and toggles, with a real producer for each gate input.
2. **P0, occupation and partial output:** break the circular occupation predicate and reconcile closure/partial/quarantine flags with actual access/output predicates.
   Validate A-to-B occupation, recapture, closed-only maintenance, and conditional upper-workings output.
3. **P0, receipts and unhandled gates:** reconcile payroll robbery producer/readers, supernatural signs/confirmation/crisis, actual mine damage/route invalidation, and achievement death/intervention history.
   Do not merely rename prose or seed flags to manufacture a scenario.
4. **P0, active account tranche:** review the now-wired acceptance and payment call sites with all five family consequences, typed benefit/breach history, closure and transfer, and visible obligation text.
   The new helper and payment calls supersede the earlier missing-call observation, without supplying final acceptance evidence.
   Account Close still needs actual containment initiation with breach exposure retained until sealing, and Terms Bound needs the accepted controlled upper-workings endpoint and its prose/UI.
5. **P1, recovery:** implement timed pressure reduction and reopening requirements, repair/recovery completion, severe/catastrophic disposition, meaningful damaged assets, and successful evacuation callback recovery.
   `.906` can fail its route/slot/control trigger once and leave preparation pending, with no explicit requeue/refund path.
6. **P1, settlement and phase sequencing:** preserve playable public projects/revenue sharing after mission start and prevent security/concession flags from abandoning unfinished accepted baseline actions.
   Keep one category and the accepted action/mission budget.
7. **P1, costs:** complete actual factory and unit commitments and dynamic same-quote display/availability/payment/refund.
   The four-cost maximum does not authorize dropping an accepted physical cost.
8. **P1, staged transactions:** close the 17 mission/event-backed delayed transactions listed in DecisionAudit with actor/state/instance receipts, stale resolution and coherent refunds.
   The other 75 guards also need terminal/route/instance checks where remaining control alone would allow a stale success after sealing or collapse.
9. **P1, contract and foreign choice:** keep compatible amendments reachable after signing, provide the accepted ordinary foreign target choice, reject hostile cooperative offers, and implement meaningful compensation/pressure/security-right outcomes.
10. **P1, controller economics/reform:** implement pressure reward and current active-state recovery, retained reserve/diversification/revenue tradeoffs, core/compliance/resistance/supply factors, and restoration recency.
    Complete the receipt allocator's explicit temporary-lifetime contract and preserve one capped aggregate.
11. **P1, achievements:** audit every row above with invalidation history and current verification actor.
    Replace unconditional duplicate-safe assumptions with the owning reconciliation proof, and require all controlled mines in the portfolio condition.
12. **P1, log/Details:** add Event029 actor preparation before history recording, three preview rows, and one non-mutating global valid-pair availability contract used by selection/list/Details.
    Keep current receipt preparation out of UI status refresh.
13. **P1, specialized AI and probability:** retain the existing ProbabilityAudit owner, obtain accepted fixtures, then review every option/decision/MTTH/incident/target/recipient surface under the full named scenarios.
    Shared major/war/mine-priority multipliers are not bespoke action plans, and several modifier flags have no producer.
14. **P2, assets and documentation:** finish parent review and row-level requirement/consumer evidence for the remaining icon families, retain missing prompt limits, reconcile current overview/handoffs and all workbook fields through their owners, then regenerate CSVs from XLSX.
    Retain the active asset workspace until actual package completion and durable evidence promotion.
15. **Completion gate:** reconcile final source identities with mandatory MCP event inspect/render/compare, probability inspect/evaluate/sweep/compare, relevant exact-route map proof and required specialist audits.
    The parent already has narrow retries running, so this auditor did not duplicate broad or identical calls.

## Asset and documentation acceptance

The parent explicitly placed 107 assets in scope.
That authorization is the inventory boundary, not a count-based completion test.

| Requirement family | Exact evidence/consumer | Current disposition |
| --- | --- | --- |
| Discovery/rush/concession/raid/collapse/Gold/depths/Gilded/account reports | `2026_10_03_parent_report_art_review.md`, `notes\validation_report.json`, `interface\029_riches_found.gfx`, corresponding EVENT pictures | Implemented standalone source/PNG/DDS parent review. Resource Curse currently uses the rush report, so do not invent an extra report requirement. |
| One static category picture | Same parent report, `decision_cat_picture_riches_found`, category `riches_found_mine_management` | Parent accepted 114x101 scene and wiring. Native category/action rendering remains unproved. |
| Nine mission icons including independent evacuation | `mission_icon_retry_2026_10_03.md`, current `icon_manifest.md`, GFX mission entries | Current nine-row visual/alpha/roundtrip review. Evacuation selected source SHA `5f74115a60cff9dc5391deaf2b6a0fc88b2176d07666269867a66257fff443cd`, runtime SHA `c30eb96b9ed44838e4db5a118a61a6a49d8432400d94499e4a66709ae98df1e2`. Eight inherited initial prompts unavailable. |
| Small category icon and 46 decision-specific icons | `icon_manifest.md`, `icon_provenance.md`, current decision/GFX consumers and contact sheets | Parent review incomplete. No assumption that one manifest row or an unrelated icon satisfies another required action. |
| Nine state icons and seven controller idea icons | State DM definitions and STAGE/CORE lifecycle, GFX state/idea entries | Separate sources/wiring recorded. Final per-row parent approval and native presentation acceptance incomplete. |
| Three evolution icons | LOGLOC `GetEventsLogSelectedEvolutionPortrait`, GFX `idea_riches_found_evolution_*` | Sprite selectors exist, but missing preview producers still block actual catalog coverage. |
| Controller aggregate modifier icon | `modifier_icon_audit_handoff.md`, current 30x20 modifier consumer and GFX | Inherited family proof retained. Do not equate independent production QA with complete parent/native review. |
| Seven achievement triplets | `achievement_icon_audit_handoff.md`, current `notes\achievement_icon_audit.json`, root `gfx\achievements\029_*`, exact seven registry IDs | Production/composition/roundtrip records and parent synchronization exist. Final route/history acceptance and remaining parent review limits stay open. |

No new asset, portrait, animation, 3D/audio/counter package, GUI or fallback was produced by this audit.
Missing prompts and unfinished review remain explicit evidence gaps.
The temporary `docs\assets\029_riches_found\` workspace must remain while these blockers are open.

Documentation discrepancies requiring owner reconciliation include:

- `docs\events\029_riches_found\overview.md` claims occupation behavior, geographic/contract completeness and evolution previews without the source proof above, retains both absent and present achievement-registry statements, and still describes the maritime gate as unresolved after that repair.
- Its controller-stage paragraph describes the old staged idea model and omits the new maintenance/stage/account source inventory.
- `decision_affordability_repair_2026_10_03.md` preserves a now-stale cost-display finding.
  Current SLOC cost selectors call the shared inclusive COST predicates, including exact train/convoy tokens.
  Its factory/unit/dynamic-cost and 17 staged transaction findings remain current.
- `late_outcome_gap_2026_10_03.md` accurately identifies accepted missing account behavior at its checkpoint, but its no-obligation-source finding predates ACCOUNT.
  Its dependence lifetime, entry/decision integration, reform and validation limits remain relevant until reviewed against the new source.
- The XLSX `Events` row 30 has Cluster ID `7, 15`, rather than blank, and uses different Details/evolution prose from current runtime localisation.
  Status is `Needs Testing`, with no completed readiness evidence in this audit.
- `event_log_event_is_reworked_default_enabled` in `common\scripted_triggers\chaosx_settings_triggers.txt:26` already includes Event029 despite the accepted full-readiness gate remaining unsatisfied.
  Presence is not approval to complete the rework.

## Accepted-plan and handoff disposition

These are audit classifications for the parent to reconcile, not silent spec promotion, rejection, or redesign.

| Document/tranche | Disposition | Basis and remaining work |
| --- | --- | --- |
| Complete named specification pack | Accepted and queued for outstanding implementation | Explicit full-spec user authorization. Existing source satisfies only the rows identified above. No accepted route was rejected or omitted from this audit. |
| `maintenance_2026_10_03.md` | Implemented source integration, blocked evidence | CORE adapter, MAINT, pulse dates and registry filtering verified. Earlier Restore Shaft start gate has been repaired, but restoration outcome remains partial. |
| `aggregate_stage_2026_10_03.md` | Implemented source integration, blocked evidence | Seven identities and once-only capped terms/priority integrated. Parent still owns conditional output, active-marker lifecycle, tooltip/balance proof. |
| `2026_10_03_parent_contract_repairs.md` | Implemented bounded source repairs | Exclusive-request guard, controller-scope amendment and selection receipts present. Does not dispose of full concession/transfer acceptance. |
| `decision_affordability_repair_2026_10_03.md` | Implemented narrow tranche, partial broader acceptance | Inclusive gates, multi-mine one-shot removal and 75 guarded transactions. Current display selectors repaired later. Physical/dynamic/17 transaction obligations remain queued. |
| `localisation_cost_repair_2026_10_03.md` | Implemented scoped cost text, visual/engine validation blocked | Current shared inclusive selectors and explicit four-field cost rows follow parent direction. This does not cover non-cost localisation, account prose, category/achievement text, or all visible keys. |
| New VERIFY `.907` and terminal queue | Implemented source repair, final handoff/validation queued | Parent explicitly authorized the same bounded state callback after terminal mines stop maintenance. No new mechanics, evolution, asset or recurring scan. Exact engine delivery and achievement route proof remain open. |
| LATE and `late_outcome_gap_2026_10_03.md` | Implemented metric/gate tranche, account integration queued | Parent authority/dependence/recency instruction is acceptance basis. ACCOUNT has appeared since the architecture capture, so final facts require an integration handoff and refreshed audit. |
| `2026_10_03_achievement_registration.md` | Implemented registry tranche, historical-route acceptance unresolved | Seven registry entries and title/description aliases are present. No seven-route test/disqualifier proof. |
| Parent report art review | Implemented standalone review | User asset authority, individual parent source/PNG/DDS observations. Event behavior not certified. |
| Mission icon retry | Implemented scoped review and evacuation repair | Independent mission source and parent-selected runtime evidence. Missing inherited prompts remain recorded. |
| Remaining icon audit handoffs | Unresolved final parent acceptance | Production/roundtrip records retained. Do not promote every manifest status to event completion. |
| Historical explorer/baseline reports | Superseded for current source status, retained evidence | `2026_10_03_resume_packet.md` and newer handoffs replace old stub/2000-PP/missing-root claims. Timeout/partial evidence is not erased. |
| Probability retry and probability audits | Blocked/unresolved numerical acceptance | Named fixtures lack accepted state records, adapters misclassify targets and current calls time out. Existing ProbabilityAudit owns the retry and compare. |
| Catalog alignment | Accepted and queued | Final current wording, unclustered field, status basis and exporter reconciliation remain the workbook owner's responsibility. |

No new broad improvement addendum was created or requested.
The accepted pack already specifies the missing mechanics.
Completion must not substitute another unresolved improvement plan for implementing it.
Here, design-gap means an accepted cost or outcome has not been translated into a concrete reviewed implementation contract, not that the auditor proposes a new route or broader feature.

## Meaningful validation performed and missing

This auditor traced current target-to-receipt-to-grant, registry-to-controller, maintenance-to-callback, stage-to-cap, mission-start-to-resolution, contract-to-phase, incident-to-harm, achievement-to-history, and log/catalog consumers.
Read-only producer/reader searches were followed by exact body reads for the occupation, closure/output, deepening, Gold pressure, raid robbery, supernatural gate, public project, account, achievement and log findings.
The authoritative XLSX was opened with `openpyxl` in `read_only=True`, without saving or exporting.
Source arithmetic and reachability findings are not executed engine scenarios or probability results.

The following accepted checks remain missing: actual two-country/repeated/same-country discovery, one/two/three/four-mine economic scenarios, full phase 3-5 and combined crisis/evolution presentation, contract compatibility and controller transfers, closure/collapse/repair/sealing routes, sustained unit/route objectives, all seven achievement histories/disqualifiers, no-DLC compatibility, save/reload persistence, multiplayer ghost-copy behavior, and exact 1,000 PP actual-cap behavior.
No supplied save was inspected, and none was required or invented for this read-only assignment.
The user's earlier menu-only `docs\testing\live_qa\20261003_full_playtest\logs\cycle1\error.log` observation with no Event029 lines is retained as menu evidence only.
It is not route, callback, achievement, asset-consumer or balance proof.

Local references read directly for the relevant interpretation:

| Source | Lines and SHA-256 | What it supports |
| --- | --- | --- |
| Offline `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 284-336, `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` | Custom text does not pay costs, explicit debit and static PP hint contract. |
| Offline `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md` | 26-36, `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818` | Decision willingness versus event option mechanisms, no click-probability inference. |
| Installed `common\decisions\_documentation.md` | 1-45, `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019` | State/country target and refresh scopes. |
| Installed `common\on_actions\00_on_actions.txt` | 5074-5088, `52A751456F1774AD5001C86D41D4E46494F751D79B6C224B6CD4C0EEBB615EB9` | ROOT new controller, FROM old controller, FROM.FROM state precedent. |
| Installed `common\dynamic_modifiers\wuw_dynamic_modifiers.txt` | 1-46, `2A03BFA939115DB4C2B0720466F287927925E9E36B939C574BFB6CE3AD832DB3` | Variable modifiers, enable predicate and daily/forced refresh. |
| Installed `common\decisions\BEL.txt` | 1207-1215, `840DEB91D637FD807747AB5C5027F2152E64F2481F227D1EAD0754B98704567B` | Native custom-cost/decision-duration precedent. |

Installed paths resolve beneath `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
These narrow direct reads supplement the exact references retained in maintenance/stage/decision/architecture handoffs.
They do not establish complete engine-reference or runtime validation of all requirements.

## Mandatory MCP coverage gaps

Initial live tool inventory discovery returned no HOI4 routes.
The refreshed inventory later exposed the event, reference, source, decision, map and probability routes, plus a Native2 registry inventory tool.
The final limitation is therefore missing returned domain evidence, not ongoing tool non-exposure or a service-wide health claim.
Live event inspect/render/compare schemas were read before the narrow follow-up requests.
No raw client, local analyzer, source graph generator, invented schema, native job or GUI route was substituted.
The required workspace for any owner retry remains `mod_chaos_redux_ea3b2d67c2c0`.

| Required evidence | Exact existing artifact or failure | Coverage retained |
| --- | --- | --- |
| This auditor's `.903` inspect/render | Explicit workspace, selector `{kind:event,eventId:chaosx.nr29.903}`, depth1/node1, inspect edge1, `refresh=false`, no helper expansion, neighborhood render without HTML. Exec cell79 returned no result after approximately52 seconds of client waiting and was terminated. | No graph/render/artifact/revision returned. Client termination is not a confirmed server timeout, task cancellation or service failure. |
| This auditor's comparison attempt | Explicit same workspace/selector, chain1/render1, `render=false`, `refresh=false`, before artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2bd3d5011cacaa8c39d04b92c591db2ddf073424b9383a5fc30eb3eeca3e69c4/9f748bf105405e58f45cad56d216c4c5553d3f1bd16f6ddbaf14aaef64ff9db4/event-trace-241c8b38d5c6.json`. Exec cell80 returned no result after approximately52 seconds and was terminated. | No comparison or graph-validation result. The earlier partial trace was submitted as the known artifact, without asserting it is a valid complete graph baseline. Server-side continuation/cancellation is unknown. |
| Root event inspect | Resume packet records focused `.1` trace revision `241c8b38d5c69545f6f1b5c5a8f4e408fdb1756d28af621255ffbdf5bc8471dc`, graph hash `270095a7ecb74b0bfca0c82cbf5b9f77c65c14fc8b1a7789530e77180783dd4d`. | `complete=false`, helpers 0, deferred helper/lifecycle projections. Partial artifact read, not final lifecycle proof. |
| `.900` inspect/render | `probability_retry_2026_10_03.md` and maintenance report: explicit event selector, depth1, one node, one edge for inspect. `tool call failed`, caused by `timed out awaiting tools/call after 600s`. | No current graph/render/artifact/revision. Earlier six-node calls also timed out. Depth0 rejected as too small, not an alternative. |
| `.904/.905` late inspect | `late_outcome_gap_2026_10_03.md`: minimum valid depth1/node1/edge1 calls both returned the same 600-second timeout. | No late graph or scenario proof. New ACCOUNT bytes postdate those observations. |
| Event compare | Probability retry records no valid graph-bearing baseline/after artifact or usable cached graph. | Compare not completed. Immutable source snapshots exist, but raw source/report/render artifacts cannot be mislabeled graph evidence. |
| Probability baseline inspect | Retry artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb24a045ace9b5aa91e15e07ce7bcb955c061fd7925b06ea8924d37941f56518/3ad3e1aa8ba465630212541a59707756cb2f6ed94c256f8ccf4e6768523a0d8a/probability-inspect-0f70e76d1dd0.json`, revision `ee6db43d3e8566b2e74f54e0c5c14676faf88a985d30e734f40029a40be2fdc0`. | Retrieved 63,347 bytes and hash verified by ProbabilityAudit. One requested offtake candidate has zero decision-adapter matches and appears under mission adapter. Old-source inventory only, no ranking. |
| Evaluation/sweep/compare | Retry reports `expected record, received undefined` at `scenarioSet.scenarios[0].state` through `[4].state`, and corresponding two/seven-case compare errors. | No accepted campaign-state fixture, scenario hash, numeric delta, threshold/rank/timing result. Saved JSON ID/description list is not complete state input. |
| Current probability inspect | Current decisions, MAINT, three evolution MTTH entries and INC random-list calls timed out after 600 seconds. | No final current-source probability coverage. No analysisId for probability_render. Simulation/sequence were correctly not invented without declared distributions/transition contract. |
| Stage/reference retrieval | `aggregate_stage_2026_10_03.md`: context limit2, dynamic-modifier search, aggregate source lookup, `.900` trace and narrower five-line/wiki-only retries all timed out after 600 seconds. | Direct source/reference repair evidence only. |
| Decision scenario | DecisionAudit single survey request, explicit USA/State361 fixture, returned no artifact before cancellation at about54 seconds, following earlier timeout. | No successful decision scenario or native row image. |
| Exact map/access proof | Resume packet records generic rail lookup/pending queries, without selected-mine path/controller/supply proof. | Generic lookup is not physical project or route evidence. |

The specialized probability pass remains routed through the existing `chaosx_ai_probability_auditor`, agent `01a10108-e81d-7cc2-b58a-041ccfd61783`, and its named baseline/compare handoffs.
The complete accepted denominator is the scenario file's 39 original Surface A-L IDs plus its supplemental foreign-empty, Surface M complete incident pools, and Surface N repeat-recipient edge contract.
Every scenario lacks final accepted current-source numerical comparison evidence here.
This completion auditor did not run a replacement probability pass or choose balancing targets.
Parent active narrow retries are pending work until their actual final results are recorded.

## Final concurrent-source follow-up

At 15:53, DEC `demons_controlled_exploitation` and `demons_make_agreement` call `riches_found_accept_account_terms`.
Material payment selects the material family and invokes `riches_found_fulfil_account_obligation`.
Authority payment selects its pending authority/trust obligation, applies the corresponding stability loss, then invokes fulfillment.
Predatory payment selects its pending industrial/human obligation, applies development sacrifice or the finite human-harm wrapper, then invokes fulfillment.
These delayed outcomes recheck payment-pending state, controller, choice and matching obligation against their current settlement predicates.
LATE now derives post-contact excavation from current depth minus depth at contact.
This is new integration evidence, not a completed account route audit or permission to reuse the old checkpoint hashes as current bytes.

| Later source | SHA-256 at 15:53 |
| --- | --- |
| CORE | `147E27D49DC4FC563DB3BFD7F95664C5AD760F9B3E293F12FC04EE09E73DA1AE` |
| ACCOUNT | `B5CBB98DB09A02BF7525B2F5775792638E5BCD63B5E24FB2B84CBDEF03F7320E` |
| TRIG | `A1DDF34CB19065EE5E3B8ED209AFA063EC4E1F9D8A4D298865142BE7376C7E00` |
| DEC | `1311DB902A995A07DBA378E3A78D1CD662996E5B221EA8845B529C8839E22D9F` |

The narrow follow-up still finds the circular occupation predicate, one positive ordinary depth action of +15, the robbery flag mismatch, and supernatural gate readers without Event029 reveal producers.
Other owner patches after the checkpoint require a refreshed final audit rather than automatic acceptance or an indefinite chase of concurrent writes.

### Parent update checked at 15:57

The account schema declares five lifetime payments, two breaches, one live 120-day obligation and a 30-day payment cooldown.
Its families are material, authority, public trust, industrial sacrifice and human crisis.
Start guards reject closed, bound, defaulted or exhausted accounts and an already-active obligation.
This is source evidence of the finite contract, not its completed balance or campaign proof.

The three existing account payment outcomes recheck their pending actor, response choice and matching promise before settlement.
Their stale branches refund the actual direct resources and call `riches_found_clear_owned_account_payment_receipt`.
That cleanup checks the original ROOT actor and expected response before clearing the state receipt, so an old country's failed timer cannot clear a different current controller's receipt merely because the response is the same.
Material refunds PP/manpower/fuel/support, authority refunds PP/command/manpower, and the current predatory recipe refunds command/infantry/support with no PP debit or refund.
Matching delayed instance and native execution behavior still require owner validation.

A repository event-ID search found exactly one definition of `chaosx.nr29.907`, in VERIFY:13.
The existing evacuation preparation callback is `chaosx.nr29.906`, EVENT:376.
No `.606` definition was found.
The requested `.907` identity therefore has no definition collision at this checkpoint.

CORE queues `.907` once per permanent seal, saving regular target `riches_found_terminal_verification_mine` and persistent due date before dispatch.
Narrow controller transfer leaves that date intact and schedules only its remaining interval, after setting the existing account-closure and Last Shift invalidation flags.
VERIFY uses that exact regular state target, registered-mine/pending/due/current-controller checks, clears pending first, and invokes the state verification and current controller's window refresh.
It adds no evolution record, asset or recurring world scan.
This callback is a source repair for terminal verification, not a basis to claim either achievement finished.
Its newly introduced source identity has no returned final MCP inspect/render/compare evidence in this audit.

The parent reports that `apply_patch` refused main-root event-file writes three times while a non-writing `[IO]` ReadWrite-handle test succeeded.
This auditor did not reproduce a write or infer the cause.
The authorized separate owned callback file implements the same route and is not classified as a fallback mechanic or route omission.
The tool-write limitation is parent-reported provenance, separate from runtime acceptance.

`localisation_cost_repair_2026_10_03.md` was read directly.
It records matching source checks for all 92 original cost recipes, 24 original inclusive resource selector components, 45 four-resource rows and the later predatory sacrifice selector.
The parent explicitly required four cost fields and permitted concise optional-symbol labels for the new sacrifice family, so the report does not treat those disclosed instructions as an unauthorized skill fallback.
The worker's coverage deliberately excludes other localisation keys and account prose.
Its survey scenario, detailed source/reference and native cost-window requests retain timeouts, cancellations or schema rejection, without a successful production row render.
Four-field native fit, mixed-level/captured equipment semantics and whole-event localisation coverage remain open.

Current parent-owned account work remains Close Account containment/breach-until-seal, bound upper workings, account prose/UI, physical commitments, dynamic costs and bespoke AI.
The callback and scoped cost-localisation repairs do not dispose of those obligations or the source gaps above.

| Updated source at 15:57 | SHA-256 |
| --- | --- |
| VERIFY | `428B61979A1AEF41489C7E40B8A5CF79979B3DD97731C3880F89E1CC9BD36FFD` |
| CORE | `52E9396FF1A90BC902F8492E9061874C289328EDC8654ECF99289154D9611F0B` |
| ACCOUNT | `B5CBB98DB09A02BF7525B2F5775792638E5BCD63B5E24FB2B84CBDEF03F7320E` |
| DEC | `1311DB902A995A07DBA378E3A78D1CD662996E5B221EA8845B529C8839E22D9F` |
| SLOC | `1D2A27128758BFA20C49C968E5510DAF11709DB07FB8BC291F9DBEFDF5D33BFA` |
| Decision English localisation | `54D211B8DFB8161FEC6CB56502BDADF290C3DC09D390B50FBD2FA54006AACCAF` |

## Checkpoint source identities

| File | SHA-256 |
| --- | --- |
| CORE | `49C9A966049CD40E1C9A400B0986411D4C451076C1C392594B5DDD832FB71767` |
| INC | `2637EEA37ACAC42C8105CC1E881589752FE33DDEA6F08779CDA7CDC095DBD5EC` |
| LATE | `501906C902BD17A2A0107FBF6C61CB93F2A7473F465D1E688CAE6F12022F84AF` |
| ACCOUNT | `95AB70647C973769185FA8749412BD64932D38C5C0EB2D950CEE319B1AC209D8` |
| MAINT | `0F5CE8200DA84AB0DB739BCEC7B1EF331BCDA0EE050E6E35393594FA9CC12CC1` |
| TRIG | `8A0BDF56F2AB7422A062BCAE53F4C7B0D56AEDA1B748F47B509C37D34D2EB884` |
| DEC | `B46CAEAB5FD0392B9D3FE2FE5DBC4CAE46B007B46BCD662536573AC84633E0E6` |
| EVENT | `45C0CE4F5C22D503AF9B627CE8300EEA463894DEFE2BE54DBBAC41864A29DCCA` |
| CONST | `492CCF66E1C4D46C2C33BC37D14CC1892A83BDA74CEA4AC7C3939766A1D0D62D` |
| Authoritative catalog XLSX | `3420053B9CEDC45B7BDE32562EFD00C0169ED74F9A9589CA482370BA8A641D67` |

Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, `chaos-redux-scripted-gui` for the inherited ordinary-surface budget, `chaos-redux-mtth` for the timing evidence boundary, and `xlsx` for authoritative read-only catalog inspection.
No skill was created or updated.
No implementation simplification was introduced by this audit.
Existing missing mechanics, weakened representations, unhandled history and evidence blockers are explicitly reported above, so the overall implementation cannot be described as having no simplifications or omissions.
