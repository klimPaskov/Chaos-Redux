# Four-state supplementary control sensitivity and Danish negative control

Disposition: implemented as source-model evidence; dated live controllers, competing outside movements and physical engine receipts remain unresolved.
Acceptance basis: the user's request for historically grounded wider German campaign scenarios with cause-separated actual losses and no casualty-total tuning target.

The [existing nine-state sensitivity](staged_state_control_sensitivity_2026-09-26.md) keeps its original JSON result unchanged after its calculation was moved to a shared test helper; its canonical row hash remains `a1cbb02bf4a14557b9d3bea75ad41182b7b08ed54e356b11ca068fc0157b3c6a` and its 589,297 modeled campaign losses remain the earlier bounded result.
The new `test_four_additional_staged_direct_control_states` reads installed European 1936 origin states and the unchanged source coefficients, then applies one measured campaign cause only during four explicit full-month direct-GER-control windows.
It does not claim that a country-wide occupation proves every in-game state controller or that local occupation violence equals all Holocaust deaths from that origin.

| Installed state and original owner | Full-month staged GER control | Apportioned source people | Modeled occupation-cause losses | Survivors |
| --- | --- | ---: | ---: | ---: |
| 110 Norway, NOR | 1941-07 through 1945-04 | 479 | 316 | 163 |
| 9 Czechoslovakia/Bohemia, CZE | 1941-07 through 1945-04 | 106,711 | 73,400 | 33,311 |
| 75 Moravia, CZE | 1941-07 through 1945-04 | 61,718 | 42,446 | 19,272 |
| 108 Eastern Serbia, YUG | 1941-07 through 1944-08 | 3,492 | 2,148 | 1,344 |
| **Four-state source sensitivity** | | **172,400** | **118,310** | **54,090** |

