# Part 07. The Hosts Answer and lifecycle

Event 112 Rise of Cossacks originated from catalog entry 122.
See part 13 for the user-confirmed identity and current workbook migration status.
The evolution spreads opportunities for new risings, actual volunteers, state defections, exact formation defections, and host compacts when major East Slavic powers undergo serious instability.
It preserves independent host choices and the same finite resource accounting used at founding.

This chapter extends the [founding and shared systems chapter](112_rise_of_cossacks_spec_part_03_founding_and_shared_systems.md).
It does not replace ordinary Rising, Settlement, or military modernization with a separate progression meter.
All chances, intervals, and caps below are proposed tuning, with exact native implementation and probability validation still required.
C means Host Cohesion and J means Settlement Legitimacy, each from 0 to 100.
I means normalized instability, W means normalized war pressure, and Rbar means normalized mean applicable resistance, as defined in part 03.
Numbered report, action, slot, and route labels are specification identifiers and do not claim an allocated native runtime namespace.

## 1. The Hosts Answer evolution

### 1.1 Shared unlock and once-only activation

The Hosts Answer is the tier 2 evolution of Event 112.
The shared chaos value must be at least 400, the existing event-evolution setting must be enabled, and this evolution must not already have been activated.
Activation uses the existing shared evolution evaluation seam and its ordinary cadence.
It does not add a new pre-host world scan or a separate daily evolution evaluator.

After the principal rising has fired, ordinary activation also requires at least 180 days of host survival and a viable Registered Host.
That host must own and control a usable capital, retain a functioning native force, have C at least 50 and J at least 45, and have completed its founding settlement.
An exile organization alone does not satisfy this landed-host gate.

The regional crisis gate requires either two qualified East Slavic powers in proven crisis episodes or one native major power at war with I at least 0.70 or surrender progress at least 50 percent.
For the single-major alternative, being at war is required in addition to either severity threshold.
Both alternatives use the same two qualifying observations 30 days apart that establish a crisis episode below.
An isolated one-tick instability spike cannot unlock the evolution.
The two-power alternative needs two distinct political powers, not two states or two observations of one power.

Before the principal event fires, the existing shared framework may activate the evolution when the tier, chaos, setting, once-only, and proven regional crisis gates pass.
Only the postfire host-survival and Registered Host conditions are waived in that prefire route.
The shared framework records the evolution flag without creating a country, granting resources, establishing a new host director, or inventing prior observations.
Any required prefire episode evidence must come from the existing shared evaluation seam.
If that seam does not yet expose the necessary bounded evidence, the adapter is an integration dependency rather than permission for a new global loop.
When Event 112 later fires, its opening freezes this already-active flag and uses the ordinary immediate spawn plus the separately defined day-14 bootstrap opportunity.

Once activated, the evolution remains activated if chaos later drops, its unlocking host changes identity, or the regional crisis temporarily ends.
An episode ending closes current opportunities under the normal lifecycle rules and never repeats the activation reward or flag transaction.
Activation itself creates no army, material grant, or new territorial crisis instance.

### 1.2 Episode qualification

The evolution activates a regional opportunity director over the accepted East Slavic power registry.
An eligible power is an ordinary human polity with an accepted East Slavic political identity and either native major-country status, eight owned East Slavic states, or at least ten million residents in that accepted region.
Part 02 owns this identity provider and exact regional mapping.
Merely occupying one East Slavic state does not turn an unrelated country into an East Slavic power.
Existing Event 112 member countries are not recursive external rising targets of their own director.
Their internal disputes use their actual charter and service commitments.

A power enters a crisis episode after two qualifying observations 30 days apart.
Qualification requires I at least 0.55 and either active war or mean applicable resistance at least 25 percent.
Surrender readings only contribute while the source is at war.
Surrender progress at least 50 percent also qualifies while at war.
An episode closes after two observations below I equal to 0.35, surrender progress below 15 percent, and mean resistance below 15 percent, or when the source power ceases to exist.
Different entry and exit thresholds prevent one fluctuating value from repeatedly creating new episodes.
Closing an episode does not delete an already independent host or cancel a physically dispatched transfer without its own disposition.

