# Event 028 dust and achievement repair

Disposition: implemented in source, with current MCP validation unresolved.
Acceptance basis: the user explicitly requested the full Event 028 specification, including the tuning matrix's partial national protection, one opening atmospheric injection, monthly reservoir, supported Event 013 calls, achievement hold periods, and cleanup.

## Corrected behavior

The three protection ideas identify basic, organized, and hardened systems.
Their former fixed bonuses cancelled entire lower-stage penalties and could produce positive net output as dust faded.
`asteroid_incoming_refresh_national_dust_protection` now computes compensation from the current Event 028 stage at 15 percent, 30 percent, or 45 percent and applies the six values through an iconless country dynamic modifier.
The same helper zeroes its values and removes the modifier at zero dust.
Stage penalty magnitudes are mirrored explicitly between the country idea literals and `asteroid_incoming_dust_protection` constants because idea modifier fields use file-local values.

Dust's weather modifier now increases the native weather penalty.
Protection reduces that added penalty by its protection fraction.
The previous negative dust values reduced weather penalties instead.

`asteroid_incoming_refresh_air_cleanliness_source` consumes its opening injection once and publishes the current monthly reservoir separately.
Stage reductions no longer subtract the opening injection from the atmospheric total.
`asteroid_incoming_apply_monthly_air_pressure` records actual shared-ledger additions under source 4 and rejects a repeated call on the same date.
Global mitigation reduces reservoir pressure by 15 percent per contribution, bounded at 45 percent.
The ordinary shared atmospheric recovery continues to remove contamination.
Both helpers reset their public temporary source inputs and Fallout-skip input before returning.

The existing Event 013 adapter supplied an exact family together with a family group, which the current Event 013 validator rejects at lines 253 through 261.
It also declared a physical origin without the required origin-state receipt, rejected at lines 264 through 285.
The repaired adapter resets public inputs, supplies only the exact family with the random group sentinel, and records an explicit meteor-impact origin state.
Main-ring secondary jobs use the locked main state as origin, and fragment-center secondary jobs use that fragment state.
The gateway remains responsible for terrain and evolution validation, and only accepted scheduled jobs count toward the four-call bound and add dust.

The monthly dust entry point now requires an actual impact and active dust, rescue, or local recovery work.
A persistent date receipt prevents repeated same-day decay and rescue loss transactions.
The miss cannot enter this maintenance transaction.

Parent review also corrected the five recovery missions to `is_good = no`.
The offline Decision modding section at lines 467 through 478 documents that `is_good = yes` labels an automatic mission's completion effects as failure.
These missions complete through successful rescue and reconstruction conditions, so their native presentation must describe completion as success.
This changes the presentation flag and leaves their weights, conditions, durations, and outcomes intact.

The collector and crater-conquest achievements use persistent start-day receipts and elapsed game days instead of adding thirty days on each monthly check.
The original counters could award the thirty-day conquest hold on the first monthly boundary after capture.
Losing crater control clears the former controller's hold receipt.
Acquiring another site does not reset the new controller's existing collector hold.
`asteroid_incoming_award_world_reconnected` checks the active hardened protection program before zero-dust cleanup removes the idea and persists the award afterward.
The prior ordering removed the required idea before evaluating the achievement.

## Current source checks

All twenty-four protection stage magnitudes match the corresponding current idea literals.
The twelve stage/protection combinations retain negative net factory effects, positive net supply burden, and nonnegative added weather penalties.
At Severe Impact Winter, hardened protection leaves factory output at minus 11 percent, construction at minus 8.25 percent, supply consumption at plus 8.25 percent, and air mission efficiency at minus 5.5 percent.
At Residual Haze, the same protection leaves factory output at minus 1.65 percent and supply consumption at plus 1.1 percent.

Using the current source decay constants without mitigation, opening loads 1, 24, 25, 49, 50, 74, 75, and 100 reach zero after 1, 8, 8, 14, 14, 19, 19, and 23 decay pulses, respectively.
The separate opening hold remains thirty days.
This is arithmetic evidence from the source tuning, not observed game execution.

The CXT daily hook was traced to the current shared `chaosx_test_country_sync_registered_content` implementation at lines 438 through 444.
That helper only marks registered content pending.
The Event 028 hook therefore already complies with the registration-only daily contract and needed no grant-path change.

## Reference evidence and route gaps

`hoi4.reference_context` for the event surface produced no result during sixteen bounded polls and was terminated locally.
`hoi4.reference_search` terminated with `timed out awaiting tools/call after 600s`.
The fallback reference sections were read directly from the local wiki and installed game documentation.

The current `hoi4.source_lookup` for `call_natural_disaster` succeeded with revision `3be18d8050a91187bfc58bd2482e9d104014b12811ed3878d5e5caf18893ec9c`.
It resolved one active definition at `mod:common/scripted_effects/chaosx_dynamic_effects.txt:533` through line 536.
Its indexed reference coverage was incomplete, with zero returned references and 17,480 unresolved references.

The retried `hoi4.reference_context` for the idea surface succeeded and reported no omitted or missing wiki/game documentation sources.
It retained the wiki dynamic-modifier section at lines 149 through 181 with revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f` and installed effects documentation with revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Its `script_doc` coverage was unavailable with zero indexed files, so the installed `common/dynamic_modifiers/0_dynamic_modifiers.txt` example was read directly.
The context bundle identifies citations only.
The detailed live section read and follow-up token search returned no result before the client code host changed, and the continuation later reported `cell 62 belongs to a stale code-mode host generation`.
Their live retrieval coverage remains unresolved, while the cited local sections were read directly.

The current narrow `hoi4.event_inspect` request for `chaosx.nr28.4`, with depth 4, 60 nodes, 120 edges, and helper expansion requested, terminated with `timed out awaiting tools/call after 600s`.
It returned no new event-validation artifact for this source revision.

| Source | Relevant lines | SHA256 of read source |
| --- | --- | --- |
| `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md` | 108 to 180, dynamic values, iconless presentation, application and removal | `FE41A26F2B8D3B8E78A9B0DEA9CE1A55F001D1E27886807A0A3FB2D2F535F14F` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 344 to 346, dynamic modifier updates, and 897, country flag scope | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| Installed `common/dynamic_modifiers/0_dynamic_modifiers.txt` | 1 to 28, variable modifiers and hidden presentation without an icon | `34832A23502C23CC02988A0DA899123A4D9891102913901B733C39C789B8469E` |
| Installed `documentation/effects_documentation.md` | 1153 to 1178, 5978 to 5993, 6730 to 6737 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| `common/scripted_effects/013_natural_disasters_effects.txt` | 214 to 304, 754 to 802, 4073 to 4270 | `3E5D2134F2059402F976307541B5730D4A30D3A123EE770664209E9A530AD216` |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | 531 to 536, public disaster gateway | `91B4609D44FC19D619FC8B6D22EF4A32B78D20AC14F9F2EF58A1B9DA152D7C04` |

The required live event, probability, map, decision, presentation, and save/reload acceptance gates remain open.
This repair neither enables Event 028 by default nor establishes completion of the whole package.
