# Event 014 Live Asset Gap Map

> **Superseded production snapshot.** This file records the live gap state on 2026-07-11 and must not be used as current missing-file evidence. The gaps it lists were resolved by later asset packages. Current authority is `docs/assets/014_cannibalism/manifest.md`, its linked package manifests, `docs/specs/014_cannibalism_specs/matrices/asset_inventory_matrix.md`, and the final documentation reconciliation handoff. The historical body below is intentionally preserved unchanged.

Date of live audit: 2026-07-11

Historical purpose: provide the bridge between the 2026-07-11 Event 014 specification, retained source packages, the runtime filesystem at that checkpoint, and the asset-production and wiring passes that followed. It does not describe the final package.

## Authority and status language

The governing design sources are:

- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_10_assets_animation_and_localisation.md
- docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_11_achievements_scenarios_and_aftermath.md
- docs/specs/014_cannibalism_specs/matrices/asset_inventory_matrix.md
- docs/specs/014_cannibalism_specs/matrices/hidden_identity_surface_audit.md
- docs/assets/014_cannibalism/manifest.md, used as historical package metadata rather than proof that a file is live

Status terms used below:

| Status | Meaning |
| --- | --- |
| Satisfying | The correct file exists at the live runtime path, matches the current specification, has the required format, and has or is ready for exact runtime wiring. |
| Source-complete | Separate source artwork, processed PNGs, sheet/static PNGs, GIF preview, contact sheet, and package notes exist, but the runtime DDS or wiring is missing. This is not a live asset. |
| Stale | The file exists, but belongs to an earlier Event 014 contract, uses obsolete semantics or names, or has no current gameplay target. |
| Wrong | The file is technically or visually incompatible with the current requirement, is in the wrong event folder, or would violate spoiler or content direction. |
| Missing | No current file satisfies the requirement. |
| Blocked | Exact production must wait for a final gameplay ID, GUI rectangle, cosmetic tag, or other implementation-owned contract. |

A historical deletion is evidence only. A deleted file never counts as satisfying, source-complete, or available for silent restoration.

## Final format contract

Unless an engine-specific implementation proves otherwise:

- Final DDS: uncompressed 32-bit BGRA/B8G8R8A8 with alpha where the surface requires transparency. Do not use DXT1, DXT3, or DXT5 for this package.
- Report images: 210 by 176 DDS, period documentary color treatment, report-card alpha treatment.
- News images: 397 by 153 DDS, black and white.
- Super-event images: 457 by 328 DDS.
- Portraits: 156 by 210 DDS.
- Idea and achievement icons: 64 by 64 DDS.
- Decision icons: 32 by 32 DDS.
- Focus icons: 94 by 86 DDS.
- Flags: 32-bit BGRA TGA, bottom-origin, at 82 by 52, 41 by 26, and 10 by 7.
- Animated sheets: uncompressed 32-bit BGRA DDS, with the exact frame count and sheet dimensions recorded for the package.
- Each icon family uses purpose-built source art. Focus, idea, decision, achievement, unit, technology, and GUI assets are not interchangeable and must not be resized or silently remapped across families.

The retained live DDS files inspected in the report/news, portrait, idea, and achievement families use uncompressed 32-bit BGRA. The two files explicitly named original_unused use DXT compression and are not acceptable finals.

## Executive live-state matrix

| Requirement family | Current specification | Files physically present at runtime | Accepted live count | Verdict |
| --- | ---: | ---: | ---: | --- |
| Report images | 10 | 11 active-named DDS plus 1 original_unused DDS | 0 | All surviving files are stale against the current ten-image direction ledger. |
| News images | 6 | 1 active-named DDS plus 1 original_unused DDS | 0 | The active image is only a broad old public-exposure candidate; it is not an accepted current final. |
| Super-event images | 4 | 0 in the Event 014 folder | 0 | Missing. One old Wendigo image is misplaced under Event 002 and is wrong. |
| Generic warlord portraits | 8 to 12 | 0 | 0 | Missing. |
| Ordinary leader portrait | 1 static plus 12 frames | 1 protected old static portrait | 0 | Protected file retained, but it does not meet the current ordinary portrait brief and has no animation package. |
| Wendigo leader portrait | 1 static plus 16 frames | 1 old static portrait | 0 | Visually wrong and no animation package. |
| Warlord flags | 8 families | 0 CBA-CBH families | 0 | Missing. |
| Unified flags | 4 families plus transformed identity | 24 partial CBL/CBL_LAST_TABLE files across three sizes | 0 | Format-valid but incomplete and based on an obsolete route identity. |
| Focus icons | 180 to 224 | 0 physically present; 37 tracked files are deleted in the worktree | 0 | Missing and blocked on final focus IDs. |
| Idea icons | 20 or more | 18 old DDS | 0 | Format-valid but stale and unwired under the new lifecycle. |
| Decision icons | 24 or more | 0 | 0 | Missing. Old source PNG packages do not count as live. |
| Achievement icons | 18 triplets, 54 DDS | 13 old triplets, 39 DDS | 0 | Old contract, missing current 18 IDs, and unwired. |
| Unit and technology art | As required by final unit/technology IDs | 0 Event 014 files | 0 | Blocked on implementation IDs. |
| Static GUI art | Full five-window state set | 0 | 0 | Missing and blocked on final GUI rectangles. |
| Required source animations already assigned | 6 custom packages | 6 source packages | 0 | Source-complete only; all 12 runtime DDS files and all wiring are missing. |
| Full Part 10 animation ledger | 14 packages | 6 adjacent custom source packages | 0 | Eleven specification rows remain without an exact source package; three rows have plausible source matches pending semantic acceptance. |
| Runtime sprite/UI wiring | Event-specific and shared registries | No Event 014 references in current registries | 0 | Missing. |

