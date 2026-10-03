# Event 032 evolution gate probability baseline

Disposition: implemented (owner-applied source guard repair); numeric validation blocked/unresolved. The Event 32 contract requires separate enable gates and safe disabled behavior for all five evolution tracks. This disposition records implementation evidence, not standalone design approval.

Scope: EVO-11 disabled across five tracks, EVO-12 already recorded, EVO-10 Automatic Retaliation at 900 Chaos as the control, plus the parent’s requested post-adoption consumer audit. This auditor made no gameplay or Git edits. The owner’s separate EVO patch changed the current sources after the immutable baseline was captured. No game or desktop session was launched.

## Baseline finding

The shared Event Log toggle is events_log_toggle_current_evolution_disabled in common\scripted_effects\chaosx_events_log_effects.txt:2886-2911. It dynamically writes or clears the global flag events_log_disabled_evolution_<eventId>_<type>_<stage>. Event 032 records event 32, types 1 through 5, and stage 1.

The five immutable Event 032 before files and their current owning files were byte-identical at the audit snapshot. Every tracked read instead checks event_evolution_disabled_32_<type>. The current sources contain 42 such stale reads: operations effects 18, achievement effects 4, scenario effects 14, general triggers 1, and scenario triggers 5.

| Surface | Before path | Current path | Before SHA-256 | Current SHA-256 |
| --- | --- | --- | --- | --- |
| Operations, evolution unlock, scheduling, adoption and behavior | docs\plans\032_missiles_plans\baselines\2026-10-03_evolution_gates\032_missiles_operations_effects.txt | common\scripted_effects\032_missiles_operations_effects.txt | a6b34365268cecb810ed035249d50a944e2fc7013608576cfa3413ba7d2b27af | a6b34365268cecb810ed035249d50a944e2fc7013608576cfa3413ba7d2b27af |
| Achievement evolution requirements | docs\plans\032_missiles_plans\baselines\2026-10-03_evolution_gates\032_missiles_achievement_effects.txt | common\scripted_effects\032_missiles_achievement_effects.txt | 8e37412a0983b254c515781150c99621c0fdd5ddcef03cc3ba7827e8cb0f9736 | 8e37412a0983b254c515781150c99621c0fdd5ddcef03cc3ba7827e8cb0f9736 |
| Scenario setup and evolution profiles | docs\plans\032_missiles_plans\baselines\2026-10-03_evolution_gates\032_missiles_scenario_effects.txt | common\scripted_effects\032_missiles_scenario_effects.txt | 1202ada370727a797f0fbc6e10f480259351c79bfb55aab7af5f966add4af3a8 | 1202ada370727a797f0fbc6e10f480259351c79bfb55aab7af5f966add4af3a8 |
| Evolution and achievement triggers | docs\plans\032_missiles_plans\baselines\2026-10-03_evolution_gates\032_missiles_triggers.txt | common\scripted_triggers\032_missiles_triggers.txt | bf930048679fb0063b55cb2389784223ad1c76073039f92e806887cd17c18a6c | bf930048679fb0063b55cb2389784223ad1c76073039f92e806887cd17c18a6c |
| Scenario eligibility triggers | docs\plans\032_missiles_plans\baselines\2026-10-03_evolution_gates\032_missiles_scenario_triggers.txt | common\scripted_triggers\032_missiles_scenario_triggers.txt | 7108775c7116a86b6dd479d5b7e3facc562870a749a2cfad7794684cb1920e43 | 7108775c7116a86b6dd479d5b7e3facc562870a749a2cfad7794684cb1920e43 |

The achievement digest exactly matches the supplied raw before-path SHA. The parent reports that byte-preservation repair was committed as 7ab7b9407; no re-normalization or source write was made during this audit.

Track mapping for a future flag-only correction:

| Track type | Track | Current read | Shared toggle flag |
| --- | --- | --- | --- |
| 1 | Saturation Arsenals | event_evolution_disabled_32_1 | events_log_disabled_evolution_32_1_1 |
| 2 | Unreliable Guidance | event_evolution_disabled_32_2 | events_log_disabled_evolution_32_2_1 |
| 3 | Special Warheads | event_evolution_disabled_32_3 | events_log_disabled_evolution_32_3_1 |
| 4 | Rogue Launch Commands | event_evolution_disabled_32_4 | events_log_disabled_evolution_32_4_1 |
| 5 | Automatic Retaliation | event_evolution_disabled_32_5 | events_log_disabled_evolution_32_5_1 |

