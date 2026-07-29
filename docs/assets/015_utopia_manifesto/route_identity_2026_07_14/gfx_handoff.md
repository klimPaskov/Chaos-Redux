# Event 015 route-identity GFX handoff

> Current status, `2026-07-15`: all 25 supplied sprites and 16 advisor handles are wired, all five League emblems have Ledger consumers, and the Ledger decision category attaches `utopia_manifesto_ledger_scripted_gui`.

This file is a wiring handoff only. The asset producer did not edit `interface/015_utopia_manifesto.gfx`, `common/characters/015_utopia_manifesto_characters.txt`, or scripted GUI/gameplay files.

## Sprite definitions

Insert the following `spriteType` entries inside the existing `spriteTypes = { ... }` block in `interface/015_utopia_manifesto.gfx`.

### Institutional leaders

```txt
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_household_assembly"
		texturefile = "gfx/leaders/015_utopia_manifesto/leader_household_assembly.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_council_of_callings"
		texturefile = "gfx/leaders/015_utopia_manifesto/leader_council_of_callings.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_board_of_measure"
		texturefile = "gfx/leaders/015_utopia_manifesto/leader_board_of_measure.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_stewardship_council"
		texturefile = "gfx/leaders/015_utopia_manifesto/leader_stewardship_council.dds"
	}
```

These names already exist in `common/characters/015_utopia_manifesto_characters.txt`; no leader-character reference needs renaming.

The four texture files were replaced in place with people-free symbolic establishments generated in the HOI4 painted leader style and processed at `156x210` with explicit `symbolic` metadata and vanilla-style comparison sheets. Empty chambers, route seals, ledgers, instruments, stores, and vacant furniture carry the identity; no person, face, hand, crowd, silhouette, statue, bust, framed portrait, or human shadow appears. The handles and founder/successor sharing remain unchanged.

### Advisors

All sixteen textures below are final `65x67` advisor dossier-card DDS files. Their sprite handles and runtime paths are unchanged by the advisor-pipeline correction, so no `.gfx` or character edit is required for this asset replacement. Each file was made from an independent fictional ImageGen portrait master with a separate head-and-shoulders crop through `retired_advisor_card_processor_REMOVED advisor`. The visible dark frame and paper/seal are also generated overlay assets; the script only crops, grades, angles, derives alpha shadows, composites generated layers, resizes, validates, and exports. None is a resized leader portrait or a programmatically drawn dossier card.

```txt
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_interpreter_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_interpreter.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_general_provisioner_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_general_provisioner.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_secretary_of_callings_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_secretary_of_callings.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_surveyor_of_shores_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_surveyor_of_shores.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_civic_engineer_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_civic_engineer.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_keeper_of_stores_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_keeper_of_stores.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_league_envoy_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_league_envoy.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_advocate_of_limits_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_advocate_of_limits.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_public_auditor_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_public_auditor.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_constitutional_jurist_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_constitutional_jurist.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_council_organizer_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_council_organizer.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_social_workshop_planner_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_social_workshop_planner.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_chief_surveyor_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_chief_surveyor.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_standards_engineer_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_standards_engineer.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_steward_of_service_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_steward_of_service.dds"
	}
	spriteType = {
		name = "GFX_portrait_utopia_manifesto_contract_broker_small"
		texturefile = "gfx/leaders/015_utopia_manifesto/advisors/advisor_utopia_manifesto_contract_broker.dds"
	}
```

### League emblems

These use the stable IDs supplied in the country-package implementation handoff.

```txt
	spriteType = {
		name = "GFX_utopia_manifesto_household_congress_emblem"
		texturefile = "gfx/interface/015_utopia_manifesto/league_emblems/household_congress_emblem.dds"
	}
	spriteType = {
		name = "GFX_utopia_manifesto_congress_of_common_tables_emblem"
		texturefile = "gfx/interface/015_utopia_manifesto/league_emblems/congress_of_common_tables_emblem.dds"
	}
	spriteType = {
		name = "GFX_utopia_manifesto_network_directorate_emblem"
		texturefile = "gfx/interface/015_utopia_manifesto/league_emblems/network_directorate_emblem.dds"
	}
	spriteType = {
		name = "GFX_utopia_manifesto_island_hierarchy_emblem"
		texturefile = "gfx/interface/015_utopia_manifesto/league_emblems/island_hierarchy_emblem.dds"
	}
	spriteType = {
		name = "GFX_utopia_manifesto_plural_compact_emblem"
		texturefile = "gfx/interface/015_utopia_manifesto/league_emblems/plural_compact_emblem.dds"
	}
```

