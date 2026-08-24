# V4 first-rig shooting rejection

- Geometry generation: `01a03449-9124-72e8-adfb-8858757ce416`
- Remesh: `01a0344f-f66e-7502-a085-ed554b90f719`
- Rig: `01a03456-569a-70c7-ba9d-0d0ec2be9201`
- Meshy action 690: `01a03458-808b-70d3-a98f-93f3b1d92e11`
- Decision: rejected at the mandatory strongest-shooting gate.
- Evidence: frames 0, 20, and 40 show catastrophic torso and arm stretching, with the ray gun pulled through and above the head. Weapon rigidity and coherent hand contact are lost, so the motion is unusable and must not be repaired or reused.
- Preserved lightweight evidence: `blender/previews/alien_infantry_recovery_v4_laser_attack_frame_0_three_quarter.png`, `blender/previews/alien_infantry_recovery_v4_laser_attack_frame_20_three_quarter.png`, and `blender/previews/alien_infantry_recovery_v4_laser_attack_frame_40_three_quarter.png`.
- Recovery: submit one independent Meshy re-rig of the accepted V4 remesh, then test action 690 again before any remaining action spend.

## Re-rig recovery result

- Independent re-rig: `01a0345e-d33a-71fb-9d9e-7edcae24b518`
- Re-rig GLB SHA-256: `307F22E539B215F6579F381637B438CE9E2E2D8E9D5628C113B0CDCB88B220CA`
- Retry Meshy action 690: `01a03461-fded-73cd-ac88-968e8037bc62`
- Retry decision: rejected. Frames 0, 40, and 80 reproduce the same catastrophic torso/arm stretching and weapon displacement through and above the head.
- Preserved retry evidence: `blender/previews/alien_infantry_recovery_v4_retry2_laser_attack_frame_0_three_quarter.png`, `blender/previews/alien_infantry_recovery_v4_retry2_laser_attack_frame_40_three_quarter.png`, and `blender/previews/alien_infantry_recovery_v4_retry2_laser_attack_frame_80_three_quarter.png`.
- Final V4 lineage decision: reject for provider rig/weapon deformation; do not submit the other six actions and do not repair locally.
