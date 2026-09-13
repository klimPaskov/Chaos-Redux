# Event 40 Super-Event Research and Implementation Prompt

Create and implement three Evolution III regional-order super-events for Chaos Redux Event 40.

## Required reading

Read in full:

- `AGENTS.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- every Event 40 specification file
- current super-event slot, image, localisation, and sound precedents

Use separate research agents:

- `chaosx_super_event_text_researcher`
- `chaosx_super_event_audio_researcher`
- `chaosx_asset_source_researcher` for archival image material
- `chaosx_generated_event_art` for fictional alternate-history scenes
- `chaosx_portrait_creator` if Lawrence's grounded identity appears prominently

The parent owns final slot, localisation, GFX, sound, event, documentation, and spreadsheet wiring.

## Shared rules

These are regional-order super-events. They do not set `world_end`.

Each package needs:

- unique slot or verified safe slot assignment
- title direction
- description direction
- button-reaction direction
- sourced and verified main quote
- final image
- unique final music track
- unique audio ID
- game-ready WAV under `sound/040_lawrence_of_arabia/`
- base sound and settings-volume wrappers
- `global.current_super_event_audio_id`
- `play_current_super_event_sound = yes`
- scripted localisation and `GetSuperEventImage`
- permanent research note
- row in `music/chaosx_music_track_list.html`
- Event 40 documentation and catalog alignment

Do not use film soundtrack music, film dialogue, actor images, generated test tones, drones, placeholder audio, or invented quotes.

Prefer structured music with a defensible license and a final duration between one and two minutes. Verify composition and recording rights separately.

## Package 1: British Arabia

Working super-event ID:

`040_british_arabia_formed`

Role:

A British-aligned federation, dominion, or protectorate has consolidated the intervention network into one regional state.

Title direction:

- short formal name tied to compact, federation, dominion, or imperial settlement
- avoid generic empire or destiny titles

Description direction:

- delegates, officers, bases, ports, routes, oil agreements, and federal institutions
- local governments remain visible actors
- show the stability promised by the settlement and the limits placed on sovereignty
- do not explain raw effects

Button direction:

- restrained official reaction
- can use short researched imperial or diplomatic allusion
- no triumphalist joke about colonial domination

Quote direction:

Research verified public-domain or historical wording about imperial obligation, promises, tutelage, alliances, or political dependence. Compare several candidates and document attribution confidence.

Image direction:

- federal delegates and military officers under visible British sponsorship
- local political actors remain central
- supporting context can include aircraft, ports, railways, or maps
- formal and uneasy composition
- generated alternate-history scene is preferred when no archival image can depict the fictional settlement

Audio direction:

- licensed or public-domain ceremonial march, orchestral piece, or structured period music
- formal and controlled, without using a British film score

## Package 2: Independent Arab Federation

Working super-event ID:

`040_independent_arab_federation_formed`

Role:

Independent governments have ratified a sovereign federal charter and converted the intervention crisis into a regional state.

Title direction:

- short name tied to congress, charter, federation, or union
- avoid generic freedom slogans

Description direction:

- public congress, ratification, local governments, military and civil institutions, and negotiated member rights
- mention the foreign promises and pressures that the federation has outgrown only through visible political consequences
- do not make Lawrence the center unless his defection was essential

Button direction:

- constitutional, determined, or sober
- research a brief regional political, literary, or historical allusion when appropriate

Quote direction:

Research verified Arab political, constitutional, anti-imperial, or independence sources. Verify translation, author, work, date, and wording. Prefer public-domain or historical sources with a clear citation.

Image direction:

- congress, public charter, proclamation, or gathering led by local governments
- sovereign symbols and member delegations
- no lone Lawrence composition
- generated period-authentic alternate-history scene is expected

Audio direction:

- licensed or public-domain regional, ceremonial, orchestral, or military music
- verify the recording license
- avoid modern commercial recordings without clear permission

## Package 3: Lawrence's Kingdom

Working super-event ID:

`040_lawrences_kingdom_formed`

Role:

A British liaison believed dead has become the central ruler of a rare Arabian monarchy, military federation, or personal union.

Title direction:

- short and specific to the accepted government form
- retain the strange personal character of the outcome
- avoid parody and film-title imitation

Description direction:

- Lawrence's rise, local rulers and officers, the founding settlement, and unresolved legitimacy
- show that local institutions enabled or accepted the arrangement
- do not claim that he created the region alone

Button direction:

- dry, unsettled, or historically allusive
- no cheap joke or film quotation

Quote direction:

Research verified Lawrence writing or another public-domain source on command, ambition, promises, burden, or political responsibility. Do not use a famous line until its wording and attribution are verified. Keep the final excerpt short enough for the UI.

Image direction:

- Lawrence among local rulers, officers, delegates, and institutions
- visible elevation without a lone hero pose
- preserve the approved grounded identity if his face appears
- do not use Peter O'Toole or any actor likeness

Audio direction:

- unique licensed or public-domain structured music
- unusual and ceremonial without copying the film score

## Research notes

Create or update:

`docs/super_events/040_lawrence_of_arabia_super_event_research.md`

For each package record:

- role
- final title direction and implemented title
- quote candidates and selected quote
- exact source and attribution confidence
- button-reference candidates and selected direction
- image mode, source, prompt, and provenance crosswalk
- audio candidates and selected track
- composer, performer, source, license, duration, and usage terms
- conversion steps
- final WAV path
- sound definition and wrapper IDs
- super-event slot and image sprite
- open uncertainty

## Audio file and identifier direction

Use event-scoped filenames:

- `sound/040_lawrence_of_arabia/super_event_040_british_arabia_formed.wav`
- `sound/040_lawrence_of_arabia/super_event_040_independent_arab_federation_formed.wav`
- `sound/040_lawrence_of_arabia/super_event_040_lawrences_kingdom_formed.wav`

Use three unique audio IDs and matching settings-volume wrappers. Follow the current repository naming contract discovered during implementation.

## Trigger rules

Each super-event fires only after its validated federation transaction completes.

- British Arabia package fires for the British-aligned origin.
- Independent Arab Federation package fires for the sovereign origin.
- Lawrence's Kingdom package fires for the personal origin.

A failed or rolled-back transaction fires no super-event.

Only one formation package should fire for one federation creation.

## Completion

Do not call any package complete while image, quote, audio, sound registration, settings-aware playback, documentation, or catalog wording is missing.

Report every blocked source, license uncertainty, placeholder, or omitted component.
