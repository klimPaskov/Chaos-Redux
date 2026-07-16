# Event 006 IW-010 Saar advisor and focus asset manifest

Date: `2026-07-15`

Event: `006_independence_wave`

Package: `IW-010` Saar (`AJX`)

Source mode: official built-in ImageGen (`$imagegen`)

Disclosure: all three depicted advisors are distinct fictional humans.

Asset status: `wired_and_verified` — runtime DDS files are installed at the
exact approved paths and the parent-owned character, localisation, recruitment,
sprite, shine, and focus-entry registrations have been verified in the live
Event 006 files. This asset tranche did not edit those parent-owned surfaces.

## Asset contract

The advisor outputs are native `65x67` HOI4 dossier cards, not leader or army
portraits. ImageGen created three independent full-resolution fictional human
masters. Each received its own explicit head-and-shoulders crop through
`.tools/process_hoi4_portrait.py advisor`, using the approved ImageGen-authored
frame and paper overlays from
`.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/`.
Neither Friedrich Hoffmann nor Karl Becker was cropped or reused. The approved
RHI and BAY portraits were not opened for editing or changed.

The focus output is one original `94x86` Event 006 focus icon. ImageGen created
the civic-scale, municipal-hall, rail, coal, and Saar-color composition on a
flat chroma field. The official ImageGen chroma helper produced real alpha;
mechanical finishing only cropped the visible bounds, resized the authored
emblem, and centered it on the existing Event 006 focus canvas. No symbol,
frame, seal, or visible detail was drawn locally.

## Advisor inventory

| Stable stem | Fictional human role | Apparent gender | Explicit crop `[left, top, right, bottom]` | Source size | Approved parent character key | Exact sprite handle | Installed runtime DDS |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| `advisor_AJX_independence_wave_mine_rail_dispatch_superintendent` | mine-and-rail dispatch superintendent; precise civilian logistics specialist | female-presenting | `[135, 35, 945, 1130]` | `1081x1455` | `AJX_independence_wave_mine_rail_dispatch_superintendent` | `GFX_portrait_advisor_AJX_independence_wave_mine_rail_dispatch_superintendent` | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds` |
| `advisor_AJX_independence_wave_cross_border_accounts_comptroller` | cross-border accounts comptroller; exacting municipal contract specialist | male-presenting | `[145, 40, 960, 1145]` | `1081x1455` | `AJX_independence_wave_cross_border_accounts_comptroller` | `GFX_portrait_advisor_AJX_independence_wave_cross_border_accounts_comptroller` | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds` |
| `advisor_AJX_independence_wave_factory_security_inspector` | factory-security inspector; civilian auditor of private guard companies | female-presenting | `[130, 35, 960, 1145]` | `1082x1454` | `AJX_independence_wave_factory_security_inspector` | `GFX_portrait_advisor_AJX_independence_wave_factory_security_inspector` | `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds` |

The live records for the mine-and-rail superintendent and factory-security
inspector use `gender = female`; the accounts comptroller uses the male default.
The stable keys are institutional role keys, but every image depicts one
specific plausible 1930s human specialist, not a council, office, seal, or
generic institution.

## Focus inventory

| Stable stem | Intended use | Target | Exact approved sprite | Installed runtime DDS | Parent integration status |
| --- | --- | ---: | --- | --- | --- |
| `goal_independence_wave_ajx_neutral_commission` | distinct Municipal Neutral Commission route-entry focus | `94x86` | `GFX_goal_independence_wave_ajx_neutral_commission` | `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds` | sprite and shine registered; assigned to `independence_wave_ajx_appoint_neutral_commission_focus` |

The matching shine handle
`GFX_goal_independence_wave_ajx_neutral_commission_shine` is registered beside
the base sprite. The dedicated icon anchors the route-entry focus. The live
tree intentionally retains recognition-diplomacy, army-integration, and
founding-administration icons on the codification, security, and entrenchment
subnodes respectively.

## Source and processed paths

For every advisor `<stem>`:

- prompt: `prompts/ajx_asset_prompts.md`;
- raw ImageGen master: `source_png/imagegen_raw/<stem>_imagegen_raw.png`;
- processed native PNG: `processed_png/advisors/<stem>.png`;
- processor metadata: `metadata/crops/<stem>.json`;
- processor comparison: `contact_sheets/advisor_reviews/<stem>_processor_comparison.png`;
- all-three canonical comparison:
  `contact_sheets/canonical_all_three/<stem>_canonical_all_three.png`;
