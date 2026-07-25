# Event 006 localisation closeout

Audit date: 2026-07-26.

## Scope

This bounded pass closed the Event 006 English localisation style findings recorded in `006_localisation_audit_v5_2026-07-25.md`. It did not alter event logic, scripted localisation selectors, costs, or the accepted Event 006 wording direction.

## Changes

- Replaced the remaining Event 006 semicolon joins with sentence breaks in the Brittany, decisions, evolution, formable, Pacific, Rhineland-Bavaria, rival-bloc, Saar, scenario, Scotland-Wales, and shared report strings.
- Replaced the three scenario Universal Belligerence em-dash titles with colon titles and made the blocked-candidate ledger label explicit with a colon.
- Removed the Evolution 5 list of hidden route families from the public body. The post-collapse text now describes new sovereignty projects without exposing route categories before their reveal.
- Replaced the Saar Commission–Security typography with a plain hyphen while preserving the visible ledger name.
- Preserved the canonical SCN-008 ready split of 138 selectable map-bound packages, 55 selectable unbound packages, and 13 non-selectable route overlays.

## Files

The edited localisation files are the Event 006 English regional, decision, evolution, formable, GUI, Pacific, rival-bloc, Saar, scenario, report, Rhineland-Bavaria, Scotland-Wales, and Volga-Ural/Mesopotamian surfaces under `localisation/english/`.

## Validation

- All 34 scoped Event 006 English YML files still begin with the UTF-8 BOM.
- A repository scan of the scoped files finds no remaining semicolon or em-dash punctuation in the audited Event 006 values. En-dashes retained inside proper compound names remain intentional labels rather than sentence punctuation.
- The existing named `GetIndependenceWaveLeaguePhase` selector remains wired to the thirteen phase localisation keys, and the GUI displays that selector instead of a raw phase integer.
- No Hearts of Iron IV process was launched and no live consumer validation was run.

## Remaining risks

This closes wording and presentation findings only. Runtime reachability, package admission, asset provenance, and live GUI/Event Log playback remain governed by the completion audit and are not claimed here.
