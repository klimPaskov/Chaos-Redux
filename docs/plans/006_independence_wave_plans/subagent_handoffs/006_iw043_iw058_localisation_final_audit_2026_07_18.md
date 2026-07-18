# IW-043 / IW-058 localisation final audit handoff

Date: 2026-07-18
Scope: final English player-facing text for Event 6 Middle Volga (IW-043), Assyria (IW-058), FORM-12/13/18 settlement surfaces, shared decision/focus ids, the two package achievements, and the current staged-integration decision text.

## Documentation reconciliation note (2026-07-18)

The localisation audit remains current for key coverage, duplicate-key checks,
player-facing wording, and encoding evidence. Its earlier note that sovereign
autonomy ordering was an unresolved gameplay blocker is superseded by the
current wiring: the autonomy decision writes compact/mode records and the
final ratification focus is the sole `.5810` caller. This text audit does not
claim whole-Event 006 runtime completion.

## Patch applied

Changed files:

- `localisation/english/006_independence_wave_iw043_iw058_events_l_english.yml`
  - Replaced implementation-facing category wording in `chaosx.nr006.4301.a.tt` and `chaosx.nr006.5801.a.tt` with player-facing founding-authority wording.
  - Removed `carrier`, `Event 6 generation`, `Event 6 origin`, and country-package language from the new consent/founding surfaces: `chaosx.nr006.4311.a.tt`, `chaosx.nr006.4312.a.tt`, `chaosx.nr006.4312.b.tt`, `chaosx.nr006.5811.desc`, `chaosx.nr006.5811.a.tt`, `chaosx.nr006.4313.desc`, `chaosx.nr006.4314.desc`, and `chaosx.nr006.5812.desc`.
  - Consent now reads as a sovereign constitutional choice; founding text names staged charter, defense, revenue, and autonomy work without exposing implementation provenance.
