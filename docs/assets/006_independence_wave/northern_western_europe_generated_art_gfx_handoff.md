# Event 006 northern and western Europe generated-art GFX handoff

## Ownership boundary

This handoff supplies final textures and copy-ready registration/portrait
fragments only. It does not edit `.gfx`, characters, country history, route
logic, localisation, state ownership, or other gameplay files. Register these
sprites in `interface/006_independence_wave_region_01_portraits.gfx`, retaining
the names and paths below.

The flag triplets require no `spriteType` registration. HOI4 discovers the
unsuffixed `ACX`, `AFX`, `AGX`, and `AJX` files by exact path under
`gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

There is no standalone AEX flag family. AEX remains a vanilla `BEL_flanders`
cosmetic overlay; the retired AEX runtime triplet and generated previews must
not be recreated. Retained AEX portrait staging below does not change that flag
boundary.

The five officer `_small` texture paths below now resolve to independent
`65x67` dossier cards. Their current source of truth is
`army_small_dossier_correction_2026_07_15/gfx_handoff.md`; the names and paths
in this copy-ready block remain valid.

## Copy-ready sprite registrations

```txt
spriteTypes = {
	spriteType = {
		name = "GFX_portrait_ACX_cornish_port_and_mines_committee"
		texturefile = "gfx/leaders/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee.dds"
	}
	spriteType = {
		name = "GFX_portrait_ACX_cornish_coastal_commander"
		texturefile = "gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander.dds"
	}
	spriteType = {
		name = "GFX_portrait_ACX_cornish_coastal_commander_small"
		texturefile = "gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander_small.dds"
	}

	spriteType = {
		name = "GFX_portrait_AEX_flemish_civil_industrial_board"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AEX_flemish_civil_industrial_board.dds"
	}
	spriteType = {
		name = "GFX_portrait_AEX_flemish_industrial_security_commander"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander.dds"
	}
	spriteType = {
		name = "GFX_portrait_AEX_flemish_industrial_security_commander_small"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AEX_flemish_industrial_security_commander_small.dds"
	}

	spriteType = {
		name = "GFX_portrait_AFX_walloon_provisional_assembly"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds"
	}
	spriteType = {
		name = "GFX_portrait_AFX_walloon_reserve_commander"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds"
	}
	spriteType = {
		name = "GFX_portrait_AFX_walloon_reserve_commander_small"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander_small.dds"
	}

	spriteType = {
		name = "GFX_portrait_AGX_friesland_coastal_council"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds"
	}
	spriteType = {
		name = "GFX_portrait_AGX_friesland_coastal_commander"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds"
	}
	spriteType = {
		name = "GFX_portrait_AGX_friesland_coastal_commander_small"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander_small.dds"
	}

	spriteType = {
		name = "GFX_portrait_AJX_friedrich_hoffmann"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds"
	}
	spriteType = {
		name = "GFX_portrait_AJX_karl_becker"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds"
	}
	spriteType = {
		name = "GFX_portrait_AJX_karl_becker_small"
		texturefile = "gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner_small.dds"
	}
}
```

## Institutional character portrait fragments

Merge these entries into the package-owned `characters = { ... }` block and add
only the route roles, ideology, traits, and availability approved by the country
package. The mixed-gender group image represents an institution; do not add an
individual biography or individual gender metadata.

```txt
ACX_cornish_port_and_mines_committee = {
	name = ACX_cornish_port_and_mines_committee
	portraits = {
		civilian = {
			large = GFX_portrait_ACX_cornish_port_and_mines_committee
		}
	}
}

AEX_flemish_civil_industrial_board = {
	name = AEX_flemish_civil_industrial_board
	portraits = {
		civilian = {
			large = GFX_portrait_AEX_flemish_civil_industrial_board
		}
	}
}

AFX_walloon_provisional_assembly = {
	name = AFX_walloon_provisional_assembly
	portraits = {
		civilian = {
			large = GFX_portrait_AFX_walloon_provisional_assembly
		}
	}
}

AGX_friesland_coastal_council = {
	name = AGX_friesland_coastal_council
	portraits = {
		civilian = {
			large = GFX_portrait_AGX_friesland_coastal_council
		}
	}
}

AJX_friedrich_hoffmann = {
	name = AJX_friedrich_hoffmann
	portraits = {
		civilian = {
			large = GFX_portrait_AJX_friedrich_hoffmann
		}
	}
}
```

Required English localisation values for those character keys:

| Key | English value |
|---|---|
| `ACX_cornish_port_and_mines_committee` | Cornish Port and Mines Security Committee |
| `AEX_flemish_civil_industrial_board` | Flemish Civil-Industrial Security Board |
| `AFX_walloon_provisional_assembly` | Walloon Provisional Assembly |
| `AGX_friesland_coastal_council` | Friesland Coastal Council |
| `AJX_friedrich_hoffmann` | Friedrich Hoffmann |

## Officer character portrait fragments

These are male-presenting fictional officers. The default male character setting
is required; do not set `female = yes`. The `small` sprite is included because
vanilla's `portraits = { army = { ... } }` precedent supplies both sizes for
corps commanders and the officer corps.

```txt
ACX_cornish_coastal_commander = {
	name = ACX_cornish_coastal_commander
	portraits = {
		army = {
			large = GFX_portrait_ACX_cornish_coastal_commander
			small = GFX_portrait_ACX_cornish_coastal_commander_small
		}
	}
}

