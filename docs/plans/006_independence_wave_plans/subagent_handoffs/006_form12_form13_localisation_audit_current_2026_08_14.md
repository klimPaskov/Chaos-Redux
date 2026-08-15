# FORM-12/13 current localisation audit after the state-833 rebind

Date: 2026-08-14

Owner: `/root/current_formable_localisation_audit`

## Scope and disposition

This audit covers the current generated FORM-12 and FORM-13 localisation and scripted-localisation surfaces after the Mari El slot moved from state 256 to installed state 833. It also checks the linked consumer manifests, qualification helpers, grouped GUI references, current FORM-12/13 decision wording, accepted Event 006 formable specification, installed state-name localisation, and the nearest vanilla dynamic-state localisation patterns.

No gameplay file, workbook, generated localisation file, or scripted-localisation file was patched. No narrow current-reference localisation defect was proven, so this handoff is the only file added.

## Current state-833 coverage

Both complete consumer specs and manifests use the candidate set `249, 397, 399, 651, 833`, require four qualifying entries, and call their matching territory helpers:

- `docs/formables/state_registry/consumers/006_form12_state_puzzle.json`
- `docs/formables/state_registry/consumers/006_form13_state_puzzle.json`
- `docs/formables/state_puzzles/006_form12_state_puzzle/manifest.json`
- `docs/formables/state_puzzles/006_form13_state_puzzle/manifest.json`

Installed vanilla localisation resolves `STATE_833` as `Mari El`, and installed `history/states/833 - Mari El.txt` declares `name = "STATE_833"`, state id 833, and a MEL core. This matches the current Event 006 MEL package anchor.

The current generated player-facing keys are:

- `chaosx_formable_state_puzzle_independence_wave_form12_summary`
- `chaosx_formable_state_puzzle_independence_wave_form12_state_249_tt`
- `chaosx_formable_state_puzzle_independence_wave_form12_state_397_tt`
- `chaosx_formable_state_puzzle_independence_wave_form12_state_399_tt`
- `chaosx_formable_state_puzzle_independence_wave_form12_state_651_tt`
- `chaosx_formable_state_puzzle_independence_wave_form12_state_833_tt`
- `chaosx_formable_state_puzzle_independence_wave_form13_summary`
- `chaosx_formable_state_puzzle_independence_wave_form13_state_249_tt`
- `chaosx_formable_state_puzzle_independence_wave_form13_state_397_tt`
- `chaosx_formable_state_puzzle_independence_wave_form13_state_399_tt`
- `chaosx_formable_state_puzzle_independence_wave_form13_state_651_tt`
- `chaosx_formable_state_puzzle_independence_wave_form13_state_833_tt`

Each state-833 tooltip resolves `[833.GetName]`, current owner, current controller, the matching FORM-12 or FORM-13 qualification result, and ROOT's current core status. The generated scripted-localisation defines one state-833 sprite selector and one state-833 qualification selector for each formable. Both live counts include state 833, and both summary-status selectors call the same territory helper used by the owning state-puzzle contract.

## Stale state-256 review

No current FORM-12 or FORM-13 localisation key, scripted-localisation name, GUI tooltip reference, scripted-GUI property, GFX sprite, consumer entry, manifest entry, qualification helper, count branch, or territory helper contains `state_256`.

State-256 definitions still exist for the separate vanilla-compatible `form_idel_uralic_republic` consumer and for the universal state registry. Those definitions are not stale FORM-12/13 keys and must not be removed as part of this rebind audit.

Unreferenced legacy FORM-12/13 state-256 PNG and DDS files remain on disk as documented by `006_form12_form13_state833_asset_audit_2026_08_13.md`. They are asset-workspace cleanup, not localisation references, and were outside this localisation-only patch authority.

## Required localisation audit lists

### Missing keys

None in the audited FORM-12/13 generated surface. All twelve generated YAML keys exist once. The grouped GUI's two summaries and ten state tooltip references resolve to those keys. Every dynamic function referenced by those strings has exactly one `defined_text` definition.

### Duplicate keys

None. The generated YAML contains no duplicate key, and a repository-wide scan found each current FORM-12/13 key exactly once.

### Scripted-localisation issues

None proven. The complete generated scripted-localisation file contains no duplicate `defined_text` name. The FORM-12/13 surface has one definition for each sprite selector, qualification selector, qualifying-count selector, summary-status selector, and shared owner/controller/core selector it consumes. Qualification selectors use the current state helpers, counts use the same five candidates declared by the manifests, and summary status uses the current territory helper.

### Dynamic text opportunities

No required patch. Owner, controller, state name, qualification, core status, qualifying numerator, and final readiness are already dynamic. The denominator `4` is a build-time requirement mirrored from `summary_required_count = 4`; it is not a drifting runtime value. A future generator-wide refinement could replace the shared word `Unresolved` with a more explicit `Does not qualify`, but the current label is paired with live owner, controller, and core evidence and is not a state-833 reference defect.

### Cross-surface mismatch notes

No FORM-12/13 localisation mismatch was found. The decision descriptions require the carrier plus at least three consenting sovereign members with three unique controlled anchors. The puzzle displays the carrier and four eligible member anchors and requires four qualifying entries, which is the same carrier-plus-three-members rule. FORM-12 keeps the Volga-Ural federal register, while FORM-13 keeps the Idel-Ural religious-civic register.

