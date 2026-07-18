# Event 019 controlled combat trials handoff, 2026-07-16

## Outcome

The four exact-formation combat achievements have an obtainable controlled-trial route:

- `019_infantry_spawn_one_battalion_wonder`
- `019_infantry_spawn_combined_arms_accident`
- `019_infantry_spawn_borrowed_future`
- `019_infantry_spawn_barracks_of_babel`

The approved route is a state-targeted one-versus-one border war. It replaces the retired ordinary-battle casualty and enemy-ratio tuple. No casualty value, force ratio, country combat aggregate, or leader-wide result is fabricated.

## Runtime identifiers

Player and AI countries use the same four decisions and the same shared launch effect:

- `infantry_spawn_achievement_one_battalion_combat_trial`
- `infantry_spawn_achievement_combined_arms_combat_trial`
- `infantry_spawn_achievement_borrowed_future_combat_trial`
- `infantry_spawn_achievement_barracks_of_babel_combat_trial`
- `infantry_spawn_achievement_start_combat_trial_from_target_state`
- `infantry_spawn_achievement_combat_trial_mission`

The border-war callback events are:

- attacker win, loss, cancel: `chaosx.nr19.920`, `.921`, `.922`
- defender win, loss, cancel: `chaosx.nr19.923`, `.924`, `.925`

Defender callbacks do not depend on `FROM.FROM`. They validate the opponent flag and nonce, resolve the frozen `infantry_spawn_achievement_combat_trial_opponent_attacker` country-ID variable, revalidate the attacker's nonce, type, and defender-country ID, then call the attacker-root handler. Duplicate callback order is harmless because resolution is idempotent.

## Exact participant and signature proof

The selected attacker state must be owned and controlled by the initiating country. It must contain exactly one division owned by that country and no allied or foreign division. That sole division must be an active Event 19 ledger unit whose unit, generation, lot, template, material-quality, coherence, composition, and disqualification evidence agree.

The launch transaction scans the full immutable component ledger against the live locked template, freezes the exact unit, generation, lot, template, attacker state, defender state, defender country, trial type, and a country-local nonce, then marks only that exact ledger division. The attacker-win path repeats the exact ledger, component, and Borrowed Future technology-gate checks before setting only the selected achievement-ready flag.

The defender state must be passable, empty of every division, and owned and controlled by a different peaceful independent AI country. The opponent cannot be an Event 19 participant, derivative, special Chaos country, faction ally, war enemy, existing trial opponent, or cleanup quarantine. A one-state or microstate opponent remains safe because `change_state_after_war = no` prevents territorial transfer.

The defender receives one locked one-infantry-battalion template named `Event 19 Controlled Trial Detachment`. Recruiting from it is forced off. Exactly one unit is created with ID `1919019019` and receives the defender marker, nonce, trial type, attacker country ID, and create-unit ID. Both states are proved to contain their literal sole expected division before the border war starts and again before a win can award.

## Balance and per-achievement gates

All started trials use combat width 80, one province per side, a 14-day engine-enforced minimum duration, a 45-day timeout mission, and a 90-day shared cooldown.

| Trial | Composition and technology | Material | Coherence | Strength | Organization | Army XP | Command Power |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| One Battalion | exactly one recorded combat battalion | poor, 2 | absurd, 2 | 90% | 75% | 15 | 10 |
| Combined-Arms | Evolution III random, at least eight distinct combat-component types | mixed, 3 | strained, 3 | 90% | 70% | 25 | 15 |
| Borrowed Future | advanced generated formation with at least one recorded gate still locked | mixed, 3 | strained, 3 | 85% | 65% | 20 | 15 |
| Barracks of Babel | Evolution III random with camelry, bicycle infantry, amphibious armor, a flame element, artillery, and engineers | serviceable, 4 | strained, 3 | 95% | 80% | 30 | 20 |

