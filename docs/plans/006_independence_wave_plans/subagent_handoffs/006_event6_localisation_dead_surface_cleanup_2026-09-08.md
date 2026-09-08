# Event 006 localisation dead-surface cleanup

Date: 2026-09-08

## Scope

This bounded cleanup removes localisation and scripted-localisation entries that have no current Event 006 consumer. It also removes player-facing implementation wording from the achievement and scenario rejection messages, and removes raw country tags from rival-bloc member detail text.

## Changes

- Deleted the unreferenced independence_wave_cost_security_standard_factory, _tooltip, and _blocked entries from localisation/english/006_independence_wave_decisions_l_english.yml. The obsolete triplet exposed five resource entries and the Spend/Commit presentation; active decisions use the four-resource independence_wave_cost_security_standard row.
- Deleted the unreferenced GetIndependenceWaveScenarioLedgerPackageId block from common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt and its three unused IW-### localisation keys from localisation/english/006_independence_wave_scenario_l_english.yml.
- Reworded independence_wave_achievement_found_league_tooltip to describe the founding requirement without referring to a congress before the independence event.
- Reworded the living-tag, Event 005 collision, and unbound-current-map scenario rejection messages to describe player-facing outcomes rather than implementation identifiers.
- Removed raw GetTag output from selected and first rival-bloc member detail strings while retaining the dynamic country name and ledger values.

## Validation

Exact repository searches confirm that the deleted cost keys, package-ID keys, and scripted-localisation helper have no remaining executable or localisation callers. The Event 006 localisation audit still resolves 0 missing explicit references, 0 duplicate Event 006 keys, 184 focus title/description pairs, 409 idea title/description pairs, 176 decision/category title/description pairs, 16 achievement triplets, and 58 unique scripted-localisation names. The touched English files retain their UTF-8 BOM.

Focused Event 006 allocator, country API, strict flag, FORM-16, SCN-008, and GUI semantic audits remain green. No gameplay, asset, admission, cost-payment effect, AI weight, or pre-event category/mission/queue surface was added or widened.

## Status

Implemented. The long Iceland, federal-compact, rival-bloc, Ruthenia, Montenegro, and Kosovo ledger displays remain queued for consumer-specific decision/UI review because shortening them without a matching effect audit could conceal real outcomes.
