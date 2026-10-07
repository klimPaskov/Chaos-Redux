# Event 032 chemical escrow API architecture, 2026-10-07

Disposition: `unresolved` for the proposed API and implementation details pending parent review.
The requirement to reserve chemical payload during preparation remains accepted, with implementation queued rather than rejected.
Acceptance basis: the parent explicitly requested full Event 032 fidelity and identified accepted spec part 3 pipeline step 7, precommit cancellation return, launch consumption, existing authorization checks, and no consequences before launch.
This is a bounded architecture sidecar, not a gameplay patch or completion claim.
The file was absent at discovery and immediately before creation.
Only this handoff is owned by this subagent, with no source, Git, test, or shared CBRN write authority.

## Conclusion

Add a small CBRN-owned scripted chemical-payload receipt API beside the existing payload helpers.
Reserve real equipment when Event 032 accepts preparation, freeze the original actor, exact chemical agent, concrete equipment token, quantity and physical custody site, then settle by verified return, launch consumption, destruction or captured custody.
Event 032 should retain only its receipt handle and operation identity, not reproduce chemical storage mappings or native stock accounting.
The minimum current equipment scope is the four prepared air-payload models already used by its strategic chemical route.
The existing shared action and consequence pipeline stays authoritative after launch.

There is a real missing chemical receipt/refund API, but existing measured CBRN protection/export primitives establish a feasible implementation pattern.
Native chemical raid reservation is a separate engine payment path and cannot supply a scripted Event 032 cancellation contract.
No accepted requirement is declared impossible or rejected by this proposal.

## Accepted contract and exact current behavior

`docs\specs\032_missiles_specs\032_missiles_spec_part_3_operations_and_consequences.md`:33-43 requires payload reservation before preparation, with actor, target, sites, receipt and war revalidation before launch.
Lines 264-277 distinguish precommit payload return from possible postcommit consumption, and lines 487-515 require technology, policy, physical stock, compatible missile/site integration and the shared chemical release pipeline.
Lines 723-743 require settlement on invalidation, site loss, removal, cancellation and reset.

Current `common\scripted_effects\032_missiles_operations_effects.txt`, abbreviated `operations` below:

- `missiles_reserve_operation_payload`:4223-4229 only calls the read-only chemical stock check and accepts preparation without removing equipment or recording a chemical escrow.
- `missiles_check_chemical_payload_stock`:4263-4291 binds the actor and intended target, selects `strategic_chemical_raid`, derives class and default cost, and tests target policy, unlock, matching profile and available stock.
- `missiles_commit_operation`:6119-6134 repeats that free-stock check because nothing is reserved.
- `missiles_consume_chemical_payload`:4334-4366 rebuilds that action context and calls `cbrn_try_debit_action_payload` at launch.
- `missiles_consume_special_payload`:4368-4412 has a generic held-warhead shortcut for nuclear/biological escrow, followed by direct chemical debit when no held warhead exists.
- `missiles_release_operation_payload`:4234-4259 returns nuclear/biological escrow, with no chemical branch.
- `missiles_cleanup_operation`:6180-6185 invokes that return before clearing operation context.
- `missiles_resolve_operation`:6081-6096 consumes the payload before guidance, interception and impact.
- `missiles_dispatch_chemical_payload`:4414-4470 reconstructs the impact context, supplies the recorded consumed amount/proof, resolves protection and dispatches the shared chemical action only after launch resolution.

Current helper documentation records this missing preparation hold as queued in `common\scripted_effects\032_missiles_operations_effects.md`:142-148.
That existing queue note does not revoke the accepted reservation requirement.

## Storage and existing API map

