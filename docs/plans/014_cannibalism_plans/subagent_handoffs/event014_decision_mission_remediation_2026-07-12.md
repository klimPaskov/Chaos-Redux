# Event 014 Decision and Mission Remediation Handoff

Date: 2026-07-12
Owner: `event014_decision_final_audit`
Scope: H-01, M-01, and M-02 from `event014_decision_mission_reaudit_2026-07-12.md`
Status: implemented; thirteen registered decision DDS files remain intentionally pending for the asset pass

## Scope boundaries

Implemented:

- H-01: six missing maintained objective families, including progress caps, persisted targets, lifecycle validation, three-way outcomes, cancellation cleanup, and AI-facing action hooks.
- M-01: seven paid, cooldown-backed, route-aware decision action families.
- M-02: thirteen unique registered decision sprites with stable final paths and no placeholder art.
- Aftermath correction: progress-backed compact partial completion and category retirement after every registered participant finishes reconstruction and compact vigilance.
- Achievement tracker support: four irreversible global visibility flags initialized and opened at the first matching public stage.

Explicitly not implemented here:

- H-02 and H-03. Focus closure and end-state receipts remain owned by `event014_focus_closure_planner`.
- Achievement tracker decisions, tracker assets, and their audit remain parent-owned.
- No focus files, specifications, event spreadsheet, presentation, binary asset, or unrelated documentation were edited.

## Files changed

Dedicated files created:

- `common/decisions/014_cannibalism_objective_decisions.txt`
- `common/script_constants/014_cannibalism_objective_constants.txt`
- `common/scripted_triggers/014_cannibalism_objective_triggers.txt`
- `common/scripted_effects/014_cannibalism_objective_effects.txt`
- `localisation/english/014_cannibalism_objectives_l_english.yml`
- `interface/014_cannibalism_objectives.gfx`

Narrow integration files changed:

- `common/scripted_effects/014_cannibalism_core_effects.txt`
  - Initializes and clears the bounded objective observer registry.
  - Processes actor objectives once inside the existing actor pulse.
  - Processes ordinary responder objectives through `global.cannibalism_objective_countries` without a recurring world scan.
  - Opens Evolution II and convergence achievement visibility flags.
- `common/scripted_effects/014_cannibalism_decision_effects.txt`
  - Existing ration-audit and forensic-recovery resolutions now record investigation operations.
- `common/scripted_effects/014_cannibalism_achievement_effects.txt`
  - Initializes the four achievement visibility flags.
  - Opens exploitation and Island Host visibility at their first matching stages.
  - Joint suppression, convergence interdiction, blockade, and landing now emit objective receipts.
  - Reconstruction participants receive a bounded registry.
  - Compact ratification records elapsed-time progress and all terminal outcomes retire the participant.
- `common/scripted_triggers/014_cannibalism_achievement_triggers.txt`
  - The international category's reconstruction branch is limited to registered reconstruction participants.
- `common/decisions/014_cannibalism_achievement_decisions.txt`
  - Compact vigilance uses a runtime duration variable, elapsed progress, and success/partial/failure resolution.
- `common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt`
  - Four existing successful counterwar actions emit stop-transformation receipts.
  - This file is shared with the focus-closure owner; their spawn-helper refactor and transformation cleanup were preserved.
- `events/014_cannibalism.txt`
  - Submission and resistance preparation affect the matching unification AI choices.
  - Preparation flags are consumed before every unification disposition.

## Maintained mission families

The prior two baseline maintained missions remain unchanged in identity:

- `cannibalism_restore_supply_corridor_mission`
- `cannibalism_rotate_compromised_formations_mission`

The six implemented families are:

| Mission | Start and progress source | Persisted identity | Full result | Partial result | Failure result |
| --- | --- | --- | --- | --- | --- |
| `cannibalism_investigation_mission` | Existing ration audit, forensic recovery, officer replacement, ritual infiltration, and ritual-economy seizure | Target state plus node id/generation when an active node exists | Linked record secured; evidence rises and the cell/node weaken | Recoverable record fragment and limited suppression | Trail burned; integrity falls and the cell/node recover |
| `cannibalism_hold_prison_mission` | Auto-starts only from the existing Event 014 bounded actor pulse when a controlled prison/camp has a live node; uninterrupted pulse progress requires a garrison and transport/support reserves | Target state plus required node id/generation | Compound secured and access removed | Partial staff removal | Cordon failure strengthens the cell/node |
| `cannibalism_reach_island_mission` | Silent-island reconnaissance, existing blockade, and existing landing operations | Exact Island Host country plus actor generation | Sea road opened and decisive aid recorded | Charts/forward positions retained | Expedition loses initiative |
| `cannibalism_break_network_mission` | Repeated existing joint-suppression operations against the same country | Exact target country plus actor generation | Route family broken; reach and target meters fall | Several links remain broken | Target network replaces exposed links |
| `cannibalism_stop_unification_mission` | Existing convergence interdiction starts a maintained war-pressure objective; the bounded responder pulse advances uninterrupted days | Exact likely host plus actor generation | Warning-window gathering fractured | Interdiction delays and damages the gathering | Pressure fails before the threshold |
| `cannibalism_stop_transformation_mission` | Existing identify, assault, logistics-disruption, and recruitment-site counterwar successes | Exact Wendigo merge host plus actor generation | Anchor chain broken before lock | Some anchors remain unusable | Counterwar loses the pre-lock window |

