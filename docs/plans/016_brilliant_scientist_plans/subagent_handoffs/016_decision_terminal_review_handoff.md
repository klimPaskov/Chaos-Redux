# Event 016 Decision and Terminal Review Handoff

Date: 2026-07-24.

Scope: Kruger Directorate and KRG decision and mission surfaces, with a bounded repair of the Strategic Singularity and Laboratory World terminal lifecycle.

Status: patched, not staged or committed.

## Critical issues repaired

1. Critical: A terminal commitment set `brilliant_scientist_terminal_commitment_locked`, while every terminal decision and the terminal category depended on `brilliant_scientist_kruger_focus_is_active` through `brilliant_scientist_krg_decisions_are_active`.
This hid the entire terminal category immediately after either commitment, including the only component review and disarmment actions.
`brilliant_scientist_krg_terminal_decisions_are_active` now preserves terminal-only actions after the ordinary focus layer closes.

2. Critical: No decision ever set `brilliant_scientist_singularity_armed`, `brilliant_scientist_singularity_fail_deadly_active`, or `brilliant_scientist_singularity_arming_ever_started`.
The existing capitulation failsafe and source-aware Fallout handoff were therefore unreachable in normal play.
The new arming and fail-deadly decisions set those states only after explicit paid, timed work, and deliberate detonation now calls the existing `brilliant_scientist_execute_singularity_terminal` helper.

3. Critical: `brilliant_scientist_execute_lab_world_terminal` had no caller.
`brilliant_scientist_krg_complete_laboratory_world` now performs a final terminal map audit and calls that existing resolver only if the current proof remains valid.

4. High: `brilliant_scientist_world_control_ratio`, `brilliant_scientist_integrated_state_ratio`, and `brilliant_scientist_major_opposition_count` were receipt-like counters.
The terminal audit now counts real global states, control by KRG or KRG subjects, direct KRG cores under KRG control, and every living major non-subject non-KRG country.
The calculated ratios are normalized fractions, and the former 90/70 world-conquest receipt gates are normalized to 0.90/0.70.

5. Medium: The existing global disarmament hold was the only way to verify a nonterminal outcome, but it required `brilliant_scientist_global_weapons_dismantled` before it could begin.
`brilliant_scientist_krg_begin_controlled_singularity_disarmament` supplies the KRG-owned eight-month reversal after arming has started, then permits the existing durable-settlement certification path.

6. Medium: The continental refresh and world-conquest activation were political-power-only receipt actions.
They now use timed material costs, factory burden where appropriate, and the explicit map audit before and after the world-conquest activation.

## Changed files and identifiers

- `common/decisions/016_brilliant_scientist_kruger_state_terminal_decisions.txt`
  - Added `brilliant_scientist_krg_begin_singularity_arming`.
  - Added `brilliant_scientist_krg_activate_singularity_fail_deadly`.
  - Added `brilliant_scientist_krg_authorize_deliberate_singularity_detonation`.
  - Added `brilliant_scientist_krg_begin_controlled_singularity_disarmament`.
  - Added `brilliant_scientist_krg_audit_laboratory_world_order`.
  - Added `brilliant_scientist_krg_complete_laboratory_world`.
  - Moved every terminal action and the existing disarmment hold to the terminal-only activity gate.
  - Added materials to the existing hold and settlement certification and made a failed Laboratory World completion retryable.

- `common/decisions/016_brilliant_scientist_kruger_state_foreign_integration_decisions.txt`
  - Replaced the corridor's control-ratio receipt with no terminal-map write.
  - Made continental refresh an explicit paid 14-day terminal-map audit.
  - Made world-conquest activation re-audit before setting `brilliant_scientist_world_conquest_decision_active` and added material/factory costs.

- `common/decisions/categories/016_brilliant_scientist_kruger_state_categories.txt`
  - The terminal category remains visible after commitment until world-end cleanup.

- `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt`
  - Added the terminal-only activity, arm, fail-deadly, detonation, disarmment, and current map-proof triggers.
  - Updated world-conquest activation and durable nonterminal certification to use the audit and controlled-disarmment proof.

- `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`
  - Added `brilliant_scientist_krg_audit_terminal_world_state`.
  - Added narrow lifecycle helpers for arming, activation, detonation-protocol cleanup, and controlled disarmament.
  - Removed integration's ratio receipts and normalized stored terminal ratios as fractions.

