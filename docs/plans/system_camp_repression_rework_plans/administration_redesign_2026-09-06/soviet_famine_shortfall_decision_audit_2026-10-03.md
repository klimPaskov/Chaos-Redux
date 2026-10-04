# Soviet famine shortfall decision audit (2026-10-03)

Disposition: unresolved for scoped completion. The accepted explicit no-resource responses are present in source, while cooldown wiring, event cost presentation, and decision-scene evidence require parent review.

Acceptance basis: the user selected an explicit no-resource response with famine and corruption penalties and no requisition debt on 2026-10-03. The implementation handoff records this basis in `soviet_famine_shortfall_implementation_2026-10-03.md`.

Scope: the Soviet relief decision, its 180-day mission, the warning and crisis event options, their dispatcher and trigger helpers, cost localization, and the owning decision category. This is a read-only audit. No gameplay files were edited and no commit was created.

## Issues sorted by severity

1. **Resolved during audit: success cooldown mapping.** The audit first found that the accepted relief route called the shared cooldown recorder without an action-ID mapping. The parent then added `sov_emergency_famine_relief` to the production recorder, mapping it to slot 2 and the centralized standard action duration. The updated fixture now parses the production mapper, mocks only the timed flag write, and asserts the exact flag name and requested duration. The refreshed result artifact still lists 17 passing parsed-source cases.

2. **High: the two event-funded relief options do not expose the three equipment payments.** `soviet_gulag.1.a` and `soviet_gulag.2.a` directly debit 120 motorized equipment, 18 trains, and 180 support equipment through `camp_rework_consume_labor_project_resources` in `common/scripted_effects/camp_repression_rework_effects.txt:5174`. Their current option labels in `localisation/english/camp_repression_rework_l_english.yml:538` and `:543`, event descriptions, and the current relief-effect tooltip do not show those amounts or texticons. `soviet_gulag_relief_funded_tt` exists in localization but was not referenced in `events/soviet_gulag.txt` at the time of this check, and it contains no equipment amounts. Parent owns the event binding. Bind a concise event tooltip that presents all three dynamic amounts with the matching icons.

3. **Medium: event callers do not yet show the stability consequence.** The accepted helper applies `emergency_relief_stability = -0.020` in `common/scripted_effects/camp_repression_major_country_effects.txt:2444`. The ordinary decision tooltip now explains the stability loss, but the two event-funded paths do not call that tooltip or the new funded-event tooltip in the source inspected. Keep this as a consequence rather than a fifth payment. Bind the event explanation, and keep it separate from the three equipment payments.

4. **Unresolved: the Soviet category may exceed the six-action presentation budget in crisis scenarios.** `gulag_and_mass_repression_system` has nine distinct clickable Soviet decisions: prisoner transfer, NKVD reinforcement, party review, military release, gulag dismantlement, famine relief, mortality concealment, administrative-collapse admission, and extreme periphery repression. The same package defines six Soviet missions. Their triggers are phase- and state-dependent, so this inventory alone does not prove that more than six actions or three missions are visible together. The completed decision inspection covered only four relief scenarios and did not return a category-wide simultaneous-visibility count. The broader camp rework remains incomplete.

## Category lifecycle and cognitive load

The native Soviet category becomes visible for an eligible Soviet country when camp-network, famine, route, or relevant site flags are active. The famine relief row itself is visible only for SOV with positive famine pressure. It is unavailable while its active mission or relief flag is present, while the shared slot-2 cooldown flag is present, or when any of the three equipment quotes is short.

The relief action adds no category or tab. The category contains nine decision identifiers and six mission definitions, but their exact simultaneous visibility was not returned by the scenario inspector. Do not read this source inventory as proof that all nine buttons or more than three missions are simultaneously displayed.

The player-facing famine value has a clear action threshold: the mission asks the country to reduce famine pressure below the dynamically localized medium band, currently 8, before its 180-day deadline. The shortfall tooltips identify famine pressure, corruption, and critical evidence as the affected values and state that active relief continues without duplicate penalties.

The reviewed shortfall text is brief and explains cause and consequence. The funded event options still omit the quantities they consume. No raw variable dump or long decision tooltip was found in this bounded surface.

