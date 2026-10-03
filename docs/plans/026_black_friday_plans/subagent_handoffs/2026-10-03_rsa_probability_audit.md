# Event26 RSA purchase probability audit

Status: incomplete. Source review is complete, but the required probability MCP analyses returned no analysis artifacts. All probability conclusions below remain unresolved unless explicitly classified as source-only.

Scope: the five purchased South Africa decisions in `common/decisions/012_africa_rsa_decisions.txt`, plus the `chaosx.nr12.1202` regional-support reply options and their narrow donor-request helpers. The decision and event files are compared with their exact physical snapshots under `docs/testing/2026-10-03_event26_rsa_before/`.

Read-only boundary: no gameplay files were changed, no tests were run, no commit was made, no game process was launched, and no logs were requested or inspected.

## Audited surfaces and source identity

| Surface | Exact source | Observed SHA-256 |
| --- | --- | --- |
| Candidate decisions | `common/decisions/012_africa_rsa_decisions.txt` | `5DD77C415A5E68E4353D82A5418B0AD8D0644C36A5AC01514656C6A81D96E740` |
| Immutable before-source used for comparison | `docs/testing/2026-10-03_event26_rsa_before/012_africa_rsa_decisions.txt` | `40283784E0D0EA091BD96C96C46F0155EC01E911091B2B20A0389AC5E1D696CC` |
| Candidate event options | `events/012_africa_rsa.txt` | `89D5165760C2B0505D50265BE01720FBA546BD6F62C45D7082323CAF58CE325E` |
| Physical event before-source | `docs/testing/2026-10-03_event26_rsa_before/events/012_africa_rsa.txt` | `F0776F45258613E443BA09EBC1608FDC560CE6C904BF2E574DD3509CD585B1EF` |
| Purchase quotation and affordability triggers | `common/scripted_triggers/012_africa_rsa_purchase_triggers.txt` | `EC3C1ADF78C811F6729B63CE4B0544D1DB00D04FE90F59E34F1F80A001431653` |
| Purchase and receipt effects | `common/scripted_effects/012_africa_rsa_purchase_effects.txt` | `023A8E8232408F4795B7E3FA1C90949CD408A271A45A1F4CBE8F87F82923821F` |
| Paid support-request lifecycle effects | `common/scripted_effects/012_africa_rsa_support_request_effects.txt` | `206C1AABD0C2BCC908C939E2827018223EF1EF3987241D486961A75EA85D1D92` |
| Existing RSA route and target triggers | `common/scripted_triggers/012_africa_rsa_triggers.txt` | `320D02ECA904154F70C9DB161D52DB692404F1BCDF9AD5518CCA8674376CE77B` |
| Existing RSA registration and cleanup effects | `common/scripted_effects/012_africa_rsa_effects.txt` | `9D34584A577ED0B33A8DFFA40E4A20EC7AAECE6D201C94A90F40C19BC7385306` |
| Purchase action selector constants | `common/script_constants/012_africa_rsa_purchase_constants.txt` | `CC40CFE52805DDE2CE39C96D85D7406E8A8237A90730C07DBAED966018E5F916` |
| Existing RSA costs and AI constants | `common/script_constants/012_africa_rsa_constants.txt` | `F4979BD1E1F2D575A88E0149036E5F698FEA3B89C5D863DEEF9ED2B48569C41A` |
| Owner transaction contract | `docs/systems/africa_rsa_purchase_transactions.md` | Read for this audit. It records the transaction design and owner-declared price cases. |

Candidate/helper hashes above are audit-snapshot fingerprints, not final-freeze identities. The target-trigger hash predates the parent's latest `hidden_trigger` wrapper update. Final candidate source hashes are pending the parent's freeze. The physical before-source hashes remain the exact byte identities recorded above.

The decision before-source file has the expected physical SHA-256 above and was the file used for the decision comparison. My earlier Git object check found the pre-repair worktree object `b498d994e068f1f8a53ac687a6714a6625f4f0f5` differed from the then-current `HEAD` path object `3705ccbd67b54bbb9a2ea70934a8e9be8607e945`.

