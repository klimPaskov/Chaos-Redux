# Fallout NZL Lifeboat State engine proof

## Status

This record covers the dormant New Zealand Lifeboat State pilot. It does not authorize package activation. The live Fallout allocator still lacks accepted conflict dispositions for Samoa and the Aotearoa overlap. Vanilla New Zealand AI plan retirement is also unresolved.

HOI4 was not run. Runtime persistence and multiplayer observation remain unobserved. A read-only offline GUI inspection was attempted for `events_log_popup_window`, but the installed inspection service closed its transport before returning a result. No GUI artifact is claimed for that surface.

## Dormant activation boundary

`fallout_nzl_activate_lifeboat_package` is defined once in `common/scripted_effects/fallout_nzl_lifeboat_effects.txt`. A repository search outside documentation returns that definition and no caller.

The entry effect requires all of these current-generation receipts:

- a committed Fallout successor assignment for carrier tag `NZL`
- country memory 91
- Oceania and remote-islands region 9
- maritime-remnant archetype 5
- exact ownership and control of states 284, 1079, 723, 1080, and 1081
- exclusion of Samoa state 726
- current Samoa and Aotearoa conflict dispositions

Activation resets only Fallout NZL-owned runtime state. It does not write assignment receipts or conflict dispositions.

## State and carrier proof

The installed vanilla state definitions identify the package states:

- `history/states/284-New Zealand.txt`
- `history/states/1079-Auckland.txt`
- `history/states/723-Southern Island.txt`
- `history/states/1080 - Marlborough.txt`
- `history/states/1081 - Otago.txt`

The installed vanilla country history file `history/countries/NZL - New Zealand.txt` uses capital state 284. Auckland state 1079 remains the reviewed secondary capital candidate when the live assignment ledger explicitly selects it.

The package uses the actual carrier tag `NZL`. Cosmetic tags change presentation only. Event cleanup therefore continues to test `tag = NZL`.

## Unit materialization proof

The installed official `effects_documentation.md` documents `create_unit` in country and state effect contexts. The repository effect `independence_wave_create_opening_divisions` in `common/scripted_effects/006_independence_wave_force_effects.txt` proves the accepted local pattern for injecting centrally tuned experience, equipment, manpower, and count values into the engine-native division string through `meta_effect`.

The NZL package follows that pattern. It creates three bounded opening formations only after the exact package gate passes. The optional escort mission creates at most one additional formation and records both a flag and a count receipt. State scopes select Wellington, Auckland, and the South Island, while explicit province priorities target Wellington `1814`, Auckland `4543`, and Canterbury `2197`. The optional escort also prioritizes Auckland `4543`.

## Political initialization proof

The repository Independence Wave package effects use typed script constants inside `set_popularities`. The NZL activation effect uses the same structure. Initial party shares are centralized in `fallout_nzl_politics` and total exactly 100.

The official character documentation marks `expire` as optional. The three fictional route leaders omit it so a late Fallout transition cannot make them unusable solely because the campaign date passed a fixed expiry.

## Bilateral target determinism

The installed official `effects_documentation.md` states that `every_country` executes its children for every country that satisfies its limit. Repository precedents store country identity through `THIS.id` and compare stored variables against `ROOT.id` or `FROM.id`.

The NZL partner selector evaluates every valid coastal successor and retains the candidate with the lowest country id. The result is independent of iterator order because every lower id replaces the prior candidate and no higher id can replace it. The selected id is stored as a scope-valued variable and as a global event target. The humanitarian rescue-passage focus runs the same selector after excluding countries with a current relief-partner receipt. This produces an exact second target without reusing the first accepted partner.

The official effect documentation defines `save_global_event_target_as` and `clear_global_event_target`. The official trigger documentation defines `has_event_target`. The bilateral chain checks the current transaction generation and revalidates the stored country before use. Cleanup clears both global targets and every NZL-owned transaction variable and flag.

When no valid coastal successor exists, the selector records a generation-bound no-partner receipt. Human and AI routes pay the same local search cost, wait the same delay, receive the same failure result, and run the same cleanup. No silent no-event branch remains.

## Chain and AI parity

Opening, domestic, external, and Year 10 chains use paired visible human and hidden AI entry events with one shared hidden delayed resolver per chain. Each resolver revalidates the package, transition generation, and active chain before applying the common score and result effects. A valid human result is shown only after the resolver writes its generation-bound result receipt. AI continues directly to cleanup. An invalid delayed callback closes its chain without showing stale text or leaving an active flag.

