# Making Chaos Redux art with the hoi4-imagegen MCP

Use the `hoi4_imagegen` MCP (tools `hoi4.image_*`) for new or replaced Chaos Redux art. Read the `hoi4-imagegen` skill for the full loop. The manual route in `SKILL.md` (the gptimage `generate_image` tool, `tools/` and `.tools/gfx/gfx.py`) stays as the fallback when the MCP is not connected, has no signed-in provider, or the art is not one of its 40 families.

## Rules for this mod

- Every group tool (`hoi4.image_icon`, `_picture`, `_portrait`, `_flag`, `_unit`, `_interface`) needs a `family`. Pick it from `hoi4.image_families`. Without `approve` the call is a free plan: tell the user its cost before you approve. With `approve: true` and an `idempotency_key` it makes one asset.
- Sizes come from this mod's own `.tools/gfx/profiles.json` rows: focus 94x86, idea 64x64 and decision 32x32. Every other family uses its vanilla canvas. `hoi4.image_families` shows the difference from vanilla, so say it when you plan one of those three.
- Style references: the tool takes them from existing Chaos Redux art of the same family first and from `assets/gfx_references/` in this skill second (tier 2), and it reports which it used and why. Add a reference with `hoi4.image_references` and give its role and rights note. Never invent a source.
- Processing runs inside the tool: the report card and its shadow, the achievement triplet, the advisor card, the portrait crop, the flag ladder, the focus `_shine` sprite, frame strips and DDS or TGA export. Run `hoi4.image_process`, `hoi4.image_validate`, `hoi4.image_preview`, `hoi4.image_review` and `hoi4.image_install` in that order. Do not run the manual processors for an asset the tool makes.
- Never derive one family's asset from another's. An idea icon is not a resized focus icon. The tool refuses another family's size (`GFX-FAMILY-MISMATCH`) and another family's installed pixels (`GFX-FAMILY-REUSE`).
- Sourced or user-provided art of one of the 40 families is imported through `hoi4.image_process` with its `family`, so it runs under the same ledger.
- Before the handoff, run `hoi4.image_audit` (the cross-family reuse audit of the whole mod) and list what it found.
- `hoi4.image_install` writes a sprite handoff by default. The main agent wires the `.gfx` file. Check that the installed paths and names follow this skill's folder and naming rules before wiring.
- No text in art. The result is installed, not verified in game: list exactly what the user should look at in game, and never start Hearts of Iron IV.
