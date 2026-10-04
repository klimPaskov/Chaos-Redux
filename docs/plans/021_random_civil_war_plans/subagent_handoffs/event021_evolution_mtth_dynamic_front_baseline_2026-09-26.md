# Event 021 evolution MTTH dynamic-front baseline, 2026-09-26

Status: the read-only source audit is complete, but timing evaluation remains unresolved because the live probability inspector discovered no candidates in the requested MTTH source. This report does not establish balance or select a tuning target. No gameplay source was edited and no commit was made.

## Scope and source identity

The only weighted surface audited is the three evolution timing entries in `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\mtth\021_random_civil_war_mtth.txt`.

Immediately before the first probability MCP call, at `2026-09-26T08:41:00.0124408Z`, the source was copied byte-for-byte to `docs/plans/021_random_civil_war_plans/probability_snapshots/event021_evolution_mtth_pre_migration_2026-09-26/021_random_civil_war_mtth.txt`. The source and copy both measured 3,432 bytes and had SHA-256 `6A8C516E1A2625F3534995F6744ED373E5803AC981FD139EA95787F07B9EA71F`; the copy is marked read-only. A later recheck found the current source still has the same hash.

Repository `HEAD` at the later source-reference hash capture was `58c2ca89f6f0f4df07113dc88655a84432d3dfcf`. These raw-byte hashes identify the working-tree inputs and do not imply that the tree was otherwise clean.

At final status, the parent effects, core effects, lifecycle effects, parent triggers, and constants files were marked modified in Git, while the MTTH source was not. No initial Git status was captured, so the origin of those five working-tree modifications is uncertain. This audit did not write those gameplay files; the hashes above identify the exact contents reviewed.

| Current source reference | Length | Raw-byte SHA-256 |
| --- | ---: | --- |
| `common/mtth/021_random_civil_war_mtth.txt` | 3,432 | `6A8C516E1A2625F3534995F6744ED373E5803AC981FD139EA95787F07B9EA71F` |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | 415,853 | `0EC202D15D662BDD7DFFA494F02D1E18AD71D8CAEEED687DD0442E493A778A5B` |
| `common/scripted_effects/021_random_civil_war_effects.txt` | 102,880 | `97C36D6DF8C4A17E208C5508654F2123047F9947885F8D118EF3B8666E1323D0` |
| `common/scripted_effects/021_random_civil_war_lifecycle_effects.txt` | 42,173 | `D80BCDFAECAFECDAE05F2B7928E87E239A67410566A2589F33549C52D0BE090E` |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` | 40,679 | `3E518F2088239F4D739AE97FA23A6BF4793034ED389B215A6EE85A53476E4465` |
| `common/script_constants/021_random_civil_war_constants.txt` | 19,113 | `1525A8ED1D75CBCFF5983139F709A7511D4EE9418CF4B11B389057101AD348F9` |

The MCP probability artifact separately reports `sourceRevision = d7f19f06d85c8037d6f1682ef6bb5676cce1fe46245921253b71e4c225d7c7d5` and `sourceHash = c55a108bcbf249ce1d76875506cd0fe4b8c8db79646c426b503ba036d72405b8`. The artifact does not define this `sourceHash` as a raw-byte hash, so it is preserved as a separate MCP identifier and is not treated as equal to or conflicting with the local raw-byte SHA-256.

The earlier `event021_dynamicity_probability_baseline_2026-09-26.md` records the same MTTH raw hash, but its parent-effects, effects, lifecycle, parent-trigger, and constants hashes differ from the current hashes above. Its other MCP conclusions are historical and are not reused as current analysis.

## References consulted

The complete event-planning scenario-matrix fixture was read at `docs/plans/021_random_civil_war_plans/probability_snapshots/event021_dynamicity_recovered_expected_pre_edit_2026-09-26/scenario_matrix_fixture.md`. Its `EVO1-01` through `EVO3-02` rows are expected-direction descriptions, not a schema-valid `scenarioSet` or prior evaluated baseline.

The required offline wiki snapshots consulted were `Data structures`, `Triggers`, `Effects`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, and `AI modding` under `paradox_wiki\`. The MTTH-variable and AI-modding sections describe `base`, `add`, and `factor` operations and modifier-trigger scope. The Event modding section describes native event `mean_time_to_happen` checks. Those native event checks are distinct from the use of `mtth:` values as scripted due-date delays described below.

The installed vanilla documentation consulted includes `documentation\script_concept_documentation.md`, `documentation\triggers_documentation.md`, `documentation\dynamic_variables_documentation.md`, `documentation\effects_documentation.md`, and `documentation\modifiers_documentation.md`. The trigger and dynamic-variable references document `any_neighbor_country`, `has_stability`, `num_of_controlled_states`, and `surrender_progress`. A search across the installed Markdown documentation for `MTTH`, `mtth:`, and `mean_time_to_happen` returned no matches, so the offline wiki supplies the available direct MTTH explanation.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, and `chaos-redux-event-planning`. No skill was created or changed.

## MCP evidence and route status

The required first audit call was `hoi4.probability_inspect` with adapter `event_mean_time_to_happen`, source `{ path: "common/mtth/021_random_civil_war_mtth.txt" }`, and `refresh: true`. The live route returned status `ok`, code `PROBABILITY_SOURCE_DISCOVERED`, workspace `mod_chaos_redux_ea3b2d67c2c0`, and `filesScanned = ["mod:common/mtth/021_random_civil_war_mtth.txt"]`.

The inspection result was `discoveryReason = no_weighted_surfaces`, `availableAdapters = []`, `candidates = 0`, `availableCandidates = 0`, `requiredInputs = 0`, and `unresolved = 0`. Those zero input and unresolved counts are not evidence that campaign inputs are complete. With no recognized candidate, the analyzer enumerated no conditions or required fixture inputs. The route is connected, but this source and adapter combination did not expose an evaluable candidate.

Probability-inspect artifact URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f786cb00c9c7411a7492c1a3ceead80eda705c15c14296561105460697f3cbe1/fd0d1e81f314471967e396596698023aa925376b7ecf610c0867519339b5c628/probability-inspect-c55a108bcbf2.json`.

