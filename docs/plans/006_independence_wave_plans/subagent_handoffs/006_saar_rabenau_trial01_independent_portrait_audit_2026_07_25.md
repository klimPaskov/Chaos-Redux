# IW-010 Saar Friedrich von Rabenau trial-01 independent portrait audit

Date: 2026-07-25  
Reviewer: independent sourced-portrait audit subagent  
Decision: **PASS**  
Disposition: `approved_for_parent_promotion`  
Runtime authorization: **export-only; no DDS conversion, no `.gfx` wiring, no character edit, and no runtime texture overwrite authorized by this audit**

The candidate passes the independent provenance, identity, role, commander-style, framing, ownership, stable-consumer, and derivative-surface gates documented below. The parent still owns the atomic identity transfer, DDS conversion, runtime equality proof, and final `.gfx`/localisation/gameplay review.

## Audit scope and files checked

The trial package was inspected in full:

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/identity_repaint_prompt.md`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/source_masters/AJX_friedrich_von_rabenau_1937_master.jpg`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/source_crops/AJX_friedrich_von_rabenau_1937_head_shoulders.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/source_crops/AJX_friedrich_von_rabenau_1937_head_shoulders.json`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/imagegen_results/AJX_friedrich_von_rabenau_identity_preserve_trial_01.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/processed_png/portrait_AJX_saar_industrial_security_commissioner.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/processed_png/portrait_AJX_saar_industrial_security_commissioner.png.json`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_friedrich_von_rabenau_trial_01/review/AJX_friedrich_von_rabenau_commander_style_sheet.png`

The source-clearance authority and its complete package were checked:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_military_role_source_clearance_2026_07_25.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/ajx_military_role_clearance/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/ajx_military_role_clearance/manifest.json`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/ajx_military_role_clearance/ownership_audit.md`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/ajx_military_role_clearance/source_hashes.sha256`
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/ajx_military_role_clearance/gfx_handoff.md`
- Both clearance source masters, the clearance exact crop and equality JSON, the candidate contact sheet, and both Commons API/file-page research snapshots.

The canonical visual references and provenance instructions were checked:

- `.agents/skills/chaos-redux-event-assets/SKILL.md`, including the real-person, commander, ownership, independent-audit, and DDS boundaries.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/CATALOG.md`
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/REFERENCE_MANIFEST.md`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png` and all nine canonical commander PNGs.
- `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/contact_sheet.png` and all eight curated commander PNGs.
- The selected commander style controls `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png` were inspected directly.

The stable consumer surfaces were read without editing them:

- `common/characters/006_independence_wave_saar_characters.txt`, `AJX_karl_becker` block.
- `interface/006_independence_wave_region_01_portraits.gfx`, `GFX_portrait_AJX_karl_becker` block.
- `history/countries/AJX - Saar.txt`, `recruit_character = AJX_karl_becker`.
- `localisation/english/006_independence_wave_saar_l_english.yml`, current `AJX_karl_becker` display name.

## Hashes, dimensions, and decoded validation

All SHA-256 values listed by the trial `manifest.md` were recomputed independently and match. The trial source master, crop, and equality JSON are byte-identical to the corresponding clearance-package files.

| Artifact | Native dimensions / mode | SHA-256 | Independent result |
| --- | --- | --- | --- |
| `identity_repaint_prompt.md` | Markdown | `F0026D0198E1884A94412D3B82B37732863E855C7C3FA9414B9807E3FE3D088E` | Match |
| `source_masters/AJX_friedrich_von_rabenau_1937_master.jpg` | `581x800`, `L` | `F6B51E6B3A39E35734D67FA4DB4081C6DA26AEB40084569FF6747CD9ACA0480B` | Match; same as clearance master |
| `source_crops/AJX_friedrich_von_rabenau_1937_head_shoulders.png` | `520x700`, `L` | `B153E0310340D1EC5ED02484A52049C5D018767FEC6C5C525BA237B5803161E1` | Match; same as clearance crop |
| `source_crops/AJX_friedrich_von_rabenau_1937_head_shoulders.json` | JSON | `1C6824DF5F0F5400A66A121015132E37301BD9363E83FFEACC43F0CDC3D84719` | Match; equality record present |
| `imagegen_results/AJX_friedrich_von_rabenau_identity_preserve_trial_01.png` | `1086x1448`, `RGB` | `B352289AFAE5AD3C326E0B964582249BF3CC4E1B305D752FE6DAA3B9B917A1A9` | Match; metadata `source_sha256` matches |
| `processed_png/portrait_AJX_saar_industrial_security_commissioner.png` | `156x210`, `RGBA`, alpha `255/255` | `FEC2653228598C9E5A9F18292ECAA07528469AA9477DCB2FFF800F73E6E55627` | Match; exact target canvas |
| `processed_png/portrait_AJX_saar_industrial_security_commissioner.png.json` | JSON | `539CEA30D73B76810D5D4DDCC5AED86379B2FE684F42F08844AC735D30DE60E6` | Match; status remains unapproved |
| `review/AJX_friedrich_von_rabenau_commander_style_sheet.png` | `1344x464`, `RGBA`, alpha `255/255` | `F4478CB4339AF7B8971AB2D141AB3DAB01FA72CBD1AA5D1E573BD966EF45586D` | Match; review-only |
| `manifest.md` | Markdown | `C5049961D4C2EEBAF96E365CBCB2E3895FD32A7C5B4B2562844EB539ADC306FB` | Present; status and hashes reviewed |

