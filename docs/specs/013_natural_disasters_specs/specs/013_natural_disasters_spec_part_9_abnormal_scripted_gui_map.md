# Event 013 Natural Disasters, Part 9, abnormal disaster scripted GUI map

This file plans the custom scripted GUI surface for Evolution III abnormal disasters. It is a design handoff, not final GUI code. Working sprite names are stable handoff names, not final localisation.

The normal aftermath category should stay readable without this map. The abnormal map appears only when the player needs to understand moving, multi-state, delayed, or global-path disasters. The GUI must never become a generic disaster announcer. It shows the physical path, current danger, recent impact cards, and recovery priorities.

## Entry flow

| Entry point | When visible | Purpose |
| --- | --- | --- |
| Aftermath category button | A country has at least one active abnormal disaster card or a severe delayed chain in its states. | Lets the affected player choose recovery and warning priorities. |
| Event Details abnormal tab | Event 013 has reached Evolution III and at least one abnormal season exists in history. | Lets the player review the current abnormal system without exposing hidden formulas. |
| Disaster Barrage confirmation follow-up | Manual scenario launched Maximum intensity and abnormal access is active. High intensity may open severe chained recovery without the abnormal map. | Shows the player what the scenario has started and what can be prioritized. |

The player should receive a visible notification when the map first becomes relevant. The notification should identify the affected disaster family and the most threatened place by direction, not through final copy.

## Window layout

Recommended target window size is a wide HOI4-style panel that can sit over the map without hiding all state context. Exact coordinates belong to implementation after inspecting the live interface.

| Region | Content | Interaction |
| --- | --- | --- |
| Header strip | Event 013 working label, active abnormal family icon, season date, severity band, close button. | Close only. Header text remains direction-only until localisation. |
| Left hazard stack | Up to five active abnormal cards, ordered by next impact or unresolved severity. | Selecting a card focuses the map layer and details panel. |
| Central map plate | Abstract region map, path lines, affected state markers, next-hit markers, chain origin markers. | Hover markers show state name, family, time to impact, and recovery state. |
| Right detail panel | Selected card details, affected states, next-hit queue, current warning choices, recovery summary. | Buttons open normal decisions or focus camera. They do not bypass decision costs. |
| Bottom timeline | Impact pulses, delayed report pulses, chain checks, super-event marker, recovery reassessment ticks. | Hover shows direction for what happened or what is pending. |
| Legend rail | Icons for impact, warning, report, aftermath, chain risk, closed state, foreign relief, blocked action. | Passive reference. |

## Card states

| Card state | Meaning | Visual direction | Gameplay interaction |
| --- | --- | --- | --- |
| `dormant_monitoring` | Abnormal system exists but no player-owned or observed state is currently threatened. | Dim card, static map marker. | Review only. |
| `warning_window` | A known state or path segment can still be prepared for. | Soft warning border and countdown. | Warning decisions available if requirements are met. |
| `impact_pending` | Impact is scheduled and preparation window is nearly closed. | Stronger pulse, marker on map. | Last chance choices, expensive emergency actions. |
| `impact_resolved` | Damage has landed and report delivery is pending or complete. | Impact stamp and damaged marker. | Opens rescue and stabilization actions. |
| `chain_risk_active` | Follow-up risk exists, such as tsunami, aftershock, lahar, disease, fire, or famine. | Secondary icon orbit around card or marker. | Prevention missions available if time remains. |
| `recovery_active` | The country is working through aftermath decisions and missions. | Repair progress strip. | Recovery decisions and mission summary. |
| `closed` | Disaster card no longer needs player action. | Muted check mark state. | Can be archived from current list. |
| `failed_recovery` | Recovery deadline failed or partial success created lasting damage. | Damaged frame and lingering modifier icon. | Shows follow-up consequences and remaining late recovery. |

## Abnormal map layers

