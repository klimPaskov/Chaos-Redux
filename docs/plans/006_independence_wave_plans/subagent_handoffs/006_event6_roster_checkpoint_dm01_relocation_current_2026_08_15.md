# Event 006 roster checkpoints and DM-01 relocation handoff

Date: 2026-08-15

## Scope

This handoff records the focused current-worktree tranche in `events/006_independence_wave.txt` and `localisation/english/006_independence_wave_l_english.yml`. It does not widen central adapter admission, content attestation, reservation groups, scenario preflight, or Join order.

## Source changes

- Hidden `chaosx.nr6.350` now publishes explicit idempotent roster receipts for KOS, KUB, TAT, RUT, and BSK package setup. KOS and RUT attach their approved additive characters behind package and `has_character` guards. KUB and TAT retain their vanilla rosters. BSK retains vanilla Yakov Bykin and applies the Event 006 portrait override only inside the package branch.
- `chaosx.nr6.311` is a triggered country event for the existing DM-01 failure flag. Its relocation option selects an already owned and controlled non-capital state, moves the capital with `set_capital = { state = PREV remember_old_capital = no }`, records completion, clears the pending relocation flag, and refreshes country state. The dispersed-office option records completion without changing the capital.
- Localisation now covers the DM-01 relocation event, the first league congress event, and the revised opening declaration wording. The same file now supplies the missing `CHAOSX_COLLECTION_*` names consumed by the committed country-collection sources, including the Iberian key supplied by the existing Iberian localisation file.

## Static evidence

- Event braces are balanced at 258/258 and no unsupported `<=` or `>=` operators were introduced.
- `chaosx.nr6.350` and `chaosx.nr6.311` each occur exactly once in the event source.
- All seven `chaosx.nr6.35.*` and `chaosx.nr6.311.*` localisation keys occur exactly once.
- The Event 006 localisation file retains its UTF-8 BOM. Collection-name crosswalk across all English localisation files has no missing keys.
- Scoped `git diff --check` is clean. Existing unrelated worktree changes are intentionally preserved.

## MCP evidence

The mandatory read-only Event Chain Viewer calls were run against workspace `mod_chaos_redux_ea3b2d67c2c0` after the source changes.

- `hoi4.event_inspect` lint for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, with zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/780a96a3c6f0d2ddb5dedb24978efb1d5a162d18a10d1b7bea867104c03e0445/3c92008aa0c06e3c8af361267bd9d418418a4438c842b7377dfeafe6ef451143/event-lint-741883f50501.json`.
- `hoi4.event_render` state view for `chaosx.nr6.350` returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and one selected node. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fed96944cbee9cc74dce8b54241a2a0db51d003dcf9bccff4705ea8f0baa7a91/7dfe01bd84b570da820bddbba44e78dbbb6b42aebdf50966a6c14753eda0530c/event-state-741883f50501-manifest.json`.
- `hoi4.event_inspect` lint for `chaosx.nr6.311` returned `EVENT_INSPECTED_PARTIAL` at the same revision, with zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b42093d325cb89285cabc66e42135d719b24059376d465eb00589551ee04498/2bc8eda72a5bef5208ef9fcf5a5908a4c199b81b150de611f5fe9f21b398ed58/event-lint-741883f50501.json`.
- `hoi4.event_render` state view for `chaosx.nr6.311` returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics and three selected nodes. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f4a366e69f3bc6142542418b1d30ecccaef37b07e798026c62639ded530318d/9afc9cab3576fbb09ccd2e912f458144954d7c7b472c2b7f175879d8b6a6b550/event-state-741883f50501-manifest.json`.

The MCP validation remains partial because the large workspace defers helper projection and lifecycle analysis. These receipts support source-linked structure only. They do not prove live game execution, save/load behavior, same-tick cancellation order, or event-log presentation.

## Remaining boundary

The current whole-event authority remains 40 adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows. No central attestation or Join change is included here. Portrait, flag, probability, GUI, super-event, and package-admission gates remain governed by their existing handoffs.
