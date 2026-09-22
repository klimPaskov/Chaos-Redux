# Biological project lifecycle integration handoff

Disposition: implemented for the bounded lifecycle helpers; weighted MCP scenario coverage remains unresolved.

The parent authorized the four biological project outputs and a shared 50% ceiling for additional hazard-treatment benefits on 2026-09-20.
This handoff describes the bounded changes in `common/scripted_effects/biological_lifecycle_effects.txt`; the parent owns final cross-system integration and completion claims.

## Runtime contract

The state-scoped lifecycle reads the outbreak agent and the state's `CONTROLLER`, then consumes the country wrappers `cbrn_project_has_vaccines`, `cbrn_project_has_field_antibiotics`, `cbrn_project_has_regenerative_serum`, and `cbrn_project_has_antiserum`.
Mass Vaccine Production uses each pathogen's `cbrn_project_effect.vaccine_*_susceptibility_multiplier` for growth, spread, and new exposed share; an active Smallpox vaccination program takes precedence over the project Smallpox susceptibility factor.
Field Antibiotics uses the bacterial `cbrn_project_effect.antibiotic_*_mortality_multiplier` for Anthrax, Plague, and Tularemia only, and yields to an active agent-specific antibiotic course so the same treatment is not compounded twice.
Regenerative Serum uses `cbrn_project_effect.regenerative_recovery_multiplier` on medical contributions to intensity decline, exposed-share clearance, and medical-saturation recovery, with no instant cure.
Broad-Spectrum Antiserum uses `cbrn_project_effect.antiserum_emergency_mortality_multiplier` only with an active agent outbreak and either a deployed field hospital, an international medical mission, or positive controller medical capacity plus support-equipment stock; it makes no extra resource debit.
The existing exact-state scheduled event tick remains the only processing path, and the patch adds no world-periodic hook.
The native raid owner sets `bio_native_raid_dispatch_in_progress` on the saved actor only around a synchronous deliberate seed dispatch and clears it afterward.
The shared integrated-operations command-power recovery helper checks that the actor lacks this flag, preventing a second reward for native raids while preserving recovery for existing non-native deliberate and doomsday routes.

## Shared treatment budget

The foundational snapshot preserves the existing active Anthrax, Plague, and Tularemia antibiotic-course multipliers and the Smallpox vaccination-program multipliers.
Quarantine growth and short-term mortality, field hospitals, project effects, high-response thresholds, historical medical advisors, and mobile casualty sorting are applied after that snapshot.
The final growth, mortality, and medical-load multipliers cannot fall below the corresponding foundational multiplier times `constant:cbrn_hazard_budget.residual_floor` (0.50).
The spread helper snapshots the pathogen-specific foundational chance after intensity, doctrine, and environment pressure, then carries repeated-seeding pressure into that snapshot. The final chance cannot fall below half that foundation after source quarantine, project vaccination, threshold response, captured-facility containment, border controls, direct containment response, and target quarantine.
The detection helper snapshots agent, intensity, saturation, concealment, wartime, and environmental detection before response benefits. Surveillance, Medical Response, threshold bonuses, quarantine, and Distributed Surveillance together cannot remove more than half the foundational missed-detection chance. The original absolute 5% to 95% chance clamp still applies.
Moving mobile casualty sorting into `bio_medical_countermeasure_mult` before the floor preserves its original medical-load arithmetic when the floor is not reached.

Source scenarios: untreated bacterial mortality with hospital, advisor, Field Antibiotics, and antiserum would be `0.80 × 0.85 × 0.78 × 0.88 = 0.466752`; the mortality residual becomes 0.50.
An Anthrax course with its foundational 0.45 mortality residual and hospital, advisor, antiserum, and high medical response would be `0.45 × 0.80 × 0.85 × 0.88 × 0.50 = 0.13464`; the preserved foundation permits a final residual of `0.45 × 0.50 = 0.225`.
Smallpox with its foundational 0.45 vaccination residual, vaccine-scale designer, hospital, advisor, antiserum, and high medical response would be `0.45 × 0.85 × 0.80 × 0.85 × 0.88 × 0.50 = 0.114444`; the final residual is 0.225.
Field hospital, advisor, and mobile sorting yield medical load `0.75 × 0.85 × 0.85 = 0.541875`, so the floor does not alter that scenario.
The Smallpox program's foundational growth residual is 0.65; quarantine, vaccine-scale designer, surveillance, containment, and medical response can lower it to about 0.2536, so the additional-treatment floor sets it to 0.325.
The source spread scenario at Smallpox intensity 20 has an unmodified `55 + 20 × 0.35 = 62` chance before doctrine and environment, and the Smallpox program's foundational 0.65 spread multiplier makes that 40.3.
High containment response, its direct remaining-response factor at response 80, captured-facility mobile containment, and target quarantine would then make `40.3 × 0.50 × 0.60 × 0.85 × 0.50 = 5.13825`; the requested additional-treatment floor would be `40.3 × 0.50 = 20.15` before the absolute 80% chance cap.
The final floor raises that example's chance to 20.15 before the absolute 80% spread cap. These are source arithmetic checks, not game-runtime or MCP scenario results.

## Helper map and lifecycle ownership

`bio_lifecycle_prepare_environment_and_countermeasure_multipliers` is a state-scope temporary-value helper called from exact-state activation and ticks. It reads `bio_active_agent`, state response flags, and the controller's projects and designers; it emits foundational and final growth, spread, death, medical, susceptibility, and recovery multipliers plus separate environmental and response detection additions. It has no durable flag or event-target writes.