- `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
  - Clarified staged-integration descriptions: `independence_wave_iw043_register_form12_member_charters_desc`, `independence_wave_iw058_register_form18_member_charters_desc`, and `independence_wave_iw058_coordinate_form18_defense_and_revenue_desc` now state preservation of member sovereignty and civilian control rather than referring to Event 6 origins or a “free-unit loop.”
  - Existing FORM-12/13/18 consent-count, anchor, settlement-mode, cost, and timer text was retained after cross-checking its values against the package and shared decision constants.
- `localisation/english/006_independence_wave_iw043_iw058_focus_l_english.yml`
  - Removed the concurrent duplicate title/description definitions for `independence_wave_iw043_repair_cheboksary_workshops` and `independence_wave_iw058_fortify_mountain_river_corridor`; the decision localisation remains the single title/description source while focus-specific `_tt` keys remain. The file has no net diff against its baseline after cleanup.

No country-core, achievement, gameplay, scripted-localisation, or asset file was changed in this final narrow pass. Existing achievement text and all country-core keys were audited; the parent may still add politics keys in country-core separately.

## Required audit output

### Missing keys

None in the scoped surfaces.

- 40 actual IW-043/IW-058 decision blocks have title and `_desc` keys.
- All 48 national focuses have title, `_desc`, and `_tt` keys; shared Cheboksary and Mountain–River title/description ids resolve from decision localisation.
- All 200 `chaosx.nr006.*` references in `events/006_independence_wave_iw043_iw058.txt` resolve in the event localisation.
- `chaosx_006_volga_bulgaria_NAME/DESC` and `chaosx_006_assyria_survives_NAME/DESC` resolve in the achievement localisation.

### Duplicate keys

None across the six scoped English files:

- `006_independence_wave_iw043_iw058_categories_l_english.yml`
- `006_independence_wave_iw043_iw058_country_core_l_english.yml`
- `006_independence_wave_iw043_iw058_decisions_l_english.yml`
- `006_independence_wave_iw043_iw058_events_l_english.yml`
- `006_independence_wave_iw043_iw058_focus_l_english.yml`
- `006_independence_wave_achievements_l_english.yml`

The previously duplicated pairs are now single-source decision ids: `independence_wave_iw043_repair_cheboksary_workshops`/`_desc` and `independence_wave_iw058_fortify_mountain_river_corridor`/`_desc`.

### Scripted-localisation issues

None found. Dynamic target surfaces already use `[FROM.GetNameDef]` for targeted decisions and saved event-target scopes for the diaspora and named-guarantee event chains. No broken `custom_effect_tooltip`, `custom_cost_text`, or event localisation reference was found in the scoped source.

### Dynamic text opportunities

- The targeted decision names and descriptions already expose the selected `[FROM.GetNameDef]`; no additional target patch is needed.
- Cost and timer strings remain literal display text in the scoped decision file, but the displayed values were cross-checked against `common/script_constants/006_independence_wave_decision_constants.txt` and `common/script_constants/006_independence_wave_iw043_iw058_constants.txt`. They currently match (including the package-specific 15/30 command-power values), so this narrow pass did not replace them with constant interpolation.
- Staged integration decisions use constant-backed `days_remove` (90/120 days) and generic dynamic cost localisation in source; they do not call bespoke start/timeout/cancel tooltip keys. If the UI later needs explicit stage timers in the card, add those keys alongside the owning decision change rather than inventing unused localisation.
- FORM-12/13/18 descriptions now expose consent counts, unique controlled anchors, and settlement-mode requirements. The member list itself is not safely available as a localisation scope, so no speculative scope expression was added.

### Cross-surface mismatch notes

- Event invitation/founding prose now agrees with decision descriptions: consent preserves sovereignty, founding creates a constitutional carrier/center only in player-facing terms, and later integration is staged.
- Stage descriptions explicitly distinguish first-stage registration from later defense/revenue integration; no annexation, subject creation, blanket core grant, or unaccountable standing force is implied.
- Earlier focus/decision audits recorded a gameplay-level sovereign-autonomy
  ordering concern. Current wiring keeps the compact/mode decision records and
  the final-proof `.5810` presentation on the ratification focus; any remaining
  parent review is a closeout verification, not a localisation defect.
- Former-host transit remains a generic “former host” card because the stored event-target scope was not exercised in a live decision-card render; no risky dynamic scope was introduced.

### File encoding concerns

All six scoped English files retain UTF-8 BOM encoding, `l_english:` headers, and no `:0` keys. No encoding conversion was introduced.

### Recommended fixes / follow-ups

1. Keep the parent gameplay review on the FORM-18 sovereign-autonomy/final-proof ordering and staged integration gates; localisation now describes the intended order but does not change it.
2. If future tuning changes package costs or durations, migrate the corresponding `_cost`, `_blocked`, `_tooltip`, and `_start_tt` strings to the existing constant interpolation pattern so UI cannot drift from script.
3. If a read-only decision-card render confirms safe former-host event-target scope, consider a dynamic former-host name in `independence_wave_iw043_negotiate_former_host_transit`.

## Validation

Read-only audit after patch:

- BOM and `:0` scan: all six scoped files passed (`BOM=True`, `NO_COLON0=True`).
- Internal and cross-file duplicate scan: zero duplicates.
- Focus coverage: 48 ids, no missing title/description/tooltip keys.
- Decision coverage: 40 actual IW-043/IW-058 blocks, no missing title/description keys.
- Event coverage: 200 exact event localisation references, no missing keys.
- Implementation-vocabulary scan over target event/decision/focus localisation: no remaining `Event 6`, `carrier`, `generation`, `origin`, `country package`, `country content`, `free-unit`, or “starting values” wording.

Skipped meaningful validation: no in-game localisation/UI render was run because this was a bounded text-only audit and the parent did not request a render. No assets were created or validated.

Unresolved wording decisions: whether future cards should interpolate package constants directly, and whether the former-host decision card can safely resolve its stored event target. Both are documented opportunities rather than silent assumptions.
