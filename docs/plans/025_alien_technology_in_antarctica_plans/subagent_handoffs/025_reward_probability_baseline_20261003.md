# Event025 external reward API probability baseline

**Disposition: blocked for probability conclusions.** The source baseline and scenario meanings are preserved, but the mandatory HOI4 MCP probability routes were not callable in this session. The source observations below are not MCP evidence and do not establish normalized probabilities, balance, or runtime behavior.

## Audited surface and owner boundary

The bounded surface is `chaosx_grant_external_alien_recovery_reward` in `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt`, its base candidate helper `chaosx_grant_random_custom_operational_technology`, its upgrade candidates gated by `chaosx_custom_technology_upgrade_is_eligible`, and the Event025/Event036 request bridge in `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt`.

The matching candidate definitions are in `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt` and `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt`. Event025 derives its exact overlap input in `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt`, using `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt` and `common/script_constants/025_alien_technology_in_antarctica_constants.txt`. The current Event036 caller is `events/036_alien_spacecraft.txt`.

No Event025 scenario, event-option, MTTH, focus, decision, technology-selection, or whole-event AI surface outside this owner API and its two ledger callers was audited.

## Live MCP status

Workspace ID: `mod_chaos_redux_ea3b2d67c2c0`.

I started with `hoi4.probability_inspect` for adapter `custom_weighted_pool` and source `{ path: "common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt" }`. The tool returned the exact error `MCP tool hoi4_agent_tools/hoi4.probability_inspect is not available to the model`.

The narrower retry used the owner source `{ path: "common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt" }` and the same workspace ID. It returned `TypeError: tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function`.

The live `ALL_TOOLS` metadata listed schemas for `probability_inspect`, `probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_render`, `probability_sequence`, `probability_simulate`, `event_inspect`, `event_render`, `reference_context`, `reference_search`, `reference_read`, and `source_lookup`. In the callable namespace, every one of those methods checked for this audit was `undefined`. The listed schema metadata therefore did not provide callable MCP evidence.

`hoi4.reference_context` was also attempted and returned `TypeError: tools.mcp__hoi4_agent_tools__hoi4_reference_context is not a function`. Reference search/read, source lookup, event inspection, event rendering, `tech_inspect`, and `tech_render` were unavailable in the callable namespace. No technology inspector or renderer entry appeared in `ALL_TOOLS` metadata. I read the applicable local references and exact technology/equipment definitions directly as the repository fallback, but they do not replace MCP evidence.

No MCP artifact URI, source revision, analyzer scenario hash, comparison ID, or rendered evidence URI exists for this audit. No probability evaluation, sweep, sequence, simulation, rendering, or comparison result was produced. The parent-supplied scenario IDs are preserved in [scenario_contract.md](C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/025_reward_probability_baseline_20261003_evidence/scenario_contract.md), but that document is a domain-state contract, not a tool-accepted scenario set or scenario hash.

The required adapters are the custom `random_list` selection in the owner API and, if the analyzer requires a manifest, `custom_weighted_pool`. The first inspection attempt selected `custom_weighted_pool`; the underlying helper uses `random_list`. The analyzer did not identify a candidate pool, resolve the source closure, or report `poolComplete`.

## Frozen source baseline

The byte-exact pre-patch copies are under `docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/025_reward_probability_baseline_20261003_evidence/source_baseline/`. Each copy matched its live source hash when copied. At final verification the owner API, owner candidate triggers/constants, Event025 ledger, Event025 triggers/constants, and Event036 event source still matched their snapshots. The Event025 runtime-effects file has since changed hash; the parent reports its intervening commit `aba406f93` contains physical-custody-only hunks. That file change is outside the owner API selection branch.

| Live source | Frozen SHA-256 |
| --- | --- |
| `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` | `4AA4CB9BAE94A76B8F33A5EA37F76E3C1AB040168FB688C7B9CD4A3C9EB6D3E1` |
| `common/scripted_triggers/016_brilliant_scientist_custom_technology_api_triggers.txt` | `EDE44BE51D047929E45DE9EDBF59D5064C98983E5A914C46F0D7FC31B58AA19B` |
| `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt` | `12F0D51FC9EC7ABF7C4F3CB8308AB94526B8992E3834C607D73C5942E508A26B` |
| `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt` | `91F55888298A54E2B711EFE1CA1AD4C2F122951D6121089E1DD637886C4692DE` |
| `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt` | `476D80940B972D7F719C666B340864661A40A79B4C2CB72ED187A92A7940CCA1` |
| `common/script_constants/025_alien_technology_in_antarctica_constants.txt` | `8B11BD0C3509F386A3B9CD96B41BF21D1C0360C496D2922C288501BD41FF074E` |
| `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt` | Frozen: `D6FA4C264051E8A4A14DF379B40F21F49CC664799D99FDBAD3A21EDDDAE996CA`; current: `8A0A3229959D191348A948DC2ACE00474476377784F7613FE52F0B43EB44D9AF` |
| `common/technologies/016_brilliant_scientist_project_technologies.txt` | `60BF2225FA86B235EE30898A9B1D19383D6D89AF72613764FD1A72D75AE7548E` |
| `common/technologies/016_brilliant_scientist_project_force_technologies.txt` | `8B0129A6B71FFCB5AD5D4EF354329D3ED10B18919D0849922A52763049F3F1D0` |
| `common/units/016_brilliant_scientist_project_forces.txt` | `FD0DF90E8C27DB087E7DF09BA8E325F3AE887A80B673677179D0FD5403489357` |
| `events/036_alien_spacecraft.txt` | `6531D27F883458F3D5E874CBEF1C01A197D23D101C57CAA2FC38D35567A69C73` |

