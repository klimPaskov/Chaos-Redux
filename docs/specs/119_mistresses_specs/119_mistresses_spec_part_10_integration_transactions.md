# Mistresses: integration, simultaneous revolt, and conserved mergers

## One crisis with a continuous history

The welcome relationship wave, screening response, Unveiling, brood war and Mother of Mothers belong to one persistent crisis. A person removed during screening must remain removed when the revolt is prepared. A civilian who survives a state seizure must remain alive under the new controller. A brood that absorbs another brood must inherit its surviving forces and history without receiving a second copy of either. The event log, settings and interface must describe the same committed state that the simulation uses.

This chapter specifies ownership, ordering and observable results. Its transaction names describe obligations for implementation. They are not claims that the engine provides atomic transactions, arbitrary data structures, safe rollback or multiplayer player transfer. Exact population formulas belong to Part 2, revolt eligibility and deployment budgets to Part 5, country and unit packages to Part 6, focus rewards to Part 7, and Mother qualification to Part 8. The contracts here bind those chapters together.

## Ownership of public and hidden state

Public Confidence and Investigative Reach are the only two persistent event-owned public values. Both remain bounded from 0 to 100. Existing national resources, individual case evidence, casualty records, map ownership and finite war objectives remain available through appropriate interfaces. None becomes a public infestation percentage, brood growth meter or Mother progress meter.

| Information or action | Authoritative owner | Publication and persistence |
|---|---|---|
| Event identity, phase, activation generation and consumed ordinary roll | Event 119 coordinator | Saved once, with an explicit migration version |
| Public Confidence and Investigative Reach | Participating human country | Saved values, coherent read-only projections for the GUI |
| Person truth, adult eligibility, original household and network membership | Immutable person record | Hidden and saved before screening admission or visual publication |
| Evidence creation, provenance, reliability and consumption | Case and investigation owner | Saved observations, with only player-available evidence published |
| Portrait and alias assignment | Identity publication owner | Saved when assigned, independent of truth, shared by every client |
| Local cells, relationship cohorts and institutional access | State and original-host registry | Hidden, with immutable provenance and explicitly mutable location |
| Physical civilian gains, losses and transfers | Shared population and cohort owners | Measured receipts, then event-specific attribution |
| Brood country, forces and package readiness | Brood registration and package owner | Saved generation and asset ownership |
| War membership, world threat, world-end exclusivity and event history | Existing shared owners | Event supplies registered inputs and consumes shared results |
| UI selection, navigation and presentation | Screening GUI | Selection may change, simulation truth may not |

The country that currently holds a record is not automatically its original host. Every case, cohort, brood and reward keeps the original host identity across capitulation, liberation, country transfer and merger. Stable registration IDs and generation IDs identify entities. Array positions, temporary targets and mutable country names do not. The shared scripted-system and state-ledger references require this separation of immutable provenance from mutable binding. [S1] [S2]

The human response follows the surviving government or its approved successor. Its main national focus tree remains intact. Alien countries receive complete dedicated packages. Nonhuman classification changes eligibility for human systems, but it does not change the species or survival status of civilians who remain in their states.

### Registered participation and bounded work

Admit countries and states when an actual event operation creates a cohort, person, case, institution link or occupation obligation. Register their successors through ownership, control, annexation, liberation and country lifecycle hooks. Remove an active-work entry only when it has no pending obligation. Retain historical provenance after active participation ends.

Monthly relationship and case work visits a stable batch of registered participants. A persistent cursor and generation define the batch. A due date belongs to the obligation, so a controller change does not restart its clock or grant an extra monthly benefit. Unvisited entries and unacknowledged receipts survive a save, retry or early exit. An invalid entry is recorded and deferred or retired according to its lifecycle, rather than causing the whole queue to be cleared. [S1]

The exceptional world census occurs once during Unveiling preparation. It reads the shared known world-state registry in bounded portions and must finish before the revolt commits. It includes uninfected human territory because Mother qualification measures worldwide success, not the infected subset alone. Prefer an existing complete shared snapshot when it meets the same date and provenance contract.

That census freezes human civilian population weights, industry weights, the six world-region assignments and original host capitals. The six regions are Europe, Asia, Africa, North America, South America and Oceania. The mapping from installed engine geography to these design regions is explicit, with each state assigned once. Later ownership and control hooks maintain holdings caches. Monthly work does not repeat the census. Human population available for protection, death or evacuation is tracked separately from the frozen territorial weights used by Part 8.