No `probability_evaluate` or `probability_sweep` was run because inspection yielded no candidate to evaluate and the required typed state and scope values were not fixtureable. No `probability_simulate` was run because no uncertain-input distribution or seed was declared. No `probability_sequence` applies because these are not a declared custom weighted pool with cadence and transitions. No `probability_compare` applies to this pre-migration baseline because there is no post-change source and no successful baseline `scenarioSet`. No probability analysis ID was created, so `probability_render` could not render an evaluated timing or unresolved view.

The read-only structural route was also used for the evolution callback IDs `chaosx.nr21.11`, `chaosx.nr21.12`, and `chaosx.nr21.13`. Each `hoi4.event_inspect` trace returned `EVENT_INSPECTED_PARTIAL` under graph revision `02aadd003a66d42965ee451ee17108816105638af9ec6f0a31e9ffaa4138eafb` and graph hash `65d862ddd1a7893bfede856be54280246099dc7c95c67203da75673e889a9695`. The focused route reports 9,836 events, 15,185 options, 1,171 entries, zero helpers, 8,910 unresolved nodes, 7,762 terminals, 38,556 edges, 2,193 diagnostics, and zero blocking diagnostics. Its coverage validation says workspace-wide helper projections and lifecycle passes were deferred. The inline file inventory is limited to 64 of 384 source-hash entries.

Trace artifact URIs:

