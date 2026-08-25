# Event 006 primary scripted-localisation registry merge

Date: 2026-08-25

## Scope and outcome

This source-layout-only continuation removes one small Event 006 scripted-localisation parser file without changing player-facing wording, selector behavior, event reachability, or package admission.

The six wave-summary, presentation, and starting-force selectors from `common/scripted_localisation/006_independence_wave_scripted_localisation.txt` now live in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt` under an explicit source marker.

The former parser file is removed after its six executable `defined_text` blocks were copied as a complete unit.

The source file banner was replaced by the receiver's source marker to avoid duplicating a file-level comment block inside the registry; the executable body, selector comments, branch order, triggers, scopes, localisation keys, and fallback behavior are unchanged.

## Removed file

- `common/scripted_localisation/006_independence_wave_scripted_localisation.txt`

## Preserved selectors

- `GetIndependenceWaveLeaguePhase`
- `GetIndependenceWavePresentationArmedText`
- `GetIndependenceWavePresentationRegionText`
- `GetIndependenceWavePresentationHostText`
- `GetIndependenceWavePresentationNetworkText`
- `GetIndependenceWaveForceTemplateName`

The receiver now contains 24 top-level definitions and the Event 006 scripted-localisation directory contains 58 unique `defined_text` names with no duplicates.

## Static validation

- The six moved executable blocks compare equal to the original file body after line-ending normalization.
- The moved body has brace delta zero.
- The six selector identifiers occur exactly once in the receiver and nowhere else in the Event 006 scripted-localisation directory.
- The receiver has no duplicate `name =` identifiers across all Event 006 scripted-localisation files.
- The merged source saves 54 committed source bytes after deleting the former parser file.
- No localisation YAML, gameplay script, event, decision, category, interface, or asset file changed.

## Runtime evidence boundary

This handoff contains source and static evidence only.

No live MCP parser, event render, save/load, or in-game validation claim is made.

## Ownership and remaining separation

Focus, GUI, scenario, formable, and package-local scripted-localisation files remain separate because their surfaces have distinct ownership or lifecycle review boundaries.

This merge does not promote an unattested package, alter the 32/161 boundary, or change the Event 006 HOLD / PARTIAL disposition.
