# Rise of Cossacks: the first host

A frontier rising seizes one eligible East Slavic state and becomes a playable country immediately.
Its first problem is keeping an army in the field while persuading the people behind that army to accept the new government.
Its eventual political identity grows from the settlements it makes with villages, towns, other hosts, neighboring peoples, and foreign powers.
An independent regional host is a complete campaign outcome.
A confederation, a Cossack Russia, a Ukrainian state, or a restored Golden Horde requires further political and military work.

All labels introduced in this package are working design labels.
They identify content for implementation and do not supply final player-facing localisation.
The user supplied the event name Rise of Cossacks and the evolution name The Hosts Answer.
The package preserves those names.

## The experience

The opening is a sudden military and political fact.
The new host has a controlled capital, an ataman's command, a small army, an emergency administration, usable equipment, and a clear route to feeding and reinforcing its troops.
It does not begin as a decision that might eventually release a country after several focuses.
The original owner receives its own response choices as soon as the territorial change occurs.
Neighbors can understand the host's immediate demands before deciding whether to recognize it, support it, contain it, or wait.

The opening army is largely mounted, but the campaign does not assume that a cavalry army can ignore tanks, aircraft, cities, winter, or a broken railway.
The player chooses which military traditions remain valuable and which institutions must change.
Kuban plastun infantry, Don command traditions, Ural communal resources, Terek local agreements, and Dnipro military councils offer different answers to those problems.

The central recurring choice concerns service and political obligation.
An ataman can obtain a rapid levy by preserving the privileges of established host households.
That can leave tenants, townspeople, returning refugees, and neighboring communities outside the settlement.
Opening service citizenship more broadly can create a larger durable state, but it also requires land arbitration, training, civilian representation, and acceptance by the original host.
Neither choice is represented by a free population conversion.

## Event identity

| Field | Required design value |
| --- | --- |
| Event ID | 112 |
| Original catalog ID | 122 |
| Type | Minor Fire-Once |
| Status | To Be Reworked |
| Required Chaos level | 1 |
| Cluster | Formables |
| Cluster role | Medium member |
| Initial manifestation | One new playable host in one valid East Slavic state |
| Evolution | The Hosts Answer |

The user-confirmed event identity is 112, while 122 is the package's original catalog entry. The historical user classification is recorded in the imported [final package audit](../../plans/112_rise_of_cossacks_plans/imported_review/review_evidence/curator/final_package_audit.md); the current workbook migration remains queued and is described in part 13.

Chaos level 1 and Formables with Medium severity are the historical user-specified design classification recorded by the imported final package audit.
Current tier constants set tier 1 at Chaos 200, tier 2 at 400, and tier 3 at 600.
The Event 112 design requires an explicit tier 1 event-eligibility binding at Chaos 200, because the current registry initializer defaults unlisted events to tier 0 and Event 112 is not source-registered.
The existing Formables cluster is cluster ID 6 with its own tier 3 invocation gate at Chaos 600, so cluster invocation and the event's direct eligibility remain distinct.
Medium is the member's severity classification and must not be confused with the separate required, optional, or randomized row-role enum.
The intended cluster member is optional and participates under the shared rules.
No new cluster identifier or numeric member-row identifier is allocated in this planning package.

The root can commit once in a campaign.
Every later host, defection, restoration attempt, and political transformation belongs to that original episode.
No later action resets the fire-once receipt.
If an opening becomes impossible before the territory transaction, the root has not fired.
It returns a genuine unavailable result and can be considered by a later ordinary selection.
After a successful territory transaction, losing the host does not make the root eligible again.

## Three playable viewpoints

| Viewpoint | Immediate question | Early tools | A successful first year |
| --- | --- | --- | --- |
| The host | Can the new army defend its capital and support the settlements that sustain it? | Emergency muster, depot recovery, a land settlement, a diplomatic offer, defensive objectives | A defensible state, an affordable force, a chosen constitution, and one credible external relationship |
| The dispossessed country | Can the secession be contained at acceptable cost? | Negotiation, lawful service concessions, border containment, a limited recovery campaign, counteroffers to individual hosts | A negotiated relationship or a sustained restoration of administration that does not leave an endless repeatable crisis |
| A neighbor or patron | Does the host improve regional security or create another armed dependency? | Recognition, guarded aid, transit terms, volunteer permission, a defensive compact, containment | An agreement whose military burden and political obligations can actually be met |

The event supports a voluntary human switch into the newly created host after its immediate setup succeeds.
The consequence-free choice to retain the current country is first in the native confirmation interface.
The switch affects the requesting human only and is offered once for the founding host.
Other human players keep control of their countries.
An AI never needs this interface to operate the host.
The opening's territorial and resource effects do not depend on whether a human accepts the switch.

## The opening transaction

