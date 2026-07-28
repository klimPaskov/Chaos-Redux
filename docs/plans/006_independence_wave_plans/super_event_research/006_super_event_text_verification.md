# Event 006 super-event text verification

Research date: 2026-07-14

This note verifies the accepted text sources for the two Event 006 super-events and provides implementation-ready localisation values. The accepted title, button, and quotation selections remain unchanged. The recommended descriptions apply narrow voice and trigger-coverage corrections found during verification.

No gameplay file, localisation file, spreadsheet, asset, audio file, interface file, or source specification was changed in this pass.

## Outcome

| Super-event | Source verdict | Text verdict | UI-fit verdict | Parent action |
| --- | --- | --- | --- | --- |
| The League of New States | Wilson Point XIV wording and attribution verified | Use the corrected broad-leadership description below | High confidence | Adopt the description correction and assign the final slot |
| Every Border a Casus Belli | Hosea 8:7 KJV wording, continuation, and public-domain label verified | Use the corrected route-neutral description and excerpt ellipsis below | High confidence | Adopt the description correction and assign the final slot |

The text package has no source, attribution, copyright, or static-UI blocker. The corrected descriptions should be folded into the Event 006 source specification when the parent accepts this working note.

## References and precedents consulted

This pass consulted the required offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding before inspecting Event 006 files.

Vanilla references included:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_objects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/loc_formatter_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/NewsEvents.txt`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/localisation/english/events_l_english.yml`

Current Chaos Redux presentation and localisation precedents included:

- `interface/chaosx_super_events.gui`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`
- `localisation/english/010_death_l_english.yml`
- `localisation/english/014_cannibalism_super_events_l_english.yml`
- `localisation/english/015_utopia_manifesto_l_english.yml`

All Event 006 specification files were treated as accepted design authority. The closest text authorities were:

- `docs/specs/006_independence_wave_specs/research/006_super_event_text_research.md`
- `docs/specs/006_independence_wave_specs/prompts/independence_wave_super_event_prompt.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`

## Description corrections found during verification

### League package

The accepted description names a permanent council. Part 6 permits a rotating presidency, an elected secretary-general, strongest-member leadership, a regional council, dual leadership, or a congress host. The phrase `chosen the league's leadership` covers every accepted structure.

The accepted final sentence frames the reveal through governments that previously dismissed the breakaways. Current Chaos Redux event-writing rules prohibit staged contrast constructions. The corrected final sentence describes the league's visible capacities directly.

### Dangerous package

The accepted description begins with the league's congress. Part 6 also permits this super-event to fire from a high-chaos twenty-country wave, synchronized wars by Event 006 countries, or a hidden formable leading an aggressive bloc. Those packages do not require a league congress. The corrected description uses `new-state governments`, which remains true for every eligible trigger family.

The accepted phrases `has ceased to limit itself` and `once protected ... has become` use temporal contrast as their dramatic structure. The corrected wording describes coordinated commands, material pledges, and simultaneous war preparations directly.

## Static UI-fit evidence

The current super-event UI uses these fixed boxes:

| Surface | Font | Box |
| --- | --- | --- |
| Title | `hoi_36header` | `700 x 50` |
| Description | `hoi4_typewriter22` | `320 x 370` |
| Quote | `hoi_18mbs` | `370 x 79` |
| Button | `hoi_20bs` | `352 x 48` source texture |

The estimates below use the exact `xadvance` values and line heights from the shipped vanilla `.fnt` files. Description estimates include the recommended `\n\n` paragraph break. Quote estimates include the full displayed attribution and its explicit line break.

| Text surface | Measured width or wrap | Available space | Result |
| --- | ---: | ---: | --- |
| `The League of New States` | `384 px`, one `36 px` line | `700 x 50` | Fits |
| `Every Border a Casus Belli` | `416 px`, one `36 px` line | `700 x 50` | Fits |
| League description | `13` lines, about `286 px` high | `320 x 370` | Fits |
| Dangerous description | `13` lines, about `286 px` high | `320 x 370` | Fits |
| Wilson quotation plus full attribution | `4` lines, about `72 px` high | `370 x 79` | Fits with `7 px` vertical margin |
| Hosea quotation plus attribution | `3` lines, about `54 px` high | `370 x 79` | Fits |
| `Small states, one covenant.` | `191 px` advance | `352 px` button | Fits |
| `They have sown the wind.` | `184 px` advance | `352 px` button | Fits |

The current `hoi_18mbs.fnt` does not define the Unicode ellipsis glyph. The localisation-ready quotations therefore use three ASCII periods as an omission marker. This preserves source honesty and avoids a missing-glyph risk.

## Super-event 1: The League of New States

### Role and trigger alignment

This package announces the first durable Event 006 league after a successful congress, minimum founding membership, charter adoption, leadership selection, and activation as a diplomatic or military actor. Its wording remains broad enough for defensive, developmental, sovereign-equality, armed-liberation, and revisionist charter families. Charter-specific language belongs in the follow-up event and related scripted localisation.

### Final localisation-ready recommendation

The parent should replace `<slot>` with the verified final super-event slot.

```yaml
chaosx_super_event.<slot>.t: "The League of New States"
chaosx_super_event.<slot>.d: "Delegates from the newest states have ratified a common charter and chosen the league's leadership. The signatories promise arbitration, mutual aid, and collective resistance to any former host or foreign patron that attempts to extinguish a member.\n\nThe league can speak for its members, bargain in their name, and coordinate shared aid or mobilization."
chaosx_super_event.<slot>.a: "Small states, one covenant."
chaosx_super_event.<slot>.q: "\"A general association of nations must be formed under specific covenants...\"\n §Y-Woodrow Wilson, Fourteen Points, Point XIV, 8 January 1918-§!"
```

