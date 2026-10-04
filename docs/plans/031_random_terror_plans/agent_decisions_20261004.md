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

## Implementation round 1 status

The round was asked to append to `agent_decisions_2026-10-04.md`; it appends here, to the existing decisions file of the same date, so the takeover keeps one decisions record.
Implementation evidence below proves what exists in source; it does not replace live-game validation, which belongs to the user.

| Decision | Disposition | Implementation commits | Validation limits |
| --- | --- | --- | --- |
| D1 Carrier availability and reuse | implemented | `cbf96a95e` | Carrier reuse after a peace-deal death needs a live save. |
| D2 Scenario capacity and failed launches | implemented | `b69105ae4` | Launch at each intensity needs a live run. |
| D3 Parent survival and actor war | implemented | `cbf96a95e` | `declare_war_on` availability depends on live diplomacy. |
| D4 Recurring incident pulse | implemented | `33a9d3b30` | Pulse timing is MTTH-driven; the probability audit route failed (see below). |
| D5 Measured mission objectives | implemented | `21f7cd1cc` | Mission completion needs live scenarios. |
| D6 One control value | implemented | `be7cd444a` | None beyond source review. |
| D7 State stage modifiers and map mode | implemented | `b25ba5124`, `26ef0bb94` | Map mode colours, thickness, pulse and button art need a live view. |
| D8 One target row per decision | implemented | `9ea870a8c` | Row count needs a live decision panel. |
| D9 Real actor operations | implemented | `8fe778928`, `e280dace9` | The `create_unit` and `delete_unit` meta-effect ids need a live check. |
| D10 Faction joins, reports and news | implemented | `04c57ae5f`, `f82397910`, `b69105ae4` | `add_to_faction` direction and popup suppression need a live run. |
| D11 Portrait pool consumers | implemented | `cfe741c34` | Displayed portraits need a live view. |
| D12 Terminal counteroffensive | implemented | no change required; the existing action already fills the role | None. |
| D13 In-world wording | implemented | `33e02046a` | The Evolution IV catalog row is queued in `catalog_changes_pending.md`. |

## Round 1 decisions

Each decision below was taken under the same delegated authority and is `implemented` in the commit named beside it.

### R1 Lazy carrier release and capital coups (`cbf96a95e`)

`random_terror_release_dead_carriers` clears a reservation only for a tag that no longer exists and runs at refresh, spawn, scenario launch and revelation, so no periodic hook is needed.
A capital that reaches Lost Local Control and cannot secede triggers the existing coup branch instead of an actor spawn.

### R2 Lifecycle refresh owns only its failure overlay (`e280dace9`)

The actor lifecycle refresh adds and removes only the failure spirits it added itself, marked by `random_terror_lifecycle_owns_<idea>`, and never manages the starting profile pair, so focus-earned spirits are never stripped.

### R3 Pulse stops when Event 31 is disabled (`33a9d3b30`)

The hidden pulse event `chaosx.nr31.96` reschedules itself only while `random_terror_event_is_enabled` holds, so turning Event 31 off in the settings ends the recurring incidents.

### R4 Mission outcome mapping (`21f7cd1cc`)

Retaking a lost state succeeds on military control, and the resolver clears Lost Local Control.
Restore Civil Authority advances through Support Victims in recovering states.
The hostage deadline gains a partial outcome through a Security Surge on an armed cell or a partial raid.
The Capital Uprisings scenario opens the capital mission.

### R5 Global Jihad transaction details (`b69105ae4`, `f82397910`)

The scenario resolves only its target evolution stage, clamps Maximum to the largest valid actor count with a floor of one, applies evolutions only after the preflight passes, and sends report `.6` to players whose countries were not seeded.
The Evolution III report waits for the first actor, and every evolution report is held back during setup.

### R6 Reinforcement and affordability (`8fe778928`, `2c0b7ed99`)

Military Reinforcement blocks Lost Local Control in its state for `reinforcement_days` through the timed `random_terror_state_reinforced` flag.
Affordability uses one inclusive `NOT = { x < cost }` trigger per decision instead of separate threshold constants.

### R7 Target rows (`9ea870a8c`)

Decisions keyed to a recorded marker keep that marker as their target, while generic crisis decisions use the priority crisis state and mission subjects.

### R8 Terror Activity map mode (`26ef0bb94`)

