# Event033 storm clocks, bounded before replay and owner proposal

Disposition: source defects verified; repair proposed for parent review, not implemented.
Role: chaosx_scripted_system_architect, TEST/REPORT ONLY.
Runner edits are stopped.

## Sealed evidence and changed-file scope

Only four task files were created: `.tools/validation/test_033_storm_clocks.js`, this handoff, `validation/storm_clock_2026_10_09/before_3eb.json`, and `validation/storm_clock_2026_10_09/source_replay_3eb.json` beneath this Event033 plans directory.
No gameplay/shared source, prior test/receipt, GUI, asset, workbook or git/index writes were made.
The before archive preserves exact raw bytes for all nine replay dependencies; the compact receipt also preserves gzip-base64 exact bytes of the sealed failing runner.

- Runtime SHA256: `3eb102bf6168362eadd58188d45791cd81f9713dc379d9e08da325334e65bd48`.
- Triggers SHA256: `ae069680a185d0a0aa24d301fe62d158edab09a1a8d7d4ca0a36752dfa974f86`.
- Constants SHA256: `900491e8c605450abc7c3057033276fdd00e52d0b709bff29be3bb42dbb15db7`.
- Sealed runner SHA256: `241c252df0060dcd616ba8b0319566066e79a9474e8242d1e1bb7d431a027b5f`.
- Before archive SHA256: `0ae40063d79ebed3531942335c857b63395d0727b6108d299ba35d186cb630bb`.

Frozen-before and explicit current-3EB/AE069 runs both execute 9 principal scenarios, 44 variants and 579 distinct source locations: 19 pass, 25 source-contract failures, zero fixture failures, intentional exit1.
Their source inventory, observations and summary match.
This is historical failing evidence, not repair acceptance.
Run the frozen reproduction with `node .tools/validation/test_033_storm_clocks.js --json`; parent owns a later explicit `--current --runtime=SHA --triggers=SHA` replay and a separately dated receipt.

## Verified defects and retained behavior

In `common/scripted_effects/033_acid_rain_effects.txt`, creation writes `acid_rain_last_severe_pulse_day` at4400 and `acid_rain_last_superstorm_pulse_day` at5308 at forecast time.
Opening branches4700–4707 and5450–5459 do not reset these clocks.
With forecastF, openingF+9days, the second dispatch on opening day reaches sustained physics with a new key; without that duplicate, the +1day call reaches sustained physics instead.
The duration10/21 variants retain the same defect; +3day repeat is subsequently deduplicated by the updated clock.

Activation4673–4680 and5414–5421 tests start but not end.
Active branches4682 and5432 have no physical end bound; retirement4730 and5483 occurs after pulse/damage dispatch.
At end, end+1day and wholly expired end+20days, pending forecasts promote0→1, dispatch an opening and then retire2.
Storm opening writes history5450 even at expiry; severe retirement draws its18..45day cooldown4751.
Active-at/after-end fixtures similarly reach sustained dispatch before retirement.

State matching4690–4691/5440–5441 checks slot+target only.
Stale frozen/forecast generation consumes opening markers and reaches callbacks, but their actual first physical entry guards reject it: no loss claim follows.
Reused storm slot1 with state serial10 versus current slot serial11, or a declared missing serial, reaches a first-guard-admitted callback because the current layer predicate does not compare serials.
Declared absent slot reads zero and fails slot matching; this is an explicit native-absence fixture, not an unknown-symbol fallback.

After genuine active cleanup, actual source retains ordinary membership/band1 beneath severe and global membership/band4 beneath storm.
Repeated cleanup preserves counters, does not repeat cooldown or closure receipts, and closes the eligible evacuation flags.
The mixed pending-slot1/active-slot2 fixture retains activecount1 and one reservation after slot1 retirement; a repaired pending branch must retain that balance without an activation increment or active decrement.

## Minimal owner control-flow change

1. Before state marker/clock/history writes or physical dispatch, require bounded owned slot, current frozen registry and forecast generation, matching state source ID, positive consistent start/end mirrors, and storm serial equal to `global.acid_rain_superstorm_episode_entries^slot`.
   Preserve current consequence-generation proof and validate ownership again before clearing membership.
   Invalid/foreign mirrors must not cause unrelated state cleanup or invented recovery history.
