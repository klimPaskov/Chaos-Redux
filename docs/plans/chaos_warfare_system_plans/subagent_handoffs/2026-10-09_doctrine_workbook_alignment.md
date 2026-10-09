# Doctrine workbook alignment handoff — 2026-10-09

Disposition: implemented as a parent-authorized transcription of current Chaos Warfare doctrine, localisation, idea, and helper sources into the separate doctrine workbook.

## Files changed

- `docs/spreadsheets/doctrines.xlsx`
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-09_doctrine_workbook_alignment.md`

No gameplay files, event-catalog files, or CSV exports were edited, and no commit or index changes were made.

## Workbook delta

`Overview` changed only `C6`, replacing the stale Chaos Warfare description with the exact `CBRN_BALANCED_CHAOS_WARFARE_DESC` text used by the current grand-doctrine source; the existing name, declared track-key order, and literal subdoctrine count of four were checked and already correct.

`chaos_warfare` changed the current description in `A2`, grand-doctrine base effects in `B3`, track labels and section names, mastery rules, track milestone entries, subdoctrine descriptions and activations, reward names and effect blocks, and the Chaos Warfare spirit table.

Exact existing-row value changes were: `A2`, `B3`, `A5:A6`, `B8:B11`, `D13:E16`, `E17`; `A19:A20`, `B22:B25`, `D27:E28`, `C29:E29`, `D30:E31`; `A33:A34`, `B36:B39`, `D41:E44`, `E45`; `A48`, `B50:B53`, `D55:E56`, `E57`, `D58:E59`; `A62`, `C64:E64`, and `A65:E66`.

Rows `67:70` were added for current and dormant spirit definitions using the existing spirit-entry cell styles; the original suggestions section and both suggestion rows moved from `67:70` to `71:74` with their values and styles preserved.

The physical doctrine-section order remains as it was in the workbook, while its labels now report source track order accurately: Armor is Track 3, Infantry Track 1, Combat Support Track 2, and Operations Track 4.

The reward mastery threshold values remain numeric `100` in all twenty `Required Mastery` cells, matching the workbook's original data type and the current file-local reward constants.

The grand doctrine uses `GFX_doctrine_chaos_warfare_medium` in the current source; the template has no separate icon column, so the workbook cell delta was limited to its existing fields.

## Source transcription

The grand doctrine description and the four subdoctrine descriptions come from the exact `CBRN_BALANCED_*_DESC` keys referenced by current doctrine source, in `localisation/english/cbrn_doctrine_balance_l_english.yml`.

The localized doctrine and reward names come from `localisation/english/chaosx_doctrines_l_english.yml`; all twenty reward keys and their effect blocks were transcribed from the current four subdoctrine files with the file-local numeric constants resolved from those same files.

The mastery multipliers and explicit eligible-unit rosters are: Hazard Assault 12.00 with five roles, Contaminant Fire Support 16.00 with three roles, Toxic Armored Warfare 14.00 with three roles, and Integrated CBRN Command 14.00 with six roles.

The rows record the source-declared `sub_units` lists and localized role names; they do not claim measured mastery pace or engine-effective aggregation behavior.

The four grand milestone rows contain the current recorder calls and the helper behavior that each sets its corresponding `cbrn_native_*_track_complete` flag and requests available doctrine-technology grants; the source-only note leaves native milestone trigger timing unverified.

The spirit section now lists six current gated definitions: three `army_spirit` entries and three `division_command_spirit` entries, with exact names, descriptions, gates, and source-backed primary effects.

The prior `chemical_air_deep_strike_spirit` entry is retained in row 70 as a dormant legacy definition because its current source sets `visible = { always = no }`, `available = { always = no }`, and AI factor zero; it is not represented as a selectable CBRN spirit.

The two suggestion rows remain suggestions and were moved intact to rows 73 and 74.

Consulted gameplay source files were `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt`, all four `common/doctrines/subdoctrines/land/chaos_warfare_*_subdoctrines.txt` files, `common/script_constants/cbrn_doctrine_constants.txt`, `common/scripted_effects/cbrn_doctrine_effects.txt`, `common/ideas/cbw_spirits.txt`, and `common/scripted_localisation/cbrn_doctrine_value_localisation.txt`.

Consulted localization files were `localisation/english/cbrn_doctrine_balance_l_english.yml`, `localisation/english/chaosx_doctrines_l_english.yml`, `localisation/english/cbrn_doctrine_l_english.yml`, `localisation/english/chaosx_ideas_l_english.yml`, `localisation/english/chaosx_units_l_english.yml`, and `localisation/english/cbrn_hq_l_english.yml`.

All fifteen consulted source-file SHA-256 values were captured before candidate creation and verified unchanged immediately before workbook replacement.
The durable [workbook review](../../../testing/2026-10-09_doctrine_workbook_alignment/workbook_review.json) retains the source hashes, declared cell edits, final cell delta and parent checks.

## Hashes and preservation evidence

The working workbook began as a Git LFS pointer with SHA-256 `2b8fb73d033fb9db549fc8eac9843e44b2028c79e05b20fd5726feea7ba46451`.

The pointer resolved to the verified local LFS object `.git/lfs/objects/44/33/44339d686c1163d682092cd441af752dc1f4685d77485d6f5892db1f2b1fbbe5`, SHA-256 `44339d686c1163d682092cd441af752dc1f4685d77485d6f5892db1f2b1fbbe5`, size 111,933 bytes; the immutable pre-edit copy is `.tmp/cbrn_doctrine_workbook_20261009/before-doctrines.xlsx`.

The final workbook SHA-256 is `108293159cd1f96594e31cfd686effa8f489303c6504b482b9a9bf5513adf11e`.

The workbook reopened successfully with the expected seven sheets, and all fifteen original ZIP member names remain present.
The writer reserialized thirteen XML payloads; package membership preservation does not mean those payloads are byte-identical.

Semantic comparisons confirmed that all cells and styles outside the declared Chaos Warfare and Overview changes remain unchanged, including every vanilla doctrine sheet and `vanilla_land_officer_spirits`; the suggestion content and styles are unchanged after their row shift.

Existing merges, freeze panes (`A44` on `chaos_warfare`), filters, validations, defined names, view settings, column widths, and original row heights were preserved; the Chaos Warfare sheet retains five columns and 31 original merged ranges.

The workbook has no formulas, so no recalculation was needed; visual application inspection was not performed.

The event-catalog CSV exporter was not run because `doctrines.xlsx` is the independent doctrine workbook and has no catalog exporter.

## Remaining limits

No unresolved player-facing doctrine or reward wording was found in the requested fields, so no cells were marked `blocked` or `needs_user_review`.

Engine-native mastery aggregation, milestone trigger timing, effective full-stack modifiers, and in-game presentation remain unverified; the workbook records those limits and this handoff makes no in-game validation claim.

Skill used: `chaos-redux-xlsx`.
