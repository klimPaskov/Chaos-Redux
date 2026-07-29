# Event 019 Live Final Localisation Re-audit

Date: 2026-07-16

Mode: live-source specialist re-audit. This subagent did not edit gameplay,
localisation, scripted localisation, GUI, GFX, assets, registries, or the
workbook. The only file created by the subagent is this handoff. Parent-agent
remediations that landed while the audit was active were re-read and included
in the final result.

## Final verdict

The live Event 019 English player-facing contract passes the assigned final
re-audit. Exact open severity counts are:

| Priority | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |

Two findings were observed and corrected during the audit. Both are closed in
the live end state:

| ID | Priority | Observed finding | Final state |
| --- | --- | --- | --- |
| `L19-LIVE-01` | P1 | `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Scenarios!C11/E11`, retained pre-remediation SCN-013 wording and mixed the direct-report copy with the shared launcher catalog. | Closed. `C11`, `D11`, and `E11` now equal text re-derived from the exact shared SCN-013 launcher keys. All three retain style 83 and wrapped text. Workbook ZIP integrity passes. |
| `L19-LIVE-02` | P2 | `infantry_spawn_supervised_demobilization_tt` contained a semicolon, contrary to the Event 019 writing contract. | Closed. `localisation/english/019_infrantry_spawn_l_english.yml:308` now uses two sentences. The main Event 019 file has zero player-facing semicolons and zero em dashes, and its UTF-8 BOM remains present. |

No other P0, P1, or P2 defect was found.

## SCN-013 direct and shared wording disposition

The direct and shared key families are both current and intentionally serve
different contexts. Their wording differences are not stale localisation:

- `infantry_spawn_scenario_type_*` and `_tt`, plus
  `infantry_spawn_scenario_intensity_*` and `_tt`, are selected by
  `common/scripted_localisation/019_infantry_spawn_scenario_scripted_localisation.txt`
  for the direct caller's confirmation and setup reports
  `chaosx.nr19.951` through `.953`.
- `chaosx.scenarios.type.infantry_spawn.*`,
  `chaosx.scenarios.infantry_spawn.desc.*`, the shared
  `chaosx.scenarios.intensity.*` labels, and
  `chaosx.scenarios.infantry_spawn.impact.*` are selected by
  `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
  for the shared Triggerable Scenarios row and shared confirmation.
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md:126` documents that
  ownership split. The direct path uses atmospheric pattern/reach wording;
  the shared launcher uses its standard type/intensity vocabulary and an
  explicit immediate-war warning.

The `Scenarios` workbook sheet catalogs the shared launcher, so row SCN-013 is
canonically sourced as follows:

- `C11`: for `conventional_flood`, `arsenal_lottery`, `general_mutiny`, and
  `anomalous_rising`, concatenate
  `chaosx.scenarios.type.infantry_spawn.<type>`, `: `, and
  `chaosx.scenarios.infantry_spawn.desc.<type>`, with a blank line between
  entries.
- `D11`: concatenate the same four
  `chaosx.scenarios.type.infantry_spawn.<type>` values with comma-space
  separators.
- `E11`: for `low`, `medium`, `high`, and `maximum`, concatenate
  `chaosx.scenarios.intensity.<level>`, `: `, and
  `chaosx.scenarios.infantry_spawn.impact.<level>`, with a blank line between
  entries.

Workbook convention stores plain visible prose. `E11` therefore removes only
the HOI4 presentation codes `section-sign R` and `section-sign !` while
retaining the complete warning sentences. The final workbook contains zero
section-sign formatting tokens. Exact cell-to-derived-text comparison passes
for `C11`, `D11`, and `E11`.

The workbook also preserves the requested identity: Event ID `19`, type
`Minor Repeatable`, blank Cluster ID, blank Member Severity, and an intentional
`In progress` status for both Event 019 and SCN-013.

## Completion matrix