## Character-file advisor handle map

The current `common/characters/015_utopia_manifesto_characters.txt` already uses the handle shown for each advisor. The `65x67` asset correction does not require or authorize a character-file edit.

| Character | Current `small` portrait handle |
| --- | --- |
| `utopia_manifesto_interpreter` | `GFX_portrait_utopia_manifesto_interpreter_small` |
| `utopia_manifesto_general_provisioner` | `GFX_portrait_utopia_manifesto_general_provisioner_small` |
| `utopia_manifesto_secretary_of_callings` | `GFX_portrait_utopia_manifesto_secretary_of_callings_small` |
| `utopia_manifesto_surveyor_of_shores` | `GFX_portrait_utopia_manifesto_surveyor_of_shores_small` |
| `utopia_manifesto_civic_engineer` | `GFX_portrait_utopia_manifesto_civic_engineer_small` |
| `utopia_manifesto_keeper_of_stores` | `GFX_portrait_utopia_manifesto_keeper_of_stores_small` |
| `utopia_manifesto_league_envoy` | `GFX_portrait_utopia_manifesto_league_envoy_small` |
| `utopia_manifesto_advocate_of_limits` | `GFX_portrait_utopia_manifesto_advocate_of_limits_small` |
| `utopia_manifesto_public_auditor` | `GFX_portrait_utopia_manifesto_public_auditor_small` |
| `utopia_manifesto_constitutional_jurist` | `GFX_portrait_utopia_manifesto_constitutional_jurist_small` |
| `utopia_manifesto_council_organizer` | `GFX_portrait_utopia_manifesto_council_organizer_small` |
| `utopia_manifesto_social_workshop_planner` | `GFX_portrait_utopia_manifesto_social_workshop_planner_small` |
| `utopia_manifesto_chief_surveyor` | `GFX_portrait_utopia_manifesto_chief_surveyor_small` |
| `utopia_manifesto_standards_engineer` | `GFX_portrait_utopia_manifesto_standards_engineer_small` |
| `utopia_manifesto_steward_of_service` | `GFX_portrait_utopia_manifesto_steward_of_service_small` |
| `utopia_manifesto_contract_broker` | `GFX_portrait_utopia_manifesto_contract_broker_small` |

The four institutional leader handles are already referenced by eight leader character entries. Each founder/successor pair should continue to share its route's institutional portrait.

## Flag wiring

Flags require no `.gfx` sprite registration. HOI4 resolves the installed TGA files from the cosmetic-tag token and current ideology. Every one of the five cosmetic-tag stems has an unsuffixed file plus deliberate `democratic`, `communism`, `neutrality`, and `fascism` variants at all three engine sizes:

- `gfx/flags/<stem>.tga` — `82x52`
- `gfx/flags/medium/<stem>.tga` — `41x26`
- `gfx/flags/small/<stem>.tga` — `10x7`

The four force-ideology routes intentionally alias only their unsuffixed file to the canonical ideology composition. All other files are independent designs: `21` built-in ImageGen compositions cover the `25` wired stems, and Practical Commonwealth has five distinct compositions. No flag sprite registration or gameplay edit is required.

## League UI consumer

The five stable country flags already exist in `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`:

- `utopia_manifesto_identity_household_congress_emblem`
- `utopia_manifesto_identity_common_tables_emblem`
- `utopia_manifesto_identity_network_directorate_emblem`
- `utopia_manifesto_identity_island_hierarchy_emblem`
- `utopia_manifesto_identity_plural_compact_emblem`

The five sprites are registered in `interface/015_utopia_manifesto.gfx`. `interface/015_utopia_manifesto_ledger.gui` contains one icon widget per emblem, and `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt` exposes the widget matching the five stable country flags. The Ledger category and decisions attach `utopia_manifesto_ledger_scripted_gui`; no fallback image is used.

## Post-wiring check

The corrected package verifies that all sixteen advisor handles resolve in the Event 015 GFX file, all sixteen character entries use those handles rather than `GFX_idea_...` stand-ins, all four leader handles still resolve, all 75 route flag TGAs occupy their engine paths, and all five League emblem widgets have scripted visibility consumers.
