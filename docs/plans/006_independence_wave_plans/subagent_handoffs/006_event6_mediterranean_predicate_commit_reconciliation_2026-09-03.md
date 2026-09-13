# Event 006 Mediterranean package-predicate commit reconciliation — 2026-09-03

## Result

The current Event 006 authority files contained a stale ownership warning for the COR, ARX, and ASX package predicates. The source requirement was not an unowned working-tree edit: it is present in commit `15405951938acf9e7327892dc54815280fbf001b` (`Bridge Event 021 adapter package predicates`) and remains in the current source at `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt:9-24`.

Each package predicate requires its vanilla carrier tag, the matching Event 006 package id, and `is_independence_wave_package_content_active = yes`. This keeps downstream Mediterranean consumers behind the generation-owned setup receipt and does not add central admission, allocation weight, Join entries, costs, routes, or any pre-event surface.

## Documentation updated

- `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md`
- `docs/specs/006_independence_wave_specs/quality/package_manifest.md`
- `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

The five authority files now cite the committed source change and no longer describe this predicate as an unowned or uncommitted gap. Earlier dated handoffs retain their historical observations and are not rewritten.

## Validation

`git show 15405951938 -- common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt` confirms the three predicate substitutions. A fresh source scan confirms all three predicates still contain `is_independence_wave_package_content_active = yes`, and `git diff --check` is clean for the reconciled documentation files.

No gameplay, asset, localisation, admission, allocator, probability, or spreadsheet source was changed by this reconciliation. The Event 006 boundary remains 32 content-attested packages across 29 compatible groups, 40 adapters, 161 unattested selectable rows, and HOLD / PARTIAL.
