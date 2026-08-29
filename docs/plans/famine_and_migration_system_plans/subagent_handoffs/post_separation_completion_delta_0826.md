# Post-separation completion delta: famine and migration

Date: 2026-08-26

Mode: read-only completion audit; this handoff is the only file authored by this subagent.

## Verdict

Status: incomplete only at the retained external-evidence boundaries.

The current source implements famine and migration as separate owner systems connected by explicit causal adapters and the neutral exact-transfer primitive. After the parent-applied lifecycle, projection, decision-owner, helper, achievement, and documentation-contract repairs recorded below, this audit found no additional concrete gameplay, localisation, achievement, asset-consumer, workbook, conservation, decision-density, naming, category, or sparse-runtime defect that can honestly be patched from the present repository evidence.

Completion must not be claimed because four previously declared blockers remain: exact upstream receipts from external owners, exact probability certification, dynamic mapmode execution evidence, and user-owned live-consumer validation. These are retained blockers rather than unimplemented famine/migration mechanics.

The authoritative probability and completion documents were updated concurrently near the audit freeze. Their current wording correctly records the final owner patches and comparison-schema blocker. Historical probability handoffs remain provenance documents and should be treated as superseded wherever they describe the removed five-entry migration destination pool or state that no owner patch exists.

## Authority and audit method

I read all eight binding parts and every supporting file under `docs/specs/famine_and_migration_system_specs`, together with `docs/plans/famine_and_migration_system_plans/completion_report.md`.

