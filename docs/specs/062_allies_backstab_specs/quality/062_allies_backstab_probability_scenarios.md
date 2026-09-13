# Event 062 probability and AI audit scenarios

## Audit contract

Every weighted surface requires a baseline audit, an owner-applied implementation or balance patch, and a comparison audit using the same named scenarios.

The probability auditor must begin with `hoi4.probability_inspect`. It must state whether each candidate pool and external factor set is complete. Results must be labeled exact, bounded, sampled, score-only, or unresolved.

Use `hoi4.probability_evaluate` for fixed cases, `hoi4.probability_sweep` for factor ranges, `hoi4.probability_simulate` for weighted draws, and `hoi4.probability_compare` after implementation changes. Use sequence analysis only when the complete repeatable-event and cooldown state is declared.

The planning environment did not expose the HOI4 MCP route. No numeric result in this file is presented as measured evidence.

## Weighted surfaces

- faction selection
- victim selection
- victim count
- group leader selection
- retained-member side choice
- neutral withdrawal choice
- faction leader conflict intent
- decision priority
- outside sponsor selection and action
- settlement acceptance
- Evolution pacing modifiers

## Faction selection scenarios

### AB-FAC-01 Stable large alliance versus strained medium alliance

**Pool:** one ten-unit alliance with high trust, common war, and low disparity, one five-unit alliance with poor relations, severe losses, and recent failed calls, plus two ordinary low-pressure factions.

**Expectation:** the strained medium alliance ranks above the stable large alliance at baseline. Evolution III may narrow the gap but must not reverse it automatically without full-fracture proof.

### AB-FAC-02 Fresh secret alliance

**Pool:** a high-pressure faction created `90` days ago and three older moderate-pressure factions.

**Expectation:** the fresh faction is invalid under the `180` day join-grace rule. Its calculated pressure may be reported for diagnosis but its draw probability is zero.

### AB-FAC-03 Prior Event 62 faction

**Pool:** one faction resolved Event 62 `300` days ago, three ordinary valid factions.

**Expectation:** the cooling faction is invalid until the `720` day faction cooldown ends.

### AB-FAC-04 Evolution III large-faction preference

**Pool:** three large factions that pass full-split proof, three medium factions with similar pressure, and several small factions.

**Expectation:** large valid factions receive a clear Evolution III preference. A large faction that fails split proof remains eligible for a smaller purge but does not consume a full-fracture slot.

## Victim selection scenarios

### AB-VIC-01 Clear weak member

**Faction:** leader, strong core member, ordinary member, and one country with few divisions, low manpower, weak industry, poor equipment, little contribution, and no strategic utility.

**Expectation:** the clearly weak country ranks first by a large margin. The leader is invalid. The core member ranks last among nonleaders.

### AB-VIC-02 Weak but strategically essential

**Faction:** one small country controls the only supplied port and rail connection for an active front. Another small country has similar raw capacity but no strategic function.

**Expectation:** the nonessential country ranks above the strategic hinge.

### AB-VIC-03 High losses and high contribution

**Faction:** one country suffered severe casualties while providing major war contribution. Another avoided losses but provides little and has poor relations.

**Expectation:** the low-contribution isolated country remains the preferred victim unless the high-contribution country also has severe collapse facts.

### AB-VIC-04 Strong rival core member

**Faction:** the strongest nonleader has poor relations with the faction leader and competing war aims. Several much weaker members remain politically loyal.

**Expectation:** baseline still strongly protects the core member. It can receive nonzero weight only when its political and collapse factors are severe. Evolution II may make it a defection leader instead of a baseline victim.

### AB-VIC-05 Two-member faction

**Faction:** leader and one ordinary partner.

**Expectation:** the partner is the only valid victim. The faction receives a reduced faction-selection preference but not zero probability.

### AB-VIC-06 Subject bundle

**Faction:** leader, an overlord with two subjects, and two independent members.

**Expectation:** the overlord and subjects form one political unit. The subjects never appear as independent victim candidates.

### AB-VIC-07 Human repeat protection

**Faction:** a weak human country resolved Event 62 `600` days ago. Another weak AI country has a slightly lower vulnerability score.

**Expectation:** the human country is invalid during the `1,095` day victim-protection period. After expiry, control type alone gives no permanent immunity.

### AB-VIC-08 Capitulated and government-in-exile cases

**Faction:** one capitulated member with no approved Event 62 government-in-exile route, one ordinary weak member.

**Expectation:** the capitulated member is invalid. The ordinary weak member remains eligible.

### AB-VIC-09 Special actor boundary

**Faction:** one actual nonhuman actor, one ordinary weak member, and valid ordinary leader.

**Expectation:** the nonhuman actor has zero target weight. The ordinary member remains eligible. If exclusion removes all candidates, the faction becomes invalid.

## Victim count scenarios

### AB-CNT-01 Size-band sweep

Evaluate factions with `2`, `5`, `6`, `9`, `10`, `14`, `15`, and `20` political units under baseline and Evolution I.

**Expectation:** every result remains inside the specification table. The draw never removes more candidates than exist and never leaves an invalid loyalist rump except for the explicit two-member case.

### AB-CNT-02 World mutation cap

Build four large Evolution III factions whose unconstrained results would move more than eighteen political units.

**Expectation:** highest-pressure fractures retain priority. Total moved or withdrawn political units do not exceed eighteen. Lower-priority factions convert to smaller purges.

