# Event 006 FORM-09 localisation registry merge

Date: 2026-08-25.

## Scope

The small FORM-09 Balkan Federation localisation file is now folded into `localisation/english/006_independence_wave_formable_registry_l_english.yml` under a source marker.

## Source-equivalence receipt

- The receiver contains one `l_english:` root.
- The receiver contains 225 unique localisation keys after the merge.
- The moved FORM-09 source contributes 26 non-root keys, including the BLX country-name ladder and FORM-09 category, decision, idea, and cancellation text.
- The moved 26-key source section matches `git show HEAD:localisation/english/006_independence_wave_form09_l_english.yml` after removing its root line and normalizing line endings.
- The receiver remains UTF-8 with BOM.

## Boundaries

Localisation keys and wording are unchanged, and FORM-09 identity, category, decision, formable, admission, and runtime behavior are unchanged.

This is a source-layout consolidation only and does not claim live tooltip or GUI evidence.

## Validation

The static receipt above was generated from the receiver and the pre-merge `git show HEAD:<source>` snapshot.