| Representation | Source and contract | Event 032 relevance |
| --- | --- | --- |
| Nine strategic agent models | `cbrn_payload_effects.txt`:20-29, 86-136 and `cbrn_payload_triggers.txt`:117-132, 215-255 | Exact chlorine, phosgene, mustard, lewisite, Tabun, Sarin, Soman, Malodor and Behavioral models. These are not the models selected by Event 032's current strategic chemical route. |
| Filled shell model | `cbrn_payload_effects.txt`:138-143 and `cbrn_payload_triggers.txt`:143-145, 158-177 | `chemical_shell_lot_1` has a country shell-filling agent profile. No Event 032 substitution proposed. |
| Four prepared air models | `cbrn_payload_effects.txt`:145-170 and `cbrn_payload_triggers.txt`:147-152, 164-183, 261-281 | Both chemical-air and strategic chemical routes use this family, with exact agent identity carried by `cbrn_air_payload_agent`. This is the required receipt family. |
| Legacy or restricted cylinders | `cbrn_payload_effects.txt`:172-212 and `cbrn_payload_triggers.txt`:134-140, 154-156, 195-214, 283 onward | Separate authorized legacy/restricted paths. They cannot replace the selected prepared air model. |
| Native raid equipment reservation | `cbrn_chemical_raid_effects.txt`:150-199 and `docs\systems\cbrn_warfare\cbrn_chemical_delivery.md`:134-148 | `essential_equipment` is the sole native payment. The outcome helper creates consumption proof from that native payment and neither debits nor refunds equipment itself. It is not a generic scripted escrow. |
| State protective-mask escrow | `cbrn_state_escrow_native_effects.txt`:9-43, 49-115, 198-229 and `cbrn_scripted_effects.md`:759-786 | Observes exact model debit/credit, retains original donor, partial remainder and native-mismatch quarantine. Useful pattern, but its state/protection fields and wrappers cannot be used unchanged. |
| Protective export transaction | `cbrn_export_transaction_effects.txt`:11-83 | COUNTRY donor fields keyed by recipient, measured concrete-model debit/refund, exact held remainder. Useful targeted-field and observation precedent, not a chemical operation receipt. |

The exact prepared air models and agent associations are:

| Frozen class | Concrete model token | Exact agent preserved separately |
| --- | --- | --- |
| Choking | `choking_chemical_air_payload_lot_1` | Chlorine or Phosgene |
| Blister | `blister_chemical_air_payload_lot_1` | Mustard or Lewisite |
| Nerve | `nerve_chemical_air_payload_lot_1` | Tabun, Sarin or Soman |
| Incapacitating | `incapacitating_chemical_air_payload_lot_1` | Malodor or Behavioral Agent |

Class derivation is `cbrn_chemical_air_raid_set_agent_class_internal`, `cbrn_chemical_raid_effects.txt`:22-62.
The scripted route supports those classes under `cbrn_action_agent_is_eligible_for_route`, `cbrn_triggers.txt`:300-314, including the explicit late-agent authorization required for nerve class.
The narrower native rocket raid agent selection must not be imposed on the existing scripted Event 032 adapter.

`cbrn_set_default_payload_requirement_for_action`, `cbrn_payload_effects.txt`:43-84, writes required quantity and resets consumed amount/proof.
For Event 032 it selects `constant:cbrn_payload_route_cost.strategic_chemical_raid`, currently 240, from `common\script_constants\cbrn_chemical_delivery_constants.txt`:24-39.
`cbrn_try_debit_action_payload`, `cbrn_payload_effects.txt`:214-253, requires static metadata, agent unlock, matching profile and sufficient exact model stock.
Its outputs are temporary `cbrn_action_payload_consumed` and `cbrn_action_payload_consumed_proof`, with internal `cbrn_payload_debit_model_matched`.
The internal mapper issues a negative native equipment effect and sets model-matched proof, then the public helper copies the requested amount into consumed output.
It does not store actor/model/operation identity, persist a refundable held amount, report a receipt handle, observe a before/after native delta, or expose a chemical refund operation.
Do not treat its nominal proof as a measured native acknowledgement when building durable escrow.

Searches of CBRN scripted effects/triggers found no general chemical-payload reserve/refund/consume receipt family.
The raid reservation and protective reservation families are actual existing APIs, while the chemical receipt operations below are proposed extensions.

## Proposed minimal CBRN helper map

Proposed names are interface recommendations, not existing definitions.
Place the receipt effects in `common\scripted_effects\cbrn_payload_reservation_effects.txt` and predicates in `common\scripted_triggers\cbrn_payload_reservation_triggers.txt`, or use a clearly separated section of the existing payload files if the parent prefers fewer files.
Document the full contract in `common\scripted_effects\cbrn_scripted_effects.md` and reference it from the existing dynamic helper API index, without a central router or wrapper skill.

