# Event 015 Asset Authority Index

Event id: `015`
Event slug: `utopia_manifesto`
General runtime sprite registry: `interface/015_utopia_manifesto.gfx`
Current route super-event registry: `interface/015_utopia_manifesto_super_event.gfx`

Snapshot: `2026-07-18`

Verdict: **PASS - every one of the 24 accepted asset-matrix rows is implemented, registered, consumed, and state-bound where required. No fallback, simplification, omission, or open blocker remains.**

## Current authority

Use these records in this order:

1. Live runtime files under `gfx/`, `interface/`, `common/characters/`, Event 015 gameplay script, scripted GUI, scripted localisation, music, and sound.
2. `requirement_to_runtime_coverage_2026_07_16.md` for the exact 24-row source-to-runtime crosswalk.
3. `decision_icon_mapping.csv` for the current decision, category, and mission mapping and assignment inventory. `final_icon_frame_audit.json` remains current only for its icon, animation, registry, GUI, and state-binding records; its frozen decision-mapping subsection is superseded by the CSV.
4. `final_non_icon_2026_07_14/asset_records.json` for reports, news, and five route-super-event images.
5. `route_identity_2026_07_14/asset_records.json` plus the dated flag, institutional-tableau, advisor, and built-in-source validators.
6. `value_calling_icon_repair_2026_07_16`, `ledger_case_cards_2026_07_16`, and `ledger_district_cards_2026_07_16` for the repaired Ledger families.
7. `gfx_handoff.md` and `icon_animation_handoff.md` for current live wiring.

`final_icon_frame_audit.json` has SHA-256 `c85df258c4aaaf37e905fdc14883cda6b0f8a1f41840df745a3136c830a66d01` and status `pass`. Its historical `173`-row, `43`-mission, and `164`-assignment mapping record is not current authority.

## Current proven inventory

| Surface | Current proof |
| --- | --- |
| Registry | `459` unique definitions in `015_utopia_manifesto.gfx` plus `5` in `015_utopia_manifesto_super_event.gfx` = `464`; duplicate names `0` |
| Ledger GUI | `46` unique sprite references; unresolved references `0` |
| Reports/news/super-event art | `14` reports, `3` news images, `5` route-super-event images; `22/22` source/processed/package/runtime records match and all final hashes are unique |
| Focuses | `124` uses, `74` unique sprites, `111` physical DDS files |
| Decisions/categories/missions | `174` mapping rows: `9` categories, `121` decisions, `44` missions; `165` live assignments |
| Ideas | `50` entries, `12` unique pictures |
| Achievements | `14` current IDs, `42` current base/grey/not-eligible variants |
| Repaired Ledger statics | Values `4`, Callings `6`, Case cards `10`, District roles `7`, District states `6` |
| Route identity | `21` independent built-in ImageGen flag designs plus `4` aliases = `75` TGAs; `4` people-free institutional tableaux; `16` independent advisor dossiers; `5` League emblems |

The seven District role cards and six state overlays are intentionally live in the **Stores/Settlements tab**, inside `utopia_ledger_stores_panel`. Necessary Ground Case cards remain in `utopia_ledger_ground_panel`.

## Current animation delivery

Five standardized packages are machine-audited: Need warning (`8` frames), reserve fill (`8`, extra presentation package), balance toward Choice (`8`), balance toward Assignment (`8`), and formation-ready seal (`10`). The required legacy-layout Ledger seal is independently frozen at `8` frames. Every package has distinct source and processed frames, exact sheet PNG, strict BGRA sheet DDS, static fallback, review GIF, contact sheet, GFX definitions, and a live GUI consumer. Sheet/static DDS pixels match their PNGs.

Runtime state binding is exact:

- Ledger seal: generic header seal until a route emblem is selected.
- Need warning: high Need, low Plenty, or constitutional crisis.
- balance directions: route-resolved Assignment-band crossings, three-day direction flags, first-refresh suppression, opposite-flag clearing, and terminal cleanup.
- formation-ready: the current route can form and the commonwealth is not formed.
- reserve fill: a live reserve-band value exists.

## Source constraints and visual review

- Four institutional masters are separate people-free built-in ImageGen tableaux. Native review confirms no people, faces, heads, bodies, hands, crowds, silhouettes, statues, busts, mannequins, framed portraits, photographs, or human shadows.
- Sixteen advisors use sixteen independent built-in ImageGen fictional portrait masters plus separately generated frame and paper/seal overlays. The visible dossier treatment is not drawn programmatically.
- Flags use 21 separate built-in ImageGen compositions. Only the four documented unsuffixed/canonical lookup pairs alias approved art.
- Value/Calling art comes from the frozen built-in ImageGen atlas SHA-256 `7a1704f1c6d720ff72b9cdc3715101361bb8b836033607d0ff244dbb31c7d440`. The exact original prompt was not present in the repository and was not reconstructed or invented; this provenance limitation does not alter the preserved generated source or delivered finals.
- Case and District cards use independent built-in ImageGen masters; rejected drafts remain outside runtime.

