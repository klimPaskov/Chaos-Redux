# Primary CBRN Graphics Handoff — 2026-10-06

This handoff covers the primary CBRN icon repair package in `docs/assets/chaos_warfare_system/2026-10-06_gfx_primary/`. Its runtime inventory is in `manifest.md`, with machine-readable hashes and strict DDS decode evidence in `notes/full_runtime_dds_manifest.json`.

The package contains 44 newly written or repaired runtime DDS outputs. Parent review approved each visual tranche before promotion. Fourteen earlier flat glyph DDS files were already promoted and committed by the parent in `0154ecfd7`, `a52882984`, and `1384e2132`; I did not rewrite them. The CBRN trait family was produced by the separate `cbrn_trait_art` owner, parent-reviewed, and its four shared-registry paths are applied; its focused commit is pending publication and is outside this 44-DDS manifest. Historical advisor portraits remain with their portrait owner, and counters/texticons remain with `cbrn_tech_counter_art`; those are separate owner handoffs, not pending work in this primary package.

## Earlier parent-committed glyph tranche

The following 14 runtime files are separate from the 44 outputs in this package manifest and were not rewritten here:

- `gfx/interface/decisions/stage_6_chemical_delivery/battlefield_operations/cbrn_battlefield_cylinder_release.dds`
- `gfx/interface/decisions/stage_6_chemical_delivery/battlefield_operations/cbrn_battlefield_projector_barrage.dds`
- `gfx/interface/decisions/stage_6_chemical_delivery/battlefield_operations/cbrn_battlefield_artillery_fire_plan.dds`
- `gfx/interface/decisions/stage_6_chemical_delivery/battlefield_operations/cbrn_battlefield_armored_delivery.dds`
- `gfx/interface/raids/stage_6_chemical_delivery/cbrn_chemical_air_operation.dds`
- `gfx/interface/state_modifiers/cbrn_occupation/modifiers_cbrn_nerve_suppression_active.dds`
- `gfx/interface/state_modifiers/cbrn_occupation/modifiers_cbrn_nerve_suppression_trauma.dds`
- `gfx/interface/state_modifiers/cbrn_occupation/modifiers_cbrn_occupation_backlash.dds`
- `gfx/interface/state_modifiers/cbrn_occupation/modifiers_cbrn_occupation_state_sealed.dds`
- `gfx/interface/ideas/stage_2_protective_equipment/cbrn_chemical_alarm_disruption.dds`
- `gfx/interface/ideas/stage_2_protective_equipment/cbrn_civilian_shelter_disruption.dds`
- `gfx/interface/ideas/stage_2_protective_equipment/cbrn_hospitals_utilities_protected.dds`
- `gfx/interface/ideas/stage_2_protective_equipment/cbrn_industry_kept_operating.dds`
- `gfx/interface/ideas/stage_2_protective_equipment/cbrn_emergency_distribution_disruption.dds`

## Assigned plan-row inventory

| Owner table | Findings | Result |
|---|---:|---|
| `biowarfare` | 7 | Four biological bomb line drawings, the isolated painted cloning vat on transparency, and separate sarin/soman program blueprints are complete. The cloning vat is the deliberate painted-object exception because that row explicitly requested it. The program sprites now point to their dedicated `sp_cw_sarin_program.dds` and `sp_cw_soman_program.dds` textures; the sarin and soman bomb sprites remain on their bomb textures. |
| `cbrn_battlefield_operations` | 5 | Four 32×32 map glyphs were parent-committed. The unused cycle-agent sprite and its dedicated DDS were removed during parent integration after a repository-wide consumer check found no other use. |
| `cbrn_chemical_delivery` | 1 | The 32×32 flat gold aircraft-and-plume raid glyph was parent-committed. |
| `cbrn_diplomacy` | 1 | The inspection-document icon is scaled to 29×29 inside its existing 32×32 DDS, centered with a clear one-pixel edge margin. Parent approved the crop. |
| `cbrn_doctrine` | 8 | Four ten-frame reward strips, the paired 106×83 delivery-integration milestone, the 64×64 chemical-suppression doctrine icon, and both 32×32 decision glyphs are complete and parent-approved. |
| `cbrn_mio_industry` | 10 | Nine distinct 48×48 payload badges are complete, and the incapacitating-air payload was recentered. The dedicated `interface/cbrn_mio_industry.gfx` now points each agent sprite at its distinct DDS. |
| `cbrn_occupation` | 4 | Four flat 32×32 state-modifier glyphs were parent-committed. |
| `cbrn_project_equipment` | 1 | The sealed steel-blue crew module with a short flamethrower projector is complete at 56×42. Parent approved it. |
| `cbrn_protection` | 6 | Five flat 32×32 protection modifiers were parent-committed. The vehicle-overpressure icon was regenerated without its neon outline or window halo and installed at 64×64. |
| `cbrn_special_projects` | 8 | Four mechanical projects and four medical projects are complete as transparent white/grey blueprint drawings at 161×98. The four biological bomb drawings are listed under `biowarfare`. |
| `shared_chaosx_ability` | 8 | Three chemical attack variants and five CBRN operational abilities are complete as transparent 34×33 bronze/gold reliefs at their existing shared-GFX consumers. |
| `shared_chaosx_traits` | 1 CBRN family row | The five CBRN commander/veteran traits and related variants were produced by the separate `cbrn_trait_art` owner, parent-reviewed, and integrated through four shared-registry path updates. Those DDS files are not included in this primary package manifest. |
| `shared_chaosx_achievements` | 0 CBRN-specific plan rows | The current plan table contains no CBRN achievement finding. Per the parent addendum, all 13 active Chaos Warfare achievement triplets were audited in place; the parent reviewed their native and 4× sheets and accepted the supplied layers without art changes. The two unsupported outcomes remain unregistered and blocked. |

