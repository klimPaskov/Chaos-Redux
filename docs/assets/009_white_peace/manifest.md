# Event 009 White Peace News Image Manifest

Asset: `news_event_009_white_peace`.

Requirement: Opaque, full-canvas `397x153` global news-event image for the alternate-history no-gain armistice, showing opposing armies lowering rifles and returning behind their established lines.

Source mode: `generated` with the built-in native ImageGen route.

Generation fit: The ceasefire and checkpoint scene are alternate history and have no authentic archival photograph; generated documentary staging provides the requested visual without claiming to depict a real event or identifiable person.

Selected source candidate: `source_png/news_event_009_white_peace_source.png`, copied from `C:/Users/klimp/.codex/generated_images/01a10d38-2a70-76c2-a7c2-9f4730e27149/exec-f6aa9284-523f-4b66-be65-9c0523258733.png`.

Source properties: RGB PNG, `2019x779`, with no alpha channel; SHA-256 `6D45B5D95C31F7F6AA86E7AD38C1C3A2C36F02CD59A523AB6A52FB44B9537481`.

Prompt: `prompts/news_event_009_white_peace.txt`.

Reference family: `.agents/skills/chaos-redux-event-assets/assets/gfx_references/event_art/news/`; reviewed its `contact_sheet.png` and `news_event_004.png` for the news-image canvas and restrained monochrome press-photo treatment. Reference art was not copied or used as an image input.

Processing: Center-fit to `397x153` with Lanczos resampling, convert to grayscale, apply `0.5%` autocontrast cutoff, then apply `1.04` contrast; the source's natural grain is retained without adding synthetic noise. The processed PNG is RGB and fully opaque.

Processed preview: `processed_png/news_event_009_white_peace.png`, `397x153`, SHA-256 `6A6C2389E7F26C1AEFE31D1E4E24651911D03EB1854165155A0474FABFC1DFF3`.

Runtime DDS: `gfx/event_pictures/009_white_peace/news_event_009_white_peace.dds`, SHA-256 `CC342B4AFEF77C62BD94D15FF157977A309205AD62487A380C014416B3346E85`.

Round-trip evidence: `roundtrip/news_event_009_white_peace_dds_roundtrip.png` and `notes/dds_roundtrip.md`; decoded BGRA pixels equal the processed PNG exactly, and alpha is fully opaque `(255,255)`.

Registration: Sprite `GFX_news_event_009_white_peace` is wired in `interface/009_white_peace_event_images.gfx` to the final DDS. News events `chaosx.nr9.7` through `.10` consume this sprite and use `major = yes` for observer broadcast. The unmarked scene is used for minor, major, and aggregate no-gain outcomes.

Contact sheet: Not required for this single requested image with no retained alternatives; the news-image contact-sheet rule applies to packages containing many images.

Status: Generated, processed, converted, and wired. The Event 009 owner reviewed the native-size preview and found no visual defect. Live event-window presentation and root-parent review remain unverified. The repository root `.gitignore` excludes `docs/assets/`; the package is available in the shared workspace but will not appear in ordinary `git status` unless selected files are force-added.