I also read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, `chaos-redux-state-ledgers`, `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, and the workbook guidance. The relevant offline Paradox wiki core, decision, GUI, event, and mapmode pages and the corresponding vanilla documentation were consulted.

The binding correction used throughout this audit was:

- Famine and migration are separate mechanics.
- Active identifiers use `famine_*`, `migration_*`, `civilian_transfer_*`, or narrow neutral `humanitarian_*` names.
- The mechanics have separate categories and exactly two dedicated mapmodes.
- Each mechanic exposes exactly three player-facing values.
- Each category remains hidden until its own problem exists, while both mapmode buttons are visible from game start.
- There is no famine/migration event object, event id, event pool, event pacing, or whole-world recurring scan.

No source-only result below is represented as a substitute for unavailable MCP or live-consumer evidence.

## Requirement-by-requirement status

| Requirement | Status | Severity | Evidence and verdict |
| --- | --- | --- | --- |
| Separate owner lifecycles | Finished in source | None | `common/scripted_effects/famine_core_effects.txt:2527-2552` performs famine-only registered-state work and cleanup. `common/scripted_effects/migration_core_effects.txt:1706-1740` performs migration-only work for valid states and uses neutral dual-owner cleanup only when the state is physically invalid. |
| Separate retirement guards | Finished in source | None | `common/scripted_triggers/famine_core_triggers.txt:128-138` depends only on famine stage, pressure, famine-owned reception-demand projection, and blockade state. It no longer reads migration obligations or aligned migration arrays. |
| Separate categories | Finished in source | None | `common/decisions/categories/famine_decision_category.txt:3-15` and `common/decisions/categories/migration_decision_category.txt:3-22` are distinct, use owner-specific visibility gates, set `visible_when_empty = no`, and own separate GUI identifiers. |
| Exactly two dedicated mapmodes | Static source finished; execution proof blocked | P0 evidence blocker | `common/map_modes/chaosx_state_map_modes.txt:390` defines `famine_state_map_mode`; line 571 defines `migration_state_map_mode`. `interface/mapmodes_interface.gfx:56-69` exposes both buttons from start. No third combined famine/migration mapmode exists. Dynamic activation, colouring, tooltip, and click-region execution remain unproven. |
| Three player-facing values per mechanic | Finished | None | `localisation/english/famine_l_english.yml:3` declares Food Security, Food Reserves, and Relief Access. `localisation/english/migration_l_english.yml:3` declares Displacement Load, Reception Capacity, and Border Policy. Phase and priority prose are not additional meters. |
| No event object, id, pool, or pacing | Finished | None | `events/famine_incidents.txt` and `events/migration_incidents.txt` are absent; source has no `famine_incident.*`, `migration_incident.*`, or `chaosx.nr149.*` object. Event 149 is explicitly unavailable/absorbed in the workbook export. Negative MCP evidence is recorded below. |
| No whole-world recurring scan | Finished | None | `common/on_actions/humanitarian_runtime_on_actions.txt:12-44` contains the one-time startup achievement baseline and the bounded `on_daily_CXT` fallback only. `common/scripted_effects/humanitarian_runtime_effects.txt:35-70` loops the two sparse owner registries. The annex path at `humanitarian_runtime_on_actions.txt:65` is a bounded one-time owned-state pass. |
| Exact conservation | Finished in source | None | The canonical transaction remains `civilian_transfer_execute_transaction` in `common/scripted_effects/civilian_transfer_effects.txt`; owner decisions consume its exact debit, survivor-credit, and death receipts. No second population mutation was introduced by the separation repairs. |
| Causal famine-to-migration coupling | Finished in source | None | Food safety uses the versioned projection in `common/scripted_effects/famine_adapter_effects.txt:20-60`, `common/scripted_effects/migration_adapter_effects.txt:17-19`, and `common/scripted_triggers/migration_core_triggers.txt:311-334`. Survivor flight uses `famine_submit_survivor_flight_request` at `famine_core_effects.txt:1613-1654` and migration-owned acceptance at `migration_core_effects.txt:683-731`. |
| Decision ownership and density | Finished in source | None | Famine evacuation at `common/decisions/famine_decisions.txt:965-1148` proves famine need, calls migration-owned availability and transfer helpers, and delegates accepted corridors to `humanitarian_corridor_execute_evacuation`. The safer-state requisition at lines 1149 onward uses an adjacent famine-owned donor selector and migration-owned hazard seam. No missing player response or density defect was found. |
| AI paths | Source present; exact certification blocked | P0 evidence blocker | Final source inspection found complete declared pools of 10 famine and 18 migration candidates. Owner-separation AI changes are present, but exact scenario ordering and normalized behavior cannot be certified by the installed analyzer. Details and artifacts are below. |
| Achievements | Finished in source | None | Eight entries are present at `common/achievements/chaos_redux_achievements.txt:3850-3889`, with player text at `famine_l_english.yml:88-96` and `migration_l_english.yml:124-138`. Corridor completion crosses the narrow neutral achievement receipt, and the final undefined-helper census found the canonical custody and cohort-cycle achievement recorders. |
| Localisation and `humanitarian_cost` rename | Finished | None | Runtime source contains the active `humanitarian_cost_*` and `GetHumanitarianCost*` family and no obsolete `civilian_response_cost_*`, `GetCivilianResponseCost*`, or `GetCivilianResponse*` cost surface. No combined runtime `famine_migration_*` or `fm_*` family remains. |
| Assets and consumers | Finished statically; live validation blocked | P0 live-consumer blocker | `interface/famine_system.gfx:12-20` and `interface/migration_system.gfx:16-30` declare the normal, grey, and not-eligible achievement consumers. The completed asset census found 61 declared final DDS files with processed/round-trip evidence. No portrait, custom 3D model, sound package, counter, animation, super-event, or named-event GUI is in scope. |
| Workbook | Finished for this system | None | The editable workbook and generated exports retain Event 149 as retired and absorbed into the separate mechanics, unavailable as a random event. Concurrent unrelated catalog work changed global workbook/export hashes after the earlier freeze; that is not a famine/migration defect and was preserved. No combined event, cluster, scenario, or pacing row was added. |
| Documentation | Finished at current authority; historical notes superseded | None | `completion_report.md`, `source_of_truth_map.md`, `ai_probability_current.md`, and `chaosx_dynamic_effects.md` carry the separate owner contracts and current blockers. Historical audit handoffs are evidence snapshots, not current authority. |

## Accepted parent fixes and exact dispositions

### Migration category re-emergence from historical totals

Pre-patch evidence inspected during this audit showed `migration_refresh_decision_phase_from_state` comparing `migration_state_resettled_population` and `migration_state_returned_population` to `category_reception_load` at the former lines 666-667. The country trigger excluded those historical totals and retirement deliberately preserved them. A later bounded state refresh could therefore re-reveal a resolved migration category indefinitely.

The accepted parent fix removed both historical branches. Current `common/scripted_effects/migration_core_effects.txt:655-679` reveals only from incident count, live flight pressure, trapped population, or live reception load at lines 661-665. Historical totals remain accounting fields only. Disposition: closed P0 lifecycle defect; not a false positive and not a remaining blocker.

### Direct famine ownership of migration category and registry work

The audited pre-fix famine evaluator directly refreshed the migration decision phase, even though accepted survivor pressure already crosses `famine_submit_survivor_flight_request` into the migration owner. The famine sparse processor also called migration proof, safety, cohort reconciliation, and cohort cleanup helpers.

Current `common/scripted_effects/famine_core_effects.txt:1980-1994` applies mortality, publishes versioned food safety, refreshes famine modifiers, marks candidate capacity dirty, and retires through famine ownership; it does not refresh the migration category. Current `famine_process_registered_state` at lines 2527-2552 owns famine work only and calls the neutral physical railway projection. Disposition: closed P0 owner-lifecycle defect.

### Famine retirement and cleanup

The pre-fix famine retirement trigger depended on `migration_state_has_obligations` and aligned migration arrays, and recovery could dispatch `humanitarian_cleanup_state_registration` across both owners.

Current `famine_state_can_retire` at `common/scripted_triggers/famine_core_triggers.txt:128-138` retains the famine state only for famine-owned facts, including positive `famine_reception_demand_population` at line 136. Famine recovery calls `famine_cleanup_state_registration`. Disposition: closed P0 lifecycle defect.

### Versioned food-safety projection

The initial census found `migration_consume_famine_food_safety` called but undefined, live `famine_to_migration_food_*` consumers without a producer, and raw famine stage/component reads inside migration destination validation. That was a runtime and owner-boundary failure.

The accepted parent patch added a fail-closed versioned publisher and invalidator in `common/scripted_effects/famine_adapter_effects.txt:20-60`, a migration-owned consumer in `migration_adapter_effects.txt:17-19`, and a validator at `common/scripted_triggers/migration_core_triggers.txt:311-334`. Capacity and destination prepasses consume the projection; famine cleanup invalidates it; registered migration work refreshes it. An untracked/no-famine state does not fabricate safe proof. The unused migration `safe_food_reserve_donor` pool, wrapper, branches, and constant were deleted. Disposition: closed P0 runtime/ownership defect.

### Survivor-flight reservation ownership

Famine previously risked reading migration reservation ledgers and performing migration reconciliation. Current `famine_submit_survivor_flight_request` at `famine_core_effects.txt:1613-1654` publishes only the proven request envelope. `migration_accept_famine_survivor_request` at `migration_core_effects.txt:683-731` owns array validation, reconciliation, protected-floor calculation, reservation bounds, request cap, acceptance, and unconditional envelope clearing. Disposition: closed P0 ownership and stale-request defect.

### Independent migration retirement and presentation

Current `migration_process_registered_state` at `migration_core_effects.txt:1706-1740` uses migration-only cleanup for a valid inactive state at lines 1728-1733. It dispatches neutral dual-owner cleanup only for a physically invalid state at lines 1734-1739. Migration-owner files use migration modifier and presentation refresh helpers instead of the neutral dual-dispatch wrapper. Disposition: closed P0 lifecycle defect.

### Evacuation owner seam and deterministic safer-state donor

Current famine evacuation at `common/decisions/famine_decisions.txt:965-1148` requires famine-owned active food security, calls migration-owned country/state availability, delegates corridor execution to the canonical neutral endpoint, and uses migration-owned trapped-obligation staging, exact-transfer, and finalization helpers. Its second AI factor uses famine/famine-catastrophic stage flags at line 1009 rather than migration displacement.

`common/scripted_effects/famine_decision_owner_effects.txt:14-37` implements `famine_select_safe_food_reserve_donor` as a deterministic adjacent, same-owner, safe, highest-existing-positive-reserve selector. It does not initialize candidates, scan the world, or fall back to the foreign-donor relief pool. The parent's rejection of the stale proposed mapping to `famine_relief_select_donor` was correct. Disposition: closed P0 helper and owner-boundary defects.

### Remaining separation seams and undefined helpers

The accepted parent tranche changed famine AI trapped factors to the famine-owned reception-demand projection; moved destination safety, reception policy, and persecution checks behind migration-owned triggers; made projection changes notify the migration capacity owner; moved physical route damage to `civilian_transfer_refresh_route_damage_projection`; routed corridor achievement completion through a neutral receipt; and corrected the canonical evacuation entry point.

The final runtime call/definition census across runtime source found 473 scripted calls, 692 definitions, and zero undefined calls after canonical replacements for forced transfer, protected internment, protected forced labor, and transfer-cycle failure. The stale combined humanitarian mission/pressure block in `common/scripted_effects/chaosx_dynamic_effects.md` was replaced with separate famine and migration contracts. Disposition: closed P0 runtime-helper defects.

## Mandatory event evidence

The three forbidden/retired selectors were inspected and rendered against event graph revision `744cd12bca3e`; every result was a partial negative lookup with no event object.

- `famine_incident.1` inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d62c23469b865b0161f2c70f531db73cfe28b0fbaddfe4fe0cc01b833b18b485/5ba3e7bc96c1506c6d55e332934329ab8e24f4c794a45a96a3b98917c7fe2840/event-state_flow-744cd12bca3e.json`.
- `famine_incident.1` render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/497685a4cc332e965f934d64cb23deee7f69c1eb62f8eaa222198e9d9a521de0/9b10e10075926b93b39c5c0a62181e301f484aab0fe1f7d53a4bf58c43bd0ae6/event-overview-744cd12bca3e-manifest.json`.
- `migration_incident.1` inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f832478aa722be785b21fcbf66028192264350c674a1e8585eed3532a4203d6/8af8fe1fbf0d089faf17c1d8bd6b04436572d61b838e7413533182f7333bf870/event-state_flow-744cd12bca3e.json`.
- `migration_incident.1` render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/373960e41b4fc9903b28f6f1d23d80c1b6da36dc667ba545d2a54349e8463207/4e09d35b040d5aecc31e9a36a361f6bee8dfc1d999a578044f5f3e2506556b3a/event-overview-744cd12bca3e-manifest.json`.
- `chaosx.nr149.1` inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e11c9cd4da17aa83cc6495c2036e6b565210d581fdbcd4487e26cfc9c3d7cbc9/153b3afff6a9ef995d4936f66f07e0daff9021c3b9470ed101a03b427f16b745/event-state_flow-744cd12bca3e.json`.
- `chaosx.nr149.1` render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/adc1e446e7d99e31071253e4110700dee9a6e01f471c6b03548fdd72e852e728/0c371697f668f41913b2a95188b372c6977cadb08a78da7cda5bfb28efc13712/event-overview-744cd12bca3e-manifest.json`.

`hoi4.event_compare` was not applicable because none of the three event objects exists and there is no baseline/changed event revision to compare.

## Mapmode evidence and limit

Existing static inspect/render evidence:

- GUI inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3dfcf63cd977826ebcf0c0929da3e9271a79ef0c4b6cfdfda0f5246780fd3575/6c2b73d7c89de9ae8ffc085b6aec51c8a1b87fe3ce92224c22e5e7bfac4c35d8/gui-inspect.9590e797d841572a.json`.
- GUI render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b917c62bdfce4541d5f58ddc41eaf6ed5884f630a57a3ea88effd5f0cd3cf003/b10b1c79f83a9f0403079ff59ebdde72a9fafc41aeb639eec9df9890da29af8a/MapmodesInterface_Ingame-full.svg`.
- Map inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a75193c5b26cd1180f60405e66b535e35ff3e96ad25d03aeeded209441129c2f/60deb73e299b4ab6ff6bc342e905d5758b8a18037e0444c2bdc859a58a4dfec6/map-inspect.24d421bcc68e84bf.json`.
- Map render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/54aca4aae57c108e044637123ef5a3cd9097ba9bc13d6f6f8670f5257d9e51dc/a53e6cad1f9c809827b8869d2d25e08c59aa60f048c0cfe2b7d362fdef8a8538/map-state.png`.

A fresh bounded map-inspect attempt timed out after 180 seconds. The artifacts prove static ownership, button placement, and map substrate only; they do not prove live mapmode activation, owner-specific colour projection, tooltip value resolution, or click behavior.

## Final probability audit

The required `chaosx_ai_probability_auditor` pass found no concrete source AI defect. It did not certify exact probability or balance.

### Current declared-pool inspections

- Famine decisions: `mission_ai_will_do`; complete 10-candidate pool; six required inputs; MCP source revision `7caa56bc69922e4ac74e494d19a279b8816aa78eee4be8be7a7052187e98f579`; MCP source hash `729c115b88697b86b2e70988fc1b093361a9220c673a94f2451b68f7613a5e74`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acd719d701e14b9e6b0c1c7b09f887386c7c4e65674f6052b698e5328fdd8aa0/7b911a370582d4a26ad301091bd644afda08efb62b1b52ef2161bbdf9656fb0e/probability-inspect-729c115b8869.json`.
- Migration decisions: `mission_ai_will_do`; complete 18-candidate pool; eleven required inputs; MCP source hash `84fa372dc07e66a1b07c299486834ce3112db3b03b8ecae2e8ca2022f014665a`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/606987e49cdca6e1b873ad1475cf70184f31259343d40fd89b243358a5c5056b/6a152f721c5f863384eb887b619ea2e9a6ec25a77209e582a74c74e02801f12f/probability-inspect-84fa372dc07e.json`.
- Migration destination selection: four live declared entries, but incomplete dynamic-candidate discovery; source hash `8169d9fb45fde0b399097d3f252c64fe6be7ba7e21a1e5952531ea8b34ddc65d`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a96188c86331f555ef4b3f706f85901555ec6e1f49b823694cc61e6599a7a368/2767d7dd3053467a2d425326ee7de011247498bd0dd14e7415ab86e4d41a82f2/probability-inspect-8169d9fb45fd.json`.
- Famine opposition: seven declared channels, but incomplete custom pool; source hash `4040a2f554f24521026236dad3316f209169a510b184103f4b81b1b437f1f22e`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69af1b8f8a18e350c14441c83bf37f47fa586d71efd6d103480ecf042b7d81bf/de9d458d8f21ab38d486f7b0e6837dbfd4acb99d7e1add93d4f08a39bce2f219/probability-inspect-4040a2f554f2.json`.
- Famine relief donor: incomplete dynamic registry with zero discovered candidates; source hash `7ea4b17392347739c4cb1630752666624bb8f489d2c8aeba915c80d29f060a8`; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38cc7f020663eaaa50b9d75603e6087e82cb7af6951d11a5829cd01e93ec4cd6/9fca70e4816ea62de5ca83d6646863f5696601db546f7f6644b48a13b6e88b5a/probability-inspect-7ea4b1739234.json`.

