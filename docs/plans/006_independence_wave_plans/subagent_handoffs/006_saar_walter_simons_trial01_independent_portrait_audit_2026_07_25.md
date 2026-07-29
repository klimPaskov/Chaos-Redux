# IW-010 Saar Walter Simons trial-01 independent portrait audit

Date: 2026-07-25.

Reviewer: independent sourced-visual audit subagent.

Decision: `PASS`.

Disposition: `approved_for_parent_promotion`.

Runtime authorization: export and atomic identity transfer remain parent-owned and are not performed by this audit.

## Audit scope

This audit covers only `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/saar_walter_simons_trial_01/`.

The compared artifacts were the unchanged archival master, exact crop, crop-equality JSON, repaint prompt, raw ImageGen repaint, processed `156x210` candidate, processing metadata, and review sheet.

The role-specific references were the canonical Vanilla HOI4 leader contact sheet plus `den_thorvald_stauning.png` and `fin_carl_mannerheim.png` selected by the processor.

No DDS, GFX, interface, character, history, localisation, source-package, or runtime file was edited.

## Source and role authority

The source-clearance authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_saar_two_role_source_clearance_2026_07_24.md`.

The grounded identity is Walter Simons (1861–1937), an independent constitutional civic figure from the Prussian Rhine Province who served as Weimar Foreign Minister, president of the Reichsgericht, and acting head of state.

The source is Bundesarchiv Bild 102-12279, dated September 1931, from [the Wikimedia Commons source page](https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-12279,_Walter_Simons.jpg).

The recorded attribution is `Bundesarchiv, Bild 102-12279 / CC-BY-SA 3.0` under the German Federal Archive / Wikimedia Commons cooperation licence basis.

The source clearance supports a civic, municipal, legal, or constitutional alternate-history role for the Saar and does not claim that Simons historically chaired an independent Saar commission.

The source-clearance ownership scan found no meaningful Walter Simons character, portrait, recruit, or localisation owner in the current Chaos Redux tree, vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`.

The stable consumer named by the trial package is `AJX_friedrich_hoffmann` using `GFX_portrait_AJX_friedrich_hoffmann` through `civilian.large` at `gfx/leaders/006_independence_wave/portrait_AJX_saar_municipal_neutral_commission.dds` after parent promotion.

## Independent provenance and hash evidence

The independent audit recomputed file hashes, decoded dimensions, modes, alpha coverage, crop equality, and the repository domain-separated decoded-RGBA hashes.

| Artifact | Decoded dimensions and mode | File SHA-256 | Domain-separated decoded-RGBA SHA-256 |
| --- | --- | --- | --- |
| `source_masters/AJX_walter_simons_1931_master.jpg` | `558x800 RGB` | `789961bc6505993f4a6441979ca4d1f247609531d23cfb8d7088ccc2d4a170b3` | `a8dfd8934d31e92262bf70742545d937994b6cda9af8c8dc23d9bac70fd42f37` |
| `source_crops/AJX_walter_simons_1931_head_shoulders.png` | `465x605 RGB` | `2b1c394da30f31f0e81b35cd6740cc0e0235a71326fdc976cce9f0217688efd7` | `0d186f35cde5f03f4703b49753e8d927c3087f3f792f6a9fd34d468cece9d85e` |
| `imagegen_results/AJX_walter_simons_identity_preserve_trial_01.png` | `1082x1453 RGB` | `dd0b7b274a6e07402991ef0bbed93f7077701c342c372e4a1426fb642aa6c80d` | `b6bca402c7965b896f8e24838f8e3edbf19e57670683a80cb3ec7cfe4aed1541` |
| `processed_png/portrait_AJX_saar_municipal_neutral_commission.png` | `156x210 RGBA`, alpha `255..255` | `a7de632090ad42ecdad19583a7b76de3b3231e75d597e1efed06486a801a9e04` | `436641a4292f9bb5fb93cbe25e3b43adeac1a46cadb0b05c1edd045145bbf1b0` |
| `review/AJX_walter_simons_leader_style_sheet.png` | `1344x464 RGBA`, alpha `255..255` | `8ffed31089d54489aa6dcfa959046563ce9393866294c9b4d4a8b288473e9684` | `0b09d5b437e425a7cb1df348e90c983d6e7efe175cd7fc5c72e1da70d1a558c8` |

The raw repaint metadata `source_sha256` matches the independently recomputed raw file hash.

The candidate metadata file hash is `602287c33dc1c412da0d7fbaa2a522a88485e136e0f22d69f825273fd29fe0b7`, and its recorded output file and decoded-RGBA hashes match the independent recomputation.

The review-sheet metadata file and decoded-RGBA hashes also match the independent recomputation.

The trial master is byte-identical to the cleared master `AJX_walter_simons_bundesarchiv_1931.jpg`, and the trial crop is byte-identical to the cleared crop `AJX_friedrich_hoffmann_walter_simons_1931_head_shoulders.png`.

The explicit crop rectangle is half-open `(55,45,520,650)` in decoded master pixels.

Independent Pillow verification produced `465x605`, `281325` pixels, `decoded_pixels_equal: true`, and matching master/output RGBA digest `9bebecbd0362fa5dc39ec8b1ce4271671c32ced58db3a7b8eec078410161bdc7`.

The crop JSON and source package preserve the canonical equality evidence rather than replacing the immutable source with a resized or filtered image.

The processor is `the retired portrait-processing utility` version `5.0` in positional `leader` mode with role family `leader`, source kind `real`, raw crop `(1,0,1080,1453)`, and deterministic output `156x210`.

## Visual review method