`bio_lifecycle_calculate_current_agent_spread_chance` is a state-scope chance helper called only after `bio_lifecycle_select_spread_target` found a valid neighbor. It reads the current agent's intensity, doctrine and repeat-seed record, prepared multipliers, and saved source/target country and target state event targets; it emits `bio_spread_chance` and `bio_no_spread_chance` for the immediate `random_list`. It adds no durable record; a selected spread branch alone calls `bio_lifecycle_seed_selected_spread_target`.

`bio_lifecycle_attempt_detection_for_current_agent` is a state-scope scheduled chance helper. It reads the current agent record, prepared response, state environment, and controller designer; it emits `bio_detection_chance` and `bio_no_detection_chance` for its immediate `random_list`. Only the selected detection branch persists a detection flag and evidence through `bio_lifecycle_mark_current_agent_detected`.

`bio_lifecycle_grant_integrated_operations_release_command_recovery` is a state-scope seed helper. It reads the saved `bio_seed_actor`, seed-source proof, and transient actor flag. It grants the existing Command Power recovery only to a valid deliberate or doomsday actor outside the synchronous native raid dispatch. It does not set or clear the actor flag itself.

No new helper declaration, script constant, persistent variable, event target, or periodic hook was added. The existing `constant:cbrn_hazard_budget.residual_floor` at 0.50 is the sole tuning source for this additional-benefit budget. Existing regular `bio_spread_*` and `bio_seed_*` event targets stay inside their effect chains; no global event-target cleanup is needed. The six native actor flag set/clear pairs remain owned by their calling effect files. There is no migration of unrelated call sites: the existing tick and dispatch calls consume the revised helpers in place.

## Validation and unresolved work

All four wrapper definitions and nine project effect constants were found in the corresponding project files, and the shared budget constant exists in `common/script_constants/cbrn_system_constants.txt`.
The edited lifecycle file has balanced script braces and a clean targeted `git diff --check` result; the arithmetic and state/controller paths were reviewed against the installed vanilla documentation and the offline wiki.
The native-raid command-power guard was source-checked against the exact `bio_seed_actor` event target and synchronous flag set/clear pairs in `biological_raid_effects.txt` and `biological_sabotage_raid_effects.txt`.
The first `hoi4.event_inspect(mode = state_flow, selector = { kind = event, eventId = cbrn_bio_lifecycle.11 })` and `hoi4.probability_inspect(adapter = random_list, source = biological_lifecycle_effects.txt)` calls each timed out after 180 seconds, so neither call produced engine evidence.
The prior event inspection timed out, and a renewed narrow `hoi4.event_inspect(mode = state_flow, selector = { kind = event, eventId = cbrn_bio_lifecycle.11 }, maxDepth = 2, maxEdges = 40, maxNodes = 40, expandHelpers = false)` returned `INTERNAL_ERROR` with blocker `Unexpected internal error` and no artifacts. This is an unavailable MCP event route, not equivalent event engine evidence.
The read-only probability baseline inspected both `random_list` pairs and evaluated the named scenario set `cbrn_bio_random_baseline_20260920`. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-fee0d3723aa1846277bd7634`, source revision `58508b19508d18619f1b00529f2069530b21f598b627585b48fe2f32095ba04a`, three scenarios, six candidates, and two unresolved findings. The baseline artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f0209593ae6a1148f6df1f5f2d0e7b1574694cc2a541eb252222bdf6fb40e4a/0e72321f6f410d2632be46b147c19d3c4dae1a48cd2e6e51f9440c8ae1b3a07a/probability-fee0d3723aa1846277bd7634.json`. Direct weights were 12.75/87.25 for the high-response Smallpox spread scenario, 50/50 for high-response detection, and 55/45 for low-response spread. Source-derived factors and target validity remained unresolved, so these figures are bounded inspection outputs, not complete in-game probabilities.
The read-only probability auditor completed a same-scenario comparison for scenario set `cbrn_bio_random_baseline_20260920`, scenario hash `6825e523bcf8d532147f0f7bd613ac2130f600f539161c218cc69e8f0ddf76dd`.
The path-after versus inline-before comparison returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-648a93bb7214fa9b5aa1f531`, with three scenarios, twelve candidates, seven unresolved findings, one diagnostic, and eighteen comparison changes. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/378f5a02b9df309982a22c9ffba4098931a8750bd3cbebc648c0eba312a2e630/f85a7506b0a024dc1faa012512826f072579efb5be6c8c3efbebc8aeb56031ea/probability-648a93bb7214fa9b5aa1f531.json`.
The stricter same-inline two-entry projection returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-b30faf8f1c79c5e3b8528759`, with six candidates, two unresolved findings, and zero comparison changes. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0bf1df3fb911854c78d8f0997c7a87376092287fc4d4ae029ae9d9d3ccf42ce4/c69a51c15cd6fa8bc23773d3b8b8ae75db7e1a88e380c807f924d0b332cad262/probability-b30faf8f1c79c5e3b8528759.json`.
The full prepatch source was unavailable to the auditor, so neither partial comparison isolates the complete floor and helper delta. The 20.15% Smallpox floor is established by source arithmetic; engine-weighted behavior and exact before-and-after equivalence remain unproven. Preserve the comparison artifacts and unresolved findings for the parent integration review.
No Hearts of Iron IV game process was launched. This worker made no commit.
