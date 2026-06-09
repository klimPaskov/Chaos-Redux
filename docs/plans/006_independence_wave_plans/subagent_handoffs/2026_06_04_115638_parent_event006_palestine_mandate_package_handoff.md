# Event006 Palestine Mandate Package Handoff

## Scope

Implemented a bounded verified-package tranche for the Event 006 Independence Wave:

- carrier tag: vanilla `PAL`
- initial release anchor: state `454` Palestine
- package label: `Palestine Mandate Council`
- package id: `constant:independence_wave_package.palestine_mandate`
- package type: `constant:independence_wave_startup.protectorate_package`
- route family: existing Protected Mandate treaty-audit, guarantee-review, proclamation, integration, AI, and event-log rows

No flags, country history, state history, country tag files, or new country files were created or modified.

## Vanilla Evidence

- `common/country_tags/00_countries.txt`: `PAL = "countries/Palestine.txt"`
- `history/countries/PAL - Palestine.txt`: `capital = 454` and `set_cosmetic_tag = PAL_mandate`
- `history/states/454-Israel.txt`: state `454`, state name `STATE_454`, and `add_core_of = PAL`
- vanilla localisation includes PAL country names, party names, `PAL_mandate`, `PAL_harold_macmichael`, and `PAL_amin_al_husseini`
- vanilla flag assets include base, medium, and small `PAL`, ideology, and `PAL_mandate` flags

## Files Changed

- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `localisation/english/006_independence_wave_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

## Audit

Read-only subagent `019e9278-4d82-7ea0-8727-734116bee904` audited the tranche. It found:

- PAL's explicit reduced-release anchor was accidentally nested inside the BOT anchor block.
- PAL could theoretically run through the oil-protectorate classifier before its Palestine-specific classifier if future data gave it an oil-producing owned state.

Both findings were fixed:

- BOT and PAL reduced-release anchor blocks are now sibling `if` blocks.
- PAL is excluded from both generic non-oil Protected Mandate and oil-protectorate classifier branches, then receives its own Palestine-specific mandate setup.

## Validation

- Event006 script/localisation braces balanced after the fix.
- No `<=` or `>=` found in touched Event006 script/localisation files.
- Focus tree count unchanged: 97 focuses, 97 `ai_will_do`, 97 `completion_reward`.
- English localisation keeps UTF-8 BOM, has no `:0`, has one `independence_wave_package_label_palestine_mandate`, and no duplicate keys.
- Workbook `unzip -t` passed.
- LibreOffice headless conversion of the workbook passed.
- Flag/history diff filter returned no touched flag, country-history, or state-history paths.

## Remaining Risks

This tranche intentionally reuses the existing Protected Mandate route rather than creating a bespoke Palestine-only decision chain. That is not a gameplay fallback: the package is a Palestine-specific verified candidate and label, backed by vanilla `PAL`, while the route logic remains the shared mandate family already implemented for Event 006.
