# Event 006 probability MCP recovery

Date: 2026-09-02

## Scope

This handoff records fresh read-only probability evidence for the Event 006 automatic allocator. No weight, candidate gate, package admission, reservation, ladder, AI, or gameplay source was changed.

## Source inspection

The mandatory `hoi4_probability_inspect` call used adapter `random_list`, source path `common/scripted_effects/006_independence_wave_effects.txt`, `refresh = true`, and workspace `mod_chaos_redux_ea3b2d67c2c0`. It returned `PROBABILITY_SOURCE_INSPECTED` with source revision `ac9600f68d631d65c646387e9b2a828871a9e7f85eb70935983a6226c9780a55`, source hash `2f659348919ae968f83fddfaca503a69b47125db8ddcc7f3d1e11c49058e0f92`, `poolComplete = true`, 14 candidates, 14 required inputs, zero available candidates, zero unresolved inspection inputs, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9f982ee6657a34618ab463c5d29bf78b43848c31366bac1915d44c8b969e85c/87b9581dc774c6868a28b94e29c7de2eb9cb435d854396d3e37dbc7b81ffc28d/probability-inspect-2f659348919a.json`.

The zero available candidates are an empty/non-live fixture result. They do not prove that the runtime allocator has no eligible packages.

## Bounded evaluation

The follow-up `hoi4_probability_evaluate` call used the same adapter and source, `horizonDays = 1`, metrics `raw_value` and `conditional_probability`, outputs JSON, ranking, matrix, and unresolved, and scenario set `E006_ALLOCATOR_EMPTY_FIXTURE_2026_09_02` containing `CALM_EMPTY`, `GATHERING_EMPTY`, `RISING_EMPTY`, `TOTALEN_EMPTY`, and `WORLD_COLLAPSE_EMPTY`, each with an empty state object. It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis id `probability-a108fc2e08a2e11724e965c9`, source revision `ac9600f68d631d65c646387e9b2a828871a9e7f85eb70935983a6226c9780a55`, source hash `2f659348919ae968f83fddfaca503a69b47125db8ddcc7f3d1e11c49058e0f92`, scenario hash `1d10b939bb7f39265b3f44a81ff129c0eb56b1246727921351a6aa061032765f`, five scenarios, 70 rows, 14 unresolved values, zero diagnostics, and six visual resources.

The authoritative JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2db87ee9d24ee3ffacdb34b8cee8d7bcd55f6952d5542c9a1e67451b8acf936a/6479aefb6bcb77c698c828c47e2a4f8d86d85e56ed491e87629ae14583dc8a2b/probability-a108fc2e08a2e11724e965c9.json`. Ranking, matrix, and unresolved SVG/PNG artifacts are retained in the MCP result and share the same analysis id.

## Interpretation and limits

This is a successful discovery and bounded empty-fixture evaluation, not normalized campaign probability evidence. The empty fixture cannot establish package rankings, conditional selection probabilities, timing, starvation, dominance, rank reversal, or live AI behavior. A complete typed campaign fixture and the required `chaosx_ai_probability_auditor` route remain necessary before accepting any balance change. No `probability_compare` is applicable because this tranche made no weighted patch and has no immutable before/after source pair.
