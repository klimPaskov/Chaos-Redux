# Event 028 state-modifier artwork

Disposition: seven original replacement candidates accepted by the parent and installed at their existing runtime paths on 2026-10-04; live consumer acceptance remains open.
Acceptance basis: the user's full visual-repair instruction and the seven state-modifier rows in Part 9 and the asset prompt authorize original artwork after the exact missing-master recovery route returned no sources.
This replaces artwork, not the accepted gameplay or icon family.
The missing historical masters remain unrecovered and are not reclassified as the new originals.

## Runtime crosswalk and review

Every texture below is one transparent 32×32 frame in `gfx/interface/state_modifiers/028_asteroid_incoming/`.
The stable sprite declarations remain in `interface/028_asteroid_incoming.gfx` and the state consumers remain in `common/dynamic_modifiers/028_asteroid_incoming_dynamic_modifiers.txt`.
All seven candidate identifiers are `E028-STATE-<row>-CAND01`.
The parent independently opened each complete original, each native processed PNG, each native decoded DDS, both current family sheets, and the canonical state-modifier reference sheet before accepting the candidates.

| Row | Texture basename and actual consumer/sprite suffix | Parent visual verdict | Final DDS SHA-256 |
| --- | --- | --- | --- |
| 01 | `main_asteroid_crater` / `asteroid_incoming_main_crater` | Accepted: broad empty deep basin, fractured rim, no radioactive motif; distinct from the smaller shard pit. | `65c761e834ef95cdbc66bdf112d4cb5ca47555e3145f3120567d0aec32a30dcb` |
| 02 | `catastrophic_impact_zone` / `asteroid_incoming_catastrophic_impact_zone` | Accepted: collapsed multi-storey masonry silhouette and dense wreckage read as catastrophic damage. | `a9a846484a5d328c4825d2dfcb938dd2e7c23e30cb148e9d9c089ee0c63e16ae` |
| 03 | `major_impact_zone` / `asteroid_incoming_major_impact_zone` | Accepted: crushed period freight wagon has a lower transport silhouette than the urban wreckage. | `dc88545b58303791ef4accd2232ee5a290eb4e3423a128b585746173daf189c4` |
| 04 | `outer_shock_zone` / `asteroid_incoming_outer_shock_zone` | Accepted: leaning telegraph pole and buckled rails remain recognizable at native size. | `994cc771144af1678650f540ca6ad694a4255a887649be87ec8cee551eba59f9` |
| 05 | `fragment_crater` / `asteroid_incoming_fragment_crater` and `asteroid_incoming_fragment_center_recovery` | Accepted: smaller shallow pit, visible embedded dark fragment, distinct footprint from the main basin. | `5b1d4d6e48f7da44f404d1a8f46cdc9863a5b5bc4fd65f90fcfca320062a0962` |
| 06 | `heavy_fragment_damage` / `asteroid_incoming_heavy_fragment_damage` | Accepted: a collapsed warehouse roof and missing wall communicate heavy structural loss. | `9c0fc3f1b3e45464a1eb68227b51a77bdcb655e9e2ce8603e07f93cc8300da6d` |
| 07 | `light_fragment_damage` / `asteroid_incoming_light_fragment_damage` | Accepted: mostly surviving factory with chipped masonry communicates lighter damage and differs from the collapsed warehouse. | `c7fa8fbb4ef0787e731997be5cc2e1d8392d438af63216885b560a4ba4a5dbb2` |

Every sprite suffix in the table is prefixed with the exact existing `GFX_idea_` identifier.
That legacy prefix does not turn these state icons into 64×64 national-spirit icons.
The fragment-center recovery alias is an existing same-site consumer, not an additional asset requirement.
Eight current sprite aliases consume seven unique files with seven unique file hashes and decoded pixel hashes.
The full current registry has 57 declarations with 57 unique identifiers after removing the local duplicate of shared slot `GFX_super_event_116_asteroid_impact`; that slot remains registered in `interface/chaosx_super_events.gfx`.

## Original generation and retained lineage

The artist made exactly seven distinct calls to the built-in ImageGen route, each requesting `transparent_background: true` at creation.
No CLI/API fallback, background removal, drawn primitive replacement, focus/decision/icon-family substitution, DDS enlargement, or transform-only subject derivation was used.
Each original is a 1254×1254 RGBA PNG; the actual returned originals remain under `C:/Users/klimp/.codex/generated_images/01a10233-dbbe-7b52-a18d-154764608d27/`.
The copied originals, immutable prompts, and actual tool receipts remain in the ignored active workspace `docs/assets/028_asteroid_incoming/regeneration/state_modifiers/` while the full event is incomplete.

