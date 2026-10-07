# Event 097 asset-production prompt

Produce the visual assets for the accepted Collaboration specification in `docs/specs/097_collaboration_specs/`. Read all ten parts, especially presentation and achievements. This is a production assignment after the written design, not permission to change mechanics or add a new interface.

## Required reading and execution

Read current AGENTS.md, the canonical `chaos-redux-event-assets` skill, and the exact relevant role profiles. Read the canonical asset reference README, report-picture catalog and contact sheet, achievement catalog and contact sheet, relevant individual references, and processor documentation. The planning task read the supplied asset skill but did not have those referenced files or pixels. Resolve that gap before production.

Use `chaosx_generated_event_art` for fictional report compositions and `chaosx_icon_artist` for achievement subjects. Spawn named roles with a complete explicit context and `fork_turns="none"` where the Codex tool is used. No asset role ran during planning.

## Report manifest

Use this event-owned final directory: `gfx/event_pictures/097_collaboration/`.
Use an event-owned sprite definition file such as `interface/097_collaboration.gfx` after inspecting current naming and collisions. Do not modify or delete the old shared vanilla handshake image used by other consumers.

| Output filename | Proposed sprite | Source direction and actual consumer |
| --- | --- | --- |
| `097_collaboration_baseline.dds` | `GFX_report_event_097_collaboration_baseline` | Fictional reciprocal discreet meetings, normal manifestation report |
| `097_collaboration_deep_networks.dds` | `GFX_report_event_097_collaboration_deep_networks` | Fictional municipal, industrial, and police figures, Evolution I report |
| `097_collaboration_administrations.dds` | `GFX_report_event_097_collaboration_administrations` | Local authority greeting an arriving occupier, Evolution II report |
| `097_collaboration_fifth_column.dds` | `GFX_report_event_097_collaboration_fifth_column` | Civil administration withdrawing support during retreat, Evolution III announcement and relevant breakthrough report |
| `097_collaboration_governments.dds` | `GFX_report_event_097_collaboration_governments` | Local regime taking office under foreign patronage, Evolution IV and government readiness report |

Use original generated period-documentary compositions for these fictional situations. Describe 1936-1945 photographic technology, architecture, clothing, vehicles, and natural composition. Do not identify real people as collaborators, introduce readable text or modern elements, or falsely call generated material archival. Use the separate source researcher only if a real, licensed archival alternative is deliberately selected and its exact fit is verified.

All final report canvases are 210x176 RGBA with the skill's black-and-white/sepia treatment, slightly tilted documentary card, transparent edge space, and soft shadow. Generate or source the scene without baking in the surrounding UI. Process with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`, then use the canonical DDS conversion and validation route. Inspect transparency, crop, focal readability, and the actual report consumer.

## Achievement subject manifest

| Exact ID | Original subject direction |
| --- | --- |
| `chaosx_097_reciprocal_conquest` | Opposed military caps and one broken defensive line |
| `chaosx_097_administration_that_lasts` | Intact civic building and five small keys |
| `chaosx_097_return_from_the_brink` | Damaged shield raised against a fallen foreign standard |
| `chaosx_097_local_government_network` | Five civic buildings linked to one distant capital |
| `chaosx_097_homeland_returns` | Civic building released from a broken foreign control chain |
| `chaosx_097_two_collaborator_spheres` | Two celestial halves over separate groups of local-government buildings |

Use native ImageGen for one original transparent subject per achievement. No frame, square background, red cross, text, flag, fake checkerboard, or borrowed idea/focus icon. Retain the original generated source, prompt, and centered 64x64 processed color subject.

Derive three complete aligned source layers deterministically: unchanged color subject, grayscale version with the same alpha and placement, and that grey source with the unchanged overlay at its exact native alignment. Never generate three unrelated state artworks or derive sources from already templated runtime output.

## Exact templates and processing

Under the canonical asset skill root, use:

```text
assets/gfx_references/icons/achievements/template/achievement_template.png
assets/gfx_references/icons/achievements/template/achievement_template_grey.png
assets/gfx_references/icons/achievements/template/overlay.png
```

Verify the supplied skill's SHA-256 values against actual files:

```text
completed: 248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA
grey:      70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022
overlay:   89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD
```

Preserve template bytes, canvas, position, and colors. The planning task did not inspect or verify these files. Do not report those hashes as an executed integrity check until actual production has compared them.

Use `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py` with all three complete source layers and an explicit separate output directory. Apply the completed background beneath the color source and the grey background beneath the grey and not-eligible sources. A single-source generic DDS conversion is not the achievement workflow.

Final files must be exact 64x64, one-level legacy BGRA DDS files, with the expected alpha-composited pixels. Run the processor's dry-run and final audit routes, preserve native-size review PNGs, and inspect each state against the reference family.

## Runtime paths and wiring

For every exact achievement ID above, install these three files directly in the root `gfx/achievements/`:

```text
<achievement_id>.dds
<achievement_id>_grey.dds
<achievement_id>_not_eligible.dds
```

Do not put achievements in an event subfolder. Align the exact IDs with `common/achievements/chaos_redux_achievements.txt`, `interface/chaosx_achievements.gfx`, and `localisation/english/chaosx_achievements_l_english.yml` after inspecting their current structures. Keep the shared registry's root unique identity intact.

There are five report DDS outputs and eighteen achievement DDS outputs, for 23 planned runtime images. Optional connected achievements may have prepared art, but their gameplay registration must remain gated until their dependencies exist. Art does not establish gameplay completion.

## Delivery and review

Stage production sources and provenance under `docs/assets/097_collaboration/` according to the current asset skill. Preserve each source mode, source identity or generation prompt, template hashes actually checked, processor commands, dimensions, alpha checks, final paths, sprite consumers, and visual review results. Clean temporary production material only after the required durable evidence and final outputs are safely retained.

Return a manifest with one row for every final runtime image. Mark missing, blocked, unprocessed, unwired, and visually unreviewed states honestly. A generated picture, prompt, or montage is not a substitute for processed and wired runtime assets. Do not introduce portraits, custom flags, 3D assets, animation, or a super-event merely to expand the asset count.