The untracked directory docs/assets/014_cannibalism/static_event_art_imagegen appeared concurrently during this audit. At the snapshot above it contained five reference-inspection PNGs and no generated deliverables, manifest, processed finals, or runtime files. It is not counted as live or source-complete. Re-audit it before issuing duplicate generation work.

## Current manifest reconciliation

docs/assets/014_cannibalism/manifest.md is a useful map of the deleted package but is not accurate as a live-state manifest.

| Manifest statement or path | Live audit result |
| --- | --- |
| Protected gfx/leaders/014_cannibalism/hannibal.dds | Present. SHA256 verified as 5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88. It must not be overwritten. |
| gfx/super_events/014_cannibalism/ | Missing. |
| gfx/interface/decisions/014_cannibalism/ | Missing. |
| gfx/interface/animated/014_cannibalism/ | Missing. |
| gfx/leaders/014_cannibalism/CBL_table_council.dds | Missing. |
| interface/014_cannibalism.gfx | Missing. |
| interface/014_cannibalism_frontline_hunger.gui | Missing. |
| common/scripted_guis/014_cannibalism_scripted_gui.txt | Missing. |
| Six animation packages marked complete | Their editable source packages are complete; their listed runtime DDS outputs are absent. |
| Animation DDS sizes OK: True | Historical validation only. No listed animation DDS currently exists. |
| Static animation sprite naming | The animation manifest alternates between GFX_[slug] and GFX_[slug]_static. The authoritative convention for the next wiring pass is GFX_[slug]_static and GFX_[slug]_animated. |
| Live package uses no placeholders or transform-only animation | No live animation package exists. The retained source frames are distinct and are valid inputs, but the statement cannot be used as live completion proof. |

After implementation, the top-level asset manifest must be rewritten from the final filesystem rather than amended with more historical claims.

## Report, news, and super-event requirement-to-file matrix

### Report images

Batch ID: E14-RPT-01

All ten files must be newly reviewed against the current period-documentary and explicit-evidence brief. Current old files are not approved as finals.

| Current requirement | Stable final path | Size and format | Current evidence | Status |
| --- | --- | --- | --- | --- |
| Initial field discovery | gfx/event_pictures/014_cannibalism/report_event_cannibalism_field_discovery.dds | 210x176 BGRA DDS | report_event_cannibalism.dds is an old generic candidate and does not meet the current exact direction | Missing |
| Missing burial party | gfx/event_pictures/014_cannibalism/report_event_cannibalism_burial_party.dds | 210x176 BGRA DDS | No exact file | Missing |
| Ration kitchen investigation | gfx/event_pictures/014_cannibalism/report_event_cannibalism_ration_kitchen.dds | 210x176 BGRA DDS | No exact file | Missing |
| Compromised field hospital | gfx/event_pictures/014_cannibalism/report_event_cannibalism_field_hospital.dds | 210x176 BGRA DDS | No exact file | Missing |
| Detention-site evidence | gfx/event_pictures/014_cannibalism/report_event_cannibalism_detention_site.dds | 210x176 BGRA DDS | No exact file | Missing |
| Silent-island landing | gfx/event_pictures/014_cannibalism/report_event_cannibalism_silent_island.dds | 210x176 BGRA DDS | report_event_cannibalism_islands.dds is an old, clean, broad island image | Missing |
| Mature commune village | gfx/event_pictures/014_cannibalism/report_event_cannibalism_commune_village.dds | 210x176 BGRA DDS | report_event_cannibalism_commune.dds is an old broad commune image | Missing |
| Captured warlord camp | gfx/event_pictures/014_cannibalism/report_event_cannibalism_warlord_camp.dds | 210x176 BGRA DDS | No exact file | Missing |
| Liberated feeding state | gfx/event_pictures/014_cannibalism/report_event_cannibalism_feeding_state_liberated.dds | 210x176 BGRA DDS | report_event_cannibalism_defeat.dds and _contained.dds are broad old aftermath images | Missing |
| Broken transformation anchor | gfx/event_pictures/014_cannibalism/report_event_cannibalism_wendigo_anchor_broken.dds | 210x176 BGRA DDS | report_event_cannibalism_world_end.dds is not the required pre-lock broken-anchor scene | Missing |

Surviving report files and dispositions:

- Stale, format-valid old finals: report_event_cannibalism.dds, report_event_cannibalism_commune.dds, report_event_cannibalism_contained.dds, report_event_cannibalism_defeat.dds, report_event_cannibalism_failure.dds, report_event_cannibalism_hannibal_hook.dds, report_event_cannibalism_islands.dds, report_event_cannibalism_network.dds, report_event_cannibalism_ritual.dds, report_event_cannibalism_spread.dds, report_event_cannibalism_world_end.dds.
- Wrong as a final: report_event_cannibalism_original_unused.dds. It is explicitly unused, belongs to the old contract, and is DXT3.

The reveal-specific old filename report_event_cannibalism_hannibal_hook.dds must never be selected by a pre-reveal event or default picture mapping.

### News images

Batch ID: E14-NEWS-01

| Current requirement | Stable final path | Size and format | Current evidence | Status |
| --- | --- | --- | --- | --- |
| Public exposure | gfx/event_pictures/014_cannibalism/news_cannibalism_public_exposure.dds | 397x153 B&W BGRA DDS | news_cannibalism.dds is a broad old candidate, but its current source direction is too clean and generic | Missing |
| First commune or island | gfx/event_pictures/014_cannibalism/news_cannibalism_commune_confirmed.dds | 397x153 B&W BGRA DDS | No exact file | Missing |
| First warlord country | gfx/event_pictures/014_cannibalism/news_cannibalism_first_warlord.dds | 397x153 B&W BGRA DDS | No exact file | Missing |
| Coordinated offensives | gfx/event_pictures/014_cannibalism/news_cannibalism_coordinated_offensives.dds | 397x153 B&W BGRA DDS | No exact file | Missing |
| Public reveal below super-event scale | gfx/event_pictures/014_cannibalism/news_cannibalism_reveal.dds | 397x153 B&W BGRA DDS | No exact file | Missing |
| Global defeat before terminal lock | gfx/event_pictures/014_cannibalism/news_cannibalism_global_defeat.dds | 397x153 B&W BGRA DDS | No exact file | Missing |

