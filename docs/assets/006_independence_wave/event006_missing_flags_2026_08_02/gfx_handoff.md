# Event 006 missing base flags handoff

Flags use HOI4's engine filename lookup and do not require `.gfx` sprite definitions. The main agent should keep the existing country tag and ideology lookup unchanged; these files supply the missing democratic/base ladder.

## Runtime ladder

Each accepted tag below has all three exact runtime files:

```text
gfx/flags/<TAG>.tga          # 82x52 normal
gfx/flags/medium/<TAG>.tga   # 41x26 medium
gfx/flags/small/<TAG>.tga    # 10x7 small
```

Accepted tags in this tranche: `AKX ATX AXX BAX BBX BFX BHX BJX BKX BWX CIX CJX CKX CLX`.

The package manifest and machine-readable validation record are at:

- `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/manifest.md`
- `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/metadata/flag_validation.json`
- `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/metadata/hashes.sha256`

All 14 ladders are bottom-origin, uncompressed 32-bit TGA files (`descriptor = 8`) and were decoded back against their processed PNGs. The source masters, design references, prompts, and comparison sheets remain in the package for review.

## Deliberately blocked reservations

The 17 reservation tags are documented in `blockers.md`; no runtime files were created for them. Do not fill those paths until the parent accepts a concrete polity identity and defensible flag design.
