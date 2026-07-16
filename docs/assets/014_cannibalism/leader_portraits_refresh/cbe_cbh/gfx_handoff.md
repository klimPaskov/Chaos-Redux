# Event 014 CBE-CBH GFX handoff

`interface/014_cannibalism.gfx` preserves the complete CBE-CBH sprite-name set at lines 199-230 while the live artwork is reduced to 9 unique DDS files.

## Contract

- Texture root: `gfx/leaders/014_cannibalism/`.
- Final size: 156x210.
- Final encoding: legacy DDS, uncompressed 32-bit BGRA, opaque alpha.
- Europe/default mapping: each tag's base and `_europe` sprite intentionally share the base DDS.
- Retired regional sprite names deliberately alias the retained base texture for their slot; CBG aliases all use the retained CBF base texture.

The exact sprite-to-file mapping is recorded in `manifest.md` and the reduction amendment above. Existing character, cosmetic-tag, focus, decision, and GUI references require no rewiring because sprite names remain stable.

## Runtime handoff

- CBE: three DDS files serving eight registered sprites.
- CBF: three DDS files serving eight registered sprites.
- CBG: zero dedicated DDS files; eight registered sprites alias the retained CBF base texture.
- CBH: three DDS files serving eight registered sprites.
- Total: 9 live DDS files serving 32 existing sprite names.

The 19 retired CBE-CBH DDS paths are absent. The retained-texture aliases are a deliberate reduction choice, not new artwork or a placeholder asset.
