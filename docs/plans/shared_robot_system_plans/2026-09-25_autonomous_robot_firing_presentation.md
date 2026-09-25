# Autonomous robot firing presentation

Disposition: `implemented` for offline entity, particle, and sound wiring; audible and live consumer review remain open.
Acceptance basis: the user's 2026-09-25 request retains the autonomous robot model and asks for shooting particles and richer sound design.

## Runtime evidence

The installed `autonomous_robot.mesh` has SHA-256 `C1B95902D34C299CD4CBA41E1CF262FA08A753A2EB8CC9E9172C4D68DBFE04D9`, matching the retained `export/final40_20260909/autonomous_robot.mesh`.
The installed attack action has SHA-256 `90EF214F280DB744AC00253F1B8CA4A78644BA4360900A9525BADC76E507D584`, matching that same export set.
The final40 attack and support-attack reimport reports show `robot_muzzle_l` parented to `Gun_L` and `robot_muzzle_r` parented to `Gun_R`.
The production `runtime_sync_crosswalk.json` records attack left frames 16–76 and right frames 19–79, and support-attack left frames 24–84 and right frames 27–87, every six frames per gun at 24 FPS.
`gfx/entities/autonomous_robot.asset` binds one vanilla `mg_muzzle_particle`, one `mg_muzzle_smoke_particle`, one `mg_muzzle_flash` light, and one short gunshot to each of those 44 discharges across the two firing states.
The old long-burst entity event is removed from attack and support attack.
Death now plays a destruction cue at frame 8 and a heavy impact at frame 69, matching the retained action phase evidence.

## Audio sources and installation

`autonomous_robot_mg_discharge_pulse.wav` is a 0.12-second mechanical excerpt of [Cymeon's machine gun recorded at a film shoot](https://freesound.org/people/Cymeon/sounds/205901/), published CC0.
Its installed SHA-256 is `E3373E3E3ED2DB9292564024802B67268268430A22252FC37AFCD4B0511AC10E`, identical to the retained source-derived candidate.
`autonomous_robot_destruction.wav` is a mechanically faded excerpt of [unfa's raw firecracker recording](https://freesound.org/people/unfa/sounds/609588/), published CC0.
Its installed SHA-256 is `7E9A1FB0128D6994F57BB6A40A58F766BE4168646DE4FCA8A3D74EDA644930BA`, identical to the retained source-derived candidate.
Both installed files decode as mono PCM16 WAV at 44.1 kHz; neither source was submitted for model training.
The source pages, original preview files, transformations, numeric onset checks, and earlier candidate decisions remain in `docs/assets/shared_robot_system/models_3d/autonomous_robot/attempts/20260906_weaponfree_blender/evidence/finalize_20260912/audio/`.
`sound/autonomous_robot_sound.asset` defines the two new sounds and positional effects, and `sound/chaosx_sound.asset` registers them.

## Validation and remaining review

A source-to-entity check compared all 22 attack and 22 support-attack particle/sound events with the exact final40 discharge frames and nodes.
The installed WAV hashes and PCM parameters were checked against the retained source-derived candidates.
The sources and numeric alignment support the implementation, but the agent had no audio listening capability and did not launch Hearts of Iron IV.
The user owns audible balance, muzzle placement, visible particle intensity, and live playback review; any issue found there remains a follow-up rather than a completed visual or audio acceptance claim.
The robot body, textures, rig, animation exports, and unit icon were left intact as requested.
