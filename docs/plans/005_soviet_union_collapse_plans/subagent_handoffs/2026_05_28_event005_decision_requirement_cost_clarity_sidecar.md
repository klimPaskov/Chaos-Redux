# Event005 decision requirement and cost clarity sidecar

## Scope

- Subagent role: Chaos Redux decision and mission sidecar.
- Task scope respected: only Event005 decision localisation was changed.
- Files changed:
  - `localisation/english/005_soviet_collapse_moldova_route_decisions_l_english.yml`
  - `localisation/english/005_soviet_collapse_l_english.yml`

## Changed ids

- Moldova route cost localisation:
  - `mol_soviet_collapse_prut_statute_cost_text`
  - `mol_soviet_collapse_prut_statute_cost_text_blocked`
  - `mol_soviet_collapse_romanian_mission_cost_text`
  - `mol_soviet_collapse_romanian_mission_cost_text_blocked`
  - `mol_soviet_collapse_sfat_veto_cost_text`
  - `mol_soviet_collapse_sfat_veto_cost_text_blocked`
  - `mol_soviet_collapse_dniester_line_cost_text`
  - `mol_soviet_collapse_dniester_line_cost_text_blocked`
  - `mol_soviet_collapse_customs_board_cost_text`
  - `mol_soviet_collapse_customs_board_cost_text_blocked`
  - `mol_soviet_collapse_patronage_limits_cost_text`
  - `mol_soviet_collapse_patronage_limits_cost_text_blocked`
- Core breakaway requirement tooltips:
  - `soviet_collapse_seize_depots_req_tt`
  - `soviet_collapse_coordinate_fronts_req_tt`

## Before and after behavior

- Before: Moldova route decisions displayed prose cost strings such as `Costs 45 Political Power and 10 Command Power.`, which was inconsistent with the Event005 icon-first cost style and the decision-mission spec.
- After: Moldova route decisions show icon-first cost text with matching red blocked variants for political power, command power, fuel, infantry equipment, support equipment, trains, and convoys.
- Before: `soviet_collapse_seize_depots_req_tt` described "officers, command authority, unsecured depot ledgers" without naming the actual visible costs or pressure gate.
- After: it names the army XP, command power, depot-control cap, and war or exposed-depot gate.
- Before: `soviet_collapse_coordinate_fronts_req_tt` said "fuel, support equipment, unfinished League coordination work" without exact icon-first values or the coordination cap.
- After: it names the fuel, support equipment, League Coordination cap, and faction or Free Republics' League requirement.

## Decision category lifecycle notes

- `soviet_collapse_breakaway_category` remains lifecycle-gated by active collapse, breakaway flags, faction/League state, and route flags.
- `soviet_collapse_moldova_route_decisions.txt` logic was not changed; route visibility and cooldown behavior remain as previously implemented.

## Mission quality notes

- No timed mission behavior was changed.
- Relevant decision-quality issue: the patched surfaces are active decisions, not passive missions. They already consume non-PP resources or route gates; the local weakness was player-facing clarity.
- Duplicate risk: low for this patch. The changed texts do not introduce new decisions, missions, timers, or effects.

## Cost and requirement clarity notes

- Moldova costs now follow icon-first cost localisation and have blocked variants.
- `soviet_collapse_seize_depots` and `soviet_collapse_coordinate_fronts` now expose the real resource and gate requirements more clearly instead of vague prose.

## AI validity and route-lock notes

- No AI weights or route locks were changed.
- Existing AI targeting and route gates remain unverified beyond text consistency because scripted triggers/effects/constants were explicitly out of scope.

## Localisation and tooltip gaps

- Remaining broader gap: some other Event005 decision cost strings outside this narrow patch still use prose or mixed "Requires" wording. I did not rewrite them because the task asked for one or two local improvements.

## Cleanup and exploit-risk notes

- No cleanup hooks, cooldowns, stockpile effects, or exploit surfaces were changed.
- No new free-unit, equipment-farm, war-goal, core, or cooldown loop risk was introduced by this localisation-only patch.

## Validation

- Ran targeted text checks after patch:
  - `rg -n "mol_soviet_collapse_.*cost_text|soviet_collapse_seize_depots_req_tt|soviet_collapse_coordinate_fronts_req_tt" localisation/english/005_soviet_collapse_moldova_route_decisions_l_english.yml localisation/english/005_soviet_collapse_l_english.yml`
  - `xxd -p -l 3 localisation/english/005_soviet_collapse_moldova_route_decisions_l_english.yml`
  - `xxd -p -l 3 localisation/english/005_soviet_collapse_l_english.yml`
- Both edited localisation files still report `efbbbf`.
- Skipped full HOI4 launch validation; not available from this subagent context and this was a localisation-only sidecar.

## Remaining risks

- The exact dynamic gate names for exposed depot pressure and League coordination caps remain controlled by existing scripted triggers/constants; I did not edit those files per scope.
- The repository had unrelated dirty changes before this sidecar. This patch does not revert or normalize them.
