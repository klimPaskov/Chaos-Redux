# Event 011 Secret Alliance asset register

This register covers every visible asset family planned for the event. Filenames and sprite names are proposals until implementation registers them. All generated art must follow the project asset and frame-animation skills. Real historical people, flags, and attested symbols are not required by this event.

## Visual language

The event should use period intelligence, covert travel, damaged infrastructure, intercepted correspondence, guarded industrial spaces, border reconnaissance, and tightly framed coalition imagery. It should avoid generic maps as the main subject, readable generated documents, modern surveillance technology, modern tactical clothing, neon cyber imagery, and abstract conspiracy-board clichés.

The visual identity uses three recurring motifs:

- **Knotted lines** for concealed coordination and competing motives
- **Broken seals** for exposure, defection, and compromised secrecy
- **Converging arrows or shadows** for the reveal and coalition war

## Event picture assets

| Asset key | Type | Target size | Source mode | Visual direction | Intended use | Proposed final path | Proposed sprite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| report_first_pattern | Report event image | 210x176 | Generated period-documentary | A 1936 to 1945 railway or factory office where several damaged dispatches and duplicated route slips are being compared, no readable text, people and physical evidence remain central | First noticeable pattern incident | gfx/event_pictures/011_secret_alliance/report_event_first_pattern.dds | GFX_report_event_011_secret_alliance_first_pattern |
| report_missing_courier | Report event image | 210x176 | Generated period-documentary | An abandoned period motorcar or bicycle beside a rural border road, open satchel, guarded search party, no body-centered sensationalism | Courier disappearance and route investigation | gfx/event_pictures/011_secret_alliance/report_event_missing_courier.dds | GFX_report_event_011_secret_alliance_missing_courier |
| report_machine_sabotage | Report event image | 210x176 | Generated period-documentary | Engineers inspecting deliberately damaged machine tools in a wartime plant, close physical detail, no modern safety equipment | Industrial sabotage | gfx/event_pictures/011_secret_alliance/report_event_machine_sabotage.dds | GFX_report_event_011_secret_alliance_machine_sabotage |
| report_safehouse_raid | Report event image | 210x176 | Generated period-documentary | Police or intelligence officers entering a sparse rented room with radios, travel cases, and concealed compartments, no readable papers | Successful safehouse or courier mission | gfx/event_pictures/011_secret_alliance/report_event_safehouse_raid.dds | GFX_report_event_011_secret_alliance_safehouse_raid |
| report_border_survey | Report event image | 210x176 | Generated period-documentary | Civilian-looking surveyors near a bridge or mountain pass observed by concealed border guards | Military preparation clue | gfx/event_pictures/011_secret_alliance/report_event_border_survey.dds | GFX_report_event_011_secret_alliance_border_survey |
| report_political_attack | Report event image | 210x176 | Generated period-documentary | Guarded government steps, damaged official vehicle, scattered crowd, severe and restrained treatment | Evolution II attempted killing or threat | gfx/event_pictures/011_secret_alliance/report_event_political_attack.dds | GFX_report_event_011_secret_alliance_political_attack |
| report_turned_channel | Report event image | 210x176 | Generated period-documentary | A tense night meeting between an envoy and intelligence handlers in period dress, faces partly obscured by composition rather than artificial blur | Turned member or controlled channel | gfx/event_pictures/011_secret_alliance/report_event_turned_channel.dds | GFX_report_event_011_secret_alliance_turned_channel |

Every report image receives the required local report-card treatment after generation and before DDS conversion.

## News and super-event assets

| Asset key | Type | Target size | Source mode | Visual direction | Intended use | Proposed final path | Proposed sprite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| news_public_coalition | News image | 397x153, black and white | Generated period-news | Delegates from several visibly different states standing beneath a shared unlettered emblem while military staff gather behind them, staged as a period press photograph | Public faction formation news event | gfx/event_pictures/011_secret_alliance/news_event_public_coalition.dds | GFX_news_event_011_secret_alliance_public_coalition |
| super_event_reveal | Super-event image | 457x328 | Generated alternate-history documentary scene | A dark formal hall with several delegations and military representatives converging around one table, a single broken seal or folded target map as a secondary prop, strong central composition, no readable flags or text, period clothing and lighting | Reveal super-event | gfx/super_events/011_secret_alliance/super_event_public_reveal.dds | GFX_super_event_011_secret_alliance_public_reveal |

The super-event image should communicate public commitment after long concealment. It should not show an anonymous globe, a pile of dossiers, a flat map with arrows, or a generic handshake.

## Decision category and mechanic UI assets