## Final super-event presentation

Slots `96`-`100` bind five route-distinct images, matching route descriptions, the shared title `UTOPIA HAS NEIGHBORS`, the verified public-domain Thomas More quotation, and audio ID `57`. `utopia_manifesto_emit_regional_proclamation` sets the exact route slot and audio ID, then calls the settings-aware playback helper.

The final WAV is Vorbis, `44,100 Hz`, stereo, `116.000000 s`, SHA-256 `68ebdcb9a4d81ca9863e85344fc19ab1ad99ffb7e83c836691d7a92181bfd1b9`. The WAV is PCM s16le, `44,100 Hz`, stereo, `116.000000 s`, SHA-256 `05da5a30ba49c6592e5295dd499e9ad3e97279586bb7e7d51228ad236ce58655`. Both are unique in the current runtime audio folders. Frozen CC0 source and licence evidence is documented in `docs/super_events/015_utopia_manifesto/audio_research.md`.

## Prior P2 history and completion boundary

The earlier `2026-07-16` requirement audit correctly found four P2 gaps: Values, Callings, Case cards, and District cards/bindings. The three repair packages and current runtime wiring resolve all four. No decision icon, text-only value, decorative panel, or other unrelated surface was accepted as a substitute.

Simplifications: none. Omissions: none. Fallbacks: none. Open blockers: none.

## Historical package notes (superseded by the current authority above)

Everything below this heading is retained only as earlier package history. Any older counts, missing-wiring instructions, or parent-handoff language below is non-authoritative.

- Event pictures:
  - The final non-icon package installs `14` report DDS files and `3` news DDS files under `gfx/event_pictures/015_utopia_manifesto/`.
  - `GFX_report_event_utopia_manifesto_found` remains registered in `interface/015_utopia_manifesto.gfx`; the other `13` report and `3` news sprite blocks are an exact parent wiring handoff documented in `gfx_handoff.md`.
  - The older `GFX_news_event_utopia_boundary_crisis` sprite and DDS remain installed as legacy Event 015 art.
- Installed legacy super-event pictures, retained but not selected by current slots `96`-`100`:
  - `GFX_super_event_utopia_new_utopia` -> `gfx/super_events/015_utopia_manifesto/super_event_utopia_new_utopia.dds`
  - `GFX_super_event_utopia_marked_bounds` -> `gfx/super_events/015_utopia_manifesto/super_event_utopia_marked_bounds.dds`
- Current route super-event pictures:
  - all five route sprites are registered in `interface/015_utopia_manifesto_super_event.gfx`, and all five exact `457x328` DDS files are installed under `gfx/super_events/015_utopia_manifesto/`
- Ledger GUI:
  - `GFX_utopia_ledger_background_panel`
  - `GFX_utopia_ledger_header_plate`
  - `GFX_utopia_ledger_seal_animated`
  - `GFX_utopia_need_warning_animated`
  - `GFX_utopia_reserve_fill_animated`
  - `GFX_utopia_formation_ready_seal_animated`
- Current authored animation packages with static fallbacks:
  - `utopia_need_warning` (`8` frames, `64x64`, `5 fps`)
  - `utopia_reserve_fill` (`8` frames, `300x24`, `4 fps`)
  - `utopia_formation_ready_seal` (`10` frames, `96x96`, `5 fps`)
- Registered legacy animation packages retained on disk but not referenced by the current Ledger GUI:
  - `utopia_overreach_warning`
  - `utopia_storehouse_fill`
  - `utopia_new_utopia_seal`
  - `utopia_marked_bounds_seal`
- Focus icons:
  - The current tree contains `122` focus icon usages across `72` unique `GFX_goal_utopia_*` sprites.
  - Every unique base sprite and matching `_shine` sprite is registered, and every current texture is present at `94x86` under `gfx/interface/goals/015_utopia_manifesto/`.
  - The runtime folder contains `109` family DDS files; `37` are retained legacy/surplus family art rather than current tree references.
- Decision and category icons:
  - `decision_icon_mapping.csv` covers the exact current source set: `9` categories, `98` decisions, and `32` missions (`139` rows total).
  - Every mapped `GFX_decision_utopia_*` or `GFX_decision_category_utopia_*` sprite is registered and has a `32x32` DDS under `gfx/interface/decisions/015_utopia_manifesto/`.
  - Gameplay integration remains assigned to the parent implementation agent: `common/decisions/015_utopia_manifesto_decisions.txt` currently contains zero `icon =` assignments.
- Idea icons:
  - The `50` current idea entries use `12` unique `picture =` tokens. Every exact `GFX_idea_utopia_*` sprite is registered and has a `64x64` DDS under `gfx/interface/ideas/015_utopia_manifesto/`.
  - Ten exact current idea sprites were generated in the final pass; the two already-current sprites (`utopia_found_manifesto` and `utopia_common_store_network`) remain in use.
