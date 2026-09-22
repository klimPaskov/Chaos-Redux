# Mounted model and animation handoff

## Ownership and readiness

The mounted model is a required custom-unit deliverable. The 3D pipeline role owns the complete asset, and the main agent owns integration and final acceptance. No Meshy or Blender tools were connected or invoked during this planning session. No paid task or runtime asset was created.

Before production, read the current owning 3D skill and its referenced local files. Resolve the profile conflict noted in the conflict register. The owning skill's separate Meshy firearm geometry rule takes precedence over a shorter profile description that suggests making the gun directly in Blender.

## Source gate

Select one eligible modern professional game or tabletop concept-art image for the weapon-free horse-and-rider body. The image must support the accepted identity without unauthorized redesign. Confirm rights for the intended use. Archival, museum, and historical-plate material can support research but does not satisfy this geometry-source requirement.

Select a separate eligible image for each required firearm geometry task. Exactly one image is used per geometry task. Do not submit a multi-angle board as a shortcut. If suitable rights-cleared sources cannot be found, return the source blocker and seek the required explicit alternative approval. Do not claim source approval because an image looks useful.

## Geometry and assembly

Use fresh Meshy 7 geometry for the weapon-free body and separate Meshy 7 geometry for each firearm. Verify the actual model selector and API schema before submission. Do not guess an endpoint or silently use another model.

The firearm route proceeds to direct Blender assembly, rigging, manual animation, attachments, and export. Do not use paid Meshy auto-rigging or animation as a substitute for this required route. Failed rig or action work is handled through the owning skill's Blender recovery workflow rather than repeated paid retries.

Horse and rider require a compatible nonhumanoid rig. Validate body separation, saddle contact, stirrups, hands, reins, weapon grip, and ground contact. A humanoid auto-rig cannot be assumed to support the combined anatomy.

## Calibration

Inspect a relevant vanilla mounted or comparable unit read-only. Record source and runtime scale, axes, origin, contact plane, visible height, material handling, and entity settings. Do not assume a default human height or estimate scale from a screenshot alone.

The final geometry and materials must preserve the intended silhouette at normal map zoom. Reduce complexity only when it preserves that identity and satisfies measured game constraints.

## Materials

Prepare the exact color, normal, and material channels expected by the game. Convert roughness to glossiness where required, inspect each channel independently, and resize channels correctly. A material that looks plausible in Blender can still be incorrect in the game's shader.

Keep preview interpretation separate from final engine channel packing. Record source maps, conversion steps, final hashes, and material consumers.

## Animation and effects

Provide every animation state consumed by the final entity. Required states normally include idle, move, attack, defend, support attack, retreat, death, and training. The exact local entity contract decides any additional states.

Firing motion must show aim, discharge, recoil, and recovery with a valid weapon locator and the required effects. Movement must keep feet and hooves in plausible contact. Review loop phases at the start, quarter, middle, three-quarter, and end. Death contact is checked across the body, not only by finding the lowest vertex.

Check quaternion continuity, transitions, and the reimported exported asset. A successful Blender preview is insufficient if the exported animation changes or the entity plays the wrong state.

## Sound and selection

Use real licensed online sources for weapon, movement, and selection sound. No generated or self-recorded substitutes are allowed under the supplied skill. Preserve original files, source evidence, license terms, and hashes. Mechanical derivatives are allowed only where the license permits them.

Inspect the actual selection-voice consumer. The profile notes country or original-tag infantry idle consumers as a relevant pattern. Do not overwrite all ordinary infantry voices to make one custom cavalry unit speak. If the engine cannot separate the consumer, return that conflict with a narrowly reviewed alternative.

Where the existing workflow requires PCM16 mono 44.1 kHz, verify the actual final file with format inspection. Do not merely rename the extension.

## Final proof

Required evidence includes source approval, geometry task provenance, calibration, Blender assembly, material-channel review, all animation states, exported mesh and animation reimport, effects and sound consumers, correct model selection, and live-game behavior. Record the runtime file hashes used for review.

The event cannot claim its custom mounted unit is complete while a placeholder model, missing state, absent sound, or unverified runtime consumer remains.