The selector first determines a valid state, its legal owner, its current controller, and a ready country carrier.
Those identities are frozen in the pending opening record.
The state and carrier are reserved together before any country setup, equipment grant, leader transfer, or army creation occurs.
The reservation is shared with other systems that can create countries in the same territory.

The transaction must preserve a viable country for the dispossessed actor.
It cannot take that actor's last usable state or its only functioning capital location.
A state in a protected terminal condition, an unresolved transfer transaction, an incompatible country-creation reservation, or an unplayable supply position is excluded.
The selector must find a different candidate instead of weakening those checks.

The host acquires exactly one state's ownership and control at founding.
It receives only its initial settlement core, with later core additions governed by integration.
Existing foreign cores and historical claims are retained.
The founding state represents the new administration's actual foothold, rather than a judgment that every resident belongs to a single community.

The current occupier is the immediate military counterpart when ownership and control differ.
The legal owner retains its separate claim and response.
The host cannot automatically inherit a whole existing faction war through an unexamined faction or puppet relationship.
The opening relationship is resolved through a bounded rebellion war or an explicitly accepted autonomy settlement, using the same actor identities in all reports and tooltips.
The implementation must prove the exact engine war-participation behavior before enabling occupied-state openings.

Country activation, capital assignment, politics, technologies, laws, opening ideas, production, force assembly, and AI initialization occur in recipient country context.
The original owner remains available for measured deductions and diplomacy.
The final commit receipt records the state, carrier, old owner, old controller, actual resource settlement, initial force, and episode identity.
Public reports describe only facts that have committed.

## Selection is random within a credible geography

The initial candidate space is an explicit East Slavic geographic registry with a broad frontier-host fallback.
Historic host regions receive a higher contextual weight, while a valid Belarusian, northern Russian, or other East Slavic state can still produce a newly organized frontier host.
The latter does not acquire a fabricated centuries-old pedigree.
Its local service charter provides the starting identity, and historic traditions can be adopted later through contact and training.

The selector samples countries and then states within the selected country, so a large country does not gain an accidental advantage solely by containing many states.
Country weight considers instability, war pressure, recent losses, the shared local-crisis limit, and mandatory supported player-crisis weighting.
State weight considers an eligible host tradition, resistance where resistance exists, supply and population viability, recent fighting, and military resources that can plausibly reach the rising.
The same candidate validity is used for natural firing, cluster firing, manual previews, and final revalidation.
Manual launch can bypass ordinary date, Chaos, and prior-event gates according to the shared scenario contract, but it cannot create an impossible country.

The effect of resistance is zero when the engine has no applicable resistance value.
The selector must not interpret a missing value as either maximum rebellion or perfect calm.
The supply and terrain checks operate on the active map, rather than assuming that a modern administrative region is one game state.
Opening viability also requires a repairable existing military factory, an actually available factory slot for the bounded workshop bridge, or a verified native civilian-to-military conversion path in the selected state.
An unaccepted future donor promise is not proof of a sustainable opening.
The check does not grant an extra building slot or invent a conversion capability.

## Dynamic strength with material limits

The rising's initial military opportunity increases with local disorder, relevant war pressure, resistance, available recruits, and the military scale of the country losing the state.
That opportunity is then limited by actual manpower, equipment, recruitment capacity, and the founding state's ability to support units.
The larger state can produce more substantial defections, but the host does not receive an uncapped percentage of a great power's entire army.

The opening distinguishes four resource origins.
Locally mobilized personnel use the explicit finite founding allowance derived from the selected state's population in part 03 and leave a reserve for reinforcement.
That authored allowance is recorded separately from existing national manpower and measured donor transfers, without claiming a second native ethnic recruitment pool.
Verified military defections transfer a measured force or its measured resources from an actual donor.
Captured depots move only equipment that the selected transaction can lawfully and mechanically account for.
One explicit founding reserve represents irregular arms already present in the rising and is bounded by local population, economy, and opening severity.
This reserve is an event-created stock, not a falsely reported deduction from an unrelated country's national stockpile.

The initial force uses a scale-appropriate set of small native formations, with the smallest viable opening allowed to use one.
It does not use one oversized division to bypass the actual native recipe and supply limits.
It must have enough equipment and organization to defend itself immediately, with its readiness visibly below that of a mature professional army where the material situation demands it.
No free recurring replacement wave is attached to elapsed time.
Reinforcement comes from training, actual recruits, production, captured equipment, migration, or a fulfilled treaty.

The common systems specification supplies the authoritative formula, worked opening cases, and conservation rules.
All formulas use a single sampled opening snapshot, so the player cannot manipulate a second calculation by clicking an option after moving stockpiles or changing the selected country.
Native recruitment and stockpile changes after founding remain ordinary campaign behavior.

## Two public values

