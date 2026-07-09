# 020 Black Plague asset prompt

Use `chaos-redux-event-assets` and the relevant asset subagents. Use `chaos-redux-frame-animation` for every animated element. Inspect the matching reference folders before creating, sourcing, processing, converting, or handing off art.

This prompt is for Event 020 Black Plague. All labels are working labels only, not final localisation.

## Source mode rules

Generated fictional art is appropriate for Black Death report scenes, rat countries, rat flags, rat portraits, rat focus icons, rat achievement icons, rat UI pieces, disease-board visual states, and world-end imagery. Use sourced images only when the implementation requires a real historical photograph, real leader, real flag, real symbol, or real archival artifact. Do not generate real leaders or real historical flags.

Every final asset needs a source file, processed PNG preview, final DDS or TGA where required, manifest entry, and `gfx_handoff.md` entry when a sprite definition is needed.

## Reference folders to inspect

Use the matching reference folder before work:

- idea and national spirit icons: `.agents/skills/chaos-redux-event-assets/assets/ideas`
- focus icons: `.agents/skills/chaos-redux-event-assets/assets/focuses`
- decision and decision category icons: `.agents/skills/chaos-redux-event-assets/assets/decisions`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/achievements`
- report event images: `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- news event images: `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- super-event images: `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- flags: `.agents/skills/chaos-redux-event-assets/assets/flags`
- tech or special project icons: `.agents/skills/chaos-redux-event-assets/assets/tech_icons` and `.agents/skills/chaos-redux-event-assets/assets/special_projects` if present

## Disease and state visuals

Required assets:

| Asset | Type | Size direction | Source mode | Use |
| --- | --- | --- | --- | --- |
| Black Death disease icon | disease UI or decision icon | existing shared disease UI size | generated | identifies the disease in the shared board |
| infected state status icon | UI state icon | UI-specific | generated | infected selected state and list rows |
| contained state status icon | UI state icon | UI-specific | generated | contained state status |
| recovery residue marker | UI state icon | UI-specific | generated | recovering or relapse-risk state |
| cured state marker | UI state icon | UI-specific | generated | cured or monitored state |
| weaponized-hit marker | UI or map marker | UI-specific | generated | recent Black Death payload exposure |
| port-risk marker | UI or map marker | UI-specific | generated | Evolution II maritime threat |
| rat-held state marker | UI or map marker | UI-specific | generated | state held by nonhuman rat country |
| black fog overlay | mapmode or GUI marker | engine-dependent | generated or scripted visual | infected and severe state presentation |

The black fog requirement may become engine-dependent during implementation. If a true map fog overlay cannot be supported, create the closest approved state-disease presentation with static and animated UI fallbacks, then report the limitation clearly.

## Shared disease-board UI assets

Required or recommended assets:

| Asset | Animation need | Use |
| --- | --- | --- |
| shared disease board header plate | static | disease-board identity within the existing shared category |
| Black Death seal | animated recommended | board state, not a duplicate category |
| selected state disease load meter | static variants or animation | severity and death pressure |
| cure progress meter | static variants or animation | treatment, suppression, cleanup unlock |
| spread route panel icons | static | border, port, troop, refugee, weapon, and rat spread routes |
| active mission warning frame | animated if useful | severe outbreak and rat-border missions |
| rat warning mark | animated recommended after public reveal | warren pressure and rat-held border states |
| state card background variants | static | clean, prepared, threatened, infected, contained, recovering, cured, weaponized, rat-held |

Animated UI assets require real source frames. Do not create final animation from a shifted, recolored, blurred, or opacity-only still image.

## Decision, mission, and special project icons

Decision icons must be 32x32 and designed for that size. They must not be resized focus icons.

Required icon families:

| Family | Icons |
| --- | --- |
| preparedness | surveillance, medical stockpile, emergency health law, early warning |
| threatened state | border control, port inspection, refugee corridor, troop-route restriction |
| infected state | quarantine, lockdown, field hospital, army cordon, treatment surge, vector control |
| contained state | maintain cordon, monitor relapse, controlled reopening |
| recovery state | cleanup crews, safe reopening, population recovery support |
| cure research | sample sharing, national cure effort, treatment deployment, medical production |
| weaponized exposure | sealed exposure marker, accident response, evidence handling, retaliation warning |
| anti-rat | rat border cordon, nest assault, evacuation, fortification, cleanup burn, warren watch |
| international coordination | medical aid, containment coalition, research sharing, port inspection compact |
| special projects | Black Death study, safety protocols, countermeasure project, payload project, accident response |

Avoid real-world lab imagery for weaponization icons. Use abstract sealed-sample, warning, safety, and strategic project motifs.

## Focus icon families

Focus icons use 94x86 and require focus-specific generation or sourcing. Do not derive them from decision icons or idea icons.

Base rat focus icon families:

- awakening warren: nest, tunnel mouth, first swarm, broken floorboards
- swarm growth: brood chamber, mass rats, corpse-fed movement, hidden reserves
- plague ecology: black fog, grain stores, port vermin, sick roads
- human war: wire line, night attack, supply sabotage, tunnel breach
- warren defense: burrow fort, ruins, hidden litters, plague moat
- absorption: two nests merging, tooth-right motif, inherited brood
- King preparation: crown instinct, black court below, all warrens answering

King focus icon families:

- coronation and sentience: rat crown, throne below, first law, speech of teeth
- royal command: crown command, elite guard, command tunnels
- brood council: council nest, many eyes, patient warren
- hunger mind: single appetite, devour roads, endless gnawing
- swarm command: tunnel signal, King guard, continental swarm
- warren economy: scavenged surface, gnawed factories, corpse fields
- plague mastery: black fog nests, cure resistance, harbor warrens
- human terror: empty village, broken hospital, roads run black
- rat unity: no lesser crowns, one underground realm
- continental conquest: plague belt, ports of swarm, continent below
- world-end path: every road a tunnel, crown below continent, rat world threshold

## Idea and national spirit icons

Idea icons use 64x64 and must be separate art from focus icons.

Required icon families:

- Black Death state modifier
- contained infection
- recovery residue
- cured but monitored state
- weaponized exposure
- base warren
- nonhuman swarm
- plague ecology
- burrowed state
- crowned warren
- royal command
- brood council
- hunger mind
- broken crown
- anti-rat doctrine or emergency cordon
- global containment coalition if implemented

## Country flags and portraits

Base rat nations need:

- base flag in normal, medium, and small sizes for every implemented rat tag
- optional dominant-warren cosmetic flag if the route uses it
- leader portrait or institutional portrait, 156x210
- possible route or severity portrait variant if the implementation uses one

The King of Rats needs:

- base King flag in normal, medium, and small sizes
- Royal Command flag variant if route identity changes the flag
- Brood Council flag variant if route identity changes the flag
- Hunger Mind flag variant if route identity changes the flag
- King leader portrait, 156x210
- optional animated portrait overlay or route-state portrait variants
- static fallback for every animated portrait or overlay

Rat flags are fictional and can use generated art. They must remain readable at 82x52, 41x26, and 10x7. Do not create ideology variants by simple recolor unless the implementation accepts identical variants and documents why.

## Unit and warfare icons

Required or recommended icons:

- warren swarm unit family
- sewer rush unit family
- plague gnawer unit family
- burrow guard unit family
- brood mass unit family
- King guard elite family
- anti-rat doctrine
- cordon operation
- nest assault
- burnout cleanup
- port quarantine line
- plague road interdiction

These may be unit icons, idea icons, decision icons, or tech icons depending on implementation surface. Use the correct target size for each surface.

## Report and news images

Report event images are 210x176 and must use the report-event card treatment. News event images are 397x153 and must be black and white.

Report image candidates:

| Moment | Source mode | Direction |
| --- | --- | --- |
| first outbreak state | generated period-documentary | crowded neglected district, sickness, black fog implication, no readable text |
| first severe collapse | generated period-documentary | overwhelmed streets, improvised hospitals, abandoned markets |
| first rat warren | generated fictional documentary | ruined district with nonhuman signs, no King reveal |
| retaken warren cleanup | generated period-documentary | soldiers and medical crews clearing ruins |

News image candidates:

| Moment | Source mode | Direction |
| --- | --- | --- |
| Evolution II overseas spread | generated or sourced-like period news | port quarantine and ships |
| first rat nation public | generated period news | panicked border or ruined town without final text |
| King military breakthrough | generated period news | rat war front, black fog, troops holding or retreating |
| King defeated after major war | generated period news | cleanup and survivors in a reflective tone |

## Super-event images

Required packages:

- King reveal image, 457x328, generated fictional super-event art
- rat world-end image, 457x328, generated fictional super-event art

Conditional packages if implemented:

- continental rat threat escalation image, 457x328
- rat defeat aftermath image, 457x328

Super-event images need strong central composition, no readable text, no modern props, and enough contrast for HOI4 UI.

## Animated asset requirements

Recommended animated assets:

| Asset | Surface | Frame direction |
| --- | --- | --- |
| black fog state card | disease board | 6 to 10 source frames with real fog variation |
| disease board seal | shared disease category or GUI | state-driven variants for calm, threatened, infected, severe, rat threat |
| rat warren warning | UI warning | 6 to 8 source frames, subtle pulse or living nest motion |
| King portrait overlay | leader portrait or scripted GUI | generated frame set with static fallback |
| world-end progress frame | King UI or focus route card | 8 to 12 frames with crown geometry and black fog |

Every animated asset must include source frame PNGs, processed frames, a horizontal sheet PNG, sheet DDS, static fallback PNG and DDS, preview GIF for review, contact sheet, frame count, timing, loop behavior, anchor point, manifest entry, and `gfx_handoff.md` entry.

## Achievement icon suite

Create completed 64x64 achievement icons for every accepted achievement in `prompts/020_black_plague_achievement_prompt.md`. Create grey and not-eligible variants when the achievement system requires them.

Use motifs from the achievement prompt, including clean cordon, fading plague hospital, port shield, defensive study mask, cracked payload shield, wire line and rat shadow, burning warren, broken crown, crown hunter, clean continent, merging warrens, crown below tunnel, three-mind crown motif, continent tunnel, rat world, and humanity returns.

## Manifest and handoff requirements

Every asset entry must record:

- asset name
- event id and slug
- asset type
- intended in-game use
- source mode
- generation prompt or source URL
- source path
- processed PNG path
- final DDS or TGA path
- target size
- sprite name
- target `.gfx` file
- target `.gui` file if known
- related focus, idea, decision, event, country, unit, achievement, or super-event
- animation metadata if animated
- status and uncertainty

For generated one-person portraits, record apparent gender presentation and matching leader-name requirements. For symbolic, council, or nonhuman institutional portraits, mark them as institutional and avoid human personal-name assumptions.
