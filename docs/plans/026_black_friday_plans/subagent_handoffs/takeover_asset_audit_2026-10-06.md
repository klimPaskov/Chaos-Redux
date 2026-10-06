# Event 026 asset audit and repair handoff

Disposition: implemented the accepted achievement-source correction and rebuilt its complete runtime state triplet; parent reviewed the candidate and processed 64x64 states. Report and idea artwork remain unchanged. No `.gfx` file edit or new asset family was needed.

## GFX plan and issue

The reviewed `C:/Users/klimp/Videos/chaos_redux_trailer/records/gfx_review/gfx_fix_plan.md` has no Event 026 owner section and no direct `black_friday` or Event 026 sprite defect row. It cites Event 026 only as a good reference group in the Event 025 idea-style comparison and shared achievement-state comparison. The cross-cutting baked-text rule was relevant to the actual completed achievement: its cream tag visibly read `0%`, contrary to its retained prompt's no-readable-text constraint. The parent confirmed the conflict and authorized the narrow correction.

The accepted edit leaves the tag blank while retaining the ledger, its four small checks and circled final check, the crate, blue file, fuel can, coins, and pen. Two earlier edits were rejected: `C:/Users/klimp/.codex/generated_images/01a10fb9-0a2f-7a51-8861-9c3ea992ee23/exec-8f4df3a6-bc46-440f-b60a-9b45ad6d024e.png` retained the `0%` marking, and `C:/Users/klimp/.codex/generated_images/01a10fb9-0a2f-7a51-8861-9c3ea992ee23/exec-aeddc018-0d21-4b41-865d-0b56526ca09f.png` blanked the tag but removed the circled ledger check. The accepted built-in ImageGen output is `C:/Users/klimp/.codex/generated_images/01a10fb9-0a2f-7a51-8861-9c3ea992ee23/exec-4ab58977-34f5-47ce-8e40-77ead2fc7572.png` and was copied unchanged to `docs/assets/026_black_friday/source_png/026_black_friday_five_departments_textfree_edit.png`. Its prompt is `docs/assets/026_black_friday/prompts/achievement_completed_textfree_edit_prompt.txt`.

## References and consumers

I used only the canonical reference root `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/gfx_references`. I inspected each matching contact sheet before its individual references: report art, ideas, and achievements. The report family has a `210x176` tilted transparent-card canvas; the idea references are mostly `60x68` isolated objects, while the event-owned icon remains at its specified `64x64`; achievement examples and supplied state templates are `64x64`.

The exact report consumers are `chaosx.nr26.2` and `chaosx.nr26.3` in `events/026_black_friday.txt`; both use `GFX_report_event_026_black_friday`. The handoff previously named `.1`, which is the hidden dispatcher and does not display the image; `docs/assets/026_black_friday/gfx_handoff.md` now records the two direct consumers. The active-sale idea and its evolution both use `GFX_idea_026_black_friday_sale`. The achievement id is `026_black_friday_five_departments`; its root-only DDS states and existing aliases in `interface/026_black_friday.gfx` match the exact expected paths. All five runtime files and their referenced canonical examples exist.

The report and idea DDS hashes remain `9430A02ABA3130884918F16A2EE28BECAFBF4272BC46CC54B42F7A4C9373E102` and `375ECA0DB0A0375A36DB9F1292D6264E112153F0AEFF2A723821A5B02D28A434`. They were not changed.

## Achievement processing and evidence

The accepted edited source is `1254x1254 RGBA`, alpha range `0..255`, with transparent corners. Its alpha-at-least-8 subject bounds are `(9, 82, 1241, 1192)`. Normalization cleared only the 44 alpha-1 pixels on the outermost canvas boundary; the original ImageGen file remains unchanged. The centered color source layer is `64x64 RGBA`, alpha range `0..255`, bounds `(4, 6, 60, 57)`. Its SHA-256 is `85DF2858D968A7C771712E19C1BD6E4AF25CB42DE7DCC0F6601A40A6B6C40CE9`.

The grey layer is deterministic grayscale of that one corrected color layer with alpha preserved; SHA-256 `F5A302FF0F15903C7906644A1610DDC04882748855FE558117293C21ACF99DC2`. The not-eligible layer is the grey layer composited with the unchanged canonical overlay; SHA-256 `6565FEE4C849D714009F7A0C9380312FBE6FD21752B1FA6F41F51B6E3B0D2B31`. The required achievement processor, `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py`, reported `AUDIT OK 026_black_friday_five_departments: strict 64x64 BGRA triplet and source-layer equality verified` before and after runtime promotion.

The exact supplied workflow-template hashes remained unchanged: completed `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`, grey `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`, and red-X overlay `89BC80C6AC975BF6F1FF000FF3070B20C337BFB8B8AE966AE35A5540C004D6DD`. Read-only pixel comparisons confirmed exact grayscale and exact grey-plus-overlay composition.

| Runtime state | Size | SHA-256 |
| --- | ---: | --- |
| `gfx/achievements/026_black_friday_five_departments.dds` | 16,512 bytes | `B5D3BE977B8D5CC0943C4503AFA800EA31AA07487F2661683A40EF53DAC0E86D` |
| `gfx/achievements/026_black_friday_five_departments_grey.dds` | 16,512 bytes | `893BBBDF7858D30A676334AD2543A2E4E92CD7DEF9B179BE53AD1EF081329F6C` |
| `gfx/achievements/026_black_friday_five_departments_not_eligible.dds` | 16,512 bytes | `C3B9DC3CCD0550A64C18F845A2A96BE36C84076585D03E8E25F7FF56280354B2` |

All three are strict one-level `64x64` BGRA DDS files with alpha range `254..255`; each runtime file is byte-identical to its staged copy. FFmpeg DDS-to-PNG previews for all five Event 026 assets are in `docs/assets/026_black_friday/decoded/audit_2026-10-06/`. I opened each final decode at native size. The report and idea decodes match their processed PNG pixels exactly; each achievement decode matches its processor review PNG exactly. The refreshed icon contact sheet is `docs/assets/026_black_friday/contact_sheets/icon_package_contact_sheet.png`, SHA-256 `CF903CB943F7D31068253591462C2CD08583A8FE02967498A57914B19BE1F50B`.

## Files changed and remaining limits

Changed asset files: the accepted edited source PNG and prompt; three processed achievement layers; three staged achievement DDS files and their processor review PNGs; three root runtime achievement DDS files; five DDS-decoded audit previews; the event asset manifest, source-mode note, GFX handoff, and icon contact sheet; and this handoff.

No runtime `.gfx`, gameplay, localisation, or event file was changed. Existing GFX registrations already point to the exact runtime paths. No live HOI4 texture session was launched; in-game texture acceptance remains user-owned. The parent owns updating `docs/plans/026_black_friday_plans/event26_asset_audit.md` and the focused commit.

Skills used: `chaos-redux-event-assets` and official `imagegen`.
