# Biological event caller lifetime repair

Disposition: implemented within the parent-approved bounded caller-storage scope, awaiting parent final integration and commit.
Acceptance basis: the parent explicitly approved 39 seed declarations, then eight nested declarations and five Japan bridge declarations, then one Event 016 Black Plague bridge receipt declaration on 2026-10-08.
The accepted design remains [the CBRN overhaul amendment](../../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md).
This work extends the caller-storage contract established by commit `0afbdf4d356e4fe0888e35a03d99e65efce0e272` and [the ordinary raid integrity handoff](../2026-10-07_biological_raid_service_integrity.md).
The parent owns final gameplay integration and commit.

## Completed patch and frozen evidence

Exactly 53 `set_temp_variable` declarations were inserted at 17 sites in four files.
No pre-existing source statement was replaced, removed, reordered, or normalized.
The [insertion manifest](../../../testing/2026-10-08_bio_event_lifetime/insertion_manifest.json) records every owner, baseline line, original anchor, field, default, and inserted byte span.
The adjacent `before/` and `after/` directories freeze the exact original and final bytes, with local `.gitattributes` applying `* -text` to preserve their mixed line endings.
All existing weights, costs, paid native lots, callbacks, gates, actor identity, release policy, RNG bodies, event log contracts, and CXT contracts remain byte-restorable.

| Changed file | Declarations | Before SHA-256 | Final SHA-256 |
| --- | ---: | --- | --- |
| `common/scripted_effects/012_africa_disease_effects.txt` | 23 | `C7CD1AD3DE30A39AA909F59D7CBD2D7913BDACCD8258FAA7E2830154A51C423D` | `7426739ED86D72D329F3432354B05483D3A9F3BC2A7FC444005D109B6DDE1AB2` |
| `common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt` | 13 | `7529A35E41E1F19F28629E34FEA18DD10E65E9BEEC00D17A5360A33E82A01490` | `2D117B57C7C044D05EC3F7A44CE7901329CEC8999F4061AAAC558C92725DE381` |
| `common/scripted_effects/japan_biological_campaign_effects.txt` | 12 | `AC8573C37071E4CDC2776C5882BB3506DBB519BA62F542C2DFD9DBEAF472DB16` | `A2F6FDA06ED75F5D65B7B14E8D7C11CA7089ABD1062432807260CBCF62AAA1D7` |
| `events/japan_cbrn_campaign_raid_bridge.txt` | 5 | `42F38FBA71C4E1B0D3B81B4543180BE95A867D986B525C60151F48ABB7F5FA5F` | `31F467B9572F3534EEABDC203D0E9D1C0C2BCC4DAAA54ADBD810A2EDFFD7B907` |

Python and `apply_patch` could not overwrite the OneDrive-backed Event 016 file after the initial seed tranche.
The unsuccessful writes left its captured bytes intact.
A native Windows sibling write followed by `Move-Item -LiteralPath ... -Force` completed the bounded update, with matching source hashes before replacement and final archive hashes afterward.
No recovery file remains.

## Caller-owned seed inputs and defaults

The four audited adapters are `africa_disease_dispatch_seed_from_current_state`, `africa_disease_dispatch_laboratory_accident`, `brilliant_scientist_dispatch_standard_biological_release`, and `japan_bio_campaign_dispatch_native_release`.
Direct assignments in an adapter already own their temporary inputs for the downstream dispatch call.
Values first created by the returning `bio_lifecycle_reset_seed_record` need the adapter to create storage before that reset call.
Dispatcher-private profile values, finalizer outputs, Condemnation working values, and retaliation storage are already declared in `bio_lifecycle_dispatch_seed` and require no adapter duplication.

For the table below, `zero` means `constant:bio_lifecycle_math.zero`, `one` means `constant:bio_lifecycle_math.one`, and `missing` means `constant:bio_lifecycle_proof.missing`.
The seven common defaults are `bio_seed_batch_condemnation_proof = missing`, `bio_seed_intensity_override = zero`, `bio_seed_exposed_share_override = zero`, `bio_seed_evidence_override = zero`, `bio_seed_condemnation_override = zero`, `bio_seed_concealment = zero`, and `bio_seed_force_detection_on_activation = missing`.

