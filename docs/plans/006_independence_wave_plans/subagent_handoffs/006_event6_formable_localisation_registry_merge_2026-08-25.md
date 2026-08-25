# Event 006 formable scripted-localisation registry merge handoff

Date: 2026-08-25

## Scope and outcome

This source-layout pass reduces two formable-family scripted-localisation parser files to zero by moving their complete executable units into the existing Event 006 scripted-localisation registry.

The receiver is `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`.

The moved files are `common/scripted_localisation/006_independence_wave_form03_scripted_localisation.txt` and `common/scripted_localisation/006_independence_wave_formable_registry_scripted_localisation.txt`.

The two source files are removed after their complete executable `defined_text` units are preserved below explicit source markers in the receiver. Redundant source header banners are condensed to keep the registry smaller. No scripted-localisation identifier, branch order, trigger, scope, localisation key, fallback, gameplay effect, decision, event, focus, or package-admission gate is changed.

## Moved selector inventory

FORM-03 lifecycle selectors:

- `GetIndependenceWaveForm03AccommodationBand`
- `GetIndependenceWaveForm03IntegrationBand`
- `GetIndependenceWaveForm03PhaseText`
- `GetIndependenceWaveForm03LanguageModelText`
- `GetIndependenceWaveForm03MemberStatusText`
- `GetIndependenceWaveForm03OutcomeText`

Shared formable-family selectors:

- `GetIndependenceWaveSelectedFormableName`
- `GetIndependenceWaveSelectedFormableMethodName`
- `GetIndependenceWaveSelectedFormableConsentRuleName`
- `GetIndependenceWaveFormableCommitCostText`

The receiver has 34 unique `defined_text` names. Together with the separate focus, GUI, and scenario registries, the Event 006 scripted-localisation surface has 58 unique names with no duplicates.

## Preservation evidence

Each removed file's executable section was appended after its source marker. Normalized comparison of the marker-delimited executable receiver sections against the `HEAD` versions of the removed files returned an exact match for both files; only comment-only header banners were condensed.

The receiver remains a single `defined_text` registry with the original Event 006 blocks followed by the FORM-03 and shared formable blocks in source-file order. The source markers are comments only and do not introduce parser keys.

## Static validation

- Removed parser files: 2.
- Moved `defined_text` blocks: 10.
- Receiver unique names: 34.
- Event 006 unique names across the remaining four scripted-localisation files: 58.
- Duplicate names across those files: 0.
- Removed-section normalized executable comparisons: 2/2 exact.
- Source bytes across the three former files: 60,599; receiver bytes: 59,866; saved: 733.
- Source lines across the three former files: 1,357; receiver lines: 1,345; saved: 12.
- Receiver brace count: checked balanced after the merge.
- No gameplay or package-admission source was changed.

This is source-layout evidence only. No live HOI4 parser, event, decision, GUI, or runtime claim is made by this handoff.
