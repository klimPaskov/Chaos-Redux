# Event 19 Claimant Identity Metadata

The twenty gameplay claimant characters remain wholly fictional men with male-default leader metadata and regional male name pools. Their fixed `GFX_portrait_*` slots now display the claimant army or muster as a collective identity scene; no slot depicts the named character or any individual focal human/person. Working names are implementation metadata, are not embedded in the images, and remain locked to the listed regional profile contracts.

| Slot | Working personal name | Gameplay metadata | Required name pool | Primary / secondary archetype | Fixed army/muster scene | Portrait sprite |
| ---: | --- | --- | --- | --- | --- | --- |
| 01 | Erik Vinterdal | male-default leader | Northern/Western European male | Quartermaster Sovereign / Hollow Marshal | European railhead logistics muster | `GFX_portrait_infantry_spawn_claimant_01` |
| 02 | Milan Vargov | male-default leader | Central/Eastern European male | Quartermaster Sovereign / Barracks Tribune | frozen European river bridgehead | `GFX_portrait_infantry_spawn_claimant_02` |
| 03 | Faris al-Mazhar | male-default leader | Middle Eastern/North African male | Quartermaster Sovereign / Iron Saint | oasis-fort defensive ring | `GFX_portrait_infantry_spawn_claimant_03` |
| 04 | Dev Suryapala | male-default leader | South/Southeast Asian male, Asia and Australasia diaspora-compatible | Quartermaster Sovereign / Field Prophet | monsoon port-and-rail fan | `GFX_portrait_infantry_spawn_claimant_04` |
| 05 | Arkady Zorenko | male-default leader | Eastern European/Eurasian steppe male | Field Prophet / Iron Saint | winter horse-artillery arrowhead | `GFX_portrait_infantry_spawn_claimant_05` |
| 06 | Anil Senaviratne | male-default leader | South Asian male | Field Prophet / Barracks Tribune | monsoon floodplain crossing | `GFX_portrait_infantry_spawn_claimant_06` |
| 07 | Tadashi Morioka | male-default leader | East Asian male | Field Prophet / Hollow Marshal | snowy forest infiltration echelons | `GFX_portrait_infantry_spawn_claimant_07` |
| 08 | Lucio Valcarcel | male-default leader | Latin American male | Field Prophet / Quartermaster Sovereign | highland pack-artillery chevron | `GFX_portrait_infantry_spawn_claimant_08` |
| 09 | Lucien Vautrin | male-default leader | Western European or North American male | Barracks Tribune / Quartermaster Sovereign | industrial tram-square front | `GFX_portrait_infantry_spawn_claimant_09` |
| 10 | Nikolai Karsky | male-default leader | Eastern European male | Barracks Tribune / Field Prophet | winter industrial artillery grid | `GFX_portrait_infantry_spawn_claimant_10` |
| 11 | Samir Qazwini | male-default leader | Middle Eastern/Central Asian male | Barracks Tribune / Iron Saint | plateau-canyon shield formation | `GFX_portrait_infantry_spawn_claimant_11` |
| 12 | Minh Tran Vinh | male-default leader | East/Southeast Asian male, Asia and Australasia diaspora-compatible | Barracks Tribune / Hollow Marshal | amphibious wavefront | `GFX_portrait_infantry_spawn_claimant_12` |
| 13 | Matteo Vellani | male-default leader | Southern European/Mediterranean or South American male | Iron Saint / Field Prophet | symbol-free coastal-cliff artillery zigzag | `GFX_portrait_infantry_spawn_claimant_13` |
| 14 | Klaus Weissen | male-default leader | Central European male | Iron Saint / Quartermaster Sovereign | machineworks checkerboard blocks | `GFX_portrait_infantry_spawn_claimant_14` |
| 15 | Jabari N'Doye | male-default leader | Sub-Saharan African male | Iron Saint / Barracks Tribune | storm-savanna mobile echelon | `GFX_portrait_infantry_spawn_claimant_15` |
| 16 | Layth al-Hadri | male-default leader | Middle Eastern/North African male | Iron Saint / Hollow Marshal | desert mobile crescent | `GFX_portrait_infantry_spawn_claimant_16` |
| 17 | Shunpei Arakida | male-default leader | East Asian male | Hollow Marshal / Quartermaster Sovereign | blackout bicycle street grid | `GFX_portrait_infantry_spawn_claimant_17` |
| 18 | Ingvar Solhavn | male-default leader | Northern European male | Hollow Marshal / Field Prophet | frozen-fjord ski envelopment | `GFX_portrait_infantry_spawn_claimant_18` |
| 19 | Elias Mercer | male-default leader | Americas male | Hollow Marshal / Barracks Tribune | hurricane-delta levee zigzag | `GFX_portrait_infantry_spawn_claimant_19` |
| 20 | Marcus Voss | male-default leader | Australasian male, Australia-only runtime profile | Hollow Marshal / Iron Saint | outback motor hook | `GFX_portrait_infantry_spawn_claimant_20` |

## Derivative institutional identities

The six derivative gameplay roles keep their existing names and technical portrait sprites. Their visible art is exclusively massed-host identity imagery. Commander-labelled slots express command through one collective formation; council-labelled slots express governance through exactly three massed formations. None shows an individual commander, councillor, person, face, bust, or anthropomorphic focal subject.

| Derivative gameplay identity | Fixed host-scene contract | Composition contract | Portrait sprite |
| --- | --- | --- | --- |
| Zombie Host Commander | massed undead army wall | one broad collective host; no focal corpse | `GFX_portrait_infantry_spawn_zombie_host_commander` |
| Zombie Host Council | three undead legion masses | one central legion mass plus exactly two recessed flanking masses | `GFX_portrait_infantry_spawn_zombie_host_council` |
| Ghost Host Commander | massed spectral spearhead | one collective wedge of vaporous ranks; no central spirit | `GFX_portrait_infantry_spawn_ghost_host_commander` |
| Ghost Host Council | three genderless spectral army formations | one empty-centered ring plus exactly two recessed crescent hosts | `GFX_portrait_infantry_spawn_ghost_host_council` |
| Golem Master Builder | collective quarry builder-host | many coal-and-basalt golems across stepped stoneworks; no master figure | `GFX_portrait_infantry_spawn_golem_master_builder` |
| Golem Pattern Council | three geological cohorts | one central basalt triangular mass plus exactly two recessed coal and ironstone/granite masses | `GFX_portrait_infantry_spawn_golem_pattern_council` |

The gameplay pool contains exactly twenty male claimant profiles. Every profile owns four regional male localisation variants. The working personal name is the primary variant; the other three remain bound to the same sprite, region gate, male metadata, and archetype profile. Profiles 04 and 12 intentionally cover both Asia and the corresponding Australasian diaspora. Profile 20 remains restricted to Australia. Selection is fail-closed when no unused region-compatible profile exists. There is no global, catch-all, or regionally mismatched fallback.

All final identity scenes are static 156x210 assets. Claimant-state animation belongs to the separate critical command border. The exact source-to-runtime record is in `claimant_portrait_asset_crosswalk_2026_07_16.md`; retained reproduction specifications and built-in ImageGen provenance are in `../prompts/claimant_portrait_reproduction_specs_2026_07_16.md`.
