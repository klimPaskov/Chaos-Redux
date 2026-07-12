# Event 014 Europe/Asia/Africa Warlord Portrait Validation

Tranche ID: `E14-POR-WARLORD-EAA-01`

Validation date: 2026-07-12

## Visual review

The three-region source, processed, actual-size, and DDS-decoded contact sheets
were inspected directly. All 24 portraits retain a large readable face,
asymmetric feral expression, distinct prop action, and region/host setting after
the final `156x210` crop.

| Region | Slot identities confirmed at final size |
| --- | --- |
| Europe | CBA skull lick; CBB two-hand enamel lid clutch; CBC cleaver crouch; CBD glove bite and engineering plate; CBE crooked-goggle lift; CBF dog-tag display; CBG ration-sack drag; CBH mug-raised intake laugh. |
| Asia | CBA lantern uplight; CBB whistle beside jaw; CBC field telephone; CBD railway punch tool; CBE route-paper tear; CBF hand-crank generator; CBG inspection reflector; CBH buckled blank ration token. |
| Africa | CBA broken compass; CBB marlinspike brace; CBC plumb bob; CBD folding rule; CBE inverted canteen; CBF stretched fan belt; CBG gate-hinge scrape; CBH shaving brush and lather bowl. |

No accepted portrait contains a real-person likeness, readable label, flag,
national emblem, sacred or ceremonial motif, living Indigenous motif, modern
tactical kit, supernatural anatomy, visible victim, or second active subject.
The generated words and background attendant in the first Asia CBH base were
removed through imagegen attempt `73` before the final stain edit; the corrected
token retains abstract tally marks only.

## Distinctness evidence

All 24 source hashes, all 24 processed hashes, and all 24 runtime DDS hashes are
unique. A 64-bit whole-image difference hash calculated from each decoded DDS
has an all-pair range of `17` to `43` differing bits.

Each of the 24 accepted repo source PNGs also hashes exactly to the saved
imagegen output named by its accepted attempt record. This closes the provenance
chain from generation call to source PNG, processed PNG, and runtime DDS.

- Closest pair: Europe CBB/Europe CBF at `17`. Direct review confirms different
  face geometry, head angle, hand pose, prop silhouette, coat construction,
  lighting direction, and breakwater versus motor-camp setting.
- Same-host Europe distances: CBA/CBB `21`, CBC/CBD `41`, CBE/CBF `31`,
  CBG/CBH `37`.
- Same-host Asia distances: CBA/CBB `33`, CBC/CBD `31`, CBE/CBF `24`,
  CBG/CBH `20`.
- Same-host Africa distances: CBA/CBB `37`, CBC/CBD `28`, CBE/CBF `36`,
  CBG/CBH `28`.

No pair is a crop, recolor, resize, or local edit of the same generated source.

## Runtime proof

The machine validation report records `24` entries and confirms:

- every processed PNG is `156x210 RGBA`
- every DDS decodes to `156x210 RGBA`
- every decoded DDS is pixel-identical to its matching processed PNG
- every DDS has a `124`-byte header, `624`-byte row pitch, 32-bit BGRA masks,
  texture caps, one stored base image, and total size `131168` bytes
- unique SHA-256 counts are `24` for sources, `24` for processed PNGs, and `24`
  for DDS files

The decoded runtime review surface is
`../contact_sheets/warlord_europe_asia_africa_dds_decoded_contact.png`; exact
header, hash, pixel, and perceptual-distance data is in
`europe_asia_africa_validation.json`.

## Registration and scope proof

The existing Event 014 sprite block already maps all 24 runtime paths:

- Europe: `GFX_portrait_<TAG>_warlord` and
  `GFX_portrait_<TAG>_warlord_europe`
- Asia: `GFX_portrait_<TAG>_warlord_asia`
- Africa: `GFX_portrait_<TAG>_warlord_africa`

No registration edit was required. This tranche did not change another agent's
regional source, processed image, DDS, contact sheet, prompt ledger, or handoff.

## Simplifications, omissions, and blockers

None within the assigned Europe, Asia, and Africa scope. The combined
all-region manifest and all-set contact sheet remain intentionally reserved for
the parent merge and are not omissions from this tranche.
