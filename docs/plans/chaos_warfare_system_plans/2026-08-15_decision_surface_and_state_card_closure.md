# CBRN decision-surface and state-card closure

## Later correction

The generic biological supply-chain decision family and the superseded coercive occupation authorization are now invisible migration surfaces. They cannot create new state cards. Covert ordinary-agent deployment uses native operative operations, while Protected Occupation Administration and exact external protective aid remain supported.

Date: 2026-08-15

Status: supported playable core remains source-ready. No additional decision family or scripted GUI is recommended.

## Closure result

The CBRN decision presentation is dormant at new-game startup unless a scenario already contains a live incident or campaign condition that genuinely requires a response. Inherited technologies, facilities, reserves, stockpiles, and doctrine do not grant presentation permission by themselves. Post-start research, doctrine adoption, relevant special-project completion, explicit successor-route activation, or a live alert, contamination, outbreak, evidence record, inspection demand, sanction, or campaign condition reveals only the relevant decision family. Empty categories hide.

The routine protection layer no longer creates one decision card for every controlled state. `cbrn_priority_state_mask_issue`, `cbrn_full_state_mask_distribution`, `cbrn_replace_state_mask_filters`, and `cbrn_supply_occupied_population` are country-level timed programs. Their completion helpers serve only eligible controlled states, preserve the accepted population-scaled stock transactions, serve the capital first where applicable, stop when real mask stock is exhausted, and cancel cleanly if their stock or eligible work disappears.

Exact-state decisions remain only where selecting or responding to a real local state is the mechanic. The retained families cover verified chemical alerts and contamination, supported battlefield objectives, raid staging and arsenal facilities, historically bounded Japan actions, protective occupation measures, forensic evidence, international decontamination, and tracked disease incidents. The generic biological state-card family is disabled, and the state-target audit found no active CBRN predicate that exposes every ordinary controlled state.

All 73 audited Chemical, Biological, CBRN, and Condemnation event definitions remain `is_triggered_only = yes`. No MTTH event or broad daily, weekly, or monthly all-country CBRN pulse was introduced.

## Implementation evidence

- Decision presentation and startup sequencing: `common/scripted_triggers/cbrn_decision_visibility_triggers.txt`, `common/scripted_effects/cbrn_decision_visibility_effects.txt`, and `common/on_actions/chaosx_on_actions.txt`.
- Category visibility: `common/decisions/categories/biowarfare_disease_containment_categories.txt`, `common/decisions/categories/cbrn_diplomacy_categories.txt`, `common/decisions/categories/cbrn_doctrine_categories.txt`, `common/decisions/categories/cbrn_protection_categories.txt`, `common/decisions/categories/chemical_warfare_categories.txt`, `common/decisions/categories/condemnation_sanctions_categories.txt`, `common/decisions/categories/japan_biological_campaign_categories.txt`, and `common/decisions/categories/japan_chemical_campaign_categories.txt`.
- National program cards and cleanup: `common/decisions/cbrn_protection_decisions.txt`.
- Population-scaled national completion: `common/scripted_effects/cbrn_protection_decision_effects.txt` and the existing stock transaction helpers in `common/scripted_effects/cbrn_protection_effects.txt`.
- Post-start reveal hooks: `common/technologies/chaosx_technologies.txt`, `common/technologies/cbrn_regimental_support_technologies.txt`, `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt`, and the Chemical and Biological special-project files.
- Player-facing wording: `localisation/english/cbrn_protection_l_english.yml`.
- Implementation checkpoint: commit `979bc360b`.

The technology and doctrine lint completed with status `ok`, no blocker, and no defect diagnostic. Evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2ce1c76c5a32b0435d555bb957ee3bc1312d1a6c28424cc8f7877e5e4760fb5/816e54205754b3d49cadfc3eb696130dbf7a36b93b3ed95a4c7b599b0a25fff7/technology-lint-27099434a14b.json`.

The decision and mission specialist accepted the explicit startup gate, exact-state bounds, national-program stock and work cancellation, lock cleanup, localisation, and absence of a broad periodic pulse after the focused re-audit.

The required AI comparison ran across the four converted programs and retained differentiated route factors, but the analyzer could not resolve nested controlled-state multiplicity, profile variables, shortage predicates, or factory affordability. The result is partial engine-tool evidence and does not support an exact click probability or rank-preservation claim. JSON evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f106485fa5521637a57c7a5d75d83dfdba36868f3a829fe32565add21389e430/ac5ae6718a0d32783fc386b7e8b9bf67f178824fbf6f7fd0a7a35c2a4f7139a1/probability-abca8d2e92397deb1edbde4a.json`.

## Improvement-loop disposition

Stop broad expansion. The correction makes the existing loop quieter and more legible without reducing exact-state operations. Another general CBRN meter, all-purpose scripted GUI, state-card family, periodic reveal pulse, or decision-store layer would add maintenance and player noise without adding a new choice.

The genuine engine and user-owned limits recorded in `2026-08-09_reward_density_and_bloat_audit.md` remain unchanged. Continuous ordinary-air contamination, unavailable exact ground-condition receipts, the separate legacy selected-state occupation suppression operation, Hardened Mobile Plant, receipt-dependent skipped achievements, and live in-game consumer validation remain disclosed omissions. The generic biological state-card family is retired as unnecessary bloat. No estimator, proxy target, neutral condition receipt, random-state fallback, or broad periodic pulse was introduced.
