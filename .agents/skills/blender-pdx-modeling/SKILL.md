---
name: blender-pdx-modeling
description: Build a true volumetric Blender character or unit model from an uploaded photo or image reference, using imagegen only to make a 2D concept sheet first and Blender MCP to create real 3D mesh geometry, armature/bone structure, materials, scale checks, and inspection renders. Use when the user asks Codex to analyze a photo, recreate a reference in Blender, make a PDX/HOI4-style model, create a rigged unit model, or prepare a model workflow for later PDX mesh export and Chaos Redux in-game wiring.
---

# Blender PDX Modeling

## Core Rule

Create a real 3D Blender model. Do not finish with a billboard, image plane, sprite, flat card, 2D cutout, alpha extrusion, textured silhouette, or any other fake-3D stand-in.

Use imagegen only to create a concept/reference image. Never use the generated image as the final model geometry or as a texture pasted onto a flat surface.

If no photo or reference image is available, ask the user to upload one before modeling. If the user wants a PDX/HOI4-compatible unit, always import a vanilla model first and read scale, facing, origin, and armature structure from it.

Do not report a simplified proxy, primitive mannequin, toy-like blockout, or loosely themed placeholder as complete. If the result does not visibly match the supplied concept/reference in silhouette, anatomy, clothing layers, surface condition, and material read, delete or clearly mark the failed attempt and keep iterating. Completion requires a model that would be reasonable to hand to a human artist for polish/export, not merely a technically rigged arrangement of primitives.

## Required References

For PDX/HOI4 work, read [Blender PDX Modeling](references/blender-pdx-modeling.md) before touching Blender. Read [Chaos Redux Integration TODO](references/chaos-redux-integration-todo.md) before claiming anything about export, animation, textures, or in-game wiring.

## Workflow

1. Inspect inputs.
   - Confirm the uploaded image role: main reference, style reference, or supporting reference.
   - If the request is vague, infer the target object from the image and state the modeling target briefly.

2. Create a 2D concept reference with imagegen.
   - Use the uploaded photo as visual guidance when available.
   - Ask imagegen for a clean model sheet or concept reference: front view, side/back cues if possible, neutral pose, readable silhouette, material callouts.
   - Save or locate the generated image for visual inspection, but do not import it as final geometry.

3. Prepare Blender through MCP.
   - Clear the scene only if the user asked for a clean scene or the current scene is unrelated.
   - Verify Blender MCP is connected.
   - Verify PDX tools when making a PDX/HOI4 model.
   - Import a vanilla reference model and keep it visible as a ghost/wire reference.

4. Measure, do not guess.
   - Read imported reference bounds, origin, facing, armature object, root bone, bone names, and parent hierarchy.
   - Use the reference height and ground plane for model scale.
   - Infer facing from the imported rig and helper nodes. Do not hardcode `-Y` unless the inspected model confirms it.

5. Build true 3D geometry.
   - Use actual meshes with volume: torso, head, limbs, hands, fingers, boots, clothing, straps, pouches, accessories, wounds, and surface details.
   - Model side and back surfaces, not just the camera-facing view.
   - Use bevels, smoothing, modifiers, sculpt-like mesh deformation, separate detail meshes, or joined mesh parts as appropriate.
   - Use real Blender materials and UV/image textures only as surface detail on real mesh, never as a substitute for geometry.
   - For humanoid PDX units, prefer a measured vanilla mesh or armature-compatible base mesh over assembling the main body from spheres, cones, and cylinders. Primitives are acceptable only as temporary scaffolding or small accessories; they are not acceptable as the finished body, face, clothing, or hands.
   - Build clothing as layered, fitted, damaged garments with believable hems, seams, collars, cuffs, wrinkles, tears, and thickness. Do not represent clothing with a few flat-looking triangles or generic tubes.
   - Build faces, hands, claws, wounds, teeth, and exposed bones as integrated anatomy. They must not look like loose blobs, decals floating off the body, or disconnected props.
   - Use procedural materials, UV painting, or texture maps to create meaningful surface variation. Do not claim "proper textures" when the result only has flat diffuse colors or generic noise.

6. Rig and weight.
   - Duplicate or construct an armature compatible with the imported reference.
   - Preserve the root bone and hierarchy needed by the PDX exporter.
   - Add exactly one armature modifier to each skinned mesh.
   - Create vertex groups matching bone names and assign meaningful weights.
   - Keep helper objects, lights, cameras, and reference planes out of export selection.

7. Validate in Blender before completion.
   - Inspect front, side, back, and angled views.
   - Confirm the model has real thickness and recognizable forms from side/back.
   - Confirm feet sit on the ground/origin convention from the imported reference.
   - Confirm the model is selected with its rig, materials assigned, modifiers visible/renderable, and reference still available.
   - Render or viewport-check at least front and side views.
   - Compare the renders directly against the concept/reference sheet. Check silhouette, proportions, face, hands, clothing damage, gear placement, and material read. If the model reads as a primitive blockout, toy, mannequin, or generic reskin, it has failed validation.
   - Inspect renders without hiding behind a reference overlay. Use a ghosted vanilla reference only for scale/facing validation, not as a way to obscure model quality.

## Failure Conditions

Stop and correct the scene before reporting completion if any of these are true:

- The final result is mostly an image plane, alpha cutout, silhouette extrusion, or billboard.
- The model only looks correct from the front.
- Scale, facing, origin, or bone structure were guessed instead of measured from the imported reference.
- The mesh has no real limbs/body volume, no back/side detail, or no usable armature relationship.
- The imagegen output is being used as the model instead of as a reference.
- The model is mostly primitive spheres, cylinders, cones, cubes, or disconnected accessory pieces.
- The model looks simplified, toy-like, mannequin-like, or visibly unlike the concept/reference.
- The face, hands, wounds, or clothing details look like pasted-on blobs, floating markers, loose sticks, or random debris.
- Materials are only flat colors or generic procedural noise while the user asked for proper textures or a realistic material read.
- The completion report would need to excuse the result as "rough", "blockout", "proxy", "placeholder", "first pass", or "needs artist polish" when the user asked for a finished model.
- The validation renders would embarrassingly fail a direct side-by-side comparison with the concept/reference sheet. In that case, do not present them as complete; either continue iterating or report the task as incomplete.

## Completion Report

Report:

- Reference image(s) used and whether imagegen was used.
- Vanilla model imported and measured.
- Final Blender object names for model, armature, materials, camera, and reference.
- Scale/facing/origin facts from the scene.
- Validation views checked.
- Any limitations, especially if export, animation, texture baking, or Chaos Redux wiring remains TODO.
- Honest quality status. If the model is still a blockout, proxy, or incomplete artist handoff, say so and do not call the goal complete.
