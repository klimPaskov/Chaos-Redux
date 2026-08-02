# Biological Localisation Copyedit Handoff

## Scope

Copyedited player-facing prose only in the English localisation files whose filenames begin with `bio`.

The pass removed semicolon joins, contrast formulas, generic explanatory phrasing, and abrupt result chains while preserving localisation identifiers, dynamic tokens, formatting codes, displayed values, conditions, outcomes, and gameplay meaning.

## Files changed

- `localisation/english/biological_battlefield_raids_l_english.yml`
- `localisation/english/biological_facility_recovery_raids_l_english.yml`
- `localisation/english/biological_sabotage_l_english.yml`
- `localisation/english/biological_sabotage_raids_l_english.yml`
- `localisation/english/biological_strategic_raids_l_english.yml`
- `localisation/english/biowarfare_disease_containment_l_english.yml`

`localisation/english/biological_stockpile_safety_l_english.yml` was reviewed and required no copyedit.

Pre-existing additions in `biowarfare_disease_containment_l_english.yml` were preserved.

## Validation

- Confirmed all seven scoped files retain UTF-8 BOM encoding and the `l_english:` header.
- Confirmed every nonblank localisation entry remains a single quoted value with a valid key shape.
- Confirmed no em dashes, semicolons, `Otherwise`, `however`, `but`, `rather than`, or `This is` constructions remain in the scoped files.
- Reviewed the scoped diff to confirm no gameplay scripts, identifiers, dynamic tokens, formatting codes, or displayed values were changed by this copyedit.

## Simplifications, omissions, and blockers

No simplifications or omissions were made. No gameplay mechanics or scripts were edited.
