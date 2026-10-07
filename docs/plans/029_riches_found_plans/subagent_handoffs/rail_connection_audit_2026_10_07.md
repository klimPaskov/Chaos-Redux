# Event029 railhead decision and mission audit

**Date:** 2026-10-07.

**Status:** The bounded audit and owner-fix recheck are complete. The three P2 findings from the initial read are verified fixed in current source. Port sea-supply proof, the current same-context AI-auditor result, and native category visual fit remain unresolved.

**Scope:** This pass covers the Open the Railhead mission, its Rail Spur and Port Route initiators, capital rail predicates and builder, mission resolution, related cost localization, and their immediate lifecycle hooks. It is not a full Event029 decision-category audit.

**Workspace:** `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

I wrote only this handoff. I did not modify gameplay source, localization, art, spreadsheets, indexes, or the Git index, and I did not commit or launch the game.

## Initial findings by severity

1. **Weighted-decision validation remains partial:** The parent reports that `chaosx_ai_probability_auditor` is already delegated in the same context. I did not start a duplicate pass. Direct MCP evidence recorded below is partial and does not replace the live auditor’s scoped findings.
2. **P2, timeout identity and result cleanup, fixed after the initial read:** The initial read found missing timeout identity checks and an orphan-recount overwrite. The owner has added active-mission and `open_railhead` kind guards to both timeout outcomes, records the partial or failure result and stage, then clears active/cleanup/target state before recount. The exact current block hash and bounds are recorded below.
3. **P2, partial-success wording, fixed after the initial read:** The owner replaced the route-open claim with text describing incomplete or low-capacity transport works and increased extraction pressure.
4. **P2, inline cost density, fixed after the initial read:** Both start rows now show three iconized values inline. The full tooltips retain all four spendable costs and the 90-day civilian-factory commitment.
5. **Unresolved port proof:** The Port Route full-success condition remains `riches_found_port_route` plus `naval_base > 0`. No full sea-supply or convoy-path proof is present in this branch. This audit does not treat the port route as proven sea supply.

## Parent patch before and after

The frozen intermediate decision file predates the new active-mission and mission-kind guards in `available` and the outer `complete_effect` loop. Its inner success branch checked the route result but did not repeat progress, route-capacity, damage, or development conditions after construction.

The frozen builder also used `fallback = yes` for both rail checks and set `riches_found_railway_laid` immediately after the build call. The current builder omits fallback and writes that marker only after `riches_found_state_has_capital_rail_connection = yes`. The current completion branch rechecks the mission identity and success conditions after construction, then resolves a failed connection as partial progress.

The prior completion tooltip declared a dependable railhead or port connection as success. The current completion tooltip states the conditional full-success requirements. The partial tooltip was not updated and still claims that the route opens.

## Category lifecycle and cognitive load

`riches_found_mine_management` is an ordinary decision category with a static category picture and no attached Event029 scripted GUI. I made no claim about native row clipping, spacing, or rendering. The scripted-GUI skill was read for the required route check, but it does not provide a native decision-list layout contract.

This bounded pass covers two alternate transport start decisions and their shared auto-completing mission for one selected mine. Route-validity gates make Rail Spur and Port Route alternatives. The broader category contains many other Event029 actions, so simultaneous visible-action count across the category is outside this audit.

The controller country has a three-slot active-mission cap. `riches_found_country_can_start_open_railhead_mission` blocks another Open the Railhead subject for that controller, and `riches_found_start_requested_mission` repeats the same-type check at activation. The start decisions and mission are scoped to a selected mine controlled by the acting country.

The player-facing mission text names the rail or port connection, mine damage repair, and Mine Development above 35. The development threshold and success or partial consequences have clear significance. The internal route-capacity predicate is not named separately, and no source or scenario result proves every target condition under campaign state.

The category description is described in source as an ordinary list supported by a static mine-rush picture. The mission description is one sentence. The completion, partial, and failure tooltips are short. The current partial wording is the exception because it claims that a route opens in a branch that can fail to establish one.

## Mission quality

| Mission | Owner and category | Region and requirement | Duration | Success | Failure and cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| `mission_riches_found_open_railhead` | The controlling country that starts the targeted action; `riches_found_mine_management`. | The selected controlled mine, connected over allied ground to the current controller capital, or the existing Port Route branch. The mission also requires route capacity, no mine damage, and Mine Development above 35. | 150 days through country variable `riches_found_open_railhead_mission_days`, populated from `constant:riches_found_duration.open_railhead_days`; the start decision’s separate project timer is 90 days. The duration constant is within the configured 120 to 180 day band. | Rail success requires the post-build capital connection. The port branch still accepts a route flag and a naval base level. Full success records the generic success result, adds 8 development and 4 local order, sets the success flag, and applies a 90-day cooldown. The mission-success counter increments only through the verified full-success helper. | Partial completion adds 3 development and 6 extraction pressure, records the partial stage, and clears active/cleanup/target state. Timeout with a route flag applies the partial values. Timeout without either route flag reduces development by 8 and adds 10 extraction pressure. Cancellation does not apply failure effects; state-control change clears mission state and recounts the old and new controllers. The timeout recount currently rewrites the generic outcome as cancelled. | Low at activation: both the country trigger and start helper prevent a second Open the Railhead subject, and the shared active-mission cap is three. Timeout identity checks still need to match the completion path. |

## Rail connection and scope review

The current predicates treat the mine as a STATE and enter its `CONTROLLER` country. Inside that country scope, `PREV` returns to the mine state and `THIS.capital` identifies the controller’s current capital state. The builder and both rail checks use the same `start_state`, `target_state`, and `build_only_on_allied = yes` parameters. They omit `fallback`, so the native default of no path fallback applies.

The capital-state mine shortcut compares the current capital value to `PREV`, allowing the mine and destination to be the same state. The `riches_found_railway_laid` marker is set only after `riches_found_state_has_capital_rail_connection = yes`, including this same-state case. A scoped search found no consumer of that marker, so downstream behavior is not proven to depend on it.

The current capital is read again during preflight, construction, and post-build verification. A changed capital therefore changes the target used by the next evaluation. The bounded `on_state_control_changed` handler calls `riches_found_clear_mission_state`, then recounts both old and new controllers. The state transfer path clears the active mission and target state before later mission callbacks can complete it.

The retained pre-rail snapshot shows the older builder used `fallback = yes` for both `can_build_railway` and `build_railway`, then set `riches_found_railway_laid` immediately after the build call. The current builder removes those fallbacks and sets the marker only after the actual connection predicate passes.

## Cost and requirement clarity

The mission itself has no separate spendable cost. Its Rail Spur start action consumes support equipment, trucks, civilian trains, and an ongoing civilian-factory commitment. Its Port Route start action consumes trucks, fuel, convoys, and an ongoing civilian-factory commitment. Each start action therefore has four distinct spendable types, with no hidden fifth cost found in this bounded review.

The cost getters use icon tokens for each amount: `£civ_factory`, `£support_equipment_text_icon`, `£motorized_equipment_text_icon`, `£train_texticon`, `£fuel_texticon`, and `£convoy_texticon`. The full cost tooltips name the resources after the iconized values. The inline strings at `riches_found_cost_rail_spur` and `riches_found_cost_port_route` each include all four values; keep all four explicit in the full tooltip and reduce the inline row to three values.

The start requirements are non-consumed requirements: the mine must be selected and controlled, in the development phase, have a valid route family, have no already-open route of that family, and have an available mission slot. These are separate from the four payments.

## AI validity and route locks

Rail Spur is gated by `riches_found_rail_route_valid`, development phase, selected controlled mine, and absence of existing rail or port route flags. Its source AI factors include mine profile, state policy, inland versus island geography, war proximity, civil-war state, local order, and major status. Port Route has a separate port-validity gate and weights for mine profile, policy, island versus inland geography, war proximity, civil war, local order, and country status. Those source factors look context-aware, but their current scenario ranking was not established.

The mission itself has `selectable_mission = no` and a flat `constant:riches_found_decision_ai.medium` score of 3. The probability adapter treats this as a score, not a normalized selection probability.

The current mission probability evaluation used the named `RF_DEV_01_INLAND_DEEP_REEF` scenario after removing its unsupported `controls` and `closedFlags` fields. It returned raw score 3, `score_only` support, and unresolved eligibility because `scope.any_controlled_state` was not declared. The decision inspector also returned a partial result for this scenario, with `available` unresolved on the same scope and `days_mission_timeout = var:riches_found_open_railhead_mission_days` unsupported by that evaluator.

The earlier `decision_ai_will_do` inspection used a prior source hash and returned no matches for Rail Spur or Port Route. A refresh against the pre-fix source did not return before the request was terminated, so I do not use the earlier result as current evidence. The mission weight is a single constant with no local threshold to sweep. The owner fixes did not change an AI weight, so this subagent did not run a before/after probability comparison. The parent reports the named probability auditor is already live in the same context; this handoff does not duplicate or supersede its result.

## Cleanup and exploit review

Successful completion passes through `riches_found_complete_mission` only after the guarded post-build checks. Partial completion explicitly clears active and cleanup flags and the mission target. The country recount rebuilds the three-slot counter from controlled mine subjects rather than trusting a stale cached count.

Controller transfer invokes `riches_found_clear_mission_state` and recounts both controllers. The native cancellation path clears the subject/progress flags and recounts without applying timeout failure or a cooldown. No railhead-specific free reward or repeatable success loop was found in this scope. Full success alone increments the mission-success counter.

The initial audit found a timeout identity and generic-result mismatch. The owner-fix recheck verified active-mission and `open_railhead` kind guards in both timeout branches, explicit partial/failure result and stage fields, and active/cleanup/target clearing before the orphan recount. Exact bounds and hashes appear in the follow-up section below.

## Initial recommended narrow follow-up

1. Add active-mission and `riches_found_mission_kind.open_railhead` guards to both timeout result branches. **Disposition: fixed in the owner update, verified below.**
2. Resolve timeout state before orphan recount so partial/failure results are preserved. **Disposition: fixed in the owner update, verified below.**
3. Reword `mission_riches_found_open_railhead_partial_tt` so it does not guarantee that transport opened. **Disposition: fixed in the owner update, verified below.**
4. Reduce each start action’s inline cost row to at most three iconized values while retaining all four costs in the full tooltip. **Disposition: fixed in the owner update, verified below.**
5. Keep the port branch marked unresolved until its accepted success definition is clear about whether a naval base alone is sufficient or full sea-supply access is required.
6. Reconcile the live parent-delegated probability auditor’s current decision-weight findings for both target decisions, using the same named scenarios and explicit availability inputs. **Disposition: delegated by parent, result not reproduced in this handoff.**

## Evidence and validation

Initial-audit source hashes were: decisions `D5D1E9F5E0BC8672996E21893215425833EF1633E5655CBCA8412F4686B23344`, rail triggers `625CF72D32EBF52566744B228FFA9A03BCFF4FD93DB96952A1E47198E217B6AC`, works effects `933CC56C67555164809307F4A0030CC59DA2DE19984F02F06A386398A6E39D9D`, and decision localization `FF675ABFF7A64081328177725F4FBD2FDC7F8C54B4CF4737CC4145C3A49617B5`. The initial `source_lookup` decision revision was `013a6f655675581515af3389a0e14ab4e6705cdf41779053bc588ffabc68b6b3`; the then-current mission definition was at lines 9221 to 9351.

The frozen intermediate `decision_before_stale_recheck.bin` has SHA-256 `75DB9D6E2BA96B6ADEE916FE65CE8886D9B9F98881E0285EDB7A95791BA5740D`. The older frozen decision, effects, and localization copies have SHA-256 values `EBC33D0F6516E4B88ECBED35BB213F53381C729002226D6AF77B48D6AD5C166B`, `E9D5E1FBE6DA4BF294A1D1C422A9DEE3A9CFB1E1FFB867ADE5F76DB8F1378E49`, and `064994C368B6AF112B192B5E587ED8D32E3E583B44EB5E765F774E3AE2A755F0` respectively.

The offline wiki sources read were `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` at lines 1867 to 1868 and 1961 to 1985, `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` at lines 811 to 872, and `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` at lines 337 to 356 and 465 to 510. The MCP revision receipt for `Triggers` is `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`; the `Scopes` revision receipt is `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`. The locally read `Decision modding` file SHA-256 is `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`.

Installed game documentation read through MCP covered `triggers_documentation.md` lines 4603 to 4627 and 1884 to 1919 at revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, `effects_documentation.md` lines 2535 to 2571 at revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and `common\decisions\_documentation.md` lines 1 to 46 at revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`. The vanilla precedent was `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\PHI.txt` lines 2019 to 2027, nested under `PHI_investment_plan_1`’s `timeout_effect` and `every_owned_state`; its file SHA-256 is `468AE9A96EACD0E6339A810931A69C0228AD08EB652F8A0A0D58BCF48044A914`.

