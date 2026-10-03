# Famine and migration weighted-logic evidence

Disposition: unresolved source and planning evidence; no balance certification.
Date: 2026-10-03.
Scope: read-only review of famine and migration decision AI scores, migration destination selection, famine relief donor selection, catastrophic-famine opposition selection, humanitarian-corridor response scores, and sparse timing.
No gameplay, AI, event, decision, mission, trigger, effect, constant, localisation, runtime, or spreadsheet file was changed. The only requested output from this subtask is this documentation handoff.

## Result classification

Current source constants, declared candidates, triggers, timer values, and control flow below are exact source facts from the named local files and their audit-time SHA-256 values.

Current effective decision scores, live eligible candidate sets, normalized weighted-pool shares, rank order, timing distributions, starvation, dominance, rank reversal, repetition frequency, and exploit safety are unresolved because the required current HOI4 MCP inspection returned no result and no typed campaign fixture was supplied.

The historical MCP artifacts listed below are partial score evidence for older source hashes. They do not certify the current source.

## Required MCP attempt and exact blocker

The connected tool inventory exposed the read-only probability family and its live schema. The single bounded starting request was:

- Tool: hoi4.probability_inspect.
- Adapter: mission_ai_will_do.
- Source: { path: common/decisions/famine_decisions.txt }.
- Workspace: omitted.
- Result: the call remained running after roughly 16 seconds; one additional bounded wait reached roughly 27 seconds total with no response; the call was terminated.
- Returned status, diagnostics, source revision, scenario hash, analysis ID, artifact URI, and rendered evidence: none.

The route was exposed, but the current service response is unverified. No probability_evaluate, probability_sweep, probability_compare, probability_simulate, probability_sequence, or probability_render call was made after the required inspect failed to return. I did not choose scenarios or treat source scans as MCP evidence.

The historical evidence report already in the repository is docs/plans/famine_and_migration_system_plans/ai_probability_current.md. Its results are dated 2026-08-26 and its frozen decision-source hashes differ from the current local files, so its analysis artifacts are retained only as provenance.

## Current weighted surfaces and source facts

Decision AI scores use the declared base and conditional factors below. The factors are source-defined and the trigger traces are exact. The effective score after matching those triggers was not computed in this audit. No score is a click probability.

### Famine decisions

Source: common/decisions/famine_decisions.txt; tuning: common/script_constants/famine_decision_constants.txt.

| Candidate | Base | Conditional modifier trace |
| --- | ---: | --- |
| famine_release_reserves | 12 | ×3 when target state has active food security; ×2 when famine food pressure is positive; ×0.5 at war. |
| famine_emergency_imports | 9 | ×3 when target state has active food security; ×0.1 when reception demand is positive. |
| famine_repair_relief_route | 14 | ×3 when target state has active food security; ×2 when at peace. |
| famine_escorted_relief_convoy | 16 | ×4 when famine food pressure is positive; ×0.25 at war. |
| famine_emergency_airlift | 8 | ×5 when famine food pressure is positive; ×2 when air experience exceeds its threshold. |
| famine_invite_relief | 7 | ×4 when famine food pressure is positive; ×2 under democracy. |
| famine_evacuation | 10 | ×4 when target state has active food security; ×3 at famine or catastrophic-famine stage; ×2 at war. |
| famine_requisition_safer_state | 5 | ×3 when target state has active food security; ×0.3 when reception demand is positive. |
| famine_conceal_crisis | 1 | ×3 under fascism; ×2 under communism; ×0.25 when famine food pressure is positive. |
| famine_maintain_extraction | 2 | ×3 at war; ×2 under communism; ×2 under fascism; ×0.1 when famine food pressure is positive. |

The ten rows are the complete explicit ai_will_do blocks found in the named famine decision source. Candidate eligibility still depends on category visibility, each decision’s visible/available/target and custom-cost gates, target-state scope, current timers, and the relevant country/state variables.

