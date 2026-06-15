# Event 010 — Death: Assets, Super-Events, Achievements, Scenarios, and Acceptance

## Visual identity

Death's visual language should be simple and severe:

- black map color;
- empty shorelines;
- abandoned harbors;
- fog or storm over dead ground;
- official paper records with no names;
- maps that look wrong because a place is present but no longer inhabited;
- Zol as a face-like absence rather than a monster;
- ghost divisions as thin, low-contrast military silhouettes, not fantasy undead hordes.

Avoid gore, skull spam, horror-comedy, modern cinematic color grading, and readable generated text. The event works best when it is quiet.

## Required asset families

### Country assets

| Asset | Type | Source mode | Direction |
| --- | --- | --- | --- |
| `DTH` flag set | Flag normal/medium/small | Generated fictional or hand-authored from generated source | Almost black cloth/void flag, no readable emblem, no text. |
| Zol leader portrait | Leader portrait 156x210 | Generated fictional/nonhuman | Black figure, void-lit face (bright white light from eyes glowing), period-compatible painterly treatment. Subtle eyes glow animation |
| Zol world-end portrait | Animated leader portrait plus static fallback | Generated frame-by-frame | Subtle void/shroud motion; real frames, not filter pulse. |
| Herald of Zol cosmetic flag | Optional route flag | Generated fictional | Black oath motif distinct from Death's own flag. |
| Black Apostolate flag | Optional hidden route flag | Generated fictional | If hidden route implemented, separate from DTH flag. |

### Report and news images

| Asset | Type | Source mode | Direction |
| --- | --- | --- | --- |
| `report_event_death_mail_boat` | Report image 210x176 | Generated period-documentary | Empty pier, mail boat, no people. |
| `report_event_death_lighthouse` | Report image 210x176 | Generated period-documentary | Lighthouse burning over empty island settlement. |
| `report_event_death_census` | Report image 210x176 | Generated period-documentary | Census office, papers, empty chairs, no readable text. |
| `news_event_death_mainland_reveal` | News image 397x153 black and white | Generated period-news | Mainland coastal town or road emptied, black horizon. |
| `news_event_death_defeated` | News image 397x153 black and white | Generated period-news | Troops entering empty blackened town; no triumphal crowds. |

Generated report images still need report-card treatment. Generated news images must be black and white.

### Super-event images

| Super-event | Image asset | Source mode | Direction |
| --- | --- | --- | --- |
| Mainland reveal | `super_event_death_reveal` | Generated | Black coastline, empty mainland settlement, official observers dwarfed by absence. |
| World-end | `super_event_death_world_end` | Generated | Several distant coasts or one symbolic shore with black tide; terminal mood. |
| Defeat aftermath | `super_event_death_defeat_aftermath` | Generated | Soldiers or surveyors in dead empty land; victory without restoration. |
| Whole world consumed | `super_event_death_world_consumed` | Generated symbolic/documentary | Empty map table or final radio room with no operators; no readable text. |
| Herald oath optional | `super_event_death_black_oath` | Generated | Government officials before a dark sealed document; not modern occult neon. |

### Icons

The implementation should not derive small icons by resizing focus icons. Each icon type needs its own output designed for its size.

| Asset family | Type | Direction |
| --- | --- | --- |
| `idea_country_without_breath` | Idea 64x64 | Black country silhouette/no pulse. |
| `idea_first_silence` | Idea 64x64 | Sealed envelope/quiet island. |
| `idea_public_death` | Idea 64x64 | Black map pin or blank nameplate. |
| `idea_last_shores` | Idea 64x64 | Black tide over coast. |
| `decision_category_death_country` | Decision category | Black atlas/map book. |
| `decision_death_survey_boat` | Decision 32x32 | Tiny boat and empty pier. |
| `decision_death_coastal_watch` | Decision 32x32 | Watchlight or beacon. |
| `decision_death_quarantine_line` | Decision 32x32 | Barricaded road. |
| `decision_death_wasteland_gear` | Decision 32x32 | Mask/boots/gear silhouette. |
| `decision_death_black_book` | Decision 32x32 | Closed black book, no text. |
| `decision_death_black_oath` | Decision 32x32 | Black hand or seal. |
| `unit_death_ghost_host` | Unit/tech icon if needed | Thin pale formation silhouette. |
| Death focus icon family | Focus 94x86 | Separate motifs for Shroud, Hunger, Census, Wasteland, Host, Last Shores. |
| Achievement icons | Achievement 64x64 | See achievement table below. |

### Custom UI and animation assets