The eight `cbrn_special_projects` plan rows are `sp_cbrn_mechanized_smoke_screens`, `sp_cbrn_collective_protection_systems`, `sp_cbrn_self_renewing_filters`, `sp_cbrn_phantom_mist`, `sp_cbrn_mass_vaccine_production`, `sp_cbrn_field_antibiotics`, `sp_cbrn_regenerative_serum`, and `sp_cbrn_broad_spectrum_antiserum`. The seven `biowarfare` rows are four distinct biological bombs, `sp_mengele_cloning`, and the separate `sp_cw_sarin_program` and `sp_cw_soman_program` blueprints. These are plan-listed repairs, not additional design scope.

## Exact runtime output set

The complete path, target dimensions, SHA-256, and processed PNG path for each of the 44 outputs are in `docs/assets/chaos_warfare_system/2026-10-06_gfx_primary/manifest.md`. The families are four doctrine strips, ten MIO badges, fifteen special-project icons, eight ability icons, and seven small repairs. Every listed DDS was strictly decoded and matched its processed PNG pixel for pixel.

The four doctrine reward-strip runtime paths are the existing unprefixed consumers:

- `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/hazard_assault_reward_strip.dds`
- `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/toxic_armor_reward_strip.dds`
- `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/contaminant_fire_reward_strip.dds`
- `gfx/interface/doctrines/rewards/stage_5_chaos_warfare/integrated_command_reward_strip.dds`

The earlier unconsumed `cbrn_doctrine_*.dds` candidate duplicates were removed after the exact `interface/cbrn_doctrine.gfx` texture paths were re-read. Their correction record and preserved candidate hashes are in `notes/doctrine_texture_path_correction.md` and its companion JSON files.

The seven small repairs are installed at these exact existing consumers:

- `gfx/interface/decisions/cbrn_diplomacy/decision_cbrn_demand_inspections.dds`
- `gfx/interface/doctrines/milestones/stage_5_chaos_warfare/delivery_integration.dds`
- `gfx/interface/doctrines/icons/chaos_warfare_doctrine_style/doctrine_toxic_armored_warfare.dds`
- `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_convene_institutional_review.dds`
- `gfx/interface/decisions/stage_5_chaos_warfare/cbrn_assign_decontamination_corridor.dds`
- `gfx/interface/equipmentdesigner/tanks/modules/tank_module_cbrn_sealed_flamethrower_crew_module.dds`
- `gfx/interface/technologies/stage_2_protective_equipment/vehicle_overpressure_and_sealed_compartments.dds`

## GFX wiring boundary

I edited only the dedicated `interface/cbrn_mio_industry.gfx` file to give the nine agent-payload sprites distinct texture paths. The shared ability definitions already pointed at the exact DDS consumers, so `interface/chaosx_ability.gfx` was not changed.

