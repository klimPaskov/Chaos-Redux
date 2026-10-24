# Part 11: Portraits, visual identity, animation and audio

## A familiar face must remain uncertain

The screening experience depends on believable variety. A player should meet women who could plausibly live in the country being played, with different ages, occupations, styles, expressions and degrees of photographic polish. The pool must support attractive humans, attractive aliens, ordinary-looking humans and ordinary-looking aliens. Source choice, image quality, cropping, file order and generated-versus-photographic style must not identify the hidden class.

The early visual language is domestic and institutional: family photographs, documents, orderly offices, military leave and comfortable homes. Its horror comes from recurring connections and subtle inconsistencies. The open-war language keeps recognizable motifs but turns them into biological structures, repeated limbs, protective plates and organized broods. The Mother is the same invasion at a vastly larger scale.

This chapter is a production specification. It does not claim that the portrait pool, sound files, models or final art have already been acquired or produced.

## The portrait requirement is a release gate

| Requirement | Acceptance target |
|---|---|
| Minimum shipped pool | At least 1,000 distinct adult identities with distinct approved portraits |
| Planned production target | 1,250 distinct identities |
| Predominantly sourced photographs | At least 80% of the shipped pool must be actual properly sourced internet photographs |
| Target photographic count | At least 1,000 photographs in the 1,250-identity target pool |
| Generated or illustrated supplement | At most 20%, used to fill justified coverage gaps and kept visually compatible |
| Identity counting | Multiple crops, mirrored copies, recolors, compression variants or photos of one person count as one identity |
| Runtime guilt | Assigned by the case system independently of the source image and its provenance |
| Portrait stability | Frozen for a published person record within the campaign |
| Long campaign | Saved no-repeat decks and the explicit reuse boundary in Part 3, without halting casework |

The production team must not reduce the pool to a few dozen portraits and call it a scalable prototype. A small test batch is useful for validating the pipeline, but the release still requires the full threshold. An all-generated replacement does not satisfy the user requirement.

The photographic exception is deliberate. These screening photographs remain photographs within a dossier treatment. They do not all require the historical-leader painted style. The supplied portrait-worker ownership and source-preservation rules still apply. A separately used historical leader portrait follows the project's grounded-person pipeline. Fictional alien leaders and impossible forms can use native image generation.

## Research and rights workflow

