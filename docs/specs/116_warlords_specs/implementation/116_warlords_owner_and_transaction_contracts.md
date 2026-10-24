# Event 116: Owner and Transaction Contracts

## 1. Status and scope

This is the narrow technical appendix to the parent-authored Event 116 Warlords design. The package records that its parent accepted the architecture handoff's contracts A–F as **design proposals**, with their identity, receipt, and owner boundaries. This historical claim is not independently established or renewed by the current import. This appendix makes those proposals reviewable by an implementer. It does not establish existing exported APIs, prescribe HOI4 effect syntax, select gameplay tuning, or certify engine capability.

Event 116 is the current Warlords event. Event 127 is historical provenance. The controlling user brief requires actual defecting generals, actual coherent territorial breakaways with surviving parents, ordinary warfare and recruitment, identity continuity with Event 019, and real Generalissimo campaigns before Supreme War State formation. That political formation is distinct from a later Final Warlord terminal branch. The latter requires current effective multinational and region-spanning military dominance, **Chaos strictly greater than 1000**, world-end scenarios enabled, its own branch enabled in the shared world-end registry, and no active or competing successful shared world-end claim.

Source basis: `source_reading/user_warlords_brief.md`, accepted `source_reading/116_architecture_integration_handoff.md`, the 20 fully read repository files recorded in `source_reading/repository/architecture/repository_read_ledger.json`, pinned to `klimPaskov/Chaos-Redux` commit `a3ef485c5da7e2337122eca04ac65c175050f251`. The complete 640,939-character 019 derivative source was read, including recovered output/tail. This appendix additionally uses complete local reads of `source_reading/repository/root/docs/systems/universal_cost_modifier.md` (15,291 characters) and `liberation_release_coordinator.md` (11,936 characters). The parent also fully read the complete cost definition `common/scripted_effects/chaosx_universal_cost_effects.md`, recorded in the 12-file root ledger. This appendix attributes that definition read to the parent and does not claim a second personal read. Other root-owned supporting evidence retains the attribution and limitations of the accepted handoff. The current boundary review additionally fully read Parts 2, 4, 8 and 9 of the Event 116 package.

No HOI4 runtime/MCP validation is available or claimed. The logical types and interface labels below are **new proposed adapters**, not installed engine types or script identifiers. Physical conservation and exact proof are acceptance requirements, not promises that the engine can already satisfy them.

## 2. Owner matrix

| Owner | Authoritative state and permitted writes | Exposed observation or acknowledgment | Writes that remain outside its authority |
|---|---|---|---|
| 116 Warlords | 116 episode, ordinary warlord participation, selected actual general reference, proposed hierarchy edges, pre-067 Command Cohesion authority and acknowledged same-value handovers, political formation milestone, dominance evidence, 116 branch lifecycle, 116-owned receipts/history | Current episode/actor validity, frozen requested transfer, edge invalidation, readiness and outcome evidence | 019 private issuance/loyalty/debt/provider state, 067 canonical creation, permanent death/removal, or private Cohesion, shared terminal flag without registered owner commit |
| 067 Generalissimo | Canonical Generalissimo identity and actual owner country, owner-valid death/removal, Influence/Command Cohesion lifecycle, 067 country package, 067 independent world end | Current canonical actor validity, approved Cohesion adjustment outcome, owner removal/takeover/settlement receipt | Converting 019 claimants into canonical 067, cloning canonical actor, granting control of foreign independent armies, merging 067 world end into 116 |
| 019 Soldiers | Immutable claimant UID and current row resolution, personally loyal lots/units, generation/template/unit identities, liabilities, exact derivative transaction, provider dispatch, derivative defeat/final cleanup | Exact participating manifest, actor/loyalty validity, staged/committed/recovered/quarantined receipt, provider proof | Selecting a fictional replacement for 116's actual general, granting 116 ordinary army subset transfer, rewriting 116 history, destroying a surviving country because its hierarchy edge ended |
| Registered 019 family/provider | Provider-specific public country identity, institutional/leadership setup, custom resource payments and refunds, provider lifecycle proof | Provider acknowledgment for the exact existing package and cleanup phase | Generic takeover of 019 ledger, deletion of a promoted claimant without actor-owner authority, automatic inheritance of Hunger Lines stage/world end |
| Shared release coordinator | Existing 005/006 plan identity, reservations, exact territory/core/controller/capital recovery, registered participant proof | Frozen footprint, execution/rollback/finalization/commit status | 116 compatibility before distinct owner/origin registration, event-specific general transfer, forces, focus tree, politics, or country package |
| 006 carrier/package registry | Carrier provenance, package identity and guards, 006 origin lifecycle | Authorized carrier/package availability through its owner | 006 setup merely because a country tag exists, adoption of an already living country as a new release candidate |
| Shared universal cost framework | Quote arithmetic/source registry, native component debit dispatch, actual-paid receipt, one-time refund/settlement proof | Documented quote, affordability, payment, recording, refund and settlement results | Purchase eligibility, target authority, cooldowns, reserve floors, 116 effect success, physical force transfers |
| Shared world-end authority | Registered terminal exclusion/claim/commit and shared world-end state | Current active owner, accepted commit or rejection | A 116/067 owner clearing shared terminal state after defeat to restart ordinary automatic events |
| 114, Mutiny, Resistance/occupation, Random Civil War settlement, Hunger Lines | Their actual causes, assets, histories, settlement and lifecycle | Proposed targeted notifications about affected countries, characters, forces, states or routes | New 116 writes to private owner state, universal nonhuman classification, implied public APIs from uninspected call sites |
| Engine/ordinary countries | Actual character ownership, diplomacy, state ownership/control, army custody, supply, stockpiles, manpower, warfare/recruitment | Verified current observations and supported mutations | Assuming a script call establishes its own success or treating bookkeeping/cosmetics as physical control |

