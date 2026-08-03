# IW-030 Montenegro grounded male portrait source admission handoff

Date: 2026-08-03.

Subagent: `/root/event6_montenegro_source_research_next`.

Scope: sourced archival portrait research, provenance, era/role fit, crop evidence, and source-only roster admission review for Event 006 IW-030 Montenegro.

No gameplay, character, history, localisation, flag, `.gfx`, DDS, attestation, or runtime file was edited.

## Final verdict

`SAFE_PACKAGE_PROMOTION = NO`.

The three original vanilla MNT consumers do not form a fully promotable sourced roster: Jovanovic now has a stronger named archival source but still needs the source-locked repaint and independent portrait audit, Dukanovic remains rights-review pending, and the Popovic source remains blocked.

The parent-approved role-correct replacement is the distinct identity `MNT_mitar_martinovic`, not a relabel of `MNT_kristo_popovic`.

Martinovic's v91 independent portrait audit records identity and source-linkage passes, a style pass with a note, a rights pass with a note, and an overall `needs_user_review` state because human style approval, identity ownership, and parent runtime wiring remain open.

No face may be assigned to a different MNT identity, and no evidence candidate may be converted to DDS or wired to runtime from this handoff.

## Roster disposition

| Intended consumer | Grounded subject | Source and role finding | Admission state | Runtime decision |
| --- | --- | --- | --- | --- |
| `MNT_blazo_jovanovic` | Blažo Jovanović (1907–1976), Montenegrin partisan leader and corps-commander consumer | The new Znaci/Commons record is dated 1942-05-25, explicitly names Jovanović as the third man in the lower row, credits Savo Orović, and links the Museum of the Revolution of the Peoples of Yugoslavia archive. | `source_identity_pass_needs_visual_repaint_review`; archival identity/date/rights evidence is materially stronger, but group context and the full real-person repaint/audit gate remain open. | Keep the existing Livno candidate evidence-only and do not promote the new crop until source-locked repaint, likeness/style/provenance audit, and parent rights review pass. |
| `MNT_blazo_dukanovic` | Blažo Đukanović (1883–1943), Yugoslav military officer and fascist-route country-leader/corps-commander consumer | Existing Commons portrait is explicitly identified and estimated 1938–1940, close to the 1936 start; the source is a book reproduction with an unknown photographer. | `needs_user_review`; exact crop, source linkage, visual likeness, male framing, and HOI4 style are recorded as passes, while the unknown-photographer/book chain remains unresolved. | No DDS, sprite, or runtime wiring until rights/provenance is independently cleared. |
| `MNT_kristo_popovic` | Krsto Zrnov Popović (1881–1947), Montenegrin Army general and oligarch-route country-leader/corps-commander consumer | The Commons portrait has no machine-readable author, source, or date; the Montenegrina lead lacks a defensible redistribution chain. | `BLOCKED_PROVENANCE`. | Do not use the generic texture as an accepted sourced portrait and do not relabel a Jovanović, Đukanović, Martinović, or Danilo face as Popović. |
| Event 006 amendment | Mitar Martinović (1870–1954), Montenegrin divisional general, former prime minister and minister of war, and Lovćen Detachment commander | The parent-approved identity amendment uses a new stable identity, with a 1912 *Ilustrovana ratna kronika* archival source and a complete source-locked evidence package. | `needs_user_review` after v91 independent audit; identity/source linkage pass, style/rights pass with notes, runtime ownership pending. | Continue only under an explicit `MNT_mitar_martinovic` identity after human style approval and parent-owned character/GFX/runtime work. |

## New higher-resolution Jovanović source

Commons page: <https://commons.wikimedia.org/wiki/File:Grupa_boraca_i_rukovodilaca_iz_Crne_Gore%2C_Lipova_Ravan%2C_25._maja_1942.jpg>.

Canonical source URL: <https://upload.wikimedia.org/wikipedia/commons/3/38/Grupa_boraca_i_rukovodilaca_iz_Crne_Gore%2C_Lipova_Ravan%2C_25._maja_1942.jpg>.

The Commons description gives the exact date `1942-05-25` and identifies the lower row as “Mirko Stanišić, Radomir Babić, Blažo Jovanović, Ratko Radović,” placing Jovanović third from the left.

The Commons record credits Savo Orović and `https://znaci.org/fotografija.php?br=8889` and labels the image Public domain under the `PD-Yugoslavia` framework.

The Znaci record identifies the source as the Museum of the Revolution of the Peoples of Yugoslavia and states that its archival photographs, documents, and materials are public domain unless otherwise noted.

Commons creator metadata names Savo Orović, while the upload history describes the original photographer as unknown; this discrepancy is retained as a rights-review uncertainty rather than silently converted into unconditional clearance.