The map mode lives in its own file, colours and thickens state borders by stage, pulses the viewer's response targets and never shows hidden readiness.
Its buttons use a native-alpha generated bomb subject mapped onto the custom map mode button family.

### R9 Focus rewards (`d2407706f`)

The eleven variable-only focuses run one `random_terror_focus_reward_<name>` effect behind a plain tooltip, as tabled in `docs/events/031_random_terror/overview.md`.
Establish Political Offices opens Build a Civil Administration to the Ideological Secretariat.
Lead the Coordination Structure never overrides another network leader or pulls in a command marked independent by Global Jihad setup.
Challenge Rival Governments grants one `topple_government` war goal, preferring a neighbour facing Armed Insurgency or Lost Local Control.
Break the Last Corridor never transfers a national capital.
The route-choice focuses add their route's decision flag, because the tree audit found that choosing a route never opened that route's decisions, and the header route line prefers the chosen route.
The two bunker focuses pass a province selection, since bunkers are province buildings.

### R10 Wording (`33e02046a`)

Fictional Religious Councils becomes Compliant Religious Councils and Forge the Fictional Seal becomes Forge the Seal; focus ids stay unchanged.
The False Revelation world-end entry in the shared events log localisation drops the word as well.

### R11 Movement restriction escalation (`a55eb8241`)

Each use raises the Stability price by 0.05 and the support equipment price by 20, up to two steps; the base price check remains as a floor.
The use counter replaces the old used flag, and every use after the first draws public condemnation.

### R12 Orphaned actor states (`a55eb8241`)

With no living parent, each state of a retired AI actor goes first to a living government outside the crisis that holds its core, and otherwise to the actor's strongest enemy by division count.
An AI actor left with a state nobody can take keeps its Event 31 identity and units; no separate marker flag is set because nothing would read it.
The JMX history uses the literal research slot count 3, matching `actor_research_slots`.

### R13 Plan documents (`8cfe65359`)

The stopped thread's finished audit handoffs, probability baselines and comparisons, before-snapshots and fixtures are committed as they stand, and the visual asset audit records the portrait pool consumers and the two map mode buttons.

## Route evidence and gaps

- `hoi4.probability_inspect` failed with `INTERNAL_ERROR` when given a source path and with invalid-argument errors without one, so the D4 pulse and the AI weight changes in `711d4fde2` have only the committed before-snapshot under `evidence/ai_modifier_before_20261004/`; the same-scenario baseline and comparison remain open.
- `hoi4.focus_inspect` and `hoi4.focus_render` on `random_terror_actor_focus_tree` succeeded after the focus reward change: 114 focuses, zero connector crossings, zero long connectors, zero tree diagnostics, source revision `1d972cb10b478ad153f3e2f702945ae5e829a3eaf0d1a79e0e853b16e6252658`, layout hash `69ec88315409c5c578ffca2852052037f7ee6a48510a92189c11ac79a1a6d2a9` (layout unchanged).
- `hoi4.reference_search` answered narrow queries for `add_building_construction`, `every_neighbor_state` and the related effects in the installed `effects_documentation.md`.

## Open after round 1

- Further focuses remain value-only or flag-only: among them Define Leadership, Relocate the Command, Distribute the Cells, Intelligence by Whisper, Command the Front, Bargain with Rivals, Seize the Urban District, Break the Parent Government, Lead the Final Jihad, Join the Jihadist International, and the three focuses that call `random_terror_actor_call_coordinated_uprising`, whose focus-side call only sets an unread flag.
- Several shared tuning values are not multiples of five (`unity_gain` 4, `actor_control_convert_gain` 8, `actor_supply_corridor_gain` 8), and Convene the Cadre and Codify the Doctrine both add `random_terror_cadre_authority`.
- The workbook owner must apply `catalog_changes_pending.md`.

## Round 1 continuation

The lead's 22 round-1 items were already implemented in the commits listed above, so the continuation resumed from "Open after round 1" and from defects found while reviewing the focus tree against the Part 6 reward rules.
Each decision below was taken under the same delegated authority and is `implemented` in the commit named beside it; live-game behaviour remains with the user.

### R14 Focus rewards never lock actor decisions (`9e9a7b806`)