Source-level rank-reversal questions include whether emergency imports or requisition lose willingness when reception demand is positive, whether relief and route actions outrank concealment or continuing extraction under severe pressure, and whether war suppresses escorted relief or repair just when route demand is highest. These are unresolved scenario questions, not confirmed bad rankings.

### Migration decisions and corridor responses

Sources: common/decisions/migration_decisions.txt; tuning: common/script_constants/migration_decision_constants.txt and common/script_constants/humanitarian_corridor_constants.txt.

| Candidate | Base | Conditional modifier trace |
| --- | ---: | --- |
| migration_prepare_evacuation | 5 | ×3 when the target state has active displacement; ×2 at war. |
| migration_open_departure_routes | 8 | ×2 at war; ×2 when the country has active displacement. |
| migration_restrict_departure | 1 | ×3 at war; ×2 under fascism; ×1.5 under communism. |
| migration_close_border | 1 | ×3 at war; ×2 when reception capacity is exhausted; ×0.2 under democracy. |
| migration_evacuate_vulnerable | 13 | ×4 when evacuation is prepared; ×3 when flight pressure is positive. |
| migration_evacuate_workers | 8 | ×3 when evacuation is prepared; ×2 when a target-state owner has civilian factories. |
| migration_negotiate_corridor | 12 | ×4 when the target state is flagged as population-trapped; ×2 under democracy. |
| migration_accept_corridor_offer | 20 | ×2 when reception policy is humanitarian-open; ×1.5 under democracy; ×0.5 when the requester is at war with the responding country. |
| migration_reject_corridor_offer | 10 | ×2 when the requester is at war with the responding country; ×0.5 when reception policy is humanitarian-open. |
| migration_open_reception | 10 | ×4 when the country has active displacement; ×3 under democracy; ×0.2 at war. |
| migration_controlled_medical_reception | 14 | ×4 when the country has active displacement; ×3 when an owned state has an exposure receipt; ×0.25 under fascism. |
| migration_distribute_arrivals | 9 | ×4 when migration_reception_load exists; ×3 when migration_reception_capacity exists. |
| migration_transit_only | 6 | ×3 when migration_reception_load exists; ×2 under democracy. |
| migration_enforce_closure | 1 | ×3 under fascism; ×2 under communism; ×3 at war. |
| migration_local_integration | 12 | ×4 when migration_reception_load exists; ×3 under democracy; ×0.3 at war. |
| migration_third_country_resettlement | 7 | ×4 when the target state has active displacement; ×3 when migration_reception_load exists. |
| migration_voluntary_return | 10 | ×5 when the target state has active displacement; ×4 at peace; ×0 when forced return is pending. |
| migration_forced_repatriation | 0.2 | ×4 under fascism; ×2 under communism; ×3 at war; ×0 when the target state is flagged as population-trapped. |

The eighteen rows are the complete explicit ai_will_do blocks found in the named migration decision source. The current eligible race is not established by this source count. Each row still depends on visible/available/target triggers, target state and cohort, cost affordability, route and policy proof, current phase flags, and decision timers.

Potential sensitivity findings that require MCP evaluation include closure willingness rising with war and exhausted capacity while open reception is suppressed by war; reception and integration factors depending on whether a load variable exists rather than its magnitude; and forced repatriation receiving a zero factor for a target flagged as trapped. That zero may be a valid safeguard or a starvation path depending on whether such a state can pass the exact host, cohort, and destination gates. No conclusion is made without the complete decision candidate pool and typed scopes.

The corridor accept/reject pair is a willingness-score race when a valid offer is pending. Its current base scores and factors create deliberate rank-reversal cases across humanitarian-open policy, democracy, and requester hostility. They are not normalized option probabilities. The source supports a ten-day offer response deadline, a three-day response decision duration, a one-day re-enable interval, a one-day corridor pulse cooldown, and a ninety-day mission hold.

