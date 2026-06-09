# Event006 Completion Audit Current State

Timestamp: 2026-06-05 18:23:17 UTC

Subagent: `chaosx_event_completion_auditor`

Mode: read-only audit. No gameplay, localisation, assets, spreadsheets, or git state were edited. This handoff report is the only file written.

## Required Reading

Opened the required offline Paradox wiki pages before inspecting Chaos files:

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
- Relevant extras: `National focus modding`, `Country creation`, `Interface modding`, `Scripted GUI modding`, `Achievement modding`.

Opened relevant vanilla docs/examples:

- `~/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `~/projects/Hearts of Iron IV/common/script_constants/documentation.md`
- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/loc_objects_documentation.md`
- `~/projects/Hearts of Iron IV/documentation/loc_formatter_documentation.md`
- Vanilla release/focus/unit precedents were spot-checked with `rg` in the vanilla game tree.

Repo skills used:

- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `xlsx` for spreadsheet-audit expectations; `openpyxl` was unavailable, so workbook review fell back to read-only `.xlsx` XML inspection.

## Source Specs And Plans Inspected

Primary source-spec pack:

- `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_decisions_ai.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_assets_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_super_event_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_achievements_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_coding_prompt.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_catalog_update.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_research_notes.md`

Current plans/handoffs:

- `docs/plans/006_independence_wave_plans/source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_improvement_loop_gate.md`
- Recent parent and subagent handoffs under `docs/plans/006_independence_wave_plans/subagent_handoffs/`, especially the 2026-06-05 playable wrapup, runtime cleanup, Event005 separation audit, candidate resolver fix, custom generic release tranche, MAP package and MAP flag handoffs.

## Executive Classification

Overall Event006 completion: **Incomplete / Weak needs validation**.

Current state is substantially more playable than older audits: immediate release, host-survival gating, reduced-core starts, startup army support, shared generic focus tree loading, Event005 setup/focus guard, MAP package, news release list, achievements, assets, super-event/audio references, and workbook row text are all present. However, a full completion claim is not proven because final game-load validation, balance scenarios, full Event005 cross-system exclusion, final spreadsheet/catalog parity, full package/formable closure, and final asset/UI validation remain open or only partially audited.

No simplification is hidden here: this report does **not** claim Event006 is complete.

## Major Requirement Matrix

