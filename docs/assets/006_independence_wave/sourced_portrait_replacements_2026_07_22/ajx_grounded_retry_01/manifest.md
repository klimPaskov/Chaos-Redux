# Event 006 AJX grounded portrait source retry

Date: 2026-07-22

Scope: source-only research and review package for the two fictional grounded
Saar identities currently consumed by Event 006 Independence Wave:

- `AJX_friedrich_hoffmann` - civic / constitutional leader surface
- `AJX_karl_becker` - corps-commander surface (the currently named Karl
  Becker is fictional in the runtime file)

This package contains two unchanged archival JPEG source masters for research,
explicit head-and-shoulders PNG crops, repository-standard 156x210 DDS outputs,
a contact sheet, and source/ownership documentation. The Schmelcher outputs are
retained as role-mismatched research evidence only; they are not approval for
the live corps-commander surface. No character, localisation, GFX, interface,
history, event, runtime `gfx/`, advisor icon, or `_small` texture was edited.
The parent implementation agent owns identity transfer, final sprite wiring,
and any runtime copy.

## Status vocabulary

- `source_ready`: the unchanged source bitstream is present, attribution and
  rights basis are recorded, identity and requested role fit are defensible,
  and the source-ready crop plus DDS are available. This is not runtime
  approval; the parent still owns contextual review and wiring. No current
  commander candidate in this retry has this status.
- `needs_user_review`: a usable source package is present, but a named date,
  era, rights, role, or visual-context issue remains unresolved. Do not wire
  without an explicit review decision.
- `role_mismatch_research_only`: a rights-documented source package is retained
  for research, but the identity does not match the requested live role. It
  must not be wired to that role.
- `rejected_vanilla_owner`: a historically plausible candidate is rejected
  because vanilla or another installed project owns the live historical
  character token. No local source master is acquired for runtime use.
- `blocked`: no defensible source was acquired, or the only lead failed a
  required identity, rights, quality, or role gate. No substitute portrait is
  authorised.

## Role ledger

