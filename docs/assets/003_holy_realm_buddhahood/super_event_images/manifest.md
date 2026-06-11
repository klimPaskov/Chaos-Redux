# Holy Realm Buddhahood Super-Event Image Manifest

Package scope: Holy Realm Buddhahood super-event image assets.

Reference inspection completed:
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_divine_sovereignty.png`
- `.agents/skills/chaos-redux-event-assets/assets/super_event_images/super_event_angel_directorate.png`
- Existing wired target dimensions from `gfx/super_events/super_event_powers_of_the_awakened.dds`: `457x328`

Source mode:
- Built-in `$imagegen` for generated symbolic, supernatural, alternate-history super-event artwork.

DDS conversion note:
- Local processing copied the generated source into this package, resized/cropped to `457x328`, converted to grayscale, applied light contrast/sharpening, and exported DDS with `convert -define dds:compression=none`.
- Final DDS was validated at `457x328`.

## Assets

### `super_event_powers_of_the_awakened`

- Asset type: super-event image
- Intended in-game use: super-event slot `61`, `Powers of the Awakened`
- Sprite name: `GFX_super_event_powers_of_the_awakened`
- Source mode: built-in `$imagegen`
- Source PNG: `docs/assets/003_holy_realm_buddhahood/super_event_images/source_png/super_event_powers_of_the_awakened_source.png`
- Processed PNG: `docs/assets/003_holy_realm_buddhahood/super_event_images/processed_png/super_event_powers_of_the_awakened.png`
- Prompt record: `docs/assets/003_holy_realm_buddhahood/super_event_images/prompts/super_event_powers_of_the_awakened_prompt.md`
- Final DDS: `gfx/super_events/super_event_powers_of_the_awakened.dds`
- Target size: `457x328`
- Visual direction: monochrome period-documentary battlefield report in the Himalayan foothills, with a chaos army halted by an implied awakened presence.
- Notes: Replaces the copied Buddha Mandate placeholder with bespoke art while preserving the existing sprite name and texture path.
- Asset status: `complete`
