# Event 020 asset manifest

Status: `complete`.

This is the event-root manifest required by `chaos-redux-event-assets`. Asset-family sections link to their detailed generation briefs, source mode, visual directions, prompts, and DDS QA.

## Dedicated response-category picture (2026-08-09)

| Asset | Intended use | Source / processed package | Runtime DDS | Size | Sprite / consumer | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `decision_cat_picture_black_plague_response` | Dedicated national cure and strategic-management decision category; plague doctors treating a patient | `decision_category_picture_black_plague_response/` | `gfx/interface/decisions/020_black_plague/decision_cat_picture_black_plague_response.dds` | 114×101, one static frame | `GFX_decision_cat_picture_black_plague_response` in `interface/020_black_plague_response.gfx`; `black_plague_response_category` | complete and wired |

The source is a fictional generated 1930s–WWII treatment scene with no readable text, simulated controls, modern equipment, or gore. The package retains the exact ImageGen prompt, source PNG, processed PNG, DDS round-trip, contact sheet, header QA, and wiring handoff in [`decision_category_picture_black_plague_response/`](decision_category_picture_black_plague_response/).

## RTA hierarchy focus icons

Detailed generation briefs, source mode, visual directions, and DDS QA are in [`manifests/event020_rat_hierarchy_icons_manifest.md`](manifests/event020_rat_hierarchy_icons_manifest.md). Exact ImageGen prompt text is retained in [`prompts/rat_hierarchy_focus_icons_2026-08-01.md`](prompts/rat_hierarchy_focus_icons_2026-08-01.md).

| Asset | Event / slug | Asset type and intended use | Source mode | Source PNG | Processed PNG | Final DDS | Target size | Sprite / `.gfx` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `black_plague_rat_four_mouths` | Event 020 / `black_plague` | Focus icon / RTA hierarchy route | `$imagegen` | `source_png/focus_black_plague_rat_four_mouths_imagegen_source.png` | `processed_png/goal_black_plague_rat_four_mouths.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_four_mouths.dds` | `94x86` | `GFX_goal_black_plague_rat_four_mouths` / `interface/020_black_plague_rat_identity.gfx` |
| `black_plague_rat_choose_a_voice` | Event 020 / `black_plague` | Focus icon / RTA hierarchy route | `$imagegen` | `source_png/focus_black_plague_rat_choose_a_voice_imagegen_source.png` | `processed_png/goal_black_plague_rat_choose_a_voice.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_choose_a_voice.dds` | `94x86` | `GFX_goal_black_plague_rat_choose_a_voice` / `interface/020_black_plague_rat_identity.gfx` |
| `black_plague_rat_read_the_marks` | Event 020 / `black_plague` | Focus icon / RTA hierarchy route | `$imagegen` | `source_png/focus_black_plague_rat_read_the_marks_imagegen_source.png` | `processed_png/goal_black_plague_rat_read_the_marks.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_read_the_marks.dds` | `94x86` | `GFX_goal_black_plague_rat_read_the_marks` / `interface/020_black_plague_rat_identity.gfx` |
| `black_plague_rat_many_nests_one_signal` | Event 020 / `black_plague` | Focus icon / RTA hierarchy route | `$imagegen` | `source_png/focus_black_plague_rat_many_nests_one_signal_imagegen_source.png` | `processed_png/goal_black_plague_rat_many_nests_one_signal.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_many_nests_one_signal.dds` | `94x86` | `GFX_goal_black_plague_rat_many_nests_one_signal` / `interface/020_black_plague_rat_identity.gfx` |
| `black_plague_rat_fang_above_the_warren` | Event 020 / `black_plague` | Focus icon / RTA hierarchy route | `$imagegen` | `source_png/focus_black_plague_rat_fang_above_the_warren_imagegen_source.png` | `processed_png/goal_black_plague_rat_fang_above_the_warren.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_fang_above_the_warren.dds` | `94x86` | `GFX_goal_black_plague_rat_fang_above_the_warren` / `interface/020_black_plague_rat_identity.gfx` |
| `black_plague_rat_stolen_route_memory` | Event 020 / `black_plague` | Focus icon / RTA hierarchy route | `$imagegen` | `source_png/focus_black_plague_rat_stolen_route_memory_imagegen_source.png` | `processed_png/goal_black_plague_rat_stolen_route_memory.png` | `gfx/interface/goals/020_black_plague/goal_black_plague_rat_stolen_route_memory.dds` | `94x86` | `GFX_goal_black_plague_rat_stolen_route_memory` / `interface/020_black_plague_rat_identity.gfx` |