Existing shared human-state modifier registration performs broad work in the inspected repository. A monthly event loop must not call that broad registration once per state. The integration owner must use a bounded lifecycle adapter or coalesce the necessary shared refresh at the owning boundary. This is a performance and ownership requirement, not permission to introduce a parallel human classifier.

Accrued birth obligations use Part 2's household eligibility and dates. The shared `apply_state_population_gain_without_recruitable_manpower_gain` returns the measured addition and removes event-created immediate recruitment credit. Record that measured result once. Closing the covert phase settles already accrued requests without granting future timer births or erasing earlier newborns. [S3]

## Saved cases, deterministic actions and safe refresh

Part 3 establishes person truth when the finite underlying person enters the simulation. Screening admits a lead concerning that person. It does not create a new truth draw. Visual identity is published once when required, without allowing its sampler to inspect truth, reliability, alien role, protected traits or image source.

Use the authoritative game simulation for all permitted random draws, in a documented stable order. Store the chosen results. Clients must not use local clock time, filesystem order, image download order, UI hover, search filters or open-window count to choose identities, evidence or outcomes. Identical saved state and the same ordered actions must produce identical case assignments in multiplayer.

An investigate, spare or purge action identifies the exact person generation, case generation, actor and allowed action state. It revalidates authority, target existence, investigation capacity and every spent resource before any irreversible effect. A stale card publishes a refreshed unavailable state. It does not retarget the next person in the list. One action receipt prevents repeated charging, repeated deaths and repeated network disruption.

Investigation completion consumes its own saved evidence procedure. Reopening the interface cannot redraw it. Pre-action prices, enabled controls, cooldowns and previewed rewards must not expose hidden truth. After an irreversible action, physical accounting remains truthful. An innocent lethal purge records one actual human death, while an alien purge removes one alien adult and no human population. Any inference from that completed outcome is distinct from a preview oracle. Part 3 owns the evidence model and the later independent proof required for vindication or accountability.

The screening window `mistresses_screening_window` and scripted GUI `mistresses_screening_gui` read a coherent published generation. They may refresh while paused. A refresh must never create people, draw evidence, apply births, debit resources, complete an investigation or recompute a verdict. During Unveiling or a relevant merger, it displays the defined transaction-lock state and then switches to the completed generation. Pending GUI delivery and pending simulation work are separate facts. Coalescing refresh notifications must not discard unfinished work. [S1]

### Nested calls and reentrancy

Normal private saved state owns long-lived transaction identity, participant membership and completion receipts. Temporary variables remain scratch space. Callers initialise documented outputs before nested shared helpers. They preserve participant references in an appropriate private frame before a helper can overwrite temporary values or event targets. A saved event target alone is not proof of an immutable snapshot. [S1]

Ownership callbacks raised during a transaction enqueue relevant lifecycle refreshes. They do not start a second revolt, merger, Mother entry or case consequence for the same generation. Drain that queue after the current publication boundary. Distinct inner and outer iteration guards prevent a nested helper from prematurely terminating its caller. No design assumes an undocumented iteration capacity.

## The Unveiling as a simultaneous logical transaction

The player should experience one coordinated revelation. Preparation may be bounded across scheduler work, but the irreversible resolution must not give an earlier processed country extra game time to act against a later one. The implementation must establish a supported dispatch boundary that prevents ordinary simulation and player choices from observing half of the committed revolt.

This is logical simultaneity. The design does not claim native database-style atomicity. Preparation performs every check that can fail without consequence. A saved transaction journal distinguishes prepared, committed and published work. Once a physical loss or transfer has happened, recovery reconciles its measured receipt and continues the same transaction. It must not restart a speculative calculation and repeat the physical effect.

### 1. Freeze the participating world

Record the phase generation, accepted participants, eligible states, original hosts, current owners and controllers, adult alien cohorts, protected human population, institution access, surviving network links, current cases, wars and available assets. Finish the worldwide denominator census before this record is sealed.

A host with no viable surviving revolt network can have no outbreak. Country order cannot introduce a minimum revolt everywhere. Case removals committed before the boundary affect this snapshot. Unresolved investigations retain their receipts and transition according to Part 3. They cannot finish halfway through preparation and silently change one country's already frozen force budget.

The snapshot records proposed absorption, territory and adult alien deployment budgets using Parts 2 and 5. It distinguishes original aliens, absorbed human victims, surviving human civilians, existing soldiers and newborns. None is substituted for another because the engine exposes a convenient single manpower value.

Part 5 permits at most one initial brood per pre-revelation host. Prevalidate its whole-state allocation, host population cap and nonoverlap before commitment. A severe one-state takeover requires the specified verified government or player continuation. An unsupported continuation is a release gate, not permission to delete the host or invent a new map state.

