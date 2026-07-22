# Event 006 IW-009 Bavaria portrait visual/provenance audit

**Audit date:** 2026-07-22
**Audited commit:** `8b63c5a2e1a208f34b668dc5cadfe6040037b09a` (`Add Bavaria sourced portrait refinishes trial`)
**Scope:** read-only independent audit of the two grounded real-male portrait
refinishes in `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bavaria_held_schobert_trial_01/`.
Only this handoff was written. No asset, runtime DDS, `.gfx`, gameplay,
localisation, character, or manifest file was changed.

## Verdict

| Subject / consumer | Identity and visual result | Role/era fit | Rights/provenance | Overall | Can advance? |
|---|---|---|---|---|---|
| Heinrich Held — `GFX_portrait_BAY_independence_wave_state_council` | **PASS.** Exact real male identity remains recognizable in the source crop, raw edit, processed `156x210`, and native/4x review sheet. Hat, round spectacles, moustache, face geometry, age, suit, tie, and pose are retained; the result is an opaque brush-painted HOI4 portrait, not a photograph, sepia conversion, generic face, or female/advisor/`_small` asset. | **PASS.** Held was Bavarian Minister-President 1924–1933 and alive at the 1936 start; the civilian/state-council assignment is exact. | **PASS with attribution requirement.** Wikimedia Commons records the unchanged Keystone/NAC file as CC0; the direct NAC/Szukaj archive reuse policy allows copying, changing, and distributing public-domain/archive-owned copies, including commercially, while recommending source attribution. The underlying record was not machine-readable during this audit, so retain both archive and Commons links. | **PASS** | **YES, subject to parent wiring only after preserving this provenance and the stable consumer.** |
| Eugen Ritter von Schobert — `GFX_portrait_BAY_independence_wave_mountain_commandant` | **PASS visually.** Exact real male identity remains recognizable at full source/crop and native `156x210`; swept hair, moustache, eyes, face proportions, collar braid, visible decorations, tunic and pose are retained. The result has deliberate opaque brush planes and a quiet HOI4-style background, with no genericization, second person, invented face, female/advisor/`_small` asset, or photo/filter finish. | **PASS with abstraction caveat.** Würzburg-born Bavarian Army infantry officer, later VII Army Corps/11th Army commander, alive in 1936. He was not a specialist Gebirgstruppe officer; “mountain commandant” is an emergency passes/depots abstraction, not a claim of mountain-branch service. | **NEEDS_REVISION / fail closed.** NAC/Commons states free use and a Poland/US public-domain rationale, but the Commons page explicitly asks for first-publication evidence. Author and first-publication venue/date remain unknown. NAC’s general free-use statement does not identify this object’s exact rights bucket, so worldwide runtime promotion is not legally defensible without a direct NAC rights confirmation or documented first-publication chain. | **NEEDS_REVISION (rights blocker, not a visual failure)** | **NO. Hold the candidate and docs-only DDS; obtain NAC confirmation/first-publication evidence or a separately cleared replacement. No fallback is authorized.** |

The two candidates are not interchangeable: Held may advance once the parent
promotes the approved processed PNG/DDS, while Schobert remains blocked despite
passing the visual identity gate.

## Package inventory and exact hashes

All paths below are relative to the trial folder. Hashes are SHA-256. PNGs are
RGB, full opaque portraits unless noted; the two docs-only DDS files round-trip
byte-for-byte to their processed PNG pixel data.

### Heinrich Held

| Artifact | Dimensions / format | SHA-256 |
|---|---|---|
| `source_masters/BAY_heinrich_held_keystone_1933.jpg` | `2471x3623`, JPEG, 1,664,336 bytes | `35d1ee399c8c86efd024e8226a8effe97afc5fc0114c4a1186ad9cd4d6c3560d` |
| `crops/BAY_heinrich_held_crop_400_160_2070_2409.png` | `1670x2249`, RGB PNG | `11841151745e97e7398bef3c60481c0bfeefaba2b2d8225f3e3466d78f75cf3a` |
| `raw_imagegen_masters/BAY_heinrich_held_refinish_raw.png` | `1082x1454`, RGB PNG | `2ea1a1b30d0734d30d5306343eb8fee0648c103558f621f1f4119865e790de48` |
| `processed_png/BAY_heinrich_held_refinish_156x210.png` | `156x210`, RGB PNG, 53,830 bytes | `b2b5854d393020a3db5b7a0767f73244581f6f8a54b99149f33ce47b7321164d` |
| `docs_dds/BAY_heinrich_held_refinish_156x210.dds` | `156x210`, legacy one-level BGRA32, 131,168 bytes | `999857d191f7b088e11daa78fb29eadd0b514dc6da494a0102423c635e736e95` |

