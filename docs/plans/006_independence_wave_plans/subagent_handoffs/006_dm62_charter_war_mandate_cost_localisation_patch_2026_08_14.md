# Event 006 DM-62 charter-war mandate cost-localisation handoff

Date: 2026-08-14

Scope: Current admitted Event 006 decision and mission sources after the DM-01 material-cost repair and Komi lifecycle, cost, and tooltip repairs.

Excluded surfaces: DM-01, IW-050 Komi, Iberian serialization, central admission, deterministic Join, portraits, flags, and the event catalog workbook.

## Disposition

One concrete source-backed cost-clarity defect was found and repaired in the owned DM-62 decision/localisation surface.

DM-62 `independence_wave_request_charter_war_mandate` reserved one civilian factory through `@CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT`, but its generic diplomatic cost text displayed only Command Power and convoy-or-train capacity.

The accepted matrix requires “diplomatic-standard cost and one civilian factory” for DM-62 (`docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv:63`).

## Changed files and identifiers

- `common/decisions/006_independence_wave_decisions.txt:2925` now selects `independence_wave_cost_diplomatic_standard_factory` only for `independence_wave_request_charter_war_mandate` (DM-62).
- `localisation/english/006_independence_wave_decisions_l_english.yml:29` adds `independence_wave_cost_diplomatic_standard_factory`.
- `localisation/english/006_independence_wave_decisions_l_english.yml:58-59` adds `independence_wave_cost_diplomatic_standard_factory_tooltip` and `independence_wave_cost_diplomatic_standard_factory_blocked`.

No cost helper, effect, constant, AI weight, route gate, admission list, Join entry, GUI definition, asset, or workbook was changed.

## Before and after behavior

Before the patch, DM-62 used `custom_cost_text = independence_wave_cost_diplomatic_standard` while the same block reserved `civilian_factory_use = @CR_SC_INDEPENDENCE_WAVE_DECISION_COST_CIVILIAN_FACTORY_LIGHT`.

The generic base, tooltip, and blocked text omitted the factory, so the decision card did not disclose the full accepted commitment even though the source applied it.

After the patch, DM-62 uses the dedicated factory-aware triplet.

The base card shows Command Power, standard convoy-or-train capacity, and `civilian_factory_light`.

The tooltip and blocked text state the same dynamic factory requirement.

The new text reads the existing `independence_wave_decision_cost.civilian_factory_light` constant, which is currently `1` at `common/script_constants/006_independence_wave_decision_constants.txt:159`; no duplicate tuning literal was introduced.

The generic `independence_wave_cost_diplomatic_standard` triplet remains unchanged for its seven other decision call sites, so decisions without the accepted factory commitment do not gain a false factory cost.

## Severity-sorted findings

### P1 fixed — DM-62 cost display omitted an active factory commitment

The accepted DM-62 row requires a diplomatic-standard cost plus one civilian factory.

The source already reserved that factory, but the generic cost triplet showed only the diplomatic portion.

The narrow selector and localisation triplet now align the player-facing card with the existing source behavior and matrix.

### P2 unresolved by design — whole Event 006 remains HOLD / PARTIAL

The current source-of-truth map still records the central content-attestation boundary, package evidence, and live consumer limits as whole-event blockers.

Those boundaries are outside this patch and do not justify widening admission or changing Join.

## Decision lifecycle notes

DM-62 belongs to the League Enforcement category and is a targeted timed decision owned by a compliant Event 006 league member.

Its target root requires a recognized-or-later applicant, charter compliance, the mutual-defence charter flag, the defensive-congress route, no active league crisis, and a live external country that is not a League member and is legally declarable.

The target is a capital state whose owner still passes `is_valid_independence_wave_charter_war_authorization_target`.

The decision runs for `constant:independence_wave_decision_duration.rapid`, currently the accepted 45-day deliberation, and uses the existing standard re-enable cooldown.

Completion pays the existing diplomatic-standard helper and stores the selected league target.

Removal resolves the selected target into one target-specific 365-day authorization flag and records its date.

Cancellation applies the existing cohesion/common-cause/reserve/confidence deltas and clears the active target without issuing a mandate.

The war on-action consumes the authorization only for a matching declaration; unrelated offensive declarations remain subject to the existing charter-breach path.

## Mission quality notes

