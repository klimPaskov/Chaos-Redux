# Asset production prompt for Event 044 Yakub Returns

Use `chaos-redux-event-assets`, `chaos-redux-frame-animation` only if a later approved animation is added, `chaos-redux-super-events` for super-event coordination, and `chaos-redux-subagents`. Character portraits follow the `chaos-redux-event-assets` portrait-production reference. Route every portrait to `chaosx_portrait_creator`, generated scene art and fictional flags to `chaosx_generated_event_art`, and gameplay icons to `chaosx_icon_artist`.

Read the complete specification package under `docs/specs/044_yakub_returns_specs/`, especially spec part 6, the country package matrix, focus architecture, achievement prompt, and super-event prompt. Inspect the canonical vanilla reference library and every exact consumer before production.

## Source-mode rules

Yakub and any approved fictional one-person successor are fictional high-chaos subjects and may use native ImageGen through the portrait worker. Real Nation of Islam leaders, civil rights leaders, Pan-African intellectuals, Muslim leaders, anti-colonial activists, and historical officials must not receive generated identities or invented event allegiance.

All flags use ImageGen source evidence. Any historically informed flag or attested symbol begins with cited design research, then receives a clean flat reconstruction. No flag may show fabric, folds, a flagpole, scenery, perspective, gradients, lighting, fake text, or invented heraldry.

Generated report, news, category, and super-event art should use period-authentic 1930s to 1940s documentary or illustrated-news style. Avoid modern equipment, modern city skylines, modern microphones, cinematic grading, readable generated text, racial caricature, pseudo-scientific race diagrams, grotesque anatomy, meme depictions of Yakub, and celebratory imagery of racial domination.

Every alpha-backed icon family requests real native transparency in the first ImageGen call and preserves alpha through DDS conversion. Background removal is fallback-only and must be documented.

## Portrait package

Create a complete `156x210` leader portrait for Yakub.

Suggested runtime basename:

`portrait_044_yakub`

Suggested runtime folder:

`gfx/leaders/044_yakub_returns/`

Visual direction:

- serious Black male political-religious organizer
- mature adult
- composed and authoritative expression
- period suit or restrained ceremonial scholarly clothing
- 1930s or early 1940s setting
- distinctive silhouette that remains plausible
- no modern accessories
- no racial diagram, laboratory proof device, grotesque anatomy, caricature, meme styling, or readable text

Create fictional successor portraits only after the country and focus implementation locks a one-person leader. Institutional outcomes should use institutional portraits or people-free council art. Potential packages are Designated Messenger, Defense Council chair, and International Secretariat chief. Do not pre-generate optional characters without an accepted consumer.

Inspect:

- `assets/vanilla_reference/portraits/leaders/`
- `assets/leader_portraits/`

No advisor or high-command dossier portrait family is authorized by this prompt unless the implemented focus tree explicitly adds named advisors and the parent expands the requirement set.

## Country flags

The final tag is unknown until the required installed tag collision audit. Register runtime filenames only after the tag is locked.

Required American state identity variants:

1. Base provisional New Nation flag.
2. Founder-led Personal Revelation flag.
3. Federal New Nation flag.
4. Secular Black Republic flag.
5. Original Supremacy flag.
6. Diaspora Congress flag.
7. International headquarters cosmetic identity when the implementation uses one.
8. Terminal cosmetic identity only where the public country identity changes.

Every implemented regional breakaway needs normal, medium, and small flags grounded in its local module. Do not reuse the American flag for Caribbean, Brazilian, British, French, West African, South African, Ethiopian, or Liberian actors.

Final sizes:

- normal `82x52`
- medium `41x26`
- small `10x7`

Inspect:

- `assets/vanilla_reference/flags/normal/`
- `assets/vanilla_reference/flags/medium/`
- `assets/vanilla_reference/flags/small/`

## Faction emblem

Create one Yakubite International emblem with a clear silhouette at faction UI size. Produce route variants only when the International's public institutional identity changes enough to require them.

Suggested basename:

`044_yakubite_international_emblem`

Suggested sprite:

`GFX_044_yakubite_international_emblem`

The emblem should communicate congress, transnational organization, Black self-government, and institutional authority. Avoid direct copies of modern organization logos and avoid racial pseudo-science.