The current read-only map lookup for state 64 returned revision `1e98f09ced1876d2f63c8fcee9155077afbfb584a97a54b92e1620c51068d863`, one inspected state, and no province geometry or campaign rail-path result. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/403a22b003f706de45931bb91f828d9433a624dadc55e081071f150a477e4798/85db621412df602f2fe07e597c12e9defe80a237fcb7b04310d5c1e4555ab5d2/map-lookup.1e98f09ced1876d2.8d030eb3664782be.json`.

The current scripted-trigger file check returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, `parametersChecked = false`, 11 checked commands, 3 unchecked argument blocks, and 2 unknown scope roots, with documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`. The parent supplied a separate focused validation result with 2 unchecked argument blocks and the same parameter limitation. Neither result establishes parameter semantics or runtime rail construction.

The pre-timeout-fix mission AI evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d94415b52d96840296ce3b036d81cc7bfd60bff55f788ea4078eb471a9661308/fbd8569f3a02d0391f80cdfd1a015d2210e2f6136680a387c771fca08cb44736/probability-d47024e1c1bdf5244d58f468.json`. It reports raw score 3 and unresolved eligibility under scenario hash `a03defc227d3096b40aba12f013c9723bff74809b72ae60312ffbaa25255d6c4`. The pre-timeout-fix decision-inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f55e6990900ac90b2a3c44fe3095958d9310867b06c9bd6d18c74361fdd8490a/0aa498ff483888826f455f32adbf76323139cafc34874c7d55d9e6b13f442935/decision-de294f578115e73341852b75.json` and reports partial coverage.