### Read-only event-chain renders

The read-only event-chain renders used reachability with downstream expansion,
`expandHelpers = false`, `maxDepth = 6`, and `maxNodes = 50`. The opening root
used `refresh = true`. The other roots reused the refreshed workspace. Every
render returned status `ok` with code `EVENT_RENDERED_PARTIAL`, skipped zero
sources, and reported no blockers. The partial status is the workspace-wide
diagnostic and catalog truncation result, not an event-tool blocker.

The shared graph hash is
`f79aeb0430b23ecbc87b1051d3d47bde0495309ac2e10022e3473260d3d96894`.

| Chain | Root | Selected nodes | Layout SHA-256 | JSON SHA-256 | SVG SHA-256 | PNG SHA-256 |
| --- | --- | ---: | --- | --- | --- | --- |
| Opening | `chaosx.fallout.127` | 10 | `6a1a13071de85c5256d25fd993067087596f5ffb095811b03d85abc532fb89cd` | `7c7deeca55620222f28247ad2d8db8fc7727802475e7a46f6f798bf0f3c1ea72` | `fb48dff4bb3e8111d1827d18e846636fe0d993de395f05aeecbc24877b01bf4e` | `c8136d236b3d692ca8369468eda8aae1935e1f599a86ebc95518ac6fa333e00a` |
| Domestic | `chaosx.fallout.133` | 10 | `b7d58331286df8fc4af6eea14176dc4673add20a9b09a9caf417af3cf82c3ae6` | `dcd42b71c68f9958afee3dedb4d154377381e51dd96cd716edc1113eb7609c9a` | `793e8fcaee4a996c1da8c6b8f857fc64e58a06411654ca46c2acc5d00490b76b` | `bdd1c10267ac689179e5a11fcf3857a5622f4346b8ecc9ed29d947c0dff00dd8` |
| External | `chaosx.fallout.139` | 17 | `581ede7d9c3d70bb1f4db9bf595efa6ec2966b8a7aef952ad506c4e83be3d362` | `c050928599c0023dccc3695aa04433191f2cdc1360382525a5fe5db90b50e04b` | `718f341bb5dd78237f814483bc5f81466938d0b3cbb6de228362101ce47fd491` | `99e03b7aef5bfabf2d1f68d1406b8a82860e35af4f0038fcd2fabc3ed32eb59e` |
| Year 10 | `chaosx.fallout.147` | 10 | `0be98c9b493adb304877ce43944d5ff5cec32e0954b60541b5d1619fe6c624e7` | `2e35a537c3ef4c4120eb6cd16d55a77dce9f7eea3305fe0e53ea515e334d5354` | `80505a3b543b481ebf08ad3bd331a980d63029c971739505c8cd0bbf7284e517` | `d3db27a2ff4ca56757657959840053819cc4c073dac4bbea35d6338a1cddc8a9` |

All four scoring helpers treat the failure and success thresholds as inclusive. Scores between those constants receive the partial result. Equipment and resource choices use the installed Air Winter precedent `NOT = { has_equipment = { type < cost } }`, which represents an exact at-least check and keeps the visible cost equal to the amount deducted.

Opening, domestic, and Year 10 active flags have matching generation variables. Durable opening and domestic results also have matching generation variables. The package reset clears stale receipts before any later valid activation.

Relief-partner gates do not trust the presentation counter. `fallout_nzl_has_two_current_relief_partners` counts live countries that are independent, have a committed current-generation Fallout assignment, and hold a reciprocal current-generation NZL partner receipt. Pacific Rescue Mandate and the open-harbors achievement both use this live quorum.

The Year 10 gate uses an engine-native timed country flag. Activation writes `fallout_nzl_before_year_ten` with the file-scoped literal `@FALLOUT_NZL_YEAR_TEN_DAYS = 3650`. The script constant `constant:fallout_nzl_duration.year_ten` mirrors that value for shared tuning and documentation surfaces. This literal is required because the timed `set_country_flag` duration field does not accept a script-constant token or variable token reliably. The readiness trigger requires the flag to be absent. Package reset clears the flag before a later valid activation writes a fresh duration. The engine persists timed flags through saves, so this surface needs no daily, weekly, monthly, or world-country polling hook.

