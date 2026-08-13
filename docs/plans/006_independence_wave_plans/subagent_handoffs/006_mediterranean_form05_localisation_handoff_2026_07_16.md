# Event 006 Mediterranean and FORM-05 Localisation Handoff

Date: 2026-07-16

Mode: patch

## Ownership and result

This pass owns the final English localisation for IW-017 Corsica, IW-018 Sardinia, IW-019 Sicily, and FORM-05 Mediterranean Island League. It does not change gameplay script, identity registration, interface wiring, or assets.

The in-scope player-facing surface is fully localised. No placeholder prose, implementation-history wording, setup-attestation language, or visual claims for adviser records were introduced.

## Files changed

- `localisation/english/006_independence_wave_mediterranean_l_english.yml`
  - New file with 308 localisation keys.
  - Covers package characters, adviser descriptions, founding and route parties, package values, 19 Mediterranean national spirits, three decision categories, 29 missions and decisions, their descriptions and effect summaries, 19 package focuses with descriptions and completion summaries, events `chaosx.nr6.21` through `.27`, and 17 AI strategy-plan labels.
- `localisation/english/006_independence_wave_form05_l_english.yml`
  - Expanded to 125 localisation keys.
  - Covers the full MIX identity, charter ledger and scripted-localisation outputs, charter values, founding and post-formation missions and decisions, exact dynamic costs and effects, three FORM-05 national spirits, events `chaosx.nr6.28` through `.34`, and the first maritime-board completion and failure states.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_mediterranean_form05_localisation_handoff_2026_07_16.md`
  - This handoff.

Both localisation files are UTF-8 with BOM, use unversioned keys, and keep every definition flush left under `l_english:`.

## Content coverage

### Countries, parties, and characters

- ARX and ASX retain their complete canonical base, definite, adjective, and four-ideology identity sets in `006_independence_wave_countries_l_english.yml`.
- MIX retains a complete base, definite, adjective, and four-ideology identity set in the FORM-05 file.
- COR receives only Event 006 party and character localisation. Its vanilla country identity is deliberately not overwritten.
- All 14 character name keys used by the Mediterranean character file are present:
  - Corsica: Petru Santucci, Pasquale Venturi, Paolo Pietri, and Antone Rocchi.
  - Sardinia: Antioco Melis, Vittorio Pala, Gavino Piras, Michele Corda, and Efisio Satta.
  - Sicily: Sebastiano Restivo, Vincenzo Lanza, Salvatore Licata, Giuseppe Lo Giudice, and Leone Messina.
- These identities follow the tranche's all-male character contract.
- The six political adviser descriptions discuss their offices and policies only. They do not imply portraits, icons, dossiers, or other visual assets.
- Every founding and route-specific `set_party_name` token has both a short and long name.

### Decisions, missions, and FORM-05 progression

- The three island categories display their live package values and explain the consequences of interrupted work.
- All 29 Mediterranean missions and decisions have final names and descriptions.
- Every Mediterranean custom effect tooltip is defined, including failure, administrative, diplomatic, security, government, and congress outcomes.
- FORM-05 includes its founding charter mission, invitation choices, three charter projects, congress-seat choice, proclamation, recovery, and all associated dynamic cost and effect text.
- The post-formation first maritime board is fully covered:
  - `independence_wave_form05_complete_first_maritime_board`
  - `independence_wave_form05_establish_common_shipping_board`
  - `independence_wave_form05_link_coastal_warning_stations`
  - `independence_wave_form05_open_customs_clearinghouse`
  - `independence_wave_form05_ratify_first_maritime_board`
  - `independence_wave_form05_reconvene_first_maritime_board`
- The category ledger uses the full 0 to 100 article scale. Its description distinguishes the founding threshold from the post-proclamation completion threshold.
- The three first-board project summaries match the live effects exactly:
  - Shipping board: primary Shipping Guarantees gain and secondary Customs Union gain.
  - Warning chain: primary Common Defense gain and secondary Shipping Guarantees gain.
  - Customs clearinghouse: primary Customs Union gain and secondary Common Defense gain.
- Events `.32`, `.33`, and `.34` communicate the opening priority tradeoff, full first-board ratification, and failed-session recovery choices.

### Focuses, incidents, and strategy labels

- The five-focus COR full-framework extension, six ARX package focuses, and eight ASX package focuses each have a final name, description, and completion summary aligned to the live scripted effect.
- Events `.21` through `.27` have titles, descriptions, both available options, and every referenced custom effect tooltip.
- Events `.28` through `.34` have every referenced title, description, option, and completion tooltip.
- All 17 top-level plans in `common/ai_strategy/006_independence_wave_mediterranean.txt` have readable labels.
- No additional player-facing localisation consumer was found in the current relevant interface files. Their Mediterranean and FORM-05 identifiers are sprite consumers rather than text keys.

## Reference audit

The audit inventory was derived from the live Mediterranean and FORM-05 decisions, categories, events, focuses, characters, ideas, scripted effects, scripted localisation, AI strategies, country identities, and shared cost and trait consumers.

- Expected localisation keys: 482
- Defined keys: 482
- Missing keys: 0
- Duplicate definitions among expected keys: 0

The two owned files supply 433 definitions. The remaining 49 expected definitions resolve through canonical shared files:

- 30 ARX and ASX country identity keys in `localisation/english/006_independence_wave_countries_l_english.yml`.
- Six shared decision cost labels in `localisation/english/006_independence_wave_decisions_l_english.yml`.
- Ten shared adviser trait names and descriptions in `localisation/english/006_independence_wave_nwe_advisors_l_english.yml`.
- Two Mediterranean focus scripted-localisation labels in `localisation/english/006_independence_wave_focus_l_english.yml`.
- One Mediterranean formable-family name in `localisation/english/006_independence_wave_formable_registry_l_english.yml`.

Vanilla supplies the intentionally untouched COR identity in `Hearts of Iron IV/localisation/english/countries_l_english.yml`, including `COR`, `COR_DEF`, `COR_ADJ`, and the four ideology names and definite forms. This pass adds no competing COR base-country keys.

No unresolved external or vanilla localisation reference remains in scope.

## Sources and implementation guidance used

- Repo skills: `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
- Offline wiki core pages required by `AGENTS.md`, plus National Focus Modding and Country Creation.
- Vanilla script-concept and localisation formatter and object documentation, with vanilla country, character, idea, decision, focus, and event localisation examples.
- Current Event 006 Mediterranean and FORM-05 gameplay, history, interface, and documentation files.

## Simplifications, omissions, and blockers

None within the assigned localisation surface. The shared and vanilla definitions listed above remain single-sourced intentionally and were verified rather than duplicated.