Prioritize sources with clear item records and usable rights information. Wikimedia Commons provides per-file license information and instructs reusers to verify that information and consider non-copyright restrictions. The Library of Congress has curated Free to Use and Reuse sets, while individual collections can contain protected exceptions. Smithsonian Open Access identifies specific assets as CC0, with other rights still requiring consideration. These are candidate discovery sources, not blanket permission for every photograph they host. See [Wikimedia reuse guidance](https://commons.wikimedia.org/wiki/Commons:Reusing_content_outside_Wikimedia), [Library of Congress curated sets](https://www.loc.gov/free-to-use/), [Women of Protest rights information](https://www.loc.gov/collections/women-of-protest/about-this-collection/rights-and-access/) and [Smithsonian Open Access FAQ](https://www.si.edu/openaccess/faq).

For a CC BY asset, preserve the applicable attribution, license link and modification notice. CC BY does not imply endorsement and does not automatically settle publicity, privacy or moral rights. The final item review must consider the intended fictional horror and suspect-screening context, especially for identifiable living people. A fictional name alone is not evidence that every necessary permission exists. Prefer an appropriate release or a documented historical/public-domain source with reviewed contextual suitability. Reject an unresolved candidate rather than inventing clearance. See the [CC BY 4.0 terms summary and legal-code link](https://creativecommons.org/licenses/by/4.0/).

These are asset acceptance rules, not a universal legal conclusion about all jurisdictions. The production record must show the actual item evidence. Search-engine thumbnails, social-media reposts, magazine scans with unclear rights, unlicensed celebrity galleries and unknown face datasets are not acceptable source records. No login, private account or personal data collection is needed to discover candidates.

The current research establishes source routes and their conditions. It does not establish that 1,250 suitable, distinct, cleared adult identities have already been found. Candidate rejection, rights review and identity deduplication are real production work.

### Acquisition stages

1. Assemble an initial discovery queue of at least 2,000 candidate identities across several source collections. Increase the queue if clearance or quality rejection is high.
2. Review a 50-identity pilot for rights, adulthood, source preservation, crop quality, native DDS behavior and visual class leakage.
3. Approve the pipeline and source policy, then acquire in batches of 100 to 250 identities with per-item receipts.
4. Review distinct identities across batches. A repeated person from a different collection remains a duplicate.
5. Fill coverage gaps with additional cleared photographs first, then the capped fictional supplement.
6. Validate the 1,000 release floor, photographic percentage, all file links, attribution and runtime sampling before marking the portrait requirement complete.

Do not assume that a collection's number of files equals its number of suitable people. Group photographs, duplicate sittings, children, unrelated objects and protected exceptions all reduce the usable yield.

## Coverage and identity independence

Cover adults across a broad age range, including older women. Include formal portraits, ordinary clothing, professional contexts and simple domestic photographs. Vary hair, expression, framing and photographic quality within the bounds of legibility. Avoid a pool consisting almost entirely of glamorous young studio portraits.

Use source metadata to understand historical period and provenance. Do not infer sensitive identity or personal history from appearance. Country and biography assignment uses fictional records and compatible art direction. A photograph's real subject name appears only where necessary in provenance and attribution. It is not silently imported as the suspect's fictional biography.

Both innocent and alien cases must use every approved source class at comparable rates. A generated image cannot be an alien marker. A modern-looking crop, restoration artifact, background color or exceptionally sharp face cannot become a reliable clue. Similar care applies to description templates, punctuation, text length and portrait framing.

The appearance likelihood ratio is capped by the screening design. The portrait creator does not label individual photographs as biologically alien or human. The case system assigns truth independently and saves it. Blind evaluation tests whether players can exploit the artwork or metadata beyond the intended weak aesthetic cue.

## Per-identity archival record

Every approved identity needs a stable source ID, original item URL, direct file URL when provided, creator attribution, title or description, relevant date, license/version or public-domain basis, rights evidence snapshot, access date, and a reviewer outcome. Record adulthood suitability and contextual-use review without collecting unnecessary private details.

Preserve the untouched source file, its cryptographic hash, the exact cropped PNG, crop coordinates or crop JSON, any approved processed PNG, the runtime DDS and its consumer mapping. Record every restoration, color adjustment or stylization. The original file remains unchanged. A crop cannot conceal the lack of source evidence.

The manifest separates real-source provenance from fictional runtime identity. It also records duplicate-group IDs, permitted use, photographic/generated class, content review, dimensions, texture format, asset lineage, attribution location and rejection reasons. A generated supplement records its generation reference and prompt lineage rather than a fabricated photographer or archive license.

If a file later loses approval, quarantine its future use and replace the asset through a versioned mapping. Existing saved cases require a deliberate compatibility policy so that removing an image does not change case truth or reuse a wrong person's biography. A versioned neutral unavailable-image panel can preserve old case history during repair, but it cannot count toward the shipped release pool.

## Portrait rendering and performance

The initial screening consumer is a portrait-sized dossier image with the project's standard 156 by 210 reference as the starting native contract. The exact scripted-GUI consumer can require an additional higher-resolution working image. Do not invent an advisor crop for every person. The 65 by 67 advisor form is created only for characters actually used as advisors.

Preserve a consistent face scale, useful shoulder context and enough background to avoid a row of indistinguishable cutouts. A deliberate dossier frame belongs to the UI layer, with separate selection, focus, disabled and evidence states. The portrait itself must not contain baked-in guilt indicators or interface controls.

Inspect a working native portrait consumer before selecting DDS format, mip policy, sprite framing and compression. The project's 2D texture conventions and the 3D material conventions are different. A 3D BC1 or BC3 rule must not be copied blindly into a portrait pipeline.

At 1,250 images, 156 by 210 pixels and four bytes per pixel, the raw pixel payload is 163,800,000 bytes, about 156.2 MiB before any mipmaps, container overhead or engine copies. This is an arithmetic budget, not a measured GPU footprint. Native loading and paging behavior must be measured. Optimization can change loading strategy or texture layout, but cannot reduce distinct identities below the release floor or reveal class through quality differences.

The UI shows a small page and a single active dossier, not a thousand simultaneous thumbnails. Saved identity decks and active-case limits belong to the case system. Texture registration and cache behavior need low-end performance testing with the full pool.

## Art coverage

| Asset family | Required coverage and direction | Native target or consumer |
|---|---|---|
| Screening portraits | Minimum 1,000 distinct approved adult identities, target 1,250 | Dossier portrait consumer, starting reference 156 by 210 |
| Historical human leaders used by the event | Correct real identities and historically plausible appearance | Leader 156 by 210, advisor 65 by 67 only where used |
| Fictional brood governors | Distinct human disguise where needed and a related revealed identity | Character portrait consumers |
| Mother portrait | One unique approved matriarch identity with consistent anatomy | Actual host leader plus scenario presentation |
| Report scenes | Relationship wave, investigation, witness protection, wrongful purge aftermath, institutional compromise, revelation, liberation, merger, Mother defeat and recovery | 210 by 176 |
| News scenes | Global relationship trend, confirmed international crisis, simultaneous revolt, Mother emergence, Mother defeat | 397 by 153, black-and-white treatment |
| Super-event scenes | The Unveiling, Mother of Mothers, and a distinct victory presentation after Mother's defeat | 457 by 328 |
| Focus icons | Each major anchor group and meaningful route distinction | 94 by 86, true alpha |
| Ideas and achievements | Distinct semantic icons with readable small silhouettes | 64 by 64 |
| Decision icons | Investigation, protection, audit, purge, cooperation, evacuation, relay operations, recovery | 32 by 32 |
| Brood flags | A common biological visual family with regional identity and supreme-command treatment | 82 by 52, 41 by 26 and 10 by 7 |
| Unit counters | Cadre, Line, Siege and a justified Mother-guardian variant | Exact installed vanilla counter family dimensions and green treatment |
| Interface | Dossier frame, two value icons, evidence source cards, queue states, confirmations and objective markers | Real native controls and verified sprite consumers |
| Strategic models | Three organic combat families plus the Mother's distinct approved strategic presence | Validated mesh, material, animation and entity bindings |

The table defines necessary coverage rather than prescribing a final focus count. The focus implementation owns the exact node graph, with art added for every final node that needs a distinct icon. Every delivered asset has an actual consumer. Unused speculative renders are kept out of the runtime package.

## Flags and symbols

Use flat generated flag artwork at the exact native sizes. The core motif can combine a closed ring, repeated protective forms and a central biological command shape. It should read as an organized alien polity, with regional differentiation by composition rather than a trivial color swap.

Human coalition symbols need their own design and must not replace every member's historical national flag. Historical flags used for grounded countries follow researched references. Every flag is checked at the smallest size for silhouette and contrast. A dramatic full-size illustration is not a usable 10 by 7 flag.

## Organic unit and Mother model briefs

**Cadre:** a comparatively compact transformed infiltrator, preserving some humanoid movement and the suggestion of a discarded human outline. It must read clearly at normal game zoom. Its role is fast local action and protection, with limited resistance to organized fire.

**Line:** a larger mass of coordinated limbs and protective tissue, adapted to sustained frontal combat. The silhouette and gait distinguish it from the Cadre. Its equipment and movement imply a real supply burden.

**Siege:** a heavy organism adapted to breaking defended positions. Its slow movement, recoil and attack cycle should communicate commitment and vulnerability. It cannot be a scaled-up copy of the Line with the same skeleton and timing.

**Mother and guardian:** the Mother is a distinct colossal command organism. The guardian is a combat formation with finite statistics and a clear role near the lair. The final consumer must distinguish leader/map presentation from a native unit model. Do not imply that visual size automatically creates a special combat system.

Each model starts from one clean, approved anatomy reference per body or held item. Avoid multi-view collages as a provider input. A supported biped route uses the current prescribed provider settings, one supported rig attempt and one attempt per required action. Retain usable results. Unsupported nonhumanoid anatomy is authored and repaired in live Blender under the current skill, not through a repository script that procedurally fabricates bones, weights or animation keys.

Required action coverage is idle, move, attack and death, with truthful additional transitions where the actual consumer needs them. Match the project's vanilla axis and height reference once. Inspect feet, contacts, clipping, deformation, root motion, normals, materials and attack timing. Export and reimport the final files, then verify the actual entity and unit binding. A model that looks correct in a standalone preview but is invisible in the game is incomplete.

Use the current 3D material contract, including appropriate BC1 or BC3 textures and full mipmaps where required by the validated consumer. Supply source files, exported assets, provider receipts, animation mapping and live-view evidence when available. Do not label a generated mesh with no skeleton or actions as a completed animated unit.

## Animation direction

The screening interface may include a subtle evidence-processing motion, a document transition or an optional unresolved-network motif. Animation must not correlate with guilt. Disabled motion settings retain all information in a static state.

The major transformation and Mother presentations deserve real authored frame sequences where animation is used. A still image that is merely moved, scaled or cross-faded does not count as a completed transformation animation. The sequence needs consistent anatomy, intentional frame-to-frame change, correct pacing and a verified sprite-frame consumer.

Keep the dramatic animation separate from the functional UI. A report must remain readable, a confirmation must remain clickable, and the screen must remain usable while paused. The event UI worker owns the event window, while shared event-log, details, settings and super-event owners retain their respective interfaces.

## Audio direction and research candidates

Early audio is restrained: document handling, quiet domestic ambience and short uncertainty cues. Open revolt introduces a coherent organic vocabulary. The Mother adds a much larger low-frequency presence and a recognizable command motif. Sounds should support decisions and battlefield events without becoming a constant wall of noise.

The source rules require identified licensed recordings or suitable existing vanilla assets for custom unit audio. Do not substitute generated, synthetic or manually manufactured placeholder noises for sourced clips. Trimming, level adjustment and approved format conversion preserve the source lineage. Selection acknowledgements, movement, attack and death have separate roles and suitable variation. Their timing follows actual animation events.

The following are researched candidates, not selected or auditioned final assets:

| Candidate | Potential use | Evidence and remaining work |
|---|---|---|
| Kevin MacLeod, The Hive, ISRC USUAN1100711 | Unveiling or network-horror cue | Creator track listing identifies a horror soundscape and CC BY 4.0 attribution. Audition, exact excerpt, current download and license evidence still required |
| Kevin MacLeod, Darkest Child, ISRC USUAN1100783 | Early unease or an alternative revelation cue | Creator listing supplies track identity and CC BY 4.0. Avoid using a child-associated musical character to imply child targets. Audition and fit review required |
| Khrinx, Monster screech, Freesound 565024 | Candidate attack or reveal accent | Item page identifies CC0. Actual clip suitability, recording provenance, variation and edit boundaries still need review |
| gpag1, Monster screams.wav, Freesound 391552 | Candidate creature vocal family | Item page identifies CC0. Audition and provenance review required before any runtime use |

Primary source links: [The Hive](https://incompetech.com/music/royalty-free/index.html?Search=Search&isrc=USUAN1100711), [Darkest Child](https://www.incompetech.com/music/royalty-free/index.html?isrc=USUAN1100783), [Monster screech](https://freesound.org/people/Khrinx/sounds/565024/), [Monster screams](https://freesound.org/people/gpag1/sounds/391552/) and [Freesound licensing guidance](https://freesound.org/help/faq/). Some creator pages render track details dynamically. Search-indexed creator metadata was available during this planning pass, but no audio file was downloaded or auditioned.

Do not use the commercial recording of Tomorrow's Girls merely because its invasion idea is incorporated. No song lyrics or unverified musical quotations are required. Composition rights and recording rights must both be suitable for any chosen track.

## Super-event presentation briefs

**The Unveiling:** move from familiar companionship to a coordinated global rupture. The image must show the revealed threat and the human scale of loss while leaving the war visibly unresolved. The cue should establish the common alien motif, with a clear start and controlled ending. Text direction concerns disbelief, betrayal and the need to act. It must not declare universal human defeat.

**Mother of Mothers:** show a supreme organism that commands existing broods, with recognizable armies, territory or infrastructure giving a sense of scale. The cue is heavier and more unified than the first revelation. Text direction concerns a final common enemy and the survival struggle now beginning. It must communicate that human victory remains possible.

**Defeat of the Mother:** show the failure of the central organism and the survival of human effort. The cue can move from tension into exhaustion and earned relief. Text direction acknowledges remaining local threats and the cost of victory. It must not imply that all occupied land or all missing people have automatically returned.

Default final cue length is 60 to 120 seconds, with a two-minute cap unless separately authorized. Research can propose excerpts from longer recordings, but the final cut, transitions, attribution and actual runtime playback must be checked. Shorter UI sounds remain separate. No final quote or player-facing sentence is authored in this specification.

## Asset completion criteria

Portrait count, distinct identities, photographic share, source evidence, attribution and class independence must all pass. Every major country and unit needs its complete visual and audio package. Every animated consumer needs real frame or skeletal data and a static fallback where relevant. Every DDS, sprite, flag, mesh and sound must resolve through its actual runtime consumer.

The final art review uses the full native UI at representative resolutions and interface scales, the full portrait library under practical case paging, and normal map zoom for the custom units. The expected result is an event whose ordinary people feel varied and believable, whose alien forms are distinct and readable, and whose presentation never substitutes polish for missing functionality.
