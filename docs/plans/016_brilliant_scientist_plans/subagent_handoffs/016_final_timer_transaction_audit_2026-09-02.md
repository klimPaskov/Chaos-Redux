# Event016 final timer and transaction audit handoff

Date: 2026-09-02

Audit mode: read-only source, offline documentation, vanilla precedent, and bounded MCP evidence.

Scope owner: `/root/timer_and_transaction_audit`.

Only this handoff document was written by this subagent. No gameplay file was edited, no concurrent Event026 alien edit was reverted, no game was launched, and no logs were requested.

## Executive verdict

The current Event016 biological transaction paths have no confirmed orphaned production flag, duplicate refund, duplicate payout, stale-victim settlement, or false biological success in the reviewed source. The parent’s current source also closes the previously identified terminal-timer gap: production and staging cancellation now test country activity, their own active receipt, and authorization/unlock state, so clearing a receipt from a terminal callback can cause the timed decision to cancel and release its factory modifier on the next evaluation.

The remaining timer risks are evidence or cross-owner contract issues rather than a reason to bulk-rewrite timers: `days_remove` and `days_re_enable` constants are directly supported by vanilla, `days_mission_timeout = constant:` remains unproven by the available official documentation and vanilla examples, and Event026’s working-tree Black Friday adapter can quote an Alien landing cost below the Event016 exact-2000 contract.
Parent review additionally distinguishes the Portal raid's selected-division reconstruction defect from the separate, source-reviewed ten-item Portal transport receipt used by biological deployments.

## Issues sorted by severity

### P2 — Event026 Alien quote is conditionally inconsistent with the Event016 exact-cost contract

`common/decisions/016_alien_infantry_landing_decisions.txt:23-39` routes the voluntary landing through `black_friday_can_reserve_alien_infantry_landing` and `black_friday_begin_alien_infantry_landing_reservation`; the concurrent Event026 adapter can use a dynamic quoted amount, while `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md:105-109` and `docs/events/016_brilliant_scientist/systems/alien_infantry.md:35-42` describe ordinary DHR landing as exactly 2,000 laser equipment.

The supported remediation is an owner decision, not a bulk patch: either keep the accepted Event026 quote and update the Event016 contract/localisation to state the conditional amount, or route the ordinary Event016 decision through the fixed 2,000-unit API and reserve the quote for an explicitly documented Event026 variant. Preserve the concurrent Event026 localisation/effect edit until its owner resolves this alignment.

Evidence limit: the source proves the fixed API and the dynamic adapter use their own receipts, but it does not establish which contract variant is intended after the concurrent Event026 change.

### P2 — Portal raid reconstruction does not conserve the selected division's state

The accepted rear-area Portal path is source-consistent: `common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt:162-172` requires a Portal target and ten `teleportation_equipment_1`, `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:163-208` stores and debits the exact transport amount, and `:221-237` refunds the saved transport amount exactly once or consumes it during settlement.

That biological transport receipt is not the native Portal raid's selected division.
The actual raid in `common/scripted_effects/016_brilliant_scientist_raid_effects.txt` destroys the assigned formation and recreates a full-readiness six-battalion cadre, so preserving formation count does not conserve existing manpower, carried equipment, damage, or experience.
The parent capability review in `016_final_raid_event_mcp_2026-09-02.md` found no documented exact-division relocation or lossless snapshot/rebuild primitive.
This is a concrete source/design blocker, not merely missing live proof; an alternative landing design requires user approval.
The separate biological receipt's exact runtime callback ordering remains untested, and its final audited source hash is `ded6a1dbf25aa8adb7c8aba20905fb349ed4cac4a7eb45efae4e12f4e511450d`.

### P3 — Alien capitulation guard remains queued for shared-adapter ownership

`common/scripted_triggers/016_alien_infantry_api_triggers.txt:61-80` makes reservation validity and the no-reserve caller check depend on contact, pending state, target validity, and `world_end`, but does not explicitly test `has_capitulated = no`.

Add the explicit capitulation guard in the shared Event026-compatible predicate when that adapter owner accepts the narrow change. Current world-end and target/control checks catch many terminal cases, but engine ordering is not proven here, so this remains a queued P3 robustness item and is not claimed fixed.

### P3 — `days_mission_timeout = constant:` support is unproven

The current `common/decisions/016*.txt` population contains 306 `days_remove` fields, of which 298 use `constant:` and 8 use `@`; 53 `days_re_enable` fields, of which 46 use `constant:` and 7 use `@`; and 32 `days_mission_timeout` fields, of which 28 use `constant:` and 4 use `var:`.

