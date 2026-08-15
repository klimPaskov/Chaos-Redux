# Universal state registry

The universal state registry is the build-time contract for formable and event-owned state displays. It registers every state in the active Hearts of Iron IV map with a stable numeric id, portable geometry provenance, and live scripted-trigger keys. The source registry records its own state count and explicit `state_id_range`; the builder derives its default expectation from that source. A caller may pass `--expected-state-count` when deliberately checking a different reviewed map.

## Ownership and source of truth

The geometry worker owns `docs/formables/state_registry/generated/state_geometry_registry.json` and any review previews or state-piece textures below that generated subtree. This architecture does not edit those paths. The geometry source carries the active map revision, map-file hashes, state-history bundle hash, horizontal-wrap metadata, exact row runs, and per-state source hashes.

`.tools/build_formable_state_registry.py` consumes that source and writes two deterministic text outputs:

- `docs/formables/state_registry/state_registry_index.json` is a lightweight portable review/index projection with each state's provenance, counts, bbox/interval, geometry hash, and runtime helper names. It intentionally omits canonical `row_runs`; consumers read those only from the hash-validated geometry source.
- `common/scripted_triggers/chaosx_universal_state_registry_triggers.txt` is the runtime trigger contract generated from the same state id list.

The schema is [state_registry.schema.json](state_registry.schema.json). The small [state_registry.template.json](state_registry.template.json) is scaffolding for a new producer or test fixture; it is not a runtime asset.

`.tools/generate_formable_state_geometry_registry.py` is the tracked producer for map changes. It resolves `--game-root` plus ordered `--mod-root` overlays, parses the active `provinces.bmp`, `definition.csv`, and state-history files, rebuilds canonical row runs, and supports `--check` without writing. State-history parsing ignores Clausewitz comments, accepts conventional `<id>-<name>.txt`/`<id>.txt` names or arbitrary filenames with one declared numeric `id`, and fails duplicate or ambiguous IDs. Every referenced province must exist in both `definition.csv` and the active bitmap before state reconstruction is accepted. Pass `--replace-state-history` when the last overlay replaces the complete state-history tree. Review/MCP provenance can be reattached with repeatable `--mcp-artifact`, `--mcp-revision`, and post-QA arguments; the producer never invents runtime textures.

Future event or formable consumers use [consumer_spec.schema.json](consumer_spec.schema.json) and [consumer_spec.template.json](consumer_spec.template.json) with `.tools/build_formable_state_puzzle_consumer.py`. The compiler accepts a fixed `state_ids` candidate set (state groups must be subsets), computes one union-based circular projection frame, emits unresolved/qualifying PNG and HOI4 BGRA DDS pairs, writes per-state qualification/visibility hooks, and creates a live aggregate territory trigger when the spec does not supply one. Explicit qualification, visibility, and territory helper names must match `^[A-Za-z_][A-Za-z0-9_]*$`; category/formable IDs may contain separators but must normalise to non-empty runtime tokens. `--dry-run` validates a spec without files; full non-dry builds emit `status: "complete"`, while `--no-dds` emits `status: "assets_pending"` until DDS conversion and round-trip evidence are complete. Required candidates remain visible; optional candidates are shown only while their explicit relevance helper is true. The template deliberately includes required candidate state 875 plus an optional unused candidate 876 with the placeholder `example_state_registry_state_876_relevant`, exercising IDs outside the existing 21-puzzle set without pretending that helper exists in gameplay.

## Build command and active-map validation

Run the builder from the mod root after the geometry producer has completed:

```powershell
python .tools/build_formable_state_registry.py --game-root "C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV" --mod-root "C:\path\to\active\mod\overlay"
```

Repeat `--mod-root` in load order when several overlays contribute map or state history files. The last existing `map/provinces.bmp` and `map/definition.csv` wins. State history is merged by numeric state id, with later roots overriding earlier roots; duplicate ids inside one root fail closed. For a mod that declares `replace_path = "history/states"`, pass `--replace-state-history` so the mod history root is treated as a complete replacement. The build is intentionally explicit about load order; it does not inspect the user's launcher or infer a combined mod stack.

By default the builder derives the expected active state count from `counts.state_count` (and checks `counts.state_id_range` against the sorted source IDs). A reviewed alternate map can override this explicitly with `--expected-state-count <count>`. `--skip-provenance` is for a source-only lint and must not be used for distribution: normal builds compare provinces and definition hashes, active numeric state ids, state-history file hashes, the state-id digest, map width, and horizontal-wrap width against the source registry. A provided `registry_content_sha256` uses the exact `sha256-canonical-json-v1` rule recorded in the source. Any mismatch stops the build before output files are written.

Other mods can add, remove, split, or reorder states and can replace map geometry. HOI4 cannot discover new state ids or generate their GUI textures at runtime. Regenerate the geometry source, this index, every consumer manifest, and the state-piece assets against the active combined map before distribution. Never ship a registry built against one map with another map's state history or province bitmap.

## Runtime trigger contract

The generated trigger file provides one stable helper family per registered state:

| Helper suffix | Scope | Meaning |
| --- | --- | --- |
| `_controlled_by_root` | country/root entry | Current state controller is the prospective carrier `ROOT`. |
| `_owned_by_root` | country/root entry | Current state owner is `ROOT`. |
| `_owned_and_controlled_by_root` | country/root entry | Current owner and controller are `ROOT`. |
| `_controlled_by_root_or_subject` | country/root entry | Current state controller is `ROOT`, or the state controller country is a subject of `ROOT`. |
| `_owned_by_root_or_subject` | country/root entry | Current state owner is `ROOT`, or the state owner country is a subject of `ROOT`. |