- Achievements:
  - All `14` exact current `utopia_manifesto_*` achievement ids have base, `_grey`, and mandated-overlay `_not_eligible` variants under `gfx/achievements/` (`42` files total).
  - All `42` explicit `GFX_achievement_utopia_manifesto_*` aliases are registered in `interface/015_utopia_manifesto.gfx`.
  - The `36` superseded `015_utopia_*` triplet files remain because a repository plan document still references them; they are not presented as current achievement coverage.
- Cosmetic flags:
  - `utopia_new_utopia`, `utopia_necessary_commonwealth`, `utopia_league_of_need`, and `utopia_marked_bounds_state` exist in normal, medium, and small HOI4 flag folders.
  - Each cosmetic tag also has `democratic`, `communism`, `fascism`, and `neutrality` variants in normal, medium, and small folders, derived from the corresponding generated base flag art so arbitrary accepting countries do not retain ideology-specific original flags.

## Source, Processed, and Preview Files

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/`
- Processed PNGs: `docs/assets/015_utopia_manifesto/processed_png/`
- DDS staging copies: `docs/assets/015_utopia_manifesto/dds/`
- Contact sheets: `docs/assets/015_utopia_manifesto/contact_sheets/`
- Animation frame packages: `docs/assets/015_utopia_manifesto/animations/`
- Final icon atlases and per-cell sources: `docs/assets/015_utopia_manifesto/source_png/final_icons/`
- Final processed icons and contact sheets: `docs/assets/015_utopia_manifesto/processed_png/final_icons/`
- Final icon DDS staging copies: `docs/assets/015_utopia_manifesto/dds/final_icons/`
- Exact decision/category/mission handoff: `docs/assets/015_utopia_manifesto/decision_icon_mapping.csv`
- Machine-readable audit result: `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json`
- Final non-icon package: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/`
- Final non-icon immutable records: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/asset_records.json`
- Final non-icon contact sheets: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/contact_sheets/`
- Tooling:
  - `docs/assets/015_utopia_manifesto/_tooling/process_utopia_assets.py`
  - `docs/assets/015_utopia_manifesto/_tooling/complete_utopia_assets.py`
  - `docs/assets/015_utopia_manifesto/_tooling/regenerate_utopia_runtime_visuals.py`
  - `docs/assets/015_utopia_manifesto/_tooling/process_final_icon_frame_package.py`
  - `docs/assets/015_utopia_manifesto/_tooling/generate_decision_icon_mapping.py`
  - `docs/assets/015_utopia_manifesto/_tooling/audit_final_icon_frame_package.py`
  - `docs/assets/015_utopia_manifesto/_tooling/process_final_non_icon_package.py`

## Historical Non-Icon Event-Art Provenance Audit

Audit date: `2026-07-14`

The four images below record the Event 015 asset state before the complete final non-icon package. They are fictional period-documentary scenes generated with OpenAI `image_gen`. No internet image, real-person likeness, archival photograph, or third-party character reference was used. The `report_event_utopia_manifesto_found` runtime derivative was superseded by the final package, so its old checksum below is historical rather than the current file checksum. Current checksums for all `22` final assets are authoritative in `final_non_icon_2026_07_14/manifest.md`.

Canonical prompt record: `docs/assets/015_utopia_manifesto/prompts/generated_event_art_prompts.md`  
Generation/processing handoff: `docs/assets/015_utopia_manifesto/generated_event_art_handoff.md`

