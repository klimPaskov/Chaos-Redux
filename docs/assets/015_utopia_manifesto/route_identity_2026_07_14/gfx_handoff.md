# Event 015 route-identity GFX handoff

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

### Advisors

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

## Character-file replacements

Replace only the `small =` handle inside each listed advisor's existing `portraits` block in `common/characters/015_utopia_manifesto_characters.txt`.

| Character | Replace current idea-icon handle with |
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

The four force-ideology routes intentionally alias only their unsuffixed file to the canonical ideology composition. All other ideology files are independent designs. Practical Commonwealth's five-file family is unchanged.

## League UI consumer

The five stable country flags already exist in `common/scripted_effects/015_utopia_manifesto_identity_effects.txt`:

- `utopia_manifesto_identity_household_congress_emblem`
- `utopia_manifesto_identity_common_tables_emblem`
- `utopia_manifesto_identity_network_directorate_emblem`
- `utopia_manifesto_identity_island_hierarchy_emblem`
- `utopia_manifesto_identity_plural_compact_emblem`

No current Event 015 interface or scripted-GUI consumer resolves those state flags to a sprite. The parent should register the five sprites above, then select the matching sprite in the intended country-details, ledger, or league UI surface. The asset package does not guess a consumer or add a fallback image.

## Post-wiring check

After the parent edit, verify that every one of the four existing leader handles and sixteen new advisor handles resolves exactly once in the Event 015 GFX file, that none of the sixteen character entries still uses a `GFX_idea_...` stand-in, and that all five stable league handles have a real UI consumer rather than only a definition.