| Adapter and scope | Reset insertion point in frozen before source | Caller-owned defaults | Directly assigned inputs |
| --- | --- | --- | --- |
| Africa deliberate, selected STATE | line 35 | Seven common defaults | Agent from `africa_host.africa_disease_agent_slot`, battlefield route, deliberate source, persistent host result, four supplied proofs, required/consumed payload unit, weaponization one |
| Africa laboratory accident, selected host-controlled STATE inside COUNTRY adapter | line 114 | Seven common defaults, four actor/victim/debit/history proofs missing, payload required/consumed zero, weaponization one, totaling 14 | Agent from host, laboratory route, accident source/result |
| Event 016 standard release, actor COUNTRY preparing a target STATE | line 53 | Seven common defaults and weaponization one, totaling eight | Fully covered agent mapping, accident/battlefield/covert route and result branches, supplied actor/victim/debit/history proofs, required/consumed deployment payload |
| Japan native release, selected STATE inside actor COUNTRY adapter | line 121 | Six common defaults, omitting concealment | Agent, Japan campaign route, deliberate source, supplied proofs, payload quantities, program weaponization/concealment, result mapping |

Each adapter also declares `bio_seed_dispatch_status = missing` immediately before its existing dispatch call at baseline lines 49, 119, 97, and 144 respectively.
The dispatcher overwrites that receipt to missing at entry and supplied after its accepted seed branch.
The receipt records acceptance and creates no duplicate guard or replay exclusion.

`bio_active_agent` remains an outer cursor owned by some spread and rejected contexts.
The repaired shared dispatcher assigns it from `bio_seed_agent` only inside its accepted branch before storage.
This change introduces no adapter reset or blanket dispatcher-entry reset of that cursor.
Likewise, the existing shared dispatcher owns `bio_seed_retaliation_status = constant:cbrn_retaliation_status.none` before classification, and the biological classifier owns `cbrn_action_retaliation_status` before its nested generic classifier.
Those prior repairs preserve the nested attribution chain without more adapter fields.

## Returned status and attribution handoffs

Africa's deliberate STATE caller immediately consumes `bio_seed_dispatch_status` and writes regular `africa_disease_dispatch_accepted` on that state's CONTROLLER.
`africa_disease_launch_seed` initializes that country variable, then consumes it after its random controlled-state block to write the crisis and release history and perform its existing host payload update.
It clears the country receipt at exit.
Africa's laboratory adapter similarly initializes regular `africa_disease_accident_dispatch_accepted` on the host, dispatches within a controlled state, writes the host receipt only after acceptance, consumes it for the crisis flag, and clears it at exit.
These regular country receipts already cross helper boundaries correctly and needed no replacement.
The accident path supplies no new actor or victim pointer, and its missing proof defaults prevent a target retained from another chain block from becoming current attribution.

Event 016's standard actor-country caller dispatches under `var:brilliant_scientist_biological_release_target_state`, saves its CONTROLLER as `bio_seed_victim`, and copies the seed receipt to `brilliant_scientist_biological_release_dispatched` after returning to the country.
`brilliant_scientist_apply_selected_biological_release` already initializes this forwarded receipt before invoking the selected branch.
The outer resolver must own it before invoking that selector, so declarations were inserted in both its success and accident branches.
The success branch consumes it for existing success/failure history and exposure.
The accident branch retains its existing capital selection, exposure, and accident history behavior without introducing a new acceptance gate.
Event-root agent, route, native outcome, and transport inputs are directly assigned by the existing native outcome events.
The Event 016 event adapter directly owns the selected target and original victim before calling the resolver.

Japan's actor-country resolver already owns `japan_bio_campaign_dispatch_status = missing` before entering its dispatch helper.
The selected STATE caller copies the shared seed receipt into that inherited storage, then consumes it for state history and the exact-state humanitarian hook.
The actor dispatch helper consumes it for actor history, and the outer resolver consumes it for existing campaign credit and failed-dispatch history.
The original actor flag `bio_native_raid_dispatch_in_progress` is cleared at its existing position after dispatch, including a rejected seed.
No additional Japan status declaration is needed at the dispatch-helper boundary.

## Nested return map and exact additions

