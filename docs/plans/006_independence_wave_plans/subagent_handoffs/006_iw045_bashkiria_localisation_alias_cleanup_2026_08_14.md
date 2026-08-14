# IW-045 Bashkiria localisation alias cleanup

Date: 2026-08-14

Scope: narrow localisation-only cleanup after the IW-045 decision canonicalization.

Changed file: `localisation/english/006_independence_wave_bashkiria_l_english.yml`.

Removed the four unconsumed project alias pairs `independence_wave_bsk_secure_oilfield_depots`, `independence_wave_bsk_register_community_compacts`, `independence_wave_bsk_establish_emergency_command`, and `independence_wave_bsk_open_volga_ural_corridor`.

The canonical decision IDs remain `independence_wave_bsk_secure_frontier_depots`, `independence_wave_bsk_integrate_frontier_guards`, `independence_wave_bsk_register_bashkir_communities`, `independence_wave_bsk_settle_former_host_ledgers`, `independence_wave_bsk_establish_frontier_emergency_command`, and `independence_wave_bsk_open_ural_network_corridor`, with their name and description keys intact.

Validation found the UTF-8 BOM, 22 decision name/description references, and zero missing localisation keys.

No gameplay, asset, character, central-attestation, Join, workbook, or runtime files were changed.

Remaining semantic aliases such as older idea names and route-consumer helper labels remain outside this narrow deletion because their ownership is not purely localisation-owned.
