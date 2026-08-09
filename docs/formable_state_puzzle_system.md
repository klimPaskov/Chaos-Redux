# Formable state-puzzle system

## Purpose

The formable state-puzzle system adds a compact, informational territorial display below selected formable decision categories while preserving the installed Vanilla category picture above it.

Every displayed state uses exact geometry from the installed map, occupies its real relative position inside a category-specific projection, and remains a separate hoverable icon.

The 21 live displays cover 392 selected formable-state entries and therefore register 784 unresolved/qualifying state-piece sprites. The same installed state can legitimately appear in more than one formable.

The display does not create a second formation action.
The ordinary formation decision remains the only action and the AI uses that decision without interacting with the display.

## Runtime contract

- Unresolved state pieces are grey with a diagonal hatch.
- Qualifying state pieces are green with a solid inner keyline.
- The hatch and keyline are the required non-colour cues.
- Every hover names the state, current owner, current controller, whether the carrier qualifies for control, and whether the carrier has a core.
- The state piece, category summary, formation decision, and AI-facing decision availability call the same scripted trigger family.
- Status is evaluated directly from live triggers.
- The panel does not cache formation eligibility or add a daily, weekly, or global refresh scan.
- The compact summary reports the live qualifying-state numerator and ready/incomplete status by calling the same per-state and territory helpers as the pieces and formation decision.
- The numerator is selected through descending `count_triggers` checks, so it does not depend on a cached variable or a refresh effect.
- The GUI contains icons and text only, with no dead or imitation buttons.

## Applicability gate

A live state puzzle is used when one category exposes one formation decision with a fixed exact-state requirement and the resulting map remains legible in a 440x180 compact panel.

The inherited static category picture remains the selected layer when the category contains multiple mutually exclusive formation decisions, the formation rule is not a fixed list of states, or the exact list is too large for individually hoverable pieces to remain compact and legible.

## Coverage