| Asset | Source mode and use | Preserved source PNG | Source SHA-256 | Processed PNG | Final DDS | Final DDS SHA-256 | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `report_event_utopia_manifesto_found` | OpenAI `image_gen`; fictional 1936-1945 manifesto-discovery report scene | `docs/assets/015_utopia_manifesto/source_png/report_event_utopia_manifesto_found_source.png` (`1369x1149`) | `18aceefe049b6f842d695cdf95d7588b319ced45699801f0115dbdb1018fead3` | `docs/assets/015_utopia_manifesto/processed_png/report_event_utopia_manifesto_found.png` (`210x176`) | former derivative at the current runtime path | `36783e46587bd593716140ebeb15b0eecfcc86b0f5e1dfed5d610b132592a86a` | historical; superseded by final package |
| `news_event_utopia_boundary_crisis` | OpenAI `image_gen`; fictional 1936-1945 boundary-inspection news scene | `docs/assets/015_utopia_manifesto/source_png/news_event_utopia_boundary_crisis_source.png` (`2020x778`) | `734958fe691ccc4ac116e003635f6147dd19c6ae1c2b480d7f4c026075ba526e` | `docs/assets/015_utopia_manifesto/processed_png/news_event_utopia_boundary_crisis.png` (`397x153`) | `gfx/event_pictures/015_utopia_manifesto/news_event_utopia_boundary_crisis.dds` | `7c4a7fa5ee44eb2ddd1f2d08fac3ce59958b09c701a51ff44669a54ddc79d7be` | installed and traceable |
| `super_event_utopia_new_utopia` | OpenAI `image_gen`; fictional proclamation scene from the superseded two-image presentation | `docs/assets/015_utopia_manifesto/source_png/super_event_utopia_new_utopia_source.png` (`1479x1063`) | `5fddc71b2a5a8aaf4b5f5f2a406f199b614fc7d99b4a403037d3644801ff5f81` | `docs/assets/015_utopia_manifesto/processed_png/super_event_utopia_new_utopia.png` (`457x328`) | `gfx/super_events/015_utopia_manifesto/super_event_utopia_new_utopia.dds` | `06606c3b38feaac7823bebdcaaa94a678efabdf0d7ac2c38463f1ddbebb954d4` | installed, traceable, legacy/unselected |
| `super_event_utopia_marked_bounds` | OpenAI `image_gen`; fictional frontier-survey scene from the superseded two-image presentation | `docs/assets/015_utopia_manifesto/source_png/super_event_utopia_marked_bounds_source.png` (`1479x1064`) | `5d57fd6b9d3d39618a1a0e1cafacdd7f406ab4137fbafbc33b7bea9023f16802` | `docs/assets/015_utopia_manifesto/processed_png/super_event_utopia_marked_bounds.png` (`457x328`) | `gfx/super_events/015_utopia_manifesto/super_event_utopia_marked_bounds.dds` | `b58b7157af42943d38f1a7327bbf24ae5a365d4bfb63c182c5a5baea3df44ed9` | installed, traceable, legacy/unselected |

The report image received the repository report-card treatment. The news and legacy super-event images were normalized to monochrome. These local derivatives do not introduce a separate third-party source.

### Current route-specific super-event package

`interface/015_utopia_manifesto_super_event.gfx` and `GetSuperEventImage` select five route-specific sprites for display slots `96` through `100`. Every slot now has a distinct generated source master, processed preview, package DDS, runtime DDS, and checksum record:

| Display slot | Required sprite | Required runtime DDS | Source status |
| --- | --- | --- | --- |
| `96` | `GFX_super_event_015_consent_of_households` | `gfx/super_events/015_utopia_manifesto/super_event_015_consent_of_households.dds` | complete and registered |
| `97` | `GFX_super_event_015_common_table` | `gfx/super_events/015_utopia_manifesto/super_event_015_common_table.dds` | complete and registered |
| `98` | `GFX_super_event_015_guardians_of_measure` | `gfx/super_events/015_utopia_manifesto/super_event_015_guardians_of_measure.dds` | complete and registered |
| `99` | `GFX_super_event_015_closed_island` | `gfx/super_events/015_utopia_manifesto/super_event_015_closed_island.dds` | complete and registered |
| `100` | `GFX_super_event_015_joke_understood` | `gfx/super_events/015_utopia_manifesto/super_event_015_joke_understood.dds` | complete and registered |

The two installed legacy super-event images remain historical assets and are not used as fallbacks for these five route-specific sprites.

## 2026-07-14 Final Non-Icon Event-Art Package

Scope: the complete generated runtime package requested for Event 015—`14` report pictures, `3` news pictures, and `5` route super-event pictures.

- Authoritative manifest with per-asset source, processed, and runtime checksums: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/manifest.md`
- Machine-readable records: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/asset_records.json`
- Preserved source masters: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/source_png/`
- Processed previews: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/processed_png/`
- Package DDS copies: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/dds/`
- Decoded DDS review PNGs: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/decoded_png/`
- Visual review sheets: `docs/assets/015_utopia_manifesto/final_non_icon_2026_07_14/contact_sheets/`
- Exact parent registration handoff: `docs/assets/015_utopia_manifesto/gfx_handoff.md`

Every report output is `210x176` with transparent report-card corners; every news output is `397x153`; every route super-event output is `457x328`. The processor validates the legacy uncompressed 32-bit BGRA DDS header, channel masks, exact byte length, dimensions, expected alpha behavior, source/final existence, and per-family checksum uniqueness. Final and source contact sheets were visually reviewed; the rejected blank-card variants of `necessary_ground` and `stewardship` are preserved for audit and are not selected by any derivative.

The asset package has no fallback sources, prompt-only rows, missing runtime DDS files, placeholder art, or visual simplifications. Parent integration remains limited to adding the `13` unregistered report sprites and `3` news sprites to `interface/015_utopia_manifesto.gfx`, switching current script references from the superseded `military` picture name to the exact `defense` identity, and assigning the three additional report identities (`island`, `foreign_commonwealth`, and `formation`) where intended by the event design.

## 2026-07-14 Final Exact Icon and Authored-Frame Package