The map artifact read and my refreshed direct decision-weight inspection did not return before their read-only requests were terminated. The map summary is insufficient to prove a rail path. The current start-decision weight result remains unresolved in this handoff. The parent reports a live auditor delegation for the same context and should reconcile its result before closing AI validation.

**Skipped meaningful validation:** No live-game validation was run, as required by the user. I attempted `hoi4.gui_inspect` with `windowName = riches_found_mine_management` and scenario `RF_DEV_01_INLAND_DEEP_REEF`; it did not return within 108 seconds. No `gui_render` followed because inspection returned no linked window or baseline, and the category source has no `scripted_gui` binding. The native category row’s visual fit therefore remains unverified. No full category action census was run because the request was bounded to the railhead branch. This subagent did not rerun the probability sweep or comparison; the parent has already delegated the scoped auditor pass.

**Remaining issues after owner-fix recheck:** The port proof remains unresolved. Current AI-auditor results have not been reconciled in this handoff. Native category visual fit remains unresolved because the inspect request did not return and the category has no dedicated scripted GUI.

**Skills applied:** `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-scripted-gui` for the category-surface route check. No skill files were changed.

## Owner-fix verification and dispositions

This follow-up is a bounded local-source check after the owner update. I did not rerun MCP analysis or edit gameplay source.

