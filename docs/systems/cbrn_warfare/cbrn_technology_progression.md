# CBRN technology progression

The chemical and biological folders use a 50/75/100 base-day research scale: `research_cost = 0.5` for basic utility, `0.75` for ordinary equipment and service improvements, and `1` for advanced equipment and containment. The values are relative to the engine's 100-day baseline before year penalties and research modifiers. `common/technologies/chaosx_technologies.txt` owns the shared research nodes, while the separate headquarters and regimental technology files own their unit certifications.

## Research and grants

1. Basic Service Respirators lead to Improved Service Masks, Advanced Protective Clothing, and Sealed Assault Protection. The first three unlock their matching equipment models; Sealed Assault Protection is the 1942 advanced equipment research, requires Chaos Warfare doctrine, unlocks the fourth mask model, and awards the hidden overpressure capability. Improved masks award fitting, registration, and filter standardization; advanced masks award rapid filter replacement. The hidden capabilities remain as IDs because protection effects and compatibility consumers read them.
2. Field Detection and Weather Sets lead to Mobile Sampling Laboratories and Theater Detection and Forecasting Sets. Each visible research unlocks the next instrument model and awards the matching hidden weather capability, so reconnaissance and forecast improvements require one research step per equipment tier.
3. Field Decontamination Kits lead to Mobile Wash Columns and Rapid Decontamination Plants. Each visible research unlocks the matching decontamination equipment tier; the field kits also unlock the Protection Company. The doctrine's Hazard Pioneer Formation certification upgrades that company directly at its mastery milestone. Its unit technology is owned by `common/technologies/cbrn_regimental_support_technologies.txt` and has no visible research node.
4. Pathogen Handling Protocols lead to Sealed Containment Laboratories and Fail-Safe Containment Facilities. Biological Surveillance Networks lead to Rapid Outbreak Response and Integrated Epidemic Control. These are ordinary biological defensive research, while the bomb rewards below are granted by projects.

The following special projects grant their matching equipment technology on completion. The technology definitions retain equipment unlocks and completion effects, and their `allow` block requires the matching completed project, so they appear as locked cards in their branch and never need a second research order. Existing event, focus, and debug grants may still award these same IDs.

| Project | Granted technology | Equipment unlocked |
| --- | --- | --- |
| `anthrax_bomb` | `anthrax_bomb_delivery_systems` | `anthrax_bomb_1` |
| `plague_bomb` | `plague_bomb_delivery_systems` | `plague_bomb_1` |
| `tularemia_bomb` | `tularemia_bomb_delivery_systems` | `tularemia_bomb_1` |
| `smallpox_bomb` | `smallpox_bomb_delivery_systems` | `smallpox_bomb_1` |
| `sp_cw_sarin_program` | `sarin` | Sarin cylinder and agent lots, plus delivery modules |
| `sp_cw_soman_program` | `soman` | Soman cylinder and agent lots, plus delivery modules |

Doctrine and operation capabilities such as Chaos Assault Battalion, chemical shell filling, armored delivery, and Theater CBRN Headquarters are granted through `cbrn_grant_available_doctrine_technologies` and its commissioning calls when their mastery or certification triggers are met. They have no visible research branch. Sealed Assault Protection remains visible equipment research after Advanced Protective Clothing; possession of doctrine alone does not grant its equipment.

## Direct unit-stat balance

The two Livens Projector researches each give the Chemical Projector Battery +2.5% soft attack, +13% hard attack, +4% defense and +6.5% breakthrough.
These are fractional subunit bonus fields rather than flat attack or defense points.
The [actual-source budget audit](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-07_doctrine_reward_budget_source_checks.md) resolves the applicable doctrine categories and country sources against each retained unit.
Its conservative independent-layer bounds for Projector are +32.8602% soft attack, +32.8455% hard attack, +34.7559% defense and +34.5832% breakthrough, including the possible extra commander defense-skill contribution where applicable.
The hard-attack fraction is larger because the battery's authored hard-attack base is 4, compared with 12 soft attack; the nominal one-technology increments are 0.52 and 0.30 points respectively before equipment and other modifiers.
The hidden 1942 Chaos Assault Battalion technology grants 4% breakthrough, alongside one 15% mastery III doctrine grant.
Reserving the possible Cadres and CBRN-earned defense-skill layers gives a conservative +34.849% breakthrough bound.
Native combination of technology, unit/category, commander and country layers remains unproved.

