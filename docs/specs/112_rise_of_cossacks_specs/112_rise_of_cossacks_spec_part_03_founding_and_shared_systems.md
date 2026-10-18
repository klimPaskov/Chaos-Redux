# Part 03. Founding and shared systems

Event 112 Rise of Cossacks originated from catalog entry 122.
See part 13 for the user-confirmed identity and current workbook migration status.
The imported [final package audit](../../plans/112_rise_of_cossacks_plans/imported_review/review_evidence/curator/final_package_audit.md) records the user-specified design classification as Minor Fire-Once, To Be Reworked, Chaos level 1, and Formables with Medium severity.
The workbook migration remains pending as described in part 13.
This chapter owns the immediate founding, shared resource accounting, two public meters, country and host registries, and common action contracts.
All numeric values are proposed first-pass tuning for implementation and live validation.
Numbered report, action, spirit, and route labels are specification identifiers, not evidence that a native runtime namespace or carrier tag has already been allocated.

The [military and economy chapter](112_rise_of_cossacks_spec_part_06_military_and_economy.md) owns the concrete army, research, service economy, and military program inventory.
The [evolution and lifecycle chapter](112_rise_of_cossacks_spec_part_07_evolution_and_lifecycle.md) owns The Hosts Answer, defeat, exile, restoration, and director cleanup.
The current supplied owner contracts take priority over the older pinned implementation wherever the integration appendix records a difference.

## 1. Core design contract

The event creates one immediately playable country in one valid East Slavic state, with its ataman, an affordable cavalry force, and a limited opening reserve established in the same opening transaction.
There is no preceding national-focus phase or delayed uprising meter.
The first strategic problem is to preserve the host while obtaining recognition, a working arsenal, and a settlement between military autonomy and civilian government.
The campaign then supports negotiated expansion, border warfare, military modernization, admission of other host traditions, and the researched political outcomes in parts 04 and 05.

There are exactly two public event meters.
Host Cohesion measures whether the military communities accept common command and their service obligations.
Settlement Legitimacy measures whether civilian communities accept the host's government and territorial settlement.
Neither meter is a spendable currency.
Political Power, Command Power, Army Experience, manpower, equipment, fuel, native construction, and native supply retain their ordinary roles.
There is no horse stockpile, plunder currency, supply-token currency, or separate military-tradition point system.

Native cavalry, infantry, motorized, and mechanized battalions carry the military design.
Plastun denotes the accepted infantry template and visual treatment, never a new infantry combat archetype.
Distinctive behavior comes from templates, training, bounded doctrine effects, terrain, raids, and charters.
The mounted cavalry and foot plastun visual rows are entities for those native families.
They do not by themselves authorize a new combat archetype or a new counter family.

### Non-negotiable invariants

1. One state changes hands at the opening and one country becomes the principal host.
2. All opening quantities come from one immutable pre-transfer snapshot.
3. The same snapshot produces the same opening for a human or AI recipient.
4. One physical owner handles each population, manpower, equipment, state, unit, and character transfer.
5. A state, carrier, character, military unit, or receipt cannot simultaneously belong to two competing releases.
6. Successful formation, reload, reactivation, annexation, or a tag switch never repeats the opening grant.
7. A failed preflight creates no country, spends no resource, and does not consume the Fire-Once success flag.
8. A partially committed opening freezes for explicit reconciliation and cannot silently reroll another country.
9. Active processing uses explicit host, country, state, and pending-transaction registries.
10. No new global daily hook or recurring all-country scan is introduced.

## 2. Campaign phases

| Phase | Entry | Main decisions | Exit |
|---|---|---|---|
| Rising | Successful immediate opening | Rally the host, choose a temporary military compact, answer the displaced authority | Survive 90 days with a controlled capital and at least one functioning formation |
| Settlement | Rising objective completed | Recognize civilian councils, organize workshops, define service obligations | Cohesion at least 50, Legitimacy at least 45, and an accepted charter |
| Registered Host | Charter accepted | Train regular cadres, secure supply, negotiate recognition, admit a first tradition | A functioning arsenal or reliable delivered arms agreement and an ordinary military reform |
| Regional Power | Three controlled chartered states or an accepted equivalent political compact | Admit hosts, regularize command, integrate territory, choose confederation or central military authority | A route-specific territorial and political outcome |
| Successor State | Route-specific formation gate passed | Use the surviving host institutions under the new identity | Continue normal play with completed one-off rewards and live obligations preserved |
| Displaced | Loss of every controlled home state or capitulation | Negotiate custody, evacuate while possible, organize political exile | Recognized restoration, integration into another host, or permanent closure |

These are state transitions and completed objectives, not six simultaneous player bars.
The military route remains playable before the political route is settled.
A surviving one-state host can become a Registered Host without conquering a required number of states.
Regional Power needs territory or a genuinely implemented confederal compact, not a cosmetic title.

The Hosts Answer is an evolution flag and a bounded opportunity director layered over these phases.
It is not the ordinary progression from Rising to Settlement.
It can be active before the first firing and changes the opening context and later opportunities without creating a second initial grant.
Its shared tier 2, chaos at least 400, setting, once-only, survival, and regional-crisis unlock gates are defined in part 07.

## 3. Identity, state, and carrier selection

### 3.1 Geography is a versioned provider

Part 02 defines the geographic anchors and the provider contract that must supply the authoritative East Slavic collection, including state IDs, names, membership reasons, province geometry, border relationships, and any alternate-state rules.
It does not claim that the exact installed state collection or province geometry is already available.
The runtime collection uses actual installed states and does not infer ethnicity from ownership, a modern map, a state name substring, or a country tag alone.
The repository does not supply the installed state geometry needed to finalize this collection.
The design is complete at the provider boundary, while exact membership and province selection remain a named implementation dependency.

The provider also identifies genuine host homelands and compatible claimant identities when supported by research.
Historical Don and Kuban identities remain distinct from a generic uprising elsewhere in East Slavia.
The primary state can be any state that passes the common geography and physical checks.
It does not need to be a historical Don or Kuban homeland.

### 3.2 Eligible primary state

A primary state must meet every condition below at snapshot and again at commit.

- It belongs to the accepted East Slavic collection and has at least 150,000 residents in the validated population reading.
- It has at least one valid land province for the capital and initial deployment, with an inspected supply and pathing basis.
- It has existing repairable military-factory capacity, a genuinely available factory slot for the one-off workshop bridge, or an explicitly verified native civilian-to-military factory conversion path available in that actual state.
- It is not a current national capital, a one-state country's sole owned state, or an active owner-managed evacuation, population-custody, or release transaction site.
- Every materially affected legal owner or controller must retain at least one other state it both owns and controls with a usable capital and supply basis wherever the transfer could otherwise remove its last viable territory. A surviving tag or an unusable occupied possession does not satisfy that preservation test.
- Its legal owner and current controller are valid countries with explicit identities.
- Its controlling military authority represents an eligible ordinary human society under the shared civilian classifier, including AI-controlled countries.
- Neither the state nor the proposed country carrier is reserved by Event 005, Event 006, Event 112, or another registered release provider.
- No active battle or unresolved state transfer is in progress in the selected deployment province.
- The opening budget computed below is at least 2,500 people and can produce the agreed minimum native formations without overspending manpower or equipment.
- The opening will not destroy an existing country or overwrite an existing character, focus tree, army, or national-history program.
- Every materially affected local country remains below the shared limit of three active local crises before this new crisis is admitted.

An occupied state is allowed only through the explicit occupied-state variant.
For an ordinarily administered state, legal owner and controller are the same displaced authority.
For an occupied state, the controller is the displaced military authority used for military strength and desertion calculations, while the legal owner is retained as a separate claimant.
Both identities are carried in the transaction.
The occupied-state variant is blocked until the war, ownership, control, unit-retreat, and claimant-response behavior has been validated against the installed engine.
It must never manufacture a duplicate war or assume that ownership and control mean the same thing.

An unavailable native resistance value on an ordinary unoccupied core is explicitly not applicable and contributes zero resistance.
A missing value caused by an unverified scope is not silently converted to zero.
The production predicate is checked before any opening mutation.
A possible future arms donor, an unproven conversion operation, a fictional extra slot, or a promised later conquest cannot satisfy it.
The qualifying route records its actual state, building capacity or slot, and native construction or conversion evidence for the later workshop objective.

### 3.3 Shared 005/006/112 arbitration

The current source declarations referenced in part 09 define DHC Don Host Emergency Circle and KHC Kuban Host Provisional Council as Event 005 successor carriers.
Those carriers have meaningful country content and may not be overwritten or replaced with duplicate Don or Kuban tags.
Their current invented leader histories conflict with the newer grounded-source requirement.
They become eligible for Event 112 only after the integration owner completes the shared identity remediation and an explicit admission adapter preserves their Event 005 content.

The proposed common release reservation records the state ID, country carrier, claimant identity, character identity, source event, transaction ID, generation, and short expiry.
It validates every claim before writing any reservation and then claims all required identities within one synchronous operation.
Reservations acquired by another family cause rejection rather than replacement.
Reservations expire only while no physical mutation has occurred.
A committed release keeps durable owner and provenance receipts after the transient lock is removed.

This neutral arbitration is genuinely shared infrastructure because 005, 006, and 112 all need it.
It is a proposed integration contract, not an existing verified public helper.
Event 112 keeps its own selection, strengths, politics, and lifecycle private.

Carrier choice follows this order.

1. A dormant, correctly grounded, geographically appropriate host carrier with an explicit safe admission adapter.
2. A separately reserved generic Cossack rising carrier whose identity works for the selected state and whose tag is proven unused.
3. No valid carrier, producing a clean unavailable result.

The generic carrier's exact tag is left to the country-package namespace audit.
The design does not invent new Don or Kuban tags.
A live DHC or KHC can later negotiate, supply volunteers, or join a compact through its existing owner.
It is never consumed as an empty tag.

### 3.4 Random target weights and player-crisis rule

Selection first chooses a displaced military authority, then a valid state belonging to that authority's candidate set.
This prevents a country from receiving a larger total crisis weight merely because its map is split into more states.
Within that country the state draw remains random and favors documented frontier opportunity.

All normalized variables below are clamped to the interval from zero to one.
For a country, I is instability, W is war pressure, and Rbar is the mean resistance of its eligible states.
Let q be the number of other active local crises, with q equal to 0, 1, or 2.
For a transaction with distinct legal owner and controller, require crisis capacity in both countries.
The occupied-candidate count and human factor vary by legal claimant and are combined explicitly below.

The proposed country weight is:

`country_weight = (1 + 0.8 I + 0.6 W + 0.4 Rbar) × 0.7^q × human_target_factor × near_capitulation_factor`

For an ordinary owner-controller pair, the human target factor is 1.25 when that materially displaced authority is player controlled and 1 otherwise.
An occupied-state adapter must apply the human factor exactly once to each candidate with any materially affected player authority.
The near-capitulation factor is 1.35 when surrender progress is at least 50 percent and 1 otherwise.
Neither factor bypasses eligibility, the crisis cap, existing reservations, or the minimum viable opening.

The proposed state weight is:

`state_weight = 1 + 0.9 R + 0.4 frontier + 0.3 documented_host_connection`

For mixed occupied claimants, let w_i be that base state weight and let human_i be 1.25 when either materially affected authority for candidate i is player controlled, otherwise 1.
Let q_controller and q_legal_i be the affected authorities' other local-crisis counts.
Candidates at the crisis cap are already excluded before these weights are formed.

`a_i = human_i × 0.7^max(q_controller, q_legal_i)`

`country_combined_factor = sum(w_i × a_i) / sum(w_i)`

