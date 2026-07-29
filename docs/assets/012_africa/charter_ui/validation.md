# Event 012 Charter League UI validation

Validation was run after DDS conversion and before handoff.

- Every requested static source has an exact processed PNG and final DDS.
- Static dimensions decoded from DDS headers: 1000x680, 976x84, 300x546, 316x546, 256x64, 128x36, 128x36, 70x24, 92x28, 330x240, 330x94, and 330x202, matching the Charter GUI layout.
- Animation sheets decode to 512x64 for 8 frames and 640x64 for 10 frames. Static fallbacks decode to 64x64.
- Static DDS files are opaque painted UI surfaces with alpha range 255..255. Animation sheets and static fallbacks have real alpha with range 0..255 and transparent corners.
- Decoded DDS review PNGs are under `decoded_dds_png/`; the final runtime montage is `contact_sheets/final_dds_montage.png`; the static source montage is `contact_sheets/static_contact.png`; animation montages are under each animation `previews/` directory.
- GIF previews use 125 ms seal frames and 167 ms authority-ring frames and are review-only.
- Final texture paths match the pre-registered `interface/012_africa_charter.gfx` texture paths exactly. No `.gfx` or `.gui` file was edited in this package.

Visual review notes: the static contact sheet shows a coherent painted brass/indigo/earth family with readable dark text-safe interiors. The animation contact sheets show authored state changes and stable centered silhouettes. Generated source frames remain in the package for audit and are not runtime dependencies.