`max_organisation = 11` on the 1942 Battalion technology is a flat organization-point bonus, following the installed vanilla infantry-technology pattern.
On the Battalion's base forty, this is a +27.5% relative gain, with a conservative +33.3404% source bound after the applicable country factors.
The three hidden weather technologies grant `recon` values of 0.01, 0.02 and 0.03 through the three visible instrument tiers.
Under the existing flat-point interpretation, their total is 0.06 points on the Recon Detachment's base four, or +1.5% before country and leader factors.
The [accepted combined reconnaissance correction](../../specs/chaos_warfare_system_specs/corrections/2026-10-07_reconnaissance_combined_budget.md) reserves the doctrine and both HQ contributions in the same source budget.

Integrated Command grants 25% reconnaissance at adoption; Operations and Medical HQs grant 4% and 2% respectively.
The independent-layer source bound is +34.589% with the point grants pooled, or +34.59813% when each point grant is normalized independently against base four.
Native flat-point semantics, HQ accumulation and actual division values remain unverified; the [source review](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-07_reconnaissance_budget_review.md) states the conflicting generic wiki wording and the exact limitations.

## Folder layout and presentation

Both folders follow the vanilla horizontal folder pattern. Every branch has its own `gridboxtype` in `interface/countrytechtreeview.gui` with `format = "LEFT"` and the vanilla `slotsize = { width = 70 height = 70 }`, so the engine's 36-pixel connector segments tile without gaps. Branch gridboxes start at x = 220, the first branch row at y = 190, and each later branch row 110 pixels lower. Inside a branch every card keeps `x = 0` and only the year column changes, and a year column is three slots (210 pixels) apart, the room a full-size 183-pixel research card needs. The year constants live at the top of `common/technologies/chaosx_technologies.txt` and the folder windows mirror them in pixels.

Cards use the vanilla item rule: a technology that unlocks equipment draws the full-size `techtree_<folder>_item` card with its name, and a technology without equipment draws the small `techtree_<folder>_small_item` box. No CBRN research technology forces the small layout. In the chemical folder only Dimercaprol is a small card; in the biological folder the four bomb delivery technologies are full-size cards and the containment, surveillance and medical services are small boxes.

Chemical rows, top to bottom: choking, blister, nerve, projectors, protection, detection, decontamination, over the year columns 1918, 1936, 1939, 1940, 1941 and 1942. Biological rows: munitions, containment, surveillance, medical, over 1936, 1938, 1940 and 1941. Every link is one column (210 pixels) or, where a branch skips a year, two columns (420 pixels), which is the longest link the vanilla support folder draws.

Year headers sit ten pixels left of their column at y = 50, matching the vanilla infantry folder. Branch names sit in the gutter left of the first card column, right-aligned so they end ten pixels before the full-size card edge at x = 164. The chemical folder has a 1450x980 content filler and the biological folder a 1040x715 one; both cover the folder background and the lowest card row.

The special-project technologies are visible locked cards rather than hidden research. The four bomb delivery technologies fill the biological munitions row, and sarin and soman continue the chemical nerve row after tabun. Each one keeps `is_special_project_tech = yes`, draws the special-project card background already registered in `interface/chaosx_techtree.gfx`, and has `allow = { ROOT = { is_special_project_completed = sp:<project> } }` in place of a permanent block, following the vanilla `jet_fighter1` pattern. Their projects still grant the technology on completion and their research weight stays at zero, so the AI never researches them directly. Their start years follow the branch they sit in: 1936 anthrax, 1938 plague, 1940 tularemia and 1941 smallpox.

