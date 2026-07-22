# Fallout NZL Numbered Sea-Road Implementation Handoff

Date: 2026-07-22

Status: bounded depth-review correction implemented in the dormant NZL Lifeboat State pilot

## Accepted gap and disposition

The depth review in `FALLOUT_NZL_LIFEBOAT_PILOT_DEPTH_REVIEW.md` found that `fallout_nzl_license_every_sea_road` promised operating permits and patrol windows but previously delivered only a one-time value exchange. The parent accepted and promoted the recurring decision-loop correction. The broader expansion ideas in that review remain rejected as bloat.

## Implementation

- The focus writes a current-generation licence receipt and opens the existing Fishery Quota Compact.
- A licensed Fishery Quota Compact consumes five convoys in addition to its existing Political Power and manpower costs.
- The licensed fishery result raises Food Security by seven and Sea-Lane Security by four.
- A licensed Quiet-Seas Patrol consumes ten convoys and twelve Navy Experience.
- The licensed wartime result raises Sea-Lane Security by twelve.
- Both licensed actions issue or renew one generation-bound 90-day patrol window.
- Every issued window increments one licence serial for package memory.
- A visible dynamic modifier grants 0.10 naval detection and 0.10 convoy escort efficiency while the window is current.
- A maintained window adds four points to isolation-route external and Year 10 scoring.
- A lapsed window subtracts four points from the same two scores.
- The unlicensed branches preserve the earlier fishery security loss and five-convoy Quiet-Seas cost.
- Isolation AI refuses the licensed fishery action below a ten-convoy reserve and prefers it when the window has lapsed.
- Cleanup clears the licence flag, licence generation, timed flag, window generation, serial, and modifier.

No focus, decision, lifecycle-idea, event, or character block was added. The reviewed counts remain 42 focuses, 18 decisions, 14 lifecycle ideas, 26 event blocks, and 6 fictional characters. One visible dynamic modifier is used and is not counted as a lifecycle idea.

## Tuning source

- Decision costs use `fallout_nzl_cost.convoy_low`, `fallout_nzl_cost.convoy_medium`, `fallout_nzl_cost.navy_experience`, `fallout_nzl_cost.manpower_low`, and the existing Political Power cost.
- The window duration uses `fallout_nzl_duration.cooldown` through a temporary variable accepted by the timed-flag duration field.
- Value changes reuse the existing minor, moderate, and major value constants.
- Detection, escort, maintained-score, and lapsed-score values live in `fallout_nzl_sea_road`.
- Player cost text reads the same script constants through scripted localisation.

## State and transaction proof

`fallout_nzl_sea_road_licensing_is_current` requires the dormant package, active licence flag, generation receipt, and current Fallout transition generation.

`fallout_nzl_sea_road_patrol_window_is_current` additionally requires the timed window flag, matching window generation, and a positive serial. The issuing helper refreshes that one timed flag rather than stacking timers.

Fishery costs are paid in `complete_effect` only after the custom affordability trigger passes. Its result issues the window only if licensing is still current. Package invalidation cancels the action through the existing package gate.

Quiet-Seas costs are five convoys without licensing and ten convoys with current licensing. Cancellation does not delete a previously earned window. Successful licensed completion renews the window. The exact recorded pirate war remains required.

The score helper is called only by `fallout_nzl_calculate_external_result` and `fallout_nzl_calculate_late_result`. The no-partner external path remains a direct failure and does not fabricate score relief.

## Engine references

The implementation was checked against:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` for `add_dynamic_modifier`, `remove_dynamic_modifier`, `force_update_dynamic_modifier`, and timed country flags.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` for flag, variable, and equipment affordability checks.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md` for the country-scoped naval detection and convoy escort modifiers.
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` for custom costs, removal effects, re-enable timing, and AI weights.
- `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md` for dynamic-modifier enable and removal behavior.
- Vanilla decisions with a Political Power cost plus a separate `custom_cost_trigger` and `custom_cost_text`, including `common/decisions/GER.txt`.

## Asset proof

The patrol window reuses the dedicated NZL Fallout `GFX_idea_fallout_nzl_lifeboat_navy` sprite already defined in `interface/fallout_world_end.gfx`. No Zombie sprite, texture, path, or audio is referenced. No additional art is required.

## Static review boundary

- Focus, decision, lifecycle-idea, event, and character counts are unchanged.
- The cost display branches use the same script constants as the payment effects.
- The timed flag is generation-bound and has one duration owner.
- External and Year 10 scores have equal and opposite four-point adjustments.
- No daily, weekly, or monthly on action was added.
- No Fallout activation caller was introduced.

HOI4 was not run, as requested. Live decision display, timed-flag expiry, modifier removal, and score behavior remain unverified until the dormant package is allowed to activate through the future allocator.

## Remaining limits

This closes only the accepted sea-road depth correction. It does not resolve successor allocation, tag conflicts, vanilla NZL AI-plan retirement, the blocked Radio Service Coordinator portrait, host authority, the exact manual province sweep, or normal-map Air Winter runtime proof.
