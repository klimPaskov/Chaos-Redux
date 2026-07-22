# Event 006 — BRI/AJX grounded portrait source retry

Date: 2026-07-22  
Mode: sourced real-person portrait research (source masters only)  
Status: mixed `source_ready`, `needs_review`, and `blocked`

This package retries the grounded real-person portraits for the BRI civic and
coastal-command roles and the AJX/Saar civic and industrial-security roles.
The package does not edit gameplay, localisation, `.gfx`, or the parent portrait
processor. No generated or generic face is used. The parent agent must make the
final role decision and run the approved native portrait pipeline; this package
does not contain processed PNG or runtime DDS output.

## Requested role mapping

The country-package handoffs describe the existing fictional placeholders as:

| Country | Requested role | Existing placeholder | Proposed runtime sprite (deferred) |
|---|---|---|---|
| BRI | civic commission / delegate | Tangi Kerbrat | `GFX_portrait_BRI_independence_wave_civic_commission` |
| BRI | coastal commandant | Jodoc Tanet | `GFX_portrait_BRI_independence_wave_coastal_commandant` |
| AJX | Saar municipal neutral commission | Friedrich Hoffmann | `GFX_portrait_AJX_saar_municipal_neutral_commission` |
| AJX | Saar industrial-security command | Karl Becker | `GFX_portrait_AJX_saar_industrial_security_command` |

## Candidate ledger

### BRI civic — sourced identity rejected for the current route role

**Marcel Cachin (1869–1958)** — `rejected_current_role_mismatch` for the
existing BRI civic-delegate token; `source_ready_labor_identity_only`.

- Identity and timing: male French politician, born in Paimpol, Brittany;
  alive on 1936-01-01. The Breton birth link supplies a direct regional civic
  identity without inventing a face.
