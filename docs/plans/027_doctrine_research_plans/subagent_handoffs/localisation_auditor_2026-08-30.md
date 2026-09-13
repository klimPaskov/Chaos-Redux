# Event 027 Doctrine Research localisation audit handoff

Date: 2026-08-30

Role: isolated final localisation auditor

Scope: Event 027 event, achievement, GFX, scripted-localisation, shared Event Log, Event Details, evolution, settings, and debug mappings named in the parent prompt.

## Outcome

The Event 027 localisation set is mechanically complete after the patch described below.

The audit found no missing localisation keys, duplicate Event 027 keys, unresolved scripted-localisation outputs, missing achievement sprites, missing Event 027 textures, cross-surface naming mismatch, or stale Fire Once wording.

The permitted localisation file lacked its required UTF-8 BOM and contained repeated engine-facing prose such as “native,” “adapter,” “owning doctrine graph,” “ledger authority,” “transaction,” and “Event 027.”

I added the BOM and rewrote only the affected Event 027 player-facing strings in `localisation/english/027_doctrine_research_l_english.yml`.

No gameplay, achievement definition, GFX, shared scripted-localisation, scripted GUI, spreadsheet, or other localisation file was changed.

## Files inspected

- `events/027_doctrine_research.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `interface/027_doctrine_research.gfx`
- `interface/chaosx_achievements.gfx`
- `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/027_doctrine_research_l_english.yml`

The requested debug mapping is defined outside the named files, so I also inspected `common/scripted_localisation/chaosx_scripted_localisation_debug.txt` read-only.

The shared name consumed by those mappings is defined in `localisation/english/chaosx_event_names_l_english.yml`, which I also inspected read-only.

## Event and option coverage

The event file defines 30 Event 027 IDs: `chaosx.nr27.1` through `chaosx.nr27.12`, plus `chaosx.nr27.60` through `chaosx.nr27.77`.

All 251 unique Event 027 title, description, option-name, and custom-tooltip references extracted from those event definitions resolve to keys in the Event 027 localisation file.

The hidden entry event `chaosx.nr27.1` is triggered-only and opens the batch helper flow.

The human-facing chain covers curriculum opening, domain selection, Grand Doctrine selection, track selection, all 18 track-specific subdoctrine pages, confirmation, success, continuation, completion, no-valid-action recovery, and ambiguous-result recovery.

The visible option labels describe navigation and selection, while the actual adoption or mastery consequence is confirmed on `chaosx.nr27.7` with `chaosx.nr27.7.a.tt`.

No visible raw trigger block was found in the Event 027 options.

`chaosx.nr27.4.option_tt` and `chaosx.nr27.5.option_tt` exist but are not referenced by the event source or elsewhere in the repository.

Those two keys are harmless stale localisation rather than missing coverage because the corresponding options only record a selection and open the later confirmation page.

## Missing key list

None.

The Event 027 file contains 314 localisation keys after the patch.

All direct event references resolve, all three achievement NAME and DESC pairs resolve, all achievement eligibility and happened tooltips resolve, all shared Event Log and evolution references resolve, and all 148 unique scripted-localisation output keys resolve against Chaos Redux plus vanilla English localisation.

## Duplicate key list

None.

No duplicate key exists inside `027_doctrine_research_l_english.yml`, and no Event 027-owned key from that file was found duplicated in another mod localisation file.

## Scripted localisation issue list

No missing output key or missing fallback was found.

The nine defined-text helpers are `GetDoctrineResearchDomainName`, `GetDoctrineResearchGrandDoctrineName`, `GetDoctrineResearchTrackName`, `GetDoctrineResearchSubdoctrineName`, `GetDoctrineResearchStageName`, `GetDoctrineResearchLastActionName`, `GetDoctrineResearchLastResultName`, `GetDoctrineResearchConcentrationStatus`, and `GetDoctrineResearchMilestoneStatus`.

Each helper has an explicit fallback, and every one of its 148 unique `localization_key` references resolves.

The event MCP lint was partial and emitted repeated `EVENT_GATE_WITHOUT_WRITER` warnings for `doctrine_research_active_batch` on Event 027 popup triggers.

Those warnings concern gameplay state flow, not localisation, and may be a helper-expansion limitation because the writer is outside the bounded event source.

They were not patched under this localisation-only assignment and should be reviewed by the owning gameplay agent if they persist in a focused state-flow inspection.

## Shared mapping audit

- Event Log evolution, history, and cluster-member selectors map Event ID 27 to `chaosx.event_name.27`.
- Event Details maps `constant:doctrine_research_event.id` to `chaosx.events_log.window.event_details.doctrine_research`.
- Evolution title and body selectors cover all four Event 027 evolution stages.
- Settings maps `settings_event_id = 27` to `chaosx.event_name.27`.
- Settings maps `global.last_fired_event_id = 27` to `chaosx.event_name.27`.
- Debug localisation maps `event_id = 27` to `chaosx.event_name.27`.
- `chaosx.event_name.27` is present and reads “Doctrine Research.”

No mapping points to a missing key or contradictory event name.

## Achievement and GFX audit

The three achievement IDs are `027_doctrine_research_first_lesson`, `027_doctrine_research_single_school`, and `027_doctrine_research_joint_curriculum`.

Each achievement has a NAME, DESC, possible tooltip, happened tooltip, and completion country flag.

The shared possible tooltip is `027_doctrine_research_achievement_eligible_tooltip`, and each achievement's happened tooltip resolves.

The Event 027 report sprite is `GFX_report_event_027_doctrine_research`.

The achievement GFX file defines the base, `_grey`, and `_not_eligible` sprite for each achievement, for nine achievement sprites and ten Event 027 sprite definitions in total.

No Event 027 sprite name is duplicated.

All ten referenced Event 027 DDS files exist, including the report image and all achievement variants.

## Dynamic text opportunities and preservation

The existing country, stage, domain, doctrine, track, subdoctrine, action, receipt, batch-size, and remaining-choice tokens were preserved.

The patch added `[ROOT.GetName]` to the successful-action and no-valid-action descriptions so those messages identify the affected country directly.

No dynamic value was replaced by a static number.

Integer formatting such as `|0` was preserved.

No new scripted-localisation helper was needed.

## Cross-surface mismatch notes

No remaining mismatch was found between event titles, achievement requirements, Event Details, evolution text, settings, debug mapping, and the shared event name.

The rewritten Event Details text still describes the repeatable worldwide curriculum and its two player-facing outcomes without exposing AI handling, snapshots, adapters, or internal ledgers.

The four evolution bodies retain their two-, three-, four-, and five-choice progression.

The achievement rewrites preserve the human-controlled-country restriction, same-curriculum restriction, Evolution IV five-choice branch requirement, and four-distinct-track requirement.

## File encoding concerns

Before the patch, `localisation/english/027_doctrine_research_l_english.yml` did not begin with a UTF-8 BOM.

After the patch, its first three bytes are `EF BB BF`.

No encoding concern was found in the inspected script or GFX files because those are not HOI4 localisation YML consumers.

## Prose-quality findings and repairs

### Vagueness

Before: descriptions referred to a “valid doctrine adapter,” “owning doctrine graph,” “doctrine pool,” and an “unambiguous one-step result” without telling the player what happened.

After: descriptions identify the curriculum, eligible doctrine action, selected country, mastery step, and paused ambiguous result directly.

### Bloat

Before: Event Details explained snapshots, ledgers, batch append behavior, and silent AI resolution.

After: Event Details states who receives the curriculum and what each choice can do in three direct sentences.

### Obvious explanation

Before: several tooltips repeated internal validation and receipt behavior instead of the requirement and consequence.

After: tooltips lead with the choice, success condition, and consequence.

### Repetition

Before: all 18 track descriptions repeated “native track,” “exactly one Event mastery step,” and “banked mastery remains.”

After: the shared wording states that confirmation advances one step, spends one choice, and preserves earned mastery.

### Overcomplication

Before: confirmation and success descriptions used “native prerequisites,” “transaction,” “authority,” and “ledger.”

After: they state what is checked, what succeeded, and when a choice is spent.

### Style-rule repair

The patch removes semicolons and em dashes from the Event 027 localisation file.

It also removes player-facing implementation identifiers and engine-facing terms including “Event 027,” “native,” “adapter,” “owning doctrine graph,” and “ledger authority.”

No stale “Fire Once” or “Fire-Once” wording exists in any assigned source.

## Sourced-quotation preservation notes

No sourced or attributed quotation appears on any inspected Event 027 surface.

No quotation required preservation, and no quote punctuation was altered.

The established stage name “Totalen Chaos” was preserved exactly.

## Changed files

- `localisation/english/027_doctrine_research_l_english.yml`
- `docs/plans/027_doctrine_research_plans/subagent_handoffs/localisation_auditor_2026-08-30.md`

## Changed keys

- Opening and selection: `chaosx.nr27.2.d`, `chaosx.nr27.2.a.tt`, `chaosx.nr27.3.d`, `chaosx.nr27.4.d`, `chaosx.nr27.4.option_tt`, `chaosx.nr27.5.d`, `chaosx.nr27.6.option_tt`
- Track descriptions: `chaosx.nr27.60.d` through `chaosx.nr27.77.d`
- Confirmation and recovery: `chaosx.nr27.7.d`, `chaosx.nr27.7.a.tt`, `chaosx.nr27.8.d`, `chaosx.nr27.9.d`, `chaosx.nr27.11.d`, `chaosx.nr27.11.a.tt`, `chaosx.nr27.12.d`, `chaosx.nr27.12.a.tt`
- Shared Event Details: `chaosx.events_log.window.event_details.doctrine_research`
- Evolution titles: `chaosx.events_log.window.evolution_details.doctrine_research.title.stage_1` through `.stage_4`
- Evolution bodies: `chaosx.events_log.window.evolution_details.doctrine_research.body.stage_1` through `.stage_4`
- Achievement descriptions: `027_doctrine_research_first_lesson_DESC`, `027_doctrine_research_single_school_DESC`, `027_doctrine_research_joint_curriculum_DESC`
- Achievement tooltips: `027_doctrine_research_achievement_eligible_tooltip`, `027_doctrine_research_first_lesson_tooltip`, `027_doctrine_research_single_school_tooltip`, `027_doctrine_research_joint_curriculum_tooltip`

## Display before and after

Before, the player was asked to reason about adapters, native graphs, fixed batches, receipt ledgers, and internal event-attributed mastery.

After, the player sees a curriculum with a known number of choices, the eligible action each choice can perform, the condition under which a choice is spent, and the exact achievement objective.

The mechanical meaning, route identity, established proper names, stage progression, and all dynamic values remain intact.

## MCP evidence

The Event 027 root was traced downstream with helper expansion and a bounded depth of eight.

Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c5f8dc21f90e4ab8bd15df5166b8a1ca2ab9bff4f6ff20a3b8ac547d7bee9bd/0d830c43a7798bc42341964d1e8c22bb734a3e9ef175567b28d524ca16270501/event-trace-55c38793c7fb.json`