### Title and button

- The title is original Event 006 wording. It is specific to institutional formation and has no external quotation dependency.
- The button is original Event 006 wording. `Covenant` deliberately supports the charter theme and echoes the selected source without claiming to quote it.

### Quotation verification

- Accepted source: [Yale Law School, Avalon Project transcript](https://avalon.law.yale.edu/20th_century/wilson14.asp)
- Primary corroboration: [U.S. National Archives transcript and record citation](https://www.archives.gov/milestone-documents/president-woodrow-wilsons-14-points)
- Additional primary-document record and rights statement: [Library of Congress, Address of President Wilson to Congress](https://www.loc.gov/item/18026102/)
- Attribution confidence: high
- Documentary attribution: Woodrow Wilson, *Fourteen Points*, Point XIV, 8 January 1918
- Wording result: the displayed words match the opening of Point XIV. The ASCII ellipsis accurately marks the omitted remainder.
- Source acceptability: the underlying 1918 address is public historical text. The Library of Congress record marks the digitized book as public domain and free to use and reuse. The Yale transcript remains an acceptable archival access point, with the National Archives providing the stronger primary corroboration.

### Date, place, and context direction

The verified date is 8 January 1918. Wilson delivered the text as an address to the United States Congress on war aims and peace terms. Point XIV proposes a general association that would guarantee the political independence and territorial integrity of states regardless of size. That context supports the league reveal directly.

Washington, D.C. is the appropriate historical place direction if a production note needs one. The super-event quote line already reaches full source confidence through the speaker, document, point, and exact date, so no place label is needed in player-facing text.

## Super-event 2: Every Border a Casus Belli

### Role and trigger alignment

This package announces an Independence Wave outcome with coordinated revisionist claims and simultaneous war risk. The route-neutral description covers all accepted trigger families, including an offensive league, a radical twenty-country wave, synchronized wars, a hidden aggressive formable, and a league-sponsored cascade. It does not fit an ordinary wave, election, consultative congress, isolated formable, or routine border war, which matches the accepted exclusions.

### Final localisation-ready recommendation

The parent should replace `<slot>` with the verified final super-event slot.

```yaml
chaosx_super_event.<slot>.t: "Every Border a Casus Belli"
chaosx_super_event.<slot>.d: "New-state governments coordinate claims, ultimatums, arms shipments, and mobilization schedules across several regions. Their border commands follow shared timetables, and governments pledge arms or troops to support one another's territorial demands.\n\nFormer hosts reinforce several fronts as they prepare for wars that may begin on the same day."
chaosx_super_event.<slot>.a: "They have sown the wind."
chaosx_super_event.<slot>.q: "\"For they have sown the wind, and they shall reap the whirlwind...\"\n §Y-Hosea 8:7, King James Version-§!"
```

### Title and button

- The title is original Event 006 wording built around the common legal phrase `casus belli`. It is not attributed as an external quotation.
- The button is a short source-derived allusion to Hosea 8:7. It omits the verse's opening connective and remains a button reaction, so it should be documented as an allusion rather than an independent original line.

### Quotation verification

- Accepted source and full-chapter context: [BibleGateway, Hosea 8, King James Version](https://www.biblegateway.com/passage/?search=Hosea%208&version=KJV)
- Attribution confidence: high
- Documentary attribution: Hosea 8:7, King James Version
- Wording result: the displayed words match the beginning of verse 7. The source continues after `whirlwind` with a colon and further clauses. The ASCII ellipsis accurately marks that continuation. The period in the accepted research text should not be used because it presents the excerpt as the complete sentence.
- Source acceptability: BibleGateway labels the KJV text on the source page as public domain. The selected line is a short scriptural excerpt with a precise book, chapter, verse, and translation citation.

### Date, place, and context direction

Hosea 8 addresses Israel and Ephraim through covenant breach, unauthorized rulers, idolatry, reliance on foreign powers, and consequences that exceed the acts that produced them. The verse therefore fits coordinated governments whose claims and support arrangements multiply into several wars.

No historical speaker, composition date, or single delivery place should be added to the in-game attribution. Those points carry scholarly uncertainty and add nothing to the super-event. The book, chapter, verse, and translation form the complete safe attribution.

## Parent-owned adoption and wiring

1. Review and accept the two description corrections.
2. Fold accepted wording into `docs/specs/006_independence_wave_specs/research/006_super_event_text_research.md` or the appropriate source specification before treating this working note as final design authority.
3. Assign and verify the two final super-event slots. This research pass intentionally did not invent slot numbers.
4. Copy the localisation-ready values into the final UTF-8 with BOM localisation file and keep the `.t`, `.d`, `.a`, and `.q` suffixes aligned with each slot.
5. Preserve the full source attributions in the final super-event documentation.
6. Keep charter-specific league tone in the follow-up event unless final architecture provides a clean dynamic localisation branch.

## Blockers, uncertainty, and simplifications

- Text source verification has no blocker.
- The corrected descriptions remain a working-plan recommendation until the parent adopts them into the source specification.
- Static UI fit has high confidence from exact shipped font metrics. No localisation or gameplay slot existed in scope for a final integrated render.
- The separate Event 006 audio verification still blocks the full League super-event package on the accepted `6001` recording's United States redistribution rights. That blocker does not affect the text verdict.
- No fallback title, quotation, button, source, or substitute wording package was used.
- No simplification was made within the assigned text-research scope.
