# Event 006 Existing Carrier-Shell Release Execution Fix

Date: 2026-08-20

## Disposition

Implemented a narrow execution fix for the empty AXX, BAX, and BBX carrier shells. The shells are intentionally present in startup history so their Event 006 character definitions can be recruited, but they have no owned states or capital at game start. The fixed-tag `release` effect is a no-op when its target country already exists, so sending an empty shell through that effect could leave the target without a valid capital and produce the `capital_scope` errors reported during startup.

## Source change

Changed `common/scripted_effects/006_independence_wave_execution_effects.txt` in `independence_wave_release_one_frozen_country`.

- Absent targets still use the former-host `release` effect and autonomy handoff.
- Existing targets are sent through that release block only when they are not an existing dormant Event 006 shell.
- Existing dormant shells proceed directly to the already-present planned-core and state-transfer steps. The execution pass assigns the frozen anchor as capital before package setup, so the shell becomes a normal playable country without relying on a no-op release.
- Living targets remain rejected by the existing plan metadata and dormant-target validation; this change does not broaden candidate admission.

## Related guards already in source

The AXX/BAX/BBX package availability triggers now use their fixed numeric anchor states (`82`, `184`, and `185`) instead of `capital_scope` on a country that has no capital. The dormant-country predicate allows only absent tags or existing shells with zero owned and controlled states and no Event 006 or Event 005 origin flags. No `capital_scope` reference remains in the three package trigger files named by the startup errors.

## Pre-event surface and costs

The pre-event crisis category, mission, pressure, and cost surface remains retired. `chaosx.nr6.1` is hidden and triggered-only; the visible report is reached only after a positive committed release. The active Event 006 decision-cost localisation remains the compact amount-plus-icon form in `localisation/english/006_independence_wave_decisions_l_english.yml`; no cost constants or gameplay costs were changed in this fix.

## Evidence and limits

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 40 adapters, 32 attestations, and 29 compatible reservation groups.
- Targeted source search found no `capital_scope` in the AXX, BAX, or BBX package trigger files.
- Focused `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics at revision `56319cc12de881e50904384f7991f675b88c92bf9c05828ec8c86ff0efb828fa`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/314876f5034dd115062f63fb71acfc483dc10e390eb79cae052323ca1cd76b49/36894e3a8f6a0c4a08723e8ff0f9933ddef10b1a2700f2ef8bb7fd892b3d63c9/event-lint-56319cc12de8.json`.
- Focused `hoi4.event_render` state output returned `EVENT_RENDERED_PARTIAL` with zero selected blocking diagnostics. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1c8e26b81779df1b645e81fde3b0aa8e8e29c56e767404561d05a3022c7f508/16584ebcc8e3e0a4540792ef17145d1cb64ec3b4057e47e2e3602a28159145d0/event-state-56319cc12de8-manifest.json`.
- The MCP workspace is large and deferred helper/lifecycle projection, so these receipts are structural evidence rather than live-game proof.

No central attestation, Join order, pre-event UI, asset, focus, or decision gameplay files were widened by this fix.
