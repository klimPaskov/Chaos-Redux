# Decision category pictures and formable state-puzzle completion report

## Outcome

The decision-category presentation audit covers the complete 296-id baseline union.

Nine categories received static pictures: three archival and six generated.
No category received an animated picture because none of the accepted additions needed motion to communicate its state.
No full mechanic window was selected.

Twenty-one fixed-state, single-formation formable categories received compact live state-puzzle displays.
The package contains 21 manifests, 392 state entries, and 784 unresolved/qualifying DDS sprites.
The other 27 formable categories retain static presentation for explicit applicability reasons documented in `docs/formable_state_puzzle_system.md`.

## Skills and routed ownership

- `chaos-redux-decisions-missions` governed category, formable, helper, tooltip, and scripted-GUI implementation.
- `chaos-redux-event-assets` governed the reference family, archival/generated art, DDS processing, manifests, and GFX handoffs.
- `chaos-redux-event-planning` governed consumer selection, layout ownership, and implementation handoff structure.
- `chaos-redux-subagents` governed context-free routing and parent review.
- `chaosx_asset_source_researcher` sourced and documented the three archival pictures.
- `chaosx_generated_event_art` created and documented the six generated pictures.
- `chaosx_icon_artist` produced the exact-geometry state-piece packages.
- `chaosx_scripted_system_architect` extracted the shared eligibility helpers and migrated the 21 decision gates.
- `chaosx_decision_mission_auditor` performed the final independent decision review.

`chaos-redux-frame-animation` was not invoked because animation was not selected.

## Reference family and reusable template

