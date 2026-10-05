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
- The government-side tuning values that are not multiples of five remain as accepted.
- The workbook owner must apply `catalog_changes_pending.md`.

### R19 One failure spirit per slot (`d26dcd276`)

The failure overlay added two spirits per collapsed value, up to six at once.
Following the lifecycle table's "one of" failure forms, it now shows at most one command failure and one economy failure, chosen by the route chosen in the tree, else the starting profile's route: Compromised Network, Rival Warlords or Doctrinal Schism, and Looting Spiral, Sponsor Dependency or Famine.
The leadership rivalry count also counts Compromised Network, so a failing Shadow Council still registers as a rivalry.

### R20 Spirit and state modifiers in multiples of five (`aff63d7d3`, `55a4727f8`)

Every actor spirit modifier and every staged state modifier now uses a multiple of 0.05, keeping each spirit's four modifiers and their direction and keeping the state penalties growing by stage.
Final route forms carry 0.10 in their signature modifiers, and the terminal spirits keep their 0.10 to 0.20 scale.

## Round 1 review fixes

The round 1 review re-read every continuation commit against the Part 6 lifecycle table and the consent rule of R17.
Each decision below was taken under the same delegated authority and is `implemented` in the review commit; live-game behaviour remains with the user.

### R21 Failure forms follow the slots

The crisis focuses still stacked failure spirits: Leadership Split and Compromised Network could show two command failures, the overlay could add a third beside a focus-chosen one and later strip the focus's spirit on recovery, and Local Revolt granted Local Revolt and Failed Rule together.
Command failures chosen by a focus now go through `random_terror_set_command_failure_form`, which replaces any other command failure and takes the chosen one over from the overlay, and the overlay adds a command failure only while the actor shows none.
Legitimacy failures go through `random_terror_add_legitimacy_failure`: the first shows as itself, and a second, different one merges both into Failed Rule, matching the table's "one of" failure forms.
Negotiated Enclave and Return from the Crisis list and remove only the failure spirits the actor holds.

### R22 Starting and terminal spirits are never granted twice

Founding Crisis re-granted the three starting spirits the actor setup had already given; it now adds only missing ones.
Ambiguous Light re-granted the three terminal spirits the terminal transition had already given; it now adds only missing ones and raises one final formation within the division limit.
The terminal transition also removes International Mandate and the legitimacy failure spirits, so the final command carries only its terminal spirits.

### R23 Consent rule applied to every binding reward

Lead the Coordination Structure pulled player-run commands into its faction and Reconcile the Jihadists forced white peace on player-run commands, against R17.
Both now bind only AI-run commands, and their tooltips say so in plain terms.

### R24 Ideological mobilization reopens where it was called

The decision marked its state permanently and hid every marked state, so a command with one eligible state could never mobilize again although the tooltip promises it.
The timed country flag alone now gates the decision, so it reopens in any eligible state, the same one included, when the mobilization ends.

### R25 Railway stays on the command's land

Salvage the Rail Spur passes `build_only_on_allied = yes`, so the shortest path never lays track through a neighbour's provinces.

## Route evidence for the review

- `hoi4.focus_inspect` on `random_terror_actor_focus_tree` before (revision `a9aaf637fb9ea0884047255cf88985a1a832a216f6d98a590a3dbe1d532395e5`) and after (revision `081ddd6adefd652bbf16ba511e24d48335ea51c0001e9ddcc491cc1b134624b2`) the fixes: 114 focuses, zero tree diagnostics, zero connector crossings, layout hash `69ec88315409c5c578ffca2852052037f7ee6a48510a92189c11ac79a1a6d2a9` unchanged.
- No AI weight, MTTH or random-selection value changed, so no probability comparison was required.
- `needs_live_game`: the merged Failed Rule path, the slot tooltips shown through `if` blocks, and `build_only_on_allied` pathing on a concave command.

## Round 1 review fixes, second pass

The second review pass re-read the lead-item commits of the round (carriers, missions, pulse, reports, stage modifiers, actor actions, costs, one-row targets, headers, portraits, map mode, movement restrictions and Global Jihad setup).
Each decision below was taken under the same delegated authority and is `implemented` in the second review commit; live-game behaviour remains with the user.

