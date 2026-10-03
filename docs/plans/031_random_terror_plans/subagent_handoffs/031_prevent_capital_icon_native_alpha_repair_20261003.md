# Event 31 prevent-capital mission icon native-alpha repair handoff

Status: implemented after parent visual review and runtime promotion.
The subagent staged the candidate without runtime writes; the parent completed the installation described below.

## Scope and consumer

- Bounded asset: `mission_random_terror_prevent_capital_seizure` only.
- Required subject retained: the centered fictional period capital building with the dark red steel shield, brass padlock, and orange lightning bolt; no added objects, symbols, or text.
- Exact existing consumer: `GFX_decision_mission_random_terror_prevent_capital_seizure` in `interface/031_random_terror.gfx`, currently using `gfx/interface/decisions/031_random_terror/mission_random_terror_prevent_capital_seizure.dds`.
- The current runtime DDS header identifies a 32x32, one-level, uncompressed BGRA consumer. The canonical mission reference family contains five Vanilla HOI4 samples at 33x32; the exact runtime consumer determines the 32x32 target here.
- The canonical `icons/missions/contact_sheet.png` was inspected before all five individual mission references. Their catalog entries identify the source kind as Vanilla HOI4. The visual-component catalog was also checked; no mission-compatible `background_template` applies, so no component layer was used.

## Initial native ImageGen edit

The official built-in ImageGen edit was available and used once, with the supplied local PNG as the edit target and `transparent_background=true`. The original ImageGen output was reported at:

`C:/Users/klimp/.codex/generated_images/01a10165-6a9c-7f61-9039-e10090735bc6/exec-3445a7a5-9840-4f47-9a41-eba3ee94766a.png`

The retained master is `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/source_png/mission_random_terror_prevent_capital_seizure_source.png` (`1254x1254` RGBA; SHA-256 `20dd09a8555d94dec1e8c2b51b80da6fa08e646fdc563fc68c7d9877f92e7046`). The exact prompt is also saved in `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/prompts/mission_random_terror_prevent_capital_seizure_imagegen_edit_prompt.md`.

Verbatim submitted prompt:

```text
Use case: background-extraction
Asset type: Hearts of Iron IV 32x32 decision-mission icon source edit for GFX_decision_mission_random_terror_prevent_capital_seizure.
Input images: Image 1: edit target, the supplied 1254x1254 Event 31 mission icon with an opaque pale checkerboard baked into its background.
Primary request: Remove only the baked pale gray-and-white checkerboard background and return the existing icon artwork as a clean cutout on a genuinely transparent canvas.
Subject: Preserve the same centered fictional period capital building, dark red steel shield, brass padlock, and orange lightning bolt already present in Image 1.
Style/medium: Preserve the existing painted HOI4 icon illustration, its materials, texture, color, shading, and edge treatment.
Composition/framing: Preserve the square canvas, subject position, scale, proportions, and complete silhouette. Keep every existing subject detail and edge intact, with no clipping.
Constraints: Change only the checkerboard background to real transparency. Keep the building, shield, padlock, and bolt unchanged in shape, color, arrangement, detail, and style. Preserve attached original shading and shadows. No added, removed, or rearranged objects or symbols; no text, border, glow, or redesign. All unused canvas outside the complete artwork must be genuinely transparent, with clean antialiased edges and no checkerboard, matte, halo, fringe, or spill.
```

## Staged output files and hashes

- ImageGen master: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/source_png/mission_random_terror_prevent_capital_seizure_source.png`; SHA-256 `20dd09a8555d94dec1e8c2b51b80da6fa08e646fdc563fc68c7d9877f92e7046`.
- Processed 32x32 PNG: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/processed_png/mission_random_terror_prevent_capital_seizure_32x32.png`; SHA-256 `cb12802d32d06191156cb56c0af0993638af71a0049b21b12773d9c2d809f6be`.
- DDS candidate: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/candidate_dds/mission_random_terror_prevent_capital_seizure.dds`; SHA-256 `822acabf6e1366ee27adbd2e06a8bf65ee725a030ed9cdc09b3c20b6a324be0a`.
- Decoded DDS round-trip: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/decoded_roundtrip/mission_random_terror_prevent_capital_seizure_dds_roundtrip.png`; SHA-256 `cb12802d32d06191156cb56c0af0993638af71a0049b21b12773d9c2d809f6be`.
- The processed PNG and decoded round-trip pixels are byte-identical; the round-trip PNG hash also matches because the saved PNG bytes are identical.
- Contact sheet: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/mission_random_terror_prevent_capital_seizure_native_alpha_contact_sheet.png`; SHA-256 `601f54823ee7a59c5067874f6f134b1194ae08e3cc50249cf8054d5eac4089c0`.
- Prompt record: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/prompts/mission_random_terror_prevent_capital_seizure_imagegen_edit_prompt.md`; SHA-256 `6d928a7e580958c5d521f4a9ecac4cd487ab4430dc58fdb2fc55910a91b02713`.

