# Event 015 corrected identity-asset workflow and regeneration handoff

Date: `2026-07-15`

Scope: active route flags, four institutional leader portraits, sixteen advisor icons, their reusable processing workflow, current runtime wiring, and visual validation

## Outcome

The active Event 15 identity package satisfies the corrected visual contract.

- All active route flags originate in built-in ImageGen. The generated heraldry remains visible through normal, medium, and small HOI4 lookup sizes; no solid-fill normalization, aggressive quantization, vector tracing, primitive redraw, motif substitution, or palette ceiling replaces the generated design.
- All four leader portraits are people-free institutional tableaux. They depict the establishment through empty chambers, council tables, ledgers, standards apparatus, stores, seals, and route emblems. They contain no people, faces, heads, bodies, hands, crowds, silhouettes, statues, busts, mannequins, framed portraits, photographs, or human shadows.
- All sixteen advisor icons begin with independent fictional ImageGen portrait masters. Separate built-in ImageGen frame and paper/seal overlays supply the dossier card artwork. The processing script only performs crop, grade, angle, alpha-shadow derivation, composition, validation, and export.
- Existing character IDs, cosmetic tags, sprite handles, and runtime paths remain stable. No placeholder, generic portrait, shape-built flag, or script-drawn advisor card is active.

## Reusable workflow correction

The reusable rules are recorded in:

- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/README.md`
- `assets/vanilla_reference/portraits/advisors/`
- `assets/vanilla_reference/portraits/leaders/`

The skill now treats flags as flat identity designs and assets rather than scene artwork while still requiring ImageGen authorship and preservation of generated heraldic detail. It separately defines the advisor master-plus-overlay workflow and the people-free institutional-leader workflow.

`.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py` is version 2.0. Advisor mode requires both `--advisor-frame-overlay` and `--advisor-paper-overlay`. Its metadata contract is:

`crop_grade_angle_alpha_shadow_composite_export_only; no programmatically drawn advisor-card artwork`

Leader mode records:

`crop_grade_export_only; no programmatically drawn leader subject, emblem, or institutional scene`

The script does not synthesize visible card borders, paper, seals, emblems, institutional scenes, or leader subjects.

## Route flags

The five active identity families have 21 independent ImageGen designs and four intentional unsuffixed engine-lookup aliases. Each of the 25 lookup stems exists at `82x52`, `41x26`, and `10x7`, for 75 runtime TGAs under:

- `gfx/flags/`
- `gfx/flags/medium/`
- `gfx/flags/small/`

The four aliases are:

- Voluntary Commonwealth unsuffixed to democratic
- Council Union unsuffixed to communism
- Planned Utopia unsuffixed to neutrality
- Closed Island unsuffixed to fascism

The Practical Commonwealth unsuffixed design is independent. Exact accepted ImageGen handles, hashes, source dimensions, aliases, processed hashes, and runtime hashes are recorded in:

- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/prompts/corrected_flag_and_institutional_prompts_2026_07_15.md`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/flag_identity_asset_records.json`
- `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/asset_records.json`

`build_identity_flag_variants.py` performs aspect fit, restrained contrast and colour finishing, mild unsharp treatment, RGBA export, source-preservation RMS validation, and size-specific output. It does not quantize, collapse to solid fills, trace, redraw, or enforce a palette ceiling.

Visual review evidence:

- `contact_sheets/flags_corrected_decoded_contact_sheet.png`
- `contact_sheets/flags_corrected_small_10x7_readability_contact_sheet.png`
- `contact_sheets/flag_imagegen_source_normal_medium_small_comparison.png`

All paths above are under `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/`.

## Advisor dossier icons

The sixteen roles each have a distinct built-in ImageGen fictional portrait master. The shared generated overlay kit contains:

- frame overlay: `exec-e3c2e24d-4275-41ba-a25c-bdbfdb2a94ff`
- paper and seal overlay: `exec-44055cbe-b80e-4e91-9f84-b47e46ded6c8`

Overlay sources and their manifest live under:

`.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/`

The approved role-master handles, prompts, hashes, crop metadata, package paths, and runtime paths are recorded in the route-identity prompt and asset-record files. Runtime DDS files remain at:

`gfx/leaders/015_utopia_manifesto/advisors/*.dds`

All sixteen are `65x67`. They were reviewed at native size and nearest-neighbour enlargement in:

`docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png`

`advisor_validation_2026_07_15.json` validates the complete corrected set. It resolves the recorded built-in ImageGen objects from the local generated-image store, requires exact byte equality for all sixteen portrait masters and both overlay masters, verifies the overlay manifest hashes, and then validates source, processed, package, and runtime relationships.

## People-free institutional leaders

The four current ImageGen source handles are:

| Institution | Built-in ImageGen handle | Runtime texture |
| --- | --- | --- |
| Household Assembly | `exec-117c963f-9206-4364-b717-7ccc445eb02a` | `gfx/leaders/015_utopia_manifesto/leader_household_assembly.dds` |
| Council of Callings | `exec-cf3a6e16-ae0a-47d7-b0d2-ac80159b3939` | `gfx/leaders/015_utopia_manifesto/leader_council_of_callings.dds` |
| Board of Measure | `exec-dda8c28b-0625-4bd7-a686-65afef28a489` | `gfx/leaders/015_utopia_manifesto/leader_board_of_measure.dds` |
| Stewardship Council | `exec-b5e1e53d-ed19-4d3b-9baa-c2edb1dfc0a3` | `gfx/leaders/015_utopia_manifesto/leader_stewardship_council.dds` |

Each output is `156x210`, uses `source_kind = symbolic`, and preserves the full institution tableau. Eight founder and successor entries share the four portraits only where they represent the same durable institution.

Visual review evidence:

`docs/assets/015_utopia_manifesto/route_identity_2026_07_14/contact_sheets/institutional_portraits_corrected_processed_contact_sheet.png`

## Runtime registry cleanup

The obsolete registrations for the unused Boundary Crisis news image and the two superseded two-image super-event assets were removed from `interface/015_utopia_manifesto.gfx`. Their files remain historical provenance and are not runtime fallbacks.

Current registry proof:

- 422 definitions in `interface/015_utopia_manifesto.gfx`
- 5 route-super-event definitions in `interface/015_utopia_manifesto_super_event.gfx`
- 427 total Event 15 registrations
- 0 duplicate sprite names
- all registered texture paths resolve

## Validation evidence

- `verify_imagegen_source_evidence.py`: 25 independent packaged sources exactly match built-in ImageGen output bytes: 21 flags and 4 institutional tableaux.
- `flag_identity_validation_2026_07_15.json`: 25 lookup stems, 75 runtime TGAs, 21 independent main-size hashes, and four exact aliases; no quantization, tracing, primitive redraw, motif substitution, or palette ceiling.
- `advisor_validation_2026_07_15.json`: all 16 corrected advisor dossier icons validate at `65x67`; all 16 recorded portrait masters and both generated overlay masters exactly match their recorded built-in ImageGen objects.
- `validation.json`: 100 runtime route-identity outputs validate: 75 flags, 4 institutional leaders, 16 advisors, and 5 League emblems.
- `final_icon_frame_audit.json`: all 427 current Event 15 registrations resolve with zero duplicate sprite names.
- `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`, the flag processor, and the asset validators compile or execute successfully; the skill validator passes.

## Files changed

- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/assets/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/**`
- `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`
- `assets/vanilla_reference/portraits/advisors/`
- `assets/vanilla_reference/portraits/leaders/`
- `gfx/flags/UTOPIA_MANIFESTO_*.tga`
- `gfx/flags/medium/UTOPIA_MANIFESTO_*.tga`
- `gfx/flags/small/UTOPIA_MANIFESTO_*.tga`
- `gfx/leaders/015_utopia_manifesto/leader_*.dds`
- `gfx/leaders/015_utopia_manifesto/advisors/*.dds`
- `interface/015_utopia_manifesto.gfx`
- corrected sources, processed files, records, manifests, validation JSON, contact sheets, prompts, and tooling under `docs/assets/015_utopia_manifesto/route_identity_2026_07_14/`
- current Event 15 asset manifest, GFX handoff, event documentation, coverage matrix, and resume packet

## Simplifications, omissions, and blockers

- Simplifications: none.
- Fallbacks: none.
- Missing requested identity assets: none.
- Unwired requested identity assets: none.
- Placeholder or generic identity art: none.
- The project-wide Event 15 completion gate remains separate from this completed asset correction.