The exact state-833 qualification helper additionally requires MEL to own and control state 833 and use it as its capital. The state-833 tooltip reports that helper's result rather than inferring qualification from the displayed owner or controller text.

### File encoding concerns

None for the runtime localisation YAML. `localisation/english/chaosx_formable_state_puzzles_l_english.yml` is strict UTF-8 with BOM. The linked decision localisation YAML is also strict UTF-8 with BOM. `common/scripted_localisation/chaosx_formable_state_puzzles.txt` is strict UTF-8 without BOM; it is a Clausewitz script file rather than a localisation YAML file, so the YAML BOM requirement does not apply.

### Prose-quality issues

- Vagueness: no blocking issue. Each tooltip names the state and labels owner, controller, formation status, and core status.
- Bloat: none. The state tooltip is a compact five-line factual display, and the summary is one line.
- Obvious explanation: none requiring removal. Owner, controller, qualification, and core status are distinct facts used to understand territorial eligibility.
- Repetition: the repeated field order is deliberate across state pieces and makes comparison easier; no sentence repeats the same consequence.
- Overcomplication: none. The strings avoid subordinate-clause stacks and administrative explanation.
- Style-rule repair: none required. The audited generated strings contain no em dash, semicolon sentence, implementation history, prompt fragment, hidden-mechanic explanation, or attributed quotation.

### Sourced-quotation preservation

No sourced or attributed quotation appears on the audited FORM-12/13 generated surface. No quotation was changed.

### Recommended fixes

No localisation fix is recommended for the state-833 rebind. Preserve the current keys in `localisation/english/chaosx_formable_state_puzzles_l_english.yml` and their matching definitions in `common/scripted_localisation/chaosx_formable_state_puzzles.txt` when the runtime generator is next run.

Asset owners may separately decide whether to delete the eight unreferenced legacy FORM-12/13 state-256 PNG/DDS artifacts identified by the state-833 asset audit. Do not delete the current `form_idel_uralic_republic` state-256 keys or shared state-256 owner/controller/core definitions.

## Meaningful validation

- Parsed both current consumer specs and manifests and confirmed complete status, the identical five-state candidate set, required count four, state-833 helper bindings, and current territory helpers.
- Checked the grouped GUI, GFX, scripted-GUI, scripted-localisation, localisation, and qualification-trigger source for current state-833 references and stale FORM-12/13 state-256 references.
- Scanned the generated YAML for duplicate keys and scanned all repository localisation YAML files for duplicate current FORM-12/13 keys.
- Scanned the complete generated scripted-localisation file for duplicate `defined_text` names and verified every FORM-12/13 dynamic function referenced from YAML resolves exactly once.
- Strictly decoded the two linked YAML files and generated scripted-localisation file as UTF-8 and checked BOM state.
- Compared the player-facing rule against the accepted Part 6 formable specification, FORM-12/13 registry rows, current decision descriptions, installed state history, installed state names, vanilla numeric-state localisation, and the official `State` localisation object contract.

## MCP evidence and blockers

The required read-only GUI inspection and rendering routes were called for `chaosx_independence_wave_formable_state_puzzle_window` with scenario id `form12_form13_localisation_current`.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/764535db077d1af1e83ca796fe58fc3211c2b1be551d8c01e35e56d7b7a2bfa5/cf004844950605e97008e828976bac47c52675c5475d08b0694c1b1f735fab2e/gui-inspect.bfed1fd8eadbbfc5.json`
- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9654598f01c40a19da62a51464f8e7698112a52589404fd484b76aaf61e8203f/8bbd65b4cd9fe06e2f619d672eec1f547890bad0e6c8d02b6ba34f8344b84491/chaosx_independence_wave_formable_state_puzzle_w-full.svg`

The inspect completed and identified the requested 93-element window, but its repository-wide source graph exceeded the diagnostic ceiling: 1,379 diagnostics were dropped, including 75 unresolved GUI references, and the combined GUI validation diagnostics were also truncated. The render completed for 1920x1080 and 1366x768 requests over normal, hover, long-text, and missing-localisation states, but returned one aggregate full-window SVG with a failed/empty validation result and no family-isolated overflow checks. Therefore the MCP routes provide useful linked source and render evidence, but they do not prove isolated FORM-12/13 tooltip overflow or family-specific visual acceptance. Source-only checks were not treated as equivalent visual evidence.

## Changed files and unresolved decisions

Changed file:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_form12_form13_localisation_audit_current_2026_08_14.md`

Changed localisation keys: none.

Dynamic localisation added or fixed: none.

Before and after display: unchanged; the current display already uses state 833 and contains no stale FORM-12/13 state-256 key.

Skipped meaningful validation: live in-game rendering was not performed because agents do not launch HOI4. Family-isolated MCP overflow acceptance remains unresolved for the exact diagnostic-budget limitation above.

Unresolved wording decision: none blocking. The optional generator-wide `Unresolved` wording refinement is outside this narrow state-rebind audit and should not be applied only to FORM-12/13.

Simplifications or fallbacks: none. No weaker substitute was used and no localisation defect was concealed.
