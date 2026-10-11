# Event 100 MCP and subagent handoff

## Evidence boundary

This is the technical review map for the accepted planning package. All nine core parts define gameplay. This file assigns the inspections and specialist work needed to implement that design without inventing engine support.

During the original planning session, metadata discovery returned no callable HOI4 MCP tools.
The architecture and improvement-loop specialists reportedly confirmed that absence in exposed metadata.
No engine inspection, probability evaluation, native rendering, save validation or live-game test was reported.
Those statements describe the original session, and do not establish current route availability, service health or standalone viewer availability.

The source protocol permits planning to finish with this explicit map. A future implementation must discover the actual current tools, schemas, supported selectors and service state before calling them. Names below follow the supplied project skills. They are planned tool families, not invented successful calls.

## Required source and capability acquisition

Read current `AGENTS.md`, relevant `.claude/skills/chaos-redux-*` sources, actual shared helper bodies, their owner documentation, offline Decision modding, Effects, Triggers, Scopes, Data structures, On actions, Ideas, Characters and scripted-localisation references. Inspect installed game documentation and exact vanilla precedents for the current version.

The planning session fully read all supplied source attachments. It additionally inspected the target repository at commit `a3ef485c5da7e2337122eca04ac65c175050f251`. That later pass was bounded. Some large repository files received named section reads, as recorded in the research companion. It was not an exhaustive repository or installed-game audit.

The Event 035 registry-linked `.md` helper document was unavailable in that pinned inspection.
Its `.txt` gateway and `docs/events/035_great_depression.md` were located, and source 100 was absent from the inspected gateway allowlist.
Revalidate the current owner contract and implement any still-required explicit extension before claiming the connection works.

## MCP usage map

| Surface | Inspect before editing | Named scenarios and required output | Comparison and acceptance limit |
| --- | --- | --- | --- |
| Engine references and helper reuse | `hoi4.reference_context`, `reference_search`, `reference_read`, `source_lookup` where exposed | Exact paths/spans and version for temporary lifetime, date conversion, scripted constants, concrete resource payment, dynamic mission timeout, political identity and native split | Source coverage is explicit. A missing helper body or installed reference remains unresolved. |
| Root event and economic lifecycle | `hoi4.event_inspect`, `event_render` and supported state-flow/impact selectors | Prefire actor, accepted admission, ten-day worker, index changes, two support slots, recovery, warning, inherited continuation, invalidation and Event 035 request | Use helper-aware full lifecycle coverage, not only a focused trace. Compare actual before/after source with `event_compare` where supported. Report partial coverage. |
| Scripted helpers and scopes | `hoi4.script_validate` or the current supported equivalent | Actual country/state scopes, caller-initialized temporary outputs, current versus originating actor, due-date conversion and each result code | A null or partial validator result is not proof of native effect behavior. Source and runtime evidence remain separate. |
| Country targeting | `hoi4.probability_inspect`, then evaluate | Complete current major-or-player union, duplicate-major/player entry, loads 0/1/2/3, risk bands, cooldown and empty pool | Sweep risk/load boundaries. Show actual relative scores and the complete pool before deriving any probability. |
| Economic decision AI | Inspect, evaluate, sweep | The Part 8 matrix plus old/effective stance, delayed shock, final taper, zero reserves, invalid targets, occupied slots, wartime production and late warning | Compare immutable implementations with identical fixtures. Test rank reversals and starvation of viable rescue. No score-to-click-probability substitution. |
| Opposition and government response | Inspect, evaluate, sweep | 5% support floor, dominant opposition, two substantial alternatives, genuine same-ideology route, invalid leader, dictatorship, feasible concession, existing civil war and unsplittable territory | Verify support-sensitive ordering, zero invalid candidates and the same frozen challenger in both branches. Exact outcome percentages require the whole pool. |
| Evolution entry and repeat timing | Inspect MTTH/pool source, evaluate, sweep | Just below and exactly 200/400/600/800, each enable setting, relevant severe hardship, stable attempt, current cooldown and successor protection | Preserve the verified timing adapter and its cadence. Do not reinterpret a ninety-day MTTH as a ten-day click chance. |
| Declared uncertainty | `hoi4.probability_analyze` (`analysis = simulate`) only after inputs are explicit | Vary only declared uncertain external pressure, selection factors or future supply outcomes with reproducible assumptions | Keep deterministic scenario facts fixed. Do not invent an uncertainty distribution because evidence is missing. |
| Full event sequence | `hoi4.probability_analyze` (`analysis = sequence`) only after the complete custom pool and state machine exist | Complete candidate set, cadence, cooldowns, removals, state transitions, lineage merges and termination | Block sequence claims when pool or cadence is incomplete. A sequence of isolated willingness scores is not a campaign model. |
| Probability presentation | `hoi4.probability_analyze` (`analysis = render`) when useful | Ranking matrix, threshold sensitivity, timing bands, actual before/after comparison or unresolved state | Link the rendered artifact to its source and fixture. Rendered polish does not resolve unsupported inputs. |
| Native category, costs and timers | Inspect actual native category and decision GUI consumers, then `hoi4.gui_inspect` and `gui_render` if those tools support the relevant surface | Main list, fiscal selection with six entries, long country names, all maximum costs, both support timers, recovery, political replacement, D11 milestone transition, supported UI scales | Store matched before/after `gui_render` evidence. Do not request an invented `gui_compare` tool. Declare what the renderer could and could not evaluate. |
| Civil-war country package | Current country and map inspection tools when exposed, installed native split source | Frozen challenger, capital legality, useful connected territory, current wars/subjects, stockpile/force partition, research/focus continuity and reunification | Native default behavior is not automatically the desired result. Opponent identity, material conservation and valid politics require evidence. |
| Artwork and native consumers | Source inspection, decoded DDS previews and supported render consumers | Fourteen action subjects, category identity, two objectives, six crisis stages, three adjustment forms, ten reports and six achievement triplets | Verify the actual consumer and template, native sizes, alpha and decoded output. A generated PNG alone does not establish asset completion. |
| Persistence and live effects | User-provided saves through `chaos-redux-save-inspection`, plus authorized user observations | Before/after due milestone, between-review interruption, exact warning tie, paid cancellation, political split, later-acquired capacity and stale callback | Save evidence proves the observed run. The user performs live game validation. Ordinary planning or implementation does not silently launch the game. |

