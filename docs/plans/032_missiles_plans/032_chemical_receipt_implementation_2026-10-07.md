# Event 032 chemical receipt implementation, 2026-10-07

Disposition: `implemented` for the chemical reservation and custody source; final Event 032 acceptance remains unresolved.
Acceptance basis: the user requires real special-payload preparation, once-only payment, exact site custody, physical capture/loss settlement and shared CBRN consequences under the complete accepted Event 032 specification.
This is not a completion claim for the event or the supplied three-error live QA report.

Published implementation commit: `5793df4345a413dcf7cadf5aeae99597a859020a`, containing 103 owned paths, including exact before-source snapshots and permanent icon provenance.
The 43-test chemical receipt suite also passed against a 28-file read-only export of the isolated proposed tree, independently of the other agents' uncommitted split changes.
All 19 indexed probability snapshots were checked as raw Git blobs against their recorded SHA-256 hashes, with path-local attributes preserving their bytes.
The first post-publication index reconciliation used a PowerShell text pipe that Git silently ignored; it was repaired with raw UTF-8/NUL input, rehearsed from the parent tree and verified against all 103 expected entries before handoff.
No working files were reset, no lock was removed and unrelated staged/unstaged ownership was preserved.
The shared-commit skill records that reusable transport pitfall.

## Gameplay changes

Chemical preparation debits the exact prepared-air equipment through the CBRN-owned measured reservation API.
Each receipt freezes holder, consumer, operation nonce, agent, model, route, source and target; duplicate requests cannot create a second payment or release.
Partial debit, partial refund and untrustworthy native observations remain explicit held/pending/quarantined records rather than nominal successful payments.
Consumption revalidates the full hold and current authorization, then closes the held quantity without requiring or debiting a replacement free stockpile.
The operation supplies its frozen paid agent and quantity to the existing protection, exposure, Deaths, Air Cleanliness, evidence and Condemnation pipeline.
The missile owner creates no world-end branch.

Cancellation returns material only from a recoverable controlled source.
Capture transfers sealed stock to the actual controller without native credit, technology or profile grants; integration requires the exact original profile and present technology.
Proven destruction discards the held quantity, isolation retains it, repair and recovery retry valid returns, and country removal settles physical custody before clearing the missile registry.
Loss of a different barrage participant does not destroy or transfer payload held at the intact primary site.
Shared chemical profile changes cannot relabel held material, and stockpile inspections and proportional destruction include already-reserved quantities.
Quarantined stock cannot earn a completed compliance acknowledgement.

Country totals use selected-receipt deltas rather than a periodic registry recount.
Site settlement freezes matching handles before retiring entries and initializes private loop-break fields.
The follow-up audit's frozen-site identity mismatch and inherited-default-break findings were repaired and tested.
Rejected commitment also runs operation cleanup, and the preparation-failure record distinguishes an invalid chemical receipt.

## Ownership and tests

The API contract, files, inputs, outputs, examples and native limitations are in [Chemical payload reservations](../../systems/cbrn_warfare/chemical_payload_reservations.md).
The [native primitive handoff](subagent_handoffs/032_chemical_native_primitives_2026-10-07.md), [receipt review](subagent_handoffs/032_chemical_receipt_review_2026-10-07.md) and [source-execution tests](subagent_handoffs/032_chemical_receipt_tests_2026-10-07.md) were reviewed by the parent.
The parent reran 43 actual-source receipt/quote tests, covering all nine chemical agents, four stock models, matching replay, changed identity/authorization, measured partial and invalid I/O, sealed capture, foreign-ROOT return, exact-site settlement, profile locks and sanctions destruction.
The source-execution fixture also checks the real selected-payload affordability predicate for all four biological agents and both nuclear families, including missing stock or technology and an unresolved earlier chemical hold.
The Event 032 source-contract suite passed 139 tests, including the removal-loop regression in the ten-test special-payload module.
These tests use explicit native/world leaves and conservative helper-temporary lifetime; they are not observations from Hearts of Iron IV.
Full consequence dispatch, broad operation orchestration, physical callback evidence, native variant/producer identity, save persistence and large selected receipt queues are separate evidence limits.

