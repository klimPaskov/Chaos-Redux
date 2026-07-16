# Event 006 Rhineland and Bavaria unique visual assets

- Package date: 2026-07-16
- Event cluster: 006 Independence Wave
- Packages: IW-008 Rhineland and IW-009 Bavaria
- Asset count: 26 final assets (16 focus icons, 8 route-institution idea icons, 2 report-event pictures)
- Source mode: OpenAI ImageGen built-in tool
- Runtime registration owner: main agent via `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Asset-production scope: source art, transparent/period processing, DDS conversion, contact sheets, hashes, validation, and sprite handoff only
- Simplifications or fallbacks: none. No placeholder, copied, recolored, or focus-derived idea art was used.

## Reference basis and visual review

The package was produced after inspecting the canonical Chaos Redux asset-reference library and its Vanilla HOI4 national-focus, idea, and report-event contact sheets and catalog entries. Focus icons use detailed transparent heraldic/institutional compositions at 94x86; idea icons use separately generated compact spirit compositions at 64x64; report images use fictional period-documentary source scenes followed by the standard tilted sepia report-card treatment at 210x176.

Review sheets:

- `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/contact_sheets/focus_rhi_contact_sheet.png`
- `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/contact_sheets/focus_bay_contact_sheet.png`
- `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/contact_sheets/idea_rhi_contact_sheet.png`
- `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/contact_sheets/idea_bay_contact_sheet.png`
- `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/contact_sheets/report_incidents_contact_sheet.png`

Both the producing agent and parent agent reviewed all five sheets and passed every asset for silhouette separation, final-size readability, clean transparency, and period coherence.

## Exact processing command sets

All commands were run from the mod root.

### Chroma-key extraction for all icons

```powershell
$package = 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16'
$helper = 'C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py'
foreach ($kind in @('focus','idea')) {
  $outDir = Join-Path $package "processed_png/_alpha_masters/$kind"
  Get-ChildItem -LiteralPath (Join-Path $package "source_png/$kind") -Filter '*.png' | Sort-Object Name | ForEach-Object {
    $out = Join-Path $outDir $_.Name
    python -B $helper --input $_.FullName --out $out --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill
  }
}
```

### FOCUS-ICON and IDEA-ICON normalization

```powershell
$pipeline = 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/tools/asset_pipeline.py'
python -B $pipeline icons --kind focus --input-dir 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/_alpha_masters/focus' --output-dir 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus'
python -B $pipeline icons --kind idea --input-dir 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/_alpha_masters/idea' --output-dir 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea'
```

### REPORT-RHI and REPORT-BAY treatment

```powershell
python -B '.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py' 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/report/report_event_006_rhi_corridor_incidents.png' 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/report/report_event_006_rhi_corridor_incidents.png' --angle 2.4 --seed 6008
python -B '.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py' 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/report/report_event_006_bay_state_incidents.png' 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/report/report_event_006_bay_state_incidents.png' --angle -2.0 --seed 6009
```

### DDS conversion

```powershell
$converter = '.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py'
# Focus assets
Get-ChildItem 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/*.png' | ForEach-Object { python -B $converter --input $_.FullName --output (Join-Path 'gfx/interface/goals/006_independence_wave/rhineland_bavaria' ($_.BaseName + '.dds')) --width 94 --height 86 }
# Idea assets
Get-ChildItem 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/*.png' | ForEach-Object { python -B $converter --input $_.FullName --output (Join-Path 'gfx/interface/ideas/006_independence_wave/rhineland_bavaria' ($_.BaseName + '.dds')) --width 64 --height 64 }
# Report assets
Get-ChildItem 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/report/*.png' | ForEach-Object { python -B $converter --input $_.FullName --output (Join-Path 'gfx/event_pictures/006_independence_wave/rhineland_bavaria' ($_.BaseName + '.dds')) --width 210 --height 176 }
```

### Validation

```powershell
python -B 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/tools/asset_pipeline.py' validate --package-root 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16' --mod-root . --output 'docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/validation/asset_validation.json'
```

## Validation result

- Expected and actual counts match: 26 source PNGs, 26 processed PNGs, and 26 runtime DDS files.
- All 26 DDS files pass legacy uncompressed BGRA header, 32-bit pixel-format flags and masks, DDSCAPS_TEXTURE, exact-length, dimension, and alpha checks.
- Runtime dimensions: 16 at 94x86, 8 at 64x64, and 2 at 210x176.
- All 26 DDS files decode pixel-identically to their processed PNGs.
- Every processed asset has transparent corners and a 0-255 alpha range.
- All 26 source PNG SHA-256 hashes are unique; minimum pairwise 16x16 RGB average-hash distance is 21.
- Detailed evidence: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/validation/asset_validation.json`.

## Asset entries

### 1. `goal_independence_wave_rhi_establish_corridor_authority`

- Asset type: National focus icon
- Related consumer: `independence_wave_rhi_establish_corridor_authority_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_rhi_establish_corridor_authority`; shine: `GFX_goal_independence_wave_rhi_establish_corridor_authority_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_rhi_establish_corridor_authority.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_rhi_establish_corridor_authority.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_rhi_establish_corridor_authority.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_establish_corridor_authority.dds`
- SHA-256 source: `222816b4b11770e56d328152795d15d2f5c19bd93264a2f6c8c4f17c99c6facb`
- SHA-256 processed: `facd0415a538f1a768bd8655645054e48f79f32c688d1f19533cdd22a7856e3b`
- SHA-256 DDS: `6417049c9e8372ecb13a4dfd69e1bb6c6610a87d4d4438e2662f3968dd005baa`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Rhenish corridor-authority emblem: a rolled civic river charter crossed by a stylized silver-blue Rhine current, secured with a substantial bronze wax seal and a small river-gate lintel
Style/medium: compact painterly late-1930s grand-strategy game icon, aged metal and parchment, restrained heraldic treatment, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered emblem cluster occupying about 76% of the square canvas, balanced silhouette, all details large enough to survive reduction, generous clear padding
Lighting/mood: sober institutional authority, restrained highlights, deep charcoal edge shading
Color palette: slate blue, river teal, aged brass, warm parchment, charcoal; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; no text, letters, numbers, logos, flags, watermark, readable seal inscription, white rim, glow, sticker border, opaque medallion disk, rectangular frame, extra objects, modern design, or background scene
```

### 2. `goal_independence_wave_rhi_unify_rail_dispatch`

- Asset type: National focus icon
- Related consumer: `independence_wave_rhi_unify_rail_dispatch_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_rhi_unify_rail_dispatch`; shine: `GFX_goal_independence_wave_rhi_unify_rail_dispatch_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_rhi_unify_rail_dispatch.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_rhi_unify_rail_dispatch.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_rhi_unify_rail_dispatch.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_unify_rail_dispatch.dds`
- SHA-256 source: `1b228b8f4935684d7432252e1bba7434d063e2c7d0249311d3939370552c7d73`
- SHA-256 processed: `ea58137dd9615fa036b06673a695942b3511ad1ef12fadab478357e21662705a`
- SHA-256 DDS: `3967f66dc0fce8f0fe87ddea39fc40f3fb13cb68f93c901f1dc42a5b7a5c6430`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Rhenish rail-dispatch emblem: a tall mechanical semaphore signal above a heavy freight locomotive wheel, with a low Rhine cargo barge prow and one broad river wave integrated beneath it
Style/medium: compact painterly late-1930s grand-strategy game icon, aged steel, brass and painted enamel, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered vertical emblem cluster occupying about 76% of the square canvas; semaphore is the highest point, wheel is the visual anchor, barge and wave remain bold at small size; generous clear padding
Lighting/mood: disciplined transport coordination, cool industrial highlights and deep charcoal edge shading
Color palette: signal red and cream accents, gunmetal, aged brass, dark Rhine blue; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; no text, letters, numbers, logos, flags, watermark, readable placards, white rim, glow, sticker border, opaque medallion disk, rectangular frame, extra trains, modern equipment, or background scene
```

### 3. `goal_independence_wave_rhi_arm_customs_guard`

- Asset type: National focus icon
- Related consumer: `independence_wave_rhi_arm_customs_guard_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_rhi_arm_customs_guard`; shine: `GFX_goal_independence_wave_rhi_arm_customs_guard_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_rhi_arm_customs_guard.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_rhi_arm_customs_guard.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_rhi_arm_customs_guard.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_arm_customs_guard.dds`
- SHA-256 source: `bf0b03fbf0183967449ae780c93c64bf972a0e0b75da25e979605d809b688de9`
- SHA-256 processed: `237a6ed6da085f8141d1b66f605aed0a0fa80491e040288a33578e39b8004061`
- SHA-256 DDS: `94030ed95a7739829627bf30581b7bbc8fca8158ca2bad5f5b40cca52b143593`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Rhenish customs-guard emblem: a thick dark-blue customs shield in front of a fortified river-gate arch with raised portcullis teeth, crossed behind by one inspection staff and one compact 1930s guard carbine
Style/medium: compact painterly late-1930s grand-strategy game icon, aged steel, blued metal and brass, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered shield-led emblem occupying about 76% of the square canvas, gate arch readable around the shield, crossed tools create a strong X silhouette, generous clear padding
Lighting/mood: alert border control, restrained cold highlights and deep charcoal edge shading
Color palette: midnight blue, river teal accents, iron grey, muted brass, dark wood; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; no text, letters, numbers, logos, flags, watermark, heraldic eagle, white rim, glow, sticker border, opaque medallion disk, rectangular frame, modern firearm, people, or background scene
```

### 4. `goal_independence_wave_rhi_secure_industrial_belt`

- Asset type: National focus icon
- Related consumer: `independence_wave_rhi_secure_industrial_belt_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_rhi_secure_industrial_belt`; shine: `GFX_goal_independence_wave_rhi_secure_industrial_belt_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_rhi_secure_industrial_belt.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_rhi_secure_industrial_belt.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_rhi_secure_industrial_belt.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_secure_industrial_belt.dds`
- SHA-256 source: `d1c584034631f9711345aa6f38e01e503f2083c7a57e042c6fd9d0b904d2d4cc`
- SHA-256 processed: `aba81c7816e756b442b97d1f7d39b6655c5512355f507a00cb2af3d57f1f5116`
- SHA-256 DDS: `59c2b0b451bdc167ee2f930a52c59f7b87bbabaf00120878c9779fa0227035b0`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Rhenish industrial-belt emblem: two compact steelworks furnace towers with a glowing pour at center, rising from a broad toothed gear whose lower arc becomes a dark blue Rhine current
Style/medium: compact painterly late-1930s grand-strategy game icon, soot-darkened steel, aged brass and controlled furnace glow, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered industrial emblem occupying about 78% of the square canvas; furnace towers form a readable crown, gear dominates the lower half, river arc remains unmistakable at small size; generous clear padding
Lighting/mood: productive industrial resolve, warm furnace core against cool river steel, deep charcoal outline
Color palette: gunmetal, soot black, rusted brass, muted orange furnace light, dark Rhine blue; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; tightly contained internal glow only; no text, letters, numbers, logos, flags, watermark, white rim, external glow, sticker border, opaque medallion disk, rectangular frame, smoke cloud extending into the background, modern factory, people, or background scene
```

### 5. `goal_independence_wave_rhi_ratify_host_transit_compact`

- Asset type: National focus icon
- Related consumer: `independence_wave_rhi_ratify_host_transit_compact_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_rhi_ratify_host_transit_compact`; shine: `GFX_goal_independence_wave_rhi_ratify_host_transit_compact_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_rhi_ratify_host_transit_compact.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_rhi_ratify_host_transit_compact.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_rhi_ratify_host_transit_compact.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_ratify_host_transit_compact.dds`
- SHA-256 source: `cd9d080c8c613809cfc9f15af0a8bab9b6fe842d877145089bc7475cf700da88`
- SHA-256 processed: `c7d81ce7529149fa634e6bad8fb74ac57878365eedfaa91b32158692c143171e`
- SHA-256 DDS: `8e49b493acdc9e140b898b5f2d66a8bb6aa300f52f5024482c95dfaf233091d8`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Rhenish transit-compact emblem: a signed treaty parchment laid beneath a stout steel-and-stone bridge span, with two different wax seals joined by a short blue ribbon and a period fountain pen
Style/medium: compact painterly late-1930s grand-strategy game icon, aged parchment, steel, stone and wax, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered horizontal emblem occupying about 78% of the square canvas; bridge crowns the composition, parchment and two seals are bold below, pen forms a clean diagonal; generous clear padding
Lighting/mood: cautious negotiated settlement, dignified warm highlights and deep charcoal edge shading
Color palette: warm parchment, slate steel, weathered stone, burgundy and blue wax, muted brass; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; parchment must contain no readable writing; no text, letters, numbers, logos, flags, watermark, white rim, glow, sticker border, opaque medallion disk, rectangular frame, hands, people, or background scene
```

### 6. `goal_independence_wave_rhi_proclaim_neutral_corridor`

- Asset type: National focus icon
- Related consumer: `independence_wave_rhi_proclaim_neutral_corridor_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_rhi_proclaim_neutral_corridor`; shine: `GFX_goal_independence_wave_rhi_proclaim_neutral_corridor_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_rhi_proclaim_neutral_corridor.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_rhi_proclaim_neutral_corridor.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_rhi_proclaim_neutral_corridor.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_proclaim_neutral_corridor.dds`
- SHA-256 source: `dfca27919cba5e5506f2f365a08a9a4e70f71fa479540a3dce7ef113e1559e4b`
- SHA-256 processed: `e860d57a8f2bdca202edc1f605a4122ccc6350960e4a72fbf95811ff6f2a1b7d`
- SHA-256 DDS: `4b3ce2d89dd788703239eb8d84fc385f7af4eb36dc5840dfc3e8e34f612992ea`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Rhenish neutral-corridor emblem: perfectly balanced bronze scales suspended above a broad dark-blue river channel, flanked by two upright guarded bridge pylons bearing plain closed shields
Style/medium: compact painterly late-1930s grand-strategy game icon, aged bronze, stone and enamel, restrained civic heraldry, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered symmetrical emblem occupying about 76% of the square canvas; scale beam is broad and readable, river forms a bold lower arc, pylons and shields frame the sides; generous clear padding
Lighting/mood: watchful neutrality and controlled passage, cool sober highlights with deep charcoal edge shading
Color palette: dark river blue, weathered bronze, pale stone, steel grey, small cream accents; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; scale pans must be level; no text, letters, numbers, logos, flags, watermark, weapons, people, white rim, glow, sticker border, opaque medallion disk, rectangular frame, or background scene
```

### 7. `goal_independence_wave_rhi_charter_network_transit_office`

- Asset type: National focus icon
- Related consumer: `independence_wave_rhi_charter_network_transit_office_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_rhi_charter_network_transit_office`; shine: `GFX_goal_independence_wave_rhi_charter_network_transit_office_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_rhi_charter_network_transit_office.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_rhi_charter_network_transit_office.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_rhi_charter_network_transit_office.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_charter_network_transit_office.dds`
- SHA-256 source: `99c4894dda14813d9140f218e24c42c685eca7471757827efe9f94821ca10d18`
- SHA-256 processed: `f55fd63cb68f481dfc5c925f70c22872d9c4a97b8497b7b4e4d1b4291f552d56`
- SHA-256 DDS: `64b9127b07c11b12eb362123f55006e1e6ed8b4d1b6a8bcb47b33c83497dec7b`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: replacement source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Rhenish network-transit-office emblem: a robust 1930s brass telegraph key and paired ceramic insulators at center, crossed by three thick branching blue freight-route bands that end in a plain rail wheel, a plain river barge hook, and a plain warehouse roof-and-door silhouette
Style/medium: compact painterly late-1930s grand-strategy game icon, aged brass, dark steel, ceramic and painted enamel, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered radial emblem occupying about 76% of the square canvas; telegraph key remains the focal point, route bands are thick and legible, three freight endpoints form a clear triangular silhouette; generous clear padding
Lighting/mood: precise network coordination, restrained brass highlights and deep charcoal edge shading
Color palette: aged brass, charcoal steel, dark Rhine blue, ceramic cream, warm wood; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; every surface must remain completely unmarked; no text, letters, numerals, tally marks, logos, flags, watermark, modern electronics, map background, labels, medallions, badges, white rim, glow, sticker border, opaque disk, rectangular frame, people, or background scene
```

### 8. `goal_independence_wave_rhi_authorize_form04_delegation`

- Asset type: National focus icon
- Related consumer: `independence_wave_rhi_authorize_form04_delegation_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_rhi_authorize_form04_delegation`; shine: `GFX_goal_independence_wave_rhi_authorize_form04_delegation_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_rhi_authorize_form04_delegation.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_rhi_authorize_form04_delegation.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_rhi_authorize_form04_delegation.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_rhi_authorize_form04_delegation.dds`
- SHA-256 source: `f0336b4cadf5df6f550a5ff466d2e840121187cce078f3e47b7e6710cebd3f84`
- SHA-256 processed: `7f9551e48eb22a66550d89dcf5f9b811fa46792ff68b20f930e8f0cc6214410e`
- SHA-256 DDS: `f3d89ac9b7c41050a93acfc7486a2410208bed088af292f864d6507adf530235`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Rhenish League delegation emblem: an open charter scroll rising above a sweeping blue river ribbon, encircled by four distinct small river-city wax seals showing simple bridge, tower, gear, and anchor motifs
Style/medium: compact painterly late-1930s grand-strategy game icon, aged parchment, wax, brass and enamel, civic league heraldry, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered ceremonial emblem occupying about 78% of the square canvas; open charter is the tall focal point, river ribbon forms the base, four large seals make a readable wreath without crowding; generous clear padding
Lighting/mood: formal regional authorization and civic solidarity, dignified warm highlights with deep charcoal edge shading
Color palette: warm parchment, dark Rhine blue, burgundy wax, aged brass, muted teal and cream; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; charter contains no readable writing; no text, letters, numbers, logos, national flags, watermark, white rim, glow, sticker border, opaque medallion disk, rectangular frame, hands, people, or background scene
```

### 9. `goal_independence_wave_bay_broker_civic_settlement`

- Asset type: National focus icon
- Related consumer: `independence_wave_bay_broker_civic_settlement_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_bay_broker_civic_settlement`; shine: `GFX_goal_independence_wave_bay_broker_civic_settlement_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_bay_broker_civic_settlement.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_bay_broker_civic_settlement.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_bay_broker_civic_settlement.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_broker_civic_settlement.dds`
- SHA-256 source: `77dd09746bba925fdb3f8d3a8ed0febfc8c9e99c217392f9fc580c7562f19cef`
- SHA-256 processed: `8d18a5495f0be87ff8c8fce2a2b843911708853026df1064df8e1523eb9575c5`
- SHA-256 DDS: `27fd2c6136329bd62bbca0d45097e582b87c965ee36594b5b81e939c3108893b`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Bavarian civic-settlement emblem: a restrained stone town-hall facade with clockless central pediment, backed by a large blue-and-white lozenge-pattern civic wax seal and a modest joined-hands clasp beneath
Style/medium: compact painterly late-1930s grand-strategy game icon, aged stone, wax and enamel, restrained Bavarian civic heraldry, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered triangular emblem occupying about 76% of the square canvas; town hall is the architectural anchor, blue-white seal is clearly visible behind it, joined hands remain broad and readable below; generous clear padding
Lighting/mood: practical civic reconciliation, cool daylight highlights and deep charcoal edge shading
Color palette: Bavarian cobalt and white, pale weathered stone, muted brass, warm skin-neutral painted hands, charcoal; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; no readable clock face, text, letters, numbers, logos, flags, royal crown, watermark, white rim, glow, sticker border, opaque medallion disk, rectangular frame, full people, or background scene
```

### 10. `goal_independence_wave_bay_reconcile_landesbank_accounts`

- Asset type: National focus icon
- Related consumer: `independence_wave_bay_reconcile_landesbank_accounts_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_bay_reconcile_landesbank_accounts`; shine: `GFX_goal_independence_wave_bay_reconcile_landesbank_accounts_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_bay_reconcile_landesbank_accounts.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_bay_reconcile_landesbank_accounts.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_bay_reconcile_landesbank_accounts.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_reconcile_landesbank_accounts.dds`
- SHA-256 source: `9bac40db73df1a066fc009d9d84cbca5b6e0a760365b66ccf792fa5c2e771a67`
- SHA-256 processed: `be3e9455ac46e0674e99ba553e141b35450472053be34ccad9f24efe5da463b0`
- SHA-256 DDS: `78ad51ad02e4d14e7e1b20638ccb83931f46bdeb61f0c632a893ba5c7bfc591c`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Bavarian Landesbank-reconciliation emblem: an open ruled accounting ledger with blank pages in front of a heavy circular bank-vault door, accompanied by a brass counting wheel and one blue wax audit seal bearing only a simple check-shaped notch
Style/medium: compact painterly late-1930s grand-strategy game icon, aged paper, steel, brass and wax, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered emblem occupying about 76% of the square canvas; vault wheel is the high circular anchor, ledger spreads boldly across the lower half, audit seal remains large and readable; generous clear padding
Lighting/mood: sober financial settlement and restored solvency, cool steel highlights with restrained warm paper tones and deep charcoal edge shading
Color palette: Bavarian cobalt, ivory paper, gunmetal, aged brass, charcoal; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; ledger pages and seal contain no writing, numbers, letters, currency signs or inscriptions; no text, logos, flags, crown, watermark, white rim, glow, sticker border, opaque medallion disk, rectangular frame, people, or background scene
```

### 11. `goal_independence_wave_bay_bind_rail_and_pass_authorities`

- Asset type: National focus icon
- Related consumer: `independence_wave_bay_bind_rail_and_pass_authorities_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_bay_bind_rail_and_pass_authorities`; shine: `GFX_goal_independence_wave_bay_bind_rail_and_pass_authorities_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_bay_bind_rail_and_pass_authorities.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_bay_bind_rail_and_pass_authorities.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_bay_bind_rail_and_pass_authorities.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_bind_rail_and_pass_authorities.dds`
- SHA-256 source: `1f32e57ad7f889d85b8a22b2285c125dfefdd73e20505ee48a81241dbc2b6ff3`
- SHA-256 processed: `f695bca18a8315a63e2f1b510f82e3c31f5cc5127745790ffef2221995fccf5c`
- SHA-256 DDS: `dde543ba8879dcc1c12b29fa9be1315e9a68f81a1803d28d1047ca08bff006a1`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Bavarian rail-and-pass-authority emblem: a bold steel railway wheel and short track climbing through a stone alpine pass arch, framed by two snow-tipped mountain peaks and a compact mechanical signal lever
Style/medium: compact painterly late-1930s grand-strategy game icon, aged steel, stone and painted enamel, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered upward-moving emblem occupying about 76% of the square canvas; railway wheel anchors the foreground, rails lead through the pass arch, peaks form a distinctive crown, signal lever stays readable; generous clear padding
Lighting/mood: controlled alpine transit and hard infrastructure, crisp cold highlights with deep charcoal edge shading
Color palette: gunmetal, slate stone, snow ivory, Bavarian blue enamel, muted red signal accent; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; no text, letters, numbers, logos, flags, crown, watermark, modern train, people, white rim, glow, sticker border, opaque medallion disk, rectangular frame, or background scene
```

### 12. `goal_independence_wave_bay_seat_landtag_and_court`

- Asset type: National focus icon
- Related consumer: `independence_wave_bay_seat_landtag_and_court_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_bay_seat_landtag_and_court`; shine: `GFX_goal_independence_wave_bay_seat_landtag_and_court_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_bay_seat_landtag_and_court.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_bay_seat_landtag_and_court.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_bay_seat_landtag_and_court.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_seat_landtag_and_court.dds`
- SHA-256 source: `6c46846b5cbbdc16f5935a07c1fc9c7079f64521eff7b6fa7c5030344bccc283`
- SHA-256 processed: `2d140f619634c2c7032e57da63b1d17aa45098d56f0419e587e3ebfc8639d7f5`
- SHA-256 DDS: `dbe6d0241c24ab30d2eb31c52fb1a82223aed20fa7d1dfe5a5eec2c2292ff4d1`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Bavarian Landtag-and-court emblem: a compact semicircle of dark wooden assembly benches behind a closed civic lawbook, with a small restrained open crown resting low on the book and a plain judicial column at each side
Style/medium: compact painterly late-1930s grand-strategy game icon, aged wood, leather, stone and subdued gilt, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered symmetrical emblem occupying about 76% of the square canvas; assembly semicircle is unmistakable, lawbook is the lower anchor, crown is modest rather than dominant, columns frame the sides; generous clear padding
Lighting/mood: constitutional restraint and formal deliberation, dignified warm highlights with deep charcoal edge shading
Color palette: dark walnut, Bavarian blue leather, pale stone, subdued antique gold, cream; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; book contains no writing or emblems; crown must be small and simple; no text, letters, numbers, logos, flags, watermark, judge gavel, people, white rim, glow, sticker border, opaque medallion disk, rectangular frame, or background scene
```

### 13. `goal_independence_wave_bay_entrust_mountain_guardians`

- Asset type: National focus icon
- Related consumer: `independence_wave_bay_entrust_mountain_guardians_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_bay_entrust_mountain_guardians`; shine: `GFX_goal_independence_wave_bay_entrust_mountain_guardians_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_bay_entrust_mountain_guardians.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_bay_entrust_mountain_guardians.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_bay_entrust_mountain_guardians.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_entrust_mountain_guardians.dds`
- SHA-256 source: `257d20fee8deade577a2e394abb000eb7b38ed56554bbbf55f6db2a23937061d`
- SHA-256 processed: `c004655d65d83a1c2f35995d7dcbca6ddb2c1b0706051fc0e11caa5492268bea`
- SHA-256 DDS: `95afec5707366b1965c171502ef3a915c7b1942d5609baf8ed02db2a13dbdfc3`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Bavarian mountain-guardians emblem: a broad cobalt alpine shield bearing a high snow peak and stone watchtower, crossed behind by two traditional mountain staffs with metal tips, with a short fir bough at the base
Style/medium: compact painterly late-1930s grand-strategy game icon, aged enamel, stone, wood and steel, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered shield-led emblem occupying about 76% of the square canvas; peak and tower are bold inside the shield, crossed staffs create a strong silhouette, fir bough remains simple; generous clear padding
Lighting/mood: vigilant local defense and mountain endurance, cold alpine highlights with deep charcoal edge shading
Color palette: Bavarian cobalt, snow ivory, slate grey, dark fir green, weathered wood and steel; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; no text, letters, numbers, logos, flags, crown, watermark, firearms, people, white rim, glow, sticker border, opaque medallion disk, rectangular frame, or background scene
```

### 14. `goal_independence_wave_bay_open_alpine_network_office`

- Asset type: National focus icon
- Related consumer: `independence_wave_bay_open_alpine_network_office_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_bay_open_alpine_network_office`; shine: `GFX_goal_independence_wave_bay_open_alpine_network_office_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_bay_open_alpine_network_office.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_bay_open_alpine_network_office.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_bay_open_alpine_network_office.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_open_alpine_network_office.dds`
- SHA-256 source: `3fc8618aff5ba6d740dfd7aabe7c6ae422ddf33b5f86731efa820fcf11c7c525`
- SHA-256 processed: `5c92dd113686f170fb9421fa2b03e9db2e3f3a9253e9a0c6f851eda93ffc5499`
- SHA-256 DDS: `e5c4ba5e7fe50a86021f864d65c019632a8e5c6b8d8cb43fe18ab6d9fef95baf`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original Bavarian alpine-network-office emblem: a three-insulator 1930s telegraph crossarm spanning two snow peaks, with a compact freight wagon wheel and hooked cargo sling joined beneath by thick blue route cables
Style/medium: compact painterly late-1930s grand-strategy game icon, aged steel, ceramic, rope and painted enamel, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered wide emblem occupying about 76% of the square canvas; telegraph crossarm crowns the image, peaks remain visible, freight wheel and cargo hook form two bold lower anchors joined by route cables; generous clear padding
Lighting/mood: practical mountain communications and freight coordination, crisp cold highlights with deep charcoal edge shading
Color palette: Bavarian cobalt, snow ivory, gunmetal, ceramic cream, dark rope and muted brass; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; no text, letters, numbers, logos, flags, crown, watermark, modern antenna, full train, people, white rim, glow, sticker border, opaque medallion disk, rectangular frame, or background scene
```

### 15. `goal_independence_wave_bay_convene_south_german_settlement`

- Asset type: National focus icon
- Related consumer: `independence_wave_bay_convene_south_german_settlement_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_bay_convene_south_german_settlement`; shine: `GFX_goal_independence_wave_bay_convene_south_german_settlement_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_bay_convene_south_german_settlement.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_bay_convene_south_german_settlement.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_bay_convene_south_german_settlement.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_convene_south_german_settlement.dds`
- SHA-256 source: `7cc910b4812f78e4da8274899566203aa667aac2c67709acc9d3c5e856cc54af`
- SHA-256 processed: `be795519f1bc7782c1f161bec8f8ff0f20c6d6a808712224b17a2b7b80078f1f`
- SHA-256 DDS: `7b1dfaaa7eba1c04e9e9e547a3bb98cfd7b46645d6040646c771b354d673a4a4`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original South German settlement emblem: a compact round wooden treaty table viewed slightly from above, holding one blank parchment and fountain pen, surrounded by three large distinct blue-and-white regional wax seals and three restrained empty chair backs
Style/medium: compact painterly late-1930s grand-strategy game icon, aged wood, parchment, wax and brass, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered circular emblem occupying about 76% of the square canvas; table edge is the silhouette, parchment is clear at center, three seals form a readable triangle, chair backs remain secondary; generous clear padding
Lighting/mood: deliberate regional negotiation, warm tabletop light with cool blue-white accents and deep charcoal edge shading
Color palette: Bavarian cobalt and ivory, dark walnut, warm parchment, subdued brass, one slate-blue seal variation; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; parchment and seals contain no writing, numerals, letters or recognizable national emblems; no text, logos, flags, crown, watermark, people, white rim, glow, sticker border, opaque medallion disk, rectangular frame, or background scene
```

### 16. `goal_independence_wave_bay_ratify_german_host_compact`

- Asset type: National focus icon
- Related consumer: `independence_wave_bay_ratify_german_host_compact_focus`
- Intended sprite name(s): `GFX_goal_independence_wave_bay_ratify_german_host_compact`; shine: `GFX_goal_independence_wave_bay_ratify_german_host_compact_shine`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 94x86 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/focus/goal_independence_wave_bay_ratify_german_host_compact.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/focus/goal_independence_wave_bay_ratify_german_host_compact.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/focus/goal_independence_wave_bay_ratify_german_host_compact.png`
- Runtime DDS: `gfx/interface/goals/006_independence_wave/rhineland_bavaria/goal_independence_wave_bay_ratify_german_host_compact.dds`
- SHA-256 source: `1640694f193835573f888af39cf11005478d7630dd4bdbef93b09abd809c68f7`
- SHA-256 processed: `3cdfbe9caecc78aec661532c1132668846164881836c161774bb0c46e284d09f`
- SHA-256 DDS: `2be9980cfe02d0194645a60efb6719e454f2f71e406301027833b588ad68d908`
- Processing route: `FOCUS-ICON` plus DDS conversion and validation above
- Visual review: PASS — distinct silhouette and final-size legibility reviewed on `contact_sheets/focus_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: source master for a Hearts of Iron IV national focus icon, intended final size 94x86
Primary request: create one original negotiated-frontier compact emblem: two large different state wax seals facing each other across paired stone frontier pillars, the left seal blue-and-white with a simple mountain motif and the right seal charcoal-and-gold with a simple river-gate motif, linked by one clasped treaty ribbon over a lowered chain
Style/medium: compact painterly late-1930s grand-strategy game icon, aged wax, stone, chain and ribbon, strong HOI4-like depth and contrast, clearly original
Composition/framing: one centered symmetrical emblem occupying about 76% of the square canvas; two seals dominate the sides, paired pillars define the frontier, linked ribbon forms a clear central bridge and lowered chain sits beneath; generous clear padding
Lighting/mood: guarded but genuine host-state accommodation, sober highlights with deep charcoal edge shading
Color palette: Bavarian cobalt and ivory, charcoal and muted gold, weathered stone, dark red treaty ribbon, steel grey; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single icon only; crisp dark painted outline around the subject; any shadow must stay tight and attached to the silhouette; seals contain no writing, letters, numerals, eagles or recognizable national emblems; no text, logos, flags, crown, watermark, people, handshake, white rim, glow, sticker border, opaque medallion disk, rectangular frame, or background scene
```

### 17. `idea_rhi_constitutional_river_compact`

- Asset type: Route-institution idea icon
- Related consumer: `rhi_constitutional_river_compact`
- Intended sprite name(s): `GFX_idea_rhi_constitutional_river_compact`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 64x64 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/idea/idea_rhi_constitutional_river_compact.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/idea/idea_rhi_constitutional_river_compact.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/idea_rhi_constitutional_river_compact.png`
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_rhi_constitutional_river_compact.dds`
- SHA-256 source: `593648edd5f2fe0868bd44d93baf10fd3f42df75000fa2acd3948bc5d9a6fb10`
- SHA-256 processed: `5ad95292b60fefe741e3182dd798d61ef154628a353e4292e6fdf79d629789e7`
- SHA-256 DDS: `5891a0fcf5d4394c8a6bafc48035872ce9391fe0d0e0d56c131d36dca25ab0a7`
- Processing route: `IDEA-ICON` plus DDS conversion and validation above
- Visual review: PASS — separate idea-specific master, not derived from focus art, and legible at 64x64 on `contact_sheets/idea_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: separate source master for a Hearts of Iron IV idea or national-spirit icon, intended final size 64x64; this must not reuse or imitate any focus-icon composition
Primary request: create one compact Rhenish constitutional-river symbol: a closed dark-blue civic lawbook clasped by a small bronze bridge arch, with one broad silver-blue river wave passing beneath and a tiny balanced scale fixed to the book clasp
Style/medium: isolated painterly late-1930s grand-strategy spirit icon, aged leather, bronze and enamel, simpler and bolder than focus art, clearly original
Composition/framing: one centered compact symbol occupying about 72% of the square canvas; lawbook is the main mass, bridge arch and river are immediately readable, scale remains simple; generous clear padding
Lighting/mood: stable constitutional order, restrained highlights and a strong charcoal outline
Color palette: dark Rhine blue, aged bronze, silver-grey, warm leather, cream; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single compact spirit icon only; crisp dark painted outline; no focus-icon wreath, frame, large medallion, text, letters, numbers, logos, flags, watermark, readable book title, white rim, glow, sticker border, people, or background scene
```

### 18. `idea_rhi_workers_rhine_charter`

- Asset type: Route-institution idea icon
- Related consumer: `rhi_workers_rhine_charter`
- Intended sprite name(s): `GFX_idea_rhi_workers_rhine_charter`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 64x64 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/idea/idea_rhi_workers_rhine_charter.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/idea/idea_rhi_workers_rhine_charter.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/idea_rhi_workers_rhine_charter.png`
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_rhi_workers_rhine_charter.dds`
- SHA-256 source: `671fba1666db112b4eebd8cc499f9bef670c6306fab54ada07c91253df3c83ce`
- SHA-256 processed: `14958b69f59bbbee816ae567aa5f83806fe707bb0c3ef386a049a2af281f7c97`
- SHA-256 DDS: `96bfdd3e5b61e38c9e45fab312455195150fe5a28b35b53444705e16319e4666`
- Processing route: `IDEA-ICON` plus DDS conversion and validation above
- Visual review: PASS — separate idea-specific master, not derived from focus art, and legible at 64x64 on `contact_sheets/idea_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: separate source master for a Hearts of Iron IV idea or national-spirit icon, intended final size 64x64; this must not reuse or imitate any focus-icon composition
Primary request: create one compact Rhenish workers-charter symbol: a strong rolled-up work sleeve and hand holding a sealed blank charter upright, backed by half of a steel gear and grounded by one sweeping dark-blue river wave
Style/medium: isolated painterly late-1930s grand-strategy spirit icon, worn paper, skin, steel and enamel, simpler and bolder than focus art, clearly original
Composition/framing: one centered vertical symbol occupying about 74% of the square canvas; hand and charter dominate, half-gear makes a broad backing silhouette, river wave stays bold; generous clear padding
Lighting/mood: organized civic labor and industrial solidarity, warm practical highlights with a strong charcoal outline
Color palette: warm parchment, natural muted skin tones, gunmetal, dark Rhine blue, burgundy wax accent; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single compact spirit icon only; crisp dark painted outline; charter and seal contain no writing, symbols, letters or numbers; no focus-icon wreath, frame, hammer-and-sickle, text, logos, flags, watermark, white rim, glow, sticker border, full person, or background scene
```

### 19. `idea_rhi_emergency_corridor_command`

- Asset type: Route-institution idea icon
- Related consumer: `rhi_emergency_corridor_command`
- Intended sprite name(s): `GFX_idea_rhi_emergency_corridor_command`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 64x64 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/idea/idea_rhi_emergency_corridor_command.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/idea/idea_rhi_emergency_corridor_command.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/idea_rhi_emergency_corridor_command.png`
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_rhi_emergency_corridor_command.dds`
- SHA-256 source: `7402f7d81c0cc5c40b8d35d73865e6773a1c9704c2b12127258d65b140bdf604`
- SHA-256 processed: `be8f67cabaa8989e8d1f72ce987091adcac4ae9da330de4fb40fb84397926a88`
- SHA-256 DDS: `4e01b22fa348fb551522df46542df85eecb6c6333c04174db4282195b3d3d973`
- Processing route: `IDEA-ICON` plus DDS conversion and validation above
- Visual review: PASS — separate idea-specific master, not derived from focus art, and legible at 64x64 on `contact_sheets/idea_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: separate source master for a Hearts of Iron IV idea or national-spirit icon, intended final size 64x64; this must not reuse or imitate any focus-icon composition
Primary request: create one compact Rhenish emergency-command symbol: a dark shield bearing a simple river-gate silhouette, crossed behind by a short command baton and a mechanical red signal lamp, with a small rail wheel at the base
Style/medium: isolated painterly late-1930s grand-strategy spirit icon, blued steel, brass and red glass, simpler and bolder than focus art, clearly original
Composition/framing: one centered shield-led symbol occupying about 74% of the square canvas; gate silhouette is broad, baton and signal lamp make a strong diagonal cross, rail wheel remains simple; generous clear padding
Lighting/mood: urgent corridor control, controlled red lamp highlight and a strong charcoal outline
Color palette: midnight blue, gunmetal, aged brass, muted red glass, dark river teal; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single compact spirit icon only; crisp dark painted outline; tightly contained lamp light only; no focus-icon wreath, frame, text, letters, numbers, logos, flags, national emblems, watermark, firearm, white rim, external glow, sticker border, people, or background scene
```

### 20. `idea_rhi_patron_transit_mandate`

- Asset type: Route-institution idea icon
- Related consumer: `rhi_patron_transit_mandate`
- Intended sprite name(s): `GFX_idea_rhi_patron_transit_mandate`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 64x64 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/idea/idea_rhi_patron_transit_mandate.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/idea/idea_rhi_patron_transit_mandate.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/idea_rhi_patron_transit_mandate.png`
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_rhi_patron_transit_mandate.dds`
- SHA-256 source: `9b8ebddb3b3ba9777e2918c6505599aff714721ce9f50e2a7d3696202ebbc72c`
- SHA-256 processed: `19ff6fb88314efa6fefecff7f8573871007a8fa04ddb8cdda4d50d2dd658c938`
- SHA-256 DDS: `2d288133a6186c84d06c03478da2df5daaf8369fe3c1b3f382520cc0aadffdde`
- Processing route: `IDEA-ICON` plus DDS conversion and validation above
- Visual review: PASS — separate idea-specific master, not derived from focus art, and legible at 64x64 on `contact_sheets/idea_rhi_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: separate source master for a Hearts of Iron IV idea or national-spirit icon, intended final size 64x64; this must not reuse or imitate any focus-icon composition
Primary request: create one compact Rhenish patron-transit-mandate symbol: a formal dark-gloved hand presenting a heavy brass transit token above crossed rail and river route bands, with two plain wax seals hanging from the token by short cords
Style/medium: isolated painterly late-1930s grand-strategy spirit icon, aged brass, leather, wax and enamel, simpler and bolder than focus art, clearly original
Composition/framing: one centered compact symbol occupying about 72% of the square canvas; hand and transit token form the focal mass, crossed route bands are broad, two seals hang clearly without clutter; generous clear padding
Lighting/mood: useful but constraining external patronage, restrained golden highlights with a strong charcoal outline
Color palette: black leather, aged brass, dark Rhine blue, burgundy and ivory wax, steel grey; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single compact spirit icon only; crisp dark painted outline; token and seals remain entirely unmarked; no focus-icon wreath, frame, text, letters, numerals, logos, flags, eagles, watermark, white rim, glow, sticker border, full person, or background scene
```

### 21. `idea_bay_constitutional_state_compact`

- Asset type: Route-institution idea icon
- Related consumer: `bay_constitutional_state_compact`
- Intended sprite name(s): `GFX_idea_bay_constitutional_state_compact`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 64x64 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/idea/idea_bay_constitutional_state_compact.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/idea/idea_bay_constitutional_state_compact.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/idea_bay_constitutional_state_compact.png`
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_bay_constitutional_state_compact.dds`
- SHA-256 source: `8847ba069fc9c5ca0d4f9db757b44646eebcb86fb831909fc265b130895b87db`
- SHA-256 processed: `45debe51ee5a1836952f49e41ec94dd7467fcd4078610481cff092ae75ee7bc7`
- SHA-256 DDS: `ff10635b7b61b5d934a52f4b70e982766660039d18947e4725b8885b84df7fc5`
- Processing route: `IDEA-ICON` plus DDS conversion and validation above
- Visual review: PASS — separate idea-specific master, not derived from focus art, and legible at 64x64 on `contact_sheets/idea_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: separate source master for a Hearts of Iron IV idea or national-spirit icon, intended final size 64x64; this must not reuse or imitate any focus-icon composition
Primary request: create one compact Bavarian constitutional-state symbol: a sturdy cobalt lawbook standing between two short pale judicial columns, fastened by a blue-and-white lozenge wax seal with a tiny balanced scale worked into the clasp
Style/medium: isolated painterly late-1930s grand-strategy spirit icon, aged leather, stone, wax and subdued metal, simpler and bolder than focus art, clearly original
Composition/framing: one centered compact symbol occupying about 72% of the square canvas; lawbook is the main mass, columns frame it closely, seal and scale clasp remain simple and readable; generous clear padding
Lighting/mood: settled constitutional authority, cool dignified highlights with a strong charcoal outline
Color palette: Bavarian cobalt and ivory, pale stone, aged brass, charcoal; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single compact spirit icon only; crisp dark painted outline; book and seal contain no writing, letters or numbers; no focus-icon wreath, architectural scene, large frame, crown, text, logos, flags, watermark, white rim, glow, sticker border, people, or background scene
```

### 22. `idea_bay_workers_district_charter`

- Asset type: Route-institution idea icon
- Related consumer: `bay_workers_district_charter`
- Intended sprite name(s): `GFX_idea_bay_workers_district_charter`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 64x64 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/idea/idea_bay_workers_district_charter.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/idea/idea_bay_workers_district_charter.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/idea_bay_workers_district_charter.png`
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_bay_workers_district_charter.dds`
- SHA-256 source: `9b0e8435980ae8516831269bb37c0c71e7279f95718f2a8e0ff629bc9694d9f3`
- SHA-256 processed: `fe27d2363cc88d59423336f2cef0bae925a3ef0ad9b66caa582a6b9ca1355f51`
- SHA-256 DDS: `20a528c769d201c0c18e8c3655eaa96a4dff80fb8adabdcbf2ac291f6080a7cd`
- Processing route: `IDEA-ICON` plus DDS conversion and validation above
- Visual review: PASS — separate idea-specific master, not derived from focus art, and legible at 64x64 on `contact_sheets/idea_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: separate source master for a Hearts of Iron IV idea or national-spirit icon, intended final size 64x64; this must not reuse or imitate any focus-icon composition
Primary request: create one compact Bavarian workers-district-charter symbol: two work-worn hands jointly holding a sealed blank charter, backed by a broad half-gear and three simple factory sawtooth roofs, with one small blue-white district ribbon beneath
Style/medium: isolated painterly late-1930s grand-strategy spirit icon, worn paper, steel, brick and fabric, simpler and bolder than focus art, clearly original
Composition/framing: one centered upright symbol occupying about 74% of the square canvas; hands and charter dominate, gear and factory roofs form one compact backing silhouette, ribbon is a simple lower accent; generous clear padding
Lighting/mood: organized district labor and civic ownership, practical warm highlights with a strong charcoal outline
Color palette: warm parchment, gunmetal, muted brick, Bavarian cobalt and ivory, natural muted skin tones; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single compact spirit icon only; crisp dark painted outline; charter, seal and ribbon contain no writing, letters, numerals or symbols; no focus-icon wreath, frame, hammer-and-sickle, text, logos, flags, crown, watermark, white rim, glow, sticker border, full people, or background scene
```

### 23. `idea_bay_restoration_court_settlement`

- Asset type: Route-institution idea icon
- Related consumer: `bay_restoration_court_settlement`
- Intended sprite name(s): `GFX_idea_bay_restoration_court_settlement`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 64x64 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/idea/idea_bay_restoration_court_settlement.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/idea/idea_bay_restoration_court_settlement.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/idea_bay_restoration_court_settlement.png`
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_bay_restoration_court_settlement.dds`
- SHA-256 source: `b94edfb98f40b68d627fe01eef6a324864971cc69b0d5d9a75babd4c74633744`
- SHA-256 processed: `3b805ca6805da4a9187059a655fb6ff721c6e43eee0d3c5dfbacefaeb4f068c3`
- SHA-256 DDS: `4352ab8b2720dff1afb21e20e14a5e0519b3117dcfdfdb6f77583abdbeb188b8`
- Processing route: `IDEA-ICON` plus DDS conversion and validation above
- Visual review: PASS — separate idea-specific master, not derived from focus art, and legible at 64x64 on `contact_sheets/idea_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: separate source master for a Hearts of Iron IV idea or national-spirit icon, intended final size 64x64; this must not reuse or imitate any focus-icon composition
Primary request: create one compact Bavarian restoration-court symbol: a small restrained open crown resting on a sealed blank court parchment, flanked closely by one pale judicial column and one level bronze scale, with a narrow cobalt ribbon binding the parchment
Style/medium: isolated painterly late-1930s grand-strategy spirit icon, aged parchment, stone, bronze and subdued gilt, simpler and bolder than focus art, clearly original
Composition/framing: one centered compact symbol occupying about 72% of the square canvas; parchment is the main mass, crown stays modest and low, column and scale create a balanced side silhouette; generous clear padding
Lighting/mood: lawful dynastic accommodation rather than triumph, muted warm highlights with a strong charcoal outline
Color palette: warm parchment, Bavarian cobalt, pale stone, antique bronze, subdued gold; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single compact spirit icon only; crisp dark painted outline; parchment and seal contain no writing, letters, numbers or emblems; crown must remain small and simple; no focus-icon wreath, frame, text, logos, flags, watermark, gavel, people, white rim, glow, sticker border, or background scene
```

### 24. `idea_bay_emergency_mountain_guardians`

- Asset type: Route-institution idea icon
- Related consumer: `bay_emergency_mountain_guardians`
- Intended sprite name(s): `GFX_idea_bay_emergency_mountain_guardians`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 64x64 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated original fictional/iconographic art
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/idea/idea_bay_emergency_mountain_guardians.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/idea/idea_bay_emergency_mountain_guardians.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/idea/idea_bay_emergency_mountain_guardians.png`
- Runtime DDS: `gfx/interface/ideas/006_independence_wave/rhineland_bavaria/idea_bay_emergency_mountain_guardians.dds`
- SHA-256 source: `827640161b3e3badc5525bc0ca8394018db5b03edda1d4c7c51282323c1c9ea5`
- SHA-256 processed: `78d7fd431d264719e1bfedd4fd8c648f7a6d623b8ff7a3090ee39d9f71294cbd`
- SHA-256 DDS: `c007a765ecec5eebb90c9bc7078444fe6c685ad241a9690384bcd84af08c9467`
- Processing route: `IDEA-ICON` plus DDS conversion and validation above
- Visual review: PASS — separate idea-specific master, not derived from focus art, and legible at 64x64 on `contact_sheets/idea_bay_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: stylized-concept
Asset type: separate source master for a Hearts of Iron IV idea or national-spirit icon, intended final size 64x64; this must not reuse or imitate any focus-icon composition
Primary request: create one compact Bavarian emergency-mountain-guardians symbol: a dark cobalt shield bearing a single snow peak and signal bell, crossed behind by one alpine staff and one hooded signal lantern, with a tiny stone watchtower base
Style/medium: isolated painterly late-1930s grand-strategy spirit icon, aged enamel, wood, steel, brass and glass, simpler and bolder than focus art, clearly original
Composition/framing: one centered shield-led symbol occupying about 74% of the square canvas; snow peak and bell are bold, crossed staff and lantern create a clean diagonal silhouette, watchtower base stays simple; generous clear padding
Lighting/mood: urgent local vigilance in mountain passes, restrained amber lantern highlight with a strong charcoal outline
Color palette: Bavarian cobalt, snow ivory, slate grey, dark wood, muted amber and brass; do not use magenta
Scene/backdrop: perfectly flat solid #ff00ff chroma-key background for local background removal; one uniform color, no gradient, texture, floor plane, reflection, lighting variation, or background shadow
Constraints: single compact spirit icon only; crisp dark painted outline; tightly contained lantern light only; no focus-icon wreath, frame, text, letters, numbers, logos, flags, crown, watermark, firearms, people, white rim, external glow, sticker border, or background scene
```

### 25. `report_event_006_rhi_corridor_incidents`

- Asset type: Report-event picture
- Related consumer: `RHI corridor incident report-event slot`
- Intended sprite name(s): `GFX_report_event_006_rhi_corridor_incidents`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 210x176 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated fictional late-1930s documentary scene; no real-person likeness or archival-source claim
- Era-fit note: fictional late-1930s Central/Western European documentary composition with period clothing, props, architecture, and photographic treatment; no modern elements or readable generated text.
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/report/report_event_006_rhi_corridor_incidents.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/report/report_event_006_rhi_corridor_incidents.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/report/report_event_006_rhi_corridor_incidents.png`
- Runtime DDS: `gfx/event_pictures/006_independence_wave/rhineland_bavaria/report_event_006_rhi_corridor_incidents.dds`
- SHA-256 source: `a61ad9ac001f7fce85f535a2a939e88ea5e0b5ac595af74a5d064e2fa12a9a25`
- SHA-256 processed: `abe850e7e7d51eb6f3ef0d3501c6b6f14205b68e812d90dd14987e8860b2f1b0`
- SHA-256 DDS: `e7e0c7a5f667021dee374f23b78511b53827e6f338df4a4b55e75f46c2f7d12d`
- Processing route: `REPORT-RHI` plus DDS conversion and validation above
- Visual review: PASS — period-coherent fictional incident scene and readable sepia documentary-card treatment reviewed on `contact_sheets/report_incidents_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: historical-scene
Asset type: source photograph for a Hearts of Iron IV report-event picture, intended final card size 210x176
Primary request: a fictional late-1930s Rhenish corridor incident at a Rhine freight customs point: a customs inspector in a plain period uniform examines an unmarked manifest folder while a railway dispatcher with a signal baton and a soot-stained industrial foreman urgently dispute a detained shipment; two other civic delegates observe
Scene/backdrop: active river-and-rail freight yard beside the Rhine, with a low cargo barge, semaphore signal, warehouse doors, steel crane and distant steelworks structures visible but secondary
Style/medium: convincing 1936-1939 European documentary press photograph made with period 35mm technology, candid realism, authentic clothing and industrial materials, natural film grain, no cinematic concept-art finish
Composition/framing: medium-wide eye-level scene, central group fully visible from waist up around the inspection crate, barge and rail signal establishing the corridor behind them, strong faces and gestures, enough surrounding context for a near-square crop
Lighting/mood: overcast industrial daylight, tense administrative standoff, realistic contrast rather than dramatic studio lighting
Color palette: neutral monochrome photographic values; local sepia card treatment will be applied later
Constraints: fictional unidentified people only; period-accurate late-1930s civilian suits, work clothes and plain customs uniform; all papers, crates and signs completely unreadable and unmarked; no text, letters, numbers, flags, logos, political symbols, swastikas, military insignia, watermark, modern vehicles, modern safety gear, modern architecture, film border, tilted card, illustration, painting, or UI overlay
```

### 26. `report_event_006_bay_state_incidents`

- Asset type: Report-event picture
- Related consumer: `BAY state incident report-event slot`
- Intended sprite name(s): `GFX_report_event_006_bay_state_incidents`
- Owning interface file: `interface/006_independence_wave_rhineland_bavaria_assets.gfx`
- Dimensions: 210x176 RGBA / uncompressed BGRA DDS
- Provenance: OpenAI ImageGen; generated fictional late-1930s documentary scene; no real-person likeness or archival-source claim
- Era-fit note: fictional late-1930s Central/Western European documentary composition with period clothing, props, architecture, and photographic treatment; no modern elements or readable generated text.
- Prompt file: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/prompts/report/report_event_006_bay_state_incidents.txt`
- Source PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/source_png/report/report_event_006_bay_state_incidents.png`
- Processed PNG: `docs/assets/006_independence_wave/rhi_bay_unique_assets_2026_07_16/processed_png/report/report_event_006_bay_state_incidents.png`
- Runtime DDS: `gfx/event_pictures/006_independence_wave/rhineland_bavaria/report_event_006_bay_state_incidents.dds`
- SHA-256 source: `6d2bbe51058a239ba625803f77ffb16dea57f65215657ae837cbe6aa4063d8f5`
- SHA-256 processed: `be5e10faa5a1bc6da73b5204a043f686c17cb29cd40f433490481a202f39b26b`
- SHA-256 DDS: `242f30f609ff275a2b2c192bba35c545bdc1a37c84fad2bea154c3bf400050c6`
- Processing route: `REPORT-BAY` plus DDS conversion and validation above
- Visual review: PASS — period-coherent fictional incident scene and readable sepia documentary-card treatment reviewed on `contact_sheets/report_incidents_contact_sheet.png`.
- Status: `complete` and `handed_off`; main agent owns final runtime wiring confirmation
- Exact ImageGen prompt:

```text
Use case: historical-scene
Asset type: source photograph for a Hearts of Iron IV report-event picture, intended final card size 210x176
Primary request: a fictional late-1930s Bavarian state incident inside a modest Landtag committee antechamber: two district clerks compare large blank account ledgers and several distinct blue-white-toned civic seal stamps on a worn table while an alpine defense representative in plain mountain-guard field dress points toward a sealed pass dossier; a restrained civic delegate and rail official listen
Scene/backdrop: stone-and-dark-wood regional government room with a tall window showing faint alpine ridges, stacked blank ledgers, a mechanical seal press and one period field telephone visible as secondary details
Style/medium: convincing 1936-1939 Central European documentary press photograph made with period 35mm technology, candid realism, authentic clothing and materials, natural film grain, no cinematic concept-art finish
Composition/framing: medium-wide eye-level scene, active group arranged around the ledger table, hands and seal objects readable, alpine representative clearly distinct, enough surrounding context for a near-square crop
Lighting/mood: cool window daylight and subdued practical interior light, tense but procedural state negotiation, realistic contrast rather than dramatic studio lighting
Color palette: neutral monochrome photographic values; local sepia card treatment will be applied later
Constraints: fictional unidentified people only; period-accurate late-1930s civilian suits, clerical dress and plain alpine guard clothing; all ledger pages, dossiers, seals and objects completely unreadable and unmarked; no text, letters, numbers, flags, logos, political symbols, swastikas, military insignia, crown insignia, watermark, modern electronics, modern clothing, modern architecture, film border, tilted card, illustration, painting, or UI overlay
```

## Package inventory and ownership

- Exact prompt files: 26 under `prompts/{focus,idea,report}/`.
- Source PNGs: 26 under `source_png/{focus,idea,report}/`.
- Retained chroma-key alpha masters: 24 under `processed_png/_alpha_masters/{focus,idea}/`.
- Final-size processed PNGs: 26 under `processed_png/{focus,idea,report}/`.
- Contact sheets: 5 under `contact_sheets/`.
- Final DDS files: 26 in the three runtime folders listed by the asset entries.
- Final sprite map: `gfx_handoff.md`.
- Main agent owns `.gfx`, focus, idea, event, localisation, documentation, and other gameplay wiring. This asset subtask did not edit those surfaces or either approved RHI/BAY portrait.

## Blockers

None in the produced visual package. Final completion depends only on the main agent confirming the already expected runtime consumers and registrations.
