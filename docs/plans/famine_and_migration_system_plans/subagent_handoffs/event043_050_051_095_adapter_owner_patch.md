# Events 043, 050, 051, and 095 famine/migration adapter owner handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-25

## Verdict

No gameplay callsite is safe to patch in this bounded pass. The four accepted owner roots were inspected under their exact repository filenames, but none exposes the complete live state, actor, positive people-denominated amount, and causal receipt required by the public famine or migration contracts. No event, common scripted file, on-action, pool, pacing pulse, event-log entry, evolution, localisation, asset, achievement, or central famine/migration file was changed. The only file added by this pass is this handoff.

The initial descriptive names `043_anarchist_takeover`, `050_oil_crisis`, `051_weather_disaster`, and `095_balkan_federation` are not filenames in this repository. The accepted numeric owners confirmed by the parent census are `events/043_massive_flood.txt`, `events/050_the_great_embargo.txt`, `events/051_heat_wave.txt`, and `events/095_occupation_revolt.txt`.

## Binding separation seam

Famine and migration remain separate mechanics joined only by explicit owner receipts. Food-route, crop, import, reserve, substitution, and relief facts may call a famine pressure adapter. Exact movement, resettlement, deportation, reception, origin debit, route deaths, survivor credit, and destination facts may call a migration adapter. A vague crisis, event title, country selector, control transfer, or report effect may not activate both branches.

The famine seam requires a valid state plus a positive people amount, non-unknown source, and proven responsible actor before `famine_migration_request_famine_pressure`, `famine_migration_request_food_security_pressure`, or another source-specific pressure wrapper can be called. The 050 island-blockade lane additionally requires the full shared blockade proof, including island or isolation, maritime dependence, war, route or port disruption, convoy or escort shortage, no humanitarian corridor, and insufficient local food.

The migration seam requires a positive exact cohort amount, origin/current-host proof, route border/transport/safety/actor proof, an event target for the real destination, and destination food-safety/reception proof or the explicit forced-return proof before `famine_migration_transfer_civilians_exact` can be called. That primitive debits the origin once, records route deaths separately, credits only surviving people, and reconciles population/manpower ledgers. Movement is not Deaths and no caller may debit population directly or replay an already-owned death.

## Owner dispositions

### Event 043, `chaosx.nr43.1`

Source: `events/043_massive_flood.txt:22-60` and its report tooltip at `:64-106`.

The root iterates every coastal state and applies unit/building/infrastructure damage, then executes `add_manpower = -5000` at `:53`. The event does not prove an exact flood-affected state beyond the broad coastal predicate, a responsible actor, a positive civilian amount, a cohort, a route, a destination, destination reception, or survivor amount. The tooltip repeats the same non-transactional effect. There is no state invalidation or water-covered-state conversion path whose survivors can be transferred before invalidation.

Disposition: do not call a famine pressure wrapper, flight-pressure wrapper, or exact transfer helper. The negative manpower effect is not an accepted civilian movement receipt and cannot be converted into a positive movement amount. A future flood owner must first persist each affected state, actor, positive surviving cohort, route, destination, and destination reception proof; only then may it call the migration transaction, and only a separately proven food-route loss may call the famine branch.

### Event 050, `chaosx.nr50.1`

Source: `events/050_the_great_embargo.txt:22-41`.

The root selects a random major or human country, fires the report/news chain, and registers a native condemnation embargo source through `every_other_country` at `:30-38`. It has no affected state scope, import dependence fact, restricted food route, insufficient domestic substitution, relief-exemption result, positive food amount, or state-specific responsible actor/receipt.

Disposition: do not call `famine_migration_request_famine_pressure`, `famine_migration_request_food_security_pressure`, or `famine_migration_request_blockade_pressure` from the country selector or condemnation registration. The island-blockade route is not proven by a generic embargo and no full blockade proof is available. A future owner-side shortage transaction must supply all four accepted Event 050 clauses, for the exact state, before using the famine seam. No migration call follows from embargo registration alone.

