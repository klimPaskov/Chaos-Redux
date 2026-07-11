# System Camp Repression Rework Report and Super-Event Art Manifest

## Package status

This package contains 17 final, materially distinct raster identities:

- 12 report-event images: one Germany discovery image, six Japan/Pingfang images, and five Soviet famine/gulag images;
- five super-event images for visible slots `12`, `74`, `75`, `76`, and `77`.

Every identity has a generated source PNG, a processed PNG, a runtime DDS, a recorded built-in `imagegen` prompt, and a GFX handoff. All 17 stable sprite definitions currently exist in the shared working tree and resolve to the final DDS paths, so the assets have status `wired`. Those `.gfx` changes were parent-owned and were not edited by this asset pass. No gameplay, localisation, spreadsheet, music, sound, GUI, or `.gfx` file was edited by this asset pass.

There are no placeholders, fallbacks, sourced-photo substitutions, or missing images.

## Source mode and historical fit

Source mode is built-in `$imagegen` for every identity. Generation is appropriate because the requested scenes are fictional or composite event moments rather than photographs of a required real person, battle, or archive item. No image is presented as a genuine historical photograph.

The generated scenes use 1930s-1940s camera language, clothing, railway equipment, telephones, field cameras, office furniture, architecture, and documentary composition. All people are fictional and anonymous. No real leader likeness was requested or accepted.

The exact final prompt set is in `docs/assets/system_camp_repression_rework/prompts/report_super_event_imagegen_prompts.md`.

One earlier Pingfang super-event render was rejected because a building carried the readable number `731`. That result was never copied into the repository. The selected final source uses blank facades and contains no readable identifier.

## Processing workflow

- Source generation: built-in `imagegen`, one call per identity.
- Report cards: the verified Chaos Redux report processor at SHA-256 `5b51613f391934960a8310268041c66b00fdd31bc12da2393eb02c8f3dc87bd9` produced `210x176` RGBA cards with cover crop, black-and-white conversion, sepia, grain, deterministic tilt, transparent edge space, and soft shadow.
- Super-events: cover-cropped to `457x328`, autocontrasted, sharpened lightly, converted to monochrome, and given restrained period grain.
- DDS conversion: repository `.tools/convert_to_dds.py`, one mip, uncompressed 32-bit BGRA/B8G8R8A8-style masks.
- Reproducible processing and validation: `docs/assets/system_camp_repression_rework/tools/build_report_super_event_assets.py`.

## Germany report audit

The dedicated `GFX_report_event_auschwitz_discovery` identity is registered and consumed by `chaosx_genocide.56` in `events/genocide_crisis_events.txt`. That discovery event is the live Germany/Auschwitz evidence handoff. No second Germany-specific report identity is required by the accepted package.

## Report-event manifest

