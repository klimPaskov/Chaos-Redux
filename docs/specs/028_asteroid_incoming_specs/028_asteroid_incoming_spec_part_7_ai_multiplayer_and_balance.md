# Asteroid Incoming, Part 7: AI, Multiplayer, and Balance

## AI role

AI behavior should preserve the moral and strategic meaning of the opening choice. Most governments should prefer the miss. A hostile strike becomes plausible when the chooser faces an active enemy, an existential threat, extreme ideology, severe desperation, or very high Chaos.

The AI must never choose a target by random option position alone.

## Opening option model

The option pool is always the three locked targets plus miss. AI scoring should compare all four options under one complete pool.

### Miss preference

The miss receives a strong base preference. It becomes stronger when:

- The chooser is democratic or politically moderate
- The chooser has high stability and is not losing a war
- All three target countries are neutral, allied, guaranteed, subject, or faction-connected
- Global dust would seriously harm the chooser's own economy or supply
- Global Fragmentation is active
- The chooser is vulnerable to fragment damage
- The chooser controls extraordinary mineral sites that could be threatened by new fragment competition

The miss preference becomes weaker when:

- The chooser is near capitulation
- One target is an active major enemy
- One target is the main source of an existential world threat
- The chooser has extreme militarist or destructive strategy
- Chaos is high enough that normal restraint has already broken down
- The target's defeat would materially improve the chooser's survival

### Protected targets

AI should assign zero or near-zero strike weight to:

- Itself
- Subjects and overlords
- Faction members
- Active allies in the same war
- Countries it guarantees when the guarantee still represents a real commitment
- Countries under a nonaggression or special protected relationship that the project treats as binding

A rare high-Chaos betrayal route can relax some protection only when an existing AI strategy explicitly supports betrayal. The event should not invent that strategy on its own.

### Hostile target value

An AI target becomes more attractive when:

- The country is an active enemy
- The locked state is a capital, major industrial center, supply hub, or critical front network
- The enemy is stronger and difficult to defeat conventionally
- The enemy leads a hostile faction
- The enemy is an existential threat actor
- The enemy is heavily condemned or diplomatically isolated
- The chooser is already accepting severe global damage through its current strategy

The score should fall when:

- The impact rings would devastate friendly or allied neighboring states
- The chooser owns states inside the expected outer rings
- The target is about to capitulate without the strike
- The target is a weak minor whose destruction offers little strategic value
- Fragmentation makes self-harm likely and the chooser is already fragile

### Ideology and route character

Ideology should influence the base willingness without replacing world-state logic.

- Democratic AI should almost always miss unless the target is an existential active enemy and the chooser faces defeat.
- Nonaligned and ordinary authoritarian AI should prefer the miss but can strike a major enemy under severe pressure.
- Fascist and extreme militarist AI can strike more readily during war.
- Communist AI should depend on route strategy and war context, not a universal aggressive bias.
- Special destructive or apocalyptic AI can treat the strike as a normal weapon when its existing identity supports that behavior.

## Target-country emergency AI

The locked target selects one preparedness stance.

- Preserve command continuity when the capital is hit, stability is low, or government-dislocation risk is high.
- Disperse transport and stockpiles when trains, fuel, aircraft, or supply hubs are concentrated in the center.
- Prepare hospitals and shelters when outer-ring population and continuing casualty risk are high.

The AI should compare expected benefit. It should not use ideology as the main factor.

## Fragment and crater AI

### Fragment risk

The chooser cannot select fragment sites. AI willingness to cause fragmentation should account for its own exposed territory and global strategic position.

### Crater control

Under Extraordinary Minerals, AI should:

- Defend controlled crater access routes
- Repair supply to controlled sites
- Avoid abandoning a site in a routine state transfer
- Prefer taking a nearby enemy site when military strength and supply support the offensive
- Recognize that a main crater is more valuable than one fragment site
- Count several fragment sites when comparing strategic value
- Avoid suicidal offensives for a distant site during a losing home-front war

### Peace behavior

Crater states should carry increased strategic value in peace and transfer logic. The system should still respect normal cores, claims, occupation, faction leadership, and subject rules. A crater should not automatically override every political settlement.

## Recovery AI

AI recovery follows the priority order from Part 6. It must preserve reserve floors.

- Do not spend the last trains needed for national supply.
- Do not commit all support equipment during an active major war.
- Do not begin a long industrial restoration project when the state is about to be lost.
- Prefer medical response when continuing civilian losses remain high.
- Prefer rail and supply repair when the capital or front is disconnected.
- Prefer dust hardening when global penalties are materially reducing output.
- Contribute to global dust mitigation only after urgent national needs have a reserve.

## Multiplayer behavior

### One chooser

Only one human country receives the targeting event. The chooser is fixed when Event 028 enters the global transaction.

### Observer information

Other human players receive:

- A trajectory-locked notice after an impact is confirmed
- The impact super-event and global news
- Their own consolidated country report when damaged
- The close-passage news when the miss is selected

