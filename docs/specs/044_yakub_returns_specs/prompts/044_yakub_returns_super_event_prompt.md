# Super-event research and production prompt for Event 044 Yakub Returns

Use `chaos-redux-super-events`, `chaos-redux-event-assets`, `chaos-redux-events`, `chaos-redux-subagents`, and the repository research rules in `AGENTS.md`.

Read the full Event 044 specification package under `docs/specs/044_yakub_returns_specs/`, especially spec parts 4 and 6, the research notes, the asset prompt, and the acceptance criteria.

Event 44 has two accepted super-event roles:

1. Terminal activation of `The Yakubite World`.
2. Defeat aftermath after a genuine global campaign against the terminal order.

Do not add super-events for the first appearance, Evolution I, state formation, Evolution II, International formation, or routine schism. Those moments use normal events or news events.

## Research gate

All titles, descriptions, button text, quotations, cultural remarks, slogans, allusions, lyric fragments, and audio choices in this prompt are directions only. None is final localization.

Use web research to verify every final quotation and cultural reference. Record exact wording, author or speaker, work or speech, year when known, source, attribution confidence, copyright status where relevant, and why it fits.

Use public-domain or clearly licensed musical recordings. Verify composition and recording rights separately. Record title, composer, performer or recording source, source, license, duration, attribution, editing, and uncertainty.

Unresearched or uncertain text and audio remain blocked. Do not invent a quotation, misattribute a line, use an unsourced internet quote, use long copyrighted dialogue or lyrics, or substitute default audio.

## Super-event 1: The Yakubite World

Role:

World-end activation. A viable Yakubite state and functioning International commit to replacing the existing international order after 1000 or more Chaos and route-specific geopolitical readiness.

Trigger meaning:

The moment is larger than Yakub's appearance, state formation, or International formation. It marks terminal commitment, assignment of supporting and opposing governments, and the beginning of global subversion, uprisings, diplomacy, and war.

Core tone:

Political mass mobilization, ideological certainty, state ceremony, revolutionary urgency, and irreversible global conflict. The game must keep the doctrine attributed to the faction.

Produce route-specific presentation variants under one public terminal branch:

### Supremacist variant

Direction:

Rigid authoritarian congress, security formations, coerced accessions, exclusionary citizenship, loyalty ceremonies, and a state claiming racial inversion as destiny. Objective text must identify Black supremacy as the state's extremist ideology and show oppression, resistance, defections, and instability.

Quote research themes:

racial hierarchy, tyranny, domination, pride, inversion, false destiny, and the dangers of replacing one hierarchy with another.

Cultural remark direction:

cold authoritarian confidence or grim recognition by the outside world. Avoid slogans that can function as real-world recruitment material.

### Federal variant

Direction:

A congress of member governments creating a transnational federation, combining self-rule with common defense and economic institutions.

Quote research themes:

federation, self-government, union, national freedom, constitutional order, and the cost of shared sovereignty.

Cultural remark direction:

formal proclamation or restrained recognition that a new order has become real.

### Revolutionary anti-colonial variant

Direction:

Liberated capitals, anti-colonial armies, strikes, uprisings, volunteers, and governments collapsing under a coordinated international wave.

Quote research themes:

colonial liberation, revolution, empire, freedom, armed struggle, and the danger of revolution becoming domination.

Cultural remark direction:

period revolutionary cadence or bitter imperial recognition, with exact source checks.

### Congress variant

Direction:

Mass organization, diplomacy, negotiated accession, relief networks, and a central assembly claiming global authority through coalition rather than one doctrine.

Quote research themes:

assembly, representation, political solidarity, self-determination, and fragile international agreement.

Cultural remark direction:

measured diplomatic finality, not generic triumph.

### Religious commonwealth variant

Direction:

Ceremonial leadership, temples or movement institutions, public devotion, member governments, and a transnational political-religious order.

Quote research themes:

false prophets, revelation, faith and power, political religion, judgment, and obedience.

Cultural remark direction:

scriptural or religious register only after exact source and context checks. Do not present Yakubite theology as mainstream Islam.

Image coordination:

Produce one `457x328` image per route variant through the asset workflow. Use generated alternate-history documentary or painted-news imagery. Keep visual differences clear enough for the scripted image selector.

Audio:

Research one unique final musical cue for this super-event. It may serve every route variant only if it fits the full range and the shared use is documented as one super-event package. If one cue cannot represent all forms, propose a bounded route-specific set with distinct IDs and complete source documentation. Do not use drones, stingers, generated tones, simple ambience, test signals, or unlicensed commercial recordings.

Runtime requirements:

- one public Event Details world-end row and toggle
- one terminal super-event slot chosen intentionally
- route-aware title, description, button, quote, and image selectors where the final research package varies
- unique audio ID or approved bounded route IDs
- base sound and settings-volume wrappers
- `global.current_super_event_audio_id`
- `play_current_super_event_sound = yes`
- scenario and automatic terminal paths use the same presentation contract

## Super-event 2: defeat of the terminal order

Role:

Defeat aftermath after a real world-scale conflict. It should not fire after a small containment action or immediate scenario failure.

Trigger meaning:

The terminal actor has been defeated, the International military command has been dismantled or dissolved, successor and member outcomes are resolved, and the campaign enters reconstruction or a new settlement.

Tone:

Reflective, exhausted, political, and specific. The text should recognize survivors, dismantled institutions, released states, trials or settlements, unresolved self-determination, and the danger of restoring old colonial or racial hierarchies.

The defeat text must not frame the war as victory over Black people, Black self-government, or Islam. It is the defeat of a particular terminal political order.

Quote research themes:

memory, responsibility, rebuilding, the cost of victory, vigilance, tyranny, reconciliation, and unfinished freedom.

Cultural remark direction:

restrained aftermath language, a short historical or literary allusion, or an understated reaction. Avoid celebratory mockery.

Image direction:

Dismantled International command offices, released delegations, broken military banners, exhausted cities, public records, and reconstruction. Produce one main `457x328` image. Add route-aware variants only if the implementation and research show a material need.

Audio:

Research a second unique musical cue, separate from the terminal activation cue. It should be reflective and structured, not a pure sound effect or ambient bed.

Runtime requirements:

- separate super-event slot or verified shared framework slot with distinct visibility state
- unique image and text selectors
- unique audio ID and settings-aware playback
- trigger guard proving a global campaign and resolved defeat
- documentation of settlement prerequisites

## Required outputs

Create or update:

- `docs/super_events/044_yakub_returns_super_event_research.md`
- researched final localization handoff for both super-events and route variants
- quote candidate matrix and final selection with confidence
- cultural remark candidate matrix and final selection
- audio candidate matrix and final selection
- downloaded source audio preservation in the temporary event workspace
- final game-ready WAV files under `sound/044_yakub_returns/`
- sound definition and wrapper handoff
- image handoff to the Event 044 asset package
- slot, visibility, scripted-localization, and event-effect wiring handoff
- updates required for `music/chaosx_music_track_list.html`
- source, license, duration, path, ID, and conversion documentation

Do not mark either package complete until image, text, quote, remark, audio, trigger, settings-aware playback, documentation, and catalog wording all refer to the same campaign moment.
