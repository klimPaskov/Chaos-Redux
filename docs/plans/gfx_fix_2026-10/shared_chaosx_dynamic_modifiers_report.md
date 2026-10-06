# shared_chaosx_dynamic_modifiers GFX fix report

Disposition: the single severity 2 finding is parent-approved and promoted to its unchanged runtime texture path after a frozen-hash guard.

Source plan: `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` lines 1180-1186.
Raw issue source: `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_issues.json` row 675.
The machine manifest is `docs/assets/gfx_fix_2026-10/shared_chaosx_dynamic_modifiers/manifest.json`.
The GFX handoff is `docs/assets/gfx_fix_2026-10/shared_chaosx_dynamic_modifiers/gfx_handoff.md`.

## Finding disposition

- `GFX_idea_chem_ability_state_contamination`: v1 was rejected by the parent because its shaded bronze trefoil read as an ability icon rather than a vanilla modifier line glyph. V2 is a flat orange and light-gray trefoil with open three-blade gaps and a dark one-pixel-style outline; the parent approved it beside exact installed vanilla modifier references.
- V2 uses a 30x20 canvas, has alpha-zero unused corners and retained its native antialiasing through the strict DDS round-trip.
- The processed nonzero-alpha mean is 160.015; the parent accepted the thin antialiased stroke at native size and declined an opacity floor because it would damage the outline.

## Sources and reference evidence

The canonical modifier contact sheet was inspected first at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/modifiers/contact_sheet.png` (SHA-256 `db63a6cd50b3bc1527d59acdee53800308c3f5a45004a9ccf4e7f847b8e2fd89`).
The individual canonical references inspected were `army_speed_factor.png` (SHA-256 `94aa648663b8762498b8ac0581c595d6f9ac9fbf0f3d86710c860d986789a431`) and `modifier_supply_consumption_factor.png` (SHA-256 `bff5c26aa134de267427e5c4a446401661847e56efd152aeb802c1eaca090a00`).
The exact installed orange reference `gfx/interface/modifiers/MODIFIER_ARMY_SPEED_FACTOR.dds` is 30x20 with SHA-256 `eb8dc7f901ffecbc26e401a0e5c935f26efcc4b7f8c9d194d33353f37c0f84e9`.
The exact installed light-gray reference `gfx/interface/modifiers/MODIFIER_SUPPLY_CONSUMPTION_FACTOR.dds` is 30x20 with SHA-256 `f24d8bfaae07ca63ded05d946c5ac880f698b4a67073b40d9d0535abb1f08d3e`.
The three exact installed/candidate examples are paired at native size and 4x in `docs/assets/gfx_fix_2026-10/shared_chaosx_dynamic_modifiers/evidence/idea_chem_ability_state_contamination_v2_native_4x_contact_sheet.png`.
The skill-local visual-components catalog has no modifier background template; no component layer was used.

## Source, DDS and runtime evidence

The approved original source is `source_pngs/idea_chem_ability_state_contamination_v2.png` (1536x1024, SHA-256 `6ddf78d0432465e6cf1cbbc14d2be29fde5f33eddc34aa56f0bdf79437b8c848`).
Its full prompt is `prompts/idea_chem_ability_state_contamination_v2.md`, and the source requested native transparency in the initial built-in ImageGen call.
The processed image is `processed_pngs/idea_chem_ability_state_contamination_v2.png` (30x20, SHA-256 `27ba72a2f9ea62e971e4c3fdc8efb50c838eb1632152151234fd04bb239fad08`).
The strict canonical DDS candidate was `dds_candidates/v2/gfx/interface/ideas/idea_chem_ability_state_contamination_v2.dds` (SHA-256 `67b2883eeb7f8fce4a2c48dc67dc95e5c975eb0ec1a13e16a30f83c2e5ba2d4b`); strict BGRA header decode and pixel equality both passed.
The runtime path remains `gfx/interface/ideas/idea_chem_ability_state_contamination.dds`; it now has the same approved SHA-256 `67b2883eeb7f8fce4a2c48dc67dc95e5c975eb0ec1a13e16a30f83c2e5ba2d4b`.
The previous runtime DDS hash `953e09d77366dac742259614d9879f02d572864ad650b76019006aa43dd62cca` matched the frozen snapshot immediately before promotion; that original is retained in `evidence/runtime_before_v2_promotion.dds`.
No sprite name or GFX texture path changed.

V1 source, prompt, processed image, and DDS candidate remain preserved in the workspace and the manifest records the parent's rejection basis.
The texconv v1 output declared a single base-level mip-count flag; it did not establish an additional mip chain or an engine-corrupt texture.
The final v2 DDS was written with the documented canonical BGRA writer in `.tools/gfx/gfx.py dds`.

## Exact consumers and remaining live check

The sprite is used by `common/dynamic_modifiers/chemical_state_modifiers.txt:4` and by `common/dynamic_modifiers/033_acid_rain_dynamic_modifiers.txt:190` and `:194`.
There is no `common/ideas` consumer for this sprite, so no separate 65x67 idea-picture variant is needed.
No gameplay, localization, GFX, GUI or costs changed.
The remaining live check is to view the contamination modifiers and acid-rain modifiers in their native lists and confirm the 30x20 trefoil remains clear on the installed interface background.

