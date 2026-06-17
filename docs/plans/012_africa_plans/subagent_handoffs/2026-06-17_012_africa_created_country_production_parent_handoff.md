# Event 012 Created-Country Production Parent Follow-Up

## Scope

Resolved the country-package auditor's medium finding that several Event 012 created actors received only the shared support-equipment production line from `africa_apply_created_country_production_package`.

## Gameplay Changes

- Added `africa_created_country_add_motorized_production`.
- Added `africa_created_country_add_train_production`.
- Kept the existing one-time package flag `africa_created_country_production_package_applied`.
- Added infantry production lines for `BBS`, `ANW`, and `OVN`.
- Added motorized production lines for `SAH`, `EAC`, `CRR`, and `OKP`.
- Added train production lines for `SAH`, `NHR`, `EAC`, and `TRM`.

## Country History Changes

- `SAH`, `EAC`, `CRR`, and `OKP` now start with `motorised_infantry`.
- `SAH`, `NHR`, `EAC`, and `TRM` now start with `basic_train`.

## Remaining Country-Package Risks

- Parent follow-up: static land OOB files were added for all 21 Event 012 created tags in `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_country_static_oob_handoff.md`.
- Parent follow-up: small static naval OOBs now cover `MAG`, `EAC`, `IOC`, `TDM`, `CRR`, `WAC`, `CBC`, `ANW`, and `OVN`; small static air OOBs now cover `MAG`, `IOC`, `OVN`, `NHR`, and `SLC`.
- Parent follow-up: created-country focus and AI behavior now have tag-specific capstone focuses and AI postures in `common/national_focus/012_africa_authority_focus.txt` and `common/ai_strategy/012_africa.txt`; the actors still do not have full bespoke country focus trees.
- Each created actor now has two generated role/support advisors; full country-specific minister and commander rosters remain future depth.
