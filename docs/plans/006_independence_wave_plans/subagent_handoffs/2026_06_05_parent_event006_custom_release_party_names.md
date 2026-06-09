# Event006 Custom Release Party Names

Date: 2026-06-05
Owner: parent Codex agent

## Change

Patched `localisation/english/chaosx_countries_l_english.yml`.

Added ideology party and party-long localisation for the six custom Event006 release tags:

- `ASN`
- `KBN`
- `PLM`
- `AYM`
- `DFR`
- `ZUL`

## Reason

The country-package audit confirmed these custom tags have country/history/tag/localisation/flag coverage and noted missing custom party-name localisation as remaining polish. Adding the party keys makes these new Independence Wave countries cleaner in the politics UI without changing release mechanics, focus assignment, route state, or candidate scope.

## Validation

Passed parent validation:

- UTF-8 BOM check passed for `chaosx_countries_l_english.yml`.
- Missing-key scan for the added party localisation keys returned no missing keys.
- Duplicate-key scan for the added party localisation keys returned no duplicates.
- Localisation version-key scan found no `:0` keys.
- Brace delta check returned zero.
- Scoped `git diff --check` passed.

## Remaining Scope

This does not complete Event006. It only closes the custom-party-name gap for the currently implemented custom release tags.