- Source record: BnF/Gallica, Agence Meurisse, 1918 —
  [Gallica record](https://gallica.bnf.fr/ark:/12148/btv1b9030818k/f1),
  [full IIIF original](https://gallica.bnf.fr/iiif/ark:/12148/btv1b9030818k/f1/full/full/0/native.jpg).
  A convenient Commons metadata mirror is
  [Marcel Cachin 1918](https://commons.wikimedia.org/wiki/File:Marcel_Cachin_1918.jpg)
  (original upload [here](https://upload.wikimedia.org/wikipedia/commons/b/b1/Marcel_Cachin_1918.jpg)).
- Rights: published in 1918, therefore US copyright term expired before the
  1931 cutoff; Commons also records `PD-US expired` and the source as Gallica.
  The Commons page carries a missing-SDC-status warning, so the manifest keeps
  the direct Gallica provenance and the public-domain basis explicit.
- Retained source: `source_masters/BRI/BRI_marcel_cachin_gallica_meurisse_1918.jpg`
  — 5063×7000, mode `L`, 5,810,691 bytes,
  SHA-256 `85fa2c4d485bddde3e5fee903f52a3dc8f91f53f22159b38e1a62164f024e2a9`.
- Visual/crop note: clear black-and-white head-and-shoulders view, centered
  face, ample crop margin for a full `156×210` country-leader portrait. Event
  006 does not use an advisor/dossier portrait pipeline.
- Ownership scan: no exact current-project or vanilla character/portrait hit
  for `Marcel Cachin`, `Marcel_Cachin`, or `Cachin` in the bounded history,
  common, interface, gfx/leaders, and localisation roots.
- Role correction: the current `BRI_independence_wave_civic_delegate` is
  promoted as the oligarchic leader of the traditional regionalist compact or
  protected-ports patron route. Cachin's socialist and communist political
  career cannot plausibly fill either office. His source may support a future
  explicit labor-route slot, but it must not be wired to the current sprite or
  used to claim IW-004 portrait completeness.

### BRI coastal commandant — source-ready

**Henri-Léon Devin (1879–1973)** — `source_ready` for the accepted Joint
Coastal Command role.

- Identity and timing: male French naval officer, alive on 1936-01-01. He
  commanded École navale at Brest from September 1930 and was appointed préfet
  maritime de Brest in September 1936. The accepted office is the Joint Coastal
  Command, not the maritime prefecture, so his active Brest naval command is a
  direct start-date role and regional fit. Player-facing text must not call him
  maritime prefect before that later appointment.
- Role evidence: [French biography](https://fr.wikipedia.org/wiki/L%C3%A9on-Henri_Devin)
  (the page records the Brest command and September 1936 prefect appointment).
- Source record: BnF/Gallica, Agence Rol, 1930 —
  [Gallica record](https://gallica.bnf.fr/ark:/12148/btv1b53236203v),
  [full IIIF original](https://gallica.bnf.fr/iiif/ark:/12148/btv1b53236203v/f1/full/full/0/native.jpg),
  [Commons metadata](https://commons.wikimedia.org/wiki/File:Capitaine_de_vaisseau_Devin,_de_l%27Ecole_navale_-_btv1b53236203v.jpg).
- Rights: Commons records `PD-1996`, `PD France`, and source files from Gallica;
  the image is a 1930 French Agence Rol photograph.
- Retained source: `source_masters/BRI/BRI_leon_henri_devin_brest_prefet_1930.jpg`
  — 6318×8587, mode `L`, 5,541,014 bytes,
  SHA-256 `ab7d69e6f485be51bfc02823bf94187a9239b54f56525ff97223c9e7b2f7e4c0`.
- Visual/crop note: clean head-and-shoulders naval portrait with a clearly
  visible face and generous crop margin.
- Ownership scan: no exact current-project or vanilla identity/portrait hit
  for `Henri-Léon Devin`, `Léon-Henri Devin`, `Leon_Henri_Devin`, or `FRA_devin`.
- Parent disposition: `source_ready`. Process only as a full `156×210`
  commander/leader portrait after identity-preserving HOI4 refinish review.

**Raoul Castex (1878–1968)** — `rejected_nonphotographic_source`.

- Role/timing: vice-admiral and maritime prefect at Brest from 22 October 1935
  through September 1936; alive on 1936-01-01. This is the strongest role/date
  match found.
- Retained evidence: `source_masters/BRI/BRI_raoul_castex_brest_prefet_1935.jpg`
  — 513×744 RGB, 46,648 bytes,
  SHA-256 `25925384c4fc9fcd8ee8dea90680c7a31844a20dc60709e90210151f5867b227`.
  [Commons record](https://commons.wikimedia.org/wiki/File:Amiral-Raoul-Castex_1.jpg)
  identifies a 1935 Photo Archives Marine Nationale image and CC0 1.0.
- Rejection: the retained image is a bust/sculpture photograph, not a period
  headshot; it cannot meet the requested portrait evidence bar. A colorized
  blog photograph was found at [Envelopmer](https://envelopmer.blogspot.com/2020/11/brest-bal-des-fourriers-31-decembre.html),
  but its redistribution rights are unclear and it is not retained.
- Ownership scan: no active character/portrait owner was found; a bounded
  vanilla history/units comment mentions “Castex” only as a historical naval
  command note, not a character or portrait definition.

**Jean-Marie Charles Abrial (1879–1962)** — `rejected_active_vanilla`.

- Source evidence retained for audit only: BnF/Gallica Agence Rol, Brest,
  1929 — [Gallica record](https://gallica.bnf.fr/ark:/12148/btv1b53212252g/f1),
  [full IIIF original](https://gallica.bnf.fr/iiif/ark:/12148/btv1b53212252g/f1/full/full/0/native.jpg),
  [Commons record](https://commons.wikimedia.org/wiki/File:(Brest,_5-4-29)_commandant_Abrial_du_Tourville_(croiseur_français)_-_btv1b53212252g.jpg).
  Original source: `source_masters/BRI/BRI_jean_marie_abrial_gallica_rol_brest_1929_original.jpg`
  (6045×8390, `L`, 4,681,628 bytes, SHA-256
  `82dde7b29e49a3e2f2815073e9c80330c760f696ae2c682d262cb8858f9af0d7`).
- Rejection: vanilla owns `FRA_jean_marie_abrial`/
  `FRA_jeanmarie_charles_abrial` and the associated FRA portrait. Do not wire
  or process for BRI. The size-negotiated derivative
  `source_masters/BRI/BRI_jean_marie_abrial_gallica_rol_brest_1929.jpg`
  (2000×2775, SHA-256
  `5d8e513b034e6c134ae272b1cee60a5ba05e554e1ce0e62c208f773c19bd22ff`)
  is marked `rejected_derivative` and must not be processed.

**Charles Huntziger (1880–1941)** — `rejected_active_vanilla`.

- A rights-clear historical source was considered, but the vanilla package
  already owns `FRA_charles_huntziger` and its FRA leader portrait. This is an
  ownership collision, not an acceptable BRI coastal-command replacement.

### AJX/Saar civic — review-gated (exact role remains blocked)

**Johannes Hoffmann (1890–1967)** — `needs_review_rights`.

- Identity and timing: male Saar politician, born in Landsweiler-Reden, Saar;
  alive on 1936-01-01. The Saar civic identity and political role fit the
  municipal-neutral commission better than an occupation official.
- Source record: anonymous Brazilian Immigration Agency photograph, Rio, 2
  June 1941 — [Saar-Nostalgie source page](https://www.saar-nostalgie.de/Joho1.htm),
  [direct source bitstream](https://www.saar-nostalgie.de/Bilder/Joho/Joho1941_2c.jpg),
  [Commons metadata mirror](https://commons.wikimedia.org/wiki/File:WP_Johannes_Hoffmann_1941.jpg).
- Retained source: `source_masters/AJX/AJX_johannes_hoffmann_saar_nostalgie_1941.jpg`
  — 306×408 RGB, 67,510 bytes,
  SHA-256 `9f9032681cd7cb2f087d2b89cd7932c8702e1fe872e33533cd754d19819416cf`.
- Visual/crop note: face is clear and crop-capable, but source dimensions are
  small compared with Gallica masters.
- Rights: Commons labels the Brazilian anonymous photograph public domain under
  Brazil's law, but also places it in `Works copyrighted in the U.S.` and warns
  that a US public-domain tag is missing. The Saar-Nostalgie family-estate page
  does not grant a redistribution licence. Keep `needs_review_rights`; do not
  process or wire until the parent has independent rights evidence.
- Ownership scan: no exact current-project or vanilla character/portrait hit for
  `Johannes Hoffmann`, `Johannes_Hoffmann`, or the relevant Hoffmann variants.

**Josef Bürckel (1895–1944)** — `rejected_role_occupation_figure`.

- A period source exists, but he was the Nazi occupation/annexation official in
  the Saar. Mapping that antagonistic figure into AJX's civic-neutral role would
  violate the role brief; no fallback face is substituted.

### AJX/Saar industrial-security commander — blocked

No candidate met all three gates (Saar-specific role on 1936-01-01, usable
period portrait, and defensible US redistribution rights):

- **Anton Dunckern (1905–1985)** — exact Saarbrücken Gestapo chief from March
  1935, but the available circa-1937 Personal File Berlin Centre image has
  unknown author and no clear US rights basis. Commons record:
  [Anton Dunckern.jpg](https://commons.wikimedia.org/wiki/File:Anton_Dunckern.jpg).
  Status `needs_review_rights`; no local source master retained.
- **Willy Schmelcher (1894–1974)** — Saar police president, 1935–42; 1938
  Reichstag portrait by A. Gerspach. Commons' `PD-Germany §134` claim does not
  resolve US/URAA status for the foreign 1938 publication. [Commons record](https://commons.wikimedia.org/wiki/File:Willy_Schmelcher.jpg).
  Status `needs_review_rights`; no local source master retained.
- **Theodor Berkelmann (1894–1943)** — 1938 Reichstag source by Franz
  Langhammer, but role/date and US rights remain unresolved. [Commons record](https://commons.wikimedia.org/wiki/File:BerkelmannTheo.jpg).
  Status `needs_review_role_and_rights`; no local source master retained.
- **Kurt Daluege (1897–1946)** — 1936 Bundesarchiv image is CC BY-SA 3.0
  Germany, but his role is Berlin police general; only a 1940 Saar inspection is
  evidenced, so he is not a valid 1936 Saar commander. [Commons record](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-2007-1010-502,_Kurt_Daluege.jpg).
  Status `needs_review_role`; no local source master retained.

The exact AJX commander remains `blocked`. A generated or generic substitute is
not permitted.

## Ownership and processing boundary

The bounded ownership scan covered current project `common`, `history`,
`interface`, `gfx/leaders`, and `localisation` roots plus the corresponding
vanilla roots. Exact matches for Abrial and Huntziger were found in vanilla
characters, leader portraits, and localisation; they are rejected. No active
character/portrait owner was found for Cachin, Devin, or Hoffmann. Castex appears
only in a historical vanilla naval-unit comment, not as an active character or
portrait.

Henri-Léon Devin is source-ready for the BRI coastal command. Cachin is usable
only for a separate labor-route identity and does not clear the current BRI
civic token. Hoffmann requires rights review, and the AJX command role remains
blocked. No candidate may be sent through
the report-event processor, advisor pipeline, or DDS converter from this retry
folder until role and rights decisions are recorded by the parent.

## Deferred outputs

| Sprite name | Deferred runtime path | Source status |
|---|---|---|
| `GFX_portrait_BRI_independence_wave_civic_commission` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` | Blocked; Marcel Cachin rejected for the current traditional/patron role |
| `GFX_portrait_BRI_independence_wave_coastal_commandant` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` | Henri-Léon Devin `source_ready` |
| `GFX_portrait_AJX_saar_municipal_neutral_commission` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` | Hoffmann rights review-gated |
| `GFX_portrait_AJX_saar_industrial_security_command` | `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_command.dds` | Blocked |

Processed PNG paths and final DDS paths are intentionally empty. The parent
agent owns independent visual approval, native portrait processing, DDS conversion,
and `.gfx` wiring after a candidate is accepted. No contact sheet was created:
there is one current-role source-ready master and the remaining retained binaries are
explicitly rejected/review evidence rather than alternatives for selection.