- `common/scripted_triggers/016_brilliant_scientist_triggers.txt`
  - Singularly terminal-ready state now rejects the Chaos-Meter-disabled setting and active controlled disarmament.
  - Laboratory World terminal-ready state requires the current map-audit proof, strict shared final chaos threshold, and an enabled Chaos Meter.

- `common/scripted_effects/016_brilliant_scientist_effects.txt`
  - Verification now clears transient terminal flags and records `verified_nonterminal` state.
  - Singularity terminal cleanup now records terminal state and clears every new transient lifecycle flag.

- `common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt`
  - Normalized world-conquest control and integration thresholds to fractional audited ratios.

- `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml`
  - Added all six decision names, descriptions, and readiness tooltips.

## Before and after behavior

Before, a KRG player could commit to a terminal focus but lost the category that contained all terminal decisions.
The singularity could be theoretically fired on capitulation but could never gain armed or fail-deadly state, and Laboratory World could never call its resolver.

After, the Strategic Singularity lifecycle is commitment, component and facility proof, one-year arming, 90-day fail-deadly authorization, then either a 120-day deliberate detonation window or the existing defeat failsafe.
The timed detonation only calls the existing fallout handoff after the strict shared threshold has been exceeded by the existing source-aware helper.
The KRG can instead spend eight months dismantling a started or armed program, certify a durable nonterminal settlement, and thereby clear the singularity commitment safely.

The Laboratory World lifecycle is focus commitment, administration and submission work, a paid 14-day on-demand world audit, then a retryable eight-month finalization that repeats the audit immediately before calling the existing Laboratory World resolver.

## Decision category lifecycle notes

- Owner: KRG.
- Category: `brilliant_scientist_krg_terminal_program_category`.
- Reveal: Evolution IV plus either global, Laboratory World, or Singularity program unlock.
- Active lifecycle: It now survives `brilliant_scientist_terminal_commitment_locked` and closes only when KRG is no longer active or `world_end`/the all-actions lock is present.
- Laboratory World: focus commitment is mutually exclusive with the Singularity focus, then the audit and finalization decisions become visible.
- Strategic Singularity: focus/project commitment enables review, arming, fail-deadly, detonation, and controlled disarmment.
- Cleanup: world-end markers clear armed, fail-deadly, arming, disarmment, and detonation-protocol transient flags.

## Mission quality notes

| Owner | Category | Region | Requirement | Duration | Success | Failure or duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| KRG | Terminal Program | Global | `brilliant_scientist_global_weapons_dismantled`, no active armed or fail-deadly state, paid standard materials | 180 days | Sets `brilliant_scientist_singularity_disarmament_hold_complete` | Cancels if the Directorate becomes inactive, dismantlement proof is lost, or arming/fail-deadly returns. It remains separate from the KRG controlled-disarmment decision. |
| KRG | Terminal Program | Global | Started or armed KRG Singularity, paid heavy materials | 240 days | Clears armed and fail-deadly, sets controlled-disarmment and hold-complete proof | Cancellation clears only the active flag. Completion hides the decision through `brilliant_scientist_krg_controlled_singularity_disarmament_complete`, so it cannot farm a repeat outcome. |

## Cost and requirement clarity notes

- Arming spends strategic PP, heavy support/motorized/fuel stores, six civilian factories, and 365 days.
- Fail-deadly spends heavy PP, standard materials, two civilian factories, and 90 days.
- Deliberate detonation spends strategic PP, heavy materials, six civilian factories, and 120 days, leaving a counterplay window in which component, facility, command, setting, or route failure cancels the protocol.
- Controlled disarmment spends strategic PP, heavy materials, six civilian factories, and 240 days.
- Laboratory World audit costs light PP/materials and 14 days, while finalization costs strategic PP/heavy materials, six civilian factories, and 240 days.
- All new player-facing readiness gates use custom tooltips rather than exposing raw trigger chains.

## AI validity and route-lock notes

- Arming has low baseline AI willingness and stronger war/world-conquest weighting.
- Fail-deadly activation is weighted strongly near the existing surrender threshold, enabling the existing capitulation failsafe rather than inventing an AI-only outcome.
- The AI may audit and finalize Laboratory World only when the same availability proof is true; finalization re-audits at resolution.
- The controlled-disarmment path is deliberately low-priority for AI and only exists while a singularity commitment is still active.
- The ordinary KRG decision layer remains route-locked after commitment; only terminal actions use the new narrow activity trigger.