### 2. Preflight the entire resolution

Validate every target generation, current ownership proof, remaining protected floor, valid passable land, intended brood registration, capital location, country package, unit family availability, equipment obligations, human continuation and shared world-state conflict. Check that the common alien faction and required war relationships can be established.

Reserve identifiers through the actual audited registries. Do not infer a free tag or namespace from its absence in one filename search. No country receives units before it owns valid land and has a valid capital. An inaccessible or impassable seed state fails preparation before population is destroyed to fund an impossible country.

If a state changes hands during preparation, invalidate its proof and rebuild the affected prepared portion before commitment. Do not silently reinterpret an old host's protected population as the new controller's available recruitment pool.

### 3. Apply measured human absorption under valid human scope

The shared `apply_exact_state_civilian_population_loss` rejects a state with a nonhuman owner or a nonhuman controller. Therefore the default Unveiling order applies authorised absorption while both holders still satisfy the human eligibility contract, before alien classification or state transfer. The caller supplies the documented protected minimum, reason and human victim attribution and consumes the measured applied result. [S3]

The result, rather than the requested amount, drives civilian deaths, remaining survivors, alien resource conversion and any Part 5 force budget that depends on absorption. The death logger receives the actual measured loss once, with physical state population application disabled in that secondary logging call. Turning off death reporting does not undo or suppress the authorised physical population loss.

Some legitimate cases may already have a nonhuman holder when a later operation becomes due. Those require an explicit shared human-cohort adapter with authoritative surviving-human proof, exact physical accounting and the same protected-floor guarantees. Temporarily clearing nonhuman classification to pass the generic helper is prohibited. An event-local raw population subtraction is not an acceptable substitute.

If the actual applied loss is below the request, use the smaller result. Do not manufacture the difference as a second loss, a reserve credit or free troops. A zero applied result produces no death entry and no absorption-funded credit.

Service partners belong to a distinct existing service cohort. Their loss uses a verified military-casualty adapter and is excluded from the civilian subtraction. If exact fielded removal is unsupported, the equivalent service-reserve adapter must be established and validated before release. Neither a civilian death nor an alien recruitment credit may stand in for an unperformed service loss.

### 4. Preserve survivors and complete authorised evacuation

State seizure does not erase the remaining human population. Preserve state-local survivor records and original-host attribution under alien occupation. Human civilians do not become alien manpower by changing a country flag.

Evacuation uses the shared physical transfer owner. Prevalidate the origin floor, destination authority, reception capacity and route before debit. The event submits its cohort and route proof. The shared owner performs the actual origin loss, transit deaths and destination gain and returns the measured results. The event must not also apply a matching raw gain or loss.

For each completed transfer:

**Actual origin debit = actual route deaths + actual destination credit.**

The residual must be zero. Reception capacity and load update symmetrically at state and country scope. Integration of an arriving cohort is a status change, not another population addition. An interrupted or invalid route retains its unsettled obligation and never fabricates a refund that duplicates civilians. [S2]

An illustrative accounting fixture begins with 100,000 eligible human civilians. If an authorised absorption request produces an actual loss of 18,000, 82,000 survive before other measured effects. If a subsequent evacuation removes 5,000 and credits 5,000 elsewhere without route deaths, the occupied origin retains 77,000 and the destination gains 5,000. The total human loss is 18,000. This example tests conservation only. It does not replace Part 2's population formula or authorise those particular loss rates.

### 5. Establish land, country identity and package

Transfer each prepared state to its intended brood and set a valid capital before country setup that requires it, OOB loading or unit deployment. Record control and ownership separately. Mother qualification separately uses Part 8's durable-holding receipt, including qualifying 30-day wartime control without an ownership rewrite. After a control loss, even alien-owned territory must regain that receipt through a new 30-day admission.

After the intended alien marker is established, call the shared nonhuman cleanup through its documented owner. `clear_nonhuman_country_human_systems` retires incompatible human institutions and views. It does not kill civilians, grant stockpile refunds or clear historical human death records. The new country must retain the surviving-human occupation obligations explicitly. [S3]

Apply the complete package from Part 6, including permitted research, laws, characters, ideas, AI, templates, names, flags and future continuation. Persistent characters follow the current country-history recruitment guidance where applicable. An older helper example does not override the newer supplied event integration contract.

### 6. Settle adult force and equipment budgets

Use the actual adult alien reserve and measured conversion receipts from the preceding phases. Newborns remain civilian births. Individual screening subjects do not each represent a hidden division or thousands of victims.

