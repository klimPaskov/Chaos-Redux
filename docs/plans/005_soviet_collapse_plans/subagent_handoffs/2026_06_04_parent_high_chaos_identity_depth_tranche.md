# Event005 Parent High-Chaos Identity Depth Tranche

Date: 2026-06-04

## Scope

Bounded parent patch for the current Soviet Collapse pass. This tranche deepens two high-chaos identity routes without adding new standalone focus ideas or touching flag assets.

No `gfx/flags`, `.tga`, flag sprite, or flag `.gfx` files were touched.

## Required References Used

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- Core offline wiki pages listed in `AGENTS.md`
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- Vanilla HOI4 effects and trigger documentation

## Files Changed

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Gameplay Changes

- Added `soviet_collapse_apply_cfr_city_network_surge`, a one-time CFR construction payoff used by existing focus helpers.
- CFR foreign factory, protectorate, border-permit, and rebuild-without-Moscow helpers now connect more clearly to the construction-state fantasy:
  - controlled core states receive civilian industry and infrastructure through the surge
  - a supply hub is added to the construction network
  - offsite civilian industry and construction mandate depth increase
  - border-permit planning now also triggers high-chaos neighbor expansion planning
- DSC endgame now updates the existing Dead Soldiers idea path instead of stacking extra bloat:
  - removes `dsc_dead_soldiers_congress` / `dsc_grave_regiment_rivalries` when present
  - adds the stronger existing `dsc_dead_army_politics` idea
  - grants a larger matching equipment and manpower package
- DSC neighbor war helper now declares immediate annexation wars at the dead-army endgame or highest chaos tier, while retaining normal war-goal preparation at lower intensity.

## Validation

- Brace balance checked for `common/scripted_effects/005_soviet_collapse_effects.txt` and `localisation/english/005_soviet_collapse_l_english.yml`: clean.
- `git diff --check` on touched script/localisation files: clean.
- Unsupported comparison-operator scan: clean.
- Localisation BOM check for `005_soviet_collapse_l_english.yml`: preserved.
- Flag diff guard: no flag files, `.tga` files, or flag sprite definitions in the diff.

## Remaining Work

- This does not complete the whole Soviet Collapse goal. Remaining work still includes evolution-detail spreadsheet alignment, remaining focus-tree route/layout cleanup, decision visibility for breakaways such as Tajikistan, and a broader release/escalation audit.
- This tranche intentionally avoids new art, new focus icons, and new standalone ideas.
