# Air Winter Mapmode Monitoring Proof

Status: implemented and statically reviewed. Hearts of Iron IV was not launched, and no live tooltip or rendering claim is made.

## Accepted contract

The accepted winter mapmode specification defines four viewer-specific information levels.

| Level | Access | Visible information |
| --- | --- | --- |
| None | Foreign state without shared reports | Current winter phase only |
| Basic sampling | State owned or controlled by the viewer, or a treaty viewer | Current phase and one-month trend |
| Atmospheric office | Viewer completed a roof-sampler project in at least one state | Trend, cause readings, and likely phase next season |
| Terminal modelling | Global Air Contamination is at least 90 percent, or a major power has an atmospheric office | Possible Fallout classification from atmospheric evidence |

The three Air Winter map modes use the same access contract. A player cannot bypass the gate by switching from the phase layer to exposure or survival. A state without initialized phase and target-phase ledgers reports that no atmospheric ledger exists instead of displaying zero-valued readings.

## Script ownership

- `common/script_constants/air_cleanliness_winter_constants.txt` owns the 9000 basis-point terminal threshold.
- `common/scripted_triggers/air_cleanliness_winter_triggers.txt` derives the viewer's basic, office, and terminal access.
- `common/scripted_effects/air_cleanliness_winter_response_effects.txt` grants `air_winter_atmospheric_office` when a roof-sampler project completes.
- `common/scripted_effects/air_cleanliness_winter_effects.txt` reconstructs that country capability from surviving sampler states during normalisation and clears it through the bounded country reset.
- `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` selects one information tier for each mapmode tooltip.
- `localisation/english/chaosx_map_modes_l_english.yml` owns the concrete player-facing reports.

The monitoring level is derived for the viewing country. It is not stored as one state value because ownership, control, treaty access, and national investment can give different viewers different reports for the same state.

## Scope proof

The installed official `common/map_modes/documentation.md` states that a state mapmode evaluates the current state through `FROM` and the viewing player through `ROOT`. Chaos Redux already uses that contract in `black_plague_state_is_visible_to_mapmode_player` and `black_plague_state_details_are_visible_to_mapmode_player`.

The Air Winter tooltips follow the same shape. The delayed tooltip calls `[FROM.GetAirWinter...MapModeTooltip]`. Its scripted localisation evaluates a state-scoped trigger. That trigger checks state ownership or control against `ROOT`, then checks country flags inside `ROOT`.

## Information boundaries

None reveals only the current phase. Basic sampling adds qualitative direction without exposing exact pressure values. The atmospheric office reveals exact state readings, the main global and local atmospheric pressures, and the calculated target phase. Terminal modelling adds a bounded classification range.

The terminal range is presentation evidence only.

| Calculated target phase | Atmospheric classification range |
| ---: | --- |
| 0 | Remote Refuge or Scarred Province |
| 1 | Scarred Province |
| 2 | Scarred Province to Ash Zone |
| 3 | Ash Zone to Dead City |
| 4 | Dead City to Wasteland |
| 5 | Wasteland |
| 6 | Wasteland to Vitrified Zone |

A state without an initialized target-phase ledger reports insufficient atmospheric readings instead of receiving a fabricated phase-0 range. The tooltip states that direct strikes and blast history can change the final classification. It does not set or commit a Fallout grade. The later deterministic grading transaction remains the sole owner of committed grade evidence.

## Idempotence and cleanup

Completing another sampler only sets the same country flag again. Monthly state normalisation can reconstruct the flag after script migration without creating a country-wide iterator. The state update already registers its owner in the bounded Air Winter country registry before normalisation. `air_winter_reset_country` clears the office flag, while the deferred state reset clears every sampler flag during the existing monthly state pass.

## Static validation boundary

Static inspection confirms:

- all three delayed tooltips route through gated scripted localisation
- initialized states test terminal selection before office, then basic, then none
- the threshold uses one script constant
- no Fallout survival coefficient, grade receipt, or ready flag is written
- every scripted localisation result has an English localisation key
- the localisation file retains its UTF-8 BOM

The following behavior is not claimed as observed:

- `ROOT` and `FROM` values during live tooltip evaluation
- nested localisation expansion inside the terminal report
- daily mapmode refresh after a sampler completes or contamination crosses 90 percent
- multiplayer visibility and save reconstruction of the country capability

Those points remain available for the user's later live validation. They are not a completion requirement for this static core-mechanics tranche.
