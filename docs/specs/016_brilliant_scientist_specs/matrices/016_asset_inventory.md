# Event 016 asset inventory

## Binding reconciliation

> Core-runtime inventory reconciled 2026-07-29. The exact stage-0 `156x210` leader or scientist DDS and `65x67` advisor DDS are produced and registered as `GFX_portrait_KRG_doctor_warren_kruger_stage_0` and `GFX_idea_doctor_warren_kruger_stage_0`. The fourteen Stage I through IV leader or scientist portraits and matching advisor cards are present under registered sprite contracts, and every advisor card uses the canonical advisor-template workflow. Six severe route animation sheets contain real frame-by-frame art and have registered static fallbacks. The Directorate UI, 100 focus icons, 51 achievement states, seven flag triplets, decision/category packages, seven report images, six super-event images, and six sound cues are present and wired. Expanded project/news/remnant art and all seven 3D entity packages remain blocked.

## Portraits and character assets

| Asset | Type | Size | Source mode | Animation | Use |
| --- | --- | ---: | --- | --- | --- |
| Kruger stage 0 leader | Portrait | 156x210 | Completed approved base copy from `portrait_generic_biowarfare_europe_male_01` | Static, registered | Initial and safe route leader or scientist |
| Kruger stage I | Portrait | 156x210 | Generated fictional variant | Static | National ascendancy |
| Kruger stage II | Portrait | 156x210 | Generated fictional variant | Static | International contest |
| Kruger stage III route variants | Portrait | 156x210 | Generated fictional variants | Static fallback | Forbidden science |
| Clone Kruger stage IV | Portrait sheet | 156x210 per frame | Generated per-frame | Yes | Clone sovereign leader |
| Machine Kruger stage IV | Portrait sheet | 156x210 per frame | Generated per-frame | Yes | Machine leader |
| Temporal Kruger stage IV | Portrait sheet | 156x210 per frame | Generated per-frame | Yes | Continuum leader |
| Xenobiological Kruger stage IV | Portrait sheet | 156x210 per frame | Generated per-frame | Yes | Biological or alien leader |
| Synthesis Kruger stage IV | Portrait sheet | 156x210 per frame | Generated per-frame | Yes | Mixed route leader |
| Advisor stage family | Advisor art | Existing surface size | Base plus generated route art | Severe stages optional | Host advisor |
| Scientist stage family | Scientist portrait | Verified special-project size | Base plus generated route art | Severe stages only if supported | All project fields |

## Event image assets

| Family | Quantity direction | Size | Source mode | Processing |
| --- | ---: | ---: | --- | --- |
| Appointment and policy reports | 4 to 6 | 210x176 | Generated period documentary | Report-card script, sepia |
| Project breakthrough reports | 8 to 15 | 210x176 | Generated period documentary | Report-card script, sepia |
| Accident and security reports | 8 to 12 | 210x176 | Generated period documentary | Report-card script, sepia |
| News images | 6 to 10 | 397x153 | Generated period press | Black and white |
| Super-event images | 6 | 457x328 | Generated fictional high-chaos | Recognition, formation, threat, Laboratory World, Singularity, and qualifying defeat packages |
| Defeat and remnants | 3 to 6 | Report or news size | Generated period documentary | Match target surface |

## UI asset family

| Asset | State variants | Source mode | Animation |
| --- | --- | --- | --- |
| Directorate background | Base, damaged or late-stage optional | Generated thematic art plus UI slicing | Static |
| Profile frame | Human, secured, sovereign | Generated or hand-processed | Static |
| Mandate meter | Empty to full states | UI production | Static fill |
| Dependence meter | Empty to full states | UI production | Static fill |
| Exposure meter | Empty to full states | UI production | Static fill |
| Control-status frame | Secure, contested, brittle, compromised, lost | Generated state family | Critical state can animate |
| Project card | Locked, theory, prototype, deployment, weaponized, damaged | Generated and UI production | Active marker can animate |
| Facility card | Normal, hardened, infiltrated, damaged, lost | Generated and UI production | Warning optional |
| Foreign contact card | Neutral, offer, threat, operation, resolved | UI production | Static |
| Sovereignty panel | Hidden, demand, countdown, confrontation | Generated thematic art | Warning border animated |
| Singularity indicator | Rumored, theory, prototype, construction, delivery, armed | Generated state family | Armed indicator animated |

