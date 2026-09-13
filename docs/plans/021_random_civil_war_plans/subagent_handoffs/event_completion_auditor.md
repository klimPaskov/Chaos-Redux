# Event 021 Random Civil War completion audit

> **Superseded historical audit.** This report describes the pre-improvement implementation inspected on 2026-08-30. Its Scotland-only adapter, two-mission surface, fixed scenario-count, single-secondary-front, and related findings were resolved in later Event 021 tranches. Current evidence and unresolved closure blockers are recorded in `docs/events/021_random_civil_war/acceptance_evidence.md`. This retained report is not the required final post-implementation completion audit.

Audit date: 2026-08-30

Auditor role: read-only event completion auditor

## Verdict

**Completion cannot honestly be claimed. Event 021 is partial and presently blocked from normal default availability.**

The repository contains a substantial Event 021 framework: the canonical event chain, hidden pressure and visible authority state, bounded scheduler and cap machinery, a standard decision category, three evolution dispatchers, reconstruction and cleanup helpers, cluster and triggerable-scenario registrations, six achievement definitions, shared log/detail integration, and a complete set of currently referenced DDS files.

The implementation nevertheless misses or simplifies several source-of-truth requirements. The most consequential defects are the missing default-enabled allowlist entry, a target weight that does not participate in target selection, a Scotland-only Event 006 adapter, proxy and unconsumed force/stockpile calculations, shallow same-tag and ordinary route distinctions, only one secondary front, fixed-count scenario intensities instead of country shares, unselected settlement outcomes, missing sponsor/neighbor decisions, stale or invalid documentation artifacts, and incomplete mandatory MCP proof.

Status vocabulary used below:

- **Finished** means the inspected repository evidence satisfies the stated source requirement, subject to the explicit runtime-validation limits in this report.
- **Partial** means a real implementation exists but does not cover the required breadth or behavior.
- **Blocked** means completion evidence or a required input is absent or unusable.
- **Design gap** means the accepted specification requires behavior for which no implemented disposition was found.
- **Stale** means documentation or a handoff no longer describes the current repository truth.

## Audit authority and material read

The audit read `AGENTS.md`, every file listed by `docs/specs/021_random_civil_war_specs/MANIFEST.sha256`, all sixteen Event 021 subagent prompts, every Event 006 specification file, the current Event 006 event/package implementation needed to assess reuse, the existing Event 021 plans and handoffs, and the current gameplay, localisation, interface, asset, documentation, catalog, and testing surfaces referenced below.

The Event 021 specification package is internally intact: a read-only SHA-256 verification matched every entry in `docs/specs/021_random_civil_war_specs/MANIFEST.sha256`.

The required repository skills were read and applied: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, and `xlsx`.

