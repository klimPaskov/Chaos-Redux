# Event 016 generic land counter completion

Status: `parent_reviewed`; the native-size contact sheet, decoded DDS round-trip, alpha treatment, frame separation, vanilla-green palette, and exact consumer filenames were accepted for repository wiring on 2026-09-01. User live-consumer acceptance remains external.

Scope completed: bespoke large and on-map two-frame counter strips for exactly `paleogenetic_creature`, `xenobiological_assault_organism`, and `temporal_guard`.

## Vanilla inspection

The canonical reference root used was `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`; no project-local visual-reference copy was used.

The large-land contact sheet inspected before individual references was `assets/vanilla_reference/units/land/counters_large/contact_sheet.png`.

The individual large references inspected were `unit_infantry_icon.png` (SHA-256 `CAF241717AF26CA1688742A86BE1A8A89C5A9B8CABA41410B4CF799827AD1972`), `unit_medium_tank_icon.png` (SHA-256 `95106F5538194B02189570747EA06B278E2BBF14455D85159B9542073826FCFE`), and `unit_motorized_icon.png` (SHA-256 `7CEC9A7C70CC7A021E187A1832BE3E9828BB27E3C901BA75E62EB9C4E803880C`), each native `152x42` with adjacent `76x42` frames.

The land-map contact sheet inspected before individual references was `assets/vanilla_reference/units/land/map_counters/contact_sheet.png`.

The individual map references inspected were `onmap_infantry.png` (SHA-256 `5A6274E5847CBE9D030B547B9C2BB723215269B234BEF227A43F273B22DC42B9`), `amphibious_tank.png` (SHA-256 `1018E8ED6BBF23BDB01997CEA90B57C12E686B417E4ACD05577A05F09BB8B034`), and `amphibious_mechanized.png` (SHA-256 `2F48152EA5D645A9545BE2A51C7292C6D03AB5F1B23B23D55BEEE11E10FB2B17`), each native `60x12` with adjacent `30x12` frames.

