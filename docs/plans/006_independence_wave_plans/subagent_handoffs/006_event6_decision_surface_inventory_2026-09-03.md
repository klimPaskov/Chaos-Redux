# Event 006 decision-surface inventory — 2026-09-03

## Disposition

This is a read-only decision and mission audit against the accepted Part 3 map and the current consolidated registries.

No gameplay, localisation, category, GUI, or balance source was changed, and no commit was made.

The accepted map is structurally represented: the implementation receipt records 80/80 rows, 80 definitions, 80 visibility-or-activation gates, 80 availability gates, 80 AI blocks, and terminal lifecycle markers; the current decision source contains DM-01 through DM-62, while the FORM03 source and prior receipt cover FORM03-D01 through FORM03-D18.

No safe narrow source patch was proven during this pass.

## Severity-sorted issues

### P1 — DM-03 registration does not express the accepted anchor and local-peace requirements

The accepted row in docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv requires control of the anchor territory, maintenance of local peace, and administration expenditure for Register population.

common/decisions/006_independence_wave_decisions.txt (independence_wave_register_population, DM-03) currently gates activation on active-origin state, completion of DM-02, the light administration cost, absence of terminal flags, and absence of another founding mission.

Its cancellation checks active-origin state, loss of the capital, and severe instability, but it does not check independence_wave_anchor_state or a named local-peace condition.

The shared trigger registry common/scripted_triggers/006_independence_wave_decision_triggers.txt has no DM-03-specific anchor/peace helper, although independence_wave_anchor_state is established by common/scripted_effects/006_independence_wave_effects.txt during origin preparation and is used by other package checks.

The available = { always = no } and non-selectable shape is not by itself an error: vanilla common/decisions/NORDIC.txt uses this pattern for an automatically activated, expiring mission.

This is therefore a source-to-map requirement gap, not proof that the mission must become player-selectable.

Recommended owner fix: define the intended local-peace scope in a named trigger, require the anchor state to be owned and controlled by the active origin, and apply the same condition to the activation/cancel/tooltip contract as appropriate.

Do not patch this locally until the owner resolves whether local peace means no country war, no war in the anchor state, no active resistance escalation, or another package-defined condition; each choice changes gameplay and cancellation semantics.

### P1/P2 — Formable revolutionary and military commit costs exceed the four-type clarity limit

common/decisions/006_independence_wave_formable_decisions.txt and localisation/english/006_independence_wave_formable_registry_l_english.yml (independence_wave_cost_selected_formable_commit) expose seven distinct spendable groups for the revolutionary and military variants: stability, command power, dynamic transport, manpower, experience, infantry equipment, and support equipment.

The decision-mission skill requires no gameplay-changing decision or GUI action to expose more than four distinct spendable cost types.

The cost is a shared formable transaction with payment effects and dynamic selector logic, so reducing it safely requires an owner decision about which costs remain and how trigger, payment, and localisation stay aligned.

Recommended owner fix: select at most four spendable groups per formable route, keep the dynamic transport helper where the route requires it, and update the trigger, payment, blocked tooltip, and cost localisation as one bounded formable transaction.

### P2 — Mandatory GUI evidence shows unresolved shared-surface defects

The fresh Statehood Ledger inspection of independence_wave_status_window passed source-graph validation, but the production render reported GUI_TAB_STATE_CONFLICT, including simultaneous instability warning/value and tab-state visibility, plus incomplete state coverage.

Inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ae4e1fa9f02044b5b385e2a8440f199d217cebf5cbed71696f25a2844cde82d/11c4beba8ae4e8aca2cb3d07c4a4c67d06f9f2125b141346eef3412de6c791a5/gui-inspect.d45e4d124f3c3692.json.

Render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c897ae755def1b32e4005965b40c873289e545d6b50b4996b46762b7b4336c1/82c2f5908aef4a1821a275527b3786b4c2c5fd2ce04c5e8e480a0f726a9de6cf/independence_wave_status_window-full.svg.

The formable state-puzzle inspection passed source-graph validation, but its static projection reported zero-size form01/form02 summary and piece widgets with clipping/invalid-size warnings.

Formable inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10ee5a34fdf9ea7e932517f8da5bc3091c25c54a37c716262f271b0f9ef2e26b/3b620cc7157d9ad37df771adfbb5699c153aa03cc1eb322a7e01e1569aebb71f/gui-inspect.b7b64e749ebb06be.json.

