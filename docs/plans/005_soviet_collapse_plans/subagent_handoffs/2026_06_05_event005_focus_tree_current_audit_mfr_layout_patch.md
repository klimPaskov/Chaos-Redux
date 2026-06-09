# Event005 Focus Tree Current Audit - MFR Layout Patch

## Scope

Audited:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

References read before inspection: `AGENTS.md`, `hoi4-focus-trees`, `chaos-redux-events`, the offline Paradox wiki core pages plus National focus modding, and vanilla documentation under `~/projects/Hearts of Iron IV/documentation`.

## Changed Files

- `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - Moved `MFR_rifles_before_speeches` from `x = 7 y = 10` to `x = 8 y = 10`.
  - Moved `MFR_builders_waste_steel` from `x = 8 y = 10` to `x = 10 y = 10`.

No gfx, flag, or interface files were touched.

## Audit Findings

- Direct `add_ideas` spam: none found in the four requested focus files.
- Duplicate helper calls inside individual focus rewards: none found for `soviet_collapse*` helper calls in the current requested files.
- Repeated helper families remain common by design but are still a readability/play-feel risk:
  - Republic trees repeatedly use `soviet_collapse_apply_focus_depot_and_supply_control`, `soviet_collapse_apply_focus_military_consolidation`, `soviet_collapse_apply_focus_legal_recognition`, and `soviet_collapse_apply_focus_foreign_channel`.
  - Custom splinter trees repeatedly use the same generic focus families plus custom-splinter identity helpers; no single reward duplicated a helper, but many 47-focus trees still share the same skeleton.
  - Ancient restorations are compact and aggressive, but their four trees remain structurally parallel at 16 focuses each.
- Ukraine, Belarus, and Kazakhstan currently have no duplicate focus coordinates inside their own focus trees, no same-row mutually exclusive line passing through an in-tree focus node by the mechanical scan, and no same-parent same-row sibling spacing of 1 or less.
- MFR had one narrow layout issue: `MFR_factory_war_cabinet` fanned into same-row children at x 6, 7, and 8. The patch spaces that local cluster to x 6, 8, and 10 while preserving prerequisites, route locks, rewards, and AI.

## Validation

- Mechanical brace balance check passed on all four requested focus files: final brace depth `0`, minimum depth `0`.
- Post-patch MFR same-parent same-row crowding scan reports `MFR crowded_siblings 0`.
- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt common/national_focus/005_soviet_collapse_ancient_restorations.txt` passed.

## Remaining Risks

- Ukraine, Belarus, and Kazakhstan still rely heavily on repeated generic focus helper families. The current pass found no outright duplicate reward calls, but the play-feel complaint likely needs a broader route-specific reward pass rather than more one-line cleanup.
- Kazakhstan is large and compact at 92 focuses; even with no mechanical overlap in the scan, it should still get an in-game visual pass because wide cross-branch prerequisites can create busy diagonal pathlines.
- Belarus is cleaner than earlier reports by mechanical scan, but its corridor/security/foreign families still share many reward patterns and may feel shallow without route-specific mechanical unlocks.
- Custom splinter trees remain structurally repetitive. The high-chaos countries have aggressive payloads in many endpoints, but several branch families still use mirrored layouts and helper mixes.
