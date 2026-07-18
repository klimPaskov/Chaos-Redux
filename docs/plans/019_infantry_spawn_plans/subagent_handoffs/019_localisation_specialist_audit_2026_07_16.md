# Event 019 Localisation Specialist Audit

Date: 2026-07-16

Mode: source-stable specialist audit with narrow localisation, documentation,
and workbook corrections. No gameplay logic, Event 006 content, Event 015
content, registry file, or asset file was edited by this audit. No commit was
created.

## Verdict

The Event 019 English localisation package is complete across the audited live
surfaces. No open P0, P1, or P2 localisation defect remains.

The audit found one engine-breaking P0 scripted-localisation field error and
several P1 and P2 wording or alignment defects. They are resolved in the shared
source-stable package. The 91 regional derivative identities and their matching
asset package are also stable.

Two gameplay limitations remain outside localisation. Four exact battle
achievements remain hidden and fail closed, and exact natural ownership transfer
of a recorded division remains approval-blocked. No fallback was introduced for
either limitation.

## P0, P1, and P2 findings

| ID | Priority | Finding | Resolution |
| --- | --- | --- | --- |
| `L10N-019-01` | P0 | The main Event 019 scripted-localisation file used the invalid British field `localisation_key` 273 times. HOI4 requires `localization_key`. | Replaced all 273 occurrences. The file now contains 273 valid fields and zero invalid fields. Every referenced key resolves. |
| `L10N-019-02` | P1 | The first regional country-name matrix used `[This.GetLeader.GetName]` in 84 identities and `[This.Capital.GetName]` in country-name localisation. Those namespaces are not reliable in country cosmetic names. | Raised during integration. The parent replaced every regional matrix value with a static direct country name. The final 273 base name, definite article, and adjective values contain zero localisation namespaces and are all unique. |
| `L10N-019-03` | P1 | `Every Barracks a Front` named internal scenario types instead of the visible names and described exact actor bookkeeping. | Reworded to `The Generals' Muster`, `The Impossible Host`, `Maximum`, and hostile governments raised by the launch. The achievement documentation was aligned. |
| `L10N-019-04` | P1 | Several visible decision, mission, achievement, derivative, and Muster Board strings described proof rows, exact records, implementation labels, or provider bookkeeping instead of the world state and player action. | Rewrote the affected strings in in-world military language while preserving every cost, lock, refund, salvage, duration, route, and disqualifier contract. |
| `L10N-019-05` | P2 | Event documentation and workbook evolution cells used prohibited semicolons or em dashes, and the medium scenario summary still said derivative hosts. | Cleaned the three Event 019 documents and aligned the workbook to the live title, body, and breakaway-host wording. |
| `L10N-019-06` | P2 | The older `019_localisation_completion_handoff.md` records pre-integration counts and selector coverage. | This dated audit supersedes that handoff for current counts and completeness evidence. |

## Coverage evidence

### Localisation files and references

| Surface | Current evidence |
| --- | --- |
| Main Event 019 localisation | 2,722 keys, 2,722 unique, no malformed rows, no duplicate keys, no `:0`, no leading key indentation, UTF-8 BOM present |
| Shared achievements localisation | 573 keys, 573 unique, clean structure, UTF-8 BOM present |
| Shared GUI localisation | 882 keys, 882 unique, clean structure, UTF-8 BOM present |
| Shared Chaos Meter localisation | 367 keys, 367 unique, clean structure, UTF-8 BOM present |
| Shared event-name localisation | 100 keys, 100 unique, clean structure, UTF-8 BOM present |
| Explicit reference sweep | 1,017 unique candidates, 118 structural GUI or GFX identifiers filtered, 899 true localisation-bearing references, zero missing |
| Implicit display pairs | 203 content identifiers, 406 required display keys, zero missing |
| Localisation aliases | 373 unique `$KEY$` aliases, zero missing |
| Main scripted localisation | 14 `defined_text` blocks, 273 `localization_key` uses, 165 unique targets, zero missing, zero invalid British fields |
| Scenario scripted localisation | 6 `defined_text` blocks, 24 `localization_key` uses, 16 unique targets, zero missing, zero invalid British fields |

Neither Event 019 scripted-localisation file contains direct `§` or `£`
formatting characters.

### Decisions, missions, focus tree, ideas, and achievements

The current live source resolves both name and description keys for:

- 64 decisions
- 13 missions
- 3 decision categories
- 45 derivative focuses
- 67 ideas, made up of 25 ordinary-country ideas and 42 derivative ideas
- 11 achievements

All 11 achievements have `_NAME`, `_DESC`, and exact-condition tooltip text.
The shared eligibility tooltip also resolves. The four exact-battle entries that
the engine cannot yet prove remain hidden in the achievement registry, so their
conditions do not leak through ordinary gameplay surfaces.

