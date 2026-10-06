# CBRN Trait Icon Repair Handoff

Status: asset production complete. Ten exact-size DDS files are installed and strictly decoded. The parent owns the four shared-registry repoints and commit.

The parent-authorized scope comes from the CBRN rows in `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md`. The generated sources and review evidence are staged under the ignored workspace `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/`.

## Review sheets

- `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/contact_sheets/before_after_native.png` shows exact 1x before and candidate pixels.
- `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/contact_sheets/before_after_4x_checker.png` shows each before and candidate enlarged 4x on transparency checkerboard.
- `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/contact_sheets/before_after_4x_dark.png` shows each before and candidate enlarged 4x over a dark UI field.
- `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/contact_sheets/after_native_1x.png` shows the ten candidate PNGs at their native dimensions.
- `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/contact_sheets/source_art_contact.png` shows the original ImageGen sources on transparency checkerboard.
- `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/contact_sheets/vanilla_scientist_traits_contact.png` shows all 22 installed vanilla scientist traits at 4x from decoded installed DDS files.
- `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/contact_sheets/vanilla_commander_traits_4x.png` shows six canonical vanilla commander-trait references at 4x.
- `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/contact_sheets/final_dds_decoded_4x_dark.png` shows final installed DDS decodes at 4x on a dark UI field.

## Reference and consumer evidence

The canonical commander-trait contact sheet was inspected first at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/commander_traits/contact_sheet.png`, then the individual references `trait_adaptable.png`, `trait_commando.png`, `trait_engineer.png`, and `trait_logistics_wizard.png`. Their catalog entries record 23x33 canvases and vanilla sources. The adjacent canonical medal contact sheet was inspected for award-metal context; the commander-trait family is the matching family for these army-leader icons. The selected ImageGen ribbons measure 12-15px across the 23px canvas, matching the 15px ribbon in the installed `trait_adaptable` reference.

Installed vanilla sources were decoded directly from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/traits/`. `interface/unitleaderwindow.gfx:187-189` defines `GFX_trait_infantry_leader` as a 23x33 trait, and lines 676-678 define `GFX_trait_adaptable` as a 23x33 trait. Representative vanilla commander sources have 19-21px-wide by 30-31px-tall visible bounds, with 253-288 pixels at alpha 224 or above on a 23x33 canvas.

The installed scientist family was inspected separately from all 22 DDS files under `gfx/interface/traits/scientist_traits/`. The native canvas is 24x33. `interface/unitleaderwindow.gfx:836-837` points `GFX_scientist_trait_bright` at its 24x33 source, and lines 880-885 show the same family for `scientist_trait_bombs_expert` and `scientist_trait_guidance_systems_expert`. The corrected inhumane source follows the exact plan row: amber-and-gold ribbon over a crisp ivory skull crossed by one steel syringe, with no glow and no magnifier.

The five pre-repair CBRN textures were all 23x33. They had only 26-51 fully opaque pixels each, versus 189-231 in the sampled vanilla commander traits. The selected candidates have 190-275 pixels with alpha at least 224. All ten processed previews have transparent corners and a 1-2px clear margin on every side.

## Asset inventory

The full JSON inventory records source paths, source and output hashes, baseline DDS hashes and backups, prompt paths, exact output paths, dimensions, alpha bounds, margins, sprite identifiers, and final DDS hashes: `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/manifest.json`.

Selected original ImageGen PNGs are in `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/source_png/`; untouched provider outputs and the superseded scientist attempt are in `rawsources/`; prompts are in `prompts/`; exact-size RGBA previews are in `processed_png/`. The source and processed PNG hashes are in the JSON manifest.

The five CBRN medals use original ImageGen sources with genuine alpha requested in their initial generation calls. The four chemical-cylinder agent variants share a gas-mask medal design and have distinct chlorine yellow-green, phosgene blue-gray, mustard yellow, and lewisite rust ribbons. The generic `gfx/interface/traits/trait_chemical_commander.dds` remains unchanged.

The first scientist generation included unrequested crossed bones, and the focused edit that removed them retained a ribbon that was too wide. Both originals remain untouched in `rawsources/` with their prompts and hashes. The selected fresh ImageGen source has the approved narrow ribbon and the skull-and-syringe emblem.

## Preview processing

The generated PNGs were cropped only to each source's alpha bounding box, resized with premultiplied RGBA Lanczos filtering, and centered on the exact 23x33 or 24x33 target canvas. A few previews received a one-pixel recenter or small proportional fitting adjustment to retain the complete art inside the required 1-2px margins; every adjustment is listed per asset in the JSON inventory. The alpha channel is retained, and all previews have transparent outer corners. The ten final DDS files have one-mip, 32-bit uncompressed BGRA headers and decode pixel-for-pixel to their processed PNGs. Six replaced baseline DDS files are preserved byte-for-byte under `docs/assets/chaos_warfare_system/2026-10-06_gfx_traits/original_dds/`. No background removal, matte repair, color spill cleanup, component layer, or opaque canvas was used.

## Registry handoff for the four new agent files

Apply these exact texture paths to the existing four sprite entries in `interface/chaosx_traits.gfx`:

```text
spriteType = {
	name = "GFX_trait_chemical_cylinder_active_chlorine"
	texturefile = "gfx/interface/traits/cbrn/trait_chemical_cylinder_active_chlorine.dds"
}
spriteType = {
	name = "GFX_trait_chemical_cylinder_active_phosgene"
	texturefile = "gfx/interface/traits/cbrn/trait_chemical_cylinder_active_phosgene.dds"
}
spriteType = {
	name = "GFX_trait_chemical_cylinder_active_mustard"
	texturefile = "gfx/interface/traits/cbrn/trait_chemical_cylinder_active_mustard.dds"
}
spriteType = {
	name = "GFX_trait_chemical_cylinder_active_lewisite"
	texturefile = "gfx/interface/traits/cbrn/trait_chemical_cylinder_active_lewisite.dds"
}
```

Keep `GFX_trait_chemical_cylinder_active` wired to the existing generic `gfx/interface/traits/trait_chemical_commander.dds`. The existing five CBRN sprite entries and `GFX_scientist_trait_inhumane` already use the parent-provided target paths listed in the JSON inventory.

## Worker handoff boundary

At worker delivery, the four registry repoints above remained for the parent to apply in `interface/chaosx_traits.gfx`; their application is recorded below. No GFX or GUI files were edited by this worker. The generic `GFX_trait_chemical_cylinder_active` continues to use `gfx/interface/traits/trait_chemical_commander.dds`, whose SHA-256 is unchanged. Runtime target sizes, alpha bounds, pixel equality, baseline backups, and final DDS hashes are recorded in the JSON manifest. No gameplay, localisation, or other asset files were changed.

## Parent integration

Disposition: implemented and parent accepted under the October 6 graphics-repair task.
The parent reviewed the ribbon-adjusted native/checker/dark sheets and final strict-decoded DDS comparison.
Four exact texture paths are repointed in the shared trait registry; the generic cylinder-active entry keeps its original texture and hash.
The five CBRN medals and scientist icon retain their existing identities and paths.
The adjacent final manifest records source lineage, native family evidence and final hashes; raw studies remain in the ignored traits workspace while acceptance is pending.
The orchestrator should inspect all ten icons beside installed commander/scientist traits and confirm four distinct agent ribbons, clean edges and readable medal symbols at native scale.