The installed-vanilla definition inspected was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`, including `GFX_group_infantry_icon`, `GFX_group_mobile_icon`, `GFX_group_armor_icon`, `GFX_unit_infantry_icon_medium`, `GFX_unit_medium_armor_icon_medium`, `GFX_unit_motorized_icon_medium`, and their `_medium_white` counterparts, all using `noOfFrames = 2`.

Installed definition-reference DDS files were `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` (`152x42`, SHA-256 `B33A8E3B69CC789EB0E31BA99F4E5BA4E5B0A8B51EC1A7A7F709C3516F720C23`), `unit_medium_tank_icon.dds` (`152x42`, SHA-256 `EB442EB0AAB913A70212E11602CE44F0991AF94AFE9B7E34CF770D0AC0206510`), `unit_motorized_icon.dds` (`152x42`, SHA-256 `5E68602744549ACAF18885925ABAE752D72CBAE6A005F233658651E17E5CE487`), `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` (`60x12`, SHA-256 `58AB78662C2A64A519B8D5D144582E7B2785915BD0A0A822696D87A9DE6F766C`), `onmap_unit_amphibious_tank_icon.dds` (`60x12`, SHA-256 `39CA305C05A1B6F2DF2DE86D9CFD2B7575AAE740698376D9A7F7E00E9A467AC4`), and `onmap_unit_amphibious_mechanized_icon.dds` (`60x12`, SHA-256 `E3B2B3DC50F48A8D7A44E318EEA23F004B51B8A4CCAE2DA99FB6FA2ACDD90DCE`).

The inspected vanilla large palette is muted green, with repeated body samples around RGB `(72,104,72)`, `(73,106,73)`, and lighter values up to approximately `(181,197,181)`; the alternate frame is pale neutral grey-white with values up to RGB `(238,238,238)`. The canonical map family is pale neutral grey-white, but these project strips retain the requested vanilla-green left normal state and pale neutral right alternate state.

## Generated and processed evidence

Built-in ImageGen was used separately for all six original source masters with genuine transparency requested in the initial calls. No background-removal fallback was used.

Source masters and exact prompts are retained under `docs/assets/016_brilliant_scientist/generic_counter_package/source_png/` and `docs/assets/016_brilliant_scientist/generic_counter_package/prompts/imagegen_prompts.md`.

Processed alpha PNGs are retained under `docs/assets/016_brilliant_scientist/generic_counter_package/processed_png/`.

The native-size review sheet comparing source, processed, smooth enlarged preview, and decoded DDS round-trip is `docs/assets/016_brilliant_scientist/generic_counter_package/contact_sheet/generic_counters_contact_sheet.png` (SHA-256 `9BDF3B7375711496AA231251D53C87C8E763FAC61E46D8E10936012FC68CD455`).

Strict header and pixel round-trip evidence is `docs/assets/016_brilliant_scientist/generic_counter_package/validation/dds_roundtrip.json` (SHA-256 `1BD8BBC0D0F7010BE9AF62FDD7538650AB2AB37F33E5026AD4EFEE94BC124F94`). All six DDS outputs use the converter's one-level 32-bit BGRA layout, have real alpha with extrema `0..255`, and decode pixel-identically to the processed PNGs.

## Runtime files and hashes

| Unit | Runtime DDS | Dimensions | Bytes | Final DDS SHA-256 | Processed PNG SHA-256 | Source PNG SHA-256 |
| --- | --- | ---: | ---: | --- | --- | --- |
| `paleogenetic_creature` large | `gfx/interface/counters/divisions_large/unit_paleogenetic_creature_icon.dds` | `152x42` | `25664` | `3D5F51CACCAF7F7CDC39266317AB457ADDE4199C7CFDC1E5E18583F7846927CC` | `8667C9E6C8573B0FDC88305D59CA1294C5C60526F26EEEAAF8BA7C1D1D3D2FB8` | `35670A20E59DA0B9A52D31CE8C6861138C6C453672B76994BA00753BC7238845` |
| `xenobiological_assault_organism` large | `gfx/interface/counters/divisions_large/unit_xenobiological_assault_organism_icon.dds` | `152x42` | `25664` | `38E94AFF9074AD710557333BB666AD6561AD2F0112373BE54757796D205C06BD` | `745ACC00910453A5E021F263EDF1869611470C2F1847FE36C3DB69ADE9CAABF2` | `79977BD09E21FFF7DAA799DFA2BE7C91A4BBFAABCA1CFDC732E573C4D1C1AF1E` |
| `temporal_guard` large | `gfx/interface/counters/divisions_large/unit_temporal_guard_icon.dds` | `152x42` | `25664` | `50622212016AC090ADD2D076E3E0B40896B932BCDA6A124083D0B1D0DDBF7C78` | `13315044E40F992B79BFA778A3B4D7297F818E64615BB6C6CE713F7EA0A75560` | `C1B88B330B1CF7F1A03D0AC9CBB4E727B4354007B0D2C489BFE4F21F08290240` |
| `paleogenetic_creature` on-map | `gfx/interface/counters/divisions_small/onmap_unit_paleogenetic_creature_icon.dds` | `60x12` | `3008` | `D8FF99C23ECFC9F706849D29672A1BBDB0ED1FA8D2EA4CF503760CA1EDAEBD46` | `887346825580446B1ADB47AD6E69C627D3B0E38F7575BEA6B11BAB26BF9C5F1B` | `A4E9A21E1AAB87C1EE59F331A0ACEF0F1AC40A4B9ADE56536AFE03821ABFC0A3` |
| `xenobiological_assault_organism` on-map | `gfx/interface/counters/divisions_small/onmap_unit_xenobiological_assault_organism_icon.dds` | `60x12` | `3008` | `2B5D99F75D76734BBDDCDB24EE0DB794D39B15460D8E0EBC0F3E7CB44B2DF854` | `9C316F22F472D539FB52F42D8783DF46AC84F49EEF3E0B424732B4E54D10D4C9` | `26A8F80BE2BA883ED02691616C3F970A8C878302426FFF68931215020B39214A` |
| `temporal_guard` on-map | `gfx/interface/counters/divisions_small/onmap_unit_temporal_guard_icon.dds` | `60x12` | `3008` | `995FF164E56AA3BBA23315203EBFA8D72CBCCF92D74F66485D718BA42BAFF8D7` | `419B65FA9411D6A2B8FC7680CDF309330EB4A5C77EDBB88825E12252D14754A9` | `FAF3B41A1784B6EE0157DA1D9E8C05059710F1E109FEA5BDC4751FFAFD74659E` |

## Sprite registration and owning consumers

The single narrow registration file is `interface/016_brilliant_scientist_generic_counters.gfx` (SHA-256 `3D0710FF16F5BE6B46207DA821F404CABBB26DCE540A9A8F37D039B7A573DD15`). It registers the following exact sprite names, each with `noOfFrames = 2`:

- `GFX_group_paleogenetic_creature_icon` and `GFX_unit_paleogenetic_creature_icon_medium` use `unit_paleogenetic_creature_icon.dds`; `GFX_unit_paleogenetic_creature_icon_medium_white` uses `onmap_unit_paleogenetic_creature_icon.dds`.

- `GFX_group_xenobiological_assault_organism_icon` and `GFX_unit_xenobiological_assault_organism_icon_medium` use `unit_xenobiological_assault_organism_icon.dds`; `GFX_unit_xenobiological_assault_organism_icon_medium_white` uses `onmap_unit_xenobiological_assault_organism_icon.dds`.

- `GFX_group_temporal_guard_icon` and `GFX_unit_temporal_guard_icon_medium` use `unit_temporal_guard_icon.dds`; `GFX_unit_temporal_guard_icon_medium_white` uses `onmap_unit_temporal_guard_icon.dds`.

The owning subunit consumers are `common/units/016_brilliant_scientist_project_forces.txt#paleogenetic_creature`, `#xenobiological_assault_organism`, and `#temporal_guard`. Their existing consumer tokens are `sprite = paleogenetic_creature`, `sprite = xenobiological_assault_organism`, and `sprite = temporal_guard`; the counter sprite names above are stable runtime aliases for the corresponding reusable land subunits.

## Changed files in this bounded subtask

- `gfx/interface/counters/divisions_large/unit_paleogenetic_creature_icon.dds`
- `gfx/interface/counters/divisions_large/unit_xenobiological_assault_organism_icon.dds`
- `gfx/interface/counters/divisions_large/unit_temporal_guard_icon.dds`
- `gfx/interface/counters/divisions_small/onmap_unit_paleogenetic_creature_icon.dds`
- `gfx/interface/counters/divisions_small/onmap_unit_xenobiological_assault_organism_icon.dds`
- `gfx/interface/counters/divisions_small/onmap_unit_temporal_guard_icon.dds`
- `interface/016_brilliant_scientist_generic_counters.gfx`
- this handoff file

The evidence package is retained under `docs/assets/016_brilliant_scientist/generic_counter_package/` for parent review and provenance. No gameplay, localisation, specs, spreadsheets, 3D models, other assets, or commits were changed.

## Blockers and review state

There is no production blocker: all six requested DDS files exist, are exact-size, strict-decodable, alpha-backed, and pixel-identical on round-trip. Parent visual review of `generic_counters_contact_sheet.png` accepted the three identities and both frame families for repository use. User live consumer validation remains outside this tranche.