### 1.3 Cadence and caps

| Control | Proposed default |
|---|---:|
| Director observation cadence | 30 days |
| Rebuild of the bounded geography-owner cache | 90 days, plus validated ownership-change hooks |
| New independent host cooldown across the campaign | 90 days |
| Committed answer cooldown against an AI-only source authority | 120 days |
| Committed answer cooldown against a player source authority | 90 days |
| Maximum pending answer per source authority | 1 |
| Maximum simultaneously independent Event 112-created landed hosts, including principal | 4 |
| Maximum active registered participant countries, including existing living partners | 12 |
| Maximum exile or custody actors inside that same participant cap | 4 |
| Maximum new answer initiated per director observation across the campaign | 1 |
| Maximum completed territorial answer per observation | 1 |
| Maximum completed material answer per observation | 1 |
| Minimum delay before a pre-active evolution's exceptional first answer check | 14 days |

The director reads only the accepted geographic collection, its current owner/controller cache, and the explicit active power and host lists.
It never scans every world country every day.
The geographic provider must fit the declared bounded operation budget, with a proposed ceiling of 256 listed states per cache refresh and work split across scheduled slices if the accepted collection exceeds that ceiling.
The ceiling is an execution budget, not permission to omit legitimate geography.
No more than 16 states are revalidated in one slice.
Source and host lists are deduplicated before eligibility and weighting.

Each territorial rising or state defection consumes an actual local-crisis instance slot for every materially affected authority.
The shared cap of three still applies.
The evolution is regional and cannot pretend to be a worldwide-danger exception to bypass that cap.
Supporting an already admitted crisis does not create a hidden fourth territorial crisis.

### 1.4 Chance and outcome selection

For a qualified episode that is due and has crisis capacity, propose the following.
Here Rbar is the mean of the state resistance scores R on the zero-to-one scale, while the entry and exit tests above use native percentage readings.

`p_answer = clamp(0.10 + 0.25 I + 0.20 W + 0.15 Rbar, 0.20, 0.65)`

Apply the existing-crisis preference factor 0.7 to the power of its number of other active local crises.
For a player-controlled source multiply by 1.25 and clamp the final probability at 0.75.
This is a proposed per-observation probability for this bounded director, not a global event probability or an MTTH claim.
An observation with no valid outcomes performs no roll and does not spend the answer cooldown.
An actual failed random roll waits for the next ordinary 30-day observation.

Build the valid outcome pool before the answer roll.
If several source powers are due, choose one from the normalized selection weights `1 + 0.8 I + 0.6 W + 0.4 Rbar`.
This source-selection weight has no additional human or crisis-count factor because those adjustments already apply in p_answer.
Make at most one answer roll for this observation across the campaign.
An individual source's unconditional answer chance in a multi-source observation is its source-selection probability multiplied by its p_answer.
After that roll succeeds, select exactly one outcome from the following surviving weights.
The completion caps account for older pending answers and do not authorize a second new answer in the same observation.

| Outcome | Base weight | Additional exact conditions |
|---|---:|---|
| A new host rises | 32 | Valid unused state/carrier/ataman reservation and free created-host and participant slots |
| A border settlement defects | 28 | Valid local authority, contiguous recipient, C/J thresholds, exact state-transfer route |
| Volunteers answer | 20 | A real source manpower/equipment quantity, accepted recipient, and valid delivery route |
| An actual formation defects | 10 | One unique real eligible formation, verified preservation of its actual strength, equipment, experience, composition, and commander, plus an accepted recipient and physical route |
| An existing host offers a compact | 10 | A living distinct host with meaningful content and a valid diplomatic offer |