The target category has no `scripted_gui` field. The shared `camp_repression_network_category` ledger interface is a separate category. The old `camp_rework_gui_execute_country_action_2` helper has a definition but no call site, while the current ledger button two routes to `camp_admin_ui_action_two`. I did not treat that legacy four-slot helper as a reachable famine-relief consumer or claim GUI coverage.

## Mission quality

`sov_emergency_famine_relief_mission` is owned by original SOV and is a non-selectable, manually activated objective under the Soviet decision package. It is countrywide and has no regional target. Its completion condition is famine pressure below `constant:camp_rework_threshold.band_medium` (8).

The mission lasts 180 days. Success clears the active relief and crisis flags, reduces famine pressure and quotas, advances reform, and schedules the existing report once. Failure clears the active relief flag and applies +12 famine pressure, +8 corruption, and evidence pressure. Cancellation clears the active relief flag and applies the minor famine penalty.

Duplicate starts are guarded by both the relief flag and `has_active_mission` in the decision, final order preflight, and event-funded trigger. The warning and critical shortfall effects also skip penalty application if relief is active or the mission remains active. The 17-case source fixture covers concurrent duplicate requests, stale equipment, active-relief popup responses, resolved famine, and invalid original authority, but it mocks the production cooldown mapper.

The slot-2 timed flag now starts when the order is accepted and lasts 150 days, while the mission lasts 180 days. After a full timeout, that flag has expired 30 days before failure resolves. The existing cutover handoff says failure or cancellation permits another paid attempt, so immediate retry after timeout remains consistent with that recorded contract and is not a free-cost loop. If retries should wait after timeout, reset the flag at the terminal outcome or use a duration longer than the mission.

## Cost and requirement clarity

The native decision has four explicit payment types: 30 political power, 120 motorized equipment, 18 trains, and 180 support equipment. Its `cost` field supplies political power. `custom_cost_trigger` checks the same three equipment quotes as availability, and `custom_cost_text` displays exactly three equipment values. The completed effect manually subtracts those three equipment types once.

Texticon coverage is correct in the decision cost string: `motorized_equipment_text_icon` and `support_equipment_text_icon` are defined by `interface/chaosx_texticons.gfx`, and `train_texticon` is defined by installed vanilla `interface/texticons.gfx`. The blocked string uses the same icons in red. Political power remains in the native cost display and is not duplicated in the custom string.

