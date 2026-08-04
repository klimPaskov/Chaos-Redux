# Air Cleanliness Source Ledger GUI Proof

## Scope

This proof covers the compact Chaos Meter Air Cleanliness panel, the persistent contamination-source dynamic list, full-row selection, and the source-detail overlay.

It does not claim live consumer validation. Hearts of Iron IV was not launched.

## Engine References

The implementation was checked against the offline `Interface modding` and `Scripted GUI modding` wiki pages, the required scope, trigger, effect, localisation, and data-structure pages, and the vanilla `common/scripted_guis/_documentation.md` file.

The persistent statistics use numeric arrays documented by the vanilla `add_to_array`, `resize_array`, variable, and array-loop effects. `resize_array` grows missing slots with zero values, which lets the ledger reconstruct its read model safely when the source arrays do not yet exist.

The dynamic list mirrors the existing Chaos Redux condemnation list and the vanilla scrollable `gridBoxType` pattern in `interface/achievements.gui`.

## Runtime Wiring Evidence

- `global.air_contamination_source_log_entries` stores stable source ids in first-observed order.
- `air_contamination_register_source_activity` adds a source id only when its first real contribution or current footprint is observed.
- No cleanup or toggle path clears `global.air_contamination_source_log_entries` after initialization.
- `chaos_air_source_dynamic_list` binds directly to that global array with `change_scope = no` and exposes `air_source_id` to each row.
- `air_source_entry_plate_button` covers the complete 449 by 49 row and calls `open_air_contamination_source_details`.
- The selection effect stores the stable source id in `chaos_meter_air_selected_source` and opens the detail overlay only after the selected source is validated against the initialized source array.
- The close effect clears the overlay flag and resets the selection to the configured negative sentinel.

## Render Scenarios

The HOI4 GUI renderer inspected the implemented sources through workspace `mod_chaos_redux_ea3b2d67c2c0` at 1280 by 720 and 1920 by 1080.

### Compact Air Cleanliness panel

Scenario `air_cleanliness_resolved` used resolved 99.99 percent contamination, maximum-length lifetime values, Fallout lock status, Fallout Night winter status, and the empty-ledger state.

- Cropped render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b72b006b26ef10e66aacb94800e3bc23d8a1138e11e9136729dab02ed9013aa5/0e9215e82c7b547df81e6618dc5835cce86d892834f2ad29bbae88353dbafe55/chaos_meter_air_content_window-cropped.png`
- Click regions: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/75a21150816d252b1c0d3471cb5b4f12b485fa7f8930e91630721939204e859e/df76b686a71385798c8be9344c94243374619d3a7ec4ffed34bf9a67b67b8ef1/chaos_meter_air_content_window-click-regions.png`
- State matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4248b7bee3167d40862948236750d86cc1fe35724f20a8ca9fe13673fe36a402/50fb95a2ba33a4dbed1886bde4201c1f325edd5bf029266ec6be21715224db0e/chaos_meter_air_content_window-state-matrix.json`

The renderer reports one structural overlap because the conditionally visible empty-state message occupies the same list viewport as the dynamic grid. The existing condemnation list produces the same single diagnostic. The two surfaces are mutually exclusive through `air_source_no_entries_info_visible`.

### Source row

Scenario `air_source_entry_resolved` used the longest source name and representative maximum current, last, lifetime, clearing, and decay values.

- Cropped render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2279e96a3797ac750415a8f752d762b22845d37ad6d1cc9411e9d9d4d013ab4/5db9e6837198502d0aa0b1159674344a6b10e4181a4faaddd54aed86d84da1e3/chaos_meter_air_source_entry-cropped.png`
- Click regions: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e114821f775128bb932776f69002a923948c3b527e1d5ea41e2e20fa4db763d0/42805843cf2c1cd8b6bbe152c654e5c85dbd402fd8672bb47ec5088fad9ec1f0/chaos_meter_air_source_entry-click-regions.png`
- State matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/95df8aad111fd2159fb4a4332b88dbfe7c6c7b193fdb19c3522397124a9f317e/78253fa917d4b5050443acd9ff68a4a0949389cfeb90aa5ed5eb6410cdadfce7/chaos_meter_air_source_entry-state-matrix.json`

The row's only structural overlap is intentional. The full-row button sits over the row background so the complete record remains clickable.

### Source details

Scenario `air_source_details_resolved` selected the smoke, ash, and aerosol family and supplied resolved maximum accounting values, dates, and the longest source explanation.

- Cropped render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc78ba047d7ae1ee6c388bdce66362f7703a05b0a4796555f8e4cf040b297752/96465e5ac1339895020c5ad8348ef8f5367be4dad1738be441163c5f1be1c470/chaos_meter_air_source_details_overlay-cropped.png`
- Click regions: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/608ab5b93ea3744d73864825e42c2f48d913bcf37dd77a1b6df2c37df10d36ec/0bf36dbe029ea76dd652f773a7270edcba59bfc304d34bc7b6fc78c6d3e43e68/chaos_meter_air_source_details_overlay-click-regions.png`
- State matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2439c7b88b618b239c8699c58ab2bd94ee5ad4ac78e1407a94f113264524e9e2/d9740a471bb0a30d52d8e7b5ecc0986d5a61efc7104fc833bb48764c47247535/chaos_meter_air_source_details_overlay-state-matrix.json`

The resolved detail scenario reports no visible overlap.

## Tool Boundary

The GUI tool's global source-graph check also reports unknown `player_context` values across existing Chaos Redux scripted GUIs. The vanilla scripted-GUI documentation and the live repository precedent both use this context. The source-specific render results above separate the implemented layout evidence from that workspace-wide analyzer limitation.
