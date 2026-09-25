# Zombie shared sound package

An earlier base-zombie model, entity, action, and dedicated-contact-sound package was removed on 2026-09-25 at the user's request.
The approved base-zombie rebuild now has a production workspace and Meshy source candidates under `docs/assets/002_zombie_outbreak/models_3d/zombies/`.
The base `zombies` and `wendigo_zombies` battalions still use the vanilla `infantry` sprite; no accepted base entity, exported action set, or base animation-to-sound synchronization is wired.

## Base rebuild sound status

The user approved the exact `refs/original/meshy_input.png` image and a 64-credit Meshy ceiling, and the recorded provider tasks consumed all 64 credits: 30 for the body, 5 for the remesh, 5 for the rig, 3 for the rejected Frankenstein walk, and 21 for seven action clips.
The seven downloaded action FBXs passed receipt hash checks but remain source candidates, not accepted runtime actions.
The included Meshy walk and the paid Frankenstein walk were rejected for the required zombie movement role; approval of the optional CC0 Quaternius zombie walk remains pending.
Topology and full visual review of the isolated 90k model candidate, manual rig and action work, PDX texture binding, `.mesh`/`.anim` export and reimport proof, and base runtime wiring remain open.

The 24-file CC0 [Zombies Sound Pack](https://opengameart.org/content/zombies-sound-pack) by artisticdude is preserved in `docs/assets/002_zombie_outbreak/models_3d/zombies/audio_sources/`, with archive and extraction details in `source_manifest.md` there.
The numbered recordings have no accepted attack or death classification, source-to-runtime role mapping, conversion, or action synchronization.
Selection, idle, movement, contact, impact, special-action, and death roles must be reviewed against accepted base actions before any new base sound consumer is wired.

The existing shared package remains consumed by the specialized zombie entities and by the `ZZZ_infantry_idle` country selection voice.
`sound/chaosx_zombies_sound.asset` defines 15 retained WAV files: three idle moans, six footsteps, three attacks, and three deaths.
The specialized entities consume the generic `chaosx_zombie_attack` and `chaosx_zombie_death` effects; `ZZZ_infantry_idle` consumes the three idle moans.
The generic idle and movement wrappers remain available for specialized entity use.
No retained sound definition references a removed base-zombie WAV.

The three idle sounds come from [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans) by ianzazz, labeled CC0.
The footsteps come from [Footsteps](https://opengameart.org/content/footsteps-0) by GboxMikeFozzy, labeled CC0.
The original source archive for the idle sounds was recorded as `https://opengameart.org/sites/default/files/zombienoises.zip` with SHA-256 `D2C90AD199AB95396DD7F5D21083B3BB7BE7090A9B4A97CE7173233C6FCC72D6`.
The retained WAV delivery format is signed 16-bit PCM, 44.1 kHz, mono.
The older three attack and three death WAVs remain for specialized consumers; five of those six still lack a durable per-file source-to-runtime mapping, so their provenance remains unresolved.

There is no base-zombie animation-to-sound synchronization while the rebuilt custom base entity and actions remain unaccepted and unwired.
The base sprite must remain `infantry` until the parent accepts the model and action export/reimport evidence, resolves sound roles and exact action timing, and wires the runtime consumer.