The parent now reports that the decision snapshot's physical and raw committed byte identity was repaired in commit `f9f057581c080784b92ed14fd0a736f6f9708958`, with a final raw-byte hash verification still pending. The event before-source file has physical SHA-256 `F0776F45258613E443BA09EBC1608FDC560CE6C904BF2E574DD3509CD585B1EF`, matching the parent-supplied identity. The parent reports that this event snapshot is currently untracked for a pending RSA commit and that no-filters attributes now prevent line-ending conversion. No committed-byte identity is claimed for it yet. This audit did not alter or stage either snapshot.

The decision before/candidate diff shows the five decision `ai_will_do` expressions, target arrays and target predicates, existing cooldown/fire-once fields, and route/activation blocks unchanged. The candidate adds five literal `ai_hint_pp_cost` values and replaces the prior affordability/payment call sites with the purchase helpers. Ordinary price constants remain in `africa_rsa_cost`.

The event before/candidate diff changes only the `chaosx.nr12.1202.a` trigger and hidden effect, plus the `chaosx.nr12.1202.b` hidden effect. Both option `ai_chance` blocks are unchanged in the physical diff and were reported AST-equal by the parent tests.

## Decisions and score-only evidence

All values in this table are source-derived willingness-score inputs, not probability results. `africa_rsa_ai.high = 10`, `preferred = 20`, and `modifier_double = 2` are read from the named RSA constants file.

| Decision ID | Existing base and modifier | Source-implied score when available | New PP saving hint | Existing repetition/target behavior |
| --- | --- | --- | --- | --- |
| `africa_rsa_protect_civilian_corridor` | `high = 10`, doubled when State 275 is controlled by ROOT. | 20 for an available decision because the same State 275 control is required by `available`. | 35 | No target array. `fire_only_once = yes`. |
| `africa_rsa_seek_regional_support` | `high = 10`, doubled when FROM is a neighbor of ROOT. | 10 for a valid non-neighbor target, 20 for a valid neighboring target. | 15 | `target_array = africa_selected_targets`. Supporter-count activation and existing target-validity/refusal/support flags remain unchanged. No `fire_only_once` field appears in this decision block. |
| `africa_rsa_enact_citizenship_land_milestone` | `preferred = 20`, with no modifier. | 20. | 75 | No target array. `fire_only_once = yes`. The current-host route gate remains unchanged. |
| `africa_rsa_guarantee_neighbor_sovereignty` | `preferred = 20`, doubled when FROM is in a faction with ROOT. | 20 for a valid non-faction target, 40 for a valid same-faction target. | 40 | `target_array = africa_selected_targets`. Route and neighbor/guarantee/war/subject checks remain unchanged. No `fire_only_once` field appears in this decision block. |
| `africa_rsa_reconstitute_exile_council` | `preferred = 20`, with no modifier. | 20. | 60 | No target array. `fire_only_once = yes`. The existing exile-recovery route helper remains unchanged. |

The score entries are exact source expressions evaluated with the named constants, but remain score-only. Neither the MCP analyzer nor the HOI4 engine evaluated them in this audit. The source conditions create conditional ranking changes: regional support moves from 10 to 20 with a neighboring target, and sovereignty moves from 20 to 40 with a same-faction target.

Those modifiers permit rank reversals within the five audited candidates, but no scenario-specific reversal, dominance, starvation, or selection frequency is established. A decision willingness score is not a click probability, and the new saving hints are separate from the `ai_will_do` expression.

## Cost quotes and affordability surface

The following are the owner ledger's declared ordinary, baseline-sale, and Evolution I prices. They are not MCP-evaluated outputs in this audit.

| Decision | Component | Ordinary | Baseline sale | Evolution I sale |
| --- | --- | ---: | ---: | ---: |
| `africa_rsa_protect_civilian_corridor` | Political Power | 35 | 18 | 9 |
| `africa_rsa_protect_civilian_corridor` | Command Power | 20 | 10 | 5 |
| `africa_rsa_protect_civilian_corridor` | `train_equipment_1` | 5 | 3 | 2 |
| `africa_rsa_protect_civilian_corridor` | `support_equipment_1` | 150 | 75 | 38 |
| `africa_rsa_seek_regional_support` | Political Power | 15 | 8 | 4 |
| `africa_rsa_enact_citizenship_land_milestone` | Political Power | 75 | 38 | 19 |
| `africa_rsa_enact_citizenship_land_milestone` | Stability, quantum 0.01 | 0.05 | 0.03 | 0.02 |
| `africa_rsa_guarantee_neighbor_sovereignty` | Political Power | 40 | 20 | 10 |
| `africa_rsa_guarantee_neighbor_sovereignty` | Command Power | 10 | 5 | 3 |
| `africa_rsa_reconstitute_exile_council` | Political Power | 60 | 30 | 15 |
| `africa_rsa_reconstitute_exile_council` | Command Power | 25 | 13 | 7 |