The removed migration `safe_food_reserve_donor` entry must not be restored to obtain a five-entry pool. Its removal is an accepted owner fix; the live famine foreign-donor pool and deterministic adjacent safer-state selector have different roles.

### Comparison blocker

Owner-applied weighted changes exist in the current source: famine decisions use famine-owned reception demand and famine-stage factors, migration corridor responses use the migration-owned humanitarian-open policy trigger, and famine relief uses narrow migration-owned persecution and policy seams.

The truthful before/current request was rejected with the exact error:

`MCP error -32602: Input validation error: Invalid arguments for tool hoi4.probability_compare: Unrecognized key: "sourceHash" at before; Unrecognized key: "sourceHash" at after`.

An earlier comparison returned analysis id `probability-a1fd0fc59443cc4150eda05a` with zero changes, but both sides resolved the same intermediate current source. It is not valid before/current evidence. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/23e92519c50c02cdf38441a6ef2ca934ee86c5cce993ec115cc9e7712854f8ce/8f6152079e14e3ec7be3d2a0a214429e888b9c92adfcaed97f9d4c36fce60a92/probability-a1fd0fc59443cc4150eda05a.json`.

MCP zero-score rows are unresolved typed scopes, not proof of zero willingness. Zero discovered dynamic candidates are incomplete discovery, not proof of an empty runtime pool.

## Frozen source hashes

These SHA-256 values were observed after the accepted parent fixes:

| File | SHA-256 |
| --- | --- |
| `common/decisions/famine_decisions.txt` | `966b31a3e49d5a0ad11e3483997e5f0567d0d83837b3c074fa293766ea4cc491` |
| `common/decisions/migration_decisions.txt` | `bd748779a4eb8a0037215a58be3f92597973f22be9e668a35efdc3cef9a3a6a6` |
| `common/scripted_effects/famine_relief_effects.txt` | `edb8313ee76953a2c20694e8c79c8469d1c2de0fc404f49bcff3ba9a8619858b` |
| `common/scripted_effects/civilian_transfer_effects.txt` | `e8c9de30fba8dcfb20bc242bb094d8d435c9144143ae9906ca9313adc09d9a0a` |
| `common/scripted_triggers/civilian_transfer_triggers.txt` | `0e7888e818fc2a63d70925e213faaa2057c2d51b773bd7a7d6521f13776d9db3` |
| `common/scripted_effects/famine_adapter_effects.txt` | `5dbfb4d1ee711be14b9b6abd7e4d088c3b3cddebb701eec56d5b1cb256c9e450` |
| `common/scripted_effects/migration_adapter_effects.txt` | `31511d8de334369711781b6be9ebf97ad1e29ac825d75c103ba6b2d401367f5d` |
| `common/scripted_effects/famine_core_effects.txt` | `0a2e02749a48fc58446d4aeb840f2413aa3c7ee3ad3dc8f0f1c6f446334713a7` |
| `common/scripted_effects/migration_core_effects.txt` | `9a496f7085b0d77cce88b43055587bd42fe1decffb784a5098f6577566f85528` |
| `common/scripted_triggers/famine_core_triggers.txt` | `fdec9deae30c6c28e0227a239430f6540cda31b3e785b288d49a999b0a5cf21b` |
| `common/scripted_triggers/migration_core_triggers.txt` | `17d6d2dca52dcd176277966f13a37256606ab693fc682974c1cca0f4d80e3f48` |
| `common/scripted_effects/migration_decision_owner_effects.txt` | `f624cb01816053945cf096c14ab75e3e067eb1bef651c0afaf0a819822e57364` |
| `common/scripted_triggers/migration_decision_owner_triggers.txt` | `d9c922be02fcf9b6f86e4e8bc08a0cacf417504202e5bf796afbf02d79132d99` |
| `common/scripted_effects/famine_decision_owner_effects.txt` | `6e5ffd468795bc8b1e019ac55118f2faf54690ea2f2d11b9e059b47f67ee47b8` |
| `common/scripted_triggers/famine_relief_triggers.txt` | `928570d6eacd7a10f76402df434e01db262aefee03a5a15ec2393cbc2962a77f` |
| `common/scripted_effects/humanitarian_achievement_effects.txt` | `84b7412fee34be658b850e60d85fb1c2d52213747929113dea045a1b7b80f516` |
| `common/scripted_effects/chaosx_dynamic_effects.md` | `34b7c40b6deb5efb5cc3bbebe6410b97b1c74b2fd4ccb85557de474bd36033f1` |
| `common/scripted_effects/camp_repression_major_country_effects.txt` | `dcc7150aad0ba8f8d2dbc60cfa080285f5d308403c3d6628b6e205c1c1f0822a` |
| `common/scripted_effects/migration_cohort_history_effects.txt` | `0a2977348604265bde7aeca53061a61a753fd3ca0704f161e469bcd7411a05ac` |

## Rejected false positives

- The former historical-total reveal branches were real when inspected and are an accepted parent fix; they are not a remaining defect or a stale audit hallucination.
- Famine no longer refreshes migration category state or migration cohorts from its evaluator/processor. The explicit accepted survivor request is the correct causal refresh path.
- Famine recovery no longer unregisters valid migration state, and migration retirement no longer unregisters valid famine state.
- Raw migration reads of famine food fields were replaced by the versioned projection. An untracked state fails closed.
- The famine adjacent reserve selector is not the deleted migration weighted pool and introduces no whole-world scan.
- Absence of famine/migration incident events is binding design, not missing content.
- No event-owned dedicated scripted GUI exists, so a `chaosx_event_ui_worker` handoff is not required for the shared/owner report surfaces.
- Broad `civilian_response_*` matches in unrelated CBRN temporary fields do not invalidate the completed humanitarian cost rename.
- Historical combined identifiers in explicitly superseded specs or handoffs are provenance, not active runtime authority.
- Unresolved MCP rows and incomplete custom-pool discovery are evidence limits, not proof of bad weights, zero eligibility, or empty runtime candidates.
- Concurrent changes to unrelated event-catalog rows are outside this audit and were preserved.

## Retained blockers

### P0: exact external-owner receipts

The system still cannot fabricate exact affected state, people, actor, route, cohort, and loss receipts where upstream owners do not publish them. The retained cases include generic occupation-law changes, strategic bombing, war/peace transitions, broad cluster/scenario identity-only callbacks, event integrations without exact cohort/route/actor/people receipts, absent source for Events 118/120/131, and hazard owners that currently fail closed without full proof.

Recommended action: each external owner publishes the exact bounded receipt at its mutation point and calls the existing famine, migration, or neutral adapter. Do not add recurring world scans or infer missing quantities.

### P0: probability adapter and comparison

The installed analyzer cannot bind all typed decision/state/target/neighbor/country scopes, cannot discover the dynamic destination/opposition/donor candidates completely, exposes score rather than normalized click/timing probability, and rejects historical source hashes in `probability_compare`.

Recommended action: repair the analyzer/scenario adapter to accept pinned before/after source objects and typed fixtures, then rerun the same named scenarios, custom-pool inspections, sweeps, and comparison through `chaosx_ai_probability_auditor`. Do not tune source merely to make unresolved tool rows nonzero.

### P0: dynamic mapmode execution

Static source and render evidence exists, but live activation, value projection, tooltip, colour, resolution, hierarchy, and click-region behavior are not certified.

Recommended action: obtain working `hoi4.map_inspect`/render and GUI state evidence for both dedicated mapmodes, or record the exact MCP limitation again if the route remains unavailable.

### P0: user-owned live consumer validation

Only the user can validate in-game decision execution, category dormancy/reveal/retirement, mapmode behavior, DDS consumers, exact transfers, and end-to-end achievement awarding.

Recommended action: retain this as a user-owned completion gate. No agent should claim live completion from static files.

## Changed-files statement and disposition recommendation

This subagent did not edit gameplay, localisation, assets, spreadsheets, source specifications, completion documents, or generated exports. It authored only `docs/plans/famine_and_migration_system_plans/subagent_handoffs/post_separation_completion_delta_0826.md`. No commit was created.

Recommended disposition: accept this handoff as the final post-separation completion delta; mark every parent repair above as closed/accepted; retain the four P0 blockers unchanged; supersede conflicting historical probability pool and no-owner-patch claims by the current `ai_probability_current.md`, `completion_report.md`, and `source_of_truth_map.md`; and do not open another implementation tranche unless one of the external owners or required evidence routes provides new actionable input.
