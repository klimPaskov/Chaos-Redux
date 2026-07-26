# Reviewed Regional Fallout Event 565: The River Ration League

## Status

This is an accepted dormant Fallout regional chain for Europe.

It is an ordinary Fallout event family and is not a super-event.

The scheduler remains fail-closed until the shared Fallout activation flag has a reviewed setter and the live engine proof is recorded.

The chain owns no Air Contamination contribution and does not use zombie ids, assets, audio, sprites, or paths.

## Ownership

The event namespace is `chaosx.fallout`.

The owned event ids are `565` through `571`.

The candidate id is `565`.

The transaction key is `710053`.

The route key is `7153` and its upper bound is `7154`.

The Event Log history id is `9158`.

The report picture is `GFX_report_event_fallout_river_ration_league`.

## Chain blocks

`565` is the human opening event.

`566` is the hidden AI opening event.

`567` is the human delayed result.

`568` is the hidden AI delayed result.

`569` is the human institutional review callback after 180 days.

`570` is the hidden AI callback.

`571` is the cancellation and cleanup event.

The result is due 42 days after the opening choice.

The callback is due 180 days after the result is resolved.

## Corridor selection

The selector considers the following fixed Danube corridor in upstream order: Upper Austria `152`, Austria `4`, Southern Slovakia `664`, Western Hungary `155`, Hungary `43`, Eastern Croatia `109`, Banat `82`, Yugoslavia `45`, Eastern Serbia `108`, Romania `46`, Bulgaria `48`, and Dobrogea `77`.

The first eligible state is frozen as upstream.

The highest eligible later state is frozen as downstream.

The candidate is rejected unless two distinct states pass the current Fallout identity, ownership, controller, generation, population, supply, adaptation, reclamation, exposure, disease, and exclusive-reservation checks.

The current region must be Europe.

Both state rows and both state reservations are revalidated before the delayed result and callback.

## Opening choices

The visible cost is three ordinary Fallout event budget points.

Joint barge law costs Food 6, Fuel 4, and Recognition 3.

Upstream priority costs Food 4, Fuel 3, and Recognition 2.

Armed customs costs Scrap 4, Fuel 6, and Recognition 2.

Flood authority costs Clean Water 4, Scrap 7, and Power 6.

Each choice is available only when its complete resource receipt is affordable.

The opening freezes both states, both owners and controllers, the transition generation, the Air Winter values, the country survival ledger, trust, tension, and the selected branch.

## Deterministic grading

All grade inputs are clamped to the shared zero to one hundred survival range.

Joint barge law uses Cohesion at 25 percent, Recognition at 20 percent, Food at 20 percent, minimum state Supply Access at 20 percent, and Clean Water at 15 percent.

Upstream priority uses Food at 30 percent, Clean Water at 20 percent, upstream Supply Access at 25 percent, Recognition at 15 percent, and Power at 10 percent.

Armed customs uses Fuel at 25 percent, Scrap at 20 percent, minimum state Supply Access at 20 percent, Recognition at 15 percent, and Cohesion at 20 percent.

Flood authority uses Clean Water at 25 percent, Power at 25 percent, Scrap at 20 percent, minimum state Supply Access at 15 percent, and average reclamation at 15 percent.

Ten points are subtracted when either state has exposure at least 70.

Another ten points are subtracted when either state has disease pressure at least 70.

Government archetype adjustments are applied by branch before grading.

Success is a grade of at least 60.

Partial is a grade from 40 through 59.

Failure is below 40.

There is no random roll and no MTTH branch resolution.

## Delayed result and callback

The result changes food, clean water, fuel, power, scrap, recognition, cohesion, Supply Access, reclamation, trust, and border tension according to the selected branch and grade.

The exact result deltas are the accepted values in `2026-07-26_river_ration_league_addendum.md`.

The result does not apply population loss.

The callback applies the accepted 180-day institutional review deltas for the selected branch and result grade.

The callback can seed `fallout_river_federation_seed` when trust is at least 65 and tension is at most 25.

It can seed `fallout_barge_war_seed` when tension is at least 50.

Otherwise it sets `fallout_river_uneasy_league`.

## Durable memory

The country stores `fallout_river_ration_league_completed`, the selected branch, the final grade, compact trust, and border tension.

Both states store upstream and downstream memory flags plus the final branch and grade.

The chain cannot repeat after durable completion.

Transient receipts, delayed tickets, frozen values, and reservations are cleared only after the cleanup ticket is released.

## Event Log

History id `9158` records the opening choice, result grade, callback grade, and cancellation.

The primary actor is the country.

The secondary actor is the frozen upstream state.

The downstream state remains in the chain memory and detail text.

Payload codes are 11 through 14 for the four opening choices, 21 through 23 for joint results, 31 through 33 for upstream results, 41 through 43 for customs results, 51 through 53 for flood results, 61 through 63 for joint callbacks, 71 through 73 for upstream callbacks, 81 through 83 for customs callbacks, 91 through 93 for flood callbacks, and 99 for cancellation.

## Runtime boundary

No global daily, weekly, or monthly iterator is added by this chain.

The candidate row remains dormant until a Fallout-owned scheduler activation setter is proven.

The exact native all-valid-province Fallout strike sweep and the runtime scheduler setter remain separate release gates for the wider package.
