# European occupation-origin coverage matrix

Disposition: implemented as a starting-state inventory and expressly counterfactual upper sensitivity; dated state-controller and receipt coverage remains unresolved.
Acceptance basis: the user's request to benchmark the wider German campaign against the six-million Holocaust total without converting source ceilings into casualty targets.

`test_historical_envelopes.py` reads the installed vanilla `history/states` starting owner and manpower, then requires every listed province to have the European continent ID in the installed `map/definition.csv`.
It enumerates the initial state IDs and population for every source in `camp_occ_origin_k` in `historical_envelope_results.json` under `all_seeded_origin_initial_european_inventory`.
This is the state set available to `camp_occ_seed_origin` at a 1936 start, not a record of later German state control.
Eighteen mixed-continent states are separately listed in the JSON for map review and are not silently counted as European by this inventory.
The HOI4 MCP map inspector returned `MAP_INSPECTED` for states 87 and 88 plus one starting state from every seeded origin, with selected-state artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d93c0bd446fbeba708eee22feeeec3b71c7706264441e731ed3bdf9c00a0131/456ccff21e52978cd49dc797ea62e100070986a841eb140ce38836fd9cef0790/map-inspect.26ca4a5626f89ddd.json`.
Its broad validation also reported unrelated building-position and floating-harbor errors; neither the installed 1936 owner files nor this map route establishes a 1941–1945 controller sequence.

| Original owner | Finite 1933 source ceiling, people | Installed European starting states | Campaign interpretation |
| --- | ---: | ---: | --- |
| POL | 3,000,000 | 18 | Germany and the Soviet Union partitioned Poland; individual state control must be supplied by date. |
| SOV | 2,525,000 | 60 | German control covered only parts of the European USSR and changed with the front. |
| ROM | 756,000 | 12 | Axis ally; no country-wide direct GER-control assumption is accepted. |
| LAT | 95,600 | 5 | Soviet annexation and later German occupation require state-level control dates. |
| LIT | 155,000 | 5 | Soviet annexation and later German occupation require state-level control dates. |
| EST | 4,560 | 5 | Soviet annexation and later German occupation require state-level control dates. |
| GER | 525,000 | 24 | German home-origin states are excluded from occupation admission and belong to the separate domestic path. |
| HUN | 445,000 | 5 | German military occupation from March 1944 does not itself prove HOI4 `is_controlled_by = GER`. |
| CZE | 357,000 | 10 | Pre-campaign annexation/occupation; later original-state controller and outside losses need receipts. |
| AUS | 191,000 | 6 | Pre-campaign annexation; source remains foreign-origin but may enter only under the actual controller gate. |
| ENG | 300,000 | 21 | Britain was not occupied by Germany; a whole-origin German campaign path is counterfactual. |
| FRA | 250,000 | 25 | Northern occupation and southern Vichy/Italian phases prevent a whole-origin controller claim. |
| HOL | 156,000 | 2 | German occupation began in 1940; liberation/control needs state dates. |
| BEL | 60,000 | 4 | German occupation began in 1940; liberation/control needs state dates. |
| DEN | 5,700 | 6 | German invasion in 1940 does not establish every in-game state's direct controller at every month. |
| NOR | 1,400 | 11 | German invasion in 1940; occupation and puppet control need state dates. |
| GRE | 73,000 | 7 | Germany, Italy and Bulgaria divided control; a whole-origin GER assumption is invalid. |
| YUG | 68,000 | 15 | Germany and its partners partitioned Yugoslavia; state-specific control is required. |
| ITA | 48,000 | 18 | Germany occupied northern and central Italy after September 1943; the south and Italian Social Republic require separate controller checks. |
| BUL | 48,500 | 4 | Axis ally; no country-wide direct GER-control assumption is accepted. |
| ALB | 200 | 3 | Italian and later German control requires dated state evidence. |

The source ceilings total 9,064,960 people; 525,000 are in the German home-origin row excluded from occupation admission, leaving 8,539,960 foreign-origin people as an absolute pre-control ceiling.
Each later admission is smaller if Germany lacks direct control, the radical campaign is inactive, a pre-enrollment decline or other custody has reduced headroom, or the state is not on the European continent.
The seed-time `camp_occ_home_german_origin` flag keeps German home states out of the occupation ledger even if cores or ownership change later; this avoids assigning the same home exposure to both the domestic and occupation paths.

The separate `all_foreign_origins_counterfactual_full_control` calculation gives Germany every foreign origin from July 1941 through April 1945, including Britain and Axis allies, with no outside or custody debit.
It produces 5,874,870 modeled occupation-campaign deaths from 8,539,960 foreign-origin source people.
That result is **not** historical reconstruction, a balance target, an engine receipt, or evidence that the [USHMM six-million Holocaust total](https://encyclopedia.ushmm.org/content/en/article/the-final-solution) has been reproduced; that total also includes murder outside occupation-campaign rows and outside killing centers.
It demonstrates how an implausible all-controlled premise can make a numerical total look close while violating the controller and cause contracts.

The [USHMM war chronology](https://encyclopedia.ushmm.org/content/en/article/the-holocaust-and-world-war-ii-key-dates) supports the broad invasion order for Poland, western Europe, the Balkans and the Soviet Union.
The [USHMM 1944 account](https://encyclopedia.ushmm.org/content/en/article/1944-key-dates) describes multiple eastern and western liberation fronts, while the [Hungary](https://encyclopedia.ushmm.org/content/en/article/the-holocaust-in-hungary) and [Italy](https://encyclopedia.ushmm.org/content/en/article/italy) entries distinguish German military occupation from the states that a game may assign to a Hungarian or Italian controller.
The next dated matrix must pair each initial state ID with observed or explicitly staged HOI4 controller changes, the campaign's current mandate and support, actual population before admission, competing custody and outside receipts, and one measured campaign receipt per month.
Until that evidence exists, neither the three-origin sensitivity nor the all-origin counterfactual can be promoted to a realistic Europe-wide loss total.

A later [nine-state dated direct-control sensitivity](staged_state_control_sensitivity_2026-09-26.md) now exercises individually apportioned state rows with explicit control-stop months and actual source-model receipts. It reports 589,297 campaign-cause losses from 909,411 allocated people across nine selected states. Those windows are historically bounded but are not proven HOI4 controllers, and the result is not additive to the separate state-87 transfer scenario. It narrows the gap between the initial-owner inventory and a dated row model without satisfying the missing full-Europe controller, movement, outside-loss and institutional-cause matrix.

The [supplementary four-state sensitivity](supplementary_direct_control_sensitivity_2026-09-27.md) adds Norway, Bohemia, Moravia and Eastern Serbia with separate sourced windows and 176 more source-model monthly receipts; the disjoint thirteen-state subtotal remains far short of full geographic and cause coverage. The same audit rejects a two-state Denmark no-rescue calculation as historically implausible rather than counting its modeled deaths toward a plausible total. Hungary, Italy, Slovakia and some Yugoslav partitions retain explicit direct-controller uncertainty, so the inventory's ceiling and counterfactual must not be promoted into a campaign result.
