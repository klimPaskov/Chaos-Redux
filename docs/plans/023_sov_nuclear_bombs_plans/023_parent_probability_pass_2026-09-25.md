# Event 23 parent probability pass

Audit date: 2026-09-25.

This handoff records the parent-run probability and timing pass after the Event 23 MTTH constants were aligned with the accepted specification. It is evidence only and does not claim live-game balance sign-off.

## Source change

`common/script_constants/023_sov_nuclear_bombs_constants.txt` now uses 120, 120, 180, and 90 days for Evolution I through Evolution IV. These are the design centers in Part 5 and the named probability scenarios. The prior 180, 240, 300, and 360 day values were a source/specification discrepancy.

## MCP surface evidence

The installed tool surface exposes no separate HOI4 service health, service-version, or client-negotiation route. The ordinary Event and probability routes were used. No helper-expansion, native, job, or invented route was used.

The Event 23 `event_mean_time_to_happen` inspection of `common/mtth/023_sov_nuclear_bombs_mtth.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`, source revision `9b9371b3a77958068a8607d0e0f67ac4d241ce07f6eaa64abc39f5c7b741648f`, source hash `89b364cff8d70ba8114832f89e206c5a9f69ec8c28635880207ea785515f596c`, and artifact `probability-inspect-89b364cff8d7.json`. The custom MTTH entries are not evaluated by this adapter, so no effective timing result is claimed.

The Event 23 random-list inspection of `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` returned `PROBABILITY_SOURCE_INSPECTED` with source revision `9b9371b3a77958068a8607d0e0f67ac4d241ce07f6eaa64abc39f5c7b741648f`, source hash `1c90f792579b83671ee5bc814853bf2bbfee7c055968701f0df86ab501b98242`, a complete four-entry pool, and four unresolved dynamic inputs. The named proof-test evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-06bcf68fd4f8373941391501`, one named scenario, four candidates, and four unresolved items. No normalized test outcome probability is claimed.

The Event 23 mission inspection of `common/decisions/023_sov_nuclear_bombs_decisions.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with source revision `8d9080e4c8a9535ae7bf1564f426f9f9e3183312476d0e42ef41c6067df26055`, source hash `f86565ae8b81a493d5c84a814610137f5f3e12d56b06ab74bbdff904ebfa3cde`, and 81 available mission candidates. The named mission evaluation returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-715945fd074fa897f9404040`, three scenarios, 30 matched candidates, and 15 unresolved items. The readiness sweep returned `PROBABILITY_ANALYZED_PARTIAL`, analysis `probability-dda177e0ba0c1ef2deaf8889`, two scenarios, 20 matched candidates, and 15 unresolved items. The same scenario set and candidate subset were compared with `probability-2d2aaae0a5df7c6fb043c9ea`, which reported zero comparison changes and retained 15 unresolved items.

The mission scenarios were `P23_EVO1_HIDDEN_NORMAL`, `P23_EVO1_PUBLIC_ACCELERATED`, and `P23_EVO2_BREAKAWAY_ACCELERATED`. The comparison and sweep scenarios were the first and third of those named cases. The adapter accepts flat primitive state and scope records, but it does not bind the nested ROOT, THIS, PREV, FROM, event-target, country-variable, ownership, controller, war, technology, delivery, or target state required by Event 23. Results are therefore partial evidence and not balance approval.

## Remaining weighted-logic limits

The current adapter does not expose effective MTTH for the custom Event 23 entries. It also cannot prove the Evolution III and Evolution IV world gates, the severe first-use conjunction, or exact selected-target mission eligibility from the supplied flat fixtures. The source-level gates remain the authoritative implementation boundary until a richer engine fixture is available.

No AI weight was changed during this pass. The source change was limited to the accepted centralized MTTH design centers. A live campaign, save and reload, native callback, and user-owned consumer validation remain outside the coding environment.
