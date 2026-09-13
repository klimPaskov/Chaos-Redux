# Event 027 Doctrine Research postfix localisation audit

Requested handoff stamp: 2026-08-30

Mode: fresh read-only audit of the current live workspace after the parent fixes and workbook resynchronization. No event, gameplay, localisation, scripted localisation, documentation source, workbook, or CSV export was edited.

## Verdict

The repaired package passes mechanical localisation coverage, action-specific confirmation routing, institutional stage naming, five-value History payload coverage, Event Details/evolution/cluster alignment, hidden-router documentation accuracy, and authoritative workbook/export parity.

Final localisation sign-off is still withheld. The mandatory one-to-one event-popup render remains unavailable because both current MCP render attempts timed out after 180 seconds. Source length cannot prove wrapping, clipping, or option overflow. Two player-facing strings also retain the internal label `Event 027`, and the successful-action interstitial `.8` does not show the remaining-choice count even though its trigger requires an active batch. The actionable selection and continuation pages do show the count.

## Files and exact audited revisions

| File | Lines or size | SHA-256 |
| --- | ---: | --- |
| `localisation/english/027_doctrine_research_l_english.yml` | 335 lines | `C709A8A1D0A5C279BB1D459F3CAD8F426F3368676571C2D1DA407AB09494344A` |
| `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt` | 1,382 lines | `42B2710A8225096C246CF1262EE11D33CE78A0EDE13274EF46CCA8CE1522DED4` |
| `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` | 13,915 lines | `B6EE297D1A1FED58CAEBDB71761726D2D4AA6F12F003675E0E25E234C2A7160E` |
| `common/scripted_effects/chaosx_logic_effects.txt` | 1,754 lines | `36F95EEB52786CD7DB678A687C23FA2120020F1372943C1C52DFF1F44C9DA461` |
| `common/scripted_effects/027_doctrine_research_effects.txt` | 3,458 lines | `5BCFDEE0D17E503FFCD46E0D6FB3CB722D867146D7E5088B22541E5A7C2E0734` |
| `events/027_doctrine_research.txt` | 4,862 lines | `08946D48E168FF2E4B90A7E12642BBA5C1712BF527F04C70399BBB79C48FF703` |
| `docs/events/027_doctrine_research/overview.md` | 160 lines | `AD630B7B195B41DE1367BA114A01D3DB8718A3099094E33BAE0463973F14AF00` |
| `docs/spreadsheets/chaos_redux_events_catalog.xlsx` | 85,513 bytes | `EBF20975C1FBA51DC68CCCBC0DFBAE62C7805683464A24F2422CFDC9825B972E` |
| `docs/spreadsheets/chaos_redux_events_catalog.csv` | 166 parsed rows | `48E639A8D8632BEA3838C9C3EC8E4E473517722D3945A844666131CC4BDD75BB` |
| `docs/spreadsheets/chaos_redux_clusters_catalog.csv` | 16 parsed rows | `77B2509D31B0E86CC20A1CFB226FA9412B31EED59EC713E9C1AFE2E352A8597E` |
| `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` | 15 parsed rows | `05A5E47238CF23E12A3AC6BA09720106460B42A212B553563F1069E70F139EEE` |

The live `chaosx_logic_effects.txt` and overview changed during this audit. They were re-read after the concurrent edits, and the hashes above identify the final state assessed here.

## Exact mechanical counts

| Check | Count | Result |
| --- | ---: | --- |
| Event 027 English localisation keys | 334 | Pass |
| Unique Event 027 English localisation keys | 334 | Pass |
| Duplicate keys inside the Event 027 English file | 0 | Pass |
| Event 027 keys duplicated elsewhere under `localisation/english/` | 0 | Pass |
| Direct event key occurrences (`title`, `desc`, option `name`, `custom_effect_tooltip`) | 420 | Pass |
| Unique direct event keys | 261 | Pass |
| Missing direct event keys | 0 | Pass |
| `GetDoctrineResearch*` calls in Event 027 English localisation | 235 occurrences, 118 unique | Pass |
| `GetDoctrineResearch*` `defined_text` definitions | 118, all unique | Pass |
| Missing definitions for called selectors | 0 | Pass |
| Unreferenced Event 027 `defined_text` definitions | 0 | Pass |
| `GetDoctrineResearchOptionStatus*` calls | 107, all unique | Pass |
| `GetDoctrineResearchOptionStatus*` definitions | 107, all unique | Pass |
| Missing or unused option-status definitions | 0 | Pass |
| Unique scripted-localisation output keys | 160 | Pass |
| Output keys resolved in Chaos Redux localisation | 45 | Pass |
| Output keys resolved in installed vanilla English localisation | 115 | Pass |
| Unresolved scripted-localisation output keys | 0 | Pass |
| Top-level Event 027 country events | 30 | Pass |
| Hidden events | 2: `.1` and `.6` | Pass |
| Visible events | 28 | Pass |
| Visible events missing a title or description | 0 | Pass |
| External Event Log, Event Details, evolution, cluster, event-name, and achievement keys checked | 28 | Pass |
| Root achievement IDs checked | 3, each defined once | Pass |

