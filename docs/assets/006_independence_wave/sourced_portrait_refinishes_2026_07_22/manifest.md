# Event 006 sourced portrait HOI4 refinish ledger

Date: 2026-07-22

This review package records identity-preserving HOI4-style edits of sourced
real male portraits for grounded Independence Wave packages. Image generation
is used only to repaint and recompose an attributed archival subject; it does
not authorize a generated substitute identity. Every subject must already pass
the source-rights, 1936 role, regional fit, and vanilla/Chaos Redux ownership
gates in the linked source manifest.

Nothing in this folder is a runtime asset until the source identity and the
painted likeness have been independently reviewed at native `156x210` scale.
The protected Rupprecht of Bavaria and Josef Friedrich Matthes portraits are
outside this package and must not be overwritten.

## Karl Jarres — Rhenish civic leader

- Intended sprite: `GFX_portrait_RHI_independence_wave_provisional_directorate`
- Grounded role: civic, constitutional, municipal, and patron-facing Rhenish
  leader for `IW-008 RHI`.
- Subject authority: Karl Jarres (1874–1951), alive in 1936 and not found as an
  active vanilla or Chaos Redux character in the bounded ownership audit.
- Primary source: `../sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_masters/RHI/RHI_karl_jarres_bundesarchiv_1925.jpg`,
  Bundesarchiv Bild 102-01175, 1925, CC BY-SA 3.0 Germany, SHA-256
  `72c952b0f1a1e3c08a16b20c123466b4bfc737d7c03ae63594cf7e6332c2c8d6`.
- Identity cross-check: `../sourced_portrait_replacements_2026_07_22/active_vanilla_conflict_retry/source_masters/RHI/RHI_karl_jarres_loc_undated.jpg`,
  Library of Congress Bain collection, no known restrictions, SHA-256
  `d07eb103f4c5fdf13ca06c9d58fdea2f626c14f82060d2b2d92b740df633b36e`.
