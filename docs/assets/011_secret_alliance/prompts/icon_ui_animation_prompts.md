# Event 011 Icon, UI, Achievement, and Animation Prompts

All source art in this tranche used the built-in `$imagegen` workflow. Distinct assets were generated with distinct tool calls. Transparent UI and icon sources used a flat `#00ff00` chroma-key background and the official local removal helper; completed achievement art and the full panel used opaque full-canvas sources.

## Shared transparent icon prompt

The decision-category, decision, status, idea, faction-emblem, meter, suspect-card, and animation prompts used this shared constraint block plus the per-asset subject delta in the tables below:

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV game UI icon or scripted-GUI art at the registered target size
Style/medium: hand-painted 1930s intelligence or military-administration art, aged HOI4 painterly texture, strong dark silhouette, target-size readability
Composition/framing: one centered individually composed subject with generous padding; straight-on for frames and cards
Scene/backdrop: perfectly flat solid #00ff00 chroma-key background for local background removal
Constraints: background is one uniform #00ff00 with no shadow, gradient, floor, reflection, or texture; do not use green in the subject; crisp separated edges; no cast shadow; no white or sticker outline; no opaque square; no fake checkerboard; no text, letters, numbers, flags, logos, watermark, modern technology, neon cyber imagery, or extremist symbols
```

## Category, panel, meter, suspect, and status sources

| Selected source | Prompt delta | Built-in result |
| --- | --- | --- |
| `decision_category_foreign_interference_source.png` | Three narrow dark cords tied behind a cracked bronze-and-burgundy seal; hidden foreign interference; compact 32x32 silhouette. | `exec-8302d333-eecf-4dec-b60f-b2ddef8daed5.png` |
| `decision_category_coalition_crisis_source.png` | Cracked burgundy seal openly encircled by four inward bayonet-like points; public coalition crisis; separately composed 32x32 silhouette. | `exec-4fa030cc-8127-4fd5-b1df-365ff6661057.png` |
| `counter_network_panel_source.png` | Straight-on wide 2:1 counterintelligence workstation panel in walnut, blackened steel, blank dossier paper, and olive fabric; reserve two top meter channels, three equal card spaces, bottom status strip, and button space; no embedded controls or text. | `exec-16ccf546-fe74-45c2-b1d5-7fde04444b20.png` |
| `evidence_meter_frame_source.png` | Long narrow empty frame with cracked wax seal, magnifying-lens clasp, and linked brass witness marks; clear central channel. | `exec-f51c6f76-9522-414e-953a-eb6f9223ef32.png` |
| `evidence_meter_fill_source.png` | Long linked band of brass evidence marks and broken-seal fragments increasing in density left to right; no outer frame. | `exec-a8f3b85d-ef7d-470c-b01b-e2dc830560d4.png` |
| `preparedness_meter_frame_source.png` | Long empty riveted-steel frame with bunker clasp, field-dispatch tabs, and sandbag-like corner texture. | `exec-557c4cd4-48bb-4f10-9c0e-3f356c1c6abb.png` |
| `preparedness_meter_fill_source.png` | Long band of reinforced gunmetal segments and khaki dispatch tabs increasing in structural density left to right. | `exec-237da40a-65e1-42f3-878b-42912746c5c7.png` |
| `suspect_card_unknown_source.png` | Wide period intelligence card with fixed blackened-steel frame, blank paper, left flag aperture, lower-left burgundy tab, top brass clip; unknown state. | `exec-77dec242-ef25-4440-b8a8-5720797c9a10.png` |
| `suspect_card_possible_source.png` | Precise edit of unknown card: preserve frame/camera/layout exactly; add two aged-amber confidence tabs at right and a clipped cord at lower right. | `exec-0fc999a2-8c38-480a-a85f-e972fea9de67.png` |
| `suspect_card_likely_source.png` | Precise edit of unknown card: preserve frame/camera/layout exactly; add three burgundy-and-brass confidence tabs at right and a taut cord at upper right. | `exec-60a4329f-357a-4d1a-a161-03af2328c282.png` |
| `suspect_card_confirmed_source.png` | Precise edit of unknown card: preserve frame/camera/layout exactly; add four locked dark-red confidence tabs and a broken-seal clasp at lower right. | `exec-156f6b2c-6a1d-4fae-b111-31d0a2ae056c.png` |
| `status_recent_operation_source.png` | Cut black signal wire crossing a sealed period envelope. | `exec-67275491-bbe7-4921-9ee3-62c4fa31a47c.png` |
| `status_turned_channel_source.png` | Reversed bronze arrow passing through a broken burgundy seal. | `exec-a57ed920-1b9c-41f5-a8e7-8603c6592c9d.png` |
| `status_false_lead_source.png` | Two diverging railway-like tracks beneath a blank stamp silhouette. | `exec-bc24fe3f-717b-4e8c-896b-0c91f0e2ce98.png` |
| `status_war_pressure_source.png` | Three converging bayonet/arrow silhouettes around a central border marker. | `exec-241e22f2-af07-4b89-9346-7c85d70aae4a.png` |

The first independent possible/likely/confirmed card generations were rejected during contact-sheet QA because their frame geometry drifted. The selected final sources above are the later precise edits of the approved unknown card.

## Decision-icon sources

All decision prompts specified a compact hand-painted 32x32 icon with one strong outlined silhouette and minimal interior detail.

| Asset | Prompt subject | Built-in result |
| --- | --- | --- |
| `decision_compare_traffic` | Overlapping period travel-route ribbons beneath a brass magnifying lens. | `exec-ac84647f-e9ba-4889-ab97-b5ad8a46dad3.png` |
| `decision_trace_courier` | Worn leather courier satchel beside a simple brass route marker. | `exec-7d87b165-0fe0-413b-a27c-b20204d46001.png` |
| `decision_compare_sabotage` | Broken dark-steel gear crossed by two matching tool-mark wedges. | `exec-20c04f1a-02ad-4fcb-8774-1b94787e4124.png` |
| `decision_compartmentalize` | Locked period filing cabinet divided into three reinforced sections. | `exec-b967bc02-e045-479c-9516-9da859bdbe19.png` |
| `decision_secure_industry` | Guarded machine-tool lathe behind a small shield plate. | `exec-2f6ba288-8298-47f9-beb3-74999f58c461.png` |
| `decision_harden_border` | Field telephone beside a reinforced border barrier and watchpost. | `exec-500cc868-b6fa-40fa-8b66-f7befd8c16d6.png` |
| `decision_quiet_approach` | Two period chairs separated by a narrow privacy screen. | `exec-9a544c4f-4db9-4fe9-9a98-1c3815c61669.png` |
| `decision_security_guarantee` | Broad metal shield extending toward a smaller plain wax seal. | `exec-5d6d36db-6b4e-4497-b68c-9ddd0ff512dd.png` |
| `decision_feed_false_plans` | Reversed route arrow entering a sealed period envelope. | `exec-964bdac8-93e6-4173-847a-e1fd80329dcf.png` |
| `decision_turn_member` | Broken chain link with one loose end bent and redirected backward. | `exec-d5bb82d4-f3c8-4c97-ac9d-e6a5d3698a86.png` |
| `decision_disrupt_conference` | Empty conference chairs beside a seized open briefcase. | `exec-9c0aa735-d587-4d70-a117-fca01056d765.png` |
| `decision_border_intercept` | Patrol silhouettes stopping a courier at a steel bridge barrier. | `exec-4a025dbd-410c-40ee-b8c1-3d5cfdb97116.png` |
| `decision_release_dossier` | Broken burgundy seal over three stacked blank evidence cards. | `exec-01cfbc61-0bf5-4650-ae99-2c12110c6590.png` |
| `decision_emergency_mobilization` | Blank folded mobilization notice, raised steel road barrier, helmet silhouette. | `exec-db75ba6c-3c07-4686-a407-51404ec8f8c5.png` |
| `decision_preempt_coalition` | Military sword cutting three converging dark cords. | `exec-b3dde5a1-9672-427c-b28a-4593965b0148.png` |
| `decision_offer_separate_terms` | Open chain link above a negotiating table with two empty chairs. | `exec-40e71793-e9d0-4839-ace4-b544ec33b10b.png` |
| `decision_strike_depots` | Forward supply crates beside a damaged rail spur and broken switch. | `exec-85368662-0807-4067-a520-19ef051c60e7.png` |

## Idea and faction-emblem sources

Idea prompts specified compact 64x64 national-spirit art without a focus frame. The faction emblem was generated as a separate 64x64 UI-seal composition.

| Asset | Prompt subject | Built-in result |
| --- | --- | --- |
| `idea_unexplained_interference` | Sealed dispatch crossed by three faint broken signal lines. | `exec-521997c2-69b7-4262-ab9a-52bb988ce420.png` |
| `idea_compromised_channels` | Open mechanical cipher box with copied brass key blank and duplicated paper key tabs. | `exec-e92b4d90-aa7f-4541-9580-904a6d2799c1.png` |
| `idea_hardened_networks` | Reinforced period communications hub with guarded cable junctions and steel shutters. | `exec-85695b61-755d-4721-9c12-be504dc410e0.png` |
| `idea_public_coalition_pressure` | Four different dark seals physically pressing toward one smaller center seal. | `exec-a2ca0c93-5ff5-42b1-87da-f771a243d09d.png` |
| `idea_known_enemy_plans` | Exposed route board with converging arrows and pinned blank cards. | `exec-2faacd24-e31d-4e8c-985a-d33885865797.png` |
| `idea_coalition_opening_coordination` | Three linked staff batons over converging route ribbons and a command compass. | `exec-dbdff06c-633e-4970-8ed9-01609f1c1c53.png` |
| `idea_fractured_coalition` | Cracked circular ring assembled from mismatched plain wax seals. | `exec-fa7d2d76-8e0d-4516-b2e9-abb8035f5e3a.png` |
| `faction_anti_target_pact_emblem` | Four interlocked angular aged-metal elements around an empty center; original procedural coalition heraldry. | `exec-5675e86d-a1a0-4d1d-bcca-fcde57e73e83.png` |

## Achievement sources

```text
Use case: stylized-concept
Asset type: completed Hearts of Iron IV achievement icon source
Style/medium: hand-painted 1930s alternate-history achievement medal; square full-canvas art with dark recessed background and restrained aged-bronze border; high contrast at 64x64
Constraints: no text, letters, numbers, flags, national emblems, real political/extremist symbols, logos, watermark, modern technology, generated red X, or fake checkerboard
```

| Achievement | Prompt subject | Built-in result |
| --- | --- | --- |
| `011_secret_alliance_the_empty_chair` | Empty conference chair beneath a visibly broken burgundy pact seal. | `exec-8d57ad2e-50f8-4474-bc4d-79cba992eecd.png` |
| `011_secret_alliance_every_thread` | Gloved intelligence hand holding five connected cords without breaking them. | `exec-671306bd-2bdd-4c62-b113-3f890c08e7f8.png` |
| `011_secret_alliance_their_man_in_the_room` | One reversed seal hidden among a formal row of matching seals. | `exec-d1fe6458-05bf-4308-91d4-bc819e1674bb.png` |
| `011_secret_alliance_divide_the_table` | Round conference table split into three separated sections. | `exec-114102b6-c94d-4031-8195-c273f49164f3.png` |
| `011_secret_alliance_surrounded_not_buried` | Central dark-steel shield holding against a complete ring of points. | `exec-ccec51cf-6277-4a63-b5cc-b3f3fd876fae.png` |
| `011_secret_alliance_two_giants_one_grave` | Two large broken rival seals outside a smaller surviving central emblem. | `exec-de561e42-39f2-488c-9982-2bc16f256175.png` |

Grey variants are exact black-and-white conversions of the completed icons. Not-eligible variants composite `source_png/achievement_not_eligible_overlay_recovered.png` over the grey icon. The overlay is the accepted Event 013 recovery of the repository treatment: 939 non-zero-alpha pixels and documented `0.07/255` mean reconstruction error against eight existing repository pairs.

## Coalition-closure animation sources

Frame 004 was generated first as the approved fully closed static fallback:

```text
Broken burgundy wax-and-bronze intelligence seal centered inside three jointed oxidized-gunmetal arms fully locked inward; soot-black cords form a tight enclosing triangle with distinct knots and brass clasps; straight-on 4:3 warning emblem, fixed symmetric pivots, flat #00ff00 background, no text or modern imagery.
```

Selected result: `exec-afe41a24-e68b-43c0-8a65-b703ad60ff20.png`.

Frames 000, 001, 002, 003, 005, 006, and 007 are precise `$imagegen` edits of frame 004. Every edit prompt preserves the exact seal identity, mechanism design, materials, camera, centered scale, outer pivots, palette, and flat chroma background while explicitly redrawing arm joints, cord lay, knots, and clasp positions for the state in `frame_plan.md`. Lighting, blur, opacity, hue, whole-image transforms, or local scripted motion were prohibited.

| Frame | Selected built-in result |
| --- | --- |
| 000 | `exec-5397f2a1-6797-4b0e-af6b-2949138c16b3.png` |
| 001 | `exec-0b620798-c663-4b08-8dcd-467662840e77.png` |
| 002 | `exec-0a268368-77d3-4a7c-a374-962a035b60bf.png` |
| 003 | `exec-5ddf8cf2-a12f-486f-b60a-b816956b3ebe.png` |
| 004 | `exec-afe41a24-e68b-43c0-8a65-b703ad60ff20.png` |
| 005 | `exec-7f4066a7-8555-4dbc-a0a3-d8ad71c79913.png` |
| 006 | `exec-592cd9c0-43c0-459c-a49d-fe5b6ef2d0df.png` |
| 007 | `exec-9443b62a-406b-4538-8916-ef6ce2d273f9.png` |

Deterministic processing was limited to official chroma removal, exact canvas resizing, frame-sheet assembly, GIF/contact-sheet assembly, and BGRA DDS conversion.
