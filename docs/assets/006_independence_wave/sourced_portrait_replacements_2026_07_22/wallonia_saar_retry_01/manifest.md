# Event 006 Wallonia/Saar sourced portrait replacement retry

Source-only manifest for the 2026-07-22 retry of the four unresolved grounded
roles in Event 006 Independence Wave:

- IW-006 / AFX Wallonia civic leader
- IW-006 / AFX Wallonia reserve or industrial commander
- IW-010 / AJX Saar civic or municipal leader
- IW-010 / AJX Saar industrial or security commander

This package contains only unchanged archival JPEG masters and a comparison
sheet. No source was cropped, resized, retouched, re-encoded, converted to
PNG/DDS, or wired into gameplay. The normal portrait-processing agent owns
identity-preserving crops, final PNG previews, DDS conversion, and runtime
handoff after the parent approves a `source_ready` row.

## Status vocabulary

- `source_ready`: the exact downloaded original is present locally, the
  dimensions/bytes/SHA-256 are recorded, the subject and requested role fit are
  defensible, and a source/rights basis is documented.
- `needs_user_review`: a face-visible source or defensible source lead exists,
  but rights, historical role, date, image quality, or political-context review
  is still required before processing.
- `blocked`: no defensible source was acquired for the requested role, or the
  best lead has an unresolved rights/identity/role problem. No generated or
  generic substitute is permitted.
- `rejected_current_project_owner`: an otherwise plausible person is already
  the live owner of a current Chaos Redux character/GFX/localisation key and
  there is no guarded transfer contract in this retry.

## Role resolution

| Requested role | Disposition | Decision evidence |
|---|---|---|
| AFX Wallonia civic leader | `blocked` | Jules Destrée is the existing live owner of `AFX_walloon_provisional_assembly`; no transfer contract was supplied. Georges Truffaut is an excellent 1936 Walloon civic fit, but the Institut Destrée page labels the image `Droits SOFAM`, which conflicts with the Commons CC BY-SA claim. No independent rights proof was found. François Bovesse has no face-visible free portrait source. |
| AFX Wallonia reserve/industrial commander | `blocked` | Jules Bastin is an exact Walloon/Belgian Army fit for 1936, and Jules-Joseph Pire is a strong Walloon Chasseurs Ardennais fit, but the available photographs expose no defensible reuse licence/original. No commander master is retained. |
| AJX Saar civic/municipal leader | `needs_user_review` | Johannes Hoffmann is the strongest civic identity, but his 1941 Brazilian Immigration Agency image has a Brazilian-PD/URAA warning and family-estate provenance. Josef Bürckel has a public-domain archival lead and Saar commissioner role, but is an authoritarian political administrator rather than a municipal leader and no unchanged local master was acquired in this retry. |
| AJX Saar industrial/security commander | `source_ready` primary; `needs_user_review` alternate | Willy Schmelcher was Polizeipräsident of Saarbrücken from 1935 and is represented by a 1938 archival book portrait with Commons public-domain metadata. Anton Dunckern was Gestapo chief in Saarbrücken from 1935 and has a face-visible circa-1937 master, but the 315x405 source is low resolution and its public-domain basis needs territorial review. |

## Acquired source masters

