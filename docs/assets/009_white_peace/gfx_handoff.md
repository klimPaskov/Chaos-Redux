# GFX Handoff: Event 009 White Peace News Image

Final texture: `gfx/event_pictures/009_white_peace/news_event_009_white_peace.dds`.

Sprite name: `GFX_news_event_009_white_peace`.

Target registry: `interface/009_white_peace_event_images.gfx`; `GFX_news_event_009_white_peace` is now wired to the final DDS.

Texture canvas: Opaque `397x153` black-and-white news photograph.

Use: Global observer news event fired once after a successful AI-only settlement; the scene shows both armies turning back toward their existing lines across an unchanged rural checkpoint.

Source and processing evidence: `source_png/news_event_009_white_peace_source.png`, `prompts/news_event_009_white_peace.txt`, and `processed_png/news_event_009_white_peace.png`.

DDS round-trip evidence: `roundtrip/news_event_009_white_peace_dds_roundtrip.png` and `notes/dds_roundtrip.md`.

Manifest: `manifest.md`.

Integration: News events `.7` through `.10` consume this sprite and declare `major = yes` for observer broadcast. Native-size review by the Event 009 owner found no visual defect. No live news-window screenshot or MCP preview is available.
