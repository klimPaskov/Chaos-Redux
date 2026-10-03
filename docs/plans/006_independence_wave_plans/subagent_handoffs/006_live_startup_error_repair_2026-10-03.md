# Event 006 live-startup error repair (2026-10-03)

## Acceptance and evidence

The user supplied `docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log` from a live debug build launched from the current working tree and directed the parent to repair the listed Event 006 startup errors first. The log is pre-repair evidence; it cannot confirm the corrected source on a later startup.

## Changes

In `common/scripted_effects/006_independence_wave_host_response_effects.txt`, the Event 006 loss-count predicate at line 150 and the primary-host count and response-tier predicates at lines 331–334 now use `check_variable`. This preserves the accepted Event 006-only loss calculation, tier values, and deterministic response selection while preventing numeric variable names from being parsed as trigger names.

In `common/scripted_effects/006_independence_wave_opening_dispatch_effects.txt`, line 245 compares the already-maintained report-callback counter through `check_variable` before decrementing it.

In `common/scripted_effects/006_independence_wave_host_response_orchestration_effects.txt`, lines 234–235 use `clr_global_flag` for the report-response and host-response queue flags.

## Reference evidence

Offline wiki reference: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 565–569, documents `check_variable`, including the shortened strict comparison forms and their applicability to temporary variables. File SHA-256: `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.

Offline wiki reference: `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, lines 349–352, documents `clr_global_flag` as the effect that clears a global flag. File SHA-256: `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C`.

Installed game reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, lines 2110–2132, documents variable comparisons and shortened `check_variable` syntax. File SHA-256: `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29`.

Installed game reference: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, lines 2801–2808, documents `clr_global_flag` and its supported scope. File SHA-256: `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.

The `hoi4.reference_context`, `hoi4.reference_search`, and `hoi4.reference_read` tools are exposed.
After the initial context/search calls did not return, a narrower `clr_global_flag` search and revision-bound read with the explicit workspace ID succeeded and confirmed installed lines 2801–2809 at revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The narrowed `check_variable` search returned installed lines 2110–2135 at revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; the same section was also read directly from disk.
The focused source lookup for the host-response AI helper timed out after 600 seconds; its narrower one-line retry also timed out after 600 seconds.
Basic event lint for `.60`, with helper expansion disabled and four-node bounds, also timed out after 600 seconds; its one-node/one-edge retry timed out after 600 seconds as well.
The context bundle retry was narrowed to two sources with the explicit workspace ID and also timed out after 600 seconds.
The revision-bound `check_variable` read timed out at 26 lines, and its narrower five-line retry also timed out after 600 seconds; direct local reading supplied the same rules.
These failures do not supply final source or graph coverage, and no Event MCP render or engine execution result is claimed.
The live schema does not expose `hoi4.script_validate`, and its `source_lookup` schema does not include `view` or `keyPath`.

## Validation and remaining findings

Source review confirms that the callback counter is set, read, and decremented within the same dispatch path, and that the corrected global-flag calls clear the existing queue flags. The user owns live startup validation; this handoff does not claim that the copied error log is clean after the edits.

The cycle 1 log also reports a localization syntax error in `localisation/english/camp_administration_ui_l_english.yml` at line 181; duplicate entries under the vanilla special-project paths; three dynamic-token lexer errors without source paths; `black_friday_quote_cbrn_external_aid_pp_fee` called as an effect from Event 026; and five `index` calls parsed as effects in `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`. This Event 006 repair did not edit those files. They remain open whole-build QA findings and must be assigned to their owning work before claiming a clean full log.
