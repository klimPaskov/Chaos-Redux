# IW-015 GLC duplicate-identity audit

Date: `2026-08-14`.

## Verdict

IW-015 GLC remains `HOLD` and fail-closed for package admission. No gameplay patch is safe from the current evidence because Event 006 assigns the real person Alfonso Daniel Castelao to a second live character while vanilla Galicia already owns the same named identity as a country leader.

This audit does not change the central adapter, content-attestation, normal/scenario preflight, reservation-group, FORM-07, deterministic Join, or authority counts. The current boundary remains 40 runtime adapters, 32 attested packages, 29 compatible groups, and 161 unattested selectable rows. IW-015 is still one of the eight adapter-only rows.

## Source crosswalk

- Vanilla `history/countries/GLC - Galicia.txt` creates the country-leader roster containing `Alfonso Daniel Castelao` and `Fuco Gómez`; the vanilla leader uses `GFX_portrait_Alfonso_Daniel_Castelao`.
- Vanilla `interface/_leader_portraits.gfx` owns the `GFX_portrait_Alfonso_Daniel_Castelao` token. The vanilla history and portrait ownership remain authoritative for the GLC carrier.
- Event 006 `common/characters/006_independence_wave_iberian_commanders.txt` defines `GLC_independence_wave_alfonso_daniel_castelao` as a second character with a corps-commander role and `GFX_portrait_GLC_alfonso_daniel_castelao`.
- `events/006_independence_wave.txt` recruits that additive character in the hidden synchronous `chaosx.nr6.350` roster event whenever the GLC package is selected and the character is absent.
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt` requires both the additive character and an active corps-command consumer in `has_independence_wave_glc_command_roster`, alongside the vanilla `Fuco Gómez` country-leader witness.
- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` publishes the GLC command-roster checkpoint only after that trigger passes and retires the additive Castelao character during GLC cleanup.

The source therefore preserves the vanilla ruling roster but still creates two live Castelao identities at the same time: the vanilla country leader and the Event 006 corps commander. The role split is explicit in comments, but no accepted origin/ownership guard proves that the duplicate real-person consumer is intended or safe.

## Why no narrow source patch is justified

1. Removing the `recruit_character = GLC_independence_wave_alfonso_daniel_castelao` branch leaves the current roster trigger unsatisfied and prevents the package setup checkpoint from becoming valid.
2. Removing the additive character from `has_independence_wave_glc_command_roster` would let setup proceed without the declared corps-command consumer and would make the force-package gate weaker than the accepted source contract.
3. Retiring or replacing vanilla Castelao would mutate the carrier's authored history and route ownership. No accepted transfer policy, replacement leader, or source-backed identity is available.
4. Renaming the Event 006 role to another person requires a new 1936 Galician role/source/rights/portrait packet and cannot be invented as a local repair.

## Required owner decision

Before any GLC runtime change, choose and document one of these designs:

- Guarded reuse/transfer of the vanilla Castelao identity with an explicit country-leader-to-corps-command ownership contract and cleanup semantics.
- A distinct, source-backed Galician corps commander with an independent identity, role/date proof, portrait provenance, and runtime asset review.
- An intentional no-additive-commander design that rewrites the GLC roster and force-readiness contract together rather than silently weakening one trigger.

Until that decision and evidence packet exist, preserve the current fail-closed adapter and do not add a central attestation or Join entry.

## MCP and static evidence

The required read-only Event Chain Viewer pass was run for the shared synchronous roster event:

- `hoi4.event_inspect` trace selector `chaosx.nr6.350`: `EVENT_INSPECTED_PARTIAL`, revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, graph hash `37eb00185cb12c74f97438ecee7380780cf4eec14d3693f7930e97a91ce4b720`, zero selected blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f018d47bb80b33c7f1308c92079dc94fe63b19d8ef303a7d382a54bf9f10566d/8d4e5b2e1a6b59ca693c071793cde862bba1428087b310135fbddb512f4ddddc/event-trace-741883f50501.json`.
- `hoi4.event_render` state view for the same selector: `EVENT_RENDERED_PARTIAL`, same revision and graph hash, zero selected blocking diagnostics. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/719132e1ee54a8d5600bcdda54f061e4c7f9bffdef314f5076df073e56446cd0/d986982dc45b923e11ed1cbb015683ab6e1d69c239f44c5995b452740318a05e/event-state-741883f50501-manifest.json`; SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b221ba88360f39b5b3485aae88637d83299d88a520372905c772acdff23fe5d6/91319a62ff2300fd2fc8c7de59a9e5bf2499afbef28dd5648934ab0d628dc5a1/event-state-741883f50501.svg`.

Both MCP results are structural/source-linked evidence only: the large workspace deferred helper and lifecycle projection, and the inline inventory was truncated. They do not prove live save/load behavior or resolve the identity policy.

Static checks after the audit passed the allocator boundary (149 publishers, 40 adapters, 32 attested, 29 groups, 161 unattested), the 32-cell/8-edge-case SCN-008 matrix, and the broad country API carrier check (191 resolved unique carriers, no missing or duplicate carriers). These checks do not waive the GLC identity gate.

No gameplay, asset, localisation, central registry, attestation, preflight, Join, or workbook files were changed by this audit.
