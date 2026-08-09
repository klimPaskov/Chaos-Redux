# Universal state registry final audit

## Scope and disposition

This bounded audit covers the universal geometry producer and builder, consumer compiler, runtime manifest discovery, schemas and template guidance, generated universal triggers, the compatibility alias, the 21 current manifests/runtime surfaces, and the formable state-puzzle documentation.

The registry contract is internally consistent at 1,081 states with IDs 1 through 1,081, 95,499 row runs, canonical content hash `9777af66b45f2539296e2cc1efaf5b0a8d6146b087f31b2bc1a4c646cc0cc6c5`, a 1,081-entry lightweight index, five helper families covering every state, zero `any_country` or `any_subject_country` clauses, 21 discovered consumers, 392 state-piece entries, and 784 runtime DDS registrations.

No broad mechanic, decision, mission, or GUI redesign was introduced. The changes below are fail-closed validation and staged-asset corrections for future consumers.

## Findings and changes

### High: staged `--no-dds` manifests were runtime-complete

Before the patch, `build_formable_state_puzzle_consumer.py --no-dds` still serialized `status: "complete"` while omitting DDS hashes and files.

The compiler now emits `status: "assets_pending"` whenever DDS conversion is skipped and emits `status: "complete"` only for a full conversion.

The runtime generator already skips every explicit non-complete status, so staged manifests cannot be discovered until their DDS pass is complete.

### Medium: normalized category/formable collisions and empty tokens

Before the patch, runtime duplicate checks compared raw IDs even though generated filenames, GUI identifiers, and localisation keys use normalised IDs.

The runtime now rejects empty normalized IDs and detects collisions such as `a-b` versus `a_b` before generation.

The compiler now rejects category/formable values that normalize to an empty token and validates all generated script-token inputs.

### Medium: scripted-trigger helper identifiers were permissive

The consumer schema, compiler, and runtime now require explicit qualification, visibility, and territory helper names to match `^[A-Za-z_][A-Za-z0-9_]*$`.

Optional state entries still require a non-empty visibility helper, while required entries may carry the compiler's `null` visibility value.

Output paths are checked as workspace-relative paths by the compiler, and runtime DDS paths are checked for traversal or absolute-path escapes before existence checks.

### Medium: state-history parsing was not comment-safe or filename-flexible

The builder now strips Clausewitz comments while preserving quoted `#` characters before reading declared IDs, names, and province blocks.

State history discovery accepts conventional `<id>-<name>.txt` and `<id>.txt` names plus arbitrary filenames containing exactly one declared numeric `id`; filename/declaration mismatches, duplicate IDs, ambiguous declarations, and files without an ID fail closed.

The geometry producer uses the same comment-safe parser, so commented-out `id`, `name`, or `provinces` clauses cannot be selected accidentally.

### Medium: state-history province provenance could be overstated

The geometry producer now verifies every state-referenced province exists in both `definition.csv` and the active `provinces.bmp` before assignment and records the derived reconstruction result instead of relying only on a literal success flag.

The existing overlay and `--replace-state-history` contracts remain explicit and ordered; no world scan or runtime map discovery was added.

## Trigger, alias, and carrier-preservation audit

The generated universal trigger file contains exactly five live helper families for every registered state: controller, owner, owner-and-controller, controller-or-subject, and owner-or-subject.

The compatibility alias delegates to the universal controlled-by-root helper without adding a scan.

The Greater Italy and Sweden-Hungary wrappers preserve their explicit ITA/HUN carrier-specific checks and were not widened to generic ROOT-subject behavior.

The audit found zero `any_country` and zero `any_subject_country` clauses in the generated universal registry trigger surface.

## Decision and mission lifecycle notes

This package owns presentation helpers and manifest contracts, not a new decision or mission system.

Formation decisions remain the gameplay owners of route/reveal gates, costs, effects, AI availability, completion, and cleanup; no costs, timers, AI weights, or mission targets were changed here.

The GUI remains informational, `context_type = decision_category`, and AI remains on the ordinary decision path without opening or clicking the GUI.

Required state pieces are always present, optional pieces require live visibility/relevance helpers, qualification and readiness remain live, and the runtime cannot add an uncompiled state texture or positioned node during play.

There are no daily, weekly, monthly, cache, event-target, or world-scan refresh paths in this audit scope.

## Costs, requirements, AI, localisation, and exploit review

