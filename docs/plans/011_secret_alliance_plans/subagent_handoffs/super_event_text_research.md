# Event 011 Secret Alliance super-event text research handoff

## Scope and outcome

This handoff supplies the final implementation-ready text package for the first public reveal of the Event 011 coalition. It covers the stable title, four reveal-route descriptions, selected quote, selected button fragment, exact source notes, dynamic localisation inputs, UI fit, and alignment with the finished audio research.

The super-event is a public revelation and faction-formation moment. It is not a world-end event. No text below uses apocalypse language or exposes a member before the reveal transaction has completed.

## Source-of-truth resolution

The authoritative source package is:

- `docs/specs/011_secret_alliance_specs/research/011_secret_alliance_super_event_text_research.md`
- `docs/specs/011_secret_alliance_specs/prompts/secret_alliance_super_event_prompt.md`
- the reveal contract in specification parts 1, 2, 4, and 5
- the reveal convergence map in `matrices/011_secret_alliance_event_chain_map.md`

The older working plan at `docs/plans/011_secret_alliance_plans/011_secret_alliance_super_event_text_research.md` selected Luke 8:17 and the Hamlet fragment `In battalions.` That choice conflicts with both authoritative source files, which prefer the Sun Tzu and Artemidorus package. Primary-text verification confirmed the authoritative wording. The new martial and ceremonial `Revelation` audio package also supports the military deception quote more closely than the older religious selection.

The older Luke and Hamlet selection is therefore superseded. It remains useful only as rejected-candidate history.

## Final presentation package

| Surface | Final value |
| --- | --- |
| Super-event role | First public reveal and faction formation |
| Reserved display slot | `73` |
| Title | `THE PACT UNMASKED` |
| Button remark | `Look about you.` |
| Main quote | `All warfare is based on deception.` |
| Player-facing attribution | `Sun Tzu, The Art of War, trans. Lionel Giles` |
| Unique audio ID | `43` |
| Audio selection | `Revelation` by William Paris Chambers, United States Marine Band recording |
| Image sprite | `GFX_super_event_011_secret_alliance_public_reveal` |

`THE PACT UNMASKED` is original event wording. It is not presented as a quotation or cultural reference. It fits hostile-war, pact-controlled, player-forced, and fractured reveals without implying that the coalition is terminal or globally dominant.

## Final localisation text

The following strings are ready for the Event 011 localisation file. The route-specific descriptions intentionally use separate keys because the reveal cause materially changes the public scene.

```yaml
chaosx_super_event.73.t: "THE PACT UNMASKED"
chaosx_super_event.73.q: "\"All warfare is based on deception.\"\n§Y-Sun Tzu, The Art of War, trans. Lionel Giles-§!"
chaosx_super_event.73.a: "Look about you."
chaosx_super_event.73.d.hostile_war: "The entry of one pact government into open war has activated commitments prepared in secret. [secret_alliance_leader.GetNameDefCap] has called [?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0] governments into [secret_alliance_leader.GetFactionName] against [secret_alliance_target.GetNameDef]. Military missions, supply agreements, and earlier disturbances now serve one campaign."
chaosx_super_event.73.d.pact_controlled: "At a public conference, [secret_alliance_leader.GetNameDefCap] has announced [secret_alliance_leader.GetFactionName] as a common front against [secret_alliance_target.GetNameDef]. [?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0] governments have signed the declaration, opened military liaison offices, and placed their preparations under a single command. The coalition's offensive timetable has entered public view."
chaosx_super_event.73.d.player_forced: "Evidence released by [secret_alliance_target.GetNameDef] has exposed the governments coordinating against it. [secret_alliance_leader.GetNameDefCap] has held [?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0] members together under the name [secret_alliance_leader.GetFactionName]. The exposed coalition has compromised routes, known contacts, and contested commitments that leave its first military plans open to interference."
chaosx_super_event.73.d.fractured: "After several withdrawals, [?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0] governments have joined [secret_alliance_leader.GetNameDef] in [secret_alliance_leader.GetFactionName] against [secret_alliance_target.GetNameDef]. Empty chairs and unsigned commitments mark the public conference. The remaining delegations have opened military liaison offices and begun a common timetable for joint operations."
```

