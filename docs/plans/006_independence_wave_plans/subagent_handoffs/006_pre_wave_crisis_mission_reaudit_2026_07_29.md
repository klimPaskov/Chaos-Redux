# Event 006 pre-wave crisis mission repair re-audit — 2026-07-29

## Verdict: static PASS

The repair resolves both prior source holds without changing the mission's ownership boundary, normal allocator handoff, or cost/duration contract.

No gameplay files were changed by this audit.

## Repaired findings verified

| Check | Evidence | Result |
| --- | --- | --- |
| Active-mission category visibility | `independence_wave_crisis_category` now remains visible when the open trigger passes, the runtime active flag is present, or `has_active_mission = independence_wave_open_host_crisis` is true in [common\\decisions\\categories\\006_independence_wave_crisis_categories.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\categories\006_independence_wave_crisis_categories.txt:8). | Pass. The player retains the 120-day mission surface after selection. |
| Vanilla mission lifecycle | The mission uses `activation`, `selectable_mission = yes`, `available`, `complete_effect`, `days_mission_timeout`, `cancel_trigger`, `cancel_effect`, and `timeout_effect` in [common\\decisions\\006_independence_wave_crisis_decisions.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\006_independence_wave_crisis_decisions.txt:11). | Pass. No mission-local `visible` block remains. |
| Command-power availability and deduction | Standard-security availability now requires standard command power in [common\\scripted_triggers\\006_independence_wave_decision_triggers.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\scripted_triggers\006_independence_wave_decision_triggers.txt:253), matching the command-power deduction in `independence_wave_pay_crisis_cost`. | Pass. |
| Centralized AI tuning | The mission reads `independence_wave_crisis_ai.base` and `.pressure_factor`, both declared in [common\\script_constants\\006_independence_wave_crisis_constants.txt](C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\script_constants\006_independence_wave_crisis_constants.txt:28). | Pass. Occupation and stability pressure retain separate multipliers. |
| Localisation | Category, mission, description, and cost keys describe the same 120-day security commitment and its centrally displayed costs. | Pass. |
| Cleanup and queue race | The queue consumer retains one requester receipt and clears the global queue, retry variable, and requester receipt after planner success, planner failure, or retry exhaustion. A busy barrier retries on centralized one-day / fourteen-attempt constants. | Static pass. |

## Files changed by the repair

- `common/decisions/categories/006_independence_wave_crisis_categories.txt`
- `common/decisions/006_independence_wave_crisis_decisions.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/script_constants/006_independence_wave_crisis_constants.txt`

## Cost and cleanup notes

`can_pay_independence_wave_crisis_cost` still repeats the command-power comparison after delegating to the repaired shared security-standard trigger.

That duplicate guard is behaviorally harmless and does not double-charge command power, because payment remains a single `complete_effect` call.

The retry consumer's final stale-queue branch can only clear the global queue when its requester receipt is absent, so it cannot clear a retry variable on a no-longer-addressable requester.

This is safe for the global lock, but save/load and requester-destruction behavior remain live-validation risks rather than a static source blocker.

## Evidence and remaining risks

Read the repair handoff, current category, mission, shared-cost-trigger, constants, localisation, and queue/retry cleanup call sites.

Offline decision documentation and the vanilla active-mission category precedent remain consistent with the new category visibility branch.

Live UI persistence, AI selection, save/load during the retry window, requester destruction, and allocator execution remain runtime evidence gaps.