Post-patch Event 027 opening-options manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95d2ea96da6d987e02532c6e63736b3852b5f9418f21d8f0164352701ac9b3f6/1dff7ac52f5d62f73ee3d6822468967de227849b688a5358fa62c7be0aeddb7c/event-options-903a0ec1e1c7-manifest.json`

Post-patch Event 027 opening-options PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99ce9f9d716dae5045848945d79ba84b4fccd13d8c7167d600e4e27157b0ce3f/e02be1d96ada3a6ffc4368f6363f4ea26d6a807e1fdd1860fd88ec8ea6ba8b1a/event-options-903a0ec1e1c7.png`

The Event MCP returned `EVENT_RENDERED_PARTIAL` because the large workspace deferred workspace-wide helper projections and lifecycle passes.

The Event Log GUI inspector accepted `events_log_popup_window` with generated scenario `event_027_details-generated-1`.

GUI inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00402f0e848af91b9be8865d1c8c4710130504e27bf43da9dd638642728ce517/6f4d1d41c8ef1c0f7a7d8af726f6bb88bb94f8ebf339900e7cdf767ca8b557fe/gui-inspect.a83c63e468778828.json`

GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d17a9b4c91ab934060e2c715bc7b1494fe4324f16a6038edb12c935172f97526/9e9c3f80dd20448cbc0bc18d693cae4aa17fe874243835f98e8861c51018b6c8/events_log_popup_window-full.svg`

