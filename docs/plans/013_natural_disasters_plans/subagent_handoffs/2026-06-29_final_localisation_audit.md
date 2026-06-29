# Event 013 final localisation audit handoff

## Scope

Audited the current Event 013 Natural Disasters localisation, scripted localisation, GUI text, news text, achievement text, and event documentation after the recent main-agent patches.

## Files changed

- `docs/events/013_natural_disasters.md`

## Keys changed

- None.

## Behavior before and after

Before, the event documentation described the death model through internal helper wording and described achievement tracking as proof predicates.

After, the documentation describes the player-facing design result: percentage-based state losses have no fixed absolute victim ceiling, dense states can suffer larger absolute losses, and achievements follow actual warning, impact, recovery, and scenario outcomes.

## Dynamic localisation

No scripted localisation was added or changed.

## Validation

- Checked Event 013 event, news, decision, achievement, GUI, and scripted-localisation references against English localisation keys. No missing player-facing keys were found.
- Checked `localisation/english/013_natural_disasters_l_english.yml` and `localisation/english/chaosx_achievements_l_english.yml` for duplicate keys, forbidden `:0` keys, and UTF-8 BOM. No issue found.
- Checked `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt` for raw `§` or `£` format symbols and for output keys missing from Event 013 localisation. No issue found.
- Checked Event 013 scoped localisation and docs prose for em dashes and semicolons. No issue found after the docs wording patch.

## Remaining issues

- No localisation blockers found in the scoped files.
- The active indicator displays numeric deaths and incident counts by design. I did not change it because the parent prompt explicitly asked to verify the active indicator GUI alignment, and the current docs describe that display as intended.
