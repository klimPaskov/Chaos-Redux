# AJX grounded portrait ownership and candidate log

Date: 2026-07-22

Scope: exact/variant real-person ownership evidence and bounded source search
for the two Event 006 Saar grounded identities. This log does not edit or
claim ownership of any runtime character, GFX, or localisation key.

## Ownership search evidence

The targeted scan covered these roots and file surfaces:

- current Chaos Redux `common/`, `history/`, `gfx/`, `interface/`,
  `localisation/`, and `events/` roots;
- vanilla Hearts of Iron IV installation
  `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`;
- Kaiserreich workshop root `394360/1521695605`;
- approved workshop roots `394360/2265420196` and `394360/1458561226`.

Terms included the real names, spacing and underscore variants, and the
current fictional portrait tokens:

```text
Johannes Hoffmann
Johannes_Hoffmann
johannes_hoffmann
Willy Schmelcher
Willy_Schmelcher
willy_schmelcher
AJX_friedrich_hoffmann
AJX_karl_becker
```

### Current Chaos Redux

No exact `Johannes Hoffmann` or `Willy Schmelcher` real-person owner was found
in the current runtime roots. The current package owns the fictional consumers
and their role-key sprites:

- `common/characters/006_independence_wave_saar_characters.txt`:
  `AJX_friedrich_hoffmann`, `AJX_karl_becker`;
- `interface/006_independence_wave_region_01_portraits.gfx`:
  `GFX_portrait_AJX_friedrich_hoffmann`,
  `GFX_portrait_AJX_karl_becker`;
- `history/countries/AJX - Saar.txt` recruits both fictional IDs.

Those current fictional IDs are the parent implementation surface, not a
reason to clone a second real-person ID. The parent owns any guarded transfer.

### Vanilla and approved workshop roots

Vanilla, Kaiserreich `1521695605`, and approved `2265420196` returned no exact
real-person match for either candidate. Approved mod `1458561226` contains an
intentional historical-person overlap:

```text
history/countries/SAR - Saarland.txt:163  name = "Johannes Hoffmann"
history/countries/SAR - Saarland.txt:164  picture = "Johannes_Hoffmann.dds"
```

Per the parent task clarification, this cross-mod use of the historical person
does **not** block the new Chaos Redux source package. No art, DDS, or source
file was copied from `1458561226`; the package uses the independent
Nationaal Archief/Anefo CC0 original. The approved-mod ownership is recorded so
the parent can avoid accidental asset/source cloning and can choose a distinct
Chaos Redux sprite token if desired.

## Candidate ledger

| Candidate | Role considered | Source lead | Result | Disposition |
|---|---|---|---|---|
| Johannes Hoffmann (1890-1967) | Saar civic / constitutional / labour-adjacent leader | Nationaal Archief/Anefo glass negative, 7 Sep 1955, Joop van Bilsen; Commons CC0; direct original retained in this package | Strong Saar identity and alive in 1936. The known post-1936 photograph is clear and face-visible but visibly older than the scenario. | `needs_user_review` with complete source-ready package |
| Willy Schmelcher (1894-1974) | Saar police / industrial-security commander | 1938 *Der Grossdeutsche Reichstag* portrait, A. Gerspach; Commons public-domain record | Exact Saarbruecken Polizeipraesident role from 1935-1942 and period close to 1936. SS/police historical context must remain explicit. | `source_ready` |
| Walther Duerrfeld (1899-1967) | Saar / Rhenish engineering and industrial commander alternate | US Army/OUSCCPAC/OCCWC public-domain trial portrait via Wollheim Memorial, circa 1945-49 | Born in Saarbruecken and active in Saar ironworks / IG Farben before 1936, but available image is a low-resolution postwar trial portrait. | `needs_user_review`; no local master copied |
| Max Braun (1892-1945) | Saar labour / civic leader | Saarbruecken municipal/family archive page | Strong labour identity, but the face source is private-family archive material with no defensible reuse licence. | `blocked_rights`; no local master |
| Hermann Roechling (1872-1955) | Saar industrial / civic authority | Commons modern photograph of a monument/effigy | The available image is a 2018 monument, not a period portrait of Roechling. A 1932 printed scan lead has unresolved US rights and is not source-ready. | `blocked_source_or_rights`; no local master |
| Josef Buerckel (1895-1944) | Saar administrative/political commissioner | Polish National Digital Archive public-domain image lead | Source rights are stronger, but his Gauleiter/Reichskommissar role is authoritarian political administration rather than the requested civic/municipal constitutional identity. | `blocked_role_fit`; no local master |
| Anton Dunckern (1906-1985) | Saar security commander alternate | Existing `wallonia_saar_retry_01` package, Berlin Document Centre c.1937 image | Exact Saar Gestapo role, but low-resolution source and territorial rights warning remain unresolved. | `needs_user_review` in prior package; not duplicated |

## Source-quality decisions

- The previously investigated 1941 Brazilian Immigration Agency Hoffmann
  image was intentionally not copied: the Commons page carries an explicit
  URAA warning and family-estate provenance. The CC0 Nationaal Archief record
  is a separate source chain.
- No portrait was generated, reconstructed, face-swapped, recoloured, or
  borrowed from an external mod. The two retained source masters are direct
  Wikimedia upload bitstreams and their hashes are recorded in the manifest.
- The Hoffmann crop excludes the adjacent attendee/hat and keeps Hoffmann's
  face, tie, jacket, and shoulders. The Schmelcher crop trims only the outer
  scan margin. Coordinates are recorded in `manifest.md`.

## Research links

- [Nationaal Archief / Hoffmann record](http://proxy.handle.net/10648/a93ab252-d0b4-102d-bcf8-003048976d84)
- [Hoffmann Commons file](https://commons.wikimedia.org/wiki/File:Stemming_Saarstatuut_Minister_President_Hoffmann,_Bestanddeelnr_907-3171.jpg)
- [LeMO: Johannes Hoffmann](https://www.hdg.de/lemo/biografie/johannes-hoffmann)
- [Deutsche Biographie: Johannes Hoffmann](https://www.deutsche-biographie.de/sfz33129.html)
- [CVCE: Johannes Hoffmann](https://www.cvce.eu/en/obj/johannes_hoffmann-en-706dbc0b-2041-401e-8948-7587ce1f2524.html)
- [Schmelcher Commons file](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg)
- [LVR Rheinische Geschichte: Walther Duerrfeld](https://www.rheinische-geschichte.lvr.de/Persoenlichkeiten/walther-duerrfeld-/DE-2086/lido/57c6991d65af78.08390995)
- [Wollheim Memorial: Walther Duerrfeld](http://www.wollheim-memorial.de/de/walther_duerrfeld_18991967)