| Proposed helper | Scope and inputs | Outputs, defaults and side effects | Direct consumers |
| --- | --- | --- | --- |
| `cbrn_resolve_action_payload_model` | COUNTRY actor, validated action agent/class/route | Caller-owned concrete `token:` model and matched proof. Current implementation scope covers the four existing prepared air models, rejecting unrelated families rather than inventing a substitute. No stock or consequence mutation. | Reservation and receipt validation, owned by CBRN. |
| `cbrn_reserve_action_payload` | COUNTRY actor with actor ROOT for existing policy gates, complete exact action context, consumer key and positive operation nonce | Caller-owned accepted proof, handle, actual held amount, recovery status. Existing matching receipt returns its identity without a second debit, while mismatched or closed replay rejects. Validates metadata/unlock/profile/policy and exact stock, observes actual debit, persists a held receipt, and creates no public use record. | Chemical branch of `missiles_reserve_operation_payload`. |
| `cbrn_payload_reservation_matches_action` | COUNTRY original actor, receipt handle, expected consumer/operation nonce and intended target/source site | Read-only identity/quantity/custody predicate. Requires full held receipt, matching frozen agent/model/route, valid actor and current authorization. Missing or stale inputs fail closed. Held receipt replaces only the free-stock test for a prepared operation. | Chemical commit precheck and payload-custody validation. |
| `cbrn_return_payload_reservation` | COUNTRY original actor, exact handle and consumer/operation nonce, verified recoverable physical custody and a refundable cancellation reason | Caller-owned measured returned amount, settled proof and recovery status. Credits only the stored concrete model to that actor, subtracting only observed gain from held remainder. Duplicate settled returns are no-ops. Does not require continuing launch technology, policy or enemy, but requires intact recoverable custody under that actor. | Voluntary cancellation, target/policy invalidation, or loss of another participant when the frozen custody site remains recoverable. |
| `cbrn_consume_payload_reservation` | COUNTRY original actor under its launch ROOT, exact matching held receipt, successful launch revalidation | Caller-owned consumed amount/proof and frozen agent/model metadata. Moves the whole held amount to consumed exactly once without another stock debit. No exposure, evidence, casualties, Condemnation or confirmed use. | Chemical branch of `missiles_consume_special_payload`, through `missiles_consume_chemical_payload` if that adapter name is retained. |
| `cbrn_discard_payload_reservation` | Exact original owner record with matching handle/consumer/nonce, frozen custody-site identity and explicit destruction/removal facts | Marks only proven destroyed or unreceivable held stock as disposed, with no stock credit and no chemical release. Repeated disposal is a no-op. Neither a live cancellation nor an intact captured site can use it to erase a refundable or transferable receipt. | Destruction/scuttling of the frozen custody site, or removed-owner stock with no valid surviving custody receiver under the accepted removal contract. |
| `cbrn_transfer_payload_custody` | Original COUNTRY receipt owner, exact STATE custody record and proven new COUNTRY holder, source/destination nonce and captured surviving quantity | Atomically removes the transferred part from the original held receipt and records the same agent/model/quantity in sealed captured custody linked to its provenance. No native free-stock credit, technology grant or consumption proof. Duplicate same-generation capture rejects. | Exact capture or surviving-site removal transaction for the frozen payload-custody state. |

The receipt helper may call the existing exact debit mapper with caller-owned outputs and observe the resolved model stock before and after it, or use a small private measured model-debit primitive following the protective precedent.
Use one payment path and one mapping owned by CBRN, and avoid a second debit after either native reservation or scripted receipt creation.
The measurement extension must distinguish valid full debit, valid partial debit and invalid observation.
A partial preparation debit rejects the operation and returns its measured held part through the same receipt refund path.
If that return is partial or blocked, preserve the receipt independently of Event 032 cleanup for recovery.
An invalid stock observation preserves the exact model, before, after, request and delta and quarantines further automatic stock writes.
Never clamp an invalid delta into a successful receipt or nominal full refund.

## Durable receipt, tuning, targets and cleanup

