# Event 016 raid-lifecycle implementation checkpoint

Date: 2026-09-02.
Status: reviewed implementation checkpoint, not tranche acceptance or Event 016 completion.
The final completion contract remains binding, and tranches 5–8 remain open.

## Implemented surfaces

- Portal breaches record the exact province, attacker, and original defender, and maintain only participant-owned state registries.
- The original defender can seal a recaptured breach in 21 days for 25 Command Power; loss of the province cancels sealing without clearing the breach.
- One idempotent cleanup effect owns sealing, peace, invalid participants, containment, and terminal cleanup without reversing extraction or clearing permanent history.
- Biological operations select one of six authorized agents, produce actual native equipment, stage operations without reserving payload, and own independent battlefield/covert deployment receipts.
- Battlefield releases take seven days and one payload; covert releases take fourteen days and two payloads.
- The Portal-assisted battlefield variant reaches hostile rear areas for ten Teleportation Equipment, saved in the same decision-owned receipt and refunded only with that transaction.
- Target ownership and control remain bound to the original victim; spent transport is validated from the receipt, not charged a second time or required in the remaining stockpile.
- Capitulation returns the independent reserve before native capture; direct annexation transfers any still-reserved cargo once to the winner and clears the former actor's receipt.
- Native raids retain their reservation and outcome ownership; staging affects outcome factors and AI willingness but does not override the native preparation timer.
- Ordinary Alien API calls reject invalid reservations before materialization and refund the one ordinary reserve before clearing its state target.
- DHR's medium rebellion tier includes ten or more arrivals below the high-tier Chaos threshold; the high tier retains precedence.
- CXT exercises only local reconciliation and safe initial biological selection, without creating a breach, raid, payload, or release.

## Source review and meaningful cases

The decision/mission reviewer checked exact 2/4/1 factory availability, private production callback ownership, selected-agent validity, route and victim rechecks, production cancellation, staging cancellation, independent payload settlement, native dispatch acceptance, and deliberate-versus-accidental zombie attribution.
The Portal variant preserves conventional targeting, rejects unfunded rear targets, stores the paid method, accepts a pending operation with zero unreserved transport, and returns payload plus transport on invalidation.
Clearing the debit receipt makes capitulation followed by annexation or a delayed decision callback a no-op for the same cargo.
The final timer review found that clearing production and staging receipts alone did not release their native timed-decision factory modifiers.
Explicit cancellation on inactive country, missing own receipt, or lost authorization now ends those timers without a completion payout; start and completion callbacks use the same active-country gate.
The final dispatch review moved success-only Directorate Exposure inside the canonical dispatch-accepted branch; a rejected execution consumes the attempted payload and records failure, not successful delivery.
These are source-level transaction checks, not live engine execution.

The shared zombie strike helper captures its actor/victim/target inputs before changing scopes, so native raid variables and decision temporaries use the same consequence path without fabricating offensive use for a home accident.
The ordinary-pathogen dispatcher must accept delivery before success history is written.
Black Plague uses the native plague equipment type plus its existing exposure pipeline, without calling a second payload-debit entry point.

## MCP and weighted evidence

The full Portal state-flow report at revision `be62dbc1cef10dcf5e81586c9848456dbe3caeea1813b344f9c4da84cc4230be` indexes the actual raid helper file and the active-beachhead flag.
Its selected file contains eight accesses, one producer, one clear, and zero subject-local issues.
The report still includes unknown/inferred scopes and global unresolved entries; it is not proof of exact in-game transaction execution.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8be27f27a70a3c19138f290ff432ba6b2f8d1fdee02c9ea63d46918f0a5f09f2/d4a18ddf3cb7a650a1825b369cedff1101bcc542c3248cd8c44373f36cb89177/event-state_flow-be62dbc1cef1.json`.

The matching full state render contains the requested `helper:brilliant_scientist_portal_register_beachhead` and the actual Portal raid/landing/extraction helpers, unlike the earlier focused fallback render.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/beed1ebbcfa9b15860c5bb1ff1f7681ef79902332aa2fe35d9c57d61a0960b56/c1cc951fed2d68d6df3c02bcdf2a3c884a9e14717d65ac254b98b15c201201c9/event-state-be62dbc1cef1.json`.
Global validation reported 3,950 blocking diagnostics; this count is not attributed wholesale to Event 016.
Comparison against the older `f9b65b464e4880b782f3f153b251bdc285b68d8628454aaf3fdf1d2ada499baa` full revision returned `EVENT_REVISION_NOT_CACHED`.
The second exact-revision comparison, from `07e7dbe505daba6fea655653ee648602cd1f75da32d1b734928286ca79ce5c50` to `be62dbc1cef10dcf5e81586c9848456dbe3caeea1813b344f9c4da84cc4230be`, also returned `EVENT_REVISION_NOT_CACHED` with zero artifacts.
No before/after event graph comparison is claimed.

The biological outcome pool resolves to battlefield success/failure/accident 70/25/5, staged 85/15/0, covert 55/30/15, and staged covert 70/20/10.
Analysis: `probability-9ffbdc27d23dd5a9d3f52466`; consult the probability handoff for its stored scenario hash and artifacts.
The five-case Portal target baseline is explicitly partial: `probability-d5182adc518cde3a6feb74ad`, scenario hash `f6c367901f29100dfe19655fc917e03c8b2ab87c588ba3aa2324ea050a6af03f`, 28 unresolved inputs.
Nested actor/target fixtures were rejected by the adapter, so no exact target eligibility or click timing is inferred.

