# Super-event prompt for Event 011 Secret Alliance

Use `chaos-redux-super-events`, `chaosx_super_event_text_researcher`, `chaosx_super_event_audio_researcher`, and `chaos-redux-event-assets` for this research package. Do not edit localisation, event script, GFX, GUI, sound definitions, or spreadsheet files.

## Super-event role

The super-event marks the public reveal of the hidden pact when the compact becomes the visible `Anti-[target country] Pact` faction. It should fire only when the reveal has campaign weight, such as:

- A major patron is involved.
- The pact has grown beyond the founders.
- The reveal is caused by war and multiple members join.
- Evolution III reaches the public compact stage.

A small evidence reveal against only three weak minors can use normal report or news treatment instead.

## Presentation direction

- Role: reveal and public faction formation.
- Tone: cold diplomatic menace, coordinated betrayal, sudden clarity after a long pattern.
- Player feeling: the player finally sees the system that has been touching their rails, factories, embassies, and borders.
- Information shown: the pact is real, its public structure now exists, and member countries have chosen open opposition.
- Information withheld: exact hidden thresholds, unrevealed pre-history, and future war timing unless the war has already started.

## Research gates

Do not write final title text, button text, quote text, lyric fragments, slogans, or cultural references without research and source documentation.

Required research outputs:

- Title recommendation with source-free direction or a sourced historical or literary allusion if used.
- Main quote from a real source, verified and attributed.
- Button remark or short cultural reference, verified if source-dependent.
- Audio candidate with license, creator, source, duration, and final `.ogg` handoff.
- Backup quote and remark options.
- Source confidence and copyright notes.

## Quote direction

Find quotes about conspiracy becoming public, hidden enemies, alliances formed through fear, secret counsel, or the danger of false security. Prefer public domain literature, political writing, diplomatic memoirs, speeches, or philosophy. Avoid invented quote-site material.

## Button remark direction

The button should be short and cold. It can use diplomatic understatement, bitter irony, or a brief public-domain literary allusion. Avoid cheap comedy because this reveal can follow sabotage, assassination, and war.

## Image direction

Coordinate with the asset prompt for a generated super-event image:

- 457x328.
- Fictional period diplomatic hall or conference room.
- Several delegations visible, faces partly obscured.
- A central treaty table or map surface without readable text.
- The target country should be implied by composition or lighting, not named in generated text.
- No modern props, modern flags, readable signatures, or real leaders.

## Audio direction

Find a real licensed or public domain track with a restrained diplomatic crisis mood. The track should feel ominous and controlled rather than apocalyptic. Prefer one to two minutes after trimming. Document title, creator, performer or recording source, URL, license, source file, final `.ogg`, suggested audio ID, and use.

## Suggested internal keys

Working labels, not final localisation:

- Super-event role key: `secret_alliance_public_reveal`.
- Suggested audio ID pattern: `chaosx_super_event_secret_alliance_reveal`.
- Suggested image sprite: `GFX_super_event_secret_alliance_reveal`.

Implementation must wire the final researched package through the existing settings-aware super-event playback pattern.
