# Asset Prompt: Holy Realm Buddhahood

Create the full visual asset package for `holy_realm_buddhahood` using `chaos-redux-event-assets` and `chaos-redux-frame-animation`.

Read the spec files under `docs/specs/003_holy_realm_specs/003_holy_realm_buddhahood_specs/specs/`, especially `holy_realm_buddhahood_asset_animation_spec.md`.
Read [the package authority and resume rules](../README.md) and the current asset handoffs before assigning a bounded production list.
Route every character portrait, including symbolic and animated portraits, to `chaosx_portrait_creator`.
Use the current asset skill for grounded-source placeholders and user-supplied HOI4-style finals, reference inspection, transparency, conversion, and specialist ownership.

Required asset groups:

- Leader portraits for Bodhisattva, Teacher of Four Directions, Great Bodhisattva, Buddha, Empty Seat, and False Buddha if schism is implemented.
- Animated Buddha portrait and static fallback.
- Animated mandala GUI sprites for dormant, teaching, meditation, awakened, wrathful, final silence, and empty states.
- Animated Dhyana Seal button and static fallback.
- Mandala panel background, value icons, warning overlays, button states, progress frames, and locked overlays.
- Report images for first reveal, teaching under bombardment, mandala chamber, and false schism.
- Super-event images for The Awakened One, Powers of the Awakened, and The Final Silence.
- Focus icon family pack for all route families.
- Idea icons and decision icons listed in the asset spec.
- Flags for Holy Realm, Awakened Realm, Empty Seat, False Mandala, Great Mandala, and Silent Mandala where implemented.
- Achievement icons listed in the achievement spec.

Source modes:

- Use generated art for fictional non-portrait assets and symbolic non-portrait assets.
- Portrait source classification and production belong to `chaosx_portrait_creator` under the current asset skill.
- Source real images for any real person, real historical flag, or real religious symbol used directly.
- Do not generate real historical leader portraits.
- Do not use generated text.
- Request native transparency for alpha-backed icons, seals, overlays, and source frames, preserving alpha through the owner skill's processing and conversion workflow.

Before creating assets, inspect the reference folders listed in the asset spec. Create source PNGs, processed PNG previews, final DDS files, manifests, contact sheets where useful, and `gfx_handoff.md` entries. Animated assets must use real source frames and final frame-sheet DDS files, with GIF previews only for review.

Every asset entry must include source mode, target size, final DDS path, proposed sprite name, target `.gfx` file, intended in-game use, and status.
Non-portrait art workers return files and handoffs without editing gameplay or runtime registries unless the parent explicitly expands scope.
The portrait worker retains the skill's portrait-specific wiring exception.
