# Event 032 command-power alias probability baseline

Date: 2026-09-05

Status: read-only prepatch baseline, partial native probability evidence, numeric threshold result unresolved.

Repository: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`

## Scope and source snapshot

The audited surface is `events/032_missile_crisis.txt`, event `chaosx.nr32.60`, options `chaosx.nr32.60.a` through `.g`, with focused attention on options `.b`, `.c`, `.d`, and `.e`.

The immutable prepatch copy is [`pre_patch_event32_cp16/032_missile_crisis.txt`](pre_patch_event32_cp16/032_missile_crisis.txt).

The source and snapshot SHA-256 at capture were `964423E2ED8A07B4D23B3EA463E01994AB58802FC2461698C8634454CDE2EAA2`.

The exact owner proposal is four token substitutions only: replace `has_command_power` with `command_power` at source lines 265, 271, 277, and 283; retain all strict `>` comparisons, cost constants, other eligibility gates, scopes, `ai_chance` bases, modifiers, and effects.

No gameplay source, runtime, save, or launch file was written by this audit, and no game was launched.

## Source surface and constants

The complete native candidate pool is `chaosx.nr32.60.a`, `.b`, `.c`, `.d`, `.e`, `.f`, and `.g`.

Options `.b`, `.c`, `.d`, and `.e` use command-power thresholds `15`, `8`, `15`, and `25` respectively, with `fuel > 250` on `.b`, `support_equipment > 40` on `.c`, and `manpower > 300` on `.d` and `.e`.

The source AI scores are `.b = 10`, `.c = 10`, `.d = 6` before modifiers, `.e = 3`, `.f = 3`, and `.g = 1`; the restraint and escalation factors are `2.00` when their source conditions are true.

The nine named scenarios are `E32_CP16_BELOW_LOW` (`command_power=7`), `E32_CP16_EQUAL_LOW` (`8`), `E32_CP16_ABOVE_LOW` (`9`), `E32_CP16_BELOW_STANDARD` (`14`), `E32_CP16_EQUAL_STANDARD` (`15`), `E32_CP16_ABOVE_STANDARD` (`16`), `E32_CP16_BELOW_HIGH` (`24`), `E32_CP16_EQUAL_HIGH` (`25`), and `E32_CP16_ABOVE_HIGH` (`26`).

Every scenario declared `is_ai=true`, command-power and alias mirrors, `fuel=1000`, `support_equipment=1000`, `manpower=1000`, incident site present, payload absent, reserve absent, and `has_war=false`; `.f` was explicitly overridden false because rogue launch target/reserve was absent.

## HOI4 MCP probability evidence

The mandatory first call was `hoi4.probability_inspect` with adapter `event_option_ai_chance`, source `{identifier: "chaosx.nr32.60", path: "events/032_missile_crisis.txt"}`, `refresh=true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`.

It returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=true`, seven candidates, zero available candidates without a scenario, nine required inputs, and zero unresolved inspect items.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e050c77b4b5b3ad8e2717dc58b4e232d60976023fef2dda7f956f24e352a4e0/daa366790f31b2e47a2c2d997f6104cf1a593240435138ccc0e2030cb8c73134/probability-inspect-595ffd5fcb81.json`.

Inspect source revision: `e00d68c8008b95240f2b73d7bd617222d06d5fb744924fc38e7a524e453e66e1`; MCP source hash: `595ffd5fcb819628488bf1594221e9e9fa7aa844ef3e4d90a4a3e107f57f4e43`.

The adapter is documented as proportional categorical selection over the complete local pool with exact normalized probability support only after all local eligibility is resolved; runtime selection uses the engine d100 path.

The nine-scenario `hoi4.probability_evaluate` call supplied the complete seven-option pool and requested `raw_value` plus `conditional_probability` with ranking, matrix, waterfall, and unresolved outputs.

It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-d1ad6c1b3f9c73ef1e823406`, 63 candidate rows, 14 unresolved items, and five diagnostics.

