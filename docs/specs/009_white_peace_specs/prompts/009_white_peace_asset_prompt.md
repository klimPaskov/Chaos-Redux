# Asset Prompt — Event 009 White Peace

Use `chaos-redux-event-assets` for all visual asset work. Route sourced real/archival images to `chaosx_asset_source_researcher`; route generated report/news images to `chaosx_generated_event_art`; route achievement icons to `chaosx_icon_artist`. Asset subagents must use `fork_context=false` if spawned by a parent agent.

## Event identity

- Event ID: `9`
- Event name: `White Peace`
- Cluster: Peace, cluster ID `4`
- Tone: restrained, quiet, diplomatic, no victor, no territorial change.

## Required assets

### 1. Report event image — White Peace

- Asset type: report event image
- Target size: `210x176`
- Suggested filename: `report_event_009_white_peace.dds`
- Suggested processed PNG: `report_event_009_white_peace.png`
- Suggested sprite: `GFX_report_event_009_white_peace`
- Suggested final folder: follow existing report-event image folder pattern.
- Source mode: generated period-documentary image unless a strong public-domain/source image is found.
- Reference folder to inspect first: `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- Required processing: report-event card treatment with `tools/process_report_event_image.py` if that tool exists in the repo.

Visual direction:

A 1936–1945 period documentary scene of a quiet armistice note being handled in a dim consular office or military radio room. Papers, typewriter, lamps, uniforms, and tired staff officers. No readable generated text. No modern props. No triumphal ceremony. The subject should feel like a peace no one celebrates.

Avoid:

- grand treaty halls;
- cheering crowds;
- modern conference rooms;
- readable fake text;
- flags that imply a specific real treaty unless sourced and intentional;
- map-first composition.

### 2. Optional Stage III news image

Create only if implementation adds a news popup for the broad settlement branch.

- Asset type: news event image
- Target size: `397x153`
- Suggested filename: `news_event_009_white_peace_circular.dds`
- Suggested sprite: `GFX_news_event_009_white_peace_circular`
- Source mode: generated period-news/documentary image or sourced archival telegraph/newsroom image.
- Reference folder: `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- Required final style: black-and-white.

Visual direction:

A period news image of telegram clerks, newspaper bundles, or a quiet border checkpoint as multiple armistice notices spread. The image should feel administrative and restrained.

### 3. Achievement icons

Use `chaosx_icon_artist`.

General achievement icon rules:

- Target size: `64x64`
- Source mode: generated icon art.
- Reference folder: `.agents/skills/chaos-redux-event-assets/assets/achievements`
- Create completed icon first.
- Grey and not-eligible variants can be generated/processed according to the achievement system pattern.

#### `achievement_white_peace_status_quo_ante`

- Title: Status Quo Ante
- Icon direction: two small flags facing each other over an unchanged border line, with a sealed paper between them. Restrained, diplomatic, no victory wreath.
- Suggested filename: `achievement_white_peace_status_quo_ante.dds`

#### `achievement_white_peace_no_winner`

- Title: No Winner, No Spoils
- Icon direction: a pair of empty hands lowering weapons beside a blank treaty page. Muted steel and parchment tones.
- Suggested filename: `achievement_white_peace_no_winner.dds`

#### `achievement_white_peace_chain_of_tables`

- Title: A Chain of Tables
- Icon direction: several small negotiation tables receding into shadow, each with a single lamp or paper stack. Readable at 64x64.
- Suggested filename: `achievement_white_peace_chain_of_tables.dds`

#### `achievement_white_peace_silence_of_giants`

- Title: Silence of Giants
- Icon direction: two large artillery silhouettes lowered under a single white document seal. The document, not the guns, should be the focal point.
- Suggested filename: `achievement_white_peace_silence_of_giants.dds`

#### `achievement_white_peace_the_circular`

- Title: The Circular Reaches Every Desk
- Icon direction: a circular stamp or telegraph ring over several small envelopes, implying many capitals receiving one message.
- Suggested filename: `achievement_white_peace_the_circular.dds`

## Animated assets

No animated assets are required for this event. Static presentation is intentional because the event should feel quiet and bureaucratic.

If a future Peace cluster interface is built, a subtle document-seal pulse or telegraph-line animation can be planned separately through `chaos-redux-frame-animation` with real source frames and static fallback.

## Manifest requirements

Create or update:

- `docs/assets/009_white_peace/manifest.md`
- `docs/assets/009_white_peace/gfx_handoff.md`

Each manifest entry must list:

- asset name;
- event ID;
- source mode;
- prompt or source URL;
- source path;
- processed PNG path;
- final DDS path;
- target size;
- sprite name;
- suggested `.gfx` file;
- intended in-game use;
- status;
- uncertainty if source/license/date is unclear.
