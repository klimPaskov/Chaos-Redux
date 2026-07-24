# Saunders Lewis source-only processing handoff

This handoff deliberately stops before ImageGen and runtime processing. The package contains an unchanged rights-cleared source master and one explicit source-pixel crop only.

## Completed

- Downloaded the direct Wikimedia Commons original for `File:Saunders Lewis (1520393).jpg`.
- Preserved the downloaded 1200×1828 JPEG byte-for-byte as the immutable master.
- Created one 1160×1060 RGB crop with both shoulder lines using box `(20, 30, 1180, 1090)`.
- Recorded source and crop hashes in `manifest.md` and `source_hashes.sha256`.

## Not performed

- No ImageGen call or generated face.
- No age reconstruction toward 1936.
- No deterministic 156×210 PNG or 65×67 derivative.
- No DDS conversion.
- No `.gfx`, character, localisation, or gameplay edit.

## Next gate if the user approves the date/licensing exception

Do not use this crop as a runtime ImageGen base. Preserving the 1973 sitter would retain the wrong period age, while aging him toward 1936 would reconstruct source-hidden facial geometry and violate the source-locked identity gate. Retain the master and crop as attributed comparison evidence only. A different rights-clear, age-appropriate Saunders Lewis photograph must start a fresh source chain.
