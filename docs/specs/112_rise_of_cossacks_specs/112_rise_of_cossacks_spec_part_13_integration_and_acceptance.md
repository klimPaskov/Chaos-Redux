# Part 13. Integration, implementation order, and completion requirements

## Delivery boundary

This package is a complete design and implementation-planning deliverable.
It contains the gameplay rules, content paths, historical reasoning, proposed tuning, production inventory, future role assignments, and acceptance requirements.
It does not contain implemented game scripts, final localisation, produced art, edited catalogs, or runtime validation.

The intended specification destination is docs/specs/112_rise_of_cossacks_specs/.
A later implementation plan belongs under docs/plans/112_rise_of_cossacks_plans/.
The implementation owner should preserve the requirement and review crosswalk rather than treating these documents as a loose collection of ideas.

The [source reading and authority record](../../plans/112_rise_of_cossacks_plans/imported_review/source_reading_and_authority.md) records the historical supplied-source gate and exact hashes.
The [implementation usage map](implementation_usage_maps.md) records all twenty canonical future roles and fifteen workflow maps.
Those appendices distinguish documented tool families from tools actually exposed in this conversation.

## Identity migration

The user-confirmed identity is Event 112 Rise of Cossacks, originating from catalog row 122.
The canonical workbook currently has Rise of Cossacks at row 122 and Lootboxes at row 112; both rows are Unavailable, with Type, Chaos, and cluster fields blank, as recorded in the [current Event 112 evidence](../../plans/112_rise_of_cossacks_plans/112_import_evidence_2026-10-10.json).
The event-ID mapping is therefore 122 to 112, but the workbook migration is still queued for the parent-owned catalog alignment.
The original row 122 remains held against reuse in the parent-owned [shared identifier registry](../shared_identifier_registry.md), which also preserves the displaced catalog identity.
The historical user classification is recorded in the imported [final package audit](../../plans/112_rise_of_cossacks_plans/imported_review/review_evidence/curator/final_package_audit.md); it does not mean those blank workbook fields have been updated.
The shared identifier registry reserves the planning root `chaosx.nr112.1` for this user-confirmed identity, while the current evidence records that the runtime root is absent.
The reservation and its source evidence are linked from the [shared identifier registry](../shared_identifier_registry.md) and [Event 112 import evidence](../../plans/112_rise_of_cossacks_plans/112_import_evidence_2026-10-10.json).
The [historical closure and parent dispositions](../../plans/112_rise_of_cossacks_plans/imported_review/112_rise_of_cossacks_improvement_and_closure.md) remain historical evidence, not current catalog or implementation proof.

The implementation owner must identify all actual consumers before changing anything.
That includes root events, scheduler entries, settings, manual requests, eligibility, stages, evolution records, actor and event log metadata, details text, icon registries, arrays, counters, achievement predicates, scenario registration, and workbook rows.
A missing filename is not proof that an identifier is unused.

The pinned event-system constants also retain a 100-event baseline.
The full integration audit must determine how that baseline relates to current runtime indexing and capacity before Event 112 is registered.
It must not assume an out-of-range ID works merely because the catalog contains more rows.
Any required extension is coordinated across all actual consumers.

No new country tag is allocated by this planning package.
The working requirement codes are documentation references.

## Event, cluster, and evolution gates

The imported final package audit records the user-specified event classification as Chaos level 1.
The [current Chaos tier constants](../../../common/script_constants/chaos_meter_constants.txt) define tier 1 at Chaos 200, tier 2 at 400, and tier 3 at 600 (lines 20–22).
The design's direct Event 112 floor is tier 1 at Chaos 200, but the [current registry initializer](../../../common/scripted_effects/chaosx_logic_effects.txt) sets each event row to tier 0 unless it has an explicit exception (lines 159–184), so Event 112 requires a tier 1 binding before that floor takes effect.
Formables is current cluster ID 6 with `unlock_tier = 3` in the [cluster constants](../../../common/script_constants/event_cluster_constants.txt) (lines 20 and 262–268), a separate Chaos 600 invocation gate.
These current source values do not mean Event 112 is registered, and its independent availability remains separate from cluster invocation.

The imported [final package audit](../../plans/112_rise_of_cossacks_plans/imported_review/review_evidence/curator/final_package_audit.md) records Formables with Medium severity as the user-specified design classification.
The integration must separately bind cluster membership, severity, and member role to the actual current registry.
It must not confuse a Medium severity enum with an optional member role or overwrite unrelated cluster membership.
The event-side and cluster-side records must agree.

