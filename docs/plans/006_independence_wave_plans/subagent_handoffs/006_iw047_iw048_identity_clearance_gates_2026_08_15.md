# IW-047 and IW-048 Identity Clearance Gates

## Disposition

`SOURCE-HARDENED / CENTRAL ADMISSION STILL HOLD-FAIL-CLOSED`

The package-local MEL and UDM roster predicates now require parent-owned identity/rights receipts in addition to their exact vanilla character tokens. This prevents unresolved generic portrait consumers from satisfying Event 006 setup or later admission by character-token presence alone.

## Changed source

- `common/scripted_triggers/006_independence_wave_mari_package_triggers.txt`
  - `has_independence_wave_mel_command_roster` now requires `independence_wave_iw_047_identity_rights_cleared` and `MEL_zinovy_zhadinov`.
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt`
  - `has_independence_wave_udm_command_roster` now requires `independence_wave_iw_048_identity_rights_cleared` and `UDM_boris`.
- `docs/events/006_independence_wave/mari_el_package.md`
- `docs/events/006_independence_wave/udmurtia_package.md`
  - Document the parent-owned flags and their unset-by-default state.

No central adapter, content-attestation OR list, normal or scenario preflight, deterministic Join, character, portrait, flag, map, event-root, or workbook source changed.

## Evidence

- `006_iw047_mari_el_portrait_source_audit_2026_08_14.md` records no defensible exact 1936 identity or rights-cleared portrait for the MEL token.
- `006_iw048_udm_boris_berman_portrait_research_fail_closed_2026_08_14.md` records no defensible exact identity, office-role, or portrait source for the UDM token.
- Static checks after the change: each touched trigger remains balanced, each roster predicate has exactly one character consumer and one identity-clearance requirement, and no unsupported comparison operators were introduced.
- Both package docs retain the existing fail-closed central boundary and explicitly provide no local setter for either flag.
- Mandatory Event MCP scan for the MEL trigger returned `EVENT_INSPECTED_PARTIAL` at revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, with zero selected blocking diagnostics and the known deferred workspace-wide helper/lifecycle analysis. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eaff6e3ced83240b681f26dea972fa233a002d3250bb8face9be8de7e22114fe/b899e5cc47ee734e3f2c797ffcafe35e731cbabb101edcf90be3fb68ec88842c/event-scan-741883f50501.json`.
- Mandatory Event MCP scan for the UDM trigger returned the same `EVENT_INSPECTED_PARTIAL` boundary with zero selected blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d193c28afc86d49a66a860192e5255b7238d89218d12282d38eb1d5e322b88fd/d6938df178ebc54907c5aecb5d9586767652bcd5d00486f48cd7521cd94e6be1/event-scan-741883f50501.json`.

## Remaining gates

IW-047 and IW-048 remain package-local and unadmitted. Their identity/portrait, flag, map, typed probability, and central admission evidence remain unresolved. Current authority remains 40 runtime adapters, 32 content attestations, 29 compatible reservation groups, and 161 unattested selectable rows.