Scope: focus-use audit, exact current idea coverage, final decision/category sprite handoff, exact current achievement triplets, and the three Ledger animations requested by their live sprite ids. This pass does not alter report/news/super-event art, flags, portraits, gameplay script, or localisation.

### Imagegen source records

Canonical prompt record: `docs/assets/015_utopia_manifesto/prompts/final_icon_frame_generation.md`

Frozen generated masters:

- `source_png/final_icons/utopia_final_decision_category_imagegen_atlas.png` (`5x6`, 30 ordered subjects, flat magenta extraction field)
- `source_png/final_icons/utopia_final_idea_imagegen_atlas.png` (`5x2`, 10 ordered subjects, flat magenta extraction field)
- `source_png/final_icons/utopia_final_achievement_imagegen_atlas.png` (`4x4`, 14 ordered medallions and two empty cells)
- `animations/utopia_need_warning/source_storyboards/utopia_need_warning_imagegen_storyboard.png` (`4x2`, eight authored states)
- `animations/utopia_reserve_fill/source_storyboards/utopia_reserve_fill_imagegen_storyboard.png` (`4x2`, eight authored inventory states)
- `animations/utopia_formation_ready_seal/source_storyboards/utopia_formation_ready_seal_imagegen_storyboard.png` (`5x2`, ten authored relief/light states)

Local work after generation was mechanical: fixed-grid crop, the installed imagegen chroma helper, alpha fitting, exact-size export, achievement grayscale/mandated-overlay variants, sheet assembly, preview generation, and repository DDS conversion. No animation is a transform-only loop of one still; every source frame has a distinct checksum.

### Current focus-use audit

| Metric | Result |
| --- | --- |
| Focus `icon = GFX_goal_utopia_*` usages | `122` |
| Unique current focus sprite ids | `72` |
| Matching base definitions | `72/72` |
| Matching `_shine` definitions | `72/72` |
| Current texture size | `94x86` |
| Physical family DDS files retained | `109` (`37` not referenced by the current tree) |

No focus icon source or runtime file was regenerated in this pass because every current usage already had a final registered texture.

### Decision, mission, and category package

- Exact handoff: `decision_icon_mapping.csv`
- Current rows: `139` (`9` categories, `98` decisions, `32` missions)
- Newly generated sprite files: `30` (`7` category sprites and `23` decision-family sprites)
- Reused final Event 015 family sprites: `25`
- Every mapped sprite definition resolves to a `32x32` DDS.
- The mapping generator parses the live decision file and refuses missing, duplicate, or stale ids.
- Integration blocker: the current gameplay file still contains zero `icon =` assignments. The parent implementation agent must apply the CSV's exact `icon_value` column; this asset pass does not edit gameplay.

### Current ideas

The current `50` idea entries use these `12` unique picture tokens:

- `utopia_found_manifesto`
- `utopia_unmeasured_country`
- `utopia_inherited_order`
- `utopia_charter_of_households`
- `utopia_common_table`
- `utopia_perfect_measure`
- `utopia_closed_island`
- `utopia_practical_commonwealth`
- `utopia_common_store_network`
- `utopia_garden_district_network`
- `utopia_auxiliary_dependency`
- `utopia_stewardship_burden`

The ten previously missing exact sprites were generated and registered. All twelve current pictures now resolve to `64x64` DDS files.

### Current achievements

Exact achievement ids, each with base, `_grey`, and `_not_eligible` runtime files:

- `utopia_manifesto_no_place_but_home`
- `utopia_manifesto_need_not_greed`
- `utopia_manifesto_every_calling_chosen`
- `utopia_manifesto_two_year_table`
- `utopia_manifesto_archipelago_of_small_places`
- `utopia_manifesto_inland_island`
- `utopia_manifesto_gold_for_common_use`
- `utopia_manifesto_the_joke_understood`
- `utopia_manifesto_consent_of_the_governed`
- `utopia_manifesto_the_perfect_measure`
- `utopia_manifesto_closed_circle`
- `utopia_manifesto_no_foreign_hands`
- `utopia_manifesto_the_stores_remain`
- `utopia_manifesto_no_one_in_chains`

The `_not_eligible` variant is the grayscale variant composited with `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/overlay.png`. The final `42` files are `64x64` uncompressed BGRA DDS with one mip level and exact aliases in `interface/015_utopia_manifesto.gfx`.

The older `015_utopia_*` set remains a historical package only. Its `36` runtime files were not deleted because `docs/plans/015_utopia_manifesto_plans/repo_explorer_handoff.md` still references them.

### Required live animations

| Sprite pair | Authored source frames | Frame size | Sheet size | Playback | Static fallback frame |
| --- | ---: | --- | --- | --- | ---: |
| `GFX_utopia_need_warning_{static,animated}` | `8` | `64x64` | `512x64` | `5 fps`, loop, play on show | `004` (peak warning) |
| `GFX_utopia_reserve_fill_{static,animated}` | `8` | `300x24` | `2400x24` | `4 fps`, loop, play on show | `004` (full inspected reserve) |
| `GFX_utopia_formation_ready_seal_{static,animated}` | `10` | `96x96` | `960x96` | `5 fps`, loop, play on show | `005` (complete formation ring) |