| Surface | Owner/category/region | Requirement and duration | Success/failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| DM-62 `independence_wave_request_charter_war_mandate` | Recognized compliant league member / League Enforcement / selected external capital | Mutual-defence pillar, defensive-congress route, no active crisis, legal external target, diplomatic-standard cost plus one factory, 45 days | One 365-day authorization against the selected external country on completion; cohesion loss and target cleanup on cancellation or failed deliberation | Active target pointer and the existing clear/replacement helper keep one unconsumed mandate per member; matching declaration consumes the flag |

No mission-duration, success, failure, target, or duplicate-lifecycle change was made by this patch.

## Cost and requirement clarity

The decision still uses `can_pay_independence_wave_diplomatic_standard_cost` for both availability and the custom cost trigger.

The one-factory commitment remains the existing `civilian_factory_use` modifier with the file-scoped light constant, and the localisation now exposes that same dynamic value.

No generic diplomatic cost was broadened, and no new gameplay cost was invented.

## AI validity and route-lock notes

No AI weight or probability-bearing source changed.

The existing low DM-62 AI weight and neutral-commission reduction remain untouched.

The target legality, mutual-defence, defensive-congress, crisis, and active-target gates remain untouched.

Because this patch changes only `custom_cost_text` and localisation, no probability comparison is required for a weight delta.

## Localisation and tooltip notes

The new base, tooltip, and blocked keys all use the existing `civilian_factory_light` constant and are present exactly once.

The English localisation file retains its UTF-8 BOM.

The existing selected-formable custom-cost key is intentionally split across the decisions and formable-registry localisation files; the new DM-62 key is self-contained in the decision localisation file.

## Cleanup and exploit-risk notes

No cleanup or effect behavior changed.

The patch changes disclosure only and cannot grant, refund, multiply, or bypass a cost.

The existing active-target cleanup, mandate replacement, mandate consumption, and origin cleanup remain the relevant duplicate and stale-state controls.

## Required evidence

The offline Paradox wiki core pages and the vanilla decision/localisation documentation and precedents were read before the source edit.

The prior mandatory shared decision and mission probability inspections remain the applicable weighted-logic evidence: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48e6446425d09136b75cd3aa37bed85cd8d35b1ce4f193c35391f304be801390/09c8965cfac37c4308892cd7a94fc25cb5a8ef8b98ff29729049e6087c14fc04/probability-inspect-efc4d478e6f2.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d2db102151e09ad515e867e2bfbb2df70069816741b21a6e23fd49281f30f88/bcd11c2ba12b48df9e9ad1b960b336a1467605d8900fe4a162d2d2317dd2d19c/probability-inspect-efc4d478e6f2.json`.

The current post-repair decision-source inspection returned `PROBABILITY_SOURCE_INSPECTED` at source revision `61bf9c2ae0bcf524aa70c2509acd4592e378f670446c7a7e89d5a02ec28fd805`, source hash `149dca17038809614d306860cce698e3eeb19598d005422ca3f034156dd02b97`, with 10 candidates, 0 available candidates under the empty fixture, 79 required inputs, and 0 inspect-unresolved rows. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6bf673ad940656c45a727b2983ea1f64a003289728dc79e1d67a8ba3c2f586e1/402439c88470d479b6c15e30bde831d8c38081e41126d799f65f4d25ad77ad08/probability-inspect-149dca170388.json`.

Those inspections reported incomplete candidate pools and therefore do not support quantitative balance claims; this cost-text-only patch does not alter those surfaces.

DM-62 uses the ordinary decision framework rather than a named event-owned scripted GUI, so no GUI rewrite was attempted.

The unchanged shared status-window GUI evidence remains in `006_current_decision_gap_audit_2026_08_14.md`; this patch does not alter that surface.

## Validation

- Extracted the current DM-62 block and asserted its diplomatic-standard trigger, factory-aware custom-cost selector, light factory modifier, rapid duration, and diplomatic payment helper.
- Confirmed exactly one factory-aware selector and seven unchanged generic diplomatic selectors in the shared decision file.
- Confirmed all three new localisation keys exist exactly once and each references `civilian_factory_light`.
- Confirmed all 18 unique shared custom-cost bases resolve globally to base, tooltip, and blocked localisation keys.
- Confirmed the English localisation BOM and ran `git diff --check` on the two source files.

Live HOI4 execution, save/load, and player-facing runtime rendering were skipped because live consumer validation remains parent/user-owned and this patch does not change decision logic beyond the text selector.

## Remaining issues and parent follow-up

No additional safe narrow source patch was found in the requested current admitted decision/mission scope after excluding the repaired surfaces.

The parent should review this two-file source change and retain the Event 006 HOLD / PARTIAL admission boundary.

No portraits, flags, workbook, central admission, or Join edits are required for this repair.