2. Capture existing status0 pending versus1 active; route `now >= end` to retirement before any activation or physics.
   Only `start <= now < end` may activate or dispatch, including already-active rows.
3. Valid opening sets its existing `acid_rain_last_*_pulse_day = global.date` before the opening dispatch.
   Retain opening receipt/key behavior and the existing sustained `last+3days` test/write; no catch-up pulse or clock fallback.
4. Expired pending0 cancels only its proven forecast membership/reservation and retires2 without activation, history, active-episode closure or a severe cooldown draw.
   Do not decrement active storm count; decrement its reserved forecast count once and remove its slot ID once.
   Severe allocated lifetime count remains unchanged; do not manufacture a new cooldown or erase unrelated cooldowns.
5. Genuine active1 retirement retains advance-interval → same-episode achievement closure → clear owned target/forecast membership → reconcile → evacuation closure → controller forecast refresh ordering.
   Preserve prior measured severe-impact history, existing active cleanup draw bounds/slot order exactly once, and each counter decrement exactly once before status2 makes repeats inert.
   Existing private loop breaks must remain immediately zero-reset and explicitly bound; no new unscoped break or array ceiling.

`acid_rain_033_achievement_close_runtime_episode` in achievement effects2033–2058 uses stored episode/credit country/generation and end checks, not strongest-current-layer selection.
Its closure mapper1544–1677 accepts pulse count>=0; the never-active pending fixture consequently records closure key1/267 even though this replay executes no committed physical pulse.
Do not call that bridge from the pending-cancellation branch.
For active closure, retain current same-episode identity and genuine stored activation/pulse evidence; opening marker alone is not proof of loss, and do not fabricate credit/pulse counts for ambiguous legacy or foreign records.

`acid_rain_advance_consequence_interval` in aftermath effects70–96 integrates stored active interval/water context; reconcile598–613 and band publication preserve the underlying parent.
Do not introduce mortality-class exclusivity or globally clip an ordinary/global interval to the storm end.
A blanket public layer-trigger end gate is unnecessary for this local repair; any broader delayed exclusive-storm accounting or ambiguous historical had-active recovery remains unresolved, not silently defined here.

## Evidence limits and next step

The runner executes actual processor activation, clock writes, scalar/trigger/array/private-break control, retirement counter mapping, consequence/reconcile/band publication, evacuation cleanup, and achievement closure mapping with conservative separate temporary call frames and typed STATE/COUNTRY fixtures.
Physical helpers are dispatch/first-entry-guard witnesses only, with only their actual pre-physical receipt-key writes executed: no successful mortality, damage, benefit, population, finance, native physics or MP proof.
Creation planning is not replayed; its exact clock assignment node is executed atF.
Controller existence, historical active receipts, empty achievement target/evacuation arrays, water tier0 and cooldown-min native draw are declared fixtures; awards and native modifier application remain boundaries.
Assertions stop at their first failure; compact observations retain later cleanup evidence.

Live MCP supplied offline Data structures435–443,566,1217,1220 (revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`), installed triggers2110–2135 (revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`) and installed effects4296–4330 (revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`).
Numeric-loop cap1000 comes from vanilla `common/defines/00_defines.lua:25`; no foreach cap was invented.
Current unshadowed source lookup5402–5514 is complete at index revision `17b9b05b79f4a464df83cfd0c57e635617b7fb964a1232c9153f50b302f3e7b8`; one terminal stale-index retry did not change physical bytes.
Narrow country-scope activation validation is partial: syntax/command-kind/declared-scope checks only, `valid=null`, five native argument blocks unchecked; not native execution acceptance.
Reference paths, spans, revisions, fixture facts and all dependency/history hashes are retained in the compact receipt.

Skills used: chaos-redux-events, chaos-redux-subagents and events/references/loop-break-isolation.md; these kept source ownership, evidence layers and temporary frames/breaks separate.
No gameplay simplification or fallback was implemented; the stated model boundaries limit this audit.
Next safe step: parent applies the local processor repair, then runs the pinned current-source replay without overwriting this before evidence.
AA must compare changed clock/live-window/pending-cancellation and cooldown-call facts against its F8 before scenarios; weights, costs, durations, overlap policy, reports, GUI and achievement policy remain untouched by this proposal.
