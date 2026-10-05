# Event 008 forced-context localisation, 2026-10-05

Disposition: implemented localisation patch, pending parent flag lifecycle integration and review.
Acceptance basis: explicit parent assignment for reports whose mechanics are skipped during terminal world state or a baseline full-tension incident.

## Changed source and keys

- `localisation/english/008_world_tension_rises_l_english.yml`
- `common/scripted_localisation/008_tensions_rising_scripted_localisation.txt`

Added wording:

- `chaosx.nr8.terminal.d`: "The crisis has moved beyond diplomatic restraint."
- `chaosx.nr8.terminal.a`: "Diplomacy cannot contain this."
- `chaosx.nr8.terminal.effect`: "This report adds no world tension or chaos."
- `chaosx.nr8.baseline.full_wt.effect`: "World tension is already at its limit. This report adds no tension."

`GetTensionsRisingMainDesc`, `GetTensionsRisingOption`, and `GetTensionsRisingEffectText` now prioritize country flag `tensions_rising_report_terminal` ahead of stored stage IV through I.
The effect getter checks `tensions_rising_report_baseline_full_world_tension` after all evolved stages and before its normal baseline fallback.
Description and option keep their normal baseline text in the full-tension context.
Normal stage packet copies, existing YAML keys and integer `|0` formatting remain unchanged.
Terminal and full-tension branches read no numeric value and apply no effects.

## Before and after

Previously terminal reports displayed normal staged prose and numeric tension or chaos gains even when the owner skipped those effects.
They now describe a crisis beyond diplomatic restraint and show a no-gain tooltip.
Previously a baseline report at full tension could display a tension gain.
It now states that tension is at its limit and the report adds none.
No update history or Settings reference appears in the new strings.

## Validation and limitations

All nineteen reachable scripted output branches resolve to plain-text YAML values.
Terminal branches are first in each of the three requested getters.
The full-tension baseline branch follows evolved stages and precedes baseline.
No old number formatter, dynamic token, quotation or existing prose was altered.
The YAML UTF-8 BOM and script plain UTF-8 encoding were retained.
No missing or duplicate new key was found.
The colour audit command and result will be appended after execution.

Parent owns setting both country flags before popup display and clearing them when its option is acknowledged.
The unused `chaosx.nr8.terminal.t` key was removed at the parent's request.
The terminal context retains the static root title `chaosx.nr8.1.t`, "Tensions Rising", and appears through its description, option and effect getters.
No event, effect, trigger, GUI or shared file was edited.
MCP inspection/rendering remains blocked by the previously documented uncallable routes, so source validation does not establish visual wrapping or runtime execution.
No artifact URI was produced.

## Evidence and skill

Applied the previously read event skill numeric `defined_text` guidance, preserving literal YAML keys and number formatting.
First-match scripted localisation behavior is documented in the previously read offline Localisation wiki lines 656-691.
Full reference paths and hashes remain in `localisation_audit_2026-10-05.md`.
No skill files changed, staging or commit performed.
`python .tools/report_colour_audit.py --event 008` returned `total keys with colour: 0` after this patch.

## Final title cleanup

Removed only the unused terminal title key from the YAML.
Assigned root event and scripted output key coverage found no missing keys.
The root title remains static in normal and terminal contexts.
The final terminal additions are `.terminal.d`, `.terminal.a`, `.terminal.effect` and `.baseline.full_wt.effect`.
No script, dynamic formatter or getter changed during this cleanup.
After title cleanup, assigned coverage resolved all 59 root-event and scripted output references, and `python .tools/report_colour_audit.py --event 008` again returned `total keys with colour: 0`.

## Final controller and visible-report coverage audit

Read-only follow-up after the owner split hidden controller `chaosx.nr8.1` from visible report `chaosx.nr8.16`.
The visible report reuses the resolved `chaosx.nr8.1.t`, `.d`, `.a`, and `.a.tt` keys.
All 60 unique event/scripted localisation key references resolve, and all 21 literal scripted output branches resolve.
The three getter calls in YAML resolve to their scripted definitions.
Direct report titles/descriptions/options and reachable scripted output values contain no colour characters.
The actual aggregate key is `chaosx.nr8.aggregate.effect`, with the normal `chaosx` prefix.
It is colour-free and preserves both integer `|0` display tokens.
No duplicate key was found in the assigned YAML.
The YAML UTF-8 BOM remains.

No achievement localisation key lives in the assigned Event 008 YAML, and the controller/report split adds no achievement tooltip consumer there.
The parent-owned achievement tooltip edits need no further change in this file.
Those external achievement surfaces were not audited or modified by this bounded follow-up.

The numeric effect getter now includes terminal, stage IV-I, aggregate-chaos, positive-baseline-tension, full-tension and baseline fallback outputs.
The earlier fallback warning is superseded by the owner's source correction.
The final baseline fallback trigger now assigns `tensions_rising_display_world_tension = tensions_rising_report_world_tension` before selecting `chaosx.nr8.baseline.effect`, so it does not reuse a stale display temporary.
The stored report context and no-effect flags remain parent-owned.
The prior MCP route blocker and rendered-validation limitation remain.
No source file was patched during this audit, only this handoff was updated.

Source revisions for this follow-up:

- `localisation/english/008_world_tension_rises_l_english.yml`: SHA-256 `08700adaf263a060e22ec85123b096dbe048323c8d16ea4d4f7c1d7eb3930bc6`.
- `common/scripted_localisation/008_tensions_rising_scripted_localisation.txt`: SHA-256 `0e5f498dc0c807e6f69b033f6477b6d38895f59621533fa07ca58870de9e334d`.
- `events/008_tensions_rising.txt`: SHA-256 `3ecdb17ba1937b4baaef5ae24b4cedc50171d1083e4ea5747b5105d4d9fda4a3`.
Final controller/report colour audit: `python .tools/report_colour_audit.py --event 008` returned `total keys with colour: 0`.

Handoff correction, 2026-10-06: read the current fallback assignment and verified its scripted-localisation source hash.
The earlier 60-reference, 21-branch and zero-colour audit results are retained.
Only this handoff was edited.
