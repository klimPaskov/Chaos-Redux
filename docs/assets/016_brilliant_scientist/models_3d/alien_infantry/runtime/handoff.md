# Alien infantry runtime handoff

Status: incomplete and `needs_user_review`.

The exact runtime consumer is `alien_infantry_entity`, reached from the owning subunit's `sprite = alien_infantry`. Keep the proposed mesh token `alien_infantry_mesh` and entity scale `0.8`, applied exactly once after the accepted replacement model is calibrated against installed `western_european_infantry.mesh`.

No `.mesh`, `.anim`, PDX material, entity, animation, or sound definition should be bound from the current candidate. Meshy task `01a02497-1fb9-7a1b-bec6-ec388d54a016` returned a scale-compatible but unarmed alien and omitted the mandatory laser rifle. The seven-view contact sheet found no obvious halo-derived shell, but the missing required component is a hard rejection. Rigging, weight work, action authoring, DDS conversion, PDX export, and reimport were intentionally stopped.

After user authorization, the only proposed paid recovery is one additional 30-credit Meshy 7 image-to-3D attempt from a rifle-silhouette-preserving cleanup. If that candidate passes geometry and component review, production must still complete all seven semantic actions, action-specific root/FPS/loop/contact/deformation QA, PDX export/reimport, packed material conversion, and synchronization of the sourced sound candidates before runtime binding.

Sound provenance and proposed identifiers are in `sound_handoff.md`. Counter consumers and the `chaosx_icon_artist` production brief are in `counter_handoff.md`. The full completion state is in `crosswalk.md` and `../validation/generation_rejection.json`.
