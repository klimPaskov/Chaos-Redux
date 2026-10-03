# Event 012 Victor Authority and Renewal AI Probability Audit

Date: 2026-10-03

Status: Source review is complete for the scoped decision rows and their directly connected Victor eligibility/effect helpers. The weighted scenario result is unresolved because the connected probability adapter returned no usable decision candidates or scenario inputs, and the retained parent artifact could not be read. No gameplay source, Git state, or game runtime was accessed or changed. This handoff is the only authorized file written.

## Scope and source files

Weighted surfaces:

- Participant decision `gods_of_africa_seek_reconciliation`, including the Victor renewal request branch.
- Participant decision `gods_of_africa_return_to_demand`, including the Victor withdrawal branch.
- Host target decision `gods_of_africa_accept_reconciliation`, including current Victor consent.
- Host target decision `gods_of_africa_reject_substitute`, including current Victor rejection.

Current source paths, reviewed blocks, and local raw SHA-256:

| Source | Relevant blocks | Local raw SHA-256 |
|---|---|---|
| `common\decisions\012_africa_gods_decisions.txt` | `gods_of_africa_return_to_demand` lines 334-363; `gods_of_africa_seek_reconciliation` lines 523-552; host `gods_of_africa_reject_substitute` lines 970-1009; host `gods_of_africa_accept_reconciliation` lines 1066-1107 | `6D6FB4A7EFC3750CE15A4925FFEEB4B42A38B689A9EC345F045FD78944ECF0F0` |
| `common\scripted_triggers\012_africa_gods_victor_triggers.txt` | `gods_of_africa_victor_relationship_is_available` lines 34-49; `gods_of_africa_victor_renewal_is_current` lines 51-64; `gods_of_africa_victor_can_request_relegitimation` lines 66-74; `gods_of_africa_victor_renewal_can_withdraw` lines 76-81 | `15CD0DA2CA86198D24AB81848570ECCEFF1E2B02B5C55B3FA512DDF51E912916` |
| `common\scripted_effects\012_africa_gods_victor_effects.txt` | `gods_of_africa_request_victor_relegitimation` lines 74-86; `gods_of_africa_commit_victor_relegitimation` lines 88-115; `gods_of_africa_withdraw_victor_relegitimation` lines 117-122; `gods_of_africa_reject_victor_relegitimation` lines 124-141 | `52D057F8487BF0A7C57EA0CE338992DCE875C31D5EECB3A1386D847E3732373A` |
| `common\scripted_triggers\012_africa_gods_triggers.txt` | `gods_of_africa_participant_generation_is_current` lines 163-177; `gods_of_africa_participant_can_register` lines 179-191; `gods_of_africa_participant_has_active_demand` lines 200-215; `gods_of_africa_demand_contract_is_current` lines 217-230; `gods_of_africa_participant_can_reconcile` lines 552-564; `gods_of_africa_reconciliation_can_be_paid` lines 1057-1067 | `44AE3D2BA45E9995B015703124E043130A07DF4888B879FBC0C1A78DF9A8B810` |
| `common\scripted_effects\012_africa_gods_effects.txt` | `gods_of_africa_reject_substitute` lines 2165-2197; `gods_of_africa_return_from_negotiation` lines 3723-3749; `gods_of_africa_seek_reconciliation` lines 3807-3826; `gods_of_africa_accept_reconciliation` lines 3831-3843 | `EA62D37F38E9C3F19C1C9BE6E6A483281F7358D93998028176B87C6349096A2F` |

Decision identifiers reviewed: `gods_of_africa_seek_reconciliation`, `gods_of_africa_return_to_demand`, `gods_of_africa_reject_substitute`, and `gods_of_africa_accept_reconciliation`.

