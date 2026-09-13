# Weaponized zombie profile helpers

## `initialize_cxt_weaponized_zombie_profile`

Purpose: initialize the CXT sandbox country before scripted project completion bypasses ordinary prototype choices.
Scope: country, guarded by `tag = CXT`.
Inputs: existing country research-step flags and profile variables; defaults come from `weaponized_zombie_cxt_fixture` in `common/script_constants/zombie_special_project_constants.txt`.
Outputs: complete six-trait country profile and country research-step flags, with neurobiological nature, dead life state, and expanded resources.
Side effects: calls `reset_weaponized_zombie_project_tracking` when the six tracked trait steps or variables are incomplete, removing stale resolution, lifecycle-choice, accident, and initial-stockpile markers before constructing the fixture.
The existing reset contract retains broader country completion and availability state.
A fully tracked six-trait profile is preserved, so repeated calls do not reroll or stack trait deltas.
The initializer does not complete the native project, charge research resources or manpower, set project flags, launch an outbreak, create event targets, or display a report.
Country stage flags represent the recorded fixture path rather than paid runtime prototype iterations.

The fixture reproduces existing ordinary choices: acquisition extraction, neurobiological nature, dead life state, medium strength/infectiousness/speed/durability/cure resistance/obedience, approved trials, expanded resources, skipped field test, routine refinement, and finalized deployment.
The source-derived profile is strength 3, infectiousness 3, speed 2, durability 2, cure resistance 2, obedience 2, test subjects 3, and accident risk 1.55.
This is an explicitly accepted CXT testing fixture and changes no ordinary-country trait choice, AI weight, probability, or research cost.
`docs/testing/runtime_repairs/20260913_cxt_history_followup/zombie_choice_profile_check.json` records the exact option tokens and verifies the fixture against their deltas.

Call sites: `complete_weaponized_zombie_project_from_project_output`, `complete_weaponized_zombie_project`, and the CXT owner’s setup before native scripted completion.
The first two direct calls make the initializer safe when generic completion is reached without the explicit setup call.
`complete_weaponized_zombie_project` retains completed gameplay bonuses and achievements but does not schedule the success report for CXT.
Ordinary countries retain the same final report and mechanical effects.

```text
# Execute in CXT country scope before native project completion.
initialize_cxt_weaponized_zombie_profile = yes
```

## Ordinary profile lifecycle

Vanilla `common/special_projects/projects/documentation.md` defines `iteration_output.country_effects` and `project_output.country_effects` as country scope with `FROM` pointing to the project.
The zombie project follows that contract: acquisition resets country tracking, subsequent prototype choices add temporary deltas through `weaponized_zombie_apply_profile_delta`, and country research flags accompany project flags written through `FROM`.
Country variables are already the persistent profile source; no project-to-country copy is required.
Completion resolves that same profile, applies existing bonuses, and schedules the final report for ordinary countries.
All ordinary strength, infectiousness, speed, durability, and cure-resistance options contribute positive values; the weakest obedience choice deliberately contributes zero.
The CXT fixture does not replace or clamp ordinary profiles.

## Assets and future work

No icons, sprites, GUI layouts, portraits, or assets are introduced by this helper.
The existing report uses `GFX_report_event_generic_biowarfare` and is unchanged.
If a future sandbox requires several representative strains, add explicitly documented fixture variants derived from real choice sequences rather than a universal buff.