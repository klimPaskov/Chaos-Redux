# Event 20 shared-board infestation animation handoff

## Scope

This handoff covers the non-model presentation asset used by the shared disease containment board. It does not create or wire a 3D unit, entity, model, or animation action.

## Source frames

Four distinct ImageGen source frames are retained under `docs/assets/020_black_plague/frame_animation/source_png/`. They preserve the same rat-and-sewer emblem while changing the red heartbeat pulse in four authored states. The processed 64×64 frames are retained under `docs/assets/020_black_plague/frame_animation/processed_png/`, with a contact sheet and GIF preview under `previews/`.

## Runtime outputs

- `gfx/interface/020_black_plague/black_plague_rat_infestation_animation_sheet.dds` — 256×64 horizontal four-frame sheet.
- `gfx/interface/020_black_plague/black_plague_rat_infestation_static.dds` — 64×64 first-frame fallback.
- `interface/020_black_plague_rat_identity.gfx` registers the fallback and `frameAnimatedSpriteType` using `buttonstate_blendframes.lua`.
- `interface/biowarfare_disease_containment.gui` places both sprites in the shared disease header.
- `common/scripted_guis/biowarfare_disease_containment_scripted_gui.txt` shows the badge only while Black Plague is the selected shared category tab.

## Verification

The sheet uses four distinct processed PNG hashes and the final DDS files are one-level uncompressed BGRA textures. The static sprite remains behind the animated sprite so a frame animation parse/render failure leaves a visible Black Plague badge rather than an empty surface.

## Remaining boundary

The user explicitly excluded bespoke rat unit models from this tranche. Rat unit model packages therefore remain a future asset requirement and are not a blocker for the scripted event/UI runtime wiring here.
