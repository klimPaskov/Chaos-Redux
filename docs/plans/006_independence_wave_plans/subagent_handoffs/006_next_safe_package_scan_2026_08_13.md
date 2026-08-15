# Repo Explorer Handoff

## Scope read

- Parent task: identify the next safe Event 006 package or shared gameplay tranche after the current IW-045 admission, using current authority `32/29/161/40`.
- Explicit constraints: this was a bounded, read-only scan; no gameplay files, central admission lists, Join effects, assets, portraits, flags, formables, localisation, or spreadsheets were changed.
- Files and IDs reviewed: all eight current adapter-only IDs (`IW-013 NAV`, `IW-015 GLC`, `IW-043 CHU`, `IW-058 ASY`, `IW-093 DOX`, `IW-098 SOK`, `IW-177 FIJ`, `IW-179 FSM`), current allocator/Join/dispatch sources, dormant package candidates, and admitted `IW-040 KUB` and `IW-044 TAT` gameplay surfaces.
- Skills and references read: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-improvement-loop`; the required offline `paradox_wiki/` pages; and the vanilla documentation files under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`.
- Engine evidence is read-only. The installed package has no Technology Tree Viewer, so no technology-tree claim is made.

## Primary findings

1. No unadmitted package clears the strict implementation gate. The current source-of-truth authority is the top override in `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`: `149` publishers, `32` content-attested selectable packages, `29` compatible reservation groups, `161` unattested selectable packages, and `40` runtime package adapters.
2. `IW-013 NAV` is the nearest adapter-only candidate but is not safe: the runtime anchor is compact state `792` (with optional `172/806`), while the installed `NAV.tga` ladder is Navarrese rather than an attested Basque-state carrier; `GFX_portrait_NAV_jose_antonio_aguirre` remains a source placeholder with provenance/rights review open; and `FORM-07` is a separate unresolved formable collision.
3. `IW-177 FIJ` is the runner-up but is not safe: the best current chair evidence is explicitly circa the 1940s, outside the 1936 baseline, while the period-valid alternative is anonymous or role-incompatible; `FORM-39` still requires an exact FIJ/PNG/WPG member package and MFX reservation review.
4. `IW-015 GLC`, `IW-043 CHU`, `IW-058 ASY`, `IW-093 DOX`, `IW-098 SOK`, and `IW-179 FSM` retain stronger identity, source-rights, flag, portrait, date, host, or formable blockers. Dormant rows such as `IW-036 BJX`, `IW-037 BKX`, `IW-039 DON`, `IW-073 CUX`, and `IW-182 GZX` lack a complete Event 006 adapter/package lifecycle and therefore cannot satisfy the no-design-decision gate.
5. The safest next tranche is not another package admission. It is an evidence-first AI/probability tranche for already admitted `IW-040 KUB` and `IW-044 TAT`, with no new identity, flag, portrait, formable, map, or host decisions.
6. A concrete TAT-only follow-up is visible but must remain conditional: `common/ai_strategy/006_independence_wave_tatarstan.txt` file-scoped values at lines 3-11 are `82/44/58/26/62/76/112/-250/-420`, while `common/script_constants/006_independence_wave_tatarstan_constants.txt` lines 81-89 contain the same values. This source mirror is internally aligned today, but any proposed alignment or tuning must wait for typed scenario baselines and a same-scenario probability comparison; `hoi4.probability_inspect` reports the strategy files as having no weighted surfaces, so no quantitative balance claim is supported yet.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Current allocator and admission authority. | Top `2026-08-14 IW-045 admission` override records `32/29/161/40` and the eight adapter-only IDs. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | Central adapter/content-attestation preflight. | Normal preflight requires both runtime adapter and content attestation; NAV/FIJ and the other adapter-only rows are not attested. |
| `common/scripted_effects/006_independence_wave_join_effects.txt` | Deterministic Join admission order. | `IW-044` and `IW-045` are admitted candidates; no unadmitted candidate was added during this scan. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_next_adapter_package_gate_audit_2026_08_13.md` | Comparative audit of all eight adapter-only packages. | NAV is nearest only conditionally; FIJ is the next research candidate, not an implementation-safe package. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_flag_admission_resolution_current_2026-08-12.md` | Current NAV/GLC flag and carrier decision evidence. | `SAFE_FLAG_ATTESTATION = NO`; NAV's Basque-versus-Navarre carrier mismatch is unresolved. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_nav_probability_audit_current_2026_08_13.md` | NAV weighted-surface evidence. | Six named scenarios produced unresolved candidate rows and no ranking/timing/balance claim. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw044_tatarstan_probability_audit_current_2026_08_13.md` | TAT probability baseline receipt. | Eleven mission candidates are discoverable, but empty fixtures leave candidates unavailable and no quantitative claim. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_current_iw040_probability_audit_2026_08_13.md` | KUB probability baseline receipt. | Eleven mission candidates are discoverable, but empty fixtures leave candidates unavailable and no quantitative claim. |
| `docs/plans/006_independence_wave_plans/006_admitted_package_ai_evidence_tranche_addendum_2026_08_13.md` | Existing plan for the safe shared tranche. | Defines typed scenario baselines, same-scenario compare, and the no-new-admission ownership boundary for KUB/TAT. |
| `common/decisions/006_independence_wave_kuban_decisions.txt` | KUB package decision missions and `ai_will_do` surfaces. | Fresh probability inspection found 11 available mission candidates and zero unresolved source rows; source hash `de8e919c4eae46c9abbb6fdb38703ccc0e59039dbd43c6eeeb120e3fe911a093`. |
| `common/decisions/006_independence_wave_tatarstan_decisions.txt` | TAT package decision missions and `ai_will_do` surfaces. | Fresh probability inspection found 11 available mission candidates and zero unresolved source rows; source hash `fc2e09b238bd9aaaa328fb2cc8b7c942869d7f4618c4b8d8e63f03de2a48aeb2`. |
| `common/ai_strategy/006_independence_wave_kuban.txt` | KUB package AI strategy layers. | Fresh `hoi4.probability_inspect` returned `discoveryReason=no_weighted_surfaces`; this is not a quantitative strategy balance surface. |
| `common/ai_strategy/006_independence_wave_tatarstan.txt` | TAT package AI strategy layers and file-scoped constants. | Fresh `hoi4.probability_inspect` returned `discoveryReason=no_weighted_surfaces`; any TAT tuning requires mission-scenario evidence first. |
| `common/script_constants/006_independence_wave_tatarstan_constants.txt` | TAT central AI tuning values. | Lines 75-90 define the nine `independence_wave_tatarstan_ai` values mirrored by the AI file. |
| `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt` and `common/scripted_effects/006_independence_wave_kuban_package_effects.txt` | Existing KUB package gating and effects. | These are package-specific, already admitted surfaces and are safe ownership boundaries for evidence-backed refinements. |
| `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt` and `common/scripted_effects/006_independence_wave_tatarstan_package_effects.txt` | Existing TAT package gating and effects. | These are package-specific, already admitted surfaces and are safe ownership boundaries for evidence-backed refinements. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_focus_layout_current_receipt_2026_08_14.md` | Current shared focus structural receipt. | `hoi4.focus_inspect` resolves 184 focuses and 196 connectors with zero crossings and zero node intersections; six authored layout findings remain, so no geometry tranche is recommended. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `script_collection_input.md`, and `script_collection_operator.md` | Vanilla syntax and collection/strategy evidence. | Read as required references for effects, triggers, constants, and typed probability fixtures. |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/default.txt` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/ARG.txt` | Vanilla AI strategy precedents. | These provide the existing `ai_strategy` block shape and parser-safe strategy value patterns; Chaos Redux package strategy layers should retain their current package gates. |

## Existing patterns

- Event 006 uses a two-gate package preflight: a runtime adapter alone is insufficient without a content-attestation branch. This is why an adapter-only row must remain fail-closed even when its country shell or map binding looks usable.
- KUB and TAT already own package-specific decision categories, project effects/triggers, AI strategy layers, portraits, flags, cleanup, and route integration. The safe tranche can therefore stay inside existing admitted ownership rather than inventing a country package or changing central dispatch.
- The current AI evidence plan separates a typed scenario baseline from any weight edit. It names `KUB_FRAGILE_PEACE`, `KUB_SEVERE_HOST_WAR`, `KUB_STABLE_ROUTE_LOCK`, `KUB_NETWORK_READY`, `TAT_FRAGILE_PEACE`, `TAT_SEVERE_HOST_WAR`, `TAT_STABLE_ROUTE_LOCK`, `TAT_NETWORK_READY`, `BOTH_RESOURCE_STARVED`, and `BOTH_IMPOSSIBLE_AMBITION`.
- The current probability workflow starts with `hoi4.probability_inspect`, then uses typed `probability_evaluate`; if a source change is made, the same scenario IDs and candidate pools must be used for `hoi4.probability_compare`. Empty fixtures and a strategy-source `no_weighted_surfaces` result are evidence gaps, not permission to tune by intuition.

## Vanilla or reference precedents

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/default.txt` and `ARG.txt` show the vanilla `ai_strategy` block structure and value-bearing strategy entries used as parser precedents.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` documents script constants and their scope limitations; `effects_documentation.md` and `triggers_documentation.md` document the effect/trigger forms used by the package gates.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_collection_input.md` and `script_collection_operator.md` are the relevant vanilla references for constructing typed scenario inputs and collection evaluation. They do not replace the installed HOI4 probability MCP route.
- The installed package has no Technology Tree Viewer. No technology-tree inspection or completion claim is possible from the current tools.

