# Asset Prompt: Event 011 Secret Alliance

Use `chaos-redux-event-assets` and `chaos-redux-frame-animation` for animated pieces. Inspect the matching reference folders before creating assets.

## Required asset families

| Asset | Type | Target size | Source mode | Suggested filename | Suggested sprite | Reference folder |
| --- | --- | --- | --- | --- | --- | --- |
| Hidden compact seal | Decision category icon | Match category pattern | Generated icon | `decision_category_secret_alliance` | `GFX_decision_category_secret_alliance` | assets/decisions |
| Investigation icon | Decision icon | 32x32 | Generated icon | `decision_secret_alliance_investigate` | `GFX_decision_secret_alliance_investigate` | assets/decisions |
| Security icon | Decision icon | 32x32 | Generated icon | `decision_secret_alliance_security` | `GFX_decision_secret_alliance_security` | assets/decisions |
| Diplomacy split icon | Decision icon | 32x32 | Generated icon | `decision_secret_alliance_split` | `GFX_decision_secret_alliance_split` | assets/decisions |
| Border watch icon | Decision icon | 32x32 | Generated icon | `decision_secret_alliance_border_watch` | `GFX_decision_secret_alliance_border_watch` | assets/decisions |
| Public confrontation icon | Decision icon | 32x32 | Generated icon | `decision_secret_alliance_confront` | `GFX_decision_secret_alliance_confront` | assets/decisions |
| Unexplained friction | Idea icon | 64x64 | Generated icon | `idea_secret_alliance_friction` | `GFX_idea_secret_alliance_friction` | assets/ideas |
| Counter-pact bureau | Idea icon | 64x64 | Generated icon | `idea_secret_alliance_bureau` | `GFX_idea_secret_alliance_bureau` | assets/ideas |
| Prepared security network | Idea icon | 64x64 | Generated icon | `idea_secret_alliance_prepared_network` | `GFX_idea_secret_alliance_prepared_network` | assets/ideas |
| Exposed pact government | Idea icon | 64x64 | Generated icon | `idea_secret_alliance_exposed_member` | `GFX_idea_secret_alliance_exposed_member` | assets/ideas |
| Patron shield | Idea icon | 64x64 | Generated icon | `idea_secret_alliance_patron_shield` | `GFX_idea_secret_alliance_patron_shield` | assets/ideas |
| Early courier report | Report event image | 210x176 | Generated period documentary or sourced if suitable | `report_event_011_secret_alliance_courier` | `GFX_report_event_011_secret_alliance_courier` | assets/report_event_images |
| Sabotage aftermath report | Report event image | 210x176 | Generated period documentary | `report_event_011_secret_alliance_sabotage` | `GFX_report_event_011_secret_alliance_sabotage` | assets/report_event_images |
| Defector trail report | Report event image | 210x176 | Generated period documentary | `report_event_011_secret_alliance_defector` | `GFX_report_event_011_secret_alliance_defector` | assets/report_event_images |
| Pact reveal news image | News event image | 397x153 | Generated period news | `news_event_011_secret_alliance_reveal` | `GFX_news_event_011_secret_alliance_reveal` | assets/news_event_images |
| Revealed pact emblem | Faction emblem or GUI seal | Match implementation surface | Generated fictional emblem | `secret_alliance_pact_emblem` | `GFX_secret_alliance_pact_emblem` | closest decisions or UI examples |
| Counter-pact board background | Scripted GUI panel | Implementation-defined | Generated UI art and deterministic layout | `secret_alliance_board_bg` | `GFX_secret_alliance_board_bg` | closest GUI examples |
| Suspect card frames | Scripted GUI cards | Implementation-defined | Generated UI elements | `secret_alliance_suspect_card_*` | `GFX_secret_alliance_suspect_card_*` | closest GUI examples |
| Evidence meter frame and fill | Scripted GUI meter | Implementation-defined | Generated UI elements | `secret_alliance_evidence_meter_*` | `GFX_secret_alliance_evidence_meter_*` | closest GUI examples |
| Crisis warning frame | Animated GUI frame | Implementation-defined | Generated frame sequence | `secret_alliance_crisis_frame_*` | `GFX_secret_alliance_crisis_frame_animated` | frame-animation skill |

## Animation briefs

### Animated hidden compact seal

- In-game use: category header or board seal when suspicion is high.
- Target size: match category or GUI surface.
- Frame count: 8 to 12 real source frames.
- Loop: slow pulse, subtle and readable.
- Static fallback: `GFX_secret_alliance_hidden_seal`.
- Animated sprite: `GFX_secret_alliance_hidden_seal_animated`.
- Source mode: generated frame sequence.
- Visual direction: shadowed wax seal, coded paper, implied triangular compact, no readable text.

### Evidence meter shimmer

- In-game use: evidence meter feedback after successful investigation.
- Target size: implementation-defined meter overlay.
- Frame count: 6 to 8 real source frames.
- Loop: short shimmer or state-driven display.
- Static fallback: `GFX_secret_alliance_evidence_meter_highlight`.
- Animated sprite: `GFX_secret_alliance_evidence_meter_highlight_animated`.
- Source mode: generated UI frames.

### Crisis warning frame

- In-game use: board warning when war countdown or public crisis is active.
- Target size: implementation-defined board overlay.
- Frame count: 8 to 12 real source frames.
- Loop: slow warning pulse.
- Static fallback: `GFX_secret_alliance_crisis_frame`.
- Animated sprite: `GFX_secret_alliance_crisis_frame_animated`.
- Source mode: generated UI frames.

## Style rules

Use strong silhouettes, muted period tones, coded diplomacy, broken seals, couriers, hidden ledgers, and industrial shadows. Do not use readable generated text. Do not make maps the main visual subject unless a specific GUI element requires a strategic board. Report images must receive the report-event card treatment. News images must be black and white.

## Manifest requirement

Create `docs/assets/011_secret_alliance/manifest.md` and `docs/assets/011_secret_alliance/gfx_handoff.md`. Record source mode, prompt, source paths, processed paths, final DDS paths, sprite names, target sizes, animation frame counts, static fallbacks, and uncertainty.
