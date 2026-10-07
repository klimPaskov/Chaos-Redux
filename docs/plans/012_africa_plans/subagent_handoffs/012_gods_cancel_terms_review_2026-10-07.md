# Event 012 Gods cancellation terms: bounded independent review

Date: 2026-10-07.
Disposition: bounded source review completed with no blocking regression found; final guard correction verified and the earlier placement finding resolved.
MCP helper-chain coverage and native execution remain unresolved.
This is neither native validation nor completion of Gods of Africa or Event 012.

## Authority and reviewed identity

Acceptance basis is the supplied parent instruction: cancel ordinary demands, pending punishment, participation and current authority on loss while retaining accepted durable conduct, measured contributions, contract/history records and historical settlement/victor receipts.
Only this handoff was written by the reviewer.
No gameplay, weights, decisions, GUI, assets, workbook, other documentation, Git state or game process was changed.
The independent decision auditor retains action-surface review; expanded primitive `hoi4.script_validate` remains parent-owned.

Repository root: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Source paths below are relative to that root and line references describe the reviewed version.
Read guidance: `AGENTS.md`, `.agents\skills\chaos-redux-events\SKILL.md`, and `.agents\skills\chaos-redux-subagents\SKILL.md`.
Read source contracts: `docs\events\012_africa\gods_of_africa.md`, `common\scripted_effects\012_africa_gods_contract_effects.md`, and relevant recovery ownership/cleanup sections of `common\scripted_effects\012_africa_gods_recovery_effects.md`.
The shared dynamic-effect registry overview confirms this cleanup belongs with the event-owned helpers; no new generic helper or router is proposed.

The exact baseline file is `C:\Users\klimp\AppData\Local\Temp\gods_cancel_terms_before_20261007\012_africa_gods_effects.txt`.
Its SHA-256 was verified as `f9fcb0d37264ebe6b10e64ca8b774226c17804170fae194bf616f4155aa00d51`.
The final independently rechecked `common\scripted_effects\012_africa_gods_effects.txt` SHA-256 is `720f1cb91a1c36e73254954f08b08bd5e2b241770b022d310aaea16b8b6d9332`.
The exact whole-file diff is confined to `gods_of_africa_cancel_participant:4505-4606`, with baseline hunk starts `4505`, `4512`, and `4570`.
Cancellation at `4520` is `if = { limit = { has_active_mission = gods_of_africa_demand_mission } remove_mission = gods_of_africa_demand_mission }`.
Archival at `508` is restored to its baseline `remove_mission = gods_of_africa_demand_mission`; no archival difference remains against the supplied baseline.

| Dependency | SHA-256 |
| --- | --- |
| `common\scripted_effects\012_africa_gods_contract_effects.txt` | `17b88c923b129683f0233e6d2fac28f6406faf1ef386a4dc5718e97a37899f1f` |
| `common\scripted_triggers\012_africa_gods_contract_triggers.txt` | `c16f211f191c8b689da5c10c8591f7380892256dd5920e62f9b578cf0b196a6e` |
| `common\scripted_effects\012_africa_gods_instalment_effects.txt` | `3f1e4e577dcae25d2c234cb7b53537d829ebc8e1c574013f8fca87a28752e7cf` |
| `common\scripted_effects\012_africa_gods_recovery_effects.txt` | `14affd56c1200bd1289b00973ba151158b686065e42b13421b8ecbd2dae562a2` |
| `common\on_actions\012_africa_gods_on_actions.txt` | `6fe10799307f5a7d05855775dcce927dfe9ede44a2b9ffbbb326da634060876b` |
| `events\012_africa_gods_of_africa.txt` | `7b502d802cecc4a160d3649e936e57f62bbefa17329586190dceb90f5510d1a5` |

## Exact patch and helper closure

The three new calls follow interrupted retirement and frozen-slot release: `gods_of_africa_clear_contract_agreement`, `gods_of_africa_clear_diplomatic_terms`, then `gods_of_africa_clear_instalment_terms`.
The cancellation patch replaces the old private demand-active flag guard with native `has_active_mission`, clears four demand ease/burden flags, clears both armour quote fields, clears `payment_credit`, and clears the ordinary/substitute/partial capacity requirements.
No executable change remains outside that cancellation helper against the supplied baseline.
There are no new helpers, parameters, tuning values, weights, targets, localization keys or assets.

