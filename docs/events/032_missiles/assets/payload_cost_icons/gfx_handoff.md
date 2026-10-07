# GFX Handoff: Event 32 Payload Cost Texticons

## Chemical payload

The parent-registered sprite is `GFX_cbrn_chemical_payload_texticon` in `interface/cbrn_payload_texticons.gfx`, pointing to the exact path `gfx/texticons/cbrn_chemical_payload_texticon.dds`.

That DDS now exists at 30×12 with native alpha and exact decoded pixel equality to `docs/events/032_missiles/assets/payload_cost_icons/processed_png/cbrn_chemical_payload_texticon.png`.

The source, processed PNG, prompt lineage, 4× nearest-neighbour preview, DDS round-trip, and review sheet are in `docs/events/032_missiles/assets/payload_cost_icons/`.

The parent approved the chemical silhouette, muted palette, alpha, and poison mark when paired with the exact tooltip context on 2026-10-07.

Chemical art production is `complete`; the parent owns consumer cost wiring.

## Biological payload

The first safe biological pictogram request was refused with request ID `dfa3a081-163e-4bc8-bbcd-6227b56330ab`; that history and its exact prompt are preserved in `manifest.md`.

The parent-provided revised benign brief produced a transparent standard three-lobed glyph through built-in ImageGen, then a focused edit simplified its linework for a 12×12 footprint.

The selected source, processed 30×12 RGBA PNG, and pixel-identical one-level BGRA DDS now exist at the parent-registered paths.

Status is parent-reviewed and wired; the parent inspected `contact_sheet_current.png` at native and 4× size and approved the distinct biological-hazard glyph and transparent edges.
The shared sprite is consumed by Event 032's preparation cost localisation; native game cost-row fit remains unverified.

The worker did not edit `interface/cbrn_payload_texticons.gfx`.

## Nuclear payload reuse

Reuse the existing installed vanilla `GFX_unit_nuclear_missile_icon_small_texticon` from `interface/texticons.gfx:2945-2950`, whose exact texture is `gfx/texticons/unit_nuclear_missile_icon_small.dds`.

Do not create a new Event 32 nuclear texticon or DDS filename.

The support-equipment texticon and the three Event 32 sibling texticons were inspected as comparators only; none is an exact chemical or biological payload-cost match.

## Review files

- `contact_sheet.png` is the immutable chemical sheet the parent reviewed and approved.
- `contact_sheet_current.png` shows the chemical approval, biological source and DDS candidate at native and 4× views, nuclear reuse, support comparator, and preserved refusal history.
- `evidence/consumer_reference_previews/consumer_reference_contact_sheet.png` shows the two-frame vanilla nuclear and shared support textures plus all three 24×24 Event 32 siblings.
- `manifest.md` contains exact source hashes, dimensions, alpha checks, prompt paths, consumer references, offline documentation revisions, and the reuse audit.