Formable render artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d202974f6702e6d78f473c71dc4a53874a21ba0aa6996197805f8fa63c769756/2953b55b46b9e5dfb207c7b668de50cf3d30ac1a59f825f7f21fbc91e8686fe3/chaosx_independence_wave_formable_state_puzzle_w-full.svg.

These are GUI-owner surfaces and were not rewritten here because this task owns decision semantics, not a shared or dedicated layout implementation.

### P2 — Weighted AI evidence is incomplete

The required chaosx_ai_probability_auditor route is not callable in this environment.

Existing direct MCP recovery evidence in docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_probability_mcp_recovery_2026-09-02.md covers a random-list inspection and a bounded evaluation against an empty fixture, but it does not provide named campaign scenarios or a probability_compare result.

The empty fixture produced zero available candidates and unresolved rows, so it cannot support a balance claim about decision or mission selection.

Recommended owner follow-up: run the auditor with named peace, war, low-legitimacy, high-chaos, and target-validity scenarios, then compare before and after only if a weighted source patch is proposed.

### P2/P3 — Cleanup coverage needs an owner-level timer inventory

common/scripted_effects/006_independence_wave_decision_effects.txt central cleanup removes the listed active missions and many Event 006 flags, including DM-01, DM-02, DM-03, DM-04, DM-05, DM-10, DM-17, DM-20, DM-23, DM-30, DM-15, DM-35, DM-45, DM-54, DM-58, and DM-59.

Other ordinary decisions rely on their own cancellation and timeout contracts, so the central cleanup is not proof that every package-owned timer and target is removed after origin invalidation.

Recommended owner follow-up: inventory every ordinary decision with an active timer, target pointer, timed flag, or mission-like state and verify its package cleanup hook, target death/ownership cancellation, and post-failure lock.

No free payout, repeated completion, or cooldown exploit was proven by this source audit, but the timer inventory remains an evidence gap.

### P3 — League display remains numerically dense

The league category presents eight numeric values in its current surface, while the decision skill recommends a meter, icon state, threshold marker, or other compact state presentation for raw dynamic-number walls.

The prior Event 006 GUI/category audit recorded this as a density concern and the FORM03 phase docket closed the separate child-action density investigation without a patch.

This is a category/GUI design follow-up, not a safe source-only change for this handoff.

## Decision-map and registry coverage

The following sources were inspected: common/decisions/006_independence_wave_decisions.txt, common/decisions/categories/006_independence_wave_categories.txt, common/decisions/006_independence_wave_form03_decisions.txt, common/decisions/006_independence_wave_formable_decisions.txt, common/scripted_triggers/006_independence_wave_decision_triggers.txt, common/scripted_effects/006_independence_wave_decision_effects.txt, common/scripted_effects/006_independence_wave_effects.txt, and the related English cost/localisation registries.

All DM-01 through DM-62 marker blocks are present in the consolidated decision source, although DM-60 through DM-62 precede DM-48 through DM-59 in file order.

The current implementation receipt records all 80 accepted rows, including the 18 FORM03 rows, with title/description localisation and lifecycle markers.

The FORM03 source uses explicit activation, availability, selectable, timeout, cancellation, and terminal effects for its timed project and ratification surfaces where applicable.

## Category lifecycle and cognitive-load notes

The founding category owns the Statehood Ledger scripted GUI and exposes the emergency/provisional capital, revenue, population, assembly, and authority surfaces; the accepted lifecycle moves from origin preparation through provisional administration and then government and recognition routes.

The formable categories own the state-puzzle scripted GUI and keep the FORM03 state projects visually separated from the general Event 006 registry.

The prior FORM03 scenario receipt reports 23 current child actions across 13 complete scenarios and closed the separate density concern; no new FORM03 density patch is recommended here.

The league category remains the clearest visible raw-number concern because eight dynamic values compete for attention without a compact state treatment.

The current source receipt reports 18 timed mission blocks with availability, timeout effects, and cancellation triggers, but DM-03’s accepted anchor and local-peace requirement is not represented in its gate contract.

The source audit did not establish a pre-event player-surface leak after the strict category gates and package setup-complete check were applied; a live save/load check is still outside this audit.

## Mission quality notes

DM-01 has an origin/setup gate, capital-control and reserve-cost checks, a mission activation path, and completion-side payment/reserve behavior.

DM-02 follows DM-01 and uses an administration/economic-anchor lifecycle with terminal success and failure flags.

DM-03 uses administration payment at timeout, one-time success and failure flags, and cancellation deltas, but lacks the accepted anchor-control and local-peace requirement described above.