- `chaosx.nr21.11`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18afe79350d6440a08e455031c7ac31b0dc59c63b948f9bddfac0b532fab484f/a5ab9d4980f355d135c5f25e08cc7437516df5ec43ced536ca41c3c6c0bb89d0/event-trace-02aadd003a66.json`
- `chaosx.nr21.12`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5db6aa1f386648fb8e7c8f5c47fb1e17708ba33e4cd3f9fd1675f007af0fb04f/8594735334c9f39ed67eddf6da0cb70ba3de9f1a8bc84690e9a972de4f1ffa65/event-trace-02aadd003a66.json`
- `chaosx.nr21.13`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d90f04abb566fb5914d17399a0d27b3dc4ba481e924301f14db0097fcec807b/2ff2c902037b35d0ed8813c4fd82545a3cd9d65ddb4301701ba147bb83c477b1/event-trace-02aadd003a66.json`

`hoi4.event_render` was run with timing view. The direct `chaosx.nr21.11` selector produced zero selected nodes and zero branch renders, so that view does not prove the three callbacks' graph paths. A namespace render for `chaosx.nr21` selected 40 entry nodes and omitted 42,824 nodes, with zero branch renders and `complete = false`. The namespace render's selected entries did not include any of the three callback IDs. This is retained as partial structural evidence only.

Direct timing-render manifest URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e869cf8b8772316618b53fec6f52619defa2ba073ec2bf9b46c8387862e408c7/6f48c1603396ebf4afe22e20d52b2430b1b304f30f0e346b2034b9c70b0b7c8c/event-timing-02aadd003a66-manifest.json`.

Namespace timing-render artifacts:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/620878f4f8ab1976cba623763c137d8bb999cb0401457119f14ec69f62db6957/b55651026960483f1a1ab637ece863f0b65eb4f0ad2f0712fb540baf23b3deea/event-timing-02aadd003a66-manifest.json`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/241188d3b096515b80c28fff364e6c24826368ec071a19e412e0fbb5d73747ec/4d3bd6521a5e2b0dd8faa482553a230f401a7f6d3412e5c2a81549e5cfa7e896/event-timing-02aadd003a66.json`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f904c56d1cbba3ba15707d460afa8288946548322c6c458f2948761b3799a5ca/702590675cf253eae9d86d4937b3df724ccbc1b5a918de04bf8a468a6344ea45/event-timing-02aadd003a66.svg`
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b58c86d8c7a7e21b8e50ca06230d7c6e422b62725e4f5d1f21fed8bb68cfb090/f2cabac2ebfd78f066cee4729e304616782d38116e067e5f1f74e05657a1954e/event-timing-02aadd003a66.png`

The namespace timing JSON was declared as a 213,620-byte JSON artifact. A first oversized resource read was truncated by transport and rejected. The artifact was then retrieved and decoded in 18 verified byte ranges: offsets `0, 12000, 24000, 36000, 48000, 60000, 72000, 84000, 96000, 108000, 120000, 132000, 144000, 156000, 168000, 180000, 192000, 204000`; each range was 12,000 bytes except the final range at offset 204,000, which was 9,620 bytes. The reconstructed payload matched the declared total length and parsed as JSON. Its `complete = false` status describes incomplete graph analysis, not an incomplete byte read.

## Scheduling semantics from the named source files

The three `common/mtth` blocks are not attached as native event `mean_time_to_happen` clauses in the reviewed call sites. `event021_parent_schedule_evolution_due_date` assigns each `mtth:` result to `event021_evolution_delay_days`, clamps it to the shared 60-to-180-day bounds, sets the corresponding `global.random_civil_war_evolution_*_due_date` to `global.date`, and adds the delay. `event021_parent_process_evolution_schedule` creates a due date only when the stage is unlocked, unrecorded, and has no existing due-date variable, then fires `chaosx.nr21.11`, `.12`, or `.13` once the stored date is reached.

Before `random_civil_war_has_committed_opening` is set, the same process fires the relevant callback immediately and clears that stage's due-date variable. That pre-fire path bypasses the computed delay. Therefore these entries currently feed a bounded scheduled delay, not a normalized selection probability or a native event's daily MTTH hazard. No stochastic timing distribution is claimed.

For a scheduled stage, `event021_parent_select_evolution_mtth_actor` scans `global.random_civil_war_active_theaters` and saves the first scope passing `event021_parent_active_front_side`. The MTTH value is evaluated in that selected actor's country scope. If no actor target was selected, the value is evaluated in the scheduler host's country scope. This is an ordered first-match context choice, not a weighted candidate race. The exact live theater array, active-side order, and state values were not supplied to MCP.