| Category | Formation surface | Selected layer | Reason |
| --- | --- | --- | --- |
| `form_scandinavia_category` | `form_scandinavia` | Compact state puzzle + inherited static picture | One fixed formation decision with a bounded Scandinavian state set. |
| `form_nordic_league_category` | `form_nordic_league` | Static picture | The Estonian route derives requirements from a dynamic all-core-state set, so one fixed installed-state manifest would be incomplete. |
| `form_north_sea_category` | `form_north_sea_empire` | Compact state puzzle + inherited static picture | One fixed formation decision with a coherent North Sea projection. |
| `form_baltic_sea_empire_category` | `form_baltic_sea_empire` | Compact state puzzle + inherited static picture | One fixed formation decision with a coherent Baltic projection. |
| `form_gran_colombia_category` | `form_gran_colombia` | Compact state puzzle + inherited static picture | One fixed formation decision with a small contiguous northern South American state set. |
| `form_austria_hungary_category` | Two formation decisions | Static picture | Multiple formation decisions use distinct territorial and political branches, so one live map would conflate eligibility. |
| `form_commonwealth_category` | `form_commonwealth` | Compact state puzzle + inherited static picture | One fixed formation decision with a bounded Commonwealth state set. |
| `form_united_netherlands_category` | `form_united_netherlands` | Compact state puzzle + inherited static picture | One fixed formation decision with a small contiguous Low Countries state set. |
| `form_united_central_america_category` | Three formation decisions | Static picture | Multiple route-specific formation decisions do not share one exact territorial proof. |
| `form_baltic_federation_category` | `form_baltic_federation` | Compact state puzzle + inherited static picture | One fixed formation decision with a small coherent Baltic state set. |
| `form_ottoman_empire_category` | Thirteen formation decisions | Static picture | The category is a branching imperial progression rather than one fixed territorial puzzle. |
| `form_european_union_category` | Fourteen formation decisions | Static picture | Candidate-specific formation branches collectively reference hundreds of states and cannot remain legible in one compact panel. |
| `form_mutapa_category` | `form_mutapa` | Compact state puzzle + inherited static picture | One fixed formation decision with a bounded southern African state set. |
| `form_roman_empire_category` | Twenty formation decisions | Static picture | Candidate and restoration branches use different territorial sets across several regions. |
| `form_persian_empire_category` | `form_persian_empire` | Static picture | The fixed list is too large for seventy-one independently hoverable pieces to remain compact. |
| `form_byzantine_empire_category` | Six formation decisions | Static picture | Restoration branches use different state groups and political gates. |
| `form_arabia_category` | Seven formation decisions | Static picture | Several alternative formation routes share the category but not one exact requirement set. |
| `form_majapahit_empire_category` | Four formation decisions | Static picture | Alternative archipelagic routes and distributed island states would make one category map ambiguous. |
| `form_maphilindo_category` | Four formation decisions | Static picture | Alternative archipelagic formation routes do not share one exact state proof. |
| `form_rattanakosin_kingdom_category` | `form_rattanakosin_kingdom` | Compact state puzzle + inherited static picture | One fixed formation decision with a small coherent mainland state set. |
| `form_hre_category` | `form_hre` | Static picture | The fixed list needs fifty-nine separate pieces and exceeds the compact legibility limit. |
| `form_greater_german_reich_category` | `form_greater_german_reich` | Static picture | Formation is not gated by a fixed exact-state list. |
| `form_greater_german_state_category` | `form_greater_proletarian_state` | Static picture | The fixed list needs seventy-three separate pieces and exceeds the compact legibility limit. |
| `form_andalusia_category` | Six formation decisions | Static picture | Alternative restoration routes span different territorial groups. |
| `maghreb_formable_category` | `unite_maghreb` | Compact state puzzle + inherited static picture | One fixed formation decision with a coherent North African projection. |
| `form_polynesia_category` | Two formation decisions | Static picture | Alternative island-union and imperial routes do not share one exact state set. |
| `form_greater_greece_category` | Six formation decisions | Static picture | Multiple restoration stages and alternate territorial gates share the category. |
| `form_macedonian_empire_category` | `form_macedonian_empire` | Static picture | The fixed list needs ninety-three separate pieces and exceeds the compact legibility limit. |
| `form_turan_category` | Five formation decisions | Static picture | Route-specific Eurasian formation stages collectively reference an oversized, branching state set. |
| `form_turkestan_category` | `form_turkestan` | Compact state puzzle + inherited static picture | One fixed formation decision with a coherent Central Asian projection. |
| `form_mountainous_republic_category` | `form_mountainous_republic` | Compact state puzzle + inherited static picture | One fixed formation decision with five contiguous Caucasian states. |
| `form_transcaucasus_category` | Seven formation decisions | Static picture | Several alternative federation and integration routes share the category. |
| `form_siberia_category` | Five formation decisions | Static picture | Alternative Siberian formations use different long-range state sets. |
| `form_idel_ural_category` | `form_idel_uralic_republic` | Compact state puzzle + inherited static picture | One fixed formation decision with five regional states. |
| `form_ethiopian_empire_category` | Five formation decisions | Static picture | Several Ethiopian restoration and expansion routes do not share one exact requirement set. |
| `form_east_africa_category` | Six formation decisions | Static picture | Multiple federation paths share the category and use different territorial checks. |
| `form_horn_of_africa_africa_category` | Four formation decisions | Static picture | Alternative Horn formations and route gates do not share one exact state proof. |
| `greater_italy_category` | `proclaim_greater_italy` | Compact state puzzle + inherited static picture | One fixed formation decision with a coherent central Mediterranean projection. |
| `form_sweden_hungary_category` | `proclaim_sweden_hungary` | Compact state puzzle + inherited static picture | One fixed formation decision with a bounded two-region requirement. |
| `antilles_category` | Three formation decisions | Static picture | The category's formation branches are not expressed as one fixed exact-state list. |
| `latin_africa_category` | `unite_latin_africa` | Compact state puzzle + inherited static picture | One fixed formation decision with a coherent central African state set. |
| `germany_formable_category` | Seven formation decisions | Static picture | Ideological and identity branches do not share one fixed territorial proof. |
| `neo_assyrian_empire_category` | `neo_assyrian_empire_decision` | Compact state puzzle + inherited static picture | One fixed formation decision with twenty-one named state scopes. |
| `neo_mesopotamia_category` | `neo_mesopotamia_decision` | Compact state puzzle + inherited static picture | One fixed formation decision with twenty-one active state scopes; the commented state is excluded. |
| `greater_mongolia_category` | `unite_greater_mongolia` | Compact state puzzle + inherited static picture | One fixed formation decision with a coherent Mongolian projection. |
| `greater_hui_state_category` | `unite_hui_states` | Compact state puzzle + inherited static picture | One fixed formation decision with a small north-western Chinese state set. |
| `GOE_form_hindustan_category` | `GOE_form_hindustan` | Compact state puzzle + inherited static picture | One fixed formation decision with a bounded subcontinental projection. |
| `AST_australia_formables_category` | Two formation decisions | Static picture | The category holds two archipelagic formations with different state groups and no inherited category picture. |

