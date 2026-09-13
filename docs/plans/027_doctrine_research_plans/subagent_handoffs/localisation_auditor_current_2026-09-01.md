# Event 027 localisation audit handoff, 2026-09-01

## Scope and authority

This was a read-only localisation audit of Event 027, Doctrine Research.

The audit covered `events/027_doctrine_research.txt`, `localisation/english/027_doctrine_research_l_english.yml`, Event 027 scripted localisation, shared Event Log and Event Details selectors, evolution and history text, achievement registration and localisation, National Breakthroughs localisation, and the authoritative Event 027 and National Breakthroughs rows in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

The accepted wording requirements were taken from the visible-text portions of `docs/specs/027_doctrine_research_specs/`, including the choice-flow, presentation, achievement, catalog, and acceptance documents.

## Changed files

- Gameplay files changed: none.
- Localisation files changed: none.
- Scripted-localisation files changed: none.
- Documentation and specification files changed: none.
- Workbook files changed: none.
- Audit artifact added: `docs/plans/027_doctrine_research_plans/subagent_handoffs/localisation_auditor_current_2026-09-01.md`.

The inspected source files were already modified or untracked in the shared dirty worktree before this handoff was written. This auditor did not alter or revert those changes.

## Source-localisation health

Source-localisation health is mechanically strong but not ready for full acceptance.

- The current Event 027 file defines 31 unique event IDs: `chaosx.nr27.1` through `chaosx.nr27.13` and `chaosx.nr27.60` through `chaosx.nr27.77`.
- All 265 unique direct Event 027 title, description, option-name, and custom-tooltip references found by the bounded source scan resolve to localisation keys.
- `027_doctrine_research_l_english.yml` contains 338 unique keys and no duplicate key definitions.
- No Event 027-owned key was found duplicated in another English localisation file.
- The Event 027 scripted-localisation file defines 119 `GetDoctrineResearch...` helpers, with no duplicate helper names.
- All 119 Event 027 scripted-localisation helpers are consumed by Event 027 localisation.
- All 162 scripted-localisation output keys resolve against current mod or installed vanilla English localisation.
- All 95 `$KEY$` substitutions in Event 027 localisation resolve.
- The Event 027 localisation file, `chaosx_event_names_l_english.yml`, and `chaosx_gui_l_english.yml` begin with the required UTF-8 BOM bytes `EF BB BF`.
- No em dash or sentence semicolon was found in the Event 027 localisation file.
- The three achievement IDs are registered and have matching `NAME`, `DESC`, eligibility-tooltip, and happened-tooltip keys.
- Navigation and action tooltips are wired for the track pages, confirmation, no-option recovery, and completion flow.
- `chaosx.nr27.4.option_tt` and `chaosx.nr27.5.option_tt` are defined but have no source consumer. They are dead localisation, not missing coverage. `chaosx.nr27.6.option_tt`, next, previous, and navigation tooltip keys are actively consumed.

This mechanical health does not prove that the visible text is concise, visually safe, or semantically accepted.

## Missing key list

None found in the bounded Event 027, Event Details, evolution, history, achievement, and National Breakthroughs surfaces.

## Duplicate key list

None found for Event 027-owned English localisation or the inspected shared Event 027 selectors.

## Scripted-localisation issue list

No missing helper, duplicate helper name, unresolved output key, or unresolved `$KEY$` substitution was found.

The scripted-localisation system provides strong dynamic coverage for country, stage, domain, Grand Doctrine, track, subdoctrine, current mastery, next mastery, completion status, Milestone status, remaining choices, result detail, and summary values.

The current issues are wording and presentation issues in the localisation that consumes these helpers, not missing helper resolution.

## Dynamic text opportunities

No required existing gameplay value was found hardcoded where an available Event 027 helper should plainly replace it.

The principal opportunity is structural rather than a new token: the repeated track-page descriptions should retain their dynamic values while presenting them in a shorter hierarchy so the current branch, current and next mastery, completion status, and Grand Doctrine Milestone status remain readable.

## Cross-surface agreement

The following surfaces agree exactly or materially:

- `chaosx.event_name.27`, the event title, and workbook Event Name use `Doctrine Research`.
- `chaosx.events_log.window.event_details.doctrine_research` exactly matches the workbook Event 27 Details cell.
- The four evolution-detail bodies exactly match the workbook Evolution I through Evolution IV cells.
- The National Breakthroughs Event Details description exactly matches the workbook Clusters row description.
- Event 027 is assigned to National Breakthroughs with Medium severity in script and workbook membership data.
- The achievement names, descriptions, and tooltip requirements agree with their registered country-flag conditions at the player-facing level.

The following mismatches or terminology inconsistencies remain:

1. The baseline Event Details and workbook Details cell say a choice advances a subdoctrine by one `mastery level`, while the event opening, Evolution I, achievement wording, and accepted design describe the reward as one `mastery step`. The baseline Event Details and matching workbook cell should use `mastery step` so the action is consistently distinguished from the resulting mastery level and from a Grand Doctrine Milestone.
2. Every track-page description from `chaosx.nr27.60.d` through `chaosx.nr27.77.d`, plus `doctrine_research.confirm.mastery`, labels the separate native status as bare `Milestone:`. The completion summary correctly says `Grand Doctrine Milestone reached:`. The shorter pages should also say `Grand Doctrine Milestone:` to prevent players from mistaking it for the subdoctrine mastery level.
3. The workbook Cluster Memberships note for Event 27 says `opens one global country fanout`. `Fanout` is implementation terminology and should be replaced with player-facing wording such as `grants each eligible country one doctrine curriculum`.
4. `chaosx.nr27.12.a` and `chaosx.nr27.12.a.tt` say the review or curriculum ends, but the event source returns to `chaosx.nr27.2` when the active batch still exists. The option therefore contradicts the actual navigation path in that state.

## Navigation, confirmation, and no-option findings

- Domain and track navigation has explicit back, next, previous, and navigation tooltip text.
- Confirmation has distinct adoption and mastery summaries, a back option, and an invalid-selection rebuild option.
- The no-option event states that it checks once more and then closes without a substitute reward, which agrees with the source branch.
- The confirmation tooltip `chaosx.nr27.7.a.tt` says to check the selected domain, track, doctrine, and prerequisites `before applying one action`. This is procedural and abstract, and it adds little beyond the visible confirmation summary. A clearer tooltip should state the consequence that matters to the player, especially when the choice is spent.
- The ambiguous-result event `.12` is not navigationally honest when a batch remains because its `End this curriculum` tooltip can return the player to the same curriculum opening.
- The adoption-only event `.13` correctly says no choice was spent and returns to the current domain's valid tracks, but its title and body expose raw implementation terminology.

## Prose-quality issues

### Vagueness

- `chaosx.nr27.12.d` says the curriculum is suspended `pending a fresh review`. It does not explain what the player is returning to or what changed, and it frames a transaction-verification failure as a vague process.
- `chaosx.nr27.7.a.tt` uses `applying one action`, which is less concrete than establishing the selected Grand Doctrine or advancing the selected subdoctrine.

### Bloat

- `chaosx.nr27.60.d` through `chaosx.nr27.77.d` each combine remaining choices, domain, Grand Doctrine, track instruction, mastery preservation, current branch, current level, maximum level, next level, completion status, and Milestone status in one dense paragraph.
- `doctrine_research.confirm.mastery` repeats nearly the same full status bundle. These values are useful, but the present sentence sequence is too long for confident event-popup acceptance.
- `chaosx.nr27.10.d` compresses batch size, adoption count, mastery-step count, domain count, track count, concentration, and Grand Doctrine Milestone status into one paragraph. It is mechanically informative but visually and cognitively dense.

### Obvious explanation

- `chaosx.nr27.7.a.tt` largely narrates the confirmation process instead of adding a requirement or consequence not already visible in the confirmation description.
- Repeating `Confirming advances it by one mastery step and preserves any mastery already earned` on all 18 track pages adds useful protection information once, but becomes boilerplate across every page and contributes to overflow risk.

### Repetition

- The 18 track descriptions are structurally identical and repeat the same instructional and status prose.
- Achievement descriptions and happened tooltips necessarily overlap, but the current pairs remain acceptably distinct: the descriptions summarize the goal and the tooltips supply the exact curriculum threshold.

### Overcomplication

