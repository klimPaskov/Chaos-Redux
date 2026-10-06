# Crisis Seal Animation Brief

The asset is the symbolic Black Plague crisis seal shown on the disease containment board when the selected crisis is Severe or Collapsed.

The existing GUI child is `disease_containment_board_black_plague_crisis_seal_animated` under `disease_containment_board_window` in `interface/biowarfare_disease_containment.gui`; the existing sprite pair is registered in `interface/020_black_plague_rat_identity.gfx`.

The static sprite is `GFX_black_plague_crisis_seal_static`, and the animated sprite is `GFX_black_plague_crisis_seal_animated`.

The source frame size is 64×64 pixels, the sheet size is 512×64 pixels, the animation has eight frames, the existing rate is 6 fps, the loop is continuous, and `play_on_show` is enabled.

The anchor is the centre of the 64×64 canvas, and the unused canvas remains natively transparent.

Frame 000 is the unchanged static seed from `source/existing_png/crisis_static.png`; frames 001–007 each use a separately generated transparent ImageGen glint layer composited over that immutable seed.

The frame-001 replacement prompt is archived before its generation in `source/imagegen/requests/crisis_frame_001.json`; the inherited test layer remains preserved as a superseded candidate.

The subject is a fictional symbolic crisis seal, and the generated light stays within the outer ring so its skull, circle, cross and lower red stone retain one identity.

The approved source method is layered ImageGen with native transparency; no complete seal redraw is used for the final frames.

The 64×64 static DDS is `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_static.dds`, and the 512×64 sheet DDS is `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_sheet.dds`.

The sheet PNG, contact sheet, and review GIF are stored beside this brief in `sheets/`, `crisis_seal_contact.png`, and `previews/` respectively.

The visual review used only the canonical `icons/decisions/`, `icons/medals/`, and `scripted_guis/institutional_boards/` families under `.agents/skills/chaos-redux-event-assets/assets/gfx_references`; those references informed canvas and alpha review, while the original Black Plague seed remained the sole subject anchor.
