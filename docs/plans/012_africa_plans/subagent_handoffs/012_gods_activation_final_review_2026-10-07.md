# Event 012 Gods activation final source review

Disposition: `implemented` for the bounded F1–F4 owner repair, with parent review and commit pending.
The exact current source is correct for the requested activation and settlement cases below.
This verdict establishes source logic only, and does not establish native execution, numerical settlement correctness, AI cadence, or acceptance of the full Gods of Africa goal.
The acceptance basis for this review is the parent's explicit read-only assignment and subsequent instruction to include the missing-type guard.

Only this handoff was written by the reviewer.
No gameplay, localisation, GUI, WP1 content, staging, index update, commit, or HOI4 launch was performed.
No implementation simplifications were introduced.

## Inputs and current identities

Read current `AGENTS.md`, events and subagents guidance, pertinent decisions and focus-helper guidance, and the activation follow-ups beginning at line 140 of `takeover_completion_review_2026-10-06.md`.
The named JSON is at `docs/plans/012_africa_plans/takeover_activation_gate_evidence_2026-10-06.json`, rather than inside `subagent_handoffs/`.
Its older trigger hash is a snapshot, superseded by the final current identity below.
The scenario, milestone and settlement-decision hashes still agree with its corresponding recorded identities.

Final SHA-256 values were reread after the parent added `has_variable = africa_triggerable_scenario_type`.

| Current reviewed file | SHA-256 |
| --- | --- |
| `common/scripted_triggers/012_africa_gods_epoch_binding_triggers.txt` | `63ba5fa62d2ca8c2bd5562abde0cdf1c1cc53fd599f64efb8d36df4181e553e7` |
| `common/scripted_effects/012_africa_triggerable_scenario_effects.txt` | `3c515a4d0b17947e9d89709e49ef2b1260f2223ff1c87ace46fdf190030c0bd2` |
| `common/scripted_effects/012_africa_focus_route_effects.txt` | `dc220b4c80eb5c9150518a325dc3c810b1f5b80dfaed9e23c2245ce31d36c838` |
| `common/decisions/012_africa_gods_decisions.txt` | `5515165dea18746734df2d50c7005d1a9c163b3afe015b2dce00967b3e4a7d45` |
| `localisation/english/012_africa_gods_l_english.yml` | `e2f561450919719da2db676ad43fddecbc30e1aba0d82b7674c0ed8f65b8d56b` |

