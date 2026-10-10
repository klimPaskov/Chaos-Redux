# Sandstorm: presentation and asset direction

## Presentation purpose

The player should recognize a huge moving weather front before reading a list of modifiers.
The map is the primary geographic explanation.
The response surface answers what is approaching the selected place, how dangerous current conditions are and which practical actions remain useful.
It does not expose the hidden simulation ledger.

The design uses the native world map with an accurate weather overlay and a compact attached response display for repeated geographic selection.
The attached display is justified by multiple changing fronts, forecast selection and target-specific actions.
It must be tested against the actual decision-category attachment and surrounding interface.
Its working layout is approximately 880 by 560 pixels, subject to the verified consumer and supported resolution.
Final dimensions follow native measurements.

## Map layers

| Layer | Meaning | Presentation direction |
| --- | --- | --- |
| Current wall | Authoritative occupied footprint and local intensity | Distinct outer boundary, warm dust body and readable severe-core pattern |
| Committed approach | Next twenty-four hours | Clear directional edge treatment and arrival context |
| Likely corridor | Twenty-four to seventy-two hours | Lighter hatched area with visibly lower certainty |
| Watch area | Three to seven days | Broad understated outline, avoiding a promise of precise future impact |
| Recently cleared route | Actual historical passage | Faint trail that expires from the operational view and remains available in history |
| Selected response target | Exact state, airfield or route section | High-contrast selection edge above the dust layer |

Every layer derives from verified map geometry and the authoritative front state.
Image generation supplies atmospheric art and texture, not country boundaries, state shapes or invented geographic pieces.
Land and sea share one projection and scale.
Coasts, islands, the map seam and ocean transit must line up with the actual supported map.
Existing unit counters, province selection and movement orders remain readable and usable.
The atmospheric layer cannot steal clicks from essential map controls.

Color is reinforced by hatching, edge shape and a written band name.
Weakening uses a sparse veil, normal a continuous ochre body, severe a denser rust-brown pattern and extreme a very dark core with a contrasting edge.
Avoid relying on red and green alone.
The player can reduce decorative motion while retaining the complete geographic information.

## Attached response display

The header identifies the selected geographic context and its qualitative phase.
The two public values are local intensity and estimated exposed civilians.
An approximation mark accompanies the population estimate.
A short causal line describes the useful current fact, such as a deepening wall, a new branch or clearing weather, with wording authored during implementation.

The central selection area links the chosen state or route to the actual map.
The action area shows the relevant three to five families from Part 05, with expandable cost and consequence detail.
A small mission area shows at most the three defined mission cards.
Owned, allied, hostile, unavailable and expired targets have visually distinct states and honest explanations.
Unavailable controls look unavailable and cannot retain active-looking art while only their click handler is disabled.

The category does not receive a separate decorative picture because it already contains the attached rich control surface.
Ordinary event and news art provide atmosphere elsewhere.
The shared event log, settings, Event Details, achievements and super-event framework retain their established structure.
The dedicated UI worker does not redesign those shared windows under Sandstorm ownership.

## Forecast and alert writing direction

Opening text names the actual source region and describes the scale and observed movement.
It establishes the broad initial footprint and explains that neighboring or distant territory may later be affected.
An already affected country receives present-tense conditions, while an approaching country receives warning language appropriate to the committed forecast.

Passage reports emphasize practical failures of sight, navigation and coordination.
Roads disappear under dust, units lose contact, loading and rail work slow, and people caught outside face danger.
Do not invent precise military incidents, named victims or casualty counts without supporting game receipts.
Humor and cultural allusions must never make civilian deaths the joke.
Any restrained irony belongs in an optional practical response remark and must be researched before final use.

Evolution I emphasizes the deepening wall.
Evolution II explains distinct new approaches.
Evolution III emphasizes the shock of a recognizably returning threat and renewed desert sources.
Evolution IV establishes simultaneous source regions and the difficulty of finding unaffected operating areas.
The evolution report only describes behavior that has actually manifested or been validly committed.

Clearance text distinguishes local safe weather from continuing repairs and other approaching branches.
The final season report follows the geographic journey and directs the player to actual recorded losses and restoration work.
It does not claim that the world returned to its previous population or industrial condition.

## Scene assets

These rows are the complete proposed scene-art obligations.
Every key is a working asset label.
Each final scene uses the matching current reference family and its exact consumer treatment.