The migration decision constants also contain a second copy of famine AI key groups such as release_reserves, emergency_imports, relief-route, concealment, and extraction. A source search of current common script files found no active references to the migration_decision_ai copies; the famine actions reference famine_decision_ai instead. This is a source-level cleanup lead only. Any removal remains a future owner decision, and no balance value should be inferred from the duplicate declarations.

### Migration destination selection

Sources: common/scripted_effects/migration_destination_selection_effects.txt, common/scripted_triggers/migration_destination_selection_triggers.txt, and common/script_constants/migration_destination_selection_constants.txt.

The selector has four named pool modes: internal safe route, foreign safe evacuation, foreign transit, and third-country resettlement. These are pool types, not four candidates. Actual candidates come from the current origin state's adjacent states and are dynamically filtered.

A candidate must pass the shared current safety and route gate, including valid state and food-safety projection, acceptable rail damage and bombing recency, valid actor and owner/controller, no active persecution, bombing, trapped-population, camp, chemical-contamination, fallout, or outbreak exclusion, positive infrastructure, no hostile-controller war, reception capacity, destination history, and pool-specific ownership, border admission, and route conditions.

Candidate weights are additive source-defined values. Internal/foreign/transit/third-country bases are 20/12/10/12; safe route adds 16 and damaged route subtracts 12; available reception adds 8 plus bounded capacity headroom up to 40; foreign policy adds 12/10/8/4 for open/controlled/transit/quarantine; relation terms add opinion, ally, faction, subject, access, or guarantee bonuses and may subtract a negative-opinion penalty; matching ideology adds 6. Food, flight, fallout, exposure, reserve-production, reserve-transport, and forced-return risks subtract bounded penalties. Candidate weight is clamped from 0 to 1000.

The custom draw sums eligible weights, draws a uniform value over the total, and walks the same adjacent-state pool to bind a destination. Zero total fails closed. General evacuation tries the internal pool first and falls back to foreign-safe evacuation only if the internal pass has no result; those are sequential fallback stages, not one combined normalized candidate pool.

Current candidate-pool completeness is unresolved because the live neighbor set, typed actor/origin targets, cohort history array, pool mode, current owner/controller map, route and hazard proofs, current policy/capacity values, and all scoped dynamic weights were not bound by the current MCP call. The probability inspector cannot receive a fabricated static list as a substitute for that scenario state.

### Famine relief donor selection

Sources: common/scripted_effects/famine_relief_effects.txt, common/scripted_triggers/famine_relief_triggers.txt, and common/script_constants/famine_relief_constants.txt.

The live donor candidates come from global.famine_relief_registered_donor_states, a dynamic sparse registry populated by explicit owner wiring. The donor is valid only after route and relation checks, a valid recipient and actor, a requested amount at least the minimum grant, recipient reserve headroom, donor reserve above the protected floor, and exact route-mode endpoint proof.

Weights begin at 10. The selected land/sea/air route adds 20/12/10. Relation adds 6 for positive opinion, 18 for ally, 14 for faction, 12 for subject, 8 for access, and 6 for guarantee. Matching ideology adds 6 and mismatch subtracts 3. Proven persecution and war-corridor overrides add 8 and 10. Donor stock surplus and recipient headroom each add a bounded increment up to 40. The final weight is clamped from 0 to 1000.

Selection is a two-pass weighted draw over the registry and fails with no candidate when the total is zero. Candidate registry membership is current and owner-driven; the complete live state list cannot be recovered from the inspected source constants alone. No donor share or top-ranked donor is certified here.

### Catastrophic-famine opposition selection

Sources: common/scripted_effects/famine_opposition_effects.txt, common/scripted_triggers/famine_opposition_triggers.txt, and common/script_constants/famine_opposition_constants.txt.

The source declares seven channels: four non-ruling political-party channels, local resistance, national autonomy, and project movement. Party candidates require positive current party support and cannot be the ruling government. Local resistance requires active, positive resistance. National autonomy requires a state core of the owner and owner autonomy_ratio above its sentinel. Project movement has no identified authority receipt in current common source and has both a failed authority predicate and fixed zero weight.