Costs are debited only after both states report a live border war. Pre-start failure costs nothing and does not apply the cooldown. Every started win, loss, cancel, invalidation, or timeout applies the same cooldown. AI uses the same target triggers, resource checks, quality gates, launch transaction, callbacks, and cleanup as the player, with `infantry_spawn_factor.tenth` as the decision weight.

## Cleanup and anti-farm behavior

Win, loss, cancel, timeout, state ownership change, civil war, outside war, extra-division entry, missing identity, and country teardown converge on the shared cancel or cleanup effects.

Opponent cleanup requires exactly one division with the expected defender marker, nonce, attacker ID, and create-unit ID. `delete_unit` filters by both `Event 19 Controlled Trial Detachment` and the create-unit ID, with no disband refund. The unique template is then removed. A post-removal scan must prove zero nonce-marked defender divisions and `has_template = no` before the opponent flag and frozen variables are cleared. Missing, duplicate, or residual evidence sets `infantry_spawn_achievement_combat_trial_cleanup_quarantined` and retains the opponent lock.

The attacker marker is cleared only through the immutable unit-row scope after unit, generation, lot, template, and nonce agreement. The transaction never increments Event 19 generations, lots, unit totals, wars, deaths, evolutions, Event Log entries, derivative records, or `world_end`. The ordinary `on_army_leader_won_combat` path remains unused. No recurring world or all-country on-action was added.

## Files changed by this tranche

- `common/script_constants/019_infantry_spawn_achievement_constants.txt`
- `common/scripted_triggers/019_infantry_spawn_achievement_triggers.txt`
- `common/scripted_effects/019_infantry_spawn_achievement_effects.txt`
- `common/decisions/019_infantry_spawn_decisions.txt`
- `events/019_infantry_spawn.txt`
- `common/on_actions/019_infantry_spawn_achievement_on_actions.txt`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/achievements/019_infantry_spawn_achievements.md`
- `docs/events/019_infantry_spawn.md`
- `docs/specs/019_infantry_spawn_specs/matrices/019_achievement_matrix.md`
- `docs/specs/019_infantry_spawn_specs/review/blockers_and_uncertainty.md`
- this handoff

No Chaos unit registry callback, provider file, registry constant, registry row, scenario registration, event catalog workbook, or visual asset file was changed. The decisions reuse `GFX_decision_infantry_spawn_training_cycle`.

## Validation evidence

- Official `start_border_war`, `cancel_border_war`, `delete_unit`, `delete_unit_template_and_units`, `set_division_force_allow_recruiting`, unit trigger, state-target decision, and script-constant documentation was checked alongside vanilla WTT border-war decisions.
- Each callback event ID `.920` through `.925` has one event block. The six start callbacks and the three validated defender forwards map to the intended win, loss, and cancel handlers. No `FROM.FROM` remains in the Event 19 callback file.
- The six touched Clausewitz script files have balanced blocks. Scoped diff whitespace checks are clean. No unsupported comparison operator or literal negative debit multiplier remains.
- Both touched English localisation files retain UTF-8 BOM. Every new decision, mission, cost, target, achievement description, and achievement tooltip key exists exactly once. The four player-facing contracts contain no casualty, force-ratio, or significant-battle claim.
- Source-of-truth achievement and blocker documentation now records the approved controlled trial. Earlier B-019-002 blocked findings in historical handoffs are superseded by this implementation and this dated handoff.

`hoi4.event_inspect` could not produce its read-only lint artifact because the configured MCP artifact store had reached its retention limit. It returned no source diagnostic. Static validation and direct official-documentation comparison were completed instead.

## Simplifications, omissions, and remaining risk

No gameplay fallback or simplification was used. The approved controlled trial is the achievement contract, not a proxy for unobservable ordinary combat. No requested composition route, AI path, cost, cooldown, timeout, outcome, cleanup proof, localisation surface, or documentation surface was omitted.

The remaining validation limitation is the unavailable MCP lint artifact noted above. No unresolved implementation defect was found in the bounded combat-trial surface.