The occupied country's draw weight is `(1 + 0.8 I + 0.6 W + 0.4 Rbar) × country_combined_factor × near_capitulation_factor`.
The conditional state draw weight is `w_i × a_i`, normalized by `sum(w_i × a_i)` within that country.
That denominator cancels the numerator introduced by the country mean, so the candidate's combined human and crisis factor applies once in its final joint probability.
Do not also multiply this occupied-country weight by a separate human factor or 0.7^q.
When legal owner and controller are the same country, all candidates have the same a_i and this reduces to the ordinary formula above.
The adapter must demonstrate the complete-pool probabilities before the occupied-state variant is enabled.

Frontier is one only for an accepted border or open frontier condition in the geography provider.
Documented host connection is one only when an accepted historical or regional identity mapping supports it.
Every otherwise valid state retains positive weight.
Weights are normalized over the complete surviving candidate pool immediately before the draw.
Revalidation failure removes the failed candidate and permits at most two additional draws in the same request.
After three failed commits the request reports its exact failure without scheduling an unbounded retry loop.

This implements the mechanics source's preference for fewer simultaneous local crises and its mandatory higher player-country crisis likelihood.
It does not change the resources of a host because the player elects to control it.
No difficulty switch disables these supported player-crisis factors.
The exact inclusion of other global scheduler factors still needs the probability auditor's full pool inspection.

## 4. Dynamic opening budget

### 4.1 Immutable measurements

Take one snapshot before any state, stockpile, army, or country mutation.
Store the source country, controller, legal owner, selected state, source date, source generation, country crisis count, and these validated measurements.

| Symbol | Measurement | Proposed anchor |
|---|---|---|
| P | Resident population of the selected state, in people | Minimum candidate size 150,000 |
| F | Displaced military authority's actually fielded land-army manpower | 400,000 gives full size contribution |
| Mfree | Its free recruitable manpower | Compare with 5 percent of F, with a 5,000 denominator floor |
| s | Its national stability fraction | No instability contribution at 65 percent, full at 20 percent |
| r | Native local resistance percentage when applicable | Full local contribution at 60 percent |
| w | Whether it is at war | Peace 0, war 1 |
| u | Its current surrender-progress fraction | Full losing-war contribution at 60 percent |

Use the project's thousand-scaled manpower and population readers where required to avoid overflowing ordinary dynamic manpower values.
The adapter must supply F from a documented fielded-manpower reading.
Division count times an invented average is not an accepted substitute.
An unavailable fielded-manpower contract blocks the chosen formula until a verified alternative is accepted.

The normalized inputs are:

`I = clamp((0.65 - s) / 0.45, 0, 1)`

`R = clamp(r / 60, 0, 1)`

`W = 0.5 w + 0.5 clamp(u / 0.60, 0, 1)`

Set u to zero when w is zero, so a stale postwar surrender value cannot add war pressure.

`Lsize = clamp(F / 400000, 0, 1)`

`M = clamp(Mfree / max(5000, 0.05 F), 0, 1)`

The proposed total opening manpower authorization is:

`raw_muster = (2000 + 0.008 P + 6000 Lsize) × (0.70 + 0.20 I + 0.15 W + 0.15 R + 0.10 M)`

`muster_cap = min(30000, 0.025 P, 2500 + 0.20 F)`

`authorized_muster = floor(min(raw_muster, muster_cap) / 250) × 250`

The population cap prevents a small state from producing a national army.
The relative-army cap prevents a small displaced country from facing a scripted rebel force several times its actual army size.
The absolute cap keeps a major-country rising a limited regional challenge.
Instability, war, local resistance, available manpower, and the displaced country's military strength all matter.
The formula raises the chance of a meaningful rising during a collapse without guaranteeing rescue, victory, or a large force when the source has no resources.

### 4.2 Local mobilization and actual defectors

The authorization is split before mutation.
The local mobilization component is a finite authored founding allowance for an irregular muster, bounded by selected-state population and the complete opening formula.
The receipt discloses that event-created allowance separately from real donor manpower.
It does not claim an installed API can identify the exact residents from whom the old army recruited.
The implementation must observe automatic native accrual where the verified adapter exposes it and count that accrual against any explicit founding military credit.
The same people cannot remain in both an automatically filled unit and the free pool.
A stricter resident-level recruitable-entitlement model is not required and no new demographic model is introduced.
If the accepted native mobilization adapter proves a lower actual permitted capacity, reduce the roster to that capacity or reject it below the 2,500-person minimum.
The defector component is an actual transfer from the displaced authority's free military manpower.
It is never also subtracted from state civilian population or counted as civilian deaths.

`source_manpower_floor = max(1000, 0.03 F)`

`defection_opportunity = min(1, 0.5 I + 0.3 W + 0.2 R)`

`requested_defectors = floor(min(0.02 Mfree, 0.25 authorized_muster, max(0, Mfree - source_manpower_floor)) × defection_opportunity / 100) × 100`

`local_muster = authorized_muster - requested_defectors`

The receiver gets only the actually available local_muster plus the observed actual defector debit.
A failed or short defector debit does not create replacement volunteers from nowhere.
The budget is reduced and the formation recipe is recomputed before creation.
If the minimum opening cannot still be met, the pre-activation transaction is refunded and released.

These are native military-pool transactions and a one-off disclosed local founding allowance.
They do not use the civilian Deaths helper.
Physical civilian relocation, when separately authorized, uses the state-ledger contract in section 8.

### 4.3 Formations and equipment

Reserve at least 20 percent of the final manpower budget as free replacement manpower.
Round the replacement minimum upward to a whole person and the fielded allowance downward.
The remaining 80 percent is the maximum fielded manpower of the opening roster.
Unused formation capacity stays in the same real replacement pool and is not lost or reminted.
Pack native cavalry into one-, two-, or three-battalion formations so small openings do not receive the same division count as major openings.
Use at most eight initial divisions.
At least 70 percent of opening combat manpower is cavalry.
When the budget supports it, one small native infantry formation represents foot plastun scouts and local guard duty.
It replaces part of the cavalry budget and does not add another manpower grant.
Support companies are admitted only when their actual manpower and equipment fit the same authorization.

Read each template's exact current manpower and equipment requirements from the installed native definitions before implementation.
The creation adapter must account for fielded manpower, free manpower, fielded equipment, and stockpile equipment together.
It cannot both create a fully manned unit for free and leave the same manpower in the stockpile.
It cannot grant equipment to a unit and also add the full allowance to the national stockpile.

Let Efield be the equipment needed by the selected opening recipe.
The opening equipment coverage factor is:

`equipment_coverage = min(1, 0.75 + 0.10 I + 0.10 W + 0.05 R)`

Authorize equipment_coverage times Efield for the fielded force and an additional 10 percent of that delivered quantity as a national reserve.
Choose exact compatible infantry-equipment models before quoting any transfer.
At most 35 percent of the equipment allowance can come from seized or defecting source stocks, subject to a 1 percent source-stock cap and an explicit military reserve floor.
The rest is the finite local mobilization cache recorded in the opening receipt.
Short actual transfers reduce delivery and never enlarge the local cache.
There are no future-tech grants, generic advanced-equipment copies, or repeated opening resupplies.

### 4.4 Ordinary state and economic continuity

Existing state buildings transfer with the state under the validated native ownership operation.
No source factories are copied into another state.
The initial government receives a bounded political setup allowance of 40 Political Power and 15 Command Power once, identical for human and AI control.
Initial Army Experience is `min(20, 3 + floor(final_muster / 2000) + floor(4 I))`.
This pays for early organization without making the host immediately doctrinally complete.

A host with zero existing military-factory capacity at founding may undertake Establish Host Workshops once.
An existing damaged military factory is still existing capacity and does not qualify the host for another factory.
The free-slot completion check also requires no newly acquired military-factory capacity.
A host with an existing factory instead completes an organizational or repair objective within the same one-off early bridge, with no additional factory reward.
The proposed ordinary cost is 60 Political Power and 90 days, with continuous ownership and control of the selected state.
The free-slot route requires at least one genuinely available factory slot at completion and adds one ordinary military factory in that state.
If the founding state's sole qualifying route is native civilian-to-military conversion, the bridge instead requires that exact native conversion of one actual civilian factory.
The conversion preserves the native building cost and duration, and completion cannot precede either its actual conversion milestone or the 90-day organization minimum.
Its resulting military factory is the bridge's own paid conversion result, not a newly acquired external factory that invalidates the same receipt.
It never also receives the free-slot factory reward, creates an extra slot, preserves the converted civilian factory, or grants technology to make an unavailable route appear valid.
The more advanced E02 workshop specialization starts only after this basic production or repair capacity exists.
Losing the state aborts the project and does not build the factory elsewhere.
The project is a bounded early economic bridge, not a repeatable conversion of Political Power into industry.
Afterward, normal production, construction, arms deliveries, and captured stocks sustain the army.
A new generic carrier begins with two research slots.
An admitted existing carrier preserves its legitimate initialized slot count, including the three-slot DHC/KHC baseline where its adapter is accepted.
The later third- and fourth-slot institutions belong to the military and economy chapter, and Event 112 grants no fifth slot.

Do not use the unrestricted technology-union helper for a tradition, a captured state, or the opening.
Opening research only admits the actual conventional equipment prerequisites required by its accepted recipe.
Any full sovereign merger that later calls technology union requires its own explicit policy and donor audit.

## 5. Immediate spawn transaction

### 5.1 One committed opening

The intended opening is synchronous and has no player-facing warm-up phase.

1. Revalidate geography, current authorities, crisis capacity, carrier eligibility, grounded ataman identity, exact deployment, native unit recipes, and helper availability.
2. Freeze the opening measurements and derive every authorized quantity.
3. Acquire the shared state, carrier, character, and release reservations.
4. Reserve the logical receipt IDs and prove donor affordability without moving assets.
5. Debit any actual defector manpower and source equipment into a transaction-owned pending transfer with full before and after observations.
6. Transfer the one state to the correct dormant carrier, establish its capital, apply exactly the founding-state core required by part 01 while preserving existing foreign cores and claims, and immediately enter a country-root initialization receiver where required.
7. Install the accepted ataman and government identity without rewriting unrelated carrier history.
8. Deliver observed transferred assets and allocate the disclosed local muster plus the fixed local equipment cache once, then create only the roster that the final budget supports.
9. Register the host, state, military recipe, character ownership, opening receipts, crisis ownership, source claims, and any pre-active evolution.
10. Confirm the country owns and controls the state and the opening inventories reconcile, then record the global successful Fire-Once result and present the report.

Before country activation, a failure refunds only actual debits and releases reservations.
After activation, an unexpected mismatch freezes the partial transaction with a repair disposition.
It does not silently annex the country back, erase characters, try another state, or issue a second local cache.
Source and destination resources remain on explicit receipts until reconciled.

The old authority receives an immediate response event after the country exists.
Its choices are negotiation, recognition with conditions, or a punitive-war path allowed by the validated diplomatic rules.
The event does not force the player to wait for independence to occur.
For an occupied state, the military occupier and legal claimant receive distinct responses and only the intended hostile relationship is created.
Native war merging, faction participation, treaty behavior, and existing-war preservation require installed-engine scenarios before this variant ships.

### 5.2 Survival and a voluntary first assembly

The survival objective requires the host to reach at least 90 elapsed days since founding with a currently controlled viable capital and at least one functioning formation.
Its native mission allows 120 days so success at day 90 does not compete with a same-tick timeout.
Success is checked before timeout on any shared due tick, including day 120.
The founding clock does not reset after capital relocation or temporary loss.
Completing the objective presents the charter opportunity once and does not automatically start the first assembly's deadline.
A surviving one-state host need not launch its assembly before the chosen charter's actual target conditions are reachable.
A failed founding mission does not later rerun its reward on restoration.
The provisional civilian settlement and ordinary first-assembly admission remain available to a surviving host after that mission expires, once their actual conditions are met.
This recovery does not restart the founding clock, award the survival reward again, or renew any opening grant.
An actual restoration follows its separate settlement and lifecycle disposition.
The ordinary settlement period follows around days 90 to 150.
It does not pay a second opening army or restore losses.
A temporary home-defense effect may support that objective only within the original state and only while defending the host's existence.
The proposed ceiling is 10 percent defensive combat benefit for 60 days, with no offensive benefit, no expansion to later conquests, and no refresh on tag changes.
The exact native modifier binding is an engine dependency.

