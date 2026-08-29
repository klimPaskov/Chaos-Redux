# Event 35 Great Depression 2.0 live repository cross-check

## Repository inspected

- Repository: `klimPaskov/Chaos-Redux`
- Default branch: `master`
- Inspection date: 2026-08-27
- Public repository state used for this planning pass

The repository cross-check prevents identifier drift and maps the migration from the current stub. It does not replace implementation-time source inspection, offline wiki reading, vanilla documentation, HOI4 MCP evidence, or user-run in-game validation.

## Current Event 35 event file

Path:

```text
events/035_great_depression.txt
```

Current structure:

- Namespace `chaosx.nr35`.
- Hidden entry event `chaosx.nr35.1`.
- Random country limited to a major or human-controlled country.
- Visible event `chaosx.nr35.2` after one day.
- Fixed timed idea `great_depression` for `365` days.
- Existing report image `GFX_report_event_great_depression`.
- News event `chaosx.news.40`.
- One visible option.

Migration implication:

- Preserve namespace and canonical entry ID.
- Preserve `chaosx.nr35.2` as the opening report unless a full migration plan proves a conflict.
- Replace the random-country plus fixed timed idea with exact target validation and the reusable start-or-deepen API.
- Remove the fixed 365-day lifecycle.
- Keep news slot `chaosx.news.40` stable unless current news inspection finds a collision.
- Treat the existing report sprite as a stable migration anchor pending asset review.

Repository source:

- https://github.com/klimPaskov/Chaos-Redux/blob/master/events/035_great_depression.txt

## Current Event 35 localisation

Path:

```text
localisation/english/035_great_depression_l_english.yml
```

Current keys:

- `chaosx.nr35.1.t`
- `chaosx.nr35.2.t`
- `chaosx.nr35.2.d`
- `chaosx.nr35.2.a`
- `chaosx.news.40.t`
- `chaosx.news.40.d`
- `chaosx.news.40.a`

Migration implication:

- Preserve existing keys where the same surface remains.
- Rewrite wording to match the dynamic event and source-specific openings.
- Add separate direction and keys for Event 34 collapse, contagion, Social Collapse, global escalation, state incidents, decisions, missions, Event Details, and achievements.
- Keep UTF-8 with BOM.

Repository source:

- https://github.com/klimPaskov/Chaos-Redux/blob/master/localisation/english/035_great_depression_l_english.yml

## Current Great Depression idea definition

Repository search for a dedicated Event 35 idea file and for `great_depression = {` did not surface a clear Event 35-owned definition. Search results found the event call and unrelated uses of the `great_depression` picture token.

Implementation action:

- Locate the actual current `great_depression` idea definition before editing.
- If it exists in a legacy shared file, migrate it into an Event 35-owned ideas or dynamic-modifier file when safe.
- If it is missing, define the complete Event 35 national condition and do not preserve an unresolved token.
- Do not infer a compile error from search alone. Repository indexing may omit or tokenize the definition differently.

The new design should use:

- One short opening-shock idea.
- One active dynamic depression condition or compact staged family.
- One post-recovery safeguard.
- Bounded recovery legacies and scars.

It should not use one fixed idea for the whole crisis.

## Current Event 34 relationship

Path:

```text
events/034_industrial_boom.txt
```

Current structure:

- Namespace `chaosx.nr34`.
- Hidden entry `chaosx.nr34.1`.
- Major or human target.
- Fixed `180` day `industrial_boom` idea.
- Visible event `chaosx.nr34.2`.
- News event `chaosx.news.39`.

The accepted Event 34 planning package replaces this stub with Overheating, Industrial Regions, landing, collapse, and a frozen Event 35 handoff.

Migration implication:

- Implement Event 34 and Event 35 shared contracts together or behind a versioned API.
- Event 35 owns start and deepen logic.
- Event 34 owns the frozen boom snapshot.
- Preserve Event 34 and Event 35 history without counting the handoff as another pacing event.

Repository sources:

- https://github.com/klimPaskov/Chaos-Redux/blob/master/events/034_industrial_boom.txt
- https://github.com/klimPaskov/Chaos-Redux/blob/master/localisation/english/034_industrial_boom_l_english.yml

## Event-system classification

The supplied source and previous live repository inspection register Event 35 as a repeatable event. Keep:

- Event type Minor Repeatable.
- Chaos level `1`.
- Repeatable weight recovery and diminishing cap behavior from the shared event system.

The direct Event 34 consequence call must not call the generic repeatable pacing handler a second time.

Likely core touchpoints:

```text
common/scripted_effects/chaosx_logic_effects.txt
common/scripted_effects/chaosx_settings_effects.txt
common/scripted_effects/chaosx_events_log_effects.txt
common/scripted_localisation/chaosx_scripted_localisation_events_log.txt
localisation/english/chaosx_event_names_l_english.yml
localisation/english/chaosx_gui_l_english.yml
```

Implementation must inspect exact current functions before patching.

## Catalog and cluster mismatch

Supplied Event CSV snapshot:

- Event 35 is Minor Repeatable.
- Chaos level `1`.
- Status To Be Reworked.
- Cluster field is blank.

