# Event 12 localisation release-candidate audit

Date: 2026-07-29.

Scope: Event 12 player-facing localisation and scripted localisation only.

## Result

The audit found and corrected a mechanical scripted-localisation keyword issue in the three Event 12 scripted-localisation files.

The offline Paradox localisation reference specifies `localization_key` with the American spelling, and vanilla plus Kaiserreich scripted-localisation examples use that spelling consistently.

Before the patch, all 1,134 Event 12 `defined_text` branches used `localisation_key`; after the patch, all 1,134 branches use `localization_key`.

This is an engine-facing syntax correction rather than a wording change, so no player-facing localisation keys were added, removed, or renamed.

## Changed files and keys

- `common/scripted_localisation/012_africa_charter_gui_scripted_localisation.txt` changed 96 keyword occurrences from `localisation_key` to `localization_key`.
- `common/scripted_localisation/012_africa_priority_member_scripted_localisation.txt` changed 204 keyword occurrences from `localisation_key` to `localization_key`.
- `common/scripted_localisation/012_africa_scripted_localisation.txt` changed 834 keyword occurrences from `localisation_key` to `localization_key`.
- No Event 12 `.yml` file changed, and no localisation key changed.

## Audit lists

### Missing keys

No missing references were found in the Event 12 audit surface.

The checks resolved 205 event text references, 402 focus IDs and descriptions, 80 idea IDs and descriptions, 65 decision text references, 17 decision-category IDs and descriptions, 906 unique scripted-localisation keys, and all current Event 12 cosmetic-country name, adjective, and definition keys.

The 3,294 Event 12 English localisation keys were also checked for global duplicate collisions against the repository English localisation tree; none were found.

### Duplicate keys

No duplicate key was found within the ten Event 12 English localisation files or across the repository English localisation tree.

### Scripted-localisation issues

The only confirmed issue was the British `localisation_key` spelling in all three Event 12 scripted-localisation files.

After the patch, the three files contain zero `localisation_key` occurrences and 1,134 `localization_key` occurrences, and all 906 unique referenced localisation keys resolve to Event 12 English keys.

The custom scripted-localisation method names referenced by Event 12 localisation were checked against the three Event 12 scripted-localisation files; no unknown method name was found.

### Dynamic text opportunities

Event 12 already uses dynamic variables, array scopes, event targets, actor names, state names, route names, timers, and action-result methods in the audited surfaces.

No additional dynamic localisation was required for a narrow release-candidate text audit.

### Cross-surface mismatch notes

No stale `institutional_council` references remain in the audited Event 12 runtime surface after the current sovereign-character rename.

All sixteen current priority-member character names resolve to the current localisation keys in the parent-owned character localisation change.

No confirmed raw technical country tags, implementation identifiers, or `africa_absurd` flavour identifiers were found in Event 12 player-facing localisation.

The exact sensitivity-protocol strings `qaama saalaa koo xuuxaa` and `haadha kee waliin wal qunnamtii saalaa raawwadhe` are absent from runtime localisation and technical identifiers.

They were intentionally not added because the parent task prohibits source-language names and native-speaker review is still pending; they remain an unresolved content decision rather than a safe mechanical localisation fix.

### File encoding concerns

All ten Event 12 English `.yml` files were confirmed UTF-8 with BOM, with no malformed single-line key/value candidates in the audited files.

The three Event 12 scripted-localisation files remain UTF-8 without BOM, matching their pre-existing text-file encoding; the patch did not change their encoding or line content outside the keyword correction.

## Validation

The task-specific checks were rerun after the patch for Event 12 key extraction, scripted-localisation reference resolution, keyword spelling counts, UTF-8 BOM state, and `git diff --check` on the three changed files.

No Hearts of Iron IV executable or live save was launched because repository instructions reserve live gameplay validation for the user.

## Unresolved wording decisions

The two required Afaan Oromoo flavour strings remain absent pending native-speaker review and an accepted design decision about their fictional ruler, regnal, court, council, or title placement.

No broad wording rewrite, translation, new source-language name, or unrelated-event localisation change was made.

## Final release-candidate pass

Date: 2026-07-29, after the natural-disaster wording, sovereign portrait/title migration, Scramble close text, and `localization_key` correction landed in the shared worktree.

The only additional confirmed defect was a duplicated article in `africa_open_scramble_page_desc` in `localisation/english/012_african_union_l_english.yml`.

The key now reads `Bring the scramble response docket before the Charter League.` instead of `Bring the the scramble response docket before the Charter League.`

The latest Event 12 English localisation surface contains 3,299 unique keys across ten UTF-8-with-BOM `.yml` files, with zero duplicate keys, zero malformed key/value lines, and zero collisions against the repository English localisation tree.

The final reference audit found zero missing keys across 205 event references, 804 focus references, 160 idea references, 72 decision references, 34 decision-category references, 908 scripted-localisation references, and 63 Charter GUI text or tooltip references.

All three Event 12 scripted-localisation files have matching `defined_text`, `name`, `text`, and `localization_key` branch counts, balanced braces, zero British `localisation_key` tokens, zero duplicate defined-text names, and zero unknown custom method names in Event 12 localisation tokens.

The natural-disaster acceptance and rejection wording matches the current action contract: the accepted branch is emitted only for a full action whose hostile call is accepted, while the rejected branch is emitted only for a full action whose call rebounds and starts the caller cooldown.

The Scramble close keys are wired to the close-docket decision and its completion effect; the text accurately describes settling the response while deferring external continent-package and world-order powers.

All sixteen current sovereign character IDs have resolving localisation keys, and no obsolete `institutional_council` character, portrait, or title reference remains in the Event 12 runtime or English localisation surface.

The remaining `council` strings are current party or institutional names and are not sovereign titles.

No raw country tag or Event 12 technical identifier was found in player-facing values outside dynamic localisation brackets; the only non-bracket technical-looking values are existing resource icon markers in the RSA cost strings.

The exact sensitivity-protocol Afaan Oromoo strings remain absent by design because source-language names are prohibited in the current parent scope and native-speaker review is pending.

Live Hearts of Iron IV parsing and in-game display checks were skipped because repository instructions reserve executable validation for the user.