### 5.3 Provisional Civil Settlement

The founding state has a finite civilian settlement before any permanent charter exists.
This is the Provisional Civil Settlement sub-objective of the existing A01 founding mission, not an additional mission slot or the acquired-state integration action A14.
It needs no previous charter, second state, conquest, outside sponsor, meter threshold, or offensive readiness.
Its physical conditions are a currently controlled viable capital, a functioning surviving formation, and the ability to keep the named civilian commitments in that state.
Low equipment coverage or organization does not by itself bar this defensive and civilian recovery program.

The immediate host response offers a free temporary compact as a political commitment.
Accepting it credits +5 Host Cohesion and +2 Settlement Legitimacy once for the campaign generation.
It establishes temporary military, rural, and urban civilian representation and a provisional property and service rule.
It does not choose or ratify one of the five permanent charters.
The first later charter cannot credit the same compact reward again.
The AI accepts this feasible opening commitment promptly, while the player can accept it without first paying for the settlement program.

Funding the settlement costs 35 Political Power before universal modifiers, with no separate stage fee.
The actual shared quote is shown and paid through the ordinary receipt contract.
The opening 40 Political Power covers the unmodified base price, but a higher valid quote can require later native Political Power accrual.
Until the actual quote is affordable and fully paid, the setup remains pending, no Political Power is debited, and no funded-stage clock runs.
An unaffordable setup makes no payment attempt, while an unexpected partial native debit follows the common fault-receipt repair contract and starts no stage clock.
The free compact remains accepted and its reward remains used during that wait.
This founding recovery is a specific exception to the AI's ordinary 20 Political Power reserve, so the AI may pay an affordable settlement quote even when less than 20 remains.
No Command Power, manpower, equipment, population, or newly invented currency pays for these stages.

| Stage | Earliest completion after actual full payment | Required civilian result | Maximum C credit | Maximum J credit |
|---|---|---|---:|---:|
| Founding council | 30 days | The provisional military, rural, and urban civilian delegation accepts the temporary property, safety, and service rule | +5 | +8 |
| Protected livelihoods | 60 days | Keep the named home-protection and civilian-livelihood commitment for 30 continuous days after the first stage | +5 | +8 |
| Kept guarantees | 90 days | Keep the provisional guarantees for 60 continuous days after the first stage, with no unmet protection or evacuation promise | 0 | +7 |

Each stage credits the smaller of its remaining one-time C allocation and the positive gap to C 60, and the smaller of its remaining one-time J allocation and the positive gap to J 50.
A higher existing meter is never reduced.
Any unused allocation expires with that stage's completion and cannot be banked for a later loss.
These values are finite founding recovery allocations, not a repeatable council reward or an exemption for later state councils.
The first stage includes the ordinary founding council's +1 C and +4 J inside its listed maxima.
Any such council credit already received is deducted from that stage's remaining allocation, and the same once-per-state council identity is consumed by completion.
Its ordinary council portion counts toward the normal rolling council allowance, while the additional founding recovery is owned by the campaign-once stage receipt.

Store the host lineage, founding state, free-compact receipt, payer and actual paid quote, funded start date, each stage's due date, applicable compliance interval, actual meter credits, council identity, and terminal status.
The existing bounded host review or a specific due-date event checks these receipts.
No new daily or all-country loop is needed.
Unmet guarantees pause progress, and the required continuous compliance period must be satisfied after compliance is restored.
An actual breach applies its one receipt-owned consequence, never another penalty for each paused review.
Completed stages, actual payment, and the used compact reward survive a delay, reload, capital loss, charter change, and eventual restoration.
They are not paid or credited a second time.

Completing the third stage supplies the accepted founding-state civilian settlement required by a first assembly.
With immediate unmodified funding and uninterrupted commitments, the host can finish that settlement at day 90 and then complete a feasible 30-day charter hold at day 120 inside an assembly window that begins when the assembly is actually chosen.
The founding mission's own timeout does not start, shorten, or restart that later window.
Delayed funding, interrupted guarantees, or a more demanding chosen charter move the actual assembly date later.
The settlement remains available to the surviving host after the founding mission times out, and no timeout or delay renews an army, cache, factory bridge, meter allocation, or political setup grant.

## 6. Two public meters

### 6.1 Meaning and initial values

Host Cohesion, abbreviated C in formulas, describes military agreement across the host's communities.
Settlement Legitimacy, abbreviated J in formulas, describes civilian acceptance and an enforceable territorial settlement.
Both range from zero to 100.
They are ordinary durable country values owned by Event 112 and are clamped whenever an accepted transaction changes them.
They are not spendable balances, substitutes for native stability, or proxies for ethnic population.

The proposed opening values are:

`C = clamp(60 + 10 R - 10 I - 10 W, 35, 70)`

`J = clamp(35 + 10 R - 5 I - 5 occupied_variant, 25, 50)`

A collapsing authority can therefore provide a stronger opening while leaving a less coherent host that must build government.
Resistance creates opportunity and some initial acceptance, but it never proves that every inhabitant supports Cossack rule.

| Meter band | Consequence | Recovery |
|---|---|---|
| C below 25 | Fractured command, no voluntary new host admissions, offensive AI expansion suspended | Assembly and service-settlement actions remain available |
| C from 25 to 44 | Uneven service obligations, no command-integration reform | Settle the actual service dispute and train cadres |
| C from 45 to 64 | Functional common command | Ordinary baseline behavior |
| C from 65 to 79 | Coordinated command | Up to 5 percent planning-speed benefit on the accepted military surface |
| C at least 80 | Strong common institutions | Up to 10 percent planning-speed benefit, replacing the lower band |
| J below 25 | Government contested | No peaceful core admission or political formation, civilian recovery still available |
| J from 25 to 44 | Provisional settlement | Negotiation and local councils are the main route forward |
| J from 45 to 64 | Accepted charter | Ordinary integration and voluntary compact negotiations |
| J from 65 to 79 | Recognized administration | 10 percent reduction in the ordinary administrative component of integration actions |
| J at least 80 | Durable civic settlement | 15 percent reduction in that component, replacing the lower band |

The military modifier targets and planning-speed binding require native documentation before implementation.
The proposal avoids an unbounded combat-stat stack.
J's ordinary administrative adjustment enters the universal quote before temporary sale-source ratios.
Neither meter changes market prices, native manpower, equipment stocks, or every national modifier indiscriminately.

### 6.2 Event-driven changes

| Accepted event | C change | J change | Repetition rule |
|---|---:|---:|---|
| Free temporary host compact accepted in the immediate response | +5 | +2 | Once per campaign generation, no second award at charter ratification |
| Provisional Civil Settlement stages completed | Up to +5, +5, and 0 | Up to +8, +8, and +7 | The three once-only stages in section 5.3 stop their C credits at 60 and J credits at 50, with the first council included |
| A new civilian council receives an accepted charter | +1 | +4 | Once per state, national J gain capped at +8 and C gain at +2 per rolling 120 days |
| An actual unpaid service dispute is settled | Restore at most its actual unrecovered C loss | Restore at most its actual unrecovered J loss | Bound to the same dispute and missed-installment receipts, no excess reward or reset through renegotiation |
| A voluntary new host enters the compact | -4 | +2 | Once per host admission |
| Its service and representation settlement is completed | +5 | +2 | Once for that host admission |
| A charter is unilaterally broken | -10 | -8 | Per distinct broken charter, never duplicated by reload |
| A peacetime stores raid is executed | +2 only for real military capture | -6 | One outcome per raid, no C gain for an empty or failed raid, C gain unavailable above 75 |
| A first successful wartime raid against a valid military target | +2 | 0 | At most once per target country per 120 days |
| A source population or equipment transaction remains unreconciled | 0 | 0 | Block its dependent action rather than disguise an accounting fault as a political penalty |
| The founding state is lost | -10 | -5 | Once per loss episode, no additional hit on each control tick |
| A researched political outcome is formed | Route-defined | Route-defined | One common receipt prevents repeat rewards and modifier stacking |

### 6.3 Bounded maintenance

Each active landed host receives one scheduled review every 30 days.
The review reads only that host's accepted commitments, recent raid receipts, and currently registered chartered states.
It does not scan every country.

Completed service obligations and stable civilian administration can restore at most +2 C and +2 J per review while the relevant value is below 60.
The recovery increment is the smaller of 2 and the gap to 60, so passive recovery never crosses 60.
This recovery requires 60 continuous days of fulfilled commitments, no broken charter, and no peacetime stores raid during that interval.
An actually unpaid committed installment causes -2 C and -1 J once for its missed due date, capped at -4 C and -2 J per review.
Its loss receipt records the actual clamped meter decrease, not a larger nominal penalty that the meter could not lose.
Settling that dispute can restore only its same actual loss still unrecovered, separately for C and J.
Any previous restoration reduces that recoverable balance, and a completed or renegotiated dispute cannot reset it.
Any other actual positive C or J credit after the loss, including passive recovery, consumes the corresponding outstanding loss balance in chronological order before that loss can fund another dispute restoration.
This accounting does not withhold the credited meter increase, it only prevents claiming that same recovery twice.
No settlement reward is created for an installment that caused no actual loss, and unrelated breaches cannot be relabeled as the same installment to enlarge recovery.
Repeated intentional lateness therefore produces no positive net meter gain through the dispute-recovery route.
A state with an unresolved local charter is a pending integration task rather than a mandatory perpetual cash drain.
War by itself does not produce automatic monthly meter loss.
Conquest by itself does not become a repeating legitimacy punishment after the specific occupation and charter state has been registered.

At low values, at least one feasible recovery action remains available.
Neither meter can lock the player out of every recovery path.
The founding settlement in section 5.3 provides a finite pre-charter route even for a surviving one-state host with no acquired council or external partner.
Its payment can wait for native Political Power accrual, and its completed allocations never refresh through a new dispute or charter.
At settled peace with no unresolved commitments, the review becomes a cheap due-date and lifecycle check.
It may stop scheduling once the Event 112 systems have been retired through a final integration disposition.

## 7. Common actions, dynamic prices, and logistics

### 7.1 Size anchors

Define registered_member_count as the number of living host communities admitted to this country's compact.
It is a count derived from accepted registry rows, not a new resource.
Define administered_state_count as the number of controlled chartered states owned by the country.
Define fielded_native_manpower from the same verified military measurement used elsewhere.

The proposed national administrative scale is:

`Sadmin = clamp(1 + 0.08 × max(0, administered_state_count - 1) + 0.05 × max(0, registered_member_count - 1), 1, 3)`

For a state project use:

`Sstate = clamp(state_population / 500000, 0.5, 2)`

For an army-wide training project use:

`Sarmy = clamp(fielded_native_manpower / 20000, 0.5, 3)`

Each existing scripted payment component has exactly one size class under the following table.
Flat is the default.
Never multiply Sadmin, Sstate, and Sarmy together, and never create a new fee merely because an action is assigned a class.
The owning contract identifies the action and component explicitly, rather than guessing a class from its displayed name.

