# Wallonia/Saar source-research and ownership log

Date: 2026-07-22  
Scope: Event 006 Independence Wave (`IW-006` AFX Wallonia and `IW-010` AJX
Saar) grounded male leader/commander portraits.  
Mode: source research and unchanged archival master acquisition only.

## Ownership gate

The exact names and variants below were searched in the current repository's
`common/characters`, `history/countries`, `common/country_leader`, `interface`,
`gfx/leaders`, and `localisation/english` trees. The search was performed before
copying any candidate. No new character, GFX, localisation, or runtime asset
was created by this retry.

| Search terms | Current-project result |
|---|---|
| `Jules Destrée`, `Jules Destree` | `Jules Destrée` is already the live display/identity behind `AFX_walloon_provisional_assembly`: `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`, `history/countries/AFX - Wallonia.txt`, and `interface/006_independence_wave_region_01_portraits.gfx`. The ASCII spelling has no separate owner. Reuse is `rejected_current_project_owner` absent a guarded transfer contract. |
| `Georges Truffaut` | No exact or variant owner hit. Candidate remains rights-gated because the Institut Destrée page says `Droits SOFAM`, while a Commons copy claims CC BY-SA 4.0. |
| `François Bovesse`, `Francois Bovesse` | No owner hit. Candidate blocked because no face-visible free portrait source was found. |
| `Jules Bastin`, `Jules-Auguste-Ghislain Bastin` | No owner hit. Candidate is role-accurate for a 1936 Walloon/Belgian Army commander, but available portrait pages do not state a defensible reuse licence. |
| `Jules-Joseph Pire`, `Jules Pire` | No owner hit. Candidate is role-accurate, but no rights-defensible original portrait was located. |
| `Johannes Hoffmann`, `Johann Hoffmann`, `Joho` | No owner hit. Candidate image is face-visible but has conflicting Brazilian-PD/URAA/family-estate provenance. |
| `Max Braun`, `Matthias Braun` | No owner hit. Available Saar image leads are political/civilian and do not satisfy the security/industrial commander role. |
| `Josef Bürckel`, `Josef Burckel` | No owner hit. Public-domain NAC/Commons image lead exists, but date/role/political-context review is still required and no local master was acquired. |
| `Anton Dunckern` | No owner hit. A circa-1937 Personal File in Berlin Document Centre portrait was acquired as a review-gated alternate. |
| `Willy Schmelcher` | No owner hit. A 1938 *Der Großdeutsche Reichstag* portrait was acquired as the primary AJX security-commander source. |
| `Theodor Berkelmann` | No owner hit. Rejected: his Saar HSSPF role begins in 1940, not the 1936 role window. |
| `Hermann Röchling`, `Hermann Rochling` | No owner hit. Rejected: available face source was a modern 2018 monument/effigy photograph, not a period portrait. |

The active-owner match is intentionally not copied into this package. This
prevents silently replacing or cloning a current identity while leaving its
character, localisation, and sprite consumers ambiguous.

## Candidate evidence and dispositions

### AFX Wallonia civic leader

1. **Jules Destrée** - exact Walloon Movement and civic fit, alive through the
   start of 1936. Existing project owner; no copy made.
