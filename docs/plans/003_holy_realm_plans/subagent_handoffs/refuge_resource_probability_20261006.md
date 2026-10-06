# Event003 refuge-resource AI comparison

Status: baseline inspect and the single required after-compare were attempted; both are unresolved because the MCP transport closed.

This is a read-only audit handoff; I did not edit gameplay source, change an AI weight, run tests, stage, or commit.

## Baseline source and MCP attempt

The frozen baseline is `docs/plans/003_holy_realm_plans/source_snapshots/unfunded_manpower_20261006/003_holy_realm_decisions.txt.before`, SHA-256 `95CB8C92154516359F5320FCAAC24F7F19D25BF00F60DC6FA64297A981707926`.

Before the owner patch, `common/decisions/003_holy_realm_decisions.txt` had the same byte length and SHA-256 as the frozen baseline.

I made the single required `hoi4.probability_inspect` attempt with adapter `decision_ai_will_do`, source `{ path: "common/decisions/003_holy_realm_decisions.txt" }`, and `refresh = false`.

The call returned immediately with `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect; Caused by: Transport closed`.

It returned no source revision, candidate inventory, required-input schema, diagnostics, artifact URI, or analysis ID, and I made no retry.

## After-compare attempt

The parent supplied and I verified the frozen post-patch source `common/decisions/003_holy_realm_decisions.txt`, SHA-256 `AAE8875AA894F9A865B067E3443B5FFD005E18561609C51A71529AFC60381703`.

I made exactly one `hoi4.probability_compare` attempt with adapter `decision_ai_will_do`, `before.path` set to the frozen `.before` file above, `after.path` set to the current decision file, `candidatePool` set to the five authorized decision IDs, `refresh = false`, and outputs `json`, `comparison`, `ranking`, and `unresolved`.

The compare returned immediately with `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: Transport closed`.

It returned no comparison ID, source revisions, scenario hashes, score or eligibility delta, diagnostics, artifacts, or rendered evidence; I made no retry.

## Declared comparison scenarios

The parent supplied the following named scenarios for the one required same-scenario comparison; neither has an MCP scenario hash because the compare did not return.

| Scenario ID | Declared state | Result class before tool result |
| --- | --- | --- |
| `003_REFUGE_FIRST_USE` | Actor TIB, AI-controlled, date 1936-07-01, Spiritual Legitimacy 60, global chaos 400, normal-realm/Bodhisattva/teaching-network flags active, final doctrine not renounced, a teaching seat available, and all decision-cost resources ample | unresolved |
| `003_REFUGE_ROADS_ALREADY_OPENED` | Same TIB AI/date/core values, with `holy_realm_memory_open_refuge_roads` and the native already-used status for `THR_open_refuge_roads` true | unresolved |

The compare request used a `scenarios` array with the two exact IDs, top-level dates and TIB actors, state entries for Legitimacy 60, global chaos 400, PP 1000, `active_teaching_missions = 0`, and `is_ai = true`, plus the declared flags.

The second scenario added `holy_realm_memory_open_refuge_roads`; it did not use `candidateOverrides` or an invented native-used-decision field.

Because the MCP transport failed before returning validation, neither scenario payload was accepted or rejected by the adapter, and native once-used status remains unconfirmed in the tool schema.

I will not invent candidate overrides or engine fields to force the “already opened” state into an unverified schema.

The candidate-pool question is the five authorized decisions named by the owner: `THR_white_scarf_relief_caravans`, `THR_second_refuge_register`, `THR_open_refuge_roads`, `THR_bodhisattva_hold_teachings_for_refugees`, and `THR_bodhisattva_invite_foreign_pilgrims`.

The source-projected selection pool is incomplete until the analyzer confirms other available TIB decisions and any supported native used-decision state for the second scenario.

The preserved peacekeeping resource return is outside the five grant removals and remains an unchanged control candidate; its exact candidate ID and scenario eligibility were not reported by the failed inspect call.

## Source change contract from the parent

The parent authorized removal of the five flat manpower grants listed above and addition of `fire_only_once = yes` to `THR_open_refuge_roads`, which is intended as a one-time branch.

The parent states that AI weight values, decision IDs, costs, and availability gates are otherwise unchanged, and that the actual 120,000-manpower peacekeeping return must remain intact.

The current and frozen decision files each contain 113 `ai_will_do` blocks, and a raw comparison of those score lines has zero differences.

The confirmed source patch removes only the five named flat manpower grants and adds `fire_only_once = yes` to `THR_open_refuge_roads`; the preserved peacekeeping return is outside the five-action comparison pool.

## Result and remaining uncertainty

No numeric before/after decision scores, availability changes, ranks, conditional shares, or view-filter invariance results are available.

The five-action candidate list is intentionally bounded and does not establish the complete available TIB decision race; decision `ai_will_do` values are willingness scores, not click probabilities.

The parent’s optional proof that all 47 Mandala-tab actions remain visible to AI was not attempted.

No exact selection probability is claimed; `ai_will_do` evidence is a willingness score unless the analyzer proves a complete candidate race.