Vanilla directly proves `constant:` for decision timers in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/SIA.txt:406,408,441,443,479,481` and the related constants in `common/script_constants/propaganda_campaigns.txt:19-24`. Vanilla also proves variable mission timeout syntax in `common/decisions/ETH.txt:984,1017,1087`, and the official script-constant documentation requires field-specific support. No official documentation or vanilla precedent found here proves `days_mission_timeout = constant:`.

Keep the Event016 Alien mission at `common/decisions/016_alien_infantry_landing_decisions.txt:86-101` using `days_mission_timeout = var:alien_infantry_landing_reservation_days`; do not bulk-convert the existing 28 constant mission timeouts without parser or engine evidence. This is an evidence gap, not a confirmed rejection of the 28 existing fields.

### P3 — Cost localisation has two icon-first clarity gaps

Production support-equipment and manpower costs in `localisation/english/016_brilliant_scientist_projects_l_english.yml` use the expected texticons, and Alien laser cost text in `localisation/english/016_alien_infantry_api_l_english.yml` is dynamic and icon-backed.

The battlefield Portal wording in `localisation/english/016_brilliant_scientist_projects_l_english.yml:635-636` spells out `Teleportation Equipment`/`transport equipment` rather than using the equipment texticon, and the covert wording at `:640-641` says `two selected payloads` without showing the selected payload equipment icon. The supported narrow remediation is dynamic localisation using the existing equipment/texticon surface; no new GUI or cost family is needed.

### P3 — External `remove_decision` callers remain an untested cleanup edge

The vanilla effects documentation states that `remove_decision` bypasses the decision’s `remove_effect` and cooldown behavior. No current Event016 caller was found that externally removes the biological production, staging, or deployment decisions, and the parent’s own cancellation predicates now clear their receipts.

Treat this as an evidence limit only. If a future caller uses `remove_decision`, it must invoke the matching Event016 clear/refund helper first; do not add a generic global cleanup hook in this bounded audit.

## Timer support and factory timing

`days_remove = constant:category.key` and `days_re_enable = constant:category.key` are supported by direct vanilla SIA precedents. The official script-concept documentation at `documentation/script_concept_documentation.md:216-243` explains fixed-point constants and says field support is explicit; it does not override the absence of a mission-timeout precedent.

The current production decisions use available/custom-cost factory-floor checks at `common/decisions/016_brilliant_scientist_biological_operations.txt:67-74` and `:94-101`, while staging uses the corresponding check and one-factory modifier at `:121-127`. Vanilla `common/decisions/AUS.txt:1887-1897,2721-2736` and `ETH.txt:2138-2149` establish the same strict `num_of_civilian_factories_available_for_projects > floor` pattern with a `civilian_factory_use` modifier.

There is no confirmed factory-timing defect. The decision’s `complete_effect` starts the private callback immediately after selection, and the active decision modifier is the mechanism reserving the factory capacity. Adding a duplicate full factory-floor test inside the private begin helper could reject an exactly-funded project; no supported public caller bypassing the decision surface was evidenced. The begin helper should continue to validate consumable inputs and transaction state, while factory availability remains at the decision gate.

## Biological transaction and lifecycle notes

Production begins only for supported single/triple multipliers and unlocked selection, records its own agent/multiplier/output receipt, and debits support equipment and manpower in `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:90-125`. Completion adds the native equipment and clears the receipt at `:127-144`; cancellation clears the receipt without output. The current production cancellation predicates at `common/decisions/016_brilliant_scientist_biological_operations.txt:76-90` and `:103-117` test inactive country, missing own receipt, and lost authorization/unlock.

Staging is an input-free factory reservation and readiness timer at `common/decisions/016_brilliant_scientist_biological_operations.txt:121-144`; its cancellation predicate at `:129-143` has the same terminal, own-receipt, and unlock safeguards. It does not create a payload, so cancellation does not refund one.

Battlefield and covert deployment use an independent receipt in `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt`.
Start validates route, affordability, target, and saved victim before debit; Portal rear-area transport is stored separately; ordinary refund credits the saved payload and transport and then clears the pending/debited receipt in the same synchronous helper.
The direct-annexation path clears the former actor's receipt before crediting the annexing country, and settlement clears the receipt after recording one attempted operation.
`brilliant_scientist_biological_deployment_transaction_is_valid` revalidates existence, non-capitulation, world-end, saved victim ownership/controller, route, target, and transport mode, preventing settlement against a changed victim.

The canonical `bio_lifecycle_seed_record_is_valid` contract at `common/scripted_triggers/biological_lifecycle_triggers.txt:11-64` accepts Event016 battlefield success when the actor/victim proofs, deliberate source, payload debit/consumption proof, and saved victim controller are present. Its operative-release branch at `:35-45` intentionally exempts payload-debit proof because that native route owns its non-refundable operation cost; Event016’s local receipt remains the caller’s independent provenance. `bio_seed_batch_condemnation_proof` is only relevant to the canonical doomsday route and is not required for battlefield dissemination or operative release.

The standard dispatcher now gates exposure and success history on accepted `bio_seed_dispatch_status` in `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt:289-334,415-469`. A rejected dispatch consumes and settles the attempted local payload as failure under the accepted contract; it does not expose the target or claim success. Zombie dispatch captures temporary native inputs before actor scope, applies deliberate consequences before outbreak ownership transfer, and skips offensive consequences for home accidents at `:336-355`. Black Plague reuses the standard dispatcher and does not debit a second public receipt at `:357-374`.

Terminal cleanup is wired through `common/on_actions/016_brilliant_scientist_raid_lifecycle_on_actions.txt:33-52`. Immediate capitulation refunds the actor’s pending biological deployment and clears unfinished production/staging receipts before vanilla capture; annexation clears the annexed country’s receipt before transferring its exact saved payload/transport cargo once to the winner. The exact on-action scope ordering is supported by vanilla `00_on_actions.txt:1178-1180,1615-1617`, but runtime ordering is not live-proven here.

## Alien isolation and reservation notes

The ordinary Alien decision at `common/decisions/016_alien_infantry_landing_decisions.txt:9-84` owns one state target and one pending reservation, uses the fixed seven-day reservation duration, and cancels through the shared invalid-reservation predicate. The mission at `:86-101` uses the saved reservation duration variable and has one success path.

The fixed API in `common/scripted_effects/016_alien_infantry_api_effects.txt:221-243` debits exactly 2,000 laser equipment, stores the amount, and activates one mission. The amount adapter at `:245-284` is the Event026 extension. Cancellation at `:286-314` clears pending state before refunding exactly the saved amount, and the Event019 universal component is marked refunded only after its own provider refund path. The public spawn helper at `:394-613` now immediately cancels/refunds an invalid pending reservation rather than silently clearing it; successful pending calls clear the reservation exactly once.

Event019 keeps its own deferred transaction and calls the Alien provider commit/rollback callbacks in `common/scripted_effects/016_alien_infantry_api_effects.txt:616-671`. The provider does not share Event016’s voluntary landing receipt, and no double debit or double refund is visible in the reviewed source. Exact callback ordering and cohort conservation remain source-only evidence.

## Decision category, cognitive load, and mission quality

The biological category wrapper begins at `common/decisions/016_brilliant_scientist_biological_operations.txt:12`, with category metadata in `common/decisions/categories/016_brilliant_scientist_raid_lifecycle_categories.txt:18-23`. Before selection it exposes up to six mutually exclusive agent choices; after selection it can expose up to five remaining choices plus single production, triple production, staging, battlefield release, and covert release, which is at the six-action density boundary and can reach ten visible rows in the theoretical fully unlocked case.

The values shown to the player have clear significance: support equipment and manpower are production inputs, factories are an occupation requirement, Command Power and payload equipment are deployment costs, transport equipment is the Portal-only surcharge, and laser equipment is the Alien reservation cost. The custom trigger/cost tooltips explain blocked state without dumping the full raw trigger. The Alien surface has one visible action and one active mission, so its action density is clear.

| Surface | Owner/category/region | Requirement and duration | Success | Failure/cancel and duplicate risk |
| --- | --- | --- | --- | --- |
| Single/triple production | Biological operations country/category | Selected unlocked agent, support/manpower stockpile, factory floor; 30/60 days | Adds the corresponding native pathogen equipment and clears its own receipt | Terminal, lost receipt, or lost unlock cancels without output; active flag and receipt prevent duplicate production |
| Staging directive | Biological operations country/category | Selected unlocked agent and one factory; 90 days, then readiness window | Records staging readiness without consuming payload | Cancellation clears only staging state; active/ready flags prevent duplicate staging |
| Battlefield release | Biological operations state-targeted decision | Valid enemy operational target, route, Command Power, selected payload, optional Portal transport; 7 days | Dispatches canonical battlefield seed, applies accepted exposure, and settles one receipt | Target/victim loss refunds saved payload and transport once; transaction validity prevents wrong-country payout |
| Covert release | Biological operations state-targeted decision | Valid enemy industrial/strategic target, route, Command Power, two selected payloads; 14 days | Dispatches operative-release seed and settles one receipt | Invalid target refunds once; native route’s non-refundable cost remains separate from Event016 payload receipt |
| Alien landing mission | Alien API country/category/state | One pending reservation, valid owned/controlled state, fixed or accepted adapter amount; 7 days | Spawns one locked cohort and clears reservation | Invalid reservation cancels and refunds once; Event019 deferred receipt is isolated from voluntary landing |

## Cost, requirement, AI, and localisation audit

Single production costs 80 support equipment plus 250 manpower; triple costs 240 support equipment plus 750 manpower. Staging has no spendable payload cost. Battlefield uses 25 Command Power plus one selected payload, and the accepted Portal rear route adds exactly ten transport equipment, for at most three spendable cost types. Covert uses 50 Command Power plus two selected payloads, for two spendable cost types. Alien uses exactly 2,000 lasers in the fixed API, subject to the Event026 contract decision above.

All reviewed spendable values are within the four-cost-type limit. Support, manpower, Command Power, and Alien laser values are icon-backed; the two biological equipment wording gaps are listed above. No raw tooltip dump or fifth hidden spendable cost was found.

Biological AI and route checks are in `common/decisions/016_brilliant_scientist_biological_operations.txt:163-173` and `common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt:117-194`. They gate selection, stockpile, route, target ownership/control, war state, operational markers, and Portal technology. Alien AI and validity gates are in `common/decisions/016_alien_infantry_landing_decisions.txt:45-82` and `common/scripted_triggers/016_alien_infantry_api_triggers.txt:8-93`; they preserve source contact isolation, cooldown, target validity, world-end, and stockpile checks.

The required weighted/probability audit was intentionally left to the parent’s probability agent. This handoff does not claim a probability or balance pass.

## Validation and evidence limits

Offline Paradox wiki pages and the required vanilla documentation were read, including Decision modding, script constants, decision effects, triggers, on-actions, and factory modifiers. Vanilla SIA, ETH, AUS, and on-action precedents were inspected.

The bounded `hoi4.event_inspect` scan/lint returned `status ok` with `EVENT_INSPECTED_PARTIAL`; workspace-wide analysis was deferred. Artifacts were `event-scan-24c482050767.json` and `event-lint-24c482050767.json`, with no reported blocker for the selected source but no full parser proof.

Read-only base decision-surface evidence was collected with `hoi4.gui_inspect` and `hoi4.gui_render`.
Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/09486ee62020f28a713c76307a68135d288055f571e5d0ff9a6791f895f09333/b0f2f73e7eb1fd1b6fd4bd972344b50bdfb5b0d5d46d83e1774c6920a31911fa/gui-inspect.0615ddeef734e620.json`.
Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf551d536d5f323e23809df0f5530c6e66fe7983b7cd75e14d4bec5fd0e44e19/df1c85151d8adf205bd80175ce340bfe45fad61ed3c56d8926521619504c568c/countrydecisionview-full.svg`.
Dynamic Event016 rows were not executed by this render, and its clipping and zero-size warnings remain unresolved.
It therefore does not establish Event016 decision-row layout acceptance, nor does it excuse visible clipping as a vanilla-renderer discrepancy.

No in-game evidence was collected by design. Therefore exact mission teardown ordering, Portal exact-division conservation, annex/capitulation callback timing, dynamic localisation expansion, and `days_mission_timeout` constant parsing remain outside the source-only proof boundary.

## Recommended next actions

1. Resolve the Event026 amount contract against the Event016 exact-2,000 specification and align the decision, localisation, and docs.
2. Retain the current production/staging cancellation predicates and start/completion terminal guards; no duplicate factory check is recommended.
3. Queue the explicit Alien `has_capitulated = no` guard with the shared Event026 adapter owner.
4. Keep `days_mission_timeout` values variable-backed unless direct parser/engine evidence establishes constant support.
5. Replace the two literal biological equipment cost phrases with existing equipment texticons.
6. Resolve the native Portal raid's selected-division reconstruction design with the user, then obtain the required evidence for that approved design; the biological transport receipt is a separate transaction.

Simplifications and omissions: no gameplay simplification was made by this audit. The listed Event026 contract decision, Portal runtime proof, Alien capitulation guard, mission-timeout syntax proof, and two localisation icon refinements remain queued or evidence-limited as explicitly stated above.
