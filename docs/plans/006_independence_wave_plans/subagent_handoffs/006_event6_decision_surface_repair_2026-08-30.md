# Event 006 decision and mission surface repair audit

Date: 2026-08-30

Owner: Event 006 decision/mission surface subagent

Status: Source audit complete; no safe gameplay patch identified; no Event 006 decision or category source was changed.

## Scope and source basis

This audit covered `common/decisions/006_independence_wave_decisions.txt`, `common/decisions/categories/006_independence_wave_categories.txt`, their Event 006 scripted trigger/effect/localisation consumers, and the accepted Event 006 decision/mission matrix and specification.

The required repository guidance was read from `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The offline Paradox references read for this audit were Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event Modding, Decision Modding, Idea Modding, AI Modding, Interface Modding, and Scripted GUI Modding.

The vanilla references read were `triggers_documentation.md`, `effects_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `loc_objects_documentation.md`, and `loc_formatter_documentation.md`, together with vanilla decision/category examples.

## Outcome and pre-event invariant

The accepted design requires an entirely empty Event 006 decision surface before an active origin exists: no category, mission, pressure, meter, queue, cost, history indicator, or Event 006 GUI entry.

The current category roots preserve that invariant: founding and government require `is_independence_wave_active_country = yes`; recognition and patron require the provisional-or-later gate; network and league require recognized-or-later; borders and formables require regional/progression gates; package categories delegate through package predicates that include the active-origin contract; overlay categories require the explicit runtime-unlocked flag.

The scenario ledger category is success-only and fail-closed: it requires `independence_wave_scenario_committed`, excludes failed/finalization-failed flags, requires the ledger-visible receipt, and requires a positive blocked-package count.

No source-only finding justified adding, removing, or weakening a pre-event gate, so no category or decision patch was made.

## Issues sorted by severity

### P1: DM-55 has a method-dependent formable commit cost with more than four real spendable groups for three methods

Identifier: `independence_wave_proclaim_military_union` (DM-55) in `common/decisions/006_independence_wave_decisions.txt:3533-3556`.

The decision uses `custom_cost_text = independence_wave_cost_selected_formable_commit`, checks `can_pay_independence_wave_selected_formable_commit_cost`, and executes `independence_wave_formable_pay_selected_commit_cost`.

The trigger in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:1490-1516` and payment effect in `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:2505-2530` are aligned: negotiated, dynastic, and league methods pay the strategic plus administration-standard palettes; revolutionary pays strategic plus security-standard; military and hidden-high-chaos methods pay strategic plus security-major.

The scripted localisation selector `GetIndependenceWaveFormableCommitCostText` in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:1313-1330` selects civic, revolutionary, or military text from `localisation/english/006_independence_wave_formable_registry_l_english.yml:27-30`.

The civic branch has four normalized spendable groups: stability, command power, one transport alternative (convoy or train), and manpower.

The revolutionary and military/hidden branches have seven normalized spendable groups: stability, command power, one transport alternative, manpower, army experience, infantry equipment, and support equipment.

These are not presentation-only extras: the trigger and payment effect genuinely require and consume the corresponding composite palettes, and the accepted formable contract retains method-specific transaction costs.

There is no accepted matrix or source contract authorizing removal of the strategic or security components, and reducing the display alone would make the decision tooltip diverge from availability and payment behavior.

Therefore this is an unresolved design/localisation issue, not a safe decision-file simplification; the parent and design/localisation owners must explicitly approve a revised payment palette before any gameplay, trigger, effect, and localisation change.

### P1: Status scripted GUI has production inspection diagnostics outside this gameplay scope

The required read-only `hoi4.gui_inspect` for `independence_wave_status_window` completed with 48 inspected elements and no missing/unresolved elements, but reported 64 non-blocking visible-overlap findings, floating-point icon clipping, and missing static fallbacks for four animated seal/dependency assets.

