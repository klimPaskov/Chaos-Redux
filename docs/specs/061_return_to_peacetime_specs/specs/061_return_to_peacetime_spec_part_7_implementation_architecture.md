# Event 061: Return to Peacetime

## Part 7: Implementation architecture and source map

## Architecture purpose

This part defines the implementation boundaries, state model, helper contracts, event chain, and expected repository surfaces.

It does not replace local vanilla and repository inspection.

Before writing engine-facing syntax, the implementation agent must inspect:

- the repository `AGENTS.md`
- the current Chaos Redux event, decision, asset, achievement, cluster, and Event Logs precedents
- the offline Paradox wiki pages for events, decisions, ideas and laws, buildings, units, scripted effects, scripted triggers, and localisation
- the installed Hearts of Iron IV documentation
- installed vanilla examples for law definitions, building conversion, safe scripted division disband, decision state targets, and country event scheduling

The uploaded planning bundle did not include those local references. Exact syntax remains a hard implementation gate.

## Expected source files

The final implementation should use event-owned files where the engine permits them.

Suggested map:

| Surface | Suggested file |
| --- | --- |
| Event chain | `events/061_return_to_peacetime.txt` |
| Decisions | `common/decisions/061_return_to_peacetime_decisions.txt` |
| Decision category | `common/decisions/categories/061_return_to_peacetime_categories.txt` |
| Event-owned ideas and staged spirits | `common/ideas/061_return_to_peacetime_ideas.txt` |
| New economy and conscription laws | event-owned law or idea file following the verified local law database pattern |
| Script constants | `common/script_constants/061_return_to_peacetime_constants.txt` |
| Event-owned scripted effects | `common/scripted_effects/061_return_to_peacetime_effects.txt` |
| Event-owned scripted triggers | `common/scripted_triggers/061_return_to_peacetime_triggers.txt` |
| Event-owned runtime scheduling | `common/on_actions/061_return_to_peacetime_on_actions.txt` only when a verified narrow hook is needed |
| AI strategy | `common/ai_strategy/061_return_to_peacetime_ai_strategy.txt` when strategy plans are needed beyond decision weights |
| Scripted localisation | event-owned scripted localisation file following repository naming precedent |
| Event and decision localisation | repository English localisation files following current event-owned conventions |
| GFX definitions | event-owned `.gfx` files following exact consumer precedents |
| Achievements | event section in `common/achievements/chaos_redux_achievements.txt` |
| Event Logs integration | shared `chaosx_events_log_effects.txt` and matching scripted localisation selectors |
| Random-event registration | shared event initialization effect |
| Cluster integration | shared cluster registry and authoritative catalog workbook |
| Event documentation | `docs/events/061_return_to_peacetime/` |
| Source specs | this directory |
| Working plans and handoffs | `docs/plans/061_return_to_peacetime_plans/` |

Do not place event-owned decisions, ideas, or effects into large shared legacy files when a dedicated file is supported.

## Event chain plan

The exact subevent numbering can change during implementation. Keep the entry event stable.

Suggested roles:

| Event | Role |
| --- | --- |
| `chaosx.nr61.1` | canonical global entry and cycle creation |
| `chaosx.nr61.2` | player-facing national baseline report |
| `chaosx.nr61.3` | AI national baseline handler when a separate hidden country event is needed |
| `chaosx.nr61.10` | bounded active-country reconciliation pulse |
| `chaosx.nr61.11` | ownership and ledger reconciliation helper event when direct effect scope is insufficient |
| `chaosx.nr61.20` | Swords into Ploughshares warning report |
| `chaosx.nr61.21` | Swords into Ploughshares resolution |
| `chaosx.nr61.30` | Great Demobilization warning report |
| `chaosx.nr61.31` | Great Demobilization resolution |
| `chaosx.nr61.40` | Permanent Peace settlement report |
| `chaosx.nr61.41` | Permanent Peace deadline resolution |
| `chaosx.nr61.42` | postwar settlement after active-war deferral |
| `chaosx.nr61.43` | final delayed division-demobilization reconciliation |
| `chaosx.nr61.50` | extreme-law recovery milestone report when a popup is justified |
| `chaosx.nr61.90` | bounded debug or validation report, hidden from normal play |

