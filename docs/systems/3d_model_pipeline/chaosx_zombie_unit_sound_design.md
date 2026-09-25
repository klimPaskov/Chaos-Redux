# Zombie shared sound package

The custom base-zombie 3D model, its entity, action files, dedicated contact sounds, and production workspace were removed on 2026-09-25 at the user's request.
The base `zombies` and `wendigo_zombies` battalions use the vanilla `infantry` sprite until a future model is approved and installed.

The remaining package is shared by the specialized zombie entities and by the `ZZZ_infantry_idle` country selection voice.
`sound/chaosx_zombies_sound.asset` defines 15 retained WAV files: three idle moans, six footsteps, three attacks, and three deaths.
The specialized entities consume the generic `chaosx_zombie_attack` and `chaosx_zombie_death` effects; `ZZZ_infantry_idle` consumes the three idle moans.
The generic idle and movement wrappers remain available for specialized entity use.
No retained sound definition references a removed base-zombie WAV.

The three idle sounds come from [Zombie noises and moans](https://opengameart.org/content/zombie-noises-and-moans) by ianzazz, labeled CC0.
The footsteps come from [Footsteps](https://opengameart.org/content/footsteps-0) by GboxMikeFozzy, labeled CC0.
The original source archive for the idle sounds was recorded as `https://opengameart.org/sites/default/files/zombienoises.zip` with SHA-256 `D2C90AD199AB95396DD7F5D21083B3BB7BE7090A9B4A97CE7173233C6FCC72D6`.
The retained WAV delivery format is signed 16-bit PCM, 44.1 kHz, mono.
The older three attack and three death WAVs remain for specialized consumers; five of those six still lack a durable per-file source-to-runtime mapping, so their provenance remains unresolved.

There is no base-zombie animation-to-sound synchronization while the custom base entity is absent.
A future base model needs its own reviewed sound and action timing package before its sprite is switched away from `infantry`.
