# Asset prompt for Event 015 Utopia Manifesto

Create the visual asset package for Chaos Redux Event 015 Utopia Manifesto. Read the full spec pack under `docs/specs/015_utopia_manifesto_specs/` first, especially part 5, part 6, and the asset matrix.

Use the correct asset subagent routing. Use `chaosx_asset_source_researcher` for real early printed Utopia imagery if the opening report image uses an archival source. Use `chaosx_generated_event_art` for fictional report images, flags, faction emblems, portraits, UI panels, and non-icon scene art. Use `chaosx_icon_artist` for focus icons, idea icons, decision icons, decision category icons, achievement icons, and small animated icon sprites. Animated work must follow `chaos-redux-frame-animation` with real source frames, static fallbacks, sheets, previews, and manifests.

Required asset groups:

- opening report event image, 210x176, sourced early Utopia or generated period documentary scene
- Need Ledger decision category icon and possible animated seal
- national spirit icons for Common Stores, Vocational Freedom, Land Need, Needful Land Doctrine, Outopia Fracture, Found Manifesto, Reading Circles, Empty Stores, Chosen Trades
- subject value icons for Local Stores, Local Consent, Vocational Acceptance, Ledger Dependence, Ward Autonomy, and Fracture Import
- decision icons for survey, storehouse, trade adoption, public occasion override, need dossier, lease request, charter settlement, renounce claim, ward survey, plebiscite, autonomous charter, needful war, store convoy, trade teachers, local warehouses, ward magistrates, household guard training, settlement congress, false dossier correction, emergency ward order, and precinct conversion
- focus icon families covering book, shelf, compass, household, plain law, public lectures, rail, harbor, guard, charter, ward, league, mandate, daughter commonwealth, subject ledgers, ultimate pillars, and no-place branch
- route cosmetic flags for Utopian Commonwealth, Eutopian League, Surveyor State, Good Place Mandate, and Outopia branch, using cosmetic-tag assets rather than replacing base country flags
- subject cosmetic flag directions for Charter Commonwealth, Surveyor Protectorate, Necessary Ward, Daughter Commonwealth, and No-Place Precinct when implementation exposes them visibly
- faction emblem for Eutopian League and optional subject network emblem
- generated fictional or symbolic leader and council portraits only when the implemented route changes leader or uses a collective body
- achievement completed icons, grey variants, and not-eligible variants for every achievement in the achievement matrix
- scripted GUI assets for the Need Ledger board or selected subject board if implemented, including static and animated states
- animated convergence seal for Ultimate Utopia when all pillars are satisfied, with static fallback
- animated Outopia seal or warning frame for hidden route reveal, with static fallback

Reference folders to inspect before asset work:

- ideas: `.agents/skills/chaos-redux-event-assets/assets/ideas`
- focuses: `.agents/skills/chaos-redux-event-assets/assets/focuses`
- decisions: `.agents/skills/chaos-redux-event-assets/assets/decisions`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/achievements`
- flags: `.agents/skills/chaos-redux-event-assets/assets/flags`
- report images: `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- super-event images: `.agents/skills/chaos-redux-event-assets/assets/super_event_images`

Do not use generated text in images. Do not generate Thomas More or any real historical person's portrait. Do not make final animation from a single filtered or shifted still. Final DDS files must live in event-scoped folders where the engine surface allows it. Achievement files are root-only under `gfx/achievements/`. Flags stay in the HOI4 flag folders.

Write `docs/assets/015_utopia_manifesto/manifest.md` and `docs/assets/015_utopia_manifesto/gfx_handoff.md`. Mark any license, source, or style uncertainty honestly.