| Reused helper | Scope / inputs | Output and side effects | Ownership evidence |
| --- | --- | --- | --- |
| `gods_of_africa_clear_contract_agreement` | Participant COUNTRY; `= yes`; no parameters | Clears only `contract_agreed` and `contract_agreed_id`; leaves outcome ledger and counts | `012_africa_gods_contract_effects.txt:243-246`; normal `clear_demand:3185` already uses it |
| `gods_of_africa_clear_diplomatic_terms` | Participant COUNTRY; `= yes`; no parameters | Clears demanded-state array/count/three display IDs, named support enemy and guarantee/access/volunteer kind flags; performs no diplomatic concession or reversal | `012_africa_gods_effects.txt:2326-2336`; normal `clear_demand:3195` |
| `gods_of_africa_clear_instalment_terms` | Participant COUNTRY; `= yes`; no parameters | Clears signed flag, frozen material, amount, remaining instalment count and next day/date; sends nothing | `012_africa_gods_instalment_effects.txt:49-56`; normal `clear_demand:3196` |

Interrupted retirement occurs before any agreement, family, demand identity or native-owner pointer is cleared.
`012_africa_gods_contract_effects.txt:70-146,216-228` consumes the open ledger before terminal counters, prioritizes a provable offensive war against the frozen original host, and otherwise uses neutral retirement.
`012_africa_gods_contract_triggers.txt:4-24,49-66` does not require active current authority for that terminal closure.
Already closed ledgers cannot be relabeled or counted again.
Neutral retirement does not reset the compliance streak; a proven adverse war retains its existing adverse-outcome behavior without invoking the Wrath/treaty-breach/punishment owners.

Slot release also precedes clearing its proof fields.
`012_africa_gods_contract_effects.txt:178-212` consumes `demand_slot_released` once and debits only `var:gods_of_africa_demand_host` with matching ID, origin, generation, authority epoch and positive count.
It never redirects a debit through a replacement `africa_host`.
For an absent original country or mismatched receipt, it consumes release permission without debiting an unrelated object; host-loss cleanup separately zeros the departing host count at `012_africa_gods_effects.txt:4485`.

The term clears do not touch measured contributions, aligned kind/day history, Wrath, lifetime conduct, issued/retired/fulfilled/failed/refused/war-broken counters, last-closed tuples, final grades, material settlement obligations, victor exemption or victory receipt identities.
`clear_report_receipts:104-122` in `012_africa_gods_report_effects.txt` clears ordinary response/punishment presentation, rather than settlement/victory receipts.
No consumer found in the reviewed owner closure requires the newly cleared terms after cancellation.

## Source scenario matrix

These are manually traced source cases, not executed game scenarios or interpreted MCP mechanic tests.

| Case | Source result | Qualification / proof |
| --- | --- | --- |
| Signed continuing-support demand, host loses authority | Existing open ledger retires once; agreement and signed schedule/material/count/day/date disappear; mission removed; earlier measured shipments remain | New calls at `4506-4512`; delivery requires a current contract and closable ledger in `012_africa_gods_instalment_effects.txt:121-128` |
| Frozen territory or enemy-support demand | Named states and enemy/support-kind receipt clear; cleanup transfers no states and revokes no unrelated guarantee/access/volunteers | `clear_diplomatic_terms:2326-2336` only clears private terms |
| Host loss with an already closed contract | Retirement is inert and cannot overwrite the previous terminal result | Closed/open guards in contract triggers `4-24`; terminal consumes first at contract effects `83-92` |
| Host loss with historical settlement/victor reports pending | Existing historical flags survive through the wrapper; final grade, settlement identity and victory sequence are retained | Loss calls `cancel_recovery_participant_preserving_receipts` at `4466`; recovery effects `223-254` snapshot/restore only previously present flags |
| Participant capitulation or annexation while host survives | Separate `clean_participant` retires/releases/removes missions and participation; no payment or punishment remains authorized | Named ROOT/FROM callbacks in `012_africa_gods_on_actions.txt`; `clean_participant:4227-4324`; retained private terms discussed below |
| Invalid participant found by registry review | Separate archival owner retires/releases, removes missions and roster row; retained history remains available | Snapshot review `204-231`; `archive_invalid_participant:498-595`; does not call the patched helper |
| Departing host annexed/disappears or shared host changes | Native annexation cleanup and host-transfer call sites reach the loss owner; valid participant ledgers retire without requiring an existing active host; no replacement debit | `012_africa_gods_on_actions.txt:on_annex`; `012_africa_host_transfer_effects.txt:980-993,1049-1063`; caller execution remains unobserved |
| Orphan native mission, demand-active flag absent | Native `has_active_mission` permits removal independently of the private flag; no completion/timeout callback is run by that primitive | `4520`; installed documentation `6083-6092`; no terminal/slot reconstruction is inferred from an orphan timer |
| No actual native demand mission | Native guard skips removal; no absent-mission engine behavior is assumed | `4520`; mirrors inspected SWI cleanup precedent |
| Repeat cleanup on a well-formed already cancelled participant | No second terminal counter or slot decrement; no shipment, punishment or new demand date | Ledger/open and release guards; native demand proof was cleared on first call; absence of cooldown-owner call |
| Original-host recovery and fresh enrollment | Residual cleanup runs before epoch increment; registration binds fresh live identity and keeps genuine history; later issued contracts rebuild diplomatic/instalment/ease/burden terms | Recovery effects `260-268,295-311`; registration `411-464`; first-history initialization in `012_africa_gods_lifecycle_effects.txt:4-39`; issuance `2261-2308` |

