# Event 35 Great Depression 2.0 asset repair brief

Status: production delivered.
Event 35 ships 80 runtime DDS files: six report and news scenes, the category picture and category icon, decision, mission, evolution, idea and state-modifier icons, the super-event image, and eligible, grey and not-eligible triplets for six Event 35 achievements and Event 34's Long Fall.
The inventory, consumers and provenance are recorded in `docs/events/035_great_depression.md` (Presentation and asset wiring) and the ignored workspace `docs/assets/035_great_depression/`.

Use this brief only to repair or replace an existing asset, or to add an asset that a newly accepted design item needs.

## Rules

- Follow the `chaos-redux-event-assets` skill; route scenes to `chaosx_generated_event_art` and icons and achievement triplets to `chaosx_icon_artist` with fully explicit prompts.
- Visual direction for every family lives in part 10; keep scenes country-neutral, period-correct, free of readable generated text, and free of modern props.
- Keep existing sprite names and paths so wiring does not change, and inspect the real consumer and reference family before fixing a canvas size.
- Icons request native transparency and keep it through DDS conversion; verify the alpha channel of every saved PNG.
- There are no portraits, flags, 3D models, unit counters or animations in the accepted design.
- When the event is otherwise complete, copy any remaining durable facts into the event doc and delete the workspace (part 10, Asset workspace).
