# Parent Handoff: OGB Rival-Seal Depth and Layout Tranche

Date: 2026-06-04
Owner: parent Codex agent
Scope: Event005 Soviet Collapse focus-tree cleanup and high-chaos reward depth

## Files Changed

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/events/005_soviet_collapse.md`

No flag files or flag sprite folders were touched.

## Focus IDs Changed

- `OGB_treat_with_idel_ural`
- `OGB_the_volga_cannot_have_two_seals`
- `OGB_letters_to_kazan_and_ufa`
- `OGB_answer_the_idel_ural_question`
- `OGB_future_bulgaria_file`

## Behavior

The OGB Volga compact/rival fork was pulled closer to the trunk:

- `OGB_treat_with_idel_ural`: moved to `x = 10, y = 4`
- `OGB_the_volga_cannot_have_two_seals`: moved to `x = 12, y = 4`
- `OGB_letters_to_kazan_and_ufa`: moved to `x = 10, y = 5`
- `OGB_answer_the_idel_ural_question`: moved to `x = 12, y = 5`
- `OGB_future_bulgaria_file`: moved to `x = 11, y = 7`

`OGB_the_volga_cannot_have_two_seals` now immediately presses the Volga trade-city claim package instead of only setting a posture and waiting for later focuses. The focus sets `ogb_trade_city_claims_pressed`, applies `soviet_collapse_apply_ogb_volga_trade_city_claims`, cores controlled trade-city claims, and prepares Idel-Ural war pressure where valid.

The compact route still uses the later `OGB_future_bulgaria_file` and `ogb_press_trade_city_claims` decision path when the claim package has not already been forced by the rival-seal route.

## Remaining Risks

This does not make OGB a full large 40-50 focus tree. It improves one verified layout line and one high-impact route payoff. OGB still needs deeper trade-road, restoration-state, and Volga diplomacy/war branches if the final target is a fully expanded OP high-chaos country.

## Validation

Validation is parent-owned after this handoff.