The modifier blocks use positive fixed-point factors centralized under `random_civil_war_evolution_mtth` in `common/script_constants/021_random_civil_war_constants.txt`. Factors below 1 shorten the computed delay and factors above 1 lengthen it. The source results below are exact source facts; each scenario's computed delay remains unresolved.

### Evolution I: `random_civil_war_evolution_i_days`

Base: `evolution_i_base_days = 90`.

| Modifier condition | Named constant | Source factor | Delay effect |
| --- | --- | ---: | --- |
| `random_civil_war_authority_is_failing = yes` | `authority_failure_factor` | `0.75` | Shorter |
| `num_of_controlled_states > large_country_state_threshold`, where threshold is `8` | `large_country_factor` | `0.85` | Shorter |
| Any of `random_civil_war_secondary_front_active`, `random_civil_war_event6_route_ready`, or `random_civil_war_multifront_active` | `extra_actor_factor` | `0.75` | Shorter, once if any flag is true |
| `surrender_progress > near_defeat_threshold`, where threshold is `0.70` | `near_defeat_factor` | `1.50` | Longer |
| `random_civil_war_settlement_phase` | `settlement_progress_factor` | `1.40` | Longer |
| None of the same three extra-actor flags above | `no_extra_actor_factor` | `1.35` | Longer |

The extra-actor and no-extra-actor modifiers use complementary tests over the same three flags and cannot both pass in the same MTTH evaluation scope. The extra-actor rule is Boolean and does not add a further factor for each additional aligned-array actor.

### Evolution II: `random_civil_war_evolution_ii_days`

Base: `evolution_ii_base_days = 135`.

| Modifier condition | Named constant | Source factor | Delay effect |
| --- | --- | ---: | --- |
| `random_civil_war_land_border_exposure_ready` | `border_route_factor` | `0.75` | Shorter |
| `random_civil_war_sponsor_commitment_active` | `sponsor_route_factor` | `0.75` | Shorter |
| `random_civil_war_event6_front_active` | `independence_front_factor` | `0.80` | Shorter |
| `random_civil_war_multifront_active` | `multifront_factor` | `0.85` | Shorter, once regardless of front count |
| `random_civil_war_settlement_phase` | `settlement_progress_factor` | `1.40` | Longer |
| `any_neighbor_country = { has_stability > strong_neighbor_stability_threshold }`, with threshold `0.65` | `strong_neighbor_factor` | `1.25` | Longer when at least one neighbor qualifies |
| None of the land-border, sponsor-commitment, or Event 006 front flags above | `no_exposure_route_factor` | `1.25` | Longer |

The no-exposure test excludes the three named exposure routes but does not test `random_civil_war_multifront_active`; a multifront case can therefore also meet the no-exposure condition. The neighbor clause is one `any_neighbor_country` trigger, not a per-neighbor multiplicative loop.

### Evolution III: `random_civil_war_evolution_iii_days`

Base: `evolution_iii_base_days = 120`.

`severe_war_factor = 0.80` shortens the delay when `random_civil_war_opening_severity` equals the `severe` or `critical` value in `random_civil_war_severity`.

## Named-flag and external-condition notes

The parent effects set `random_civil_war_event6_route_ready` when live Event 006 evidence validates a dormant route. This is route readiness, distinct from an active Event 006 front. The Evolution I modifier treats it as an extra-actor marker, while Evolution II instead checks `random_civil_war_event6_front_active` for the active-front factor.

The parent effects set `random_civil_war_secondary_front_active` on the secondary opposition actor and the crisis host. They also set `random_civil_war_multifront_active` on the new actor and related host/source scopes as secondary fronts are activated. The Event 006 front-active marker is set on its selected actor. The land-border exposure-ready flag is set on the country whose land-border exposure route is prepared. Settlement resolution sets `random_civil_war_settlement_phase` and the reconstruction-phase flag.

The named source files show clearing paths for the Event 006 front, secondary-front and multifront, land-border exposure, and settlement markers. They do not contain the sponsor-commitment activation site. The named source set also does not define `random_civil_war_authority_is_failing`; the prior handoff identifies the core trigger file as `common/scripted_triggers/021_random_civil_war_triggers.txt`, which was outside this audit's authorized source list and was not opened. Both conditions remain externally defined inputs here.

