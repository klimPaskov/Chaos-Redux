# Event 006 Mediterranean flag-reference provenance repair

Date: 2026-07-16
Scope: the three migrated technical flag-reference rows in
`mediterranean_danube_generated_flags_2026_07_15` only
Mode: bounded patch; no flag pixels, runtime files, gameplay, localisation,
portraits, or unrelated assets changed

## Result

The three canonical reference rows now validate against the files that exist in
the current skill library. The package also preserves the retired path/hash
records for the files actually supplied to ImageGen, without claiming that the
byte-distinct canonical review PNGs were the historical generation inputs.

## Files changed

- `docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/build_flags.py`
- `docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/hashes.sha256`
- `docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/manifest.md`
- `docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/prompts/imagegen_prompts.md`
- `docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/notes/technical_reference_provenance_2026_07_16.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_mediterranean_flag_reference_provenance_repair_2026_07_16.md`

## Exact before/after provenance semantics

Before the repair, a path-only migration had changed both the prompt input
lists and the live ledger paths from the retired `assets/flags/` references to
the current `assets/vanilla_reference/flags/normal/` references. The three old
SHA-256 values remained beside the new paths. This produced two defects at
once: all three live ledger rows failed, and the prompt record implied that the
current canonical bytes had been used in historical ImageGen calls.

After the repair:

- the ordered ImageGen input lists again name the retired paths actually used at
  generation time;
- the new provenance note freezes each retired path and old SHA-256, maps it to
  the current canonical path and current SHA-256, and explicitly states that
  the two byte sets have different roles and are not asserted equivalent;
- the live hash ledger records the current canonical paths with their actual
  current hashes;
- the retained builder uses the canonical paths only as non-pixel-affecting
  ledger dependencies and includes the provenance note in future ledgers; and
- the manifest points reviewers to the same provenance boundary.

| Reference | Before: migrated path with stale legacy hash | After: live canonical path/hash | Preserved historical generation input |
|---|---|---|---|
| `ARM_UK` / ARX | `.../vanilla_reference/flags/normal/arm_uk.png` + `69b612800eb642be2004ccf1ae263fc014ce555f6c0204eff6b607962308b38c` | `.../vanilla_reference/flags/normal/arm_uk.png` + `0852be44f8f75579b9677904673c6ca254158a33da6b680df96d55b28ffbb9e9` | `.../assets/flags/ARM_UK.png` + `69b612800eb642be2004ccf1ae263fc014ce555f6c0204eff6b607962308b38c` |
| `ARG_gen_nazism_party` / ASX | `.../vanilla_reference/flags/normal/arg_gen_nazism_party.png` + `07007cca92ff9f8a6544858a985aed5a6133a4f5e313dbd7169ea4ee491951e9` | `.../vanilla_reference/flags/normal/arg_gen_nazism_party.png` + `cbb5400e93cb0aacaa82193eb4555ba70619bdaa1f0c0198f0fc556ae7a432ac` | `.../assets/flags/ARG_gen_nazism_party.png` + `07007cca92ff9f8a6544858a985aed5a6133a4f5e313dbd7169ea4ee491951e9` |
| `ANU_fascism` / ICX | `.../vanilla_reference/flags/normal/anu_fascism.png` + `aec2babab5bced21a7665583118307446cd5f10d3d3895e39ff7a93359d5cc34` | `.../vanilla_reference/flags/normal/anu_fascism.png` + `b0633149ca295792b63561638db340f7bcab4ad22a21179963781350b1a1b243` | `.../assets/flags/ANU_fascism.png` + `aec2babab5bced21a7665583118307446cd5f10d3d3895e39ff7a93359d5cc34` |

The `ANU_fascism` record applies to the selected ICX generation and both
retained rejected ICX edit calls.

## Validation

- Parsed all 39 `hashes.sha256` rows and recomputed every live SHA-256:
  `39 valid`, `0 malformed`, `0 missing`, `0 mismatched`.
- Rechecked the nine runtime TGA hashes against their pre-repair values:
  `9 checked`, `0 mismatched`. This covers ARX, ASX, and ICX at normal, medium,
  and small sizes.
- The package ledger also revalidated all retained ImageGen raws, flat masters,
  processed PNGs, contact sheets, research inputs, and validation evidence; no
  non-reference hash changed.
- Parsed `build_flags.py` with Python's AST parser successfully.
- Scoped Git status contains only the five package text/provenance files listed
  above; no TGA, PNG, SVG, DDS, portrait, gameplay, or localisation file entered
  the patch.

The complete builder was intentionally not executed because it is a mutating
rebuild that rewrites generated masters, processed previews, contact sheets,
validation output, and all nine runtime TGAs. Live ledger recomputation proves
the requested integrity repair without violating the frozen-pixel boundary.

## Remaining risks and omissions

- The three retired technical-reference PNG bytes are absent from the current
  working tree. Their historical paths and SHA-256 values are preserved, but an
  exact replay of the original ImageGen calls would still require those retired
  bytes from an external or historical source. This limitation is now explicit
  rather than hidden behind canonical paths.
- No remaining live hash-ledger mismatch was found.
- No fallback, pixel substitution, flag regeneration, or scope expansion was
  used.

Skills used: `chaos-redux-event-assets` and `chaos-redux-subagents`.