Connected helper identifiers reviewed: `gods_of_africa_victor_relationship_is_available`, `gods_of_africa_victor_renewal_is_current`, `gods_of_africa_victor_can_request_relegitimation`, `gods_of_africa_victor_renewal_can_withdraw`, `gods_of_africa_request_victor_relegitimation`, `gods_of_africa_commit_victor_relegitimation`, `gods_of_africa_withdraw_victor_relegitimation`, `gods_of_africa_reject_victor_relegitimation`, `gods_of_africa_participant_generation_is_current`, `gods_of_africa_demand_contract_is_current`, `gods_of_africa_return_from_negotiation`, and `gods_of_africa_accept_reconciliation`.

The supplied change note says the four AI bases were preserved from baseline `b609837d9`. Current source confirms the literal values below. Git was explicitly out of scope, so the historical source and that baseline assertion were not independently compared.

## Current AI values and source traces

All four in-scope `ai_will_do` blocks are literal-base-only blocks with no modifier clauses.

| Decision | Scope and phase | Base | Source-level gate and trace | Result class |
|---|---|---:|---|---|
| `gods_of_africa_seek_reconciliation` | Participant; request | 10 | Visible for `gods_of_africa_victor_can_request_relegitimation` or the older defiant reconciliation path. Availability calls `gods_of_africa_reconciliation_can_be_paid`; its Victor branch accepts the request gate without a political-power check. When the renewal is already current, the request gate fails, so the pending Victor offer hides this decision. | Score-only; scenario outcome unresolved |
| `gods_of_africa_return_to_demand` | Participant; withdraw/return | 5 | Visible and available through `gods_of_africa_victor_renewal_can_withdraw` for a pending Victor request, or through the older active negotiation/demand gates. The Victor request and withdrawal decisions are phase-separated: the current request gate excludes a current renewal, while withdrawal remains visible. | Score-only; scenario outcome unresolved |
| `gods_of_africa_accept_reconciliation` | Active host; target `FROM` participant | 4 | `target_array = gods_of_africa_candidate_registry`. The target and available gates accept a current Victor renewal or the older paid-reparations/pending-offer case. The target-root gate requires a valid active host. The shared effect dispatches current Victor consent to `gods_of_africa_commit_victor_relegitimation`. | Score-only; scenario outcome unresolved |
| `gods_of_africa_reject_substitute` | Active host; target `FROM` participant | 1 | `target_array = gods_of_africa_candidate_registry`. The target and available gates accept a current Victor renewal or the older pending substitute case. The target-root gate requires a valid active host. The shared effect dispatches a current Victor offer to `gods_of_africa_reject_victor_relegitimation`. | Score-only; scenario outcome unresolved |

For one current Victor target, accept has four times the literal base of reject. That is only a raw score comparison between these two rows; it is not a 4:1 probability claim, and it does not rank the complete host decision pool. Request and withdrawal are different participant phases, and their 10 and 5 bases are not a coavailable race while the request is current.

The offline wiki describes decision `ai_will_do` as an MTTH-style AI score and says that the AI commonly draws a value between zero and the resulting score and chooses the highest-scoring entry. It separately describes event `ai_chance` as probability-proportional-to-size sampling. Therefore these bases are score evidence, not normalized click probabilities or event-option probabilities. The installed-game decision documentation confirms that targeted decision `visible`/`available` use the acting country and target scopes, and that `target_root_trigger` and `target_trigger` separate the acting-country and target-country checks.

## Victor eligibility and effect findings

The current relationship gate requires a live participant, an active host, the recorded/exempt Victor state, consistent history ownership, a positive victory count, and a matching origin-host identity. A current renewal additionally binds the request to the active host id, host generation, origin-host id, and Victor victory sequence, and rejects a request while the participant is at war with the host or holds a host core state.

A new request first clears prior request and rejection-report state, stores the active host/generation/origin/sequence tuple, and sets `gods_of_africa_victor_renewal_requested`. This Victor branch does not deduct political power and does not grant a numeric recognition value in the inspected request/commit blocks. Host acceptance records the relegitimation history, clears `gods_of_africa_victor_exempt`, clears the request, and registers the participant. Host rejection records a rejection, clears the request, and leaves the Victor exempt. Withdrawal clears the request.

