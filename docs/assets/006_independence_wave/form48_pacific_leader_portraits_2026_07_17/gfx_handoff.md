# FORM-48 Pacific country-leader GFX handoff

## Exact runtime contract

| Sprite | Texture | Character consumer |
|---|---|---|
| `GFX_portrait_HBX_independence_wave_civic_convention` | `gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds` | `HBX_independence_wave_civic_convention_chair` |
| `GFX_portrait_FSM_independence_wave_inter_island_congress_chair` | `gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds` | `FSM_independence_wave_inter_island_congress_chair` |

The registrations already exist in parent-owned
`interface/006_independence_wave_pacific_portraits.gfx`:

```text
spriteTypes = {
	spriteType = {
		name = "GFX_portrait_HBX_independence_wave_civic_convention"
		texturefile = "gfx/leaders/006_independence_wave/portrait_HBX_independence_wave_civic_convention.dds"
	}
	spriteType = {
		name = "GFX_portrait_FSM_independence_wave_inter_island_congress_chair"
		texturefile = "gfx/leaders/006_independence_wave/portrait_FSM_independence_wave_inter_island_congress_chair.dds"
	}
}
```

The live `civilian.large` consumers already exist in parent-owned
`common/characters/006_independence_wave_pacific_characters.txt`, and both
characters declare `gender = male`. Player-facing names are Daniel Mercer and
Elias Kihleng. The asset lane verified these bindings but did not edit any
interface, character, effect, trigger, history, focus, decision, or localisation
file.

## Asset state

- Both runtime textures are legacy `156x210` uncompressed BGRA DDS files.
- Each runtime file is byte-identical to its retained `final_dds/` copy.
- Each decoded DDS is pixel-identical to the independently approved PNG.
- Parent reviewer `/root` approved the exact candidate and review-sheet hashes;
  the separate record is `notes/visual_review.md`.
- BAY and RHI protected portraits remain hash-identical; see `manifest.md` and
  `notes/validation.json`.

No adviser role or adviser visual belongs in this handoff. No advisor portrait,
`65x67` card, small sprite, dossier frame, or advisor texture was created or
registered.
