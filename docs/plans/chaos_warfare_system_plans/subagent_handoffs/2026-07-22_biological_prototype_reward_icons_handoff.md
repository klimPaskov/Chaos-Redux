# Biological prototype reward-card icons handoff

Date: `2026-07-22`

Producer: Chaos Redux generated icon production subagent

Scope: bounded fictional UI art package replacing eleven `GFX_PLACEHOLDER_sp_project_picture` consumers in `common/special_projects/projects/biowarfare_main_projects.txt`.

The parent agent owns the gameplay replacement and `.gfx` edit. This handoff contains the exact sprite names, texture paths, target canvas, and ready-to-copy wiring. No gameplay, localisation, `.gfx`, raid, or existing Chaos Redux icon file was edited by the producer.

## Runtime contract

- Target: `198x218`.
- Format: legacy one-level uncompressed 32-bit BGRA DDS, no mipmaps.
- Exact DDS length: `172784` bytes.
- Transparency: RGBA source/processed PNGs with transparent outer corners; DDS alpha minimum `0`, maximum `255`.
- Runtime precedent: current vanilla `GFX_PLACEHOLDER_sp_project_picture` texture, not the separate `161x98` special-project project-icon surface.
- Final folder: `gfx/interface/special_project/rewards/biowarfare/`.
- Suggested existing `.gfx` target: `interface/special_projects/biowarfare.gfx`.

## Exact sprite wiring

Add these `spriteType` blocks to `interface/special_projects/biowarfare.gfx`:

```text
spriteType = {
    name = "GFX_sp_anthrax_reward_caution"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_caution.dds"
}
spriteType = {
    name = "GFX_sp_anthrax_reward_field_testing"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_field_testing.dds"
}
spriteType = {
    name = "GFX_sp_anthrax_reward_antibiotics"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_antibiotics.dds"
}
spriteType = {
    name = "GFX_sp_plague_reward_caution"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_caution.dds"
}
spriteType = {
    name = "GFX_sp_plague_reward_field_testing"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_field_testing.dds"
}
spriteType = {
    name = "GFX_sp_plague_reward_antibiotics"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_antibiotics.dds"
}
spriteType = {
    name = "GFX_sp_tularemia_reward_caution"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_caution.dds"
}
spriteType = {
    name = "GFX_sp_tularemia_reward_field_testing"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_field_testing.dds"
}
spriteType = {
    name = "GFX_sp_tularemia_reward_antibiotics"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_antibiotics.dds"
}
spriteType = {
    name = "GFX_sp_smallpox_reward_caution"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_caution.dds"
}
spriteType = {
    name = "GFX_sp_smallpox_reward_field_testing"
    texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_field_testing.dds"
}
```

The parent should replace each requested placeholder picture reference with its matching sprite id exactly as named above. Do not point these consumers at the existing `GFX_sp_anthrax_bomb`, `GFX_sp_plague_bomb`, `GFX_sp_tularemia_bomb`, or `GFX_sp_smallpox_bomb` `161x98` project icons.

## Delivered final DDS files

- `gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_caution.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_field_testing.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_antibiotics.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_caution.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_field_testing.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_antibiotics.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_caution.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_field_testing.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_antibiotics.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_caution.dds`
- `gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_field_testing.dds`

## Source and intermediate files

Source PNGs, one independent ImageGen output per id:

- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_anthrax_reward_caution.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_anthrax_reward_field_testing.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_anthrax_reward_antibiotics.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_plague_reward_caution.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_plague_reward_field_testing.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_plague_reward_antibiotics.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_tularemia_reward_caution.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_tularemia_reward_field_testing.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_tularemia_reward_antibiotics.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_smallpox_reward_caution.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/source_png/sp_smallpox_reward_field_testing.png`

The matching keyed intermediate PNGs are in `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/intermediate_png/` with the same ids plus `_keyed`. The matching exact-size processed PNGs are in `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/processed_png/` with the same ids.

## Package documentation and review files

- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/manifest.md`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/prompts/imagegen_prompt_records.md`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/hashes/sha256.txt`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/validation/dds_validation.json`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/validation/visual_validation_notes.md`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/gfx_handoff.md`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/contact_sheets/source_keyed_contact_sheet.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/contact_sheets/processed_checker_contact_sheet.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/contact_sheets/final_dds_contact_sheet.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/reference_inspection/vanilla_placeholder_sp_project_picture.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/reference_inspection/vanilla_sp_reward_icon.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/reference_inspection/chaos_sp_anthrax_bomb.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/reference_inspection/chaos_sp_plague_bomb.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/reference_inspection/chaos_sp_tularemia_bomb.png`
- `docs/assets/chaos_warfare_system/stage_7_biological_warfare/prototype_reward_icons/reference_inspection/chaos_sp_smallpox_bomb.png`

## Validation result

All eleven icons pass exact dimensions, DDS legacy-header checks, alpha checks, transparent-corner checks, zero chroma-key residue, and exact RGBA decode equality. The producer did not edit gameplay or `.gfx`; the only remaining work is parent-agent wiring and consumer replacement.