The primitives are evaluated directly in the current state scope. They use the documented state-scope `is_controlled_by`, `is_owned_by`, `is_owned_and_controlled_by`, and nested `controller`/`owner` country scopes with `is_subject_of`; they do not rely on undocumented `controls_or_subject_of` or `owns_or_subject_of` names. There is no per-state `_exists` trigger: state IDs are build-time registry entries, and a consumer that names an unknown ID fails at build time. The helpers do not set variables, flags, event targets, or cached counters. A formable decision, event, tooltip, scripted localisation block, and state-puzzle piece should all call the same helper key for a state. The GUI is presentation only; AI takes the ordinary decision or event path and never depends on the GUI.

The default consumer policy is `controlled_by_root`. A consumer may declare `qualification_policy`, `visibility_policy`, or an explicit helper hook in its own manifest/index entry. Build-time compilation must resolve those declarations to named helpers; arbitrary state sets, state geometry, and helper names cannot be discovered dynamically by the game.

Greater Italy and Sweden-Hungary retain their existing carrier-specific subject-control rules. Their wrappers remain explicit ITA/HUN checks and are not silently widened to every `ROOT` subject policy. If a future consumer needs that policy, use the state-scope `_controlled_by_root_or_subject` helper or an explicit carrier-scoped helper; never add a repeated whole-world `any_country` scan.

## GUI and map highlighting use

The registry does not create a generic central GUI. A consumer declares the exact state ids it needs in its own manifest and the consumer compiler creates deterministic unresolved/qualifying visual pieces and a runtime-generator-compatible manifest. The runtime generator discovers every `status: "complete"` manifest under `docs/formables/state_puzzles`, skips drafts and staged `assets_pending` manifests, rejects duplicate category/formable identifiers after normalisation (including `a-b` versus `a_b`), validates scripted-helper identifiers and safe runtime DDS paths, honors per-state `qualification_helper` and optional `visibility_helper`, and preserves the existing 21-manifest outputs. For a decision category that only needs map highlighting, use the vanilla `highlight_states`/`highlight_state_targets` surface with the manifest ids. For a state puzzle, compile unresolved and qualifying visual variants from exact geometry and select the variant through the corresponding live helper. Horizontal world-wrap metadata (`geometry_encoding.map_wrap` with `horizontal: true` or `axis: "x"`, `world_width`, and each state's `circular_x_interval`) must be preserved when laying out a projection; do not collapse seam-crossing states into a near-worldwide bounding box. The canonical interval keys are `start_x`, `length`, `end_x_unwrapped`, `wraps_x_seam`, and `unwrap_offset`; the inclusive rule is `end_x_unwrapped = start_x + length - 1`, and every unwrapped row-run x must lie inside the interval.
Standalone manifest GUI and scripted-GUI output remains byte-stable; grouped windows and bindings are additive runtime surfaces.

### Shared scripted-GUI groups

A consumer may declare `group_id` and its family-specific `activation_helper` to project several independent formables through one decision-category window. Grouped specs require the activation helper; optional `group_scripted_gui_id` and `group_window_id` override deterministic identifiers derived from the normalized group id. Every member of a normalized group must agree on the raw group id and shared GUI/window identifiers, and the generator rejects collisions with another group or standalone consumer. The compiler emits these declarations into each manifest without special-casing any event or formable family.

The runtime generator emits one overlay window and one scripted-GUI binding per group, while retaining standalone windows and bindings for ungrouped manifests. Each family owns a summary and map container at the same origin, and its overlay visibility is driven only by that family's activation helper; state qualification, optional-candidate visibility, hover text, sprites, and summary status remain live. The scripted GUI is presentation-only (`visible = { is_ai = no }` and `ai_enabled = { always = no }`), so AI behavior continues through the decision category and its ordinary scripted triggers.

`summary_required_count` is an optional positive integer formation threshold independent of the visible candidate count. When omitted, the compiler derives it from required candidates; when supplied, the generator keeps the denominator at that threshold and clamps the qualifying numerator by emitting defined-text branches from the threshold down to one. A manifest may therefore honestly display `2 / 3` when only two researched candidate pieces exist, while `territory_helper` remains authoritative for final readiness.

Older manifests that predate this field retain their optional-candidate relevant-count denominator during regeneration; compiler-emitted manifests use the explicit threshold contract.

State names in hover text should use the engine's state scope (`[<state_id>.GetName]`) or the source `name_key`; ownership and controller text must be read live from the state scope. Do not cache a green piece after control is lost and do not add a daily/weekly/monthly whole-world refresh action. If a large GUI needs an engine-supported dirty variable, update it only from the consumer's bounded event/effect path and keep the trigger itself live.

## Validation and limitations

The builder validates source schema, unique positive ids, expected count, map hashes, state-history hashes, state-id coverage, row-run encoding metadata, map dimensions, horizontal-wrap width, and deterministic source content hash. It does not generate or inspect DDS files and does not replace the required map/GUI MCP evidence for a consumer. The geometry producer and parent integration owner remain responsible for exact row-run extraction, textures, consumer manifests, MCP map inspection, GUI rendering, and live in-game validation.

No on-action scan, persistent state cache, generic country scan, or dynamic assumption is part of this architecture. The registry is an immutable build artifact; only owner/controller/core qualification is live at runtime.
