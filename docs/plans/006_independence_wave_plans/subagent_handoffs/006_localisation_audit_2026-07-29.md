# Event 006 localisation audit handoff

Date: 2026-07-29
Scope: the 42 English Event 006 localisation files, their event, decision, focus, category, scripted-localisation, event-log, super-event, achievement, country-tag, character, and interface consumers.
Disposition: PASS for the bounded localisation snapshot after the concurrent cost and GUI tooltip repairs, with whole-event completion still outside this audit.

The audited localisation surface is structurally well covered.
The first scan found nine missing category descriptions and twelve newly added cost bases without tooltip and blocked-state pairs; the nine category descriptions were added by this audit and the twelve cost triplets were added concurrently by the parent before the final scan.
This handoff does not claim whole-event completion because the package adapters remain source-only or overlay-only in their own handoffs and live runtime, portraits, assets, AI, save/load, and final admission evidence remain outside this audit.

## Missing key list

Nine missing category descriptions were added by this audit:

- `independence_wave_iw059_mesopotamia_category_desc` in `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`.
- `independence_wave_iw085_cyrenaica_category_desc` in `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml`.
- `independence_wave_iw101_kongo_category_desc`, `independence_wave_iw102_kuba_category_desc`, and `independence_wave_iw105_loango_category_desc` in `localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml`.
- `independence_wave_iw156_moluccan_category_desc`, `independence_wave_iw196_antilles_category_desc`, `independence_wave_iw197_mapuche_category_desc`, and `independence_wave_iw204_restoration_category_desc` in `localisation/english/006_independence_wave_iw156_iw196_iw197_iw204_overlays_l_english.yml`.

The following 12 `custom_cost_text` bases were missing both the `_tooltip` and `_blocked` keys in the initial expanded-scope scan.

- `independence_wave_iw035_charter_cost` in `localisation/english/006_independence_wave_iw035_livonia_l_english.yml`.
- `independence_wave_iw035_coastal_watch_cost` in `localisation/english/006_independence_wave_iw035_livonia_l_english.yml`.
- `independence_wave_iw035_depot_cost` in `localisation/english/006_independence_wave_iw035_livonia_l_english.yml`.
- `independence_wave_iw035_federal_compact_cost` in `localisation/english/006_independence_wave_iw035_livonia_l_english.yml`.
- `independence_wave_iw059_cabinet_cost` in `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`.
- `independence_wave_iw059_constitutional_cost` in `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`.
- `independence_wave_iw059_depot_cost` in `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`.
- `independence_wave_iw059_officer_cost` in `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`.
- `independence_wave_iw085_assembly_cost` in `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml`.
- `independence_wave_iw085_cavalry_cost` in `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml`.
- `independence_wave_iw085_oasis_cost` in `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml`.
- `independence_wave_iw085_regency_cost` in `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml`.

For each base above, the exact initial gaps were `<base>_tooltip` and `<base>_blocked`.
The parent subsequently added all 24 keys in the IW-035, IW-059, and IW-085 files, and the final scan reports zero missing cost triplets across all 133 custom-cost bases.
Concurrent parent additions for the Dalmatia, Vojvodina, COG, regional overlay, IW-035, IW-059, and IW-085 cost surfaces are observed but are not claimed by this audit.

No missing event title, description, option, focus title or description, decision name or description, category name or description, character name or description, country-tag name or ideology variant, achievement name or description, interface text, or shared event-log/super-event reference was found in the scoped checks.

## Duplicate key list

None in the scoped English Event 006 files.

## Scripted localisation issue list

None found in the 11 Event 006 scripted-localisation files.
The audit resolved 237 `localisation_key` and scripted-localisation text references with zero missing keys and no duplicate scripted-localisation names in the scoped files.
No raw trigger fragments, implementation flags, event-target syntax, or malformed scripted-localisation references were exposed in the audited player-facing strings.

## Dynamic text opportunities

- Keep the 12 parent-added cost triplets synchronized with their existing script constants and payment effects, following the established IW-005 and IW-022 pattern.
- The parent-added IW-035, IW-059, and IW-085 strings currently display literal numeric values in several tooltip and blocked lines even though package-specific constants exist; replace those literals with constant-backed tokens if the owning package code accepts dynamic localisation in those fields.
- The AGX conference description could mention its authorization mandate and Low Countries candidacy gates because those are visible requirements in `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`; this is a gameplay-owner clarity opportunity, not a missing-key failure.
- The existing `implementation program` wording in the Form03 surface could be made more player-facing in a later wording pass, but it is not a broken reference or a new package blocker.
- Scenario ledger words such as `SCN-008`, package identifiers, and registry terms are intentional diagnostic or in-world ledger text in `006_independence_wave_scenario_l_english.yml`; they should not be replaced with generic prose without a connected design decision.

## Cross-surface mismatch notes

- The nine newly added adapter categories now have both names and route-specific descriptions, so category panels no longer fall back to a blank description.
- Previous localisation handoffs reported a complete cost-triplet surface for the earlier 34-file scope; the expanded scan briefly found 12 new gaps, and the parent additions now restore complete triplet coverage for the 42-file scope.
- Event title, description, option, focus, decision, category, scripted-localisation, event-log, event-details, evolution, super-event, achievement, character, country-tag, and interface references resolve in the current English source scan.
- The super-event history string now describes the ordinary wave assembling its release rather than referring to an implementation-level frozen plan.
- New overlay wording no longer exposes `vanilla`, `cosmetic carrier`, `tree`, or `history` implementation terms in player-facing route descriptions; the remaining package and registry vocabulary is confined to intentional scenario-ledger or in-world accounting text.
- The Event 006 package adapters remain partial or overlay-only according to their own handoffs, and the HAW and 6001 rights blockers are not missing localisation keys.

