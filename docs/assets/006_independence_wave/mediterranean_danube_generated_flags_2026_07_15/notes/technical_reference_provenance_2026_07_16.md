# Technical flag-reference provenance migration

Date: 2026-07-16
Package: `mediterranean_danube_generated_flags_2026_07_15`

## Purpose

This record separates two facts that a path-only migration had combined:

1. the retired technical-presentation PNGs actually supplied to the original
   ImageGen calls; and
2. the current canonical vanilla-reference PNGs used for present-day package
   review and hash-ledger validation.

The two sets are not byte-identical. The retired paths no longer exist in the
working tree, so their SHA-256 values are retained as historical generation-
input evidence rather than entries in the live-path hash ledger. No legacy byte
equivalence is inferred from a matching subject or filename.

## Frozen mapping

| ImageGen use | Original ordered input and historical SHA-256 | Current canonical review reference and SHA-256 | Provenance semantics |
|---|---|---|---|
| `ARX` selected generation | `.agents/skills/chaos-redux-event-assets/assets/flags/ARM_UK.png`; SHA-256 `69b612800eb642be2004ccf1ae263fc014ce555f6c0204eff6b607962308b38c` | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal/arm_uk.png`; SHA-256 `0852be44f8f75579b9677904673c6ca254158a33da6b680df96d55b28ffbb9e9` | The retired file remains the recorded ImageGen input. The canonical file is a current flat-flag review reference only. |
| `ASX` selected generation | `.agents/skills/chaos-redux-event-assets/assets/flags/ARG_gen_nazism_party.png`; SHA-256 `07007cca92ff9f8a6544858a985aed5a6133a4f5e313dbd7169ea4ee491951e9` | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal/arg_gen_nazism_party.png`; SHA-256 `cbb5400e93cb0aacaa82193eb4555ba70619bdaa1f0c0198f0fc556ae7a432ac` | The retired file remains the recorded ImageGen input. The canonical file is a current flat-flag review reference only. |
| `ICX` selected generation and both rejected edit calls | `.agents/skills/chaos-redux-event-assets/assets/flags/ANU_fascism.png`; SHA-256 `aec2babab5bced21a7665583118307446cd5f10d3d3895e39ff7a93359d5cc34` | `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/normal/anu_fascism.png`; SHA-256 `b0633149ca295792b63561638db340f7bcab4ad22a21179963781350b1a1b243` | The retired file remains the recorded input to all three ICX calls. The canonical file is a current flat-flag review reference only. |

## Ledger behavior after repair

- `prompts/imagegen_prompts.md` preserves the original ordered input paths.
- `hashes.sha256` records the actual bytes at the three current canonical paths,
  so every live ledger row can be verified against the working tree.
- `build_flags.py` points its non-pixel-affecting `technical_reference` ledger
  entries at the current canonical review files. Those inputs are not read by
  flag normalization, resizing, TGA export, or any other pixel-producing step.
- The retained ImageGen raw files, flat masters, processed PNGs, contact sheets,
  and runtime TGA files were not regenerated or changed by this migration.