I inspected the master, exact crop, raw repaint, candidate, and review sheet at native resolution.

I inspected the same artifacts at `4x` nearest-neighbour enlargement, including the candidate face and source-visible details.

I inspected the canonical leader contact sheet and the selected Stauning and Mannerheim references at native resolution and `4x` nearest-neighbour enlargement.

The temporary enlarged audit renders were created outside the repository and are not source or runtime assets.

## Separate gate scores and verdicts

Provenance and crop traceability: `5/5 — PASS`.

Identity likeness: `5/5 — PASS`.

HOI4 country-leader portrait style: `4/5 — PASS`, with a dark-background review note that does not override the identity gate.

Framing and runtime canvas: `5/5 — PASS`.

Consumer and ownership boundary: `PASS` for parent promotion, with final runtime proof still pending.

Identity is treated as a non-compensable gate; the style result was not used to excuse any identity drift.

## Identity likeness findings

The candidate keeps Walter Simons recognizable as the same older man in the 1931 source, with no substitute face or generic officeholder treatment.

- Moustache: the source's thin, drooping, slightly asymmetric moustache remains the same shape and placement; painterly strokes increase local contrast but do not materially curl, widen, or replace it.
- Eyes: the unequal eye openings, eyelid shapes, spacing, asymmetrical shadowing, and slightly off-centre gaze remain; neither eye is equalized or enlarged.
- Brows and forehead: the deep brow folds and very high receding forehead remain visible in the raw repaint and survive the `156x210` candidate.
- Nose: the long narrow bridge, downward tip, and nostril orientation remain consistent with the source.
- Facial width and cheeks: the long narrow head, hollow under-eye and cheek planes, tapering jaw, and small chin remain; the repaint does not round or broaden the face.
- Hairline: the high receding hairline, thin side hair, and side-part direction remain consistent with the source.
- Ears: the visible ear's placement and outer shape remain consistent, with no invented or reshaped ear detail.
- Age and expression: forehead lines, under-eye hollows, guarded gaze, closed mouth, and older age presentation remain; there is no material beautification, rejuvenation, or smile substitution.
- Pose: the same restrained three-quarter head angle and shoulder orientation remain.
- Clothing: the high white collar, dark bow tie, and civilian coat remain source-visible and unchanged in identity terms; no unsupported insignia or hidden clothing detail was added.

The candidate is an actual muted oil-and-gouache repaint rather than a raw photograph, colourized photograph, or simple filter pass.

## HOI4 leader-style findings

The candidate is a full `156x210` head-and-shoulders country-leader portrait with the full head and both shoulders inside the frame.

The subdued oil/gouache brushwork, modeled facial planes, restrained contrast, and period civilian clothing fit the canonical Stauning and Mannerheim leader family.

The dark textured studio background is less pale than the selected vanilla references but remains readable, uncluttered, period-neutral, and compatible with the leader surface.

There is no text, border, watermark, UI, modern object, caricature, or cinematic effect.

The candidate is fully opaque and is not an advisor, dossier, operative, commander-small, `_small`, generic, or fallback portrait.

## Gate table

| Gate | Verdict | Evidence or boundary |
| --- | --- | --- |
| Attributed real-person source | `PASS` | Bundesarchiv Bild 102-12279, September 1931, CC BY-SA 3.0 basis with recorded attribution. |
| Immutable source master | `PASS` | Trial master is byte-identical to the cleared `558x800` RGB master. |
| Exact source crop | `PASS` | `(55,45,520,650)` Pillow crop, `465x605`, equality proof true, matching RGBA digest. |
| Source-locked repaint | `PASS` | Raw repaint is retained separately and visibly follows the source face, pose, age, clothing, and composition. |
| Identity likeness | `PASS` | Moustache, eyes, face width, cheeks, nose, hairline, ears, age, expression, and pose remain source-consistent at native and `4x`. |
| HOI4 leader style | `PASS` | Restrained oil/gouache full-size leader portrait; dark background is a review note only. |
| Canvas and framing | `PASS` | Candidate is opaque `156x210` with full head and both shoulders. |
| Ownership | `PASS` | Prior five-root scan found no conflicting Walter Simons owner. |
| Runtime boundary | `PASS` for parent promotion | Parent must perform the atomic Friedrich Hoffmann → Walter Simons identity/localisation transfer and prove the final DDS path and sprite. |
| DDS/runtime completion | `PENDING` | No DDS or runtime edit is present or authorized in this audit package. |

## Parent promotion boundary and remaining risks

The current stable consumer remains the fictional `AJX_friedrich_hoffmann` with `GFX_portrait_AJX_friedrich_hoffmann` and player-facing name `Friedrich Hoffmann` until the parent performs the atomic transfer.

The parent must update the consumer identity and localisation to Walter Simons without changing the approved image, source attribution, or civic role boundary.

The parent must convert this exact candidate with the repository-standard DDS converter and verify the resulting runtime texture at native size.

The parent should inspect the converted DDS for excessive darkness because the candidate uses a dark textured background.

The source crop JSON retains canonical clearance-package paths by design; its bytes, hashes, dimensions, and equality evidence independently match the trial source files and the cleared package.

The trial package manifest still says `candidate_requires_independent_audit` and the processing metadata still says `candidate_requires_visual_approval`; this handoff records the independent PASS without mutating either source package file.

## Simplifications, omissions, and blockers

No simplification, fallback, generic substitute, invented historical role, unsupported clothing, or identity substitution was used.

The portrait is approved for parent promotion but is not a shipped runtime asset until the parent completes the atomic consumer transfer, final licence attribution review, DDS conversion, and runtime/package equality proof.
