# Holy Realm Asset and Animation Specification

This event requires a full asset package. It uses leader portrait evolution, animated mandala GUI, decision icons, focus icons, idea icons, super-event art, report images, flags, formable identity assets, and achievement icons.

Texture consumers use the DDS treatment required by their inspected family, while country flags use the installed flag format and three-size family.
Production, references, native transparency, conversion, specialist ownership, and manifests follow [chaos-redux-event-assets](../../../../../.claude/skills/chaos-redux-event-assets/SKILL.md).
Frame packages follow [chaos-redux-frame-animation](../../../../../.claude/skills/chaos-redux-frame-animation/SKILL.md).
Every character portrait belongs to `chaosx_portrait_creator`, including fictional, symbolic, and animated portrait variants.
The source modes below describe design classification and do not authorize non-portrait workers to produce portraits or agents to operate RunPod.

## Reference folders to inspect before asset work

All folders are under `.claude/skills/chaos-redux-event-assets/assets/gfx_references/` in the repository:

- Ideas and national spirits: `icons/ideas`.
- News event images: `event_art/news`.
- Report event images: `event_art/report`.
- Super-event images: `event_art/super_event`.
- Decision icons: `icons/decisions`.
- Flags: `flags/normal`.
- Focus icons: `icons/national_focus`.
- Achievements: `icons/achievements`.

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

Implementation coverage (current as of the 2026-10-06 release reconciliation):

- Mandala: all seven states above are implemented as 16-frame `6720x420` sheets plus static fallbacks under `gfx/interface/decisions/003_holy_realm/mandala_states/`, selected through `GetHolyRealmMandalaSprite`.
  The parent-approved real-frame package (14 DDS files, digest `F55E542C65E2604DB946F58D9FB7ACF599FB9C922058E8486525F95824677F56`) and its manifest live in `docs/assets/003_holy_realm_buddhahood/release_animation_20261006/`; it supersedes the earlier opaque glow-only sheets, which are kept only as rejected evidence.
- Portraits: `GFX_portrait_THR_buddha_mandate_animated` and `GFX_portrait_THR_empty_seat_animated` are 16-position sheets built from eight authored poses mirrored into the loop, a parent-authorized reduction; their static fallbacks are `GFX_portrait_THR_buddha_mandate` and `GFX_portrait_THR_empty_seat`.
  The active package is documented in `docs/plans/003_holy_realm_plans/subagent_handoffs/portraits_release_20261006.md` and archived under `docs/assets/portraits/003_holy_realm/release_20261006/`.
- Dhyana Seal: the five concentration decision rows use a static 34x34 lotus (accepted 2026-10-06 graphics decision); the 12-frame `GFX_decision_holy_realm_dhyana_seal_animated` sheet stays registered as an unused reserve and is not a live GUI feature.
- The former source archive `docs/assets/003_holy_realm_buddhahood/animations/` no longer exists; do not regenerate it.

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
