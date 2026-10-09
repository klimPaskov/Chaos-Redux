# Event 012 Gods industrial support owner helper implementation

Date: 2026-10-08.
Role: chaosx_scripted_system_architect, bounded patch-capable owner helper worker.
Disposition: implemented for the delegated new owner helper files, with parent integration and native acceptance open.
Acceptance basis: the explicit bounded implementation delegation and the parent's 2026-10-08 acceptance in `012_gods_industrial_tribute_design_2026-10-08.md`.
Repository: C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux.
The parent owns all existing gameplay integration files, final review and commit.
UI worker 01a11ac5-6943-7a50-a08d-978b6a8f5558 retains GUI/header presentation.

## Delivered files

| New file | Result |
|---|---|
| `common\scripted_effects\012_africa_gods_industry_effects.txt` | Seven public owner APIs, private original-scoped removal and measured transaction rollback |
| `common\scripted_effects\012_africa_gods_industry_effects.md` | Complete public/private helper map, scope/input/output/default/lifetime contracts, native limits and integration examples |
| `common\scripted_triggers\012_africa_gods_industry_triggers.txt` | Eight requested public triggers and eight private tuple/site/transaction proofs |
| `common\script_constants\012_africa_gods_industry_constants.txt` | Schema-first accepted repair/time/damage/capacity table and arithmetic negation factor |
| `common\dynamic_modifiers\012_africa_gods_industry_modifiers.txt` | +50% native state civilian-factory repair support with existing state-development icon |
| `.tools\validation\test_012_gods_industry_helpers.js` | Actual-source interpreter and 29 bounded contract scenarios |
| This handoff and `own_evidence\012_gods_industry_helpers_2026-10-08\` | Source scenario output, reference paths/spans/revisions, MCP reports/limits, recovered event image and source fingerprints |

Only these delegated new files and evidence files were written.
No existing source, localisation, category, AI, workbook, GUI, equipment floor helper, other mechanic, Git state, game process or MCP package was changed.
Public existing integration call sites remain with the parent by the explicit ownership boundary.
Private helpers have direct local production call sites.
No new global target, recurring hook, world scan, router or wrapper skill was added.

## Owner behavior implemented

The existing named industry family and base CPP quote remain authoritative, including the current base 20 and family constant rather than a literal family number.
Selection is host-local, prefers an eligible capital and otherwise picks maximum damage with first-encountered ties, and does not reserve a slot.
Binding occurs after demand epoch and ledger open, freezes the actual state/Q/D/actor/host/origin/generation/epoch/contract tuple, and reserves exactly one host record.
New-site damage is at least 0.50, with ownership/control/core/Africa and nonconsumed host project-factory capacity at least 1.
Existing unfinished-site payments require remaining damage greater than zero.
The pure full/partial wrappers calculate bare temporary amounts without changing any normal quote/family fields.
Every payment recomputes the legacy payer CPP reserve from its actual p and retains generation authorization.
Pre-contract budget eligibility never requires an active industrial receipt.

D is privately floored from 60 * Q / existing base quote and clamped to 30..120.
CPP remains exact, and cumulative paid service uses floor(D * min(C + p, Q) / Q) - G, with the final entitlement reserved for exact full funding.
New native time adds only the purchased increment to max(current day, previous due day).
G never increases from extensions, default, substitution or normal settlement.
The native duration remains finite even if the Gods owner clock stops.

The in-flight record precedes debit, includes the exact frozen tuple and pre-transaction C/G/due plus both native `has_political_power` snapshots, and blocks concurrent cleanup/binding.
Donor debit and receiver credit are independently measured and must both equal requested p.
Fresh authority/ledger/site/capacity proof and original-scoped native presence precede positive `payment_delivered`/`payment_received` outputs.
The helper never consumes the parent's remaining balance, creates compliance, credits materials or manufactures economic fulfillment.
Once C changes, C + unchanged remaining != Q prevents replay until the parent consumes the receipt.
Observed native/CPP failure rolls back only measured new money and the provisional current timer, preserving earlier C/G/due/sequence.
Failed rollback/restoration is unresolved evidence and blocks further payment.

Paid positive-to-zero damage observed during the native term creates the exact early-completion proof and removes the scoped modifier.
Its remaining CPP can settle without another program or new G.
Healthy unpaid sites, unobserved repair, and observations after recorded expiry supply no completion receipt.
Host-owned paid service survives donor annexation and financial close/default/substitution/normal secured-Africa settlement.
Host replacement, identity/epoch loss, capitulation or site ownership/control/core loss removes the original recipient-scoped modifier before clearing pointers.
Loss callbacks use a caller-supplied frozen expected five-field tuple and still work after revocation.
Late callbacks cannot retire a replacement contract.
Open expired partial records remain reserved, while closed expired/completed records are reclaimable through bounded retirement receipts preserving final funded/unpaid amounts.

## Parent integration checklist

The API's complete map, defaults, side effects and record symbols are in `common\scripted_effects\012_africa_gods_industry_effects.md`.
All helper symbols below carry the `gods_of_africa_` prefix.

1. In the existing host tick, call `review_industry_program` before need selection.
Use `industry_candidate_is_available` and `select_industry_site` for the physical industry candidate, keeping the existing need severity/ranking and payer budget profile.
2. After freezing the original quote, demand tuple, demand authority epoch and opening the contract ledger, call `bind_industry_terms` on ACTOR.
Do not advertise an industrial contract whose owner binding failed.
3. Add `industry_full_payment_can_execute` and `industry_partial_payment_can_execute` to existing human availability/cost gates and their existing AI consumers.
The full wrapper uses remaining and the partial wrapper uses the existing clamped precomputed amount.
Do not mutate normal payment quotes to evaluate these gates.
4. Give `gods_of_africa_host_can_receive_demand_payment` an explicit industry receiver branch using `industry_host_can_receive_payment`, and exclude industry from its generic non-fuel branch.
5. In `gods_of_africa_transfer_payment`, dispatch the named industry family to `pay_industrial_tribute` before generic political handling, with caller-set normal payment family/amount.
Read positive measured `payment_delivered` and `payment_received` once, then reduce demand remaining through its current owner.
Do not run the generic CPP debit/credit again.
6. Keep full/partial agreement, cooldown, mission deadline, history and reports with their existing owners.
Full original closure needs actual funded Q and earned paid support or exact early-completion proof, never a requested-amount assignment.
`industry_completion_is_proven` specifically proves early physical completion, and is not an unconditional full-funding predicate.
7. Call `finish_industry_contract` before clearing participant industry terms on successful full payment, accepted substitution, default, refusal, donor interruption and normal settlement.
Call `clear_industry_terms` from existing participant/demand cleanup.
These preserve host-owned earned support rather than removing it as a hostile loss.
8. Hook `retire_industry_program` into actual host/epoch/site-loss cleanup before original object pointers are destroyed.
Supply bare `gods_of_africa_industry_retire_host_id`, `_generation`, `_origin_host_id`, `_epoch`, `_contract_id` temps from the captured old callback/loss tuple.
Do not reconstruct a delayed callback tuple from the replacement's current record.
Read/copy bounded final funded/unpaid retirement evidence through the existing durable history boundary before later reclamation overwrites it.
9. Use the existing Gods CXT extension for inert readiness and fixtures, without damaging states, granting content, installing support or adding another carrier/hook.
10. Localise the native modifier and precise CPP/site/new-days/repair-speed/expiry terms through the existing parent/UI owners, retain existing icon wiring and material substitutions, update docs/workbook after integration facts exist, and finish the required audit comparisons.

The supplied ten-file baseline remains `012_gods_industry_implementation_2026-10-08_evidence\before\manifest.json`.
It was read to establish the delegated parent surfaces and immutable pre-edit identities.
This worker does not claim parent files remained unchanged while other owners worked.
No original payer reserve, numeric willingness factor, demand scaling, deadline, material substitute, original funding, or earned closed term was simplified.
No helper-design substitution or fallback was used.

## Meaningful source validation

Command: `node .tools/validation/test_012_gods_industry_helpers.js` from the mod root.
Final result: 29 cases passed, retained in `own_evidence\012_gods_industry_helpers_2026-10-08\source_scenarios.txt`.
The tests parse and execute actual new helper source rather than a separate arithmetic-only model.
They use conservative helper frames that remove newly created temps on return and retain caller-initialized forwarded outputs.
Native primitives and seven existing parent authorization predicates are explicit fixtures, with those boundaries listed in the output.
Existing decision/mission/ledger consumers and the parent integration are not mocked as completed implementation.

Coverage includes exact full and fractional CPP, contiguous partial time, partial after expiry, cumulative fractional-day conservation, replay with unchanged balance, below/exact/above legacy reserve, pure wrapper normal-variable immutability, no-site/capital/maximum-damage selection, each frozen scalar mismatch, site capture and post-preflight capture, host replacement and revoked cleanup, stale callback, capped receiver credit, short donor debit, first native failure, failed replacement restoring only the earlier interval, failed restoration leaving unresolved evidence, missing native support before expiry, in-flight cleanup rejection, early physical completion/remainder settlement, healthy/unearned/late completion rejection, donor annexation and closed-term conservation, single slot/day cap, removal failure retaining original pointers, zero-day purchase rejection, lost receiver capacity/wrong family, and closed-expired rebind preserving its bounded retirement receipt.

The first test pass found that its short-debit fixture also scaled rollback's negative host credit reversal.
The fixture was corrected to apply the injected debit shortfall only to the donor's native debit.
Testing also led to explicit guards that prevent participant finish/clear from erasing an in-flight binding and recheck authority/site/capacity before commit.
No test-loader failure was hidden with a no-op local helper.

## MCP and reference evidence

Exposed connected routes used read-only: `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup`, `event_inspect`, `event_render`, `decision_inspect`, `map_inspect`, and `script_validate`.
The event context returned both required source kinds with `omittedSources = []` and `missing = []`, and exact native/wiki rules were read separately.
No helper-expansion, job, negotiated native task, package write or game operation was used.
No connected version/health/task-negotiation claim is made.

Required native/wiki source citations and revisions are retained in `mcp_references_and_checks.json` and `coverage_and_limits.json` under this handoff's own evidence folder.
Important reads include installed effects 1153–1173 and 5978–5991, triggers 3775–3795, dynamic readers 431–434, 608–611 and 1118–1120, state repair modifier 4879–4886, script-concept constants 216–222, and the schema-first constants documentation 1–34.
Their parallel offline reads include Modifiers 149–181 and 1217–1220, Triggers 648, Data structures 1496, 1551 and 1676, plus local variable lifetime/scoping and localisation namespace sections.
Vanilla `ETH_international_red_cross_dynamic_modifier` and `ETH_state_development_dynamic_modifier` were directly read at installed `common\dynamic_modifiers\bba_dynamic_modifiers.txt:242–268`, current SHA-256 `f8147454267e43da91def4e1937ff56d67a2e09d98c78cc857e5d09d77763539`.
The bounded source lookup returned zero indexed definitions for the state modifier and was not treated as a matching precedent, with the direct vanilla read retained as source evidence.
The existing private equipment modulo/subtract pattern and existing shared dynamic-helper registry were inspected before implementing industry-private arithmetic.

Whole-file MCP script checks counted 350 effect and 225 trigger commands with zero unresolved command findings, but returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, unknown root scopes (9/16), unchecked argument blocks (151/98), and `parametersChecked = false`.
STATE-scoped add/remove/presence snippets separately matched documented native kind and declared scope, while their argument blocks remained unchecked.
Those results are command/reference evidence, not full semantic or engine validation.

Actual linked event is `chaosx.nr12.604`, verified in `events\012_africa_gods_of_africa.txt:80`.
The initial request incorrectly used `chaosx.nr012.604`, which is excluded from valid coverage and was corrected after exact source verification.
Corrected trace/render returned `EVENT_INSPECTED_PARTIAL` / `EVENT_RENDERED_PARTIAL`, focused analysis, helper count 0, and source revision `283a550085362183c930b3e9508acd4051d381fab0d6edd4f1b8afac59de6889`.
The corrected render selected the response event, option and terminal, which were visually read in the decoded 17204-byte PNG.
Its SHA-256 matched `99157c4d88cd0c6301d0b63bb9fbd65eca70204480811d773b73514ffa676b6d`, with a local copy in own evidence.
Its original PNG URI is retained in `actual_event_surface.json` and `coverage_and_limits.json`.
The manifest resource text failed JSON parsing at position 22533, despite declared 46902 bytes, so complete manifest/helper coverage remains unresolved.
No repeated observer loop or fabricated complete artifact was used.

Bounded map inspection returned `MAP_LOOKUP_COMPLETED` for illustrative state 275, revision `ca07e55d582bea0d42b950c6e4ae3a4ed6c2e901d0727f4e92309733b9f6a847`.
It is not a prescribed repair state or native damage observation, and requested no overview/full map validation.
Decision inventory returned `DECISION_ANALYZED_PARTIAL`, `complete = false`, zero declared scenarios and source revision `0a6f9e820a8abdcba68e79ef02b268a7e15783694d096f41742bcf2d3425594b`.
Its artifact reference and scope limits are retained, and it is not proof of integrated decision behavior.

## Simplifications, omissions, blockers and uncertainty

No gameplay-design simplification or fallback was applied within the delegated helper implementation.
Parent-owned integration, localisation, CXT, reports, docs/workbook alignment, GUI, audits and final commit were intentionally not edited under the explicit file boundary.
The parent receives working source helpers and tests, not a claim that the complete industrial mechanic is integrated.

`SourceNoNativeProof` explicitly covers native CPP numeric precision/caps, exact native timer refresh/restoration/expiry and real repairs/queue assignment.
Native presence alone cannot establish expiry, an extension's duration, or actual repairs.
One passing source scenario deliberately demonstrates the unsupported case where a native refresh fails while an old modifier remains present, so requested extension cannot be independently proven from the documented presence trigger.
Observed absence/native installation failure still triggers measured rollback, while this indistinguishable refresh case remains native acceptance uncertainty rather than a fabricated reader or fallback.
Damage observations prove a paid supported site's result, without proving what share of damage the program caused.

The test's native expiry is a modeled primitive grounded in documented finite days, and is not observed engine execution.
Parent integration tests with real existing consumers are skipped here because those consumers are outside this worker's ownership and still pending parent wiring.
Matching AI baseline/after comparison is pending the parent's `chaosx_ai_probability_auditor` after changed eligibility is wired, preserving the supplied before sources and named scenarios.
This worker implements no weighted helper, AI number, MTTH, random selection or probability-bearing modifier and performs no AI rebalance.
Full event-chain comparison/helper lifecycle coverage remains with the parent because focused evidence omits helpers and this patch does not own the existing integration chain.
GUI before/after acceptance remains with its assigned UI owner, and native acceptance remains with the user.
The exact manifest retrieval limit and partial script-validation fields are preserved instead of claiming equivalent engine proof from source tests.

Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or changed.
Completed work is the reusable owner helper patch, documented API, bounded native modifier/constants, source scenarios and explicit evidence handoff.
Remaining work is the parent's concrete integration checklist, its same-scenario audits, final review/commit and the native acceptance limits above.
