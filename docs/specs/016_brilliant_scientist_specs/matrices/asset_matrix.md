# Asset matrix for Brilliant Scientist

This matrix is a planning summary. The full asset prompt is in `prompts/brilliant_scientist_asset_prompt.md`.

## Core portrait progression

| Stage | Use | Source mode | Animation |
| --- | --- | --- | --- |
| Stage 0 | Advisor and special-project scientist baseline | Copy and rename `portrait_generic_biowarfare_europe_male_01` as the base asset, then process as needed | Static |
| Stage 1 | National fame | Generated or edited fictional portrait based on stage 0 direction | Static |
| Stage 2 | Severe secret projects | Generated fictional portrait | Static or subtle non-animated counterpart |
| Stage 3 | Dangerous anomaly | Generated fictional portrait | Optional animated overlay |
| Stage 4 | Sovereign or alien reveal | Generated fictional portrait | Required frame-sheet animation with a static non-animated counterpart |

## Gameplay icons

| Asset group | Target size | Source mode | Notes |
| --- | ---: | --- | --- |
| Advisor icon | Existing portrait dimensions or character pattern | Base copy then variants | Stable naming needed |
| Idea icons | 64x64 | Generated icon art | Separate from focus icons |
| Decision category icon | Existing category pattern | Generated icon art | Laboratory seal or equation motif |
| Decision icons | 32x32 | Generated icon art | One per major project and emergency family |
| Focus icons | 94x86 | Generated icon art | Host branch and Kruger tree family |
| Achievement icons | 64x64 plus variants | Generated icon art | Completed, grey, not-eligible variants later |
| Tech or special project icons | 64x64 or 132x52 | Generated icon art | Only if implementation adds new tech visuals |

## Country and super-event assets

| Asset | Size | Source mode | Notes |
| --- | ---: | --- | --- |
| Kruger flag normal | 82x52 TGA | Generated fictional flag | Must also produce medium and small |
| Kruger flag medium | 41x26 TGA | Generated fictional flag | Validate orientation |
| Kruger flag small | 10x7 TGA | Generated fictional flag | Validate readability |
| Route flags | HOI4 flag sizes | Generated fictional flags | Clone, robot, alien, final device if cosmetic tags exist |
| Sovereign reveal super-event image | 457x328 | Generated fictional super-event image | Period-authentic laboratory state scene |
| Final device super-event image | 457x328 | Generated fictional super-event image | No abstract geometry as final art |
| Defeat aftermath image | 457x328 | Generated or sourced depending on final direction | Use generated if fictional aftermath scene |
| Report event images | 210x176 | Generated period-documentary images | Process through report card treatment |
| News event images | 397x153 | Generated or sourced, black and white | Use for global reveal or scandals |

## Animated assets

| Asset | Surface | Frame direction |
| --- | --- | --- |
| Stage 4 Kruger portrait | Leader portrait or scripted GUI overlay | 8 to 12 real source frames, alien eye light and instrument glow, no transform-only animation |
| Decision category danger seal | Decision category or scripted GUI | 6 to 8 frames, active warning pulse based on Strangeness or Autonomy |
| Final device progress frame | Custom GUI if implemented | 8 frames, state-driven glow that changes with arming progress |
| Project family selected cards | Custom GUI optional | Static variants usually enough unless GUI is built |

## Reference folders asset agents must inspect

- `.agents/skills/chaos-redux-event-assets/assets/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/focuses`
- `.agents/skills/chaos-redux-event-assets/assets/achievements`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/flags`
- `.agents/skills/chaos-redux-event-assets/assets/special_projects`
