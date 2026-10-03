# Event 027 live index-filter repair

Disposition: source repair implemented, post-repair live startup evidence pending.
Acceptance basis: the user's live QA direction requires removing the rejected `add_mastery.index` field and retaining exactly one track target in every grant.
This handoff supersedes the native-filter spelling conclusions in `parent_native_repairs_2026-10-03.md` and the corresponding earlier source-audit recommendation.

## Observed defect

The orchestrating live QA session reports HOI4 v1.19.2.0 rejects `index` inside `add_mastery` with `Invalid effect 'index'` and `Unknown effect-type: index`.
The supplied evidence is `docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log`.
The archived file contains 428 matching rejection lines from repeated loading, corresponding to two messages for each of 107 source grants per load.
All matching errors for this native adapter file name the rejected field.

Installed `documentation/effects_documentation.md:1477-1504` and the offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:2508-2542` document an optional `index` filter.
The supplied live parser result takes precedence for this installed game.
Neither `index` nor `track_index` is used inside any Event 027 `add_mastery` block after the repair.
The separate supported numeric `track` argument in `set_sub_doctrine` is retained.

## Target uniqueness

Each mastery grant retains explicit `folder`, `sub_doctrine`, and track-type filters.
The transaction caller revalidates its active Grand Doctrine before invoking the grant.
Every installed Grand Doctrine in the applicable folder has exactly one occurrence of each filtered track type.
The per-grant source crosswalk is `docs/plans/027_doctrine_research_plans/live_qa_filter_uniqueness_2026-10-03.json`.

| Domain | Native grants | Maximum matching tracks |
| --- | --- | --- |
| Army | 36 | 1 |
| Chaos Warfare | 4 | 1 |
| Navy | 26 | 1 |
| Air | 25 | 1 |
| Special Forces | 16 | 1 |

Special Forces subdoctrines can appear in both tracks, but the two track types are distinct identifiers: `special_forces_first` and `special_forces_second`.
Filtering by the owning track type therefore selects one track even when the subdoctrine name is reused.
No installed Grand Doctrine repeats the same track type within its folder, so this graph needs no additional target-disambiguation mechanism.
This verifies grant targeting under the installed graph and does not resolve the separate Special Forces mastery-level readback ambiguity.

The installed source parser reported `SOURCE_UNCLOSED_BLOCK` for the vanilla `long_range_submarines` definition at `common/doctrines/subdoctrines/sea/navy_submarine_doctrines.txt:297`.
Its explicit `track = submarines` header was also read directly.
That parser diagnostic remains recorded in the JSON evidence and is not treated as executed native behavior.
All owning Grand Doctrine track lists and the repaired Event 027 adapter source parsed for this targeting crosswalk.

## Scope and validation limits

The completed repair removes the unsupported native grant filter and adds a comment recording the engine/documentation discrepancy.
It does not change amounts, selected domains, eligible branches, mastery readback, assignment indexes, batch sizes, AI weights, or banked-mastery handling.
The parent retains other in-progress Event 027 source work separately when committing this repair through the shared-tree workflow.

The native targeting crosswalk covers all 107 grants.
No game was launched by this task.
A clean post-repair startup log, native banked-mastery observations, and complete Event 027 acceptance evidence remain pending from the live QA workflow.
The full event is not declared complete by this startup repair.
