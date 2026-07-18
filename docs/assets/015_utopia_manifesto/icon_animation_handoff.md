# Event 015 icon and animation handoff

Runtime sprite registry: `interface/015_utopia_manifesto.gfx`

Snapshot: `2026-07-16`

Status: **PASS - the current icon, static Ledger, animation, GUI, and binding slice is complete.**

Machine animation, registry, GUI, and state-binding authority: `final_icon_frame_audit.json`, SHA-256 `c85df258c4aaaf37e905fdc14883cda6b0f8a1f41840df745a3136c830a66d01`. Its frozen decision-mapping subsection is historical. Current mapping authority is `decision_icon_mapping.csv`, SHA-256 `757ec0c51edca25b5453899f28816a3d34e8a5b330be268bed6ff4d27e0abcc0`.

## Current exact package

- Focuses: `124` assignments, `74` unique base sprites, matching shine registrations, `111` physical DDS files.
- Decisions/categories/missions: `174` mapping rows (`9` categories, `121` decisions, `44` missions), with `165` live gameplay icon assignments.
- Ideas: `50` entries, `12` unique live pictures.
- Achievements: `14` exact current IDs and `42` current base/grey/not-eligible variants.
- Registry: `459` base definitions plus `5` route-super-event definitions = `464`, duplicate names `0`.
- Ledger GUI: `46` unique sprite references, unresolved references `0`.
- Repaired static Ledger families: Values `4`, Callings `6`, Case cards `10`, District roles `7`, District states `6`; all runtime hashes are unique within each family.

District role cards and state overlays are deliberately in `utopia_ledger_stores_panel`, the **Stores/Settlements tab**. Case cards are in `utopia_ledger_ground_panel`, the Necessary Ground tab.

## Authored-frame package matrix

| Package | Role | Frames | Frame/sheet | FPS | Loop | Static frame | Binding |
| --- | --- | ---: | --- | ---: | --- | ---: | --- |
| `utopia_ledger_seal` | required Ledger seal | `8` | `64x64` / `512x64` | `12` | yes | `000` | generic header until a route emblem exists |
| `utopia_need_warning` | required critical warning | `8` | `64x64` / `512x64` | `5` | yes | `004` | high Need, low Plenty, or constitutional crisis |
| `utopia_reserve_fill` | extra reserve presentation | `8` | `300x24` / `2400x24` | `4` | yes | `004` | reserve-band variable exists |
| `utopia_balance_to_choice` | required balance direction | `8` | `158x24` / `1264x24` | `5` | no | `007` | route-resolved band crossing toward Choice |
| `utopia_balance_to_assignment` | required balance direction | `8` | `158x24` / `1264x24` | `5` | no | `007` | route-resolved band crossing toward Assignment |
| `utopia_formation_ready_seal` | required formation proof | `10` | `96x96` / `960x96` | `5` | yes | `005` | current route can form and is not formed |

The five standardized packages (Need, reserve, Choice, Assignment, formation) pass exact source-count, source-distinctness, processed-count, processed-distinctness, frame-size, horizontal-concatenation, static-frame, strict one-level BGRA DDS, PNG/DDS pixel-equality, GFX metadata, GIF-frame-count, contact-sheet, GUI-reference, and state-binding checks. Reserve is explicitly extra and is not used to substitute for an accepted row.

Choice and Assignment each use eight separate built-in ImageGen objects. Their manifest hashes are `639d2e6e75f082b5a139b7e26222b061a41906005ac139f0685c3931cab74e4f` and `6fbc91cc8fe69d35c7d778c090ff29fd61fa59ca14b4f972a2e7a9cd13c072ce`. Their final frames show opposite authored structural changes rather than transform-only movement.

## Independently frozen legacy Ledger seal

The Ledger seal uses an older folder layout, so it is intentionally outside the standardized JSON animation map and was audited separately.

