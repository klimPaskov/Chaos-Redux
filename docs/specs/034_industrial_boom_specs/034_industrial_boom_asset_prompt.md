# Asset production prompt for Event 34 Industrial Boom

Create the complete Event 34 Industrial Boom visual package according to the accepted specification under `docs/specs/034_industrial_boom_specs/`.

Read `AGENTS.md`, `chaos-redux-event-assets`, and the Event 34 specification before production. Use `chaos-redux-frame-animation` only when an implementation-approved animated state is added. Do not infer portraits, flags, focus icons, unit counters, 3D models, or super-event assets from the event theme.

## Source and ownership split

Use `chaosx_generated_event_art` for the fictional period report image and decision-category pictures. Use `chaosx_icon_artist` for category, decision, project, idea, state-modifier, and achievement icons. Character portrait workers are outside this package.

Inspect the matching canonical reference family and its contact sheet before creating each asset type. Follow the owning vanilla or established Chaos Redux consumer. When a required contact sheet is missing, create it with filenames and native dimensions and update the reference catalog before production.

All alpha-backed icons require native ImageGen transparency from the first generation, preserved through processing and DDS conversion. Reject opaque squares, fake checkerboards, white halos, chroma spill, clipped silhouettes, and transparent holes. Background removal is fallback-only and must be recorded.

## Event art

### Opening report image

Working asset identity: `034_industrial_boom_opening_report`

Source mode: generated fictional period documentary scene.

Visual direction:

- A 1936 to 1945 factory hall, shipyard, or rail-linked industrial complex operating at extraordinary pace.
- Workers, machinery, crates, rail wagons, cranes, furnaces, assembly lines, or machine shops should make output volume visible.
- Crowded aisles, temporary scaffolding, stacked inputs, multiple shifts, and worn machinery should imply future strain without turning the opening into a disaster scene.
- Documentary realism or period illustrated-newsreel realism.
- Strong subject and readable composition at the report-image crop.

Avoid:

- Maps as the main subject.
- Staff tables and conference rooms.
- Modern robotics, digital displays, contemporary safety clothing, modern trucks, or postwar factories.
- Readable generated text, logos, watermarks, UI overlays, and financial charts.
- Modern cinematic color grading.

Create the generated source PNG, processed preview, final DDS, prompt record, source-mode note, and manifest entry. Inspect the active report-event consumer for final dimensions and crop.

## Decision category pictures

Inspect the canonical decision-category picture references at the skill-local `icons/decision_categories/pictures/` family and its contact sheet. Verify the live consumer before selecting the final canvas.

Create three coordinated but separately generated pictures:

1. `034_industrial_boom_category_productive`
   - Coordinated industrial flow from factory to rail or port.
   - Busy, beneficial, and controlled.
2. `034_industrial_boom_category_strain`
   - The same economic identity under congestion, maintenance pressure, material queues, and crowded transport.
   - Still productive, visibly overextended.
3. `034_industrial_boom_category_landing`
   - Inspection, repair, reduced shifts, conversion work, and retained infrastructure.
   - Controlled transition with collapse avoided.

Do not create these states by local recoloring, smoke overlays, brightness changes, or filter-only edits of one still. Each final state needs its own source art. Keep composition, period, and visual language coordinated.

The pictures are presentation only. Do not paint fake buttons, values, meters, or controls into them.

## Decision category icon

Working identity: `034_industrial_boom_category_icon`

Motif:

- A factory complex combined with an overworked flywheel, furnace, or mechanical limit indicator.

Requirements:

- Strong centered silhouette.
- Native transparent background when the inspected consumer uses alpha.
- Dark outline and subtle shadow appropriate to the reference family.
- Readable at final size.

## Core decision icons

Create separate decision-specific source art for:

- `034_industrial_boom_run_hot`
  - Overdriven flywheel, furnace, or assembly line.
- `034_industrial_boom_stabilize_supply`
  - Linked rail, truck, port crane, and material flow.
- `034_industrial_boom_build_reserves`
  - Spare machine tools, stored components, repair stores, or deliberately idle capacity.
- `034_industrial_boom_cool_expansion`
  - Throttled machinery, closed industrial valve, or reduced furnace intensity.
- `034_industrial_boom_protect_region`
  - Factory protected by repair, redundancy, or civil-defense infrastructure.
- `034_industrial_boom_credit_restraint`
  - Restrained contract or credit mechanism expressed through period industrial symbols, without modern currency graphics.
- `034_industrial_boom_liquidate_projects`
  - Cancelled construction, dismantled scaffold, or closed speculative works.
- `034_industrial_boom_emergency_logistics`
  - Priority rail and transport rerouting.
- `034_industrial_boom_emergency_halt`
  - Main industrial switch, stopped flywheel, or closed furnace under emergency control.
- `034_industrial_boom_controlled_landing`
  - Factory transition, inspection, and retained machinery.

Decision icons must follow the decision-icon reference family. Do not resize the category icon or an idea icon to satisfy them.

