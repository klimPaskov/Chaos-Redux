# 106 Resistance, Part 5: Presentation and asset direction

All newly proposed surface and asset labels in this file are working labels, not final localisation. The event name and the three evolution names come from the user. Finished prose, option wording, tooltips, and achievement titles belong to implementation and its localisation review.

## The player's view

The event should feel immediate and widespread. Occupied streets, railways, work sites, and communities become harder to control. The reports draw their tension from people acting with unexpected resolve in many places at once. They should not invent a single world resistance command or claim to know which later liberation movement will succeed.

An affected occupier sees a completed rise in resistance and the practical strain it can place on garrisons. A country with occupied cores sees local defiance and an uncertain opportunity. An observer sees the scale of the disturbance. The same report family can carry these three viewpoints without creating different gameplay outcomes.

Keep the emotional focus on occupied people and the forces trying to hold territory. Use concrete scenes and consequences. Avoid staff-table summaries, paperwork drama, staged denials, failed-broadcast clichés, invented quotations, or a narrator announcing what the player should fear.

Humour is limited to dry or self-damning reactions where the viewpoint supports them. Garrison casualties and civilian suffering receive a serious treatment. A liberation viewpoint can show guarded hope without promising a country, an army, or a successful revolt.

## Information hierarchy

The native occupation screen remains the place to inspect current resistance, compliance, and garrison needs. The event adds no persistent player-managed currency or counter.

| Information | Presentation role |
| --- | --- |
| Native current resistance | Primary local condition, visible through the existing occupation interface |
| Native compliance and garrison condition | Existing context for recovery and later uprising readiness |
| Wave addition | Transient mechanical explanation in the report or its effects tooltip |
| Locally changed and locally saturated state counts | Optional concise report facts when available from the completed wave |
| Recent local wave memory | Hidden input to cross-event behavior, explained qualitatively only when relevant |
| Wave identifiers, episode identifiers, receipt slots, raw readiness and force calculations | Internal bookkeeping |

The new persistent custom value budget is zero. Adding a new public resistance-support gauge would duplicate native occupation information and make a simple global event harder to read.

If the report has room for only one number, show the wave's nominal addition. If it also shows affected counts, distinguish eligible states from states that actually increased. A country with ten eligible states and four already at 100% has ten eligible occupations and six changed states. Do not present all ten as positive additions.

## Text surface map

| Surface | Viewpoint and tone | Required information | Dynamic context and restraint |
| --- | --- | --- | --- |
| Event identity | Clear, direct | Resistance and its event identity | Preserve the user-supplied name across the shared event list and event details |
| Occupier report | Strained control, dry or grim reaction | A worldwide surge has reached the recipient's occupations | Use recipient-relevant states only when their completed-wave facts are valid |
| Occupied-homeland report | Local resolve, guarded hope | Resistance has increased in eligible occupied cores associated with the recipient | Do not claim that an uprising has happened or that outside help is guaranteed |
| Observer report | Serious, geographically broad | Occupations across the world were affected | Avoid assigning the observer responsibility for the wave |
| Saturated result | Concrete and accurate | Eligible occupations at the cap could not rise further | A high existing resistance level still matters to later native and 095 behavior |
| Empty direct-invocation result | Brief factual acknowledgment | The firing found no valid occupied states | Give no invented target, benefit, loss, or compensation |
| Acknowledgment option | Occupier's bitter acceptance, homeland's cautious resolve, or observer's concern | Acknowledges the already applied result | Direction only, with no mechanical choice and no second wave |
| Effects tooltip | Precise and plain | Current resistance rises by the stage's points, with a 100% cap | Distinguish percentage points from relative percentage growth and from resistance target |
| Event Details premise | Evocative and readable | Occupied communities across the world act at once | Keep mechanical instructions and effect lists in the appropriate mechanical surface |
| Wave history entry | Neutral world event record | One firing, its date, and its frozen stage | Use the shared actorless world-event representation |
| Evolution history | A lasting increase in future intensity | The recorded stage and actual activation date | Do not describe the stage entry as another wave |
| Evolution preview | Readable future behavior | User stage name, activation requirement, and future addition | Preview entries have no invented history index or date |
| Relevant 095 result | Local opportunity or breakdown | Which actual affected homeland or region helped the uprising | 095 owns the outcome text, and only committed results can describe new rebels |
| Containment feedback | Measured recovery | The tracked affected territory has recovered enough for its earned Chaos reduction | Explain the outcome without revealing receipt identifiers or suggesting a spendable reward |
| Achievement text | Ambitious campaign objective | The exact containment or homeland-restoration challenge from Part 4 | Final title and description must make the frozen cohort and disqualifications understandable |
| Catalog Name and Details | Same identity and premise as the game | Final event name and final Event Details prose | Mirror final implementation wording in the authoritative workbook |

Light-parchment report bodies use plain text, including dynamic substitutions. Put required colour and icons only in surfaces whose native formatting supports them. Do not make fake tables or meters out of punctuation inside localisation.

## Evolution expression

