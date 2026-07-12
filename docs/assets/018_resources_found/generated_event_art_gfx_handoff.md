# Event 018 Raster GFX Handoff

This handoff is intentionally registration-only. The generated-art worker did not edit shared `.gfx`, `.gui`, gameplay, or localisation files.

## Report and news sprites

Add the following declarations inside the existing `spriteTypes = { ... }` block in `interface/018_resources_found.gfx`:

```txt
	spriteType = { name = "GFX_report_event_018_resource_discovery" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_resource_discovery.dds" }
	spriteType = { name = "GFX_report_event_018_compound_field" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_compound_field.dds" }
	spriteType = { name = "GFX_report_event_018_sick_workings" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_sick_workings.dds" }
	spriteType = { name = "GFX_report_event_018_missing_shift" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_missing_shift.dds" }
	spriteType = { name = "GFX_report_event_018_first_evidence" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_first_evidence.dds" }
	spriteType = { name = "GFX_report_event_018_perimeter_breach" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_perimeter_breach.dds" }
	spriteType = { name = "GFX_report_event_018_evacuation" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_evacuation.dds" }
	spriteType = { name = "GFX_report_event_018_monster_hunt" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_monster_hunt.dds" }
	spriteType = { name = "GFX_report_event_018_full_seal" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_full_seal.dds" }
	spriteType = { name = "GFX_report_event_018_anchor_cleanup" texturefile = "gfx/event_pictures/018_resources_found/report_event_018_anchor_cleanup.dds" }

	spriteType = { name = "GFX_news_event_018_global_resource_field" texturefile = "gfx/event_pictures/news/018_resources_found/news_event_018_global_resource_field.dds" }
	spriteType = { name = "GFX_news_event_018_border_crisis" texturefile = "gfx/event_pictures/news/018_resources_found/news_event_018_border_crisis.dds" }
	spriteType = { name = "GFX_news_event_018_public_attack" texturefile = "gfx/event_pictures/news/018_resources_found/news_event_018_public_attack.dds" }
	spriteType = { name = "GFX_news_event_018_cave_country_emergence" texturefile = "gfx/event_pictures/news/018_resources_found/news_event_018_cave_country_emergence.dds" }
	spriteType = { name = "GFX_news_event_018_regional_containment" texturefile = "gfx/event_pictures/news/018_resources_found/news_event_018_regional_containment.dds" }
	spriteType = { name = "GFX_news_event_018_global_defeat" texturefile = "gfx/event_pictures/news/018_resources_found/news_event_018_global_defeat.dds" }
```

These sprite IDs already appear in `events/018_random_resource.txt` and `events/_chaosx_news.txt`.

## Super-event sprites

Add these declarations inside `spriteTypes = { ... }` in `interface/chaosx_super_events.gfx`:

```txt
	spriteType = {
		name = "GFX_super_event_018_cave_emergence"
		texturefile = "gfx/super_events/018_resources_found/super_event_018_cave_emergence.dds"
	}
	spriteType = {
		name = "GFX_super_event_018_world_end"
		texturefile = "gfx/super_events/018_resources_found/super_event_018_world_end.dds"
	}
	spriteType = {
		name = "GFX_super_event_018_global_defeat"
		texturefile = "gfx/super_events/018_resources_found/super_event_018_global_defeat.dds"
	}
```

`common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` already maps display values `82`, `83`, and `84` to these three sprite IDs.

## Character portrait sprites

Add these declarations inside `spriteTypes = { ... }` in `interface/chaosx_characters.gfx`:

```txt
	spriteType = {
		name = GFX_portrait_DHO_vhorruk
		texturefile = "gfx/leaders/018_resources_found/portrait_DHO_vhorruk.dds"
	}
	frameAnimatedSpriteType = {
		name = GFX_portrait_DHO_vhorruk_animated
		texturefile = "gfx/leaders/018_resources_found/portrait_DHO_vhorruk_animated.dds"
		noOfFrames = 8
		animation_rate_fps = 4
		looping = yes
		play_on_show = yes
		pause_on_loop = 0.0
		alwaystransparent = yes
	}

	spriteType = {
		name = GFX_portrait_DHO_thessik
		texturefile = "gfx/leaders/018_resources_found/portrait_DHO_thessik.dds"
	}
	spriteType = {
		name = GFX_portrait_DHO_thessik_small
		texturefile = "gfx/leaders/018_resources_found/portrait_DHO_thessik_small.dds"
	}
	spriteType = {
		name = GFX_portrait_DHO_orrukesh
		texturefile = "gfx/leaders/018_resources_found/portrait_DHO_orrukesh.dds"
	}
	spriteType = {
		name = GFX_portrait_DHO_orrukesh_small
		texturefile = "gfx/leaders/018_resources_found/portrait_DHO_orrukesh_small.dds"
	}
	spriteType = {
		name = GFX_portrait_DHO_khalvek
		texturefile = "gfx/leaders/018_resources_found/portrait_DHO_khalvek.dds"
	}
	spriteType = {
		name = GFX_portrait_DHO_khalvek_small
		texturefile = "gfx/leaders/018_resources_found/portrait_DHO_khalvek_small.dds"
	}
```

`common/characters/018_resources_found_cave_characters.txt` already uses all seven static/commander sprite names. Keep the character's `large = GFX_portrait_DHO_vhorruk` mapping static: this is the safe country-leader presentation surface.

For animated event-log presentation, the Event 018 branch in `GetEventsLogSelectedEvolutionPortrait` currently returns `GFX_portrait_DHO_vhorruk`. Change only that branch's `localization_key` to `GFX_portrait_DHO_vhorruk_animated`. The event-log dynamic sprite consumer already supports `frameAnimatedSpriteType`, as proven by its existing Buddha Mandate, Empty Seat, and Zol world-end branches.

## Flags

Flags require no `.gfx` registration. The engine resolves these exact final names:

```text
gfx/flags/DHO.tga
gfx/flags/DHO_democratic.tga
gfx/flags/DHO_fascism.tga
gfx/flags/DHO_communism.tga
gfx/flags/DHO_neutrality.tga
gfx/flags/DHO_WORLD_BELOW.tga
```

Each name has a matching file under `gfx/flags/medium/` and `gfx/flags/small/`. The world-end cosmetic identity is `DHO_WORLD_BELOW`, matching the implemented `set_cosmetic_tag`; do not register or reference `DHO_WORLD_END`.

## Dimensions and formats

| Family | Runtime dimensions | Format |
|---|---:|---|
| Report event | `210x176` | one-mip 32-bit BGRA DDS, alpha corners |
| News event | `397x153` | one-mip 32-bit BGRA DDS from true-grayscale PNG |
| Super event | `457x328` | one-mip 32-bit BGRA DDS |
| Large portrait | `156x210` | one-mip 32-bit BGRA DDS |
| Commander small | `50x67` | one-mip 32-bit BGRA DDS |
| Vhorruk sheet | `1248x210` | one-mip 32-bit BGRA DDS, 8 horizontal frames |
| Flag root | `82x52` | uncompressed 32-bit bottom-origin TGA |
| Flag medium | `41x26` | uncompressed 32-bit bottom-origin TGA |
| Flag small | `10x7` | uncompressed 32-bit bottom-origin TGA |

## Remaining integration work

Only the parent-owned registrations and the one animated event-log key switch above remain. No asset filename, dimension, format, or cosmetic-tag uncertainty remains.
