# Validation evidence

The source image is a generated fictional alternate-history documentary scene and is retained unchanged in `source_png/`.

The report-card processor produced an RGBA `210x176` preview. Its alpha extrema are `0..255`, with transparent corners and a soft shadow. Visual inspection confirms the scene remains readable at native report-card scale and retains the covered lamps, ration table, memorial ribbons, civilians, unmarked guards, and empty sky.

The repository DDS converter produced a one-level uncompressed BGRA DDS at the requested runtime path. Header checks recorded `DDS ` magic, `DDS_HEADER` size `124`, dimensions `210x176`, `DDS_PIXELFORMAT` size `32`, flags `65`, fourCC `0`, 32-bit masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`, texture caps `0x1000`, exact length `147968` bytes, and alpha bytes `0..255`.

No `.gfx`, gameplay, localisation, workbook, or unrelated files were edited. No HOI4 run was performed.
