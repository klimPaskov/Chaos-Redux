# Clone maturation core source review

Disposition: implemented independent source review of isolated scaffolding, with live integration accepted and queued pending parent probability baseline and wiring.
Acceptance basis is the parent-requested bounded review and the accepted Clone maturation production correction in `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`.
Only this review document was changed.

## Reviewed source and verdict

Reviewed `common/scripted_effects/016_clone_maturation_effects.txt` and its matching Markdown contract, `common/scripted_triggers/016_clone_maturation_triggers.txt`, `common/script_constants/016_clone_maturation_constants.txt`, and `016_clone_maturation_core_2026-09-08.md` in this handoff directory.
Also compared the old cycle helper in `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`, its live decision in `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt`, inherited Deployment site marking in `common/scripted_effects/016_brilliant_scientist_project_effects.txt`, and the reserve consumer in `common/scripted_effects/clone_system_effects.txt`.
No blocking source defect found in the draft core under its documented single-native-timer contract.
This verdict does not approve the unchanged live decision as implementing the correction.

## Transaction and scope review

- Constants match the accepted 100 `clone_equipment_1`, 65 PP, 150 support equipment, 1,000 fuel, four native civilian factories, 90 days and 30-day re-enable interval.
- Start requires current operations and direct affordability, snapshots all three direct payments plus output quantity, establishes paid authority, then debits exactly the snapshots through the shared resource helpers.
- Inclusive admission checks all four costs, while begin deliberately checks only the three direct costs after native admission.
  With exactly four free factories, begin remains valid whether the engine reports four before reservation or zero after reservation.
  A PP, support or fuel shortage appearing before begin prevents both receipt creation and all debits.
- Complete-receipt cancellation copies snapshots into temporary refund variables, clears all persistent authority, then refunds the original direct values once.
  Repeated cancel, finish after cancel, and cleanup after settlement have no complete receipt and cannot refund or produce equipment again.
- Successful finish requires both the complete receipt and current operations, snapshots the paid output quantity, clears receipt authority, adds only clone equipment, refreshes the existing physical-stockpile reserve consumer, then records history.
  There is no rifle, support-equipment reward, direct manpower award or division creation in this path.
- Invalid operation at expiry enters cancellation even when the receipt is incomplete.
  Missing fields, a missing paid flag, negative direct snapshots or nonpositive output all fail receipt validation and retire fragments without inventing refunds or output.
  If a paid flag is missing but fragments remain before a new valid begin, the begin overwrites all fragments with a new fully paid receipt rather than treating them as refund authority.
- History extraction preserves the old cycle increment, burden flag, crisis threshold and crisis exclusions exactly, omitting the two old equipment rewards.
  Finish alone grants the temporary history authorization and the history helper consumes it before incrementing.
  Neither admission nor finish imposes the old lifetime cycle maximum.
- `any_owned_state` establishes actual ownership and `is_controlled_by = PREV` tests the country invoking this trigger, including when an external event ROOT differs.
  A country flag alone cannot satisfy the site gate.
  Both accepted state markers have actual writers: paid designation marks FROM, and Deployment marks the primary-facility event target.
  Any currently qualifying owned-and-controlled site satisfies the contract, not necessarily the original site's identity.
- The parent-added `brilliant_scientist_krg_cleanup_clone_maturation` calls cancellation before `remove_decision`.
  Its receipt retirement makes repeated cleanup harmless and leaves any later finish call without output authority.
  Native factory release remains native ownership, with no factory creation or scripted factory refund in the core.

## Exact integration requirements

The live `brilliant_scientist_krg_run_bounded_clone_growth_cycle` still uses the old batch payment, lifetime maximum, old completion helper and native PP charge at review time.
No live start/finish/terminal cleanup call site into the new core was found.
Parent must replace that wiring after the required frozen probability baseline, retaining the existing category and icon.

1. Use the new inclusive admission/custom-cost gate, `cost = 0`, four native CIC, 90-day duration and 30-day cooldown.
2. Call begin in the native start callback, cancel in cancellation, and finish in expiry, with concise tooltips gated on their successful result flags.
3. Cancel on noncurrent receipt or lost operational/site eligibility so a failed direct-cost race cannot leave a productive timer.
4. Wire terminal invalidation through the new cleanup helper before removing the decision elsewhere.
5. Remove the old batch debit and old rifle/support completion route from this decision, and remove its lifetime-cap admission condition without deleting durable history.
6. Complete the parent-owned matching-scenario probability comparison and final decision/localisation review.

The amended cancellation tooltip accurately limits refunds to a complete recorded payment.
The new cancellation-trigger tooltip covers operational, site and order invalidation without dumping nested trigger internals.
Arbitrary overlapping external calls are not a supported API: no transaction generation token exists, so a late callback from a distinct external timer after another begin would not be distinguishable.
The documented single native decision timer is therefore an integration precondition, not an inferred general concurrency guarantee.

## Evidence and limits