The current repository HEAD at final verification was `33a6c622afa1ee09fad8aec463b5880f241025d4`. `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt` and `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt` remain dirty in the shared worktree, and their live bytes match the frozen baseline. The Event016 owner API has SHA-256 `4AA4CB9BAE94A76B8F33A5EA37F76E3C1AB040168FB688C7B9CD4A3C9EB6D3E1` both live and frozen, confirming the parent update that the API remains unpatched. The parent also reports commits `aba406f93` for physical custody, `0df226b14` for the report alias, and `33a6c622` for pulse settings. The latter changes did not change the owner API or the frozen reward bridge sources listed above.

The documentation source named in the request as an Event025 `specs/011 technology contract` is not present under the live package. The current `specs/011` file is `011_achievements.md`. The accepted reward contract used here is in `specs/006_outcomes_rewards_and_aftermath.md` and `specs/013_implementation_architecture.md`, together with `matrices/025_reward_arbitration_matrix.md` and `specs/014_acceptance_criteria.md`.

## Source observations, not MCP results

The base helper at `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:523` builds seven candidates: `portal`, `clone`, `robot`, `paleogenetic`, `xenobiological`, `alien_infantry`, and `temporal`. It initializes the temporary result marker and each candidate weight to zero, then assigns the same `chaosx_custom_technology_tuning.random_candidate_weight` to every unowned family. The current constant is `1` at `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt:87`.

The owner API starts at `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:639`. When `chaosx_external_alien_recovery_exclude_overlap` is set, the condition at line 681 skips the entire base helper. The API does not filter only the overlapping family. It then tries its eleven upgrade candidates, each with the same raw weight `1` when `chaosx_custom_technology_upgrade_is_eligible` passes, and applies Alien Systems Integration when no upgrade is selected.

The Event025 ledger preparer sets or clears `chaosx_external_alien_recovery_exclude_overlap` based on whether the requested overlap is above zero at lines 74-115. It also stores `chaosx_external_alien_recovery_allow_base` at line 101, but the owner API has no read of that variable. Event025 sets the request to allow bases by default at line 325, then sets it to zero for any overlap at line 336. Event036 overlap conversion also sets it to zero at line 490. The current owner API uses the broad country flag instead of this per-request input.

The parent’s explicit intent requires the Event025-after-Event036 route to keep the base tier available, then try an eligible upgrade, then Integration. The current positive-overlap flag suppresses the whole base tier. The owner code maps `portal` to the broad `aircraft` result label and `temporal` to `propulsion`, but that mapping alone does not prove an exact duplicate with Event036. The candidate to exclude therefore remains unresolved until an exact technology/equipment ID mapping is accepted. Preserve the separate Event036-after-Event025 request of zero if the accepted upgrade-only conversion contract remains in force, while describing it as a broad-field conversion gate rather than proof of identical IDs.

The overlap scenario is country-scoped. `chaosx_nr25_apply_winner_settlement` derives an aircraft or propulsion broad-field match from same-country Event036 ledger flags at the current `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt:2812` branch. The owner API maps its `portal` result to `aircraft` at lines 694-695 and `temporal` to `propulsion` at line 696. The Event016 tech definitions show that portal technology enables `teleportation_equipment_1` and the `portal_raider` land consumer at `common/technologies/016_brilliant_scientist_project_technologies.txt:37-48`, while temporal technology enables `temporal_guard_equipment_1` and `temporal_guard` at lines 172-182. Their force upgrades act on `portal_raider` and `temporal_guard` at `common/technologies/016_brilliant_scientist_project_force_technologies.txt:36-46` and `:121-132`, and both sub-unit definitions are land consumers in `common/units/016_brilliant_scientist_project_forces.txt:112-117` and `:322-327`. Event036 instead grants `jet_fighter1`, `jet_fighter2`, and `jet_fighter_equipment_2` at `events/036_alien_spacecraft.txt:56-62`. These broad labels do not establish identical tech or equipment IDs. The current Event036 representation also cannot express simultaneous aircraft and propulsion fields in one receipt.

