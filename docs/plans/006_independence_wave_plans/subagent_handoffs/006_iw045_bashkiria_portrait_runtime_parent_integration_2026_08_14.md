# IW-045 Bashkiria portrait runtime parent integration receipt

Date: 2026-08-14.

This receipt supersedes the earlier source-only runtime hold for the IW-045 Yakov Bykin portrait. The grounded source-placeholder package remains the authoritative identity source, and no styled-final or RunPod workflow was requested.

## Runtime asset

- Source package: consolidated `docs/assets/portraits/006_independence_wave/`; the IW-045 original is flat in the parent, while crop/metadata evidence is under `processed/`.
- Subject: vanilla `BSK_yakov_bykin`, Yakov Borisovich Bykin.
- Source: Wikimedia Commons, MDobrom, CC BY-SA 4.0, with attribution and share-alike obligations preserved.
- Deterministic candidate: in-memory RGB 156x210 reconstruction from the exact crop, SHA-256 `470c6d4f6213c3ca7a0451e3440a5534b1e50333eec456f43cab204ad3644f34`; the consolidated parent/processed archive intentionally retains no 156x210 PNG for IW-045.
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_BSK_independence_wave_yakov_bykin.dds`, 156x210, legacy uncompressed BGRA, opaque alpha, one mip level, pixel payload round-trips to the candidate.
- Runtime sprite: `GFX_portrait_BSK_independence_wave_yakov_bykin` in `interface/006_independence_wave_iw045_bashkiria_portraits.gfx`.

The global vanilla `GFX_portrait_Yakov_Borisovich_Bykin` definition remains untouched. The Event 005 institutional `GFX_portrait_BSK_oilfield_workshop_council` is not reused.

## Parent-owned consumer wiring

`events/006_independence_wave.txt` now applies the dedicated sprite only inside the BSK vanilla-roster checkpoint after confirming `is_independence_wave_bashkiria_package` and `has_independence_wave_bsk_command_roster`. The idempotent `independence_wave_bsk_portrait_override` flag prevents repeat application during setup retries.

`common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt` clears the override receipt during setup and restores the original vanilla token during package cleanup when the override flag and character are present. The cleanup also clears the receipt flag. Ordinary BSK history and the vanilla character definition remain unchanged outside the package route.

## Validation and limits

The consolidated source package retains original bytes, exact crop, crop JSON, decoded equality evidence, provenance, and review. The 156x210 candidate PNG is intentionally not retained by the archive-consolidation policy; the portrait worker validated an in-memory deterministic reconstruction and the runtime DDS header, BGRA payload, and decoded pixel roundtrip. Event MCP state-flow inspect and render were rerun after the parent wiring and returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0cba4ce84ec0b206bb8e66d6d0c1dec6cbfeb86468d348038098a5556ee1273/e050f9b03023b41397b6239967e0782165798608bbea928c110f1107ac302d1f/event-state_flow-d21fdfa2723e.json`. Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0f7faaaa4c44e4244483f25657f9906a8819239d36602009c5601d8d2a09ad3/c14da708ded51c4314233374f3f74538099b5176a1df4e0d88a8af4af75be529/event-state-d21fdfa2723e-manifest.json`. The partial status reflects deferred workspace-wide helper and lifecycle projection, not a selected BSK portrait error. A fresh state-651 map inspect returned `MAP_INSPECTED` with selected state checks passing, while unrelated workspace-wide building and port position diagnostics remain. The corresponding state render returned `MAP_RENDERED` with validation passed. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa204178c3c3f4825a2d0d1088cfbbf53894f89040fd8c24493bae5e4a02078a/29ea86309a02dbf34a14cc31a86b7202a79907e337127998285df8fa9447cc34/map-inspect.cb30ffa8fc6cf855.json`. Render PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c90bb25bad065af436b3e522d687d23a1d0e7a65de26e17c4bb92feb465e856/5187ea6fa5e44eae4688619fc78a756e7e66784f11bcfed6d0e0ee8c6744321c/map-state.png`.

This receipt does not admit IW-045. Central adapter registration, content attestation, normal/scenario preflight, and Join ordering remain fail-closed. Quantitative AI balance also remains unproven because the BSK strategy adapter exposes no weighted surface and typed mission fixtures are incomplete.