Loss revokes permission before participant iteration (`4440-4468`, recovery `77-114`), without changing the epoch scalar needed for frozen-slot proof.
Queued owner work is gated at `africa_gods_of_africa_owner_tick:4805-4818`; payments require current live authority at `2589-2601`; punishment requires current host and participant identity at `3411-3419`.
The patch itself does not call any payment or punishment owner.
Cleanup does not call `gods_of_africa_clear_demand`, whose `3231-3241` section adds the ordinary cooldown.
Fresh enrollment's first-demand date at `453-454` is a separate existing owner action, not a cleanup-added cooldown.

Historical settlement reports validate their frozen originating target, generation and origin (`012_africa_gods_settlement_triggers.txt:58-72`), independently of current membership.
An actually absent originating host can prevent presenting that receipt even though its history remains stored; this patch does not invent another presenter.
Victor reports use their retained victory sequence/identity and receiver existence (`012_africa_gods_victor_triggers.txt:40-50`).

## Boundaries and retained private state

Keep the existing receipt-preserving wrapper for host loss and residual recovery cleanup.
Raw `gods_of_africa_cancel_participant` still clears `final_outcome_committed` and `settlement_report_pending` at `4563-4564`.
The only direct caller located is the wrapper at recovery effects `241`; the wrapper is reached from loss at `4466` and residual recovery at recovery effects `263`.
Do not add raw cancellation as an alternate historical-receipt owner without preserving those flags.

Participant archival and participant capitulation use separate duplicated cleanup bodies, so this patch does not physically remove their agreement, diplomatic, signed-instalment and ease/burden remnants.
Those bodies clear native demand identity/active permission and remove live membership; current-contract and instalment predicates consequently reject them.
New ledger opening clears the agreement (`contract_effects:59`), and actual new demand issuance invokes the diplomatic/instalment reset helpers and rebuilds burden flags (`effects:2287-2308`, `2494-2514`).
No demonstrable shipment, punishment or new-contract term inheritance defect was found from these particular inactive remnants on the well-formed reviewed paths.
The final directly read `012_africa_gods_contract_effects.md:92-93` correctly describes cancellation through the historical-receipt wrapper on host loss/residual recovery, rather than archival.
That ownership distinction matches the observed call sites; archival and participant capitulation remain separate consumers.

The patched path also retains `payment_instalment_material`, `last_instalments_left`, closed-ledger identity fields, participant authority binding fields, and some presentation/recency markers.
`last_instalments_left` is an ordinary response snapshot, and successful future transfers refresh it; payment material is overwritten when a new continuing-support quote is selected and ignored by other families.
Participant authority bindings alone do not grant current membership or permission, and enrollment rewrites them.
Closed-ledger fields are needed for terminal deduplication and must not be indiscriminately removed.
Accepted reconciliation/conduct and punishment recency history is not equivalent to a pending executable punishment.
Existing consequences already applied to stockpiles, states or political statistics are not refunded by cancellation.

