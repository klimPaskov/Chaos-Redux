# 070 Cookie Click: visual assets, animation, models and sound

## Art direction

The living cookie is the visual center of the system.
It begins as a small warm biscuit with a readable face and becomes decorated, crowned, larger and increasingly hostile.
The surrounding interface remains recognizable as an HOI4 interface.
Its cookie, rewards and reactions can be colorful without turning every panel into a separate bright control.

The Cookie Monster is an original continuation of that same creature.
Its chips, cracks, icing, crown and facial proportions preserve the identity established during feeding.
Its country and army use baked material, wafer structures, chocolate armor and working oven machinery.
A model family must remain recognizable at the game's ordinary map scale.

All asset names and role descriptions here are production identifiers.
They are not final player-facing localization.
No historical portrait or flag is required for the original Monster.
Existing historical countries used as subjects retain their appropriate sourced identity assets.

## Finite visual inventory

| Family | Required coverage | Planned consumer and output |
| --- | --- | --- |
| Cookie body bands | Six coherent bodies for Levels 1–4, 5–9, 10–19, 20–29, 30–49 and 50+ | Event-owned clickable window, 320 × 320 display design with exact native consumer verified |
| Expression coverage | Eight readable expressions across all six bands, 48 supported pose combinations | Satisfied, happy, expectant, hungry, starving, angry, threatening and revolting |
| Evolution appearance | Three additive evolution treatments and an ordinary untreated state | I material appetite, II watchful intelligence, III exposed destructive form |
| Progress controls | Fullness bar, Level identity, daily count area, milestone states and warning state | Native controls with separate artwork, never text baked into a screenshot |
| Click and reward effects | Crumb, sparkle, heart, reward burst, damage chip, smoke and warning fracture families | A bounded effect pool and supported native sprite consumers |
| Pet event reports | Arrival, first major growth, first material theft, weak death, warning and recovery | Six report compositions, 210 × 176 target using the project report pipeline |
| World news | Uprising, first settled Cookie region, first subject, global campaign and defeat | Five news compositions, 397 × 153 target |
| Super-event images | Uprising, Final Bite launch and final Cookie-world result | Three distinct 457 × 328 compositions |
| Monster portrait | One consistent character with neutral, active and threatening motion roles | 156 × 210 animated portrait plus static fallback |
| Institutional advisors | Bakery administration, logistics command and shaping office | Three symbolic 65 × 67 advisor portraits |
| Commanders | Six fictional Cookie officers with distinct silhouettes | Role-correct leader portraits, no invented historical identities |
| Country flags | Core Empire identity and four governing-method cosmetic treatments | Large 82 × 52, medium 41 × 26 and small 10 × 7 TGA outputs per identity |
| Domain emblem | One Cookie-domain diplomatic emblem | Actual supported faction or category consumer, not an unused decorative file |
| National spirits | Three lifecycles with clear stage variants | 64 × 64 idea icons, variant count derived from actual live idea stages |
| Focus icons | Every final focus node in all seven branches | 94 × 86 targets and exact route-to-icon manifest, no generic icon assigned to every focus |
| Decision icons | Every distinct operation family and meaningful crisis state | 32 × 32 target, reuse only when the action meaning is genuinely shared |
| Technology icons | Every implemented Cookie technology node | 64-pixel or 132 × 52 consumer as established by installed templates |
| Equipment art | Every Cookie equipment family and meaningful tier | Dimensions taken from its actual production and technology consumer |
| Unit counters | Six ordinary families and two world-end families, with supported variants | Bespoke large counters, small map counters and division-template consumers |
| Achievement icons | Fourteen authored achievements | Earned, unearned and disallowed 64 × 64 states for each |
| Opponent category picture | One reusable anti-Cookie response composition | Eligible static ordinary decision category only |
| State-shape pieces | Conditional exact territorial formable consumer only | Not required for this dynamic global state-share campaign without a fixed state set |

The listed UI display size is a composition target.
The asset worker must verify native slot dimensions before final export.
Do not describe a guessed display size as a measured vanilla requirement.
Focus and technology inventories are closed against actual final node manifests before generation starts.
Unassigned generic art is not considered coverage.

## Native animation plan

Create genuine changing frames for body compression, settling, facial reaction and transformation.
A static cookie moved up and down by a transform does not satisfy the requested squash animation.
A still portrait with only an added glow does not satisfy the animated leader requirement.

The following are initial production frame counts.
The frame-animation worker can adjust them after measuring native timing, while preserving each behavior and the coverage manifest.