Use original-actor country ownership and a CBRN-assigned monotonically distinct local receipt handle.
Country identity plus handle is the receipt identity, while consumer key plus operation nonce identifies duplicate preparation requests.
Use targeted normal fields keyed by that handle, with a small country-local active handle array for duplicate lookup and recovery.
The export transaction and offline variable-targeting reference provide an existing pattern for indexed normal fields.
No global actor event target, shared single-escrow slot, periodic country scan, or Event 032-owned chemical equipment switch is needed.

Persist these CBRN-owned fields for each receipt: original paying actor pointer/id, current custody holder pointer/id, consumer key, operation nonce, agent, class, route, concrete model token, intended target-state pointer/id, frozen payload-custody and launch-site pointer/id, requested and observed reserved amount, remaining held amount, disposition, cumulative returned/consumed/transferred/disposed amounts, and exact native-mismatch evidence when present.
At preparation bind the exact physical custody state to a CBRN-owned mirror of receipt actor/id/nonce and held identity, so a control-change callback can distinguish this payload from another operation or ordinary missile stock.
The master country receipt owns the quantity, while the state mirror proves physical custody and must not become a second independently spendable balance.
Captured sealed custody becomes a new linked master receipt with its own generation/current holder, retiring the original held balance once.
Bind input identity before native stock effects so failed or nested work cannot erase the pending owner record.
Retain closed disposition/nonce evidence long enough to reject repeated reserve/refund/consume requests.
Remove a handle from the active/recovery set only when its held remainder is zero and its disposition is conclusively settled.
Event 032 keeps the handle and mirrors the expected operation identity, with its ordinary preparation active flag remaining separate from CBRN's accounting authority.