The offline Paradox wiki snapshot was consulted for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, and Country creation. Installed vanilla documentation was consulted in `documentation/effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `dynamic_variables_documentation.md`, together with vanilla `start_civil_war` precedents.

The engine reference matters here because installed `effects_documentation.md:8030-8059` defines `start_civil_war` `size`, `army`, `navy`, `air`, `states`, and filter behavior, while the offline Effects wiki warns that transferring the current capital prevents the civil war from firing. Installed dynamic-variable documentation also distinguishes `num_divisions` from actual formations and `num_of_military_factories` from equipment stockpile quantities.

## Completion status by surface

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Event identity and chain | Partial | `events/021_random_civil_war.txt:12-199` defines `chaosx.nr21.1` through `.16` and news events `.211-.212`, but most visible events are acknowledgement shells whose behavior lives entirely in parent helpers. Mandatory MCP projection was partial. |
| Default availability | Blocked | Event 021 is registered in `common/scripted_effects/chaosx_logic_effects.txt:310-320`, but `common/scripted_triggers/chaosx_settings_triggers.txt:10-40` omits Event 021 from `event_log_event_is_reworked_default_enabled`; `common/scripted_effects/chaosx_logic_effects.txt:381-394` consequently adds it to the disabled array at initialization. |
| Fracture Pressure and State Authority | Partial | Initialization, recalculation, clamping, and bands exist in `common/scripted_effects/021_random_civil_war_effects.txt:41-195` and `:219-380`. Route-evidence flags set in `common/scripted_effects/021_random_civil_war_parent_effects.txt:228-324` are broad and sticky, so recovered countries can retain opposition evidence and several archetypes do not require a concrete organized actor. |
| Target eligibility and weighting | Blocked | Eligibility helpers and a weight calculator exist at `common/scripted_effects/021_random_civil_war_effects.txt:387-453`, but automatic prefire selects a country with an unweighted `random_country` at `common/scripted_effects/021_random_civil_war_parent_effects.txt:2172-2187` and calculates the chosen country's weight only afterward. The target weight therefore does not determine the draw. |
| Severity selection | Partial | Severity weights and engine shares are centralized in `common/script_constants/021_random_civil_war_constants.txt` and calculated in `common/scripted_effects/021_random_civil_war_effects.txt:497-590`. The final launch uses severity-derived `start_civil_war` ratios, but the preceding candidate process and supporting force package do not meet the accepted model. |
| Six route archetypes | Partial | Route weights and flags exist in `common/scripted_effects/021_random_civil_war_parent_effects.txt:228-340`. Ideological, legal, regional, and command routes converge on near-identical ideology-swapped `start_civil_war` blocks at `:1263-1402`; the Event 006 and same-tag routes are separately implemented but incomplete. |
| Connected states and viable capitals | Partial | The plan excludes the current capital and grows from a random anchor through one `every_neighbor_state` pass at `common/scripted_effects/021_random_civil_war_parent_effects.txt:420-523`. This is bounded and usually connected, but it is not the specified recursive region construction or explicit capital, supply, rail, population, and industry scoring pass. |
| Parent remnant viability | Partial | `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:413-426` checks a surviving controlled state, capital/lost-capital state, factories, and manpower. It does not prove a connected and supplied remnant or validate the final partition topology. |
| Dynamic forces and stockpiles | Blocked | `common/scripted_effects/021_random_civil_war_parent_effects.txt:530-590` derives requested divisions from `num_divisions`, manpower from the country pool, and an equipment amount from `num_of_military_factories`; the latter is a factory-count proxy, not actual stockpile. Those requested division/manpower/equipment variables are not applied by the launch blocks at `:1263-1402`, which use only `start_civil_war` size/army/navy/air ratios. Formation location, loyalty, regional control, and actual stockpile are not allocated. |
| Event 006 full-package adapter | Blocked | The only dormant candidate and complete-package proof are Scotland/IW-001 in `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:39-114`. The adapter hardcodes package identity, state `121`, tag `SCO`, and `independence_wave_setup_iw_001_scotland` in `common/scripted_effects/021_random_civil_war_parent_effects.txt:1404-1545`. This is a real reuse of one complete Event 006 package, but it is not the required adapter over every complete human package at later stages. |
| Event 006 ownership boundaries | Partial | The Scotland adapter does not alter Event 006's firing weight, cap, congress, league, or evolution registrations, and it records Event 021 origin. Because only IW-001 is handled, the no-duplication and complete-package requirements are not demonstrated across the Event 006 package registry. |
| Same-tag path | Partial | `common/scripted_effects/021_random_civil_war_parent_effects.txt:1551-1575` opens a 45-day crisis and `:2125-2142` resolves it to autonomy if talks opened, otherwise government victory. There is no substantial loyalty, depot, coercion, dual-power, support-zone, or state-control contest matching the accepted same-tag design. |
| Front construction | Partial | The opening actor is created through four near-identical civil-war branches, and Evolution I can create one additional civil war on the first claimant at `common/scripted_effects/021_random_civil_war_parent_effects.txt:1041-1234`. The accepted two-to-four-front framework, mixed Event 006 actors, multiple front goals, coherent front-state assignment, and cap-aware deferred additional fronts are not fully implemented. |
| Decisions and missions | Partial | Seven standard decisions and two missions exist in `common/decisions/021_random_civil_war_decisions.txt:10-316`; no dedicated scripted GUI was introduced, so no `chaosx_event_ui_worker` handoff is required. Every displayed resource gate uses strict `>` against the cost, so exact-cost countries are blocked. The missions use 30-day constants at `common/script_constants/021_random_civil_war_constants.txt:468-469`, rather than the specified roughly 120-180 day operational objectives. The rail mission tests generic infrastructure rather than a named rail spine. |
| Neighbor and sponsor actions | Design gap | Effects for integrating formations, monitoring a border, supporting a government, and supporting opposition exist in `common/scripted_effects/021_random_civil_war_decision_effects.txt:110-170`, but no corresponding player decisions are exposed in `common/decisions/021_random_civil_war_decisions.txt`. Relief is exposed, while the specified separated relief and armed-support interaction surface is incomplete. |
| Evolution I | Partial | Active and prefire hooks exist, and one secondary front can be created. The required two-to-four-front breadth, multiple independent actor types, Event 006 package participants, territorial goals, and distinct front behavior are not complete. |
| Evolution II | Partial | Exposure and neighboring-country propagation exist at `common/scripted_effects/021_random_civil_war_parent_effects.txt:2445-2533`. Armed support, relief, and no-aid are mechanically separated in helper outcomes, but the player-facing sponsor actions are missing and only immediate-neighbor exposure is represented. Strange-incident logic exists but lacks current end-to-end probability evidence. |
| Evolution III | Partial | Nonterminal global fracture bands, queueing, caps, generation limits, and scheduler hooks exist at `common/scripted_effects/021_random_civil_war_parent_effects.txt:60-126` and `:2595-2617`, with tuning in `common/script_constants/021_random_civil_war_constants.txt`. Mandatory engine projection of the lifecycle and queue callbacks was unavailable in the Event MCP trace. |
| Bounded scheduling, caps, and nested crises | Partial | A bounded four-country registration sample, reviewed-array budget, critical queue, theater/global front caps, and maximum generation of two are present. The scheduler runs from `common/on_actions/chaosx_on_actions_chaos_meter.txt:21-83`. Source architecture is bounded, but no current scenario test proves queue fairness, cap release, annexed-target removal, nested-generation enforcement, or save/resume lifecycle. |
| Wars cluster 004/007/021 | Partial | Runtime constants and member helpers include Event 021 in `common/script_constants/event_cluster_constants.txt:134-136` and `common/scripted_effects/chaosx_event_cluster_effects.txt:498` and `:1296-1302`. `docs/systems/event_system/event_clusters.md:306-320` describes it. The authoritative workbook/export still lists only Events 004 and 007, and the shared player text exposes aggregate skipped counts rather than the Event 021 target/route collision reason required by the spec. |
| Triggerable scenario | Blocked | Registry hooks identify the scenario as current `SCN-018`, and all four named intensities are present. `common/script_constants/021_random_civil_war_constants.txt:549-551` defines Low/Medium/High as fixed budgets `1`, `2`, and `3`; `common/scripted_effects/021_random_civil_war_parent_effects.txt:2290-2359` consumes those counts. This does not implement approximately 10%, 25%, and 50% of eligible countries. Repeated random draws can also select countries that have become ineligible, reducing unique launches. Maximum uses all eligible countries as specified. |
| AI strategies | Partial | `common/ai_strategy_plans/021_random_civil_war_ai_strategy_plans.txt` defines actor profiles, and decision `ai_will_do` blocks exist. The route implementations collapse several archetypes into the same war launch, there is no complete opportunistic sponsor behavior, and the current weighted MCP disposition is recorded below. |
| Event logs and details | Partial | `common/scripted_effects/021_random_civil_war_parent_effects.txt:745-765` publishes Event 021 identity, actor, and payload into the shared system; shared actor/detail mappings exist in `common/scripted_effects/chaosx_events_log_effects.txt` around `:261-268` and `:2713`. The current localisation audit reports no exact cluster skip reason, no dynamic front/route/rail target, incomplete actor/capital/front detail payload, dead no-target strings, and an uninitialized authority fallback that can display Collapse. |
| Settlement outcomes | Blocked | The settlement selector at `common/scripted_effects/021_random_civil_war_parent_effects.txt:1588-1628` selects only independence, opposition victory, autonomy, coalition, or government victory. Partition, merger, and evolution flags can be set by `common/scripted_effects/021_random_civil_war_effects.txt:1392-1452`, but no selector path chooses them. The outcomes mostly set flags and generic reconstruction/grace state rather than implementing distinct legal, territorial, political, and military settlements. |
| Reconstruction and recurrence | Partial | Reconstruction ticks, recurrence scoring, grace, obligations, and repeat scheduling exist in `common/scripted_effects/021_random_civil_war_effects.txt:1392-1496` and `common/scripted_effects/021_random_civil_war_parent_effects.txt:2623-2703`. There is no current task-specific scenario evidence for obligation expiry, recurrence thresholds, repeat eligibility, or reconstruction convergence. |
| Cleanup | Partial | Cleanup removes missions, arrays, targets, flags, ideas, and scheduler state in `common/scripted_effects/021_random_civil_war_parent_effects.txt:2704-2774`. The Event MCP trace did not expand helper/lifecycle projections, and no automated lifecycle test proves that every terminal, annexation, deferred, or interrupted path reaches cleanup exactly once. |
| Six achievements | Partial | All six exact IDs are registered in `common/achievements/chaos_redux_achievements.txt:4059-4147`, with predicates in `common/scripted_triggers/021_random_civil_war_triggers.txt:626-712` and 18 wired root DDS files at `interface/021_random_civil_war.gfx:84-154`. `No State Left Behind` evaluates the bounded opening-state plan rather than every opening core state, while `A Flag of Our Own` and `Fractals of Sovereignty` are effectively constrained to the Scotland-only adapter. No current achievement scenario proof exists. |
| Visual assets | Partial | `interface/021_random_civil_war.gfx:9-154` references 35 textures; a read-only path audit found all 35 files. Three event pictures and all 18 root achievement state files exist. `docs/assets/021_random_civil_war/manifest.md:35-55` still marks the package `needs_user_review`, and `:29` incorrectly says root achievement duplicates were not created even though the wired root files now exist. In-game consumer acceptance is absent. |
| Portrait, animation, super-event, 3D, and named-event scripted GUI | Finished as not in scope | The accepted Event 021 specification excludes these surfaces. No character portrait, custom 3D unit, animation package, super-event, or dedicated scripted GUI was introduced, so no portrait, 3D audio/counter, frame-animation, super-event, or event-UI-worker handoff is required. |
| Documentation | Stale | `docs/events/021_random_civil_war/overview.md:49-57`, `:85-99`, `:127-181`, `:205-225`, and `:263-269` overstate connected-state quality, actual stockpile/force handling, sponsor actions, settlement breadth, scenario shares, details/skip reasons, and catalog/testing alignment. Its simplification section does not disclose the material gaps in this audit. |
| Workbook and exports | Blocked | The current `docs/spreadsheets/chaos_redux_events_catalog.xlsx` cannot be opened by `openpyxl` because `[Content_Types].xml` is missing from its ZIP package. The current CSV export remains legacy at `docs/spreadsheets/chaos_redux_events_catalog.csv:108`, the Wars row still lists only `4, 7` at `docs/spreadsheets/chaos_redux_clusters_catalog.csv:2`, and the scenarios export contains no Fracture Cascade/SCN-018 row. The exports were not regenerated because this audit is read-only. |
| Tests and acceptance evidence | Blocked | No Event 021-specific test references were found under `tests/`, `.tools/`, or `docs/testing/`. CXT setup registration exists, but it is not an event acceptance matrix. No current proof covers all archetypes, severities, state topologies, Event 006 packages, same-tag states, front caps, scenario intensities, achievements, settlement outcomes, reconstruction, recurrence, or cleanup. |
| Improvement loop | Blocked | No Event 021 improvement addendum or disposition exists. `docs/plans/021_random_civil_war_plans/subagent_handoffs/localisation_auditor.md:192` explicitly records that no central improvement plan was written. The mandatory near-completion improvement-loop review has not occurred. |

## Event identity, availability, and dispatch details

`events/021_random_civil_war.txt:12-21` preserves the required entry identity `chaosx.nr21.1` as a hidden triggered-only dispatcher. The opening, multi-front, exposure, settlement, global-fracture, ordinary-opposition, Event 006-front, reconstruction, cleanup, three evolution, review, scenario-country, same-tag, and news surfaces are all named in `events/021_random_civil_war.txt:23-199`.

The event is placed in the repeatable tier by `common/scripted_effects/chaosx_logic_effects.txt:317`, has a target-availability rejection and zero-weight safeguard at `:895-900` and `:1115-1125`, and is fired through `common/scripted_effects/chaosx_settings_effects.txt:4936-4942` after target prefire.

Those pieces do not overcome the default-disabled initializer. The allowlist in `common/scripted_triggers/chaosx_settings_triggers.txt:10-40` includes neighboring event IDs but not Event 021, and the initializer in `common/scripted_effects/chaosx_logic_effects.txt:381-394` disables every omitted event. `common/on_actions/021_random_civil_war_cxt_on_actions.txt:9-29` establishes the CXT registration bus and `random_civil_war_rework_ready`, but it does not add Event 021 to the default-enabled allowlist.

## Event 006 adapter audit

The Event 006 package specification and implementation establish a package registry, package completion gates, actor setup, route/focus behavior, and distinct later-stage states for multiple human-facing independence packages. `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md:5-17` records 32 content-attested selectable packages across 29 compatible reservation groups, 161 unattested selectable rows, 40 runtime adapters, and eight adapter-only fail-closed rows. Event 006 itself remains explicitly HOLD/PARTIAL, but Event 021 is still required to adapt every package that Event 006 currently regards as complete; Event 021 does not enumerate or dispatch that admitted set.

The Event 021 candidate trigger at `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:39-62` recognizes only a host that owns Scotland's state 121 and has dormant `SCO`. The complete-package proof at `:64-114` is explicitly documented as IW-001 and checks only the newly released Scotland package. The adapter at `common/scripted_effects/021_random_civil_war_parent_effects.txt:1404-1545` hardcodes the IW-001 package, Scotland's state and tag, and `independence_wave_setup_iw_001_scotland`.

This is not a placeholder adapter: it genuinely calls the Event 006 setup helper and then validates and records Event 021 origin. It is still a one-package special case against a current Event 006 authority of 32 content-attested packages. No evidence was found that Event 021 can select each complete human Event 006 package at its eligible later stage, route an already-existing Event 006 actor into a new front, preserve all package-specific territory and leaders across those packages, or prove no duplicate and no incomplete/nonhuman package across the complete registry.

Event 006 itself was inspected through both source and mandatory event MCP calls. The Event 006 MCP projection was also partial, so source evidence for its package helpers is not equivalent to a complete engine trace.

## Mandatory Event MCP evidence

The production `hoi4.event_inspect` and `hoi4.event_render` routes were used for both event chains in scope.

Workspace: `mod_chaos_redux_ea3b2d67c2c0`

Scanned revision: `eaac06f8f701ab05a6dbddefaf5fb924868bf893c253257c6ec3df519141cc1e`

Graph hash: `5dd50b6a226ffebbb466497af47c5a9da5cdafe7541988c46a47646be718d9ed`

Event 021 exact-root inspect returned `EVENT_INSPECTED_PARTIAL` because the workspace scan deferred helper and lifecycle projections and reported four unrelated blocking diagnostics; the selected graph had no helper expansion.

- Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa83412d8261ed0a34be25337a1ec7df8ca18c6ba020ffb130235bc4bd0fd80d/36369b4fe165104803c3b4b32213482a855972dacbf8c2a388e285dd8fb47237/event-trace-eaac06f8f701.json`
- Namespace trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4cd6b902ecc835e509441436d129dc4d2a5b733e5b05720b64910440b8ca424/97a2165f3a199ffe8bf5a98757e0a6207de336a4273fb0c95bbd8b3881b371cb/event-trace-eaac06f8f701.json`
- Exact-root overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7366425cbb91ceb4bd076b04460ad2e87350f8bfeee30b5b62237f8f61a3fdf/86172f682752caeb91ab052bd03df66eb1369be44ead2db134e5e1931bffacf5/event-overview-eaac06f8f701-manifest.json`
- Exact-root overview JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/08f282f9a8dc73f02e440802d68a43890275869f84b2503e372819acb844948b/b94e839095a43838e34d68f61025a566dc06ab5fbaab192e89b5b2c6189d7045/event-overview-eaac06f8f701.json`
- Namespace overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c7a6fd1f1feb3f6884b1a37bd906a137841e494a018090be47a1cf02f34548b/b002231479dd596e5135e381c583f95aa38a0359176556e5cad6d38860fbfb6f/event-overview-eaac06f8f701-manifest.json`

