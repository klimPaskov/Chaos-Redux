# Super-event research and production prompt: Event 011 Secret Alliance

Status: fulfilled historical implementation prompt. The final title, five route descriptions, quote, remark, image, audio, and presentation lifetime are implemented and documented in `docs/super_events/011_secret_alliance_super_event_research.md`.

Research and prepare the full super-event package for the first public reveal of the anti-target pact. Read the event specs, `research/011_secret_alliance_super_event_text_research.md`, and the project super-event skill before work.

## Role

This is a reveal and faction-formation super-event. It marks the moment when several previously separate governments publicly become one faction against the target. It is not a world-end event.

Possible reveal routes include:

- one active member enters a normal hostile war against the target and activates the pact
- the pact publicly declares itself at Evolution III
- the target forces exposure through a public dossier or captured conference
- a fractured subset reveals after doubtful members withdraw

The presentation may vary its description by route, but it should use one stable super-event slot and one unique audio package.

## Text research

Review the researched candidates rather than inventing a quote.

Preferred main quote candidate:

- “All warfare is based on deception.”
- Sun Tzu, *The Art of War*, Lionel Giles translation
- Verify exact wording against Project Gutenberg and document the translation

Preferred button remark candidate:

- “Look about you.”
- Short fragment from Artemidorus's warning in Shakespeare's *Julius Caesar*, Act II, Scene III
- Document it as a fragment

Backups include the researched Shakespeare, Psalm 83, and Thucydides candidates. Confirm attribution, rights status, and UI fit before selection.

This prompt originally left the title open. The implemented title is `THE PACT UNMASKED`; the historical direction below does not reopen that choice.

Write the final description as original in-world prose. It should mention the public faction, its leader, its membership scale, and the immediate strategic change. It must not explain internal variables or list every earlier incident.

## Image coordination

Coordinate with the generated event-art package for:

- `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds`
- proposed sprite `GFX_super_event_011_secret_alliance_public_reveal`

The image is a generated alternate-history documentary scene with several delegations and military representatives making a formal common commitment. It should not use fixed participant flags or readable generated text.

## Audio research

Find and compare at least four legally usable music candidates.

Required shape:

- real music
- 75 to 115 seconds after editing
- controlled tense opening
- formal, martial, or ceremonial middle
- appropriate to a public alliance reveal
- no supernatural horror tone
- no modern trailer percussion
- no pure drone, stinger, test tone, generated oscillator, or noise bed

Verify composition rights and recording rights separately. Prefer public-domain recordings, Creative Commons recordings that permit mod redistribution and editing, official archives with clear rights, or other clearly licensed sources.

For every candidate, document:

- title
- composer
- performer or recording source
- source URL
- license
- license confidence
- duration
- attribution requirement
- why it fits
- proposed trim and fade
- rejection reason if not selected

Preserve the selected source download under the event's documentation asset archive. Convert the final track to 44.1 kHz OGG. Use an event-scoped path:

`music/011_secret_alliance/super_event_<slot>_public_reveal.ogg`

Propose a unique audio ID and sound wrapper. Do not reuse another super-event track.

## Required outputs

Create or update:

- `docs/super_events/011_secret_alliance_super_event_research.md`
- selected and backup quote notes
- final title, description, button remark, and quote package
- audio candidate table
- selected source audio and final OGG
- license and attribution notes
- image handoff reference
- proposed super-event slot and unique audio ID
- implementation wiring handoff for the main agent

Do not edit event, localisation, GFX, GUI, sound definition, or spreadsheet files. The main agent owns final wiring.

## Completion gate

Do not call the super-event package ready if the final audio source, license, recording rights, unique track, final OGG, selected quote, title, description, button text, image handoff, or implementation identifiers remain unresolved. Report any blocker directly.
