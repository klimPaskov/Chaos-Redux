# Fallout Manual Province Sweep Proof

Status: dormant exact-sweep substrate implemented. Public release and runtime acceptance remain blocked.

## Outcome

The installed map can be expanded into 10,154 explicit native thermonuclear launch calls. Each call uses a verified province id with `launch_nuke`, `use_nuke = no`, and `nuke_type = thermonuclear_bomb`.

The province set is a version-pinned offline expansion of installed map data. HOI4 exposes no documented global all-valid-land-province enumerator, so this proves native calls and exact pinned-map coverage but does not prove an engine-native enumeration. The user's strict proof requirement therefore remains blocked.

The implementation does not use one strike per state. It does not use province modifiers as a substitute. It does not use variable-only fallout.

The public Triggerable Scenario row and launch dispatch are absent. The missing engine-native enumerator is a static blocker. Runtime acceptance, throughput, and presentation also remain unobserved because Hearts of Iron IV was not run and must not be run as part of this documentation reconciliation.

## Engine references

The official `effects_documentation.md` records that `launch_nuke` supports country scope, accepts `province`, accepts `use_nuke`, and accepts an explicit `nuke_type`.

Vanilla `common/raids/nuclear_raids.txt` passes `var:ROOT.target_province` to `launch_nuke`. Its thermonuclear raid paths also set `nuke_type = thermonuclear_bomb`.

The official documentation and offline Data structures reference both record `for_loop_effect`. Its loop value is a temporary variable. The generated sweep therefore passes `var:fallout_manual_target_province` directly and never scopes that temporary variable through `ROOT` or `PREV`.

The offline On actions reference records that `on_nuke_drop` supplies the launcher as ROOT and the struck state as FROM. The synthetic observer is evaluated before the Chaos Meter disabled setting.

Vanilla `common/on_actions/00_on_actions.txt` schedules twelve one-day nuclear news events from every `on_nuke_drop` callback. A Chaos Redux callback cannot suppress that separate vanilla branch. If all 10,154 scripted calls emit the callback, vanilla will schedule about 121,848 one-day news event attempts. Callback occurrence, callback synchrony, and the resulting news-event load are not proven.

## Installed map identity

- Installed Hearts of Iron IV build inspected: 1.19.2.0
- `map/definition.csv` SHA-256: `86846BE71198D6772C651638AA22E3656133198DE9B7C49C6234ED48CF33D87B`
- State-source manifest SHA-256: `9C2B20312B4D774999C55958094C0E8302BDE089BC178999BA7B56FF978C8A8F`
- All assigned state membership SHA-256: `290C400BED83A545556E418D7EF676831625F968D1C97877A6366D30290B39ED`
- Valid land membership SHA-256: `4546CC398C5D4756DF8D8DF097A77E48509CD53D417663A14ECED1EF3899E763`
- Sorted valid province id SHA-256: `A0F5504AEA22EC76D8C687228C9A4BF485B255C2F8CA9E7DB8A62CFB8D259949`
- Generated scripted-effect SHA-256: `D803BD0972FCE3F69DB50829687A2C35733FCC5018CC7F582BB6A493216089E3`
- Chaos Redux map or state overrides found: none

The state-source hash uses each state filename and its raw file hash in filename order. The membership hashes use state id followed by province id in numeric order. The valid id hash uses one decimal province id per line with LF line endings.

## Valid target derivation

A province enters the ledger only when all of these conditions hold:

1. Its id is greater than zero.
2. `map/definition.csv` classifies it as land.
3. Exactly one installed `history/states` province block assigns it.

Results:

- 1,081 state files parsed
- 10,272 unique state-assigned province ids
- 10,154 valid assigned land province ids
- 118 assigned non-land ids excluded
- Province zero excluded
- 1,081 states represented by at least one valid target
- 126 valid land targets in impassable states included because no official exclusion was found
- Minimum valid id 2
- Maximum valid id 13,413

The numeric interval from 2 through 13,413 is not used as a proxy for validity.

## Impassable states

The ledger includes 126 ordinary land province ids assigned to states marked `impassable = yes`.

No official effect documentation or offline wiki rule says that `launch_nuke` rejects land because its containing state is impassable. Those ids are not sea, lake, unassigned, or placeholder rows. Excluding them would reduce the sweep to 10,028 targets without an engine basis.

If later runtime observation shows native rejection, the sweep must remain blocked. The implementation must not silently drop those provinces.

## Generated batches

`common/scripted_effects/fallout_consolidated_effects.txt` contains 41 effects named `fallout_manual_execute_batch_0` through `fallout_manual_execute_batch_40`.

- Batches 0 through 39 contain 250 targets each.
- Batch 40 contains 154 targets.
- Batch-local contiguous runs produce 533 inclusive loops.
- Every loop declares `compare = less_than_or_equals`.
- Every batch declares its own index and expected expanded size.

A static re-expansion of all emitted loops produced:

- 10,154 expanded ids
- 10,154 unique ids
- zero order mismatches against the canonical valid-id ledger
- zero batch index mismatches
- zero declared-size mismatches

The `batch_index` field in `FALLOUT_MANUAL_PROVINCE_LEDGER.csv` was corrected to use floor division of the zero-based canonical target position by 250. It now matches batches 0 through 40, including the final 154-target batch.

