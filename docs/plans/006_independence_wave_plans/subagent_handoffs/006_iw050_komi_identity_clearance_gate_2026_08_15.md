# IW-050 Komi Identity Clearance Gate

## Disposition

`SOURCE-HARDENED / CENTRAL ADMISSION STILL HOLD-FAIL-CLOSED`

The package-local `has_independence_wave_komi_command_roster` predicate now requires the parent-owned `independence_wave_iw_050_identity_rights_cleared` flag in addition to the exact vanilla `KOM_pavel_murashev` character. This prevents the generic vanilla portrait token from satisfying Event 006 setup while the researched 1936 identity and rights gate is unresolved.

## Changed source

- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt`
  - Added the identity/rights clearance flag to the Komi roster predicate.
  - Left the vanilla character, history, flag ladder, package effects, central dispatcher, attestation, preflight, scenario, and Join surfaces unchanged.
- `docs/events/006_independence_wave/komi_package.md`
  - Documented that the roster checkpoint requires the parent-owned clearance flag.

## Evidence

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw050_komi_portrait_source_audit_2026_08_14.md` records that no attributable 1936 Pavel Murashev portrait or authentic Komi institutional image has been accepted.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw050_komi_symbol_research_2026_08_14.md` records that the neutral and route-specific flag provenance is also unresolved.
- The vanilla `KOM_pavel_murashev` character remains untouched and is still required by the package-local roster predicate.
- Static check after the change: the Komi trigger has 86 opening and closing braces, one exact character consumer, one identity-clearance requirement, and no unsupported comparison operators.
- Mandatory Event MCP scan returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, with workspace-wide helper/lifecycle analysis deferred and zero selected blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a8f1dfd5a81de257e4ec2dfa64772f8aafd5960bd41e0d7377a40d36c256b48/4341f420e80deca5a35afabab988fe824bb7c792a2ee7a924715068f34df98fc/event-scan-741883f50501.json`.
- Mandatory map inspection still returns `MAP_STATE_ID_COLLISION` for explicit state `397` from `game:history/states/397-Syktyvkar.txt`.
- Mandatory Komi AI inspection returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, and zero unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7324f973006ab2caba9b5d683e5c095399430b98f4d3e864a77e6ce6666349f1/30c21d6c9bc52bc51ddb3ac282af32e81985b4e8a9373c188214184dc64f4f3d/probability-inspect-78be03b0b074.json`.

## Remaining gates

IW-050 remains package-local and fail-closed. The parent-owned clearance flag has no local setter, the exact portrait and flag evidence remain unresolved, the installed-map collision and typed probability limits remain documented, and central authority remains 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows. No central admission or Join change is authorized by this correction.