| Existing component or physical obligation | Size class | Deterministic application |
|---|---|---|
| A01 Provisional Civil Settlement funding | Flat | The ordinary base remains 35 PP regardless of country, state, or army size |
| A03 one-off founding workshop or its admitted organizational, repair, or conversion bridge | Flat | The scripted ordinary administrative base remains 60 PP, with native construction or conversion costs owned separately by their actual native route |
| A27 ordinary civil-program extension | Flat | The ordinary base remains 20 PP |
| Negotiated arms-contract consideration | Flat | Use the actual agreed price as its ordinary base, with delivery-owned escrow and no country-size surcharge |
| A14 acquired-state integration administrative PP | Sstate | Multiply only its existing administrative PP base by the target state's Sstate |
| E04 reconstruction explicitly contracted to one named state | Sstate | Multiply only its existing administrative PP component by that same state's Sstate |
| Charter ratification and constitutional reform, national or federal congress, constitutional or consolidation acts, and default national first-peace administrative reviews | Sadmin | Multiply only the existing PP fee for that accepted administrative act by the current country's Sadmin |
| M01 service register and M04 common standards | Sarmy for Army XP only | Multiply only the existing Army XP component of these two army-wide programs by Sarmy, their PP component stays Flat unless another explicit accepted row applies |
| M02, M03, M05, M06, and other per-formation Army XP fees | Flat | Keep the stated ordinary XP base, with no implicit army-wide multiplier |
| Every scripted Command Power component | Flat | No size multiplier, and the action's final actual CP requirement must still pass the 60 CP ceiling below |
| Stated equipment, manpower, fuel, or other material delivery quantities | Flat physical quantity | No size multiplier changes the stated obligation or its observed source debit, custody, and delivery accounting |
| Native-owned raid allocations and other native-owned construction, training, conversion, or equipment costs | Native pipeline | No Event 112 size multiplier or second scripted quote, debit, or refund is applied to the native-owned cost |
| Every other existing scripted component without a specifically accepted row | Flat | Keep its stated ordinary base until a later explicit design disposition assigns a different class |

The specific named rows take precedence over the broader administrative row.
A14 and a single-state E04 therefore use Sstate rather than also receiving Sadmin.
An A20 or A21 review following a more specific original P, GP, or E04 promise uses that original component owner and classification, not a second default review fee.
Record the chosen class, actual target and count inputs, and ordinary base in the action's implementation map and payment receipt context.
Recompute an unpaid quote at confirmation from the same currently valid target, while a successfully paid receipt keeps its actual paid amount.

For a true scripted price component, apply its one selected size factor, then actual eligible consumer modifiers and any J adjustment already authorized specifically for that administrative integration component.
The universal quote composes active eligible sources afterward and rounds once at the appropriate quantum.
Flat removes size scaling only and does not silently exempt a true scripted price from the shared modifier contract.
A fixed physical delivery objective remains the stated physical quantity and cannot be enlarged, reduced, or considered fulfilled merely because a separate monetary consideration or scripted expense was modified.
Any material expense and actual physical delivery must have their correct distinct roles recorded, with no delivered quantity greater than its actual measured source movement.
Mission deadlines, compliance intervals, physical objectives, native manpower requirements, and the native training or construction pipeline are not multiplied by these three size factors.

The sum of the final actual Command Power requirements needed to commit one action must not exceed 60.
A scripted shared quote of 61 CP makes the action unavailable before any component is paid.
Do not silently clamp that quote to 60, charge 61, or invent a successful helper receipt for another amount.
For native-owned CP, inspect and respect the actual native requirement through its native pipeline and reject an unsupported above-ceiling action without a second scripted quote.
Positive prices never become free through rounding.
Displayed amount, confirmation affordability, paid amount, receipt, AI budget, and actual-paid refund must agree.
The pinned implementation and current documented contract require reconciliation before this is claimed complete.

### 7.2 Native supply remains authoritative

The system uses native supply, infrastructure, rail, ports, hubs, fuel, equipment fulfillment, training, and organization.
It does not maintain a competing supply stockpile.
A raid or volunteer deployment requires an actual valid route and a physically available formation or transferred resource.
An icon marked prepared is not route proof.

The opening army must pass a local supply review for the selected capital and force recipe.
Larger future armies need ordinary production and supply investment.
Patrols and the temporary home-defense effect do not cancel native attrition or generate fuel.
Mounted forces remain useful in a poor industrial setting but still consume their actual native equipment and supply.
Motorized and mechanized modernization adds normal truck, fuel, and maintenance demands.

### 7.3 Payment transaction

At confirmation the owner acquires an action lock and repeats the entire non-cost preflight.
It computes all ordinary component prices, obtains fresh quotes, checks every resource and reserve floor, and verifies that each receipt ID is unused before the first debit.
Only then does it pay components in one synchronous chain.
Every component records its actual debit and the same quoted amount.
A partial debit or receipt rejection blocks the gameplay result and enters explicit refund or reconciliation.
The universal recorder rejects actual-paid amounts that differ from the quote, so an owner fault record must preserve an unexpected partial native debit rather than pretending it was successfully recorded.
No delayed phase rereads an old sale price as if it were a locked quote.
Delayed installments quote again when due and can fail cleanly without silently overdrawing the country.

Successful completion settles the transaction after the cancellation window closes.
Cancellation refunds stored actual-paid amounts only.
Refunding a discounted purchase never credits the undiscounted ordinary price.
Payer identity and original resource/model identity remain fixed through a tag change or country integration.
Native resource-cap behavior during refunds must be tested, and an uncredited remainder cannot be marked refunded merely because a credit helper returned success.

### 7.4 Arms deliveries

Arms delivery is a real exchange with an existing willing country.
The donor selects an exact compatible model and cannot sell below its own reserve floor.
The buyer's observed actual PP debit remains in a transaction-owned escrow receipt until matching equipment is actually delivered.
Escrow is the record of already paid native PP awaiting its contractual recipient, not a new spendable resource.
The supplier receives political compensation only from that escrow and only for observed delivery, so a sale discount cannot create an undiscounted difference as free PP.
For a partially delivered contract, cumulative supplier compensation is `floor(actual_paid_PP × cumulative_delivered_equipment / contracted_equipment_quantity / PP_quantum) × PP_quantum`.
Each new delivery pays only the difference between that cumulative amount and supplier PP already actually credited.
The final full delivery pays the exact remaining paid-price balance, so rounding never creates or loses the agreed total.
Native credit-cap truncation leaves the already-earned but uncredited amount payable on the same escrow receipt and cannot make it buyer-refundable.
Cancellation of undelivered equipment refunds only the corresponding unearned escrow balance.
It never refunds PP already credited to the supplier or PP earned by equipment that the buyer actually received.
The default accepted contract makes the supplier bear nondelivery risk.
Broader insurance and compensation products are outside this system.
Any separate administrative charge is explicitly displayed and never silently added.
The transfer has one buyer, one donor, one direction, one model, one quantity, one route, and one transaction ID.
The pair cannot reverse the same delivery immediately to farm discounts or task rewards.
Use a 180-day pair cooldown for compensated deliveries and exclude already pending quantities from availability.

Until a route is accepted, no equipment moves and no payment is settled.
On dispatch the actual donor debit becomes a transfer-in-progress receipt.
On delivery the recipient receives only the amount proven in that receipt.
Interception, changed diplomacy, unavailable route, target loss, or annexation has an explicit return, redirect-with-consent, loss, or unresolved-custody outcome.
The same shipment cannot be delivered both to the host and to its new owner after annexation.
After a completed trade, a return or reversal is a new explicit transaction that proves both the actual equipment return and the supplier's actual PP debit before the buyer receives returned PP.
An old purchase refund cannot silently reverse a settled delivery.

For example, a contract actually paid 37 PP for 300 rifles.
After 100 rifles are observed at the buyer, cumulative supplier compensation is `floor(37 × 100 / 300) = 12 PP` at a one-PP quantum.
The supplier receives 12 and 25 remains in escrow.
If the remaining 200 rifles are validly canceled, only that 25 is refunded.
If another 100 arrives, cumulative compensation becomes 24 and the supplier receives another 12.
The last 100 completes delivery and pays the exact remaining 13, for total supplier compensation of 37 and zero remaining escrow.

### 7.5 Readiness and the three national spirit slots

Voluntary territorial expansion, a paid expedition, or a new political commitment that explicitly requires military readiness uses one shared baseline.
The host needs a controlled capital with a validated native supply route, at least one functioning field formation, at least 75 percent equipment fulfillment, at least 50 percent organization, and adequate actual current free manpower.
The replacement check is `current host free manpower / (current host fielded land-army manpower + current host free manpower) >= 0.20`.
Count every person once and include all later native-trained units in the actual fielded measurement.
The system does not attribute a mixed national manpower pool to an Event 112 cohort or maintain a separate demographic balance.
Keep the proportion after any quoted outgoing transfer.
The equipment and organization readings refer to the formations actually committed to the proposed action, with no empty dummy division counted as proof.
The capital defender must remain viable after that commitment.
Exact native weighted-formation readings remain an adapter dependency.

Defence, ordinary reinforcement, withdrawal, evacuation, reconciliation, and feasible meter recovery remain available below this offensive-readiness baseline.
A political route can require a stronger army for its own finite declaration gate, but cannot silently redefine the common low-meter recovery rules.
Native units trained later count in the country's actual military assessment and do not receive a scripted replacement entitlement.

There are at most three focus-created national spirit slots, aligned with part 06 as S01 Institutions and service settlement, S02 Army organization, and S03 Civil economy and reconstruction.
Institutional, Military, and Economic are short working labels for those same slots.
Political projects and reforms replace the accepted variant in their slot.
Traditions contribute through those existing slots or another explicitly bounded verified modifier surface, without creating a fourth permanent focus-created spirit.
The temporary home-defence effect is a timed founding emergency effect and is not a fourth permanent focus reward.
No renamed project stacks its predecessor and successor versions.

Concrete action names, military programs, and economic projects use the inventory in part 06 and their political route chapters.
No action exposes more than four spendable resource types or charges more than 60 Command Power.
The main view exposes at most five primary actions at one time.

### 7.6 Bounded frontier raids

#### 7.6.1 Two mission types

The baseline uses two native land-raid families after the host has survived 45 days, has C at least 40, and has a physically ready native cavalry or infantry formation.
The committed formation meets the shared readiness conditions and leaves a viable supplied defender at home.
Preparing or resolving a raid counts as one of the host's six active time-sensitive commitments.
Both need an adjacent accepted frontier target, an actual starting point, and a valid land route.
Neither can target an ally, subject under the actor's own control, a protected treaty partner, a current truce partner, or an already reserved target state.
Wartime military targets are normal candidates.
R01 requires an actual war with the target authority.
A peacetime stores raid additionally requires a recorded unresolved border dispute, explicit advance warning, and the adverse diplomatic consequences below.
That bounded peacetime exception belongs to R02 only.

| Mission | Target | Successful result | Resource limit |
|---|---|---|---|
| R01 Supply-route disruption | A frontier state with targetable ordinary infrastructure | Bounded damage to that actual state's infrastructure | At most 0.5 level for success and 1 level for critical success |
| R02 Military-store recovery | A frontier military-depot context with actual eligible victim stock | Exact model-specific military equipment debit and transfer | At most 400 rifles or 30 support equipment, never both in one raid |

A coastal or river extraction program is an optional R02 route adapter only after its exact native path, craft, eligible unit, target, and equipment behavior are verified.
It never creates an unverified third raid system or a separate craft currency.

The depot context is a gameplay abstraction for military stocks serving the targeted frontier.
It does not claim the engine physically stores the national stockpile in that state.
The target's available military stock and the per-state extraction ceiling both constrain the result.
An empty stockpile does not produce loot.
There is no civilian population debit, slavery, civilian-casualty reward, or free conversion of state population into raiders.

Use native infrastructure damage only where the state-scoped building contract is unambiguous.
Railway, supply-hub, port, or special-facility sabotage requires an exact inspected province consumer and a separately accepted mission variant.
The generic random-state damage helper is unsuitable because the mission already owns an exact target and physical outcome.

#### 7.6.2 Preparation and native allocation

The proposed native preparation is 14 days with a 90-day target-state cooldown and a 45-day actor raid cooldown.
At most one raid may be preparing or resolving for one host country at a time.
The same target country's stores can yield a material transfer to the same host at most once per 180 days.
These gates apply across both mission IDs, cosmetic changes, and successor tags through the durable host lineage.