| Requirement | Classification | Evidence and notes |
| --- | --- | --- |
| Event006 independent from Event005 | Weak/Needs validation | Event006 sets `chaosx_release_origin_independence_wave` in `independence_wave_setup_released_country`. Event005 `soviet_collapse_setup_breakaway_country` and `soviet_collapse_load_event_created_focus_tree` both guard against `chaosx_release_origin_independence_wave`. Full Event005 decision arrays and all downstream systems were not exhaustively proven clean. |
| KUB/ALT must not be expanded | Proven for active Event006 surfaces | Active scan over `events/006_independence_wave.txt`, Event006 effects/triggers/decisions/focus/localisation/ideas/constants/interface found only `common/scripted_triggers/006_independence_wave_triggers.txt:46-47` candidate exclusions for `KUB` and `ALT`. |
| Immediate release after scoring and host survival | Proven | `events/006_independence_wave.txt` loops candidate pool, validates `can_independence_wave_host_release_current_candidate_safely`, reserves survival state, prepares reduced footprint, then calls `release = event_target:independence_wave_current_candidate` in the same immediate resolver. |
| Host survival mandatory | Weak/Needs validation | The trigger requires a non-candidate-owned host state and excludes reserved survival states; the effect reserves capital when valid and otherwise strongest non-candidate state. This is strong script evidence, but no live multi-host/multi-candidate scenario was run. |
| News event displays all countries released in current wave | Proven | `independence_wave_register_successful_release` stores `global.independence_wave_country_1` through `_16`. `GetIndependenceWaveReleasedCountryList` chooses loc lists 1-16. `chaosx.news.6.d` includes `Confirmed releases: [This.GetIndependenceWaveReleasedCountryList]`. |
| Starting units/equipment/templates and army-building path | Proven for runtime releases; Weak for direct bookmark selection | `independence_wave_setup_released_country` adds manpower, infantry/support equipment, unlocked `Independence Wave Provisional Guard` template, two capital guard divisions, and one arms factory in a controlled core state. Custom country history files have no OOB, so direct-start use is not covered by this audit. |
| Released countries can expand beyond one-state starts without erasing hosts | Proven for core mechanism; Weak for balance | Reduced-footprint release masks non-anchor cores, restores them after release, marks `independence_wave_reduced_territory_start` and `independence_wave_border_survey_filed`, and Border Commission decisions can transfer non-capital, non-protected, unowned-by-root cores from hosts that remain above state floor. Balance and AI behavior need live validation. |
| Generic Event006 released countries share generic tree | Proven | `independence_wave_load_provisional_focus_tree` loads `independence_wave_liberation_provisional_tree`. Generic niche releases `ASN`, `KBN`, `PLM`, `AYM` are restored as ordinary/niche generic releases and are not hardcoded to republic-specific stacked focuses. Tree currently has 50 focus blocks by `rg` count. |
| Unique upright flags for every new country/formable | Weak/Needs validation | `ASN`, `KBN`, `PLM`, `AYM` have base and ideology variants across base/medium/small, with DDS and TGA. `DFR` and `ZUL` have base and ideology TGA variants. `MAP` has unique base/medium/small TGA only; MAP flag handoff records upright TopLeft files, but there are no MAP ideology variants and no MAP DDS parity. Formable-specific unique flags were not exhaustively audited. |
| Evolution log count/gating | Proven for active writer call sites; Weak for helper naming | Active `record_events_log_evolution_entry` calls are only inside `independence_wave_record_tier_evolution_log_entry`, with four gated stage flags: Gathering Storm, Rising Cascade, Old Names Return, Impossible Statehood. Only call site found is Event006 immediate after successful release. Many package/formation log helper definitions remain but do not call `record_events_log_evolution_entry` by themselves; this should be kept under review. |
| Baseline evolutions start at least from Gathering Storm | Proven | `independence_wave_record_tier_evolution_log_entry` logs Gathering Storm at `chaos_tier = 1`; there is no Calm World tier-0 writer branch. |
| MAP package and parent MAP claim correction | Proven for inspected effect | `MAP` is registered as tag/country/history/localisation. Candidate seed uses Araucania `950` and Aysen `949`; MAP petition effect adds cores to `949` and `512` but no longer uses `add_claim_by = ROOT` there, matching the parent correction. |
| Localisation keys/encoding | Proven for sampled Event006 surfaces | `006_independence_wave_l_english.yml`, `chaosx_countries_l_english.yml`, and `chaosx_achievements_l_english.yml` begin with BOM `efbbbf`; no `:0` keys found in sampled files. Full mod localisation was not audited. |
| Super-event/audio references | Proven for references/assets; Weak for runtime visual/audio trigger validation | Seven Event006 super-event sprites exist in `interface/chaosx_super_events.gfx` and `gfx/super_events/`; corresponding `.ogg` and `.wav` files exist and are referenced in `music/chaosx_super_event_music.asset` and `sound/chaosx_sound.asset`. Runtime playback was not validated. |
| Achievements | Proven present; Weak for runtime unlock validation | Event006 achievements have gameplay blocks, localisation, GFX declarations, and DDS variants. `cr_capital_still_answers` is present later in the achievement file after unrelated common achievements, which is structurally odd but not proven broken by the read-only checks. |
| Scripted GUI / decision surfaces | Proven present; Weak for UI runtime | Scripted GUI files exist for Dossier Board, Congress, Patron Ledger, Formation Ledger, and Border Commission. Decision categories and AI weights are extensive. No live UI render or in-game tooltip audit was run. |
| Assets/manifests | Proven for many wired assets; Weak for optional/final polish | Report/news/focus/decision/category/idea/achievement/super-event assets and manifests are present. `source_of_truth_map.md` still says asset completion does not equal Event006 completion; package-specific optional variants and final visual validation remain follow-up. |
| Workbook/catalog alignment | Weak/Needs validation | `.xlsx` XML inspection found current Event006 row text describing immediate host-survival release, startup divisions, shared 50-focus tree, Border Commission reduced-core recovery, super-events, and 19 achievements. `openpyxl` was missing, so no structured spreadsheet read/recalc was performed. |
| Remaining accepted/queued plans | Incomplete | Source map says the broad improvement addendum is closed as broad plan but queued work remains: final package depth where explicitly wanted, package-specific presentation/animation manifests, catalog/spreadsheet/event-detail alignment, balance scenarios, final audits, PRA separation, and no new broad planner until queued work is handled or narrowed. |

