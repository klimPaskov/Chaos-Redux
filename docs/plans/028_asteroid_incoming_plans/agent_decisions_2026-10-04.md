# Event 028 agent decisions, 2026-10-04

Disposition: accepted and implemented unless an entry says otherwise.
Acceptance basis: the user granted the implementing agent full design authority for Event 028 and asked for the recommended, spec-consistent option to be recorded here instead of asking for input.
Each entry names the spec basis and the commit or source surface that implements it.

## Crater actions

### Supplied crater garrison

Decision: a supplied garrison is at least one of the acting country's divisions in the crater state, or in an ordinary neighbouring state the actor controls that has a rail connection from the actor's current capital.
Basis: Part 6 asks for "supplied divisions in or adjacent to the crater".
The installed `triggers_documentation.md` has no trigger that reads a division's supply status, and neither COMBATANT nor state scopes expose one, so the capital rail link is the closest supported test.
The check follows `asteroid_incoming_state_has_capital_rail_route` and lives in `asteroid_incoming_crater_has_supplied_garrison` (`common/scripted_triggers/028_asteroid_incoming_crater_triggers.txt`).
The same garrison rule gates Secure the Crater Perimeter and Prepare a Crater Offensive.

### Perimeter ownership

Decision: a secured perimeter belongs to the country that secured it and lapses when another country takes control of the crater.
A new controller must secure the site again before it can survey it, while the survey record and its one-use research bonus stay on the state permanently, so changing controllers cannot farm the survey.
Basis: Part 6 exploit control "crater security actions cannot be farmed through rapid controller switching".

### Fortifying access states

Decision: Fortify Crater Access improves at most `asteroid_incoming_crater.access_state_limit` (two) neighbouring ordinary states the actor controls.
Each gains one infrastructure level when below the infrastructure cap and one fort level in every province whose fort is below the fort cap.
Each access state can be fortified once across all crater sites.
The old every-neighbour infrastructure loop is removed.
Basis: Part 6 "builds or repairs defenses and supply in neighboring normal states; the crater itself remains unusable".
Forts are province buildings, so the construction uses the province selector shown in the wiki `add_building_construction` row and vanilla focus precedents.

### Rival actions

Decision: reconnaissance grants army intelligence on the crater's controller, disruption applies a timed local-supply modifier to up to two hostile-held access states, and the offensive plan applies a timed attacker-only attack modifier to the actor's battles in the crater state.
Rival actions no longer require the actor to control the crater, which made them impossible before.
Basis: Part 6 "gather intelligence, affect local supply, or guide AI strategy; no free war goals or ownership transfers".

### Paid costs are shown as costs

Decision: command power for the security and survey actions and manpower for the fortification action appear in the cost text with the other paid costs, instead of as separate requirement lines.
Every crater action stays within four spendable cost types.
Basis: Part 6 "a requirement is not a hidden fifth cost" and "no action may have more than four spendable cost types".

### Crater competition alongside dust protection

Decision: crater actions open once the country's own emergency and reconstruction actions are closed, even while global dust remains.
Global dust can last for more than a year, and holding crater competition behind it hid the Extraordinary Minerals actions for most wars.
Basis: Part 6 Phase 4 is "visible only when Extraordinary Minerals is active and the country controls, borders, or is at war over a crater site" and does not wait for Phase 3 to end.
No `ai_will_do` block changed; only decision visibility widened.