### Eugen Ritter von Schobert

| Artifact | Dimensions / format | SHA-256 |
|---|---|---|
| `source_masters/BAY_eugen_von_schobert_nac_1940.jpg` | `2315x3520`, JPEG, 1,016,112 bytes | `0512bb979b5bac234eac4c0c61f397664ba97e64cf1626ec95aa05d6d99e7f83` |
| `crops/BAY_eugen_von_schobert_crop_170_100_2145_2760.png` | `1975x2660`, RGB PNG | `9189ea5b8971b74f795d40e665025945e530197532286ec3f0b187a461d461a9` |
| `raw_imagegen_masters/BAY_eugen_von_schobert_refinish_raw.png` | `1080x1456`, RGB PNG | `d941289dba8eebb34419484d0483351e6d2a1066d835ace294ca2d21a1f8818c` |
| `processed_png/BAY_eugen_von_schobert_refinish_156x210.png` | `156x210`, RGB PNG, 56,940 bytes | `67ea312d6dccdb1a1dbdf2d94035f73816da179eb942ff34d76bbdca65f3063f` |
| `docs_dds/BAY_eugen_von_schobert_refinish_156x210.dds` | `156x210`, legacy one-level BGRA32, 131,168 bytes | `d2c9432e7918fca4f43d51c11b108ffeb65f5dd1aaad440123a49a0e22f66381` |

### Review sheets and canonical references

| Artifact | Dimensions / format | SHA-256 |
|---|---|---|
| `contact_sheets/BAY_held_schobert_source_crop_result_canonical_contact_sheet.png` | `1012x580`, RGB PNG | `85960b3437a8efc4358eee7c1b1f98f13a1001e60cbda4ba4708f0e7469d009` |
| `contact_sheets/BAY_held_schobert_source_crop_result_canonical_contact_sheet_4x.png` | `4048x2320`, RGB PNG | `7d486859792371ff97ccede7c1b1f98f13a1001e60cbda4ba4708f0e7469d009` |
| `vanilla_reference/portraits/leaders/den_thorvald_stauning.png` | `156x210` | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` |
| `vanilla_reference/portraits/leaders/ire_eamon_de_valera.png` | `156x210` | `ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0` |
| `vanilla_reference/portraits/commanders/generic_africa_land_1.png` | `156x210` | `17d875344719b09a03ef32cc3329971778a738c4ac20210f6cbb7394a1e7585f` |
| `vanilla_reference/portraits/commanders/generic_africa_land_3.png` | `156x210` | `76731af64301c3c68eee012a9eb9f001f4a11561e42bbb13cae0949ea5535b0b` |

The last four rows are the actual canonical files under
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/`.
The package metadata/prompts use the obsolete non-existent prefix
`.agents/skills/chaos-redux-event-assets/assets/leader_portraits/`; the hashes
match the real canonical files, but those path strings must be corrected before
the package is treated as self-contained final evidence.

For both DDS files I verified: magic `DDS `; header size `124`; declared
`156x210`; pixel format size `32`, flags `65`, fourCC `0`, 32-bit BGRA masks
`0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`; texture caps `0x1000`; exact
length `128 + 156*210*4 = 131168`; alpha range `255..255`; and decoded BGRA
payload equal to the processed PNG pixels.

## Subject reviews

### Heinrich Held — PASS

**Source and identity.** The unchanged local master is the direct 2,471x3,623
Commons upload of the Agencja Keystone View Company/Narodowe Archiwum Cyfrowe
image, dated 1 January 1933 (circa 1933). The Commons record identifies the
subject as German politician Heinrich Held and records CC0 1.0:

- [Commons file page — Heinrich Held, 1933](https://commons.wikimedia.org/wiki/File:Heinrich_Held,_1933.jpg)
- [NAC/Szukaj source record — object 473188](https://www.szukajwarchiwach.gov.pl/en/jednostka/-/jednostka/6270998/obiekty/473188)
- [Direct unchanged Commons upload](https://upload.wikimedia.org/wikipedia/commons/0/03/Heinrich_Held%2C_1933.jpg)
- [Bavariathek official biography](https://www.bavariathek.bayern/medien-themen/portale/geschichte-des-bayerischen-parlaments/person/118710060.html)

The Bavariathek record confirms Held was a Bavarian Landtag member and
Minister-President from 1924–1933. He was alive in 1936, so a civic/state
authority slot is role- and era-correct. The source master contains the NAC
band at the bottom; the exact crop `(400,160)-(2070,2409)` excludes that band
without retouching the identity input.

**Visual result.** At full source/crop size and the native `156x210` output,
Held remains unmistakable through the tall black hat, round spectacles,
straight moustache, broad nose/cheeks, frontal expression, patterned tie,
white collar, and dark suit. The processed result uses visible opaque brush
planes and a restrained warm gray-beige painted background consistent with the
canonical male leader references. It does not read as a raw photograph,
colorized photograph, sepia filter, generic oil filter, reconstructed face, or
advisor dossier card. No extra person, female presentation, flag, insignia,
modern prop, or identity-bearing invented detail is visible.

**Rights.** The Commons CC0 record is explicit. The official [Szukaj reuse
policy](https://www.szukajwarchiwach.gov.pl/en/ponowne-wykorzystanie) says
archival copies may be used in any way unless their description or scan says
otherwise, and that public-domain or archive-owned material may be copied,
changed, distributed, and used commercially; it recommends preserving archive,
fonds/reference, source-link, and retrieval-time attribution. NAC’s official
[archive-materials use page](https://www.nac.gov.pl/en/audiovisual-archive/providing-access/how-to-use-ndas-archive-materials/)
states that anyone may use collected archive materials free of charge except
items not allowed to be made available, while noting that an object’s legal
status is supplied when a copy is ordered; it also recommends citing the
archive.
The direct object page was blocked by an anti-bot interstitial during this
audit, so the exact row-level designation was not independently readable; the
CC0 dedication plus the archive’s unqualified reuse policy is nevertheless a
defensible rights basis. Keep both URLs and attribute “Agencja Keystone View
Company / National Digital Archive of Poland (NAC), object 473188” in durable
provenance.

### Eugen Ritter von Schobert — NEEDS_REVISION (rights blocker)

**Source and identity.** The unchanged local master is the direct 2,315x3,520
NAC/Commons portrait, dated July 1940, author unknown, catalogue/info `2-12702`.
The source is a real male subject, not a generated likeness:

- [Commons file page — Eugen von Schobert](https://commons.wikimedia.org/wiki/File:Eugen_von_Schobert.jpg)
- [NAC record family — catalogue/info 2-12702](https://www.audiovis.nac.gov.pl/obraz/2-12702/)
- [Direct NAC image endpoint recorded by the package](https://audiovis.nac.gov.pl/obraz/30585/7c907d5fd06cac7ac892ec5f9d66fdae/)
- [Direct unchanged Commons upload](https://upload.wikimedia.org/wikipedia/commons/d/d3/Eugen_von_Schobert.jpg)
- [Bavarikon official biographical record](https://verwaltungshandbuch.bavarikon.de/VWH/Schobert%2C_Eugen)

Bavarikon identifies Eugen Erich Siegfried Ritter von Schobert as born in
Würzburg on 13 March 1883, entering the 1st Bavarian Infantry Regiment, serving
in the Bavarian provisional national council in Munich in 1918–19, and later
commanding the VII Army Corps and 11th Army. He was alive at the 1936 scenario
start. The exact crop `(170,100)-(2145,2760)` retains the swept hair,
moustache, eyes, collar treatment, visible decorations, and upper tunic; the
NAC caption strip at the bottom is outside the crop.

**Visual result.** Full-size source/crop, raw edit, processed `156x210`, and
native/4x review all preserve the same person. The final face, hair part,
moustache, collar braid, decorations, and pose are readable at native size;
the warm gray-beige background and deliberate brush planes match the canonical
commander family. No generic face, second person, female/advisor presentation,
`_small` texture, invented medal/insignia, or photo/sepia/filter finish is
visible. The only visual/role caveat is that Schobert was an infantry/army
commander, not a specialist mountain officer; the existing label must remain an
emergency mountain-region abstraction rather than a historical branch claim.

**Rights and fail-closed decision.** The Commons page records the NAC statement
that its photos are public domain or State-Treasury-owned with a free-use
licence, and applies the Poland/US public-domain rationale. However, the same
page explicitly says “To uploader: Please provide where and when the image was
first published.” The local package has no first-publication venue/date,
author, or object-level NAC rights designation beyond that summary. NAC’s
general [official price-list note](https://www.nac.gov.pl/wp-content/uploads/2023/03/NAC_CZYTELNIA_Cennik_ang.pdf)
states that photographs available through its online archive are public domain
or State-Treasury-owned and grant free use on all known exploitation fields,
but it does not prove which branch applies to this unknown-author object. The
Poland/US PD assertion therefore remains conditional, and worldwide mod
redistribution is not legally defensible yet.

**Required resolution before runtime promotion:** obtain an object-level NAC
written confirmation that `2-12702` is State-Treasury-owned/free for derivative
redistribution, or document the first-publication venue/date and confirm the
applicable public-domain rule. Until then, keep this candidate and its DDS in
the trial evidence folder only. Do not silently substitute Ludwig Kübler or a
generated/vanilla face; no fallback is approved.

## Ownership and collision audit

The source-mode and subject-ownership gates were applied case-insensitively on
2026-07-22. Search variants included:

```text
Heinrich Held; Heinrich_Held; heinrich_held; Held, Heinrich
Eugen von Schobert; Eugen Ritter von Schobert; Eugen_Schobert;
Eugen_von_Schobert; eugen_ritter_von_schobert; eugen_von_schobert;
Eugen Siegfried Erich
```

### Vanilla and current Chaos Redux

The required roots were checked in both installed vanilla and Chaos Redux:
`common/characters/`, `history/countries/`, `common/country_leader/`,
`interface/`, `gfx/leaders/`, and `localisation/english/`.

- **Vanilla:** no exact identity character, recruitment, portrait, `.gfx`, or
  localisation hit for either subject in those roots. Vanilla’s incidental
  “Schobert” strings in unit-history text are not character or portrait
  ownership under the gate. No `Heinrich Held` owner exists.
- **Chaos Redux:** no source identity character/portrait owner exists. The only
  intentional matches are the Event 006 display-name localisations and stable
  target sprites. The live roster is generated under
  `BAY_independence_wave_state_council` (civilian large) and
  `BAY_independence_wave_mountain_commandant` (civilian/army large), with
  `gender = male`; those tokens are the intended consumers, not duplicate
  historical character IDs.
- **No Event 006 female/advisor/dossier/commander-`_small` file** is present in
  this trial. Current `gfx/leaders/006_independence_wave/` contains the two old
  runtime large DDS targets and protected Rupprecht, but no BAY `_small` DDS.

### Approved reference mods

The same roots/terms were checked in approved reference mods Kaiserreich
`1521695605`, `2265420196`, and `1458561226`.

- Kaiserreich `1521695605` contains a genuine separate
  `GER_eugen_von_schobert` character, recruited by `history/countries/GER -
  Germany.txt`, with `GFX_portrait_GER_eugen_von_schobert_army_large` and
  `..._small` in `interface/kaiserreich/portraits/GER_portraits.gfx`.
  This is a **reference-mod collision**, not an active Chaos Redux/vanilla
  owner; do not reuse its portrait or identifiers. If Kaiserreich is ever
  loaded alongside Chaos Redux, simultaneous identity ownership would require a
  load-order/transfer decision.
- Kaiserreich has incidental Heinrich Held prose in German event localisation
  but no `Heinrich Held` character, recruitment, portrait, or `.gfx` owner.
- Approved mods `2265420196` and `1458561226` returned no exact identity,
  recruitment, portrait, or `.gfx` hits for either person.

The reference collision does not invalidate an independent Chaos Redux source
portrait, but it must remain in the handoff so the parent does not claim a
global no-collision result.

## Intended stable consumers and current runtime state

The stable consumers were checked without editing them:

- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`
  creates the two male generated tokens and assigns
  `GFX_portrait_BAY_independence_wave_state_council` to civilian large and
  `GFX_portrait_BAY_independence_wave_mountain_commandant` to civilian/army
  large.
- `interface/006_independence_wave_region_01_portraits.gfx` registers the two
  stable sprites and points them to:
  `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds`
  and
  `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.
- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`
  displays `Heinrich Held` and `Eugen Ritter von Schobert` for those tokens.

The current target runtime files are still the prior generated/blocked assets,
not this trial’s docs-only DDS:

```text
gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_state_council.dds
  131168 bytes, SHA-256 C371F76669AFBC23E80D862AE8A97F20E6E15B89B4546667ECDB62134CDEE035
gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds
  131168 bytes, SHA-256 E1B37C14E058CCEB7C96280BCE14ACC809C9C6D9F572627171C28F4A48DE7EC6
```

Do not count those existing files as approval of this trial. The parent must
replace them only with an independently admitted candidate; no gameplay/GFX
change is part of this audit.

## Protected Rupprecht check

The protected route-owned runtime portrait remains unchanged:

```text
gfx/leaders/006_independence_wave/portrait_BAY_rupprecht_of_bavaria.dds
131168 bytes
SHA-256 7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B
```

This exact uppercase hash matches the parent requirement. Rupprecht is a
separate guarded restoration-route character and is not a substitute for Held
or Schobert.

## Blockers, documentation defects, and simplifications

1. **Schobert rights blocker:** first-publication evidence and object-level NAC
   rights status are unresolved. Keep `NEEDS_REVISION`; no runtime promotion.
2. **Canonical-reference path defect:** metadata/prompts name the obsolete
   `assets/leader_portraits/` prefix. The actual canonical root is
   `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/`.
   Hashes are correct, but the path strings need correction before final
   provenance promotion.
3. **Schobert role caveat:** the source proves Bavarian infantry/army command,
   not specialist mountain troops. Existing localisation may use “mountain
   commandant” only as the route’s emergency passes/depots abstraction.
4. **Stale historical plan references:** older Event 006 plan notes still list a
   BAY commander `_small` dossier surface. This trial intentionally contains no
   `_small`, advisor, or fallback output; the parent should reconcile those stale
   notes before final documentation cleanup.
5. **No fallback/simplification was introduced by this audit.** Held is a
   sourced real-person repaint; Schobert is retained as a rights-blocked sourced
   candidate, not replaced by a generic, generated, female, advisor, or invented
   identity.

## Validation evidence

- Read the parent Event 006 asset prompt, `AGENTS.md`, the complete
  `chaos-redux-event-assets` skill, and the canonical vanilla reference
  README/CATALOG plus leader/commander portrait families.
- Recomputed all source, crop, raw-master, processed-PNG, docs-DDS, and review
  sheet SHA-256 values; they agree with the package hash ledger. Separately, the
  canonical reference path strings in metadata/prompts are stale (the binary
  hashes themselves are correct). The contact sheets were reviewed at native
  and 4x nearest-neighbour scale.
- Verified both DDS legacy headers, exact lengths, declared dimensions, BGRA
  masks, texture caps, alpha range, and decoded-PNG pixel equality.
- Checked full and native visual identity, head-and-shoulders framing, male
  presentation, recognizable likeness, source-visible clothing/details,
  restrained painted finish, and absence of generic/female/advisor/`_small`
  substitutions.
- Checked exact identity/name-order/title variants across installed vanilla,
  current Chaos Redux, and approved reference mods. The Kaiserreich Schobert
  character collision is recorded above; no active vanilla/Chaos Redux owner
  was found.
- Recomputed the protected Rupprecht runtime hash; it remains
  `7F0AF64FDF4FECD49DF454D1198935BB3CE6A8F74AFC1AC82F8223704EAAAD2B`.

## Parent handoff

- Admit Held’s processed PNG/DDS only after preserving the source, crop,
  archive/Commons URLs, CC0/NAC attribution, and stable sprite target.
- Hold Schobert at `NEEDS_REVISION` until NAC confirms the exact object’s free
  derivative-redistribution status or first-publication evidence closes the
  Poland/US PD chain. Do not wire or substitute it meanwhile.
- Correct the four stale canonical reference paths in the package metadata and
  prompts, then rerun the package hash ledger before any final promotion.
- Keep Rupprecht byte-identical and keep this audit’s no-advisor/no-`_small`
  boundary intact.
