# Unresolved Verification Blockers

> Historical planning snapshot: these environment blockers were resolved in the mounted live repository. The offline wiki, vanilla documentation, repository precedents, implementation files, assets, and audit surfaces were consulted during implementation. This file is retained as provenance and does not describe current blockers. Current gates are recorded in `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_source_of_truth_and_resume_2026_07_15.md`.

These are environment blockers from the planning run. They are not design omissions.

## Repository file map

The full Chaos Redux repository was not mounted. Exact current Event 15 files, helper names, GUI patterns, focus loaders, and documentation paths were not verified.

Required resolution:

- run the repo explorer prompt in the live repository

## Offline wiki and vanilla precedent

The required `paradox_wiki/` snapshot and vanilla Hearts of Iron IV documentation were not mounted.

Required resolution:

- inspect the required event, focus, decision, GUI, GFX, country, localisation, AI, effect, trigger, and scope references before implementation

## Exact industrial thresholds

The design uses weak-country bands. Exact factory, state, focus-depth, and faction thresholds need live balance review.

Required resolution:

- map current event target distribution and choose centralized tuning constants

## Protected-tree registry

The package assumes a reusable test for safe tree replacement. Its current existence is unknown.

Required resolution:

- reuse an existing registry or design one through the scripted-system architect

## Exact geography helpers

Port, island, corridor, resource, and Inland Island target helpers require live map and state review.

Required resolution:

- use dynamic regions or verified scripted state groups

## Scripted GUI precedent

The exact parent window, dimensions, button pattern, and selected-target GUI support were not verified.

Required resolution:

- inspect current Chaos Redux and vanilla GUI examples

## Asset production

Historical blocked state, resolved: at the time of this planning snapshot, `interface/015_utopia_manifesto_super_event.gfx` and display slots `96`-`100` required five DDS files that did not yet exist:

- `gfx/super_events/015_utopia_manifesto/super_event_015_consent_of_households.dds`
- `gfx/super_events/015_utopia_manifesto/super_event_015_common_table.dds`
- `gfx/super_events/015_utopia_manifesto/super_event_015_guardians_of_measure.dds`
- `gfx/super_events/015_utopia_manifesto/super_event_015_closed_island.dds`
- `gfx/super_events/015_utopia_manifesto/super_event_015_joke_understood.dds`

All five route-specific masters, processed PNGs, final DDS files, source records, checksums, sprite registrations, and route mappings now exist. The two legacy images are unregistered historical files and are not fallbacks. Current evidence is in `docs/assets/015_utopia_manifesto/manifest.md`, `docs/assets/015_utopia_manifesto/gfx_handoff.md`, and the completion coverage matrix.

## Super-event research package

Text and audio research are complete and integrated.

- title and cultural remark: original Chaos Redux wording, documented in `docs/super_events/015_utopia_manifesto_super_event_text_research.md`
- main quote: exact closing sentence from Thomas More's *Utopia*, Gilbert Burnet translation, verified against the Project Gutenberg primary text and public-domain compatible
- audio: Brahms, *Symphony No. 3 in F major, Op. 90*, III. *Poco allegretto*, Musopen Symphony Orchestra
- recording rights: file-specific CC0 1.0 Universal; source file matches the Commons SHA-1 and byte size
- runtime: exclusive playback audio ID `57`, final `116 s` OGG and WAV, six music helpers, six sound wrappers, and display slots `96`-`100`
- catalogue: active row in `music/chaosx_music_track_list.html`
- uniqueness: no matching cue under any other event in the current `54`-OGG and `52`-WAV scan; the only WAV match is the expected Event 015 mirror

Resolved disposition:

- no text-source, audio-source, licence, attribution, uniqueness, or route-image action remains

## Workbook

The supplied CSV was read, but the live `chaos_redux_events_catalog.xlsx` workbook was not mounted or edited.

Required resolution:

- run the spreadsheet worker after final localisation

## Formal subagent passes

No custom subagent was executable in this environment.

Required resolution:

- run every relevant prompt in the orchestration order with `fork_context=false`

## Completion status

This planning package is complete as a design handoff. Event 15 implementation is not complete and is not claimed to be complete.