Runtime `.gfx` and focus wiring remain parent-owned, and the handoff is now promoted in `interface/020_black_plague_rat_identity.gfx` and the RTA focus tree. No models, tags, gameplay, or localisation files were changed by this package.

## Animated seal packages (2026-08-02)

| Asset | Intended use | Source / processed package | Runtime DDS | Size / animation | Sprite names | Handoff |
| --- | --- | --- | --- | --- | --- | --- |
| `black_plague_crisis_seal` | Shared disease-board Severe Crisis / Collapsed header | `animations/black_plague_crisis_seal/source_frames/` and `processed_frames/` | `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_static.dds`; `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_sheet.dds` | 64x64 frames; 8 frames; 512x64 sheet; 6 FPS loop | `GFX_black_plague_crisis_seal_static`; `GFX_black_plague_crisis_seal_animated` | `animations/black_plague_crisis_seal/{manifest.md,gfx_handoff.md}` |
| `black_plague_rat_king_terminal_readiness` | Rat King terminal/world-end readiness decision seal, reserved for a future scripted-GUI panel | `animations/rat_king_world_end_readiness_seal/source_frames/` and `processed_frames/` | `gfx/interface/animated/020_black_plague/world_end_readiness_seal/black_plague_rat_king_terminal_readiness_static.dds`; `gfx/interface/animated/020_black_plague/world_end_readiness_seal/black_plague_rat_king_terminal_readiness_sheet.dds` | 64x64 frames; 8 frames; 512x64 sheet; 6 FPS loop | `GFX_black_plague_rat_king_terminal_readiness_static`; `GFX_black_plague_rat_king_terminal_readiness_animated` | `animations/rat_king_world_end_readiness_seal/{manifest.md,gfx_handoff.md}` |

Both packages use independent generated source frames and retain static fallbacks. Runtime registration is promoted in `interface/020_black_plague_rat_identity.gfx`. The crisis seal is mounted on the shared selected-state card and gated by `disease_containment_board_view_state_is_black_plague_crisis`, with the player-facing tooltip `disease_containment.gui.selected.black_plague_crisis_seal.tt`; the terminal-readiness animated sprite is consumed by `black_plague_rat_king_execute_terminal_takeover`, while a separate terminal-readiness scripted-GUI panel remains absent. No bespoke Rat model or additional country tag is part of either package.

## Rat Nations news strip (2026-08-02)

| Asset | Intended use | Source / processed package | Runtime DDS | Size | Sprite / consumer |
| --- | --- | --- | --- | --- | --- |
| `news_event_020_rat_nations` | Public news report when organized broods take the surface | `source_png/news_event_020_rat_nations_imagegen_source.png`; `processed_png/news_event_020_rat_nations.png`; `contact_sheets/news_event_020_rat_nations_contact_sheet.png` | `gfx/event_pictures/020_black_plague/news_event_020_rat_nations.dds` | 397x153, black and white | `GFX_news_event_020_rat_nations` / `chaosx.nr20.41` in `events/020_black_death.txt` |

The strip is generated fictional period-news imagery with no readable text or modern objects. Runtime registration is in `interface/020_black_plague_event_pictures.gfx`; it replaces the report-card consumer on the public organized-rat news event without changing the event id or log contract.
