# Event 006 formable and state-puzzle contract audit — 2026-08-29

## Disposition

This bounded audit covers the Event 006 formable decision surfaces, their state-puzzle consumers, and the matching registry triggers, effects, and localisation. The source review found one safe, source-backed localisation correction and several owner-level follow-ups. No new formable family, admission route, flag, portrait, icon, or GUI surface was invented.

## Changed files and identifiers

- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `independence_wave_formable_commit_cost_civic`

Before this change, the civic/dynastic/league commitment row displayed the standard 20 command-power token while the effect paid strategic command power and standard administration command power, for the central civic commitment of 40. The row now uses `constant:independence_wave_formable_cost.civic_command_power`, displaying 40 and matching the trigger, effect, and registry constant. No gameplay effect or gate was changed.

## Issues sorted by severity

### P1 — revolutionary and military commit rows expose seven spendable cost types

`independence_wave_formable_commit_cost_revolutionary` and `independence_wave_formable_commit_cost_military` display stability, command power, a diplomatic transport alternative, manpower, army experience, infantry equipment, and support equipment. The matching trigger in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:1490-1516` checks strategic plus security-standard or security-major payment, and the effect in `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:2505-2529` pays those same resource groups. This is internally consistent but violates the four-distinct-spendable-cost ceiling for a gameplay-changing decision.

There is no accepted source contract selecting which four resources to retain. Reducing the row or payment would therefore change method intent and could make the trigger, payment effect, and tooltip disagree. This remains an owner design decision: specify a four-group method palette or split the commitment into bounded phases, then update the trigger, effect, localisation, and required probability comparison together. No speculative patch was made.

### P2 — generic commit checks civilian-factory capacity without reserving or displaying it

The shared commit decision in `common/decisions/006_independence_wave_decisions.txt:3518-3547` delegates availability and cost text to the selected-formable helpers. `can_pay_independence_wave_selected_formable_commit_cost` also checks the standard civilian-factory capacity through the strategic-cost helper, but the decision has no local `civilian_factory_use` modifier and the dynamic commit row does not show that requirement. This is outside the owned decision files and should be classified by the parent as either a clearly labelled capacity requirement or a real reservation. Do not silently add a factory payment in this bounded audit.

### P2 — terminal transaction failure may leave the shared transaction category visible

`independence_wave_formable_transaction_category` in `common/decisions/categories/006_independence_wave_categories.txt:253-262` is gated by regional power, discovery, profile match, and not-active status, but does not visibly exclude `independence_wave_formable_transaction_failed`. The invitation helper rejects a failed transaction in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:1136-1149`. This may be intentional for a retry path, but the category can present method and consent selectors after a terminal failure unless cleanup removes the selected profile or the category gains an explicit retry gate. The category file is outside this worker's ownership; parent review is required.

### P3 — current production GUI and weighted balance evidence are unavailable

The required `hoi4.gui_inspect`, `hoi4.gui_render`, `hoi4.probability_inspect`, and `chaosx_ai_probability_auditor` routes are not present in this subagent's tool catalog. The existing source-of-truth map and prior handoffs contain historical shared state-puzzle evidence, but that is not a current production render or probability comparison. No visual fidelity or weighted-balance completion claim is made here.

## Registry and state-puzzle crosswalk

The 48-row registry in `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv` is distinct from the currently admitted runtime families. The 14 runtime-authored Event 006 state-puzzle families are FORM-01, FORM-02, FORM-03, FORM-04, FORM-05, FORM-07, FORM-08, FORM-09, FORM-12, FORM-13, FORM-16, FORM-18, FORM-39, and FORM-48. The other 34 rows remain deliberately fail-closed: FORM-06, FORM-10, FORM-11, FORM-14, FORM-15, FORM-17, FORM-19, FORM-20, FORM-21, FORM-22, FORM-23, FORM-24, FORM-25, FORM-26, FORM-27, FORM-28, FORM-29, FORM-30, FORM-31, FORM-32, FORM-33, FORM-34, FORM-35, FORM-36, FORM-37, FORM-38, FORM-40, FORM-41, FORM-42, FORM-43, FORM-44, FORM-45, FORM-46, and FORM-47.

The matching manifests under `docs/formables/state_puzzles/` and `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt` agree for the 14 admitted families. FORM-03 uses exact AFX/AGX anchors plus the frozen Belgium delegation state; FORM-05 uses exact COR/ARX/ASX anchors and current-capital checks; FORM-16 uses ARM/GEO/AZR states 230/231/229; FORM-48 uses HBX/HAW/FSM states 378/629/684 and remains readiness/FSM-gated. FORM-08 intentionally remains fail-closed: states 82 and 84 are known, the registry requires three states, and its state-puzzle helper is `always = no` until a third researched member or anchor is admitted.

## Decision-category lifecycle notes

There are 17 current Event 006 formable-related decision categories attached to `independence_wave_formable_state_puzzle_scripted_gui`. The 14 runtime families use the grouped state-puzzle presentation, while the IW043, IW058, and FORM-16 categories retain their own lifecycle gates within the same attachment policy. Pending founding invitations take precedence over selected-profile and post-formation views.

The discovery category requires Event 006 recognition and `independence_wave_unlock_formable_discovery`; source review found no setter that exposes it before the active event path, and cleanup clears the unlock. Membership, congress, charter, federal-compact, and post-formation categories are gated by family-specific readiness, exact anchors, connected routes, identity clearance, admission policy, live member checks, and phase flags. FORM-05 uses its custom charter invitation path and does not duplicate the generic membership response category. FORM-48 remains unreachable until its readiness/FSM contract is admitted.

