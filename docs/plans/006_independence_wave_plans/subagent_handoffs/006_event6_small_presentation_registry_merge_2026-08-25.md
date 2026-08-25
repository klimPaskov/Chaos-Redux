# Event 006 small presentation-registry merge

Date: 2026-08-25

## Scope and outcome

This source-layout-only tranche reduces three small Event 006 parser files without changing gameplay, package admission, FORM-05 lifecycle behavior, or IW-005 overlay ownership.

The three FORM-05 scripted-localisation selectors and the IW-005 Flanders status selector now live in `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`.

The twelve FORM-05 sprite definitions now live in `interface/006_independence_wave_small_assets.gfx`.

Source markers identify both former files and preserve their ownership boundaries inside the shared registries.

## Removed files

- `common/scripted_localisation/006_independence_wave_form05_scripted_localisation.txt`
- `common/scripted_localisation/006_independence_wave_iw005_flanders_scripted_localisation.txt`
- `interface/006_independence_wave_form05.gfx`

## Preserved identifiers

The scripted-localisation registry preserves exactly these four unique names:

- `GetIndependenceWaveForm05Ledger`
- `GetIndependenceWaveForm05CapitalModel`
- `GetIndependenceWaveForm05DelegationStatus`
- `GetIndependenceWaveIW005FlandersInstitutionStatus`

The GFX registry preserves the twelve FORM-05 names and their original texture paths:

- seven FORM-05 decision sprites;
- three FORM-05 idea sprites;
- the FORM-05 formable emblem;
- the FORM-05 charter-congress report sprite.

No trigger, effect, decision, event, localisation YAML key, asset binary, package gate, or admission row changed.

## Validation

- The four moved scripted-localisation names occur exactly once in the receiver.
- Every moved FORM-05 sprite name occurs exactly once in the receiver.
- Receiver brace deltas are zero for the scripted-localisation and GFX files.
- `git diff --check` passes for the bounded source/doc changes.
- References in the FORM-05 and IW-005 system notes now point to the receiver registries with source markers.

This handoff contains source/static evidence only. It does not claim live parser, GUI, or in-game validation.