| Asset key | Type | Target size | Source mode | Visual direction | State coverage | Proposed final path | Proposed sprite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category_foreign_interference | Decision category icon | Match verified project category pattern | Generated icon | Three narrow cords tied behind a cracked national seal, period intelligence aesthetic | Base | gfx/interface/decisions/011_secret_alliance/decision_category_foreign_interference.dds | GFX_decision_category_011_secret_alliance_foreign_interference |
| category_coalition_crisis | Decision category icon | Match verified project category pattern | Generated icon | The same seal openly encircled by several points or blades, designed separately from the baseline category icon | Evolution III and reveal | gfx/interface/decisions/011_secret_alliance/decision_category_coalition_crisis.dds | GFX_decision_category_011_secret_alliance_coalition_crisis |
| panel_counter_network | Scripted GUI panel | Size from final GUI layout | Generated UI art | Subdued paper, metal, and fabric textures with space for two meters and three suspect cards, no embedded text | Static background | gfx/interface/011_secret_alliance/counter_network_panel.dds | GFX_011_secret_alliance_counter_network_panel |
| meter_evidence_frame | Meter frame | Size from final GUI layout | Generated UI art | Broken-seal and lens motif, high readability | Empty frame | gfx/interface/011_secret_alliance/evidence_meter_frame.dds | GFX_011_secret_alliance_evidence_meter_frame |
| meter_evidence_fill | Meter fill | Size from final GUI layout | Deterministic UI processing from approved art | Increasing linked marks, no numeric text | Fill states | gfx/interface/011_secret_alliance/evidence_meter_fill.dds | GFX_011_secret_alliance_evidence_meter_fill |
| meter_preparedness_frame | Meter frame | Size from final GUI layout | Generated UI art | Fortification and dispatch motif | Empty frame | gfx/interface/011_secret_alliance/preparedness_meter_frame.dds | GFX_011_secret_alliance_preparedness_meter_frame |
| meter_preparedness_fill | Meter fill | Size from final GUI layout | Deterministic UI processing from approved art | Increasing reinforced segments | Fill states | gfx/interface/011_secret_alliance/preparedness_meter_fill.dds | GFX_011_secret_alliance_preparedness_meter_fill |
| suspect_card | Target card frame | Size from final GUI layout | Generated UI art | Period index-card frame with a confidence tab and flag area, no generated writing | Unknown, possible, likely, confirmed | gfx/interface/011_secret_alliance/suspect_card_states.dds | GFX_011_secret_alliance_suspect_card_states |
| status_recent_operation | Status icon | 32x32 or verified GUI size | Generated icon | A cut wire crossing a sealed envelope | Base | gfx/interface/011_secret_alliance/status_recent_operation.dds | GFX_011_secret_alliance_status_recent_operation |
| status_turned_channel | Status icon | 32x32 or verified GUI size | Generated icon | Reversed arrow through a broken seal | Base | gfx/interface/011_secret_alliance/status_turned_channel.dds | GFX_011_secret_alliance_status_turned_channel |
| status_false_lead | Status icon | 32x32 or verified GUI size | Generated icon | Two diverging tracks beneath a blurred stamp shape, no text | Base | gfx/interface/011_secret_alliance/status_false_lead.dds | GFX_011_secret_alliance_status_false_lead |
| status_war_pressure | Warning icon | 32x32 or verified GUI size | Generated icon | Converging bayonet or arrow silhouettes around a central border marker | Base | gfx/interface/011_secret_alliance/status_war_pressure.dds | GFX_011_secret_alliance_status_war_pressure |

## Animated state asset

Only one animated family is recommended. Motion should signal the transition into Evolution III and the approach of open coalition war.

| Field | Requirement |
| --- | --- |
| Working asset name | coalition_closure_warning |
| In-game use | Animated border or seal in the counter-network panel when the public coalition threshold is active |
| Target frame size | Determine from verified GUI layout, recommended range 96x96 to 160x96 |
| Frame count target | 8 real source frames |
| Loop | Slow continuous loop, 6 to 8 fps, no rapid flashing |
| Motion concept | Separate source frames show several cords, shadows, or metal arms closing inward around a central broken seal, then easing back slightly without fully reopening |
| State meaning | Evolution III active and offensive countdown running |
| Static fallback | Fully closed but readable coalition warning state |
| Source mode | Generated frame-by-frame art through the official image generation workflow |
| Final sheet | Horizontal frame sheet, width equals frame width multiplied by 8 |
| Proposed static sprite | GFX_011_secret_alliance_coalition_closure_warning |
| Proposed animated sprite | GFX_011_secret_alliance_coalition_closure_warning_animated |
| Proposed paths | gfx/interface/011_secret_alliance/coalition_closure_warning_static.dds and gfx/interface/011_secret_alliance/coalition_closure_warning_sheet.dds |
| Target GFX | interface/011_secret_alliance.gfx, proposed |
| Target GUI | Event-owned counter-network scripted GUI |
| Avoid | Transform-only motion, opacity pulse, simple glow, rotating one still image, map arrows, flashing red screen |

