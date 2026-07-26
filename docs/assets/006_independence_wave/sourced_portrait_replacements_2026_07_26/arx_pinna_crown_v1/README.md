# IW-018 ARX Pietro Pinna Parpaglia crown-route portrait candidate

This is a source-preserving candidate for the Sardinian crown consultative
council role. It is not runtime admission. No DDS, `.gfx` edit, character edit,
advisor icon, small portrait, or generated replacement was wired.

## Evidence chain

- Primary source: `source/ARX/Img024PPP.jpg`, an unchanged 2477x3500 Commons
  image of Pietro Pinna Parpaglia, SHA-256
  `8588dcb39daf1e5840542fef851065763c2613931aadb74fd4ea867d27c115de`.
- Attribution/license: [Img024PPP, Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Img024PPP.jpg), uploader C. E. Pinna P., CC BY-SA 4.0. Preserve attribution and share-alike notice with any later promotion.
- Identity corroboration: the separate unchanged `Pietro_Pinna_Parpaglia_source.jpg`
  is the 642x483 Commons archival copy credited to the Order of Military Italy
  source, with `PD-Italy` and `PD-1996`; it is retained only as corroboration.
- Role evidence: Pinna Parpaglia was born in Pozzomaggiore, Sardinia, in 1891,
  and was active as an Italian air-force general in 1936. This supports a
  Sardinia-linked military-administrative subject, but does not by itself prove
  a Savoy/dynastic crown-council officeholder; the strict crown route remains
  unresolved.
- Ownership blocker: the source audit found an exact Kaiserreich character
  owner, `SRD_pietro_pinna_parpaglia`, in `common/characters/SRD characters.txt`
  with history, localisation, and GFX consumers. This candidate cannot be
  reused for Event 006 unless the external-owner collision is removed by a
  separately approved design decision; no such decision exists.
- Exact crop: `crops/ARX/Pietro_Pinna_Parpaglia_archival_crop_final.png`,
  coordinates `(600,900,1450,2050)`, with equality JSON in `metadata/ARX/`.
- ImageGen repaint: `repaints/ARX/Pietro_Pinna_Parpaglia_identity_preserve_imagegen.png`,
  SHA-256 `194c2938f5f2772954347a8dd26f5962eb4bcdfe8f5f2dfdd70e11f20cfaec50`.
- Deterministic candidate: `processed/ARX/Pietro_Pinna_Parpaglia_156x210.png`,
  SHA-256 `a0429c75ebf0b575668dbcdfb7aa45a2576b85e6aa4f6fb80e6c04ca11343b2f`,
  role family `leader`, processor status `candidate_requires_visual_approval`.

## Required gate before wiring

An independent reviewer may compare the unchanged source, exact crop, raw
repaint, processed candidate, and the country-leader reference pack, then record
separate likeness, HOI4-style, framing, provenance, ownership, and crown-role
fit results, but the external Kaiserreich owner and unresolved strict crown
role already block admission. The candidate remains evidence-only and does not
authorize changing `ARX_sardinian_crown_consultative_council` or adding a
runtime DDS.