## Icon families

| Type | Target size | Estimated distinct assets | Notes |
| --- | ---: | ---: | --- |
| Focus icons | 94x86 | 45 to 70 | Reuse within coherent subgroups, unique capstones |
| Idea and spirit icons | 64x64 | 15 to 25 | Own source art, not focus resizes |
| Decision icons | 32x32 | 30 to 45 | Simplified silhouettes |
| Decision category icons | Verify existing | 8 to 10 | Own category compositions |
| Tech and special-project icons | 64x64 and 132x52 where needed | 25 to 45 | Stage and prototype families |
| Achievement completed icons | 64x64 | 17 | Plus grey and not-eligible variants, for 51 final DDS files |
| Focus filter icons | Verify existing | 10 to 12 | Route taxonomy |
| Faction emblem | Verify existing | 1 to 3 | Kruger bloc and possible commonwealth variant |

## Flags

| Flag | Normal | Medium | Small | Source mode |
| --- | ---: | ---: | ---: | --- |
| Base Kruger State | 82x52 | 41x26 | 10x7 | Generated fictional |
| Human technocracy | 82x52 | 41x26 | 10x7 | Generated fictional |
| Replicated sovereignty | 82x52 | 41x26 | 10x7 | Generated fictional |
| Machine ascendancy | 82x52 | 41x26 | 10x7 | Generated fictional |
| Temporal Continuum | 82x52 | 41x26 | 10x7 | Generated fictional |
| Xenobiological ascendancy | 82x52 | 41x26 | 10x7 | Generated fictional |
| Synthesis | 82x52 | 41x26 | 10x7 | Generated fictional |

Create only route variants that are implemented. Validate TGA origin and orientation.

## Animation packages

| Package | Frame target | Suggested frames | FPS direction | Loop | Static fallback |
| --- | ---: | ---: | ---: | --- | --- |
| Clone Kruger portrait | 156x210 | 8 to 12 | 4 to 6 | Yes | Stage IV clone static |
| Machine Kruger portrait | 156x210 | 8 to 12 | 4 to 6 | Yes | Stage IV machine static |
| Temporal Kruger portrait | 156x210 | 10 to 16 | 4 to 6 | Yes | Stage IV temporal static |
| Xenobiological or alien Kruger portrait | 156x210 | 8 to 12 | 3 to 5 | Yes | Stage IV static selected from the locked campaign conclusion |
| Synthesis Kruger portrait | 156x210 | 10 to 16 | 3 to 5 | Yes | Stage IV synthesis static |
| Control warning frame | UI-defined | 6 to 10 | 4 to 8 | Yes | Critical static frame |
| Active project marker | UI-defined | 6 to 8 | 4 to 6 | Yes | Active static marker |
| Singularity armed indicator | UI-defined | 8 to 12 | 3 to 6 | Yes | Armed static state |

No final animation may be generated by transforming one still.

## Reference folders

Asset workers must inspect:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/news`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/super_event`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/technologies/legacy`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/special_projects`

## Asset completion evidence

For every asset:

- Source file.
- Processed PNG.
- Final DDS or TGA.
- Exact dimensions.
- Transparency check where relevant.
- Manifest entry.
- Proposed or final sprite name.
- GFX handoff.
- Related event, focus, idea, decision, achievement, project, or UI state.
- Source and license note when sourced.
- Prompt and source-mode rationale when generated.

For every animation:

- Brief.
- Frame plan.
- One source PNG per frame.
- Processed frames.
- Horizontal sheet PNG and DDS.
- Static fallback PNG and DDS.
- GIF preview.
- Contact sheet.
- Frame count, FPS, loop, anchor, and trigger.
