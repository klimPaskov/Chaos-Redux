# Event 114 asset-production prompt

Implement the visual package for Event 114 Demilitarization from the accepted files in docs/specs/114_demilitarization_specs/. Follow current AGENTS.md, chaos-redux-event-assets, and the current specialist definitions. Read 114_demilitarization_presentation.md, the gameplay files that own each consumer, and 114_demilitarization_achievements.md before producing assets.

All names in the specification are working labels. Write functional text through native localisation. Do not generate readable interface labels, numbers, flags, invented treaty signatures, or button text into scene artwork.

## Required coverage

Produce the 22 original subjects listed in 114_demilitarization_presentation.md:

- News: A114-N01 opening withdrawal and A114-N02 actual capital concentration.
- Reports: A114-R00 frontier withdrawal, A114-R01 inland withdrawal, A114-R02 real departures or dissolution, and A114-R03 closed provincial military space.
- Category: A114-P01 static picture and A114-C01 small category icon.
- Decisions: A114-D01 service conditions, D02 cadres, D03 consolidation, and D04 attendance.
- Missions: A114-M01 endangered muster and A114-M02 sustained recovery, with separate original sources and outputs.
- Spirits: A114-I01, I02, and I03 as one progression family.
- Achievements: A114-A01 through A05, each with its full completed, grey, and not-eligible state triplet.

Mission icons have their own briefs, source artwork, manifest rows, and outputs. Coordinate their motifs with the decision family while preserving the supplied icon-type separation rule.

R00 and both mission subjects are explicit parent additions to the original 19-row asset consultation. The baseline country report needs its own report composition, and mission consumers require distinct production rows. N02 is used only when the narrative actually concerns a valid capital refuge. R03 must remain truthful for zero-space countries.

## Consumer and reference gate

For every row, inspect and record the actual owning sprite and consumer, canvas, alpha rule, state binding, and any frame treatment. Inspect the canonical role reference and contact sheet under assets/gfx_references/ before generation.

Use the source-supported planning canvases only after verification: reports 210x176, news 397x153, ordinary decisions 32x32, spirits 64x64, and achievements 64x64 per final state. The category picture's 114x101 is a reference-family target. Its real consumer and the small category icon's exact canvas remain to be checked.

The simple category has ordinary decisions, a short description, and one formatted cohesion value. Its static picture is eligible under that design. If the implemented category acquires complex controls, reconsider the picture against the owner skill before production.

## Production ownership

Use chaosx_generated_event_art for the news, report, and static-picture families. Use chaosx_icon_artist for category, decision, mission, spirit, and achievement subjects. A genuinely historical named subject or real source photograph belongs to chaosx_asset_source_researcher.

Spawn the actual required specialist through collaboration.spawn_agent with fork_turns set to none and a self-contained bounded family brief. Supply exact consumer, references, source mode, target canvas, runtime identity, output ownership, and handoff path.

The main implementation agent owns final non-portrait GFX registration and gameplay wiring. Do not treat a specialist's saved PNG as a wired gameplay asset.

## Scene and icon treatment

Generate fictional period documentary scenes with plausible 1936–1945 equipment and unnamed subjects. Keep the frontier opening, inland withdrawal, and Total closure visually distinct. Use a separate wide composition for news.

Generate full-canvas photographic sources for reports. Apply the current report-card processor afterward for black-and-white treatment, sepia, paper edge, slight tilt, transparent corners, and shadow. Do not generate a fake report card or interface window.

Generate icons with genuine native transparency. The 32x32 decision subjects must be simple enough to read at their actual size. Keep category, spirit, and achievement families separate even when their symbols are coordinated.

Inspect supported background_template components only for consumers whose actual family permits them. Keep generated subjects and cataloged template layers separate. Do not shrink a category background into an ordinary decision icon.

For each achievement, generate one original 64x64 completed subject. Derive the grey and not-eligible source layers deterministically, retaining the unchanged required red-cross overlay. Use process_achievement_icons.py and the exact supplied templates. Keep the triplet's geometry and subject aligned.

## Requests, processing, and runtime files

Save the exact native generation or editing request before execution, including prompt, transparency and reference-image inputs. Follow the current source-generation route. If the exposed tool has no backend selector, record its actual execution path rather than claiming a chosen model.

Preserve source candidates, accepted lineage, processed PNGs, and runtime outputs separately. Source repairs use the approved image-editing route. Resizing, family processing, and conversion must follow the current documented workflow.

Convert final 2D DDS assets through .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py, with the achievement processor owning the complete triplets. Validate the required legacy BGRA header, dimensions, alpha, and decoded pixel result.

Use actual event-owned runtime paths such as gfx/event_pictures/114_demilitarization/, gfx/interface/decisions/114_demilitarization/, and gfx/interface/ideas/114_demilitarization/ where the inspected consumer permits them. Preserve stable existing identities. Achievement files belong directly in gfx/achievements/ as the exact ID, ID_grey, and ID_not_eligible.

## Visual acceptance

Review every selected source at full resolution and every output at native size. Verify silhouette, subject completeness, transparent unused canvas, preserved interior opacity, unclipped meaningful detail, reference-family fit, and clean DDS round trip. Edge contact alone does not prove clipping.

Review all three spirit states together and all three states of each achievement together. A decoder succeeding does not establish readability or correct composition.

Maintain docs/assets/114_demilitarization/ with a manifest and gfx_handoff.md mapping every requirement to its saved request or attribution, source lineage, final output, sprite, actual consumer, state binding, and evidence. Promote durable provenance into permanent documentation before the current skill's final workspace cleanup.

Report completed consumers and exact unresolved blockers. Do not fill missing references, missing alpha, or an unverified canvas with a decorative placeholder and call the family complete.