Inspect:

`assets/vanilla_reference/icons/factions/`

## Report-event images

Create generated `210x176` report images for the following accepted scenes. Several related subevents may share an image when the setting and action remain the same.

1. `044_yakub_first_appearance`
   - Yakub speaking in a Detroit meeting hall with press, followers, and discreet observers.
2. `044_federal_chapter_surveillance`
   - period investigators mapping chapters and financial links.
3. `044_parallel_institutions`
   - school, food network, printing press, or cooperative administration.
4. `044_failed_arrest`
   - confused raid, crowd pressure, police vehicles, and a movement escaping or producing a martyr crisis.
5. `044_constitutional_compact`
   - American and movement delegates negotiating territorial status.
6. `044_unilateral_secession`
   - improvised government taking control of offices, depots, and streets.
7. `044_founding_convention`
   - delegates choosing the state's political direction.
8. `044_caribbean_chapter`
   - locally grounded Caribbean religious and anti-colonial organizing.
9. `044_brazilian_chapter`
   - civic school, legal defense, and political association in an urban Brazilian setting.
10. `044_colonial_chapter`
   - one West African or European imperial module scene with clear local specificity.
11. `044_international_congress`
   - delegations, radio offices, relief maps, and member flags.
12. `044_international_schism`
   - divided congress, delegations leaving, and rival security groups.
13. `044_originalist_loyalty_state`
   - authoritarian loyalty ceremony, surveillance, or ideological education without celebratory racial domination.
14. `044_terminal_mobilization`
   - international columns, uprisings, and delegations committing to global conflict.
15. `044_terminal_defeat`
   - dismantled command offices, released members, and exhausted survivors rebuilding.

Suggested sprite form:

`GFX_report_event_<basename>`

Inspect:

`assets/vanilla_reference/event_art/report/`

## News images

Create black-and-white `397x153` news images only for campaign moments that receive news events:

- Yakubite state formation
- Yakubite International formation
- International schism when it changes world politics
- negotiated peaceful partition when it creates a sovereign state

Suggested basenames:

- `044_news_new_nation_formed`
- `044_news_international_formed`
- `044_news_international_schism`
- `044_news_peaceful_partition`

Inspect:

`assets/vanilla_reference/event_art/news/`

## Decision category pictures

Create one static category picture for the American crisis on the active consumer's verified canvas. The reference family currently uses `114x101`, but inspect the actual runtime sprite and GUI before final sizing.

Suggested basename:

`044_yakubite_crisis_category`

Suggested sprite:

`GFX_decision_category_044_yakubite_crisis`

Scene direction:

Yakub at a meeting hall podium, followers and journalists in front, government observers at the edge, Detroit industry outside or implied. Do not paint buttons, values, meters, labels, state pieces, or fake controls into the art.

Optional replacement category pictures may be produced only after the implementation confirms long-lived consumers:

- `044_new_nation_government_category`
- `044_yakubite_international_category`
- `044_original_supremacy_category`

Inspect:

`assets/vanilla_reference/icons/decision_categories/pictures/`

If the family contact sheet is missing, create and catalog it before production. Never wire reference images into runtime files.

## Decision and category icons

Create separate `32x32` decision icons for implemented action families. Pre-register stable basenames before production.

Required families:

- chapter surveillance
- informants and infiltration
- finance audit
- public employment and housing
- monitored organization
- arrest operation
- constitutional talks
- legal separatist charter
- federal corridor security
- local government protection
- territorial compact
- general suppression
- school and relief institutions
- movement business network
- community defense
- state arsenal
- foreign chapter organizing
- legal defense abroad
- aid corridor
- International congress
- International intelligence
- volunteers
- member discipline
- doctrinal conformity
- federation
- terminal commitment

Create a distinct decision-category icon with a movement emblem, podium, or meeting-hall motif.

Inspect:

- `assets/vanilla_reference/icons/decisions/`
- `assets/vanilla_reference/icons/decision_categories/`
- `assets/vanilla_reference/icons/missions/` for mission art

## Idea and national-spirit icons

Create separate `64x64` icons for:

- Disputed Revelation
- Parallel Institutions
- Improvised National Defense

Create additional route or stage idea icons only for persistent ideas actually implemented. Staged versions should use a coordinated family and not become unrelated artwork.

