# Fury Leader Flame Overlay Frame Plan

| Frame | Motion state | Visual change | Prompt delta | Anchor note | Loop note |
| --- | --- | --- | --- | --- | --- |
| 000 | rest | lowest flame tongues, embers clustered near bottom corners, faint side lick | calm supernatural burn | bottom-center | matches frame 007 closely |
| 001 | rise left | left lower tongue rises and curls inward, right edge stays restrained | left-side surge | bottom-center | easing into motion |
| 002 | rise both | both lower corners flare higher, thin side tongues lengthen | both sides lift | bottom-center | stronger silhouette |
| 003 | peak left | left side leans inward slightly, brighter ember core near lower edge | left peak with hotter core | bottom-center | first high point |
| 004 | peak center-low | central lower edge gains short split tongues but face zone stays open | low center flare only | bottom-center | hottest frame |
| 005 | peak right | right lower tongue rises and curls inward, left side recedes | right-side surge | bottom-center | mirrored energy |
| 006 | fall both | both sides shorten, ember field still active | falling glow | bottom-center | easing out |
| 007 | return | low, clean edge fire with small drifting tongues, close to frame 000 | return to rest | bottom-center | loop back to frame 000 |

## Shared generation constraints

- Same camera and canvas every frame: straight-on portrait overlay, `156x210`
- Transparent asset workflow: generate on perfectly flat `#00ff00` chroma-key background, then remove locally
- Background must remain fully flat with no shadow, no floor plane, no reflections
- Keep the center clear enough that eyes, nose, and mouth of an underlying portrait remain readable
- Flame mass should stay at lower quarter and outer side edges
- No text, no symbols, no modern UI, no black frame, no checkerboard, no ornate border
- Motion must come from distinct generated frame artwork, not from local transforms
