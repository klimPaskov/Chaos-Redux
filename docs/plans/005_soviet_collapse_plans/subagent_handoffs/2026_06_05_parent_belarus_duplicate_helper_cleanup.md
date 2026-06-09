# Event005 Parent Tranche: Belarus Duplicate Helper Cleanup

## Scope

Bounded focus reward cleanup for duplicate shared-helper calls inside Event005 focus rewards. This tranche does not edit flags, assets, or localisation.

## Changed Files

- `common/national_focus/005_soviet_collapse_republics.txt`

## Implementation

- Removed redundant `soviet_collapse_apply_focus_legal_recognition = yes` from `blr_soviet_collapse_national_council_of_minsk`.
- Removed redundant `soviet_collapse_apply_focus_legal_recognition = yes` from `blr_soviet_collapse_council_bargains_with_forests`.
- Both focuses still call `soviet_collapse_apply_focus_republican_compact_plan = yes`, which already includes legal-recognition work through the shared compact helper.
- This prevents the same legal-recognition reward/tooling chain from being applied twice in the same focus while preserving the intended Belarus republican-compact route.

## Mechanical Audit

The parent scan checked these focus files for repeated helper calls and obvious helper nesting overlaps:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

After the patch, the scan reported:

```text
no duplicate helper combos found
```

The same scan also found no direct `add_ideas` calls in those three Event005 focus files.

## Validation

- Brace-balance check passed for `common/national_focus/005_soviet_collapse_republics.txt`.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt` passed.

## Remaining Risks

- This only clears directly duplicated helper calls in focus rewards. It does not prove that all shared helper payloads are deep or country-specific enough.
- Broad focus-tree branch structure, pathline cleanup, and reward-depth work remain incomplete until the current focus-audit subagent and later implementation tranches clear them.
