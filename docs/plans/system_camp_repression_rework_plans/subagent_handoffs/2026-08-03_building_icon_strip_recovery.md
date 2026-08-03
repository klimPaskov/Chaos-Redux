# Building icon strip recovery

Status: complete.

The runtime strip had a full-payload rewrite in the later camp-art composite commits. The first 33 frames were recovered from the known-good `10619055c` asset, which preserves the installed vanilla frames 1-31 and the existing Chaos Redux facility frames 32-33. The accepted camp frames were then appended as frames 34-35 from the previously reviewed camp-art runtime.

## Runtime result

- Runtime: `gfx/interface/buildings/building_icon_strip.dds`.
- Dimensions: `1610x46`.
- Frame footprint: `46x46`.
- Frame count: `35`.
- Current SHA-256: `4dd03a739aba0e4e30d98b03dcd49e82eaaea2a1b1f9e00b3e2532049c953cb4`.
- Known-good recovery source SHA-256 (`10619055c`): `57480b03c2805e307ccdaf74e85ed76fbbe4cba841487be2beae947753163aa8`.
- Previous corrupted runtime SHA-256: `de2dc7538003b3966a64d4d8ad303e98ab4930a281cd60040bf01419e33bd1bf`.

## Frame ownership

- Frames 1-31: installed vanilla strip payload, byte-exact.
- Frames 32-33: recovered Chaos Redux biowarfare and chemical-warfare facility frames from `10619055c`.
- Frame 34: concentration-camp pictogram; also used by `gulag_labor_camp_network`.
- Frame 35: extermination-camp pictogram.

## Validation evidence

- Frames 1-33 are row-wise payload-byte exact against `10619055c`.
- Frames 1-31 are row-wise payload-byte exact against the installed vanilla strip.
- Frames 34-35 are byte-exact against the accepted camp-art frames in the preceding runtime strip.
- DDS header remains legacy uncompressed BGRA with magic `DDS `, header size `124`, pixel format flags `65`, BGRA masks `0x00FF0000/0x0000FF00/0x000000FF/0xFF000000`, `DDSCAPS_TEXTURE=0x1000`, and alpha extrema `0..255`.
- `interface/countrystateview.gfx` declares `GFX_buildings_strip` with `noOfFrames = 35`.
- `common/buildings/chaosx_buildings.txt` maps concentration and Gulag to frame 34 and extermination to frame 35.

No gameplay, GUI layout, localisation, or standalone camp DDS files were changed in this recovery. Live Hearts of Iron IV validation remains the user-owned gate.
