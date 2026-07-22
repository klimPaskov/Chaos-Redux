# Event 006 AJX grounded source retry handoff

Date: 2026-07-22
Owner: sourced visual asset subagent
Scope: source/research package and fail-closed role/ownership handoff only

## Result

The AJX retry now documents the available grounded sources and the gates that
prevent an unsafe commander substitution. No current commander candidate is
source-ready for the live `AJX_karl_becker` army corps-commander surface.

- **Leader candidate - Johannes Hoffmann (1890-1967):** complete source
  master, explicit 156x210 head-and-shoulders crop, DDS, and provenance. The
  Nationaal Archief/Anefo original is CC0 and the Saar civic/constitutional
  identity is strong. Status remains `needs_user_review` because the image is
  dated 7 September 1955, after the 1936 scenario; the parent must explicitly
  accept the age/era gap before wiring.
- **Pre-1940 Hoffmann lead:** Saar-Nostalgie labels a circa-1935 image and
  credits Landesarchiv Saarbruecken. It is only 360x271 and has no stated reuse
  licence, so it is `blocked` and was not copied or processed.
- **Willy Schmelcher (1894-1974):** complete archival source, crop, and DDS
  are retained as `role_mismatch_research_only`. Schmelcher was Saarbruecken
  Polizeipraesident and SS/police leadership, not an army corps commander. His
  package must not be wired to `AJX_karl_becker`.
- **Karl Becker (1879-1940):** exact Speyer-born General der Artillerie leads
  are rights-documented, but the vanilla live owner
  `GER_karl_heinrich_emil_becker` is active and Becker's technical/administrative
  role is not a clean corps-command match. No source master was acquired.
- **Wilhelm Fahrmbacher (1888-1970):** strongest Zweibruecken/Palatinate and
  later corps-command lead, but no rights-clear face-visible pre-war source
  was found. No group-photo crop or generated substitute was made.
- **Max Braun (1892-1945):** strong Saar labour/civic lead, but available
  municipal/family-archive face sources have no defensible reuse licence. No
  source master was acquired.

No character, event, localisation, GFX, history, interface, runtime `gfx/`,
advisor icon, or `_small` file was edited. No ImageGen call was made because
the selected identities did not pass both role and source gates.

## Owned files

Asset package:

- [README.md](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/README.md)
- [manifest.md](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/manifest.md)
- [gfx_handoff.md](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/gfx_handoff.md)
- [ownership and candidate log](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/search_notes/ownership_and_candidate_log.md)
- [contact sheet](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/contact_sheets/ajx_grounded_sources_and_crops.png)
- [source hash inventory](../../../assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/ajx_grounded_retry_01/source_hashes.sha256)
- `source_masters/AJX/AJX_johannes_hoffmann_nationaal_archief_1955.jpg`
- `source_masters/AJX/AJX_willy_schmelcher_polizeipraesident_1938.jpg`
- `processed_png/AJX/AJX_johannes_hoffmann_head_shoulders.png`
- `processed_png/AJX/AJX_willy_schmelcher_head_shoulders.png`
- `final_dds/AJX/AJX_johannes_hoffmann.dds`
- `final_dds/AJX/AJX_willy_schmelcher.dds`

No new binary was added in this corrective handoff. The Schmelcher binaries
remain in the package only as research provenance and are not runtime-approved.

## Handoff details

1. Hoffmann retained source: Nationaal Archief/Anefo, photographer Joop van
   Bilsen, archive component 907-3171, 7 Sep 1955, [Commons record](https://commons.wikimedia.org/wiki/File:Stemming_Saarstatuut_Minister_President_Hoffmann,_Bestanddeelnr_907-3171.jpg),
   [durable archive handle](http://proxy.handle.net/10648/a93ab252-d0b4-102d-bcf8-003048976d84),
   [direct original](https://upload.wikimedia.org/wikipedia/commons/f/f9/Stemming_Saarstatuut_Minister_President_Hoffmann%2C_Bestanddeelnr_907-3171.jpg?download=1).
2. Pre-1940 Hoffmann lead: [Saar-Nostalgie page](https://www.saar-nostalgie.de/Joho1.htm),
   caption `Johannes Hoffmann etwa 1935`, credit `Foto: L.A. Saarbruecken`,
   remote image `Bilder/Joho/vor1945/JoHo1935bk.jpg`, 360x271. Rights and
   source quality are unresolved; no binary was copied.
3. Schmelcher retained research source: 1938 *Der Grossdeutsche Reichstag*
   portrait, image credit A. Gerspach, [Commons record](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg),
   [direct original](https://upload.wikimedia.org/wikipedia/commons/6/69/Willy_Schmelcher.jpg),
   Commons public-domain / `PD-Germany-Section-134` record. His police/SS
   role is a hard mismatch for the live army corps commander.
4. Karl Becker research links: [1937 Bundesarchiv portrait](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-H27401,_Karl_Becker.jpg),
   [April 1940 NAC portrait](https://commons.wikimedia.org/wiki/File:General_Karl_Becker.jpg),
   and [Deutsche Biographie](https://www.deutsche-biographie.de/sfz2563.html?language=en).
   Vanilla recruits `GER_karl_heinrich_emil_becker`; no source master was
   acquired or transferred.
5. Fahrmbacher research links: [career record](https://www.generals.dk/general/Fahrmbacher/Wilhelm_Karl/Germany.html),
   [Deutsche Digitale Bibliothek](https://www.deutsche-digitale-bibliothek.de/person/gnd/105520829),
   and [Commons category](https://commons.wikimedia.org/wiki/Category:Wilhelm_Fahrmbacher).
   No rights-clear face portrait was found.
6. Max Braun research links: [Saarbruecken municipal history](https://www.saarbruecken.de/kultur/stadtarchiv/schaufenster_stadtgeschichte/menschen/liste_der_stadtoberhaeupter/max_braun)
   and [LVR biography](https://www.rheinische-geschichte.lvr.de/Projekte/Widerstandskarte/max-braun-fuehrte-den-saarwiderstand-von-frankreich-und-england-aus-fort/DE-2086/lido/dc00019105).
   Available face sources are credited to private family archives without a
   reuse licence; no source master was acquired.

## Parent actions required

- Decide whether the 1955 Hoffmann image is acceptable for the 1936 grounded
  leader. If not, keep the leader surface `needs_user_review`; do not invent or
  generic-fill it.
- Do not transfer Schmelcher to the corps role. Seek a new rights-clear,
  face-visible, role-correct commander source before making a sprite handoff.
- Do not clone Karl Becker from vanilla or crop a Fahrmbacher group image.
- Do not run ImageGen unless both selected identities first pass the role and
  source gates; if an identity-preserving edit is later approved, retain the
  unchanged attributed source master alongside the output.

## Validation evidence

- Retained source masters were downloaded from direct Wikimedia upload URLs and
  remain hash-recorded unchanged.
- Existing PNG dimensions are exactly 156x210; DDS headers report width 156
  and height 210, and the package hash inventory remains unchanged because no
  binary was added in this corrective documentation pass.
- The contact sheet remains a visual comparison of the retained masters and
  crops. Its generic `source-ready crop` labels describe processing shape, not
  approval of the Schmelcher role.
- No files outside the existing asset package and this dated handoff were
  changed by this subagent.

## Focused commit

This corrective documentation pass is committed separately; the final commit
is `e8601f3b7` (the follow-up handoff hash record is committed separately).
