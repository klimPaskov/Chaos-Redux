# Event 023 specification, Part 4: Targeting, coercion, and nuclear use

## Purpose of the targeting layer

Event 23 gives the Soviet Union decisions to target countries, issue demands, prepare exact strikes, and authorize nuclear use. These actions must create pressure without turning the stockpile into a universal surrender button.

The target receives time, choices, and foreign support opportunities. The Soviet Union must decide what it wants, what it is willing to destroy, and whether the threat remains credible after delay, refusal, compromise, or public exposure.

The system separates four steps:

1. Select a valid target country.
2. Define a public demand and a broad strike profile.
3. Prepare one exact target state and delivery route.
4. Authorize, hold, redirect, or abort the release.

No decision should jump directly from country selection to an unreviewed detonation.

## Target-management presentation

Use the reusable selected-target decision pattern to avoid showing one decision for every country.

The player sees:

- One action to select or change the current target.
- A short target summary.
- Only the demand and preparation actions valid for that target.
- One action to close the target view.

AI should evaluate all valid targets through its own scoring route and should not depend on the human target selector.

A selected target must clear when the country is annexed, becomes invalid, joins the Soviet faction under a settlement, accepts the demand, loses the relevant territory, or enters a terminal world state.

## Country eligibility

### Baseline wartime targets

Before Evolution II, a country can be targeted only when all relevant conditions hold:

- It is at war with the Soviet Union.
- It is not a Soviet subject, ally, or faction member.
- It has at least one exact state valid for a shared nuclear strike.
- The Soviet Union has a usable delivery route under current vanilla rules.
- The Soviet stockpile contains at least one unreserved operational bomb.
- Readiness and Integrity meet the selected profile's floor.
- No active cooldown, unresolved launch, or duplicate target mission exists.

### Evolution II coercion targets

Evolution II adds peacetime or civil-conflict targeting against:

- Valid minor countries.
- Soviet breakaways created or recognized through Event 5.
- Countries holding registered Soviet nuclear devices or storage sites.
- Countries occupying a Soviet core, capital region, or registered strategic nuclear facility.
- Countries already under a bounded Soviet ultimatum connected to an active conflict.

A peaceful major should not become an ordinary coercion target. Major-to-major nuclear targeting belongs to Evolution III and IV crisis logic.

### Hard exclusions

The following should be blocked unless a separate accepted route explicitly overrides them:

- The Soviet Union itself.
- Countries with no valid exact state target.
- Countries protected by an active settlement or stand-down.
- Special nonhuman or scenario countries when shared nuclear effects do not support them.
- Countries inside the same faction.
- Subjects whose overlord is the Soviet Union.
- Targets already destroyed or capitulated when the demand has become meaningless.
- A country selected only because it is small, with no Soviet strategic interest or conflict basis.

## Demand families

A demand states what compliance means. The target should never receive a vague choice between submission and destruction without knowing the public issue.

### Cease hostilities

Used during an active war.

The target is asked to accept a ceasefire, white peace, or a bounded armistice that preserves the conflict's current territorial logic. The exact settlement must use verified peace helpers and must not silently annex unrelated territory.

### Withdraw from Soviet territory

Used when the target controls Soviet cores, the Soviet capital region, or registered nuclear sites.

Compliance requires withdrawal, transfer, or a negotiated handover of named states. The demand should identify the states or named region.

### Return nuclear devices and personnel

Used during Soviet Collapse or after a custody seizure.

Compliance can return devices, technical staff, codes, components, or storage access. The target may negotiate security assurances, recognition, fuel, economic aid, or joint custody.

### Accept Soviet protection

Used against a valid minor or breakaway after Evolution II.

Compliance can create a guarantee, nonaggression arrangement, military access pact, subject relationship, or reintegration settlement according to the target's status. A full subject or reintegration outcome should require stronger Soviet leverage than a truce or device return.

