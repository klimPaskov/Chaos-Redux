# Event 006 decision/mission final no-safe-gap handoff (2026-08-15)

## Scope and disposition

This is a final read-only scan of the current Event 006 decision and mission surfaces, with repaired DM-01 material costs, Komi lifecycle/cost/tooltip work, Iberian serialization, Join/admission work, and the owner-applied ICE cost/localisation patch treated as out of scope for new edits.

No new safe local gameplay patch was found. The current source has no remaining cost-selector, direct-localisation, or obvious project-lifecycle mismatch that can be corrected without changing shared lifecycle ownership or inventing design.

No gameplay source was edited in this tranche. The current ICE cost/localisation correction is already owner-applied in commit `d6470c5b5` and is not duplicated here.

## Evidence and current findings

- A static crosswalk over 50 `common/decisions/006_independence_wave*.txt` files and 67 Event 006 English localisation files found zero missing `custom_cost_text` base, `_tooltip`, or `_blocked` keys and zero missing direct decision/mission `name`, `desc`, or `custom_effect_tooltip` references.
- The current ICE package cost/effect/localisation crosswalk remains source-backed: the two administrative factory modifiers use the existing one- and two-factory decision-cost constants, the other ICE projects use their existing security/diplomatic/equipment contracts, and the Shipping Registers tooltip discloses its Coastwatch effect. The detailed ICE receipt is `006_iw012_ice_decision_cost_effect_localisation_crosscheck_2026_08_14.md`.
- The current DM-01 material commitment is present in the shared provisional-capital gate/effect path; no additional material-cost repair was identified.

## Remaining issue, classified as not safe to patch here

Severity: medium/high lifecycle ownership blocker, not a local ICE defect.

`has_independence_wave_active_founding_mission` includes `independence_wave_ice_hold_the_harbour` at `common/scripted_triggers/006_independence_wave_decision_triggers.txt:41-44`, but `can_pay_independence_wave_provisional_capital_cost` at line 328 does not consume that helper or otherwise test for an active ICE harbour mission. `independence_wave_start_provisional_capital_mission` calls that gate and activates `independence_wave_secure_provisional_capital` at `common/scripted_effects/006_independence_wave_decision_effects.txt:911-916`.

This may permit the shared DM-01 automatic start and the ICE harbour deadline to overlap on one refresh, but source inspection cannot establish activation order or intended coexistence. A fix would require the central lifecycle owner to decide whether the harbour mission replaces or coexists with DM-01, then validate the decision in runtime/save-load scenarios. Adding a central guard without that decision would be an admission/lifecycle change, so it is not a safe patch for this tranche.

The ICE package documentation also says Coastwatch expansion spends Command Power (`docs/events/006_independence_wave/iw012_ice_package.md:26`), while the current security-standard source, payment helper, and localisation do not spend or disclose Command Power. This is a documentation/spec discrepancy, not a source-backed gameplay defect; it remains queued for the package owner rather than being guessed here.

## Required audit notes

Decision and mission lifecycle: the ICE harbour mission intentionally persists alongside six one-at-a-time paid projects; local package/capital/route cancellation coverage is present. The only unresolved lifecycle question is the shared DM-01 activation ordering above.

Mission quality: `independence_wave_ice_hold_the_harbour` is a 1440-day survival mission with no material payment; the six ICE projects have explicit category, requirement, duration, payment, and cleanup contracts in the detailed ICE handoff. No duplicate-risk defect was found beyond the shared harbour/DM-01 ordering question.

Cost and requirement clarity: current Event 006 direct cost selectors resolve to base, tooltip, and blocked localisation keys. No stale ICE cost key or unresolved factory disclosure remains after `d6470c5b5`.

AI validity and route locks: no new weighted AI or probability-bearing source was changed or proposed. Therefore no new probability MCP call was necessary in this bounded scan. The existing Event 006 probability receipt remains unresolved because the required artifact route reported `ARTIFACT_MANIFEST_INVALID` and an absolute-path retry reported `INTERNAL_ERROR`; this is not treated as balance certification.

Localisation and tooltips: direct key coverage is complete in the current Event 006 English files for the scanned decision/mission surfaces. The Coastwatch Command Power wording mismatch is documentation-only and design-owned.

Cleanup and exploit risk: no new local cleanup or exploit loop was identified. The possible simultaneous DM-01/harbour activation is a shared lifecycle concern requiring owner/runtime evidence, not a safe one-line ICE patch.

## Validation boundary

The static source crosswalk and direct-key scan were run against current files. No GUI inspect/render was applicable because no decision-owned scripted GUI was in scope. No new probability MCP call was run because no weighted surface required a change or balance decision in this final read-only pass. No live game, save/load, or activation-order validation was run; the parent owns that runtime boundary.

## Final recommendation

Close this tranche as **no safe gap**. Preserve the current owner-applied cost/localisation repairs. Queue the shared DM-01/ICE harbour activation question for a central lifecycle owner with an explicit coexistence/replacement decision and runtime evidence before any guard is added.
