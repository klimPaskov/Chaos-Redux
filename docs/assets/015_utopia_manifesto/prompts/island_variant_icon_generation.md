# Event 015 island-variant icon generation prompts

Date: 2026-07-15

Source mode: built-in ImageGen, one independent generation call per asset. No CLI model, fallback source, reused icon, atlas crop, or locally drawn substitute was used.

All three sources used a perfectly flat #ff00ff chroma field so the installed ImageGen chroma helper could create real alpha. The focus generations used the repository focus reference contact and the Event 015 island-defense atlas as style references. The decision generation used the repository decision references and the Event 015 final decision/category atlas as small-icon style references.

## Archipelago network focus

- Use case: stylized-concept
- Asset type: Hearts of Iron IV national focus icon source art, designed to finish at 95x85 pixels
- Primary request: Create one isolated, fully rendered HOI4-style focus icon for an archipelago network: exactly three clearly separate inhabited islands connected through civic harbor and convoy links.
- Scene and backdrop: perfectly flat solid #ff00ff chroma-key background for local removal; an emblematic painted vignette rather than a full rectangular scene.
- Subject: three small green-brown rocky islands in a strong triangular cluster over dark blue water; each island has one small 1930s civic settlement or storehouse and a harbor pier. Two period coastal cargo boats and pale painted wake-lines connect all three sites. One compact brass survey divider and a modest provision crate or grain sack support the civic survey and provisioning meaning without obscuring the islands.
- Style: period-appropriate HOI4 painted UI art; aged oil-painted detail, dark inked silhouette, muted navy, olive, parchment, bronze, and warm ochre; the visual density and emblematic framing language of the supplied focus references without copying an existing icon.
- Composition: one centered 95x85-oriented focus composition with a broad readable silhouette, three unmistakable islands, restrained rope or laurel framing, generous chroma separation, and no clipping.
- Mood: sober civic planning and maritime provision; hopeful but practical.
- Required: exactly three inhabited islands, visible harbor and convoy connections, visible civic survey and provision cues, crisp dark edges, generous padding, and no #ff00ff in the subject.
- Avoid: text, letters, numbers, labels, fake writing, flags, national emblems, conquest, weapons, modern map graphics, neon routes, arrows, satellite imagery, white matte, white outline, sticker border, opaque square background, checkerboard, watermark, multiple variants, contact sheet, full rectangular scene, or a shadow on the chroma field.

Selected built-in output: C:/Users/klimp/.codex/generated_images/019f6472-e946-7c03-a8da-4156500da1b6/exec-ac517c62-de3b-4064-8b25-bb5795cfa4ec.png

## Leased island focus

- Use case: stylized-concept
- Asset type: Hearts of Iron IV national focus icon source art, designed to finish at 95x85 pixels
- Primary request: Create one isolated, fully rendered HOI4-style focus icon for a leased island: a formal, negotiated, temporary civic lease of an island shore, visibly not conquest.
- Scene and backdrop: perfectly flat solid #ff00ff chroma-key background for local removal; an emblematic painted vignette rather than a full rectangular scene.
- Subject: an open vellum lease ledger with blank ruled pages and a red wax seal, a large antique brass key resting across it, and two civilian hands calmly completing an exchange or handshake. One peaceful rocky island shore with a modest 1930s harbor pier and civic storehouse sits behind the ledger. A short blank lease ribbon supports the limited-tenure reading.
- Style: period-appropriate HOI4 painted UI art; aged oil-painted detail, dark inked silhouette, muted navy, sea green, parchment, bronze, oxblood wax, and warm ochre; the visual density and emblematic framing language of the supplied focus references without copying an existing icon.
- Composition: one centered 95x85-oriented focus composition; ledger and key form the main silhouette, negotiated hands and peaceful shore remain clear, restrained bronze or laurel framing, generous chroma separation, and no clipping.
- Mood: formal civic negotiation, stewardship, temporary custody, and lawful peace.
- Required: identifiable lease ledger, key, shore, wax seal, and negotiated hand exchange; crisp dark edges, generous padding, and no #ff00ff in the subject.
- Avoid: text, letters, numbers, signatures, fake writing, flags, soldiers, guns, warships, subjugation, conquest, occupation, annexation, modern graphics, white matte, white outline, sticker border, opaque square background, checkerboard, watermark, multiple variants, contact sheet, full rectangular scene, or a shadow on the chroma field.

Selected built-in output: C:/Users/klimp/.codex/generated_images/019f6472-e946-7c03-a8da-4156500da1b6/exec-2f3bbec6-946d-42af-b2a0-6743e4768a4e.png

## Archipelago network decision

- Use case: stylized-concept
- Asset type: Hearts of Iron IV decision icon source art, independently composed to finish at 64x64 pixels
- Primary request: Create one isolated, compact HOI4-style decision icon for an active archipelago-network map-table operation linking exactly three island sites. It must be a fresh decision composition, not a focus icon, focus crop, or heraldic medallion.
- Scene and backdrop: perfectly flat solid #ff00ff chroma-key background for local removal.
- Subject: a small top-down 1930s wooden chart board or folded parchment sea chart with exactly three raised island markers. Three dark red cord segments join brass pins at all three sites into one clear triangle. One compact brass divider and one tiny period cargo-boat token sit at the edge while the three linked sites remain dominant.
- Style: compact period HOI4 painted decision art; aged parchment, dark wood, tarnished brass, oxblood cord, muted blue-gray water, strong dark outline, controlled contrast, and chunky hand-painted shapes for 64x64 readability.
- Composition: a centered near-square object cluster with generous transparent margin, viewed slightly from above; no laurel wreath, shield, focus badge, scenic horizon, or rectangular painted backdrop.
- Mood: practical civic logistics and coordinated harbor planning rather than military invasion.
- Required: exactly three island sites, all three visibly linked by physical cord and pins, immediate map-table operation reading, crisp dark edges, generous padding, and no #ff00ff in the subject.
- Avoid: text, letters, numbers, labels, fake writing, flags, modern digital map graphics, glowing routes, arrows, satellite imagery, weapons, soldiers, conquest, white matte, white outline, sticker border, opaque square background, checkerboard, watermark, multiple variants, contact sheet, focus framing, or a shadow on the chroma field.

Selected built-in output: C:/Users/klimp/.codex/generated_images/019f6472-e946-7c03-a8da-4156500da1b6/exec-5626a412-a632-41a5-b9d0-c84dfa9d85d5.png

## Deterministic processing record

The generated sources were copied into the Event 015 asset package, keyed with the installed ImageGen `remove_chroma_key.py` helper using border sampling, soft matte, thresholds 12 and 220, and despill, then fitted with the existing Event 015 `fit_rgba` processor. A restrained one-pixel UI shadow was composited behind each already outlined subject. Final PNGs were converted through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to one-level uncompressed 32-bit BGRA DDS files.

Final runtime normalization follows the repository asset contracts rather than the dimensions stated in the generation brief: both focus DDS files are `94x86`, and the independently composed decision DDS is `32x32`. The ImageGen masters and processed PNGs remain preserved at their source-review dimensions; the runtime and staged DDS pairs are the normalized outputs.
