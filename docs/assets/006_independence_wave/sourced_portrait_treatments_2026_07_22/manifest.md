# Event 006 sourced leader-portrait treatments

Date: 2026-07-22
Processor: `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` v5.0, `leader` mode
Reference family: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`

This package converts attributed archival portraits into identity-preserving
156x210 HOI4 leader textures. It does not use ImageGen, face reconstruction,
generic portraits, generated institutions, or fictional substitutes. Source
masters and rights evidence remain in the adjacent
`sourced_portrait_replacements_2026_07_22/` research packages.

No Event 006 advisor, theorist, high-command, officer-corps, or dossier portrait
is required. The obsolete `_small` dossier files and their consumers were
removed rather than regenerated. Commanders use their full 156x210 portrait.

The review-only contact sheet is
`contact_sheets/processed_sourced_portraits_contact_sheet.png` (SHA-256
`9a778c245221acac7b2859d98555ce13fb046a7cf65aa2244ba0b9a583040bb2`).
It displays all twenty-four source- and visually reviewed treatments at native
portrait aspect and is never referenced by runtime GFX. Twenty-one treatments
currently pass the separate vanilla-character ownership gate. Three retained
treatments (Konrad Adenauer, Franz Ritter von Epp, and Edmund Ironside) fail that
gate because vanilla recruits the same people as active characters; they remain
rejected evidence pending different sourced replacements.

## Treatment ledger

| Subject | Grounded role and source authority | Crop | Processed candidate | Runtime DDS | Status |
|---|---|---:|---|---|---|
| Arthur Quiller-Couch | Cornish civic leader; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `0,0,493,643` | `processed_png/ACX_arthur_quiller_couch.png` | `portrait_ACX_cornish_port_and_mines_committee.dds` | `processed_readiness_only`; IW-003 has no admitted adapter |
| Richard Fortescue Phillimore | Cornish coastal commander; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `145,25,435,415` | `processed_png/ACX_richard_phillimore.png` | `portrait_ACX_cornish_coastal_commander.dds` | `processed_readiness_only`; IW-003 has no admitted adapter |
| Saunders Lewis | Welsh civic-national leader; [western retry ledger](../sourced_portrait_replacements_2026_07_22/western_gap_retry/manifest.md) | `140,140,880,1135` | `processed_png/WLS_saunders_lewis.png` | `portrait_WLS_independence_wave_national_council.dds` | `processed_wired`; authentic 1916 image of Lewis; IW-002 remains fail-closed because its commander is unresolved |
| Douwe Kalma | Frisian civic leader; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `70,40,470,580` | `processed_png/AGX_douwe_kalma.png` | `portrait_AGX_friesland_coastal_council.dds` | `processed_wired`; IW-007 remains fail-closed pending its complete package audit |
| Pieter Reenalda | Frisian coastal commander; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `350,100,930,880` | `processed_png/AGX_pieter_reenalda.png` | `portrait_AGX_friesland_coastal_commander.dds` | `processed_wired`; command role is maritime/coastal, not an invented army identity |
| Konrad Adenauer | Rhenish civic leader; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `0,0,484,650` | `processed_png/RHI_konrad_adenauer.png` | `portrait_RHI_independence_wave_provisional_directorate.dds` | `rejected_active_vanilla_character`; vanilla defines `GER_konrad_adenauer` and recruits him for GER at game start; IW-008 requires a different sourced male civic identity |
| Josef Harpe | Rhenish-Westphalian army commander; [western retry ledger](../sourced_portrait_replacements_2026_07_22/western_gap_retry/manifest.md) | `0,0,4637,6242` | `processed_png/RHI_josef_harpe.png` | `portrait_RHI_independence_wave_river_commandant.dds` | `processed_wired`; Bundesarchiv source, Buer regional connection, and 1943 source date remain explicit; IW-008 requires a full package audit before any re-admission |
| Heinrich Held | Bavarian civic leader; [western retry ledger](../sourced_portrait_replacements_2026_07_22/western_gap_retry/manifest.md) | `400,160,2070,2409` | `processed_png/BAY_heinrich_held.png` | `portrait_BAY_independence_wave_state_council.dds` | `processed_wired`; former Bavarian minister-president; archive watermark excluded by the approved crop; IW-009 requires a full package audit before any re-admission |
| Franz Ritter von Epp | Bavarian military and emergency-route leader; [western retry ledger](../sourced_portrait_replacements_2026_07_22/western_gap_retry/manifest.md) | `600,350,2900,3447` | `processed_png/BAY_franz_von_epp.png` | `portrait_BAY_independence_wave_mountain_commandant.dds` | `rejected_active_vanilla_character`; vanilla defines `GER_franz_ritter_von_epp` and recruits him for GER at game start; IW-009 requires a different sourced male military identity |
| Adolphe Landry | Corsican civic leader; [Mediterranean source ledger](../sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md) | `36,0,476,592` | `processed_png/COR_adolphe_landry.png` | `portrait_COR_independence_wave_adolphe_landry.dds` | `processed_wired`; replaces the fictional Petru Santucci identity; IW-017 still requires a fresh full-package audit before any re-admission |
| Jean Chiappe | Corsican security commander; [Mediterranean source ledger](../sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md) | `560,120,860,524` | `processed_png/COR_jean_chiappe.png` | `portrait_COR_independence_wave_jean_chiappe.dds` | `processed_wired`; replaces the fictional Pasquale Venturi identity; crop tightened to head and shoulders |
| Emilio Lussu | Sardinian civic leader and veteran; [Mediterranean source ledger](../sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md) | `175,20,710,740` | `processed_png/ARX_emilio_lussu.png` | `portrait_ARX_independence_wave_emilio_lussu.dds` | `processed_wired`; replaces the fictional Antioco Melis identity; crop tightened to head and shoulders |
| Luigi Sturzo | Sicilian civic leader; [Mediterranean source ledger](../sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md) | `520,330,1170,1205` | `processed_png/ASX_luigi_sturzo.png` | `portrait_ASX_independence_wave_luigi_sturzo.dds` | `processed_wired`; replaces the fictional Sebastiano Restivo identity |
| Pietro Lanza di Scalea | Sicilian dynastic leader; [Mediterranean source ledger](../sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md) | `155,15,495,473` | `processed_png/ASX_pietro_lanza_di_scalea.png` | `portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` | `processed_wired`; replaces the fictional Vincenzo Lanza identity |
| Luigi Rizzo | Sicilian straits-security commander; [Mediterranean/Eurasia retry ledger](../sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/manifest.md) | `70,0,333,354` | `processed_png/ASX_luigi_rizzo.png` | `portrait_ASX_independence_wave_luigi_rizzo.dds` | `processed_wired`; replaces the fictional Salvatore Licata identity with a 1935 portrait of a Sicilian-born serving admiral |
| Gallo Shabo | Assyrian civic leader; [Assyria source ledger](../sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md) | `45,0,1045,1346` | `processed_png/ASY_gallo_shabo.png` | `portrait_ASY_independence_wave_provisional_national_council.dds` | `processed_wired`; IW-058 remains fail-closed because its other route identities are unresolved |
| Mirsaid Sultan-Galiev | Middle Volga congress leader; [Volga source ledger](../sourced_portrait_replacements_2026_07_22/mediterranean_volga_assyria/manifest.md) | `100,0,1140,1400` | `processed_png/CHU_mirsaid_sultan_galiev.png` | `portrait_CHU_independence_wave_middle_volga_congress.dds` | `processed_wired`; IW-043 remains fail-closed because three route leaders are unresolved |
| Galimzhan Ibrahimov | Middle Volga federal-presidium leader; [Mediterranean/Eurasia retry ledger](../sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/manifest.md) | `60,40,800,1036` | `processed_png/CHU_galimzhan_ibrahimov.png` | `portrait_CHU_independence_wave_federal_presidium.dds` | `processed_wired`; source is public-domain and the Commons upload-history Photoshop note is retained as a provenance caveat; IW-043 remains fail-closed because two other route identities are unresolved |
| Staf De Clercq | Flemish political leader; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `0,0,335,451` | `processed_png/AEX_staf_de_clercq.png` | `portrait_AEX_flemish_civil_industrial_board.dds` | `processed_readiness_only`; IW-005 has no admitted standalone adapter and the historical route caveat remains documented |
| Joris Van Severen | Flemish movement and paramilitary leader; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `0,70,590,864` | `processed_png/AEX_joris_van_severen.png` | `portrait_AEX_flemish_industrial_security_commander.dds` | `processed_readiness_only`; IW-005 has no admitted standalone adapter and the historical route caveat remains documented |
| Jules Destrée | Walloon civic leader; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `0,8,891,1208` | `processed_png/AFX_jules_destree.png` | `portrait_AFX_walloon_provisional_assembly.dds` | `processed_wired`; IW-006 remains fail-closed because its commander is unresolved |
| R. B. Cunninghame Graham | Scottish civic leader; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `1250,720,2750,2740` | `processed_png/SCO_cunninghame_graham.png` | `portrait_SCO_independence_wave_civic_convention.dds` | `processed_wired`; archived portrait predates 1936 and the source date is retained in the ledger |
| Edmund Ironside | Scottish territorial commander; [NWE source ledger](../sourced_portrait_replacements_2026_07_22/northwestern_europe/manifest.md) | `430,140,800,638` | `processed_png/SCO_edmund_ironside.png` | `portrait_SCO_independence_wave_territorial_commandant.dds` | `rejected_active_vanilla_character`; vanilla defines `ENG_edmund_ironside` and recruits him for ENG at game start; IW-001 requires a different sourced male commander |
| Muhammadu Dikko | Sokoto/Katsina mounted commander; [Pacific/Sokoto source handoff](../../plans/006_independence_wave_plans/subagent_handoffs/006_event6_pacific_asante_sokoto_sourced_portrait_research_2026_07_22.md) | `705,380,870,602` | `processed_png/SOK_muhammad_dikko.png` | `portrait_SOK_muhammad_dikko.dds` | `processed_wired`; replaces fictional Umaru Gwadabawa; crop tightened to head and shoulders; IW-098 remains fail-closed because Bello, Hasan, and Siddiq are unresolved |
| Naum Faiq | Assyrian civic-national legacy candidate; [Mediterranean/Eurasia retry ledger](../sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/manifest.md) | `10,0,456,600` | `processed_png/ASY_naum_faiq.png` | none | `rejected_subject_timing`; source and treatment are defensible, but Faiq died in 1930 and cannot be presented as a living 1936 officeholder |
| Agha Petros | Assyrian levies legacy candidate; [Mediterranean/Eurasia retry ledger](../sourced_portrait_replacements_2026_07_22/med_eurasia_gap_retry/manifest.md) | `120,30,710,824` | `processed_png/ASY_agha_petros.png` | none | `rejected_subject_timing`; source and treatment are defensible, but Petros died in 1932 and cannot be presented as a living 1936 commander |
| David Kalakaua Kawananakoa | Hawaiian leader; [Pacific source handoff](../../plans/006_independence_wave_plans/subagent_handoffs/006_event6_pacific_asante_sokoto_sourced_portrait_research_2026_07_22.md) | `245,170,945,1112` | `processed_png/HAW_david_kalakaua_kawananakoa.png` | none | `rejected_source_quality`; clipped highlights do not survive an identity-preserving HOI4 finish |

## Runtime hashes

| DDS | SHA-256 |
|---|---|
| `portrait_ACX_cornish_port_and_mines_committee.dds` | `7e17cde267d9306495d7d879a0d623b118c70eca5fd66ddcd1c27092d2ad96ba` |
| `portrait_ACX_cornish_coastal_commander.dds` | `b6b84c64e16c6112ff117300b6271a3e50e239acc663cf5fc7c7641673ed50e6` |
| `portrait_AEX_flemish_civil_industrial_board.dds` | `918efe9de7804567ec9dd130ad855d81ed32171cf7a0e4e4a6cf27cf19283153` |
| `portrait_AEX_flemish_industrial_security_commander.dds` | `8fe59ea0b1b7c7d5b2f556a016aabf0c52a00f8260d3af8840e93c7ac90564ee` |
| `portrait_AFX_walloon_provisional_assembly.dds` | `3bf60a4fbb7904e300c31ea0e0ce3741813bfe54089eee88bbf7e592211d3565` |
| `portrait_AGX_friesland_coastal_council.dds` | `9194cba1cc5da0ec941f76c1938d7b016cc8a9bb2252bd4437e1e5109b6dedec` |
| `portrait_AGX_friesland_coastal_commander.dds` | `de21c5c8c7ca5639aa82cdfbb9c4a8ad53b192c7d16895e4d5d136114e3b7444` |
| `portrait_RHI_independence_wave_provisional_directorate.dds` | `06c40e7d557cf7e5bfd719c2a576e15d86a435b8ea9757f1f91620bf0e61ac64` |
| `portrait_RHI_independence_wave_river_commandant.dds` | `33dcc5595610ac7069e01d6c7c2515657c1fd93d921e55fe8b3707b7914f0d1a` |
| `portrait_BAY_independence_wave_state_council.dds` | `c371f76669afbc23e80d862ae8a97f20e6e15b89b4546667ecdb62134cdee035` |
| `portrait_BAY_independence_wave_mountain_commandant.dds` | `e1b37c14e058cceb7c96280bce14acc809c9c6d9f572627171c28f4a48de7ec6` |
| `portrait_COR_independence_wave_adolphe_landry.dds` | `c76b8f66aad39b90288bf216f388d642c7297f4a4e4701b223c378bda7d9b523` |
| `portrait_COR_independence_wave_jean_chiappe.dds` | `83014381e587873b461d8cd71c0d6ba958364a54085d17a157c6ee40c4e6de79` |
| `portrait_ARX_independence_wave_emilio_lussu.dds` | `92c4e49dd66d083f27fb455fa0dc2fa09949e8d40bdc2d7473aa6b957e99d445` |
| `portrait_ASX_independence_wave_luigi_sturzo.dds` | `bdd4fe08090a8dd3a2ac464add432dc3a4c60d1f7fa0dcd5d834bfea511e67c0` |
| `portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` | `a067f230ef233e5c6314959f9f0904e6d5c036f2d284bef9a44d6eb2a5a3be01` |
| `portrait_ASX_independence_wave_luigi_rizzo.dds` | `2348b811cc46f2ff8d7cbb0a7d0a66865205cd57d526903cbc159ae1aaa9dea5` |
| `portrait_ASY_independence_wave_provisional_national_council.dds` | `129fc2c576c57871ebaba5e715af35b4a1d50a4d655cd93e0eeb1e9e79cc1f43` |
| `portrait_CHU_independence_wave_middle_volga_congress.dds` | `23a328a3224236cc6d35cc180ef6d90c3ddfd59f5d33271b1e29633ac3c152e5` |
| `portrait_CHU_independence_wave_federal_presidium.dds` | `6370964c0bf62d13afa30d404f45fb44650256abbbf4b885e8370d67cfa93283` |
| `portrait_SCO_independence_wave_civic_convention.dds` | `d2fa024af32069dd83aedc13190772fb0c02cccf0947af83c4a1317767cc245b` |
| `portrait_SCO_independence_wave_territorial_commandant.dds` | `04d0ed792885b6149ec0eb5257e906b69279dd57cf52ead32d0f68b9230e8eaf` |
| `portrait_WLS_independence_wave_national_council.dds` | `12ca49ed34c4d84b4135e580baa1c36994dc391baade62d02dbd80e1fd1fed05` |
| `portrait_SOK_muhammad_dikko.dds` | `facfe7ca0547cc4898061fa387faab61fc138e92f228f43469a8a7473402f7c3` |

Every listed DDS decodes as RGBA `156x210` and is pixel-identical to its
processed PNG. Pixel equality proves conversion fidelity only; it does not
override the active-character ownership rejection for Adenauer, Epp, or
Ironside. Protected BAY Rupprecht and RHI Matthes retained their approved hashes
unchanged.

## Admission boundary

This is a portrait replacement tranche, not package admission. The compile-time
Event 006 content-attestation set remains empty. A package may be restored only
after every leader, route leader, commander, and named officeholder in that
package satisfies the sourced-real-person gate, the subject is not already owned
as an active vanilla or Chaos Redux character, and the package is re-audited.
