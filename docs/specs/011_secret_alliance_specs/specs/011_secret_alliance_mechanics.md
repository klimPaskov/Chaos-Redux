# Event 011 Secret Alliance mechanics specification

## State model

The pact uses a global or target-owned state model with member flags on participating countries. The target country stores the player-facing values and display state. Member countries store participation, secrecy, confidence, and role flags.

Core target values:

| Value | Role | How it changes |
| --- | --- | --- |
| `pact_suspicion` | How much the target can see a pattern | Rises from repeated incidents, leaks, successful investigations, failed pact actions, and high-chaos pressure |
| `pact_evidence` | Proof that can be used to expose members | Rises from investigations, courier turns, intercepted communications, and member leaks |
| `pact_preparedness` | Target readiness for reveal or war | Rises from defense decisions, missions, border guards, mobilization, and allied support |
| `pact_infiltration` | Pact reach inside the target | Rises from successful pact actions, target low stability, weak counterintelligence, and repeated failures |
| `pact_pressure` | Pact aggression toward open action | Rises from pact events, major patron leadership, target wars, target expansion, and high chaos |
| `pact_cohesion` | Pact willingness to stay coordinated | Rises from member confidence and patron backing. Falls from evidence, diplomacy, losses, and member fear |
| `pact_war_preparation` | How ready the pact is for public confrontation | Rises from Evolution II actions, patron involvement, target weakness, and member count |
| `pact_public_reveal` | Public state gate | Set once the compact becomes visible |

Core member values:

| Value or flag | Role |
| --- | --- |
| `secret_alliance_member` | Country is part of the hidden compact |
| `secret_alliance_founder` | Country was one of the original three |
| `secret_alliance_patron` | Country is a major or strongest leader inside the compact |
| `secret_alliance_wavering` | Country can be split or bought out |
| `secret_alliance_exposed` | Country is known to the target |
| `secret_alliance_public_member` | Country is part of the visible faction state |
| `secret_alliance_member_confidence` | Country-specific willingness to escalate |
| `secret_alliance_member_exposure` | Country-specific evidence against that member |

## Candidate eligibility

A founding member must be:

- Alive and independent enough to conduct diplomacy.
- Not the target.
- Not a subject of the target.
- Not in a war with the target.
- Not a special chaos country or a nonhuman country.
- Not a country with a temporary existence model that cannot use normal diplomacy.
- Preferably a minor country.
- Preferably outside a faction.

A faction member is not an absolute invalid candidate unless the pool is too narrow, but faction membership is a strong penalty at baseline. The design goal is that the initial pact looks like a set of unrelated minors, not a disguised part of an existing bloc.

A founding opening should require three valid minor candidates. If the pool is smaller, the root event is unavailable for that target and should show the same unavailable treatment used by other target-gated events.

## Weighted founding member score

The implementation should use a scripted score or reusable helper. The exact numeric tuning belongs in script constants, but the score should follow this model:

| Factor | Direction |
| --- | --- |
| Independent minor | Strong bonus |
| Outside a faction | Strong bonus |
| Shares a land border with target | Bonus |
| Same strategic region or continent | Bonus |
| Target recently generated threat, annexed land, or joined wars | Bonus |
| Different ruling ideology from target | Bonus |
| Negative opinion of target | Bonus |
| Target has claims on candidate or candidate has claims on target | Bonus |
| Candidate is a subject | Exclude unless the subject status allows separate diplomacy |
| Candidate is in target faction or allied to target | Exclude or near-zero score |
| Candidate is at war with target | Exclude |
| Candidate is already in another active Chaos Redux crisis role | Strong penalty or exclude depending on role |
| Candidate is a major during baseline | Exclude for baseline founding |

The member picker should avoid choosing several countries with no plausible connection if better candidates exist. Geographic and ideological variety is acceptable, but at least one founding member should have a concrete reason for hostility when the candidate pool supports it.

## Major patron eligibility

A major patron can appear through Evolution II. It must not already be at war with the target. It should not be in the target's faction, a subject of the target, or a special chaos country.

Major patron score should favor:

- Rival ideology.
- Competing faction leadership.
- Proximity to the target.
- Prior diplomatic hostility.
- Large army compared to the target.
- Fear of target expansion.
- Existing relations with founding members.
- High chaos.
- Low evidence and high pact cohesion.

A major can be a founder only in a pre-fire evolved opening. That package starts with the patron and at least two minor members, then opens the counter-play layer soon after the first report.

## Invitation rules

Invitations are not daily world scans. They should be event-driven or pulse-driven through scheduled pact actions. Each invitation attempt picks from a scored candidate pool and rolls against pact cohesion, pressure, patron backing, and the target's recent reputation.

Invitation outcomes:

- Joins hidden pact.
- Refuses and stays silent.
- Refuses and leaks partial evidence.
- Refuses and warns the target if the target has strong relations or high diplomatic credibility.
- Accepts only as a wavering member with low confidence.

Invitation attempts should pause or slow when:

- The pact is already public.
- The target has strong evidence and public exposure is near.
- The pact has too many members for the current stage.
- The target has successfully isolated the patron.

## Stage caps

The following caps are design targets. Implementation can tune exact values through script constants.

