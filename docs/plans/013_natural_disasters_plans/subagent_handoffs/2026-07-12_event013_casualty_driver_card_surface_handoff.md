# Event 013 casualty-driver and card-surface handoff

Date: 2026-07-12

> Historical handoff snapshot. The source-asset retention decision mentioned in the original validation note was outside this tranche at the time; the 1,035-file Event 013 source/provenance archive is now retained under `docs/assets/013_natural_disasters/`. Current retention and completion status live in the manifest and final completion audit.

## Scope

This tranche closes accepted improvement-loop Parts 7 and 8 for casualty vulnerability and shared aftermath presentation. It adds gameplay-significant, family-aware casualty exposure, preserves one explanation of the strongest observed driver, and exposes the same stable facts on live aftermath cards and abnormal-history records.

## Changed files

- `common/script_constants/013_natural_disasters_constants.txt`
  - adds `natural_disaster_death_driver`, `natural_disaster_relief_status`, `natural_disaster_death_driver_factor`, and `natural_disaster_death_driver_priority` tables;
- `common/scripted_effects/013_natural_disasters_effects.txt`
  - adds `natural_disaster_apply_death_driver_candidate`, `natural_disaster_prepare_death_driver_profile`, and `natural_disaster_set_foreign_relief_status`;
  - applies and caps exposure multipliers before shared Deaths registration;
  - initializes new-card cumulative deaths, casualty driver, and relief state;
  - prepares family-group context for chain and neighbor losses;
  - preserves cumulative card deaths across repeats and causal follow-ups;
  - snapshots family group, casualty driver, cumulative deaths, and relief state through abnormal append, update, copy, and clear paths;
- `common/decisions/013_natural_disasters_decisions.txt`
  - records route-secured, refused, withdrawn, arrived, and misdirected relief states at their decision or mission transitions;
  - donor selection records pledged through the shared physical-route helper;
- `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt`
  - adds live and abnormal-selected family-group, casualty-driver, and relief selectors;
  - adds conditional card timing for scheduled impact, reassessment, and pending assessment;
- `localisation/english/013_natural_disasters_l_english.yml`
  - adds player-facing group, driver, relief, and timing text;
  - expands the live aftermath and abnormal selected-record details;
- `docs/events/013_natural_disasters.md`
  - documents casualty tuning, latest versus cumulative deaths, combined damage-summary disposition, relief states, snapshot fields, and direct versus internal causal API authority;
- `docs/plans/013_natural_disasters_plans/013_event_completion_final_audit.md`
  - records Parts 7 and 8 closure;
- `docs/plans/013_natural_disasters_plans/013_implementation_validation_notes.md`
  - records the static trace, balance cap, and added live-engine scenarios.

## Gameplay and presentation contract

- Applicable named exposure factors multiply together but are clamped to `natural_disaster_death_driver_factor.maximum_combined`, currently `1.35`.
- The display driver is chosen by an independent priority table, not by effect order.
- `natural_disaster_last_deaths` remains latest-impact data for reports and spike checks.
- `natural_disaster_total_deaths` is card-cumulative and is the live/history display value.
- The Damage row intentionally combines impact signature and primary damage profile. No redundant second row was added.
- Relief progresses through none, pledged, route secured, arrived, misdirected, refused, or withdrawn. Warning-era and legacy records have safe defaults.
- Warning cards show their scheduled impact date. Reassessment formatting is used only when a recovery reassessment exists.

## Documentation and catalog alignment

The Event Details premise and evolution wording did not change. No spreadsheet cells or event-detail localisation required an update for this tranche.

## Validation status and remaining risk

Static validation covers constant references, aligned abnormal arrays, live and GUI selector coverage, localisation references, brace balance, and UTF-8 BOM retention. The repository has no deterministic headless HOI4 scenario harness, so representative driver selection and cap behavior, repeated-card cumulative deaths, warning timing, and all relief lifecycle labels remain in the queued live-engine matrix. The source-asset archive note above is historical; current retention is verified by the manifest and final audit.

No fallback or gameplay-surface simplification was used.
