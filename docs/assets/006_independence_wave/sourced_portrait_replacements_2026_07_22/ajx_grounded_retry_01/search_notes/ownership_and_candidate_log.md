# AJX grounded portrait ownership and candidate log

Date: 2026-07-22

Scope: exact/variant real-person ownership evidence and bounded source search
for the two Event 006 Saar grounded identities. This log does not edit or
claim ownership of any runtime character, GFX, or localisation key.

## Ownership search evidence

The targeted scan covered these roots and file surfaces:

- current Chaos Redux `common/`, `history/`, `gfx/`, `interface/`,
  `localisation/`, and `events/` roots;
- vanilla Hearts of Iron IV installation;
- Kaiserreich workshop root `394360/1521695605`;
- approved workshop roots `394360/2265420196` and `394360/1458561226`.

Terms included the real names, spacing and underscore variants, and current
fictional portrait tokens:

```text
Johannes Hoffmann
Johannes_Hoffmann
johannes_hoffmann
Willy Schmelcher
Willy_Schmelcher
willy_schmelcher
Karl Becker
Karl_Becker
karl_becker
Karl Heinrich Emil Becker
Karl_Heinrich_Emil_Becker
Wilhelm Fahrmbacher
Wilhelm_Fahrmbacher
Max Braun
Max_Braun
AJX_friedrich_hoffmann
AJX_karl_becker
```

### Current Chaos Redux

No exact Johannes Hoffmann, Willy Schmelcher, Karl Becker, or Wilhelm
Fahrmbacher real-person owner was found in the current runtime roots. The
current package owns only the fictional consumers and their role-key sprites:

- `common/characters/006_independence_wave_saar_characters.txt`:
  `AJX_friedrich_hoffmann`, `AJX_karl_becker`;
- `interface/006_independence_wave_region_01_portraits.gfx`:
  `GFX_portrait_AJX_friedrich_hoffmann`,
  `GFX_portrait_AJX_karl_becker`;
- `history/countries/AJX - Saar.txt` recruits both fictional IDs.

Those fictional IDs are the parent implementation surface, not a reason to
clone a second real-person ID. The parent owns any guarded transfer.

### Vanilla and approved workshop roots

Vanilla has an active historical Karl Becker owner:

```text
history/countries/GER - Germany.txt:1047
recruit_character = GER_karl_heinrich_emil_becker #Artillery Scientist
```

Vanilla localisation defines the same historical name. Kaiserreich
`1521695605` also contains the `GER_karl_heinrich_emil_becker` localisation
token. This is a binding owner rejection for cloning Karl Becker into AJX.

Vanilla, Kaiserreich, and approved `2265420196` returned no exact live owner
for Johannes Hoffmann, Willy Schmelcher, or Wilhelm Fahrmbacher. Approved mod
`1458561226` contains a historical-person overlap:

```text
history/countries/SAR - Saarland.txt:163  name = "Johannes Hoffmann"
history/countries/SAR - Saarland.txt:164  picture = "Johannes_Hoffmann.dds"
```

Per the parent task clarification, this cross-mod historical-person overlap is
non-blocking. No art, DDS, or source file was copied from that mod; the
Hoffmann package uses the independent Nationaal Archief/Anefo CC0 original.

## Candidate ledger