| Asset | Target | State logic | Notes |
| --- | --- | --- | --- |
| `death_black_atlas_background` | Scripted GUI/window | Static after reveal | Dark map-board panel, readable UI space. |
| `death_black_atlas_header_animated` | Header strip | Visible after reveal; stronger at world-end | Frame-sheet, slow fog/shroud drift. |
| `death_coastal_risk_pulse_animated` | Risk icon | Shows high/critical coastal jump risk | Static fallback required. |
| `death_wither_target_frame_animated` | State card frame | Active wither target | Thin animated edge. |
| `death_compact_warning_animated` | Compact panel | Low cohesion | Subtle flicker. |
| `death_zol_portrait_world_end_animated` | Leader or GUI portrait | World-end or Herald oath | Optional but recommended. |

Animations must follow the frame-animation workflow: source frames, processed frames, horizontal frame sheet, DDS, static fallback, preview GIF for review only, manifest, and `.gfx` handoff.

## Super-event package plan

Super-event title text, button text, cultural remarks, and quotes are not selected by this planning spec. They must be researched by the super-event text workflow before implementation. The implementation agent must not use invented sample lines, working titles, or placeholder quotes as final localisation.

Each super-event below uses a functional role label only. The role label is for planning and asset routing, not a final title. The final title, button text, cultural remark, and quote must come from `docs/super_events/010_death_super_event_research.md` after source-backed research.

### Super-event role 1 — Mainland reveal

| Field | Direction |
| --- | --- |
| Functional role label | Mainland reveal |
| Trigger | Death consumes first mainland state with more than 100,000 population. |
| Role | First reveal. |
| Tone | Blunt public recognition, not yet final apocalypse. |
| Title requirement | Research a short reveal title; do not use an unresearched working title. |
| Description direction | A mainland coastal state has emptied. The old island reports are reinterpreted. The black country is now a named crisis. |
| Button or cultural remark requirement | Research a short line or allusion about diplomatic helplessness, counting the living, official disbelief, or failed treaty language. Do not use invented sample text. |
| Quote requirement | Research and verify a quote about death, silence, discovery, fear, naming, or inevitability. Prefer public-domain literature, scripture, philosophy, or historical source. |
| Audio direction | Sparse, grim, 1-2 minute public-domain or clearly licensed track; not a drone/test tone. |
| Image | `super_event_death_reveal` generated. |
| Follow-up | Unlock Death Country decisions, Compact, world-threat flag. |

### Super-event role 2 — World-end

| Field | Direction |
| --- | --- |
| Functional role label | World-end |
| Trigger | Death has consumed an entire continent and Chaos is above 1000. |
| Role | World-end scenario. |
| Tone | Terminal, oceanic, global. |
| Title requirement | Research a short terminal title tied to coasts, final borders, silence, or Death crossing continents. Do not use an unresearched working title. |
| Description direction | One continent is gone from the living world; new black footholds appear on every remaining continent. |
| Button or cultural remark requirement | Research a short line or allusion about every shore becoming exposed, the sea carrying disaster, or the last safe border failing. Do not use invented sample text. |
| Quote requirement | Research and verify a quote about finality, judgment, silence, shores, collapse, or the end of order. |
| Audio direction | Finality, slow dread, unique final track. |
| Image | `super_event_death_world_end` generated. |
| Follow-up | Set world-end flag, create footholds, spawn world-end hosts, freeze normal event firing. |

### Super-event role 3 — Defeat aftermath

| Field | Direction |
| --- | --- |
| Functional role label | Defeat aftermath |
| Trigger | Death defeated after public reveal and after consuming a large crisis threshold. |
| Role | Defeat aftermath. |
| Tone | Costly victory; no restoration of the dead. |
| Title requirement | Research a short aftermath title about survival, empty land, memory, or victory that cannot restore the dead. Do not use an unresearched working title. |
| Description direction | Death is removed from the map, but wastelands stay empty. Countries argue over memory, rebuilding, and blame. |
| Button or cultural remark requirement | Research a short line or allusion about grief, memorial records, the limits of victory, or the names of the dead. Do not use invented sample text. |
| Quote requirement | Research and verify a quote about memory, survival, grief, vigilance, or rebuilding after loss. |
| Audio direction | Reflective, not triumphant. |
| Image | `super_event_death_defeat_aftermath` generated. |
| Follow-up | Cleanup compact, open reconstruction decisions, mark Death defeated. |

### Super-event role 4 — Whole world consumed

