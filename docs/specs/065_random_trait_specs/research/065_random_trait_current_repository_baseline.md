# Event 065 Current Repository Baseline

## Inspection snapshot

- Repository: `klimPaskov/Chaos-Redux`
- Default branch inspected: `master`
- Indexed commit shown by repository search: `d549536e869056a49890a08ff795fbc80659984e`
- Inspection date: `2026-09-03`

This is a targeted Event 65 inspection.

It is not a full repository audit.

## Current event script

Path:

`events/065_random_trait.txt`

Observed structure:

1. `chaosx.nr65.1` is hidden and triggered only.
2. Its immediate block loops over `every_country`.
3. Every country receives `chaosx.nr65.2`.
4. `chaosx.nr65.2` is a visible report event.
5. Its option contains the trait `random_list`.
6. The actual leader mutation therefore occurs when each country resolves the visible event option.
7. The random list carries a `TODO` note to add more traits.
8. The list is manually maintained.
9. The list contains repeated source IDs.
10. Confirmed examples include `devoted_trotskyist` and `inventive_genius`.
11. No Baseline, Evolution I, Evolution II, or Evolution III branch was observed.
12. No duplicate redraw, existing-trait exclusion, saturation handling, result counter, ledger, or weight class was observed.

## Current design problems

### Mutation timing

Putting the gameplay effect in the visible option makes the result depend on event resolution.

Human players can leave the popup open.

AI countries resolve through a different visible-event path.

Multiplayer clients can hold reports for different lengths of time.

The rework should apply the global mutation before reports open.

### Pool maintenance

The current file is a long hand-maintained list.

That approach cannot prove complete coverage after a game update, DLC update, or Chaos Redux trait addition.

Repeated source IDs alter probability.

A missing source ID is hard to detect.

The rework should generate and validate the list from the final loaded country-leader trait sources.

### Evolution coverage

The current script does not implement the user-provided `1`, `2`, `3`, and `5` trait counts.

It does not implement high-Evolution featured weighting.

### Feedback

The current report does not show the trait selected for the player's leader.

It does not show global counts, active Evolution, pool size, collision handling, or saturation.

## Current localisation

Path:

`localisation/english/065_random_trait_l_english.yml`

Observed content:

- generic root title
- generic visible report title
- generic description about a leader changing their approach to government and war
- generic acknowledgment option

The current description is too broad for the new global premise.

It also does not explain the player's actual result.

The rework needs final direction-based text written after the runtime data contract exists.

## Current random-event registration

Path:

`common/scripted_effects/chaosx_logic_effects.txt`

Event `65` is already added to `global.repeatable_events`.

The rework should preserve that registration and verify all shared pool counters and selectors.

## Current event-name mapping

Path:

`localisation/english/chaosx_event_names_l_english.yml`

Event `65` is mapped to `Random Trait`.

The accepted event name already matches the user's catalog entry.

## Current image wiring

Path:

`interface/chaosx_pictures.gfx`

Sprite:

`GFX_report_event_leader_trait`

Runtime file:

`gfx/event_pictures/065_random_trait/report_event_leader_trait.dds`

Repository metadata reports the DDS file as `130` bytes.

That size is unusually small for a final `210x176` report image.

The file must be inspected as an image and validated for format, dimensions, content, and runtime readability before reuse.

The planning package does not assume it is valid or invalid.

## Current cluster constants

Path:

`common/script_constants/event_cluster_constants.txt`

The inspected constant registry assigns:

- Wars `1`
- Liberations `2`
- Diplomatic Panic `3`
- Peace `4`
- Natural Disasters `5`
- Formables `6`
- Positive Economy `7`
- Diseases `8`

ID `9` is free in that source snapshot.

The supplied cluster CSV uses ID `10` for Intelligence.

The current preferred reservation for Randomizations is ID `9`, pending a fresh implementation-time collision check.

## Required repository delta

The implementation should:

1. Replace the visible-option mutation with one hidden authoritative executor.
2. Add event-owned constants, triggers, effects, ledgers, counters, and debug hooks.
3. Add the generated trait registry tool and outputs.
4. Remove manual duplicates.
5. Implement the `1`, `2`, `3`, and `5` grant counts.
6. Implement uniform and featured weight profiles.
7. Add Event 65 Evolution state and history.
8. Add direct Chaos milestones.
9. Send reports only to human-controlled countries.
10. Add result-safe scripted localisation.
11. Validate or replace the report image.
12. Add complete Event Log and Event Details coverage.
13. Add Randomizations cluster wiring after the ID check.
14. Update permanent docs and the authoritative workbook.
15. Keep normal campaign enablement off until the rework reaches `Needs Testing`.

## Inspection boundary

This baseline relied on the current Event 65 files and directly connected shared systems.

A live repo explorer should repeat the inspection before implementation because the repository may change after this planning snapshot.