Do not create a player-facing popup for every hidden update.

## Global state

Suggested global state:

| Identifier | Role |
| --- | --- |
| `global.return_to_peacetime_cycle_id` | monotonically increasing normal firing identifier |
| shared evolution state for Event 61 | activation and enable state through the existing system |
| shared Event Logs arrays | global history and evolution entries |

The event does not need a permanent global readiness value.

## Country state

Suggested persistent country variables:

| Variable | Role |
| --- | --- |
| `return_to_peacetime_last_baseline_cycle` | idempotence guard |
| `return_to_peacetime_last_evolution_1_cycle` | stockpile resolution guard |
| `return_to_peacetime_last_evolution_2_cycle` | division resolution guard |
| `return_to_peacetime_last_evolution_3_cycle` | settlement resolution guard |
| `return_to_peacetime_readiness` | public 0 to 100 total |
| `return_to_peacetime_economy_restore_target_rank` | highest unresolved economy rank removed by the event |
| `return_to_peacetime_conscription_restore_target_rank` | highest unresolved conscription rank removed by the event |
| `return_to_peacetime_owned_ledger_total` | cached owned and controlled ledger total |
| `return_to_peacetime_current_cycle_converted` | national report value |
| `return_to_peacetime_total_restored` | current transition tracking and achievement support |
| `return_to_peacetime_pending_cycle_pressure` | merged warning intensity |
| `return_to_peacetime_structural_action_mask` | action-family proof for settlement |
| `return_to_peacetime_stockpile_value_removed` | Evolution I result and achievement support |
| `return_to_peacetime_divisions_demobilized` | Evolution II result |
| `return_to_peacetime_manpower_returned` | result value when measurable |
| `return_to_peacetime_settlement_deadline` | persistent settlement timing when the engine pattern needs it |
| `return_to_peacetime_reconciliation_generation` | stale scheduled-event guard when useful |

Suggested persistent country flags:

| Flag | Role |
| --- | --- |
| `return_to_peacetime_active` | country pulse and category gate |
| `return_to_peacetime_contracts_restarted` | institutional and industrial state |
| `return_to_peacetime_general_staff_restored` | full defence institution |
| `return_to_peacetime_meaningful_rearmament` | derived exemption result |
| `return_to_peacetime_national_program_complete` | stronger rearmament result |
| `return_to_peacetime_inventory_liquidation_active` | singleton mission guard |
| `return_to_peacetime_mustering_out_active` | singleton mission guard |
| `return_to_peacetime_defence_settlement_active` | singleton mission guard |
| `return_to_peacetime_war_deferral_active` | Evolution III deferral |
| `return_to_peacetime_emergency_used_this_cycle` | one-use guard |
| `return_to_peacetime_improvised_rearmament_active` | aftermath state |
| `return_to_peacetime_permanent_conversion_chosen` | route record |
| `return_to_peacetime_extreme_law_first_entry_economy` | cycle guard |
| `return_to_peacetime_extreme_law_first_entry_army` | cycle guard |
| `return_to_peacetime_pulse_scheduled` | duplicate pulse prevention |

Use variables or arrays instead of dozens of separate flags when the local project pattern provides a clearer bounded representation.

## State ledger

Suggested state variable:

`return_to_peacetime_converted_factory_capacity`

Suggested marker flag:

`return_to_peacetime_has_factory_ledger`

The marker exists only while the count is positive.

The state ledger is authoritative.

Country totals are caches for UI, AI, and validation. Rebuild them from owned and controlled states when ownership can have changed.

## Law ranks

Create one explicit rank helper for each law group.

The helper should map current token to a numerical rank and provide adjacent movement.

### Economy rank

| Rank | Law |
| ---: | --- |
| 0 | Peacetime Economy |
| 1 | Civilian Economy |
| 2 | Early Mobilization |
| 3 | Partial Mobilization |
| 4 | War Economy |
| 5 | Total Mobilization |

### Conscription rank

| Rank | Law |
| ---: | --- |
| 0 | No Army |
| 1 | Disarmed Nation |
| 2 | Volunteer Only |
| 3 | Limited Conscription |
| 4 | Extensive Conscription |
| 5 | Service by Requirement |
| 6 | All Adults Serve |
| 7 | Scraping the Barrel |

