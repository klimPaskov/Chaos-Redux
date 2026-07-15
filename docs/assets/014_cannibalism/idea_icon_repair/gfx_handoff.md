# Event 014 idea-icon GFX handoff

## Wiring state

Root-agent wiring is complete in `interface/014_cannibalism.gfx:152-159`. The asset worker did not edit the `.gfx` file. The eight definitions follow the HOI4 idea-picture convention: each gameplay `picture = cannibalism_...` resolves to `GFX_idea_cannibalism_...`.

| Related idea / picture | Sprite | Runtime DDS | Wiring |
|---|---|---|---|
| `cannibalism_wendigo_conjoined_hunger` | `GFX_idea_cannibalism_wendigo_conjoined_hunger` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_conjoined_hunger.dds` | confirmed at line 152 |
| `cannibalism_wendigo_winter_feeding_network` | `GFX_idea_cannibalism_wendigo_winter_feeding_network` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_winter_feeding_network.dds` | confirmed at line 153 |
| `cannibalism_wendigo_locked_terminal_form` | `GFX_idea_cannibalism_wendigo_locked_terminal_form` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_locked_terminal_form.dds` | confirmed at line 154 |
| `cannibalism_liberated_feeding_states` | `GFX_idea_cannibalism_liberated_feeding_states` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_liberated_feeding_states.dds` | confirmed at line 155 |
| `cannibalism_identification_and_burial_emergency` | `GFX_idea_cannibalism_identification_and_burial_emergency` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_identification_and_burial_emergency.dds` | confirmed at line 156 |
| `cannibalism_broken_military_trust` | `GFX_idea_cannibalism_broken_military_trust` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_broken_military_trust.dds` | confirmed at line 157 |
| `cannibalism_rebuilt_supply_discipline` | `GFX_idea_cannibalism_rebuilt_supply_discipline` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_rebuilt_supply_discipline.dds` | confirmed at line 158 |
| `cannibalism_permanent_vigilance` | `GFX_idea_cannibalism_permanent_vigilance` | `gfx/interface/ideas/014_cannibalism/idea_cannibalism_permanent_vigilance.dds` | confirmed at line 159 |

## Verified definitions

```text
	spriteType = { name = "GFX_idea_cannibalism_wendigo_conjoined_hunger" texturefile = "gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_conjoined_hunger.dds" }
	spriteType = { name = "GFX_idea_cannibalism_wendigo_winter_feeding_network" texturefile = "gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_winter_feeding_network.dds" }
	spriteType = { name = "GFX_idea_cannibalism_wendigo_locked_terminal_form" texturefile = "gfx/interface/ideas/014_cannibalism/idea_cannibalism_wendigo_locked_terminal_form.dds" }
	spriteType = { name = "GFX_idea_cannibalism_liberated_feeding_states" texturefile = "gfx/interface/ideas/014_cannibalism/idea_cannibalism_liberated_feeding_states.dds" }
	spriteType = { name = "GFX_idea_cannibalism_identification_and_burial_emergency" texturefile = "gfx/interface/ideas/014_cannibalism/idea_cannibalism_identification_and_burial_emergency.dds" }
	spriteType = { name = "GFX_idea_cannibalism_broken_military_trust" texturefile = "gfx/interface/ideas/014_cannibalism/idea_cannibalism_broken_military_trust.dds" }
	spriteType = { name = "GFX_idea_cannibalism_rebuilt_supply_discipline" texturefile = "gfx/interface/ideas/014_cannibalism/idea_cannibalism_rebuilt_supply_discipline.dds" }
	spriteType = { name = "GFX_idea_cannibalism_permanent_vigilance" texturefile = "gfx/interface/ideas/014_cannibalism/idea_cannibalism_permanent_vigilance.dds" }
```

## Review evidence

- Contact sheet: `docs/assets/014_cannibalism/idea_icon_repair/contact_sheets/event014_idea_icon_repair_contact_sheet.png`
- Manifest: `docs/assets/014_cannibalism/idea_icon_repair/manifest.md`
- Hash ledger: `docs/assets/014_cannibalism/idea_icon_repair/hashes.sha256`
- Remaining GFX uncertainty: none
- Blocked or needs-review assets: none