No surviving outcome means a clean no-op.
It does not force a new country, fabricate volunteers, or downgrade into a free generic reward.
The UI says which local conditions made the opportunity possible.
The actual private weight pool and external factors remain part of the probability-auditor evidence.
The exact-formation candidate uses the observed field unit and is independent of the source free-manpower reading.
A source with zero free manpower can therefore offer an eligible real formation while its free-manpower volunteer candidate is unavailable.
The common formation contract in part 03 limits the answer to one actual unit, preserves its current losses and obligations, and rejects duplicate ownership or an incompatible existing commitment.
If its exact native binding is unavailable, remove that formation candidate before normalization and mark the required feature as incomplete.
Do not replace the chosen formation with a personnel contingent or claim that another working outcome completes this required route.

### 1.5 New host strength

A new host uses the same factual snapshot and opening accounting as the principal rising.
Its proposed authorization is 60 percent of the primary formula, rounded down to a whole 250-person block, with an absolute maximum of 12,000 people.
It must still meet the 2,500-person viability floor without adding an artificial floor grant.
The new host receives one state and its own finite local muster receipt.
Its support relationship with the principal host is an offer governed by its council, politics, and existing wars.
The principal host does not automatically annex it or receive its army for free.

The campaign's 90-day new-host cooldown, four-created-host cap and twelve-participant cap, source crisis cap, source cooldown, available identities, and actual resources all constrain growth.
Every new host uses the 005/006/112 identity and reservation contract.
Releasing, annexing, or restoring a host never regenerates its original cache.

### 1.6 Evolution active before the first firing

The opening receipt freezes evolution_active_at_spawn before any country or resource mutation.
The principal country still appears immediately in one state with the ordinary fact-based muster formula.
It does not receive a second base grant or a player-specific multiplier.

The evolved opening additionally registers the regional contact and power cache, marks the founding appeal as already broadcast, and presents The Hosts Answer as active from the first report.
If the opening snapshot contains a qualifying power at war with either I at least 0.70 or surrender progress at least 50 percent, a single bootstrap answer check is due after 14 days.
The snapshot marks that source as bootstrap eligible, then the day-14 check revalidates its current severity and all physical conditions.
The principal founding counts as a new host for the campaign 90-day new-host cooldown.
Consequently, this early check can produce a legal compact, real volunteers, one independently eligible exact formation, or an independently eligible state defection, while a second independent host waits until that cooldown expires.
This one explicit bootstrap check does not need a fabricated earlier observation.
It obeys all identity, source, route, active-host, local-crisis, and material caps.
If no severe source exists, the normal two-observation qualification applies.

The bootstrap receipt prevents repeat early checks on reload, control switch, or the principal host's restoration.
Successful early volunteers are real transfers and successful early risings are separate newly accounted host countries.
An evolution activated after the ordinary founding begins its normal director schedule and never reruns opening initialization.

## 2. Player-facing counterpressure

The higher initial target weight and shorter evolution source cooldown implement the mandatory difficulty rule where a human country faces the uprising.
If the player instead controls a host, harder supported crisis behavior applies only when a real external grievance or punitive-response opportunity exists.
A peaceful newly selected host is not assigned an extra arbitrary threat just because control changed.

For a country with an existing punitive claim created by a peacetime stores raid or a broken recognized frontier settlement, propose a 20 percent adverse-response opportunity at each 30-day due observation for an AI host target and 25 percent for a human host target.
After a committed adverse response, the same host lineage has a minimum 120-day AI cooldown or 90-day human cooldown.
The response still needs a living willing opponent, an actually valid action, and available local-crisis capacity.
The opponent pays its normal costs and does not receive free punitive divisions.
The host receives a warning and the same defensive and diplomatic counterplay.

Ordinary arms prices, training costs, grants, trade terms, and meter arithmetic are unchanged by human control.
The same country changing controller does not reset its current cooldown.
Only a newly scheduled supported crisis uses the appropriate current player factor.

## 3. Defeat, restoration, and cleanup

### 3.1 Loss is recorded once per episode