Owner participation is explicit and versioned. A 116-origin episode involving 019 assets does not change their issuance origin. A 019 country joining 116 remains its actual country, an absent-country release path is not run a second time. 019 human claimant countries retain human classification. IDs, enums and callbacks remain provisional until the coding collision audit and owner registration.

## 3. Proposed logical types

These are implementation-independent schemas. Numeric storage, parallel arrays, event targets or engine-specific serialization must be selected only after capability and scope review. Persisted actor identity must not rely solely on a volatile event target or UI index.

| Type | Required logical contents | Validity rule |
|---|---|---|
| `OwnerRef` | System identity, interface/version identity, registered authority | Exact known owner, no default guessed owner |
| `EpisodeRef` | Owner, positive episode/generation identity, lifecycle state | Distinguishes a legitimate later country generation from the former episode. It never revives a permanently removed 067 person |
| `CountryRef` | Actual country identity, generation/origin when relevant | Country existence and correct generation are checked afresh |
| `CharacterRef` | Actual character identity, current actual country, actor owner, owner immutable UID when present | Owned, active, alive and eligible according to actor owner, a UID alone does not prove live-character continuity |
| `TransactionKey` | Owner, episode, positive nonce, operation kind, exact source/destination identity | Unique operation within owner lifetime, duplicate calls resolve the same operation |
| `OwnerReceipt` | Transaction key, actor/source mirrors, operation/component identity, phase/result, recorded mutation evidence, consumption/settlement state | Fresh mutation receipt differs from a consumed tombstone, caller checks all mirrors |
| `StateFact` | Actual state, separate owner and controller, relevant cores, capital role, protected/selected role | Each fact is observed in the correct state scope, ownership cannot substitute for control |
| `CharacterPreservationManifest` | Same original actual character ID, changing attributes, traits, history and portrait, valid ruler/general roles, owner-valid death/removal state, supported transfer method/proof | Verified same-actor preservation before birth admission, including no active duplicate in the parent. Existing actor promotion does not authorize profile recreation |
| `ForceManifest` | Exact engine forces and custody, owner unit/lot/generation/template UID/cohort where present, relevant live physical quantities and assignments, transfer eligibility | No arbitrary ordinary-force fraction may replace a required exact subset |
| `ResourceManifest` | Exact resource kind/variant/provider, source/destination balances, outstanding liabilities, permitted external sinks/sources | Conserves actual quantities and owner liabilities, unsupported kinds remain explicit blockers |
| `TransferManifest` | Transaction key, actors, state, character, force and resource manifests, parent-survival and destination-viability evidence, recovery footprint | Frozen before mutation, revisions/identity remain valid at each dependent boundary |
| `CommandEdge` | Actual root/member actors, relationship kind, current command authority proof, relevant forces/states/routes, owner acknowledgment, revision | Political membership alone cannot establish commandable armies |
| `DominanceSnapshot` | Root/episode, bounded registered actors and command edges, current major/region/territory/force/route evidence, observation date/revision, unknown/rejection reasons | Fresh, complete enough for the core design's predicate and invalidated by relevant changes |
| `InvalidationNotice` | Cause owner/receipt, affected actual actors/assets/edges, old/new observations or unknown state, episode/generation | Idempotent, targeted and owner-scoped, cannot erase unrelated actors/history |
| `CostComponentReceipt` | Payer, transaction/component IDs, ordinary cost, final quote, actual paid, resource kind, source proof, refund/settlement state | Actual debit proof precedes record acceptance, requested/discounted price alone is not paid proof |
| `TerminalReceipt` | 116 episode, current root/ruler, political milestone, dominance revision, exact Chaos predicate, all-world-end-enabled setting, own branch toggle, shared claim/commit result | Published success requires accepted shared terminal commit and revalidated 116 readiness |

