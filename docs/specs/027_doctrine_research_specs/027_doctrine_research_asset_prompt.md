# Asset production prompt: Event 027 Doctrine Research

## Status

Every asset in this prompt is produced, wired, and documented.
Provenance, prompts, review views, and checksums are in `docs/assets/027_doctrine_research/manifest.md` and `gfx_handoff.md`, and part 4 lists the runtime paths and sprites.
Use this prompt only to replace an asset; follow `.claude/skills/chaos-redux-event-assets/SKILL.md` and route through `chaos-redux-subagents`.

## Report-event image

- Route: `chaosx_generated_event_art`.
- Runtime: `gfx/event_pictures/027_doctrine_research/027_doctrine_research_report.dds`, sprite `GFX_report_event_027_doctrine_research` in `interface/027_doctrine_research.gfx`.
- Canvas: match the current report-event consumer and reference family named in the asset skill.
- Scene: a 1936 to 1945 joint-service field exercise or military-school demonstration with one clear instructor or officer as focal subject, infantry and artillery activity, an armoured vehicle, aircraft overhead, and maps, manuals, range boards, or observation equipment as secondary props; a distant harbour cue only when it fits.
- Keep it internationally neutral: no flags, insignia, or recognisable leaders.
- Reject readable generated text, modern equipment or architecture, cinematic grading, holograms, collages, doctrine UI screenshots, laboratory scientists, a lone command table, battle carnage, and malformed hands, weapons, or vehicles.

## Achievement icon triplets

- Route: `chaosx_icon_artist`, after inspecting the canonical achievement references and triplet workflow.
- Each achievement needs its own source art and a completed, grey, and not-eligible DDS in `gfx/achievements/` named after the full achievement ID; never recolour one achievement into another.

| Achievement ID | Motif | Readability priority |
| --- | --- | --- |
| `027_doctrine_research_first_lesson` | A field manual opened at its first marked lesson, with a small staff-college insignia, pointer, or pencil | The first-lesson marker reads at 64x64. |
| `027_doctrine_research_single_school` | Five doctrine tabs or lesson markers converging on one school crest | Five concentrated steps without numerals or text, and unlike the native Doctrine of Choice icon. |
| `027_doctrine_research_joint_curriculum` | Four service or track symbols around a curriculum binder, compass, or crest | The four-part structure stays balanced and readable. |

## Doctrine icons

Choice pages reuse the native domain, Grand Doctrine, track, and subdoctrine sprites, including Chaos Warfare's.
Never generate replacement doctrine icons and never substitute a focus, idea, decision, or unrelated technology icon.
