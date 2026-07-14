# GFX handoff

## Ready asset

- Stable decision id: `bio_designate_strategic_raid_staging_state`
- Intended sprite: `GFX_decision_bio_designate_strategic_raid_staging_state`
- Final texture: `gfx/interface/decisions/biowarfare/bio_designate_strategic_raid_staging_state.dds`
- Target size: `32x32`
- Alpha: real RGBA alpha preserved through PNG and legacy uncompressed BGRA DDS conversion
- Related system: Stage 7 Chaos Warfare biological warfare

## Suggested sprite definition

The following is a handoff snippet only. It has not been added to any interface file, per task scope:

```text
spriteType = {
	name = GFX_decision_bio_designate_strategic_raid_staging_state
	texturefile = "gfx/interface/decisions/biowarfare/bio_designate_strategic_raid_staging_state.dds"
}
```

## Target `.gfx` file

No `.gfx` file was provided by the parent prompt, and this package intentionally does not inspect or edit interface wiring. Add the sprite definition to the existing Chaos Redux decision-sprite registry selected by the main agent. Do not create a parallel registry solely for this icon unless the existing project pattern requires it.

## Visual notes

The icon is a decision-specific composition, not a resized focus or idea icon. At final size it presents a dark aircraft/hangar silhouette above a sealed, teal-grey industrial canister on a transfer trolley, with amber containment accents and a visible lock/staging cue. It does not depict gore, exposed material, or a generic biohazard symbol as the sole subject.

## Remaining wiring risk

The DDS is ready at the exact requested runtime path, but the game will not resolve the intended sprite until the main agent registers `GFX_decision_bio_designate_strategic_raid_staging_state` in the correct existing `.gfx` file.