Supplied cluster CSV snapshot:

- Negative Economy exists as an unavailable placeholder.
- Cluster ID blank.
- Details and members blank.
- Type Minor Fire-Once.
- Chaos level `2`.

New accepted brief:

- Event 35 belongs to Negative Economy.
- Member danger Low.

Implementation action:

- Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx` after implementation facts are final.
- Allocate or confirm the Negative Economy cluster ID in the authoritative workbook and runtime registry.
- Define cluster type, members, roles, participation chances, order, unlock tier, cooldown, and text.
- Add Event 35 as Low member.
- Run `python .tools/export_event_catalog_csv.py`.
- Never edit the three CSV exports directly.

This specification does not guess the missing cluster ID or remaining roster.

## Current art and news anchors

Known current anchors:

- Report sprite `GFX_report_event_great_depression`.
- News event `chaosx.news.40`.

Implementation action:

- Inspect `interface/chaosx_pictures.gfx` and the actual texture path.
- Inspect `events/_chaosx_news.txt` for news slot `40`.
- Preserve identifiers when no collision exists.
- Replace art only through the asset workflow and keep sprite naming stable where possible.

## Likely new Event 35 files

The final file map depends on current repository patterns. A clean event-owned structure is likely to include:

```text
events/035_great_depression.txt
common/script_constants/035_great_depression_constants.txt
common/scripted_effects/035_great_depression_effects.txt
common/scripted_triggers/035_great_depression_triggers.txt
common/dynamic_modifiers/035_great_depression_dynamic_modifiers.txt
common/ideas/035_great_depression_ideas.txt
common/decisions/035_great_depression_decisions.txt
common/decisions/categories/035_great_depression_categories.txt
common/on_actions/035_great_depression_on_actions.txt
common/scripted_localisation/035_great_depression_scripted_localisation.txt
localisation/english/035_great_depression_l_english.yml
interface/035_great_depression.gfx
```

Use shared files only for genuinely reusable APIs or event-log integration. Do not put all Event 35 logic into `chaosx_logic_effects.txt`.

## Shared API documentation

If Event 35 adds a reusable start-or-deepen effect, document its:

- Purpose.
- Scope.
- Required inputs.
- Outputs.
- Defaults.
- Rejection reasons.
- Side effects.
- Usage examples.

If it belongs in the public dynamic-effects registry, update:

```text
common/scripted_effects/chaosx_dynamic_effects.md
```

Private Event 35 helpers remain in Event 35 documentation.

## Runtime schedule

The event needs an event-owned sparse schedule for active countries and registered states. Do not add an unrestricted `on_daily`, `on_weekly`, or `on_monthly` world iteration.

Likely pattern:

- One bounded start effect registers active country.
- One delayed event or event-owned on-action evaluates that country.
- Center arrays limit state work.
- Contagion arrays limit foreign work.
- Evolution III performs one bounded initialization and then sparse updates.

The exact implementation requires source and vanilla inspection.

## Event Details and evolution migration

Event 35 currently has no full evolution pipeline in the stub.

Implementation needs:

- Event name mapping.
- Actor mapping.
- Event Details premise.
- Three evolution preview rows.
- Logged evolution rows with actor, date, tier, and stage.
- Source-specific history details.
- Negative Economy cluster membership.
- Evolution enable and disable behavior.

The three evolutions are:

1. Financial Contagion at Rising Chaos.
2. Social Collapse at Chaos Tier.
3. The Second Great Depression at Totalen Chaos.

## Super-event migration

The current Event 35 stub has no dedicated super-event.

The accepted design adds one super-event only for the first concrete worldwide pressure application under Evolution III.

Implementation needs:

- Intentional free slot.
- One-time visibility receipt.
- Image.
- Title, description, reaction, and sourced quote.
- Unique licensed musical cue.
- Base sound and volume wrappers.
- Settings-aware playback.
- Scripted localisation and GFX.
- Permanent research documentation.
- Audio catalog row.


## Migration sequence

Recommended implementation order:

1. Inspect Event 35, Event 34, current idea token, news slot, art sprite, event registry, and Event Details paths.
2. Define Event 35 constants, source enums, episode state, Severity, phase, and sparse registry.
3. Implement reusable start-or-deepen API and independent entry.
4. Replace fixed 365-day idea with opening shock and dynamic condition.
5. Implement Depression Centers and transfer logic.
6. Implement doctrines, decisions, missions, AI, and cleanup.
7. Implement Event 34 snapshot consumer and transaction tests.
8. Implement Financial Contagion.
9. Implement Social Collapse.
10. Implement The Second Great Depression and super-event.
11. Complete Event Details, history, cluster, docs, assets, achievements, and workbook.
12. Run probability, decision, localisation, completion, and improvement-loop audits.

## Repository limitations of this planning pass

- The live public repository was inspected through the GitHub connector.
- The local Windows mod checkout, offline Paradox wiki, installed vanilla files, vanilla documentation, and HOI4 MCP were not mounted in this environment.
- No repository files were edited.
- No claim is made that the current game build loads or that the current `great_depression` idea token is unresolved at runtime.
- Final implementation must repeat the mandatory local inspections and engine-supported evidence workflow.