| Candidate | Role considered | Source lead | Result | Disposition |
|---|---|---|---|---|
| Johannes Hoffmann (1890-1967), 1955 source | Saar civic / constitutional leader | Nationaal Archief/Anefo glass negative, 7 Sep 1955, Joop van Bilsen; Commons CC0; direct original retained in this package | Strong Saar identity and alive in 1936. The known photograph is clear and face-visible but visibly older than the scenario. | `needs_user_review` with complete source package |
| Johannes Hoffmann, circa 1935 lead | Saar civic / constitutional leader | Saar-Nostalgie page labels `Johannes Hoffmann etwa 1935`, credits Landesarchiv Saarbruecken, remote 360x271 image | Better era fit, but page states no reuse licence and the low resolution is weak for a 156x210 portrait. | `blocked`; no local master |
| Willy Schmelcher (1894-1974) | Saar police / security commander alternate | 1938 *Der Grossdeutsche Reichstag* portrait, A. Gerspach; Commons public-domain record | Exact Saarbruecken Polizeipraesident role from 1935-1942 and period-close portrait. This is police/SS leadership, not an army corps command. | `role_mismatch_research_only`; retained source package is not runtime approval |
| Karl Becker (1879-1940) | Palatinate/German artillery commander | 1937 Bundesarchiv CC BY-SA 3.0 DE portrait; April 1940 NAC public-domain portrait; Deutsche Biographie | Exact Speyer-born General der Artillerie, but technical/administrative career is weak for a corps commander and vanilla owns `GER_karl_heinrich_emil_becker`. | `rejected_vanilla_owner`; no local master |
| Wilhelm Fahrmbacher (1888-1970) | Palatinate corps commander | Generals.dk and Deutsche Digitale Bibliothek establish Zweibruecken origin and VII Army Corps command; Commons category has no suitable portrait | Strongest regional/role fit, but no pre-war or early-war face-visible portrait with a defensible reuse licence. | `blocked`; no local master |
| Max Braun (1892-1945) | Saar labour / civic leader | Saarbruecken municipal history and LVR resistance biography; face leads credited to private Braun/Sommer family archives | Strong labour identity, but available face source has no reuse licence. | `blocked`; no local master |
| Walther Duerrfeld (1899-1967) | Saar / Rhenish engineering and industrial commander alternate | US Army/OUSCCPAC/OCCWC public-domain trial portrait via Wollheim Memorial, circa 1945-49 | Born in Saarbruecken and active in Saar ironworks / IG Farben before 1936, but image is low-resolution and postwar. | `needs_user_review`; no local master copied |
| Hermann Roechling (1872-1955) | Saar industrial / civic authority | Commons modern photograph of a monument/effigy | Available image is not a period portrait. A 1932 printed scan lead has unresolved rights. | `blocked`; no local master |
| Josef Buerckel (1895-1944) | Saar administrative/political commissioner | Polish National Digital Archive public-domain image lead | Rights are stronger, but Gauleiter/Reichskommissar role is authoritarian political administration rather than civic/municipal constitutional leadership. | `blocked_role_fit`; no local master |
| Anton Dunckern (1906-1985) | Saar security commander alternate | Existing `wallonia_saar_retry_01` package, Berlin Document Centre c.1937 image | Exact Saar Gestapo role, but low-resolution source and territorial rights warning remain unresolved. | `needs_user_review` in prior package; not duplicated |

## Source-quality decisions

- The earlier 1941 Brazilian Immigration Agency Hoffmann image was not
  reused: its Commons page carries a URAA warning and family-estate
  provenance. The CC0 Nationaal Archief record is a separate source chain.
- The Saar-Nostalgie pre-1940 Hoffmann lead was inspected but not acquired;
  credit to Landesarchiv Saarbruecken is not a reuse licence, and 360x271 is
  not a defensible source-ready master for this portrait slot.
- Schmelcher's source master, crop, and DDS remain byte-preserved in the
  package only so the provenance and the earlier research decision are not
  lost. They must not be used as the live corps-commander portrait.
- Karl Becker source links were verified, but no binary was copied because the
  vanilla historical owner is active and his documented role is not a clean
  corps-command match.
- Fahrmbacher was not represented by a group-photo crop, grave image, or
  copyright-controlled portrait lead. No portrait was generated or
  reconstructed.
- No portrait was face-swapped, recoloured, repainted, or borrowed from an
  external mod. No ImageGen call was made in this retry.

## Research links

- [Hoffmann 1955 Commons source](https://commons.wikimedia.org/wiki/File:Stemming_Saarstatuut_Minister_President_Hoffmann,_Bestanddeelnr_907-3171.jpg)
- [Hoffmann pre-1940 lead](https://www.saar-nostalgie.de/Joho1.htm)
- [Max Braun municipal history](https://www.saarbruecken.de/kultur/stadtarchiv/schaufenster_stadtgeschichte/menschen/liste_der_stadtoberhaeupter/max_braun)
- [Max Braun LVR biography](https://www.rheinische-geschichte.lvr.de/Projekte/Widerstandskarte/max-braun-fuehrte-den-saarwiderstand-von-frankreich-und-england-aus-fort/DE-2086/lido/dc00019105)
- [Schmelcher Commons source](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg)
- [Karl Becker Bundesarchiv source](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-H27401,_Karl_Becker.jpg)
- [Karl Becker Deutsche Biographie](https://www.deutsche-biographie.de/sfz2563.html?language=en)
- [Fahrmbacher career lead](https://www.generals.dk/general/Fahrmbacher/Wilhelm_Karl/Germany.html)
- [Fahrmbacher Deutsche Digitale Bibliothek record](https://www.deutsche-digitale-bibliothek.de/person/gnd/105520829)
- [Fahrmbacher Commons category](https://commons.wikimedia.org/wiki/Category:Wilhelm_Fahrmbacher)
- [Walther Duerrfeld LVR biography](https://www.rheinische-geschichte.lvr.de/Persoenlichkeiten/walther-duerrfeld-/DE-2086/lido/57c6991d65af78.08390995)
- [Wollheim Memorial: Walther Duerrfeld](http://www.wollheim-memorial.de/de/walther_duerrfeld_18991967)

