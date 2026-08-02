# Player-Facing Text Style Cleanup Handoff

Date: 2026-08-02

Scope: documentation surfaces under `docs/events/**`, `docs/specs/**`, and `docs/super_events/**` that contain player-facing drafts or wording intended to mirror localisation.

This handoff does not claim gameplay, localisation, workbook, asset, or live consumer completion.

## Source-of-truth map

| Surface | Current documentation authority | Reading and disposition |
| --- | --- | --- |
| Event 003 Holy Realm sample event and localisation samples | `docs/specs/003_holy_realm_specs/003_holy_realm_spec.md` | The explicit sample-copy blocks were normalized in place. They remain tone samples, not final localisation. |
| Event 004 Random War report and catalog wording | `docs/specs/004_random_war_specs/004_random_war_spec.md` | The report direction and catalog detail and evolution drafts were normalized in place. Runtime localisation was not opened. |
| Event 007 Fury first-conquest and scenario text | `docs/specs/007_fury_specs/specs/007_fury_spec_part_1_core.md`, `docs/specs/007_fury_specs/specs/007_fury_triggerable_scenario_spec.md`, and `docs/specs/007_fury_specs/specs/007_fury_achievements_spec.md` | Explicit player-facing directions and achievement descriptions were normalized in place. These remain design directions. |
| Event 008 Tensions Rising | `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_event_log_and_localisation.md`, `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_evolutions_and_hidden_effects.md`, and `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_spec.md` | Popup, follow-up, event-detail, evolution-detail, catalog-facing, and pulse-summary wording now shares one premise-led vocabulary. Live localisation and workbook parity remain unverified. |
| Event 009 White Peace | `docs/specs/009_white_peace_specs/specs/009_white_peace_event_text_log_cluster.md` and `docs/specs/009_white_peace_specs/specs/009_white_peace_spec.md` | Popup, event-detail, catalog-detail, and dynamic availability wording now avoids effect lists and matches the restrained diplomatic premise. Live localisation and workbook parity remain unverified. |
| Event 010 Death | `docs/specs/010_death_specs/specs/010_death_spec_part_1_core_flow.md`, `docs/specs/010_death_specs/specs/010_death_assets_super_events_achievements.md`, and `docs/specs/010_death_specs/prompts/010_death_super_event_prompt.md` | The repeated Event Details and super-event description directions now use the same premise-led wording. The prompt is synchronized with the specs. Live localisation remains unverified. |
| Event 020 Black Plague catalog draft | `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md` | The working contract now uses visible outbreak, containment, rat-state, and world-end language instead of hidden counters and implementation identifiers in player-facing fields. The file still records `Needs Testing`, and the workbook remains owned by the spreadsheet worker. |
| Super-event 011 Secret Alliance | `docs/super_events/011_secret_alliance/research.md` | The final fractured-route description was normalized in the final text package. The file states that live localisation is the implementation authority. |
| Super-event 015 Utopia Manifesto | `docs/super_events/015_utopia_manifesto/text_research.md` | The final closed-island description was normalized. Other original descriptions and sourced quotations were left intact. |
| Camp repression super-event research | `docs/super_events/system_camp_repression_rework_super_event_research.md` | The five archived original descriptions were normalized. The file explicitly marks this YAML as superseded research and names live localisation files as authoritative. Sourced quotation punctuation was preserved. |

## Files changed

- `docs/specs/003_holy_realm_specs/003_holy_realm_spec.md`
- `docs/specs/004_random_war_specs/004_random_war_spec.md`
- `docs/specs/007_fury_specs/specs/007_fury_achievements_spec.md`
- `docs/specs/007_fury_specs/specs/007_fury_spec_part_1_core.md`
- `docs/specs/007_fury_specs/specs/007_fury_triggerable_scenario_spec.md`
- `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_event_log_and_localisation.md`
- `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_evolutions_and_hidden_effects.md`
- `docs/specs/008_tensions_rising_specs/specs/008_tensions_rising_spec.md`
- `docs/specs/009_white_peace_specs/specs/009_white_peace_event_text_log_cluster.md`
- `docs/specs/009_white_peace_specs/specs/009_white_peace_spec.md`
- `docs/specs/010_death_specs/prompts/010_death_super_event_prompt.md`
- `docs/specs/010_death_specs/specs/010_death_assets_super_events_achievements.md`
- `docs/specs/010_death_specs/specs/010_death_spec_part_1_core_flow.md`
- `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md`
- `docs/super_events/011_secret_alliance/research.md`
- `docs/super_events/015_utopia_manifesto/text_research.md`
- `docs/super_events/system_camp_repression_rework_super_event_research.md`

## Plan and handoff disposition