Losing the founding state records one C/J loss and ends the temporary founding-state defense effect.
If another owned and controlled state exists, the host relocates its capital through the validated ordinary native route.
It keeps its identity, current equipment, templates, political route, completed reforms, and receipts.
The survival objective needs 90 elapsed days and checks for a currently valid controlled capital and functioning force inside its 120-day mission window.
Success takes precedence over timeout at the shared deadline.
It does not restart its clock or award a new opening package after a capital move.

Capitulation suspends offensive missions, new compact admissions, and undispatched material transfers.
It does not erase historically completed charters or duplicate a surviving field army.
A country can be capitulated while still having a valid native existence, so capitulation and deletion are separate lifecycle states.

### 3.2 Political exile and restoration

A host without land can retain a political_exile identity only through an explicit accepting sponsor or recognized surviving council.
This is a political registry state unless the actual native government-in-exile rules have been verified and fulfilled.
The system does not claim native exile bonuses simply because a flag says exile.

Only assets actually evacuated before loss, delivered to a sponsor, or transferred under a verified native route survive as material receipts.
A remembered pre-defeat army size is not a resource pool.
An exiled ataman without material proof has a political identity and zero implied manpower or equipment.
Captured, dead, transferred, and retired characters retain exclusive status.

Restoration needs a real state-transfer agreement or an independently valid territorial result, an eligible original carrier, and a living correctly owned leadership identity.
It reactivates the original host lineage and imports only its actual surviving resources.
There is no fresh opening cache, no reset of prior local mobilization, no automatic veteran recreation, and no cleared raid history.
If no carrier or leader route can be safely restored, the political circle may join another host through a documented integration outcome.
It cannot occupy a different live tag by renaming it.

### 3.3 Pending transactions at loss

Undispatched quotes are invalidated and no resource is paid.
Dispatched assets remain tied to their physical donor debit and current custodian.
A receiver's annexer does not automatically inherit an asset that is still held by a different sponsor.
Redirecting a shipment requires explicit authority, a valid destination, and one new delivery disposition linked to the original receipt.
Paid projects in a lost state either cancel under their declared refund contract or continue only if their genuine owner still has authority.
Refunds never recreate a deleted payer and never use an ordinary undiscounted cost.

Native prepared raids follow the engine's verified cancellation and return behavior.
Event 112 clears only its own eligibility and receiver markers.
It does not invent a native refund or allow a late resolution to hit the state's new friendly owner.

### 3.4 Campaign closure and coordinator succession

If the principal host disappears while another registered host survives, the oldest valid landed host takes the internal coordinator role.
This transfers scheduling responsibility only.
It does not transfer political leadership, territory, currencies, troops, or ownership of other events' content.

When no landed host, accepted exile, pending transfer, or unresolved physical receipt remains, stop all Event 112 scheduled activity.
Clear transient global targets, current reservations, actor receiver slots, map projections, and outstanding public missions owned by Event 112.
Remove event-owned temporary modifiers without deleting shared doctrine, native units, or another owner's national focus tree.
Release completed local-crisis instances through the shared crisis owner.
Preserve the global successful Fire-Once flag, historical host identities, opening-grant proof, used carrier generations, character ownership history, and completed/refunded receipt tombstones.

## 4. Chaos, shared presentation, and route integration

Event 112 remains the one Minor Fire-Once entry in the shared event registry.
Child host opportunities are stages and receipts of its evolution, not additional ordinary scheduler firings of the same event.
The catalog's chaos level 1 and Formables Medium membership are classification fields.
They are not assumed to mean an unverified numeric add-to-chaos effect.
The integration owner binds exact Event Log, Event Details, evolution registration, stage identifiers, country crisis counting, and any shared chaos-meter contribution to the inspected framework.

Cossack polities remain ordinary human societies.
They do not enter the actual-nonhuman classifier, disable ordinary civilian systems, or register as an apocalyptic world-threat source merely because this event created them.
Civilian outcomes use the existing shared policies when such outcomes actually occur.