All six use runtime mission durations, capped progress, explicit partial thresholds, and cancel effects that first test for earned success before resolving partial or failure. A recycled country tag cannot inherit country-target progress. State node progress cannot survive a node-generation change.

## Seven action families

| Decision | Route and target gate | Paid resources | Cooldown and cleanup | Gameplay result |
| --- | --- | --- | --- | --- |
| `cannibalism_replace_compromised_officer_chain` | Ritual prosecution route | Manpower, support equipment, command power | Country re-enable timer | Restores integrity, suppresses cell strength, advances investigation |
| `cannibalism_infiltrate_ritual_cell` | Ritual infiltration route; controlled live cell | Manpower, support equipment, command power | Decision timer plus target-state cooldown | Raises evidence and damages cell, cult, and node |
| `cannibalism_break_ritual_economy` | Prosecution or infiltration route; controlled feeding-linked live cell | Manpower, infantry equipment, support equipment, command power | Decision timer plus target-state cooldown | Damages cell, cult, node, and global reach |
| `cannibalism_reconnoiter_silent_island` | Ordinary international responder; live Island Host country target | Convoys, Navy Experience, command power | Decision timer plus target-country cooldown | Starts/advances the sea-road objective |
| `cannibalism_liberate_feeding_state` | Ordinary international responder; controlled live feeding/silent-larder node | Manpower, infantry equipment, support equipment, command power | Decision timer plus target-state cooldown; node retirement uses exact id/generation | Enters the existing liberation and recovery sequence without creating population or reserves |
| `cannibalism_prepare_network_submission` | Pre-reveal warlord network phase; mutually exclusive with resistance | Larder, support equipment, command power | One-shot preparation; consumed by any unification disposition or convergence break | Raises alignment and weights retained-command submission |
| `cannibalism_prepare_network_resistance` | Pre-reveal warlord network phase; mutually exclusive with submission | Larder, infantry equipment, support equipment, command power | One-shot preparation; consumed by any unification disposition or convergence break | Lowers alignment, strengthens command resolve, and weights resistance |

Every action has `ai_will_do`, a real resource gate and payment, a cooldown or one-shot preparation lifecycle, and a bounded cleanup path. None grants units, equipment, population, or Larder. Feeding-state liberation calls the existing node-retirement/recovery sequence and does not alter population outside the established systems.

## Aftermath lifecycle

`global.cannibalism_reconstruction_participants` is populated from the exact contributor and former-feeding-state owner sets when eligible global-defeat reconstruction begins. It deliberately survives Event 014 gameplay cleanup because reconstruction begins immediately before that cleanup.

Compact ratification records:

- `cannibalism_compact_vigilance_start_date`
- `cannibalism_compact_vigilance_progress_days`
- `cannibalism_compact_vigilance_duration`

At timeout or cancellation, elapsed progress resolves as:

- full: compact maintained and at least the full-progress threshold
- partial: at least the partial-progress threshold, without setting the failure flag
- failure: below the partial threshold

Every terminal outcome clears the participant's active reconstruction flag, removes it from the bounded participant registry, refreshes its reconstruction idea, and checks whether any registered participant remains. The reconstruction system flag is cleared only after none remain.

## Achievement visibility flags

The exact parent-consumed ids are wired as follows:

- `achievement_cannibalism_exploitation_visibility_open`
  - cleared by `cannibalism_initialize_achievement_runtime`
  - set by the shared exploitation-record effect at the first exploitation selection
- `achievement_cannibalism_island_host_visibility_open`
  - cleared by achievement initialization
  - set only after successful Island Host formation reaches the existing warlord-formation receipt