### R26 Recovery keeps one Support Victims row

Support Victims was opened to recovery states (missions commit `21f7cd1cc`), but the one-row rule (`9ea870a8c`) then required the priority crisis state, which only an active crisis can be, so in the recovery phase Support Victims had no target except a Restore Civil Authority subject.
With no active crisis left, `random_terror_refresh_priority_state` now makes a recovering state the government controls the priority state, the one with the most residual activity first, so the action keeps exactly one row through recovery.
Actions that require an active crisis stage still find no target on a recovering priority state.

### R27 Terror Activity tooltip lines

The five stage texts of the Terror Activity map mode tooltip were written over three physical lines each, which the localisation parser cannot read, so the tooltip lost its response and next-risk lines.
Each text is one line with `\n` breaks.

### R28 Break the Parent Government wording

The reward said the parent "loses" a negative stability and war support value, which displayed as a double negative; it now reads "suffers stability" and "war support" followed by the signed value, as Fracture the Sky does.

## Route evidence for the second pass

- `hoi4.decision_inspect` in inventory mode returns the whole-repository inventory (8,120 decisions, `DECISION_ANALYZED_PARTIAL`) and gives no per-decision evidence for this review.
- `hoi4.probability_inspect` with the `decision_ai_will_do` adapter and a one-decision candidate pool still fails with "Invalid tool arguments"; no AI weight changed in this pass.
- `needs_live_game`: the recovery priority state row, the map mode delayed tooltip and the `[?var.GetName]` mission names in the government category header.

## Round 2 decisions

The round 2 assessment of 2026-10-05 listed new source findings and took the decisions below under the same delegated authority.
Each is `implemented` in the commit named beside it; live-game behaviour remains with the user.

### R29 Timed flags take literal durations (`05bca0b24`)

Eight timed flags passed a bare temporary variable as `days`: recent incident, pulse pending, response action lock, actor action lock, ideological mobilization, state reinforcement, coup active and government paralysis.
Vanilla `common/scripted_effects/SOV_scripted_effects.txt:28` keeps the variable form commented out with the note that it does not work with variables, vanilla `SIA_scripted_effects.txt:780` only passes `days = var:<normal variable>`, and the wiki Effects table lists `days` as `<int>` for `set_country_flag`.
A dropped duration would have made the action locks and the pulse guard permanent, so every site now builds the flag through `meta_effect` with `[?temp|.0]`, the pattern already used for the target reservation flag, and every duration is unchanged.
`add_dynamic_modifier` keeps its variable `days`, which `documentation/effects_documentation.md:1166` allows.

### R30 A contained crisis recovers and closes (`786237392`)

Basis: Part 1 baseline lifecycle (opening shock to containment and aftermath), Part 3 phase 4 and clutter control, the matrix cleanup column for Public Accounting ("one per incident package") and Security Reform ("longer cooldown"), and validation case V01.
Before this change no state was ever marked recovering unless relief or a retake reached it, closure needed four flags of which two came from once-per-game decisions, and nothing ever lowered pressure in peace, so the response category stayed open forever.

- A state that falls from Active or worse to Dormant or Clear becomes recovering, and the marker clears at Clear, so residual cells stay targetable until they are gone.
- The recovery phase begins when no state is Active or worse, no core is held at Armed Insurgency or Lost Local Control and no Event 31 command is at war with the government; no actor defeat is required.
  The territorial phase now also counts the government's cores that an armed command has taken, so a parent whose state passed to an actor keeps its territorial actions instead of entering recovery.
- Each affected government keeps one hidden, event-owned recovery check every 30 days; in recovery it lowers Terror Pressure by 10 and recovering activity by 5, and it tries to close the crisis.
  This adds no world iteration and touches neither repeatable weight nor minor-event pacing.
- The obligations are: no recovering state, no running mission and zero Terror Pressure.
  Public Accounting and Security Reform are optional institutional choices, once per crisis instead of once per game.
  Public Accounting lowers pressure by 10, and Security Reform lengthens the post-crisis rest from 180 to 365 days.
