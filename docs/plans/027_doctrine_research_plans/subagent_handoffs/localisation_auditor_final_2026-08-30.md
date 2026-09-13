# Event 027 Doctrine Research final localisation audit

Date: 2026-08-30

Mode: fresh read-only source audit. No gameplay, localisation, scripted localisation, workbook, event-log, achievement, or documentation source was patched.

## Verdict

The Event 027 localisation package is mechanically complete at the key and scripted-localisation reference level, but it is not ready for a clean final localisation sign-off.

Mechanical coverage is strong. The Event 027 English file contains 333 unique keys, all 261 direct Event 027 references resolve, and all 107 `GetDoctrineResearchOptionStatus*` calls have exactly one matching definition. The event-log, Event Details, evolution, achievement, debug-name, and workbook keys inspected are present and unique.

Final sign-off remains blocked by player-facing implementation leakage, incomplete remaining-choice presentation, a non-dynamic History detail, generic confirmation wording that mixes adoption and mastery state, and missing visual overflow proof for the standard event popup pages.

## Scope and sources inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/xlsx/SKILL.md`
- all 16 files in `docs/specs/027_doctrine_research_specs/`
- the required offline wiki core pages, with the localisation and event-localisation sections reviewed directly
- installed vanilla `documentation/script_concept_documentation.md` localisation sections
- installed vanilla doctrine localisation used by Event 027 scripted localisation
- `events/027_doctrine_research.txt`
- `localisation/english/027_doctrine_research_l_english.yml`
- `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`
- Event Log, Event Details, evolution, cluster, debug-name, and achievement consumers
- `docs/events/027_doctrine_research/overview.md`
- authoritative `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Current source fingerprints used for this audit:

| File | Lines | SHA-256 |
| --- | ---: | --- |
| `events/027_doctrine_research.txt` | 4,862 | `08946D48E168FF2E4B90A7E12642BBA5C1712BF527F04C70399BBB79C48FF703` |
| `localisation/english/027_doctrine_research_l_english.yml` | 334 | `D4794BE98AFFC9B481AEFF14D5B79B6A0501240E06494EAC46D8FA180D44B7D7` |
| `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt` | 1,390 | `3076DEABB9EF7511E9FB0C794FBB2D7202B6D871B06D7574C40FB83A8C3B14AF` |
| `docs/events/027_doctrine_research/overview.md` | 156 | `A6CD34D5F57FC61FE336A47AFD1118EAE5769701D1648258726B1C8AED246871` |

The working tree contained extensive concurrent changes before this audit. They were preserved. Only this handoff was created.

## Exact localisation and flow counts

| Check | Result |
| --- | ---: |
| Event 027 English keys | 333 |
| Unique Event 027 English keys | 333 |
| Duplicate keys inside the Event 027 file | 0 |
| Duplicate Event 027 keys elsewhere under `localisation/english/` | 0 |
| Event definitions under `chaosx.nr27.*` | 30 |
| Hidden routing or root events | 2, `.1` and `.6` |
| Visible human event pages with descriptions | 28 |
| Direct event localisation references | 261 |
| Missing direct event references | 0 |
| `defined_text` blocks in the Event 027 scripted-localisation file | 119 |
| Unique `defined_text` names | 119 |
| Unique `GetDoctrineResearch*` calls from the Event 027 English file | 118 |
| Missing called `defined_text` definitions | 0 |
| Unused Event 027 `defined_text` definitions | 1 |
| `GetDoctrineResearchOptionStatus*` references | 107 |
| Unique option-status references | 107 |
| `GetDoctrineResearchOptionStatus*` definitions | 107 |
| Unique option-status definitions | 107 |
| Missing option-status definitions | 0 |
| Unreferenced option-status definitions | 0 |
| Scripted-localisation output keys | 164 |
| Output keys resolved in Chaos Redux localisation | 49 |
| Output keys resolved in installed vanilla localisation | 115 |
| Unresolved output keys | 0 |
| External Event Log, evolution, cluster, debug, and achievement keys checked | 23 |
| Missing external consumer keys | 0 |
| Duplicate external consumer keys | 0 |

Option-status coverage by visible track page is exact:

| Page | Status calls |
| --- | ---: |
| `.60` Infantry | 9 |
| `.61` Combat Support | 9 |
| `.62` Armor | 8 |
| `.63` Operations | 10 |
| `.64` Submarines | 6 |
| `.65` Screens | 8 |
| `.66` Carriers | 6 |
| `.67` Capital Ships | 6 |
| `.68` Fighter Aircraft | 6 |
| `.69` Strike Aircraft | 6 |
| `.70` Medium Aircraft | 6 |
| `.71` Heavy Aircraft | 7 |
| `.72` Special Forces First | 8 |
| `.73` Special Forces Second | 8 |
| `.74` Chaos Warfare Infantry | 1 |
| `.75` Chaos Warfare Combat Support | 1 |
| `.76` Chaos Warfare Armor | 1 |
| `.77` Chaos Warfare Operations | 1 |

## Missing key list

None found in the assigned scope.

- All 261 direct `title`, `desc`, option `name`, and `custom_effect_tooltip` references from `events/027_doctrine_research.txt` resolve.
- `chaosx.event_name.27` exists in `localisation/english/chaosx_event_names_l_english.yml:29` and is selected by `common/scripted_localisation/chaosx_scripted_localisation_debug.txt:129-130`.
- The Event Details key, evolution type key, four evolution titles, four evolution bodies, National Breakthroughs name and detail keys, six achievement name and description keys, and four achievement tooltips all resolve uniquely.

## Duplicate key list

None found.

- Internal duplicates in `027_doctrine_research_l_english.yml`: 0.
- Duplicate definitions of those 333 keys across `localisation/english/`: 0.
- Duplicate Event 027 achievement IDs in `common/achievements/chaos_redux_achievements.txt`: 0. Each of the three IDs appears once at lines 4203, 4208, and 4213.

## Scripted localisation findings

### Passing coverage

- The 107 visible option-status calls are one-to-one with 107 definitions from `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt:216-1390`.
- Every option-status definition orders completion before Mastery 5 through Mastery 1, then selected-at-zero, then unselected fallback. This prevents a complete branch from displaying as another advance.
- The country-scoped name selectors cover domain, Grand Doctrine, track, subdoctrine, stage, action, result detail, concentration, summary Milestone, display completion, and display Milestone state.
- Current, next, and maximum mastery values use whole-number formatting on the event pages.
- The 164 scripted-localisation output keys all resolve. Forty-nine are owned by Chaos Redux and 115 resolve in installed vanilla doctrine localisation.

### Issues

1. `GetDoctrineResearchLastResultName` at `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt:184` is defined but never called by the Event 027 English file. This is dead scripted localisation, not a missing key.
2. `GetDoctrineResearchStageName` at lines 160-167 returns global Chaos tier labels. It produces awkward player text such as `Calm World curriculum` and `Totalen Chaos batch` when called by `chaosx.nr27.2.d` and `chaosx.nr27.10.d`.
3. The generic confirmation at `localisation/english/027_doctrine_research_l_english.yml:241` always prints a subdoctrine, Grand Doctrine, current level, maximum level, next level, completion state, and Milestone state. A Grand Doctrine adoption therefore presents irrelevant subdoctrine and mastery fields, while a mastery action receives the same adoption disclaimer. This should be action-specific scripted localisation.

## Current, next, maximum, completion, and Milestone wording

The required data is wired on all 18 track pages and on the generic confirmation page:

- current and maximum: `[?doctrine_research_display_current_level|0]/[?doctrine_research_display_maximum_level|0]`
- next: `[?doctrine_research_display_next_level|0]`
- completion: `[GetDoctrineResearchDisplayCompletionStatus]`
- native Milestone: `[GetDoctrineResearchDisplayMilestoneStatus]`

The selectors distinguish `complete` from `in progress`, and distinguish `active`, `expected on track completion`, and `not expected`. The final summary separately reports whether a native Milestone was reached.

The wording still has two quality defects:

- `Mastery 0 -> 1` through `Mastery 4 -> 5` at lines 327-331 and `Unselected -> Mastery 1` at line 333 read like developer-state labels. They are concise, but natural player-facing forms such as `Mastery 4 to Mastery 5` would be clearer.
- The generic confirmation repeats all state fields even when the selected action is Grand Doctrine adoption and no mastery change can occur.

## Human-flow page audit

The chain has 28 visible pages: `.2-.5`, `.60-.77`, and `.7-.12`. Every visible page has a title and description, and every scripted option reference resolves. Hidden `.1` and `.6` correctly need no visible description.

The remaining-choice requirement is not met:

- Only 2 of 28 visible descriptions contain the dynamic remaining-choice value: `chaosx.nr27.3.d` and `chaosx.nr27.9.d`.
- `chaosx.nr27.2.d` shows total batch size but not choices remaining.
- `chaosx.nr27.4.d`, `chaosx.nr27.5.d`, all 18 track descriptions `.60.d-.77.d`, and `chaosx.nr27.7.d` omit the remaining-choice count even though they are active selection or confirmation pages.
- The specification requires the opening to show both total and remaining choices and requires each choice page to keep the remaining count visible.

Additional human-flow defects:

1. `chaosx.nr27.8.d` at line 247 exposes `doctrine_research_last_transaction_receipt_id` as `Record N`. The specs explicitly prohibit transaction receipts and internal IDs in player text.
2. `chaosx.nr27.9.d` at line 250 repeats the internal receipt number.
3. `chaosx.nr27.10.a.tt` at line 256 exposes `the oldest queued batch`. Queue ordering is an implementation detail that the player does not need.
4. `chaosx.nr27.12.d` at line 262 explains duplicate-effect prevention. This is implementation-history style text rather than an in-world consequence.
5. `chaosx.nr27.11.a`, `.11.a.tt`, and `.12.a.tt` use implementation verbs such as `rebuild`, `close`, and `resume the oldest curriculum` instead of stating what the staff can do next.
6. The `.4` and `.5` descriptions identify the domain but do not name the active or selected Grand Doctrine. The generic track pages identify the track and branch but do not retain the full domain and Grand Doctrine context requested by the spec.

## Event Log, Event Details, and evolution audit

### Passing coverage

- Event 027 has the actorless mapping in `common/scripted_effects/chaosx_events_log_effects.txt:222-228`.
- Event Details selects `chaosx.events_log.window.event_details.doctrine_research` at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:5938`.
- Four Event Details evolution previews are registered at `common/scripted_effects/chaosx_events_log_effects.txt:3044-3059`.
- Four evolution titles are selected at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:2245-2248`.
- Four evolution bodies are selected at lines 8666-8669.
- The evolution bodies state the correct two, three, four, and five choice counts.
- No fake history date or index was added to the Event Details evolution preview path.

### Blockers and mismatches

1. History details and Event Details share the same static key through `GetEventsLogEventDetailDescription`. The Event 027 branch at line 5938 has no history payload or stage-specific variant. It cannot state the actual one, two, three, four, or five choice batch size for the selected firing, so the acceptance requirement that History details describe the current firing's batch size is not met.
2. Evolution II text at `027_doctrine_research_l_english.yml:314` says that `later choices wait` when a curriculum is open. This shifts the evolution preview from the three-choice stage into queue behavior and can be read as choices inside the same curriculum waiting on one another. The preview should lead with three separate choices and the strategic use of those choices.
3. The four evolution titles at lines 309-312 are named after global Chaos tiers rather than the widening institutional curriculum requested by the presentation spec.
4. The Event Details premise at line 307 is clear and non-mechanical, but it does not say that evolution stages increase a firing from one choice to as many as five. The presentation spec explicitly requests that fact.

## Achievement audit

The three achievement IDs are unique and their localisation is complete:

- `027_doctrine_research_first_lesson`
- `027_doctrine_research_single_school`
- `027_doctrine_research_joint_curriculum`

All three have `_NAME`, `_DESC`, eligibility tooltip, and condition tooltip coverage. The descriptions state the public requirements without naming arrays, flags, receipt IDs, or debug state. The wording does not duplicate the official all-subdoctrine achievement condition.

No localisation blocker was found on the achievement surface.

## Authoritative XLSX audit

The workbook was read directly in read-only mode. No CSV was treated as authority.

- `Events!28` is Event 27.
- `Clusters!10` is cluster 9.
- Event name is `Doctrine Research`.
- Type is `Minor Repeatable`.
- Chaos level is `1`.
- Cluster ID is `9`.
- Member severity is `Medium`.
- Event status is `Needs Testing`.
- National Breakthroughs status is `Partially Available`.

The workbook Event Details, Evolution I through IV, and National Breakthroughs detail strings are exact character-for-character matches with the corresponding localisation keys. This gives six exact wording matches.

The exact match also carries two localisation defects into the authoritative workbook:

- Evolution II contains the ambiguous queue sentence.
- National Breakthroughs says each member `validates its own owner system`. This is implementation jargon in player-facing cluster text.

## Cross-surface mismatch notes

1. `docs/events/027_doctrine_research/overview.md:82` calls `.60-.77` `hidden routers`, but `events/027_doctrine_research.txt` defines `.60-.77` as visible titled and described country-event pages. Only `.6` is the hidden router.
2. The overview correctly records one, two, three, four, and five choices and the current mastery display fields, but the live visible pages do not keep remaining choices visible on most of the flow.
3. The workbook and Event Details are synchronized exactly, but synchronized implementation jargon is still a prose defect.
4. The overview acknowledges that rendered pagination and overflow proof is still missing. The current audit reached the same blocker independently.

## Dynamic text opportunities

1. Add an action-specific confirmation description selector for Grand Doctrine adoption versus mastery advancement. This can suppress irrelevant mastery fields during adoption and suppress the adoption disclaimer during mastery.
2. Add the country-owned remaining-choice value to the opening, Grand Doctrine, track, subdoctrine, and confirmation pages.
3. Add a history payload or stored stage selector so the selected History row can report the batch size that actually fired.
4. Replace Chaos-tier curriculum labels with institutional stage names while retaining the tier separately where the interface needs it.
5. Replace hardcoded Grand Doctrine and track names in option labels with their existing vanilla or owner-system localisation tokens where consumer syntax permits it. The 107 subdoctrine options already use dynamic owning localisation keys.
6. Make Event Details mention the evolution range from one to five choices without listing internal queue state.

## File encoding concerns

No localisation encoding defect was found.

- `localisation/english/027_doctrine_research_l_english.yml` has UTF-8 BOM.
- `localisation/english/chaosx_event_names_l_english.yml` has UTF-8 BOM.
- The other English localisation file found through Event 027-adjacent search also has UTF-8 BOM.
- Event script, scripted localisation, and Markdown files do not require a localisation BOM.

The Event 027 English file has one `l_english:` header, 333 parseable one-line keys, no `:0` versions, and no leading indentation before keys.

## Prose-quality findings

### Vagueness

- `validates its own owner system` in the National Breakthroughs description does not tell the player what changes or why the cluster matters.
- `Calm World curriculum`, `Gathering Storm curriculum`, and similar stage phrases do not describe a military institution or curriculum.
- Evolution II's `later choices wait` does not clearly identify whether it means queued batches or choices inside the current batch.

### Bloat

- `chaosx.nr27.7.d` is 632 source characters and mixes action confirmation, branch state, Grand Doctrine state, adoption rules, and transaction rules in one paragraph.
- `chaosx.nr27.10.d` is 586 source characters and reads as a ledger dump. The visible summary values are useful, but the prose needs stronger grouping and fewer labels in one sentence chain.
- The 18 track descriptions range from 526 to 542 source characters. Their current, next, maximum, completion, and Milestone fields are required, but the repeated opening instruction can be tightened once the status presentation is retained.

### Obvious explanation

- `Rebuild the valid doctrine pool before the next choice` narrates an internal refresh rather than a player consequence.
- `Close this completed batch and start the oldest queued batch` explains queue mechanics that can happen automatically.
- The paused transaction text explains why duplicate prevention exists instead of stating the visible outcome.

### Repetition

- The generic confirmation repeats the same mastery and Milestone fields already shown on the selected track page even when those fields do not apply to adoption.
- Receipt IDs are repeated on both the result and continuation pages.
- Every track description repeats the same instruction and five status labels. This is partly required for clarity, but action-specific concise templates would reduce repetition without removing data.

### Overcomplication

- The result sentence at line 247 combines an internal record ID, country, action, domain, nested result detail, and choice consumption in one sentence chain.
- The summary line at 254 presents seven independent facts in one paragraph with little hierarchy.
- The cluster description uses `owner system`, a developer abstraction, instead of naming the institution or benefit owned by each member event.

### Style-rule repair needed

- Player-facing receipt IDs, queue ordering, duplicate-effect prevention, and owner-system validation violate the rule against exposing implementation details.
- No em dash, sentence semicolon, staged contrast formula, sourced-quote alteration, or obvious staccato chain was found in the Event 027 English file.
- No update-history language such as `reworked`, `newly added`, or `hardcoded` was found in the player-facing Event 027 text.

## Sourced-quotation preservation notes

No sourced or attributed quotation appears in the inspected Event 027 event pages, Event Details, evolution text, achievement text, documentation summary, or authoritative workbook row. No quotation required preservation, and none was altered.

## MCP inspection and overflow evidence

The required read-only Event MCP route was used.

- Event scan status: `EVENT_INSPECTED_PARTIAL`, successful.
- Scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e045b2079a689732afa6e6b0242fda775af75a69c1f1cd3724f1e610b931a11/17a0cf00f5b0cc213d068d1b1b2b69f7e15593b2ebb5c3c75ba7158a72f946b9/event-scan-312506d40da9.json`
- Overview render status: `EVENT_RENDERED_PARTIAL`, successful.
- Overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc26457e1d765cef32d913fd7e416d67f8f892c65e02dc005c3f752b53a567b3/fb600add3888cfc23a5721d96e058d5e1e44f449e13a20ca7b7b37021bd74a6f/event-overview-312506d40da9-manifest.json`
- Overview JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/555e299a227d30e8e064aae25c6d4bad3f4830cc9d842091da3e6b579b4afd37/a4381986a13c01b6a5dfafb9f61e2c5512ca3f8f155e3fd3bdb2a2a462007fd0/event-overview-312506d40da9.json`
- Overview SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/211290fcb742af89ede73f0bfcffad3202cd7d68ec7c3a150895bf53a87d4d4a/43d87c747904423521edb855cabe32bf774b88a2cba5dddea966959c75a1e42c/event-overview-312506d40da9.svg`
- Overview PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da2876b7e18f14bd7a5d85f67f3d5f01afc598a5045ee20c8d72cdff7c5e90bc/97d9a755c814663828112717c7bc3c6d8b528759184e717d856e193f48121466/event-overview-312506d40da9.png`

