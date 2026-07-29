# Event 020 Rat identity and weaponization icon handoff

## Scope completed

The asset package adds four dedicated Rat Nation idea sprites, the long weaponization special-project icon, four distinct weaponization approach decision icons, eleven critical Rat/Rat King focus icons, five fictional non-human leader portraits, and unique normal/medium/small flags for RTA through RTM plus RTX. No gameplay, localisation, or `.gfx` file was edited.

## Wiring snippets for the main agent

Use the existing event-owned asset `.gfx` conventions and preserve these stable names:

```text
spriteType = { name = "GFX_sp_black_plague_weaponization" texturefile = "gfx/interface/special_project/project_icons/sp_black_plague_weaponization.dds" }
spriteType = { name = "GFX_decision_black_plague_weapon_safety_first" texturefile = "gfx/interface/decisions/020_black_plague/decision_weaponization_safety_first.dds" }
spriteType = { name = "GFX_decision_black_plague_weapon_military_acceleration" texturefile = "gfx/interface/decisions/020_black_plague/decision_weaponization_military_acceleration.dds" }
spriteType = { name = "GFX_decision_black_plague_weapon_dual_use" texturefile = "gfx/interface/decisions/020_black_plague/decision_weaponization_dual_use.dds" }
spriteType = { name = "GFX_decision_black_plague_weapon_defensive_conversion" texturefile = "gfx/interface/decisions/020_black_plague/decision_weaponization_defensive_conversion.dds" }
```

The idea `picture` values already present in `common/ideas/020_black_plague_rat_ideas.txt` should resolve through `GFX_idea_black_plague_rat_brood_instinct`, `GFX_idea_black_plague_rat_no_civilian_economy`, `GFX_idea_black_plague_rat_dominion`, and `GFX_idea_black_plague_rat_king_dominion`.

For focus nodes, use the goal-sprite convention because the live focus files use `icon = GFX_goal_*`: `GFX_goal_black_plague_rat_first_warren`, `GFX_goal_black_plague_rat_urban_warren`, `GFX_goal_black_plague_rat_field_brood`, `GFX_goal_black_plague_rat_dock_brood`, `GFX_goal_black_plague_rat_war_brood`, `GFX_goal_black_plague_rat_brood_signal`, `GFX_goal_black_plague_rat_king_the_royal_basin`, `GFX_goal_black_plague_rat_absolute_crown`, `GFX_goal_black_plague_rat_brood_council`, `GFX_goal_black_plague_rat_breath_hierophancy`, and `GFX_goal_black_plague_rat_earned_terminal_route`.

Portrait runtime files are under `gfx/leaders/020_black_plague/` and are ready for dedicated leader sprite definitions: `portrait_rat_urban_brood.dds`, `portrait_rat_field_brood.dds`, `portrait_rat_dock_brood.dds`, `portrait_rat_war_brood.dds`, and `portrait_rat_king_static.dds`. The current country initialiser still points to a generic portrait; wiring those character tokens remains gameplay scope for the main agent.

Flags are intentionally root-only under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` because HOI4 resolves tag flags from those locations. The design source and processed previews are retained under `docs/assets/020_black_plague/source_png/flags/` and `processed_png/flags/`.

## Validation evidence

- Canonical contact sheets were inspected before generation: ideas, national focuses, decisions, special projects, flags, and leader portraits.
- Final idea DDS dimensions are 64x64; decisions 33x32; focuses 94x86; special project 161x98; portraits 156x210.
- Every new DDS has the standard 128-byte uncompressed BGRA header, exact payload length, texture caps, and alpha values spanning transparent and opaque pixels for icon families.
- Every flag tag has normal 82x52, medium 41x26, and small 10x7 TGA outputs.
- Review sheets: `docs/assets/020_black_plague/contact_sheets/event20_rat_ideas_contact_sheet.png`, `event20_weaponization_decisions_contact_sheet.png`, `event20_rat_focus_contact_sheet.png`, `event20_rat_portraits_contact_sheet.png`, and `event20_rat_flags_contact_sheet.png`.

## Explicit follow-up gaps

The full Rat and Rat King focus trees still need the remaining focus-specific icons, and the wider Rat decision family, route/world-end cosmetic flags, animated Rat King portrait/seal, and the 14 achievement completed/grey/not-eligible triplets remain unproduced. No generic, resized-cross-type, placeholder, or transform-only substitute was added for those rows.
