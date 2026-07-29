# Event 016 localisation runtime audit handoff

## Scope

Audited the current Event 016/KRG localisation files, Event 016 event/decision/focus/idea/character/country/cosmetic-tag/special-project/technology/unit/equipment/achievement/super-event references, the two Event 016 scripted-localisation files, and the shared Event Log selectors that consume Event 016 names, evolution text, event details, and world-end ownership text.

## Patch applied

- `common/decisions/016_brilliant_scientist_foreign_decisions.txt`
  - Changed the foreign-operation protection completion tooltip reference from `brilliant_scientist_foreign_protection_effect_tt` to `brilliant_scientist_foreign_offer_protection_effect_tt`.
- `localisation/english/016_brilliant_scientist_foreign_l_english.yml`
  - Renamed the foreign-operation tooltip key to `brilliant_scientist_foreign_offer_protection_effect_tt`.

Before the patch, `brilliant_scientist_foreign_protection_effect_tt` was defined twice with different text. The foreign-operation text described the host's full/limited/refusal response, while the Directorate text described the selected partner's Mandate, Dependence, Exposure, and Project Capacity changes. Localisation load order could therefore show the wrong tooltip in either decision surface. After the patch, the foreign operation and Directorate framework each resolve to a unique key.

## Audit results

### Missing key list

None found in the audited Event 016 surfaces. A source-reference scan over Event 016/KRG code found 597 explicit tooltip, title, text, and `localization_key` references with zero missing global localisation keys. Focus IDs (100), decision IDs (312), Event 016 achievement IDs (17), character/leader/scientist-trait IDs, special-project identifiers, project-force sub-units, equipment, technologies, Event Log event-detail/evolution selectors, and super-event text all resolve.

### Duplicate key list

The only Event 016 duplicate was `brilliant_scientist_foreign_protection_effect_tt`. It is removed by the rename above. No Event 016/KRG duplicate remains in the global localisation key scan.

### Scripted-localisation issue list

None found. `GetBrilliantScientist*` and `GetBrilliantScientistForeignProjectName` call sites all have definitions. Their non-GFX `localization_key` outputs all resolve. Event Log selectors for `brilliant_scientist.evolution.type`, evolution stages 1-4, evolution summary, and `chaosx.events_log.window.event_details.brilliant_scientist` all resolve.

### Dynamic text opportunities

No runtime blocker required a new scripted-localisation helper. Existing dynamic values and scopes are wired for the current surfaces, including Directorate measures, GUI status getters, foreign actor/operation targets, containment recipient, former-host target, and KRG foreign-integration targets. No malformed or unbalanced bracket tokens were found in the Event 016 localisation set.

### Cross-surface mismatch notes

- Event 016 achievement names and descriptions correctly live in the shared `localisation/english/chaosx_achievements_l_english.yml`; `016_brilliant_scientist_achievements_l_english.yml` contains the provenance-investigation decision surface. This split is intentional but easy to overlook during future audits.
- The Directorate foreign-protection effect tooltip and foreign-operation protection tooltip now have separate keys and meanings.
- Event name `chaosx.event_name.16`, evolution selectors, event-details body, public world-end ownership selectors, and super-event keys are aligned. No wording change was made.

### File encoding concerns

All 15 `localisation/english/016_*.yml` files are UTF-8 with BOM. The edited foreign localisation file retained its BOM. No `:0` keys or leading-space localisation keys were found in the Event 016 set or the shared event-name/GUI localisation files checked.

## Validation

- Re-ran global localisation key extraction and duplicate detection after the patch: no Event 016/KRG duplicate keys remain.
- Re-ran explicit Event 016/KRG source-reference coverage: 597 references, zero missing localisation keys.
- Checked all Event 016 YAML BOMs, `:0` key forms, leading-space keys, and bracket balance/dynamic token shape.

Skipped live game, GUI rendering, and in-game localisation validation because agents must not launch HOI4; those checks remain parent-owned/user-owned. No spreadsheet was edited.

## Unresolved wording decisions

None. No new flavour text or mechanic text was introduced.

## Follow-up for parent

Review the two-key rename in the foreign-operation decision and preserve the unique key when reconciling concurrent Event 016 changes. No broader localisation or scripted-localisation patch is required from this audit.
