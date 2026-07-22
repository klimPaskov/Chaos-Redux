# IW-009 Bavaria Held/Schobert sourced portrait refinishes — trial 01

Date: `2026-07-22`  
Owner: sourced visual asset subagent  
Disposition: **two candidates produced; both `needs_independent_review`; no runtime wiring**

## Scope and outputs

Owned paths only:

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/`
- this handoff

The package retains unchanged source-master copies, exact source crops, raw
built-in ImageGen masters and frozen prompts, native `156x210` processed PNGs,
docs-only DDS files, per-asset JSON metadata, source/crop/result/canonical
contact sheets at native and 4× nearest-neighbour review sizes, and SHA-256
inventory. No runtime DDS, `.gfx`, gameplay, localisation, character,
advisor/dossier, `_small`, flag, or protected asset was edited.

## Candidates

| Role | Source / provenance and rights | Crop | Output | Stable sprite / runtime target | Status |
|---|---|---|---|---|---|
| Heinrich Held, civic country leader | NAC/Agencja Keystone View Company; Commons [file page](https://commons.wikimedia.org/wiki/File:Heinrich_Held,_1933.jpg), direct NAC record [object 473188](https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6270998/obiekty/473188), direct original [JPG](https://upload.wikimedia.org/wikipedia/commons/0/03/Heinrich_Held%2C_1933.jpg); circa 1933, CC0 1.0 recorded by Commons. Local source SHA-256 `35d1ee399c8c86efd024e8226a8effe97afc5fc0114c4a1186ad9cd4d6c3560d`. | Exact `(400,160)-(2070,2409)`, `1670x2249`, local crop SHA-256 `11841151745e97e7398bef3c60481c0bfeefaba2b2d8225f3e3466d78f75cf3a`. | Processed PNG SHA-256 `b2b5854d393020a3db5b7a0767f73244581f6f8a54b99149f33ce47b7321164d`; docs-only DDS SHA-256 `999857d191f7b088e11daa78fb29eadd0b514dc6da494a0102423c635e736e95`. | `GFX_portrait_BAY_independence_wave_state_council`; deferred `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds`. | `needs_independent_review` |
| Eugen Ritter von Schobert, army/corps commander | NAC catalogue/info `2-12702`; Commons [file page](https://commons.wikimedia.org/wiki/File:Eugen_von_Schobert.jpg), NAC [record](https://www.audiovis.nac.gov.pl/obraz/2-12702/), direct original [JPG](https://upload.wikimedia.org/wikipedia/commons/d/d3/Eugen_von_Schobert.jpg); July 1940, unknown author; NAC free-use statement and Commons Poland/US public-domain rationale recorded, with first-publication uncertainty. Local source SHA-256 `0512bb979b5bac234eac4c0c61f397664ba97e64cf1626ec95aa05d6d99e7f83`. | Explicit `(170,100)-(2145,2760)`, `1975x2660`, local crop SHA-256 `9189ea5b8971b74f795d40e665025945e530197532286ec3f0b187a461d461a9`. | Processed PNG SHA-256 `67ea312d6dccdb1a1dbdf2d94035f73816da179eb942ff34d76bbdca65f3063f`; docs-only DDS SHA-256 `d2c9432e7918fca4f43d51c11b108ffeb65f5dd1aaad440123a49a0e22f66381`. | `GFX_portrait_BAY_independence_wave_mountain_commandant`; deferred `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`. | `needs_independent_review` |

## Reverification and ownership evidence

Direct source pages were reopened on `2026-07-22`. Held’s Commons page records
the original `2471x3623` Keystone master, circa 1 January 1933, source archive,
author/agency, and CC0 1.0 dedication. Schobert’s Commons page records the
original `2315x3520` NAC image, July 1940 date, unknown author, NAC catalogue
`2-12702`, public-domain/free-use statement, and the caveat that Commons asks
for first-publication evidence for the US analysis. Historical fit was checked
against the Deutsches Historisches Museum/Bavariathek Held biography and
Deutsche Biographie/Commons Schobert records: Held was Bavarian Minister-
President 1924–1933; Schobert was Würzburg-born, entered the Royal Bavarian
Army, commanded Bavarian infantry formations, and was alive in 1936.

Exact and variant identity terms were searched case-insensitively in installed
vanilla and current Chaos Redux `common/characters`, `history/countries`,
`common/country_leader`, `interface`, `gfx/leaders`, and
`localisation/english`. Vanilla returned no Held or Schobert identity,
character, recruitment, portrait, or localisation hits. Chaos Redux returned
no source-identity character/portrait owner; only the intended generated BAY
package tokens, stable GFX consumers, and display-name localisations resolve.
No transfer guard applies because no origin character exists. Full terms and
paths are in both package metadata records.

## Reference and processing evidence

The required canonical reference roots were inspected directly:

- `assets/vanilla_reference/README.md` and `CATALOG.md`;
- `assets/leader_portraits/README.md`, `REFERENCE_MANIFEST.md`, and role contact sheets;
- canonical leader family sheet for Held style (`den_thorvald_stauning`, `ire_eamon_de_valera`);
- canonical commander family sheet for Schobert style (`generic_africa_land_1`, `generic_africa_land_3`).

Offline `Portrait modding`, `Graphical asset modding`, `Character modding`, and
`Interface modding` wiki snapshots were read, together with vanilla BAY
character/GFX definitions and vanilla generic army-portrait precedents. The
required portrait target is full `156x210`; no small portrait was produced.

ImageGen was used only in the allowed real-person edit mode: each exact crop
was the sole identity input, and canonical portraits were style-only inputs.
The raw results visibly use opaque painted planes and restrained brush texture,
not a raw photograph, sepia conversion, or generic filter. Native processed
PNG and docs-only DDS pixels match exactly; DDS headers are valid legacy
uncompressed BGRA32 (`156x210`, one level, 131168 bytes).

## Protected runtime check

The protected BAY Rupprecht runtime portrait was not touched and was verified
after production at SHA-256:

`7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`

## Blockers and required parent action

Both candidates require an independent review before any runtime copy or GFX
wiring. Review Held’s likeness and Commons/archival reuse terms. Review
Schobert’s likeness, first-publication rights uncertainty, and the infantry
versus mountain-command role abstraction. The producing subagent does not
approve its own candidate. No fallback or substitute is authorized; if a
reviewer rejects a candidate, the parent must retain the rejection as a
blocker or acquire a separately defensible sourced identity.

No simplification was made within the two requested roles. The only deferred
work is independent approval and, if approved, parent-owned runtime promotion
to the existing stable paths.
