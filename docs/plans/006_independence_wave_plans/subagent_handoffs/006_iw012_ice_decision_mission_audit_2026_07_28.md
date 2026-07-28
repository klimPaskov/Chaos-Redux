# IW-012 Iceland decision and mission audit

> Reconciled 2026-07-28: the route-family HOLD below predates the parent’s four ICE shared-focus consumers and exact vanilla-path carrier. The current bounded decision/mission disposition is PASS after the project-only serialization guard, 1,440-day survival deadline, four route-focus imports, and FORM-02 Nordic-precedence guard. Live timing, AI, save/load, and runtime transaction evidence remain open. See `006_iw012_ice_package_implementation_2026_07_28.md` for the current parent-owned handoff.

## Verdict

**Historical HOLD for route-family completeness; the ICE mission and project loop is mechanically viable after the narrow fixes below.**

The additive ICE package has a valid material-cost project chain and one timed mission, no political-power store, no passive checklist, no free-unit loop, and no unsafe live country target.

The remaining hold described by this pre-carrier snapshot was narrow but real: the vanilla `iceland_tree` could not consume the shared constitutional or traditional route flags, and ICE had no equivalent local decisions. The current exact carrier imports the four route consumers, so use the reconciliation notice and current implementation handoff for present source status.

The emergency-military and patron-client routes are reachable.

## Issues, ordered by severity

1. **Critical — fixed:** `independence_wave_ice_hold_the_harbour` originally timed out after 360 days although its serialized stabilization path requires 1,230 project-days.
   The local mission constant is now 1,440 days, retaining a deadline while allowing the necessary sequence and a network action.
2. **Critical — fixed:** Compact Support started at 15 but the Compact required 55, while the pre-Compact project path could reach only 45.
   `compact_negotiation_threshold = 45` makes the required shipping, council, coastwatch, and former-host sequence viable.
3. **High — fixed:** Armed Neutrality needed Coastwatch 60 although its prerequisite chain reaches 55 before the armed project.
   `armed_neutrality_threshold = 55` permits the completion that delivers the final security requirement.
4. **High — fixed:** The ICE category had no category registration and no description showing the ICE, former-host, network, or League values.
5. **High — fixed:** A patron-client route adapter and idea consumer existed in the concurrent ICE implementation, but the existing shared client decision required `independence_wave_unlock_patron_client_route`, which setup did not publish.
   ICE setup now publishes that existing unlock flag.
6. **High — fixed:** Armed Neutrality could finish after another route locked and then mark its project complete without actually selecting emergency military.
   Its cancel trigger now terminates on `independence_wave_government_route_locked` and applies the established project-failure consequence.
7. **Historical pre-carrier finding:** ICE was an additive-overlay package while the shared constitutional and traditional focus locks lived only in `006_independence_wave_focus.txt`, which was not loaded for `iceland_tree`.
   The current carrier imports the four route consumers and the route locks are now documented in the implementation and focus re-audits.
   The existing ICE route-politics adapter supports both results if another valid consumer calls it, but it does not make them selectable.
   Adding those route decisions is a broader route-system change and remains parent-owned.
8. **Low — remaining:** Shared material-cost guards use strict greater-than resource checks, so the displayed cost is a minimum commitment rather than an exact zero-stockpile threshold.
   This affects the Event 006 shared cost helper, not ICE alone; it was left unchanged.

## Decision category lifecycle

`independence_wave_ice_north_atlantic_category` is visible only while `is_independence_wave_ice_package = yes` and now has its own category definition.

The mission activates once after package setup, cancels successfully on `has_stable_independence_wave_ice_state`, and fails on timeout, lost capital, former-host loss, or package removal.

The six projects serialize through `has_independence_wave_ice_active_package_project`.

Completed projects set unique completion flags; all project and mission IDs are removed by `independence_wave_cleanup_iw_012_ice` on package cleanup.

## Mission quality notes

