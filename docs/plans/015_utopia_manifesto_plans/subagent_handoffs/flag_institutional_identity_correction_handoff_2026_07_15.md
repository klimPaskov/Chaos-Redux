# Event 015 flag and institutional identity correction handoff

Handoff date: `2026-07-15`

Subagent: `chaosx_generated_event_art`

Scope: exact Event 015 cosmetic-tag flag stems and the four existing institutional leader portrait textures only

## Outcome

The active Event 015 identity package no longer derives flags or institutional portraits from the old atlases.

- `21` distinct cosmetic-flag compositions have individual OpenAI built-in ImageGen source masters and recorded call handles.
- The exact `25` wired flag stems are installed at `82x52`, `41x26`, and `10x7`; only four documented unsuffixed/canonical pairs repeat art.
- Final flags are solid-fill, texture-free designs produced from the generated compositions without local motif drawing, procedural geometry, or palette-only variant creation.
- Four institutional leader textures have individual built-in ImageGen collective masters and visibly match the bundled vanilla HOI4 painted leader style.
- All four portraits were processed with the official portrait processor, an explicit crop, `source-kind collective`, per-asset metadata, individual vanilla comparison sheets, and `156x210` DDS output.
- Runtime files replace the existing TGA/DDS targets in place. No gameplay, character, localisation, `.gfx`, interface, or scripted-GUI file was edited.

## Exact flag source map

