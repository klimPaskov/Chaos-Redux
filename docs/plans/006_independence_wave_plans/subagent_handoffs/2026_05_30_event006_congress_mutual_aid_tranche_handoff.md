# Event 006 Congress Mutual Aid Tranche Handoff

## Scope

Implemented a bounded New States Congress expansion for Event 006 Independence Wave. This tranche adds mutual guarantee and shared arms-pool actions for Event 006 releases without touching flag asset paths or Event 005 systems.

## Files Changed

- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`

## Identifiers Added

- `independence_wave_sign_mutual_guarantee`
- `independence_wave_open_congress_arms_pool`
- `can_independence_wave_sign_mutual_guarantee`
- `can_independence_wave_open_congress_arms_pool`
- `independence_wave_sign_mutual_guarantee_effect`
- `independence_wave_open_congress_arms_pool_effect`
- `independence_wave_congress_arms_pool_opened`
- `independence_wave_signed_mutual_guarantees`
- `global.chaosx_iw_mutual_guarantee_count`
- `chaosx_iw_mutual_guarantee_network`
- `global.chaosx_iw_congress_arms_pool_count`

## Behavior

- Event 006 releases with New States Congress access and sent delegates can target another delegate-sending Event 006 release to sign mutual guarantees.
- Mutual guarantee signing creates reciprocal `give_guarantee` effects, raises coalition cohesion and legitimacy on both sides, raises foreign attention, and tracks progress toward the five-link mutual-guarantee achievement flag.
- Congress delegates can open a shared arms pool once by spending infantry and support equipment.
- The arms pool raises militia strength, coalition cohesion, and legitimacy, giving the Congress a military cooperation action beyond flat political power spending.
- AI weights favor mutual guarantees for civic, anti-puppet, and wartime states while reducing enthusiasm for patron-cabinet routes.
- AI weights favor the arms pool during war, for revolutionary routes, and for compact members, while de-prioritizing it when militia strength is already above the initial baseline.

## Validation

- Brace balance clean for Event 006 constants, triggers, effects, decisions, and decision categories.
- No `<=` or `>=` found in touched Event 006 script files.
- `localisation/english/006_independence_wave_l_english.yml` remains UTF-8 with BOM (`efbbbf`).
- No `:0` localisation keys found in the Event 006 localisation file.
- No files under `gfx/flags`, `common/countries`, or `history/countries` are changed by this tranche.
- Vanilla precedent checked for `give_guarantee = FROM`, `has_war_with = FROM`, `has_equipment`, and `add_equipment_to_stockpile` with negative equipment amounts.

## Subagent Note

Attempted to spawn `chaosx_decision_mission_auditor` with `fork_context=false`, explicit paths, and the user correction, but the subagent tool rejected the spawn because the agent thread limit was reached. Parent-side validation was completed instead.

## Remaining Risks

- This tranche adds Congress decision-category actions, not the full scripted GUI Congress surface from the source spec.
- Mutual guarantee achievement tracking now sets the network flag after five signed links, but the broader achievement set still needs a final completion audit.
- Congress collapse, patron takeover, volunteer corridors, and full charter vote lifecycle remain later Event 006 work.