The helper must validate the active law group before movement.

The baseline floor is rank 1 for each group.

Evolution III can move to rank 0.

## Public helper boundaries

The implementation should ask `chaosx_scripted_system_architect` to review repeated logic before duplicating it.

Likely reusable helpers:

- get ordinary economy law rank
- get ordinary conscription law rank
- move economy law one validated adjacent step
- move conscription law one validated adjacent step
- compare current law with a stored target rank
- convert one military factory to one civilian factory and record a state ledger unit
- restore one ledger unit through the reverse atomic transaction
- calculate current owned ledger total
- safely debit a positive equipment stockpile amount
- safely disband an eligible conventional division and return its contents

### Shared helper rule

A helper belongs in the shared dynamic registry only when its contract is neutral and useful across event families.

Examples:

- validated adjacent law movement can support Events 61, 82, and 103
- exact factory conversion with a caller-owned ledger may support future economic events
- safe stockpile debit already has partial shared coverage

Event 61 orchestration, Readiness, evolution selection, mission scheduling, and its private ledger meaning remain event-owned.

Any new shared helper requires documentation in `chaosx_dynamic_effects.md` or the appropriate owner API documentation.

## Existing stockpile debit helpers

The supplied dynamic-effects registry documents positive debit helpers for:

- support equipment
- motorized equipment
- convoys
- trains
- infantry equipment
- plague bombs
- fuel

Event 61 can use the ordinary supported helpers for relevant conventional families.

It should not use the plague-bomb or fuel helper for Swords into Ploughshares under this design.

Artillery, anti-tank, anti-air, mechanized, armour, and aircraft need one of these outcomes:

- verified existing owner helper found in the repository
- new exact positive debit helper with a reusable neutral contract
- event-owned exact helper when engine support is narrow
- family excluded and recorded as blocked

Do not approximate unsupported family removal through an unrelated equipment token.

## Factory transaction helper contract

Suggested input:

- target state scope
- requested amount
- transaction direction
- caller cycle ID

Suggested outputs:

- requested amount
- completed amount
- shortfall amount
- current state ledger
- failure reason code

Baseline direction:

- military to civilian
- increment ledger

Restoration direction:

- civilian to military
- decrement ledger

The helper must validate every building level atomically.

The helper should never create a building from a zero or negative requested amount.

## Readiness calculation helper

One event-owned effect should calculate all five hidden pillars and write the clamped total.

Suggested contract:

1. clear temporary pillar variables
2. read current arms contracts and state ledger restoration share
3. read current economy law rank
4. read current conscription rank
5. read current defence institution state
6. read War Support and material-protection proof
7. add capped pillar points
8. clamp total to 0 through 100
9. set or clear meaningful rearmament according to total and structural proof
10. update qualitative category states

The helper should not change gameplay state beyond Readiness and its derived flags.

## Structural-action mask

Use a bit mask, array, or project-standard compact representation when supported.

Action families:

| Family | Counts for last chance | Counts as required physical or legal action |
| --- | --- | --- |
| Factory reopening | yes | yes |
| Economy law restoration | yes | yes |
| Conscription restoration | yes | yes |
| General Staff | yes | no |
| Cadre retention | yes | no |
| Stockpile protection | yes | no |
| Defence Ministry | yes | no |
| National Arsenal | yes | yes |
| National Rearmament Program | yes | no |
| Public defence campaign | no | no |
| Repeated action in same family | no additional credit | unchanged |

The settlement checks at least two families and at least one required physical or legal family.

## Decision target-pool helper

The state reopening pool should rebuild from current valid states.

Suggested state score inputs:

- positive ledger
- available civilian factory
- core status
- current control
- damage
- supply or capital connection
- immediate occupation risk
- ledger size

Output no more than three human-visible state targets.

The AI can evaluate the full pool through the same score.

Do not store stale state event targets across ownership change without validation.

## Evolution scheduling helper

One event-owned scheduler should determine the next enabled unresolved evolution for a country and cycle.

Inputs:

- current cycle ID
- shared Event 61 evolution enable and activation state
- country last-resolved cycle values
- currently active singleton mission
- merged-cycle pressure

Rules:

