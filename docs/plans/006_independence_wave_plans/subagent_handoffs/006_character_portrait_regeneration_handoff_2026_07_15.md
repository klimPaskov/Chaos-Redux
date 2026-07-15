# Event 006 character portrait regeneration handoff

## Outcome

All 18 fictional large portrait assets outside the two user-approved historical
exceptions were regenerated through independent official ImageGen calls and
installed under their existing stable filenames. Nine commander thumbnails
were derived from the accepted full commander masters. The previous generic
NWE portrait handoffs are superseded for visual-source and final-file evidence
by this package.

The approved files
`portrait_BAY_rupprecht_of_bavaria.dds` and
`portrait_RHI_josef_friedrich_matthes.dds` were not edited. Their accepted
hashes are guarded by the package builder.

## Changed surfaces

- `gfx/leaders/006_independence_wave/`: 18 large DDS replacements and nine
  commander thumbnail replacements;
- `docs/assets/006_independence_wave/portrait_regeneration_2026_07_15/`:
  ImageGen masters, processed PNGs, metadata, vanilla comparisons, decoded DDS
  evidence, prompts, review record, exact hashes, and reproducible builder;
- `docs/assets/006_independence_wave/manifest.md`: current package routing;
- `.agents/skills/chaos-redux-event-assets/SKILL.md`: the misdirected
  person-free institutional rule was removed; valid portrait and advisor rules
  remain;
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`:
  the historical-portrait restoration helper now uses the two registered,
  approved sprite names instead of three undefined aliases.

No gameplay token, portrait sprite name, character token, or localisation key
was renamed.

## Validation evidence

- 18 of 18 full runtime DDS files decoded as exact `156x210` legacy
  uncompressed BGRA copies of their approved processed PNGs;
- nine of nine commander thumbnails decoded as exact `50x67` legacy
  uncompressed BGRA copies of their approved derived PNGs;
- the two approved historical hashes matched before and after the build;
- all currently registered Event 006 leader texture paths resolve;
- the actual runtime DDS contact sheets passed visual review at both sizes.

## Boundary and risk

The ACX, AEX, and AJX pairs remain art-ready readiness-pool entries without
current sprite registrations. They must not be treated as playable package
proof. The Event 006 completion goal remains open beyond this asset tranche.