The 107 option-status calls remain distributed as follows: `.60` 9, `.61` 9, `.62` 8, `.63` 10, `.64` 6, `.65` 8, `.66` 6, `.67` 6, `.68` 6, `.69` 6, `.70` 6, `.71` 7, `.72` 8, `.73` 8, and `.74-.77` one each.

## Missing key list

None.

- All 261 unique direct event references resolve.
- All 118 unique scripted-localisation calls resolve to one definition.
- All 160 unique selector outputs resolve to current mod or installed vanilla localisation.
- The Event Log, static Event Details, five History details, four evolution titles, four evolution bodies, evolution type, cluster name and description, Event 027 display name, and achievement surfaces resolve.

## Duplicate key list

None.

- Event 027 English-file duplicates: 0.
- Duplicate definitions of those 334 keys elsewhere under `localisation/english/`: 0.
- `chaosx.event_name.27` is present once.
- The three root achievement IDs occur once each at `common/achievements/chaos_redux_achievements.txt:4203`, `:4208`, and `:4213`.

## Scripted localisation findings

The earlier unused `GetDoctrineResearchLastResultName` definition is gone. All 118 current `GetDoctrineResearch*` definitions have a caller.

`GetDoctrineResearchConfirmationDescription` now selects between adoption and mastery text and has a neutral invalid-selection fallback. Both valid action variants include the current remaining-choice value. The mastery variant includes Grand Doctrine, track, subdoctrine, current mastery, maximum mastery, next mastery, completion status, and Milestone status. The adoption variant correctly omits subdoctrine mastery state.

All 107 option-status definitions remain one-to-one with their visible option calls. Their state order still covers complete, Mastery 5 through Mastery 1, selected at Mastery 0, and the unselected fallback. No raw subdoctrine ID can emerge from a missing option-status selector.

## Remaining-choice display

The earlier actionable-flow gap is repaired.

- Twenty-three direct descriptions show `doctrine_research_batch_remaining_choices`: `.2`, `.3`, `.4`, `.5`, `.60-.77`, and `.9`.
- Both valid dynamic confirmation descriptions selected by `.7.d` show the same value.
- Therefore every opening, domain, Grand Doctrine, track, subdoctrine-selection, valid confirmation, and continuation page shows the remaining count.
- `.8` is a successful-action interstitial whose trigger still requires `doctrine_research_active_batch`. It says that one choice was spent but does not say how many remain. It immediately routes to `.9` when choices remain or `.10` when none remain. Under a strict reading of “every active page,” this is one remaining coverage gap.
- `.11` and `.12` also occur while the batch flag exists, but they are fail-closed/no-option terminal handling rather than actionable curriculum pages. Their omission is not treated as an actionable-choice display defect.

## Action-specific confirmation and result wording

The generic confirmation is repaired. Adoption and mastery no longer share a description, and neither valid path displays irrelevant `No Subdoctrine` data.

No player-facing Event 027 value contains the words `receipt`, `queue`, `queued`, `ledger`, `array`, `rebuild`, `duplicate`, or `implementation`. The key `chaosx.nr27.7.rebuild` retains an internal identifier, but its visible value is the natural `Review the available doctrine choices`.

Two visible values still expose the internal event number:

- `localisation/english/027_doctrine_research_l_english.yml:286`, `doctrine_research.confirm.adoption`: “without granting an Event 027 mastery step.”
- `localisation/english/027_doctrine_research_l_english.yml:289`, `doctrine_research.result.detail.adoption`: “granted no Event 027 mastery step.”

This contradicts the requested no-internal-jargon standard. The intended distinction is useful, but it should be expressed as “does not advance a subdoctrine” or equivalent player-facing doctrine language.

## Current, next, maximum, completion, and Milestone wording

All 18 track descriptions `.60-.77` include:

- selected domain, Grand Doctrine, and track;
- current subdoctrine;
- current and maximum mastery;
- next mastery;
- completion status; and
- Milestone status.

The mastery confirmation repeats all six relevant state fields before commitment. Adoption confirmation intentionally does not show mastery progression. The summary continues to report whether a Milestone was reached. Option-state strings now use natural `Advance from Mastery X to Mastery Y` wording instead of arrow notation.

## Institutional stage names

The five player-facing curriculum stages are now institutional rather than global Chaos-tier labels:

1. Foundational
2. Expanded
3. Advanced
4. Joint-Service
5. Comprehensive

