# Remaining safe cleanup — 2026-08-24

## Scope

This bounded follow-up resolves two candidates that were previously deferred because their owner files had concurrent edits. It changes no gameplay behavior, balance, probability, GUI source, interface layout, asset, spreadsheet, or Event 21+ event-specific implementation.

## Event 5 duplicate localisation removal

Deleted `localisation/english/005_soviet_collapse_custom_splinter_focus_expansion_l_english.yml`.

The deleted file contained 28 localisation keys. All 28 exist in the canonical `localisation/english/005_soviet_collapse_l_english.yml`; 13 values were identical and 15 canonical values contained the current wording. The smaller file had no unique key, no filename consumer, and no documentation or generated-reference role.

The canonical localisation file was not edited by this cleanup. Removing the smaller file eliminates duplicate definitions and leaves the current canonical values authoritative.

## Event 14 stale source comment

Changed the section comment in `common/scripted_effects/014_cannibalism_effects.txt` from the retired filename `014_cannibalism_core_effects.txt` to `Consolidated legacy core section`.

The edit is comment-only. Historical handoffs retain the former filename where it records the source layout at the time of those audits.

## Validation and retained boundaries

Focused localisation parsing confirmed 28/28 replacement keys before deletion. Repository-wide filename search found no consumer of the removed localisation file. The active Event 14 script keeps its concurrent gameplay edits unchanged; only the isolated comment hunk belongs to cleanup.

No current-runtime helper, dynamic reference, meta effect, scripted-localisation method, GFX consumer, or spreadsheet key was removed. No GUI or interface file changed.
