# Event 31 agent decisions, 2026-10-04

## Authority and disposition

The user granted full design authority for the Event 31 takeover on 2026-10-04 and asked that the recommended, spec-consistent option be chosen without further input.
Each decision below is `accepted and queued` on that basis until its implementation commit lands, when it becomes `implemented` with the commit recorded beside it.
The accepted design remains `docs/specs/031_random_terror_specs/`; these decisions only resolve gaps and contradictions found in the current source.

## Decisions

### D1 Carrier availability and reuse

A carrier is free only when its tag does not exist in game and its `random_terror_slot_<tag>_used` flag is clear.
The normal spawner, the Global Jihad availability trigger and the scenario preflight all use that one predicate.
Cleanup clears the used flag only when the tag no longer exists, so a retained human-controlled actor can never be reused or receive a second starting package.
Basis: the landless carriers fail `exists = yes` before their first transfer, which made Global Jihad unlaunchable, and Part 5 requires a carrier to be released only after all actor state is gone.

### D2 Scenario capacity and failed launches

The preflight counts only carriers whose evolution gate the requested intensity unlocks.
Low, Medium and High require their configured actor count, and Maximum uses the largest valid actor count the free carriers and valid states support, with a minimum of one.
Evolution unlock flags and stages are applied only after the preflight passes, so a blocked launch leaves no evolution, flag or actor behind.
Basis: Part 7 availability, Maximum actor rule and acceptance case 11.

### D3 Parent survival and war on ordinary actor creation

An ordinary spawn never takes the parent's capital and requires the parent to keep at least one other owned and controlled state.
When that fails, the state keeps its lost-control stage and the existing coup or civil-war branch carries the crisis.
A newly created actor immediately declares war on its parent when it can, matching the Global Jihad setup.
Basis: Part 5 parent-survival rules, and the retake, offensive and isolation actions all assume a real war that ordinary spawns never created.

### D4 Event-owned recurring incident pulse

Each affected country receives one hidden, event-owned pulse event scheduled from the Part 2 timing bands by its most severe active state.
The pulse applies one incident to a valid active state of that country, resolves spread only through the existing incident engine, and reschedules itself while the country still has an active crisis.
A country flag guards against duplicate pending pulses, the pulse never touches repeatable weight or minor-event pacing, and no world iteration is added.
Basis: Part 1 recurring crisis loop and Part 2 recurring incident pacing.

### D5 Mission objectives

Achieve-type missions (Contain the Attack Wave, Break the Cross-Border Corridor, Restore Civil Authority) complete when measurable state progress is reached, measured against values stored when the mission starts.
Hold-type missions (Protect the Transport Network, Prevent Capital Seizure) resolve at the deadline as success when the objective held without a new disruption, and as partial or failure otherwise.
The hostage response actions stay usable on the hostage state while the Hostage Deadline holds its slot, and its deadline gains the accepted partial outcome.
Basis: the decision and mission matrix outcomes, and the audited self-blocked success flags.

### D6 One Territorial Control value

`random_terror_territorial_control` is the only actor control value.
Every reader and writer of `random_terror_actor_control`, including the focus tree, decisions, event weights and category text, moves to it.
Basis: the category showed a value that no gate used.

### D7 State stage modifiers and map mode

Each state activity stage from Dormant to Lost Local Control carries its own dynamic state modifier, applied when the stage changes and removed when the state clears.
Event 31 gets its own state map mode in a separate map-mode file with stage colours, border thickness cues and a tooltip naming the stage, the current government mission and the broad next risk.
Basis: Part 2 state modifier effects and Part 11 state and map presentation.

### D8 One target row per decision

State-targeted government decisions target the country's current priority crisis state and its active mission subject states, so each decision shows one row in normal play.
Basis: the matrix visible-action budgets and the engine rule that every matching target creates its own row.

### D9 Real actor operations

Actor actions perform their matrix operation with existing units and buildings: militia and defector actions create bounded formations, depot repair and civil administration change real buildings or state control, foreign fighters give a net manpower intake and one experienced formation, and lifecycle refresh only manages its own lifecycle ideas so focus rewards stay in place.
Basis: the matrix result column and the audited hollow helpers.

### D10 Faction joins, reports and news

Joining the final command uses the final actor as the faction owner that adds the joining actor.
Evolution IV fires its own report, the network, first-territory, Final Jihad and Broken Claim news events are wired to their moments, and Global Jihad setup suppresses the lower evolution popups in favour of its own report.
Global Jihad at Medium and above creates the Jihadist International led by its strongest actor when at least two valid actors exist, and leaves at least one actor independent at High and Maximum.
Basis: Part 4 logging rules, Part 7 setup step 5 and actor distribution rules.

### D11 Portrait pool consumers

The 36 roleless pool characters are recruited by the carrier histories in small region and gender pools.
One-person carriers promote one pooled candidate at actor setup and replace the leader when the carrier is reused, while councils and The Unanswered Presence keep their institutional or symbolic identities.
Basis: country package matrix naming rules and the portrait consumer handoff.

### D12 Terminal counteroffensive

`random_terror_terminal_counteroffensive` stays as the one terminal-phase government action of the Final state budget.
Basis: the matrix Final state budget row allows a terminal action, and it is the only coalition action against the final command.

### D13 In-world wording

In-world event, focus, decision and news text names the movement directly and does not call it fictional.
The scenario premise in the Triggerable Scenarios window keeps its framing sentence.
Basis: the event writing rules, while the representation rule stays a design constraint in the spec.