news_cannibalism_original_unused.dds is wrong as a final because it is explicitly unused, old-contract art, and DXT1.

### Super-event images

Batch ID: E14-SUPER-01

| Current requirement | Stable final path | Size and format | Current evidence | Status |
| --- | --- | --- | --- | --- |
| Reveal among assembled warlords | gfx/super_events/014_cannibalism/super_event_cannibalism_reveal.dds | 457x328 BGRA DDS | Event 014 super-event folder absent | Missing |
| Ordinary world-end | gfx/super_events/014_cannibalism/super_event_cannibalism_world_end_ordinary.dds | 457x328 BGRA DDS | Event 014 super-event folder absent | Missing |
| Wendigo world-end | gfx/super_events/014_cannibalism/super_event_cannibalism_world_end_wendigo.dds | 457x328 BGRA DDS | Event 014 super-event folder absent | Missing |
| Global defeat aftermath | gfx/super_events/014_cannibalism/super_event_cannibalism_global_defeat.dds | 457x328 BGRA DDS | Event 014 super-event folder absent | Missing |

gfx/super_events/002_zombie_outbreak/super_event_wendigo_hannibal.dds is wrong for Event 014. It is stored under another event, depicts a generic horned face rather than transformed identity continuity in frozen ruins with joint forces, and cannot be copied or aliased into this package.

The old generated source set under docs/assets/014_cannibalism/generated_art_sources/ contains report, news, and four old super-event directions. Those sources remain useful historical references, but none is accepted as the exact current Part 10 art contract.

## Portrait requirement-to-file matrix

### Generic warlords

Batch ID: E14-POR-WARLORD-01

The minimum non-fallback package is eight distinct portraits, one for each warlord slot:

| Slot | Stable final path | Size and format | Live status |
| --- | --- | --- | --- |
| CBA | gfx/leaders/014_cannibalism/leader_CBA_warlord.dds | 156x210 BGRA DDS | Missing |
| CBB | gfx/leaders/014_cannibalism/leader_CBB_warlord.dds | 156x210 BGRA DDS | Missing |
| CBC | gfx/leaders/014_cannibalism/leader_CBC_warlord.dds | 156x210 BGRA DDS | Missing |
| CBD | gfx/leaders/014_cannibalism/leader_CBD_warlord.dds | 156x210 BGRA DDS | Missing |
| CBE | gfx/leaders/014_cannibalism/leader_CBE_warlord.dds | 156x210 BGRA DDS | Missing |
| CBF | gfx/leaders/014_cannibalism/leader_CBF_warlord.dds | 156x210 BGRA DDS | Missing |
| CBG | gfx/leaders/014_cannibalism/leader_CBG_warlord.dds | 156x210 BGRA DDS | Missing |
| CBH | gfx/leaders/014_cannibalism/leader_CBH_warlord.dds | 156x210 BGRA DDS | Missing |

The eight base portraits cover eight origin-agnostic reusable warlord slots. Each must be male-presenting, bald, bloodied, visibly distinct, grounded in invented rough cloth and scavenged period military pieces, non-supernatural, and visibly unlike the hidden leader. Six additional regional variants per slot complete the mandatory 56-portrait matrix; none is optional and none may use a prison setting.

The old deleted leader_CBL_warlord.dds and the retained source portrait of a clean, dark-haired suited man do not satisfy this package.

### Ordinary and transformed leader

Batch IDs: E14-POR-ORDINARY-01 and E14-POR-WENDIGO-01

| Requirement | Stable final path | Required package | Current file and disposition |
| --- | --- | --- | --- |
| Ordinary static fallback | gfx/leaders/014_cannibalism/hannibal_ordinary_static.dds | 156x210 BGRA DDS | gfx/leaders/014_cannibalism/hannibal.dds is protected and hash-valid, but visually stale: formal suit, horn/antler-like background, insufficient gore, mantle, and scars. Preserve; do not overwrite or count. |
| Ordinary animated sheet | gfx/leaders/014_cannibalism/hannibal_ordinary_sheet.dds | 12 distinct 156x210 frames; 1872x210 BGRA DDS | Missing |
| Wendigo static fallback | gfx/leaders/014_cannibalism/hannibal_wendigo_static.dds | 156x210 BGRA DDS | gfx/leaders/014_cannibalism/hannibal_wendigo.dds is a flat symbolic silhouette without facial continuity or cold body horror. Wrong for the current brief. |
| Wendigo animated sheet | gfx/leaders/014_cannibalism/hannibal_wendigo_sheet.dds | 16 distinct 156x210 frames; 2496x210 BGRA DDS | Missing |

Each animated portrait package also requires separate source frames, processed PNG frames, the horizontal PNG sheet, a static PNG fallback, review GIF, contact sheet, brief, frame plan, and manifest. Motion changes must be drawn into distinct frames. The ordinary sequence needs breathing, eyes, shadow, and blood progression. The transformed sequence needs identity continuity plus distinct frost, breath, flesh, and shadow progression.

Internal file names may identify the hidden leader for maintainability. Player-visible default textures, focus names, tooltips, event pictures, achievement visibility, GUI labels, and portrait resolution must remain generic until the public-reveal gate.

