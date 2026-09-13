# Event 067 Generalissimo

## Accepted catalog identity

- Event ID: `067`
- Event name: Generalissimo
- Type: Minor Fire-Once
- Status before implementation: To Be Reworked
- Minimum Chaos level: 1
- Cluster: Military Preparation
- Cluster role: High member

## Playable promise

A country receives a commander who is so effective that refusing to use him feels wasteful. He begins as a loyal military asset and can remain that way while global Chaos is low. Once the world becomes unstable enough, battlefield success and formal authority give him political weight. The government can keep using him, contain him, remove him, submit to him, or fight the army he has built around himself.

The event must preserve the following tension throughout its normal lifecycle:

- The Generalissimo is worth using even when the player understands the risk.
- Avoiding all risk requires giving up a large military advantage.
- Political danger grows from military use and institutional concessions.
- Countermeasures impose real military, political, industrial, or logistical costs.
- A coup is avoidable through competent management.
- A failed arrest, capture, or assassination creates an immediate revolt.
- High influence produces a stronger junta, but the government can weaken the network before acting.
- A victorious Generalissimo remains the country's ruler, general, and field marshal.

The event must not become an unavoidable timer that punishes the player for receiving a strong commander. A player who manages authority, limits the officer network, accepts temporary military inefficiency, and reacts to demands should be able to keep influence below the final threshold for a long period.

## Target selection

The event selects one valid country from two eligible classes:

- player-controlled countries
- major countries

The initial implementation should use a class-weighted selection so a player country has a meaningful chance to receive the event without guaranteeing it. The default balance target is that the player class receives a modest majority of the class roll when at least one valid player and one valid major exist. Countries inside the selected class are then weighted by current conditions.

Positive target factors should include:

- player control
- active war
- an unfavorable or uncertain war situation
- a large army
- high military spending or military factory count
- an active military preparation state
- a recent loss of important territory
- a shortage of skilled commanders relative to army size

Negative or blocking factors should include:

- an existing Event 067 crisis or resolved Event 067 history
- an active civil war
- capitulation
- no controlled core territory
- too little territory to create a valid two-sided civil war if the crisis later escalates
- classification as an actual nonhuman country
- an event-owned actor whose systems cannot use ordinary commanders or civilian politics
- a temporary country that cannot retain a commander and country package
- a current world-end state

The event is unavailable when no valid target exists. The Events list must show the ordinary unavailable state instead of queuing the event against an invalid scope.

### Target weighting requirements

The target weighting is a probability-bearing surface. The implementation must route it through the named scenarios in `handoffs/067_generalissimo_probability_scenario_matrix.md` and through `chaosx_ai_probability_auditor`.

The weighting must satisfy these qualitative rules:

- A losing player country at war should normally outrank a peaceful stable major.
- A valid major remains possible when valid player countries exist.
- A special Chaos country or actual nonhuman country receives zero weight.
- An active civil-war country receives zero weight.
- A sole valid target receives the complete normalized probability.
- Multiplayer does not create one Generalissimo per player. The normal event still creates one worldwide character.

## Initial manifestation

The target receives the Generalissimo immediately. He is a newly created character owned by Event 067 and does not replace, upgrade, rename, or absorb an existing commander.

The initial event should establish these public facts:

- the man has appeared with complete military credentials that nobody can verify
- senior officers accept his competence after direct observation
- he can assume field command at once
- his origin remains uncertain
- he makes no political demand at baseline
- the government has not yet transferred constitutional or political authority to him

The event should avoid explaining whether his ability is supernatural, engineered, fraudulent, prophetic, or connected to another event. The mystery should remain unresolved unless a later event connection explicitly earns an answer.

## Baseline military package

The Generalissimo receives the maximum useful commander package that the current game version permits.

Required capabilities include:

- maximum supported commander level
- maximum supported Attack
- maximum supported Defense
- maximum supported Planning
- maximum supported Logistics
- every positive applicable general trait
- every positive applicable field marshal trait
- every positive Chaos Redux commander trait that is safe and applicable
- maximum useful army-group or command capacity
- the largest supported army command without ordinary over-command penalties where the engine allows it
- immunity from ordinary negative commander-trait drift that would undermine the event premise
- continued availability for direct command after he becomes country leader

There is no balance target that compares him with ordinary commanders. He is supposed to exceed them decisively.

### One-character rule

The implementation must use one canonical character token. It must not create one general, one field marshal, and one ruler as separate people with the same portrait and name.

If the engine represents promotion to field marshal as one role that retains general traits, that one field marshal role satisfies the commander side of the design. The character must still be able to command armies directly and retain all applicable traits.

If the engine cannot keep the same character as country leader and active army leader, that is an implementation blocker. The implementation agent must document the exact engine limitation and obtain a design decision before using linked duplicate characters.

## Baseline command use

The Generalissimo can be assigned through the normal command interface. The event should not force the player to place divisions under him.

Political credit is tracked through formal command authority and campaign outcomes because exact attribution of every battle to one commander may not be available to script. The event therefore uses an event-owned command mandate state:

1. Advisory Reserve
2. Theater Command
3. National Field Command
4. Supreme Command

These are qualitative authority states, not extra public meters. The current state appears in the crisis category and tooltips.

At initial firing, the Generalissimo begins at Theater Command. The government can expand or restrict his mandate when the relevant crisis stage is active.