| Owner | Category / region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| ICE / IW-012 | North Atlantic Republic / state 100 | Package setup, controlled capital, living former host, five ICE ledgers | 1,440 days | All stability thresholds cancel the mission and set `independence_wave_ice_harbour_crisis_resolved` | Timeout, capital loss, host loss, or package removal; ICE suffers the shared project-failure deltas | One activation only; resolved/failed flags prevent reactivation |

The viable sequence is Shipping Registers → Municipal Council → Coastwatch → Former Host Charter → North Atlantic Compact → Armed Neutrality.

Its values move from `25/35/20/20/15` to `75/80/70/65/60` for Authority, Cohesion, Coastwatch, Shipping, and Compact Support, exceeding the `65/65/60/60` stability gates.

## Costs, AI, tooltips, cleanup, and exploit risk

- The projects use the shared administration, security, and diplomatic material helpers: civilian-factory use plus command power/manpower; manpower/army XP/rifles/support equipment; and command power plus convoy-or-train expenditure.
- Each player-visible cost and outcome has a localized custom cost or effect tooltip.
- The category description now shows ICE values, eight former-host ledgers, network standing, and all five League ledgers.
- The AI uses high or urgent decision weights and ICE-only plans gated by package setup; the former-host charter re-checks a living, non-war former host and cancels if that target becomes invalid.
- Cleanup removes every ICE project/mission, lifecycle and route ideas, ICE flags, and the five ICE variables.
- Projects are one at a time, do not grant units or equipment, and pay their materials before completion; completion flags and `fire_only_once` on Armed Neutrality prevent farming.

## Changed files and identifiers

- `common/decisions/categories/006_independence_wave_ice_categories.txt`
  - Added `independence_wave_ice_north_atlantic_category` registration.
- `localisation/english/006_independence_wave_ice_l_english.yml`
  - Added `independence_wave_ice_north_atlantic_category_desc`.
- `common/script_constants/006_independence_wave_ice_constants.txt`
  - Added `independence_wave_ice_value.compact_negotiation_threshold`, `armed_neutrality_threshold`, and raised `independence_wave_ice_duration.harbour_crisis` from 360 to 1,440.
- `common/decisions/006_independence_wave_ice_decisions.txt`
  - Updated the Compact and Armed Neutrality availability thresholds.
  - Updated Armed Neutrality cancellation for an externally locked government route.
- `common/scripted_effects/006_independence_wave_ice_package_effects.txt`
  - Setup now sets `independence_wave_unlock_patron_client_route` so shared decision DM-38 reaches the existing `ice_north_atlantic_patron_mandate` consumer.

The concurrent ICE route-politics adapter and shared selector dispatch were reviewed but are not claimed as this audit's changes.

## Validation performed

- Checked decision/mission fields against the offline Decision Modding wiki and vanilla `SWE.txt`/`ICE.txt` decision patterns, plus the vanilla effects, triggers, and script-constants documentation.
- Confirmed balanced Clausewitz blocks in all ICE decision, category, constants, effects, and triggers files.
- Confirmed every ICE decision localization reference resolves across ICE and shared Event 006 decision localisation.
- Confirmed all ICE-local `constant:` references used by decisions resolve in `006_independence_wave_ice_constants.txt`.
- Checked the exact project-value path and timeline above, the shared network start of 10 against the observed gate of 15, and the existing shared network progression that can raise it.
- Confirmed the route adapter is dispatched directly after the government route locks and that the patron mandate is added and later removed.

## Skipped validation

No live game, save/load, allocator, or AI-playthrough run was performed; repository policy assigns those checks to the parent/user and does not permit launching HOI4.

No commit was made because this ICE package is an untracked, concurrently assembled shared-worktree surface; committing it would risk including work owned by other agents.

## Simplifications, omissions, and blockers

No fallback route or generic-focus rewrite was added.

The former-host-disappearance failure is deliberately retained because the package documentation defines it as a mission failure condition; an alternate recovery route would require explicit design approval.

The preceding route-consumer blocker was a pre-carrier finding and is superseded by the four ICE route consumers imported into `iceland_tree`. Current remaining boundaries are live focus visibility, route-AI activation, save/load, and runtime transaction evidence; the broader shared-focus geometry hold is recorded by the current whole-event audit.