## Likely edit order for the parent

1. Keep all eight adapter-only IDs fail-closed and leave `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_join_effects.txt`, and the allocator registry unchanged.
2. Treat `IW-013 NAV` as a research blocker, not an implementation target, until the Basque/Navarre flag carrier, Aguirre source/rights, and `FORM-07` decisions are explicitly resolved; do not silently reuse a neutral or ideology-specific flag.
3. Start the admitted-package tranche with read-only typed fixture design for the ten named KUB/TAT scenarios and record whether the MCP accepts the required country flags, project ledgers, route-government flags, host status, resource floors, and mission availability.
4. Run `hoi4.probability_inspect` first on both decision files, then scenario-specific `probability_evaluate`; stop and document the exact unsupported fixture field if evaluation cannot be made typed and reproducible.
5. Only if a typed baseline exposes a reproducible ordering defect, make a narrow change in the existing KUB/TAT decision `ai_will_do` blocks or package AI files. Do not add a focus tree, country, formable, flag, portrait, event, GUI, map, or technology surface.
6. Run mandatory same-scenario `hoi4.probability_compare` with the pre-change source hashes and the post-change candidate pools, then update only the evidence tranche documentation and the relevant package docs.
7. Treat any TAT file/constant alignment proposal as a separate narrow patch after the baseline/compare, not as a basis for admitting another package.

