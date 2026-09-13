# Damage Control, Networks, and Recovery

## Decision category role

The Intelligence Compromise category is the target's main control surface. The name is a working label and should receive final localisation during implementation.

The category uses an ordinary decision presentation with a static category picture and concise dynamic header text. It does not need a separate mechanic window because the player manages one visible value, several archive domains, and a small current action set.

The category should always answer:

- how exposed the country remains
- which archive domains matter most
- whether personnel face immediate danger
- which actions can shorten the incident
- what operational sacrifice each action requires
- whether the country is ready to attempt deception

The category exposes three to five primary actions in a phase. It supports one to three active missions. Obsolete decisions disappear when their domain, phase, or target no longer exists.

## Cost philosophy

Damage control should consume resources that fit the action and should impose real operational tradeoffs.

Political Power can appear when a response is genuinely political or bureaucratic. It should not carry the category by itself.

Useful costs and sacrifices include:

- command power
- army, navy, or air experience
- support equipment
- civilian factory commitment
- operative or agency capacity
- lost network strength
- cancelled operations
- temporary planning disruption
- temporary research or administrative disruption
- tied-down formations during a deception mission
- diplomatic access to a trusted partner
- time

Each action can use at most four spendable cost types. Requirements and risks remain distinct from costs.

The strongest emergency actions should reduce Exposure substantially, but they should also create a short-lived weakness or destroy part of the target's own intelligence position. The player is choosing which damage is acceptable.

## Emergency action family

### Replace Codes and Authentication Tables

This action responds to compromised cryptologic material, security procedures, command authentication, or communications schedules.

It should be available when the cryptologic domain is active, when Exposure is Severe or Critical, or when a foreign exploiter has authenticated the archive through communications evidence.

The action uses command power and support equipment as its main costs. The amount scales with the target's size, war state, army, and exposed domain depth. A major at war pays more than a small player country at peace.

The action produces:

- a large Exposure reduction when cryptologic material is active
- a smaller general Exposure reduction when used as a broad emergency measure
- a sharp reduction in foreign confidence in communications-derived files
- lower Personnel Risk for contacts whose authentication methods were exposed
- a temporary command-friction or coordination penalty while the new system enters use

The temporary disruption is important. A player under attack can still replace codes, but doing so during a battle has a real cost.

The action cannot be repeated without a new code compromise or evolved second tranche.

### Recall Exposed Personnel

This action withdraws operatives, couriers, liaison officers, radio contacts, and other personnel whose identities or methods may appear in the archive.

It appears when Personnel Risk is meaningful. With agency mechanics available, it can target exposed operatives, active operations, or vulnerable networks. Without those mechanics, it represents a broader security recall and protects the base event from severe personnel consequences.

Its primary costs are operational:

- operatives become unavailable or return home
- active operations can be delayed or cancelled
- network strength can fall
- foreign access can be lost
- liaison channels can close temporarily

The action produces:

- a strong reduction in Personnel Risk
- a moderate Exposure reduction when agent registries or operational diaries are active
- protection against capture or burned-cover outcomes
- a later need to rebuild cover identities and networks

The decision must state which operations or network assets are at risk before the player commits. It should not silently cancel unrelated activity.

### Rewrite Compromised Plans

This action changes the military plan that foreign governments have studied.

It should use one visible action with dynamic domain targeting. The tooltip names the most exposed relevant military domain. When several military domains are active, the player receives a compact follow-up choice or another established target-selection method that does not open a permanent interface.

The variants are:

- land replan
- naval replan
- air replan
- mobilization replan

The action uses the relevant experience type and imposes a temporary readiness loss in the same domain. A land replan can reduce planning or coordination while commanders issue new orders. A naval replan can disrupt patrol efficiency and basing. An air replan can reduce mission efficiency during relocation. A mobilization replan can slow reinforcement or training during the transition.

The action produces:

- a substantial Exposure reduction in the selected domain
- reduced future named exploitation in that domain
- lower Reliance among recipients whose observations no longer match the archive
- a stronger foundation for a later false plan

The action can be taken again only when another domain remains compromised or a later tranche reopens the problem.

### Shut Down Vulnerable Channels

