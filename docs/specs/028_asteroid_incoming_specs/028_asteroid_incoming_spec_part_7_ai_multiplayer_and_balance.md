# Asteroid Incoming, Part 7: AI, Multiplayer and Balance

Status: implemented in source; numeric probability evidence is partial (see the [current resume](../../plans/028_asteroid_incoming_plans/resume_20261007.md)).
AI weights live in `asteroid_incoming_ai` and `asteroid_incoming_recovery` (`ai_*` keys).

## Opening AI

AI choices must preserve the moral and strategic meaning of the board.
Most governments take the near miss; a strike becomes plausible under war, desperation, destructive identity or very high Chaos.
The AI never chooses by option position, and the opening board and the reopened board carry identical `ai_chance` blocks.

### Near-miss weight

The near miss starts from a strong base and grows for democratic choosers, choosers at peace, stable choosers, active fragmentation and choosers that already hold crater sites.
It shrinks for desperate choosers (high surrender progress, low stability or war support), fascist choosers at war and very high Chaos.

### Strike weight

A strike starts near zero and grows when the target is an enemy, a major, a faction leader, when the locked state is its capital, or when it carries major logistics.
It is multiplied up for fascist and desperate choosers and high Chaos, and down for democratic choosers, active fragmentation, choosers already holding crater sites and targets already near capitulation.

Two modifiers come last, so no later addition can lift them:

- **Friendly ground (0.25):** the target state, a neighbour or a state two land steps away is owned or controlled by the chooser, a faction partner not at war with it, or a co-belligerent; these are the states the catastrophic and major rings would devastate.
- **Protected target (0):** the target is the chooser, a subject or overlord, a faction partner not at war with it, a co-belligerent, a non-aggression partner or a guarantee in either direction.

README Open question 5 asks whether guaranteed and non-aggression partners' states should also count as friendly ground.

A betrayal route that relaxes protection exists only if an existing AI strategy explicitly supports it; Event 028 invents none.

### Ideology

Ideology sets base willingness without replacing the world-state logic.
Democracies almost always take the near miss unless facing defeat by an existential enemy.
Non-aligned and ordinary authoritarian governments prefer it but can strike a major enemy under severe pressure.
Fascist and extreme militarist governments strike more readily during war.
Destructive special actors can treat the strike as a weapon only when their existing identity supports it.

## Target preparedness AI

The target weighs command continuity when its capital is hit or stability is low, transport dispersal when its trains, fuel and supply are exposed, and medical command when outer-ring population and rescue risk are high.
Ideology is not the main factor.

## Crater AI

Under Extraordinary Minerals:

- the six crater decisions carry their own `ai_will_do` weights, with the main crater valued above a fragment site;
- the AI strategy plan `asteroid_incoming_crater_fronts` adds front unit requests to fronts crossing the main crater (60) or a fragment site (25) while the country is at war and its surrender progress is at most 0.25, following the vanilla state-flag front pattern; it adds no forced offensive, so a collapsing country keeps its divisions at home;
- peace desires add `take_states` weight for the negotiator's own bid on the main crater (75) and each fragment site (30), below the vanilla core desire of 100, so cores, claims, influence, faction leadership and subject bids still decide the settlement.

Because each front gets one request regardless of how many sites it crosses, a later revision could scale the request with the number of sites; this is a future idea, not a requirement.

## Recovery AI

Recovery follows the priority order in Part 6 and keeps reserve floors: it does not spend the last trains needed for supply, commit all support equipment during a major war, start long industrial work in a state about to be lost, or contribute to global observation before urgent national needs have a reserve.
AI countries receive no recovery missions (Part 6).

## Multiplayer

- One chooser per transaction; tag switching does not transfer chooser authority, and a player who switches into the target receives the preparedness event if the game routes it to them.
- Other humans receive the locked-course bulletin, the impact bulletin and super-event, their own report when affected, and the close-passage bulletin after a near miss.
  The locked-course bulletin names the target and impact date but never fragment sites.
- A global transaction blocks another player's timer from starting a second copy; it resumes through the shared event system afterwards.
- The confirmation never forces several days of blocking on every player.

## Balance anchors

- The population losses and armour values are fixed user requirements; balance moves through building shares, recovery durations, target suitability, dust scaling and costs.
- The near miss has no direct reward; its value is avoided destruction, avoided dust and fragment risk, and preserved diplomacy.
- Fragments scale from three to six and report honest reductions.
- Dust must hurt the world without stopping every country from fighting; protection softens part of the penalty and nothing reverses the impact.

## Probability scenarios

The audit must evaluate the complete four-option pool in each named case, separating option score from normalized probability.

| ID | Chooser | Targets | Expected ordering |
| --- | --- | --- | --- |
| `AST_AI_01` | Stable democratic major at peace | Three neutral or friendly | Near miss dominates |
| `AST_AI_02` | Democratic major losing an existential war | One hostile major, two neutrals | Near miss stays strong; only the hostile major is plausible |
| `AST_AI_03` | Fascist major in total war | Enemy faction leader, weak enemy, neutral | Faction leader first or close to the near miss; neutral near zero |
| `AST_AI_04` | Non-aligned minor at peace | Three unrelated majors | Near miss strongly dominates |
| `AST_AI_05` | Destructive special actor | Three enemies | Best enemy can dominate when identity supports it |
| `AST_AI_06` | Ordinary country at war | Subject, faction ally, enemy | Subject and ally exactly zero; enemy competes with the near miss |
| `AST_AI_07` | Fragile chooser at 700 Chaos with fragmentation | One strong enemy | Near miss weight above the same case at 500 Chaos |
| `AST_AI_08` | Near-capitulation chooser at 700 Chaos | One existential enemy | Strike materially more likely than in a stable case |
| `AST_AI_09` | Chooser holding several crater sites | One distant enemy | Near miss gains weight |
| `AST_AI_10` | Any chooser | Ally, guarantee, subject | Near miss effectively certain |

Recovery scenarios: high preventable deaths favour mobile hospitals; a disconnected capital favours the rail corridor; a collapsing front with few trains suppresses expensive work; severe dust with strong industry favours factory hardening; a threatened main crater favours perimeter security; a distant enemy fragment site never overrides homeland defence.

## Anti-exploit rules

- Reopening the board, cancelling confirmation, or reloading never rerolls targets or fragments.
- State transfers during the lock never move the impact.
- Each state receives one profile and each death is recorded once.
- Mineral bonuses are rebuilt from current control and cannot duplicate.
- Control switching cannot repeat security or survey rewards, and achievement holds reset on lost control.
- Repairs never exceed what the impact destroyed.

## Performance

Target and ring lists exist only for the active transaction, all fragment centres lock before damage, dust uses the monthly host and event-driven updates, crater bonuses refresh from control-change hooks, and there is no new daily scan of every country.
