# IW-047 Mari El — `MEL_zinovy_zhadinov` portrait source audit handoff

Date: 2026-08-14.

Status: **HOLD / blocked identity and rights gate.** No runtime DDS, `.gfx`, character, gameplay, localisation, central-admission, or Join files were changed.

## Vanilla consumer and global token

Installed vanilla `common/characters/MEL.txt` defines `MEL_zinovy_zhadinov` with display name `Zinovy Zhadinov`, Marxist ideology, civilian country-leader role, and portrait token `GFX_portrait_Zinovy_Zhadinov`.

Installed vanilla `history/countries/MEL - Mari El.txt` recruits `MEL_zinovy_zhadinov` in the 1936 setup at capital 833, Yoshkar-Ola.

Installed vanilla `interface/_leader_portraits.gfx` globally owns `GFX_portrait_Zinovy_Zhadinov` and points it to the generic texture `gfx/leaders/Europe/Portrait_Europe_Generic_2.dds`.

The installed texture is `156x210` RGB, 87,368 bytes, file SHA-256 `9ef3369f963d20a5ac37f5cfcc599a5f6ad1cc9871f377ee42c210d8d97bb513`, and decoded RGBA SHA-256 `fc78277e4306afc7282782d8fb69d6f8f0140f0c1cc3daf8c8ee9a2fbca04de6`.

No Chaos Redux duplicate character, portrait token, or runtime owner for `MEL_zinovy_zhadinov` or `GFX_portrait_Zinovy_Zhadinov` was found.

## Identity/date/role research

The exact `Zinovy Zhadinov` spelling has no attributed biographical record, image record, or institutional source in the reviewed vanilla, project, Wikidata, Russian Wikipedia, English Wikipedia, and Internet Archive search surfaces.

The [Mari regional committee history](https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%80%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%BD%D0%BE%D0%B9_%D0%BA%D0%BE%D0%BC%D0%B8%D1%82%D0%B5%D1%82_%D0%9A%D0%9F%D0%A1%D0%A1) lists Czeslaw Iosifovich Wróblewski as first secretary from January 1935 through November 1937, covering 1936.

The same source lists Zinovy Yakovlevich Zhadnov only from November 1937 through May 1938, after the 1936 consumer date.

