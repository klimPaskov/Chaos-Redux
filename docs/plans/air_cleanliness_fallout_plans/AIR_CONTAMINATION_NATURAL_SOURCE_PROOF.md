# Air Contamination Natural Source Proof

## Accepted correction

Large wildfire smoke, volcanic eruptions, and widespread ash aftermath contribute to Air Contamination. Their combined monthly contribution must remain very low and hard capped.

The canonical correction is recorded in `docs/specs/air_cleanliness_fallout_specs/specs/baseline/01_core_overhaul.md`.

## Runtime ownership

Event 013 owns physical disaster impact resolution. Air Cleanliness owns monthly atmospheric accounting.

`air_contamination_register_natural_disaster_source` runs from state scope after family and severity resolution. It is called by:

- `natural_disaster_execute_impact` for ordinary and scheduled chain impacts
- `natural_disaster_execute_repeated_impact` for repeated impacts
- `natural_disaster_apply_neighbor_impact` for selected regional-spread states

Chained ashfall and massive-eruption jobs return through the ordinary Event 013 impact route. The regional-spread route copies its parent sequence id and impact index before registration. Each state removes itself from the neighbor candidate array after selection.

The source key is the state-local tuple of Event 013 sequence id, impact index, and family. Re-entry of the same physical impact therefore contributes once. A later segment or a different physical family remains eligible.

## Magnitude proof

The aggregate reservoir is clamped from `0 bp` through `4 bp` after every impact and before every monthly read. `4 bp` equals `0.04 percent` Air Contamination.

The largest single addition is an abnormal massive eruption at `1.25 bp`, equal to `0.0125 percent`. The smallest addition is `0.05 bp`, equal to `0.0005 percent`. Regional wildfire smoke begins at `0.10 bp`, equal to `0.001 percent`.

The reservoir decays by `0.25 bp` after its monthly value is copied. A full reservoir with no further inputs produces 16 monthly contributions from `4.00 bp` through `0.25 bp`. Their gross sum is `34 bp`, equal to `0.34 percent`, before normal recovery.

Below 25 percent contamination, normal recovery is `3 bp` monthly. A full reservoir without further inputs can produce only `2.5 bp`, equal to `0.025 percent`, of temporary net growth before its monthly contribution falls to the recovery rate. If continuous disasters keep the reservoir full, the low-band net increase is limited to `1 bp` monthly, equal to `0.01 percent`.

## Monthly coordinator proof

`air_contamination_prepare_natural_source_monthly` is called by the existing `air_contamination_monthly_update`. It copies the clamped reservoir, decays it once, and caches the date in `global.air_contamination_natural_source_last_tick_date`.

A second call on the same date reuses the cached contribution and cannot apply a second decay. No new daily, weekly, monthly, country, or state on action was added. The current `on_monthly` host route remains the only periodic owner.

Host acquisition and transfer continue while the Chaos Meter display is disabled. Air Cleanliness therefore retains its own monthly lifecycle for human, AI, and spectator coordinators. The independent Air Cleanliness toggle still controls whether the cached source enters contamination.

## Lock and save behavior

Missing reservoir variables initialize to zero inside the public monthly helper, which keeps existing saves safe. Disabling Air Cleanliness hides the current contribution and prevents it from entering the monthly delta while the reservoir continues to dissipate.

Final Silence retains its fixed contamination total. New natural-source registrations stop, the hidden reservoir continues to dissipate, and the monthly breakdown exposes zero natural contribution while the lock is active.

## UI and asset proof

The existing Air Cleanliness monthly model line displays the cached wildfire-smoke and volcanic-ash contribution. The overview text identifies both sources. This correction requires no new icon, DDS file, sprite, or GFX registration.

## Static evidence boundary

The implementation was reviewed against the offline wiki, installed official documentation, Event 013 runtime paths, the existing host monthly route, and the vanilla capped-variable precedent. HOI4 was not launched at the user's request. Runtime observation is therefore not claimed.