- Generated source sheet: `1536x1024`, SHA-256 `e09067700aebd0d627e83f211890f497844f95b370503610f931b07db06deb2d`.
- Source slices: eight unique `443x443` PNGs.
- Processed frames: eight unique `64x64` PNGs.
- Exact sheet PNG: `512x64`, SHA-256 `9404dc2e8af552c24c6a6bbec35e736573e017b6f04c57e5e6dacc3a62d789a1`.
- Static PNG equals frame `000`, SHA-256 `9ead13f7beef549b87fc077527019686f1b0e3018daab61f8acd5499c3eeb4d9`.
- Runtime sheet DDS: strict uncompressed BGRA, `131200` bytes, SHA-256 `17a5c98dcdc3cf9ba5317ecfb61ba9811e77152b603929675d6ab4c027114bd4`, pixel-identical to sheet PNG.
- Runtime static DDS: strict uncompressed BGRA, `16512` bytes, SHA-256 `9a423fcf63ac58fa63fa24b4c77b29fc6636b97a0f282dcb0a21254622ddef2c`, pixel-identical to static PNG.
- Review GIF: eight frames, looping, `120 ms` per review frame, SHA-256 `f73bad0e1cbec016d2fe43063e75490553692446ce030aead805e5702485d37b`.
- Contact sheet: `320x156`, SHA-256 `6780acdccb83eb308dcd3b6e03cffcdc3bb1ccc0aca1c4e065747e6db22f901d`.
- Runtime GFX: `8` frames, `12 fps`, looping, `play_on_show = yes`; live GUI consumer at `(18,16)` with exact route-emblem replacement visibility.

The GIF is review-only. Its `120 ms` preview cadence is recorded exactly and does not override the runtime's independently defined `12 fps` playback.

## Repaired static package proof

- Values/Callings: frozen built-in ImageGen atlas SHA-256 `7a1704f1c6d720ff72b9cdc3715101361bb8b836033607d0ff244dbb31c7d440`; validator SHA-256 `aa9a249348fb5bd864bb8ffc2a46ba6a67fc595cb58a08261cf32e8e5e61e007`; decoded review contact SHA-256 `b461f61933ff53b43480ed8233a103ed6f20564f4525eb40666fe59d9de5a8bf`.
- Case cards: ten independent ImageGen masters; validator SHA-256 `924f2fc5a164ce6756ff453922a3e75cea6b8c79639b5254cec59072e746e1c4`; decoded review contact SHA-256 `e8a4583f6d35e7fd4a6dc2345bac0356ee7adcfc20625102f9c1df7790d70a2f`.
- District cards: thirteen independent ImageGen masters; validator SHA-256 `cc20a3bf3d48aa2f873af421a5c07ccce8943ee19edbaf785c040200b25eae84`; role review contact SHA-256 `31b6c48fbd3436b40cbc04ac42fc1993a5d11a5d345ef5507e4d04bd7ad9ec96`; state review contact SHA-256 `0365e42264fdbe30e4b075b9ebddf8c85c897f081a41951063e0a9a0835a9807`.

Every repaired runtime DDS has the expected size/header, matches its packaged file, decodes to the processed pixels, and resolves through one GFX definition and one intended GUI consumer. The original Value/Calling generation prompt is not present in the repository; the preserved generated atlas and prior provenance are reported honestly instead of inventing a prompt.

## Visual review and limits

Original-resolution contact sheets show distinct, legible Values/Callings, ten semantically distinct Case states, seven people-free role cards, six distinct state overlays, a cracking Need measure, opposite balance structures, a progressive formation seal, a real Ledger-seal glow cycle, and the extra reserve sequence. No required animation is a transform-only still.

This was a static package, image, DDS, GFX, GUI, and script-binding audit. GIF metadata and contact sheets were reviewed; HOI4 runtime playback was not launched. That is a tool limit, not a missing asset or fallback.

Simplifications: none. Omissions: none. Fallbacks: none. Open blockers: none.

## Historical exact package snapshot (2026-07-14, superseded)

The older notes below are retained only as package history. Their counts and missing-parent language are superseded by the current authority above.