| Asset | Actual returned original basename | Original PNG SHA-256 |
| --- | --- | --- |
| `main_asteroid_crater` | `exec-aafbf949-b326-4fca-992d-bf235e9312ef.png` | `17c9bfe48a41a4de8c0f0c5ad0bb43a086601b8ad4e714439b4d02f0da39ef8a` |
| `catastrophic_impact_zone` | `exec-74f17aa3-00f1-43f6-8d57-7a7c3d9333bf.png` | `299787e75a4922c95fd1ceaf002acf501d3a02b90a34f27d8074b93dbd63f007` |
| `major_impact_zone` | `exec-eb2c6aff-1cff-4dbf-b316-f15ebd0c74be.png` | `ff5aaa8bcbe5649b96cf13838ceb627d5f271e631c555aca728b05f986b674cf` |
| `outer_shock_zone` | `exec-745ad9f2-72b6-4f35-b6b7-06afa07adeee.png` | `921c79d05735e32424ff4f6778cb639419e48e7cacdb7f28471548ee9aaa4406` |
| `fragment_crater` | `exec-0eacefee-9643-4a7a-ba9a-0c57066f11d0.png` | `4bc25e89461f923c3fe4055d6cfa4f5ac2b4f5ea391b21f2352a81c24ce61b9d` |
| `heavy_fragment_damage` | `exec-f7b22fa6-d380-427a-9fba-722491391b92.png` | `fc1fbf130ab6eb4a1b3343f14d572421fe194e2c890136661b838a9b102609d6` |
| `light_fragment_damage` | `exec-9467f254-600c-4af6-8f0c-8f5f3c891ce8.png` | `3f7e6801aa078ea3ba68e64138277bb93275bfa98243f3baff5bdcc0e7c72b41` |

The authoritative producer evidence is [the state-icon handoff](../../../plans/028_asteroid_incoming_plans/subagent_handoffs/state_icon_regeneration_20261003.md).
Its record date is 2026-10-04 and its filename preserves the original assignment date.
The package's `reference_inspection_v1.json` records the exact fifteen canonical/installed state references and their pixel comparison.
Its `validation_v1.json` retains original, prompt, receipt, processed, DDS and decoded identities, explicit conversion commands, and reference consumers.
The selected art is version 1; version 2 refers only to the review-board layout and changes no icon pixels.

## Processing, replacement, and limits

Processing uses an alpha-2 visible crop with eight source pixels of guard, one aspect-preserving premultiplied Lanczos resize, and centered transparent placement.
The faint alpha-1 exterior remains in the untouched originals, and no alpha-2 painted subject is clipped.
The skill-local `convert_to_dds.py` produces a legacy uncompressed BGRA DDS with a strict 128-byte header and 4,224-byte total length.
All seven files retain alpha from 0 through 255, transparent outer borders, and exact decoded RGBA equality to their corresponding native PNGs.
The independent light, dark, and checker review found no matte, spill, clipping, or halo.

The parent checked every old runtime hash against the recorded before hash before replacement and preserved byte-exact old DDS copies in `runtime_before_20261004/` inside the active package.
Each promoted runtime file was then hash-compared with its accepted candidate.
The earlier before hashes and the initial path-only commit remain historical evidence in [state icon placement](../../../plans/028_asteroid_incoming_plans/state_icon_placement_20261003.md), not the current artwork identity.
No source master or working render is committed or pushed, consistent with the workspace rule.
Only the final DDS, curated provenance/review facts, and permanent handoff are delivery surfaces.

This seven-row artwork replacement introduces no simplification or omitted asset.
It does not establish live state-window rendering, map behavior, or complete Event 028 acceptance.
The other accepted asset families, nuclear-free presentation, gameplay findings, and required MCP/live scenarios remain separate gates.
The active workspace must be retained until full event completion, then cleaned under the event-assets skill after durable facts are promoted.

## Future scope

These seven state symbols need no additional family or animation.
Any later alternate state-art branch must have its own accepted requirement and source lineage; it must not reuse the separate 64×64 material icon as a state marker.