Map inspection confirmed province 6521 belongs to state 64 and has actual geometry in the installed map, while separate global position diagnostics remain unresolved.
No map data was rewritten.

## Design blocker requiring a decision

The Portal raid destroys its assigned formation and reconstructs the locked six-battalion cadre at full readiness.
This preserves formation count but does not conserve its exact remaining manpower, equipment composition, damage, or experience.
The installed documented API exposes no exact-unit relocation or lossless unit snapshot/rebuild mechanism.
`teleport_armies` operates on a state with a country-owner filter and would move unrelated formations.
The capability audit is appended to `016_final_raid_event_mcp_2026-09-02.md`.
No state-wide relocation, extra replacement cost, or other substitute has been approved or implemented.
Portal formation-conservation acceptance therefore remains blocked pending a user-approved design.

## Other open gates and shared ownership

- Native staging's preparation-duration improvement is not implemented as a timer override; the native timer remains unchanged, explicitly documented rather than claimed complete.
- Actor/target probability fixtures, remaining comparisons, and full biological state-flow acceptance remain open.
- Event 026 is concurrently modifying voluntary Alien reservation costs; only Event 016's three reservation-validity/refund hunks belong to this checkpoint, and the exact 2,000-gun conservation contract remains under coordination.
- An explicit Alien capitulation gate is queued for the shared reservation-adapter review; current state-loss cancellation exists, but a separate capitulation predicate has not been added in this checkpoint.
- All seven 3D packages, firearm effects/audio, final export/reimport, focus reward review, Directorate GUI, remaining lifecycle findings, final planner/auditors, and catalog alignment remain open.
- The events skill records the verified focused/full MCP evidence distinction in its existing MCP evidence section.
- No game launch or live-game acceptance is claimed.

## File ownership

Gameplay ownership covers the Event 016 raid lifecycle constants, biological decisions/triggers/effects/scripted localisation, two normal decision categories, Portal containment decision, Portal raid helpers/triggers, participant-only on-actions, four native biological/zombie raid files, the narrow zombie consequence scope fix, DHR tier predicate, CXT adapter, and the three ordinary Alien reservation guards.
Presentation ownership covers Event 016 project and raid localisation, existing generated sprite reuse, biological/Portal/Alien system documentation, the closure contract, and the curator's named historical-ledger reconciliation files.
No new model, sprite identifier, focus, country, evolution, super-event, achievement, public meter, or GUI was introduced.

## Guidance used

The implementation followed `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`, with `chaos-redux-mtth` used by the read-only weighted-logic reviewer.
The documentation review consulted `chaos-redux-focus-trees` for its retained structural focus evidence, while the separate existing-model inventory used `chaos-redux-3d-model-pipeline` without changing model files.
The skill maintainer used `skill-creator` to update and validate `chaos-redux-events` in its existing MCP evidence section.
Relevant offline wiki, installed vanilla, source-scope, transaction, and tool capability evidence is cited in the specialist handoffs rather than duplicated here.

## Follow-up evidence

`016_final_timer_transaction_audit_2026-09-02.md` records the completed source review and the owner fixes for timer teardown and rejected dispatch.
Parent review corrected its initial conflation of biological Portal transport receipts with native raid division reconstruction, corrected one localisation filename, and qualified the base decision-view render as not executing Event 016's dynamic rows.

`016_final_raid_probability_2026-09-02.md` records the corrected DHR source-backed comparison, `probability-d491f178da340465bfd521d0`, with nine identical saved conditional tier scenarios, zero unresolved pool inputs, and no changes to that pool.
It does not validate the changed tier-helper predicates or the 90-day pulse cadence.
The earlier analysis-ID-as-source calls were invalid and are explicitly superseded, not treated as an unavailable adapter.
Exact pre-patch biological source bytes were not retained with the earlier audit, so the final Portal/Bio before-and-after comparison remains unproven; the previous target evaluations also remain unresolved.
This evidence-retention failure belongs to the implementation workflow and is not a game-engine limitation.
Recovery must use an authenticated earlier source snapshot, such as retained task-tool history verified against the artifact hash, or explicitly establish a new source-frozen baseline for the next change without claiming it proves the earlier patch.

Final frozen biological source hashes: decisions `a1ed2f6d7b6e1e6296e1e415c0ecce4e925a912c75897d27f4a182ad715b920c`, triggers `02afa9bdb79aafa80d1ae7430d54e5ca576dc7b8053940ac4ae3ae1da2e7268d`, and effects `ded6a1dbf25aa8adb7c8aba20905fb349ed4cac4a7eb45efae4e12f4e511450d`.

Remaining timer-review dispositions:

- Accept the vanilla-backed decision timer and factory-occupation patterns; retain variable-backed Alien mission timeout.
- Queue the unrelated existing mission-timeout constant support checks for the lifecycle/presentation tranche; this checkpoint does not convert those fields.
- Queue the Portal transport and selected-payload equipment texticons, biological category density review, and actual populated decision-row rendering for tranche 6 presentation.
- Preserve the external `remove_decision` cleanup warning as a future-caller contract; no such biological caller is currently present, so no global cleanup hook is added.
- Keep Event 026 quote conservation and the explicit Alien capitulation guard under shared-adapter coordination.
- Keep the native Portal landing redesign unimplemented until the user approves a conservation-preserving alternative.