Logical result variants for all new adapters: `Rejected(reason)` with no mutation, `Observed(value)` for read-only success, `Pending(transaction, phase)`, `Applied(receipt)` for fresh proved mutation, `AlreadyApplied(receipt)` for an identical idempotent replay, `Recovered(receipt)` for exact proved restoration, and `Quarantined(transaction, phase, reason)` for uncertain/irreversible partial state. A failed helper call does not imply `Rejected` if mutation may have begun. Unknown capability, actor, or receipt state fails closed.

Receipt identity includes the actual source and destination, not just a reused tag or selected row. When scopes nest, freeze owner/episode/nonce/actor/index context privately and initialize temporary scalar/array outputs before each helper call. Do not assume shared temporary outputs or named event targets survive nested helpers unchanged.

## 4. Accepted contracts A–F as proposed typed interfaces

### A. `ResolveCurrentActor`: new proposed 116/019/067 observation adapter

**Input:** `{ requester: OwnerRef, episode: EpisodeRef, expected: CharacterRef }`.

**Output:** `Observed({ actual: CharacterRef, ownerAcknowledgment, characterRevision })` or `Rejected(reason)`. Read only.

The owning system resolves its immutable UID to the current row and verifies actual owned character identity. 019's selected row is not enduring identity. 067 validation rejects missing/stale global mirrors, the wrong country, departed actors, and its own valid permanent removal. A replacement actor or legitimate later country generation cannot reuse an old identity receipt to recover readiness. A permanently removed 067 person is never revived. No invalid actor result creates or selects a substitute general. Existing 019 derivative promotion preserves its owned actor, the natural 019 commander reconstruction path is not treated as equivalent live-character transfer.

### B. `ParticipateInExactTransfer`: new proposed owner-coordinated transaction adapter

**Input:** `{ key: TransactionKey, requested: TransferManifest, participantOwners: OwnerRef[] }`.

**Output:** the transaction result variant and exact owner receipts for staged, committed, recovered or quarantined assets. Preparation must be separable from mutation.

Live-character preservation is a hard capability gate before a birth path is admitted. Prove a mechanism that preserves the same actual character ID, relevant traits, attributes, history, portrait and valid ruler/general roles in the destination without an active parent duplicate. If that mechanism is unproved, reject the affected birth path before any birth mutation. A reversible staged failure requires exact proved restoration. Failure after the first irreversible step requires quarantine and owner repair, never a claimed rollback or replacement profile.

116 requests the actual defecting general, exact territory and physical forces/resources. 019 contributes only explicitly eligible personally loyal assets and associated debt/liability records, providers acknowledge their own package. Existing derivative countries are observed/adopted into 116's registry without a new release or duplicate general. Ordinary armies, air/naval assets and stockpiles require their own verified conservation mechanism. 019's exact recorded formation reconstruction does not satisfy an ordinary-army transfer capability by implication.

The adapter cannot clear original issuance history, allocate duplicate issuance IDs, repair damaged formations, discard obligations or grant unrelated recruitment. It returns separate proof for live character preservation, territory mutation, forces/resources, accounting, and public owner setup. All required participating owners must acknowledge before successful publication.

### C. `ObserveEffectiveCommand`: new proposed bounded observation adapter

**Input:** `{ root: CharacterRef, episode: EpisodeRef, registeredActors, registeredEdges, relevantStateAndRouteFootprint, requiredRevision }`.

**Output:** `Observed(DominanceSnapshot)` or explicit unknown/invalid evidence. Read only.