The native raid allocates 10 Command Power and owns any essential equipment reservation shown by the final inspected definition.
Those engine-owned allocations are not debited again by an Event 112 effect.
No scripted universal-cost receipt pretends to own native reservation, preparation cancellation, or automatic equipment collection.
Any flat native allocation that cannot consume the universal cost contract receives an explicit cost-surface disposition and remains a compatibility gate.
The implementation cannot silently exclude an otherwise mandatory discount or invent a refund for a native payment it did not own.

Native raids can use their actual land-unit strength, organization, experience, preparation, recon, and resistance factors.
The current copied raid documentation and portal definitions establish those source surfaces, but installed DLC, current schema, starting-point behavior, and cancellation still need verification.

#### 7.6.3 Proposed probability model

Normalize preparation, experience, organization, strength, recon, and resistance to zero through one using their documented native reference ranges.
The intended caps are expressed here as design requirements.
The probability auditor must verify the actual native interpolation, clamping, risk-taking effects, and external factors before exact displayed percentages are claimed.

`S = 0.25 + 0.15 preparation + 0.12 experience + 0.10 organization + 0.10 strength + 0.05 recon + 0.05 resistance`

`K = 0.08 + 0.08 experience + 0.04 recon`

`D = clamp(0.12 - 0.04 preparation - 0.04 experience - 0.02 organization - 0.02 strength, 0.02, 0.12)`

S is ordinary-or-critical success probability, K is critical success conditional on success, and D is unconditional disaster probability.
The proposed outcome distribution is critical S times K, success S times one minus K, disaster D, and limited success one minus S minus D.
The chosen anchors keep S at most 0.82, K at most 0.20, and D at least 0.02 under the design inputs.
They are not four independent weights.
Native behavior that differs from this probability interpretation requires adjustment rather than relabeling a score as a probability.

#### 7.6.4 Outcome and anti-farm contract

| Outcome | Actor's native formation | Supply-road mission | Military-stores mission |
|---|---|---|---|
| Disaster | Proposed 10 percent strength and 40 percent organization loss | No target damage | No captured stocks |
| Limited success | Proposed 4 percent strength and 20 percent organization loss | At most 0.25 infrastructure damage | At most one quarter of the currently available capture ceiling |
| Success | Proposed 1.5 percent strength and 10 percent organization loss | At most 0.5 infrastructure damage | Up to the current capture ceiling |
| Critical success | Proposed 5 percent organization loss | At most 1 infrastructure damage | Same material ceiling, with a better military report or one extra bounded Army XP instead of doubled loot |

The victim retains a protected equipment floor based on its actual military demand.
The exact model transfer is the minimum of the outcome amount, the current available stock above that floor, the pending-transfer-free quantity, and the state extraction limit.
It is measured at resolution rather than assumed from preparation.
Source model and actual debit determine the delivered model and amount.
An unavailable or unproven archetype-to-model debit blocks the material reward.

Army XP gain is at most 1 for limited success, 2 for success, and 3 for critical success.
National XP is awarded only once per target country per 120 days and only for a real hostile mission with a committed physical outcome.
A repeated empty or invalid target grants no national XP, no Cohesion, and no material.
Native unit-experience behavior remains separate and must be included in the probability and farm audit.
State repair does not reset extraction history.
Neither defeat nor formation into a new country name resets actor or target cooldowns.

Peacetime stores raids reduce J by 6 on execution even if their attempted capture fails, worsen the victim's attitude, and create a punitive-response opportunity for that victim.
The possible C gain requires a real accepted military capture and respects its cap, so an empty raid cannot create military prestige.
The victim receives a real response and can offer settlement, reinforce its frontier, or pursue the validated punitive-war path.
Ordinary wartime logistics raids do not automatically receive that civilian-government penalty.
The design does not allow the actor to raid its own subjects, transfer the same stock back, and collect repeated rewards.

#### 7.6.5 Exact scope and concurrency boundary

Preflight, AI intent, and launch checks run in the actor-country context, with the victim and selected target carried explicitly.
Physical state/province candidate filters remain actor-neutral unless the exact current engine binding has been established.
Both actor_effects and victim_effects at success-level resolution begin in RAID_INSTANCE scope according to the documented native contract.
Enter the actor, victim, or state deliberately.
Nesting into a country does not turn ROOT into that country.

A helper requiring country ROOT uses an immediate hidden actor-country receiver and explicitly saved regular actor, victim, state, province, and raid-identity references.
Temporary values do not cross the event boundary.
Use disjoint exact-one receiver markers or fixed event identities for the bounded pending raid slots.
One global pending raid scalar is prohibited.

Immediately before the physical result, revalidate actor existence, host lineage, victim identity, state owner/controller, exact province, current war or dispute authority, cooldown identity, and receipt state.
If any identity changed, the raid records an invalidated-resolution outcome and applies only the native already-owned costs or losses that the engine contract actually requires.
It does not redirect the target, invent loot, refund native preparation from a guessed amount, or damage a newly friendly state.
Prepared-instance visibility after the type becomes unavailable remains a specific native test requirement.

#### 7.6.6 Worked raid probabilities

With preparation 1, experience 0.25, organization 0.70, strength 0.85, recon 0.20, and resistance 0, the model gives S equal to 0.595, K equal to 0.108, and D equal to 0.039.
The outcome probabilities are 6.426 percent critical success, 53.074 percent ordinary success, 3.9 percent disaster, and 36.6 percent limited success.
They sum to 100 percent.
With all six inputs at 1, the model gives S equal to 0.82, K equal to 0.20, and D equal to 0.02.
The resulting outcomes are 16.4 percent critical success, 65.6 percent ordinary success, 2 percent disaster, and 16 percent limited success.
The critical outcome improves the result within the same extraction ceiling and never doubles captured equipment.
These arithmetic results validate the proposed distribution only.
The native game's factor evaluation and external risk modifiers still require the probability audit.


## 8. Host registry and transfer receipts

### 8.1 Durable host identity

A host_id identifies a political and military community independently of its current country tag, cosmetic name, array position, or ataman.
A campaign_id identifies the one Event 112 campaign.
A generation identifies a specific validated country activation or restoration without resetting earlier rewards.
IDs are monotonic within their declared safe numeric range and are never reused after deletion.
Exhaustion fails closed rather than wrapping into an old receipt.

The country carrier, origin state, founder identity, source event, current ataman, political route, and current status remain distinct fields.
Host status is one of reserved, landed, integrated, displaced, political_exile, restored, or closed.
The registry separately records whether the country has an active local-crisis slot, an opening receipt, a pending raid, a pending transfer, and an accepted representation charter.

At most four simultaneously independent landed hosts can have been created by Event 112, including the principal.
The separate active participant registry contains at most twelve country actors across created hosts, admitted existing partners, and exile or custody actors.
Up to four active exile or custody actors may occupy that same twelve-country registry rather than an extra list outside its cap.
Historical identity rows and completed receipts are preserved outside the active processing list.
Existing living DHC/KHC partners count toward the twelve-country participant cap and do not consume an Event 112-created carrier slot merely by joining.
If Event 112 activates an admitted dormant carrier as its own rising, that activation does consume one of the four created-host slots.
A displaced carrier cannot be recycled while its political identity, exile claim, person ownership, or pending receipts remain live.
Reaching the cap changes a possible new rising into another independently valid opportunity or a no-op.
It never deletes, merges, or transfers a living country without the appropriate political transaction.

Every aligned registry operation appends, updates, or removes all columns together.
Lookups require exactly one match.
Zero matches are unavailable and multiple matches are a data-integrity blocker.
An array index is never treated as a durable host ID.
Country-target validation uses actual country existence and ownership checks rather than scope_exists on a variable scope.

### 8.2 Transaction classes

| Receipt | Required identities | Physical proof | Terminal dispositions |
|---|---|---|---|
| Opening | Campaign, host, generation, state, carrier, ataman, displaced authority | State ownership/control and combined fielded/free manpower and equipment totals | Committed, refunded before activation, partial activation requiring reconciliation |
| Volunteer manpower | Donor, receiver, host, source pool, quantity, route | Observed military-pool debit and equal delivered or explicitly held amount | Delivered, returned, held in accepted custody, documented loss |
| Equipment transfer | Donor, receiver, exact model, quantity, route, payer transaction | Observed model-specific stock debit and receipt-bound delivery | Delivered, returned, redirected with consent, documented loss |
| State defection | Origin owner/controller, receiver, state, crisis episode, local authority | Exactly one ownership/control result with intact population and preserved claims | Committed, rejected, frozen partial transfer |
| Character transfer | Unique person identity, current owner, destination role | Original ownership invalidated before exclusive destination ownership | Transferred, rejected, captured, dead, retired |
| Formation defection | Exact source unit identity, composition, manpower, equipment, experience, commander | One source removal and one faithful destination transfer or reconstruction | Transferred, rejected, held pending an exact native route |
| Civilian relocation | Origin and destination state, authority, people, floor, route, capacity | Measured origin debit minus route deaths equals measured destination credit | Delivered, returned where physically valid, accepted custody, reconciled death record |
| Charter or formation | Host identities, political route, territory proof, source receipts | Correct route and ownership at confirmation | Accepted once, rejected, superseded by named lawful transition |

Military volunteers are actual transfers from a consenting donor or a validated defection source.
They are not a population-growth effect.
The ordinary volunteer batch is the minimum of 2,000 people, 2 percent of donor free manpower, 10 percent of the receiver's current military manpower, and the donor's available amount above its reserve floor.
Use at least one verified source and route.
One donor-receiver pair can dispatch at most one volunteer batch per 120 days.
An evolution's call for volunteers does not authorize a free batch when nobody can supply it.

Formation defection is required selected content, with activation blocked until the exact native transfer route is verified.
It must preserve strength, missing equipment, experience, composition, and unique commander ownership.
Destroying an understrength unit and recreating a fully equipped veteran is forbidden.
If only manpower and equipment transfers are verified, the public opportunity is honestly a volunteer or deserter contingent, not a claimed transfer of that exact division.
That separate contingent can operate independently, but it does not complete or replace the required formation-defection implementation.
The Hosts Answer has a distinct exact-formation outcome in its five-way pool in part 07.
It selects at most one actual formation per answer and validates that formation independently of the source country's free manpower balance.
The unit must have a unique preserved identity, a viable physical transfer route, and no incompatible training, home-garrison, evacuation, transfer, or other current commitment.
The recipient must have a viable supplied capital, an available accepted place for the real formation, and the home-defense conditions required for that actual transaction.
The receipt carries the observed source unit, actual strength, every equipment model and quantity, experience, composition, commander ownership, current location, receiving country, and terminal transfer result.
Rename, reconstruction through an approved adapter, charter change, and reload retain the same unit-lineage receipt and cannot present the unit as a new unclaimed formation.
Only the actual source removal and corresponding faithful destination result complete the transfer, with no additional local muster, free replacement pool, or restored missing equipment.

### 8.3 Civilian movement is a separate contract

Chartering a state, admitting a host, gaining a core, or changing a flag does not move population.
An ordinary military muster does not call the civilian Deaths helper.
Only a separately authorized actual relocation uses the state-ledger system.

For such a relocation, one owner validates the origin floor, route, state authorities, recipient capacity, and custody obligations before mutation.
It measures the origin population debit, measures any route-death slice once, and measures destination credit.
The conservation condition is `origin_debit - route_deaths - destination_credit = 0`.
The receiving state's load and receiving country's load update together by the same accepted quantity.
Integration or resettlement outcomes do not create additional people.
Existing custody at either site requires its owning closure or release receipt even when the Event 112 marker did not create that custody.

The newer supplied exact-population contract requires observed loss, an upward-protected floor, and a Deaths entry that does not apply a second population debit.
The pinned older implementation does not implement that full contract.
Civilian relocation remains blocked until the correct current helper and source/destination credit route are available and validated.
Choosing relocation is optional for the player, while the selected P04, P11, P12, P14, and GP08 content makes its implementation a required part of the complete package.
The baseline military muster and nonmoving charter actions can be developed independently, but their completion cannot be reported as completion of the whole package while those selected civilian routes remain blocked.

