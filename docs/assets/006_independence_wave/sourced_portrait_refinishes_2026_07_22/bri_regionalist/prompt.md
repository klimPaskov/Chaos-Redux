# ImageGen prompts - BRI regionalist portrait refinish

The selected master is v2. Candidate v1 is retained only as review evidence.
Both prompts treat the John Wickens photograph as the identity-bearing edit
target. Canonical vanilla portraits are style references only.

## Selected v2 prompt

```text
Use case: identity-preserve. Asset type: Hearts of Iron IV country-leader portrait. This is a strict edit of Image 1, the exact sourced 1904 photograph of Régis de l'Estourbeillon. Image 2 is style-only for the vanilla HOI4 painted finish and pale quiet background.

Primary request: make a minimal identity-preserving HOI4 portrait treatment from Image 1. Do not redraw or reinterpret the face. The output must retain the same man from Image 1 with the same facial silhouette, brow, eyes and gaze direction, nose, cheeks, jaw, moustache, apparent age, expression, head angle, hat, and visible Breton costume. Preserve the source-supported upper torso and costume details. Only perform a clean head-and-shoulders crop, remove the busy photographic background to a pale quiet neutral backdrop, and apply a very restrained painterly texture and controlled contrast like Image 2. Keep the result realistic, dignified, and recognizable as the exact photographed individual, not a lookalike.

Composition/framing: vertical head-and-shoulders, centered, full hat and shoulders visible, no extra people or objects.
Lighting/mood: soft even archival light, muted warm gray/sepia-neutral values.
Constraints: edit only background, crop, and subtle finish; preserve exact face and visible clothing/regalia. No new facial details, no beautification, no de-aging, no aging, no pose change, no clothing changes. No text, watermark, UI, frame, flag, symbol, invented insignia, medals, uniform, tartan, pseudo-Celtic motif, sacred/cultural symbol, stereotype, caricature, glamour or cinematic treatment.
Avoid: generic face, facial reconstruction, face substitution, modern concept art, dramatic color grading, over-smoothing, strong oil-paint effect that erases likeness.
```

## Retained v1 prompt

```text
Use case: identity-preserve. Asset type: Hearts of Iron IV country-leader portrait, full 156x210 portrait convention. Edit Image 1 only: it is the exact sourced 1904 John Wickens photograph of Régis de l'Estourbeillon, the grounded male Breton regionalist civic leader. Images 2 and 3 are style references only for the restrained vanilla HOI4 painted finish, pale quiet background, controlled contrast, and head-and-shoulders framing; do not copy their faces or identities.

Primary request: perform a source-preserving portrait treatment. Keep the exact same man's identity and recognizable face from Image 1: same facial structure, apparent age, expression, moustache/facial hair, head angle, and proportions. Keep the clothing and regalia actually visible in Image 1, including the period Breton outfit and hat, without inventing or removing details. Reframe the original upper body into a clean head-and-shoulders crop suitable for a 156x210 leader portrait. Apply only a restrained hand-painted HOI4 leader-portrait finish: subtle brush texture, quiet pale neutral background, gentle edge separation, readable silhouette, controlled midtone contrast, and slightly softened early-photo halftone texture. This is an edit, not a new portrait or a reconstruction.

Composition/framing: vertical head-and-shoulders crop; face centered and fully visible; preserve head angle and source-supported upper-torso costume; no extra people or objects.
Lighting/mood: calm, dignified, period archival; soft even light, no cinematic drama.
Color palette: muted warm gray and restrained sepia-neutral tones consistent with vanilla HOI4 leader portraits; no vivid colors.
Constraints: change only the crop, quiet backdrop, and subtle painterly finish. Preserve the exact source identity, facial hair, expression, age appearance, pose, hat, and visible clothing/regalia. Keep the result realistic and non-caricatured. No text, watermark, UI artifact, frame, border, badge, medal, invented insignia, invented uniform, or face substitution.
Avoid: new or generic face, beautification, de-aging, aging beyond source, facial reconstruction, altered ethnicity, altered expression, altered hat or clothing, tartan, pseudo-Celtic motifs, sacred/cultural symbols, flags, slogans, modern props, stereotypes, caricature, glamour lighting, cinematic concept art, oil-paint filter that obscures likeness, and any readable text.
```

