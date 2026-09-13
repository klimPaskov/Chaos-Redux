# Camp administration foundation handoff

Disposition: implemented within the parent-assigned new-file foundation scope.
Acceptance basis: the user's complete camp administration implementation request, `accepted_implementation.md`, and the parent-approved public contracts exchanged during implementation on 2026-09-06.
Complete feature acceptance remains parent-owned; this handoff does not assert GUI, historical calibration, AI or live-engine completion.

## Files and public surface

- `common/script_constants/camp_administration_constants.txt`: population units, capacities, workforce/development ratios, economic caps, material maintenance/reserves, budgets, project duration, mortality abstractions, role/control/cause enums and research limits.
- `common/scripted_effects/camp_administration_effects.txt`: initialization, finite admission, measured cause receipts, allocation/economic refresh, material payment, automatic maintenance/development, partial/full release, closure/reopening, national/site reform and common research award claims.
- `common/scripted_effects/camp_administration_effects.md`: complete public helper, scope, input/output, default, side-effect, lifecycle, tuning and migration contract with admission example.
- `common/scripted_triggers/camp_administration_triggers.txt`: valid registered operator, narrowly authorized subject control, productive workforce, independent slots and country-owner radical gate.
- `common/dynamic_modifiers/camp_administration_dynamic_modifiers.txt`: national military factory output, project-relevant infrastructure construction and existing local extraction contributions.
- `foundation_source_tests.py`: executable source evaluator and task-specific regression scenarios.
- `foundation_test_results.json`: latest source scenario results.

No existing runtime, shared accounting, configuration, registry, GUI, country module or localisation file was edited by this worker.
No Git commit was created, as assigned.

## Integration contract

The integration owner received and implemented country initialization, registered-site initialization, bounded monthly replacement, close-before-pointer-clear, explicit same-authority reopening, and voluntary `camp_admin_reform_site` hooks.
Parent must review that integration rather than treating this statement as its independent completion proof.
The legacy percentage population pulse must never run alongside foundation monthly custody losses.
Country census/admission preparation runs before `camp_admin_monthly_country`; country institutional programs run after its maintenance and economy step so both share the remaining material budget.
`camp_admin_civilian_states` retains countries in the existing bounded processor after legacy active custody sites retire.
Terminal country cleanup must close retained civilian states before removing their country from processing.
National reform must also call the occupation owner's `camp_occ_close_country`; it is not silently coupled into this foundation.

Country owners hold source membership and decrement it only by returned actual admission, define role and site-specific output scale, authorize narrowly identified subject-hosted institutions, and implement major historical regime gates.
All default cohorts are empty; the foundation never invents detainees from a state pressure score.
Occupation and custody cannot reserve the same civilians: admission excludes the occupation remaining cohort and occupation initialization must exclude existing detainees.
The major-country owner receives `camp_admin_release_detainees` for finite engineering releases, rather than releasing the entire camp or granting a flat manpower stockpile.

The two slots are `camp_admin_economy_slot_active` and `camp_admin_institution_slot_active`.
Material payments use `camp_admin_quote_support`, `camp_admin_quote_pp` and `camp_admin_payment_accepted`; ordinary maintenance and development have zero PP cost.
The common award helper consumes an explicit valid-program contract, bounds the returned single-use research bonus to 50–100 percent, and permits two accepted claims per calendar year across all programs.
Program identity, category, limited-use engine bonus wiring and program repetition guards remain country-owner responsibilities.
`camp_admin_development_paused` blocks new project starts; existing supported commitments continue.
The institutional owner confirmed the same auto-start rule.

Material completion exposes `camp_admin_economy_completed_this_month`, `camp_admin_economy_completed_state_id` and `camp_admin_economy_completed_type` for the parent journal.
This worker emits no duplicate history entries.

## Arithmetic and lifecycle proof

Production uses actual surviving finite workers with mutually exclusive industry/works/extraction allocations.
The developed 40 percent participating-industry equivalent is weighted over real national military factories and bounded to 25 percent.
Infrastructure construction receives up to 40 percent only during the state's live works project; the `state_production_speed_infrastructure_factor` modifier does not affect unrelated building types.
Existing local resource opportunity bounds the extraction allocation and 40 percent maximum.
Killing roles receive no forced-work allocation; a radical national mandate alone never converts site roles.
Suspension stops productive allocation while custody and maintenance obligations continue.

The shared exact civilian-loss API is called once with logging disabled, the real before/after state population difference is measured, and that amount is registered with `chaos_deaths_apply_state_pop = 0`.
Site and original-authority cause/month/cumulative ledgers use that same measured amount in thousands.
No second population debit, casualty-derived research progress or protected-group selector is introduced.
Partial release, full release, closure and civilian replacement never add population.
Country output is refreshed immediately on releases and closures.
Original responsibility and cause totals survive capture; foreign reopening and duplicate custody/civilian registry membership are rejected.

Maintenance is 0.5 support equipment per thousand people each month, so a 100,000-person cohort requires 50 units/month and a 1,000,000-person cohort 500 units/month before development.
The spending ceiling includes those existing obligations, plus 150 or 350 optional material units for development/priority budgets.
Actual available stock after a 100-unit reserve determines any shortage.
Four supplied-work reform programs replace 25 percent of the surviving-worker target each, without recreating anyone or deleting constructed infrastructure.

