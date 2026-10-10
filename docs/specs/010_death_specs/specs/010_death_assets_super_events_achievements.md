# Event 010 - Death: Assets, Super-Events, Achievements, Scenarios, and Acceptance

## Visual identity

Death's visual language should be simple and severe:

- black map color.
- empty shorelines.
- abandoned harbors.
- fog or storm over dead ground.
- official paper records with no names.
- maps that look wrong because a place is present but no longer inhabited.
- Zol as a face-like absence rather than a monster.
- ghost divisions as thin, low-contrast military silhouettes, not fantasy undead hordes.

Avoid gore, skull spam, horror-comedy, modern cinematic color grading, and readable generated text. The event works best when it is quiet.

## Required asset families

### Country assets

| Asset | Type | Source mode | Direction |
| --- | --- | --- | --- |
| `DTH` flag set | Flag normal/medium/small | Generated fictional or hand-authored from generated source | Almost black cloth/void flag, no readable emblem, no text. |
| Zol leader portrait | Leader portrait 156x210 | Generated fictional/nonhuman | Black figure, void-lit face (bright white light from eyes glowing), period-compatible painterly treatment. Subtle eyes glow animation |
| Zol world-end portrait | Animated leader portrait plus static fallback | Generated frame-by-frame | Subtle void/shroud motion. Real frames, not filter pulse. |
| Herald of Zol cosmetic flag | Optional route flag | Generated fictional | Black oath motif distinct from Death's own flag. |
| Black Apostolate flag | Optional hidden route flag | Generated fictional | If hidden route implemented, separate from DTH flag. |

### Report and news images

| Asset | Type | Source mode | Direction |
| --- | --- | --- | --- |
| `report_event_death_mail_boat` | Report image 210x176 | Generated period-documentary | Empty pier, mail boat, no people. |
| `report_event_death_lighthouse` | Report image 210x176 | Generated period-documentary | Lighthouse burning over empty island settlement. |
| `report_event_death_census` | Report image 210x176 | Generated period-documentary | Census office, papers, empty chairs, no readable text. |
| `news_event_death_mainland_reveal` | News image 397x153 black and white | Generated period-news | Mainland coastal town or road emptied, black horizon. |
| `news_event_death_defeated` | News image 397x153 black and white | Generated period-news | Troops entering empty blackened town. No triumphal crowds. |

Generated report images still need report-card treatment. Generated news images must be black and white.

### Super-event images

| Super-event | Image asset | Source mode | Direction |
| --- | --- | --- | --- |
| Mainland reveal | `super_event_death_reveal` | Generated | Black coastline, empty mainland settlement, official observers dwarfed by absence. |
| World-end | `super_event_death_world_end` | Generated | Several distant coasts or one symbolic shore with black tide. Terminal mood. |
| Defeat aftermath | `super_event_death_defeat_aftermath` | Generated | Soldiers or surveyors in dead empty land. Victory without restoration. |
| Whole world consumed | `super_event_death_world_consumed` | Generated symbolic/documentary | Ruined coastal capital consumed by a vast black tide. Dramatic exterior end-state, no office, no map table, no readable text. |
| Herald oath optional | `super_event_death_black_oath` | Generated | Government officials before a dark sealed document. Not modern occult neon. |

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
| `death_black_atlas_header_animated` | Header strip | Visible after reveal. Stronger at world-end | Frame-sheet, slow fog/shroud drift. |
| `death_zol_portrait_world_end_animated` | Leader or GUI portrait | World-end or Herald oath | Implemented as static fallback plus registered eight-frame animated sprite. |

The planned coastal-risk pulse, wither-target frame and compact-warning animations were never registered; they are superseded by the accepted Atlas design, which has no standalone status icons.
The header animation is registered as `GFX_death_black_atlas_header_animated` in `interface/010_death.gfx`; the earlier GUI inspection reported an unresolved static-fallback link for it, which remains an open verification item (see the release completion record).

Animations must follow the frame-animation workflow: source frames, processed frames, horizontal frame sheet, DDS, static fallback, preview GIF for review only, manifest, and `.gfx` handoff.

## Super-event package plan

The five super-event packages are implemented; Part 1 lists their IDs, titles and triggers, and [`docs/super_events/010_death/`](../../../super_events/010_death/README.md) holds the sourced text research, attribution and audio evidence.
Do not replace researched titles, options, cultural remarks or quotes with invented lines, and do not reuse achievement titles as super-event text.
The per-role research briefs that guided that work are retained in git history and in `prompts/010_death_super_event_prompt.md`.

