# Event 006 IW-038 Ruthenia portrait wiring repair

Date: 2026-09-19

Disposition: implemented narrow runtime wiring repair. Event 006 remains **HOLD / PARTIAL**; this repair does not promote IW-038, close grounded portrait rights, or claim live engine validation.

## Defect

The Ruthenia cleanup effect in `common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt` referenced `GFX_portrait_RUT_augustin_voloshyn` and `GFX_portrait_RUT_augustin_voloshyn_small`, but the consolidated Event 006 portrait registry defines only the dedicated large sprite `GFX_portrait_RUT_independence_wave_augustin_voloshyn`. No authorized small or dossier portrait family exists for this package.

## Repair

The cleanup-scoped `set_portraits` call now uses the registered dedicated large sprite and no longer emits the unregistered small token. The runtime texture remains `gfx/leaders/006_independence_wave/portrait_RUT_augustin_voloshyn.dds`; no source art, crop, DDS, character identity, package gate, or admission rule changed.

## Validation

- A scoped static search finds no remaining `GFX_portrait_RUT_augustin_voloshyn` or `GFX_portrait_RUT_augustin_voloshyn_small` references in runtime source.
- `GFX_portrait_RUT_independence_wave_augustin_voloshyn` is defined once in `interface/006_independence_wave_portraits_registry.gfx` and is used by both the Ruthenia cleanup effect and the existing Event 006 portrait override.
- The final DDS decodes as RGBA `156x210` and was opened for visual review; the portrait has stable headroom, shoulders, and no matte or crop defect.
- The broader Event 006 static asset audit remains the authority for the already-reviewed 49 accepted asset rows, native dimensions, final-DDS decode coverage, and outstanding ASSET-044/045/046 and GUI/rights gates.

No new portrait, small portrait, fallback identity, or cross-family asset was created.