Supporting lifecycle source identities:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/012_africa_gods_effects.txt` | `f9fcb0d37264ebe6b10e64ca8b774226c17804170fae194bf616f4155aa00d51` |
| `common/scripted_triggers/012_africa_gods_recovery_triggers.txt` | `3664ab41fa1bfc62eca631c5e1618cfa94e3e3dda7568d0c749c816e5e34369c` |
| `common/scripted_effects/012_africa_gods_recovery_effects.txt` | `14affd56c1200bd1289b00973ba151158b686065e42b13421b8ecbd2dae562a2` |
| `common/scripted_effects/012_africa_gods_settlement_effects.txt` | `888652459bd40d41491cb8995e48d46399a50a2c52d0d52db2348044db38170e` |
| `events/012_africa_gods_of_africa.txt` | `7b502d802cecc4a160d3649e936e57f62bbefa17329586190dceb90f5510d1a5` |

## Source cases and findings

These are source entailments with stated preconditions, rather than executed engine or MCP scenario fixtures.
Normal positive cases assume the exact committed current host, first proof, valid current capital, active Event 012, and no loss, transfer, terminal or final receipt.

| Case | Current source result |
| --- | --- |
| Initial formation alone | `africa_is_one` and `africa_continental_settlement_complete` do not satisfy security. They remain legitimate formation receipts. |
| EI before formation | The EI call fails the formation requirement without binding an epoch. The milestone retry at focus-route effects line 2319 starts the canonical initializer after formation and identity writes. |
| Formation before EI | The milestone call fails the EI requirement. The existing EI owner call at evolution effects line 51 subsequently binds and starts the same clock. |
| Fresh SCN011 Africa Is One | Scenario effects lines 224–242 seed first-proof success only if succeeded/recovered proof is absent, clear pending proof in that branch, seed EI chronology, and call consolidation. Owned and controlled current capital and uncapitulated status remain mandatory. |
| SCN011 already has earned or recovered proof | The seed branch does nothing. It does not replace recovered history or replay compound proof resolution, proof rewards, proof ledgers, achievements or reports. The chronology addition also avoids replaying the ordinary EI reward package. |
| Wrong capital ownership/control, capitulation, loss receipt, stale identity, transfer or terminal state | Unchanged physical-return, owner-object and epoch checks reject authorization or current permission. A delayed callback cannot bypass them. |
| Repeated initializer while pending | Existing epoch excludes a second grant. Same-generation initialization skips reset, and the pending flag prevents a second start day, due day or activation event. |
| Successful Scramble ratification | Settled enum with no global defeat is security. Ratification writes the enum at world-order effects line 1423. |
| Successful deferred-docket closure | The same secured endpoint is written at world-order effects line 1449. |
| Defeated settled Scramble | Defeat writes both the defeat flag and settled enum at lines 4085 and 4092. That enum alone fails security. Other loss/physical safety gates still apply. |
| Applied World scenario, no existing epoch | Applied marker, existing type variable, and exact World type make security true. The direct World body has no consolidation call, and a later ordinary EI call cannot grant a new epoch. |
| Applied marker without type variable | The World arm is false because `has_variable` fails. The marker alone is not an endpoint. Independently successful settled Scramble can still satisfy the other arm. |
| Type alone, or applied Africa Is One type | Neither satisfies the World arm. World type is 2, Africa Is One type is 1. |
| Ordinary later World progression without the exact applied-type pair | `africa_world_terminal_campaign_active` alone supplies no security witness. Normal progression is not blanket-disabled. Actual successful settlement and terminal safety remain effective independently. |
| Existing valid pending epoch reaches its due day after security | Current epoch permission intentionally permits security. The due wake rechecks scheduled/pending receipts and date, then the activation owner selects final settlement instead of activation. |
| Existing valid active epoch after security | The active host remains eligible for final closure. The owner tick closes settlement before ordinary tribute work, or the secured host action invokes the same final owner. |
| Initial formation with final-council unlock | The settlement decision remains invisible and unavailable without security. Its canonical effect independently rechecks security at execution. |
| Repeated settlement click or queued callback | Host final commitment and subsequent loss of live permission prevent another census transaction or initial payout. Participant outcome/obligation/diplomacy receipts provide additional guards. |

F1 and F4 are implemented by the country-scoped `gods_of_africa_continent_is_secured` at epoch-binding triggers lines 54–66.
Its two arms are successful settled Scramble without defeat, or the exact applied World scenario with a present type variable.
The shared initial formation flags were preserved.

The country-scoped lifecycle chain is `africa_gods_of_africa_begin_consolidation` → `gods_of_africa_authorize_initial_epoch` → `gods_of_africa_initialize_system` → `gods_of_africa_start_consolidation`.
Relevant definitions are Gods effects lines 4720–4731 and 18–92, recovery effects lines 8–32, and recovery triggers lines 5–48.
The caller token is consumed after either authorization success or rejection.
No helper, constant, periodic hook, scope pointer or tuning value was added by this review.
The unchanged tuning source remains `constant:gods_of_africa_timing.consolidation_days = 180`.

The due endpoint is recovery triggers lines 278–292 → hidden `chaosx.nr12.600` → Gods effects lines 4733–4738 → final settlement lines 4593–4648.
The wake requires current permission, pending/scheduled receipts, no activation, and `global.num_days` at least the retained due day.
Secured status is intentionally absent from current epoch permission and the wake predicate.
It is excluded at new-grant and activation gates, and required at final settlement.
The repair leaves inherited pending hooks unchanged and makes no independent acceptance claim for those hooks.

## One host settlement transaction

Decision `gods_of_africa_commit_settlement`, decisions lines 1636–1662, has no `target_array`, activation, target-root or target trigger, and no participant `FROM` effect.
Visibility requires active host validity, security, and the existing final-council/settlement-focus receipt.
Availability rechecks active validity and security with the named requirement tooltip.
Completion calls `gods_of_africa_commit_final_settlement` once in host scope.

The final owner commits its one-use host flag before traversing the retained `gods_of_africa_candidate_registry`.
It classifies historical survivors, freezes obligations and standing diplomacy, initializes delivery, sends one bounded batch, finalizes participants, records the milestone once, then clears live authority and clock receipts.
The census is retained from Event 012 world-order effects lines 820–825 and 902–915, with unique insertion checked by Gods triggers lines 128–139.
This is one host transaction over that census, rather than one repeated transaction for each visible target row.
It does not add another unrestricted world scan.

Settlement-history checks remain independent of live epoch permission after the host final flag is written, through `012_africa_gods_settlement_triggers.txt:5–48`.
Participant final outcome, obligation and diplomacy guards are in settlement effects lines 20–60, 94–137 and 141–188.
Later outstanding-support batches remain separate from final grading.
This review confirms ownership and replay guards, without claiming measured stockpile debits, fuel storage behavior, or numeric entitlement correctness.

The three existing English settlement title/description/effect keys were updated, and `gods_of_africa_secured_settlement_required_tt` was added.
The wording describes the host action and available reserve-backed support without promising another target-specific payout.

## MCP and primary reference evidence

The exposed reference, source lookup, event inspect/render and script validation routes were verified from the live tool metadata.
Reference context, targeted searches and revision-bound reads succeeded.
The context bundle omitted Event modding, Scopes, On actions and Localisation at its limit, so it is not represented as exhaustive reference coverage.
Targeted Scopes and decision reads supplied the rules used here.

| Rule directly read | Source path and lines | Source revision |
| --- | --- | --- |
| Variable equality and inclusive date comparison | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:2110–2135` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Country flag effect scope | Same game root, `documentation/effects_documentation.md:6730–6738` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Scoped constant access | Same game root, `documentation/script_concept_documentation.md:216–222` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Constant schema | Same game root, `common/script_constants/documentation.md:1–34` | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Decision owner, availability and targeted row creation | Same game root, `common/decisions/_documentation.md:1–46` | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |
| Offline variable syntax | `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:566` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline flag syntax | `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:897` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Immediate decision effect and ROOT/FROM row semantics | `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:268–277,511–518` | `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` |
| Country capital enters state scope | `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:268` | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Custom tooltip alias | Game `documentation/triggers_documentation.md:2482–2489` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |

Vanilla precedent `SOV_third_five_year_plan_available`, `game:common/scripted_triggers/SOV_scripted_triggers.txt:62–67`, was read directly and through source lookup.
It wraps a flag requirement in a named custom trigger tooltip.
Lookup revision was `21d8467bd1e7081365cd2f35374162b43ed303bbaba3cd0e900ba86abf27dcd2`.
Exact settled, first-proof and consolidation helper definitions were also returned without overrides by source lookup, revision `cb8d66dba54f48f0368336027c46babd6d906ac7f835b17351149fb7966c699d`.

`hoi4.script_validate` checked the final secured trigger including the missing-type guard, SCN011 chronology addition, settlement availability and completion bodies under explicit country scope.
These returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, with checks limited to syntax, command kind and declared scope.
The secured trigger had unresolved scripted settled helper coverage and one unchecked `check_variable` argument block.
The chronology body had unresolved first-proof and consolidation helper coverage.
Availability had unresolved active-host helper coverage and an unchecked custom-tooltip argument block, whose prose read does not prove recursive argument validation.
Completion had unresolved final-settlement helper coverage.
Those helper definitions and the answering native rules were separately read, which supports the source review without turning the partial validator into engine acceptance.
Documentation catalog revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

An additional inlined physical-return trigger returned `SCRIPT_CHECKED`, `valid = true`, with `parametersChecked = false`.
That result covers the same three check kinds, rather than native scope-target behavior.
The subsequent optional `has_variable` reference read did not publish a result before its waiting execution was stopped, and is not claimed as a completed read.

Narrow `.600` trace succeeded with `EVENT_INSPECTED_PARTIAL`, focused mode, helpers disabled, depth 1, six nodes and eight edges.
The complete linked trace resource was read by bounded byte ranges after the first large resource response was truncated.
Graph revision: `4969042f8122a553c30402d067b14cdc9c731bc3674b68dd419cb0813fb913a7`.
Graph hash: `60323e4fbfff191e6014b7974139c7ab25f78ed1404cd7311f444ed4bf70b43f`.
Artifact SHA-256: `732994e638db082e17b2aea72a47c244e146887c828c4cafa6b88b6eab0bf91b`.
Artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/732994e638db082e17b2aea72a47c244e146887c828c4cafa6b88b6eab0bf91b/32d813835b29c6a20da478df817a1ccdc11717b9c79b1943f1cd334cb19eeaaf/event-trace-4969042f8122.json`.

The trace confirms the hidden triggered-only country event calls `africa_gods_of_africa_commit_activation` at event source line 18.
It expressly reports `EVENT_FOCUSED_ANALYSIS_DEFERRED`, `complete = false`, and an unresolved helper boundary for that call.
That boundary is a coverage limit, not proof that the helper is absent from current source.
A matching narrow options render failed with `JOB_WORKER_EXIT`, message `The worker stopped without publishing a terminal job outcome`, and no artifact.
No render completion is claimed.
No broad graph job, helper-expansion negotiation, service restart or invented viewer capability was used.
No meaningful event-graph before/after helper comparison is claimed because the available focused graph excludes the changed helpers and there is no established matching pre-repair graph baseline in this review.
Probability comparison and native payout/cadence evidence remain the parent and `chaosx_ai_probability_auditor` responsibilities, with no numeric AI conclusion here.

## Parent follow-up and limits

No additional gameplay defect was found in the five-file repair under the specified cases.
Parent can review and commit it on these source identities, carrying the render and partial-validation limits above.

Documentation remains stale at recovery effects markdown line 17 and recovery triggers comment line 54, which still describe the initial continental receipt as a security witness.
Parent should replace that description with successful settled Scramble without defeat, or the exact applied World scenario with a present type variable.
The old evidence JSON trigger hash should remain identified as historical or be reconciled with the final hash above.
These documentation discrepancies do not change the inspected runtime predicates.

The unchanged clock starts when the canonical caller has both formation and EI chronology, and therefore begins at the later boundary in the two ordinary orderings.
Full spec line 89 says establishment proof, while the current guide line 9 and source describe an EI consolidation clock.
This pre-existing timing-description difference is left for parent design/documentation reconciliation, and this review does not silently alter the clock or assert complete spec alignment.

Inherited history, pending-hook lifecycle, native transactions, full numeric grading, portraits, assets, GUI, focus-tree acceptance, AI behavior and whole-goal completion are not promoted by this bounded verdict.
The user retains live-game validation, and the reviewer neither launched HOI4 nor requested that the user perform a test.