The subject is in an active-life wartime setting at age 35, which is historically compatible with a grounded adult-male MNT roster but is later than the 1936 scenario start.

## Immutable local evidence

Source master: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/source_masters/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942.jpg`.

The unchanged master decodes to 2083x1380 grayscale (`L`) and has SHA-256 `919393b924cee9c6de3d1e1fd4e864b4ffed387a3fe60fd52c43bc58b6d682a4`.

Exact crop: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/source_crops/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_head_shoulders_v2.png`.

The crop rectangle is `[left=1040, top=500, right=1490, bottom=1200]` in decoded master pixels, producing a 450x700 grayscale (`L`) crop with SHA-256 `e96c730d6d82702ea2937c1ff3bfa46b9d998921784aae2bf5be435a336cd737`.

The crop proof is `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/crop_metadata/mnt_blazo_jovanovic_znaci_8889_lipova_ravan_1942_crop_v2.json`.

The proof was generated with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` v1.0 and reports `status=exact_source_crop_verified`, `decoded_pixels_equal=true`, and equal decoded RGBA hash `ba2531b4c6c576cef56a6d1547044d0901f40b7e21fdba26534c61e51a3f5883`.

The source crop is evidence only and has not been resized into runtime, repainted, converted to DDS, or referenced by a sprite.

## Visual suitability finding

The lower-row moustached subject is readable at native source scale and provides a materially better face crop than the earlier 1271x922 derivative.

The crop retains source-visible cap, rifle, shoulder strap, adjacent people, and group context, so the next repaint must preserve the face and visible uniform evidence without inventing unsupported decorations or silently deleting identity-bearing structure.

The crop is suitable for a new source-locked repaint trial, not for direct runtime use.

The source comparison sheet is `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v53_2026_08_01/review/mnt_portrait_source_admission_contact_sheet_2026_08_03.png`.

The sheet is 1290x760 RGB with SHA-256 `9c6606f0522cd5afbf31da2c6e6739186996a82060b1e96e0ced240260dbfdb4` and compares the new crop, prior Livno crop, Dukanović crop, new full group, direct Jovanović corroboration, and Dukanović master.

## Existing replacement evidence

The approved replacement source is Mitar Martinović, not Popović under a new label.

The immutable Martinović source is `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/source_masters/mnt_mitar_martinovic_1912_chronicle.jpg` with exact crop `source_crops/mnt_mitar_martinovic_1912_head_shoulders.png` and equality proof `crop_metadata/mnt_mitar_martinovic_1912_crop.json`.

The source is a 1912 publication by Izdavačka knjižarnica Svetozara F. Ognjanovića, Novi Sad, extracted from *Ilustrovana ratna kronika III broj.pdf*, and the package records the Commons `PD-collective-work|Serbia` basis with the archive site-terms caveat.

The v91 audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw030_mnt_portrait_audit_v91_2026_08_02.md` prefers the v7 candidate but keeps the overall state `needs_user_review` pending human style approval and parent ownership/runtime admission.

Danilo Aleksandar Petrović-Njegoš remains a non-selected alternate lead with a named Carl Vandyk 1911 source and Library of Congress corroboration in `iw030_mnt_portrait_source_research_v107_2026_08_02`; it requires a separate explicit identity decision and must never be assigned to Popović, Jovanović, Đukanović, or the unrelated `YUG_danilo_kalafatovic` owner.

## Historical MNT identity and flag note

The relevant historical identity reference is the Kingdom of Montenegro, whose 1905–1918 flag is documented at <https://commons.wikimedia.org/wiki/File:Flag_of_Montenegro_(1905%E2%80%931918).svg> and carries a public-domain official-flag basis.

The reference is a historical identity aid only: red-blue-white horizontal bands with the royal double-headed-eagle coat of arms are appropriate research context for a royal Montenegrin route, but no flag asset was selected, processed, or promoted in this handoff.

## Required next gates

1. Parent reviews the new Jovanović source chain and explicitly accepts the rights uncertainty or marks the candidate blocked.
2. If accepted, run the grounded real-person sequence from the new exact crop: source-locked identity-preserving repaint, deterministic 156x210 processing, and independent likeness/style/provenance audit against canonical leader/commander references.
3. Resolve the Dukanović unknown-photographer/book-reproduction rights chain before any DDS conversion.
4. Complete Martinović human style approval and parent-owned identity/character/runtime admission before using it as the explicit Popović-role replacement.
5. Convert to repository-standard DDS and wire `.gfx` only after every live MNT consumer has an admitted identity, source, rights, visual audit, and ownership result.

No fallback, generic acceptance, relabeling, generated officeholder, flag edit, gameplay patch, or runtime shortcut is authorized.

