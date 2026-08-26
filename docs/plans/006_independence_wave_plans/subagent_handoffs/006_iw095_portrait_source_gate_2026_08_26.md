# Event 006 IW-095 Dahomey portrait source gate handoff (2026-08-26)

## Scope and disposition

This handoff covers the bounded portrait source gate for IW-095 Dahomey (`DAH`), current anchor state `776`, French former host, and 1936 opening.

Disposition: `research_only_fail_closed_source_candidate_hold`.

The selected source is an authentic institutional body candidate, the Abomey royal/customary court. The source predates the opening, but it does not identify a 1936 officeholder or prove an independent Dahomey government in 1936.

No runtime source placeholder, processed 156x210 portrait, DDS, `.gfx` entry, character consumer, styled final, or central package admission was created.

## Selected institutional source

The candidate is the Abomey royal/customary court represented by the royal thrones and reception court at the palace of Guézo in Abomey. It is recorded as an institution, not as a person and not as a generic African substitute.

Primary source: Albert-Kahn collections, inventory `A63516S`, <https://collections.albert-kahn.hauts-de-seine.fr/document/trones-royaux-d-abomey-guezo-glele-behanzin-agoliagbo-devant-la-salle-de-reception-ajalala-de-la-cour-du-palais-de-null-guezo-jalalahennou/617a7a44cf8b8968b3382868>.

Photographer: Frédéric Gadmer.

Mission: `1930 - Dahomey - RP Francis Aupiais et Frédéric Gadmer - (9 janvier-14 mai)`.

Date: 20 February 1930.

Place: Abomey, Dahomey (current Benin), Africa.

The collection caption names the royal thrones of Guézo, Glé-Glé, Béhanzin, and Agoliagbo and identifies the palace reception court. The source is six years before the 1936 opening and supports period-authentic Abomey royal institutional material.

The source does not establish which person held authority in 1936, does not establish an independent state in 1936, and contains no person or face. It therefore cannot be wired to a named country leader or presented as a 1936 government portrait without a parent-approved institutional role abstraction.

## Rights and attribution gate

The captured Albert-Kahn record states `Soumis au droit d'auteur opérateur - salarié` and `Librement réutilisable (CC-BY-4.0)`.

The captured Commons import and API state `CC BY-SA 4.0` and attribute the same Albert-Kahn collection and Frédéric Gadmer.

The two public records disagree on the licence. The source is archived for research, but redistribution as a runtime portrait remains blocked until the parent resolves the discrepancy and records the accepted attribution text.

Captured source pages and API evidence are retained under `docs/assets/portraits/006_independence_wave/processed/`.

## Archive outputs

The archive preserves the required flat parent with the existing single `processed/` subfolder and no new child folder.

The untouched Commons original is `docs/assets/portraits/006_independence_wave/iw095_dah_abomey_royal_customary_body_source_2026_08_26_original.jpg`.

The original decodes as RGB JPEG, `2560x1899`, 4,006,345 bytes, SHA-256 `0310f6cc149fed8fb8e2b8322dc6e37723c056c3524e780f32838cb0bed914a8`, and Commons SHA-1 `4a87fa41927cbcd156a7931aeefbdff51c04e50b`.

The exact source crop is `docs/assets/portraits/006_independence_wave/iw095_dah_abomey_royal_customary_body_source_2026_08_26_source_crop.png`.

The crop is RGB PNG, `1411x1899`, 3,989,440 bytes, SHA-256 `a1742dff3bb1a3c238fa22f42abefe6af9b1be1391686835ac4ca77f5d88812a`, and rectangle `(574, 0, 1985, 1899)`.

The crop evidence JSON is `docs/assets/portraits/006_independence_wave/processed/iw095_dah_abomey_royal_customary_body_source_2026_08_26_source_crop_evidence.json` with SHA-256 `036b8db59a3189f4e7ac9fed2b24bfcd48b88a9ed936c47707942f56610132da`. It records `decoded_pixels_equal=true`, matching RGBA hash `47d819c5b7b5a817157012829e5ab9fa7809b573b3b4c55a3dd9f1743e7de646`, and manual crop processing with Pillow 11.1.0.