| ID | Image sprite (file) | Audio | Quote source | Image direction |
| --- | --- | --- | --- | --- |
| `62` | `GFX_super_event_death_reveal` | `sound/010_death/super_event_32_death_reveal.wav` | Francis Bacon | Black coastline, empty mainland settlement, official observers dwarfed by absence. |
| `63` | `GFX_super_event_death_world_end` | `super_event_33_death_world_end.wav` | Matthew Arnold | Several distant coasts or one symbolic shore with black tide. |
| `64` | `GFX_super_event_death_defeat` (`super_event_death_defeat_aftermath.dds`) | `super_event_34_death_defeat_aftermath.wav` | Abraham Lincoln | Soldiers or surveyors in dead empty land; victory without restoration. |
| `65` | `GFX_super_event_death_world_consumed` | `super_event_35_death_world_consumed.wav` | Edward Young | Ruined coastal capital consumed by a vast black tide; no office, map table, or readable text. |
| `66` | `GFX_super_event_death_black_oath` | `super_event_36_death_black_oath.wav` | Isaiah 28:15 (KJV) | Government officials before a dark sealed document; not modern occult neon. |

## Achievement plan

Achievements should be difficult and not unlock just because the event fires.
Achievement titles are not super-event titles and must not be reused as super-event localisation unless separately researched and documented.

| ID | Title | Visibility | Eligible player | Conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `death_no_one_heard_the_first_boat` | No One Heard the First Boat | Hidden | Any country receiving early island reports | Find Death and declare war before a mainland coast names it. | Death is named from a mainland coast first. | Hard | Small boat beside black empty pier. |
| `death_not_on_my_continent` | Not on My Continent | Visible | Any continental country neighboring or near Death | Defeat Death after it is named, before it consumes three mainland states on your continent. | Use Black Oath. | Medium-hard | Coastline barricade against black map edge. |
| `death_the_names_do_not_come_back` | The Names Do Not Come Back | Visible | Any country | Defeat Death after it consumed at least 10 million population, then complete three wasteland outpost projects. | Restore through forbidden Herald path. | Hard | Blank census book and candle. |
| `death_last_ferry` | The Last Ferry | Visible | Island/coastal country | Prepare at least five threatened island or coastal states with Keep the Port Lit that Death later consumes (`death_decision_tuning.last_ferry_required_states`), then survive until the black country is named. | Become Herald. | Hard | Ferry silhouette leaving black shore. |
| `death_counted_every_name` | Counted Every Name | Hidden | Compact leader or major | Use census and compact work to defeat Death before the Hollow Hosts gather. | Black methods above low exposure. | Very hard | Ledger with empty columns, no readable text. |
| `death_black_tide_reversed` | Black Tide Reversed | Visible | Any country in world-end scenario | After Last Shores fires, recapture every Death foothold outside the first consumed continent and defeat Death. | Any Herald state survives as Herald. | Extreme | Black tide pulled back from multiple coasts. |
| `death_friend_of_zol` | Friend of Zol | Hidden | Any country eligible for Black Oath | Become Herald of Zol, survive until Death reaches world-end, and keep your capital unconsumed for one year. | Break the Oath. | Very hard | Black oath seal with living crown. |
| `death_no_witnesses` | No Witnesses | Hidden/rare | Death scenario player or Herald route if supported | Death consumes all eligible world states. | Death defeated. | Extreme | Empty radio room or black globe. |
| `death_before_the_name` | Before the Name | Hidden | Any country | Defeat Death before a mainland coast gives it a public name. | Trigger naming or use manual maximum scenario. | Very hard | Covered map label with black stain. |
| `death_the_living_conference` | The Living Conference | Visible | Major or threatened leader | Form the containment compact with at least five members, keep cohesion above threshold, and defeat Death. | Use Black Oath or abandon compact. | Hard | Conference table with black empty chair. |
| `death_book_burner` | Book Burner | Hidden | Necromancy user | Open the Black Book, use at least one bound-name decision, burn the book before exposure reaches high, then defeat Death. | Become Herald or let exposure reach maximum. | Hard | Burning black book with no visible letters. |
| `death_six_continents_one_color` | Six Continents, One Color | Hidden | Death scenario / any observer if achievement system supports global failure | Witness or cause Last Shores footholds on every continent. | Death defeated before world-end. | Extreme | Six small black coast shapes around a dark center. |
| `death_black_apostolate` | Black Apostolate | Hidden | Herald route player | Become a Herald, keep Death alive into world-end, pay enough name debt, sacrifice enough states, and proclaim the Black Apostolate. | Break the oath or fail the hidden thresholds. | Extreme | Black institutional seal over a dead ledger. |