This action closes compromised networks, routes, dead drops, liaison links, and communication channels.

It is the safest immediate option for a weak service and the harshest option for the target's own intelligence reach.

Its costs are the network and operations that the country deliberately abandons. It can:

- reduce network strength
- cancel or block ongoing operations
- remove foreign access in one region
- break a liaison arrangement
- impose a short intelligence-recovery delay

It produces:

- a strong Personnel Risk reduction
- a moderate Exposure reduction
- protection against the most severe network exploitation
- less information about which foreign recipients are relying on the archive

A strong agency may prefer a more selective response. A weak agency should often choose this action because it cannot safely preserve every channel.

## Reconstruction action family

### Rebuild Cover Identities

This action replaces documents, safe houses, legends, contacts, and administrative records used to protect personnel.

It becomes available after Recall Exposed Personnel, Shut Down Vulnerable Channels, a burned-cover outcome, or a Deep Files tranche that includes identities.

It uses a temporary civilian factory burden, support equipment, and time. The exact package scales with the number of affected personnel and the target's industrial capacity.

It produces:

- restored Personnel Risk protection
- faster operative recovery where supported
- partial restoration of lost foreign access
- a small Exposure reduction because old identities become useless
- stronger resistance to the next network exploitation attempt

The action is not a free reversal of a lost operation. It rebuilds capacity for future work.

### Reconstitute Foreign Networks

This action rebuilds intelligence networks abandoned or damaged during containment.

It belongs primarily to the agency-enabled path. It should not appear in the base-game-only path when there is no network surface to restore.

It uses operative time and agency capacity. It can ask the player to choose which region or operation family receives priority when several networks were damaged.

It produces:

- gradual restoration of network strength
- renewed foreign access
- removal of an incident-specific reconstruction penalty
- improved ability to identify named exploiters

The action should not restore every network instantly. A country that saved its personnel by closing everything accepts a longer rebuilding phase.

### Compartmentalize the Archive

This action changes how the target stores and distributes classified information.

It is a lasting resilience investment. It uses civilian factory capacity, administrative time, and a temporary research or coordination burden. It should be expensive enough that a country under immediate attack may postpone it.

The action produces:

- a bounded permanent or long-lived resilience record
- lower initial Exposure on a later Event 52 incident
- reduced chance that one future leak includes every sensitive domain
- faster identification of which office or route was compromised
- improved resistance to Deep Files personnel exposure

The resilience has a cap. Repeated Event 52 incidents should not let a country reduce future openings to zero.

The action does not change current Exposure by a large amount because reorganizing archives cannot make already distributed files disappear.

### Restore Trusted Liaison Channels

This action repairs intelligence sharing with one friendly government after the target has closed or distrusted foreign links.

It requires a valid friendly country and enough relations or faction trust. The selected partner must not be a current hostile named exploiter.

It can use agency capacity, diplomatic effort, and a small industrial or support-equipment burden for secure communications.

It produces:

- a friendly sample or report about circulating files
- identification of one domain or named exploiter
- lower diplomatic uncertainty with the partner
- faster recovery of a damaged liaison route
- a small Exposure reduction when the partner destroys or quarantines its copy

The action should not force every ally to surrender the archive. It creates one credible cooperative channel.

## Incident missions

### Archive Freshness

Archive Freshness is the main incident timer.

Its duration is dynamic. The ordinary band is roughly 120 to 240 days. Deep Files and severe Total Compromise profiles extend it. Strong initial compartmentation, peace, and rapid first action shorten it.

The mission communicates that the archive will eventually become obsolete. It should also make clear that passive waiting leaves foreign governments with more time to exploit it.

Mission completion closes the remaining special exposure after final processing. It does not undo real consequences already suffered.

### Personnel at Risk

Personnel at Risk appears when the archive includes agent registries, contact chains, cryptologic procedures, or operational diaries and the hidden risk exceeds a meaningful threshold.

The ordinary duration is 60 to 100 days.

The player can resolve it by completing one or more valid protective actions, such as:

- Recall Exposed Personnel
- Shut Down Vulnerable Channels
- Replace Codes and Authentication Tables
- reduce Exposure below the dangerous threshold
- complete a targeted cover rebuild when the mission begins later in the incident