Party weights use support plus severity, responsibility, repression, and wartime context, with a base of 15 and a maximum of 400. Local resistance uses a base of 35, a 1.5 resistance scale, a 50 proven-resistance bonus, and the shared severity/responsibility/repression inputs. National autonomy uses a base of 20, a context bonus of 20, and the shared severity/responsibility/repression inputs. The random_list selects among these variable weights; it is probability-proportional-to-weight sampling, not an ai_will_do score race.

Resolution is gated by a valid state, active catastrophic famine, active extraction, positive extraction responsibility, famine score at least the catastrophic threshold, and no prior resolution during the same catastrophic stage. The recorded date is the stage start date, so a later recovery and re-entry to catastrophic stage can allow another resolution. If all channel weights are zero, the selector fails closed, but the general stability/blame consequence still executes. Repetition rate and repeated-channel behavior across separate stage entries remain unresolved.

The current source threshold is constant:famine_food_score.catastrophic_threshold; the parent-provided source audit identifies it as 100, equal to the score formula maximum. This makes reachability and opposition activation boundary scenarios essential. A proposed threshold change in the planning package remains unresolved design, not an accepted tuning target.

### Sparse timing and pacing

The shared host-only coordinator is called from the existing daily on_daily action. humanitarian_process_registered_runtime iterates sparse registries for famine profile anchors, famine active states, migration active states, migration reception candidates, active migration countries, and registered relief donors. State control, war, peace, and nuclear callbacks mark or invalidate affected records. The subsystem loop is registry-bounded rather than a new famine/migration every-country candidate scan; it still revisits active registered rows on the daily host pulse.

Deterministic timing constants in the current sources are:

| Surface | Current source values |
| --- | --- |
| Famine decision removal durations | 14, 18, 21, 28, 30, and 35 days. |
| Famine decision re-enable intervals | 45, 60, 75, and 90 days. |
| Famine mission timing | Repair-route timeout 150 days; deliver-relief timeout 110 days; route hold 14 days; evacuation protection 10 days; relief observation 7 days. |
| Migration decision removal durations | 10, 14, 18, 21, 28, 30, 35, and 45 days. |
| Migration decision re-enable intervals | 45, 60, 75, 90, and 120 days. |
| Migration mission timing | Secure-corridor timeout 120 days; evacuation-protection timeout 100; reception timeout 150; return timeout 180; evacuation protection 10; reception and return observations 30 days. |
| Humanitarian corridor | Offer response 10 days; response decision 3 days; response re-enable 1 day; pulse cooldown 1 day; mission hold 90 days. |

These are deterministic deadlines, cooldowns, decision timers, and scheduler cadence, not MTTH timing distributions. The inspected source set has no event ai_chance pool or event MTTH entry. The ai_will_do blocks use MTTH block syntax for scores, but there is no mtth: variable entry here whose value is an event firing-time distribution.

## Candidate completeness and future scenario fixtures

All scenario IDs below are intended for a fresh future audit after a responsive probability_inspect. None has a current result from this subtask. The named source has no current scenario hash or artifact for them, so their classification is unresolved.

