# Universal state registry architecture handoff

## Scope and ownership

This handoff covers the reusable build-time registry, active-map producer, live trigger contract, and consumer compiler for future formable or event-owned state displays. The geometry source remains owned by the geometry worker at [state_geometry_registry.json](../../formables/state_registry/generated/state_geometry_registry.json); this pass did not edit that generated file, review previews, or runtime DDS beneath the generated geometry ownership boundary. The existing 21-puzzle runtime generator remains the owner of shared generated GUI/GFX/localisation output.

The architecture is intentionally finite at build time and live at runtime. A consumer names a fixed candidate set of numeric state IDs and receives deterministic geometry assets. HOI4 cannot discover a new state ID, rebuild map geometry, or create a missing DDS at runtime, so another mod's map/state changes require rebuilding the geometry source, consumer assets, manifests, and runtime output against the active combined map.

## Files and contracts

The tracked active-map producer is `.tools/generate_formable_state_geometry_registry.py`. It resolves `--game-root` plus ordered `--mod-root` overlays, chooses the highest-precedence `map/provinces.bmp` and `map/definition.csv`, merges state history by numeric ID, rejects duplicate IDs within one root, and treats the final mod root as a complete history replacement when `--replace-state-history` is supplied. It parses state history and definition rows, maps province RGB values to state IDs, emits canonical nested `[y,[x_start,length,...]]` row runs, and computes the accepted per-state geometry/history/content hashes. `--check` compares deterministic core geometry/provenance while ignoring reviewed MCP-only metadata; repeatable `--mcp-artifact`, `--mcp-revision`, `--mcp-post-qa-revision`, and notes arguments preserve evidence when a source is rebuilt.

`.tools/build_formable_state_registry.py` consumes the geometry source read-only and writes `docs/formables/state_registry/state_registry_index.json` plus `common/scripted_triggers/chaosx_universal_state_registry_triggers.txt`. The index is deliberately lightweight: it contains provenance, counts, exact bbox/interval metadata, geometry hashes, policies, and helper names, but not the canonical row-run payload. Consumers read row runs from the content-hash-validated geometry source. The builder derives the default expected state count from `counts.state_count`; `--expected-state-count` is an explicit override, not a vanilla 1081 hardcode. Active state-file hashes are checked by numeric state ID, so an overlay may rename a file without weakening provenance checks.

The geometry schema and fixture are [state_registry.schema.json](../../formables/state_registry/state_registry.schema.json) and [state_registry.template.json](../../formables/state_registry/state_registry.template.json). The final source uses `registry_content_sha256_algorithm: "sha256-canonical-json-v1"`, `counts.state_id_range`, nonzero province/pixel/row/run counts, portable source-file/hash fields, nested row runs, and `circular_x_interval.start_x`, `length`, `end_x_unwrapped`, `wraps_x_seam`, and `unwrap_offset`. The inclusive invariant is `end_x_unwrapped = start_x + length - 1`. Builder validation applies the canonical seam transform `x_unwrapped = x if x >= start_x else x + world_width` and rejects out-of-interval runs, invalid ordering, bad counts, duplicate provinces, bad geometry hashes, and bad bboxes.

The live helper family contains one state wrapper for every registered state and five policy variants:

- `chaosx_state_registry_state_<id>_controlled_by_root`
- `chaosx_state_registry_state_<id>_owned_by_root`
- `chaosx_state_registry_state_<id>_owned_and_controlled_by_root`
- `chaosx_state_registry_state_<id>_controlled_by_root_or_subject`
- `chaosx_state_registry_state_<id>_owned_by_root_or_subject`

The subject variants use documented state-scope primitives (`is_controlled_by`/`is_owned_by` plus nested `controller`/`owner = { is_subject_of = ROOT }`). They do not use unsupported `controls_or_subject_of`, `owns_or_subject_of`, a state-scope `exists`, `any_country`, periodic on_actions, persistent caches, or event targets. The old ordinary formable primitive is a compatibility alias to `chaosx_state_registry_controlled_by_root`; the explicit ITA/HUN carrier-or-subject wrappers remain untouched. This preserves the existing Italy/Hungary subject-control policy while allowing ordinary wrappers to delegate to the universal live primitive.

## Consumer API

Future consumers use [consumer_spec.schema.json](../../formables/state_registry/consumer_spec.schema.json), [consumer_spec.template.json](../../formables/state_registry/consumer_spec.template.json), and `.tools/build_formable_state_puzzle_consumer.py`. A spec provides `category_id`, a unique `formable_id`, the registry path, a positive canvas and padding, a unique fixed `state_ids` list, optional subset `state_groups`, default qualification/visibility policies, and per-state overrides. The compiler refuses undeclared group IDs, unknown registry IDs, duplicate overrides, invalid RGBA channels, unresolved qualification helpers, and optional states lacking a visibility helper. Non-dry builds require `status: "complete"`.

Policy mapping is explicit and build-time:

- `controlled_by_root`, `owned_by_root`, `owned_and_controlled_by_root`, `controlled_by_root_or_subject`, and `owned_by_root_or_subject` resolve to the corresponding universal state helper.
- An explicit `qualification_helper` or `visibility_helper` wins over a policy and can point to a consumer-owned scripted trigger.
- Qualification always resolves to a named helper. Required candidates are always visible and always block the aggregate territory helper. Optional candidates are rendered/countable only while their visibility helper is true; while hidden, the aggregate helper does not block formation.
- If no `territory_helper` is supplied, the compiler writes `common/scripted_triggers/chaosx_state_registry_consumer_<category>.txt` with a bounded AND/OR contract and records its helper/path in the manifest. No world scan is introduced.

