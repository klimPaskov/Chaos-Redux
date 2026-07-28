# IW-012 Iceland package asset handoff

Status: source-reuse package; no new binary art required.

## Reused source assets

- Vanilla historical ICE flag and cosmetic identity: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/ICE.tga` and the vanilla ICE cosmetic flag definitions.
- Vanilla historical male leader portrait `GFX_portrait_ICE_sveinn_bjornsson` from the installed ICE character definitions.
- Vanilla historical male commander portrait `GFX_portrait_ICE_bjorn_sveinsson_bjornsson` from the installed ICE character definitions.
- Event 006 shared idea and decision icons already registered in `interface/006_independence_wave_custom_icons.gfx`.

## Processing and wiring

This adapter deliberately does not copy, repaint, resize, or convert the approved vanilla ICE art. If a future Event 006 variant needs a sourced ICE-era portrait, the required path is archival male photograph → explicit head-and-shoulders crop → identity-preserving ImageGen HOI4 repaint → independent likeness/style audit → 156×210 processing → DDS wiring. Original-size repaint masters belong directly in `docs/assets/006_independence_wave/portraits_generated_png`; that shelf stays flat, contains no nested folders, and contains no normalized PNGs.

No Event 006 advisor icons are created or wired for IW-012.

FORM-02 uses the existing NUX cosmetic identity only while vanilla Nordic
League flags are unused. Its member trigger rejects `form_nordic_nation_flag`
and `form_nordic_league_flag`; cleanup removes only Event 006 FORM-02 state and
never clears those vanilla flags.

The shared government-route lock invokes the ICE additive route adapter, so
constitutional, traditional, emergency, and patron route states reuse the
vanilla male roster and the shared Event 006 icon family without creating
portrait, dossier, or advisor derivatives.
