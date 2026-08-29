# Achievement Implementation Prompt: Event 039 Murder Mystery

Implement the eight accepted Event 39 achievements from `039_murder_mystery_spec_part_16_achievements.md`. Read `AGENTS.md`, the event asset skill, the full Event 39 source package, and existing Chaos Redux achievement patterns before editing.

## Achievement set

Implement these stable working IDs unless a verified repository collision requires a documented rename:

- `039_murder_mystery_no_second_victim`
- `039_murder_mystery_empty_chair_holds`
- `039_murder_mystery_net_without_knives`
- `039_murder_mystery_the_knife_breaks`
- `039_murder_mystery_no_masters_above_us`
- `039_murder_mystery_necessary_hypocrisy`
- `039_murder_mystery_every_chair_empty`
- `039_murder_mystery_last_safe_cabinet`

Use the exact eligible countries, unlock conditions, irreversible disqualifiers, scenario policies, difficulty, visibility, and tracking rules in Part 16. Do not reduce a campaign achievement to one focus or current-state check.

## Tracking

Create durable one-shot flags and actor records for conditions that cannot be inferred safely later. Examples include later victim count, opening response, foreign derivative ever created, original-player side, route lock, derivative viability, terminal office snapshot, meaningful war or objective contribution, and debug or scenario disqualification.

Once a disqualifying event occurs, the achievement remains disqualified. Save and reload must preserve every condition.

Use event-owned callbacks and registries. Recurring world scans are forbidden. Ensure dynamic tag reuse cannot transfer achievement history to a new country package.

## Scenario policy

Natural investigation achievements must reject triggerable-scenario setup. Assassin route achievements may allow High or Maximum only if normal production, route, Cohesion, subject, and unit requirements remain fully earned. Terminal achievements reject debug victory and any future terminal shortcut unless separately accepted.

Record the final policy in localisation direction, documentation, and tests.

## Localisation

Write final achievement names and descriptions from the directions in Part 16. Descriptions should state the public challenge precisely without exposing hidden registry internals. A clearer final title may replace the working title. Retain the stable ID.

## Icons

Route icon production through `chaosx_icon_artist`. Inspect the achievement reference shelf and current engine pattern. Create one distinct base icon per achievement, then the required normal, grey, and not-eligible DDS triplet in `gfx/achievements/` with filenames matching the full achievement ID.

Use the project not-eligible overlay workflow. Do not guess grey treatment, reuse another achievement, or resize focus, idea, or decision art.

## Validation

For each achievement, document:

- eligible actor and start state
- all positive conditions
- all irreversible disqualifiers
- scenario and debug policy
- tracking identifiers
- icon files
- localisation keys
- one normal unlock path
- one near-miss path that must not unlock
- save and reload check
- dynamic-country and inheritance behavior

Test that achievements do not unlock for AI actors when player control is required, after tag switching that violates the condition, through scenario setup that grants prerequisites, or after an invalid terminal registry repair.

Update achievement docs and the Event 39 completion report. Missing icon variants, ambiguous contribution, reversible disqualifiers, or debug shortcuts are blockers.