The authoritative Part 2 conversion is surviving adult infiltrators plus the floor of half the actual measured absorbed civilian and service adults. The one resulting adult-alien budget is partitioned between fielded formations and remaining reserves by Part 6. It is not granted once as manpower and again as a separately funded army.

Each new formation has one owner for adult manpower and one owner for each required equipment debit. An OOB equipment factor controls initial unit fill. It is not proof that national stockpile was consumed. The deployment owner must reconcile observed stockpile and unit equipment before and after creation, including engine automatic consumption if the verified method has any.

The initial organic equipment entitlement in Part 5 is an explicitly authorised transformation grant. Record it once against the funded formations and their preparation level. Captured human equipment is a separate measured transfer from an actual existing stock. The organic grant does not prove a human stockpile debit and cannot be counted again as captured equipment.

For each equipment family, the committed identity is:

**Opening stockpile + authorised grants + receipts from transfer = closing stockpile + paid deployment or action cost + other measured outflow.**

Existing formations that change owner keep their surviving equipment. They do not also grant an identical new stockpile. New formations cannot receive both a direct unit grant and a stockpile grant presented as its already paid equipment. Partial payment must not launch a full-cost action.

Organic unit integration follows the current provider registry contract supplied to Part 6. Reserve three numeric family IDs and one shared Event 119 provider ID at or above 500 after audit. Register exact aligned rows idempotently, with visual profile 999 and the specified `family_only` Event 19 policy. The owner implements family-aware `chaos_unit_family_provider_[PROVIDER]_event19_<hook>` callbacks with active-brood, reveal and package-readiness guards. The default `pay_management_action` does not charge the organic costs and is insufficient. Provider-owned cost and spawn receipts are required. Central Event 19 family lists and dispatch maps do not receive bespoke Mistresses branches. [S14] [S15]

### 7. Establish the common war and publish

All broods belong to the same alien side. They do not declare war on one another, inherit contradictory enemy relationships or become hostile because they have different original hosts. Preserve valid human wars and add the intended invasion relationships through one shared war owner.

Only after population, country, unit and war receipts reconcile does the transaction publish its new phase. Coalesce map caches, screening views, decisions, focus availability, world threat and event history. Original-host records continue to describe what happened even if the host has capitulated.

A reload after commitment but before presentation delivers the missing presentation once. It does not respawn the revolt. A failure before physical commitment leaves the prepared work recoverable without charging or killing anyone. If the native engine cannot support the required irreversible boundary or post-failure reconciliation, that is a release blocker for this transaction, not evidence that a generic helper can supply it.

## Brood contact and forced merger

### A component, one frozen recipient

Broods merge when their valid controlled land touches. The graph includes active brood generations as nodes and qualifying direct land contact as edges. Exclude sea adjacency, merely neighbouring national borders without the required control, invalid deployment terrain and disconnected stranded occupation that does not satisfy the Part 6 contact rule.

Resolve each connected component from a frozen graph. If A touches B and B touches C, all three belong to one component even if A does not touch C. Choose one recipient before transferring any donor. Later transfers in the same transaction do not increase a candidate's rank.

The frozen lexicographic ranking is:

1. Higher effective surviving adult alien land-force strength.
2. Higher usable owned-and-controlled military industry.
3. Lower immutable brood registration ID.

Strength uses the actual surviving adult combatants in fielded eligible units, with launch combat-equivalent weights of Cadre 1.00, Line 1.50 and Siege 3.00. Apply the native strength normalisation once. If an actual manpower measure already reflects casualties, do not reduce it again by the same casualty factor.

Legitimate surviving alien formations inherited in earlier completed mergers count once in their current owner. Exclude pending deployments, civilian population, allied expeditionaries, ordinary captured human formations, duplicate references and assets only inherited during the present component transaction. The exact native measurement requires installed-engine verification. Division count alone is not the specified strength.

The conceptual request `MERGE_COMPONENT(snapshot_id, member_generation_ids)` receives the frozen membership and returns one recipient, per-donor completion receipts, asset reconciliation and continuation results. It denotes a design interface. It is not a proposed new engine command.

### Transfer obligations

Before any donor disappears, capture its eligible assets, outstanding obligations and controllers. The recipient's own assets form the opening set. Every donor contributes each asset once, keyed by its stable origin or a native identity that has been verified to survive transfer.