It observes actual armies, usable routes, territory and current authority. A commanded subject needs verified authority over both its current forces and future recruited forces, obligatory participation in the order's campaigns, strategic access and a usable chain of orders. A one-time expeditionary transfer cannot qualify an otherwise independent military. Independent command remains a rival even when country cosmetics, faction membership or historical subjugation suggest otherwise. Political formation, saved war wins or a stale hierarchy flag cannot produce a successful dominance snapshot. The core design supplies the readiness predicate and starting profile. This appendix sets no geography partition, duration, army share or score threshold. Continuous proof requires complete supported change coverage. An observation service failure invalidates proof rather than granting unobserved grace.

### D. `InvalidateCommandRelationship`: new proposed cross-owner notification adapter

**Input:** `InvalidationNotice` with exact owner and affected-asset scope.

**Output:** fresh or previously applied invalidation receipt, affected edges/readiness become stale or invalid. Re-evaluation remains read only until a separate authorized mutation.

Causes include liberation, freed/autonomous subjects, defection, actual actor removal/death, civil-war settlement, annexation, occupation/control change, force command change and route loss. The operation preserves paid costs, historical milestones, private owner obligations and surviving ordinary warlords. It does not annex, demobilize, recreate or delete countries/characters. Lifecycle notifications remain valid after new-spawn eligibility is disabled. Cleanup authorization requires the stored lifecycle owner, not the currently eligible spawn provider.

### E. `RequestOwnedCohesionChange`: new proposed 116/067 ownership and publication adapter

**Input:** `{ key, country, currentCohesionOwner, canonicalActorWhenRequired, causeOwner, causeReceipt, requestedOwnedEffect }`. Owner transition additionally freezes the current amount, pending cause receipts, history and authority revision.

**Output:** current-owner-approved applied outcome and public observation, rejection, or identical replay. A handover returns both owners' matching acknowledgments for the same actual country, current amount, pending receipts, history and authority revision. Exactly one active owner writes and publishes the value.

Command Cohesion is the parent design's sole new public persistent value type. Before a 067 takeover, 116 owns the warlord country's value and its mutations. A proposed accepted handover freezes the actual country, same current amount, pending cause receipts and history. Mutations are frozen during handover. 067 acknowledges prepared adoption of that exact state, 116 acknowledges closure of its write authority, and the acknowledged ownership commit enables 067 as sole writer. Prepared adoption does not enable a second writer. The transition neither refreshes the amount nor exposes duplicate active stores. If 067 already owns an active post-takeover value when 116 encounters the country, 116 uses that existing value from the outset.

During 067 ownership, 116 submits causes and consumes owner acknowledgments. 067's pre-takeover Influence retains its distinct lifecycle. A later lawful 067 departure can return the same current value and receipt/history continuity to 116 only after 067 acknowledges closure of its authority. A civilian transition retires the active warlord display while preserving history. Missing or uncertain closure quarantines the ownership handover. It does not create a new meter, reset the amount or resurrect the removed actor. Save/load or duplicate callbacks must preserve the single acknowledged authority. No ownership transition is implemented until the shared interface is accepted and verified.

The project skill guidance prefers at most two public persistent values across shared surfaces. This is not a literal user constraint. The parent design chooses one new value type. Private receipts, revisions and readiness evidence are not additional public meters.

### F. `CommitFinalWarlord`: new proposed 116/shared terminal adapter

**Input:** `{ key, actualRootAndRuler, politicalFormationReceipt, freshDominanceSnapshot, readinessRevision, branchSettings }`.

**Output:** a shared-authority-backed `TerminalReceipt`, rejection without terminal consumption, identical committed replay, or quarantine if the shared claim/publication outcome is uncertain.

Immediately before claiming shared terminal authority, recheck the live actor, owner-valid deaths/removal, current military dominance, prior actual Supreme War State formation, **Chaos>1000**, world-end scenarios enabled, the Final Warlord's own branch enabled in the shared world-end registry, and no active world end or competing successful shared claim. A stale quote or preview cannot authorize launch after control or settings changes. Current domestic unity, post-formation international command, usable routes and uninterrupted consolidation proof must all remain valid. Existing 067 or any other active world end blocks 116. 067's older at least 1000 independent branch is neither imported nor merged.

Successful presentation and the cessation of ordinary automatic events follow successful shared terminal commit. War continues. Later defeat invalidates/closes the relevant 116 hierarchy/readiness and preserves ordinary surviving successors and history, it does not clear shared world-end state. Replay/reload cannot produce another successful launch or re-enable ordinary events.

## 5. Exact transfer transaction phases

