# Event 020 Rat Country Package Alias Patch Handoff

## Scope

This handoff records the bounded country-package audit and the two load-time idea-reference repairs for the RTA–RTM Rat Nation slots and the RTX Rat King shell.

The package remains a dormant finite-pool country package whose ownership, state transfer, leader creation, pulses, merger cleanup, and Rat King transfer are runtime-owned by the Event 020 scripted effects.

## Changed files

- `common/national_focus/020_black_plague_rat_king_focus_tree.txt:72` now adds the registered `black_plague_rat_king_dominion` idea when `black_plague_rat_king_first_decree` completes.
- `common/decisions/020_black_plague_rat_decisions.txt:87` now adds the registered `black_plague_rat_dominion` idea when `black_plague_rat_harden_the_immune_blood` completes.

The prior identifiers `black_plague_rat_crowned_brood` and `black_plague_rat_plague_mastery` were not defined in `common/ideas/020_black_plague_rat_ideas.txt` and had no localisation or registered sprite.

These are parent-approved semantic content aliases to the closest currently registered ideas, not new bespoke spirit implementations.

## Before and after behavior

Before the patch, the two focus or decision rewards attempted to add undefined ideas and could leave the reward path invalid at load or completion time.

After the patch, both rewards resolve to registered package ideas with existing localisation and `GFX_idea_*` sprites.

The dedicated `Crowned Brood` and `Plague Mastery` spirit identities described by the Event 020 design remain deferred content and are explicitly not claimed as implemented here.

## Country package coverage

- `common/country_tags/020_black_plague_rat_countries.txt` registers 14 unique tags: RTA–RTM plus RTX.
- `common/countries/020_black_plague_rat_country.txt` supplies the shared country shell and eastern graphical cultures.
- `history/countries/RTA...RTM` and `history/countries/RTX - Rat King.txt` provide dormant shell politics, capital placeholder, zero research slots, and the shared `020_black_plague_rat_1936` OOB reference.
- `history/units/020_black_plague_rat_1936.txt` defines five locked templates, while runtime effects add and lock `Royal Rat Guard`.
- `common/units/020_black_plague_rat_units.txt` defines six inactive zero-manpower rat sub-units used only by scripted creation.
- `common/ideas/020_black_plague_rat_ideas.txt` currently registers four ideas: `black_plague_rat_brood_instinct`, `black_plague_rat_no_civilian_economy`, `black_plague_rat_dominion`, and `black_plague_rat_king_dominion`.
- `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` supplies brood archetype and King AI strategies with rat template priorities and front behavior.
- `interface/020_black_plague_rat_identity.gfx` registers all current custom focus, idea, and portrait sprites.
- `localisation/english/020_black_plague_rat_countries_l_english.yml`, `020_black_plague_rat_focus_l_english.yml`, and `020_black_plague_rat_decisions_l_english.yml` are UTF-8 with BOM and cover the current country, focus, decision, leader, unit, template, and idea keys.
- Normal, medium, and small TGA flags exist for all 14 tags at 82x52, 41x26, and 10x7 pixels respectively, with distinct hashes per tag and size.

## Validation evidence

- Static package scan found 14 unique registered tags, one matching country shell, one history file per tag, and an existing `history/units/020_black_plague_rat_1936.txt` OOB.
- Focus localisation scan found 23 base-tree focuses and 38 King-tree focuses with no missing title or description keys.
- Decision localisation scan found all 12 decision IDs and both category keys covered by `020_black_plague_rat_decisions_l_english.yml`.
- Focus icon scan found 17 base-tree and 25 King-tree icon tokens with no missing sprite token across mod and vanilla interface GFX files.
- Decision icon scan found all 10 decision icon tokens across mod and vanilla interface GFX files.
- Idea picture scan found all four registered idea pictures mapped to `GFX_idea_*` sprites in `interface/020_black_plague_rat_identity.gfx`.
- Identity texture scan found all 20 custom goal, idea, and portrait texture paths present on disk.
- TGA header scan found all 42 flag files with expected dimensions and no missing or malformed files.
- The read-only focus inspection was run after the alias patch and before the parent normalized the King-tree alternative prerequisites, returning artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aad9c5e9901703cc022a92a19c20758348b91ec3ac9e7d725e227565945088b8/7ecc09f9f11ed0c2081c0e25cc12a764054f16d1038df91a7aab838ed7d198e2/focus-inspect.d7e271d003034934.json`.
- The parent has since replaced the explicit nested `OR` prerequisite groups with repeated `prerequisite = { focus = ... }` blocks, matching the offline National focus modding reference, so the two old malformed-group diagnostics are superseded.
- The focus inspector also reports vanilla generic icon references as missing because its scan does not resolve the installed game's interface sprites; a direct mod-plus-vanilla GFX scan resolved every icon token, so those remaining inspector diagnostics are tool limitations rather than source defects.
- A post-normalization read-only focus inspection returned artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61221121c6be4a5d4bdaa6cd002339b2ed2817362e2993f549221d66815f83a1/3bdef54c198ec3cd4f77737f64207f83ce5630a80be11586db78044e65f950db/focus-inspect.da54592a41f60fd8.json` with 38 focuses, zero malformed prerequisite diagnostics, and only the same unresolved generic vanilla icon reports.
- The installed package exposes no Technology Tree Viewer, so technology dependency and unlock inspection remains unresolved.

## Remaining setup and identity risks

- Country history is intentionally dormant with `capital = 1` and no static owner; runtime `black_plague_rat_create_from_state` must transfer a valid host state, add the core, and set the capital before the shell is playable.
- Research slots remain zero by design and no separate rat technology package or production setup exists; scripted zero-manpower, zero-equipment unit creation is the intended military path.
- The custom sub-units are inactive and have no `need` block, so ordinary recruitment and equipment production are intentionally unavailable.
- Parent-owned runtime code still deserves review for timed-flag duration values passed through variables in `common/scripted_effects/020_black_plague_rat_effects.txt:717` and `:779` against the vanilla effects documentation.
- Bespoke `Crowned Brood`, `Plague Mastery`, and other deeper spirit lifecycle content remains deferred, along with any separate idea icons for those identities.
- Bespoke rat 3D models and entity wiring remain deliberately deferred by the parent scope.
- The older `2026-07-24_rat_system_country_package_audit.md` handoff predates the current package and should be treated as superseded where it claims missing tags, assets, or slot cleanup.

## Parent review request

Please stage the two source changes and this handoff with the cohesive Event 020 package commit, and preserve the alias/deferred-content note in the final completion report.