This pass independently walked the actual source branches and compared the old history extraction.
It did not rerun or independently certify the implementing worker's reported 59 interpreter assertions and two outer-ROOT scenarios.
No interpreter stubs or new test framework were introduced in this review.
Native equipment variant selection, resource caps, callback ordering, timer release and dynamic-modifier refresh remain engine behavior, not proven by source walkthrough.
No game launch or probability evaluation was performed.
The unchanged live decision's weighted block remains parent/auditor ownership.
Required read-only MCP inspection was attempted with `hoi4.event_inspect`, `mode = state_flow`, event `chaosx.nr16.1`, `maxDepth = 1`, `maxNodes = 8`, and `expandHelpers = true`.
The request remained running without a response across repeated waits and its orchestration cell was terminated.
No artifact or validation result was returned, so this pass has no MCP lifecycle evidence and does not substitute its source review for that evidence.

Required guidance used: AGENTS.md, `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`, with the offline core wiki pages and vanilla effect, trigger, decision and script-constant documentation consulted during this work session.
The decision documentation's distinction between explicit removal and expiry is why the cleanup review requires cancellation before removal.
No skills were changed and no gameplay simplification was introduced by this review.

Reviewed SHA256 after the parent's cleanup addition:

- Effects: `37365a1ddbd50d72467679a2789f9059c71569e7a08adb1e198169199bb47e09`.
- Triggers: `a7c596b3283039c03a8f292092d0043929f3f768299e8488bc64e5c6a5a609c5`.
- Constants: `767daad3cf47e1e8d7c0b0041874bd6489e52f80f3b675e2a50b6ed9c3d44b8e`.

## Live integration re-review, 2026-09-08

Disposition: implemented source integration reviewed, probability comparison and engine lifecycle evidence remain separate.
This section supersedes the earlier statements that the live decision, compatibility wrapper and terminal hook were unwired.
No blocking integration defect was found in the reviewed source.
Only this review document was edited by the reviewer.

The live decision at `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt:63` uses the new requirements and inclusive four-cost predicate, native PP cost zero and PP hint 65.
The file-local native factory constant is four, matching the admission/display profile, and native duration/cooldown reference the accepted 90/30 constants.
The old batch payment and lifetime-cap check are absent from this decision.
Its admission has no manpower, truck or military-factory burden, including the inspected operational helper chain.
The unchanged `ai_will_do` has exactly the existing medium base and no additional modifiers, but this source equality is not a probability comparison.

Start calls the receipt-paying core and shows its started tooltip only with a complete current receipt.
The native cancellation trigger covers both an invalid receipt and lost operations, whose real-site gate includes ownership and PREV control.
Explicit `cancel_if_not_visible = no` keeps cancellation under that receipt-aware trigger rather than losing the refund path merely because visibility closes.
The cancel callback invokes the complete-receipt refund helper, and the expiry callback invokes the compatibility helper with the completed tooltip gated by the fresh finished result.
`common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt:165` is now a thin call to finish, with no residual rifle/support output or duplicate history increment.
The source reference search found one native begin caller and one native compatibility-finish caller, preserving the documented single-timer boundary.

The terminal integration at `common/scripted_effects/016_brilliant_scientist_effects.txt:4038` calls maturation cleanup first in the existing country-scoped world-end cleanup helper.
Its two immediate callers in `016_brilliant_scientist_super_event_effects.txt` invoke it directly in their country scope without a state iterator or event-target scope switch around the call.
The maturation helper cancels and clears the receipt before removing the decision.
With a complete receipt, first cleanup refunds PP/support/fuel once and then removes the timer.
With a partial or malformed receipt, first cleanup clears all fragments without refund or clone output and then removes the timer.
Repeated cleanup, cancellation after cleanup, or a subsequent expiry call sees no receipt, so cannot refund again, increment history or create equipment.
No helper creates factories or invents a scripted CIC refund.

The four scripted-localisation selectors match the inclusive admission thresholds individually and reference the English cost keys.
The aggregate cost shows exactly those four resource groups.
The existing growth description describes physical clone reserves and identity history, not the removed infantry/support kit.
The completed text and actual output agree at the accepted current tuning of 100 clones, and the text correctly distinguishes reserve-derived weekly manpower from an immediate manpower or division award.
As previously documented, completed text reads the current profile while output is receipt-snapshotted, so a future mid-cycle tuning change could make the displayed quantity differ from that already-paid receipt.
That is a presentation limitation, not a payment/output mismatch at the reviewed tuning.

Read-only MCP trace for `chaosx.nr16.1`, depth one, maximum six nodes and helper expansion returned `EVENT_INSPECTED_PARTIAL`.
Its validation reports `passed = false` because workspace-wide helper projections and lifecycle passes were deferred, with zero projected helpers.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed193989cb8456f89a50f7040a17c3982bcb711dd112756654ebacdfa3b44dfc/014bf767aa66ef4fee2419477d964b3e7454afabae5f7715e041b588ff5bfb70/event-trace-4bccb6ec7fe1.json`.
This artifact is a partial Event016 inspection, not clone-maturation decision lifecycle proof.
This re-review used actual source call paths and branch walkthrough, not an executed timer simulation, and did not rerun the implementation worker's interpreter assertions.
Remaining evidence ownership is the parent's final source/test acceptance and the probability auditor's matching-scenario comparison, with native engine behavior unproven here.