AEX_flemish_industrial_security_commander = {
	name = AEX_flemish_industrial_security_commander
	portraits = {
		army = {
			large = GFX_portrait_AEX_flemish_industrial_security_commander
			small = GFX_portrait_AEX_flemish_industrial_security_commander_small
		}
	}
}

AFX_walloon_reserve_commander = {
	name = AFX_walloon_reserve_commander
	portraits = {
		army = {
			large = GFX_portrait_AFX_walloon_reserve_commander
			small = GFX_portrait_AFX_walloon_reserve_commander_small
		}
	}
}

AGX_friesland_coastal_commander = {
	name = AGX_friesland_coastal_commander
	portraits = {
		army = {
			large = GFX_portrait_AGX_friesland_coastal_commander
			small = GFX_portrait_AGX_friesland_coastal_commander_small
		}
	}
}

AJX_karl_becker = {
	name = AJX_karl_becker
	portraits = {
		army = {
			large = GFX_portrait_AJX_karl_becker
			small = GFX_portrait_AJX_karl_becker_small
		}
	}
}
```

Required English localisation values for the officer keys:

| Key | English value |
|---|---|
| `ACX_cornish_coastal_commander` | Thomas Trevorrow |
| `AEX_flemish_industrial_security_commander` | Hendrik Vermeulen |
| `AFX_walloon_reserve_commander` | Marcel Delcourt |
| `AGX_friesland_coastal_commander` | Sjoerd Hoekstra |
| `AJX_karl_becker` | Karl Becker |

## Route-use locks

| Character | Allowed use | Blocked or forbidden use |
|---|---|---|
| `ACX_cornish_port_and_mines_committee` | future ACX civic opening after geography is approved | do not wire while ACX lacks unique Cornwall geography; not a real-person leader |
| `ACX_cornish_coastal_commander` | future ACX harbor/coastal command roster after geography is approved | do not wire while ACX is geography-blocked; not a historical officer |
| `AEX_flemish_civil_industrial_board` | future AEX civil/industrial opening after the protected anchor is approved | do not wire while AEX lacks a protected Brussels/Flanders anchor; not a real-person leader |
| `AEX_flemish_industrial_security_commander` | future AEX industrial-security command roster after the anchor is approved | do not wire while AEX is anchor-blocked; not a historical officer |
| `AFX_walloon_provisional_assembly` | accepted AFX constitutional, labor, and patron civil openings | emergency military command role |
| `AFX_walloon_reserve_commander` | accepted AFX emergency military command and command roster | universal civil opening or a historical-person claim |
| `AGX_friesland_coastal_council` | accepted AGX civil, cultural, labor, and patron openings | commander role or pan-Frisian authority |
| `AGX_friesland_coastal_commander` | accepted AGX command roster and coastal-security role | universal civil opening or pan-Frisian authority |
| `AJX_friedrich_hoffmann` | AJX constitutional, labor, patron, and municipal-neutral civil openings | military-government role or a historical-person claim |
| `AJX_karl_becker` | AJX industrial-security command roster | country-leader role or a historical-officer claim |

## Handoff-only regional name-pool recommendations

These snippets follow vanilla `common/names/00_names.txt`. They are recommendations
for male-generated names that visually agree with this package's male officer
art; they are not written to gameplay files by this tranche. If a package later
adds female generic officers, it must add a separate female pool and matching
female-presenting art instead of reusing these portraits.

```txt
ACX = {
	male = {
		names = { John William Thomas Richard Pascoe }
	}
	surnames = { Trevorrow Penrose Tregenza Pascoe }
}

AEX = {
	male = {
		names = { Jan Pieter Hendrik Karel }
	}
	surnames = { "De Smet" Vermeulen "Van den Broeck" Peeters }
}

AFX = {
	male = {
		names = { Jules Marcel Léon Henri }
	}
	surnames = { Dubois Lambert Leclercq Delcourt }
}

AGX = {
	male = {
		names = { Sjoerd Douwe Tjalling Pieter }
	}
	surnames = { "de Vries" Dijkstra Hoekstra Visser }
}

AJX = {
	male = {
		names = { Karl Friedrich Wilhelm Otto }
	}
	surnames = { Becker Schmitt Wagner Hoffmann }
}
```

## Validation and review references

The actual post-conversion large runtime portraits are shown in
`contact_sheets/006_nwe_generated_final_dds_decoded_contact_sheet.png`. The old
`contact_sheets/006_nwe_generated_officer_small_dds_decoded_contact_sheet.png`
is pre-correction evidence only. Current native and enlarged `_small`
comparisons, retained DDS files, decoded pixels, exact hashes, and header checks
are in `army_small_dossier_correction_2026_07_15/`.
The actual TGA files at all three engine sizes are shown in
`contact_sheets/006_nwe_generated_flags_contact_sheet.png`; cited-design versus
ImageGen versus flat-master evidence is shown in
`contact_sheets/006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png`.
Full asset identity, prompts, route boundaries, reproduction steps, and hashes are in
`northern_western_europe_generated_art_manifest.md`.