- Focus use: `122` assignments, `72` unique base sprites, `72` matching `_shine` sprites, all current textures `94x86`. The folder retains `109` family DDS files in total.
- Decisions/categories/missions: `decision_icon_mapping.csv` contains `139` exact rows (`9` categories, `98` decisions, `32` missions). Every mapped sprite has a registered `32x32` DDS. The parent implementation agent still needs to add the gameplay `icon =` assignments.
- Ideas: all `12` unique picture tokens used by the current `50` idea entries have registered `64x64` DDS files; ten missing exact pictures were generated in this pass.
- Achievements: all `14` exact current `utopia_manifesto_*` ids have base, `_grey`, and mandated-overlay `_not_eligible` files (`42` total), plus `42` explicit sprite aliases. The older `36` `015_utopia_*` files are retained historical assets, not current coverage.
- Live authored-frame additions:
  - `GFX_utopia_need_warning_{static,animated}`: `8` distinct source frames, `64x64`, `512x64` sheet, `5 fps`.
  - `GFX_utopia_reserve_fill_{static,animated}`: `8` distinct source frames, `300x24`, `2400x24` sheet, `4 fps`.
  - `GFX_utopia_formation_ready_seal_{static,animated}`: `10` distinct source frames, `96x96`, `960x96` sheet, `5 fps`.
- Source and review proof:
  - `docs/assets/015_utopia_manifesto/source_png/final_icons/`
  - `docs/assets/015_utopia_manifesto/processed_png/final_icons/`
  - `docs/assets/015_utopia_manifesto/animations/<asset>/`
  - `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json`

## Historical 2026-07-01 Static Icon Package Notes

The subsections below preserve the earlier regeneration handoffs. Their decision/idea and achievement counts are superseded by the current exact package above. The cosmetic-flag subsection remains the separate flag handoff and was not changed by the icon/frame pass.

### Focus Icons