The new hints equal the ordinary Political Power components, not the multi-resource bundle totals, and remain static during sales. The owner ledger describes them as conservative native saving hints and explicitly does not claim discounted AI scoring.

Source review shows each decision calls its matching `africa_rsa_can_pay_*_purchase` wrapper from both `available` and `custom_cost_trigger`. The shared helper freshly quotes the selected action, rejects an invalid quote or an existing pending receipt, and checks Political Power plus every positive secondary component through `universal_cost_component_is_affordable`. The purchase effects revalidate the owner route and target, recompute the quoted bundle, require every component to match the prior quote and be affordable before the first debit, and then record, settle, or refund receipt rows through the shared transaction calls.

The prior corridor gates could admit equipment amounts below the exact model-specific debit, and the replacement helper checks the quoted `train_equipment_1` and `support_equipment_1` amounts. This is source behavior and the owner ledger's source-test contract, not proof of native resource mutation or runtime quote/payment equality.

Gate-order observation: owner decision route/target checks are in the decision's availability block and the payment entry effects repeat those checks before charging. Within `africa_rsa_can_pay_selected_purchase`, quote construction precedes the pending-receipt check. The pending-receipt and valid-quote checks both precede native resource affordability checks. No engine trace was returned to establish how often or in what order the UI invokes `available` versus `custom_cost_trigger`.

The sale branch depends on `black_friday_is_active`, `universal_cost_source_is_active`, and `black_friday_quote_custom_cost`. Native balances, source/evolution state, and the underlying quote/receipt APIs are external to the bounded source set. These factors remain unverified here.

## Regional support reply source audit

The current `africa_rsa_is_valid_regional_support_target` wrapper delegates the original polity and route predicates to `africa_rsa_is_eligible_regional_support_target`, then places the pending-donor exclusion inside an implementation-only `hidden_trigger`. The pending flag still gates eligibility, so this wrapper does not change AI or target semantics and avoids exposing the raw flag as a tooltip. The eligible helper checks the valid relationship target, both coalition event targets, non-SAF identity, absence of supporter/refused flags, no faction membership with the allied union government, and no war with the coalition. The parent reports AST equality between these moved predicates and the original target helper.

The donor-scoped `africa_rsa_pending_support_response_is_valid` trigger requires the pending flag, that shared eligible-target helper, the active civil-war flag, an existing coalition target, and an external-support count below the existing required count of two. Event `chaosx.nr12.1202` has exactly two local options: `.a` acceptance and `.b` refusal. The acceptance option calls this trigger through its custom trigger tooltip. The refusal option has no trigger of its own.

The paid request path confirms the purchase receipt first and queues the donor only when `africa_rsa_purchase_confirmation_result` is successful. A failed confirmation refunds instead of queuing. Queueing rechecks the valid-target wrapper, appends the donor to `africa_rsa_pending_support_requests`, sets the donor pending flag, and fires `chaosx.nr12.1202`.

The acceptance effect requires a pending flag and rechecks the response trigger before registering the donor. It sets the donor event target, calls the existing coalition registration helper, and sends equipment only if registration has set the donor's `africa_rsa_regional_supporter` flag. Registration records the response, checks donor eligibility, the two-supporter cap, and duplicate membership, then appends the supporter, updates the count from the array length, and sets the supporter flag. The shipment still uses `constant:africa_rsa_ratio.regional_support_transfer = 0.02`. The effect then releases the pending request, clearing the donor flag and removing its pointer from the coalition array.

The refusal effect also requires a pending flag, records the refusal and response if the coalition target exists, and releases the pending request. A duplicate or stale acceptance cannot reach shipment after the pending flag is cleared, and the registration helper independently rejects an ineligible or already-counted donor. If a crisis-ended event somehow retains a pending flag, acceptance is unavailable and rejected by the effect guard. Refusal remains available and can record a refusal before releasing the stale request, but it does not ship equipment.