`python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/foundation_source_tests.py` passed 16 scenario groups against parsed current production helpers and the existing shared exact-loss source.
They cover zero initialization, finite source/capacity intake, consumed proof, four distinct causes, exact physical/cohort/log conservation, exclusive allocations, economic caps, live/ended works projects, suspension, reserves, twelve automatic months, duplicate callbacks on another day of the same month, selected reform and twelve-month paid civilian replacement, independent award slot and annual cap, 1M/7M obligation funding, cap reachability with a real finite 1M admission, capture cleanup, occupation nonoverlap and protected-floor clamping.
The developed 1M cohort/100 participating military factories/full support fixture reaches the 25 percent national bound through the actual helper arithmetic, distributed over five legal five-level sites with 200,000 actual source-admitted people each.
The 1M/7M maintenance cases likewise use five/35 legal developed sites instead of exceeding the building cap inside one state.
The twelve-month 76,000-person fixture ends with 71,353 survivors and 9,556.925 support equipment from an explicit 10,000-unit starting fixture.
A nine-month fixture also completes three paid automatic upgrades, growing capacity from 100,000 to 175,000 without any automatic intake.
The required supplied-work correction produces distinct source-evaluated durations: 17 months for a 5,000-person workforce cohort at the same site, two months for an 80,000-person cohort, three months for the later developed stage and four months for a larger physical project.
The corresponding frozen work targets are 5.25, 5.25, 11.5 and 13.25 work units.
Fractional work persists when available workers decrease; shortages and zero remaining workers add no work or development payment.
The physical capacity calculation clamps development to its supported maximum before applying capacity bonuses, and a five-level concentration site with three developments yields 200,000 places.
These fixtures are stated inputs, not historical save-game stockpile measurements.

The evaluator mocks only engine primitives and external accounting consumers, raises on unsupported statements, rejects undocumented direct `limit` fields under `for_each_scope_loop`, and asserts every Deaths registration uses population application off after the physical debit.
It does not prove engine rounding, dynamic modifier scheduling, actual native scope parsing, real stockpile starting values, GUI behavior or historical long-period casualty calibration.
Those evidence limits remain visible in its result file.

## References and MCP evidence

Required repository rules and the events, decisions/missions, state-ledgers and subagents skills were read and applied.
No skill was changed.
Offline wiki core pages were consulted, with Data structures variable/array/event-target sections, Effects variable/transaction sections, Modifiers dynamic modifiers, Scopes, On actions and decision/event guidance supplying the relevant syntax checks.
No Paradox wiki web access was used.

Vanilla references: `documentation/script_concept_documentation.md` Script Constants, `common/script_constants/documentation.md`, `documentation/dynamic_variables_documentation.md` state population/resource/building levels and country equipment/year fields, `documentation/effects_documentation.md` arrays, variables, stockpile effects and event targets, `documentation/triggers_documentation.md` scope/variable predicates, and `documentation/modifiers_documentation.md` state building-specific construction speed.
Vanilla precedents include `common/dynamic_modifiers/0_dynamic_modifiers.txt` autonomous-state structure and `common/dynamic_modifiers/wuw_dynamic_modifiers.txt` `GER_south_east_asian_construction_modifier`, which explicitly uses `state_production_speed_infrastructure_factor`.
Existing owner references: `camp_repression_rework_effects.txt`, existing camp triggers and genocide dynamic modifiers, and `chaosx_dynamic_effects.txt/.md` exact civilian loss and shared support-equipment removal.

The worker's `hoi4.event_inspect` request returned `timed out awaiting tools/call after 180s`; no event graph result or substitute engine proof is claimed.
A worker GUI inspection without a paired scenario was rejected with `windowName and scenario must be provided together`; no evidence was produced by that invalid call.
The parent then instructed this worker to consume the already completed GUI baseline instead of launching a duplicate inspection.
The parent baseline request/result files were read: `mcp/before_inspect_request.json`, `mcp/before_inspect_result.json` (`GUI_INSPECTED`, workspace `mod_chaos_redux_ea3b2d67c2c0`, artifact `gui-inspect.01d5386426215109.json`) and `mcp/before_render_result.json` (`GUI_RENDERED`, `repression_ledger_window-full.svg`).
These are the old HUN/sites fixture and its recorded source identity; they are not current-helper visual acceptance.
Current-source GUI inspection/render and final visual evidence remain parent-owned as explicitly directed.
No focus, map-data rewrite or weighted probability helper was authored; no probability audit is claimed for this deterministic foundation.

## Remaining limitations and follow-up

No gameplay fallback or population substitute was used within the assigned foundation.
Different-authority reuse of the same historical site is intentionally unsupported until an explicit authority-phase ledger can preserve both histories.
Civilian-converted locations cannot reopen as custody sites through the empty-location API and enter both arrays.
The construction allocation supports the explicitly owned infrastructure project, not an invented engine construction-queue query.
Wider occupation campaign mortality and historical million-scale calibration belong to the separate occupation/country modules; they must not be forced through detainee mortality to meet a quota.
Actual GER/JAP/SOV starting-stock and production-economy sustainability need parent scenario evidence; no native save or running game was available or invoked by this worker.
Parent integration review, specialist audits, current GUI evidence, cross-module source tests and full accepted-scope completion remain required.

## Supplied-work correction acceptance

Disposition: implemented following the parent's explicit required correction that supplied work and physical project scale, rather than a shared three-month timer, determine completion.
`camp_admin_economy_progress` and `camp_admin_economy_target` use work units, with the parent GUI already consuming their guarded ratio.
`camp_admin_economy_work_rate` uses surviving matching allocations and current funded conditions.
Targets freeze current site physical scale and development stage, or the finite civilian conversion group, once per slot; the completion fraction of an existing month-based commitment is preserved once during migration.
No GUI file was edited by this worker.
The occupation owner also requested the existing public `chaos_deaths_record_state_ledger = 1` projection contract; custody's measured log-only receipt now sets it, so shared observers can distinguish a casualty receipt even when population growth masks the raw population delta.
