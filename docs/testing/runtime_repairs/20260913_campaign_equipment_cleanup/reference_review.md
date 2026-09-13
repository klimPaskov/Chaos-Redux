# Campaign error repair references

The user authorized fixing the errors in attachment `0bbafcb8-4032-4160-88fa-ad3c3f2ca4e2/pasted-text.txt`.
No live-game launch, console interaction, computer control, or additional log search is part of this repair pass.

## Soviet State checks

Installed `documentation/triggers_documentation.md`, sections `exists` and `scope_exists`, distinguishes a Country existence test from an existence test usable in any scope.
The offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` and `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` are the parallel syntax references.
The eight edited helpers are explicitly documented as State helpers and are reached through selected-State targets or State iterators.
Owner, controller, launcher, response-country, and breakaway-country existence tests remain Country checks.

## Missile industrial access

Installed `documentation/triggers_documentation.md`, section `building_count_trigger`, permits State and Country scopes and lists `arms_factory`, `industrial_complex`, and `dockyard`.
Its `num_of_factories` section permits Country scope only.
The offline Triggers snapshot gives the same State building-count distinction.
Vanilla `common/scripted_effects/ITA_scripted_effects.txt:3114` uses an OR of the three factory types when selecting an industrial State.
The existing missile industrial-access bonus is 8 in `common/script_constants/032_missiles_constants.txt`.
This repair changes the predicate to local industrial access without changing score constants.

## Missile strategic-region intersection

Installed `documentation/triggers_documentation.md`, section `any_state_in`, requires one of `array`, `continent`, `ai_area`, or `strategic_region`.
The offline Scopes snapshot gives the same category-selector contract.
The `is_in_array` section and offline Data structures snapshot document array membership checks, including a State scope as the value.
Vanilla `common/decisions/RAJ_GOE.txt:443` checks a State with `is_in_array = { array = RAJ.owned_states_at_game_start value = THIS }`.
The replacement selects States in one strategic region and then tests membership in the launcher Country's one-State array.
The selected region still comes from the first matching iteration.
The installed effective region files have 304 distinct IDs, exactly 1 through 304, with no gaps or duplicates, matching the existing probe bounds.
The mod has no `map/strategicregions` overrides.

## Convoy getter

Installed `documentation/dynamic_variables_documentation.md`, section `num_equipment`, documents the equipment-count getter and an equipment token argument.
Vanilla `common/units/equipment/convoys.txt` defines `convoy` as the archetype and `convoy_1` as its concrete equipment type.
The pasted engine diagnostic explicitly says free convoy counts are tracked by archetype and that it substitutes the archetype for the concrete type.
Both the exile eligibility predicate and its scripted cost presentation therefore use `num_equipment@convoy`.
Concrete convoy types used by stockpile effects remain valid and were not changed.

## Cleanup guards

Installed trigger and effect documentation define same-scope `has_dynamic_modifier` before `remove_dynamic_modifier`, and `has_event_target` before clearing a saved global target.
The Sweden worker handoff records the exact vanilla precedent, changed cleanup calls, recovered original-byte proof, and MCP projection limits.

## Skills

`chaos-redux-events` and `chaos-redux-subagents` guide this repair pass.
No skill was created or changed.
Only Sol and Luna specialists were delegated bounded work.

## Ethiopia equipment prerequisite

Installed `common/technologies/support.txt:20` defines `tech_support` with `enable_equipments = { support_equipment_1 }`.
Installed `common/units/equipment/support.txt` defines the support archetype and its concrete type, whose definition has no unconditional `active = yes`.
Installed `history/countries/ETH - Ethiopia.txt:139` starts Ethiopia with infantry weapons, mountaineers, trucks, and basic trains, without `tech_support`.
The installed `support_weapons` technology enables fire-support subunits, so it is not the equipment prerequisite used for this repair.
The mod descriptor only replaces loading screens, so these vanilla definitions remain effective.
Installed `documentation/effects_documentation.md`, section `set_technology`, supports Country scope and documents `popup = no` for a silent setup grant.
The equipment worker handoff records the final owning spawn path and prerequisite ordering.
