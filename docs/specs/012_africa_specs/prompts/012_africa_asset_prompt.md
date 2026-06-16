# Asset Prompt — Event 012 Africa

Use `chaos-redux-event-assets` and `chaos-redux-frame-animation` for every animated asset. Use the asset subagent split from `chaos-redux-subagents`:

- `chaosx_asset_source_researcher` for real/archival images, real leaders, historical flags, and attested historical symbols.
- `chaosx_generated_event_art` for generated non-icon fictional, alternate-history, symbolic, high-chaos, supernatural, UI, report/news/super-event images, fictional flags, faction emblems, and portraits.
- `chaosx_icon_artist` for focus icons, ideas/national spirits, decision icons, decision category icons, achievement icons, formable seals, and animated small icon/button sprites.

All project subagents must be spawned with `fork_context=false`; the parent prompt must include the needed paths and constraints.

## Input spec files

Read these source spec files first:

- `docs/specs/012_africa_specs/specs/012_africa_spec_part_1_core.md`
- `docs/specs/012_africa_specs/specs/012_africa_focus_tree_plan.md`
- `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md`
- `docs/specs/012_africa_specs/specs/012_africa_country_packages_and_subjects.md`
- `docs/specs/012_africa_specs/specs/012_africa_evolutions_world_end_and_scenarios.md`
- `docs/specs/012_africa_specs/matrices/012_africa_asset_matrix.md`
- `docs/specs/012_africa_specs/prompts/012_africa_achievement_prompt.md`

## Reference folders to inspect

Before producing each asset type, inspect the matching reference folder:

- Ideas/national spirits: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas`
- Focus icons: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/focuses`
- Decisions and categories: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions`
- Achievements: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements`
- Flags: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/flags`
- Report images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- News images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- Super-event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images`

If a reference folder is absent in the current checkout, record that as a blocker or use the closest existing project/vanilla pattern and say exactly which pattern was used.

## Output package

Use:

```text
docs/assets/012_africa/
  manifest.md
  gfx_handoff.md
  prompts/
  source_png/
  processed_png/
  contact_sheets/
  animations/
  notes/
```

Final DDS/TGA files must be placed in the correct mod asset folders during implementation, not only under `docs/assets`.

## Source-mode rules

Do not generate real leader portraits. Do not generate real historical flags or attested real symbols as if they were historical. Source them, document source URL, author/archive, license or public-domain status when available, and process them.

Generated art is appropriate for:

- fictional United Africa route flags;
- fictional/symbolic council portraits;
- supernatural and nonhuman high-chaos actors;
- focus, idea, decision, achievement icons;
- fictional report/news/super-event scenes;
- scripted GUI panels and animated seals.

Generated World War II-era report/news/super-event images must look period-authentic: 1936–1945 photography/press composition, period clothing, period vehicles/architecture, no modern UI, no readable generated text.

## Core report/news/super-event images

Produce or mark blocked:

1. `report_event_africa_proclamation_congress` — report event image, 210x176, generated period-documentary, opening event.
2. `news_event_africa_new_unifier` — news event image, 397x153 black-and-white, generated or sourced if a suitable non-specific congress image exists.
3. `news_event_africa_scramble_response` — news event image, 397x153 black-and-white, generated documentary/symbolic.
4. `report_event_africa_rsa_civil_war` — report event image, 210x176. If real Smuts/Allied imagery is used, source it; otherwise use generated alternate-history documentary scene.
5. `super_event_africa_is_one` — super-event image, 457x328, generated symbolic/documentary, full African unification.
6. `super_event_africa_scramble` — super-event image, 457x328, generated documentary/symbolic, outside powers react to unified Africa.
7. `super_event_africa_continent_sponsor` — super-event image, 457x328, generated symbolic/diplomatic, Africa sponsoring another continental unifier.
8. `super_event_africa_cross_continental_union` — super-event image, 457x328, generated symbolic, Afro-Asian/Afro-Eurasian dynamic union.
9. `super_event_africa_world_is_one` — super-event image, 457x328, generated high-chaos symbolic terminal branch.

## Focus icon families

Create a coordinated icon pack rather than one icon per exact focus if the final implementation uses many focuses. Each icon still must be designed for focus-icon use at 94x86, not resized from idea/decision icons.

Required focus families:

- Congress/charter icons: congress hall, charter seal, ballot, delegates, linked hands.
- Liberation icons: broken chains, rail sabotage, port uprisings, irregular columns, anti-colonial banners.
- General Staff icons: command baton, rail shield, supply depots, African shield, staff office.
- Crown Congress icons: royal stools, crowns, old city gates, trade gold, drums; source motifs if based on real symbols.
- Green Covenant icons: sacred tree, river spirit, storm, animal guardians, masks, forest court.
- Industry icons: railways, mines, ports, factories, river barges, supply hubs.
- Diplomacy/League icons: envoy papers, conference tables, radio microphones, treaty stamps.
- Diaspora icons: Atlantic ships, return papers, books, printing press, officer schools.
- Post-unification icons: continental standard, intercontinental bridges, final seal, world congress.
- RSA civil war icons: parliament split, mineworker command, Allied supply port, continental militia.

