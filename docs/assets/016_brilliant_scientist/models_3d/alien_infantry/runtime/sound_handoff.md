# Alien infantry sound handoff

Status: sourced entity-state candidates complete; final definitions, entity events, mixing, and live validation remain parent-owned.

The exact vanilla model precedent is `gfx/entities/units_infantry.asset#infantry_rifle_entity`. Its states expose `attack`, `defend`, `support_attack`, `move`, `retreat`, `death`, and `idle`; the installed movement precedent fires `infantry_move_animation` from a state event. Entity-state sound identifiers proposed for the custom consumer are `alien_infantry_laser_fire`, `alien_infantry_move`, `alien_infantry_idle`, and `alien_infantry_death`.

The final accepted entity should fire laser audio from the muzzle event in `attack` and `support_attack`, movement audio at grounded foot contacts in `move` and `retreat`, the idle one-shot on idle entry, and death audio at the death onset. Exact action frames remain blocked until an accepted rifle-bearing mesh and final actions exist.

All source URLs, authors, CC0 licenses, immutable originals, transformations, checksums, and derived PCM receipts are recorded in `evidence/audio/provenance/audio_sources.json`.

Selection and acknowledgement are intentionally blocked at the subunit level. Installed HOI4 uses country/original-tag-wide `TAG_infantry_idle`, `TAG_infantry_move_out`, `TAG_infantry_neutral_combat`, `TAG_infantry_positive_combat`, and `TAG_infantry_retreat` voice consumers. Replacing them would also replace ordinary infantry voices, which is forbidden by the accepted brief.