| Initial finding | Current disposition | Exact current evidence |
| --- | --- | --- |
| Timeout could resolve a stale or replaced mission and orphan recount could overwrite partial/failure as cancelled. | **Fixed.** Both timeout result branches now require `riches_found_mission_is_active` and `riches_found_mission_kind.open_railhead`. Each branch records its matching `last_mission_result` and `mission_stage`, clears `mission_active`, `mission_cleanup_pending`, and `mission_target`, then clears the mission subject/progress before the final recount. | `common\decisions\029_riches_found_decisions.txt`, mission block lines 9221 to 9371, timeout block lines 9311 to 9367. Normalized current mission-block SHA-256 `D09647E25E177EE22D5A90FA9D4BC6A7C96FEB69C3E6BFB3F20C4D7B0B8DB02F`. The retained pre-fix block SHA-256 is `AF3D89D232B1D302FEC8CCD7C0667328CD74BD3549807470F73D8731DB5D6B7B`. |
| Partial-success text promised an opened route. | **Fixed.** It now describes incomplete or low-capacity works and increased extraction pressure without promising a connection. | `localisation\english\029_riches_found_decisions_l_english.yml:23`. The railhead localization subset SHA-256 is `CB17C065D37CAAAA1814C840E97ADFEE0A387402933DDD57250CDABE1A82E181`. |
| Four values appeared in each inline cost string. | **Fixed.** Rail Spur and Port Route each show three iconized inline values. The full hover tooltip retains the fourth cost and the civilian-factory commitment for 90 days. | The inline keys are at `localisation\english\029_riches_found_decisions_l_english.yml:672` and `:679`; full tooltips are at `:674` and `:681`. |
| Parent concern that rail and port start phases might have changed. | **No change in the bounded caller blocks.** Each current block matches the retained pre-stale-recheck snapshot after line-ending normalization. | `decision_riches_found_rail_spur` block SHA-256 `4E29087C97BAFCDB22AF9E85BD47BD1987D85133FB1647DA3C5377552FA96AB5`; `decision_riches_found_port_route` block SHA-256 `B0B777D24E4DE94C074D51D70E59432DFAF5358848C656622EDD27238FC63C74`. |