| Consuming owner | Producing helper | Output and required initial value | Baseline insertion point and consumer |
| --- | --- | --- | --- |
| `brilliant_scientist_resolve_native_biological_raid`, COUNTRY | `brilliant_scientist_calculate_biological_payload_requirement` | `brilliant_scientist_biological_payload_required = constant:brilliant_scientist_value.zero` | Before calculator line 212, then copied to deployment payload and used by standard seed proofs |
| Same resolver, COUNTRY | `brilliant_scientist_apply_selected_biological_release` | `brilliant_scientist_biological_release_dispatched = missing`, two sites | Before selector lines 217 and 234, inherited through standard and Black Plague branches |
| `japan_bio_campaign_dispatch_native_release`, COUNTRY | Actor-scoped `bio_sabotage_prepare_program_values_internal` | `bio_sabotage_weaponization_mult = constant:bio_sabotage_resolution.weaponization_operational`, `bio_sabotage_concealment = zero` | Before line 118, then copied into selected-state seed inputs |
| `japan_bio_campaign_resolve_native_raid_outcome`, COUNTRY | `japan_bio_campaign_select_native_result` | `japan_bio_campaign_result = constant:bio_sabotage_result.rejected` | Before line 175, then native failure/partial/success selection and shared sabotage result |
| Same resolver, COUNTRY across STATE then actor scopes | `bio_sabotage_record_failed_attempt_evidence_internal` | `bio_sabotage_attempt_lead_matches_actor = missing` | Before line 187, then `bio_sabotage_apply_failed_attempt_condemnation_internal` uses exact actor match for evidence visibility |
| Same resolver, actor COUNTRY | `japan_bio_campaign_prepare_doctrine_parameters` | `japan_bio_campaign_actor_cooldown_days = constant:japan_bio_campaign_timing.base_actor_cooldown_days` | Before line 195, then stored next-allowed day uses the returned base/theater/terminal value |
| `chaosx_japan_cbrn_raid.2`, actor-country event immediate | `japan_cbrn_raid_restore_biological_parameters` | Price tier normal, native engine outcome zero, agent none, payload/support required zero | Before bridge line 44, five fields then consumed by the resolver and its actor/state history |
| `brilliant_scientist_dispatch_black_plague_release`, COUNTRY with selected STATE | `black_plague_apply_weaponized_exposure_runtime` | `black_plague_weaponized_runtime_bridge_result = constant:black_plague_value.zero` | Before line 143, then state provenance and actor delivery history each require returned one |

All exact line values above refer to the immutable `before/` files.
The JSON manifest is authoritative for the original anchors and complete field names.
The Black Plague runtime already declares its nested `black_plague_exposure_result` before `black_plague_apply_exposure`, then copies it into the runtime bridge result.
Only the Event 016 consumer lacked storage for that forwarded bridge result.
The five Japan event declarations are inside the existing valid, unique-marker branch, preserving its failure behavior.
The restore helper still maps the native paid tier and quantities from those chain-local markers, with no change to its reservation table or payment path.

## Helper, constant, target, cleanup, and migration plan

No new helper is needed for these local ownership declarations.
They initialize each consuming frame rather than moving the same declarations into another returning helper.
No new tuning constant, duration, AI value, threshold, or table was added.
Existing constant categories supply all initial values.
Helper documentation is recorded in the owner and consumer map above, and the existing reusable dynamic-effects documentation at `common/scripted_effects/chaosx_dynamic_effects.md:352-370` already establishes the same caller-owned return contract.
No dynamic-effects file was edited.

Existing regular `bio_seed_actor`, `bio_seed_victim`, Africa host, Japan actor/victim/state, and humanitarian attacker targets remain effect-chain pointers.
Regular targets clear when their originating chain ends and cannot be manually cleared, so current proof fields remain the attribution guard.
No global target or persistent receipt was introduced.
The existing Africa receipt cleanup and native dispatch-flag cleanup are preserved.
Migration consists solely of creating storage at the exact consuming boundary before the existing helper executes.

## Meaningful validation

Run `node docs/testing/2026-10-08_bio_event_lifetime/source_tests.js`.
The [actual-source suite](../../../testing/2026-10-08_bio_event_lifetime/source_tests.js) records 105 passing cases and zero failures in [source_results.json](../../../testing/2026-10-08_bio_event_lifetime/source_results.json).
It imports the unchanged existing `BaseVM`, whose scripted calls discard temporary names first created inside the returning helper and preserve inherited names.
Country 7, victim 9, target state 100, and home state 101 have separate regular storage and flag maps.
Supporting source and constant hashes are included with the results.

- Every one of the 53 inserted statements reconstructs the archived after source from the original bytes, and current source agrees apart from permitted line-ending conversion.
- The four seed owners retain all 35 reset-only defaults at their actual dispatch call, with no prior global temporary dictionary granting accidental lifetime.
- Frozen-before runs reproduce 32 missing acceptance or history outcomes across Africa, Event 016, Japan, and the Black Plague wrapper.
- Four Africa agents cover accepted and rejected deliberate seeds, and laboratory acceptance changes only the host crisis receipt and its cleanup.
- Four ordinary Event 016 agents cover battlefield and covert releases using the actual calculator, selector, resolver, and standard adapter.
- A rejected Event 016 seed records its existing failure history without success credit, and the home accident retains capital state 101, host actor/victim identity, and the laboratory route.
- Japan covers both agents, three paid tiers, and four native outcome markers in both frozen-before and current-source stages.
- Japan's result getter, readiness program getter, restored payload quantities, actor/state history, failed-attribution forwarded proof, and base/theater/terminal cooldown returns execute through their consuming boundaries.
- A rejected Japan seed clears its existing native flag and withholds actor/state release history, and an invalid bridge fixture restores or dispatches nothing.
- The accepted and rejected Black Plague runtime receipts respectively allow or withhold both state provenance and actor delivery history.
- A rejected direct seed leaves an inherited active-agent cursor unchanged.