No recurring world scan or direct recursive launch was introduced.
The existing nuclear and biological escrow still need their separate physical-custody audit; their capture/refund semantics are not established by this chemical work.
Special preparations replace the support-equipment fee with their real payload, preserving the four-resource limit while leaving every CP, fuel, missile, payload quantity and numeric AI weight unchanged.
The three-value inline row and full four-resource tooltip share the live availability predicates and owner constants.
The read-only probability auditor preserved before-source bytes and ran the named baseline before this patch; unresolved model inputs do not establish AI parity or campaign balance.
The reviewed [cost-probability handoff](subagent_handoffs/032_preparation_cost_probability_2026-10-07.md) records AI and human comparison attempts for `COST-01` through `COST-06`: each side has 24 excluded rows and 520 unresolved inputs, not a passing parity result.
The final compare uses identical saved inputs on its two sides, but the original pre-edit evaluation object was not saved and its exact hash continuity is lost; helpers also resolve from the current workspace rather than the full frozen dependency closure.
The fixture supplies an archetype-level chemical stock value while the receipt quote reads a concrete prepared-lot model, adding a specific stock-input gap to the incomplete program, date, technology and scope bindings.
No numeric rank, click probability, historical helper delta or complete same-baseline probability pass is claimed.
Both shared payload-cost icons are produced, parent-reviewed at native and 4× sizes, and wired at the exact declared paths.
Chemical art retains its canister silhouette; the biological cost uses the approved standard hazard pictogram after the initial vial request was refused.
The native ImageGen route and alpha were preserved, with no alternate backend or local-drawing fallback; earlier refusals and rejected candidates remain in the [asset handoff](subagent_handoffs/032_payload_cost_icons_2026-10-07.md).
No gameplay simplification or excluded asset family was introduced.
The 82-file earlier event asset audit was not rerun wholesale for these two shared additions, and live decision-row text fit remains unverified.

## MCP evidence

The connected server reports version `3.10.0`; native task negotiation and whole-helper lifecycle coverage were not assumed.
The three new receipt files returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, no reported file findings and unchecked native parameter blocks: 401 commands/233 argument blocks/15 unknown-scope roots for the CBRN effects; 108/46/7 for the Event 032 adapter; and 24/6/2 for the Event 032 predicates.
Explicit COUNTRY/STATE snippets then retained scope-specific results in [032_chemical_receipt_mcp_2026-10-07.json](032_chemical_receipt_mcp_2026-10-07.json).
Their omitted findings and unresolved helpers, dynamic scope bindings and native argument blocks are not full engine proof.
The exact loop, variable, comparison, model-token and native stock syntax was reviewed against the installed documentation and offline wiki revisions retained by the primitive and test handoffs.

An exact `.83` trace returned `EVENT_INSPECTED_PARTIAL` with zero helper coverage, revision `2c3d335e60864d8c0eaddccd379909409538d05e04c6cad5a4fb28c73a521a18` and graph hash `1e80464bb8b2bb7b6158f2fdf776922c197ced860885684a5ac38610309072b1`.
The matching scope render returned `EVENT_RENDERED_PARTIAL` but selected zero nodes and therefore establishes no operation-chain coverage.
Its authoritative JSON was retrieved in two byte ranges and verified at 44,905 bytes with SHA-256 `5d2e7ec255f3cbda6e2fb65ce33a41dc8a9bd134e6e266b66cf962b592349ba7`.
`hoi4.source_lookup` separately found `chaosx.nr32.83` at `events/032_missile_crisis.txt:513–526`, source-index revision `0c77eed119af3b502060e989c461c5b1c733b0dcb80470f80204f16c88d2a13c`.
The discrepancy is a domain selection/coverage gap, not a missing event or successful render review.
Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d2e7ec255f3cbda6e2fb65ce33a41dc8a9bd134e6e266b66cf962b592349ba7/858f81c8fc540d2ac0eec2cba96d59e35e77866940d2e4be5b8e1e9ef37468b9/event-scope-2c3d335e6086.json`.
Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d36290189ee0f3500cee99fb66c43a5a9b15dd8a241974ac80017b6adb7cb28/d9132ee2c4f146160565fe40054953758d53694df2001361c0c90f3ba307f173/event-trace-2c3d335e6086.json`.
The complete trace resource was not retrieved; its full inventory and findings remain unreviewed.
The event compare against cached revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0` failed with `EVENT_REVISION_NOT_CACHED`.
The narrower one-node artifact-backed retry failed with `ARTIFACT_NOT_FOUND: Artifact provenance manifest is unavailable`.
Neither result establishes before/after graph behavior, and no self-comparison was substituted.

## Live QA and remaining goal

The supplied STATE `exists` and undefined-target clears were repaired in `480d757f3d89a911c52df4d156c17cbde3325096`.
Duplicate native ID `1028 4713` remains unattributed after source forensics; the temporary allocation markers remain and no clean live error log is claimed.
The [current contract reconciliation](subagent_handoffs/032_current_contract_reconciliation_2026-10-07.md) retains the other accepted work and validation gaps.
No requirement is rejected or weakened by this tranche.
Other agents' civil-war split implementation and unrelated shared-index changes are outside its commit ownership.
The related Event 021 claimant-split suite was run against the shared working source and passed 11 tests; its uncommitted test and split implementation remain owned by that agent and are not included in this commit.
The reusable private-loop-break rule is captured in the events skill reference; its examples distinguish documented while/for limits from unverified foreach ceilings.
