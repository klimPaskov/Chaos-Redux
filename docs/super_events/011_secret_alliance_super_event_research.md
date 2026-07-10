# Event 011 Secret Alliance super-event research

This note records the authoritative implementation package for the first public reveal of Event 011 `Secret Alliance`.

## Research status

- Text package: complete and implementation-ready
- Quote wording and attribution: verified against a public-domain primary-text edition
- Button fragment: verified against a public-domain primary-text edition
- Audio research and final files: complete
- Display slot: implemented as `73`
- Unique audio ID: implemented as `43`
- Image direction and identifiers: final
- Final super-event image: complete and wired
- Gameplay, localisation, GFX, audio-definition, and music-table wiring: complete

The source specification governs the selection. The older plan that chose Luke 8:17 and `In battalions.` is superseded.

## Final text package

| Surface | Final text |
| --- | --- |
| Title | `THE PACT UNMASKED` |
| Quote | `All warfare is based on deception.` |
| Attribution | `Sun Tzu, The Art of War, trans. Lionel Giles` |
| Button remark | `Look about you.` |

The final punctuation is locked to the implemented localisation. The quote retains its terminal period inside the closing quotation mark. The attribution has no leading or trailing dash. The button fragment is capitalized as `Look` and ends with a period.

Implemented localisation:

```yaml
chaosx_super_event.73.t: "THE PACT UNMASKED"
chaosx_super_event.73.q: "\"All warfare is based on deception.\"\n§YSun Tzu, The Art of War, trans. Lionel Giles§!"
chaosx_super_event.73.a: "Look about you."
chaosx_super_event.73.d: "[This.GetSecretAllianceSuperEventDescription]"
super_event_73_desc_hostile_war: "The entry of one pact government into open war has activated commitments prepared in secret. [secret_alliance_leader.GetNameDefCap] has called [?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0] governments into [secret_alliance_leader.GetFactionName] against [secret_alliance_target.GetNameDef]. Military missions, supply agreements, and earlier disturbances now serve one campaign."
super_event_73_desc_pact_controlled: "At a public conference, [secret_alliance_leader.GetNameDefCap] has announced [secret_alliance_leader.GetFactionName] as a common front against [secret_alliance_target.GetNameDef]. [?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0] governments have signed the declaration, opened military liaison offices, and placed their preparations under a single command. The coalition's offensive timetable has entered public view."
super_event_73_desc_player_forced: "Evidence released by [secret_alliance_target.GetNameDef] has exposed the governments coordinating against it. [secret_alliance_leader.GetNameDefCap] has held [?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0] members together under the name [secret_alliance_leader.GetFactionName]. The exposed coalition has compromised routes, known contacts, and contested commitments that leave its first military plans open to interference."
super_event_73_desc_fractured: "After several withdrawals, [?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0] governments have joined [secret_alliance_leader.GetNameDef] in [secret_alliance_leader.GetFactionName] against [secret_alliance_target.GetNameDef]. Empty chairs and unsigned commitments mark the public conference. The remaining delegations have opened military liaison offices and begun a common timetable for joint operations."
```

## Reveal-route mapping

| Description key | Reveal-route constants |
| --- | --- |
| `super_event_73_desc_hostile_war` | `secret_alliance_reveal_route.hostile_war` |
| `super_event_73_desc_pact_controlled` | `secret_alliance_reveal_route.public_conference` |
| `super_event_73_desc_player_forced` | `secret_alliance_reveal_route.public_dossier`, `captured_conference`, and `preemption` |
| `super_event_73_desc_fractured` | `secret_alliance_reveal_route.fractured` |

No generic route fallback is approved. Every current reveal-route value is mapped.

## Dynamic localisation inputs

- fixed target `secret_alliance_target`
- public faction leader `secret_alliance_leader`
- actual public faction name `[secret_alliance_leader.GetFactionName]`
- reveal count `[?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0]`

The event-target prefix is omitted inside localisation. The count uses integer formatting and reads the durable reveal snapshot on the fixed target. The snapshot must be created before the super-event is shown.

## Quote source and rights

Project Gutenberg prints Chapter I, item 18 of Lionel Giles's 1910 translation exactly as:

> All warfare is based on deception.

Sources:

- primary text <https://www.gutenberg.org/files/132/132-h/132-h.htm>
- catalogue metadata <https://www.gutenberg.org/ebooks/132>
- Project Gutenberg licence <https://www.gutenberg.org/policy/license.html>

The catalogue identifies Lionel Giles as translator and marks eBook 132 public domain in the United States. Project Gutenberg requires users outside the United States to check local law. The player-facing line is a six-word excerpt, and the documentation preserves the exact translator attribution.

## Button source and rights

Artemidorus's warning in *Julius Caesar*, Act II, Scene III reads:

> If thou be’st not immortal, look about you: security gives way to conspiracy.

Sources:

- primary text <https://www.gutenberg.org/cache/epub/1522/pg1522-images.html>
- catalogue metadata <https://www.gutenberg.org/ebooks/1522>
- Project Gutenberg licence <https://www.gutenberg.org/policy/license.html>

The button uses the exact lexical fragment `look about you` with standalone capitalization and a period. It is documented as a fragment. Project Gutenberg marks eBook 1522 public domain in the United States, and the underlying Shakespeare play is public-domain literature.

## Audio package

- selected work `Revelation`
- composer William Paris Chambers
- composition year 1901
- performer United States Marine Band
- director Col. John R. Bourgeois
- recording source *Sound Off!*, 1992
- source and recording rights public domain as documented in the audio handoff
- audio ID `43`
- final duration `86.101746` seconds
- final OGG `music/011_secret_alliance/super_event_43_public_reveal.ogg`
- sound mirror `sound/011_secret_alliance/super_event_43_public_reveal.wav`
- sound ID `chaosx_super_event_secret_alliance_public_reveal_track`
- music catalogue `music/chaosx_music_track_list.html`
- catalogue row `The Pact Unmasked`, audio ID `43`, `Revelation`, United States Marine Band, duration `01:26`, public-domain composition and federal-government recording
- detailed handoff `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_audio_research.md`

The cue has a formal martial shape and remains tag-neutral. It supports a dangerous public coalition without implying a terminal scenario.

## Image package

- final DDS `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds`
- sprite `GFX_super_event_011_secret_alliance_public_reveal`
- source mode generated alternate-history documentary art
- central subject public delegations and military representatives accepting one common commitment
- no fixed participant flags or readable generated text

The final generated documentary image is registered in `interface/chaosx_super_events.gfx`, selected in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, and listed in the final Event 011 asset register.

## UI fit

The title and remark are short. The quote uses one line plus attribution. Each description uses one paragraph and three complete sentences in the active `320 x 370` description box. Dynamic long-form country and faction names remain the presentation edge case. No text or wiring fallback is used for them.

## Implementation handoff

The full selector logic, exact localisation contract, source comparison, and wiring checklist are in:

`docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_text_research.md`

No quote, remark, title, audio, image, or route-text fallback was used. The settings-aware music and sound variants, audio ID table, image selector, explicit fractured-route description, reveal effect, and music catalogue row are fully wired.
