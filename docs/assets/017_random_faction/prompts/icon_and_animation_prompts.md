# Event 017 Random Faction Icon and Animation Prompt Record

## Provenance

The accepted source PNGs and animation atlases were created with the built-in `$imagegen` workflow before this audit. This audit preserved that real source art and repaired only deterministic chroma removal, normalization, frame-sheet assembly, previews, and DDS derivatives.

The exact historical tool-call text was not retained with the original commit. The prompt matrix below is the canonical reproducibility record derived from the approved source art, Event 17 asset specification, and final sprite identifiers. It does not claim to be a verbatim transcript of the earlier tool calls.

## Shared production block

Combine this block with the asset-specific subject row below.

```text
Use case: stylized-concept
Asset type: Hearts of Iron IV game UI icon
Primary request: create the specified Event 17 faction-pressure symbol as original painted game art
Style/medium: compact HOI4-style painted icon, period diplomatic and military materials, aged brass, paper, cloth, wax, dark ink, restrained painterly texture
Composition/framing: one centered subject, strong silhouette, readable at the stated target size, generous padding
Lighting/mood: tense interwar diplomatic pressure, strong value contrast
Scene/backdrop: perfectly flat solid #00ff00 chroma-key background for local removal; no floor plane, shadow, gradient, texture, or reflection in the background
Constraints: no readable text, no maps as the main subject, no watermark, no modern objects, no checkerboard, no opaque square backdrop, no white rim, no sticker outline; keep the subject fully separated from the key color
```

## Decision and category icon prompts

All decision-family outputs are separate source artworks composed for 32x32 readability, not resized idea or achievement art.

| Asset | Asset-specific prompt subject |
|---|---|
| `decision_category_random_faction_bloc_pressure` | A bronze diplomatic seal binding red, blue, and dark faction banners with taut cords; broad, unmistakable category silhouette. |
| `decision_random_faction_neutrality_council` | A small round council table seen slightly from above, ringed by chairs and centered on an unmarked neutrality medallion. |
| `decision_random_faction_border_posts` | Twin guarded frontier posts, striped barrier, sandbags, and a simple connecting cable. |
| `decision_random_faction_liaison` | Officer cap, sealed liaison envelope, and crossed diplomatic cords in one compact silhouette. |
| `decision_random_faction_radio_networks` | Portable 1930s radio set beside a narrow mast carrying several small signal pennants. |
| `decision_random_faction_corridor` | Neutral shield between two striped border pillars, with a narrow guarded passage implied through the center. |
| `decision_random_faction_commitment` | Heavy wax stamp pressing a sealed faction pledge over folded banners. |
| `decision_random_faction_stabilize_alignment` | Brass compass and stabilizing crossed directional arrows held between opposing red and blue banner points. |
| `decision_random_faction_opposition` | Opposing faction banners pulled against a central sealed document, visibly resisting one another. |
| `decision_random_faction_observers` | Field binoculars over stamped travel papers and a compact frontier pass. |
| `decision_random_faction_neutrality_press` | Compact field press or teleprinter feeding a sealed neutrality bulletin with no legible text. |
| `decision_random_faction_staff_mission` | Military staff cap, sealed dispatch, and crossed liaison cords, distinct from the civilian liaison icon. |

## Idea icon prompts

All idea outputs are separate 64x64 spirit compositions with their own source art.

| Asset | Asset-specific prompt subject |
|---|---|
| `idea_random_faction_alignment_shock` | Red and blue faction arrows striking a cracked central diplomatic seal, sharp impact silhouette. |
| `idea_random_faction_border_pressure` | Neutral shield and border marker compressed between red and blue faction banners. |
| `idea_random_faction_bloc_polarization` | Two opposing banner standards tied into a tense central knot of cables and seals. |
| `idea_random_faction_neutrality_exhaustion` | Worn neutral shield sagging under stacked dossiers, frayed cloth, and spent diplomatic seals. |
| `idea_random_faction_liaison_mission` | Portable radio, officer cap, sealed envelope, and three small faction pennants linked by signal lines. |

## Achievement icon prompts

Use the shared style but set `Asset type` to `64x64 Hearts of Iron IV achievement icon` and request a dark bronze square achievement frame. Each completed icon is separate source art. Grey variants are grayscale derivatives; not-eligible variants use the repository achievement cross overlay.

| Achievement id | Asset-specific prompt subject |
|---|---|
| `017_random_faction_four_doors` | Four distinct faction emblems arranged as cabinet doors around one small round council table. |
| `017_random_faction_hold_the_line` | Fortified border gate and neutral shield holding between two guarded frontier towers. |
| `017_random_faction_crowded_border` | Three differently colored faction banners and cable lines converging on one small neutral frontier marker. |
| `017_random_faction_liaison_web` | Radio mast and officer cords forming a visible network between three small flags. |
| `017_random_faction_frontier_commitment` | Small shield standing between two hostile faction fronts under a storm-dark sky. |
| `017_random_faction_not_everyone` | One plain unmarked flag or empty chair standing apart from clustered bloc banners around a cabinet table. |

## Animation prompts

The accepted atlases contain eight separately drawn states and were sliced into individual source frames. For any future regeneration, use one built-in generation or high-fidelity edit pass per frame with the base prompt and the exact frame delta from the corresponding `frame_plan.md`; do not synthesize motion with local transforms or filters.

### Bloc-pressure seal base

```text
Use case: stylized-concept
Asset type: 64x64 HOI4 animated decision seal source frame
Primary request: paired red and blue faction banners, taut crossed diplomatic cables, stacked travel papers, a wax seal, and a central bronze diplomatic medallion
Style/medium: compact painterly HOI4 UI emblem with aged brass, cloth, cord, paper, and wax
Composition/framing: identical centered camera, silhouette, scale, and center anchor across all eight frames
Scene/backdrop: perfectly flat solid #00ff00 chroma-key background, fully uniform
Constraints: redraw the requested cable, cloth, seal-light, paper, and spark state in the source art; no transform-only motion; no readable text; no watermark; no cast shadow; no key green in the subject
```

Frame-specific deltas are recorded in `docs/assets/017_random_faction/animations/random_faction_bloc_pressure_seal/frame_plan.md`.

### Border-warning base

```text
Use case: stylized-concept
Asset type: 64x64 HOI4 animated border-warning source frame
Primary request: guarded frontier post, striped barrier, sandbags, barbed wire, overhead cables, two faction flags, and a warning lantern
Style/medium: compact painterly HOI4 UI emblem with aged wood, metal, cloth, cable, glass, and earth
Composition/framing: identical centered camera, silhouette, scale, and center anchor across all eight frames
Scene/backdrop: perfectly flat solid #00ff00 chroma-key background, fully uniform
Constraints: redraw the requested lantern, beacon, wire, flag, and red-alert state in the source art; no transform-only motion; no readable text; no watermark; no cast shadow; no key green in the subject
```

Frame-specific deltas are recorded in `docs/assets/017_random_faction/animations/random_faction_border_warning/frame_plan.md`.
