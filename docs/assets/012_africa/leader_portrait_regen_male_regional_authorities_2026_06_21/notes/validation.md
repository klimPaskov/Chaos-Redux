# Validation Notes

Date: `2026-06-21`

- Confirmed the seven replaced live DDS targets remain `156x210`.
- Manually reviewed the final processed PNG set and live DDS contact sheet. All seven selected portraits read as male-presenting adult human leaders.
- Checked that the set stays visually distinct by face, age, clothing, and backdrop across Congo Basin Charter, Great Lakes Council, Indian Ocean Congress, Maghreb Coast, Sahel Caravan, South African Liberation Congress, and Zambezi Stone Cities.
- Confirmed the package contains a source PNG, processed PNG, and final live DDS for each replaced portrait.
- The repo helper `.tools/convert_to_dds.py` failed in this environment because its ffmpeg fallback raised `struct.error: pack expected 34 items for packing (got 32)`. Live DDS replacements were written with ImageMagick using `-define dds:compression=none`, then verified with `identify` and `file`.
