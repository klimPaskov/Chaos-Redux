# Event 014 Cannibalism decision-cost texticons

This package supplies the seven distinct semantic icons used by Event 014 decision cost text: Larder Stores, consumed state population, Victory Receipt, Convoy-Hunt Receipt, Enemy-Loss Receipt, small airframes, and transport aircraft.

The package is asset-complete and intentionally does not edit Event 014 decisions, gameplay, or GUI files. Event 014 localisation consumes the `£` tokens listed below wherever the corresponding cost ledger is shown; the parent owner retains the gameplay binding.

## Reference audit

- Closest canonical style review: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/modifiers/contact_sheet.png`.
- The canonical skill reference root contains no dedicated texticon contact sheet or texticon family, so the installed vanilla consumer contract was inspected directly in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/texticons.gfx` and `gfx/texticons/*.dds`.
- The installed vanilla texticons use single-frame uncompressed BGRA8 DDS assets with real alpha; the common regular family includes 18x18 assets, and the existing Famine custom Deaths texticons establish the repository-specific 18x18 texticon precedent.
- The source art was generated with native transparent backgrounds and contains no people, gore, flags, religious symbols, sacred motifs, or ethnographic claims.

## Runtime inventory

| Semantic ledger | Localisation token | GFX sprite token | Runtime DDS | Source canvas | Final canvas | Alpha and DDS format |
| --- | --- | --- | --- | --- | --- | --- |
| Larder Stores | `£cannibalism_larder_texticon` | `GFX_cannibalism_larder_texticon` | `gfx/texticons/014_cannibalism/cannibalism_larder_texticon.dds` | 1254x1254 RGBA PNG | 18x18 RGBA PNG and 18x18 BGRA8 DDS | Native alpha, uncompressed BGRA8, one mip level, 1424 bytes |
| Consumed state population | `£cannibalism_state_population_texticon` | `GFX_cannibalism_state_population_texticon` | `gfx/texticons/014_cannibalism/cannibalism_state_population_texticon.dds` | 1254x1254 RGBA PNG | 18x18 RGBA PNG and 18x18 BGRA8 DDS | Native alpha, uncompressed BGRA8, one mip level, 1424 bytes |
| Victory Receipt | `£cannibalism_victory_receipt_texticon` | `GFX_cannibalism_victory_receipt_texticon` | `gfx/texticons/014_cannibalism/cannibalism_victory_receipt_texticon.dds` | 1254x1254 RGBA PNG | 18x18 RGBA PNG and 18x18 BGRA8 DDS | Native alpha, uncompressed BGRA8, one mip level, 1424 bytes |
| Convoy-Hunt Receipt | `£cannibalism_convoy_hunt_receipt_texticon` | `GFX_cannibalism_convoy_hunt_receipt_texticon` | `gfx/texticons/014_cannibalism/cannibalism_convoy_hunt_receipt_texticon.dds` | 1254x1254 RGBA PNG | 18x18 RGBA PNG and 18x18 BGRA8 DDS | Native alpha, uncompressed BGRA8, one mip level, 1424 bytes |
| Enemy-Loss Receipt | `£cannibalism_enemy_loss_receipt_texticon` | `GFX_cannibalism_enemy_loss_receipt_texticon` | `gfx/texticons/014_cannibalism/cannibalism_enemy_loss_receipt_texticon.dds` | 1254x1254 RGBA PNG | 18x18 RGBA PNG and 18x18 BGRA8 DDS | Native alpha, uncompressed BGRA8, one mip level, 1424 bytes |
| Small airframes | `£cannibalism_airframe_texticon` | `GFX_cannibalism_airframe_texticon` | `gfx/texticons/014_cannibalism/cannibalism_airframe_texticon.dds` | 1254x1254 RGBA PNG | 18x18 RGBA PNG and 18x18 BGRA8 DDS | Native alpha, uncompressed BGRA8, one mip level, 1424 bytes |
| Transport aircraft | `£cannibalism_transport_aircraft_texticon` | `GFX_cannibalism_transport_aircraft_texticon` | `gfx/texticons/014_cannibalism/cannibalism_transport_aircraft_texticon.dds` | 1254x1254 RGBA PNG | 18x18 RGBA PNG and 18x18 BGRA8 DDS | Native alpha, uncompressed BGRA8, one mip level, 1424 bytes |

