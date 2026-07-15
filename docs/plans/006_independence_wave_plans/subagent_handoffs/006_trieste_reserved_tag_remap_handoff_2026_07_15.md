# Event 006 Trieste reserved-tag remap handoff

Date: 2026-07-15

## Result

`IW-021` Trieste Free State now uses `ICX`. The prior reservation, `AUX`, is a
Windows DOS device basename. Windows could enumerate generated `AUX.tga` and
`AUX.png` files created through a long-path-aware process, but normal Win32
path access could not reopen them. A Windows HOI4 installation therefore could
not be trusted to load the country, history, localisation, or flag surfaces.

`ICX` was selected from the dated collision-free `??X` pool, then checked
against vanilla, all 122 installed Workshop directories, every local mod, and
the rest of Chaos Redux. The package identity, anchor, reservation group,
country definition, history shell, force profile, and historical Trieste flag
design are otherwise unchanged.

## Migrated surfaces

- `common/country_tags/006_independence_wave_countries.txt`
- `common/countries/006_independence_wave_ICX.txt`
- `history/countries/ICX - Event 006 Country Shell.txt`
- region-02 package trigger and publisher effects
- country localisation
- candidate registry and research resolution
- current-map binding and force-package matrix
- source-of-truth tag architecture and research audit documentation
- Mediterranean/Danube flag research, ImageGen provenance, build script,
  validation, contact sheets, manifests, and handoffs
- normal, medium, and small runtime flags as `ICX.tga`

No gameplay package was promoted to content-ready by this remap.

## Reusable audit correction

`.tools/audit_hoi4_country_tags.py` excludes the engine-reserved `GFX`
namespace and the Windows-reserved three-character device basenames `AUX`,
`CON`, `NUL`, and `PRN` from both accepted Event 6 tags and its suggested
replacement pool. This prevents the audit from offering an apparently unused
tag whose required filenames cannot be opened reliably on Windows.

## Validation boundary

- The generated flag package was rebuilt after the remap, so its contact
  sheets, hashes, validation JSON, processed PNGs, and runtime TGAs all refer to
  `ICX`.
- The installed tag audit reports zero country-tag collisions for the remapped
  Event 6 registry.
- `AUX` remains only as a documented retired value; no gameplay, localisation,
  history, or asset filename uses it.
- Banat `AXX` remains blocked and Sicily `ASX` remains route-ownership locked.

No fallback identity, unresearched flag, or new country was introduced.
