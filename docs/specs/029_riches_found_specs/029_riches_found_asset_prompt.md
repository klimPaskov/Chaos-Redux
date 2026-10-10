# Event 029 asset prompt

Use this prompt for the remaining Event 029 asset work.

The inventory, subject directions, and status table are owned by [Part 6](029_riches_found_spec_part_6_assets_localisation_achievements.md); runtime sprites are registered in `interface/029_riches_found.gfx`, and provenance lives in `docs/assets/029_riches_found/` and the dated records under `docs/events/029_riches_found/`.

## Routing

- Decision, mission, state-modifier, idea, evolution, and achievement icons: `chaosx_icon_artist`.
- Report art and the category picture: `chaosx_generated_event_art`.
- No portrait, flag, focus icon, animation, audio, unit, counter, or 3D asset belongs to Event 029.

Follow `.claude/skills/chaos-redux-event-assets/SKILL.md` for the image-generation route, reference families under `.claude/skills/chaos-redux-event-assets/assets/gfx_references/`, native transparency, processing, DDS conversion, contact sheets, manifests, and handoffs.
Asset workers do not edit gameplay, interface, localisation, documentation, or catalog files; the parent owns wiring and documentation.

## Remaining work

1. Review or repair the 37 decision icons that have not been individually reviewed, from versioned masters and exact decoded DDS views on the vanilla row background; contact sheets or hash counts are not visual proof.
2. Reconcile the evacuation v5 and temporary-closure v4 composites with their selected DDS versions before either is accepted.
3. Final review of the mission, state-modifier, idea, and report families.
4. The three evolution icons need a live consumer, which is parent wiring rather than new art.
5. Before Event 029 is called complete, move durable provenance, prompts, review facts, hashes, and runtime crosswalks from `docs/assets/029_riches_found/` into permanent event documentation, then clear the temporary workspace.

A missing or rejected required asset stays blocked; a placeholder is never reported as complete.
