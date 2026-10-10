# 007 Fury decisions and missions specification

## Category roles

`fury_war_office_category` (Fury War Office) exists for Fury actors and is used by the AI, because Fury never selects a player.
It can display if a player uses console or tag switching, but ordinary gameplay never grants it to the player.
It controls target selection, finite reserve deployment, occupation and compliance, coring, the cooperation or rivalry commitment, and terminal coordination.

`anti_fury_response_category` gives non-Fury countries a small response family after the major super-event or the world-end branch.
It appears only for countries bordering a Fury actor and for majors, and hides once every Fury actor is defeated.

Source: `common/decisions/007_fury_decisions.txt`, with costs in the `fury_decision_cost` script-constant block and payment adapters in `common/scripted_effects/007_fury_effects.txt`.

## Shared rules

- Fury values are internal AI drivers (see Part 1); tooltips describe consequences, not momentum or overextension numbers.
- Reach, Pact Cohesion, and numeric Compliance Drive are retired under the [accepted release corrections](007_fury_release_corrections_2026-10-05.md) and must not return as requirements or decorative counters.
- Costs use command power, rifles, support equipment, manpower, trains, army experience, and stability; political power is not a default cost.
- Every paid action quotes from central constants, rechecks its gates before payment, and refunds or retracts on a rejected settlement.
- Full hovers show every payment with independently calculated affordability colours, while compact rows show at most three components.
- The category shows only decisions that matter now: one target decision when no target exists, occupation decisions only for owned non-core states, route decisions only while another Fury actor exists, and terminal decisions only during the world-end branch.
- Mission text names states and regions through scripted localisation, never raw state IDs.

## Fury War Office decisions

| Decision | Shown when | Cost family | Effect | AI use |
| --- | --- | --- | --- | --- |
| `fury_select_new_target` (Select the Next Target) | at peace, no current target, a valid neighbour exists, occupation pressure not extreme, overextension below the selection gate | command power | chooses the best-scoring legal neighbour and declares war | high, doubled at peace, zero at high pressure |
| `fury_open_forward_depots` | at war after `Depot Cadres`, with reserve remaining and a depot spawn state | 15 command power, 610 rifles, 40 support equipment, 6,300 manpower | releases one finite reserve column through the lifetime cap | medium, doubled at war |
| `fury_register_occupation_settlement` (Prepare an Occupied State) | before the occupation registers unlock, with an unregistered non-core state | command power, rifles, support equipment | registers one state, adds compliance and the Compliance Drive idea | medium, raised by overextension |
| `fury_count_captured_registers` | after registers unlock, with an unregistered non-core state | command power, rifles, support equipment | registers another state and adds compliance | medium, raised by high pressure |
| `fury_rail_registry_survey` | after `Rail and Occupation Supply`, with a registered state lacking rail registry | command power, trains, support equipment | marks rail registry, adds compliance, and relieves pressure | medium, raised by high pressure |
| `fury_core_state_by_administration` | after `Core by Administration`, with a high-compliance candidate and no extreme pressure | command power, rifles, support equipment, manpower | cores one state and relieves more strain | medium, raised by high pressure |
| `fury_core_state_by_march` | after `Core by March`, with a lower-compliance candidate | command power, rifles, manpower, stability | cores one state faster at a harsher price | low, raised at war, zero at extreme pressure |
| `fury_form_war_table` | Evolution II applied, no route chosen, a valid partner exists, no world-end | command power, rifles | cooperation route, project-pact membership for eligible partners, `Fury Pact Command` idea | low |
| `fury_mark_rival_column` | Evolution II applied, no route chosen, another Fury actor exists, no world-end | command power | rivalry route, `Rival Fury Doctrine` idea, momentum | low |
| `fury_share_terminal_reserves` | terminal actor with a valid recipient | command power, rifles, support equipment, manpower | delivers the actual paid vector to another terminal actor | medium, raised at war and high pressure |
| `fury_assign_terminal_fronts` | terminal actor during the world-end branch | command power, army experience | preparation, momentum, and overextension relief across terminal actors | low, raised at peace or with no neighbours |

