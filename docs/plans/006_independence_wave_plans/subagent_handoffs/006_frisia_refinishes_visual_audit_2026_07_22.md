# Event 006 Frisia portrait-refinish visual audit

Audit date: 2026-07-22  
Auditor: `chaosx_generated_event_art`  
Scope: read-only visual and provenance audit of the two grounded real male
Frisia portraits in
`docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/frisia/`.
No runtime, GFX, gameplay, localisation, manifest, skill, or source asset was
edited. This handoff is the only file changed by this audit.

## Controlling rule and disposition

AGX/Frisia is a grounded real polity. Douwe Kalma and Pieter Reenalda therefore
must remain sourced real male identities. ImageGen is permitted only as an
identity-preserving HOI4 painted treatment of the unchanged source photograph;
it may not reconstruct, substitute, or materially redraw either face.

Both candidates fail closed on exact same-person likeness. The raw ImageGen
masters and the 156x210 outputs preserve broad cues (male subject, hair, suit or
uniform, moustache where applicable) but materially drift in face geometry and
pose. Neither portrait is admitted to runtime or DDS conversion from this
package. The package status remains `needs_user_review`/blocked for likeness,
not a permission to use a weaker substitute.

## Separate verdicts

| Criterion | `leader_AGX_douwe_kalma_156x210.png` | `commander_AGX_pieter_reenalda_156x210.png` | Evidence |
|---|---|---|---|
| Exact same-person likeness | **FAIL — material face drift; closed** | **FAIL — material face drift; closed** | Kalma changes the source's slight three-quarter angle toward a straighter near-frontal view; eye spacing, nose bridge/tip, mouth contour, ear shape, and jaw taper do not track the passport source. Reenalda changes the source's angled view toward near-frontal; eye placement, nose/ear contours, jaw width, and moustache shape/extent drift. The changes remain visible in both raw masters and the 156x210 outputs. |
| Male-only compliance | **PASS** | **PASS** | Both source masters, raw masters, and processed outputs depict the same requested male-presenting role; no female, generic, or opposite-gender replacement is present. |
| Source / era / role fit | **PASS** (strong) | **PASS** (with role caveat) | Kalma: real Frisian writer/nationalist (1896–1953), 1922 passport source, alive in 1936, defensible civic-leader fit. Reenalda: real first officer of the Koninklijke Paketvaart Maatschappij (b. 1887), 1911 uniform source, alive in 1936, strong maritime/coastal-command visual fit; the source documents a civilian shipping officer rather than a regular navy commission, so the parent should retain that role note. |
| Head-and-shoulders crop | **PASS** | **PASS** | Both processed files are exactly 156x210 and frame head, shoulders, and restrained upper torso without extra people or scene dependence. |
| HOI4 painted style at full and 156x210 | **PASS** | **PASS** | Full raw masters use quiet pale warm-gray painted backgrounds, controlled contrast, subdued period brush texture, and readable silhouettes. Native outputs retain these traits and match the 156x210 leader/commander family treatment. Kalma is muted warm color; Reenalda is muted neutral grayscale consistent with the grayscale source. |
| No invented stereotypes / fantasy elements | **PASS** | **PASS** | Ordinary source-supported dark civilian suit/white shirt/tie and archival maritime uniform remain; no Frisian costume, flag, rank invention, ribbon, medal, prop, text, watermark, modern item, extra person, fantasy, or caricature is visible. |
| Rights / source traceability | **PASS for provenance; runtime still blocked** | **PASS for provenance; runtime still blocked** | Unchanged masters are retained and hash-identical to the Northwestern Europe source package. Parent ledger records Commons/Tresoar source pages, collection context, dates, photographer uncertainty, and public-domain/no-restriction basis. New prompts and ImageGen masters are retained, so the transformation chain is auditable. Preserve the parent ledger's territorial-rights caveat in any later release review. |

## Visual evidence

### Douwe Kalma

- Unchanged source: `545x667` RGB passport photograph. The face is narrow and
  slightly turned, with a distinct swept hairline, long straight nose, thin
  mouth, and tapering jaw.
- ImageGen master: `1081x1455` RGB, painted and clean, but turns the head toward
  near frontal and redraws the eye geometry, nose, ear, mouth, and jaw. The
  generated subject reads as a plausible young man, not an exact repaint of the
  source identity.
- Native output: `156x210` RGB; the same drift remains readable at game size.
  The crop and style pass independently, but they cannot cure identity drift.

### Pieter Reenalda

- Unchanged source: `1243x1787` grayscale uniform portrait. The source has a
  distinctive angled head, broad moustache, eye spacing, nose profile, and
  square lower face.