## Flag requirement-to-file matrix

### Current files

The live flag tree contains only partial CBL and CBL_LAST_TABLE families:

- Root 82x52: CBL_neutrality.tga, CBL_LAST_TABLE_democratic.tga, CBL_LAST_TABLE_fascism.tga, CBL_LAST_TABLE_neutrality.tga.
- medium 41x26: complete base plus four-ideology sets for CBL and CBL_LAST_TABLE.
- small 10x7: complete base plus four-ideology sets for CBL and CBL_LAST_TABLE.

All 24 surviving files are dimension-valid, bottom-origin BGRA TGA, and visually distinct. They are nevertheless stale for the current package:

- The root set is incomplete.
- CBL_LAST_TABLE is an obsolete route identity; the current contract requires central-command, confederated, and ritual-state variants.
- No CBA-CBH warlord family exists.
- The clean administrative/table imagery does not satisfy the present warlord identity brief.

Commit 1fb0617a4aa790301b0fd8ef6958ec44cc8e9961 deleted six root-size files: CBL.tga, CBL_communism.tga, CBL_democratic.tga, CBL_fascism.tga, CBL_LAST_TABLE.tga, and CBL_LAST_TABLE_communism.tga. They are historical evidence and must not be restored or counted without a new approved design mapping.

### Required families and stable naming

Batch IDs: E14-FLAG-WARLORD-01 and E14-FLAG-UNIFIED-01

Required family tokens:

- CBA, CBB, CBC, CBD, CBE, CBF, CBG, CBH
- CBL
- CBL_CENTRAL_COMMAND
- CBL_HOST_CONFEDERATION
- CBL_RITUAL_STATE
- ZZZ_CANNIBALISM_HANNIBAL for the deliberate transformed cosmetic identity

This is the frozen runtime ledger. `CBL_CENTRAL_COMMAND`, `CBL_HOST_CONFEDERATION`, and `CBL_RITUAL_STATE` are applied by the three post-reveal hierarchy focuses. `ZZZ_CANNIBALISM_HANNIBAL` is applied only by the public Wendigo merge. The eight warlord slots use their tag families directly and do not require extra origin cosmetics. `CBL_LAST_TABLE` is obsolete and must not be restored or counted. E14-FLAG-WARLORD-01 and E14-FLAG-UNIFIED-01 are unblocked for production against these exact tokens.

For each family token F, produce:

- gfx/flags/F.tga, gfx/flags/F_communism.tga, gfx/flags/F_democratic.tga, gfx/flags/F_fascism.tga, gfx/flags/F_neutrality.tga at 82x52.
- gfx/flags/medium/F.tga and the same four suffixes at 41x26.
- gfx/flags/small/F.tga and the same four suffixes at 10x7.

Once accepted, this guaranteed baseline is 13 families by 5 variants by 3 sizes, or 195 TGA files. Any additional frozen origin-route cosmetic family must receive the same five variants and three sizes. If implementation intentionally proves that a cosmetic family can never resolve an ideology suffix, that reduction must be recorded in the final flag manifest; it must not be assumed during art generation. Ideology variants require distinct compositions rather than recolors. All designs must read at 10x7 and avoid text and borrowed real-world sacred or tribal symbols.

## Focus, idea, decision, achievement, unit, and technology matrix

### Focus icons

Batch IDs:

- E14-FOCUS-LOCAL-01: 60 to 72 local-warlord icons.
- E14-FOCUS-UNIFIED-01: 96 to 120 unified-route icons.
- E14-FOCUS-WENDIGO-01: 24 to 32 transformed-overlay icons.

Stable path rule: gfx/interface/goals/014_cannibalism/goal_[final_focus_id].dds, 94x86 uncompressed BGRA DDS.

Exact filenames are blocked until the final focus trees and focus IDs exist. Generating 180 to 224 icons from architecture prose alone would create another unmappable stale package. Each final focus ID needs one row in an ID-to-art ledger before generation, including motif family, spoiler gate, shared-icon approval if any, source path, final DDS, and GFX regular/shine aliases.

The runtime focus folder is physically empty. Thirty-seven tracked old files are deleted in the current worktree and are not candidates for restoration:

~~~text
goal_cannibalism_black_kitchens.dds
goal_cannibalism_butcher_packs.dds
goal_cannibalism_coastal_port_lists.dds
goal_cannibalism_convoy_ambush.dds
goal_cannibalism_council_knives.dds
goal_cannibalism_couriers.dds
goal_cannibalism_depot_inventory.dds
goal_cannibalism_empty_larder.dds
goal_cannibalism_field_kitchen_conversions.dds
goal_cannibalism_first_table.dds
goal_cannibalism_hannibal_cadres.dds
goal_cannibalism_hannibal_discipline.dds
goal_cannibalism_hannibal_hook.dds
goal_cannibalism_hunger_columns.dds
goal_cannibalism_hunting_ground.dds
goal_cannibalism_island_anchorages.dds
goal_cannibalism_larder_columns.dds
goal_cannibalism_last_table.dds
goal_cannibalism_last_table_preparations.dds
goal_cannibalism_mainland_corridors.dds
goal_cannibalism_map_larder.dds
goal_cannibalism_origin_state.dds
goal_cannibalism_pact_compact.dds
goal_cannibalism_port_harvests.dds
goal_cannibalism_prison_processions.dds
goal_cannibalism_prison_roads.dds
goal_cannibalism_prisoner_ledger.dds
goal_cannibalism_rail_corridors.dds
goal_cannibalism_ration_codes.dds
goal_cannibalism_region_projects.dds
goal_cannibalism_restrained_registers.dds
goal_cannibalism_restrained_war.dds
goal_cannibalism_runaway_accounts.dds
goal_cannibalism_scavenger_parties.dds
goal_cannibalism_table_for_one.dds
goal_cannibalism_warlord_kitchen.dds
goal_cannibalism_world_larder.dds
~~~