The 42 mismatches occur in pending-job cancellation, unlock recording, country adoption, guidance behavior, achievement credit, scenario profile setup and availability, and rogue/retaliation checks. With the canonical Event Log flag set and the legacy flag absent, the source predicates do not treat that track as disabled. This is an exact source-binding finding. MCP did not prove a runtime transition or numeric chance.

## EVO-10 source trace

The accepted scenario is EVO-10: Automatic Retaliation at 900 or more Chaos, no active world end, and a hostile missile pair. The relevant source helpers are missiles_evaluate_evolution_unlocks at common\scripted_effects\032_missiles_operations_effects.txt:550-613 and missiles_schedule_evolution_track at lines 455-547. The evaluation call is in common\scripted_effects\032_missiles_effects.txt:273, inside the accepted-firing-count-greater-than-zero branch.

The source requires missiles_program_ever_initialized, an existing global.missiles_firing_guided_count, Chaos at least missiles_evolution_pressure.minimum_chaos_retaliation, and global.missiles_firing_retaliation_count at least missiles_evolution_pressure.minimum_retaliation_programs. The constants resolve to 900 Chaos and two retaliation programs. The track delay is missiles_evolution_timing.retaliation_days = 150. The Automatic Retaliation branch does not apply the shortening multiplier used by several other tracks.

The 150-day value is a deterministic due-date increment after the evolution evaluation call. Event 032 has no mtth: entry in the inspected Event 032 source set. The evaluation is called from the accepted-firing setup path, so its source does not establish daily hazard timing or an exact campaign unlock date. The schedule branch itself contains no world_end or hostile-pair condition. Whether an upstream caller supplies those two matrix conditions remains unresolved because event_inspect timed out.

Classification: threshold source gate exact; due-date arithmetic bounded; caller bindings, pulse interval, campaign timing distribution, and selection probability unresolved. No candidate pool is normalized for this deterministic single-track path.

## EVO-11 disabled before, during and after adoption

At the captured pre-patch baseline, before scheduling and while pending, the wrong flag names mean the scheduler can enter its queue path when only the canonical shared disable flag is set. Its pending-clear branch also checks the legacy name, so it does not clear the pending marker for the canonical disabled state. When the due date is reached and the evaluation helper is called, missiles_record_evolution_unlock checks that same legacy name before setting the unlocked flag and writing the evolution log entry.

The pre-patch source therefore had exact mismatches for all five tracks at queue, cancellation and record boundaries. It did not establish a numeric chance. The evolution timing is an event-driven scheduled date, not an MTTH distribution or random selection race.

The pre-patch after-adoption audit found a separate gap that a 42-name replacement alone would leave:

- Country adoption flags are set by missiles_evaluate_country_evolution_adoption in common\scripted_effects\032_missiles_operations_effects.txt:135-180. No matching clr_country_flag for the five adoption flags was found in common\scripted_effects or common\scripted_triggers.
- missiles_special_payload_available in common\scripted_triggers\032_missiles_triggers.txt:288-296 checks the adopted Special Warheads country flag and any one of four operational integration flags. It does not check the shared disable flag.
- missiles_retaliation_network_available in the same file at lines 359-366 checks the Automatic Retaliation country flag, program management eligibility, and command-control threshold. It does not check the shared disable flag.
- missiles_operation_has_reliable_payload_custody in common\scripted_triggers\032_missiles_operations_triggers.txt:155 onward has four special-payload branches. Each requires the selected payload, policy permission, integration flag, and matching site custody; none checks the shared disable flag.
- missiles_integrate_requested_special_payload in common\scripted_effects\032_missiles_operations_effects.txt:1520-1562 tests the adopted country flag and payload readiness, then installs the selected integration and custody state without the shared disable flag.
- missiles_assign_selected_payload_custody at common\scripted_effects\032_missiles_operations_effects.txt:1465-1495 selects a random owned and controlled state passing launch and security checks, then sets payload-custody flags. The current integration path can reach it while the shared evolution is disabled after adoption. The actual state pool is unresolved.
- missiles_operation_can_be_prepared and missiles_operation_can_be_committed in common\scripted_triggers\032_missiles_operations_triggers.txt:62-91 do not check the shared disable flag. missiles_preflight_operation calls the four-branch custody trigger, and missiles_commit_operation at common\scripted_effects\032_missiles_operations_effects.txt:4477-4486 calls operation resolution after that local commit trigger. A disabled-after-adoption scenario therefore needs checks at the accepted preflight and commit boundaries.
- missiles_prepare_saturation_barrage in common\decisions\032_missiles_decisions.txt:477-512 and missiles_integrate_special_payload at lines 551-580 use local adoption flags for visibility and AI gating. Their current visibility/AI conditions do not read the canonical global disable flag.