| Requested role | Status / subject | Source page and direct original | Archive, date, author, rights basis | Local master and file evidence | Fit and uncertainty |
|---|---|---|---|---|---|
| AJX industrial/security commander | `source_ready` - **Willy Schmelcher** | [Commons file page](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg); [unchanged direct original](https://upload.wikimedia.org/wikipedia/commons/6/69/Willy_Schmelcher.jpg) | E. Kienast (ed.), *Der Großdeutsche Reichstag 1938, IV. Wahlperiode*, R. v. Decker's Verlag, Berlin, 1938; image credit A. Gerspach, Neustadt. Commons metadata places the file in `PD-Germany-§134` and marks it Public domain. This is a Commons rights assertion based on the historical publication and unknown photographer status; parent legal review should still confirm the intended distribution territory. | [`source_masters/AJX/AJX_willy_schmelcher_commander_1938.jpg`](source_masters/AJX/AJX_willy_schmelcher_commander_1938.jpg); JPEG, 539x703, 70,984 bytes; SHA-256 `a843a31c949b1128d857365f2e27c53e4897d7d2c62d6e2fd3b600c6823d2ad7` | Exact Saarbrücken police/security identity: Schmelcher was Polizeipräsident in Saarbrücken from March 1935 to October 1942. Face and uniform are clearly visible. Nazi SS/police history is a required context note. |
| AJX industrial/security commander alternate | `needs_user_review` - **Anton Dunckern** | [Commons file page](https://commons.wikimedia.org/wiki/File:Anton_Dunckern.jpg); [unchanged direct original](https://upload.wikimedia.org/wikipedia/commons/8/81/Anton_Dunckern.jpg) | Personal File in the Berlin Document Centre; circa 1937; author unknown. Commons marks Public domain / Public Domain Mark under a life-plus-70 or shorter-term rationale and explicitly warns that a US public-domain tag should also be established. The local package records the Commons claim but does not silently treat the warning as resolved. | [`source_masters/AJX/AJX_anton_dunckern_security_commander_c1937.jpg`](source_masters/AJX/AJX_anton_dunckern_security_commander_c1937.jpg); JPEG, 315x405, 89,211 bytes; SHA-256 `109e048050666b1f7029eb32c26e4692aba3a1ee6b484c2eb3c36bd3658f9bd0` | Exact Saar security identity: Dunckern became Gestapo chief in Saarbrücken after the 1935 reintegration. Face and uniform are visible, but the small, grainy master may not survive the target 156x210 portrait treatment cleanly. SS/Gestapo history and territorial rights need explicit review. |

Both files above are byte-preserved downloads of the direct Wikimedia upload
URLs. `contact_sheets/ajx_commander_source_candidates.png` is a review-only
comparison sheet and is not a runtime texture.

## Candidate leads without an acquired master

### AFX Wallonia civic leader

- **Jules Destrée (1863-1936)** is an exact Walloon Movement/civic fit and has
  a period press portrait in the earlier Northwestern Europe source package.
  The current project already owns this identity as
  `AFX_walloon_provisional_assembly`: localisation key, character recruitment,
  and GFX are live in the AFX history/localisation/interface files. This retry
  therefore records `rejected_current_project_owner` and does not copy or clone
  the existing master. A guarded transfer contract from the parent would be
  required before reuse.
- **Georges Truffaut (1901-1942)** was a Liège/Walloon activist, Ligue d'Action
  wallonne leader, Liège councilman (1932), deputy (1934), and alderman for
  public works from 1935, making him an excellent 1936 civic/industrial fit.
  The [Institut Jules Destrée biography](http://www.wallonie-en-ligne.net/1995_Cent_Wallons/Truffaut_Georges.htm)
  identifies the image as `Photo Institut Jules-Destrée (Droits SOFAM)`. A
  corresponding [Commons file](https://commons.wikimedia.org/wiki/File:TRUFFAUT_Georges.gif)
  claims CC BY-SA 4.0 and points to the same source, but this conflicts with
  the SOFAM rights notice. Status: `needs_user_review` / not source-ready;
  no file was downloaded.
- **François Bovesse (1890-1944)** is a credible Namur/Walloon political fit,
  but the [Commons category](https://commons.wikimedia.org/wiki/Category:Fran%C3%A7ois_Bovesse)
  exposes monuments and graves rather than a defensible face-visible portrait.
  Status: `blocked_no_face_source`.

### AFX Wallonia reserve or industrial commander

- **Jules Bastin (1889-1944)** was born in Roux/Charleroi and in 1936 was
  sous-chef d'état-major of the Cavalry Corps and a tactics professor at the
  École de guerre. The [Free Belgians biography](https://www.freebelgians.be/articles/print.php?id=29)
  exposes `image34.jpg`, but no reuse licence or archive release is stated;
  other portrait leads similarly lack a clear free original. Status:
  `needs_rights_review`; no file was retained.
- **Jules-Joseph Pire (1878-1953)** was a Walloon-born Belgian lieutenant
  general who commanded the Chasseurs Ardennais in the requested period. The
  [biographical lead](https://fr.wikipedia.org/wiki/Jules_Pire) and prior
  catalogue references do not provide a rights-defensible original portrait.
  Status: `blocked_no_defensible_source`.

### AJX Saar civic or municipal leader

- **Johannes Hoffmann (1890-1967)** is the best identity/role fit (Saar
  editor, status-quo politician, and Saar civic leader before the 1935 vote).
  The [1941 Commons image](https://commons.wikimedia.org/wiki/File:WP_Johannes_Hoffmann_1941.jpg)
  is anonymous Brazilian Immigration Agency material, but Commons carries an
  explicit URAA warning and [Saar-Nostalgie](https://www.saar-nostalgie.de/Joho1.htm)
  identifies the Hoffmann family estate. Status: `needs_user_review` / blocked
  pending a rights decision; no new copy was made.
- **Josef Bürckel (1895-1944)** was Reichskommissar/Gauleiter for the Saar from
  1935 and has a [Commons source page](https://commons.wikimedia.org/wiki/File:Josef_B%C3%BCrckel.jpg)
  with an original [NAC signature 1-E-10242 image](https://upload.wikimedia.org/wikipedia/commons/d/d3/Josef_B%C3%BCrckel.jpg)
  dated 1937-39 and marked public domain via the Polish National Digital
  Archive. He is an administrative/political commissioner, not a neutral
  municipal leader; the source host also throttled this retry's download.
  Status: `needs_user_review_role_fit`; no local master is supplied.

## Processing and wiring boundary

- No processed PNG preview, portrait crop, DDS, `_small` texture, `.gfx` edit,
  character edit, localisation edit, or runtime path was created here.
- The parent may send only the Schmelcher `source_ready` master through the
  approved identity-preserving portrait pipeline after its historical-context
  and rights review. Dunckern remains an alternate review item, not an automatic
  replacement.
- The AFX civic and commander surfaces remain blocked. The AJX civic surface
  remains review-gated. Do not use generated faces, generic stand-ins, proxies,
  postwar substitutes, or a re-encoded derivative to close these gaps.
- Suggested final consumers (to be confirmed by the parent after processing):
  `gfx/leaders/006_independence_wave/portrait_AJX_<approved_subject>.dds` and
  its normal portrait sprite definition. This package intentionally does not
  choose the final subject key or edit the `.gfx` file.
