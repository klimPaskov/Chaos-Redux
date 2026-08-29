# Prompt for `chaosx_icon_artist`

Spawn with `fork_context=false`.

Repository root: `<MOD_ROOT>`.

Read:

- the asset prompt
- the asset matrix
- `chaos-redux-event-assets`
- matching vanilla-reference catalogs and contact sheets

Create the accepted icon families:

- decision category icon
- four famine-stage state modifier icons
- five displacement and reception state modifier icons
- decision icons for relief, convoy, airlift, evacuation, border policy, controlled medical reception, distribution, integration, and return
- eight achievement triplets from the achievement prompt
- Deaths icons or texticons only if the parent provides a verified consumer

Use ImageGen source evidence for every generated icon.

Each asset type needs separate source art and its own native-size brief. Do not resize one icon type to satisfy another.

Require real transparency, centered silhouettes, matching reference style, no white matte, no checkerboard, no opaque square, no generated text, and clear native-size readability.

Create source PNGs, processed PNGs, final DDS files, contact sheets, manifest rows, and `gfx_handoff.md`.

Do not edit gameplay, localisation, GUI, or spreadsheet files.

Write the handoff under:

```text
docs/plans/famine_and_migration_system_plans/subagent_handoffs/icon_asset_handoff.md
```
