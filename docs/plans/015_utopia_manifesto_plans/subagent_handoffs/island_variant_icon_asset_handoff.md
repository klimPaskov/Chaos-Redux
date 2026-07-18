# Event 015 island-variant icon asset handoff

Date: 2026-07-15

## Scope completed

Produced the three requested final ImageGen-sourced icons for the already registered Event 015 island-variant sprites. No gameplay, localisation, GUI, focus, decision, or interface file was edited.

## Runtime deliverables and identifiers

| Sprite | Asset type | Final path | Size |
| --- | --- | --- | --- |
| GFX_goal_utopia_archipelago_network | national focus icon | gfx/interface/goals/015_utopia_manifesto/goal_utopia_archipelago_network.dds | 95x85 |
| GFX_goal_utopia_leased_island | national focus icon | gfx/interface/goals/015_utopia_manifesto/goal_utopia_leased_island.dds | 95x85 |
| GFX_decision_utopia_archipelago_network | decision icon | gfx/interface/decisions/015_utopia_manifesto/decision_utopia_archipelago_network.dds | 64x64 |

The focus textures also resolve the already registered GFX_goal_utopia_archipelago_network_shine and GFX_goal_utopia_leased_island_shine definitions.

## Files created or updated

- Three frozen ImageGen source PNGs under docs/assets/015_utopia_manifesto/source_png/.
- Three keyed intermediate PNGs and three exact-size processed PNGs under docs/assets/015_utopia_manifesto/processed_png/.
- Three package DDS copies under docs/assets/015_utopia_manifesto/dds/.
- Three runtime DDS files under gfx/interface/goals/015_utopia_manifesto/ and gfx/interface/decisions/015_utopia_manifesto/.
- Two transparency and native-size review contacts under docs/assets/015_utopia_manifesto/contact_sheets/.
- Prompt record at docs/assets/015_utopia_manifesto/prompts/island_variant_icon_generation.md.
- Source record at docs/assets/015_utopia_manifesto/notes/island_variant_icon_source_records.md.
- Updated docs/assets/015_utopia_manifesto/manifest.md and docs/assets/015_utopia_manifesto/gfx_handoff.md.

## Before and after

Before this handoff, the five base and shine sprite registrations existed but their three target DDS paths were absent. The runtime paths now contain final art: a three-island harbor and provisioning network, a negotiated lease ledger and key, and a separate compact three-site chart-table decision operation.

## Meaningful validation

- Visual review at final dimensions confirms that both focus icons read as full HOI4 focus compositions and the decision remains a distinct compact action composition.
- The two 95x85 focus PNGs and one 64x64 decision PNG have real alpha, transparent corners, nonempty opaque subjects, and zero detected residual magenta pixels under the package QA threshold.
- The three final DDS files use the required legacy one-level uncompressed BGRA layout: 124-byte DDS header after the magic, 32-bit RGB plus alpha pixel format, correct masks, DDSCAPS_TEXTURE, exact byte length, and alpha range 0 through 255.
- Runtime and package copies are byte-identical. All three processed PNG and DDS checksums are distinct.
- interface/015_utopia_manifesto.gfx contains exactly one base definition for each requested sprite, exactly one shine definition for each focus, and the expected final texture paths.
- The checker and charcoal contacts show centered subjects without a white matte, opaque square, checker contamination, or chroma fringe.

## Parent follow-up

Retain the existing sprite registrations and gameplay references. The parent remains responsible for final integration review; no additional asset-side wiring is required for these three texture paths.

## Simplifications, omissions, and blockers

None. No fallback or substitute was used.

## Skills used

- chaos-redux-event-assets
- chaos-redux-subagents
- official imagegen

