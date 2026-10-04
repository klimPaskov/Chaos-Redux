# Event 023 local-custody probability audit

Audit date: 2026-10-03.

Status: source review completed; probability analysis and before/after comparison unresolved because the connected HOI4 probability routes are unavailable.

This report is read-only with respect to gameplay, localisation, assets, workbooks, and Git. The only file written for this audit is this handoff.

## Scope

Weighted surface: Event 023 breakaway local-custody decisions, limited to `sov_nuclear_bombs_breakaway_secure_custody`, `sov_nuclear_bombs_breakaway_attempt_technical_access`, `sov_nuclear_bombs_breakaway_form_command`, and `sov_nuclear_bombs_breakaway_integrate_delivery` in `common/decisions/023_sov_nuclear_bombs_decisions.txt`.

The shared launch and evolution surfaces are outside scope. The assembly auditor's handoff was not edited.

Scenarios supplied for this audit: `P23_LOCAL_FIRST_DEPOT`, `P23_LOCAL_SECOND_AFTER_FIRST_OPERATIONAL`, `P23_LOCAL_LOST_DEPOT`, `P23_LOCAL_OTHER_ACTOR_ACCESS`, `P23_LOCAL_JOINT_CUSTODY`, and `P23_LOCAL_ACTIVE_STAGE_LOCK`.

The existing `docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_probability_scenarios.md` contains other Soviet Collapse cases, including `P23_COLLAPSE_NEGOTIATE_STABLE_BREAKAWAY` and `P23_COLLAPSE_OPERATIONAL_SUCCESS`, but none of the six `P23_LOCAL_*` IDs. The six local cases are therefore recorded as audit scenario names from the parent instruction, not as complete fixtures from the checked-in scenario matrix.

## MCP route and evidence status

The enabled tool catalog contains no `mcp__hoi4_agent_tools__*` route. Runtime exposure checks returned `undefined` for `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, `hoi4.probability_simulate`, `hoi4.probability_sequence`, `hoi4.probability_render`, `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, and `hoi4.event_render`.

A direct read-only `hoi4.probability_inspect` attempt failed locally with `TypeError: tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function`; no request reached an HOI4 server and no live schema was available.

The narrower resource-template discovery call `list_mcp_resource_templates({server:"hoi4_agent_tools"})` failed with `failed to get client: MCP startup failed: timed out handshaking with MCP server after 119.9999997s`.

The supplied workspace identifier is `mod_chaos_redux_ea3b2d67c2c0`. Without a callable probability route or its live schema, I could not bind an inspect or compare request to that workspace without guessing unsupported fields.

No probability inspect, evaluate, sweep, compare, simulation, sequence, or probability render completed. No MCP artifact URI, server revision, scenario hash, comparison id, or rendered evidence URI/path exists for this audit. No server version/health or task negotiation was established, and no job or helper-expansion route was used.

The decision-specific structural and probability views are unresolved. Source review does not substitute for the mandatory MCP analysis.

## Immutable before sources and current after sources

The three immutable snapshots match the SHA-256 values supplied by the parent. They capture the actor-owned pointer patch, while the secure-custody decision still has its old country-wide `sov_nuclear_bombs_breakaway_custody_secured` lock and its staged country flags.

| Role | Exact path | SHA-256 |
| --- | --- | --- |
| Before decision source | `docs/plans/023_sov_nuclear_bombs_plans/probability_source_snapshots/local_custody_2026-10-03/before_decisions.txt` | `915A516FCB7B3717AC58BFF09673B3A7AF5F52CCCF2AB46A748596A9BDEE5AE8` |
| Before trigger dependency | `docs/plans/023_sov_nuclear_bombs_plans/probability_source_snapshots/local_custody_2026-10-03/before_triggers.txt` | `4CE6073BFDE02761C5744BD618B89CA2CBFD59CFFC05FA9885ADB85F99D50982` |
| Before effect dependency | `docs/plans/023_sov_nuclear_bombs_plans/probability_source_snapshots/local_custody_2026-10-03/before_effects.txt` | `E99B18C5EE99D3A6E7E7384515FCD9E0A3C7927D7AFF01885A5A5B4AFFCEF8D0` |
| After decision source | `common/decisions/023_sov_nuclear_bombs_decisions.txt` | `EDD21C1D4F062DBD02C4DF5FC99FF5B50F23093ECF6C8582777B946AABB01AAB` |
| After trigger dependency | `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt` | `B09ED078E9FBA26628488CA1BC51656CC5FCE7F301492263E545D74948B168DD` |
| After event-effect dependency | `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | `57DF338E7C974D2BD4F0466437B60D80462A4D41A86E57856A4AFE17614CB2EB` |
| After runtime-effect dependency | `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `2BD130BC9C4F079A5D73456A077CDF12EBA04ADE12E3FAE19C923388A1F012B0` |
| Existing tuning constants checked for weight centralisation | `common/script_constants/023_sov_nuclear_bombs_constants.txt` | `5BCF3F563B9ABEEC59C8A93A73FA1F89A7AF3FB1EF9B9D4B9D7FDE90B40E54FC` |