| Stage | Hidden member shape | Major patron shape | Aggression |
| --- | --- | --- | --- |
| Baseline | Three founders, rare extra observer only through special leak route | None | Low |
| Evolution I | Founders plus small number of minors | None | Moderate covert pressure |
| Evolution II | More minors, patron possible | One major can join or found evolved opening | High covert pressure |
| Evolution III | Public faction, public recruitment possible | One major likely if not weakened, second major rare | Open military pressure |

## Pact action families

### Diplomatic chill

A low-risk baseline action. It damages opinion, creates identical diplomatic notes, and increases suspicion slightly if repeated. It should not feel decisive alone.

### Press campaign

A hidden pact member funds newspapers, radio, or public meetings against the target. It can reduce target stability or relations with nearby neutrals. It raises suspicion if the same phrases appear in several countries.

### Courier circuit

A covert logistics action. It increases pact cohesion or creates member confidence. Player investigations can intercept it for evidence.

### Industrial survey

A member's trade or military mission probes target industry and railways. It can make later sabotage stronger. Countermeasures can block it.

### Sabotage attempt

Evolution II action. It can damage a factory, railway, supply hub, airbase, dockyard, or infrastructure in a target state. Damage should scale by infiltration, target counterintelligence, state importance, and preparedness. Fatal sabotage can feed the deaths tracker at a small or moderate level depending on state population and incident type.

### Provocation

Evolution II and III action. It creates a border or diplomatic incident. Neighboring members are best targets. It can create a limited border operation, raise pact pressure, or accelerate reveal.

### Assassination or abduction attempt

Evolution II action with high visibility. It can target a general, advisor, operative, or senior political staff. The event should have several outcomes: failed attempt, wounded target, killed target, captured agent, and false flag confusion. Player security decisions reduce the worst outcomes.

### War council

Evolution III action. Pact members align war preparation, exchange guarantees, prepare simultaneous declarations, or present ultimata. Strong player preparedness weakens its effect.

## Reveal thresholds

The public reveal can be caused by these gates:

- Any hidden pact member enters war with the target.
- `pact_evidence` reaches exposure threshold and the target chooses to reveal.
- `pact_pressure` and `pact_war_preparation` reach the public ultimatum threshold.
- Pact cohesion collapses due member leaks.
- Evolution III unlocks and a delayed reveal event fires after the target has had time to interact with the category.

The reveal helper should:

- Mark public reveal state.
- Set public member flags.
- Create the `Anti-[target country] Pact` faction with a correct leader.
- Invite or add public members.
- Handle war calls based on the reveal route.
- Store founding members for achievements and history.
- Record event history.
- Unlock post-reveal decisions.
- Stop hidden invitation actions.
- Replace hidden incidents with public pressure actions.

## Faction leadership after reveal

Leadership order:

1. Major patron if present and valid.
2. Strongest founding member by industry and army size.
3. Highest cohesion member if no major and founders are weak.

If the leader capitulates, becomes invalid, or disappears from the public compact, the faction should choose the patron first, then a founder, then another valid public member if the pact still exists. If all members are gone or invalid, cleanup should close the pact and remove obsolete decisions.

## War call behavior

When reveal is war-caused, all valid public pact members should join the war immediately. When reveal is evidence-caused, the pact can form publicly but may not enter war instantly unless pressure is high or the player chooses an aggressive response. When reveal is ultimatum-caused, the pact demands concessions or compliance and can start war if the player refuses.

Valid members that cannot legally join war should receive a public hostile stance and a delayed join plan. The player should see that they are public enemies even if engine limitations defer actual entry.

## Counter-preparedness effects

Preparedness should matter at reveal. It can:

- Reduce the first sabotage or first war council effect.
- Grant temporary defense or mobilization readiness.
- Lower pact war preparation.
- Make wavering members leave during evidence reveal.
- Improve border operation success.
- Reduce assassination damage.
- Reveal one member card in the Dossier Board.

Preparedness should not be a generic permanent buff. It should be spent, converted, or decay after the public crisis begins.

## Cleanup rules

Cleanup must handle:

- Target annexed or gone.
- Member annexed or gone.
- Member becomes subject of target.
- Member joins target faction before reveal.
- Member joins war against target and triggers reveal.
- Public pact loses all members.
- Public faction leader capitulates.
- Target wins the war.
- Target accepts a settlement route.
- A major patron becomes invalid before public reveal.

Cleanup should remove hidden member flags, country variables, selected target flags, decision visibility flags, active mission flags, stale event targets, and UI selected cards. It should preserve historical flags used for achievements and event log records.

Mission cleanup should also clear active mission flags after success or failure. Public leader repair should run during lifecycle refresh and before war calls, because the valid leader can change between reveal and the first public crisis.

## Dynamic tuning model

All important values should be tuned through script constants or documented helper effects. Dynamic factors should include:

- Chaos tier and chaos value.
- Target size, industry, manpower, faction status, and recent war behavior.
- Member size and proximity.
- Member confidence.
- Pact cohesion and pressure.
- Target evidence and preparedness.
- Target agency or counterintelligence state.
- War state and border state.
- Prior successes and failures.

Avoid fixed costs, fixed chances, and identical timers across all actions. Use duration bands and dynamic factors so baseline is quiet, Evolution I is noticeable, Evolution II is threatening, and Evolution III is openly dangerous.
