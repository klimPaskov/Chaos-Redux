# AI behavior and probability handoff

## The opening objective

Ireland's war plan targets the northern objective and its approaches.
Assign only a supported number of divisions to the available front, keeping the rest in supplied Irish reserve locations.
Avoid naval invasions of Great Britain, unrelated expeditionary deployments, and distant offensives before the North is secure.
Maintain enough home defense to prevent the capital from falling while the northern attack is prepared.

Use supported AI strategy and focus-priority mechanisms, verified in the installed version.
A planning statement that the AI should prioritize the North is not evidence that it does.
The validation fixture must inspect actual target selection, staging, supply, and offensive conduct.
Do not freeze every unrelated military system or remove legitimate defensive responses to another enemy.
The narrow override ends at settlement, failure, or Ireland's invalidation.

The AI should select a paid preparation only when the cost leaves sufficient equipment and manpower to reinforce the actual opening army.
It may take the one-time extension when it is making progress and still has an affordable, credible offensive.
It should decline the extension when the government is collapsing or the force cannot continue.
These decisions use the same eligibility and payment helpers as a human.

## Postwar priorities

Immediately after victory, prioritize the constitutional mission, emergency-to-permanent army transition, and usable reconstruction.
A damaged North and a large unsupported army take precedence over another optional foreign commitment.
The AI must not leave the temporary logistics bonus to expire while refusing every sustainable army choice.
It should keep a real equipment reserve and account for active construction commitments.

The first strategic choice follows the campaign's actual opportunities.
Suggested relative starting scores are empire 30, federal 35, and primary Atlantic 35.
These are unnormalized tuning weights, not predicted percentages.
Increase imperial interest for a secure Irish government, sufficient army and naval preparation, and a plausible Scottish opportunity.
Increase federal interest for credible self-government policy, eligible friendly partners, and manageable commitments.
Increase Atlantic interest for strong ports, access opportunities, trading partners, and poor prospects for a continental or British-isles campaign.

Ideology influences compatible institutions and diplomatic acceptance, but must not be the only route selector.
A republic can pursue an empire, an authoritarian government can prioritize Atlantic defense, and Gaelic education is not locked to one ideology.
Mutual exclusions and prior commitments always override preference weights.

## Imperial behavior

Prepare transport, escorts, equipment, and logistics before opening a later Scottish campaign.
Honor the event-specific post-settlement interval.
Seek a negotiated relationship when a credible favorable settlement exists, but do not assume an independent Scotland always gives up sovereignty.
After acquisition, complete administration and control Strain before opening several additional targets.
Prioritize a reachable territorial objective and avoid serial declarations on every listed Celtic or Atlantic location.

At Strain 50 or above, prefer administration and consolidation.
At 75 or above, do not choose optional package expansion actions.
Ordinary self-defense remains active.
The AI should use client relationships where direct control would impose costs it cannot sustain.
An imperial AI must still meet the exact ownership and control requirement before proclamation.

## Federal behavior

Send offers to eligible useful partners and accept refusals without a rapid-repeat loop.
Support an actually endangered partner when the promised capacity is available.
Fund the charters only after Scotland and Wales can meet their territorial and sovereignty conditions.
When an essential member cannot be obtained, develop the useful league path and shared industry instead of sitting on an impossible federation focus forever.

Accepted shared procurement must have real contributors.
A country with missing equipment or insufficient factories chooses a smaller commitment or abstains.
Arbitration is preferred when it preserves a viable federation at an affordable cost.
A promised obligation that would destroy a member's defense can be rejected.
The AI may withdraw under clearly adverse conditions and the main system must handle that outcome.

## Atlantic behavior

Develop the chosen fleet doctrine, aircraft, ports, and merchant capacity as a coherent system.
Do not build a large submarine force and then treat it as the protected escort fleet required by a landing mission.
Prioritize repair and convoy replacement before a second expensive overseas circuit.
Seek alternative access candidates after a refusal and use the longer-range domestic alternative where appropriate.

The AI should not attack North America because it has completed a diaspora group.
Overseas diplomacy and strategic island access use actual target conditions.
Expansion is optional.
A strong defensive Atlantic posture is a legitimate final strategy.

## Holder and partner AI

The northern holder evaluates actual defense, threat, supply, and the wider war.
It can reinforce or conserve its force, but cannot veto a mechanically qualified settlement.
Optional postwar normalization uses relations and present circumstances.
An AI partner values sovereignty terms, domestic capacity, security benefit, ideology where relevant, and Ireland's record of honored promises.
Human responses are never replaced by those weights.

## Probability evaluation requirements

The supplied chaosx_ai_probability_auditor must begin with probability inspection during implementation.
Inspect entry points, conditions, relative scores, timing models, helper dependencies, and scenario inputs before evaluating results.
Use named evaluations and sweeps for normal 1936 Britain, a fortified late North, Ireland at several army strengths, partner refusals, missing essential tags, Strain boundaries, and all Evolution thresholds.

Use the verified game-version MTTH adapter for Evolution timing.
Use simulation only for declared uncertain inputs and keep exact, bounded, sampled, and unresolved results separate.
Compare before and after a patch.
No tool-backed probability work was performed in this planning environment.
The weights above must not be described as balanced or statistically verified.