| Scenario ID | Surface and required complete inputs | Candidate/external-factor status now |
| --- | --- | --- |
| fm03_severity_reachability | Famine decisions and catastrophic opposition at strain, acute, famine, catastrophic-entry, recovery, and threshold-boundary dates; bind all famine components, score maximum, reserve/capacity, access, exposure, extraction responsibility, stage start date, and current extraction and opposition receipts. | Candidate declarations are source-visible; typed state and threshold scenario unresolved. |
| fm06_route_modes | Famine relief and route repair for land, sea, and air; bind one typed recipient state and actor, every actual registered donor state, ownership/control, stock/capacity, exact endpoint/route proofs, route damage, blockade, diplomacy/war, and action cost inventory. | Dynamic donor pool and route fixture incomplete. |
| fm07_blockade_response | Relief convoy, emergency airlift, route repair, donor selection, and any valid corridor response under open-route, damaged-route, and blocked-island cases; supply scheduled restoration/damage changes and actual logistics stocks. | Dynamic routes and donor list incomplete. |
| fm08_extraction_correction | famine_maintain_extraction versus all simultaneously available famine relief, concealment, and mitigation decisions; bind extraction and governance components, stage, pressure, war, government, stock, target state, and all PP/equipment/fuel/convoy affordability gates. | Ten declared famine score candidates are source-complete; scenario eligibility and score evaluation unresolved. |
| fm09_service_affordability | Current famine and migration decisions under scarce and sufficient political power, convoys, trains, support equipment, aircraft, fuel, and reserve stocks; include the parent-identified land-import ten-convoy cost in its actual source path. | Score-source declarations are known; live stock and custom-cost gates are unbound. |
| fm11_parallel_offer | Corridor accept versus reject under humanitarian-open/controlled/closed reception, democratic/authoritarian government, requester at peace/war, valid/expired offer, and route/capacity change before response. | Response pair is source-visible; pending-offer typed scopes and complete active response pool unresolved. |
| fm12_host_overload | Open reception, controlled medical reception, distribution, transit, closure, and integration under spare/near-full/exhausted capacity, war/peace, and demand changes. Bind country and target state loads, capacities, exposure receipts, routes, policy, costs, and phase flags. | Eighteen declared migration score candidates are source-complete; live eligible pool and input completeness unresolved. |
| fm13_exposed_reception | Controlled medical reception versus open reception, closure, transit, or distribution with and without valid exposure receipts, persecution, and spare capacity. Bind owner/controller, load/capacity, cohort, receipt generation, ideology, war, and exact route. | Typed cohort and receipt state unresolved. |
| fm14_destination_safety | Every actual adjacent candidate under internal-safe, foreign-safe, transit, and third-country pools, including unsafe-state exclusions, safe-state alternatives, relation and capacity differences, history exclusions, and internal-first fallback. | Pool types are declared; candidate states and scoped modifiers incomplete. |
| fm16_durable_choice | Local integration, voluntary return, forced repatriation, and third-country resettlement with safe/unsafe origin, persecution, capacity, policy, trapped status, war, government, and exact cohort history. Include the zero-factor trapped-target case. | Decision candidates are source-visible; exact origin/host targets and eligibility unresolved. |
| fm22_term_renewal | Decision timers, mission deadlines, daily sparse processing, offer pulse, recovery, route loss, capacity change, expiration, and re-entry across explicit dates. | Current timing values are deterministic; no complete declared state-transition fixture or MTTH distribution. |

The older named scenarios remain useful labels for a refreshed matrix: prob_famine_relief_dense, prob_famine_relief_blocked_island, prob_soviet_extraction, prob_requisition_donor, prob_humanitarian_border, prob_capacity_exhausted_border, prob_outbreak_reception, prob_nuclear_evacuation, prob_genocide_escape, prob_authoritarian_pushback, prob_destination_selection_internal, prob_destination_selection_persecution, prob_corridor_acceptance, prob_forced_return, prob_integration, prob_opposition_channel, and prob_relief_donor. The prior artifacts for those names are historical partial results, not current certification.

## Historical MCP provenance from ai_probability_current.md

These artifacts were already recorded in the dated 2026-08-26 report. Their references are preserved here for provenance only.