These phases are logical requirements. They do not claim an atomic engine transaction. Persist the exact phase, manifest, owner acknowledgments and failure reason before proceeding to a dependent stage. The irreversible frontier is the **earliest participant mutation that cannot be proved exactly reversible**, not merely a convenient final flag.

| Phase | Required actions/evidence | Allowed failure handling |
|---|---|---|
| `Observed` | Resolve actual actor and current country, verify current eligibility and prospective physical assets | Reject without mutation |
| `Prepared` | Allocate unique transaction, freeze exact manifest and recovery footprint, prove parent survival/destination viability, collect owner participation | Cancel/release preparation only after any preparatory mutations are proved reversed |
| `Reserved` | Reserve exact states/assets/actor against incompatible active operations, preserve original owners/controllers/cores/capitals | Idempotent cancellation, retain failed recovery ledger |
| `Locked` | Revalidate actor, live footprint, all aligned owner arrays, liabilities and reserve authority | Stale lock rejects before transfer, exact restoration of any changed preparations |
| `Staged` | Build permitted unpublished provisional destination and exact proved replacements where authorized, preserve source accounting, no public warlord success/history | Remove/prove provisional objects and restore exact original footprint before unlocking |
| `DestinationProved` | Prove exact territory/capital/actor preservation, exact destination formation and resource constraints, owner proofs and no extra units | Exact precommit recovery, no assumed success from effect calls |
| `SourceMoved` | Execute supported exact custody move or 019-approved recreate/prove/delete, prove exact source delta and no duplicated custody | Recovery only when every changed physical/owner fact is exactly reconstructible, otherwise quarantine |
| `CommitReady` | Prove every subtraction/addition, liability reassignment and frozen expected poststate, all participating owners agree on irreversible frontier | Exact recovery only while no participant frontier was crossed |
| `AccountingCommitted` | Write durable exact custody/obligation move and source tombstones, prove expected balances and actor outcome | Quarantine on failed proof, no lossy rollback/refund |
| `Finalizing` | Apply owner-approved public country/character package and diplomacy/war/history unlock in required order | Quarantine/diagnostic finalization failure, preserve ledger, no successful presentation |
| `Committed` | Prove public identity, actual war/diplomatic result, conservation and all terminal acknowledgments, record success once | Idempotent replay, later gameplay outcomes are new lifecycle operations |
| `Recovering` | Undo only manifested reversible changes, prove exact source/world/accounting restoration and removal of provisional replacements | Retry from retained cursor/ledger, never claim recovery from partial restoration |
| `Recovered` | Exact restoration proved, owner receipts mark completed compensation, release reservations | Idempotent no-op on repeated recovery, no duplicated refund |
| `Quarantined` | Retain both affected actors' transaction evidence, asset identity, receipts and diagnostic state, block conflicting mutation | Targeted owner repair only, no second release, new nonce retry or assumed clean state |

019's own sequence and helpers remain authoritative for 019 assets. In its current implementation, failed proof after accounting commit quarantines both actors. Its exact source recovery may recreate only missing frozen units and consumes its natural recreation recovery guard. 116 cannot bypass or reset that guard.

The existing shared release coordinator has a different specific frontier: `liberation_release_begin_finalization`. Its documented 005/006 country packages, politics, technology, forces, stockpiles and host air/naval transfers begin only after that point, failures there become `finalization_failed`, retain evidence, and never enter compensating rollback. A proposed 116 extension must map this frontier explicitly. It cannot promise 019-style recovery for 005/006 finalizer effects or declare later irreversible country setup reversible.

## 6. Transaction invariants

