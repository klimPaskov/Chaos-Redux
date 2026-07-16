# Event 006 Rhineland and Bavaria GFX handoff

This file maps the 26 completed runtime assets to the exact sprite names expected by `interface/006_independence_wave_rhineland_bavaria_assets.gfx`. The asset producer did not edit that interface file or any gameplay consumer. The main agent owns final registration and consumer wiring.

## Focus icons

| Focus consumer | Base sprite | Shine sprite | Runtime DDS |
| --- | --- | --- | --- |
| `independence_wave_rhi_establish_corridor_authority_focus` | `GFX_goal_independence_wave_rhi_establish_corridor_authority` | `GFX_goal_independence_wave_rhi_establish_corridor_authority_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_establish_corridor_authority.dds` |
| `independence_wave_rhi_unify_rail_dispatch_focus` | `GFX_goal_independence_wave_rhi_unify_rail_dispatch` | `GFX_goal_independence_wave_rhi_unify_rail_dispatch_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_unify_rail_dispatch.dds` |
| `independence_wave_rhi_arm_customs_guard_focus` | `GFX_goal_independence_wave_rhi_arm_customs_guard` | `GFX_goal_independence_wave_rhi_arm_customs_guard_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_arm_customs_guard.dds` |
| `independence_wave_rhi_secure_industrial_belt_focus` | `GFX_goal_independence_wave_rhi_secure_industrial_belt` | `GFX_goal_independence_wave_rhi_secure_industrial_belt_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_secure_industrial_belt.dds` |
| `independence_wave_rhi_ratify_host_transit_compact_focus` | `GFX_goal_independence_wave_rhi_ratify_host_transit_compact` | `GFX_goal_independence_wave_rhi_ratify_host_transit_compact_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_ratify_host_transit_compact.dds` |
| `independence_wave_rhi_proclaim_neutral_corridor_focus` | `GFX_goal_independence_wave_rhi_proclaim_neutral_corridor` | `GFX_goal_independence_wave_rhi_proclaim_neutral_corridor_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_proclaim_neutral_corridor.dds` |
| `independence_wave_rhi_charter_network_transit_office_focus` | `GFX_goal_independence_wave_rhi_charter_network_transit_office` | `GFX_goal_independence_wave_rhi_charter_network_transit_office_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_charter_network_transit_office.dds` |
| `independence_wave_rhi_authorize_form04_delegation_focus` | `GFX_goal_independence_wave_rhi_authorize_form04_delegation` | `GFX_goal_independence_wave_rhi_authorize_form04_delegation_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_authorize_form04_delegation.dds` |
| `independence_wave_bay_broker_civic_settlement_focus` | `GFX_goal_independence_wave_bay_broker_civic_settlement` | `GFX_goal_independence_wave_bay_broker_civic_settlement_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_broker_civic_settlement.dds` |
| `independence_wave_bay_reconcile_landesbank_accounts_focus` | `GFX_goal_independence_wave_bay_reconcile_landesbank_accounts` | `GFX_goal_independence_wave_bay_reconcile_landesbank_accounts_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_reconcile_landesbank_accounts.dds` |
| `independence_wave_bay_bind_rail_and_pass_authorities_focus` | `GFX_goal_independence_wave_bay_bind_rail_and_pass_authorities` | `GFX_goal_independence_wave_bay_bind_rail_and_pass_authorities_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_bind_rail_and_pass_authorities.dds` |
| `independence_wave_bay_seat_landtag_and_court_focus` | `GFX_goal_independence_wave_bay_seat_landtag_and_court` | `GFX_goal_independence_wave_bay_seat_landtag_and_court_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_seat_landtag_and_court.dds` |
| `independence_wave_bay_entrust_mountain_guardians_focus` | `GFX_goal_independence_wave_bay_entrust_mountain_guardians` | `GFX_goal_independence_wave_bay_entrust_mountain_guardians_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_entrust_mountain_guardians.dds` |
| `independence_wave_bay_open_alpine_network_office_focus` | `GFX_goal_independence_wave_bay_open_alpine_network_office` | `GFX_goal_independence_wave_bay_open_alpine_network_office_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_open_alpine_network_office.dds` |
| `independence_wave_bay_convene_south_german_settlement_focus` | `GFX_goal_independence_wave_bay_convene_south_german_settlement` | `GFX_goal_independence_wave_bay_convene_south_german_settlement_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_convene_south_german_settlement.dds` |
| `independence_wave_bay_ratify_german_host_compact_focus` | `GFX_goal_independence_wave_bay_ratify_german_host_compact` | `GFX_goal_independence_wave_bay_ratify_german_host_compact_shine` | `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_ratify_german_host_compact.dds` |