## Hidden pre-evolution service record

Before Evolution I, the event tracks a bounded hidden service record. It records meaningful use without exposing political danger during the loyal phase.

The service record can increase through:

- formal expansion of his command mandate
- a hostile major's capitulation while he holds national command
- recapture of the host capital or another critical state while he holds national command
- holding the host capital through a serious enemy threat
- capture of an enemy capital or high-value strategic state
- completion of an Event 067 campaign mission
- a major reduction in a losing war's danger while he holds national command

It can fall through:

- prolonged reserve status
- a serious defeat while he holds national command
- loss of the capital or a major command region
- government action that publicly limits his responsibility

The hidden record is capped. When Evolution I activates, only a bounded share converts into Generalissimo Influence. Early military use therefore matters, but a successful pre-evolution campaign cannot produce an instant ultimatum.

## Event pacing and evolution entry

The three evolutions are separate from ordinary stage progression. Evolution activation gives zero Chaos.

### Evolution I entry

Evolution I becomes eligible when:

- global Chaos is at least 200
- the Generalissimo is alive and still present
- the crisis has not been permanently resolved
- Evolution I is enabled

The normal active-event pacing target is about 90 days, modified by service record, war, public prestige, command mandate, stability, and recent military outcomes.

If Event 067 first fires at 200 or higher Chaos, Evolution I may be active at opening. The Generalissimo still begins without an immediate revolt. The first formal demand should arrive after a short bounded delay.

### Evolution II entry

Evolution II becomes eligible when:

- global Chaos is at least 400
- Evolution I is active
- the Generalissimo remains present
- influence or the hidden officer network has reached the required threshold
- Evolution II is enabled

The normal pacing target is about 120 days. A country that has granted Supreme Command, accepted several demands, and allowed influence to rise should progress faster. A country that has restricted him and weakened his network should progress slower or remain below the entry condition.

If Event 067 first fires at 400 or higher Chaos, the opening can include an established officer following and visible Influence. The opening must not skip the player's first meaningful management window.

### Evolution III entry

Evolution III becomes eligible when:

- global Chaos is at least 600
- Evolution II is active
- the Generalissimo remains present
- influence has reached the high threshold
- Evolution III is enabled

The normal pacing target is about 90 days. When Evolution III activates at maximum influence, the ultimatum should follow after a short visible interval. Evolution activation itself does not start the revolt.

If Event 067 first fires at 600 or higher Chaos, the event begins as a mature crisis with Evolutions I and II active. Evolution III remains paced unless the manual scenario explicitly starts at the ultimatum.

## Disabled evolution behavior

- If Evolution I is disabled, the Generalissimo remains a loyal military asset and no political crisis begins.
- If Evolution II is disabled, military demands and Generalissimo Influence remain active, but the state-wide network and expanded political demands never unlock.
- If Evolution III is disabled, no final ultimatum occurs. The player can retain, contain, or remove him through the earlier system.
- Disabled evolutions must not set recorded flags or unlock later content indirectly.
- The triggerable scenario may create a mature crisis through a tightly scoped scenario launch bypass. That bypass is cleared when setup finishes.

## Normal end states

### Permanent removal

A successful dismissal, retirement agreement, arrest, capture, or assassination removes the Generalissimo permanently and closes the crisis.

The exact aftermath depends on the method. A peaceful retirement causes less damage than an assassination or officer purge. Every successful method ends Generalissimo Influence and prevents the normal Event 067 coup path.

### Managed coexistence

The government can keep him indefinitely if influence remains below the ultimatum threshold or Evolution III is disabled. This is a real outcome, not a temporary delay before an unavoidable coup.

### Peaceful submission

The government accepts his final demand. The country becomes a military junta without a civil war, receives the Generalissimo focus tree, and transfers the character into the ruler role while keeping him available for command.

### Military revolt

A failed arrest, capture, or assassination, a failed final removal attempt, or refusal of the final ultimatum starts an immediate revolt. The Generalissimo creates a dedicated military-junta side and becomes its ruler and active field commander.

### Government victory

The government defeats the junta. The Generalissimo is permanently removed, the officer network is dismantled or reconciled, and the host receives a difficult military-reform aftermath.

### Junta victory

The Generalissimo reunifies the host country under military rule. He retains his complete commander package, all dedicated ruler traits, and the full dedicated focus tree.

## Cluster behavior

Event 067 is a High member of Military Preparation.

When selected through a cluster firing:

- the event still creates only one Generalissimo
- the target validity gate still applies
- an invalid target causes a documented member skip
- the event applies its own fire-once history and weight behavior
- the cluster counts as one global pacing event
- Event 067 does not add a second timer transaction
- its event history and Event Details remain available as normal

The current supplied catalog exports do not contain the accepted cluster assignment. The authoritative workbook and runtime cluster registry must be reconciled during implementation.

## Scope limits

The following additions are outside the event's accepted design:

- a custom Generalissimo combat unit
- a custom equipment archetype
- a 3D character model
- a new doctrine or technology tree
- a full-screen crisis GUI
- several simultaneous Generalissimos during the normal event
- a fixed worldwide coup timer that ignores influence
- an automatic civil war simply because Evolution III is active
- a grounded historical person used as the Generalissimo
- duplicate character tokens for commander and ruler roles
