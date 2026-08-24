# Event 014 Siege Eaters v8 ImageGen prompt lock

Source mode: `reference_only_user_authorized_source_informed_refinement` from the official Gamefound/Chip Theory source recorded in `refs/source/recovery_v8/provenance.json`.

Final provider input: `refs/original/meshy_input.png`, SHA-256 `1AC18B9B008CCCC70BC0AF30605CA72ADCC9030A1C233732559400C9A6744F75`.

## Prompt

Use case: faithful model-ready background extraction and cleanup of the supplied exact character artwork. Preserve the exact full-body living warrior's identity, anatomy, proportions, face, expression, horned skull headdress, bone-and-leather armor, clothing, footwear, plates, spikes, exact massive two-handed spiked mace, both hands, and exact overhead pose. Remove only the scene, floor or display base, cast shadow remnants, text, decorative flecks, and compression artifacts. Clean and upscale without redesigning the armor or weapon. Add conspicuous irregular culturally neutral charcoal-black and muted iron-red fictional siege stripes to exposed face and body, plus restrained dried blood, dust, and grime. Return one fully colored isolated subject with the entire mace, hands, body, and feet visible on a genuine transparent RGBA background with clean edges and intact negative spaces.

Do not add or transform the subject into a knight or plate-armored warrior, undead body, living Indigenous clothing or paint, sacred or culture-specific motif, modern tactical equipment, firearm, extra weapon, extra person, extra limb, altered weapon grip, altered pose, terrain base, text, logo, watermark, or gore.

## Alpha recovery

Native ImageGen and one targeted alpha-repair pass both returned baked RGB checkerboard pixels. The selected documented fallback removed only border-connected near-neutral checker pixels, kept one connected foreground component, softened alpha by 0.65 pixels, and decontaminated edge RGB from the nearest opaque subject colors. U2Net/ISNet variants were rejected for matte damage, halos, or checker fringe.

## Comparison and approval

- Comparison: `refs/source/recovery_v8/source_to_refinement_comparison.png`.
- Comparison SHA-256: `CDE376E9703D4A4E5DF993048F7BAD0F9CF339830BB8D5A7B5176C411600A25B`.
- Parent approval: approved exact final checksum on 2026-08-24.
- Provider status: the exact Meshy 7 request returned HTTP 402 before task creation; no credits or artifacts resulted.