| Historical analysis | Source/scenario evidence | Artifact and limitation |
| --- | --- | --- |
| Famine flat-fact matrix, probability-ee3074ce9bf0db80f330bf06 | Scenario hash 638129d61ba378c2ecf61a438d17216d7a2dc976dcbd2e3e92b5e552e99fca6e; MCP source hash 729c115b88697b86b2e70988fc1b093361a9220c673a94f2451b68f7613a5e74; 4 scenarios, 40 rows, 15 unresolved. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e860826d78756ed13c6c7e608cb2778834fae16206807e319e4892bca3e23f2d/339223bb1fe22ee11a649ed0e6ae3417667561d1ec0eaa172215868d8d1c2cc8/probability-ee3074ce9bf0db80f330bf06.json |
| Migration flat-fact matrix, probability-967ff4fb246a0c8c86c5eeb4 | Scenario hash 8c8eb15e528b68603c943cfcf1b47708c56bd1e792b95059293dd62c1aa1da23; MCP source hash 84fa372dc07e66a1b07c299486834ce3112db3b03b8ecae2e8ca2022f014665a; 11 scenarios, 198 rows, 60 unresolved. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95f14549a35b5e562b9bb71d9ccd9255232396329e62f6080eaabc8d722260e7/049cb1d0bc519eda59b00e99c4af4c59c8f7c93aaa0b3d3afd1bf7a56953d6ec/probability-967ff4fb246a0c8c86c5eeb4.json |
| Famine decision inspect | Historical adapter mission_ai_will_do; source revision 7caa56bc69922e4ac74e494d19a279b8816aa78eee4be8be7a7052187e98f579; MCP source hash 729c115b88697b86b2e70988fc1b093361a9220c673a94f2451b68f7613a5e74; 10 declared candidates and 6 required inputs. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acd719d701e14b9e6b0c1c7b09f887386c7c4e65674f6052b698e5328fdd8aa0/7b911a370582d4a26ad301091bd644afda08efb62b1b52ef2161bbdf9656fb0e/probability-inspect-729c115b8869.json |
| Migration decision inspect | Historical MCP source hash 84fa372dc07e66a1b07c299486834ce3112db3b03b8ecae2e8ca2022f014665a; 18 declared candidates and 11 required inputs. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/606987e49cdca6e1b873ad1475cf70184f31259343d40fd89b243358a5c5056b/6a152f721c5f863384eb887b619ea2e9a6ec25a77209e582a74c74e02801f12f/probability-inspect-84fa372dc07e.json |
| Destination selector inspect | Historical source hash 8169d9fb45fde0b399097d3f252c64fe6be7ba7e21a1e5952531ea8b34ddc65d; four pool modes found, dynamic neighbors not discovered. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a96188c86331f555ef4b3f706f85901555ec6e1f49b823694cc61e6599a7a368/2767d7dd3053467a2d425326ee7de011247498bd0dd14e7415ab86e4d41a82f2/probability-inspect-8169d9fb45fd.json |
| Opposition pool inspect | Historical source hash 4040a2f554f24521026236dad3316f209169a510b184103f4b81b1b437f1f22e; seven channels identified, but the analyzer marked the pool incomplete. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69af1b8f8a18e350c14441c83bf37f47fa586d71efd6d103480ecf042b7d81bf/de9d458d8f21ab38d486f7b0e6837dbfd4acb99d7e1add93d4f08a39bce2f219/probability-inspect-4040a2f554f2.json |
| Relief donor inspect | Historical source hash 7ea4b17392347739c4cb1630752666624bb8f489d2c8aeba915c80d29f060a8; zero dynamic candidates were discovered and the registry was incomplete. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/38cc7f020663eaaa50b9d75603e6087e82cb7af6951d11a5829cd01e93ec4cd6/9fca70e4816ea62de5ca83d6646863f5696601db546f7f6644b48a13b6e88b5a/probability-inspect-7ea4b1739234.json |
| Famine before/current comparison | Historical analysis probability-4afd69e0e79bd79eefce0d1a; scenario hash 90ebda36ce4ae460b3dd64cbefdb6ae5d5ae4f8deadf0da15828cfec35a13739; comparisonChanges 0; 46 unresolved. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ee35ac8f350bc2e820ac4e71ba492777a718644d576f6d84ad48eec3e1a1746/d989f58eebde25a1a880569a5c8bb072ad9a291ec76bef52f6f6f25b107a856c/probability-4afd69e0e79bd79eefce0d1a.json |
| Migration before/current comparison | Historical analysis probability-35fd3b50d64d8a2cbbed5af4; scenario hash d0e5281c91db132e22ea8cfa0c4d9373bbe197d251859451641995bc87b43b26; comparisonChanges 6, 134 unresolved, 4 information diagnostics. The six changes were two corridor modifier rows repeated across three scenarios, not six decision or balance changes. | hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e18aeed48d51f13834da02e62224082ea671580383a588d501179eb5c3f7b1a/7a2916fce9cb62258856d61c7e7ff5517c423a9ea95ef08259521beb05219349/probability-35fd3b50d64d8a2cbbed5af4.json |

