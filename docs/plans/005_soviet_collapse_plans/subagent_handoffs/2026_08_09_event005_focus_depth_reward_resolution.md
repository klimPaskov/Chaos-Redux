# Event 005 Focus Depth And Reward Resolution

Date: 2026-08-09

## Scope

This audit covers every national focus in the four active Event 005 files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

## Current Package

The package contains 43 trees and 1,760 focuses: 515 republic focuses, 1,035 custom-splinter focuses, 134 factory-successor focuses, and 76 ancient-restoration focuses.

The current per-tree counts are:

- Republics: Ukraine 83, generic breakaway 36, internal republics 76, Baltic 42, Caucasus 40, Central Asia 45, Moldova 48, Belarus 53, and Kazakhstan 92.
- Compact specialist splinters: FTH 47, UWR 14, KMB 16, PRA 22, ILX 18, IKX 18, DSC 18, NRF 18, and ICD 18.
- Full custom splinters: AEX, TNC, AAX, BBH, AOX, UDC, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, IMX, IUL, ADX, ARD, and NLC each have 47 focuses.
- Factory successors: CFR 47, IJX 29, and MFR 58.
- Ancient restorations: INX 20, SOG 20, ANX 20, and ABX 16.

Every tree contains at least three branch families and combines political, military, economic or logistical, diplomatic or expansion, and country-specific mechanic payoffs. The compact specialist trees use fewer nodes because their individual decisions, units, state mechanics, or shared crisis systems carry route depth outside the focus file; none uses a generic fallback tree.

## Reward Audit

The historical count of 1,127 shallow rewards came from a conservative text signature that classified any helper-only completion reward as shallow without expanding the helper. It was useful as a triage signal but was not semantic evidence.

The final audit parsed all 1,760 completion rewards, recursively expanded every reachable scripted effect, and required at least one material gameplay category beyond flags, variables, or a tooltip. Material categories included politics, forces, equipment, research, construction, territory, diplomacy, decisions or events, and strategic modifiers.

The first recursive pass found five remaining semantic leaf focuses:

- `AOX_radical_turn`
- `CFR_housing_as_discipline`
- `CFR_the_debt_map`
- `IJX_fortify_the_volga_crossings`
- `MFR_civilian_factory_rivalry`

Each received a route-specific visible payload and tooltip. The repeated audit result is:

- focus rewards checked: 1,760
- semantic leaf risks: 0

The previously identified Ukraine officer question, Baltic state question, and AAX Caspian survey outliers also have material command, recognition, intelligence, logistics, fuel, or construction payloads and player-facing tooltips.

## Structural And Localisation Evidence

- Duplicate focus IDs: 0.
- Missing focus title keys: 0.
- Missing focus description keys: 0.
- Every focus has an `ai_will_do` block.
- Unsupported or unscoped route fallbacks: 0.
- The obsolete pre-expansion UWR focus-plan sidecar was removed so it cannot be mistaken for the live fourteen-focus tree.

## Layout Gate And Final Art

The historical 520 pathline count is a superseded coordinate heuristic rather than a set of 520 live route defects. The completion procedure reserves one MCP compact rewrite across all 43 trees as the final source-changing operation, followed only by read-only inspect, render, and raster evidence. Because that rewrite is intentionally last, its generated artifact identifiers live in the MCP workspace cache and the final completion report rather than a later documentation edit.

The strict final icon audit covers all 1,760 focuses. Every focus now has its own sprite assignment and its own decoded texture hash. UWR and KMB retain 30 bespoke final icons; the other 1,730 focuses retain their authored base imagery and use distinct route-family accents plus one-to-one semantic medallions. All 43 tree contact sheets were visually reviewed. The manifest, processed previews, contact sheets, provenance, and exact hashes are recorded under `docs/assets/005_soviet_collapse/focus_icon_assignments/` and in the final icon handoff.
