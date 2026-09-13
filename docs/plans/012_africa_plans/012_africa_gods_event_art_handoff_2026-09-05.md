# Event 012 Gods of Africa generated event-art handoff

Status: implemented asset production; current working-tree source wiring is evidenced, while live visual review, playback, and promotion remain pending.

Reconciliation note, 2026-09-05: the asset package itself changed no GFX or gameplay files, but the current parent working tree now contains the Event 012 report sprite declarations and decision-category picture consumers described below. This source evidence supersedes the narrower pending-wiring wording without constituting parent or user approval.

## Scope and source mode

This package covers the eight current Event 012 Gods report-event consumers and one static decision-category picture required by the accepted presentation specification. No elephant or 3D-model art was produced, and no icons, portraits, super-event art, gameplay, localisation, GUI, or GFX files were edited.

The source mode is `generated` through the built-in ImageGen tool. Generation fits because the Gods of Africa institution and its supernatural signs are fictional alternate-history material with no real archival scene to source. The prompts enforce 1936–1945 material culture, institutional rather than religious imagery, no readable text, no modern devices, no sacred-object collage, and no caricature or colonial stereotype.

ImageGen source outputs were copied from `C:\Users\klimp\.codex\generated_images\01a06e83-5d54-7893-85e9-29c0f3e29967\` into the event-scoped source folder. Prompt records are retained in `docs/assets/012_africa_gods_of_africa/prompts.md`.

## Runtime asset manifest

Report-event outputs were processed with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py`, yielding RGBA `210x176` sepia cards with transparent corners, then converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to one-level uncompressed BGRA DDS. The category picture was cover-fit resized with Pillow from its generated `1448x1086` RGB source to an opaque `114x101` RGB preview, then converted with the same repository converter.

