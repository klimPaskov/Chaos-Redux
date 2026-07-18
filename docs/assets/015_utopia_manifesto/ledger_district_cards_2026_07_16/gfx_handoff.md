# Event 015 Ledger District Card GFX and GUI Handoff

## Handoff status

The thirteen requested runtime textures are complete at the exact paths and sizes already reserved by the parent implementation. The existing sprite registrations, GUI icon consumers, and scripted-GUI visibility bindings were audited read-only and match every delivered filename. No GFX, GUI, gameplay, localisation, specification, or top-level authority file was edited by this asset package.

- Target sprite registry: interface/015_utopia_manifesto.gfx.
- GUI consumer: interface/015_utopia_manifesto_ledger.gui, inside `utopia_ledger_stores_panel` on the Stores/Settlements tab.
- Visibility owner: common/scripted_guis/015_utopia_manifesto_scripted_gui.txt.
- Related event: Event 015, Utopia Manifesto, entry root chaosx.nr15.1.
- Localisation keys: none; all assets are text-free visual layers.
- Naming or placement uncertainty: none.
- Blocked or needs-review assets: none.

## District role card mapping

All role textures are static 300x96 one-level uncompressed BGRA DDS files. Their GUI elements share position x 334, y 4 and alwaystransparent = yes. Existing visibility logic ensures that only the selected district role is shown.

| Final DDS path | Existing sprite name | Existing GUI element | Existing visibility binding |
|---|---|---|---|
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_market_garden.dds | GFX_utopia_ledger_district_role_market_garden | utopia_ledger_district_role_market_garden | utopia_ledger_district_role_market_garden_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_industrial_housing.dds | GFX_utopia_ledger_district_role_industrial_housing | utopia_ledger_district_role_industrial_housing | utopia_ledger_district_role_industrial_housing_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_rail_junction.dds | GFX_utopia_ledger_district_role_rail_junction | utopia_ledger_district_role_rail_junction | utopia_ledger_district_role_rail_junction_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_port_town.dds | GFX_utopia_ledger_district_role_port_town | utopia_ledger_district_role_port_town | utopia_ledger_district_role_port_town_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_research_town.dds | GFX_utopia_ledger_district_role_research_town | utopia_ledger_district_role_research_town | utopia_ledger_district_role_research_town_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_refugee_municipality.dds | GFX_utopia_ledger_district_role_refugee_municipality | utopia_ledger_district_role_refugee_municipality | utopia_ledger_district_role_refugee_municipality_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_inland_island_ring.dds | GFX_utopia_ledger_district_role_inland_island_ring | utopia_ledger_district_role_inland_island_ring | utopia_ledger_district_role_inland_island_ring_visible |

## District state overlay mapping

All state textures are static 48x48 one-level uncompressed BGRA DDS files with transparent unused canvas. Their GUI elements share position x 578, y 12 and alwaystransparent = yes. Existing visibility logic resolves the current state and its precedence.

| Final DDS path | Existing sprite name | Existing GUI element | Existing visibility binding |
|---|---|---|---|
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_surveyed.dds | GFX_utopia_ledger_district_state_surveyed | utopia_ledger_district_state_surveyed | utopia_ledger_district_state_surveyed_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_planned.dds | GFX_utopia_ledger_district_state_planned | utopia_ledger_district_state_planned | utopia_ledger_district_state_planned_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_building.dds | GFX_utopia_ledger_district_state_building | utopia_ledger_district_state_building | utopia_ledger_district_state_building_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_blocked.dds | GFX_utopia_ledger_district_state_blocked | utopia_ledger_district_state_blocked | utopia_ledger_district_state_blocked_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_complete.dds | GFX_utopia_ledger_district_state_complete | utopia_ledger_district_state_complete | utopia_ledger_district_state_complete_visible |
| gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_disputed.dds | GFX_utopia_ledger_district_state_disputed | utopia_ledger_district_state_disputed | utopia_ledger_district_state_disputed_visible |

## Existing registration shape

The existing registry uses one spriteType per texture with the stable sprite name and direct event-scoped texture path. No new registry file is needed. The existing role and state GUI iconType blocks reference those names directly and require no scaling fields because the textures are delivered at native size.

## Review and validation

- Source-to-runtime and native-size review sheets are in contact_sheets/.
- Exact source, processed, decoded, and runtime hashes are in metadata/checksums.sha256.
- metadata/processing_report.json records the aspect-preserving fit and DDS decode parity for every texture.
- validation/validation_report.json records the read-only registration, GUI-consumer, and visibility-binding checks.
- validation/native_size_visual_review.md records the final human review, including the research-town rejection and corrected source.

The package is ready for integration without filename changes or follow-up art decisions.