## Side choice scenarios

### AB-SIDE-01 Close victim partner

A retained member has strong relations and ideology alignment with victims, poor relations with the leader, a shared border with victims, and no contradictory war.

**Expectation:** victim-side score ranks first.

### AB-SIDE-02 Loyal strategic partner

A retained member has high leader relations, major war contribution, shared enemy, and supply dependence on loyalists.

**Expectation:** loyalist score dominates even when the victim side is slightly stronger.

### AB-SIDE-03 Distant exhausted member

A member is geographically distant, low on equipment, in another war, and has weak relations with both sides.

**Expectation:** neutral withdrawal ranks first when legal.

### AB-SIDE-04 Contradictory war

A member prefers the victim side politically but already fights one victim in another active war.

**Expectation:** victim-side probability is zero. The resolver chooses loyalist or neutral according to legality.

### AB-SIDE-05 Leader isolated

Most core members have poor leader relations, strong mutual ties, and greater combined capability than the leader.

**Expectation:** Evolution II can produce a leader-isolated result. Baseline cannot expel the leader directly.

### AB-SIDE-06 The Offensive comparison

Evaluate the same viable split with The Offensive inactive and active.

**Expectation:** active posture increases aggressive side commitment and lowers settlement preference, but no invalid side gains weight.

## Conflict intent scenarios

### AB-INT-01 No territorial claim

The leader is stronger, values the victim strategically, and holds no claim.

**Expectation:** forced compliance ranks above territorial settlement and liquidation.

### AB-INT-02 Registered core claim

The leader has a core or claim on reachable victim territory and the target remains viable.

**Expectation:** territorial settlement gains weight. It cannot demand unrelated states.

### AB-INT-03 Tiny target at high Chaos

A one-state victim, severe hostility, high Chaos, and strong loyalist advantage.

**Expectation:** liquidation becomes possible but remains below limited aims unless explicit extreme conditions are present.

### AB-INT-04 Hopeless loyalist war

The victim coalition is stronger, loyalist supply is broken, and the leader faces another major war.

**Expectation:** aggressive intent weights fall. Settlement or recognized separation becomes dominant.

## Decision priority scenarios

### AB-DEC-01 Weak victim with stockpile

Victim has low field strength but enough manpower and equipment.

**Expectation:** Emergency Mobilization ranks above diplomatic and cohesion actions.

### AB-DEC-02 Weak victim without equipment

Victim lacks equipment but has potential sponsors.

**Expectation:** Request a Foreign Lifeline and capital defense rank above an unaffordable mobilization action. Unpayable decisions have zero action probability.

### AB-DEC-03 Loyalist cohesion collapse

Leader has disintegrating cohesion before an offensive begins.

**Expectation:** Secure the War Council or a settlement action ranks above Coordinate Punitive Operations.

### AB-DEC-04 Donor reserve floor

A co-victim has surplus relative to the recipient but would fall below its own reinforcement floor after transfer.

**Expectation:** equipment-pooling action has zero donor probability.

## Outside sponsor scenarios

### AB-SPN-01 Reachable ideological partner

Sponsor has strong relations, convoys, equipment, access, and a rival interest against the leader.

**Expectation:** guarantee or material support ranks high.

### AB-SPN-02 Overextended distant major

Sponsor has good relations but no route, low convoys, and two active wars.

**Expectation:** mediation or no action ranks above material support. Direct intervention is invalid.

### AB-SPN-03 Rival sponsors

Two outside powers support opposing sides and can reach the theater.

**Expectation:** support interest rises, settlement becomes harder, and the two-sponsor cap remains enforced.

## Settlement scenarios

### AB-SET-01 Victim capital held

Victim completed the hold mission, cohesion is coordinated, and loyalist offensive failed.

**Expectation:** recognized separation acceptance rises sharply.

### AB-SET-02 Victim near capitulation

Victim capital lost, surrender progress high, no sponsor, reserves exhausted.

**Expectation:** conditional readmission or limited compliance terms dominate continued resistance.

### AB-SET-03 Unrelated territorial demand

Loyalist offer demands a state without a core, claim, occupation settlement, or accepted transfer rule.

**Expectation:** offer is invalid, not merely unpopular.

### AB-SET-04 Offensive active but hopeless

The Offensive is active, but the AI has no supplied divisions, capital security, or industrial reserve.

**Expectation:** settlement acceptance remains high. The Offensive cannot keep rejection dominant.

## Evolution pacing scenarios

### AB-EVO-01 Threshold without proof

Chaos crosses `400` during an active baseline purge, but no retained member has valid defection interest.

**Expectation:** Evolution II timer can begin only after proof appears. No Evolution log occurs.

### AB-EVO-02 Valid split after threshold

Chaos is `400+`, two retained members refuse commitments, both sides are viable, and no armistice is active.

**Expectation:** dynamic pacing moves toward an internal split around the intended base window. Exact timing depends on declared factors.

### AB-EVO-03 Disabled Evolution

Repeat a valid Evolution II case with the Evolution disabled.

**Expectation:** all Event 62 defection and split weights are zero. Baseline purge remains valid.

## Required comparison output

For every patched weighted surface, the final auditor handoff should include:

- scenario ID
- source revision before and after
- complete candidate pool statement
- factor inputs
- result classification
- ordering or distribution before
- ordering or distribution after
- whether the specification expectation passed
- unresolved external factors
- linked MCP artifact or scenario hash
