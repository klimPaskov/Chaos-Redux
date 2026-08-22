# Event016 D’Rhondan art GFX handoff

Asset worker scope is complete for generated flags, report/news scenes, the D’Rhondan faction emblem, and the country identity panel. No `.gfx`, gameplay, localisation, GUI, event, focus, decision, country, or spreadsheet file was edited.

## Parent-owned report sprite definitions

Add the following texture-backed sprites to the existing Event016 report-picture registry or the target `.gfx` file selected by the main agent. Keep the sprite names exact.

```text
spriteType = {
	name = "GFX_report_event_016_dhrondan_craft_authorized"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_craft_authorized.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_envoy_departure"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_envoy_departure.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_planetary_audience"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_planetary_audience.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_pact_return"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_pact_return.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_ufo_landing"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_ufo_landing.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_expedition_failure"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_expedition_failure.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_revolt_warning"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_revolt_warning.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_rebellion"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_rebellion.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_diplomatic_compact"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_diplomatic_compact.dds"
}
spriteType = {
	name = "GFX_report_event_016_dhrondan_special_project_envoy_craft"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_special_project_envoy_craft.dds"
}
```

The first eight tokens are the parent contract for `.40-.47`. The diplomatic compact token is the country-package contract for `.49-.51`.

## Parent-owned news sprite definitions

`.48` uses the exact stable sprite token below. The envoy and rebellion news tokens are proposed for future global news consumers.

```text
spriteType = {
	name = "GFX_news_event_016_dhrondan_sovereignty"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_news_sovereignty.dds"
}
spriteType = {
	name = "GFX_news_event_016_dhrondan_envoy"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_news_envoy.dds"
}
spriteType = {
	name = "GFX_news_event_016_dhrondan_rebellion"
	texturefile = "gfx/event_pictures/016_brilliant_scientist/event016_dhrondan_news_rebellion.dds"
}
```

## Country identity and faction art

Proposed target `.gfx`: the Event016 interface identity registry selected by the main agent. These are full-canvas or alpha-backed interface textures and should not be placed in event-picture registries.

```text
spriteType = {
	name = "GFX_dhrondan_faction_emblem"
	texturefile = "gfx/interface/016_brilliant_scientist/dhrondan_faction_emblem.dds"
}
spriteType = {
	name = "GFX_dhrondan_country_identity_panel"
	texturefile = "gfx/interface/016_brilliant_scientist/dhrondan_country_identity_panel.dds"
}
```

The faction emblem is 128x128 with native transparency. The country identity panel is opaque 512x256 with dark negative space on the left for interface text.

## Flags

Flags are engine filename lookups, not `.gfx` sprites. Use the exact tag/cosmetic names and all three ladders:

- `DHR.dds`, `DHR_IMPERIAL.dds`, `DHR_SYNOD.dds`, `DHR_COVENANT.dds` under `gfx/flags/` at 82x52.
- Same basenames under `gfx/flags/medium/` at 41x26.
- Same basenames under `gfx/flags/small/` at 10x7.

## Ownership boundary

The transparent `sp_dhrondan_envoy_craft` special-project icon at 161x98 and any Event016 achievement completed/grey/not-eligible triplet at 64x64 remain blocked for `chaosx_icon_artist`. The dedicated 210x176 special-project support scene is complete and is not a substitute for that icon surface.