The crop was independently decoded with Pillow from the trial master using the recorded half-open rectangle `(20, 30, 540, 730)`. The result is `520x700`, `364000` pixels, and `decoded_pixels_equal: true`; both RGBA byte digests are `fe18eb7636ddc8ec8ac3e078da7746f00bf451822c8c2b0d8e1d071f20be9bb8`. The trial equality JSON points to the canonical clearance paths, but the trial master, crop, and JSON bytes and hashes match those canonical files exactly.

The processor's domain-separated decoded-RGBA scheme was independently recomputed from the tool README and `the retired portrait-processing utility`. The raw ImageGen digest is `f4d90e00aa986afc14f9390337d7760e75d3c6a09331f99c6923a48c2a9b121b`, matching metadata `determinism.decoded_rgba_sha256`. The candidate digest is `96c790a415e354aea836b40dedbcc4f3df6f8f014b01e654841fb11b7ae6f62f`, matching both metadata and the trial manifest. The review-sheet digest is `7056fd2be48dcee1510ec0e7d8f1cf964d5bba7ebdad5860067b14e7f5debdf2`, matching metadata.

## Native and 4x nearest-neighbour visual review

The unchanged master, exact crop, raw repaint, deterministic candidate, review sheet, both role-specific contact sheets, all canonical commander references, and the selected Montgomery/Witzleben files were inspected at native size and at least `4x` nearest-neighbour enlargement. The review sheet is evidence only and does not replace this independent comparison.

### Identity-bearing feature comparison

- Eye opening and asymmetry: the darker viewer-left eye and narrower viewer-right aperture/gaze relationship remain readable in the raw repaint and candidate; there is no eye enlargement or forced symmetrization at native or enlarged view.
- Nose: the prominent straight bridge, central placement, tip, and nostril direction are retained; the painterly highlight changes tone but not the defining geometry.
- Moustache: the same compact, closed moustache and mouth line remain in place; tonal brush edges are slightly stronger than the monochrome source but do not materially widen or replace it.
- Jaw and face width: the narrow upper face, broad cheek planes, taper into the jaw, and small chin match the source crop; no beautifying roundness or substitute jaw is visible.
- Ears: the source-visible viewer-right ear and its protrusion are retained, while the shadowed opposite ear remains appropriately subdued.
- Hairline: the central part, receding temples, side direction, and source-visible hair mass are preserved.
- Expression: the closed-mouth, sober, slightly stern expression is retained without a smile or rejuvenating change.
- Pose: the same near-frontal head angle and shoulder orientation are retained; the candidate is not frontalized or rotated into a new pose.
- Neck and shoulders: the high collar, visible neck, both shoulders, and broad shoulder silhouette remain in the same frame relationship.
- Clothing and insignia: the dark German uniform, collar ornament, neck Iron Cross, shoulder decorations, and visible ribbon bar are retained from the source-visible presentation. The source is grayscale, so no color-specific historical claim is made; no extra medal, insignia, object, or hidden detail was introduced.

The raw repaint and candidate are a colorized painted interpretation rather than a filtered photograph, but the compared facial landmarks and source-visible pose remain the same person. Minor differences are brush highlights, color, and low-resolution rendering, not material identity drift.

## Gate results

