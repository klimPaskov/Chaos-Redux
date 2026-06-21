# Event 012 Africa Decision Category Load Error Handoff

Date: 2026-06-21

## Scope

Fixed/audited the Event 012 Africa decision category load-error surface reported from `common/decisions/012_africa_decisions.txt`.

The current checkout already has the legal split:

- Category metadata lives in `common/decisions/categories/012_africa_categories.txt`.
- Decision entries live in `common/decisions/012_africa_decisions.txt`, grouped under already-defined category ids.

No focus files were inspected or edited.

## Files Changed

- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_decision_category_load_error_handoff.md`

No gameplay file edit was needed in the current checkout because the Event 012 category metadata is already outside `common/decisions/012_africa_decisions.txt`.

## Category Ids Verified

These category definitions are present in `common/decisions/categories/012_africa_categories.txt` and are used as top-level decision groups in `common/decisions/012_africa_decisions.txt`:

- `africa_continental_congress_category`
- `africa_charter_league_diplomacy_category`
- `africa_charter_member_category`
- `africa_liberation_war_office_category`
- `africa_regional_integration_category`
- `africa_diaspora_return_category`
- `africa_authority_atlas_category`
- `africa_high_chaos_category`
- `africa_continent_sponsor_category`
- `africa_rsa_civil_war_emergency_category`

The reported older ids `africa_bestiary_category` and `africa_world_order_category` do not exist in the current Event 012 decision file. The current equivalents appear to be `africa_high_chaos_category` and `africa_continent_sponsor_category`.

## Why The Parse Error Is Fixed

The HOI4 decision parser expects `common/decisions/*.txt` to contain decisions inside pre-defined category blocks. Category-only fields such as `icon`, `picture`, `visible_when_empty`, and `scripted_gui` belong in category definitions under `common/decisions/categories/*.txt`.

Validation of the current Event 012 files found:

- `common/decisions/012_africa_decisions.txt` contains no `scripted_gui =`, `picture =`, or `visible_when_empty =` assignments.
- `scripted_gui = africa_continental_congress_scripted_gui` exists only in `common/decisions/categories/012_africa_categories.txt`.
- `africa_continental_congress_scripted_gui` is defined in `common/scripted_guis/012_africa_scripted_gui.txt` with `context_type = decision_category`.
- Every Event 012 top-level decision category id has a matching category definition.

That removes the reported failure mode where the decisions database parses a category definition as if it were a decision group, reports `Unknown category`, and then treats `scripted_gui` plus subsequent decision ids as unexpected tokens.

## Validation Performed

- Consulted offline Paradox wiki pages required for decision/category work, including Decision modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Idea modding, AI modding, Interface modding, and Scripted GUI modding.
- Consulted vanilla `~/projects/Hearts of Iron IV/common/decisions/_documentation.md`.
- Consulted vanilla category examples under `~/projects/Hearts of Iron IV/common/decisions/categories/`, including category files using `scripted_gui`.
- Compared Event 012 top-level decision category ids in `common/decisions/012_africa_decisions.txt` against definitions in `common/decisions/categories/012_africa_categories.txt`; no missing category ids were found.
- Checked `common/decisions/012_africa_decisions.txt` for category-only tokens: no `scripted_gui =`, `picture =`, or `visible_when_empty =` assignments remain there.

## Skipped Validation

- Did not launch HOI4 or perform an in-game reload check; this environment does not provide a deterministic game-load validation path.
- Did not run broad decision balance, cost, AI, mission-quality, or focus integration audits because the task was limited to category parse errors.

## Remaining Risks

- The user-provided log line numbers and category ids match an older/bad Event 012 decision file layout more closely than the current checkout. If the same log still appears after this checkout is used, there may be another copy of `012_africa_decisions.txt` in the active mod load path outside this repository.
- This handoff does not resolve unrelated decision quality or balance issues. It only verifies the category/database split that caused the reported parser cascade.
