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

`air_contamination_register_natural_disaster_aftermath_source` runs from the
state aftermath-card opener. It accepts severe or worse volcanic eruptions,
regional or worse ashfall, and severe or worse massive eruptions, then stores
the disaster sequence id on the state.
The same aftermath card cannot write the source twice. This is a second
physical contribution for settled ash, not a second registration of the impact
receipt.

The source key is the state-local tuple of Event 013 sequence id, impact index, and family. Re-entry of the same physical impact therefore contributes once. A later segment or a different physical family remains eligible.

## Magnitude proof

The aggregate reservoir is clamped from `0 bp` through `4 bp` after every impact and before every monthly read. `4 bp` equals `0.04 percent` Air Contamination.

The largest single addition is an abnormal massive eruption at `1.25 bp`, equal to `0.0125 percent`. The smallest addition is `0.05 bp`, equal to `0.0005 percent`. Regional wildfire smoke begins at `0.10 bp`, equal to `0.001 percent`.

The complete accepted source ladder is centralized in `common/script_constants/air_cleanliness_natural_source_constants.txt`.

| Physical family | Local | Severe | Regional | Catastrophic | Abnormal |
| --- | ---: | ---: | ---: | ---: | ---: |
| Wildfire | 0 bp | 0 bp | 0.10 bp | 0.20 bp | 0.35 bp |
| Volcanic eruption | 0.05 bp | 0.10 bp | 0.20 bp | 0.35 bp | 0.50 bp |
| Ashfall | 0.05 bp | 0.15 bp | 0.30 bp | 0.50 bp | 0.75 bp |
| Massive eruption | 0.25 bp | 0.50 bp | 0.75 bp | 1.00 bp | 1.25 bp |

The aftermath ladder adds 0.05, 0.10, or 0.15 bp for regional, catastrophic, or
abnormal ashfall, 0.05, 0.10, 0.15, or 0.20 bp for severe, regional,
catastrophic, or abnormal volcanic eruptions, and 0.10, 0.15, 0.20, or 0.25 bp
for severe, regional, catastrophic, or abnormal massive eruptions. These values
share the same global 4 bp reservoir clamp.

Even the largest direct massive-eruption impact and its largest aftermath
receipt total only `1.50 bp` before the shared reservoir clamp, equal to `0.015
percent` Air Contamination. Natural sources therefore remain a low-pressure
contributor even when an ash-heavy card follows the impact.

Event 013 defines severity as the ordered integer ladder from Local `1` through Abnormal `5`. The wildfire gate uses `greater_than_or_equals` against Regional `3`, then selects the exact Catastrophic and Abnormal overrides. Volcanic eruption, ashfall, and massive eruption select an exact value for every defined severity. No natural-source constant exceeds the shared `4 bp` ceiling.

The reservoir decays by `0.25 bp` after its monthly value is copied. A full reservoir with no further inputs produces 16 monthly contributions from `4.00 bp` through `0.25 bp`. Their gross sum is `34 bp`, equal to `0.34 percent`, before normal recovery.

Below 25 percent contamination, normal recovery is `3 bp` monthly. A full reservoir without further inputs can produce only `2.5 bp`, equal to `0.025 percent`, of temporary net growth before its monthly contribution falls to the recovery rate. If continuous disasters keep the reservoir full, the low-band net increase is limited to `1 bp` monthly, equal to `0.01 percent`.

## Monthly coordinator proof

`air_contamination_prepare_natural_source_monthly` is called by the existing `air_contamination_monthly_update`. It copies the clamped reservoir, decays it once, and caches the date in `global.air_contamination_natural_source_last_tick_date`.

A second call on the same date reuses the cached contribution and cannot apply a second decay. No new daily, weekly, monthly, country, or state on action was added. The current `on_monthly` host route remains the only periodic owner.

