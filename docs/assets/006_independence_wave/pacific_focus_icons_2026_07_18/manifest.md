# Event 006 Pacific focus-icon family manifest

Status: complete asset tranche; parent-owned `.gfx` registration and focus-reference wiring completed in the shared workspace
Production date: 2026-07-18
Asset type: national focus icons
Scope: 7 HBX California and 7 HAW Hawaiʻi icons only
Source mode: built-in Codex ImageGen, one distinct generation per icon, with flat `#00ff00` chroma-key removal
Target size: `94x86` native focus icon
Reference: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png` (16 vanilla focus references inspected; reference family uses centered silhouette, transparent corners, metal/enamel depth, and warm/cool contrast)

## Requirement coverage

Every requested focus has a retained ImageGen source PNG, processed transparent PNG, final uncompressed BGRA DDS, source/final hashes, native-size review, and enlarged review. The current Pacific focus implementation now resolves to these exact IDs through the parent-owned `interface/006_independence_wave_pacific_focus_icons.gfx`; this package did not edit focus scripts or `.gfx` files.

| Focus family | Sprite ID | Source PNG | Processed PNG | Runtime DDS |
|---|---|---|---|---|
| HBX screen federal arsenals | `GFX_goal_independence_wave_hbx_screen_federal_arsenals` | `source_png/focuses/goal_independence_wave_hbx_screen_federal_arsenals_source.png` | `processed_png/focuses/goal_independence_wave_hbx_screen_federal_arsenals.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_screen_federal_arsenals.dds` |
| HBX reopen coastal supply bureaus | `GFX_goal_independence_wave_hbx_reopen_coastal_supply_bureaus` | `source_png/focuses/goal_independence_wave_hbx_reopen_coastal_supply_bureaus_source.png` | `processed_png/focuses/goal_independence_wave_hbx_reopen_coastal_supply_bureaus.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_reopen_coastal_supply_bureaus.dds` |
| HBX seat Sacramento civic convention | `GFX_goal_independence_wave_hbx_seat_sacramento_civic_convention` | `source_png/focuses/goal_independence_wave_hbx_seat_sacramento_civic_convention_source.png` | `processed_png/focuses/goal_independence_wave_hbx_seat_sacramento_civic_convention.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_seat_sacramento_civic_convention.dds` |
| HBX bind ports, factories, and guard | `GFX_goal_independence_wave_hbx_bind_ports_factories_and_guard` | `source_png/focuses/goal_independence_wave_hbx_bind_ports_factories_and_guard_source.png` | `processed_png/focuses/goal_independence_wave_hbx_bind_ports_factories_and_guard.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_bind_ports_factories_and_guard.dds` |
| HBX settle federal asset ledger | `GFX_goal_independence_wave_hbx_settle_federal_asset_ledger` | `source_png/focuses/goal_independence_wave_hbx_settle_federal_asset_ledger_source.png` | `processed_png/focuses/goal_independence_wave_hbx_settle_federal_asset_ledger.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_settle_federal_asset_ledger.dds` |
| HBX charter Pacific procurement board | `GFX_goal_independence_wave_hbx_charter_pacific_procurement_board` | `source_png/focuses/goal_independence_wave_hbx_charter_pacific_procurement_board_source.png` | `processed_png/focuses/goal_independence_wave_hbx_charter_pacific_procurement_board.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_charter_pacific_procurement_board.dds` |
| HBX convene Pacific maritime congress | `GFX_goal_independence_wave_hbx_convene_pacific_maritime_congress` | `source_png/focuses/goal_independence_wave_hbx_convene_pacific_maritime_congress_source.png` | `processed_png/focuses/goal_independence_wave_hbx_convene_pacific_maritime_congress.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_hbx_convene_pacific_maritime_congress.dds` |
| HAW reconcile shipping registers | `GFX_goal_independence_wave_haw_reconcile_shipping_registers` | `source_png/focuses/goal_independence_wave_haw_reconcile_shipping_registers_source.png` | `processed_png/focuses/goal_independence_wave_haw_reconcile_shipping_registers.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_reconcile_shipping_registers.dds` |
| HAW organize island coastwatch | `GFX_goal_independence_wave_haw_organize_island_coastwatch` | `source_png/focuses/goal_independence_wave_haw_organize_island_coastwatch_source.png` | `processed_png/focuses/goal_independence_wave_haw_organize_island_coastwatch.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_organize_island_coastwatch.dds` |
| HAW seat island government compact | `GFX_goal_independence_wave_haw_seat_island_government_compact` | `source_png/focuses/goal_independence_wave_haw_seat_island_government_compact_source.png` | `processed_png/focuses/goal_independence_wave_haw_seat_island_government_compact.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_seat_island_government_compact.dds` |
| HAW bind shipping, supply, and coastwatch | `GFX_goal_independence_wave_haw_bind_shipping_supply_and_coastwatch` | `source_png/focuses/goal_independence_wave_haw_bind_shipping_supply_and_coastwatch_source.png` | `processed_png/focuses/goal_independence_wave_haw_bind_shipping_supply_and_coastwatch.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_bind_shipping_supply_and_coastwatch.dds` |
| HAW settle base and property accounts | `GFX_goal_independence_wave_haw_settle_base_and_property_accounts` | `source_png/focuses/goal_independence_wave_haw_settle_base_and_property_accounts_source.png` | `processed_png/focuses/goal_independence_wave_haw_settle_base_and_property_accounts.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_settle_base_and_property_accounts.dds` |
| HAW ratify autonomous Pacific mandate | `GFX_goal_independence_wave_haw_ratify_autonomous_pacific_mandate` | `source_png/focuses/goal_independence_wave_haw_ratify_autonomous_pacific_mandate_source.png` | `processed_png/focuses/goal_independence_wave_haw_ratify_autonomous_pacific_mandate.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_ratify_autonomous_pacific_mandate.dds` |
| HAW dispatch Pacific delegation | `GFX_goal_independence_wave_haw_dispatch_pacific_delegation` | `source_png/focuses/goal_independence_wave_haw_dispatch_pacific_delegation_source.png` | `processed_png/focuses/goal_independence_wave_haw_dispatch_pacific_delegation.png` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_haw_dispatch_pacific_delegation.dds` |