Each animation package contains its brief, frame plan, frozen storyboard, separate source frames, separate processed frames, exact sheet PNG, static PNG, final sheet/static DDS, contact sheet, and GIF preview. The formation flare is processed through the same shared source crop and scale as the other seal frames so its apparent seal size does not jump.

### Runtime registry and audit evidence

- Registry: `interface/015_utopia_manifesto.gfx`
- Live GUI: `interface/015_utopia_manifesto_ledger.gui`
- Live GUI sprite coverage: `6/6` definitions and textures
- Corrected GUI texture root: `gfx/interface/015_utopia_manifesto/`
- Audit command: `python docs/assets/015_utopia_manifesto/_tooling/audit_final_icon_frame_package.py`
- Audit record: `docs/assets/015_utopia_manifesto/final_icon_frame_audit.json`
- Visual review contacts:
  - `processed_png/final_icons/utopia_final_decision_category_contact.png`
  - `processed_png/final_icons/utopia_final_idea_contact.png`
  - `processed_png/final_icons/utopia_final_achievement_contact.png`
  - `processed_png/final_icons/utopia_final_achievement_triplets_contact.png`
  - `animations/utopia_need_warning/previews/utopia_need_warning_contact.png`
  - `animations/utopia_reserve_fill/previews/utopia_reserve_fill_contact.png`
  - `animations/utopia_formation_ready_seal/previews/utopia_formation_ready_seal_contact.png`

## 2026-07-01 Focus Icon Regeneration

Scope: focus icons only.

The full Event 015 focus icon family was regenerated from actual imagegen source art after the previous focus pack was rejected as placeholder-like. The pass covers all 109 existing `goal_utopia_*` runtime focus DDS files under `gfx/interface/goals/015_utopia_manifesto/`. The current tree uses `72` of those sprites across `122` focus icon assignments; the remaining `37` files are retained family art.

Source mode:

- Seven imagegen-generated focus atlases were copied into `docs/assets/015_utopia_manifesto/source_png/` as `focus_atlas_*_imagegen_atlas.png`.
- Each `<stem>_source.png` focus source is a crop from one of those imagegen atlases.
- Local processing was limited to chroma-key removal, transparent cropping/fitting, 94x86 resizing, contact-sheet creation, and DDS export.
- No primitive shape, local-script-only, or white-square placeholder source art was used for regenerated focus icons.

Updated focus deliverables:

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/goal_utopia_*_source.png`
- Processed previews: `docs/assets/015_utopia_manifesto/processed_png/goal_utopia_*.png`
- Package DDS copies: `docs/assets/015_utopia_manifesto/dds/goal_utopia_*.dds`
- Runtime DDS files: `gfx/interface/goals/015_utopia_manifesto/goal_utopia_*.dds`
- Review sheets:
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_01.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_02.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_03.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_04.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/focus_regenerated_imagegen_contact_all.png`

Validation summary:

- Focus DDS coverage: 109 regenerated, 109 runtime `goal_utopia_*` files present.
- Target size: every regenerated focus DDS is 94x86.
- Transparency: regenerated focus DDS files have transparent unused corners and no opaque white square background.
- Visual review: contact sheets were inspected after a second matte pass to remove visible chroma-key edge artifacts.

Blocked focus icons: none.

Needs parent review: none flagged by this pass.

## Historical 2026-07-01 Decision and Idea Icon Regeneration

Scope at the time: decision, decision-category, and idea icons only. This section records the earlier family-generation tranche; current exact coverage and counts are superseded by the `2026-07-14 Final Exact Icon and Authored-Frame Package` section above.

The Event 015 runtime decision/category and idea icon families were regenerated from actual imagegen source art after placeholder, simple-shape, white-background, and misalignment concerns were raised. This pass covers all 25 existing runtime `*.dds` files under `gfx/interface/decisions/015_utopia_manifesto/` and all 31 existing runtime `*.dds` files under `gfx/interface/ideas/015_utopia_manifesto/`.

Source mode:

- Three imagegen-generated atlases were copied into `docs/assets/015_utopia_manifesto/source_png/` as:
  - `decision_idea_regenerated_imagegen_decision_atlas_source.png`
  - `decision_idea_regenerated_imagegen_idea_atlas_01_source.png`
  - `decision_idea_regenerated_imagegen_idea_atlas_02_source.png`
