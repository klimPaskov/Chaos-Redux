# Air Contamination Source Ledger

## Purpose

The Air Contamination source ledger gives the Chaos Meter a permanent, clickable record of every atmospheric source family that has contributed to the global burden.

A source enters the ledger when it first records a positive contribution or a positive current footprint. Its row remains in the ledger even after its current contribution falls to zero.

The ledger is an Air Cleanliness system surface. It is not an Event Details row, an evolution, or an ordinary event-log entry.

## Source Families

The ledger uses four stable source ids from `common/script_constants/chaos_meter_constants.txt`.

- `chemical` records changes from chemical contamination state classes.
- `biological` records changes from biological outbreak agents and intensity bands.
- `fallout` records active fallout intensity, direct terminal nuclear deltas, and the permanent Fallout atmospheric footprint.
- `aerosols` records the shared minor reservoir used by large wildfire smoke, volcanic eruptions, lingering ash, and other bounded atmospheric particulate aftermath.

The aerosol family stays grouped because its engine contribution is one shared capped reservoir. Splitting the visible row into disaster-specific statistics would invent precision that the runtime does not store.

## Persistent Accounting

`global.air_contamination_source_log_entries` stores source ids in first-observed order. Parallel arrays indexed by stable source id store the source statistics.

Each source records:

- current contribution in basis points and percent,
- lifetime gross additions,
- lifetime direct clearing or withdrawal,
- lifetime net delta,
- cumulative observed pressure decay,
- last applied delta,
- last change in current pressure,
- first observed date,
- latest activity date.

The exact global ledger separately records total Air Contamination rises and falls. Atmospheric recovery records its latest applied value and lifetime applied value. This keeps system recovery distinct from direct source clearing.

## Mutation Wiring

Chemical and biological state transitions pass a stable source id and their updated global footprint into `air_contamination_apply_delta_bp`. The central delta effect replaces the requested change with the actual clamped change before registering the source activity.

The monthly host update registers fallout and aerosol gross inputs before applying their combined net change. After the combined change is clamped, the update derives the exact atmospheric recovery that reached the global total.

The strategic singularity terminal consequence is owned by the fallout source family.

`air_contamination_refresh_values` synchronizes all four current footprints, records exact changes to the global total, rebuilds summary percentages, and creates a truthful legacy record when a loaded campaign already has an active source but no ledger receipt.

When Fallout permanently fixes Air Contamination at 99 percent, the refresh path attributes the actual transition rise to the fallout source when that change is observable. A campaign loaded after that boundary receives a current fallout footprint without inventing a historical rise that occurred before the ledger existed.

## GUI Layout

`interface/chaosx_chaos_meter_popup.gui` keeps the Air Cleanliness window at its existing 500 by 343 size.

The upper section uses both halves of the window. Four paired rows place contamination beside clean air, last net change beside applied recovery, source footprint beside record count, and lifetime rises beside lifetime falls. Full-width system-status and Air Winter rows follow above the source ledger.

The lower section contains a scrollable list. Each row is a full-width button and shows the source name, current contribution, last applied delta, lifetime additions, direct clearing, and observed pressure decay.

Selecting a row opens `chaos_meter_air_source_details_overlay`. The overlay exposes the complete source accounting, observation dates, source description, and source-specific decay behavior. Closing the overlay returns to the unchanged permanent ledger.

`common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt` owns list population, row clicks, selection validation, and overlay visibility. `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt` resolves source names, descriptions, behaviors, and signed delta text.

## Assets and Sprite Wiring

The ledger requires no new image asset.

- The panel and list background reuse `GFX_tiled_plain_bg`.
- Source rows reuse `GFX_chaosx_chaos_meter_entry` from the existing Chaos Meter sprite package.
- The detail overlay reuses `GFX_closebutton_small`.
- The simulation control reuses `GFX_chaosx_checkbox_checked` and `GFX_chaosx_checkbox_unchecked`.

No additional `.dds` file, asset manifest entry, or `.gfx` definition is needed.

## Future Plans

- Add a bounded source-history sublist if individual receipts become necessary for campaign analysis.
- Add regional source attribution only after the runtime stores regional contribution ledgers rather than reconstructing them from current state.
- Add a compact trend indicator sprite if a reviewed final asset improves readability without reducing the statistics area.