- Runtime folder: `gfx/interface/goals/015_utopia_manifesto/`
- Runtime size: `94x86`
- Source proof: `docs/assets/015_utopia_manifesto/source_png/focus_atlas_*_imagegen_atlas.png`
- Contact sheets:
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_01.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_02.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_03.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_04.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_all.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_focus_icon_regeneration.md`
- Validation: 109 runtime `goal_utopia_*` DDS files exist, are `94x86`, and have transparent unused corners.

### Decision, Category, and Idea Icons

- Decision/category runtime folder: `gfx/interface/decisions/015_utopia_manifesto/`
- Idea runtime folder: `gfx/interface/ideas/015_utopia_manifesto/`
- Decision/category runtime size: `32x32`
- Idea runtime size: `64x64`
- Source proof:
  - `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_decision_atlas_source.png`
  - `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_idea_atlas_01_source.png`
  - `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_idea_atlas_02_source.png`
- Contact sheets:
  - `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_decisions.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_ideas.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_decision_idea_icon_regeneration.md`
- Validation: 25 runtime decision/category DDS files are `32x32`; 31 runtime idea DDS files are `64x64`; the regenerated icons have transparent unused corners and no obvious white square backgrounds.

### Achievement Icons

- Runtime folder: `gfx/achievements/`
- Runtime size: `64x64`
- Stems covered:
  - `015_utopia_new_utopia`
  - `015_utopia_need_not_greed`
  - `015_utopia_friends_without_treaties`
  - `015_utopia_six_hour_country`
  - `015_utopia_no_bloody_glory`
  - `015_utopia_inland_island`
  - `015_utopia_storehouses_abroad`
  - `015_utopia_league_of_need`
  - `015_utopia_marked_bounds_survivor`
  - `015_utopia_all_useful_arts`
  - `015_utopia_renounced_bounds`
  - `015_utopia_paper_no_more`
- Variants: base, `_grey`, and `_not_eligible`
- Contact sheet: `docs/assets/015_utopia_manifesto/contact_sheets/achievements_regenerated_imagegen_contact.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_achievement_icon_regeneration.md`
- Validation: all 36 runtime achievement DDS files exist, are `64x64`, and have no obvious white square backgrounds.

### Cosmetic Flags

- Runtime folders:
  - `gfx/flags/`
  - `gfx/flags/medium/`
  - `gfx/flags/small/`
- Cosmetic tags:
  - `utopia_new_utopia`
  - `utopia_necessary_commonwealth`
  - `utopia_league_of_need`
  - `utopia_marked_bounds_state`
- Runtime sizes: `82x52`, `41x26`, and `10x7`
- Ideology variants: each cosmetic tag has `democratic`, `communism`, `fascism`, and `neutrality` copies in all three runtime flag folders.
- Source proof: `docs/assets/015_utopia_manifesto/source_png/flag_utopia_*_source.png`
- Contact sheet: `docs/assets/015_utopia_manifesto/contact_sheets/utopia_cosmetic_flags_imagegen_contact.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_cosmetic_flag_asset_handoff.md`
- Validation: final TGAs match the existing HOI4 flag convention, remain readable by color and silhouette at small size, and include ideology variants so cosmetic tags replace arbitrary accepting-country flags consistently.

## Historical 2026-07-01 Animated GUI Package

This section preserves the older five-animation generation tranche. Those pieces use discrete generated frames, but only the Ledger seal is referenced by the current GUI; the other four remain registered legacy sequences. The current live Need, reserve, and formation-ready animations are listed above.

The full `gfx/interface/015_utopia_manifesto/` runtime family was regenerated from actual imagegen source art on 2026-07-01 after the earlier UI pieces were rejected as visually weak. The regenerated package covers the three Ledger panels, all five historical animated sheets, and all five static fallbacks. Source proof lives in `docs/assets/015_utopia_manifesto/source_png/utopia_*_source.png` and `docs/assets/015_utopia_manifesto/source_png/utopia_*_sheet_source.png`; review proof lives in `docs/assets/015_utopia_manifesto/contact_sheets/utopia_runtime_panels_regenerated_contact.png` and each animation's `previews/` folder.

| Asset | Static sprite | Animated sprite | Frame count | Frame size | Sheet size | Runtime use |
| --- | --- | --- | --- | --- | --- | --- |
| Ledger seal | `GFX_utopia_ledger_seal_static` | `GFX_utopia_ledger_seal_animated` | 8 | `64x64` | `512x64` | wired in `interface/015_utopia_manifesto_ledger.gui` |
| Overreach warning | `GFX_utopia_overreach_warning_static` | `GFX_utopia_overreach_warning_animated` | 8 | `64x64` | `512x64` | retained registered legacy sequence |
| Storehouse fill | `GFX_utopia_storehouse_fill_static` | `GFX_utopia_storehouse_fill_animated` | 8 | `64x16` | `512x16` | retained registered legacy sequence |
| New Utopia seal | `GFX_utopia_new_utopia_seal_static` | `GFX_utopia_new_utopia_seal_animated` | 10 | `96x96` | `960x96` | retained registered legacy sequence |
| Marked Bounds seal | `GFX_utopia_marked_bounds_seal_static` | `GFX_utopia_marked_bounds_seal_animated` | 10 | `96x96` | `960x96` | retained registered legacy sequence |

Panel regeneration:

- `GFX_utopia_ledger_background_panel` -> `gfx/interface/015_utopia_manifesto/utopia_ledger_background_panel.dds` (`700x500`)
- `GFX_utopia_ledger_header_plate` -> `gfx/interface/015_utopia_manifesto/utopia_ledger_header_plate.dds` (`700x96`)
- `GFX_utopia_ledger_warning_panel` -> `gfx/interface/015_utopia_manifesto/utopia_ledger_warning_panel.dds` (`320x128`)

Runtime visibility triggers:

- `utopia_ledger_new_utopia_seal_visible`
- `utopia_ledger_marked_bounds_seal_visible`
- `utopia_ledger_storehouse_fill_visible`
- `utopia_ledger_overreach_warning_visible`

## Current Runtime Coverage

- Every current focus and idea reference has a registered, present, correctly sized texture.
- Every row in `decision_icon_mapping.csv` has a registered, present, correctly sized texture; gameplay icon fields are the remaining parent integration step.
- Every exact current Event 015 achievement id has its complete triplet in the root `gfx/achievements/` folder.
- Every current Ledger GUI sprite reference resolves, and the three requested live animations have static fallbacks, distinct source frames, exact sheets, GIF previews, and contact sheets.
- Report/news/super-event completeness is tracked separately in `manifest.md`; the icon/frame package does not claim the five blocked route-specific super-event images.