The two decision entries retain their current score source values. Saturation barrage has base 1, a war factor of 5, and factor 0 when the Saturation country flag is absent. Special payload integration has base 1, a war factor of 4, and factor 0 when the Special Warheads country flag is absent. With the adoption flag left set, the source leaves those existing AI score blocks active under the canonical disabled assumption. The analyzer did not return effective score traces or normalized selection probabilities. The current category has 31 static decision definitions. The complete list is in the scenario JSON, while the live eligible subset remains unresolved.

The four payload authorization alternatives are chemical, biological, nuclear, and thermonuclear. The source has a deterministic OR of eligibility branches, not probability-proportional payload sampling. Their complete static set and unresolved integration, policy, custody, dynamic site-pool, and operation-state factors are in the scenario JSON.

Classification: retained adoption flags and missing canonical checks are exact source findings. Positive AI willingness under a disabled-after-adoption assumption is score-only. Candidate rank, decision-selection probability, dominance, starvation, rank reversal, and live operation outcomes are unresolved because the analyzer did not return numeric evidence and the live candidate subset is not bound.

The source supports an exploit-risk finding: after adoption, a canonical disable can leave special-payload integration/use and retaliation-network availability reachable through surviving country flags. This is a source-derived risk, not an observed campaign exploit. The owner-directed correction should gate visibility and operation eligibility, preflight, and commit using the canonical Event Log flag, while leaving inventory and site custody intact and keeping all numeric weights unchanged. Use the existing transaction paths and avoid a recurring world-wide scan.

The parent supplied immutable before copies for the operations triggers, decision file, mission file, Event 032 event file, and core effects. Their before hashes were read from disk and are listed beside the original five in the scenario JSON.

## EVO-12 already recorded

missiles_schedule_evolution_track checks the per-track unlocked receipt before setting a pending flag. missiles_record_evolution_unlock repeats the unlocked check before setting the global evolution receipt and calling record_events_log_evolution_entry. With the matching unlocked receipt present and pending flag absent, the source blocks a duplicate schedule and duplicate record for each of the five tracks.

Classification: source idempotence guards exact; persisted log state and runtime result unresolved. The scenario fixture supplies one already-unlocked case for each type and keeps the canonical disable flag off so EVO-12 is distinct from EVO-11.

## Owner patch source review

The owner’s final source tranche maps the 42 legacy reads in the original five files to the shared Event Log flags. The diff shows the expected canonical type/stage flags and adds enabled/active helpers for all five tracks. The current source scan has no event_evolution_disabled_32_<type> read left in common or events.

The operation trigger now checks active tracks during preparation and commit, and commit rechecks reliable payload custody. Special-payload availability and custody, retaliation-network availability, rogue incident opening, warning actionability, the emergency-delegation option, the saturation decision, and the special-payload integration decision use active-track checks. The preflight refreshes the AI profile. The operation receipt freezes rogue-bypass origin, the track gate checks that origin after the temporary bypass clears, and cleanup clears the frozen origin flag. The core saturation reserve-package multiplier uses the active helper.

The source diff preserves decision base/factor values and event ai_chance constants. The parent reports unchanged coefficient-token counts of 60 in decisions, 50 in events, and 17 in operations. These are source comparisons only. No normalized decision share, event-option share, hazard, or site-selection probability was returned.

The parent reports 17 source-level EVO guard tests passed. This does not establish runtime probability. The separate preparation-mission lifecycle findings remain with the decision auditor; the mission file SHA matches its immutable before file and no mission patch is part of this EVO tranche.

Final source reads confirm missiles_preflight_operation refreshes the AI profile before candidate selection and requires reliable payload custody. The commit trigger rechecks both missiles_operation_tracks_are_enabled and reliable custody before missiles_commit_operation resolves the operation. The rogue bypass origin is frozen in the operation receipt, survives clearing the temporary bypass, participates in the active-track check, and is cleared by operation cleanup. missiles_warning_is_actionable requires missiles_automatic_retaliation_active, so disabled queued warning work no longer passes the actionable branch. The owner reports its receipt settles without launching.

The raw country adoption flags remain for physical reserve-cap/custody behavior, civil-war inheritance, and achievement receipts with an explicit canonical enabled gate. New behavior and AI profile selection use active helpers. The ordinary preparation mission gate issues identified by the parent remain separate and unresolved in this audit.