The ordinary participant-generation predicate explicitly rejects `gods_of_africa_victor_exempt`. Current active-demand and demand-contract predicates depend on that generation predicate, and participant registration also rejects exempt Victors. The existing demand mission cancels when the participant generation is no longer current. This supports the source-level boundary that ordinary demand eligibility and its generation-bound response/mission path remain closed until host acceptance clears the exemption. This audit did not trace every unrelated scheduler or punishment consumer.

## Scenario inventory and completeness

The following scenario ids were supplied for this audit. They are named here but were not evaluated because the live probability route supplied no complete phase pool or typed state fixtures. Every row is unresolved; no scenario hash exists.

| Scenario id | Candidate-pool completeness | External-factor completeness | Result |
|---|---|---|---|
| `COOPERATIVE-AFFORDABLE` | Incomplete; the adapter did not return the actual eligible response pool. | Incomplete; exact actor/host/target state, scope `FROM`, active-host binding, and affordability inputs were not supplied to the connected route. | Unresolved |
| `HARDSHIP` | Incomplete. | Incomplete; the scenario’s hardship/resource values and active offer state were not available as typed inputs. | Unresolved |
| `GAMBLER-WEAK-AFRICA` | Incomplete. | Incomplete; the exact actor/host state and the scenario’s Africa-strength inputs were not available as typed inputs. | Unresolved |
| `OCCUPIER` | Incomplete. | Incomplete; the target’s war, host-core, control/occupation, and current relationship state were not available as typed inputs. | Unresolved |
| `LOYAL-ALLY-EMERGENCY` | Incomplete. | Incomplete; ally/loyalty/emergency state, current host identity, and full target roster were not available as typed inputs. | Unresolved |
| `ABUSIVE-AFRICA` | Incomplete. | Incomplete; the exact host/participant state, abuse indicators, and eligible alternatives were not available as typed inputs. | Unresolved |
| `VICTOR-REQUEST` | Incomplete. | Incomplete; the current participant/host/origin/generation/victory-sequence tuple and full participant response pool were not supplied in a supported scenario object. | Unresolved |
| `VICTOR-HOST-CONSENT` | Incomplete; the actual candidate-registry targets and other coavailable host decisions were not exposed. | Incomplete; active host ROOT, target FROM, current request tuple, and candidate eligibility state were not supplied. | Unresolved |
| `VICTOR-WITHDRAWAL` | Incomplete; the participant decision pool and simultaneous host-consent alternatives were not exposed. | Incomplete; actor state and relative participant/host decision cadence or ordering were not supplied. | Unresolved |

The inspector’s 36 source candidates are a file-level discovery result, not a complete live host/participant response pool. No exact, bounded, or sampled selection probability is supported.

## MCP evidence and blockers

The current broad read-only probability inspection succeeded for `decision_ai_will_do` on `common/decisions/012_africa_gods_decisions.txt`.