Current full-file SHA-256 values are decisions `AE8C42A480A71CCD41AB2553DC324815DAADF6496A406F8B530123B5E2ADE7B9`, localization `0B5E5495AB2D7878EA5FCEAA674DC2B7CFBDB3682DC454225D8B7A5BF97D6CAD`, works effects `933CC56C67555164809307F4A0030CC59DA2DE19984F02F06A386398A6E39D9D`, and rail triggers `625CF72D32EBF52566744B228FFA9A03BCFF4FD93DB96952A1E47198E217B6AC`.

The railhead localization subset still hashes to `CB17C065D37CAAAA1814C840E97ADFEE0A387402933DDD57250CDABE1A82E181`. A bounded search found no 6,900 or 7,200 variants in the railhead decision block, its cost keys, or the referenced Event029 constants. Those other parent cost variants do not affect this railhead block.

The railhead mission block differs from the retained intermediate snapshot. The two start-action caller blocks match that snapshot exactly under normalized block hashing. The localization subset hash covers only the listed railhead and cost keys. I did not compare unrelated decision blocks or the rest of the localization file. Per the parent’s stated commit boundary, the two pending seal recipes and four unowned deny lines remain outside the rail-only commit.

**Still unresolved:** Port Route success still checks the route flag and a naval base level without proving sea supply. The parent-delegated probability auditor’s fresh targeted result is not included in this handoff. The ordinary category has no dedicated scripted GUI, and native category visual fit remains unverified after the `gui_inspect` request did not return.