Thirty-five focuses reused actor decision helpers, which set the 14-day action lock through `random_terror_actor_action_common`.
Focus rewards set the temp variable `random_terror_focus_context` first, and the common step starts the cooldown only outside that context.
Unread bookkeeping flags (action record, membership record, uprising call, failed revelation gate) were removed, absorbing an actor no longer marks the absorber with the community-rejection flag, and actor retirement also removes International Mandate, Local Revolt, Mass Defection and Failed Rule.

### R15 Ideological mobilization is a timed recruitment drive (`3f08c7355`)

Begin Ideological Mobilization charged manpower and only set a permanent flag while its tooltip promised more manpower.
Per the matrix row (recruitment and obedience, with a duration), its manpower price now becomes one disciplined formation (two after Codify the Doctrine), the command gains `random_terror_mobilized_cadres` for `mobilization_days`, and the decision reopens when the mobilization ends.
A separate permanent `random_terror_ideological_mobilization_recorded` flag keeps the Jihadist International entry condition.

### R16 One stable spirit per idea slot (`73dfc8045`)

The tree stacked several forms of one institution (for example Distributed and Unified Field Command, or four legitimacy forms at once) and fourteen focuses granted a spirit the actor already held.
Command, economy and legitimacy are slots, set only through `random_terror_set_<slot>_form`, which removes the other stable forms of the slot; the failure overlay stays outside the slots and keeps ownership of Looting Spiral and Sponsor Dependency unless a focus chooses them.
The opening no longer replaces a starting spirit, so the three starting problems last until the route choices, matching the Part 6 lifecycle table.
Every focus that only repeated a spirit received its own concrete reward, as listed in `docs/events/031_random_terror/overview.md`.

### R17 Concrete rewards for the remaining hollow focuses (`d334dc062`, `173fad47c`, `09b093898`)

Every remaining focus that only moved hidden values or set a flag now changes the map, forces, diplomacy, a decision transaction or a visible value, with a plain tooltip; the full table is in the overview.
Rewards that bind another command use the existing consent events: the merger offer (`chaosx.nr31.43`), the sponsor request (`chaosx.nr31.42`) and the membership request (`chaosx.nr31.44`).
Access, pacts, guarantees and faction entry granted without such an event apply only to AI commands, so a player command is never bound without its own choice.
Open the Worldwide Uprising launches a real coordinated uprising only after Evolution V, because the government's Stop the Coordinated Uprising mission requires it; before then it prepares cells.
Every formation raised by a focus or an actor action goes through `random_terror_focus_raise_formation`, which respects `actor_division_cap`.
Salvage the Rail Spur used `add_building_construction` with `rail_way` in a state scope, which vanilla never does; it now lays a railway with `build_railway` between the seat and a border state.

### R18 Tuning values in multiples of five (`a9b46c56d`)

The actor gains and the two army-experience prices that double as focus rewards were 3, 4, 6, 8 or 12; they are now 5 or 10, as the focus-tree rules require, and every cost row reads the same constants.
Government-side mission and pressure values were left as they are because they are outside the focus-tree rule and carry the accepted mission balance.

## Route evidence for the continuation

- `hoi4.focus_inspect` on `random_terror_actor_focus_tree` succeeded before (revision `93811ab314e9556dec7ed4d952dc4e0f2c7abccf541c118d2f26abc9cd4a2401`) and after (revision `fc0ea4895b3df48b810aad091d3de376609f25cb10d4745bb6dc7abd5aa94db2`) the reward changes: 114 focuses, zero tree diagnostics, zero connector crossings, layout hash `69ec88315409c5c578ffca2852052037f7ee6a48510a92189c11ac79a1a6d2a9` unchanged.
- No AI weight, MTTH or random-selection value changed in the continuation, so no new probability comparison was required; the round-1 probability gap above still stands.
- Source checks run on every commit: brace balance with comments stripped, every referenced script constant defined with a schema, every scripted effect and trigger call defined, every tooltip and cost key localised.

## Open after the continuation

- The new rewards that reach other countries (military access, pacts, guarantees, mergers, sponsor and membership requests, railways, uprisings) need a live run to confirm the engine accepts each scope and target as written; they are `needs_live_game`.
- Idea modifiers inside each spirit still use small values such as 0.03 and 0.04, which the focus-tree rules call fairy dust; consolidating them is a balance pass of its own.
- The government-side tuning values that are not multiples of five remain as accepted.
- The workbook owner must apply `catalog_changes_pending.md`.
