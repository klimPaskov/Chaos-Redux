# Event 006 FORM-05 compact cost localisation handoff

## Scope

This tranche updates only the FORM-05 decision cost strings in `localisation/english/006_independence_wave_form05_l_english.yml`. Gameplay effects, triggers, decision ids, constants, and icons were not changed.

## Source-applied changes

- Replaced the padded prose for delegation, shipping, opening, customs, capital, shipping-board, customs-clearinghouse, and first-board-ratification costs with compact icon-first bundles.
- Reused the existing `£command_power`, `£manpower_texticon`, `£convoy_texticon`, `£GFX_train_texticon`, and `£civ_factory` icon family already used by the FORM-05 surface.
- Reused the shared `independence_wave_decision_cost` values and the FORM-05 `combined_command_power` constant. The opening, customs, and customs-clearinghouse strings therefore disclose the same 30 command-power commitment consumed by the combined administrative/diplomatic payment effect.
- Changed available tooltips to reference their matching compact cost key, avoiding duplicate prose.
- Changed the affected blocked strings to explicit red icon-first costs with an `Unavailable:` prefix.

## Consumer crosswalk

The eight changed base keys remain the `custom_cost_text` consumers at lines 43, 85, 149, 213, 247, 382, 463, and 502 of `common/decisions/006_independence_wave_form05_decisions.txt`. Their existing custom-cost triggers and payment effects remain unchanged.

## Validation

- The localisation file retains its UTF-8 BOM and contains no NUL bytes.
- Each affected base key, `_tooltip` key, and `_blocked` key remains unique.
- The affected strings no longer contain literal `Command Power`, `manpower`, `convoys`, `civilian factory`, `Commits`, or padded conjunction prose.
- The source constants and decision consumers were re-read after the edit to confirm that the disclosed bundles match the existing payment helpers.

## Remaining scope

This closes only the FORM-05 cost-prose subtranche. Other Event 006 package-cost prose, uncosted surfaces, category-density review, typed-probability evidence, package admission, and live tooltip/runtime receipts remain queued under the whole-event HOLD / PARTIAL boundary.