The suspected stale base-helper output is not reproduced in the two current ledger callers. The preparer resets `chaosx_custom_technology_random_grant_applied` to zero at line 85 before calling the owner API, and the random base helper resets it again at line 524 when called. Event025 calls the preparer immediately before the API at line 349, and Event036 does the same at line 496. The owner API itself can skip the helper on overlap and does not independently reset that marker before reading it, so a direct caller that bypasses the preparer remains a robustness concern. The current bridge source does not establish a stale-marker failure.

The duplicate guards are source-specific. The Event025 ledger returns its existing receipt when `chaosx_alien_recovery_event025_recorded` is set. The Event016 owner API tracks the global consumed marker plus Event025 and Event036 consumed markers, allowing the separate event source a later reward while preventing a repeat from the same source in that country. This is source-level control flow only, not a simulated repetition result.

The helper has no AI score race, strategy factor, MTTH timing, or modifier trace. Its random lists use equal raw weights on eligible entries. I make no normalized share, exact selection probability, ranking, sensitivity, rank-reversal, timing, or sampled result claim. The source-level failure mode is whole-base-tier starvation under overlap. Candidate dominance among active entries and campaign-level repetition/exploit behavior remain unverified by MCP.

## Scenario completeness and classifications

The ten required IDs and their deterministic domain-state meanings are in [scenario_contract.md](C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/025_reward_probability_baseline_20261003_evidence/scenario_contract.md). Each declares the full seven-family base set and eleven-upgrade set through source eligibility rules, the source-event receipt state, ownership state, and applicable overlap. These declarations were not submitted to the analyzer. Analyzer candidate-pool completeness is unknown for every scenario, and external-factor completeness is unresolved for every scenario.

| Scenario ID | Source-declared pool state | Base/modifier trace from source | Probability result classification |
| --- | --- | --- | --- |
| `no_owned_bases` | Seven base families; no base-qualified upgrade. | All seven raw base weights receive the same constant when eligible. | Unresolved. |
| `one_owned_base` | Six base families; one compatible upgrade is also eligible by fixture. | Current source prioritizes the base helper before the upgrade pool. | Unresolved. |
| `overlap_aircraft_other_bases_missing` | Seven source candidates are declared. Which candidate, if any, duplicates the Event036 reward is not established by IDs. | Current source skips all seven because a positive broad-field overlap sets the country flag. | Unresolved. |
| `overlap_propulsion_other_bases_missing` | Seven source candidates are declared. Which candidate, if any, duplicates the Event036 reward is not established by IDs. | Current source skips all seven because a positive broad-field overlap sets the country flag. | Unresolved. |
| `overlap_both_other_bases_missing` | The intended fixture claims simultaneous aircraft and propulsion broad-field overlap. | The live scalar overlap contract cannot represent both fields in one receipt, and exact candidate IDs are unproven. | Unresolved and input-model blocked. |
| `all_bases_owned_upgrade_available` | No base candidate; one eligible upgrade. | The upgrade list uses the same raw constant for eligible entries. | Unresolved. |
| `all_bases_and_upgrades_owned` | No base or upgrade candidate. | The API selects the Integration idea or its already-owned reinforcement branch. | Unresolved. |
| `repeated_event025_receipt` | No random candidate pool is supposed to run on the second resolver call. | The stored result is exposed under the existing Event025 receipt flag. | Unresolved. |
| `event036_first` | Event036’s vanilla jet reward and aircraft broad-field receipt precede the Event025 owner call. | The Event025 overlap path currently skips the whole base pool. Exact identity between the jet IDs and any Event016 candidate is unproven. | Unresolved. |
| `event025_first` | Conditional first result is `portal`; later Event036 grants its vanilla jet reward and the ledger matches the broad `aircraft` label. | The later Event036 caller requests upgrade-only conversion. The label match does not prove an identical technology or equipment ID. | Unresolved. |

The only exact numeric source values available here are raw source weights and authored outcome values. They are not normalized probabilities. The Integration idea constants include research speed `0.06`, special-project speed `0.04`, and air attack `0.02`; if the Integration idea already exists, the API adds stability `0.02`. Those outcome values are recorded for traceability and were not balance-tested.

## Offline reference evidence

The reference MCP routes were not callable, so I read these local sections directly. Their hashes identify the local snapshots and are not MCP revisions.