DM-04 and DM-05 are downstream founding and government objectives gated by the prior founding state and legitimacy and route conditions.

DM-06 through DM-62 and the FORM03 rows are represented by the consolidated receipt and contain the expected lifecycle fields for their decision or mission type; targeted rows require focused owner review for target death, route closure, border validity, and duplicate activation in live scenarios.

## Cost and requirement clarity

The current Event 006 cost audit reports 699 custom-cost consumers and 191 unique keys across 24 files.

Normal custom cost strings have matching normal, blocked, and tooltip localisation triplets, resolve through texticons, and do not spell spendable resource names as literal labels.

The dynamic transport helper is used for route-dependent convoy and train costs, and the legacy cost_security_standard_factory key has no active callers.

The seven-type revolutionary and military formable commit variants remain unresolved exceptions to the four-type limit.

Six native political-power cost rows remain intentionally native and are not evidence of a custom-cost localisation defect.

## AI validity and route-lock notes

The current matrix receipt reports an AI block for every accepted row.

The decision trigger registry contains route, phase, package-setup, target, and cost guards for the consolidated surface, and the latest category-gate handoffs enforce active-origin and adapter boundaries.

The source audit did not find a missing broad active-origin gate in the current category registrations, and no dead-country target was proven from static source review.

Quantitative AI selection and route weighting remain unverified because the named probability auditor route is unavailable and the direct fixture evidence is empty.

## Localisation and tooltip gaps

Current direct cost keys resolve and use icon-first formatting according to the recent localisation audit.

If the DM-03 gate is corrected, its requirement and blocked-state localisation must be updated to explain the anchor and local-peace condition in player terms rather than exposing raw trigger logic.

The formable cost selector must keep its dynamic normal, blocked, and tooltip variants synchronized with any future four-type cost reduction.

## Cleanup and exploit-risk notes

DM-03 is one-time guarded by success and failure flags, pays administration only at timeout when affordable, and applies failure consequences when the payment cannot be made.

The package cleanup effect clears the principal founding missions and flags, but ordinary timed decisions still need a per-id cleanup and target inventory before a complete stale-state claim is possible.

No exploit loop was proven in this read-only pass, and no source change was made that could introduce one.

## Concrete recommended fixes

1. Add an owner-approved DM-03 anchor and local-peace helper and align its activation, cancellation, availability, and dynamic tooltip contract; preserve the vanilla-style automatic mission shape unless the owner explicitly changes that lifecycle.
2. Reduce revolutionary and military formable commits to no more than four spendable cost groups and update trigger, payment, and localisation together.
3. Route the Statehood Ledger and formable puzzle render findings to the GUI owner for state exclusivity, size and clipping, and state-coverage fixes.
4. Run chaosx_ai_probability_auditor with named scenarios and a probability comparison before accepting any AI or weight change.
5. Complete a per-decision timer, target, cancellation, and cleanup inventory, including target death, route closure, and duplicate-activation cases.
6. Revisit the league category’s eight visible values with a compact meter or threshold presentation only through the category and GUI owner.

## Validation and evidence

python -B .tools/audit_event6_allocator.py completed successfully with no allocator diagnostics.

python -B .tools/audit_event6_gui_matrix.py completed successfully for the semantic Statehood Ledger matrix and reported the expected five tab contracts, frame sets, cleanup variables, and static and animated pairs; it does not claim runtime rendering or save and load evidence.

python -B .tools/audit_event6_scenario_matrix.py completed successfully with SCN-008 coverage and eight edge-case receipts.

The mandatory hoi4.gui_inspect and hoi4.gui_render calls were completed for both decision-owned Event 006 GUI surfaces; the artifact references and production-render findings are recorded above.

The offline Paradox wiki core pages, decision and GUI pages, vanilla decision documentation, vanilla effects and triggers documentation, and vanilla NORDIC mission precedent were consulted.

Skipped meaningful validation: no Hearts of Iron IV process was launched, no live save and load or target-death scenario was run, no typed probability comparison was possible without the required worker route, and no GUI rewrite was authorized or needed for this decision-owned audit.

## Changes and blockers

Changed files: only this handoff file.

Changed decision, mission, scripted-GUI, or localisation identifiers: none.

No simplification or fallback was used.

The remaining blockers are owner resolution of DM-03’s local-peace semantics, broad formable transaction ownership for the seven-type costs, GUI-owner follow-up for production render defects, and unavailable chaosx_ai_probability_auditor routing.

