# Event 016 Idea and National-Spirit Icon Asset Handoff

## Scope and ownership

This handoff covers the exact thirteen bespoke 64x64 idea and national-spirit icons requested by `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_9_assets_animation_and_localisation.md` lines 296-318.

The asset tranche is complete through source generation, alpha processing, DDS conversion, DDS decoding, contact-sheet review, and validation. The parent agent owns final visual review in context, `.gfx` registration, gameplay references, localisation alignment, and the final commit.

This subagent did not edit gameplay, localisation, focus, idea, decision, event, `.gfx`, `.gui`, spreadsheet, or shared top-level manifest files. Existing Kruger portrait and advisor DDS files were not overwritten.

## Canonical references and source mode

Before generation, I inspected the one canonical reference family at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/ideas/contact_sheet.png` and the matching `icons/ideas` entries in `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`.

The canonical sheet shows compact HOI4 spirit-style compositions with strong centered silhouettes, aged texture, dark outlines, and transparent unused canvas. The reference PNGs were review material only and were not used as final art.

All thirteen icons use the official built-in `$imagegen` generate workflow. Each prompt required a unique subject composition on a perfectly flat `#00ff00` chroma-key background, with no readable text, letters, numbers, modern UI, protected medical emblem, atom symbol, watermark, checkerboard, white halo, or opaque square frame. The installed ImageGen chroma-key helper removed the background, after which Pillow resized each alpha image to exact 64x64.

## Completed asset inventory

Every row has a retained generated source PNG, processed transparent PNG, final runtime DDS, DDS-decoded PNG, manifest row, prompt/provenance entry, and validation TSV row.

| Concept | Stable stem | Motif | Runtime DDS | Sprite token |
|---|---|---|---|---|
| Kruger's Appointment | `idea_brilliant_scientist_kruger_appointment` | Gloved hand presenting a brass laboratory key before a civic seal | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_kruger_appointment.dds` | `GFX_idea_brilliant_scientist_kruger_appointment` |
| The Kruger Method | `idea_brilliant_scientist_kruger_method` | Precision compass and calipers around a sealed specimen vial | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_kruger_method.dds` | `GFX_idea_brilliant_scientist_kruger_method` |
| National Scientific Dependence | `idea_brilliant_scientist_national_scientific_dependence` | Amber flask and small gear tethered to a larger institutional gear | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_national_scientific_dependence.dds` | `GFX_idea_brilliant_scientist_national_scientific_dependence` |
| Public Scientific Renaissance | `idea_brilliant_scientist_public_scientific_renaissance` | Laboratory tree with copper roots, laurel leaves, and rising lens-sun | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_public_scientific_renaissance.dds` | `GFX_idea_brilliant_scientist_public_scientific_renaissance` |
| Controlled Secret Compact | `idea_brilliant_scientist_controlled_secret_compact` | Two gloved hands sealing a leather dossier and hidden vial | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_controlled_secret_compact.dds` | `GFX_idea_brilliant_scientist_controlled_secret_compact` |
| Unrestricted Laboratory State | `idea_brilliant_scientist_unrestricted_laboratory_state` | Armored laboratory door opened around a glowing retort and vapor | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_unrestricted_laboratory_state.dds` | `GFX_idea_brilliant_scientist_unrestricted_laboratory_state` |
| Scientific Vacuum | `idea_brilliant_scientist_scientific_vacuum` | Empty bell jar with a matte-black void and dormant instruments | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_scientific_vacuum.dds` | `GFX_idea_brilliant_scientist_scientific_vacuum` |
| Improvised Laboratory State | `idea_brilliant_scientist_improvised_laboratory_state` | Salvaged tin, coils, clamp, retort, and field-tool apparatus | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_improvised_laboratory_state.dds` | `GFX_idea_brilliant_scientist_improvised_laboratory_state` |
| Inherited Project Portfolio | `idea_brilliant_scientist_inherited_project_portfolio` | Leather portfolio carrying lens, coil, vial, and gear relics | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_inherited_project_portfolio.dds` | `GFX_idea_brilliant_scientist_inherited_project_portfolio` |
| Fragmented Command | `idea_brilliant_scientist_fragmented_command` | Cracked brass baton with three disconnected radio nodes | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_fragmented_command.dds` | `GFX_idea_brilliant_scientist_fragmented_command` |
| Experimental Supply Chain | `idea_brilliant_scientist_experimental_supply_chain` | Cargo crates, copper tubing, and a glowing test flask | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_experimental_supply_chain.dds` | `GFX_idea_brilliant_scientist_experimental_supply_chain` |
| Scientific Exodus | `idea_brilliant_scientist_scientific_exodus` | Leather case and glowing flask leaving through a broken doorway | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_scientific_exodus.dds` | `GFX_idea_brilliant_scientist_scientific_exodus` |
| World-threat Project State | `idea_brilliant_scientist_world_threat_project_state` | Dark containment globe-ring wrapped by three crimson project tendrils | `gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_world_threat_project_state.dds` | `GFX_idea_brilliant_scientist_world_threat_project_state` |

## Files created

### Evidence package

- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/manifest.md`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/validation.tsv`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/gfx_handoff.md`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/prompts/016_idea_national_spirit_icon_prompts.md`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/contact_sheets/source_contact_sheet.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/contact_sheets/processed_decoded_contact_sheet.png`