| Key | Consumer and planned size | Visual direction | Source mode |
| --- | --- | --- | --- |
| SC099_R1 | Local formation report, 210×176 | A very broad desert wall approaching a period road or observation post, with scale communicated by distant structures | Generated fictional documentary scene |
| SC099_R2 | Local military passage report, 210×176 | Period formations losing visual contact in dense dust, restrained detail and identifiable roads or markers | Generated fictional documentary scene |
| SC099_R3 | Local recovery report, 210×176 | Dust clearing from a rail yard or workshop while workers assess actual damage | Generated fictional documentary scene |
| SC099_N0 | Global opening news, 397×153 | A panoramic wall across a desert horizon | Generated black-and-white documentary scene |
| SC099_N1 | Great Dust Wall news, 397×153 | An enormous dense wall overwhelming familiar built scale | Generated black-and-white documentary scene |
| SC099_N2 | Splinter Storms news, 397×153 | Visually separated dense weather bodies across a broad coastal or desert landscape | Generated black-and-white documentary scene |
| SC099_N3 | Returning Storm news, 397×153 | A recognizable recovering settlement facing a renewed wall from another direction | Generated black-and-white documentary scene |
| SC099_N4 | World of Dust news, 397×153 | A large industrial or transport landscape under almost continuous dust, with documentary restraint | Generated black-and-white documentary scene |
| SC099_S1 | Global milestone super-event, 457×328 | A powerful central composition of a major transport landscape swallowed by dust, with a small readable human-scale reference | Generated fictional scene after the super-event brief is researched |

Generated documentary treatment is alternate-history illustration and must never be labeled an authentic photograph of a historical incident.
All equipment, clothing, vehicles and buildings must fit the campaign's period.
Archival sources can inform dust texture, light and material behavior after their provenance and permitted use are checked.
No invented insignia, modern respirators, contemporary trucks or satellite imagery should enter a period scene by accident.

Report photographs are generated separately from the established card geometry.
The asset owner applies the proper 210×176 black-and-white or sepia card treatment, transparent corners, tilt and shadow using the approved reference workflow.
News remains black and white.
The super-event scene is composed for its exact frame rather than cropped from a tiny news image.

## Icons and geographic texture

Five 32×32 decision icons correspond to the five primary response families.
Their subjects are a sheltered doorway, protected machinery, a marked transport route, a field compass and formation marker, and a covered aircraft engine or hangar.
A distinct 32×32 category icon depicts the storm's broad moving wall.
Four 64×64 local-effect icons represent weakening, normal, severe and extreme conditions with distinct silhouettes and density, not only a palette change.
Eight 64×64 completed achievement sources follow Part 09.
Each icon family receives source art composed for that native target and its matching template.

One atmospheric texture loop is proposed for the local wall's decorative dust motion.
Its working target is twenty-four distinct 256×256 frames at ten frames per second, looping over 2.4 seconds, with a static fallback.
A horizontal sheet is 6,144×256 and fits the current texture-side limit.
The texture's geography comes from a separate exact mask and positioning consumer.
The loop itself depicts evolving particulate motion, with real distinct source frames and a coherent seam.
Sliding, recoloring, blurring or rotating one still does not satisfy the final animation requirement.

The geographic movement of the front is driven by actual simulation updates.
Decorative texture motion never determines its path or exposure.
If the native animated overlay is unavailable, the static atmospheric texture can preserve the full accurate moving footprint while the animation remains a separate documented production blocker.
This fallback does not permit replacing a moving geographic wall with a fixed icon.

## Asset production and evidence

The asset owner reads the current matching references under .claude/skills/chaos-redux-event-assets/assets/gfx_references/ before production.
References are review material and are not copied into runtime as final art.
All generated finals require actual image-generation evidence.
Generation and editing follow the current [event-assets owner skill](../../../.claude/skills/chaos-redux-event-assets/SKILL.md#generation-and-editing), including native transparency and truthful reporting of the exposed execution path.

Every logical slot maps to its runtime path, sprite, consumer and conditional state in a manifest.
The manifest distinguishes source art, accepted final pixels, file hashes, decoded-pixel hashes and actual consumer revisions.
Native-size and enlarged review must verify alpha, crop, frame placement and legibility.
Animation additionally needs frame review, loop endpoints, source lineage, DDS sheet and matching runtime wiring.
The asset prompt supplies the production ownership and handoff requirements.

## Super-event presentation research

The proposed global milestone earns one distinct researched presentation package.
Its final title, description, quote and button remark are produced only after source verification.
The quote should come from a traceable primary historical, literary or documentary source that fits the scale and human consequence without pretending it describes this fictional event.
The researcher compares candidates and records why the selected passage fits.

Audio must be a structured musical recording with verified composition and recording rights.
It should build from isolation or obscured distance into overwhelming scale, then leave room for the player's return to the campaign.
The preferred final duration is one to two minutes, with a two-minute maximum unless explicitly authorized otherwise.
Wind effects alone, a drone or a generated noise bed do not replace the musical requirement.
The track and audio identity must be unique unless the user explicitly approves exact reuse.
The existing Event 013 moving-storm slot cannot be assumed to belong to this new milestone.

## Visual acceptance

Inspect the actual map before authoring geographic assets.
Capture matching before and after states at the supported small and large resolutions, including scaling and long localisation.
Check a dense European region, a giant desert state, an island, occupied territory and ocean transit.
Confirm that the selected response refers to the place under the pointer and that the overlay does not block unit orders.
Render enabled, disabled, unaffordable, paid, interrupted, cleared and returning conditions.
The optional GUI rewrite tool is not itself an acceptance requirement, while inspection, rendering, comparison and correct attachment remain required.
