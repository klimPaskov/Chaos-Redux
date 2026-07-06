# Super-event research prompt for 011 Secret Alliance

Use `chaos-redux-super-events`. For quote and cultural remark research, use `chaosx_super_event_text_researcher`. For audio research, use `chaosx_super_event_audio_researcher`. Use `chaosx_generated_event_art` or `chaosx_asset_source_researcher` for the image depending on source mode chosen by the main agent. Spawn project subagents with `fork_context=false` and include this prompt plus the source spec paths.

Event: 011 Secret Alliance
Super-event role: reveal of the public Anti-[player country] Pact
Source spec path: `docs/specs/011_secret_alliance_specs/`
Suggested research note path: `docs/super_events/011_secret_alliance_super_event_research.md`

## Trigger moment

The super-event fires when the hidden pact becomes public enough to form the Anti-[player country] Pact. This can happen through a hard reveal, such as a full signatory going to war with the player, or through the Evolution III public pact transition.

## Tone

The tone should be tense, diplomatic, encircling, and military. The world should feel like several governments have stopped pretending. The super-event should make earlier sabotage and rumours feel connected in hindsight.

Avoid generic apocalypse wording. Avoid comedy. Avoid making the image or text feel like a normal alliance announcement.

## Title direction

Research required. The title should be short, specific, and about a hidden pact becoming public. It must not be a generic phrase like world in flames or final crisis. Do not use an unresearched working label as final localisation.

## Description direction

The description should state that several governments have openly aligned against the player after a period of unexplained incidents and denied contacts. It should not reveal hidden variables or list mechanical effects. It should mention that the pact's public identity is dynamic around the player country.

## Quote direction

Research required. Find a real, verifiable quote about secret treaties, alliances, hidden enemies, encirclement, false peace, betrayal, or diplomacy turning into war. Prefer public domain, historical, diplomatic, philosophical, or literary sources. Verify exact wording, source, author, date, and attribution confidence. Avoid unsourced internet quote pages.

Do not invent a quote. Do not use a quote if attribution is uncertain and a stronger source exists.

## Cultural remark or button direction

Research required. The button should be short, grim, and fitting for a sudden public encirclement. A brief historical, literary, or political allusion can fit if researched. For modern copyrighted material, keep any direct fragment very short or use a paraphrased allusion.

Do not provide final button text until source checks are complete.

## Audio direction

Research required. Find unique music, preferably 1 to 2 minutes or trimmed to that range, with a tense diplomatic or martial character. The final audio must be licensed or public domain, documented, converted to 44.1 kHz OGG, wired through the settings-aware super-event audio helper, and added to the music track documentation.

Reject unclear licenses, YouTube uploads with no license data, generated tones, drones, beeps, primitive oscillator music, and placeholder ambience.

## Image direction

Coordinate with the asset prompt. Preferred image is a generated or sourced reveal composition showing a shadowed conference, sealed pact, or circle of delegations. Maps and folders can be secondary props. Do not use readable generated text. Do not use real flags unless source mode and usage are cleared.

## Required output from research

- selected final title after research, if title research is part of assigned scope
- selected main quote with source and confidence
- selected button remark or cultural reference with source and copyright risk note
- selected audio with title, creator, performer if relevant, source URL, license, duration, and final OGG path
- image direction and final image asset path or handoff
- implementation notes for super-event slot, audio id, and localisation keys
- uncertainties and blockers