- Status: `PROBABILITY_SOURCE_INSPECTED`.
- MCP source hash: `1692058d825b8bf3cd581548b0fc46c1662605ed5799a709f4d2cdca18863b13`.
- MCP source revision: `1155e4f693b48a16b0390c57c7fb5925ef4b6a47f46033002e77d7a571467167`.
- Discovery result: 36 candidates; `poolComplete = false`; zero available candidates; `availableAdapters = []`; one required input path, `scope.FROM`; unresolved count 0 in the discovery summary. The zero unresolved diagnostic count does not establish scenario or candidate-pool completeness.
- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a093ea916bebe5ef8ca20c5f23859e99c742ac0fb7603335e6e347edf31c98b9/e2b5d87c50fd4363bad4640fb26974c9621e0b48ba4f70eb70dd83b905b6ddb7/probability-inspect-1692058d825b.json`; size 974,461 bytes.

Parent-provided narrow inspection evidence for `gods_of_africa_comply_demand` is retained separately and is not treated as the Victor response pool: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21ad033f9112906fa89e8047c0d243f265b43ea68a025e97913a91a0cf59b0e/562e2196a5615e2668e9d6de3a1a2968584de13f10a600268a62ae16d13b6b8a/probability-inspect-13931a6bc7f7.json`, reported size 105,638 bytes, source hash `13931a6bc7f76d7f82a804f9c515f33844aaa9c2ca6809fb8e93b6df109b8860`, source revision `76c94f3ddda8d7094decf523eb3a1a1ecb3fe9f019e6f49f5d15c8c78072e679`. Its pool contains only `gods_of_africa_comply_demand`; the parent explicitly reports that this is not the complete response pool and is not evidence of AI acceptance.

The parent reports that four bounded reads of that retained artifact failed with `-32603: Artifact provenance manifest is unavailable`. This client’s `list_mcp_resources` returned no resources. The current broad inspection’s compact result is available, but its full artifact was not consumed.

A read-only `hoi4.decision_inspect` call was attempted for each of the four named decisions. All four were rejected before analysis with `-32602: Decision inspection requires declared scenarios at scenarios`. No scenario fixtures were invented to bypass that validation requirement.

A read-only `hoi4.probability_render` attempt used the exact retained inspector filename stem `probability-inspect-1692058d825b` and requested the unresolved view. It failed with `PROBABILITY_ANALYSIS_NOT_CACHED`: the renderer requires a retained analysis id from this authorized workspace. No rendered artifact was produced.

`hoi4.probability_evaluate` was not run because the scenario names lack supported typed state inputs and the inspected adapter exposed no available candidates. `hoi4.probability_sweep` was not run because there is no complete candidate pool or evaluable scenario baseline from which to sweep thresholds, sensitivity, or rank reversals. `hoi4.probability_compare` was not run because no exact before-source artifact or proposed after-source is available in scope; comparing the current source to itself or comparing a cached analysis identifier would be invalid. `hoi4.probability_simulate` was not run because no uncertain-input distributions were declared. `hoi4.probability_sequence` is out of scope because this is not a manifest-declared custom pool with cadence and transitions.

Reference evidence:

- Installed decision documentation: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md`, lines 1-46; reference id `c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`. The cited section defines the target and acting-country scopes for `visible`, `available`, `target_root_trigger`, and `target_trigger`.
- Offline decision-modification wiki: `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`, AI section lines 357-374; reference id `151bbd3b6a875558e43f67a1daa1288c5904dfbedfa09e3fca2e5e42b8ccc58f`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`. This identifies decision `ai_will_do` as an MTTH-style AI score block.
- Offline AI-modification wiki: `paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md`, MTTH section lines 26-37; reference id `ab2b62a1e95fe5c84560ceedca6723cea6918faf69b08fd399709a2afbf8efe6`, revision `917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818`. This distinguishes highest-score `ai_will_do` evaluation from event `ai_chance` probability-proportional sampling.
- The `chaos-redux-mtth` skill was read because the offline decision reference classifies `ai_will_do` as an MTTH-style block. The four source rows use direct literal bases; no named `mtth:` entry or custom timing distribution is involved.

## Risk findings

