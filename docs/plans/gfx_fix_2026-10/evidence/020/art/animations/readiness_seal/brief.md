# Rat King Readiness Seal Animation Brief

The asset is the symbolic Black Plague terminal-readiness seal used by the Rat King final-order decision `black_plague_rat_king_execute_terminal_takeover` in `common/decisions/020_black_plague_rat_decisions.txt`.

The existing sprite pair is registered in `interface/020_black_plague_rat_identity.gfx` as `GFX_black_plague_rat_king_terminal_readiness_static` and `GFX_black_plague_rat_king_terminal_readiness_animated`.

The retained authored master size is 64×64 pixels with a 512×64 master sheet; the reviewed decision consumer uses a 34×34 runtime frame and a 272×34 runtime sheet, with eight frames at the existing 6 fps rate, continuous looping, and `play_on_show` enabled.

The anchor is the centre of the 64×64 canvas, and the unused canvas remains natively transparent.

Frame 000 is the unchanged static seed from `source/existing_png/readiness_static.png`; frames 001–007 each use a separately generated transparent ImageGen glint layer composited over that immutable seed.

The subject is a fictional symbolic readiness seal, and each glint remains a small accent over the original dark rat-king emblem.

The reviewed decision row is 41 pixels wide, so a 34×34 static and 272×34 sheet were accepted by the parent from the retained 64×64 authored masters and installed at the original DDS paths.

The existing runtime paths remain `gfx/interface/animated/020_black_plague/world_end_readiness_seal/black_plague_rat_king_terminal_readiness_static.dds` and `gfx/interface/animated/020_black_plague/world_end_readiness_seal/black_plague_rat_king_terminal_readiness_sheet.dds`.

The authored master sheet, accepted 34×34 runtime PNGs, contact sheets, and review GIF are stored in this package under `sheets/`, `decision_34x34_preview/`, the animation root, and `previews/`.

The visual review used only the canonical `icons/decisions/`, `icons/medals/`, and `scripted_guis/institutional_boards/` families under `.agents/skills/chaos-redux-event-assets/assets/gfx_references`; the original readiness seal remained the sole subject anchor.