- schedule only one visible evolution mission at a time
- skip disabled layers cleanly
- do not wait for a disabled earlier layer
- merge repeat cycles into an active matching mission
- after resolution, schedule the next enabled unresolved layer
- honor active-war deferral for Evolution III
- remain idempotent after save and reload

## Stockpile liquidation architecture

Recommended two-stage calculation:

### Stage 1: family eligibility

For each supported ordinary family:

- calculate current positive stockpile
- calculate reserve floor
- subtract floor
- clamp surplus at zero
- calculate family share from Readiness, war state, protection, and cycle pressure
- calculate exact requested debit

### Stage 2: debit and value

For each positive requested amount:

- call the verified exact debit helper
- record actual completed debit
- multiply actual debit by central family value weight
- add to hidden reconstruction value
- record broad family result for the report

Use actual completed amounts for rewards.

## Division demobilization architecture

Recommended stages:

1. build eligible unit set
2. apply hard exclusions
3. calculate dynamic target count
4. apply tiny-army and minimum-force caps
5. score candidates
6. protect explicitly retained units
7. select exact target count
8. revalidate each candidate
9. disband through verified safe route
10. record actual successful count and returned values
11. calculate Veteran Reintegration tier from actual result

A failed disband must not count toward the civilian benefit.

## New law lifecycle

### Peacetime Economy

- available to Event 61 through Evolution III
- can be forced or voluntarily selected through Event 61
- can be exited through Event 61 recovery or another valid law system
- its strongest Peace Dividend interaction ends when the country leaves it
- first-entry conversion is an Event 61 effect, not a repeatable modifier attached directly to the law

### No Army

- available to Event 61 through Evolution III
- can be forced or voluntarily selected through Event 61
- can be exited through the Service Registry path or another valid law system
- final conventional division demobilization is an Event 61 effect, not a continuously firing law effect
- owner-excluded special units remain under their owner contract

The law definitions should not contain hidden daily scripted cleanup.

## Industrial Reconversion Shock lifecycle

Use one idea family with three staged variants or one dynamic modifier when the local project pattern supports it cleanly.

Required properties:

- severe phase begins at baseline
- scheduled transition to middle phase
- scheduled transition to final phase
- repeat firing returns to severe phase
- total remaining duration cap
- high Readiness can mitigate part of later phases
- save and reload preserve the current stage and deadline
- category cleanup removes only the finished Event 61 state, not unrelated ideas

## Universal cost framework

Use the shared universal cost framework for:

- political power debit
- army experience debit
- temporary civilian factory commitment
- Stability debit when safely supported
- any other nonstandard transaction added during implementation

Every decision should define:

- visible cost
- blocked reason
- refund or cancellation rule
- completion recheck
- target invalidation behavior
- AI affordability rule

Do not handwrite several incompatible factory-commitment systems.

## Event Logs architecture

### History

The global entry calls the shared history recorder once.

Prepare aggregate variables before the call:

- affected country count
- total converted factories
- countries with economy-law change
- countries with conscription-law change
- countries with active reconversion shock

### Evolutions

Before recording an evolution milestone, set:

- `events_log_evolution_event_id = 61`
- event-owned type value for the evolution
- stage value
- tier value
- actor and actor-presence flag only for a genuine country actor row

Then call the shared recorder.

Disabled evolutions do not set recorded flags or unlock their content.

### Event Details

Add:

- one event catalog row for Event 61
- three evolution catalog entries
- correct type, Chaos level, cluster, and status
- no fake history metadata in catalog previews

## Random-event registration

During implementation:

- keep Event 61 in the repeatable array
- keep its ID stable
- make `get_event_type` resolve it as Minor Repeatable
- update visible and debug name mappings
- restore normal default enable status only when the rework is ready

The event uses the shared Minor Repeatable weight and cap behavior.

## Peace cluster implementation

Update the cluster registry and authoritative workbook:

- Cluster ID 4
- Peace
- member 9 as Low
- member 61 as High
- member order 9, then 61

The current exported duplicate `9, 9` must be corrected in the workbook and regenerated.

Cluster execution should:

- attempt White Peace first
- record its fired or skipped state
- execute Return to Peacetime second
- count as one pacing event
- preserve each member's own history and repeatable state

## Achievement implementation

Add all three achievements to the single Chaos Redux achievement registry.

