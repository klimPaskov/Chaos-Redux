# Event 006 Trieste reserved-tag remap handoff

Date: 2026-07-15

## Result

`IW-021` Trieste Free State now uses `ICX`. The prior reservation, `ZIN`, is
already the Chaos Redux Event 068 carrier and remains outside Event 006
creation. The separate retired `AUX` reservation is the Windows DOS device
basename; it cannot back portable country, history, localisation, or flag
files.

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
replacement pool. `ZIN` is an ordinary existing Chaos Redux carrier and is
not treated as an OS-reserved basename.

## Validation boundary

- The generated flag package was rebuilt after the remap, so its contact
  sheets, hashes, validation JSON, processed PNGs, and runtime TGAs all refer to
  `ICX`.
- The installed tag audit reports zero country-tag collisions for the remapped
  Event 6 registry.
- `ZIN` remains the existing Event 068 carrier; Event 006 does not create or
  overwrite it.
- Banat `AXX` remains blocked and Sicily `ASX` remains route-ownership locked.

No fallback identity, unresearched flag, or new country was introduced.
