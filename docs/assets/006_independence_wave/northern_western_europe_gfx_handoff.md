# Event 006 northern and western Europe portrait GFX handoff

## Ownership boundary

The real-portrait tranche produced two approved route-owned DDS portraits and
updated only their asset registration surface. Character, gameplay,
localisation, GUI, and country-history wiring remain package-owned. The
rejected low-fidelity Brittany portrait, runtime DDS, and sprite registration
were removed; its identifier remains reserved pending a stronger source.

## Proposed sprite registrations

```txt
spriteTypes = {
	spriteType = {
		name = "GFX_portrait_RHI_josef_friedrich_matthes"
		texturefile = "gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds"
	}

	spriteType = {
		name = "GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria"
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
| `GFX_portrait_BRI_francois_debeauvais` (reserved; not registered) | none until an identity-safe, dual-jurisdiction source is approved | every runtime use while content-readiness is unset |
| `GFX_portrait_RHI_josef_friedrich_matthes` | Josef Friedrich Matthes on the 1923 Rhenish separatist/republic direction | generic neutral corridor, military cabinet, labor government, or another person |
| `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria` | Rupprecht on the Event 6 Bavarian traditional-crown/restoration direction, assigned to the existing vanilla character with `set_portraits` | republican, labor, military-emergency, generic constitutional opening, or any non-Event 6 origin |

The BRI portrait is explicitly blocked. The rights-cleared 1928 group crop is
too weak for identity-preserving editing; sharper 1932/1933 candidates fail the
United States rights review. Do not recreate the removed fallback or silently
substitute either rejected candidate.

## Explicitly non-runtime symbol previews

Do not register these processed review files as flag or UI sprites:

- `processed_png/country_symbols/acx_st_pirans_cross.png`;
- `processed_png/country_symbols/aex_flemish_lion_arms.png`;
- `processed_png/country_symbols/afx_walloon_rooster.png`;
- `processed_png/country_symbols/agx_west_frisian_flag.png`;
- `processed_png/country_symbols/ajx_saar_territory_1920_1935.png`.

ACX, AFX, AGX, and AJX are provenance-backed exact historical design inputs for
the separate official ImageGen flag pass. Their final unsuffixed runtime
triplets are documented in
`northern_western_europe_generated_art_gfx_handoff.md`. The AEX lion preview is
retained only as evidence for vanilla `BEL_flanders`: no AEX runtime triplet,
generated flag source, or processed generated-flag preview may be recreated.

## Validation evidence

Both approved DDS files reopen as 156x210 RGBA images, use uncompressed 32-bit
BGRA masks, and have the expected 131,168-byte file length. Decoded runtime
proof is present in each per-person source/candidate/canonical sheet under
`contact_sheets/portraits/`.

Full provenance, licenses, hashes, route distinctions, and blocked sources are
in `northern_western_europe_source_manifest.md`.