Projection uses one circular frame for the union of all candidate columns, selecting the column after the largest circular gap as `wrap_start`. Every row run is split at that global cut and shifted by at most one world width. The manifest records `wrap_start`, `wrap_length`, `wraps_x_seam`, and `world_width`; this prevents edge-adjacent candidates from being projected in incompatible per-state frames. The compiler emits deterministic unresolved/qualifying RGBA PNGs, copies their exact bytes into source/processed variants, invokes the repository HOI4 BGRA DDS converter, and records real PNG and DDS SHA-256 values. It also emits a geometry artifact, full projection previews, and a runtime-generator-compatible manifest.

The fixture deliberately declares required state 875 and optional unused candidate state 876. State 876 is not in the example group and uses the placeholder `example_state_registry_state_876_relevant`; a real event/formable owner must define that live helper before shipping the generated manifest.

## Runtime-generator migration

`.tools/generate_formable_state_puzzle_runtime.mjs` now discovers all complete manifests beneath `docs/formables/state_puzzles`, skips drafts, rejects duplicate decision-category/formable identifiers, accepts required-state subsets of candidate states, and honors per-state `qualification_helper` and optional `visibility_helper` hooks. Visibility hooks are emitted as `<element>_visible` scripted-GUI properties only for manifests that use them, preserving the current 21-manifest output shape. Optional manifests receive live relevant-count denominator localisation and visibility-aware qualifying counts; legacy manifests keep their existing static denominator and output. A manifest can use a compiler-generated territory helper or retain its existing category-specific helper.

## Helper map and lifecycle

| Helper or artifact | Scope/input | Output/side effect | Consumers |
| --- | --- | --- | --- |
| `chaosx_state_registry_state_<id>_*` | Country wrapper around fixed numeric state scope | Live owner/controller/subject result; no variables or flags | Formable decisions, events, scripted GUI/localisation, consumer manifests |
| `chaosx_formable_state_qualifies` | Legacy state wrapper | Delegates to universal controlled-by-root primitive | Existing ordinary formable wrappers |
| `chaosx_state_registry_consumer_<category>_territory_qualifies` | Country scope; generated fixed candidate list | Live AND/OR formation gate; hidden optional candidates do not block | New consumer manifest territory status and owner gameplay call site |
| Geometry producer | Explicit game/mod roots | JSON geometry/provenance source; no runtime files | Registry builder and consumer compiler |
| Consumer compiler | Consumer spec + validated geometry registry | PNG/DDS assets, manifest, geometry artifact, aggregate trigger | Runtime generator and parent-owned gameplay wiring |

No event target, persistent variable, flag, or cleanup hook is needed by the shared registry. A consumer that introduces its own temporary state must own and clear that state in its gameplay path; the universal triggers remain side-effect free.

## Validation evidence

The following checks were run against the current installation:

- `python .tools/generate_formable_state_geometry_registry.py --check` passed without writing the geometry-owned source.
- `python .tools/build_formable_state_registry.py --check` passed against the active vanilla map; a normal build emitted 1,081 state entries, 1,081 controlled wrappers, and the lightweight index.
- `jsonschema` validation passed for the generated geometry registry and both schema templates.
- A synthetic seam fixture passed builder interval validation and consumer union-frame assertions for width 8, occupied columns at both edges, `wrap_start=6`, `length=4`, `end=9`, and canonical split mapping.
- `python .tools/build_formable_state_puzzle_consumer.py --spec docs/formables/state_registry/consumer_spec.template.json --dry-run` passed with candidates 875 and 876, one required and one optional visibility hook.
- A temporary complete-spec compile produced four PNGs and four DDS files (unresolved/qualifying pairs for states 875/876), real asset hashes, and an aggregate territory trigger. The temporary manifest was fed to the runtime generator, which discovered 22 complete manifests and 394 state pieces; temporary files were removed and the generator was rerun to restore the existing 21-manifest/392-piece output.
- `node --check .tools/generate_formable_state_puzzle_runtime.mjs` passed. OneDrive synchronization intermittently returned Windows `UNKNOWN` write errors during repeated generated-file writes; retrying after the sync lock cleared restored the expected output.

The required HOI4 MCP map evidence remains the geometry worker's reviewed artifact set in [universal_state_registry_geometry_handoff.md](universal_state_registry_geometry_handoff.md). This architecture pass did not rewrite a shared GUI, map, focus, event, decision, or probability surface, so no additional MCP GUI/map rewrite or probability compare was applicable.

## Migration and follow-up

1. Keep existing 21 manifests and ITA/HUN wrappers as the compatibility baseline.
2. For a new formable/event, copy the consumer template, replace the unique IDs and helper hooks, regenerate the PNG/DDS/manifest, then run the runtime generator and the consumer's gameplay/UI MCP evidence pass.
3. If a combined map changes, rerun the geometry producer against the explicit load order, review provenance and map evidence, rebuild the index and consumers, and regenerate every dependent texture. Do not ship a registry built against a different map.
4. Parent gameplay owners must wire the generated territory helper into the actual decision/event path and define any explicit optional visibility helper; the compiler does not invent gameplay policy or AI behavior.

Known limitation: arbitrary state IDs cannot be discovered or geographically projected in a live game without a prebuilt candidate registry and assets. The runtime helper contract is intentionally exact-state and live-owner/controller based; broad dynamic country scans remain out of scope.