The [Wróblewski biography](https://ru.wikipedia.org/wiki/%D0%92%D1%80%D1%83%D0%B1%D0%BB%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%2C_%D0%A7%D0%B5%D1%81%D0%BB%D0%B0%D0%B2_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%BE%D0%B2%D0%B8%D1%87) confirms a real male 1936-period officeholder, but Wróblewski is a different person and cannot be transferred to the vanilla `MEL_zinovy_zhadinov` identity.

The [Zhadnov biography](https://ru.wikipedia.org/wiki/%D0%96%D0%B0%D0%B4%D0%BD%D0%BE%D0%B2%2C_%D0%97%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D0%B9_%D0%AF%D0%BA%D0%BE%D0%B2%D0%BB%D0%B5%D0%B2%D0%B8%D1%87) confirms a different real person whose Mari office begins in late 1937, not 1936.

Stable Zhadnov source URL: https://ru.wikipedia.org/wiki/%D0%96%D0%B0%D0%B4%D0%BD%D0%BE%D0%B2%2C_%D0%97%D0%B8%D0%BD%D0%BE%D0%B2%D0%B8%D0%B9_%D0%AF%D0%BA%D0%BE%D0%B2%D0%BB%D0%B5%D0%B2%D0%B8%D1%87.

## Bounded exact-identity retry (2026-08-13)

The exact consumer was re-checked without relaxing the identity gate. Wikimedia Commons file-namespace searches for `"Zinovy Zhadinov"`, `"Zinoviy Zhadinov"`, `"Зиновий Жадинов"`, and `"Зиновий Иванович Жадинов"` each returned zero files; the [Commons API query record](https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch=%22Zinovy%20Zhadinov%22&srnamespace=6&format=json&utf8=1) is representative.

Wikidata exact-name searches in English and Russian, Internet Archive exact-phrase searches in English and Russian, Russian Wikipedia exact-name and role/name searches, Library of Congress, Open Library, and DigitalNZ returned no exact identity record or portrait candidate. Complete query URLs, HTTP statuses, and zero-result counts are archived in `docs/assets/portraits/006_independence_wave/iw047_mel_zinovy_zhadinov_source_research_2026_08_14__retry_2026_08_13.json` (SHA-256 `87b388d40de5f590c2dab3aee7edf77c8ee60f54d1224c05ee261738dcb0870e`).

The [committee raw source](https://ru.wikipedia.org/w/index.php?title=%D0%9C%D0%B0%D1%80%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%BD%D0%BE%D0%B9_%D0%BA%D0%BE%D0%BC%D0%B8%D1%82%D0%B5%D1%82_%D0%9A%D0%9F%D0%A1%D0%A1&action=raw) still lists Wroblewski as first secretary from 10 January 1935 through November 1937 and Zhadnov as acting first secretary only from November 1937 through 20 May 1938. It does not name the exact vanilla spelling `Zinovy Zhadinov`.

Retry verdict: **FAIL/HOLD remains.** No attributed, rights-clear, period-compatible exact source exists in the bounded retry surfaces, so no image, crop, generated face, substitution, DDS, `.gfx`, or character edit was made.

## Rights gate

The Wróblewski article image is documented by [its Russian Wikipedia file description](https://ru.wikipedia.org/w/index.php?title=%D0%A4%D0%B0%D0%B9%D0%BB:%D0%92%D1%80%D1%83%D0%B1%D0%BB%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%A7%D0%B5%D1%81%D0%BB%D0%B0%D0%B2_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%BE%D0%B2%D0%B8%D1%87.jpg&action=raw) as sourced from `knowbysight.info`, with no author, and marked fair-use-only for the article.

That image is not a rights-cleared runtime source and does not depict the vanilla character identity.

No image for Zhadnov was exposed by the reviewed article summary or search results, and the institutional committee source is text-only rather than a licensed portrait source.

## Archive and files

Research evidence is archived flat under [docs/assets/portraits/006_independence_wave/](../../../assets/portraits/006_independence_wave/), with no subject subfolder.

- `iw047_mel_zinovy_zhadinov_source_research_2026_08_14__manifest.json` records the consumer, global token ownership, identity findings, candidate role evidence, rights disposition, hashes, and explicit HOLD state.
- `iw047_mel_zinovy_zhadinov_source_research_2026_08_14__HOLD.md` records the human-readable research, rights gate, and archive layout.
- `iw047_mel_zinovy_zhadinov_source_research_2026_08_14__mel_committee_summary.json` archives the institutional role evidence, SHA-256 `507aff9b32fb0338a51cdca7b6b0d24d5c697a03db7a5f3286db61f2dc71d7b5`.
- `iw047_mel_zinovy_zhadinov_source_research_2026_08_14__zhadnov_summary.json` archives the post-1936 Zhadnov evidence, SHA-256 `067b1d5b9f4229122b94b519367860ddd12c8a76f2746856e29e2eaffda2ffe2`.
- `iw047_mel_zinovy_zhadinov_source_research_2026_08_14__vrublevsky_summary.json` archives the 1936-period Wróblewski evidence, SHA-256 `c387d3ee13457756532011e05a3d3ada22897873f976631214f994dbcb9ebd40`.
- `iw047_mel_zinovy_zhadinov_source_research_2026_08_14__vrublevsky_file_license.txt` archives the fair-use file description, SHA-256 `b11d043adb2a36b1921c84875c1e81c6da44384bb8b1970acad1785d1e9673b9`.

The parent layout contract is preserved: research/source files are flat in the archive root, `processed/` has no IW-047 files, and no `156x210` archive file exists.

## Skipped work and blockers

- No source image was accepted, so no original image, crop, equality JSON, processed PNG, DDS, or `.gfx` handoff was created.
- Crop/framing review was not run because there is no identity-safe source image.
- The vanilla generic texture was not copied into the archive or treated as a source placeholder.
- No generated portrait, ImageGen output, RunPod operation, repaint, identity substitution, or institutional stand-in was used.
- Parent must choose one of two explicit design resolutions before portrait work can resume: correct the character identity to an attested 1936 Mari officeholder with a rights-cleared source, or authorize a distinct authentic institutional consumer rather than silently mapping another person to `MEL_zinovy_zhadinov`.