Human choices that deduct political power, command power, equipment, manpower, army experience, or navy experience have an exact at-least trigger before the shared payment helper runs. Hidden AI tests the same resource gates and selects a physical-value alternative when the political or command resource is unavailable. The native experience effects are `army_experience` and `navy_experience`, as documented in the installed `effects_documentation.md`. The invalid `add_army_experience` and `add_navy_experience` spellings are not used.

## Opening and domestic outcome reachability

The first two chain bands were recalculated from the exact initialization, choice costs, current state control, and prior-result terms. All five package states contribute `(4 + 4 + 3 + 2 + 2) / 5 = 3` context points.

At activation and outside war, the opening anchors are:

- Open ledger raises Parliament Trust from 31 to 35. `(22 + 35 + 18) / 3 + 3 + 2 + 7 = 37`, so it reaches the inclusive success boundary of 32.
- Guarded berths raises Sea-Lane Security from 18 to 22. `(22 + 31 + 22) / 3 + 3 + 1 = 29`, so it remains in the partial band.
- Local compacts does not change an opening-score value. `(22 + 31 + 18) / 3 + 3 - 3 = 23.667`, so it reaches the inclusive failure band at 24.

The guarded opening gains three further points during war and therefore succeeds at 32. This is an authored conditional result, not a random roll.

The domestic score uses Food Security and Parliament Trust after the opening result, the Lifeboat Parliament focus, the Dairy Stores focus, the current choice cost, and the prior-result term. With full state control and no war, the three opening anchors continue to distinct domestic bands:

- opening success produces domestic scores from 51 through 52.5, above the inclusive success boundary of 47
- opening partial produces domestic scores from 43.5 through 45, inside the partial band
- opening failure produces domestic scores from 34 through 35.5, at or below the inclusive failure boundary of 36

War pressure can lift the guarded domestic choice from a prior partial result to 47 and from a prior failure to 37.5. This preserves escalation-sensitive recovery without making the baseline bands unreachable.

## Decision transaction proof

The package defines eighteen decisions or missions. State-targeted Home Guard mobilization writes a current-generation receipt on the exact selected state and permits only one active mobilization. The dairy relief convoy and Quiet-Seas patrol are one-shot conversions, so neither can be repeated as a value reward loop.

The partner relief-port action is a country-targeted 105-day transaction. Its target must be a current relief partner whose capital state is coastal, owned, and controlled by that same partner. At payment, the exact capital state is stored as global event target `fallout_nzl_partner_relief_port_state`, and the shared external-mission lock prevents a second transaction from replacing it. Daily cancellation checks revalidate that exact state. Successful completion adds one naval-base level in the stored state, writes a state generation receipt, writes the reciprocal country receipt, and clears the target. Cancellation and package reset clear the target without selecting a substitute.

The relief guarantee records one exact country id and generation on NZL. Root, availability, and custom-cost gates all reject another guarantee while that ledger is occupied. Package reset revokes the relation when the country still exists. The narrow annexation hook clears the ledger if the guaranteed country is annexed, allowing a later valid partner without overwriting an uncleaned receipt.

The Weather Station Chain writes a 90-day timed warning. Starting either major harbor repair consumes that warning into a project-specific receipt. The receipt reduces the cancellation loss from seven points to four and adds four Sea-Lane Security on successful completion. Cancellation, success, and package reset clear the project receipt.

## Numbered sea-road proof

`fallout_nzl_license_every_sea_road` writes a permanent current-generation licence receipt, opens Fishery Quota Compact, grants seven Sea-Lane Security, and keeps Last-Berth Closure available. A licensed fishery compact requires five convoys in addition to its existing political-power and manpower payment, raises Food Security by seven and Sea-Lane Security by four, and issues or refreshes the 90-day patrol window. A licensed Quiet-Seas patrol requires ten convoys and twelve navy experience, raises Sea-Lane Security by twelve, and issues or refreshes the same window.

A current window adds four points to the external and Year 10 score calculations, while a lapsed licensed window subtracts four. It does not create a fifth live package value, repeatable store, or automatic reward loop. The package uses one lifecycle dynamic modifier, actions may refresh the timed window, package reset clears every owned licence and patrol record, and AI preserves a five-convoy reserve before operating the licensed cycle. The reviewed decision and mission count remains eighteen and the focus count remains forty-two.

The focused decision and mission audit found no actionable defect. Its proof is `subagent_handoffs/2026-07-22_fallout_nzl_numbered_sea_road_decision_mission_audit.md`.

## Fallout country-memory Event Log proof