## Probability fixture manifest

The coding parent must preserve a complete machine-readable fixture alongside each actual probability output. At minimum it names the actor, complete candidate pool, current index, effective and selected stance, next unapplied review, current external family components, programme identity and dates, paid receipts, actual resource reserves, objective dates, opposition support and evolution settings.

Use named fixtures such as `mild_opening`, `lagged_overcorrection`, `e4_currency_prompt`, `e4_currency_late_warning`, `e4_without_e2`, `deflation_empty_reserves`, `currency_both_shock_conditions`, `programme_release_ladder`, `stable_control_liability`, `dominant_opposition`, `constitutional_transfer`, `authoritarian_refusal`, `unsplittable_country` and `successor_day_90`.

Each fixture states expected ordering or allowed outcome, not an invented observed result. Source identities and exact before/after revisions are required. The package's arithmetic demonstrations are independent authored-model examples and must retain that label.

## Canonical specialist map

Dispatch through the current canonical role and runtime contracts in `chaos-redux-subagents`, rather than an imported configuration's model or concurrency settings.
Give every spawned role a self-contained prompt with no inherited context.
Pass the event ID, slug, user-authorized acceptance basis, current source paths, allowed/excluded files, exact task, known blockers, prior dispositions, expected handoff and mandatory parent review.
Do not rely on inherited conversation state or treat a file's existence as approval.
Actual implementation review results belong in `docs/plans/100_inflation_plans/subagent_handoffs/`.

