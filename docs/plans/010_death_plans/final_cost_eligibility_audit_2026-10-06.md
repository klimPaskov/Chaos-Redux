# Event 010 Death Final Cost Eligibility Audit

Date: 2026-10-06. Status: `unresolved` for MCP comparison; the current source pairs were reviewed read-only and this report is the only file written by this audit.

## Scope and source identity

The audit covers `death_select_transit_custodianship`, `death_maintain_transit_custodianship`, `death_open_black_book`, `death_whisper_to_zol`, `death_take_black_oath`, `death_offer_prison_census`, `death_feed_border_to_death`, and `death_break_black_oath` in `common/decisions/010_death_decisions.txt`, their cost gates in `common/scripted_triggers/010_death_triggers.txt`, payment effects in `common/scripted_effects/010_death_effects.txt`, and nominal tuning in `common/script_constants/010_death_constants.txt`.

The baseline `HEAD` commit was `ce0b926dc78a129037d3196ea0b747d75b580817`; its decision file was supplied from `git show HEAD:common/decisions/010_death_decisions.txt` as the full 1,300-line `before.inlineClausewitz` value. The Git blob was `4ba22180b076320aef777d7d878c02daf7324664`.

The current decision file has 1,310 lines and SHA-256 `2D1A76C5D152F0EC34C8C527EA7F4951CD0E5502A8D83DE40F0E451245A6CF62`. Current helper/constants SHA-256 values are `457E7C74383B12E3B5C16637799BEBF66C484D80CC719F50DB3A723892A57BF2` for triggers, `D9F7456C91D73776AAC5FE52A85D79511660A2EC039F4E20177A00CA0CEC590B` for effects, and `95D2CFE478EC4B1C325059DB43929C7D6290023634CA466D3C2FA5E89A791DA6` for constants.

## Current gate and payment parity

Each of the six Stability purchases checks the same dynamic Stability quote in its `can_pay_*` trigger and debits that quote in its `death_pay_*` effect through `add_stability` after multiplying the payment by the negative-one constant:

| Decision | Gate helper | Payment helper | Nominal source Stability spend |
| --- | --- | --- | ---: |
| `death_open_black_book` | `can_pay_death_open_black_book_cost` | `death_pay_open_black_book_cost` | 0.08 |
| `death_whisper_to_zol` | `can_pay_death_whisper_to_zol_cost` | `death_pay_whisper_to_zol_cost` | 0.05 |
| `death_take_black_oath` | `can_pay_death_take_black_oath_cost` | `death_pay_take_black_oath_cost` | 0.12 |
| `death_offer_prison_census` | `can_pay_death_offer_prison_census_cost` | `death_pay_offer_prison_census_cost` | 0.03 |
| `death_feed_border_to_death` | `can_pay_death_feed_border_cost` | `death_pay_feed_border_cost` | 0.05 |
| `death_break_black_oath` | `can_pay_death_break_oath_cost` | `death_pay_break_oath_cost` | 0.10 |

The gate and payment pairs use the matching `global.black_friday_price_death_decision_cost_<decision>_stability` variable. The decision availability/custom-cost paths invoke the corresponding gate, and their completion effects invoke the corresponding payment helper. The localized base and blocked cost strings display the same Stability quote for these six decisions. These are source-parity findings; the Black Friday-adjusted quote at runtime remains scenario-dependent.

Transit setup and upkeep are also internally paired in the current source. `can_pay_death_transit_custodianship_policy_cost` and `death_pay_transit_custodianship_policy_cost` use the same fuel, support-equipment, and truck quote variables. `can_pay_death_transit_custodianship_upkeep` and `death_pay_transit_custodianship_upkeep` use the matching upkeep quote variables. The payment helpers debit the truck amounts as `motorized_equipment_1`. The decision cost rows display support equipment, trucks, and fuel; setup additionally explains custodial capacity in its effect tooltip.

The `HEAD` baseline already contains the Transit setup and upkeep truck checks and debits. Therefore this `HEAD`-to-worktree comparison cannot prove that the truck restoration occurred. It can only document that the current gate, debit, and cost row agree.

The current setup and upkeep helpers also omit command-power and train checks and debits that are present in `HEAD`; the current localized rows omit those components too. The numeric constants and Black Friday price table still define and publish the corresponding command-power and train quote variables, but the current Transit decision gates, payers, and cost rows do not consume or display them. This is a cost-component difference from `HEAD`, even though the remaining numeric quote values were not retuned. This audit records the difference without choosing its balance target.

The six Stability additions are gate-helper changes; their payment effects already use the matching Stability quotes. The decision file's eight AI weight blocks and `ai_hint_pp_cost` values were not changed in this patch. The parent's separate source scan reports 29 sale-aware payer/gate pairs with matching quote-variable sets and 68 base/blocked cost rows across 34 custom-cost families, each with no more than three displayed amounts; that broader count is parent-provided evidence, not a result of this compare.

## Single probability comparison attempt

No new `probability_inspect` was run. The available earlier decision inspection covered only `death_survey_the_wasteland`, `death_interrogate_empty_road`, and `death_seal_names_in_iron`; its source revision `e6e5f024833de22f656879dca26e8498f20a0a8be994cb31313ae8d087efca7e` and artifact do not cover this eight-decision pool or Stability/Transit scenarios, so they were not treated as a suitable baseline.

Exactly one `hoi4.probability_compare` request was submitted with adapter `decision_ai_will_do`, the eight IDs listed above, `before.inlineClausewitz` from the `HEAD` decision file, `after.path = common/decisions/010_death_decisions.txt`, and `outputs = [json, comparison, unresolved]`. No refresh was requested.

The request used scenario set `E010_DEATH_FINAL_COST_ELIGIBILITY_2026_10_06` with the synthetic scenarios `STABILITY_BELOW_ALL`, `STABILITY_EQUAL_OFFER_CENSUS`, `STABILITY_EQUAL_WHISPER_FEED`, `STABILITY_EQUAL_OPEN_BOOK`, `STABILITY_EQUAL_BREAK_OATH`, `STABILITY_EQUAL_TAKE_OATH`, `STABILITY_ABOVE_ALL`, `TRANSIT_TRUCK_BELOW_SETUP_AND_UPKEEP`, `TRANSIT_TRUCK_EQUAL_SETUP`, and `TRANSIT_TRUCK_EQUAL_UPKEEP`. The Stability assumptions used nominal source quotes of 0.03, 0.05, 0.08, 0.10, and 0.12; the Transit assumptions used nominal setup/upkeep truck quotes of 100 and 50. These are declared synthetic inputs, not observed campaign values or sale-adjusted prices.

The submitted candidate pool contains only these eight decision IDs. The Transit state-target scope pools were declared `complete = false`; no complete category-wide decision pool or complete live state map was asserted. The comparison returned the exact client error `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: Transport closed`. No comparison artifact, comparison ID, source revision, scenario hash, ranking, modifier trace, pool-completeness result, or unresolved-item report was returned. No retry was made.

## Evidence limits

The `before` source was the decision file only. Any referenced scripted triggers and effects resolve from the current workspace on both sides unless the analyzer explicitly snapshots those dependencies. Consequently, even a returned comparison would not prove a true before-helper versus after-helper delta for the new Stability gates or Transit cost helpers. The compare also targeted willingness scores, not click probabilities; the restricted pool and incomplete target maps preclude normalized selection claims. The synthetic scenario names above are request inputs, not returned or evaluated scenario evidence.

The final AI/cost eligibility result is therefore `unresolved` at the MCP comparison layer. This audit made no gameplay edits and staged or committed nothing; it wrote only this report.
