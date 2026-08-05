# Event 012 elephant localisation audit

Date: 2026-08-06

Scope: the new Event 012 armoured-elephant subunit, equipment, hidden technology, and named host-guard English localisation only.

## Changed files and keys

- `localisation/english/012_africa_elephant_l_english.yml`
  - `chaosx_elephant_desc`
  - `chaosx_elephant_equipment_1_desc`
  - `chaosx_africa_elephant_warfare_tech_desc`

No identifier, gameplay script, equipment definition, technology definition, scripted-localisation definition, GUI, asset, or achievement key changed.

## Coverage findings

The localisation file is UTF-8 with BOM and contains eight unique keys. The four expected visible identifiers all have a name and `_desc` key:

- `chaosx_elephant`
- `chaosx_elephant_equipment`
- `chaosx_elephant_equipment_1`
- `chaosx_africa_elephant_warfare_tech`

The subunit, archetype, equipment variant, and technology identifiers are referenced by the corresponding Event 12 unit, equipment, technology, and runtime-effect sources. The technology enables `chaosx_elephant_equipment_1` and `chaosx_elephant`, while the host and priority-member helpers grant the technology and stockpiles. The host formation intentionally keeps its literal division-template name because division-template names are runtime strings rather than localisation keys.

## Before and after display

Before the patch, three descriptions exposed implementation language: `vanilla elephantry`, `Event 012`, and the internal `bridge` metaphor. After the patch, the subunit description explains training, supply, armour, and battlefield purpose; the equipment description explains the standardised harness and stores; and the technology description explains the protection-charter standard.

### Prose repair summary

- Vagueness: no unused guard description is retained for the literal division-template name.
- Bloat: no material bloat remained after the rewrite.
- Obvious explanation: the equipment variant no longer announces itself as the first Event 12 pattern.
- Repetition: overlapping implementation labels were removed rather than repeated across the three descriptions.
- Overcomplication: the technology description now uses one direct sentence.
- Style-rule repair: all technical identifiers, implementation history, and vanilla-comparison language were removed from player-facing values.

No dynamic localisation was added or changed. No sourced or attributed quotation appears on this surface. No dynamic token, formatting code, cost, requirement, timer, actor, or state reference was present to preserve.

## Audit lists

- Missing keys: none among the four expected identifiers and their `_desc` companions.
- Duplicate keys: none in the elephant localisation file.
- Scripted-localisation issues: none; the new strings do not call scripted localisation.
- Dynamic text opportunities: none required for this static unit/equipment/technology surface.
- Cross-surface mismatch: none; the host formation's literal division-template name is not represented as a standalone localisation key.
- Encoding concerns: none; UTF-8 BOM remained intact after the patch.
- Sourced-quotation preservation: not applicable.

## Meaningful validation

- Parsed the file as eight single-line English localisation entries and confirmed all expected name/description pairs resolve uniquely.
- Scanned localisation values after the patch for `Event 012`, `Action 102`, `vanilla`, `bridge`, and raw `chaosx_` or `africa_` identifiers; none remain in displayed values.
- Confirmed the file still begins with `EF BB BF` and ends with a newline.
- `hoi4.tech_inspect` traced `chaosx_africa_elephant_warfare_tech` and produced `TECH_INSPECTED_PARTIAL`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76901b6ba919a3fa87b72106d32fa6e2feff9952fdbbaa4f6e76033c7f3a776e/c5022c7e2c94bc2c6690e413c7ed47c3bd5a90b8647fa26813f8fa50a36f8bdb/technology-trace-db7734c31ce7.json`.
- `hoi4.tech_render` produced a one-node technology render, also partial and not source-accurate because helper projections were deferred. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/687da17c2537cf5427e3abf99a9d18c84d46857d32d072cef88290d36349a470/e1b17aa6e40b1d23310a7d28ceea73b23b2d9fd2c6913dd1b5d48803a3cff207/technology-technology-db7734c31ce7.json`.

The MCP technology result is useful source-linked evidence but not complete engine validation. No in-game validation was run because that belongs to the user.

## Unresolved wording and ownership

The host formation remains intentionally named by its runtime division-template string; no unused localisation keys are retained for it. This audit did not change the hardcoded division-template name because that is gameplay-script ownership, not a localisation-only change.

The localisation file was already untracked when audited. This pass modified only its four description values and did not claim ownership of the other newly added elephant runtime files.

No broader simplification or fallback was introduced.
