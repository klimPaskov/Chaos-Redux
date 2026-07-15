# Event 014 Origin Specialist Icon Cleanup Handoff

Date: 2026-07-15

## Outcome

- Regenerated `goal_cannibalism_warlord_train_the_origin_specialists` as a distinct 94x86 focus icon with exactly three origin motifs: an Island Host naval grapnel and landing rope, a Siege Commune entrenching shovel and masonry, and a March Host spoked wheel with mount tack and rolled road gear.
- Removed all package copies and ledger, manifest, handoff, contact-sheet, and validation references for four retired prison assets:
  - `goal_cannibalism_warlord_prison_unite_cells_and_guards`
  - `goal_cannibalism_warlord_prison_infiltrate_the_transfers`
  - `goal_cannibalism_warlord_prison_arm_the_penal_columns`
  - `goal_cannibalism_warlord_prison_lockhouse_network`
- Preserved the current generic containment assets `goal_cannibalism_warlord_secure_the_prisoner_ledger` and `goal_cannibalism_warlord_seize_prisons_and_depots`.
- Repaired source provenance for four current 64x64 spirit icons with independent spirit-specific imagegen compositions:
  - `idea_cannibalism_closed_muster_rolls`
  - `idea_cannibalism_archipelago_hunt`
  - `idea_cannibalism_city_that_eats`
  - `idea_cannibalism_moving_front`
- The focus package now contains 68 current assets. The registered static package remains exactly 30 current assets.
- No gameplay script, `.gfx`, localisation, or specification file was edited.

## Files and asset surfaces changed

- `docs/assets/014_cannibalism/warlord_focus_icons_imagegen/`
  - Replaced the origin-specialist source, alpha, processed PNG, and package DDS.
  - Removed the four retired IDs from source, alpha, processed, and DDS directories.
  - Updated the prompt ledger, processor inventory count, manifest, GFX handoff, validation ledger, and all three contact sheets.
- `gfx/interface/goals/014_cannibalism/goal_cannibalism_warlord_train_the_origin_specialists.dds`
- `docs/assets/014_cannibalism/registered_static_icons_imagegen/`
  - Replaced source, alpha, processed PNG, and package DDS for the four listed spirit icons.
  - Updated prompt provenance, manifest, validation ledger, and the four contact sheets affected by idea artwork.
  - The decision/category-only contact sheet remained byte-identical.
- Four matching live idea DDS files under `gfx/interface/ideas/014_cannibalism/`.
- This handoff file.

## Imagegen provenance

The exact focus prompt and output hint are recorded in `docs/assets/014_cannibalism/warlord_focus_icons_imagegen/prompts/focus_icon_prompt_ledger.json`.

- Origin specialist output hint: `C:/Users/klimp/.codex/generated_images/019f64e2-969d-7b03-a2dc-2b90103c4ad0/exec-89c80ac1-ee92-4667-b1fb-124df0c89f14.png`

The exact four spirit prompts and output hints are recorded in `docs/assets/014_cannibalism/registered_static_icons_imagegen/prompts/registered_static_icons_prompts.md`.

- Closed muster rolls: `C:/Users/klimp/.codex/generated_images/019f64e2-969d-7b03-a2dc-2b90103c4ad0/exec-76da8398-3fe7-4da2-a76d-c4f7a291a20f.png`
- Archipelago hunt: `C:/Users/klimp/.codex/generated_images/019f64e2-969d-7b03-a2dc-2b90103c4ad0/exec-4e4c0ff1-9774-4e92-a786-ea1b78008ddc.png`
- City that eats: `C:/Users/klimp/.codex/generated_images/019f64e2-969d-7b03-a2dc-2b90103c4ad0/exec-4b6e5977-ef98-46cd-879f-c9fd7ebad6cc.png`
- Moving front: `C:/Users/klimp/.codex/generated_images/019f64e2-969d-7b03-a2dc-2b90103c4ad0/exec-fd799629-6e92-4bd5-972a-a73927914460.png`

No CLI image generator, borrowed art, or fallback source was used.

