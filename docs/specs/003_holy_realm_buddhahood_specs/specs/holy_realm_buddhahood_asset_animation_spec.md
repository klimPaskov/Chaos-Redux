# Holy Realm Asset and Animation Specification

This event requires a full asset package. It uses leader portrait evolution, animated mandala GUI, decision icons, focus icons, idea icons, super-event art, report images, flags, formable identity assets, and achievement icons.

All final game assets must be processed into DDS and placed in the correct mod folders. Asset workers must create source PNGs, processed PNG previews, final DDS files, manifests, and `gfx_handoff.md` notes. Animated assets must follow the frame animation workflow and must deliver frame sheets, not GIFs.

## Reference folders to inspect before asset work

- Ideas and national spirits: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/ideas`.
- News event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/news_event_images`.
- Report event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/report_event_images`.
- Super-event images: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/super_event_images`.
- Decision icons: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/decisions`.
- Flags: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/flags`.
- Focus icons: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/focuses`.
- Achievements: `~/projects/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/achievements`.

## Source mode rules

Generated source mode:

- Fictional leader portraits.
- Symbolic council portraits.
- Mandala panel backgrounds.
- Animated mandala frames.
- Focus icons.
- Idea icons.
- Decision icons.
- Achievement icons.
- Fictional flags.
- Super-event images for supernatural or symbolic moments.
- Report images that show fictional alternate-history scenes.

Sourced source mode:

- Any real historical person.
- Real flags or real religious symbols if used directly.
- Real historical sites or archival images if the event chooses to depict actual material.

Do not generate a portrait of a real person. Do not invent historical flags with generated art if the route claims to use real historical symbols.

## Leader portraits

Target size: 156x210.

Required portraits:

| Asset | Source mode | Static | Animated | Notes |
| --- | --- | --- | --- | --- |
| Bodhisattva leader | Generated unless real person chosen | Required | Not required | Humble teacher, period HOI4 style |
| Teacher of Four Directions | Generated | Required | Optional | Slight aura, more pilgrim symbols |
| Great Bodhisattva | Generated | Required | Optional | Mandala shadow, no generated text |
| Buddha leader | Generated symbolic fictional | Required | Required | Calm luminous figure, not a caricature |
| Empty Seat successor | Generated symbolic | Required | Required | Empty throne, lotus, bell, or council silhouette |
| False Buddha | Generated symbolic | Required if schism implemented | Optional | Cracked mandala or excessive light |

Animated portrait guidance:

- 8 frames.
- Frame size 156x210.
- Sheet size 1248x210.
- FPS 6 to 8.
- Looping yes.
- Static fallback required.
- Motion should be subtle source-frame variation, such as robe stillness, halo breath, candle flicker, or dust in light.
- Do not make fake speech or modern deepfake-like motion.

## Mandala GUI assets

Suggested central size: 420x420. Implementation may adjust after checking the existing GUI.

Required central animated sprites:

| Sprite | Frames | Sheet size | State |
| --- | --- | --- | --- |
| `GFX_holy_realm_mandala_dormant_animated` | 16 | 6720x420 | Locked or early state |
| `GFX_holy_realm_mandala_teaching_animated` | 16 | 6720x420 | Teaching missions active |
| `GFX_holy_realm_mandala_meditation_animated` | 16 | 6720x420 | Three-minute vow active |
| `GFX_holy_realm_mandala_awakened_animated` | 16 | 6720x420 | Buddhahood complete |
| `GFX_holy_realm_mandala_wrathful_animated` | 16 | 6720x420 | Chaos emergency |
| `GFX_holy_realm_mandala_final_silence_animated` | 16 | 6720x420 | Final Silence ritual |
| `GFX_holy_realm_mandala_empty_animated` | 16 | 6720x420 | After Final Silence |

Each needs a static fallback without `_animated`.

Implementation coverage:

- `GFX_portrait_THR_buddha_mandate_animated` is delivered as a 16-frame `2496x210` sheet at `gfx/leaders/THR/portrait_THR_buddha_mandate_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/`. The static fallback remains `GFX_portrait_THR_buddha_mandate`.
- `GFX_portrait_THR_empty_seat_animated` is delivered as a 16-frame `2496x210` sheet at `gfx/leaders/THR/portrait_THR_empty_seat_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_empty_seat/`. The static fallback is `GFX_portrait_THR_empty_seat`.
- `GFX_decision_holy_realm_dhyana_seal_animated` is delivered as a 12-frame `1152x96` sheet at `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/`. The static fallback is `GFX_decision_holy_realm_dhyana_seal`.
- `GFX_holy_realm_mandala_dormant_animated` is delivered as a 16-frame `6720x420` sheet at `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_dormant_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/`.
- `GFX_holy_realm_mandala_teaching_animated` is delivered as a 16-frame `6720x420` sheet at `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_teaching_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_teaching/`.
- `GFX_holy_realm_mandala_meditation_animated` is delivered as a 16-frame `6720x420` sheet at `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_meditation_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/`.
- `GFX_holy_realm_mandala_awakened_animated` is delivered as a 16-frame `6720x420` sheet at `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_awakened_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/`.
- `GFX_holy_realm_mandala_wrathful_animated` is delivered as a 16-frame `6720x420` sheet at `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_wrathful_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/`.
- `GFX_holy_realm_mandala_final_silence_animated` is delivered as a 16-frame `6720x420` sheet at `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_final_silence_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_final_silence/`.
- `GFX_holy_realm_mandala_empty_animated` is delivered as a 16-frame `6720x420` sheet at `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_empty_animated.dds`, with source frames, processed frames, preview GIF, contact sheet, and prompt notes under `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/`.
- All required central Mandala animated sprites in this table have source-frame packages and wired DDS frame sheets.

Central mandala visual direction:

- Sacred wheel, lotus geometry, mountain silhouette, candle or lamp light.
- No readable generated text.
- Strong center and ring readability.
- Low clutter at in-game size.
- State changes should be meaningful, not only hue shifts.

## Dhyana Seal button animation

Target size: 96x96.

Frames: 12.

Sheet size: 1152x96.

States:

- Locked.
- Available.
- Holding or channeling.
- Interrupted.
- Complete.

The active loop should show a pulse drawn in source frames. Do not create the final animation by applying a script-made brightness pulse to one still.

## Panel support assets

| Asset | Size direction | Use |
| --- | --- | --- |
| Mandala panel background | Match GUI window | Main scripted GUI plate |
| Value icons | 32x32 or 40x40 | Bodhi, Dhyana, Compassion, Detachment, Defilements, World Suffering |
| Progress bar frames | GUI dependent | Meditation Charge and Bodhi Progress |
| Warning overlays | GUI dependent | High Defilements and Wrathful Protection |
| Locked overlays | GUI dependent | Unmet power or Final Silence requirements |
| Hover and selected button states | GUI dependent | All clickable mandala buttons |

## Event images

Report event image target: 210x176.

News event image target: 397x153, black and white.

Super-event image target: 457x328.

Required image directions:

| Image | Type | Source mode | Direction |
| --- | --- | --- | --- |
| First Holy Realm reveal | Report | Generated documentary or sourced Himalayan period photo if appropriate | Mountain monastery, nervous envoys, quiet bell |
| Teaching under bombardment | Report | Generated documentary | Monks and medics moving through ruins, no modern props |
| Mandala chamber opens | Report | Generated symbolic documentary | Dark room, luminous mandala, officials watching |
| Buddhahood transformation | Super-event | Generated symbolic | Luminous seated figure, mountain horizon, no text |
| First power display | Super-event or news | Generated symbolic | Chaos army halted at river, wall, or pass by serene light |
| Final Silence | Super-event | Generated symbolic | Empty seat, still world, extinguished flames |
| False Buddha Schism | Report or news | Generated symbolic | Cracked mandala, rival banners, unrest |

## Focus icon families

Target size: 94x86.

Icon families can be reused by branch, but the final manifest must map actual focus ids to icons.

| Family | Motif |
| --- | --- |
| Opening trunk | Bell, mountain gate, monastery road |
| Teaching path | Scroll, lamp, traveling monks, radio sutra |
| Meditation path | Lotus, breath, seated figure, quiet wheel |
| Governance | Council seats, sealed office, regent seal |
| Sanctuary industry | granary, road, workshop, clinic, supply hub |
| Guardian military | mountain pass, temple guard, shield and bell |
| Diplomacy compact | joined hands, compact seal, relief convoy |
| Liberation route | pilgrimage road, protected valley, open gate |
| Powers | water, wall, sky, invisibility veil, sun and moon |
| Final Silence | empty lotus, extinguished lamp, silent bell |
| Schism | cracked halo, false wheel, broken seal |

## Idea and decision icons

Idea icon target: 64x64.

Decision icon target: 32x32.

Required icons:

- Fragile Sangha.
- Remote Sanctuaries.
- Worldly Burden.
- The Awakened Seat.
- Revealed Powers of the Buddha.
- Empty Seat.
- False Mandala.
- Holy Realm Mandala category.
- Teaching Missions category.
- Sanctuary Works category.
- Sangha Compact category.
- Buddha Powers category.
- Final Silence category.
- Each power button.
- Major teaching mission families.

## Flags

Required sizes:

- Normal 82x52.
- Medium 41x26.
- Small 10x7.

Flag states:

- Holy Realm base.
- Awakened Realm.
- Empty Seat.
- False Mandala if schism identity exists.
- Great Mandala formable.
- Silent Mandala hidden formable.
- Puppet variants only if possible.

Visual motifs:

- Wheel, lotus, mountain, bell, empty seat.
- Distinct silhouettes at small size.
- No generated text.

## Achievement icons

Target size: 64x64.

Completed version first, then grey and not-eligible variants if the repository achievement system requires them.

Each achievement in the achievement spec has an icon direction.

## GFX handoff requirements

Every asset that needs a sprite must provide:

- Final DDS path.
- Proposed static sprite name.
- Proposed animated sprite name where relevant.
- Target `.gfx` file.
- Target `.gui` file or gameplay surface.
- Frame count and FPS for animated assets.
- Static fallback path.
- Notes on whether the sprite is decorative or state-driven.

The implementation agent must verify animated sprite syntax against local HOI4 examples before wiring.

## Quality gates

The asset package is incomplete if:

- Any final image remains only as PNG when the game expects DDS.
- Any animation is only a GIF.
- Any animation was made from one still through transform-only effects.
- Any leader portrait for a real person was generated.
- Any historical flag or symbol is invented without noting it is fictional.
- Any animated sprite lacks a static fallback.
- The manifest does not record source mode, source path, final path, target size, and sprite name.