- The repeated track descriptions present nine pieces of state in a single prose run instead of a short instruction followed by clearly labelled values.
- The `.12` and `.13` recovery text explains transaction-resolution mechanics rather than the concrete doctrine result and next player choice.

### Writing-style violations and raw implementation terminology

- `chaosx.nr27.13.t`, `Native Doctrine Progress Resolved`, exposes an engine-facing distinction.
- `chaosx.nr27.13.d` uses `banked native mastery`, another implementation-facing phrase.
- `chaosx.nr27.12.d` uses validation language, `cannot verify` and `exactly one mastery level`, rather than directly stating that the branch did not record a valid advance.
- The workbook membership note uses `global country fanout`.
- No em-dash, semicolon-in-sentence, prompt-fragment, update-history, or tuning-note violation was found elsewhere in the Event 027 localisation file.

## Sourced-quotation preservation notes

No sourced or attributed quotation was found on the inspected Event 027, achievement, Event Details, evolution, history, log, National Breakthroughs, or workbook surfaces.

No quotation was altered.

## Recommended fixes by file and key

No fix was applied by this read-only auditor.

1. In `localisation/english/027_doctrine_research_l_english.yml`, rewrite `chaosx.nr27.13.t` and `chaosx.nr27.13.d` to describe prior doctrine progress without `native` or `banked native mastery`, while preserving that the branch completed during assignment and no curriculum choice was spent.
2. In the same file, rewrite `chaosx.nr27.12.d`, `chaosx.nr27.12.a`, and `chaosx.nr27.12.a.tt` so the text describes the unresolved advance concretely and agrees with both possible destinations. If the intended behavior is truly to end the curriculum, the owning event agent must change the script instead; localisation alone cannot repair that behavior mismatch.
3. In the same file, change the visible label in `chaosx.nr27.60.d` through `chaosx.nr27.77.d` and `doctrine_research.confirm.mastery` from `Milestone:` to `Grand Doctrine Milestone:`.
4. In the same file and the authoritative workbook Events row, change the baseline Event Details phrase from `by one mastery level` to `by one mastery step`.
5. In the same file, shorten and restructure `chaosx.nr27.60.d` through `chaosx.nr27.77.d` and `doctrine_research.confirm.mastery` without removing dynamic tokens, requirements, current and next mastery, completion status, or Grand Doctrine Milestone status.
6. In the same file, simplify `chaosx.nr27.7.a.tt` so it states the material consequence of confirmation instead of instructing the player to check implementation prerequisites.
7. In `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, replace the Event 27 Cluster Memberships note `opens one global country fanout` with direct player-facing wording.
8. In `localisation/english/027_doctrine_research_l_english.yml`, either remove the dead `chaosx.nr27.4.option_tt` and `chaosx.nr27.5.option_tt` keys or wire them if the adoption and track-selection pages are intended to have option tooltips.

## Read-only MCP evidence

The Event 027 downstream trace returned `EVENT_INSPECTED_PARTIAL` with status `ok`.

Event trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f0de6a7b6a35e6af72f43e2d05cb620b05648c7d03f705635e26df00932776be/7aaa8529c840ac02079222a874142a5aaa5f7f275f421caea10c2e4905ea079a/event-trace-2725045f62d1.json`.

The Event 027 option render returned `EVENT_RENDERED_PARTIAL` and provides structural option-flow evidence, not a one-to-one in-game event-popup text view.

Event options manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82908a6ad24bccd6045ce5b1d4f4a4d889e04c43ef68b42ceeda2df3f05ab00f/10b88c6c3e2880d4817c0b3c43d78c57d47815065efe91b4c073c5a828c6323d/event-options-2725045f62d1-manifest.json`.

Event options PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c94ba67b7940226e96345e394edb1ec733aa1087fdccf0b49c206542caa2270e/e187ce228ab8e374deae93a7ae0003c934f9b50d04288c95a6c3bf906394dd5e/event-options-2725045f62d1.png`.

The shared `events_log_popup_window` inspection for scenario `event_027_details-generated-1` returned `GUI_INSPECTED`.

GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab98f41fbf6a3cf9dd76d70ecf0887412ad9cb6cd97273e63f814d13c567c5fd/93f5b526f4d43fa0229d17ba7289737aea51573c50b4ea6e02d9c5062c8d783e/gui-inspect.8e2e9e6530f5448c.json`.

The fresh shared GUI render at 1920 by 1080 and 1366 by 768, UI scale 1, returned `GUI_RENDERED`, but `validation.passed` was `false` and the response was truncated at the MCP wire budget.

GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53106e9beb1b45d4acfed1b10157ac0fd3479eb333569cc2b62fbe7b61ae8b02/3e752e4b75026a2278fc22a5bb2dcbe17a2e15c2a4cf6fe5375f696fe69a1a27/events_log_popup_window-full.svg`.

The generated scenario does not provide accepted Event 027-specific Event Details and evolution text-layout evidence, so clipping, wrapping, and overflow for those strings remain unverified.

The technology folder inspection returned `TECH_INSPECTED` with status `ok` and no direct blocker.

Technology folder artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e6b1b19c52c348af05882438e769ad27a751a39c6caa3e2659d930acdcc1afa/a1b0a4bc58d7c26dcbf8c45459d4e085428735cdb74e21577100664bcf306d60/technology-folders-d21024047005.json`.

The doctrine render returned `TECH_RENDERED`, but its own result reports `sourceAccurate: false`. It is useful structural evidence and is not accepted as a one-to-one in-game Technology Tree Viewer visual check.

Doctrine render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ed9bd9d2d9d3afdf87c8bbf0c5457190dbcefb62cc7b1a72a06ef02f06fa97b/3d4f98ce7ec5c847e013bc056743940b01f0e22fcce9b946a677a99194c26ac4/technology-doctrine-d21024047005-manifest.json`.

Doctrine PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb653113a422f6c9e58d4f94b0aaedf23755f0ad7f9de7063626d13e5d9932d8/ff1751a0c9e9ee7521fdbe7b0f4ca1c413aa18504f80ef541bb2589fdf465aff/technology-doctrine-d21024047005.png`.

## Meaningful validation performed

- Parsed current event IDs and every direct Event 027 localisation reference.
- Parsed Event 027 English keys and checked duplicate ownership across English localisation.
- Parsed Event 027 scripted-localisation helper names, consumers, output keys, and nested `$KEY$` references against mod and vanilla English localisation.
- Checked BOM bytes for the Event 027 file and inspected shared Event Name and GUI localisation files.
- Compared Event Details, all four evolution descriptions, Event history wording, achievement wording, National Breakthroughs wording, and workbook cells.
- Traced confirmation, retry, no-option, ambiguous-result, and adoption-only navigation against their visible labels and tooltips.
- Used read-only Event, GUI, and doctrine MCP routes and recorded their artifact URIs and explicit fidelity limits.

## Skipped or unavailable meaningful validation

- No live Hearts of Iron IV run or player interaction was performed or claimed.
- The available Event MCP render is a structural event graph, not the production country-event popup, so it cannot validate Event 027 title, description, option, or tooltip overflow.
- The shared Event Details GUI scenario did not return accepted Event 027-specific text-layout proof and its render validation failed.
- The doctrine image is explicitly not source-accurate, so doctrine-tree localisation placement and overflow remain unaccepted.
- Achievement notification and achievement-panel visual layout were not available through a dedicated MCP consumer route in this audit.

## Unresolved acceptance blockers

1. Raw implementation terminology remains visible in `.13` and in the workbook Cluster Memberships note.
2. Mastery-step wording is inconsistent with the baseline Event Details `mastery level` phrase, and bare `Milestone:` labels do not consistently distinguish the Grand Doctrine Milestone from subdoctrine mastery.
3. The `.12` option and tooltip contradict the source path when an active curriculum remains.
4. Track-page, confirmation, and summary text remain too dense for acceptance without a production event-popup overflow check.
5. Event 027-specific Event Details and evolution strings lack a passing production GUI render at the required resolutions.
6. Doctrine-tree localisation lacks source-accurate visual evidence.
7. Achievement consumer layout lacks dedicated visual evidence.

## Acceptance statement

Event 027 has healthy source localisation coverage, encoding, key uniqueness, and scripted-localisation resolution in the bounded audit.

Event 027 is not accepted as complete. Source-localisation health is not equivalent to full localisation acceptance because semantic wording defects, a navigation-text contradiction, and unresolved production-layout evidence remain.
