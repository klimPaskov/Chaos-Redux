# Event 019 English localisation completion handoff

## Outcome

The English player-facing localisation package for Event 019 Infantry Spawn is complete across the live event, formation-incident, management, claimant, derivative-country, Muster Board, Event Log, and direct-caller scenario surfaces. The later SCN-013 integration supplies its shared launcher text in `chaosx_gui_l_english.yml`.

The main Event 019 localisation file now contains 1,201 unique keys. It covers every explicit live source reference found in the audited Event 019 scripts, including all 104 references for formation incidents `chaosx.nr19.300` through `chaosx.nr19.312`, along with the complete claimant identity library, generic history text for future registry families, and the full derivative cosmetic-tag matrix.

The five Muster Board selector contracts now resolve to live definitions in the existing Event 019 scripted-localisation file. The exact selector names, source values, and localisation mappings remain recorded below as a verification contract.

No registry file, launcher row, scenario ID, visual asset, or gameplay script was created by this localisation tranche.

## Files changed

- `localisation/english/019_infrantry_spawn_l_english.yml`
  - complete Event 019 English localisation package
  - complete titles, descriptions, options, and exact effect tooltips for formation incidents `chaosx.nr19.300` through `chaosx.nr19.312`
  - existing misspelled filename preserved
  - UTF-8 BOM preserved
