# 1936 and 1939 CBRN starting protection inventory audit — 2026-09-25

**Disposition: source implemented; runtime quantities and country-specific 1939 industry remain unresolved.** The user's 2026-09-25 choice applies force-scaled military issue bands and a 25% military replacement reserve to both bookmarks, separately retains Britain's sourced 1939 civilian issue, and leaves other civilian starting coverage at zero without country evidence.

The startup dispatcher in `common/scripted_effects/chaosx_startup_history_effects.txt` applies the shared protection profile to 41 marked countries without a 1936-only gate. The marker suppresses their older fixed mask and civilian grants before the force profile reconciles stock. Reconciliation preserves any existing stocks and supplies only the shortfall toward the profile target; the read-only audit found no duplicate mask grant in these paths. Military requirement is derived from runtime deployed army manpower in thousands: `M = deployed_army_manpower_k × 10` crates. The source therefore cannot establish absolute quantities in either bookmark without the engine's deployed manpower value.

| Countries | Military issue target | Replacement reserve target | Civilian starting target | Dated setup found in this audit |
| --- | ---: | ---: | ---: | --- |
| ENG | 75% of M | 25% of M | 1936: zero; 1939: up to 40,000 crates within eligible core-state need | 1939 civilian distribution and dated personnel |
| FRA | 75% of M | 25% of M | Zero | No separate dated personnel or mask grant identified |
| GER | 75% of M | 25% of M | Zero | Dated personnel |
| USA | 75% of M | 25% of M | Zero | Dated personnel; 1939 phosgene knowledge and 320 mustard lots are separate from masks |
| SOV | 75% of M | 25% of M | Zero | Dated personnel |
| ITA | 100% of M | 25% of M | Zero | No separate dated personnel setup identified |
| JAP | 50% of M | 25% of M | Zero | Dated personnel |
| POL, CZE, BEL, HOL, CAN, AST, NZL, SAF, ROM, YUG, TUR, SPR, CHI, PRC, SHX, GXC, YUN, XSM, SIK, MAN, BUL, HUN, GRE, RAJ, AUS, POR, SWE, NOR, DEN, FIN, BRA, ARG, MEX, CHL | 25% of M each | 25% of M each | Zero each | POL has dated personnel; no other separate dated mask grant identified |

The 1939 Britain branch is gated after 1938-12-31 and its country marker, then dispatches `cbrn_protection.3`. `common/script_constants/startup_history_constants.txt` sets the 40,000-crate target. `common/scripted_effects/cbrn_protection_effects.txt` visits only owned, controlled core states with positive population, initializes each state protection ledger before reading need, caps issue to that need, and preserves the 25% military reserve floor. The military demand calculation uses country manpower and mask ledgers, not state civilian ledgers. This bounded audit found no uninitialized state-ledger read in these startup paths; other decision and event quote surfaces were outside its scope.

The initial read-only event-tool calls used invalid request shapes and produced no analysis. Parent correction with `selector = { kind = event, eventId = cbrn_protection.3 }` returned `EVENT_INSPECTED_PARTIAL` [trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1b4906e4a0cb0c89819bc54afcef245e8726ada279fc341d52785df2a98e71e/29121f28d5b6fa100239dbf3577326aee697ea9e95644bea9208dbf81636eda3/event-trace-f737d8d5eb3e.json) and `EVENT_RENDERED_PARTIAL` [overview](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef55457dde85879aa7154f6c9900f5a576f4e675454fcdbd521111e7c2fa103e/e23ba912ba1aff43751fc56d40083924050e9b85a6dface0135dc4cd1539eaa4/event-overview-f737d8d5eb3e.json), both at revision `f737d8d5eb3e07985d0b73c706f872a0ccada3c8856c1f2fc0b0984806ade4e9`. The focused route reported zero direct blockers but deferred workspace-wide helper and lifecycle projections, so it does not prove the issue/clear transaction or final state allocations.

Remaining checks are runtime absolute military demand and resulting stocks for both bookmarks, actual British core-state allocations, and sourced country-specific 1939 industrial and personnel setup where the accepted design calls for it. The audit did not launch HOI4 or change gameplay files.