| Animation | Coverage | Initial frame plan | Playback rule |
| --- | --- | --- | --- |
| Idle breathing and blinking | Six body bands | 8 frames per band | Slow loop only while visible |
| Accepted click | Six body bands | 8 frames per band | Restart or merge short reactions without losing authoritative clicks |
| Full feeding reaction | Six body bands | 12 frames per band | One playback at the completed daily target |
| Hungry movement | Six body bands | 8 frames per band | Occasional movement with readable discomfort |
| Severe threat | Three advanced bands | 12 frames per band | Short warning loop with real facial change |
| Weak starvation death | Two eligible weak bands | 16 frames per band | One-way dry, crack, collapse and empty result |
| Revolt transformation | Appropriate starting advanced forms | 24 frames per supported transformation source band | Gameplay is already locked before playback |
| Monster portrait | Neutral, active and threatening roles | 12 frames per role | Role-aware loop with a static fallback |
| Crumbs and sparks | Seven effect families | 6 frames per family initially | Short bounded bursts, no permanent accumulation |

Expressions can be assembled from approved compatible body and face assets where the engine supports this cleanly.
The expression matrix still has to cover all 48 required combinations.
Mouth placement, eye anchors and clipping must be checked at every body band.
Do not assume one small-cookie mouth texture will fit the final monster.

The evolution treatment is layered only where the current renderer supports the required ordering and alpha.
Otherwise export a finite set of composed approved variants.
The implementation cannot claim all 192 possible combinations are covered merely because four source layers exist.
A coverage sheet must show which actual combinations are used and how they render.

## Motion and accessibility

Every accepted click provides supported visible feedback.
Repeated input can coalesce decorative particle counts, but cannot reduce actual accepted clicks or alter milestones.
Use a fixed effect pool and a visual pulse when the pool is saturated.
Actual reward numbers appear only after a real grant.
Ordinary per-click numbers show progress, not invented currency.

Reduced-motion mode uses the static approved pose for the current semantic state, clear progress changes and minimal nonmoving confirmation.
The state remains readable without sound or color.
Low Fullness uses text and shape cues as well as its hue.
The accessible fallback is an intentional alternative mode.
It does not prove that the ordinary animated implementation is finished.

Do not cover the click target with particles, warning overlays or reward labels that capture mouse input.
The hit region stays stable through squash, growth and transformation.
The old feeding action becomes disabled as soon as the revolt is committed.

## Country identity assets

The base flag uses a clear biscuit emblem readable at the smallest size.
The four method variants change one strong motif, such as a working field, shaping mold, traveling furnace or consumed structure.
They must remain members of the same original country family.
The exact geometry is created during art production and checked at all three native sizes.

The governing method changes the country's visible political and administrative identity through the supported cosmetic route.
The Monster remains the leader.
No additional invented head of state is needed to make the branch appear political.
The three institutional portraits have distinct functions and are not generic faces used to fill every advisor slot.

Prepared feeding territories and directly converted regions receive appropriate decision and map-state icons.
There is no need for a custom 3D bakery building unless the final implementation adds a real visible map entity with an actual consumer.
Such an addition would require its own model profile and cannot be represented as already included by an unrelated focus icon.

## Unit model profiles

| Family | Required silhouette and motion | Component plan | Counter and equipment identity |
| --- | --- | --- | --- |
| Cookie Infantry | Biscuit soldier with flexible dough joints, march, aim, fire and crumble death | Weapon-free body plus separate firearm model and manually fitted rig | Upright biscuit soldier and simple rifle motif |
| Crumb Swarms | Several small articulated crumb creatures acting as a coherent formation | One authored swarm family with controlled component and bone budget | Cluster silhouette that stays readable at native size |
| Chocolate Guard | Broad chocolate armor over a distinct biscuit body, deliberate disciplined motions | Body, armor structure and separate firearm, with all parts counted in scale and export | Shielded chocolate profile |
| Dough Golems | Heavy soft-mass creature with visibly different stride, strike and collapse | Nonhuman rig profile and articulated body, no disguised vanilla infantry skeleton assumption | Heavy dough fist or body silhouette |
| Oven Artillery | Wheeled oven carriage with crew, recoil, loading and smoke | Chassis, moving doors or barrel, crew and required effect locators | Recognizable oven-gun silhouette |
| Wafer Riders | Mobile wafer mount and cookie rider with coherent joined movement | Mount and rider profile, appropriate weapon component, synchronized movement | Mounted wafer outline |
| Great oven formation | Large slow mobile furnace, working machinery, fire and breakdown | Heavy vehicle profile with every visible moving component counted | Large furnace silhouette distinct from ordinary artillery |
| Monster Guard | Advanced guarded biscuit form tied to the Monster's identity | Original elite body and separate firearm or explicit non-firearm weapon profile | Elite crown and guard motif distinct from Chocolate Guard |