The status render completed at 1920x1080 and 1366x768 across the required state matrix, but the MCP response was wire-truncated and returned `validation passed = false`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af9686ba85271998f10aca03ee67df48d6b5f9568d3704a73691d567af575d2e/64c070934c084a2d072d8e630f1e5ca78ff01b7394f753d4c480e60ddfb8bd2a/independence_wave_status_window-full.svg`.

This subtask owns decision gameplay and cannot edit the interface or assets; the GUI owner should route the overlap, clipping, and static-fallback findings through the event-owned GUI workflow.

### P2: IW095 factory reservation is a fifth visible icon but not a fifth consumed spendable group

Identifiers: `iw095_organize_civic_guard` and `iw095_authorize_emergency_directorate` in `common/decisions/006_independence_wave_decisions.txt:4065-4082` and `4231-4248`.

Both use `independence_wave_cost_security_standard_factory`, whose read-only localisation has four consumed groups (manpower, army experience, infantry equipment, and support equipment) plus a separate civilian-factory `Commit` reservation.

The IW095 package contract intentionally grants a zero factory floor and reserves one factory through the decision modifier; the factory is not an additional consumed resource payment in the security palette.

No gameplay change is safe here; the localisation owner may re-layout the separate `Spend` and `Commit` lines if the visual four-type policy is interpreted as an icon-count policy, but that is outside this subtask and must not hide the reservation.

### P2: Static declaration counts require runtime candidate-pool proof before any category pruning

The source contains five founding decisions, six government decisions, six recognition decisions, seven security decisions, and several package/formable blocks with 10-23 declarations.

Phase, setup, project-ready, identity, current-generation, invitation, cooldown, active-mission, and route predicates gate those declarations; declaration count alone does not prove simultaneous visibility.

The accepted design requires no more than six visible primary actions and no more than three active missions without a documented reason, but no safe source-only deletion or merge can be selected without runtime candidate-pool evidence and accepted design ownership.

### P2: Mandatory probability-auditor route is unavailable in this runtime

The required `chaosx_ai_probability_auditor` route is not callable/exposed in this runtime; only generic HOI4 probability tools are available.

No quantitative AI balance or probability claim is made here, and no AI weight was changed.

### P2: Decision-specific MCP inspection route is unavailable

No callable `hoi4.decision_inspect` route is exposed in this runtime; the available mandatory GUI routes inspect the linked scripted windows, not the standard `countrydecisionview` decision list.

The decision source, triggers, effects, and vanilla decision documentation were audited statically, but that is not claimed as equivalent engine evidence for decision-candidate ordering or simultaneous list density.

## Decision category lifecycle notes

The founding category is visible only for `is_independence_wave_active_country` and retains its status scripted GUI entry without a pre-event category.

Government and security follow the active-origin gate; recognition and patron follow provisional-or-later; network and league follow recognized-or-later; borders and formables follow regional power plus their explicit unlock/transaction gates.

Package categories require the package predicate and setup-complete flag, while overlay categories additionally require `is_independence_wave_overlay_runtime_unlocked` and an active overlay.

Invitation and post-formation categories use pending-invitation, autonomous-member, active-progression, or post-formation carriers rather than a generic always-visible warehouse.

The IW095 category requires the package predicate, setup receipt, identity-rights clearance, and current-generation force package; its package predicate includes active origin, exact package id, Event 006 liberation origin, and exclusion checks.

The scenario ledger is a public success receipt, not a pre-event pressure or queue surface.

## Cognitive-load audit

Visible primary actions are phase- and package-gated in source, and the current roots do not expose the full declaration inventory simultaneously by default.

The founding route has five founding missions, and the source has active-mission locks and mission-cap triggers for founding, diplomatic, security, and league-crisis work; the matrix’s founding durations and sequencing remain intact.

The category descriptions expose legitimacy, recognition, capacity, security, and instability only behind the active/provisional lifecycle gates; no pre-event value dump was found in the decision categories.

The status scripted GUI inspection found a structurally reachable 48-element surface, while the formable state-puzzle inspection found a 93-element surface with no local overlap or blocker.

The formable puzzle render completed with 14 states, two resolutions, five variants, zero changed pixels in its comparison artifact, and validation passed; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f62af8876d463158e58357ba1ea513b8702e60f9c3286d2bf5faa292449f121/59dd5aff885022a9fc3c49de1ebdb93fb5b755cf249d18fd8410add64c368ace/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The formable commit cost remains cognitively dense for revolutionary and military/hidden methods because it exposes seven actual spendable groups; hiding one would create a misleading availability/payment surface, so the design decision must precede implementation.

## Mission quality notes

The accepted founding mission set is DM-01 through DM-05, with the decision matrix’s duration bands, sequencing, active-mission caps, and package/phase gates preserved.

DM-01 uses the founding-entry gate and reservation/cost disclosure before activation; the source includes cancellation/timeout handling and completion cleanup through the existing Event 006 helpers.

DM-02 through DM-05 are phase- and flag-gated follow-on missions, and the source includes active-mission locking rather than presenting all mission families as unrelated simultaneous actions.

DM-06 through DM-62 and package missions use target, project-ready, identity, setup, current-generation, cooldown, and route checks where applicable; target triggers validate existence, country identity, control/ownership, relation, generation, and war-state constraints.

No new mission, duration, target, success, failure, or cleanup change was justified by this audit, and no duplicate mission loop was added.

## Cost and requirement clarity

A read-only Event 006 custom-cost scan resolved all direct Event 006 `custom_cost_text` keys; the only direct fixed localisation with more than four icon types was `independence_wave_cost_security_standard_factory`.

That key uses `£manpower_texticon`, `£army_experience`, `£infantry_equipment_text_icon`, `£support_equipment_text_icon`, and a separate `£civ_factory` reservation line; it contains no literal resource-name substitute.

The indirect `independence_wave_cost_selected_formable_commit` key resolves through scripted localisation, so it was audited by following its method selector and payment effect rather than by treating the wrapper key as a flat string.

All inspected spendable values use texticons; no source patch was made because the seven-group formable branches are real payment requirements and the IW095 factory is an explicit reservation.

## AI validity and route-lock notes

The inspected target gates use existence, self-target exclusion, war-state, relation, control/ownership, generation, and package/route constraints; no invalid target or dead-country relaxation was introduced.

DM-55 AI selection remains behind `has_independence_wave_formable_commit_readiness` and the existing profile/route checks, with the existing instability and route-avoidance modifiers retained.

No AI weight was changed because the mandatory custom probability-auditor route is unavailable and no source-backed balance target was supplied.

## Localisation and tooltip gaps

No localisation file was edited, per task boundary.

The formable cost strings are icon-first and method-specific, but the revolutionary and military/hidden variants remain longer than the four-group cognitive-load target; this requires an accepted gameplay palette decision before localisation can be safely shortened.

The IW095 strings clearly separate `Spend` from `Commit`; any future presentation cleanup must preserve the factory reservation and all four consumed security groups.

The standard decision GUI was not MCP-inspected because no decision-specific route is exposed; tooltip readability therefore has only source and localisation evidence in this audit.

## Cleanup and exploit-risk notes

Existing Event 006 mission and package flows retain cancellation/timeout, current-generation, cooldown, active-mission, invitation, and stale-target cleanup gates; no cleanup hook was altered.

The formable commit decision remains `fire_only_once`, blocks commit-pending and active-formable states, and pays through the single method-dispatched effect, limiting duplicate commit loops.

The scenario ledger remains success-only and fail-closed, and no pre-event queue or pressure store was added.

## Required follow-up

The parent should treat the DM-55 seven-group revolutionary/military/hidden transaction as an explicit design decision: either accept the current method-specific composite cost despite the four-group UI policy, or obtain an approved revised palette and update trigger, payment effect, scripted localisation, and decision tooltip together.

The localisation/GUI owners should resolve the IW095 `Spend`/`Commit` presentation question and the status-window overlap, icon-clipping, and static-fallback diagnostics without weakening gameplay gates.

No plan handoff for new mechanics was written because this audit found no safe local implementation; the remaining work is an owner-level design/UI decision rather than an authorized fallback.

## Validation and skipped validation

Task-specific validators completed successfully: `.tools/audit_event6_allocator.py`, `.tools/audit_event6_country_api.py`, `.tools/audit_event6_flags.py --strict`, `.tools/audit_event6_form16.py`, `.tools/audit_event6_gui_matrix.py`, and `.tools/audit_event6_scenario_matrix.py`.

The allocator validator explicitly reports the retired pre-event crisis surface with no category, mission, cost, or queue; the other validators report complete Event 006 flags, country API, FORM-16, GUI semantic matrix, and SCN-008 matrix contracts.

Required GUI evidence was collected for `independence_wave_status_window` and `chaosx_independence_wave_formable_state_puzzle_window` through read-only `hoi4.gui_inspect` and `hoi4.gui_render` calls; the artifact references and status-render truncation are recorded above.

Live HOI4 execution was not performed because repository guidance forbids agents from launching the game; live consumer validation remains with the user.

The standard decision-specific MCP inspector and `chaosx_ai_probability_auditor` were not available in this runtime, so decision-list runtime density and quantitative AI probability evidence remain unclaimed.

## Changed files and identifiers

Gameplay files changed: none.

Localisation files changed: none.

Assets or interface files changed: none.

Documentation added: this handoff only.

Decision identifiers reviewed: DM-01 through DM-62, `independence_wave_proclaim_military_union`, and the IW095 decision family, with category lifecycle gates reviewed across the Event 006 category file.

Simplifications, fallback content, package-gate relaxations, and unrelated-event edits: none.