`africa_rsa_clear_pending_support_requests` walks only the recorded pending-donor array, clears each donor's pending flag, then clears the array. The existing old-host cleanup, terminal-host cleanup, and continental-crisis cleanup call it. The scoped search found no direct `on_actions` reference to this cleanup helper or the pending array, so this repair does not introduce a daily scan.

| Qualified option | Physical before-source `ai_chance` | Current `ai_chance` | Source comparison |
| --- | --- | --- | --- |
| `chaosx.nr12.1202.a` | `base = constant:africa_rsa_ai.option_normal`, with `factor = constant:africa_rsa_ai.modifier_double` when `has_opinion = { target = FROM value > @CR_SC_AFRICA_RSA_AI_SUPPORT_OPINION_GATE }` | Same expression | Exact source-expression match. |
| `chaosx.nr12.1202.b` | `base = constant:africa_rsa_ai.option_minor` | Same expression | Exact source-expression match. |

The source constants resolve those bases to 50 and 25, and the doubled factor to 2. These are raw `ai_chance` weights, not normalized probabilities. The new eligibility gate can change which options participate, so unchanged weight expressions do not prove unchanged conditional choice behavior.

Classification: the baseline/current expression match is exact at source level and parent-reported AST level. The literal weights are score-only evidence. All scenario-specific option shares and native event outcomes remain unresolved.

## Required scenario matrix

All six purchase-scenario IDs and four reply-scenario IDs were supplied by the parent. No scenario was evaluated because the required inspect calls produced no result and the live tool schema exposes `scenarioSet` only as an opaque value. Inventing its inner fixture keys would violate the scenario contract.

| Scenario ID | Declared scenario intent | In-scope candidate completeness | External-factor completeness | Result and classification |
| --- | --- | --- | --- | --- |
| `ordinary_funded` | Ordinary quotes with all required components funded. | The five named RSA purchase IDs are complete only for the authorized audit slice. The actual decision race is incomplete. `africa_rsa_terminate_base_lease_early` is another decision in the same category, and the two target-array actions can expand to multiple country targets. Other live AI candidates are outside the authorized scope. | Incomplete: actual resources, route/target states, candidate universe, date, AI strategy inputs, and native decision-selection behavior were not bound to an accepted scenario fixture. | Unresolved. No score race or selection probability. |
| `baseline_sale_funded` | Baseline 50% sale case using the owner-declared prices above. | Same incomplete selection pool as `ordinary_funded`. | Incomplete: sale-source activation and timing, source validity, quote rounding, actual balances, target/route state, and other AI candidates were not represented in MCP output. | Unresolved. Declared prices are ledger data, not analyzer results. |
| `evolution_sale_funded` | Evolution I 75% sale case using the owner-declared prices above. | Same incomplete selection pool as `ordinary_funded`. | Incomplete: Evolution state, active source identity, timing, quote validity/rounding, actual balances, target/route state, and other AI candidates were not represented in MCP output. | Unresolved. Declared prices are ledger data, not analyzer results. |
| `each_component_below_payable` | Test each of the 11 positive component rows immediately below its payable quote. | The five in-scope IDs and 11 owner-ledger components are enumerated, but the overall selection pool remains incomplete. | Incomplete: no resource vector, sale state, component-boundary fixture, route/target state, or native fractional-resource binding was accepted by the analyzer. | Unresolved. No threshold or starvation result. |
| `invalid_target_or_route` | An invalid route or target should be unavailable and must not charge. | The five IDs are enumerated. Valid target instances and all competing decisions are not. | Incomplete: no exact country bindings, event targets, route flags, target validity, or resource inputs were supplied to MCP. | Unresolved. Source effects recheck route/target before payment, but no engine result. |
| `pending_receipt` | A pending receipt blocks another purchase. | The five IDs are enumerated. Full AI pool and target instances remain incomplete. | Incomplete: pending-receipt state and all other route/resource inputs were not bound in a valid analyzer fixture. | Unresolved. Source helper contains the guard, but no MCP or native proof. |
| `reply_valid` | A pending, still-eligible donor replies during the active crisis while the coalition is below its two-supporter cap. | Complete local event pool: `chaosx.nr12.1202.a` and `.b`. | Incomplete: donor/coalition scope bindings, event targets, flags, support count, opinion, and date were not accepted by MCP. | Unresolved. Source guards are present, but no conditional option result. |
| `pending_duplicate` | A stale or duplicate reply attempts acceptance after its pending request has been consumed. | Complete local event pool: `chaosx.nr12.1202.a` and `.b`. | Incomplete: duplicate delivery timing, pending flag, array membership, and actual event callback state were not bound to MCP. | Unresolved. Source guard and duplicate ledger checks are present, but no engine replay trace. |
| `cap_reached` | The coalition has already recorded two external supporters before a donor replies. | Complete local event pool: `chaosx.nr12.1202.a` and `.b`. | Incomplete: coalition count and donor/country bindings were not supplied to MCP. | Unresolved. Source makes acceptance ineligible and registration rechecks the cap, but no option share was evaluated. |
| `crisis_ended` | The civil-war flag has ended before a donor reply is resolved. | Complete local event pool: `chaosx.nr12.1202.a` and `.b`. | Incomplete: crisis flag, pending-array cleanup timing, donor flag, and event-popup timing were not bound to MCP. | Unresolved. Acceptance is source-blocked. Cleanup ordering and refusal-only stale behavior have no native trace. |

