# Event 010 Death Localisation Audit

Date: 2026-07-11

## Scope

Audited the completed maritime-evidence and custodial-policy tranche across:

- `common/decisions/010_death_decisions.txt`
- `common/scripted_localisation/010_death_scripted_localisation.txt`
- `common/script_constants/010_death_constants.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/dynamic_modifiers/010_death_state_modifiers.txt`
- `events/010_death.txt`
- `localisation/english/010_death_l_english.yml`

Read-only dependency checks covered the relevant Death scripted triggers and the registered decision sprites in `interface/010_death.gfx`. No gameplay, interface, or asset file was edited.

## Files changed

- `localisation/english/010_death_l_english.yml`
  - Corrected `death_send_survey_boat_desc`. The old text claimed that only one island file existed even though the decision can remain available after later reports. The description now remains accurate throughout the quiet investigation.
- `docs/plans/010_death_plans/subagent_handoffs/2026_07_11_death_localisation_audit.md`
  - Added this audit handoff.

## Evidence

- All 69 changed English keys have exactly one definition across the mod localisation tree.
- All 20 scripted-localisation names in the Death file are unique. All 68 localisation keys selected by that file resolve exactly once.
- All 96 explicit visible-key references from the audited decision and event files resolve exactly once.
- Pre-confirmation event text, case text, category text, survey text, and port-watch text do not name Death, Zol, No Ferry Returns, world end, or the Living Compact. Confirmed wording is selected only by country confirmation or public reveal. The aftermath title and status are selected only after defeat.
- Displayed evidence changes match the scripted values: first report `+2`, second report `+3`, telegraph work `+2`, the first quiet quarantine `+1`, weather closure `-3`, and the survey confirmation path. The confirmed survey text also matches the `-2` spread-pressure effect.
- Displayed custodial values match the scripted constants and effects. A state's first survey and first outpost grant `1` capacity each. Compact service at defeat grants `2`, qualifying defeat participation grants `2`, and policy costs are `1`, `2`, and `3`. Transit opening costs `20` command power, `200` support equipment, `100` motorized equipment, `6` trains, and `400` fuel. Upkeep costs `10`, `100`, `50`, `3`, and `250` respectively. Transit maintenance lasts `180` days.
- The policy-selection gate prevents replacing an established custodial policy. Survey and outpost capacity-claim flags survive reconsumption cleanup, so control changes and reconsumption do not recreate capacity. Memorial Stewardship's national benefit is protected by a country flag, gives `+3%` stability, reduces mourning debt by up to `2`, and can be received only once per country.
- Each of the eight decision icon identifiers used by the audited decision file resolves to one registered sprite in `interface/010_death.gfx`, and every referenced DDS file exists.
- `localisation/english/010_death_l_english.yml` retains the UTF-8 BOM bytes `EF BB BF`.

## Remaining risk

No blocker remains in the changed tranche. Five older Death-side soul-power custom-cost families do not define their derived `_tooltip` keys. They predate this tranche and were left untouched to preserve the bounded audit scope.

## Simplifications and blockers

No simplifications or fallbacks were used. No gameplay, interface, sprite, or asset corrections were needed for the audited tranche.