All thirteen achievements are implemented in `common/achievements/chaos_redux_achievements.txt` with the `010_` prefix on these IDs (for example `010_death_last_ferry`).
Six Continents, One Color counts distinct continents through `global.death_world_end_unique_continents`, not foothold states (accepted 2026-10-05).
The original first-implementation priority was: `death_before_the_name`, `death_not_on_my_continent`, `death_the_names_do_not_come_back`, `death_black_tide_reversed`, `death_no_witnesses`, `death_friend_of_zol`, `death_book_burner`, and `death_black_apostolate`.

## Event catalog row direction

After implementation, the spreadsheet row for ID 10 should be updated from `Spirit of War/Peace` to `Death`.

Suggested player-facing details field:

> A quiet black country appears on a remote island and does not announce itself. Months later, nearby records stop matching reality as islands fall silent and ports empty. The name Death remains a rumour until the first mainland state vanishes.

Suggested evolution fields:

- `Second Shore: Death reaches beyond its first island, and the silence spreads along nearby shores.`
- `Mainland Hunger: Islands fall quiet as Death's reach approaches the mainland.`
- `First Hosts: The first weak ghost hosts appear among the emptied states.`
- `Hollow Hosts: Ghost hosts gather in greater numbers and press farther from the silent coasts.`
- `World End: Death opens black footholds across every continent, and containment becomes a terminal struggle.`

Suggested world-end field:

> If Death consumes a full continent, black footholds appear on every continent and the last shores become a terminal struggle.

Type remains `Minor Fire-Once`.
Cluster fields remain blank / no cluster.
The suggested wording above was superseded by the implemented in-game text; [`catalog_changes_pending.md`](../../../plans/010_death_plans/catalog_changes_pending.md) holds the exact row values for the queued workbook update.

## Documentation requirements

The canonical event doc [`docs/events/010_death/overview.md`](../../../events/010_death/overview.md) exists and covers:

1. What Death is.
2. Replacement of Spirit of War/Peace.
3. Event map and subevents.
4. Origin selection.
5. State consumption and wasteland effects.
6. Hidden reports.
7. Reveal super-event.
8. Spread, withering, coastal jumps.
9. Ghost divisions.
10. Containment decisions and compact.
11. Necromancy and Herald paths.
12. World-end branch.
13. Defeat aftermath.
14. Assets and sprite expectations.
15. AI behavior.
16. Triggerable scenario.
17. Limitations or unsupported visual fields.

## Implementation acceptance criteria

Every criterion below is met at source level according to the [release completion record](../../../plans/010_death_plans/release_completion_2026-10-06.md); engine behaviour, the GUI production render, complete weighted-logic comparison, inherited art-master provenance, and the queued workbook row remain open verification items rather than missing implementation.
The criteria stay as the acceptance contract for any rework:

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
- Containment decisions use concrete costs, map objectives, the narrow hold-line mission, and AI behavior.
- The Living Containment Compact or equivalent coalition system exists after reveal.
- Dark methods, Black Oath, Herald, and Black Apostolate routes are fully implemented or hidden behind their actual prerequisites. They must not be half-visible placeholders.
- World-end requires both full continent consumption and Chaos above 1000.
- World-end footholds appear on every remaining continent.
- Whole-world consumed final super-event and achievement hooks exist.
- Death is registered as a special chaos country and actual nonhuman country.
- Assets are created, processed, converted, documented, and wired or accurately reported as pending asset work.
- Super-event text, image, audio, docs, and spreadsheet fields agree.
- AI behavior is route/stage-aware and does not pick impossible actions.
- Completion audit and localisation audit run after implementation.

## Implementation uncertainties (resolved or recorded)

- Exact island-state filters depend on available state metadata and existing state-group helpers.
- Some state building or map-visual fields may not support direct deletion/visual effects. Implementation must document exact supported representation.
- The best way to apply ticking strength loss should be chosen from existing Chaos Redux helper patterns to avoid broad daily world scans.
- Reuse and inspect the existing Death `DTH` owner package, registered in `common/country_tags/chaosx_countries.txt:5`; see [the shared identifier registry](../../shared_identifier_registry.md). Genuinely new tag proposals still require the installed-mod collision audit.
- The optional animated Zol portrait uses a real eight-frame source package, a static fallback, and registered `interface/chaosx_characters.gfx` sprite names. World-end leader gameplay uses the static fallback.
- Super-event audio and quote research was completed by the dedicated research workflow and is recorded under `docs/super_events/010_death/`.