The player-forced wording covers a public dossier, captured conference, or player preemption. It describes released evidence broadly enough to remain true for each route without claiming a specific document that may not exist.

## Route selector contract

`GetSuperEventDesc` should select the four keys above while slot `73` is visible.

| Player-facing package | Runtime route values |
| --- | --- |
| Hostile war | `constant:secret_alliance_reveal_route.hostile_war` |
| Pact-controlled | `constant:secret_alliance_reveal_route.public_conference` |
| Player-forced | `constant:secret_alliance_reveal_route.public_dossier`, `constant:secret_alliance_reveal_route.captured_conference`, or `constant:secret_alliance_reveal_route.preemption` |
| Fractured | `constant:secret_alliance_reveal_route.fractured` |

Every defined reveal route is covered. No generic description fallback is approved. `global.secret_alliance_reveal_route` must be set before `secret_alliance_fire_reveal_super_event` runs. An unset or unknown route at slot `73` is a validation error.

The manual scenario should use the description matching its actual transaction order. Use hostile-war when the target war exists before the reveal call. Use pact-controlled when the faction is publicly formed before its leader starts the war.

## Dynamic localisation contract

The proposed strings match the active architecture and current implementation draft.

| Information | Localisation expression | Source state |
| --- | --- | --- |
| Fixed target country | `[secret_alliance_target.GetNameDef]` or `[secret_alliance_target.GetNameDefCap]` | Global event target `secret_alliance_target` |
| Public faction leader country | `[secret_alliance_leader.GetNameDef]` or `[secret_alliance_leader.GetNameDefCap]` | Global event target `secret_alliance_leader` |
| Public leader's current faction name | `[secret_alliance_leader.GetFactionName]` | Faction created before the super-event call |
| Public leader character, if later needed | `[secret_alliance_leader.GetLeader]` | Country localisation property on `secret_alliance_leader` |
| Reveal member count | `[?secret_alliance_target.secret_alliance_reveal_member_count_snapshot|0]` | Country-scoped snapshot stored on the fixed target before faction creation and presentation |

Localisation omits the `event_target:` prefix by engine rule. The member count uses `|0` because it is an integer. The final descriptions use the leader country rather than the leader character so a head-of-government name cannot be mistaken for a separate coalition member.

The reveal transaction calculates `global.secret_alliance_reveal_member_count` and copies it into `secret_alliance_reveal_member_count_snapshot` on the fixed target before the faction is created. The text uses the target-scoped snapshot so the displayed count remains tied to this reveal even if later wartime logic changes the live global membership registry.

## Quote verification

### Selected quote

> All warfare is based on deception.

- Attributed author: Sun Tzu, printed as Sun Tzŭ in the cited edition
- Work: *The Art of War*
- Translation: Lionel Giles, 1910
- Location: Chapter I, item 18
- Primary-text source: <https://www.gutenberg.org/files/132/132-h/132-h.htm>
- Catalogue and rights metadata: <https://www.gutenberg.org/ebooks/132>
- Project Gutenberg licence: <https://www.gutenberg.org/policy/license.html>
- Wording confidence: high

Project Gutenberg prints item 18 exactly as `All warfare is based on deception.` The catalogue identifies Lionel Giles as translator, dates the translation to 1910, and marks eBook 132 public domain in the United States.

Project Gutenberg states that users outside the United States must check local law. Lionel Giles lived from 1875 to 1958, so the translation is not automatically public domain in every jurisdiction that uses an author-life-plus-70 term before 2029. The final use is one six-word sentence. This note records the United States public-domain status and the international jurisdiction caveat without making a worldwide legal determination.

The source and attribution are sufficiently verified for the selected package. No quote aggregator or modern retranslation is used.

## Button fragment verification

### Selected remark

> Look about you.

- Author: William Shakespeare
- Speaker: Artemidorus
- Work: *Julius Caesar*
- Location: Act II, Scene III
- Primary-text source: <https://www.gutenberg.org/cache/epub/1522/pg1522-images.html>
- Catalogue and rights metadata: <https://www.gutenberg.org/ebooks/1522>
- Project Gutenberg licence: <https://www.gutenberg.org/policy/license.html>
- Wording confidence: high