### Demilitarize a strategic zone

Used when a border, airfield, missile site, port, or nuclear facility creates an immediate threat.

Compliance removes or limits a specific military condition. The demand should use named states or a verified region and should not produce a generic permanent debuff.

### Surrender in a collapsing war

Used only when the target is already close to defeat, the Soviet Union has a dominant conventional position, and a nuclear demand would plausibly accelerate an existing collapse.

It must not grant a free full annexation of a healthy country. The final settlement should follow the war's real objectives and current peace logic.

## Threat methods

### Private signal

A secret message communicates capability and a bounded demand.

- Lowest public diplomatic cost.
- Weakest credibility without a prior test or verified leak.
- Gives the target room to negotiate quietly.
- Can fail because the target doubts the weapon or the delivery route.

### Public ultimatum

A declared demand names the target and consequence.

- Raises credibility when the arsenal is Demonstrated.
- Raises diplomatic and condemnation pressure even if no strike occurs.
- Encourages foreign guarantees and public resistance.
- Creates a visible deadline.
- Backing down without a settlement damages future credibility.

### Wartime demonstration

A test or remote detonation accompanies the demand.

- Consumes a bomb.
- Routes through the shared test or demonstration adapter.
- Improves proof and urgency.
- Creates contamination and possible deaths according to location.
- Can harden the target's resistance if the display is seen as indiscriminate or desperate.

### Limited attack warning

The Soviet Union announces that a military or logistics target is being prepared.

- Available only during war or an active custody crisis.
- Gives the target a chance to evacuate, disperse, surrender the objective, or seek interception.
- Makes a later strike more credible.
- Can reduce immediate deaths through evacuation, while making military interception easier.

## Target response framework

The target receives a timed response mission. The normal response window should be long enough for diplomacy and preparation, usually 14 to 45 days depending on urgency.

Target options include:

- Accept the demand.
- Offer a partial settlement.
- Request more time.
- Refuse publicly.
- Refuse privately and prepare evacuation.
- Seek a major guarantee.
- Join or request entry into a faction.
- Invite foreign forces or observers.
- Disperse industry, aircraft, command, or nuclear custody.
- Expose the threat to the world.
- Attempt sabotage or a raid against Soviet delivery or storage assets.
- Prepare retaliation when the target has nuclear capability.

The response set should be filtered by actual campaign state. A landlocked minor cannot request a naval evacuation route that does not exist. A country without allies cannot rely on a guarantee that no valid major will consider.

## Compliance logic

Compliance should be driven by a weighted assessment, then audited through the probability tools.

Factors that make compliance more likely:

- The Soviet Union has publicly demonstrated the arsenal.
- The Soviet Union has a prepared exact target and credible delivery route.
- The demand is limited and specific.
- The target is losing the conventional war.
- The target is isolated.
- The target lacks nuclear weapons and strong air defense.
- Soviet prior threats ended in action or credible settlement.
- The target's capital, army, or strategic site is exposed.
- The target has low stability, low war support, or a fragile government.

Factors that make compliance less likely:

- The demand requires national extinction or unconditional annexation.
- The target has nuclear capability.
- The target is guaranteed by a strong major.
- The target belongs to a strong faction.
- The Soviet delivery route is weak or uncertain.
- Soviet Readiness or Integrity is poor.
- The Soviet Union has issued repeated empty threats.
- The target is winning the conventional war.
- The threatened profile is indiscriminate and creates strong domestic resolve.
- A player controls the target and chooses to resist.

Nuclear capability should not grant a flat coercion bonus that overrides these factors. Research on nuclear coercion indicates that compellent threats often suffer from credibility and cost problems. The gameplay should reflect that uncertainty.

## Partial settlements

A partial settlement should be common enough to create bargaining play.

Examples include:

- A temporary ceasefire instead of surrender.
- Return of nuclear devices without political reintegration.
- Withdrawal from one named region while another dispute remains.
- Joint custody under foreign observers.
- A security guarantee in exchange for disarmament.
- A Soviet guarantee instead of subject status.
- Demilitarization with no territorial transfer.

The Soviet player can accept, reject, or raise the demand. Raising it should shorten the deadline, increase foreign reaction, and make compliance less likely.

## Credibility memory

The event should track a bounded credibility memory without exposing another permanent meter.

Credibility improves when:

- A public test succeeds.
- A prepared warning is followed by a limited strike after refusal.
- A target accepts a demand that foreign observers understand.
- The Soviet Union keeps a negotiated settlement.
- Delivery and command remain visibly ready during a crisis.

Credibility declines when:

- A test fails publicly.
- The Soviet Union issues an ultimatum, then withdraws without settlement.
- A prepared strike is technically aborted after being exposed.
- The Soviet Union threatens a target it cannot reach.
- Conflicting Soviet authorities issue different demands.
- Breakaways seize devices and Moscow cannot account for them.

Credibility should decay slowly toward neutral. One successful coercion should not make every later target surrender.

## Strike profiles

The event selects a strategic profile, then the shared nuclear route resolves the exact physical consequences.

### Remote demonstration

- Uses a valid remote or evacuated location supported by the shared adapter.
- Intended to prove resolve with the lowest direct military effect.
- Still creates contamination and political consequences.
- Can be selected before a combat strike when the target refuses.

### Military concentration

- Targets a state with meaningful enemy divisions or a verified military concentration.
- Requires current war.
- AI prefers this profile for bounded first use against a nonnuclear enemy.
- The shared adapter determines military and civilian losses.

### Logistics node

- Targets a state with a supply hub, major railway junction, port, or other verified logistics value.
- Requires a live military reason.
- Can damage the wider front and civilian infrastructure.
- The target should be able to disperse or reinforce the node during the warning window.

### Industrial complex

- Targets a state with substantial military industry or strategic production.
- Carries heavier civilian and economic consequences.
- Requires higher Readiness and stronger authorization.
- AI uses it only after severe conventional failure or prior nuclear use by the enemy.

### Capital command

- Targets the enemy capital or a verified national command center.
- Creates high escalation risk.
- Blocked for ordinary limited coercion.
- AI uses it only during retaliation, an active major exchange, or a near-capitulation emergency at Evolution IV.

### Populated center

- Targets population as the primary strategic purpose.
- This is the highest-consequence countervalue profile.
- It requires explicit player confirmation and the widest evolution access.
- AI should almost never select it. Evolution IV, 1000 or more Chaos, an active nuclear major war, severe strategic loss, prior enemy nuclear use or confirmed imminent enemy use, and no valid lower-consequence target should all be required.

## Exact state targeting

Every strike needs an exact target state before final authorization.

The state must remain valid at launch time. Validity includes:

- The target country still owns or controls it according to the shared strike contract.
- The selected profile still has a real basis in that state.
- The state is reachable through the current delivery route.
- The target is not protected by a completed stand-down.
- The state has not become an invalid special target.

If the state becomes invalid, the mission pauses or cancels. It must not redirect to a random state, a capital proxy, or another profile.

## Delivery-route requirement

Event 23 should use the current installed vanilla nuclear delivery system.

Possible routes may include strategic bombers, raids, missiles, or another current vanilla path. The implementation must inspect the installed version and DLC state before naming exact requirements.

Event 23 may improve delivery preparation, reserve a suitable force, and validate range, fuel, air access, or launch readiness. It should not create a parallel nuclear combat system or grant free delivery aircraft.

Event 32 may later add missile capability. Event 23 can detect and use that capability through a neutral hook, but it must remain fully playable with a verified base delivery route when Event 32 is absent.

## Authorization chain

A strike follows a staged authorization process.

### Preliminary authorization

