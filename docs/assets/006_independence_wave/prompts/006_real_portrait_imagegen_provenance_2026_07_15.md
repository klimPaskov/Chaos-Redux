# Event 006 real-person portrait ImageGen provenance

Date: 2026-07-15

Mode: Codex built-in OpenAI ImageGen image editing. No API, CLI, stock-face,
synthetic-person, or no-reference fallback was used. Each accepted edit used
the attributed archival photograph as the sole identity source and the three
canonical vanilla leader portraits only as finish/framing references.

Canonical references:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ire_eamon_de_valera.png`

## Josef Friedrich Matthes

Identity source:
`docs/assets/006_independence_wave/source_png/portraits/rhi_josef_friedrich_matthes_source.jpg`

Retained edit:
`docs/assets/006_independence_wave/source_png/portraits/imagegen_edits/portrait_rhi_josef_friedrich_matthes_imagegen_master.png`

Prompt:

> Use case: identity-preserve
>
> Asset type: identity-preserving master for a 156x210 Hearts of Iron IV historical country-leader portrait
>
> Input images: Image 1 is the edit target and sole identity/source-of-truth: the attributed 22 November 1923 Bain News Service photograph of Josef Friedrich Matthes. Images 2-4 are canonical vanilla Hearts of Iron IV leader portraits used only for painted finish, framing, value range, and quiet-background style; do not copy their people, faces, clothes, or accessories.
>
> Primary request: Transform Image 1 into a tight head-and-shoulders vanilla Hearts of Iron IV painted portrait while keeping Josef Friedrich Matthes unmistakably the same real person.
>
> Composition/framing: portrait orientation; head, shoulders, and upper chest only; face large and immediately readable at 156x210; retain the source's upright near-frontal pose, head angle, direct serious gaze, and compact proportions.
>
> Identity invariants: preserve exactly the broad square face, jaw, cheeks, nose, brow, eye spacing, lips, ears, age, skin texture, hairline, expression, and all asymmetries visible in Image 1. Preserve his dark beret shape and angle, white shirt, black bow tie, textured tweed suit lapels, and small light paper/card at the breast. Do not beautify, de-age, thin, widen, reconstruct, or replace any facial feature.
>
> Style/medium: restrained vanilla HOI4 hand-painted portrait treatment like Images 2-4: crisp controlled brushwork over faithful anatomy, slightly simplified small-scale detail, subdued contrast, mild period texture, historically plausible muted colorization, quiet mottled warm gray-beige background.
>
> Color palette: charcoal beret, gray-brown tweed, cream shirt, black bow tie, muted natural skin tones.
>
> Constraints: change only presentation, crop, subdued colorization, background, and painterly finish; source identity and documented clothing remain invariant. No added uniform, insignia, medals, beard, moustache, glasses, hat changes, text, border, UI, watermark, dramatic lighting, photorealistic finish, cinematic concept-art finish, or invented details.

Processing crop from the retained 1080x1440 edit: `(5, 0, 1075, 1440)`.
The deterministic processor metadata is retained beside the processed PNG.

## Rupprecht of Bavaria

Identity source:
`docs/assets/006_independence_wave/source_png/portraits/bay_rupprecht_of_bavaria_source.jpg`

Retained first pass (rejected for an overly full moustache):
`docs/assets/006_independence_wave/source_png/portraits/imagegen_edits/portrait_bay_rupprecht_of_bavaria_imagegen_candidate_01.png`

Retained corrected master:
`docs/assets/006_independence_wave/source_png/portraits/imagegen_edits/portrait_bay_rupprecht_of_bavaria_imagegen_master.png`

Initial prompt:

> Use case: identity-preserve
>
> Asset type: identity-preserving master for a 156x210 Hearts of Iron IV historical country-leader portrait
>
> Input images: Image 1 is the edit target and sole identity/source-of-truth: the attributed circa-1916 Franz Grainer portrait of Crown Prince Rupprecht of Bavaria. Images 2-4 are canonical vanilla Hearts of Iron IV leader portraits used only for painted finish, framing, value range, and quiet-background style; do not copy their people, faces, clothes, or accessories.
>
> Primary request: Transform Image 1 into a tight head-and-shoulders vanilla Hearts of Iron IV painted portrait while keeping Rupprecht unmistakably the same real person.
>
> Composition/framing: portrait orientation; head, shoulders, and upper chest only; face large and immediately readable at 156x210; retain the source's near-frontal pose, slight head angle, gaze, and erect military bearing.
>
> Identity invariants: preserve exactly the long narrow skull, high receding hairline, short combed hair, ears, brow, eye shape and spacing, long straight nose, cheek structure, jaw, thin horizontal moustache, age, stern expression, skin texture, and all asymmetries visible in Image 1. Do not beautify, de-age, broaden, thin, reconstruct, or replace any facial feature.
>
> Clothing and route details: preserve the source's circa-1916 field-marshal tunic, high embroidered collar, epaulettes, shoulder chain, and the medals and orders that are actually visible at the upper chest. Preserve source-visible shapes and placement only. Do not add, remove, rearrange, enlarge, or invent insignia, heraldry, medals, or decorations. This is a Bavarian dynastic-restoration leader portrait, not a generic modern officer.
>
> Style/medium: restrained vanilla HOI4 hand-painted portrait treatment like Images 2-4: crisp controlled brushwork over faithful anatomy, slightly simplified small-scale detail, subdued contrast, mild period texture, restrained historically plausible muted colorization, quiet mottled warm gray-green background.
>
> Color palette: dark muted field-gray/blue military tunic, subdued metallic decoration, warm neutral skin tones, quiet gray-green background.
>
> Constraints: change only presentation, crop, subdued colorization, background, and painterly finish; source identity, age, expression, pose, hair, moustache, clothing, and documented decorations remain invariant. No helmet, weapon, hands, text, border, UI, watermark, extra medals, dramatic lighting, photorealistic finish, cinematic concept-art finish, or invented details.

Correction prompt:

> Use case: identity-preserve correction edit
>
> Asset type: corrected master for a 156x210 Hearts of Iron IV historical country-leader portrait
>
> Input roles: Image 1 is the painted candidate to correct. Image 2, the attributed circa-1916 Franz Grainer photograph of Crown Prince Rupprecht of Bavaria, is the sole identity, anatomy, clothing, and decoration source-of-truth. Images 3-4 are canonical vanilla Hearts of Iron IV references for finish and framing only; never copy their people or clothing.
>
> Primary request: Keep Image 1's restrained painted presentation and tight portrait composition, but correct it toward Image 2 with exact historical identity fidelity.
>
> Mandatory facial corrections: make the moustache exactly the very thin, narrow, close-trimmed horizontal moustache in Image 2, with no bushy vertical volume or drooping corners. Preserve Image 2's long narrow face, slim jaw, modest cheek volume, high receding hairline, short dark combed hair, ear shape, asymmetrical eyes, long straight nose, age, and severe closed-mouth expression. Do not beautify, de-age, broaden, soften, or substitute the face.
>
> Mandatory uniform corrections: preserve only the collar embroidery, epaulettes, shoulder chain, large neck orders, and medal row visible in Image 2, at the same relative placement. Simplify tiny unreadable detail rather than inventing heraldry. Do not add, enlarge, rearrange, or redesign medals and orders. Crop at head, shoulders, and upper chest so lower decorations do not dominate.
>
> Style: crisp restrained vanilla HOI4 painted finish, subdued contrast, slight period texture, muted historically plausible colorization, quiet warm gray-green background.
>
> Constraints: change only the listed identity and source-fidelity corrections. No helmet, hands, weapons, text, UI, border, watermark, extra insignia, photorealism, or cinematic concept art.

Processing crop from the retained 1080x1440 corrected edit:
`(5, 0, 1075, 1440)`.

## Francois Debeauvais

No ImageGen operation was performed. The only legally defensible 1928 source
does not contain enough facial information for an identity-preserving edit.
Generating from it would reconstruct rather than preserve the real person.
Sharper 1932 and 1933 candidates were retained solely as rejected research
evidence and were not supplied to ImageGen.