The 4x nearest framing review is `docs/assets/portraits/006_independence_wave/processed/iw095_dah_abomey_royal_customary_body_source_2026_08_26_source_review_4x_nearest.png` with dimensions `624x840`, 987,962 bytes, and SHA-256 `db6dc874a8703598e522fb4ab6ea1bb2295801b8a7694c7b9e745384f5b1cf3a`.

The framing review passes for an institutional court/evidence image because it retains the central throne pair and palace context. It fails the ordinary named-person portrait criterion because no person or face appears.

No file under `docs/assets/portraits/006_independence_wave` has `156x210` in its name, and no 156x210 output is retained.

## Evidence manifest and source records

The source manifest is `docs/assets/portraits/006_independence_wave/processed/iw095_dah_portrait_source_manifest_2026_08_26.json`.

The rights and role note is `docs/assets/portraits/006_independence_wave/processed/iw095_dah_abomey_royal_customary_body_source_rights_role_review_2026_08_26.md`.

The captured primary archive page is `iw095_dah_abomey_royal_customary_body_source_albert_kahn_page_2026_08_26.html`, 53,086 bytes, SHA-256 `4f5fdc9f53ceab8a3d7190dd7ce3a7b4b3fd4761cba99ebb07abb19977a53b5b`.

The captured Commons page is `iw095_dah_abomey_royal_customary_body_source_commons_page_2026_08_26.html`, 110,057 bytes, SHA-256 `45fa817c15dac5518b7fe7b8ab0cdcd432d1551218e66ad84197a7a4c07a25c8`.

The captured Commons API record is `iw095_dah_abomey_royal_customary_body_source_commons_api_2026_08_26.json`, 5,402 bytes, SHA-256 `d2208aa4b90825472bf3f22b784d662b4509cf6fbd76ba6553f77e821fe55082`.

## Vanilla and existing-consumer review

Installed vanilla binds `DAH` to `countries/Dahomey.txt`, capital `776`, and the 1936 neutral opening has only generic advisor/high-command/theorist characters. `common/characters/DAH.txt` has no named country leader, corps commander, or field marshal and repeatedly marks large portraits as missing.

The installed vanilla leader reference family was inspected through the canonical contact sheet. `africa_generic_1.png` and related references are technical 156x210 framing references only and are not identity candidates.

The Event 012 Africa priority-member roster and `.gfx` wiring contain no DAH-specific grounded portrait consumer. No existing Event 006 archive entry duplicates A63516S or the Abomey royal/customary body candidate.

No exact IW-095 character identifier, institutional consumer, portrait sprite name, or runtime path is currently accepted by the parent package.

## Runtime and replacement state

`source_placeholder`: not promoted because the institutional role and rights gate remain unresolved.

`styled_final`: not requested and not created. RunPod was not opened or operated.

`replacement_pending`: false because no source-placeholder consumer was accepted.

`PNG`: only the untouched source and exact evidence crop are retained; no 156x210 output is retained.

`DDS`: not run because there is no approved runtime consumer and rights are unresolved.

`.gfx`: not changed because an orphaned sprite would be unsafe.

`characters`: not changed because character identity and role ownership remain with the parent package and no IW-095 institutional token exists.

`central admission`: unchanged and not requested.

## Blocker and next owner action

The parent must decide whether an Abomey royal/customary court is an acceptable authentic institutional body for IW-095's provisional government and must resolve the Albert-Kahn/Commons licence discrepancy before any runtime promotion.

If the parent accepts that body and rights basis, the portrait worker can create a package-local source-placeholder consumer with an exact character id, portrait-specific `.gfx`, DDS conversion, and a new runtime manifest. The source must not be described as a named 1936 leader or independent restored Dahomey.

If the parent requires a named 1936 officeholder instead, this source gate remains blocked and a different exact male source with period role continuity is required.