1. **Actual identity:** the selected general is an actual valid owned actor, existing 019 country/character participation preserves that same actor. A matching profile, display name, UID or cosmetic tag alone does not prove live character continuity. 067 deaths/removal remain effective.
2. **Single custody:** every manifested physical force/asset has one proved final custodian. During an approved unpublished 019 replacement stage, provisional duplication is locked and must resolve to exactly one surviving manifested set before publication.
3. **Physical conservation:** **source loss = destination gain + explicit proved loss**, for the attributed transfer, with exact resource variants/providers. Separately account any authorized external input rather than including it in the transfer-attributed destination gain. Every loss and external input must have an exact owner-approved reason and proof. An unexplained mismatch never becomes a transfer allowance. Casualties, battle damage and ordinary economic flows are not silently repaired. If concurrent engine changes make the comparison unprovable, abort before mutation or quarantine after mutation. Do not normalize toward a convenient total.
4. **Liability conservation:**019 debt/manpower obligations preserve their issuance identity, issued/paid/outstanding amounts and owner linkage. Transfers do not mint ordinary evolution history or reset burdens.
5. **Territorial truth:** prove owner and controller separately, cores and capital exactly as required, parent protected footprint intact and destination viable. A scripted call or country-exists flag is insufficient.
6. **All-or-proved-partial state:** success requires all participating owner acknowledgments. Partial/unknown outcomes retain manifests and diagnostics, never become clean rejection or published success.
7. **Freshness:** all dependent mutations revalidate their frozen actor/source/episode/revision. An invalidated dominance snapshot cannot be reused for terminal commit.
8. **Receipt isolation:** payer, source, destination, owner, episode, nonce and component identity must match. Historical tombstones survive cleanup as appropriate and cannot authorize new compensation.
9. **No free reversal:** exact precommit recovery is proved before refundable cancellation. Postcommit quarantine is not a refund opportunity. Later defeat is gameplay history, not an undo of formation/conquest costs.
10. **Bounded ownership:** iteration visits only registered actors, manifested assets, relevant states/routes and stored owner footprints. Work exceeding a supported iteration budget preserves the unvisited suffix/cursor, truncation cannot be treated as completed proof.

## 7. Existing universal cost names and proposed 116 adapter

The following names are documented existing shared helpers in the fully read universal cost source. Their definitions and complete input/output schemas are in `common/scripted_effects/chaosx_universal_cost_effects.md`. The parent fully read that definition in the 12-file root ledger. This appendix relies on that attributed global evidence and does not claim a second personal definition read. Complete-definition reading is therefore not a globally missing dependency. This table is a naming/lifecycle boundary, not invented script parameter syntax or live proof.

| Existing name | Documented responsibility | 116 adapter requirement |
|---|---|---|
| `universal_cost_quote_integer` | Quote ordinary current payable cost using family mask and positive quantum, final/displayed/saved amount and source proof | Quote for display and again at confirmation, use the exact final quote for payment/receipt |
| `universal_cost_check_quote_affordable` | Payer-scoped affordability for resource kind and final quote, no debit | Preflight every positive component and existing reserve/eligibility rules |
| `universal_cost_pay_component` | Debit one supported native resource component, payment result | Require exact supported resource/variant and actual debit evidence |
| `universal_cost_record_transaction` | Record transaction/component identity, ordinary/quoted/actual-paid amount, resource kind/source | Record each successful component once under the same logical action transaction |
| `universal_cost_refund_transaction` | Refund recorded actual-paid pending native components once, report partial outcomes | Only invoke when the 116 effect is validly refundable and restoration is proved |
| `universal_cost_mark_component_refunded` | Acknowledge an external owner-adapter credit | Exact unsupported resource credit must already be proved, acknowledgment does not itself pay a refund |
| `universal_cost_settle_transaction` | Prevent later refund and retain receipt proof | Settle only when the action cannot be cancelled/refunded, do not settle at preview/quote |
| `universal_cost_source_register`, `universal_cost_source_clear` | Register/upsert or clear one global discount source | 116 does not become a discount-source owner by using quoted costs |
| `universal_cost_rebuild_custom_quote_ratio_cache` | Rebuild composed trigger-readable quote cache | Preserve framework ownership, no duplicated 116 sale arithmetic |
| `universal_cost_source_register_black_friday`, `universal_cost_source_clear_black_friday` | Stable source 26 wrappers | Remain Event 026-owned lifecycle calls |

Documented quote value: `universal_cost_quote_displayed_cost`, equal to the final payable amount. Quotes are not locks or payment receipts. Delayed actions re-quote, source expiry does not rewrite actual-paid historical receipts. Zero stays zero, negative/reward values bypass discounts. This appendix adds no costs or discount tuning.

**New proposed `116CostActionAdapter`:** accept actual payer, exact target authority/context, ordinary cost provider and logical components. Validate current non-cost gates and all component affordability before debit. Pay/record successful components individually, preserve actual-paid proof on any later component/effect failure. Unsupported resources use an explicit owner payment/refund provider, never an approximated native token. Custom refund acknowledgment follows proved external credit. If payment happened but receipt recording cannot be proved, quarantine the debit with its evidence, do not retry payment or fabricate a recorded success. Failure between debit and recording is a capability/recovery case that must be closed before release.