Their matching document source packages show the scale of the old tree, not completion of the current 180-to-224-icon requirement.

### Idea icons

Batch ID: E14-IDEA-01

The live folder contains 18 format-valid but stale and unwired DDS files:

~~~text
cannibalism_field_disappearances.dds
cannibalism_ritual_hunger.dds
cannibalism_public_truth.dds
cannibalism_exploitation_scandal.dds
cannibalism_commune_country.dds
cannibalism_last_table.dds
cannibalism_night_transfer_zone.dds
cannibalism_empty_village_reports.dds
cannibalism_silent_garrison.dds
cannibalism_commune.dds
cannibalism_hunting_ground.dds
cannibalism_council_obedience.dds
cannibalism_warlord_kitchen.dds
cannibalism_hannibal_discipline.dds
cannibalism_scavenger_logistics.dds
cannibalism_pact_couriers.dds
cannibalism_solitary_rampage.dds
cannibalism_last_table_integration.dds
~~~

They must not be silently assigned to the new lifecycle. A same-family file may only survive if the final idea ID ledger explicitly accepts its exact semantics and source quality.

The recommended 24-icon baseline is:

~~~text
idea_cannibalism_in_the_ranks.dds
idea_cannibalism_emergency_ration_discipline_command.dds
idea_cannibalism_sealed_military_scandal.dds
idea_cannibalism_terror_feeding_program.dds
idea_cannibalism_discipline_restored.dds
idea_cannibalism_the_line_was_crossed.dds
idea_cannibalism_starving_warband.dds
idea_cannibalism_broken_chain_of_command.dds
idea_cannibalism_hunted_by_all.dds
idea_cannibalism_the_first_larder.dds
idea_cannibalism_origin_island_host.dds
idea_cannibalism_origin_siege_commune.dds
idea_cannibalism_origin_march_host.dds
idea_cannibalism_hierarchy_central_command.dds
idea_cannibalism_hierarchy_host_confederation.dds
idea_cannibalism_hierarchy_ritual_state.dds
idea_cannibalism_unified_larder_state.dds
idea_cannibalism_revealed_command.dds
idea_cannibalism_global_feeding_state.dds
idea_cannibalism_transformation_anchors.dds
idea_cannibalism_wendigo_terminal_form.dds
idea_cannibalism_liberation_trauma.dds
idea_cannibalism_recovery_discipline.dds
~~~

All paths are under gfx/interface/ideas/014_cannibalism/ and all files are 64x64 uncompressed BGRA DDS. The implementation idea lifecycle may add further distinct icons; it may not collapse these directions merely to remain at twenty.

### Decision icons

Batch ID: E14-DECISION-01

The runtime decision folder is absent. Old PNG source packages contain 24 earlier decision/category pictures, but no runtime file exists and the old names do not cover the new family ledger.

Produce these 23 exact 32x32 decision files under gfx/interface/decisions/014_cannibalism/:

~~~text
decision_cannibalism_supply_repair.dds
decision_cannibalism_convoy_relief.dds
decision_cannibalism_unit_rotation.dds
decision_cannibalism_officer_replacement.dds
decision_cannibalism_military_police.dds
decision_cannibalism_forensic_recovery.dds
decision_cannibalism_witness_protection.dds
decision_cannibalism_tribunal.dds
decision_cannibalism_amnesty.dds
decision_cannibalism_cell_infiltration.dds
decision_cannibalism_courier_disruption.dds
decision_cannibalism_prison_protection.dds
decision_cannibalism_island_reconnaissance.dds
decision_cannibalism_blockade.dds
decision_cannibalism_commune_assault.dds
decision_cannibalism_larder_consumption.dds
decision_cannibalism_warband_recruitment.dds
decision_cannibalism_foreign_seeding.dds
decision_cannibalism_warlord_submission.dds
decision_cannibalism_hannibal_absorption.dds
decision_cannibalism_anchor_assault.dds
decision_cannibalism_transformation_acceleration.dds
decision_cannibalism_state_recovery.dds
~~~

The twenty-fourth minimum icon is decision_category_cannibalism.dds, also 32x32 for the decision-list category icon. Larger decision-category pictures and mechanic-window seals are separate GUI-specific assets and must receive their own dimensions after layout freeze; they do not replace any of the 23 decision icons.

### Achievement triplets

Batch ID: E14-ACHIEVEMENT-01

The live 39 files form 13 old triplets:

~~~text
014_cannibalism_clean_mess
014_cannibalism_no_second_table
014_cannibalism_silent_island
014_cannibalism_do_not_feed_the_front
014_cannibalism_trial_without_panic
014_cannibalism_black_larder
014_cannibalism_last_ship_home
014_cannibalism_burn_the_cookbooks
014_cannibalism_hunger_of_hannibal
014_cannibalism_the_living_are_not_cattle
014_cannibalism_empty_larder
014_cannibalism_table_for_one
014_cannibalism_after_the_feast
~~~

Each stem currently has .dds, _grey.dds, and _not_eligible.dds at 64x64 uncompressed BGRA. Their source packages and contact sheets are technically valid for the old contract. They are stale because the current Part 11 ledger defines 18 different achievement IDs and no current achievement script or sprite aliases use them. The apparent no_second_table overlap must be explicitly accepted; it cannot be silently remapped.

The authoritative new stems are:

