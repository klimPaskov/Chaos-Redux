# Achievement asset workflow skill update

Date: 2026-08-24.

## Changed files

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/achievement_template.png` is the exact user-supplied completed-state background, SHA-256 `248DB006611EB3942550C43DF83802AA6FB24761035FC928B5D34586C0C4C5BA`.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/achievement_template_grey.png` is the exact user-supplied grey and not-eligible background, SHA-256 `70E073694C1A7D9FE40C63B1EB2E987A8A45B3FFD15CCF789EEAA5B843B90022`.
- The authoritative source files were `C:/Users/klimp/Downloads/achievement_template.png` and `C:/Users/klimp/Downloads/achievement_template_grey.png`; repository copies were hash-checked byte-for-byte.
- `.agents/skills/chaos-redux-event-assets/tools/process_achievement_icons.py` now preserves complete native 64x64 state triplets, accepts mixed current DDS inputs, writes strict canonical DDS triplets, and supports explicit, directory, dry-run, and audit modes.
- `.agents/skills/chaos-redux-event-assets/SKILL.md` now requires the native unchanged-state-layer contract, complete triplets, strict output layout, mixed-DDS fallback behavior, explicit source/output separation, and the narrow templated-border rerun guard.
- `.agents/skills/chaos-redux-event-assets/tools/README.md` documents the same processor contract and commands.
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/README.md` and `CATALOG.md` document both user-provided backgrounds, the existing unchanged overlay, provenance, hashes, and exclusion from achievement reference counts and contact sheets.

## Exact behavior

The normal migration input is a complete `<achievement_id>`, `<achievement_id>_grey`, and `<achievement_id>_not_eligible` triplet from one directory, or all three explicit state paths for one triplet.

Every decoded source state must be exactly 64x64 and is retained at its native canvas and exact position without resizing, cropping, alpha-trimming, grayscale conversion, recoloring, redrawing, filtering, or other preprocessing.

Completed output is the supplied completed background beneath the unchanged completed state layer.

Grey output is the supplied grey background beneath the unchanged `_grey` state layer.

Not-eligible output is the supplied grey background beneath the unchanged `_not_eligible` state layer.

Normal alpha compositing is the only pixel interaction between a background and its state layer, so an opaque custom source background may hide the supplied bottom layer.

The existing red `overlay.png` remains available as an unchanged asset for future source-triplet creation, but this migration never rebuilds or replaces a supplied not-eligible layer from grey plus overlay.

The strict legacy BGRA DDS parser runs first for DDS sources.

When strict parsing rejects compressed, mipped, noncanonical, or truncated current DDS, `_load_rgba` falls back to Pillow with `ImageFile.LOAD_TRUNCATED_IMAGES = True` enabled only during that decode and validates a successful nonzero decode before the 64x64 state check.

Final outputs and audits remain strict one-level uncompressed BGRA DDS files with 64x64 dimensions and exact 16512-byte length.

The processor imports the repository `write_bgra_dds` writer and validates each output against the exact expected background-underlay composition.

Separate output is required by default, existing outputs require `--force`, and intentional replacement beside source files requires `--in-place --force`.

The processor refuses a source state triplet whose unchanged six-pixel outer template border is detected, where that heuristic is applicable, and reports `--allow-templated-sources` as the explicit override for intentional reprocessing.

## Task-specific validation

- The four current runtime input classes were exercised without writing runtime files.
- `16512` bytes: `gfx/achievements/000_chaos_redux_00_calm_before_the_storm.dds` and its state companions used the strict parser and wrote/audited a canonical triplet under `C:\Users\klimp\AppData\Local\Temp\chaosx_achievement_workflow_20260824_preserve\out_16512`.
- `21972` bytes: `gfx/achievements/003_holy_realm_debate_the_pretender.dds` and its noncanonical companions used the Pillow fallback where required and wrote/audited a canonical triplet under `...\out_21972`.
- `2872` bytes: `gfx/achievements/007_fury_firebreak.dds` and its compressed companions used the Pillow fallback where required and wrote/audited a canonical triplet under `...\out_2872`.
- `16511` bytes: `gfx/achievements/005_soviet_collapse_concrete_does_not_sleep.dds` and its truncated/noncanonical companions used the Pillow fallback where required and wrote/audited a canonical triplet under `...\out_16511`.
- Independent validation decoded all twelve outputs with the strict parser, confirmed 64x64 dimensions, exact 16512-byte lengths, and exact equality to `alpha_composite(background, decoded original state layer)` for every state.
- The opaque completed state in `000_chaos_redux_00_calm_before_the_storm.dds` remained pixel-identical after composition because its top layer is fully opaque.
- The explicit three-path CLI wrote and audited `explicit_probe_20260824` under `...\explicit_20260824`.
- A bulk directory dry-run over all 335 current base DDS triplets succeeded without writing runtime files, and an incomplete temporary triplet without `_not_eligible` failed closed with the expected missing-state error.
- A synthetic temporary triplet exposing the unchanged template border failed closed with the rerun guard; the explicit override is available for intentional exceptions.

## Skipped checks and remaining risks

No runtime `gfx/achievements/`, `interface/`, `common/achievements/`, localisation, spreadsheet, or existing reference/contact-sheet files were edited by this workflow change.

Live game validation and runtime sprite wiring remain with the parent agent and user.

MCP inspection was not applicable to this asset-only skill and tool change.

The templated-border guard is heuristic and intentionally does not reject opaque custom state layers whose border differs from the supplied template; source/output directory separation and explicit in-place mode remain the primary rerun safety controls.

The source fallback is intentionally broader than final output validation, and Pillow decoder support remains dependent on the installed Pillow build for future DDS variants.

No commit was created, per task scope.
