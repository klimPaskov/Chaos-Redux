# Event 006 Decision Tooltip Cleanup Handoff

Subagent: `chaosx_decision_mission_auditor`

Scope: bounded cleanup for remaining package/formable decision requirement tooltip gaps in `common/decisions/006_independence_wave_decisions.txt` and matching English localisation. This does not claim full Event 006 completion.

## Files changed

- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_155247_decision_tooltip_cleanup.md`

## Gameplay surface changed

Wrapped the remaining raw `available`, `target_root_trigger`, and `target_trigger` requirement bodies in `custom_trigger_tooltip` blocks. Existing triggers were preserved inside the wrappers. No costs, AI weights, timers, visible gates, package flags, state IDs, effects, or mission success/failure behavior were changed.

## Decision ids touched

- `independence_wave_integrate_volga_kama_ministries`
- `independence_wave_open_assyrian_recognition_congress`
- `independence_wave_charter_danzig_free_city_board`
- `independence_wave_open_buganda_lukiko_records`
- `independence_wave_review_buganda_protectorate_treaties`
- `independence_wave_open_sokoto_scholar_council`
- `independence_wave_register_northern_emirates`
- `independence_wave_open_bukhara_oasis_council`
- `independence_wave_register_bukhara_oasis_charter`
- `independence_wave_open_khiva_canal_council`
- `independence_wave_register_khiva_water_charter`
- `independence_wave_open_mesopotamian_river_records`
- `independence_wave_map_mesopotamian_river_petitions`
- `independence_wave_open_don_river_records`
- `independence_wave_map_don_petitions`
- `independence_wave_open_kuban_black_sea_records`
- `independence_wave_map_kuban_petitions`
- `independence_wave_open_altai_oyrot_records`
- `independence_wave_map_altai_petitions`
- `independence_wave_open_dahomey_palace_council`
- `independence_wave_register_bight_customs_charter`
- `independence_wave_open_barotse_litunga_records`
- `independence_wave_map_barotse_floodplain_treaties`
- `independence_wave_open_miskito_shore_records`
- `independence_wave_map_miskito_coastal_petitions`
- `independence_wave_open_itza_peten_records`
- `independence_wave_map_itza_yucatan_petitions`
- `independence_wave_open_maya_council_records`
- `independence_wave_map_maya_peninsula_petitions`
- `independence_wave_open_guarani_land_council`
- `independence_wave_map_guarani_communal_lands`
- `independence_wave_open_charrua_memory_council`
- `independence_wave_map_charrua_assembly_lands`
- `independence_wave_open_kurdish_mountain_registry`
- `independence_wave_map_kurdish_pass_districts`
- `independence_wave_open_circassian_mountain_records`
- `independence_wave_map_circassian_pass_petitions`
- `independence_wave_open_andean_highland_records`
- `independence_wave_map_andean_petitions`
- `independence_wave_open_nahua_san_salvador_records`
- `independence_wave_map_nahua_charter_petitions`
- `independence_wave_open_inuit_arctic_register`
- `independence_wave_map_inuit_arctic_petitions`
- `independence_wave_open_namibia_land_records`
- `independence_wave_map_namibia_land_petitions`
- `independence_wave_open_bechuanaland_kgotla_records`
- `independence_wave_map_bechuanaland_land_petitions`
- `independence_wave_open_ghana_gold_coast_records`
- `independence_wave_map_ghana_council_petitions`
- `independence_wave_open_eritrea_red_sea_records`
- `independence_wave_map_eritrea_coastal_petitions`
- `independence_wave_open_darfur_records`
- `independence_wave_map_darfur_petitions`
- `independence_wave_open_zulu_records`
- `independence_wave_map_zulu_petitions`
- `independence_wave_assemble_junction_committee`
- `independence_wave_secure_bridge_guard`
- `independence_wave_invite_compact_delegate`

Existing KUB/ALT decision blocks were only given requirement tooltip wrappers because they were already present in the file. No KUB/ALT mechanics, gates, effects, or scope were expanded.

## Localisation keys added

Added one requirement key for each wrapped `available` block, plus compact invite root/target keys:

- `independence_wave_integrate_volga_kama_ministries_requirements_tt`
- `independence_wave_open_assyrian_recognition_congress_requirements_tt`
- `independence_wave_charter_danzig_free_city_board_requirements_tt`
- `independence_wave_open_buganda_lukiko_records_requirements_tt`
- `independence_wave_review_buganda_protectorate_treaties_requirements_tt`
- `independence_wave_open_sokoto_scholar_council_requirements_tt`
- `independence_wave_register_northern_emirates_requirements_tt`
- `independence_wave_open_bukhara_oasis_council_requirements_tt`
- `independence_wave_register_bukhara_oasis_charter_requirements_tt`
- `independence_wave_open_khiva_canal_council_requirements_tt`
- `independence_wave_register_khiva_water_charter_requirements_tt`
- `independence_wave_open_mesopotamian_river_records_requirements_tt`
- `independence_wave_map_mesopotamian_river_petitions_requirements_tt`
- `independence_wave_open_don_river_records_requirements_tt`
- `independence_wave_map_don_petitions_requirements_tt`
- `independence_wave_open_kuban_black_sea_records_requirements_tt`
- `independence_wave_map_kuban_petitions_requirements_tt`
- `independence_wave_open_altai_oyrot_records_requirements_tt`
- `independence_wave_map_altai_petitions_requirements_tt`
- `independence_wave_open_dahomey_palace_council_requirements_tt`
- `independence_wave_register_bight_customs_charter_requirements_tt`
- `independence_wave_open_barotse_litunga_records_requirements_tt`
- `independence_wave_map_barotse_floodplain_treaties_requirements_tt`
- `independence_wave_open_miskito_shore_records_requirements_tt`
- `independence_wave_map_miskito_coastal_petitions_requirements_tt`
- `independence_wave_open_itza_peten_records_requirements_tt`
- `independence_wave_map_itza_yucatan_petitions_requirements_tt`
- `independence_wave_open_maya_council_records_requirements_tt`
- `independence_wave_map_maya_peninsula_petitions_requirements_tt`
- `independence_wave_open_guarani_land_council_requirements_tt`
- `independence_wave_map_guarani_communal_lands_requirements_tt`
- `independence_wave_open_charrua_memory_council_requirements_tt`
- `independence_wave_map_charrua_assembly_lands_requirements_tt`
- `independence_wave_open_kurdish_mountain_registry_requirements_tt`
- `independence_wave_map_kurdish_pass_districts_requirements_tt`
- `independence_wave_open_circassian_mountain_records_requirements_tt`
- `independence_wave_map_circassian_pass_petitions_requirements_tt`
- `independence_wave_open_andean_highland_records_requirements_tt`
- `independence_wave_map_andean_petitions_requirements_tt`
- `independence_wave_open_nahua_san_salvador_records_requirements_tt`
- `independence_wave_map_nahua_charter_petitions_requirements_tt`
- `independence_wave_open_inuit_arctic_register_requirements_tt`
- `independence_wave_map_inuit_arctic_petitions_requirements_tt`
- `independence_wave_open_namibia_land_records_requirements_tt`
- `independence_wave_map_namibia_land_petitions_requirements_tt`
- `independence_wave_open_bechuanaland_kgotla_records_requirements_tt`
- `independence_wave_map_bechuanaland_land_petitions_requirements_tt`
- `independence_wave_open_ghana_gold_coast_records_requirements_tt`
- `independence_wave_map_ghana_council_petitions_requirements_tt`
- `independence_wave_open_eritrea_red_sea_records_requirements_tt`
- `independence_wave_map_eritrea_coastal_petitions_requirements_tt`
- `independence_wave_open_darfur_records_requirements_tt`
- `independence_wave_map_darfur_petitions_requirements_tt`
- `independence_wave_open_zulu_records_requirements_tt`
- `independence_wave_map_zulu_petitions_requirements_tt`
- `independence_wave_assemble_junction_committee_requirements_tt`
- `independence_wave_secure_bridge_guard_requirements_tt`
- `independence_wave_invite_compact_delegate_root_requirements_tt`
- `independence_wave_invite_compact_delegate_target_requirements_tt`

No existing localisation keys were renamed or removed.

## Validation

- Required wiki/docs consulted before reading/editing Chaos files:
  - `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
  - Vanilla decision precedents in `/home/klim/projects/Hearts of Iron IV/common/decisions/`