### Event 051, `chaosx.nr51.1`

Source: `events/051_heat_wave.txt:22-52`.

The root's hidden effect iterates every country, clears heat overlap through `natural_disaster_clear_heat_overlap_for_country`, and adds the country idea `heat_wave` for two years at `:30-39`. The option only reports the same idea at `:41-51`. This root does not expose affected states, crop/water/labor loss, positive people amount, responsible actor, migration amount, route, destination, or a direct-disaster Deaths receipt.

Disposition: do not call a famine, flight, or exact-transfer adapter from this country-wide idea/overlap operation. Event 051 must remain separate from the natural-disaster owner that can resolve exact affected states and direct mortality. If that owner later supplies a positive exact crop/water/labor shock and actor, it may call the famine seam; if it separately supplies exact movement and destination proof, it may call the migration seam. The original disaster owner retains Deaths.

### Event 095, `chaosx.nr95.1`

Source: `events/095_occupation_revolt.txt:22-63`.

The root selects a government-in-exile, selects a random enemy country, transfers each matching controlled state with `transfer_state_to = PREV.PREV` at `:33-36`, creates revolt divisions at `:38-59`, and fires the report at `:60`. This proves a control/ownership operation, not a civilian transaction. It does not prove famine, deportation, forced labor, unequal relief, protected administration, relief delivery, a positive civilian amount, a cohort, a route, or a destination. `transfer_state_to` is not a population movement receipt.

Disposition: do not call occupation, forced-labor, deportation, famine, flight, Deaths, or exact-transfer adapters from the revolt root or state transfer loop. Event 095 may consume accumulated revolt pressure only after a future owner records exact local famine/deportation/forced-labor/relief facts. Protected administration or relief can reduce revolt only when the owner supplies those exact live facts. No movement or casualty is fabricated for the revolt.

## Public API and no-double-counting proof

The inspected public contracts remain in `common/scripted_effects/chaosx_famine_migration_effects.txt` and `common/scripted_effects/famine_migration_adapter_effects.txt`; neither file was edited. `famine_migration_apply_pressure_request` requires valid state, a positive request amount, a proven non-unknown source, and a proven actor before registering food or flight pressure (`chaosx_famine_migration_effects.txt:1162-1213`). Source-specific wrappers are at `:1242-1369`.

`famine_migration_transfer_civilians_exact` is the sole exact state-to-state population primitive (`chaosx_famine_migration_effects.txt:1893-2053`). It debits the origin once through the existing state-population helper, separates requested route deaths from survivor credit, records route deaths through Deaths only when the owner requests that ledger receipt, and credits the destination only with measured survivors. No Event 043 or Event 095 state/control effect qualifies as that transaction.

The adapter file explicitly keeps direct Deaths ownership with the original system and says route deaths remain inside the exact transfer ledger. No owner call in these four roots provides a new direct-death receipt, so no Deaths adapter was added and no mortality was duplicated.

## Required source and engine evidence

The required AGENTS.md, complete `chaos-redux-events` and `chaos-redux-subagents` skills, eight famine/migration specification parts, supporting matrices/prompts/routing/bibliography/closure review, permanent handoffs, offline wiki core pages, and applicable vanilla documentation were read before disposition. Relevant engine references included event scope/ROOT/FROM behavior, state and country effect scopes, event targets, `add_manpower`, `transfer_state_to`, scripted constants, and on-action behavior.

