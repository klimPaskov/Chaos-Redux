# Independence Wave asset production prompt

Create the complete visual asset package for Chaos Redux Event 6, Independence Wave.

Read and apply:

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md` for every animated item
- the full Event 6 specification folder
- `matrices/006_asset_family_registry.csv`
- `matrices/006_candidate_country_registry.csv`
- `matrices/006_achievement_matrix.csv`

Event ID: `6`

Event slug: `independence_wave`

Working asset package path:

`docs/assets/006_independence_wave/`

Final event-scoped asset folders should use `006_independence_wave` directly under the relevant category folder.

## Required event presentation assets

Produce or hand off:

- wave summary report image, 210x176
- host crisis report image, 210x176
- first recognition report image, 210x176
- league congress news image, 397x153 and black and white
- league formation super-event image, 457x328
- dangerous coordinated revisionism super-event image, 457x328
- regional and signature-country report variants listed in the asset registry when implementation scope includes them

The two super-event scenes and most wave scenes are alternate history. Use generated period-authentic documentary or political scenes unless a scene must show a real person or actual historical artifact.

Do not make a map, border diagram, conference map table, or generic staff room the main subject. Show new governments, delegates, crowds, militia formations, ports, local institutions, public ceremonies, or armed political blocs.

## Core mechanic UI

Create the complete visual family for the Event 6 decision category and scripted GUI:

- category icon
- panel background
- five mechanic value icons
- former-host status card
- patron cards and influence markers
- league card and charter emblem
- formable seal
- progress bars
- selected, inactive, locked, warning, active, and completed states where needed
- clear static fallback for every animated element

Functional layout remains the main agent's responsibility. Generated UI art must not determine exact interactive geometry.

## Animated assets

Create real frame-by-frame packages for:

1. recognition seal progression
2. dependency warning pulse
3. league charter activation
4. formable eligibility seal

For each animation:

- write a brief and frame plan
- create or approve a static fallback first
- generate or source every meaningful visual frame separately
- normalize frames mechanically only
- create processed frames, horizontal sheet PNG, final sheet DDS, static PNG and DDS, preview GIF, and contact sheet
- record frame size, frame count, sheet size, FPS, loop behavior, anchor, `play_on_show` expectation, state trigger, and target GFX or GUI surface

Do not create final motion by translating, scaling, rotating, recoloring, blurring, changing opacity, or adding a scripted glow to one still image.

## Icon families

Create separate source art for each asset type.

### Focus icons, 94x86

Build coordinated families for:

- founding administration
- constitutional government
- popular councils
- traditional restoration
- military emergency
- patron client
- recognition diplomacy
- army integration
- infrastructure authority
- former-host settlement
- league congress
- regional formables
- high-chaos sovereignty
- country-specific ambition modules

### Idea icons, 64x64

Build staged families for:

- Improvised Government
- Unrecognized State
- Fragmented Command
- Unsettled Borders
- Patron Pressure
- Post-Release Instability
- League Membership
- country-specific founding identity

### Decision icons, 32x32

Build families for:

- recognition
- government construction
- army integration
- depot and border actions
- former-host negotiation
- patron aid
- patron balancing
- network aid
- league votes
- border arbitration
- formable proclamation
- integration missions

Do not resize focus art to satisfy idea or decision assets.

## Country flags and portraits

The candidate registry contains 206 initial packages. Do not bulk-generate all flags and portraits without package review.

For every package selected for implementation:

- preserve an existing registered base flag when appropriate
- source historical flags and historically attested symbols
- generate only fictional, alternate-history, ideology, route, or high-chaos variants
- produce normal, medium, and small HOI4 flag files
- validate orientation and TGA headers
- use sourced portraits for real leaders
- use generated portraits for fictional leaders and councils
- record apparent gender presentation for one-person fictional portraits
- require matching regional name pools and metadata
- use institutional names and collective portraits for councils and committees

All newly registered Event 6 country, formable, cosmetic, and route tags end in `X`.

## Achievement icons

Create completed 64x64 icons for all achievements in `matrices/006_achievement_matrix.csv`, then create the required grey and not-eligible variants through the approved achievement workflow.

Final achievement filenames must match final achievement IDs under `gfx/achievements/`.

## Reference inspection

Inspect the matching reference folders before creating each asset type:

- `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- `.agents/skills/chaos-redux-event-assets/assets/focuses`
- `.agents/skills/chaos-redux-event-assets/assets/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/achievements`
- `.agents/skills/chaos-redux-event-assets/assets/flags`

## Required outputs

- source PNG for every asset
- processed PNG preview
- final DDS or TGA as appropriate
- contact sheets
- `docs/assets/006_independence_wave/manifest.md`
- `docs/assets/006_independence_wave/gfx_handoff.md`
- prompts and source notes
- source URLs, authors, archives, dates, licenses, and uncertainty for sourced material
- final paths and proposed sprite names
- completed, blocked, and needs-review status for every requested item

Do not wire GFX or gameplay files unless the parent explicitly expands scope. Do not leave placeholder art and call the package complete.
