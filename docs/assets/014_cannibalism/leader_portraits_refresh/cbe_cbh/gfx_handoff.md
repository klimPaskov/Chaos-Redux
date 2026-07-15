# Event 014 CBE-CBH GFX handoff

No interface edit is required. `interface/014_cannibalism.gfx` already registers the complete CBE-CBH set at lines 199-230.

## Contract

- Texture root: `gfx/leaders/014_cannibalism/`.
- Final size: 156x210.
- Final encoding: legacy DDS, uncompressed 32-bit BGRA, opaque alpha.
- Europe/default mapping: each tag's base and `_europe` sprite intentionally share the base DDS.
- All other regional sprites map one-to-one to the same-named regional DDS.

The exact sprite-to-file mapping is recorded in `manifest.md`. The regenerated DDS filenames preserve every existing registration, so downstream character, cosmetic-tag, focus, decision, and GUI references require no rewiring. The changed artwork introduces distinct close-up props and gestures entirely inside the existing 156x210 texture contract.

## Runtime handoff

- CBE: seven DDS files serving eight registered sprites.
- CBF: seven DDS files serving eight registered sprites.
- CBG: seven DDS files serving eight registered sprites.
- CBH: seven DDS files serving eight registered sprites.
- Total: 28 live DDS files serving 32 existing sprite names.

No placeholder, fallback portrait, or alternate texture path is used.
