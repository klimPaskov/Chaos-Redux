# Event 014 Warlord Portrait GFX and Character Handoff

Batch: `E14-POR-WARLORD-01`

Disposition: eight final portrait DDS files are ready at the exact stable runtime paths. This asset tranche did not edit `.gfx`, gameplay, character, portrait-pool, or localisation files.

## Exact sprite ledger

The parent confirms that live leader effects expect these exact sprite names. They must remain stable.

| Slot | Exact sprite | Final texture | Size / format | Origin assignment | Status |
| --- | --- | --- | --- | --- | --- |
| CBA | `GFX_portrait_CBA_warlord` | `gfx/leaders/014_cannibalism/leader_CBA_warlord.dds` | `156x210`, BGRA DDS | Island Host candidate 1 | ready |
| CBB | `GFX_portrait_CBB_warlord` | `gfx/leaders/014_cannibalism/leader_CBB_warlord.dds` | `156x210`, BGRA DDS | Island Host candidate 2 | ready |
| CBC | `GFX_portrait_CBC_warlord` | `gfx/leaders/014_cannibalism/leader_CBC_warlord.dds` | `156x210`, BGRA DDS | Siege Commune candidate 1 | ready |
| CBD | `GFX_portrait_CBD_warlord` | `gfx/leaders/014_cannibalism/leader_CBD_warlord.dds` | `156x210`, BGRA DDS | Siege Commune candidate 2 | ready |
| CBE | `GFX_portrait_CBE_warlord` | `gfx/leaders/014_cannibalism/leader_CBE_warlord.dds` | `156x210`, BGRA DDS | March Host candidate 1 | ready |
| CBF | `GFX_portrait_CBF_warlord` | `gfx/leaders/014_cannibalism/leader_CBF_warlord.dds` | `156x210`, BGRA DDS | March Host candidate 2 | ready |
| CBG | `GFX_portrait_CBG_warlord` | `gfx/leaders/014_cannibalism/leader_CBG_warlord.dds` | `156x210`, BGRA DDS | Prison Host candidate 1 | ready |
| CBH | `GFX_portrait_CBH_warlord` | `gfx/leaders/014_cannibalism/leader_CBH_warlord.dds` | `156x210`, BGRA DDS | Prison Host candidate 2 | ready |

## Ready-to-copy sprite definitions

Append these entries inside the existing `spriteTypes = { ... }` block in `interface/014_cannibalism.gfx`. Do not create a second root block.

```text
	spriteType = {
		name = "GFX_portrait_CBA_warlord"
		texturefile = "gfx/leaders/014_cannibalism/leader_CBA_warlord.dds"
	}
	spriteType = {
		name = "GFX_portrait_CBB_warlord"
		texturefile = "gfx/leaders/014_cannibalism/leader_CBB_warlord.dds"
	}
	spriteType = {
		name = "GFX_portrait_CBC_warlord"
		texturefile = "gfx/leaders/014_cannibalism/leader_CBC_warlord.dds"
	}
	spriteType = {
		name = "GFX_portrait_CBD_warlord"
		texturefile = "gfx/leaders/014_cannibalism/leader_CBD_warlord.dds"
	}
	spriteType = {
		name = "GFX_portrait_CBE_warlord"
		texturefile = "gfx/leaders/014_cannibalism/leader_CBE_warlord.dds"
	}
	spriteType = {
		name = "GFX_portrait_CBF_warlord"
		texturefile = "gfx/leaders/014_cannibalism/leader_CBF_warlord.dds"
	}
	spriteType = {
		name = "GFX_portrait_CBG_warlord"
		texturefile = "gfx/leaders/014_cannibalism/leader_CBG_warlord.dds"
	}
	spriteType = {
		name = "GFX_portrait_CBH_warlord"
		texturefile = "gfx/leaders/014_cannibalism/leader_CBH_warlord.dds"
	}
```

## Character binding

Vanilla `create_country_leader` accepts a sprite token in its `picture` field. The existing live leader effects should bind the corresponding slot with:

| Slot | Required line in that slot's leader creation block |
| --- | --- |
| CBA | `picture = GFX_portrait_CBA_warlord` |
| CBB | `picture = GFX_portrait_CBB_warlord` |
| CBC | `picture = GFX_portrait_CBC_warlord` |
| CBD | `picture = GFX_portrait_CBD_warlord` |
| CBE | `picture = GFX_portrait_CBE_warlord` |
| CBF | `picture = GFX_portrait_CBF_warlord` |
| CBG | `picture = GFX_portrait_CBG_warlord` |
| CBH | `picture = GFX_portrait_CBH_warlord` |

If the implementation instead promotes database characters, use the same sprite inside each character's civilian portrait block:

```text
		portraits = {
			civilian = {
				large = GFX_portrait_CBA_warlord
			}
		}
```

Replace only the slot token for CBB through CBH. Character ids are not frozen by the asset specification, so this handoff does not invent them.

## Gender and naming contract

- Every portrait is male-presenting.
- Every dynamic incarnation must select a personal name from the actual origin state's male regional pool and must use male metadata.
- Do not pair these portraits with a female name pool or `female = yes`.
- Optional epithets in `manifest.md` are region-neutral writing cues only. They may follow a locally plausible male personal name; they are not fixed localisation keys and must not replace the regional name selection.
- No player-facing name, tooltip, portrait metadata, or default texture should expose the concealed Event 014 leader before the public-reveal gate.

## Flag blocker

No CBA-CBH flag file accompanies this handoff. The current gap map marks the warlord and unified flag batches blocked on the unresolved cosmetic-tag ledger. The recommended base-family path pattern is documented in `manifest.md`; the parent must reconcile and accept the final family tokens before any flag-generation tranche begins.

## Remaining parent actions

1. Add the eight exact sprite definitions to the existing `interface/014_cannibalism.gfx` root block.
2. Verify each live CBA-CBH leader creation effect uses the matching exact `picture` sprite.
3. Keep male regional name-pool selection aligned with each spawn state's actual language region.
4. Reconcile the Event 014 flag/cosmetic-tag ledger before requesting flag art.

There is no uncertainty in portrait filenames, texture paths, sprite names, dimensions, or gender presentation.