- Closure sends one short recovery report (`chaosx.nr31.9`, existing reconstruction art), finalizes the player's achievement checks (so The Long Watch can count contained crises), sets a timed `random_terror_recovery_cooldown` that ordinary waves respect but a deliberate Global Jihad scenario may override (Part 1: "unless a connected transnational network deliberately re-enters it"), and resets every per-crisis marker, including the six named in the assessment and all mission outcome flags.
- Defects fixed on the way: Support Victims also set a permanent copy of its 60-day commitment flag, and Public Accounting and the response-cell AI read a failed-raid country flag that is only ever set on states; they now read `random_terror_failed_raid_memory`.
- Restore Services keeps the one-row rule on the priority recovering state.

### R31 Per-crisis and per-target guards replace once-per-game locks (`d58858f2a`)

Basis: the matrix cleanup column (Establish Response Cell "remove after final recovery", Negotiate Surrender "one settlement per actor", Expose and Quiet Leverage "evidence consumed or archived" and "closes on exposure or sponsor change", Absorb "transactional", Contest "clear contest state after result", Foreign Fighters "bounded intake, cooldown, no free loop", Join "leave or split only through valid route"), and the wiki rule that `fire_only_once` on a targeted decision locks each target for the rest of the game, which reused carrier tags and repeated crises turn into permanent locks.

- Establish a Response Cell is once per crisis through `random_terror_response_cell_active`, reset at closure (R30).
- Expose the Sponsor and Pressure the Sponsor in Private are alternatives on one evidence package.
  Either consumes the state's evidence marker, and the public case condemns each sponsoring country once through its own `random_terror_sponsorship_condemnation_recorded`.
  Expose was hidden whenever private leverage was available, which every evidence incident made true, so the public option was almost never offered; both now show on the same evidence.
- Negotiate an Enclave Surrender is one settlement per armed command, read from `random_terror_negotiated_surrender`, which actor runtime cleanup now clears with its disarmament terms.
- Absorb, Contest and Join keep one transaction in flight per target and remember a refusal or challenge per target with `<flag>_@<tag>` records, cleared in both directions when either command retires.
- Recruit Foreign Fighters sets its flag for `foreign_fighters_cooldown_days` (180) through a `meta_effect` literal instead of permanently.
- Terminal Counteroffensive and Accelerate the Revelation keep `fire_only_once`, because the terminal stage happens once per world.

### R32 The incident report names its state, family and losses, and asks for a first emphasis (`8f232f358`)

Basis: Part 1 Opening shock ("one visible attack report tied to an exact state" that "establishes civilian harm, state damage, the apparent incident family, and the government's immediate choices"), Part 1 Assessment (protection, intelligence, victim support or rapid coercion, changing the available actions and the first operation without locking a doctrine), and Part 11's demand for exact state and incident context.

- The report text follows the nine family groups of the picture selector plus its fallback, so text and art never disagree; the measured loss is the exact population loss already applied by the incident, and no number is shown when none was measured.
- The four emphases each last 90 days, add a timed country modifier reusing the matching government decision icon (vanilla also uses decision sprites for dynamic modifiers, for example `yellow_river_blown`), and set a timed flag read by the matching decision family.
  Each also has an immediate bounded effect on the reported state or on Response Legitimacy, with every value in the new `random_terror_emphasis` constants.
- The hooks were chosen where the existing action already exists, so no new decision is added: Protective Cordons reuse the transport-protection odds for attacks on crowds and routes, Intelligence Priority opens Intelligence Sweep before a response cell and lifts the first raid by one band, Relief First keeps Support Victims beside a response cell and lets it weaken active cells, and Rapid Crackdown deepens Security Surge.
- Later reports of the same crisis keep the single acknowledgement option.
- Community rejection keeps the fallback picture but gets its own report text, because the fallback text describes the network claiming a district.
- Each `random_terror_choose_emphasis_*` effect sets its own `random_terror_emphasis_duration` temp variable before using it; the shared begin helper only sets `random_terror_emphasis_chosen`, so no temp output crosses a scripted-effect return.
- Route evidence: `hoi4.probability_inspect` with the `event_option_ai_chance` adapter returned "Invalid tool arguments" both with `candidatePool = ["chaosx.nr31.2"]` and with no other argument, and `hoi4.event_inspect` returned the same error for narrow `lint` and `trace` queries on `chaosx.nr31.9` and `chaosx.nr31.97`; the new option weights are reviewed in source only.