### 8.4 State defection

A state can defect into an existing host only if it is contiguous with that host, belongs to the accepted geography, has an active eligible source crisis, and has a documented local council or host authority prepared to accept the receiver.
The receiver needs C at least 45 and J at least 50.
The state cannot be a capital, sole remaining state, active custody-transfer site, or another release's reservation.
The action reuses the shared state reservation and commits one state only.
It does not copy factories, add population, issue another opening cache, or automatically transfer all native divisions present.
Former legal claims remain represented unless a separate settlement removes them.
Any native unit, war, or occupation behavior not yet verified blocks this variant rather than authorizing a guessed reconstruction.

## 9. Common autonomous behavior

### 9.1 AI uses the same system

AI hosts use the same candidate rules, opening formulas, native recipes, prices, transfer sources, cooldowns, reservations, and receipts as player hosts.
They receive no invisible replacement armies, stockpile top-ups, bonus manpower, or special debt cancellation.
Their ordinary production and deployment behavior is carried by native AI plans and the accepted templates.

At most six active time-sensitive commitments may belong to one host at once, including no more than three Event 112 missions.
A pending paid project, shipment, raid, or other timed promise counts toward the six even when it uses a different native presentation.
Long-term charters remain registered obligations in the bounded twelve-country system rather than permanent mission timers.
Preflight checks available commitment capacity before payment and never cancels an existing paid commitment merely to expose another action.

At each existing host review or newly available decision opportunity, evaluate actions in this order.

1. Complete mandatory cleanup, reconciliation, and already paid deliveries.
2. Preserve the capital, real supply, a replacement reserve, and at least one viable formation.
3. Recover C below 40 or J below 35 through a feasible actual dispute or council action.
4. Establish the first working arsenal or a real delivered arms agreement.
5. Finish service rolls and training already supported by native resources.
6. Consider a raid with positive expected military benefit and adequate post-action reserves.
7. Negotiate a host compact or an accepted political route.
8. Expand only when the native military and supply situation supports it.

Ordinary AI purchases retain at least 20 PP and 10 CP after payment unless the action directly prevents immediate collapse.
They also retain the defined manpower and equipment replacement floors.
One raid or paid project cannot reserve resources already committed to another pending delivery.
AI cannot treat a discounted displayed price as permission to skip a non-cost condition.

AI raiding requires a predicted S of at least 0.55 from the actual available native inputs, no critical home defense emergency, and a target with real value.
AI pauses offensive expansion when C is below 40, J below 35, or its army lacks the accepted native supply and equipment readiness.
Pausing aggression does not turn off ordinary defense or recovery.

## 10. Worked opening budgets

These examples calculate the proposed design with exact rational arithmetic.
They are not engine observations.
All viable examples assume that state geography, the accepted local mobilization adapter, compatible equipment, and the exact native formation recipe pass preflight.
If one of those independent requirements fails, a mathematically valid authorization is reduced or rejected under the ordinary transaction rules.
Population and military quantities are people.

| Case | P | F | Source free manpower | Stability | Resistance | War | Surrender |
|---|---:|---:|---:|---:|---:|---|---:|
| A Stable small authority | 300,000 | 30,000 | 20,000 | 70% | 0% | No | 0% |
| B Stressed regional authority | 800,000 | 200,000 | 15,000 | 35% | 20% | Yes | 20% |
| C Major authority near collapse | 1,600,000 | 900,000 | 250,000 | 20% | 45% | Yes | 55% |
| D Large-state hard cap | 3,000,000 | 1,200,000 | 300,000 | 15% | 60% | Yes | 60% |
| E Below viable minimum | 150,000 | 5,000 | 0 | 70% | 0% | No | 0% |
| F War crisis with no free source manpower | 600,000 | 150,000 | 0 | 25% | 30% | Yes | 40% |
| G No source field army | 800,000 | 0 | 0 | 20% | 30% | Yes | 50% |

| Case | Raw muster | Lowest cap | Authorized after 250-person rounding | Requested actual defectors | Local allocation | Maximum fielded | Minimum replacements |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 3,880 | 7,500 | 3,750 | 0 | 3,750 | 3,000 | 750 |
| B | 12,350 | 20,000 | 12,250 | 100 | 12,150 | 9,800 | 2,450 |
| C | 26,130 | 30,000 | 26,000 | 4,600 | 21,400 | 20,800 | 5,200 |
| D | 41,600 | 30,000 | 30,000 | 6,000 | 24,000 | 24,000 | 6,000 |
| E rejected | 2,292.5 | 3,500 | 2,250 | 0 | 2,250 | 1,800 | 450 |
| F | 9,753.888889 | 15,000 | 9,750 | 0 | 9,750 | 7,800 | 1,950 |
| G | 9,345 | 2,500 | 2,500 | 0 | 2,500 | 2,000 | 500 |

Case E is rejected before any country, soldier, equipment, or political allowance exists.
Its displayed subminimum amounts show the failed arithmetic only.

### 10.1 Regional crisis calculation

Case B has I equal to 2/3, R equal to 1/3, W equal to 2/3, Lsize equal to 1/2, and M equal to 1.
Its base is `2000 + 0.008 × 800000 + 6000 × 1/2 = 11400`.
Its pressure factor is `0.70 + 0.20 × 2/3 + 0.15 × 2/3 + 0.15 × 1/3 + 0.10 = 13/12`.
Raw muster is exactly `11400 × 13/12 = 12350`.
The three caps are 30000, 20000, and 42500, so rounding 12350 down to a 250-person block authorizes 12250.

The donor floor is `max(1000, 0.03 × 200000) = 6000`.
The pre-opportunity defector ceiling is `min(300, 3062.5, 9000) = 300`.
The opportunity factor is `0.5 × 2/3 + 0.3 × 2/3 + 0.2 × 1/3 = 0.6`.
Thus `floor(300 × 0.6 / 100) × 100 = 100` actual donor personnel are requested.
The local allocation is 12150, with at most 9800 fielded personnel and at least 2450 replacements if the donor debit succeeds.
If the measured debit is only 60, the final budget is 12210, the fielded ceiling is 9768, and the replacement minimum is 2442.
The absent 40 people are never supplied by an extra local grant.

### 10.2 Major-country collapse calculation

Case C has I equal to 1, R equal to 3/4, W equal to 23/24, Lsize equal to 1, and M equal to 1.
The base is `2000 + 12800 + 6000 = 20800`.
The factor is `0.70 + 0.20 + 0.15 × 23/24 + 0.15 × 3/4 + 0.10 = 1.25625`.
Raw muster is `20800 × 1.25625 = 26130`, below the 30000 absolute cap and 40000 population cap.
The 250-person rounding authorizes 26000.
The source floor is 27000.
The defector ceiling is `min(5000, 6500, 223000) = 5000` and the opportunity factor is `0.5 + 0.3 × 23/24 + 0.2 × 3/4 = 0.9375`.
The requested donor debit is `floor(4687.5 / 100) × 100 = 4600`.
The remaining 21400 is the explicitly disclosed local founding allowance, with observed automatic accrual accounted against explicit credit under the accepted adapter.
Maximum fielded manpower is 20800 and minimum free replacements are 5200.
This remains a regional army despite the source fielding 900000 people.

### 10.3 Equipment and native-creation reconciliation

For a verified recipe needing 1200 compatible rifles, use Case B's coverage factor of `0.75 + 0.10 × 2/3 + 0.10 × 2/3 + 0.05 × 1/3 = 0.90`.
The fielded allowance is 1080 rifles and its nominal 10 percent reserve is 108, giving an allowance of 1188 rifles.
Whole-model quantities round downward, so the receipt never exceeds that allowance.
If the donor owns 20000 available compatible rifles and its protected military floor is not binding, the donor ceiling is `min(0.35 × 1188, 0.01 × 20000) = 200` rifles.
The local cache authorized before mutation is 988 rifles.
If the actual donor debit is only 170, total delivery is 1158 and the local cache remains 988.
Preserving at least a 10 percent replacement reserve relative to fielded delivery allows at most 1052 rifles in units and leaves 106 in the stockpile.
The adapter records 1052 plus 106 equals 1158 and recomputes the affected formation readiness.

Those 1200 rifles are an illustrative accepted recipe input, not a claim about a particular vanilla cavalry template.
If the native creation operation takes equipment or manpower automatically, the adapter subtracts those measured automatic amounts from any explicit credits.
A unit created already manned and equipped plus a second full stockpile grant fails reconciliation.

### 10.4 Quantized prices and refunds

For a 35 PP administrative component, a specific Legitimacy adjustment of 10 percent produces ordinary cost 31.5 PP.
An eligible shared source ratio of 0.80 produces 25.2 PP, and one final upward quantum of 1 PP produces a displayed and paid quote of 26 PP.
With no source discount, the owner still supplies an ordinary payable cost quantized consistently to 32 PP.
The exact implementation must preserve this one-price contract without applying two successive ceilings to a discounted component.
Two eligible ratios of 0.80 and 0.75 compose to 0.60.
A 37 PP ordinary component therefore quotes `ceil(37 × 0.60) = 23 PP`.
An exact balance of 23 is affordable before any explicitly displayed reserve prerequisite.

If a cancellable contract actually paid 23, cancellation credits at most that same 23 once.
A change in source discounts between payment and cancellation never changes the refund to 37.
If the native resource cap permits only 18 of that 23 to be credited, the remaining 5 stays on an unresolved refund receipt.
If an unexpected payment physically debits 21 against a 23 quote, no gameplay reward commits and the actual 21 remains on an owner fault receipt for refund or reconciliation.
The generic recorder cannot be called as if actual payment equaled 23.

### 10.5 Two-meter opening examples

| Case | Host Cohesion | Settlement Legitimacy | Design consequence |
|---|---:|---:|---|
| A | 60 | 35 | A modest force begins with more coherent command |
| B | 50 | 35 | Stronger military opportunity still needs a civil settlement |
| C | 47.916667 | 37.5 | Stronger military opportunity still needs a civil settlement |
| D | 50 | 40 | Stronger military opportunity still needs a civil settlement |
| F | 47.777778 | 35.555556 | Stronger military opportunity still needs a civil settlement |
| G | 45.833333 | 35 | Stronger military opportunity still needs a civil settlement |

For Case C, adopting the temporary compact changes C from 47.916667 to 52.916667 and J from 37.5 to 39.5.
Ignoring other earned changes, the first funded settlement stage changes them to 57.916667 and 47.5.
The second stage stops at C 60 and J 50.
The final kept-guarantees stage completes the actual civilian settlement with no further meter credit because both founding recovery ceilings are already reached.
A later distinct acquired-state council follows the ordinary council reward and rolling cap, while a duplicate founding-state receipt adds nothing.
Meter presentation may use sensible rounded display precision, but all gate comparisons use the same stored value and declared comparison rule.

### 10.6 Conservative one-state settlement example

The following uses the lower clamps C 35 and J 25 as a conservative boundary, even though the current opening formula's actual minimum C is 40.
It assumes the free compact is accepted, the settlement is funded immediately at its unmodified 35 Political Power price, all commitments are kept, and no passive recovery, raid, conquest, outside sponsor, extra council, or unpaid-service dispute contributes anything.

| Point | C arithmetic | Resulting C | J arithmetic | Resulting J |
|---|---|---:|---|---:|
| Free temporary compact | 35 + 5 | 40 | 25 + 2 | 27 |
| Day 30 first stage | 40 + 5 | 45 | 27 + 8 | 35 |
| Day 60 second stage | 45 + 5 | 50 | 35 + 8 | 43 |
| Day 90 final stage | 50 + 0 | 50 | 43 + 7 | 50 |

