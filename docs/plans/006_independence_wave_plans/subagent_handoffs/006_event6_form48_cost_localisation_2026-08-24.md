# Event 006 FORM-48 compact cost localisation handoff

## Scope

This tranche updates only the seven FORM-48 cost families in `localisation/english/006_independence_wave_pacific_l_english.yml`. No decision, trigger, effect, constant, character, country, or GUI source changed.

## Source-applied changes

- Converted invitation acceptance, carrier convoy, carrier procurement, carrier basing, member convoy, member procurement, and member basing costs to compact icon-first bundles.
- Reused the exact `independence_wave_form48_cost` constants already consumed by each decision's `custom_cost_trigger` and payment effect.
- Used the existing `£command_power`, `£convoy_texticon`, `£GFX_train_texticon`, `£fuel_texticon`, `£infantry_equipment_text_icon`, `£support_equipment_text_icon`, and `£civ_factory` icons.
- Replaced duplicated prose tooltips with references to the matching compact cost key.
- Replaced the affected blocked strings with explicit red bundles and an `Unavailable:` prefix.

## Consumer crosswalk

The seven base keys remain the `custom_cost_text` consumers in `common/decisions/006_independence_wave_form48_decisions.txt`. Their existing triggers and payment helpers map as follows:

- Member convoy: command power plus convoys.
- Carrier convoy: command power, convoys, fuel, and civilian factories.
- Carrier procurement: convoys, infantry equipment, support equipment, and civilian factories.
- Carrier basing: command power, support equipment, and civilian factories.
- Member procurement: infantry equipment, support equipment, and a civilian factory.
- Member basing: command power and support equipment.

## Validation

- The localisation file retains its UTF-8 BOM and contains no NUL bytes.
- Every affected base, `_tooltip`, and `_blocked` key is unique and present.
- The seven affected base strings contain no player-facing literal resource names or `Commits` prose outside their scripted constants and icon tokens.
- The corresponding triggers, constants, payment effects, and decision consumers were re-read to confirm resource agreement.

## Remaining scope

This closes the FORM-48 cost-prose subtranche only. Remaining Event 006 package cost prose, uncosted surfaces, category-density review, typed-probability evidence, admission gates, live GUI/tooltips, and the whole-event HOLD / PARTIAL boundary remain open.