## Visual audit

- The origin-specialist icon visibly contains the required grapnel and rope, shovel and masonry, and wheel, tack, and road gear. It contains no prison imagery, fourth origin, sacred or Indigenous motif, named leader, portrait, text, logo, or watermark.
- Closed muster rolls uses a leather dispatch cylinder, three blank rolled sheets, a plain roster strap, and blank tags.
- Archipelago hunt uses a brass signal lamp, exactly three basalt island forms, and a torn net.
- City that eats uses an industrial ration cauldron, gear, brick arch, and smokestack.
- Moving front uses an empty marching boot, spoked road wheel, empty helmet, and rolled field pack.
- The four spirits use independent silhouettes and are not resized or adapted from focus art. Their generated sources use flat chroma green. The final icons contain no visible key green, text, cultural or sacred motif, or portrait.

## Independent validation evidence

### Focus package

- Ledger, source, alpha, processed, package DDS, manifest, GFX handoff, and validation inventory each contain exactly 68 current IDs.
- All 68 source files and all 68 normalized processed compositions are unique.
- Every processed icon is 94x86 with transparent corners and zero visible chroma-key green.
- Every package DDS matches its live DDS byte for byte and uses a legacy one-mip uncompressed 32-bit BGRA header and payload matching the processed PNG.
- Origin-specialist processed RGBA SHA-256: `c90cfa7b3c94dc71033b65a5c6a82f13c054bc2dccb4ac477ed5556d4da32c3b`
- Origin-specialist DDS SHA-256: `4953526a9453bf3ab605b0089f1f93aca9c2249085a2f1b9bffe56b4ecbb06e3`
- The four retired IDs are absent from package and live asset paths. The two generic containment IDs remain present.

### Registered static package

- Validation, source, processed, package DDS, manifest mapping, and live `.gfx` mapping counts are exactly 30. Alpha count is 29 because the 114x101 category panel is intentionally opaque.
- All 30 source files and all 30 normalized processed compositions are unique.
- Every package DDS matches its registered live DDS byte for byte. Dimensions, BGRA masks, one-mip payloads, transparent corners, opacity rules, and zero visible chroma-key green validate for all 30 assets.
- `idea_cannibalism_closed_muster_rolls`: processed RGBA `a8962825676f33c48abc125f859622720ab5ad4040b4bf798b60c81afe37a3ea`; DDS `0af64b0808b29e144a85af94d1091587ddc783aa82f59e8e7a5fe7ad960b3efe`.
- `idea_cannibalism_archipelago_hunt`: processed RGBA `6ca2e9e93906c3522b53186cbfead158338ee5150d19ddd5be25d0fa715da1e3`; DDS `390de4c2c0e2ddc0a524b2dc12adfc53158bc0e8e1d2dd43dcf5f4de29767355`.
- `idea_cannibalism_city_that_eats`: processed RGBA `16a71b657de0982d018693402e9f8f71ca0a7f58c82dd8c41005617201219145`; DDS `f6cbc153170f038abb5bb18dd552f51b07a84f0411b486618bb0c4765c3e76ab`.
- `idea_cannibalism_moving_front`: processed RGBA `1a5992e7dc45ae697049d03cffd8fad576dad4de31101df6f8fad43926c6aab4`; DDS `6a8e0f327f84fd992ce29869a3ce2f788e110be2c9e94dbabbdc44c0c700f459`.
- A before-and-after hash inventory remained 132 files with zero additions or removals. Exactly the four target source, alpha, processed, package DDS, and live DDS sets changed, together with their affected review artifacts, manifest, prompt record, and validation ledger. The other 105 files in that inventory remained byte-identical.
- The removed `idea_cannibalism_lockhouse_network` and `idea_cannibalism_prison_host_origin` live DDS files remain absent. No orphan idea or removed origin was restored.

## Skills used

- `chaos-redux-event-assets`
- `imagegen`
- `chaos-redux-subagents`

No skill was created or modified.

## Simplifications, omissions, fallbacks, and blockers

None.