Cost settlement and country-transfer accounting are distinct frontiers. A cancellation of a precommit action may refund only after exact authorized restoration. A completed action, irreversible finalization, postcommit quarantine or later defeat must not use an ordinary cancellation refund. A partial refund retains pending components and proof rather than claiming the whole action recovered. Duplicate clicks and retries cannot duplicate debit, refund or settlement.

## 8. Invalidation and cleanup requirements

| Cause | Required 116 response | Owner-specific state retained/handled |
|---|---|---|
| General defects or personally loyal forces change command | Invalidate affected source/member edges and readiness, obtain exact current actor/force receipt | 019 loyalty/obligations remain 019-owned, actual general continuity required |
| Liberation or subject freedom/autonomy | Remove or re-evaluate effective-command evidence for released territory/armies/routes | Country release and provenance remain registered release/package owners |
| Occupation, control or logistics loss | Mark relevant territorial/route evidence stale, recompute bounded footprint | Resistance/ordinary occupation history retained, no arbitrary new country |
| Random Civil War/ordinary war settlement | Observe actual winning country, surviving actors and changed diplomacy, invalidate old links | Winning dynamic country and actual assets persist, no scripted automatic rival absorption |
| 067 canonical death/permanent removal/government victory | Close canonical actor access and associated readiness, invalidate hierarchy command | 067 removes its owned networks/traits/package as authorized, no resurrection, no shared world-end reset |
| 019 derivative defeated but survives | Invalidate effective command as observed, keep actual remnant country/actor | 019 proof-gated defeat disables its package and records history, final annex cleanup is not implied |
| 019 actual final annex/destruction | Notify stored 019/provider lifecycle owner and wait for exact formation/template/provider cleanup proof | Keep private ledgers on failure, owner cleans only its tracked units/markers/identity |
| 116 terminal root defeated | Break/close 116 hierarchy and owner branch readiness as authorized | Surviving ordinary successor warlords, actual war outcomes, paid costs/history and shared terminal state persist |

Cleanup must match stored owner/episode/package UID. Clear only owned state markers using the registered footprint and exact owner guard. New-spawn eligibility is irrelevant to an existing cleanup obligation. A defeat notice does not authorize destroying all formations, clearing debt or dropping cosmetics. Final destruction must distinguish provider public teardown, exact tracked force/template proof, actor removal authorization, and receipt/history retention.

No recurring global scan is added to discover actors or repair ownership. Use targeted owner notices plus bounded reconciliation of registered participants and relevant assets. Existing pulse scheduling may revisit registered stale evidence, it does not expand into world-wide daily/weekly/monthly actor, state or division scans. Elapsed time/dates, where required by the core design, remain distinct from callback counts.

## 9. Save/load and multiplayer requirements

Persist transaction key, exact phase/frontier, manifest, owner acknowledgments, original recovery facts, pending components, actual-paid receipts, mutation/recovery cursors, invalidation revisions and terminal claim/commit state. Do not expose a committed success before its durable proof. Transient event targets/temp indexes are rebuilt from persistent exact identity and revalidated before use.

On load, resume only from the persisted legal phase. Before any mutation, confirm actual actor/country generation, owner mirrors, aligned ledgers and live physical state. A changed or missing actor before mutation cancels through exact preparatory restoration. A changed actor/asset after mutation enters the appropriate recovery or quarantine path, it does not start a replacement transaction. Postcommit uncertainty cannot revert to a refundable prepared state. Retain shared terminal state and automatic-event suppression after reload.

Owner interfaces must produce the same result for a repeated transaction key and identical inputs. The same key with different actors/assets is rejected as conflict. Keep tombstones/settled receipts sufficient to defeat repeated callbacks, replayed missions, load retries and duplicate UI clicks. A later generation/episode requires a new authoritative identity, not deletion of the old receipt to make it reusable.

In multiplayer, multiple clients may request the same action but only the authoritative synchronized owner can mutate. The implementation must establish a synchronized claim/reservation and deterministic validation order, no client-local flag or UI disable is a lock. Conflicting transactions against the same character, state, forces or payer components resolve before debit/mutation. All clients receive the same accepted key, phase, receipts and published result. Shared world-end exclusion must similarly provide one authoritative commit winner across 067/116/other branches.

Stable iteration/selection order and owner dispatch must be defined for the chosen engine implementation. Any random selection is resolved once by the authoritative episode and persisted before staging, not rerolled on load or client retry. Do not claim deterministic multiplayer behavior until duplicate requests, crossed invalidations, save/reload and shared-terminal competition have been exercised in the actual runtime.

