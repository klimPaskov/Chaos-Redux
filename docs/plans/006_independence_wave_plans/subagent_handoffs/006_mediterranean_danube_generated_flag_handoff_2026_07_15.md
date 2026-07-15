# Event 006 Mediterranean and Danube generated-flag handoff

## Assignment and mode

- Agent role: bounded generated-event-art asset tranche.
- Skills used: `chaos-redux-event-assets`, `chaos-redux-subagents`, and the
  official `imagegen` skill.
- Scope: IW-018 Sardinia/ARX, IW-019 Sicily/ASX, IW-021 Trieste/ICX; preserve
  IW-024 Banat/AXX as blocked.
- Mode: create official-ImageGen-derived source masters, deterministic HOI4 TGA
  ladders, contact sheets, provenance, attribution, hashes, and a wiring
  handoff. Gameplay and localisation were outside scope.
- Commit: none, as requested.

## Files and identifiers handed off

Runtime identifiers are the exact HOI4 flag filenames:

- `gfx/flags/ARX.tga`, `gfx/flags/medium/ARX.tga`,
  `gfx/flags/small/ARX.tga`;
- `gfx/flags/ASX.tga`, `gfx/flags/medium/ASX.tga`,
  `gfx/flags/small/ASX.tga`;
- `gfx/flags/ICX.tga`, `gfx/flags/medium/ICX.tga`,
  `gfx/flags/small/ICX.tga`.

The complete source, processed, review, and build package is:

`docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/`

Key files inside it:

- `manifest.md`;
- `gfx_handoff.md`;
- `prompts/imagegen_prompts.md`;
- `build_flags.py`;
- `hashes.sha256`;
- `notes/validation.json`;
- `source_png/` with three selected raw ImageGen outputs, three deterministic
  flat masters, and both rejected Trieste edit outputs;
- `processed_png/{normal,medium,small}/`;
- `contact_sheets/006_mediterranean_danube_imagegen_raw_vs_flat_contact_sheet.png`;
- `contact_sheets/006_mediterranean_danube_final_tga_ladders_contact_sheet.png`.

## Delivered design behavior

| Tag | Delivered behavior | Historical/design boundary |
|---|---|---|
| `ARX` | white field, edge-reaching red St George cross, four black heads facing inward, forehead bands above open eyes | approved fictional 1936 Sardinian civic synthesis; never describe as an attested sovereign flag |
| `ASX` | equal green/ecru/red vertical bands and one all-gold Trinacria, normalized with one leg down | 1848 S.015 constitutional-independence route only; not a neutral or universal Sicilian baseline |
| `ICX` | civic-red field and one centered upright white/silver corsesca | grounded in the 1918-1936 Triestine civic design; ratio, digital red, and selected ImageGen device proportion are production normalizations |
| `AXX` | no output | blocked because no attested Banat Republic flag or approved synthesis exists |

No ideology variants were produced because no approved ideology-to-design or
cosmetic-tag mapping exists. This follows the existing Event 006 unsuffixed
flag-family precedent without inventing generic overlays.

## Trieste selection evidence

The licensed auxiliary layout aid's light charge measures 59.9% of field height
and 23.8% of field width. The selected first ImageGen result measures 67.3% by
24.7% and retains one long top spear, exactly two upward-curving side blades, a
compact joint, and a short lower shaft. Two official edit attempts were retained
but rejected:

- undersized edit: 46.9% by 18.4%;
- oversized edit: 74.7% by 28.3%.

The first result was retained as the closest overall reviewed output. No manual
charge scaling, SVG substitution, or locally drawn fallback was used. The
height difference remains explicitly disclosed for parent review.

## Validation evidence

- The two contact sheets were reviewed against the research aids and reopen the
  actual final TGA ladders.
- `notes/validation.json` records all nine runtime dimensions, alpha, image
  type, pixel depth, bottom-left origin, exact byte length, and equality between
  decoded TGAs and processed PNGs.
- The 10x7 ladder retains the defining cross/head layout, tricolour/Trinacria,
  and corsesca charge through documented source-cell coverage thresholds rather
  than new geometry.
- `hashes.sha256` inventories the cited inputs, all selected and rejected
  ImageGen sources, processed outputs, runtime TGAs, contact sheets, and QA
  report.

## Main-agent follow-up

1. Review the contact sheets and manifest classifications.
2. Decide whether ASX exists only on the constitutional route or needs a named
   cosmetic tag; do not use S.015 as a neutral baseline.
3. Wire ARX, ASX, and ICX country/route logic without changing the declared
   identity boundaries.
4. Keep AXX blocked and absent.
5. Align country docs, event docs, localisation, and any spreadsheet fields
   only after the route decisions and country implementation facts exist.
6. Retain final completion ownership and do not treat this asset handoff as
   proof that a country package or Event 006 is complete.

## Simplifications, omissions, and blockers

- AXX is deliberately omitted and remains blocked.
- Ideology and cosmetic variants are deliberately omitted because ownership is
  unapproved.
- ASX is `needs_user_review` until the constitutional-route mapping is resolved.
- ICX retains the closest compliant official ImageGen result even though its
  charge is taller than the auxiliary layout aid; both failed proportion edits
  are retained and documented.
- No fallback, placeholder, manual vector reconstruction, gameplay edit,
  localisation edit, country edit, or commit was made.