## Validation checks

- Re-read the current authority override and verify that the allocator remains `32/29/161/40` and that the deterministic Join list contains no new candidate.
- Run `rg -n` parity checks for the eight adapter-only IDs across the adapter trigger, content-attestation trigger, and Join effects to prove that no accidental admission occurred.
- Verify that KUB and TAT decision source inspections still discover exactly 11 mission candidates each, with source hashes recorded in the receipts.
- Run `hoi4.probability_inspect` before every weighted-surface pass, then typed `probability_evaluate` for all ten named scenarios; use explicit range arguments for any sweep because an omitted range is rejected by the MCP.
- If source changes are made, run `hoi4.probability_compare` against the same scenario IDs and candidate pools and preserve both artifact URIs in the follow-up handoff.
- Reuse the current read-only `hoi4.focus_inspect`/render receipt and state-234/state-249 map receipts only as structural evidence; do not claim that unrelated focus diagnostics or partial event renders are fixed.
- Keep the absence of a Technology Tree Viewer explicit in the validation record.

## Risks and blockers

### Confirmed blockers

- No unadmitted package currently has the combined adapter, content-attestation, identity, flag, portrait, formable, and rights evidence required by the strict gate.
- NAV has a confirmed flag-carrier mismatch between Basque state 792 and the installed Navarrese ladder, plus unresolved Aguirre portrait provenance and `FORM-07` review.
- FIJ has a confirmed pre-1936 chair/date and role evidence blocker plus unresolved `FORM-39` package membership and MFX reservation review.
- KUB/TAT mission candidates are source-discoverable but current empty fixtures leave evaluation unavailable, so no ranking, timing, or balance claim is supported.
- KUB/TAT strategy files are reported by MCP as having no weighted surfaces; strategy values cannot be evaluated as a quantitative weighted pool through the current route.
- The shared focus receipt still records six authored layout findings and unrelated vanilla continuous-focus icon diagnostics; this is not a safe reason to widen the next tranche.
- The installed package has no Technology Tree Viewer.

