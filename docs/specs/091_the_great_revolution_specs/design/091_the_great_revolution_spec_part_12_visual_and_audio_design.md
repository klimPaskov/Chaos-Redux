# 12. Visual and audio production design

## Visual grammar

The core image combines Lenin's recognizable face, an organic third eye, labor transformed into military force, and a global revolution with local texture. Deep red, near-black, worn metal, dirty cloth, and pale human skin create a consistent palette. The third eye is anatomy, with lid, socket, tissue, and gaze. It is not a red dot, jewel, forehead lamp, or generic occult sticker.

Workers should retain the tools, clothing, workshop materials, and regional context that explain who they were. Nonhuman features appear through unnatural movement, altered proportions, eyes, wounds that behave incorrectly, synchronized attention, and tools wielded with impossible force. Regional identity must not become caricature. A colonial origin changes institutions, architecture, climate, clothing, and organizing networks without changing the recognizable Lenin identity.

Historical symbols are researched before the fictional emblem is generated. The hammer and sickle reference industrial workers and peasants. The third eye adds the event's fictional claim of perception and command. The symbol must remain readable in the smallest flag and counter consumers.

## Lenin source and identity

The portrait owner finds an identifiable historical Lenin source with a documented rights basis, highest usable resolution, and an explicit record of the actual person. The source is the identity master. The requested third-eye result is either the user's styled final based on that master or an approved transparent overlay. A newly generated substitute face is not an acceptable Lenin portrait.

The `chaosx_portrait_creator` route in `chaos-redux-event-assets` governs production. It archives the sourced master, prepares masks, placement guidance and crops, and wires the source placeholder, while the user alone runs the grounded HOI4-style styling step. The wired source portrait stays an explicit pending placeholder until the user supplies the styled replacement. No sourced master, styled portrait or animated consumer exists yet.

The same identity record governs the central super-event figure and staged event portraits. Separate compositions can use the same historical identity without turning every asset into a crop of one picture.

## Required asset manifest

Dimensions below come from the supplied asset workflows and must be checked against the actual chosen consumer before production. Every final asset needs its path, sprite or entity consumer, source or generation record, rights record where relevant, QA evidence, and a static fallback when animation is involved.

| Asset group | Required deliverables | Consumer and production contract |
| --- | --- | --- |
| Lenin portrait | Historical master, 156 by 210 leader portrait, organic-eye styled final or transparent overlay, power-stage variants, static fallback | Actual leader and event portrait consumers, with preserved identity |
| Joined leader overlays | Five stages, each with transparent master, politics placement, diplomacy placement where supported, and static fallback | Independent click-through UI containers bound to the current leader, no small hardcoded roster |
| Country flags | Main flag and justified route variants at 82 by 52, 41 by 26, and 10 by 7 | TGA, 32-bit uncompressed, bottom-left origin, decoded orientation and alpha checked |
| Faction identity | Original emblem, faction-name research, compatible country color | Name and identifier collision audit before registration |
| Opening report | A dedicated 210 by 176 report composition | Sepia photo-card treatment, natural tilt and transparent corners from the approved frame convention |
| Global news | Dedicated 397 by 153 composition | Black-and-white news image that reads at wide aspect ratio |
| Super-events | Three distinct 457 by 328 compositions for opening, Red World, and earned defeat | Each complete role has separate image, title direction, main quote, remark, button direction, audio, and registration |
| Incident reports | Strikes, rituals, local uprising, council congress, transformation, command loss, Stalin confrontation, Trotsky partnership, body custody | Dedicated compositions as needed by actual event families, with purposeful reuse only inside the same documented family |
| Focus icons | Eight family grammars and distinct political, military, industrial, international, command, and terminal anchors | 94 by 86 master consumers, transparent silhouettes and normal-zoom readability |
| Idea icons | Leadership, disconnected administration, political settlement, joiner stage, human opposition, temporary operational effects | 64 by 64, evolving core spirit families instead of an uncontrolled stack |
| Decision icons | Powers, cells, all army roles, aid, sovereignty resistance, independence, commands, cure and reconstruction | 32 by 32, each action family recognizable without text |
| Category picture | Animated active-revolution composition plus static fallback | Nominal 114 by 101 subject to consumer inspection, no fake controls or meters |
| Unit counters | Eight bespoke large counter designs and verified small-map equivalents | Large 152 by 42 strip containing two 76 by 42 frames, muted vanilla green with restrained pale glyphs |
| Unit visual packages | Eight family models, textures, rigs, held items, actual skeletal actions, template emblems, relevant equipment and technology art | Measured vanilla scale, distinct silhouettes, genuine contact and action timing |
| Achievements | One original approved artwork per achievement with required completed, grey, and not-eligible states | 64 by 64 triplets using the immutable template and overlay rules |
| Promotional key art | One separate signature composition for the approved promotional consumer | Consumer dimensions chosen before production, no automatic crop of a super-event |

