# Captured Biological Facility Localisation Audit

Date: 2026-07-22

## Scope

Audited only:

- `localisation/english/biological_facility_recovery_raids_l_english.yml`
- `common/raids/biological_facility_recovery_raids.txt`
- `common/raids/categories/chaosx_raid_categories.txt`
- `events/biological_facility_capture_events.txt`

The gameplay files were read only. No gameplay, asset, or other localisation file was edited.

## Audit result

The scoped localisation contains 45 expected keys with 45 definitions. There are no missing keys, unexpected keys, duplicate keys, or exact duplicates elsewhere in `localisation/english/*.yml`.

### Missing key list

- None. All 45 keys consumed by the requested category, raid, and event surfaces are defined.

### Duplicate key list

- None in the target file or across the English localisation directory.

### Scripted localisation issue list

- None. The target name uses the native `$LOCATION$` token, and the event descriptions use the correctly scoped regular event-target namespace.

### File encoding concerns

- None. The target file is valid UTF-8 with BOM and contains no `:0` keys.

The success-factor lookups are complete:

- `bio_facility_secure_hq_security` -> `success_modifier_bio_facility_secure_hq_security` and `_improvement`
- `bio_facility_secure_high_hazard` -> `success_modifier_bio_facility_secure_high_hazard` and `_negative`
- `bio_facility_destroy_hq_security` -> `success_modifier_bio_facility_destroy_hq_security` and `_improvement`
- `bio_facility_destroy_high_hazard` -> `success_modifier_bio_facility_destroy_high_hazard` and `_negative`

The raid target key `raid_target_name_biological_captured_facility_state` uses `$LOCATION$` as required by the native raid target UI. The five event descriptions use `[bio_facility_notice_state.GetName]`. This is the correct localisation namespace for the regular event target saved as `bio_facility_notice_state`; the `event_target:` prefix belongs in script scope syntax, not in this localisation reference. No scripted-localisation issue was found.

The localisation is valid UTF-8 with BOM (`EF BB BF`). No `:0` keys or indented localisation keys were found. No decision, administrative-order, deploy, or deployment wording remains in the scoped localisation. The raid source uses native land raid arrows, and the report events only acknowledge completed accounting.

## Changed files and keys

Changed files:

- `localisation/english/biological_facility_recovery_raids_l_english.yml`
- `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-22_biological_captured_facility_localisation_audit.md`

Changed localisation keys:

- `tooltip_raid_category_biological_facility_recovery_raids`
- `biological_facility_recovery_raid_available_tooltip`
- `bio_facility_capture_secure_failure_tt`
- `bio_facility_capture_destroy_failure_tt`
- `cbrn_bio_facility.2.a`
- `cbrn_bio_facility.3.a`
- `cbrn_bio_facility.4.desc`
- `cbrn_bio_facility.4.a`
- `cbrn_bio_facility.5.a`
- `cbrn_bio_facility.6.a`

## Before and after

- The category tooltip described only a failed entry. It now describes a failed operation, which covers both secure and destroy routes.
- The category availability text previously mixed category-level site control with per-raid technology checks and referred to an administrative-order launch. It now states the player-facing site, technology, formation, and land-operation requirements without implying a decision launch.
- The five report-event options previously used action-like wording despite having no effects. They now acknowledge the completed capture, loss, breach, release, or recovery report.
- Failure and breach text previously promised attribution and Condemnation. The lifecycle only produces those records when surviving custodian proof exists, so the text now makes that condition explicit and describes spread as a risk.

## Dynamic text opportunities

- Existing target and state-name dynamic localisation is sufficient and was retained.
- The secure and destroy limited-result strings show the nominal 40 percent and 50 percent fractions from the current raid constants. The helper also enforces a minimum release or transfer of one unit, so very small ledgers can display a nominal percentage that does not equal the rounded amount. This is a wording decision for a future gameplay/localisation pass, not a missing key.
- Command power, equipment reservations, and raid timing are supplied by the native raid UI and are not missing localisation keys in this file.

## Cross-surface notes

- All category, raid-type, target, availability, launchability, success-modifier, success-level, event-title, event-description, and event-option keys consumed by the three requested source surfaces are covered.
- The current `.6.desc` wording about a replacement arsenal remaining active was present during this audit and was preserved as an unrelated concurrent edit.

## Validation and skipped checks

Meaningful checks run:

- Exact scoped key audit: 45 references expected, 45 definitions, 0 missing, 0 unexpected, 0 duplicates.
- Exact duplicate scan across English localisation: 0.
- BOM and UTF-8 validation: valid BOM and UTF-8.
- Source-to-localisation event-target check: four `save_event_target_as = bio_facility_notice_state` sites and five matching event-description references.
- Decision-launch language scan of the scoped localisation: 0 hits.

A read-only event inspection was attempted for `cbrn_bio_facility.2` and `events/biological_facility_capture_events.txt`, but the artifact tool stopped at `EVENT_NODE_LIMIT` with 103456 nodes over its 100000-node limit and returned no artifact URI. In-game raid rendering and live engine validation were therefore skipped. No gameplay source was changed to compensate.

No unresolved key-coverage, encoding, event-target, success-modifier, or decision-launch localisation issue remains.

## Recommended fixes

The ten small wording fixes listed above were applied in `localisation/english/biological_facility_recovery_raids_l_english.yml`. No gameplay-side fix is recommended from this audit.

## Parent remediation after audit

The completion audit subsequently promoted the assigned Biological Security Section from an optional bonus to a fail-closed requirement. The parent added six native success-modifier localisation keys for the secure and destroy requirement factors and revised the category/launch text accordingly. It also separated minimum-one accidental-release rounding from limited secure/destroy fractions, removing the low-stock wording caveat recorded above. The localisation surface now contains 51 unique gameplay keys plus the `l_english` header; the earlier 45-key count remains the evidence for the exact source version reviewed by this auditor.