| Layer | Families using it | What it shows | Static fallback |
| --- | --- | --- | --- |
| `rupture_wave_layer` | whole-earth rupture wave | Regional seismic rings, aftershock clusters, delayed coast risks. | Static ring markers and numbered region cards. |
| `meteor_path_layer` | meteor impact, meteor shower | Predicted impact cluster, confirmed craters, fragment spread. | Static crater icons and next-impact list. |
| `eruption_plume_layer` | massive eruption, volcanic eruption, ashfall | Vent region, ash plume direction, lahar valleys, possible coastal collapse. | Static ash cone and downwind arrows. |
| `tsunami_train_layer` | tsunami, ocean impact chain, volcanic collapse | Coast origin, arrival order, port risk, evacuation priority. | Static coast markers with arrival order. |
| `storm_corridor_layer` | moving storm corridor, tornado outbreak | Moving path, next-hit queue, segment history, chain branches. | Static path line with numbered state cards. |

Only one primary layer should be active at a time. Secondary chain risks can appear as small overlays on the selected layer.

## Target sprite names

These names are stable handoff targets for asset and GUI work. The main implementation can adjust file paths after inspecting repo conventions, but should not rename them without updating every handoff.

| Sprite name | Type | Target size direction | Use | Static fallback |
| --- | --- | --- | --- | --- |
| `GFX_013_abnormal_disaster_panel` | static panel | wide custom GUI panel | Main background plate. | Same sprite. |
| `GFX_013_abnormal_disaster_panel_damaged` | static panel variant | same as panel | Severe or failed-recovery variant. | Same sprite. |
| `GFX_013_disaster_card_frame` | static UI frame | card sized | Normal card frame. | Same sprite. |
| `GFX_013_disaster_card_frame_warning_animated` | frameAnimatedSpriteType | card frame sheet | Warning window pulse. | `GFX_013_disaster_card_frame_warning_static` |
| `GFX_013_disaster_card_frame_impact_animated` | frameAnimatedSpriteType | card frame sheet | Impact pending or just hit. | `GFX_013_disaster_card_frame_impact_static` |
| `GFX_013_map_marker_impact` | icon | small marker | Confirmed impact state. | Same sprite. |
| `GFX_013_map_marker_next_hit_animated` | frameAnimatedSpriteType | small marker sheet | Next-hit state marker. | `GFX_013_map_marker_next_hit_static` |
| `GFX_013_map_marker_chain_risk` | icon | small marker | Follow-up chain risk. | Same sprite. |
| `GFX_013_rupture_wave_sheet` | frame sheet sprite | map overlay sheet | Seismic ring pulse. | `GFX_013_rupture_wave_static` |
| `GFX_013_meteor_fall_sheet` | frame sheet sprite | map overlay sheet | Meteor shower cluster. | `GFX_013_meteor_fall_static` |
| `GFX_013_eruption_plume_sheet` | frame sheet sprite | map overlay sheet | Volcanic plume motion. | `GFX_013_eruption_plume_static` |
| `GFX_013_tsunami_train_sheet` | frame sheet sprite | map overlay sheet | Coast wave arrival pulse. | `GFX_013_tsunami_train_static` |
| `GFX_013_storm_corridor_sheet` | frame sheet sprite | map overlay sheet | Moving storm path. | `GFX_013_storm_corridor_static` |
| `GFX_013_foreign_relief_badge` | icon | small badge | Relief active or pledged. | Same sprite. |
| `GFX_013_recovery_progress_frame` | UI frame | meter frame | Recovery progress strip. | Same sprite. |
| `GFX_013_recovery_progress_fill` | UI fill | meter fill | Recovery progress fill. | Same sprite. |

## Animation briefs

All final animations must use real per-frame source art and a horizontal frame sheet. Transform-only previews are not final assets.

