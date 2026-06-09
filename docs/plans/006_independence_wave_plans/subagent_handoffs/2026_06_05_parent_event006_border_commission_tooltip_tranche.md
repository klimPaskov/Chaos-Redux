# Event 006 Border Commission Tooltip Tranche

## Scope

Parent-side patch for the Independence Wave Border Commission decision category. This tranche only improves player-facing requirement and effect reporting for the existing Border Commission decisions.

## Changed Files

- `common/decisions/006_independence_wave_decisions.txt`
- `localisation/english/006_independence_wave_l_english.yml`

## Decision IDs Updated

- `independence_wave_file_border_survey`
- `independence_wave_petition_border_parish`
- `independence_wave_request_league_arbitration`
- `independence_wave_offer_protected_transfer`
- `independence_wave_issue_dossier_ultimatum`
- `independence_wave_freeze_claim_under_observers`

## Implementation Notes

- Wrapped Border Commission availability and state-target requirements in custom trigger tooltips.
- Hid the raw scripted effect calls behind `hidden_effect`.
- Added custom effect tooltips that describe the visible outcome of each decision.
- Kept release identity, country scope, flag assets, package assignment, and formable routing unchanged.

## Validation

- Brace balance passed for:
  - `common/decisions/006_independence_wave_decisions.txt`
  - `common/scripted_effects/006_independence_wave_effects.txt`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`
- `localisation/english/006_independence_wave_l_english.yml` still has UTF-8 BOM.
- No trailing whitespace in touched text files.
- No `:0` localisation key pattern in `006_independence_wave_l_english.yml`.
- Targeted structural audit confirmed all six updated decisions contain:
  - `custom_trigger_tooltip`
  - `hidden_effect`
  - `custom_effect_tooltip`

## Remaining Risks

- This does not close the broader decision-feedback audit. Later package, formation, sealed-dossier, and other late-game decisions still need the same requirement/effect tooltip pass.
- This does not change the current display-only scripted GUI architecture.
- This does not add any bespoke package expansion for Kuban, Altai, or the niche generic release lane.