| Asset or obligation | Required result after merger |
|---|---|
| Owned and controlled land | Preserve the union, with separate ownership and control facts |
| Human survivors and displaced cohorts | Preserve physical people, original host, location, status and unsettled transfers |
| Adult alien reserves | Sum valid remaining reserves once, without converting human civilians |
| Land units | Preserve surviving strength, equipment, experience and identity where supported |
| Air and naval assets | Account for all that actually exist, including deployed and stored assets, with no assumed annexation behaviour |
| Stockpile, equipment variants and fuel | Preserve measured holdings and valid designs once, respecting native capacity and transfer semantics |
| Factories, infrastructure and buildings | Preserve territorial assets without replaying their construction rewards |
| Research and production capability | Union compatible researched technology and valid designs, reconcile exclusions and unfinished progress explicitly |
| Research slots | Retain the highest earned entitlement, with provenance, rather than adding identical institutional grants repeatedly |
| Characters | Keep living eligible characters and roles once, including donor commanders, without duplicate recruitment |
| Focus completions and rewards | Preserve completed receipts, permanent territorial results and compatible unlocked capabilities |
| Active missions, costs and deployments | Rebind their remaining obligation to the recipient or settle a documented invalidation once |
| Faction, wars and diplomacy | Retain the alien side and valid union of enemy obligations without brood-on-brood wars |
| Original host and event history | Preserve immutable source identities, victim attribution and prior log entries |
| Human controllers | Complete a verified continuation before donor retirement |
| Mother and her objectives, if active | Rebind her unique host once while retaining the real lair state, guardian identity, fixed relay set, mission commitments and consumed relocation |

Annexation is a transfer mechanism only to the extent its native behaviour is verified. It is not a blanket proof that every listed asset moves. Read actual before and after state for categories whose native transfer is automatic, then apply only the missing authorised transfer. Do not combine automatic inheritance with a duplicate scripted credit.

The existing `union_compatible_researched_technologies_from_donor` is useful for its documented subset. It does not transfer research slots, annex the donor or preserve every mutually exclusive branch. It deliberately respects conflicts such as concentrated versus dispersed industry and flexible versus streamlined production. [S3]

The recipient retains its active mutually exclusive route and associated modifiers. Donor knowledge, usable equipment designs and unfinished research remain recorded as inherited capability with their origin. Compatible capability must remain usable. Mutually exclusive capability must retain a supported dormant or equivalent representation without activating both exclusive modifier sets. Merely writing an archive row is not evidence that a lost gameplay asset has been conserved. If installed-engine capability cannot preserve the specified research, design or progress result, the destructive merger remains blocked for that case until the implementation owner establishes a supported equivalent. A future helper name cannot remove this limitation.

The same principle applies to focus rewards. Preserve donor permanent results and compatible unlocks, then mark their reward receipts as already delivered. The recipient keeps its chosen political route. It does not rerun a donor's focus rewards, gain a second initial factory package or stack duplicate starting spirits. Part 7's maximum of three focus-owned active spirits remains in force after merger.

Mother upgrades or replaces command slot 1. Her defeat replaces that slot with the command aftermath. Strategic settlement slot 3 remains available for occupation policy. A merger cannot create a second Mother spirit or a fourth focus-owned spirit.

### Player continuation is part of the transaction

The merger is mandatory when its contact and eligibility rules are satisfied. A donor player does not receive a veto that prevents it. Their continuation is nevertheless a precondition for retiring their playable country.

For a single human donor and an AI recipient, transfer control to the recipient using a verified supported path. Prepare the recipient package and queue any required delayed bootstrap before the player-switch operation. In the documented current integration pattern, `change_tag_from` is the final effect in the relevant country block. Do not continue executing donor setup under an assumed unchanged player scope. [S1]

For multiple human controllers, prove that the installed multiplayer environment supports the intended shared recipient control or a defined supported observer and recipient handoff. A saved receipt identifies every affected player and their resulting control. Silently converting a human to AI, disconnecting them, sending them to a vanished tag or pretending an ordinary country effect changes network ownership is unacceptable.

This capability is unverified in this design session. Implementation must resolve it before the forced multiplayer merger is enabled. A short protected pending transaction is permitted while the supported handoff completes. A permanent refusal path, arbitrary weaker recipient or silent loss of a controller is not.

### Commit and reconcile

Freeze graph, rank, assets and controller destinations. Validate the recipient's land, capital, package and shared side. Transfer or reconcile assets in a documented order, then retire donors only after their obligations are acknowledged. Record each donor's consumed generation.

Publish once for the component and refresh only affected participants. New contact caused by the committed merger belongs to the next graph generation. Repeated callbacks for the old edges cannot merge the same donor again. If a donor disappears through an external effect before commitment, invalidate the component proof and rebuild from current registered participants. If it disappears after a recorded transfer, reconcile that transfer rather than crediting the snapshot again.