| Gate | Verdict | Independent finding |
| --- | --- | --- |
| Provenance and rights | **PASS** | The authority records Bundesarchiv Bild 183-C05190, Dorneth for Scherl Bilderdienst, 13 April 1937, CC BY-SA 3.0 DE, with source page, direct original, attribution, archive snapshots, immutable master, and exact crop evidence. Trial bytes match the authority. |
| Male, historical, and role fit | **PASS with caveat** | Friedrich von Rabenau (1884-1945) is a real male German Army Generalleutnant and Heeresarchive chief alive in the 1936 setting. A broad German corps-command identity is defensible for the alternate-history AJX emergency state. The source does not document a Saarbrücken command or industrial-security office, and none is claimed. If the parent requires a historically Saar-specific commander, this role must remain blocked. |
| Exact likeness and identity | **PASS** | The non-compensable feature comparison above finds the eye asymmetry, nose, moustache, face width, ears, hairline, expression, pose, neck, shoulders, clothing, and visible insignia preserved at native and 4x review. Style quality was not used to excuse a feature change. |
| HOI4 painted commander style | **PASS** | The candidate is an opaque full portrait with restrained oil/gouache brushwork, controlled military palette, modeled planes, no photographic finish, no text, no watermark, no UI, and no modern prop. Its darker studio background is more subdued than the pale canonical references but remains readable and compatible with the commander family. |
| `156x210` framing | **PASS** | Candidate is exactly `156x210` RGBA with alpha `255/255`; full head, neck, both shoulders, collar, and source-visible decorations are inside the frame with no clipping or dossier-card treatment. |
| Subject ownership | **PASS** | The authority's five-root scan found no Rabenau character, recruit, leader, commander, operative, officeholder, portrait filename, sprite, or localisation owner in Chaos Redux, vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`. The current-project audit also found no live Rabenau token outside the evidence packages, so no transfer guard is required for the sourced identity. |
| Stable-consumer transfer requirements | **PASS for parent promotion; runtime proof pending** | The package names the existing `AJX_karl_becker` consumer, stable sprite `GFX_portrait_AJX_karl_becker`, and existing runtime path `gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds`. Both `civilian.large` and `army.large` use that sprite. Parent must atomically replace the fictional Karl Becker player-facing identity with Friedrich von Rabenau, keep the token/path stable, update the name/localisation contract, then convert and prove runtime equality. This audit does not authorize those writes. |
| Advisor/dossier/operative/commander-small/`_small` absence | **PASS** | The trial package contains only the source master/crop/equality evidence, prompt, raw repaint, full `156x210` candidate, processor metadata, review sheet, and manifest. No advisor, dossier, operative, commander-small, `_small`, female, generic, or fallback derivative exists in the package. Historical Event 6 `_small` references in older plan/evidence folders are not this candidate and must not be treated as its consumer. |

## Stable-consumer and runtime boundary

The existing target remains the single `AJX_karl_becker` character and its stable `GFX_portrait_AJX_karl_becker` large sprite. The candidate is suitable for both existing `civilian.large` and `army.large` consumers after the parent performs one atomic identity transfer; it is not a second character and does not authorize cloning Rabenau into another roster.

The current package intentionally has no DDS, no `.gfx` edit, no character transfer, no localisation edit, and no runtime/package equality proof. The parent must preserve the full commander surface, must not downsize this candidate into an advisor or `_small` card, and must obtain a fresh post-conversion/runtime audit if the package is promoted.

## Remaining risks and required parent actions

1. The role is alternate-history broad German corps command only. Do not describe Rabenau as a documented Saarbrücken commander or invent a Saar posting.
2. The trial crop-equality JSON retains canonical clearance-package paths rather than trial-relative paths. This is acceptable because the bytes and hashes match the authority, but the parent should retain the authority package as the provenance source of truth.
3. The candidate's dark textured background is more subdued than the pale vanilla commander references. It passed native readability and style-family review, but the parent should inspect the in-game portrait surface after conversion.
4. The live character and localisation still identify `AJX_karl_becker` as Karl Becker. Promotion requires an atomic player-facing identity transfer, not an additive Rabenau owner or a simultaneous fictional/source identity.
5. The package remains metadata-marked `candidate_requires_visual_approval` and manifest-marked `candidate_requires_independent_audit`; this handoff records the independent PASS but does not mutate those package statuses or create a DDS.

No simplification, fallback, generated substitute, invented Saar posting, advisor/dossier derivative, or runtime write was used.
