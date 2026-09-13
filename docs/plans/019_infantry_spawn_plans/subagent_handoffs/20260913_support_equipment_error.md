# Event019 Ethiopia support-equipment error handoff

Disposition: implemented in the parent-owned Event019 helper, with the evidence and limitation recorded here.

Scope: Ethiopia country setup reaching `chaosx.nr19.1` and the ordinary Event019 unit materializer.

## Finding

The reported line is `[equipmentpool.cpp:1540]: Trying to fill variant where none exist from type: support_equipment belonging to Ethiopia`.

The supplied error contains no runtime template, profile, stack, or event context, so the exact formation selected by the live run cannot be identified from the report.

The source chain is `events/019_infantry_spawn.txt:13-19` (`chaosx.nr19.1` to `infantry_spawn_fire_manifestation`), followed by `common/scripted_effects/019_infantry_spawn_core_effects.txt` country-generation setup and `common/scripted_effects/019_infantry_spawn_generation_effects.txt:2259-2329` (`infantry_spawn_spawn_current_template_unit`).

Country generation saves `infantry_spawn_generation_country` and executes the generation process inside `event_target:infantry_spawn_generation_country`, so the country scope at the materialization preflight is the generating country, including ETH.

The ordinary branch reaches generic `create_unit` at `common/scripted_effects/019_infantry_spawn_generation_effects.txt:2313-2319`, while `infantry_spawn_record_current_unit_obligations` runs only after creation at `:2339`.

Before this boundary, the ordinary template ledger is available through `infantry_spawn_accumulate_current_template_needs`; the raw support need is accumulated at `:1762-1811`, then scaled and rounded later at `:1839` and `:1853`.

Ethiopia history starts with `infantry_weapons`, `tech_mountaineers`, `tech_trucks`, and `basic_train`, without `tech_support`.

Vanilla `common/technologies/support.txt:20-24` enables `support_equipment_1`, while vanilla `common/units/equipment/support.txt:30` defines `support_equipment_1` without `active = yes`; `support_weapons` does not unlock the generic support equipment variant.

The parent technology inspection confirmed the focused dependency `tech_support -> equipment:support_equipment_1` with resolved status and confirmed confidence in `docs/testing/runtime_repairs/20260913_campaign_equipment_cleanup/support_technology_unlock_excerpt.json`.

## Ordinary profiles proven to require generic support equipment

`support_rich_reserve` is an ordinary candidate profile selected in `common/scripted_effects/019_infantry_spawn_generation_effects.txt:166-167` and carries engineer and recon support components behind their technology gates.

`engineer_reserve` is an ordinary candidate profile selected at `:214-215` and carries engineer and logistics support components behind the engineer and logistics-company technology gates.

`heavy_support_formation` is an ordinary candidate profile selected at `:313-314` and carries engineer and recon support components plus artillery, anti-tank, and anti-air support components; the latter three use their own equipment families and do not change the generic support-equipment conclusion.

The component accumulators add generic support need for engineer, recon, logistics, field hospital, signal, and helicopter support at `:1765`, `:1771`, `:1791`, `:1797`, `:1803`, and `:1809`.

## Parent-owned repair reviewed

The parent inserted the preflight in `common/scripted_effects/019_infantry_spawn_generation_effects.txt:2297-2308`, immediately before the ordinary generic `create_unit` call.

The guard requires the ordinary family marker `constant:infantry_spawn_lot_family.none` and `NOT = { has_tech = tech_support }`, recomputes raw template needs, and silently applies `set_technology = { tech_support = 1 popup = no }` only when `infantry_spawn_need_support_equipment > 0`.

Using raw need before start-equipment scaling prevents a small or zero rounded fill budget from suppressing the prerequisite when the template itself contains a support-bearing component.

The post-create obligation recorder still recomputes scaled quantities and debt, and no unit-template arguments, support companies, equipment quantities, or debt accounting were changed.

The ordinary-family guard leaves registered provider materializers outside this bounded repair, including providers that may publish support manifests after generic creation; no runtime evidence identifies one of those providers as the failing Ethiopia path.