## What the inspected Zombie implementation actually supplies

The pinned public source is commit `41bc4e5045a7b5c131be69dda2f08079d478634c`, dated 18 October 2026. Eight assigned files were fully read and their hashes recorded. These are implementation precedents, while the newer supplied instructions and the user's event requirements control this design.

In `002_zombie_outbreak_effects.txt`, `annex_neighboring_dynamic_zombie_outbreaks_to_main` annexes eligible neighbours into fixed ZZZ using `transfer_troops = yes`. `transfer_dynamic_zombie_successor_to_main` also transfers a successor into ZZZ. `promote_strongest_dynamic_zombie_successor_to_main` calls the scorer `strongest_dynamic_zombie_successor`. The inspected scorer calculates ten times division count plus controlled-state count. It does not calculate weighted surviving alien combatants. [S4] [S5]

In `zombie_special_project_effects.txt`, `weaponized_zombie_resolve_canonical_standard_neighbor_merges` compares current division counts pairwise. Equal counts take neither annexation branch. A separate same-type manual-scenario path in `weaponized_zombie_expand_against_neighbors` compares division counts and gives its actor the tie. Neither function freezes a whole connected component or proves the complete asset union required here. [S6]

The Zombie spawn paths provide a useful ordering precedent by transferring land and assigning a capital before OOB loading and unit creation. `can_host_zombie_outbreak_state` excludes impassable states. Other Zombie paths classify the new country before those transfers. That classification order cannot be copied ahead of Mistresses human absorption because the shared human loss helper would reject the state afterward. [S4] [S6] [S7]

The inspected Zombie on-actions use daily and weekly broad work. Current Mistresses requirements instead use registered bounded participants and lifecycle updates. The source verifies that different Zombie merger mechanisms exist. It does not verify the user's shorthand description as one universal existing algorithm. [S8]

## One invasion, neighbouring events and identifier migration

The requested design identity is Event 119 Mistresses. The original catalog identifies Mistresses as 130, while current 119 is Random New Alliance. Original 158 Tomorrow's Girls supplies the related adult alien invasion concept, and original 162 Tin foil hat supplies the anti-alien coalition response. These facts create a migration obligation, not permission to overwrite a live namespace. [S9]

Before implementation, inventory the workbook, runtime namespace contents, flags, settings arrays, log IDs, localisation, super events, world-end rows and any save migration rules. The bounded repository filename scan found no runtime filenames matching 119, 130, 158 or 162. It did not perform a complete namespace-content audit and does not establish that any identity is free.

Reserve 119 for this requested design through an explicit migration decision. Preserve Random New Alliance's existing identity and historical meaning by the approved relocation or retirement route. Legacy numeric 119 alone must never be interpreted as proof that Mistresses fired. A legacy Mistresses 130 bridge requires recognisable Mistresses provenance and schema, then maps to one current activation without firing the ordinary event again.

Tomorrow's Girls must not run a second independent invasion after this system has claimed its alien crisis generation. Preserve its thematic content within the one Mistresses phase owner and record any legacy activation bridge once. It contributes no additional ordinary-event fired count, duplicate adult cohort, second revelation or parallel Mother.

Tin foil hat may remain a distinct response event identity. Its coalition joins the existing human defence against the actual revealed threat. It consumes the shared crisis phase and war context, never invents a second alien presence or makes all human nations omniscient during the covert opening. Coalition membership, leadership replacement and surviving participation follow the established faction owner. Relevant achievements and history use committed outcomes rather than the mere availability of the response.

The workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the editable catalog authority. Update it only when the migration is concrete, then regenerate the derived CSV with the documented exporter. Do not edit the CSV as an independent source. Event, world-end, super-event, scenario, family and provider numeric IDs have distinct registries. A suggested next ID is not a reservation.

## Settings, history and the playable world-end

### Ordinary settings and history

The base event remains Minor Fire-Once with its proposed opening Chaos and date rules from Part 1. Its ordinary-roll registration, timer and fired count use the shared logic owner. Settings actions enter the same guarded setup contract. A repeated manual request cannot duplicate an active system.

The two evolutions use the existing evolution enablement, MTTH scheduler and history machinery. Part 5 specifies their proposed 90-day base MTTH inputs, conditional 0.50 factors, ordering, evolved-opening exceptions and saved 30-day or minimum 90-day response deadlines. Threshold crossing unlocks the schedule rather than directly firing an already-active evolution. Eligibility unlocks do not create Chaos by themselves. A concrete consequence owns any Chaos change. Disabled history or evolution entries do not become falsely marked as recorded. Use the correct event, type, stage, tier and actor context, including an explicit no-actor state where needed. [S13]