Success prevents or sharply reduces the next severe personnel outcome.

Partial success can save personnel while sacrificing a network or operation.

Failure triggers one bounded severe result based on actual exposed assets. It should not roll against every operative at once.

### Emergency Replan

Emergency Replan appears when the target is at war or faces a credible imminent invasion and land, naval, air, or mobilization files are active.

The ordinary duration is 75 to 135 days.

The mission asks the player to change the relevant plan through the Rewrite Compromised Plans action or through a domain-specific objective. A land objective can require moving a meaningful share of ready divisions away from an exposed concentration. A naval objective can require rebasing the relevant fleet. An air objective can require relocating a meaningful air group. The objective must use named or clearly highlighted targets and avoid arbitrary busywork.

Success reduces Exposure and weakens one named exploiter.

Failure gives a hostile relevant exploiter a stronger opening advantage if war begins or continues.

### Deception Window

Deception Window begins after Poison the Leak or a staged false deployment.

The ordinary duration is 90 to 150 days.

The player must maintain the selected deception long enough for one or more reliant recipients to act. The mission can require tied-down divisions, a fleet in a misleading port, aircraft based in a false priority region, or continued transmission of false orders.

Success creates domain-specific foreign mistakes.

Partial success affects only some recipients or produces a weaker penalty.

Failure can expose the deception, extend Exposure, or disrupt the target's own plan.

## Operative and network compromise

Agency-enabled incidents should evaluate active networks and operatives through bounded risk checks.

The risk model considers:

- current Exposure
- Archive Depth
- active personnel domains
- target counterintelligence
- target cryptology
- operative traits or current assignment where safely available
- network strength
- operation sensitivity
- whether the target already changed codes
- whether the target ignored Personnel at Risk
- foreign named-exploiter service quality

A powerful intelligence service should protect more people and recover faster. It should not become immune.

The outcome ladder is:

1. Suspicion or a temporary efficiency loss
2. Network strength loss
3. Operation delay
4. Operation cancellation
5. Burned cover and forced recall
6. Capture or wounding at the highest risk

The event should prefer lower outcomes unless several danger factors align. Capture is a serious incident result and should be limited per target and sequence.

A country with several operatives should not receive a cascade of simultaneous capture rolls. One severe personnel outcome can occur per Personnel at Risk failure, with another possible only under Deep Files or Total Compromise after a new proven exposure tranche.

## Base-game intelligence path

The event must remain complete without full agency mechanics.

The base path uses:

- reversible civilian, army, navy, and air intelligence exposure
- temporary military planning and industrial knowledge effects
- diplomatic and political exploitation
- generic personnel-security pressure
- code replacement
- military replanning
- channel shutdown
- archive compartmentation
- deception and false-plan outcomes

Agency content adds networks, operations, operative identities, cryptology depth, liaison rebuilding, and richer foreign exploitation. The event should not show empty decisions or broken tooltips when those surfaces are unavailable.

## Recovery quality

The end state should reflect how the target handled the crisis.

### Controlled recovery

The target lowers Exposure before major exploitation succeeds, protects personnel, and completes at least one lasting reform.

This can grant a bounded resilience memory and a positive closing report.

### Expensive recovery

The target neutralizes the archive but loses networks, cancels operations, or accepts major readiness disruption.

The incident ends safely, yet the cost remains visible.

### Passive expiry

The target waits for the archive to age.

Exposure closes at the end of the mission, but named exploiters receive more chances and no lasting resilience is earned.

### Failed recovery

The target suffers severe exploitation, personnel loss, or a deception failure before the archive expires.

The incident still ends. The event does not trap the country in a permanent crisis. Real losses remain.

## Cleanup expectations

Every temporary incident state must clear through one owner-controlled cleanup path.

Cleanup must cover:

- Exposure
- archive domains
- depth and confidence
- broad foreign intelligence advantages
- named exploiters
- recipient Reliance
- personnel-risk records
- decisions and missions
- target penalties
- deception flags
- selected false-plan targets
- temporary partner records
- incident timers
- sequence targets and arrays

Invalid countries must be removed during the incident without breaking other participants. Total Compromise cleanup should close each target separately and close the sequence only after every target has resolved.
