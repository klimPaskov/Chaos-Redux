# Event005 Parent Tranche: DSC Field-Hospital Decision Link

## Scope

Parent patch for the Soviet Collapse focus-depth goal. Flags were not touched.

## Files changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Identifiers changed

- `DSC_field_hospital_memorials`
- `dsc_register_field_hospital_columns`
- `dsc_register_field_hospital_columns_tt`
- `dsc_field_hospital_memorials_tt`

## Behavior before

`DSC_field_hospital_memorials` exposed a mixed reward list directly on the focus: political power, manpower, support equipment, recognition variables, institution variables, and a military consolidation helper. It did not unlock a field-hospital-specific action.

## Behavior after

`DSC_field_hospital_memorials` now presents one readable tooltip and hides the implementation payload. It unlocks `dsc_register_field_hospital_columns`, a recurring DSC decision that mobilizes a field-hospital column package, adds support stores, improves DSC roll-call and mobilization variables, fortifies a controlled roll-call post, and uses existing custom-splinter mobilization mechanics instead of adding a new national spirit.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/decisions/005_soviet_collapse_decisions.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt common/decisions/005_soviet_collapse_decisions.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `python3` brace balance check returned level `0` for all three touched files.
- Localisation BOM check returned `efbbbf`.

## Remaining gaps

This is one bounded route-depth tranche, not a full focus-tree rework. Remaining focus-depth gaps include other visible reward dumps, shallow chaos-country branches, broader layout/pathline review, evolution-detail alignment, and terminal release/scenario verification.
