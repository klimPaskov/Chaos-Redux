# Chaos Meter Popup Window

## What This Adds

This update adds a dedicated Chaos Meter popup window that opens from the topbar chaos meter.

The popup is designed around the vanilla world tension window style and size, and adds five tabs:

1. `Status`
2. `History` (default tab)
3. `Air Cleanliness`
4. `Condemnation`
5. `Deaths`

## How It Works

### Opening Behavior

- The topbar chaos meter now has a transparent click area.
- The meter remains visually an icon/text element (not a highlighted button on hover).
- Clicking it opens the popup and defaults to the `History` tab.
- The topbar tooltip is unified into one tooltip that includes current value, tier, and `Click to open Chaos Meter details`.
- Shortcut: `Ctrl + Shift + M` opens the chaos meter details popup.

### Status Tab

The `Status` tab shows:

- current chaos value,
- current chaos tier,
- a short mechanics explanation.

### History Tab

The `History` tab shows a scrollable log of chaos value changes with toolbar controls for filtering and sorting.

Each row records:

- history sequence number,
- date of the change,
- reason/category of what happened,
- source country for country-driven changes (flag shown in each row),
- delta (`+`/`-`) applied in that update,
- resulting total chaos value after the update (shown in yellow).

The list is mouse-wheel scrollable and uses a right-side scrollbar.

History toolbar controls:

- Filter: `All`, `Major`, `Minor`, `Other`
- Sort mode: `By Index`, `By Actor`, `By Delta`
- Sort order: `Ascending`, `Descending`

Actor sort behavior:

- Rows with an actor are grouped by actor with deterministic actor-id ordering.
- Rows without an actor are always pushed to the bottom, regardless of ascending/descending mode.

War declaration entries are merged into one row per day/reason/actor bucket to reduce spam when one country declares multiple wars at once.

History rows now include per-cause reason mapping for the full chaos meter change surface (war/peace/annexation/puppets/liberation/faction and diplomacy shifts/subtle events/settings updates/global trend updates).

### Air Cleanliness Tab

The `Air Cleanliness` tab shows:

- current global contamination and cleanliness,
- monthly contamination delta and natural recovery,
- chemical/outbreak state contribution counts,
- last nuke contamination contribution,
- one consolidated contamination stage status line,
- active winter phase and fallout world-end progress.
- a right-side quick mechanic overview with threshold summary.

Every value/summary row in this tab has a tooltip explaining what it represents.

### Condemnation Tab

The `Condemnation` tab shows:

- your current country condemnation (`chem_warfare_condemnation`),
- global total condemnation and number of contributing countries,
- a scrollable country list of condemnation sources,
- ascending/descending sort controls by condemnation amount.

Rows include country flags and a diplomacy quick-open button.
When condemnation values change, the visible condemnation tab is rebuilt immediately so the list updates in real time.

### Deaths Tab

The `Deaths` tab shows:

- total global deaths (civilian + military),
- split between civilian deaths and military casualties,
- chaos generated from deaths using `1 chaos per 1,000,000 deaths`,
- most recent recorded deaths change,
- a separator and a scrollable country totals list below the summary block.

Country entries show the latest recorded update plus cumulative total, civilian, and military deaths for that country.
The per-country details overlay is intentionally disabled in this version of the deaths view.

## Data Flow

History entries are recorded in `common/scripted_effects/chaos_meter_effects.txt` through `record_chaos_meter_history_entry`.
The displayed list is built into dedicated view arrays via `rebuild_chaos_meter_history_view`.

Entry data is stored in global arrays:

- `global.chaos_meter_history_sequence_entries`
- `global.chaos_meter_history_delta_entries`
- `global.chaos_meter_history_total_entries`
- `global.chaos_meter_history_reason_entries`
- `global.chaos_meter_history_date_entries`
- `global.chaos_meter_history_target_count_entries`
- `global.chaos_meter_history_actor_entries`
- `global.chaos_meter_history_has_actor_entries`

Derived view arrays used by the GUI:

- `global.chaos_meter_history_view_sequence_entries`
- `global.chaos_meter_history_view_delta_entries`
- `global.chaos_meter_history_view_total_entries`
- `global.chaos_meter_history_view_reason_entries`
- `global.chaos_meter_history_view_date_entries`
- `global.chaos_meter_history_view_target_count_entries`
- `global.chaos_meter_history_view_actor_entries`
- `global.chaos_meter_history_view_has_actor_entries`

The popup reads these arrays through scripted GUI dynamic list rendering.

Condemnation view arrays:

- `global.chaos_meter_condemnation_view_country_entries`
- `global.chaos_meter_condemnation_view_value_entries`

Condemnation view rebuild effect:

- `rebuild_chaos_meter_condemnation_view`

Deaths source arrays:

- `global.chaos_meter_deaths_sequence_entries`
- `global.chaos_meter_deaths_date_entries`
- `global.chaos_meter_deaths_change_entries`
- `global.chaos_meter_deaths_total_entries`
- `global.chaos_meter_deaths_reason_entries`

Deaths view arrays:

- `global.chaos_meter_deaths_view_sequence_entries`
- `global.chaos_meter_deaths_view_date_entries`
- `global.chaos_meter_deaths_view_change_entries`
- `global.chaos_meter_deaths_view_total_entries`
- `global.chaos_meter_deaths_view_reason_entries`

## Integration Notes

- Core chaos updates (`add_chaos_meter_value`) now write to history.
- Direct settings-based value writes (`update_actual_chaos_meter`) also write to history.
- Disable/reenable settings transitions that change current value also write to history.
- Deaths are registered through `chaos_meter_register_deaths`, which also synchronizes chaos gain from death milestones.
- Country totals shown in the deaths tab are maintained on country-scoped variables and legacy raw logs are backfilled through bounded rebuild chunks when needed.

## Icons and GFX Wiring

Vanilla `.dds` assets copied into this mod (with `chaosx` prefixed filenames):

- `gfx/interface/chaosx_chaos_meter_bg.dds`
- `gfx/interface/chaosx_chaos_meter_entry.dds`
- `gfx/interface/chaosx_sort_button_100x29_2.dds`
- `gfx/interface/chaosx_button_123x34_vanilla.dds`

Sprite definitions are registered in:

- `interface/chaosx.gfx`

Sprite names used in code:

- `GFX_chaosx_chaos_meter_bg`
- `GFX_chaosx_chaos_meter_entry`
- `GFX_chaosx_sort_button_100x29_2`
- `GFX_chaosx_button_123x34_vanilla`

No additional art is required for this feature unless you want a custom non-vanilla visual skin.

## Future Plans

1. Add a dedicated filter for world-state/system rows separate from actor-driven rows.
2. Add quick jump controls (latest/oldest) for long campaigns.
3. Add optional category color accents per reason family.
