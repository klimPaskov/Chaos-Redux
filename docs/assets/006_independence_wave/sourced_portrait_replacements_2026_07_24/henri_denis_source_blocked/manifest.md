# IW-006 AFX Wallonia commander source package: Henri Denis

Status: `blocked_current_owner`.

This is a grounded-source package for the Event 006 AFX Wallonia reserve/industrial commander surface. It contains one unchanged archival master and one direct pixel crop only. No ImageGen output, processed portrait, DDS, GFX edit, gameplay edit, or localisation edit was made.

## Candidate and role fit

The candidate is Henri-Jean-Charles-Eugène Denis (Henri Denis), born 10 September 1877 at Marbais, Brabant, Belgium, and deceased 19 January 1957. Marbais is in Walloon Brabant, so the identity is Wallonia-linked and the candidate was alive in 1936.

Denis was a Belgian Army lieutenant-general with logistics, transport, provincial-command, and corps-level experience, and he served as Minister of Defence from 1936 to 1940. Those documented duties make him a credible historical analogue for an emergency industrial-security or reserve-command slot in the Event 006 alternate-history package.

The role is an alternate-history territorial abstraction. This package does not claim that Denis served AFX Wallonia, led an independent Walloon state, or held the exact in-game emergency-works title.

## Source master

| Field | Value |
|---|---|
| File | `henri_denis_revue02_master.jpg` |
| Dimensions | 1740 x 2480 pixels |
| Format / mode | JPEG / 8-bit grayscale (`L`) |
| Byte count | 1,114,481 |
| SHA-256 | `69BE092EC989B5640B66D9B787310FE27141864A5E50E37FC0F8B545B07C6AE3` |
| Local path | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/henri_denis_revue02_master.jpg` |
| Source page | [Wikimedia Commons: File:Léopold III-1940-revue-02.jpg](https://commons.wikimedia.org/wiki/File:L%C3%A9opold_III-1940-revue-02.jpg) |
| Direct upload | [Original upload](https://upload.wikimedia.org/wikipedia/commons/6/61/L%C3%A9opold_III-1940-revue-02.jpg) |
| Depicted date | May 1940 |
| Publication/source | *L'Illustration*, issue 5072, 18 May 1940 |
| Author | Anonymous in the source record |
| Rights | Wikimedia Commons records the file as public domain / Public Domain Mark 1.0, with no known restrictions stated on the file page |
| Attribution note | Retain the source page, publication, anonymous-author note, and public-domain designation with any later derivative |

The master is the direct original upload, not a thumbnail, screenshot, proxy, or re-encoded derivative. It shows Leopold III at left and Henri Denis at right during the May 1940 review.

## Head-and-shoulders crop

| Field | Value |
|---|---|
| File | `henri_denis_revue02_head_shoulders_crop.png` |
| Dimensions | 780 x 1060 pixels |
| Crop rectangle | `left=960, top=260, right=1740, bottom=1320` in the 1740 x 2480 master |
| SHA-256 | `50F6D976C74012B75F7F7DA15A99A0CB36F19446FD2D968022251B64EC254E76` |
| Local path | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/henri_denis_source_blocked/henri_denis_revue02_head_shoulders_crop.png` |
| Method | Direct source-pixel crop with Pillow; no resampling, retouching, repainting, face synthesis, or colourisation |

The crop isolates the right-hand subject from cap to upper torso. The face is visible, although the cap visor shades part of the forehead and eyes. The source-visible military cap insignia is Belgian and no Nazi symbol is visible in the crop.

The source is from 1940 rather than 1936. It is identity evidence for a 1936-living person, not a claim that this exact later uniform should be used unchanged as a 1936 portrait.

## Identity and historical references

- [Académie royale de Belgique, Biographie Nationale, Henri Denis](https://www.academieroyale.be/academie/documents/FichierPDFBiographieNationaleTome2097.pdf) records Denis as a lieutenant-general and Defence Minister, born at Marbais on 10 September 1877.
- [Generals.dk, Henri Denis](https://generals.dk/general/Denis/Henri-Jean-Charles-Eug%C3%A8ne/Belgium.html) records his Belgian Army promotions and 1936-1940 Defence Ministry service.
- [Wikimedia Commons category: Henri Denis](https://commons.wikimedia.org/wiki/Category:Henri_Denis) provides the source-file context and identifies him as the Marbais-born military officer and politician.

## Ownership gate

The exact and variant searches were `Henri Denis`, `Henri-Jean-Charles-Eugène Denis`, `Henri Jean Charles Eugene Denis`, `Denis Henri`, `Henri_Denis`, and `BEL_henri_denis`.

Current Chaos Redux has no exact or variant Henri Denis character, portrait, history, interface/GFX, or English-localisation owner. Event 006's current stable AFX consumer remains `AFX_walloon_reserve_commander` with sprite `GFX_portrait_AFX_walloon_reserve_commander` and runtime texture path `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds`; this package does not alter that path.

The installed vanilla game has no exact Henri Denis owner in the searched character, history, interface/GFX, or localisation roots. Vanilla does own other considered Belgian candidates, including Jules Pire, Jean-Baptiste Piron, and Jules Bastin under its `BEL_*` identities, so those identities were not copied as substitutes.

The approved Kaiserreich reference mod `1521695605` has an active exact owner and portrait: `common/characters/BEL characters.txt:864-878` defines `BEL_henri_denis` with `GFX_portrait_BEL_henri_denis_army_small`; `history/countries/BEL - Belgium.txt:200` recruits it and line 249 marks it as a Walloon character; `interface/kaiserreich/portraits/BEL_portraits.gfx:267-268` binds the sprite to `gfx/interface/advisors/BEL/BEL_henri_denis.png`; and `localisation/english/KR_country_specific/BEL - Belgium l_english.yml:1827-1828` names and dates the identity. This live owner collision is dispositive under the portrait identity-ownership gate.

Approved reference `2265420196` has no exact Henri Denis owner in the searched roots. Approved reference `1458561226` has no Henri Denis owner; its incidental Belgian identity hits for Pire, Bastin, and Piron do not make those candidates reusable.

No guarded transfer contract was supplied. The source and crop therefore remain review evidence only, and the AFX runtime surface stays blocked rather than cloning an identity already owned by the approved reference mod.

## Parent handoff

Do not wire this package into `AFX_walloon_reserve_commander` while the Kaiserreich `BEL_henri_denis` owner exists without an explicit transfer contract that invalidates the origin owner and defines the intended cross-mod ownership boundary. If a transfer is later approved, preserve the master, crop rectangle, hashes, source attribution, and 1940-era caveat through the normal identity-preserving processing audit.

No fallback or invented substitute was used. The blocker is the active approved-reference owner collision, not a lack of historical role fit or a lack of source bytes.
