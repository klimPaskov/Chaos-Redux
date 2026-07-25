# IW-007 AGX/Frisia Focus Overlay Handoff

## Scope

This patch adds the accepted narrow IW-007 Frisia/AGX package lane inside the existing Event 006 full-framework focus tree.

It does not add a government route family, formable family, advisor, leader, or new art package.

## Changed files

- `common/national_focus/006_independence_wave_focus.txt`
- `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt`
- `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`

## Route coverage

| Focus id | Route role | Existing mechanic consumed |
| --- | --- | --- |
| `independence_wave_agx_chart_waterline_authority_focus` | Waterline opening | AGX waterline and coastal-security values, founding value bundle |
| `independence_wave_agx_bind_dikes_pumps_harbors_focus` | Port/island administration | AGX values, anchor-state infrastructure, administrative progress |
| `independence_wave_agx_integrate_coastal_guard_focus` | Coastal-maritime defense | AGX values, security progress, existing force-profile-compatible army/command rewards |
| `independence_wave_agx_codify_water_board_government_focus` | Constitutional, labor-council, or patron-client settlement | Existing AGX route-government flags and route helper predicates |
| `independence_wave_agx_settle_water_board_succession_focus` | Former-host settlement | Existing `independence_wave_agx_reconcile_water_board_records` completion flag and living-former-host trigger |
| `independence_wave_agx_open_north_sea_network_office_focus` | North Sea cooperation | Existing network-member flag, network standing, and league ledger values |
| `independence_wave_agx_mandate_north_sea_coastal_conference_focus` | Conference authorization | New narrow AGX foundation trigger mirrors the existing conference decision gate without paying or completing the decision |
| `independence_wave_agx_prepare_low_countries_dossier_focus` | Low Countries Federation handoff | Existing AGX conference completion, formable discovery flag, and Low Countries registry |

The branch is gated by `is_independence_wave_agx_package = yes` and starts from `independence_wave_prepare_capital_administration`.

The former-host path requires either no living former host or the existing `independence_wave_agx_host_records_settled` flag.

The conference focus requires stable AGX waterline values, recognition, network membership, the existing Low Countries candidate flag, and no client-route lock.

The paid `independence_wave_agx_convene_north_sea_coastal_conference` decision remains responsible for its strategic cost and 300-day duration.

## Icons and localisation

All eight focuses reuse registered generic Event 006 focus sprites: infrastructure authority, founding administration, army integration, constitutional state, former-host settlement, league congress, recognition diplomacy, and regional formable.

Each focus has a title, description, and effect tooltip in `006_independence_wave_wallonia_frisia_l_english.yml`.

No new asset request is required for this narrow overlay.

## Validation

`hoi4.focus_inspect` now reports 184 focuses and 184 resolved titles for `independence_wave_focus_tree`.

The post-patch inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f80a38fcb08f6deb2ca2aba5755f50cc7d2732b5cd41083a0a4986ae5d0604a5/b224766d325339e19fdf072b317d7cded9b9b9bff17eb470ca27eabd692dbc9b/focus-inspect.956a02f6d24f6ddb.json`.

`hoi4.focus_render` produced the post-patch HTML, SVG, JSON, source-map, and plan artifacts under the `6278773fb4e35ecc1332b0b434162c78261c01c0a2ef086a38c2baa1c046e2c6` render artifact.

Reference checks confirmed all eight focus title/description keys, all eight custom tooltip keys, all eight registered icon ids, the eight hidden-effect symbols, and `has_independence_wave_agx_north_sea_conference_foundation`.

The localisation file retains its UTF-8 BOM.

## Remaining route risks

The national tree still has the pre-existing 14 blocking layout diagnostics, including crossings and long connectors in the shared framework; this patch did not attempt the broader layout repair.

The AGX lane uses the existing shared network and formable systems, so final conference and federation consent checks remain downstream responsibilities of the decision and Form-03 packages.

No additional focus-level mutual exclusion was added because AGX route-government decisions are already mutually exclusive and the client-route lock is enforced by the existing conference gate.