The accepted pacing-fidelity gap remains separate. Event 032 stores a fixed due date and reevaluates on an accepted-firing call, while the specification matrix describes MTTH scenarios. No MTTH rewrite was authorized and the deterministic date is not presented as MTTH probability evidence.

## Final before/after source identities

The following current after hashes were read directly from disk after the parent’s final EVO source update. The scenario JSON contains the ten exact before paths and their before hashes.

| Source | Final after SHA-256 |
| --- | --- |
| common\scripted_effects\032_missiles_operations_effects.txt | 1fdaf60021d4824c0c4fb8f3170e9f92366dc2ef8b6ae3f4771f2afdebe42187 |
| common\scripted_effects\032_missiles_achievement_effects.txt | 2771ac0f85dc881bb2cfaf1ccf7fd58bc7718d9391115fb5a34282f509fee37c |
| common\scripted_effects\032_missiles_scenario_effects.txt | ad525a7412a6c8a026abeb99cf03b3faa68ca64df7b911cde9aca039b0649270 |
| common\scripted_triggers\032_missiles_triggers.txt | cdc2d9ba336e5d4c6c7c2367cd7fcd7d07dc6c87a726e93c5d36a889acef7fd9 |
| common\scripted_triggers\032_missiles_scenario_triggers.txt | b32007002e098ab801338a737aabfb1c3446b9e5ad626739b76d2820a3b8be65 |
| common\scripted_triggers\032_missiles_operations_triggers.txt | 3d08b39f0b6f45f59c5dd666ab30b7c9604c84e240b39d0b9814ee2e4f1d0e4b |
| common\decisions\032_missiles_decisions.txt | 2dac7ec6050754848b64f0737f1cb4e51d557bbe59f60f0253fd199aa3224db2 |
| common\decisions\032_missiles_missions.txt | a9d8a1f4c83d3b5450cda48540b8b69c38177c79ae0adacdfa61815ccd07f158 |
| events\032_missile_crisis.txt | b088e3245e1ce7858037f3a697045286f83a2e41dbddf69102dd18152a6f23ab |
| common\scripted_effects\032_missiles_effects.txt | 47cc92f71f3f927ed5b0e88277c039734c77fd21da7f2564828a6bbb581859b5 |

The five original baselines plus operations triggers, decisions, missions, event script, and core effects form the ten source pairs requested by the parent. The mission file is byte-identical to its before copy. The other nine source files differ from their before copy.

## MCP evidence and blockers

The required first probability inspection used adapter event_mean_time_to_happen on common\scripted_effects\032_missiles_operations_effects.txt with workspace mod_chaos_redux_ea3b2d67c2c0. It returned: tool call failed for hoi4_agent_tools/hoi4.probability_inspect, timed out awaiting tools/call after 600s.

A narrowed retry used the same source, adapter, explicit workspace, and candidatePool containing only missiles_schedule_evolution_track. It returned the same 600-second timeout. A separate probability_inspect for adapter decision_ai_will_do used the complete 31-decision candidate pool from the JSON. It also returned a 600-second timeout.

A narrow probability_inspect for adapter direct_random on common\scripted_effects\032_missiles_operations_effects.txt, targeting missiles_assign_selected_payload_custody, also returned a 600-second timeout. The eligible owned-and-controlled secure-state pool remains unresolved, and no site-selection distribution was produced.

The read-only source lookup for events_log_toggle_current_evolution_disabled succeeded at revision 090d4a720753b82afefdf0f4b4f112fad666bc67ce8e9aeed27e31b2e85a2129 and returned definition lines 2886-2911. It returned no references and marked reference coverage incomplete with 17,612 unresolved references. This confirms the helper definition and flag template only.

Five additional focused source lookups for missiles_special_payload_available, missiles_retaliation_network_available, missiles_operation_has_reliable_payload_custody, missiles_prepare_saturation_barrage, and missiles_integrate_special_payload each timed out after 600s. Their definitions were read from local source and their source paths and hashes are listed in the scenario JSON.

The narrow event_inspect trace for event chaosx.nr32.1 used a 12-node, depth-2 downstream bound and returned a 600-second timeout. The matching event_render unresolved view used the same event selector and bound and also returned a 600-second timeout. No structural artifact or rendered path was produced.

reference_context for the Event 032 surface timed out after 600s. The local references below were read directly and hashed. Parent-reported additional narrow retries, a 0.5 trace with 12 nodes and depth 2 and a rocket_engines technology inspect with 8 nodes and depth 1, also ended in client timeouts after 600s. No numeric proof was returned by those retries.