There is no immutable pre-edit runtime-effect source among the supplied snapshots. The current runtime helper can be reviewed, but its historical before/after change cannot be established from these artifacts.

The current event-effect file also differs from `before_effects.txt` outside the local-custody repair, including action-context and detonation receipt areas around lines 726-866 and remote-recovery authorization around line 1892. Those concurrent out-of-scope differences were not audited or attributed to this repair. They further prevent treating the current whole helper file as an isolated before/after dependency graph.

Because helper definitions in the live workspace are after-source files and the before copies live under `docs/plans`, faithful dependency resolution of a copied before graph cannot be claimed. In particular, the pre-edit runtime helper is absent. Even if the MCP route returns, a numeric comparison remains unresolved unless the adapter can isolate the complete copied before dependency graph or a trustworthy immutable pre-edit runtime source is supplied. Do not compare the current file to itself.

## Source-derived AI scores

The before and current decision blocks were read directly. The source diff changes eligibility, selection, and cancellation predicates; it does not change any of the four `ai_will_do` expressions, costs, or decision removal durations.

| Decision id | Before `ai_will_do` | After `ai_will_do` | Modifier trace | Classification |
| --- | --- | --- | --- | --- |
| `sov_nuclear_bombs_breakaway_secure_custody` | `base = 1.30` | `base = 1.30` | No modifiers | Exact source score only |
| `sov_nuclear_bombs_breakaway_attempt_technical_access` | `base = 0.40` | `base = 0.40` | No modifiers | Exact source score only |
| `sov_nuclear_bombs_breakaway_form_command` | `base = 0.25` | `base = 0.25` | No modifiers | Exact source score only |
| `sov_nuclear_bombs_breakaway_integrate_delivery` | `base = 0.10` | `base = 0.10` | No modifiers | Exact source score only |

The in-file score order is secure custody, technical access, command formation, then delivery integration. This is an `ai_will_do` willingness-score order, not a normalized share, click probability, or probability-proportional sample. The offline AI modding reference describes `ai_will_do` selection as score-based in the general case and distinguishes it from event-option `ai_chance` sampling.

The score expressions are unchanged, but changed eligibility can change which decision instances enter the AI's live candidate set. The full decision candidate pool, vanilla-level AI effects, and campaign state are not established. The source order alone proves no dominance, starvation, or balance result.

## Eligibility and receipt review

`sov_nuclear_bombs_breakaway_secure_custody` now opens when `sov_nuclear_bombs_event_selected_breakaway_site_is_valid_for_actor` is false. The same acting-country condition appears in `visible`, `target_root_trigger`, `available`, and the completion limit. Its target predicate admits registered transferred depots in `breakaway_physical` custody, excludes Event 5 snapshot-pending, dismantled, missing, technical-denial, and already operationalized sites, and requires the actor to own or control the state. The available and completion checks additionally require a live `sov_nuclear_bombs_site_holder` matching `ROOT`.

The selected-site validity helper also checks the stored state pointer against its stored state id, current registration and transfer state, pending/dead/denial/operationalized status, physical custody, current holder equal to `ROOT`, and current ownership or control by `ROOT`. Joint custody therefore fails the physical-only selection gate.

The new state-level receipt helpers bind custody to `sov_nuclear_bombs_local_custody_actor = sov_nuclear_bombs_site_holder`, technical access to `sov_nuclear_bombs_institutional_access_actor = sov_nuclear_bombs_site_holder`, and command access to `sov_nuclear_bombs_breakaway_command_actor = sov_nuclear_bombs_site_holder`. Technical and command receipts also reject their respective contested markers. Country-level selected-site wrappers require the actor-valid current state pointer before checking those state receipts, so a receipt held by another depot or inherited from another actor does not satisfy the selected site.

