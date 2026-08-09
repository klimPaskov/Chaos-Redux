# Universal state-registry consumer workflow

Use this workflow when a formable or event-owned state puzzle is built from the installed map. The universal registry owns map geometry; a consumer owns only its finite candidate set, projection, live helper policy, and output locations.

This file is template guidance, not a runtime file. It does not replace the owning decision, event, scripted-GUI, asset, or in-game validation work.

## Source and build surfaces

The canonical active-map geometry source is `docs/formables/state_registry/generated/state_geometry_registry.json`. It contains the installed map revision, provinces and definition hashes, state-history bundle provenance, map dimensions and wrap metadata, state IDs, province membership, exact absolute row runs, geometry hashes, and state-history hashes.

The source registry is immutable build input for consumers. Do not hand-edit it, copy its state geometry into a second owner manifest, stretch an old mask, or redraw a state in an asset editor.

The registry builder is `.tools/build_formable_state_registry.py`. It validates the source against the active map roots, checks provenance and state-ID coverage, and writes the portable registry index plus generated universal live-trigger wrappers.

The consumer contract is `docs/formables/state_registry/consumer_spec.schema.json` and `docs/formables/state_registry/consumer_spec.template.json`. The schema defines the finite candidate `state_ids`, optional `state_groups`, projection, qualification and visibility policies, helper overrides, and owner output paths.

The consumer compiler is `.tools/build_formable_state_puzzle_consumer.py`. It reads the canonical registry and consumer spec, projects exact row runs, writes unresolved and qualifying PNG/DDS pairs and previews, records the geometry artifact, and emits a runtime-compatible manifest with per-state helper hooks. A full conversion emits `status: "complete"`; `--no-dds` deliberately emits `status: "assets_pending"` so runtime discovery cannot ingest missing DDS paths.

The runtime generator is `.tools/generate_formable_state_puzzle_runtime.mjs`. It discovers every `manifest.json` directly below `docs/formables/state_puzzles/*/` whose `status` is `complete`, validates each manifest and runtime DDS pair, rejects duplicate category or formable identifiers after runtime normalisation (including `a-b` versus `a_b`), and emits the shared GFX, GUI, scripted-GUI, scripted-localisation, and localisation surfaces. It has no hardcoded category allow-list.

Runtime textures are converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. Preserve the processed PNG, final DDS, dimensions, hashes, and decoded round-trip evidence with the owning consumer package.

## Required build order

### 1. Resolve the active map and provenance

Treat the base HOI4 installation followed by ordered mod overlays as the active map roots. Pass the roots explicitly in load order; the builder selects the last existing `map/provinces.bmp` and `map/definition.csv`, while numeric state-history files are merged with later roots overriding earlier roots.

Use `--replace-state-history` when the last mod root replaces the complete `history/states` tree. Do not infer the launcher stack, search arbitrary roots, or silently merge an incomplete replacement.

Run a provenance check before producing consumer assets:

```powershell
python .tools/build_formable_state_registry.py `
  --game-root "C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV" `
  --mod-root "C:\path\to\overlay_a" `
  --mod-root "C:\path\to\overlay_b" `
  --check
```

The builder must fail closed on a provinces or definition hash mismatch, state-history hash or bundle mismatch, state-ID set or count mismatch, state-history declarations that reference a province missing from either `definition.csv` or `provinces.bmp`, map dimension or horizontal-wrap mismatch, invalid row runs, or a canonical registry-content hash mismatch. State-history parsing strips Clausewitz comments safely and accepts either conventional `<id>-<name>.txt`/`<id>.txt` names or arbitrary filenames with one declared numeric `id`; duplicate or ambiguous IDs fail closed. `--skip-provenance` is source-only lint and is never distribution evidence.

If a map-changing mod adds, removes, splits, renumbers, or replaces states, regenerate the geometry source against the same ordered combined roots before rebuilding the index, triggers, consumers, and assets. Never ship a registry or consumer compiled from one map revision with another map's bitmap, definition file, or state history.

### 2. Declare a bounded consumer

Copy `consumer_spec.template.json`, validate it against `consumer_spec.schema.json`, and replace every example value. Set `status` to `draft` while designing and to `complete` only after the spec, assets, and evidence are ready for runtime discovery.

`state_ids` is a finite build-time candidate set. Use a candidate superset when an event, route, or branch can make different predeclared states relevant later, and mark optional entries with `required: false` plus an explicit live `visibility_helper`. Required entries remain visible; optional entries are shown only while the helper says they are relevant.

Every candidate still needs a qualification helper. Use a generated universal helper such as `chaosx_state_registry_state_<STATE_ID>_controlled_by_root`, an owner helper, or an explicit policy override that resolves to a real script token. Explicit qualification, visibility, and territory helpers must match `^[A-Za-z_][A-Za-z0-9_]*$`; category/formable IDs may contain separators for compatibility but must normalise to a non-empty runtime token. `visibility_helper` changes presentation only; it never grants formation eligibility.

Keep `state_groups` as subsets of `state_ids` and record alternate-group meaning in the owning decision design. Supply `territory_helper` only when an owner helper already composes the same live state rules; otherwise let the compiler emit its bounded aggregate helper.

