# Event 006 BRI Henri-Léon Devin revision 02 visual admission audit

Date: `2026-07-22`  
Reviewer scope: independent visual/source admission only. The unchanged source
master, ImageGen master, native PNG, manifests, GFX, gameplay, localisation,
and skills were not edited. This handoff is the only file changed by this
review.

## Decision

**`approved_visual_source_only` — admit for the parent-owned native DDS
conversion and runtime review.**

The revision preserves the sourced Henri-Léon Devin identity and the
source-supported naval uniform details at both full master size and native
`156x210` scale. The prior trial's unverified coloured ribbon/trim treatment,
dark olive background, and harsher finish are corrected. This is not a claim
that a DDS or runtime sprite exists; do not wire a path into `docs/assets/`.

## Grounded source gate

- Subject: Henri-Léon Devin (1879–1973), grounded real male French naval
  officer, alive at the 1936 start date.
- Accepted role: BRI Joint Coastal Command. The source manifest records his
  command of École navale at Brest from September 1930; it does not present him
  as maritime prefect before the later September 1936 appointment.
- Source: BnF/Gallica Agence Rol, 1930, documented `PD-1996`/`PD France` basis.
- Source mode: `grounded_source_only`. The generated master is admitted only as
  an identity-preserving repaint/recomposition of the unchanged attributed
  source; it is not a generated substitute identity.
- Ownership evidence: the bounded source manifest records no active project or
  vanilla character/portrait owner for `Henri-Léon Devin`, `Léon-Henri Devin`,
  `Leon_Henri_Devin`, or `FRA_devin`. Event 006 has no advisor portrait or
  advisor-icon requirement.

## Exact file verification

| Item | Path | Actual dimensions / mode | SHA-256 |
|---|---|---:|---|
| Unchanged source master | `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/source_masters/BRI/BRI_leon_henri_devin_brest_prefet_1930.jpg` | `6318x8587`, `Format8bppIndexed` | `ab7d69e6f485be51bfc02823bf94187a9239b54f56525ff97223c9e7b2f7e4c0` |
| ImageGen master | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/imagegen_sources/BRI/BRI_henri_leon_devin_hoi4_revision_02.png` | `1082x1454`, `Format24bppRgb` | `d9cfdce881cde859a6d1aa46787fdd4f5f2a13acb7ac4d7528414cb60cdfcc52` |
| Native review PNG | `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/processed_png/BRI/BRI_henri_leon_devin_hoi4_revision_02.png` | `156x210`, `Format24bppRgb` (opaque) | `2ab9fe7986964db30b5b3553268739097168a92f4becf0ae07cabddb9b891bae` |

The measured dimensions, modes, and hashes agree with the refinish manifest
and the retained `source_hashes.sha256` entry. The manifest's recorded
processing is internally consistent: `1080x1454` crop at `x=1,y=0` from the
`1082x1454` master, then Lanczos resize to `156x210`, with no frame, filter,
dossier treatment, or post-generation face edit.

## Canonical comparison basis

I inspected the canonical root README/CATALOG and the role-specific leader and
commander contact sheets. The direct comparisons were:

- `assets/vanilla_reference/portraits/leaders/contact_sheet.png` plus
  `den_thorvald_stauning.png`, `fin_carl_mannerheim.png`,
  `ice_sveinn_bjornsson.png`, and `ire_eamon_de_valera.png` for the common
  HOI4 painted finish, quiet background, value control, and native framing.
- `assets/vanilla_reference/portraits/commanders/contact_sheet.png` plus
  `generic_africa_navy_1.png` and `generic_africa_navy_2.png` for full naval
  commander framing and readable cap/upper-torso treatment.
- The retired `assets/leader_portraits/` sheets were checked only to confirm
  their routing note; they are not an active source of truth.

All canonical role references use the full `156x210` portrait canvas.

## Visual findings

| Check | Result | Evidence |
|---|---|---|
| Source identity and role | **Pass** | The repaint remains the same naval officer from the Gallica photograph, with the accepted Brest naval-command role and grounded male identity. No replacement face, second person, advisor identity, or generic substitute appears. |
| Full-size likeness | **Pass** | The long face, low/hooded eyes under the visor, straight nose, thin moustache, narrow mouth, ears, and reserved expression track the unchanged photograph. The face reads as Devin without relying on the cap alone. |
| Native `156x210` likeness | **Pass** | At native scale the cap silhouette, eyes, nose, thin moustache, jaw, and centered head remain readable and identity-specific. The face is not reduced to a generic naval officer. |
| Age and expression | **Pass** | The master stays near the source's early-50s appearance and reserved forward gaze; there is no visible beautification, de-aging, gender drift, or expression substitution. |
| Cap, badge, and bands | **Pass** | The source-supported naval cap crown, visor, anchor-in-laurel badge, and stacked band spacing are retained without an extra emblem or changed device. Bright areas remain neutral off-white/silver-gray rather than invented award colors. |
| Shoulder boards | **Pass** | The source-supported shoulder-board geometry and light/dark value relationship are carried through; no new colored piping, rank device, or decorative trim is introduced. |
| Coat and buttons | **Pass** | The dark double-breasted naval coat, white collar, tie, broad lapels, and button rhythm remain consistent with the source. The standard portrait crop keeps the head, cap, shoulders, and chest inside the canvas without clipping. |
| Both ribbon rows | **Pass** | The short upper chest row and longer lower row remain in the source position and arrangement. Bars use neutral charcoal, silver-gray, off-white, and muted sepia only; no award colors or medal meanings are inferred. |
| Invented colors/decorations | **Pass** | The previous bright colored ribbon/accent and brightened rank decoration are absent. No flags, text, frames, props, extra medals, fantasy elements, or additional people are visible. |
| HOI4 painted finish | **Pass with minor note** | The result is a coherent restrained repaint with controlled contrast and a readable silhouette. Brush texture remains visible at full size but is substantially calmer than trial 01 and compatible with the canonical leader/commander family at native scale. |
| Background/value family | **Pass** | The background is pale, quiet warm cream rather than olive or vignetted. Master top-corner samples are approximately RGB `218,209,189` and `223,212,189`; native top corners are approximately RGB `223,213,192` and `227,215,192`. |
| Crop and readability | **Pass** | The full master and native PNG retain an uncropped cap, clear face, complete shoulder silhouette, and readable chest rows. No source-critical detail is cut by the `156x210` review canvas. |

## Runtime boundary and remaining work

- Visual/source admission is approved; the parent may run the repository-standard
  DDS converter and its own final runtime/GFX checks.
- No DDS, `.gfx` edit, gameplay edit, localisation edit, or advisor asset was
  created or approved by this audit.
- No fallback, generic portrait, invented decoration, or alternate identity is
  authorized.
- There are no visual-gate simplifications, omissions, or blockers. Final
  runtime completion remains parent-owned and must not be inferred from this
  visual approval.

## Validation evidence

- `System.Drawing` decode verified the source, full ImageGen master, native PNG,
  and canonical role references; the three Devin inputs have the exact sizes and
  pixel formats recorded above.
- SHA-256 values were recomputed locally and match the refinish manifest and
  retained source-hash record.
- Full-size and native visual inspection covered likeness, age/expression,
  cap/badge/bands, shoulder boards, coat/buttons, both ribbon rows, invented
  colors/decorations, crop/readability, pale background, and vanilla HOI4
  painted finish. No DDS conversion or live-game admission test was run in this
  bounded audit.