### Events, evolutions, Event Log, and Event Details

- Visible report `chaosx.nr19.917` resolves its title, description, and option.
- The four evolution records resolve as `Organized Muster`, `Arsenal Lottery`,
  `Command Fracture`, and `Anomalous Muster`.
- Each evolution title is wired into the live list, history detail, event detail,
  and selected-evolution selectors.
- Each evolution body is wired into the selected-evolution detail selector.
- All 14 Event 019 history payload types have both title and description keys.
- `chaosx.events_log.window.event_details.infantry_spawn` resolves and matches
  the workbook Event Details premise exactly.
- Hidden support events that intentionally expose no report text were not given
  invented localisation.

### Claimant and anomalous routes

The claimant library contains:

- 20 profile titles
- 20 profile descriptions
- 80 fictional personal names
- 20 raw portrait tokens
- 160 personal-name selector branches across the two live selectors
- 42 portrait selector branches including the two safe defaults
- 8 live demand branches plus the no-demand default
- 10 live status branches plus the inactive default
- 5 live archetype branches plus the no-archetype default
- 3 live prototype-disposition branches plus the unmanaged default
- 3 built-in anomalous-family branches in both family-name selectors

This includes the two Generalissimo demand values in addition to the original
six claimant demands.

### Regional derivative identities

The live matrix is 13 identity stems crossed with 7 origin regions, producing
91 regional tags. Every tag has all 15 required country localisation keys:

- base name, definite article, and adjective
- democratic name, definite article, and adjective
- communism name, definite article, and adjective
- fascism name, definite article, and adjective
- neutrality name, definite article, and adjective

Final matrix evidence:

| Check | Result |
| --- | --- |
| Regional tags | 91 |
| Expected keys | 1,365 |
| Missing keys | 0 |
| Incorrect ideology aliases | 0 |
| Base name, definite article, and adjective values | 273 |
| Unique base values | 273 |
| Localisation namespaces in base values | 0 |
| Semicolons or em dashes in the matrix | 0 |

The 13 unsuffixed identity flags and country names remain intact as source
designs and compatibility identities. They are not counted as substitutes for
the 91 regional rows.

The regional asset specialist confirmed the matching stable package:

- 91 source composites
- 273 processed PNGs
- 273 runtime TGAs
- exact `INFANTRY_SPAWN_<IDENTITY>_<REGION>` naming at all sizes
- no asset failure, fallback, or filename deviation

### Muster Board

All player-facing text and tooltips used by the five Muster Board tabs resolve:

- overview
- formation lots
- claimants
- anomalous families
- recent muster history

The audit also covered action buttons, selection states, prices, accounting
rows, lock explanations, empty states, route labels, family selectors, claimant
selectors, and animated or static UI toggle tooltips. Structural GUI object names
were kept separate from localisation references.

### Triggerable scenarios

- Event 019 owns live scenario identity `SCN-013`.
- Shared localisation resolves `chaosx.scenarios.entry.id.infantry_spawn` as
  `#013`.
- The direct-caller confirmation, setup success, setup failure, four type names,
  four type descriptions, four intensity names, four intensity descriptions,
  launch tooltips, and two generated leader names resolve.
- Event 006 remains the sole owner of `SCN-008` and was not edited.
- The shared IDs remain independent at raw values 8 for Independence Wave, 11
  for Africa, and 13 for Infantry Spawn.

## Documentation and workbook alignment

The following source-of-truth surfaces now match the current player-facing
localisation:

- `docs/events/019_infantry_spawn.md`
- `docs/achievements/019_infantry_spawn_achievements.md`
- `docs/systems/019_infantry_spawn_triggerable_scenario.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Workbook evidence:

- `Events!C20` exactly matches the Event Details premise.
- `Events!D20:G20` exactly match the four evolution title and body pairs using
  `Title: Body` punctuation.
- The four evolution cells retain style IDs 50, 51, 52, and 53.
- `Scenarios!E11` exactly contains the four current intensity summaries and uses
  `breakaway hosts` at Widespread intensity.
- `Scenarios!E11` retains style ID 83.
- The workbook ZIP package opens without a corrupt member.

The three Event 019 documents, main Event 019 localisation, both Event 019
scripted-localisation files, regional identity matrix, and Event 019 achievement
section contain no semicolon or em dash.

## Files changed by this audit

### Scripted localisation

- `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`
  - changed 273 invalid `localisation_key` fields to `localization_key`
  - did not create, remove, or rename a selector

### Player-facing localisation

- `localisation/english/019_infrantry_spawn_l_english.yml`
  - refined the following exact keys:
    - `infantry_spawn_scenario_intensity_medium_tt`
    - `infantry_spawn_select_next_unaccounted_lot_tt`
    - `infantry_spawn_settle_selected_lot_obligations_tt`
    - `infantry_spawn_open_standardization_cycle_tt`
    - `infantry_spawn_supervised_demobilization_tt`
    - `infantry_spawn_issue_common_tables_tt`
    - `infantry_spawn_preserve_specialist_companies_tt`
    - `infantry_spawn_preserve_prototype_formation_tt`
    - `infantry_spawn_cannibalize_advanced_lot_tt`
    - `infantry_spawn_request_selected_anomalous_family_tt`
    - `infantry_spawn_request_selected_anomalous_family_cost`
    - `infantry_spawn_sustain_selected_family_tt`
    - `infantry_spawn_standardization_cycle_mission_desc`
    - `infantry_spawn_supervised_demobilization_mission_desc`
    - `infantry_spawn_prototype_maintenance_trial_mission_desc`
    - `infantry_spawn_derivative_rally_claimant_guard_decision_tt`
    - `infantry_spawn_derivative_replace_claimant_decision_tt`
    - `infantry_spawn_derivative_crown_the_claimant_desc`
    - `infantry_spawn_muster_gui_debt_tt`
    - `infantry_spawn_muster_gui_anomalous_footer`
    - `infantry_spawn_emergency_field_integration_tt`
    - `infantry_spawn_derivative_concentrated_sustainment_method_desc`
    - `infantry_spawn_muster_gui_selected_lot_accounting`
- `localisation/english/chaosx_achievements_l_english.yml`
  - refined the Event 019 eligibility tooltip and all 11 Event 019 condition
    tooltips
  - changed `019_infantry_spawn_one_battalion_wonder_DESC` from generated to
    unbidden language

The existing misspelled filename `019_infrantry_spawn_l_english.yml` was
preserved because it is the established live file path. It was not renamed.

### Documentation and workbook

- `docs/events/019_infantry_spawn.md`
  - aligned the derivative identity and 91-flag asset inventory
  - cleaned prohibited punctuation
- `docs/achievements/019_infantry_spawn_achievements.md`
  - aligned `Every Barracks a Front` with the visible scenario names
  - cleaned prohibited punctuation
- `docs/systems/019_infantry_spawn_triggerable_scenario.md`
  - cleaned prohibited punctuation without changing the SCN-013 contract
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
  - aligned `Events!D20:G20` punctuation
  - aligned `Scenarios!E11` with `breakaway hosts`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_localisation_specialist_audit_2026_07_16.md`
  - this audit record

These files already contained concurrent parent and sibling work. The list above
describes this audit's exact ownership inside the shared diffs.

## Superseded counts

`019_localisation_completion_handoff.md` remains useful as an earlier selector
record, but its completion counts no longer describe the live package. This
audit supersedes the following old claims:

- main localisation count from 1,201 to 2,722 keys
- decision, mission, and category count from 65 to 80 identifiers
- idea count from 57 to 67
- cosmetic coverage from 13 unsuffixed tags to 91 regional tags, while retaining
  the 13 compatibility identities
- claimant demand coverage from values 0 through 6 to eight live demand branches
  plus the default
- explicit reference coverage from 603 to 899 true localisation-bearing refs

## Registry invariant

The repository contains exactly one file named
`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.

No registry file was created, renamed, copied, or edited by this audit. Event
documentation and the asset GFX handoff both point to that sole registry.

## Simplifications, omissions, and blockers

### Localisation audit

No localisation surface was simplified or omitted. No placeholder, fallback,
weaker substitute, missing regional identity, missing achievement string,
missing UI state, or hardcoded substitute was introduced.

### Blockers outside localisation

- `019_infantry_spawn_one_battalion_wonder`
- `019_infantry_spawn_combined_arms_accident`
- `019_infantry_spawn_borrowed_future`
- `019_infantry_spawn_barracks_of_babel`

These four achievements remain hidden and unawarded because the engine does not
currently expose the complete exact tuple of participating recorded division,
enemy strength ratio, battle duration, and same-battle casualty evidence. Their
localisation is complete, but gameplay completion remains fail closed.

Natural exact transfer of a recorded division between owners also remains
blocked pending owner approval of the documented design choice. No unrelated
division is selected and no approximate transfer fallback was added.

## Skills and references

Skills used:

- `chaos-redux-events`
- `chaos-redux-subagents`
- `xlsx`

The audit consulted the required offline Paradox wiki pages, including
Localisation, Data Structures, Triggers, Effects, Scopes, Events, Decisions,
Ideas, AI, Interface Modding, Scripted GUI Modding, National Focus Modding,
Country Creation, and Achievement Modding. It also consulted the installed
vanilla documentation and vanilla localisation precedents. The offline
Localisation page and vanilla source both confirm that scripted localisation
requires the American `localization_key` field spelling.

No reusable skill gap was found, so no skill was created or updated.

## Git handoff

No files were staged. No subagent commit was created. The parent owns final diff
review, staging, and the plan commit.