The consumer may choose projection canvas, padding, scale, and output paths, but it may not invent map geometry, state IDs, runtime sprite names, or GUI node positions outside the declared finite set.

### 3. Compile exact geometry and status assets

Run the compiler from the mod root after the registry provenance check:

```powershell
python .tools/build_formable_state_puzzle_consumer.py `
  --spec "docs\formables\state_registry\consumer_spec.json"
```

Use `--dry-run` to validate the spec and projection without writing files. Use `--no-dds` only for a deliberately staged asset pass; it writes `status: "assets_pending"`, which the runtime generator skips. A consumer cannot be promoted until every runtime DDS exists and has round-trip evidence. Non-dry builds require spec `status: "complete"`.

The compiler validates the registry content hash and every candidate ID, computes one union-based projection frame with explicit horizontal-wrap handling, and writes one unresolved and one qualifying asset per candidate. It also records `qualification_helper`, optional `visibility_helper`, `canvas_position`, `runtime_dds`, `runtime_png`, and the registry hash in the manifest.

There is no runtime fallback for an unknown candidate. If a future event needs a state not in the compiled superset, add the state to the consumer spec and rebuild the consumer and runtime outputs.

### 4. Generate and inspect runtime surfaces

Run the runtime generator only after complete manifests and runtime DDS files are present:

```powershell
node .tools/generate_formable_state_puzzle_runtime.mjs
```

The generator skips manifests explicitly marked `draft`, `assets_pending`, or another non-complete status, fails when the root is missing or no complete manifest exists, and fails on duplicate normalised category/formable IDs, invalid scripted-helper identifiers, unsafe runtime paths, or missing runtime data. Do not restore a selected-category allow-list or hand-add generated GUI nodes.

The generated state entries are informational icons. The GUI has no state-changing click action, no fake button, and no AI-only path. The ordinary formation decision remains the only action.

## Runtime contract

State qualification, ownership, control, core policy, subject exceptions, and optional relevance are evaluated live from scripted triggers. The state piece, hover, summary, formation decision `available` trigger, and AI-facing decision logic must resolve to the same qualification policy and territory helper.

Do not cache state qualification, owner/controller names, or formation readiness. Do not add `on_daily`, `on_weekly`, `on_monthly`, a whole-world `any_country` scan, or another periodic iterator to refresh the display. A presentation-only dirty variable is acceptable only when a verified engine contract requires it and every scoped state-changing caller updates it; it must never replace the live formation trigger.

HOI4 cannot create a new texture, state-piece sprite, or positioned scripted-GUI node during play. An event can change live relevance or control for a predeclared candidate, but it cannot introduce an arbitrary runtime state ID, texture, or GUI node. Regeneration is the only supported path for a new candidate.

## Mandatory evidence gates

### Map MCP evidence

Use the installed read-only HOI4 MCP map routes before promoting a consumer:

- `mcp__hoi4_agent_tools__hoi4_map_inspect` with the candidate `stateIds` and bounded `provinceIds` to verify state membership and exact geometry provenance.
- `mcp__hoi4_agent_tools__hoi4_map_render` with the relevant `state` or `province` layer and review overlays to confirm the source map and projection context.

Record the returned artifact URIs, source revision, and any diagnostics in the owner handoff. If either route is unavailable, record the exact blocker and do not treat source-only review as map-engine evidence.

### GUI MCP evidence

After the runtime generator emits the consumer window, use the installed read-only HOI4 MCP GUI routes:

- `mcp__hoi4_agent_tools__hoi4_gui_inspect` for the linked decision category, window hierarchy, icon bounds, tooltip regions, scripted-GUI properties, and generated sprite references.
- `mcp__hoi4_agent_tools__hoi4_gui_render` for every supported resolution and the normal, hover, unresolved, qualifying, optional-hidden, long-text, and missing-localisation states relevant to the consumer.

Record the returned artifact URIs and review that every piece stays inside the intended category description width, keeps its real relative position, has a tight hover region, and remains informational. If a GUI route is unavailable, record the exact blocker and do not substitute source inspection for the required visual evidence.

### DDS round-trip evidence

Convert each processed PNG with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` using the exact target dimensions and the repository's one-level uncompressed 32-bit BGRA contract. Decode every final DDS back to PNG at native size and compare it to the processed PNG pixel-for-pixel.

Retain a machine-readable or tabular record of source and DDS paths, dimensions, SHA-256 values, DDS header and byte-length checks, alpha extrema, and decoded round-trip equality. A missing, dimension-mismatched, header-invalid, or pixel-different DDS blocks `status: "complete"` promotion.

There is no dedicated DDS MCP route in the installed HOI4 tool surface; the repository converter and local decode/round-trip evidence are the required asset checks. Do not claim that a map or GUI MCP artifact proves DDS integrity.

## Handoff minimum

The owner handoff should list the consumer spec and schema, registry content hash and map roots, builder `--check` result, compiler result and manifest path, candidate and optional visibility policy, generated runtime outputs, map and GUI MCP artifact URIs, DDS round-trip evidence, and any skipped or blocked checks.

Report every simplification explicitly. In particular, report a deferred candidate, a missing DDS, a failed provenance check, an unavailable MCP route, an unresolved engine scope, or a staged `--no-dds` build as incomplete rather than silently falling back to hand-authored geometry or cached state data.