Focus texture dimensions are 94x86. The main agent should point each focus `icon =` field to the base sprite above and retain the matching shine registration in the owning interface file.

## Route-institution idea icons

| Idea token | Expected picture value | Sprite | Runtime DDS |
| --- | --- | --- | --- |
| `rhi_constitutional_river_compact` | `rhi_constitutional_river_compact` | `GFX_idea_rhi_constitutional_river_compact` | `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_rhi_constitutional_river_compact.dds` |
| `rhi_workers_rhine_charter` | `rhi_workers_rhine_charter` | `GFX_idea_rhi_workers_rhine_charter` | `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_rhi_workers_rhine_charter.dds` |
| `rhi_emergency_corridor_command` | `rhi_emergency_corridor_command` | `GFX_idea_rhi_emergency_corridor_command` | `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_rhi_emergency_corridor_command.dds` |
| `rhi_patron_transit_mandate` | `rhi_patron_transit_mandate` | `GFX_idea_rhi_patron_transit_mandate` | `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_rhi_patron_transit_mandate.dds` |
| `bay_constitutional_state_compact` | `bay_constitutional_state_compact` | `GFX_idea_bay_constitutional_state_compact` | `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_bay_constitutional_state_compact.dds` |
| `bay_workers_district_charter` | `bay_workers_district_charter` | `GFX_idea_bay_workers_district_charter` | `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_bay_workers_district_charter.dds` |
| `bay_restoration_court_settlement` | `bay_restoration_court_settlement` | `GFX_idea_bay_restoration_court_settlement` | `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_bay_restoration_court_settlement.dds` |
| `bay_emergency_mountain_guardians` | `bay_emergency_mountain_guardians` | `GFX_idea_bay_emergency_mountain_guardians` | `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_bay_emergency_mountain_guardians.dds` |

Idea texture dimensions are 64x64. The main agent should set each idea's `picture =` value to the token shown above; HOI4 resolves it to the listed `GFX_idea_<token>` sprite.

## Report-event pictures

| Intended consumer | Sprite | Runtime DDS |
| --- | --- | --- |
| RHI corridor incident report-event slot | `GFX_report_event_006_rhi_corridor_incidents` | `gfx/event_pictures/006_independence_wave/rhineland_bavaria/report_event_006_rhi_corridor_incidents.dds` |
| BAY state incident report-event slot | `GFX_report_event_006_bay_state_incidents` | `gfx/event_pictures/006_independence_wave/rhineland_bavaria/report_event_006_bay_state_incidents.dds` |

Report-event texture dimensions are 210x176. The main agent should use the exact `GFX_report_event_006_...` sprite in the relevant event `picture =` field.

## Review and validation evidence

- Producer and parent visual review: PASS across all five package contact sheets.
- All 26 DDS files: valid legacy uncompressed 32-bit BGRA, correct dimensions and alpha, exact expected file length.
- DDS-to-processed-PNG round trip: pixel-identical for all 26 assets.
- Source uniqueness: 26 unique SHA-256 values; minimum pairwise perceptual-hash distance 21.
- Evidence: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/validation/asset_validation.json`.
- Full prompts, hashes, provenance, processing commands, and per-asset review status: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/manifest.md`.

## Main-agent wiring ownership

The main agent must confirm the sprite registrations and all live consumers in the focus, idea, and event files. Any later sprite-name or path change must be reflected in both the owning interface file and this package documentation. No fallback asset is authorized or required. The approved portraits `portrait_BAY_rupprecht_of_bavaria.dds` and `portrait_RHI_josef_friedrich_matthes.dds` were not touched.

## Blockers

None in the asset files. Runtime wiring remains the main agent's responsibility.