On custody selection, `sov_nuclear_bombs_breakaway_secure_local_custody` clears the four projected country flags for custody, technical access, command, and delivery, stores the current actor as `sov_nuclear_bombs_local_custody_actor` on the selected state, sets the physical custody receipt, then projects technical and command flags only when that same selected state has the corresponding local receipt.

The three stage-start helpers recheck their selected-state receipt and next-stage absence. Technical start also rechecks both required technologies and physical custody; command start rechecks technical receipt and physical custody; delivery start rechecks command receipt, current physical custody, and delivery capability. The shared completion helper repeats the matching stage receipt and exact-site checks before publishing each completion. The three timed mission `cancel_trigger`s cancel on loss of their stage's selected-site receipt, and delivery also cancels if its delivery capability is lost. All three `cancel_effect`s call `sov_nuclear_bombs_cancel_breakaway_operationalization`, which clears the active mission and progress stage while retaining the actor's depot for a valid retry.

The updated `sov_nuclear_bombs_rebind_event5_site_holder` in `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` snapshots the prior holder in an unscoped temporary, derives the current non-SOV controller or else owner, and reclassifies only when that holder actually changes. A changed breakaway holder sets `breakaway_physical`; another changed holder sets `foreign`; a same-holder callback leaves the custody class untouched, preserving joint custody. The helper body reads the current state and contains no state or country iteration. Its call sites invoke it from state handling, including Event 5 state reconciliation. The full callback chain and runtime behavior remain unverified. The live helper still debits the prior holder's transferred ledger and credits the derived holder, but no before-runtime snapshot exists to verify the parent's claim that those formulas are unchanged.

## Scenario completeness and results

The state-candidate predicate is source-defined, but no scenario supplies the actual state roster, actor tag, owner/controller/holder identities, transferred amounts, receipt flags, active-stage state, technologies, delivery capability, affordability, or other simultaneously available decisions. The four decision IDs are a complete list of the explicitly authorized audit scope, not a complete engine AI decision pool. The scenario candidate pool and external-factor completeness are therefore `No` for every runtime scenario.

| Scenario id | Source-only expectation | Missing scenario inputs | Result classification |
| --- | --- | --- | --- |
| `P23_LOCAL_FIRST_DEPOT` | Custody selection requires at least one registered, transferred, unoperationalized physical depot whose current holder is the actor. Stage actions require the newly selected site's own custody receipt. | Actual candidate state ids/count, actor identity, owner/controller/holder, ledger quantity, pending flags, technologies, cost affordability, and competing decisions. | Unresolved runtime; score-only bases listed above. |
| `P23_LOCAL_SECOND_AFTER_FIRST_OPERATIONAL` | The first operationalized site is invalid for the current selection, and operationalized sites are excluded as new targets. A second site can be selected only if another eligible physical depot exists. Its own technical and command receipts determine which projected stage flags return. | Exact first and second state ids, second-site eligibility/receipts, holder identities, actor technologies, other candidate sites, and competing decisions. | Unresolved runtime; no sequence or repetition count. |
| `P23_LOCAL_LOST_DEPOT` | A changed current holder is reclassified as physical breakaway custody or foreign custody. If the selected site no longer passes actor-valid physical custody, the stage receipt fails and the active mission cancels. | Which ownership/control change occurred, resulting holder, custody class, pending snapshot status, current mission stage, and alternate eligible depots. | Unresolved runtime; historical runtime delta also unresolved. |
| `P23_LOCAL_OTHER_ACTOR_ACCESS` | Technical and command markers from another actor cannot satisfy the selected site's actor-to-holder equality checks. | Actual holder, recorded custody/technical/command actors, contested markers, selected state identity, and any alternate candidate states. | Unresolved runtime; source gate reviewed. |
| `P23_LOCAL_JOINT_CUSTODY` | A site still classified as joint is excluded from physical-only breakaway selection. A same-holder rebind preserves its existing custody class. | Exact holder/actor identities, any second physical depot, stage flags, and campaign state. | Unresolved runtime; no AI score result. |
| `P23_LOCAL_ACTIVE_STAGE_LOCK` | `no_active_project` and the operationalization-mission-active flag block selection or a new stage while a stage is active. Completion and cancellation still use the current selected-site receipt. | Active stage/mission id, current depot, timer point, receipt state, and competing decision pool. | Unresolved runtime; source gate reviewed. |

