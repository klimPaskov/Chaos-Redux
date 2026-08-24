# `cannibal_bone_riders` runtime handoff

Status: blocked at provider compound rig. Do not wire the model as an animated unit yet.

Proposed entity identifier: `cannibal_bone_riders_entity`. Proposed mesh identifier: `cannibal_bone_riders_mesh`. Proposed animation identifiers are `cannibal_bone_riders_idle`, `cannibal_bone_riders_move`, `cannibal_bone_riders_attack`, `cannibal_bone_riders_defend`, `cannibal_bone_riders_support_attack`, `cannibal_bone_riders_retreat`, `cannibal_bone_riders_training`, and `cannibal_bone_riders_death`. None has a final exported file because Meshy’s rig endpoint rejected the compound mounted pose.

The geometry candidate and local checkpoints are valid evidence, not a runtime deliverable. Final armature, weights, action import/retarget, DDS channel packing, io_pdx_mesh export, and reimport remain blocked behind a coherent professional provider rig/action source. Blender must not author replacement motion.

Proposed sounds are `cannibal_bone_riders_select`, `cannibal_bone_riders_move`, `cannibal_bone_riders_idle`, `cannibal_bone_riders_sling_release`, `cannibal_bone_riders_training`, and `cannibal_bone_riders_death`. Five sourced WAV candidates exist; stone impact remains blocked. Attribute the CC BY recordings as documented in `audio/audio_manifest.md`. Animation synchronization cannot be finalized until action frame ranges exist.

Existing counter consumers are `GFX_unit_cannibal_bone_riders_icon_medium`, `GFX_unit_cannibal_bone_riders_icon_medium_white`, and `GFX_unit_cannibal_bone_riders_icon_small`. Runtime DDS paths are `gfx/interface/counters/divisions_large/unit_cannibal_bone_riders_icon.dds`, `gfx/interface/counters/divisions_small/onmap_unit_cannibal_bone_riders_icon.dds`, and `gfx/texticons/unit_cannibal_bone_riders_icon_small.dds`. All three pass header, two-frame, alpha, and decoded-roundtrip validation. The parent owns final definitions and in-game validation.
