# 068 ZIN: assets and visual handoff

## The visual system

The event should show societies with distinct histories and equipment, while keeping a coherent Hearts of Iron IV presentation. Its fantasy subjects do not need to resemble spacecraft invaders. The source maps define geography and identity. They are not concept sheets proving the exact face, armor or anatomy of an unpictured character.

`registries/068_zin_asset_requirements.json` enumerates country, character, unit, map, super-event and interface requirements. Every row is a planned requirement. None is marked as a produced or installed asset. A unit visual job can share a compatible underlying animation source through an approved family workflow, but it cannot silently omit distinct anatomy, counters or regional identity.

## Country presentation

Every one of the 44 full arrival packages receives a readable public country identity, its own fictional leader portrait, flags, focus icon family, decision and idea icon family, correct homeland news art and a country-specific narrative package. The country registry supplies political and artistic direction.

The four additional Rush dominions need separate presentation when they become sovereign or succession countries. The Golden King, Einendil, Afrit's Rush-crown form, the civil, military and treasury regents, and the Free Dominion leadership need dedicated character direction. Reusing Afrit's face across his legitimate states is correct identity continuity. Reusing another unrelated character's portrait with a new filename is not.

A regional orc, goblin, troll or ogre ruler should look like the relevant society. Do not give every monster country one generic hooded portrait. Dondor leaders are human. Sunhot elves are physically exceptional but peaceful in their normal diplomatic portrayal. Volgan's visual identity centers on ancient command and grave power. Afrit centers on worship and captured authority, with a distinct crowned form when he actually takes Rush.

## Native output contracts

The following dimensions come from the inspected project asset guidance and must be rechecked against the exact installed consumer before production. They are not evidence that a texture was rendered or tested here.

| Surface | Planned output | Review |
| --- | --- | --- |
| Leader portrait | 156 x 210 | Subject identity, head-and-shoulders framing, native-size clarity and exact character reference. |
| Large flag | 82 x 52 | Correct proportion, readable symbol and political variants. |
| Medium flag | 41 x 26 | Coherent downsampled identity. |
| Small flag | 10 x 7 | Simple silhouette that remains distinguishable. |
| Focus icon | 94 x 86 | HOI4 visual family, alpha and actual focus consumer. |
| Idea or achievement icon | 64 x 64 | Clear central symbol and no illegible detail. |
| Decision icon | 32 x 32 | Readable action family and exact state variants. |
| News image | 397 x 153 | Source-aware composition, approved black-and-white treatment and readable homeland geography. |
| Report image | 210 x 176 | Approved report treatment and composition. |
| Super-event image | 457 x 328 | Exact display crop and scene hierarchy. |
| Unit counters | Inspect installed family | Exact native canvas, frames, alpha and sampled vanilla green. Never guess from another counter family. |
| Models and textures | Inspect installed domain | Measured scale, actual material channels, texture limits and runtime entity. |

A format conversion is not an artistic enhancement. Native ImageGen creates or faithfully prepares art when required. Mechanical tools may crop, resize, assemble approved frames and convert textures under the owning skill. They must not substitute coded drawings for requested original art.

## Source-map news images

Keep the thirteen original map files unchanged under the durable source directory. A runtime derivative should be a region-aware crop or an approved fitted full-map view. Preserve coastline, relative geography and the visible source character. Do not generatively redraw labels, add invented islands or make an uncertain spelling look authoritative.

The extreme aspect ratio of Magical Lands needs a deliberate regional crop. Compressing the whole vertical sheet into a wide news panel would make its geography unreadable. Rush and Cold Lands likewise need several reusable homeland crops rather than a random image detached from the arriving society. The full original remains accessible in this documentation and the reader.

Prepare separate derivatives for the actual news and report consumers. Record original checksum, crop rectangle, scale, color treatment and output checksum. Compare the derivative to the original at native size. The output must retain a recognizable homeland even if every tiny handwritten label cannot remain readable.

The Worshipdom and Yeldenne lack a confirmed homeland sheet in the brief. Their arrival art remains a source question. A Rush court scene can illustrate Afrit's actual political activity, but cannot be mislabeled as the map of his homeland. Do not silently select Dark Lands merely because Afrit is hostile. Resolve those two references or obtain approval for a non-map exception.

## Flags and symbols

Use one strong society symbol with political variants that remain readable at the smallest size. Rush's royal, popular, regency, federal and Afrit-crown forms should share a recognizable lineage without identical flags. Dominion marks should remain identifiable when they enter a larger federation or become corrupted.

Symbols derived from a source map are new fictional design proposals unless the map actually depicts a banner. A place called Asgard, Heaven, Nether or Isengard is not permission to copy a real religious symbol or another game's emblem. Real flags or historical symbols used for Earth governments require source-based handling under the asset skill.