## Ideas and national spirits

Create 64x64 idea/national-spirit icons for at least:

- `idea_africa_paper_cores`
- `idea_africa_proclamation_without_machinery`
- `idea_africa_charter_league`
- `idea_africa_regional_trust`
- `idea_africa_colonial_alarm`
- `idea_africa_liberation_momentum`
- `idea_africa_congress_legitimacy`
- `idea_africa_continental_general_staff`
- `idea_africa_green_covenant`
- `idea_africa_diaspora_return_cadres`
- `idea_africa_scramble_pressure`
- `idea_africa_world_is_one_ambition`

## Decision and decision-category icons

Create 32x32 decision icons and decision-category icons for:

- Continental Congress category;
- Charter League Diplomacy category;
- Liberation War Office category;
- Regional Integration category;
- Diaspora Return Offices category;
- Green Covenant category;
- Sponsor Continent Unifiers category;
- formation/proclamation decision;
- aid corridor decision;
- integration referendum decision;
- regional administration decision;
- natural disaster warning decision;
- elephant/special unit decision;
- RSA civil-war emergency decisions.

## Flags and emblems

Produce final normal/medium/small flag assets during implementation for:

- United Africa baseline cosmetic identity;
- Federal Congress Africa route;
- People’s Liberation Front Africa route;
- Continental General Staff Africa route;
- Crown Congress Africa route;
- Green Covenant Africa route;
- Afro-Middle Eastern Union;
- Afro-Asian Union;
- Afro-Eurasian Union;
- World Is One final identity;
- 10 regional authority subject identities;
- high-chaos nonhuman/supernatural actors if implemented.

Base flags for existing countries must not be overwritten. Use cosmetic tags/route flags. Historical symbols must be sourced; fictional route flags can be generated.

## Leader and council portraits

Produce/source portraits for:

- Federal Congress council — generated institutional council portrait.
- Liberation Front chair/council — generated fictional unless a real figure is explicitly chosen by implementation, in which case source.
- Continental Marshal — generated fictional military portrait.
- Crown Congress regent/council — generated symbolic/fictional; source real dynastic symbols if used.
- Green Covenant oracle/council — generated supernatural/symbolic; animated variant recommended.
- RSA Allied continuity leader if real — sourced portrait only.
- RSA Continental Proclamation council/leader — generated fictional or sourced if a real person is deliberately used.
- Regional authority councils — mostly institutional generated portraits, one per major region if visible.
- Nonhuman/forest/tide entities — generated symbolic/nonhuman portraits with institutional names.

For generated one-person portraits, record apparent gender presentation and required matching name pool/metadata. Council or symbolic-body portraits use institutional names.

## Scripted GUI and animated assets

The Continental Congress UI needs:

- background panel;
- header plate;
- meter frames/fills for Legitimacy, Authority, Cohesion, Momentum, Regional Trust, Colonial Alarm, Paper-Core Burden, Covenant Pressure;
- regional authority cards with neutral/protected/integrating/rebellious/integrated states;
- selected target frame;
- warning border for cohesion or rebellion crisis;
- Charter seal locked/available/active/formed;
- Green Covenant seal hidden/revealed/active/critical;
- formable progress emblem incomplete/ready/formed;
- static fallback for every animated element.

Animated assets must use `chaos-redux-frame-animation`:

- `africa_charter_seal_animated`: 64x64 or current category/GUI size, 8–12 frames, slow glow/float, static fallback `GFX_africa_charter_seal`.
- `africa_cohesion_warning_border_animated`: target GUI card size, 6–10 frames, warning pulse, static fallback.
- `africa_green_covenant_seal_animated`: 64x64 or UI size, 10–16 frames, storm/river/tree glow, static fallback.
- `africa_formable_ready_emblem_animated`: target UI emblem size, 8–12 frames, availability glow, static fallback.
- Optional high-chaos leader overlay: 156x210 or overlay size, 8–12 frames, symbolic light/smoke, no real-person fake motion.

Each animated package must include source frames, processed frames, sheet PNG, sheet DDS, static fallback DDS, preview GIF for review only, contact sheet, manifest entry, and `.gfx` handoff.

## Achievements

Use `prompts/012_africa_achievement_prompt.md` for achievement icon list. Create 64x64 completed icons first; generate grey and not-eligible variants if required by the achievement system.

## Manifest requirements

For every asset, record:

- asset name;
- related event id `12` and slug `africa`;
- asset type;
- source mode;
- prompt or source URL;
- source author/archive/license/date when applicable;
- source PNG path;
- processed PNG path;
- final DDS/TGA path;
- target size;
- sprite name;
- suggested `.gfx` file;
- related focus/idea/decision/event/super-event;
- notes and status;
- for animation: frame count, FPS, loop, state logic, static fallback, sheet path, preview path.

## Completion standard