Public milestones are the founding, survival or defeat, charter settlement, significant host admission, The Hosts Answer activation, a major regional rising, and a researched political formation.
Routine monthly reviews, quote recalculation, and internal reservation changes do not become news spam.
Public qualitative text describes the military and political situation.
Exact stock, capacity, receipt, and private eligibility information is restricted to the relevant owner/controller surfaces.

The political route integration request carries campaign and host IDs, current government and character ownership, accepted charters, controlled territorial proof, active obligations, opening-used proof, current C/J values, tradition slots, and native army ownership.
The formation transaction returns a stable resulting carrier/cosmetic identity, exact changed territory, granted claims or cores, renamed institutions, explicit retained obligations, and one completed formation receipt.
Golden Horde and Cossack Russia are researched political outcomes in part 05 using this same contract.
They do not obtain duplicate manpower, armies, stockpiles, or technology unions merely because a new title appears.

### 4.1 Concrete Chaos Impact Table

The following values are proposed design tuning for the shared Chaos system.
They are not the catalog's chaos-level classification.
Only an actual committed consequence can add or remove Chaos.
Eligibility, selecting an evolution, opening a focus group, changing a flag, and recording a milestone each contribute zero by themselves.

Each contribution uses the shared history route with the actual cause, actor, scope, magnitude, and unique receipt.
Before applying an Event 112 contribution, inspect whether a shared war, annexation, death, country-fragmentation, or another event owner already accounts for that same causal outcome.
That owner keeps the contribution.
Event 112 records a linked zero additional entry rather than charging the same outcome twice.
A distinct political consequence must be described precisely before it can receive its own entry.

| Impact code | Concrete committed consequence | Proposed Event 112 contribution | Dynamic condition and repeat guard | Containment or reversal |
|---|---|---:|---|---|
| CI01 | The initial unrecognized armed host becomes a viable independent country | +2 | One successful opening receipt, zero additional if the same fragmentation is already fully owned by a shared consequence | Up to the actual credited 2 can be removed after a recognized durable regional settlement and 180 days without its founding existential crisis |
| CI02 | An additional independent host creates a genuinely new unresolved regional authority | +3 for the first, +2 for the second, +1 for the third | Actual new country and crisis receipts, diminishing across the campaign, total at most 6 | Remove only that host's credited portion after its crisis is durably settled or its institutions close through an actual settlement |
| CI03 | The resurgence becomes an unresolved movement across at least three regional cohorts and two source powers | Up to +5 | One campaign-wide receipt, requiring actual participating hosts or completed territorial answers in those distinct regions, not three messages or volunteer batches | Up to the outstanding credited amount can reverse after 180 days with no qualifying regional crisis episode and honored settlements for surviving participants |
| CI04 | A host breaks recognized agreements and creates simultaneous new interstate disputes with two distinct living counterparts | Up to +3 | Actual material breaches and responses, once per campaign, no payment for a grievance already counted as a shared war outcome | Reverse only the outstanding credited amount after both disputes are actually settled and 180 days of compliance |
| CI05 | A contested Cossack Russia national order is established over the required heartland and provokes a distinct unresolved succession dispute | Up to +10 | Actual GP02 political and territorial completion, living rival claimant or materially contested settlement, and one national-order account | Recognition and a completed national reconstruction settlement can remove the account's outstanding attributed contribution |
| CI06 | A contested Golden Horde imperial order is established across its required regions and provokes a distinct unresolved regional-order dispute | Up to +12 | Actual GP03 completion and relevant opposing counterpart, no automatic addition for a voluntary commonwealth | Recognition, accepted member terms, and the first postwar settlement can remove the outstanding attributed contribution |
| CI07 | A durable voluntary Union of Hosts resolves previously credited fragmentation | No new positive contribution | Actual charters, contributions, and 180-day compliance, not the congress announcement | May remove eligible outstanding CI01 through CI03 portions, never more than those receipts actually credited |
| CI08 | A state transfer, war, annexation, or death already handled by the shared owner | 0 additional | Link the actual shared receipt and preserve its ownership | Event 112 never reverses another owner's war or death contribution |
| CI09 | Training, a successful ordinary raid, actual volunteers, a civilian return, or a peaceful constitutional name change | 0 | These outcomes matter through their actual military, social, and political effects | No negative reward is generated merely because the action was peaceful |
| CI10 | Evolution eligibility, activation, prefire state, internal cache refresh, or log display | 0 | All occurrences | No reversal because no contribution exists |

