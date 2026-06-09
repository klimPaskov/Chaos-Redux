# Event 006 Release News Scope Fix Handoff

## Files changed

- `common/scripted_effects/006_independence_wave_effects.txt`

## Gameplay surface changed

- Independence Wave current-wave release display slots.
- `chaosx.news.6` uses these slots through `GetIndependenceWaveReleasedCountryList`.

## Changed identifiers

- `global.independence_wave_country_1`
- `global.independence_wave_country_2`
- `global.independence_wave_country_3`
- `global.independence_wave_country_4`
- `global.independence_wave_country_5`
- `global.independence_wave_country_6`
- `global.independence_wave_country_7`
- `global.independence_wave_country_8`
- `global.independence_wave_country_9`
- `global.independence_wave_country_10`
- `global.independence_wave_country_11`
- `global.independence_wave_country_12`
- `global.independence_wave_country_13`
- `global.independence_wave_country_14`
- `global.independence_wave_country_15`
- `global.independence_wave_country_16`

## Before

`independence_wave_register_successful_release` stored the current country scope directly:

```txt
set_variable = { global.independence_wave_country_1 = THIS }
```

The news localisation reads those slots as country-id variables:

```txt
[?global.independence_wave_country_1.GetName]
```

That mismatch could make the release list display raw or wrong values instead of country names.

## After

Each slot stores the current release country id:

```txt
set_variable = { global.independence_wave_country_1 = THIS.id }
```

This matches existing Chaos Redux precedent for dynamic country-name variables, including `global.asteroid_country`, `global.generalissimo_country`, and random-war news variables.

## Validation

- Searched for remaining direct `THIS` assignments to `global.independence_wave_country_*`; none remain.
- Confirmed all 16 slot assignments now use `THIS.id`.
- Confirmed `GetIndependenceWaveReleasedCountryList` still maps release counts one through sixteen to the corresponding localisation list.

## Remaining risks

- This was a script/static fix only. It still needs live in-game confirmation that `chaosx.news.6` prints every released country name correctly after a real wave.
