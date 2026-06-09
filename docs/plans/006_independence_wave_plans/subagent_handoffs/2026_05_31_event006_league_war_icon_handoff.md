# Event006 `cr_league_war_victory` Achievement Icon Handoff

Date: `2026-05-31`

Scope: bounded achievement icon package only for `cr_league_war_victory` / "The Charter Held". No `.gfx`, localisation, gameplay, events, decisions, focuses, scripted files, country files, or other docs outside the asset manifest and this handoff were edited.

## Reference inspection

- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_grey.png`
- `.agents/skills/chaos-redux-event-assets/assets/achievements/achievement_not_eligible.png`
- Existing Event006 achievement contact sheet package for style, contrast, framing, and triplet-state consistency

## Source mode

- Mode: `$imagegen`
- Generated image path: `/home/klim/.codex/generated_images/019e7f5c-91c2-7f82-9662-dbc6e6de20cb/ig_01810fb2f88ec80b016a1c828afc9881918e10db560c093512.png`
- Direction followed: small sealed charter over crossed rifles, readable at 64x64, no country flags, no modern logos, no text

## Files changed

- `docs/assets/006_independence_wave/achievement_icons/prompts/cr_league_war_victory.txt`
- `docs/assets/006_independence_wave/achievement_icons/source_png/cr_league_war_victory_source.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory_grey.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory_not_eligible.png`
- `docs/assets/006_independence_wave/achievement_icons/contact_sheets/raw_sources_64_contact.png`
- `docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet.png`
- `docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet_all_states.png`
- `docs/assets/006_independence_wave/achievement_icons/manifest.md`
- `gfx/achievements/cr_league_war_victory.dds`
- `gfx/achievements/cr_league_war_victory_grey.dds`
- `gfx/achievements/cr_league_war_victory_not_eligible.dds`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_league_war_icon_handoff.md`

## Processing notes

- The generated source already matched the Chaos Redux achievement-card treatment, so processing stayed close to the source composition.
- Completed icon was resized to `64x64` with light sharpening.
- Grey and not-eligible variants were derived locally from the completed icon to match the existing Event006 achievement triplet pattern.
- DDS conversion used `convert -define dds:compression=none`.

## Proposed wiring handoff

- Achievement id: `cr_league_war_victory`
- Proposed sprite name: `GFX_achievement_cr_league_war_victory`
- Proposed `.gfx` file target: `interface/chaosx_achievements.gfx`
- Final DDS paths:
  - `gfx/achievements/cr_league_war_victory.dds`
  - `gfx/achievements/cr_league_war_victory_grey.dds`
  - `gfx/achievements/cr_league_war_victory_not_eligible.dds`

## Validation

- Commands run:
  - `identify docs/assets/006_independence_wave/achievement_icons/source_png/cr_league_war_victory_source.png docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory.png docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory_grey.png docs/assets/006_independence_wave/achievement_icons/processed_png/cr_league_war_victory_not_eligible.png gfx/achievements/cr_league_war_victory.dds gfx/achievements/cr_league_war_victory_grey.dds gfx/achievements/cr_league_war_victory_not_eligible.dds`
  - `identify docs/assets/006_independence_wave/achievement_icons/contact_sheets/raw_sources_64_contact.png docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet.png docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet_all_states.png`
- Result:
  - Source PNG validates as `1254x1254 PNG`
  - Processed PNG triplet validates as `64x64 PNG`
  - Final DDS triplet validates as `64x64 DDS`
  - Updated contact sheets exist and include the new icon

## Remaining risks

- `.gfx` wiring was intentionally left untouched per task scope, so the sprite alias above remains a proposed handoff value until the parent agent registers or confirms it.
