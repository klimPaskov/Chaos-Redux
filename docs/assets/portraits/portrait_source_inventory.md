# Portrait source inventory

Audit date: 2026-08-02.

Scope: every DDS under `gfx/leaders/` was treated as a current mod portrait asset, including leader, commander, institutional, advisor, scientist, small-card, and animated-sheet variants.

Original-resolution PNG found and archived by exact runtime basename: 175 of 296.

Additional original-resolution PNG recoveries from the second-pass search: 30.

No acceptable original-resolution PNG found; final runtime DDS converted losslessly to PNG: 121.

Every one of the 296 runtime portraits now has a matching PNG and prompt-only TXT file using the exact runtime DDS basename. Original sources were preferred over runtime conversions. Runtime-sized processed PNGs, older DDS-decoded source frames, contact sheets, rejected candidates, superseded candidates, and identity-preserving repaints whose real source existed only in another format were not mislabeled as originals.

Final verification: all 296 runtime DDS basenames resolve to exactly one archived PNG and exactly one single-line `hoi4_portrait,` TXT prompt. All 121 DDS-derived PNG fallbacks were decoded independently and matched their runtime DDS pixel data exactly.

# Additional original-resolution PNGs recovered

## 003_holy_realm (12)

- Eight static portrait masters recovered from the discarded `360d` Codex worktree's generated source package.
- The Buddha Mandate static and animated entries use the first original full-resolution animation source frame.
- The Empty Seat static and animated entries use the first original full-resolution animation source frame.

## 005_soviet_collapse (5)

- `BEC_leader.png`
- `BLT_leader.png`
- `COU_leader.png`
- `ILU_leader.png`
- `IRA_leader.png`

These five generated portrait masters were restored directly from reachable Git blobs.

## 006_independence_wave (4)

- `portrait_ACX_cornish_port_and_mines_committee.png`
- `portrait_AEX_flemish_civil_industrial_board.png`
- `portrait_ASY_independence_wave_provisional_national_council.png`
- `portrait_BRI_independence_wave_civic_commission.png`

These four fictional institutional masters were recovered from their full-resolution generated source outputs.

## 010_death (2)

- `portrait_DTH_zol.png`
- `portrait_DTH_zol_world_end.png`

Both entries use the recovered full-resolution Zol source master from Git history. The animated sheet remains a DDS-derived fallback because a static source is not a substitute for its animation package.

## 018_resources_found (7)

- `portrait_DHO_khalvek.png`
- `portrait_DHO_khalvek_small.png`
- `portrait_DHO_orrukesh.png`
- `portrait_DHO_orrukesh_small.png`
- `portrait_DHO_thessik.png`
- `portrait_DHO_thessik_small.png`
- `portrait_DHO_vhorruk_animated.png`

The three static/small pairs use their recovered full-resolution generated masters. The animated Vhorruk entry uses the first original full-resolution animation source frame recovered from Git history; the unrelated static Vhorruk entry remains a DDS-derived fallback.

# DDS-derived fallback portraits

## 000_easter_eggs (1)

- `gfx/leaders/000_easter_eggs/portrait_ENG_neville_chamberlain_immortal.dds`

## 001_communism_spread (1)

- `gfx/leaders/001_communism_spread/portrait_communist_rebels.dds`

## 002_zombie_outbreak (13)

- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_1.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_2.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_3.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_4.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_leader_5.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_demonic.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_infected.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_mutant.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_necrotic.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_parasitic.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_rabid.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_undead.dds`
- `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_wendigo.dds`

## 003_holy_realm (1)

- `gfx/leaders/003_holy_realm/portrait_THR_godly_figure.dds`

## 005_soviet_collapse (61)

- `gfx/leaders/005_soviet_collapse/AAX_leader.dds`
- `gfx/leaders/005_soviet_collapse/ABX_leader.dds`
- `gfx/leaders/005_soviet_collapse/ADX_leader.dds`
- `gfx/leaders/005_soviet_collapse/AEX_leader.dds`
- `gfx/leaders/005_soviet_collapse/ANX_leader.dds`
- `gfx/leaders/005_soviet_collapse/AOX_leader.dds`
- `gfx/leaders/005_soviet_collapse/ARD_leader.dds`
- `gfx/leaders/005_soviet_collapse/ARM_leader.dds`
- `gfx/leaders/005_soviet_collapse/AZR_leader.dds`
- `gfx/leaders/005_soviet_collapse/BBH_leader.dds`
- `gfx/leaders/005_soviet_collapse/BLR_leader.dds`
- `gfx/leaders/005_soviet_collapse/BSK_leader.dds`
- `gfx/leaders/005_soviet_collapse/BYA_leader.dds`
- `gfx/leaders/005_soviet_collapse/CFR_leader.dds`
- `gfx/leaders/005_soviet_collapse/CRI_leader.dds`
- `gfx/leaders/005_soviet_collapse/DHC_leader.dds`
- `gfx/leaders/005_soviet_collapse/DSC_leader.dds`
- `gfx/leaders/005_soviet_collapse/EST_leader.dds`
- `gfx/leaders/005_soviet_collapse/FER_leader.dds`
- `gfx/leaders/005_soviet_collapse/FEV_leader.dds`
- `gfx/leaders/005_soviet_collapse/FTH_leader.dds`
- `gfx/leaders/005_soviet_collapse/GAC_leader.dds`
- `gfx/leaders/005_soviet_collapse/GEO_leader.dds`
- `gfx/leaders/005_soviet_collapse/ICD_leader.dds`
- `gfx/leaders/005_soviet_collapse/IJX_leader.dds`
- `gfx/leaders/005_soviet_collapse/IKX_leader.dds`
- `gfx/leaders/005_soviet_collapse/ILX_leader.dds`
- `gfx/leaders/005_soviet_collapse/IMX_leader.dds`
- `gfx/leaders/005_soviet_collapse/INX_leader.dds`
- `gfx/leaders/005_soviet_collapse/IUL_leader.dds`
- `gfx/leaders/005_soviet_collapse/KAR_leader.dds`
- `gfx/leaders/005_soviet_collapse/KAZ_leader.dds`
- `gfx/leaders/005_soviet_collapse/KHC_leader.dds`
- `gfx/leaders/005_soviet_collapse/KMB_leader.dds`
- `gfx/leaders/005_soviet_collapse/KOM_leader.dds`
- `gfx/leaders/005_soviet_collapse/KYR_leader.dds`
- `gfx/leaders/005_soviet_collapse/LAT_leader.dds`
- `gfx/leaders/005_soviet_collapse/LID_leader.dds`
- `gfx/leaders/005_soviet_collapse/LIT_leader.dds`
- `gfx/leaders/005_soviet_collapse/MFR_leader.dds`
- `gfx/leaders/005_soviet_collapse/MOL_leader.dds`
- `gfx/leaders/005_soviet_collapse/NLC_leader.dds`
- `gfx/leaders/005_soviet_collapse/NRF_leader.dds`
- `gfx/leaders/005_soviet_collapse/PRA_leader.dds`
- `gfx/leaders/005_soviet_collapse/RCD_leader.dds`
- `gfx/leaders/005_soviet_collapse/RLD_leader.dds`
- `gfx/leaders/005_soviet_collapse/SDZ_leader.dds`
- `gfx/leaders/005_soviet_collapse/SEP_leader.dds`
- `gfx/leaders/005_soviet_collapse/SOG_leader.dds`
- `gfx/leaders/005_soviet_collapse/SZA_leader.dds`
- `gfx/leaders/005_soviet_collapse/TAJ_leader.dds`
- `gfx/leaders/005_soviet_collapse/TAN_leader.dds`
- `gfx/leaders/005_soviet_collapse/TAT_leader.dds`
- `gfx/leaders/005_soviet_collapse/TMS_leader.dds`
- `gfx/leaders/005_soviet_collapse/TNC_leader.dds`
- `gfx/leaders/005_soviet_collapse/TRS_leader.dds`
- `gfx/leaders/005_soviet_collapse/UDC_leader.dds`
- `gfx/leaders/005_soviet_collapse/UKR_leader.dds`
- `gfx/leaders/005_soviet_collapse/UWD_leader.dds`
- `gfx/leaders/005_soviet_collapse/UZB_leader.dds`
- `gfx/leaders/005_soviet_collapse/YAK_leader.dds`

## 006_independence_wave (11)

- `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander.dds`
- `gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander.dds`
- `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds`
- `gfx/leaders/006_independence_wave/portrait_ARX_luigi_mella_santelia.dds`
- `gfx/leaders/006_independence_wave/portrait_ARX_vittorio_verne.dds`
- `gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds`
- `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds`
- `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_adolphe_landry.dds`
- `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_jean_chiappe.dds`
- `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds`
- `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds`

## 010_death (1)

- `gfx/leaders/010_death/portrait_DTH_zol_world_end_animated.dds`

## 018_resources_found (1)

- `gfx/leaders/018_resources_found/portrait_DHO_vhorruk.dds`

## 038_malta_crusaders (1)

- `gfx/leaders/038_malta_crusaders/portrait_CRU_crusader.dds`

## 091_the_great_revolution (1)

- `gfx/leaders/091_the_great_revolution/portrait_REV_vladimir_lenin.dds`

## scientists (29)

- `gfx/leaders/scientists/generic_scientists/portrait_generic_africa_male_01.dds`
- `gfx/leaders/scientists/generic_scientists/portrait_generic_asia_male_01.dds`
- `gfx/leaders/scientists/generic_scientists/portrait_generic_asia_male_02.dds`
- `gfx/leaders/scientists/generic_scientists/portrait_generic_biowarfare_europe_male_01.dds`
- `gfx/leaders/scientists/generic_scientists/portrait_generic_europe_male_02.dds`
- `gfx/leaders/scientists/generic_scientists/portrait_generic_europe_male_03.dds`
- `gfx/leaders/scientists/generic_scientists/portrait_generic_europe_male_04.dds`
- `gfx/leaders/scientists/portrait_AST_howard_florey.dds`
- `gfx/leaders/scientists/portrait_ENG_alexander_fleming.dds`
- `gfx/leaders/scientists/portrait_ENG_ernst_chain.dds`
- `gfx/leaders/scientists/portrait_ENG_paul_fildes.dds`
- `gfx/leaders/scientists/portrait_GER_erich_traub.dds`
- `gfx/leaders/scientists/portrait_GER_gerhard_schrader.dds`
- `gfx/leaders/scientists/portrait_GER_josef_mengele.dds`
- `gfx/leaders/scientists/portrait_GER_kurt_blome.dds`
- `gfx/leaders/scientists/portrait_GER_kurt_gutzeit.dds`
- `gfx/leaders/scientists/portrait_GER_perfect_aryan.dds`
- `gfx/leaders/scientists/portrait_GER_sigmund_rascher.dds`
- `gfx/leaders/scientists/portrait_GER_walter_schreiber.dds`
- `gfx/leaders/scientists/portrait_JAP_chikahiko_koizumi.dds`
- `gfx/leaders/scientists/portrait_JAP_masaji_kitano.dds`
- `gfx/leaders/scientists/portrait_JAP_shiro_ishii.dds`
- `gfx/leaders/scientists/portrait_POL_franciszek_witaszek.dds`
- `gfx/leaders/scientists/portrait_SOV_grigory_mairanovsky.dds`
- `gfx/leaders/scientists/portrait_SOV_ivan_mikhailovich_velikanov.dds`
- `gfx/leaders/scientists/portrait_SOV_lavrentiy_pavlovich_beria.dds`
- `gfx/leaders/scientists/portrait_USA_frank_olson.dds`
- `gfx/leaders/scientists/portrait_USA_ira_baldwin.dds`
- `gfx/leaders/scientists/portrait_USA_murray_sanders.dds`