| Sprite ID | Related event / use | Visual identity | Source PNG | Processed PNG | Final DDS | Size | GFX target | Status |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| `GFX_report_event_auschwitz_discovery` | `chaosx_genocide.56`; Auschwitz evidence discovery | Investigators document an abandoned experiment-linked laboratory annex beside the rail spur. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_auschwitz_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_auschwitz_discovery.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_auschwitz_discovery.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_pingfang_authority` | `japan_ishii.1` | Medical bureau officers receive files and keys inside a remote administrative office. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_pingfang_authority_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_pingfang_authority.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_authority.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_kwantung_medical_bypass` | `japan_ishii.2` | A sealed medical dispatch changes hands inside a night railway communications office. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_kwantung_medical_bypass_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_kwantung_medical_bypass.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_kwantung_medical_bypass.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_pingfang_outbreak` | `japan_ishii.3` | Period medical staff close a rural railway perimeter after an outbreak escapes the compound. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_pingfang_outbreak_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_pingfang_outbreak.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_outbreak.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_pingfang_discovery` | `japan_ishii.4` | Investigators open a laboratory archive and photograph a central evidence table. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_pingfang_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_pingfang_discovery.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_discovery.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_pingfang_retreat` | `japan_ishii.5` | File crates, a burn barrel, trucks, and an open gate frame the retreat decision. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_pingfang_retreat_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_pingfang_retreat.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_retreat.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_pingfang_tribunal` | `japan_ishii.6` | A tribunal evidence room assembles records and covered laboratory material into one case. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_pingfang_tribunal_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_pingfang_tribunal.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_tribunal.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_soviet_famine_warning` | `soviet_gulag.1` | Empty reserve bins are inspected while loaded grain wagons depart outside. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_soviet_famine_warning_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_soviet_famine_warning.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_famine_warning.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_soviet_famine_crisis` | `soviet_gulag.2` | Villagers carry empty sacks toward a shuttered granary beside an idle train. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_soviet_famine_crisis_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_soviet_famine_crisis.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_famine_crisis.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_soviet_administrative_breakdown` | `soviet_gulag.3` | Rail officials argue over incompatible manifests while empty wagons stall beyond the window. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_soviet_administrative_breakdown_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_soviet_administrative_breakdown.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_administrative_breakdown.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_soviet_famine_relief` | `soviet_gulag.4` | Railway and relief workers unload grain sacks into handcarts at a remote siding. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_soviet_famine_relief_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_soviet_famine_relief.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_famine_relief.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |
| `GFX_report_event_soviet_records_discovered` | `soviet_gulag.5` | Local administrators, archivists, and observers compare the opened paper trail. | `docs/assets/system_camp_repression_rework/source/report_super_event/report_event_soviet_records_discovered_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/report_event_soviet_records_discovered.png` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_records_discovered.dds` | `210x176` | `interface/camp_repression_rework.gfx` | `wired` |

## Super-event manifest

| Slot | Stable sprite ID | Role and visual identity | Source PNG | Processed PNG | Final DDS | Size | GFX target | Status |
| ---: | --- | --- | --- | --- | --- | ---: | --- | --- |
| `12` | `GFX_super_event_angel_directorate` | Angel of Death Directorate revolt; a white-coated anonymous commander overlooks a seized laboratory compound, rail roadblocks, radios, and unmarked troops. | `docs/assets/system_camp_repression_rework/source/report_super_event/super_event_angel_of_death_directorate_revolt_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/super_event_angel_of_death_directorate_revolt.png` | `gfx/super_events/system_camp_repression_rework/super_event_angel_of_death_directorate_revolt.dds` | `457x328` | `interface/chaosx_super_events.gfx` | `wired` |
| `74` | `GFX_super_event_camp_global_discovery` | Severe global discovery; investigators hand evidence into a field press and teleprinter room. | `docs/assets/system_camp_repression_rework/source/report_super_event/super_event_global_discovery_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/super_event_global_discovery.png` | `gfx/super_events/system_camp_repression_rework/super_event_global_discovery.dds` | `457x328` | `interface/chaosx_super_events.gfx` | `wired` |
| `75` | `GFX_super_event_camp_soviet_famine_catastrophe` | Soviet famine catastrophe; an empty agricultural landscape, shuttered elevator, receding grain train, and sparse villagers. | `docs/assets/system_camp_repression_rework/source/report_super_event/super_event_soviet_famine_catastrophe_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/super_event_soviet_famine_catastrophe.png` | `gfx/super_events/system_camp_repression_rework/super_event_soviet_famine_catastrophe.dds` | `457x328` | `interface/chaosx_super_events.gfx` | `wired` |
| `76` | `GFX_super_event_camp_pingfang_exposure` | Pingfang exposure; witnesses and investigators carry crates from a blank-facade laboratory archive into press view. | `docs/assets/system_camp_repression_rework/source/report_super_event/super_event_pingfang_exposure_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/super_event_pingfang_exposure.png` | `gfx/super_events/system_camp_repression_rework/super_event_pingfang_exposure.dds` | `457x328` | `interface/chaosx_super_events.gfx` | `wired` |
| `77` | `GFX_super_event_camp_colonial_reckoning` | Colonial reckoning; local witnesses and investigators jointly open records at a tropical rail-and-warehouse depot. | `docs/assets/system_camp_repression_rework/source/report_super_event/super_event_colonial_reckoning_source.png` | `docs/assets/system_camp_repression_rework/processed/report_super_event/super_event_colonial_reckoning.png` | `gfx/super_events/system_camp_repression_rework/super_event_colonial_reckoning.dds` | `457x328` | `interface/chaosx_super_events.gfx` | `wired` |

## Checksums

| Asset stem | Source PNG SHA-256 | Final DDS SHA-256 |
| --- | --- | --- |
| `report_event_auschwitz_discovery` | `9f842a54bd8ba0c8e3958977b9977f035e5a99b60478e5aa09919b13900dff15` | `740ea2f7e37eec78599a9ce5a8a81bf75a166f2a51b6db4ce7d548ce4026b17f` |
| `report_event_pingfang_authority` | `4888feac7bb26c1933184b255c39425d50f1427c1bacdc08f96eb4a1e16c2190` | `03ba7243df437f22781205f792fce88e4fc30b809bcdc71c6f52ab6b77bc9513` |
| `report_event_kwantung_medical_bypass` | `d395fe314668107d85e2980c25f0d8fe6f2b4e822ac1259de4d82ada04752c5a` | `44ddffe51f0c18e3905c37de1571a5dba83c11148c7de9514ade7dc7801630de` |
| `report_event_pingfang_outbreak` | `5edcf2e93960a857a84d93df66fc942b75a2b240d115c50b8970ec6f01313e94` | `9c394e435b6557cd6768f0bb65fe3aafd44dffbd57264c1c6dbf788f3422fd5f` |
| `report_event_pingfang_discovery` | `bdf54a76e6c4ac9216b128996976f511379924a03bd8866ed01b600fe81b6c2c` | `6ab17009e2839c261e71b93232c541e5436ae1d3b34978609662b02f1386601c` |
| `report_event_pingfang_retreat` | `3c4ebce53ff23f767db676fab0afeff450f883ff8554d31934312cdcdd3dfc01` | `65e33662a16ff9932636494e6adfdaf68419150be88d005f867300d7bfe19bb4` |
| `report_event_pingfang_tribunal` | `54c53fd6f1bde2cc596065f9e742feee1339bb1c491c024c1f49440618e82f0b` | `6e3dca436c27670d27f411bad4b953236fe0c0ad8cdfa5cf170068f3bdf2c7f0` |
| `report_event_soviet_famine_warning` | `cf5984332f9454cf86a086db3a1c95bf66a1a2175df8ef90d7a2a84ba8c94ee4` | `b4fb502dd828063b9017d3dc08351080079b46ff126ddc799520b344c80468a8` |
| `report_event_soviet_famine_crisis` | `169959463599feb8a49044504668b92e4c9284bdd3f4034dbc509a67ac90db94` | `a899ef4757168b1a16e0f96efc688f31911dc25fe9b1a3be2ea0d2a5147d006c` |
| `report_event_soviet_administrative_breakdown` | `aa64a3f4f1df37b68bcb30014086d15460db45adc63ed150d8ca154d6667527e` | `30f09f67dc91977d316572bf845d8554ad2cd0d0665b5468e91b871f1448baad` |
| `report_event_soviet_famine_relief` | `fbaa6433f7f9efad0a8173bec738b4f9e2cb3e3351beae2a8cc34fb8cf5ec546` | `117ae5d4864c61e401a64e05ef128db6ba083348791694b6aae04827ddfd81b7` |
| `report_event_soviet_records_discovered` | `8024c580bc733f1a8a9ae3e6ba8cf82345fc34c71dff0a81ccf77a2639839b81` | `8091a2b3aafe20a9f4d1da4cb3d358ca2d5c1f7540842dc84c1e8de048c77f9d` |
| `super_event_angel_of_death_directorate_revolt` | `497d0ea2ad8532f0da01676030cc18491d3e3fa29fe52daf2669ad744fbebad7` | `cb7dbe1bc49a46eb975f6ce460c4f4579e534ad47d261eadf2d1d22c88532be0` |
| `super_event_global_discovery` | `e008ca2a2bbc60e3ff39c1cdc2bb6c8ede2fed61682eaf05ac117e3e8260f22c` | `e46598855ba8e36d2540306c49242ef24f9abb8ce0b4ecbf9b8b600c48ec61eb` |
| `super_event_soviet_famine_catastrophe` | `c24bf076d884d79f38a65630671747eced4f828fc6a7fc85a62c5aacc2a8e4d1` | `4fcdffcab8e8ee09013f8636d5d45271b5500028ef005390090a19e884c08eb7` |
| `super_event_pingfang_exposure` | `71b79654b687b9b823975db05509933bc5fc1c7ed4c1af1ed5f0d119e6346978` | `8892dc9b391ee0e0616aa66ba47b71bc588bb4c6eba40b4da45947215d63ec33` |
| `super_event_colonial_reckoning` | `492e8aa232082f03f9f8229e4aad7a42b00938a3699687cfb60f750e45e7ee59` | `137866ea38015d4fdd74fb829dffea3fcb100b775c011e5dee81c48705e85d90` |

## Review artifacts

- `docs/assets/system_camp_repression_rework/contact_sheets/report_super_event_source_contact_sheet.png`
- `docs/assets/system_camp_repression_rework/contact_sheets/report_event_processed_contact_sheet.png`
- `docs/assets/system_camp_repression_rework/contact_sheets/super_event_processed_contact_sheet.png`
- `docs/assets/system_camp_repression_rework/contact_sheets/super_event_ui_mask_preview_contact_sheet.png`
- five individual `super_event_*_ui_mask_preview.png` files in the same contact-sheet folder.

## Visual acceptance

The source, processed, and UI-mask sheets were reviewed at full resolution. The selected finals contain:

- no recognizable real individuals;
- no readable generated text;
- no swastikas, SS runes, rising-sun flags, or other prohibited insignia;
- no protected-class selector boards, lineups, or target imagery;
- no blood, bodies, human remains, graphic medical procedures, or graphic gore;
- no modern vehicles, screens, hazard suits, or UI overlays.

The scenes remain distinct after final cropping: office authority, railway bypass, quarantine perimeter, archive recovery, retreat logistics, tribunal evidence, granary warning, famine landscape, rail-office fracture, relief train, opened records, Auschwitz discovery, laboratory revolt, press-wire disclosure, wide famine catastrophe, exterior Pingfang exposure, and colonial records handover.

## Blockers and simplifications

None. No requested art was omitted, reused, or replaced with a weaker substitute. Parent wiring remains intentionally outside this asset-production scope.