| Current fictional consumer | Grounded candidate | Status | Historical / role fit | Source master | Source dimensions | Source SHA-256 | Crop coordinates (x1,y1,x2,y2) | PNG / DDS | Era and rights uncertainty |
|---|---|---|---|---|---:|---|---|---|---|
| `AJX_friedrich_hoffmann` | **Johannes Hoffmann** (1890-1967) | `needs_user_review` | Saar journalist, status-quo campaigner, and later CVP founder / first Saar Minister-President. Alive in 1936 and a defensible constitutional/civic identity for the Saar route. | [`source_masters/AJX/AJX_johannes_hoffmann_nationaal_archief_1955.jpg`](source_masters/AJX/AJX_johannes_hoffmann_nationaal_archief_1955.jpg) | 2223x2974 | `a4cee537f55c8054f985ec11bfecbe1c3cbc2cb222268ea8ca12b26eceff73ce` | `(850,220,2220,2065)` | [`processed_png/AJX/AJX_johannes_hoffmann_head_shoulders.png`](processed_png/AJX/AJX_johannes_hoffmann_head_shoulders.png) (`f69b9aa4a8dc55dfdc5cce6144eeb4be76cf3e6bc8cc36d922d94bf3759560fa`); [`final_dds/AJX/AJX_johannes_hoffmann.dds`](final_dds/AJX/AJX_johannes_hoffmann.dds) (`dac22811606f613ea8541efb51390a4a8530e42479d72fc0c666f16a9dd41547`) | Portrait dated 7 Sep 1955, nineteen years after the scenario start, showing Hoffmann at age 64-65. Person and civic role fit are strong, but the parent must explicitly accept the post-1936 visual-era gap before wiring. Nationaal Archief/Anefo metadata and Commons record dedicate the image CC0. |
| `AJX_friedrich_hoffmann` | **Johannes Hoffmann**, pre-1940 archival lead | `blocked` | The Saar-Nostalgie page labels a 1935 image and credits Landesarchiv Saarbruecken; it is a better era fit but only 360x271 and the page gives no reuse licence. | Not acquired; review lead only | 360x271 (remote lead) | - | - | No PNG or DDS produced. | Rights chain and archive permission are unresolved, and the low resolution is weak for a 156x210 face portrait. Do not process or wire without explicit rights/quality approval. |
| `AJX_karl_becker` | **Willy Schmelcher** (1894-1974) | `role_mismatch_research_only` | Saarbruecken Polizeipraesident from March 1935 to October 1942; this is a police/SS security identity, not an army corps commander. The source may not be presented as a neutral or military corps role. | [`source_masters/AJX/AJX_willy_schmelcher_polizeipraesident_1938.jpg`](source_masters/AJX/AJX_willy_schmelcher_polizeipraesident_1938.jpg) | 539x703 | `a843a31c949b1128d857365f2e27c53e4897d7d2c62d6e2fd3b600c6823d2ad7` | `(8,0,531,703)` | [`processed_png/AJX/AJX_willy_schmelcher_head_shoulders.png`](processed_png/AJX/AJX_willy_schmelcher_head_shoulders.png) (`95d65fd51943795cf166d5c2b8be5b6675fea47b6bf1e0919c946305c9d395d1`); [`final_dds/AJX/AJX_willy_schmelcher.dds`](final_dds/AJX/AJX_willy_schmelcher.dds) (`eb55cb6333fd2d308b9bda076761dd1745714ac393c88e72a4d24f93d6c5a475`) | 1938 is close to the scenario and the face/uniform are clear. Commons records the book portrait as public domain under `PD-Germany-Section-134`; retained only as attributed research evidence because the live role is wrong. |
| `AJX_karl_becker` | **Karl Becker** (1879-1940) | `rejected_vanilla_owner` | General der Artillerie, Chief Heereswaffenamt / Army Armaments Office, born Speyer. Technical/administrative artillery general rather than a field corps commander; exact historical identity is already a live vanilla character (`GER_karl_heinrich_emil_becker`). | Not acquired; research links only | - | - | - | No PNG or DDS produced. | A 1937 Bundesarchiv CC BY-SA 3.0 DE portrait and an April 1940 NAC public-domain portrait are face-visible and rights-documented, but the vanilla owner gate and weak corps-command role fit reject them for AJX. |
| `AJX_karl_becker` | **Wilhelm Fahrmbacher** (1888-1970) | `blocked` | Born Zweibruecken in the Rhenish Palatinate; General der Artillerie and later commander of VII Army Corps. Strong regional and role lead, but no pre-war or early-war face-visible portrait with a defensible reuse licence was found. | Not acquired; research links only | - | - | - | No PNG or DDS produced. | Commons exposes only group, surrender, and grave photographs; portrait leads at Generals.dk and WW2Gravestone have unclear or controlled rights. Do not crop a group image or invent a likeness. |

The retained PNG crops are direct geometric crops and a Lanczos resize to the
canonical 156x210 leader/commander portrait dimensions. No face reconstruction,
retouching, repainting, recolouring, background replacement, or invented
uniform detail was performed. The JPEG masters remain byte-preserved. A
processed crop is not the same as approval for the requested runtime role.

## Source records

### Johannes Hoffmann - retained 1955 review source

- Commons file page: <https://commons.wikimedia.org/wiki/File:Stemming_Saarstatuut_Minister_President_Hoffmann,_Bestanddeelnr_907-3171.jpg>
- Direct original bitstream: <https://upload.wikimedia.org/wikipedia/commons/f/f9/Stemming_Saarstatuut_Minister_President_Hoffmann%2C_Bestanddeelnr_907-3171.jpg?download=1>
- Nationaal Archief durable record: <http://proxy.handle.net/10648/a93ab252-d0b4-102d-bcf8-003048976d84>
- Archive / collection: Nationaal Archief, Fotocollectie Anefo, archive
  component 907-3171, glass negative.
