# Event 006 scenario localization clarity handoff

Date: 2026-08-28.

Owner: parent Event 006 implementation agent.

Scope: player-facing wording for the post-launch Event 006 scenario summary and unavailable-movement record.

The scenario launch-status strings no longer expose the SCN-008 identifier, transaction barrier, or release-plan ownership. The summary now describes movements turned away and movements without a safe homeland, and its failed action says that the coordinated release did not begin.

The unavailable-movement record now uses a plain-language title, shows the movement name without a country tag or internal package identifier, and describes the record as fixed when the incident began. Rejection reasons now describe countries, homelands, living borders, former hosts, and safety reviews rather than assigned tags, scopes, arrays, or internal package terminology.

Changed files:

- `localisation/english/006_independence_wave_scenario_l_english.yml`

The localization file retains UTF-8 BOM encoding and all existing keys and scripted-localization selectors. No trigger, effect, decision, category, cost, AI weight, scenario counter, ledger array, admission gate, or pre-event surface changed. The unused package-id selector definitions remain for compatibility, but are no longer displayed by the unavailable-movement description.

Focused review confirms the scenario localization retains every referenced key, preserves all dynamic counters and scripted getters, and removes the player-facing `SCN-008`, transaction-barrier, assigned-tag, scope, and aligned-array wording from the active summary and unavailable-movement text.

The allocator, country API, strict flag-family, FORM-16, and SCN-008 static matrix audits remain the required Event 006 evidence and continue to preserve the 32/29/40/161 boundary and 3/4/5/7/10 ladder. No MCP visual or runtime claim is made because Event inspect/render remain blocked by `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero artifacts.

No fallback or simplification was promoted.