## Files And Identifiers Inspected

Core Event006:

- `events/006_independence_wave.txt`
  - `chaosx.nr6.1`
  - `chaosx.nr6.2`
  - `chaosx.news.6`
- `common/scripted_effects/006_independence_wave_effects.txt`
  - `independence_wave_prepare_release_count`
  - `independence_wave_seed_niche_generic_candidates`
  - `independence_wave_seed_verified_package_candidates`
  - `independence_wave_reserve_host_survival_state`
  - `independence_wave_prepare_reduced_release_footprint`
  - `independence_wave_restore_reduced_release_cores`
  - `independence_wave_setup_released_country`
  - `independence_wave_restore_niche_generic_release_identity`
  - `independence_wave_load_provisional_focus_tree`
  - `independence_wave_map_mapuche_land_petitions_effect`
  - `independence_wave_record_tier_evolution_log_entry`
  - `independence_wave_register_successful_release`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
  - `is_independence_wave_release`
  - `is_independence_wave_achievement_release`
  - `can_independence_wave_use_candidate_tag`
  - `can_independence_wave_host_release_current_candidate_safely`
  - `is_independence_wave_border_commission_target_state`
  - `can_independence_wave_recover_surveyed_core`
- `common/decisions/006_independence_wave_decisions.txt`
  - `independence_wave_border_commission_category`
  - `independence_wave_recover_surveyed_core`
  - `independence_wave_petition_border_parish`
  - `independence_wave_request_league_arbitration`
  - `independence_wave_offer_protected_transfer`
  - `independence_wave_issue_dossier_ultimatum`
  - `independence_wave_freeze_claim_under_observers`
- `common/national_focus/006_independence_wave_focus.txt`
  - `independence_wave_liberation_provisional_tree`
- `common/script_constants/006_independence_wave_constants.txt`
  - `independence_wave_super_event`
  - `independence_wave_event_log`
  - `independence_wave_achievement`

Event005 separation:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `soviet_collapse_setup_breakaway_country`
  - `soviet_collapse_load_event_created_focus_tree`
- `events/005_soviet_collapse.txt` spot search
- `common/scripted_triggers/005_soviet_collapse_triggers.txt` spot search
- `common/decisions/005_soviet_collapse*.txt` spot search
- `common/national_focus/005_soviet_collapse*.txt` spot search

Countries and flags:

- `common/country_tags/chaosx_countries.txt`
- `common/countries/ASN - Asante Council.txt`
- `common/countries/KBN - Kanem-Bornu Authority.txt`
- `common/countries/PLM - Palmares Council.txt`
- `common/countries/AYM - Aymara Highland Congress.txt`
- `common/countries/MAP - Mapuche Land Congress.txt`
- `common/countries/DFR - Darfur Council.txt`
- `common/countries/ZUL - Zulu Council.txt`
- Matching `history/countries/*.txt` files for `ASN`, `KBN`, `PLM`, `AYM`, `MAP`, `DFR`, `ZUL`
- `gfx/flags`, `gfx/flags/medium`, `gfx/flags/small` entries for those tags

Localisation, GUI, assets, achievements:

- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_countries_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `common/scripted_guis/006_independence_wave_scripted_guis.txt`
- `interface/006_independence_wave_scripted_gui.gui`
- `interface/006_independence_wave_icons.gfx`
- `interface/006_independence_wave_report_event_images.gfx`
- `interface/006_independence_wave_news_event_images.gfx`
- `common/achievements/chaos_redux_achievements.txt`
- `interface/chaosx_achievements.gfx`
- `gfx/achievements/cr_*`
- `interface/chaosx_super_events.gfx`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `common/scripted_guis/chaosx_scripted_gui_super_events.txt`
- `music/chaosx_super_event_music.asset`
- `sound/chaosx_sound.asset`
- `gfx/super_events/super_event_independence_wave_*.dds`
- `music/super_event_independence_wave_*.ogg`
- `sound/chaosx_super_event_independence_wave_*.wav`
- `docs/assets/006_independence_wave/**/manifest.md` spot/list inspection

