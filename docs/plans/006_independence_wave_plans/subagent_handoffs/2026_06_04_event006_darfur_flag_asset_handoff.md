# Event 006 Darfur Flag Asset Handoff

## Scope

Produced a bounded HOI4 flag package for the planned Event 006 Darfur country package, likely tag `DFR`. No gameplay script, localisation, `.gfx`, `.gui`, country-tag, country, history, focus, decision, or spreadsheet files were intentionally edited.

## Historical Basis

The final asset is a conservative reconstruction of the published Darfur/Sultanate of Darfur flag description: horizontal green, red, and black stripes in a 1:2:1 ratio with a white crescent in the red stripe.

Sources consulted:

- `https://www.flag-encyclopedia.com/fdarfur_me.htm`
  - Gives the Darfur flag description, 2:3 ratio, green/red/black 1:2:1 stripes, and white crescent, and identifies it as the Sultanate of Darfur flag.
- `https://www.fotw.info/flags/sd_sdarf.html`
  - Useful caution source. The page notes uncertainty around Darfur flag traditions and warns that a recent Darfur liberation movement flag is not likely to be the traditional Fur/Darfur flag.
- `https://en.wikipedia.org/wiki/Sultanate_of_Darfur`
  - Background for the Sultanate of Darfur, its 17th-century origins, 1874 fall, 1898 restoration, and 1916 British conquest.
- `https://www.britannica.com/topic/Sudan-flag-of-The`
  - Contextual Sudanese flag history; notes black, red, and green Mahdist flags and Islamic/Sudanese color associations.

License/public-domain confidence:

- Final files are original simple geometric reconstructions created for Chaos Redux from source descriptions, not copied from a source bitmap.
- Simple flag geometry and color descriptions are not treated as copyrightable artwork here.
- Historical attribution confidence is not high. The sourceable design is plausible enough for a restoration-route symbol, but not proven by a primary archival flag source.

## Files Created

Final HOI4 flags:

- `gfx/flags/DFR.tga`
- `gfx/flags/medium/DFR.tga`
- `gfx/flags/small/DFR.tga`

Intermediate and review files:

- `docs/assets/006_independence_wave/flags/darfur/source_png/DFR_source_reconstruction.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_medium.png`
- `docs/assets/006_independence_wave/flags/darfur/processed_png/DFR_small.png`
- `docs/assets/006_independence_wave/flags/darfur/DFR_contact_sheet.png`
- `docs/assets/006_independence_wave/flags/darfur/manifest.md`

## Dimensions and Format

Validated with ImageMagick `identify`:

```text
DFR.tga TGA 82x52 srgba 8
DFR.tga TGA 41x26 srgba 8
DFR.tga TGA 10x7 srgba 8
DFR_source_reconstruction.png PNG 246x156 srgb 8
DFR.png PNG 82x52 srgb 8
DFR_medium.png PNG 41x26 srgb 8
DFR_small.png PNG 10x7 srgb 8
```

Validated TGA headers with `xxd -p -l 18`:

```text
gfx/flags/DFR.tga 000002000000000000000000520034002028
gfx/flags/medium/DFR.tga 00000200000000000000000029001a002028
gfx/flags/small/DFR.tga 0000020000000000000000000a0007002028
```

The `0x28` descriptor matches existing Chaos Redux top-left-origin 32-bit RGBA TGA country flags.

## Design Notes

- Normal and medium flags include the crescent.
- Small `10x7` flag uses only the green/red/black stripe pattern because a crescent at that size becomes unreadable noise.
- No ideology-specific variants were created. The non-specific `DFR.tga` fallback is valid by the HOI4 country-creation reference and avoids inventing unsourced ideological symbols.
- The palette is subdued for HOI4 readability and avoids modern conflict imagery, militia symbols, gore, spectacle, or copyrighted modern insignia.

## Validation

Commands run:

```text
identify -format '%f %m %wx%h %[channels] %[bit-depth]\n' ...
file gfx/flags/DFR.tga gfx/flags/medium/DFR.tga gfx/flags/small/DFR.tga ...
xxd -p -l 18 gfx/flags/DFR.tga ...
git status --short -- gfx/flags/DFR.tga gfx/flags/medium/DFR.tga gfx/flags/small/DFR.tga docs/assets/006_independence_wave/flags/darfur
```

Scoped `git status` showed only the new Darfur flag asset paths listed in this handoff. The wider worktree already contains unrelated dirty Event 005/Event 006 files; those were not part of this asset task.

## Blockers and Uncertainty

- No primary-source Darfur sultanate flag image was found in this bounded pass.
- The flag is defensible as a sourced reconstruction, not as a proven archival standard.
- Parent should decide whether the package should remain a fallback `DFR` flag only or later receive route-specific cosmetic tags/ideology variants after gameplay design is finalized.