| Value | What it means | What changes it | What it governs |
| --- | --- | --- | --- |
| Host Cohesion, 0 to 100 | Acceptance of common command and the credibility of obligations between the host's military constituencies | Kept service terms, reliable pay and supply, participation in councils, disputed command, unequal burdens, broken host charters | Mobilization reliability, joint operations, political transitions, integration of other host traditions, risk of refusal or secession |
| Settlement Legitimacy, 0 to 100 | Acceptance of the civil settlement by the population the host governs | Land arbitration, functioning administration, civilian representation, delivered protection, uncompensated requisition, abuses, broken recognition terms | Local integration, recruitment breadth, recognition, peaceful accessions, resistance pressure, durability after conquest |

These are the only persistent custom values that the player is expected to track.
Operational stress is communicated through native manpower, stockpiles, supply, war status, mission conditions, and temporary consequences.
The design does not add a horse currency, raid currency, imperial legitimacy currency, host influence score, or a separate meter for every region.
Individual charters, promises, and treaties have readable states and exact terms.
Those records are commitments with outcomes, rather than additional continuously accumulated resources.

The values create tension without making one constitutional path a disguised punishment.
A confederation can maintain high Cohesion by honoring local command agreements.
A centralized state can maintain it through a credible common service law and reliable logistics.
Both need Settlement Legitimacy if they want durable control over large civilian populations.
Military coercion can secure short-term control, but it cannot substitute for every later civil requirement.

## Baseline campaign phases

| Phase | Entry and expected pace | Decisions that matter | Exit and continuing content |
| --- | --- | --- | --- |
| Manifestation | The founding transaction, immediately | Whether the human follows the host, how the old owner responds | A live country and a real military or negotiated relationship |
| Bridgehead | Approximately the first 90 to 150 days, dynamically extended by major disruption | Depot access, rationing, field command, first land settlement, ceasefire terms | Defensible capital and a sustainable initial force, or an orderly defeat and exile outcome |
| Established host | Usually the remainder of the first year | Service citizenship, treasury and workshops, representation, diplomatic dependence | A functioning charter and a constitutional commitment |
| Chosen polity | After the founding settlement, with no requirement to conquer a capital first | Confederation, civic republic, centralized command, social revolution, service restoration, or a patron settlement | A distinct focus and decision program with its own costs and opposition |
| Regional or national project | Once territory, logistics, legitimacy, and political terms make it credible | Host federation, Ukrainian or Russian statehood, steppe partnership, sea access, eastern host connection, or the Horde project | A formation settlement followed by integration, recognition, and a succession or demobilization test |
| Durable settlement | After victory, negotiated survival, reunification, or a contained defeat | Budget and service reform, veteran resettlement, constitutional succession, treaty renewal | A state that can remain playable without permanently farming the founding crisis |

The timings are pacing anchors.
War, displacement, ruined infrastructure, external support, and successful objectives alter them within the defined bounds.
An ordinary focus cannot advance a phase by itself while the necessary territorial or material conditions are false.
An active objective resolves when its actual requirements are achieved, without requiring a second reward click.

## What changes when the hosts answer

The baseline country can always negotiate with neighbors and pursue its political project.
The Hosts Answer changes the regional response to a surviving host amid major instability.
Historic host communities gain their own bounded response opportunities, including legal autonomy, local rising, military defection, volunteers, or refusal.
The leading host must choose between respecting separate partners and bringing them under a common state.

The evolution is not the ordinary constitutional congress, a military modernization stage, or a formation button.
It creates new actors and additional political obligations.
A hostile or independent answer is possible when the founding host's program threatens another community's interests.
The separate evolution specification defines activation, an evolved first opening, pacing, response selection, capacity limits, and cleanup.

## War, peace, and defeat remain playable

A host can win recognition without conquering all East Slavia.
An old owner can restore its state without receiving free permanent repression bonuses.
A host can accept a service compact, remain an autonomous subject, or become a member of a federation when the involved countries agree.
Those outcomes settle actual territorial and military claims and change future obligations.

The loss of the founding capital creates a relocation or evacuation problem if viable territory or an accepting refuge exists.
It does not automatically recreate the same army elsewhere.
An exile organization can preserve a political claim, remaining characters, and a limited contact network.
Any later return is a documented campaign action within the original episode, paid from surviving resources and requiring a new territorial opportunity.
Total defeat without a valid refuge closes the active host processor.
Earned history, prior treaties, and legitimate achievements remain recorded.

## Content promises

The specification gives every major route an entry, a political bargain, a military and economic program, external relationships, a capstone, a failure mode, and play after the capstone.
Regional traditions change objectives and available institutions, rather than supplying interchangeable modifiers.
Civilian communities, rival Cossack organizations, the old owner, and patrons can all refuse an offer for concrete reasons.
Grand formables require a settlement with their constituent regions and an affordable government after formation.
The Golden Horde project is explicitly a twentieth-century alternate-history claim built through steppe politics.
Its history, institutions, succession disputes, and trade ambitions are treated separately from Cossack national projects.

