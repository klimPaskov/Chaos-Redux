# Event 105 technical research and implementation handoff

## Decision and evidence boundary

This source contract was promoted by the recorded planning-parent acceptance in [review dispositions](105_random_idea_review_dispositions.md) and [architect research](evidence/105_architecture_research.md#parent-disposition-after-research).
The 10 October import preserves that reported design disposition as history, while the authorized task imports and reviews documentation only.
Current workflow, root/catalog findings, and parent-owned import evidence are linked from [README](README.md#current-import-review-10-october-2026).
Pinned research below remains historical, and named source paths are future implementation targets.
The user's 10 October 2026 choice accepts planning IDs 105 Random Idea and independent 104 Rule, as recorded in README.
The user authorized adopting uploaded IDs and migrating the catalog on 24 October 2026. Random Idea is current catalog identity 105 and former row 110 is historical provenance; Rule is 104 and former row 107 belongs to Lootboxes. See the [shared identifier registry](../shared_identifier_registry.md#imported-event-identity-proposals). This changes identity metadata only; implementation and runtime availability remain separate.

The design requires the complete effective loaded set of technically addable national ideas.
Use supported native runtime discovery if the installed engine exposes it.
Otherwise implement a generated registry for the complete effective active loadout after proving its resolution and native dispatch contracts.
A smaller maintained or curated pool is not accepted by this package.

This is a planning handoff.
No Event 105 gameplay implementation, registry generator, runtime pool, generated final asset, HOI4 inspection artifact, or live playtest was produced here.
The named helper and file proposals below are implementation targets, not claims that those definitions already exist.

All public repository inspection is pinned to commit a3ef485c5da7e2337122eca04ac65c175050f251 in klimPaskov/Chaos-Redux.
The supplied source bundle was the planning-session workflow authority where it differed from that checkout.
Current repository AGENTS.md and owner skills govern future implementation workflow.
The current user brief governs Event 105 and the connection to Rule 104.
Exact source references appear in 105_random_idea_research_sources.md and the reading ledger.

## What the reference investigation establishes

| Question | Evidence found | Conclusion and limit |
| --- | --- | --- |
| Is there a documented complete idea database iterator? | The offline Data structures game-array table names global technology and several other database collections, but no all-ideas array [R1, lines 1779–1815] | None was documented in the inspected snapshot. This does not prove that the current installed engine has no newer capability |
| Can known ideas be represented as tokens? | Idea token values, token equality, GetTokenKey, and token substitution are described [R1, lines 955–985] | Known-identity dispatch is a plausible native route. Tokens do not discover unknown definitions |
| Is the generic token table an idea registry? | Raw effect names and other language tokens can also tokenize [R1, line 985] | Walking token integers is not a valid type or completeness proof |
| Do ideas have their own scope? | The reference says ideas have no ordinary idea-object scope [R1, line 551] | A country scope selector cannot be assumed to operate on idea tokens |
| Are hidden and empty ideas automatically invalid? | Empty national ideas are described as addable, and hidden ideas as ordinary spirits with hidden display [R2, lines 30–45 and 317–319] | Their lack of visibility or usefulness does not justify exclusion |
| Do normal selection restrictions establish non-addability? | The reference says direct add_ideas bypasses allowed, while false do_effect can suppress modifiers without removing the idea [R2, lines 247 and 344–354] | Selection UI conditions and useful local effects are not the technical eligibility boundary |
| Does every token in common/ideas belong in this event? | Separate law, advisor, officer, designer, character-slot, and idea-category behavior is documented [R2, lines 405–485] | Effective national-idea type must be resolved before inclusion |
| Is an advisor-looking identifier necessarily excluded? | The inspected Chaos definition puts TUR_nuri_demirag under country [R9] | Identifier shape is not a category test |
| Can a native addition trigger further effects? | on_add, on_remove, cancellation, and replacement are documented [R2, lines 218–247] | Post-dispatch absence cannot prove that nothing happened |
| Does load order simply mean the last idea ID wins? | File override and replace_path behavior are described, but duplicate database-entry precedence is explicitly database-specific [R4, lines 257–288 and 511–519] | The IDEA-specific duplicate-ID rule remains unverified |
| Can current numeric token values safely identify ideas forever? | Token IDs index an engine-memory table [R1, line 957] | Saved identity rebinding across changed loadouts requires evidence |

The offline snapshot contains older-version discussion, while the pinned mod descriptor declares support for 1.19.* [R10].
The snapshot is required project reference material, but it is not proof of the user's installed engine behavior.
The Windows installed-game documentation and actual enabled game loadout were unavailable in the historical planning environment.

## Native discovery investigation to complete first

Inspect the installed dynamic-variable, script-concept, effect, trigger, idea-category, and idea documentation through the actual exposed reference tools.
Search for complete idea-definition iterators, arrays, category enumerators, idea tokens, direct-add effects, and native validity checks.
Do not assume the spelling global.ideas or global.idea is valid merely because another database has a global array.

If a complete iterator exists, document its owning scope, element type, ordering, default entry, custom category coverage, DLC behavior, and whether it exposes never-owned and inactive event ideas.
Compare its complete output against the resolved active-loadout definition inventory.
Include a small fixture mod adding an unmistakable technically valid national spirit that no country initially owns.
The new identity must appear without teaching Event 105 its identifier.

An engine-owned array may contain a reserved object, but a zero value or first position is not enough to identify one.
Prove registration order, initialization, and the consuming native effect's validity rule before omitting that entry.
All real loaded identities must remain covered.

Separately prove the dynamic known-ID dispatch path.
Discovery, category classification, token substitution, ownership testing, and native addition are separate capabilities.
A successful test of one does not establish the others.

Do not discover addability by experimentally adding every possible idea to real countries.
Discovery is read-only metadata work.
Behavioral probes belong in isolated implementation fixtures whose execution and effects are explicitly recorded.

## Generated registry route

### The active loadout is the input

The generator must receive the actual game build and the actual selected playset, including enabled descriptor order, dependencies, DLC mounts, disabled content, local overrides, and the relevant source files.
Scanning every installed workshop folder would include inactive content and fail the loaded-game requirement.
Scanning only the Chaos Redux repository would omit most of the intended universe.

Resolve the effective virtual file set before collecting idea IDs.
Same-path replacement, dependency ordering, replace_path, file evaluation order, and duplicate database identities are distinct operations.
The parser must reproduce the installed engine's behavior for each one that affects the result.
Do not collapse them into an unsupported generic last-mod-wins rule.

The offline Modding source also records capitalization-related loading behavior [R4, line 559].
Use the installed environment's actual path semantics and preserve evidence for case variants instead of silently changing filenames or merging different inputs.

### Structural parsing and classification

Parse Clausewitz structure, including nested blocks, repeated keys, quoted strings, comments, encoding markers, and the effective idea-category definitions.
Do not use a regex that treats every outer token or every occurrence of an idea name as a national idea.
Resolve custom idea_tags categories and their native consumers.
The literal categories country and hidden_ideas are important precedents, but they are not an authorized whitelist that discards every other mod-defined national-idea category.

Unknown category classification is a completeness issue.
Resolve it from installed documentation and native evidence, or mark that loadout's registry unready.
Do not silently ship the resolvable subset as the whole pool.

Keep one selectable row per effective exact identity.
For each row, preserve the winning definition, category, source path, source revision, and the evidence establishing technical national-idea membership.
Maintain an exclusion ledger containing actual type or load-resolution reasons.
An excluded row must not say foreign, harmful, empty, hidden, DLC-specific, useless, incompatible, missing icon, or unsafe callback as its sole reason.

DLC entitlement and definition loading are different questions.
The offline snapshot notes that scripts may live in base files behind has_dlc conditions while DLC folders carry other content [R4, lines 269–278].
A purchase-restricted interface condition is not an independent Event 105 filter when the national idea is actually loaded and directly addable.
The generator must use the content the engine loads, without inventing access to unavailable files or duplicating DLC definitions.

### Generated outputs and activation

Produce a versioned manifest of the full resolved universe, exact identity bindings, classification and exclusion evidence, loadout fingerprint, and the generated native dispatch and ownership-test structures.
The generated component should refer to the original definitions rather than copying their modifiers, callbacks, or localisation into new spirits.
It must not alter idea definitions or broadly replace their directories.

A game-start on_action can initialize already generated data after the engine loads it.
It cannot be assumed to scan arbitrary files or run an external generator.
If generation is a pre-launch step, provide a deterministic tool command and a generated compatibility component that is actually enabled in the playset before launching the game.
That preparation cost must be described in the implementation documentation.
Do not advertise it as automatic runtime discovery.

Regenerate when the game build, effective idea files, category definitions, active descriptor order, dependencies, mounts, overrides, or relevant generator version changes.
Checking only the number of ideas is insufficient because two different universes can have the same size.
The manifest must match the generated code, source loadout, and save-identity migration state.

If the engine cannot itself read the launch manifest or detect a changed external loadout, enforce readiness in the pre-launch tooling and document the resulting limitation.
Do not promise an automatic in-game stale-registry check unless it exists and has been verified.
The event cannot silently continue with a known stale or partially generated set.

### Registry approval gate

The complete-loadout route may proceed after proving the exact overlay, duplicate-ID, category, dispatch, and identity-persistence contracts for the supported engine.
If an active mod cannot be resolved completely, record the specific parser or classification blocker.
The implementation may not remedy that problem by removing an entire source mod's otherwise addable ideas or shipping only the vanilla and Chaos subset under the original feature claim.

An opt-in extension API may exist for other project purposes, but it is not the completeness mechanism for this event.
The inspected CXT extension path requires registered setup contracts, and actual empty hidden CXT carriers exist [R7–R8].
Those facts establish neither arbitrary definition discovery nor an exclusion rule for the carriers.

## Exact random selection

For a given draw, use the complete loaded national-idea universe minus current exact ownership and identities already dispatched or reserved by the same firing for that country.
Refresh current ownership between dispatches.
An initially held idea that is removed by a prior callback can become eligible later in the same bundle if Event 105 has not already attempted it there.
This is conditional uniform selection from the current eligible set.
It is not a promise that the final retained set is a uniform subset of the initial ownership snapshot.

Prefer an exact eligible-set selector with verified integer random bounds.
The offline reference describes inclusive lower and exclusive upper bounds for the relevant random-variable primitive [R1, lines 564–595].
An inclusive design range requires the proper native upper-bound conversion.
Do not round a continuous random number to create whole counts, since that can give unequal endpoint probabilities.

If performance requires segmented storage, select a segment in proportion to its current eligible identity count, then select an identity uniformly within that segment.
Uniform selection of source files or equally weighted unequal segments biases the result.
Recompute or invalidate affected eligible counts when callbacks change ownership.

A bounded rejection loop can stop short even when valid candidates remain.
For example, with ten eligible identities among ten thousand, one hundred independent proposals still have about a 90.5% chance of accepting none under the ideal static model.
That is an illustrative mathematical example, not a measured game-pool size.
Use a finite complete traversal or exact fresh pool instead of treating an arbitrary retry count as exhaustion.

The project and offline reference describe a 1,000-iteration ceiling for relevant effect loops [R1, lines 1219 and 1828].
Work chunks may respect that ceiling, but the pool may exceed it.
Every continuation preserves its cursor, unvisited suffix, country, firing identity, chosen identities, count target, and random-state semantics.
Never truncate a registry to the first thousand entries or restart a chunk at the beginning.

Performance evidence must use a pool above that boundary and a representative large country roster.
Report pool size, country count, examined identities, native dispatch count, continuation count, elapsed tool time where available, and persistent-state growth.
A planned budget is not proof that the engine meets it.
No daily whole-world rediscovery or polling loop is introduced by this event.

## Native dispatch and callbacks

Treat one native addition as irreversible from Event 105's point of view once it begins.
An arbitrary selected definition can execute callbacks that are not fully observable or reversible.
The event's idempotence boundary is its own dispatch receipt, not a claim of a transaction covering every foreign script.

Before dispatch, validate the country, exact identity binding, technical category, current ownership, and firing-local distinctness.
Store a receipt identifying the firing, recipient, exact identity, and dispatch-started state before entering the native effect.
This prevents synchronous re-entry from dispatching the same slot again.
Call the native addition once.
Then observe current ownership separately.
At the final immediate-settlement checkpoint, save the observed retained set for the Chaos contribution and result presentation.
Later native changes must not rewrite that saved observation.

| Observed condition | Required behavior |
| --- | --- |
| Candidate became owned before dispatch | Skip it without consuming a draw and refresh the remaining set |
| Binding is proven invalid before dispatch | Do not execute it, record the technical fault, and continue only if the remaining complete universe is still known |
| Native dispatch returns and the selected identity is held | Record dispatch and immediate retention separately |
| Native dispatch returns and the selected identity is absent | Keep the consumed draw, record absence, and do not retry |
| A callback removes or replaces a previous result | Preserve the callback's result and update retention at settlement |
| A callback grants another candidate | Exclude that now-held identity from later direct dispatches |
| A callback re-enters Event 105 | Reuse the shared request/firing guard and prevent duplicate or recursive grants |
| Execution becomes uncertain after dispatch starts | Preserve the receipt and unresolved state, avoid retry or compensating removal, and expose the diagnostic |
| The recipient ceases to be valid | Stop its remaining dispatches without redirecting them to an unrelated country |

A no-op add to an already-held idea is not a successful fresh draw.
A post-add has_idea result is an ownership observation, not an engine callback receipt.
Without an authoritative return value, the implementation may report dispatch performed and retained observed, but must not label every dispatch native-success-proven.

Nested callbacks may also request another legitimate event firing.
The outer Event 105 work retains immutable context until settlement.
Use the existing scheduler to defer a separate legitimate request if supported, or reject recursive re-entry with a clear diagnostic.
Do not recursively execute another whole-world Event 105 grant while the first firing is open, silently create another firing identity, or reinitialize the RNG per country.

Native callbacks may still contain assumptions that fail outside their original system.
That is a material consequence of the deliberately broad pool.
Do not respond by applying a compatibility blacklist or changing the selected definition's own script.
A technical inability to apply the object as a national idea remains the membership boundary.

## Persistent identity and burden

Persist the semantic exact idea key and its direct-dispatch history for each country.
This requirement does not assert that a normal HOI4 numeric variable can store an arbitrary string.
The implementation must choose and prove one of the following mechanisms.

| Mechanism | Required proof |
| --- | --- |
| Native saved token values | Save loading rebinds each token to the same idea key, including after harmless registry reordering and supported loadout changes |
| Generated stable keyed storage | Persistent keys are derived deterministically from exact idea identities, collisions are checked, and regenerated ownership/dispatch access resolves the same key without relying on a new ordinal |
| A generated persistent manifest and migration mapping | The old manifest remains available, every old identity maps exactly or becomes an unresolved tombstone, and missing manifests cannot silently reset or misidentify history |

A raw token integer or dense registry ordinal alone is not sufficient.
Missing old identities retain their historical meaning and contribute zero burden while absent.
They must never become a different idea merely because the regenerated registry reuses an index.
Reappearing identities recover their own history under the explicit intersection rule.

The historical set may grow to the finite number of distinct directly drawn identities.
Keep counts and latest outcome summaries separately from detailed pending-report data.
Do not preserve every country's entire world history as an unbounded matrix solely to support Storm burden.
Native or callback-created indirect ideas do not acquire direct receipts through a before-and-after ownership diff.

Before any global dispatch, capture C, roster, all B values, and the effective stage from the current evolution permissions.
Preserve those inputs through any chunking or callback interruption.
Use current ownership only for the individual draw and immediate-settlement observations.

## Proposed owner boundaries

Event-local symbolic helper names may be finalized during implementation after collision checks.
Keep the complete Event 105 lifecycle in its own effects file.
A helper moves to the shared dynamic registry only when it has a genuine second neutral caller and a documented reusable contract.

| Planned responsibility | Inputs and ownership | Required result |
| --- | --- | --- |
| Validate universe | Current engine/registry and loadout identity | Ready, genuinely empty, or exact unresolved technical reason |
| Capture firing | Shared firing identity and valid country roster | Immutable C and all recipient B/count snapshots |
| Build or refresh fresh set | Complete universe, current owner, current firing's attempted set | Exact eligible identities or exact count with an unbiased selector |
| Draw identity | Complete current eligible set | One uniform exact identity, with no effects yet |
| Dispatch identity | Owner country, firing identity, selected exact key | Once-only dispatch receipt and separate retention observation |
| Refresh burden | Stable historical direct-dispatch identities and current ownership | B and optional current member set |
| Settle firing | Captured roster and this firing's direct receipts | Final immediate retention, one Chaos contribution, report and history context |
| Continue bounded work | Immutable request context and cursor | No dropped suffix, reroll, duplicate, or country-scope leak |

Every caller initializes the temporary scalar and array outputs it consumes before each helper call.
Re-entry must not overwrite those outputs or an unrelated ROOT, FROM, event target, or current recipient.
Use explicit recipient context, because ROOT does not automatically become the current country inside every iterator.
Temporary outputs are not a safe substitute for durable context across native callbacks.

## Historical repository integration and implementation targets

At the pinned research revision, the complete inspected events directory contained numbered event files through 100, with no Event 105 or 110 file in that directory.
Targeted indexed searches for chaosx.nr105 and random_idea also returned no matches, but those searches alone are not an exhaustive negative proof.
The inspected docs/specs directory likewise had no Event 105 package at that revision.
Plan the proposed root chaosx.nr105.1 as new work at this pinned revision, subject to the final exact namespace audit, while preserving the user's requested To Be Reworked design metadata.

| Surface | Targeted implementation action |
| --- | --- |
| events/105_random_idea.txt | Add the canonical triggered root and thin event-owned dispatch/report entry, with required grants in hidden immediate resolution |
| common/scripted_effects/105_random_idea_effects.txt | Own discovery binding, quantity, country resolution, direct receipts, burden, settlement, and bounded continuation |
| common/script_constants/105_random_idea_constants.txt | Centralize event identity and all accepted thresholds, Storm arithmetic, per-dispatch result codes, and retention-award tuning after schema inspection |
| common/scripted_effects/chaosx_logic_effects.txt | Register 105 as minor repeatable, extend relevant arrays through the actual highest registered ID, and integrate readiness before automatic dispatch |
| common/scripted_effects/chaosx_events_log_effects.txt | Add premise/details, supported evolution rows, immutable result-summary linkage, and explicit actorless history context |
| common/scripted_effects/chaosx_settings_effects.txt | Integrate existing enablement, evolved-opening permissions, and manual/debug entry without a new event-owned settings UI |
| common/on_actions/chaosx_on_actions_system.txt and the established event dispatch path | Verify shared routing and once-only behavior, without adding routine whole-world polling |
| common/scripted_effects/chaosx_event_cluster_effects.txt and common/script_constants/event_cluster_constants.txt | Reconcile the named Randomizations member through the existing cluster contract after its identity audit |
| common/scripted_localisation/chaosx_scripted_localisation_events_log.txt | Add Event 105 name, premise, stage, and saved-result selectors in the correct scopes |
| localisation/english/chaosx_event_names_l_english.yml, _chaosx_events_l_english.yml, and chaosx_gui_l_english.yml | Add implementation-stage public wording and exact dynamic values using the established encoding and namespace rules |
| Existing achievement definitions, shared achievement hooks, and event-owned achievement effects | Implement the two exact accepted contracts after verifying native war, country, state, and industry measures |
| Existing report GFX and gfx/achievements/ | Register accepted final art and the two exact achievement triplets |
| docs/events/105_random_idea.md and docs/achievements/105_random_idea/ | Document implemented behavior, validation limits, ownership, and achievement tracking |
| docs/spreadsheets/chaos_redux_events_catalog.xlsx | Resolve the scoped Event 105 and Rule identity conflicts, then mirror implemented public wording and export all three CSVs through the existing exporter |

The pinned event system allocates its event-array bound from the highest registered ID plus one [R12, lines 1424–1436].
Do not replace that with a literal total count when adding a sparse ID such as 105.
Its repeatable handler records history and handles cap/pacing state [R12, lines 1162–1204].
Run readiness and actor-context preparation at the appropriate pre-fire point, so an empty technical result cannot be mistaken for a successful completed grant after a generic history row has already been written.
If a race or callback causes a later fault, preserve an honest fired-attempt result rather than erasing shared history to hide the fault.

The inspected default weight, cap factor, and recovery values are 1000, 0.5, and 20 [R13].
Use current player settings and the existing repeatable framework instead of inventing a separate cooldown, weight recovery system, or fixed percentage chance for Event 105.
No probability claim for the event's campaign frequency is possible without the full current active event pool.

The supplied CSV names Randomizations as cluster 14, but the pinned implemented cluster constants register 1–8 and 12, with no Randomizations definition in the inspected cluster initializer [R14].
That is a catalog-to-implementation discrepancy, not proof that 14 is freely allocatable.
The canonical workbook, active spec reservations, and complete shared identifier registry must be checked before binding or reserving the cluster number.
This package preserves the name and Medium severity and allocates no new shared numeric ID.

The supplied event CSV labels 105 Anti-player ideology, 107 Rule, 109 Custom laws with a national-spirit premise, and 110 Random idea with a different premise.
The current user explicitly supplies Random Idea 105 and Rule 104.
Those records were reconciled by the user's 24 October 2026 authorization to adopt uploaded IDs and migrate the catalog. Preserve the old row observations as historical evidence; do not copy an old row wholesale or renumber unrelated implemented content.
The workbook was not supplied or inspected in the historical planning session, and no catalog file was changed by it.
The historical parent check confirmed those catalog identity conflicts and the absence of roots for 104, 105, 107, and 110 at that time, with all four workbook rows Unavailable.
Requested To Be Reworked remains design metadata. Identity migration does not change runtime availability or authorize a Playable status.

## Implementation completion gate

The planning package is complete when its accepted contracts and review dispositions are coherent.
The event implementation must satisfy the complete pool, stable save identities, native dispatch and callback behavior, count and selection rules, presentation, both achievements, final assets, shared integration, and catalog reconciliation, with meaningful available evidence and no known defect or unapproved simplification.
Use actual-source probability calculations and direct reference/source checks where MCP analysis is unavailable, under the current bounded retry rules.
Absent optional inspections or renders limit verification without universally blocking otherwise finished implementation.
An unresolved capability necessary to deliver the complete pool or an exact achievement predicate remains a real implementation obstacle.
User-owned game testing is neither requested nor awaited for agent delivery.

Use 105_random_idea_acceptance_and_usage_maps.md for named scenarios, owner routes, and expected evidence.
Missing MCP tools in the historical session did not block its planning handoff.
Those receipts establish no current tool absence, native proof, or implemented gameplay.
