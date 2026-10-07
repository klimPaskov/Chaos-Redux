# Prompt for `chaosx_icon_artist`

Spawn with no inherited thread context (Codex `fork_turns="none"`; other runtimes follow the [subagent skill](../../../../.agents/skills/chaos-redux-subagents/SKILL.md)).

Repository root: `<MOD_ROOT>`.

Read:

- the asset prompt
- the asset matrix
- `chaos-redux-event-assets`
- matching vanilla-reference catalogs and contact sheets

Create the accepted icon families:

- two separate decision category icons and their verified consumers
- four famine-stage state modifier icons
- five displacement and reception state modifier icons
- decision icons for relief, convoy, airlift, evacuation, border policy, controlled medical reception, distribution, integration, and return
- eight achievement triplets from the achievement prompt
- Deaths icons or texticons only if the parent provides a verified consumer

Use ImageGen source evidence for every generated icon.

Each asset type needs separate source art and its own native-size brief. Do not resize one icon type to satisfy another.

Request native ImageGen transparency for alpha-backed families and preserve alpha through processing and DDS conversion.
Follow the owner skill for fallback-only alpha repair and record any fallback.
Require real transparency, centered silhouettes, matching reference style, no white matte, no checkerboard, no opaque square, no generated text, and clear native-size readability.

Create source PNGs, processed PNGs, final DDS files, contact sheets, manifest rows, and `gfx_handoff.md`.

Do not edit gameplay, localisation, GUI, or spreadsheet files.

Write the handoff under:

```text
docs/plans/famine_and_migration_system_plans/subagent_handoffs/icon_asset_handoff.md
```