## Assets and sprite wiring

Each live category owns a manifest and review projection under `docs/formables/state_puzzles/<manifest_owner_id>/`; the manifest records the exact category and formation ids.

Runtime state-piece textures live under `gfx/interface/formables/state_puzzles/<manifest_owner_id>/states/`.

Every required state owns an unresolved and qualifying DDS registered by `interface/chaosx_formable_state_puzzles.gfx`.

The category windows live in one owner-specific `interface/chaosx_formable_state_puzzle_<formable_id>.gui` file per live formable, and the `decision_category` bindings live in `common/scripted_guis/chaosx_formable_state_puzzles.txt`.

Player-facing summaries, state hovers, and sprite-selection keys live in the formable state-puzzle localisation and scripted-localisation files.

No animated sprite is required for this system.

## Geometry and GUI validation

HOI4 MCP map inspection validated the installed province geometry and state membership used by the manifests. The shared state-layer render is recorded at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4eaf3e38b3ca2b30147f0b469ea118c90b5fa8e84813b9159be3a11c8d316341/5955e67ccdd29a496569e2bc6dad1afad6ec55b3dae8b0f2e1a961f5f7e72c53/map-state.png`.

The post-generation GUI inspection resolved all 21 formable category references and is recorded at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2eb170613915717fe7e0e9c11bd08511f9859eb45e69e157dc6fc4364bd225e/2cb04c228656f2c3b8bebac39201168bb719516de179c7f4c48d2bbe20188ebe/gui-inspect.d60311b14e0ced7d.json`.

The five-state Mountainous Republic display was rendered across 1366x768, 1920x1080, and 2560x1440 in normal, hover, long-text, and missing-localisation states. Its cropped review artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2e860825aa0768072275474b94a966a2b9ece02e288fcd9321311af5fc46e914/6bea71fc96ede58beddd82f849fa0afe05a7390550bfd9ec0d17634c6c9b0ff0/chaosx_formable_state_puzzle_form_mountainous_re-cropped.png`.

The dense 39-state Hindustan display was rendered across 1366x768 and 1920x1080 in normal, hover, and long-text states. Its cropped review artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3500a95f06376772735ec930c06ac96feee732db92769b33a4508a2d5d7d78bb/cbb8f749ec5c038fad76eb95acebd81de75c8792ae820aa1efef036400a9e9d5/chaosx_formable_state_puzzle_goe_form_hindustan_-cropped.png`.

The renderer's generic overlap diagnostic counts intentional contacts and overlaps between adjacent exact-geometry state pieces. Visual review of both rendered composites found no unintended overlap, clipping, or summary collision. Whole-workspace GUI diagnostics outside these 21 windows and map-wide building-position or port diagnostics remain unrelated to this system.

Bounded GUI rewrite was attempted, but the live route rejected the requested change with `GUI_UNSAFE_PATCH_RANGE` and `REWRITE_STRUCTURE_LIMIT`; no rewrite output was accepted. The runtime files were therefore edited through the normal repository workflow and then inspected and rendered through MCP.

The manifests are invalidated when the installed map revision changes.
State pieces must be regenerated from exact geometry rather than stretched or redrawn.

## Future plans and suggestions

- Split any oversized static category into route-specific categories before reconsidering a live map.
- Add a compact legend toggle only if a future engine-supported informational control communicates more than the permanent hatch and keyline cues.
- Rebuild the state-piece package after installed map updates and compare manifest geometry checksums before shipping.
- Consider route-specific puzzles for branching categories only after the decision structure exposes an unambiguous active branch to the category GUI.