Event 006 exact-root and namespace inspection likewise returned partial projections.

- Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a36eca03bff007be26e2d01087a96684ee90c6d60f6486b65db6d0ed06f56c67/a1929230f3aa63bd40b1b97fba184c2001d3138cd663a4fbe93aed54023834e7/event-trace-eaac06f8f701.json`
- Namespace trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9bc1362e1e14df1c5193c3405f61f56485cb07272f12145f674da654cd4058f9/ca6c9bafdfae6fd16f5868bb9c89f8355d57a47a009ada6f299c05206eedaf56/event-trace-eaac06f8f701.json`
- Exact-root overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4b09bcc3f27a0e0eb54184da9ee6e45be11205f955c1584a27bd05f06b9d2c8/621a2e832f4b6fb4c306fb917d3328a9c37ab2293b246ac3a991cbbcbc51fcd4/event-overview-eaac06f8f701-manifest.json`
- Exact-root overview JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da3e710cf3d317e2f12ad0597951ae38601ff499c82ec65cbabb9b6176d1e9af/12c0b1655bc88d13fe241bb3f2f3070ed434451d10967a53a01c345d0222eaf5/event-overview-eaac06f8f701.json`
- Namespace overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07a7b83cb796071c7c990bde0773fe251c0de52b3965041c204b2c9a5bc9d2a8/810e134a7f0ace8937c33f36da172a05e656af6a9156692ff34b119514d739ca/event-overview-eaac06f8f701-manifest.json`

The namespace renders selected 180 nodes and produced indistinguishable broad layouts for Event 021 and Event 006, so they are retained as evidence that the route ran, not as proof of chain isolation.

`hoi4.event_compare` was required because the current Event 021 source differs from the repository baseline. A first compare returned `EVENT_COMPARISON_BASELINE_REQUIRED`. A second attempt scanned the workspace and supplied the baseline source, but returned `EVENT_BASELINE_MISSING` with the instruction to scan before comparing. No valid comparison artifact exists. This is an exact MCP blocker; the Git/source diff is not substituted for comparison evidence.

Because helper expansion was unavailable, the event MCP evidence does not prove the target reservation transaction, Event 006 helper chain, state partition, secondary-front callbacks, settlement selection, recurrence, reconstruction, cleanup, shared log payload, or scenario lifecycle. These remain source-reviewed but engine-unproven.

## Weighted AI and probability evidence

The first dedicated `chaosx_ai_probability_auditor` route remained `running` and produced no return after repeated bounded waits; it was shut down without usable evidence. A narrower replacement pass was requested. Its final disposition must be treated as mandatory completion evidence and is recorded in the final version of this handoff.

Independent source review identified these weighted surfaces, but source findings are not a substitute for the required probability MCP pass:

- Shared Event 021 selection weight and cap/recovery behavior.
- Candidate target weights and eligibility.
- Route-archetype weights.
- Severity weights and modifiers.
- Evolution I secondary-front route weights.
- Evolution II sponsor/relief/no-aid and strange-incident random lists.
- Settlement-outcome selection.
- Cluster optional-member probability and collision handling.
- Triggerable-scenario random target selection.
- Decision and mission `ai_will_do` scores.
- AI strategy factors and role selection.

Until the replacement auditor returns current scenario-specific MCP artifacts or an exact MCP blocker for each surface, Event 021's AI/probability acceptance gate is **blocked**.

## Assets and presentation

The asset package is materially present. `interface/021_random_civil_war.gfx:9-154` registers the category picture and icon, seven decision icons, two mission icons, three idea icons, three event/news pictures, and six three-state achievement sprite families. A path audit found all 35 referenced textures. The runtime folders contain three Event 021 event pictures and eighteen root achievement DDS files.

The package does not require character portraits, custom 3D units, unit audio, custom counters, frame animation, a super-event, or a dedicated named-event scripted GUI. The corresponding specialized handoffs are correctly absent and are not completion blockers.

The asset documentation is stale. `docs/assets/021_random_civil_war/manifest.md:29` says root achievement duplicates were not created and requires parent registration against event-scoped interface paths, while `interface/021_random_civil_war.gfx:84-154` now uses existing root `gfx/achievements/...` paths. The manifest and `docs/assets/021_random_civil_war/gfx_handoff.md:71` need disposition updates. All listed icon assets remain marked `needs_user_review`, so visual consumer acceptance cannot be claimed.

## Documentation, catalog, and accepted-plan disposition

The source-of-truth specification is accepted and intact, but implementation does not satisfy it. No later accepted Event 021 improvement addendum was found.

Existing handoffs have these dispositions:

| Handoff | Disposition |
| --- | --- |
| `scripted_system_architect_handoff.md` | Partly implemented in constants, helpers, state, reservation, scheduler, recurrence, and cleanup surfaces; no final owner acceptance/disposition note was found. |
| `generated_event_art_handoff.md` | Runtime event and category pictures are present and wired; user/in-game visual acceptance remains pending. |
| `icon_artist_handoff.md` | Its original blocked missing states were later produced and wired, but the handoff itself remains stale and was not superseded or formally promoted. |
| `localisation_auditor.md` | Current audit is useful and identifies exact-cost gates, details, cluster reason, and dynamic-text gaps; no owner patch/disposition is present. |
| `ai_probability_audit.md` | Stale pre-implementation evidence from 2026-08-29; it describes Event 021, cluster, and scenario surfaces as absent and cannot validate the current implementation. |

No Event 021 country-package auditor, decision/mission auditor, documentation-curator, spreadsheet-worker, improvement-loop-planner, or final completion report handoff was found. The conditional focus-tree audit was not triggered because Event 021 did not add or alter a focus tree; the Event 006 adapter calls existing Event 006 setup rather than owning a new tree.

The current authoritative workbook is not merely stale; it is invalid as an `.xlsx` package. A read-only `openpyxl.load_workbook(..., read_only=True)` call failed because `[Content_Types].xml` is absent, and archive listing showed only a partial set of package entries. The working tree marks the workbook and all three exports modified, so this audit did not infer that the invalid state predates the current work.

The current exports are still inconsistent with the implementation and spec:

- `docs/spreadsheets/chaos_redux_events_catalog.csv:108` describes Event 021 only as “A random country fractures into rival governments and armed camps” and marks it `To Be Reworked`.
- `docs/spreadsheets/chaos_redux_clusters_catalog.csv:2` lists the Wars cluster as Events `4, 7`, omitting Event 021.
- `docs/spreadsheets/chaos_redux_scenarios_catalog.csv` has no Fracture Cascade or SCN-018 row.

## Meaningful validation performed and missing

Performed:

- Verified every Event 021 specification file against its SHA-256 manifest.
- Read and compared the full accepted Event 021 package against current script, localisation, assets, docs, plans, catalog, and relevant Event 006 package surfaces.
- Consulted offline wiki and installed vanilla documentation for event, civil-war, scope, state, decision, AI, and dynamic-variable behavior.
- Ran mandatory Event 021 and Event 006 `hoi4.event_inspect` and `hoi4.event_render` calls and retained their partial artifacts and exact limits.
- Attempted mandatory `hoi4.event_compare` against the changed Event 021 revision and recorded both exact blocker codes.
- Routed every weighted Event 021 surface to a dedicated `chaosx_ai_probability_auditor`; the first route returned no evidence and the replacement disposition is required below.
- Checked all 35 Event 021 GFX texture references and confirmed the current files exist, including all six achievement triplets.
- Attempted to open the authoritative workbook read-only and established that its package is invalid; verified the current export omissions directly.
- Searched `tests/`, `.tools/`, and `docs/testing/` for Event 021-specific acceptance coverage and found none.

Missing or blocked:

- Complete event helper/lifecycle MCP projections and a successful changed-revision comparison.
- Current probability MCP artifacts for all weighted surfaces until the replacement auditor returns.
- Task-specific executable scenario coverage for all routes, severities, topology cases, Event 006 packages, same-tag flow, two-to-four fronts, exposure, caps, queueing, nesting, scenario shares, settlements, achievements, reconstruction, recurrence, and cleanup.
- Valid authoritative workbook and regenerated exports.
- Current asset consumer review and event/detail visual acceptance.
- Improvement-loop addendum and accepted disposition.
- Parent disposition for stale, partial, or blocked subagent handoffs.

## Undisclosed simplifications and blockers

The following simplifications are material and are not fully disclosed by the current overview:

1. Event 021 is registered but default-disabled because its allowlist entry is missing.
2. Target weighting is calculated but does not influence the random target draw.
3. Four ordinary archetypes share nearly identical civil-war launch behavior.
4. Connected territory uses a random anchor and one neighbor expansion pass rather than the specified topology and viability planner.
5. Force and stockpile planning uses country-level proxies; equipment is derived from military-factory count and the requested package is not consumed by the launch.
6. Event 006 reuse is limited to Scotland/IW-001 rather than every complete eligible human package.
7. The same-tag route is a short autonomy-or-victory timer rather than a developed dual-power crisis.
8. Evolution I creates at most one additional front rather than the full two-to-four-front framework.
9. Neighbor armed-support and monitoring effects are not exposed as decisions.
10. Low/Medium/High Fracture Cascade intensities are fixed at one, two, and three targets rather than approximately 10%, 25%, and 50% of eligible countries.
11. Partition, merger, and evolution settlements are defined as flags but are never selected by normal settlement logic.
12. Several achievements operate over the simplified state or Scotland-only surfaces rather than the accepted general package.
13. Event Details and cluster diagnostics do not expose all accepted actor, front, target, route, and skip-reason data.
14. The authoritative workbook is currently invalid, and all three generated exports remain inconsistent with Event 021.
15. Mandatory event comparison, full helper projection, probability acceptance, task-specific tests, visual consumer review, and improvement-loop disposition are absent.

## Required next actions before any completion claim

1. Restore normal availability by adding the accepted Event 021 default-enabled disposition and prove the shared selection path can actually fire it.
2. Make candidate weights govern candidate choice, then run baseline and post-change probability audits with the accepted named scenarios.
3. Replace proxy/unconsumed force-package calculations with actual supported engine inputs and explicit formation, manpower, equipment, air, navy, and state allocations that meet vanilla semantics.
4. Generalize the Event 006 adapter across the complete eligible human package registry and prove no duplicate, incomplete, nonhuman, congress, league, cap, or evolution regressions.
5. Implement or explicitly reject with user approval the missing ordinary-route distinctions, same-tag depth, two-to-four fronts, neighbor/sponsor decisions, and settlement outcomes.
6. Implement scenario intensities as eligible-country shares with unique-target and cap-aware selection.
7. Repair exact-cost decision gates, mission duration/target semantics, dynamic details, cluster skip reasons, and achievement predicates that currently inherit simplified mechanics.
8. Produce task-specific scenario evidence for reservation, state topology, launch, fronts, caps, queueing, nesting, settlements, obligations, recurrence, cleanup, and achievements.
9. Obtain successful current `hoi4.event_inspect`, `hoi4.event_render`, and changed-revision `hoi4.event_compare` evidence with helper/lifecycle coverage; retain exact blockers if the MCP remains unable to produce it.
10. Complete the required improvement-loop review, merge accepted design changes into the spec, and disposition every existing handoff as promoted, queued, rejected, superseded, or blocked.
11. Repair the authoritative workbook, update Event 021, Evolutions I-III, Wars cluster 004/007/021, and SCN-018 from accepted implementation facts, then regenerate all three CSV exports through the repository exporter.
12. Reconcile the asset manifest with the wired root paths and obtain user/in-game visual acceptance.

## Final completion statement

**Event 021 Random Civil War is not complete.**

The current implementation is a broad but materially simplified framework with blocking availability, targeting, package-adapter, force-allocation, scenario, settlement, documentation, catalog, validation, and MCP-evidence gaps. It must remain classified as **partial / blocked**, not finished.
