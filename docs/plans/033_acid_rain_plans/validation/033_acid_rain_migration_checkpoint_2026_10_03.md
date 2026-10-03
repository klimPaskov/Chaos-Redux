# Event 033 migration checkpoint

Disposition: implemented for acute-state selection and native mission cleanup, with executed save evidence pending.
The user's Part 12 migration gate requires cloud-only prototype states to remain outside acute coverage.
The parent changed `acid_rain_migrate_legacy_runtime` to record `acid_rain_legacy_affected` only when `acid_rain_state` is present.
The separate `acid_clouds_state` cleanup removes its presentation modifier without creating coverage or population-loss receipts.
This change does not invent historical deaths.

The current synthetic acceptance run stopped at the source migration contract because legacy mission cleanup was absent.
Its previous required token `cancel_mission` has no entry in installed effect documentation or the offline wiki effects catalog.
The supported native effect is `remove_mission` in country scope.
The validator now requires that native effect and separately rejects cloud-presentation coverage.
`acid_rain_remove_legacy_missions` checks each active legacy mission in country scope and uses native removal.
The existing one-time legacy state pass invokes it for the owner and controller of a state carrying either prototype modifier.
The existing formation country census invokes it as well, covering a residual timer in a participant whose prototype modifier is absent.
Both legacy mission identifiers remain as inert save-lookup definitions with `allowed`, `activation`, and `available` false, an unconditional cancellation trigger, and no completion, timeout, cancellation, payment, or weather effects.
Those identities preserve native lookup while retiring the prototype behavior.
No recurring world hook or additional all-country scan was introduced.

The current source-contract test passes and is retained in `033_acid_rain_source_contract_2026_10_03.json` with the exact source hashes.
It checks native removal behind active-mission guards, scoped callers, blocked legacy activation, absence of callbacks and activation calls, and acute-only migrated coverage.
The complete acceptance run then stops at the separate cluster Major-pacing assertion.
Current source commits Minor pacing at a repeatable trigger's launch and resets Major pacing when a delayed Event 33 member dispatches.
The requested mixed-Major behavior requires a single Major commitment at launch when Event 33 is selected.
Immutable pre-patch cluster and logic sources have been retained for the probability auditor before that separate repair.

Relevant references were read directly after the MCP reference request lost its handle and source lookup timed out:

- Installed `documentation/effects_documentation.md`, lines 6083-6092, documents country-scoped `remove_mission`.
- Installed `documentation/triggers_documentation.md`, lines 3022-3029, documents `has_active_mission`.
- Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, line 1916, documents `remove_mission`.
- Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, line 649, documents `has_active_mission`.
- Installed `common/decisions/ENG.txt` has `remove_mission` precedents at lines 4300 and 4400.
- Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`, lines 467-478, documents mission duration, activation, completion, and cancellation.
- Installed `common/decisions/_documentation.md`, lines 1-40, documents permanent `allowed` filtering and the evaluation scopes.

Installed effects documentation SHA-256: `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
Installed triggers documentation SHA-256: `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.

No save was supplied for this checkpoint, and no live game was launched.
Save migration, reload, multiplayer, and executed population-loss evidence remain open.
The local native cleanup source tranche is ready for a scoped commit.
That commit does not establish full migration, event, GUI, probability, or live-game acceptance.
