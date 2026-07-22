# Event 006 AJX grounded portrait source retry

Date: 2026-07-22

Scope: source-only replacement package for the two fictional grounded Saar
identities currently consumed by Event 006 Independence Wave:

- `AJX_friedrich_hoffmann` - civic / constitutional leader surface
- `AJX_karl_becker` - industrial / security commander surface

This package contains two unchanged archival JPEG source masters, explicit
head-and-shoulders PNG crops, repository-standard 156x210 DDS outputs, a
contact sheet, and source/ownership documentation. No character, localisation,
GFX, interface, history, event, runtime `gfx/`, advisor icon, or `_small`
texture was edited. The parent implementation agent owns identity transfer,
final sprite wiring, and any runtime copy.

## Status vocabulary

- `source_ready`: the unchanged source bitstream is present, attribution and
  rights basis are recorded, identity and requested role fit are defensible,
  and the source-ready crop plus DDS are available. This is not runtime
  approval; the parent still owns contextual review and wiring.
- `needs_user_review`: a usable source package is present, but a named date,
  era, rights, role, or visual-context issue remains unresolved. Do not wire
  without an explicit review decision.
- `blocked`: no defensible source was acquired, or the only lead failed a
  required identity/rights/role gate. No substitute portrait is authorised.
- `rejected_external_mod_owner`: a candidate is rejected because another
  project's live character/GFX owner is binding. The non-blocking Hoffmann
  historical-person overlap with approved mod `1458561226` is documented
  separately below and is not treated as a rejection under the parent task
  clarification.

## Role ledger

| Current fictional consumer | Grounded candidate | Status | Historical / role fit | Source master | Source dimensions | Source SHA-256 | Crop coordinates (x1,y1,x2,y2) | PNG / DDS | Era and rights uncertainty |
|---|---|---|---|---|---:|---|---|---|---|
| `AJX_friedrich_hoffmann` | **Johannes Hoffmann** (1890-1967) | `needs_user_review` | Saar journalist, status-quo campaigner, and later CVP founder / first Saar Minister-President. He was alive in 1936 and is a defensible constitutional/civic identity for the Saar route. | [`source_masters/AJX/AJX_johannes_hoffmann_nationaal_archief_1955.jpg`](source_masters/AJX/AJX_johannes_hoffmann_nationaal_archief_1955.jpg) | 2223x2974 | `a4cee537f55c8054f985ec11bfecbe1c3cbc2cb222268ea8ca12b26eceff73ce` | `(850,220,2220,2065)` | [`processed_png/AJX/AJX_johannes_hoffmann_head_shoulders.png`](processed_png/AJX/AJX_johannes_hoffmann_head_shoulders.png) (`f69b9aa4a8dc55dfdc5cce6144eeb4be76cf3e6bc8cc36d922d94bf3759560fa`); [`final_dds/AJX/AJX_johannes_hoffmann.dds`](final_dds/AJX/AJX_johannes_hoffmann.dds) (`dac22811606f613ea8541efb51390a4a8530e42479d72fc0c666f16a9dd41547`) | The portrait is dated 7 Sep 1955, nineteen years after the scenario start, and shows Hoffmann at age 64-65. The person and role fit are strong, but the parent must explicitly accept the post-1936 visual-era gap before wiring. Nationaal Archief/Anefo metadata and the Commons record dedicate the image CC0; source/author/date are attributable. |
| `AJX_karl_becker` | **Willy Schmelcher** (1894-1974) | `source_ready` | Polizeipraesident of Saarbruecken from March 1935 to October 1942; exact Saar security identity with an active 1938 portrait. The role is historically Nazi SS/police and must be presented with that context, not as a neutral modern security office. | [`source_masters/AJX/AJX_willy_schmelcher_polizeipraesident_1938.jpg`](source_masters/AJX/AJX_willy_schmelcher_polizeipraesident_1938.jpg) | 539x703 | `a843a31c949b1128d857365f2e27c53e4897d7d2c62d6e2fd3b600c6823d2ad7` | `(8,0,531,703)` | [`processed_png/AJX/AJX_willy_schmelcher_head_shoulders.png`](processed_png/AJX/AJX_willy_schmelcher_head_shoulders.png) (`95d65fd51943795cf166d5c2b8be5b6675fea47b6bf1e0919c946305c9d395d1`); [`final_dds/AJX/AJX_willy_schmelcher.dds`](final_dds/AJX/AJX_willy_schmelcher.dds) (`eb55cb6333fd2d308b9bda076761dd1745714ac393c88e72a4d24f93d6c5a475`) | 1938 is close to the 1936 scenario and the face/uniform are clearly visible. Commons records the historical book portrait as public domain under the German publication basis (`PD-Germany-Section-134`); parent legal review remains appropriate for the intended distribution territory. |

The PNG crops are direct geometric crops and a Lanczos resize to the canonical
156x210 leader/commander portrait dimensions. No face reconstruction,
retouching, repainting, recolouring, background replacement, or invented
uniform detail was performed. The JPEG masters remain byte-preserved.

## Source records

### Johannes Hoffmann

