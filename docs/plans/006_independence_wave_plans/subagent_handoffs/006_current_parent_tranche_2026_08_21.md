# Event 006 current parent tranche — 2026-08-21

## Disposition

Event 006 remains **HOLD / PARTIAL** against the accepted Independence Wave specifications. This handoff records the source fixes and portrait wiring completed in the current parent tranche without promoting any package or claiming live-game completion.

## Implemented source fixes

- `common/scripted_effects/006_independence_wave_roster_effects.txt` now owns the synchronous package-roster checkpoint used by the compatibility event and direct package setup callers. It writes package readiness receipts and preserves the approved character-scoped Montenegro and Bashkiria portrait overrides without creating a pre-event surface.
- `events/006_independence_wave.txt` keeps `chaosx.nr6.350` hidden and trigger-only, and the root event still presents only after a committed standalone or joint transaction.
- `common/scripted_effects/006_independence_wave_execution_effects.txt` records a non-player-facing terminal receipt for the standalone transaction, including plan phase, failure class, selected/expected counts, execution counters, and outcome flags.
- The Banat, Thrace, and Epirus dormant-carrier availability triggers use fixed anchor states 82, 184, and 185 with explicit ROM/GRE host ownership checks and no `capital_scope`. This prevents invalid-capital errors on AXX, BAX, and BBX before allocation. `.tools/audit_event6_allocator.py` now asserts that regression contract.
- The shared dormant-carrier predicate now uses the documented `num_of_controlled_states > 0` trigger guard instead of the invalid `num_controlled_states` variable. Existing empty carrier shells can therefore pass the dormant check while living countries remain excluded, allowing a direct Event 006 trigger to reserve and instantiate the admitted partial package set.

## Portrait wiring

Thirty-seven of the fifty-one supplied 156x210 DDS files were installed byte-for-byte into existing Event 006 runtime portrait basenames under `gfx/leaders/006_independence_wave/`. Existing `.gfx` and character consumers were preserved, and all installed targets pass the required DDS validation.

Fourteen supplied files remain intentionally unmapped because no safe existing Event 006 character, runtime basename, or portrait `.gfx` consumer exists. They are YAK (two), BYA (two), ALT (two), FER (two), KUR (one), ACX (one), ARX Gioacchino Solinas (one), FIJ (two), and GLC Alexandre Bóveda (one). The package and country audits keep those rows fail-closed; no real person was relabelled onto another consumer.

The source archive remains exactly one parent folder with one `processed` subfolder, and no 156x210 runtime DDS files were added to that archive. The complete mapping and the fourteen blockers are documented in `006_portrait_wiring_supplied_runtime_2026_08_21.md`.

## Documentation and validation

The source-of-truth map, FER package note, and simplifications report now describe the retired crisis boundary, `.350` as a readiness checkpoint, ordered FER anchors 408/409, and package-local versus central admission correctly.

The following static checks pass after this tranche: allocator, country API, SCN-008 scenario matrix, FORM-16, and Statehood Ledger semantic matrix. The allocator reports 149 publishers, 32 centrally attested packages, 29 compatible reservation groups, 40 runtime adapters, 161 unattested selectable rows, and a 20-package standalone witness with the `3/4/5/7/10` ladder.

The required narrow `hoi4.event_inspect` retry for `chaosx.nr6.1` was attempted after the source changes and timed out awaiting `tools/call` after 180 seconds. No new live-engine artifact or event comparison is claimed. Previous partial MCP artifacts remain source-linked evidence only.

## Remaining blockers

- The whole accepted event still lacks complete central admission for 161 selectable rows and typed same-scenario probability evidence.
- IW-051, IW-052, IW-053, IW-054, IW-057, and IW-060 remain package-local and fail-closed behind identity, map/origin, rights/asset, roster/force, and probability gates.
- Focus diagnostics, Statehood Ledger runtime render/save-load evidence, formable-puzzle runtime evidence, and complete event lifecycle comparison remain open.
- Super-event 23 remains blocked on exact redistributable audio rights. Super-event 24 remains source-wired but lacks complete reachability/playback evidence.
- No live manual transaction receipt was supplied by the user, so the new terminal receipt source contract cannot yet be matched to a runtime outcome.

No fallback, generic portrait, package promotion, pre-event crisis surface, or unlicensed audio substitute was added.