The historical report also records typed-scope probes in which a schema-accepted FROM binding still did not resolve the special target or compound hidden trigger. Historical evaluation artifacts were partial score traces with empty state fixtures. No historical probability_render image or standalone rendered path was identified in that report.

The current local decision-file hashes prove those old artifacts are not bound to today’s decision files: famine decisions are now 52e84b51b6c9faf5827f3152613870e4ebbd65215edd35d70e913d18ba01dfaa, while the older report records bb8d664fb7aac3dff93321b2abc25999f8441d5760979d851b041931df4d12a2; migration decisions are now 279487dc7f2fcef921f7294fd207ba8c1c33f871c652280ebb31d2d1fd2a3e8b, while the older report records 6cfad3a2ba346576e012313f0ac0efcb9f120b8250c40f489ad0f627faedf1a6.

## Audit-time source inventory

These are local SHA-256 values from the named current working-tree files, not HOI4 MCP source revisions.

| Source | SHA-256 |
| --- | --- |
| common/decisions/famine_decisions.txt | 52e84b51b6c9faf5827f3152613870e4ebbd65215edd35d70e913d18ba01dfaa |
| common/decisions/migration_decisions.txt | 279487dc7f2fcef921f7294fd207ba8c1c33f871c652280ebb31d2d1fd2a3e8b |
| common/script_constants/famine_decision_constants.txt | 32e53d81dedae55852b3fd2ec4f81889e41e1eec471d04255f9877b45b20cb4c |
| common/script_constants/famine_mission_constants.txt | e80342e694c16664d45f1084b378caafeed4f31e779cd619f753141007b96dc3 |
| common/script_constants/migration_decision_constants.txt | 48c0cbc35ad6e98e2fac0a4cb5a499dfa71cb06f5b7adb484a1d05b47e33f9ce |
| common/script_constants/migration_mission_constants.txt | 5071066c2124ac11a779e20f0d0540fabef181745263a20327cc11b00a20a1ab |
| common/script_constants/migration_destination_selection_constants.txt | 2c80a0632b6e14f8b6b855abe74ee90d5c81ee314c108d49c33c9eef2623b38e |
| common/script_constants/famine_relief_constants.txt | caaa63c52ea7765d65392a2f3d96ae98a5daeb4981d469822200c0e64883ca41 |
| common/script_constants/famine_opposition_constants.txt | 64036542ebeb6c9814351c11203bb2c60ccde65b2e658f31e6246ae705910067 |
| common/script_constants/humanitarian_runtime_constants.txt | ecc9268eeb56755c10767ef5c622758d8adcd67195aa17e75e0bad9a0f3f8a7a |
| common/script_constants/humanitarian_corridor_constants.txt | 12b774d71734564e8d423bfe68b401e37adfd73c801b1b3fa9efaae0e25c0aab |
| common/scripted_effects/migration_destination_selection_effects.txt | f20084bf1fe1b12a885710b0a3e081e251f3aefd3505aca4c65925421caeb9ff |
| common/scripted_effects/famine_relief_effects.txt | 571c9a3bcc299cf67a0a32f1844859d226137c4e434026a7e9ab899e733b2959 |
| common/scripted_effects/famine_opposition_effects.txt | b7b95475b8c3ff22a2847304126754580a7ac0946ead18063bf34577f68a8578 |
| common/scripted_effects/humanitarian_corridor_effects.txt | c56c3c656468e8174078f2e0403f06523c7c5817d0049a4f98dfd77b8db11ee7 |
| common/scripted_effects/humanitarian_runtime_effects.txt | b2f9ed887955d4ac7ae71d6bc2140c0d07c4948a0c86dd5f1bd462b8aaa740bc |