- ImageGen master: `1080x1456` RGB, painted and clean, but changes the head angle
  toward near frontal and redraws the eye placement, nose/ear contours, jaw
  width, and moustache shape/extent. It preserves a maritime-uniform concept,
  not the exact source face.
- Native output: `156x210` RGB; the face drift is still material at native size.
  Crop, uniform read, and style pass independently.

## Canonical HOI4 comparison

The canonical leaders family and commanders family were inspected through their
full contact sheets and native references. Both families are full `156x210`
portraits with quiet painted backgrounds, controlled value ranges, restrained
texture, and readable head-and-shoulders silhouettes. The nearest civilian
leader style checks were `den_thorvald_stauning.png`,
`ire_eamon_de_valera.png`, and `ice_sveinn_bjornsson.png`; the nearest maritime
commander checks were `generic_africa_navy_1.png` and
`generic_africa_navy_2.png`. The Frisia outputs meet the style/canvas treatment
at full and native size, but style similarity does not authorize face drift.

## Source and rights chain

The exact source package is
`docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/northwestern_europe/`.
Its ledger identifies:

- Kalma: [Commons source](https://commons.wikimedia.org/wiki/File:DouweKalma1922.jpg),
  [Tresoar collection record](https://tresoar.nl/zoeken/collectie/84de852d-f5ae-421d-b541-1a85db913ccd),
  passport photograph dated 27 Sep 1922, photographer unknown, public-domain
  record/no restrictive license noted.
- Reenalda: [Commons source](https://commons.wikimedia.org/wiki/File:Eerste_officier_KPM_Pieter_Reenalda_in_uniform,_1911,_archiefnr_318-29.jpg),
  [Tresoar collection record](https://tresoar.nl/zoeken/collectie/2fec947d-31eb-4806-93cd-02510a98fc09),
  KPM first-officer portrait dated 1911, photographer unknown, public-domain
  record.

The current Frisia package correctly retains the unchanged source masters,
source-mode declaration (`user-provided source image` from the named source
package), prompts, ImageGen masters, processed previews, and review sheet. It
contains no DDS and no runtime registration, as stated by its explicit scope.

## Exact files and SHA-256 hashes inspected

### Current Frisia package

| File | Dimensions / type | SHA-256 |
|---|---:|---|
| `frisia/manifest.md` | Markdown | `64afac322c10b90046d214897d9bb2b12582d6566d949e31b555c3da9b538171` |
| `frisia/prompts/leader_AGX_douwe_kalma_imagegen.txt` | Prompt | `9ffb61bdeb737aa68272edeeafbfea0ef2d9423308965382d413e06ce6d84786` |
| `frisia/prompts/commander_AGX_pieter_reenalda_imagegen.txt` | Prompt | `348eacf340cf148edaef3537327ec5b64968471725ddbf211367c1ff3bda67ea` |
| `frisia/source_masters/AGX_douwe_kalma.jpg` | 545x667 RGB | `d8ce5c3cfe7d3b29bb9422139b21e83504f71dfd64a8fc0a821ef7d9b6501d9f` |
| `frisia/source_masters/AGX_pieter_reenalda.jpg` | 1243x1787 grayscale | `2830fdc7d56040c2a3fa6a6f686bfd73126612786cc6eba80d428863190c488f` |
| `frisia/imagegen_masters/leader_AGX_douwe_kalma_imagegen_master.png` | 1081x1455 RGB | `05ca0a2794fac5819f0c2c143b3e9f833d8139a218128d5552c10f0c6c14f5aa` |
| `frisia/imagegen_masters/commander_AGX_pieter_reenalda_imagegen_master.png` | 1080x1456 RGB | `ea0209e84fecb5702df53dbf82da70d1cb587fb2c218006216c8260c765cef7a` |
| `frisia/processed_png/leader_AGX_douwe_kalma_156x210.png` | 156x210 RGB | `628157f9ec2dd956186a321d0260628f126637494ebc3246e8749f12544e9c89` |
| `frisia/processed_png/commander_AGX_pieter_reenalda_156x210.png` | 156x210 RGB | `d38acb3fe1432b378bbebe5d88ba3b55d2100397d6bb19ffd7716e67434fea05d5` |
| `frisia/review/contact_sheet.png` | 570x520 review sheet | `02479866a9e5e940769cee2b85db51ad41e57358e14070799488a7c90ec42adf` |

### Unchanged source/provenance package and prior treatment evidence

| File | SHA-256 |
|---|---|
| `northwestern_europe/manifest.md` | `8a9ccd4bc5d5f3cde7fc21c7df5bdcfe2dbcb7f16cdaa1a130804e06eb2fd467` |
| `northwestern_europe/source_hashes.sha256` | `58038eb62ec9bbd02a0c8fb457a163db1dd1da835c544c0d8145329eef62c099` |
| `northwestern_europe/source_masters/AGX/AGX_douwe_kalma.jpg` | `d8ce5c3cfe7d3b29bb9422139b21e83504f71dfd64a8fc0a821ef7d9b6501d9f` |
| `northwestern_europe/source_masters/AGX/AGX_pieter_reenalda.jpg` | `2830fdc7d56040c2a3fa6a6f686bfd73126612786cc6eba80d428863190c488f` |
| `sourced_portrait_treatments_2026_07_22/metadata/AGX_douwe_kalma.json` | `7c4c830552ef47d8de2db48ea10679cc34ffe5aa2f9908360716e12a6b8d3023` |
| `sourced_portrait_treatments_2026_07_22/metadata/AGX_pieter_reenalda.json` | `556866cc24a772d40c9206a73bf7b996800fd49cc9e9a486f149f0d2cb03db8c` |
| `sourced_portrait_treatments_2026_07_22/visual_review.md` | `a1cc03121f3da2e2b2f86f447e95a7197db0c3b8aa655dcf8aa5b4ac72e4a8e8` |
| `sourced_portrait_treatments_2026_07_22/review_sheets/AGX_douwe_kalma_review.png` | `e1f13b9ccd012fcae2a96dd51b151f004edb0223be74fdd2ebf62d9befd06af7` |
| `sourced_portrait_treatments_2026_07_22/review_sheets/AGX_pieter_reenalda_review.png` | `d8f00e404a28d86e9e5337ce08229c51a7dc11308aaad0e82a158f65f42857c7` |

### Canonical reference root

| File | SHA-256 |
|---|---|
| `vanilla_reference/README.md` | `e6a2f4a4cfdce04d4c0682103b6c5d38a98557d40e7491cb9f3a9a869eb59c52` |
| `vanilla_reference/CATALOG.md` | `72fdd8110bdfc42cce194afae44d45e6373501342b5dca5049594be4fdd1aa37` |
| `vanilla_reference/portraits/leaders/contact_sheet.png` (all 8 leader refs) | `8966ae351d1fe8fc13d47ca1c59ec3d8a34da9101ce5fd65f7acff3421bd0401` |
| `vanilla_reference/portraits/commanders/contact_sheet.png` (all 5 commander refs) | `d62a4b80265533c93669a5eef267dff8db2021a01c1f31dcb73102bf1cc20ca9` |
| `vanilla_reference/portraits/leaders/ire_eamon_de_valera.png` | `ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0` |
| `vanilla_reference/portraits/leaders/den_thorvald_stauning.png` | `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6` |
| `vanilla_reference/portraits/leaders/ice_sveinn_bjornsson.png` | `860726d268873f21ae0dbd6fb170482f50fad6393882b97b2b7b7a1814189d14` |
| `vanilla_reference/portraits/commanders/generic_africa_navy_1.png` | `6351227cc9a7416698d2b94e87ea07fb1cf97afe8874cbee2015a3362cfcb0ec` |
| `vanilla_reference/portraits/commanders/generic_africa_navy_2.png` | `a608d7554187cd944130862e09ed4279fd5311f16a6735d07cf357148d11250f` |

## Method and residual risks

- Read `AGENTS.md` and the complete current
  `.agents/skills/chaos-redux-event-assets/SKILL.md`, including the grounded
  portrait source-mode gate, real-person sequence, canonical reference rules,
  and 156x210 commander requirement.
- Inspected the complete current Frisia package, both unchanged source-master
  copies and their source ledger/hash package, the prior AGX metadata/review
  evidence, and the canonical leader/commander reference root only.
- No automated face-recognition score is treated as acceptance; the material
  geometry/pose drift is directly visible in source, raw, contact-sheet, and
  native-size comparisons.
- The main residual blocker is identity preservation. A future revision must
  retain the source eye/nose/mouth/jaw geometry and head angle while adding only
  the painted finish and crop. Do not convert these candidates to DDS or wire
  them until a human accepts exact likeness.
- A later parent release review should preserve the source ledger's rights and
  role caveats, especially that Reenalda is a KPM first officer rather than a
  documented military navy general.

## Handoff status

`leader_AGX_douwe_kalma_156x210.png`: `needs_user_review` — **blocked on
material face drift**.  
`commander_AGX_pieter_reenalda_156x210.png`: `needs_user_review` — **blocked on
material face drift**.

No final DDS or `.gfx` handoff is authorized from these candidates.