The asset package must include a brief, frame plan, one source PNG per frame, processed frames, sheet PNG, sheet DDS, static PNG and DDS, preview GIF, contact sheet, manifest, and GFX handoff.

## Decision icons

Each icon requires its own 32x32 source composition. None may be a resized focus or idea icon.

| Icon key | Visual motif | Decision family | Proposed final path | Proposed sprite |
| --- | --- | --- | --- | --- |
| decision_compare_traffic | Overlapping travel routes and a magnifying lens | Investigation | gfx/interface/decisions/011_secret_alliance/decision_compare_traffic.dds | GFX_decision_011_secret_alliance_compare_traffic |
| decision_trace_courier | Courier satchel and route marker | Counterintelligence | gfx/interface/decisions/011_secret_alliance/decision_trace_courier.dds | GFX_decision_011_secret_alliance_trace_courier |
| decision_compare_sabotage | Broken gear with matching tool marks | Investigation | gfx/interface/decisions/011_secret_alliance/decision_compare_sabotage.dds | GFX_decision_011_secret_alliance_compare_sabotage |
| decision_compartmentalize | Locked cabinet divided into sections | Protection | gfx/interface/decisions/011_secret_alliance/decision_compartmentalize.dds | GFX_decision_011_secret_alliance_compartmentalize |
| decision_secure_industry | Guarded machine tool | Protection | gfx/interface/decisions/011_secret_alliance/decision_secure_industry.dds | GFX_decision_011_secret_alliance_secure_industry |
| decision_harden_border | Field telephone and fortified crossing | Protection | gfx/interface/decisions/011_secret_alliance/decision_harden_border.dds | GFX_decision_011_secret_alliance_harden_border |
| decision_quiet_approach | Two chairs separated by a shaded screen | Diplomacy | gfx/interface/decisions/011_secret_alliance/decision_quiet_approach.dds | GFX_decision_011_secret_alliance_quiet_approach |
| decision_security_guarantee | Shield extended toward a smaller seal | Diplomacy | gfx/interface/decisions/011_secret_alliance/decision_security_guarantee.dds | GFX_decision_011_secret_alliance_security_guarantee |
| decision_feed_false_plans | Reversed map arrow entering an envelope | Deception | gfx/interface/decisions/011_secret_alliance/decision_feed_false_plans.dds | GFX_decision_011_secret_alliance_feed_false_plans |
| decision_turn_member | Broken chain link reversing direction | Offensive counter-network | gfx/interface/decisions/011_secret_alliance/decision_turn_member.dds | GFX_decision_011_secret_alliance_turn_member |
| decision_disrupt_conference | Empty conference chairs and a seized briefcase | Offensive counter-network | gfx/interface/decisions/011_secret_alliance/decision_disrupt_conference.dds | GFX_decision_011_secret_alliance_disrupt_conference |
| decision_border_intercept | Patrol silhouettes at a bridge | Border action | gfx/interface/decisions/011_secret_alliance/decision_border_intercept.dds | GFX_decision_011_secret_alliance_border_intercept |
| decision_release_dossier | Broken seal over stacked evidence cards | Public exposure | gfx/interface/decisions/011_secret_alliance/decision_release_dossier.dds | GFX_decision_011_secret_alliance_release_dossier |
| decision_emergency_mobilization | Mobilization notice motif without text and a raised barrier | Evolution III emergency | gfx/interface/decisions/011_secret_alliance/decision_emergency_mobilization.dds | GFX_decision_011_secret_alliance_emergency_mobilization |
| decision_preempt_coalition | Sword cutting converging cords | Evolution III emergency | gfx/interface/decisions/011_secret_alliance/decision_preempt_coalition.dds | GFX_decision_011_secret_alliance_preempt_coalition |
| decision_offer_separate_terms | Open chain link and negotiating table | Revealed war | gfx/interface/decisions/011_secret_alliance/decision_offer_separate_terms.dds | GFX_decision_011_secret_alliance_offer_separate_terms |
| decision_strike_depots | Forward crates and damaged rail spur | Revealed war | gfx/interface/decisions/011_secret_alliance/decision_strike_depots.dds | GFX_decision_011_secret_alliance_strike_depots |

## Idea and national spirit icons

These 64x64 assets must be designed as idea icons, not focus icons.

