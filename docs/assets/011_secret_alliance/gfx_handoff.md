# Event 011 Secret Alliance raster GFX handoff

This handoff covers only the seven report images, one news image, and one reveal super-event image created by the generated event-art tranche. Icon, UI, achievement, and animation assets use their separate tranche handoff.

The runtime event script already refers to the report and news sprite names below. The DDS files are ready at the exact paths registered in the Event 011 asset matrix. This subagent did not edit any `.gfx` file.

## Report and news sprites

Suggested target: `interface/011_secret_alliance.gfx`.

```text
spriteTypes = {
	spriteType = {
		name = "GFX_report_event_011_secret_alliance_first_pattern"
		texturefile = "gfx/event_pictures/011_secret_alliance/report_event_first_pattern.dds"
	}
	spriteType = {
		name = "GFX_report_event_011_secret_alliance_missing_courier"
		texturefile = "gfx/event_pictures/011_secret_alliance/report_event_missing_courier.dds"
	}
	spriteType = {
		name = "GFX_report_event_011_secret_alliance_machine_sabotage"
		texturefile = "gfx/event_pictures/011_secret_alliance/report_event_machine_sabotage.dds"
	}
	spriteType = {
		name = "GFX_report_event_011_secret_alliance_safehouse_raid"
		texturefile = "gfx/event_pictures/011_secret_alliance/report_event_safehouse_raid.dds"
	}
	spriteType = {
		name = "GFX_report_event_011_secret_alliance_border_survey"
		texturefile = "gfx/event_pictures/011_secret_alliance/report_event_border_survey.dds"
	}
	spriteType = {
		name = "GFX_report_event_011_secret_alliance_political_attack"
		texturefile = "gfx/event_pictures/011_secret_alliance/report_event_political_attack.dds"
	}
	spriteType = {
		name = "GFX_report_event_011_secret_alliance_turned_channel"
		texturefile = "gfx/event_pictures/011_secret_alliance/report_event_turned_channel.dds"
	}
	spriteType = {
		name = "GFX_news_event_011_secret_alliance_public_coalition"
		texturefile = "gfx/event_pictures/011_secret_alliance/news_event_public_coalition.dds"
	}
}
```

Current event consumers in `events/011_secret_alliance.txt`:

| Sprite | Events |
| --- | --- |
| `GFX_report_event_011_secret_alliance_first_pattern` | `chaosx.nr11.3`, `.9`, `.12`, `.193`, `.196`, `.197` |
| `GFX_report_event_011_secret_alliance_missing_courier` | `chaosx.nr11.6` |
| `GFX_report_event_011_secret_alliance_machine_sabotage` | `chaosx.nr11.7` |
| `GFX_report_event_011_secret_alliance_safehouse_raid` | `chaosx.nr11.11`, `.13`, `.15`, `.194` |
| `GFX_report_event_011_secret_alliance_border_survey` | `chaosx.nr11.5`, `.8`, `.192` |
| `GFX_report_event_011_secret_alliance_political_attack` | `chaosx.nr11.4`, `.10` |
| `GFX_report_event_011_secret_alliance_turned_channel` | `chaosx.nr11.14`, `.16`, `.191`, `.195`, `.198` |
| `GFX_news_event_011_secret_alliance_public_coalition` | `chaosx.nr11.200` |

## Reveal super-event sprite

Append this sprite definition inside the existing `spriteTypes` block in `interface/chaosx_super_events.gfx`; do not create a second root block.

```text
	spriteType = {
		name = "GFX_super_event_011_secret_alliance_public_reveal"
		texturefile = "gfx/super_events/011_secret_alliance/super_event_public_reveal.dds"
	}
```

The super-event research tranche selected slot `73`. The main agent must connect that slot's scripted-localisation image selection to `GFX_super_event_011_secret_alliance_public_reveal` for the hostile-war, pact-controlled, player-forced, and fractured reveal descriptions.

## Asset readiness

| Sprite | Final DDS | Size / format | Status |
| --- | --- | --- | --- |
| `GFX_report_event_011_secret_alliance_first_pattern` | `gfx/event_pictures/011_secret_alliance/report_event_first_pattern.dds` | `210x176`, 32-bit BGRA | ready |
| `GFX_report_event_011_secret_alliance_missing_courier` | `gfx/event_pictures/011_secret_alliance/report_event_missing_courier.dds` | `210x176`, 32-bit BGRA | ready |
| `GFX_report_event_011_secret_alliance_machine_sabotage` | `gfx/event_pictures/011_secret_alliance/report_event_machine_sabotage.dds` | `210x176`, 32-bit BGRA | ready |
| `GFX_report_event_011_secret_alliance_safehouse_raid` | `gfx/event_pictures/011_secret_alliance/report_event_safehouse_raid.dds` | `210x176`, 32-bit BGRA | ready |
| `GFX_report_event_011_secret_alliance_border_survey` | `gfx/event_pictures/011_secret_alliance/report_event_border_survey.dds` | `210x176`, 32-bit BGRA | ready |
| `GFX_report_event_011_secret_alliance_political_attack` | `gfx/event_pictures/011_secret_alliance/report_event_political_attack.dds` | `210x176`, 32-bit BGRA | ready |
| `GFX_report_event_011_secret_alliance_turned_channel` | `gfx/event_pictures/011_secret_alliance/report_event_turned_channel.dds` | `210x176`, 32-bit BGRA | ready |
| `GFX_news_event_011_secret_alliance_public_coalition` | `gfx/event_pictures/011_secret_alliance/news_event_public_coalition.dds` | `397x153`, black-and-white, 32-bit BGRA | ready |
| `GFX_super_event_011_secret_alliance_public_reveal` | `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds` | `457x328`, 32-bit BGRA | ready |

## Reference and processing evidence

The current checkout's missing reference folders and report processor were restored from both local Chaos Redux worktrees documented in `manifest.md`. The processor SHA-256 is `5B51613F391934960A8310268041C66B00FDD31BC12DA2393EB02C8F3DC87BD9` in both copies. The complete prompt, source, processing, rights, reference, and validation record is in `manifest.md` and `notes/validation.md`.

## Uncertainty and blockers

None for asset names, paths, sizes, or output formats. Final `.gfx` and slot wiring are outside this subagent's granted scope and remain with the main implementation agent.