A balanced-block parse of the installed vanilla `common/decisions` folder found 75 decision blocks with both native `cost` and `custom_cost_trigger`/`custom_cost_text`, including four with an explicit script debit. `RAJ_arm_communist_militants` in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\RAJ_GOE.txt:5095` has `cost = 25`, a 500-infantry-equipment custom trigger/text, and subtracts 500 equipment in its completion effect at lines 5137-5156. The file SHA-256 is `3B99609B24365B753257F1B83ADA542E612225318A8D16BE06BC58EBDA5806FF`. This disproves a blanket reading of the older wiki sentence as forbidding any native/custom cost combination.

The decision inspector separately emitted `DECISION_COST_UNRESOLVED` with message `Conflicting or repeated decision cost declarations`. The installed vanilla block above uses the same combination, so I treat this as an analyzer limitation rather than a confirmed engine error. The inspector does not prove the current three-icon row's fit or runtime debit receipt.

The shortfall event options have no political-power charge. Their funded path consumes the same three equipment types. The event option UI has no native decision-cost row, so its tooltip must disclose the quantities and icons directly.

The helper also reduces stability by 2 percent. The parent accepted this as a consequence, not an additional spendable payment. The ordinary decision tooltip now exposes it. Keep the three payment types in the event-cost tooltip and state the stability loss separately.

## AI validity and route locks

The decision is restricted to `original_tag = SOV`, uses no target state, and has `ai_will_do = { base = constant:camp_rework_ai_weight.soviet_relief }` with weight 40. Its availability and final helper both recheck famine, equipment, and active relief state. The mission has `allowed = { always = no }` and no AI weight, so it cannot be started as a separate AI decision.

The probability auditor completed baseline and after decision-weight evaluations for 11 named scenarios with one candidate. Both report raw weight 40, `supportLevel = score_only`, and `conditionalProbability = null`, so these are not campaign-choice probabilities. `has_active_mission` and `scope.has_equipment` remain unresolved except the active-relief scenario, which resolves as ineligible. The baseline analysis ID is `probability-5a6197709fcc6d816acbf941` and the after analysis ID is `probability-4873a14c2cdd55e9bf6c9ada`, both with scenario hash `de0bd3db5e7955986c631de200339ca7e17600c7bbda504a92eddcd5218c2aa9`.

The 11 scenarios are `SOV-funded-exact`, `SOV-motorized-short`, `SOV-train-short`, `SOV-support-short`, `SOV-short-no-target`, `SOV-funded-no-target`, `SOV-concealed-target`, `SOV-discovered-target`, `SOV-active-relief`, `SOV-stale-resolved`, and `invalid-GER`. The sweep is pending and the probability-compare task remains running. The scenario adapter treats `scope.has_equipment` as one coarse input, so it does not distinguish the three quoted equipment items. No AI probability or balance completion claim is made.

## Localization and tooltip gaps

The decision has localized keys for the slot-2 cooldown flag, active relief flag, mission title and description, success, failure, cancellation, and the three equipment cost icons. The decision effect tooltip now mentions the stability consequence and the famine threshold.
The localization subagent reported no missing or duplicate English keys among 31 scoped popup, decision, mission, and visible-availability identifiers. The remaining gap is event-option binding and payment content, not missing key coverage.

The two funded event choices need a bound cost tooltip with the three texticons and dynamic amounts. The event-funded stability consequence also needs to appear through a tooltip bound to those options. The shortfall, relief-underway, and famine-eased option keys and their distinct warnings exist in localization.

## Cleanup and exploit risk

The funded helper clears the result receipt before preflight, consumes the three equipment types only after the shared order-ready trigger succeeds, and sets the accepted receipt only after debit. The paid decision dispatcher returns the 30 political power quote when the receipt is absent. The shared route applies a cooldown only after acceptance and clears the receipt. Event callers invoke the funded helper directly, add no political-power refund, and clear the receipt after the attempt.

Repository search found the normal paid decision as the only live route setting the famine-relief action ID. The old four-slot execution helper is definition-only, and the live camp ledger's button-two path is unrelated. I found no current non-paid dispatcher caller that can reach the political-power refund branch.

The implementation adds no requisition debt, direct population change, research grant, or successful relief reward to the shortfall options. The shortfall penalties are meaningful and guarded against duplicate application while relief is active.

The cost remains paid on every accepted relief attempt. The 150-day cooldown and 180-day mission timeout determine retry spacing, but a full timeout naturally clears after 180 days. No free equipment, political-power, unit, or research loop is present in the source reviewed.

## Before and after behavior

Before the accepted shortfall change, the warning and critical funded event options could call the relief helper without checking the required equipment and had no explicit no-resource response. The frozen pre-change event snapshot is `mcp/soviet_famine_2026-10-03/before_soviet_gulag.txt`.

After the change, funded event options require SOV, positive famine, no relief flag or mission, and the full three-equipment quote. The helper repeats this preflight before debit. Warning shortage adds 5 famine pressure and 3 corruption, using centralized constants in `common/script_constants/camp_repression_rework_constants.txt:1311` and `:1322`. Critical shortage uses the existing major failure outcome of 12 famine pressure, 8 corruption, and evidence pressure from constants at `:1312` and `:1323`. Separate relief-underway and famine-eased acknowledgements prevent stale popup choices from double-penalizing ongoing or resolved crises.

## Evidence and validation

The parent refreshed `soviet_famine_shortfall_source_results.json` after replacing the generic cooldown mock with a production-mapper exercise. The fixture asserts the emitted `camp_gui_country_action_2_cooldown` flag and the requested 150-day duration, while equipment, political-power, mission, and timed-flag effects remain mocked. The result artifact records 17 passing parsed-source cases. I did not rerun the fixture.

A negotiated `hoi4.decision_inspect` task completed after verifying server version `hoi4-agent-tools 3.6.0`, `Client.ping`, the live tool schema, and client/server `tasks.requests.tools.call` negotiation. Its task ID is `camp_famine_oct3:job_751f663f32fb22d3a4dc63e4d13bd1462252ac79d4eb8a252267f4bf6bf43b2b`. The linked artifact is `hoi4-agent://workspace/camp_famine_oct3/artifact/33072c8f32c09a78b28f717d83233be645130bd12fb426efe7ebcd04e256c2f4/7b1261122f7aacb0294f7706cfee3d8466bfbfe6b9d185b559b88b416df43a95/decision-36f3d899cdde7ab236c0fdfe.json`. I read and verified five byte ranges covering all 325,165 bytes, and the final SHA-256 matched the artifact URI. The inspection source revision is `ff9c6e80191d3170d41a3b805623e74e8c3ed0ede5c1164934202aa0e200be8a`.

