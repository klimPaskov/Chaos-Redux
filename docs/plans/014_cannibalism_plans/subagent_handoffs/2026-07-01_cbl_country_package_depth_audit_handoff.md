# Event 014 CBL Country Package Depth Audit Handoff

Scope: Event 014 Cannibal Commune (`CBL`) country package after the depth pass.

Mode: patch-capable country-package audit. I made a narrow formable-route gate fix inside scoped files and recorded remaining non-blocking risks.

## Skills and References Used

- `chaos-redux-subagents`
- `chaos-redux-events`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- Offline wiki pages consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, country creation, national focuses, state setup, unit setup, and technology.
- Vanilla documentation consulted for script constants, effects, triggers, `load_focus_tree`, `load_oob`, `create_unit`, `transfer_state_to`, `set_capital`, `set_cosmetic_tag`, `drop_cosmetic_tag`, and `recruit_character`.

## Changed Files

- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_cbl_country_package_depth_audit_handoff.md`

## Changed Identifiers

- Trigger logic changed:
  - `cannibalism_cbl_has_hunting_ground_project`
  - `cannibalism_cbl_last_table_map_control`
- Localisation key changed:
  - `cannibalism_cbl_map_the_last_table_tt`
- Formable/cosmetic route affected:
  - `CBL_LAST_TABLE`
- No country tags, state ids, leaders, parties, focus tree ids, idea ids, or formable ids were renamed.

## Before and After Behavior

- Before: `cannibalism_cbl_has_hunting_ground_project` required `cannibalism_cbl_hunting_ground_projects_completed` to be greater than `constant:cannibalism_last_table_requirement.hunting_ground_projects`. The constant is `1`, so the trigger required at least 2 completed projects even though runtime CBL setup initializes the counter to 1 and the constants define the requirement as 1.
- After: the trigger uses `compare = greater_than_or_equals`, so one prepared hunting-ground project satisfies the documented constant.
- Before: `cannibalism_cbl_last_table_map_control` required `num_of_controlled_states > constant:cannibalism_last_table_requirement.controlled_states`. The constant is `4`, so the mission required 5 controlled states.
- After: the trigger uses `NOT = { num_of_controlled_states < constant:cannibalism_last_table_requirement.controlled_states }`, so 4 controlled states satisfies the constant without using unsupported `>=` syntax.
- Before: `cannibalism_cbl_map_the_last_table_tt` told the player to control more than four states and complete at least two hunting-ground projects.
- After: the tooltip tells the player to control at least four states and complete at least one hunting-ground project.

## Country Package Coverage Checklist

- Tag registration: covered. `common/country_tags/chaosx_countries.txt:6` registers `CBL = "countries/Cannibal Commune.txt"`.
- Country definition: covered. `common/countries/Cannibal Commune.txt` defines graphical culture and map/UI colors.
- Cosmetic formable: covered. `common/countries/cosmetic.txt:41` defines `CBL_LAST_TABLE`.
- Country history: covered. `history/countries/CBL - Cannibal Commune.txt` sets OOB, politics, stability, war support, research slots, techs, characters, country flag, and starting idea.
- OOB/templates: covered. `history/units/CBL_1936.txt` defines `Night Larder Columns`, `Commune Guard`, `Scavenger Parties`, `Butcher Packs`, `Prison Processions`, and `Hannibal Cadres`.
- Characters: covered. `common/characters/CBL.txt` defines `CBL_table_council` and `CBL_larder_marshal`.
- Focus tree: covered. `common/national_focus/014_cannibalism_focus_tree.txt:15` defines `cannibalism_commune_focus_tree`.
- Runtime focus loading: covered. `common/scripted_effects/014_cannibalism_effects.txt:878` loads `cannibalism_commune_focus_tree` on first CBL creation and `:918` repairs it for existing CBL if missing.
- AI strategy: covered. `common/ai_strategy/014_cannibalism.txt` defines CBL-gated strategy plans for survival, raiding, pact patience, solitary raids, Last Table preparation, and world-end pressure.
- Cleanup: covered for requested surfaces. `common/scripted_effects/014_cannibalism_effects.txt:683` clears CBL commune/hunting-ground state pressure and `:698-731` clears route flags, missions, route ideas, and cosmetic tag.

## File Surface Checklist

- `common/country_tags/chaosx_countries.txt`: present and contains CBL tag.
- `common/countries/Cannibal Commune.txt`: present.
- `common/countries/cosmetic.txt`: present and contains `CBL_LAST_TABLE`.
- `common/characters/CBL.txt`: present.
- `history/countries/CBL - Cannibal Commune.txt`: present.
- `history/units/CBL_1936.txt`: present.
- `common/national_focus/014_cannibalism_focus_tree.txt`: present.
- `common/ai_strategy/014_cannibalism.txt`: present.
- `common/script_constants/014_cannibalism_constants.txt`: present.
- `common/scripted_triggers/014_cannibalism_triggers.txt`: present.
- `common/scripted_effects/014_cannibalism_effects.txt`: present.
- `common/ideas/014_cannibalism_ideas.txt`: present.
- `interface/014_cannibalism.gfx`: present.
- `localisation/english/014_cannibalism_l_english.yml`: present.
- CBL and `CBL_LAST_TABLE` flags: present in normal, medium, and small sizes, including ideology variants.

## Missing or Stale Country Package Surfaces

- Stale non-scoped documentation: `docs/events/014_cannibalism.md:57` still says the Last Table map mission requires more than four controlled states and at least two hunting-ground projects. I did not patch this because the user-scoped patch list did not include `docs/events/014_cannibalism.md`; the scoped gameplay and localisation files now require at least four states and at least one project.
- No CBL advisor, high command, or dedicated non-commander character advisor surface was found. This is a playability-depth risk, not a load blocker.
- No CBL-specific production-line, navy, air force, convoy route, supply-hub, railway, or port setup exists beyond stockpiles, templates, transferred-state infrastructure, focus rewards, and spawned units.

## Map and State Setup Issues

- No blocking map setup issue found in the scoped files.
- CBL has no owned start state by design. Runtime creation transfers `event_target:cannibalism_commune_state` to CBL, marks it with `cannibalism_commune_origin_state` and `cannibalism_commune`, applies `cannibalism_commune_state`, and sets CBL capital to that state at `common/scripted_effects/014_cannibalism_effects.txt:866-900`.
- `history/countries/CBL - Cannibal Commune.txt` still uses `capital = 1` as a history placeholder. Runtime creation overrides it. If CBL is created outside `cannibalism_create_commune_country`, the placeholder capital can be incoherent.
- Cleanup removes `cannibalism_commune` state flags and commune/hunting-ground modifiers, but it does not clear `cannibalism_commune_origin_state`. If that marker is meant to be temporary state pressure rather than historical origin memory, it should be cleared in a later scoped cleanup pass.

## Politics, Leader, Portrait, Flag, Advisor, and Party Issues

- No blocking politics or leader issue found.
- CBL politics are coherent: neutrality ruling party, no elections, and 100 neutrality popularity in `history/countries/CBL - Cannibal Commune.txt`.
- `CBL_table_council` is an institutional leader name with a council portrait, so gendered personal-name pool rules are not applicable.
- `CBL_larder_marshal` is also institutional, uses the CBL council portrait, and does not trigger the opposite-gender portrait/name-pool defect.
- `GFX_portrait_CBL_table_council` is registered in `interface/014_cannibalism.gfx:101`, and `gfx/leaders/014_cannibalism/CBL_table_council.dds` exists at 156x210.
- `GFX_portrait_CBL_hannibal` is registered in `interface/014_cannibalism.gfx:102`, and `gfx/leaders/014_cannibalism/hannibal.dds` exists at 156x210.
- CBL and `CBL_LAST_TABLE` flags exist in normal, medium, and small sizes with 82x52, 41x26, and 10x7 dimensions.
- No advisors or high command exist for CBL; this remains a country-depth risk.

## Focus, Decision, Idea, and Asset Issues

- Fixed: Last Table mission gate was stricter than its constants and localisation after the depth pass. `cannibalism_cbl_has_hunting_ground_project` and `cannibalism_cbl_last_table_map_control` now match `constant:cannibalism_last_table_requirement.hunting_ground_projects = 1` and `controlled_states = 4`.
- Focus tree loading is safe for an emergent tag because runtime creation explicitly calls `load_focus_tree = { tree = cannibalism_commune_focus_tree keep_completed = no }`.
- CBL focus route ids are localized and have registered icon sprites.
- The Last Table formable route is wired: `cbl_proclaim_the_last_table` checks `cannibalism_last_table_map_validated`, sets `set_cosmetic_tag = CBL_LAST_TABLE`, sets route flags, and adds `cannibalism_last_table_discipline`.
- CBL mission chain is wired: `cannibalism_cbl_map_the_last_table` activates `cannibalism_cbl_last_table_map_mission`; success sets `cannibalism_last_table_map_validated` and adds `cannibalism_last_table_integration`.
- Event 014 ideas are localized and picture sprites are registered in `interface/014_cannibalism.gfx`.
- All `texturefile` paths in `interface/014_cannibalism.gfx` exist.

## Starting Military, Technology, Industry, Supply, and Production Issues

- No blocking starting military issue found for runtime CBL.
- OOB templates exist for all current CBL spawned division types.
- Runtime creation grants manpower, infantry equipment, support equipment, convoys, trains, loads `CBL_1936`, and spawns starting raider/guard forces.
- Runtime reinforcement grants manpower, infantry equipment, support equipment, convoys, and a reinforcement raider unit.
- History grants two research slots and basic infantry/support/recon technologies.
- Remaining playability risk: CBL has no production lines, construction setup, air force, navy, fuel stockpile beyond focus/decision interactions, or dedicated supply buildout. It can function as an emergency hostile tag but is thin as a long-play country.

## AI and Playability Issues

- No blocking AI-strategy reference issue found.
- `common/ai_strategy/014_cannibalism.txt` gates strategies through `is_cannibal_commune_country` and route flags.
- AI can pursue survival, reinforcement, port/rail pressure, pact patience, solitary raids, Last Table preparation, and world-end pressure.
- Remaining playability risk: no `ai_national_focuses`/strategy-plan ordering surface was found for CBL. Route behavior depends on per-focus `ai_will_do` and broad AI strategies.
- Remaining playability risk: no advisor/high-command/production package means CBL may be mechanically sparse after its initial spawned units and focus rewards.

## Meaningful Validation Run

- Confirmed CBL is registered in `common/country_tags/chaosx_countries.txt` and included in shared `is_special_chaos_country` handling in `common/scripted_triggers/chaosx_dynamic_triggers.txt:101-123`.
- Confirmed `cannibalism_commune_focus_tree` is loaded on first CBL creation and repaired for existing CBL via `has_focus_tree`.
- Confirmed `load_oob = "CBL_1936"`, runtime capital assignment, starting force spawn, and reinforcement spawn references exist.
- Confirmed all CBL focus titles/descriptions and focus icon sprites are covered.
- Confirmed all 13 Event 014 ideas have localisation and picture sprites.
- Confirmed CBL character localisation and portrait sprite references are covered.
- Confirmed all `interface/014_cannibalism.gfx` texture paths exist.
- Confirmed `localisation/english/014_cannibalism_l_english.yml` still has UTF-8 BOM after the localisation patch.
- Confirmed CBL and `CBL_LAST_TABLE` normal, medium, and small TGA flags exist at 82x52, 41x26, and 10x7 with bottom origin.
- Searched for stale Last Table threshold wording after the patch. Only `docs/events/014_cannibalism.md:57` remains stale and was left unpatched because it is outside the requested scoped file list.

## Skipped Meaningful Validation

- I did not run a live HOI4 launch or in-game scenario validation.
- I did not create a git commit. `common/scripted_triggers/014_cannibalism_triggers.txt` is untracked in the current workspace, and committing my narrow trigger changes would also commit the parent depth-pass file content. The workspace also contains many unrelated pre-existing dirty files.

## Remaining Setup or Identity Risks

- `docs/events/014_cannibalism.md:57` should be updated by the parent to match the patched Last Table threshold.
- `cannibalism_commune_origin_state` is not cleared by `cannibalism_cleanup_commune_country_pressure`; decide whether it is intended historical memory or a stale state marker.
- CBL lacks advisors, high command, production lines, air/naval setup, and broader supply/industry scaffolding.
- CBL route AI is functional but not focus-order planned.
- Forced/manual CBL creation outside `cannibalism_create_commune_country` remains incoherent because the history placeholder capital and templates do not create a complete map state by themselves.