## 10. Capability blockers and required implementer evidence

| Capability or missing definition | Blocking uncertainty | Required evidence/disposition |
|---|---|---|
| Live general movement | 019 natural claimant creation reproduces records, it does not prove preservation of an actual changing engine actor | Verified same actual character ID, traits, attributes, history, portrait and valid ruler/general roles, with no active parent duplicate. Until proved, reject the affected birth path before mutation. Reversible staged failure requires exact restoration. Postirreversible failure requires quarantine and owner repair, never a substitute profile |
| Ordinary exact force subset transfer | 019's approved recorded recreation is not a generic ordinary-army API | Supported exact custody move and preserved assignments/state, or explicit unresolved blocker, no arbitrary force-share substitute |
| Resources, stockpile variants, fuel/manpower and air/naval custody | Exact physical asset observations/transfer may differ by class | Class-specific conservation proofs and exact owner receipt, unsupported classes cannot be counted as moved |
| Dynamic country and viable footprint | Country creation, controller/core/capital behavior and synchronous recovery need proof | Actual parent/destination survival/control/capital/supply evidence and exact pre-frontier restoration |
| Subject effective army command and usable routes | Nominal diplomacy may not provide directed armies or observable supply/route authority | Verified command/delegation and route observation contracts, unknown evidence blocks counted domination |
| Shared release extension | Current coordinator registers 005/006 and has a specific irreversible finalizer | Distinct 116 owner/origin registration, host survival compatibility, phase mapping and full dependency reads |
| Shared terminal exclusion | Logical concurrent winner cannot be assumed from a flag | Registered shared claim/commit semantics and duplicate/competition/load evidence |
| 067 owner migration | Older actual `nr67` event differs from nine-part intended `nr067` system | Reconciled actual actor representation/lifecycle and acknowledged current Cohesion adapter, no assumed implemented pack |
| Universal cost adapters and runtime proof | Complete definition globally fully read by the parent. Proposed 116 adapter and live quote/debit parity remain unproved | Use the read definition and verify any additional required definitions/constants/providers. Prove supported resource paths and display/confirmation/actual-paid/refund/settlement, including debit-record failure handling |
| 019/provider transitive definitions | Monolith call sites do not establish every helper's full contract | Full reads of definitions actually used: transaction/management helpers, constants, provider callbacks, history/achievement, scenarios and retry queues |
| Cross-event notifications | 114/Mutiny/Resistance/settlement/Hunger Lines APIs not established by this appendix | Owner registration and inspected exact callback contracts before writes or lifecycle dependency |
| Identifier allocation | Shared identifier registry unavailable at inspected revision | Coding collision audit/workbook reconciliation before namespaces, enums, scenarios or callbacks become final |
| Serialization, callback scopes, multiplayer | No actual runtime proof | Save/load at each frontier, exact scope/cursor continuation, replay isolation and synchronized conflict cases |

Verification should cover the material boundaries, not mirror each helper's implementation: wrong/dead/replaced actor, existing 019 derivative participation without duplicate country/character, exact partial transfer recovery, failure after accounting/finalization, duplicate debit/refund/replay, liberation or defection between readiness observation and terminal commit, subject autonomy/route loss, 067 permanent removal, surviving 019 remnant versus final annex cleanup, and simultaneous 067/116 terminal requests. These are required evidence scenarios for later implementation, not tests performed in this planning pass.

An unresolved capability remains explicit in the implementation review. Do not reconstruct missing APIs from helper names, substitute cosmetic flags for military control, truncate a manifest to fit a loop budget, publish success from a partial receipt, or claim engine proof from repository comments. The parent core design can be accepted independently of these engineering gates, shipping the corresponding mechanism requires closing its actual blocker.

## 11. Boundary check against Parts 8 and 9

Parts 8 and 9 were fully read for this review. Their boundary requirements are reflected above: the bounded origin roster follows surviving political and military lineages, subject command covers current and future forces and war policy, political formation does not claim a world end, post-formation international readiness remains current, unknown observation invalidates proof, and all-world-end settings and exclusive shared authority are rechecked at terminal commit. The one-time baseline and bounded one-off proof jobs do not authorize recurring whole-world scans.

No remaining concrete owner or transaction boundary conflict was identified after these corrections. Live-character transfer, comprehensive continuous-control evidence, effective subject command, route observation and synchronized shared terminal commitment remain explicit capability blockers. This review does not accept or change any balance thresholds in Parts 8 or 9.
