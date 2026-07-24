# Leader portrait reference index

This directory is the user-requested, directly browsable HOI4 portrait-style reference pack for agents.
It contains a small male-only set of byte-identical Vanilla HOI4 review PNGs under `leaders/` and `commanders/`, plus role-specific contact sheets.
The complete canonical library remains under `../vanilla_reference/`; these copies are review material, never runtime assets.
Exact source mapping and SHA-256 values are in [`REFERENCE_MANIFEST.md`](REFERENCE_MANIFEST.md).

## Route by HOI4 role

| HOI4 role | Canonical reference path | Native canvas | Quick-reference sheet |
| --- | --- | ---: | --- |
| Country leader | `../vanilla_reference/portraits/leaders/` | `156x210` | `leaders/contact_sheet.png` |
| Army or navy commander | `../vanilla_reference/portraits/commanders/` | `156x210` | `commanders/contact_sheet.png` |
| Operative | `../vanilla_reference/portraits/operatives/` | `156x210` | canonical family sheet only |

The curated pack contains four country leaders and eight land/naval commanders, including four European named-command examples.
All are male-presenting and all are `156x210`.
It deliberately contains no Event 6 runtime art, generated people, female portraits, advisor icons, dossier cards, or `_small` derivatives.

Before producing a portrait:

1. Read the canonical [library rules](../vanilla_reference/README.md) and [catalog](../vanilla_reference/CATALOG.md).
2. Inspect the matching canonical contact sheet and this pack's role-specific sheet.
3. Keep country-leader and commander textures as full `156x210` portraits.
4. For a grounded real person, follow the fail-closed sequence exactly: unchanged attributed archival male photograph -> explicit head-and-shoulders crop -> source-locked identity-preserving ImageGen repaint in the matching HOI4 painted style -> deterministic `156x210` processing -> independent likeness, style, and provenance audit by someone other than the producer -> DDS conversion and runtime wiring only after every gate passes.
5. Retain the unchanged master, exact crop and crop-equality JSON, raw ImageGen result, processed `156x210` candidate, prompt, attribution, rights evidence, and independent audit record.
6. Reject raw-photo finishes, generic oil filters, reconstructed or substituted faces, weak likenesses, beautification, symmetrization, invented hidden detail, unsupported clothing or insignia, and style treatments that materially change the person.
7. Recompute processor `decoded_rgba_sha256` values with the domain-separated scheme documented in `../../tools/README.md`; do not compare them with a plain SHA-256 of raw RGBA bytes.

Reference PNGs may be viewed and supplied as style-only inputs.
Do not recolour, trace, wire, copy into runtime folders, or ship them as final Chaos Redux art.