Evaluate artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dff761c7c49b98191d25323656c02c961b4772b9d94318aa6986ae01e4f87d54/4d9d59f857bcdf8b69108320025136e49c66f139a9db20705c5b8fc65e22fc02/probability-d1ad6c1b3f9c73ef1e823406.json`.

Evaluate source revision: `ecfc789b4c9b44162bae12501df0fa57a24bbf98709d272b340488e9b6a23692`; MCP source hash: `595ffd5fcb819628488bf1594221e9e9fa7aa844ef3e4d90a4a3e107f57f4e43`; scenario hash: `0cb8c7016d65ef88b090f947899ad5a0ee99ac1eda4f9219ad0adaf4b1c1a8b7`.

The evaluator resolved `.a` false for the AI actor, `.f` false through the declared override, `.g` true with raw score `1`, and source-local score traces `.b = 10`, `.c = 10` before its unresolved modifier, `.d = 12` after the `6 x 2.00` restraint factor, and `.e = 3` before its unresolved modifier.

The evaluator left `.b`, `.c`, `.d`, and `.e` eligibility unresolved in every threshold scenario, so every conditional probability is null and no normalized selection probability, rank reversal, dominance, or starvation claim is valid.

The exact native blockers are `TRIGGER_UNRESOLVED`: `has_command_power` cannot compare the declared scenario value; `has_fuel` and `has_manpower` cannot compare their declared numeric values; `has_variable` cannot compare the declared incident-site state; compound `has_equipment` is not declared by the scenario; and the payload helper cannot resolve its `has_variable` and `var:missiles_incident_site` scope chain.

The evaluator also emitted `EVENT_OPTION_FALLBACK_NOT_PROVEN`, `.a` never eligible across the supplied AI scenarios, `.f` never eligible because of the explicit absent-target override, and inactive verification/escalation modifiers in this fixture.

The required `hoi4.probability_sweep` ran on path `command_power` with the same nine scenarios and complete pool, using nine sweep points and rank-reversal detection.

It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-141c8882f73f96151a11310a`, nine sweep points, 14 unresolved items, and the same five diagnostics.

Sweep artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6715906d418ef6c02443343c40d635a9546c2151218cd1e2ce2b107907addcc5/8b44c1e59f0dc069ad8afa5d78390a34387078c9954becf23bd39c3f1836d742/probability-141c8882f73f96151a11310a.json`.

Sweep source revision: `10d4cb03dbddeee01652520e91e5b23f27430db9db4daa3745eeb958e0ccc508`; MCP source hash: `595ffd5fcb819628488bf1594221e9e9fa7aa844ef3e4d90a4a3e107f57f4e43`; sweep scenario hash: `fbbefcb88d3ab44ed1a87200304b8943e2dbdc1ad43d7db3cfcc9ef00d27b9da`.

Ranking, matrix, waterfall, threshold, sensitivity, and unresolved render URIs are retained in the evaluate and sweep MCP responses; the unresolved views are the appropriate rendered evidence for this partial result.

## Structural event evidence

A focused read-only `hoi4.event_inspect` lint for `{kind: event, eventId: chaosx.nr32.60}`, depth 1, 20 nodes, 40 edges, and no helper expansion returned `EVENT_INSPECTED_PARTIAL`.

Lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecde789a533b1c65bb85e62748f053432bf869bd49e5db906eef505b715bb52f/640f854e32b1e9c5ff6fa76de5258eced36b3800be6209484e92dd8c8f30c280/event-lint-1e7516fb0013.json`.

Structural revision: `1e7516fb00135d5559a8dfcc786dbeaeac9e3850d4f17dad626bbe811df96bc0`; graph hash: `7a39b49e488ea4f2b2e4549cb4640a598037d2bf0fb6587b1a9e3ea496a3c587`.

The matching `hoi4.event_render` options view returned `EVENT_RENDERED_PARTIAL` with layout hash `6f334c84477bf6d757e3a86d50ac5f0a6cd565af39e02079b760f090ef4e6fcd` and selected 15 nodes; workspace-wide helper and lifecycle projections were deferred by the service.

Options JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9c59aedf36fb471ee957991708936a74f951e2725547ae5a5b551b186c768f4/33eca02b01771cc55ca4210a8734337c9f4a7eaa787b4e1c5b1fc4e535d42ea4/event-options-1e7516fb0013.json`.

Options manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/415caed2c16a264c8a685ab2b8fda4dc7ff4ee1effdfce35e12cfde5c9122b72/925bce192d061d5deec85b1b1aa275e7c7691672fb8beb1e54c8c08d0881f354/event-options-1e7516fb0013-manifest.json`.

## Owner handoff

The parent may proceed with the four `has_command_power` to `command_power` parser corrections without waiting for a numeric probability acceptance result, because the proposed edit preserves costs, strict comparisons, other gates, scopes, weights, modifiers, and effects.

The probability conclusion remains `unresolved` for the current prepatch source because the native adapter cannot bind the unsupported alias or the related numeric and scoped predicates.

After the owner patch, rerun `hoi4.probability_inspect` first and then `hoi4.probability_evaluate`, `hoi4.probability_sweep`, and mandatory `hoi4.probability_compare` using these same nine scenario IDs, the complete a-g pool, and the declared external state fixture.

No postpatch compare ID exists in this baseline handoff.

## Skipped analyses and uncertainty

`hoi4.probability_compare` was not run because no owner-applied postpatch source was in scope during this read-only baseline.

No seeded simulation or probability sequence was run because this event-option race has no declared uncertain-input distribution or multi-step custom-pool cadence contract.

The native adapter does not prove the strict below/equal/above boundary until the alias and numeric/scoped input blockers are resolved; do not convert the raw score traces into click probabilities.