## Localisation and tooltip gaps

All six added decision ids have English names and descriptions, and the four complex readiness gates have custom tooltips.
The existing Directorate GUI still only exposes an armed indicator and does not surface arming, fail-deadly, controlled-disarmment, or terminal map-audit state.
No GUI change was made because the current task owns decisions rather than a new GUI surface.

## Cleanup and exploit-risk notes

- World-end cleanup clears all new transient lifecycle flags.
- Destroyed components or a lost required network cancel arming and deliberate-detonation work before resolution.
- A final Laboratory World audit occurs after the timer, preventing stale audit data from firing the ending.
- Controlled disarmment sets a permanent completion proof, preventing repeated completion loops.
- The pre-existing submission acceptance event still writes legacy receipt variables in `events/016_brilliant_scientist_kruger_state_events.txt`.
Those values no longer qualify either terminal path because every terminal/world-conquest resolution uses the explicit audit, but removing the legacy bookkeeping from that event was left outside this bounded decision-script patch.

## Meaningful validation

- Verified that the only direct Laboratory World resolver caller is now `brilliant_scientist_krg_complete_laboratory_world`.
- Verified that the only setters of `brilliant_scientist_singularity_arming_ever_started`, `brilliant_scientist_singularity_armed`, and `brilliant_scientist_singularity_fail_deadly_active` are the new paid lifecycle helpers.
- Verified that the existing defeat evaluator still calls `brilliant_scientist_execute_singularity_terminal` through `brilliant_scientist_singularity_capitulation_failsafe_is_ready`.
- Verified each new decision id has English localisation and that the modified localisation file retains UTF-8 BOM.
- Performed structural brace balance and targeted diff whitespace checks on every touched Clausewitz file.

## Skipped or blocked validation

- `hoi4.gui_inspect` for `kruger_directorate_container` could not produce an artifact because the workspace scan hit `SCAN_BYTE_LIMIT`.
- `hoi4.event_inspect` trace and lint attempts for the terminal source reached `EVENT_ISSUE_LIMIT` before producing a graph artifact.
- No in-game runtime session was available to exercise a complete world-control scenario.

## Remaining issues and recommended follow-up

1. Decide whether to delete the obsolete receipt writes in `events/016_brilliant_scientist_kruger_state_events.txt` once the event owner reviews its target scopes.
The new audit makes them non-authoritative, but removing them would prevent misleading display values between audits.

2. Add scripted localisation or a small Directorate panel status line for current audited control ratio, integration ratio, outstanding major opposition, arming status, and fail-deadly authority.
This needs a GUI-owner review because the read-only GUI inspector could not finish.

3. Run a live KRG scenario through both terminal routes and one cancellation each once a test save has the necessary world state.

No broad new decision system, GUI system, formable suite, or event chain was added.

## Parent review disposition, 2026-07-24

Accepted after source review with three narrow corrections:

- Removed the legacy submission-event writes to `brilliant_scientist_world_control_ratio` and `brilliant_scientist_major_opposition_count`. Those values are now written only by the explicit live-map audit, so submission receipts cannot make a stale audit appear to pass or charge a player for a terminal action that fails its final re-audit.
- Blocked renewed Singularity arming after global dismantlement, a completed disarmament hold, controlled disarmament, permanent route cancellation, or durable settlement. This closes the interval in which an eight-month disarmament could otherwise be immediately reversed before the settlement decision completed.
- Changed the delayed former-host settlement decision, event, and localisation to use the persistent global former-host target. The short-lived formation-chain target still handles inheritance, but it cannot support a decision taken months or years after state formation.

The deliberate detonation decision retains zero AI weight by design. The source AI matrix says a strong armed AI preserves the device as a deterrent unless it has selected deliberate use; AI terminal firing remains the severe-surrender fail-deadly path, while a player can select the explicit deliberate-use action.

Parent evidence:

- All terminal and integration decision IDs have matching title and description localisation, and every referenced custom tooltip key resolves.
- The live-map audit has exactly four bounded decision call sites and no recurring on-action call.
- Territorial-control, direct-integration, and living-major-opposition values have no remaining event receipt writers.
- The repaired terminal files retain balanced block structure, centralised constants, and exact scenario and commitment guards. Native runtime acceptance remains pending with the final mapped audits.
