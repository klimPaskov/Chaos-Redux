# Event 014 warlord portrait matrix validation

Date: 2026-07-12

## Current result

The reusable CBA-CBH slot system has a complete seven-region portrait matrix: Europe, Asia, Africa, the Middle East, North America, South America, and Oceania. All 56 registered paths have distinct generated source art, distinct processed art, and distinct live DDS output. The six required baldness repairs have been regenerated, converted, and visually accepted.

| Surface | Count | Unique SHA-256 hashes | Validation |
| --- | ---: | ---: | --- |
| Generated source PNGs | 56 | 56 | Pass |
| Processed portrait PNGs | 56 | 56 | Pass; every file is 156 by 210 |
| Live portrait DDS files | 56 | 56 | Pass; every file is 131,168 bytes in the accepted one-mip 32-bit portrait format |

The final all-region manifest proves 56 source, 56 processed, and 56 runtime portrait paths, 56 unique hashes at each layer, decoded DDS parity, and 56-of-56 regional sprite registrations. The canonical evidence is `docs/assets/014_cannibalism/warlord_portraits_imagegen/manifest.md`, with complete contacts and hash ledgers beside it.

## Visual review

The Europe, Asia, Africa, Americas, Middle East, and Oceania source, processed, and DDS-decoded contact sheets were reviewed at full resolution. The review accepted the feral behavior, blood, origin tools, scavenged period gear, silhouettes, expressions, actions, and absence of borrowed sacred motifs. Europe CBB, Asia CBB, Asia CBH, Africa CBE, Africa CBF, and Africa CBG were regenerated because their first versions retained visible hair. The replacements are fully hairless and preserve six distinct actions and origin-readable props. The final 56-cell DDS review is `docs/assets/014_cannibalism/warlord_portraits_imagegen/contact_sheets/warlord_all_regions_dds_decoded_contact_2026-07-12.png`.

The European CBA portrait supplies the requested skull-holding and licking behavior. The ordinary reveal portrait uses a separate twelve-frame skull raise, contact, lick, recoil, and return animation; neither is reused as another regional portrait.

## Conversion and fallback statement

The final DDS tranches were converted with the signed Microsoft DirectXTex May 2026 `texconv` build recorded in their handoffs. No reused portrait, palette swap, transform-only animation, procedural drawing, default portrait, or conversion fallback is present in the accepted matrix.

## Verdict

Closed. No portrait-matrix omission, simplification, fallback, or visual blocker remains.