The cited text reads `If thou be’st not immortal, look about you:`. The button preserves the exact lexical fragment `look about you`, capitalizes the first word, and replaces the source colon with a period so the fragment can stand alone. It must be documented as a short fragment with adapted standalone punctuation, not as the complete Artemidorus sentence.

Project Gutenberg marks eBook 1522 public domain in the United States. Shakespeare died in 1616, and the underlying play is public-domain literature. The button uses four words from the play and carries no modern editorial commentary.

## UI fit

The active layout in `interface/chaosx_super_events.gui` provides:

- title box `700 x 50` using `hoi_36header`
- description box `320 x 370` using `hoi4_typewriter22`
- quote box `370 x 79` using `hoi_18mbs`
- button text using `hoi_20bs`

Fit decisions:

- `THE PACT UNMASKED` is 17 characters and fits the title box with substantial room.
- `Look about you.` is 15 characters and is appropriate for the existing button.
- The quote is six words. The attribution remains short enough to sit beneath it in the quote box.
- Each route description is one paragraph with three complete sentences. This avoids extra vertical space from paragraph breaks.
- Dynamic country and faction names are the largest width variable. The prose avoids placing two long dynamic names in the same clause except where necessary to identify leader, faction, and target.
- The route descriptions should be visually checked with a long target name and a long faction-leading country name after localisation wiring. If wrapping exceeds the box, shorten surrounding original prose and preserve all three required dynamic facts.

## Audio and image alignment

The audio handoff selected `Revelation`, a 1901 march by William Paris Chambers, performed by the United States Marine Band under Col. John R. Bourgeois for the 1992 album *Sound Off!*.

Implementation identifiers:

- audio ID `43`
- final OGG `music/011_secret_alliance/super_event_43_public_reveal.ogg`
- sound mirror `sound/011_secret_alliance/super_event_43_public_reveal.wav`
- underlying sound ID `chaosx_super_event_secret_alliance_public_reveal_track`
- final duration `86.101746` seconds
- rights status recorded as public-domain composition and U.S. federal-government performance
- audio handoff `docs/plans/011_secret_alliance_plans/subagent_handoffs/super_event_audio_research.md`

The formal march supports the selected title and military deception quote. It does not push the scene toward a religious, supernatural, or terminal reading.

The image remains assigned to the generated alternate-history documentary package:

- final path `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds`
- sprite `GFX_super_event_011_secret_alliance_public_reveal`
- central subject several public delegations and military representatives accepting a common commitment
- no fixed national flags, readable generated text, globe, dossier pile, or arrow-covered map

The final DDS was not present during this text pass. Asset production and `.gfx` wiring remain outside this subagent's scope.

## Main-agent wiring handoff

1. Add the slot `73` image, title, quote, remark, and route-description branches to `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`.
2. Add the final strings to the Event 011 English localisation file with UTF-8 BOM encoding.
3. Keep route selection on `global.secret_alliance_reveal_route` and preserve all six defined values through the four packages above.
4. Keep `secret_alliance_snapshot_reveal_state` before the super-event call so the member count is stable.
5. Wire `GFX_super_event_011_secret_alliance_public_reveal` only after the final DDS exists.
6. Wire audio ID `43`, its music helpers, sound wrappers, and the music table from the audio handoff.
7. Keep the super-event after public-state and faction creation so the faction name and leader target resolve.
8. Do not reuse any of these strings in pre-reveal Event Details, evolutions, decisions, reports, or spreadsheet text.

## Blockers and simplifications

- Text research has no source, attribution, wording, route-coverage, or UI-design blocker.
- No fallback quote, button remark, generic route description, placeholder wording, or modern copyrighted reference was used.
- No route was omitted or merged beyond the requested grouping of the three player-forced runtime values.
- The international status of the 1910 Giles translation varies by jurisdiction. The exact United States public-domain status and Project Gutenberg's outside-U.S. warning are recorded above.
- The final super-event image is not yet present. This blocks a full super-event completion claim, but it does not block the text handoff.
- Gameplay, localisation, scripted localisation, GFX, audio definitions, music-table, and spreadsheet wiring remain for the main agent by task boundary.
