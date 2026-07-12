Implement the Chaos Redux GFX, icon, flag, map mode, and division symbol cleanup to completion.

Before editing, fully read and apply `AGENTS.md`, every `.agents/skills/*/SKILL.md`, `CHAOS_REDUX_MECHANICS.md`, the event, cluster, and scenario catalogs, and all relevant existing docs. Open the required offline Paradox wiki pages and vanilla HOI4 documentation for graphical assets, interface, map modes, decisions, localisation, flags, division template symbols,. Do not rely on memory for asset or UI wiring.

Required work:

1. Add biological operation icons. Search for biological warfare, bioweapon, outbreak, operation, raid, strike, stockpile, containment, and related surfaces. Create and wire dedicated icons for existing bio operation surfaces with missing, default, or generic art. At minimum, create a generic biological operations icon.

2. Fix flags with white lines. Inspect custom flags in `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. Repair the real TGA files. Do not use UI overlays, DDS display copies, scripted localisation, or other workarounds. Validate normal `82x52`, medium `41x26`, small `10x7`, correct origin, no `- top` output, correct orientation, and no white edge artifacts.

3. Fix custom map modes that do not show created icons. Audit map mode definitions, `.gui`, `.gfx`, sprite names, paths, localisation, and existing icon files. Reuse existing created icons when they are game-ready. Fix missing sprite definitions, wrong names, bad paths, bad target files, missing localisation, or wrong dimensions.

4. Add two new division template symbols in the proper HOI4 division template symbol picker surface: biowarfare and chemical warfare. Inspect vanilla and Chaos Redux patterns before adding files.

5. Add and wire the Japan chemical campaign against China decision category icon. Find the exact existing category ID first. Do not invent a new category unless the repo proves it is missing and needed.

6. Add and wire custom zombie outbreak decision category icons for every Event 002 zombie decision category that still uses missing, generic, or default category art.

7. Analyze the project for missing custom GFX. Compare referenced `GFX_` names, `.gfx` definitions, `.gui` usage, decision categories, map modes, division symbols, texture paths, localisation texticons, DDS files, and TGA files. Fix every in-scope problem. List every remaining missing sprite or texture with its reference source and expected path.

Follow `chaos-redux-event-assets`. Use `chaosx_icon_artist` with `fork_context=false` for generated icons and division symbols when available. Every new icon needs source PNG, processed PNG, DDS, manifest entry, and `.gfx` wiring. Do not use primitive placeholders, resized unrelated icons, copied focus icons, recolors, fake checkerboards, white halos, outlines, or opaque square backgrounds.

Use `chaosx_repo_explorer` with `fork_context=false` only if file locations or wiring patterns are unclear. Use `chaosx_localisation_auditor` if visible localisation changes. Run `chaosx_improvement_loop_planner` near completion only if the work expands into a meaningful design change. Otherwise state that it remained bounded GFX cleanup.

Do not claim completion until every requested asset is created, repaired, wired, documented, and validated. Final report must list changed files, created or repaired assets, sprite names, flag fixes, map mode fixes, division symbols, missing GFX audit results, meaningful validation, and every blocker, omission, or simplification. Keep iterating until the goal is fully accomplished.