## File encoding concerns

All 42 scoped English Event 006 localisation files begin with a UTF-8 BOM.
The current parser found no duplicate keys, no `:0` keys, no em-dash characters, and no raw malformed section or currency escapes.
One ordinary semicolon is present in the concurrently added `independence_wave_cost_pre_wave_crisis_tooltip` sentence in `localisation/english/006_independence_wave_decisions_l_english.yml`; it is grammatical punctuation and is not an encoding or Clausewitz localisation delimiter issue.
The intentional en-dashes in route names such as `Araucania–Patagonia` remain unchanged.

## Changed files

This audit authored wording or category additions in these ten files:

- `localisation/english/006_independence_wave_ice_l_english.yml`.
- `localisation/english/006_independence_wave_iw022_dalmatia_l_english.yml`.
- `localisation/english/006_independence_wave_iw025_vojvodina_l_english.yml`.
- `localisation/english/006_independence_wave_iw035_livonia_l_english.yml`.
- `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`.
- `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml`.
- `localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml`.
- `localisation/english/006_independence_wave_iw156_iw196_iw197_iw204_overlays_l_english.yml`.
- `localisation/english/006_independence_wave_pacific_l_english.yml`.
- `localisation/english/006_independence_wave_super_event_l_english.yml`.

The authored key changes are the nine category descriptions above plus the Iceland municipal-charter effect tooltip, Dalmatia and Vojvodina category and reserve wording, Livonia category wording, Cyrenaica and COG hold wording, Antilles and Mapuche/Araucania route wording, the Pacific California focus tooltip, and the crisis super-event history description.
Concurrent parent cost additions visible in several of these same files are not attributed to this audit.
The concurrent GUI tooltip repair adds `pdx_tooltip = "independence_wave_status_gui_refresh_tt"` to the refresh button in `interface/006_independence_wave.gui` and adds `independence_wave_status_gui_refresh_tt` to `localisation/english/006_independence_wave_gui_l_english.yml`; those changes are parent-owned and are not attributed to this audit.

## Behavior or display before and after

Before the category additions, the nine new overlay categories exposed their names but had no category description key.
After the additions, each category explains its route-specific institutional and territorial problem in the decision-category panel.
The Iceland effect tooltip now uses a grammatical coordinated list instead of a semicolon splice.
The Dalmatia, Vojvodina, Livonia, Cyrenaica, Kongo, Kuba, Loango, Antilles, Mapuche, and Araucania strings now describe the in-world authority or settlement rather than exposing vanilla or cosmetic implementation terminology.
The Pacific tooltip now describes California's civic-industrial settlement rather than an internal package label.
The crisis super-event history now describes the wave assembling its release rather than an implementation-level frozen plan.
The status refresh button now exposes a player-facing tooltip explaining that it refreshes the visible founding-value ledgers and route panels.

## Meaningful validation

- A PowerShell locale parser scanned 42 Event 006 English YML files and counted 6,182 keys with zero BOM failures and zero duplicate keys after the concurrent cost and GUI additions.
- Event source references resolved 449 namespaced title, description, option, and custom-tooltip references with zero missing keys.
- The 11 scripted-localisation files resolved 237 references with zero missing keys.
- The four focus files resolved 312 focus titles, 312 focus descriptions, and 312 custom effect tooltips with zero missing keys.
- The 28 decision files resolved 394 names and 394 descriptions with zero missing names or descriptions, and their 426 custom effect tooltip references resolved.
- The 28 decision categories resolved 58 category names and 58 category descriptions after the nine additions above.
- Event 006 achievements resolved all 16 names and descriptions, seven Event 006 character files resolved 56 name and description references, 85 named country tags resolved base and ideology variants, and the interface scan resolved 39 text or tooltip references including the repaired refresh-button tooltip.
- Shared event-log, event-details, evolution, scenario, debug, and super-event references resolved 134 scoped localisation references with zero missing keys.
- The final cost scan found 133 custom-cost bases with zero missing `_tooltip` or `_blocked` variants.

## Skipped meaningful validation and why

No Hearts of Iron IV process, live save, or in-game event-log playback was run because repository instructions reserve live consumer validation for the user.
No GUI render or MCP visual comparison was run because this audit changed text keys only and introduced no interface layout or scripted GUI change.
No event catalog workbook update was made because the wording changes are implementation-facing tooltip and category repairs rather than a new event-detail or evolution-detail catalog row.

## Unresolved wording decisions

- The owning package agent should decide whether the newly added IW-035, IW-059, and IW-085 cost strings should replace their literal numbers with the available package constants.
- The AGX conference description may optionally enumerate its authorization and candidacy prerequisites in a separate gameplay-owner pass.
- The Form03 `implementation program` phrase and scenario ledger terminology are retained pending an explicit design decision because changing them could alter route meaning.

## Plan handoff path

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_localisation_audit_2026-07-29.md`