### Source PNGs

- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_kruger_appointment.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_kruger_method.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_national_scientific_dependence.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_public_scientific_renaissance.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_controlled_secret_compact.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_unrestricted_laboratory_state.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_scientific_vacuum.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_improvised_laboratory_state.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_inherited_project_portfolio.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_fragmented_command.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_experimental_supply_chain.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_scientific_exodus.png`
- `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/source_png/idea_brilliant_scientist_world_threat_project_state.png`

### Processed 64x64 PNGs

The same thirteen filenames are present under `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/processed_png/`.

### DDS-decoded PNGs

The same thirteen filenames are present under `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/dds_decoded_png/`.

### Runtime DDS files

The same thirteen stable stems are present as `.dds` files under `gfx/interface/ideas/016_brilliant_scientist/`. Existing `idea_doctor_warren_kruger_stage_*.dds` files were not modified.

## Validation evidence

`validation.tsv` has one row per icon and records SHA-256 hashes for source PNG, processed PNG, runtime DDS, and DDS-decoded PNG. It records generated source dimensions of 1254x1254, processed and decoded dimensions of 64x64, alpha minimum and maximum, transparent-corner checks, DDS magic, header size 124, 32-bit BGRA pixel format fields, texture caps, exact 16512-byte file length, and processed-to-decoded pixel equality.

All thirteen rows report `pixel_equal_processed_decoded=True` and `status=complete`.

The processed and decoded contact sheet was visually inspected over a checkerboard. All icons have transparent unused canvas, centered silhouettes, dark outlines, no white matte, and distinct compositions. The source contact sheet preserves the generated green-screen source evidence and labels every stable stem.

## Exact parent wiring instructions

1. Open the existing Event 016 idea or national-spirit `.gfx` file chosen by the parent and follow its established formatting.
2. Register one `spriteType` per row using the exact `GFX_idea_brilliant_scientist_<stable_stem>` name and exact runtime texture path listed above. A ready-to-copy block for all thirteen sprites is in `docs/assets/016_brilliant_scientist/idea_national_spirit_icons/gfx_handoff.md`.
3. Point each Event 016 idea or national-spirit definition to its matching sprite token. Do not point gameplay at `docs/assets/` paths or contact sheets.
4. Keep these icons separate from Kruger portrait and advisor sprites. Do not overwrite or repurpose existing `idea_doctor_warren_kruger_stage_*.dds` files.
5. Visually review the processed/decoded contact sheet and the in-game spirit surface before committing. If the parent changes a sprite stem or runtime path, update the manifest, validation TSV, and this handoff together.
6. Record the final `.gfx` filename and parent review result in the event plan or durable documentation when wiring is complete.

Ready-to-copy example:

```text
spriteType = {
	name = "GFX_idea_brilliant_scientist_kruger_appointment"
	texturefile = "gfx/interface/ideas/016_brilliant_scientist/idea_brilliant_scientist_kruger_appointment.dds"
}
```

Repeat the same block for the remaining twelve rows with the exact pairings above.

## Simplifications, placeholders, and blockers

No simplifications were made. No placeholder, resize-from-focus, recolor, primitive local drawing, readable generated text, protected medical emblem, modern UI motif, or animation fallback was used. No assets are blocked. The only outstanding work is parent-owned `.gfx` and gameplay wiring plus final in-context visual review.

## Parent integration review

The parent visually reviewed `contact_sheets/processed_decoded_contact_sheet.png` at original resolution and accepted all thirteen compositions for runtime use.

`interface/016_brilliant_scientist_idea_icons.gfx` registers all thirteen exact sprite names and runtime paths. The five Kruger State starting liabilities consume their matching pictures in `common/ideas/016_brilliant_scientist_country_ideas.txt`. The seven mutually exclusive host relationship states and the independent world-threat state consume their matching pictures in `common/ideas/016_brilliant_scientist_host_ideas.txt`.

The host lifecycle is reconciled by `brilliant_scientist_refresh_directorate_idea_lifecycle`. Its priority order, thresholds, modifier tuning, and refresh callers are documented in `docs/events/016_brilliant_scientist/systems/idea_lifecycle.md` and centralized in `common/script_constants/016_brilliant_scientist_idea_constants.txt`.

Parent validation confirmed thirteen unique sprite registrations, thirteen unique runtime paths, all referenced DDS files present, balanced braces in the wired script and GFX files, a UTF-8 BOM on the lifecycle localisation file, and no second positive research-speed source competing with Kruger's advisor trait.
