# Event 012 Africa Bestiary Role Spirit Cleanup

Date: `2026-06-17`

Owner: parent implementation pass

## Changed files

- `common/scripted_effects/012_africa_effects.txt`

## Gameplay surface

`africa_remove_created_country_role_spirits` now removes all created-country role spirits for the expanded Africa country package set.

## Identifiers added to cleanup

- `africa_chimpanzee_telegraph_league_seat`
- `africa_okapi_court_seat`
- `africa_termite_citadel_engineers_seat`
- `africa_honeyguide_commons_seat`
- `africa_great_herds_compact_seat`

## Before

The helper removed the original sixteen role spirits but omitted the five expanded Bestiary seats. Those five ideas are added by `africa_generate_created_country_role_staff`, so a cleanup path could leave stale role spirits on recreated, transformed, or refreshed actor packages.

## After

The cleanup helper covers all twenty-one created-country role spirits currently added by Event 012 country-package setup.

## Validation

- Confirmed the five added cleanup IDs match the ideas defined in `common/ideas/012_africa_ideas.txt`.
- Confirmed the same five IDs are added by `africa_generate_created_country_role_staff`.

## Remaining issues

This pass does not address broader country-package audit items such as full bespoke minister/commander pools, starting OOB files, or per-tag focus AI depth. Later follow-ups added static OOBs and two generated advisors per created actor, but this cleanup handoff remains scoped to role-spirit wording.