Reuse `cbrn_proof`, `cbrn_math`, existing agent/class/route constants and the shared route cost.
Add only a small uniquely named receipt-disposition constant category for pending, held, consumed, returned, captured/transferred, disposed and quarantined/recovery states, with its schema in `common\script_constants\`.
This is bookkeeping metadata, not a new balance table.
No new cost, multiplier, AI weight, duration, quantity cap, random draw or loss percentage is proposed.
Keep the quantity frozen from the accepted preparation receipt, rather than recomputing a refund from current tuning.

Regular CBRN action event targets serve the current synchronous call only.
Delayed operation callbacks rebuild them from the persistent receipt and operation pointers and revalidate exact actor, handle, nonce and source-site identity.
Use COUNTRY existence checks for actors and registered-site/state identity checks for state pointers.
Do not treat `scope_exists` on a variable scope as proof of object validity.
Foreign-ROOT site-loss cleanup must settle the proven former actor's receipt in that actor's current COUNTRY scope, using THIS or its frozen original actor pointer rather than the captor ROOT.
A return is allowed only when the triggering loss concerns another participant and the payload's own custody remains recoverable, while loss of its frozen custody site uses the explicit capture/destruction disposition below.
The policy gate is ROOT-dependent, so reservation and launch authorization must run with ROOT bound to the actor, while pure return/disposal accounting must not borrow that requirement.

Before every helper call, each caller initializes all temporary outputs it reads or forwards, including nested measurement outputs.
At minimum this includes receipt handle/result/amount, model/matched proof, before/after/observed/valid stock fields, `cbrn_action_agent_class`, required payload, consumed payload and consumed proof.
`cbrn_reset_action_context`, `cbrn_exposure_effects.txt`:1135-1175, resets public action metadata and outputs but leaves regular event-target names bound within the chain.
After each reset, rebuild the exact actor and target and every consumed authorization proof.
The reset must not clear durable receipt fields or its original actor/model/quantity.
Reservation must clear transient consumption/release/dispatch proof before returning its reservation result, so a preparation receipt cannot be mistaken for a release.

### Exact-agent integrity across profile changes

Prepared air stock is class equipment plus one exact country profile, not nine independently tracked prepared-agent stocks.
`cbrn_change_air_payload_profile`, `cbrn_payload_effects.txt`:368-389, currently discards part of free old-class stock and replaces the exact profile.
With escrow, changing Tabun to Sarin and later returning reserved nerve-class equipment would relabel the old payload under the new profile.
Storing the old agent in the receipt alone cannot fix that physical stock representation.

Recommend the narrow CBRN-owned guard that prevents ordinary air-profile reconfiguration while any original-profile prepared reservation has a refundable held quantity or unresolved return.
All routine profile writers and the existing selector's availability/tooltip must respect that guard, including recovery after a partial refund.
Release the guard after consumption, full return or authorized disposal, independently of other receipts, so one closing operation cannot unlock another open reservation.
Sealed captured receipts carry their own exact agent metadata and are excluded from the captor's existing production-profile lock until an explicitly validated integration binds them to that profile.
Transferring the original receipt into sealed capture retires its former actor's profile binding, while the new holder may configure a matching profile only when its own unrelated prepared reservations permit it.
A forced out-of-contract profile change must block or quarantine the incompatible receipt rather than convert its agent, silently destroy it or manufacture strategic-agent lots.
This guard is a proposal requiring parent acceptance as part of the storage extension, not an implemented restriction or a rejection of the required escrow.
An alternative that allows mixed exact-agent prepared stocks would require a broader storage redesign and is outside this minimal sidecar.

### Capture, removal and other physical dispositions

The parent's physical-custody clarification supersedes the earlier blanket chemical-return recommendation.
Current nuclear/biological behavior is a source finding, not evidence that recovery from a captured or scuttled custody site is approved.
`missiles_settle_lost_site_allocation` at operations:3305-3346 closes an uncommitted operation tied to the lost participant, then cleanup calls `missiles_release_operation_payload` at 6185.
That return helper at 4234-4259 credits a held nuclear/biological warhead without comparing the lost state to its frozen custody site or checking that site's disposition.
The nuclear/biological typed escrow audit and implementation remain parent-owned.

Specification basis: part 2:163-180 defines a physical state record and prepared-operation receipt, 339-347 distinguishes damage from destruction and stock loss, 363-398 freezes capture facts and requires exact-once bounded transfer, and 434-443 requires surviving-site transfer or destruction on removal.
Part 3:264-277 says payload normally returns before commitment and may be consumed afterwards, while 487-496 requires compatible launch-site and current shared-system eligibility.
Those clauses support disposition-aware settlement, not an automatic refund from every lost physical site.
They do not supply a chemical survival percentage or a completed captured-chemical integration rule.

| Triggering physical fact | Proposed chemical disposition | Required evidence and accounting |
| --- | --- | --- |
| Voluntary cancellation, target invalidation, ended war or changed launch policy | Return only recoverable still-held payload | Original actor exists, exact custody mirror/nonce matches, that actor still controls the intact custody site, and an explicit recoverable-custody proof is supplied. Current launch technology/policy need not remain valid for the return. |
| Loss of another barrage participant, with lost-state id different from frozen payload-custody id | Close the operation and permit the same verified return | Revalidate the payload's own custody state independently. An unrelated participant's capture or scuttling does not establish destruction or seizure of this warhead. |
| Scuttling or confirmed destruction of the frozen payload-custody site | Destroy its remaining held receipt | Freeze the destruction reason and custody identity before cleanup. No former-owner refund, captor credit or launch-use proof. The site may still have active flags when cleanup runs, so do not infer recoverability from pre-mutation flags. |
| Capture of the frozen payload-custody site with surviving payload | Transfer into sealed captured custody | Freeze former actor, new actual controller, site condition, exact receipt and supported surviving quantity before cleanup. Close the original held balance once and create a linked sealed receipt for that exact state/current holder. No native available-stock or technology grant. |
| Damaged or isolated custody site with no proven destruction or transfer | Hold pending explicit recovery or loss settlement | Isolation or disabled launch capability alone proves neither physical destruction nor successful recovery. Return requires the recoverable-custody proof, and unrecoverable stock remains quarantined/held until an explicit accepted disposition is supported. |
| Original actor removed | Resolve surviving physical custody first, then dispose only nontransferable remainder | If an exact surviving state and living current holder are proven, use the same sealed transfer path. Do not credit a removed actor or distribute stock by an arbitrary successor estimate. Destroy only the quantity assigned an explicit removal/loss disposition. |

Captured chemical receipt accounting is separate from `missiles_site_captured_reserve`, whose units are ordinary missiles.
The captured receipt preserves exact agent, concrete chemical model, quantity and original payment provenance, even when the new holder lacks technology or has a different air profile.
It is sealed storage, not free prepared equipment that can be relabeled by the captor's current profile.
An explicit CBRN-owned captured-payload integration/release effect would require current rightful holder, exact state/receipt, technology/integration and a matching prepared-agent profile before any measured credit into usable stock.
The existing guard/study/scuttle/integrate site choices are the candidate Event 032 consumers, but the parent must accept and implement their chemical receipt hooks.
Do not silently substitute whole destruction for an intact capture merely because that API is missing.
If surviving quantity or transfer identity cannot be proved, retain the unresolved receipt and report that exact gap rather than refund, discard or fabricate survival.
No chemical survival ratio is selected by this sidecar.

Shared-owner settlement inputs must include exact receipt actor/handle/consumer/operation nonce, frozen payload type/agent/model/quantity, physical custody-site id and mirror nonce, triggering lost-state id, typed loss reason, pre-change holder and condition, actual new controller when relevant, proven recoverable/surviving/destroyed amounts, and commitment/consumption disposition.
Keep these inputs separate from the existing `missiles_allocation_loss_mode`, which distinguishes missile allocation loss from refund but cannot distinguish chemical capture, destruction and unrelated participant loss.
Freeze loss facts before `missiles_abort_operation` or cleanup clears the operation's source pointer and before site flags are mutated.
Event 032 owns the operation and supplies exact callback facts, while CBRN owns chemical quantity, measured native return, sealed transfer, destruction, receipt closure and recovery records.
Scope all actor/holder operations to the proven owner, never a capture callback's foreign ROOT.

The settlement operation must choose one disposition for each accounted unit: original held, returned, consumed, transferred into sealed custody, or destroyed.
Capture must prevent a cleanup return of that same quantity, destruction must prevent later return/transfer, and launch consumption must prevent every cancellation credit.
A captured receipt and its source receipt are linked conservation records, not two spendable copies.
Repeat callbacks validate both site mirror generation and receipt closure before any credit or transfer.
Civil-war/release/removal bridges preserve these receipt identities before publishing inherited site records.
All stock/custody settlement effects remain separate from release consequences and must not create exposure, casualties, evidence, Condemnation or confirmed use.

## Minimal migration and call-site plan

1. Implement the CBRN-owned receipt effects, validation predicates, four-model resolver, measured debit/credit and documentation together, with the Event 032 direct consumers in the same implementation tranche.
2. Replace the preparation chemical availability-only branch with reserve creation after missile escrow succeeds, preserving all existing technology/project, policy, integration, exact source-site custody and target gates.
3. Extend preparation rollback and payload cleanup with typed physical settlement: verified return for recoverable custody, sealed transfer for supported capture, and destruction/removal disposal for proven loss, preserving unresolved or partially refunded CBRN-owned records.
4. Change chemical commit validation to prove the exact held receipt and current authorization, not require a second free 240 units that preparation already removed.
5. Replace launch chemical debit with once-only held receipt consumption, and handle chemical receipts before the generic nuclear/biological shortcut, which otherwise skips CBRN receipt accounting.
6. Use the receipt's frozen agent and actual consumed quantity in impact dispatch, rather than a mutable country selector, and leave protection/exposure/action-record dispatch at its existing post-launch stage.
7. Add the owner-side air-profile receipt guard, state custody mirror, sealed capture transfer and removal disposition, then update Event 032 helper documentation and the chemical-delivery API map.

Keep free-stock eligibility for a new preparation and receipt eligibility for an already prepared operation separate.
The API must repeat the shared static metadata, route-agent eligibility, technology/project, policy/readiness, matching profile and stock gates at reservation, with all non-stock authorization and custody gates repeated at launch.
Stock payment at launch is established by the matching reserved receipt, never by a second stock debit.
Return should remain possible after a policy change, lost technology or ended war when physical custody remains recoverable, because the receipt proves the original payment.
Capture or destruction of the frozen custody site takes its own disposition instead of authorizing that return.

CBRN stock detection and monitored destruction also require a narrow integration check.
`condemnation_has_chemical_stockpile`, `common\scripted_triggers\condemnation_sanctions_triggers.txt`:148 onward, currently detects free native families, and `condemnation_destroy_chemical_stockpiles`, `common\scripted_effects\condemnation_response_effects.txt`:78-168, removes those free families.
Holding all free chemical equipment in new receipts must not make an arsenal invisible to that existing contract.
The CBRN owner should include still-held receipts in ownership detection and settle affected reservations through an explicit disposal/invalidation hook when its existing destruction action requires it.
Do not double-remove equipment already debited at reservation or allow cleanup to refund a destroyed receipt.
This identifies a storage integration dependency, not authorization to redesign sanctions or change destruction tuning.

## Risks, unsupported analysis and validation requirements

- Current nominal debit proof is not a measured native stock delta, so exact receipts require before/after observation and full/partial/mismatch behavior.
- Exactness established by existing getters is actor, concrete model, exact logical agent/profile and quantity. Individual manufacturer, captured producer and equipment variant identities are not returned by the current API. No claim of recreating those hidden identities is made.
- Current prepared-agent identity needs the profile guard described above, or a separately designed broader representation. Returning a class model under a different agent profile is not an exact agent refund.
- Generic action resets and nested temporary outputs can erase unowned proof storage, so the implementation tests must model caller/helper lifetime at every boundary.
- Blocked refunds must survive Event 032 cleanup and must not be treated as settled by a cleared outer active flag.
- Closed handles must reject duplicate payment and late cancellation of a successor operation.
- Existing `cbrn_scripted_effects.md`:494-500 still describes unused native-raid refunds, while current raid source:150-199 and `cbrn_chemical_delivery.md`:134-148 explicitly establish full native payment and no outcome refund. Use the current source for this proposal and leave that stale native API prose for owner reconciliation.

Meaningful validation completed here is source mapping, exact model/route/proof tracing, reset/lifetime review, cancellation/removal integration tracing, and inspection of existing measured CBRN receipt precedents.
No stock simulation, source interpreter, gameplay edit, test run, game launch, log search, Git write or subagent spawning was performed.
Parent implementation should validate exact-stock preparation and a second spending attempt, all supported exact agents/classes, before/after measured payment, cancellation twice, launch once without a second debit, reset between preparation and launch, policy/profile changes, loss of another participant versus capture/destruction of the frozen custody site, blocked isolation recovery, foreign-ROOT capture settlement without refund, sealed recapture, actor removal with surviving custody, partial refunds, mismatches, late stale callbacks, and receipt-aware destruction.
Those are proposed validation cases, not executed scenarios or balance evidence.

A bounded `hoi4.event_inspect` trace was requested for `chaosx.nr32.1` with depth 1, six nodes, eight edges and no helper expansion.
It returned no tool result within approximately 32 seconds, and the waiting execution was terminated to avoid further long MCP work.
No job handle, source revision, graph artifact or engine coverage was obtained, and the server's final read-only request outcome remains unobserved.
No retry, long expansion, probability call or renderer was used.
The exact gap is unavailable inspection results for this bounded request, not a claim that the route or service is absent.
Required event-helper MCP coverage remains unresolved for parent validation, and this source architecture is not substituted for engine proof.

## Reference identities and ownership handoff

| Source | SHA-256 |
| --- | --- |
| `common\scripted_effects\032_missiles_operations_effects.txt` | `5EC05957945AD6F2F2E71ADF4091EDECA7B08E57A233F8267585B7428CBCD6E7` |
| `common\scripted_effects\cbrn_payload_effects.txt` | `84D3D8A19C94954ADCA3D4B7EE8030BE9EB3F77552B8F8C6D8014A47A34732B9` |
| `common\scripted_triggers\cbrn_payload_triggers.txt` | `B6DC90825E6F20B517D0FE84C3210A54AAF5B96F27FD467F1BDAA1EE6A7EF8C7` |
| `common\scripted_effects\cbrn_chemical_raid_effects.txt` | `B770477F77423347EEDA57E644EE3ACFA3EB6AAE9E492347A9FF71E049C67D8C` |
| `common\scripted_effects\cbrn_state_escrow_native_effects.txt` | `107D041E9762E2E54E131C4D23E26CDAB8842F2CD611213F45F181091CD1B567` |
| `common\scripted_effects\cbrn_export_transaction_effects.txt` | `08D9AE97D885518F578C14DD2E28E7E3477FE61EB3B792AEC751875B84659A86` |
| `common\scripted_effects\cbrn_exposure_effects.txt` | `3112E6B2D976F592D714ECED13440871EA1A8214D945D646672B6853335C3580` |

Local offline reference sections read: `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`:437-442 for persistent/temporary lifetime, 551 for targeted normal fields, and 955-959 for token values and `GetTokenKey`.
Wiki source SHA-256: `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
Installed documentation read: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`:1252-1264 for COUNTRY equipment debit/credit and optional producer behavior, and 6496-6503 for regular event targets.
Installed source SHA-256: `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
The measured CBRN mask/export helpers are the repository precedent, and existing dynamic helper files/API index were inspected before proposing the extension.

