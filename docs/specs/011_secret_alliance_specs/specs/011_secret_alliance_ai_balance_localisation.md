# Event 011 Secret Alliance AI, balance, and localisation direction

## AI actor groups

| Actor group | Behavior goal |
| --- | --- |
| Founding minor members | Harass and coordinate without choosing instant suicide |
| Wavering members | Join for fear or patronage, leave when evidence and diplomacy are strong |
| Major patron | Coordinate sabotage, accelerate reveal, and lead public faction if confident |
| Target country AI | Investigate, defend, and prepare using the same action families as a player |
| Nearby neutral countries | React to evidence, decide whether to warn the target, stay neutral, or drift toward pact pressure |
| Existing allies of target | Help through guarantees, volunteers, intelligence, or diplomatic pressure when evidence is public enough |
| Enemy countries already at war with target | Receive covert support, but should not automatically join the hidden compact |

## Founding member AI

Founders should prioritize low-risk covert actions during baseline. Their willingness rises with pact cohesion and target threat. Their willingness falls when the target is much stronger, when evidence is high, when they are bordering the target with weak defenses, or when their stability is low.

Founders should avoid open war until reveal unless:

- They are already pulled into war by ordinary diplomacy.
- The target attacks them.
- The pact pressure is high and Evolution III is near.
- A major patron is present and target preparedness is low.

## Wavering member AI

Wavering members join for safety, not ideology. They should be more likely when a major patron exists or when the target has been aggressive. They should leave or leak when:

- Evidence is high.
- The target offers a face-saving exit.
- The target has strong relations with them.
- The pact leader is weak.
- The pact is near public reveal and the target's army is much stronger.

Wavering members should not receive the strongest public pact bonuses.

## Major patron AI

A major patron should behave like a strategic sponsor. It should use actions that increase cohesion, sabotage strength, member confidence, and reveal pressure. It should not join if already overwhelmed, if it depends on the target's faction, or if it has no strategic reason to oppose the target.

Major patron route preferences:

| Situation | Preference |
| --- | --- |
| Rival ideology and strong army | High willingness to join and lead |
| Same faction as target | Avoid |
| At war with target already | Cannot join hidden pact, route through reveal if already a member |
| Target has high evidence | Avoid or rush reveal if already involved |
| Target weak and isolated | Accelerate ultimatum |
| Target strong and allied | Prefer covert pressure and member expansion |
| Patron has low stability | Avoid public reveal unless high chaos |

## Target AI response

If an AI country becomes the target through multiplayer or settings, it should use category actions based on situation:

- Low stability: secure capital ministries and avoid risky public leaks.
- High industry: harden industry and guard rail nodes.
- Strong army: prepare war case and border readiness.
- Weak army: quiet talks and member splitting.
- Has agency: investigation actions first.
- Bordering member: frontier sweeps and border readiness.
- High evidence: controlled reveal and diplomacy.
- High pact pressure: emergency preparedness.

AI target should not ignore the category. It needs a periodic decision plan that reads values and selects from the same action families.

## Neutral country reactions

Neutral countries can receive event-driven reactions when the target publishes evidence or when the pact pressures them. Possible outcomes:

- Warning sent to target.
- Neutrality reaffirmed.
- Relations cool toward target.
- Refusal to join hidden pact.
- Quiet cooperation with the pact.
- Public condemnation of the pact after exposure.

Neutral AI should weigh ideology, distance, target threat, member pressure, and relations.

## Balance shape

The pact should be threatening because it accumulates pressure, not because one hidden action destroys the player. The player should feel an early signal, a growing pattern, then a crisis.

Balance targets:

| Stage | Player impact | Counter-play expectation |
| --- | --- | --- |
| Baseline | Minor but noticeable after several incidents | The player can suspect a pattern but has limited tools |
| Evolution I | Noticeable diplomatic and covert pressure | The player can infer coordination from repeated patterns |
| Evolution II | Real sabotage, political danger, and decision category | The player can weaken, expose, delay, or prepare |
| Evolution III | Public faction, war option, and high aggression | The earlier response materially changes the opening crisis |

## Effect strength

Important actions should matter. Avoid tiny modifiers as the main effect. A strong effect is acceptable when it has clear costs, cooldowns, risks, or a stage gate.

Examples of meaningful effects:

- A successful industrial security mission can prevent the next major sabotage event.
- A strong public dossier can make one or more wavering members leave.
- A failed assassination protection mission can remove or wound a relevant advisor or general.
- A border operation can reduce the member's opening war preparation.
- A successful patron exposure can block rare second-major membership.

Small relation or stability modifiers can support the event, but they should not be the whole payoff.

## Localisation direction

Player-facing text should be in-world and direction-only. It should not reveal hidden member lists before the mechanic reveals them. It should describe repeated behavior, public unease, and concrete incidents.

### Root report direction

The first report should center on repeated diplomatic behavior from unrelated capitals. It should mention matching phrasing, similar requests, and staff noticing a pattern. It should not name the pact.

### Baseline follow-up direction

Baseline reports should describe a trade mission, a newspaper line, a customs block, an attache request, or an embassy habit that repeats. The player should feel the event through repetition and wrong detail.

### Evolution I direction

Evolution I text should make the pattern more obvious through multiple countries acting in a coordinated way. It should still avoid direct confirmation. Use public nervousness, merchant hesitation, and military staff noticing similar routes.

### Evolution II direction

Evolution II text should show that people are being hurt or threatened. Sabotage, provocation, missing couriers, and attacks on officials can appear. The decision category direction should feel like the target government organizing a counter-network.

### Evolution III direction

Evolution III text should be public, hard, and direct. The faction name becomes visible. Member countries stop pretending incidents are unrelated. If war causes reveal, the reveal text should move quickly from surprise to practical war readiness.

### Option tone direction

Options should not be bland. Use official suspicion, cold resolve, grim understatement, or controlled anger. The humor mode should be restrained because the event can lead to assassination and war. A few low-stakes early reports can use dry bureaucratic irony, but major sabotage and deaths should stay serious.

### Decision text direction

Decision names should sound like government actions, intelligence tasks, or military security orders. They should not expose hidden future branches. Descriptions should show visible requirements, costs, and expected public effect.

### Event Details direction

Event Details should explain the premise as a hidden pattern of foreign coordination against the target that can become public and military if left unchecked. It should not list modifiers, rewards, or hidden thresholds.

### Super-event direction

The reveal super-event prompt handles source-dependent title, quote, button, and audio research. The spec only defines the role and tone.

## Achievement design spread

Achievements should reward different play styles:

- Early investigation.
- Diplomatic splitting.
- War survival.
- Small-country victory.
- Preemptive border success.
- Major patron isolation.
- Winning without relying on a larger faction.
- Defeating founding members quickly after reveal.

Achievements should not unlock just because the event fired or because the player waited.

## Acceptance checks

Implementation should provide evidence for:

- Candidate selection and founding members.
- Member invitation and reveal routes.
- Evolution entry paths.
- Decision category visibility and cleanup.
- Dynamic values and cost scaling.
- AI action use and invalid route blocking.
- Event log and detail wording.
- Asset and super-event handoff state.
- Achievement tracking and disqualifiers.
- Spreadsheet alignment after final wording exists.