The pre-edit source baseline is `docs/testing/runtime_repairs/20260913_campaign_equipment_cleanup/baseline/019_infantry_spawn_generation_effects.txt.pre_ethiopia_support_20260913.bin`, 139104 bytes, SHA256 `3b0336ffa0bacaeed24fae78302b037b28fb172e5e390791ce10382e0030ce7f`.

The parent-owned source after the insertion has SHA256 `f727af2b88c8e631fb54110e0061ceb509ed079163a8a48e9ac6517c26540402`.

## Generic support-archetype stockpile audit

Event019 contains generic `add_equipment_to_stockpile = { type = support_equipment ... }` accounting paths in `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:1388`, `:1434`, `:1448`, and `:1588-1591`; these cover management costs and refunds.

Additional generic support-archetype accounting appears in `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt:354`, `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:6471` and `:6474`, and `common/scripted_effects/019_infantry_spawn_management_effects.txt:430`, `:451`, `:5619`, `:6004`, and `:7123`.

These operations are outside the `chaosx.nr19.1` initial ordinary materialization chain and were left unchanged to preserve management, claimant, derivative, request, and incident accounting.

They remain an independent risk if an Ethiopia save reaches one of those positive archetype additions before `tech_support` is present; the supplied error does not identify any such call.

## Saved MCP evidence

The previously returned raw Event Chain Viewer result objects are copied under `docs/testing/runtime_repairs/20260913_campaign_equipment_cleanup/support_event19/`.

`event_inspect_trace_964dd033660a_attempt0.json` is the `EVENT_INSPECTED_PARTIAL` result with revision `964dd033660ad33876b6a25b579f70b5972852d29ed02fed266aabb47bd4e399`, graph hash `f48546410596e89b4866bc13bf797facdcc65f6e0190dff6dabe363cb7b280ac`, and copied-file SHA256 `0aac746e5d862d16468a6ff6aeb91c87bc478d176420bb6f66226264cd31541d`.

`event_inspect_trace_964dd033660a_attempt1.json` is the second returned `EVENT_INSPECTED_PARTIAL` result for the same revision and graph hash, with copied-file SHA256 `e94245b3c01adec8149d25fe17a9a2ef2047b2cb2e1aab60ed2a0a6933c01e54`.

Both inspect results report 9741 events, 15167 options, 1159 entries, 38371 edges, 30454 state accesses, 8739 unresolved nodes, zero blocking diagnostics, and deferred helper/lifecycle projection because the workspace analysis is large.

`event_render_964dd033660a.json` is the returned `EVENT_RENDERED_PARTIAL` scope result for the same revision and graph hash, with layout hash `359d23f17761e392e985dbbec2c71022c21c7d345f939c3b2e3a3cf1f8fbd2d1` and copied-file SHA256 `a060cf5bf307f2bd4a439d271a8ff67bbf5f802987712ba446edb72376ba597a`.

The render reports four selected nodes, 42570 omitted nodes, and no blocking diagnostics; helper expansion remains deferred in this large-workspace result.

The authoritative trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ea3df4b18fa22515105ea17dbb1cec7e9093dfe22536b5b9b5dde9b315c2a61/e641a123354cd369255959b91bd64427ae9df016496a613bc6c6ef055ddb5a2a/event-trace-964dd033660a.json`.

The authoritative scope render JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8489c129086c3387bda5fa3492020028a7fb42fe0adff342c28c585939994a9/89620558038d547a063e6a562116655a38acacb208fc8ccc8c57c3c87eef397b/event-scope-964dd033660a.json`.

## Validation limits

Source ordering and the parent insertion were reviewed directly, and the source SHA and baseline SHA are recorded above.

The MCP results are partial and do not expose the runtime-selected Event019 profile or fully expand scripted helpers, so the exact live failing profile remains unproven.

No game launch, console use, or log search was performed under the task constraints; live consumer validation remains with the user.

No country map, politics, focus, leader, portrait, flag, advisor, decision, asset, OOB, production, or starting-template surfaces were changed by this repair.
