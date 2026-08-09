# Event 018 asset and presentation record

This document is the durable runtime inventory for Event 018 after removal of the temporary `docs/assets/018_resources_found/` evidence workspace. Runtime files remain in engine-facing folders. Permanent production and audit evidence remains under `docs/plans/018_resources_found_plans/subagent_handoffs/` and `docs/super_events/018_resources_found/`.

No runtime definition points into `docs/assets/`. The separate durable portrait-source archive convention is not used by the wholly fictional Oth-Kesh identity.

## Selected-field interface

The selected-field panel uses `gfx/interface/018_resources_found/resource_field_panel.dds` and the static Suspended and Closed identities in the same folder. Five real-frame animation sheets live under `gfx/interface/animated/018_resources_found/`: Seal and Unsafe contain 10 frames each, while Disturbance, Breach, and Sealing contain 12 frames each. Every animated family has a registered static fallback for the animation-disabled setting.

`interface/018_resources_found.gfx`, `interface/018_resources_found.gui`, and `common/scripted_guis/018_resources_found_scripted_gui.txt` own registration, layout, and state selection. The final MCP pass inspected active, history, empty, full, minimum, maximum, long-text, hover, selected, disabled, and warning states at 1280 by 720, 1366 by 768, 1920 by 1080, and 2560 by 1440. It found no Event 018-local overflow, clipped child, click-box mismatch, invisible or conflicting click region, missing sprite, texture, font, localisation, resolution drift, or missing button trigger/effect. The exact artifact links and state matrix are retained in `subagent_handoffs/event018_scripted_gui_visual_fix_handoff.md`.

## Focus, idea, decision, category, and achievement art

The current DHO focus tree has 67 registered 94 by 86 focus icons under `gfx/interface/goals/018_resources_found/`. The original 65-icon package and its decoded-pixel, registration, and provenance audit are recorded in `subagent_handoffs/asset_audio_reaudit_handoff.md` and `subagent_handoffs/icon_provenance_repair_handoff.md`. The two later standalone hierarchy focuses use:

- `goal_DHO_count_every_vein.dds` for `DHO_count_every_vein`;
- `goal_DHO_chamber_autonomy.dds` for `DHO_chamber_autonomy`.

Both later icons are 94 by 86 uncompressed BGRA DDS files with transparent corners and exact decoded round-trip parity. Their production and registration evidence is retained in `subagent_handoffs/event018_two_focus_icons_2026-08-09.md`.

The remaining permanent package contains 36 unique idea or state icons under `gfx/interface/ideas/018_resources_found/`, 39 action-family decision icons plus five category icons and five category pictures under `gfx/interface/decisions/018_resources_found/`, and 15 complete achievement triplets under `gfx/achievements/`. The action-family sprites cover 125 visible Event 018 decisions and missions. Nine scheduler missions are intentionally hidden and have no icon.

## Report, news, super-event, portrait, and flag art

The runtime package contains 10 report images, six news images, and three distinct 457 by 328 super-event images. The fictional Oth-Kesh country package includes its leader and commander portraits, the eight-frame Vhorruk presentation sheet, and six original flag identities at large, medium, and small sizes.

The final asset audit found unique runtime hashes and exact sprite consumers for these families. The Oth-Kesh are wholly fictional nonhumans, so their portrait and identity art used the generated-fictional route rather than a grounded-person source placeholder.

## Cave-monster 3D package

The Event 018 cave unit consumes one bespoke model package under `gfx/models/units/018_resources_found_cave_monster/`:

- `resources_found_cave_monster.mesh`;
- diffuse, normal, and specular DDS textures;
- idle, move, attack, and death animation files;
- `animation_018_resources_found_cave_monster.asset`.

The model was produced through the Event 018 3D workflow and is wired by the cave unit entity package. Mesh, material, animation, scale, export, and reimport evidence is retained in `subagent_handoffs/cave_monster_3d_model_handoff.md` and `018_cave_monster_3d_integration_addendum.md`.

## Super-event audio, quotes, and rights

Event 018 owns super-event displays 82 through 84 and audio IDs 54 through 56. Their final OGG cues are 115, 110, and 109 seconds, with matching WAV masters, stable sound wrappers, volume variants, music localisation, and catalogue entries.

- Emergence uses Mussorgsky's *Bydlo*, performed by the Skidmore College Orchestra from the documented worldwide public-domain release, with Job 28:5 as its sourced quotation.
- World End uses Brahms's Symphony No. 1, movement I, under the documented CC0 recording grant, with the sourced *Prometheus Bound* quotation.
- Global defeat uses Chopin's Prelude in E minor, Op. 28 No. 4, performed by Ivan Ilic under CC BY 3.0, with the sourced Herodotus quotation and retained attribution/change notice.

The exact source, licence, checksum, attribution, selector, and trigger evidence is retained in `docs/super_events/018_resources_found/overview.md`, `subagent_handoffs/super_event_audio_researcher_handoff.md`, `subagent_handoffs/super_event_text_researcher_handoff.md`, and `subagent_handoffs/asset_audio_reaudit_handoff.md`.

## Temporary-workspace disposition

The event-scoped `docs/assets/018_resources_found/` folder was an implementation and review workspace. Its durable runtime inventory, licensing conclusions, provenance counts, sprite mappings, review findings, and exceptions are preserved in this document and the permanent handoffs named above. The temporary folder is intentionally absent at completed-state review and must not be recreated merely to satisfy a historical path in an older handoff.
