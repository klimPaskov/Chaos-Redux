# Prempeh II leader-portrait processing brief

No ImageGen prompt was used. Prempeh II is a real historical person, so the
`chaos-redux-event-assets` real-person rule requires an attributed archival
source and the deterministic `retired_advisor_card_processor_REMOVED leader` finish.

## Identity-preservation brief

Create one full `156x210` male civilian country-leader portrait for Nana
Otumfuo Agyeman Prempeh II from the National Archives UK CO 1069/44 image dated
31 January 1935. Preserve his recognizable face, apparent age, expression,
hair and head ornament, skin tone as represented by the monochrome source,
Asante cloth, fly whisk/regalia, seated posture, and proportions. Use a tight
head-and-shoulders crop with enough throne and cloth context to preserve his
office and identity. Apply only the processor's restrained HOI4 grading,
edge-preserving finish, grain, and vignette. Do not reconstruct, beautify,
colourise, replace, or generate facial features. Do not create an advisor or
commander-small derivative.

## Exact rejected crop and command

Source dimensions: `393x563` pixels.
Rejected candidate crop in source pixels: `left=105, top=5, right=275, bottom=234`.

```powershell
python -B retired_advisor_card_processor_REMOVED leader `
	docs/assets/006_independence_wave/iw093_asante_prempeh_ii_2026_07_18/source_image/CO_1069-44-12_prempeh_ii_1935.jpg `
	docs/assets/006_independence_wave/iw093_asante_prempeh_ii_2026_07_18/processed_png/portrait_DOX_prempeh_ii.png `
	--source-kind real `
	--crop 105 5 275 234 `
	--review-sheet docs/assets/006_independence_wave/iw093_asante_prempeh_ii_2026_07_18/contact_sheets/portrait_DOX_prempeh_ii_process_review.png `
	--metadata docs/assets/006_independence_wave/iw093_asante_prempeh_ii_2026_07_18/metadata/portrait_DOX_prempeh_ii_processing.json `
	--reference-dir .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders
```

The stored metadata records `--force = true` because two earlier crop trials
were overwritten in place before this candidate was submitted. Those trials
were not retained. The parent rejected the submitted result because it remained
a sharpened grayscale archival photograph rather than a painted/colour HOI4
leader portrait. The candidate is retained only as rejection evidence; its
former runtime DDS was deleted and it must not be wired or reused.