- `achievement_cannibalism_evolution_ii_visibility_open`
  - cleared by achievement initialization
  - set when Evolution II opens
- `achievement_cannibalism_convergence_visibility_open`
  - cleared by achievement initialization
  - set when the first convergence window opens

These flags are not cleared during ordinary phase transitions or end-of-event cleanup, so they remain irreversible campaign visibility history after opening.

## Registered sprite handoff

`interface/014_cannibalism_objectives.gfx` registers exactly thirteen unique sprites and thirteen unique stable paths:

- `GFX_decision_cannibalism_replace_compromised_officer_chain` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_replace_compromised_officer_chain.dds`
- `GFX_decision_cannibalism_infiltrate_ritual_cell` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_infiltrate_ritual_cell.dds`
- `GFX_decision_cannibalism_break_ritual_economy` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_break_ritual_economy.dds`
- `GFX_decision_cannibalism_reconnoiter_silent_island` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_reconnoiter_silent_island.dds`
- `GFX_decision_cannibalism_liberate_feeding_state` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_liberate_feeding_state.dds`
- `GFX_decision_cannibalism_prepare_network_submission` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_prepare_network_submission.dds`
- `GFX_decision_cannibalism_prepare_network_resistance` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_prepare_network_resistance.dds`
- `GFX_decision_cannibalism_investigation_mission` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_investigation_mission.dds`
- `GFX_decision_cannibalism_hold_prison_mission` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_hold_prison_mission.dds`
- `GFX_decision_cannibalism_reach_island_mission` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_reach_island_mission.dds`
- `GFX_decision_cannibalism_break_network_mission` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_break_network_mission.dds`
- `GFX_decision_cannibalism_stop_unification_mission` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_stop_unification_mission.dds`
- `GFX_decision_cannibalism_stop_transformation_mission` -> `gfx/interface/decisions/014_cannibalism/decision_cannibalism_stop_transformation_mission.dds`

No DDS, source art, reused art, generated art, fallback icon, or placeholder was created. The thirteen paths above are the intentional asset-subagent handoff.

## Meaningful validation

- Maintained-family coverage: all eight exact objective ids are present once (the two prior baseline missions plus six implemented missions).
- Three-way coverage: all six implemented missions have full, partial, failure, timeout, and cancellation resolution paths.
- Operational inventory: thirteen unique gameplay decision/mission entries were added to the audited prior inventory of 92, producing the requested operational inventory of 105. The separately parent-owned read-only achievement tracker entries are not gameplay actions and are excluded from this count.
- Action behavior: all seven action ids are unique, all seven have re-enable timers, all seven have AI weights, and all seven pay the resources described by their dynamic localisation.
- Objective tuning: all 135 objective constants are centralized; every objective constant reference resolves.
- Objective bounds: progress variables, global reach, node strength, target alignment, country meters, and compact elapsed days are clamped at their relevant caps.
- Registry behavior: objective pulse work iterates only `global.cannibalism_actor_countries` and `global.cannibalism_objective_countries`; aftermath retirement iterates only `global.cannibalism_reconstruction_participants`. No new recurring whole-world iteration or on-action was added.
- Localisation: all 72 new keys are unique, every new decision/tooltip reference resolves, and the file is UTF-8 with BOM.
- Sprite handoff: thirteen decision icon references match thirteen unique GFX sprite names and paths. The only intentionally missing files in this package are the thirteen listed DDS paths.
- Resource integrity: the objective implementation contains no unit creation, equipment grant, manpower grant, population mutation, or Larder grant. Feeding-state liberation routes through the existing recovery helper.
- Visibility tracker support: each of the four exact visibility flags has one initialization clear, one first-stage set, and a parent-owned tracker consumer.

An additional read-only `chaosx_decision_mission_auditor` launch was attempted, but the project subagent thread limit was occupied by parallel parent/focus work. The audit above was therefore completed locally. The parent requested a later clean re-audit after all parallel Event 014 tranches settle.

## Simplifications, omissions, and blockers

- Intentional pending assets: the thirteen DDS files listed above do not exist yet. This is the requested M-02 registration-first handoff, not a fallback. The decision ids and paths must not be renamed by the asset pass.
- H-02/H-03 remain outside this patch and under the focus-closure owner's active tranche.
- The parent-owned staged achievement tracker is outside this audit's operational inventory and asset ownership.
- No gameplay simplification, fallback behavior, free-resource substitute, generic copied decision, recurring world scan, or unapproved route expansion was used.
- No commit was created, as explicitly requested for this remediation tranche.

## Skills used

- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

No skill was created or updated by this subtask.
