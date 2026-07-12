# Event 014 Warlord Portrait Validation

Batch: `E14-POR-WARLORD-01`

Validation date: 2026-07-11

## Visual review

Source, processed, actual-size, and DDS-decoded contact sheets were reviewed directly.

| Slot | Origin | Distinguishing evidence at 156 by 210 |
| --- | --- | --- |
| CBA | Island Host 1 | Lean long face, narrow profile, rope and pea-coat panel, blue-grey storm pier, amber signal lamp. |
| CBB | Island Host 2 | Heavy round face, broad front-biased pose, sailcloth and plate, dark storehouse, rain and netting. |
| CBC | Siege Commune 1 | Gaunt angular skull, sharp over-shoulder pose, field-wire coil, raw apron, brick arch and sandbags. |
| CBD | Siege Commune 2 | Massive square head, cloudy eye, low-angle stance, padded engineering vest, concrete factory light. |
| CBE | March Host 1 | Tall rangy face, diagonal walking posture, binoculars and blanket sash, sunset road and period truck. |
| CBF | March Host 2 | Compact muscular face, turned motor-column pose, period goggles and tyre chain, repair lamp and wheel. |
| CBG | Prison Host 1 | Thick rectangular face, rigid front view, striped raw cloth, suspenders, bars and caged corridor light. |
| CBH | Prison Host 2 | Very gaunt narrow face, long neck and upward gaze, throat wrap and blanket, barred intake-room daylight. |

Every reviewed portrait is one fictional adult male-presenting person with a visibly bald scalp. Blood is readable on face, scalp, hands, raw cloth, hide, or period clothing at actual final size. No portrait contains a second person, visible victim, supernatural anatomy, horn, antler, glowing eye, skull mask, fixed flag, sacred motif, copied ceremonial regalia, readable text, or modern tactical kit.

## Distinctness check

All source, processed, and DDS SHA-256 hashes are unique. A 64-bit full-image difference hash was also calculated from each decoded final portrait.

- Same-origin distances: CBA/CBB `35`, CBC/CBD `41`, CBE/CBF `31`, CBG/CBH `29`.
- All-pair range: `22` to `44` differing bits out of `64`.
- Closest pair: CBB/CBD at `22`; manual review confirms different face geometry, head angle, clothing silhouette, lighting direction, and environmental origin cues.

No pair is a crop, recolor, resize, or edit of the same source.

## PNG and DDS format check

Each processed source is `156x210 RGBA`. Each final DDS reports:

- dimensions: `156x210`
- ffprobe pixel format: `bgra`
- DDS header size: `124`
- row pitch: `624`
- pixel format flags: `0x41` (`RGB` plus alpha pixels)
- bit depth: `32`
- masks: red `00FF0000`, green `0000FF00`, blue `000000FF`, alpha `FF000000`
- total file size: `131168` bytes
- stored image levels: one base image, no generated mip chain

Every DDS decodes pixel-identically to its matching processed PNG. The decoded DDS contact sheet is `../contact_sheets/warlord_dds_decoded_contact.png`.

## Protected-file check

The protected Event 014 leader file retains SHA-256 `5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88` after all eight conversions.

## Scope check

This tranche created or edited only generated sources, processed portrait PNGs, final CBA-CBH portrait DDS files, review contact sheets, hashes, prompts, notes, manifests, and handoffs. No `.gfx`, character, gameplay, localisation, spreadsheet, flag, achievement, animation, or protected-leader file was edited.

## Blocker

The flag package remains blocked because the final accepted flag/cosmetic-tag ledger is not frozen. No flag filename was guessed and no flag output was created.