The more detailed `entries` render timed out after 180 seconds. The overview render verifies the source-linked chain but does not provide a one-to-one rendered standard event popup with final wrapped localisation. Therefore visible clipping and overflow on the 632-character confirmation, 586-character summary, 18 descriptions over 526 characters, and long dynamic option labels remain unverified. Source review is not treated as equivalent visual proof.

## Recommended fixes

1. In `localisation/english/027_doctrine_research_l_english.yml`, remove receipt IDs from `chaosx.nr27.8.d` and `chaosx.nr27.9.d`.
2. Replace `chaosx.nr27.7.d` with adoption-specific and mastery-specific dynamic descriptions. Add the corresponding selector in `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`.
3. Add remaining-choice text to `chaosx.nr27.2.d`, `.4.d`, `.5.d`, `.60.d-.77.d`, and `.7.d`.
4. Rewrite `.10.a.tt`, `.11.a`, `.11.a.tt`, `.12.d`, and `.12.a.tt` as player-facing outcomes without queue, rebuild, receipt, or duplicate-prevention language.
5. Replace `doctrine_research.stage.*` display values with institutional curriculum names, or separate curriculum name from Chaos tier display.
6. Add stage or batch-size payload handling for Event 027 History rows in the event-log recorder and `GetEventsLogEventDetailDescription`, with one static fallback only when no payload is available.
7. Rewrite the Evolution II body and National Breakthroughs description in both localisation and the authoritative workbook. Regenerate CSV exports only through the workbook exporter after an owner-approved workbook patch.
8. Correct `docs/events/027_doctrine_research/overview.md:82` so `.6` is the hidden router and `.60-.77` are visible track pages.
9. Remove `GetDoctrineResearchLastResultName` if no consumer needs it, or use it in an action-specific result sentence.
10. Rerun the Event MCP entries render or another supported standard event-popup visual route after text changes. Do not close the overflow blocker from source length alone.

