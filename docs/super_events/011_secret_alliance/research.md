# Event 011 Secret Alliance super-event research

This note records the authoritative implementation package for the first public reveal of Event 011 `Secret Alliance`. Engine-compatible gameplay is frozen at `407b9a05eb7024dd1728c4092fba2f1162efde9c`, while balance and presentation state remain frozen at `1c87d9235319781c871c2948813ab55693eb8618`; Event 011 localisation has SHA-256 prefix `6A42CEFE`. The parser correction does not alter the verified quote, button fragment, five route packages, image, audio, or presentation lifetime.

## Research status

- Text package: complete and implemented
- Quote wording and attribution: verified against a public-domain primary-text edition
- Button fragment: verified against a public-domain primary-text edition
- Audio research and final files: complete
- Display slot: implemented as `73`
- Unique audio ID: implemented as `43`
- Image direction and identifiers: final
- Final super-event image: complete and wired
- Gameplay, localisation, GFX, and sound-definition wiring: complete
- Canonical HTML audio catalogue row: parent-owned

The source specification governs the selection. The older plan that chose Luke 8:17 and `In battalions.` is a superseded candidate package.

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
super_event_73_desc_hostile_war: "One member's war has pulled the hidden pact into daylight. [secret_alliance_presentation_leader.GetNameDefCap] has called [?secret_alliance_presentation_target.secret_alliance_reveal_member_count_snapshot|0] governments into [GetSecretAlliancePresentationFactionName] against [secret_alliance_presentation_target.GetNameDef]. Liaison officers are crossing borders and supply trains are following routes arranged months ago. The scattered attacks were the opening work of one campaign."
super_event_73_desc_pact_controlled: "Delegates have taken their seats beside [secret_alliance_presentation_leader.GetNameDef] and named [GetSecretAlliancePresentationFactionName] as their common front against [secret_alliance_presentation_target.GetNameDef]. All [?secret_alliance_presentation_target.secret_alliance_reveal_member_count_snapshot|0] governments have signed, opened liaison offices, and handed their first military moves to a common command."
super_event_73_desc_player_forced: "A dossier released by [secret_alliance_presentation_target.GetNameDef] has named the governments working against it. [secret_alliance_presentation_leader.GetNameDefCap] has kept [?secret_alliance_presentation_target.secret_alliance_reveal_member_count_snapshot|0] members together as [GetSecretAlliancePresentationFactionName]. They enter public view with exposed couriers, watched routes, and promises several capitals may regret making."
super_event_73_desc_fractured: "[?secret_alliance_presentation_target.secret_alliance_reveal_member_count_snapshot|0] governments walked into the same conference under [secret_alliance_presentation_leader.GetNameDef] and declared [GetSecretAlliancePresentationFactionName] against [secret_alliance_presentation_target.GetNameDef]. One delegation is threatening to leave, two have delayed their signatures, and staff officers are still waiting for orders their capitals refuse to sign. Some chairs may be empty by the time the first joint order arrives."
super_event_73_desc_weakened: "[secret_alliance_presentation_leader.GetNameDefCap] has brought [?secret_alliance_presentation_target.secret_alliance_reveal_member_count_snapshot|0] governments before the cameras as [GetSecretAlliancePresentationFactionName]. Their staff officers are already redrawing routes spoiled by raids and defensive preparations inside [secret_alliance_presentation_target.GetNameDef]. The public declaration has begun with the coalition trying to repair its first move."
```

## Reveal-route mapping

| Description key | Reveal-route constants |
| --- | --- |
| `super_event_73_desc_hostile_war` | `secret_alliance_reveal_route.hostile_war` |
| `super_event_73_desc_pact_controlled` | `secret_alliance_reveal_route.public_conference` |
| `super_event_73_desc_player_forced` | `secret_alliance_reveal_route.public_dossier`, `captured_conference`, and `preemption` |
| `super_event_73_desc_fractured` | `secret_alliance_reveal_route.fractured` |
| `super_event_73_desc_weakened` | `secret_alliance_reveal_route.weakened` |

No generic route fallback is approved. Every current reveal-route value is mapped. The controlled package is selected only for a strong and ready pact facing lower target Preparedness. The player-forced package covers coalition-case Evidence or an exposed sponsor. The fractured package covers low Cohesion, a recent dispute, or a preserved turned channel. The weakened package is the remaining public-conference outcome after the state checks and applies the matching Cohesion and Readiness losses before conversion.

## Dynamic localisation inputs

- presentation target `secret_alliance_presentation_target`
- presentation leader `secret_alliance_presentation_leader`
- stable presentation faction helper `[GetSecretAlliancePresentationFactionName]`
- reveal count `[?secret_alliance_presentation_target.secret_alliance_reveal_member_count_snapshot|0]`

The event-target prefix is omitted inside localisation. The count uses integer formatting and reads the durable reveal-time member count on the presentation target. `GetSecretAlliancePresentationFactionName` resolves the country-name or adjective-name form from the copied grammar flag rather than reading a faction that settlement may already have renamed or dismantled.

## Presentation lifetime

`secret_alliance_fire_reveal_super_event` copies the route, target, leader, member count, and faction-name grammar before it opens slot `73`. The slot and audio remain active for 14 days. Hidden event `chaosx.nr11.202` runs on day 15 and clears the slot, audio ID, route snapshot, presentation targets, and grammar flag. Country lifecycle handling closes the same context early if either presentation country ceases to exist. Automatic and scenario relaunch gates require counted `.50` delayed-call callbacks, counted `.51` through `.53` commitment callbacks, this presentation callback context, the `.190` war-pulse callback, and the `.201` scenario notice callback to drain before a new run starts. Annexation releases the counted delayed-call slot owned by the annexed country.

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
- composition status public domain, separately documented in the audio handoff and Wikimedia Commons rights record
- recording status public-domain United States federal-government performance, independently identified by the official Marine Band catalogue
- audio ID `43`
- final duration `86.101746` seconds
- preserved source `docs/assets/011_secret_alliance/source_audio/revelation_us_marine_band_commons_source.ogg`
- runtime WAV `sound/011_secret_alliance/super_event_43_public_reveal.wav`
- sound ID `chaosx_super_event_secret_alliance_public_reveal_track`
- sound registration `sound/chaosx_sound.asset`
- dispatcher state `global.current_super_event_audio_id`
- canonical HTML audio catalogue `music/chaosx_music_track_list.html` remains parent-owned
- detailed handoff `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_audio_research.md`

The cue has a formal martial shape and remains tag-neutral. It supports a dangerous public coalition without implying a terminal scenario. The settings-aware sound helper controls its runtime playback.

## Image package

- final DDS `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds`
- sprite `GFX_super_event_011_secret_alliance_public_reveal`
- source mode generated alternate-history documentary art
- central subject public delegations and military representatives accepting one common commitment
- no fixed participant flags or readable generated text

The final generated documentary image is registered in `interface/chaosx_super_events.gfx`, selected in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, and listed in the final Event 011 asset register.

## UI fit

The title and remark are short. The quote uses one line plus attribution. Each description uses one compact paragraph in the active `320 x 370` description box. Dynamic long-form country names remain the presentation edge case, while the stable helper prevents live faction teardown from changing the displayed faction identity. No generic text or wiring fallback is used.

## Implementation handoff

The historical selector plan, source comparison, and wiring checklist are in:

`docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_text_research.md`

That handoff's old image and wiring blockers are superseded by the final implementation package. No quote, remark, title, audio, image, or route-text fallback was used. The settings-aware sound variants, audio ID table, image selector, explicit fractured and weakened route descriptions, durable 14-day presentation context, day-15 cleanup, reveal effect, and audio catalogue row are fully wired. The holistic verdict is owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; this super-event record does not replace it.
