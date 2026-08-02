# Event 012 Africa real-sourced sovereign portrait runtime tranche

Date: 2026-08-02.

This tranche replaces four Event 012 priority-member sovereign DDS files with source-locked HOI4 leader portraits. The technical character IDs, sprite IDs, Independence Wave carriers, and gameplay routes remain unchanged. No country tag, cosmetic tag, model, focus, decision, or event identifier was added.

## Runtime replacements

| Stable sprite and runtime DDS | Grounded identity | Source evidence | Parent/runtime disposition |
| --- | --- | --- | --- |
| `GFX_portrait_012_africa_priority_kanem_bornu_sovereign` / `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_kanem_bornu_sovereign.dds` | Shehu Sanda Kura of Borno | 1936 public-domain source record; exact crop `crops/kanem_bornu_sanda_kura_source_crop.png`; vendor-scan caveat retained in the source manifest | Installed after independent PASS; source-visible white wrapped turban, pale robe, dark embroidered robe, and star-shaped medal preserved |
| `GFX_portrait_012_africa_priority_harar_sovereign` / `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_harar_sovereign.dds` | Emir Abdullahi of Harar | Direct Commons original corroborated by Gallica frame 33; CC BY-SA 4.0; exact crop `crops/harar_emir_abdullahi_source_crop.png` | Installed after independent PASS; latest repaint is clean-shaven and preserves the white turban and robe; low-resolution source caveat retained |
| `GFX_portrait_012_africa_priority_kongo_sovereign` / `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_kongo_sovereign.dds` | Pedro VII Afonso of Kongo | 1934 Sociedade de Geografia de Lisboa photograph; public-domain Commons record; exact crop `crops/kongo_pedro_vii_source_crop.png` | Installed after independent PASS; pale ceremonial cloth cape, plume, embroidered robe, spectacles, moustache, and staff remain source-supported |
| `GFX_portrait_012_africa_priority_merina_sovereign` / `gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_merina_sovereign.dds` | Queen Ranavalona III of the Merina Kingdom | USC Libraries ca. 1890–1895 photograph; public-domain Commons record; exact crop `crops/merina_ranavalona_iii_source_crop.png` | Installed after independent PASS; female metadata and exact name retained; head ornament, lace collar, gown, veil, throne, and fan remain source-visible |

The DDS files are one-level uncompressed BGRA, opaque, and 156x210. The stable `.gfx` registrations already point at these runtime basenames, so no interface edit was needed.

## Review evidence

The independent reviewer compared the archival crops, raw ImageGen outputs, processed 156x210 candidates, and canonical HOI4 leader references at native and 4x nearest-neighbour scale. The review is recorded in `012_africa_real_portrait_independent_review_2026-08-02.md` and committed as `84ce959b3`.

Current approved processed hashes are:

- Kanem-Bornu: `dd59ec4b1da98ec4f27280b2ea85623bb2c6a501ca0a9cc6db354904008a11c1`.
- Harar: `0db62830d5f71df96eacd3521b2b341baf36b6c0485b72d5d03fe0486daa192f`.
- Kongo: `7144850b6ed12ef7321dfc2916be188b78788f49b16993bd1ddccdebe37c5859`.
- Merina: `d71b0cf0f9a31486b610dee2898b3a8eba4cd913ffa29a11db39b686daf0fafa`.

Current runtime DDS hashes are:

- Kanem-Bornu: `483d68f9360660db131bba2c4affbe61bc06a8638ef449c388a8ab43bfe5926b`.
- Harar: `cac604cb22c5957174842f0b3be095c784e3eb11e3210861e5c2936581e39be7`.
- Kongo: `576375623a71579cb0ca8bbf5a5e908442661624fda60aef787c9574cfe9ec28`.
- Merina: `649a1608fa4ec45e8721af3276cfb7a428f87c1395f1603ddb563dcaaf8ee024`.

## Held rows and simplifications

Buganda remains review-only. The available Mutesa II source is a shadowed 145x195 third-from-left crop in a four-kings group photograph, and the repaint sharpens uniform insignia that cannot be proven from that crop. Its generated runtime portrait and generic Kabaka localisation remain unchanged.

Asante remains blocked: Prempeh II is already owned by Event 006, while the locally retained Prempeh I candidate still needs independent identity confirmation. Sokoto, Luba, and Lunda remain rights/provenance review cases. Oyo, Manden, Aksum, Kilwa, Nubia, and Great Zimbabwe remain source-gap cases. Zulu's Dinuzulu photograph cannot be silently used for Solomon kaDinuzulu. The eleven held rows therefore retain the existing generated source mode; no unsupported lion head, spear, ritual mask, face paint, crown, or animal regalia was added to them.

The source masters, exact crop PNG/JSON proofs, raw source-locked outputs, processed PNGs, DDS derivatives, and source manifest remain in the ignored workspace `docs/assets/012_africa_priority_portraits_real_sources/` for audit and future replacement. They were not silently relabelled as fictional art. No model production was attempted.