Each needs:

- stable unique key
- persistent tracking
- disqualifier flags
- player-only completion check
- icon
- localisation
- documentation
- event-cycle and tag-continuity handling
- debug and live test case

Do not create a separate achievement database file with another unique ID.

## Asset implementation

For each planned asset:

1. inspect exact installed vanilla consumer and dimension
2. create an asset brief
3. generate or source through the correct asset subagent
4. retain provenance and processing evidence
5. create PNG preview and final DDS
6. wire through the event-owned or shared `.gfx` precedent
7. validate in game
8. promote durable manifest facts into permanent docs
9. remove temporary event-scoped asset workspace only after full acceptance

The main implementation agent owns final GFX and consumer wiring.

## Localisation implementation

Use final in-world wording.

Required groups:

- event name
- baseline national report
- evolution warnings and results
- category title and description
- every decision and mission
- every idea and law
- every blocked requirement
- Event Logs and Event Details text
- Peace cluster text
- achievements
- dynamic result lines

Spawn `chaosx_localisation_auditor` after the broad visible text exists.

Do not paste working labels, prompt text, raw variable names, or implementation notes into the game.

## AI probability implementation

Spawn `chaosx_ai_probability_auditor` for:

- decision `ai_will_do`
- voluntary Permanent Peace choice
- protection family selection when weighted
- state target selection when weighted
- disposition choice
- any option `ai_chance`

Use `hoi4.probability_inspect` before evaluation.

Use complete pools when options normalize.

Use the named scenarios in the probability research file.

Save evidence under the Event 61 plan or validation directory.

Source-only reasoning does not satisfy this gate.

## Required subagent routing

### Before broad editing

- `chaosx_repo_explorer` when file locations or current Event 61 surfaces are uncertain
- `chaosx_scripted_system_architect` for law, factory, stockpile, and safe-disband helper boundaries

### During implementation

- `chaosx_decision_mission_auditor` for category phases, costs, missions, cleanup, and AI usability
- `chaosx_generated_event_art` for report and category art
- `chaosx_icon_artist` for icon packages
- `chaosx_localisation_auditor` after final visible text exists
- `chaosx_ai_probability_auditor` for every weighted surface

### Near completion

- `chaosx_improvement_loop_planner` once, after a meaningful implementation tranche
- implement, merge, queue, or reject every returned item with a written reason
- `chaosx_documentation_curator` for source-of-truth alignment
- `chaosx_spreadsheet_doc_worker` for workbook and export alignment
- `chaosx_event_completion_auditor` before any completion claim

Every patch-capable subagent writes its event handoff under:

`docs/plans/061_return_to_peacetime_plans/subagent_handoffs/`

## Validation commands and tools

Use the repository-required checks discovered during implementation.

The minimum validation plan should include:

- event parser and structural validation
- decision and mission validation
- idea and law validation
- localisation-key validation
- sprite and DDS path validation
- Event Logs contract validation
- cluster registry validation
- achievement registry validation
- state ledger scripted tests
- law-rank scripted tests
- probability evidence
- save and reload tests
- live in-game debug playtest only when explicitly authorized through the debug-playtest skill

The debug-playtest skill is not invoked by this planning package.

## Catalog and status transition

The authoritative workbook row should remain `To Be Reworked` until implementation begins.

After implementation and repository validation, move it to the project status that accurately reflects the state, such as `Needs Testing`.

Do not mark it implemented before:

- final assets exist
- final localisation exists
- probability audit passes
- docs and workbook align
- completion audit closes all required surfaces

## Architecture acceptance conditions

The implementation architecture is satisfied only when:

- event-owned files hold event-owned logic
- shared helpers have neutral contracts and documentation
- state ledger is authoritative and country totals are caches
- law movement uses explicit validated ranks
- one readiness helper owns the derived total
- one scheduler owns evolution sequencing and disabled-layer skips
- one pulse runs only for active countries
- stockpile rewards use actual exact debit results
- division benefits use actual safe disband results
- new laws do not hide broad daily cleanup
- Event Logs record one global firing and valid evolution milestones
- cluster order and workbook export are corrected
- all visible assets and localisation are final before status promotion
- the required subagent and probability handoffs exist
- exact engine syntax is proven against the installed local references