The inspection returned `DECISION_ANALYZED_PARTIAL`, `complete = false`, with 7,921 decisions, 1,958 categories, four declared scenarios, and 218 unresolved definitions. It analyzed only the requested relief candidate. The raw AI score was 40 in each scenario and remained score-only. The active relief-flag scenario resolved the decision as ineligible. The ready-stock, one-unit-short, and resolved-famine scenarios remained unresolved for `has_active_mission` and three `scope.has_equipment` inputs, so they do not prove availability or payment behavior.

The regular connected decision-inspection call stalled after a scenario-corrected request. The earlier exact vanilla `hoi4.source_lookup` request timed out after 180 seconds, as recorded by the implementation handoff. I used the local installed vanilla decision source directly instead.

The offline wiki cost section was read from `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:284` through `:336`, revision `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`. Installed decision documentation at `common/decisions/_documentation.md:6` through `:45` explains `allowed`, `visible`, and `available`; its SHA-256 is `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`. Installed `has_equipment` documentation at `documentation/triggers_documentation.md:3835` through `:3843` has SHA-256 `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.

The installed `interface/countrydecisionview.gui:4` declares `countrydecisionview`, and its `decision_item` contains the cost-and-timer text control around lines 399-457. After verifying live 3.6.0 schemas and client task negotiation, I attempted `hoi4.gui_inspect` and `hoi4.gui_render` for this built-in native consumer. The task-enabled GUI inspection request failed with `Invalid task creation result` because the server returned no task handle, and the corrected normal `gui_inspect` and `gui_render` calls each timed out after 60 seconds with MCP `-32001`, without artifacts. The render request used `sov_relief_native_view` at 1936.1.1 with normal, locked, long-text, and missing-localisation states at 1920x1080 and 1280x720. The category has no linked mod-owned scripted GUI, and the old four-slot action helper has no current call site; its separate ledger UI was not treated as the famine-relief consumer. Native row cost fit and event popup layout remain unresolved. No game was launched.

The localization auditor completed a bounded text audit and its handoff is `soviet_famine_shortfall_localisation_2026-10-03.md`; event tooltip binding remains parent-owned and open.

## Changed files and remaining work

This audit changed only this report. Audited identifiers are `sov_emergency_famine_relief`, `sov_emergency_famine_relief_mission`, `soviet_gulag.1.a`, `soviet_gulag.1.c`, `soviet_gulag.1.relief_underway`, `soviet_gulag.1.famine_eased`, `soviet_gulag.2.a`, `soviet_gulag.2.shortfall`, `soviet_gulag.2.relief_underway`, and `soviet_gulag.2.famine_eased`.

Parent follow-up: bind the funded event tooltip with dynamic equipment texticons and the stability consequence, collect the probability compare and event inspection/render/compare evidence, review category overlap in a named SOV crisis scenario, and confirm that an immediate paid retry after the 180-day timeout is accepted with the 150-day cooldown counted from order start. The native `countrydecisionview` inspect and render calls timed out without artifacts. The broad camp rework remains incomplete and this audit makes no package-completion claim.

Plan handoff path: `docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/soviet_famine_shortfall_decision_audit_2026-10-03.md`.