| Field | Direction |
| --- | --- |
| Functional role label | Whole world consumed |
| Trigger | Death consumes all eligible world states. |
| Role | Final completion. |
| Tone | Silence and record failure. |
| Title requirement | Research a short final title about witness, silence, last records, or the end of human observation. Do not use an unresearched working title. |
| Description direction | There is one country and no one left to read the map. |
| Button or cultural remark requirement | Research a short line or allusion about silence without witnesses, failed records, or the absence of an audience. Do not use invented sample text. |
| Quote requirement | Research and verify a quote about silence, oblivion, lastness, witness, or the failure of records. |
| Audio direction | Very sparse final track, unique and documented. |
| Image | `super_event_death_world_consumed` generated. |
| Follow-up | Achievement hooks; terminal state. |

### Optional super-event role — Herald oath reveal

Only use this if the Herald route is implemented deeply enough.

| Field | Direction |
| --- | --- |
| Functional role label | Herald oath reveal |
| Trigger | A major country or player-led country publicly pledges to Zol. |
| Role | Hidden route reveal / betrayal of the living. |
| Tone | Government euphemism, cultic surrender. |
| Title requirement | Research a short title about oath, names, surrender, or pledged service to Death. Do not use an unresearched working title. |
| Button or cultural remark requirement | Research a short line or allusion about signatures, names, bargains, betrayal, or state surrender. Do not use invented sample text. |
| Quote requirement | Research and verify a quote about bargains, names, betrayal, vows, or death. |
| Image | `super_event_death_black_oath` generated. |

## Achievement plan

Achievements should be difficult and not unlock just because the event fires.
Achievement titles are not super-event titles and must not be reused as super-event localisation unless separately researched and documented.

| ID | Title | Visibility | Eligible player | Conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `death_no_one_heard_the_first_boat` | No One Heard the First Boat | Hidden | Any country receiving early island reports | Discover Death and declare war before mainland reveal. | Death reveals itself first. | Hard | Small boat beside black empty pier. |
| `death_not_on_my_continent` | Not on My Continent | Visible | Any continental country neighboring or near Death | Defeat Death after reveal before it consumes three mainland states on your continent. | Use Black Oath. | Medium-hard | Coastline barricade against black map edge. |
| `death_the_names_do_not_come_back` | The Names Do Not Come Back | Visible | Any country | Defeat Death after it consumed at least 10 million population, then complete three wasteland outpost projects. | Restore through forbidden Herald path. | Hard | Blank census book and candle. |
| `death_last_ferry` | The Last Ferry | Visible | Island/coastal country | Evacuate at least five threatened island/coastal states before Death consumes them, then survive the reveal. | Become Herald. | Hard | Ferry silhouette leaving black shore. |
| `death_counted_every_name` | Counted Every Name | Hidden | Compact leader or major | Use census/compact decisions to delay ghost tier, then defeat Death before 800-tier ghosts appear. | Black methods above low exposure. | Very hard | Ledger with empty columns, no readable text. |
| `death_black_tide_reversed` | Black Tide Reversed | Visible | Any country in world-end scenario | After Last Shores fires, recapture every Death foothold outside the first consumed continent and defeat Death. | Any Herald state survives as Herald. | Extreme | Black tide pulled back from multiple coasts. |
| `death_friend_of_zol` | Friend of Zol | Hidden | Any country eligible for Black Oath | Become Herald of Zol, survive until Death reaches world-end, and keep your capital unconsumed for one year. | Break the Oath. | Very hard | Black oath seal with living crown. |
| `death_no_witnesses` | No Witnesses | Hidden/rare | Death scenario player or Herald route if supported | Death consumes all eligible world states. | Death defeated. | Extreme | Empty radio room or black globe. |
| `death_before_the_name` | Before the Name | Hidden | Any country | Defeat Death before the public reveal super-event fires. | Trigger reveal or use manual maximum scenario. | Very hard | Covered map label with black stain. |
| `death_the_living_conference` | The Living Conference | Visible | Major or threatened leader | Form the containment compact with at least five members, keep cohesion above threshold, and defeat Death. | Use Black Oath or abandon compact. | Hard | Conference table with black empty chair. |
| `death_book_burner` | Book Burner | Hidden | Necromancy user | Open the Black Book, use at least one bound-name decision, burn the book before exposure reaches high, then defeat Death. | Become Herald or let exposure reach maximum. | Hard | Burning black book with no visible letters. |
| `death_six_continents_one_color` | Six Continents, One Color | Hidden | Death scenario / any observer if achievement system supports global failure | Witness or cause Last Shores world-end footholds on every continent. | Death defeated before world-end. | Extreme | Six small black coast shapes around a dark center. |