This manifest is a family-level production requirement. The asset owner expands it into individual paths after the design anchors and engine consumers are accepted. It does not authorize dozens of unnecessary near-duplicate icons merely to hit a quantity.

## Focus and action icon families

The eye family uses a recognizable organic eye and political documents. The cell family uses concealed networks, factory doors, pamphlets, and rail maps. The army family gives each tool and vehicle a distinct silhouette. Foundries use furnaces, casting forms, rails, machinery, and repaired armor. The international family distinguishes joined hands and congresses from binding cords, stamped orders, and occupied institutions. Continental commands combine their regional function with the same command grammar. The Red World family shows increasingly unified institutions and altered humanity without adding an unrelated fantasy visual language.

Independence needs an unmistakable visual break from submission. Its icon should remain clear even when the player has very little political power, a transformed leader, and an urgent annex countdown. The icon is an action cue. It must not depend on reading a long tooltip to distinguish it from accepting further dependence.

## Animation requirements

The category animation can show the eye opening, workers gathering, factory activity changing, and distant revolutionary points appearing. Those changes require genuinely different authored or generated frames. Panning, zooming, rotating, flickering, or recoloring one still image does not satisfy the real-frame requirement.

Leader animation is narrow and deliberate. Eye movement, lid motion, tissue movement, and a restrained supernatural change can communicate life without making the entire portrait distracting. The static fallback should preserve the same stage and meaning. Animation must stop or change appropriately when the event is defeated or the leader is no longer eligible.

For alpha-backed consumers, every generated source and animation frame requests native transparency at the initial image-generation call (the `gptimage` MCP route in `chaos-redux-event-assets`) and preserves alpha through processing. Record background removal only as a validated fallback.

The production owner checks actual sprite-sheet dimensions, frame order, alpha, timing and native registration, and records the generation route actually used for each frame set.

## Model and held-item production

All eight core families require custom visual treatment. The latest 3D pipeline is authoritative over older project wording. Body geometry begins from one approved colored whole-object reference with empty hands where held items will be attached. Every held item, including firearms, hammers, sickles, engineer tools, and other equipment, is a separate Meshy 7 geometry task under the current pipeline. Older direct-Blender firearm instructions are superseded for this package.

Each role receives one bounded provider biped-rig attempt and one action attempt where the approved provider route applies. Failed provider output moves to the live Blender workflow under the latest skill. Paid attempts are tracked through the current ledger and approval rules at production time. Planning does not spend credits or imply approval for an unlimited attempt loop.

References for model generation must meet the current source requirement for usable modern professional non-anime concepts with appropriate rights. Historical archival photographs can inform research, but they are not automatically suitable whole-object model references. Each body and item needs a source or generation decision that fits its technical purpose.

Scale is measured against the actual vanilla comparison object. It is not guessed from a nominal human height. Held tools need convincing grips, hand contact, strike arcs, ground contact, and collision avoidance. Vehicle and cavalry packages require actual crew or rider relationships appropriate to the chosen entity representation.

