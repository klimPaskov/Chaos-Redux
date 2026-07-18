# Event 019 Regional Flag Generation and Provenance

> **Historical and superseded (2026-07-18):** This note records the 7/16
> seven-motif/composite pipeline only. It is not the current regional flag
> source or runtime chain. The current source of truth is 91 independent
> built-in ImageGen full-flag raws -> 91 deterministic 820x520 spot-colour
> masters -> 273 native PNGs -> 273 bottom-left-origin runtime TGAs, with
> visual/runtime rows passing but independent remediation re-audit, workbook
> export, and final completion audit still pending. The old composite paths,
> validation records, checksums, and contact sheets are archival.

Date: 2026-07-16

## Result

The regional flag package contains exactly 91 cosmetic-tag identities:

- 13 existing Event 019 identity designs
- 7 regional secondary motifs
- 13 × 7 final region-aware tags
- 91 high-resolution source composites
- 273 processed PNGs across normal, medium, and small tiers
- 273 runtime TGAs across `gfx/flags/`, `gfx/flags/medium/`, and
  `gfx/flags/small/`

The exact runtime token is always:

```text
INFANTRY_SPAWN_<IDENTITY>_<REGION>
```

Identity stems:

```text
CLAIMANT_BREAKAWAY
ZOMBIE_BASE
ZOMBIE_CLAIMANT
ZOMBIE_COLLECTIVE
ZOMBIE_SPECIES
GHOST_BASE
GHOST_CLAIMANT
GHOST_COLLECTIVE
GHOST_SPECIES
GOLEM_BASE
GOLEM_CLAIMANT
GOLEM_COLLECTIVE
GOLEM_SPECIES
```

Region tokens:

```text
EUROPE
MIDDLE_EAST
AFRICA
ASIA
AUSTRALIA
NORTH_AMERICA
SOUTH_AMERICA
```

The original thirteen un-suffixed Event 019 cosmetic flags remain intact as
the identity precedents and current non-regional compatibility assets. They
were not replaced, recolored, deleted, or counted as substitutes for any of
the 91 regional tags.

## Authored source model

The package combines authored raster sources rather than drawing final flag
geometry locally:

1. The thirteen existing Event 019 ImageGen flag designs provide the stable
   claimant/family/route identity layer.
2. Seven new built-in ImageGen calls provide the regional secondary layer:
   split heraldic chevron, eight-point knot, stepped sun/spearhead,
   mountain-cloud gate, navigation star/wave, broken star/rail chevron, and
   condor-step/maize diamond.
3. The official ImageGen chroma-removal helper converts the seven frozen green
   sources to real alpha with soft matte, despill, and one-pixel edge
   contraction.
4. The retained Event 019 processor composites each authored regional motif in
   the fly-side badge position of every authored identity design.

No rectangle, circle, star, chevron, bird, mountain, wave, sun, spearhead,
knot, rail, or other visible emblem geometry is drawn by the local processor.
It performs alpha cleanup, subject containment, compositing, resizing, contact
sheet assembly, TGA export, hashing, and validation only.

The full prompt record and selected built-in output ids are in
`prompts/regional_flag_motif_prompts_2026_07_16.md`.

## Deterministic composition

Processor:

```text
docs/assets/019_infantry_spawn/_tooling/process_event_019_regional_flags.py
```

For every tag the processor writes:

- source composite: `source_png/flags/regional_variants/<TAG>_source.png`
  at 820 × 520 opaque RGBA
- processed normal: `processed_png/flags/<TAG>_normal.png` at 82 × 52
- processed medium: `processed_png/flags/<TAG>_medium.png` at 41 × 26
- processed small: `processed_png/flags/<TAG>_small.png` at 10 × 7
- final normal: `gfx/flags/<TAG>.tga`
- final medium: `gfx/flags/medium/<TAG>.tga`
- final small: `gfx/flags/small/<TAG>.tga`

Each native tier is composed against the already approved matching Event 019
identity tier. This preserves every base pixel outside the regional badge
instead of repeatedly scaling a single low-resolution derivative. The regional
motif uses a 22 × 22 normal badge, a 12 × 12 medium badge, and a 4 × 4 small
badge. The small tier deliberately keeps a strong 3–4-pixel heraldic mark; it
does not attempt to retain invisible interior ornament.

## Review and validation

Review sheets:

- `contact_sheets/event_019_regional_motif_source_contact_sheet.png`
- `contact_sheets/event_019_regional_flag_contact_sheet.png`
- `contact_sheets/event_019_regional_flag_small_readability_contact_sheet.png`

Machine-readable evidence:

- `regional_flag_validation_2026_07_16.json`
- `regional_flag_checksums_2026_07_16.sha256`

Validated results:

- 91/91 source composites exist at 820 × 520 in opaque RGBA mode.
- 273/273 processed PNGs have the exact native dimensions and opaque RGBA
  mode.
- 273/273 TGAs are uncompressed type-2, 32-bit, eight-alpha-bit,
  bottom-left-origin files with descriptor `8` and exact byte length.
- Pillow-decoded TGA pixels match the paired processed PNGs exactly.
- `file(1)` reports `Targa image data` for every TGA and reports no `- top`
  origin marker.
- All 91 tag images are hash-unique independently at 82 × 52, 41 × 26, and
  10 × 7.
- Every identity has seven distinct regional outputs at every size.
- Every regional variant differs from its identity base only inside the
  regional badge area; unchanged identity pixels remain identical.
- The regional badge changes 227–404 pixels at normal size, 81–129 at medium,
  and 9–16 at small. This is enough to remain visible without replacing the
  family/route motif.
- No chroma green survives on any final flag border.

Visual review of the 13 × 7 matrix confirms the claimant ledger, zombie tally/
crown/linked-host/spiral, ghost anchor/crown/chorus/moon-door, and golem rune/
builder/pattern/colossi motifs remain recognizable. The regional marks are
independent silhouettes and internal constructions, not palette swaps.

## Failures, fallbacks, and placeholders

No asset failed generation, chroma cleanup, composition, export, header
validation, pixel comparison, uniqueness validation, or visual review. No
fallback, placeholder, historical substitute, source recolor, primitive local
redraw, or transform-only stand-in was used.