Host acquisition and transfer continue while the Chaos Meter display is disabled. Air Cleanliness therefore retains its own monthly lifecycle for human, AI, and spectator coordinators. The independent Air Cleanliness toggle still controls whether the cached source enters contamination.

## Engine-sensitive accounting proof

The installed official `effects_documentation.md` records `add_to_variable`, `set_variable`, and `clamp_variable` as effects supported in any scope. It defines `clamp_variable` as `Max( Min( var, max ), min )`. Both bounds may be variables, so `constant:air_contamination_natural_source.monthly_cap_bp` is valid after script-constant injection.

The installed official `script_concept_documentation.md` states that script constants are injected into scripts at load and that every scoped variable accepts a fixed-point constant through the `constant:` prefix. The installed `common/script_constants/documentation.md` defines the fixed-point schema used by the natural-source table.

The offline Data structures page confirms that regular variables can be stored on states and in global scope. It also documents `add_to_variable`, `check_variable`, and `clamp_variable`. The offline Effects and Triggers pages agree with the installed documentation. The state-local impact identity and the global reservoir therefore use documented variable scopes and effects.

The vanilla capped-variable precedent is `common/scripted_effects/BUL_scripted_effects.txt`. Its faction effects add to a variable and immediately clamp the result between a minimum and maximum. The natural-source registration follows the same add-then-clamp order. It adds a second clamp before monthly consumption so a loaded or externally modified reservoir cannot bypass the ceiling.

`air_contamination_monthly_update` copies `air_monthly_natural_bp` into the displayed source ledger and adds it once to `air_contamination_delta_bp`. The same delta then passes through `air_contamination_apply_delta_bp`. There is no separate direct write from the natural-source helper to `global.air_contamination_bp`.

## Static route audit

The three Event 013 registration sites were checked in their surrounding state-scope effects.

| Entry effect | Family and severity ready first | Physical identity ready first | Registration position |
| --- | --- | --- | --- |
| `natural_disaster_execute_impact` | Yes | Yes | Before population, building, aftermath, and spread resolution |
| `natural_disaster_execute_repeated_impact` | Yes | Yes | Before population, building, chain, and report resolution |
| `natural_disaster_apply_neighbor_impact` | Yes | Parent sequence and impact index copied first | Before population, building, aftermath, and report resolution |

The regional-spread candidate is removed from `natural_disaster_neighbor_candidates` before its impact effect runs. Chained ashfall and massive-eruption work returns through the ordinary or repeated impact effects, so it reaches the same registration helper and ceiling.

The aftermath-card opener calls the settled-ash helper immediately after the
state receives `natural_disaster_aftermath_active`. The helper's sequence guard
prevents duplicate writes if the card is reopened or reassessed. A
repository-wide reference check found no writer to
`global.air_contamination_natural_source_reservoir_bp` outside initialization,
the impact registration, the aftermath registration, and monthly decay.

## Lock and save behavior

Missing reservoir variables initialize to zero inside the public monthly helper, which keeps existing saves safe. Disabling Air Cleanliness hides the current contribution and prevents it from entering the monthly delta while the reservoir continues to dissipate.

Final Silence retains its fixed contamination total. New natural-source registrations stop, the hidden reservoir continues to dissipate, and the monthly breakdown exposes zero natural contribution while the lock is active.

## UI and asset proof

The existing Air Cleanliness monthly model line displays the cached wildfire-smoke and volcanic-ash contribution. The overview text identifies both sources. This correction requires no new icon, DDS file, sprite, or GFX registration.

## Static evidence boundary

The implementation was reviewed against the offline wiki, installed official documentation, Event 013 runtime paths, the existing host monthly route, and the vanilla capped-variable precedent. The read-only HOI4 event inspector was also attempted against `events/013_natural_disasters.txt`, but the Event 013 helper graph exceeded its fixed 200,000-projection ceiling even with helper expansion disabled. Source-level route review remains the evidence for the three call sites. HOI4 was not launched at the user's request. Runtime observation is therefore not claimed.
