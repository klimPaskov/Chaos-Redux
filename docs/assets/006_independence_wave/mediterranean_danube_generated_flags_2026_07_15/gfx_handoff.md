# Event 006 Mediterranean and Danube flag wiring handoff

## Ownership boundary

This handoff supplies final flag textures and route constraints only. It does
not edit `.gfx`, country tags, country history, event logic, decisions, focuses,
localisation, states, spreadsheets, or any other gameplay file.

Flags are an engine root-folder exception. HOI4 discovers these files by exact
tag filename, so no `spriteType` block and no new `.gfx` file are required:

| Tag | Normal | Medium | Small |
|---|---|---|---|
| `ARX` | `gfx/flags/ARX.tga` | `gfx/flags/medium/ARX.tga` | `gfx/flags/small/ARX.tga` |
| `ASX` | `gfx/flags/ASX.tga` | `gfx/flags/medium/ASX.tga` | `gfx/flags/small/ASX.tga` |
| `ICX` | `gfx/flags/ICX.tga` | `gfx/flags/medium/ICX.tga` | `gfx/flags/small/ICX.tga` |

## Parent-owned route wiring

### ARX Sardinia

Use the unsuffixed ARX triplet only for the approved alternate-history
Sardinian civic synthesis. Player-facing documentation must call it a
fictional 1936 civic synthesis based on attested Four Moors motifs, not an
attested 1936 sovereign flag. Do not layer Savoy or another dynastic identity
over it without separate route research and art.

### ASX Sicily

The delivered S.015 tricolour is constitutional-independence-route art only.
Before wiring it, the parent must choose one of these evidence-compatible
arrangements:

1. confirm that the ASX tag is instantiated only for the constitutional-
   independence route, allowing the unsuffixed triplet to remain the route's
   country identity; or
2. approve a specific cosmetic tag, copy the same reviewed triplet to that
   exact parent-owned cosmetic filename, and wire the route with HOI4 cosmetic-
   tag logic.

Do not silently use this art for neutral, crown, labor, military, fascist, or
client routes. This handoff intentionally does not invent the cosmetic tag name
or patch gameplay logic.

### ICX Trieste

The unsuffixed ICX triplet is appropriate for the plain Triestine civic identity
and can support an international-commission or constitutional civic opening
where the country package retains that identity. Do not add UN, Italian,
Yugoslav, Habsburg, labor, fascist, or patron overlays without separate route-
owned research and assets.

### AXX Banat

No flag exists in this handoff. Banat remains blocked until the user approves
either an explicitly fictional neutralized-gate design or a politically
specific route design. Do not use Romanian, Serbian, Hungarian, Habsburg, or
internet-reconstruction heraldry as an attested 1918 Republic baseline.

## Ideology and cosmetic variants

No `_communism`, `_democratic`, `_fascism`, `_neutrality`, or cosmetic-tag
triplet is supplied. The Event 006 unsuffixed-flag precedent is followed because
the research packet does not approve any ideology-to-design mapping. Generic
recolours, stars, fasces, dynastic shields, or copied emblems are not acceptable
substitutes.

## Parent review checklist

- Review the two package contact sheets before wiring.
- Confirm ARX's fictional-synthesis wording wherever the identity is documented.
- Resolve ASX's constitutional route ownership before enabling the flag.
- Confirm ICX's civic use and disclosed 3:2/red/device-proportion normalization.
- Keep AXX blocked and absent.
- Do not claim country-package or Event 006 completion from this art handoff.

Asset statuses and complete provenance are in `manifest.md`; exact ImageGen
prompts are in `prompts/imagegen_prompts.md`.
