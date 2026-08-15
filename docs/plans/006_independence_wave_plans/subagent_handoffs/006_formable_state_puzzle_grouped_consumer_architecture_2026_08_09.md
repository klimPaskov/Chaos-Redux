# Formable state-puzzle grouped-consumer compiler handoff

Date: 2026-08-09

Owner: `/root/formable_gui_group_architecture`

## Scope completed

The build-time consumer compiler and runtime generator now support generic grouped formable state-puzzle projections without event-specific identifiers or gameplay hardcoding.

The consumer schema and compiler accept `group_id`, required grouped `activation_helper`, optional `group_scripted_gui_id`, optional `group_window_id`, and optional positive `summary_required_count`.

Grouped declarations are copied into each v1 manifest so the generator remains the sole owner of runtime GUI and scripted-GUI output.

The compiler derives `summary_required_count` from required candidate states when omitted and allows an explicit threshold to exceed the candidate count for honest fail-closed summaries.

The runtime normalizer supplies the required-state default for legacy and older v1 manifests so existing complete manifests remain readable without regeneration.

## Runtime contract

The generator rejects duplicate normalized decision-category and formable identifiers as before.

It rejects duplicate or conflicting normalized group identifiers, group scripted-GUI identifiers, group window identifiers, and collisions between grouped and standalone runtime identifiers.

Every grouped family gets its own overlay container at the shared origin, with its summary and map children preserving the family projection, live hover, state qualification, optional visibility, and sprite selection.

One grouped `.gui` window and one grouped scripted-GUI binding are emitted per normalized group, while ungrouped manifests retain standalone windows and bindings.

Each grouped family overlay trigger uses that manifest's declared `activation_helper`, so overlapping projections are mutually presented by live helper state.

The grouped scripted-GUI binding is visible only to human players and only while at least one member activation helper is true, while each family overlay still has its own helper trigger.

Scripted GUI output is presentation-only with `visible = { is_ai = no }` and `ai_enabled = { always = no }`; decision and mission logic remains the gameplay owner.

Summary localization uses the manifest threshold as denominator and emits qualifying-count defined-text branches from that threshold down to one, clamping the displayed numerator without fabricating candidate states.

`territory_helper` remains the authoritative readiness trigger.

Manifests without an explicit `summary_required_count` retain the legacy optional-candidate relevant-count denominator and standalone runtime output remains byte-stable, including the original percentage-width root windows.

## Files changed

- `.tools/build_formable_state_puzzle_consumer.py`
- `.tools/generate_formable_state_puzzle_runtime.mjs`
- `docs/formables/state_registry/consumer_spec.schema.json`
- `docs/formables/state_registry/consumer_spec.template.json`
- `docs/formables/state_registry/README.md`

This subagent did not run the generator or edit generated runtime, interface, common scripted-GUI, gameplay, localization, or manifest files.

## Scripted-system boundary

No new scripted effect, scripted trigger, script constant, variable, event target, or cleanup hook is introduced by this generic compiler extension.

The caller-owned `activation_helper` is the only runtime input for group presentation, and its existing country or decision-category scope, side effects, and lifecycle remain unchanged.

The generator's grouped binding is read-only presentation logic with no AI effect or gameplay call site; decision categories continue to attach the generated binding separately.

The migration path is manifest-local: old v1 and reviewed-legacy shapes normalize to the prior standalone output, while compiler-emitted manifests carry explicit grouped metadata and summary thresholds.

## Validation performed

`node --check .tools/generate_formable_state_puzzle_runtime.mjs` and Python AST/JSON parsing are the appropriate source-only checks for this handoff.

The generator was intentionally not executed because generated runtime/gameplay files are parent-owned for this tranche.

An existing standalone baseline was inspected read-only with `hoi4.gui_inspect` for `chaosx_formable_state_puzzle_form_commonwealth_window` under scenario `decision_category_picture_and_attached_gui_current` in workspace `mod_chaos_redux_ea3b2d67c2c0`. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23fe9737ab12f0115b7da0ca05c2763c725979c562ebc4a443131ca555facd5f/1bfdcad58009fa136ebaf908c0fb820bfd7ca3cd30a351cb8f20ecf926a08e7b/gui-inspect.40594e291ff4f87d.json` with shared revision `40594e291ff4f87d93d4bee966634e917d66b6840eff6b65d8e9304609d6ccb0`.

That baseline inspection returned global index collisions, source-graph truncation, and visible-overlap diagnostics, so it is not evidence for the not-yet-generated grouped window. HOI4 MCP inspection/render comparison for each grouped window remains pending for the parent integration pass after generation.

After the parent generated the independence-wave manifests, a read-only `hoi4.gui_inspect` of `chaosx_independence_wave_formable_state_puzzle_window` under the same scenario returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35b295637de737be87f41f0b526398fc92fc62aa7edf69ff17db7c6ca0d3828c/bc616198d87f69f7f45bf78d22599cdf26d4f9f029b65744b42a405d084346f9/gui-inspect.a495a5be55135cf9.json` and shared revision `a495a5be55135cf9ad2447ee668d0156938b170b8d973788f16492d47b909d40`.

The grouped inspection reports global graph truncation/index collisions and 277 `GUI_VISIBLE_OVERLAP` diagnostics because the offline scenario cannot prove mutually exclusive activation-helper states; parent-owned scenario renders must exercise one activation helper at a time and retain the diagnostics as bounded evidence.

## Follow-up for parent

Run the runtime generator after the grouped manifests and activation helpers are wired, then inspect each emitted grouped window and scripted-GUI binding through the mandatory HOI4 MCP GUI route.

Confirm the decision-category call sites attach the grouped scripted-GUI id and that every family activation helper is true only for its intended projection.

Review generated localization in-game for the `summary_required_count` cases, including a candidate pool that displays `2 / 3` while the territory helper remains false.

No simplification or fallback was introduced in the compiler or generator.