## Meaningful validation run

- Parsed all Event 027 English keys and direct event references.
- Compared direct event references against the Event 027 English key set.
- Compared every `GetDoctrineResearch*` call against every `defined_text` name.
- Performed an exact one-to-one comparison of all 107 option-status calls and definitions.
- Resolved all 164 scripted-localisation output keys against current Chaos Redux and installed vanilla English localisation.
- Scanned Event 027 keys for repository-wide duplicates.
- Checked unique root achievement IDs and their visible localisation consumers.
- Compared six workbook strings character for character against Event Details, evolution, and cluster localisation.
- Verified BOM on every English localisation file found in the Event 027 scope.
- Used the read-only Event MCP scan and overview render.

## Skipped or blocked meaningful validation

- A one-to-one rendered standard event-popup view was unavailable from the successful overview artifact. The detailed entries render timed out after 180 seconds, so wrapping, clipping, and option overflow remain blocked.
- No Technology Tree Viewer is installed. This audit did not substitute source-only doctrine tree inspection for that absent viewer.
- No live game validation was requested or performed.

## Changed files

- `docs/plans/027_doctrine_research_plans/subagent_handoffs/localisation_auditor_final_2026-08-30.md`

No source localisation, scripted localisation, event, Event Log, Event Details, achievement, documentation overview, workbook, or CSV file was changed.

## Unresolved wording decisions

- Final institutional names for Baseline and Evolutions I through IV need owner approval or a bounded writing pass.
- The exact player-facing sentence for an ambiguous native mastery receipt should state the visible outcome without revealing duplicate-prevention machinery.
- The History payload wording should decide whether to name the stage, the exact choice count, or both. The exact choice count is required for clarity.

## Plan handoff path

This file is the requested handoff. No separate design-gap plan was created.