No passive political-power exchange, equipment/trains/convoys/manpower/XP cost, cooldown, war-goal, unit, core, or exploit loop is introduced by these registry changes.

Future consumers must keep the final formation `available` trigger and AI trigger on the same bounded territory helper; the compiler now rejects missing qualification hooks and malformed helper names before a consumer can be emitted.

Generated hover and summary surfaces continue to read current owner/controller/core/control state and preserve optional readiness/count semantics without stale cached values.

No new player-facing keys were added by this audit; schema and template guidance now document staged status, helper syntax, normalized collision rejection, provenance checks, and map-changing regeneration requirements.

## Validation evidence

- `python -m py_compile .tools/build_formable_state_registry.py .tools/generate_formable_state_geometry_registry.py .tools/build_formable_state_puzzle_consumer.py` passed.
- `node --check .tools/generate_formable_state_puzzle_runtime.mjs` passed.
- `python .tools/generate_formable_state_geometry_registry.py --check` passed against the active map source.
- `python .tools/build_formable_state_registry.py --check` passed with 1,081 active states.
- `python .tools/build_formable_state_puzzle_consumer.py --spec docs/formables/state_registry/consumer_spec.template.json --dry-run` passed for fixture IDs 875 and 876.
- `node .tools/generate_formable_state_puzzle_runtime.mjs` passed with `Generated 21 formable state puzzles with 392 state-piece entries.`
- A temporary compiler fixture confirmed that `--no-dds` writes `status: "assets_pending"` and that runtime discovery skips the staged manifest; the fixture directory was removed after the check.
- Existing asset evidence records 784 runtime sprites/DDS, the four-PNG/four-DDS round-trip fixture was cleaned, and the synthetic seam fixture remains width 8, start 6, length 4.

## MCP evidence and blockers

Fresh supplied map inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7572f229fdfa3f1d7c4d86b79086b7405952b528a3af0be803846b56ea6ba98/3cd97ea864823b31ac420ba1011270161be002fd5327eb419dd7dae9c4d0f2dc/map-inspect.9438c9fe43fbe756.json`.

Fresh supplied GUI inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/85703a7f43be2ce3ea6e0a4b159ad11b8d725e7f9e5e9a8222a5d675ea37ab5a/232195d6f5ef4859500dde7ef6077a8caa6df5d7b3aaf548b2cc24be062a28c5/gui-inspect.dae3dfc0491d53dd.json`.

Fresh supplied compact render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7d630f7e60a2edd288ffbf7ee39f91bb60b9a6a6af2b578840e928d08524ee6/6e37ee30036d2fe48e90d14255a2e77158a7c294e0e7a1666b8ecfb1f3c55abf/chaosx_formable_state_puzzle_form_mountainous_re-full.svg`.

Fresh supplied dense render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8aeb75a73d456b40b55c11d40ada9d776ed47b7516802d3606c859fca853d0b/8feb84a66bcb8860ead22dd266205ac6773e600b37fb2e7aa7c64dc4db1fea4f/chaosx_formable_state_puzzle_goe_form_hindustan_-full.svg`.

The supplied map evidence reports passing bitmap geometry, state/region membership, and network/adjacency checks while retaining unrelated workspace building-position and floating-harbor diagnostics.

The supplied GUI evidence resolves the compact window and requested elements, while global diagnostics remain affected by unrelated workspace-wide sprite collisions.

No live game launch was performed, in accordance with repository policy. No probability MCP pass was required because this audit changed no weighted AI, MTTH, random-selection, or decision-score surface.

## Changed files

- `.tools/build_formable_state_registry.py`
- `.tools/generate_formable_state_geometry_registry.py`
- `.tools/build_formable_state_puzzle_consumer.py`
- `.tools/generate_formable_state_puzzle_runtime.mjs`
- `docs/formables/state_registry/consumer_spec.schema.json`
- `docs/formables/state_registry/README.md`
- `.agents/skills/hoi4-decisions-missions/templates/formable_state_puzzle/README.md`
- `.agents/skills/hoi4-decisions-missions/templates/formable_state_puzzle/universal_state_registry_workflow.md`
- `.agents/skills/hoi4-decisions-missions/templates/formable_state_puzzle/validation_checklist.md`

No simplification was made to the universal trigger families, current manifests, wrap math, or ITA/HUN preservation. The only remaining blockers are the unrelated MCP global diagnostics and parent-owned live-game/DDS acceptance beyond this source audit.