| Animated asset | Frame plan | Loop and timing direction | Visual state | Static fallback |
| --- | --- | --- | --- | --- |
| Warning card frame | 8 frames showing a drawn warning rim growing, peaking, and settling. | 8 to 12 fps, looping, play on show. | Preparation window open. | Warning static frame. |
| Impact card frame | 10 frames showing a stronger impact flash and damaged border. | 10 to 12 fps, looping until impact resolves. | Impact pending or immediate aftermath. | Impact static frame. |
| Next-hit marker | 8 frames with marker pressure rising in place. | 8 fps, looping. | Selected next state. | Next-hit static marker. |
| Rupture wave | 12 frames with uneven seismic rings expanding across the plate. | 8 fps, looping or one-shot on refresh. | Whole-earth rupture active. | Static ring overlay. |
| Meteor fall | 12 frames with separate falling fragments and small ground flashes. | 10 fps, looping for shower, one-shot for impact. | Meteor shower or impact cluster. | Static crater cluster. |
| Eruption plume | 12 frames with ash plume growth and downwind drift drawn per frame. | 8 fps, looping slowly. | Active eruption or ashfall chain. | Static plume. |
| Tsunami train | 10 frames with coastward wave pulses and arrival markers. | 8 fps, looping while wave arrival is pending. | Delayed tsunami chain. | Static coast wave markers. |
| Storm corridor | 14 frames with a drawn storm core moving along a path, plus path flicker. | 10 fps, looping while corridor advances. | Moving storm or tornado corridor. | Static path line. |

## Player interaction flow

1. Player receives a visible aftermath or abnormal notification.
2. Player opens the aftermath category.
3. If abnormal map is available, a button opens the map with the most urgent card selected.
4. Player reviews central map and next-hit queue.
5. Player selects a card or state marker.
6. Detail panel shows card fields, active risks, warning choices, and recovery actions.
7. Buttons route to normal decisions or mission details. GUI buttons must not duplicate or bypass cost logic.
8. When an impact lands, the card changes to impact resolved and the delayed country report remains reliable.
9. Recovery missions update the card state and timeline.
10. Closed cards move to archive view and stop pulsing.

## AI equivalent

| GUI concept | AI equivalent |
| --- | --- |
| Selected card | Highest score active card in country scope. |
| Next-hit queue | Scripted priority list from impact date, population, capital, supply, port, and war pressure. |
| Warning button | AI decision with same requirements and cost model. |
| Recovery progress | Recovery score variable that controls cleanup and late modifiers. |
| Chain risk badge | AI risk score for spending on prevention before repair. |

## Static fallback rule

Every animated surface needs a static fallback. If animations are disabled, missing, unsupported, or blocked by asset work, the map must still communicate the active disaster, next affected states, report status, and recovery state through static sprites and text fields. A static fallback is not a gameplay simplification. It is required accessibility and engine safety.

## Accepted implementation clarifications, 2026-07-11

The live route view is sequence-scoped and contains up to five selectable markers in segment order. Each copied marker row carries its state scope, sequence and segment, family and origin, origin medium, basin or motion domain, schedule and impact state, fine route, linked target and due date, report date, recovery phase, reassessment, result, and archive status. Another sequence cannot enter that view, and each observer rebuilds independent country arrays.

All five physical layers are authored against one normalized five-anchor layout. The family-specific frame sheet supplies the route shape, while the selected segment's state, strategic region, date, warning state, and next-hit status give each anchor its physical meaning. Static mode uses the same markers and coordinates.

The bottom timeline has six selectable state-driven milestones: warning, schedule, impact, report, follow-up, and reassessment. A milestone is visible only when its fact exists and changes the scoped detail text rather than applying gameplay.

The return control stores the selected state, closes the GUI, and routes a controlled live record back to the ordinary warning, recovery, relief, or chain decisions. Archived and foreign records remain read-only. No warning or recovery effect is duplicated in scripted GUI code.

The implemented header uses the existing mapped family category pictures as a compact active-family icon, and adds the selected severity band and scheduled impact date beside the sequence summary. A dormant monitor keeps the header readable without inventing a family when no record is selected.

The implemented legend consumes eight passive icon and label pairs for impact, warning, report, aftermath, chain risk, closed state, foreign relief, and blocked action. The foreign-relief badge is therefore a live direct-window consumer as well as a registered recovery asset.

Manual Disaster Barrage abnormal map access is Maximum-only. High intensity can create severe chained disasters and recovery pressure, but does not imply access to the Evolution III abnormal path map.

The Event Details abnormal entry intentionally becomes a dormant read-only monitor once Evolution III has been logged. It can show the abnormal surface before a currently active record exists, while active records still drive the selected header, markers, and recovery details.