`GetDoctrineResearchStageName` maps exactly five runtime stages to these keys and retains `Unclassified` only as a fail-closed fallback. History details and evolution titles use the same names. No current player-facing Event 027 localisation says `Calm World`, `Gathering Storm`, `Rising Chaos`, `Chaos Tier`, or `Totalen Chaos`.

## Exact five History payloads

The earlier static-History mismatch is repaired.

- `common/script_constants/027_doctrine_research_constants.txt:27-31` defines the five batch sizes as 1, 2, 3, 4, and 5.
- `common/scripted_effects/027_doctrine_research_effects.txt:1691-1700` prepares the immutable firing profile and copies its size to `global.doctrine_research_last_firing_size`.
- `common/scripted_effects/chaosx_logic_effects.txt:1281-1289` passes that size as the Event 027 History payload before recording the row.
- `record_events_log_history_entry` stores the override in `global.events_log_history_payload_entries`.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5938-5973` contains exactly five Event 027 payload branches, one for each batch-size constant, followed by the generic Event Details fallback.
- The five History keys at Event 027 localisation lines 304-308 state one, two, three, four, and five choices and use Foundational, Expanded, Advanced, Joint-Service, and Comprehensive respectively.

No sixth payload branch, duplicate payload value, missing History key, or payload-to-wording mismatch was found.

## Event Details, evolution, cluster, and workbook alignment

The static Event Details wording now states the complete one-to-five progression and explains both Grand Doctrine establishment and one-step subdoctrine mastery.

The four evolution titles use Expanded, Advanced, Joint-Service, and Comprehensive. Their four bodies state exactly two, three, four, and five choices. The National Breakthroughs description no longer says that each event “validates its own owner system”; it describes the cluster in player-facing institutional terms.

Six authoritative workbook strings were compared character for character with localisation:

- Event 27 `Details`;
- Event 27 `Evo I` through `Evo IV`; and
- Cluster 9 `Details`.

All six are exact matches.

The workbook-to-export comparison used every non-empty workbook row and every CSV cell:

| Sheet/export | Workbook non-empty rows | CSV rows | Cell mismatches |
| --- | ---: | ---: | ---: |
| Events / `chaos_redux_events_catalog.csv` | 166 | 166 | 0 |
| Clusters / `chaos_redux_clusters_catalog.csv` | 16 | 16 | 0 |
| Scenarios / `chaos_redux_scenarios_catalog.csv` | 15 | 15 | 0 |

The Event 27 workbook row remains `Needs Testing`, and Cluster 9 remains `Partially Available`. These statuses are consistent with the documented open validation work and do not contradict the localisation.

## Documentation alignment

`docs/events/027_doctrine_research/overview.md:82` now accurately says that `.6` is hidden and `.60-.77` are visible track pages. Line 90 documents the immutable one-to-five History payload. Line 92 honestly retains the rendered pagination/overflow limitation. No stale claim that `.60-.77` are hidden remains.

## Achievement audit

The three achievements remain complete and unique:

- `027_doctrine_research_first_lesson`
- `027_doctrine_research_single_school`
- `027_doctrine_research_joint_curriculum`

Each has `_NAME`, `_DESC`, eligibility tooltip, and condition tooltip coverage. Their public requirements remain clear and do not expose arrays, flags, receipts, or transaction state. No achievement/localisation mismatch was found.

## File encoding concerns

No encoding blocker was found.

- `localisation/english/027_doctrine_research_l_english.yml` begins with UTF-8 BOM.
- `localisation/english/chaosx_event_names_l_english.yml` begins with UTF-8 BOM.
- All three exported CSVs begin with UTF-8 BOM.
- The Event 027 English file has one `l_english:` header, 334 parseable one-line keys, no `:0` suffixes, and no leading indentation before keys.
- Script, Markdown, and XLSX containers do not require a localisation BOM.

## Cross-surface mismatch notes

No Event Details/evolution/cluster/workbook/export mismatch remains. No stage-name mismatch remains. No hidden-router documentation mismatch remains. No History payload-to-description mismatch remains.

The remaining cross-surface concern is visual rather than textual: source strings are substantially longer than a normal prose-only review can certify against the standard event-popup consumer.

## Prose-quality findings

### Vagueness

The principal vague/internal phrase is `Event 027 mastery step` in the adoption confirmation and result. Players should be told that adoption does not advance a subdoctrine.

### Bloat and overflow risk

- All 18 track descriptions are 658 source characters before dynamic substitution.
- The mastery confirmation is 577 source characters.
- The completed-batch summary is 543 source characters.
- The opening description is 422 source characters.

These strings carry useful state, but the repeated label sequence creates a material wrapping risk. Without the production popup render, their visual acceptability is unproved.

### Obvious explanation

The adoption confirmation and result both explain that no `Event 027` mastery step was granted. The distinction from subdoctrine advancement is useful once, but the internal event number is unnecessary and the result repeats the same implementation-framed distinction.

### Repetition

The 18 track descriptions intentionally share one template and differ through dynamic tokens. This preserves consistency but means any overflow defect affects every track page. No accidental repeated sentence was found within an individual description.

### Overcomplication

The action-specific selectors have reduced the previous overloaded confirmation. The mastery confirmation remains dense because it presents five state labels plus context and commitment behavior. This is acceptable only if the popup render proves clean wrapping.

### Style-rule repair still needed

The two `Event 027` phrases are the only current player-facing internal-label violations found. No em dash or sentence semicolon occurs in the Event 027 English localisation. No sourced quotation is present.

## Dynamic text opportunities

1. Add the remaining-choice value to `.8.d` if the acceptance standard literally includes every page whose trigger requires `doctrine_research_active_batch`.
2. Replace both `Event 027 mastery step` phrases with dynamic-token-preserving, player-facing subdoctrine language.
3. If popup evidence shows overflow, split the track status into a shorter dynamic status sentence rather than removing current, maximum, next, completion, or Milestone information.

## Sourced-quotation preservation notes

No sourced or attributed quotation appears in the inspected Event 027 event pages, Event Details, History details, evolution text, cluster text, achievement text, overview summary, workbook row, or CSV exports. No quotation required preservation, and no text was altered.

## MCP inspection and popup evidence

The mandatory read-only Event MCP route was used against the current workspace.

- A full scan request with 240 nodes and helper expansion timed out after 180 seconds.
- A reduced scan with 80 nodes and no helper expansion succeeded as `EVENT_INSPECTED_PARTIAL` in workspace `mod_chaos_redux_ea3b2d67c2c0`.
- Current scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/489e46de1f7cd5761d3752ad9fa24244756a3783f59d319f87d4703f038c6b3b/d76dbf8a8401bb075601e598775a80e6a9355e7290ffe7e0c6c7cd407f270dc1/event-scan-02410b498829.json`
- The current `entries` render with 80 nodes timed out after 180 seconds.
- The current `overview` render with 80 nodes also timed out after 180 seconds.