The four NZL authored roots remain `.127`, `.133`, `.139`, and `.147`. Shared history uses dedicated system ids `9101`, `9102`, `9103`, and `9104`, so ordinary event ids are neither reused nor registered as Events-catalog rows. `event_system_event_type.fallout_country_memory = 4` owns a distinct History filter. The generic `record_events_log_system_history_entry` helper prepends all shared parallel-array fields without changing `global.last_fired_event_id`. Its compact payload stores the result band. The NZL wrapper then commits its detailed sequence-keyed private row before `refresh_events_log_system_history_views` rebuilds any open human History, Events, Event Details, or NZL package-card presentation.

Every NZL private row stores the exact shared sequence, date, dedicated id, detailed payload, country-memory id 91, choice, result, domestic prior-opening result, route, NZL actor, optional partner actor, four package values, and transition generation. Opening, domestic, and Year 10 commits are limited to one current result per generation. Their durable generation receipts survive package runtime reset, so same-generation reactivation cannot duplicate those rows. External commits are limited to one per current transaction. The completed rescue-passage mission records its successful second partner before transaction cleanup.

Event Details reloads by exact history sequence. It does not read later live NZL values into an old row. History rows show the NZL flag, the exact result band, and a second clickable flag and partner name for partnered external rows. The Fallout package card augments the base Fallout description, uses one selected transition generation, and appears only after a committed memory exists. A current package reads live values, route, and the current proven aggressor from NZL for every human viewer only after a memory is committed in its current generation. A historical package, or a newly reactivated package with no current-generation memory, selects the newest stored generation and its latest value row. The four chain summaries and at most two distinct external contacts are loaded only from that generation.

The installed official `effects_documentation.md` documents `add_to_array`, `clear_array`, `for_loop_effect`, and `while_loop_effect`. Its `add_to_array` contract states that `index = 0` inserts and shifts older values, which matches shared History ordering. The installed `dynamic_variables_documentation.md` documents the comparable and localisable `date` variable used for exact row dates and `GetDateStringNoHour` display. Repository actor-array precedents prove the established numeric country-scope storage pattern.

Static review confirmed equal append counts across the NZL parallel arrays, balanced script blocks, unique history ids, durable same-generation deduplication, cross-viewer NZL scope, and the separate ordinary-event boundary. No Event 2 mapping, SCN-014 row, manual dispatch, recurring on action, activation caller, or Zombie-owned path was added. Player-facing memory text names Wellington, Auckland, Canterbury, Marlborough, and Otago and contains no implementation-history wording. The final focused audit found no unresolved sea-road or Event Log regression and is recorded in `subagent_handoffs/2026-07-22_fallout_nzl_sea_road_event_log_completion_audit.md`. Numeric scope persistence, save recovery, and multiplayer observation remain unproved without a runtime pass. The attempted offline GUI inspection returned no artifact because the service transport closed.

## Focus structure proof

The read-only HOI4 focus inspector recognized all 42 authored focus blocks after the dedicated focus sprites were registered. The 2026-07-19 inspection produced layout hash `9f0b08848257a2a99f989ffffa4aa7a3d1e560e05cac8d4a3c9aac6a91f83911`. It reported zero connector crossings, zero node intersections, and zero same-row spacing violations. All 24 Fallout NZL focus DDS files and their sprite definitions were resolved.

The 6,992 by 1,744 pixel raster was inspected directly. It shows one readable opening trunk, three separated survival, humanitarian, and isolation areas, one explicit humanitarian and isolation mutual exclusion, and a late convergence on Year 10. Three long connectors fan from `fallout_nzl_bind_the_two_islands` to the first nodes of the separated branches. They do not cross nodes or other connectors and remain accepted as the visual expression of the branch split.

The inspector still reports `NZL_fallout_relief_speaker` and `NZL_fallout_harbor_constable` as missing static leaders. Both are deliberately created by the activation effect through idempotent `generate_character` blocks before the focus tree is loaded. This is an offline inspector limitation for runtime-generated characters. The remaining sprite diagnostics belong to vanilla continuous focuses imported by the tool and are not Fallout NZL references.

## Building trigger proof

Vanilla events use direct state building comparisons such as `naval_base > 0`. The NZL two-islands achievement uses the same state trigger form for states 284 and 1079, with the zero value supplied by the typed schema constant.

## Pirate target and war receipt proof

The offline on-actions reference and installed vanilla on-action files agree on the engine scopes used by the package:

- `on_war_relation_added` exposes the attacker as `ROOT` and defender as `FROM`
- `on_capitulation` exposes the capitulated country as `ROOT` and winner as `FROM`
- `on_peaceconference_ended` exposes the winner as `ROOT` and loser as `FROM`
- `on_annex` exposes the annexer as `ROOT` and annexed country as `FROM`
- `on_state_control_changed` exposes the new controller as `ROOT`, old controller as `FROM`, and changed state as `FROM.FROM`

`common/on_actions/fallout_nzl_lifeboat_on_actions.txt` uses only these narrow hooks. It does not add a daily, weekly, monthly, or world-country iteration. A pirate war receipt is written only when one side is the current NZL package and the other side matches the generation-bound aggressor variable. Capitulation, annexation, and a winning peace-conference result write the settlement receipt only after that exact war receipt exists. If New Zealand is the capitulated or defeated peace-conference side, the same hooks write a distinct generation-bound defeat receipt. That receipt unlocks the late isolation focus with a four-point security gain and a seven-point Parliament Trust loss. It never counts as settlement for the Closed Seas achievement.

The hostile target originates in the bilateral chain. A partner rejection is considered piracy evidence only when the responding country is already at war with the exact NZL owner event target. The owner stores that responder's country id and the current Fallout transition generation. No later focus, decision, or on action searches for a replacement.

The installed effects documentation and offline effects reference both accept a variable country target in `create_wargoal`. Vanilla defines `topple_government` in `common/wargoals/00_invasion.txt`. The punitive focus grants that goal against the stored aggressor for 180 days and does nothing if the pair is already at war or NZL already holds a goal against it.

The force-settlement decision uses the documented country-scope `surrender_progress` trigger. It becomes available only after the exact aggressor exceeds 65 percent surrender progress, then applies `white_peace` to that stored scope and writes the same settlement receipt. Its former timer-only settlement path has been removed.

## Capital-loss and basing proof

The capital-loss receipt is written from `on_state_control_changed` only when the old controller is the current NZL package and the changed state matches its assignment ledger capital. The state trigger requires literal engine state tokens, so the on-action uses reviewed literals 284 and 1079 while the paired assignment comparisons use `fallout_nzl_state.wellington` and `fallout_nzl_state.auckland`.

Foreign basing is a real bilateral choice. The human external result can grant the exact partner military access and docking rights. Hidden AI applies the same effect only on the isolation route when sea-lane security is below the stable band and the partner returned a partial or successful response. The effect records the permanent achievement disqualifier, raises sea-lane security, and reduces harbor capacity and parliament trust.

## Asset and ownership proof

The package has seventy-five NZL Fallout sprite definitions in `interface/fallout_world_end.gfx`. Every defined texture path resolves to a dedicated runtime file. These definitions cover four event reports, three fictional leaders, two completed advisors, twenty-four focus icons, fourteen idea icons, eighteen decision or mission icons, one decision category icon, and nine achievement states. The three cosmetic identities each have large, medium, and small dedicated flags.

The Radio Service Coordinator remains an explicit asset blocker. Its version 10 source passed neither the frozen paper-mean gate nor the frozen bottom-variation gate after ninety-six final candidates. No candidate PNG, review sheet, metadata record, DDS, or sprite definition was accepted. The dormant generated-character block therefore retains one unresolved portrait reference and cannot be reached because the package activation helper has no caller. No fallback portrait is used.

The event catalog workbook no longer assigns Fallout to Zombie Event 2. Its Event 2 detail contains only Zombie Apocalypse material. No Fallout event or scenario row was added. SCN-014 remains reserved in design documentation and absent from the live scenario catalog. The export was regenerated after the workbook correction. Dedicated NZL country-memory history and package details are implemented on the shared Event Log surfaces without creating an ordinary Fallout event row.

## Remaining activation blockers

1. The live conflict ledger does not yet produce the Samoa and Aotearoa disposition receipts.
2. The live allocator does not yet call the package activation effect.
3. Vanilla NZL alternate AI plans have empty abort blocks. No engine-safe additive override has yet been proved that retires those plans without replacing their pre-Fallout definitions.
4. The Radio Service Coordinator portrait has no accepted final asset or sprite definition.

The package must remain dormant until all four items are closed or explicitly redesigned. Event Log scope persistence and presentation are also still awaiting an authorized engine observation, but no runtime pass was requested for this tranche.