Workbook/catalog:

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` via `unzip`/XML text inspection
- `docs/specs/006_independence_wave_specs/006_independence_wave_catalog_update.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_parent_event006_reduced_core_catalog_alignment.md`

## Specific Findings

### Release Resolver

Classification: **Proven**

`chaosx.nr6.1` is a hidden triggered event. Its immediate block prepares release counts and candidate pools, loops candidates, validates host safety, reserves a survival state, masks reduced release cores, releases the candidate immediately, sets autonomy/truce/origin, runs startup setup, restores cores, registers successful releases, opens Congress, then fires report/news events.

This satisfies the correction that Independence Wave releases must happen immediately after scoring and host-survival validation, rather than waiting on dossier decisions.

### Host Survival

Classification: **Weak/Needs validation**

Strong script evidence exists:

- `can_independence_wave_host_release_current_candidate_safely` requires the host to exist, have more than the survival state floor, own a non-capital candidate core, own at least one state that is not candidate-cored, and not have the reserved survival state also be a candidate core.
- `independence_wave_reserve_host_survival_state` prefers the host capital when it is owned by the host and not candidate-cored, then falls back to valuable non-candidate states.
- `independence_wave_prepare_reduced_release_footprint` avoids `independence_wave_host_survival_reserved`.
- Border Commission target states also exclude `independence_wave_host_survival_reserved`.

Weakness:

- This audit did not run live scenarios with multiple releases from the same host, hostile occupations, capitals that are candidate-cored, or repeated Border Commission transfers after several waves.
- The guarantee is script-plausible, not runtime-proven.

### Border Commission And Recovery

Classification: **Proven for existence, Weak for balance/runtime**

The Border Commission includes:

- `independence_wave_file_border_survey`
- `independence_wave_recover_surveyed_core`
- `independence_wave_petition_border_parish`
- `independence_wave_request_league_arbitration`
- `independence_wave_offer_protected_transfer`
- `independence_wave_issue_dossier_ultimatum`
- `independence_wave_freeze_claim_under_observers`

Recovery transfers target states to ROOT through `transfer_state_to = ROOT`, but target states must be non-capital, not owned by ROOT, cored by ROOT, not claimed by ROOT, not host-survival-reserved, not already claimed by Border Commission, and owned by a country with more than the configured state floor. This satisfies the "expand beyond one-state starts without erasing hosts" design in current script.

MAP-specific check:

- `independence_wave_map_mapuche_land_petitions_effect` adds cores to Aysen `949` and Rio Negro `512`.
- No `add_claim_by = ROOT` remains in that MAP effect, matching the parent correction.

### News Release List

Classification: **Proven**

Successful releases are stored in `global.independence_wave_country_1` through `global.independence_wave_country_16`; scripted localisation `GetIndependenceWaveReleasedCountryList` selects the matching list by actual release count. The news event uses that scripted localisation. This covers all current wave releases up to the configured maximum of 16.

### Generic Shared Focus Tree

Classification: **Proven**

The active focus tree file defines `independence_wave_liberation_provisional_tree`. The runtime loader applies it to Event006-origin releases that have not already loaded the provisional tree. Current generic niche custom tags `ASN`, `KBN`, `PLM`, and `AYM` are explicitly restored as ordinary/niche generic releases rather than package overlays. The tree contains 50 focus blocks by focused `rg` count.

No active Event006 KUB/ALT focus or decision surfaces were found.

### Event005 Separation

Classification: **Weak/Needs validation**

Proven pieces:

- Event006-origin releases receive `chaosx_release_origin_independence_wave`.
- Event005 `soviet_collapse_setup_breakaway_country` is wrapped in a guard: `NOT = { has_country_flag = chaosx_release_origin_independence_wave }`.
- Event005 `soviet_collapse_load_event_created_focus_tree` is also wrapped in that guard.
- Event006 achievements check Event006 origin and key shared-tag achievements explicitly exclude Soviet Collapse flags.

Remaining risk:

- Event005 has large legacy breakaway arrays, decision target arrays, national focuses, and custom successor setup functions. This audit did not fully prove that an Event006 shared tag can never be touched by any Event005 downstream system if some external path manually adds Event005 flags or arrays.

### Evolution Log

Classification: **Proven for current active evolution writes**

Only four active `record_events_log_evolution_entry` calls were found, all inside `independence_wave_record_tier_evolution_log_entry`:

- `independence_wave_evolution_gathering_storm_logged`
- `independence_wave_evolution_rising_cascade_logged`
- `independence_wave_evolution_old_names_logged`
- `independence_wave_evolution_impossible_statehood_logged`

The only current call site found is `events/006_independence_wave.txt` after `global.independence_wave_actual_release_count > 0`.

Risk:

- Many package and formation "record log entry" helpers remain defined and set event-log variables. They do not directly call `record_events_log_evolution_entry` in the inspected state, but future edits could accidentally wire package-level entries back into the evolution writer.

### MAP And Flags

Classification: **Weak/Needs validation**

MAP package exists as a real custom tag:

- `common/country_tags/chaosx_countries.txt`
- `common/countries/MAP - Mapuche Land Congress.txt`
- `history/countries/MAP - Mapuche Land Congress.txt`
- `localisation/english/chaosx_countries_l_english.yml`
- MAP package scoring/seed/effects/triggers/decisions

MAP flag handoff records upright `TopLeft` files:

- `gfx/flags/MAP.tga`
- `gfx/flags/medium/MAP.tga`
- `gfx/flags/small/MAP.tga`

Gap:

- No MAP ideology-variant flags or DDS files were found. If the requirement is interpreted as base unique flag only, MAP is covered. If it means parity with other custom countries' ideology flag set, MAP is incomplete.

### Achievements

Classification: **Proven present, Weak for unlock validation**

Found 19 Event006 achievement gameplay definitions, localisation keys, GFX sprite declarations, and asset files:

- `cr_independence_without_patron`
- `cr_five_small_flags`
- `cr_suppression_failed`
- `cr_brokers_exposed`
- `cr_partition_without_war`
- `cr_first_old_name`
- `cr_old_name_modern_state`
- `cr_local_land_congress`
- `cr_railway_country`
- `cr_impossible_recognition`
- `cr_not_the_collapse`
- `cr_charter_becomes_state`
- `cr_charter_not_chains`
- `cr_the_ledger_votes_back`
- `cr_human_renunciation`
- `cr_league_war_victory`
- `cr_no_more_flags_needed`
- `cr_capital_still_answers`

Oddity:

- `cr_capital_still_answers` is placed after unrelated common achievements in `common/achievements/chaos_redux_achievements.txt`, while its localisation/GFX remain in the Event006 sections. The brace check passed, so this is not proven broken, but it is structurally untidy and should be reviewed before a final completion claim.

### Super Events And Audio

Classification: **Proven references, Weak runtime**

Found Event006 super-event sprites, image files, music assets, sound assets, `.ogg`, and `.wav` files for:

- first league
- human renunciation
- league war
- first old name
- great partition week
- first impossible state
- rump that endures

`independence_wave_emit_super_event` sets `global.current_super_event_audio_id` and calls `play_current_super_event_audio` for human players. Runtime display/playback was not tested.

### Workbook And Catalog

Classification: **Weak/Needs validation**

`openpyxl` was unavailable, so the workbook could not be loaded through the preferred structured spreadsheet workflow. Read-only `.xlsx` XML inspection found the current Event006 row text includes:

- immediate hidden resolver
- host-survival state reservation
- shrink/skip unsafe releases
- Event006 origin
- startup divisions and army-building support
- shared 50-focus Liberation Provisional tree
- Border Commission recovery of surveyed unowned cores without consuming protected host states
- current management surfaces
- seven bounded super-events
- 19 current achievements
- status remains "In progress"

This aligns with current implementation direction, but full spreadsheet parity is still weak because the workbook was not opened/recalculated through a spreadsheet engine and no full row-by-row catalog audit was performed.

## Validation Commands Run

Representative read-only checks:

```bash
rg -n "focus_tree|id =|country =|available_if_capitulated|tag =|original_tag|ASN|KBN|PLM|AYM|MAP|KUB|ALT|ai_will_do|completion_reward|icon =" common/national_focus/006_independence_wave_focus.txt
rg -n "record_.*log_entry|record_events_log_evolution_entry|evolution_.*logged|independence_wave_event_log\\." events/006_independence_wave.txt common/decisions/006_independence_wave_decisions.txt common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/script_constants/006_independence_wave_constants.txt localisation/english/006_independence_wave_l_english.yml
rg -n "\\b(KUB|ALT|Kuban|Altai|kuban|altai)\\b" events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/decisions/006_independence_wave_decisions.txt common/national_focus/006_independence_wave_focus.txt localisation/english/006_independence_wave_l_english.yml common/ideas/006_independence_wave_ideas.txt common/script_constants/006_independence_wave_constants.txt interface/006_independence_wave_icons.gfx
rg -n "<=|>=" events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/decisions/006_independence_wave_decisions.txt common/national_focus/006_independence_wave_focus.txt common/script_constants/006_independence_wave_constants.txt localisation/english/006_independence_wave_l_english.yml
awk '...' events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt common/scripted_triggers/006_independence_wave_triggers.txt common/decisions/006_independence_wave_decisions.txt common/national_focus/006_independence_wave_focus.txt common/script_constants/006_independence_wave_constants.txt common/scripted_guis/006_independence_wave_scripted_guis.txt interface/006_independence_wave_scripted_gui.gui interface/006_independence_wave_icons.gfx interface/006_independence_wave_report_event_images.gfx interface/006_independence_wave_news_event_images.gfx interface/chaosx_achievements.gfx interface/chaosx_super_events.gfx
for f in localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_countries_l_english.yml localisation/english/chaosx_achievements_l_english.yml; do xxd -p -l 3 "$f"; done
rg -n "^[^#\\n]*:0" localisation/english/006_independence_wave_l_english.yml localisation/english/chaosx_countries_l_english.yml localisation/english/chaosx_achievements_l_english.yml
find gfx/flags -maxdepth 2 -type f \( -name 'ASN*' -o -name 'KBN*' -o -name 'PLM*' -o -name 'AYM*' -o -name 'MAP*' -o -name 'DFR*' -o -name 'ZUL*' \) | sort | xargs -r file
unzip -p docs/spreadsheets/chaos_redux_events_catalog.xlsx xl/sharedStrings.xml | tr '<' '\\n' | rg -i "Event 006|Event 6|Independence Wave|chaosx\\.nr6|006_independence|independence wave" -C 2
```

Results:

- No `<=` or `>=` found in focused Event006 files.
- Focused brace-balance check returned no errors.
- Sampled Event006 localisation files are UTF-8 BOM.
- No `:0` localisation keys found in sampled Event006/country/achievement localisation.
- Active Event006 KUB/ALT references are only candidate exclusions.
- Workbook XML contains current Event006 row text, but spreadsheet-engine validation was skipped because `openpyxl` is unavailable.

## Skipped Validation

- No HOI4 launch or game-load validation.
- No live event fire in game.
- No in-game check of release loop, host survival, focus tree assignment, super-event playback, news text, decision tooltips, or achievement unlocks.
- No full Event005 downstream array/decision/focus audit beyond targeted origin/focus-loader checks.
- No full localisation missing-key audit across every Event006 focus, decision, idea, achievement, event-log/detail key.
- No image visual inspection for every flag, icon, report image, news image, achievement icon, or super-event.
- No full spreadsheet parse/recalc because `openpyxl` is missing; workbook was inspected through XML only.
- No git status/diff/commit operations.

## Parent Action List

Highest-impact remaining gaps before any completion claim:

1. Run or perform the parent-level live validation scenarios: manual Event006 fire at multiple chaos tiers, multi-host wave, capital-cored candidate skip, reduced-core Border Commission recovery, news list with several releases, and Event005 shared-tag separation.
2. Decide whether MAP must have ideology-variant flags/DDS parity and whether custom formables require unique flag assets beyond current country tags.
3. Do a full Event005 cross-system exclusion audit for Event006-origin shared tags, especially arrays, targeted decisions, custom successor setup functions, and focus side effects.
4. Complete final spreadsheet/catalog/event-detail parity with a real spreadsheet engine or LibreOffice validation, then update only from implemented facts.
5. Close or explicitly carry forward remaining queued plan work: final package/formable balance, package-specific presentation/animation manifests where accepted, final localisation missing-key audit, and final scripted GUI/runtime UI checks.
