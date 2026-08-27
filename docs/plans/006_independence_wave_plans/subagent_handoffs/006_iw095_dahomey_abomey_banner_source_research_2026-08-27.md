# IW-095 Dahomey/Abomey banner source research handoff — 2026-08-27

## Scope and decision

This handoff covers only the non-portrait visual identity gate for Event 006, IW-095 Dahomey (`DAH`).

The package-wide opening-1936 Dahomey flag remains **BLOCKED**.

New research found a defensible primary historical source for a route-specific Abomey/Danhomè royal-war-banner motif, but not for a package-wide 1936 national flag.

The route-specific motif is therefore **SOURCE_EVIDENCE_FOUND / NEEDS_USER_REVIEW** pending an explicit alternate-history or traditional-institution route decision and resolution of museum-image rights.

The source supports a claim such as “a clean original flag design based on an attested Danhomè royal war-banner motif” rather than “the historical Dahomey flag in 1936.”

No gameplay, flag, GFX, localisation, runtime asset, or spreadsheet file was changed.

## Primary source: Musée du quai Branly — Jacques Chirac

**Source ID:** `MQB-207636-DAH-1856-BANNER`

**Institution:** Musée du quai Branly — Jacques Chirac, online Collections Connection.

**Object number:** `71.1930.54.910 D`.

**Collection identifier:** `ccObjectID 207636`.

**Recorded appellations:** `TENTURE` and `Drapeau`.

**Recorded culture:** `Royaume du Danhomè`.

**Recorded date:** `1856`.

**Credit line:** “Tenture offerte par le roi Ghézo à l’Empereur Napoléon III.”