- Style reference: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/contact_sheet.png`;
  style and framing only, never an identity source.
- Trial source: `imagegen_sources/RHI/RHI_karl_jarres_hoi4_trial_01.png`,
  `1080x1456`, SHA-256
  `2a3181b5736f30e60a4e1962646cd98918774ae36ab0e162c5c78db6de4311d3`.
- Refined source: `imagegen_sources/RHI/RHI_karl_jarres_hoi4_refined_02.png`,
  `1080x1456`, SHA-256
  `473e0574639ad7a8b32355a5d2c821c7982c0927607faf96884e8b9854dcc49f`.
- Processed review PNG: `processed_png/RHI/RHI_karl_jarres_hoi4.png`,
  `156x210`, SHA-256
  `af560fe69f990e0e6da26f03c9fcc62f55f43077b514b0fb3b33fa3605ad9933`.
- Processing: `1070x1440` crop at source offset `x=5, y=0` from the refined
  `1080x1456` master, then Lanczos resize to `156x210`; no post-generation face
  edit, filter, frame, or dossier treatment.
- Current disposition: `rejected_visual_likeness_pending_revision`. Independent
  audit found that the painted face remained too broad, smooth, symmetrical,
  and generic against both Jarres photographs; the hat was overbuilt and the
  background too dark/olive for the vanilla leader family. Do not convert or
  wire this candidate. See
  `../../plans/006_independence_wave_plans/subagent_handoffs/006_karl_jarres_refinish_visual_audit_2026_07_22.md`.

### Generation instructions retained

The first pass used the Bundesarchiv photograph as the sole identity source
and the curated leader contact sheet only for HOI4 finish and framing. The
refinement used both Jarres photographs to correct facial drift while retaining
the successful painted composition. Both prompts explicitly prohibited a new
person, beautification, de-aging, facial-hair or glasses changes, invented
uniforms or insignia, flags, text, frames, props, fantasy elements, and other
people.

### Revision 03 after independent rejection

- ImageGen master: `imagegen_sources/RHI/RHI_karl_jarres_hoi4_revision_03.png`,
  `1081x1455`, SHA-256
  `4276f09d7218c6ad09c6d2c91576d0f95521c06b897cd4d537a282c7249f4cff`.
- Native review PNG: `processed_png/RHI/RHI_karl_jarres_hoi4_revision_03.png`,
  `156x210`, SHA-256
  `90f395c882ba42f577a44228713125ff2d278698c970dce152348d90d80fe3c9`.
- Processing: `1080x1454` crop at `x=0, y=1` from the `1081x1455` master,
  then Lanczos resize to `156x210`. The crop leaves one source pixel on the
  right; this exact offset is recorded rather than described as centered.
- Corrective direction: the LOC portrait was made the primary face authority;
  the Bundesarchiv image remained the age, hat, coat, collar, and tie authority.
  The prompt explicitly targeted Jarres's long narrow face, hooded asymmetric
  eyes, narrow jaw, thin guarded mouth, restrained hat/brim, pale warm-gray
  background, and quiet vanilla texture.
- Current disposition: `rejected_visual_likeness_pending_revision`. Independent
  review found that the face still reads as a generic substitute without the
  hat, while the hat and lapels remain overbuilt against the archival sources.
  Do not convert or wire it. See
  `../../plans/006_independence_wave_plans/subagent_handoffs/006_jarres_revision03_cachin_trial01_visual_audit_2026_07_22.md`.

## Marcel Cachin — Breton labor-route candidate only

- Runtime sprite: none. He must not be assigned to
  `GFX_portrait_BRI_independence_wave_civic_commission`.
- Grounded role boundary: source and visual candidate for a future explicit
  Breton labor-route character only. The current civic token leads the
  oligarchic traditional or patron route, which does not fit Cachin's
  socialist and communist political career.
- Subject authority: Marcel Cachin (1869–1958), born in Paimpol, alive in 1936,
  and not found as an active vanilla or Chaos Redux character in the bounded
  ownership audit.
- Source: `../sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/source_masters/BRI/BRI_marcel_cachin_gallica_meurisse_1918.jpg`,
  BnF/Gallica Agence Meurisse, 1918, documented public-domain/PD-US-expired
  basis, SHA-256
  `85fa2c4d485bddde3e5fee903f52a3dc8f91f53f22159b38e1a62164f024e2a9`.
- ImageGen master: `imagegen_sources/BRI/BRI_marcel_cachin_hoi4_trial_01.png`,
  `1080x1457`, SHA-256
  `b623484563b1efb19fdf466cd4f6bc7eaf2f3fab7ca8396eff7dd294be34dd24`.
- Native review PNG: `processed_png/BRI/BRI_marcel_cachin_hoi4_trial_01.png`,
  `156x210`, SHA-256
  `225ce2f8eaf8092ba63a481e200f70d0dad20df67bf1a5b4fc56c8e8bc02bf7f`.
- Processing: `1080x1454` crop at `x=0, y=1` from the `1080x1457` master,
  then Lanczos resize to `156x210`; two source pixels remain below the crop.
- Identity controls: the Gallica portrait was the only facial and clothing
  authority. Jarres and the curated leader contact sheet supplied only finish
  and framing. The prompt required Cachin's high forehead, swept-back hair,
  arched brows, wide eyes, long rounded nose, large curled moustache, long jaw,
  serious expression, dark suit, white collar, and tie; it prohibited any
  generated substitute, beautification, de-aging, uniform, insignia, text,
  prop, or additional person.
- Current disposition: `visually_approved_role_rejected_for_current_token`.
  Independent review approved the identity-preserving HOI4 treatment at full
  and native scale, but the gameplay-role audit rejects Cachin for the current
  traditional/patron civic token. Retain this as labor-route evidence only;
  do not convert or wire it to the current package. See
  `../../plans/006_independence_wave_plans/subagent_handoffs/006_jarres_revision03_cachin_trial01_visual_audit_2026_07_22.md`.

## Henri-Léon Devin — Breton coastal commander

- Intended sprite: `GFX_portrait_BRI_independence_wave_coastal_commandant`.
- Grounded role: Joint Coastal Command for `IW-004 BRI`. Devin commanded the
  École navale at Brest from September 1930; the package does not present him
  as maritime prefect before his September 1936 appointment.
- Source: `../sourced_portrait_replacements_2026_07_22/bri_ajx_rights_clear_retry/source_masters/BRI/BRI_leon_henri_devin_brest_prefet_1930.jpg`,
  BnF/Gallica Agence Rol, 1930, documented PD-1996/PD-France basis, SHA-256
  `ab7d69e6f485be51bfc02823bf94187a9239b54f56525ff97223c9e7b2f7e4c0`.
- ImageGen master: `imagegen_sources/BRI/BRI_henri_leon_devin_hoi4_trial_01.png`,
  `1081x1455`, SHA-256
  `b30ffff5a4bcb82d66f2ac4b8c06421ada4b51b505bc575aa805b609beb0f542`.
- Native review PNG: `processed_png/BRI/BRI_henri_leon_devin_hoi4_trial_01.png`,
  `156x210`, SHA-256
  `7b9e9bf849dd8deeb45c7de9044b31af5429053aa501a18813700038b93cca2c`.
- Processing: `1080x1454` crop at `x=0, y=1` from the `1081x1455` master,
  then Lanczos resize to `156x210`. The crop leaves one source pixel on the
  right; this exact offset is recorded rather than described as centered.
- Identity controls: the Gallica portrait was the only authority for Devin's
  face, age, expression, moustache, cap, anchor device, shoulder boards,
  double-breasted coat, buttons, and visible ribbon arrangement. Cachin and the
  curated commander contact sheet supplied only finish and framing. The prompt
  prohibited any generated substitute, changed facial geometry, invented or
  altered decorations, flags, text, frames, props, or additional people.
- Current disposition: `rejected_uniform_fidelity_pending_revision`. Independent
  review found the face recognisable, but the repaint introduced unverified
  colored ribbon/trim details, brightened rank decoration, a dark olive
  background, and harsher texture than the canonical HOI4 commander family.
  Do not convert or wire it until a source-faithful revision passes review. See
  `../../plans/006_independence_wave_plans/subagent_handoffs/006_jarres_revision03_cachin_trial01_visual_audit_2026_07_22.md`.

### Revision 02 after uniform-fidelity rejection

- ImageGen master:
  `imagegen_sources/BRI/BRI_henri_leon_devin_hoi4_revision_02.png`,
  `1082x1454` RGB, SHA-256
  `d9cfdce881cde859a6d1aa46787fdd4f5f2a13acb7ac4d7528414cb60cdfcc52`.
- Native review PNG:
  `processed_png/BRI/BRI_henri_leon_devin_hoi4_revision_02.png`,
  `156x210` RGB/opaque, SHA-256
  `2ab9fe7986964db30b5b3553268739097168a92f4becf0ae07cabddb9b891bae`.
- Processing: centered `1080x1454` crop at `x=1, y=0` from the
  `1082x1454` master, then Lanczos resize to `156x210` with no filter, frame,
  dossier treatment, or post-generation face edit.
- Corrective direction: the unchanged Gallica photograph remained the sole
  authority for Devin's face, age, expression, cap, badge, band spacing,
  shoulder boards, coat, buttons, and two visible ribbon rows. The curated
  commander sheet controlled only the restrained painted finish, native
  readability, and pale warm-gray/cream background. Because the source is
  grayscale, all uncertain trim, insignia, and ribbon details were explicitly
  constrained to neutral charcoal, silver-gray, off-white, and muted sepia;
  no award color or medal meaning was inferred.
- Independent audit: `approved_visual_source_only`. Full-size and native review
  confirmed the same-person likeness, age and expression, source-supported cap,
  anchor and band structure, shoulder boards, coat and buttons, both neutral
  ribbon rows, pale background, readable crop, and restrained HOI4 finish. See
  `../../plans/006_independence_wave_plans/subagent_handoffs/006_devin_revision02_visual_audit_2026_07_22.md`.
- Final DDS:
  `final_dds/BRI/portrait_BRI_independence_wave_coastal_commandant.dds`,
  `156x210` BGRA, one mip, SHA-256
  `0806f9560139ea1dbc30ff4385b16e829560d85bcddd15a91a294b28d39802fb`.
- Runtime DDS:
  `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds`,
  byte-identical SHA-256
  `0806f9560139ea1dbc30ff4385b16e829560d85bcddd15a91a294b28d39802fb`.
- Runtime sprite:
  `GFX_portrait_BRI_independence_wave_coastal_commandant` in
  `interface/006_independence_wave_brittany_portraits.gfx`; the existing stable
  sprite name and path required no interface edit.
- Current disposition: `approved_and_wired`. The character localisation names
  Henri-Léon Devin and describes his École navale command at Brest without
  prematurely calling him maritime prefect. No advisor, dossier, miniature,
  `_small`, or generated substitute asset was created.

## Régis de l'Estourbeillon — Breton regionalist civic leader

The `bri_regionalist/` package supplies the approved source-preserving portrait
for the traditional and patron-facing Brittany civic token. Its unchanged
identity source is John Wickens's 1904 photograph of de l'Estourbeillon in
Breton national costume, retained with source, publication, authorship,
public-domain, and ownership-search evidence. ImageGen edited only that sourced
person into the full-color restrained HOI4 leader style. Independent review
passed likeness, male-only, role, crop, costume, provenance, style, and native
readability gates.

- Processed v3 PNG:
  `bri_regionalist/processed_png/leader_bri_regionalist_regis_de_l_estourbeillon_v3.png`,
  `156x210`, SHA-256
  `5426E39BC1622E7ECD32A41CC0A1C05D6596446A40FA0B7BA2047EF350BBAE80`.
- Package DDS:
  `bri_regionalist/final_dds/BRI/portrait_BRI_independence_wave_civic_commission.dds`.
- Runtime DDS:
  `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`.
- DDS SHA-256:
  `583F821ED7F8B78A89321DBB7E1E7B7CAD7E30829DFA5DD14B6F255E42E27DC0`;
  package and runtime files are byte-identical.
- Stable sprite:
  `GFX_portrait_BRI_independence_wave_civic_commission`; no new sprite,
  advisor, dossier, miniature, `_small`, female, or substitute identity was
  added.

## Eugen Ritter von Schobert — blocked repaint attempt

The source-ready Schobert master remains valid source evidence for Bavaria's
military role, but two identity-preserving ImageGen edit attempts were rejected
by the image service before producing output. No generated file, substitute
identity, deterministic photographic treatment, PNG, DDS, or runtime overwrite
was created. A different rights-clear real Bavarian officer may be researched,
or the same source may be revisited only if the image service can process it
without weakening the identity gate.

## Frisia — both first refinishes rejected

The Douwe Kalma civic-leader and Pieter Reenalda maritime-command refinishes
under `frisia/` are both `rejected_material_face_drift`. They satisfy the male,
grounded-source, provenance, crop, period, and broad HOI4-style checks, but the
painted faces materially diverge from their attributed masters. No DDS or
runtime overwrite is authorized. The independent evidence is recorded in
`../../../plans/006_independence_wave_plans/subagent_handoffs/006_frisia_refinishes_visual_audit_2026_07_22.md`.

## Frisia retry 02 — sourced portraits approved and wired

The separate `frisia_retry_02/` package uses stronger exact archival masters
for Douwe Kalma and Pieter Reenalda. Its independent visual audit passes Kalma
and Reenalda candidate 02 for same-person likeness, sourced real-male policy,
period role, head-and-shoulders crop, and restrained full-color HOI4 painted
finish at native `156x210`. Reenalda candidate 01 remains fail-closed. The two
approved PNGs were converted to the existing Event 006 AGX texture paths with
stable sprite names; both DDS files are 131168-byte one-level BGRA textures and
decode pixel-identically to their approved PNGs. IW-007 remains outside the
compile-time attestation until its fresh post-wiring country-package audit.

## Admission boundary

No generated face may be used for a grounded Event 006 country. A generated
one-person identity is permitted only for a wholly fictional, explicitly
high-chaos polity whose leader is also fictional; none of the current
206 registry rows meets that condition. Event 006 has no advisor portrait or
advisor icon requirement.