All four selected rows have distinct installed state IDs and 176 separate accepted monthly source-model receipts; their allocated people equal their modeled cause losses plus survivors.
The Norway window begins after [NARA's documented 9 April 1940 invasion](https://www.archives.gov/research/holocaust/finding-aid/civilian/rg-84-norway.html) and ends before the [Norwegian government's 8 May 1945 German capitulation](https://www.regjeringen.no/en/the-government/previous-governments/regjeringer-siden-1814/historiske-regjeringer/norways-governments-1940-1945/the-chief-officers-in-oslo-may-1945/id438698/); the window is a direct-military-control inference for this one installed state.
[NARA's Bohemia and Moravia finding aid](https://www.archives.gov/research/holocaust/finding-aid/civilian/rg-84-czech.html) dates German occupation to March 1939 and Prague's liberation to May 1945.
Installed vanilla `history/states/9-Czechoslovakia.txt` lines 36–39 and `75-Moravia.txt` lines 28–31 additionally assign both `owner = GER` and `controller = GER` on `1939.3.14`; their initial owner remains CZE, so the seed-origin and later controller are distinct in the installed history.
That history is stronger than a 1936 map tile but still does not prove a 1936 campaign's later focus route or a live save.
[USHMM's Yugoslavia account](https://encyclopedia.ushmm.org/content/en/article/axis-invasion-of-yugoslavia) describes Germany's military occupation administration in Serbia after the April 1941 invasion; [the scholarly study of the September 1944 Serbia campaign](https://doi.org/10.1080/13518046.2015.1061825) supports ending the Eastern Serbia full-month window in August rather than including the changing September front.
The eastern Serbian puppet administration and partisans mean a GER controller tag is an inference, not a verified game state.

The supplementary four states are disjoint from the original nine: together the thirteen selected states allocate 1,081,811 source people, model 707,607 occupation-cause losses and leave 374,204 survivors over 530 monthly receipts.
The disjoint subtotal is separately written to `historical_envelope_results.json` under `staged_thirteen_state_disjoint_source_subtotal`; state IDs 37 and 99 are explicitly absent from that list.
This combined number is only a source-model coverage subtotal, not a historical reconstruction or a step toward forcing [USHMM's approximately six-million Holocaust total](https://encyclopedia.ushmm.org/content/en/article/the-final-solution) into one cause.
It omits most European states, documented deportations and killing centers, country-specific outside losses, mixed-origin custody and later institutional deaths; it is not additive to the separate state-87 Łódź transfer envelope.

## Denmark is a rejected no-rescue scenario

The same direct-control arithmetic for installed state 37 Denmark and state 99 Jutland would allocate 4,192 modeled source people and record 2,859 generic campaign losses from July 1941 through April 1945, leaving 1,333 survivors over 92 monthly receipts.
The source-model result is archived separately as `rejected_denmark_no_rescue_counterfactual` in `historical_envelope_results.json` with `accepted_historical_sensitivity = false`; it is not included in the thirteen-state subtotal above.
[USHMM's Danish rescue chronology](https://encyclopedia.ushmm.org/content/en/timeline-event/holocaust/1942-1945/danish-jews-escape) records approximately 7,200 Jews escaping to Sweden from September into October 1943, while [USHMM's Denmark account](https://encyclopedia.ushmm.org/content/en/article/denmark) estimates about 120 Danish Jewish Holocaust deaths in total and describes the largely independent Danish government before August 1943.
The 1933 source ceiling of 5,700 people is not the same population and date as those historical figures, but a model that assigns 2,859 local campaign deaths to just two Danish states with no rescue path is historically implausible.
This is evidence of missing policy timing and origin-preserving living movement, not permission to tune a generic monthly death rate to the Danish total.
No accepted gameplay exception or Sweden transfer was added here; that requires a source and route contract that preserves one physical debit, destination credit and original responsibility.

Superseding disposition, 2026-10-04 (agent decision 6 in `docs/plans/system_camp_repression_rework_plans/agent_decisions_2026-10-04.md`): implemented. Danish-origin rows are deferred from the generic campaign until the October 1943 order, and the dated rescue moves 0.94 of each living Danish home row to Sweden through the exact movement receipt in escape mode. `danish_rescue_source_tests.py` runs the production monthly pass: the pre-change rule reproduces these 2,859 deaths, while deferral plus rescue leaves 81 deaths and 3,940 escaped from the same 4,192 allocated people. The generic campaign fraction is unchanged and Denmark is still not added to the thirteen-state subtotal.

## Provenance and limits

Installed vanilla state files `history/states/110-Norway.txt` lines 3–5 and 21 (SHA-256 `76f33f262e6d38e835ceeae09c6131b4864b204f242af59c29ab9ee20965acaf`), `9-Czechoslovakia.txt` lines 2–4, 13 and 36–39 (`0305620291a5478cedb34f4c710c50b1e7cf2810baedb6f91d5a59706568cc45`), `75-Moravia.txt` lines 2–4, 13 and 28–31 (`70cd11433ea48f8c27022bc80410febbad1786a5905ca06e89ef563fead1ec6d`), and `108-Eastern Serbia.txt` lines 3–4, 13 and 26 (`18389a1054b83c86c9c43003194c4ae649b6fda518f861d0e7a867d3052b7067`) supply installed IDs, names, initial populations and owners.
The excluded Danish negative-control files are `37-Denmark.txt` lines 3–5 and 9 (`65d407cf5a01e95acca722a1ba46aa01dcecdca834a6c40b156d695eb9d9d0b5`) and `99-Jutland.txt` lines 3–5 and 9 (`f5ee9227eb63f09988f957e46ab4b31d0161a6bc12f549b7482096be50512061`).
HOI4 MCP map lookup covered these states among 36 requested IDs and returned `MAP_LOOKUP_COMPLETED` at revision `068028c8b0c3875682fd153b23ed411493195a7faf8317c247f6c4a5e6cbd88e`, [lookup artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0951649dedcad2235c65bd5dcedcfb5077b5eb97b0aac305d1e5c2308503bdf1/7c9d896c2d82ff5e957570815d4934b3a5db577ae2ddb28f7cdb460aa32ffc20/map-lookup.068028c8b0c38756.7ec03df0e99aa03e.json).
Its [controller](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d57af25690c299ca9096f29752ad42d5e2fd04e1d533ce2ae97e5002b43ba9c/123789ec25fdf47667875401e8050338bf525748ff6ed52d8bcf81b079820910/map-controller-tile-b4b32c2cdb9a.json) and [owner](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e668d669965bb4f16938c78716af2fddc272fb61f6e66ba99aff618dc7c2dcea/5922af241513e3a746e6d46815d4f00315ac8bb66291b99b1ec1f7dfe2e05859/map-owner-tile-b4b32c2cdb9a.json) tiles rendered at the same revision and were visually reviewed by the map auditor.
The lookup's 1936 `controller = null` and starting-owner tiles do not prove the staged wartime controller windows; the source-model scenario does not establish current population, cash reserves, site support or physical death receipts in a live game.
The wider matrix must still reconcile documented transfers, rescue, outside loss, labor and custody causes against original responsibility without double debit.
