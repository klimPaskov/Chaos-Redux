# Event005 Parent Tranche: Evolution Details, Dynamic Patron Menu, Focus Audit Status

## Scope

This tranche covered the current blockers around Soviet Collapse evolution preview wiring, dynamic foreign patron menu visibility, and focus-tree cleanup status. Flags were explicitly out of scope and were not touched.

## Files touched by this tranche

- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- Existing Event005 focus/script/localisation files already had broader in-progress edits from the current Event005 cleanup stream.

## Implemented

- Confirmed Event005 now registers five evolution previews:
  - Gathering Storm
  - Rising Chaos
  - Chaos Tier
  - Terminal Rupture
  - High-Chaos Successor Mutation
- Removed the extra high-chaos/world-collapse preview path by wiring the high-chaos preview to the combined high-chaos successor mutation entry.
- Set the Soviet Collapse world-collapse event-log tier to `4`, matching the spreadsheet's Terminal Rupture stage instead of creating a second world-collapse-style stage.
- Hardened the foreign patron expanded menu:
  - `Show decisions for [breakaway]` remains hidden once that target is selected.
  - `Hide decisions for [breakaway]` remains available for the selected target.
  - All foreign patron intervention decisions now include the root-side selected-target trigger in their target trigger bypass, so selected breakaways such as Tajikistan are not dependent only on the target country flag scope during UI refresh.

## Validation

- Event005 evolution preview count check: `5`.
- Soviet Collapse evolution localisation duplicate check: `0` duplicate keys.
- Brace-balance checks passed for touched Event005 decision, focus, scripted effect, script constant, settings, and localisation files.
- `git diff --check` passed for the touched Event005 files.
- Unsupported operator scan for `<=` / `>=` returned no matches in the touched Event005 files.
- `gfx/flags` diff/status check returned no output. No flag files were touched.

## Focus Audit Status

- Per-focus-tree geometry audit found no duplicate coordinates and no focus-between-mutual-exclusive cases in the checked Event005 focus trees.
- The initial cross-file geometry audit overcounted because multiple separate focus trees reuse the same coordinate grid inside shared files.
- The remaining "nonreciprocal mutual exclusivity" findings were parser false positives caused by multi-line `mutually_exclusive` blocks; manual inspection showed the reported groups are reciprocal.

## Remaining Risk

- Focus rewards still need a deeper content pass in custom splinter trees. The focus files no longer show direct idea spam in the audited files, but several chaos splinter trees still repeat low-impact support equipment, anti-air, infrastructure, and similar small rewards. This is a content-quality issue, not a load/syntax issue.
- The repository worktree contains broad unrelated Event006 and older Event005 changes. A clean commit should only be made after isolating the current Event005 tranche or finishing the broader Event005 cleanup goal.
