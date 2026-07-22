# GFX handoff: biological prototype reward-card icons

Suggested existing target: `interface/special_projects/biowarfare.gfx`

All textures are exact `198x218` legacy one-level uncompressed BGRA DDS files under `gfx/interface/special_project/rewards/biowarfare/`. Add the following sprite definitions without changing names or paths:

```text
spriteType = { name = "GFX_sp_anthrax_reward_caution" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_caution.dds" }
spriteType = { name = "GFX_sp_anthrax_reward_field_testing" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_field_testing.dds" }
spriteType = { name = "GFX_sp_anthrax_reward_antibiotics" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_anthrax_reward_antibiotics.dds" }
spriteType = { name = "GFX_sp_plague_reward_caution" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_caution.dds" }
spriteType = { name = "GFX_sp_plague_reward_field_testing" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_field_testing.dds" }
spriteType = { name = "GFX_sp_plague_reward_antibiotics" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_plague_reward_antibiotics.dds" }
spriteType = { name = "GFX_sp_tularemia_reward_caution" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_caution.dds" }
spriteType = { name = "GFX_sp_tularemia_reward_field_testing" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_field_testing.dds" }
spriteType = { name = "GFX_sp_tularemia_reward_antibiotics" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_tularemia_reward_antibiotics.dds" }
spriteType = { name = "GFX_sp_smallpox_reward_caution" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_caution.dds" }
spriteType = { name = "GFX_sp_smallpox_reward_field_testing" texturefile = "gfx/interface/special_project/rewards/biowarfare/sp_smallpox_reward_field_testing.dds" }
```

The parent agent should wire these exact sprite ids to the matching eleven placeholder-picture consumers in `common/special_projects/projects/biowarfare_main_projects.txt`. Do not substitute the existing `161x98` `GFX_sp_*_bomb` project icons.

Full package manifest and source/processed/hash/validation records: `manifest.md`.