The Hosts Answer is the one selected substantive evolution.
Its exact tier 2 and Chaos 400 activation, prefire behavior, survival conditions, major-instability proof, cadence, caps, and lifecycle are in part 07.
Its eligibility, activation, and display add zero Chaos.
Concrete outcome contributions follow the cause-owned Chaos Impact Table.

## Shared-system ownership map

| Neighbor or shared surface | Required relationship | Forbidden shortcut |
| --- | --- | --- |
| Event 005 Soviet Collapse | Coordinate Don and Kuban carrier identity, dormant admission, state and character reservations, and meaningful existing trees | Reinitialize a living DHC or KHC |
| Event 006 Independence Wave | Use the shared dormant identity and release arbitration where applicable | Allocate a duplicate claimant or transfer a reserved state |
| Event 073 Mongols Rise | Treat a living Mongolian restoration as a possible partner or rival in the Horde route | Copy continent-wide claims or fixed cavalry grants |
| Event 048 Old Great Bulgaria | Use its inspected behavior only as existing implementation evidence | Copy broad instant cores and fixed army rewards into this dynamic host |
| Shared local crises | Admit and close actual instances with the three-crisis cap and player-pressure rule | Classify a regional rising as a worldwide exception to bypass the cap |
| Shared Chaos and history | Use actual cause, magnitude, actor, scope, repetition, overlap, and reversal receipts | Add Chaos for activation or duplicate shared war, annexation, or death effects |
| Shared universal costs | Use one actual quote for display, affordability, debit, AI, and permitted refund | Invent discount support for a native-owned raid field |
| Shared state ledgers | Own actual civilian movements through one measured transfer route | Treat military mobilization, a core, or a flag change as population movement |
| Native raids | Preserve RAID_INSTANCE scope, native reservations, exact target, and callback identity | Use a country helper with the wrong ROOT or charge native preparation twice |
| Country and character owners | Preserve actual living identity and existing content | Invent a duplicate person or use an empty tag as a historical claimant |
| CXT | Register relevant fixtures and readiness inertly, with actual test grants only through the documented player-triggered path | Fire Event 112 or replenish an army during periodic registration |
| Shared event UI | Parent owns the log, details, settings, and super-event framework integration | Assign shared framework ownership to an event-specific UI worker |
| Workbook and exports | Edit the true XLSX only in a later authorized alignment pass, then regenerate all required exports | Patch CSVs directly or claim this planning package changed the catalog |

## Private and shared architecture

Event 112 owns its founding selection, two public meters, host lineage, route commitments, evolution opportunity director, and cleanup.
Those are private event systems unless a genuine shared consumer requires a neutral interface.

The state, carrier, and character reservation problem is genuinely shared by several release events.
A neutral arbitration interface is appropriate.
Its design must remain independent of Cossack-specific politics or balance.
It should return an explicit accepted, rejected, or partial-commit disposition with actual ownership.

The event's dynamic opening is a frozen transaction.
The physical mutation owner controls state transfer, actual military debits, finite local grants, army initialization, and receipts in the correct order.
A second helper cannot apply the same material outcome because a tooltip or report also mentions it.

All recurring processing is bounded.
The director uses the accepted geography provider, current owner/controller cache, explicit participants, due dates, and pending work.
No new daily or weekly loop over all countries is authorized.
A long collection uses saved continuation and the documented iteration budget.
Changing callback frequency cannot change the amount of elapsed-time recovery.

## Exact dependencies to bind before gameplay construction

The complete installed state and province geometry is not bound in this package.
The parent-owned current tag/cosmetic inventory is recorded in the [import evidence](../../plans/112_rise_of_cossacks_plans/112_import_evidence_2026-10-10.json), but it is not a geography or admission audit.
Part 02 therefore defines actual geographic anchors and selection rules without inventing a complete state-ID or province manifest.
The implementation owner must build that manifest from the active installed map.
The current DHC/KHC history capitals of 218 and 234 are evidence about those country histories, not substitutes for map binding.

The exact native fielded-manpower, free-manpower, equipment-model, supply, formation-readiness, state ownership, country activation, and unit-creation contracts must be inspected.
A guessed average division size is not a replacement for fielded manpower.
A model-specific transfer must use an actual model-specific source and debit.

The occupied-state opening and exact formation defection need verified native war and unit behavior.
Their selected design requirements remain explicit.
They cannot be described as completed if the implementation only supports an ordinary owner-controlled state and personnel volunteers.
The complete-package acceptance matrix must identify every such branch.