## Scenario matrix coverage and classification

Scenario IDs are taken from the named fixture. No scenario was submitted to the MCP adapter, and no actor string, state map, scope map, typed numeric variable, neighbor relation, or scheduled state transition was fabricated. The flags listed below are the source-relevant flags supplied in the request, but their values were not bound in a successful scenario evaluation.

| Scenario ID | Fixture context and source factors | Input completeness | Result classification |
| --- | --- | --- | --- |
| `EVO1-01` | Large stalemated war, low authority, extra actor. The source includes the >8 controlled-state gate, the authority-failure helper, and the Boolean extra-actor group. | The three possible actor flags are known identifiers, but their values, authority state, controlled-state count, active-theater actor, and event state were not bound. | Source direction supports a shorter Evolution I delay when the named conditions hold. Effective timing and expected-direction validation are unresolved. |
| `EVO1-02` | One side near defeat, no extra region. The source includes surrender progress above `0.70` and the no-extra-actor flag group. | Surrender progress and actor/region flags were not bound. Missing typed values are not treated as zero or false. | Source direction supports a longer delay when the named conditions hold. Effective timing is unresolved. |
| `EVO2-01` | Long border, sponsor route, surviving Event 006 independence front. The source includes border, sponsor, and active Event 006 front factors, with a possible multifront factor. | Border and Event 006 flags were not bound. Sponsor flag lifecycle and current sponsor context were not supplied. | Source direction supports a shorter Evolution II delay when those conditions hold. Effective timing is unresolved. |
| `EVO2-02` | Early settlement and strong neighbors. The source includes settlement and `any_neighbor_country` stability gates, plus a separate no-exposure-route condition. | Settlement state, neighbor scopes/stability, and route flags were not bound. | Source direction supports a longer delay when settlement and strong-neighbor conditions hold. Effective timing and any overlap with no-exposure are unresolved. |
| `EVO3-01` | Evolution III available during a live severe Event 021 war. The source factor tests opening-severity variable equality against severe/critical constants. | The typed `random_civil_war_opening_severity` variable and live stage state were not bound. | Source direction supports a shorter delay for severe/critical opening severity. Effective timing is unresolved. |
| `EVO3-02` | Evolution III is already active before the first Event 021 firing. The fixture expects pre-fire activation without duplicate evolution recording. | This is the scheduler's pre-fire path, not an evaluated MTTH scenario. No event-recording path was selected by structural render. | Exact source fact: the uncommitted-opening branch fires the callback immediately and bypasses the MTTH delay. Duplicate-record behavior is unresolved in this audit. |

There is no normalized candidate pool for the three MTTH entries. The delay actor context comes from the live ordered `global.random_civil_war_active_theaters` array, and its membership and first qualifying actor were not provided. External-factor completeness is therefore incomplete for every timing scenario.

## Findings by audit concern

All three entries have explicit positive bases, conditional modifiers, and centralized constants. No raw numeric coefficient is duplicated inside an entry, and the checked source factors are all positive. The repeated settlement factor is a shared named constant used by Evolutions I and II. The actual scheduled delay is source-bounded by the parent effect's 60- and 180-day clamp, but no effective value within that range was evaluated.

Evolution I has a mutually exclusive extra-actor/no-extra-actor pair. Evolution II's multifront factor is one Boolean factor, not a per-actor factor, and the no-exposure modifier can overlap it because it checks only three route flags. These are exact source relationships, not balance conclusions.

The three timing entries do not define an AI score race, an option `ai_chance`, a probability-proportional candidate selection, or a custom weighted pool. Starvation, dominance, rank reversal, and normalized candidate probabilities are not applicable to this surface. The source-level scheduler keeps one due-date variable per stage and uses unlock/recorded guards, but event callback completion, repetition under live state changes, timing drift, and snowball risk were not simulated or proven by the partial structural graph.

