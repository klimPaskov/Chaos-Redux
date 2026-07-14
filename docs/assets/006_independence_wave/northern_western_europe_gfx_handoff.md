# Event 006 northern and western Europe portrait GFX handoff

## Ownership boundary

The source-asset worker produced three route-owned final-form DDS portraits and
did not edit `.gfx`, character, gameplay, localisation, GUI, or country-history
files. The main agent visually accepted the archival Brittany crop and
registered all three sprites in `interface/006_independence_wave.gfx` on
2026-07-14. Character and route wiring remains package-owned.

## Proposed sprite registrations

```txt
spriteTypes = {
	spriteType = {
		name = "GFX_portrait_BRI_francois_debeauvais"
		texturefile = "gfx/leaders/006_independence_wave/portrait_BRI_francois_debeauvais.dds"
	}

	spriteType = {
		name = "GFX_portrait_RHI_josef_friedrich_matthes"
		texturefile = "gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds"
	}

	spriteType = {
		name = "GFX_portrait_BAY_rupprecht_of_bavaria"
		texturefile = "gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds"
	}
}
```

Use the surrounding repository `.gfx` wrapper style if it differs from this
minimal handoff. Keep the sprite names and texture paths stable unless the parent
finds an actual identifier collision.

## Character wiring locks

| Sprite | Allowed use | Forbidden use |
|---|---|---|
| `GFX_portrait_BRI_francois_debeauvais` | François Debeauvais on an explicitly Breton nationalist route | universal BRI opening, neutral commission, constitutional cabinet, labor route, or another person |
| `GFX_portrait_RHI_josef_friedrich_matthes` | Josef Friedrich Matthes on the 1923 Rhenish separatist/republic direction | generic neutral corridor, military cabinet, labor government, or another person |
| `GFX_portrait_BAY_rupprecht_of_bavaria` | Rupprecht on the Bavarian traditional-crown/restoration direction | republican, labor, military-emergency, or generic constitutional opening |

The BRI portrait is a low-resolution crop from an identified 1928 group
photograph. The parent must review the decoded sheet before wiring it. If the
quality is rejected, leave the portrait blocked; do not silently substitute the
rights-uncertain 1932 image.

## Explicitly non-runtime symbol previews

Do not register these processed review files as flag or UI sprites:

- `processed_png/country_symbols/acx_st_pirans_cross.png`;
- `processed_png/country_symbols/aex_flemish_lion_arms.png`;
- `processed_png/country_symbols/afx_walloon_rooster.png`;
- `processed_png/country_symbols/agx_west_frisian_flag.png`;
- `processed_png/country_symbols/ajx_saar_territory_1920_1935.png`.

They are provenance-backed motif inputs for a separate generated period-civic
flag pass. No ACX, AEX, AFX, AGX, or AJX TGA exists in this source-only
handoff; the final fictional baseline triplets and fictional portrait sprites
are documented in
`northern_western_europe_generated_art_gfx_handoff.md`.

## Validation evidence

All three DDS files reopen as 156x210 RGBA images and have the expected
uncompressed BGRA file length of 131,168 bytes. Visual decode proof is in
`contact_sheets/006_northern_western_europe_final_dds_decoded.png`.

Full provenance, licenses, hashes, route distinctions, and blocked sources are
in `northern_western_europe_source_manifest.md`.