CI05 and CI06 share one national-order account.
The maximum cumulative positive addition from that account is 12.
Changing from one national identity to the other can add only a genuinely justified difference up to that maximum.
It cannot pay 10 and then 12 for successive cosmetic declarations.
A peaceful civic federation or accepted commonwealth receives zero positive formation Chaos unless a separate real contested consequence qualifies.

All discretionary Event 112 positive additions together are capped at 30 for the campaign.
This cap excludes genuinely independent shared war or death effects owned elsewhere.
The source, actor, state, partner, and host-lineage receipts survive annexation, restoration, and cosmetic changes.
Closing an episode does not clear the lifetime contribution guard.

A reversal uses only the actual outstanding positive amount attributed to its matching cause.
It cannot drive the shared meter below its supported floor or refund an amount that was never credited.
The history records the measured applied change.
A settlement cannot repeatedly earn negative Chaos by being signed, broken, and signed again.
Reversal settles the credited cause and never restores its one-time positive allowance.

The complete-package implementation gate includes a cause-overlap trace for initial formation, a secondary host, a war, a death-bearing transfer, a peaceful federation, both national projects, and a repeated restoration.
Source review alone does not prove that the current shared framework has every required receipt field.
The integration owner must bind this table to the actual inspected Chaos and Event Log interfaces without inventing unsupported engine parameters.


## 5. Evolution examples and acceptance scenarios

### 5.1 Chance and answer arithmetic

Take the stressed regional source in part 03 Case B, with I equal to 2/3, W equal to 2/3, and mean normalized R equal to 1/3.
The answer chance before crisis preference is `0.10 + 0.25 × 2/3 + 0.20 × 2/3 + 0.15 × 1/3 = 0.45` per due selected-source observation.
With one other local crisis, the AI-only source chance is `0.45 × 0.7 = 0.315`, or 31.5 percent.
The comparable player source chance is `0.315 × 1.25 = 0.39375`, or 39.375 percent.
There is only one selected source and at most one new answer roll across the campaign at that observation.
The player factor changes opportunity pressure, not the resources of the country that rises.

At maximum I, W, and mean R, the unmodified chance is capped at 0.65.
The player factor would produce 0.8125, so the final cap is 0.75.
Three already active local crises still block a new territorial answer regardless of this probability.
A failed random roll creates no cooldown receipt for a successful answer and waits for the next normal observation.

If all five outcome types are valid, their weights 32, 28, 20, 10, and 10 total 100.
If only real volunteers and an existing host compact are valid, their normalized chances are 2/3 and 1/3 within the already successful answer.
If only an exact real formation and an existing host compact are valid, their normalized chances are 1/2 and 1/2, including when the source has zero free manpower.
An absent required source stockpile or free-manpower quantity removes the volunteer candidate instead of leaving a fictional volunteer result in the draw.
The separate formation candidate survives only when its actual unit and exact transfer contract remain valid.

For a secondary rising derived from Case C's primary authorization of 26000, `floor(26000 × 0.60 / 250) × 250 = 15500` before the secondary cap.
The 12000 absolute secondary ceiling therefore authorizes 12000.
For Case A, 60 percent of 3750 is 2250, below 2500, so no secondary country can rise from that candidate.
There is no automatic minimum bonus that rescues an invalid secondary opening.

### 5.2 Prefire evolution timeline