No asset is complete unless the final DDS/TGA exists in the intended gameplay folder, dimensions are verified, transparency/orientation is correct, the manifest is updated, and `gfx_handoff.md` gives exact sprite names and target `.gfx` snippets or paths.


## Revision 2 expansion requirements

Also implement the expanded source files:

- `specs/012_africa_niche_polities_and_subjects.md`
- `specs/012_africa_high_chaos_absurd_paths.md`
- `matrices/012_africa_expanded_subject_matrix.md`
- `matrices/012_africa_absurd_high_chaos_routes_matrix.md`

The implementation must add the Legacy Authority Lane, Authority Register decisions, Integration Temperature/trust/resistance model, Priority A historical authorities, as many Priority B authorities as needed for regional depth, and high-chaos Covenant actors with explicit nonhuman/supernatural classification. Do not collapse this into generic modifiers, placeholder tags, or one broad “native authority” subject.


## Revision 2 asset prompt detail

The asset worker must inspect the relevant reference folders before producing icons, flags, report images, super-event images, and animations. Historical flags/symbols for legacy authorities require sourced or source-reviewed treatment. Generated art is allowed for fictional council portraits, fictional route flags, supernatural courts, animal/nonhuman countries, symbolic seals, and high-chaos report/super-event images.

New asset groups:

1. **Legacy authority seals:** one seal family for each Priority A subject and regional variants for Priority B.
2. **Authority Register UI:** target cards, selected/locked/available states, authority trust indicator, integration temperature icon, observer/subject/partner/covenant status badges.
3. **Green Covenant UI:** Covenant Pressure, Wild Mandate, Human Legitimacy, Omen Reliability icons and animated state frames.
4. **Nonhuman leader/council portraits:** generated fictional portraits for Gorilla Nation, Chimpanzee Assembly, Bonobo Congress, Great Herd, Crocodile Admiralty, Hyena Radio Dominion, Termite Engineers, Baobab Senate, Locust Customhouse, Giraffe Signals, Okapi Secret State.
5. **Supernatural council portraits:** Orisha Court, Ananse Web, Mami Wata Tidemark, Bird of the Walls.
6. **Disaster warning report/news images:** flood warning, lightning court, forest refusal, locust customhouse, termite subsidence, port tide warning, false omen panic.
7. **Animated sprites:** Green Covenant seal, Omen Reliability warning pulse, Forest Parliament canopy overlay, Orisha Court bench seal variants, Mami Wata tide shimmer, Ananse web-line target card, Bird of the Walls route emblem.

## Archive of Old Seats and Bestiary expansion assets

Also create/source/plan assets for `specs/012_africa_niche_country_expansion.md`.

Required additions:

- Dossier UI/category visuals for Restoration Dossiers, Archive Mandate, Old-Seat Legitimacy, Local Sovereignty, Restoration Debt, Mythic Pressure, Nonhuman Sovereignty, and Bestiary Alarm.
- Focus icon family for Archive of Old Seats: opener, regional files, Rivers and Crowns, Stone and Stelae, Desert Books, Lake Courts, Coastal Ledgers, Respect the Old Seats, Counterfeit Crown, Central Archive, Bestiary Clause, Parliament/Root-and-Fang route label.
- Decision icons for surveying old seats, chartering local offices, protecting regalia, raising local guards, settlement, forgery crisis, nonhuman observer seats, and supernatural sanctions.
- Historical dossier seal/flag source review for high-priority packages: Kush/Meroe, Aksum/Zagwe, Kilwa/Swahili port league, Great Zimbabwe/Mutapa/Rozwi, Manden/Songhai, Asante/Fante, Oyo/Ife/Benin, Kongo/Loango, Ndongo/Matamba, Luba/Lunda/Kuba, Buganda/Bunyoro, Merina/Sakalava.
- Generated fictional/nonhuman portraits and seals for Gorilla Highlands Council, Chimpanzee Marshes, Bonobo Glasshouse Court, Okapi Court, Crocodile Rivers, Baobab Senate, Termite Surveyor Republic, Honeyguide Commons, Lion Arbitration Circuit, Great Forest Federation, Great Herds Compact, Dust Senate, Tidemark Dominion, Masks That Vote, Ananse Ledger, and Orisha/Vodun/Nature Courts.
- Animated UI packages where useful: forgery exposure warning pulse, Bestiary Alarm warning frame, Archive seal available glow, Parliament of Root and Fang route seal. Follow `chaos-redux-frame-animation`; no transform-only animation.
- Achievement icons for all Archive/Bestiary achievements added to the achievement matrix.

Historical flags, symbols, and real portraits are source-mode assets and must not be generated as final historical assets. Nonhuman, supernatural, and impossible legal-body assets are generated fictional assets.


## Leader portrait and asset naming note

Leader, council, nonhuman institutional, flag, and route-reveal assets use neutral filenames and sprite names. Any source-language joke names belong in localisation, not in generated images, filenames, sprites, or readable asset text. Do not generate readable text in the image.