- Commons file page: <https://commons.wikimedia.org/wiki/File:Stemming_Saarstatuut_Minister_President_Hoffmann,_Bestanddeelnr_907-3171.jpg>
- Direct original bitstream: <https://upload.wikimedia.org/wikipedia/commons/f/f9/Stemming_Saarstatuut_Minister_President_Hoffmann%2C_Bestanddeelnr_907-3171.jpg?download=1>
- Nationaal Archief durable record: <http://proxy.handle.net/10648/a93ab252-d0b4-102d-bcf8-003048976d84>
- Archive / collection: Nationaal Archief, Fotocollectie Anefo, archive
  component 907-3171, glass negative.
- Image date: 7 September 1955. Photographer: Joop van Bilsen for Anefo.
- Commons metadata identifies Nationaal Archief as rights holder and applies
  `CC0` / Creative Commons Zero public-domain dedication. This is a clear
  attribution and licence record for the downloaded original.
- Identity and role references: [LeMO biography](https://www.hdg.de/lemo/biografie/johannes-hoffmann),
  [Deutsche Biographie](https://www.deutsche-biographie.de/sfz33129.html),
  and [CVCE biography](https://www.cvce.eu/en/obj/johannes_hoffmann-en-706dbc0b-2041-401e-8948-7587ce1f2524.html).
  These establish the Saar political identity, his status-quo opposition to
  the 1935 Anschluss, and later CVP / Minister-President role. The image date
  is later than the scenario and is therefore explicitly review-gated.

### Willy Schmelcher

- Commons file page: <https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg>
- Direct original bitstream: <https://upload.wikimedia.org/wikipedia/commons/6/69/Willy_Schmelcher.jpg>
- Published source named by Commons: E. Kienast (ed.), *Der Grossdeutsche
  Reichstag 1938, IV. Wahlperiode*, R. v. Decker's Verlag, Berlin, 1938;
  image credit A. Gerspach, Neustadt.
- Commons metadata describes the subject as SS-Gruppenfuehrer Willy
  Schmelcher and marks the historical book portrait public domain under
  `PD-Germany-Section-134`. The source master is the direct original upload,
  not a thumbnail or a re-encoded derivative.
- Role references: the Saarbruecken police leadership record in the existing
  Event 006 research package identifies Schmelcher as Polizeipraesident in
  Saarbruecken from March 1935 through October 1942. The source date 1938 is
  inside the requested pre-war/early-war visual window.

## Candidate screening and fail-closed notes

- The earlier 1941 Brazilian Immigration Agency Hoffmann image is **not**
  reused. Its Commons page carries a URAA warning and family-estate
  provenance; the rights chain is not equivalent to this Nationaal Archief
  CC0 record.
- Max Braun remains blocked: the Saarbruecken municipal/family-archive lead
  exposes no reuse licence for a local master.
- Hermann Roechling remains blocked: the available modern monument photograph
  is an effigy, not a period portrait of the person.
- Walther Duerrfeld is a useful Saarbruecken-born engineering/industrial
  alternate, but the available US Army public-domain image is a low-resolution
  postwar IG Farben trial portrait. It was not selected or copied into this
  package; use only after a separate era/visual review.
- Anton Dunckern remains the previously documented low-resolution,
  rights-review alternate in `wallonia_saar_retry_01`; it is not duplicated
  here. No generated face or generic substitute closes that gap.

## Ownership gate

The exact/variant search covered current Chaos Redux runtime roots, installed
vanilla, Kaiserreich workshop `1521695605`, and approved workshop roots
`2265420196` and `1458561226`, using the real names, underscore variants, and
portrait tokens. Current Chaos Redux owns only the fictional consumer tokens
`AJX_friedrich_hoffmann` and `AJX_karl_becker`; no live Johannes Hoffmann or
Willy Schmelcher character/GFX owner was found in the current runtime roots.
Vanilla, `1521695605`, and `2265420196` returned no exact real-person match.

Approved mod `1458561226` contains a historical-person overlap in
`history/countries/SAR - Saarland.txt:163-164` (`Johannes Hoffmann`, picture
`Johannes_Hoffmann.dds`). Per the parent task clarification this cross-mod
historical-person reuse is **non-blocking**. No portrait art, source file, or
texture was copied from that mod; this package uses the independently sourced
Nationaal Archief/Anefo CC0 original above.

## Processing and wiring boundary

- The repository converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`
  produced both legacy uncompressed BGRA 32-bit DDS files at 156x210.
- The final DDS files are package outputs under `docs/assets/`; they are not
  runtime textures. No file under `gfx/` was created or changed.
- No `_small` texture, advisor/dossier crop, `.gfx` block, character rename,
  localisation key, or gameplay reference was edited.
- See [gfx_handoff.md](gfx_handoff.md) for deferred runtime paths and sprite
  suggestions. See [search_notes/ownership_and_candidate_log.md](search_notes/ownership_and_candidate_log.md)
  for the exact scan terms, source candidates, and unresolved review gates.

## Package files

- [contact_sheets/ajx_grounded_sources_and_crops.png](contact_sheets/ajx_grounded_sources_and_crops.png)
- [source_hashes.sha256](source_hashes.sha256)
- [gfx_handoff.md](gfx_handoff.md)

