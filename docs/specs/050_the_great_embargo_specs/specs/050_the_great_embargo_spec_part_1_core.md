# Event 050: The Great Embargo

## Part 1: Core event design

All action names, stage names, outcome names, and asset names in this specification are working design labels. The implementation agent must write final player-facing text after reading the complete pack and the event writing rules.

## Catalog entry

- Event ID: `50`
- Event name: The Great Embargo
- Type: Minor Repeatable
- Status: To Be Reworked
- Chaos level: 1
- Cluster: Negative Economy
- Member severity: Medium

## Event promise

The Great Embargo creates a temporary international campaign to isolate one economically important country. The event asks whether the target can replace lost access, split the coalition, accept concessions, turn isolation into domestic mobilization, or seize what it can no longer buy.

The crisis must feel different for each target. A continental power with oil, steel, food, rail capacity, and friendly land routes can endure a high Pressure level with painful inefficiency. An island power that imports fuel and rubber can enter an immediate strategic emergency at the same Pressure. A weakened major may yield to several important partners. A powerful regime may use the embargo to justify autarky and war.

The target has agency from the opening day. Outside countries also make decisions when their trade capacity, rivalry, ideology, faction position, or location gives them a meaningful role. The event stays compact by assigning individual choices only to important participants and likely intermediaries.

## Opening incident

One valid player-controlled country or one valid major power is selected as the target. A convening country or small convening group announces a coordinated restriction campaign. The public justification is selected from current campaign facts where possible, then from a broad accusation pool when no strong fact exists.

The opening should immediately change the target's economic situation. Trade access narrows, replacement routes become uncertain, foreign military support becomes harder to secure, and import-dependent production begins to suffer. The target receives the Embargo Pressure value, the opening response category, one urgent replacement-supply mission, and a report that identifies the most important coalition members.

Outside countries do not all receive the same event. Core enforcers, large suppliers, major shipping states, faction partners, and plausible neutral intermediaries receive roles suited to their position. Minor countries with no meaningful economic or diplomatic connection can join the background coalition without receiving a personal event.

## Target selection

### Eligible targets

The normal pool contains:

- each valid player-controlled country that uses ordinary civilian, trade, production, and diplomacy systems
- each valid major power that uses those systems

Player countries remain eligible when they are not majors. A country targeted by an active Event 50 crisis is excluded until that crisis resolves. A country can be selected again in a later firing after all crisis-owned state has been cleared.

### Exclusions

The target pool excludes:

- countries classified as special Chaos actors when ordinary economic isolation would not make sense
- countries classified as actually nonhuman
- countries that do not use normal civilian systems
- countries without a viable government or usable economic base
- capitulated countries whose remaining condition cannot support an independent crisis
- countries already scheduled as another target in the same Evolution II firing
- temporary system carriers and other non-playable administrative actors

The shared classifiers in `chaosx_dynamic_triggers` should govern the broad civilian and special-country exclusions. Event 50 should own only its crisis-specific validity rules.

### Target class balance

The default selection should give the player a substantial chance to experience the event without making every repeat player-focused. A reasonable starting direction is a target-class roll near forty percent player and sixty percent major when both pools exist. The implementation agent may tune the final ratio through centralized constants after probability inspection.

When no valid player exists, the event selects a valid major. When no valid major exists, it selects a valid player. When neither pool exists, Event 50 is unavailable for that firing.

In multiplayer, the target-class roll treats player countries as one pool. It should not scale linearly with the number of players and turn a large lobby into a near-guaranteed player target every time. At most one player country should be selected by one ordinary firing. Evolution II may target more than one player only under an explicit multiplayer mode or a deliberately tuned high-chaos rule.

## Public justification families

The justification shapes coalition membership, concessions, outside reactions, and text. It does not create a second public meter.

### Aggression and territorial expansion

This reason fits a target that recently started wars, annexed land, violated guarantees, or expanded through coercion. Rivals, threatened neighbors, democratic countries, and members of opposing factions become more willing to join. Concessions focus on withdrawal, guarantees, demilitarization, or limits on further claims.

### Ideological hostility

This reason fits a target whose ideology creates broad fear or hostility among important powers. Ideological allies may resist the embargo even when trade would benefit them. Concessions focus on party activity, foreign agitation, alignment, or support for movements abroad.

### Condemnation and public outrage

This reason can draw on existing public Condemnation or a separately established scandal. Event 50 does not create hidden atrocity evidence and does not expose Condemnation sources that are still secret. Public condemnation can strengthen coalition recruitment and reduce the chance that friendly states openly defect.

### Trade conflict and nationalization

This reason fits resource seizures, broken commercial arrangements, debt disputes, expropriation, licensing conflicts, or sudden market exclusion. Commercially exposed countries become more important than ideological partners. Concessions focus on compensation, preferred contracts, restored access, or debt settlement.

### Treaty breach or diplomatic crisis

This reason fits a visible breach of a pact, guarantee, access agreement, inspection arrangement, or other current obligation. Coalition cohesion is high when the target plainly violated a shared commitment. Concessions focus on restoring the agreement or accepting monitoring.

### Broad accusation

When the campaign state supplies no strong reason, the coalition can form around accusations, diplomatic hostility, alleged interference, or an international consensus that the target has become unacceptable. This family should retain uncertainty. The event should not fabricate specific crimes or present an unsupported allegation as confirmed fact.