Cookie Infantry, Chocolate Guard and any firearm-equipped Monster Guard use separate body and firearm generation jobs.
The dedicated 3D pipeline is the operative source for that separation.
Some other supplied profiles contain older conflicting firearm shorthand.
Resolve their task instructions before execution.
Do not generate a weapon fused into a body's hands and then call it a separate-weapon pipeline.

Each paid geometry job uses one clean approved reference image showing the intended object.
A multi-view board, collage or turnaround sheet is not a valid substitute input.
Reference approval precedes the paid job.
The provider model and capabilities must be verified at execution, with the dedicated skill's Meshy-7 requirement treated as a locked requirement until explicitly revised.

For firearms, perform the manual Blender fitting, arms, aiming, recoil and firing animation work required by the dedicated pipeline.
Do not send the armed character through a generic provider auto-animation flow.
For other supported profiles, follow the stated single permitted provider rig or action attempt before the specified Blender fallback.
Conflicting retry authorization in older profiles is resolved before paid work.
No paid work was performed by this planning package.

## Scale, actions and export

Measure an actual suitable installed-vanilla reference for each model class.
Record its source geometry dimensions, effective entity scale, required map readability and the chosen conversion.
Apply the scale correction once.
Do not assume a universal 1.8-meter character height or stack an object-scale correction with an equivalent entity-scale correction.

Include weapons, mounts, crew, doors, barrels and other visible components in the geometry and performance budget.
Each profile needs a declared budget based on the reference class.
A small body file does not prove a low-cost entity when several uncounted attachments are added.

Required actions include idle, movement, attack, supported combat posture and death.
Artillery and firearm attacks require correctly placed and timed muzzle, smoke or firing locators.
Movement must articulate the actual model rather than translate a rigid sculpture.
Death must reach a valid stopped pose without leaving a floating weapon or detached crew.

Export through the current supported pipeline, then reimport the exported files.
Verify skeleton, materials, texture assignments, scale, locators and action names from the exported result.
A Blender viewport render alone does not prove that the game consumes the model.
Required live evidence includes each family moving, fighting and dying at normal map zoom.

## Counters and templates

Each of the eight families needs its own counter identity.
Inspect the installed large-counter, small-counter and division-template consumers.
The expected large land-counter family uses 152 × 42 with two 76-pixel frames, while other consumers use their inspected native geometry.
Verify the 76 × 42 and 30 × 12 template-related roles before export.

Sample the actual installed vanilla green palette and preserve its evidence.
Do not choose an approximately green color by eye.
Keep silhouettes centered and legible with the native overlays, selection states and text.
A counter that looks correct alone can still fail under a division number or equipment icon.

## Sound and voice

The living cookie needs sourced click, crumb, happy confirmation, full-feeding, hunger, crack, warning and transformation sound roles.
The Empire needs unit selection, movement acknowledgement, attack acknowledgement and action sound roles where the engine actually supports them.
Use a distinct coherent Cookie sound identity, with pitch and texture suited to the material.

The final audio must be sourced from permitted Internet material with attribution and license evidence.
Do not generate new final audio, synthesize a substitute, or record a new voice performance under a profile that requires sourced sound.
Editing permitted source audio into shorter cues is allowed when the source license permits it.
Preserve source file, author, license, retrieval date, edit notes and final consumer mapping.

Country-level selection and acknowledgment consumers can be shared across unit families.
Do not promise a different voice set for each battalion family unless the actual game supports that binding.
Per-action Foley can remain family-specific where a verified consumer exists.
Artillery, firearms, mounts and creature strikes need source-backed timing aligned with their actual attack frames.

No final unit sound recording is selected in this package.
That is an open asset-production requirement, not a completed audio pass.
The super-event research file identifies a music candidate separately and does not grant a license to arbitrary effects from the same website.

## Export and quality evidence

Use the project-specific output paths and naming rules after checking existing runtime consumers.
Keep temporary originals, prompts, references, frame manifests, provider receipts and export evidence under the event-owned asset workspace until review.
Promote final runtime assets only after their actual consumers are known and tested.

For the project's strict uncompressed DDS route, verify the expected header and pixel byte count, alpha and round-trip image.
Do not silently substitute a different compressed format.
Flags retain their required TGA orientation and dimensions.
Actual exceptions need an inspected consumer and a documented reason.

The asset manifest includes asset ID, purpose, exact consumer, source mode, dimensions, frame count, variant coverage, source provenance, export proof, final path and live validation state.
Every final focus, decision, technology, unit, achievement and portrait consumer has a matching asset.
Unused files are not counted as fulfilled requirements.