One explicit malformed-state limit applies to the orphan-mission case: if the active flag is absent while a matching ledger still remains open, `contract_ledger_can_close` rejects retirement because it requires that flag (`contract_triggers:8`).
Later `open_contract_ledger` requires no open ledger (`contract_effects:40`), so such an independently inconsistent receipt can block a later genuine contract ledger.
Unconditional mission removal does not repair it, and the reviewed patch does not create that state.
No well-formed cancellation path reviewed here demonstrated that condition; it is a conditional consumer risk, not grounds to erase private receipts or fabricate a terminal outcome.

## References and MCP evidence

Connected reference routes were verified and called successfully.
The context result listed omitted Scopes/Triggers/On actions/Localisation topics; coverage is limited to the specific cleanup primitives read, not a claim that every listed topic was covered.

| Directly read reference | Exact source / lines | Revision |
| --- | --- | --- |
| Native `remove_mission`, COUNTRY; removes without complete/timeout effects | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md:6083-6092` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Native `clear_variable`, any scope | Same installed file `2773-2782` | Same installed revision |
| Offline `remove_mission` | `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:1916` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Offline regular-variable clearing | `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:565` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Vanilla cleanup precedent, read with `hoi4.source_lookup` | `game:common/scripted_effects/SWI_scripted_effects.txt`, `SWI_outgoing_president_cleanup:1877-1901` | Lookup revision `e5442531acabd536329a282e64ede237f2d8c246e624869d36d409f6ebacdd63` |

`hoi4.source_lookup` independently resolved the current cancellation definition at `4505-4606`, lookup revision `98abc7a5bd798ce260ee58195085d00cbec01662c03cf881d4c16611e8cc6e1c`.
Its reference result was incomplete with 19,902 unresolved references, so zero returned references was not treated as proof of no callers.
Local exact-symbol searches and direct caller reads supplied the source review instead.

The narrow live `hoi4.event_inspect` trace of `chaosx.nr12.606` returned `EVENT_INSPECTED_PARTIAL`, graph revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`, graph hash `d494c41cf68a6eb896650d0f95ea38572ce93b8c83273a07a92d60c74eb41ceb`.
Bounds were depth 2, 24 nodes, 60 edges, helper expansion enabled through the ordinary trace route.
The relevant report section was retrieved with a bounded resource read and identifies the actual event plus exactly this unresolved helper call: `EVENT_HELPER_UNRESOLVED`, “Scripted helper africa_gods_of_africa_owner_tick is absent from the active catalog”, at `mod:events/012_africa_gods_of_africa.txt:121`.
The helper exists in current source at `012_africa_gods_effects.txt:4805`; this is a coverage blocker in the connected catalog, not evidence that the gameplay definition is missing.
The complete large trace artifact was not reconstructed or hash-verified; its relevant bounded section and linked artifact identity are retained here.

Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f79fa85d3115194abfc7d7aa3db735d44fbbd90823edafa0e25535924edf1d9e/930957d497a532b408a8f8b713736e44916fe6c47e1dbfe83d83079e5b634a72/event-trace-8f4a82aa5d84.json`.

The matching `hoi4.event_render` state view returned `EVENT_RENDERED_PARTIAL`, selected zero nodes, and cannot provide a visual/helper-state acceptance claim.
Its bounded manifest was read through small byte ranges and parsed; it reports `complete = false`, no selected IDs and no rendered branches.
No claim of verified artifact bytes or rendered behavior is made.
Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8bac0c5df0d1a0d14e4aa8813f0397edd6f1658b5dde339be04a169cf7a217f8/9605a064ffe7ea089b8fa109f5376de40a1fe4d63869717cbddded7795a4044e/event-state-8f4a82aa5d84-manifest.json`.

