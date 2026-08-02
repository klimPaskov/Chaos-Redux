# Fallout NZL numbered sea-road decision and mission audit

Date: 2026-07-22

Status: **PASS — no actionable defect found in the promoted sea-road correction.**

## Audit boundary

Read-only audit of the dormant New Zealand Lifeboat State sea-road correction
promoted by `FALLOUT_NZL_LIFEBOAT_PILOT_DEPTH_REVIEW.md` and implemented in
`subagent_handoffs/fallout_nzl_sea_road_implementation_2026-07-22.md`.

Reviewed surfaces only:

- `common/decisions/fallout_consolidated_decisions.txt`
- `common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt`
- `common/script_constants/fallout_consolidated_constants.txt`
- `common/scripted_triggers/fallout_consolidated_triggers.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt` and `.md`
- `common/national_focus/fallout_consolidated_focus.txt`
- `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt`
- `localisation/english/fallout_consolidated_l_english.yml`
- promoted pilot specification and sea-road implementation handoff

No gameplay or localisation source was edited. This handoff is the only file
written by the audit.

## Issue list, sorted by severity

No critical, major, moderate, or minor implementation defect was found.

The only outstanding limit is runtime evidence: HOI4 was deliberately not run,
and the package remains dormant pending its separate allocator gate. That is a
validation limitation, not a source defect in this correction.

## Acceptance evidence

| Check | Result | Exact evidence |
| --- | --- | --- |
| Fishery Political Power and manpower transaction | Pass | `fallout_nzl_fishery_quota_compact` sets `cost = constant:fallout_nzl_cost.political_power_low` and debits `manpower_low` in its completion transaction (`common/decisions/fallout_consolidated_decisions.txt:187-220`). Those constants are `25` and `350` (`common/script_constants/fallout_consolidated_constants.txt:169-175`). |
| Licensed fishery convoy transaction | Pass | Current licensing requires `convoy_low` in both availability and custom-cost trigger, then debits that same constant only in the current-licence branch (`common/decisions/fallout_consolidated_decisions.txt:193-220`). `convoy_low = 5` (`common/script_constants/fallout_consolidated_constants.txt:183`). |
| Licensed Quiet-Seas transaction | Pass | Current licensing selects `convoy_medium`; stale/non-licensed state selects `convoy_low`; both branches require and debit `navy_experience` (`common/decisions/fallout_consolidated_decisions.txt:920-962`). The constants are 10, 5, and 12 (`common/script_constants/fallout_consolidated_constants.txt:174,183-184`). |
| 4 / 7 / 12 value contract | Pass | Shared values define minor/moderate/major as 4/7/12 (`common/script_constants/fallout_consolidated_constants.txt:63-68`). Fishery applies +7 Food, then +4 Sea-Lane Security only with licensing and -4 otherwise (`common/decisions/fallout_consolidated_decisions.txt:225-240`). Quiet-Seas applies +12 only with current licensing and +7 otherwise (`common/decisions/fallout_consolidated_decisions.txt:973-986`). |
| 90-day, generation-bound single patrol window | Pass | `cooldown = 90` (`common/script_constants/fallout_consolidated_constants.txt:253-264`). The issue helper writes one timed flag, stamps generation, increments serial, and only adds the modifier if absent (`common/scripted_effects/fallout_consolidated_effects.txt:82-101`). The current trigger requires package, licence, timed flag, matching generation, and positive serial (`common/scripted_triggers/fallout_consolidated_triggers.txt:91-101`). |
| Custom-cost display/payment parity | Pass | Fishery and patrol scripted-localisation switches select the licensed or non-licensed display from the same current-licence trigger (`common/scripted_localisation/fallout_consolidated_scripted_localisation.txt:41-75`). English cost rows read the same `manpower_low`, `convoy_low`, `convoy_medium`, and `navy_experience` constants as the transactions (`localisation/english/fallout_consolidated_l_english.yml:153-158,201-209`). The fishery tooltip explicitly preserves its separately listed 25 Political Power cost. |
| Isolation AI five-convoy reserve | Pass | Licensed Fishery AI weight is zero below `convoy_medium` (10), while its payment is `convoy_low` (5), leaving five hulls after an AI cycle (`common/decisions/fallout_consolidated_decisions.txt:242-252`; constants at `common/script_constants/fallout_consolidated_constants.txt:183-184`). Quiet-Seas itself still requires the licensed ten-hull affordability gate (`common/decisions/fallout_consolidated_decisions.txt:920-944`). |
| External and Year 10 score-only pressure | Pass | The sea-road helper modifies temporary `fallout_nzl_chain_score` by +4 for a current window and -4 for a lapse, only for current isolation licensing (`common/scripted_effects/fallout_consolidated_effects.txt:114-130`). Its only call sites are the external and late calculators (`common/scripted_effects/fallout_consolidated_effects.txt:1237,1310`). |
| No recurring polling | Pass | The reviewed source contains no `on_daily`, `on_weekly`, or `on_monthly` reference. Natural expiry is handled by the dynamic modifier's remove trigger (`common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt:8-13`) and documented in `common/scripted_effects/fallout_consolidated_effects.txt:49-51`. |
| Cleanup, idempotency, and stale-state safety | Pass | Package reset closes the window then clears active licensing, generation, serial, and the fishery reveal (`common/scripted_effects/fallout_consolidated_effects.txt:157-162,223`). The modifier removes itself when the current-window trigger fails (`common/dynamic_modifiers/fallout_consolidated_dynamic_modifiers.txt:8-13`), and all decision, score, and effect branches use the fail-closed current-licence trigger. |
| Focus and route lock | Pass | `fallout_nzl_license_every_sea_road` remains package-gated, preserves its immediate +7 security reward, opens Last-Berth Closure, and invokes the licensing helper without convoy removal (`common/national_focus/fallout_consolidated_focus.txt:289-304`). The focus is the isolation-route prerequisite for the harbour-constable continuation (`common/national_focus/fallout_consolidated_focus.txt:305-316`). |
| Counts and dormant boundary | Pass | Static count is 18 category decisions/missions and 42 NZL focus ids. Repository search found `fallout_nzl_activate_lifeboat_package` only at its dormant helper definition and its documentation (`common/scripted_effects/fallout_consolidated_effects.txt:528-579`, `.md:85`), not at a caller. No Zombie reference appears in any reviewed source. |