Parent integration now maps `GFX_sp_cw_sarin_program` and `GFX_sp_cw_soman_program` to their new dedicated program DDS files while preserving `GFX_sp_sarin_bomb` and `GFX_sp_soman_bomb` on their bomb files. Parent integration also removed the orphan `GFX_decision_cbrn_battlefield_cycle_agent` definition from `interface/cbrn_battlefield_operations.gfx` and its former texture `gfx/interface/decisions/stage_6_chemical_delivery/battlefield_operations/cbrn_battlefield_cycle_agent.dds` after confirming there is no other consumer. Those parent edits are visible in the current tree but are not part of my changed-file list.

No other shared `.gfx`, gameplay, localisation, focus, event, AI, GUI, spreadsheet, or counter files were edited by this subagent.

## Achievement triplet audit

The current runtime registry contains these 13 active IDs: `chaos_warfare_masks_before_guns`, `chaos_warfare_prepared_army`, `chaos_warfare_poisoned_victory`, `chaos_warfare_clean_hands_dirty_work`, `chaos_warfare_evidence_survives`, `chaos_warfare_quarantine_without_collapse`, `chaos_warfare_arsenal_dismantled`, `chaos_warfare_terminal_contagion`, `chaos_warfare_mask_for_every_door`, `chaos_warfare_weapon_turns_home`, `chaos_warfare_first_user_pays`, `chaos_warfare_air_still_breathable`, and `chaos_warfare_antidote_arrived`.

All 39 registered DDS states exist, strictly decode as 64×64, and show distinct unlocked, grey, and not-eligible states. Every not-eligible state has the same visible red-cross footprint. The native and 4× runtime sheets are `contact_sheets/cbrn_achievement_triplets_native.png` and `contact_sheets/cbrn_achievement_triplets_4x.png`; detailed per-file hashes and state metrics are in `notes/cbrn_achievement_triplet_audit.json`. The parent reviewed the triplets at native and 4× and accepted reuse without art changes.

The existing `chaos_warfare_no_wind_is_friendly` and `chaos_warfare_unbroken_supply_corridor` DDS triplets are present on disk but have no achievement definitions or sprite registrations. They remain blocked because their exact outcomes are unsupported; their art was not generated or modified.

## Review evidence and known rejected candidates

Native and 4× family sheets are under `docs/assets/chaos_warfare_system/2026-10-06_gfx_primary/contact_sheets/`. Per-family alpha, source-path, and round-trip evidence is under `notes/`; original generation prompts are under `prompts/`; raw ImageGen output and untouched DDS-derived inputs are under `source_png/`.

The first delivery-integration sheet incorrectly showed the second state in color. It is retained only as rejected review evidence at `contact_sheets/cbrn_doctrine_milestone_4x.png`. The final runtime DDS pair is shown from a strict DDS decode at `contact_sheets/cbrn_doctrine_milestone_dds_decoded_native.png` and `contact_sheets/cbrn_doctrine_milestone_dds_decoded_4x.png`; the second state is fully grayscale and has identical alpha geometry to the color state.

The first aircraft raid-icon source was rejected because it contained an opaque checkerboard; that source remains as `source_png/GFX_raid_type_icon_cbrn_chemical_air_operation.native.png`. The successful native-alpha ImageGen edit is preserved as `source_png/GFX_raid_type_icon_cbrn_chemical_air_operation.imagegen_edit.png`, with its alpha check in `notes/alpha_air_operation.json`.

The scale-only suppression crop, the first module candidate with a conventional cannon, the first vehicle edit with visible crew, and the first decision candidate grid were not promoted. Their sources or review evidence remain in the package where applicable. The final suppression and vehicle DDS files match the parent-approved warm vertical tank/flame and plain painted armored-truck previews.

## Validation and limits

All 44 runtime DDS outputs were strictly decoded at their target dimensions and are pixel-identical to the processed PNGs. The delivery-integration pair is 212×83 with two 106×83 states; the second frame has zero non-grayscale pixels and exactly matches frame-one alpha. The achievement audit is read-only and preserves the supplied state layers.

The connected HOI4 MCP inventory exposed no GFX/asset-render route. No in-game or engine render evidence is claimed; review evidence consists of the inspected canonical reference families, target-size native and 4× sheets, exact current `.gfx` paths, and strict DDS round-trips.

This subagent did not commit. The parent owns the primary-package commit and final integration. The separate trait package is produced and reviewed, with its focused commit pending publication; portrait work remains with its portrait owner, and counter/texticon outputs remain with `cbrn_tech_counter_art`.

## Skills used

This package followed `chaos-redux-event-assets`, `chaos-redux-subagents`, and the official `imagegen` skill. No skill was created or updated.
