# In-Game 3D Model Validation Checklist

## Identity and placement

- [ ] Correct model appears for the intended consumer.
- [ ] Model faces the correct direction.
- [ ] Model sits on ground or water correctly.
- [ ] Relative scale matches the approved vanilla comparison.
- [ ] No source, reference, camera, or helper object appears.

## Materials

- [ ] All textures load.
- [ ] No magenta, black, invisible, or unintended transparent surface.
- [ ] Gloss, roughness, and normal behavior match the PDX precedent.
- [ ] Texture remains readable at normal map zoom.
- [ ] No severe shimmer or moire.

## Actions

- [ ] Idle action is correct and loops.
- [ ] Move action is correct and loops.
- [ ] Attack action is correct and finishes or loops as designed.
- [ ] Special actions map to the correct state.
- [ ] Root does not drift unexpectedly.
- [ ] Pivots and planted contacts are acceptable.
- [ ] Transitions do not snap or collapse the mesh.

## Performance

- [ ] Test uses the expected simultaneous instance count.
- [ ] Frame-time or FPS delta is recorded.
- [ ] No repeated error spam is observed from the asset.
- [ ] Texture memory and material count fit the profile.

## Evidence

- [ ] Standard-zoom screenshot.
- [ ] Close screenshot.
- [ ] Vanilla scale comparison.
- [ ] Action capture.
- [ ] Performance result.
- [ ] Exact runtime identifiers and consumer recorded.