- Image date: 7 September 1955. Photographer: Joop van Bilsen for Anefo.
- Commons metadata identifies Nationaal Archief as rights holder and applies
  CC0 / Creative Commons Zero public-domain dedication. This is a clear
  attribution and licence record for the downloaded original.
- Identity and role references: [LeMO biography](https://www.hdg.de/lemo/biografie/johannes-hoffmann),
  [Deutsche Biographie](https://www.deutsche-biographie.de/sfz33129.html),
  and [CVCE biography](https://www.cvce.eu/en/obj/johannes_hoffmann-en-706dbc0b-2041-401e-8948-7587ce1f2524.html).
  These establish the Saar political identity, his status-quo opposition to
  the 1935 Anschluss, and later CVP / Minister-President role. The image date
  is later than the scenario and is therefore explicitly review-gated.

### Johannes Hoffmann - pre-1940 lead, not acquired

- Page: <https://www.saar-nostalgie.de/Joho1.htm>
- Remote image path: `Bilder/Joho/vor1945/JoHo1935bk.jpg` (360x271).
- Page caption: `Johannes Hoffmann etwa 1935` and credit `Foto: L.A.
  Saarbruecken`.
- The page does not state a reuse licence or permission to redistribute the
  scan. The resolution is also too weak to call source-ready without review.
  No image was copied into this package and no crop or DDS was produced.

### Willy Schmelcher - retained role-mismatch research source

- Commons file page: <https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg>
- Direct original bitstream: <https://upload.wikimedia.org/wikipedia/commons/6/69/Willy_Schmelcher.jpg>
- Published source named by Commons: E. Kienast (ed.), *Der Grossdeutsche
  Reichstag 1938, IV. Wahlperiode*, R. v. Decker's Verlag, Berlin, 1938;
  image credit A. Gerspach, Neustadt.
- Commons metadata describes the subject as SS-Gruppenfuehrer Willy
  Schmelcher and marks the historical book portrait public domain under
  `PD-Germany-Section-134`. The source master is the direct original upload,
  not a thumbnail or a re-encoded derivative.
- Role references identify Schmelcher as Polizeipraesident in Saarbruecken
  from March 1935 through October 1942. The source date is inside the
  pre-war/early-war visual window, but this police/SS role does not satisfy
  the live army corps-commander role.

### Karl Becker - blocked by owner and role gates

- [Commons, Bundesarchiv Bild 183-H27401](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-H27401,_Karl_Becker.jpg): March 1937, face-visible portrait, German Federal Archives, CC BY-SA 3.0 DE; direct original <https://upload.wikimedia.org/wikipedia/commons/e/e6/Bundesarchiv_Bild_183-H27401%2C_Karl_Becker.jpg>.
- [Commons, General Karl Becker](https://commons.wikimedia.org/wiki/File:General_Karl_Becker.jpg): April 1940, National Digital Archive Poland, public-domain basis; direct original <https://upload.wikimedia.org/wikipedia/commons/0/0f/General_Karl_Becker.jpg>.
- [Deutsche Biographie](https://www.deutsche-biographie.de/sfz2563.html?language=en)
  records Karl Becker (born 14 Dec 1879 in Speyer, died 8 Apr 1940 in Berlin)
  as General der Artillerie, President of the Research Council, and Chief of
  the Heereswaffenamt. His documented career is technical/administrative and
  does not establish a corps-command match.
- The vanilla scan found `history/countries/GER - Germany.txt:1047` recruiting
  `GER_karl_heinrich_emil_becker` as an artillery scientist, with matching
  localisation in vanilla. Kaiserreich workshop `1521695605` also contains
  the historical owner token. No source master was copied because the owner
  gate is binding.

### Wilhelm Fahrmbacher - blocked source lead

- [Generals.dk career page](https://www.generals.dk/general/Fahrmbacher/Wilhelm_Karl/Germany.html)
  records Wilhelm Fahrmbacher, born 19 Sep 1888 in Zweibruecken, General der
  Artillerie, commander of 5th Infantry Division from August 1938 and VII Army
  Corps from October 1940.
- [Deutsche Digitale Bibliothek record](https://www.deutsche-digitale-bibliothek.de/person/gnd/105520829)
  confirms the Zweibruecken origin and general officer identity.
- [Commons category](https://commons.wikimedia.org/wiki/Category:Wilhelm_Fahrmbacher)
  exposes group/surrender/grave photographs, not a rights-clear face-visible
  pre-war portrait. Other portrait leads at Generals.dk and
  WW2Gravestone are not accompanied by a defensible reuse licence. No image
  was acquired or cropped.

## Candidate screening and fail-closed notes

- The earlier 1941 Brazilian Immigration Agency Hoffmann image is **not**
  reused. Its Commons page carries a URAA warning and family-estate
  provenance; the rights chain is not equivalent to this Nationaal Archief
  CC0 record.
- Max Braun remains blocked: [Saarbruecken municipal history](https://www.saarbruecken.de/kultur/stadtarchiv/schaufenster_stadtgeschichte/menschen/liste_der_stadtoberhaeupter/max_braun)
  and [LVR biography](https://www.rheinische-geschichte.lvr.de/Projekte/Widerstandskarte/max-braun-fuehrte-den-saarwiderstand-von-frankreich-und-england-aus-fort/DE-2086/lido/dc00019105)
  establish the Saar civic/labour identity, but the available municipal page
  credits family archives and states no reuse licence. No local master was
  copied.
- Hermann Roechling remains blocked: the available modern monument photograph
  is an effigy, not a period portrait of the person. A 1932 printed scan lead
  has unresolved rights and is not source-ready.
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
`2265420196` and `1458561226`, using real names, underscore variants, and
portrait tokens. Current Chaos Redux owns only the fictional consumers
`AJX_friedrich_hoffmann` and `AJX_karl_becker`; no live Johannes Hoffmann or
Willy Schmelcher historical owner was found in the current runtime roots.

Vanilla has the active Karl Becker owner: `history/countries/GER - Germany.txt`
recruits `GER_karl_heinrich_emil_becker`, and vanilla localisation defines the
same historical identity. Kaiserreich `1521695605` also contains the owner
token. This is a binding external-owner rejection, not a reason to clone or
rename the vanilla character into AJX.

Approved mod `1458561226` contains a historical-person overlap in
`history/countries/SAR - Saarland.txt:163-164` (`Johannes Hoffmann`, picture
`Johannes_Hoffmann.dds`). Per the parent task clarification this cross-mod
historical-person reuse is **non-blocking**. No portrait art, source file, or
texture was copied from that mod; this package uses the independent
Nationaal Archief/Anefo CC0 original above.

## Processing and wiring boundary

- The repository converter `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`
  produced the retained 156x210 legacy uncompressed BGRA 32-bit DDS files.
- The final DDS files are package outputs under `docs/assets/`; they are not
  runtime textures. No file under `gfx/` was created or changed.
- No `_small` texture, advisor/dossier crop, `.gfx` block, character rename,
  localisation key, history file, or gameplay reference was edited.
- The Schmelcher PNG/DDS paths are documented for research provenance only;
  they are not a suggested commander handoff.
- See [gfx_handoff.md](gfx_handoff.md) for deferred runtime paths and the
  explicit no-commander-approval boundary. See
  [search_notes/ownership_and_candidate_log.md](search_notes/ownership_and_candidate_log.md)
  for the exact scan terms, source candidates, and unresolved review gates.

## Package files

- [contact_sheets/ajx_grounded_sources_and_crops.png](contact_sheets/ajx_grounded_sources_and_crops.png)
- [source_hashes.sha256](source_hashes.sha256)
- [gfx_handoff.md](gfx_handoff.md)

