# Event 014 CBL Country Package Audit Handoff

Scope: Event 014 Cannibal Commune (`CBL`) only.

Mode: patch-capable country-package audit. I made small local fixes to CBL package wiring and localisation, then validated the relevant static surfaces.

## Guidance Consulted

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- Offline wiki pages: Data structures, Triggers, Effects, Localisation, Event modding, Decision modding, AI modding, Country creation, National focus modding, Graphical asset modding.
- Vanilla documentation: `effects_documentation.md` for `load_focus_tree`, `triggers_documentation.md` for `has_focus_tree`.
- Vanilla precedent: `common/decisions/BEL.txt` uses `load_focus_tree = { tree = congo_focus keep_completed = yes }` on generated subject-country focus loading.

## Changed Files

- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_cbl_country_package_audit_handoff.md`

## Changed Identifiers

- Added country flag: `cannibalism_commune_spawn_source`
- Updated trigger: `cannibalism_can_form_commune_from_country`
- Updated effect path: `cannibalism_create_commune_country`
- Updated existing-CBL branch: `cannibalism_commune_reinforcement`
- Updated focus-tree reload check for `cannibalism_commune_focus_tree`
- Added localisation keys:
  - `CBL_democratic`, `CBL_democratic_DEF`, `CBL_democratic_ADJ`
  - `CBL_fascism`, `CBL_fascism_DEF`, `CBL_fascism_ADJ`
  - `CBL_communism`, `CBL_communism_DEF`, `CBL_communism_ADJ`
  - `CBL_neutrality`, `CBL_neutrality_DEF`, `CBL_neutrality_ADJ`
  - `CBL_LAST_TABLE_democratic`, `CBL_LAST_TABLE_democratic_DEF`, `CBL_LAST_TABLE_democratic_ADJ`
  - `CBL_LAST_TABLE_fascism`, `CBL_LAST_TABLE_fascism_DEF`, `CBL_LAST_TABLE_fascism_ADJ`
  - `CBL_LAST_TABLE_communism`, `CBL_LAST_TABLE_communism_DEF`, `CBL_LAST_TABLE_communism_ADJ`
  - `CBL_LAST_TABLE_neutrality`, `CBL_LAST_TABLE_neutrality_DEF`, `CBL_LAST_TABLE_neutrality_ADJ`

No country tag, state ID, leader ID, party ID, focus ID, formable ID, or portrait path was changed.

## Before And After Behavior

- Before: `cannibalism_can_form_commune_from_country` required `NOT = { country_exists = CBL }`, so `cannibalism_create_commune_country` could create CBL once but its existing-CBL reinforcement branch was unreachable from the normal call path.
- After: a non-CBL outbreak country in island stage with high cult and low containment can call the creation effect once. The first qualifying source creates CBL; later qualifying source countries reinforce CBL once through `cannibalism_commune_reinforcement`.
- Before: existing CBL focus-tree repair relied on `cannibalism_commune_focus_tree_loaded`, which could become stale if the flag and actual tree state diverged.
- After: the existing-CBL reinforcement branch checks `has_focus_tree = cannibalism_commune_focus_tree` and reloads with `keep_completed = yes` only when the tree is actually missing.
- Before: CBL and `CBL_LAST_TABLE` had base country localisation but no ideology-specific country/cosmetic name variants.
- After: all four vanilla ideology variants have name, definite name, and adjective keys for both `CBL` and `CBL_LAST_TABLE`.

## Country Package Coverage Checklist

- Tag registration: present at `common/country_tags/chaosx_countries.txt:6` with `CBL = "countries/Cannibal Commune.txt"`.
- Country definition: present at `common/countries/Cannibal Commune.txt`; uses dark red country/UI colors and western graphics.
- History file: present at `history/countries/CBL - Cannibal Commune.txt`; sets politics, stability, war support, research slots, starting idea, OOB, and `CBL_table_council`.
- OOB: present at `history/units/CBL_1936.txt`; defines `Night Larder Columns` and `Commune Guard` templates.
- Character: present at `common/characters/CBL.txt`; `CBL_table_council` uses institutional localisation and `GFX_portrait_CBL_table_council`.
- AI: present at `common/ai_strategy/014_cannibalism.txt`; all strategies are gated by `is_cannibal_commune_country`.
- Focus tree: present at `common/national_focus/014_cannibalism_focus_tree.txt:14`; runtime loading is wired in `common/scripted_effects/014_cannibalism_effects.txt:825` and repaired in the existing-CBL branch at `:863-864`.
- Cosmetic tag: present at `common/countries/cosmetic.txt:41` as `CBL_LAST_TABLE`.
- Creation/reinforcement: creation call starts at `common/scripted_effects/014_cannibalism_effects.txt:802`; CBL setup starts at `:809`; reinforcement starts at `:873`.
- Defeat cleanup: global defeat refresh exists at `common/scripted_effects/014_cannibalism_effects.txt:910`; defeat requires no active outbreak countries and CBL missing or capitulated.

## File Surface Checklist

All requested primary files are present:

- `common/country_tags/chaosx_countries.txt`
- `common/countries/Cannibal Commune.txt`
- `history/countries/CBL - Cannibal Commune.txt`
- `history/units/CBL_1936.txt`
- `common/characters/CBL.txt`
- `common/ai_strategy/014_cannibalism.txt`
- `common/national_focus/014_cannibalism_focus_tree.txt`
- `common/countries/cosmetic.txt`
- `common/scripted_effects/014_cannibalism_effects.txt`
- `common/scripted_triggers/014_cannibalism_triggers.txt`
- `interface/014_cannibalism.gfx`
- `localisation/english/014_cannibalism_l_english.yml`
- `gfx/flags/CBL.tga`, `gfx/flags/medium/CBL.tga`, `gfx/flags/small/CBL.tga`
- `gfx/flags/CBL_LAST_TABLE.tga`, `gfx/flags/medium/CBL_LAST_TABLE.tga`, `gfx/flags/small/CBL_LAST_TABLE.tga`
- `gfx/leaders/014_cannibalism/CBL_table_council.dds`

## Missing Or Stale Country Package Surfaces

- Fixed: existing-CBL reinforcement was stale/dead because the trigger blocked all calls once CBL existed. Patched through `cannibalism_commune_spawn_source`.
- Fixed: existing-CBL focus loading could be stale because it used only a country flag. Patched to `has_focus_tree`.
- Fixed: ideology-specific country and cosmetic localisation variants were missing.
- Remaining: no advisor, high command, commander, navy, air force, or production-line package exists for CBL. This is not blocking for an emergency tag but limits player playability.

## Map And State Setup Issues

- CBL has no start-state ownership by design. Runtime creation transfers one random owned/controlled state from the failed source country to CBL, sets `cannibalism_commune_origin_state` and `cannibalism_commune`, adds `cannibalism_commune_state`, then sets CBL capital to that state at `common/scripted_effects/014_cannibalism_effects.txt:814-847`.
- `history/countries/CBL - Cannibal Commune.txt` uses `capital = 1` as a history placeholder. The creation effect overrides this at runtime. If CBL is forced into existence outside the Event 014 creation effect, its capital/state setup is not coherent.
- The trigger still assumes island-stage failed countries have at least one owned/controlled state. I did not add a broader state-validity guard because that changes failure semantics beyond the CBL package patch.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- CBL politics are coherent: neutrality ruling party, no elections, 100 neutrality popularity.
- `CBL_table_council` is an institutional leader name with a council portrait, so the gendered personal-name pool rule is not applicable.
- `GFX_portrait_CBL_table_council` is registered in `interface/014_cannibalism.gfx:66`; the DDS exists and is 156x210.
- CBL and `CBL_LAST_TABLE` flag sets exist in normal, medium, and small sizes. Measured TGA dimensions are 82x52, 41x26, and 10x7.
- No CBL advisors or high command exist. This is a residual playability risk, not a syntax blocker.

## Focus, Decision, Idea, And Asset Issues

- Focus tree assignment is now explicitly loaded at runtime and repaired if missing.
- The previously high-risk mutually exclusive focus prerequisites are in OR form:
  - `cbl_couriers_between_tables` accepts either `cbl_no_public_feasts` or `cbl_hunting_ground_doctrine` at `common/national_focus/014_cannibalism_focus_tree.txt:197`.
  - `cbl_world_as_larder_gate` accepts either `cbl_listen_for_hannibal` or `cbl_proclaim_the_last_table` at `common/national_focus/014_cannibalism_focus_tree.txt:297`.
- Last Table route is implemented as a focus/cosmetic route: `cbl_proclaim_the_last_table` sets `CBL_LAST_TABLE`, `cannibalism_last_table_formed`, `cannibalism_table_for_one_achieved`, and `cannibalism_later_unifier_accepted` at `common/national_focus/014_cannibalism_focus_tree.txt:245-266`.
- World-end route is available through focus `cbl_world_as_larder_gate` and decision `cannibalism_launch_world_end_route`; both call `cannibalism_try_world_end_route`.
- All CBL focus name/description localisation keys exist.
- All texture paths referenced by `interface/014_cannibalism.gfx` exist.
- Remaining: Last Table is not a map-state-control formable decision suite. If the design intent is a full formable with conquest requirements, that needs a parent-level design plan rather than a local package patch.

## Starting Military, Technology, Industry, Supply, And Production Issues

- Creation setup grants manpower, infantry equipment, support equipment, convoys, trains, OOB templates, and spawned divisions through `cannibalism_spawn_commune_starting_forces`.
- Reinforcement grants manpower/equipment/convoys and one raider-template spawn through `cannibalism_commune_reinforcement`.
- Technologies are minimal but coherent for the templates: infantry weapons, improved infantry weapons, support equipment, and recon.
- There are no starting production lines, construction, air force, navy, fuel, supply-hub, rail, port, or industry additions for CBL beyond the seized state and stockpiles. CBL survivability depends on the transferred state and focus rewards.
- OOB contains templates only; actual starting divisions are spawned by `common/scripted_effects/014_cannibalism_effects.txt:881-896`. Console/history-only CBL spawning will not receive fielded units unless the event effect is run.

## AI And Playability Issues

- AI strategies are gated to CBL through `is_cannibal_commune_country`.
- The AI has survival, wartime, network, and world-end pressure strategies. `avoid_starting_wars` uses positive `avoid_suicide_wars` early and negative `raid_ports`/`world_end_aggression` later, which appears intentional for reducing caution as the route escalates.
- Focus AI weights exist across the tree.
- Playability risk remains: no AI strategy plan orders CBL through a specific focus route, so route selection depends on per-focus `ai_will_do`.
- Playability risk remains: lack of advisors/production setup may leave player CBL thin after the initial spawned divisions.

## Validation

- Primary file presence check: all requested CBL package files were present.
- Creation/reinforcement path check: confirmed `cannibalism_can_form_commune_from_country` no longer blocks existing CBL, and `cannibalism_commune_spawn_source` guards each source country from repeated creation/reinforcement.
- Focus loading check: confirmed new CBL loads `cannibalism_commune_focus_tree`, and existing CBL branch uses `has_focus_tree` plus `keep_completed = yes`.
- Localisation check: confirmed all CBL focus name/description keys exist; confirmed `014_cannibalism_l_english.yml` still has UTF-8 BOM after edits.
- Asset check: confirmed all `texturefile` paths in `interface/014_cannibalism.gfx` exist; confirmed CBL and `CBL_LAST_TABLE` flag dimensions are 82x52, 41x26, and 10x7; confirmed `CBL_table_council.dds` is 156x210.

Skipped validation:

- No in-game HOI4 runtime test was run from this subagent pass. The audit is static repo validation only.

## Residual Risks And Uncertainty

- Runtime creation still does not explicitly validate that the source country has a valid owned/controlled state before setting `cannibalism_commune_spawn_source`. If a future edge case reaches island-stage failure without such a state, CBL setup may be incomplete.
- CBL defeat cleanup marks global defeat but does not perform a full CBL package teardown of state flags/modifiers if the tag survives as capitulated. This may be acceptable for event memory, but it is not a hard cleanup.
- Last Table is a focus/cosmetic path, not a full formable decision suite with state-control requirements.
- CBL has a minimal emergency-country package rather than a full country package with advisors, commanders, navy/air setup, production lines, or bespoke supply buildout.

No broad identity redesign, new focus tree, new formable suite, or unrelated Event 013/Event 015 files were touched.
