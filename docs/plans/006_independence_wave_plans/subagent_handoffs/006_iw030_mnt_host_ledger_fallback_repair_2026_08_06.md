# IW-030 Montenegro host-ledger fallback repair

Date: 2026-08-06.

## Scope

This bounded decision-lifecycle repair covers the Montenegro former-host ledger action after the depot project has completed.

It does not alter MNT admission, portraits, AI weights, formable registration, the founding mission duration, costs, or the shared Event 006 systems.

## Changed files and identifiers

- `common/decisions/006_independence_wave_montenegro_decisions.txt`
  - Updated `independence_wave_mnt_settle_former_host_ledgers` visibility and availability.
  - A peaceful living former host continues to use the ordinary bilateral route.
  - After `independence_wave_mnt_depots_reopened`, an absent or hostile former host satisfying `has_independence_wave_mnt_unsettled_host` exposes and enables the existing local fallback, subject to the unchanged diplomatic-standard cost, capital-control check, one-active-project lock, and project-ready gate.
- `localisation/english/006_independence_wave_montenegro_l_english.yml`
  - Updated `independence_wave_mnt_settle_former_host_ledgers_desc` and `independence_wave_mnt_host_ledgers_effect_tt` so the player-facing text describes both the negotiated and local-settlement outcomes.

The repair intentionally reuses the existing effect identifier `independence_wave_mnt_focus_settle_host` in `common/scripted_effects/006_independence_wave_montenegro_package_effects.txt` without changing it.

That helper grants the existing minor cohesion plus decisive crown-legitimacy recovery when `has_independence_wave_mnt_unsettled_host = yes`, skips bilateral former-host deltas in that branch, and sets `independence_wave_mnt_host_ledgers_settled` to prevent repetition.

The existing cancellation branch on `independence_wave_mnt_settle_former_host_ledgers` already invokes the same helper when the former host dies or enters war after the project has begun, provided the capital remains controlled and the MNT project remains ready.

## Behavior

Before this patch, the former-host ledger decision required a living former host to be visible.

If the former host disappeared or went to war after the depot project was already complete but before the ledger action started, the decision disappeared even though the documented local fallback existed in the helper.

After this patch, the depot receipt unlocks the local completion route whenever the former-host relationship becomes unavailable.

The normal route remains a living, peaceful former-host negotiation with the same cost and duration.

The fallback keeps the same diplomatic-standard cost and 180-day duration, then applies the existing local ledger closure and decisive crown recovery without attempting a bilateral change against a dead or hostile host.

For the previously deadlocked transition path, depots, guards, offices, and the fallback settle at 75 + 120 + 120 + 180 = 495 days inside the existing 540-day mission window.

Their compact changes are +15/+5, +10/+5, +10/+10, and +5/+20 for cohesion/crown legitimacy, taking the opening 34/31 to 74/71 and clearing the 60/60 founding gate.

## Static validation

- Reviewed the decision branches so both visibility and availability retain `is_independence_wave_mnt_project_ready`, the unchanged diplomatic cost trigger, capital control, and one-active-project lock.
- Confirmed the new fallback branch requires both `independence_wave_mnt_depots_reopened` and `has_independence_wave_mnt_unsettled_host`, so a hostless package cannot use it before the documented depot recovery exists.
- Confirmed the existing cancellation path calls `independence_wave_mnt_focus_settle_host` only while the MNT package is still ready, the capital is controlled, and the host is unsettled; capital loss still takes the existing project-failure route.
- Confirmed the helper's local branch does not call `independence_wave_mnt_apply_former_host_settlement` or `independence_wave_focus_progress_host_negotiations`, avoiding an invalid former-host scope after death or war.
- Confirmed both changed localisation keys remain present in the MNT English localisation file, which retains its UTF-8 BOM.
- No AI or probability-bearing value changed, so a probability comparison was not applicable.
- A post-change MCP probability inspection of `common/decisions/006_independence_wave_montenegro_decisions.txt` using the `decision_ai_will_do` adapter returned `PROBABILITY_SOURCE_INSPECTED` (`sourceHash=611a3035c651a8d7a31bab51e8256779b555b38f960bb24469d9c3d85894b22c`, one candidate, ten required inputs, unresolved=0, `poolComplete=false`). This is syntax/surface evidence only; it does not claim normalized decision probabilities.
- MNT owns no decision-specific scripted GUI in this repair, so no GUI inspection or render route was applicable.

## Skipped validation and remaining issues

No live game, release, host-death, war-transition, save-load, or AI-play test was run.

Those runtime scenarios remain parent or user validation work, and this handoff does not claim MNT admission.

IW-030 remains outside central content attestation, and its portrait, force-materialization, and runtime evidence gates remain unchanged and fail-closed.

No simplification, fallback asset, or unrelated balance change was introduced.
