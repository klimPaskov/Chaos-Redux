# Event 023 closure helpers

These are event-owned helpers for the existing Soviet arsenal contract.
They reuse the existing security/logistics payment, command clamps, missing-device accounting, public-knowledge and credibility endpoints.
They do not extend the global dynamic-helper API or own shared nuclear damage.

| Helper | Scope and input | Output, defaults and side effects |
| --- | --- | --- |
| `sov_nuclear_bombs_clear_command_developments` | Soviet country | Clears the four doctrine-development flags during reform, without granting or spending resources. |
| `sov_nuclear_bombs_complete_command_development` | Soviet country, pending flag required | Grants the current doctrine?s one development, gives Military eight Integrity, clamps command values, refreshes posture, clears pending and requests one AI review. No pending flag means no award. |
| `sov_nuclear_bombs_begin_arsenal_service` | Soviet country, valid over-capacity service and affordable logistics required | Debits the existing logistics profile, stands down eight Readiness, stores exactly that held amount as a normal variable and activates the service mission. |
| `sov_nuclear_bombs_restore_service_readiness` | Service owner country, held-Readiness normal variable | Returns only that cycle?s held Readiness once, clears the field and clamps. Absent field is a no-op. Other losses and paid resources are preserved. |
| `sov_nuclear_bombs_complete_arsenal_service` | Soviet country, pending flag and valid actor | Restores held Readiness, gives eight Integrity, creates literal-day stabilization/cooldown flags, clears pending and requests AI review. It never refunds supplies. |
| `sov_nuclear_bombs_interrupt_work_after_enemy_strike` | Soviet country after a confirmed enemy detonation | Ends unfinished service/development missions before retaliation routing, restores held service Readiness once, and gives neither unfinished development nor stabilization. |
| `sov_nuclear_bombs_request_public_test_presentation` | Soviet country after one public-test reservation starts | Clears an old choice, marks one pending choice and opens report 183. Cancellation removes the pending choice. |
| `sov_nuclear_bombs_apply_public_test_presentation` | Soviet country after a confirmed demonstration | Freezes the current choice as last-test presentation, defaults an unchosen wartime demonstration to announcement afterward, changes credibility through the existing helper and gives observers four Integrity, then clears the active choice. |
| `sov_nuclear_bombs_publish_first_demonstration` | Soviet country with the final presentation | Publishes news 230 once globally and preserves that first presentation for delayed news. Later demonstrations are a no-op for that headline. |
| `sov_nuclear_bombs_apply_doctrine_transfer_risk` | Exact registered transferred depot STATE, only called after proven Soviet departure or an existing pending marker | Dispersed custody marks one risk pending. It waits for zero reserved devices, no pending native state and no active dismantlement. On resolution it marks the risk resolved before a 25/75 roll, then routes any loss through the existing missing-site helper. No raw device arithmetic is added. |
| `sov_nuclear_bombs_publish_successor_emergence` | Breakaway country in its own successful delivery-integration callback, local custody state pointer | Saves regular actor/state targets into one delayed news per breakaway and applies Soviet credibility/exposure consequences through their existing endpoints. Targets carry in the firing chain rather than a shared mutable global pointer. |

The service quote is shared between overload eligibility, routine upkeep and the first-hover tooltip.
Its capacity is the effective registered reactor count times the upkeep capacity per reactor, with the existing floor.
Its inventory is only intact actor operational, assigned and reserved devices.
Readiness held for service is returned on successful completion, invalid-actor cancellation or confirmed-strike preemption, and is never returned twice.

The transfer-risk retry runs in exact-source action cleanup before clearing the source pointer, and in exact-state reconciliation only if a pending marker already exists.
There is no periodic world or state scan.
Breakaway operationalization cannot bypass an unresolved transfer risk.

A caller example is the existing confirmed-enemy-strike seam:

```text
sov_nuclear_bombs_record_confirmed_enemy_strike = {
	sov_nuclear_bombs_interrupt_work_after_enemy_strike = yes
	# Existing confirmed-strike doctrine and posture handling follows.
}
```

For servicing, the decision calls `sov_nuclear_bombs_begin_arsenal_service = yes` only after displaying the matching logistics cost.
For a transferred depot, the Event 5 receipt validates its old Soviet owner/controller and new non-Soviet holder before invoking the state helper.
The constants and the accepted decisions live in the companion closure constants file and the Event 023 takeover decision document.
