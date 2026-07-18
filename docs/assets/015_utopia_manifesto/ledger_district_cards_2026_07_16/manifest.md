# Event 015 Ledger District Cards Asset Manifest

## Package scope

This package supplies the seven district-role cards and six district-state overlays required by the Event 015 Commonwealth Ledger. Every accepted asset has its own built-in ImageGen master and its own final runtime texture. No focus or decision artwork was reused, and no visible artwork was drawn or assembled by the local processing scripts.

Common record fields for every row:

- Related event id: 015, entry root chaosx.nr15.1.
- Related event slug: utopia_manifesto.
- Source mode: built-in ImageGen.
- Source author, source link, source date, and license: not applicable to generated fictional artwork. Exact ImageGen handles and saved-source provenance are recorded in metadata/source_provenance.json.
- Full generation prompt: prompts/district_card_prompts.md under the prompt id listed below.
- Era-fit note: fictional 1930s civic-planning imagery, matched to the quiet painted interface language of the Event 015 Ledger and period municipal records; no real historical scene or person is represented.
- Target sprite registry: interface/015_utopia_manifesto.gfx.
- Localisation key: not applicable; these are text-free scripted-GUI visual layers.
- Animation fields: not applicable; every asset is a single static frame.
- Status: complete. Source, processed PNG, runtime DDS, decoded verification, registration, GUI consumer, visibility binding, and native-size review all exist.

Package-relative source, processed, and decoded paths in the tables below resolve from docs/assets/015_utopia_manifesto/ledger_district_cards_2026_07_16/.

## District role cards

Asset type for every row: scripted-GUI district-role card. Target size: 300x96. GUI anchor: x 334, y 4 within `utopia_ledger_stores_panel`, the Stores/Settlements tab that owns live district presentation. The subdued left field preserves the Ledger text area while the right-weighted scene identifies the selected district role.

| Asset name / prompt id | Intended in-game use and visual note | Source PNG | Processed PNG | Final DDS | Sprite / GUI element | Status |
|---|---|---|---|---|---|---|
| utopia_ledger_district_role_market_garden / role_market_garden | Selected market-garden district; allotments, cold frames, cottages, and modest civic cultivation. | source_png/roles/utopia_ledger_district_role_market_garden_source.png | processed_png/roles/utopia_ledger_district_role_market_garden.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_market_garden.dds | GFX_utopia_ledger_district_role_market_garden / utopia_ledger_district_role_market_garden | complete |
| utopia_ledger_district_role_industrial_housing / role_industrial_housing | Selected industrial-housing district; dense row housing, workshop blocks, and sawtooth works. | source_png/roles/utopia_ledger_district_role_industrial_housing_source.png | processed_png/roles/utopia_ledger_district_role_industrial_housing.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_industrial_housing.dds | GFX_utopia_ledger_district_role_industrial_housing / utopia_ledger_district_role_industrial_housing | complete |
| utopia_ledger_district_role_rail_junction / role_rail_junction | Selected rail-junction district; converging rails, switches, depot, and semaphore infrastructure. | source_png/roles/utopia_ledger_district_role_rail_junction_source.png | processed_png/roles/utopia_ledger_district_role_rail_junction.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_rail_junction.dds | GFX_utopia_ledger_district_role_rail_junction / utopia_ledger_district_role_rail_junction | complete |
| utopia_ledger_district_role_port_town / role_port_town | Selected port-town district; quiet quay, warehouse, crane, and small working boats. | source_png/roles/utopia_ledger_district_role_port_town_source.png | processed_png/roles/utopia_ledger_district_role_port_town.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_port_town.dds | GFX_utopia_ledger_district_role_port_town / utopia_ledger_district_role_port_town | complete |
| utopia_ledger_district_role_research_town / role_research_town_edit | Selected research-town district; interwar laboratories, greenhouse, observatory dome, and weather mast. The accepted source is a precise ImageGen edit of this role's own independent draft. | source_png/roles/utopia_ledger_district_role_research_town_source.png | processed_png/roles/utopia_ledger_district_role_research_town.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_research_town.dds | GFX_utopia_ledger_district_role_research_town / utopia_ledger_district_role_research_town | complete |
| utopia_ledger_district_role_refugee_municipality / role_refugee_municipality | Selected refugee municipality; cottages, relief tents, clinic, water tower, and productive gardens without camp or prison imagery. | source_png/roles/utopia_ledger_district_role_refugee_municipality_source.png | processed_png/roles/utopia_ledger_district_role_refugee_municipality.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_refugee_municipality.dds | GFX_utopia_ledger_district_role_refugee_municipality / utopia_ledger_district_role_refugee_municipality | complete |
| utopia_ledger_district_role_inland_island_ring / role_inland_island_ring | Selected Inland Island ring district; concentric rail, greenbelt, civic works, and an enclosed central settlement. | source_png/roles/utopia_ledger_district_role_inland_island_ring_source.png | processed_png/roles/utopia_ledger_district_role_inland_island_ring.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_role_inland_island_ring.dds | GFX_utopia_ledger_district_role_inland_island_ring / utopia_ledger_district_role_inland_island_ring | complete |