## Artifact paths

- Native generated sources: `source_png/*_source.png`.
- Exact-size processed previews: `processed_png/*.png`.
- DDS decode evidence: `roundtrip_png/*_roundtrip.png`.
- Review sheet: `contact_sheets/cost_texticons_contact.png`.
- Aircraft review sheet: `contact_sheets/aircraft_cost_texticons_contact.png`.
- Generation prompts and native ImageGen provenance: `prompts/generation_prompts.md`.
- Aircraft-specific alpha, dimensions, hashes, and DDS round-trip record: `validation/aircraft_texticons_validation.json`.
- GFX registration: `interface/014_cannibalism_texticons.gfx`.

## SHA-256 inventory

| Name | Source PNG | Processed PNG | Final DDS |
| --- | --- | --- | --- |
| `cannibalism_larder_texticon` | `eeb5aaf05c6914772fb6d87ab200fc928a8acfa1243f73c65b51720249b747da` | `980895a98ded8d15caa1778fafd06fb294d93700b161cf7595e8cdbe1b65389a` | `a7b16ef82fec685f56cf81ab8966dfdf4d4149e800b3fe256491eead8544f267` |
| `cannibalism_state_population_texticon` | `14ff6f64be0ec607dd00f020164ad7700b149cf94f35c3e263a71e6af240080c` | `b9a38b2e2925b81cbb984023b78d2c368bb277b7e9d2076fd012abd76d69836a` | `821e0a7d57d88f8e06eeb5175ea35dbf3dbc6e56112f40fb3a525aee570d84d9` |
| `cannibalism_victory_receipt_texticon` | `d8c67c3a60b97870c9bc1a12756bf596ad4ece4cceb893045a9ba939dd493424` | `e582800aea5b1ab68a25f69a824531eddf80f873017f0183f8795b79b71b0ef0` | `5e57714b45b88049f4ee07348bafc2eedc3bf09567ec9c4182efef3abe006d0d` |
| `cannibalism_convoy_hunt_receipt_texticon` | `9527483b3bc4f341bd6df137b9dba8dffda8fa51a0c6f007622b1f2c116e6828` | `24c5b8a06c40143cffcc47a69252538ceac0efe903ad6487780a6f080adaf4d5` | `63a610dd8c40a7a9455e45cd8f5014bb04c009e7896fbab427ec2638443fc3b8` |
| `cannibalism_enemy_loss_receipt_texticon` | `0b93d70559f89e03ee0a44840f1dc6c811ebaf163e7f165b4ee7859d831f40ee` | `62221d1ad4b2d04c871af853c45b5e29ae1a3adcccb41afca43fe0bfe2951db2` | `5b80325229fbb8185fcb4883e39573f45983c608c758c5403462ce5d02e979c7` |
| `cannibalism_airframe_texticon` | `ba701b24155a69aa0dd17fe900185bcbee09af63ed68d255475a45cb8753bbc1` | `e959ebbde8251bbcae4552f8852b07fe52b8601d5e33907637428c7195338679` | `b0a850cd356fc44ceb56fad4bf43e6fc00e06cdc64f94adc215903c6330ad987` |
| `cannibalism_transport_aircraft_texticon` | `1a0cef5e0af68b37d00f7c800f288af83ca47629d2860feb5a902e0a4df717b2` | `5b1dcde8121bcb35145e3d3998530ff111dcfd260a4ac62493a874c3142887b0` | `9152c30bb07826492a909fcc128710bcd1084cf11b5639ce9da2ea48a5166807` |

The contact-sheet SHA-256 is recorded in `gfx_handoff.md` after the final review-sheet build.