Assume The Hosts Answer was already active before a valid founding on day 0.
The normal one-state principal country appears immediately with the normal snapshot budget, and the opening marks the appeal and evolution snapshot once.
If an accepted major East Slavic source is at war and has I at least 0.70 or surrender progress at least 50 percent, the single bootstrap opportunity becomes due on day 14.
The director rechecks current severity, local crisis capacity, exact identities, available resources, and routes on day 14.
It can dispatch actual volunteers, transfer one independently eligible exact formation, initiate a valid compact, or propose an independently valid state defection.
The principal founding has already started the 90-day campaign cooldown for a new independent host, so the bootstrap cannot create a second independent host on day 14.

The regular observation schedule remains anchored to day 30, day 60, day 90, and so on.
The bootstrap is an additional once-only due point, not a reset of those dates.
A source with no severe bootstrap snapshot needs its ordinary two qualifying observations 30 days apart.
A successful answer against that source begins its 120-day AI-only or 90-day player-source cooldown.
The actual current control context is sampled at commitment and a later control switch cannot shorten an already committed cooldown.

At day 90 the campaign new-host cooldown can expire, but a particular source still needs a qualified episode, available source cooldown, a viable state and carrier, crisis capacity, and a successful selected-source opportunity.
The elapsed date does not guarantee an uprising.
The other hosts remain independent actors with their own accepted councils and agreements.

### 5.3 Evolution, raid, and lifecycle cases