## Candidate views

- Contact sheet with the master, processed PNG, 4x smooth preview, decoded DDS, light and dark compositions, current runtime comparison, and alpha channel: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/mission_random_terror_prevent_capital_seizure_native_alpha_contact_sheet.png`.
- Native ImageGen master composited on light: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/source_native_on_light.png`.
- Native ImageGen master composited on dark: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/source_native_on_dark.png`.
- Processed 32x32 candidate enlarged 8x on light: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/candidate32_on_light_8x.png`.
- Processed 32x32 candidate enlarged 8x on dark: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/candidate32_on_dark_8x.png`.
- Processed candidate at 4x smooth enlargement: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/candidate32_smooth_4x.png`.
- 4x smooth candidate composited on light: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/candidate32_smooth4x_on_light.png`.
- 4x smooth candidate composited on dark: `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/candidate32_smooth4x_on_dark.png`.
- The unchanged current runtime DDS was decoded only for comparison at `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/review/existing_runtime_dds_decoded_review.png`.

## Validation and limitations

- The ImageGen master is `1254x1254` RGBA, alpha range `0–255`, and has four zero-alpha corners. The baked checkerboard is absent from the source master.
- At alpha `>=8`, source bounds are `(147,20)` to `(1107,1234)` with right and bottom exclusive. Nine master pixels on the far-left edge have alpha `1`; they are not apparent in the light/dark views. No alpha cleanup or background-removal fallback was applied.
- The processed preview is exactly `32x32`, RGBA, alpha range `0–255`, and all four corners remain zero-alpha. At alpha `>=64`, bounds are `(4,1)` to `(28,32)` with right and bottom exclusive.
- `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` produced the candidate DDS. Its exact 128-byte header matches the untouched runtime DDS header. The candidate has a 4224-byte total length and zero mipmaps.
- Pillow decoded the final DDS and the decoded RGBA pixels matched the processed PNG exactly.
- The checkerboard visible in contact-sheet panels is a review-only transparency aid. It is not in the ImageGen source, processed PNG, or DDS.
- The source, runtime DDS, GFX, gameplay, localization, inventories, and unrelated assets were not edited. Original source SHA-256 remains `fe44a21912cd8af16185936551a58bb69561d7416c6fdbbac35e72635e259cb7`; original runtime DDS SHA-256 remains `4e1556bbeaa327cc6f771ae8871fc2a28d99a4070a5be0ed9b5696080af81368`.
- `.gitignore` line 80 ignores `docs/assets/`, so the staging files remain available in the shared workspace but are not shown by `git status`. No force-add or `.gitignore` change was made.
- No ImageGen or alpha-validation failure occurred. The remaining gate is parent visual review and the parent's final installation/hash-inventory reconciliation.

## Handoff

`docs/assets/031_random_terror/icon_native_alpha_repair_20261003/manifest.md` contains the asset manifest. `docs/assets/031_random_terror/icon_native_alpha_repair_20261003/gfx_handoff.md` carries the existing sprite and runtime-path wiring note. Parent review must happen before the staged DDS is copied to `gfx/interface/decisions/031_random_terror/mission_random_terror_prevent_capital_seizure.dds`.

## Parent acceptance and installation

The parent accepted this single targeted repair under the user's explicit complete visual-audit and repair instruction.
Review covered the full contact sheet, native light-background source and smooth enlarged dark-background consumer preview.
The capital building, steel shield, brass lock and orange attack marker remain readable in the same composition, with no baked checkerboard or visible matte fringe.
The nine source alpha-one pixels remain disclosed; no cleanup fallback was used.
The parent verified the old runtime hash and new candidate hash before replacing only the exact registered DDS path.
The installed runtime SHA-256 is `822acabf6e1366ee27adbd2e06a8bf65ee725a030ed9cdc09b3c20b6a324be0a`.
The existing GFX sprite and mission consumer are unchanged.
The inherited RGB/background-removal procedural gap for this final asset is resolved by the retained real native ImageGen edit, not by claiming that an earlier edit occurred.
Historical source and runtime comparison files remain in the temporary workspace; retain them until the full event's asset lifecycle is complete.
This is visual/source-consumer acceptance for one asset, not observed live-game rendering or whole-event completion.
