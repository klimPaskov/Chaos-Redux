# IW-051 Sakha/YAK identity and portrait source research handoff

> Map-evidence note (2026-08-15): the existing 574/Yakutsk anchor passes direct map inspection. Any older allocation-probe `MAP_STATE_ID_COLLISION` wording is historical and does not alter the portrait source/rights disposition.

Date: 2026-08-15.

## Disposition

The source package is complete for parent review, not for runtime installation. Pavel Pevznyak clears the source identity, public-domain/provenance, crop, and 1936 role/date gates for the exact vanilla `YAK_pavel_pevznyak` consumer. Anatoly Pepelyayev clears identity, source, rights metadata, and crop review but fails the 1936 YAK country-leader role/date gate, so his package is research-only and remains blocked.

No generic or generated likeness was substituted. No DDS or `.gfx` wiring was created. No 156x210 PNG is retained in the Event 006 archive. The originals remain flat at `docs/assets/portraits/006_independence_wave/`; all crop, metadata, provenance, API evidence, and review previews remain under its existing single `processed/` directory.

## Exact vanilla consumer evidence

Installed vanilla `common/characters/YAK.txt` defines:

- `YAK_pavel_pevznyak`, name Pavel Pevznyak, civilian large portrait `GFX_portrait_Pavel_Pevznyak`, stalinism country leader expiring `1943.1.1.1`.
- `YAK_anatoly_pepelyayev`, name Anatoly Pepelyayev, civilian large portrait `GFX_portrait_Anatoly_Pepelyayev`, oligarchism country leader expiring `1960.1.1.1`.

Installed vanilla `history/countries/YAK - Yakutia.txt` starts democratic Yakutia with last election `1936.1.1` and recruits both characters. Installed vanilla `interface/_leader_portraits.gfx` currently maps Pavel to `gfx/leaders/Asia/Portrait_Asia_Generic_2.dds` and Anatoly to `gfx/leaders/Asia/Portrait_Asia_Generic_1.dds`. Exact ID/key search found no duplicate owner in the Chaos Redux mod tree.

## Pavel Pevznyak source

Source page: `https://commons.wikimedia.org/wiki/File:Pevznyak_Pavel_Matveevich_Trim.jpg`.

The Commons metadata identifies Pavel Matveevich Pevznyak, birth name Faivel Mordukhovich, as Secretary of the Yakutsk Regional Committee from August 1930 through January 1939, with a 1930s Yakutsk photograph from the Photo Fund of the Republic of Sakha (Yakutia), No. 14301. This directly covers the 1936 opening role/date gate and matches the installed vanilla identity rather than inventing an alternate appointment.

Commons records the file as Public domain, CC-PD-Mark, and `attribution_required=false`; the credit links to the RGASPI Sakha collection record `https://rgaspi.kaisa.ru/yakutiya/object/355421833_368471863`. The source API record is archived at `docs/assets/portraits/006_independence_wave/processed/iw051_sakha_yak_pavel_pevznyak_source_commons_api_2026_08_15.json`, and the identity API capture is `docs/assets/portraits/006_independence_wave/processed/iw051_sakha_yak_pavel_pevznyak_source_identity_russian_wikipedia_api_2026_08_15.json`.

The flat original is `docs/assets/portraits/006_independence_wave/iw051_sakha_yak_pavel_pevznyak_source_placeholder_2026_08_15__portrait_YAK_pavel_pevznyak_original.jpg`, dimensions `672x920`, bytes `388488`, SHA-256 `556dbceeb60e2db3172a0487e67c1a21d26495ea1b9332c598f126b5c011b511`. The exact source crop is `docs/assets/portraits/006_independence_wave/processed/iw051_sakha_yak_pavel_pevznyak_source_placeholder_2026_08_15__portrait_YAK_pavel_pevznyak_source_crop.png`, dimensions `672x905`, SHA-256 `cb25c99934ad339e8f7b536fb020070f039ea010a55eddd7c0ae1691202b269d`. Automatic YuNet detected one face at `[155,173,330,425]`; visual review confirms a clear single-subject head-and-shoulders crop.

## Anatoly Pepelyayev source

Source page: `https://commons.wikimedia.org/wiki/File:Analolij_Piepielajew.jpg`.

Commons identifies Anatoliy Pepelaev as a Russian White Army general and dates the image to 1918, crediting Henryk Mościcki and Jan Cynarski, `Historia XX w.`, Warszawa 1934. Commons records Public domain and `attribution_required=false`; the source API record is archived at `docs/assets/portraits/006_independence_wave/processed/iw051_sakha_yak_anatoly_pepelyayev_source_commons_api_2026_08_15.json`, and the identity API capture is `docs/assets/portraits/006_independence_wave/processed/iw051_sakha_yak_anatoly_pepelyayev_source_identity_english_wikipedia_api_2026_08_15.json`.

The identity source records that Pepelyayev was released from prison on 1936-06-06 and employed as a carpenter in Voronezh, and separately records his 1922-1923 campaign toward Yakutsk. This establishes historical Sakha relevance but not a 1936 YAK country-leader office. The exact vanilla role/date gate therefore fails; the package must not be promoted by assuming an alternate appointment.

The flat original is `docs/assets/portraits/006_independence_wave/iw051_sakha_yak_anatoly_pepelyayev_research_2026_08_15__portrait_YAK_anatoly_pepelyayev_original.jpg`, dimensions `645x1024`, bytes `105053`, SHA-256 `a0ef9f80c92e2c53d6c9c4f8f191a4f20acda9fdf7775e0525868e3f2a9d363c`. The exact source crop is `docs/assets/portraits/006_independence_wave/processed/iw051_sakha_yak_anatoly_pepelyayev_research_2026_08_15__portrait_YAK_anatoly_pepelyayev_source_crop.png`, dimensions `645x868`, SHA-256 `ad71cf3da5515150382f0993b6a973c29e038581fff23d65ec36b948564fb348`. Automatic YuNet detected one face at `[255,249,182,230]`; visual review confirms a single subject with face, cap, uniform, medals, and sword retained, though the 1918 source's printed text mark remains visible.

## Handoff files and blockers

- Consolidated manifest: `docs/assets/portraits/006_independence_wave/processed/metadata__iw051_sakha_yak_portrait_source_research_2026_08_15__manifest.json`.
- Crop/framing/role review: `docs/assets/portraits/006_independence_wave/processed/metadata__iw051_sakha_yak_portrait_source_research_2026_08_15__review.md`.
- Non-wiring GFX handoff: `docs/assets/portraits/006_independence_wave/processed/metadata__iw051_sakha_yak_portrait_source_research_2026_08_15__gfx_handoff.md`.
- Per-source provenance contracts: the two `metadata__iw051_*__portrait_*.txt` files in `processed/`.
- Crop metadata: the two `metadata__iw051_*source_crop.json` files in `processed/`.

The exact 156x210 candidates were used only in the temporary crop-tool workspace and are not in the archive. The archive's two review previews are `624x840` 4x nearest images under `processed/`; they are not runtime portraits. DDS conversion was intentionally skipped because the source/role gates and parent review boundary do not authorize runtime installation. RunPod was not operated by the agent.
