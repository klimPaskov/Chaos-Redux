# Asset production prompt: Event 101 Tasks

Produce the complete accepted Event 101 visual package using `chaos-redux-event-assets`. Read AGENTS.md, the current asset skill, the registered worker definitions, Part 7, this prompt and the achievement prompt before production. The seven main specs are the gameplay authority. All names here are proposed technical identifiers and structural directions, not finished player-facing copy.

Use `chaosx_icon_artist` for icons and `chaosx_generated_event_art` for the seven non-icon images. The parent owns all GFX, localisation, mission, modifier, event and achievement wiring. Keep workers within the named asset and evidence paths.

This is a future production input under [current authority and workflow](README.md#current-authority-and-workflow). The import does not run it. Delegate exact assets and allowed paths with self-contained prompts. Current asset-skill rules own generation, processing, independent review where required, workspace cleanup and parent integration.

## Reference and source lock

Use the current skill's canonical root `.claude/skills/chaos-redux-event-assets/assets/gfx_references/`. Inspect each matching contact sheet, individual reference, catalog row and exact native consumer before choosing the final canvas, crop, alpha and frame behavior.

The historical repository receipt inspected the older `assets/vanilla_reference/` directory. Its catalog recorded the generic crisis small category icon at 52 by 39 and category-picture references at 114 by 101. Those dated observations do not establish the current tree or a universal engine size. Use the current skill's canonical tree and inspect the actual consumer before generating category assets.

| Output family | Matching reference family | Source mode |
| --- | --- | --- |
| Mission icons | `icons/decisions/` and `icons/missions/` | Original native ImageGen, genuine transparent background |
| Small category icon | `icons/decision_categories/` | Original native ImageGen, reference-constrained symbolic subject |
| Static category picture | `icons/decision_categories/pictures/` | Original generated period still life, consumer-correct background |
| Report scenes | `event_art/report/` | Original fictional documentary-style scene, opaque photograph before local card processing |
| Outcome idea icons | `icons/ideas/` and relevant approved visual components | Two separate original transparent ImageGen subjects |
| Achievements | `icons/achievements/` plus exact immutable template inputs | Seven separate original transparent subjects, deterministic state derivation |

All report scenes are fictional period scenes, not claimed archival photographs or real-person portraits. Show believable 1930s and 1940s equipment, architecture and clothing. Keep identifiable real people and countries out of the generic family art unless a later accepted brief supplies a grounded identity and sources.

Do not trace, recolor or ship review references. Do not resize one asset type to fill another. No generated readable text, fake controls, meters, counters or button artwork may appear in these images.

For every alpha-backed icon and achievement subject, request `transparent_background = true` in the initial native ImageGen call and preserve real alpha through processing and DDS conversion. Keep the full-canvas photograph source opaque before report-card processing. Category backgrounds follow their inspected consumer. Background removal is fallback-only for failed native alpha or an inherited opaque source, with the untouched source, method and edge validation recorded under the current asset skill.

## Runtime asset manifest

The proposed GFX destination is `interface/101_tasks.gfx`, subject to parent confirmation that an existing owner file is not more appropriate. Keep each proposed sprite stable after wiring.

### Six mission icons

Every row is a separate original 32 by 32 transparent composition. Use compact silhouettes and limited interior detail. The sprites are selected by the active task's family within one mission consumer.

| ID | Subject direction | Final DDS | Proposed sprite |
| --- | --- | --- | --- |
| A01 | Field objective and military advance, readable without a map full of arrows | `gfx/interface/decisions/101_tasks/decision_101_tasks_offensive.dds` | `GFX_decision_101_tasks_offensive` |
| A02 | Protected position and a clear defensive object | `gfx/interface/decisions/101_tasks/decision_101_tasks_defensive.dds` | `GFX_decision_101_tasks_defensive` |
| A03 | Usable equipment and formation readiness in one compact symbol | `gfx/interface/decisions/101_tasks/decision_101_tasks_preparation.dds` | `GFX_decision_101_tasks_preparation` |
| A04 | Substantial construction tool or working industrial component | `gfx/interface/decisions/101_tasks/decision_101_tasks_industrial.dds` | `GFX_decision_101_tasks_industrial` |
| A05 | Practical agreement or delivered support, not a generic decorative handshake alone | `gfx/interface/decisions/101_tasks/decision_101_tasks_diplomatic.dds` | `GFX_decision_101_tasks_diplomatic` |
| A06 | Emergency response and recovery with a clear practical object | `gfx/interface/decisions/101_tasks/decision_101_tasks_crisis.dds` | `GFX_decision_101_tasks_crisis` |

### Category and temporary effects

| ID | Canvas | Subject direction | Final DDS and proposed sprite |
| --- | --- | --- | --- |
| A07 | Proposed 52 by 39, verify exact consumer | Restrained dispatch-and-deadline symbol, distinct from the mission icons | `gfx/interface/decisions/101_tasks/decision_category_101_tasks.dds`, `GFX_decision_category_101_tasks` |
| A08 | Reference 114 by 101, verify exact consumer | Period dispatch materials and analog time cue in one static still life, no readable invented writing | `gfx/interface/decisions/101_tasks/decision_cat_101_tasks.dds`, `GFX_decision_cat_101_tasks` |
| A09 | 64 by 64 | Fulfilled national commitment and useful organized effort, compact symbolic idea art | `gfx/interface/ideas/101_tasks/idea_101_tasks_fulfilled.dds`, `GFX_idea_101_tasks_fulfilled` |
| A10 | 64 by 64 | Missed commitment and limited administrative burden, visibly distinct from collapse | `gfx/interface/ideas/101_tasks/idea_101_tasks_setback.dds`, `GFX_idea_101_tasks_setback` |

A08 is eligible because the category contains only native text and one mission. It has no custom controls or animation. A09 and A10 serve the visible positive and negative aggregate effect carriers. The actual capability and expiry are native tooltip text, not baked into either icon.

### Six report images

Each final report card is exactly 210 by 176 RGBA and DDS. Generate one neutral operational scene per family. The same family card may support assignment and outcome reports only when it remains truthful. A scene of victory celebration cannot also illustrate a failed defense.

| ID | Scene direction | Final DDS | Proposed sprite |
| --- | --- | --- | --- |
| A11 | Troops and field equipment at a road junction or military position | `gfx/event_pictures/101_tasks/report_event_101_tasks_offensive.dds` | `GFX_report_event_101_tasks_offensive` |
| A12 | A maintained defensive position under credible pressure | `gfx/event_pictures/101_tasks/report_event_101_tasks_defensive.dds` | `GFX_report_event_101_tasks_defensive` |
| A13 | Practical equipment preparation or usable-force training | `gfx/event_pictures/101_tasks/report_event_101_tasks_preparation.dds` | `GFX_report_event_101_tasks_preparation` |
| A14 | Workers and a useful industrial or transport commissioning site | `gfx/event_pictures/101_tasks/report_event_101_tasks_industrial.dds` | `GFX_report_event_101_tasks_industrial` |
| A15 | A practical aid exchange or period agreement setting | `gfx/event_pictures/101_tasks/report_event_101_tasks_diplomatic.dds` | `GFX_report_event_101_tasks_diplomatic` |
| A16 | Grounded emergency supplies, repairs or recovery coordination | `gfx/event_pictures/101_tasks/report_event_101_tasks_crisis.dds` | `GFX_report_event_101_tasks_crisis` |

Generate the photographic source first. Apply `.claude/skills/chaos-redux-event-assets/tools/process_report_event_image.py` for the consistent black-and-white and sepia card, grain, border, subtle tilt, transparent margins and soft shadow. Do not ask ImageGen to paint a tilted card or simulate the game frame.

### Seven achievement subjects and twenty-one final states

Each ID has its own original transparent subject at 64 by 64. The exact goals, title directions, difficulty, visibility and tracking requirements are in [the achievement prompt](101_tasks_achievement_prompt.md).

| Asset ID | Achievement ID | Subject direction |
| --- | --- | --- |
| A17 | `chaosx_tasks_six_families` | Six distinct practical task elements in a single readable emblem |
| A18 | `chaosx_tasks_capital_stands` | Protected government seat with a surviving defensive structure |
| A19 | `chaosx_tasks_corridor_open` | A repaired transport connection through a broken barrier |
| A20 | `chaosx_tasks_built_by_us` | Substantial completed work and a distinctive construction tool |
| A21 | `chaosx_tasks_reliable_partner` | Delivered aid and a protective commitment in one clear composition |
| A22 | `chaosx_tasks_three_crises` | Three resolved emergency elements around a recovery motif |
| A23 | `chaosx_tasks_kept_commitments` | Three completed commitments expressed through a durable compact emblem |

For each exact achievement ID, create these three final root-level files:

- `gfx/achievements/<achievement_id>.dds`
- `gfx/achievements/<achievement_id>_grey.dds`
- `gfx/achievements/<achievement_id>_not_eligible.dds`

Use the exact ID from the registry. Do not create an Event 101 subfolder under `gfx/achievements/`. Parent wiring belongs in the existing shared achievement registry, `interface/chaosx_achievements.gfx` and `localisation/english/chaosx_achievements_l_english.yml`.

## Achievement processor contract

For new art, retain the original color subject, derive the grey subject deterministically and create the not-eligible source with the unchanged overlay. Supply all three complete source layers to `.claude/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`.

Use the immutable completed template, grey template and overlay from the current canonical template directory. These are imported historical SHA-256 values. Compare them with the actual current owner inputs, recording any revision difference without altering the templates or inventing current verification:

| Input | SHA-256 |
| --- | --- |
| `achievement_template.png` | `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA` |
| `achievement_template_grey.png` | `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022` |
| `overlay.png` | `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD` |

Use separate source and processed output directories. Do not independently generate three states, redraw the red overlay, alter the templates, add a second outer frame or feed processed outputs back as fresh source.

## Conversion, review and delivery

Use only the current converter at `.claude/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. The obsolete `.tools/convert_to_dds.py` path must not be restored. Follow the skill's strict one-level legacy 32-bit BGRA header, channel, alpha and decoded-pixel contract for these 2D assets.

Retain native ImageGen source evidence, prompt, source mode, background mode, processed PNG, final DDS, current consumer reference, dimensions, visible bounds and selection history for every asset. Review icons on contrasting solid backgrounds and checkerboard evidence, and review report cards at native size. A checkerboard must never be baked into the texture.

The active work root is `docs/assets/101_tasks/`, with `manifest.md`, `prompts/`, `source_png/`, `processed_png/`, `contact_sheets/`, `notes/` and `gfx_handoff.md`. Every manifest row identifies asset ID, consumer, exact paths, sprite, source evidence, status and any unresolved reference or alpha issue.

The accepted inventory is 23 original subjects or compositions producing 37 runtime DDS files: six mission icons, two category assets, two idea icons, six report cards and twenty-one achievement states. Seven achievement subjects are inputs to their state triplets, not seven additional runtime textures.

The parent visually reviews the contact sheets and exact native consumers before wiring. Promote durable provenance, paths, review results and remaining uncertainty into the canonical `docs/events/101_tasks.md` or an appropriate permanent event-plan record before cleaning temporary asset work under the asset skill. Keep active or blocked evidence while acceptance is unresolved.

Report each asset as generated, processed, converted, handed off, wired, complete or explicitly blocked according to actual evidence. Deliver the complete authorized inventory and exact wiring handoff, then the parent integrates and reviews its owned consumers. Do not claim live-game appearance from a PNG preview or wait for user-owned live testing.