The offline references used for this pass include `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, and `AI modding - Hearts of Iron 4 Wiki.md`. Vanilla references included `documentation/effects_documentation.md`, `triggers_documentation.md`, `dynamic_variables_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`, and `common/script_constants/documentation.md`.

## MCP evidence

The mandatory baseline event inspection used selector `{kind: "event", eventId: ...}`, workspace `mod_chaos_redux_ea3b2d67c2c0`, `mode: "state_flow"`, downstream direction, depth 2, 40 nodes, 80 edges, helper expansion disabled, and refresh enabled.

- Event 043 returned `EVENT_INSPECTED_PARTIAL` with status `ok`, zero blocking diagnostics, and `MCP_INLINE_FILES_TRUNCATED` (355 source files total, 64 inline). Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9dc6b2e9910ddc400a154eada15adbc5cb5ecc406607f9ea85a5c01573c391f8/354fa1b6bdcd33a286e00a02f30a6af2fba4920e52aed3d613c7df2b5f813c01/event-state_flow-59143acd4a23.json`. Artifact SHA-256: `9dc6b2e9910ddc400a154eada15adbc5cb5ecc406607f9ea85a5c01573c391f8`. Graph hash: `05a83fd72cbf3aa808f3f48e2ce14384b2da160472498d76344f3d950a7b0ed6`.
- Event 050 returned `EVENT_INSPECTED_PARTIAL` with status `ok`, zero blocking diagnostics, and the same `MCP_INLINE_FILES_TRUNCATED` diagnostic. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c5ac06ae3034a769736fab540c28688eb955cf3d872e5d8465e11a287dcc65b/1b5217aec59161651fce5937a789c239f1605eb77275c7353d73b40b084c0892/event-state_flow-59143acd4a23.json`. Artifact SHA-256: `8c5ac06ae3034a769736fab540c28688eb955cf3d872e5d8465e11a287dcc65b`.
- Event 051 inspection timed out after 180 seconds while awaiting `hoi4_agent_tools` and returned no artifact.
- Event 095 inspection timed out after 180 seconds while awaiting `hoi4_agent_tools` and returned no artifact.

Baseline render attempts used the same selectors/workspace, downstream overview view, depth 2, 40 nodes, helper expansion disabled, and no HTML. Event 043 and Event 050 renders timed out after 180 seconds. Event 051 returned `INTERNAL_ERROR` with blocker `Unexpected internal error`. Event 095 timed out after 180 seconds. No render artifact is claimed for any of the four roots.

The first inspection attempt used the invalid selector shape `{eventId: ...}` and was rejected with `MCP error -32602: Invalid discriminator value. Expected 'event' | 'namespace' | 'file' | 'source' | 'node' | 'manifest' at selector.kind`. The corrected event selector was used for all baseline artifacts above.

Because no gameplay source changed, an after-change compare/re-inspect/render pass has no candidate delta to compare and was not run. No source-only result is presented as an engine-render comparison. If a future owner receipt makes one row patchable, rerun inspect, render, `hoi4.event_compare`, re-inspect, and render after the narrow callsite change, retaining any timeout or truncation artifact.

## Probability and validation

No weight, `ai_chance`, MTTH, random list, pool, or pacing value changed, so `hoi4.probability_inspect`, the required `chaosx_ai_probability_auditor` evidence pass, and `hoi4.probability_compare` were not applicable. The custom auditor route was not available in the callable tool surface; this is recorded for any future weighted patch rather than substituted with source-only analysis.

Read-only filename and callsite checks confirmed the four accepted event files above and no same-number prefixed common event/scripted-trigger/on-action owner files. `rg` found no `famine_migration_request_*`, `famine_migration_adapt_*`, or `famine_migration_transfer_civilians_exact` call in any of the four roots. No HOI4 process was launched.

## Blockers and next owner inputs

The exact blockers are missing owner receipts, not missing shared APIs. Event 043 needs a resolved affected-state set, positive surviving cohort and actor, route, destination, reception, and any pre-invalidation legal transfer point. Event 050 needs exact state import dependence, restricted route, insufficient substitution, absent relief exemption, positive food amount, and actor. Event 051 needs exact affected states, crop/water/labor amount, actor, and separate movement proof if migration is intended. Event 095 needs exact local famine/deportation/forced-labor/relief/protected-administration facts and a causal revolt-pressure receipt.

No fallback, fixed total, proxy state or actor, flat modifier, direct population mutation, invented route, or vague dual-branch adapter was used. The next patch should be limited to the exact owner transaction immediately after those facts are recorded, with source-specific famine and migration calls kept separate.