Guidance used: `AGENTS.md`, the events and subagents skills already read in this conversation, pertinent CBRN storage/action documentation and exact source, offline wiki and installed effect sections.
No skill was created or changed.
No gameplay simplification or fallback was made.
Completed deliverable: this architecture map and migration proposal.
Pending work: parent acceptance of the exact receipt/profile/custody policy, CBRN-owner implementation with Event 032 call sites, meaningful tests, documentation reconciliation and required MCP/native validation.

## Parent integration boundary, 2026-10-07

Acceptance basis: the parent explicitly clarified that chemical commitment must prove typed held payload and current technology/policy/site eligibility after real reservation, without requiring replacement free stock.
This boundary is incorporated into the proposed migration and does not expand this sidecar into the parent-owned nuclear/biological typed escrow audit.
Current source inspection confirms `missiles_operation_preparation_remains_valid` and `missiles_operation_can_be_committed` at `common\scripted_triggers\032_missiles_operations_triggers.txt`:259-294 invoke integration/custody gates and missile reserve sufficiency, while their chemical custody branch at 434-454 does not itself prove a typed chemical escrow, held quantity or current payload technology.
The integration and site-family flags must not be treated as substitutes for those missing proofs.

Keep new-preparation affordability before reservation distinct from prepared-operation validity after reservation.
Add the chemical receipt predicate to the latter preparation/commit checks and immediately before launch consumption, while keeping the pre-reservation eligibility path able to prepare an operation that has no receipt yet.
For the held path, require chemical payload type, exact original actor and operation identity, frozen exact agent, concrete model/class/route, intended target/source-site identity, held disposition and the full frozen reserved quantity.
A bare `missiles_operation_payload_escrow_active` flag or generic held-warhead shortcut cannot authorize chemical commitment.