| Document class | Disposition | Evidence |
| --- | --- | --- |
| Accepted source specs | Left in place and patched only at explicit display-copy blocks | No source spec was replaced or redesigned. |
| Working plans and addenda | Unchanged | No implementation plan was promoted, rejected, queued, or superseded by this text-only pass. |
| Existing subagent handoffs | Unchanged | No prior handoff was deleted or rewritten. |
| Archived camp research | Retained as superseded evidence | The archive warning remains in `docs/super_events/system_camp_repression_rework_super_event_research.md`. |
| New cleanup handoff | Created | This file is the resume anchor for the parent agent. |

No separate resume packet was needed because this handoff contains the source map, changed-file list, open decisions, and validation evidence.

## Contradictions and unresolved decisions

| File or surface | Evidence | Parent decision or follow-up |
| --- | --- | --- |
| `docs/specs/008_tensions_rising_specs/` | The event-log file, evolution map, and main spec now share the same display vocabulary, but live English localisation and the workbook were not inspected in this documentation-only pass. | Run the localisation auditor and then mirror the accepted wording into the workbook. |
| `docs/specs/009_white_peace_specs/` | The event-detail and catalog-detail drafts now match in premise and scope, but live localisation and the workbook were not inspected. | Confirm the implementation wording before spreadsheet alignment. |
| `docs/specs/010_death_specs/` | Core flow, catalog direction, and super-event prompt now agree. Runtime localisation was not opened. | Reconcile the live Event Details and super-event keys before treating the docs as final. |
| `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md` | The contract still reports `Needs Testing` and includes planning status fields. | Keep the workbook and status under the spreadsheet worker and parent review boundary. |
| `docs/super_events/system_camp_repression_rework_super_event_research.md` | Sourced quote and attribution lines retain em-dash formatting from the cited source or approved display excerpt. | Preserve exact sourced punctuation unless the parent explicitly approves a source-faithful alternate display format. |
| Camp archive versus live text | The file says its YAML is not an exact copy of live localisation and names the live YAML files as authoritative. | Do not use this archive as runtime copy without comparing the live files. |
| Existing dirty worktree | Pre-existing edits were present in Event 006 docs, Event 269 docs, Event 016 handoff docs, and air-cleanliness review docs. | Those edits were not touched by this pass. |

## Duplicate and superseded document list

- Event 008 has duplicate display-copy directions in the event-log file, the evolution map, and the main spec. The overlapping blocks were synchronized where they were explicit player-facing drafts.
- Event 009 has duplicate popup and Event Details directions in two spec files. The overlapping blocks were synchronized.
- Event 010 repeats super-event descriptions in the core flow, asset and achievement spec, and super-event prompt. The repeated directions were synchronized.
- The camp-repression YAML snippets are explicitly superseded research. Live localisation remains the authority.
- Event 003 contains separate early tone samples, route sample text, and later localisation samples. They are distinct surfaces, not competing source specs, and the explicit copy blocks were normalized without merging the sections.

## Stale prompt and instruction audit

- `docs/specs/010_death_specs/prompts/010_death_super_event_prompt.md` was stale relative to the revised Death descriptions and is now synchronized.
- The Event 008 and Event 009 prompt folders contain implementation instructions and audit boundaries, not conflicting final display copy. They were left unchanged.
- Event 020 prompts retain planning directions and do not contain a paste-ready final description. They were left unchanged.
- The camp-repression archive contains earlier wording, but its superseded notice is explicit and remains in place.

## Validation run

- Read the required repository guidance, the `chaos-redux-subagents` skill, the `chaos-redux-events` skill, the named source specs, and the relevant super-event research files before editing.
- Ran targeted `rg` searches for display-copy markers, duplicate event-detail phrases, stale descriptions, and super-event YAML blocks.
- Ran `git diff --check` on the tracked changed documentation paths and checked this new handoff text separately.
- Scanned added diff lines for em dashes and semicolons, then checked this handoff separately. No added line contains either punctuation mark.
- Rechecked the canonical Event 008, Event 009, and Event 010 wording with `rg` after patching.
- Inspected `docs/events/**` for concrete display-copy blocks. The reviewed matches were implementation ledgers or references to live localisation, so no `docs/events/**` file required a text patch in this pass.

## Skipped meaningful validation

- Live localisation parity was not checked because this subagent may not edit or own gameplay localisation and the parent did not provide a final runtime text manifest.
- The event catalog workbook was not opened or edited because it belongs to `chaosx_spreadsheet_doc_worker`.
- No game launch, save test, or live UI rendering was run. This was a documentation-only task.

## Remaining risks

- Some live localisation may still contain the old prose even though the specs and research handoffs are now cleaner.
- The workbook may still carry effect-list wording for Event 020 or stale wording for Events 008, 009, and 010 until its owner performs a final parity pass.
- Archived sourced quotes can still contain em dashes by design. Removing them without checking the source would risk misquotation.
- This pass does not establish that any event, super-event, or catalog row is implemented or complete.