Likely route families:

- founder authority
- federal constitutional order
- secular republican institutions
- Originalist directorate
- Diaspora Congress
- International Cohesion or headquarters
- negotiated partition
- movement remnant or underground network

Inspect:

`assets/vanilla_reference/icons/ideas/`

## Focus icons

Every implemented focus needs an accurate `94x86` focus icon. Build coordinated but distinct families for:

- founding emergency and capital security
- food, schools, welfare, press, and cooperative institutions
- Personal Revelation
- Federal New Nation
- Black Republic
- Original Supremacy
- Diaspora Congress
- industry and state-directed production
- community defense, army professionalization, and arsenals
- diplomacy, recognition, and guarantees
- intelligence and internal security
- territorial integration and formables
- International offices and Cohesion
- terminal preparation and route commitment

Do not resize idea or decision art into focus icons. Do not use pseudo-scientific racial imagery for the Original Supremacy route. Show ideology through administration, loyalty, education, surveillance, exclusionary law, and hierarchy.

Inspect:

`assets/vanilla_reference/icons/national_focus/`

## Achievement icons

Create completed `64x64` source art and required grey and not-eligible variants for all eight achievements:

1. `044_no_martyrs`
   - open case file, intact courthouse, lowered microphone or torch.
2. `044_the_peaceful_partition`
   - two hands over divided but connected industrial territory.
3. `044_a_nation_before_a_state`
   - school, food basket, printing press, courthouse, and shield as one compact institution symbol.
4. `044_the_congress_holds`
   - regional emblems around a congress table.
5. `044_doctrine_without_dominion`
   - open book, broken chain, and independent flag.
6. `044_the_founder_is_gone`
   - empty chair before a lit congress emblem.
7. `044_the_inversion`
   - severe inverted crown or hierarchy with cracked foundations, framed as an extremist-route challenge.
8. `044_every_temple_empty`
   - abandoned congress hall, broken banners, and daylight, without destruction of civilians or indiscriminate religious imagery.

Final achievement filenames must match the final achievement IDs and remain directly under `gfx/achievements/` as required by the engine convention.

Inspect:

`assets/vanilla_reference/icons/achievements/`

## Super-event image coordination

Coordinate with `prompts/044_yakub_returns_super_event_prompt.md`.

Create `457x328` super-event images for:

- The Yakubite World terminal activation, with route-specific visual variants for supremacist, federal, revolutionary, congress, and religious commonwealth forms.
- Defeat of the terminal order, with one main global-aftermath image and optional route-aware variants only when the research package and runtime selector justify them.

Suggested sprite family:

- `GFX_super_event_044_yakubite_world_supremacist`
- `GFX_super_event_044_yakubite_world_federal`
- `GFX_super_event_044_yakubite_world_revolutionary`
- `GFX_super_event_044_yakubite_world_congress`
- `GFX_super_event_044_yakubite_world_commonwealth`
- `GFX_super_event_044_yakubite_world_defeated`

Inspect:

`assets/vanilla_reference/event_art/super_event/`

## Animation and 3D scope

No animation is authorized for the accepted package. Do not create animated portraits, animated category pictures, frame sheets, or leader overlays as polish.

No custom 3D model, unit family, sound package, or counter package is required. The state's army uses ordinary period units and equipment.

## Packaging and manifests

Use a temporary event workspace under:

`docs/assets/044_yakub_returns/`

Every asset row needs:

- stable asset ID
- exact asset type
- target size
- source mode
- source path or ImageGen prompt evidence
- native transparency status where relevant
- source and final checksums
- final PNG and DDS paths
- proposed sprite name
- runtime consumer
- reference folder inspected
- reviewer and status
- blocker or exception note

Create contact sheets by asset family. Keep icon families separate. Validate small-size readability, alpha, alignment, and route distinction.

Before final event completion, move runtime assets into event-scoped engine folders, wire every consumer, promote durable provenance and coverage facts into permanent event documentation, confirm no runtime reference points into `docs/assets/`, and delete the temporary event workspace. Retain it while any asset is blocked or awaiting review.

Do not claim asset completion while a required flag, portrait, icon, report image, category picture, super-event image, or manifest row is missing, generic, unwired, or a placeholder.
