# Facility icon halo correction handoff

Status: complete.

## Runtime change

- Updated only `gfx/interface/buildings/building_icon_strip.dds`.
- Frames 32 and 33 retain the existing biowarfare and chemical-warfare pictograms, but their tile backgrounds now use the shared `gfx/interface/buildings/building_background.png` and their transparent edge pixels carry black RGB values.
- The correction removes the light gray or white edge glow produced when the game composites the facility frames over the construction panel.
- Frames 1-31 and 34-35 are payload-byte identical to the pre-correction runtime.

## Processing

The existing facility foreground pixels were selected with the warm-pixel seed `red - max(green, blue) >= 8` and `red >= 20`, then expanded by one pixel to retain the dark icon outline and shadow. The selected foreground was composited over the supplied 46x46 shared building tile. No facility icon was rescaled or recolored.

## Validation

- Final SHA-256: `c010949226860dd9820746c4ddb36cc89d2464ea9696d75682dae4520a1e175b`.
- DDS remains a `1610x46` legacy uncompressed BGRA strip with a 124-byte header and exact file length `296368` bytes.
- Frames 1-31 and 34-35 are byte-for-byte unchanged; only frames 32 and 33 differ.
- Neutral near-white pixels with nonzero alpha in frames 32 and 33: `0` in both corrected frames.
- Alpha extrema remain `0..255`.
- The candidate contact sheet and machine checks are retained in `docs/assets/system_camp_building_background_composite/evidence/facility_halo_inspection/`.

No `.gfx`, GUI, gameplay, localisation, standalone building texture, or frame-order changes were made. Live Hearts of Iron IV validation remains the user-owned gate.