## Project icon family

Create a coordinated source family with distinct subjects:

- `034_industrial_boom_project_production_practices`
- `034_industrial_boom_project_rail_supply`
- `034_industrial_boom_project_conversion_capacity`
- `034_industrial_boom_project_repair_network`
- `034_industrial_boom_project_resource_efficiency`
- `034_industrial_boom_project_permanent_capacity`
- `034_industrial_boom_project_synthetic_recycling`
- `034_industrial_boom_project_machine_city`
- `034_industrial_boom_project_controlled_corridor`
- `034_industrial_boom_project_unrestricted_spread`
- `034_industrial_boom_project_contain_spread`

The coordinated family may share palette, line weight, industrial materials, and frame logic. Each icon still needs separate source art designed for the actual consumer.

## Country effect icon family

Inspect the ideas and national-spirit reference family. Create staged icons for the actual effect lifecycle:

- `034_industrial_boom_idea_baseline`
- `034_industrial_boom_idea_speculative_mania`
- `034_industrial_boom_idea_industrial_miracle`
- `034_industrial_boom_idea_runaway_industrialization`
- `034_industrial_boom_idea_cooling`
- `034_industrial_boom_idea_exhaustion`
- `034_industrial_boom_idea_post_boom_vulnerability`
- `034_industrial_boom_idea_retained_legacy`

Use staged replacement and clear shared identity. Do not create generic factory icons with only color changes. Each stage should show a distinct condition at final size.

## State modifier icon family

Inspect the state-modifier reference family and owning definition. Create:

- `034_industrial_boom_state_region`
- `034_industrial_boom_state_protected_region`
- `034_industrial_boom_state_tested_protection`
- `034_industrial_boom_state_compromised_protection`
- `034_industrial_boom_state_active_project`
- `034_industrial_boom_state_secured_legacy`
- `034_industrial_boom_state_fragile_miracle`
- `034_industrial_boom_state_spread`
- `034_industrial_boom_state_unfinished_works`
- `034_industrial_boom_state_exhaustion`

Related statuses should use symbols and frame differences that remain legible without relying on color alone.

## Overheating presentation assets

Inspect the selected category or compact-meter consumer before production. Create only the assets that the implementation confirms are required.

Likely needs:

- Period industrial meter frame.
- Fill or segmented threshold strip.
- Current marker.
- Trend icons for falling quickly, falling, stable, rising, and rising quickly.
- Reserve status icons for none, limited, strong, and depleted.
- Landing forecast icons for strong, uncertain, dangerous, and emergency.

The meter must avoid a modern digital dashboard. Thresholds need shape and text support in addition to color.

Animation is not required. Do not create a transform-only pulse or glow. When implementation approves a warning animation, follow the frame-animation skill with real per-frame art and a static fallback.

## Achievement icons

Create one completed 64x64 source direction for each planned achievement, then produce the required grey and not-eligible variants according to the current Chaos Redux achievement pattern:

- `chaos_redux_034_managed_expansion`
  - Overdriven industry returned below a marked limit.
- `chaos_redux_034_miracle_holds`
  - Dense factory and railway complex held inside a strong structure.
- `chaos_redux_034_redline_nation`
  - Pressure indicator near maximum with the production line intact.
- `chaos_redux_034_the_long_fall`
  - Idle industrial skyline with one restored plant or rail line.
- `chaos_redux_034_built_to_last`
  - Two generations of industrial works integrated into one network.
- `chaos_redux_034_every_link_held`
  - Damaged outer network with an intact central flow.

Achievement filenames must match the final achievement IDs and remain directly under the engine-required achievement root when the current consumer requires root placement.

## Contact sheets and review

Create contact sheets that show:

- Source art and final processed candidates.
- Filenames and native dimensions.
- Final-size icon previews.
- Alpha over light, dark, and checker review backgrounds.
- Phase picture crops.
- Coordinated family consistency.

Reject:

- Reused vanilla art.
- Resized unrelated icons.
- Primitive local drawings.
- One source image used to satisfy several asset types.
- Unreadable tiny detail.
- White matte or opaque square backgrounds.
- Fake text.

## Packaging and handoff

During production use `docs/assets/034_industrial_boom/` as the temporary workspace. Final runtime files must move into event-scoped engine folders such as `034_industrial_boom` under the correct asset category. Do not leave runtime references pointing into the temporary workspace.

Write the manifest and `gfx_handoff.md` with:

- Asset ID and type.
- Source mode.
- Prompt or source record.
- Reference family and consumer inspected.
- Source and final paths.
- Dimensions, alpha mode, and DDS settings.
- Proposed stable sprite name.
- Status and review result.
- Blockers and any approved exception.

Do not edit gameplay, localisation, GUI, decisions, events, ideas, scripted effects, scripted triggers, or the catalog workbook unless the parent explicitly expands scope. The parent owns final non-portrait GFX wiring and live consumer validation.
