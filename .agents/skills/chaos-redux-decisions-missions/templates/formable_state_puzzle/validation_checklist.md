# Formable state-puzzle validation checklist

This checklist records evidence for a copied owner implementation. It does not claim that the skill-local package is loaded by the game.

## Universal registry and consumer gate

- [ ] For a registry-backed consumer, the only geometry source is `docs/formables/state_registry/generated/state_geometry_registry.json`; no owner file duplicates its row runs or masks.
- [ ] `consumer_spec.schema.json` validates the owner spec copied from `consumer_spec.template.json`, explicit helper ids match `^[A-Za-z_][A-Za-z0-9_]*$`, and `status: "complete"` is withheld until all asset and evidence gates pass; a `--no-dds` manifest remains `assets_pending`.
- [ ] `.tools/build_formable_state_registry.py --check` was run against the base game root plus ordered overlay roots, with `--replace-state-history` when the final overlay replaces the complete state-history tree.
- [ ] The builder passed with no provenance mismatch and fails closed when any map bitmap/definition hash, state-history hash or bundle, state-ID set/count, map dimension, horizontal-wrap, row-run, or canonical registry-content check differs.
- [ ] `.tools/build_formable_state_puzzle_consumer.py` compiled the finite candidate set from the canonical registry, and every candidate ID is present in the registry before output generation.
- [ ] Candidate supersets use `required: false` and an explicit live `visibility_helper` for optional relevance; no event can introduce a state ID outside the compiled set at runtime.
- [ ] `.tools/generate_formable_state_puzzle_runtime.mjs` discovers all `status: "complete"` manifests, rejects duplicate normalised category/formable IDs (including punctuation/underscore collisions), and emits no hand-authored or allow-listed state nodes.
- [ ] Geometry discovery accepts conventional or arbitrary state-history filenames only when one un-commented numeric `id` is unambiguous; every referenced province exists in both `definition.csv` and `provinces.bmp`.
- [ ] Qualification, ownership, control, core, and optional relevance are evaluated live from the shared helper family; no eligibility cache, stale owner/controller text, or whole-world refresh scan is used.
- [ ] A map-changing mod triggered regeneration of the registry, index/triggers, every affected consumer, every state-piece asset, and runtime generated surfaces against the same ordered combined roots.

## Manifest and installed geometry

- [ ] `state_manifest.example.json` validates against `state_manifest.schema.json` before any legacy example value is copied; migrated consumers use the universal consumer schema instead of a second geometry manifest.
- [ ] The owner manifest records the active installed `map/provinces.bmp`, `definition.csv`, and every state-history file with revision and SHA-256 values.
- [ ] Every state entry lists the exact state id, localisation key, province ids, row-run or mask checksum, source bounding box, transparent bounding box, projection, canvas position, and shared-border rule.
- [ ] The geometry extraction report is archived beside the owner implementation and its checksum matches the manifest.
- [ ] A map revision change causes every state mask and projected position to be rebuilt.

## Piece and sprite contract

- [ ] There is exactly one state-piece icon and one hover region for every manifest state.
- [ ] Neighbouring pieces use one origin, scale, projection, and border policy and do not leave a seam gap or double outline.
- [ ] The unresolved composite is grey, hatched, and outlined.
- [ ] The qualifying composite is green and carries a check or solid inner keyline.
- [ ] The GFX file contains only static sprite registrations and uses owner runtime asset paths after copying.
- [ ] No animation frame, movement, pulse, or transform-only effect appears in the piece, cue, border, or static alternative.

## Shared eligibility and refresh

- [ ] One state-scope helper owns the owner, controller, core, subject, ally, and occupation policy.
- [ ] Each generated state wrapper calls that helper instead of repeating its clauses.
- [ ] The live count uses descending `count_triggers` over every per-state wrapper, or a documented event-refreshed count calls the same helper once per manifest state and writes only owner-scoped count, required-count, and dirty variables.
- [ ] The summary status and formation decision availability call the same territory helper.
- [ ] Alternate-group rules are explicit in the manifest and composed by the territory helper.
- [ ] The formation decision evaluates the territory helper at availability time and cannot be bypassed by presentation state.
- [ ] When the optional variable path is used, refresh calls cover the decision open/visibility path and every already-scoped state-transfer, control, focus, or event effect that can change a required state.
- [ ] No whole-world daily, weekly, monthly, or other periodic iterator was added for the display.

## Hover, summary, and decision context

- [ ] The hover names the current state and resolves current owner, current controller, control result, core result, and qualification result.
- [ ] Owner and controller fallback text is shown when either scope is absent.
- [ ] The summary shows the current qualifying count, display denominator, and final readiness status without raw variable names.
- [ ] The scripted GUI uses `context_type = decision_category` and stays within the compact category description width.
- [ ] The state pieces are informational icons only and expose no dead click region or fake button.
- [ ] The static-category alternative gate is recorded and is false whenever the puzzle is needed.

## AI and lifecycle

- [ ] The AI uses the same formation decision trigger and territory helper without opening or clicking the human-facing GUI.
- [ ] The GUI has no action effects and no AI-only shortcut.
- [ ] When the optional variable path is used, completion, cancellation, route invalidation, and country identity changes call the owner cleanup effect.
- [ ] Optional cleanup clears only owner-owned count, required-count, dirty, and selected-state variables.
- [ ] Costs, route gates, alternate minima, control policy, and refresh tuning live in the owner manifest, script constants, or documented tuning file rather than call-site literals.

## Assets, localisation, and evidence

- [ ] Every GFX texture path resolves under the owner asset package and never points into the skill-local directory.
- [ ] The YAML localisation file is UTF-8 with BOM and contains category, summary, requirement, hover, owner/controller fallback, control, core, and status keys.
- [ ] `mcp__hoi4_agent_tools__hoi4_map_inspect` covers the consumer state IDs and bounded province IDs, and `mcp__hoi4_agent_tools__hoi4_map_render` supplies the relevant state/province layer artifact with source revision recorded.
- [ ] `mcp__hoi4_agent_tools__hoi4_gui_inspect` covers the linked category, hierarchy, click regions, hover regions, and sprite properties.
- [ ] `mcp__hoi4_agent_tools__hoi4_gui_render` covers every supported resolution and the relevant normal, hover, unresolved, qualifying, optional-hidden, long-text, and missing-localisation states.
- [ ] Every processed PNG was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, and every DDS was decoded back at native size with exact dimensions, BGRA header/byte-length, alpha, hash, and pixel-equality evidence.
- [ ] The same named scenarios are used to compare piece status, summary status, and formation decision availability.
- [ ] Any unavailable MCP route, unresolved engine dynamic-list scope, missing geometry artifact, DDS round-trip failure, or deferred in-game check is recorded with the exact reason.
