# Event 019 Regional Flag Assets Handoff

> **Historical and superseded (2026-07-18):** This handoff documents the
> retired 7/16 motif/composite production pipeline and its outputs. Do not use
> its `regional_variants/` paths, composite claims, or 7/16 validation/contact
> sheets as the current source. The current chain is 91 independent built-in
> ImageGen full-flag raws -> 91 deterministic 820x520 spot-colour masters ->
> 273 native PNGs -> 273 runtime TGAs. Visual/runtime rows pass, while
> independent remediation re-audit, workbook export, and final completion audit
> remain pending.

Date: 2026-07-16

Subagent scope: Event 019 region-aware derivative flag production only. No
gameplay, localisation, scripted effect, scripted trigger, script constant,
on-action, visual registry, or unrelated Event 006/015 asset file was edited.
No commit was created.

## Delivered matrix

The package contains exactly 91 regional cosmetic-tag identities: thirteen
identity stems crossed with seven region tokens.

Identity stems:

- `CLAIMANT_BREAKAWAY`
- `ZOMBIE_BASE`, `ZOMBIE_CLAIMANT`, `ZOMBIE_COLLECTIVE`, `ZOMBIE_SPECIES`
- `GHOST_BASE`, `GHOST_CLAIMANT`, `GHOST_COLLECTIVE`, `GHOST_SPECIES`
- `GOLEM_BASE`, `GOLEM_CLAIMANT`, `GOLEM_COLLECTIVE`, `GOLEM_SPECIES`

Region tokens:

- `EUROPE`
- `MIDDLE_EAST`
- `AFRICA`
- `ASIA`
- `AUSTRALIA`
- `NORTH_AMERICA`
- `SOUTH_AMERICA`

Exact token and filename contract:

```text
INFANTRY_SPAWN_<IDENTITY>_<REGION>
gfx/flags/INFANTRY_SPAWN_<IDENTITY>_<REGION>.tga
gfx/flags/medium/INFANTRY_SPAWN_<IDENTITY>_<REGION>.tga
gfx/flags/small/INFANTRY_SPAWN_<IDENTITY>_<REGION>.tga
```

The thirteen pre-existing un-suffixed identities remain untouched. They are
the stable claimant/family/route source designs and non-regional compatibility
flags, not substitutes for matrix rows.

## Art and provenance

Skills used:

- `chaos-redux-event-assets`
- official `imagegen`

The full canonical vanilla flag ladder and contact sheet were inspected before
production. The offline Country Creation flag section and installed vanilla
cosmetic-tag documentation were also consulted.

Seven separate built-in ImageGen calls created the regional secondary motifs:

| Region | Secondary motif |
| --- | --- |
| Europe | split heraldic chevron |
| Middle East | eight-point geometric knot |
| Africa | stepped sun and spearhead |
| Asia | mountain-cloud gate |
| Australia | navigation star and wave |
| North America | broken star and rail chevron |
| South America | condor-step and maize diamond |

The approved chroma-removal helper produced real-alpha motif masters. The
deterministic processor then composited each authored motif over each existing
authored identity. It does not draw or trace emblem geometry and does not
recolor the identity designs.

Provenance records:

- `docs/assets/019_infantry_spawn/prompts/regional_flag_motif_prompts_2026_07_16.md`
- `docs/assets/019_infantry_spawn/notes/regional_flag_generation_provenance_2026_07_16.md`

## Files created or updated

Source and processed assets:

- 7 ImageGen motif sources under
  `docs/assets/019_infantry_spawn/source_png/flags/regional_motifs/`
- 7 alpha-cleaned motif masters under
  `docs/assets/019_infantry_spawn/processed_png/flags/regional_motifs/`
- 91 source composites under
  `docs/assets/019_infantry_spawn/source_png/flags/regional_variants/`
- 273 native processed PNGs under
  `docs/assets/019_infantry_spawn/processed_png/flags/`
- 273 final TGAs under `gfx/flags/`, `gfx/flags/medium/`, and
  `gfx/flags/small/`

Review and evidence:

- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_motif_source_contact_sheet.png`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_flag_contact_sheet.png`
- `docs/assets/019_infantry_spawn/contact_sheets/event_019_regional_flag_small_readability_contact_sheet.png`
- `docs/assets/019_infantry_spawn/regional_flag_validation_2026_07_16.json`
- `docs/assets/019_infantry_spawn/regional_flag_checksums_2026_07_16.sha256`
- `docs/assets/019_infantry_spawn/_tooling/process_event_019_regional_flags.py`

Documentation aligned:

- `docs/assets/019_infantry_spawn/manifest.md`
- `docs/assets/019_infantry_spawn/gfx_handoff.md`

## Validation evidence

- 91/91 source composites are 820 × 520 opaque RGBA PNGs.
- 91/91 normal, 91/91 medium, and 91/91 small processed PNGs match 82 × 52,
  41 × 26, and 10 × 7 respectively.
- 273/273 runtime files are uncompressed type-2, 32-bit, eight-alpha-bit,
  bottom-left-origin TGAs with descriptor `8` and exact byte length.
- `file(1)` identifies every final as Targa data and reports no `- top` marker.
- Every TGA decodes pixel-identically to its paired PNG.
- Every PNG/TGA is fully opaque in its runtime flag canvas; the seven motif
  masters retain real transparency for composition.
- All 91 tags are independently hash-unique at normal, medium, and small size.
- Each identity's seven regional variants remain distinct at 10 × 7.
- The regional badge alters only 227–404 pixels at normal size, 81–129 at
  medium, and 9–16 at small; every pixel outside the badge retains the approved
  base identity.
- The two regional contact sheets were visually reviewed across all thirteen
  rows. Family/route motifs remain recognizable and every normal-size regional
  emblem has a distinct silhouette and internal construction.

Current repository consumers already match the asset contract: the derivative
package effect builds `INFANTRY_SPAWN_[IDENTITY]_[REGION]`, and all 91 primary
regional localisation keys are present. Those files were inspected read-only
and were not changed by this handoff.

## Registry invariant

No registry file was created or edited. Runtime flags are resolved by cosmetic
tag filename and do not require a `.gfx` definition or a separate cosmetic-tag
registry. The Event 019 single-registry-code-file invariant is unchanged.

## Asset failures, fallbacks, simplifications, and blockers

None. All seven motif generations, chroma removals, 91 compositions, 273 TGA
exports, uniqueness checks, header checks, pixel comparisons, and visual
reviews succeeded. No placeholder, fallback, historical substitute, primitive
local redraw, recolor-only variant, or weaker substitute was used.