The final action set covers idle, selection, movement, combat, and death roles. The animator authors real skeletal changes through the live supported workflow, exports them, reimports them, and checks the actual game entity. A repository script declaring a rig and a few keyframes is not the final authored animation.

Textures follow the current model pipeline. Use BC1 diffuse and BC3 normal and packed specular textures with full mip chains where those are the verified consumer requirements. The packed specular channels preserve their documented meanings. Typical textures are 512, with 1024 justified by the actual asset. Older blanket uncompressed-DDS and oversized-texture rules do not override the latest model workflow.

## Audio design and research

The three musical cues must be unique structured music with a beginning, development, and an ending suitable for the super-event. The opening needs collective movement, industrial insistence, and unease. Red World needs a different and more absolute terminal progression. Defeat needs reflective weight and a sense of survivors facing the consequences.

Use the current music catalog first to prevent reuse. The pinned catalog already assigns playback audio ID 91 to a Brilliant Scientist cue, so Event 091 must not assume that audio ID 91 is available. Event number, visible display slot, and playback audio ID are different namespaces. All three are audited separately before implementation.

Music research must verify the composition, lyrics if any, arrangement, performance, recording, source file, license or public-domain basis, attribution, derivative rights, and actual excerpt. An old composition does not make a modern recording free to redistribute. A page's general license does not automatically cover an embedded recording. Candidate status is explicit until those checks pass.

The final musical excerpts should be approximately one to two minutes and no longer than two minutes under the latest super-event workflow. Exact in and out points follow listening and phrase structure. The planning package may recommend a window for audition, but it does not claim an unlistened timestamp is a validated musical cut.

Generated tones, placeholder marches, generic drones, and reused unrelated super-event cues do not satisfy this requirement. Mechanical trimming, normalization, fading, and conversion of a properly licensed source are production steps after source acceptance. They are not a substitute for finding the right music.

## Unit sound roles

| Family | Required sound character | Routing and source caution |
| --- | --- | --- |
| Awakened Workers | Collective labor cadence, heavy breath or unnatural absence of it, tools and basic arms | Avoid assigning altered voices to ordinary human formations through a broad tag override |
| Hammer Guard | Weight, metal impact, short coordinated commands, controlled strain | Source impacts with credible force and avoid an identical hit on every attack |
| Sickle Host | Restrained movement, blade contact, low coordinated calls | Night or infiltration character should not make the unit literally silent in all game contexts |
| Red Motor Columns | Engines, mechanical wear, workshop repairs, altered crew commands | Differentiate vehicle material from magical ambience, with appropriate loop behavior |
| Revolutionary Cavalry | Horses, tack, riders, movement, regional commands where verified | Rights and language authenticity apply to voices as well as music |
| Foundry Brigades | Armor movement, metal stress, cannon and crew roles | Match actual equipment and animation timing |
| Third-Eye Commissars | Clear command identity, unsettling synchronized replies, limited ritual accents | No generated or manually synthesized final voice package |
| Red Engineers | Tools, rails, machinery, construction and demolition roles | Distinguish civilian work, movement, and combat without constant noise |

All final custom sounds are internet-sourced with a documented redistribution basis. The latest voice workflow specifies signed 16-bit PCM at 44.1 kHz mono where that matches the consumer. Other sound roles follow the inspected consumer rather than a guessed universal encoding. Record the original source and final converted file hashes during production.

## Visual QA and acceptance

Inspect flags decoded at all three sizes, icons at native size, portraits with ordinary and unusually shaped leader images, category animation with its fallback, focus trees at normal zoom, and units at the actual tactical map scale. Check politics and diplomacy views separately. Compare native screenshot states at 1920 by 1080 and scale 1, then the supported resolution and UI-scale matrix.

The signature package is not complete because files exist. The user must be able to recognize Lenin, distinguish the eight army families, understand the current transformation stage, see the meaning of the main decisions, hear three distinct musical roles, and play without clipped or displaced overlays. The production handoff assigns evidence to each requirement.
