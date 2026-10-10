# Public Values and Thresholds

[Part 2](../specs/030_time_traveler_spec_part_2_baseline_and_values.md) owns the value rules, causes, and tooltips.
This matrix lists only the band boundaries that script constants must encode.

| Value | Band 1 | Band 2 | Band 3 | Main consumer |
| --- | --- | --- | --- | --- |
| Credibility | Doubted `0-34` | Trusted `35-69` | Indispensable `70-100` | consultation tier and Evolution I pacing |
| Exposure | Secret `0-29` | Suspected `30-64` | Public `65-100` | foreign operation availability and interest cap `2`, `4`, `6` |
| Timeline Divergence | Recognizable `0-29` | Altered `30-64` | Broken `65-100` | forecast precision and Evolution II to V pacing |
| Temporal Stability (Evolution V display) | Collapsing `0-35` | Strained `36-70` | Coherent `71-100` | node behavior and machine world-end readiness |

Temporal Stability equals `100` minus Timeline Divergence, and only one of the two is shown at a time.
The machine world end additionally needs Stability below the tuned threshold, proposed `25`.

## Design guard

A new persistent Event 030 value is rejected unless it changes a distinct player decision and cannot be represented by these values, a band, an incident state, or a temporary mission.
The current design has no fourth meter.
