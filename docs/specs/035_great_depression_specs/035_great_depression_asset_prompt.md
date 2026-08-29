# Event 35 Great Depression 2.0 asset-production prompt

## Goal

Create the complete final visual asset package required by the accepted Event 35 specification under `docs/specs/035_great_depression_specs/`. Follow `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-frame-animation` when animation is explicitly approved, and the exact installed-vanilla reference family for each consumer.

This prompt covers final art production and handoff. It does not authorize gameplay, localisation, `.gfx`, `.gui`, event, decision, idea, achievement, sound, or spreadsheet edits unless the parent grants a narrow file list.

## Required reading

Read:

- Specification parts 1 through 11.
- Decision map and state lifecycle map.
- Research notes.
- Repository cross-check.
- Super-event prompt.
- Achievement prompt.
- Current Event 35 art, sprites, and consumers.
- Skill-local reference README, catalog, contact sheets, and exact source entries.

Inspect every final consumer before choosing dimensions, alpha, crop, frame count, or DDS format.

## Routing

Use separate bounded subagent tasks:

- `chaosx_generated_event_art` for fictional or alternate-history report, news, category, recovery, Social Collapse, and super-event scenes.
- `chaosx_asset_source_researcher` only when the chosen asset must show real archival material.
- `chaosx_icon_artist` for category, decision, mission, idea, state, evolution, modifier, and achievement icons.
- `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher` for Evolution III text and sound research.

Character portraits are not part of the accepted baseline inventory. A later leader or country route must use `chaosx_portrait_creator` under its own approved brief.

## Temporary workspace

Use:

`docs/assets/035_great_depression/`

Suggested structure:

```text
docs/assets/035_great_depression/
  manifest.md
  gfx_handoff.md
  source/
  generated/
  processed/
  contact_sheets/
  super_event/
  achievements/
  notes/
```

Keep the workspace while production is active or blocked. Before final event completion, promote durable provenance, prompt, review, and runtime crosswalk facts into permanent Event 35 or super-event documentation, verify no runtime reference points into `docs/assets/`, then delete the event-scoped workspace.

## Report and news images

### Asset 1: Independent depression opening

Role:

- Main Event 35 national opening report.

Source mode:

- Generated period documentary art by default.

Composition:

- One clear industrial setting.
- Closed factory gates, idle machine hall, unused freight yard, halted construction, or workers leaving a closed plant.
- Human figures at period scale.
- 1930s to 1940s clothing, vehicles, industrial equipment, and architecture.

Mood:

- Severe economic interruption.
- Practical human hardship.
- No horror or exaggerated spectacle.

Avoid:

- Stock chart.
- Currency pile.
- Boardroom.
- Map.
- Government desk.
- Modern skyscraper.
- Digital display.
- Readable generated headline.
- Cinematic teal and orange treatment.

### Asset 2: Industrial Boom collapse opening

Role:

- Event 35 inherited opening from Event 34.

Source mode:

- Generated.

Composition:

- A recently expanded industrial complex suddenly idle.
- Unfinished new factories, abandoned construction cranes, packed but unused rail sidings, new machinery under covers, or workers at closed gates.
- Visible contrast between recent expansion and sudden stoppage through the scene itself.

Avoid:

- Splitting the canvas into before and after panels.
- Text labels.
- Abstract boom and bust arrows.
- Reusing the independent opening scene with only color changes.

### Asset 3: Contagion conversion

Role:

- Material international conversion into full Event 35 when a separate report image is used.

Source mode:

- Generated.

Composition:

- Port warehouses, export factory, freight station, or ship-loading area losing activity after foreign orders or imports disappear.
- One clear domestic scene with visible external dependence.

Avoid:

- World map and arrows.
- Currency exchange board.
- Generic international handshake.

### Asset 4: Social Collapse major report

Role:

- A major strike, factory occupation, government crisis, coup, or civil conflict milestone.

Source mode:

- Generated unless a real archival scene is intentionally selected and licensed.

Composition:

- Specific factory gate, occupied workshop, industrial square, military building, or government street.
- Period crowd and security presence.
- The asset must match the exact incident family selected by implementation.

Tone:

- Serious.
- No caricature, gore, or comic crowd behavior.

