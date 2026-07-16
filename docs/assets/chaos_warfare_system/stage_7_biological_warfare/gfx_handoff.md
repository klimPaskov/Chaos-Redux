# GFX handoff

## Ready asset

- Stable decision id: `bio_designate_strategic_raid_staging_state`
- Intended sprite: `GFX_decision_bio_designate_strategic_raid_staging_state`
- Final texture: `gfx/interface/decisions/biowarfare/bio_designate_strategic_raid_staging_state.dds`
- Target size: `32x32`
- Alpha: real RGBA alpha preserved through PNG and legacy uncompressed BGRA DDS conversion
- Related system: Stage 7 Chaos Warfare biological warfare

## Registered sprite definition

The following definition is registered in `interface/biological_warfare.gfx`:

```text
spriteType = {
	name = GFX_decision_bio_designate_strategic_raid_staging_state
	texturefile = "gfx/interface/decisions/biowarfare/bio_designate_strategic_raid_staging_state.dds"
}
```

## Target `.gfx` file

`interface/biological_warfare.gfx`

## Visual notes

The icon is a decision-specific composition, not a resized focus or idea icon. At final size it presents a dark aircraft/hangar silhouette above a sealed, teal-grey industrial canister on a transfer trolley, with amber containment accents and a visible lock/staging cue. It does not depict gore, exposed material, or a generic biohazard symbol as the sole subject.

## Remaining wiring risk

None. The stable sprite name, final DDS path, decision reference, and interface registry agree.