The five purchase scenarios have an incomplete full AI decision pool. The four reply scenarios have the complete two-option pool for event `chaosx.nr12.1202`, but their external campaign states remain incomplete. No exact or bounded selection probability is claimed for any scenario.

## MCP evidence and exact blocker

Live schemas exposed `hoi4_probability_inspect`, `hoi4_probability_evaluate`, `hoi4_probability_sweep`, `hoi4_probability_compare`, `hoi4_probability_render`, `hoi4_probability_simulate`, and `hoi4_probability_sequence` under `mcp__hoi4_agent_tools__`. Their availability in tool metadata did not establish a completed service response.

The adapter-and-candidate-list retry omitted `source` and returned this exact validation error: `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_inspect: An adapter requires a source; provide a source alone to discover compatible adapters`.

The initial source-bound request used the mod-relative object `{ path: "common/decisions/012_africa_rsa_decisions.txt" }` with `adapter = decision_ai_will_do` and `refresh = true`, but remained pending and was terminated after about two minutes. The narrower retries used the same source object alone, then with the five-ID candidate pool, and finally with only `africa_rsa_protect_civilian_corridor`. The source-only and five-candidate calls remained pending for multiple minutes and were terminated. The final single-decision retry remained pending for about 42 seconds and was terminated on the parent's request to finish the handoff under load. None returned a tool result, server error body, artifact, source revision, or scenario hash.

`probability_evaluate`, `probability_sweep`, and the mandatory `probability_compare` between the physical before-source and current candidate were not run because no inspect result defined the accepted scenario inputs. Guessing `scenarioSet` keys would be invalid. `probability_render` was not callable meaningfully because no retained analysis ID exists. No comparison ID or rendered evidence URI exists. The same service nonresponse is the exact blocker for the required probability pass. It is not evidence that the source is balanced or that the adapter supports these scripts.

The only reply-specific MCP route used was `probability_inspect` for `adapter = event_option_ai_chance` and source `events/012_africa_rsa.txt`. The source-only discovery request remained pending and was terminated without a result. The final bounded retry supplied the complete event-qualified pool `chaosx.nr12.1202.a` and `chaosx.nr12.1202.b`, remained pending for about 43 seconds, and was terminated without a result. No artifact, revision, scenario hash, or server error body was returned. No reply-option evaluate, sweep, baseline/current compare, or render result exists.

The parent reports two bounded `event_inspect` trace attempts for canonical event `chaosx.nr26.1`, one with two nodes and one with one node. Neither returned a result within its 20-second window. These attempts were not for `chaosx.nr12.1202`. The parent reports no reply-specific event-inspect trace artifact yet. No event render or structural artifact is available for the reply. Exact predicate and effect observations below are source review only, not event-chain MCP evidence.

`probability_simulate` was not appropriate because the parent declared deterministic scenario labels rather than distributions for uncertain inputs. `probability_sequence` was not appropriate because this is native decision selection, not a complete declared custom pool with cadence, transitions, and terminal state. No helper-expansion, job, native-task, or game-launch route was used.