- `localisation/english/chaosx_event_names_l_english.yml`
  - corrected `chaosx.event_name.19` from `Infrantry Spawn` to `Infantry Spawn`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_localisation_completion_handoff.md`
  - this completion record and selector contract

`localisation/english/chaosx_achievements_l_english.yml` was audited only. Its concurrent Event 019 achievement localisation was not edited by this subagent.

## Coverage completed

### Events, reports, and Event Log

- hidden entry title `chaosx.nr19.1.t`
- manifestation report `chaosx.nr19.2` with all three live options
- four evolution reports `chaosx.nr19.101` through `chaosx.nr19.104`
- five claimant reports `chaosx.nr19.200` through `chaosx.nr19.204`
- thirteen formation-incident reports `chaosx.nr19.300` through `chaosx.nr19.312`, each with a title, origin-state description, three option names, and three exact custom-effect tooltips
- four Event Log evolution entries and summary
- Event Details premise `chaosx.events_log.window.event_details.infantry_spawn`
- all fourteen supported history payloads:
  - `infantry_spawn.history.claimant_appearance.{title,description}`
  - `infantry_spawn.history.claimant_takeover.{title,description}`
  - `infantry_spawn.history.failed_coup.{title,description}`
  - `infantry_spawn.history.claimant_revolt.{title,description}`
  - `infantry_spawn.history.zombie_revolt.{title,description}`
  - `infantry_spawn.history.ghost_revolt.{title,description}`
  - `infantry_spawn.history.golem_revolt.{title,description}`
  - `infantry_spawn.history.anomalous_revolt.{title,description}`
  - `infantry_spawn.history.zombie_defeat.{title,description}`
  - `infantry_spawn.history.ghost_defeat.{title,description}`
  - `infantry_spawn.history.golem_defeat.{title,description}`
  - `infantry_spawn.history.anomalous_defeat.{title,description}`
  - `infantry_spawn.history.claimant_defeat.{title,description}`
  - `infantry_spawn.history.scenario_launch.{title,description}`

### Direct-caller scenario

- four type names and explanatory tooltips
- four intensity names and explanatory tooltips
- confirmation report `infantry_spawn_scenario_confirmation`
- setup-complete report `infantry_spawn_scenario_setup_complete`
- setup-failed report `infantry_spawn_scenario_setup_failed`
- request, launch, repeat-launch, and invalid-input tooltips
- `infantry_spawn_scenario_muster_council`
- `infantry_spawn_scenario_unbidden_assembly`

SCN-013 launcher-row and numeric registry localisation are supplied by the later shared Triggerable Scenarios integration; this tranche remains the owner of the direct confirmation and result reports.

### Decisions, missions, focuses, ideas, and AI-visible effect text

- all 65 live Event 019 decision, mission, and category identifiers have names and descriptions
- every explicit decision trigger, cost, and effect tooltip is defined
- the derivative focus-tree name and all 45 derivative focus names, descriptions, and custom effect tooltips are defined
- all 57 main and derivative idea identifiers have names and descriptions
- claimant, ordinary-lot, anomalous-family, and derivative-country prices use the live variables and script constants
- visible effects identify route locks, idea changes, family outcomes, equipment grants, command resources, stability, war support, and decision unlocks

### Muster Board

All 114 unique text and tooltip references in `interface/019_infantry_spawn_muster_board.gui` are defined.

Coverage includes:

- window controls and all five tabs
- Muster Control, Army Congestion, Equipment Debt, and Anomalous Saturation cards
- five Evolution III formation-request modes with full live price aliases
- formation-lot list, selected-lot accounting, and all lot actions
- claimant identity, demand, standing, and all six claimant responses
- anomalous-family list, selected-family pressure and sustainment data, and all seven family actions
- recent muster-generation history

The five selector calls present in the localisation values and verified against live source definitions are:

- `[This.GetInfantrySpawnSelectedClaimantArchetype]`
- `[This.GetInfantrySpawnSelectedClaimantDemand]`
- `[This.GetInfantrySpawnSelectedClaimantStatus]`
- `[This.GetInfantrySpawnSelectedFamilyName]`
- `[This.GetInfantrySpawnMusterFamilyName]`

The verified source contract for these five calls is below.

### Claimant identity library

- 20 distinct profile titles and descriptions:
  - `infantry_spawn_claimant_profile_01` through `infantry_spawn_claimant_profile_20`
  - matching `_desc` keys
- 80 fictional personal-name variants:
  - `infantry_spawn_claimant_name_01_1` through `infantry_spawn_claimant_name_20_4`
- 20 raw portrait tokens:
  - `infantry_spawn_claimant_portrait_token_01` through `infantry_spawn_claimant_portrait_token_20`
  - values remain the raw numeric strings `01` through `20`
- five raw commander-trait token keys:
  - `infantry_spawn_claimant_traits_quartermaster: "logistics_wizard"`
  - `infantry_spawn_claimant_traits_prophet: "offensive_doctrine"`
  - `infantry_spawn_claimant_traits_tribune: "organizer"`
  - `infantry_spawn_claimant_traits_saint: "defensive_doctrine"`
  - `infantry_spawn_claimant_traits_marshal: "inflexible_strategist"`
- fallback `infantry_spawn_claimant_name_unrecorded`

The 80 personal names follow the region and male gameplay metadata of the 20 claimant profiles. They are fictional and do not rely on real public figures. Their fixed technical portrait sprites display region-compatible army/muster identity scenes rather than the named people.

### Derivative identities

All six required generated leader keys are defined:

- `infantry_spawn_derivative_zombie_host_commander_name`
- `infantry_spawn_derivative_zombie_host_council_name`
- `infantry_spawn_derivative_ghost_host_commander_name`
- `infantry_spawn_derivative_ghost_host_council_name`
- `infantry_spawn_derivative_golem_master_builder_name`
- `infantry_spawn_derivative_golem_pattern_council_name`

All 13 live cosmetic tags have a complete 15-key matrix:

- base name, `_DEF`, and `_ADJ`
- democratic name, `_DEF`, and `_ADJ`
- communism name, `_DEF`, and `_ADJ`
- fascism name, `_DEF`, and `_ADJ`
- neutrality name, `_DEF`, and `_ADJ`

This produces 195 cosmetic localisation keys. The 13 source tags are:

- `INFANTRY_SPAWN_CLAIMANT_BREAKAWAY`
- `INFANTRY_SPAWN_ZOMBIE_BASE`
- `INFANTRY_SPAWN_ZOMBIE_CLAIMANT`
- `INFANTRY_SPAWN_ZOMBIE_COLLECTIVE`
- `INFANTRY_SPAWN_ZOMBIE_SPECIES`
- `INFANTRY_SPAWN_GHOST_BASE`
- `INFANTRY_SPAWN_GHOST_CLAIMANT`
- `INFANTRY_SPAWN_GHOST_COLLECTIVE`
- `INFANTRY_SPAWN_GHOST_SPECIES`
- `INFANTRY_SPAWN_GOLEM_BASE`
- `INFANTRY_SPAWN_GOLEM_CLAIMANT`
- `INFANTRY_SPAWN_GOLEM_COLLECTIVE`
- `INFANTRY_SPAWN_GOLEM_SPECIES`

## Verified selector contract

All five definitions are live in `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`. The mappings below record the values checked during the final localisation audit.

### Selected claimant archetype

Live selector:

`GetInfantrySpawnSelectedClaimantArchetype`

Primary board variable:

`infantry_spawn_muster_gui_claimant_archetype`

The board copies it from:

`infantry_spawn_claimant_archetype_entries^infantry_spawn_selected_claimant_index`

Exact mapping from `infantry_spawn_claimant_archetype`:

| Value | Constant | Localisation key |
| --- | --- | --- |
| 0 | `constant:infantry_spawn_claimant_archetype.none` | `infantry_spawn_claimant_archetype_none` |
| 1 | `constant:infantry_spawn_claimant_archetype.quartermaster_sovereign` | `infantry_spawn_claimant_archetype_quartermaster_sovereign` |
| 2 | `constant:infantry_spawn_claimant_archetype.field_prophet` | `infantry_spawn_claimant_archetype_field_prophet` |
| 3 | `constant:infantry_spawn_claimant_archetype.barracks_tribune` | `infantry_spawn_claimant_archetype_barracks_tribune` |
| 4 | `constant:infantry_spawn_claimant_archetype.iron_saint` | `infantry_spawn_claimant_archetype_iron_saint` |
| 5 | `constant:infantry_spawn_claimant_archetype.hollow_marshal` | `infantry_spawn_claimant_archetype_hollow_marshal` |

Use the `none` key as the final default.

### Selected claimant demand

Live selector:

`GetInfantrySpawnSelectedClaimantDemand`

Persistent selected-row value:

`infantry_spawn_claimant_demand_entries^infantry_spawn_selected_claimant_index`

The selector requires `infantry_spawn_selected_claimant_index_is_valid = yes` before testing the array row.

Exact mapping from `infantry_spawn_claimant_demand`:

| Value | Constant | Localisation key |
| --- | --- | --- |
| 0 | `constant:infantry_spawn_claimant_demand.none` | `infantry_spawn_claimant_demand_none` |
| 1 | `constant:infantry_spawn_claimant_demand.formal_appointment` | `infantry_spawn_claimant_demand_formal_appointment` |
| 2 | `constant:infantry_spawn_claimant_demand.equipment_share` | `infantry_spawn_claimant_demand_equipment_share` |
| 3 | `constant:infantry_spawn_claimant_demand.autonomous_district` | `infantry_spawn_claimant_demand_autonomous_district` |
| 4 | `constant:infantry_spawn_claimant_demand.another_formation` | `infantry_spawn_claimant_demand_another_formation` |
| 5 | `constant:infantry_spawn_claimant_demand.political_seat` | `infantry_spawn_claimant_demand_political_seat` |
| 6 | `constant:infantry_spawn_claimant_demand.emergency_powers` | `infantry_spawn_claimant_demand_emergency_powers` |

Use `infantry_spawn_claimant_demand_none` as the final default and when no claimant row is valid.

### Selected claimant status

Live selector:

`GetInfantrySpawnSelectedClaimantStatus`

Persistent selected-row value:

`infantry_spawn_claimant_status_entries^infantry_spawn_selected_claimant_index`

The selector requires `infantry_spawn_selected_claimant_index_is_valid = yes` before testing the array row.

Exact mapping from `infantry_spawn_claimant_status`:

| Value | Constant | Localisation key |
| --- | --- | --- |
| 0 | `constant:infantry_spawn_claimant_status.inactive` | `infantry_spawn_claimant_status_inactive` |
| 1 | `constant:infantry_spawn_claimant_status.emerging` | `infantry_spawn_claimant_status_emerging` |
| 2 | `constant:infantry_spawn_claimant_status.recognized` | `infantry_spawn_claimant_status_recognized` |
| 3 | `constant:infantry_spawn_claimant_status.demanding` | `infantry_spawn_claimant_status_demanding` |
| 4 | `constant:infantry_spawn_claimant_status.countermanded` | `infantry_spawn_claimant_status_countermanded` |
| 5 | `constant:infantry_spawn_claimant_status.retired` | `infantry_spawn_claimant_status_retired` |
| 6 | `constant:infantry_spawn_claimant_status.arrested` | `infantry_spawn_claimant_status_arrested` |
| 7 | `constant:infantry_spawn_claimant_status.takeover` | `infantry_spawn_claimant_status_takeover` |
| 8 | `constant:infantry_spawn_claimant_status.revolt_staged` | `infantry_spawn_claimant_status_revolt_staged` |
| 9 | `constant:infantry_spawn_claimant_status.revolted` | `infantry_spawn_claimant_status_revolted` |
| 10 | `constant:infantry_spawn_claimant_status.defeated` | `infantry_spawn_claimant_status_defeated` |

Use `infantry_spawn_claimant_status_inactive` as the final default and when no claimant row is valid.

### Selected and dynamic-list anomalous family names

Live selectors:

- `GetInfantrySpawnSelectedFamilyName`
- `GetInfantrySpawnMusterFamilyName`

Variables:

- selected family card: `infantry_spawn_muster_gui_selected_family_id`
- dynamic family list row: `infantry_spawn_muster_gui_family_id`

Exact built-in family mapping:

| Value | Constant | Localisation key |
| --- | --- | --- |
| 501 | `constant:event19_zombie_family.family_id` | `infantry_spawn_family_name_base_dead` |
| 502 | `constant:event19_ghost_family.family_id` | `infantry_spawn_family_name_pale_procession` |
| 503 | `constant:event19_golem_family.family_id` | `infantry_spawn_family_name_coal_golem` |
| any other value | external or unavailable family row | `infantry_spawn_family_name_unrecorded` |

Both selectors use the same mapping against their respective variable. This remains compatible with future external Event 019 family providers because an unknown family receives the explicit in-world default without adding or changing a registry row.

## Achievement localisation audit

The live achievement file contains 11 Event 019 achievements. The concurrent achievement localisation file defines all 33 required achievement-facing keys:

- 11 `_NAME` keys
- 11 `_DESC` keys
- 11 exact-condition tooltip keys

`infantry_spawn_achievement_eligible_tooltip` is also present. Hidden achievement conditions remain confined to hidden achievement entries and their own achievement surfaces. No Event 019 gameplay, event, decision, focus, idea, Muster Board, Event Log, or scenario prose reveals hidden achievement conditions.

## Source and validation audit

- 603 unique references were extracted from live localisation-bearing fields across the two Event 019 event files, three decision files, derivative focus tree, two idea files, Muster Board GUI, Event 019 scripted localisation, scenario scripted localisation, and Event Log scripted localisation. All 603 resolve.
- the generic anomalous-revolt and anomalous-defeat history titles and descriptions resolve through the live Event Log payload mappings without assuming a zombie, ghost, or golem identity
- all 104 live title, description, option-name, and custom-effect-tooltip references for `chaosx.nr19.300` through `chaosx.nr19.312` resolve
- all 13 incident descriptions use the stored `[infantry_spawn_incident_state.GetName]` origin scope
- all incident costs, debt adjustments, lot ratings, status and command changes, supply burdens, claimant susceptibility changes, resistance consequences, and lasting formation affinities match the live scripted effects
- all 65 decision, mission, and category identifiers resolve to names and descriptions
- all 45 focus identifiers resolve to names and descriptions, and the focus-tree identifier resolves to its tree name
- all 57 idea identifiers resolve to names and descriptions
- all 114 Muster Board GUI references resolve
- all 212 localisation aliases resolve
- all 231 script-constant insertions resolve to live constants, including the 24 distinct incident constants used by the formation reports
- all 84 ordinary variable insertions occur in the live Event 019 source
- all 13 source cosmetic tags have exactly 15 localisation keys
- all 80 claimant personal-name keys, 20 profile keys, 20 portrait tokens, five trait tokens, and six derivative leader keys are present
- all five Muster Board selector calls resolve to live scripted-localisation definitions
- the Event 019 file contains 1,201 localisation keys with no duplicates
- the Event 019 and event-name localisation files retain UTF-8 BOM encoding
- no `:0` suffix, leading-key indentation, em dash, semicolon, malformed quoted key line, unresolved localisation alias, or extra blank line at end of file remains

The live source no longer contains the transient leading `+` before `GetInfantrySpawnSelectedClaimantName`, and the derivative focus wrappers around the claimant, ghost, and golem branches are structurally present. Those earlier concurrent defects are resolved and are not remaining blockers.

## Simplifications, omissions, and blockers

- SCN-013 is registered by the shared Triggerable Scenarios integration; no remaining localisation blocker belongs to this handoff.
- The existing filename `019_infrantry_spawn_l_english.yml` remains misspelled to preserve every live path and reference.
- No formation-incident effect was generalized or omitted. Every option reports its live costs and consequences, including lasting affinity and demobilization-resistance behavior.
- No player-facing localisation, claimant profile, derivative identity, cost, effect tooltip, scenario type, scenario intensity, Event Log payload, achievement surface, or cosmetic matrix was simplified or omitted.

## Skills and references

This tranche used `chaos-redux-events` and `chaos-redux-subagents`, the required offline Paradox wiki pages, official vanilla localisation documentation, vanilla localisation precedents, and the complete Event 019 spec package. No skill required an update because this work introduced no reusable workflow absent from the current repo skills.

## Git handoff

No files were staged and no subagent commit was created. The shared worktree contains concurrent parent and sibling changes, and the parent owns final staging and commit.
