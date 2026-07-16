# Event 006 Mediterranean GFX handoff

The full registration set is live in `interface/006_independence_wave_mediterranean_assets.gfx`; no additional sprite-name or texture-path decisions are required.

## Focus sprites

Each 94×86 texture has a base sprite and a matching `_shine` sprite using `gfx/FX/buttonstate.lua`.

| Token | Final texture | Live sprites |
|---|---|---|
| `independence_wave_cor_customs` | `gfx/interface/goals/006_independence_wave/mediterranean/goal_independence_wave_cor_customs.dds` | `GFX_goal_independence_wave_cor_customs`, `GFX_goal_independence_wave_cor_customs_shine` |
| `independence_wave_cor_mountain_communes` | `gfx/interface/goals/006_independence_wave/mediterranean/goal_independence_wave_cor_mountain_communes.dds` | base, `_shine` |
| `independence_wave_arx_shipping` | `gfx/interface/goals/006_independence_wave/mediterranean/goal_independence_wave_arx_shipping.dds` | base, `_shine` |
| `independence_wave_arx_mountain_guards` | `gfx/interface/goals/006_independence_wave/mediterranean/goal_independence_wave_arx_mountain_guards.dds` | base, `_shine` |
| `independence_wave_asx_port` | `gfx/interface/goals/006_independence_wave/mediterranean/goal_independence_wave_asx_port.dds` | base, `_shine` |
| `independence_wave_asx_grain_straits` | `gfx/interface/goals/006_independence_wave/mediterranean/goal_independence_wave_asx_grain_straits.dds` | base, `_shine` |
| `independence_wave_asx_two_sicilies` | `gfx/interface/goals/006_independence_wave/mediterranean/goal_independence_wave_asx_two_sicilies.dds` | base, `_shine` |
| `independence_wave_form05_maritime_congress` | `gfx/interface/goals/006_independence_wave/mediterranean/goal_independence_wave_form05_maritime_congress.dds` | base, `_shine` |

## Decision sprites

All textures are 32×32 and registered as `GFX_decision_<token>`.

| Token | Final texture |
|---|---|
| `independence_wave_cor_customs` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_cor_customs.dds` |
| `independence_wave_cor_mountain_communes` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_cor_mountain_communes.dds` |
| `independence_wave_arx_shipping` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_arx_shipping.dds` |
| `independence_wave_arx_mountain_guards` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_arx_mountain_guards.dds` |
| `independence_wave_asx_port` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_asx_port.dds` |
| `independence_wave_asx_grain_straits` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_asx_grain_straits.dds` |
| `independence_wave_asx_two_sicilies` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_asx_two_sicilies.dds` |
| `independence_wave_form05_maritime_congress` | `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_maritime_congress.dds` |

## Lifecycle-idea sprites

All textures are 64×64. The engine resolves each gameplay `picture = <token>` to `GFX_idea_<token>`.

| Token | Final texture |
|---|---|
| `independence_wave_mediterranean_island_crisis` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_mediterranean_island_crisis.dds` |
| `independence_wave_mediterranean_state_compact` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_mediterranean_state_compact.dds` |
| `independence_wave_mediterranean_constitutional_assembly` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_mediterranean_constitutional_assembly.dds` |
| `independence_wave_mediterranean_mountain_communes` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_mediterranean_mountain_communes.dds` |
| `independence_wave_mediterranean_labor_compact` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_mediterranean_labor_compact.dds` |
| `independence_wave_mediterranean_crown_council` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_mediterranean_crown_council.dds` |
| `independence_wave_mediterranean_island_guard` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_mediterranean_island_guard.dds` |
| `independence_wave_mediterranean_patron_customs` | `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_mediterranean_patron_customs.dds` |

## Report sprite

- Sprite: `GFX_report_event_006_mediterranean_island_incidents`
- Texture: `gfx/event_pictures/006_independence_wave/mediterranean/report_event_006_mediterranean_island_incidents.dds`
- Size: 210×176
- Live binding: seven `picture = GFX_report_event_006_mediterranean_island_incidents` uses in `events/006_independence_wave_mediterranean.txt`

## Consumer coverage

- Focus registrations cover every accepted Mediterranean icon token in `common/national_focus/006_independence_wave_focus.txt`, including all three live maritime-congress bridge uses.
- Decision registrations cover every accepted icon token in `common/decisions/006_independence_wave_mediterranean_decisions.txt`.
- Idea registrations cover every one of the eight accepted `picture` tokens in `common/ideas/006_independence_wave_mediterranean_ideas.txt`.
- The report registration covers all seven Mediterranean event consumers.
- Exact row-level counts and evidence are frozen in `notes/requirement_to_runtime_crosswalk.md` and `notes/runtime_validation.json`.

## Ownership boundary

This package owns the shared `GFX_goal_independence_wave_form05_maritime_congress` and `GFX_decision_independence_wave_form05_maritime_congress` bridge pair because COR, ARX, and ASX use them before formation. It does not own the dedicated FORM05 charter/delegation, shipping, defence, customs, capital, proclamation, post-formation lifecycle-idea, emblem/flag, or charter-congress report surfaces. Those remain outside this package and were neither generated nor registered here.

No advisor assets were created or registered.

## Regeneration and review

Run `python docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/process_assets.py` from the mod root. The script processes only this package's 25 selected sources, writes the exact runtime paths above, validates PNG transparency and full DDS headers, proves decoded DDS pixels equal the processed PNGs, checks registrations and live consumers, rejects byte-identical family duplicates, and rebuilds both compact review sheets.

There are no animation frames, frame timing values, loop states, or anchor overrides. No fallback or simplification is present.