The locked notice should reveal the main target and impact date. Fragment locations remain unknown.

### Tag switching

Tag switching during the event does not transfer chooser authority. A player who switches into the target can still receive the target-country emergency event if the game's scope and current human control support it.

### Simultaneous timers

A global Event 028 transaction blocks another player's timer from starting another copy. The blocked timer should resume through the shared event-system behavior after the transaction finishes.

### Pausing and confirmation

The event should use the project's normal multiplayer pause and confirmation behavior. Confirmation should not create several days of mandatory blocking for every player.

## Balance anchors

### Main impact

The user-defined population percentages are fixed. Balance should use building ranges, recovery duration, target suitability, and dust scaling. The core losses remain unchanged.

### Miss

The miss should have no direct reward. Its value is avoided destruction, avoided dust, and preserved diplomacy. It also forgoes the chance to remove a rival and create extraordinary mineral sites.

### Fragmentation

Fragment count scales from three to six. Geographic validity can reduce the count. The event should report the reduction honestly.

### Minerals

The plus 100 and plus 20 armour values are fixed. Stacking remains uncapped. Balance review should inspect piercing thresholds, AI strategic value, and state-control churn.

### Dust

Dust should create a meaningful global cost without making every country unable to fight. National protection actions should reduce part of the penalty. The opening impact remains irreversible.

## Required probability scenarios

The AI probability audit must evaluate a complete four-option pool in named scenarios.

| Scenario ID | Chooser situation | Target mix | Expected ordering |
| --- | --- | --- | --- |
| `AST_AI_01` | Stable democratic major at peace | Three neutral or friendly targets | Miss dominates every strike option |
| `AST_AI_02` | Democratic major losing an existential war | One hostile major, two neutrals | Miss remains strong, hostile major is the only plausible strike |
| `AST_AI_03` | Fascist major in total war | One enemy faction leader, one weak enemy, one neutral | Enemy faction leader ranks first or close to miss, neutral remains near zero |
| `AST_AI_04` | Nonaligned minor at peace | Three unrelated majors | Miss strongly dominates |
| `AST_AI_05` | Destructive special actor | Three enemies | Best strategic enemy dominates miss when route identity supports use |
| `AST_AI_06` | Any ordinary country | One subject, one faction ally, one enemy | Subject and ally score zero, enemy competes with miss |
| `AST_AI_07` | Fragile chooser at 700 Chaos with fragmentation | One strong enemy | Fragmentation risk raises miss weight relative to the same 500-Chaos case |
| `AST_AI_08` | Near-capitulation chooser at 700 Chaos | One existential enemy | Enemy strike becomes materially more likely than in a stable case |
| `AST_AI_09` | Chooser controls several mineral sites | One distant enemy | Miss gains weight because new fragments can threaten the existing advantage |
| `AST_AI_10` | All three targets protected | Ally, guarantee, subject | Miss is effectively certain |

The audit should distinguish option score from normalized probability and should test sensitivity to ideology, war state, capitulation progress, target relations, and fragmentation.

## Recovery decision scenarios

Weighted recovery surfaces also need named tests.

- High preventable deaths and adequate equipment should prioritize mobile hospitals.
- Capital supply disconnection should prioritize the rail corridor.
- Active frontline collapse and low train reserve should block expensive reconstruction.
- Severe dust and strong industry should prioritize factory hardening.
- A controlled main crater under threat should prioritize perimeter security.
- A distant enemy fragment site should not override homeland defense.

## Anti-exploit rules

- The human cannot reopen the event to reroll targets.
- Canceling confirmation does not reroll.
- Save and reload does not reroll locked targets or fragments.
- State transfers during the two-day delay do not move the impact.
- A state receives one strongest damage profile.
- Deaths are recorded once per actual population transaction.
- Mineral modifiers are derived from current site control and cannot duplicate.
- Rapid controller switching does not repeat survey or security rewards.
- Recovery decisions cannot restore more buildings than the event destroyed.
- Global mitigation cannot be spammed by one country beyond its cap.
- A country cannot farm an achievement by giving a crater back and retaking it repeatedly.

## Performance rules

- Build target and ring lists only for the active Event 028 transaction.
- Do not add a recurring daily all-country scan.
- Dust stage changes should use monthly or event-driven updates.
- Crater bonuses should refresh from bounded control-change and lifecycle hooks.
- Country reports should be assembled after the transaction. The event must not create one report event per state.
- Fragment target selection should lock the full set before applying any state destruction.

## Manual and force-trigger validation

Force triggering can bypass normal major-event timing. It must keep target validity, transaction locking, and three-option construction.

Manual tests should include:

- Impact against a continental major
- Impact against a small multi-state country
- Capital impact
- Cross-border rings
- Target annexed during the delay
- Fragmentation with reduced valid fragment pool
- Overlapping outer fragment rings
- Miss at each Chaos tier
- Mineral control transferred through war and peace
- Save and reload during the two-day lock and during dust recovery