The progression should be legible without suggesting separate powers.

| Stage | Narrative direction | Mechanical emphasis |
| --- | --- | --- |
| Baseline | Scattered local acts occur across unrelated occupations | A sudden +25-point rise can undo recent pacification |
| Rising Resistance | Defiance is more confident and harder for occupiers to contain | Future waves add 50 points |
| Mass Resistance | Whole occupied regions can become difficult to administer | Future waves add 75 points, often approaching the cap |
| Total Resistance | The surge can fill the entire native resistance scale at once | Future waves add 100 points and cap at 100% |

These are tone directions. They do not create population participation percentages, universal strikes, separate damage rolls, or new mandatory incidents. The actual campaign consequences come from native occupation mechanics and the specified consumers.

## Required visual package

Use one coherent visual motif across the report and the two achievement subjects. Reuse the same event identity through all three evolution stages. Stage names and shared evolution metadata communicate the stronger future addition.

| Working asset identifier | Consumer | Source mode | Size and output | Visual direction |
| --- | --- | --- | --- | --- |
| `report_event_106_resistance` | The ordinary Resistance report family | Generated fictional period documentary scene | Final report card 210×176, one registered report sprite | An occupied industrial street or rail district with closed shutters, a rough obstruction, and a few watchful anonymous figures. The composition conveys local defiance without a named country or real movement |
| `chaosx_106_containment_mastery` | Containment achievement | Original transparent icon subject | 64×64 completed, grey, and not-eligible variants | A reinforced rail junction or guarded lamp surviving a ring of extinguished sparks, with one strong central silhouette |
| `chaosx_106_home_recovery` | Homeland restoration achievement | Original transparent icon subject | 64×64 completed, grey, and not-eligible variants | A broken restraint opening around a small home or homeland-shaped stone, without a specific country's flag |

The two achievement identifiers are proposed stable registrations. Check for collisions before wiring them, then use those exact registered IDs for all three DDS filenames. Do not silently rename one derivative or add an asset prefix that the achievement registry does not expect.

### Report art

The report picture uses the current project's black and white documentary treatment with a sepia finish. Compose a clear central subject that survives the small card. Leave room for the deterministic processing step that supplies tilt, transparent corners, paper border, and soft shadow.

Generate the underlying fictional scene without baked-in UI, text, captions, card borders, signatures, watermarks, or a false archival label. The processor owns the card treatment. Preserve the selected source and the processed output separately.

Avoid exact modern national flags, named historical leaders, recognizable extremist insignia, and country-specific uniforms in this global image. Their presence would make one local resistance tradition stand in for every occupation. The scene can be recognizably of the game's period without making a factual claim about a photographed incident.

A historical photograph may replace the generated route only after a separately documented source choice establishes its provenance, rights, period, and fit. Do not label a generated image as historical evidence.

### Achievement triplets

Each achievement has one original transparent colour subject. Keep the subject's scale, position, and alpha alignment identical across its three source states.

The completed composition uses the supplied unchanged `achievement_template.png`. The grey composition uses a deterministic grayscale derivative of the same subject with the supplied unchanged `achievement_template_grey.png`. The not-eligible composition uses that same grey subject and the unchanged red-cross overlay with the grey template.

The templates and overlay remain 64×64 and are not regenerated. Final textures are one-level legacy BGRA DDS files with strict decoded equality to the approved composition. Preserve the subjects, composed PNGs, final DDS files, and validation evidence.

Final achievement paths are directly under `gfx/achievements/`:

- `<registered_achievement_id>.dds`
- `<registered_achievement_id>_grey.dds`
- `<registered_achievement_id>_not_eligible.dds`

Ordinary event art belongs in the event folder directly under its asset category, with `gfx/event_pictures/106_resistance/` as the proposed report destination. The current owning GFX file and actual sprite names must be verified before final registration. Existing registered names stay stable.

## Visual and text acceptance

View the actual report with an affected occupier, a valid occupied-homeland recipient, and an observer. Check the empty and saturated cases. Use a long country name and a long state name to catch clipping and awkward substitutions.

View the main evolution history, the selected firing's related evolution history, and the Event Details evolution preview separately. Historical surfaces show real recorded metadata. The preview shows the catalog of stages. Re-enabling a stage must not create a duplicate historical row.

Inspect the Resistance identity in the actual shared list and detail consumers. The pinned shared interface resolves event text through the existing row system. Verify the name, description, and evolution mappings against ID 106 so stale catalog labels cannot display unrelated content. Evidence item E07 records the inspected consumer.

Inspect every achievement state at 64×64 in the native consumer. Check the subject silhouette, grayscale treatment, red-cross alignment, alpha edges, and filenames. A large preview cannot substitute for the native-size review.

The implementation's localisation auditor checks every final surface in the table above against the numerical rules and the current world context. It also checks tone, dynamic tokens, plain-text report bodies, and the prohibition on em dashes and semicolons in authored prose.

Planning this package creates asset briefs and text directions. It does not establish that any final art, localisation, GFX registration, or in-game render has been produced.
