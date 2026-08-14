# IW-051 Sakha/YAK portrait source review

Review date: 2026-08-15.

This is a source and crop review only. The Event 006 archive keeps flat originals at its root and keeps crop, metadata, provenance, source API evidence, and review previews under its existing single `processed/` directory.

| Vanilla consumer | Source identity | 1936 Event 006 role/date | Rights/provenance | Crop/framing | Disposition |
| --- | --- | --- | --- | --- | --- |
| `YAK_pavel_pevznyak` / `GFX_portrait_Pavel_Pevznyak` | PASS: Pavel Matveevich Pevznyak, also recorded as Faivel Mordukhovich | PASS: Commons archival description records Secretary of the Yakutsk Regional Committee from August 1930 through January 1939 | PASS as documented by Commons Public domain / CC-PD-Mark; Photo Fund of the Republic of Sakha (Yakutia), No. 14301, credit link to RGASPI | PASS for source review; one detected face, crop `[0,0,672,905]`, source crop `672x905`, clear head-and-shoulders view | Source-placeholder candidate; parent review and a user-supplied styled final remain required before any runtime promotion |
| `YAK_anatoly_pepelyayev` / `GFX_portrait_Anatoly_Pepelyayev` | PASS: Anatoly Nikolayevich Pepelyayev | FAIL / needs user review: identity evidence records release on 1936-06-06 and carpentry work in Voronezh, while the source is a 1918 White Army portrait; Yakutia connection is his 1922-1923 campaign, not a 1936 office | PASS as documented by Commons Public domain; source credits Henryk Mościcki and Jan Cynarski, `Historia XX w.` | PASS for source review; one detected face, crop `[0,42,645,910]`, source crop `645x868`, single subject and uniform/cap retained | Research candidate only; do not assume a 1936 YAK appointment or wire runtime |

## Exact evidence paths

- Pavel original: `docs/assets/portraits/006_independence_wave/iw051_sakha_yak_pavel_pevznyak_source_placeholder_2026_08_15__portrait_YAK_pavel_pevznyak_original.jpg` (`672x920`, SHA-256 `556dbceeb60e2db3172a0487e67c1a21d26495ea1b9332c598f126b5c011b511`).
- Pavel crop: `docs/assets/portraits/006_independence_wave/processed/iw051_sakha_yak_pavel_pevznyak_source_placeholder_2026_08_15__portrait_YAK_pavel_pevznyak_source_crop.png` (`672x905`, SHA-256 `cb25c99934ad339e8f7b536fb020070f039ea010a55eddd7c0ae1691202b269d`).
- Anatoly original: `docs/assets/portraits/006_independence_wave/iw051_sakha_yak_anatoly_pepelyayev_research_2026_08_15__portrait_YAK_anatoly_pepelyayev_original.jpg` (`645x1024`, SHA-256 `a0ef9f80c92e2c53d6c9c4f8f191a4f20acda9fdf7775e0525868e3f2a9d363c`).
- Anatoly crop: `docs/assets/portraits/006_independence_wave/processed/iw051_sakha_yak_anatoly_pepelyayev_research_2026_08_15__portrait_YAK_anatoly_pepelyayev_source_crop.png` (`645x868`, SHA-256 `ad71cf3da5515150382f0993b6a973c29e038581fff23d65ec36b948564fb348`).
- Machine crop evidence: the corresponding `metadata__...source_crop.json` files record YuNet model hash `ebafce4e3c118d6554634be5c27ab333b4c047a9a8c3faf1d7cf93101c22f0f0`, one subject, exact crop box, decoded pixel equality, and normalized archive paths.
- Source and identity captures: the four `iw051_sakha_yak_*_api_2026_08_15.json` files in `processed/` preserve the Commons and identity-page response metadata used for this disposition.

## Archive and runtime boundary

No exact `156x210` PNG is retained in the archive. The two 156x210 candidates were temporary source-review artifacts only; the archive contains only 4x nearest review previews (`624x840`) under `processed/`, not runtime portraits. No DDS, `.gfx`, character, history, country, gameplay, or localisation file was changed.

The matching installed-vanilla consumers are `common/characters/YAK.txt` and `interface/_leader_portraits.gfx`. The current textures remain vanilla generic Asia portraits until the parent approves a source/role gate and the user supplies any requested HOI4-style final.