The migration-relevant distinction is that actor-count sensitivity in these entries is expressed through Boolean markers, not an aligned-array count. Evolution I's extra-actor condition accepts any of the three marker flags once. Evolution II's multifront condition also applies once. No additional coefficient change is supported or recommended by this evidence.

## Recommended follow-up, without tuning targets

No numeric coefficient change is recommended from this baseline. For the pending roster migration, preserve the current distinction between Event 006 route readiness and Event 006 active-front state, and verify that the existing extra-actor and multifront markers remain truthful in the country scope where the scheduler evaluates each MTTH entry.

For a later audit, add the exact source that defines `random_civil_war_authority_is_failing` and the source that activates `random_civil_war_sponsor_commitment_active` to the audit inputs if their behavior changes or must be certified. Keep pressure, surrender, opening-severity variables, controlled-state counts, neighbor scopes, and active-theater membership unresolved until the live adapter explicitly supports those typed bindings.

The probability MCP follow-up is to use an adapter/index that recognizes these `common/mtth` values when reached through the current `mtth:` call pattern. This report does not diagnose why the live inspector returned `no_weighted_surfaces` and does not recommend a gameplay-source workaround.

## Later same-scenario compare recipe

The preserved pre-migration source path is `docs/plans/021_random_civil_war_plans/probability_snapshots/event021_evolution_mtth_pre_migration_2026-09-26/021_random_civil_war_mtth.txt`. The post-migration source path is `common/mtth/021_random_civil_war_mtth.txt`.

Once the live inspector discovers the MTTH candidates and a successful baseline evaluation has produced a schema-valid `scenarioSet`, run `hoi4.probability_compare` with adapter `event_mean_time_to_happen`, `before: { path: "docs/plans/021_random_civil_war_plans/probability_snapshots/event021_evolution_mtth_pre_migration_2026-09-26/021_random_civil_war_mtth.txt" }`, `after: { path: "common/mtth/021_random_civil_war_mtth.txt" }`, and the exact same saved `scenarioSet` object used by the baseline evaluation. Request `timing`, `comparison`, `sensitivity`, and `unresolved` outputs, and retain the returned comparison ID, scenario hash, source revisions, and artifacts.

This audit did not create a successful scenario set, scenario hash, analysis ID, or comparison ID. The descriptive Markdown matrix is not a machine `scenarioSet`. Therefore no numeric post-change compare can truthfully claim to reuse this audit's evaluated scenarios. If the migration is still pending when typed fixtures become available, first run and save the pre-migration evaluations using the six existing `EVO1-01` through `EVO3-02` IDs, with explicit values for all supported fields and no implied zero/false defaults. `EVO3-02` should remain a separate scheduler-path check because the current source bypasses its MTTH delay before the first committed opening. After migration, pass that identical saved scenario object to `hoi4.probability_compare` with the before/after paths above. Do not add `sourceRevision` or `sourceHash` fields to the compare source objects.

## Skipped analyses, limitations, and remaining uncertainty

`hoi4.probability_evaluate` and `hoi4.probability_sweep` were skipped because the live inspect result contained zero candidates and the required pressure, surrender, severity, state-count, neighbor, scope, and actor inputs were not fixtureable. `hoi4.probability_simulate` and `hoi4.probability_sequence` were not applicable because no uncertain distributions or complete declared custom pool were supplied. `hoi4.probability_render` was unavailable as an analysis view because no probability analysis ID was returned. No comparison was run because no post-change source exists and no successful baseline scenario set exists.

`hoi4.event_inspect` and `hoi4.event_render` ran, but their analysis is focused and partial. The direct timing selector found zero nodes for `chaosx.nr21.11`; the namespace view selected unrelated entry nodes and did not cover the three callback paths. Helper expansion was not requested. No structural MCP result is presented as proof of lifecycle or callback completion.

Unresolved inputs are the truth and scope of the named flags at scheduling time, exact pressure and authority values, surrender progress, controlled-state count, opening-severity variable, neighbor stability and relations, sponsor commitment activation, active-theater membership/order, and whether each event callback completes and records its evolution before rescheduling. The audit makes no exact probability, effective timing, sampled distribution, score, rank, repetition rate, or balance claim.