The normal random history path can record an event before its immediate effects. Prepare any required actor context at the proper pre-fire boundary. The opening record must describe what the world can know at that point. It must not reveal alien truth through its name, portrait, tooltip, details or debug selector visible to normal players.

History records what occurred. Event Details previews what the event can do. The preview has no invented occurrence date. Related evolution history and the main history entry use shared selectors and stable identity. Event-owned screening GUI workers do not edit the shared event log, settings or super-event framework.

### Mother registration and exclusivity

Mother of Mothers has a public, default-enabled world-end registry row with a stable identity reserved after the full audit. Its persistent enablement uses the existing disabled-scenario ledger and registry rebuild owner. It is distinct from any optional manual triggerable-scenario identity. The inspected world-end constants explicitly preserve existing numeric identities and append new ones. The inspected triggers test membership of `global.disabled_world_end_scenarios` and keep manual launches separate. [S11] [S12]

Part 8 owns the exact qualification predicate. This chapter consumes its one authoritative result. In particular, Chaos must be strictly above 1,000, the world-end owner must be free, and sustained success in the defined world regions must be demonstrated from frozen pre-Unveiling weights and the authoritative durable holdings. Those holdings can include 30-day supplied wartime control without changing the human legal owner. Initial allocations and their recaptures never earn recent-gain credit. Relevant lifecycle hooks invalidate a broken qualification streak immediately between five-day emergence checks. Exactly 1,000 fails. A temporary achievement of a threshold must not bypass the specified consecutive qualification period.

Mother entry claims the shared world-end owner once and suspends ordinary automatic global rolls worldwide. It records the scenario and super-event presentation through their existing owners. The playable Mother war, its defence objectives, occupation obligations, existing investigations where still meaningful and local brood aftermath must remain active. Shared callbacks that blanket-disable all work on `world_end` require an explicit audit so they do not accidentally stop the requested survival game.

Her actual character and lair belong to one valid host. Other broods remain regional administrations under the common command. Entry does not annex noncontiguous countries. A later host merger rebinds the unique Mother record without moving the lair's physical state, rerolling relays, duplicating the guardian or refunding commitments. A genuine relocation uses Part 8's separate one-use transaction. Its receipt cannot be reset by merger or reload.

The coalition's final mission has one shared owner and one commitment receipt. Allied contributions attach to that mission. Host changes revalidate its current target bindings without creating a second payment or a second victory. Total military destruction remains a valid defeat route and cannot be blocked by an orphaned guardian or relay record.

Entry is not reversed because Chaos later falls. Defeating Mother breaks supreme coordination and removes her specific advantages. It does not delete local broods, human survivors or existing wars. Part 8 determines the surviving war state.

World-end recovery follows Part 8's 30-day consolidation and clears only the ownership held by this exact Mother generation. Before ordinary automatic rolls resume, the shared owner must establish that no other terminal transition or active world-end claim requires suspension. Preserve historical entry and disablement settings. A generic `clear world_end` operation is insufficient and must not reopen unrelated terminal branches. The defeated Mother never respawns in that campaign.

World threat is a separate shared aggregate. `refresh_world_threat_state` currently enumerates registered source flags, so Mistresses must register its source through that owner and request a refresh. It must not set `world_in_threat` directly or clear another event's threat. Mother defeat may reduce its own source while living broods continue to qualify as a threat. [S3]

### Optional manual scenario entry

If the project exposes a manual scenario version, it uses the separate triggerable-scenario registry and launch contract. It is not a second ordinary event or an automatic Mother bypass. The documented four intensity choices and final confirmation must read the actual selected launch values. Cancellation is consequence-free.

A manual scenario may bypass ordinary Chaos, date and evolution prerequisites only through the explicit manual contract. It still rejects impossible package setup, duplicate active generations and conflicting world-end ownership. Clear temporary bypass state after setup. Reuse idempotent setup and accounting owners instead of maintaining a divergent manual invasion implementation. [S10]

## Acceptance evidence required before release

The following are future checks. None is claimed as executed against HOI4 in this design session.

