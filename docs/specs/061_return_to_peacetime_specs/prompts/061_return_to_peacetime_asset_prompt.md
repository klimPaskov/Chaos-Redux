# Asset production prompt: Event 061 Return to Peacetime

Produce the complete final visual asset package defined in the Event 61 specification.

Read Part 6, the asset requirements handoff, the event-asset skill, the generated-art subagent definition, and the icon-artist subagent definition before work.

Inspect the exact installed vanilla references and current Chaos Redux consumer files before locking dimensions, crop, alpha, format, path, or sprite name.

Do not use primitive placeholders, copied unrelated mod art, generated readable text, or silent generic icon duplication.

## Source mode

Use generated fictional global scenes for:

- baseline report image
- Swords into Ploughshares report image
- Great Demobilization report image
- Permanent Peace report image
- Return to Rearmament category picture

Use generated icon art for:

- category icon
- decision icons
- mission icons when the consumer requires separate art
- national-spirit icons
- law icons
- achievement icons

The subjects are anonymous and fictional.

Do not depict a named real person.

Do not use a national flag or identifiable political emblem as the central subject.

## Report image family

Create four distinct report images using the verified report-event canvas and final `210x176` target when local precedent confirms it.

### Baseline

Show a 1930s to 1940s factory line being retooled from artillery, military vehicles, or ammunition work toward civilian machinery or transport production.

Workers should remove military tooling while returning service personnel appear as secondary figures.

Keep one coherent scene.

Avoid split-screen collage, readable signs, flags, modern safety equipment, and modern machinery.

### Swords into Ploughshares

Show a large military depot where rifles, vehicle parts, crates, and machine tools are being sorted, dismantled, or redirected into reconstruction.

Do not show a theatrical bonfire of weapons.

### The Great Demobilization

Show a demobilization center or railway platform with soldiers returning equipment, receiving papers, and preparing for civilian travel.

Keep the tone serious and human.

### Permanent Peace

Show closed arsenal gates and quiet barracks with civilian building work beyond them.

The scene should communicate both civilian recovery and strategic vulnerability.

Do not use ruined-world or apocalypse imagery.

## Category picture

Create one static category picture using the exact installed reference dimensions.

Show a factory floor divided by purpose, with military tooling on one side and civilian production on the other.

Use machine tools, procurement files, and freight as supporting details.

Do not paint buttons, progress bars, numbers, or fake interface controls.

## Icon family

Use one coherent visual family with strong silhouettes, period materials, and readable small-size contrast.

Create distinct icons for:

- Return to Rearmament category
- arms contracts
- state arsenal reopening
- General Staff
- public defence campaign
- economy-law restoration
- conscription restoration
- emergency rearmament
- permanent civilian conversion
- Defence Ministry
- National Arsenal
- Service Registry
- emergency national defence
- Army Stores protection
- mobile and armoured reserve protection
- Air Reserves protection
- Logistics Reserves protection
- Central Reconstruction
- Civilian Auctions
- essential cadres
- border formations
- accelerated mustering out
- national defence settlement
- voluntary Permanent Peace
- extreme-law recovery
- Industrial Reconversion Shock
- Reconstruction Materials
- Veteran Reintegration
- Peace Dividend
- Improvised Rearmament
- Peacetime Economy
- No Army

Do not reuse one icon for different concepts merely by changing the file name.

## Achievement icons

Create three distinct achievement icons:

1. closed arsenal doors forced open around a growing gear and rifle silhouette
2. one plough blade reshaped into a bayonet around a factory gear
3. a padlocked arsenal beneath a laurel with idle smokestacks and a distant border marker

No text.

Review at actual achievement size.

## Technical requirements

For every asset:

- preserve the untouched generated source
- record prompt and source mode
- process to exact consumer dimensions
- maintain correct alpha rules
- create PNG preview
- convert to DDS through the repository workflow
- use stable lowercase snake_case file names
- document final DDS path and proposed sprite name
- validate crop and readability at actual in-game size
- add manifest row
- provide GFX handoff to the main implementation agent

The main implementation agent owns final `.gfx`, event, decision, idea, law, and achievement wiring.

## Quality checks

Reject:

- unreadable generated text
- modern clothing or equipment
- wrong aspect ratio
- faces that become the central named identity
- clipped subjects
- white halos
- checkerboard remnants
- transparent holes
- opaque square backgrounds where transparency is required
- primitive geometry as final art
- a category picture that imitates buttons or meters
- duplicate icon silhouettes across unrelated actions
- report images that look like a collage
- report images that rely on flags for meaning

## Handoff

Write event-scoped handoff files under:

`docs/plans/061_return_to_peacetime_plans/subagent_handoffs/`

Include:

- asset identifier
- consumer
- source mode
- source path
- prompt record
- dimensions
- processed PNG path
- final DDS path
- proposed sprite name
- reference inspected
- review result
- blocker or final status

Do not mark the package final until every required consumer has a valid asset and local in-game validation confirms the crop and wiring.