The parent reports earlier source-level checks passed for 45 fresh text-trigger contexts and 75 invalid/pending/fallback contexts. The parent now reports that all 30 guard-focused checks and 295 purchase-bundle checks were rerun and passed, including AST equality for the moved target requirements and unchanged `chaosx.nr12.1202` `ai_chance` blocks. These are parent-reported results. This auditor did not run the tests, and they do not establish native AI option selection, resource mutation, rendering, replay ordering, or save/reload behavior.

The owner ledger records offline wiki references at Data structures lines 425-490, Localisation lines 680 and 729-791, and Decision modding lines 284-336, plus installed documentation citations for triggers, effects, and decision rules. The parent reports that `reference_context` reached its actual 600-second tool timeout and that a narrower reference retry returned no result within 20 seconds. No reference MCP artifact or revision is claimed by this audit.

For the event-option semantics, I read offline `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md` lines 153-159 (SHA-256 `96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D`) and `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md` lines 30-31 (SHA-256 `917CD261F7DA51FE4D8687C5D7663E768A09C5C101AC130CE646BC64637AA818`). They describe option triggers as availability gates and `ai_chance` as proportional option weights with a d100 resolution, distinct from decision `ai_will_do` score races. A targeted search of installed `documentation/` found no `ai_chance` semantics section. The closest installed entry is `documentation/effects_documentation.md` lines 3677-3679 (SHA-256 `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`), which documents `event_option_tooltip`, not option weighting. These local references explain the evidence distinction and do not supply scenario or engine-run results.

## Risk findings and recommendations

- **AI validity:** source checks keep route and target validation outside and inside the payment path, and affordability covers the concrete positive components. MCP validity over the requested scenarios remains unresolved.
- **Dominance and rank reversal:** source-only score changes are conditional as shown above. No numeric scenario race, dominance, or starvation conclusion is supported.
- **Repetition and cooldowns:** the diff leaves targets, route controls, and existing fire-once fields unchanged. Relief, citizenship, and exile are fire-once. Regional support and sovereignty rely on their existing activation, counters, route flags, and target filters. The probability tools did not establish actual repeated AI cadence or target exhaustion.
- **Regional reply replay and snowball:** queueing follows successful purchase settlement, the pending donor flag blocks another request, acceptance revalidates donor eligibility and the crisis/cap state, and registration checks the two-supporter cap and duplicate ledger membership before the unchanged 2% shipment. A consumed pending flag blocks another shipment. This is exact source behavior and parent-reported source-test coverage, not native replay proof.
- **Crisis-ended cleanup:** three explicit cleanup paths clear pending donor flags by traversing the pending array. If a stale request nevertheless survives, acceptance is blocked and refusal can close it without shipping. The MCP event trace did not establish lifecycle ordering in the engine.
- **Event AI option behavior:** both raw `ai_chance` expressions are unchanged, but the acceptance trigger now narrows eligibility. No conditional option share, refusal rate, or timing claim is supported without the probability pass.
- **Exploit risk:** the purchase helper verifies complete bundle affordability before debit and has receipt settlement/refund branches, but the shared native transaction APIs and save/reload behavior are outside the returned evidence. This is not a finding that the implementation is exploit-free.
- **AI saving hints:** keep the five stated ordinary-PP hints as the current conservative design unless the owner explicitly wants sale-sensitive AI behavior. Any hint or weight change requires a new baseline, matching named scenarios, and a successful `probability_compare`.
- **Required follow-up:** after the MCP probability route responds, inspect the exact decision and event sources and obtain accepted input schemas before constructing fixtures. Evaluate the six purchase scenarios and four reply scenarios, sweep each purchase-component affordability boundary plus the neighbor/faction and valid/pending/cap/crisis option gates, then compare each physical before-source against its candidate under the same named scenario set. Render comparison, ranking, and unresolved views from returned analysis IDs. Do not report selection probabilities until the analyzer confirms candidate-pool and external-factor completeness.

No numeric AI-weight or `ai_chance` fix is recommended from this incomplete probability evidence. The parent reports the decision snapshot byte identity is repaired in commit `f9f057581c080784b92ed14fd0a736f6f9708958` and will reverify its raw-byte hash. The event before-source still needs its pending no-filters commit. No source file was edited by this auditor.
