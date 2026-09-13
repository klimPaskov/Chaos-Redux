# Asset orchestration prompt: Event 043 Monsters from the Deep

Coordinate the complete Event 043 asset package from:

```text
docs/specs/043_monsters_from_the_deep_specs/
```

Use no inherited conversation context.

## Read first

Read `AGENTS.md`, the complete Event 043 package, event-assets skill, frame-animation skill, portrait skill, 3D skill, super-event skill, subagent skill, matching vanilla reference catalogs, and current runtime consumers.

## Route by asset type

- portraits and portrait animation: `chaosx_portrait_creator`
- generated report, category, flag, emblem, and super-event art: `chaosx_generated_event_art`
- archival or real-source research when needed: `chaosx_asset_source_researcher`
- focus, idea, decision, mission, achievement, and small UI icons: `chaosx_icon_artist`
- every unit model, skeletal action, sourced unit sound, and counter brief: `chaosx_3d_model_pipeline`
- final super-event text and music research: their dedicated research agents

Every subagent runs with a complete prompt and `fork_context=false`.

## Source of truth

Use `matrices/043_asset_requirement_crosswalk.md` and `matrices/043_3d_model_brief_matrix.md`.

Do not infer unlisted advisor portraits or extra asset families. Do not omit a required asset because another file looks similar.

## Rules

- separate icon types
- native transparency for alpha-backed assets
- flat opaque flags
- real source frames for animation
- unique apex geometry
- unique sourced unit sounds
- bespoke vanilla-green counters
- original Cthulhu art
- no commercial design copying
- no cultural pattern copying
- no primitive placeholder art
- no final runtime asset under `docs/assets`
- no unapproved fallback

## Working folder

Use `docs/assets/043_monsters_from_the_deep/` during active work. Preserve source, prompt, rights, processing, checksums, contact sheets, manifests, model jobs, and handoffs.

## Parent responsibility

The parent registers sprite and entity IDs, wires GFX, GUI, events, focuses, decisions, characters, sound definitions, and gameplay, then verifies live consumers.

## Completion

Reconcile every crosswalk row with a final runtime consumer. Promote durable evidence into permanent Event 043 docs. Delete the temporary workspace only after all runtime references and reviews pass.

Report missing, blocked, needs-user-review, generated, sourced, processed, wired, and verified states separately.