Supporting current source spans include the famine and migration ai_will_do blocks above; destination selector logic at migration_destination_selection_effects lines 316-446 and candidate trigger at migration_destination_selection_triggers line 191; relief weights and selector at famine_relief_effects lines 113-323 and donor candidate trigger at famine_relief_triggers line 525; opposition validity and channel resolution at famine_opposition_triggers lines 9-99 and famine_opposition_effects lines 271-301; corridor response scores in migration_decisions lines 1209-1239; daily sparse processing in humanitarian_runtime_effects lines 35-70 and the shared daily coordinator in common/on_actions/chaosx_on_actions_chaos_meter.txt.

## Reference review

The offline wiki was read directly from local files because no live reference retrieval was used during this bounded audit.

- paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md, lines 25-73: MTTH block ordering; ai_will_do generates score values and an AI score race, while ai_chance and random_list use probability-proportional sampling.
- paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md, lines 357-385: decision ai_will_do uses MTTH block syntax; decision visibility/availability, targeted scopes, and fixed-seed notes are distinct inputs.
- paradox_wiki/Effects - Hearts of Iron 4 Wiki.md, lines 4510-4550: random_list entries are relative weights normalized over their sum, and variable weights are supported.

Installed documentation read directly:

- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md, lines 5413-5432: random_list accepts a variable weight in the current scope.
- C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md, lines 216-242: script-constant visibility, constant references, and fixed-point semantics.

The installed documentation inventory exposed no decision-specific ai_will_do or decision-selection scoring section. No reference_context, reference_search, reference_read, or source_lookup result was obtained for this subtask. No web sources were used.

## Recommendations and skipped analyses

- Keep every proposed balance change unresolved until its owner accepts an intended outcome. The source review does not select a target score.
- Before any future weighted change, freeze the exact old source bytes and custom pool manifest outside runtime-loaded folders, save their paths and SHA-256 hashes, and preserve the named scenario fixture.
- Re-run probability_inspect for each current source or declared custom pool. Then evaluate complete named fixtures, sweep sensitivity/rank reversals, and render the ranking/matrix/unresolved view where it helps review.
- For a later weight, probability, or timing patch, run probability_compare on the exact old and new paths under the same saved scenarioSet. Do not compare the current file to itself or treat a stale analysis artifact as the old source.
- Do not request probability_sequence until a complete manifest declares candidates, cadence, recovery, cooldown, cap, removal, reset, timer changes, state transitions, and terminal states. Do not convert deterministic sparse registry cleanup into a random pool.
- Use probability_simulate only after uncertain inputs have explicit distributions, seeds, sample counts, and confidence reporting.
- The current hidden and compound trigger inputs, typed FROM/event-target scopes, dynamic neighbor list, registered donor state list, and active offer/host set remain unresolved. Candidate overrides cannot stand in for live state proof.
- A source scan found no current positive weight on the deliberately dead project_movement opposition channel; its proof is false and weight is zero. This does not establish completeness of the other six eligible-state weights.
- The current source caps weighted values and fails closed on empty destination and donor pools, which reduces fabricated-fallback risk. It does not certify starvation, dominance, route safety, or exact normalized shares.
- The parent-provided A01-A04 findings remain source findings from the surrounding plan and do not become numeric probability evidence here: A01 proof-one capacity-setter rejection needs a typed availability/receipt fixture; A02 the catastrophic threshold at the weighted formula maximum needs a boundary and stage-entry fixture; A03 railway-repair score cases must model actual physical route restoration rather than assume that clearing the projection restores access; A04 land-import score cases must include the stated ten-convoy affordability cost.
- No current rendered evidence exists for this attempt. No gameplay patch, before/after comparison, or balance target was produced.
