# Event 016 Event 019 provider-extension localisation audit

Date: 2026-08-03

## Scope

This read-only audit covers the Event 016 provider-extension surface in `common/ideas/016_brilliant_scientist_project_force_ideas.txt`, `localisation/english/019_infrantry_spawn_l_english.yml`, and the matching references in `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`. The portal-raider provider is 509 and the temporal-guard provider is 510. No gameplay, scripted-localisation, asset, or model file was edited.

## Exact-key and missing-key audit

- `brilliant_scientist_event19_portal_host` is declared once in the ideas file at line 57, added once by the public-package dispatcher at line 1261, removed once by the public-additions cleanup at line 1367, and has one name key plus one `_desc` key at localisation lines 1630-1631.
- `brilliant_scientist_event19_temporal_host` is declared once in the ideas file at line 63, added once by the public-package dispatcher at line 1265, removed once by the public-additions cleanup at line 1368, and has one name key plus one `_desc` key at localisation lines 1632-1633.
- All 16 idea IDs declared in the Event 016 ideas file have matching name and `_desc` keys in the English localisation tree.
- The two event IDs fired by the scoped provider effect, `chaosx.nr19.918` and `chaosx.nr19.919`, have title, description, and option `a` keys. No missing key was found in this reference path.
- The exact scoped names are collision-free. A scan of the target localisation file found 2,908 parsed keys and zero duplicate definitions. A scan of the complete English localisation tree also found zero duplicate definitions, including the new keys.

## Scripted-localisation issue list

- No broken scripted-localisation reference is emitted directly by the scoped provider effect. It only dispatches the two Event 019 report events and the provider idea IDs listed above, all of which resolve.
- The existing Event 019 family-name selectors in `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt` do not map family IDs 509 or 510. Because both provider rows explicitly use visual profile 999, the selectors intentionally fall back to `infantry_spawn_family_name_unrecorded` and the neutral reception picture. This matches the Event 019 external-provider contract, which forbids a family or picture map for profile 999. It is a display opportunity, not a missing-key defect in this scoped change.

## Dynamic text opportunities

- If the owner later wants portal and temporal hosts named in the reception popup or Muster Board, add provider-specific family-name selectors and localisation in the Event 019 scripted-localisation surface. That would require an explicit design change to the profile-999 neutral-provider contract and is outside this audit scope.
- Event 019 reports 918 and 919 remain intentionally provider-neutral. Their generic wording does not reveal the portal or temporal route, while generated division-template names in the provider effect already identify `Portal Raider Formation` and `Temporal Guard Formation`. No dynamic change is required for the current contract.

## Cross-surface mismatch notes

- The new receipt names match the provider family constants and the generated template names. `Portal Raider` aligns with `chaos_unit_family_event16_portal_raider` and `kruger_portal_raider`; `Temporal Guard` aligns with `chaos_unit_family_event16_temporal_guard` and `kruger_temporal_guard`.
- The descriptions state that the receipt does not restore the Event 016 parent identity. This matches `brilliant_scientist_event19_install_project_force_public_package`, which adds only the provider-owned host idea and route variable without invoking Event 016 parent setup.
- The description wording is inherited from the five existing receipts and uses implementation-facing phrases such as `provider-owned receipt` and `Event 016 parent identity`. The ideas are `visible = no`, so this is not a runtime-facing leak under the current implementation. If hidden ideas can be surfaced by a future UI or debug view, rewrite all seven receipt descriptions together rather than changing only portal and temporal.
- `Temporal Guard Host Receipt` is a short route label, while the native equipment/unit localisation uses `Temporal Continuity Guard`. Decide whether to retain the concise route label or expand the receipt name for strict cross-surface naming consistency. No gameplay identifier depends on the display choice.

## File encoding concerns

- `localisation/english/019_infrantry_spawn_l_english.yml` begins with the required UTF-8 BOM (`EF BB BF`) and `l_english:` header. The new values are single-line UTF-8 strings with valid ASCII keys, no `:0` suffix, no em dash, and no semicolon.
- The working copy of the localisation file contains mixed line endings (3,185 CRLF records and 59 LF-only records). Git still presents only the four provider additions, and the BOM is intact. Avoid a broad line-ending rewrite in this scoped change. The ideas and scripted-effect files are LF-only Clausewitz source files without a BOM, as expected.

## Validation evidence

- Parsed the target and complete English localisation trees for duplicate keys.
- Cross-checked every Event 016 idea ID against name and `_desc` localisation keys.
- Cross-checked provider idea add/remove references and Event 019 report-event references in the scoped scripted effect.
- Read the offline Localisation, Idea modding, Event modding, Data structures, Triggers, Effects, Modifiers, Scopes, On actions, Decision modding, and AI modding wiki snapshots, plus vanilla `loc_formatter_documentation.md`, `loc_objects_documentation.md`, `effects_documentation.md`, and `triggers_documentation.md`.
- No game launch or in-game validation was performed, per repository rules. No source patch was necessary.

## Recommended fixes

1. Required: none for key coverage, exactness, duplicate safety, or BOM encoding.
2. Optional wording pass: if these hidden receipt ideas may become visible, update all seven `brilliant_scientist_event19_*_host_desc` keys together in `localisation/english/019_infrantry_spawn_l_english.yml` to remove implementation-history phrasing while preserving the provider-isolation meaning.
3. Optional dynamic-label pass: only with owner approval to change the neutral profile-999 contract, add portal/temporal family-name selectors and keys in the Event 019 scripted-localisation surface. Do not add isolated keys to the current file without the selector change.
4. Optional consistency decision: choose between the concise `Temporal Guard Host Receipt` and the native `Temporal Continuity Guard` label. No source edit is recommended until that naming decision is made.

## Changed files and remaining risks

- Source files changed: none.
- Handoff added: this file only.
- No dynamic localisation was added or fixed.
- Remaining risk is limited to the intentional generic fallback label for external profile-999 providers and the hidden-receipt wording noted above. Provider lifecycle and live derivative validation remain parent-owned.