The canonical review-only reference family is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/`.
It contains the 13 user-provided 114x101 PNGs and a labeled `contact_sheet.png`.
The family is documented in the reference `README.md` and `CATALOG.md` and is not referenced by runtime GFX.

The reusable template is `.agents/skills/chaos-redux-decisions-missions/templates/formable_state_puzzle/`.
It contains the required README, schema, filled manifest, GUI, GFX, scripted-GUI, scripted-trigger, scripted-effect, scripted-localisation, localisation, static-picture alternative, and validation checklist.
The skill-local files are scaffolding only and are not runtime consumers.

## Static decision-category pictures

| Category | Source layer | Sprite |
| --- | --- | --- |
| `chaosx_communism_fight_category` | Archival | `GFX_decision_cat_picture_communist_insurgency` |
| `chaosx_space_race_decision_category` | Archival | `GFX_decision_cat_picture_space_race` |
| `chaosx_greenland_sale_category` | Archival | `GFX_decision_cat_picture_greenland_sale` |
| `brilliant_scientist_aftermath_treaty_category` | Generated | `GFX_decision_cat_picture_brilliant_scientist_aftermath_treaty` |
| `chaosx_ufo_decision_category` | Generated | `GFX_decision_cat_picture_antarctic_ufo_race` |
| `chaosx_mass_panic_decision_category` | Generated | `GFX_decision_cat_picture_mass_panic` |
| `chaosx_africa_gods_decision_category` | Generated | `GFX_decision_cat_picture_africa_gods` |
| `chaosx_master_decision_category` | Generated | `GFX_decision_cat_picture_the_master` |
| `air_cleanliness_treaty_category` | Generated | `GFX_decision_cat_picture_air_cleanliness_treaty` |

The nine exact texture paths are registered in `interface/chaosx_decision_category_pictures.gfx`.
Every final DDS is 114x101, matching the active `countrydecisionview.gui` consumer.
Archival provenance is in `archival_picture_handoff.md`; generated prompts and checksums are in `generated_picture_handoff.md`.

## Live formable displays and eligibility helpers

| Category | Formation id | Territory helper | Manifest owner | States |
| --- | --- | --- | --- | ---: |
| `form_scandinavia_category` | `form_scandinavia` | `chaosx_formable_form_scandinavia_territory_qualifies` | `form_scandinavia_category` | 29 |
| `form_north_sea_category` | `form_north_sea_empire` | `chaosx_formable_form_north_sea_empire_territory_qualifies` | `form_north_sea_category` | 28 |
| `form_baltic_sea_empire_category` | `form_baltic_sea_empire` | `chaosx_formable_form_baltic_sea_empire_territory_qualifies` | `form_baltic_sea_empire_category` | 41 |
| `form_gran_colombia_category` | `form_gran_colombia` | `chaosx_formable_form_gran_colombia_territory_qualifies` | `form_gran_colombia` | 11 |
| `form_commonwealth_category` | `form_commonwealth` | `chaosx_formable_form_commonwealth_territory_qualifies` | `form_commonwealth` | 17 |
| `form_united_netherlands_category` | `form_united_netherlands` | `chaosx_formable_form_united_netherlands_territory_qualifies` | `form_united_netherlands` | 8 |
| `form_baltic_federation_category` | `form_baltic_federation` | `chaosx_formable_form_baltic_federation_territory_qualifies` | `form_baltic_federation_category` | 14 |
| `form_mutapa_category` | `form_mutapa` | `chaosx_formable_form_mutapa_territory_qualifies` | `form_mutapa` | 14 |
| `form_rattanakosin_kingdom_category` | `form_rattanakosin_kingdom` | `chaosx_formable_form_rattanakosin_kingdom_territory_qualifies` | `form_rattanakosin_kingdom` | 9 |
| `form_turkestan_category` | `form_turkestan` | `chaosx_formable_form_turkestan_territory_qualifies` | `form_turkestan` | 21 |
| `form_mountainous_republic_category` | `form_mountainous_republic` | `chaosx_formable_form_mountainous_republic_territory_qualifies` | `form_mountainous_republic` | 5 |
| `form_idel_ural_category` | `form_idel_uralic_republic` | `chaosx_formable_form_idel_uralic_republic_territory_qualifies` | `form_idel_uralic_republic` | 5 |
| `greater_italy_category` | `proclaim_greater_italy` | `chaosx_formable_proclaim_greater_italy_territory_qualifies` | `proclaim_greater_italy` | 25 |
| `form_sweden_hungary_category` | `proclaim_sweden_hungary` | `chaosx_formable_proclaim_sweden_hungary_territory_qualifies` | `form_sweden_hungary_category` | 18 |
| `latin_africa_category` | `unite_latin_africa` | `chaosx_formable_unite_latin_africa_territory_qualifies` | `unite_latin_africa` | 18 |
| `neo_assyrian_empire_category` | `neo_assyrian_empire_decision` | `chaosx_formable_neo_assyrian_empire_decision_territory_qualifies` | `neo_assyrian_empire_decision` | 21 |
| `neo_mesopotamia_category` | `neo_mesopotamia_decision` | `chaosx_formable_neo_mesopotamia_decision_territory_qualifies` | `neo_mesopotamia_decision` | 21 |
| `maghreb_formable_category` | `unite_maghreb` | `chaosx_formable_unite_maghreb_territory_qualifies` | `unite_maghreb` | 18 |
| `greater_mongolia_category` | `unite_greater_mongolia` | `chaosx_formable_unite_greater_mongolia_territory_qualifies` | `unite_greater_mongolia` | 21 |
| `greater_hui_state_category` | `unite_hui_states` | `chaosx_formable_unite_hui_states_territory_qualifies` | `unite_hui_states` | 9 |
| `GOE_form_hindustan_category` | `GOE_form_hindustan` | `chaosx_formable_goe_form_hindustan_territory_qualifies` | `GOE_form_hindustan` | 39 |

The helper registry is `common/scripted_triggers/chaosx_formable_state_puzzle_triggers.txt`.
It contains 461 unique definitions: one shared primitive, 392 per-state wrappers, 47 requirement-group helpers, and 21 territory helpers.
Every selected formation decision calls exactly one territory helper from its `available` block.
The detailed original-to-helper mapping is in `helper_architecture_handoff.md`.

Greater Italy and Sweden-Hungary retain their carrier-or-subject policy.
Their wrappers use carrier-scoped `any_subject_country` checks rather than a whole-world `any_country` search.
No daily, weekly, monthly, or global refresh scan was added.

## Runtime paths and sprite contract

- Category metadata: `common/decisions/categories/zzz_chaosx_formable_state_puzzle_categories.txt`
- Decision availability: `common/decisions/formable_nation_decisions.txt`
- Scripted GUI: `common/scripted_guis/chaosx_formable_state_puzzles.txt`
- Scripted localisation: `common/scripted_localisation/chaosx_formable_state_puzzles.txt`
- GUI windows: 21 files matching `interface/chaosx_formable_state_puzzle_<formable_id>.gui`
- Sprite registry: `interface/chaosx_formable_state_puzzles.gfx`
- Player localisation: `localisation/english/chaosx_formable_state_puzzles_l_english.yml`
- Runtime DDS: `gfx/interface/formables/state_puzzles/<manifest_owner_id>/states/`
- Manifests and review evidence: `docs/formables/state_puzzles/<manifest_owner_id>/manifest.json`
- Deterministic runtime generator: `.tools/generate_formable_state_puzzle_runtime.mjs`

Each manifest supplies the exact unresolved and qualifying sprite ids for every state.
The 784 exact runtime ids are registered in the GFX file; modern packages use `GFX_formable_state_puzzle_<formable_id>_state_<state_id>_<variant>`, while reviewed legacy packages retain their manifest-declared `GFX_<formable_id>_state_<state_id>_<variant>` ids.
The generator consumes both schemas through a strict adapter and does not rename legacy assets.

The live qualifying numerator uses descending `count_triggers` checks over the same state wrappers.
The pieces, hover status, count, completion summary, and formation decision therefore share one eligibility source and do not depend on cached variables.

## Audit and validation evidence

- The runtime generator reports 21 formables and 392 state entries.
- All 21 manifests parse and reference 784 existing DDS files.
- The GFX registry contains 784 sprite definitions with no missing texture path.
- The GUI package contains 21 root windows and 392 state-piece icons.
- All 21 category `scripted_gui` references resolve to one runtime declaration.
- All nine static-picture DDS files match the active 114x101 consumer.
- Both touched localisation files retain UTF-8 BOM encoding and no `:0` key suffixes.
- The full source-mapped category inventory contains 296 unique rows with no duplicate or omitted baseline id.

Installed-map membership, province geometry, and projection provenance are recorded in the manifests and state-piece handoffs.
The state-layer MCP render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4eaf3e38b3ca2b30147f0b469ea118c90b5fa8e84813b9159be3a11c8d316341/5955e67ccdd29a496569e2bc6dad1afad6ec55b3dae8b0f2e1a961f5f7e72c53/map-state.png`.