**Official record:** [Musée du quai Branly object lookup](https://collections.quaibranly.fr/?action=search&field=/Record/ObjectNumber,/Record/ObjectNumber2&label=N°%20de%20gestion&value=%5b71.1930.54.910%20D%5d).

**Machine-readable record used for verification:** [quai Branly Collections Connection record](https://collections.quaibranly.fr/ccProxy.ashx/?action=get&command=search&query=and(not(isnull(CCObjectID));71.1930.54.910%20D)&fields=*&range=1-20&responseFormat=json).

The museum record describes a cotton appliqué textile with a red-and-blue border, three pairs of strips at the left end for attaching it to a pole, armed warriors carrying firearms and récades, a yellow animal described as possibly a lion, and a combat scene repeated below.

The record gives dimensions both as `230 x 353 x 0,5 cm` in the object fields and approximately `305 x 192 cm` in the descriptive text, so the dimensional discrepancy must not be silently normalized in a future manifest.

The object is strong evidence for the existence and visual language of a Danhomè royal/military banner associated with King Ghézo and the Abomey court.

It is not evidence that the same design was a state or regional national flag in French Dahomey in 1936.

## Museum photograph and rights boundary

The record exposes museum-controlled preview images named `207636.jpg`, `207636-1.jpg`, `207636-2.jpg`, and `207636-3.jpg` through the quai Branly image proxy.

Those previews were inspected only in temporary storage and were not copied into the repository, processed, or proposed as runtime assets.

The same institution’s iconothèque record `PV0080632` identifies a 1938 monochrome photograph of this type of Dahomey flag at the Musée de l’Homme, with the description “Dahomey. Drapeau en coton blanc, avec incrustations de soie [décoré de scènes de combat et de chasse (lion)].”

The 1938 photograph is useful corroboration that the object was documented in a museum context before the event’s opening date, but it does not establish a 1936 official state flag and its image rights are separate from the textile’s historical provenance.

The museum’s [online-collection conditions](https://m.quaibranly.fr/fr/recherche-scientifique/catalogues-et-publications/bibliotheque-et-fonds-documentaires/catalogues/conditions-de-mise-en-ligne-des-collections/) state that image exploitation may require permission from the rights holder, and the iconothèque guidance directs reproduction requests to `contact-icono@quaibranly.fr` or RMN-Grand Palais.

The museum [legal notices](https://www.quaibranly.fr/en/legal-notices/legal-notices/) require prior written authorization for reuse of protected website content.

The photograph record also carries a “Reproduction interdite” restriction.

Consequently, the historical object is a strong design reference, while the museum image is **not rights-cleared for direct redistribution**.

Do not ship a quai Branly photograph, trace it as a raster asset, or imply that an image proxy is a permissive source.

## Corroborating institutional and openly licensed references

The [Albany Museum of Art curator note](https://www.albanymuseum.com/applique-banner/) describes an early-twentieth-century Fon appliqué banner tradition in which royal-court guilds made custom banners and each king had a distinct animal, plant, or tool symbol.

That note associates a lion with King Glele and describes red armed figures, yellow opponents, and the Hevioso/Daghesu royal symbol.

It is useful institutional corroboration for the court-banner convention, but its image rights are not clearly stated and it is not a 1936 flag source.

The [Cleveland Museum of Art “Lion” record](https://www.clevelandart.org/art/1965.323.2) explains that Fon royal objects used visual symbols or “strong names” connected to particular Abomey kings and associates the lion with King Glele.

That artwork is dated to the 1940s and explicitly marked as known to be under copyright, so it is corroboration only and must not be reused as a runtime image.

The [Commons record for King Adandozan’s banner of war](https://commons.wikimedia.org/wiki/File:King_Adandozan_banner_of_war.jpg) documents an authentic royal banner sent as a gift in 1811 and identifies the image as `CC BY-SA 4.0` with Commons VRT permission ticket `2021020410008441`.

The downloaded inspection copy had SHA-256 `E4AF11CB1D9621B67041D3CE4D3D74CF41460D77387FBE9872DFEAD55BE610E2`.

This openly licensed image can serve as a separately attributed visual reference if needed, subject to CC BY-SA 4.0 attribution and share-alike obligations, but its c.1800/1811 date makes it corroboration of royal-war-banner practice rather than a 1936 baseline.

The modern [Béhanzin banner reconstruction](https://commons.wikimedia.org/wiki/File:Royal_banner_of_B%C3%A9hanzin_of_Dahomey.svg) remains a reconstruction based on a secondary heraldic site and is not promoted to primary evidence by this handoff.

## Date and role fit

| Candidate use | Fit | Reason |
| --- | --- | --- |
| Opening-1936 package-wide `DAH` national flag | **Blocked** | No independently documented 1936 Dahomey state/regional flag has been established, and the 1856 royal banner is not a national flag. |
| Route-specific Abomey/Danhomè royal or traditional-institution flag | **Needs user review** | The museum object is an attested Danhomè royal banner with explicit provenance, pole attachments, date, and court context. |
| Generic modern Benin/Dahomey flag | **Rejected** | Modern or post-colonial designs do not prove an opening-1936 identity and would collapse the event’s historical distinction. |
| French tricolour as the `DAH` identity | **Rejected** | It represents the colonial sovereign rather than a distinct Dahomey/Abomey route identity and does not satisfy the requested non-portrait identity gate. |
| Direct museum photograph as runtime asset | **Blocked pending permission** | The museum controls the image presentation and requires rights clearance for reproduction. |

The existing `006_iw095_symbol_source_gate_2026-08-26.md` remains the source of truth for the earlier package-wide baseline block and for the installed vanilla DAH family’s post-1936 dating concerns.

The first-footprint addendum’s requirement for a historically grounded Abomey royal-institution connection is satisfied at the motif-reference level, not at the level of a proven opening-1936 national flag.

## Proposed manifest-style record

| Field | Proposed value |
| --- | --- |
| Asset ID | `IW-095-DAH-ABOMEY-ROYAL-BANNER-MOTIF` |
| Family | ASSET-044 route-specific normal/medium/small flag ladder |
| Status | `needs_user_review` |
| Source mode | `historically_grounded_route_symbol_reference` |
| Primary source | Musée du quai Branly object `71.1930.54.910 D`, `ccObjectID 207636` |
| Date/role | 1856; Danhomè royal/military banner offered by King Ghézo; route motif only |
| Provenance | Museum object record, culture field `Royaume du Danhomè`, named royal gift provenance, pole-attachment description |
| Rights | Historical object reference is strong; museum image rights are not cleared; written permission or an original reconstruction is required |
| Source file in repository | None; no museum photograph or reconstruction was installed during research-only work |
| Processed PNG/TGA | None |
| Final DDS | None; flags follow the event-assets flag workflow and require parent acceptance before production |
| Proposed route tag | `DAH_abomey_royal` or another parent-approved route-specific cosmetic tag; do not use bare `DAH` |
| Proposed runtime family | `flag_DAH_abomey_royal` with normal/medium/small variants, subject to parent naming approval |
| Consumer | Route-specific IW-095 Abomey/Danhomè royal or traditional-institution identity |
| Uncertainty | Complex appliqué scenes must be simplified into a clean flat flag without inventing an unattested crest; object dimensions conflict in the museum record; image rights remain unresolved; route semantics are not yet accepted |

The package-wide baseline row remains `IW-095-DAH-FLAG-FAMILY`, status `blocked`, with no source PNG, processed variant, final variant, or runtime basename cleared by this research.

## Exact next asset steps if the route is accepted

1. The parent must explicitly accept a route-specific Abomey/Danhomè royal identity and record the chosen cosmetic tag and runtime basename; the base `DAH` flag must remain untouched.

2. If direct visual fidelity to the museum photograph is required, request written reproduction permission from quai Branly/RMN-Grand Palais before any image is archived or redistributed.

3. If the parent accepts an original reconstruction, the asset worker should use the object record’s documented red-and-blue border, pole-side attachment treatment, and historically described animal/royal-war-banner motif as a strict design reference, while creating a new flat orthographic flag rather than copying the museum photograph.

4. The reconstruction must not use fabric folds, museum-photo perspective, painted battle scenes, readable text, modern Benin/Dahomey colour assumptions, or an invented generic sacred symbol.

5. Any simplification from the multi-figure appliqué into a small route emblem must be listed in the eventual manifest as an interpretive reduction of the 1856 Ghézo banner, not presented as an independently attested 1936 flag.

6. After acceptance, render the normal, medium, and small variants at 82×52, 41×26, and 10×7 using the repository’s flat-flag workflow, retain the generated source and processed outputs, and record hashes, source citation, rights status, date/role fit, and uncertainty.

7. The parent retains ownership of `.gfx`, cosmetic-tag, event, and country wiring, and should add that wiring only after the asset package has a stable basename and reviewable outputs.

8. If the route is not accepted or rights cannot be handled under the original-reconstruction path, keep the route motif in `needs_user_review` and keep the package-wide ASSET-044 baseline blocked.

## Safe disposition

No runtime visual asset is cleared by this handoff.

The quai Branly object record is a defensible historical source for an Abomey/Danhomè royal-banner motif, but the underlying image files are not cleared for direct reuse.

The safe continuation is either a parent-approved, route-specific original flat reconstruction with complete provenance and explicit alternate-history/traditional-route labelling, or continued blocking of the entire IW-095 flag family.