Decoded verification PNGs use decoded_png/roles/<asset-name>.png and are pixel-identical to the corresponding processed PNG.

## District state overlays

Asset type for every row: scripted-GUI district-state overlay/badge. Target size: 48x48 with transparent unused canvas. GUI anchor: x 578, y 12 within `utopia_ledger_stores_panel`, the Stores/Settlements tab that owns live district presentation. Each badge has an independently generated material construction and silhouette so it remains distinguishable at native size without text.

| Asset name / prompt id | Intended in-game use and visual note | Source PNG | Processed PNG | Final DDS | Sprite / GUI element | Status |
|---|---|---|---|---|---|---|
| utopia_ledger_district_state_surveyed / state_surveyed | Surveyed state; compact theodolite and survey-board assembly. | source_png/states/utopia_ledger_district_state_surveyed_source.png | processed_png/states/utopia_ledger_district_state_surveyed.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_surveyed.dds | GFX_utopia_ledger_district_state_surveyed / utopia_ledger_district_state_surveyed | complete |
| utopia_ledger_district_state_planned / state_planned | Planned state; blank rolled plan and drafting-frame assembly, with no pseudo-writing. | source_png/states/utopia_ledger_district_state_planned_source.png | processed_png/states/utopia_ledger_district_state_planned.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_planned.dds | GFX_utopia_ledger_district_state_planned / utopia_ledger_district_state_planned | complete |
| utopia_ledger_district_state_building / state_building | Building state; timber scaffold and active municipal-work structure. | source_png/states/utopia_ledger_district_state_building_source.png | processed_png/states/utopia_ledger_district_state_building.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_building.dds | GFX_utopia_ledger_district_state_building / utopia_ledger_district_state_building | complete |
| utopia_ledger_district_state_blocked / state_blocked | Blocked state; broken bridge timbers, barricade, and warning lantern without a generic red-X symbol. | source_png/states/utopia_ledger_district_state_blocked_source.png | processed_png/states/utopia_ledger_district_state_blocked.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_blocked.dds | GFX_utopia_ledger_district_state_blocked / utopia_ledger_district_state_blocked | complete |
| utopia_ledger_district_state_complete / state_complete | Complete state; finished civic hall, ceremonial key, and grain sheaf. | source_png/states/utopia_ledger_district_state_complete_source.png | processed_png/states/utopia_ledger_district_state_complete.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_complete.dds | GFX_utopia_ledger_district_state_complete / utopia_ledger_district_state_complete | complete |
| utopia_ledger_district_state_disputed / state_disputed | Disputed state; torn blank charter, opposed cords, and two contrasting wax seals. | source_png/states/utopia_ledger_district_state_disputed_source.png | processed_png/states/utopia_ledger_district_state_disputed.png | gfx/interface/015_utopia_manifesto/ledger/utopia_ledger_district_state_disputed.dds | GFX_utopia_ledger_district_state_disputed / utopia_ledger_district_state_disputed | complete |

Decoded verification PNGs use decoded_png/states/<asset-name>.png and are pixel-identical to the corresponding processed PNG.

## Rejected source retained for provenance

The first research-town ImageGen draft is preserved at source_png/rejected/utopia_ledger_district_role_research_town_rejected_roof_number.png. A pale roof marking resembled the readable number 500, so it was rejected before processing and runtime conversion. Built-in ImageGen then removed only that marking from the same independent research-town master. The rejected draft is not referenced by the mod.

## Processing and review evidence

- tooling/process_district_cards.py performs only deterministic crop, uniform resize, mild image-wide grading, chroma removal for state masters, transparent padding, DDS serialization, and decode verification. It draws no visible art.
- Roles use an exact 25:8 centered cover crop followed by uniform scaling to 300x96. The retained source area is recorded per asset in metadata/processing_report.json; nonuniform stretch is false for every role.
- State subjects are uniformly contained within a 44x44 inner box and centered on a transparent 48x48 canvas. No state is stretched.
- Runtime format is one-level uncompressed 32-bit BGRA DDS with no mipmaps. Every decoded DDS is pixel-identical to its processed PNG.
- metadata/checksums.sha256 records the source, processed, decoded, runtime, documentation, contact-sheet, and validation hashes.
- validation/validation_report.json contains exact DDS-header, length, dimension, alpha, pixel-parity, geometry, uniqueness, visible-magenta, and live-wiring results.
- validation/native_size_visual_review.md records the per-asset visual review.

Review sheets:

- contact_sheets/district_roles_source_runtime_contact.png
- contact_sheets/district_roles_native_1x.png
- contact_sheets/district_states_source_runtime_contact.png
- contact_sheets/district_states_native_1x.png
- contact_sheets/district_states_nearest_4x.png

## Runtime integration

The exact sprite registrations and GUI consumers were already present when this bounded art package was produced and were audited read-only. The role cards occupy the shared x 334, y 4 slot; state badges occupy the shared x 578, y 12 slot. State and role selection is controlled by existing visibility bindings in common/scripted_guis/015_utopia_manifesto_scripted_gui.txt. See gfx_gui_handoff.md for the exact mapping.

No simplifications, fallback artwork, placeholder art, cross-role reuse, or unresolved asset blockers remain in this package.