Highest priority achievements for first implementation: `death_before_the_name`, `death_not_on_my_continent`, `death_the_names_do_not_come_back`, `death_black_tide_reversed`, `death_no_witnesses`.

## Event catalog row direction

After implementation, the spreadsheet row for ID 10 should be updated from `Spirit of War/Peace` to `Death`.

Suggested player-facing details field:

> A quiet black country appears on a remote island and does not announce itself. Months later, nearby records stop matching reality. Islands fall silent, ports empty, and the name Death remains a rumour until the first mainland state vanishes.

Suggested evolution fields:

- `Gathering Storm: Empty Shoreline Whispers makes missing-island reports more frequent without revealing Death.`
- `Rising Chaos: The Inland Smell brings Death closer to mainland coasts and shortens the hidden island-only phase.`
- `Chaos Tier: First Ghost Muster unlocks weak passive ghost hosts if Death has consumed enough population.`
- `Totalen Chaos: Black Tide Recovery strengthens ghosts and lets Death return to coasts after setbacks.`
- `World Collapse: the terminal branch becomes available; if a continent is consumed while Chaos is above 1000, Death opens footholds on every continent.`

Suggested world-end field:

> If Death consumes a full continent while Chaos is above 1000, the Last Shores world-end scenario begins: Death gains coastal footholds on every continent, ghost hosts become aggressive, and normal containment becomes a terminal struggle.

Type remains `Minor Fire-Once`. Cluster fields remain blank / no cluster. Status should remain `To Be Reworked` until implementation completes and is tested.

## Documentation requirements

Create or update a canonical event doc after implementation:

`docs/events/010_death.md`

The doc should cover:

1. what Death is;
2. replacement of Spirit of War/Peace;
3. event map and subevents;
4. origin selection;
5. state consumption and wasteland effects;
6. hidden reports;
7. reveal super-event;
8. spread, withering, coastal jumps;
9. ghost divisions;
10. containment decisions and compact;
11. necromancy and Herald paths;
12. world-end branch;
13. defeat aftermath;
14. assets and sprite expectations;
15. AI behavior;
16. triggerable scenario;
17. limitations or unsupported visual fields.

## Implementation acceptance criteria

The rework is not complete unless all of these are true:

- The old Spirit of War/Peace active content is deleted, disabled, or marked superseded with no active references.
- ID 10 resolves to Death in event names, debug names, event details, event log, catalog, and manual trigger surfaces.
- Death can spawn silently on a valid remote island state.
- The origin state is consumed through the shared consumption effect.
- Every consumed state deletes population, industry, and strategic value, adds civilian deaths when enabled, becomes a Death core, and applies wasteland behavior.
- Death has no starting units.
- Pre-reveal reports are delayed and do not spoil Death.
- Mainland consumption over 100,000 population triggers reveal and super-event.
- Post-reveal withering follows the rule that target states with non-Death divisions present cannot be consumed by withering.
- Death declares war on neighboring countries after reveal.
- Coastal jump logic exists with cooldown and containment counters.
- Ghost divisions unlock around 600, strengthen around 800, and become aggressive only at world-end.
- Death defeat requires full occupation/no controlled states, not ordinary surrender shortcuts.
- Recaptured wastelands remain empty and strategically damaged.
- Containment decisions use concrete costs, map objectives, active missions, and AI behavior.
- The Living Containment Compact or equivalent coalition system exists after reveal.
- Dark methods and Black Oath routes are either fully implemented or explicitly queued as unimplemented optional branches; they must not be half-visible placeholders.
- World-end requires both full continent consumption and Chaos above 1000.
- World-end footholds appear on every remaining continent.
- Whole-world consumed final super-event and achievement hooks exist.
- Death is registered as a special chaos country and actual nonhuman country.
- Assets are created, processed, converted, documented, and wired or accurately reported as pending asset work.
- Super-event text, image, audio, docs, and spreadsheet fields agree.
- AI behavior is route/stage-aware and does not pick impossible actions.
- Completion audit and localisation audit run after implementation.

## Known uncertainties to resolve during implementation

- Exact island-state filters depend on available state metadata and existing state-group helpers.
- Some state building or map-visual fields may not support direct deletion/visual effects; implementation must document exact supported representation.
- The best way to apply ticking strength loss should be chosen from existing Chaos Redux helper patterns to avoid broad daily world scans.
- The country tag `DTH` must be conflict-checked.
- If the Black Atlas scripted GUI is too large for the first implementation pass, it should be queued explicitly and the decision category header must still show core values through scripted localisation.
- Super-event audio and quote research require dedicated research subagents before final wiring.