## Models and scale

Create a measured reference plan for human and elven infantry, mounted units, giants, ents, trolls, ogres, yetis, demons, mycids, grave hosts, dragons, wargs, mammoths, other Mazerin beasts, ships and the castle. The military registry identifies exact unit consumers and regional requirements.

The 3D production worker must begin with the current owning pipeline's environment and dependency gates. This planning package makes no provider calls and authorizes no new runtime claims. The accepted production path requires a real inspected reference, one approved model-ready image, a verified provider route, immediate preservation of results, and exact source-to-runtime lineage.

The inspected current 3D owner uses a modern-artwork source-first path followed by faithful ImageGen preparation of a separate derivative. It rejects source restrictions incompatible with that use. A source-free design route requires its separately documented approval after the stated search gate. This is stricter than some older general asset guidance. Refresh and follow the owning 3D skill rather than silently applying an older broad redesign instruction.

A generic licensed concept must not silently redefine a canonical ZIN character. For unique characters and unprecedented creatures, obtain approval for the actual reference or a suitable original route. Preserve the approved subject's anatomy, equipment and identity. Meshy receives one full-color model-ready image, not a turnaround sheet or a collage.

Measure the installed vanilla reference source mesh and its entity scale. Distinguish provider-space dimensions, normalized exported dimensions and effective in-game dimensions. Apply the scale conversion once. A Sunhot model must convey the specified height relative to humans without assuming that real-world meters equal the game's mesh units.

Nonhumanoid creatures need a dedicated compatible rig map. Every required idle, movement, attack, defense and death action needs real semantic motion. A transform-only rotation, repeated static pose or renamed walk cycle does not satisfy a dragon attack or an ent death. Provider animation is a candidate until its anatomy, contact and action meaning are reviewed. Export and reimport the actual mesh and animation bytes before handoff.

## Castle and Glo

Yeldenne's castle is a single visible provincial landmark at the stored founding province. It is not a national idea pretending to be a building. Its model has a dedicated spawn identity and a measured footprint, with the actual province and state connection recorded.

The castle persists through ordinary occupation, annexation, liberation and changes of capital. Glo's power follows the controller of the containing state. The castle's legal owner, Horos's current location and control of one individual province do not override that rule.

The production and integration team must prove placement across admitted founding locations. A nice Blender render is insufficient. The model, entity, building definition, spawn point and map position must all agree in game. Broad generic cleanup must not delete the only castle or create a second copy when a country is restored.

## Unit sound and counters

Unit audio is sourced recorded material with explicit rights and provenance. Search by the actual sound role and creature or weapon identity. Preserve originals and record any permitted trim, fade, resample and conversion. Do not synthesize creature voices, build test-tone substitutes or borrow unlicensed audio from a commercial game.

Each distinct unit needs the applicable selection, acknowledgement, movement, attack, impact, special-action and death roles supported by its actual consumer. A named soundeffect without an engine binding is not a working sound. Where selection routing is country-wide, document all affected infantry consumers and avoid overwriting ordinary Rush or Earth voices with a single creature sound.

Counters require new art for each used surface, the exact inspected vanilla green palette, proper frame order and native dimensions. An arbitrary green icon or a renamed vanilla counter does not satisfy the requirement. The icon worker returns original source, processed alpha image, DDS, native-size contact sheet, decoded comparison and runtime handoff.

## Animation choices

Static portraits and interfaces are acceptable defaults where motion adds no information. Optional animated portraits are reserved for Einendil's accepted reveal, Afrit's crowned state, Volgan's direct arrival and other approved identity transitions. Optional Glo or corruption indicators can communicate an active or dangerous state.

An accepted 2D animation needs planned and produced individual frames, consistent subject identity, frame order, timing, loops and static alternatives. A scaled or translated copy of one image is not a finished animation. The static alternative exists for a supported display state, not as an undisclosed replacement for promised motion.

## Handoff and durable evidence

Source material, working assets and runtime files remain separate. Temporary production evidence belongs in the event-owned workspace while work is active or blocked. Promote durable attribution, licenses, source hashes, coverage and runtime binding facts into permanent documentation before removing a completed temporary workspace. Never delete the thirteen user source maps as temporary assets.

The main agent owns final gameplay, GFX, entity, sound-definition and shared-interface wiring. Asset workers deliver bounded outputs and manifests. The final review must compare actual installed hashes against the selected approved outputs so an older file cannot silently overwrite a newer accepted asset.

No final portrait, icon, model, animation, counter, sound, music cut, DDS or scripted GUI is included here. This is the production specification and requirement inventory.