The generated GUI scenario did not inject the Event 027 Event Details or evolution strings into the rendered artifact, so the production Event Log render could not verify those specific strings for clipping, wrapping, or overflow.

This is an exact MCP scenario-fidelity blocker, and source review is not treated as equivalent visual evidence.

The GUI inspector also reported workspace-wide symbol-collision diagnostics and six non-blocking visible-overlap findings, but the bounded inline response did not attribute those findings to the Event 027 text fields.

## Meaningful validation

- Parsed 314 Event 027 localisation keys with zero duplicates.
- Parsed 30 Event 027 event IDs and 251 unique direct event localisation references with zero missing references.
- Resolved 148 unique scripted-localisation output keys against the mod and vanilla English localisation with zero missing outputs.
- Verified three achievement IDs and all corresponding NAME, DESC, possible-tooltip, and happened-tooltip keys.
- Verified ten Event 027 sprite definitions with zero missing or duplicate expected sprites.
- Verified all ten referenced Event 027 DDS files exist.
- Verified the localisation BOM is `EF BB BF`.
- Verified zero hits for stale Fire Once wording, semicolons, em dashes, “Event 027,” “native,” “adapter,” “owning doctrine graph,” and “ledger authority” in the patched Event 027 localisation file.

## Skipped meaningful validation and why