| Case | Required observable result |
|---|---|
| Clean host beside heavily infiltrated host | One can have no revolt while the other loses only its prepared eligible states |
| Human owner with nonhuman controller | Generic civilian loss is rejected, with no loss or credit until an authorised cohort adapter resolves it |
| Requested loss exceeds protected floor | Actual measured loss controls every dependent receipt and death total |
| Death reporting disabled | Physical authorised loss occurs once and reporting remains disabled |
| Evacuation before seizure | Origin debit equals destination credit plus route deaths, with survivor provenance intact |
| Empty stockpile or partial payment | No full formation or action is produced without its full paid obligation |
| Invalid capital or impassable seed | Preparation fails before irreversible population or force expenditure |
| A-B-C contact chain in different iteration orders | Same component, same frozen recipient and same total assets |
| Equal strength and industry | Lower immutable registration ID wins deterministically |
| Earlier successful merger | Legitimate inherited surviving units count once toward the next merger |
| Research conflict or missing native transfer support | Exact limitation is surfaced before destructive commit, without false conservation claims |
| Two human donor controllers | Both receive verified continuation and no silent AI substitution |
| Save and reload around each publication boundary | No repeated births, charges, deaths, troops, rewards or history |
| Paused GUI refresh and repeated click | No truth reroll and at most one committed action |
| Mother qualifies while another world-end owns the registry | No competing Mother entry |
| Mother enters, then Chaos falls | Ordinary rolls remain suspended and the playable war continues |
| Mother defeated while another suspension reason exists | Only her ownership is released, with no blanket restart |
| No DLC, each relevant DLC, supported combined set | Core invasion, screening and war remain available, with documented enhancements only |

Native annexation, player switching, exact unit-strength inspection, population rounding, country package readiness, research preservation and shared world-end suppression all require installed-engine evidence. Static parsing, a render or a public source example cannot establish those runtime behaviours.

## Sources and evidence boundary

The adapted systems specialist fully read the supplied design contract, source protocol, current AGENTS and scripted-system architect role, event-planning skill and all seven references, events skill and all four references, subagents skill, dynamic effect and trigger references, map-states skill and both references, and debug-playtest and save-inspection main skills. The wider team completed the supplied 151-source reading gate. This specialist does not claim to have personally reread all 151 sources.

The eight targeted repository files were fully read separately. Their paths and SHA-256 receipts are in [repository evidence](../../plans/119_mistresses_plans/imported_review/119_mistresses_repository_evidence.json). No installed HOI4, DLC, save or multiplayer test was available here. The execution map assigns those remaining checks to the implementation stage.

[S1]: ../../plans/119_mistresses_plans/imported_review/119_mistresses_source_evidence.md#provided-project-contracts "Current scripted-system and country integration contract | .claude/skills/chaos-redux-events/references/scripted-systems-and-country-integration.md"
[S2]: ../../plans/119_mistresses_plans/imported_review/119_mistresses_source_evidence.md#provided-project-contracts "Current shared population and cohort ledger contract | .claude/skills/chaos-redux-map-states/references/state-ledgers.md"
[S3]: ../../plans/119_mistresses_plans/imported_review/119_mistresses_source_evidence.md#provided-project-contracts "Shared effects and accounting contracts | chaosx_dynamic_effects.md"
[S4]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/002_zombie_outbreak_effects.txt "Pinned Zombie effects"
[S5]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scorers/country/002_zombie_outbreak_scorers.txt "Pinned Zombie successor scorer"
[S6]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/zombie_special_project_effects.txt "Pinned weaponized Zombie effects"
[S7]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_triggers/002_zombie_outbreak_triggers.txt "Pinned Zombie triggers"
[S8]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/on_actions/002_zombie_outbreak_on_actions.txt "Pinned Zombie lifecycle hooks"
[S9]: 119_mistresses_spec_part_1_core.md "Accepted event identity and related-event design contract"
[S10]: ../../plans/119_mistresses_plans/imported_review/119_mistresses_source_evidence.md#provided-project-contracts "World-end, manual scenario and aftermath contract | .claude/skills/chaos-redux-events/references/world-end-triggerable-scenarios-and-aftermath.md"
[S11]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/script_constants/world_end_scenario_registry_constants.txt "Pinned world-end registry constants"
[S12]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_triggers/chaosx_world_end_scenario_triggers.txt "Pinned world-end enablement triggers"
[S13]: ../../plans/119_mistresses_plans/imported_review/119_mistresses_source_evidence.md#provided-project-contracts "Shared history and evolution contracts | .claude/skills/chaos-redux-events/references/event-log-evolutions-and-clusters.md"
[S14]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/script_constants/chaos_unit_family_registry_constants.txt "Unit family registry constants and future-provider contract"
[S15]: https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/chaos_unit_family_registry_effects.txt "Unit family provider callback defaults"