The paid cooperation and rivalry decisions close during the terminal phase, and each locks the opposite focus route.

## Fury missions

| Mission | Activation | Fails when | Result |
| --- | --- | --- | --- |
| `fury_garrison_the_names_mission` | after `Garrison Occupied Towns`, with a registered state and no occupation crisis | the capital or a registered state leaves Fury control | success lowers pressure and adds compliance; failure raises resistance and overextension |
| `fury_restore_the_registers_mission` | while the occupation crisis is active | the capital or a registered state leaves Fury control | success relieves pressure strongly; failure adds pressure |

The crisis mission replaces the ordinary garrison mission while extreme pressure lasts, so at most one occupation mission runs.

## Anti-Fury response

| Decision | Shown to | Cost family | Effect |
| --- | --- | --- | --- |
| `anti_fury_border_watch` | a country bordering Fury | command power, rifles | starts `anti_fury_border_watch_mission`; success adds a defensive idea and lowers the neighbouring actor's momentum, failure raises it |
| `anti_fury_start_supply_denial` | a country bordering Fury | command power, rifles | starts `anti_fury_supply_denial_mission`; success adds an idea, lowers momentum, and raises Fury overextension, failure relieves the actor's overextension |
| `anti_fury_firebreak_staff_talks` | any eligible responder | command power, army experience | temporary staff-talks idea without forming a faction |
| `anti_fury_send_emergency_aid` | a responder while a Fury actor attacks a non-player-linked target | command power, rifles, support equipment, trains | delivers equipment to the target, lowers the attacker's momentum, and starts `anti_fury_aid_route_mission`; failure returns the momentum |

Each mission fails if the sender's capital falls, and Border Watch and Supply Denial also fail if the Fury neighbour declares war on the sender.
The decision audit records an unresolved gap: none of the three missions checks supplied border divisions, rail access, or an open aid route, so success currently means waiting out the timer.
A proposed repair is in the README's open questions.

## Drafts not adopted

The original draft named several decisions that the implementation replaced or dropped.
They are listed once here so no agent rebuilds them from older prompts.

| Draft | Disposition |
| --- | --- |
| Find the Next Weak Neighbor | implemented as `fury_select_new_target` |
| Cut the Border Rail, Capital First Plan | not adopted; their intent survives as the `Motorised Supply Columns` and `Frontier War Plans` focus rewards without sabotage or capital targeting |
| Open the Depots | implemented as `fury_open_forward_depots` |
| Empty the Training Yards, Depot Cadre Conversion | not adopted; finite reserve refills come from `Depot Cadres` and `Depot Officers Without Leave` |
| Install the Settlement Office, Count the Captured Registers, Core the First Ring | implemented as the register, rail registry, and two coring decisions |
| Open Shared War Tables, Send Cadres to the Other Fury, Partition Before Victory | replaced by `fury_form_war_table`, the cooperation focuses, and reserve sharing; no partition |
| Mark the Rival Fury, Absorb the Rival Fire | implemented as `fury_mark_rival_column` and the rivalry focuses |
| Survey Beyond the Continent, Carry Orders Overseas | replaced by the world-end focus branch; Reach is retired |
| Border Survey, Recognition Denial | retired by the release corrections because their payments had no distinct consequence |
| Guard the Fury Capital, Secure the First Depot Belt missions | not adopted; the two occupation missions cover the same pressure |

## Cleanup

Decision cleanup must remove:

- the current target when the target dies or becomes invalid.
- route flags, pact membership, and missions when a Fury actor is cleaned up.
- registration and rail flags only through state transfer or coring, never by hidden rollback.
- anti-Fury missions and ideas after the Fury threat ends.
- scenario setup flags after launch.

No decision may remain visible for a dead target, protected invalid target, or invalid state.