~~~text
014_cannibalism_01_clean_first_country
014_cannibalism_02_no_second_table
014_cannibalism_03_three_front_containment
014_cannibalism_04_silent_islands_reclaimed
014_cannibalism_05_cured_then_returned
014_cannibalism_06_repentant_weapon
014_cannibalism_07_break_the_island_host
014_cannibalism_08_warlord_without_master
014_cannibalism_09_host_of_unification
014_cannibalism_10_all_mouths_one_command
014_cannibalism_11_continental_larder
014_cannibalism_12_stop_the_reveal
014_cannibalism_13_defeat_hannibal
014_cannibalism_14_break_the_winter_hunger
014_cannibalism_15_ordinary_world_end
014_cannibalism_16_wendigo_world_end
014_cannibalism_17_global_burial_detail
014_cannibalism_18_no_empty_state
~~~

For every stem S, generate gfx/achievements/S.dds, gfx/achievements/S_grey.dds, and gfx/achievements/S_not_eligible.dds at 64x64 uncompressed BGRA. The completed art is distinct; the grey version is a true monochrome treatment; the not-eligible version has the project overlay. Hidden and secret icons must not become visible in the achievement list before their Part 11 gates.

### Unit counters and technology art

Batch IDs: E14-UNIT-01 and E14-TECH-01

No Event 014 unit-counter, technology, equipment, or badge file exists. Exact output is blocked until the implementation defines whether these are real subunit types, template-only names, modifiers, technologies, or equipment unlocks.

The required design ledger must evaluate:

- Scavenger Warband
- Feast Cohort
- Bone Guard
- Island Reavers
- Siege Eaters
- March Predation Columns
- Network Cadres
- transformed Wendigo variants

For every implemented subunit ID U, use the local counter convention:

- gfx/interface/counters/divisions_large/unit_U_icon.dds: 152x42 BGRA sheet, two 76x42 frames.
- gfx/interface/counters/divisions_small/onmap_unit_U_icon.dds: 60x12 BGRA sheet, two 30x12 frames.
- GFX_unit_U_icon_medium and GFX_unit_U_icon_medium_white in interface/chaosx_subuniticons.gfx with noOfFrames = 2.

For every actual non-equipment technology ID T, use gfx/interface/technologies/T.dds at 64x64 BGRA and register GFX_T_medium. For an equipment-unlock portrait, follow the final equipment registry and local 131x52 medium-art precedent rather than assuming a technology icon can be reused. No unit image may be reused as focus, idea, decision, or technology art.

## Animation source, runtime, and specification gap matrix

### Six retained source packages

All six packages below contain eight visually distinct source frames, eight processed 64x64 RGBA frames, a 512x64 PNG sheet, a 64x64 static PNG, an eight-frame 128x128 GIF preview, a contact sheet, brief, and frame plan. Their source frames satisfy the non-transform-only rule. No runtime DDS or registry/UI wiring exists.

| Package | Stable static DDS | Stable sheet DDS | Sprite aliases | Source status | Runtime status |
| --- | --- | --- | --- | --- | --- |
| cannibalism_frontline_hunger_seal | gfx/interface/animated/014_cannibalism/cannibalism_frontline_hunger_seal_static.dds | gfx/interface/animated/014_cannibalism/cannibalism_frontline_hunger_seal_sheet.dds | GFX_cannibalism_frontline_hunger_seal_static / _animated | Source-complete; plausible Early warning seal match | Missing |
| cannibalism_cult_pressure_warning | gfx/interface/animated/014_cannibalism/cannibalism_cult_pressure_warning_static.dds | gfx/interface/animated/014_cannibalism/cannibalism_cult_pressure_warning_sheet.dds | GFX_cannibalism_cult_pressure_warning_static / _animated | Source-complete; plausible Cult Cohesion warning match, semantic approval needed | Missing |
| cannibalism_island_signal_card | gfx/interface/animated/014_cannibalism/cannibalism_island_signal_card_static.dds | gfx/interface/animated/014_cannibalism/cannibalism_island_signal_card_sheet.dds | GFX_cannibalism_island_signal_card_static / _animated | Source-complete; direct Island alert match | Missing |
| cannibalism_hannibal_resonance_seal | gfx/interface/animated/014_cannibalism/cannibalism_hannibal_resonance_seal_static.dds | gfx/interface/animated/014_cannibalism/cannibalism_hannibal_resonance_seal_sheet.dds | GFX_cannibalism_hannibal_resonance_seal_static / _animated | Source-complete custom reveal-only seal; not the 94x86 twelve-frame unification seal | Missing |
| cannibalism_council_portrait_overlay | gfx/interface/animated/014_cannibalism/cannibalism_council_portrait_overlay_static.dds | gfx/interface/animated/014_cannibalism/cannibalism_council_portrait_overlay_sheet.dds | GFX_cannibalism_council_portrait_overlay_static / _animated | Source-complete custom overlay; not the six-frame selected-target overlay | Missing |
| cannibalism_world_end_progress_border | gfx/interface/animated/014_cannibalism/cannibalism_world_end_progress_border_static.dds | gfx/interface/animated/014_cannibalism/cannibalism_world_end_progress_border_sheet.dds | GFX_cannibalism_world_end_progress_border_static / _animated | Source-complete 64x64 custom border; not either UI-dependent twelve-frame terminal frame | Missing |

Batch E14-ANIM-RUNTIME-01 converts those twelve listed outputs to uncompressed BGRA DDS, registers all twelve aliases in interface/014_cannibalism.gfx, and wires their intended GUI surfaces. Static sprites use the exact _static suffix; animated sprites use _animated, noOfFrames = 8, looping = yes, play_on_show = yes, and 8 FPS. The reveal seal must be unavailable before the reveal gate; the world-end border must be unavailable before terminal readiness.

### Full Part 10 ledger