- **Eligibility:** The request gate closes while a current Victor request exists. Host accept/reject are gated by the current request helper and an active-host ROOT gate. These are exact source findings; live target discovery remains unresolved.
- **Withdrawal validity:** `gods_of_africa_victor_renewal_can_withdraw` checks existence plus recorded/exempt/requested flags, but does not itself check active host, request host id, generation, origin, sequence, war, or host-core state. `gods_of_africa_return_to_demand` remains visible/available through this helper. This permits clearing a stale request flag; whether that is intentional cleanup behavior is unresolved.
- **Host consent:** Accept and reject are both valid for a current renewal on the host’s target decision surface. Their raw bases are 4 and 1. The adapter did not prove that those are the only coavailable host choices.
- **Dominance/starvation/rank reversal:** Unresolved. No complete candidate list or modifier trace was returned, and no sweep ran. The local blocks have no inline modifiers, but the adapter did not establish absence of external strategy factors or other engine context.
- **Withdrawal timing risk:** Participant withdrawal has base 5 while the host accept/reject rows have bases 4/1. These act in different country scopes and must not be compared as one score race. Source permits the participant to withdraw while the host offer is pending; actual cross-country AI cadence and whether withdrawal beats host consent are unresolved.
- **Repetition:** The request decision has `fire_only_once = no`. Host rejection clears the current request while retaining Victor exemption, and a later request clears the pending rejection report state. Repeated request/rejection cycles are structurally possible. Whether the AI will repeat them, and at what cadence, is unresolved.
- **Exploit/snowball:** The Victor request itself is free and the host’s acceptance is also cost-free. Acceptance restores ordinary participant eligibility, so subsequent demand behavior can resume after the explicit host milestone. No separate numeric recognition gain is present in the inspected commit block. This source path alone does not establish abusive campaign impact.
- **Hardcoded tuning:** The 5, 10, 1, and 4 bases are literals. Their intended balance is not selected by this audit. Scenario testing and any later centralization should follow an owner-chosen target and a valid baseline/compare workflow.

## Recommended follow-up, not applied

1. Have the probability-capable parent route re-run inspection on the four exact decisions with a supported typed scenario schema, full `scope.FROM` bindings, active-host ROOT, current host/generation/origin/victory-sequence values, relevant flags/war/core state, and the complete candidate roster for each phase. Preserve the returned artifact before attempting evaluate or render.
2. Ask the mechanic owner to decide whether a Victor may withdraw after the request’s host/generation/origin/sequence ceases to be current and whether AI withdrawal should remain available throughout host consent. If not intended, align `gods_of_africa_victor_renewal_can_withdraw` in `common\scripted_triggers\012_africa_gods_victor_triggers.txt` with the current-request predicates, then compare the same named scenarios.
3. Ask the owner whether repeated requests after rejection are intentional. If not, add an owner-approved cooldown or attempt gate to `gods_of_africa_victor_can_request_relegitimation` and preserve the desired rejection-report lifecycle in `common\scripted_effects\012_africa_gods_victor_effects.txt`; re-evaluate request and host-consent phases.
4. Keep the four bases unchanged until a complete baseline and scenario evaluation can support a balance decision. No numeric target is recommended here.

## Omitted work and remaining uncertainty

- No supported scenario evaluations, sweeps, or source comparisons were produced.
- No exact selection probability, rank-reversal result, starvation result, sampled estimate, or timing distribution is claimed.
- The supplied historical baseline assertion was not checked with Git because Git was forbidden.
- No event `ai_chance`, event MTTH, random-list, focus, research/doctrine, AI-strategy-factor, or custom-pool surface was included in this bounded decision audit.
- No gameplay change, test, Git operation, game launch, or file outside this handoff was performed.


## Skills and source identity note

Skills read and applied: `.agents\skills\chaos-redux-subagents\SKILL.md` for audit ownership and evidence requirements; `.agents\skills\chaos-redux-decisions-missions\SKILL.md` for decision AI behavior and balance review; and `.agents\skills\chaos-redux-mtth\SKILL.md` because decision `ai_will_do` is documented as an MTTH-style score block. No skill was created or updated. Event-specific skills were out of scope because no event option, event MTTH, random event, or random-list weight was audited.

The local SHA-256 values above are raw filesystem digests. The MCP `sourceHash` and `sourceRevision` values are recorded as returned, but the connected response does not define their hash domain. The retained artifact could not be opened, so equality between the MCP source snapshot and local raw bytes remains unverified.