### Ordinary risks

- Probability artifacts are source-hash sensitive; a later source edit invalidates the existing compare baseline.
- A transient MCP error occurred during one initial KUB inspection attempt; the retry succeeded and produced the source-discovery artifact recorded above.
- Live game/save-load validation remains outside this read-only scan and belongs to the parent/user workflow.

## Recommended next action

Fail closed on package selection: do not admit or implement another unadmitted Event 006 country package now. Start the queued, evidence-only KUB/TAT AI tranche with typed scenario fixtures and MCP probability baselines; if and only if those baselines support a reproducible defect, apply the smallest package-local AI/decision refinement and prove it with the same-scenario compare. The TAT file/constant values are a possible narrow follow-up, not an admission signal or a substitute for the required probability evidence.

No implementation, simplification, central admission, Join change, asset fallback, portrait fallback, flag fallback, formable promotion, or user design decision was made by this scan.

## MCP evidence artifacts

- KUB decision probability inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c471de5f641eec240acf6658fe64da7a96916b70513ce915c122664d87abf828/2f280a7f105fa1e330e5121145a6ff6c836a0dcd86a4d65564fc5025587e18f0/probability-inspect-de8e919c4eae.json`.
- TAT decision probability inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d53860054d6ad13d0f944e3dadb1564808fd4e63cf6165cb996d97b4a83686f7/3c089bc6d0dc7ae6787688c6d69479b7b11a4ac45264eb3d774ce6d5b031667f/probability-inspect-fc2e09b238bd.json`.
- KUB strategy inspection (`no_weighted_surfaces`): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/244390f89377720e42ea73330fb4cc8c473aa4f73d959053e526b99243dfacf4/e77545823f90471c0debbd8d40e328c5dabc7020895db0cc3461bf26ddb59323/probability-inspect-e4407e6b4829.json`.
- TAT strategy inspection (`no_weighted_surfaces`): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfcd7bb7df04abaa9f23e3bf79d768c5c763ba90a13fdf148704501d36df2cca/8794fb5d480fab2d6a792a4e70e0f3ff73c0cf3c763ae384a4fa4c8fd8510a0e/probability-inspect-213b76937d1b.json`.
- Current focus structural receipt: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42b84867f0b243741cb08d3e18b213be884167dafb7cf0b3ad235c8d11827adf/b0c567c6501a1e3b4157af83f86d878e2f97080645fb20fa607e0693ce335e7c/focus-inspect.1fbce5b0e266a11a.json`.
- TAT state-249 map inspection receipt: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7b4a207b98dc17e3509ead40dbcaea432324aacba36f30a683221e5e2c5d08a/6aefffdbfdbe43dc1b290b1cf4430c8f17be8b973e1706685e8e6f1e46644cd6/map-inspect.202f4d7d6e78751d.json`.

