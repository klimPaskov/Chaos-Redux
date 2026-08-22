# IW-048 UDM `UDM_boris` / Boris Berman portrait source-gate handoff

Date: 2026-08-15

Status: `blocked` / fail-closed at rights. The exact vanilla consumer now has a defensible historical identity and 1936 role match, but the only attributable period image located is explicitly non-free/fair-use. No image was archived, no `156x210` file was retained, and no runtime or gameplay wiring was touched.

## Parent decision

Keep `UDM_boris` on runtime `HOLD`. Do not admit UDM, change central admission/Join, install DDS/GFX, or substitute a generic/generated face. The referenced processed source-gate record is no longer present; this handoff preserves the fail-closed disposition, but the missing evidence prevents promotion.

## Exact consumer and resolved identity

- Vanilla `common/characters/UDM.txt:2-13`: `UDM_boris`, display name `Boris Berman`, civilian `large = GFX_portrait_Boris_Berman`, Stalinist country-leader role.
- Vanilla `history/countries/UDM - Udmurtia.txt:1,101`: capital 399 (Izhevsk), recruits `UDM_boris` in the current 1936 country history.
- Vanilla `interface/_leader_portraits.gfx:7086-7089`: `GFX_portrait_Boris_Berman` points to generic `gfx/leaders/Europe/Portrait_Europe_Generic_1.dds`.
- Role resolution: Boris Zakharovich Berman, first secretary of the Udmurt regional committee from 28 December 1934 through 10 June 1937, covering 1936. The vanilla first/surname token is left unchanged.

## Candidate and rights evidence

The candidate is the 272x359 male image served by the Sakharov Center martirolog record and mirrored on Russian Wikipedia as `Файл:Борис Берман.jpg`. Sakharov and Wikimedia bytes match exactly: 55,281-byte JPEG, SHA-256 `9FA47A1288BDA065FBD33B749BCD378863767C92567430165C6AA4AA918E679F`, SHA-1 `E63C9660A6D13BAD263D63FD2AB3C4602AF44A9A`. The file metadata dates it `не позднее 1938 г.` and identifies the subject, but says the artist is unspecified.

The Russian Wikipedia file metadata explicitly marks the image `Добросовестное использование` (fair use), `NonFree=true`, and `Copyrighted=true`, with the source credited to `https://nekropole.info/ru/Boris-Berman`. The Sakharov page has no image licence or permission statement, and the upstream page's CC-BY page metadata does not grant image rights. This fails the grounded portrait rights gate even though identity, male subject, and 1936 role/date fit pass.

Exact URLs reviewed on 2026-08-15:

- `http://www.sakharov-center.ru/asfcd/martirolog/?t=page&id=3603`
- `http://www.sakharov-center.ru/asfcd/martirolog/photo/Auto/250399Y001733.jpg`
- `https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:%D0%91%D0%BE%D1%80%D0%B8%D1%81_%D0%91%D0%B5%D1%80%D0%BC%D0%B0%D0%BD.jpg`
- `https://upload.wikimedia.org/wikipedia/ru/8/8e/%D0%91%D0%BE%D1%80%D0%B8%D1%81_%D0%91%D0%B5%D1%80%D0%BC%D0%B0%D0%BD.jpg`
- `https://nekropole.info/ru/Boris-Berman`
- `https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D1%80%D0%BC%D0%B0%D0%BD,_%D0%91%D0%BE%D1%80%D0%B8%D1%81_%D0%97%D0%B0%D1%85%D0%B0%D1%80%D0%BE%D0%B2%D0%B8%D1%87`
- `http://www.knowbysight.info/BBB/07869.asp`

## Archive, crop, processing, and wiring state

- `docs/assets/portraits/006_independence_wave/` was not given a new original.
- All asset evidence remains flat under its existing sole `processed/` child; no subject subfolder was created.
- Crop processing was not entered because rights failed first; therefore no crop coordinates/equality JSON or `156x210` candidate was produced.
- No DDS, `.gfx`, portrait-specific wiring, character edit, central adapter, attestation, preflight, scenario registration, Join, localisation, event, or gameplay change was made.
- RunPod was not opened or operated. Native ImageGen was not invoked.

## Remaining blocker

Obtain a separate exact Boris Zakharovich Berman photograph with clear public-domain/redistributable rights, or written permission from the rights holder. Until then, the non-free image, vanilla generic texture, Boris Davidovich Berman, another Boris, a generic Udmurt face, and generated substitutes are all rejected.
