# Quaternion sign sweep of custom unit animations — 18 October 2026

The clone infantry arm repair (`models_1018_clone_handoff.md`) found serialized q/-q sign flips between consecutive quaternion samples in arm and leg channels.
A scan of every `.anim` under `gfx/models/units/` with the maintained `.tools/3d_pipeline/review/anim_signs.py` found the same defect in 28 further actions across 12 units.
Each file was replaced by that tool's output applied to the shipped bytes: whole four-component samples are negated so consecutive samples have a non-negative dot product, and no key, bone, translation, scale, or timing changes; the tool re-read every written file and reports zero remaining flips.
The Event 020 rat death action also has one flip; it was left to the running rat rebuild, which replaces that action.
The chaos assault battalion has no flips, so its reported animation problem has a different cause.
Removing the flips matters only if the in-game blend between keys does not take the shorter rotation by itself; this is the explanation favoured by the clone screenshot, not an observed result.

| File | Before SHA-256 | Installed SHA-256 |
|---|---|---|
| `gfx/models/units/018_resources_found_cave_monster/resources_found_cave_monster_death.anim` | `798370CBCA39F143B7778709AAB3454389340B367593FFCB50B336453AB0ED00` | `9545451EF23C065BA4AF30EB039BDAB5430140F3616504C3C6878603A80DB8F2` |
| `gfx/models/units/039_assassin_cadre/chaosx_assassin_cadre_death.anim` | `268D7A6A89A2F853424679CE481C03F2850F9BE210F54AA865B62EA65BF3F6B8` | `B7BFDD37C7704B9ABC7CC9513294B70907A49392D53C4798798EAB974FC1D255` |
| `gfx/models/units/039_assassin_cadre/chaosx_assassin_cadre_support_attack.anim` | `CECDC2E7169FD05124F2C27DD17B2DD7FD6B9ACB2827DE11C06DA2F6A9B887CD` | `B3D02EE7EBDADD034B45E74A481E8ADB220D94F7EDFA14C37AC1817BE45C0215` |
| `gfx/models/units/039_mechanized_assassin/chaosx_mechanized_assassin_move.anim` | `9611657B2A4F1916ACDA2446B2C4853A8419BC57FFC728FA98A09E4F5E9DF46F` | `338203913DA6BD35B29EC2EBF1DEDA68F74D33AAD12F8959FE9CE5D13BEC6E7D` |
| `gfx/models/units/039_mechanized_assassin/chaosx_mechanized_assassin_retreat.anim` | `FBDC3BEA8112C7D2603CBCB47582A4707E5E9F764BAD6210F1B1E17C72851957` | `D257847FF12642F33B58B8CA3BF2AAEABC52476E97939425775B4F6A9A3D0242` |
| `gfx/models/units/alien_infantry/alien_infantry_death.anim` | `D836BE94902AF5608B3FCC98BE8005B5A8EADA59E947B58930F43D8D66A2D7EB` | `78D2AEBDC906A5A2EA30558D70726860D107AA84CE3B89EB01F3E4B10D546951` |
| `gfx/models/units/alien_infantry/alien_infantry_move.anim` | `801C85CB1B4E6D581C633B11ABFDE3F06A713FDF4AB0C0DBFF2B6D82E4D0F03B` | `0142FCD638F72CD354D5D9C96E95C5652241730F28BE3D37FEFA9E5E36E3C5E6` |
| `gfx/models/units/alien_infantry/alien_infantry_retreat.anim` | `781CEDAA3AD5D9D32038275EEC64F0DD6D19C8456FBC41FE96A5E63A2C66B764` | `07770FBFEC5547FEF99AA1548042B17C7B4476A1A3D1C4F29E792779BF243BC0` |
| `gfx/models/units/autonomous_robot/autonomous_robot_attack.anim` | `12C5FBE5800B8A5EA3F76F2820B7EBC4EE22683F5612F4ED9374ECB9F3A3BC60` | `A69F2727DD19BED9FAC6BCC00F6CCC955B0D34F04FDFC81B1AB5FF41575C4DAC` |
| `gfx/models/units/autonomous_robot/autonomous_robot_death.anim` | `55906BDECD6E3EDB74EB08EA3F09B24087662C3C2131C74E426063D37A2669F4` | `ED6B5BB919A08843641A44AD4B36CAF4DFD697F3AEE6CBDB4B8A3B12C1E32E42` |
| `gfx/models/units/autonomous_robot/autonomous_robot_move.anim` | `C9D7B4A4B1DB3B96A8DB2B17068A5789CBC199CFA5D7FA56279DC2FEAD60B5CE` | `D023A67E4F579C6183CE898FE89FF06FDC55EEFA6C26740C91CE17DE6B281787` |
| `gfx/models/units/autonomous_robot/autonomous_robot_retreat.anim` | `4FA97B0724973B2E210B3A61971FB15FCE87BF05F70C7E101C701F23B3CCB604` | `FAC00DEFB86F56174B2885FC01EDBD7A0F7D5E3072228EC1C8B8900348ACAA9A` |
| `gfx/models/units/autonomous_robot/autonomous_robot_support_attack.anim` | `84C51469064726C10B4BEA0A8D55BCBBAA873D1805376A260D24806368D8C63F` | `61B7FF1090B02B4E3D3579DF90319C38F4BA8EBF9BBF3F0BBADB458AA3FE8817` |
| `gfx/models/units/autonomous_robot/autonomous_robot_training.anim` | `74F6555891D145CEA230D13512745410A6EC8A8BBFEBC60DED3D8C2A14DCCE46` | `EC1B664EC5DFC7207A1483C465CA77A634A058DB93E35A9E50A27D22FC08808D` |
| `gfx/models/units/death_ghost_hosts/death_ghost_hosts_attack.anim` | `68CA34DA0939B89FA177CC39389A57158FD0545230867F2887354FF6977D1C48` | `33A4500F21A7C330806305D0EC948AC0AB64F8097B9478EEA3F30E69D0279B9D` |
| `gfx/models/units/death_ghost_hosts/death_ghost_hosts_death.anim` | `86DA23E06401CB7627EADF22C3FD3CF732A50BF0F413781F29AB86AEC9DE6E9B` | `36CCBF2868B617CE905323F2C976A2A3C309E0B192AC87BFC0547A0A340FAA15` |
| `gfx/models/units/paleogenetic_creature/chaosx_paleogenetic_creature_attack.anim` | `E2C12ACA221E272E89B2206E3921A7C362D5986D67B7E50003C33A786112543F` | `BE8CDF46167A8088E1800A880CBDC4F2846813EEC2F7C2AA5D33B96B593B2943` |
| `gfx/models/units/paleogenetic_creature/chaosx_paleogenetic_creature_death.anim` | `C4AD3C0422A3D55B8B8673B6613378B7ADD3E14DB15083C5A86036E8FF691043` | `92D530A59DB6AF00459F0BA07F909832C4B5937FFAFA9E04E66B7049438C2079` |
| `gfx/models/units/paleogenetic_creature/chaosx_paleogenetic_creature_defend.anim` | `406122254762CB92A94E5B14465F44F81CC748E9B089C8E1B819C11D4E80F173` | `EEF001F4F6C244366D30FC74847013835508EB79FF7C6F7BD2628CCBC7B20371` |
| `gfx/models/units/paleogenetic_creature/chaosx_paleogenetic_creature_retreat.anim` | `D35C092F1B75B1E2555C91999D5E88B09CF67E81463175896A123CC5B6921AA9` | `EB9101E977622EB88256978169EF65C13FD1EF0F1D0B109D8112F2EB704F3B1E` |
| `gfx/models/units/portal_raider/portal_raider_move.anim` | `DB9293EF315D0B38D82C0B253F4371B13D76CC05A3DB2E55C76BB3A74152775F` | `425F92F69F68B3A9BB99A27A6086D07369C8CF50EE42F8B08860F9958E6F1601` |
| `gfx/models/units/temporal_guard/chaosx_temporal_guard_support_attack.anim` | `1E6390807EF7EBD5674F47C36121D9038F658B0F35FED1385D3CFE4F4BFCB74F` | `8456882515EB47A38C7F82B1E8BE5CE0C0494A94E7DFE50D99B4CDF9267BB3EB` |
| `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_attack.anim` | `0014222D058CE0AA82005F4275B3B792738E30B54B24CFE4BFFB682071A0E541` | `EAC44495E2CCEB28884C9610B3EEEF0FFA6F6DD6A600B6792431E4FAA0587DBB` |
| `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_death.anim` | `79BD1FB67658527C2BD907F63E937D6CF7DB41F60E3B1359A360D1760C43E681` | `0B222712B39B58E666FBC71DDF30C3850161172060AE6254C83622B343D1377D` |
| `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_defend.anim` | `F6686A6E74A92B3B6791F566F4EEE94EF4C2CD77426E4F15C2C302677A931BEF` | `03836E16FFF23893E079C06DAEAC1C3000833F7C2AD1C5F7D4CDCE93500918D2` |
| `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_idle.anim` | `22869AE9C47066C27DF129E37311E2EB4EB72E2890C3D022A8D8FD616F4DD6FE` | `9B281B22F6308A9A4A0380019EEC1E31A256F850DBA1942CBFEDF9B72574B1EF` |
| `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_move.anim` | `ECC8970C333DC467616C289A54FF88AC2AC53DE0CEC7B6853C6D09326120DEE5` | `D2128E7B6ABA9F7B37DF553338697E1C3BBDECC563998BC6D77E0C1D1EBFA348` |
| `gfx/models/units/xenobiological_assault_organism/xenobiological_assault_organism_support_attack.anim` | `177AF3EE8C759A6A5451B31C4D7B2F8B0EAC433F70ECC377E6A177B2FF44EA3A` | `2E65A7907C6E652AE4D2902A1E79DAC1376383941BF0FC0590D415FCF0A9814F` |