Each focus also has a paired `_shine` sprite using the same DDS texture. Exact copy-ready registration blocks are in `gfx_handoff.md`.

## Visual review and identity notes

- HBX reads as California/Pacific civic-industrial administration: arsenal gate and restrained bear seal; port ledger and supply bureau; Sacramento dome and civic table; port/factory/guard triad; bilateral asset ledger; procurement board; and three-route maritime congress.
- HAW avoids invented historical or universal sacred symbolism: shipping register, coastwatch tower/lantern, representative table compact, inter-island logistics network, base/property keys and ledger, bounded autonomy mandate, and diplomatic delegation ship/table.
- The seven HBX and seven HAW compositions are not recolors or relabels of a shared still. Their central subjects and silhouettes remain distinct at native size.
- `contact_sheets/006_pacific_focus_icons_1x_contact_sheet.png` is the native 94x86 review. `contact_sheets/006_pacific_focus_icons_3x_contact_sheet.png` is the enlarged nearest-neighbour review. `contact_sheets/006_pacific_focus_icons_source_contact_sheet.png` preserves the chroma-key source review.

## Validation evidence

- `validation/validation.json` records all 14 source, processed, and DDS hashes plus dimensions, alpha range, legacy BGRA header fields, `DDSCAPS_TEXTURE`, and exact file length.
- `validation/hashes.sha256` is the flat SHA-256 ledger.
- All runtime DDS files are 94x86, 32-bit, one-level uncompressed BGRA8888 (`DDS ` header 124, pixel format size 32, flags 65, fourCC 0, masks RGBA `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, texture caps `0x1000`), 32,464 bytes, alpha min 0 and max 255.
- Processed PNGs have transparent corners and no remaining chroma-key field; checkerboard contact sheets were inspected at native and 3x size.

## Scope boundary

No advisor, theorist, high-command, officer-corps, leader, commander, portrait, flag, localisation, gameplay, `.gfx`, `.gui`, or spreadsheet files were created or edited by this package. There are zero Event 006 advisor DDS outputs, references, or placeholders.