2. **Georges Truffaut** - Liège activist, municipal councilman, deputy, and
   alderman for public works from 1935. [Institut Destrée page](http://www.wallonie-en-ligne.net/1995_Cent_Wallons/Truffaut_Georges.htm)
   identifies the photograph as `Droits SOFAM`. [Commons file](https://commons.wikimedia.org/wiki/File:TRUFFAUT_Georges.gif)
   claims CC BY-SA 4.0 but points to the same rights-noted source. No source
   file retained; `needs_user_review`.
3. **François Bovesse** - credible Namur/Walloon politician, but the [Commons
   category](https://commons.wikimedia.org/wiki/Category:Fran%C3%A7ois_Bovesse)
   contains no defensible face-visible archival portrait. `blocked`.

### AFX Wallonia reserve or industrial commander

1. **Jules Bastin** - Roux/Charleroi-born Belgian Army officer; 1936
   sous-chef d'état-major of the Cavalry Corps and École de guerre tactics
   professor. [Free Belgians biography](https://www.freebelgians.be/articles/print.php?id=29)
   exposes a portrait URL (`https://www.freebelgians.be/upload/image34.jpg`),
   but no licence or archive release. `blocked_rights`.
2. **Jules-Joseph Pire** - Walloon-born lieutenant general and Chasseurs
   Ardennais commander. [Biography lead](https://fr.wikipedia.org/wiki/Jules_Pire)
   is role-accurate, but no original with a clear reuse grant was acquired.
   `blocked_rights`.
3. **Émile Dossin de Saint-Georges** - Liège-born general, but died in January
   1936 and therefore is not a strong active/alive scenario-year commander.
   Available Commons files were not used. `rejected_era_fit`.

### AJX Saar civic or municipal leader

1. **Johannes Hoffmann** - Saar civic/editorial leader and status-quo politician
   before the 1935 plebiscite. [Commons 1941 file](https://commons.wikimedia.org/wiki/File:WP_Johannes_Hoffmann_1941.jpg)
   is anonymous Brazilian Immigration Agency material; [Saar-Nostalgie](https://www.saar-nostalgie.de/Joho1.htm)
   states family-estate provenance, and Commons warns of possible US rights
   restoration. `needs_user_review`; not source-ready.
2. **Josef Bürckel** - Saar Reichskommissar/Gauleiter from 1935; [Commons
   page](https://commons.wikimedia.org/wiki/File:Josef_B%C3%BCrckel.jpg) links a
   1937-39 original [NAC image](https://upload.wikimedia.org/wikipedia/commons/d/d3/Josef_B%C3%BCrckel.jpg)
   marked public domain. This is an authoritarian political administrator,
   not a neutral municipal leader; no local file was retained while role fit
   was unresolved. `needs_user_review_role_fit`.
3. **Hans Neikes / Ernst Dürrfeld / Emil Mangold** - Saarbrücken mayoral
   candidates found in city-chronicle research, but no defensible face-visible
   period portrait was located. `blocked_no_face_source`.

### AJX industrial or security commander

1. **Willy Schmelcher** - exact Saarbrücken police-president identity from March
   1935 to October 1942. [Commons file](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg)
   identifies the 1938 book source, A. Gerspach as image credit, and
   `PD-Germany-§134` public-domain metadata. Acquired unchanged as primary;
   `source_ready` pending parent legal/context review.
2. **Anton Dunckern** - Gestapo chief in Saarbrücken after March 1935; [Commons
   file](https://commons.wikimedia.org/wiki/File:Anton_Dunckern.jpg) credits a
   circa-1937 Personal File in the Berlin Document Centre, author unknown, and
   marks Public domain/PDM with a US-status warning. Acquired unchanged as a
   low-resolution alternate; `needs_user_review`.
3. **Theodor Berkelmann** - real SS official, but his Saar HSSPF assignment is
   post-1940, so not a 1936 role fit. `rejected_era_fit`.
4. **Hermann Röchling** - Saar industrialist, but the available Commons face
   lead is a modern photograph of a monument/effigy, not a period portrait.
   `rejected_source_type`.

## Search and download notes

- Wikimedia Commons API metadata was queried for the two acquired files;
  direct uploads were downloaded with a descriptive user-agent. The files
  were checked as JPEGs with nonzero byte counts and exact dimensions before
  being copied into `source_masters/AJX/`.
- The acquired masters were not downloaded through a thumbnail, image proxy,
  re-encoder, or screenshot path. Their SHA-256 values are in the package-level
  [`source_hashes.sha256`](../source_hashes.sha256).
- Wikimedia upload requests for Truffaut and Bürckel were intermittently
  throttled; no HTML/error body was retained as an image. Truffaut therefore
  remains rights-gated and Bürckel remains a source lead without a local file.
- No face was generated or identity substituted. Blocked roles remain blocked
  until a human supplies a defensible source/rights decision or a compliant
  original is found.