Rebuild the CBRN read-only action context from that frozen receipt and explicitly rerun `cbrn_action_agent_is_unlocked`, `cbrn_action_payload_profile_is_ready` and `cbrn_chemical_action_policy_allows_exact_target`, alongside current compatible missile technology/integration, enabled track, policy, command, target, war and participating-site checks.
Preserve exact-agent project alternatives supported by the shared CBRN unlock predicate.
For an already prepared operation, the matching full held receipt supplies payload payment sufficiency, so omit `cbrn_action_payload_stock_is_sufficient` and the former free-stock commitment test from that held path.
Launch consumes the validated receipt without another native debit, and failed current eligibility closes through the explicit physical-custody disposition above.
When a return is physically supported, it uses the exact stored model/amount and original living actor without requiring launch eligibility for that refund.

Meaningful parent test boundaries: zero free payload with a full valid held receipt can commit, while wrong held type, agent, model, quantity, actor/nonce, lost current technology, changed policy or invalid source site cannot.
These are proposed test cases, not tests run by this subagent.
Only this architecture handoff changed, with no gameplay/Git writes, simplification or change to the previous engine-evidence limits.

## Parent physical-custody boundary incorporated, 2026-10-07

Acceptance basis: the parent explicitly required separate treatment of loss of the frozen payload-custody/launch state and loss of another barrage participant, with no assumed return from captured or scuttled custody.
The capture/removal section, helper map, receipt fields and migration/validation steps above replace the earlier blanket-return proposal.
The recommendation is disposition-aware settlement with verified original-owner return, exact sealed capture transfer, proven destruction and surviving-site removal handling, with unresolved quantities retained for owner review.
Chemical survival amounts and captured-payload integration remain proposed details requiring parent acceptance, while nuclear/biological typed escrow work remains parent-owned.
No gameplay changes or simulation were performed.