The successful scan is structural and source-linked. It is not a one-to-one standard event-popup image and cannot verify text width, wrapping, clipping, option height, or background containment. Accordingly, popup overflow remains an explicit blocker and this handoff does not grant final localisation sign-off.

## Blockers

1. One-to-one production popup evidence is unavailable. Both current render routes timed out, so overflow cannot be accepted from source inspection.
2. `doctrine_research.confirm.adoption` and `doctrine_research.result.detail.adoption` expose the internal label `Event 027`.
3. Under the literal “every active page” requirement, `.8.d` lacks a remaining-choice display despite requiring `doctrine_research_active_batch`. All actionable selection and continuation pages pass.

## Recommended fixes

1. Replace `Event 027 mastery step` at localisation lines 286 and 289 with `subdoctrine mastery step`, `advance a subdoctrine`, or equivalent wording that preserves the gameplay distinction.
2. Decide whether the successful-action interstitial is included in the remaining-choice acceptance rule. If yes, add the current remaining value to `chaosx.nr27.8.d`.
3. Retry a supported one-to-one standard event-popup render after the current MCP timeout condition clears. Review `.60-.77`, mastery confirmation, `.10`, and the longest option labels at production scale.

## Meaningful validation performed

- Re-read every user-named source, workbook, and export from the live workspace.
- Re-ran direct-key, duplicate-key, scripted-call, definition, option-status, output-key, visible-page, and achievement coverage checks.
- Re-resolved all 160 scripted-localisation outputs against current Chaos Redux and installed vanilla English localisation.
- Traced all five History values from constants through firing-size capture, History payload storage, selector branches, and visible wording.
- Compared six authoritative workbook fields character for character with localisation.
- Compared every non-empty workbook cell with all three exported CSVs.
- Re-read the shared logic and overview after concurrent changes landed during the audit.
- Ran the mandatory read-only Event MCP inspection and attempted both detailed and overview renders.

## Skipped or blocked meaningful validation

- One-to-one event-popup layout evidence is blocked by two current 180-second MCP render timeouts.
- No live game run was performed. That remains outside the agent workflow.

## Changed files

- `docs/plans/027_doctrine_research_plans/subagent_handoffs/localisation_auditor_postfix_2026-08-30.md`

No source/gameplay/localisation/workbook/CSV file was changed.

## Simplifications, omissions, and uncertainty

No audit surface requested by the parent was omitted. The only unresolved evidence is production popup layout. The interpretation of whether `.8` counts as an “active page” is stated explicitly rather than silently waived.