- Reserves one bomb.
- Locks the selected target country, state, and profile.
- Starts a visible preparation mission.
- Applies temporary readiness and exposure consequences.
- Gives the target its response and evacuation window.

### Technical certification

- Checks the device, delivery route, current state validity, and command chain.
- A scientific safety veto can delay or block the strike under the relevant custody doctrine.
- The player may overrule the veto at a serious Integrity cost when the route permits it.

### Final authorization

- Occurs only after preparation and certification.
- Requires a separate deliberate action for the human player.
- Rechecks every target, war, stockpile, and command condition.
- Calls the shared strike adapter exactly once.
- Commits the reserved bomb only after the adapter accepts the strike.

### Hold, redirect, and abort

Before release, the Soviet Union may:

- Hold the strike while keeping the target mission active.
- Accept a late settlement.
- Redirect to another valid state under the same profile after a new certification delay.
- Reduce the profile to a remote demonstration.
- Abort and return the bomb after accounting.

After the shared adapter confirms release, the event cannot refund the weapon or reverse consequences.

## Shared consequence handoff

Event 23 owns:

- Soviet authorization.
- Target country.
- Exact target state.
- Strategic profile.
- Delivery route proof.
- Reserved stockpile transaction.
- Warning and response timing.
- Command and credibility consequences.
- Event-owned follow-up reports.

The shared nuclear system owns:

- The physical detonation.
- Population loss.
- Military deaths and disruption where supported.
- Building damage.
- Fallout and state contamination.
- Air Cleanliness pressure.
- Condemnation and evidence.
- Direct nuclear-use Chaos changes.
- Shared death logging.
- Long-term radiation effects.
- Terminal Fallout readiness.

Event 23 must not apply a second population, contamination, condemnation, or Chaos effect after the shared route succeeds.

## Soviet AI use boundaries

### Below Evolution II

AI may prepare and test weapons. It can issue wartime warnings. It should not use peacetime coercion.

### Evolution II, below 800 Chaos

AI may issue bounded demands to minors and Soviet breakaways. Limited combat use is possible only when:

- The target is nonnuclear.
- The Soviet Union is in a serious war or custody crisis.
- A valid military or logistics target exists.
- Conventional options are failing or much more costly.
- Readiness and Integrity are high enough.
- The target refused a specific demand or has used mass-destruction weapons.
- No active stand-down or acceptable settlement exists.

### Evolution III, 800 to 999 Chaos

AI can retaliate against a nuclear major after confirmed enemy nuclear use. It does not deliberately initiate a major-to-major exchange.

### Evolution IV, 1000 or more Chaos

AI first use against a nuclear major becomes possible, but only under the strict conditions in Part 5. High Chaos alone cannot authorize it.

## Target AI response

Target AI should distinguish deterrence from compellence.

- It should resist demands that would destroy the state when Soviet use appears disproportionate or unlikely.
- It should accept limited, enforceable settlements when isolated and losing.
- It should seek a guarantee when time and diplomacy allow.
- A nuclear target should favor warning, dispersal, retaliation preparation, and hotline use.
- A breakaway holding devices should prefer bargaining over immediate use unless its own command and delivery conditions become operational.
- A target should remember Soviet compliance with prior settlements and should punish repeated bad-faith escalation.

## Multiplayer behavior

A human target must always receive the response event and full response window unless a true immediate retaliation route is being resolved.

The Soviet human player must receive final authorization before first use. Multiplayer should not allow one player to bypass another player's response through rapid repeated clicks, tag switching, or reopening the target category.

All reservation, selection, and response state must persist through save and reload.

## Writing direction

Targeting text should state the concrete demand, the target country, the named place or strategic purpose, and the available time. It should avoid generic language about destiny, final warnings, or a world on the edge.

Target reactions should show evacuation, military dispersal, embassy activity, public anger, faction appeals, and uncertainty about Soviet intent. Civilian-targeting text should be severe and direct without spectacle or cheap humour.