Three start years follow the column they sit in so that each branch advances one column at a time: lewisite and tabun are 1936 research, and Rapid Decontamination Plants is 1941 research. Lowering a start year only removes an ahead-of-time penalty for a country that researches before that year; the research-day targets are unchanged.

All research card art is 64x64, as vanilla uses for `artillery1.dds` inside a full-size card. The Livens projector cards use `gfx/interface/technologies/livens_projector_tech.dds`, `livens_projector_improved_tech.dds` and `livens_projector_advanced_tech.dds`; the wider 94x45 paintings remain with the Livens equipment sprites, which is the canvas their equipment consumer expects. The chemical agent cards each show their own munition or apparatus instead of one shared cylinder painting: `chlorine_gas_tech.dds`, `phosgene_gas_tech.dds`, `mustard_gas_tech.dds`, `lewisite_gas_tech.dds`, `tabun_ga_vector_tech.dds`, `sarin_gas_tech.dds` and `soman_gas_tech.dds`.

Player-facing names, descriptions, seven `CBRN_TECH_YEAR_*` folder-year labels, and eleven `CBRN_TECH_BRANCH_*` lane labels live in `localisation/english/cbrn_technology_research_l_english.yml`. They describe the combined equipment and service capability rather than displaying tuning constants. The folder and technology icon sprites are registered in `interface/chaosx_techtree.gfx`, `interface/chaosx_equipment.gfx` and `interface/cbrn_protection.gfx`; no further artwork is needed for this progression. The visible protection icons are `GFX_basic_gas_masks_medium`, `GFX_improved_gas_masks_medium`, `GFX_advanced_gas_masks_medium`, and `GFX_sealed_assault_protection_medium`. The visible detection icons are `GFX_chemical_detection_paper_medium`, `GFX_mobile_sampling_laboratories_medium`, and `GFX_theater_cbrn_command_set_medium`. The visible decontamination icons are `GFX_field_decontamination_kits_medium`, `GFX_mobile_wash_columns_medium`, and `GFX_rapid_decontamination_plants_medium`. The biological containment and surveillance icons are `GFX_pathogen_handling_protocols_medium`, `GFX_sealed_containment_laboratories_medium`, `GFX_fail_safe_containment_facilities_medium`, `GFX_bio_surveillance_networks_medium`, `GFX_rapid_outbreak_response_medium`, and `GFX_integrated_epidemic_control_medium`. Their DDS files live under `gfx/interface/technologies/` or `gfx/interface/technologies/stage_2_protective_equipment/`, matching the sprite `texturefile` definitions. The technology folder backgrounds are `GFX_chemical_warfare_techtree_bg` and `GFX_biowarfare_techtree_bg` in `interface/chaosx_techtree.gfx`.

The technology renderer resolves all 21 chemical and all 12 biological card coordinates from source with no pairwise card overlap and no unresolved icon sprite, and the GUI renderer draws the rebuilt folder chrome at 1920x1080 and 2560x1440 with UI scale 1. That renderer does not draw native technology cards, tooltips or scrolling, so in-game scroll reach, card tooltips and final DDS appearance remain unverified; the [layout note](../../plans/chaos_warfare_system_plans/2026-10-10_technology_folder_layout_repair.md) records the before and after geometry.

## Interactions and future plans

Protection issue and maintenance consume actual mask stocks through `common/scripted_effects/cbrn_protection_effects.txt`. Doctrine grants are resolved in `common/scripted_effects/cbrn_doctrine_effects.txt`. Project completion outputs are in `common/special_projects/projects/biowarfare_main_projects.txt` and `common/special_projects/projects/chemical_warfare_nerve_projects.txt`. Research AI weights are in `common/ai_strategy/chemical_warfare_research.txt`; retired capability IDs must not receive direct research weight because they are awarded automatically.

Future work could add an in-folder project milestone indicator that shows completed bomb and nerve-agent projects without making their output technologies researchable. Any such presentation should use the installed technology GUI and preserve the one-project, one-equipment-unlock path.