- `idea_utopia_common_stores_unproven_source.png` uses a separate imagegen-generated replacement source because the first idea atlas cell produced an explicit question-mark prop.
- Each final `<stem>_source.png` decision or idea source derives from imagegen output.
- Local processing was limited to atlas cropping, chroma-key removal, transparent fitting, restrained outline/drop shadow, exact-size resizing, contact-sheet creation, and DDS export.
- No primitive shape, local-script-only, or white-square placeholder source art was used for regenerated decision/category or idea icons.

Updated decision and idea deliverables:

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/decision_*_source.png` and `docs/assets/015_utopia_manifesto/source_png/idea_*_source.png`
- Processed previews: `docs/assets/015_utopia_manifesto/processed_png/decision_*.png` and `docs/assets/015_utopia_manifesto/processed_png/idea_*.png`
- Package DDS copies: `docs/assets/015_utopia_manifesto/dds/decision_*.dds` and `docs/assets/015_utopia_manifesto/dds/idea_*.dds`
- Runtime DDS files:
  - `gfx/interface/decisions/015_utopia_manifesto/*.dds`
  - `gfx/interface/ideas/015_utopia_manifesto/*.dds`
- Review sheets:
  - `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_decisions.png`
  - `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_ideas.png`

Validation summary:

- Decision/category DDS coverage: 25 regenerated, 25 runtime files present.
- Idea DDS coverage: 31 regenerated, 31 runtime files present.
- Target size: every regenerated decision/category DDS is 32x32; every regenerated idea DDS is 64x64.
- Transparency: regenerated runtime DDS files have transparent unused corners and no opaque white square background.
- Visual review: contact sheets were inspected over checker backgrounds for alignment, white-square backgrounds, and chroma-key remnants.

Blocked decision or idea icons: none.

Needs parent review: none flagged by this pass.

## Historical 2026-07-01 Achievement Icon Regeneration

Scope at the time: Event 015 achievement icons and their disabled variants. This section records the superseded `015_utopia_*` package; the exact current 14-id package is documented in the `2026-07-14 Final Exact Icon and Authored-Frame Package` section above.

The Event 015 achievement icon family was regenerated from actual imagegen source art after parent review found the earlier achievement contact sheet still looked like flat placeholder emblems. This pass covers all 12 achievement stems and their `_grey` and `_not_eligible` variants.

Updated achievement deliverables:

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/015_utopia_*_source.png`
- Processed previews: `docs/assets/015_utopia_manifesto/processed_png/015_utopia_*.png`
- Package DDS copies: `docs/assets/015_utopia_manifesto/dds/015_utopia_*.dds`
- Runtime DDS triplets: `gfx/achievements/015_utopia_*.dds`
- Review sheet: `docs/assets/015_utopia_manifesto/contact_sheets/achievements_regenerated_imagegen_contact.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_achievement_icon_regeneration.md`

Validation summary:

- Achievement DDS coverage: 12 stems with base, `_grey`, and `_not_eligible` variants; 36 runtime files present.
- Target size: every regenerated achievement DDS is 64x64.
- Visual review: contact sheet was inspected for imagegen-backed medal art, disabled variants, and absence of white square backgrounds.

Blocked achievement icons: none.

## 2026-07-01 Cosmetic Flag Generation

Scope: late-route cosmetic identity flags.

Four late cosmetic identities were generated from actual imagegen source art and exported into the project-standard HOI4 flag folders.

Runtime flag deliverables:

- `gfx/flags/utopia_new_utopia.tga`
- `gfx/flags/utopia_necessary_commonwealth.tga`
- `gfx/flags/utopia_league_of_need.tga`
- `gfx/flags/utopia_marked_bounds_state.tga`
- matching `gfx/flags/medium/` and `gfx/flags/small/` copies
- ideology-specific copies for each tag in normal, medium, and small folders:
  - `_democratic.tga`
  - `_communism.tga`
  - `_fascism.tga`
  - `_neutrality.tga`

Review and source files:

- Source PNGs: `docs/assets/015_utopia_manifesto/source_png/flag_utopia_*_source.png`
- Processed PNGs: `docs/assets/015_utopia_manifesto/processed_png/flag_utopia_*_processed.png`
- Contact sheet: `docs/assets/015_utopia_manifesto/contact_sheets/utopia_cosmetic_flags_imagegen_contact.png`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_cosmetic_flag_asset_handoff.md`

Validation summary:

- Normal flags are 82x52, medium flags are 41x26, and small flags are 10x7.
- Final TGAs match the repo's existing flag pattern and remain visually distinct at small size.
- Parent follow-up after the country-package-adjacent audit added all ideology-specific flag variants from the generated base flags, closing the runtime cosmetic-flag fallback risk for countries with ideology-specific original flags.

## Historical 2026-07-01 Runtime Ledger Panel and Animation Regeneration

Scope at the time: the original runtime Ledger family. Its physical files remain registered under the corrected `gfx/interface/015_utopia_manifesto/` root, but only `GFX_utopia_ledger_seal_animated` from this older animation set is referenced by the current Ledger GUI. The three current live animation additions are documented in the `2026-07-14 Final Exact Icon and Authored-Frame Package` section above.

The Event 015 Ledger panels and animated GUI pieces were regenerated from actual imagegen source art after the runtime UI folder was rejected as visually weak. This pass covers all 13 retained runtime DDS files in `gfx/interface/015_utopia_manifesto/`, including static panels, animated frame sheets, and static fallbacks.

Source mode:

- Imagegen-generated sources were copied into `docs/assets/015_utopia_manifesto/source_png/` as `utopia_*_source.png` and `utopia_*_sheet_source.png`.
- Animated pieces were processed into discrete per-frame source PNGs under `docs/assets/015_utopia_manifesto/animations/<asset>/source_frames/`.
- Local processing was limited to transparent extraction, frame fitting, sheet construction, contact/previews, DDS export, and staging copies.
- No primitive shape, local-script-only, single-still transform-only, or white-square placeholder source art was used for the regenerated Ledger runtime family.

Updated runtime deliverables:

- `gfx/interface/015_utopia_manifesto/utopia_ledger_background_panel.dds` (`700x500`)
- `gfx/interface/015_utopia_manifesto/utopia_ledger_header_plate.dds` (`700x96`)
- `gfx/interface/015_utopia_manifesto/utopia_ledger_warning_panel.dds` (`320x128`)
- `gfx/interface/015_utopia_manifesto/utopia_ledger_seal_sheet.dds` (`512x64`, 8 frames)
- `gfx/interface/015_utopia_manifesto/utopia_ledger_seal_static.dds` (`64x64`)
- `gfx/interface/015_utopia_manifesto/utopia_overreach_warning_sheet.dds` (`512x64`, 8 frames)
- `gfx/interface/015_utopia_manifesto/utopia_overreach_warning_static.dds` (`64x64`)
- `gfx/interface/015_utopia_manifesto/utopia_storehouse_fill_sheet.dds` (`512x16`, 8 frames)
- `gfx/interface/015_utopia_manifesto/utopia_storehouse_fill_static.dds` (`64x16`)
- `gfx/interface/015_utopia_manifesto/utopia_new_utopia_seal_sheet.dds` (`960x96`, 10 frames)
- `gfx/interface/015_utopia_manifesto/utopia_new_utopia_seal_static.dds` (`96x96`)
- `gfx/interface/015_utopia_manifesto/utopia_marked_bounds_seal_sheet.dds` (`960x96`, 10 frames)
- `gfx/interface/015_utopia_manifesto/utopia_marked_bounds_seal_static.dds` (`96x96`)

Review files:

- Panel contact sheet: `docs/assets/015_utopia_manifesto/contact_sheets/utopia_runtime_panels_regenerated_contact.png`
- Animation contact sheets and preview GIFs: `docs/assets/015_utopia_manifesto/animations/<asset>/previews/`
- Handoff: `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/2026-07-01_runtime_gui_animation_regeneration.md`

Current runtime wiring status for this historical set:

- `GFX_utopia_ledger_seal_animated` remains visible in the Utopian Ledger header.
- `GFX_utopia_overreach_warning_animated`, `GFX_utopia_storehouse_fill_animated`, `GFX_utopia_new_utopia_seal_animated`, and `GFX_utopia_marked_bounds_seal_animated` remain registered with valid textures but are not referenced by the current Ledger GUI.

Validation summary:

- All 13 runtime DDS files exist with expected dimensions.
- Animated sheets have the expected frame counts: Ledger seal 8, Overreach warning 8, Storehouse fill 8, New Utopia seal 10, Marked Bounds seal 10.
- Runtime sprites are registered in `interface/015_utopia_manifesto.gfx`; current `.gui` use is limited as stated above.
- Contact sheets were visually inspected for panel readability, centered transparent icons, frame distinction, and lack of white matte.

All animated GUI pieces are built from discrete generated source frames, not transform-only movement of a single still. Each animated asset has:

- source frame PNGs
- processed frame PNGs
- sheet PNG
- final sheet DDS
- static fallback DDS
- contact sheet or GIF preview

Runtime use:

- All five historical sprites remain registered, but only `GFX_utopia_ledger_seal_animated` is referenced by the current Ledger GUI. The live Need, reserve, and formation-ready pieces use the separately documented 2026-07-14 animation package.

## Validation Notes

- Icon families were regenerated through subagent imagegen passes for focus, decision/category, idea, and achievement icons.
- Cosmetic flags were generated through a separate imagegen asset sidecar.
- `interface/015_utopia_manifesto_super_event.gfx` registers all five current route super-event images. The general `interface/015_utopia_manifesto.gfx` still needs the exact `16` report/news blocks documented in `gfx_handoff.md`.
- The parent implementation validation pass must confirm that every Event 015 `GFX_*` reference resolves after applying that registration handoff and the documented `military`-to-`defense` script alignment.
