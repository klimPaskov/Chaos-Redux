# Local follow-up: release, visibility, and focus audit

Subagent route: attempted `chaosx_focus_tree_auditor` with `fork_context=false`; runtime rejected the spawn because the agent thread limit was reached. This note records the local audit and patches made instead.

## User-facing issues addressed

- Stronger republics and industrial successors need much larger initial forces.
- Union Unmade must catch layered releasables such as Arctic, Siberian, and northern tags whose cores may move from Moscow to another breakaway during the same terminal rupture.
- Human foreign patrons can select a dynamically released breakaway and still open an empty decision panel.
- Soviet Collapse event details need both high-chaos and extreme-successor previews in the event-details window.
- Listed TGA flags must use the correct top-left origin metadata.

## Patches made

- `common/script_constants/005_soviet_collapse_constants.txt`
  - Raised chaos-tier follow-on release burst counts, the follow-on cap, terminal ordinary release passes, and dynamic breakaway force scaling.
  - Large republics now scale much harder from controlled states and factories, with higher regional, major, and terminal field-brigade bonuses.
- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
  - Raised Soviet Collapse triggerable scenario unit scaling across intensity levels, especially high and maximum intensity.
- `common/scripted_effects/005_soviet_collapse_effects.txt`
  - Gathering Storm now grants the extra first-wave release pass.
  - Selecting a foreign patron target force-normalizes that target as a breakaway before opening the target decision desk.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - Explicitly selected patron targets no longer fail the intervention decision gate just because a dynamic release path missed the full breakaway classifier.
- `common/scripted_effects/chaosx_settings_effects.txt`
  - Event 5 details now register both the high-chaos successor preview and the extreme successor preview.
- `docs/events/005_soviet_collapse.md`
  - Updated implementation notes for the stronger dynamic force scaling.
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_4_releases_leagues_union_unmade.md`
  - Updated release/unit expectations to match the stronger implementation.
- `gfx/flags/**`
  - Rechecked all user-listed base, medium, and small TGA files. All 162 checked files already had the top-left origin bit set; no pixel flip was performed.

## Focus audit evidence

Mechanical parser pass over:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Results:

- 1698 focus blocks parsed.
- 0 focuses with multiple direct `add_ideas` rewards.
- 0 focuses with duplicate direct `add_ideas`.
- 0 direct idea-only reward focuses found by the parser.
- 0 same-tile position collisions found.
- 0 non-reciprocal mutual-exclusion links found.

The remaining shallow-focus problem is therefore mostly in helper cadence, route identity, and generated reward structure rather than direct duplicate `add_ideas` lines inside focus blocks. Existing prior handoffs already identify high-impact follow-up areas: custom splinter route identity helpers, Ukraine layout/branch depth, Belarus spacing, and chaos-country bespoke expansion packages.

## Remaining risks

- This pass did not complete the full focus-tree route redesign. The mechanical audit did not find direct duplicate idea rewards, but it does not prove that helper effects are interesting or that every route has enough bespoke decisions, cores, units, or war goals.
- Triggerable scenario high/max intensity unit counts are intentionally very aggressive and may need live balance tuning if division counts become too heavy.
- The selected breakaway decision fix assumes the selected target should be trusted once the player has chosen it from the breakaway array. This is safer for dynamic releases but should be watched for impossible targets if another system adds non-breakaway countries to the same array.
