# WP3 to WP5 shared-sound dependency handoff

The ordering section of the user-authored unit-fix plan assigns removal of the paleogenetic creature's zombie-sound dependencies to WP5.
The current `gfx/entities/paleogenetic_creature.asset` still calls WP3 soundeffects; no WP5 file is edited by WP3.

Current inherited calls whose WP3 presentation changed are:

- `chaosx_zombie_move`: move at 0.7000 and 2.1333 seconds, retreat at 0.3667, 0.9667 and 1.5000 seconds.
The shared cue volume is 0.50, random onset delay is removed, and four of its six recorded footstep takes are shorter single-transient cuts.
- `chaosx_parasitic_zombie_feed`: support_attack at 3.0667 seconds.
Its volume is 0.55.

Other current WP3 dependencies are `chaosx_mutant_zombie_roar`, `chaosx_base_zombie_grab_contact`, `chaosx_infected_zombie_pain`, `chaosx_parasitic_zombie_gurgle`, and `chaosx_base_zombie_body_fall`.
Their source files and identifiers are retained in this tranche.
The moan 01 recording also changes at its stable shared path; the infantry selection consumer is country/original-tag driven, so additional-selection inventory rows do not prove a paleogenetic entity-state consumer.

Disposition: `unresolved` external integration dependency.
WP5 must bind its dedicated, licensed creature recordings and definitions before this shared-family separation can be claimed complete.
The old shared recordings remain recoverable from hash-bound local Git LFS objects, and WP3's audio handoff preserves exact preimages and source provenance.
No new download or unapproved creature-source substitution is authorized in this session.
Until WP5 resolves the dependency, the changed movement/feed gains and shorter footsteps also reach that creature through these existing calls; the orchestrator should include it in the audio review.