| Asset | Source PNG dimensions and SHA-256 | Processed PNG dimensions and SHA-256 | Final DDS dimensions, bytes, SHA-256 | Runtime path and sprite |
| --- | --- | --- | --- | --- |
| Proclamation | `1536x1024`, `e9c4c245964d475bf1fd4d089f1767a925b3ead7fe7c1d771b85af99381633d4` | `210x176`, `9eb9858d4d31e02acff056542b0c16a5e1a3b30fcfd0119e0b099001d4140dd0` | `210x176`, `147968 B`, `8a712242fd1f39bdf1da32f5cfa42a98bfbe71207151c9946e89002560088ef8` | `gfx/event_pictures/012_africa/report_event_012_africa_gods_proclamation.dds`, `GFX_report_event_012_africa_gods_proclamation` |
| Introduction | `1536x1024`, `c85a164a2bb36e3195551a6f54b34b16de0ff30cbeee1e6e80a532464ed007b3` | `210x176`, `d5f476dc54d1a04406c65dc4c2b06142bf170ada54cea7de78fab9c7d1eec218` | `210x176`, `147968 B`, `c4068eb974489614c8b14f9a7fe50bddb1c34a4ae5dfcd83ee4d05b1cb40b9e2` | `gfx/event_pictures/012_africa/report_event_012_africa_gods_introduction.dds`, `GFX_report_event_012_africa_gods_introduction` |
| Demand | `1536x1024`, `603db74af37b6bf35b0499da44adb3e3d86f0d0e317ffbf37e29ba3fd491c944` | `210x176`, `f47b160e4fa4ca60c449e7ffc3157ba32aa71a22a45fb80ac9021207b09d871c` | `210x176`, `147968 B`, `643953a87bf0ad9143ef55e712ebafcabba78c1b1488f1bc61180eb05e64fede` | `gfx/event_pictures/012_africa/report_event_012_africa_gods_demand.dds`, `GFX_report_event_012_africa_gods_demand` |
| Response | `1536x1024`, `7db741aa319421f4d03ddfdfc44234688372fde0762d8703a3229b9dd1f996b6` | `210x176`, `e094f30a6ecd791601169fb6d01a73f2233833fccdbbd883e3071afdbeed8ab7` | `210x176`, `147968 B`, `23bfbd0fa2feb953c35f3b29aa8632043ca76fab8f886179d8588876b0145d9b` | `gfx/event_pictures/012_africa/report_event_012_africa_gods_response.dds`, `GFX_report_event_012_africa_gods_response` |
| Punishment | `1536x1024`, `628ff0992d482dc3adfc196455e6a9538cab7652a75cf5881a48f6383de96e4a` | `210x176`, `5d4cf7966e2448a18d8925e7f24c87c47188efa04b8ac3ef3cc9d5f302b203be` | `210x176`, `147968 B`, `46c2129c2b8dddfe5f8a94e61286437aeb9cc14ce55c9605fac4362c8c1319ff` | `gfx/event_pictures/012_africa/report_event_012_africa_gods_punishment.dds`, `GFX_report_event_012_africa_gods_punishment` |
| Settlement | `1536x1024`, `162ebac360458c6f777e24ca5f518d3c125c23eda9aad6a9706b6d0455c60fd1` | `210x176`, `9f864c6f17716c2d08241dbbed0de29e126c19dabf04306425f0720ee9b467d3` | `210x176`, `147968 B`, `c86a501cf54baa80e6cd00fc760f7d75f0c0236f1246f232b25eee5dffafeadd` | `gfx/event_pictures/012_africa/report_event_012_africa_gods_settlement.dds`, `GFX_report_event_012_africa_gods_settlement` |
| Defiance | `1536x1024`, `a3010906ae9de85de89ef0c95fd1b352d854723847c5e34b656c1607c6f76eff` | `210x176`, `968510a8e016ff593267811aefc40db9c2523f3297df5f5ea075d7c9e912d644` | `210x176`, `147968 B`, `905da9f3643f97215cfca183a792f11935b8e7e6c28a34175f3999c0b8d4ead` | `gfx/event_pictures/012_africa/report_event_012_africa_gods_defiance.dds`, `GFX_report_event_012_africa_gods_defiance` |
| Protection | `1536x1024`, `5ad6e1e8c18b0d28cafe5c3eddc6f73c7cda89e8f6566ecb1ac6e1102fff2e93` | `210x176`, `b0e7435b82bcb63c947470bfcc655ea6ee76b152cd63088cb585a23ec76fcbc5` | `210x176`, `147968 B`, `d4ff6eaae8af3811ea8b0094d12c47fb29afc0ae5d0a969ebf03ae4c97d28149` | `gfx/event_pictures/012_africa/report_event_012_africa_gods_protection.dds`, `GFX_report_event_012_africa_gods_protection` |
| Decision-category picture | `1448x1086`, `77f8b23c4619c56989a0db6dcdf339b4d097c147c433ec2404d311f5affbc8fb` | `114x101`, `8480b4889917f74acf4d2f2e26d6ca8a91559d2efbc8a05b01ba3f1a0b4bc751` | `114x101`, `46184 B`, `8d454bc66950a8a344699abf241c6bb3708b222000a15f05543c368623676066` | `gfx/interface/decisions/012_africa/decision_cat_picture_012_africa_gods.dds`, `GFX_decision_cat_picture_012_africa_gods` |

All report processed PNG corners decode as fully transparent while retaining nonzero subject alpha; the category picture is intentionally opaque. DDS validation found the expected legacy 128-byte header, dimensions, `width*4` pitch, exact payload length, and byte-for-byte BGRA payload equality against each processed PNG.

## Consumer crosswalk and parent wiring

The eight report sprites are consumed by `events/012_africa_gods_of_africa.txt` at `chaosx.nr12.601`, `.602`, `.603`, `.604`, `.605`, `.608`, `.609`, and `.610`, and their declarations are present in the current working-tree `interface/012_africa_event_pictures.gfx`.

The current working-tree `common/decisions/categories/012_africa_gods_categories.txt` contains `picture = GFX_decision_cat_picture_012_africa_gods` for both active categories. The category picture source and consumer wiring are therefore evidenced, while the choice to share it and live visual acceptance remain parent/user decisions.

The canonical reference families inspected were `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/event_art/report/contact_sheet.png` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/pictures/contact_sheet.png`. Report references establish the 210x176 sepia card treatment and category references establish the 114x101 institutional-picture family.

## Review and omissions

The review sheet is `docs/assets/012_africa_gods_of_africa/review/contact_sheet.png`. The family remains people-free at the category surface and uses people only as secondary figures in reports, with no portraits or sacred-object collage.

No requested asset is blocked. Super-event art, icons, portraits, elephant art, 3D models, GFX edits, and gameplay wiring remain outside this bounded handoff; current parent source wiring is evidence only, and the existing Event 012 super-event package remains untouched.