| Reference | Relevant section | Local SHA-256 |
| --- | --- | --- |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | `Random effects`, lines 4504-4542, describes `random_list` values as relative weights rather than chances. | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | Line 431, variable values may be used as `random_list` weights. | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` | `random_list`, lines 5413-5422, says the effect is selected by associated weight and accepts a variable weight and optional seed. | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |

These references support the distinction between the source raw weights and resulting selection probability. They do not establish the active pool or its normalization for any named scenario.

## Validity, starvation, repetition, and exploit risk

Base-candidate validity is gated by current technology ownership and the Event016 operational/grant receipts. Upgrade validity additionally requires the corresponding operational base, an unowned upgrade, and compatible xenobiological-control state. The source declares seven base selectors and eleven upgrade selectors. The analyzer did not verify that closure or report impossible candidates. The candidate-to-Event036 exact-overlap mapping is also unresolved because the Event016 portal/temporal IDs and their land consumers differ from Event036’s vanilla jet IDs.

No source entry has a larger raw weight than another eligible entry, so no source-weight dominance is apparent. Equal raw weights do not prove equal normalized probabilities when the active pool is unresolved. Rank reversals and sensitivity are unmeasured. The overlap flag starves the entire base tier at the control-flow level even when other base families would be valid.

Repeated Event025 resolution returns its prior record, and owner API consumption is tracked separately for the two event sources. This limits same-source repeat grants per country in the inspected bridge. The existing-Integration stability reinforcement is reached only on another accepted source reward path, but campaign-level farming and multi-source balance remain unresolved without MCP scenarios.

## Recommended owner fixes, not applied

1. Keep selection logic in the Event016 owner API. Honor the per-request `allow_base` intent and overlap field instead of using `chaosx_external_alien_recovery_exclude_overlap` to suppress the whole base pool.
2. For an Event025 reward after Event036, keep base selection enabled as the parent requested and continue to the eligible-upgrade pool only when no valid base remains, then use Integration when both pools are empty. Define any member-level exclusion by matching actual technology/equipment IDs or by an explicit accepted broad-field policy. Do not infer that `portal` is aircraft or `temporal` is propulsion in the exact-ID sense from the result labels alone.
3. Preserve the Event036-after-Event025 upgrade-only request at `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt:490` if that remains the accepted event-order contract. Treat the current broad-field comparison as its declared policy input, not as proof that the vanilla jet package and an Event016 custom technology share an ID.
4. Resolve the current Event025 overlap request at `common/scripted_effects/025_alien_technology_in_antarctica_ledger_effects.txt:336`, which currently sets `allow_base` to zero, against the parent’s explicit base-first intent. The owner API currently ignores the stored `chaosx_external_alien_recovery_allow_base` value.
5. Initialize `chaosx_custom_technology_random_grant_applied` inside the owner API before any branch that might skip the base helper if the public API is expected to support direct callers without `chaosx_alien_recovery_ledger_prepare_api_request`. The two current ledger callers already reset the marker, so this is defensive rather than a reproduced bridge defect.
6. After the owner patch, update `docs/events/025_alien_technology_in_antarctica/overview.md:23` if its wording still implies every overlap goes directly to upgrades. Keep it aligned with `specs/006_outcomes_rewards_and_aftermath.md`, `matrices/025_reward_arbitration_matrix.md`, and the accepted source behavior.

## Compare handoff and remaining blockers

The baseline `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` copy is at `docs/plans/025_alien_technology_in_antarctica_plans/subagent_handoffs/025_reward_probability_baseline_20261003_evidence/source_baseline/016_brilliant_scientist_custom_technology_api_effects.txt`. The owner API's live SHA-256 still matches it. After a patch, the auditor must use the identical ten scenario IDs and the same domain inputs from `scenario_contract.md`, convert them through the then-live accepted schema, and preserve the analyzer-returned scenario hashes, source revisions, and artifact URIs.

For `probability_compare`, use the real frozen baseline source path and the real post-patch source path. If the patch changes both the Event016 owner file and the Event025 bridge, compare each changed weighted source under the same saved scenario set using the live schema. Do not use the current source as both before and after, and do not pass hashes or revisions inside source objects unless the live schema explicitly accepts them.

`probability_evaluate`, `probability_sweep`, `probability_compare`, `probability_render`, `event_inspect`, and `event_render` remain unrun because their callables were absent. `probability_simulate` was not appropriate because the parent did not declare uncertain inputs or seeds. `probability_sequence` was not run because the tool was absent and no analyzer-accepted complete sequence manifest was available. The `overlap_both_other_bases_missing` scenario remains unresolved until its intended two-field semantics are represented by an accepted source input.

No gameplay, event, AI, technology, localization, workbook, Git index, or runtime file was edited by this audit. The only new files are this handoff, the scenario contract, and byte-exact evidence copies in the authorized evidence folder.