The actual lowest coupled opening C 40 and J 25 follows the same J path and finishes at C 55 and J 50.
Both can begin a charter whose actual gates are C 50 and J 50 after the day-90 civilian settlement, then satisfy its 30-day hold at day 120.
A charter requiring higher values is a voluntary later target, with its own substantive progression and no forced premature assembly timer.
If the universal quote is 53 Political Power while the host still has only the opening 40, the free compact remains valid but funded day zero waits until the actual balance reaches at least 53.
The three stage minima then run 30, 60, and 90 days from that actual payment, without changing the original survival clock.

## 11. Founding and shared-system acceptance scenarios

These are concrete future acceptance cases.
Only the pure design arithmetic in section 10 was evaluated during planning.
Game scenarios, source-helper repairs, probability baselines, CXT fixtures, screenshots, and live logs remain future evidence.

| ID | Scenario | Required result |
|---|---|---|
| F01 | All eligible states are capitals, sole states, or physically unavailable | Clean unavailable result, no resources, no country, no consumed success flag |
| F02 | Population is just below 150000 | Candidate rejected even if other pressure inputs are high |
| F03 | Case E gives 2250 people | Reject before mutation, no artificial minimum grant |
| F04 | Case F has no source free manpower | Zero donor debit, finite disclosed local allowance only |
| F05 | Case G has no source field army | Relative cap remains 2500, no divide by zero |
| F06 | Case D exceeds the national and local anchors | Authorized amount is 30000, never raw 41600 |
| F07 | Human and AI receive the identical immutable snapshot | Same muster, stock allowance, PP, CP, experience, slots, and equipment coverage |
| F08 | Country has two other local crises | Lower weight and admission of one further local crisis only |
| F09 | One affected authority already has three local crises | Territorial variant unavailable even when another authority has capacity |
| F10 | Source ends its war before the snapshot | Surrender contribution is zero in the peace snapshot |
| F11 | Ordinary unoccupied core has no applicable resistance | R is explicitly zero, while a missing scope binding blocks the calculation |
| F12 | Event 005, 006, and 112 request the same state or carrier | One reservation winner, no overwrite or duplicate troops |
| F13 | DHC or KHC is live or lacks grounded identity remediation | No empty-carrier admission, preserve existing content and army |
| F14 | A candidate ataman already exists elsewhere | Transfer only through exclusive verified person ownership or reject that carrier |
| F15 | Occupied state has distinct owner, controller, and faction wars | Block until the exact diplomatic and unit behavior is verified, no guessed duplicate war |
| F16 | State becomes a battle site after selection | Revalidate, reject, and try at most the two remaining bounded draws |
| F17 | Donor payment is short before activation | Reduce to actual delivery, recompute roster, refund and release if no longer viable |
| F18 | Native units are automatically manned or equipped | Combined unit plus free-pool inventories match the one authorization |
| F19 | Native automatic local accrual is exposed by the adapter | Count it once against explicit founding credit, with no resident-origin claim |
| F20 | Transfer activates country but receipt reconciliation fails | Freeze a partial activation for repair, no automatic annexation, reroll, or second cache |
| F21 | Save and reload immediately after opening | Same host, person, opening receipt, army, cooldowns, and success flag |
| F22 | Founding state changes control twice in one combat episode | One C/J loss receipt, no repeated control-tick penalty |
| F23 | Capital moves to another valid surviving state during the 90-day mission | Preserve elapsed objective time, no renewed home-defence or opening grant |
| F24 | All states are lost before the survival objective ends | Enter the lifecycle disposition in part 07, no reset that generates another rising |
| F25 | A damaged factory is the host's only military capacity | Repair route only, no second factory from the early workshop bridge |
| F26 | The host gains a military factory before workshop completion | Revalidate and resolve the paid objective without adding duplicate capacity |
| F27 | Fresh generic carrier versus admitted existing DHC/KHC | Two research slots for generic, legitimate existing count preserved by admission adapter |
| F28 | First and second council charters complete inside 120 days | Combined national J gain at most 8, duplicate state receipt grants nothing |
| F29 | Two unpaid installments and several duplicate overdue checks | At most -4 C and -2 J that review, once per real missed installment |
| F30 | A peace has no unpaid commitments or new disputes | No unbounded passive meter drain, bounded recovery only below 60 |
| F31 | C or J is zero and military readiness is low | At least one feasible recovery route, defence, reinforcement, and evacuation remain available |
| F32 | A fourth focus reward would add another permanent event spirit | Replace its S01, S02, or S03 variant or reject the reward definition |
| F33 | Quote 23 and native balance exactly 23 | Inclusive affordability passes unless an independently displayed reserve condition applies |
| F34 | Source ratio expires between preview and confirmation | Fresh quote at confirmation, same new price in display and actual debit |
| F35 | Two discounts, fractional component, high family masks | One documented composition and quantum, no family leakage or price mismatch |
| F36 | Partial native debit is 21 against quote 23 | No gameplay reward, owner fault receipt preserves actual 21 for reconciliation |
| F37 | Refund 23 reaches a cap after 18 | Five remains unresolved, no repeated credit of the original 23 |
| F38 | Exact old-model truck stock exists but current model does not | A generic newer-model debit cannot consume or fabricate old-model equipment |
| F39 | Payer has 1000 and then 1001 retained components | Correct unique lookup and refund or an explicit bounded archive disposition before capacity is exceeded |
| F40 | Volunteer donor has 10000 free people and receiver military pool 5000 | At most min(2000,200,500,above-floor amount), with observed debit only |
| F41 | Receiver or donor is annexed during a shipment | One consent, return, custody, or loss disposition, no dual delivery |
| F42 | A division defects while understrength and short of equipment | Preserve its real composition and losses through a verified binding or block that required feature's activation, a separate honest personnel transfer is not proof that division defection is complete |
| F43 | Civilian council accepted without physical migration | No population mutation and no Deaths record |
| F44 | Authorized civilian movement has a partial physical debit | Actual debit equals actual credit plus measured deaths, both reception ledgers match |
| F45 | Array IDs are duplicated or near safe-range exhaustion | Fail closed, keep durable identity, no array index reused as a host ID |
| F46 | CXT registration runs again | Readiness registration remains inert, no event, army, resource, or state grant |
| F47 | AI sees an appealing expansion with only 40 percent organization | It preserves its position and pursues defence or recovery rather than paying for an unready offensive |
| F48 | Country name, charter, or great project changes repeatedly | Used founding, workshops, council, formation, and transaction receipts remain used |
| F49 | A 37 PP contract for 300 rifles delivers 100 and validly cancels the rest | Supplier receives 12 PP, only the remaining 25 escrow is refundable, and the 100 delivered rifles remain accounted |
| F50 | Supplier compensation is clipped by a native PP cap | Already-earned uncredited PP stays payable, cancellation can refund only the unearned undelivered share |
| F51 | Buyer seeks a refund after completed delivery | Require a separate reversal proving actual equipment return and actual supplier PP debit, no purchase-receipt refund |
| F52 | Conservative C 35 and J 25 one-state opening has no second council or external partner | The free compact and three funded stages reach C 50 and J 50 by funded day 90 without conquest, passive credit, raids, or unpaid-service recovery |
| F53 | A funded stage starts with a meter already above its founding recovery ceiling | Never lower the meter or bank unused credit, consume only that stage's one-time completion receipt |
| F54 | Initial 40 PP faces an actual settlement quote of 53 PP | Accept the free compact once, keep paid setup pending until the full 53 is affordable, and start no funded-stage clock or partial debit |
| F55 | The founding mission expires before the surviving host finishes its civilian settlement | Keep the unpaid or incomplete settlement and ordinary first-assembly admission available, with no renewed opening grant or survival reward |
| F56 | Charter ratification, reload, and restoration revisit completed founding stages | Preserve actual paid and credited receipts, no second compact, council, or stage award |
| F57 | A protection commitment is broken between stages | Pause dependent progress until the required continuous compliance is restored, apply one real breach consequence, and preserve completed stages |
| F58 | A player prefers a charter whose meter gate is above the day-90 recovery result | Do not launch its assembly deadline automatically, allow later honest progress toward that target |
| F59 | The founding state's first council already credited +1 C and +4 J | Deduct those actual credits from the first stage's remaining maxima and consume the same council identity, no duplicated council reward |
| F60 | Repeated real installments are deliberately paid late | Each -2 C and -1 J actual loss can restore at most that same loss once, so no cycle creates a net gain and renegotiation resets nothing |
| F61 | A nominal installment penalty meets C 1 and J 0 | Record actual losses of 1 C and 0 J, permit at most those same restoration quantities, and never grant the nominal 2 C or 1 J |
| F62 | A proposed one-state host has no military factory, no available slot, and no verified native conversion path | Reject the candidate before mutation even if a future supplier might appear, without adding a fictional slot or technology |
| F63 | Native conversion is the founding state's only valid production route | Consume or convert the actual civilian factory through the verified native operation, preserve its real cost and duration, and grant no second workshop factory |
| F64 | A source owns two states but only the proposed transferred state is controlled and usable | Reject the candidate because another owned, controlled, usable state will not remain, even though its tag and another nominal possession would survive |
| F65 | A crisis source has zero free manpower but one independently eligible actual formation | The exact-formation candidate can remain valid through its own verified transfer route, while an unsupported free-manpower volunteer candidate is removed |
| F66 | The founding-state core makes native local accrual available | Add only that one core, preserve foreign cores and claims, and account any observable automatic accrual once against the disclosed opening military budget |
| F67 | A peaceful neighbor has infrastructure and an unresolved border dispute | R01 remains unavailable without actual war, while R02 still needs every separate warning, relationship, stock, route, and consequence condition |
| F68 | Sadmin is 3, Sstate is 2, and Sarmy is 3 with no other modifiers | A01 remains 35 PP, the workshop remains 60 PP, and A27 remains 20 PP, with no multiplication of the three scales |
| F69 | A14 targets a one-million-resident state with no other modifiers | Its 60 PP base becomes 120 PP through Sstate alone, while its stated 100 support-equipment obligation remains 100 and its 180-day duration is unchanged |
| F70 | M01 runs with Sarmy 3 and no other modifiers | Its 20 Army XP component becomes 60 Army XP while its 40 PP component remains 40, and the real training objective creates no additional troops |
| F71 | A valid shared final CP quote is 61 or combined required CP exceeds 60 | Reject the whole action before paying any component, without a hidden clamp, partial payment, or fabricated quote |
| F72 | R01's native preparation allocates its actual 10 CP while country scales are high | Follow the native allocation once, with no Event 112 size multiplier, second quote, scripted debit, or guessed native refund |

## Appendix A. Implementation dependencies

The map provider must validate every accepted state ID, capital province, deployment point, border connection, and native supply route against the installed state geometry.
The repository evidence does not contain those installed state files.
Fielded manpower, free manpower, resistance applicability, weighted formation readiness, unit creation, local automatic accrual, and equipment model selection each need an explicit installed binding.
The design does not replace an unavailable fielded-manpower reading with division count multiplied by a guessed average.

The default ordinary owner-controller opening is distinct from the optional occupied-state opening.
Ownership, control, retreat, country activation, war merging, factions, existing claims, and meaningful carrier content need their own native scenarios.
Shared 005/006/112 state, carrier, and person arbitration is proposed neutral infrastructure, not an already verified helper.
Its integration and the DHC/KHC grounded identity remediation are prerequisites for those specific carriers.

Civilian relocation is an optional player path with required implementation for the selected P04, P11, P12, P14, and GP08 programs.
Its newer exact-population contract dependency therefore blocks complete-package implementation until resolved.
Native military-pool movement and the disclosed one-off founding allowance do not invoke that route.
No civilian population or Deaths debit is inferred from mobilization.

The future integration gate includes the required original probability baseline, accepted candidate-pool and player-crisis comparisons, static source checks, user-directed CXT fixtures, and user live-game validation.
No unrun MCP or live test is claimed by this document.

## Appendix B. Checked shared helper contracts and older implementation mismatches

