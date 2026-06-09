# Parent Tranche: Release Pacing and Focus Branch Cleanup

Date: 2026-06-04

## Scope

- Reduced Soviet Collapse progressive release bursts so republics no longer spill out in large immediate batches.
- Kept the opening release wave on base republic candidates by removing the dynamic any-releasable pool from first-wave helpers.
- Removed a low-value four-way CFR construction-priority mutual exclusion row.
- Separated several Ukraine focus coordinates across military, socialist/political, foreign, and expansion lanes.
- Added a concrete Far Eastern Republic Japan-facing focus interaction.

## Files Changed

- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/opinion_modifiers/chaosx_opinion_modifiers.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Behavior

- Calm-world opening release remains limited to the base republic candidate lists.
- Gathering Storm and higher chaos can still release niche/internal Soviet republics, but through progressive follow-on checks rather than the first wave.
- Custom pressure successors remain excluded from the generic dynamic union release candidate pool and still use their pressure-successor gate.
- Follow-on release constants now produce small staged batches instead of bulk loops across most of the candidate pool.
- CFR construction priorities are no longer mutually exclusive, so cities, rails, factories, and contracts are separate construction tools rather than a red-line lock.
- FEV `FEV_pacific_observer_missions` now improves Japan-facing relations if Japan exists, adds convoys and fuel, and runs foreign-channel logic.

## Validation

- Brace balance checked clean for touched script/focus/opinion files.
- `rg "<=|>="` returned no matches in touched script/focus/opinion files.
- `git diff --check` passed for touched files.
- UTF-8 BOM confirmed preserved for `005_soviet_collapse_custom_countries_l_english.yml`.
- Corrected focus-coordinate audit found no duplicate coordinates in the Soviet Collapse focus files after edits.

## Remaining Risks

- The broader focus-tree rework is not complete. Many trees still have tight focus spacing and generic helper-heavy rewards.
- Ukraine is improved but still has dense political/endgame sections that need another visual pass.
- The release pacing is script-validated, but in-game timing still needs user verification against the intended chaos-tier feel.