Physical civilian return is selected content for P04, P11, P12, P14, and GP08.
It is optional for the player.
It remains a required implementation surface for the full package.
The older pinned exact-population helper differs from the newer supplied contract, so a current owner-approved implementation or adapter is needed before these movements execute.

The same distinction applies to the two custom model entities, the state puzzle, and all three super-event milestones.
Their detailed production and evidence requirements are planned here.
No runtime completion can be claimed while a required accepted row is missing.

## Implementation sequence

1. Reconcile the Event 112 and original 122 identity, carrier ownership, and required runtime capacity.
2. Bind exact installed geography, engine references, country history, character ownership, and native military recipes.
3. Preserve immutable weighted-source and scenario baselines before changing any probability surface.
4. Implement and validate the minimum complete one-state host, including capital, government, army, industry path, research, laws, focus loading, and recovery.
5. Implement the shared quote and receipt contracts, local settlement, charters, and military and economic development.
6. Add regional programs and practical modules with actual partner refusal, failure, and recovery.
7. Add the eight great projects with their exact state proof, political commitments, formation receipts, and postwar content.
8. Add The Hosts Answer through the bounded director and distinct real response types, including prefire activation.
9. Produce and integrate only the finite approved assets, flags, portraits, models, state-puzzle outputs, achievements, and super-event materials.
10. Run the domain, probability, visual, country, decision, focus, localisation, and completion audits against the final source revisions.
11. Reconcile documentation and, only when authorized, align the real workbook and regenerated exports with the actual implementation.
12. Make a completion claim that states what the evidence proves and preserves any remaining live-consumer limitation.

The sequence allows independent art research and bounded asset production once identity and consumer inputs are fixed.
It does not require all art to wait until every gameplay branch exists.
A changed model skeleton, state geometry, source file, or fixture invalidates evidence that no longer matches it.

## Requirement coverage

| Requirement | Owning specification | Design status | Implementation evidence |
| --- | --- | --- | --- |
| Immediate random valid East Slavic host | Parts 01 through 03 | Fully specified with geography provider and transaction | Future installed binding and country validation |
| Dynamic strength | Part 03 | Formula, caps, receipts, seven worked cases | Arithmetic checked, engine behavior future |
| Distinct host traditions | Parts 02 and 04 | Twelve families and fourteen substantial programs | Future country, route, writing, and asset validation |
| Confederation and centralized military state | Parts 04 and 05 | Institutions, costs, refusal, and first-peace tests | Future diplomacy and focus validation |
| Golden Horde and Cossack Russia | Part 05 | Full multistage campaigns and alternate settlements | Future exact map, country, political, and runtime proof |
| Sustainable modernization | Part 06 | Native templates, production, purchases, and training | Future native definitions and reinforcement proof |
| The Hosts Answer | Part 07 | Activation, prefire, cadence, response types, caps, and cleanup | Future scheduler, probability, and lifecycle proof |
| Decisions and missions | Part 08 and route owners | Thirty common action families and detailed route missions | Future exact quote, timer, completion, and AI proof |
| Complete country and grounded characters | Part 09 | Carrier adapters, office fallback, four named candidates | Future full collision audit and source-first portraits |
| Focus tree | Part 10 | Twenty strategic groups and complete program crosswalk | Future node expansion, layout, reachability, and AI proof |
| AI and balance | Part 11 and system owners | Priorities, proposed targets, and integrated fixtures | Future source-backed comparisons |
| UI and assets | Part 12 and asset prompt | Finite consumer inventory and production criteria | Future visual and binary evidence |
| Achievements and super-events | Dedicated prompts and part 12 | Eight achievements and three milestone briefs | Future exact predicates, art, text, audio, and framework proof |
| Integration and source authority | This part and appendices | Identity crosswalk, role map, all-source ledger, blockers | Targeted repository reads complete, remaining implementation sources explicit |
| Improvement loop | Review and disposition document | Actual near-completion findings and closure recorded before delivery | Design review only, not gameplay validation |

## Completion discipline

A file count or a successful script return is not proof that the event works.
The final implementation must show which requirements each source, fixture, render, receipt, and comparison covers.
It must also state what those artifacts do not prove.

The parent retains integration and acceptance responsibility.
Specialist auditors can identify and repair bounded defects within their assigned scope.
They do not independently choose a new country identity, discard an accepted route, or waive a missing source.
A new reusable issue belongs to its shared owner rather than an Event 112 workaround.

This package may be delivered as a completed specification while future engine and production gates remain open.
It must be called a specification.
The final planning report must be honest about the fully read supplied sources, the targeted repository and historical research, the actual design arithmetic, and the absence of runtime execution.