### Asset 5: National news image

Role:

- Public news for independent national depression.

Source mode:

- Generated or sourced according to final direction.

Composition:

- Wider public view of idle industry, relief line, or halted city construction.
- Distinct from the national report crop.

### Asset 6: International recovery

Role:

- Evolution III recovery report or news.

Composition:

- Freight, ports, public works, and industry resuming.
- Workers, locomotives, and cranes returning to service.
- Visible remaining damage or unfinished repair.

Avoid:

- Handshake as main subject.
- Conference table.
- Clean modern prosperity advertisement.

## Decision category pictures

Inspect the exact category-picture consumer and the canonical reference family before production.

### Panic and Contraction picture

- Closed gates, halted freight, anxious workers, unfinished construction.
- Strong focal subject and enough dark or quiet area for category text.

### Depression picture

- Long-term idle machinery, shuttered workshop, worn relief line, or abandoned industrial district.
- Different scene or composition from Panic.

### Stabilization picture

- Repair crews, supervised reopening, railway maintenance, or public works in progress.
- Mixed damage and returning activity.

### Recovery picture

- Operating workshop, moving freight, reopened gate, and returning workers.
- Avoid pristine triumph. Scars should remain visible.

Alternative:

- One strong base picture plus approved static phase overlays or distinct crops can replace four full scenes only after consumer and readability review. The manifest must record the decision.

## Category icon

Subject direction:

- Stopped industrial gear, shuttered factory, idle smokestack, or broken production line.

Requirements:

- Separate source art.
- Native transparent background when the consumer uses alpha.
- Clear silhouette at final size.
- Dark outline and subtle shadow when appropriate.
- No square opaque background.
- No text, currency sign, stock arrow, or generic warning triangle as the only subject.

## Core decision icons

Create separate source art for each.

### Emergency Public Works

- Worker, shovel, railway, scaffolding, bridge repair, or construction machinery.
- Employment and infrastructure must read at 32x32.

### Rescue Strategic Industry

- Protected factory, machine tool, military plant, or shielded industrial gear.
- Avoid a generic shield resized from another asset.

### Stabilize Finance and Trade

- Secured payment ledger, bank door, cargo manifest, port crate, or guarded trade route symbol.
- Avoid readable text and modern banking symbols.

### Austerity and Retrenchment

- Cut project, closed file of commitments, withdrawn scaffolding, or reduced public works motif.
- Avoid scissors as a generic office icon unless the final composition remains period and economic.

### Direct State Planning

- Production board, allocated factory, state-directed gear network, or official industrial plan motif.
- Avoid modern flowchart UI.

### Let the Market Clear

- Closed plant beside surviving machinery, auctioned industrial equipment, or collapsing weak workshop.
- Show contraction without using a stock arrow.

## State-action icons

Create separate 32x32 icons for:

- Protect Depression Center.
- Reopen Idled Plants.
- Rebuild Shuttered Center.
- Restructure or Consolidate.
- Abandon Center.
- Select Center when the selector uses an icon.

## Mission icons

Create separate mission art for:

- Halt the Panic.
- Keep Essential Industry Running.
- Put the Depression Centers Back to Work.
- Hold the Social Peace.
- Prove the Stabilization.
- Prove the Recovery.
- Emergency National Stabilization.

Mission art should read as an objective, deadline, or operation. It must not be a resized decision icon.

## Idea and modifier icon family

Inspect the final idea and dynamic-modifier structure before creating art. Produce only accepted visible carriers.

Expected visual roles:

- Opening Panic.
- Sustained Depression.
- Economic Paralysis.
- Fragile Recovery.
- Economic Contagion.
- Worldwide Pressure.
- Relief-led legacy.
- Finance-led legacy.
- Strategic-industry legacy.
- State-directed legacy.
- Retrenchment or consolidation legacy.
- Hollow recovery scar.

Use shared visual language without copying one source image into several consumers. Each final visible idea needs distinct readable art.

## State-modifier icon family

Create separate state-modifier icons for:

- Shocked Industrial Center.
- Idled Plants.
- Shuttered Center.
- Protected Center.
- Public Works Zone.
- Reopening Center.
- Abandoned Works.
- Hollowed Industrial District.

