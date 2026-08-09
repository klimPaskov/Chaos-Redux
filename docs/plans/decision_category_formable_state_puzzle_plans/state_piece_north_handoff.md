# Northern formable state-piece runtime handoff

## Scope

This handoff covers exactly five live formables: `form_scandinavia_category`/`form_scandinavia`, `form_north_sea_category`/`form_north_sea_empire`, `form_baltic_sea_empire_category`/`form_baltic_sea_empire`, `form_baltic_federation_category`/`form_baltic_federation`, and `form_sweden_hungary_category`/`proclaim_sweden_hungary`.

Nordic League is explicitly excluded.

The reviewed legacy manifest shape was retained because the strict compatibility adapter in `.tools/generate_formable_state_puzzle_runtime.mjs` accepts each manifest after all runtime references were installed.

## Map and MCP evidence

All five reviewed packages use map revision `b69b583264f11454ac4a5975145ec632c881dea0d0e078be523facd0c2854333` and installed map SHA-256 `e131d30e5dcb13d9c2a8598f820a2de0ae9828f3a24f2bddc1bcfff40f71660a`.

The mandatory map-inspect artifact URI recorded in each manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6b8d783cc00af7749dd438d627312544b5578497f3ff9b68529f4dc05740704/b872d793d0517080dd9db46c113fe5df89a9fb0c698c5cec0bfecc010f3dea8c/map-inspect.b69b583264f11454.json`.

The canonical reviewed geometry artifacts are the `*_geometry_artifact.json` files beside each manifest, and their SHA-256 values remain unchanged in the manifests.

## Exact state sets and reviewed files

### Scandinavia

Source of truth: `docs/formables/state_puzzles/form_scandinavia_category/manifest.json`.

Geometry and review files: `docs/formables/state_puzzles/form_scandinavia_category/form_scandinavia_category_geometry_artifact.json`, `form_scandinavia_category_contact_sheet.png`, `form_scandinavia_category_projection_440x180.png`, and `form_scandinavia_category_projection_440x180_qualifying.png`.

State groups: Norway `{110, 142, 143, 144, 920, 921, 922, 923, 924, 925}`; Sweden `{38, 124, 138, 139, 140, 141, 666, 913, 915, 916, 917, 918, 919}`; Denmark `{37, 99, 337, 910, 911, 912}`.

The package contains 29 states and 58 unresolved/qualifying assets under `docs/formables/state_puzzles/form_scandinavia_category/{source,processed}/` and `gfx/interface/formables/state_puzzles/form_scandinavia_category/states/`.

### North Sea Empire

Source of truth: `docs/formables/state_puzzles/form_north_sea_category/manifest.json`.

Geometry and review files: `docs/formables/state_puzzles/form_north_sea_category/form_north_sea_category_geometry_artifact.json`, `form_north_sea_category_contact_sheet.png`, `form_north_sea_category_projection_440x180.png`, and `form_north_sea_category_projection_440x180_qualifying.png`.

State groups: Norway `{110, 142, 143, 144, 920, 921, 922, 923, 924, 925}`; Denmark `{37, 99, 911, 912}`; Sweden `{138, 915}`; England `{123, 125, 126, 127, 128, 129, 130, 131, 931, 932, 132, 338}`.

The package contains 28 states and 56 unresolved/qualifying assets under `docs/formables/state_puzzles/form_north_sea_category/{source,processed}/` and `gfx/interface/formables/state_puzzles/form_north_sea_category/states/`.

### Baltic Sea Empire

Source of truth: `docs/formables/state_puzzles/form_baltic_sea_empire_category/manifest.json`.

Geometry and review files: `docs/formables/state_puzzles/form_baltic_sea_empire_category/form_baltic_sea_empire_category_geometry_artifact.json`, `form_baltic_sea_empire_category_contact_sheet.png`, `form_baltic_sea_empire_category_projection_440x180.png`, and `form_baltic_sea_empire_category_projection_440x180_qualifying.png`.

State groups: Sweden `{38, 124, 138, 139, 140, 141, 666, 913, 915, 916, 917, 918, 919}`; Denmark `{37, 99, 911, 912}`; Finland `{111, 145, 148, 149, 150, 926, 927, 928, 929, 930}`; Estonia `{13, 191, 811, 812, 813}`; Latvia `{12, 190, 808, 809, 810}`; Lithuania `{11, 189, 814, 815}`.

The package contains 41 states and 82 unresolved/qualifying assets under `docs/formables/state_puzzles/form_baltic_sea_empire_category/{source,processed}/` and `gfx/interface/formables/state_puzzles/form_baltic_sea_empire_category/states/`.

### Baltic Federation

Source of truth: `docs/formables/state_puzzles/form_baltic_federation_category/manifest.json`.

Geometry and review files: `docs/formables/state_puzzles/form_baltic_federation_category/form_baltic_federation_category_geometry_artifact.json`, `form_baltic_federation_category_contact_sheet.png`, `form_baltic_federation_category_projection_440x180.png`, and `form_baltic_federation_category_projection_440x180_qualifying.png`.

State groups: Estonia `{13, 191, 811, 812, 813}`; Latvia `{12, 190, 808, 809, 810}`; Lithuania `{11, 189, 814, 815}`.

The package contains 14 states and 28 unresolved/qualifying assets under `docs/formables/state_puzzles/form_baltic_federation_category/{source,processed}/` and `gfx/interface/formables/state_puzzles/form_baltic_federation_category/states/`.

### Sweden-Hungary

Source of truth: `docs/formables/state_puzzles/form_sweden_hungary_category/manifest.json`.

Geometry and review files: `docs/formables/state_puzzles/form_sweden_hungary_category/form_sweden_hungary_category_geometry_artifact.json`, `form_sweden_hungary_category_contact_sheet.png`, `form_sweden_hungary_category_projection_440x180.png`, and `form_sweden_hungary_category_projection_440x180_qualifying.png`.

State groups: Hungary `{155, 974, 43, 973, 154}`; Sweden `{138, 139, 140, 915, 124, 913, 919, 141, 916, 38, 917, 918, 666}`.

The package contains 18 states and 36 unresolved/qualifying assets under `docs/formables/state_puzzles/form_sweden_hungary_category/{source,processed}/` and `gfx/interface/formables/state_puzzles/form_sweden_hungary_category/states/`.

## DDS conversion and validation

All 260 missing runtime files were converted from the reviewed processed PNGs with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, using each manifest bounding box width and height exactly.

Every output is present at its manifest `dds` path, has a `DDS ` magic/header with a 124-byte header, one mip level, 32-bit BGRA masks, exact bbox dimensions, and the expected uncompressed `width * height * 4` payload.

Every DDS payload has real alpha transparency with both zero and opaque alpha samples.

All 260 DDS files decode back to the exact RGBA bytes of their reviewed processed PNG, with 260/260 exact round-trips and no dimension, header, alpha, or pixel mismatches.

The manifest `png_sha256`, geometry artifact SHA-256, map revision, map SHA-256, projections, state ordering, sprite names, and runtime paths were not changed.

## Runtime helper audit

The live helper file `common/scripted_triggers/chaosx_formable_state_puzzle_triggers.txt` contains all 130 required state wrappers and the five formable territory wrappers used by the generated adapter: `chaosx_formable_form_scandinavia_territory_qualifies`, `chaosx_formable_form_north_sea_empire_territory_qualifies`, `chaosx_formable_form_baltic_sea_empire_territory_qualifies`, `chaosx_formable_form_baltic_federation_territory_qualifies`, and `chaosx_formable_proclaim_sweden_hungary_territory_qualifies`.

The adapter emulation passed for all five legacy manifests: every ordered state has an unresolved/qualifying pair, a two-coordinate canvas position, two sprite names, and two existing runtime DDS paths.

## Blocker and scope boundary

Running `.tools/generate_formable_state_puzzle_runtime.mjs` from the repository remains blocked by its unchanged global `selectedCategories` set because seven west/south categories do not yet have manifests: `form_gran_colombia_category`, `form_commonwealth_category`, `form_united_netherlands_category`, `form_mutapa_category`, `greater_italy_category`, `latin_africa_category`, and `maghreb_formable_category`.

That generator blocker is outside this northern package and was left unchanged for the separate west/south package owner.

No gameplay, GUI, GFX registry, localisation, or manifest geometry was edited.