The post-generation GUI inspection resolving the 21 references is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2eb170613915717fe7e0e9c11bd08511f9859eb45e69e157dc6fc4364bd225e/2cb04c228656f2c3b8bebac39201168bb719516de179c7f4c48d2bbe20188ebe/gui-inspect.d60311b14e0ced7d.json`.

The five-state Mountainous Republic render covers 1366x768, 1920x1080, and 2560x1440 with normal, hover, long-text, and missing-localisation states.
The dense 39-state Hindustan render covers 1366x768 and 1920x1080 with normal, hover, and long-text states.
Their cropped artifacts are recorded in `docs/formable_state_puzzle_system.md`.
The generic overlap diagnostic counts intended adjacency between separately placed map pieces; visual review found no unintended collision or clipping.

## Explicit exceptions, omissions, and blockers

The 27 static formable exceptions are deliberate selection results, not hidden fallbacks.
They comprise branching or multi-formation categories, the dynamic Nordic League all-core-state route, archipelagic alternatives, non-fixed gates, and fixed maps too large for a legible 440x180 hover surface.
Every exception and concrete reason appears in `docs/formable_state_puzzle_system.md`.

No selected picture, manifest, state-piece variant, runtime sprite, helper, GUI binding, tooltip layer, or reusable-template file is omitted.
No approximate state shape, generic tile, ImageGen map, cached eligibility state, fake button, animation fallback, or full-window substitute was used.

The installed MCP exposes no direct decision-category inspect/render route, so the supported category-attached GUI route supplies the engine-facing presentation evidence.
Bounded GUI rewrite rejected the proposed patch with `GUI_UNSAFE_PATCH_RANGE` and `REWRITE_STRUCTURE_LIMIT`; no rewrite output was accepted, and the normally edited runtime was re-inspected and rendered afterward.
Whole-workspace GUI diagnostics and map-wide building-position or port diagnostics remain outside this task; the selected GUI references and state/province geometry checks pass.

The unrelated shared-worktree Independence Wave FORM-09 category is recorded as a one-id current delta outside the 296-id baseline audit and was not changed by this plan.

There are no task-level implementation blockers or undisclosed simplifications.
