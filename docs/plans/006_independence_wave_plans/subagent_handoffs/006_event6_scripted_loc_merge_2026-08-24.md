# Event 006 scripted-localisation merge handoff

Date: 2026-08-24

## Scope and outcome

This bounded patch reduced the Event 006 scripted-localisation file count from twelve files to nine files.

Four small Event 006-owned files were concatenated into `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`.

The new registry preserves every original comment, `defined_text` block, identifier, branch order, trigger, scope, localisation key, and fallback in the same source order after newline normalization.

No localisation YAML, gameplay, GFX, decisions, events, interface files, or unrelated dirty files were changed.

## Files changed

Added:

- `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_scripted_loc_merge_2026-08-24.md`

Removed after their complete contents were placed in the registry:

- `common/scripted_localisation/006_independence_wave_crisis_localisation.txt`
- `common/scripted_localisation/006_independence_wave_decision_cost_localisation.txt`
- `common/scripted_localisation/006_independence_wave_decision_scripted_localisation.txt`
- `common/scripted_localisation/006_independence_wave_rival_bloc_scripted_localisation.txt`

## Merged identifiers

The registry contains ten unique top-level `defined_text` identifiers in the following preserved order:

1. `GetIndependenceWaveCrisisHistoryCause`
2. `GetIndependenceWaveCrisisResolution`
3. `GetIndependenceWaveProvisionalCapitalCostText`
4. `GetIndependenceWaveProvisionalCapitalCostBlockedText`
5. `GetIndependenceWaveExpulsionGroundName`
6. `GetIndependenceWaveFormerHostNameDef`
7. `GetIndependenceWaveFormerHostNameDefCap`
8. `GetIndependenceWaveRivalBlocRoute`
9. `GetIndependenceWaveRivalBlocEventDetails`
10. `GetIndependenceWaveRivalBlocEventDetailsMember`

The source-file group order is crisis history, provisional-capital costs, expulsion and former-host selectors, then rival-bloc selectors.

No selector calls another Event 006 selector from inside these scripted-localisation files, so moving the unique definitions to a later single file introduces no cross-file evaluation-order dependency.

Branch order inside each `defined_text` remains unchanged because the original file contents were concatenated as complete units.

## Complete audited identifier inventory

The twelve original files contained 54 top-level definitions and all 54 names were unique.

- Crisis registry: `GetIndependenceWaveCrisisHistoryCause`, `GetIndependenceWaveCrisisResolution`
- Decision-cost registry: `GetIndependenceWaveProvisionalCapitalCostText`, `GetIndependenceWaveProvisionalCapitalCostBlockedText`
- Decision registry: `GetIndependenceWaveExpulsionGroundName`, `GetIndependenceWaveFormerHostNameDef`, `GetIndependenceWaveFormerHostNameDefCap`
- Focus registry: `GetIndependenceWaveTransportFocusTitle`, `GetIndependenceWaveEconomicProgramFocusTitle`, `GetIndependenceWaveMilitaryProgramFocusTitle`, `GetIndependenceWaveAmbitionFocusTitle`, `GetIndependenceWaveFirstPowerCenterFocusTitle`, `GetIndependenceWaveSecondPowerCenterFocusTitle`
- FORM-03 registry: `GetIndependenceWaveForm03AccommodationBand`, `GetIndependenceWaveForm03IntegrationBand`, `GetIndependenceWaveForm03PhaseText`, `GetIndependenceWaveForm03LanguageModelText`, `GetIndependenceWaveForm03MemberStatusText`, `GetIndependenceWaveForm03OutcomeText`
- FORM-05 registry: `GetIndependenceWaveForm05Ledger`, `GetIndependenceWaveForm05CapitalModel`, `GetIndependenceWaveForm05DelegationStatus`
- Formable registry: `GetIndependenceWaveSelectedFormableName`, `GetIndependenceWaveSelectedFormableMethodName`, `GetIndependenceWaveSelectedFormableConsentRuleName`, `GetIndependenceWaveFormableCommitCostText`
- GUI registry: `GetIndependenceWaveLegitimacyBand`, `GetIndependenceWaveRecognitionBand`, `GetIndependenceWaveCapacityBand`, `GetIndependenceWaveSecurityBand`, `GetIndependenceWaveInstabilityBand`, `GetIndependenceWaveFoundingPhase`, `GetIndependenceWaveHostStatus`, `GetIndependenceWavePatronBand`, `GetIndependenceWavePatronName`, `GetIndependenceWaveMissionStatus`
- IW-005 Flanders registry: `GetIndependenceWaveIW005FlandersInstitutionStatus`
- Rival-bloc registry: `GetIndependenceWaveRivalBlocRoute`, `GetIndependenceWaveRivalBlocEventDetails`, `GetIndependenceWaveRivalBlocEventDetailsMember`
- Scenario registry: `GetIndependenceWaveScenarioSummaryOutcome`, `GetIndependenceWaveScenarioLastTypeName`, `GetIndependenceWaveScenarioFailureReason`, `GetIndependenceWaveScenarioLastIntensityName`, `GetIndependenceWaveScenarioTerritoryName`, `GetIndependenceWaveScenarioForceName`, `GetIndependenceWaveScenarioLedgerPackageId`, `GetIndependenceWaveScenarioLedgerReason`
- Core presentation registry: `GetIndependenceWaveLeaguePhase`, `GetIndependenceWavePresentationArmedText`, `GetIndependenceWavePresentationRegionText`, `GetIndependenceWavePresentationHostText`, `GetIndependenceWavePresentationNetworkText`, `GetIndependenceWaveForceTemplateName`