The narrow cross-system `hoi4.impact_inspect` request for `gods_of_africa_cancel_participant` returned `IMPACT_ANALYZED_PARTIAL`, source revision `8eca4d9fb3330b5bf99858d501318bb9f67eba10efe43f61b7062acf55b8fab8`, one definition, zero resolved consumers and 19,791 unresolved entries.
Its large linked report was not fully retrieved and is supplementary unresolved evidence only.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6c667269c58dd0c4bdce6b5bdf63670f07962b310586aba06edd77c0f564a7a/eaa0c24ad4a702dd86cd7ef352d549404f055a8f0d53479c08f87c312dd6dba7/impact-ea5bd277a0ab88769f9e7327.json`.

Event comparison attempts with guessed before/after selectors were rejected by live argument validation (`-32602`; before/after require exactly one graph revision or artifact URI).
No successful baseline-versus-patch event comparison was obtained, and no self-comparison is offered as substitute proof.
The exact physical whole-file diff supplies the bounded patch identity, while the unresolved helper catalog prevents claiming MCP comparison coverage of this closure.
No health/version/task negotiation was established for paged `mode = helper_expansion`, jobs or native tasks, so those routes were not used.

The parent's subsequent status update confirms connected server version `3.10.0` and that the narrow graph projection does not expand helper behavior.
The parent also reports all 28 added expanded primitive statements as `SCRIPT_CHECKED` under declared COUNTRY scope, with `parametersChecked = false` and `argumentBlocksUnchecked = 0`.
That supplied evidence supports the added native primitive kinds/scopes; it was not independently rerun by this reviewer and does not execute the helper closure, prove parameter semantics or establish native outcomes.
The parent's final update additionally reports the native mission guard as independently `SCRIPT_CHECKED`, covering three commands with no unresolved commands.
This reviewer did not rerun that check, as requested.
Command validation supports the supplied guard syntax; the corrected source placement was independently rechecked below.

## Final guard/hash review

The parent's final instruction replaces the OLD private `has_country_flag = gods_of_africa_demand_active` guard in cancellation with native `has_active_mission = gods_of_africa_demand_mission`.
The final guard follows the inspected `SWI_outgoing_president_cleanup:1892-1894` precedent, removes an actual orphan mission independently of private flags, and avoids making an absent-mission call.
The earlier source placement finding at hash `4af08b18f003ef158280df1c396fd7873dfac6b3abac030637143da8034832fd` is superseded by the parent's function-scoped correction.
The corrected file independently hashes to `720f1cb91a1c36e73254954f08b08bd5e2b241770b022d310aaea16b8b6d9332`; cancellation `4520` contains the native guard and archival `508` matches baseline.
The full baseline comparison contains only the cancellation hunks; this resolves the placement finding without a change to archival ownership or term-clearing behavior.
The helper documentation's native-guarded cancellation claim at `012_africa_gods_contract_effects.md:98` matches this corrected source.
No code was edited by this reviewer and no additional MCP calls were made for the correction.
The previously reviewed term-clearing, ledger ordering, historical-receipt and recovery-enrollment findings remain applicable.

Publication recheck completed against the actual current file after the parent's last source-finalization instruction.
Raw-file SHA-256 again matches `720f1cb91a1c36e73254954f08b08bd5e2b241770b022d310aaea16b8b6d9332`, and the physical baseline again matches `f9fcb0d37264ebe6b10e64ca8b774226c17804170fae194bf616f4155aa00d51`.
The full whole-file comparison still contains only the three cancellation hunks, and extracted archival block bytes compare identical with preserved line endings.
The actual cancellation statement at `4520` contains `has_active_mission`; the three term-cleanup calls and private-field clears match the reviewed final patch.
The old `4af08` placement mismatch is historical and resolved, not a current source blocker.
Only this existing handoff was updated; no helpers were re-audited, no other file or Git state was changed, and no MCP call was made for this publication recheck.

## Parent disposition and remaining validation

Recommendation: accept the corrected bounded cancellation patch on its reviewed source contract, retain wrapper ownership, and carry the MCP coverage limits into the parent report.
No additional code change is recommended solely to remove the inactive remnants listed above.
If the parent broadens cleanup ownership, preserve ledger retirement and original-host release first, historical receipt wrapper behavior, and the absence of the normal demand cooldown.
Constants/tuning, event-target migration and helper migration are unchanged; there is no new state lifetime or shared helper to integrate.

Completed: verified baseline and final hashes; reviewed exact diff and rechecked final guard placement; traced helper writes, terminal/slot ordering, current authority gates, loss/recovery/archival/capitulation callers, receipt preservation and future enrollment; recorded source scenarios, parent-supplied primitive/guard validation and live MCP limitations.
Skipped by assignment: decision action audit, weighted/probability auditing, GUI/map/focus inspection, expanded declared-scope script validation, and all native execution.
Blocked/unresolved: connected event helper-catalog coverage, meaningful MCP baseline comparison for this cleanup closure, and native behavior.
Resolved: final native-mission guard placement and the inadvertent archival delta.
Skills used: events and subagents; no skill created or updated.
No simplification or fallback was implemented, and no full-feature completion claim is made.
