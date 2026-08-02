# Camp, Fallout, Germany, and Japan Localisation Copyedit Handoff

## Scope

Copyedited existing player-facing prose in the English localisation files whose filenames begin with `camp`, `fallout`, `germany`, or `japan`.

The pass removed semicolon joins, explicit thesis-versus-antithesis constructions, abrupt dramatic sentence chains, staged official-response contrasts, and visible fiction or biology disclaimers. Localisation identifiers, dynamic tokens, formatting codes, displayed values, conditions, outcomes, and gameplay meaning were preserved.

## Files changed

- `localisation/english/camp_repression_country_kits_l_english.yml`
- `localisation/english/camp_repression_rework_l_english.yml`
- `localisation/english/fallout_consolidated_l_english.yml`
- `localisation/english/germany_mengele_l_english.yml`
- `localisation/english/japan_biological_campaign_l_english.yml`

Thirty-four localisation entries were copyedited. No mechanics, gameplay scripts, identifiers, or localisation keys were changed.

## Validation

- Confirmed all five changed files retain UTF-8 BOM encoding and the `l_english:` header.
- Confirmed every nonblank localisation entry remains a single quoted value with a valid key shape.
- Compared all changed entries with `HEAD` and found no changes to dynamic tokens, formatting codes, icons, or displayed numbers.
- Confirmed no em dashes or semicolons remain in any scoped file.
- Reviewed the scoped diff to verify that edits are limited to player-facing prose.

## Simplifications, omissions, and blockers

No simplifications, omissions, or blockers remain within the assigned filename scope.

## Parent follow-up

Include these five localisation files and this handoff in the parent style-cleanup review and commit.
