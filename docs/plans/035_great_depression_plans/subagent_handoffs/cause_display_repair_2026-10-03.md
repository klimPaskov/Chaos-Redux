# Event 35 distinct cause display

## Disposition

Implemented presentation repair under the user's requirement to show the current causes alongside Severity, phase, trend, threshold, and relapse state.
The existing order remains worldwide contraction, organized social unrest, contagion, inherited boom collapse, and opening shock.
This repair changes no hidden component, Severity calculation, probability, actor, or crisis state.

## Source changes

`common/scripted_localisation/035_great_depression_localisation.txt` keeps the first cause unchanged.
The second and third cause selectors return comma-prefixed optional suffix keys.
The third-slot opening shock now requires two preceding active causes, preventing it from repeating the second-slot opening shock.
When fewer causes exist, the remaining slots return the intentional empty `great_depression.causes.no_suffix` string.

`localisation/english/035_great_depression_l_english.yml` composes the first cause with those optional suffixes in the six opening report variants and national category description.
The obsolete repeated `great_depression.causes.none` fallback is replaced by four explicit additional-cause keys and the empty suffix.
No unconditionally printed comma remains between the three selectors.

## Validation

A read-only parser evaluated the actual three selector bodies over all 32 combinations of the five input flags.
Each result matched the first three active causes in the preserved priority order, with no duplicate or missing cause and no repeated fallback.
The all-false case returned domestic contraction only.
The inherited-plus-opening case returned boom collapse and opening shock only.
The all-true case returned worldwide contraction, organized social unrest, and financial contagion.
This truth table proves the source Boolean selection, not an in-game render or broader event outcome.

Scripted-localisation SHA-256: `480B6DDC014E80A1B084FF09EFBEDA54B62CAA8BE253D13D153FE8B4B2295005`.
English localisation SHA-256 after the display repair: `17296885CFBCD17C568926B63B7F4B3505A1851F6C85721741ED8E9EC22BC1FD`.

## References and live evidence boundary

Offline `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`, lines 655 to 696, and installed `common/scripted_localisation/00_scripted_localisation.txt`, lines 1 to 36, establish first-matching selector and fallback behavior.
The exact reference hashes are retained in `cost_contract_repair_2026-10-03.md`.
The supplied cycle-one log is `docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log`, SHA-256 `EDB523793E8C7EA1C79FF53546B1CFE5789C498217160191C9B022F09A85BAB3`.
It has no Event 35 identifier or path matches, and the orchestrator reported that the main menu loaded.
That log does not prove this later cause display or the new cleanup callback.
The connected tool list temporarily exposed no HOI4 routes after the interrupted connection.
The routes subsequently returned after the resource-template handshake, but a retry narrowed to one eight-line `great_depression_clear_conversion_frame` definition still terminated after 600 seconds without an artifact.
The exposed source-lookup schema lacks the newer `view` and `keyPath` fields, and no `script_validate` route is exposed.
No MCP equivalent or live render is claimed.