| ID | Scenario | Required result |
|---|---|---|
| L01 | Evolution activates after ordinary founding | Start director scheduling only, no second primary country or founding resources |
| L02 | Evolution was active at founding but no source met severe snapshot criteria | No day-14 shortcut, ordinary two-observation qualification |
| L03 | Severe prefire source stabilizes before day 14 | Consume the one bootstrap check without a forced reward, preserve normal scheduling |
| L04 | Severe prefire source has willing actual volunteers on day 14 | One measured batch or offer, no source-free people |
| L05 | Bootstrap new-host candidate is otherwise valid | Respect the 90-day campaign host cooldown started by the principal founding |
| L06 | Four independent Event 112-created hosts already exist | No fifth independent created host, preserve living countries, choose another independently valid answer or none |
| L07 | Four active exile or custody actors or twelve total participant countries already exist | Do not discard people or characters to free a slot, reject new discretionary admission and resolve existing obligations |
| L08 | Several source powers qualify at the same observation | Deduplicate and select one source, at most one new answer roll across the campaign |
| L09 | All answer outcomes are physically invalid | No roll, no cooldown, no generic reward |
| L10 | Source fluctuates around the entry threshold | Two-entry and two-exit observations prevent rapid episode renewal |
| L11 | An unrelated occupier controls regional states | It can be a valid displaced authority in founding, but does not become an East Slavic political power solely by occupation |
| L12 | A member host becomes internally unstable | Use its real charter disputes, no recursive self-targeting by the external rising director |
| L13 | A secondary rising's 60 percent budget is 2250 | Reject below minimum, no floor grant |
| L14 | A successful answer would exceed the shared three-crisis cap | Territorial answer blocked, no worldwide-danger exemption |
| L15 | The regional collection exceeds a 256-state refresh budget | Continue declared slices without omitting valid states, at most 16 revalidations per slice |
| L16 | A prepared raid becomes unavailable before resolution | Revalidate the existing native instance and cancel or invalidate according to the verified contract |
| L17 | Two host raids resolve at nearly the same time | Disjoint exact-one relay slots retain correct actor, victim, state, province, and receipt |
| L18 | Raid victim, state owner, or controller changes during preparation | No damage or loot redirected to a new friendly owner, native-owned costs follow native cancellation rules |
| L19 | Source stocks vanish before stores-raid resolution | Actual captured stock is zero, no made-up depot cache |
| L20 | Actor repairs, raids, renames, and raids the same target again | State, victim, actor-lineage, extraction, XP, and Cohesion cooldowns survive those changes |
| L21 | Peacetime raider becomes player controlled after the grievance | Future due checks use the supported human crisis factor, existing committed cooldown is not shortened |
| L22 | Human host chooses ordinary peaceful arms trade | No blanket human price penalty or hostile response without the defined grievance |
| L23 | Founding capital is lost but another viable state remains | Relocate through native rules, keep the 90-day survival clock and one loss receipt |
| L24 | Capitulation occurs with living country and troops | Suspend the appropriate offensive actions, preserve actual units and pending receipts |
| L25 | Last state is lost but a willing sponsor accepts the council | Political exile with real surviving assets only, no assumed native exile benefits |
| L26 | Exile has no evacuated equipment or manpower | Keep political identity and permitted characters without fabricating an army |
| L27 | An exiled host restores into a valid real state | Same durable host lineage and used opening receipts, actual available assets only |
| L28 | Principal country disappears while other hosts survive | Bounded oldest eligible coordinator succession for scheduling only, no political annexation |
| L29 | A pending delivery exists when a country is annexed | Exact return, redirect with consent, custody, or loss receipt, never both original and annexer delivery |
| L30 | A peace settlement reconstitutes an earlier tag | No repeat workshop, initial Army XP, political setup, tradition, or opening cache |
| L31 | Last active actor and pending obligation are gone | Stop timers and clear owned temporary markers, preserve Fire-Once, history, identities, and tombstones |
| L32 | A final national project changes flag, name, or ideology | Receipts, obligations, remaining assets, and used grants survive the new presentation |
| L33 | Chaos is 399, tier 2 is unavailable, or the evolution setting is disabled | No activation, even if a host and severe regional crisis exist |
| L34 | Postfire host is 179 days old or has C below 50 or J below 45 | No ordinary unlock, the rising and its recovery remain playable |
| L35 | One native major has a severe spike at only one observation | No unlock until the same two-observation episode proof is satisfied |
| L36 | Two distinct qualified powers meet proven episode conditions | Regional gate passes subject to all other shared and postfire gates |
| L37 | Shared prefire gates pass before any host exists | Record the once-only evolution flag through the existing shared seam, no new host loop or resource grant |
| L38 | Chaos falls after activation and later rises above 400 again | Preserve one activation, no repeated flags, bootstrap, resources, or activation consequence |
| L39 | All five answer types are genuinely valid | Normalize weights 32, 28, 20, 10, and 10 to one pool and dispatch exactly one selected outcome |
| L40 | Only exact formation and existing compact are valid, with source free manpower zero | Both remain at one-half of the successful answer pool, no invented volunteer quantity and no free-manpower veto on the real unit |
| L41 | Exact formation transfer lacks a verified native preservation binding | Remove that candidate before normalization and retain its required-incomplete status, no personnel fallback can count as its completion |
| L42 | One formation is renamed or pledged to another active mission before commitment | Revalidate its same unit lineage and incompatible obligations, then reject duplication or transfer only its one actual body of troops |

## 6. Runtime and evidence limits

The director is a proposed Event 112 owner system.
It is not claimed to exist in the pinned repository.
Its owner list, cache slices, due dates, pending-answer slots, crisis tokens, and cleanup receipts must be implemented with inspected engine operations.
No new global daily or periodic all-country loop is authorized.
The shared scheduler and probability auditor must inspect the full final eligible pools and preserve the original baseline before changing weights.

Native raid availability, cavalry eligibility, current DLC requirements, preparation ownership, cancellations, probabilities, and country-root relays need the installed raid documentation and scenarios.
Political exile can remain a contact organization when native government-in-exile requirements are unmet.
Formation defection is required selected content, with activation blocked until the engine can preserve exact real strength, experience, equipment, composition, and unique commander ownership.
A verified volunteer or deserter-contingent route can operate independently but does not replace that required feature or establish that the complete package is implemented.

The implementation appendix in part 03 identifies the inspected shared contracts and the older-source mismatches.
Those source findings are not live-game bug proofs.
No MCP suite, game launch, live save, command, or runtime validation is reported as completed here.