The following appendix is an integration handoff.
Its findings do not alter player-visible resources or claim that the older implementation has already been repaired.


### Evidence boundary

All nine files in repository_evidence.json were fully semantically read at commit `a3ef485c5da7e2337122eca04ac65c175050f251`.
The checked line ranges below identify the particular bodies used for each conclusion.
They are line numbers in the normalized local reference copies, with original Git blob identities preserved in the ledger.
The October 10 supplied owner contracts remain the newer authority.
No installed-game scenario, log inspection, MCP validation suite, or live trace was run.
These are source and contract findings, with arithmetic implications identified as inferences where engine semantics remain unverified.

### Exact shared contracts that the design needs

| Owner interface | Contract used by Event 112 | Evidence and disposition |
|---|---|---|
| `damage_state_building_dynamic` | Damage one deliberately selected native building in the explicit state scope | Present at lines 49 to 60 of the pinned dynamic effects file, while exact fractional damage and selected-state behavior still require an installed scenario |
| `apply_state_population_loss_without_recruitable_manpower_gain` | A physical state population debit must not create recruitable manpower as a side effect | Present at lines 539 to 626, optional civilian relocation requires the newer complete transaction contract |
| `apply_exact_state_civilian_population_loss` | Validate floor, perform one physical loss, observe actual loss, then register exactly that loss without a second debit | Pinned lines 628 to 716 differ from the newer owner contract |
| `union_compatible_researched_technologies_from_donor` | Full admitted sovereign continuity only, never a generic reward for one tradition or state | Present at lines 482 to 528 and deliberately excluded from ordinary Event 112 actions |
| `universal_cost_quote_integer` | Owner computes ordinary current price, helper composes eligible sources, one quantized final quote drives display and payment | Present at lines 420 to 598, composition and quantization must be reconciled with the newer documented algorithm |
| `universal_cost_check_quote_affordable` | Native resource availability is checked against the exact final quote | Lines 675 to 687 call the shared trigger, inclusive boundary required |
| `universal_cost_pay_component` | Pay one supported resource kind after the complete action preflight | Lines 698 to 997 issue native effects, owner must still prove actual debit |
| `universal_cost_record_transaction` | Unique positive transaction and component IDs, ordinary and quoted amounts, actual amount equal to quote, payer-owned ledger | Lines 1222 to 1456 reject a quote versus actual mismatch and duplicate components |
| `universal_cost_refund_transaction` | Refund stored actual paid amounts once while the transaction remains refundable | Lines 1543 to the file end, owner must verify any native capped credit before acknowledging completion |
| `universal_cost_mark_component_refunded` | An unsupported owner adapter acknowledges only a component it already credited exactly | Lines 1488 to 1536, never a substitute for the physical credit |
| `universal_cost_settle_transaction` | Mark the accepted completed transaction nonrefundable and preserve its proof | Lines 1460 to 1482 |

Dynamic effects are inspected in the [pinned shared file](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_dynamic_effects.txt).
Universal interfaces are inspected in the [pinned implementation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_universal_cost_effects.txt), its [API documentation](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_effects/chaosx_universal_cost_effects.md), the [system contract](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/systems/universal_cost_modifier.md), the [constant definitions](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/script_constants/chaosx_universal_cost_constants.txt), and the [affordability triggers](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/scripted_triggers/chaosx_universal_cost_triggers.txt).

#### Universal quote input and output names

The quotation inputs are `universal_cost_quote_ordinary_cost`, `universal_cost_quote_family_mask`, and `universal_cost_quote_rounding_quantum`.
The outputs are `universal_cost_quote_final_cost`, `universal_cost_quote_displayed_cost`, `universal_cost_quote_saved_cost`, `universal_cost_quote_composed_ratio`, `universal_cost_quote_source_count`, `universal_cost_quote_primary_source_id`, and `universal_cost_quote_valid`.
The ratio basis is 10000.
For a positive ordinary price and eligible sources, the desired mathematical result is `ceil(ordinary × composed_ratio / 10000 / quantum) × quantum`.
A zero cost stays zero and a reward is not discounted as if it were a spend.
An owner supplies coherent quantization when no eligible source exists, without rounding a discounted component twice.

Affordability adds `universal_cost_quote_resource_kind` and returns `universal_cost_quote_affordable`.
Payment uses `universal_cost_payment_resource_kind` and `universal_cost_payment_amount`, with `universal_cost_payment_result` as its reported result.
That result is not a substitute for measured before and after inventory values where native effects can clamp or select different models.

The receipt fields are `universal_cost_transaction_id`, `universal_cost_transaction_component_id`, `universal_cost_transaction_resource_kind`, optional `universal_cost_transaction_resource_id`, `universal_cost_transaction_ordinary_cost`, `universal_cost_transaction_quoted_cost`, `universal_cost_transaction_actual_paid_cost`, optional `universal_cost_transaction_source_id`, and `universal_cost_transaction_primary_component`.
The API returns `universal_cost_record_transaction_result` and `universal_cost_recorded_component_index`.
Refund and settlement use the original transaction ID.
All temporary inputs and outputs are initialized explicitly at the correct scope because a similarly named temporary in another nested scope is not an isolated variable.

#### Relevant price families and native resource kinds

| Resource | Family mask | Native kind | Event 112 handling |
|---|---:|---:|---|
| Political Power | 1 | 1 | Quote the actual ordinary political cost |
| Command Power | 2 | 2 | At most 60 CP per authored action, engine-owned raid allocation is separately classified |
| Manpower | 4 | 3 | Real pool payment and observed debit |
| Fuel | 8 | 4 | Native capacity, route, and measured amount |
| Infantry equipment | 16 | 5 | Exact compatible model required for a physical transfer |
| Support equipment | 32 | 6 or exact-model kind 11 | Do not claim an archetype query proves a model-specific debit |
| Motorized equipment | 64 | 7 | Pinned kind 7 names `motorized_equipment_1`, so old-model handling needs a different verified adapter |
| Train equipment | 128 | 8 or exact-model kind 12 | Exact donor and receiver model continuity |
| Convoys | 256 | 9 | Actual route capacity and exact native model |
| Army Experience | 32768 | 10 | Ordinary spend, not a new tradition currency |
| Stability | 67108864 | 15 | Native fraction and 0.01 quantum if a route explicitly spends it |
| War support | 134217728 | 16 | Native fraction and 0.01 quantum if a route explicitly spends it |
| Unsupported owner adapter | Declared matching family | 199 | Owner pays and refunds actual values, generic framework records proof |

The common equipment family mask is 112 for infantry, support, and motorized families together.
Navy Experience has family 16777216 and kind 13, and Air Experience has family 33554432 and kind 14.
These are inspected definitions, not a request to use every possible resource in this event.

### Source and contract mismatches requiring an integration disposition

| Checked body | Expected contract | Observed pinned algorithm | Disposition and required boundary scenarios |
|---|---|---|---|
| `universal_cost_source_matches_quote_family`, lines 287 to 358 | Membership by `mask mod (2 × bit) >= bit`, tested on both masks | Divides by each bit, applies modulo 2, then accepts any positive remainder | Algorithm differs from the documented modulo-span route. If fractional division survives, disjoint masks such as 1 and 2 can both appear positive at bit 2. This is a conditional arithmetic inference, not proven live behavior. Check disjoint, overlapping, zero, all, and high-bit masks |
| `universal_cost_round_up_to_quantum`, lines 364 to 414 | Exact upward quantum with current Euclidean-remainder rule and positive minimum | Rounds raw units, compares with the unrounded value, and adds one when below | Might agree under some native rounding semantics. Verify exact quantum, just below and above a quantum, tiny positive prices, negative rewards, and 0.01 fraction costs |
| `universal_cost_quote_integer`, lines 420 to 598 | One final price for display, availability, payment, AI, and refunds | Starts from ordinary cost and quantizes in the active-source path | Define the ordinary no-source quantum before integration without introducing a second ceiling when sources apply |
| `universal_cost_pay_component`, lines 698 to 997 | Actual debit equals quoted component and exact equipment model | Checks affordability, invokes a native effect, then reports success without a complete observed-debit receipt | Require owner measurement and fault receipt on partial payment, stock-model selection mismatch, or native clamp |
| `universal_cost_credit_component`, lines 1001 to 1127, and refund from 1543 | Only actual credited value becomes refunded | Reports successful native credit after the native effect without measuring resource-cap truncation | Test CP and XP near cap, changed caps, partial native credit, and a second refund call. Preserve uncredited remainder |
| Receipt lookup, lines 1135 to 1210, and refund iteration from 1543 | Correct lookup and settlement for all retained records | Payer arrays grow and while loops traverse records | Current owner notes a 1000-iteration engine guard. Check record 1000 and 1001 and define archive or bounded index strategy before exceeding it |
| `apply_exact_state_civilian_population_loss`, lines 628 to 716 | Upward floor, one physical debit, measured actual loss, Deaths does not debit population a second time, state ledger recorded | Rounds the floor, computes requested clamped loss before mutation, reports success, and uses `chaos_deaths_apply_state_pop = 1` in the logged route | This differs from the newer supplied owner contract. Do not install Event 112 civilian relocation against this older route. Check fractional floor, actual short debit, Deaths disabled, state and country reception symmetry, and no recruitable windfall |

No entry above establishes a live-game bug by source reading alone.
Do not silently edit the shared files as an Event 112 private implementation.
The integration owner must assign accepted neutral fixes or adapters to their owners, with before and after evidence.

The two current-owner referenced paths `common/scripted_triggers/chaosx_universal_cost_exact_triggers.md` and `common/scripted_triggers/chaosx_universal_cost_exact_triggers.txt` returned 404 at the pinned commit.
The fully read pinned dynamic effects file does not define `cbrn_debit_motorized_stockpile_oldest_first`, `chaosx_convert_days_to_date_offset`, or `chaosx_convert_date_offset_to_days`.
This establishes absence from that declared shared file, not an exhaustive claim about every unexamined repository or installed file.
Retrieve the accepted newer implementation or assign the dependency before an action relies on it.

### Native raid boundary

The repository's [native raid documentation copy](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/raids/_documentation.md) and [Event 016 precedent](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/common/raids/016_brilliant_scientist_portal_raids.txt) were both read in full.
The former documents both actor and victim outcome effects in RAID_INSTANCE scope, with explicit actor_country, victim_country, target_state, and target_province references.
Entering a country does not change ROOT into that country.
The newer owner requires an immediate hidden country receiver for a country-ROOT-only helper, regular saved references across that boundary, and disjoint exact-one pending slots.
No temporary value is assumed to survive an event boundary.

Native Command Power allocation and essential-equipment collection are engine-owned parts of raid preparation.
Do not pay an extra scripted copy of those same costs, claim universal discounts affect an unverified native field, or invent a cancellation refund.
The Event 016 precedent demonstrates bounded types, preparation, mission costs, target-specific effects, and both state and special-facility targets.
It does not prove that a cavalry Event 112 raid, arbitrary frontier origin, current DLC combination, or the proposed land route works in the installed game.
The exact success, critical-success, limited-success, and disaster interpretation also needs the current native scenario.

### CXT integration

The [CXT testing document](https://github.com/klimPaskov/Chaos-Redux/blob/a3ef485c5da7e2337122eca04ac65c175050f251/docs/testing/chaosx_test_country.md) was read in full.
Daily registration is inert and bounded to the relevant tag or pending registration scope.
Initial application and manual player debug invocation are distinct from registration.
Event 112's package fixture records schema and component readiness only unless a user explicitly invokes a concrete test fixture.
It never fires the actual rise, transfers a live state, creates a host army, grants models, or reruns the founding every day.
Native combat-family templates do not become new Event 19 archetype registrations merely because their visuals differ.
Actual new entity, template fixture, or shared content owners require explicit disposition under the current integration contracts.

The destructive CXT console command was not invoked.
No registered-system application or debug-country mutation occurred during this planning task.