- package DDS mirror: `final_dds/advisors/<stem>.dds`;
- decoded verification PNG: `decoded_png/advisors/<stem>.png`.

For the focus icon:

- prompt: `prompts/ajx_asset_prompts.md`;
- raw ImageGen master:
  `source_png/imagegen_raw/goal_independence_wave_ajx_neutral_commission_imagegen_raw.png`;
- alpha-processed master:
  `source_png/alpha_processed/goal_independence_wave_ajx_neutral_commission_alpha_master.png`;
- processed native PNG:
  `processed_png/focus/goal_independence_wave_ajx_neutral_commission.png`;
- processing metadata:
  `metadata/focus/goal_independence_wave_ajx_neutral_commission.json`;
- comparison sheet:
  `contact_sheets/focus/goal_independence_wave_ajx_neutral_commission_comparison.png`;
- package DDS mirror:
  `final_dds/focus/goal_independence_wave_ajx_neutral_commission.dds`;
- decoded verification PNG:
  `decoded_png/focus/goal_independence_wave_ajx_neutral_commission.png`.

## Canonical and project references

Advisor processing was reviewed against all three canonical dossier cards:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/generic_europe_1.png`;
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/generic_female_europe.png`;
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/generic_asia_1.png`.

The focus was reviewed against every canonical national-focus example and
against Event 006's founding-administration, recognition-diplomacy, and
infrastructure-authority runtime icons. The existing project family uses a
`94x86` canvas, which takes precedence over the canonical vanilla examples'
`100x88` source canvases for this registered Event 006 path.

## Runtime hashes and DDS evidence

| Runtime file | SHA-256 | Header/alpha result |
| --- | --- | --- |
| `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds` | `e2a8e4d56c9bd23ded9d07ec48fd3943e9da2a6a88cc0a6a7d8ea3a27d48bd5a` | valid one-level `65x67` BGRA, alpha `0..255`, `17,548` bytes |
| `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds` | `a58836ebcb8c4b2af6dd82b2dda060b1cdf2c40cd18233bf98bdc271c189e22e` | valid one-level `65x67` BGRA, alpha `0..255`, `17,548` bytes |
| `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds` | `4c7a956a9f45005ac130bb1d6f3e965b3f32ba92237ec238775b445d745b3f80` | valid one-level `65x67` BGRA, alpha `0..255`, `17,548` bytes |
| `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds` | `06063478a0d1a4e0cd562e1230f31cfa46eeb718814f11bcb83e86b6c059b613` | valid one-level `94x86` BGRA, alpha `0..255`, `32,464` bytes |

Every runtime DDS is byte-identical to its package mirror. Reopening the actual
DDS yields pixels identical to the processed PNG. All four corners are fully
transparent. The focus alpha master contains no surviving high-green fringe
pixels under the recorded validation rule.

## Review evidence

- source masters: `contact_sheets/advisor_sources_contact_sheet.png`;
- advisor native size: `contact_sheets/advisor_portraits_native_contact_sheet.png`;
- advisor 5x nearest: `contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png`;
- decoded DDS: `contact_sheets/advisor_portraits_decoded_contact_sheet.png`;
- per-advisor canonical comparisons: `contact_sheets/canonical_all_three/`;
- focus native/enlarged/canonical/project comparison: `contact_sheets/focus/`;
- combined handoff view: `contact_sheets/ajx_asset_completion_contact_sheet.png`;
- machine-readable evidence: `ajx_asset_validation_2026_07_15.json`;
- full SHA-256 inventory: `checksums.sha256`;
- verified sprite and character handoff: `gfx_handoff.md`;
- final file-by-file completion record: `handoff.md`.

## Source and rights note

The four source masters are original fictional ImageGen outputs created for
Chaos Redux. Canonical vanilla references and the shared generated dossier
overlays remain review/processing inputs only and are not copied as standalone
Chaos Redux art.

## Simplifications, omissions, fallbacks, and blockers

- Simplifications: none.
- Fallback art: none.
- Reused leader, commander, RHI, or BAY art: none.
- Placeholder or institution-only advisor portraits: none.
- Missing requested source, processed PNG, DDS, metadata, or contact-sheet
  evidence: none.
- Remaining asset integration work: none. Parent-owned AJX character,
  localisation, recruitment, portrait-sprite, focus-sprite, shine, and
  route-entry assignment are present at the verified paths recorded in
  `gfx_handoff.md`.
- Readiness gates and FORM-04 completion remain outside this bounded asset
  tranche; no gameplay-readiness claim is made here.