| Surface | Live result |
| --- | --- |
| English key integrity | `019_infrantry_spawn_l_english.yml` has 2,881 keys, all unique. The four shared files have 882 GUI, 573 achievement, 101 event-name, and 367 chaos-meter keys, each internally unique. Cross-file duplicates among the five audited files: 0. All five retain UTF-8 BOM. No `:0` keys or leading key indentation occur in the main file. |
| Explicit references | The field-aware Event 019 source sweep classified 395 live localisation references, 382 unique, with 0 missing. Structural GFX/dynamic tokens were checked against their consumers rather than misclassified as YML keys. |
| Events and options | 48 Event 019 event definitions exist across the main and scenario files: 35 visible and 13 hidden. The two event files contribute 182 unique Event 019 localisation references, all resolved. The root report selects the baseline or highest applied Evolution I-IV description in exact descending order. All material options expose their wired effect text. |
| Decisions, missions, categories | 68 decisions and 14 missions have all 164 required name/description keys. Three categories have all six name/description keys. Across all three decision files, 52 custom-cost bases have all 156 required base/blocked/tooltip variants. All 75 explicit decision trigger/effect tooltip references resolve. |
| Focuses | Exactly 45 derivative focuses have all 90 name/description keys. The focus-tree identifier itself is structural and is not counted as a forty-sixth focus. |
| Ideas | Exactly 42 derivative ideas have all 84 required display keys. Including the 25 staged/ordinary Event 019 ideas, all 67 idea identifiers have all 134 name/description keys. |
| Claimant text | All 20 profile titles, 20 profile descriptions, 80 regional male names, 20 technical portrait-number tokens, and neutral unrecorded values resolve. Profile region and diaspora wording matches the live regional gates. No player-facing Event 019 value uses stale female or focal-individual wording. |
| Army/host scene selectors | Scripted localisation returns exactly 27 Event 019 GFX scene tokens: 20 regional claimant army/muster scenes, six massed host/council scenes, and one neutral unassigned muster. All 27 tokens are defined and their textures exist. The technical `portrait` identifiers are retained as allowed compatibility identifiers; the displayed slots contain no focal individual. |
| Leader gender contract | Claimant creation fixes `female = no` and validation requires `is_female = no`. Zombie, ghost, and golem human commanders and all three institutional councils use `female = no`; both direct-scenario institutional leaders do likewise. Player-facing text contains no contradictory gender wording. |
| Derivative country identities | Thirteen identity stems (one claimant and twelve anomalous derivative identities) have all 1,365 regional name/definite/adjective keys across seven regions and five government contexts, plus all 195 unsuffixed compatibility keys. All 273 regional and 39 unsuffixed large/medium/small flag files exist. |
| SCN-013 | Both contexts are complete: four direct type names/tooltips, four direct reach names/tooltips, four shared type names/descriptions, and four shared intensity names/impacts. Confirmation, success, failure, ID, name, and four blocked-launch explanations resolve. The direct/shared differences are intentional as documented above. |
| Muster Board | `interface/019_infantry_spawn_muster_board.gui` has 125 unique text, button, and tooltip references; all 125 resolve. Tabs, overview, lot accounting, claimant, anomalous-family, history, animation, cost, empty-state, and lock copy are covered. |
| Achievements | Exactly 11 achievements have all 22 name/description keys, all 11 condition tooltips, and the shared eligibility tooltip: 34 required keys, 0 missing. Controlled-trial wording reflects the accepted exact recreate/prove/delete contract and does not introduce a fallback. |
| Event Log and Event Details | `chaosx.event_name.19`, the Event Details premise, the four evolution title/body pairs, and all 18 live history payload title/description pairs resolve. The 18 payload constants equal the 18 title selectors and 18 description selectors exactly. Evolution titles are present in all four shared title contexts and bodies in the detail context. |
| Shared integration copy | The shared GUI contains 18 Event 019-specific scenario keys. Achievement localisation contributes the 34 keys above. Ghost-decline deaths use both the shared breakdown-line key and the Event 019 cause-name key; both resolve through reason 20. |
| Dynamic tokens and formatting | Across the five audited files, 380 unique `$KEY$` aliases resolve with 0 missing and no malformed bracket, dollar, or section-format pair. Both Event 019 scripted-localisation files contain no direct section or icon formatting characters. All 203 referenced Event 019 script constants resolve. The incident state scope is backed by its saved event target. |
| Costs, cooldowns, locks | Displayed dynamic costs, cooldowns, mission durations, lock reasons, and family-management durations resolve to live variables/constants. The fixed 30% demobilisation share, 45% specialist/cannibalisation share, and 120-365-day prototype range match their live constants and effect paths. No stale cost, cooldown, or lock claim was found. |
| Writing and identity hygiene | The main Event 019 player-facing values contain zero semicolons, zero em dashes, and zero update-history, fallback, provider, registry-row, array-row, debug, or engine-failure vocabulary. The earlier ten localisation findings are all absent from the live end state. |

## Event Log/history set equality

The exact 18 payloads are `claimant_appearance`, `claimant_takeover`,
`failed_coup`, `claimant_revolt`, `zombie_revolt`, `ghost_revolt`,
`golem_revolt`, `anomalous_revolt`, `zombie_defeat`, `ghost_defeat`,
`golem_defeat`, `anomalous_defeat`, `claimant_defeat`, `scenario_launch`,
`first_family_cantonment`, `first_family_negotiated`,
`first_family_refused`, and `first_family_reception_failed`. Every constant has
one current title and one current description mapping; no extra selector or
unmapped payload remains.

The evolution contract is likewise exact: `Organized Muster`, `Arsenal
Lottery`, `Command Fracture`, and `Anomalous Muster`, each with its current
body text and Event Details preview row.

## Files and references inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/xlsx/SKILL.md`
- the complete Event 019 specification and matrix package under
  `docs/specs/019_infantry_spawn_specs/`, plus the live near-completion addendum
- both Event 019 event files; all Event 019 decision/category, focus, idea,
  achievement, scripted-localisation, scripted-GUI, GUI, claimant, derivative,
  scenario, Event Log, Event Details, chaos-meter, and identity sources needed
  to trace the assigned text
- the five English localisation files listed in the completion matrix
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, read-only, including
  exact Event row and SCN-013 cell comparisons
- required offline wiki pages: Data structures, Triggers, Effects, Modifiers,
  Localisation, Scopes, On actions, Event modding, Decision modding, Idea
  modding, and AI modding
- current vanilla localisation, script-concept, effect, trigger, and
  conditional-event documentation and precedents

## Simplifications, omissions, skills, and Git

No assigned localisation surface was omitted, simplified, or replaced with a
fallback. No open player-facing defect, placeholder, missing key, stale
identity, gender mismatch, unreported workbook divergence, or weaker
substitute was accepted.

Skills used:

- `chaos-redux-subagents`
- `chaos-redux-events`
- `xlsx` (read-only workbook parity and integrity inspection)

No skill was created or updated. No gameplay, localisation, asset, or workbook
file was edited by this subagent. No file was staged and no commit was created;
the parent owns final integration, staging, and the meaningful-plan commit.
