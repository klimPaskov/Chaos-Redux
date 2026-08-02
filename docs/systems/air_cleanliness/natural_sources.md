# Air Cleanliness Natural Sources

## Purpose

Large wildfire smoke and volcanic ash add a small atmospheric burden to Air Contamination. The contribution is intentionally weaker than chemical contamination and nuclear fallout. It can reinforce an existing crisis, but it cannot become a rapid natural route to Fallout.

## Runtime flow

Event 013 registers a natural atmospheric source after it resolves the impact family and severity. The shared helper accepts:

- wildfires at regional severity or above
- volcanic eruptions at any resolved severity
- ashfall at any resolved severity
- massive eruptions at any resolved severity

When an ash-heavy aftermath card opens, a second state-scoped helper records a
small settled-ash contribution. Severe or worse volcanic eruptions, regional or
worse ashfall, and severe or worse massive eruptions qualify. The stored disaster sequence is the idempotency key,
so reopening the same card cannot add the aftermath source twice.

Each state records the disaster sequence, impact index, and family that last contributed. Repeating the same physical impact does not add the source twice. A later impact in the same sequence can contribute when its impact index or family differs.

The contribution enters `global.air_contamination_natural_source_reservoir_bp`. The reservoir represents the next monthly smoke-and-ash contribution in Air Contamination basis points.

The existing host-owned `air_contamination_monthly_update` performs the only periodic work:

1. Copy the current reservoir into `global.air_contamination_natural_source_bp`.
2. Add that amount to the normal monthly contamination delta.
3. Reduce the reservoir by `0.25 bp`.
4. Preserve the reduced reservoir for the next month.

The monthly helper has a date guard. A repeated host call on the same date reuses the cached monthly value and does not decay the reservoir twice. No new country or state iterator is introduced.

## Magnitude and ceiling

The maximum natural-source contribution is `4 bp` per month, equal to `0.04 percent` Air Contamination. The reservoir is clamped immediately after every impact and before every monthly read.

| Source | Qualifying severity | Added reservoir pressure |
| --- | --- | ---: |
| Wildfire | Regional | 0.10 bp |
| Wildfire | Catastrophic | 0.20 bp |
| Wildfire | Abnormal | 0.35 bp |
| Volcanic eruption | Local through abnormal | 0.05 through 0.50 bp |
| Ashfall | Local through abnormal | 0.05 through 0.75 bp |
| Massive eruption | Local through abnormal | 0.25 through 1.25 bp |
| Ashfall aftermath | Regional through abnormal | 0.05 through 0.15 bp |
| Volcanic aftermath | Severe through abnormal | 0.05 through 0.20 bp |
| Massive-eruption aftermath | Severe through abnormal | 0.10 through 0.25 bp |

At the ceiling, the source remains close to the reversible low-contamination recovery rate. A long series of ash impacts can keep the burden present, while the hard monthly ceiling prevents many affected states from multiplying into a large contamination spike.

## System interactions

- Air Winter reads the resulting global Air Contamination value through its existing forcing model.
- Chemical and nuclear source accounting is unchanged.
- Air Contamination chaos synchronization receives only the final net monthly delta, so small natural contributions enter the same remainder buffer as every other source.
- Disabling Air Cleanliness blocks new natural-source registration and prevents the cached source amount from entering contamination. The existing atmospheric reservoir continues to dissipate through the host monthly pulse.
- Final Silence blocks new natural-source registration and shows zero natural contribution. The hidden reservoir continues to dissipate without changing the locked total.
- Natural disaster recovery cards do not clear the reservoir. The atmospheric burden fades on its own after the local response has ended.
- The aftermath receipt is written before the recovery card's first reassessment. It does not alter the card's population, building, or recovery effects.

## Files

- `common/script_constants/fallout_consolidated_constants.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_effects/chaos_meter_effects.txt`
- `localisation/english/chaosx_chaos_meter_l_english.yml`

## Icons and UI assets

No new icon is required. The existing Air Cleanliness monthly recovery line also displays the live smoke-and-ash contribution. No sprite identifier, DDS file, or GFX registration is added by this mechanic.

## Future plans

1. Add a bounded cleanup effect for dedicated volcanic monitoring or smoke-control projects if those mechanics gain a direct atmospheric mandate.
2. Let Fallout cause memory distinguish nuclear soot from volcanic ash without changing the natural-source ceiling.
3. Add a regional ash observation to the final normal-map visual package after the ordinary-map route and regional asset gates pass review.

## References consulted

The implementation follows the offline Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding pages. It also follows the installed official effects, triggers, modifiers, script concepts, and script constants documentation. The vanilla capped-variable pattern was checked in `common/scripted_effects/BUL_scripted_effects.txt`.