## Decision category lifecycle notes

Owner: `NZL`; category: `fallout_nzl_lifeboat_category`.

- The category is package-gated at each affected decision. A stale package makes
  the decisions unavailable or cancels their active transaction; no fallback
  target, cheaper licensed path, or stale score effect remains.
- `fallout_nzl_license_every_sea_road` writes the licensing receipt and opens
  the pre-existing fishery decision. It does not charge convoys at focus
  completion, so resource affordability remains an explicit decision-time
  transaction.
- Fishery Quota Compact is a 35-day reusable peacetime cycle with a 90-day
  re-enable interval. Licensed completion refreshes a single patrol window;
  unlicensed completion preserves the previous security loss.
- Quiet-Seas Patrol is a distinct, one-shot 70-day wartime operation. It is
  locked to the current exact pirate war, active only after the isolation
  route's relevant receipts, and cancels when the package, war, or settlement
  becomes invalid.

## Mission quality notes

| Action | Owner / category | Region and requirement | Duration | Success | Failure / cancellation | Duplicate risk |
| --- | --- | --- | ---: | --- | --- | --- |
| Fishery Quota Compact (decision cycle) | NZL / Lifeboat category | Package current; fishery reveal; Sea-Lane Security above Critical; licensed branch additionally needs 5 convoys | 35 days | +7 Food; licensed: +4 Sea-Lane Security and refreshed window; unlicensed: -4 Sea-Lane Security | Package invalidation cancels the in-progress action after costs are committed | Low: peacetime food/patrol operating cycle, mechanically distinct from war patrol |
| Quiet-Seas Patrol (timed mission) | NZL / Lifeboat category | Isolation route, exact current pirate war, access revoked, no settlement; 12 Navy XP plus 10 licensed or 5 unlicensed convoys | 70 days | Licensed: +12 Sea-Lane Security and refreshed window; unlicensed: +7 Sea-Lane Security | Package/war/settlement invalidation cancels and applies -4 Parliament Trust | Low: one-shot exact-war surge, distinct target, duration, factory commitment, cost, and outcome |

## Cost and requirement clarity

- The custom-cost entries are concise and icon-first. Their normal, blocked,
  and tooltip forms are all present for both licensing states.
- The recurring distinction is player-facing: five convoy hulls on the
  licensed fishery, ten on the wartime licensed patrol, and a 90-day window.
  The focus and action descriptions avoid implementation-history wording.
- The normal Political Power cost remains engine-listed, while the custom
  fishery tooltip explicitly says the manpower and convoy costs are in
  addition to listed Political Power. Vanilla uses this combined normal-cost
  and custom-resource-cost pattern (for example,
  `common/decisions/AUS.txt:1633-1645`).

## AI validity and route-lock notes

- The reserve test is present only where the specification requires it: the
  reusable licensed Fishery cycle. At 10 hulls the AI can pay five and retain
  five; at 9 or fewer its weight is zero.
- Quiet-Seas has its own exact-war visibility and current licensed/unlicensed
  affordability branches. It cannot retarget a dead, settled, or substitute
  aggressor because the existing pirate-war trigger gates the action.
- Humanitarian logic is unaffected: the scoring helper first requires the
  isolation-route flag, and its only two callers are external and Year 10.

## Localisation and tooltip gaps

No gap found in the promoted sea-road text. The relevant English file remains
UTF-8 with BOM. Dynamic display keys use the same script constants as payment
logic rather than copied 5/10/12/90 literals.

## Cleanup and exploit-risk notes

- Reissuing a patrol window refreshes one named timed flag and one dynamic
  modifier; it does not stack timers or modifiers. Serial increments are
  generation-local and become inaccessible when the flag expires.
- Reset clears all sea-road records and removes the dynamic modifier. A stale
  package also makes the modifier's enable/current trigger false.
- Fishery has a 90-day re-enable interval and paid licensed cost. Quiet-Seas
  is one-shot. These controls prevent free-window, equipment-farming, and
  repeated-security reward loops within the correction's scope.

## Recommended fixes

None. Parent patching is not required for this audited correction.

## Meaningful validation performed

- Static transaction trace from constants through availability,
  custom-cost trigger/display, completion debit, result value change, and
  patrol-window helper.
- Static call-site audit proving the sea-road score helper has two callers:
  external and Year 10 only.
- Static count: 18 decisions/missions and 42 focus ids.
- Static dormant-boundary search: no activation caller and no Zombie reference
  in the reviewed surfaces; no daily, weekly, or monthly on-action reference.

## Skipped meaningful validation

HOI4 was not run by task instruction. Consequently, actual UI rendering,
custom-cost colouring, timed-flag expiry, dynamic-modifier removal, and live
AI selection remain to be proven only when the separately gated allocator can
activate the package.

## Remaining issues outside this audit

Successor allocation, state-conflict disposition, vanilla NZL AI-plan
retirement, the radio portrait blocker, multiplayer/target retention, province
sweep, map return, and live runtime proof remain outside this correction.
