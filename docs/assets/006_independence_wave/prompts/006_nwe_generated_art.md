# Event 006 northern and western Europe generated-flag prompts

## Authority and production rules

This is the current flag-only prompt and provenance record for the ACX, AFX,
AGX, and AJX Event 006 triplets. No non-flag production recipe belongs to this
authority.

The four live country flags were generated in four separate official ImageGen
calls. Each call received one rights-cleared historical flat-design reference
and one canonical vanilla HOI4 normal/medium/small flag ladder as visual inputs.
The historical reference controls the design; the vanilla ladder controls only
flat presentation and small-size readability. Every prompt forbids fabric,
lighting, perspective, decoration, text, watermarks, and alternate redesigns.

Every call requested a 3:2, front-facing, edge-to-edge orthographic flag. Raw
ImageGen outputs are retained unchanged in
`../source_png/generated_nwe/flags/`. The build tool maps those raw pixels to
the documented exact palette without dithering, never imports a reference mask,
and never traces or redraws a symbol. For ACX only, it deterministically
promotes one almost-solid noisy cross-edge scanline to the adjacent white field.
The normal flag is resized from that flat master; medium and small are resized
from normal with no bespoke redesign.

## ACX Cornwall — St Piran's Cross

Historical input: `../source_png/country_symbols/acx_st_pirans_cross_source.png`
([Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Flag_of_Cornwall.svg),
public domain); identity and proportion check:
[Flag Institute UK Flag Registry](https://www.flaginstitute.org/wp/flags/cornwall-flag/).

Canonical presentation input: `arm.png` at all three vanilla-reference sizes.

> Reproduce the attached historical St Piran's Cross design exactly as a clean
> flat flag: one plain white upright cross on a solid black field, with the same
> centered geometry and no added charge. Output one edge-to-edge 3:2
> orthographic flag master. No pole, border, folds, fabric texture, lighting,
> shadow, depth, gradient, weathering, caption, lettering, watermark, mockup,
> modern logo, or alternate redesign. Use the attached canonical vanilla HOI4
> flag ladder only as a reference for flat graphic clarity at small size.

Raw ImageGen output:
`C:/Users/klimp/.codex/generated_images/019f64f5-0142-7ea2-9be6-3b919c017427/exec-7f7bae87-7c21-433f-bf73-adbbdaca7976.png`.

Repo copy:
`../source_png/generated_nwe/flags/ACX_st_pirans_cross_imagegen_raw.png`.

Flat master:
`../source_png/generated_nwe/flags/ACX_st_pirans_cross_imagegen_flat_master.png`.

Exact output palette: `#000000`, `#FFFFFF`.

## AEX no-standalone-flag boundary

AEX is a vanilla `BEL_flanders` cosmetic overlay, not a standalone Event 006
country. No AEX flag prompt is active. No AEX generated master, processed PNG,
or runtime TGA belongs to this package. The historical Lion of Flanders source
is retained only as evidence for the existing vanilla cosmetic overlay.

The flag-only builder rejects an AEX artifact instead of recreating or silently
deleting one.

## AFX Wallonia — 1913 coq hardi

Historical input: `../source_png/country_symbols/afx_walloon_rooster_source.png`
([Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Flag_of_Wallonia.svg),
CC0); historical identity check:
[Wallonia Public Service](https://connaitrelawallonie.wallonie.be/histoire-et-symboles/symboles/un-embleme-le-coq-hardi).

Canonical presentation input: `isr.png` at all three vanilla-reference sizes.

> Reproduce the attached Walloon coq hardi flag design exactly as a clean flat
> flag: one red coq hardi, beak closed and dexter leg raised, centered on one
> solid yellow field. Preserve its single-charge arrangement and orientation.
> Output one edge-to-edge 3:2 orthographic flag master. No pole, border, folds,
> fabric texture, lighting, shadow, depth, gradient, weathering, caption,
> lettering, watermark, mockup, modern logo, or alternate redesign. Use the
> attached canonical vanilla HOI4 flag ladder only as a reference for flat
> graphic clarity at small size.

Raw ImageGen output:
`C:/Users/klimp/.codex/generated_images/019f64f5-0142-7ea2-9be6-3b919c017427/exec-96127640-0f4b-4a81-b6db-f17f28e66008.png`.

Repo copy:
`../source_png/generated_nwe/flags/AFX_walloon_coq_hardi_1913_imagegen_raw.png`.

Flat master:
`../source_png/generated_nwe/flags/AFX_walloon_coq_hardi_1913_imagegen_flat_master.png`.

Exact output palette: `#FFD100`, `#E4002B`.

## AGX Friesland — provincial flag

Historical input: `../source_png/country_symbols/agx_west_frisian_flag_source.png`
([Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Frisian_flag.svg),
public domain); official design check:
[Province of Fryslân](https://www.fryslan.frl/friese-vlag).

Canonical presentation input: `ice.png` at all three vanilla-reference sizes.

> Reproduce the attached Friesland provincial flag design exactly as a clean
> flat flag: seven alternating diagonal bands, four blue and three white, with
> exactly seven red pompeblêden in the documented arrangement. Preserve the
> diagonal direction, symbol count, and orientation. Output one edge-to-edge
> 3:2 orthographic flag master. No pole, border, folds, fabric texture,
> lighting, shadow, depth, gradient, weathering, caption, lettering, watermark,
> mockup, modern logo, extra symbols, or alternate redesign. Use the attached
> canonical vanilla HOI4 flag ladder only as a reference for flat graphic
> clarity at small size.

Raw ImageGen output:
`C:/Users/klimp/.codex/generated_images/019f64f5-0142-7ea2-9be6-3b919c017427/exec-8553e19e-c7ad-4591-95f2-845eeaddcc52.png`.

Repo copy:
`../source_png/generated_nwe/flags/AGX_friesland_provincial_imagegen_raw.png`.

Flat master:
`../source_png/generated_nwe/flags/AGX_friesland_provincial_imagegen_flat_master.png`.

Exact output palette: `#244994`, `#FFFFFF`, `#E72326`.

## AJX Saar — Territory flag, 1920–1935

Historical input:
`../source_png/country_symbols/ajx_saar_territory_1920_1935_source.png`
([Wikimedia Commons source](https://commons.wikimedia.org/wiki/File:Flag_of_Saar_1920-1935.svg),
public domain); institutional check:
[Saarland State Chancellery](https://artsandculture.google.com/story/saarhundert-das-saargebiet-ein-kind-der-internationalen-v%C3%B6lkergemeinschaft-staatskanzlei-saarland/kQWBBjUfmhpHJA?hl=en).

Canonical presentation input: `arm.png` at all three vanilla-reference sizes.

> Reproduce the attached Saar Territory 1920–1935 flag design exactly as a
> clean flat flag: three equal horizontal bands in blue, white, and black from
> top to bottom. Preserve the stripe order, equal geometry, and orientation.
> Output one edge-to-edge 3:2 orthographic flag master. No pole, border, folds,
> fabric texture, lighting, shadow, depth, gradient, weathering, caption,
> lettering, watermark, mockup, modern logo, emblem, or alternate redesign. Use
> the attached canonical vanilla HOI4 flag ladder only as a reference for flat
> graphic clarity at small size.

Raw ImageGen output:
`C:/Users/klimp/.codex/generated_images/019f64f5-0142-7ea2-9be6-3b919c017427/exec-801f7d89-ac0f-4f24-845a-19118f40caa2.png`.

Repo copy:
`../source_png/generated_nwe/flags/AJX_saar_territory_1920_1935_imagegen_raw.png`.

Flat master:
`../source_png/generated_nwe/flags/AJX_saar_territory_1920_1935_imagegen_flat_master.png`.

Exact output palette: `#00209F`, `#FFFFFF`, `#000000`.

## Review and reproduction authority

The manual historical comparison is
`../006_nwe_historical_flag_comparison.md`. The provenance contact sheet is
`../contact_sheets/006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png`.
The runtime ladder contact sheet is
`../contact_sheets/006_nwe_generated_flags_contact_sheet.png`.

The deterministic reproduction command is:

```powershell
python -B docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py --scope flags
```

The equivalent no-argument invocation is also supported. No other scope value
is accepted.
