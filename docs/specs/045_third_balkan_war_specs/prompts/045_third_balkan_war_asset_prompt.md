# Asset production prompt for Event 045: Third Balkan War

Use `chaos-redux-event-assets`, `chaos-redux-super-events`, and `chaos-redux-frame-animation` only if later review adds a genuine animation requirement. Route work through the correct narrow asset subagents with context-complete prompts. Character portraits and 3D work are outside this accepted asset set.

Read the full Event 045 spec pack first, especially:

- `specs/045_third_balkan_war_spec_part_1_core.md`
- `specs/045_third_balkan_war_spec_part_3_escalation_intervention_decisions.md`
- `specs/045_third_balkan_war_spec_part_6_ai_achievements_assets.md`
- `research/045_third_balkan_war_research_notes.md`
- `prompts/045_third_balkan_war_super_event_prompt.md`

Use the temporary workspace `docs/assets/045_third_balkan_war/` during active production. Final runtime files must move to event-scoped engine folders. Promote durable provenance and crosswalk facts into permanent Event 045 documentation, verify that no runtime reference points into `docs/assets/`, then remove the temporary workspace only after the complete event is accepted.

## Required reference inspection

Before producing each asset family, inspect the matching skill-local vanilla reference folder, its `contact_sheet.png`, and its `CATALOG.md` entry. Follow the active vanilla or Chaos Redux consumer to confirm exact dimensions, frame count, alpha behavior, and target sprite definition.

For the decision category picture, inspect:

```text
.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/
```

Create and document the contact sheet first if it is missing.

## Required scene art

### Opening outbreak super-event image

- Stable working basename: `045_third_balkan_war_outbreak`
- Subject: several Balkan armies already mobilizing through one frontier rail junction, crowded troop transport, mountain or border infrastructure, mixed equipment, and evidence of multiple national columns
- Tone: period documentary realism, restrained irony in the situation rather than comedy in the people
- Source mode: sourced period image when a defensible archival scene fits, otherwise generated alternate-history documentary art
- Avoid: a map as the central subject, modern equipment, readable generated text, gore, triumphant single-national propaganda, and jokes about casualties

### Another World War handoff super-event image

- Stable working basename: `045_third_balkan_war_world_war`
- Subject: the regional junction overwhelmed by major-power columns, aircraft, foreign staff vehicles, or several military routes leaving the original theater
- Tone: grave, wider scale, visually distinct from the opening
- Use only when the final stage proof exists

### Report or news image family

Create distinct or clearly staged images for:

- another Balkan country entering
- foreign arms or volunteers arriving
- guarantee or faction enforcement
- direct major intervention
- armistice or regional settlement

Use sourced archival material only when attribution, rights, date, and period fit are defensible. Generated scenes must look like 1936-1945 documentary photographs, not modern cinematic concept art.

## Decision category picture

- Stable working basename: `045_third_balkan_war_category`
- Subject: a frontier rail and road junction, border barriers, mobilizing columns, a visible port or mountain route in the distance, and signs of several competing directions
- Presentation: static category picture
- No fake buttons, fake meter, fake map controls, or generated text
- Confirm the runtime canvas from the actual consumer rather than assuming the reference family's nominal size

## Decision icons

Create independent 32x32 source compositions for:

- `decision_045_register_claim`
- `decision_045_request_arms`
- `decision_045_invite_volunteers`
- `decision_045_secure_corridor`
- `decision_045_offer_armistice`
- `decision_045_allied_occupation`
- `decision_045_frontier_mobilization`
- `decision_045_transit_access`
- `decision_045_mediation`
- `decision_045_guarantee`
- `decision_045_faction_invitation`
- `decision_045_sanctions`
- `decision_045_direct_intervention`

Use native ImageGen transparency, preserve alpha, keep one strong silhouette, and validate at final size. Do not derive these by resizing achievement or super-event art.

## Mission icons

Create independent mission-specific 32x32 art for:

- `mission_045_capital_rail_line`
- `mission_045_port_corridor`
- `mission_045_armistice_line`
- `mission_045_restrain_ally`
- `mission_045_straits_approaches`

## Achievement icons

Create separate 64x64 completed art for the six achievement IDs in `prompts/045_third_balkan_war_achievement_prompt.md`, plus the exact grey and not-eligible variants required by the current achievement consumer.

Achievement files must remain directly under the engine-required achievement root and use full achievement IDs as basenames. Each concept needs its own source art and manifest row.

## Packaging and evidence

For every asset record:

- stable asset ID and consumer
- source mode
- source URL, creator, archive, license, date, and rights confidence when sourced
- ImageGen prompt and native transparency mode when generated
- original source file
- processed PNG preview
- final DDS path
- proposed sprite name
- actual dimensions and alpha behavior
- contact-sheet review
- final-size readability review
- runtime handoff and pending wiring

Do not ship placeholders, primitive local drawings, reused unrelated icons, opaque square backgrounds, fake checkerboards, or unapproved fallbacks. Mark an asset blocked when the required source, rights, reference, or generation route cannot be verified.
