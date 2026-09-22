# Context-complete specialist task cards

No role below was executed during planning.
These are pending instructions for the implementation environment.
Use `collaboration.spawn_agent` with `fork_turns="none"` only when that interface is actually available.
A role definition alone does not constitute an executed audit.

## Required envelope for every invocation

Copy this envelope plus the chosen role card into the invocation.
Do not assume the specialist can see the parent conversation.

Event is 074, Japan Lands in USA, Minor Fire-Once, Chaos level 1, Wars Medium.
Japan and USA already exist and are at war.
A successful firing immediately gives Japan a major combat-ready Pacific mainland army and wartime control, with California preferred and no winning or naval-supremacy requirement.
There is one special landing, finite support and reinforcement, three evolutions at 200/400/600, paid American response, normal war rules and no new country or focus tree.
The spec root is `docs/specs/074_japan_lands_in_usa_specs/`.
Read its README, all relevant design files, capability gates, source register, requirements coverage and acceptance matrix.
Work products belong under `docs/plans/074_japan_lands_in_usa_plans/`.
The main implementation contract is `prompts/074_japan_lands_in_usa_coding_prompt.md` under the spec root.
Current source gaps are listed explicitly in the reading register.
The planning author read 42 supplied text files and three additional full repository documents, but did not execute agents, inspect all external references, generate assets or run HOI4 tests.
The parent must append the current checkout, changed files, actual evidence, exact unresolved questions, allowed write scope and desired output filename.
Do not treat missing information as a passed test.

## chaosx_repo_explorer

Read-only source exploration unless separately authorized.
Resolve current event dispatch, root/history order, profile data, unit creation, local supply, AI strategies, technology grants, shared settings, evolution log, achievements and catalog owners.
Return exact file paths and line references, known supported consumers, conflicts with the legacy event, and the smallest proof cases for G01 through G11.
Do not write gameplay from guessed IDs or summarized wiki snippets.

## chaosx_scripted_system_architect

Review the defended landing, immutable footprint, actor scopes, cumulative issue ledger, reserve lots, reservations, support closure and campaign cleanup.
Focus on irreversible partial execution, ownership mistakes, leaking supply, casualty refill, reload duplication and a support-expiry cleanup that wrongly ends the campaign.
Return a concrete integration plan and evidence requirements within the granted scope.
Do not invent a native transaction rollback or per-division relocation API.

## chaosx_decision_mission_auditor

Read Part 4 and the decision-mission prompt in full.
Audit all nine actions and five missions for exact target ownership, four-cost maximum, native/custom cost parity, reservation/refund behavior, meaningful early-access rewards, continuous holds, deadlines, family waits and lifetime ceilings.
Check support closure separately from operation closure.
Return one row per action and mission with findings and exact tests.

## chaosx_ai_probability_auditor

Inspect before calculating with `hoi4.probability_inspect`.
Read Part 6 and P01 through P12 in the capability file.
Evaluate named states, sweep thresholds, simulate only declared uncertain inputs, compare revisions and render or sequence where required.
Keep exact, bounded, sampled and unresolved results distinct.
An unavailable verified game-version MTTH adapter is a blocker for timing claims.
Do not choose the intended design or modify source unless the parent grants that scope.

## chaosx_country_package_auditor

Audit preservation of existing JAP and USA identities, governments, parties, leaders, flags, focus trees, existing military units and diplomacy.
Review ordinary commander reuse, valid equipment and the American paid-force package.
No new tag is planned, so verify that no duplicate country or unnecessary identity assets have been introduced.
Any actual new-tag proposal requires a separate full collision audit and approval.

## chaosx_localisation_auditor

Read Part 7 and all implemented player-facing consumers.
Check factual geography, issued versus pending forces, costs, time windows, working-label leakage, modifier scope, current-country wording, native tooltips and relevant catalog detail text.
Check that super-event text has completed the required research instead of being copied from a working label.
Return exact missing keys, misleading claims, inconsistent phrasing and revised wording within the granted scope.

## Asset production roles

For `chaosx_asset_source_researcher`, pass the asset prompt plus the specific missing uniform, transport, coast or native-reference question.
For `chaosx_generated_event_art`, pass the asset prompt plus exact report/news/super-event subjects, sizes, region conditions, source mode and consumer.
For `chaosx_icon_artist`, pass exact action, category, spirit or achievement IDs, required templates, native sizes and output consumers.
All must read the matching actual reference family and retain provenance.
No role may claim a planned filename is a generated or accepted asset.
Portrait, frame-animation and 3D roles are not required by the present feature scope.

## Super-event text and audio roles

For `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher`, pass the complete dedicated super-event prompt plus the current resolved slot and approved references if any.
The text role supplies checked quotations and final text only after source review.
The audio role supplies a sourced 60–120-second cleared recording excerpt with composition and recording rights, exact timestamps and attribution.
Unresearched text and missing audio remain blockers.

## chaosx_spreadsheet_doc_worker

After final verified gameplay and localisation, read the authoritative workbook and supplied CSV snapshot.
Update Event 074's final mechanics, final event-detail wording and Wars Medium assignment in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.
Preserve unrelated workbook structure and content.
Regenerate the CSV through `.tools/export_event_catalog_csv.py`.
Do not edit the export directly or mark an unvalidated feature complete.

## chaosx_documentation_curator

Reconcile the final source specs, implementation docs, route coverage, asset manifest, catalog wording and accepted specialist findings.
Remove stale descriptions of full-state ownership transfer or the old twelve-division opening from active documentation.
Preserve historical evidence as history instead of rewriting it to imply past validation.
Keep working audits under plans and accepted design under specs.

## chaosx_improvement_loop_planner

This invocation is mandatory before the parent claims near completion.
Read all eight design parts, all prompt and reference contracts, the current implementation and actual evidence supplied by the parent.
Evaluate whether the central mainland invasion is complete and usable, especially the defended coast, independent opening supply, force concentration, American choices, delayed evolution, feedback and normal outcomes.
Return either a bounded concrete improvement addendum or an explicit closure handoff under the plans folder.
Do not add unrelated country identities, focus trees, currencies, world-ending routes or UI systems merely to expand the file count.
The parent must disposition every finding and integrate accepted changes into all affected surfaces.

## chaosx_event_completion_auditor

After the improvement findings have been disposed, audit the complete implementation against all user requirements, eight design parts, required prompts, route table, capability gates and acceptance cases.
Inspect actual file consumers and evidence.
Separate passed static checks, passed runtime checks, unexecuted checks and blocked components.
Report missing sources, skipped agents, unresearched presentation and false completion claims explicitly.
Do not accept a smaller force, ownership transfer, permanent immunity or omitted decision as a silent fallback.

## Other supplied roles

The focus-tree auditor, UI worker, portrait creator, 3D pipeline, skill maintainer and other defined roles were read during planning.
They are invoked only if an actual approved change creates their relevant surface or a skill-maintenance problem.
Do not manufacture work to claim that every supplied role has executed.
The requirement is complete relevant coverage with honest execution status.