No live-game validation was performed or claimed.

No live event-popup interaction was performed because agents may not launch Hearts of Iron IV.

Event Log clipping and overflow for the specific Event 027 Event Details and evolution strings remain visually unverified because the available generated MCP scenario did not populate those strings in the production render.

## Remaining risks and recommended follow-up

1. The owning GUI reviewer should render `events_log_popup_window` with a scenario that explicitly selects Event ID 27 and injects Event 027 Event Details and each evolution stage, then check both 1920×1080 and 1366×768 at UI scale 1.
2. The owning gameplay agent should run a focused Event MCP state-flow inspection for `doctrine_research_active_batch` if the partial lint's `EVENT_GATE_WITHOUT_WRITER` warning remains after helper expansion.
3. The owning event agent may either remove the unreferenced `chaosx.nr27.4.option_tt` and `chaosx.nr27.5.option_tt` keys or wire them if selection-page tooltips are desired, but no gameplay edit was authorized here.

## Unresolved wording decisions

None.

The achievement conditions and curriculum consequences were concrete enough to rewrite without changing mechanics.

## Commit status

No commit was created.

The repository had extensive unrelated work in progress, and `localisation/english/027_doctrine_research_l_english.yml` already contained a large uncommitted Event 027 implementation before this audit.

Committing that file would have captured changes not owned by this isolated auditor.

## Simplifications, omissions, and blockers

No requested Event 027 localisation surface was omitted from source inspection.

The only incomplete evidence is the Event 027-specific Event Log production render described above.

No gameplay or shared-file simplification was introduced.