- Brace/trailing whitespace check:
  - `common/decisions/006_independence_wave_decisions.txt`: `brace_balance=0`, `min_balance=0`, `trailing_ws=0`
  - `localisation/english/006_independence_wave_l_english.yml`: `brace_balance=0`, `min_balance=0`, `trailing_ws=0`
- Localisation BOM check: passed, file still starts with UTF-8 BOM.
- Localisation `:0` style check: passed, no `:0` found.
- Unsupported operator check: `rg -n "<=|>=" common/decisions/006_independence_wave_decisions.txt localisation/english/006_independence_wave_l_english.yml` returned no matches.
- `git diff --check -- common/decisions/006_independence_wave_decisions.txt localisation/english/006_independence_wave_l_english.yml`: passed.
- Parser summary for `available`, `target_trigger`, and `target_root_trigger` blocks lacking `custom_trigger_tooltip`: `remaining_unwrapped=0`.
- Tooltip reference check: `tooltip_refs=328`, `missing=0`.

## Remaining risks

- Requirement text summarizes existing `can_independence_wave_*` helpers rather than enumerating every hidden helper condition. This keeps the patch bounded and avoids changing gameplay.
- The repository worktree was already heavily dirty, and `common/decisions/006_independence_wave_decisions.txt` is untracked in Git. No commit was made by this subagent because staging the full untracked file would include broader parent work outside this narrow cleanup.
- No full Event 006 completion, balance pass, in-game validation, or broader package audit is claimed here.