No scenario fixture fields were invented. No seed or uncertain input was declared, so simulation was not appropriate. No complete custom pool with cadence and transitions was supplied, so sequence analysis was not appropriate.

## Balance, repetition, and exploit findings

There is no source-level modifier trace capable of reversing the four stored bases. Cross-decision rank reversal, sensitivity thresholds, and starvation against the rest of Event 023 remain unresolved because the required sweep and complete live decision pool are unavailable.

The four named stages are gated in sequence, so their base scores do not form a four-way race while one selected depot remains valid. Secure-custody selection reopens only after that selected depot becomes invalid, including after operationalization, and completed sites are excluded from the target predicate. This source structure shows no unbounded repeat on the same depot. The count and AI cadence across multiple eligible depots remain unresolved without a complete scenario pool and the installed analyzer.

The positive source bases remain attached to the four decision definitions, while current visibility, availability, cost, technology, route-capability, and completion gates determine whether an instance can be acted on. Technology and cost checks do not all appear in `visible`, so this source review cannot prove how the engine excludes unavailable instances from AI scoring. Runtime validity remains unresolved because no MCP scenario could be evaluated. No AI-strategy or AI-template reference to these four exact decision ids was found in the scoped repository search; generic engine-level effects were not established.

The four base weights are inline literals rather than entries in the existing `sov_nuclear_bombs_ai` script-constant group. A separate, non-balancing maintainability patch may centralize them in `common/script_constants/023_sov_nuclear_bombs_constants.txt` while preserving `1.30`, `0.40`, `0.25`, and `0.10`. It is not a repair blocker and is not recommended as a balance adjustment; any later AI-weight source change still requires the same-scenario probability comparison.

The sources support the parent's statement that numeric weights, costs, and decision removal durations did not change in these four decisions. The local-custody diffs add no random-selection branch. The broader current event-effect file has the unrelated snapshot differences listed above, and the runtime helper has no before copy, so this audit cannot certify a historical file-wide random or ledger delta.

## References and local revisions

Offline wiki references were read directly because the live reference tools were unavailable: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` lines 357-373, SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`; `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` lines 26-36, SHA-256 `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818`; and `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` lines 811-845, SHA-256 `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49`.

Installed vanilla documentation was read directly at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md` lines 1-36, SHA-256 `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`. It documents the targeted-decision scopes and evaluation of `visible`, `available`, `target_root_trigger`, and `target_trigger`; this is reference context, not validation of these mod definitions.

The checked-in Event 023 scenario matrix has SHA-256 `9889DB1555FA8BB6F5784D6B692055866515203987908230C71E277ED199CF7B`; the AI and probability specification has SHA-256 `0A56968CB6911961A2484CA973396CB4903D4CBF2798450EEED20A1713F7C918`. Its Soviet Collapse AI priority order at lines 348-370 places physical custody first, technical access after recognition/return/concealment decisions, and operationalization only when security, command, and delivery can be sustained. Its probability contract at lines 387-398 requires inspect, named scenarios, and same-scenario comparison.

## Recommended follow-up and blockers

Restore or expose the HOI4 probability routes and their live schemas for workspace `mod_chaos_redux_ea3b2d67c2c0`, then run `probability_inspect` first and evaluate/sweep all six named scenarios with explicit, schema-supported inputs. Provide the complete state target pool and the relevant simultaneous AI decision candidates before making any dominance, starvation, rank-reversal, or probability claim.

Run `probability_compare` only with the exact `before_decisions.txt` snapshot and current `common/decisions/023_sov_nuclear_bombs_decisions.txt`, using the identical named scenario set. Preserve the before trigger/effect copies as dependencies and demonstrate that the adapter resolves them as an isolated before graph. The missing `before_runtime_effects.txt` source is a historical comparison blocker; without an exact pre-edit runtime source or verified dependency isolation, leave the numeric delta unresolved.

Do not change these AI weights on the evidence in this report. The only score conclusion is the exact source base trace, classified score-only. No balance acceptance is provided.

Skipped: probability evaluate/sweep/compare/render because the probability tools are absent and the resource-template discovery timed out; simulation because no uncertain values or seed were declared; sequence because no complete custom-pool manifest was declared; broader Event 023, assembly, launch, evolution, localisation, and asset analysis because they are outside the authorized surface.