### R33 Cells spread between states and across borders, survivors scatter, and distant attacks leave traces

Basis: Part 2 Cross-state spread ("Spread requires a reason", the `90`-day anchor, "one new hotspot at a time") and Cross-border spread (common only after Evolution II, the receiving country gets its own opening report, no transfer of the source government's decisions or costs), Part 2 acceptance cases 6 and 7, Part 4 Evolution I Survivor displacement and Evolution II Network Reach and Distant demonstration attacks, and validation case V03 Cross-state spread.

- Spread runs inside the existing event-owned country pulse, not a new on_action or world scan, and opens at most one new hotspot per government per window (90 days, 60 at high Network Reach), stored as a date through `chaosx_convert_days_to_date_offset`.
- Every new hotspot goes through `random_terror_apply_incident`, so stage, report, hotspot count, recovery check and pulse need no second path, and containment and corridor missions can now fail on a real new hotspot.
- Sources: Entrenched or worse with any reason, Active with a recorded reason, or any state with remaining activity whose survivors were scattered.
  The third case extends the lead's wording so that a raid that knocks a cell down to Dormant can still scatter its survivors, which Part 4 describes as the point of displacement.
  Bordering actor territory counts only for Entrenched or worse sources, because it is geography rather than a recorded incident.
- The copycat and training-area markers were set but never read; they now count as spread reasons and clear when the state returns to Clear, so an old marker cannot revive a cleared state's spread.
- Odds are one `random_list` of constant weights (35 open against 65 hold); scattered survivors double the open weight, Evolution I multiplies it by 1.25, and containment, transport protection and Security Surge each halve it, while Movement Restrictions block spread and distant attacks.
- Domestic and foreign targets are weighed 70 to 30 when both exist, so cross-border spread is possible after Evolution II without becoming the usual result.
- Survivor displacement follows the lead's acceptance (partial or costly raid, Security Surge without an intelligence breakthrough) rather than Part 2 acceptance case 7's failed raid, because a failed raid leaves the cell in place; a defection channel or allied intelligence on the state prevents it.
- A distant attack is rarer and costlier than local spread, as Part 4 requires: it needs Evolution II, Network Reach above the high gate and a 120-day global window, has weight 8, costs 5 Network Reach, and leaves only a Dormant trace unless the attack itself records a reason for a cell to stay.
  Its single `random_country` selection runs only after the roll succeeds, the same cost as one wave-target selection.
- The report names the origin state and the strongest reason, and the government category shows whether a cell can move, which keeps the player able to understand each change.
- Route evidence: the probability route stayed blocked as recorded under R32, so the new spread weights are reviewed in source only.

### R34 One sponsor check for every sponsorship path

Basis: the lead's defect report (Seek a Sponsor lacked the `has_war_with` exclusion its focus counterpart had, so a parent at war with its own insurgents could pay to supply them) and Part 10's rule that Event 14 cannibal countries are never Event 31 sponsors or partners.

- `random_terror_sponsor_candidate` is the single check used by the decision's `visible`, `available` and `target_trigger`, by Identify the Sponsor (`random_terror_focus_sponsor_candidate` now only calls it), by `random_terror_commit_sponsor_request` and by the accept option of `chaosx.nr31.42`.
- It excludes countries at war with the command, the command's parent and cannibal countries.
  The consent event reads the relationship against `FROM`, because there the asked country is `ROOT`; the pending-offer check applies only on the asking side, because the asked country holds that flag while it answers.
- The requirement tooltip now states every real condition instead of the old Network Authority wording, which no check read.

### R35 One uprising per state per window, not one per game

Basis: the decision matrix row for Call a Coordinated Uprising ("one uprising per target window") and the lead's finding that `random_terror_uprising_recent` was cleared only by mission success or actor cleanup, so a partial, failed or cancelled defence locked the state for good.

- `random_terror_uprising_recent` now means only that a rising is under way; `random_terror_finish_uprising_mission`, which every success, partial, failure and cancellation path calls, clears it, and so does crisis closure for the owner's states.
- The 28-day date window is the only lasting limit, read through one trigger, `random_terror_state_uprising_window_open`, in the decision's three blocks, the transaction check, the focus host check and the uprising start.

### R36 Live actors join the shared special-country classifier

Basis: Part 10 Special-country classifiers (one generic actor marker in the shared special-country trigger).

- One OR entry, `random_terror_is_actor = yes`, was added to `is_special_chaos_country` with a minimal edit; it covers live commands only, because the trigger requires the actor flag without the cleanup flag.
- Actors stay out of `is_actual_nonhuman_country`, and governments with Terror Pressure are not classified.

### R37 Response Capacity improves raids and sweeps, and part of it lasts

Basis: Part 3 (Establish Joint Response Cell creates coordination capacity; intelligence-led responses depend on capacity) and Part 1 (clean containment gives a limited long-term counterterror capacity); the lead found the value written but never read, and cleared by the same closure Security Reform causes.

- Capacity raises the clean-success weight of every Targeted Raid band (3 per point) and deepens Intelligence Sweep (1 more activity per point), counting at most 6 points, all in the new `random_terror_capacity` constants.
  A weight bonus was chosen over a band jump so that every point matters and the abusive and failure weights stay as tuned.
- The response cell adds 2 more capacity than an ordinary response, so it is the coordination step Part 3 describes.
- Security Reform adds 2 lasting capacity and a clean containment adds 1, capped at 4 in all; closure resets the crisis capacity to that lasting value instead of clearing it.
- The header and the response cell, Security Reform, Intelligence Sweep and Targeted Raid tooltips state the values.
- Route evidence: the raid weight change is probability-bearing; the probability route stayed blocked as recorded under R32, so it is reviewed in source only.

### R38 Objective-based final strengths and the opening uprising wave (amends D12)

Basis: Part 8 Final state ideas ("should change as the final campaign advances or loses key objectives" and "should not give unlimited power at full strength regardless of world state"), Extreme abilities, Uprising system ("a country with zero pressure and no active cell cannot receive a full rebel army"), Phase 1 and Global counterplay, and the accepted improvement-review item "Objective-based world-end power".
D12 settled only the size of the government action budget; it is amended, not replaced: the single Terminal Counteroffensive row stays, and the final strengths and the uprising wave are added beside it.

- The three static spirits became variable-driven dynamic modifiers on the final command, recomputed by one event-owned hidden terminal check every 30 days, so values scale smoothly instead of jumping between idea tiers.
  The spirits stay defined for the jihadist Seal the Final Command and Deny the False Revelation focuses, and the terminal transition removes them so no strength is counted twice.
- Presence of the Entity reads the command capital (40 of 100 points), surviving commands holding their capitals and International Unity; losing the command capital lowers it at once through an `on_state_control_changed` callback that exits on the terminal flag.
- World in Revolt reads governments above Terror Pressure 70 through a new bounded list of affected governments (`global.random_terror_affected_countries`) and surviving commands; Supply Through Ruin reads controlled ports, states with infrastructure above 3, and External Supply.
- Floors (20, 15, 15) and the cap (100) live in constants; at full strength the modifiers exceed the old flat spirits, and at the floor they are a small fraction of them.
- The Ambiguous Light now adds 10 points to each strength instead of re-adding the flat spirits, and Seal the Final Command adds 10 to Presence.
- The uprising wave runs at the world-end transition only for governments with Terror Pressure above the uprising gate and a pressured active state, and gives them the existing Stop the Coordinated Uprising mission where a slot is free.
- Route evidence: the strength weights are not AI or random weights; no probability route was needed.