| Wired stem | Active source evidence |
| --- | --- |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH` | exact alias of `_democratic` |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_democratic` | `exec-d221430b-6b27-4ee3-86d9-ce9b79ef8471` |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_communism` | `exec-637487dd-a5a2-4ffd-98e3-e5095026979a` |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_neutrality` | `exec-e2e2e1b7-94f4-42a7-8dec-2dc2b8d4a7dc` |
| `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_fascism` | `exec-4bfd5bd2-6634-4f2b-b06a-27a81723c8d7` |
| `UTOPIA_MANIFESTO_COUNCIL_UNION` | exact alias of `_communism` |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_democratic` | `exec-166408fb-5532-49a1-98a9-7931534ce029` |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_communism` | `exec-a213e972-6856-429d-9b8d-a47a37d6ac06` |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_neutrality` | `exec-18384790-b692-41fc-82f8-2c3caba11393` |
| `UTOPIA_MANIFESTO_COUNCIL_UNION_fascism` | `exec-d90ef2e5-098f-44c9-8ed8-893d4052cb73` |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA` | exact alias of `_neutrality` |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_democratic` | `exec-eabafa44-47d8-45c9-98de-7a8a0fbedde2` |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_communism` | `exec-6bb7fe09-3064-4e3a-9a82-9a8c1d1770a2` |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality` | `exec-456c432e-2b37-4ae7-a380-52d7733a500c` |
| `UTOPIA_MANIFESTO_PLANNED_UTOPIA_fascism` | `exec-51695f4d-df59-4963-9802-28b774cc60d3` |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND` | exact alias of `_fascism` |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_democratic` | `exec-a2424d89-6954-42f7-bb42-7ff1e047be13` |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_communism` | `exec-9ebdee8a-a027-4499-aa3e-8b737e0c145e` |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_neutrality` | `exec-91acc487-c80c-4436-a40c-330d7c2a1609` |
| `UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism` | `exec-d3bea27e-81b9-4edb-990d-4f1e8cd5a674` |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH` | `exec-912fb135-9772-4900-acce-20bc32f1fc66` |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_democratic` | `exec-74a82e3c-4309-4148-b459-1c2dbf753ecb` |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_communism` | `exec-acee6c41-999a-403f-bd38-07c60ea9691e` |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_neutrality` | `exec-5bc343f9-6007-4b76-9943-1de4da3c7802` |
| `UTOPIA_MANIFESTO_PRACTICAL_COMMONWEALTH_fascism` | `exec-4e4f5847-f124-4dcb-9ab2-798e90a69bbd` |

Every active master is preserved under `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/flags/`. The exact source hash, source dimensions, call handle, processed hash, package path, runtime path, and runtime hash are recorded in both `flag_identity_asset_records.json` and the merged `asset_records.json`.

### Intentional aliases

- `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH` → `UTOPIA_MANIFESTO_VOLUNTARY_COMMONWEALTH_democratic`
- `UTOPIA_MANIFESTO_COUNCIL_UNION` → `UTOPIA_MANIFESTO_COUNCIL_UNION_communism`
- `UTOPIA_MANIFESTO_PLANNED_UTOPIA` → `UTOPIA_MANIFESTO_PLANNED_UTOPIA_neutrality`
- `UTOPIA_MANIFESTO_CLOSED_ISLAND` → `UTOPIA_MANIFESTO_CLOSED_ISLAND_fascism`

For every alias, source PNG, processed PNG, package TGA, and runtime TGA are exact byte copies of the canonical composition at every engine size. Practical Commonwealth has no alias.

## Flag finishing and review

The source compositions were center-fitted independently at each engine size. A deterministic maximum-six-color normalization with no dithering removed low-level generated tonal variation and collapsed border shading. It did not synthesize or redraw any symbol.

The runtime contract is:

- `gfx/flags/<stem>.tga` — `82x52`
- `gfx/flags/medium/<stem>.tga` — `41x26`
- `gfx/flags/small/<stem>.tga` — `10x7`
- uncompressed `32`-bit TGA, fully opaque alpha, bottom-left origin, descriptor `8`

Review sheets:

- `contact_sheets/flags_corrected_imagegen_source_contact_sheet.png`
- `contact_sheets/flags_corrected_decoded_contact_sheet.png`
- `contact_sheets/flags_corrected_small_10x7_readability_contact_sheet.png`
- `contact_sheets/flag_size_ladder_decoded_contact_sheet.png`

The 82×52 sheet was reviewed for flatness, motif separation, route identity, and absence of text, fabric, painterly staging, real flags, and political/extremist symbols. The enlarged native `10x7` sheet was reviewed for surviving silhouette and color-block identity.

## Institutional portrait source map

| Existing texture/handle family | Active built-in source | Processor record |
| --- | --- | --- |
| `leader_household_assembly.dds` / `GFX_portrait_utopia_manifesto_household_assembly` | `exec-59ff2fa1-755d-4e86-9df8-1a9586d9f629` | `metadata/institutional_portraits/leader_household_assembly.json` |
| `leader_council_of_callings.dds` / `GFX_portrait_utopia_manifesto_council_of_callings` | `exec-db5ac931-dd5a-4f4c-b56c-f0a13d7ced05` | `metadata/institutional_portraits/leader_council_of_callings.json` |
| `leader_board_of_measure.dds` / `GFX_portrait_utopia_manifesto_board_of_measure` | `exec-a710c8a9-e1bc-4b67-bc73-da2db13f8851` | `metadata/institutional_portraits/leader_board_of_measure.json` |
| `leader_stewardship_council.dds` / `GFX_portrait_utopia_manifesto_stewardship_council` | `exec-6fae8a6d-e911-4667-b258-f8173bdf73df` | `metadata/institutional_portraits/leader_stewardship_council.json` |

Each source is an original fictional three-person institutional collective. The bundled vanilla leader portraits were passed as style references only. The resulting sources use close bust grouping, period civilian clothing, subdued painted values, restrained edges, and quiet backgrounds rather than wide scenes, tiny figures, photography, or modern concept-art rendering.

Processing was identical and explicit for all four:

- `.tools/process_hoi4_portrait.py leader`
- crop `[5, 0, 1075, 1440]`
- `--source-kind collective`
- output `156x210`
- per-portrait comparison against `assets/leader_portraits`
- `.tools/convert_to_dds.py --width 156 --height 210`

Review sheets:

- `contact_sheets/institutional_portraits_corrected_source_contact_sheet.png`
- `contact_sheets/institutional_portraits_corrected_processed_contact_sheet.png`
- `contact_sheets/institutional_reviews/leader_household_assembly_comparison.png`
- `contact_sheets/institutional_reviews/leader_council_of_callings_comparison.png`
- `contact_sheets/institutional_reviews/leader_board_of_measure_comparison.png`
- `contact_sheets/institutional_reviews/leader_stewardship_council_comparison.png`

All four metadata records have status `approved_after_visual_comparison`.

## Rejected source outputs

The correction rejected and replaced six built-in outputs before the final package:

- initial Voluntary Commonwealth democratic composition — insufficient five-house clarity
- initial Planned Utopia neutrality composition — compass-rose rather than drafting-divider reading
- Voluntary Commonwealth neutrality — arrow-like marks rather than houses
- Practical Commonwealth neutrality — oil/genie lamp rather than municipal streetlight
- Council Union democratic — crossed hammer-like tools and sickle-adjacent form
- Council Union communism — hammer/sickle-adjacent political-symbol risk

Full rejected handles and reasons are preserved in `prompts/corrected_flag_and_institutional_prompts_2026_07_15.md`. None of those files is copied into an active source path.

## Validation evidence

Focused flag validation: `flag_identity_validation_2026_07_15.json`

- exact `25`-stem coverage at all three sizes (`75` TGA files)
- `21` unique independent main-size hashes with built-in handles
- four documented aliases byte-identical to their canonical files at every size
- bottom-left TGA header, origin, dimensions, opacity, file length, decode, and processed-pixel equality
- all five ideology families contain four distinct ideology hashes

Focused institutional validation: `institutional_portrait_validation_2026_07_15.json`

- four distinct source and processed hashes
- `source-kind collective`, explicit crop, built-in handle, and comparison path recorded for every portrait
- `156x210` one-level uncompressed BGRA DDS contract
- package/runtime byte equality and decoded-DDS/processed-PNG pixel equality

Built-in source evidence: `imagegen_source_evidence_2026_07_15.json`

- `25` independent active sources (`21` flags and `4` institutional portraits)
- `25` distinct built-in handles
- every packaged source PNG is an exact byte copy of the built-in output named by its handle

Aggregate package validation was rebuilt after merging the concurrent advisor correction. `validation.json` validates `100` runtime outputs: `75` flags, `4` institutional portraits, `16` advisors, and `5` league emblems. `checksums.sha256` matches that merged package.

## Files changed in this correction

- `gfx/flags/UTOPIA_MANIFESTO_*.tga`
- `gfx/flags/medium/UTOPIA_MANIFESTO_*.tga`
- `gfx/flags/small/UTOPIA_MANIFESTO_*.tga`
- `gfx/leaders/015_utopia_manifesto/leader_*.dds` for the four institutional textures
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/flags/**`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/source_png/institutional_portraits/**`
- matching processed, final, decoded, metadata, contact-sheet, prompt, record, checksum, validation, and tooling files inside the same package
- package `manifest.md`, `gfx_handoff.md`, `asset_records.json`, and aggregate `validation.json`
- this handoff and the supersession note in `route_identity_asset_handoff.md`

No gameplay, localisation, characters, `.gfx`, interface, scripted-GUI, decision, event, focus, or spreadsheet file was edited.

## Skills and references used

- `chaos-redux-event-assets`
- `chaos-redux-subagents`
- official `imagegen`

Required offline wiki core pages were consulted together with Interface Modding, Portrait Modding, and Country Creation. Vanilla documentation was inspected, vanilla flag formats were mirrored, and bundled vanilla leader-portrait references were used for the required style comparisons.

No skill was created or updated; this correction did not reveal a reusable workflow gap beyond the existing asset and ImageGen guidance.

## Simplifications, omissions, and blockers

- Simplifications: none.
- Fallbacks: none.
- Missing requested assets: none.
- Unwired requested assets: none; these files replace existing runtime targets and require no reference change.
- Residual asset-quality blocker: none after the six rejected calls were replaced.
- Parent action: review the scoped correction alongside the concurrent advisor package and include the shared manifest/record changes in the integrated Event 015 commit.
