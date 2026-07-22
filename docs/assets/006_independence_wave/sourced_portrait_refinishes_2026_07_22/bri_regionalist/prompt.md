# ImageGen prompts - BRI regionalist portrait refinish

The current master is v3. Prior v2 and candidate v1 are retained as review
evidence. Every prompt treats the unchanged John Wickens photograph as the
identity-bearing edit target. Male vanilla HOI4 country-leader portraits are
style references only.

## Selected v3 prompt

```text
Use case: identity-preserve. Asset type: Hearts of Iron IV country-leader portrait, full 156x210 portrait convention. Edit Image 1 only: the exact sourced John Wickens 1904 photograph of Régis de l'Estourbeillon. Images 2, 3, and 4 are male vanilla HOI4 country-leader portrait references used for style only: full-color restrained painted rendering, pale quiet painted background, controlled value range, and readable head-and-shoulders silhouette. Do not copy their faces, clothing, identities, insignia, or poses.

Primary request: create a stricter revision 3 as a full-color, restrained 1930s HOI4-painted portrait while preserving the exact sourced man from Image 1. This is not a new portrait and not a reconstructed likeness. Keep the same male face and facial geometry: exact brow, eyes and gaze direction, nose, cheeks, jaw, ears, moustache/facial hair, apparent age as seen in the source, expression, head angle, pose, and proportions. Keep the same broad dark hat, hairline, shoulder silhouette, and every visible part of the period Breton costume from Image 1: dark outer garment, cape-like shoulder panels, rows of buttons, and the visible patterned chest panel. Do not invent or reveal hidden costume detail.

Apply only a restrained HOI4 painted finish: convert the monochrome source into subtle muted full color with period-appropriate 1930s palette and brushwork; quiet pale painted neutral background; controlled contrast and soft edge separation; light painterly texture instead of photographic halftone. Visible costume colors must remain subdued charcoal/black, slate, muted tan/gray and restrained dull-metal highlights, with no bright or symbolic colors. Keep the face natural, not beautified, idealized, de-aged, aged, or genericized.

Composition/framing: centered vertical head-and-shoulders crop, full hat and both shoulders visible, source head angle unchanged, no extra people or objects.
Lighting/mood: calm, dignified, softly lit archival portrait; no cinematic drama.
Constraints: change only color treatment, quiet painted backdrop, subtle HOI4 brush finish, and the crop. Preserve exact source identity, facial hair, gaze/expression, age appearance, pose, silhouette, hat, and visible costume. No text, watermark, UI, frame, badge, flag, invented symbol, sacred/cultural motif, tartan, pseudo-Celtic motif, invented insignia, medals, modern props, stereotype, caricature, glamour, or photographic/sepia filter.
Avoid: sepia monochrome, black-and-white output, brown photo tint, modern digital concept art, glossy photorealism, heavy oil-paint abstraction, face reconstruction, face substitution, changed ethnicity, altered facial proportions, altered gaze, changed hat or costume, newly invented clothing, or any readable text.
```

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