## Cognitive-load notes

Visible primary actions are phase-gated. The shared membership category has at most three responses; FORM-01, FORM-02, and FORM-04 serialize congress actions behind one active project; FORM-03 serializes language, corridor, industrial, charter, and membership work; FORM-05 serializes charter articles and post-formation board work; FORM-48 presents one carrier phase and one member response phase. The transaction category has six method selectors, three consent-rule choices, and one invitation action, which is at the six-action ceiling but is not simultaneously mixed with the phase categories.

Timed objectives use explicit `activation = { always = no }`, hidden availability, timeout/failure effects, and cancellation when the active carrier, member, session, or obligation disappears. No state-puzzle overlay creates an additional mission. The grouped GUI exposes finite qualifying/unresolved state counts and required counts rather than an unbounded raw state dump; FORM-08's 2-of-3 mismatch is meaningful because it explains its fail-closed state.

Current source review shows each displayed state summary has a corresponding territory helper and each decision availability reuses the family contract. A current production render was not available, so clipping, spacing, font overflow, asset loading, and click-region behavior remain unverified.

## Mission quality notes

The state-puzzle surface itself owns no missions. FORM-01/02/04 first-stage congress missions, FORM-05 charter and first-board deadlines, and FORM-48 carrier-cycle deadlines are single-owner, category-specific, and guarded by active-stage flags. They specify owner, region/family, requirement, duration, timeout/failure, and cancellation conditions in the matching decision/effect files. Active-project checks serialize duplicate phases. No duplicate mission or stale active deadline was proven in the source audit.

## Cost and requirement clarity

The five owned decision files reference 46 custom cost localisation keys. The English definitions are present, spendable resources use texticons, and the dynamic transport helper displays convoy or train as the applicable alternative. FORM-01/02/03/04/05/08/09/12/13/16/18/39/48 decision rows stay within the four-group palette when counted by displayed spendable categories. The generic selected-formable civic row is now also internally correct and displays the central 40 command-power requirement.

The revolutionary and military selected-formable rows remain the sole known over-budget exception in this surface, with seven distinct spendable categories each. This is a design blocker rather than a safe localisation-only defect because the payment effect consumes all seven categories. Non-consumed requirements such as capital control, peace, identity, admission, route, and factory capacity are represented by availability triggers rather than falsely added to the cost string.

## AI validity and route locks

AI and human paths share the same family availability/readiness helpers for the admitted state-puzzle families. Exact state ownership/control, current-capital safety, peace/route connection, invitation generation, frozen consent, identity compatibility, member admission, and post-formation integration gates are retained. FORM-16's static contract validator confirms ARM/GEO/AZR membership, consent/refusal, mutation, receipt, rollback, and cleanup gates. FORM-48 retains its HBX/HAW/FSM autonomous-membership and FSM readiness locks.

No AI weight or probability-bearing value was changed. A probability baseline/compare is still required through the unavailable MCP route before any balance patch to method selection or AI pursuit is considered.

## Localisation and tooltip gaps

The 46 referenced custom cost keys have English definitions, and all spendable values are icon-first. `independence_wave_formable_commit_cost_civic` was corrected as described above. Dynamic transport text remains delegated to the existing scripted localisation helper. The over-budget revolutionary/military rows need an accepted method-specific palette before tooltip text can be safely simplified. State-puzzle summary and decision requirement text are source-aligned; current production overflow and click-region evidence is blocked by missing GUI MCP routes.

## Cleanup and exploit-risk notes

The state-puzzle overlay is presentation-only and owns no persistent flags, variables, effects, or costs. Registry cleanup clears selection/profile, invitation/proposal, member arrays, commit/active flags, and associated variables. FORM-16 and FORM-48 also have explicit rollback and cleanup receipts. The admitted formable effects do not create a free equipment, core, or war-goal loop in this audit. FORM-08 and FORM-48 remain fail-closed where their contracts are incomplete or FSM-gated.

The only cleanup concern requiring parent review is the possible visibility of the shared transaction category after `independence_wave_formable_transaction_failed`, described above. No stale state-puzzle state was found.

## Validation

The following focused checks were rerun after the localisation correction and all passed:

- `python -B .tools/audit_event6_allocator.py` — allocator ordering, package reservations, admitted/adapter-only counts, and pre-event crisis retirement passed.
- `python -B .tools/audit_event6_scenario_matrix.py` — 32 SCN-008 cells and 8 edge cases passed.
- `python -B .tools/audit_event6_form16.py` — FORM-16 carrier, exact states, consent, mutation, rollback, cleanup, and readiness passed.

No Hearts of Iron IV process was launched. GUI inspect/render and probability inspect/compare were not run because those MCP routes are not exposed in this environment; this is an explicit evidence blocker, not a validation pass.

## Simplifications, omissions, and blockers

No broad simplification, fallback, placeholder, generic admission, or new family was introduced. The 34 unadmitted registry rows remain fail-closed by design. The seven-type revolutionary/military cost issue was not patched without an accepted four-group method contract. The factory-capacity presentation/consumption ambiguity and failed-transaction category visibility were not changed because their canonical decision/category owners are outside this bounded surface. Current GUI visual and weighted probability evidence remain pending parent/tool availability.

No separate plan was written because the safe correction is one line and the remaining changes require owner design decisions rather than an implementation plan from this worker.