Post-patch probability_inspect was attempted for evolution timing, the 31-decision AI pool, the 10-mission AI pool, the four-payload direct-random custody selector, and the two separate five-option event pools. Every post-patch inspect call timed out after 600s. The post-patch event_inspect trace and event_render options view also timed out after 600s.

The first probability_compare probe with the exact operation before and after paths failed validation because each scenario lacked the required state record. A second probe with the full saved scenario objects failed on unrecognized scenario keys. The adapted comparison inputs retained all 22 scenario IDs and candidate pools and supplied only id/state records populated with source-defined global flags and variables. Country adoption, actor, target, warning, and physical-site bindings were left unbound rather than fabricated.

The first probability_compare schema probe failed because each scenario lacked the required state record; the second was rejected for unsupported top-level scenario fields. The adapted batch then issued 11 same-fixture calls covering the ten before/after source pairs plus separate event-option pools and a direct-random custody check. All 11 completed calls in exec cell 109 timed out awaiting tools/call after 600s. A twelfth operation-timing compare was still pending at the prior handoff. At the user's request, I polled the exact `functions.exec` cell 119 handle without restarting it; `functions.wait` returned `exec cell 119 not found`. Its terminal result is therefore unavailable in this runtime, not verified as a timeout. No comparison data, analysis artifact, MCP scenario hash, comparison ID, source-hash inventory, or rendered evidence was returned.

probability_evaluate and probability_sweep were not run because the required post-patch probability_inspect calls did not return. probability_render had no analysis ID or probability artifact to render. probability_simulate was not used because no MCP-supported uncertain-input model or seed was available. probability_sequence is inapplicable because this surface is not a declared custom weighted pool with a complete sequence manifest. Numeric probability, rank, dominance, starvation, and rank-reversal conclusions remain unresolved.

## Scenario and candidate completeness

The accompanying JSON preserves all 22 saved scenario IDs, including EVO-10, EVO-11 before pending, EVO-11 while pending, EVO-11 after adoption, and EVO-12 already unlocked. It declares the actual canonical flags, legacy reads, pending/unlocked receipts, track-specific source thresholds, the full static 31-decision category pool, all four special-payload branches, and local wiki and vanilla documentation hashes.

The static candidate inventory is complete for the Event 032 decision category, the mission file, both event-option pools, and the four special-payload branches. The random custody-site selector has a dynamic state pool that cannot be enumerated without a bound country and site state. The MCP scenario adapter accepted only id and state per scenario; the submitted projection retained source-defined global flags and numeric variables while leaving country adoption, actor, target, warning, hostile-pair, and physical-site context unbound rather than inventing scopes. There are no candidateOverrides or synthetic seeds. No MCP-issued scenario hash was returned. The externally computed SHA-256 of the submitted 22-scenario id/state projection is `af7b807ccd7aaff2df3abfd1fe8e75da20d8b211384365c606b7a982b376fd0d` (3,493 bytes; compact UTF-8 JSON without BOM, state keys sorted, scenario order preserved). This hashes the request projection, not the report or fixture file.

## References and skipped analyses

The offline wiki Event modding page was read at lines 130-132 for MTTH timing and line 159 for proportional ai_chance behavior. The offline Triggers page was read at lines 452-453 for has_global_flag. The offline Effects page was read at lines 349-351 for setting and clearing global flags. These local files are identified by SHA-256 values in the scenario JSON’s companion evidence below.

Installed vanilla documentation was read at triggers_documentation.md lines 3991-4001 for has_global_flag and effects_documentation.md lines 2801-2808 and 7085-7092 for clr_global_flag and set_global_flag. The relevant installed files and local file hashes are listed in the scenario JSON.

No chaos-redux-mtth skill pass was needed because the Event 032 source path contains no mtth: or mean_time_to_happen entry. The probability scenario matrix’s “Evolution MTTH scenarios” heading does not make this implementation a native MTTH hazard; the source stores a fixed due date and evaluates it on a later accepted-firing call.

Skills used: chaos-redux-subagents, chaos-redux-events, and chaos-redux-decisions-missions for the decision and mission AI pool review. No skill files were changed. The MTTH skill was not used because the inspected Event 032 path has no native mtth: or mean_time_to_happen entry.

## Handoff

The baseline finding and owner source changes are recorded separately. All ten immutable before files and final after hashes are listed in the scenario JSON. The same-fixture compare batch was attempted on those paths: eleven returned 600-second timeouts, and the twelfth operation-timing handle was polled but is missing from the active execution runtime. No result or artifact can be claimed for that call. No source edits were made by this auditor. Numeric selection, probability, timing-distribution, dominance, starvation, and rank-reversal claims remain unresolved.
