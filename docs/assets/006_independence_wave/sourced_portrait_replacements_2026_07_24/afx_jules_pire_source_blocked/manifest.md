# IW-006 AFX Wallonia commander source package: Jules-Joseph Pire

Status: `blocked_current_vanilla_owner_and_source_rights`.

This is a bounded source-research package for the Event 006 AFX Wallonia reserve/industrial commander surface. It contains no image master, crop, processed PNG, DDS, contact sheet, GFX edit, gameplay edit, or localisation edit because the candidate is already an active vanilla character and the archive leads did not expose a rights-clear image bitstream.

## Candidate and role fit

The candidate is Lieutenant-General Jules-Joseph Pire (29 March 1878, Hannut, Belgium - 29 January 1953, Brussels). Hannut is in Wallonia, and Pire was alive and a senior Belgian officer on 1 January 1936.

Pire commanded the Corps des Chasseurs Ardennais from 26 September 1936 to 1 April 1939. He was recalled after mobilisation in September 1939 and commanded the 10th Infantry Division during the 1940 campaign. State Archives of Belgium records also identify him as a person in charge of the Belgian Legion and Armée secrète during the Second World War, with the Belgian WWII/CegeSoma article placing him at the head of the Armée secrète from March 1944.

That Walloon origin, Chasseurs Ardennais command, and senior reserve/territorial experience make Pire a strong historical fit for the AFX commander concept. This package does not claim that Pire served an independent AFX Wallonia or held the exact in-game emergency-works title.

## Requested stable consumer

| Field | Value |
|---|---|
| Character token | `AFX_walloon_reserve_commander` |
| Current in-game display name | `Marcel Delcourt` |
| Sprite | `GFX_portrait_AFX_walloon_reserve_commander` |
| Runtime texture path | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` |
| Requested historical identity | `Jules-Joseph Pire` |

The current AFX token and localisation still describe Marcel Delcourt. Changing that stable consumer to Pire would require a guarded gameplay/localisation identity transfer; this source-only package does not perform or imply that transfer.

## Source and rights review

| Candidate lead | What it establishes | Source status | Decision |
|---|---|---|---|
| [CEGESOMA Photo Catalogue FG](https://www.cegesoma.be/docs/PhotCat/PhoCatFG.htm), image 41244 | Catalogues “Général Jules Pire au milieu de l'E.M. de sa 10e D.I.” | Group photograph, not a one-person portrait; the old Pallas link does not expose an accessible original or a clear reuse licence in this run | Reject as a runtime master |
| [CEGESOMA Photo Catalogue NJ](https://www.cegesoma.be/docs/PhotCat/PhoCatNJ.htm), item 2399 | Catalogues “Jules Pire, generaal van het Belgisch leger, bevelhebber van het Geheime Leger, 1940-1945. - 2 foto's” | Archive catalog record only; the linked Pallas record/bitstream was inaccessible and no rights statement was surfaced | Hold as research lead, not an asset |
| [State Archives of Belgium, Resistance in Belgium Q7799](https://data.arch.be/wiki/Item%3AQ7799) | Official identity and Belgian resistance-network role | Authority record, not an image licence | Historical corroboration only |
| [Belgium WWII / CegeSoma, Armée secrète](https://www.belgiumwwii.be/belgique-en-guerre/articles/armee-secrete.html) | Identifies Lieutenant-General Pire as head of the Armée secrète from 1944 | Institutional historical article, not an image licence | Historical corroboration only |
| [OpenEdition, La guerre de 1940](https://books.openedition.org/septentrion/7343?lang=en) | Academic context for General Pire commanding the Chasseurs Ardennais before the war | Secondary research source, not an image licence | Role corroboration only |
| Generals.dk portrait and linked `10ID_LtGen_Pire.jpg` | Shows a recognisable Pire reference image | Reposted/copying site and linked image do not provide a defensible upstream rights-clear master | Reject; do not download or copy |

No Commons, official museum, or archive page in the reviewed results supplied a directly downloadable, attributed, rights-clear Pire portrait suitable for processing. No source bytes were downloaded, and no derivative image was made.

## Ownership gate

The installed vanilla game actively owns this exact identity. `common/characters/BEL.txt:652` defines `BEL_jules_pire`; lines 657, 660, and 661 name it and bind `GFX_portrait_BEL_jules_pire` and `GFX_portrait_BEL_jules_pire_small`; lines 664-694 define its corps-commander/advisor instances and `BEL_jules_pire` idea token. `history/countries/BEL - Belgium.txt:328` and `:372` recruit `BEL_jules_pire`, and vanilla English localisation names it “Jules Pire” at `localisation/english/ideas_l_english.yml:1407`.

The current Chaos Redux gameplay surface has no Pire token. It has the separate fictional `AFX_walloon_reserve_commander` token, its existing portrait sprite declaration, and the stale `Marcel Delcourt` localisation. The current and approved-reference ownership scans found no exact Pire owner in Chaos Redux, Kaiserreich `1521695605`, or approved references `2265420196` and `1458561226`; the vanilla owner is nevertheless dispositive.

No guarded transfer contract was supplied. The vanilla portrait must not be cloned, copied, or recommended as a replacement, and the AFX stable consumer must remain unwired for this identity.

## Deliverable ledger

| Deliverable | Result |
|---|---|
| Attributed source master | Not produced; no defensible rights-clear bitstream |
| Processed PNG preview | Not produced |
| Final DDS | Not produced |
| Contact sheet | Not produced; no comparable rights-clear candidates |
| Manifest and provenance | This file |
| Ownership evidence | `ownership_scan.md` |
| GFX/runtime handoff | `gfx_handoff.md` |
| Processing handoff | `processing_handoff.md` |

## Next decision

Keep the Pire route closed. To admit a real commander, the parent must select a different identity or provide an explicit guarded transfer contract that invalidates the vanilla owner and authorises the identity/token change. This package does not choose an alternate or use a fallback.