| Part 10 row | Exact stable sheet | Frames and dimensions | Current coverage | Next batch |
| --- | --- | --- | --- | --- |
| Early warning seal | cannibalism_early_warning_seal_sheet.dds | 8; 512x64 | frontline_hunger_seal is a plausible approved substitute only if the GUI owner accepts that exact semantic mapping | E14-ANIM-RUNTIME-01 or regenerate |
| Cult Cohesion emblem | cannibalism_cult_cohesion_emblem_sheet.dds | 8; 512x64 | cult_pressure_warning is a plausible warning-state substitute, not automatically accepted as the emblem | E14-ANIM-RUNTIME-01 or regenerate |
| Network threads | cannibalism_network_threads_sheet.dds | 12; final GUI width by 12 rows | Missing | E14-ANIM-GUI-01 |
| Island alert | cannibalism_island_alert_sheet.dds | 8; 512x64 | island_signal_card is a direct source candidate | E14-ANIM-RUNTIME-01 |
| Selected target card overlay | cannibalism_selected_target_overlay_sheet.dds | 6; final overlay width by 6 rows | Missing | E14-ANIM-GUI-01 |
| Critical Larder glow | cannibalism_critical_larder_glow_sheet.dds | 8; 512x64 | Missing | E14-ANIM-GUI-01 |
| Frenzy border | cannibalism_frenzy_border_sheet.dds | 8; final border width by 8 rows | Missing | E14-ANIM-GUI-01 |
| Warlord route emblem | cannibalism_warlord_route_emblem_sheet.dds | 8; 752x86 | Missing | E14-ANIM-ROUTE-01 |
| Ordinary portrait | gfx/leaders/014_cannibalism/hannibal_ordinary_sheet.dds | 12; 1872x210 | Missing | E14-POR-ORDINARY-01 |
| Unification seal | cannibalism_unification_seal_sheet.dds | 12; 1128x86 | Existing resonance seal is wrong size and frame count | E14-ANIM-ROUTE-01 |
| Ordinary terminal frame | cannibalism_ordinary_terminal_frame_sheet.dds | 12; final frame width by 12 rows | Existing world-end border is wrong size and frame count | E14-ANIM-TERMINAL-01 |
| Wendigo portrait | gfx/leaders/014_cannibalism/hannibal_wendigo_sheet.dds | 16; 2496x210 | Missing | E14-POR-WENDIGO-01 |
| Wendigo anchor pulse | cannibalism_wendigo_anchor_pulse_sheet.dds | 12; 768x64 | Missing | E14-ANIM-WENDIGO-01 |
| Wendigo terminal frame | cannibalism_wendigo_terminal_frame_sheet.dds | 12; final frame width by 12 rows | Missing | E14-ANIM-WENDIGO-01 |

All non-portrait animation DDS paths in the second table live under gfx/interface/animated/014_cannibalism/. Each also needs a same-stem _static.dds, separate generated or sourced frames, processed frames, PNG sheet, GIF, contact sheet, brief, frame plan, and manifest. UI-dependent widths are blocked until interface/014_cannibalism_frontline_hunger.gui freezes the actual rectangles. Do not synthesize these packages by transforming one retained still or by resizing one of the six source packages.

The source specification therefore remains eleven exact animation rows short unless the three plausible mappings are explicitly accepted. The other three retained custom packages are useful additional GUI art, not substitutes for rows with different dimensions, frame counts, or meaning.

## Static GUI art and runtime wiring

### GUI asset batches

All GUI art under gfx/interface/014_cannibalism/ is missing. Stable logical names can be reserved now; exact pixel sizes remain blocked on the final GUI layout.

| Batch | Required files or families | Size state |
| --- | --- | --- |
| E14-GUI-EARLY-01 | early_category_background.dds, field_hunger_frame.dds, field_hunger_fill.dds, command_integrity_frame.dds, command_integrity_fill.dds, cult_cohesion_slot.dds, state_card.dds, warning_seal.dds | Blocked on final rectangles |
| E14-GUI-NETWORK-01 | network_background.dds, five tab-state files, node_card.dds, target_country_frame.dds, target_state_frame.dds, node_port.dds, node_prison.dds, node_formation.dds, node_island.dds, node_rail.dds, node_warlord.dds, selected/locked/active/urgent/cleared overlays | Blocked on final rectangles |
| E14-GUI-CANNIBAL-01 | larder_meter.dds, frenzy_meter.dds, controlled_state_card.dds, recruitment_button states, raid_target_card.dds, network_alignment_seal.dds | Blocked on final rectangles |
| E14-GUI-REVEAL-01 | revealed_portrait_frame.dds, warlord_loyalty_card.dds, global_larder_meter.dds, network_reach_meter.dds, continental_target_card.dds, world_end_progress_frame.dds, unification_seal.dds | Blocked on final rectangles; reveal-gated |
| E14-GUI-WENDIGO-01 | transformed_portrait_frame.dds, anchor_card.dds, countdown_frame.dds, wendigo_unit_capacity.dds, terminal_warning_border.dds | Blocked on final rectangles; alternate-reveal-gated |

No fallback dimensions are authorized. The GUI owner must provide a dimension ledger before generation so the art is sliced once and the animation sheet widths are final.

### Registry and GUI ownership matrix

