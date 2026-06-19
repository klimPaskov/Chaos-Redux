# Event 012 Localisation/Docs Capstone Parity Audit Handoff

## Scope

- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/specs/012_africa_specs/CURRENT_SOURCE_OF_TRUTH.md`

## Files changed

- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-19_012_africa_localisation_docs_capstone_parity_audit_handoff.md`

## Changed ids and keys

- No localisation keys were changed by this audit.
- Audited focus keys:
  - `AFR_BEST_kinship_boundary_pacts`
  - `AFR_BEST_kinship_boundary_pacts_desc`
  - `AFR_BEST_night_signal_omens`
  - `AFR_BEST_night_signal_omens_desc`
  - `AFR_BEST_terracotta_citadel_terms`
  - `AFR_BEST_terracotta_citadel_terms_desc`
  - `AFR_BEST_bon_gentle_veto_court`
  - `AFR_BEST_bon_gentle_veto_court_desc`
  - `AFR_BEST_hyr_night_broadcasts`
  - `AFR_BEST_hyr_night_broadcasts_desc`
  - `AFR_BEST_bir_verified_wall_warnings`
  - `AFR_BEST_bir_verified_wall_warnings_desc`
  - `AFR_BEST_sao_terracotta_line`
  - `AFR_BEST_sao_terracotta_line_desc`

## Before and after behavior

- Before: The Event 012 foundation doc correctly removed the stale `BON`/`HYR`/`BIR`/`SAO` capstone blocker, but two patch-touched sentences still used update-history phrasing: "These trees now include" and "the current role branches".
- After: The same doc states the companion-tree and AI coverage in present tense: "These trees include" and "the role branches, tag capstones, and tag AI".

## Findings

- Missing keys: none for the seven audited focus ids; every id has both title and `_desc` localisation.
- Duplicate keys: none found in `012_african_union_l_english.yml`.
- Scripted/dynamic localisation issues: none introduced by the new focus keys; the audited keys do not use dynamic scopes, `$...$` nesting, or scripted localisation calls.
- Dynamic text opportunities: none required for this patch; the new focus text is static by design and refers to fixed actor/package concepts.
- Cross-surface mismatches: none found in the scoped docs. Both docs state that `BON`, `HYR`, `BIR`, and `SAO` capstone parity is closed without claiming Event 012 is complete.
- File encoding concerns: none found; the localisation file still begins with UTF-8 BOM bytes `efbbbf`.

## Validation

- Matched each of the seven audited focus ids against `common/national_focus/012_africa_authority_focus.txt` and the localisation title/description keys.
- Checked `012_african_union_l_english.yml` for `:0` entries, duplicate parsed keys, and BOM preservation.
- Checked the scoped docs for stale capstone blocker wording such as "last four high-chaos actors", "still need capstone", and "capstone parity work".

## Skipped validation

- No gameplay-file validation was run beyond read-only focus-id matching, because this audit was scoped to localisation and documentation and did not edit gameplay files.

## Remaining issues

- None for the scoped localisation/docs patch.
