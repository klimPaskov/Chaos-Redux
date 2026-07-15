# Event 014 Flag Asset Frozen Ledger

> **Corrected production contract (2026-07-15).** The thirteen families, five compositions, and three sizes below remain the runtime contract, but every design is a flat, front-facing vexillological graphic generated specifically for the refresh. Warlord families are origin-agnostic. Current source and provenance evidence lives in `docs/assets/014_cannibalism/flags_refresh/` and the top-level Event 014 asset manifest.

## Runtime contract

This ledger resolves the former `CBL_LAST_TABLE` conflict and is the production source of truth for Event 014 flags.

- `CBA` through `CBH`: eight origin-agnostic reusable slots. Each can host an Island Host, Siege Commune, or March Host package.
- `CBL`: ordinary unified base identity, created only by the public Evolution III reveal.
- `CBL_CENTRAL_COMMAND`: applied by `cannibalism_unified_focus_one_command`.
- `CBL_HOST_CONFEDERATION`: applied by `cannibalism_unified_focus_many_jaws`.
- `CBL_RITUAL_STATE`: applied by `cannibalism_unified_focus_ritual_administration`.
- `ZZZ_CANNIBALISM_HANNIBAL`: applied only by the public Wendigo merge in `cannibalism_prepare_wendigo_merge_identity`.

No Event 014 flag or cosmetic tag exposes Hannibal before `cannibalism_reveal_complete`. The obsolete `CBL_LAST_TABLE` family is not a runtime identity and must not be restored or counted.

## Required files

For every family token `F`, produce five genuinely distinct compositions rather than palette swaps. Each source must depict only the flat flag design: no fabric, folds, poles, scenery, perspective, texture, lighting, or presentation mockup.

- `gfx/flags/F.tga`
- `gfx/flags/F_communism.tga`
- `gfx/flags/F_democratic.tga`
- `gfx/flags/F_fascism.tga`
- `gfx/flags/F_neutrality.tga`
- the same five names under `gfx/flags/medium/`
- the same five names under `gfx/flags/small/`

The complete package is thirteen families by five compositions by three sizes: 195 TGA files.

| Size | Dimensions | Format |
|---|---:|---|
| Standard | 82x52 | uncompressed 32-bit TGA, bottom-left origin |
| Medium | 41x26 | uncompressed 32-bit TGA, bottom-left origin |
| Small | 10x7 | uncompressed 32-bit TGA, bottom-left origin |

Ideology-specific files are mandatory because a cosmetic fallback does not override an ideology-specific base flag.

## Family art directions

| Family | Distinct fictional motif |
|---|---|
| `CBA` | tooth-ring and crossed cleavers in hard geometric bands |
| `CBB` | split jaw and hooked knife in a bold saltire or chevron field |
| `CBC` | cracked bowl and three fangs in high-contrast heraldic geometry |
| `CBD` | black sunburst, butcher hook, and angular bone-white divisions |
| `CBE` | wagon wheel and cleaver reduced to severe flat silhouettes |
| `CBF` | rail spike, horse jaw, and broken line rendered as simple heraldry |
| `CBG` | crescent bite, butcher block, and triangular color divisions |
| `CBH` | crossed cleavers, tooth crown, and asymmetric flat bands |
| `CBL` | one empty command table joined to several blood-red routes; no leader portrait |
| `CBL_CENTRAL_COMMAND` | one blade and one chain binding every route into a rigid vertical command |
| `CBL_HOST_CONFEDERATION` | four unequal Host weapons joined around a common table without losing their shapes |
| `CBL_RITUAL_STATE` | state ledger, punishment table, sealed bowl, and ordered chains; no borrowed sacred imagery |
| `ZZZ_CANNIBALISM_HANNIBAL` | frost-cracked jaw, winter command chain, ruined road, dark red ice; no Indigenous regalia or sacred motifs |

Within each family, the five compositions should express collective command, civic resistance, rigid militarization, warlord neutrality, and an ideology-neutral form through layout and object choice only. Do not use real political emblems, extremist insignia, national coats of arms, tribal symbols, readable text, or merely recolored copies.

## Production and proof

- Use generated fictional gore-heavy source art with no real victims or recognizable people.
- Keep the central silhouette legible after conversion to 10x7.
- Preserve one source image or source-sheet crop per final composition, plus prompt and provenance records.
- Provide processed PNG intermediates, all TGA files, a manifest, normal/medium/small contact sheets, alpha/orientation checks, and normalized RGBA uniqueness checks.
- Do not overwrite existing Wendigo base flags; only add the explicit transformed cosmetic family.
- Remove the obsolete `CBL_LAST_TABLE` live files only after all thirteen current families have passed validation.