The status should be recognizable through machine state, gate state, worker activity, or construction state. Do not rely only on color.

## Evolution icons

### Financial Contagion

- Several linked industrial or payment nodes with one failing connection.
- No world map.
- No medical-virus symbol as the primary subject.

### Social Collapse

- Factory gate, crowd, broken institutional seal, or split industrial and political authority.
- Serious, readable, and free of caricature.

### The Second Great Depression

- Several idle industrial systems or a large stopped freight and factory motif.
- Global scale communicated through breadth of industry, not cartography.

## Severity, trend, and threshold visuals

The ordinary decision interface may need:

- Severity fill or meter strip.
- Threshold ticks.
- Improving and worsening trend icons.
- Maximum-Severity frame.
- Fragile-recovery frame.

These are UI presentation assets and can use clean graphic design when the inspected consumer requires it. They must still follow the existing HOI4 UI palette and framing. Do not create fake buttons or controls inside a category picture.

Color is insufficient on its own. Use arrow direction, fill pattern, frame damage, and labels through localisation.

## Evolution III super-event image

Follow the separate super-event prompt.

Core image direction:

- Period-authentic global industrial shutdown.
- One strong scene or a restrained documentary composition.
- Idle port cranes, freight lines, machine halls, factory gates, and work lines.
- Several national settings may be implied through people and infrastructure, but avoid a busy collage.
- No map, chart, readable headline, modern city, or fantasy spectacle.

Final asset requires source, processed preview, DDS, sprite handoff, provenance, and review evidence.

## Achievement triplets

Create unique achievement art for every final Event 35 achievement ID:

- Back to Work contract.
- Every Center Reopened contract.
- Containment Line contract.
- The Social Peace contract.
- Lean but Standing contract.
- Recovery of Nations contract.

Each requires:

- Eligible DDS.
- Grey DDS.
- Not-eligible DDS.
- Full achievement ID as filename.
- Root placement under `gfx/achievements/` unless current engine inspection proves another rule.
- Final manifest row and icon review.

Do not derive every achievement from one factory icon through recolor.

## Generated-art rules

For full-canvas period scenes:

- Use 1930s to 1940s photographic technology or period press illustration.
- Preserve one coherent subject, camera, and light direction.
- Avoid modern cinematic framing and color grading.
- Keep all clothing, machinery, vehicles, signs, and architecture period fit.
- Do not request readable text.
- Reject malformed hands, machinery, rails, factory geometry, and crowd faces when they are prominent.

For alpha-backed icons:

- Request native transparency in the first ImageGen call.
- Preserve source PNG with alpha.
- Reject fake checkerboards, white halos, matte pixels, opaque square backgrounds, and internal alpha holes.
- Use background removal only after native transparency fails and record the fallback.

## Processing and DDS

For every asset:

1. Preserve source.
2. Record prompt or source URL.
3. Create processed PNG at exact target canvas.
4. Check crop, alignment, alpha, and final-size readability.
5. Convert through the repository-approved DDS workflow.
6. Verify DDS dimensions and alpha behavior.
7. Create contact-sheet evidence for icon families.
8. Record final path and proposed sprite.
9. Hand off to parent for non-portrait `.gfx` and gameplay wiring.

Do not leave runtime assets under `docs/assets/`.

## Naming and placement

Use lowercase snake_case and event-scoped folders where the engine surface permits them.

Expected folder form:

`035_great_depression`

Examples:

- `gfx/event_pictures/035_great_depression/`
- `gfx/interface/decisions/035_great_depression/`
- `gfx/interface/ideas/035_great_depression/`
- `gfx/interface/state_modifiers/035_great_depression/`

Achievement files remain directly under the achievement root and use the full achievement ID.

Final paths and sprite identifiers must be locked before production where possible.

## Required handoff

Return:

- Asset inventory with status.
- Source mode and rights.
- Prompt or source link.
- Source and final checksums.
- Native dimensions and final dimensions.
- Final PNG and DDS paths.
- Sprite name.
- Consumer.
- Contact-sheet path.
- Alpha review.
- Final-size review.
- Any rejected candidates and reasons.
- Any blocker.

Do not claim the event asset package complete while a required report, category, action, mission, state, evolution, achievement, or super-event asset is missing or unwired.