| Runtime surface | Required owner file | Current status | Wiring contract |
| --- | --- | --- | --- |
| Report/news sprites | interface/chaosx_pictures.gfx | No Event 014 aliases | Register each final path once; event picture mappings must select only phase-appropriate sprites. |
| Super-event sprites | interface/chaosx_super_events.gfx | No Event 014 aliases | Four distinct aliases, each gated by its branch and scale. |
| Event-specific icons and animations | interface/014_cannibalism.gfx | File missing | Register decisions, ideas, focus regular/shine sprites, GUI art, and all static/animated sheet pairs. |
| Achievement sprites | interface/chaosx_achievements.gfx | No current Event 014 aliases | Register all 54 current triplet files under the final achievement IDs. |
| Character/GUI portrait sprites | final character definitions plus interface/014_cannibalism.gfx | No current Event 014 wiring | Static character portrait and animated reveal-window sprites must resolve only after their gates. |
| Unit counters | interface/chaosx_subuniticons.gfx | No Event 014 aliases | Register medium and medium_white aliases with two frames only for implemented subunits. |
| Technology/equipment art | appropriate technology or equipment .gfx registry | No Event 014 aliases | Register only after final technology/equipment IDs exist. |
| GUI layout | interface/014_cannibalism_frontline_hunger.gui | File missing | Own all rectangles, textures, animation placements, and default-hidden states. |
| GUI script | common/scripted_guis/014_cannibalism_scripted_gui.txt | File missing | Own visibility and interaction gates; default state must be spoiler-safe. |

The shared registries chaosx_pictures.gfx, chaosx_super_events.gfx, chaosx_achievements.gfx, chaosx_characters.gfx, and chaosx_subuniticons.gfx contain no current Event 014 report, super-event, achievement, hidden-leader, or unit wiring.

## Anti-spoiler production contract

- Before public reveal, default GUI textures, event-picture fallbacks, scripted localisation, focus search labels, achievement list entries, super-event slots, flags, portraits, and sprite names exposed through player-facing debugging must not reveal the hidden leader's name or face.
- Ordinary pre-reveal art may show evidence, cells, uncertain coordination, blank frames, map threads, seals, or anonymous warlords. It may not show the final command portrait, personal mantle, unique scars, unified standards, or recognizable transformed identity.
- Reveal news, reveal super-event, ordinary animated portrait, unified flags, command window, and hidden-route achievements are reveal-gated.
- Wendigo portrait, transformed flag, anchor art, alternate terminal frame, and secret achievement art are alternate-reveal-gated.
- The stop-the-reveal achievement icon must show an unseen or unopened portrait frame and must not show the face.
- Internal filenames may remain explicit where needed for maintenance, but player-facing aliases should prefer neutral phrases such as revealed_command until the gate is open.

## Deleted-history evidence

Commit f2d7e448db94312955200d5ba7b0bd50228ae2b0, dated 2026-07-05, deleted an earlier Event 014 implementation. Among its deleted surfaces were:

- interface/014_cannibalism.gfx
- interface/014_cannibalism_frontline_hunger.gui
- common/scripted_guis/014_cannibalism_scripted_gui.txt
- twelve runtime DDS files for the six retained source animations
- twenty-four old decision/category DDS files
- four old super-event DDS files
- leader_CBL_warlord.dds and CBL_table_council.dds
- prior events, decisions, focuses, ideas, achievements, localisation, and country package files

Commit 1fb0617a4aa790301b0fd8ef6958ec44cc8e9961, dated 2026-07-06, deleted six root-size CBL/CBL_LAST_TABLE flag files listed in the flag section.

The current worktree separately marks all thirty-seven old focus DDS files as deleted. These deletions belong to the shared dirty worktree. This audit did not restore, rename, convert, or stage any of them.

Historical files may be inspected to recover registry syntax or dimensions. They must not be restored wholesale, treated as complete, or substituted for current assets without a current requirement-to-file review.

## Production order and dependency gates

1. Freeze four ledgers before large icon generation: final focus IDs, final idea IDs, final decision IDs, and final unit/technology IDs.
2. Freeze the GUI rectangle ledger before UI-dependent static art or animation sheets.
3. Produce E14-RPT-01, E14-NEWS-01, and E14-SUPER-01; these have stable dimensions and current exact directions.
4. Produce E14-POR-WARLORD-01 and the two flag batches. Confirm all tag and cosmetic-tag tokens before conversion.
5. Produce E14-POR-ORDINARY-01 and E14-POR-WENDIGO-01 as separate static-plus-animation packages; preserve the protected old portrait unchanged.
6. Produce E14-ACHIEVEMENT-01 from the exact eighteen Part 11 IDs.
7. Produce E14-IDEA-01 and E14-DECISION-01 after their gameplay ledgers are accepted.
8. Produce the three focus batches only from the final ID-to-art ledger.
9. Convert and wire E14-ANIM-RUNTIME-01, then create the remaining Part 10 animation batches with their exact frame counts and final GUI widths.
10. Produce static GUI art from the frozen rectangles, then wire GFX, GUI, and scripted-GUI visibility together.
11. Produce unit and technology art only for implemented IDs.
12. Rebuild docs/assets/014_cannibalism/manifest.md and a new gfx_handoff.md from the final live filesystem, including hashes, dimensions, compression, sprite aliases, GUI owners, and spoiler gates.

## Completion conditions for the asset package

Event 014 visual assets are not complete until:

- every current requirement has one exact file row, source package, final runtime file, and runtime owner;
- all ten reports, six news images, four super-event images, eight required warlord portraits, both static-and-animated leader forms, required flag families, final focus set, idea set, decision set, eighteen achievement triplets, required unit/technology art, GUI state set, and all fourteen specification animations are accounted for;
- the six retained source animations are converted and wired rather than merely listed as complete;
- all UI-dependent dimensions are taken from the final GUI rather than guessed;
- sprite registries contain no missing files or duplicate/stale aliases;
- reveal and alternate-reveal art cannot resolve before their gates;
- no asset is reused across icon types and no hidden fallback or silent old-file mapping is used;
- the top-level asset manifest describes the actual live filesystem.

No fallback, cross-icon reuse, silent restoration, or unapproved simplification is proposed in this map. The remaining blockers are explicit implementation-owned ID and GUI-dimension contracts.