## Coalition construction

The opening coalition is built from roles, not a single undifferentiated list.

- One convenor gives the coalition a diplomatic center and usually has the greatest influence over settlement terms.
- Two to five core enforcers supply most of the pressure through economic size, resources, shipping, finance, proximity, or alliance leadership.
- Four to twelve compliance partners add breadth, diplomatic isolation, and secondary enforcement.
- Two to six pressured neutrals begin outside the coalition and form the first pool for intermediary or defection play.
- A wider background layer can be represented collectively when many small countries comply without requiring personal event chains.

Coalition strength must depend on who participates. A bloc containing the target's principal oil supplier, major ports, and nearby land routes can be stronger than a larger group of distant countries with little relevant trade.

## Baseline lifecycle

### Phase 1: Shock

The coalition is announced, Pressure is established, and the target sees its immediate exposure. The opening mission asks the target to secure a replacement supply path before the crisis reaches a critical stage. Core participants receive their opening commitment choices.

This phase should be short enough that the player understands the crisis before the first monthly review. It must still give time to inspect the category, identify the most urgent shortage, and choose an initial response.

### Phase 2: Adaptation

The target begins self-sufficiency projects, smuggling, intermediary negotiations, concessions, or defiance. The coalition tests enforcement and negotiates with neutrals. Pressure can rise or fall in meaningful steps.

The target should start forming a recognizable strategy during this phase. It can combine compatible actions, but cannot pursue every response at full strength without costs or contradictions.

### Phase 3: Coalition fracture or consolidation

After several review cycles, the coalition develops internal conflicts. Hardliners demand stronger enforcement. Commercial opportunists profit from leakage. Friendly participants seek concessions that let them leave. Neutrals decide whether the risk of secondary pressure outweighs the gains from trade.

A target that has created replacement supply can begin attacking coalition unity. A target that has failed to adapt faces severe economic consequences and may consider resource seizure.

### Phase 4: Resolution

The crisis ends through coalition collapse, negotiated settlement, political fatigue, successful endurance, target defeat, target invalidation, or military escalation that changes the nature of the crisis. The event applies one bounded aftermath package, records the outcome, clears its ledgers, and restores future eligibility.

## Baseline player loop

The target repeatedly answers three practical questions:

1. Which shortage or foreign dependency can become strategically dangerous first?
2. Should the country reduce its real dependence, lower Pressure through diplomacy, or accept isolation and change its political economy?
3. Which coalition member or neutral route offers the best chance to break international unity?

A useful action must move at least one part of this loop. It should secure real supply, reduce the effective damage of Pressure, change coalition membership, open a negotiated exit, create a temporary mobilization path, or prepare an aggressive response.

The category should not become a shop for small modifiers. Every visible action needs a cost, duration, target, risk, objective, or lasting concession that changes the target's next decision.

## Resolution families

### Coalition collapse

Pressure remains in the collapsing band across more than one review, core participants leave, or enforcement becomes too weak to sustain the embargo. The target keeps concessions already made and investments already completed. It gains a bounded political and diplomatic outcome reflecting a successful break in international unity.

### Negotiated settlement

The target satisfies a settlement package accepted by the convenor and enough core members. The embargo lifts in an orderly way. The target avoids the harshest long-term damage, but concessions remain visible through treaties, access, opinion, claims restraint, or temporary policy obligations.

### Political fatigue

The coalition fails to maintain support until the dynamic duration expires. This route is common when Pressure becomes porous and no side can force a decisive result. The target emerges weakened, participants retain memory of the confrontation, and some trade relations recover slowly.

### Defiant endurance

The target survives a long period of severe isolation without conceding or collapsing. It can retain part of its emergency mobilization and self-sufficiency gains. It also receives an exhaustion cost and may remain diplomatically isolated after formal restrictions end.

### Resource-access escalation

The target issues demands or starts a war to secure strategic resources. Event 50 records the crisis origin and shifts its economic layer into an escalation state. Ordinary war, annexation, occupation, Deaths, and Chaos systems own the resulting conflict. The embargo can remain active during the war or close into a hardened wartime blockade according to the final implementation design.

### Target defeat or invalidation

Capitulation, annexation, civil war replacement, loss of a viable economic base, or transformation into an excluded actor must close or transfer the crisis safely. Transfer is allowed only when the successor clearly inherits the same government and obligations. Ambiguous succession ends the old crisis and permits a later fresh firing.

## Repeatability

Every later firing is a new international crisis.

It does not inherit:

- the former target
- the former coalition
- former Pressure
- former duration
- former intermediary routes
- former secondary-sanction marks
- former decision progress
- former settlement demands
- former coalition fatigue

Long-term consequences that logically outlive a crisis remain. Examples include domestic extraction already built, a treaty concession that still has a duration, a damaged diplomatic relationship, or an achievement flag. Event-owned crisis state must be removed completely.

## Replay identity

Repeatability comes from changing world conditions, not random flavor alone. Different firings should vary through:

- target dependence and resource profile
- coalition composition
- public justification
- current wars and factions
- available neutral routes
- world shipping and land access
- target ideology and legitimacy
- current Chaos tier and active evolutions
- existing economic events
- human decisions by outside players

A repeated firing against the same country should still feel different when its economy, allies, borders, resources, and political position have changed.
