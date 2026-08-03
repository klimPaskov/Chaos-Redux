# Event 016 KRG country-idea icon wiring handoff

Date: 2026-08-03

## Scope

Parent-owned wiring for the 21-icon Kruger State country-idea extension. The package is static 2D art only; no unit model, entity, animation, gameplay, localisation, or spreadsheet surface was added.

## Changed runtime files

- `common/ideas/016_brilliant_scientist_country_ideas.txt`: added a unique `picture = brilliant_scientist_<idea_stem>` token to all 21 previously unassigned visible ideas.
- `interface/016_brilliant_scientist_idea_icons.gfx`: registered the matching `GFX_idea_brilliant_scientist_<idea_stem>` sprites and final DDS paths.
- `gfx/interface/ideas/016_brilliant_scientist/`: added 21 final 64x64 DDS textures produced by the asset subagent.

The 21 ideas are civic, machine, replication, synthesis, feudal, documented, weaponized, and fragmented portfolio administration; general staff, machine command, clone officer, project council, and project-army rivalry; automated, portal, biological, and conventional supply; prototype cannibalization; international scientific center; autonomous research network; and intellectual isolation. Existing 13 Event 016 idea/national-spirit sprites remain unchanged, yielding 34 registered Event 016 idea sprites.

## Asset evidence

The source masters, processed previews, decoded DDS previews, contact sheets, prompts, validation ledger, and sprite handoff are retained under `docs/assets/016_brilliant_scientist/krg_country_idea_icons/`. The asset handoff records unique hashes, 64x64 dimensions, transparent corners, exact BGRA DDS headers, 16,512-byte files, and pixel-equal decode checks for all 21 rows.

## Parent validation

- Static idea scan: 28 country ideas, 28 unique `picture` tokens, zero missing assignments, and zero duplicate picture tokens.
- Sprite scan: 34 unique Event 016 idea sprite names, all texture paths present, zero missing DDS references.
- Asset validation: 21/21 final DDS rows pass the subagent's header, alpha, corner-transparency, hash, and decoded-pixel checks.
- Contact-sheet review: each icon is distinct, readable at 64x64, transparent at corners, and visually consistent with the existing bronze laboratory language.
- No models, fallback textures, generic substitutions, or transform-only animated assets were introduced.

## Remaining limits

Targeted in-game idea-card presentation and broader campaign acceptance remain user-owned. The native CBRN callback blocker, quantitative balance, transfer/cleanup, Event 019 isolation, and other outstanding Event 016 validation gates are unchanged.
