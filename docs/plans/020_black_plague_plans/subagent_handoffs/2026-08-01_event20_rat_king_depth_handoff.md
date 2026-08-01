# Event 20 Rat King depth handoff

## Scope

This parent-owned tranche deepens `RTX` without adding a third rat tag, a new disease category, human manpower, normal equipment, or 3D models. The separate Rat King route remains compatible with the existing two-tag architecture: `RTA` is the reusable base carrier and `RTX` is the sentient Royal Basin.

## Changed files

- `common/national_focus/020_black_plague_rat_king_focus_tree.txt`
  - expanded the tree from 50 to 70 focuses;
  - replaced every generic or MCP-unresolved icon reference with an existing Event 020 custom goal sprite;
  - added six-focus Crown, Council, and Hierophancy lanes plus Royal Node Watch and Crown Strike Preparations;
  - all rewards use existing royal registers, division-cap bonuses, brood mass, or terminal preparation;
  - no new country tags, unit types, equipment, or world-periodic actions.
- `localisation/english/020_black_plague_rat_focus_l_english.yml`
  - added title and description pairs for all 20 focuses; file remains UTF-8 with BOM.
- `docs/events/020_black_plague/rat_king_depth.md`
  - records the route contract, register effects, and future extension boundary.
- `docs/events/020_black_plague/overview.md`
  - aligns the live overview with 50-focus RTA and 70-focus RTX route surfaces.
- `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`
  - reconciles the current focus counts and remaining scope.

## Validation evidence

- `hoi4.focus_inspect` on `black_plague_rat_king_focus_tree` returned `focusCount: 70` with zero missing icon diagnostics and complete title resolution. Remaining diagnostics are authored-layout and missing-filter warnings only.
- Focus IDs are unique, brace balance is 448/448, and every focus has a title/description localization pair (the tree container's `black_plague_rat_king_focus_tree_desc` is intentionally not a focus localization key).
- The localization file retains a UTF-8 BOM.

## Remaining risks

The focus inspector reports layout/filter warnings inherited from the authored tree; no unresolved focus references remain. Live focus timing, AI completion order, and fresh-save route transfer still require user-side in-game validation. Bespoke rat models remain outside the current goal by explicit instruction.
