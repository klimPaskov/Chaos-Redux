# DDS Round-Trip Evidence: Event 009 White Peace News Image

The repository-standard `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` converted `processed_png/news_event_009_white_peace.png` to `gfx/event_pictures/009_white_peace/news_event_009_white_peace.dds` at `397x153`.

The DDS has the expected `DDS ` magic, a 124-byte header, the pixel-format block at byte 76 with 32-bit BGRA masks, a texture capability flag, no mipmaps, and a total file size of `243092` bytes (`128 + 397 * 153 * 4`).

Decoded alpha extrema are `(255,255)`, matching the opaque full-canvas requirement.

The decoded BGRA image at `roundtrip/news_event_009_white_peace_dds_roundtrip.png` is pixel-identical to `processed_png/news_event_009_white_peace.png`.

Processed PNG SHA-256: `6A6C2389E7F26C1AEFE31D1E4E24651911D03EB1854165155A0474FABFC1DFF3`.

Runtime DDS SHA-256: `CC342B4AFEF77C62BD94D15FF157977A309205AD62487A380C014416B3346E85`.

Decoded round-trip PNG SHA-256: `9F5368F83EE88C56AC00B1399533C06E309FB3AA0882F62E072E62EB56B4F22E`.
