# Event 014 Static Mechanic-Window Art Manifest

The 26 mechanic-window assets in this package are final at the exact dimensions frozen in `docs/plans/014_cannibalism_plans/014_gui_dimension_ledger.md`.

Each row has:

- an independently generated full-resolution source in `source_png/`;
- an exact-size processed master in `processed_png/`;
- a two-layer OpenRaster master in `editable_ora/`, with generated artwork and a separate visible text-safe guide layer;
- a pixel-identical runtime PNG and an uncompressed, one-image-level 32-bit BGRA DDS under `gfx/interface/014_cannibalism/`;
- source, processed, OpenRaster, PNG, and DDS SHA-256 hashes in `../validation/static_gui_inventory.tsv`.

The validation-only contact sheet `../validation/static_gui_text_safe_native_contact.png` shows every final at native resolution with the actual rectangles from `interface/014_cannibalism_frontline_hunger.gui` superimposed. The guides are absent from all runtime textures.

`revealed_portrait_frame` and `transformed_portrait_frame` have true transparent portrait openings. No early or network art includes the revealed leader, a unique revealed-command silhouette, or a transformed-route symbol.

Final processing is reproducible through `../process_gui_nonportrait_assets.py`. It performs crop/resize, keyed-background cleanup for the two portrait frames, guide-master assembly, DDS writing, hashing, and validation; it does not synthesize or fake source artwork.
