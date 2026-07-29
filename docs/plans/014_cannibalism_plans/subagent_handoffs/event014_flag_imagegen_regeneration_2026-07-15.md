# Event 014 Flag Imagegen Regeneration Handoff — 2026-07-15

## Outcome

All 65 live Event 014 fictional flag designs were regenerated successfully. Every base or ideology variant came from its own built-in image-generation call, retains its own generated source master, and replaces the corresponding normal, medium, and small runtime TGA without changing any engine-facing filename.

- Distinct built-in imagegen calls: `65`
- Distinct generated source masters: `65`
- Processed 82x52 masters: `65`
- Runtime TGAs: `195` (`65` normal, `65` medium, `65` small)
- Runtime palettes: exactly `5` fully opaque flat colors per flag, inside the required `3–5` range
- Fallback generation routes: none
- Failed or substituted designs: none

The exact design inventory is the cross-product of these 13 roots and five suffixes:

- Roots: `CBA`, `AHX`, `CBC`, `AIX`, `CBE`, `CBF`, `AMX`, `CBH`, `CBL`, `CBL_CENTRAL_COMMAND`, `CBL_HOST_CONFEDERATION`, `CBL_RITUAL_STATE`, `ZZZ_CANNIBALISM_HANNIBAL`
- Suffixes: no suffix, `_communism`, `_democratic`, `_fascism`, `_neutrality`

`ZZZ_weaponized_wendigo` was deliberately excluded, does not appear in the prompt/evidence inventories, and has no scoped working-tree change.

## Exact changed paths

For each of the 65 stems defined above, the following exact paths were regenerated or replaced:

- `docs/assets/014_cannibalism/flags_refresh/prompts/<stem>.txt`
- `docs/assets/014_cannibalism/flags_refresh/source_png/<stem>.png`
- `docs/assets/014_cannibalism/flags_refresh/processed_png/<stem>.png`
- `gfx/flags/<stem>.tga`
- `gfx/flags/medium/<stem>.tga`
- `gfx/flags/small/<stem>.tga`

Package metadata and review artifacts changed at these exact paths:

- `docs/assets/014_cannibalism/flags_refresh/prompts/prompt_specs.json`
- `docs/assets/014_cannibalism/flags_refresh/generation_evidence.json`
- `docs/assets/014_cannibalism/flags_refresh/manifest.md`
- `docs/assets/014_cannibalism/flags_refresh/validation.json`
- `docs/assets/014_cannibalism/flags_refresh/notes/build_regeneration_prompts.py`
- `docs/assets/014_cannibalism/flags_refresh/notes/process_flags.py`
- `docs/assets/014_cannibalism/flags_refresh/contact_sheets/source_masters_contact_sheet.png`
- `docs/assets/014_cannibalism/flags_refresh/contact_sheets/final_runtime_flags_contact_sheet.png`
- `docs/assets/014_cannibalism/flags_refresh/contact_sheets/source_vs_final_contact_sheet.png`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_flag_imagegen_regeneration_2026-07-15.md`

No gameplay, `.gfx` configuration, GUI, localisation, script, country-history, focus, decision, event, or spreadsheet file was edited.

## Image-generation provenance

Each stem used a separate, design-specific built-in imagegen prompt. The prompts share only the production constraints needed for a coherent flag family; each specifies a different irregular heraldic device and composition. Ideology variants are not palette swaps, geometric traces, local drawings, transformed copies, or multiple crops from one generated sheet.

`generation_evidence.json` contains one record per stem with:

- mode `built-in-imagegen`
- exact prompt-file path and prompt SHA-256
- original built-in output path and SHA-256
- retained in-repository source path and SHA-256
- positive byte-for-byte built-in/source copy match

All 65 built-in outputs exist, all 65 retained source files match their built-in outputs byte-for-byte, and all 65 source hashes are unique.

## Visual and processing decisions

- Prompts require a flat rectangular flag, a distinctive asymmetrical or irregular generated device, three through five dominant colors, and no text, watermark, flagpole, fabric scene, perspective presentation, real extremist mark, or borrowed Indigenous sacred motif.
- Source masters remain unmodified as provenance evidence. Runtime masters use only mechanical center-cropping, resizing, non-dithered palette flattening, and palette-preserving downscaling; no emblem was traced, redrawn, rebuilt from primitives, or edge-simplified.
- A full source/median-cut/maximum-coverage/fast-octree visual comparison was reviewed at 82x52. Maximum coverage best retained the generated heraldry for `56` designs; five palette-sensitive designs use fast octree and four use median cut. The selected method is recorded per stem in the manifest and validation file.
- Medium and small flags derive from the selected 82x52 generated design and reuse its final five-color palette.
- TGAs are direct, uncompressed, 32-bit BGRA exports with eight alpha bits and bottom-left origin.

The final runtime sheet shows 65 visibly different authored emblems and field layouts. The source-versus-final sheet shows source, normal, medium, and small results together for every stem.

## Validation evidence

`docs/assets/014_cannibalism/flags_refresh/validation.json` records the full per-stem proof. The completed checks include:

- `65` prompt specifications, `65` prompt files, `65` evidence records, `65` source PNGs, and `65` processed PNGs
- `195` expected runtime TGAs present at the three exact engine sizes: `82x52`, `41x26`, and `10x7`
- `65/65` distinct source hashes, `65/65` distinct processed hashes, and `65/65` byte-distinct TGAs independently at normal, medium, and small size
- exactly five opaque runtime colors for every design
- uncompressed true-color image type `2`, 32-bit depth, descriptor `8`, bottom-origin data, exact byte length, and decoded pixel equality for every TGA
- small-size contrast gate: at least two retained colors and less than 90 percent dominance by any one color
- normal-size geometry gate: every processed design retains a nontrivial edge-transition count
- GNU `file` inspection through Git's bundled executable: `195/195` report RGBA and 32-bit dimensions; zero output rows contain `- top`
- visual review of all three labeled contact sheets

## References and skills

The required offline Paradox wiki core pages were consulted before asset-package inspection. Vanilla normal/medium/small flag references and the event-assets skill's reference README, catalog, and contact sheet were reviewed for proportion, contrast, and engine-size expectations. No Paradox wiki web access was used.

Skills used:

- `imagegen`
- `chaos-redux-event-assets`
- `chaos-redux-subagents`

## Simplifications, omissions, and blockers

None. All requested families, variants, prompts, separate built-in calls, source masters, processed masters, runtime sizes, provenance records, contact sheets, and validations are present. No fallback or substitute asset was used.

No commit was created. The parent agent retains final review and commit ownership; no additional flag wiring is required because all engine-facing filenames were preserved.