The suite executes the actual reset, shared dispatcher, four adapters, Event 016 payload calculator and selection/resolution bodies, and Japan restoration/result/doctrine/history/bridge bodies.
Native marker uniqueness, exact policy/target validity, route and agent profile arithmetic, finalization, storage mutation, retaliation classification, failed-attempt evidence production, and Black Plague runtime acceptance are explicit fixture boundaries.
The seed storage fixture captures the actual dispatcher handoff rather than executing a complete biological episode.
The failed-attribution case proves receipt transport into the condemnation consumer boundary and does not execute full evidence accumulation or sanctions.
The Black Plague cases prove the returned gate in Event 016 and do not execute the native runtime bridge.
No native raid, reservation collection, callbacks, payment/refund, outbreak potency, later spread/death/protection tick, scheduler, or complete balance behavior is inferred.
No game process was launched.

## MCP and reference evidence

The [MCP receipt](../../../testing/2026-10-08_bio_event_lifetime/mcp_receipt.json) preserves the reference context, detailed reads, source lookup, validation result, and interrupted event request.
Workspace identity is `mod_chaos_redux_ea3b2d67c2c0`.
Reference context reported omitted Event modding, Triggers, Scopes, and On actions sources.
This task claims only the targeted lifetime, setter, and regular-event-target rules actually read, with no general event-documentation coverage claim.

| Read reference | Windows path and lines | Revision |
| --- | --- | --- |
| Temporary lifetime and unscoped values | `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, 435-443 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Regular event targets and chain lifetime | Same wiki file, 303-311 | Same revision |
| Native temporary assignment and supported scopes | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, 7820-7827 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Native event-target scope support | Same installed effects documentation, 6496-6504 | Same revision |
| Vanilla direct-assignment precedent, `remove_from_allowed_party` | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/00_scripted_effects.txt`, 839-851 | SHA-256 `93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF` |

`hoi4.source_lookup` resolved the Africa deliberate helper at baseline lines 34-54 under index revision `3789fe6166bb10cd0aee944e4a103c460d376c4d673bb715af3398945e1741a6`.
Its definition was complete, but references were incomplete with 20,185 unresolved indexed references.
Repository searches supplied the explicit caller relationships recorded above, without promoting the partial index to complete consumer coverage.

The narrow `hoi4.event_inspect` request used `mode = trace`, selector `{kind: source, sourcePath: common/scripted_effects/012_africa_disease_effects.txt, line: 34}`, downstream depth one, eight nodes, twelve edges, and `expandHelpers = false`.
The client collection cell was terminated by this worker after approximately 120 seconds while that request remained pending.
No terminal result, server failure, timeout, event artifact, or job handle was collected.
The service outcome is unresolved, and parent direction prohibited further retries.
The two earlier attempts returned selector schema errors, which are retained in the receipt.
No helper-expansion mode or native task/job route was used, and no event render/compare artifact was obtained.
Source-model checks are not equivalent event or engine evidence.

`hoi4.script_validate` checked the 14 accident declarations as an explicit STATE effect against installed documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
It checked syntax, command kind, and declared scope, but returned `valid = null`, `parametersChecked = false`, and 14 unchecked native argument blocks.
Twenty findings were returned from 28 total findings, with eight omitted supported-command findings.
Parameter semantics and helper lifetime remain outside that route's validation.
No command-kind or scope contradiction was reported in the returned findings.

The parent separately routed weighted-body evidence to `/root/bio_remaining_probability` and received the immutable before/after archive locations.
This worker introduced or changed no weighted body and claims no numerical probability comparison.

## Simplifications, omissions, and blockers

No gameplay simplification or substitute mechanic was introduced.
The bounded caller-storage patch and its source evidence are complete.
Full native execution, queue behavior, callback cardinality, profile arithmetic, attribution/sanctions mutation, Black Plague runtime execution, live state history, and complete biological system acceptance remain unproved.
Event MCP coverage remains unresolved because the pending read-only result was not collected, and there is no render/compare evidence from this worker.
Other ordinary seed consumers outside these four owners remain outside this handoff.
No public text, asset, localisation, workbook, or CSV change was required by these internal storage declarations.
No new cleanup logic, constants, or helper API was added.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or updated.