| Idea key | Lifecycle role | Visual direction | Proposed final path | Proposed sprite |
| --- | --- | --- | --- | --- |
| idea_unexplained_interference | Early mixed pressure | A sealed dispatch crossed by faint broken lines | gfx/interface/ideas/011_secret_alliance/idea_unexplained_interference.dds | GFX_idea_011_secret_alliance_unexplained_interference |
| idea_compromised_channels | Penetration penalty | Open cipher box and copied key material | gfx/interface/ideas/011_secret_alliance/idea_compromised_channels.dds | GFX_idea_011_secret_alliance_compromised_channels |
| idea_hardened_networks | Preparedness benefit | Reinforced communication hub and guarded cables | gfx/interface/ideas/011_secret_alliance/idea_hardened_networks.dds | GFX_idea_011_secret_alliance_hardened_networks |
| idea_public_coalition_pressure | Evolution III pressure | Several dark seals pressing toward one center | gfx/interface/ideas/011_secret_alliance/idea_public_coalition_pressure.dds | GFX_idea_011_secret_alliance_public_coalition_pressure |
| idea_known_enemy_plans | Reveal benefit from Evidence | Marked route board with exposed arrows, no readable labels | gfx/interface/ideas/011_secret_alliance/idea_known_enemy_plans.dds | GFX_idea_011_secret_alliance_known_enemy_plans |
| idea_coalition_opening_coordination | Coalition readiness conversion | Linked staff batons over converging routes | gfx/interface/ideas/011_secret_alliance/idea_coalition_opening_coordination.dds | GFX_idea_011_secret_alliance_coalition_opening_coordination |
| idea_fractured_coalition | Low Resolve penalty | Cracked ring of mismatched seals | gfx/interface/ideas/011_secret_alliance/idea_fractured_coalition.dds | GFX_idea_011_secret_alliance_fractured_coalition |

## Faction emblem

| Asset key | Type | Target size | Source mode | Direction | Proposed path | Proposed sprite |
| --- | --- | --- | --- | --- | --- | --- |
| faction_anti_target_pact | Faction emblem or UI seal | Verify existing faction-emblem pattern | Generated fictional emblem | An enclosing ring made from three or more interlocked angular elements around an empty center, strong at small size, no fixed national symbol so it works against any target | gfx/interface/011_secret_alliance/faction_anti_target_pact_emblem.dds | GFX_011_secret_alliance_faction_emblem |

The emblem must not use a real extremist symbol or copy any participant's flag. It is a procedural coalition identity.

## Achievement icons

| Achievement key | Completed icon direction | Variants | Proposed final paths |
| --- | --- | --- | --- |
| 011_secret_alliance_the_empty_chair | An empty conference chair beneath a broken pact seal | Completed, grey, not eligible | gfx/achievements/011_secret_alliance_the_empty_chair.dds and required variants |
| 011_secret_alliance_every_thread | A hand holding several connected cords without breaking them | Completed, grey, not eligible | gfx/achievements/011_secret_alliance_every_thread.dds and required variants |
| 011_secret_alliance_their_man_in_the_room | A reversed seal hidden among matching seals | Completed, grey, not eligible | gfx/achievements/011_secret_alliance_their_man_in_the_room.dds and required variants |
| 011_secret_alliance_divide_the_table | A conference table split into separate sections | Completed, grey, not eligible | gfx/achievements/011_secret_alliance_divide_the_table.dds and required variants |
| 011_secret_alliance_surrounded_not_buried | A central shield holding against a full ring | Completed, grey, not eligible | gfx/achievements/011_secret_alliance_surrounded_not_buried.dds and required variants |
| 011_secret_alliance_two_giants_one_grave | Two large broken seals outside a surviving central emblem | Completed, grey, not eligible | gfx/achievements/011_secret_alliance_two_giants_one_grave.dds and required variants |

Achievement filenames must exactly match final registered IDs. The not-eligible variant must use the repository overlay workflow.

## Assets intentionally excluded

- No new country flags, because the event uses existing countries and does not transform their public identities.
- No leader portraits, because the event does not create leaders or countries.
- No focus icons, because dedicated focus trees would add scope without improving the event-owned loop.
- No generated readable dossiers or newspaper headlines.
- No map-only event art.
- No animation for every meter or button. The single Evolution III warning loop carries the important state change.

## Required package structure for asset production

```text
docs/assets/011_secret_alliance/
  manifest.md
  prompts/
  source_png/
  processed_png/
  contact_sheets/
  animations/coalition_closure_warning/
  gfx_handoff.md
```

Final DDS files belong in the event-scoped game folders listed above. They must not remain only under documentation.

## Asset acceptance gates

- Every listed visible asset is complete, blocked, or marked for user review.
- Generated icon types have separate source artwork appropriate to their size and UI role.
- Report images use the project report-card processing workflow.
- News art is black and white.
- Super-event art is 457x328 and remains legible behind the super-event interface.
- Transparent icons have real transparency and no square matte.
- Animation uses eight real source frames and a horizontal sheet, with a static fallback.
- Every DDS has exact dimensions and a manifest entry.
- The GFX handoff gives final paths and stable sprite names.
- No historical symbol or real-person likeness is fabricated.
