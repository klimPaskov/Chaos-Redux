# Event 015 Decision and Idea Icon Regeneration Handoff

Date: 2026-07-01
Subagent scope: runtime decision/category icons, runtime idea icons, matching asset-package source/processed/DDS copies, contact sheets, and this handoff.

## Source Mode and Process

Used the official imagegen workflow with flat `#00ff00` chroma-key backgrounds, then removed the chroma key locally before final resizing and DDS export.

Imagegen evidence saved in the package:

- `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_decision_atlas_source.png`
- `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_idea_atlas_01_source.png`
- `docs/assets/015_utopia_manifesto/source_png/decision_idea_regenerated_imagegen_idea_atlas_02_source.png`

One atlas cell for `idea_utopia_common_stores_unproven` produced an explicit question-mark prop, so that icon was replaced with a separate imagegen-generated source saved as:

- `docs/assets/015_utopia_manifesto/source_png/idea_utopia_common_stores_unproven_source.png`

Local processing was limited to atlas slicing, chroma-key removal through the installed imagegen helper, transparent crop/fitting, restrained dark outline and drop shadow, final resizing, contact sheet creation, and package/runtime DDS export. No final icon is a primitive local drawing or a resized focus icon.

## Runtime DDS Files

Decision/category icons regenerated at 32x32:

- `gfx/interface/decisions/015_utopia_manifesto/decision_category_utopia_league.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_category_utopia_ledger.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_boundary_arbitration.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_boundary_wardens.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_collect_petitions.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_common_administration.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_common_storehouse.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_fund_apprenticeships.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_guard_shore.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_household_census.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_household_guard.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_just_cause_review.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_league_aid_corridor.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_local_households.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_local_store.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_mark_needed_district.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_open_stores.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_recognize_friend.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_renunciation_vote.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_rural_rotation.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_send_magistrates.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_settlement_charter.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_storehouse_aid.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_storehouse_audit.dds`
- `gfx/interface/decisions/015_utopia_manifesto/decision_utopia_urgent_service.dds`

Idea icons regenerated at 64x64:

- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_arbitration_tables.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_civic_wardens.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_common_administration.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_common_stores_unproven.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_common_store_network.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_compulsory_assignments.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_empty_stores.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_feared_doctrine.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_foreign_laughter.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_found_manifesto.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_guilds.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_guild_congress.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_household_councils.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_household_guard.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_island_discipline.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_league_of_need.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_living_humanism.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_marked_bounds.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_marked_bounds_doctrine.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_necessary_commonwealth.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_needful_land.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_new_utopia.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_paper_utopia.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_public_storehouses.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_storekeeper_commission.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_store_state.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_unproven_common_stores.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_useful_arts.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_utopian_league.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_vocation_accord.dds`
- `gfx/interface/ideas/015_utopia_manifesto/idea_utopia_vocation_confusion.dds`

## Asset Package Copies

For each regenerated stem, matching files were written as:

- `docs/assets/015_utopia_manifesto/source_png/<stem>_source.png`
- `docs/assets/015_utopia_manifesto/processed_png/<stem>.png`
- `docs/assets/015_utopia_manifesto/dds/<stem>.dds`

Contact sheets:

- `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_decisions.png`
- `docs/assets/015_utopia_manifesto/contact_sheets/decision_idea_regenerated_imagegen_contact_ideas.png`

Manifest note:

- `docs/assets/015_utopia_manifesto/manifest.md`

## Validation

- Runtime decision/category DDS count: 25.
- Runtime idea DDS count: 31.
- All runtime decision/category DDS files are exactly 32x32.
- All runtime idea DDS files are exactly 64x64.
- Runtime DDS corner alpha check passed for all regenerated icons.
- Opaque near-white canvas check found no icon with more than 20 percent opaque near-white pixels.
- Contact sheets exist and were visually reviewed on checker backgrounds.
- Visual review found no obvious opaque white square backgrounds, no fake checkerboard, no visible chroma-key edge remnants, and no major misalignment.

## Blockers

None.

## Out of Scope

No `.gfx`, `.gui`, gameplay/script, localisation, focus icon, achievement, flag, audio, spreadsheet, or animation files were intentionally edited by this pass.