| Specialist | Exact responsibility and input | Owned output and boundaries | Session disposition |
| --- | --- | --- | --- |
| `chaosx_scripted_system_architect` | Review mutation order, helper scope, due dates, two slots, local quotes, lineage and owner adapters from the accepted parts | Narrow documented helper plan and concrete call sites. Shared framework edits require parent ownership. | Applied in a context-free planning task. Parent reviewed the complete report and folded accepted fixes. |
| `chaosx_decision_mission_auditor` | Audit all fourteen native action consumers, costs, cancellation, timers, AI gates and lifecycle | Bounded review or exact scoped fixes during implementation. Parent reviews every repair. | Applied in a context-free planning review. Source-level findings were resolved in the accepted parts. |
| `chaosx_improvement_loop_planner` | Final depth and anti-bloat review after the main design is assembled | One resolved addendum or closure handoff under `docs/plans/100_inflation_plans/` | Applied near completion with complete required source and nine-part reread. Accepted corrections were folded into the package. |
| `chaosx_event_completion_auditor` | Compare the entire accepted package against implemented routes, assets, texts, owner integration and evidence | Read-only completeness table, explicit missing/simplified/blocked/stale results. It cannot certify missing runtime evidence. | Required at implementation closeout. Planning closeout evidence is recorded separately. |
| `chaosx_ai_probability_auditor` | Perform the complete named targeting, policy, opposition, refusal, MTTH and repeat scenarios | Read-only inspect/evaluate/sweep/compare evidence, optional justified simulation/sequence/render | Deferred to a session with actual source implementation and the required probability service. No probability audit is claimed here. |
| `chaosx_country_package_auditor` | Actual party, leader, country identity, territorial split, current wars, subjects, material inheritance and focus continuity | Country compatibility matrix and narrow permitted repairs, with parent integration | Required for political implementation and each directly relevant DLC configuration. |
| `chaosx_generated_event_art` | Fictional documentary category and report scenes from the accepted asset manifest | Source art, processed previews, provenance and family handoff. It does not write gameplay or ordinary runtime GFX. | Production handoff in the asset prompt. |
| `chaosx_icon_artist` | Fourteen native action subjects, objective/category icons, spirit stages and six achievement subjects | Correct family-native art and required achievement triplets through immutable templates | Production handoff in the asset and achievement prompts. |
| `chaosx_asset_source_researcher` | Any actually required grounded nonportrait scene or archival artifact | Verified source/provenance and processing handoff | Conditional production assignment when a manifest row uses a real historical subject. |
| `chaosx_portrait_creator` | A genuinely missing valid current character portrait, if discovered in country integration | Identity-preserving source, correct leader/advisor outputs, archive and narrow permitted portrait wiring | Conditional on a real missing consumer. Existing country portraits are reused where valid. |
| `chaosx_localisation_auditor` | All final event, decision, tooltip, spirit, achievement, history and Details text written from direction | Readable accurate final strings, dynamic token and encoding audit, no invented gameplay | Required after the actual text exists. The current specs contain writing direction, not final localisation. |
| `chaosx_documentation_curator` | Reconcile accepted decisions, implemented evidence and closed review dispositions | Accurate event docs and implementation resume record, without gameplay or catalog authority | Parent completed planning reconciliation. Use the role after implementation tranches when documentation needs coordination. |
| `chaosx_spreadsheet_doc_worker` | Exact verified catalog fields after implementation, using current `chaos-redux-xlsx` guidance | Update the authoritative XLSX and regenerate CSV exports through the owner command | Current planning leaves the requested status To Be Reworked. No catalog was edited. |
| `chaosx_repo_explorer` | Bounded current ownership or precedent uncertainty | Read-only source paths, contracts, revisions and explicit coverage | Generic supplied-source readers performed the present repository investigation. Do not claim this canonical role was instantiated for it. |

Specialized roles whose surfaces are not introduced by the accepted design are not manufactured into event content merely to instantiate them.

## Parent review and closing sequence

The parent owns runtime integration, ordinary GFX wiring, shared registries, event history, cost-provider boundaries and the final completion claim. Specialist output is evidence to review, not self-validating approval.

After a meaningful implementation tranche, run the mandatory improvement loop again and resolve its result. Finish decision, country, probability, localisation, asset and completion review on the actual implemented source. Preserve current evidence and report unresolved branches explicitly. A planning package can be complete while production gates remain open. An implemented event cannot be called complete on the strength of this planning package alone.