## Files deliberately left separate

- `006_independence_wave_focus_scripted_localisation.txt` remains separate because it is a large focus-owned selector set.
- `006_independence_wave_form03_scripted_localisation.txt` remains separate because it is a large FORM-03 lifecycle registry.
- `006_independence_wave_form05_scripted_localisation.txt` remains separate despite its small size because its three selectors belong to the dedicated FORM-05 lifecycle.
- `006_independence_wave_formable_registry_scripted_localisation.txt` remains separate because it is a large shared formable-family registry.
- `006_independence_wave_gui_scripted_localisation.txt` remains separate because it is a dedicated GUI status registry.
- `006_independence_wave_iw005_flanders_scripted_localisation.txt` remains separate because it is a cross-event IW-005 integration surface with distinct ownership.
- `006_independence_wave_scenario_scripted_localisation.txt` remains separate because it is a large triggerable-scenario registry.
- `006_independence_wave_scripted_localisation.txt` remains separate as the primary wave-summary and force-template registry.

## Encoding and source preservation

All twelve original Event 006 scripted-localisation files were plain UTF-8 without a byte-order mark at audit time.

The eight unmerged source files were not rewritten, so their existing encoding and contents remain untouched.

The new registry is UTF-8 with BOM, with leading bytes `EF BB BF`.

Each of the four removed originals was compared with the registry after normalizing line endings, and all four complete texts were found unchanged inside the registry.

## Static validation

- Final Event 006 file count: nine.
- Final Event 006 top-level definitions: 54 total and 54 unique.
- Definitions in the new registry: ten.
- Duplicate Event 006 definitions: none.
- Duplicate definitions for any Event 006 identifier across all of `common/scripted_localisation`: none.
- Distinct bracketed `GetIndependenceWave*` calls across `common`, `events`, `interface`, and `localisation`: 54.
- Bracketed calls without a definition: none.
- Event 006 definitions without a bracketed call: none.
- Event 006 `localization_key` references: 368 references to 358 unique keys.
- Referenced localisation keys missing from localisation YAML: none.
- New registry top-level assignment type: only `defined_text`.
- New registry brace delta: zero.

## Localisation audit findings

- Missing key list: none found for the 358 unique `localization_key` values referenced by these files.
- Duplicate key list: not applicable to this scripted-localisation-only patch. No YAML key was added or changed.
- Scripted localisation issue list: no duplicate definition, missing call target, changed identifier, changed branch order, or missing localisation target was found by the static checks.
- Dynamic text opportunities: none introduced or removed. All existing variables, constants, scopes, and dynamic country references were preserved.
- Cross-surface mismatch notes: none found in the bracket-call and localisation-key coverage checks.
- File encoding concerns: the twelve original files lacked BOM. The new consolidated registry has BOM, while the eight ownership-sensitive or larger files remain byte untouched for the parent to review separately if repository policy requires an encoding-only pass.
- Prose-quality issues: no player-facing sentence was changed. The merge preserves all existing localisation keys and does not alter vagueness, bloat, obvious explanation, repetition, overcomplication, or style-rule status in YAML consumers.
- Sourced-quotation preservation: no sourced or attributed quotation exists in the inspected scripted-localisation source blocks, and no quote-bearing YAML was edited.

## Before and after behavior

Before the patch, the ten merged selectors were loaded from four separate Event 006 files.

After the patch, the same ten selectors load from one Event 006 registry with unchanged identifiers and unchanged internal selection behavior.

No dynamic localisation was added, removed, or rewritten.

No player-facing prose changed, so there is no before-and-after wording change under vagueness, bloat, obvious explanation, repetition, overcomplication, or style-rule repair.

Dynamic tokens, scopes, constants, formatting behavior, and localisation-key targets were preserved without exception.

## MCP evidence and blocker

The required read-only Event MCP route was attempted with `hoi4.event_inspect` in trace mode for `chaosx.nr6.1` after correcting the selector to `{ kind = event, eventId = chaosx.nr6.1 }`.

The accepted request timed out after 180 seconds with `timed out awaiting tools/call after 180s` and returned no artifact URI or runtime localisation evidence.

Source checks are not treated as equivalent MCP evidence.

The missing MCP artifact is the only skipped meaningful validation for this structural merge.

## Remaining issues and parent follow-up

The parent should review the scoped diff and decide whether the eight untouched no-BOM scripted-localisation files need a separate encoding-only change.

The parent should retry the Event MCP inspection if runtime event-chain evidence is required before its final completion claim.

There are no unresolved wording decisions and no design handoff was required.

No commit was created.
