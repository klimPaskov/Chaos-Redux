# Event 006 Post-Release Instability asset registry reconciliation

Date: 2026-08-02

The accepted IDEA-06 lifecycle matrix and asset prompt require a distinct Post-Release Instability idea icon, but the original 48-row asset-family matrix stopped at ASSET-048. The runtime sprite, source master, processed master, and build-report entry already existed under stable implementation names and did not need new art or gameplay wiring.

## Resolution

- Added `ASSET-049` to `docs/specs/006_independence_wave_specs/matrices/006_asset_family_registry.csv` as the eighth idea-icon family for IDEA-06.
- Preserved `idea_independence_wave_post_release_instability` and `GFX_idea_independence_wave_post_release_instability` without renaming or moving the runtime consumer.
- Updated the Event 006 asset manifest, GFX handoff, icon prompt record, generated-art inventory, source-research handoff, and build report with the stable ID.
- Updated the specification package manifest with the new byte count, row count, and SHA-256 for the registry matrix.

## Evidence

- Source master: `docs/assets/006_independence_wave/source_png/ideas/idea_independence_wave_post_release_instability_source.png`.
- Processed master: `docs/assets/006_independence_wave/processed_png/ideas/idea_independence_wave_post_release_instability.png`.
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/idea_independence_wave_post_release_instability.dds`.
- Runtime GFX consumer: `GFX_idea_independence_wave_post_release_instability` in `interface/006_independence_wave.gfx`.
- Registry matrix after the patch: 50 UTF-8 lines including the header, 11,768 bytes, SHA-256 `bbecf73b11a0c5ed927c81519216688d614e2e5a9d58fd45eee08289e8dbfb1f`.
- `docs/assets/006_independence_wave/_tooling/icon_build_report.json` parses successfully after adding the ASSET-049 field.

This closes the Post-Release Instability stable-ID documentation gap only. ASSET-046 formable flag/emblem coverage, portrait shelf indexing, unresolved package assets, and super-event audio remain separate blockers. No advisor icon or portrait asset was created.
