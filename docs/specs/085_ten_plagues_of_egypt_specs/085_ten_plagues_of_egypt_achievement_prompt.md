# Event 085 — Achievement Implementation and Art Prompt

Implement the twelve Ten Plagues achievements defined in [Part 18](085_ten_plagues_of_egypt_spec_part_18_achievements.md), which is the only copy of their conditions.
Read Parts 7, 8, 12, 14 and 18 first, then follow the repository rules and the `chaos-redux-events`, `chaos-redux-event-assets` and `chaos-redux-subagents` skills.

## Registry and conditions

- Check `common/achievements/chaos_redux_achievements.txt` and map each semantic `tp85_*` key to a collision-free event-prefixed ID such as `085_ten_plagues_of_egypt_<suffix>`; record the mapping once and use it for conditions, localisation, icons and docs.
- Implement every condition, disqualifier, eligibility rule, fixed denominator and hidden-to-visible transition from Part 18, reading the same records as gameplay: Deaths entries, Passover status, objective results, Migration transfers and corridors, Natural Disasters results and Famine stages.
- No unlock may come from an acknowledgement or a claimed result; save and load never disqualifies.
- Write final titles and descriptions from the directions; do not ship the working labels.
- Test each listed disqualifier as a negative case.

## Icons

- For each of the twelve icon directions, generate one original subject with genuine transparency, no text, frame, background, red cross or checkerboard.
- Build the colored, grey and not-eligible source triplet with the skill's immutable templates and unchanged overlay, and process it with `.claude/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`; never feed a single file or redraw the cross.
- Runtime DDS files sit directly in `gfx/achievements/` named by the final ID and the required suffixes.
- Route icon production to `chaosx_icon_artist` with a self-contained prompt per `chaos-redux-subagents`; the parent wires the framework and reviews the icons at native size.

## Return

Final IDs and localisation keys, condition and tracker notes, changed files, the 36 processed icon states with their source manifest, negative-case results and any unresolved hooks.
