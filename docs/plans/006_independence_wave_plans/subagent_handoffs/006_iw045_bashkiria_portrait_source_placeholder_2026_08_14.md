# IW-045 Bashkiria — `BSK_yakov_bykin` grounded portrait source-placeholder handoff

Date: 2026-08-14.

Status: source placeholder complete and reviewed; superseded by the deterministic runtime handoff, with dedicated DDS/GFX and parent consumer/cleanup wiring now satisfied.

## Subject and consumer

The subject is the real male officeholder Yakov Borisovich Bykin (born Yakov Borisovich Berkovich), first secretary of the Bashkir Regional Committee of the All-Union Communist Party (Bolsheviks), 1930 through October 1937.

Vanilla `common/characters/BSK.txt` defines `BSK_yakov_bykin` with `GFX_portrait_Yakov_Borisovich_Bykin`, and vanilla `history/countries/BSK - Bashkortostan.txt` recruits that character in the 1936 setup.

Installed vanilla `interface/_leader_portraits.gfx` defines the exact token globally:

```text
spriteType = {
    name = GFX_portrait_Yakov_Borisovich_Bykin
    texturefile = "gfx/leaders/Europe/Portrait_Europe_Generic_3.dds"
}
```

The current token texture is generic installed art (`156x210`, file SHA-256 `1e1a7c0b6a20b1d2c8c26fe32538f704e43a61f2953bbd9a306cda4397b74499`, decoded RGBA SHA-256 `891cea8914f80b7acd6ebc8664f90a111358591592b68e8fdffb20caad350088`). It is not a portrait-specific Bykin source.

## Grounded source and provenance

Source page: [Wikimedia Commons — Быкин Яков Борисович, 1912](https://commons.wikimedia.org/wiki/File:%D0%91%D1%8B%D0%BA%D0%B8%D0%BD_%D0%AF%D0%BA%D0%BE%D0%B2_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87,_1912_.jpg).

The file caption identifies Bykin in Switzerland in 1912 and records uploader/author `MDobrom`; the file page declares [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Preserve attribution and share-alike obligations for any shipped derivative; this is not public-domain material.

Independent role corroboration: [English biography](https://en.wikipedia.org/wiki/Yakov_Bykin), [Russian biography](https://ru.wikipedia.org/wiki/%D0%91%D1%8B%D0%BA%D0%B8%D0%BD%2C_%D0%AF%D0%BA%D0%BE%D0%B2_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87), and [Wikidata Q15064831](https://www.wikidata.org/wiki/Q15064831).

## Durable package

Evidence is consolidated under [the Event 006 portrait archive](../../../assets/portraits/006_independence_wave/):

- `iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_original.jpg`: untouched `1986x3178` source, 1,184,558 bytes, SHA-256 `882608cf2ea282f5a603cc1c917f2b13a8b813d5c79857ee3d3e6a6c4fd02ddb`.
- The unchanged source master is retained directly in the parent archive as `iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_original.jpg`, with the same dimensions and SHA-256 `882608cf2ea282f5a603cc1c917f2b13a8b813d5c79857ee3d3e6a6c4fd02ddb`; the lossless crop and metadata remain in `processed/`.
- `processed/iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_source_crop.png`: lossless `1125x1514` crop, SHA-256 `0b8bc295b95910e750944ac48a41644ffae74e327764d5aa36b735961e1993e3`.
- `processed/metadata__iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_source_crop.json`: exact crop/equality evidence, SHA-256 `959a3566f4786e2aeb48ed6e733c56ee595624c686a0db5bb9c6ba1ccf46e388`; crop rectangle `[372,401,1497,1915]`; one detected face `[810,676,250,306]`; decoded RGBA equality `true`; matching crop/output RGBA hash `474dbf8c8e566f393d68292f62d9a6004705fd39c3002cbec7df3aecec78ca77`.
- The deterministic RGB `156x210` LANCZOS candidate has SHA-256 `470c6d4f6213c3ca7a0451e3440a5534b1e50333eec456f43cab204ad3644f34`, but its PNG is intentionally not retained in the consolidated archive; it was reconstructed in memory for DDS validation.
- `processed/metadata__iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin.txt`: co-located provenance contract, source-mode/state/review, source attribution, license, hashes, crop and runtime isolation; current SHA-256 is recorded in the manifest.
- `processed/metadata__iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_manifest.json`: manifest with identity, consumer, ownership search, source rights, crop evidence, review, and runtime handoff facts.
- `BSK_yakov_bykin_review.md`: identity/framing/provenance review and vanilla comparison.
- The canonical installed-token reference remains in the skill-local leader reference shelf; its source PNG is not duplicated into the consolidated Event 006 archive.

The canonical installed-leader reference family and contact sheet at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/` were inspected before processing.

## Ownership search and runtime gate

Search terms included `BSK_yakov_bykin`, `GFX_portrait_Yakov_Borisovich_Bykin`, `Yakov Borisovich Bykin`, `Yakov Bykin`, `Быкин`, `BSK_leader`, and `GFX_portrait_BSK_oilfield_workshop_council` across `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/`.

The only project-side BSK portrait is Event 005's institutional `GFX_portrait_BSK_oilfield_workshop_council` (`gfx/leaders/005_soviet_collapse/BSK_leader.dds`); it is not Bykin, is not IW-045-owned, and was not reused.

The dedicated runtime DDS and portrait-specific GFX are installed as documented in `006_iw045_bashkiria_portrait_runtime_2026_08_14.md`. Reusing the vanilla `GFX_portrait_Yakov_Borisovich_Bykin` token globally remains forbidden; the source package remains durable evidence only and no runtime reference points into `docs/assets/portraits/`.

## Parent wiring handoff

The installed portrait-specific path is `gfx/leaders/006_independence_wave/portrait_BSK_independence_wave_yakov_bykin.dds` and the stable sprite is `GFX_portrait_BSK_independence_wave_yakov_bykin`, preserving the vanilla character's identity reference only through the parent’s explicit guarded transfer. Conversion and validation evidence are recorded in the runtime handoff:

```powershell
python -B .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --input <exact-crop-derived-in-memory-156x210-candidate> --output gfx/leaders/006_independence_wave/portrait_BSK_independence_wave_yakov_bykin.dds --width 156 --height 210
```

The candidate input is intentionally not a current filesystem path because the consolidated archive policy forbids retaining an IW-045 156x210 PNG. The final DDS raw payload and decoded pixels were independently proven equal to that deterministic reconstruction.

The `.gfx` registration and character-scoped consumer wiring do not override the global vanilla token. The user has not requested a `styled_final`; `replacement_pending` is false, and the user alone would run RunPod if a styled final were ever explicitly requested.

## Review verdicts and blockers

- Identity: PASS for grounded source placeholder; parent runtime consumer review is recorded in the superseding runtime handoff.
- Framing: PASS; single-subject head-and-shoulders crop and native `156x210` candidate preserve the source face, hair, jacket, chair, and expression without repaint or genericization.
- Provenance: PASS; original bytes, crop equality JSON, source URL, uploader attribution, CC BY-SA 4.0 status, dimensions, and hashes are retained.
- Runtime: PASS for the dedicated DDS/GFX package; parent `.350` consumer override and guarded cleanup restoration are wired, while the global vanilla token remains untouched.
- Simplifications/omissions: central admission and live in-game display were not claimed; no fallback identity or Event 005 council art was substituted.
