# IW-051 YAK flag handoff

## Runtime boundary

- Carrier: registered vanilla `YAK`.
- Runtime outputs: four `YAK_INDEPENDENCE_WAVE_*` route basenames, each with normal, medium, and small TGA ladders.
- No `YAK.tga`, `YAK_democratic.tga`, `YAK_communism.tga`, `YAK_fascism.tga`, or `YAK_neutrality.tga` file was changed.
- No `.gfx` file is required for the existing country-flag lookup.
- No central adapter, attestation, preflight, deterministic Join, character, history, or localisation file is changed by this asset package.

## Provenance and review

The 1926 Yakut ASSR Aurora/light-blue motif is retained only as a documented
research reference. These four ladders are generated alternate-history route
syntheses, not copied historical flags and not a neutral 1936 baseline. The
native source masters are flat and preserved unchanged; the accidental red
canvas remainder is excluded by explicit per-route crop boxes in
`build_flags.py`. Prompt text was not co-located with the supplied masters and
is recorded as missing rather than reconstructed.

## QA

`metadata/flag_validation.json` records the exact source/crop/master hashes,
dimensions, route classifications, TGA headers, descriptor conventions, and
opaque-alpha checks. `metadata/dds_validation.json` records uncompressed BGRA
header checks and PNG round-trip equality for all 12 evidence DDS files.
Normal and medium TGAs use bottom-origin descriptor 8; small TGAs use the
installed vanilla small-flag descriptor 0. All ladders are 82x52, 41x26, and
10x7 respectively.

## Parent gate

Keep the asset package `needs_user_review` until the generated route identity,
missing prompt archive, and final YAK setup/identity clearance are accepted.
Do not promote the carrier base or widen central Event 006 admission from this
handoff alone.
