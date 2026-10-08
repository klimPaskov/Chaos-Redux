# Event 033 evolution log context

Disposition: implemented bridge repair with focused source-frame evidence, evolution controls and native log acceptance remain open.
Parent acceptance follows the user's requirement to wire each actual Acid Rain evolution through the shared log with its own stage and tier.

The caller supplied `acid_rain_evolution_stage` and `acid_rain_evolution_tier`, but `acid_rain_record_evolution` forwarded neither to the shared recorder.
The actual shared recorder defaults an absent stage to 1 and an absent tier to 0, and retains present ambient values.
The bridge now writes both exact caller inputs into its shared context before invoking that recorder.
No eligibility, chance, weight, threshold, cooldown, date, receipt or Chaos formula changes in this repair.
No shared logger or unrelated event source is edited.

`.tools/validation/test_033_evolution_log_context.js` executes the actual bridge body under separate conservative parent/child temporary frames.
Eighteen cases cover stages 1/2/3, absent or stale shared metadata and host/no-host contexts.
The actual shared logger's stage/tier append-field bindings are checked directly, while recording is an explicit call spy rather than native row execution.
The immutable before source in commit `03447df6c5e4226525d2c26dc450f103d2297e78` fails the test because both metadata fields are absent.
The after runtime SHA-256 is `94c0c9d3c8b8b63f57878033648bb71b1f34ac89739d279a299ec3f163c1a510` and all eighteen source-frame cases pass.
The actual shared logger SHA-256 at test time is `2f102f595fd53f36943bad657ddeb557743248d4144695b4b036f778d4afcd83`.
This test does not execute caller impact receipts, evolution enablement, actual native arrays or the in-game log interface.

Primary sections read are installed `documentation/effects_documentation.md:7820-7827`, SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-443`, SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
The installed `common/scripted_effects/00_scripted_effects.txt:837-854` provides the temporary scratch pattern, while the shared logger at `common/scripted_effects/chaosx_events_log_effects.txt:1030-1115` is the direct project consumer contract.
The live MCP reference-context/search routes returned source identities with omitted sections explicitly retained as limits.
Revision-bound reads and a narrow shared-recorder lookup remain independently tracked, without promoting a dispatched request into successful evidence.
No native gameplay or full event-completion claim is made.