Proof artifacts:

- `FALLOUT_MANUAL_VALID_PROVINCE_IDS.txt`
- `FALLOUT_MANUAL_PROVINCE_LEDGER.csv`
- `FALLOUT_MANUAL_PROVINCE_RANGES.csv`
- `FALLOUT_MANUAL_STATE_SOURCE_MANIFEST.csv`

## Runtime completion barrier

The generic batch and verifier callbacks `.901` and `.902` were replaced by identity-bearing event tokens. `chaosx.fallout.900` remains the bootstrap, `.910` through `.950` map one-to-one to batch indices 0 through 40, `.960` through `.966` map one-to-one to verifier attempts 0 through 6, and `.903` remains the exact countdown callback.

The dormant manual runtime ledger uses schema 4. Every scheduled batch, verifier, and countdown callback stores the active transaction generation. Baseline capture stores all 1,081 state rows, counts them once, and writes one generation-bound completion receipt. Callback triggers and the host validator use that O(1) receipt and reject a missing or mismatched generation without rescanning the state collection. Schema 1 through schema 3 active transactions fail closed because they do not contain this provenance.

Before any later batch can issue native effects, the validator binds the issued count to the cursor. Cursors 0 through 40 require `next_batch * 250` issued calls. Cursor 41 requires exactly 10,154 issued calls because the last batch contains 154 targets. A mismatch enters the terminal manual error state without issuing another batch.

Each hourly batch callback independently recomputes the cursor count and last-completed-batch invariant before it opens the native launch window. It also rejects negative observations, observations above issued calls, and impossible struck-state counts. The daily validator is recovery coverage rather than the only prelaunch barrier.

The seven-day countdown cannot begin from the issued counter alone. The verifier requires all of these values:

- next batch equals 41
- issued launch calls equal 10,154
- observed `on_nuke_drop` callbacks equal 10,154
- unique struck-state count equals 1,081
- state strike-count sum equals 10,154
- struck-state array size equals 1,081
- no sweep error

An invalid batch identity, invalid batch size, count mismatch, lost countdown coordinator, or overdue countdown stops the transaction. A coordinator may be rehomed only while the hourly sweep or verifier phase remains recoverable. A failed batch is never replayed because some native effects may already have executed.

Each verified struck state first mutates its live population with the exact
state-loss helper until the captured prestrike baseline reaches its approved
90 to 95 percent loss band. Its provenance receipt then measures the complete
prestrike-to-post-strike loss after native callback effects and the exact
reconciliation. The observed loss is accumulated once and sent to the shared
Deaths ledger after the state mutations, with state mutation disabled on that
accounting call so the population is not deleted twice. The Fallout exception
keeps this receipt mandatory even when the general Deaths setting is disabled.
Static control flow applies that aggregate Deaths receipt, fallout, Air
Contamination, Chaos history, condemnation, and treaty consequences once, only
after complete verification. It then invalidates the sweep and verifier
scheduling state before the countdown begins. The vanilla references do not
specify whether the native callback writes this mod's Deaths ledger, so runtime
review must confirm that it does not create a duplicate receipt.

The exact countdown stores its start day and an end day equal to start plus seven only after verification. Event `chaosx.fallout.903` is scheduled with a literal seven-day delay. It is the only path that may submit the standard Fallout request. The daily coordinator does not submit or reschedule the countdown because a calendar-day comparison cannot prove that 168 hours elapsed. Lost countdown ownership and an overdue callback fail closed. This is static proof, not runtime proof.

The `.903` trigger and the request wrapper both validate countdown ownership, generation, coordinator, status, and exact due day before submission. Successful standard-request submission clears both the request-due flag and countdown schedule provenance. Rejected submission enters the first-error-owned terminal state and clears every pending schedule token and generation value.

## Release blockers

### Scenario id allocation

The live triggerable-scenario registry includes Black Plague at raw id 12 and reaches raw id 13 with The Unbidden Muster. Fallout assigns raw id 14 as one greater than the highest assigned identity to the dormant manual sandbox row. Existing ids remain unchanged. This row is not an ordinary Event Log, Event Details, evolution, or ordinary super-event registration.

Fallout owns the reserved raw id 14 through `fallout_manual_scenario_identity.triggerable_scenario_id`. This is exactly one greater than the highest live assignment. Raw id 12 and every existing scenario id remain unchanged. The reservation does not register a public row or waive the runtime gate.

### Runtime behavior

Static source proof does not establish these runtime properties:

- every native call is accepted, including calls against land in impassable states
- scripted `use_nuke = no` calls invoke `on_nuke_drop` once and within the guarded batch window
- the engine preserves a distinct native strike result for every province
- 250 calls per event remain bounded for frame time, save integrity, and multiplayer synchronization
- the player-facing result remains readable across the 41 batches
- the vanilla twelve-event `on_nuke_drop` branch remains bounded when it may schedule about 121,848 one-day news event attempts

The manual sandbox row and Fallout-owned dispatch are present but launch-gated. The visible countdown direction and release claim remain dormant until those properties are resolved. Scenario identity is no longer a blocker. No weaker substitute has been installed or approved.
