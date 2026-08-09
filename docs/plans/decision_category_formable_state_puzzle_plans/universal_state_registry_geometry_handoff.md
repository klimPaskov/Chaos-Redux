# Universal state registry geometry handoff

## Deliverables

The deterministic registry is [state_geometry_registry.json](../../formables/state_registry/generated/state_geometry_registry.json).

The visual QA sheet is [state_geometry_registry_contact_sheet.png](../../formables/state_registry/generated/state_geometry_registry_contact_sheet.png).

The machine-readable QA report is [state_geometry_registry_qa.json](../../formables/state_registry/generated/state_geometry_registry_qa.json).

No runtime DDS, GFX, GUI, gameplay, localisation, category, or builder source files were edited by this geometry pass.

## Coverage and format

The registry contains exactly 1081 entries with contiguous state IDs 1 through 1081 and each entry uses its installed `name_key` (`STATE_<id>`), portable `history/states/<filename>` source path, source-file SHA-256, sorted province membership, pixel count, row count, run count, tight inclusive source-map bounding box, circular x interval, seam flags, geometry SHA-256, and absolute row runs.

The map source is 5632 by 2048 pixels with `map/provinces.bmp` SHA-256 `e131d30e5dcb13d9c2a8598f820a2de0ae9828f3a24f2bddc1bcfff40f71660a` and `map/definition.csv` SHA-256 `86846be71198d6772c651638aa22e3656133198de9b7c49c6234ed48cf33d87b`.

The registry contains 13,414 province definitions, 4,084,924 assigned state pixels, 7,449,412 intentionally unassigned sea/background pixels, and 95,499 row runs.

The canonical geometry encoding is `absolute_row_runs`, where each row is `[y, [x_start, length, x_start, length, ...]]`; y and x runs are ascending, x starts are inclusive, lengths are positive, and all coordinates remain absolute map coordinates.

Horizontal wrapping is explicit through `circular_x_interval.start_x`, `length`, `end_x_unwrapped`, `wraps_x_seam`, and `unwrap_offset` for every state.

The current installed map has no state occupying both x edges, so `crossing_state_ids` is empty and the contact sheet's wrap-axis panel uses nearest-seam state 875 as a non-crossing QA sample rather than inventing a wrapped state.

## Hash rules

Each `geometry_sha256` is SHA-256 of `json.dumps(row_runs, ensure_ascii=True, separators=(',', ':')).encode('utf-8')`.

The state-history bundle SHA-256 is computed from the ascending-ID UTF-8 lines `state_id|source_state_file|source_state_file_sha256\n`.

`registry_content_sha256` uses the stable identifier `sha256-canonical-json-v1` and is SHA-256 of the full registry object with only its own `registry_content_sha256` field omitted, serialized as `json.dumps(..., ensure_ascii=True, sort_keys=True, separators=(',', ':')).encode('utf-8')`.

The current registry content SHA-256 is `9777af66b45f2539296e2cc1efaf5b0a8d6146b087f31b2bc1a4c646cc0cc6c5`.

The `geometry_encoding.map_wrap` object explicitly carries `horizontal: true`, `axis: "x"`, and `world_width: 5632` for builder schema compatibility.

## MCP evidence

The initial full map inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc8be6f937fded287c4af9a647c000b6dc09aab304bddf9d85e24f703817d8c5/1a1fe0648c28cc1e0cd166c451d1f67fb5c61c90f52c3b074712a1c917f5cbac/map-inspect.5070618991ee5bd9.json` with revision `5070618991ee5bd9f3076ed92beecfc6a0788c12333e35fc0b648631e800002d`.

The selected-state MCP inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0fc8626f14ac5299b44354a6e13fb7c249a8e8377a2f0130a3000356ded636fc/70466c85ff43455a05e6383e4b5b1068b047401f69cdba380b340f04c22c0306/map-inspect.5070618991ee5bd9.json`.

The selected-state province row-run artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6241071e94799de2798d5b3e223c76826f93d18ce6a9b88974f4edc458c118c2/053655ab9ebe3b2ba51a47c11ba97e23af4dad3d1658d117d1a9da84602da38f/map-province-geometry.5070618991ee5bd9.803e184a5d5c5ec0.json`.

The representative post-generation MCP inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9596fb7854ea831c03f8de6ed06987138e4185ba1ad3576fe04ddf079c164164/35697c5dadde2d7d9bbf4162fda28f3e85ea418222d2b95143f4d7a502b4f226/map-inspect.7b89760624d46beb.json` with revision `7b89760624d46beb870ec35c3720df061bd5ca10615d8726d1fea80c7e33e4a1`.

The representative post-generation province row-run artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a348783098a7f51a6295dba82f18b735737c5e788ca38f16457138ee8096704/2f14e6fdab80d0a10580aab268059f017f4da17b18bc304ad7bad1e615dd04af/map-province-geometry.7b89760624d46beb.76e6d79886b836cc.json`.

The post-generation inspection reports identical source bitmap and definition hashes; the registry records both MCP revisions and all artifact URIs.

## Validation evidence

The QA report records passing checks for exact state ID coverage, nonzero reconstructed pixels for every state, state-history province membership reconstruction, row-run monotonicity and non-overlap, row-run containment in every circular interval, content-hash recomputation, and explicit horizontal-wrap handling.

The contact sheet covers tiny state 705 (`history/states/705-Sao Tome.txt`), island state 932 (`history/states/932-Isle of Man.txt`), large state 644 (`history/states/644-state 3.txt`), and nearest-seam wrap-axis state 875 (`history/states/875-Chukchi Peninsulay.txt`).

## Reusable producer contract

The tracked producer owned by the registry architect should read the same installed `provinces.bmp`, `definition.csv`, and `history/states/*.txt` sources, construct a province-to-state ownership map, emit canonical absolute row runs, compute circular intervals with inclusive `length = world_width - max_gap`, and apply the hash rules above.

The builder must treat `state_id_range` as descriptive metadata for this registry rather than assuming that other map mods are contiguous; future registries should preserve explicit state IDs from source files.

## Limitations

The MCP map validator reports pre-existing map position and port diagnostics in `map/buildings.txt`; bitmap geometry, definitions, state membership, adjacencies, and network checks passed.

The registry is geometry and provenance data only; runtime state-piece sprite generation, DDS conversion, GFX definitions, GUI wiring, and gameplay eligibility remain parent-owned.
